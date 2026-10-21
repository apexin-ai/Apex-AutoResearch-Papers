# paper writing discussion

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_discussion_20260526T173335.log`
- **Structured JSON:** [`d8c549e5dae617e69358.json`](../../sessions/d8/d8c549e5dae617e69358.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
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
  "uuid": "e6a1eba9-479f-4aec-a006-fa178b80bc32",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779819600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "44a905eb-6d4b-425d-9da9-802d76456f93",
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf"
}
```

---

### Assistant

_source line 4_

I'll read the required files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "2499aebf-4bb8-42ea-b9b0-08a82b318b7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XnwAL9VPYqNUcEwFG12k7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13520,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13520
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_018GHjt2fLAroNKSkLzmGit9`</summary>

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
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "368d9d82-ade3-4930-94c6-101c4eca59eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XnwAL9VPYqNUcEwFG12k7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13520,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13520
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

_source line 6 · 2026-05-26T17:33:46.666Z_

<details><summary>↩ Tool result · `toolu_018GHjt2fLAroNKSkLzmGit9`</summary>

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
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "ab266426-b91a-45f5-a23d-240741540f1b",
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

<details open><summary>🔧 Tool call — Read · `toolu_012rtnELnr5pL74sr5DgCh7p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "9670299e-8bfb-4fe7-bc59-ee54d93399e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XnwAL9VPYqNUcEwFG12k7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13520,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13520
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

_source line 8 · 2026-05-26T17:33:47.126Z_

<details><summary>↩ Tool result · `toolu_012rtnELnr5pL74sr5DgCh7p`</summary>

```text
1	\section{Introduction}\label{sec:intro}
2	
3	Vision-Language-Action (VLA) models that operate in physical environments must avoid collisions with objects and people. Collision incidents cause task failure, risk damage to the robot and its surroundings, and represent a primary barrier to deploying VLAs outside controlled laboratory settings~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa}, an extension of the LIBERO simulation platform~\cite{liu2023libero}, provides the first systematic protocol for measuring collision behavior in VLA manipulation tasks, reporting the Collision Avoidance Rate (CAR) as the fraction of episodes free from robot-obstacle contact. Recent methods have adopted this evaluation framework to demonstrate safety improvements: SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstration learning~\cite{cofreeevla2026} all report high CAR under standard evaluation. Our own SDF-augmented Pi0~\cite{black2024pi0} configuration reaches 91.5\% CAR across 800 evaluation episodes (four independent runs). The collision avoidance problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\fbox{\parbox{0.92\linewidth}{\vspace{3.5cm}\centering\textit{Placeholder: Figure 1. The fake safety problem.\\Left: Pi0+A1 achieves CAR\,=\,91.5\% but TSR\,=\,0\% (robot frozen, displacement $<$\,0.1\,mm).\\Center: Displacement-filtered CAR$_\text{f}$ drops Pi0+A1 to ${\approx}$\,0\%.\\Right: Pi0.5 achieves CAR\,=\,28.5\% with TSR\,=\,71.5\% (all safe episodes above 288\,mm displacement).}\vspace{3.5cm}}}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR$_\text{f}$ filters out action-collapsed episodes where displacement falls below $\tau_d$, revealing that Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and CAR$_\text{f}$ equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not. Of the 732 episodes that Pi0+A1 classifies as collision-free, 99.6\% exhibit maximum displacement below 0.1\,mm (see Section~\ref{sec:fake_safety} for measurement protocol), and 73.9\% remain below 1\,$\mu$m. The Task Success Rate (TSR) is 0\% across all 800 episodes: the model produces no task-directed behavior. The robot generates sub-actuator-resolution motion, records no collisions by default, and receives credit for obstacle avoidance it never performed. The same pattern holds across the Pi0 model family. Pi0 Full Fine-Tune reports CAR\,=\,83.0\% with TSR\,=\,0.5\% and 99.4\% fake safe episodes. Pi0 LoRA achieves CAR\,=\,82.0\% with TSR\,=\,0\%. In every configuration, the safety score is an artifact of inaction rather than a measure of learned avoidance.
13	
14	Two contamination mechanisms produce this illusion. The first is \emph{action collapse}: the model generates near-zero actions, the robot remains stationary, and zero motion guarantees zero collisions. Action collapse accounts for over 99\% of safe episodes across all Pi0 configurations we evaluate. The second mechanism is subtler. Collision-free demonstration trajectories used for fine-tuning implicitly encode obstacle-avoiding motion patterns, so models that imitate these trajectories inherit avoidance behavior without any explicit geometric supervision. The standard CAR metric cannot distinguish either mechanism from deliberate, geometry-aware avoidance. Safety scores that conflate inaction, implicit trajectory mimicry, and genuine geometric reasoning lose their diagnostic value. The result is what we term \emph{fake safety}: high CAR scores that reflect measurement artifacts rather than learned collision avoidance capability. This failure mode echoes a broader pattern in machine learning evaluation, where metrics become optimization targets and cease to measure their intended construct~\cite{karwowski2024goodhart}, and where superficial dataset regularities substitute for the intended learning signal~\cite{gururangan2018annotation}.
15	
16	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 70+ experiments and 6000+ evaluation episodes. Three findings emerge.
17	
18	\textbf{Fake safety is pervasive.} We introduce the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), a corrective metric that excludes episodes where EE displacement falls below a threshold $\tau_d$ (Section~\ref{sec:dfcar}). Applying CAR$_\text{f}$ to Pi0+A1 collapses its safety score from 91.5\% to approximately 0\%, because only 3 of 732 safe episodes survive displacement filtering. The threshold choice is not sensitive: the displacement distribution is sharply bimodal, with collapsed episodes clustering below 1\,$\mu$m and active episodes exceeding 200\,mm, a gap of five orders of magnitude. Any $\tau_d \in [2, 200]$\,mm produces identical filtering results. Pi0.5 validates the metric from the opposite direction: it achieves TSR\,=\,74.7\%\,$\pm$\,1.5\% and CAR\,=\,26.8\%\,$\pm$\,1.6\%, with every safe episode above 288\,mm displacement and a 0\% fake safe rate. CAR$_\text{f}$ equals raw CAR for this model, confirming that the filter preserves genuine avoidance while removing only artifacts (Section~\ref{sec:fake_safety}).
19	
20	\textbf{End-effector-only SDF refinement is structurally limited.} We test the theoretical upper bound of this paradigm by replacing the learned SDF network with ground-truth distance fields computed from the simulation geometry. Three oracle variants (adaptive step size, fixed step size, and feature-space gradient) all achieve \emph{lower} CAR than unrefined baselines: 73.1--76.9\% versus 82.0--83.0\% (Section~\ref{sec:ee_only}). Refinement with perfect distance information produces more collisions, not fewer. Per-task analysis reveals the mechanism: on the one task where the end-effector is the primary collision body, oracle refinement helps; on the remaining three tasks, the SDF gradient pushes the EE away from the nearest surface while the resulting joint-space displacement rotates intermediate arm links into obstacle volumes. Any scheme that monitors only the EE position remains blind to arm-body collisions that dominate in manipulation tasks where the robot must reach around obstacles.
21	
22	\textbf{Collision avoidance originates from demonstration data, not geometric supervision.} On Pi0.5, LoRA fine-tuning without any SDF objective achieves CAR\,=\,54.5\%, identical to LoRA+SDF at $\lambda = 0.005$ (CAR\,=\,54.5\%) and statistically indistinguishable from $\lambda = 0.01$ (CAR\,=\,56.3\%, $p > 0.1$). All fine-tuned models exhibit 0\% frozen episodes and mean EE displacement above 0.37\,m, confirming genuine active avoidance (Section~\ref{sec:avoidance_source}). The demonstration data consists exclusively of collision-free trajectories; LoRA fine-tuning on this data raises CAR by ${\sim}$28 percentage points over the Pi0.5 baseline, an improvement attributable entirely to implicit learning of obstacle-avoiding motion patterns. SDF supervision at tested loss weights adds nothing beyond the avoidance information already encoded in the training distribution.
23	
24	Our contributions are:
25	\begin{itemize}
26	    \item \textbf{CAR$_\text{f}$ metric.} We propose displacement-filtered CAR, a corrective metric that separates genuine obstacle avoidance from action collapse. The metric is robust across $\tau_d \in [2, 200]$\,mm due to the bimodal displacement distribution and operates at the episode level, detecting partial collapse that remains invisible to model-level TSR filtering.
27	    \item \textbf{Systematic fake safety diagnosis.} We document pervasive fake safety across the Pi0 and Pi0.5 model families through 70+ experiments and 6000+ evaluation episodes, showing that over 99\% of safe episodes in Pi0 configurations are artifacts of action collapse. We further demonstrate through ground-truth oracle experiments that end-effector-only SDF refinement is a structural dead end: perfect distance information reduces CAR below unrefined baselines.
28	    \item \textbf{Avoidance source attribution.} We establish that collision avoidance in fine-tuned VLAs originates from implicit learning of collision-free demonstration trajectories, not from explicit geometric supervision. SDF auxiliary losses at $\lambda \in \{0.005, 0.01\}$ produce no measurable CAR improvement over LoRA-only fine-tuning, confirming that the geometric signal is redundant with information already present in the training distribution.
29	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "a4aa2f1b-b9e0-4dec-9acd-5f8f6d6e2905",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:intro}\n\nVision-Language-Action (VLA) models that operate in physical environments must avoid collisions with objects and people. Collision incidents cause task failure, risk damage to the robot and its surroundings, and represent a primary barrier to deploying VLAs outside controlled laboratory settings~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, an extension of the LIBERO simulation platform~\\cite{liu2023libero}, provides the first systematic protocol for measuring collision behavior in VLA manipulation tasks, reporting the Collision Avoidance Rate (CAR) as the fraction of episodes free from robot-obstacle contact. Recent methods have adopted this evaluation framework to demonstrate safety improvements: SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstration learning~\\cite{cofreeevla2026} all report high CAR under standard evaluation. Our own SDF-augmented Pi0~\\cite{black2024pi0} configuration reaches 91.5\\% CAR across 800 evaluation episodes (four independent runs). The collision avoidance problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{3.5cm}\\centering\\textit{Placeholder: Figure 1. The fake safety problem.\\\\Left: Pi0+A1 achieves CAR\\,=\\,91.5\\% but TSR\\,=\\,0\\% (robot frozen, displacement $<$\\,0.1\\,mm).\\\\Center: Displacement-filtered CAR$_\\text{f}$ drops Pi0+A1 to ${\\approx}$\\,0\\%.\\\\Right: Pi0.5 achieves CAR\\,=\\,28.5\\% with TSR\\,=\\,71.5\\% (all safe episodes above 288\\,mm displacement).}\\vspace{3.5cm}}}\n\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR$_\\text{f}$ filters out action-collapsed episodes where displacement falls below $\\tau_d$, revealing that Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and CAR$_\\text{f}$ equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not. Of the 732 episodes that Pi0+A1 classifies as collision-free, 99.6\\% exhibit maximum displacement below 0.1\\,mm (see Section~\\ref{sec:fake_safety} for measurement protocol), and 73.9\\% remain below 1\\,$\\mu$m. The Task Success Rate (TSR) is 0\\% across all 800 episodes: the model produces no task-directed behavior. The robot generates sub-actuator-resolution motion, records no collisions by default, and receives credit for obstacle avoidance it never performed. The same pattern holds across the Pi0 model family. Pi0 Full Fine-Tune reports CAR\\,=\\,83.0\\% with TSR\\,=\\,0.5\\% and 99.4\\% fake safe episodes. Pi0 LoRA achieves CAR\\,=\\,82.0\\% with TSR\\,=\\,0\\%. In every configuration, the safety score is an artifact of inaction rather than a measure of learned avoidance.\n\nTwo contamination mechanisms produce this illusion. The first is \\emph{action collapse}: the model generates near-zero actions, the robot remains stationary, and zero motion guarantees zero collisions. Action collapse accounts for over 99\\% of safe episodes across all Pi0 configurations we evaluate. The second mechanism is subtler. Collision-free demonstration trajectories used for fine-tuning implicitly encode obstacle-avoiding motion patterns, so models that imitate these trajectories inherit avoidance behavior without any explicit geometric supervision. The standard CAR metric cannot distinguish either mechanism from deliberate, geometry-aware avoidance. Safety scores that conflate inaction, implicit trajectory mimicry, and genuine geometric reasoning lose their diagnostic value. The result is what we term \\emph{fake safety}: high CAR scores that reflect measurement artifacts rather than learned collision avoidance capability. This failure mode echoes a broader pattern in machine learning evaluation, where metrics become optimization targets and cease to measure their intended construct~\\cite{karwowski2024goodhart}, and where superficial dataset regularities substitute for the intended learning signal~\\cite{gururangan2018annotation}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 70+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Fake safety is pervasive.} We introduce the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that excludes episodes where EE displacement falls below a threshold $\\tau_d$ (Section~\\ref{sec:dfcar}). Applying CAR$_\\text{f}$ to Pi0+A1 collapses its safety score from 91.5\\% to approximately 0\\%, because only 3 of 732 safe episodes survive displacement filtering. The threshold choice is not sensitive: the displacement distribution is sharply bimodal, with collapsed episodes clustering below 1\\,$\\mu$m and active episodes exceeding 200\\,mm, a gap of five orders of magnitude. Any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. Pi0.5 validates the metric from the opposite direction: it achieves TSR\\,=\\,74.7\\%\\,$\\pm$\\,1.5\\% and CAR\\,=\\,26.8\\%\\,$\\pm$\\,1.6\\%, with every safe episode above 288\\,mm displacement and a 0\\% fake safe rate. CAR$_\\text{f}$ equals raw CAR for this model, confirming that the filter preserves genuine avoidance while removing only artifacts (Section~\\ref{sec:fake_safety}).\n\n\\textbf{End-effector-only SDF refinement is structurally limited.} We test the theoretical upper bound of this paradigm by replacing the learned SDF network with ground-truth distance fields computed from the simulation geometry. Three oracle variants (adaptive step size, fixed step size, and feature-space gradient) all achieve \\emph{lower} CAR than unrefined baselines: 73.1--76.9\\% versus 82.0--83.0\\% (Section~\\ref{sec:ee_only}). Refinement with perfect distance information produces more collisions, not fewer. Per-task analysis reveals the mechanism: on the one task where the end-effector is the primary collision body, oracle refinement helps; on the remaining three tasks, the SDF gradient pushes the EE away from the nearest surface while the resulting joint-space displacement rotates intermediate arm links into obstacle volumes. Any scheme that monitors only the EE position remains blind to arm-body collisions that dominate in manipulation tasks where the robot must reach around obstacles.\n\n\\textbf{Collision avoidance originates from demonstration data, not geometric supervision.} On Pi0.5, LoRA fine-tuning without any SDF objective achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ (CAR\\,=\\,54.5\\%) and statistically indistinguishable from $\\lambda = 0.01$ (CAR\\,=\\,56.3\\%, $p > 0.1$). All fine-tuned models exhibit 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming genuine active avoidance (Section~\\ref{sec:avoidance_source}). The demonstration data consists exclusively of collision-free trajectories; LoRA fine-tuning on this data raises CAR by ${\\sim}$28 percentage points over the Pi0.5 baseline, an improvement attributable entirely to implicit learning of obstacle-avoiding motion patterns. SDF supervision at tested loss weights adds nothing beyond the avoidance information already encoded in the training distribution.\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{CAR$_\\text{f}$ metric.} We propose displacement-filtered CAR, a corrective metric that separates genuine obstacle avoidance from action collapse. The metric is robust across $\\tau_d \\in [2, 200]$\\,mm due to the bimodal displacement distribution and operates at the episode level, detecting partial collapse that remains invisible to model-level TSR filtering.\n    \\item \\textbf{Systematic fake safety diagnosis.} We document pervasive fake safety across the Pi0 and Pi0.5 model families through 70+ experiments and 6000+ evaluation episodes, showing that over 99\\% of safe episodes in Pi0 configurations are artifacts of action collapse. We further demonstrate through ground-truth oracle experiments that end-effector-only SDF refinement is a structural dead end: perfect distance information reduces CAR below unrefined baselines.\n    \\item \\textbf{Avoidance source attribution.} We establish that collision avoidance in fine-tuned VLAs originates from implicit learning of collision-free demonstration trajectories, not from explicit geometric supervision. SDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ produce no measurable CAR improvement over LoRA-only fine-tuning, confirming that the geometric signal is redundant with information already present in the training distribution.\n\\end{itemize}",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01HX9wyyf2bgnBrNRYz9QxXs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "41b3c70e-cae8-412c-9a35-a7bbb46af275",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XnwAL9VPYqNUcEwFG12k7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13520,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13520
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

_source line 10 · 2026-05-26T17:33:47.595Z_

<details><summary>↩ Tool result · `toolu_01HX9wyyf2bgnBrNRYz9QxXs`</summary>

```text
1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR evaluation assumes that a collision-free episode reflects deliberate obstacle avoidance. This assumption fails when a model has collapsed into inaction: a robot that never moves will never collide, yet it has not avoided anything. We show that this failure mode dominates the safety scores of Pi0-family models and introduce CAR$_\text{f}$ as a corrective diagnostic.
4	
5	\subsection{Action Collapse Contamination}\label{sec:collapse}
6	
7	Our Pi0+A1 configuration (SDF auxiliary loss on Pi0; see Section~\ref{sec:sdf_aux} for the training anomaly) achieves a CAR of 91.5\% across 800 evaluation episodes, a figure that would suggest reliable obstacle avoidance. Displacement analysis\footnote{These statistics are computed from obstacle displacement recorded by the original evaluation protocol.} tells a different story. Of the 732 episodes classified as safe, 541 (73.9\%) exhibit maximum displacement below 1\,$\mu$m, another 188 (25.7\%) remain below 0.1\,mm, and only 3 (0.4\%) exceed the 0.1\,mm threshold. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved. TSR is 0\% across all 800 episodes: the model produces no task-directed behavior whatsoever.
8	
9	Applying CAR$_\text{f}$ (Eq.~\ref{eq:car_f}) filters out these action-collapsed episodes. Pi0+A1 drops from CAR\,=\,91.5\% to CAR$_\text{f} \approx 0$\%, because only 3 of 732 safe episodes survive displacement filtering. This is the primary demonstration of what CAR$_\text{f}$ is designed to detect: a headline safety score that is entirely attributable to inaction.
10	
11	The contamination is not specific to the SDF auxiliary loss. Pi0 Full-FT reports CAR\,=\,83.0\% with TSR\,=\,0.5\%, and 99.4\% of its safe episodes are fake safe, yielding CAR$_\text{f} \approx 0$\%. Pi0 LoRA (without any collision objective) achieves CAR\,=\,82.0\%, TSR\,=\,0\%, with a comparable fake safe rate. Across all three Pi0 configurations, CAR$_\text{f}$ collapses to near zero.
12	
13	Pi0.5 provides the validation case. Re-evaluation with displacement recording (200 episodes, seed~7) yields CAR\,=\,28.5\% and TSR\,=\,71.5\%. All 57 safe episodes exhibit maximum EE displacement above 288\,mm. The fake safe rate is 0\%, and CAR$_\text{f}$ equals raw CAR (28.5\%). Pi0.5 does not avoid obstacles by standing still; it executes tasks through the workspace and avoids collisions along the way. The displacement filter removes nothing, confirming that CAR$_\text{f}$ correctly preserves genuine safety.
14	
15	\paragraph{Threshold robustness.} The choice of $\tau_d = 0.1$\,mm is not sensitive. The displacement distribution is sharply bimodal: collapsed episodes cluster below 1\,$\mu$m while active episodes exceed 200\,mm, a gap spanning five orders of magnitude. Any threshold $\tau_d \in [2, 200]$\,mm yields identical filtering results, because no episodes occupy the intermediate range. This bimodality makes CAR$_\text{f}$ robust to threshold selection rather than dependent on an arbitrary cutoff. We provide a full sensitivity analysis in Appendix~\ref{sec:appendix_threshold}. A reviewer might ask why not simply exclude models with $\text{TSR}=0\%$. $\text{CAR}_\text{f}$ operates at the episode level, not the model level; it detects partial collapse where a fraction of episodes are frozen while others succeed, a failure mode invisible to model-level TSR filtering.
16	
17	Table~\ref{tab:fake_safety} summarizes the fake safety decomposition across all evaluated methods. Figure~\ref{fig:displacement} shows the end-effector displacement distribution.
18	
19	\begin{table}[t]
20	\centering
21	\caption{Fake safety decomposition on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. ``Fake Safe'' is computed over safe (non-collision) episodes only. ``Real Safe'' counts safe episodes that exceed the displacement threshold.}
22	\label{tab:fake_safety}
23	\vspace{2pt}
24	\small
25	\begin{tabular}{lccccccl}
26	\toprule
27	Method & Ep. & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) & Disp.\textsuperscript{\textdagger} (m) \\
28	\midrule
29	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & 1/166 & $\approx$\,0 & 0.027 \\
30	Pi0 LoRA     & 200 & 82.0 & 0.0 & ${\sim}$99 & ${\sim}$1/164 & $\approx$\,0 & 0.010 \\
31	Pi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & 3/732 & ---$^*$ & 0.003 \\
32	\midrule
33	Pi0.5 (3-seed)\textsuperscript{\textdaggerdbl}  & 600 & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & --- & --- & --- & 0.367 \\
34	Pi0.5 (reeval)  & 200 & 28.5 & 71.5 & 0.0 & 57/57 & 28.5 & 0.367 \\
35	\bottomrule
36	\end{tabular}
37	\vspace{2pt}
38	{\footnotesize $^*$\,Denominator $<5$; rate estimate statistically unreliable.}\\
39	\vspace{2pt}
40	{\footnotesize \textsuperscript{\textdagger} Pi0-family displacement values report obstacle displacement (max over episode) from an earlier evaluation protocol. Pi0.5 values report end-effector displacement from the rotation-corrected protocol (\S\ref{sec:dfcar}). In both cases, displacement below 1\,mm indicates action collapse, independently confirmed by TSR{=}0\%.}\\
41	\vspace{2pt}
42	{\footnotesize \textsuperscript{\textdaggerdbl} Evaluated before rotation correction (\S\ref{sec:dfcar}); post-correction single-seed reeval (CAR{=}28.5\%, TSR{=}71.5\%) shows consistent results.}\\
43	\vspace{2pt}
44	{\footnotesize Values prefixed with $\sim$ are estimated from mean displacement; precise per-episode breakdowns are available for configurations with $\geq$800 evaluation episodes.}
45	\end{table}
46	
47	\begin{figure}[t]
48	\centering
49	\fbox{\parbox{0.92\linewidth}{\vspace{3cm}\centering\textit{Placeholder: end-effector displacement distribution.\\Bimodal histogram showing collapsed ($<1\,\mu$m) vs.\ active ($>200$\,mm) episodes.}\vspace{3cm}}}
50	\caption{End-effector displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap between the two modes makes the displacement threshold $\tau_d$ robust to any value in $[2, 200]$\,mm.}
51	\label{fig:displacement}
52	\end{figure}
53	
54	\subsection{Capability-Safety Anti-correlation}\label{sec:anticorrelation}
55	
56	The fake safety pattern corresponds to a spatial structure in the TSR-CAR plane. Figure~\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods (Full-FT, LoRA, Pi0+A1) occupy the upper-left: CAR between 82\% and 91.5\%, TSR at or below 0.5\%. Over 99\% of their safe episodes are fake safe. Pi0.5 sits in the lower-right: TSR of 73--76\% across seeds, CAR of 25--28\%. Intermediate configurations (Pi0.5+A1, LoRA-only fine-tunes) populate the middle of the plane, with TSR around 51--54\% and CAR around 54--57\%.
57	
58	The pattern has a straightforward explanation within these two model families. Models that execute tasks move the robot through the workspace and into proximity with obstacles, raising the probability of collision. Models that fail to act remain near the initial configuration, avoiding collisions by default. Higher task capability correlates with lower CAR not because capable models are less safe, but because the denominator of risk exposure changes: a moving robot encounters obstacles that a stationary one does not.
59	
60	We report this anti-correlation as an empirical observation within Pi0 and Pi0.5, not as a universal law. A causal claim would require evidence across a broader set of architectures, benchmarks, and task distributions. Within the scope of our evaluation, the observation reinforces a practical point: CAR is informative only when conditioned on sufficient task capability. The upper-right quadrant of the TSR-CAR plane (high TSR, high CAR) represents genuinely safe and capable behavior; the upper-left quadrant is accessible through action collapse alone.
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\linewidth]{fig_tsr_car_scatter.pdf}
65	\caption{TSR vs.\ CAR for all evaluated configurations. Pi0-family models cluster in the upper-left (high CAR from inaction), Pi0.5 in the lower-right (high TSR with genuine collision exposure). Intermediate methods (Pi0.5+A1, LoRA-only) occupy the center. Error bars denote $\pm$1 standard deviation across seeds where applicable.}
66	\label{fig:tsr_car_scatter}
67	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "edf9ad44-4a01-48e0-8fcf-7e0b6cca23b5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
      "content": "\\section{The Fake Safety Problem}\\label{sec:fake_safety}\n\nStandard CAR evaluation assumes that a collision-free episode reflects deliberate obstacle avoidance. This assumption fails when a model has collapsed into inaction: a robot that never moves will never collide, yet it has not avoided anything. We show that this failure mode dominates the safety scores of Pi0-family models and introduce CAR$_\\text{f}$ as a corrective diagnostic.\n\n\\subsection{Action Collapse Contamination}\\label{sec:collapse}\n\nOur Pi0+A1 configuration (SDF auxiliary loss on Pi0; see Section~\\ref{sec:sdf_aux} for the training anomaly) achieves a CAR of 91.5\\% across 800 evaluation episodes, a figure that would suggest reliable obstacle avoidance. Displacement analysis\\footnote{These statistics are computed from obstacle displacement recorded by the original evaluation protocol.} tells a different story. Of the 732 episodes classified as safe, 541 (73.9\\%) exhibit maximum displacement below 1\\,$\\mu$m, another 188 (25.7\\%) remain below 0.1\\,mm, and only 3 (0.4\\%) exceed the 0.1\\,mm threshold. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved. TSR is 0\\% across all 800 episodes: the model produces no task-directed behavior whatsoever.\n\nApplying CAR$_\\text{f}$ (Eq.~\\ref{eq:car_f}) filters out these action-collapsed episodes. Pi0+A1 drops from CAR\\,=\\,91.5\\% to CAR$_\\text{f} \\approx 0$\\%, because only 3 of 732 safe episodes survive displacement filtering. This is the primary demonstration of what CAR$_\\text{f}$ is designed to detect: a headline safety score that is entirely attributable to inaction.\n\nThe contamination is not specific to the SDF auxiliary loss. Pi0 Full-FT reports CAR\\,=\\,83.0\\% with TSR\\,=\\,0.5\\%, and 99.4\\% of its safe episodes are fake safe, yielding CAR$_\\text{f} \\approx 0$\\%. Pi0 LoRA (without any collision objective) achieves CAR\\,=\\,82.0\\%, TSR\\,=\\,0\\%, with a comparable fake safe rate. Across all three Pi0 configurations, CAR$_\\text{f}$ collapses to near zero.\n\nPi0.5 provides the validation case. Re-evaluation with displacement recording (200 episodes, seed~7) yields CAR\\,=\\,28.5\\% and TSR\\,=\\,71.5\\%. All 57 safe episodes exhibit maximum EE displacement above 288\\,mm. The fake safe rate is 0\\%, and CAR$_\\text{f}$ equals raw CAR (28.5\\%). Pi0.5 does not avoid obstacles by standing still; it executes tasks through the workspace and avoids collisions along the way. The displacement filter removes nothing, confirming that CAR$_\\text{f}$ correctly preserves genuine safety.\n\n\\paragraph{Threshold robustness.} The choice of $\\tau_d = 0.1$\\,mm is not sensitive. The displacement distribution is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m while active episodes exceed 200\\,mm, a gap spanning five orders of magnitude. Any threshold $\\tau_d \\in [2, 200]$\\,mm yields identical filtering results, because no episodes occupy the intermediate range. This bimodality makes CAR$_\\text{f}$ robust to threshold selection rather than dependent on an arbitrary cutoff. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}. A reviewer might ask why not simply exclude models with $\\text{TSR}=0\\%$. $\\text{CAR}_\\text{f}$ operates at the episode level, not the model level; it detects partial collapse where a fraction of episodes are frozen while others succeed, a failure mode invisible to model-level TSR filtering.\n\nTable~\\ref{tab:fake_safety} summarizes the fake safety decomposition across all evaluated methods. Figure~\\ref{fig:displacement} shows the end-effector displacement distribution.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. ``Fake Safe'' is computed over safe (non-collision) episodes only. ``Real Safe'' counts safe episodes that exceed the displacement threshold.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccccl}\n\\toprule\nMethod & Ep. & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) & Disp.\\textsuperscript{\\textdagger} (m) \\\\\n\\midrule\nPi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & 1/166 & $\\approx$\\,0 & 0.027 \\\\\nPi0 LoRA     & 200 & 82.0 & 0.0 & ${\\sim}$99 & ${\\sim}$1/164 & $\\approx$\\,0 & 0.010 \\\\\nPi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & 3/732 & ---$^*$ & 0.003 \\\\\n\\midrule\nPi0.5 (3-seed)\\textsuperscript{\\textdaggerdbl}  & 600 & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & --- & --- & --- & 0.367 \\\\\nPi0.5 (reeval)  & 200 & 28.5 & 71.5 & 0.0 & 57/57 & 28.5 & 0.367 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^*$\\,Denominator $<5$; rate estimate statistically unreliable.}\\\\\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{\\textdagger} Pi0-family displacement values report obstacle displacement (max over episode) from an earlier evaluation protocol. Pi0.5 values report end-effector displacement from the rotation-corrected protocol (\\S\\ref{sec:dfcar}). In both cases, displacement below 1\\,mm indicates action collapse, independently confirmed by TSR{=}0\\%.}\\\\\n\\vspace{2pt}\n{\\footnotesize \\textsuperscript{\\textdaggerdbl} Evaluated before rotation correction (\\S\\ref{sec:dfcar}); post-correction single-seed reeval (CAR{=}28.5\\%, TSR{=}71.5\\%) shows consistent results.}\\\\\n\\vspace{2pt}\n{\\footnotesize Values prefixed with $\\sim$ are estimated from mean displacement; precise per-episode breakdowns are available for configurations with $\\geq$800 evaluation episodes.}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{3cm}\\centering\\textit{Placeholder: end-effector displacement distribution.\\\\Bimodal histogram showing collapsed ($<1\\,\\mu$m) vs.\\ active ($>200$\\,mm) episodes.}\\vspace{3cm}}}\n\\caption{End-effector displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap between the two modes makes the displacement threshold $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\subsection{Capability-Safety Anti-correlation}\\label{sec:anticorrelation}\n\nThe fake safety pattern corresponds to a spatial structure in the TSR-CAR plane. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods (Full-FT, LoRA, Pi0+A1) occupy the upper-left: CAR between 82\\% and 91.5\\%, TSR at or below 0.5\\%. Over 99\\% of their safe episodes are fake safe. Pi0.5 sits in the lower-right: TSR of 73--76\\% across seeds, CAR of 25--28\\%. Intermediate configurations (Pi0.5+A1, LoRA-only fine-tunes) populate the middle of the plane, with TSR around 51--54\\% and CAR around 54--57\\%.\n\nThe pattern has a straightforward explanation within these two model families. Models that execute tasks move the robot through the workspace and into proximity with obstacles, raising the probability of collision. Models that fail to act remain near the initial configuration, avoiding collisions by default. Higher task capability correlates with lower CAR not because capable models are less safe, but because the denominator of risk exposure changes: a moving robot encounters obstacles that a stationary one does not.\n\nWe report this anti-correlation as an empirical observation within Pi0 and Pi0.5, not as a universal law. A causal claim would require evidence across a broader set of architectures, benchmarks, and task distributions. Within the scope of our evaluation, the observation reinforces a practical point: CAR is informative only when conditioned on sufficient task capability. The upper-right quadrant of the TSR-CAR plane (high TSR, high CAR) represents genuinely safe and capable behavior; the upper-left quadrant is accessible through action collapse alone.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_tsr_car_scatter.pdf}\n\\caption{TSR vs.\\ CAR for all evaluated configurations. Pi0-family models cluster in the upper-left (high CAR from inaction), Pi0.5 in the lower-right (high TSR with genuine collision exposure). Intermediate methods (Pi0.5+A1, LoRA-only) occupy the center. Error bars denote $\\pm$1 standard deviation across seeds where applicable.}\n\\label{fig:tsr_car_scatter}\n\\end{figure}",
      "numLines": 67,
      "startLine": 1,
      "totalLines": 67
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01SbqY9xjyH2HszzwBoBTsXW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "d5ecac58-fea3-4eb6-bf28-a14278474513",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XnwAL9VPYqNUcEwFG12k7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13520,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13520
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

_source line 12 · 2026-05-26T17:33:48.068Z_

<details><summary>↩ Tool result · `toolu_01SbqY9xjyH2HszzwBoBTsXW`</summary>

```text
1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Section~\ref{sec:fake_safety} establishes that fake safety dominates Pi0's CAR scores. A natural question remains: could a perfect SDF signal enable effective refinement? We test this with oracle experiments (Section~\ref{sec:oracle_setup}) that replace the learned SDF with ground-truth distance fields from simulation geometry. If EE-only refinement is structurally sound, these oracles should exceed unrefined baselines by a wide margin.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. Oracle variants evaluated over 160 episodes (4 tasks $\times$ 40); baselines and A3 over 200 episodes (4 tasks $\times$ 50). All three oracle variants achieve lower CAR than unrefined baselines, and fake safe rates remain above 96\%. Fake safe rate computed using obstacle displacement threshold; see Table~\ref{tab:fake_safety} footnote for measurement protocol details.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Table~\ref{tab:oracle} reports the results. All three oracle variants achieve \emph{lower} CAR than both unrefined baselines. The best oracle (Oracle-feature, 76.9\%) falls 5.1 points below LoRA (82.0\%) and 6.1 points below Full-FT (83.0\%). Oracle-adaptive and Oracle-fixed perform worse still at 75.0\% and 73.1\%. Refinement with perfect distance information produces more collisions than doing nothing. Fake safe rates confirm that oracle refinement does not reduce action collapse: Oracle-adaptive and Oracle-fixed both register 98.3\% (118/120 and 115/117 safe episodes), Oracle-feature registers 96.7\% (119/123). Ground-truth gradients redirect near-zero motion into near-zero motion in a different direction; they cannot generate viable trajectories from a collapsed policy.
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\linewidth]{fig_oracle_bar.pdf}
32	\caption{Aggregate CAR for oracle SDF refinement variants versus unrefined baselines. All three GT oracle variants achieve lower CAR than both baselines, despite access to perfect distance information.}
33	\label{fig:oracle_bar}
34	\end{figure}
35	
36	The per-task breakdown reveals why refinement backfires on active episodes. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. This is the expected case: EE-directed refinement helps when the EE itself is the collision site. On the remaining tasks, all oracle variants degrade performance. Oracle-adaptive reduces Task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and Task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Refinement trades one collision for another with no mechanism to detect the substitution.
37	
38	The feature-space oracle makes this coupling explicit. It applies the SDF gradient in the policy's latent space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants). Yet gradient magnitudes are two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space), and CAR (76.9\%) shows no advantage over action-space oracles despite 17$\times$ more steps. The latent space lacks geometric grounding: small perturbations in feature space do not translate into collision-free joint configurations.
39	
40	The A3 configuration with a learned SDF head illustrates a complementary failure mode. Across all 160 evaluation episodes, the SDF network never outputs a distance below the refinement threshold, so zero refinement steps occur. The learned decoder has calibrated its outputs to avoid triggering the safety mechanism, and the refinement module sits inert. The resulting CAR of 74.5\% is consistent with the oracle range, confirming that the model operates as an unrefined baseline.
41	
42	These results establish that EE-only SDF refinement is a structural limitation, not an engineering gap. Perfect distance information cannot compensate for the absence of full-body collision awareness. Any scheme that monitors only the EE position remains blind to arm-body collisions, which dominate in manipulation tasks where the robot must reach around obstacles. Effective collision avoidance for VLA models requires geometric representations that span the entire manipulator, not only its tip. Section~\ref{sec:avoidance_source} investigates what does produce collision avoidance in fine-tuned models and how geometric supervision contributes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "474ef22c-cbbc-46e1-b114-8039f6cebab9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex",
      "content": "\\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nSection~\\ref{sec:fake_safety} establishes that fake safety dominates Pi0's CAR scores. A natural question remains: could a perfect SDF signal enable effective refinement? We test this with oracle experiments (Section~\\ref{sec:oracle_setup}) that replace the learned SDF with ground-truth distance fields from simulation geometry. If EE-only refinement is structurally sound, these oracles should exceed unrefined baselines by a wide margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields. Oracle variants evaluated over 160 episodes (4 tasks $\\times$ 40); baselines and A3 over 200 episodes (4 tasks $\\times$ 50). All three oracle variants achieve lower CAR than unrefined baselines, and fake safe rates remain above 96\\%. Fake safe rate computed using obstacle displacement threshold; see Table~\\ref{tab:fake_safety} footnote for measurement protocol details.}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & TSR (\\%) & CAR (\\%) & Fake Safe (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 0.0 & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 0.5 & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 0.0 & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 0.0 & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 0.0 & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 0.0 & 74.5 & -- & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:oracle} reports the results. All three oracle variants achieve \\emph{lower} CAR than both unrefined baselines. The best oracle (Oracle-feature, 76.9\\%) falls 5.1 points below LoRA (82.0\\%) and 6.1 points below Full-FT (83.0\\%). Oracle-adaptive and Oracle-fixed perform worse still at 75.0\\% and 73.1\\%. Refinement with perfect distance information produces more collisions than doing nothing. Fake safe rates confirm that oracle refinement does not reduce action collapse: Oracle-adaptive and Oracle-fixed both register 98.3\\% (118/120 and 115/117 safe episodes), Oracle-feature registers 96.7\\% (119/123). Ground-truth gradients redirect near-zero motion into near-zero motion in a different direction; they cannot generate viable trajectories from a collapsed policy.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_oracle_bar.pdf}\n\\caption{Aggregate CAR for oracle SDF refinement variants versus unrefined baselines. All three GT oracle variants achieve lower CAR than both baselines, despite access to perfect distance information.}\n\\label{fig:oracle_bar}\n\\end{figure}\n\nThe per-task breakdown reveals why refinement backfires on active episodes. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. This is the expected case: EE-directed refinement helps when the EE itself is the collision site. On the remaining tasks, all oracle variants degrade performance. Oracle-adaptive reduces Task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and Task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Refinement trades one collision for another with no mechanism to detect the substitution.\n\nThe feature-space oracle makes this coupling explicit. It applies the SDF gradient in the policy's latent space rather than in Cartesian coordinates, and fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants). Yet gradient magnitudes are two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space), and CAR (76.9\\%) shows no advantage over action-space oracles despite 17$\\times$ more steps. The latent space lacks geometric grounding: small perturbations in feature space do not translate into collision-free joint configurations.\n\nThe A3 configuration with a learned SDF head illustrates a complementary failure mode. Across all 160 evaluation episodes, the SDF network never outputs a distance below the refinement threshold, so zero refinement steps occur. The learned decoder has calibrated its outputs to avoid triggering the safety mechanism, and the refinement module sits inert. The resulting CAR of 74.5\\% is consistent with the oracle range, confirming that the model operates as an unrefined baseline.\n\nThese results establish that EE-only SDF refinement is a structural limitation, not an engineering gap. Perfect distance information cannot compensate for the absence of full-body collision awareness. Any scheme that monitors only the EE position remains blind to arm-body collisions, which dominate in manipulation tasks where the robot must reach around obstacles. Effective collision avoidance for VLA models requires geometric representations that span the entire manipulator, not only its tip. Section~\\ref{sec:avoidance_source} investigates what does produce collision avoidance in fine-tuned models and how geometric supervision contributes.",
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01QMNH5MRW8hYWpPpYMXvweY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "2ad3ce71-90ed-44d8-ba09-5111c442b157",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XnwAL9VPYqNUcEwFG12k7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13520,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13520
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

_source line 14 · 2026-05-26T17:33:48.491Z_

<details><summary>↩ Tool result · `toolu_01QMNH5MRW8hYWpPpYMXvweY`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Sections~\ref{sec:fake_safety} and~\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\lambda = 0.005$, and LoRA+SDF at $\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\ref{sec:dfcar}).
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\lambda \in \{0.005, 0.01\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\% frozen rate and EE displacement above 0.37\,m, confirming genuine active avoidance.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 & 0.0 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 51.5 & 54.5\,$\pm$\,2.8 & 0.392 & 0.0 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.3 & 0.387 & 0.0 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.3\,$\pm$\,1.6 & 0.389 & 0.0 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	Table~\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\% across two seeds. LoRA+SDF at $\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\%, and $\lambda = 0.01$ (three seeds) reaches 56.3\%. All fine-tuned configurations register 0\% frozen episodes and mean EE displacement above 0.37\,m, confirming that the collision avoidance reflected in CAR is genuine active motion. At $\lambda \in \{0.005, 0.01\}$, SDF does not improve CAR beyond the LoRA-only baseline ($p > 0.1$).
25	
26	We construct a null distribution by pooling the two LoRA-only seeds and three $\lambda = 0.005$ seeds into five per-seed CAR measurements (mean 54.5\%, standard deviation 2.15\%), treating them as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.3\% falls within $0.5\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect.
27	
28	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\%. This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance even when the model receives geometric gradients during early training.
29	
30	The avoidance signal originates in the training distribution. The demonstration data consists exclusively of collision-free trajectories; a model that imitates these demonstrations reproduces obstacle-avoiding motion patterns from the training scenes. LoRA fine-tuning alone raises CAR from 26.8\% (Pi0.5 baseline) to ${\sim}$55\%, an improvement of ${\sim}$28 percentage points attributable entirely to collision-free demonstration data. SDF supervision at $\lambda \in \{0.005, 0.01\}$ is redundant with the avoidance information already encoded in these trajectories.
31	
32	\subsection{CAR--TSR Trade-off}\label{sec:tsr_collapse}
33	
34	All fine-tuned models exhibit moderate TSR degradation relative to the Pi0.5 baseline: 74.7\% $\to$ 51.5--54.0\% at 30K steps, a reduction of ${\sim}$21--23 percentage points. The SDF loss is not responsible for this degradation. LoRA-only drops by 23.2 points (to 51.5\%), while SDF variants drop by 20.7--20.9 points (to 53.8--54.0\%). SDF-augmented models show TSR 2.3--2.5 percentage points above LoRA-only, within seed-to-seed noise. Table~\ref{tab:per_task_tsr} decomposes TSR by task. The degradation is non-uniform: Chocolate Pudding retains most of its pre-training capability (${\sim}$68--78\% across conditions), while Orange Juice degrades most (${\sim}$25--33\%). Milk and BBQ Sauce occupy intermediate positions (35--49\% and 59--69\%, respectively). No task collapses to near-zero; the per-task pattern is similar between SDF and LoRA-only conditions, confirming that the SDF loss term does not drive the degradation.
35	
36	\begin{table}[t]
37	\centering
38	\caption{Per-task TSR (\%) at 30K training steps (seed means). All tasks retain meaningful success rates after fine-tuning. The degradation pattern is similar between LoRA-only and SDF-augmented training.}
39	\label{tab:per_task_tsr}
40	\vspace{2pt}
41	\small
42	\begin{tabular}{lcccc}
43	\toprule
44	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
45	 & (3 seeds) & (2 seeds) & (3 seeds) & (3 seeds) \\
46	\midrule
47	Orange Juice      & 70.7 & 33.0 & 33.3 & 24.7 \\
48	Choco.\ Pudding   & 86.0 & 68.0 & 78.0 & 76.7 \\
49	Milk              & 66.0 & 46.0 & 35.3 & 48.7 \\
50	BBQ Sauce         & 76.0 & 59.0 & 69.3 & 65.3 \\
51	\midrule
52	Mean              & 74.7 & 51.5 & 54.0 & 53.8 \\
53	\bottomrule
54	\end{tabular}
55	\end{table}
56	
57	The TSR reduction reflects a distributional shift in the policy, not learned paralysis. All fine-tuned models retain substantial EE motion (mean displacement ${\sim}$0.39\,m, 0\% frozen episodes): the robot continues to move actively through the workspace. The simultaneous CAR improvement and TSR degradation arise from the same source. The demonstration data consists exclusively of collision-free trajectories; LoRA fine-tuning on this data teaches obstacle-avoiding motion patterns, raising CAR by ${\sim}$28 percentage points. The same distributional shift moves the policy away from the pre-trained manipulation prior, reducing task success by ${\sim}$21--23 percentage points. The non-uniform per-task pattern---Chocolate Pudding retains ${\sim}$68--78\% while Orange Juice drops to ${\sim}$25--33\%---suggests that vulnerability to fine-tuning varies by task, potentially reflecting differences in grasp geometry or coverage in the demonstration distribution.
58	
59	\subsection{Dose-Response at Higher Loss Weights}\label{sec:lambda_high}
60	
61	\placeholder{Pending: $\lambda = 0.1$ results (expected 2026-05-27).} The experiments above establish that SDF supervision at $\lambda \in \{0.005, 0.01\}$ is redundant with collision-free demonstrations. Whether higher loss weights produce a dose-dependent CAR improvement remains an open question. Three outcomes are possible:
62	
63	\begin{itemize}
64	\item[(a)] If $\lambda = 0.1$ achieves CAR above 65\%, a dose-dependent relationship exists between SDF loss weight and collision avoidance, indicating that sufficient geometric gradient signal can exceed the avoidance provided by demonstrations alone.
65	\item[(b)] If CAR falls in the 60--65\% range, a weaker dose-response is present but the practical gain over demonstrations alone is modest.
66	\item[(c)] If CAR remains at or below 57\%, SDF supervision is fully redundant across the tested $\lambda$ range, and collision-free demonstrations account for all observed avoidance behavior.
67	\end{itemize}
68	
69	The final narrative for this section will be updated once the $\lambda = 0.1$ evaluation completes.
70	
71	\begin{figure}[t]
72	\centering
73	\fbox{\parbox{0.92\linewidth}{\vspace{2.5cm}\centering\textit{Placeholder: Effect of SDF loss weight $\lambda$ on CAR and TSR.\\$\lambda \in \{0, 0.005, 0.01, 0.1\}$; $\lambda = 0$ corresponds to LoRA-only.}\vspace{2.5cm}}}
74	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\lambda = 0$ point corresponds to LoRA-only (no SDF). \placeholder{Pending: $\lambda = 0.1$ results.}}
75	\label{fig:lambda_car}
76	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "ed241d26-d86a-46bc-8986-aa7edb388968",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nSections~\\ref{sec:fake_safety} and~\\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of SDF geometric supervision from LoRA fine-tuning on collision-free demonstrations by comparing three conditions on Pi0.5: LoRA-only (no SDF), LoRA+SDF at $\\lambda = 0.005$, and LoRA+SDF at $\\lambda = 0.01$. All models are evaluated at the 30K-step checkpoint with rotation-corrected evaluation (Section~\\ref{sec:dfcar}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed, 30K-step checkpoints). At $\\lambda \\in \\{0.005, 0.01\\}$, SDF adds no measurable CAR beyond LoRA-only ($p > 0.1$). All fine-tuned models exhibit 0\\% frozen rate and EE displacement above 0.37\\,m, confirming genuine active avoidance.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) & Frozen (\\%) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & 0.367 & 0.0 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 51.5 & 54.5\\,$\\pm$\\,2.8 & 0.392 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.3 & 0.387 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.3\\,$\\pm$\\,1.6 & 0.389 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 54.5\\% across two seeds. LoRA+SDF at $\\lambda = 0.005$ (three seeds) produces identical CAR of 54.5\\%, and $\\lambda = 0.01$ (three seeds) reaches 56.3\\%. All fine-tuned configurations register 0\\% frozen episodes and mean EE displacement above 0.37\\,m, confirming that the collision avoidance reflected in CAR is genuine active motion. At $\\lambda \\in \\{0.005, 0.01\\}$, SDF does not improve CAR beyond the LoRA-only baseline ($p > 0.1$).\n\nWe construct a null distribution by pooling the two LoRA-only seeds and three $\\lambda = 0.005$ seeds into five per-seed CAR measurements (mean 54.5\\%, standard deviation 2.15\\%), treating them as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.3\\% falls within $0.5\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\%. This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance even when the model receives geometric gradients during early training.\n\nThe avoidance signal originates in the training distribution. The demonstration data consists exclusively of collision-free trajectories; a model that imitates these demonstrations reproduces obstacle-avoiding motion patterns from the training scenes. LoRA fine-tuning alone raises CAR from 26.8\\% (Pi0.5 baseline) to ${\\sim}$55\\%, an improvement of ${\\sim}$28 percentage points attributable entirely to collision-free demonstration data. SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with the avoidance information already encoded in these trajectories.\n\n\\subsection{CAR--TSR Trade-off}\\label{sec:tsr_collapse}\n\nAll fine-tuned models exhibit moderate TSR degradation relative to the Pi0.5 baseline: 74.7\\% $\\to$ 51.5--54.0\\% at 30K steps, a reduction of ${\\sim}$21--23 percentage points. The SDF loss is not responsible for this degradation. LoRA-only drops by 23.2 points (to 51.5\\%), while SDF variants drop by 20.7--20.9 points (to 53.8--54.0\\%). SDF-augmented models show TSR 2.3--2.5 percentage points above LoRA-only, within seed-to-seed noise. Table~\\ref{tab:per_task_tsr} decomposes TSR by task. The degradation is non-uniform: Chocolate Pudding retains most of its pre-training capability (${\\sim}$68--78\\% across conditions), while Orange Juice degrades most (${\\sim}$25--33\\%). Milk and BBQ Sauce occupy intermediate positions (35--49\\% and 59--69\\%, respectively). No task collapses to near-zero; the per-task pattern is similar between SDF and LoRA-only conditions, confirming that the SDF loss term does not drive the degradation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps (seed means). All tasks retain meaningful success rates after fine-tuning. The degradation pattern is similar between LoRA-only and SDF-augmented training.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (3 seeds) & (2 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 70.7 & 33.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 86.0 & 68.0 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 46.0 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 76.0 & 59.0 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 74.7 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe TSR reduction reflects a distributional shift in the policy, not learned paralysis. All fine-tuned models retain substantial EE motion (mean displacement ${\\sim}$0.39\\,m, 0\\% frozen episodes): the robot continues to move actively through the workspace. The simultaneous CAR improvement and TSR degradation arise from the same source. The demonstration data consists exclusively of collision-free trajectories; LoRA fine-tuning on this data teaches obstacle-avoiding motion patterns, raising CAR by ${\\sim}$28 percentage points. The same distributional shift moves the policy away from the pre-trained manipulation prior, reducing task success by ${\\sim}$21--23 percentage points. The non-uniform per-task pattern---Chocolate Pudding retains ${\\sim}$68--78\\% while Orange Juice drops to ${\\sim}$25--33\\%---suggests that vulnerability to fine-tuning varies by task, potentially reflecting differences in grasp geometry or coverage in the demonstration distribution.\n\n\\subsection{Dose-Response at Higher Loss Weights}\\label{sec:lambda_high}\n\n\\placeholder{Pending: $\\lambda = 0.1$ results (expected 2026-05-27).} The experiments above establish that SDF supervision at $\\lambda \\in \\{0.005, 0.01\\}$ is redundant with collision-free demonstrations. Whether higher loss weights produce a dose-dependent CAR improvement remains an open question. Three outcomes are possible:\n\n\\begin{itemize}\n\\item[(a)] If $\\lambda = 0.1$ achieves CAR above 65\\%, a dose-dependent relationship exists between SDF loss weight and collision avoidance, indicating that sufficient geometric gradient signal can exceed the avoidance provided by demonstrations alone.\n\\item[(b)] If CAR falls in the 60--65\\% range, a weaker dose-response is present but the practical gain over demonstrations alone is modest.\n\\item[(c)] If CAR remains at or below 57\\%, SDF supervision is fully redundant across the tested $\\lambda$ range, and collision-free demonstrations account for all observed avoidance behavior.\n\\end{itemize}\n\nThe final narrative for this section will be updated once the $\\lambda = 0.1$ evaluation completes.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.92\\linewidth}{\\vspace{2.5cm}\\centering\\textit{Placeholder: Effect of SDF loss weight $\\lambda$ on CAR and TSR.\\\\$\\lambda \\in \\{0, 0.005, 0.01, 0.1\\}$; $\\lambda = 0$ corresponds to LoRA-only.}\\vspace{2.5cm}}}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\\lambda = 0$ point corresponds to LoRA-only (no SDF). \\placeholder{Pending: $\\lambda = 0.1$ results.}}\n\\label{fig:lambda_car}\n\\end{figure}",
      "numLines": 76,
      "startLine": 1,
      "totalLines": 76
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
Now I have all the context I need. Let me write the discussion.tex file based on the task requirements and the data from the other sections.

Key numbers to use (verified from the sections):
- Pi0+A1: CAR=91.5%, fake_safe=99.6%, dfCAR≈0%
- Pi0.5: TSR=74.7±1.5%, CAR=26.8±1.6%
- Oracle: 73.1-76.9% vs baselines 82.0-83.0%
- LoRA-only CAR=54.5% = SDF λ=0.005 CAR=54.5%


- TSR drops from 74.7% to 51.5-54.0% (roughly 21-23 percentage points), and I've run over 70 experiments across 6000+ episodes to validate these findings
- The delay parameter τ_d shows robustness across a massive range from 2 to 200mm, spanning five orders of magnitude
- The spatial suite results show stark differences: Pi0 with full fine-tuning achieves 0% CAR with 0.29m displacement, while Pi0.5 reaches 13% CAR
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "7cae40aa-050c-4f70-b308-b79de0d577cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197jAaL3mVeNFKQSew4WjzB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15513,
      "cache_read_input_tokens": 24967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15513
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

Now writing the discussion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "f46980d9-c68f-42c4-a43f-8fb779b9f09d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197jAaL3mVeNFKQSew4WjzB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15513,
      "cache_read_input_tokens": 24967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15513
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

<details open><summary>🔧 Tool call — Write · `toolu_01SK3r6KuWCB6mM2F3hPmPP3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.\n\n\\paragraph{The role of geometric supervision.}\nSDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}\n\n\\paragraph{Limitations.}\nOur evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}\n\n\\paragraph{Future work.}\nThree directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.\n\n\\paragraph{Broader impact.}\nDeploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "526cca4e-5cf6-479f-84b4-37c3a88d30a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197jAaL3mVeNFKQSew4WjzB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15513,
      "cache_read_input_tokens": 24967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15513
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

_source line 18 · 2026-05-26T17:34:30.900Z_

<details><summary>↩ Tool result · reported error · `toolu_01SK3r6KuWCB6mM2F3hPmPP3`</summary>

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
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "33c042f2-1830-47b0-bdfd-910e84d6146e",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_013xYsSudo9BT5ztTXr96tA6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "aaa6b6f2-1e3a-40a8-8342-a6e70ca11362",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcFpoiRxDoNK7Vr7mRDEwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1718,
      "cache_read_input_tokens": 40480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1718
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

_source line 20 · 2026-05-26T17:34:33.999Z_

<details><summary>↩ Tool result · `toolu_013xYsSudo9BT5ztTXr96tA6`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\ref{sec:avoidance_source}).
4	
5	\paragraph{Limitations.}
6	The empirical scope of this study is bounded in several respects. All experiments use the \texttt{object\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \texttt{spatial\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\% CAR despite substantial end-effector displacement (0.29\,m): the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \texttt{object\_pudding} benchmark. The EE-only SDF oracle (Section~\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\tau_d = 0.1$\,mm is empirically robust across four orders of magnitude (Appendix~\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\% baseline to $<$7\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.
7	
8	\paragraph{Future work.}
9	Five directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.
10	
11	\paragraph{Broader impact.}
12	Metric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "f6390693-030d-463e-a497-6966ed7c94fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m): the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.\n\n\\paragraph{Future work.}\nFive directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Write · `toolu_01C7SXhfH4p1GWCwHR9NgPNh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.\n\n\\paragraph{The role of geometric supervision.}\nSDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}\n\n\\paragraph{Limitations.}\nOur evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}\n\n\\paragraph{Future work.}\nThree directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.\n\n\\paragraph{Broader impact.}\nDeploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "a8d57693-0505-4527-b4a4-4b9b8bb14455",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LK8ct6t9UPSYcfgqCogYJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 42198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1243
      },
      "output_tokens": 66,
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

_source line 22 · 2026-05-26T17:34:51.888Z_

<details><summary>↩ Tool result · `toolu_01C7SXhfH4p1GWCwHR9NgPNh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "09bf18f0-002e-4bfe-a7c7-9a943f4ccd5f",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).\n\n\\paragraph{Implications for VLA safety evaluation.}\nCAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.\n\n\\paragraph{The role of geometric supervision.}\nSDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}\n\n\\paragraph{Limitations.}\nOur evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}\n\n\\paragraph{Future work.}\nThree directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.\n\n\\paragraph{Broader impact.}\nDeploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 12,
        "newStart": 1,
        "newLines": 18,
        "lines": [
          " \\section{Discussion and Conclusion}\\label{sec:conclusion}",
          " ",
          "-This work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).",
          "+Across 70+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge on a single theme: standard collision avoidance evaluation in VLAs measures the wrong thing. First, action collapse contaminates CAR, inflating Pi0+A1 from 91.5\\% to an effective ${\\approx}$\\,0\\% once displacement filtering removes frozen episodes (99.6\\% fake safe rate). Second, end-effector-only SDF refinement is structurally limited: ground-truth oracle variants achieve 73.1--76.9\\% CAR, below unrefined baselines at 82--83\\%, because EE-directed gradients redistribute collisions to arm links rather than eliminating them. Third, the collision avoidance observed in fine-tuned Pi0.5 originates from collision-free demonstration data, not geometric supervision: LoRA-only training achieves CAR\\,=\\,54.5\\%, identical to LoRA+SDF at $\\lambda = 0.005$ and statistically indistinguishable from $\\lambda = 0.01$ (56.3\\%, $p > 0.1$).",
          " ",
          "+\\paragraph{Implications for VLA safety evaluation.}",
          "+CAR$_\\text{f}$ corrects action-collapse contamination using only end-effector position logging, a signal already available in most evaluation pipelines. The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active episodes above 200\\,mm), so the threshold $\\tau_d$ is robust across five orders of magnitude. We recommend that future work report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination for a given model. Because CAR$_\\text{f}$ operates at the episode level, it detects partial collapse where a fraction of episodes are frozen while others succeed. This failure mode is invisible to model-level TSR filtering. The contamination mechanism is model-agnostic: any action-collapsed VLA will produce artificially inflated CAR.",
          "+",
          "+\\paragraph{The role of geometric supervision.}",
          "+SDF auxiliary losses at $\\lambda \\in \\{0.005, 0.01\\}$ add no measurable CAR beyond LoRA-only fine-tuning on collision-free demonstrations (${\\sim}$28 percentage point improvement over the Pi0.5 baseline). The demonstration distribution already encodes obstacle-avoiding motion patterns that subsume the geometric signal at these loss weights. EE-only SDF refinement faces a separate, structural problem: even with ground-truth distance fields, redirecting the end-effector away from the nearest surface can rotate intermediate arm links into obstacle volumes, increasing rather than decreasing collisions. \\placeholder{Pending: $\\lambda = 0.1$ results will determine whether higher-dose SDF produces genuine additional avoidance or remains redundant with the demonstration signal.}",
          "+",
          " \\paragraph{Limitations.}",
          "-The empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m): the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.",
          "+Our evaluation covers a single benchmark suite (SafeLIBERO object\\_pudding Level~I, four tasks) and two model families (Pi0, Pi0.5). Preliminary results on the spatial\\_bowl suite show different failure patterns: Pi0 Full-FT achieves 0\\% CAR despite 0.29\\,m mean EE displacement, suggesting arm-body collisions dominate when the robot must reach through narrow corridors. Pi0.5 achieves only 13\\% CAR on spatial\\_bowl, compared to 26.8\\% on object\\_pudding. Whether these patterns generalize to OpenVLA, RT-2, or other architectures remains untested. The oracle experiments monitor only the end-effector; full-body SDF along the kinematic chain may yield qualitatively different results. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across $[2, 200]$\\,mm for the current benchmark, but the bimodal gap may narrow on tasks with slower manipulation motions, making $\\tau_d$ selection more consequential. Fine-tuning introduces moderate TSR degradation of ${\\sim}$21--23 percentage points (74.7\\% $\\to$ 51.5--54.0\\%); whether training strategies exist that preserve task capability while maintaining collision avoidance has not been explored. \\placeholder{Pending: if $\\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect (SDF gradient redirecting collisions from one obstacle to another in narrow corridors) warrants dedicated analysis.}",
          " ",
          " \\paragraph{Future work.}",
          "-Five directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.",
          "+Three directions follow from these findings: (1) full-body SDF monitoring along the kinematic chain, replacing end-effector-only geometry with representations that cover intermediate arm links; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families to test whether fake safety and demonstration-driven avoidance generalize; (3) multi-benchmark evaluation beyond SafeLIBERO to characterize how task geometry affects the displacement distribution and CAR$_\\text{f}$ threshold robustness.",
          " ",
          " \\paragraph{Broader impact.}",
          "-Metric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.",
          "+Deploying VLAs in safety-critical settings requires metrics that reflect genuine collision avoidance capability. Contaminated CAR scores allow models with no real avoidance behavior to pass safety benchmarks, creating a false sense of readiness for physical deployment. CAR$_\\text{f}$ provides a low-cost correction that exposes this gap and can be adopted with minimal changes to existing evaluation protocols."
        ]
      }
    ],
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nThis work identifies a systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with inaction caused by action collapse. Across all Pi0-family configurations evaluated on SafeLIBERO, over 98\\% of episodes classified as safe exhibit sub-threshold displacement; raw CAR is therefore unreliable as a safety metric. Displacement-filtered CAR (CAR$_\\text{f}$) separates these two behaviors by excluding episodes below a displacement threshold $\\tau_d$ and credits only active avoidance. Two structural findings reinforce this diagnosis: TSR and CAR are anti-correlated under current methods (Section~\\ref{sec:fake_safety}), and end-effector-only SDF refinement fails to prevent full-body collisions even with ground-truth geometry (Section~\\ref{sec:ee_only}). Fine-tuning on collision-free demonstrations produces non-zero CAR$_\\text{f}$ with zero frozen rate but suffers catastrophic TSR collapse, placing it in a region of the TSR-CAR plane that no other evaluated method occupies (Section~\\ref{sec:avoidance_source}).\n\n\\paragraph{Limitations.}\nThe empirical scope of this study is bounded in several respects. All experiments use the \\texttt{object\\_pudding} Level~II suite from SafeLIBERO (4 tasks). The fake safety mechanism is model-agnostic in principle: any action-collapsed VLA will receive inflated CAR. Direct verification, however, covers only the Pi0 and Pi0.5 model families; whether the same contamination pattern appears in OpenVLA, RT-2, or other VLA architectures requires additional experiments. Preliminary evaluation on the \\texttt{spatial\\_bowl} suite reveals a complementary failure mode: the Pi0 Full-FT baseline achieves 0\\% CAR despite substantial end-effector displacement (0.29\\,m): the robot moves but collides through arm-body contact rather than end-effector contact. Pi0.5 achieves only 13\\% CAR on this suite. These results suggest that spatial tasks with narrow corridors pose additional challenges, dominated by full-body collisions, beyond those captured by the \\texttt{object\\_pudding} benchmark. The EE-only SDF oracle (Section~\\ref{sec:ee_only}) tests end-effector-level refinement exclusively; full-body SDF monitoring along the kinematic chain may yield different outcomes. The displacement threshold $\\tau_d = 0.1$\\,mm is empirically robust across four orders of magnitude (Appendix~\\ref{sec:appendix_threshold}), but remains task-dependent in principle. All fine-tuned models at 30K steps exhibit catastrophic TSR collapse (from 74.7\\% baseline to $<$7\\%), and whether alternative training schedules or regularization can retain task capability while preserving collision avoidance remains untested. In narrow-corridor scenarios (Task~3), SDF gradients redistribute collisions between obstacles rather than eliminate them: the point-wise gradient pushes the end-effector away from the nearest surface, but in bilateral obstacle geometries this shifts the trajectory into the opposing obstacle (Section~\\ref{sec:ee_only}). This collision transfer effect defines a boundary condition for training-time SDF supervision.\n\n\\paragraph{Future work.}\nFive directions follow from this analysis. First, full-body SDF monitoring along the robot kinematic chain would address the structural gap identified in Section~\\ref{sec:ee_only}. Second, evaluation across additional SafeLIBERO suites and other manipulation benchmarks would test whether the contamination patterns generalize beyond the task family studied here. Third, cross-architecture evaluation on non-Pi0-family VLAs (OpenVLA, RT-2) would determine the prevalence of fake safety in the broader VLA landscape. Fourth, we recommend that future VLA safety evaluations report both raw CAR and CAR$_\\text{f}$; the gap between the two quantifies the degree of action-collapse contamination in a given model. Fifth, the catastrophic TSR collapse observed during fine-tuning (Section~\\ref{sec:avoidance_source}) motivates investigation into training strategies that preserve task capability while retaining collision avoidance learned from demonstrations.\n\n\\paragraph{Broader impact.}\nMetric reliability is a prerequisite for safe deployment of autonomous manipulation systems. Contaminated evaluation metrics create a risk that models with no genuine collision avoidance capability pass safety benchmarks and proceed to deployment. Displacement filtering is a low-cost correction: it requires only end-effector position logging, no additional data collection or model modification. The analysis in this work is conducted entirely in simulation; real-world deployment introduces additional safety considerations (sensor noise, sim-to-real transfer, dynamic obstacles) that fall outside the present scope.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 23_

Section written. Key changes from the old version:

- Removed all "catastrophic forgetting/collapse/TSR collapse" language and "TSR <7%" claims
- Replaced with correct numbers: moderate TSR degradation ~21-23pp (74.7% → 51.5-54.0%)
- Opening paragraph summarizes all three findings with verified numbers
- Added "Implications for VLA safety evaluation" paragraph recommending dual CAR/dfCAR reporting
- "Role of geometric supervision" paragraph covers both SDF redundancy and EE-only structural limitation
- Limitations paragraph covers single benchmark, two model families, EE-only oracle, τ_d robustness, and TSR degradation
- Future work condensed to three directions
- Broader impact kept concise (metric reliability for deployment)
- Two `\placeholder{}` markers for pending λ=0.1 results
- ~480 words, within the 500-word target

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "uuid": "96927ebc-42ad-4391-8a3c-bacdd731e90a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012esiKi4zaYn1BRvzFRtevV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 43441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1539
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

Section written. Key changes from the old version:

- Removed all "catastrophic forgetting/collapse/TSR collapse" language and "TSR <7%" claims
- Replaced with correct numbers: moderate TSR degradation ~21-23pp (74.7% → 51.5-54.0%)
- Opening paragraph summarizes all three findings with verified numbers
- Added "Implications for VLA safety evaluation" paragraph recommending dual CAR/dfCAR reporting
- "Role of geometric supervision" paragraph covers both SDF redundancy and EE-only structural limitation
- Limitations paragraph covers single benchmark, two model families, EE-only oracle, τ_d robustness, and TSR degradation
- Future work condensed to three directions
- Broader impact kept concise (metric reliability for deployment)
- Two `\placeholder{}` markers for pending λ=0.1 results
- ~480 words, within the 500-word target

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 75443,
  "duration_api_ms": 76668,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "03bf6b6c-1624-4d06-98a0-f6ac08282bcf",
  "total_cost_usd": 0.38671275000000005,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 33533,
    "cache_read_input_tokens": 162533,
    "output_tokens": 3732,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33533,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 217,
        "cache_read_input_tokens": 43441,
        "cache_creation_input_tokens": 1539,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1539
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2455,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002535,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 3732,
      "cacheReadInputTokens": 162533,
      "cacheCreationInputTokens": 33533,
      "webSearchRequests": 0,
      "costUSD": 0.38417775,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c98ceb8b-9f55-4348-9ffb-b1dfbbb98c92"
}
```

</details>

---
