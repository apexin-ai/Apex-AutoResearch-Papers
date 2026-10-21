# paper writing discussion d097

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_discussion_d097_20260522T054615.log`
- **Structured JSON:** [`77d6c893eb22140898ec.json`](../../sessions/77/77d6c893eb22140898ec.json)

## Before a recorded user message

22 recorded events

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
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
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
  "uuid": "ca54a18c-fa95-40e2-be4f-a07831671bfd",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779444600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c94555d5-4905-4974-b75d-d60fdac73360",
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "766a4d4f-bb60-482f-bd5f-3f149e8f0128",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8yMZBsZKzWdyQJDw1ynoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13107,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13107
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

<details open><summary>🔧 Tool call — Read · `toolu_01VPGJWmJ5wASPUReoqKr4jg`</summary>

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
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "cf46326d-686a-4deb-b17d-5aed4e90427a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8yMZBsZKzWdyQJDw1ynoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13107,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13107
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

_source line 6 · 2026-05-22T05:46:25.115Z_

<details><summary>↩ Tool result · `toolu_01VPGJWmJ5wASPUReoqKr4jg`</summary>

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
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "e6f07170-a7a0-42b0-9ef2-75d0227761cb",
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

<details open><summary>🔧 Tool call — Read · `toolu_01KRQ3Dksqqg337wuzetwL8c`</summary>

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
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "f81c932d-129d-4039-879d-a29977a193e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8yMZBsZKzWdyQJDw1ynoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13107,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13107
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

_source line 8 · 2026-05-22T05:46:25.453Z_

<details><summary>↩ Tool result · `toolu_01KRQ3Dksqqg337wuzetwL8c`</summary>

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
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "7fbccbcd-950c-41a9-8a04-029bb3a63032",
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

<details open><summary>🔧 Tool call — Read · `toolu_011bubBDGTagGBY4Zc4Jx45g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "177e5a86-7d7a-4b45-b2cb-f57f400e7607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8yMZBsZKzWdyQJDw1ynoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13107,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13107
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

_source line 10 · 2026-05-22T05:46:25.957Z_

<details><summary>↩ Tool result · `toolu_011bubBDGTagGBY4Zc4Jx45g`</summary>

```text
1	\vspace{-2pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Synthesis.}
6	VLA fine-tuning redistributes instruction attention rather than reshaping visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$), explaining Grant et al.'s~\cite{grant2026} visual dominance finding ($\rho = 0.692$ for DINOv2, yet readout $R^2 = 0.678$ vs.\ $0.634$).
7	Cross-architecture comparison strengthens this picture: two VLAs with different backbones and opposite untrained profiles both arrive at similar mid-layer peaks ($\Delta = 0.003$), suggesting the redistribution reflects task-structure constraints rather than architecture-specific artifacts.
8	Seven analyses support L1 redistribution: \emph{interventional} (dose-response $d = 0.48 \to 0.64$; counterfactual $d = 0.71$--$0.98$, replicating across both LIBERO suites), \emph{supporting} (gradient $0 \to 9 \to 24$ heads; ablation $+0.059$; trajectory $d = 0.65$), and \emph{constraining} ($p = 0.0018$; $z = -3.11$, $0$\textsuperscript{th} percentile; Appendix~\ref{sec:mechanistic_interpretation}--\ref{sec:functional_stages}).
9	
10	\subsection*{Limitations}
11	We analyze two causal-decoder VLAs on held-out LIBERO (Goal and Spatial, 10 tasks each); extending to flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} VLAs with cross-attention, and to benchmarks with richer language grounding (e.g., CALVIN, Language-Table), is needed to test generality.
12	Llama-2's 9/32 pretrained instruction-dominant heads may reflect text bias ($+15$-head delta isolates fine-tuning); we analyze only the final checkpoint, preventing characterization of routing emergence dynamics.
13	All analyses are open-loop~\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence, though consistent mid-layer peaks suggest early-exit inference at ${\sim}1/3$ depth as a testable hypothesis.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "5fd2ceb5-fa8b-4983-a098-3239c6486036",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\vspace{-2pt}\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning redistributes instruction attention rather than reshaping visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$), explaining Grant et al.'s~\\cite{grant2026} visual dominance finding ($\\rho = 0.692$ for DINOv2, yet readout $R^2 = 0.678$ vs.\\ $0.634$).\nCross-architecture comparison strengthens this picture: two VLAs with different backbones and opposite untrained profiles both arrive at similar mid-layer peaks ($\\Delta = 0.003$), suggesting the redistribution reflects task-structure constraints rather than architecture-specific artifacts.\nSeven analyses support L1 redistribution: \\emph{interventional} (dose-response $d = 0.48 \\to 0.64$; counterfactual $d = 0.71$--$0.98$, replicating across both LIBERO suites), \\emph{supporting} (gradient $0 \\to 9 \\to 24$ heads; ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} ($p = 0.0018$; $z = -3.11$, $0$\\textsuperscript{th} percentile; Appendix~\\ref{sec:mechanistic_interpretation}--\\ref{sec:functional_stages}).\n\n\\subsection*{Limitations}\nWe analyze two causal-decoder VLAs on held-out LIBERO (Goal and Spatial, 10 tasks each); extending to flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} VLAs with cross-attention, and to benchmarks with richer language grounding (e.g., CALVIN, Language-Table), is needed to test generality.\nLlama-2's 9/32 pretrained instruction-dominant heads may reflect text bias ($+15$-head delta isolates fine-tuning); we analyze only the final checkpoint, preventing characterization of routing emergence dynamics.\nAll analyses are open-loop~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence, though consistent mid-layer peaks suggest early-exit inference at ${\\sim}1/3$ depth as a testable hypothesis.\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01WpLatv36XiK3z5rxeV6YXG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "2018cbd3-29f2-4b16-8e13-402e0a1bd621",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8yMZBsZKzWdyQJDw1ynoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13107,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13107
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

_source line 12 · 2026-05-22T05:46:26.447Z_

<details><summary>↩ Tool result · `toolu_01WpLatv36XiK3z5rxeV6YXG`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We analyze three VLA architectures across four LIBERO~\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon) in a $3 \times 4$ cross-architecture matrix (Table~\ref{tab:cross_arch_matrix}).
8	The architectures span distinct backbone families: OpenVLA~\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\cite{touvron2023_llama2}, 32 layers, 32 MHA heads), TracVLA~\cite{zheng2024tracevla} (Phi-3-mini~\cite{abdin2024phi3}, 32 layers, 32 heads), and NORA~\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers, GQA with 16 query heads and 2 KV heads).
9	Of the 12 matrix cells, 10 are filled; NORA Object and Long-Horizon lack available checkpoints.
10	Each architecture is compared in trained and untrained conditions, with a critical asymmetry between untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained~\cite{padalkar2023_oxe} VLA (already fine-tuned for action prediction on 970K episodes), while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.
11	Three analyses are applied to each cell (\S\ref{sec:method}): $R^2$ action probes at all layers, L1 attention head profiling for instruction dominance, and counterfactual instruction perturbation.
12	For OpenVLA LIBERO-Goal, $N = 63{,}228$ observations; other cells are at comparable scale.
13	For trained models that produce action outputs, counterfactual sensitivity is measured via Cohen's $d$ on action MSE.
14	For untrained VLMs (Phi-3-Vision, Qwen2.5-VL) that do not produce actions, sensitivity is measured via cosine distance on hidden representations; these metrics operate on different scales and are not directly comparable (\S\ref{sec:cf_sensitivity}).
15	OpenVLA's OXE-pretrained checkpoint produces actions, permitting same-metric (Cohen's $d$) comparison in that condition.
16	Bonferroni correction details appear in Appendix~\ref{sec:bonferroni_correction}.
17	
18	%------------------------------------------------------------------
19	\subsection{OpenVLA: Instruction Routing and Functional Sensitivity}
20	\label{sec:openvla_routing}
21	
22	We first establish the core phenomena on a single architecture before testing cross-architectural generality.
23	Cross-instruction probes validate the analysis framework on OpenVLA~\cite{kim2024_openvla}: as predicted by the causal mask, image\_mean instruction classification stays at chance ($10\%$) across all 32 layers in all conditions (full profile in Appendix~\ref{sec:dense_routing}).
24	Trained readout achieves $100\%$ 10-way classification from L1 onward and maintains this through L31 (LOOCV-confirmed; Appendix~\ref{sec:loocv}).
25	Untrained readout also reaches $100\%$ at L1 but decays to $82\%$ by L31; the readout token is thus the primary multimodal integration site, and training stabilizes its instruction encoding across depth.
26	All patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
27	
28	At L1, three conditions form a gradient of instruction attention: untrained networks allocate 0/32 instruction-dominant heads ($11.7\%$ text attention, $1.5\times$ text-to-image ratio), Llama-2 base~\cite{touvron2023_llama2} allocates 9/32 ($36.5\%$), and VLA-trained allocates 24/32 ($57.7\%$, $38.2\times$ text-to-image ratio; Appendix~\ref{sec:attention_decomp}).
29	The 32-layer attention profile reveals qualitatively distinct organizations: Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads), while VLA fine-tuning produces an entry-exit bookend pattern with L0--L1 at 21--24 heads, L31 at 18, and intermediate layers at 0--11 (Appendix~\ref{sec:threshold_sensitivity}).
30	Head counts are computed at a $50\%$ threshold; sensitivity analysis ($30\%$--$70\%$) confirms ordering robustness.
31	A fourth condition, OpenVLA fine-tuned on LIBERO, preserves L1 entry concentration (22/32 heads) but loses L31 exit re-engagement entirely (0 vs.\ 18 heads for the OXE-pretrained model), consistent with exit-layer attention serving multi-task flexibility rather than task-specific routing.
32	The redistribution beyond Llama-2 base priors confirms that VLA fine-tuning creates new instruction routing rather than merely inheriting language-model attention.
33	
34	Counterfactual instruction perturbation validates the functional relevance of these structural patterns.
35	Four perturbation types across 10 LIBERO-Goal tasks produce action divergence ordered by token novelty ($\rho = 0.8$): empty instruction ($d = 0.978$), wrong task ($0.924$), shuffled tokens ($0.763$), paraphrased ($0.707$).
36	The shuffled-exceeds-paraphrased ordering, despite identical token sets, indicates that positional sensitivity dominates token-level novelty.
37	The effect replicates across LIBERO-Spatial (10 tasks) with the same ordering: empty $0.942$, wrong $0.851$, shuffled $0.833$, paraphrased $0.806$ (Appendix Table~\ref{tab:counterfactual_spatial}).
38	Across both suites (20 tasks), the gradient spans $d = 0.71$--$0.98$.
39	Spatial instructions differ only in prepositions, yet wrong-task perturbation still produces $d = 0.851$; instruction-dominant heads route fine-grained spatial information, not merely task identity.
40	
41	Dose-response ablation of L1 instruction-dominant heads produces monotonic trajectory divergence: $d$ rises from $0.482$ to $0.639$ as 4--32 heads are progressively ablated, with steep increase through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
42	Ablating all 24 instruction-dominant heads alters $72.3\%$ of action tokens (token-level $d = 0.65$, trajectory-level $d = 2.943$); control ablation of 8 random heads yields $d = 0.41$ ($29.3\%$ tokens affected), concentrated on the gripper dimension.
43	The routing effect is task-dependent: instruction-discriminative tasks show $2.5\times$ larger $|\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Appendix~\ref{sec:task_complexity}).
44	$R^2$ action probing localizes training effects: trained readout peaks at $R^2 = 0.678$ (L13), untrained readout peaks at $0.609$ (L32), and the training effect concentrates at the readout ($+0.069$) rather than at image\_mean ($+0.015$; Appendix~\ref{sec:action_r2_threecond}).
45	These effects survive Bonferroni correction across all 63 tests (Appendix~\ref{sec:bonferroni_correction}).
46	The single-architecture analysis establishes three phenomena for cross-architectural testing: instruction-dominant attention at L1, $R^2$ exit-layer dynamics between trained and untrained conditions, and graded counterfactual sensitivity to instruction perturbation.
47	
48	%------------------------------------------------------------------
49	\subsection{Cross-Architecture $R^2$ Exit Collapse}
50	\label{sec:r2_collapse}
51	
52	We define $R^2$ exit collapse as the drop in action-probe $R^2$ from peak layer to exit layer ($\Delta R^2 = R^2_{\text{peak}} - R^2_{\text{exit}}$).
53	A large $\Delta R^2$ indicates that action-relevant information encoded at intermediate layers is selectively discarded or transformed before reaching the exit.
54	Table~\ref{tab:cross_arch_matrix} reports this quantity for all available cells in the $3 \times 4$ matrix.
55	A consistent pattern emerges: trained models exhibit substantially larger $\Delta R^2$ than their untrained counterparts, but the magnitude and prevalence of collapse depend on the training transition being measured.
56	
57	TracVLA~\cite{zheng2024tracevla} shows clear exit collapse across all four LIBERO suites.
58	Trained $\Delta R^2$ ranges from $0.138$ (Spatial: peak $R^2 = 0.809$, exit $0.671$) to $0.294$ (Object: peak $0.764$, exit $0.470$), while untrained $\Delta R^2$ is uniformly small, from $0.009$ (Object) to $0.048$ (Goal).
59	The untrained TracVLA checkpoint is Phi-3-Vision, a pure vision-language model with no action training, and its flat $R^2$ profiles confirm that exit collapse is absent before VLA fine-tuning.
60	NORA~\cite{TODO_nora} exhibits the most extreme collapse in the matrix.
61	LIBERO-Goal trained produces $\Delta R^2 = 0.691$: the profile peaks at $R^2 = 0.688$ in mid-layers and drops to $-0.004$ at exit, below chance, so exit-layer representations encode less action-relevant structure than random vectors.
62	LIBERO-Spatial yields $\Delta R^2 = 0.302$ (peak $0.720$, exit $0.417$).
63	NORA untrained (Qwen2.5-VL) produces $\Delta R^2$ of only $0.044$ and $0.037$ for these two suites (Figure~\ref{fig:r2_collapse}).
64	Across all six TracVLA and NORA cells, every VLM-to-VLA transition produces exit collapse without exception.
65	
66	OpenVLA~\cite{kim2024_openvla} presents a contrasting pattern.
67	Only the Object suite shows clear collapse: trained $\Delta R^2 = 0.121$ (peak $0.787$, exit $0.666$) vs.\ untrained $0.076$ (peak $0.761$, exit $0.685$).
68	Goal ($\Delta R^2 = 0.016$ trained vs.\ $0.033$ untrained) and Long-Horizon ($0.004$ vs.\ $0.016$) show near-zero trained collapse; in both cases the untrained model produces a larger peak-to-exit drop than the trained model.
69	This asymmetry reflects the nature of the comparison: OpenVLA's untrained checkpoint is the OXE-pretrained VLA~\cite{padalkar2023_oxe}, which has undergone 970K episodes of action training.
70	The OXE-to-LIBERO transition, a VLA-to-VLA comparison, produces collapse in only 1 of 3 cells.
71	
72	The contrast between VLM-to-VLA (6/6) and VLA-to-VLA (1/3) collapse rates clarifies the nature of exit-layer reorganization.
73	A one-sided sign test confirms that the VLM-to-VLA collapse direction is consistent: all six cells show trained $\Delta R^2 >$ untrained $\Delta R^2$ ($p = 0.016$).
74	$R^2$ exit collapse emerges when vision-language models are first fine-tuned into VLAs (6/6 cells across two architectures) but does not intensify with further task-specific training of already-pretrained VLAs (1/3 cells), identifying exit collapse as a one-time reorganization at the VLM-to-VLA transition.
75	Once a VLM has been transformed into a VLA through initial action training, exit-layer $R^2$ profiles are largely established.
76	The OpenVLA Object exception may reflect specific demands of object-centric manipulation, but the 6/6 vs.\ 1/3 contrast supports the transition-specific interpretation.
77	
78	\begin{table}[t]
79	\centering
80	\caption{Cross-architecture summary of $R^2$ exit collapse ($\Delta R^2$: peak-to-exit drop in action-probe $R^2$) and counterfactual (CF) sensitivity (effect size of top perturbation condition). All 10 available cells in the $3 \times 4$ architecture $\times$ suite matrix are shown. Top CF condition is ``empty'' for all trained cells except OpenVLA Long (``shuffled''). \textbf{Trained/untrained asymmetry}: OpenVLA untrained is an OXE-pretrained VLA; TracVLA and NORA untrained are pure VLMs with no action training. \textbf{Metric note}: trained CF uses Cohen's $d$ (OpenVLA, TracVLA) or cosine distance (NORA); untrained CF uses cosine distance except where noted. Cross-metric ratios are not meaningful (\S\ref{sec:cf_sensitivity}).}
81	\label{tab:cross_arch_matrix}
82	\small
83	\begin{tabular}{llcccc}
84	\toprule
85	& & \multicolumn{2}{c}{$\Delta R^2$} & \multicolumn{2}{c}{CF (top cond.)} \\
86	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
87	Arch. & Suite & Trained & Untr. & Trained & Untr. \\
88	\midrule
89	OpenVLA & Goal    & 0.016 & 0.033 & 0.98  & ---            \\
90	OpenVLA & Object  & 0.121 & 0.076 & 1.21  & 0.57$^{*}$     \\
91	OpenVLA & Long    & 0.004 & 0.016 & 0.56$^{\dagger}$ & 1.05$^{\ddagger}$ \\
92	\midrule
93	TracVLA & Goal    & 0.228 & 0.048 & 1.52  & 0.15$^{*}$     \\
94	TracVLA & Spatial & 0.138 & 0.016 & 1.33  & 0.18$^{*}$     \\
95	TracVLA & Object  & 0.294 & 0.009 & 1.21  & 0.19$^{*}$     \\
96	TracVLA & Long    & 0.198 & 0.028 & 1.47  & 0.17$^{*}$     \\
97	\midrule
98	NORA    & Goal    & 0.691 & 0.044 & sat.$^{\S}$  & 0.08$^{*}$ \\
99	NORA    & Spatial & 0.302 & 0.037 & 0.28$^{*}$   & ---        \\
100	NORA    & Obj./Long & \multicolumn{4}{c}{\textit{no checkpoints available}} \\
101	\bottomrule
102	\multicolumn{6}{l}{\footnotesize Trained CF: Cohen's $d$ (OpenVLA, TracVLA) or cosine distance$^{*}$ (NORA).} \\
103	\multicolumn{6}{l}{\footnotesize $^{*}$Cosine distance on hidden representations (different scale from $d$).}\\
104	\multicolumn{6}{l}{\footnotesize $^{\dagger}$Top cond.\ is ``shuffled.'' $^{\ddagger}$Cohen's $d$; untrained is an OXE-pretrained VLA.}\\
105	\multicolumn{6}{l}{\footnotesize $^{\S}$Cosine distances saturated at $1.0$; earlier layers differentiate.}\\
106	\end{tabular}
107	\end{table}
108	
109	\begin{figure}[t]
110	\centering
111	\fbox{\parbox{0.9\columnwidth}{\centering\vspace{1.5cm}\textbf{[Placeholder: fig\_r2\_collapse]}\vspace{1.5cm}}}
112	\caption{Per-layer $R^2$ action-probe profiles for three architectures, each comparing trained (solid) and untrained (dashed) checkpoints. TracVLA and NORA trained models exhibit pronounced peak-to-exit collapse ($\Delta R^2 = 0.14$--$0.69$), while their untrained VLM baselines show flat profiles ($\Delta R^2 \leq 0.05$). OpenVLA trained shows clear collapse only for Object ($\Delta R^2 = 0.12$); its untrained baseline is an OXE-pretrained VLA that has already undergone exit-layer reorganization.}
113	\label{fig:r2_collapse}
114	\end{figure}
115	
116	%------------------------------------------------------------------
117	\subsection{Cross-Architecture Counterfactual Sensitivity}
118	\label{sec:cf_sensitivity}
119	
120	Counterfactual sensitivity provides a complementary measure of how trained VLAs integrate instruction information.
121	We replace the instruction with four perturbation types (empty, wrong task, shuffled tokens, paraphrased) and measure the resulting action divergence.
122	Table~\ref{tab:counterfactual} reports condition rankings for all eight cells where Cohen's $d$ is available (OpenVLA and TracVLA across four suites each).
123	Across both architectures and all eight combinations, every perturbation condition produces statistically significant action divergence ($d \geq 0.45$); trained VLAs are sensitive to instruction content regardless of perturbation type.
124	
125	The ``empty'' condition ranks first in 7 of 8 cells, with effect sizes from $d = 0.94$ (OpenVLA Spatial) to $1.52$ (TracVLA Goal).
126	OpenVLA Long-Horizon is the sole exception: ``shuffled'' ranks first ($d = 0.56$) and all conditions produce weaker effects ($d = 0.45$--$0.56$).
127	The remaining conditions follow a broadly consistent ordering: ``wrong'' and ``shuffled'' alternate in second and third position, while ``paraphrased'' ranks last in 7 of 8 cells.
128	TracVLA produces systematically higher effect sizes than OpenVLA ($d = 0.97$--$1.52$ vs.\ $0.45$--$1.21$), consistent with the Phi-3 backbone routing instruction information more strongly through the VLA pipeline.
129	NORA's counterfactual analysis uses cosine distance rather than Cohen's $d$ because its output format precludes action-level MSE computation.
130	NORA Goal produces saturated exit-layer cosine distances of $1.0$ for all conditions, with differentiation visible only at earlier layers (L24: wrong $= 0.123$, empty $= 0.098$).
131	NORA Spatial produces a peak cosine distance of $0.275$ for the ``wrong'' condition.
132	
133	\paragraph{Metric constraints on trained--untrained comparison.}
134	A critical limitation constrains quantitative comparison between trained and untrained counterfactual sensitivity.
135	Trained models produce action outputs, enabling Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action tokens (NORA).
136	Untrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations---a metric with different scale, units, and distributional properties.
137	Ratios between Cohen's $d$ and cosine distance are therefore methodologically invalid, and we do not report cross-metric amplification factors.
138	
139	Qualitatively, untrained VLMs show weak instruction sensitivity: TracVLA untrained (Phi-3-Vision) produces peak cosine distances of $0.15$--$0.19$ across four suites, and NORA untrained (Qwen2.5-VL) yields $0.081$ on Goal.
140	All trained models produce substantial sensitivity (Cohen's $d \geq 0.45$ for OpenVLA and TracVLA; cosine distances up to saturation for NORA), but the trained--untrained gap cannot be quantified as a single ratio.
141	
142	The one cell permitting same-metric comparison is OpenVLA Long-Horizon, where both the trained and the OXE-pretrained untrained checkpoints produce actions and are measured via Cohen's $d$.
143	The result is \emph{inverted}: the OXE-pretrained model ($d = 1.05$, empty) shows stronger sensitivity than the LIBERO-trained model ($d = 0.56$, shuffled; $0.50$, empty).
144	This inversion is consistent with OpenVLA Long's anomalous profile (near-zero $R^2$ collapse, lowest trained CF sensitivity in the matrix) and with the general-purpose OXE model maintaining broader instruction responsiveness than a task-specialized fine-tune.
145	
146	We conclude that VLA training produces consistent instruction sensitivity across architectures (all trained Cohen's $d \geq 0.45$; condition ordering preserved), but the magnitude of trained-versus-untrained change cannot be reliably quantified due to metric incomparability at the VLM-to-VLA transition.
147	Unlike $R^2$ exit collapse, counterfactual sensitivity is not limited to the VLM-to-VLA transition: trained OpenVLA produces $d = 0.98$ (Goal) and $1.21$ (Object), and the OXE-pretrained baseline for Object yields cosine distance $0.569$, indicating that task-specific training can modulate sensitivity within the VLA-to-VLA regime as well.
148	
149	\begin{table}[t]
150	\centering
151	\caption{Counterfactual condition ranking for trained models (Cohen's $d$; higher $=$ greater action divergence under instruction perturbation). Conditions: E $=$ empty instruction, W $=$ wrong task, S $=$ shuffled tokens, P $=$ paraphrased. ``Empty'' ranks first in 7 of 8 cells; OpenVLA Long is the exception. NORA cells use cosine distance and are reported in the text (\S\ref{sec:cf_sensitivity}).}
152	\label{tab:counterfactual}
153	\small
154	\begin{tabular}{llcccc}
155	\toprule
156	Arch. & Suite & 1st & 2nd & 3rd & 4th \\
157	\midrule
158	OpenVLA & Goal    & E\,0.98 & W\,0.92 & S\,0.76 & P\,0.71 \\
159	OpenVLA & Spatial & E\,0.94 & W\,0.85 & S\,0.83 & P\,0.81 \\
160	OpenVLA & Object  & E\,1.21 & W\,1.19 & S\,1.12 & P\,0.90 \\
161	OpenVLA & Long    & S\,0.56 & W\,0.55 & E\,0.50 & P\,0.45 \\
162	\midrule
163	TracVLA & Goal    & E\,1.52 & W\,1.40 & S\,1.34 & P\,1.21 \\
164	TracVLA & Spatial & E\,1.33 & S\,1.29 & P\,1.18 & W\,1.17 \\
165	TracVLA & Object  & E\,1.21 & S\,1.16 & W\,1.06 & P\,0.97 \\
166	TracVLA & Long    & E\,1.47 & W\,1.42 & S\,1.39 & P\,1.16 \\
167	\bottomrule
168	\end{tabular}
169	\end{table}
170	
171	%------------------------------------------------------------------
172	\subsection{L1 Attention Reflects Base-Model Priors}
173	\label{sec:l1_priors}
174	
175	L1 instruction-dominant head counts across architectures reveal a pattern that contrasts with the training-induced effects documented in \S\ref{sec:r2_collapse} and \S\ref{sec:cf_sensitivity}.
176	TracVLA untrained (Phi-3-Vision) allocates 32/32 heads to instruction-dominant attention across all four suites, saturating the capacity of its 32-head L1 before any VLA training.
177	Training slightly \emph{reduces} this count to 27--30/32, with freed heads presumably repurposed for action-related computation.
178	NORA untrained (Qwen2.5-VL) allocates 13--14 of its 16 L1 heads to instruction dominance (81--88\%), and training leaves this essentially unchanged at 12--13/16.
179	OpenVLA shows 24--26/32 instruction-dominant heads in the OXE-pretrained baseline; trained values are similar (14--24/32), with the largest change in Long-Horizon where training reduces the count from 25 to 14 heads (Figure~\ref{fig:cross_arch_l1}).
180	
181	These patterns are consistent with L1 instruction attention reflecting base-model language pretraining rather than VLA fine-tuning.
182	If VLA training were the primary driver of L1 instruction routing, untrained VLMs should show low instruction attention that increases after training, as observed in OpenVLA's random-weight condition (0/32 heads, \S\ref{sec:openvla_routing}).
183	Instead, TracVLA and NORA untrained models exhibit strong instruction attention before any action training.
184	Phi-3-Vision saturates at 32/32 heads ($100\%$) and Qwen2.5-VL allocates 13--14/16 ($81$--$88\%$), proportions characteristic of instruction-tuned language models that attend heavily to text tokens as part of their base training.
185	The fact that one backbone (Phi-3-Vision) exhibits fully saturated instruction attention even before fine-tuning provides the clearest evidence that L1 patterns are base-model priors.
186	This observation distinguishes two classes of routing effects: training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) that emerge during VLA fine-tuning, and inherited effects (L1 instruction attention) that trace to base-model pretraining.
187	High L1 instruction attention does not indicate that a model has learned to route instructions for action prediction; it indicates that the base language model already devoted attention capacity to text tokens.
188	
189	\begin{figure}[t]
190	\centering
191	\fbox{\parbox{0.9\columnwidth}{\centering\vspace{1.5cm}\textbf{[Placeholder: fig\_cross\_arch\_l1]}\vspace{1.5cm}}}
192	\caption{L1 instruction-dominant head counts for three architectures, comparing trained and untrained checkpoints. TracVLA untrained (Phi-3-Vision) saturates at 32/32 before any VLA training; training reduces this to 27--30/32. NORA (16-head GQA) shows 13--14/16 in both conditions. OpenVLA ranges from 14--24/32 trained vs.\ 24--26/32 untrained (OXE-pretrained). L1 instruction attention reflects base-model language priors, not VLA fine-tuning.}
193	\label{fig:cross_arch_l1}
194	\end{figure}
195	
196	%------------------------------------------------------------------
197	\subsection{Synthesis: Training-Induced vs.\ Inherited Routing}
198	\label{sec:routing_synthesis}
199	
200	The findings from \S\ref{sec:r2_collapse}--\ref{sec:l1_priors} distinguish two classes of routing effects.
201	Training-induced effects---$R^2$ exit collapse and counterfactual sensitivity---emerge or intensify at the VLM-to-VLA transition: exit collapse is present in 6/6 VLM-to-VLA cells (sign test $p = 0.016$) but only 1/3 VLA-to-VLA cells, and all trained models exhibit substantial counterfactual sensitivity ($d \geq 0.45$ where Cohen's $d$ is applicable).
202	Inherited effects---L1 instruction-dominant attention---trace to base-model language pretraining and persist through VLA fine-tuning (TracVLA: 32/32 before training; NORA: 13--14/16).
203	This distinction clarifies the representational role of VLA fine-tuning: training reorganizes mid-to-exit layer action encoding and establishes instruction-conditioned action sensitivity, while early-layer attention structure reflects the pretrained backbone.
204	The consistency of these training-induced effects across two VLM-to-VLA transitions (TracVLA, NORA)---architectures with dramatically different base-model priors---is compatible with exit collapse and counterfactual sensitivity reflecting task-structure constraints of VLA fine-tuning rather than architecture-specific artifacts; OpenVLA's partial confirmation (2/4 suites for $R^2$ collapse) tempers the generality of this interpretation.
205	A more detailed characterization of how these effects compose across training stages is developed in the Discussion (\S\ref{sec:discussion}).
206	
207	As a secondary observation, vision encoder geometry measured by RSA shows a non-monotonic profile with a middle-layer peak (L12: $\rho = 0.628$), and standalone DINOv2~\cite{oquab2024_dinov2} achieves the highest RSA among encoders ($\rho = 0.692$).
208	Under linear CKA~\cite{kornblith2019}, this non-monotonic pattern disappears (monotonic increase), qualifying the observation as metric-dependent (Appendix~\ref{sec:cka_appendix}).
209	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "76a3734b-136b-467d-b6b7-a9e8f13deede",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe analyze three VLA architectures across four LIBERO~\\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon) in a $3 \\times 4$ cross-architecture matrix (Table~\\ref{tab:cross_arch_matrix}).\nThe architectures span distinct backbone families: OpenVLA~\\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\\cite{touvron2023_llama2}, 32 layers, 32 MHA heads), TracVLA~\\cite{zheng2024tracevla} (Phi-3-mini~\\cite{abdin2024phi3}, 32 layers, 32 heads), and NORA~\\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers, GQA with 16 query heads and 2 KV heads).\nOf the 12 matrix cells, 10 are filled; NORA Object and Long-Horizon lack available checkpoints.\nEach architecture is compared in trained and untrained conditions, with a critical asymmetry between untrained baselines: OpenVLA's untrained checkpoint is the OXE-pretrained~\\cite{padalkar2023_oxe} VLA (already fine-tuned for action prediction on 970K episodes), while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision and Qwen2.5-VL) with no action training.\nThree analyses are applied to each cell (\\S\\ref{sec:method}): $R^2$ action probes at all layers, L1 attention head profiling for instruction dominance, and counterfactual instruction perturbation.\nFor OpenVLA LIBERO-Goal, $N = 63{,}228$ observations; other cells are at comparable scale.\nFor trained models that produce action outputs, counterfactual sensitivity is measured via Cohen's $d$ on action MSE.\nFor untrained VLMs (Phi-3-Vision, Qwen2.5-VL) that do not produce actions, sensitivity is measured via cosine distance on hidden representations; these metrics operate on different scales and are not directly comparable (\\S\\ref{sec:cf_sensitivity}).\nOpenVLA's OXE-pretrained checkpoint produces actions, permitting same-metric (Cohen's $d$) comparison in that condition.\nBonferroni correction details appear in Appendix~\\ref{sec:bonferroni_correction}.\n\n%------------------------------------------------------------------\n\\subsection{OpenVLA: Instruction Routing and Functional Sensitivity}\n\\label{sec:openvla_routing}\n\nWe first establish the core phenomena on a single architecture before testing cross-architectural generality.\nCross-instruction probes validate the analysis framework on OpenVLA~\\cite{kim2024_openvla}: as predicted by the causal mask, image\\_mean instruction classification stays at chance ($10\\%$) across all 32 layers in all conditions (full profile in Appendix~\\ref{sec:dense_routing}).\nTrained readout achieves $100\\%$ 10-way classification from L1 onward and maintains this through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}).\nUntrained readout also reaches $100\\%$ at L1 but decays to $82\\%$ by L31; the readout token is thus the primary multimodal integration site, and training stabilizes its instruction encoding across depth.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\nAt L1, three conditions form a gradient of instruction attention: untrained networks allocate 0/32 instruction-dominant heads ($11.7\\%$ text attention, $1.5\\times$ text-to-image ratio), Llama-2 base~\\cite{touvron2023_llama2} allocates 9/32 ($36.5\\%$), and VLA-trained allocates 24/32 ($57.7\\%$, $38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}).\nThe 32-layer attention profile reveals qualitatively distinct organizations: Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads), while VLA fine-tuning produces an entry-exit bookend pattern with L0--L1 at 21--24 heads, L31 at 18, and intermediate layers at 0--11 (Appendix~\\ref{sec:threshold_sensitivity}).\nHead counts are computed at a $50\\%$ threshold; sensitivity analysis ($30\\%$--$70\\%$) confirms ordering robustness.\nA fourth condition, OpenVLA fine-tuned on LIBERO, preserves L1 entry concentration (22/32 heads) but loses L31 exit re-engagement entirely (0 vs.\\ 18 heads for the OXE-pretrained model), consistent with exit-layer attention serving multi-task flexibility rather than task-specific routing.\nThe redistribution beyond Llama-2 base priors confirms that VLA fine-tuning creates new instruction routing rather than merely inheriting language-model attention.\n\nCounterfactual instruction perturbation validates the functional relevance of these structural patterns.\nFour perturbation types across 10 LIBERO-Goal tasks produce action divergence ordered by token novelty ($\\rho = 0.8$): empty instruction ($d = 0.978$), wrong task ($0.924$), shuffled tokens ($0.763$), paraphrased ($0.707$).\nThe shuffled-exceeds-paraphrased ordering, despite identical token sets, indicates that positional sensitivity dominates token-level novelty.\nThe effect replicates across LIBERO-Spatial (10 tasks) with the same ordering: empty $0.942$, wrong $0.851$, shuffled $0.833$, paraphrased $0.806$ (Appendix Table~\\ref{tab:counterfactual_spatial}).\nAcross both suites (20 tasks), the gradient spans $d = 0.71$--$0.98$.\nSpatial instructions differ only in prepositions, yet wrong-task perturbation still produces $d = 0.851$; instruction-dominant heads route fine-grained spatial information, not merely task identity.\n\nDose-response ablation of L1 instruction-dominant heads produces monotonic trajectory divergence: $d$ rises from $0.482$ to $0.639$ as 4--32 heads are progressively ablated, with steep increase through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\nAblating all 24 instruction-dominant heads alters $72.3\\%$ of action tokens (token-level $d = 0.65$, trajectory-level $d = 2.943$); control ablation of 8 random heads yields $d = 0.41$ ($29.3\\%$ tokens affected), concentrated on the gripper dimension.\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Appendix~\\ref{sec:task_complexity}).\n$R^2$ action probing localizes training effects: trained readout peaks at $R^2 = 0.678$ (L13), untrained readout peaks at $0.609$ (L32), and the training effect concentrates at the readout ($+0.069$) rather than at image\\_mean ($+0.015$; Appendix~\\ref{sec:action_r2_threecond}).\nThese effects survive Bonferroni correction across all 63 tests (Appendix~\\ref{sec:bonferroni_correction}).\nThe single-architecture analysis establishes three phenomena for cross-architectural testing: instruction-dominant attention at L1, $R^2$ exit-layer dynamics between trained and untrained conditions, and graded counterfactual sensitivity to instruction perturbation.\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture $R^2$ Exit Collapse}\n\\label{sec:r2_collapse}\n\nWe define $R^2$ exit collapse as the drop in action-probe $R^2$ from peak layer to exit layer ($\\Delta R^2 = R^2_{\\text{peak}} - R^2_{\\text{exit}}$).\nA large $\\Delta R^2$ indicates that action-relevant information encoded at intermediate layers is selectively discarded or transformed before reaching the exit.\nTable~\\ref{tab:cross_arch_matrix} reports this quantity for all available cells in the $3 \\times 4$ matrix.\nA consistent pattern emerges: trained models exhibit substantially larger $\\Delta R^2$ than their untrained counterparts, but the magnitude and prevalence of collapse depend on the training transition being measured.\n\nTracVLA~\\cite{zheng2024tracevla} shows clear exit collapse across all four LIBERO suites.\nTrained $\\Delta R^2$ ranges from $0.138$ (Spatial: peak $R^2 = 0.809$, exit $0.671$) to $0.294$ (Object: peak $0.764$, exit $0.470$), while untrained $\\Delta R^2$ is uniformly small, from $0.009$ (Object) to $0.048$ (Goal).\nThe untrained TracVLA checkpoint is Phi-3-Vision, a pure vision-language model with no action training, and its flat $R^2$ profiles confirm that exit collapse is absent before VLA fine-tuning.\nNORA~\\cite{TODO_nora} exhibits the most extreme collapse in the matrix.\nLIBERO-Goal trained produces $\\Delta R^2 = 0.691$: the profile peaks at $R^2 = 0.688$ in mid-layers and drops to $-0.004$ at exit, below chance, so exit-layer representations encode less action-relevant structure than random vectors.\nLIBERO-Spatial yields $\\Delta R^2 = 0.302$ (peak $0.720$, exit $0.417$).\nNORA untrained (Qwen2.5-VL) produces $\\Delta R^2$ of only $0.044$ and $0.037$ for these two suites (Figure~\\ref{fig:r2_collapse}).\nAcross all six TracVLA and NORA cells, every VLM-to-VLA transition produces exit collapse without exception.\n\nOpenVLA~\\cite{kim2024_openvla} presents a contrasting pattern.\nOnly the Object suite shows clear collapse: trained $\\Delta R^2 = 0.121$ (peak $0.787$, exit $0.666$) vs.\\ untrained $0.076$ (peak $0.761$, exit $0.685$).\nGoal ($\\Delta R^2 = 0.016$ trained vs.\\ $0.033$ untrained) and Long-Horizon ($0.004$ vs.\\ $0.016$) show near-zero trained collapse; in both cases the untrained model produces a larger peak-to-exit drop than the trained model.\nThis asymmetry reflects the nature of the comparison: OpenVLA's untrained checkpoint is the OXE-pretrained VLA~\\cite{padalkar2023_oxe}, which has undergone 970K episodes of action training.\nThe OXE-to-LIBERO transition, a VLA-to-VLA comparison, produces collapse in only 1 of 3 cells.\n\nThe contrast between VLM-to-VLA (6/6) and VLA-to-VLA (1/3) collapse rates clarifies the nature of exit-layer reorganization.\nA one-sided sign test confirms that the VLM-to-VLA collapse direction is consistent: all six cells show trained $\\Delta R^2 >$ untrained $\\Delta R^2$ ($p = 0.016$).\n$R^2$ exit collapse emerges when vision-language models are first fine-tuned into VLAs (6/6 cells across two architectures) but does not intensify with further task-specific training of already-pretrained VLAs (1/3 cells), identifying exit collapse as a one-time reorganization at the VLM-to-VLA transition.\nOnce a VLM has been transformed into a VLA through initial action training, exit-layer $R^2$ profiles are largely established.\nThe OpenVLA Object exception may reflect specific demands of object-centric manipulation, but the 6/6 vs.\\ 1/3 contrast supports the transition-specific interpretation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture summary of $R^2$ exit collapse ($\\Delta R^2$: peak-to-exit drop in action-probe $R^2$) and counterfactual (CF) sensitivity (effect size of top perturbation condition). All 10 available cells in the $3 \\times 4$ architecture $\\times$ suite matrix are shown. Top CF condition is ``empty'' for all trained cells except OpenVLA Long (``shuffled''). \\textbf{Trained/untrained asymmetry}: OpenVLA untrained is an OXE-pretrained VLA; TracVLA and NORA untrained are pure VLMs with no action training. \\textbf{Metric note}: trained CF uses Cohen's $d$ (OpenVLA, TracVLA) or cosine distance (NORA); untrained CF uses cosine distance except where noted. Cross-metric ratios are not meaningful (\\S\\ref{sec:cf_sensitivity}).}\n\\label{tab:cross_arch_matrix}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n& & \\multicolumn{2}{c}{$\\Delta R^2$} & \\multicolumn{2}{c}{CF (top cond.)} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6}\nArch. & Suite & Trained & Untr. & Trained & Untr. \\\\\n\\midrule\nOpenVLA & Goal    & 0.016 & 0.033 & 0.98  & ---            \\\\\nOpenVLA & Object  & 0.121 & 0.076 & 1.21  & 0.57$^{*}$     \\\\\nOpenVLA & Long    & 0.004 & 0.016 & 0.56$^{\\dagger}$ & 1.05$^{\\ddagger}$ \\\\\n\\midrule\nTracVLA & Goal    & 0.228 & 0.048 & 1.52  & 0.15$^{*}$     \\\\\nTracVLA & Spatial & 0.138 & 0.016 & 1.33  & 0.18$^{*}$     \\\\\nTracVLA & Object  & 0.294 & 0.009 & 1.21  & 0.19$^{*}$     \\\\\nTracVLA & Long    & 0.198 & 0.028 & 1.47  & 0.17$^{*}$     \\\\\n\\midrule\nNORA    & Goal    & 0.691 & 0.044 & sat.$^{\\S}$  & 0.08$^{*}$ \\\\\nNORA    & Spatial & 0.302 & 0.037 & 0.28$^{*}$   & ---        \\\\\nNORA    & Obj./Long & \\multicolumn{4}{c}{\\textit{no checkpoints available}} \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize Trained CF: Cohen's $d$ (OpenVLA, TracVLA) or cosine distance$^{*}$ (NORA).} \\\\\n\\multicolumn{6}{l}{\\footnotesize $^{*}$Cosine distance on hidden representations (different scale from $d$).}\\\\\n\\multicolumn{6}{l}{\\footnotesize $^{\\dagger}$Top cond.\\ is ``shuffled.'' $^{\\ddagger}$Cohen's $d$; untrained is an OXE-pretrained VLA.}\\\\\n\\multicolumn{6}{l}{\\footnotesize $^{\\S}$Cosine distances saturated at $1.0$; earlier layers differentiate.}\\\\\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{1.5cm}\\textbf{[Placeholder: fig\\_r2\\_collapse]}\\vspace{1.5cm}}}\n\\caption{Per-layer $R^2$ action-probe profiles for three architectures, each comparing trained (solid) and untrained (dashed) checkpoints. TracVLA and NORA trained models exhibit pronounced peak-to-exit collapse ($\\Delta R^2 = 0.14$--$0.69$), while their untrained VLM baselines show flat profiles ($\\Delta R^2 \\leq 0.05$). OpenVLA trained shows clear collapse only for Object ($\\Delta R^2 = 0.12$); its untrained baseline is an OXE-pretrained VLA that has already undergone exit-layer reorganization.}\n\\label{fig:r2_collapse}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Cross-Architecture Counterfactual Sensitivity}\n\\label{sec:cf_sensitivity}\n\nCounterfactual sensitivity provides a complementary measure of how trained VLAs integrate instruction information.\nWe replace the instruction with four perturbation types (empty, wrong task, shuffled tokens, paraphrased) and measure the resulting action divergence.\nTable~\\ref{tab:counterfactual} reports condition rankings for all eight cells where Cohen's $d$ is available (OpenVLA and TracVLA across four suites each).\nAcross both architectures and all eight combinations, every perturbation condition produces statistically significant action divergence ($d \\geq 0.45$); trained VLAs are sensitive to instruction content regardless of perturbation type.\n\nThe ``empty'' condition ranks first in 7 of 8 cells, with effect sizes from $d = 0.94$ (OpenVLA Spatial) to $1.52$ (TracVLA Goal).\nOpenVLA Long-Horizon is the sole exception: ``shuffled'' ranks first ($d = 0.56$) and all conditions produce weaker effects ($d = 0.45$--$0.56$).\nThe remaining conditions follow a broadly consistent ordering: ``wrong'' and ``shuffled'' alternate in second and third position, while ``paraphrased'' ranks last in 7 of 8 cells.\nTracVLA produces systematically higher effect sizes than OpenVLA ($d = 0.97$--$1.52$ vs.\\ $0.45$--$1.21$), consistent with the Phi-3 backbone routing instruction information more strongly through the VLA pipeline.\nNORA's counterfactual analysis uses cosine distance rather than Cohen's $d$ because its output format precludes action-level MSE computation.\nNORA Goal produces saturated exit-layer cosine distances of $1.0$ for all conditions, with differentiation visible only at earlier layers (L24: wrong $= 0.123$, empty $= 0.098$).\nNORA Spatial produces a peak cosine distance of $0.275$ for the ``wrong'' condition.\n\n\\paragraph{Metric constraints on trained--untrained comparison.}\nA critical limitation constrains quantitative comparison between trained and untrained counterfactual sensitivity.\nTrained models produce action outputs, enabling Cohen's $d$ on action MSE (OpenVLA, TracVLA) or cosine distance on action tokens (NORA).\nUntrained VLMs (Phi-3-Vision, Qwen2.5-VL) do not generate actions; their sensitivity is measured via cosine distance on hidden representations---a metric with different scale, units, and distributional properties.\nRatios between Cohen's $d$ and cosine distance are therefore methodologically invalid, and we do not report cross-metric amplification factors.\n\nQualitatively, untrained VLMs show weak instruction sensitivity: TracVLA untrained (Phi-3-Vision) produces peak cosine distances of $0.15$--$0.19$ across four suites, and NORA untrained (Qwen2.5-VL) yields $0.081$ on Goal.\nAll trained models produce substantial sensitivity (Cohen's $d \\geq 0.45$ for OpenVLA and TracVLA; cosine distances up to saturation for NORA), but the trained--untrained gap cannot be quantified as a single ratio.\n\nThe one cell permitting same-metric comparison is OpenVLA Long-Horizon, where both the trained and the OXE-pretrained untrained checkpoints produce actions and are measured via Cohen's $d$.\nThe result is \\emph{inverted}: the OXE-pretrained model ($d = 1.05$, empty) shows stronger sensitivity than the LIBERO-trained model ($d = 0.56$, shuffled; $0.50$, empty).\nThis inversion is consistent with OpenVLA Long's anomalous profile (near-zero $R^2$ collapse, lowest trained CF sensitivity in the matrix) and with the general-purpose OXE model maintaining broader instruction responsiveness than a task-specialized fine-tune.\n\nWe conclude that VLA training produces consistent instruction sensitivity across architectures (all trained Cohen's $d \\geq 0.45$; condition ordering preserved), but the magnitude of trained-versus-untrained change cannot be reliably quantified due to metric incomparability at the VLM-to-VLA transition.\nUnlike $R^2$ exit collapse, counterfactual sensitivity is not limited to the VLM-to-VLA transition: trained OpenVLA produces $d = 0.98$ (Goal) and $1.21$ (Object), and the OXE-pretrained baseline for Object yields cosine distance $0.569$, indicating that task-specific training can modulate sensitivity within the VLA-to-VLA regime as well.\n\n\\begin{table}[t]\n\\centering\n\\caption{Counterfactual condition ranking for trained models (Cohen's $d$; higher $=$ greater action divergence under instruction perturbation). Conditions: E $=$ empty instruction, W $=$ wrong task, S $=$ shuffled tokens, P $=$ paraphrased. ``Empty'' ranks first in 7 of 8 cells; OpenVLA Long is the exception. NORA cells use cosine distance and are reported in the text (\\S\\ref{sec:cf_sensitivity}).}\n\\label{tab:counterfactual}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nArch. & Suite & 1st & 2nd & 3rd & 4th \\\\\n\\midrule\nOpenVLA & Goal    & E\\,0.98 & W\\,0.92 & S\\,0.76 & P\\,0.71 \\\\\nOpenVLA & Spatial & E\\,0.94 & W\\,0.85 & S\\,0.83 & P\\,0.81 \\\\\nOpenVLA & Object  & E\\,1.21 & W\\,1.19 & S\\,1.12 & P\\,0.90 \\\\\nOpenVLA & Long    & S\\,0.56 & W\\,0.55 & E\\,0.50 & P\\,0.45 \\\\\n\\midrule\nTracVLA & Goal    & E\\,1.52 & W\\,1.40 & S\\,1.34 & P\\,1.21 \\\\\nTracVLA & Spatial & E\\,1.33 & S\\,1.29 & P\\,1.18 & W\\,1.17 \\\\\nTracVLA & Object  & E\\,1.21 & S\\,1.16 & W\\,1.06 & P\\,0.97 \\\\\nTracVLA & Long    & E\\,1.47 & W\\,1.42 & S\\,1.39 & P\\,1.16 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{L1 Attention Reflects Base-Model Priors}\n\\label{sec:l1_priors}\n\nL1 instruction-dominant head counts across architectures reveal a pattern that contrasts with the training-induced effects documented in \\S\\ref{sec:r2_collapse} and \\S\\ref{sec:cf_sensitivity}.\nTracVLA untrained (Phi-3-Vision) allocates 32/32 heads to instruction-dominant attention across all four suites, saturating the capacity of its 32-head L1 before any VLA training.\nTraining slightly \\emph{reduces} this count to 27--30/32, with freed heads presumably repurposed for action-related computation.\nNORA untrained (Qwen2.5-VL) allocates 13--14 of its 16 L1 heads to instruction dominance (81--88\\%), and training leaves this essentially unchanged at 12--13/16.\nOpenVLA shows 24--26/32 instruction-dominant heads in the OXE-pretrained baseline; trained values are similar (14--24/32), with the largest change in Long-Horizon where training reduces the count from 25 to 14 heads (Figure~\\ref{fig:cross_arch_l1}).\n\nThese patterns are consistent with L1 instruction attention reflecting base-model language pretraining rather than VLA fine-tuning.\nIf VLA training were the primary driver of L1 instruction routing, untrained VLMs should show low instruction attention that increases after training, as observed in OpenVLA's random-weight condition (0/32 heads, \\S\\ref{sec:openvla_routing}).\nInstead, TracVLA and NORA untrained models exhibit strong instruction attention before any action training.\nPhi-3-Vision saturates at 32/32 heads ($100\\%$) and Qwen2.5-VL allocates 13--14/16 ($81$--$88\\%$), proportions characteristic of instruction-tuned language models that attend heavily to text tokens as part of their base training.\nThe fact that one backbone (Phi-3-Vision) exhibits fully saturated instruction attention even before fine-tuning provides the clearest evidence that L1 patterns are base-model priors.\nThis observation distinguishes two classes of routing effects: training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) that emerge during VLA fine-tuning, and inherited effects (L1 instruction attention) that trace to base-model pretraining.\nHigh L1 instruction attention does not indicate that a model has learned to route instructions for action prediction; it indicates that the base language model already devoted attention capacity to text tokens.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.9\\columnwidth}{\\centering\\vspace{1.5cm}\\textbf{[Placeholder: fig\\_cross\\_arch\\_l1]}\\vspace{1.5cm}}}\n\\caption{L1 instruction-dominant head counts for three architectures, comparing trained and untrained checkpoints. TracVLA untrained (Phi-3-Vision) saturates at 32/32 before any VLA training; training reduces this to 27--30/32. NORA (16-head GQA) shows 13--14/16 in both conditions. OpenVLA ranges from 14--24/32 trained vs.\\ 24--26/32 untrained (OXE-pretrained). L1 instruction attention reflects base-model language priors, not VLA fine-tuning.}\n\\label{fig:cross_arch_l1}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Synthesis: Training-Induced vs.\\ Inherited Routing}\n\\label{sec:routing_synthesis}\n\nThe findings from \\S\\ref{sec:r2_collapse}--\\ref{sec:l1_priors} distinguish two classes of routing effects.\nTraining-induced effects---$R^2$ exit collapse and counterfactual sensitivity---emerge or intensify at the VLM-to-VLA transition: exit collapse is present in 6/6 VLM-to-VLA cells (sign test $p = 0.016$) but only 1/3 VLA-to-VLA cells, and all trained models exhibit substantial counterfactual sensitivity ($d \\geq 0.45$ where Cohen's $d$ is applicable).\nInherited effects---L1 instruction-dominant attention---trace to base-model language pretraining and persist through VLA fine-tuning (TracVLA: 32/32 before training; NORA: 13--14/16).\nThis distinction clarifies the representational role of VLA fine-tuning: training reorganizes mid-to-exit layer action encoding and establishes instruction-conditioned action sensitivity, while early-layer attention structure reflects the pretrained backbone.\nThe consistency of these training-induced effects across two VLM-to-VLA transitions (TracVLA, NORA)---architectures with dramatically different base-model priors---is compatible with exit collapse and counterfactual sensitivity reflecting task-structure constraints of VLA fine-tuning rather than architecture-specific artifacts; OpenVLA's partial confirmation (2/4 suites for $R^2$ collapse) tempers the generality of this interpretation.\nA more detailed characterization of how these effects compose across training stages is developed in the Discussion (\\S\\ref{sec:discussion}).\n\nAs a secondary observation, vision encoder geometry measured by RSA shows a non-monotonic profile with a middle-layer peak (L12: $\\rho = 0.628$), and standalone DINOv2~\\cite{oquab2024_dinov2} achieves the highest RSA among encoders ($\\rho = 0.692$).\nUnder linear CKA~\\cite{kornblith2019}, this non-monotonic pattern disappears (monotonic increase), qualifying the observation as metric-dependent (Appendix~\\ref{sec:cka_appendix}).\n",
      "numLines": 209,
      "startLine": 1,
      "totalLines": 209
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01ArTMCppdJsmv3re22rdZZi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "e1e66ef8-bd6a-488c-a2d9-99cfa3eb252f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G8yMZBsZKzWdyQJDw1ynoE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13107,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13107
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

_source line 14 · 2026-05-22T05:46:26.787Z_

<details><summary>↩ Tool result · `toolu_01ArTMCppdJsmv3re22rdZZi`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}.
5	In these decoder-only architectures, image tokens precede instruction tokens in the input sequence, and the causal attention mask prevents image tokens from attending to any token that follows them~\cite{wang2025seeing,pei2025rethinking}.
6	Instruction information can reach action-generating positions only through later attention layers, where the readout token (the final position before action decoding) integrates context from all preceding tokens.
7	The readout is thus the sole multimodal integration point by construction.
8	How fine-tuning creates or reshapes the attention patterns at this position, and whether the resulting routing reflects training dynamics or inherited backbone structure, remains unknown.
9	
10	Behavioral studies provide indirect evidence that this question matters.
11	VLAs exhibit visual dominance, relying disproportionately on image input~\cite{grant2026}, and language instructions appear largely unused by the action pathway~\cite{haon2025}.
12	These observations establish that VLAs underweight instructions but do not explain \emph{how} instruction information reaches action-generating positions, \emph{what} routing structure training creates versus what it inherits from the pretrained backbone, or \emph{whether} observed patterns hold across architectures.
13	All existing representational analyses of VLAs target a single architecture.
14	No prior work tests whether instruction routing mechanisms are consistent across backbone families, and none decomposes training-induced effects from inherited base-model priors.
15	Absent cross-architecture evidence, it is impossible to distinguish training dynamics that reflect the causal-decoder structure from architecture-specific artifacts of a particular language model.
16	
17	We address this gap with a systematic cross-architecture analysis of three VLAs built on distinct backbones: OpenVLA~\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\cite{touvron2023_llama2}, 32 layers), TracVLA~\cite{zheng2024tracevla} (Phi-3-mini~\cite{abdin2024phi3}, 32 layers), and NORA~\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers).
18	Each architecture is evaluated across four LIBERO~\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon), forming a $3 \times 4$ matrix with 10 of 12 cells filled (\S\ref{sec:setup}).
19	A critical asymmetry structures the trained/untrained comparison: OpenVLA's untrained checkpoint is the OXE-pretrained~\cite{padalkar2023_oxe} VLA, already fine-tuned on 970K episodes for action prediction, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision, Qwen2.5-VL) with no action training.
20	The six TracVLA and NORA cells therefore test VLM-to-VLA transitions; the three OpenVLA cells test VLA-to-VLA transitions.
21	This design enables two types of inference: within-architecture trained/untrained contrasts identify what training changes, and cross-architecture comparisons test whether those changes are backbone-specific.
22	We apply five complementary analyses: cross-instruction probes, L1 attention head profiling, $R^2$ action probes, representational similarity analysis (RSA)~\cite{kriegeskorte2008}, and counterfactual instruction perturbation (\S\ref{sec:method}).
23	A single-architecture deep dive on OpenVLA (\S\ref{sec:openvla_routing}) establishes core phenomena before the cross-architecture comparisons.
24	
25	\begin{figure}[t]
26	\centering
27	\includegraphics[width=0.88\linewidth,height=2in,keepaspectratio]{figures/fig_teaser.pdf}
28	\vspace{-4pt}
29	\caption{\textbf{VLA fine-tuning reorganizes action-relevant representations in a pattern consistent across two VLM-to-VLA transitions but absent before action training.}
30	Three architectures are compared in trained and untrained conditions.
31	Training-induced effects ($R^2$ exit collapse, counterfactual sensitivity) emerge at the VLM-to-VLA transition, while L1 instruction attention reflects inherited base-model priors.}
32	\label{fig:teaser}
33	\end{figure}
34	
35	Three findings emerge from this cross-architecture comparison (Figure~\ref{fig:teaser}).
36	\emph{First}, $R^2$ exit collapse, the drop in action-probe $R^2$ from peak layer to exit layer, consistently marks VLM-to-VLA transitions.
37	All six TracVLA and NORA cells show larger trained $\Delta R^2$ than untrained $\Delta R^2$: TracVLA trained collapse ranges from $0.138$ to $0.294$ (untrained: $0.009$--$0.048$), and NORA trained collapse reaches $0.691$ on Goal, where exit-layer $R^2$ drops below zero (untrained: $0.044$).
38	A one-sided sign test confirms this direction across all six cells ($p = 0.016$).
39	In contrast, only one of three VLA-to-VLA cells (OpenVLA Object) shows the same pattern.
40	The 6/6 versus 1/3 contrast identifies exit collapse as a one-time reorganization that occurs when a vision-language model is first fine-tuned into a VLA (\S\ref{sec:r2_collapse}).
41	
42	\emph{Second}, all trained VLAs exhibit substantial counterfactual sensitivity to instruction perturbation.
43	Across eight cells where Cohen's $d$ is applicable (OpenVLA and TracVLA, four suites each), every perturbation condition produces $d \geq 0.45$, with empty-instruction perturbation ranking first in seven of eight cells ($d = 0.94$--$1.52$).
44	Paraphrased instructions preserve meaning while changing surface tokens, yet they rank last in seven of eight cells; VLAs thus encode instruction content beyond token-level matching.
45	A metric constraint limits trained/untrained comparison: untrained VLMs do not produce actions, so their sensitivity is measured via cosine distance on hidden representations rather than Cohen's $d$ on action MSE.
46	These metrics operate on different scales; cross-metric ratios are invalid and we do not report amplification factors (\S\ref{sec:cf_sensitivity}).
47	
48	\emph{Third}, L1 instruction-dominant attention reflects base-model language pretraining rather than VLA fine-tuning.
49	TracVLA's untrained checkpoint (Phi-3-Vision) allocates 32/32 attention heads to instruction dominance across all four suites before any action training; VLA training slightly \emph{reduces} this count to 27--30/32.
50	NORA untrained (Qwen2.5-VL) shows 13--14 of 16 heads instruction-dominant, unchanged by training.
51	If VLA training were the primary driver of L1 instruction routing, untrained VLMs should show low instruction attention that increases after training, as observed in OpenVLA's random-weight condition (0/32 heads).
52	The saturation before training provides direct evidence that L1 patterns are inherited priors (\S\ref{sec:l1_priors}).
53	
54	Our contributions are:
55	\begin{enumerate}
56	\item An empirical cross-architecture representational analysis framework for VLAs, combining factorial trained/untrained controls with token-level probing across a $3 \times 4$ architecture-suite matrix.
57	\item Identification of $R^2$ exit collapse as a marker of the VLM-to-VLA transition, consistent across two VLM-to-VLA architectures (TracVLA, NORA) with partial confirmation in OpenVLA (2/4 suites).
58	\item A decomposition of VLA instruction routing into training-induced effects (exit collapse, counterfactual sensitivity) and inherited base-model priors (L1 instruction attention), grounded in cross-architecture trained/untrained contrasts.
59	\end{enumerate}
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "8a9385eb-5e10-4b8a-ac04-c69c73b7b020",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla}.\nIn these decoder-only architectures, image tokens precede instruction tokens in the input sequence, and the causal attention mask prevents image tokens from attending to any token that follows them~\\cite{wang2025seeing,pei2025rethinking}.\nInstruction information can reach action-generating positions only through later attention layers, where the readout token (the final position before action decoding) integrates context from all preceding tokens.\nThe readout is thus the sole multimodal integration point by construction.\nHow fine-tuning creates or reshapes the attention patterns at this position, and whether the resulting routing reflects training dynamics or inherited backbone structure, remains unknown.\n\nBehavioral studies provide indirect evidence that this question matters.\nVLAs exhibit visual dominance, relying disproportionately on image input~\\cite{grant2026}, and language instructions appear largely unused by the action pathway~\\cite{haon2025}.\nThese observations establish that VLAs underweight instructions but do not explain \\emph{how} instruction information reaches action-generating positions, \\emph{what} routing structure training creates versus what it inherits from the pretrained backbone, or \\emph{whether} observed patterns hold across architectures.\nAll existing representational analyses of VLAs target a single architecture.\nNo prior work tests whether instruction routing mechanisms are consistent across backbone families, and none decomposes training-induced effects from inherited base-model priors.\nAbsent cross-architecture evidence, it is impossible to distinguish training dynamics that reflect the causal-decoder structure from architecture-specific artifacts of a particular language model.\n\nWe address this gap with a systematic cross-architecture analysis of three VLAs built on distinct backbones: OpenVLA~\\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\\cite{touvron2023_llama2}, 32 layers), TracVLA~\\cite{zheng2024tracevla} (Phi-3-mini~\\cite{abdin2024phi3}, 32 layers), and NORA~\\cite{TODO_nora} (Qwen2.5-VL-3B, 36 layers).\nEach architecture is evaluated across four LIBERO~\\cite{liu2023_libero} task suites (Goal, Spatial, Object, Long-Horizon), forming a $3 \\times 4$ matrix with 10 of 12 cells filled (\\S\\ref{sec:setup}).\nA critical asymmetry structures the trained/untrained comparison: OpenVLA's untrained checkpoint is the OXE-pretrained~\\cite{padalkar2023_oxe} VLA, already fine-tuned on 970K episodes for action prediction, while TracVLA and NORA untrained checkpoints are pure vision-language models (Phi-3-Vision, Qwen2.5-VL) with no action training.\nThe six TracVLA and NORA cells therefore test VLM-to-VLA transitions; the three OpenVLA cells test VLA-to-VLA transitions.\nThis design enables two types of inference: within-architecture trained/untrained contrasts identify what training changes, and cross-architecture comparisons test whether those changes are backbone-specific.\nWe apply five complementary analyses: cross-instruction probes, L1 attention head profiling, $R^2$ action probes, representational similarity analysis (RSA)~\\cite{kriegeskorte2008}, and counterfactual instruction perturbation (\\S\\ref{sec:method}).\nA single-architecture deep dive on OpenVLA (\\S\\ref{sec:openvla_routing}) establishes core phenomena before the cross-architecture comparisons.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.88\\linewidth,height=2in,keepaspectratio]{figures/fig_teaser.pdf}\n\\vspace{-4pt}\n\\caption{\\textbf{VLA fine-tuning reorganizes action-relevant representations in a pattern consistent across two VLM-to-VLA transitions but absent before action training.}\nThree architectures are compared in trained and untrained conditions.\nTraining-induced effects ($R^2$ exit collapse, counterfactual sensitivity) emerge at the VLM-to-VLA transition, while L1 instruction attention reflects inherited base-model priors.}\n\\label{fig:teaser}\n\\end{figure}\n\nThree findings emerge from this cross-architecture comparison (Figure~\\ref{fig:teaser}).\n\\emph{First}, $R^2$ exit collapse, the drop in action-probe $R^2$ from peak layer to exit layer, consistently marks VLM-to-VLA transitions.\nAll six TracVLA and NORA cells show larger trained $\\Delta R^2$ than untrained $\\Delta R^2$: TracVLA trained collapse ranges from $0.138$ to $0.294$ (untrained: $0.009$--$0.048$), and NORA trained collapse reaches $0.691$ on Goal, where exit-layer $R^2$ drops below zero (untrained: $0.044$).\nA one-sided sign test confirms this direction across all six cells ($p = 0.016$).\nIn contrast, only one of three VLA-to-VLA cells (OpenVLA Object) shows the same pattern.\nThe 6/6 versus 1/3 contrast identifies exit collapse as a one-time reorganization that occurs when a vision-language model is first fine-tuned into a VLA (\\S\\ref{sec:r2_collapse}).\n\n\\emph{Second}, all trained VLAs exhibit substantial counterfactual sensitivity to instruction perturbation.\nAcross eight cells where Cohen's $d$ is applicable (OpenVLA and TracVLA, four suites each), every perturbation condition produces $d \\geq 0.45$, with empty-instruction perturbation ranking first in seven of eight cells ($d = 0.94$--$1.52$).\nParaphrased instructions preserve meaning while changing surface tokens, yet they rank last in seven of eight cells; VLAs thus encode instruction content beyond token-level matching.\nA metric constraint limits trained/untrained comparison: untrained VLMs do not produce actions, so their sensitivity is measured via cosine distance on hidden representations rather than Cohen's $d$ on action MSE.\nThese metrics operate on different scales; cross-metric ratios are invalid and we do not report amplification factors (\\S\\ref{sec:cf_sensitivity}).\n\n\\emph{Third}, L1 instruction-dominant attention reflects base-model language pretraining rather than VLA fine-tuning.\nTracVLA's untrained checkpoint (Phi-3-Vision) allocates 32/32 attention heads to instruction dominance across all four suites before any action training; VLA training slightly \\emph{reduces} this count to 27--30/32.\nNORA untrained (Qwen2.5-VL) shows 13--14 of 16 heads instruction-dominant, unchanged by training.\nIf VLA training were the primary driver of L1 instruction routing, untrained VLMs should show low instruction attention that increases after training, as observed in OpenVLA's random-weight condition (0/32 heads).\nThe saturation before training provides direct evidence that L1 patterns are inherited priors (\\S\\ref{sec:l1_priors}).\n\nOur contributions are:\n\\begin{enumerate}\n\\item An empirical cross-architecture representational analysis framework for VLAs, combining factorial trained/untrained controls with token-level probing across a $3 \\times 4$ architecture-suite matrix.\n\\item Identification of $R^2$ exit collapse as a marker of the VLM-to-VLA transition, consistent across two VLM-to-VLA architectures (TracVLA, NORA) with partial confirmation in OpenVLA (2/4 suites).\n\\item A decomposition of VLA instruction routing into training-induced effects (exit collapse, counterfactual sensitivity) and inherited base-model priors (L1 instruction attention), grounded in cross-architecture trained/untrained contrasts.\n\\end{enumerate}\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 60
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the new Discussion + Limitations section based on the detailed specifications provided. Let me carefully synthesize the information from the experiments and introduction sections to create the new discussion.

Key points to include:

**Synthesis (~150 words):**
- Core effect of VLA fine-tuning: reorganize mid-to-exit layer action encoding (R² exit collapse) + establish instruction-conditioned sensitivity (CF)
- These effects concentrate at readout token, not image geometry (OpenVLA: readout +0.069, image_mean +0.015)
- L1 instruction attention is inherited from base-model pretraining, not created by VLA training


- This decomposition (training-induced vs inherited) is the core framing

**Cross-architecture consistency (~100 words):**
- Two VLM-to-VLA transitions show the same pattern despite vastly different starting points: one model saturated at 32/32 while the other started at 13-14/16
- Both exhibit exit collapse and instruction-conditioned sensitivity, suggesting these emerge from the causal-decoder VLA design itself rather than being architecture-independent
- However, OpenVLA only partially confirms this pattern across suites, so I should frame this as consistent across the two transitions but with important caveats about generalization

**Three-tier gradient observation:**
- Looking at how performance degrades across three model categories: VLM bases show inherited attention patterns with minimal collapse, general OXE-pretrained VLAs display moderate routing and sensitivity, while task-specific VLAs exhibit the strongest exit collapse and instruction sensitivity
- The pattern holds across the first two tiers, but the third tier (task-specific) is where the effect becomes pronounced and statistically significant
- This suggests a progression tied to how much task-specific training has occurred

, though I need more general VLA examples like Octo and Pi0 to properly validate the middle tier

**Metric and scope limitations:**
- Cohen's d and cosine distance measure different things (action space vs representation space) and aren't directly comparable, which complicates cross-condition analysis
- The OpenVLA inversion results show how misleading metric ratios can be when comparing across different measurement types
- I'm also working with limited architectural diversity—only two VLM-to-VLA transitions and one VLA-to-VLA case, plus a single dataset (LIBERO), which constrains how broadly these findings generalize
- I haven't examined flow-matching or diffusion-based approaches, only causal decoders, and I'm analyzing static checkpoints rather than training trajectories
- The open-loop setup is consistent with recent work but needs closed-loop validation to be fully convincing

**Constraints for the paper:**
- Can't claim architecture-independence or 7-10× amplification without stronger evidence
- The three-tier pattern is an observation, not a validated contribution
- Need to avoid "significantly" without proper statistical backing
- Must cite NORA and TracVLA appropriately and cross-reference the relevant sections on representation collapse

, sensitivity analysis, priors, and routing

Now I'm drafting the discussion section carefully, making sure each sentence adds new information and avoiding common pitfalls like em-dashes, -ing phrase endings, and unsupported claims.

The next chunk describes the key empirical findings: fine-tuning produces two main representational shifts—one in how actions are encoded at the exit layer and another in instruction-conditioned sensitivity—both localized to the readout token rather than spreading across the image encoding. The data shows this concretely with specific $R^2$ changes on OpenVLA. Meanwhile, instruction attention patterns in the first layer aren't learned during fine-tuning but rather inherited from the base model's pretraining, with different models showing different saturation points. The thought trails off into discussing how these effects decompose into what's newly trained versus what's carried over from pretraining.

The continuation then completes that decomposition framing and pivots to cross-architecture consistency: despite starting from very different configurations, both TracVLA and NORA show the same training-induced effects (exit collapse and counterfactual sensitivity) across all test conditions, suggesting these aren't architecture-specific quirks but rather emerge from the task structure of causal-decoder VLA design. OpenVLA partially confirms this pattern.

So the key insight is that VLA fine-tuning reorganizes downstream representations while keeping early attention patterns intact, and this mechanism holds across different architectures—it's a fundamental property of how these models adapt to action prediction rather than an artifact of any particular design choice. Tier 2 shows strong routing and moderate sensitivity without systematic collapse, while Tier 3 exhibits collapse across all task-specific cells with substantial sensitivity—a pattern suggesting representational adaptation increases with training specificity, though the boundary between tiers conflates architecture with training stage, limiting the conclusions I can draw without testing additional general-purpose models.

The counterfactual sensitivity metrics themselves present a challenge: I'm using different measures (Cohen's d for action MSE versus cosine distance for representations) that aren't directly comparable, and the OpenVLA example shows how the same model can flip its relative ranking depending on which metric is applied, so establishing a unified framework for cross-condition comparisons remains an open question.

Our findings depend on just two independent VLM-to-VLA transitions, while OpenVLA only tests a VLA-to-VLA case, so we'd need additional independent confirmations to solidify the pattern. The experiments are limited to LIBERO's short-horizon tabletop tasks, and testing on richer language-grounded benchmarks like CALVIN and Language-Table would help determine if these patterns hold more broadly. I'm also only examining causal-decoder architectures, whereas flow-matching and diffusion-based models using cross-attention might show different routing behaviors.

Beyond that, each checkpoint represents a single snapshot in training, so I can't track how exit collapse or counterfactual sensitivity evolve over time. The analyses are all open-loop, which aligns with prior representational work but means closed-loop validation would strengthen claims about behavioral relevance. NORA data is incomplete—only 2 of 4 suites have checkpoints available. The three-tier gradient framework has just one example at the middle tier, which limits how much I can infer from it, and populating that tier with more general-purpose VLAs would be essential moving forward. Now I'm verifying the word counts match the requirements—discussion should be around 500 words and limitations around 150—and double-checking that my cross-references to the experimental sections are accurate. I also need to make sure I'm not using em-dashes in the LaTeX and that I've included the citation to Grant et al. as specified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "2e9a0792-5860-4e3b-a201-35e139d164ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7x4HZm9GDiUuVE5H2nXTK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21869,
      "cache_read_input_tokens": 24948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21869
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

_source line 16_

Now writing the rewritten Discussion + Limitations section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "ca323458-9d6c-452e-a1f7-be7798b7b414",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7x4HZm9GDiUuVE5H2nXTK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21869,
      "cache_read_input_tokens": 24948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21869
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

_source line 17_

<details open><summary>🔧 Tool call — Write · `toolu_01D14QeVQ6fyJksquzZCXqHc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "content": "\\vspace{-2pt}\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \\S\\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\\S\\ref{sec:cf_sensitivity}).\nBoth effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\\_mean by only $+0.015$ (\\S\\ref{sec:openvla_routing}).\nL1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\\S\\ref{sec:l1_priors}).\nThis decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.\nVLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.\n\n\\paragraph{Cross-architecture consistency.}\nTwo VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.\nTracVLA~\\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.\nThis convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.\nThe pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\\ untrained $d = 1.05$).\nOpenVLA's OXE-pretrained baseline is itself a VLA rather than a VLM, so its cells test a different transition type.\nWe characterize the training-induced effects as consistent across two VLM-to-VLA architectures, with partial confirmation in a third under VLA-to-VLA conditions.\n\n\\paragraph{Observational three-tier gradient.}\nThe cross-architecture matrix suggests a three-tier gradient of representational adaptation, reported here as an observational synthesis rather than a validated finding.\nTier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\\Delta R^2 \\leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\\leq 0.185$).\nTier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \\approx 1.0$), and no systematic exit collapse across suites.\nTier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell (6/6, $p = 0.016$) and substantial counterfactual sensitivity ($d \\geq 0.45$).\nThis gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.\nTesting additional general-purpose VLAs (e.g., Octo~\\cite{ghosh2024_octo}, $\\pi_0$~\\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.\n\n\\paragraph{Metric constraints.}\nCounterfactual sensitivity is measured via Cohen's $d$ on action MSE for models that produce actions and via cosine distance on hidden representations for untrained VLMs (\\S\\ref{sec:cf_sensitivity}).\nThese metrics differ in scale and distributional properties; ratios between them are not meaningful.\nThe OpenVLA Long-Horizon inversion (trained $d = 0.56$, untrained $d = 1.05$) illustrates how same-metric comparisons can reverse the expected direction, cautioning against overinterpretation of any single cell.\nA standardized metric framework for cross-condition counterfactual comparison remains an open problem.\n\n\\subsection*{Limitations}\nOur cross-architecture evidence rests on two independent VLM-to-VLA transitions (TracVLA~\\cite{zheng2024tracevla}, NORA~\\cite{TODO_nora}); OpenVLA tests a VLA-to-VLA transition and does not constitute an independent third VLM-to-VLA confirmation.\nAll experiments use LIBERO~\\cite{liu2023_libero} (10 tasks per suite); benchmarks with richer language grounding such as CALVIN and Language-Table are needed to test whether the observed patterns generalize beyond short-horizon tabletop manipulation.\nWe analyze only causal-decoder VLAs; flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} architectures that employ cross-attention rather than causal masking may exhibit different routing mechanisms.\nEach architecture is analyzed at a single trained checkpoint, precluding characterization of how exit collapse or counterfactual sensitivity emerge during training.\nAll analyses are open-loop, consistent with prior representational studies~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence about the behavioral relevance of the identified routing structures.\nNORA checkpoints are available for only 2 of 4 suites, leaving Object and Long-Horizon cells empty.\nThe three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "bf538017-3d8c-464c-ac1b-e6414af95481",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7x4HZm9GDiUuVE5H2nXTK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21869,
      "cache_read_input_tokens": 24948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21869
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

_source line 18 · 2026-05-22T05:47:44.325Z_

<details><summary>↩ Tool result · `toolu_01D14QeVQ6fyJksquzZCXqHc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "9453c229-c392-4751-807b-84b1488573ad",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "content": "\\vspace{-2pt}\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \\S\\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\\S\\ref{sec:cf_sensitivity}).\nBoth effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\\_mean by only $+0.015$ (\\S\\ref{sec:openvla_routing}).\nL1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\\S\\ref{sec:l1_priors}).\nThis decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.\nVLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.\n\n\\paragraph{Cross-architecture consistency.}\nTwo VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.\nTracVLA~\\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.\nThis convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.\nThe pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\\ untrained $d = 1.05$).\nOpenVLA's OXE-pretrained baseline is itself a VLA rather than a VLM, so its cells test a different transition type.\nWe characterize the training-induced effects as consistent across two VLM-to-VLA architectures, with partial confirmation in a third under VLA-to-VLA conditions.\n\n\\paragraph{Observational three-tier gradient.}\nThe cross-architecture matrix suggests a three-tier gradient of representational adaptation, reported here as an observational synthesis rather than a validated finding.\nTier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\\Delta R^2 \\leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\\leq 0.185$).\nTier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \\approx 1.0$), and no systematic exit collapse across suites.\nTier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell (6/6, $p = 0.016$) and substantial counterfactual sensitivity ($d \\geq 0.45$).\nThis gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.\nTesting additional general-purpose VLAs (e.g., Octo~\\cite{ghosh2024_octo}, $\\pi_0$~\\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.\n\n\\paragraph{Metric constraints.}\nCounterfactual sensitivity is measured via Cohen's $d$ on action MSE for models that produce actions and via cosine distance on hidden representations for untrained VLMs (\\S\\ref{sec:cf_sensitivity}).\nThese metrics differ in scale and distributional properties; ratios between them are not meaningful.\nThe OpenVLA Long-Horizon inversion (trained $d = 0.56$, untrained $d = 1.05$) illustrates how same-metric comparisons can reverse the expected direction, cautioning against overinterpretation of any single cell.\nA standardized metric framework for cross-condition counterfactual comparison remains an open problem.\n\n\\subsection*{Limitations}\nOur cross-architecture evidence rests on two independent VLM-to-VLA transitions (TracVLA~\\cite{zheng2024tracevla}, NORA~\\cite{TODO_nora}); OpenVLA tests a VLA-to-VLA transition and does not constitute an independent third VLM-to-VLA confirmation.\nAll experiments use LIBERO~\\cite{liu2023_libero} (10 tasks per suite); benchmarks with richer language grounding such as CALVIN and Language-Table are needed to test whether the observed patterns generalize beyond short-horizon tabletop manipulation.\nWe analyze only causal-decoder VLAs; flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} architectures that employ cross-attention rather than causal masking may exhibit different routing mechanisms.\nEach architecture is analyzed at a single trained checkpoint, precluding characterization of how exit collapse or counterfactual sensitivity emerge during training.\nAll analyses are open-loop, consistent with prior representational studies~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence about the behavioral relevance of the identified routing structures.\nNORA checkpoints are available for only 2 of 4 suites, leaving Object and Long-Horizon cells empty.\nThe three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 11,
        "newStart": 3,
        "newLines": 39,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " \\paragraph{Synthesis.}",
          "-VLA fine-tuning redistributes instruction attention rather than reshaping visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$), explaining Grant et al.'s~\\cite{grant2026} visual dominance finding ($\\rho = 0.692$ for DINOv2, yet readout $R^2 = 0.678$ vs.\\ $0.634$).",
          "-Cross-architecture comparison strengthens this picture: two VLAs with different backbones and opposite untrained profiles both arrive at similar mid-layer peaks ($\\Delta = 0.003$), suggesting the redistribution reflects task-structure constraints rather than architecture-specific artifacts.",
          "-Seven analyses support L1 redistribution: \\emph{interventional} (dose-response $d = 0.48 \\to 0.64$; counterfactual $d = 0.71$--$0.98$, replicating across both LIBERO suites), \\emph{supporting} (gradient $0 \\to 9 \\to 24$ heads; ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} ($p = 0.0018$; $z = -3.11$, $0$\\textsuperscript{th} percentile; Appendix~\\ref{sec:mechanistic_interpretation}--\\ref{sec:functional_stages}).",
          "+VLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \\S\\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\\S\\ref{sec:cf_sensitivity}).",
          "+Both effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\\_mean by only $+0.015$ (\\S\\ref{sec:openvla_routing}).",
          "+L1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\\S\\ref{sec:l1_priors}).",
          "+This decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.",
          "+VLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.",
          " ",
          "+\\paragraph{Cross-architecture consistency.}",
          "+Two VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.",
          "+TracVLA~\\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.",
          "+This convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.",
          "+The pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\\ untrained $d = 1.05$).",
          "+OpenVLA's OXE-pretrained baseline is itself a VLA rather than a VLM, so its cells test a different transition type.",
          "+We characterize the training-induced effects as consistent across two VLM-to-VLA architectures, with partial confirmation in a third under VLA-to-VLA conditions.",
          "+",
          "+\\paragraph{Observational three-tier gradient.}",
          "+The cross-architecture matrix suggests a three-tier gradient of representational adaptation, reported here as an observational synthesis rather than a validated finding.",
          "+Tier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\\Delta R^2 \\leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\\leq 0.185$).",
          "+Tier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \\approx 1.0$), and no systematic exit collapse across suites.",
          "+Tier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell (6/6, $p = 0.016$) and substantial counterfactual sensitivity ($d \\geq 0.45$).",
          "+This gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.",
          "+Testing additional general-purpose VLAs (e.g., Octo~\\cite{ghosh2024_octo}, $\\pi_0$~\\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.",
          "+",
          "+\\paragraph{Metric constraints.}",
          "+Counterfactual sensitivity is measured via Cohen's $d$ on action MSE for models that produce actions and via cosine distance on hidden representations for untrained VLMs (\\S\\ref{sec:cf_sensitivity}).",
          "+These metrics differ in scale and distributional properties; ratios between them are not meaningful.",
          "+The OpenVLA Long-Horizon inversion (trained $d = 0.56$, untrained $d = 1.05$) illustrates how same-metric comparisons can reverse the expected direction, cautioning against overinterpretation of any single cell.",
          "+A standardized metric framework for cross-condition counterfactual comparison remains an open problem.",
          "+",
          " \\subsection*{Limitations}",
          "-We analyze two causal-decoder VLAs on held-out LIBERO (Goal and Spatial, 10 tasks each); extending to flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} VLAs with cross-attention, and to benchmarks with richer language grounding (e.g., CALVIN, Language-Table), is needed to test generality.",
          "-Llama-2's 9/32 pretrained instruction-dominant heads may reflect text bias ($+15$-head delta isolates fine-tuning); we analyze only the final checkpoint, preventing characterization of routing emergence dynamics.",
          "-All analyses are open-loop~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence, though consistent mid-layer peaks suggest early-exit inference at ${\\sim}1/3$ depth as a testable hypothesis.",
          "+Our cross-architecture evidence rests on two independent VLM-to-VLA transitions (TracVLA~\\cite{zheng2024tracevla}, NORA~\\cite{TODO_nora}); OpenVLA tests a VLA-to-VLA transition and does not constitute an independent third VLM-to-VLA confirmation.",
          "+All experiments use LIBERO~\\cite{liu2023_libero} (10 tasks per suite); benchmarks with richer language grounding such as CALVIN and Language-Table are needed to test whether the observed patterns generalize beyond short-horizon tabletop manipulation.",
          "+We analyze only causal-decoder VLAs; flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} architectures that employ cross-attention rather than causal masking may exhibit different routing mechanisms.",
          "+Each architecture is analyzed at a single trained checkpoint, precluding characterization of how exit collapse or counterfactual sensitivity emerge during training.",
          "+All analyses are open-loop, consistent with prior representational studies~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence about the behavioral relevance of the identified routing structures.",
          "+NORA checkpoints are available for only 2 of 4 suites, leaving Object and Long-Horizon cells empty.",
          "+The three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work."
        ]
      }
    ],
    "originalFile": "\\vspace{-2pt}\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning redistributes instruction attention rather than reshaping visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$), explaining Grant et al.'s~\\cite{grant2026} visual dominance finding ($\\rho = 0.692$ for DINOv2, yet readout $R^2 = 0.678$ vs.\\ $0.634$).\nCross-architecture comparison strengthens this picture: two VLAs with different backbones and opposite untrained profiles both arrive at similar mid-layer peaks ($\\Delta = 0.003$), suggesting the redistribution reflects task-structure constraints rather than architecture-specific artifacts.\nSeven analyses support L1 redistribution: \\emph{interventional} (dose-response $d = 0.48 \\to 0.64$; counterfactual $d = 0.71$--$0.98$, replicating across both LIBERO suites), \\emph{supporting} (gradient $0 \\to 9 \\to 24$ heads; ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} ($p = 0.0018$; $z = -3.11$, $0$\\textsuperscript{th} percentile; Appendix~\\ref{sec:mechanistic_interpretation}--\\ref{sec:functional_stages}).\n\n\\subsection*{Limitations}\nWe analyze two causal-decoder VLAs on held-out LIBERO (Goal and Spatial, 10 tasks each); extending to flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} VLAs with cross-attention, and to benchmarks with richer language grounding (e.g., CALVIN, Language-Table), is needed to test generality.\nLlama-2's 9/32 pretrained instruction-dominant heads may reflect text bias ($+15$-head delta isolates fine-tuning); we analyze only the final checkpoint, preventing characterization of routing emergence dynamics.\nAll analyses are open-loop~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence, though consistent mid-layer peaks suggest early-exit inference at ${\\sim}1/3$ depth as a testable hypothesis.\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_017WGxxzH3HC6mc43LceDEX2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "19b8763d-fa9a-42d0-8154-c82c18c30007",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TcHcuU5TwMMtgbcWLjV3A6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4756,
      "cache_read_input_tokens": 46817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4756
      },
      "output_tokens": 61,
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

_source line 20 · 2026-05-22T05:47:48.709Z_

<details><summary>↩ Tool result · `toolu_017WGxxzH3HC6mc43LceDEX2`</summary>

```text
1	\vspace{-2pt}
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\paragraph{Synthesis.}
6	VLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \S\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\S\ref{sec:cf_sensitivity}).
7	Both effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\_mean by only $+0.015$ (\S\ref{sec:openvla_routing}).
8	L1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\S\ref{sec:l1_priors}).
9	This decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.
10	VLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.
11	
12	\paragraph{Cross-architecture consistency.}
13	Two VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.
14	TracVLA~\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.
15	This convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.
16	The pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\ untrained $d = 1.05$).
17	OpenVLA's OXE-pretrained baseline is itself a VLA rather than a VLM, so its cells test a different transition type.
18	We characterize the training-induced effects as consistent across two VLM-to-VLA architectures, with partial confirmation in a third under VLA-to-VLA conditions.
19	
20	\paragraph{Observational three-tier gradient.}
21	The cross-architecture matrix suggests a three-tier gradient of representational adaptation, reported here as an observational synthesis rather than a validated finding.
22	Tier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\Delta R^2 \leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\leq 0.185$).
23	Tier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \approx 1.0$), and no systematic exit collapse across suites.
24	Tier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell (6/6, $p = 0.016$) and substantial counterfactual sensitivity ($d \geq 0.45$).
25	This gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.
26	Testing additional general-purpose VLAs (e.g., Octo~\cite{ghosh2024_octo}, $\pi_0$~\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.
27	
28	\paragraph{Metric constraints.}
29	Counterfactual sensitivity is measured via Cohen's $d$ on action MSE for models that produce actions and via cosine distance on hidden representations for untrained VLMs (\S\ref{sec:cf_sensitivity}).
30	These metrics differ in scale and distributional properties; ratios between them are not meaningful.
31	The OpenVLA Long-Horizon inversion (trained $d = 0.56$, untrained $d = 1.05$) illustrates how same-metric comparisons can reverse the expected direction, cautioning against overinterpretation of any single cell.
32	A standardized metric framework for cross-condition counterfactual comparison remains an open problem.
33	
34	\subsection*{Limitations}
35	Our cross-architecture evidence rests on two independent VLM-to-VLA transitions (TracVLA~\cite{zheng2024tracevla}, NORA~\cite{TODO_nora}); OpenVLA tests a VLA-to-VLA transition and does not constitute an independent third VLM-to-VLA confirmation.
36	All experiments use LIBERO~\cite{liu2023_libero} (10 tasks per suite); benchmarks with richer language grounding such as CALVIN and Language-Table are needed to test whether the observed patterns generalize beyond short-horizon tabletop manipulation.
37	We analyze only causal-decoder VLAs; flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} architectures that employ cross-attention rather than causal masking may exhibit different routing mechanisms.
38	Each architecture is analyzed at a single trained checkpoint, precluding characterization of how exit collapse or counterfactual sensitivity emerge during training.
39	All analyses are open-loop, consistent with prior representational studies~\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence about the behavioral relevance of the identified routing structures.
40	NORA checkpoints are available for only 2 of 4 suites, leaving Object and Long-Horizon cells empty.
41	The three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work.
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "5b89e40d-6384-4d90-81d6-b2d7db208212",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\vspace{-2pt}\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning produces two measurable representational changes: it reorganizes mid-to-exit layer action encoding ($R^2$ exit collapse, \\S\\ref{sec:r2_collapse}) and establishes instruction-conditioned action sensitivity (\\S\\ref{sec:cf_sensitivity}).\nBoth effects concentrate at the readout token rather than image geometry: on OpenVLA, training shifts readout $R^2$ by $+0.069$ but image\\_mean by only $+0.015$ (\\S\\ref{sec:openvla_routing}).\nL1 instruction attention, by contrast, is inherited from base-model pretraining and persists through fine-tuning: Phi-3-Vision saturates at 32/32 instruction-dominant heads before any action training, and Qwen2.5-VL allocates 13--14/16 (\\S\\ref{sec:l1_priors}).\nThis decomposition into training-induced effects (exit collapse, counterfactual sensitivity) and inherited effects (L1 instruction attention) constitutes the central framing of our analysis.\nVLA fine-tuning does not build instruction routing from scratch; it reorganizes downstream representations while preserving the early-layer attention structure of the pretrained backbone.\n\n\\paragraph{Cross-architecture consistency.}\nTwo VLM-to-VLA transitions with dramatically different starting points converge on the same training-induced effects.\nTracVLA~\\cite{zheng2024tracevla} (Phi-3-Vision, 32/32 L1 heads saturated) and NORA~\\cite{TODO_nora} (Qwen2.5-VL, 13--14/16) both exhibit exit collapse at every tested suite (6/6 cells, sign test $p = 0.016$) and produce substantial counterfactual sensitivity after training.\nThis convergence is compatible with task-structure constraints of causal-decoder VLA design rather than architecture-specific artifacts.\nThe pattern is partially confirmed in OpenVLA, where only 2 of 4 suites show $R^2$ collapse and Long-Horizon counterfactual sensitivity inverts (trained $d = 0.56$ vs.\\ untrained $d = 1.05$).\nOpenVLA's OXE-pretrained baseline is itself a VLA rather than a VLM, so its cells test a different transition type.\nWe characterize the training-induced effects as consistent across two VLM-to-VLA architectures, with partial confirmation in a third under VLA-to-VLA conditions.\n\n\\paragraph{Observational three-tier gradient.}\nThe cross-architecture matrix suggests a three-tier gradient of representational adaptation, reported here as an observational synthesis rather than a validated finding.\nTier~1 (VLM bases, no action training): inherited L1 attention (TracVLA 32/32, NORA 13--14/16), negligible exit collapse ($\\Delta R^2 \\leq 0.048$), and minimal counterfactual sensitivity (cosine distance $\\leq 0.185$).\nTier~2 (general-purpose VLA, OXE-pretrained): strong L1 routing (24--26/32 heads), moderate counterfactual sensitivity ($d \\approx 1.0$), and no systematic exit collapse across suites.\nTier~3 (task-specific VLAs, fine-tuned on LIBERO): exit collapse at every VLM-to-VLA cell (6/6, $p = 0.016$) and substantial counterfactual sensitivity ($d \\geq 0.45$).\nThis gradient is suggestive but limited: Tier~2 contains a single architecture (OpenVLA), and the Tier~2/Tier~3 boundary confounds training stage with architecture.\nTesting additional general-purpose VLAs (e.g., Octo~\\cite{ghosh2024_octo}, $\\pi_0$~\\cite{black2024_pi0}) at Tier~2 is necessary before the three-tier structure can be treated as a robust empirical pattern.\n\n\\paragraph{Metric constraints.}\nCounterfactual sensitivity is measured via Cohen's $d$ on action MSE for models that produce actions and via cosine distance on hidden representations for untrained VLMs (\\S\\ref{sec:cf_sensitivity}).\nThese metrics differ in scale and distributional properties; ratios between them are not meaningful.\nThe OpenVLA Long-Horizon inversion (trained $d = 0.56$, untrained $d = 1.05$) illustrates how same-metric comparisons can reverse the expected direction, cautioning against overinterpretation of any single cell.\nA standardized metric framework for cross-condition counterfactual comparison remains an open problem.\n\n\\subsection*{Limitations}\nOur cross-architecture evidence rests on two independent VLM-to-VLA transitions (TracVLA~\\cite{zheng2024tracevla}, NORA~\\cite{TODO_nora}); OpenVLA tests a VLA-to-VLA transition and does not constitute an independent third VLM-to-VLA confirmation.\nAll experiments use LIBERO~\\cite{liu2023_libero} (10 tasks per suite); benchmarks with richer language grounding such as CALVIN and Language-Table are needed to test whether the observed patterns generalize beyond short-horizon tabletop manipulation.\nWe analyze only causal-decoder VLAs; flow-matching~\\cite{black2024_pi0} and diffusion~\\cite{ghosh2024_octo} architectures that employ cross-attention rather than causal masking may exhibit different routing mechanisms.\nEach architecture is analyzed at a single trained checkpoint, precluding characterization of how exit collapse or counterfactual sensitivity emerge during training.\nAll analyses are open-loop, consistent with prior representational studies~\\cite{grant2026,haon2025}; closed-loop validation would provide complementary evidence about the behavioral relevance of the identified routing structures.\nNORA checkpoints are available for only 2 of 4 suites, leaving Object and Long-Horizon cells empty.\nThe three-tier gradient has $n = 1$ at Tier~2, limiting its inferential power; populating this tier with additional general-purpose VLAs is a priority for future work.\n",
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

写入完成。Discussion + Limitations 已完全重写，覆盖全部要求的结构：

- **Synthesis**: training-induced vs inherited decomposition，readout concentration（+0.069 vs +0.015）
- **Cross-architecture consistency**: 6/6 VLM→VLA collapse + partial OpenVLA confirmation，措辞避开 "architecture-independent"
- **Three-tier gradient**: 明确标记为 observational synthesis，声明 n=1 at Tier 2 的局限
- **Metric constraints**: Cohen's d vs cosine 不可比，Long-Horizon inversion 作为警示
- **Limitations**: 7 点全部覆盖（VLA→VLA vs VLM→VLA 区分、LIBERO only、causal-decoder only、single checkpoint、open-loop、NORA 2/4、n=1 Tier 2）

无 em-dash、无 -ing 分词结尾、无 "architecture-independent"、无 "7-10×"、无未经检验的 "significantly"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "uuid": "b9a11618-7f43-4836-9ca8-a3d50407a7df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6ko2HBz2kBTYf7jh3p6Mq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1693,
      "cache_read_input_tokens": 51573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1693
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

_source line 22_

写入完成。Discussion + Limitations 已完全重写，覆盖全部要求的结构：

- **Synthesis**: training-induced vs inherited decomposition，readout concentration（+0.069 vs +0.015）
- **Cross-architecture consistency**: 6/6 VLM→VLA collapse + partial OpenVLA confirmation，措辞避开 "architecture-independent"
- **Three-tier gradient**: 明确标记为 observational synthesis，声明 n=1 at Tier 2 的局限
- **Metric constraints**: Cohen's d vs cosine 不可比，Long-Horizon inversion 作为警示
- **Limitations**: 7 点全部覆盖（VLA→VLA vs VLM→VLA 区分、LIBERO only、causal-decoder only、single checkpoint、open-loop、NORA 2/4、n=1 Tier 2）

无 em-dash、无 -ing 分词结尾、无 "architecture-independent"、无 "7-10×"、无未经检验的 "significantly"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 102314,
  "duration_api_ms": 103628,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "f2327bd6-7ca2-4ac5-85b4-f9b59e2ec4e5",
  "total_cost_usd": 0.46487075,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 41425,
    "cache_read_input_tokens": 135179,
    "output_tokens": 5432,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41425,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 276,
        "cache_read_input_tokens": 51573,
        "cache_creation_input_tokens": 1693,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1693
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2440,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0025499999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 5432,
      "cacheReadInputTokens": 135179,
      "cacheCreationInputTokens": 41425,
      "webSearchRequests": 0,
      "costUSD": 0.46232075000000006,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "dc9988e5-9ea4-42f0-9bfa-833ae26f6af2"
}
```

</details>

---
