# paper writing method

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_writing_method_20260521T050028.log`
- **Structured JSON:** [`cac53de9eee85b929803.json`](../../sessions/ca/cac53de9eee85b929803.json)

## Before a recorded user message

46 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
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
  "uuid": "e5151b13-30b5-45d7-81cf-a6d8acd637b2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/memory/"
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
    "resetsAt": 1779357600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2b3b16bb-ae78-49b1-b190-6925ce3bfaaa",
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and checking existing project files for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "1b856d53-deac-468b-abb8-0ff707ff2578",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnJQjXdqtPdaKCs5vjKK6X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15143,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15143
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

<details open><summary>🔧 Tool call — Read · `toolu_016KW92QykYaUQ6yBx77nKYt`</summary>

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
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "07cd112d-60d4-4572-bb78-fefbbf2b7dc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnJQjXdqtPdaKCs5vjKK6X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15143,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15143
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

_source line 6 · 2026-05-21T05:00:39.543Z_

<details><summary>↩ Tool result · `toolu_016KW92QykYaUQ6yBx77nKYt`</summary>

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
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "0f90de08-45c3-42d6-a046-867d858a3b14",
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

<details open><summary>🔧 Tool call — Read · `toolu_01AdL35mwPUKg5LBA4EZxsbV`</summary>

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
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "2cc04e70-7773-40c3-91ac-0c5cf18ec2cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnJQjXdqtPdaKCs5vjKK6X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15143,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15143
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

_source line 8 · 2026-05-21T05:00:40.067Z_

<details><summary>↩ Tool result · `toolu_01AdL35mwPUKg5LBA4EZxsbV`</summary>

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
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "339c906c-e3f4-44cc-a949-728a33a3d44f",
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

<details open><summary>🔧 Tool call — Bash · `toolu_0123Bdgk5sicoVZCAUVNvYno`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/ 2>/dev/null",
  "description": "List existing paper files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "f1f8e95b-3051-4892-b172-61098770a6c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SnJQjXdqtPdaKCs5vjKK6X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15143,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15143
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

_source line 10 · 2026-05-21T05:00:40.989Z_

<details><summary>↩ Tool result · `toolu_0123Bdgk5sicoVZCAUVNvYno`</summary>

```text
acl.sty
acl_latex.tex
acl_natbib.bst
anthology.bib.txt
custom.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "6005eff0-cd42-44ad-b6c6-cf5eb19ada2a",
  "tool_use_result": {
    "stdout": "acl.sty\nacl_latex.tex\nacl_natbib.bst\nanthology.bib.txt\ncustom.bib",
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

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the existing paper files and project context to understand what's already written and the research details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "f560b819-207e-4ad4-9acb-0dd1aa434d40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDPH8UpPLjHszJoAX85PSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11279,
      "cache_read_input_tokens": 26590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11279
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

Let me gather more context from the project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "c0a7bbaf-a9b9-4e24-91c2-1c7c5f1b087e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDPH8UpPLjHszJoAX85PSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11279,
      "cache_read_input_tokens": 26590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11279
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

<details open><summary>🔧 Tool call — Read · `toolu_015xWkKLppboBtK6nNrvnnzD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "9c3af78b-d134-4b9d-899c-05f8aa3d75e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDPH8UpPLjHszJoAX85PSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11279,
      "cache_read_input_tokens": 26590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11279
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

_source line 14 · 2026-05-21T05:00:49.312Z_

<details><summary>↩ Tool result · `toolu_015xWkKLppboBtK6nNrvnnzD`</summary>

```text
1	% Use this file for citations not found in the ACL Anthology (contained in "anthology.bib").
2	
3	@book{Aho:72,
4	    author  = {Alfred V. Aho and Jeffrey D. Ullman},
5	    title   = {The Theory of Parsing, Translation and Compiling},
6	    year    = "1972",
7	    volume  = "1",
8	    publisher = {Prentice-Hall},
9	    address = {Englewood Cliffs, NJ}
10	}
11	
12	@book{APA:83,
13	    author  = {{American Psychological Association}},
14	    title   = {Publications Manual},
15	    year    = "1983",
16	    publisher = {American Psychological Association},
17	    address = {Washington, DC}
18	}
19	
20	@article{Chandra:81,
21		author = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},
22		year = "1981",
23		title = {Alternation},
24		journal = {Journal of the Association for Computing Machinery},
25		volume = "28",
26		number = "1",
27		pages = "114--133",
28		doi = "10.1145/322234.322243",
29	}
30	
31	@inproceedings{andrew2007scalable,
32	  title={Scalable training of {L1}-regularized log-linear models},
33	  author={Andrew, Galen and Gao, Jianfeng},
34	  booktitle={Proceedings of the 24th International Conference on Machine Learning},
35	  pages={33--40},
36	  year={2007},
37	}
38	
39	@book{Gusfield:97,
40	    author  = {Dan Gusfield},
41	    title   = {Algorithms on Strings, Trees and Sequences},
42	    year    = "1997",
43	    publisher = {Cambridge University Press},
44	    address = {Cambridge, UK}
45	}
46	
47	@article{rasooli-tetrault-2015,
48	    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},
49	    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},
50	    journal   = {Computing Research Repository},
51	    volume    = {arXiv:1503.06733},
52	    year      = {2015},
53	    url       = {http://arxiv.org/abs/1503.06733},
54	    note    = {version 2}
55	}
56	
57	@article{Ando2005,
58		Acmid = {1194905},
59		Author = {Ando, Rie Kubota and Zhang, Tong},
60		Issn = {1532-4435},
61		Issue_Date = {12/1/2005},
62		Journal = {Journal of Machine Learning Research},
63		Month = dec,
64		Numpages = {37},
65		Pages = {1817--1853},
66		Publisher = {JMLR.org},
67		Title = {A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data},
68		Volume = {6},
69		Year = {2005}
70	}
71	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "939b5e83-b850-4dc7-9600-dc2712e1a3c8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib",
      "content": "% Use this file for citations not found in the ACL Anthology (contained in \"anthology.bib\").\n\n@book{Aho:72,\n    author  = {Alfred V. Aho and Jeffrey D. Ullman},\n    title   = {The Theory of Parsing, Translation and Compiling},\n    year    = \"1972\",\n    volume  = \"1\",\n    publisher = {Prentice-Hall},\n    address = {Englewood Cliffs, NJ}\n}\n\n@book{APA:83,\n    author  = {{American Psychological Association}},\n    title   = {Publications Manual},\n    year    = \"1983\",\n    publisher = {American Psychological Association},\n    address = {Washington, DC}\n}\n\n@article{Chandra:81,\n\tauthor = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},\n\tyear = \"1981\",\n\ttitle = {Alternation},\n\tjournal = {Journal of the Association for Computing Machinery},\n\tvolume = \"28\",\n\tnumber = \"1\",\n\tpages = \"114--133\",\n\tdoi = \"10.1145/322234.322243\",\n}\n\n@inproceedings{andrew2007scalable,\n  title={Scalable training of {L1}-regularized log-linear models},\n  author={Andrew, Galen and Gao, Jianfeng},\n  booktitle={Proceedings of the 24th International Conference on Machine Learning},\n  pages={33--40},\n  year={2007},\n}\n\n@book{Gusfield:97,\n    author  = {Dan Gusfield},\n    title   = {Algorithms on Strings, Trees and Sequences},\n    year    = \"1997\",\n    publisher = {Cambridge University Press},\n    address = {Cambridge, UK}\n}\n\n@article{rasooli-tetrault-2015,\n    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},\n    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},\n    journal   = {Computing Research Repository},\n    volume    = {arXiv:1503.06733},\n    year      = {2015},\n    url       = {http://arxiv.org/abs/1503.06733},\n    note    = {version 2}\n}\n\n@article{Ando2005,\n\tAcmid = {1194905},\n\tAuthor = {Ando, Rie Kubota and Zhang, Tong},\n\tIssn = {1532-4435},\n\tIssue_Date = {12/1/2005},\n\tJournal = {Journal of Machine Learning Research},\n\tMonth = dec,\n\tNumpages = {37},\n\tPages = {1817--1853},\n\tPublisher = {JMLR.org},\n\tTitle = {A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data},\n\tVolume = {6},\n\tYear = {2005}\n}\n",
      "numLines": 71,
      "startLine": 1,
      "totalLines": 71
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01RFTPRF6DAAkhmKtbFCFcHg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/acl_latex.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "f37a9697-a76d-4f06-949a-7156887a1475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDPH8UpPLjHszJoAX85PSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11279,
      "cache_read_input_tokens": 26590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11279
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

_source line 16 · 2026-05-21T05:00:49.647Z_

<details><summary>↩ Tool result · `toolu_01RFTPRF6DAAkhmKtbFCFcHg`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	% Change "review" to "final" to generate the final (sometimes called camera-ready) version.
4	% Change to "preprint" to generate a non-anonymous version with page numbers.
5	\usepackage[review]{acl}
6	
7	% Standard package includes
8	\usepackage{times}
9	\usepackage{latexsym}
10	
11	% For proper rendering and hyphenation of words containing Latin characters (including in bib files)
12	\usepackage[T1]{fontenc}
13	% For Vietnamese characters
14	% \usepackage[T5]{fontenc}
15	% See https://www.latex-project.org/help/documentation/encguide.pdf for other character sets
16	
17	% This assumes your files are encoded as UTF8
18	\usepackage[utf8]{inputenc}
19	
20	% This is not strictly necessary, and may be commented out,
21	% but it will improve the layout of the manuscript,
22	% and will typically save some space.
23	\usepackage{microtype}
24	
25	% This is also not strictly necessary, and may be commented out.
26	% However, it will improve the aesthetics of text in
27	% the typewriter font.
28	\usepackage{inconsolata}
29	
30	%Including images in your LaTeX document requires adding
31	%additional package(s)
32	\usepackage{graphicx}
33	
34	% If the title and author information does not fit in the area allocated, uncomment the following
35	%
36	%\setlength\titlebox{&lt;dim>}
37	%
38	% and set &lt;dim> to something 5cm or larger.
39	
40	\title{Instructions for *ACL Proceedings}
41	
42	% Author information can be set in various styles:
43	% For several authors from the same institution:
44	% \author{Author 1 \and ... \and Author n \\
45	%         Address line \\ ... \\ Address line}
46	% if the names do not fit well on one line use
47	%         Author 1 \\ {\bf Author 2} \\ ... \\ {\bf Author n} \\
48	% For authors from different institutions:
49	% \author{Author 1 \\ Address line \\  ... \\ Address line
50	%         \And  ... \And
51	%         Author n \\ Address line \\ ... \\ Address line}
52	% To start a separate ``row'' of authors use \AND, as in
53	% \author{Author 1 \\ Address line \\  ... \\ Address line
54	%         \AND
55	%         Author 2 \\ Address line \\ ... \\ Address line \And
56	%         Author 3 \\ Address line \\ ... \\ Address line}
57	
58	\author{First Author \\
59	  Affiliation / Address line 1 \\
60	  Affiliation / Address line 2 \\
61	  Affiliation / Address line 3 \\
62	  \texttt{email@domain} \\\And
63	  Second Author \\
64	  Affiliation / Address line 1 \\
65	  Affiliation / Address line 2 \\
66	  Affiliation / Address line 3 \\
67	  \texttt{email@domain} \\}
68	
69	%\author{
70	%  \textbf{First Author\textsuperscript{1}},
71	%  \textbf{Second Author\textsuperscript{1,2}},
72	%  \textbf{Third T. Author\textsuperscript{1}},
73	%  \textbf{Fourth Author\textsuperscript{1}},
74	%\\
75	%  \textbf{Fifth Author\textsuperscript{1,2}},
76	%  \textbf{Sixth Author\textsuperscript{1}},
77	%  \textbf{Seventh Author\textsuperscript{1}},
78	%  \textbf{Eighth Author \textsuperscript{1,2,3,4}},
79	%\\
80	%  \textbf{Ninth Author\textsuperscript{1}},
81	%  \textbf{Tenth Author\textsuperscript{1}},
82	%  \textbf{Eleventh E. Author\textsuperscript{1,2,3,4,5}},
83	%  \textbf{Twelfth Author\textsuperscript{1}},
84	%\\
85	%  \textbf{Thirteenth Author\textsuperscript{3}},
86	%  \textbf{Fourteenth F. Author\textsuperscript{2,4}},
87	%  \textbf{Fifteenth Author\textsuperscript{1}},
88	%  \textbf{Sixteenth Author\textsuperscript{1}},
89	%\\
90	%  \textbf{Seventeenth S. Author\textsuperscript{4,5}},
91	%  \textbf{Eighteenth Author\textsuperscript{3,4}},
92	%  \textbf{Nineteenth N. Author\textsuperscript{2,5}},
93	%  \textbf{Twentieth Author\textsuperscript{1}}
94	%\\
95	%\\
96	%  \textsuperscript{1}Affiliation 1,
97	%  \textsuperscript{2}Affiliation 2,
98	%  \textsuperscript{3}Affiliation 3,
99	%  \textsuperscript{4}Affiliation 4,
100	%  \textsuperscript{5}Affiliation 5
101	%\\
102	%  \small{
103	%    \textbf{Correspondence:} \href{mailto:email@domain}{email@domain}
104	%  }
105	%}
106	
107	\begin{document}
108	\maketitle
109	\begin{abstract}
110	This document is a supplement to the general instructions for *ACL authors. It contains instructions for using the \LaTeX{} style files for ACL conferences.
111	The document itself conforms to its own specifications, and is therefore an example of what your manuscript should look like.
112	These instructions should be used both for papers submitted for review and for final versions of accepted papers.
113	\end{abstract}
114	
115	\section{Introduction}
116	
117	These instructions are for authors submitting papers to *ACL conferences using \LaTeX. They are not self-contained. All authors must follow the general instructions for *ACL proceedings,\footnote{\url{http://acl-org.github.io/ACLPUB/formatting.html}} and this document contains additional instructions for the \LaTeX{} style files.
118	
119	The templates include the \LaTeX{} source of this document (\texttt{acl\_latex.tex}),
120	the \LaTeX{} style file used to format it (\texttt{acl.sty}),
121	an ACL bibliography style (\texttt{acl\_natbib.bst}),
122	an example bibliography (\texttt{custom.bib}),
123	and the bibliography for the ACL Anthology (\texttt{anthology.bib}).
124	
125	\section{Engines}
126	
127	To produce a PDF file, pdf\LaTeX{} is strongly recommended (over original \LaTeX{} plus dvips+ps2pdf or dvipdf).
128	The style file \texttt{acl.sty} can also be used with
129	lua\LaTeX{} and
130	Xe\LaTeX{}, which are especially suitable for text in non-Latin scripts.
131	The file \texttt{acl\_lualatex.tex} in this repository provides
132	an example of how to use \texttt{acl.sty} with either
133	lua\LaTeX{} or
134	Xe\LaTeX{}.
135	
136	\section{Preamble}
137	
138	The first line of the file must be
139	\begin{quote}
140	\begin{verbatim}
141	\documentclass[11pt]{article}
142	\end{verbatim}
143	\end{quote}
144	
145	To load the style file in the review version:
146	\begin{quote}
147	\begin{verbatim}
148	\usepackage[review]{acl}
149	\end{verbatim}
150	\end{quote}
151	For the final version, omit the \verb|review| option:
152	\begin{quote}
153	\begin{verbatim}
154	\usepackage{acl}
155	\end{verbatim}
156	\end{quote}
157	
158	To use Times Roman, put the following in the preamble:
159	\begin{quote}
160	\begin{verbatim}
161	\usepackage{times}
162	\end{verbatim}
163	\end{quote}
164	(Alternatives like txfonts or newtx are also acceptable.)
165	
166	Please see the \LaTeX{} source of this document for comments on other packages that may be useful.
167	
168	Set the title and author using \verb|\title| and \verb|\author|. Within the author list, format multiple authors using \verb|\and| and \verb|\And| and \verb|\AND|; please see the \LaTeX{} source for examples.
169	
170	By default, the box containing the title and author names is set to the minimum of 5 cm. If you need more space, include the following in the preamble:
171	\begin{quote}
172	\begin{verbatim}
173	\setlength\titlebox{&lt;dim>}
174	\end{verbatim}
175	\end{quote}
176	where \verb|&lt;dim>| is replaced with a length. Do not set this length smaller than 5 cm.
177	
178	\section{Document Body}
179	
180	\subsection{Footnotes}
181	
182	Footnotes are inserted with the \verb|\footnote| command.\footnote{This is a footnote.}
183	
184	\subsection{Tables and figures}
185	
186	See Table~\ref{tab:accents} for an example of a table and its caption.
187	\textbf{Do not override the default caption sizes.}
188	
189	\begin{table}
190	  \centering
191	  \begin{tabular}{lc}
192	    \hline
193	    \textbf{Command} & \textbf{Output} \\
194	    \hline
195	    \verb|{\"a}|     & {\"a}           \\
196	    \verb|{\^e}|     & {\^e}           \\
197	    \verb|{\`i}|     & {\`i}           \\
198	    \verb|{\.I}|     & {\.I}           \\
199	    \verb|{\o}|      & {\o}            \\
200	    \verb|{\'u}|     & {\'u}           \\
201	    \verb|{\aa}|     & {\aa}           \\\hline
202	  \end{tabular}
203	  \begin{tabular}{lc}
204	    \hline
205	    \textbf{Command} & \textbf{Output} \\
206	    \hline
207	    \verb|{\c c}|    & {\c c}          \\
208	    \verb|{\u g}|    & {\u g}          \\
209	    \verb|{\l}|      & {\l}            \\
210	    \verb|{\~n}|     & {\~n}           \\
211	    \verb|{\H o}|    & {\H o}          \\
212	    \verb|{\v r}|    & {\v r}          \\
213	    \verb|{\ss}|     & {\ss}           \\
214	    \hline
215	  \end{tabular}
216	  \caption{Example commands for accented characters, to be used in, \emph{e.g.}, Bib\TeX{} entries.}
217	  \label{tab:accents}
218	\end{table}
219	
220	As much as possible, fonts in figures should conform
221	to the document fonts. See Figure~\ref{fig:experiments} for an example of a figure and its caption.
222	
223	Using the \verb|graphicx| package graphics files can be included within figure
224	environment at an appropriate point within the text.
225	The \verb|graphicx| package supports various optional arguments to control the
226	appearance of the figure.
227	You must include it explicitly in the \LaTeX{} preamble (after the
228	\verb|\documentclass| declaration and before \verb|\begin{document}|) using
229	\verb|\usepackage{graphicx}|.
230	
231	\begin{figure}[t]
232	  \includegraphics[width=\columnwidth]{example-image-golden}
233	  \caption{A figure with a caption that runs for more than one line.
234	    Example image is usually available through the \texttt{mwe} package
235	    without even mentioning it in the preamble.}
236	  \label{fig:experiments}
237	\end{figure}
238	
239	\begin{figure*}[t]
240	  \includegraphics[width=0.48\linewidth]{example-image-a} \hfill
241	  \includegraphics[width=0.48\linewidth]{example-image-b}
242	  \caption {A minimal working example to demonstrate how to place
243	    two images side-by-side.}
244	\end{figure*}
245	
246	\subsection{Hyperlinks}
247	
248	Users of older versions of \LaTeX{} may encounter the following error during compilation:
249	\begin{quote}
250	\verb|\pdfendlink| ended up in different nesting level than \verb|\pdfstartlink|.
251	\end{quote}
252	This happens when pdf\LaTeX{} is used and a citation splits across a page boundary. The best way to fix this is to upgrade \LaTeX{} to 2018-12-01 or later.
253	
254	\subsection{Citations}
255	
256	\begin{table*}
257	  \centering
258	  \begin{tabular}{lll}
259	    \hline
260	    \textbf{Output}           & \textbf{natbib command} & \textbf{ACL only command} \\
261	    \hline
262	    \citep{Gusfield:97}       & \verb|\citep|           &                           \\
263	    \citealp{Gusfield:97}     & \verb|\citealp|         &                           \\
264	    \citet{Gusfield:97}       & \verb|\citet|           &                           \\
265	    \citeyearpar{Gusfield:97} & \verb|\citeyearpar|     &                           \\
266	    \citeposs{Gusfield:97}    &                         & \verb|\citeposs|          \\
267	    \hline
268	  \end{tabular}
269	  \caption{\label{citation-guide}
270	    Citation commands supported by the style file.
271	    The style is based on the natbib package and supports all natbib citation commands.
272	    It also supports commands defined in previous ACL style files for compatibility.
273	  }
274	\end{table*}
275	
276	Table~\ref{citation-guide} shows the syntax supported by the style files.
277	We encourage you to use the natbib styles.
278	You can use the command \verb|\citet| (cite in text) to get ``author (year)'' citations, like this citation to a paper by \citet{Gusfield:97}.
279	You can use the command \verb|\citep| (cite in parentheses) to get ``(author, year)'' citations \citep{Gusfield:97}.
280	You can use the command \verb|\citealp| (alternative cite without parentheses) to get ``author, year'' citations, which is useful for using citations within parentheses (e.g. \citealp{Gusfield:97}).
281	
282	A possessive citation can be made with the command \verb|\citeposs|.
283	This is not a standard natbib command, so it is generally not compatible
284	with other style files.
285	
286	\subsection{References}
287	
288	\nocite{Ando2005,andrew2007scalable,rasooli-tetrault-2015}
289	
290	The \LaTeX{} and Bib\TeX{} style files provided roughly follow the American Psychological Association format.
291	If your own bib file is named \texttt{custom.bib}, then placing the following before any appendices in your \LaTeX{} file will generate the references section for you:
292	\begin{quote}
293	\begin{verbatim}
294	\bibliography{custom}
295	\end{verbatim}
296	\end{quote}
297	
298	You can obtain the complete ACL Anthology as a Bib\TeX{} file from \url{https://aclweb.org/anthology/anthology.bib.gz}.
299	To include both the Anthology and your own .bib file, use the following instead of the above.
300	\begin{quote}
301	\begin{verbatim}
302	\bibliography{anthology,custom}
303	\end{verbatim}
304	\end{quote}
305	
306	Please see Section~\ref{sec:bibtex} for information on preparing Bib\TeX{} files.
307	
308	\subsection{Equations}
309	
310	An example equation is shown below:
311	\begin{equation}
312	  \label{eq:example}
313	  A = \pi r^2
314	\end{equation}
315	
316	Labels for equation numbers, sections, subsections, figures and tables
317	are all defined with the \verb|\label{label}| command and cross references
318	to them are made with the \verb|\ref{label}| command.
319	
320	This an example cross-reference to Equation~\ref{eq:example}.
321	
322	\subsection{Appendices}
323	
324	Use \verb|\appendix| before any appendix section to switch the section numbering over to letters. See Appendix~\ref{sec:appendix} for an example.
325	
326	\section{Bib\TeX{} Files}
327	\label{sec:bibtex}
328	
329	Unicode cannot be used in Bib\TeX{} entries, and some ways of typing special characters can disrupt Bib\TeX's alphabetization. The recommended way of typing special characters is shown in Table~\ref{tab:accents}.
330	
331	Please ensure that Bib\TeX{} records contain DOIs or URLs when possible, and for all the ACL materials that you reference.
332	Use the \verb|doi| field for DOIs and the \verb|url| field for URLs.
333	If a Bib\TeX{} entry has a URL or DOI field, the paper title in the references section will appear as a hyperlink to the paper, using the hyperref \LaTeX{} package.
334	
335	\section*{Limitations}
336	
337	This document does not cover the content requirements for ACL or any
338	other specific venue.  Check the author instructions for
339	information on
340	maximum page lengths, the required ``Limitations'' section,
341	and so on.
342	
343	\section*{Acknowledgments}
344	
345	This document has been adapted
346	by Steven Bethard, Ryan Cotterell and Rui Yan
347	from the instructions for earlier ACL and NAACL proceedings, including those for
348	ACL 2019 by Douwe Kiela and Ivan Vuli\'{c},
349	NAACL 2019 by Stephanie Lukin and Alla Roskovskaya,
350	ACL 2018 by Shay Cohen, Kevin Gimpel, and Wei Lu,
351	NAACL 2018 by Margaret Mitchell and Stephanie Lukin,
352	Bib\TeX{} suggestions for (NA)ACL 2017/2018 from Jason Eisner,
353	ACL 2017 by Dan Gildea and Min-Yen Kan,
354	NAACL 2017 by Margaret Mitchell,
355	ACL 2012 by Maggie Li and Michael White,
356	ACL 2010 by Jing-Shin Chang and Philipp Koehn,
357	ACL 2008 by Johanna D. Moore, Simone Teufel, James Allan, and Sadaoki Furui,
358	ACL 2005 by Hwee Tou Ng and Kemal Oflazer,
359	ACL 2002 by Eugene Charniak and Dekang Lin,
360	and earlier ACL and EACL formats written by several people, including
361	John Chen, Henry S. Thompson and Donald Walker.
362	Additional elements were taken from the formatting instructions of the \emph{International Joint Conference on Artificial Intelligence} and the \emph{Conference on Computer Vision and Pattern Recognition}.
363	
364	% Bibliography entries for the entire Anthology, followed by custom entries
365	%\bibliography{custom,anthology-overleaf-1,anthology-overleaf-2}
366	
367	% Custom bibliography entries only
368	\bibliography{custom}
369	
370	\appendix
371	
372	\section{Example Appendix}
373	\label{sec:appendix}
374	
375	This is an appendix.
376	
377	\end{document}
378	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "fa308d29-2c85-4c92-a146-a8c6ce95e54e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/acl_latex.tex",
      "content": "\\documentclass[11pt]{article}\n\n% Change \"review\" to \"final\" to generate the final (sometimes called camera-ready) version.\n% Change to \"preprint\" to generate a non-anonymous version with page numbers.\n\\usepackage[review]{acl}\n\n% Standard package includes\n\\usepackage{times}\n\\usepackage{latexsym}\n\n% For proper rendering and hyphenation of words containing Latin characters (including in bib files)\n\\usepackage[T1]{fontenc}\n% For Vietnamese characters\n% \\usepackage[T5]{fontenc}\n% See https://www.latex-project.org/help/documentation/encguide.pdf for other character sets\n\n% This assumes your files are encoded as UTF8\n\\usepackage[utf8]{inputenc}\n\n% This is not strictly necessary, and may be commented out,\n% but it will improve the layout of the manuscript,\n% and will typically save some space.\n\\usepackage{microtype}\n\n% This is also not strictly necessary, and may be commented out.\n% However, it will improve the aesthetics of text in\n% the typewriter font.\n\\usepackage{inconsolata}\n\n%Including images in your LaTeX document requires adding\n%additional package(s)\n\\usepackage{graphicx}\n\n% If the title and author information does not fit in the area allocated, uncomment the following\n%\n%\\setlength\\titlebox{&lt;dim>}\n%\n% and set &lt;dim> to something 5cm or larger.\n\n\\title{Instructions for *ACL Proceedings}\n\n% Author information can be set in various styles:\n% For several authors from the same institution:\n% \\author{Author 1 \\and ... \\and Author n \\\\\n%         Address line \\\\ ... \\\\ Address line}\n% if the names do not fit well on one line use\n%         Author 1 \\\\ {\\bf Author 2} \\\\ ... \\\\ {\\bf Author n} \\\\\n% For authors from different institutions:\n% \\author{Author 1 \\\\ Address line \\\\  ... \\\\ Address line\n%         \\And  ... \\And\n%         Author n \\\\ Address line \\\\ ... \\\\ Address line}\n% To start a separate ``row'' of authors use \\AND, as in\n% \\author{Author 1 \\\\ Address line \\\\  ... \\\\ Address line\n%         \\AND\n%         Author 2 \\\\ Address line \\\\ ... \\\\ Address line \\And\n%         Author 3 \\\\ Address line \\\\ ... \\\\ Address line}\n\n\\author{First Author \\\\\n  Affiliation / Address line 1 \\\\\n  Affiliation / Address line 2 \\\\\n  Affiliation / Address line 3 \\\\\n  \\texttt{email@domain} \\\\\\And\n  Second Author \\\\\n  Affiliation / Address line 1 \\\\\n  Affiliation / Address line 2 \\\\\n  Affiliation / Address line 3 \\\\\n  \\texttt{email@domain} \\\\}\n\n%\\author{\n%  \\textbf{First Author\\textsuperscript{1}},\n%  \\textbf{Second Author\\textsuperscript{1,2}},\n%  \\textbf{Third T. Author\\textsuperscript{1}},\n%  \\textbf{Fourth Author\\textsuperscript{1}},\n%\\\\\n%  \\textbf{Fifth Author\\textsuperscript{1,2}},\n%  \\textbf{Sixth Author\\textsuperscript{1}},\n%  \\textbf{Seventh Author\\textsuperscript{1}},\n%  \\textbf{Eighth Author \\textsuperscript{1,2,3,4}},\n%\\\\\n%  \\textbf{Ninth Author\\textsuperscript{1}},\n%  \\textbf{Tenth Author\\textsuperscript{1}},\n%  \\textbf{Eleventh E. Author\\textsuperscript{1,2,3,4,5}},\n%  \\textbf{Twelfth Author\\textsuperscript{1}},\n%\\\\\n%  \\textbf{Thirteenth Author\\textsuperscript{3}},\n%  \\textbf{Fourteenth F. Author\\textsuperscript{2,4}},\n%  \\textbf{Fifteenth Author\\textsuperscript{1}},\n%  \\textbf{Sixteenth Author\\textsuperscript{1}},\n%\\\\\n%  \\textbf{Seventeenth S. Author\\textsuperscript{4,5}},\n%  \\textbf{Eighteenth Author\\textsuperscript{3,4}},\n%  \\textbf{Nineteenth N. Author\\textsuperscript{2,5}},\n%  \\textbf{Twentieth Author\\textsuperscript{1}}\n%\\\\\n%\\\\\n%  \\textsuperscript{1}Affiliation 1,\n%  \\textsuperscript{2}Affiliation 2,\n%  \\textsuperscript{3}Affiliation 3,\n%  \\textsuperscript{4}Affiliation 4,\n%  \\textsuperscript{5}Affiliation 5\n%\\\\\n%  \\small{\n%    \\textbf{Correspondence:} \\href{mailto:email@domain}{email@domain}\n%  }\n%}\n\n\\begin{document}\n\\maketitle\n\\begin{abstract}\nThis document is a supplement to the general instructions for *ACL authors. It contains instructions for using the \\LaTeX{} style files for ACL conferences.\nThe document itself conforms to its own specifications, and is therefore an example of what your manuscript should look like.\nThese instructions should be used both for papers submitted for review and for final versions of accepted papers.\n\\end{abstract}\n\n\\section{Introduction}\n\nThese instructions are for authors submitting papers to *ACL conferences using \\LaTeX. They are not self-contained. All authors must follow the general instructions for *ACL proceedings,\\footnote{\\url{http://acl-org.github.io/ACLPUB/formatting.html}} and this document contains additional instructions for the \\LaTeX{} style files.\n\nThe templates include the \\LaTeX{} source of this document (\\texttt{acl\\_latex.tex}),\nthe \\LaTeX{} style file used to format it (\\texttt{acl.sty}),\nan ACL bibliography style (\\texttt{acl\\_natbib.bst}),\nan example bibliography (\\texttt{custom.bib}),\nand the bibliography for the ACL Anthology (\\texttt{anthology.bib}).\n\n\\section{Engines}\n\nTo produce a PDF file, pdf\\LaTeX{} is strongly recommended (over original \\LaTeX{} plus dvips+ps2pdf or dvipdf).\nThe style file \\texttt{acl.sty} can also be used with\nlua\\LaTeX{} and\nXe\\LaTeX{}, which are especially suitable for text in non-Latin scripts.\nThe file \\texttt{acl\\_lualatex.tex} in this repository provides\nan example of how to use \\texttt{acl.sty} with either\nlua\\LaTeX{} or\nXe\\LaTeX{}.\n\n\\section{Preamble}\n\nThe first line of the file must be\n\\begin{quote}\n\\begin{verbatim}\n\\documentclass[11pt]{article}\n\\end{verbatim}\n\\end{quote}\n\nTo load the style file in the review version:\n\\begin{quote}\n\\begin{verbatim}\n\\usepackage[review]{acl}\n\\end{verbatim}\n\\end{quote}\nFor the final version, omit the \\verb|review| option:\n\\begin{quote}\n\\begin{verbatim}\n\\usepackage{acl}\n\\end{verbatim}\n\\end{quote}\n\nTo use Times Roman, put the following in the preamble:\n\\begin{quote}\n\\begin{verbatim}\n\\usepackage{times}\n\\end{verbatim}\n\\end{quote}\n(Alternatives like txfonts or newtx are also acceptable.)\n\nPlease see the \\LaTeX{} source of this document for comments on other packages that may be useful.\n\nSet the title and author using \\verb|\\title| and \\verb|\\author|. Within the author list, format multiple authors using \\verb|\\and| and \\verb|\\And| and \\verb|\\AND|; please see the \\LaTeX{} source for examples.\n\nBy default, the box containing the title and author names is set to the minimum of 5 cm. If you need more space, include the following in the preamble:\n\\begin{quote}\n\\begin{verbatim}\n\\setlength\\titlebox{&lt;dim>}\n\\end{verbatim}\n\\end{quote}\nwhere \\verb|&lt;dim>| is replaced with a length. Do not set this length smaller than 5 cm.\n\n\\section{Document Body}\n\n\\subsection{Footnotes}\n\nFootnotes are inserted with the \\verb|\\footnote| command.\\footnote{This is a footnote.}\n\n\\subsection{Tables and figures}\n\nSee Table~\\ref{tab:accents} for an example of a table and its caption.\n\\textbf{Do not override the default caption sizes.}\n\n\\begin{table}\n  \\centering\n  \\begin{tabular}{lc}\n    \\hline\n    \\textbf{Command} & \\textbf{Output} \\\\\n    \\hline\n    \\verb|{\\\"a}|     & {\\\"a}           \\\\\n    \\verb|{\\^e}|     & {\\^e}           \\\\\n    \\verb|{\\`i}|     & {\\`i}           \\\\\n    \\verb|{\\.I}|     & {\\.I}           \\\\\n    \\verb|{\\o}|      & {\\o}            \\\\\n    \\verb|{\\'u}|     & {\\'u}           \\\\\n    \\verb|{\\aa}|     & {\\aa}           \\\\\\hline\n  \\end{tabular}\n  \\begin{tabular}{lc}\n    \\hline\n    \\textbf{Command} & \\textbf{Output} \\\\\n    \\hline\n    \\verb|{\\c c}|    & {\\c c}          \\\\\n    \\verb|{\\u g}|    & {\\u g}          \\\\\n    \\verb|{\\l}|      & {\\l}            \\\\\n    \\verb|{\\~n}|     & {\\~n}           \\\\\n    \\verb|{\\H o}|    & {\\H o}          \\\\\n    \\verb|{\\v r}|    & {\\v r}          \\\\\n    \\verb|{\\ss}|     & {\\ss}           \\\\\n    \\hline\n  \\end{tabular}\n  \\caption{Example commands for accented characters, to be used in, \\emph{e.g.}, Bib\\TeX{} entries.}\n  \\label{tab:accents}\n\\end{table}\n\nAs much as possible, fonts in figures should conform\nto the document fonts. See Figure~\\ref{fig:experiments} for an example of a figure and its caption.\n\nUsing the \\verb|graphicx| package graphics files can be included within figure\nenvironment at an appropriate point within the text.\nThe \\verb|graphicx| package supports various optional arguments to control the\nappearance of the figure.\nYou must include it explicitly in the \\LaTeX{} preamble (after the\n\\verb|\\documentclass| declaration and before \\verb|\\begin{document}|) using\n\\verb|\\usepackage{graphicx}|.\n\n\\begin{figure}[t]\n  \\includegraphics[width=\\columnwidth]{example-image-golden}\n  \\caption{A figure with a caption that runs for more than one line.\n    Example image is usually available through the \\texttt{mwe} package\n    without even mentioning it in the preamble.}\n  \\label{fig:experiments}\n\\end{figure}\n\n\\begin{figure*}[t]\n  \\includegraphics[width=0.48\\linewidth]{example-image-a} \\hfill\n  \\includegraphics[width=0.48\\linewidth]{example-image-b}\n  \\caption {A minimal working example to demonstrate how to place\n    two images side-by-side.}\n\\end{figure*}\n\n\\subsection{Hyperlinks}\n\nUsers of older versions of \\LaTeX{} may encounter the following error during compilation:\n\\begin{quote}\n\\verb|\\pdfendlink| ended up in different nesting level than \\verb|\\pdfstartlink|.\n\\end{quote}\nThis happens when pdf\\LaTeX{} is used and a citation splits across a page boundary. The best way to fix this is to upgrade \\LaTeX{} to 2018-12-01 or later.\n\n\\subsection{Citations}\n\n\\begin{table*}\n  \\centering\n  \\begin{tabular}{lll}\n    \\hline\n    \\textbf{Output}           & \\textbf{natbib command} & \\textbf{ACL only command} \\\\\n    \\hline\n    \\citep{Gusfield:97}       & \\verb|\\citep|           &                           \\\\\n    \\citealp{Gusfield:97}     & \\verb|\\citealp|         &                           \\\\\n    \\citet{Gusfield:97}       & \\verb|\\citet|           &                           \\\\\n    \\citeyearpar{Gusfield:97} & \\verb|\\citeyearpar|     &                           \\\\\n    \\citeposs{Gusfield:97}    &                         & \\verb|\\citeposs|          \\\\\n    \\hline\n  \\end{tabular}\n  \\caption{\\label{citation-guide}\n    Citation commands supported by the style file.\n    The style is based on the natbib package and supports all natbib citation commands.\n    It also supports commands defined in previous ACL style files for compatibility.\n  }\n\\end{table*}\n\nTable~\\ref{citation-guide} shows the syntax supported by the style files.\nWe encourage you to use the natbib styles.\nYou can use the command \\verb|\\citet| (cite in text) to get ``author (year)'' citations, like this citation to a paper by \\citet{Gusfield:97}.\nYou can use the command \\verb|\\citep| (cite in parentheses) to get ``(author, year)'' citations \\citep{Gusfield:97}.\nYou can use the command \\verb|\\citealp| (alternative cite without parentheses) to get ``author, year'' citations, which is useful for using citations within parentheses (e.g. \\citealp{Gusfield:97}).\n\nA possessive citation can be made with the command \\verb|\\citeposs|.\nThis is not a standard natbib command, so it is generally not compatible\nwith other style files.\n\n\\subsection{References}\n\n\\nocite{Ando2005,andrew2007scalable,rasooli-tetrault-2015}\n\nThe \\LaTeX{} and Bib\\TeX{} style files provided roughly follow the American Psychological Association format.\nIf your own bib file is named \\texttt{custom.bib}, then placing the following before any appendices in your \\LaTeX{} file will generate the references section for you:\n\\begin{quote}\n\\begin{verbatim}\n\\bibliography{custom}\n\\end{verbatim}\n\\end{quote}\n\nYou can obtain the complete ACL Anthology as a Bib\\TeX{} file from \\url{https://aclweb.org/anthology/anthology.bib.gz}.\nTo include both the Anthology and your own .bib file, use the following instead of the above.\n\\begin{quote}\n\\begin{verbatim}\n\\bibliography{anthology,custom}\n\\end{verbatim}\n\\end{quote}\n\nPlease see Section~\\ref{sec:bibtex} for information on preparing Bib\\TeX{} files.\n\n\\subsection{Equations}\n\nAn example equation is shown below:\n\\begin{equation}\n  \\label{eq:example}\n  A = \\pi r^2\n\\end{equation}\n\nLabels for equation numbers, sections, subsections, figures and tables\nare all defined with the \\verb|\\label{label}| command and cross references\nto them are made with the \\verb|\\ref{label}| command.\n\nThis an example cross-reference to Equation~\\ref{eq:example}.\n\n\\subsection{Appendices}\n\nUse \\verb|\\appendix| before any appendix section to switch the section numbering over to letters. See Appendix~\\ref{sec:appendix} for an example.\n\n\\section{Bib\\TeX{} Files}\n\\label{sec:bibtex}\n\nUnicode cannot be used in Bib\\TeX{} entries, and some ways of typing special characters can disrupt Bib\\TeX's alphabetization. The recommended way of typing special characters is shown in Table~\\ref{tab:accents}.\n\nPlease ensure that Bib\\TeX{} records contain DOIs or URLs when possible, and for all the ACL materials that you reference.\nUse the \\verb|doi| field for DOIs and the \\verb|url| field for URLs.\nIf a Bib\\TeX{} entry has a URL or DOI field, the paper title in the references section will appear as a hyperlink to the paper, using the hyperref \\LaTeX{} package.\n\n\\section*{Limitations}\n\nThis document does not cover the content requirements for ACL or any\nother specific venue.  Check the author instructions for\ninformation on\nmaximum page lengths, the required ``Limitations'' section,\nand so on.\n\n\\section*{Acknowledgments}\n\nThis document has been adapted\nby Steven Bethard, Ryan Cotterell and Rui Yan\nfrom the instructions for earlier ACL and NAACL proceedings, including those for\nACL 2019 by Douwe Kiela and Ivan Vuli\\'{c},\nNAACL 2019 by Stephanie Lukin and Alla Roskovskaya,\nACL 2018 by Shay Cohen, Kevin Gimpel, and Wei Lu,\nNAACL 2018 by Margaret Mitchell and Stephanie Lukin,\nBib\\TeX{} suggestions for (NA)ACL 2017/2018 from Jason Eisner,\nACL 2017 by Dan Gildea and Min-Yen Kan,\nNAACL 2017 by Margaret Mitchell,\nACL 2012 by Maggie Li and Michael White,\nACL 2010 by Jing-Shin Chang and Philipp Koehn,\nACL 2008 by Johanna D. Moore, Simone Teufel, James Allan, and Sadaoki Furui,\nACL 2005 by Hwee Tou Ng and Kemal Oflazer,\nACL 2002 by Eugene Charniak and Dekang Lin,\nand earlier ACL and EACL formats written by several people, including\nJohn Chen, Henry S. Thompson and Donald Walker.\nAdditional elements were taken from the formatting instructions of the \\emph{International Joint Conference on Artificial Intelligence} and the \\emph{Conference on Computer Vision and Pattern Recognition}.\n\n% Bibliography entries for the entire Anthology, followed by custom entries\n%\\bibliography{custom,anthology-overleaf-1,anthology-overleaf-2}\n\n% Custom bibliography entries only\n\\bibliography{custom}\n\n\\appendix\n\n\\section{Example Appendix}\n\\label{sec:appendix}\n\nThis is an appendix.\n\n\\end{document}\n",
      "numLines": 378,
      "startLine": 1,
      "totalLines": 378
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D6dvFCdVPKzpLHpqVhM2tt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "49af8a65-bdc3-47ec-9767-f3c97de7b6a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDPH8UpPLjHszJoAX85PSL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11279,
      "cache_read_input_tokens": 26590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11279
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

_source line 18 · 2026-05-21T05:00:50.455Z_

<details><summary>↩ Tool result · `toolu_01D6dvFCdVPKzpLHpqVhM2tt`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_roadmap"
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
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "201d1eff-e298-41b7-ae12-6fa06701c0b8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Let me read the project's literature map and other relevant files to get the citation keys and research context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "4aa395e4-2674-4302-81b2-53e3d39ce98d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gpn1r9wm5aer6Fn2RioEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 37869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7304
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

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MsLGg47P5k8gZc34LiL9eg`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "literature_map.yaml",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "9581974d-834b-49be-80b4-1df399ab2017",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gpn1r9wm5aer6Fn2RioEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 37869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7304
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

_source line 21 · 2026-05-21T05:00:55.380Z_

<details><summary>↩ Tool result · `toolu_01MsLGg47P5k8gZc34LiL9eg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "8c0768a0-07ef-4384-b7f5-68ebd0261ef6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  miao2026closing:\\\\n    title: \\\\\\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\\\\\"\\\\n    authors: [\\\\\\\"Ruoxi Miao\\\\\\\", \\\\\\\"Lyle Ungar\\\\\\\"]\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.25052\\\\\\\"\\\\n    category: \\\\\\\"mechanistic_calibration\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  xiao2025knowledge:\\\\n    title: \\\\\\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\\\\\"\\\\n    authors: [\\\\\\\"Zheng Xiao\\\\\\\"]\\\\n    year: 2025\\\\n    venue: \\\\\\\"ACL 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2504.13816\\\\\\\"\\\\n    category: \\\\\\\"cross_lingual_probing\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    relevance: \\\\\\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  civelli2026shared:\\\\n    title: \\\\\\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\\\\\"\\\\n    authors: [\\\\\\\"Andrea Civelli\\\\\\\"]\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.12731\\\\\\\"\\\\n    category: \\\\\\\"cross_lingual_probing\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  zhou2025lace:\\\\n    title: \\\\\\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\\\\\"\\\\n    authors: [\\\\\\\"Zhou\\\\\\\"]\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.03136\\\\\\\"\\\\n    category: \\\\\\\"multilingual_calibration\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    relevance: \\\\\\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  ravisankar2026dali:\\\\n    title: \\\\\\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\\\\\"\\\\n    authors: [\\\\\\\"Ravisankar\\\\\\\"]\\\\n    year: 2026\\\\n    venue: \\\\\\\"EACL 2026\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2504.09378\\\\\\\"\\\\n    category: \\\\\\\"cross_lingual_alignment\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  miao2026coral:\\\\n    title: \\\\\\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\\\\\"\\\\n    authors: [\\\\\\\"Ruoxi Miao\\\\\\\"]\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.06022\\\\\\\"\\\\n    category: \\\\\\\"mechanistic_calibration\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    relevance: \\\\\\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  joshi2025calibration:\\\\n    title: \\\\\\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\\\\\"\\\\n    authors: [\\\\\\\"Joshi\\\\\\\"]\\\\n    year: 2025\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"mechanistic_calibration\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  confidence_manifold2026:\\\\n    title: \\\\\\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\\\\\"\\\\n    authors: []\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.08159\\\\\\\"\\\\n    category: \\\\\\\"mechanistic_calibration\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  karandikar2021sbece:\\\\n    title: \\\\\\\"Soft Calibration Objectives for Neural Networks\\\\\\\"\\\\n    authors: [\\\\\\\"Karandikar\\\\\\\"]\\\\n    year: 2021\\\\n    venue: \\\\\\\"NeurIPS 2021\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"calibration_methods\\\\\\\"\\\\n    role: \\\\\\\"method-component\\\\\\\"\\\\n    relevance: \\\\\\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  khanmohammadi2025ccps:\\\\n    title: \\\\\\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\\\\\"\\\\n    authors: [\\\\\\\"Khanmohammadi\\\\\\\"]\\\\n    year: 2025\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2505.21772\\\\\\\"\\\\n    category: \\\\\\\"mechanistic_calibration\\\\\\\"\\\\n    role: \\\\\\\"direct-competitor\\\\\\\"\\\\n    relevance: \\\\\\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  liu2025middle:\\\\n    title: \\\\\\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\\\\\"\\\\n    authors: [\\\\\\\"Liu\\\\\\\", \\\\\\\"Niehues\\\\\\\"]\\\\n    year: 2025\\\\n    venue: \\\\\\\"ACL 2025\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"cross_lingual_alignment\\\\\\\"\\\\n    role: \\\\\\\"foundation\\\\\\\"\\\\n    relevance: \\\\\\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  ji2025calibrating:\\\\n    title: \\\\\\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\\\\\"\\\\n    authors: [\\\\\\\"Ji\\\\\\\"]\\\\n    year: 2025\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"mechanistic_calibration\\\\\\\"\\\\n    role: \\\\\\\"background\\\\\\\"\\\\n    relevance: \\\\\\\"Verbal uncertainty governed by single linear direction in representation space.\\\\\\\"\\\\n    verified: false\\\\n    added_by: \\\\\\\"director\\\\\\\"\\\\n    added_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\ncategories:\\\\n  mechanistic_calibration: \\\\\\\"Probing/steering calibration signals in LLM internal representations\\\\\\\"\\\\n  cross_lingual_probing: \\\\\\\"Cross-lingual transfer of probes/directions in multilingual models\\\\\\\"\\\\n  cross_lingual_alignment: \\\\\\\"Language alignment and shared representations in multilingual LLMs\\\\\\\"\\\\n  multilingual_calibration: \\\\\\\"Calibration methods for multilingual LLMs\\\\\\\"\\\\n  calibration_methods: \\\\\\\"General calibration objectives and techniques\\\\\\\"\\\\n\\\\nmeta:\\\\n  created_at: \\\\\\\"2026-05-20\\\\\\\"\\\\n  last_updated: \\\\\\\"2026-05-20\\\\\\\"\\\\n  total_papers: 12\\\\n\\\", \\\"total_chars\\\": 6989, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/literature_map.yaml\", \"content\": \"papers:\\n  miao2026closing:\\n    title: \\\"Closing the Confidence-Faithfulness Gap in Large Language Models\\\"\\n    authors: [\\\"Ruoxi Miao\\\", \\\"Lyle Ungar\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2603.25052\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Showed correctness direction and verbalized confidence direction are orthogonal (cosine < 0.04) in 7-8B models. Motivates probing internal representations. English-only — our cross-lingual extension is the natural next step.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  xiao2025knowledge:\\n    title: \\\"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\\\"\\n    authors: [\\\"Zheng Xiao\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2504.13816\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest prior work. Cross-lingual transfer of knowledge-boundary probes (answerable vs unanswerable). Key differences: they probe knowledge boundaries (input-level), we probe correctness (output-dependent); they measure probing accuracy, not ECE/Brier; they test 8 languages, we target 20+.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  civelli2026shared:\\n    title: \\\"A Shared Geometry of Difficulty in Multilingual Language Models\\\"\\n    authors: [\\\"Andrea Civelli\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2601.12731\\\"\\n    category: \\\"cross_lingual_probing\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Cross-lingual difficulty probe transfer at intermediate layers. Architecture-dependent optimal depth (24-49%). Probes IRT difficulty (question property), not correctness (model property). Critical control for our difficulty ablation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  zhou2025lace:\\n    title: \\\"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs\\\"\\n    authors: [\\\"Zhou\\\"]\\n    year: 2025\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03136\\\"\\n    category: \\\"multilingual_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"LACE: adaptive layer ensemble for multilingual calibration. Confirmed 5x ECE gap across 100+ languages. Requires per-language validation data. Our CaCLR needs no non-English correctness labels.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ravisankar2026dali:\\n    title: \\\"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs\\\"\\n    authors: [\\\"Ravisankar\\\"]\\n    year: 2026\\n    venue: \\\"EACL 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2504.09378\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"DALI: causal evidence via activation patching that English middle-layer representations fix non-English errors across 24 languages. Strongest causal support for our hypothesis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  miao2026coral:\\n    title: \\\"Correctness-Optimized Residual Activation Lens (CORAL)\\\"\\n    authors: [\\\"Ruoxi Miao\\\"]\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.06022\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Transferable correctness probes via regularized MLP on residual activations, ~50% ECE improvement at 53-66% depth. English-only, cross-task. CaCLR positioned as solution to their identified distribution-shift transfer degradation.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  joshi2025calibration:\\n    title: \\\"Calibration Across Layers: Understanding Calibration Evolution in LLMs\\\"\\n    authors: [\\\"Joshi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Identified low-dimensional calibration direction in residual stream evolving across layers.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  confidence_manifold2026:\\n    title: \\\"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\\\"\\n    authors: []\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2602.08159\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Correctness signals occupy 3-8 dimensions, linearly separable. 25 labeled examples achieve 89% of full-data accuracy. All English-only.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  karandikar2021sbece:\\n    title: \\\"Soft Calibration Objectives for Neural Networks\\\"\\n    authors: [\\\"Karandikar\\\"]\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"\\\"\\n    category: \\\"calibration_methods\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"SB-ECE: differentiable soft-binned ECE enabling gradient-based calibration optimization. Core component of our CaCLR objective.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  khanmohammadi2025ccps:\\n    title: \\\"Calibrating LLM Confidence by Probing Perturbed Representation Stability (CCPS)\\\"\\n    authors: [\\\"Khanmohammadi\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2505.21772\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Calibration via probing perturbed representation stability at final layer. ~55% ECE reduction. English-only, single layer. No cross-lingual or multi-layer analysis.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  liu2025middle:\\n    title: \\\"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\\\"\\n    authors: [\\\"Liu\\\", \\\"Niehues\\\"]\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"cross_lingual_alignment\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Middle layers form strongest language-agnostic shared space. Supports our hypothesis about intermediate-layer transfer.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\n  ji2025calibrating:\\n    title: \\\"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\\\"\\n    authors: [\\\"Ji\\\"]\\n    year: 2025\\n    venue: \\\"EMNLP 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"mechanistic_calibration\\\"\\n    role: \\\"background\\\"\\n    relevance: \\\"Verbal uncertainty governed by single linear direction in representation space.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20\\\"\\n\\ncategories:\\n  mechanistic_calibration: \\\"Probing/steering calibration signals in LLM internal representations\\\"\\n  cross_lingual_probing: \\\"Cross-lingual transfer of probes/directions in multilingual models\\\"\\n  cross_lingual_alignment: \\\"Language alignment and shared representations in multilingual LLMs\\\"\\n  multilingual_calibration: \\\"Calibration methods for multilingual LLMs\\\"\\n  calibration_methods: \\\"General calibration objectives and techniques\\\"\\n\\nmeta:\\n  created_at: \\\"2026-05-20\\\"\\n  last_updated: \\\"2026-05-20\\\"\\n  total_papers: 12\\n\", \"total_chars\": 6989, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HCuDbPGTgso47MRuzNR8rB`</summary>

```json
{
  "project": "xling_calib_direction",
  "file": "paper_framing.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "248a9749-1205-4d33-8622-868e028e07ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gpn1r9wm5aer6Fn2RioEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 37869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7304
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

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_01SpXYVVv6VcR2LAgmLWPnjg`</summary>

```json
{
  "project": "xling_calib_direction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "65547c41-1b8f-4db4-902e-e3668b406837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gpn1r9wm5aer6Fn2RioEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7304,
      "cache_read_input_tokens": 37869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7304
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

_source line 24 · 2026-05-21T05:00:56.215Z_

<details><summary>↩ Tool result · `toolu_01HCuDbPGTgso47MRuzNR8rB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\\\"method replication to more languages\\\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n### Key Empirical Contributions (elevated from appendix to main body, D012)\\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\"\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \\\"geometric analysis\\\" not \\\"mechanistic explanation.\\\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n13. **\\\"CaCLR is your own method — self-debunking is less impactful\\\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\\n14. **\\\"CKA is correlational, not mechanistic\\\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \\\"On learning invariant representations for domain adaptation\\\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 17679, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "0d5f634e-8102-4d79-a7de-6b6d0ac4f503",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — xling_calib_direction\\\\n\\\\n## Target Venue\\\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\\\n- Core submission: 2 models × 20 languages × all contributions\\\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\\\n\\\\n## Core Insight\\\\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\\\n\\\\n## Core Claims (4, causal chain)\\\\n\\\\n### Claim 1 — Pareto Frontier (Discovery)\\\\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\\\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\\\n\\\\n### Claim 2 — Decomposition (Analysis)\\\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\\\n\\\\n### Claim 3 — CaCLR (Method / Diagnostic)\\\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\\\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\\\\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\\\\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\\\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\\\n\\\\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\\\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\\\\\\\"method replication to more languages\\\\\\\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\\\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\\\n\\\\n### Key Empirical Contributions (elevated from appendix to main body, D012)\\\\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\\\\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\\\\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\\\\n\\\\n## Story Spine\\\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\\\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\\\\n- **Headline template (method success)**: \\\\\\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\\\\\"\\\\n- **Headline template (negative result)**: \\\\\\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\\\\\"\\\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\\\n\\\\n## Field-Level Significance\\\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\\\n\\\\n## Anticipated Reviewer Concerns & Responses\\\\n1. **\\\\\\\"Xiao et al. already did this\\\\\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\\\n2. **\\\\\\\"Temperature scaling baseline\\\\\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\\\n3. **\\\\\\\"Mean-shift too weak / why does it fail?\\\\\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\\\n4. **\\\\\\\"Difficulty confound\\\\\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\\\n5. **\\\\\\\"INT8 artifacts\\\\\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\\\n6. **\\\\\\\"Only MCQA\\\\\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\\\n7. **\\\\\\\"Predictable from domain adaptation theory\\\\\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\\\n8. **\\\\\\\"No statistical tests\\\\\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\\\n9. **\\\\\\\"Probing methodology concerns\\\\\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\\\n10. **\\\\\\\"No mechanistic explanation\\\\\\\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \\\\\\\"geometric analysis\\\\\\\" not \\\\\\\"mechanistic explanation.\\\\\\\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\\\\n11. **\\\\\\\"Why not conformal prediction?\\\\\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\\\n12. **\\\\\\\"CaCLR parallel activations = test leakage?\\\\\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\\\n13. **\\\\\\\"CaCLR is your own method — self-debunking is less impactful\\\\\\\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\\\\n14. **\\\\\\\"CKA is correlational, not mechanistic\\\\\\\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\\\\n\\\\n## Additional Related Work Coverage (Dream-identified gaps)\\\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \\\\\\\"On learning invariant representations for domain adaptation\\\\\\\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\\\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\\\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\\\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\\\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\\\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\\\\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\\\\n\\\\n## Differentiation from Closest Prior Work\\\\n| Paper | Their Focus | Our Difference |\\\\n|-------|-------------|----------------|\\\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\\\n\\\", \\\"total_chars\\\": 17679, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/paper_framing.md\", \"content\": \"# Paper Framing — xling_calib_direction\\n\\n## Target Venue\\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\\n- Core submission: 2 models × 20 languages × all contributions\\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\\n\\n## Core Insight\\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. This geometric insight, combined with the architecture-dependent depth-transferability tradeoff (strong on Qwen, weak on Llama), provides a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\\n\\n## Core Claims (4, causal chain)\\n\\n### Claim 1 — Pareto Frontier (Discovery)\\nCross-lingual correctness probes reveal a depth-transferability tradeoff that varies across architectures: on some architectures (Qwen), deeper layers produce better English probes but consistently degrade in cross-lingual transfer (strong tradeoff); on others (Llama), the tradeoff is language-specific — some languages improve with depth while others plateau or degrade. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\\n- Full evidence: 2 large architectures × 20 languages × all layers × 5 transfer conditions. Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\\n\\n### Claim 2 — Decomposition (Analysis)\\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\\n\\n### Claim 3 — CaCLR (Method / Diagnostic)\\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space — this is a design limitation worth discussing.\\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\\n\\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\\\"method replication to more languages\\\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\\n\\n### Key Empirical Contributions (elevated from appendix to main body, D012)\\n- **Control task methodological warning**: Hewitt & Liang selectivity analysis reveals ~28% of low-resource language-layer probing results are capacity artifacts (selectivity below meaningful threshold). First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\\n\\n## Story Spine\\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) ~28% of low-resource probing results are capacity artifacts (control task warning for the field); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the depth-transferability tradeoff, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\\n- **Headline template (method success)**: \\\"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\\\"\\n- **Headline template (negative result)**: \\\"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\\\"\\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\\n\\n## Field-Level Significance\\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n1. **\\\"Xiao et al. already did this\\\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\\n2. **\\\"Temperature scaling baseline\\\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\\n3. **\\\"Mean-shift too weak / why does it fail?\\\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\\n4. **\\\"Difficulty confound\\\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\\n5. **\\\"INT8 artifacts\\\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\\n6. **\\\"Only MCQA\\\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\\n7. **\\\"Predictable from domain adaptation theory\\\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\\n8. **\\\"No statistical tests\\\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\\n9. **\\\"Probing methodology concerns\\\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\\n10. **\\\"No mechanistic explanation\\\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \\\"geometric analysis\\\" not \\\"mechanistic explanation.\\\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\\n11. **\\\"Why not conformal prediction?\\\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\\n12. **\\\"CaCLR parallel activations = test leakage?\\\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\\n13. **\\\"CaCLR is your own method — self-debunking is less impactful\\\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\\n14. **\\\"CKA is correlational, not mechanistic\\\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\\n\\n## Additional Related Work Coverage (Dream-identified gaps)\\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \\\"On learning invariant representations for domain adaptation\\\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\\n\\n## Differentiation from Closest Prior Work\\n| Paper | Their Focus | Our Difference |\\n|-------|-------------|----------------|\\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\\n\", \"total_chars\": 17679, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T05:00:56.228Z_

<details><summary>↩ Tool result · `toolu_01SpXYVVv6VcR2LAgmLWPnjg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-21 01:18 UTC | 更新原因: Correct model sizes (Llama4 66GB, Qwen3 122GB), revert to parallel download strategy, disk math confirms both fit\\n\\n## 核心方向\\nCross-lingual correctness probe transfer: 探索 LLM 内部 correctness direction 的跨语言可迁移性，测试 probe-based calibration 在非英语语言的可行性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research phase — MVP 通过 (D004), Dream 审稿两轮完成 (D005→D009), P0 条件批准\\n- **MVP**: 3/3 完成 (mvp_001 ✓, mvp_002 ✓, mvp_003 ✓)\\n- **代码准备**: 全部就绪 ✅\\n  - transfer_eval.py: 5 种 transfer methods 已部署 (zero-shot, mean-shift, Procrustes, few-shot, CaCLR)\\n  - extract_activations_large.py: register_forward_hook + post-norm + 70/30 split ✅\\n  - train_caclr.py: M007 梯度修复已验证 ✅\\n- **模型下载** (并行，磁盘充足):\\n  - Llama4 Scout W4A16: ~44GB/66GB，ETA ~30-45min\\n  - Qwen3 GPTQ-Int4: ~38GB/122GB，ETA ~2-3h\\n  - 两模型合计 ~188GB，基础占用 ~88GB，总计 ~276GB/350GB = 79%\\n- **P1 先行**: plan_013 控制任务 ✅ (selectivity 0.262 at L27), plan_012 Procrustes sensitivity 运行中\\n- **关键发现**: Pareto tradeoff Qwen strong/Llama weak; mean-shift rank-invariance proof; few-shot +4.9pp AUROC over zero-shot\\n\\n## 近期任务\\n- [ ] Llama4 下载完成 (~30-45min) → 完整性验证 → dry-run → 正式审批 plan_002\\n- [ ] Qwen3 下载完成 (~2-3h) → 完整性验证 → dry-run → 正式审批 plan_001\\n- [ ] plan_002 执行: 提取激活 (12 layers × 20 langs) → 5 种 transfer eval\\n- [ ] plan_001 执行: 提取激活 (24 layers × 20 langs) → 5 种 transfer eval\\n- [ ] Procrustes sensitivity 结果收集 + CSV 完整性验证 (双进程写入风险)\\n- [ ] CPU-bound P1 (plan_011/012/013) 与 P0 并行推进\\n\\n## GPU 预算\\n- 服务器: westd-13176 (4× RTX 6000 PRO 96GB)\\n- 磁盘: /root/autodl-tmp/ 350GB total，下载完成后 ~276GB used (~74GB 余量)\\n- 激活存储策略: 先提取 Llama4 (~33GB) → 实验 → 可删模型释放 66GB → 再提取 Qwen3\\n- P0 总 GPU 预算: plan_001(80h) + plan_002(40h) + plan_003(20h) + plan_004(15h) = 155h → ~39h 墙钟\\n- 距 EACL ARR deadline (Aug 3): 74 天\\n\\n## Dream 审稿摘要 (Re-dream, D009)\\n| 档位 | 分数 | 核心反馈 |\\n|------|------|---------|\\n| Best | 4/6 WA | CaCLR underspec, CKA depth confound, arch confound, scope+controls 认可 |\\n| Median | 3/6 WR | Novelty insufficient (DA theory predicts), self-debunking less impactful |\\n| Worst | 3/6 WR | Contributions trivial/confirmatory, control task finding should be centered |\\n\\n### D009 确认行动项 (已全部执行 ✅)\\n1. CaCLR 完整实现规格 → plan_003 notes\\n2. CKA partial correlation controlling for depth → plan_011 (最关键分析)\\n3. Architecture-dependence 限定为 observational → paper_framing.md Claim 1\\n4. Control task finding 提升到 story spine → paper_framing.md\\n5. 补充引用: Zhao et al. 2019, DALI, Pires et al., Wu & Dredze → paper_framing.md\\n6. CKA: \\\"geometric/correlational analysis\\\" 非 \\\"mechanistic\\\" → paper_framing.md + plan_011\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D012 | 2026-05-21 | Novelty strategy: CKA partial correlation (plan_01 | plan_011, plan_013, plan_012 |\\n| D011 | 2026-05-21 | Revert to parallel download: Llama4 (66GB) + Qwen3 | plan_001, plan_002 |\\n| D010 | 2026-05-20 | GlobalMMLU data decisions: test 70/30 split for Ca | — |\\n| D009 | 2026-05-20 | Re-dream processed (4/3/3), P0 approved with condi | — |\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n\\n\", \"lines\": 67}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "a04223c3-b29b-476e-9978-a1fe832be893",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\\\", \\\"content\\\": \\\"# xling_calib_direction — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 01:18 UTC | 更新原因: Correct model sizes (Llama4 66GB, Qwen3 122GB), revert to parallel download strategy, disk math confirms both fit\\\\n\\\\n## 核心方向\\\\nCross-lingual correctness probe transfer: 探索 LLM 内部 correctness direction 的跨语言可迁移性，测试 probe-based calibration 在非英语语言的可行性。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Research phase — MVP 通过 (D004), Dream 审稿两轮完成 (D005→D009), P0 条件批准\\\\n- **MVP**: 3/3 完成 (mvp_001 ✓, mvp_002 ✓, mvp_003 ✓)\\\\n- **代码准备**: 全部就绪 ✅\\\\n  - transfer_eval.py: 5 种 transfer methods 已部署 (zero-shot, mean-shift, Procrustes, few-shot, CaCLR)\\\\n  - extract_activations_large.py: register_forward_hook + post-norm + 70/30 split ✅\\\\n  - train_caclr.py: M007 梯度修复已验证 ✅\\\\n- **模型下载** (并行，磁盘充足):\\\\n  - Llama4 Scout W4A16: ~44GB/66GB，ETA ~30-45min\\\\n  - Qwen3 GPTQ-Int4: ~38GB/122GB，ETA ~2-3h\\\\n  - 两模型合计 ~188GB，基础占用 ~88GB，总计 ~276GB/350GB = 79%\\\\n- **P1 先行**: plan_013 控制任务 ✅ (selectivity 0.262 at L27), plan_012 Procrustes sensitivity 运行中\\\\n- **关键发现**: Pareto tradeoff Qwen strong/Llama weak; mean-shift rank-invariance proof; few-shot +4.9pp AUROC over zero-shot\\\\n\\\\n## 近期任务\\\\n- [ ] Llama4 下载完成 (~30-45min) → 完整性验证 → dry-run → 正式审批 plan_002\\\\n- [ ] Qwen3 下载完成 (~2-3h) → 完整性验证 → dry-run → 正式审批 plan_001\\\\n- [ ] plan_002 执行: 提取激活 (12 layers × 20 langs) → 5 种 transfer eval\\\\n- [ ] plan_001 执行: 提取激活 (24 layers × 20 langs) → 5 种 transfer eval\\\\n- [ ] Procrustes sensitivity 结果收集 + CSV 完整性验证 (双进程写入风险)\\\\n- [ ] CPU-bound P1 (plan_011/012/013) 与 P0 并行推进\\\\n\\\\n## GPU 预算\\\\n- 服务器: westd-13176 (4× RTX 6000 PRO 96GB)\\\\n- 磁盘: /root/autodl-tmp/ 350GB total，下载完成后 ~276GB used (~74GB 余量)\\\\n- 激活存储策略: 先提取 Llama4 (~33GB) → 实验 → 可删模型释放 66GB → 再提取 Qwen3\\\\n- P0 总 GPU 预算: plan_001(80h) + plan_002(40h) + plan_003(20h) + plan_004(15h) = 155h → ~39h 墙钟\\\\n- 距 EACL ARR deadline (Aug 3): 74 天\\\\n\\\\n## Dream 审稿摘要 (Re-dream, D009)\\\\n| 档位 | 分数 | 核心反馈 |\\\\n|------|------|---------|\\\\n| Best | 4/6 WA | CaCLR underspec, CKA depth confound, arch confound, scope+controls 认可 |\\\\n| Median | 3/6 WR | Novelty insufficient (DA theory predicts), self-debunking less impactful |\\\\n| Worst | 3/6 WR | Contributions trivial/confirmatory, control task finding should be centered |\\\\n\\\\n### D009 确认行动项 (已全部执行 ✅)\\\\n1. CaCLR 完整实现规格 → plan_003 notes\\\\n2. CKA partial correlation controlling for depth → plan_011 (最关键分析)\\\\n3. Architecture-dependence 限定为 observational → paper_framing.md Claim 1\\\\n4. Control task finding 提升到 story spine → paper_framing.md\\\\n5. 补充引用: Zhao et al. 2019, DALI, Pires et al., Wu & Dredze → paper_framing.md\\\\n6. CKA: \\\\\\\"geometric/correlational analysis\\\\\\\" 非 \\\\\\\"mechanistic\\\\\\\" → paper_framing.md + plan_011\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D012 | 2026-05-21 | Novelty strategy: CKA partial correlation (plan_01 | plan_011, plan_013, plan_012 |\\\\n| D011 | 2026-05-21 | Revert to parallel download: Llama4 (66GB) + Qwen3 | plan_001, plan_002 |\\\\n| D010 | 2026-05-20 | GlobalMMLU data decisions: test 70/30 split for Ca | — |\\\\n| D009 | 2026-05-20 | Re-dream processed (4/3/3), P0 approved with condi | — |\\\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\\\n\\\\n\\\", \\\"lines\\\": 67}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/ROADMAP.md\", \"content\": \"# xling_calib_direction — Research Dashboard\\n\\n> 最后更新: 2026-05-21 01:18 UTC | 更新原因: Correct model sizes (Llama4 66GB, Qwen3 122GB), revert to parallel download strategy, disk math confirms both fit\\n\\n## 核心方向\\nCross-lingual correctness probe transfer: 探索 LLM 内部 correctness direction 的跨语言可迁移性，测试 probe-based calibration 在非英语语言的可行性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research phase — MVP 通过 (D004), Dream 审稿两轮完成 (D005→D009), P0 条件批准\\n- **MVP**: 3/3 完成 (mvp_001 ✓, mvp_002 ✓, mvp_003 ✓)\\n- **代码准备**: 全部就绪 ✅\\n  - transfer_eval.py: 5 种 transfer methods 已部署 (zero-shot, mean-shift, Procrustes, few-shot, CaCLR)\\n  - extract_activations_large.py: register_forward_hook + post-norm + 70/30 split ✅\\n  - train_caclr.py: M007 梯度修复已验证 ✅\\n- **模型下载** (并行，磁盘充足):\\n  - Llama4 Scout W4A16: ~44GB/66GB，ETA ~30-45min\\n  - Qwen3 GPTQ-Int4: ~38GB/122GB，ETA ~2-3h\\n  - 两模型合计 ~188GB，基础占用 ~88GB，总计 ~276GB/350GB = 79%\\n- **P1 先行**: plan_013 控制任务 ✅ (selectivity 0.262 at L27), plan_012 Procrustes sensitivity 运行中\\n- **关键发现**: Pareto tradeoff Qwen strong/Llama weak; mean-shift rank-invariance proof; few-shot +4.9pp AUROC over zero-shot\\n\\n## 近期任务\\n- [ ] Llama4 下载完成 (~30-45min) → 完整性验证 → dry-run → 正式审批 plan_002\\n- [ ] Qwen3 下载完成 (~2-3h) → 完整性验证 → dry-run → 正式审批 plan_001\\n- [ ] plan_002 执行: 提取激活 (12 layers × 20 langs) → 5 种 transfer eval\\n- [ ] plan_001 执行: 提取激活 (24 layers × 20 langs) → 5 种 transfer eval\\n- [ ] Procrustes sensitivity 结果收集 + CSV 完整性验证 (双进程写入风险)\\n- [ ] CPU-bound P1 (plan_011/012/013) 与 P0 并行推进\\n\\n## GPU 预算\\n- 服务器: westd-13176 (4× RTX 6000 PRO 96GB)\\n- 磁盘: /root/autodl-tmp/ 350GB total，下载完成后 ~276GB used (~74GB 余量)\\n- 激活存储策略: 先提取 Llama4 (~33GB) → 实验 → 可删模型释放 66GB → 再提取 Qwen3\\n- P0 总 GPU 预算: plan_001(80h) + plan_002(40h) + plan_003(20h) + plan_004(15h) = 155h → ~39h 墙钟\\n- 距 EACL ARR deadline (Aug 3): 74 天\\n\\n## Dream 审稿摘要 (Re-dream, D009)\\n| 档位 | 分数 | 核心反馈 |\\n|------|------|---------|\\n| Best | 4/6 WA | CaCLR underspec, CKA depth confound, arch confound, scope+controls 认可 |\\n| Median | 3/6 WR | Novelty insufficient (DA theory predicts), self-debunking less impactful |\\n| Worst | 3/6 WR | Contributions trivial/confirmatory, control task finding should be centered |\\n\\n### D009 确认行动项 (已全部执行 ✅)\\n1. CaCLR 完整实现规格 → plan_003 notes\\n2. CKA partial correlation controlling for depth → plan_011 (最关键分析)\\n3. Architecture-dependence 限定为 observational → paper_framing.md Claim 1\\n4. Control task finding 提升到 story spine → paper_framing.md\\n5. 补充引用: Zhao et al. 2019, DALI, Pires et al., Wu & Dredze → paper_framing.md\\n6. CKA: \\\"geometric/correlational analysis\\\" 非 \\\"mechanistic\\\" → paper_framing.md + plan_011\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D012 | 2026-05-21 | Novelty strategy: CKA partial correlation (plan_01 | plan_011, plan_013, plan_012 |\\n| D011 | 2026-05-21 | Revert to parallel download: Llama4 (66GB) + Qwen3 | plan_001, plan_002 |\\n| D010 | 2026-05-20 | GlobalMMLU data decisions: test 70/30 split for Ca | — |\\n| D009 | 2026-05-20 | Re-dream processed (4/3/3), P0 approved with condi | — |\\n| D008 | 2026-05-20 | Clarify P1 criterion: mvp_003 is 2/4 PASS (not 3/4 | mvp_003, mvp_001 |\\n| D007 | 2026-05-20 | mvp_003 (Llama-3.1-8B) cross-architecture validati | mvp_003, mvp_001 |\\n| D006 | 2026-05-20 | MVP gate re-evaluation after P1 leakage fix: 2/4 P | mvp_001, plan_003 |\\n| D005 | 2026-05-20 | Dream review (3/6 weak reject) processed: 13 confi | plan_003, plan_011, plan_012, plan_013 |\\n| D004 | 2026-05-20 | MVP gate: 3/4 PASS，核心假设获充分支持，进入 research 阶段 | mvp_001 |\\n| D003 | 2026-05-20 | P4 criterion 从 ΔAUROC ≥ 2pp 改为 ΔECE ≤ -2pp for ≥3/ | mvp_001 |\\n\\n\", \"lines\": 67}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the method section. I need to:

1. Follow the 6 subsection structure exactly
2. ~1200 words
3. No em-dashes, no -ing phrase endings, no AI style
4. Complete CaCLR specs, mean-shift rank-invariance proof
5. All symbols defined on first use
6. Proper citations with known bibtex keys and [TO_ADD_BIB] markers

Let me draft this carefully.

Key bibtex keys I have:
- miao2026closing
- xiao2025knowledge


- civelli2026shared
- zhou2025lace
- miao2026coral
- karandikar2021sbece
- ravisankar2026dali
- liu2025middle
- joshi2025calibrating
- confidence_manifold2026
- khanmohammadi2025ccps

And I need to add [TO_ADD_BIB] markers for hewitt2019control, kornblith2019cka, bendavid2010theory, artetxe2018vecmap, and conneau2018muse.

Now I'm planning out the method section structure with a word budget of roughly 1200 words across six subsections, with the transfer methods section taking up the bulk at around 450 words since it needs to cover CaCLR details and the mean-shift proof. I need to be careful about style constraints—avoiding em-dashes, -ing phrase endings, and certain transition words, plus steering clear of "leverage" and "utilize."

For the mean-shift rank-invariance proof, I'm working through the logic: when we apply mean-shift alignment followed by StandardScaler and LogisticRegression, subtracting the mean difference from target activations is equivalent to adding a constant offset to the probe logits. Since AUROC only cares about the relative ordering of predictions, this constant shift leaves AUROC unchanged, so the change in AUROC is zero.

Now I'm drafting the full LaTeX content with proper equation formatting, citation styles, and making sure each paragraph stays between 5-8 sentences while defining all terms on first use.

For CaCLR, I need to document the experimental setup: the kernel choice (Gaussian RBF with median heuristic for bandwidth), the optimizer settings (Adam with learning rate 1e-3), how I initialize from the standard logistic regression solution, the data source (GlobalMMLU test split), the 1-D limitation and why it matters, the sensitivity analysis across α and β hyperparameters, early stopping based on English validation ECE, and relegating batch size and epoch details to the appendix.

Now I'm working through the mean-shift proof more carefully. The StandardScaler is fit on English data using μ_en and σ_en, so when I apply it to target activations without alignment, I get z_t = (h_t - μ_en) / σ_en. With mean-shift alignment where I shift target activations by δ = μ_en - μ_t, the scaled result becomes (h_t - μ_t) / σ_en, which normalizes the target to its own mean while preserving the English variance—this is the key to why the alignment works.

The difference between aligned and unaligned logits is constant across all samples: w^T c where c = δ / σ_en, so mean-shift just adds a fixed offset to the logit predictions.

Since AUROC only depends on the relative ranking of samples, this constant shift doesn't affect the metric at all.

Now I'm drafting the full method section with proper notation and a formal proof paragraph, aiming for around 1200 words total across all subsections.

Writing LaTeX for method section... I'm distinguishing correctness probing from related approaches like knowledge boundary probing, which operates at the input level, and difficulty probing, which uses Item Response Theory to capture language-agnostic question properties. The core question I'm exploring is whether a correctness probe trained on English can transfer zero-shot to other languages, and which alignment strategies enhance that transfer. Now I need to structure the experimental framework, covering the models, languages, datasets, and activation extraction methods, followed by the alignment approaches including zero-shot evaluation, mean-shift alignment with theoretical justification, Procrustes alignment, few-shot adaptation, and a contrastive learning method with full specifications.

I'm allocating space across the subsections—roughly 120 words for the introduction, 200 for the experimental setup, 550 for the alignment methods which is the core contribution, and smaller sections for the remaining components, totaling around 1200 words in the double-column format. Now I'll write out the full LaTeX carefully, keeping track of citations that need to be added later.

Writing the full paper section... Writing the method section...

I'm distinguishing correctness probing from related approaches like knowledge boundary probing and difficulty probing, then framing the core research question about whether probes trained on English can transfer zero-shot to other languages. For the experimental setup, I'm specifying the models we're evaluating—Qwen3-8B and Llama4-Scout as the main ones, with additional models for validation—and outlining that we're testing across 20 languages spanning different resource levels.

Now I'm detailing how we partition the GlobalMMLU data into training and evaluation sets using stratified sampling, with English labels derived only from the training portion. For activation extraction, I'm sampling residual stream outputs at regular intervals depending on model depth and applying INT8 quantization to manage memory constraints.

I'm evaluating performance using AUROC for discrimination ability, ECE for calibration, Brier score, and selectivity metrics. Then I'm comparing five transfer approaches, starting with a zero-shot baseline where the English probe applies directly to target languages unchanged, followed by mean-shift alignment that adjusts for cross-lingual activation differences before probing.

Now I'm working through the mathematical proof that mean-shift alignment preserves AUROC under our StandardScaler and logistic regression setup—the key insight is that subtracting the mean difference from target activations only adds a constant to each scaled dimension, which doesn't affect ranking or the model's discriminative ability. I'm learning an orthogonal transformation matrix using parallel sentence pairs to align the English and target language representations, similar to cross-lingual word embedding methods. The results show that around 50 pairs capture most of the alignment benefit, with high-resource languages needing fewer pairs than low-resource ones. Interestingly, Procrustes alignment helps when the zero-shot performance is weak but actually hurts when it's already strong.

For the few-shot approach, I'm retraining the probe with a small labeled dataset in the target language. Then I'm introducing CaCLR, which combines three objectives: standard binary cross-entropy loss on the English training data, a calibration-focused loss using expected calibration error, and a cross-lingual consistency term that ties everything together.

The consistency component uses Maximum Mean Discrepancy on the probe's output logits from parallel English and target-language examples, which lets gradients flow back to the probe parameters. I'm using a Gaussian RBF kernel with median heuristic bandwidth, and the parallel data comes from the unlabeled portion of the training split—no target-language labels needed. I initialize from logistic regression and optimize with Adam.

For the difficulty-capability decomposition, I'm training IRT-based probes to identify question difficulty as a language-agnostic property, then projecting out that difficulty direction from the representations to isolate the capability-specific component.

Now I'm analyzing cross-lingual representational similarity using Centered Kernel Alignment, and I've discovered a Simpson's Paradox in the relationship between CKA and transfer performance—the raw correlation is negative because both metrics covary with depth, but once I control for depth, the partial correlation becomes positive and significant.

I'm also measuring the angular distance between correctness directions across languages to understand the geometric structure of these representations. Additionally, I'm applying control task validation to ensure the probes are capturing genuine correctness information rather than surface patterns, using PCA dimensionality reduction and cross-validation to prevent overfitting.

The selectivity analysis reveals that meaningful correctness information concentrates in the middle layers, particularly layers 20 through 27, while shallow layers show minimal selectivity. However, about 28% of low-resource language-layer combinations fall below the selectivity threshold, suggesting some of the reported transfer performance may be inflated by capacity artifacts rather than genuine cross-lingual alignment.

Now I'm reviewing my draft against the requirements—checking that I've covered the problem formulation, distinguished this from related work, included all five transfer methods with their specifications, and verified the terminology is precise throughout. I'm verifying the notation is consistent throughout—the hidden representations, probe weights, linear probes, and evaluation metrics all check out. The draft feels solid, so I'm ready to finalize it, though I should decide whether the proof needs a formal Proposition/Proof environment or if an inline approach with a bold heading works better for the methods section. I'm also going to use a placeholder for the section reference about CaCLR's 1-D limitation since I don't know the final section numbering yet, and I want to confirm that the ACL template supports the `\textsc` command.

One more thing to nail down: the spec asks me to use "first large-scale study comparing correctness probe transfer across architectures" for the framing rather than "first systematic study," and to use "zero-correctness-label" instead of "zero-label" when describing CaCLR's requirements—I'll make sure those phrasings are in place.

Now I'm working through the final version and adding equation labels for cross-referencing. Let me verify the mean-shift normalization proof one more time: StandardScaler computes mean and standard deviation on English training data, then for target samples I apply a shift by the difference between English and target means, which preserves the normalized representation up to a constant offset that doesn't affect the logit output.

Actually, I need to be more careful with the notation—the mean-shifted target activation should be h_t + δ where δ = μ_en - μ_t, so when I normalize by the English scaler I get a different expression than what I initially wrote. Let me re-derive this properly from the beginning. I'm verifying the algebra works out—the difference between the normalized values with and without mean-shift gives me that constant $c_i$ term, which confirms the derivation is sound. Now I need to present this more clearly in the paper.

I should also standardize the language tier labels to use small caps consistently throughout, and make sure the reference to the CaCLR limitation is properly formatted even if it's still a draft. The language list formatting needs attention too.

Now I'm finalizing the document structure—I realize the \paragraph{} organization within each subsection is actually standard practice for ACL papers, so that approach should work fine. For the proof, an inline statement with bold formatting is more space-efficient than a formal theorem environment, which fits better with the method section style. Let me write out the complete LaTeX content while keeping everything within the ~1200 word target.

I also need to double-check the style constraint about avoiding sentences that end with -ing phrases. Looking through my draft, I don't see any trailing gerunds like "demonstrating that" or "reducing the ECE by"—the -ing words I have are either at the start of clauses or embedded within phrases, so that should be fine. Let me produce the final version now, making sure all equations and formatting are complete.

I'm doing a word count across the sections to see where I stand. The current draft totals around 1160 words, which is close to the 1200-word target. I should expand a couple of sections slightly—particularly §3.5 and §3.6—to reach closer to 1200 without overdoing it. I also need to make sure I include the "zero-correctness-label" terminology for CaCLR as specified, so I'll work that phrasing in where it belongs. I'm finalizing the LaTeX output now, making sure to use "zero-correctness-label" terminology as specified and verifying that `\textsc{}` will render properly in the ACL template. Let me also quickly confirm the file doesn't already exist before writing it, and do a final check against the task requirements to ensure I've covered the problem formulation, probe definition, model specifications across all four models, the twenty languages organized by tier, and the GlobalMMLU test data. I'm finishing up the checklist—subspace angle analysis, geometric framing, probing controls with proper cross-validation, capacity artifact warnings, and all the formatting requirements like symbol definitions, bibliography keys, and avoiding em-dashes and gerunds. I should clarify that CaCLR is positioned as a natural baseline for distributional matching, not a novel contribution, then I'm ready to write the final version.

Now I need to reframe how I present CaCLR—emphasizing that we're testing whether distributional matching improves transfer rather than proposing a new method. The intro should also highlight this as the first large-scale study comparing correctness probe transfer across architectures. I've already cited the relevant Procrustes alignment work like MUSE and VecMap, so that's covered. For the experimental setup, I'm noting the optimizer details, warm-start initialization from standard LR, early stopping on English validation ECE, and I'll put batch size and epoch specifics in the appendix along with the sensitivity sweeps for the hyperparameters.

One key detail I want to make sure is clear: the MMD loss operates on probe logits rather than raw activations to maintain proper gradient flow to the probe parameters. With all these elements confirmed, I'm ready to write out the final LaTeX file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "3d3fb6a7-4faa-472c-93f1-7a36f1e28272",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMwBk51SwabSBN5UidFtZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9832,
      "cache_read_input_tokens": 45173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9832
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_017tbFeJc7GVaCAxM7WEC6o1`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null && echo \"EXISTS\" || echo \"NEW\"",
  "description": "Check if method.tex already exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "ba963603-d904-4e54-8cbd-575e644b9ef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMwBk51SwabSBN5UidFtZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9832,
      "cache_read_input_tokens": 45173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9832
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

_source line 28 · 2026-05-21T05:03:55.599Z_

<details><summary>↩ Tool result · `toolu_017tbFeJc7GVaCAxM7WEC6o1`</summary>

```text
NEW
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "4896f218-7b71-470d-87d5-d51654dfd9e2",
  "tool_use_result": {
    "stdout": "NEW",
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

_source line 29_

Now I'll write the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "712ad8b8-a64f-4b53-b8a3-a38382fa938c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tq3bPHMe4HfPxV6bJeZwee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9326,
      "cache_read_input_tokens": 55005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9326
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

_source line 30_

<details open><summary>🔧 Tool call — Write · `toolu_01QfW66z4cdWs3vUH8ut8ZPu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem}\n\nGiven a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$. A \\emph{correctness probe} is a linear classifier\n\\begin{equation}\n  f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)\n  \\label{eq:probe}\n\\end{equation}\ntrained to predict $p(\\text{correct} \\mid \\mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.\n\nWe distinguish correctness probing from two related tasks. \\emph{Knowledge boundary probing} \\citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \\emph{Difficulty probing} \\citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.\n\n\\subsection{Experimental Framework}\n\\label{sec:framework}\n\n\\paragraph{Models.} We evaluate Qwen3-8B and Llama4-Scout as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).\n\n\\paragraph{Languages.} We test 20 languages spanning three resource tiers based on GlobalMMLU availability: \\textsc{high} (zh, de, fr, es, ja), \\textsc{med} (ar, ko, vi, th, tr), and \\textsc{low} (hi, sw, bn, te, my, am, zu, yo, si, km).\n\n\\paragraph{Data.} We use the GlobalMMLU test split, partitioned 70/30 via stratified sampling into \\texttt{probe\\_train} and \\texttt{eval} portions. English binary correctness labels come from \\texttt{probe\\_train} only; all reported results use \\texttt{eval} exclusively.\n\n\\paragraph{Activation extraction.} We register forward hooks on post-layer-norm residual stream outputs. Layers are sampled at regular intervals (every 4th layer for 28-layer models, every 8th for 96-layer models). We use INT8 quantization for large models and include a FP16 validation ablation at representative layers to control for quantization artifacts.\n\n\\paragraph{Metrics.} We report Area Under the ROC Curve (AUROC) for correctness discrimination, Expected Calibration Error (ECE, 15-bin) for calibration quality, Brier score, and selectivity \\citep{hewitt2019control}. % [TO_ADD_BIB]\n\n\\subsection{Transfer Methods}\n\\label{sec:transfer}\n\nWe compare five methods ordered by complexity.\n\n\\paragraph{(a) Zero-shot transfer.} The English-trained probe $f_l$ is applied directly to target language representations without adaptation. This serves as the baseline for all comparisons.\n\n\\paragraph{(b) Mean-shift alignment.} We subtract the cross-lingual mean difference $\\boldsymbol{\\delta} = \\boldsymbol{\\mu}_{\\text{en}} - \\boldsymbol{\\mu}_t$ from target activations before applying the English probe.\n\n\\textbf{Rank-invariance proof.} Under the StandardScaler fitted on English training data, each dimension is normalized as $z_i = (h_i - \\mu_{\\text{en},i}) / \\sigma_{\\text{en},i}$. After mean-shift, the target representation becomes $h_i + \\delta_i$, and the scaled value is\n\\begin{equation}\n  z'_i = \\frac{h_i + \\delta_i - \\mu_{\\text{en},i}}{\\sigma_{\\text{en},i}} = z_i + c_i\n  \\label{eq:meanshift}\n\\end{equation}\nwhere $c_i = \\delta_i / \\sigma_{\\text{en},i}$ is a constant independent of the input sample. The probe logit then shifts by $\\mathbf{w}^\\top \\mathbf{c}$, a scalar applied identically to every sample. Because AUROC depends only on the ranking of predictions, this uniform offset leaves the ranking unchanged: $\\Delta\\text{AUROC} \\equiv 0$. Our MVP experiments confirm this prediction exactly ($\\Delta\\text{AUROC} = 0.000000$ across 5 languages $\\times$ all layers). ECE can change because binned probability values shift after the sigmoid transformation, but these changes are inconsistent across configurations and do not constitute reliable calibration improvement.\n\n\\paragraph{(c) Procrustes alignment.} We learn an orthogonal mapping from a small set of parallel sentence pairs by solving\n\\begin{equation}\n  \\mathbf{R}^* = \\arg\\min_{\\mathbf{R}^\\top\\mathbf{R}=\\mathbf{I}} \\|\\mathbf{X}_{\\text{en}}\\mathbf{R} - \\mathbf{X}_t\\|_F\n  \\label{eq:procrustes}\n\\end{equation}\nfollowing cross-lingual word embedding alignment methods such as MUSE \\citep{conneau2018muse} and VecMap \\citep{artetxe2018vecmap}. % [TO_ADD_BIB]\nApproximately 50 parallel pairs achieve 98\\% of 200-pair performance. Resource tier matters: \\textsc{high} languages saturate at ${\\sim}$22 pairs and \\textsc{low} languages at ${\\sim}$48. An effect reversal occurs at moderate transfer quality: Procrustes alignment helps when zero-shot AUROC $< 0.50$ but degrades performance when zero-shot AUROC $> 0.60$, which implies that alignment strategy must be conditioned on baseline transfer quality.\n\n\\paragraph{(d) Few-shot probe training.} We retrain the probe from scratch on 25, 50, or 100 target-language labeled examples. This requires target-language correctness labels and serves as an upper-bound reference.\n\n\\paragraph{(e) CaCLR (Calibration-aware Cross-Lingual Regularization).} CaCLR tests whether joint calibration and distributional matching can improve zero-correctness-label transfer. The objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n  \\label{eq:caclr}\n\\end{equation}\n$\\mathcal{L}_{\\text{BCE}}$ is standard binary cross-entropy on English \\texttt{probe\\_train} labels. $\\mathcal{L}_{\\text{SB-ECE}}$ is the differentiable Soft-Binned ECE (SB-ECE) of \\citet{karandikar2021sbece}, which replaces hard histogram bins with soft assignments to enable gradient-based calibration optimization. $\\mathcal{L}_{\\text{consistency}}$ is Maximum Mean Discrepancy (MMD) computed on \\emph{probe logits} from parallel English and target-language inputs. Operating on probe outputs (rather than raw activations) ensures gradient flow to probe parameters. For linear probes, the logit $\\mathbf{w}^\\top \\mathbf{h} + b$ is one-dimensional, so MMD operates in 1-D space; we discuss this design limitation in \\S\\ref{sec:discussion}. We use a Gaussian RBF kernel with bandwidth selected by the median heuristic. Parallel activations come from the GlobalMMLU \\texttt{probe\\_train} portion (70\\% of test split); no target-language correctness labels are required. The probe is initialized from the standard logistic regression solution (warm start) and optimized with Adam (learning rate $10^{-3}$). We apply early stopping based on English validation ECE. Both $\\alpha$ and $\\beta$ are swept across three orders of magnitude; batch size and epoch count are reported in the Appendix.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomposition}\n\nWe train IRT-based difficulty probes that predict question difficulty, a language-agnostic property independent of model capability. To isolate the capability-specific component, we project out the difficulty direction from each representation:\n\\begin{equation}\n  \\mathbf{h}_l^{\\text{res}} = \\mathbf{h}_l - (\\mathbf{h}_l \\cdot \\hat{\\mathbf{w}}_{\\text{diff}})\\hat{\\mathbf{w}}_{\\text{diff}}\n  \\label{eq:residual}\n\\end{equation}\nwhere $\\hat{\\mathbf{w}}_{\\text{diff}}$ is the unit-norm difficulty direction. We retrain correctness probes on the residual $\\mathbf{h}_l^{\\text{res}}$ and compare cross-lingual transfer. This decomposition yields a prescriptive signal: when the difficulty component dominates a language-layer combination, transfer should succeed because the underlying structure is shared across languages. When the capability component dominates, transfer should degrade because the encoding is language-specific.\n\n\\subsection{Geometric Analysis}\n\\label{sec:geometric}\n\nWe quantify cross-lingual representational similarity with Centered Kernel Alignment (CKA) \\citep{kornblith2019cka}. % [TO_ADD_BIB]\nThe central analysis applies partial correlation to control for layer depth, which reveals a Simpson's Paradox in the CKA-transfer relationship. The raw correlation between CKA and transfer AUROC across all language-layer pairs is negative, because both quantities covary with depth (deeper layers have lower CKA and, in some architectures, lower transfer AUROC). After controlling for depth, the partial correlation reverses sign: within each layer, higher cross-lingual CKA predicts better probe transfer (Llama pilot: $\\rho = +0.41$, $p = 0.006$; 14 of 17 layer-level correlations positive). We report bootstrap confidence intervals (1000 resamples) for all partial correlations. We supplement CKA with subspace angle analysis that measures the cross-lingual angular distance between correctness directions $\\mathbf{w}_l$ at each layer. These results are framed as geometric and correlational analysis, not mechanistic explanation.\n\n\\subsection{Probing Controls}\n\\label{sec:controls}\n\nWe validate probe quality with the control task framework of \\citet{hewitt2019control}. % [TO_ADD_BIB]\nSelectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\\% of low-resource combinations fall below a meaningful selectivity threshold, which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "5b5bb4b2-9f19-492a-802b-2070bac76b4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tq3bPHMe4HfPxV6bJeZwee",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9326,
      "cache_read_input_tokens": 55005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9326
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

_source line 31 · 2026-05-21T05:05:02.194Z_

<details><summary>↩ Tool result · `toolu_01QfW66z4cdWs3vUH8ut8ZPu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "d3e5e3e5-44d6-49fb-a6b9-bdbda32aaf58",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem}\n\nGiven a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$. A \\emph{correctness probe} is a linear classifier\n\\begin{equation}\n  f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)\n  \\label{eq:probe}\n\\end{equation}\ntrained to predict $p(\\text{correct} \\mid \\mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.\n\nWe distinguish correctness probing from two related tasks. \\emph{Knowledge boundary probing} \\citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \\emph{Difficulty probing} \\citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.\n\n\\subsection{Experimental Framework}\n\\label{sec:framework}\n\n\\paragraph{Models.} We evaluate Qwen3-8B and Llama4-Scout as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).\n\n\\paragraph{Languages.} We test 20 languages spanning three resource tiers based on GlobalMMLU availability: \\textsc{high} (zh, de, fr, es, ja), \\textsc{med} (ar, ko, vi, th, tr), and \\textsc{low} (hi, sw, bn, te, my, am, zu, yo, si, km).\n\n\\paragraph{Data.} We use the GlobalMMLU test split, partitioned 70/30 via stratified sampling into \\texttt{probe\\_train} and \\texttt{eval} portions. English binary correctness labels come from \\texttt{probe\\_train} only; all reported results use \\texttt{eval} exclusively.\n\n\\paragraph{Activation extraction.} We register forward hooks on post-layer-norm residual stream outputs. Layers are sampled at regular intervals (every 4th layer for 28-layer models, every 8th for 96-layer models). We use INT8 quantization for large models and include a FP16 validation ablation at representative layers to control for quantization artifacts.\n\n\\paragraph{Metrics.} We report Area Under the ROC Curve (AUROC) for correctness discrimination, Expected Calibration Error (ECE, 15-bin) for calibration quality, Brier score, and selectivity \\citep{hewitt2019control}. % [TO_ADD_BIB]\n\n\\subsection{Transfer Methods}\n\\label{sec:transfer}\n\nWe compare five methods ordered by complexity.\n\n\\paragraph{(a) Zero-shot transfer.} The English-trained probe $f_l$ is applied directly to target language representations without adaptation. This serves as the baseline for all comparisons.\n\n\\paragraph{(b) Mean-shift alignment.} We subtract the cross-lingual mean difference $\\boldsymbol{\\delta} = \\boldsymbol{\\mu}_{\\text{en}} - \\boldsymbol{\\mu}_t$ from target activations before applying the English probe.\n\n\\textbf{Rank-invariance proof.} Under the StandardScaler fitted on English training data, each dimension is normalized as $z_i = (h_i - \\mu_{\\text{en},i}) / \\sigma_{\\text{en},i}$. After mean-shift, the target representation becomes $h_i + \\delta_i$, and the scaled value is\n\\begin{equation}\n  z'_i = \\frac{h_i + \\delta_i - \\mu_{\\text{en},i}}{\\sigma_{\\text{en},i}} = z_i + c_i\n  \\label{eq:meanshift}\n\\end{equation}\nwhere $c_i = \\delta_i / \\sigma_{\\text{en},i}$ is a constant independent of the input sample. The probe logit then shifts by $\\mathbf{w}^\\top \\mathbf{c}$, a scalar applied identically to every sample. Because AUROC depends only on the ranking of predictions, this uniform offset leaves the ranking unchanged: $\\Delta\\text{AUROC} \\equiv 0$. Our MVP experiments confirm this prediction exactly ($\\Delta\\text{AUROC} = 0.000000$ across 5 languages $\\times$ all layers). ECE can change because binned probability values shift after the sigmoid transformation, but these changes are inconsistent across configurations and do not constitute reliable calibration improvement.\n\n\\paragraph{(c) Procrustes alignment.} We learn an orthogonal mapping from a small set of parallel sentence pairs by solving\n\\begin{equation}\n  \\mathbf{R}^* = \\arg\\min_{\\mathbf{R}^\\top\\mathbf{R}=\\mathbf{I}} \\|\\mathbf{X}_{\\text{en}}\\mathbf{R} - \\mathbf{X}_t\\|_F\n  \\label{eq:procrustes}\n\\end{equation}\nfollowing cross-lingual word embedding alignment methods such as MUSE \\citep{conneau2018muse} and VecMap \\citep{artetxe2018vecmap}. % [TO_ADD_BIB]\nApproximately 50 parallel pairs achieve 98\\% of 200-pair performance. Resource tier matters: \\textsc{high} languages saturate at ${\\sim}$22 pairs and \\textsc{low} languages at ${\\sim}$48. An effect reversal occurs at moderate transfer quality: Procrustes alignment helps when zero-shot AUROC $< 0.50$ but degrades performance when zero-shot AUROC $> 0.60$, which implies that alignment strategy must be conditioned on baseline transfer quality.\n\n\\paragraph{(d) Few-shot probe training.} We retrain the probe from scratch on 25, 50, or 100 target-language labeled examples. This requires target-language correctness labels and serves as an upper-bound reference.\n\n\\paragraph{(e) CaCLR (Calibration-aware Cross-Lingual Regularization).} CaCLR tests whether joint calibration and distributional matching can improve zero-correctness-label transfer. The objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n  \\label{eq:caclr}\n\\end{equation}\n$\\mathcal{L}_{\\text{BCE}}$ is standard binary cross-entropy on English \\texttt{probe\\_train} labels. $\\mathcal{L}_{\\text{SB-ECE}}$ is the differentiable Soft-Binned ECE (SB-ECE) of \\citet{karandikar2021sbece}, which replaces hard histogram bins with soft assignments to enable gradient-based calibration optimization. $\\mathcal{L}_{\\text{consistency}}$ is Maximum Mean Discrepancy (MMD) computed on \\emph{probe logits} from parallel English and target-language inputs. Operating on probe outputs (rather than raw activations) ensures gradient flow to probe parameters. For linear probes, the logit $\\mathbf{w}^\\top \\mathbf{h} + b$ is one-dimensional, so MMD operates in 1-D space; we discuss this design limitation in \\S\\ref{sec:discussion}. We use a Gaussian RBF kernel with bandwidth selected by the median heuristic. Parallel activations come from the GlobalMMLU \\texttt{probe\\_train} portion (70\\% of test split); no target-language correctness labels are required. The probe is initialized from the standard logistic regression solution (warm start) and optimized with Adam (learning rate $10^{-3}$). We apply early stopping based on English validation ECE. Both $\\alpha$ and $\\beta$ are swept across three orders of magnitude; batch size and epoch count are reported in the Appendix.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomposition}\n\nWe train IRT-based difficulty probes that predict question difficulty, a language-agnostic property independent of model capability. To isolate the capability-specific component, we project out the difficulty direction from each representation:\n\\begin{equation}\n  \\mathbf{h}_l^{\\text{res}} = \\mathbf{h}_l - (\\mathbf{h}_l \\cdot \\hat{\\mathbf{w}}_{\\text{diff}})\\hat{\\mathbf{w}}_{\\text{diff}}\n  \\label{eq:residual}\n\\end{equation}\nwhere $\\hat{\\mathbf{w}}_{\\text{diff}}$ is the unit-norm difficulty direction. We retrain correctness probes on the residual $\\mathbf{h}_l^{\\text{res}}$ and compare cross-lingual transfer. This decomposition yields a prescriptive signal: when the difficulty component dominates a language-layer combination, transfer should succeed because the underlying structure is shared across languages. When the capability component dominates, transfer should degrade because the encoding is language-specific.\n\n\\subsection{Geometric Analysis}\n\\label{sec:geometric}\n\nWe quantify cross-lingual representational similarity with Centered Kernel Alignment (CKA) \\citep{kornblith2019cka}. % [TO_ADD_BIB]\nThe central analysis applies partial correlation to control for layer depth, which reveals a Simpson's Paradox in the CKA-transfer relationship. The raw correlation between CKA and transfer AUROC across all language-layer pairs is negative, because both quantities covary with depth (deeper layers have lower CKA and, in some architectures, lower transfer AUROC). After controlling for depth, the partial correlation reverses sign: within each layer, higher cross-lingual CKA predicts better probe transfer (Llama pilot: $\\rho = +0.41$, $p = 0.006$; 14 of 17 layer-level correlations positive). We report bootstrap confidence intervals (1000 resamples) for all partial correlations. We supplement CKA with subspace angle analysis that measures the cross-lingual angular distance between correctness directions $\\mathbf{w}_l$ at each layer. These results are framed as geometric and correlational analysis, not mechanistic explanation.\n\n\\subsection{Probing Controls}\n\\label{sec:controls}\n\nWe validate probe quality with the control task framework of \\citet{hewitt2019control}. % [TO_ADD_BIB]\nSelectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\\% of low-resource combinations fall below a meaningful selectivity threshold, which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 32_

Now let me verify the output against the requirements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "0fb15967-15f7-4bd4-ad2c-58c02b4be4ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2wY1EtpzVaoVYT8Ch4pns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3058,
      "cache_read_input_tokens": 64331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3058
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01PUZcusdNjUVLvxBUr6FcRA`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper && grep -c \"—\" method.tex && echo \"---\" && grep -n \"—\" method.tex || echo \"NO_EMDASH\"",
  "description": "Check for em-dashes in method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "b2292261-b9d3-4f34-a65a-52e4722b0658",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2wY1EtpzVaoVYT8Ch4pns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3058,
      "cache_read_input_tokens": 64331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3058
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

_source line 34 · 2026-05-21T05:05:07.209Z_

<details><summary>↩ Tool result · `toolu_01PUZcusdNjUVLvxBUr6FcRA`</summary>

```text
0
NO_EMDASH
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "b5f49a4d-99b7-4664-afa3-d8c11ee39c30",
  "tool_use_result": {
    "stdout": "0\nNO_EMDASH",
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01BLhYDbXzgXaUHrceFeD4qr`</summary>

```json
{
  "command": "grep -n \"ing,\" method.tex || echo \"NO_ING_COMMA\" && echo \"---\" && grep -nE \"ing\\.$\" method.tex || echo \"NO_ING_PERIOD\"",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "e1c98154-b71f-41de-95aa-fbbf026b16b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2wY1EtpzVaoVYT8Ch4pns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3058,
      "cache_read_input_tokens": 64331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3058
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

_source line 36 · 2026-05-21T05:05:12.106Z_

<details><summary>↩ Tool result · `toolu_01BLhYDbXzgXaUHrceFeD4qr`</summary>

```text
82:Selectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\% of low-resource combinations fall below a meaningful selectivity threshold, which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.
---
82:Selectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\% of low-resource combinations fall below a meaningful selectivity threshold, which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "df95fc8f-4665-44bb-9955-e609e285a342",
  "tool_use_result": {
    "stdout": "82:Selectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\\% of low-resource combinations fall below a meaningful selectivity threshold, which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.\n---\n82:Selectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot results on Qwen2.5-7B show selectivity concentrated in layers 20 through 27 (0.244 to 0.262), with shallow layers below 0.05. Across the full language-layer grid, approximately 28\\% of low-resource combinations fall below a meaningful selectivity threshold, which indicates that a substantial fraction of reported probing results in these settings reflect capacity artifacts rather than genuine correctness encoding.",
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01L7umM5eyAFqVc2P5uLF5EL`</summary>

```json
{
  "command": "cat method.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g' | sed 's/[{}$%\\\\]//g' | wc -w",
  "description": "Approximate word count of method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "15ef8dc0-fd83-4613-b6d3-d07b308a62f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2wY1EtpzVaoVYT8Ch4pns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3058,
      "cache_read_input_tokens": 64331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3058
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

_source line 38 · 2026-05-21T05:05:12.927Z_

<details><summary>↩ Tool result · `toolu_01L7umM5eyAFqVc2P5uLF5EL`</summary>

```text
1106
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "01afb423-50c3-4623-afd4-b6d1f6f0bf21",
  "tool_use_result": {
    "stdout": "1106",
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

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
The grep found "ing," matches on line 82, but looking at the actual content, these are things like "training", "probing" as nouns/gerunds within sentences, not trailing -ing phrases at sentence endings. Let me check more carefully.

Line 82: "...exploiting representational capacity." - "exploiting" is in the middle, used as a participle within "rather than exploiting", not a trailing -ing phrase. This is fine.

"...probe training to guard against..." - "training" is a noun here. Fine.


"...high-dimensional overfitting, and report..." - "overfitting" is a noun. Fine.

"...correctness encoding." - This ends the section. "encoding" is used as a noun. Let me check if this could be read as a trailing -ing phrase... "reflect capacity artifacts rather than genuine correctness encoding" - "encoding" is a noun here, the object of "reflect". This is fine.

The rule is about sentences ending with participial phrases like "..., demonstrating that...", "..., highlighting the...", "..., leveraging the...". My usage is all nouns/gerunds used as noun phrases, not trailing participial phrases.

No em-dashes found. Word count is ~1106.

I need to recalculate more carefully since the sed command strips LaTeX commands and their arguments, which removes actual content like model names and language codes. Let me try a different counting method to get the real word count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "4207dd4e-3a85-458e-83bc-f369ab17c804",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rtWnyLMkasMjJ9rwZWfUL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 67389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 840
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01Lx3iTAmnma3BKBv5accLRe`</summary>

```json
{
  "command": "detex method.tex 2>/dev/null | wc -w || (cat method.tex | sed 's/\\\\begin{equation}//g; s/\\\\end{equation}//g; s/\\\\label{[^}]*}//g; s/%.*$//g' | wc -w)",
  "description": "More accurate word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "21e2d6a5-a66a-4ba6-9732-112c74e0707e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rtWnyLMkasMjJ9rwZWfUL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 67389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 840
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

_source line 41 · 2026-05-21T05:05:26.543Z_

<details><summary>↩ Tool result · `toolu_01Lx3iTAmnma3BKBv5accLRe`</summary>

```text
1141
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "b80cb59e-9dd6-4418-b7cb-aa20036bcda8",
  "tool_use_result": {
    "stdout": "1141",
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

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
~1141 words after detex, which is close to the ~1200 target. The actual rendered content with inline math and citations will be within the desired range. This is fine.

Let me also verify a few more things:
1. All symbols defined at first use ✓
2. CaCLR implementation specs complete ✓
3. Mean-shift proof present ✓
4. No banned words ✓

Let me check for banned words.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "9aaf777a-7f11-4fd9-ab27-23f58be79d7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m6R6dkhF8qD1MnH4nsNDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 68229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 545
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01N9D7magmQg6smw85gBSiCx`</summary>

```json
{
  "command": "grep -niE \"leverage|utilize|delve|Furthermore|Moreover|Additionally|myriad|plethora\" method.tex || echo \"NO_BANNED_WORDS\"",
  "description": "Check for banned words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "dacdb755-8c33-40a4-8e78-d16080832eb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012m6R6dkhF8qD1MnH4nsNDo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 545,
      "cache_read_input_tokens": 68229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 545
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

_source line 44 · 2026-05-21T05:05:31.861Z_

<details><summary>↩ Tool result · `toolu_01N9D7magmQg6smw85gBSiCx`</summary>

```text
NO_BANNED_WORDS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "3f88d78a-5ea0-49b2-84ab-69efcc1973a4",
  "tool_use_result": {
    "stdout": "NO_BANNED_WORDS",
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

_source line 45_

All checks pass:
- **0 em-dashes**
- **No banned words** (leverage, utilize, delve, etc.)
- **No trailing -ing phrases** (the "ing," hits are nouns like "training", "encoding", "overfitting")
- **~1141 words** (within the ~1200 target)
- All 6 subsections complete with required content
- Mean-shift rank-invariance proof with formal derivation and experimental confirmation
- CaCLR full implementation specs (kernel, optimizer, lr, init, parallel source, 1-D limitation, sweeps, early stopping)
- All symbols defined at first use
- Known bibtex keys used; unknown keys marked with `% [TO_ADD_BIB]` comments

File written to `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "uuid": "dbebd18f-5961-4b7e-b633-dc2224020403",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFq3MRby16nu6yeNiccv3f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 68774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 248
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

_source line 46_

All checks pass:
- **0 em-dashes**
- **No banned words** (leverage, utilize, delve, etc.)
- **No trailing -ing phrases** (the "ing," hits are nouns like "training", "encoding", "overfitting")
- **~1141 words** (within the ~1200 target)
- All 6 subsections complete with required content
- Mean-shift rank-invariance proof with formal derivation and experimental confirmation
- CaCLR full implementation specs (kernel, optimizer, lr, init, parallel source, 1-D limitation, sweeps, early stopping)
- All symbols defined at first use
- Known bibtex keys used; unknown keys marked with `% [TO_ADD_BIB]` comments

File written to `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 302977,
  "duration_api_ms": 304163,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "5513e6af-cbce-4822-b3c4-a84f49b2ee4e",
  "total_cost_usd": 0.95226225,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 57575,
    "cache_read_input_tokens": 444807,
    "output_tokens": 14638,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57575,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 220,
        "cache_read_input_tokens": 68774,
        "cache_creation_input_tokens": 248,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 248
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3900,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.004005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 14638,
      "cacheReadInputTokens": 444807,
      "cacheCreationInputTokens": 57575,
      "webSearchRequests": 0,
      "costUSD": 0.94825725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "28d247ed-7ca5-491f-93fb-94f9e8347716"
}
```

</details>

---
