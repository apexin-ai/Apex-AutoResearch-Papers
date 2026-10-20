# paper writing

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper_writing_20260519T042917.log`
- **Structured JSON:** [`6fc52c85a5a7dcc505c0.json`](../../sessions/6f/6fc52c85a5a7dcc505c0.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
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
  "uuid": "32b69dd9-6455-417b-a44f-673270f5323e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
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
    "resetsAt": 1779181800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a98e5953-a0be-479b-bea5-c91889e894f5",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required files to understand the writing norms and current state of the introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "26988fca-63e7-4d0a-b76a-cec68dcdcfb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3ZNtYrsUpyVLAoEQHyvrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15263,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15263
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

<details open><summary>🔧 Tool call — Read · `toolu_011usCfGoXMYtWG3k9KxcU9S`</summary>

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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "34e43f48-08b1-450e-9989-08908d37784a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3ZNtYrsUpyVLAoEQHyvrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15263,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15263
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

_source line 6 · 2026-05-19T04:29:29.063Z_

<details><summary>↩ Tool result · `toolu_011usCfGoXMYtWG3k9KxcU9S`</summary>

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
213	---
214	
215	## 七、投稿前通用准备
216	
217	### 7.1 模板必须官方（硬规则）
218	
219	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
220	- **不要用**：
221	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
222	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
223	  - 组里学长留的旧版本（来源不明、无法追溯）
224	- 风险：
225	  - 样式不符合 → desk reject
226	  - margin 不对 → 被审稿人质疑诚信
227	  - reference 格式错 → 被认为不规范
228	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
229	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
230	
231	### 7.2 投稿要求逐项核对
232	
233	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
234	- 页数限制：查目标会议官网
235	- 匿名化要求：review 版 vs camera-ready 版本设置不同
236	- 行号开启（review 版常需）
237	- 字体大小、margin 不得修改 sty 文件
238	
239	### 7.3 最终修改 10 项检查流程
240	
241	提交前必须逐一检查：
242	1. 所有最新实验结果已全部录入
243	2. 根据实验结果将叙事调至最优状态
244	3. 附录所有内容在正文中被引用且融入叙事
245	4. 无数据堆砌（每个数字服务于叙事推进）
246	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
247	6. 全文主线统一（idea 变化后各章节逻辑一致）
248	7. 所有专有名词有定义
249	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
250	9. 图表知识密度高、无视觉遮挡
251	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
252	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "a8789dec-9b62-4aa7-8295-e942c03d637c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 252,
      "startLine": 1,
      "totalLines": 252
    }
  }
}
````

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_011LAYjqu2UDKPnWp9gPhZvM`</summary>

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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "adc162b3-a633-4dbc-b868-fd71a2f2f375",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3ZNtYrsUpyVLAoEQHyvrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15263,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15263
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

_source line 8 · 2026-05-19T04:29:29.563Z_

<details><summary>↩ Tool result · `toolu_011LAYjqu2UDKPnWp9gPhZvM`</summary>

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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "6111ca21-e768-4048-82e6-f0a1e716ffa4",
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

<details open><summary>🔧 Tool call — Read · `toolu_01JB7HheNhdh2koCJUsTB5Sh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "7b92e466-d17d-4a9d-9651-bb2c10e0bc47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3ZNtYrsUpyVLAoEQHyvrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15263,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15263
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

_source line 10 · 2026-05-19T04:29:30.066Z_

<details><summary>↩ Tool result · `toolu_01JB7HheNhdh2koCJUsTB5Sh`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Practitioners monitoring iterative training pipelines face a diagnostic blind spot: the metrics most commonly used to detect distributional degradation can yield false positive rates of 62.5--100\% when applied without proper statistical controls, yet no established protocol exists for distinguishing genuine early-warning signals from artifacts of shared non-stationary trends.
5	This blind spot is consequential because iterative training collapse, where models are unwittingly trained on output from earlier generations, is increasingly likely as machine-generated text proliferates on the web~\cite{shumailov2024curse,alemohammad2024mad}.
6	Tail modes vanish, lexical diversity narrows, and calibration deteriorates across generations.
7	These failure modes motivate the search for cheap-to-compute \emph{canary metrics} that provide early warning, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
8	
9	Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
10	Yet the statistical methodology underlying these lead-lag claims (whether a canary metric genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends) has received little scrutiny.
11	
12	We identify several methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:
13	(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends, a well-known hazard when correlating co-trending time series;
14	(2)~no multi-method cross-validation; conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;
15	(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and
16	(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.
17	The closest predecessor is \citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.
18	Their analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests, leaving open the question of whether the observed lead is genuine or an artifact of shared trends.
19	The early-warning framework of \citet{scheffer2009early,scheffer2012anticipating}, widely adopted in ecology for anticipating tipping points, provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\cite{boettiger2012limits}.
20	
21	We address these gaps through a systematic case study of canary prediction of diversity collapse, the progressive loss of lexical diversity in model-generated text across training generations.
22	Using Pythia-410M across six contamination levels ($\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:
23	\begin{enumerate}
24	    \item \textbf{Method sensitivity.} Applied to the same data (16 candidate canary$\to$downstream pairs, including candidates later excluded; \S\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$ (poor agreement).
25	    \item \textbf{Spurious regression.} Canary$\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.
26	    \item \textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\to$diversity pairs FDR-significant at full synthetic replacement ($\alpha{=}1.0$) but 0/24 at $\alpha{\leq}0.25$ (three seeds), with seed-dependent onset at $\alpha{=}0.50$ (0/8--6/8, three seeds), demonstrating that detectability depends sharply on both contamination level and training stochasticity.
27	\end{enumerate}
28	To move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.
29	
30	The framework's utility is demonstrated by its calibration on built-in experimental controls.
31	Naive cross-correlation identifies 100\% of canary--collapse metric pairs as FDR-significant; the uniform consensus pipeline ($K{\geq}4/5$ methods) reduces this to 0\% FPR but yields $p{=}0.16$ under null-calibrated testing, failing to reach conventional significance.
32	MMCT's FPR-inverse weighting resolves this gap, providing formal $p$-values with FPR${=}$0\% and 79.2\% detection at $\alpha{=}0.75$ (a $9.5\times$ improvement over the uniform threshold's 8.3\%).
33	Applying the framework, we identify token entropy as a one-generation-ahead canary for diversity collapse at $\alpha{=}1.0$: the full consensus pipeline confirms directional asymmetry with cross-correlation $|r|{>}0.99$, 24/24 forward-direction pairs FDR-significant, and 0/24 in the reverse direction.
34	Three-seed replication at $\alpha{=}0.75$ extends this finding (19/24 forward, 0/24 reverse via permutation Granger), though method-level consensus remains transitional (Tier~2--3).
35	The onset boundary of causal detectability lies at $\alpha{\approx}0.25$--$0.50$, below which all seeds agree on null.
36	We note that Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
37	Our work constitutes, to our knowledge, the first multiverse-style analysis~\cite{bell2022modeling,kapoor2024reforms} of lead-lag claims in model collapse: the same dataset, analyzed with five statistical methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.
38	
39	Our contributions are:
40	\begin{enumerate}
41	    \item \textbf{Systematic exposure of three methodological pitfalls} (method sensitivity, spurious regression, regime dependence) in lead-lag analysis of iterative training collapse.
42	    Method choice alone inflates spurious-signal rates to at least 62.5\%; first-differencing eliminates canary$\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.
43	    These results demonstrate that single-method, single-regime analyses, the current norm in this literature, are unreliable.
44	
45	    \item \textbf{A Multi-Method Consensus Test (MMCT)} that moves beyond ad-hoc threshold voting to formal inference: the standard $K{\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing; MMCT's pair-level FPR-inverse weighting provides formal $p$-values achieving FPR${=}$0\% and 79.2\% detection at $\alpha{=}0.75$ (a $9.5\times$ improvement over the uniform threshold's 8.3\%).
46	    Shapley-value decomposition (exact 32-coalition enumeration) reveals that naive cross-correlation is the sole FPR driver (Shapley(FPR)${=}{+}0.348$) while permutation Granger is the strongest FPR suppressor (Shapley(FPR)${=}{-}0.194$); these diagnostics provide principled guidance for method panel selection.
47	
48	    \item \textbf{Identification of token entropy as a robust one-generation-ahead canary} for diversity collapse at $\alpha{=}1.0$, confirmed by 4 independent methods, 4 seeds, and cross-architecture replication on GPT-2-medium and OPT-1.3B, with complete directional asymmetry (24/24 forward, 0/24 reverse); directional asymmetry extends to $\alpha{=}0.75$ across 3~seeds (19/24 forward, 0/24 reverse) in a transitional consensus regime (Tier~2--3). The claim is scoped to diversity metrics (distinct-$n$), not model collapse broadly.
49	
50	    \item \textbf{Cross-architecture generalization} (\S\ref{sec:generalization}): validation on three decoder-only transformer families (Pythia-410M, GPT-2-medium, OPT-1.3B) confirms that the entropy-leads-diversity pattern and the consensus framework's operating thresholds transfer across architectures, with all three families reaching Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ and 0 reverse-direction pairs significant in any architecture.
51	\end{enumerate}
52	
53	The remainder of this paper is organized as follows.
54	\S\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.
55	\S\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.
56	\S\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.
57	\S\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\S\ref{sec:method_sensitivity}), regime-dependent detectability (\S\ref{sec:regime}), a case study of canary prediction of diversity collapse (\S\ref{sec:case_study}), consensus framework validation (\S\ref{sec:consensus_validation}), and cross-architecture generalization (\S\ref{sec:generalization}).
58	\S\ref{sec:discussion} discusses implications (including the practical utility paradox, the token entropy--perplexity distinction, and NLP-specific constraints on lead-lag analysis) and outlines directions for future work.
59	\S\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\S\ref{sec:limitations}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "aeae04b2-a052-47e9-b213-d808dc7c4145",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nPractitioners monitoring iterative training pipelines face a diagnostic blind spot: the metrics most commonly used to detect distributional degradation can yield false positive rates of 62.5--100\\% when applied without proper statistical controls, yet no established protocol exists for distinguishing genuine early-warning signals from artifacts of shared non-stationary trends.\nThis blind spot is consequential because iterative training collapse, where models are unwittingly trained on output from earlier generations, is increasingly likely as machine-generated text proliferates on the web~\\cite{shumailov2024curse,alemohammad2024mad}.\nTail modes vanish, lexical diversity narrows, and calibration deteriorates across generations.\nThese failure modes motivate the search for cheap-to-compute \\emph{canary metrics} that provide early warning, analogous to early-warning signals for critical transitions in ecological and climate systems~\\cite{scheffer2009early,scheffer2012anticipating}.\n\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\nYet the statistical methodology underlying these lead-lag claims (whether a canary metric genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends) has received little scrutiny.\n\nWe identify several methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:\n(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends, a well-known hazard when correlating co-trending time series;\n(2)~no multi-method cross-validation; conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;\n(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and\n(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests, leaving open the question of whether the observed lead is genuine or an artifact of shared trends.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating}, widely adopted in ecology for anticipating tipping points, provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\\cite{boettiger2012limits}.\n\nWe address these gaps through a systematic case study of canary prediction of diversity collapse, the progressive loss of lexical diversity in model-generated text across training generations.\nUsing Pythia-410M across six contamination levels ($\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:\n\\begin{enumerate}\n    \\item \\textbf{Method sensitivity.} Applied to the same data (16 candidate canary$\\to$downstream pairs, including candidates later excluded; \\S\\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).\n    \\item \\textbf{Spurious regression.} Canary$\\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.\n    \\item \\textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\\to$diversity pairs FDR-significant at full synthetic replacement ($\\alpha{=}1.0$) but 0/24 at $\\alpha{\\leq}0.25$ (three seeds), with seed-dependent onset at $\\alpha{=}0.50$ (0/8--6/8, three seeds), demonstrating that detectability depends sharply on both contamination level and training stochasticity.\n\\end{enumerate}\nTo move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.\n\nThe framework's utility is demonstrated by its calibration on built-in experimental controls.\nNaive cross-correlation identifies 100\\% of canary--collapse metric pairs as FDR-significant; the uniform consensus pipeline ($K{\\geq}4/5$ methods) reduces this to 0\\% FPR but yields $p{=}0.16$ under null-calibrated testing, failing to reach conventional significance.\nMMCT's FPR-inverse weighting resolves this gap, providing formal $p$-values with FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$ (a $9.5\\times$ improvement over the uniform threshold's 8.3\\%).\nApplying the framework, we identify token entropy as a one-generation-ahead canary for diversity collapse at $\\alpha{=}1.0$: the full consensus pipeline confirms directional asymmetry with cross-correlation $|r|{>}0.99$, 24/24 forward-direction pairs FDR-significant, and 0/24 in the reverse direction.\nThree-seed replication at $\\alpha{=}0.75$ extends this finding (19/24 forward, 0/24 reverse via permutation Granger), though method-level consensus remains transitional (Tier~2--3).\nThe onset boundary of causal detectability lies at $\\alpha{\\approx}0.25$--$0.50$, below which all seeds agree on null.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\nOur work constitutes, to our knowledge, the first multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of lead-lag claims in model collapse: the same dataset, analyzed with five statistical methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls} (method sensitivity, spurious regression, regime dependence) in lead-lag analysis of iterative training collapse.\n    Method choice alone inflates spurious-signal rates to at least 62.5\\%; first-differencing eliminates canary$\\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    These results demonstrate that single-method, single-regime analyses, the current norm in this literature, are unreliable.\n\n    \\item \\textbf{A Multi-Method Consensus Test (MMCT)} that moves beyond ad-hoc threshold voting to formal inference: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing; MMCT's pair-level FPR-inverse weighting provides formal $p$-values achieving FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$ (a $9.5\\times$ improvement over the uniform threshold's 8.3\\%).\n    Shapley-value decomposition (exact 32-coalition enumeration) reveals that naive cross-correlation is the sole FPR driver (Shapley(FPR)${=}{+}0.348$) while permutation Granger is the strongest FPR suppressor (Shapley(FPR)${=}{-}0.194$); these diagnostics provide principled guidance for method panel selection.\n\n    \\item \\textbf{Identification of token entropy as a robust one-generation-ahead canary} for diversity collapse at $\\alpha{=}1.0$, confirmed by 4 independent methods, 4 seeds, and cross-architecture replication on GPT-2-medium and OPT-1.3B, with complete directional asymmetry (24/24 forward, 0/24 reverse); directional asymmetry extends to $\\alpha{=}0.75$ across 3~seeds (19/24 forward, 0/24 reverse) in a transitional consensus regime (Tier~2--3). The claim is scoped to diversity metrics (distinct-$n$), not model collapse broadly.\n\n    \\item \\textbf{Cross-architecture generalization} (\\S\\ref{sec:generalization}): validation on three decoder-only transformer families (Pythia-410M, GPT-2-medium, OPT-1.3B) confirms that the entropy-leads-diversity pattern and the consensus framework's operating thresholds transfer across architectures, with all three families reaching Tier~3 consensus ($K{\\geq}4/5$) at $\\alpha{=}1.0$ and 0 reverse-direction pairs significant in any architecture.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), a case study of canary prediction of diversity collapse (\\S\\ref{sec:case_study}), consensus framework validation (\\S\\ref{sec:consensus_validation}), and cross-architecture generalization (\\S\\ref{sec:generalization}).\n\\S\\ref{sec:discussion} discusses implications (including the practical utility paradox, the token entropy--perplexity distinction, and NLP-specific constraints on lead-lag analysis) and outlines directions for future work.\n\\S\\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\\S\\ref{sec:limitations}).",
      "numLines": 59,
      "startLine": 1,
      "totalLines": 59
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
Now I have a thorough understanding of the current introduction and the target structure. Let me also read the paper_framing.md to ensure I respect all constraints.

Let me also check what citations are available in the bib file to make sure I don't invent any.

Let me now draft the new Introduction. Let me understand the key changes:

1. The current intro has 4 contributions (pitfalls, MMCT, token entropy canary, cross-architecture). The target has 4 contributions in a specific order: Claim 3→2→1→4, which maps to:
   - C1: Systematic exposure of three methodological pitfalls (Claim 3)
   - C2: Regime-dependent detectability with canary blind spot (Claim 2)
   - C3: Token entropy as one-generation-ahead canary (Claim 1)
   - C4: Canary-based early intervention (Claim 4)

2. The 5-paragraph structure needs to be:
   - P1-2: Research background (iterative training collapse + canary metrics motivation)
   - P3: Problem importance (existing lead-lag analysis methodological defects)
   - P4: Existing methods insufficient (4 contributions listed here)
   - P5: Paper roadmap (3 pitfalls + MMCT + case study + intervention)
   - P6: Contribution summary (4 items in specified order)

3. Cross-architecture generalization is no longer a separate contribution; instead, Claim 4 (early intervention) is now the 4th contribution.

4. New elements to include:
   - Regime map spanning 8 alpha values from 0.00 to 1.00
   - Canary blind spot phenomenon at α=0.10
   - Early intervention mechanics (predictive vs reactive approach, one-generation-ahead triggering, 63% peak perplexity reduction, 2-generation faster recovery)
   - MMCT methodology details

Now I'm looking at how to apply Shapley decomposition specifically to diversity metrics rather than treating model collapse as a whole, and I should check the paper_framing.md file for additional context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "f055924a-58ae-4db6-bcda-91dad3b049b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LKBPidM83Ap19dd2gZ8gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13336,
      "cache_read_input_tokens": 27104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13336
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

Let me also check the paper framing document and the bib file for available citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "20d5d90e-1de7-42da-a78b-2bb4551fba15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LKBPidM83Ap19dd2gZ8gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13336,
      "cache_read_input_tokens": 27104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13336
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

<details open><summary>🔧 Tool call — Agent · `toolu_018vNCjWHRLGnbJdJ1SboaSp`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper_framing and bib files",
  "prompt": "I need to find two things in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/:\n1. The paper_framing.md file (or similar framing document)\n2. The .bib file used by the paper\n\nSearch for these files and return their full paths and key content. For the bib file, just list the citation keys (the @article{KEY, or @inproceedings{KEY, etc.) so I know what citations are available. For the framing doc, return the full content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "0aca6ee1-4d86-420c-bfb7-54e91b657833",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LKBPidM83Ap19dd2gZ8gC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13336,
      "cache_read_input_tokens": 27104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13336
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

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad4e7eab64c843e15",
  "tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "description": "Find paper_framing and bib files",
  "task_type": "local_agent",
  "prompt": "I need to find two things in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/:\n1. The paper_framing.md file (or similar framing document)\n2. The .bib file used by the paper\n\nSearch for these files and return their full paths and key content. For the bib file, just list the citation keys (the @article{KEY, or @inproceedings{KEY, etc.) so I know what citations are available. For the framing doc, return the full content.",
  "uuid": "566a4b1a-754c-468c-acbb-bfdf5dc667f4",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da"
}
```

---

## Round 1

39 recorded events

### User

_source line 15 · 2026-05-19T04:29:50.374Z_

I need to find two things in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/:
1. The paper_framing.md file (or similar framing document)
2. The .bib file used by the paper

Search for these files and return their full paths and key content. For the bib file, just list the citation keys (the @article{KEY, or @inproceedings{KEY, etc.) so I know what citations are available. For the framing doc, return the full content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "874cd644-297f-4f01-8b5a-bf1f30d5e09e"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4e7eab64c843e15",
  "tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "description": "Finding **/*.md",
  "usage": {
    "total_tokens": 27277,
    "tool_uses": 1,
    "duration_ms": 2139
  },
  "last_tool_name": "Glob",
  "uuid": "98cdb964-6c00-4eae-be75-c784024e065d",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01WVGtBNSSWJ96t3ebLh8KJa`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "56fff399-34ba-4d03-ba39-9132ad352129",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KotxkKCapy1XCgG5UfSDbZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27268,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 18 · 2026-05-19T04:29:52.537Z_

<details><summary>↩ Tool result · `toolu_01WVGtBNSSWJ96t3ebLh8KJa`</summary>

```text
artifacts/mvp_evaluation_criteria.md
task_context/history/reviewer/loop_1.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
task_context/history/reviewer/loop_2.md
artifacts/literature_scan_20260514.md
artifacts/_project/report/mvp_4seed_verdict.md
docs/IDEA_BRIEF.md
task_context/history/director/loop_2.md
task_context/history/reviewer/loop_3.md
artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md
artifacts/ccf_maxlag7_report.md
artifacts/dream_reports/dream_20260514T184925/median/paper_framing.md
artifacts/dream_reports/dream_20260514T184925/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T184925/best/review_report.md
artifacts/dream_reports/dream_20260514T184925/median/review_report.md
artifacts/dream_reports/dream_20260514T184925/worst/review_report.md
task_context/history/agent/loop_2.md
task_context/history/director/loop_3.md
task_context/history/agent/loop_2_1778805655.md
task_context/history/reviewer/loop_4.md
task_context/history/director/loop_4.md
task_context/history/agent/loop_3.md
task_context/history/agent/loop_4.md
.claude/sessions/agent_4f7f7eac/CLAUDE.md
.claude/sessions/agent_4f7f7eac/AGENTS.md
task_context/history/director/loop_5.md
task_context/history/agent/loop_4_1778822085.md
.claude/sessions/agent_8bc724a9/CLAUDE.md
.claude/sessions/agent_8bc724a9/AGENTS.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_3_1778822265.md
task_context/history/agent/loop_3_1778834841.md
.claude/sessions/agent_926c705f/CLAUDE.md
.claude/sessions/agent_926c705f/AGENTS.md
artifacts/d024_literature_notes.md
artifacts/_project/report/cross_alpha_analysis.md
artifacts/alpha_sweep_a050_s42/report/alpha_sweep_a050_s42_final_analysis.md
artifacts/_project/intermediate/a075_analysis_prep.md
artifacts/a075_analysis_prep.md
artifacts/_project/report/framing_alignment_check_b11471.md
artifacts/_project/report/framing_alignment_check.md
artifacts/framing_alignment_check.md
artifacts/_project/intermediate/d026_optimized_commands.md
artifacts/d026_optimized_commands.md
artifacts/_project/report/d027_report.md
task_context/history/agent/loop_5.md
task_context/history/director/loop_6.md
artifacts/_project/intermediate/generalization_prep.md
artifacts/generalization_prep.md
artifacts/_project/report/panel_analysis_feasibility.md
artifacts/panel_analysis_feasibility.md
artifacts/_project/report/method_ablation_phase2_report.md
artifacts/cross_alpha_v4_ready.md
task_context/history/reviewer/loop_6.md
artifacts/_project/report/d029_fdr_fix_results.md
artifacts/_project/report/d029_rerun_verification.md
artifacts/analysis/consensus_framework/d029_rerun_verification.md
artifacts/_project/report/d028_fpr_update.md
artifacts/analysis/consensus_framework/d028_fpr_update.md
artifacts/_project/report/cross_alpha_fdr_4point.md
artifacts/method_ablation_phase2/report/method_ablation_phase2_summary.md
artifacts/consensus_framework/consensus_framework.md
artifacts/_project/report/consensus_framework.md
artifacts/analysis/consensus_framework/d027_report.md
artifacts/analysis/cross_alpha_fdr_4point.md
task_context/history/agent/loop_5_1778846969.md
artifacts/prep_cross_alpha_v5_verify.md
artifacts/prep_c4_gpt2m_readiness.md
.claude/sessions/agent_fef7ab09/CLAUDE.md
.claude/sessions/agent_fef7ab09/AGENTS.md
.claude/sessions/agent_c15168fa/CLAUDE.md
.claude/sessions/agent_c15168fa/AGENTS.md
artifacts/report_gen_wiki_gpt2m_failure.md
task_context/history/agent/loop_6.md
.claude/sessions/agent_3c8d1c65/CLAUDE.md
.claude/sessions/agent_3c8d1c65/AGENTS.md
artifacts/plan_006_s42/report/plan_006_s42_T18_analysis.md
.claude/sessions/agent_b21c26e7/CLAUDE.md
.claude/sessions/agent_b21c26e7/AGENTS.md
artifacts/alpha_sweep_a075_s42/report/cross_alpha_v6_analysis.md
task_context/history/director/loop_7.md
task_context/history/reviewer/loop_7.md
task_context/history/agent/loop_7.md
task_context/history/director/loop_8.md
task_context/history/agent/loop_7_1778890078.md
artifacts/_project/report/cross_alpha_summary.md
artifacts/cross_alpha_aggregation/cross_alpha_summary.md
artifacts/_project/report/scan_report.md
artifacts/literature_scan_20260515/scan_report.md
artifacts/_project/report/audit_report.md
artifacts/drift_discrepancy_audit/audit_report.md
artifacts/alpha_sweep_a050_s43/report/a050_s43_analysis.md
artifacts/gen_wiki_gpt2m_a100_s42_v3/report/gpt2m_cross_arch_analysis.md
artifacts/gen_wiki_gpt2m_a100_s42_v3/report/five_method_leadlag.md
artifacts/gen_wiki_gpt2m_a100_s42_v3/report/five_method_leadlag_bce78c.md
artifacts/_project/report/kappa_report.md
artifacts/gpt2m_kappa/kappa_report.md
artifacts/_project/report/subset_ablation_report.md
artifacts/method_ablation/subset_ablation_report.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "a269854f-1186-47a6-a6ce-8a9e9dbfbe43"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4e7eab64c843e15",
  "tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "description": "Finding **/*.bib",
  "usage": {
    "total_tokens": 27280,
    "tool_uses": 2,
    "duration_ms": 2271
  },
  "last_tool_name": "Glob",
  "uuid": "a2ac1e70-2cce-45c8-a7a3-93838d6af482",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01TuZ3HinpKomPLrRQSyVnZS`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "35ff79ea-29c0-4e2a-9855-ea3901ce2331",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KotxkKCapy1XCgG5UfSDbZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27268,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27268,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 21 · 2026-05-19T04:29:52.664Z_

<details><summary>↩ Tool result · `toolu_01TuZ3HinpKomPLrRQSyVnZS`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "141b117c-9ea4-4c60-9ce3-09a51a1881ff"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4e7eab64c843e15",
  "tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "description": "Reading docs/paper/references.bib",
  "usage": {
    "total_tokens": 30082,
    "tool_uses": 3,
    "duration_ms": 4751
  },
  "last_tool_name": "Read",
  "uuid": "dadbc687-3fad-4356-baaa-66ab71a49452",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Kp959KjsRuVg1k7ZNCkv61`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "042d36cd-e973-4c4e-b3af-42f2644fb14a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012X1g5ptyAoqs6JofZua4ob",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 27268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2796,
        "ephemeral_1h_input_tokens": 0
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

_source line 24 · 2026-05-19T04:29:55.134Z_

<details><summary>↩ Tool result · `toolu_01Kp959KjsRuVg1k7ZNCkv61`</summary>

```text
1	% ============================================================
2	% CORE MODEL COLLAPSE
3	% ============================================================
4	
5	@article{shumailov2024curse,
6	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
7	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
8	  journal   = {Nature},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2305.17493},
11	}
12	
13	@inproceedings{alemohammad2024mad,
14	  title     = {Self-Consuming Generative Models Go {MAD}},
15	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
16	  booktitle = {International Conference on Learning Representations},
17	  year      = {2024},
18	  url       = {https://arxiv.org/abs/2307.01850},
19	}
20	
21	@inproceedings{dohmatob2024tale,
22	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
23	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
24	  booktitle = {International Conference on Machine Learning},
25	  year      = {2024},
26	  url       = {https://arxiv.org/abs/2402.07043},
27	}
28	
29	@inproceedings{dohmatob2025strong,
30	  title     = {Strong Model Collapse},
31	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
32	  booktitle = {International Conference on Learning Representations},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2410.04840},
35	}
36	
37	@inproceedings{guo2024linguistic,
38	  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
39	  author    = {Guo, Yanzhu and Shang, Guokan and others},
40	  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2311.09807},
43	}
44	
45	
46	@inproceedings{hataya2023will,
47	  title     = {Will Large-scale Generative Models Corrupt Future Datasets?},
48	  author    = {Hataya, Ryuichiro and Bao, Han and Arai, Hiromi},
49	  booktitle = {International Conference on Computer Vision},
50	  year      = {2023},
51	  url       = {https://arxiv.org/abs/2211.08095},
52	}
53	
54	@inproceedings{seddik2024bad,
55	  title     = {How Bad is Training on Synthetic Data? {A} Statistical Analysis},
56	  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
57	  booktitle = {Advances in Neural Information Processing Systems},
58	  year      = {2024},
59	  url       = {https://arxiv.org/abs/2404.05090},
60	}
61	
62	@article{truong2025entropy,
63	  title     = {Entropy Collapse: A Universal Failure Mode of Intelligent Systems},
64	  author    = {Truong, Xuan Khanh and Truong, Quynh Hoa},
65	  journal   = {arXiv preprint arXiv:2512.12381},
66	  year      = {2025},
67	  url       = {https://arxiv.org/abs/2512.12381},
68	}
69	
70	
71	@article{du2026geometric,
72	  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},
73	  author    = {Du, Xin and Tanaka-Ishii, Kumiko},
74	  journal   = {arXiv preprint arXiv:2605.00435},
75	  year      = {2026},
76	  url       = {https://arxiv.org/abs/2605.00435},
77	}
78	
79	@article{gao2021pile,
80	  title     = {The {Pile}: An 800{GB} Dataset of Diverse Text for Language Modeling},
81	  author    = {Gao, Leo and Biderman, Stella and Black, Sid and Golding, Laurence and Hoppe, Travis and Foster, Charles and Phang, Jason and He, Horace and Thite, Anish and Nabeshima, Noa and Presser, Shawn and Leahy, Connor},
82	  journal   = {arXiv preprint arXiv:2101.00027},
83	  year      = {2021},
84	  url       = {https://arxiv.org/abs/2101.00027},
85	}
86	
87	
88	% ============================================================
89	% CANARY / EARLY WARNING METRICS
90	% ============================================================
91	
92	@article{du2025scales,
93	  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},
94	  author    = {Du, Y. and Wu, G. and Tang, G. and Wang, W. and Fan, Q.},
95	  journal   = {arXiv preprint arXiv:2510.05133},
96	  year      = {2025},
97	  url       = {https://arxiv.org/abs/2510.05133},
98	}
99	
100	@article{gambetta2024surplexity,
101	  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
102	  author    = {Gambetta, Daniele and others},
103	  journal   = {arXiv preprint arXiv:2410.12341},
104	  year      = {2024},
105	  url       = {https://arxiv.org/abs/2410.12341},
106	}
107	
108	
109	@article{sigma2026spectral,
110	  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},
111	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
112	  journal   = {arXiv preprint arXiv:2601.03385},
113	  year      = {2026},
114	  url       = {https://arxiv.org/abs/2601.03385},
115	}
116	
117	@article{kalinowski2026topology,
118	  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},
119	  author    = {Kalinowski, Alexander},
120	  journal   = {arXiv preprint arXiv:2604.26984},
121	  year      = {2026},
122	  url       = {https://arxiv.org/abs/2604.26984},
123	}
124	
125	@inproceedings{cao2025entropycal,
126	  title     = {On the Entropy Calibration of Language Models},
127	  author    = {Cao, Steven and Valiant, Gregory and Liang, Percy},
128	  booktitle = {Advances in Neural Information Processing Systems},
129	  year      = {2025},
130	  url       = {https://arxiv.org/abs/2511.11966},
131	}
132	
133	@article{sahoo2026calibration,
134	  title     = {Calibration Collapse Under Sycophancy Fine-Tuning: How Reward Hacking Breaks Uncertainty Quantification in {LLMs}},
135	  author    = {Sahoo, Subramanyam},
136	  journal   = {arXiv preprint arXiv:2604.10585},
137	  year      = {2026},
138	  url       = {https://arxiv.org/abs/2604.10585},
139	}
140	
141	% ============================================================
142	% DIVERSITY METRICS (BACKGROUND)
143	% ============================================================
144	
145	
146	@inproceedings{li2016diversity,
147	  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},
148	  author    = {Li, Jiwei and others},
149	  booktitle = {North American Chapter of the Association for Computational Linguistics},
150	  year      = {2016},
151	  url       = {https://arxiv.org/abs/1510.03055},
152	}
153	
154	% ============================================================
155	% REPRESENTATION / SPECTRAL COLLAPSE
156	% ============================================================
157	
158	
159	% ============================================================
160	% DATA MIXING & ACCUMULATION
161	% ============================================================
162	
163	@inproceedings{kazdan2025collapse,
164	  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},
165	  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},
166	  booktitle = {International Conference on Machine Learning},
167	  year      = {2025},
168	  url       = {https://arxiv.org/abs/2410.16713},
169	}
170	
171	@inproceedings{dey2024breaking,
172	  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},
173	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
174	  booktitle = {International Conference on Machine Learning},
175	  year      = {2024},
176	  url       = {https://arxiv.org/abs/2404.01413},
177	}
178	
179	
180	@inproceedings{fu2025selfconsuming,
181	  title     = {A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops},
182	  author    = {Fu, Shi and Wang, Yingjie and Chen, Yuzhu and Tian, Xinmei and Tao, Dacheng},
183	  booktitle = {International Conference on Learning Representations},
184	  year      = {2025},
185	  url       = {https://arxiv.org/abs/2502.18865},
186	}
187	
188	@article{he2025golden,
189	  title     = {Golden Ratio Weighting Prevents Model Collapse},
190	  author    = {He, Shiliang and Xu, Zhongbin and Cheng, Yan},
191	  journal   = {arXiv preprint arXiv:2502.18049},
192	  year      = {2025},
193	  url       = {https://arxiv.org/abs/2502.18049},
194	}
195	
196	@inproceedings{falahati2026curated,
197	  title     = {Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences},
198	  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},
199	  booktitle = {International Conference on Machine Learning},
200	  year      = {2026},
201	  url       = {https://arxiv.org/abs/2605.07724},
202	}
203	
204	% ============================================================
205	% MITIGATION & VERIFICATION
206	% ============================================================
207	
208	@article{dces2026counter,
209	  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},
210	  author    = {Zhu, Bingze and Xie, Yubo},
211	  journal   = {Electronics},
212	  year      = {2026},
213	  url       = {https://www.mdpi.com/2079-9292/15/4/869},
214	}
215	
216	% ============================================================
217	% POSITION / SURVEY / EPISTEMICS / ANALYTICAL ROBUSTNESS
218	% ============================================================
219	
220	@inproceedings{bell2022modeling,
221	  title     = {Modeling the Machine Learning Multiverse},
222	  author    = {Bell, Samuel J. and Kampman, Onno P. and Dodge, Jesse and Lawrence, Neil D.},
223	  booktitle = {Advances in Neural Information Processing Systems},
224	  year      = {2022},
225	  url       = {https://arxiv.org/abs/2206.05985},
226	}
227	
228	@article{kapoor2024reforms,
229	  title     = {{REFORMS}: Consensus-based Recommendations for Machine-learning-based Science},
230	  author    = {Kapoor, Sayash and Cantrell, Emily and Peng, Kenny and Pham, Thanh Hien and Bail, Christopher A. and Gundersen, Odd Erik and Hofman, Jake M. and Hullman, Jessica and Lones, Michael A. and Malik, Momin M. and Nanayakkara, Priyanka and Poldrack, Russell A. and Raji, Inioluwa Deborah and Roberts, Michael and Salganik, Matthew J. and Serra-Garcia, Marta and Stewart, Brandon M. and Vandewiele, Gilles and Narayanan, Arvind},
231	  journal   = {Science Advances},
232	  volume    = {10},
233	  number    = {18},
234	  pages     = {eadk3452},
235	  year      = {2024},
236	  doi       = {10.1126/sciadv.adk3452},
237	}
238	
239	@article{coretta2023multidimensional,
240	  title     = {Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses},
241	  author    = {Coretta, Stefano and Casillas, Joseph V. and Roessig, Simon and Franke, Michael and others},
242	  journal   = {Advances in Methods and Practices in Psychological Science},
243	  volume    = {6},
244	  number    = {3},
245	  year      = {2023},
246	  doi       = {10.1177/25152459231162567},
247	}
248	
249	@article{simonsohn2020specification,
250	  title     = {Specification curve analysis},
251	  author    = {Simonsohn, Uri and Simmons, Joseph P. and Nelson, Leif D.},
252	  journal   = {Nature Human Behaviour},
253	  volume    = {4},
254	  number    = {11},
255	  pages     = {1208--1214},
256	  year      = {2020},
257	  doi       = {10.1038/s41562-020-0912-z},
258	}
259	
260	@article{schaeffer2025position,
261	  title     = {Position: Model Collapse Does Not Mean What You Think},
262	  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
263	  journal   = {arXiv preprint arXiv:2503.03150},
264	  year      = {2025},
265	  url       = {https://arxiv.org/abs/2503.03150},
266	}
267	
268	% ============================================================
269	% METHODOLOGY (GRANGER / LEAD-LAG)
270	% ============================================================
271	
272	@article{granger1969investigating,
273	  author    = {Granger, Clive W. J.},
274	  title     = {Investigating Causal Relations by Econometric Models and Cross-spectral Methods},
275	  journal   = {Econometrica},
276	  volume    = {37},
277	  number    = {3},
278	  pages     = {424--438},
279	  year      = {1969},
280	  publisher = {Wiley},
281	}
282	
283	@article{shojaie2022granger,
284	  title     = {{Granger} Causality: A Review and Recent Advances},
285	  author    = {Shojaie, Ali and Fox, Emily B.},
286	  journal   = {Annual Review of Statistics and Its Application},
287	  year      = {2022},
288	  url       = {https://arxiv.org/abs/2105.02675},
289	}
290	
291	@article{marcinkevics2022neural,
292	  title     = {{Granger} Causality Using Neural Networks},
293	  author    = {Marcinkevics, Raphael and Vogt, Julia},
294	  journal   = {arXiv preprint arXiv:2208.03703},
295	  year      = {2022},
296	  url       = {https://arxiv.org/abs/2208.03703},
297	}
298	
299	@article{granger1974spurious,
300	  title     = {Spurious Regressions in Econometrics},
301	  author    = {Granger, Clive W. J. and Newbold, Paul},
302	  journal   = {Journal of Econometrics},
303	  volume    = {2},
304	  number    = {2},
305	  pages     = {111--120},
306	  year      = {1974},
307	  doi       = {10.1016/0304-4076(74)90034-7},
308	}
309	
310	@article{toda1995statistical,
311	  title     = {Statistical Inference in Vector Autoregressions with Possibly Integrated Processes},
312	  author    = {Toda, Hiro Y. and Yamamoto, Taku},
313	  journal   = {Journal of Econometrics},
314	  volume    = {66},
315	  number    = {1--2},
316	  pages     = {225--250},
317	  year      = {1995},
318	  doi       = {10.1016/0304-4076(94)01616-8},
319	}
320	
321	@article{ruiz2026causalaudit,
322	  title     = {Causal-Audit: A Framework for Risk Assessment of Assumption Violations in Time-Series Causal Discovery},
323	  author    = {Ruiz, Marco and Arana-Catania, Miguel and Ardila, David R. and Ventura, Rodrigo},
324	  journal   = {arXiv preprint arXiv:2604.02488},
325	  year      = {2026},
326	  url       = {https://arxiv.org/abs/2604.02488},
327	}
328	
329	@article{yi2026causalcompass,
330	  title     = {{CausalCompass}: Evaluating the Robustness of Time-Series Causal Discovery in Misspecified Scenarios},
331	  author    = {Yi, Huiyang and Shen, Xiaojian and Wu, Yonggang and Chen, Duxin and Wang, He and Yu, Wenwu},
332	  journal   = {arXiv preprint arXiv:2602.07915},
333	  year      = {2026},
334	  url       = {https://arxiv.org/abs/2602.07915},
335	}
336	
337	% ============================================================
338	% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)
339	% ============================================================
340	
341	@article{scheffer2009early,
342	  title     = {Early-warning signals for critical transitions},
343	  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},
344	  journal   = {Nature},
345	  year      = {2009},
346	  doi       = {10.1038/nature08227},
347	}
348	
349	@article{scheffer2012anticipating,
350	  title     = {Anticipating Critical Transitions},
351	  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},
352	  journal   = {Science},
353	  year      = {2012},
354	  doi       = {10.1126/science.1225244},
355	}
356	
357	@article{boettiger2012limits,
358	  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},
359	  author    = {Boettiger, Carl and Hastings, Alan},
360	  journal   = {Journal of the Royal Society Interface},
361	  year      = {2012},
362	  doi       = {10.1098/rsif.2012.0125},
363	}
364	
365	% ============================================================
366	% MODELS
367	% ============================================================
368	
369	@inproceedings{biderman2023pythia,
370	  title     = {Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling},
371	  author    = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purber, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar},
372	  booktitle = {International Conference on Machine Learning},
373	  year      = {2023},
374	  url       = {https://arxiv.org/abs/2304.01373},
375	}
376	
377	% ============================================================
378	% DATASETS
379	% ============================================================
380	
381	@inproceedings{merity2017pointer,
382	  title     = {Pointer Sentinel Mixture Models},
383	  author    = {Merity, Stephen and Xiong, Caiming and Bradbury, James and Socher, Richard},
384	  booktitle = {International Conference on Learning Representations},
385	  year      = {2017},
386	  url       = {https://arxiv.org/abs/1609.07843},
387	}
388	
389	% ============================================================
390	% TRAINING DYNAMICS
391	% ============================================================
392	
393	@article{dohare2024plasticity,
394	  title     = {Loss of Plasticity in Deep Continual Learning},
395	  author    = {Dohare, Shibhansh and Hernandez-Garcia, J. Fernando and Rahman, Parash and Mahmood, A. Rupam and Sutton, Richard S.},
396	  journal   = {Nature},
397	  volume    = {632},
398	  pages     = {768--774},
399	  year      = {2024},
400	  url       = {https://www.nature.com/articles/s41586-024-07711-7},
401	}
402	
403	@inproceedings{lyle2023plasticity,
404	  title     = {Understanding Plasticity in Neural Networks},
405	  author    = {Lyle, Clare and Zheng, Zeyu and Nikishin, Evgenii and Avila Pires, Bernardo and Pascanu, Razvan and Dabney, Will},
406	  booktitle = {International Conference on Machine Learning},
407	  year      = {2023},
408	  url       = {https://arxiv.org/abs/2303.01486},
409	}
410	
411	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "e382299d-ac66-4586-b7f7-2597ae36701c"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad4e7eab64c843e15",
  "tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "description": "Reading artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md",
  "usage": {
    "total_tokens": 30083,
    "tool_uses": 4,
    "duration_ms": 5310
  },
  "last_tool_name": "Read",
  "uuid": "f6ffd96a-4262-451f-bcef-674c5f4da1f3",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01TjZ3qhFhkjQcGfFv3wZoLe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "e7eeea2d-4616-4339-80fd-5f697cf87433",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012X1g5ptyAoqs6JofZua4ob",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 27268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2796,
        "ephemeral_1h_input_tokens": 0
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

_source line 27 · 2026-05-19T04:29:55.693Z_

<details><summary>↩ Tool result · `toolu_01TjZ3qhFhkjQcGfFv3wZoLe`</summary>

```text
1	# Paper Framing — distrib_canary_collapse
2	
3	## Target Venue
4	- Primary: AAAI 2027 (expected deadline ~August 2026)
5	- Fallback: EMNLP 2026 Findings (ARR October cycle if AAAI timeline tight)
6	- Note: EMNLP 2026 Main ARR May deadline已过；AAAI 2027 给出充足实验时间
7	
8	## Core Claims (3 条)
9	
10	1. **Canary→Diversity Lead**: 在迭代合成数据训练中，ECE 和 token entropy 作为廉价 canary 指标，稳定领先 diversity 退化（distinct_1/2）1-2 代——提供可量化的早期预警窗口。
11	2. **Regime-Dependent Predictability**: 可预测性取决于 contamination regime——100% self-consuming 下 perplexity 与 canary 同步崩溃（不可预测），低 α 条件下 collapse 更渐进、canary lead time 有望扩展到 quality 指标。Predictability phase diagram 划定可预测/不可预测边界。
12	3. **Methodological Rigor**: 朴素相关分析在非平稳训练指标上产生伪回归；Toda-Yamamoto panel temporal precedence 提供统计严谨的 lead-lag 量化，方法论 ablation 量化伪显著关联被推翻的比例。
13	
14	## Story Spine
15	
16	- **Problem**: Model collapse 的在线监控工具已存在（SIGMA 谱监控、DCES 反应式干预），但没有工作系统性回答"哪些指标最早预测崩溃、领先多久、在什么 regime 下有效"。Du et al. 非正式观察到 ECE 领先 accuracy，但仅限单指标对、1-3 代、无统计检验。
17	
18	- **Existing approaches & their gaps**: SIGMA 提供谱监控但无 lead-time 量化；DCES 反应式而非预测式；Du et al. 是最接近的经验前辈但方法论不足（无正式 time-series 检验、无多家族对比）；Kalinowski 拓扑 CI 针对表征坍缩非合成数据退化且计算昂贵。Truong & Truong 证明一阶相变下标准早期预警指标失效——但仅限特定 regime 和特定指标族。
19	
20	- **Our framing**: 我们不是提出"通用 canary"，而是**系统性映射可预测性的边界**——哪些 collapse 维度可预测（diversity）、哪些不可预测（perplexity in extreme regime）、在什么 contamination 条件下、用什么统计方法。Null results（canary 不 lead perplexity）不是失败，而是 phase diagram 中的一个 boundary data point。
21	
22	- **Headline result template**: "ECE and token entropy predict diversity collapse 1-2 generations ahead (|r|>0.99, p<0.001, 4/4 seeds) in iterative synthetic data training, while a predictability phase diagram reveals regime-dependent boundaries where canary signals exist vs. where synchronous collapse precludes early warning."
23	
24	## Anticipated Reviewer Concerns & Responses
25	
26	| Concern | Response Strategy | Required Experiment |
27	|---------|-------------------|---------------------|
28	| "Canary 不预测 perplexity，实用价值有限" | Framing 为 regime-dependent：100% SC 是极端 regime；α-sweep 展示低 α 下 canary→perplexity 是否恢复 | α-sweep (P0) |
29	| "只在 Pythia-410M 上验证，scale 泛化？" | Spot-check Pythia-1.4B × 核心条件 | scale-check (P1) |
30	| "WikiText-103 单一数据集" | C4 cross-domain validation | domain-transfer (P1) |
31	| "为什么不用简单相关分析？" | 方法 ablation：naive corr vs Toda-Yamamoto，量化伪显著比例 | method-ablation (P0, 零 GPU) |
32	| "4 个 canary 中 2 个失败，选择偏差？" | 全量报告 4 族结果，诚实讨论 effective_rank/self_bleu 失败原因 | 已有 MVP 数据 |
33	| "Intervention 实验缺失" | CRS-triggered vs reactive vs no-intervention 对比 | intervention (P2) |
34	
35	## Venue Fit
36	
37	AAAI 2027 优势：
38	- ML 方法论 track 接受 empirical analysis + 统计方法论贡献
39	- 不要求 SOTA，接受 systematic study with novel methodology
40	- Phase diagram / regime boundary 概念在 AAAI 偏理论的审稿人中有吸引力
41	
42	风险：
43	- 如果被认为"只是 empirical study 没有算法贡献"→ 补 CRS + intervention 提升 method 贡献
44	- 模型规模偏小（Pythia-410M/1.4B）→ 诚实标注 limitation + scaling trend
45	
46	## Key Narrative Constraints (from MVP)
47	
48	1. **不能 claim "canary predicts model collapse"** — 只能 claim "canary predicts diversity collapse"，perplexity 通道在 100% SC 下断裂
49	2. **effective_rank 和 self_bleu 作为 canary 失败** — 必须全量报告，不能只报正面结果
50	3. **distinct_3 的 lead time 不如 distinct_1/2 可靠** — 主文聚焦 distinct_1/2，distinct_3 放 supplementary
51	4. **max_lag=5 可能截断真实 lead** — α-sweep 中增大 max_lag≥7
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "34ba8767-208e-438e-abc1-cbf8aef58f6f"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ad4e7eab64c843e15",
  "tool_use_id": "toolu_018vNCjWHRLGnbJdJ1SboaSp",
  "status": "completed",
  "output_file": "",
  "summary": "Find paper_framing and bib files",
  "usage": {
    "total_tokens": 38729,
    "tool_uses": 4,
    "duration_ms": 18989
  },
  "uuid": "151edaed-fc0c-47d5-8aa1-8fd1520dc282",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da"
}
```

---

### Tool result

_source line 29 · 2026-05-19T04:30:09.366Z_

<details><summary>↩ Tool result · `toolu_018vNCjWHRLGnbJdJ1SboaSp`</summary>

```text
Perfect! I found both files. Here are my findings:

## Files Located

**1. Bibliography File:**
- Full path: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib`

**Citation Keys in the .bib file:**
- `shumailov2024curse`
- `alemohammad2024mad`
- `dohmatob2024tale`
- `dohmatob2025strong`
- `guo2024linguistic`
- `hataya2023will`
- `seddik2024bad`
- `truong2025entropy`
- `du2026geometric`
- `gao2021pile`
- `du2025scales`
- `gambetta2024surplexity`
- `sigma2026spectral`
- `kalinowski2026topology`
- `cao2025entropycal`
- `sahoo2026calibration`
- `li2016diversity`
- `kazdan2025collapse`
- `dey2024breaking`
- `fu2025selfconsuming`
- `he2025golden`
- `falahati2026curated`
- `dces2026counter`
- `bell2022modeling`
- `kapoor2024reforms`
- `coretta2023multidimensional`
- `simonsohn2020specification`
- `schaeffer2025position`
- `granger1969investigating`
- `shojaie2022granger`
- `marcinkevics2022neural`
- `granger1974spurious`
- `toda1995statistical`
- `ruiz2026causalaudit`
- `yi2026causalcompass`
- `scheffer2009early`
- `scheffer2012anticipating`
- `boettiger2012limits`
- `biderman2023pythia`
- `merity2017pointer`
- `dohare2024plasticity`
- `lyle2023plasticity`

**2. Paper Framing Document:**
- Full path: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md`

**Framing Content** (complete):

The paper frames a research contribution around **early warning signals for model collapse in iterative synthetic data training**. The three core claims are:

1. **Canary→Diversity Lead**: Token entropy (ECE) and token entropy metrics lead diversity degradation by 1-2 generations in iterative synthetic data training, providing a quantifiable early warning window.

2. **Regime-Dependent Predictability**: Predictability depends on contamination regime—under 100% self-consuming conditions, perplexity collapses synchronously with canary metrics (unpredictable), while under lower contamination (α), collapse is more gradual and lead time extends to quality metrics. A predictability phase diagram defines boundaries.

3. **Methodological Rigor**: Naive correlation analysis on non-stationary training metrics produces spurious regressions; Toda-Yamamoto panel temporal precedence provides statistically rigorous lead-lag quantification, with methodological ablation quantifying the percentage of false positive correlations.

**Target Venue**: AAAI 2027 (primary) or EMNLP 2026 Findings (fallback)

**Key Narrative Constraints**:
- Cannot claim "canary predicts model collapse"—only "diversity collapse"
- Must report that effective_rank and self_bleu fail as canary metrics
- Perplexity channel breaks under 100% self-consuming conditions
- Distinct_1/2 are reliable; distinct_3 less so
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "935a3da5-320f-4ff7-8fa1-965ed9601fbb",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to find two things in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/:\n1. The paper_framing.md file (or similar framing document)\n2. The .bib file used by the paper\n\nSearch for these files and return their full paths and key content. For the bib file, just list the citation keys (the @article{KEY, or @inproceedings{KEY, etc.) so I know what citations are available. For the framing doc, return the full content.",
    "agentId": "ad4e7eab64c843e15",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found both files. Here are my findings:\n\n## Files Located\n\n**1. Bibliography File:**\n- Full path: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib`\n\n**Citation Keys in the .bib file:**\n- `shumailov2024curse`\n- `alemohammad2024mad`\n- `dohmatob2024tale`\n- `dohmatob2025strong`\n- `guo2024linguistic`\n- `hataya2023will`\n- `seddik2024bad`\n- `truong2025entropy`\n- `du2026geometric`\n- `gao2021pile`\n- `du2025scales`\n- `gambetta2024surplexity`\n- `sigma2026spectral`\n- `kalinowski2026topology`\n- `cao2025entropycal`\n- `sahoo2026calibration`\n- `li2016diversity`\n- `kazdan2025collapse`\n- `dey2024breaking`\n- `fu2025selfconsuming`\n- `he2025golden`\n- `falahati2026curated`\n- `dces2026counter`\n- `bell2022modeling`\n- `kapoor2024reforms`\n- `coretta2023multidimensional`\n- `simonsohn2020specification`\n- `schaeffer2025position`\n- `granger1969investigating`\n- `shojaie2022granger`\n- `marcinkevics2022neural`\n- `granger1974spurious`\n- `toda1995statistical`\n- `ruiz2026causalaudit`\n- `yi2026causalcompass`\n- `scheffer2009early`\n- `scheffer2012anticipating`\n- `boettiger2012limits`\n- `biderman2023pythia`\n- `merity2017pointer`\n- `dohare2024plasticity`\n- `lyle2023plasticity`\n\n**2. Paper Framing Document:**\n- Full path: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/dream_reports/dream_20260514T184925/best/paper_framing.md`\n\n**Framing Content** (complete):\n\nThe paper frames a research contribution around **early warning signals for model collapse in iterative synthetic data training**. The three core claims are:\n\n1. **Canary→Diversity Lead**: Token entropy (ECE) and token entropy metrics lead diversity degradation by 1-2 generations in iterative synthetic data training, providing a quantifiable early warning window.\n\n2. **Regime-Dependent Predictability**: Predictability depends on contamination regime—under 100% self-consuming conditions, perplexity collapses synchronously with canary metrics (unpredictable), while under lower contamination (α), collapse is more gradual and lead time extends to quality metrics. A predictability phase diagram defines boundaries.\n\n3. **Methodological Rigor**: Naive correlation analysis on non-stationary training metrics produces spurious regressions; Toda-Yamamoto panel temporal precedence provides statistically rigorous lead-lag quantification, with methodological ablation quantifying the percentage of false positive correlations.\n\n**Target Venue**: AAAI 2027 (primary) or EMNLP 2026 Findings (fallback)\n\n**Key Narrative Constraints**:\n- Cannot claim \"canary predicts model collapse\"—only \"diversity collapse\"\n- Must report that effective_rank and self_bleu fail as canary metrics\n- Perplexity channel breaks under 100% self-consuming conditions\n- Distinct_1/2 are reliable; distinct_3 less so"
      }
    ],
    "totalDurationMs": 18992,
    "totalTokens": 39622,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8645,
      "cache_read_input_tokens": 30064,
      "output_tokens": 906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8645
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 906,
          "cache_read_input_tokens": 30064,
          "cache_creation_input_tokens": 8645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8645,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 2,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have the citation keys. Let me also check if there's a more up-to-date paper_framing.md - the one found seems to be an older version (mentions AAAI 2027 as primary, EMNLP 2026 Findings as fallback). The task instructions already give me the complete framing constraints. Let me proceed with writing.

Let me also check for intervention-related citations since Claim 4 is about early intervention. Let me look for any related content.

Actually, I have enough context from the task instructions. Let me draft the introduction now.


I'm mapping out the structure carefully: five paragraphs following the contribution order of Claim 3, then 2, then 1, then 4, with a roadmap at the end. I need to stay around 1100 words while avoiding em-dashes, -ing phrase endings, and consecutive transition words. The key constraints are being precise about what the canary metric actually predicts (diversity collapse, not model collapse), using "regime map" terminology, and being careful not to overstate the causal claims around Granger precedence. The literature's claims about lead-lag relationships rest on single analytical approaches without proper statistical controls, which is fundamentally a multiverse problem where the same data produces contradictory conclusions depending on method choice. I need to identify four specific methodological gaps: lack of differencing, absence of multi-method comparison, missing multiple comparison correction, and no regime-specific analysis. The closest prior work has particular limitations I should highlight. My approach will systematically expose these pitfalls through multiverse-style analysis, propose a corrected method, and demonstrate it on token entropy as an early warning signal for diversity collapse. Then I'll structure the contributions in a specific order and wrap with a roadmap. Now let me write the actual paper.

Actually, I'm realizing the contribution list needs restructuring. The four items should be: systematic exposure of the three methodological pitfalls, regime-dependent detectability with the canary blind spot, token entropy as a one-generation-ahead canary, and canary-based early intervention. This means MMCT gets folded into the pitfalls contribution rather than standing alone, and cross-architecture generalization drops out as a standalone item, replaced by regime-dependent detectability and early intervention.

Now looking at the specifics of contribution 1, I'm seeing the concrete evidence: method choice inflates spurious signals to at least 62.5%, first-differencing completely eliminates the canary-perplexity associations, and the Granger test results flip dramatically across contamination levels. MMCT emerges as the resolution here—using FPR-inverse weighted consensus achieves perfect false positive rate and substantially better detection than simpler thresholding approaches. The Shapley decomposition shows naive cross-correlation is the main driver of false positives while permutation-based Granger testing suppresses them most effectively.

For contribution 2, I'm mapping out how detection depends on the regime: permutation Granger shows a sharp step function from complete failure at low alpha to perfect detection at alpha=1.0, while MMCT exhibits a more gradual dose-response curve. There's a notable blind spot for the canary at alpha=0.10, and detection becomes reliable only above alpha=0.25.

Contribution 3 focuses on the token entropy canary's behavior: at maximum contamination it achieves perfect forward detection across multiple architectures and seeds with zero reverse detections, but at intermediate contamination levels the performance degrades to transitional ranges, showing how the signal strength determines detectability across different model scales.

For contribution 4, I'm looking at early intervention—triggering one generation before peak collapse reduces perplexity degradation by 63% and accelerates recovery by two generations compared to reactive approaches, though I've only validated this at the highest contamination level so far.

Now I'm drafting the introduction and need to be precise with the numbers and claims. I'm planning to open with the core problem: model collapse from iterative training on synthetic data erodes diversity and calibration, which motivates developing canary metrics as early warning systems. Then I'll address the methodological gap in existing work—several recent studies have proposed canary approaches, but they haven't fully characterized when and how these metrics actually work. I'm reconsidering the structure—the brief mentions "5 段结构" with research background, problem importance, methodological gaps, core idea, and contributions. Looking at what I've outlined, I could potentially merge or split some sections, particularly combining problem importance with existing method limitations rather than treating them as separate paragraphs.

For the new version, I'm planning to reorganize into: research background covering model collapse and canary metrics, then problem importance and existing gaps together, followed by our core approach with the multiverse analysis and MMCT framework, and finally the contributions list with a roadmap. I need to keep the narrative story-driven rather than data-heavy in these opening paragraphs, saving specific numbers for the contributions section.

Now I'm drafting the first paragraph on the research background. The key is establishing how model collapse happens through iterative training on generated text, why it matters as a production concern, and how canary metrics could serve as early warning signals—drawing the parallel to ecological tipping points to motivate the approach.

The second paragraph shifts to the problem: recent work has proposed specific canary metrics like calibration error, spectral indicators, and sampling dynamics, but these studies haven't rigorously validated whether these metrics actually lead degradation or just correlate with it through confounding trends. The challenge is especially acute with short, noisy time series from iterative training, which makes standard statistical methods unreliable.

Now I'm identifying four concrete methodological gaps in how these analyses are conducted. The existing work skips differencing tests that would rule out spurious correlations from shared non-stationary trends, relies on single statistical methods without examining their assumptions, applies no correction for multiple comparisons across metric pairs, and doesn't account for how lead-lag relationships might vary across different training regimes.

The prior work by du et al. only examines one metric pair over a handful of generations using visual inspection rather than formal statistical testing. My approach is to conduct a multiverse-style analysis across different contamination levels in Pythia-410M to systematically test whether these lead-lag claims hold up under methodological scrutiny.

I'm proposing the Multi-Method Consensus Test as a way to validate that a relationship is genuinely robust—it has to show up consistently across different statistical approaches and random initializations, not just in one analysis. When I apply this framework, token entropy emerges as a reliable early warning signal for diversity collapse, and I can show that intervening based on this signal actually reduces the worst-case performance degradation.

Now I'm mapping out how the framework behaves across different parameter regimes, and I'm noticing something important: there's a blind spot around α=0.10 where diversity does collapse measurably, but the canary metrics don't actually diverge from the baseline noise, which means the detection threshold needs to be set higher to catch these cases reliably. I'm seeing that recent work has explored this direction—calibration error as an early signal, spectral indicators, and center-edge sampling dynamics all proposed as collapse detectors. Let me tighten that opening sentence though; it's running long and could be clearer if I split the thought about monitoring canary metrics from the analogy to ecological systems. Let me finish that sentence about DCES and then reconsider the structure. I'm thinking about how to allocate my word budget across the five paragraphs—background should be around 150 words, the problem statement another 130, then deficiencies, our approach, and the rest. The current paragraph is flowing well, so I'll keep it as one cohesive block rather than splitting it. Several recent studies have pursued this direction—calibration error rising before accuracy drops, spectral indicators of distributional shift, and center-edge sampling dynamics as collapse signals—but the statistical rigor behind these lead-lag claims remains largely unexamined. The core methodological gap is distinguishing whether a candidate canary truly precedes downstream degradation or merely correlates with it through shared non-stationary trends, a challenge compounded by the short, noisy time series typical of iterative training runs.

I'm identifying four critical methodological gaps in how existing analyses approach this problem: the absence of differencing tests to rule out spurious regression from co-trending series, reliance on a single statistical method without cross-validation of its assumptions, no correction for multiple comparisons when testing many metric pairs, and no regime-dependent analysis despite evidence that results flip at different contamination levels. The closest related work reports calibration error preceding accuracy degradation, but that analysis is limited to a single metric pair, spans only a few generations, and depends on visual inspection rather than rigorous statistical testing.

The early-warning framework from prior work provides theoretical grounding but hasn't been applied systematically to iterative training with the methodological rigor that short, noisy time series require. I should consolidate the citation strategy to avoid redundancy—keeping the boettiger reference in the earlier section on why short noisy time series are challenging, and using the scheffer citations here to anchor the theoretical motivation. or make them distinct enough:

P2: Why the methodology matters (the gap is important)
P3: Four specific deficiencies (the gap in detail)

Let me try:

% P2: Problem importance
Yet the statistical methodology underlying these lead-lag claims has received little scrutiny. Whether a candidate canary genuinely precedes downstream degradation, or merely correlates with it under shared non-stationary trends, remains unresolved. Iterative training produces short, noisy time series (often fewer than 15 points), where detection power is low and false positive rates can be high. Without proper methodological controls, claimed lead-lag relationships may be artifacts of co-trending rather than evidence of genuine temporal precedence. The early-warning framework from ecology provides theoretical motivation for canary-based prediction but hasn't been applied to iterative training collapse with the statistical rigor that short, non-stationary series demand.

% P3: Four specific deficiencies
I'm identifying four concrete gaps in how existing work analyzes lead-lag relationships during training collapse. No differencing tests rule out spurious regression from shared trends, conclusions rely on a single statistical method without examining its assumptions, no multiple comparison correction protects against false discoveries across many metric pairs, and no regime-dependent analysis accounts for how results might flip at different contamination levels. The closest related work shows calibration error rising before accuracy degrades, but doesn't address these methodological issues systematically.

% P4: Our approach
Now I'm moving to describe our solution: a multiverse-style analysis of canary prediction for diversity collapse, examining how lexical diversity degrades across training generations. I'm using Pythia-410M across six contamination levels and multiple random seeds, applying five different statistical methods to test whether observed lead-lag patterns hold up under different analytical choices.

The core contribution is the Multi-Method Consensus Test, a framework that weights results by false positive rate to identify robust findings across specifications. I'm demonstrating that token entropy serves as a reliable one-generation-ahead predictor of diversity collapse, and showing that intervening based on this signal reduces peak perplexity by 63% versus waiting for collapse to occur. I should note that Granger precedence here shows temporal predictive improvement rather than true causality, and the canary claim applies specifically to diversity metrics rather than model collapse more broadly. The PR-inverse weighting approach dramatically improves performance, achieving zero false positives and nearly 80% detection power—a ninefold gain over the standard method. Shapley decomposition pinpoints naive cross-correlation as the main source of false positives while identifying permutation Granger as the most effective corrective. Now I'm mapping out how detection performance varies across different regimes, though there's a particular blind spot when the canary signal is present. Token entropy emerges as a reliable one-generation-ahead canary for diversity collapse, with the consensus pipeline confirming strong directional asymmetry at α=1.0 across all methods and seeds—24/24 forward pairs show FDR significance while reverse pairs show none. This pattern replicates across GPT-2-medium and OPT-1.3B, though at α=0.75 the signal weakens to 19/24 forward with transitional consensus. The effect is specific to diversity metrics like distinct-n; the perplexity channel doesn't show the same signal. Now I'm moving toward the practical application of using canary metrics for early intervention. I'm checking the paper's actual section structure against what I referenced earlier—there's no intervention section in the roadmap, so I need to update that cross-reference to point to an existing section like the case study or experiments instead. I need to figure out which sections actually exist in the paper rather than guessing. The task specifies that contributions should reference the current structure, and I have the roadmap with established section labels, so I should stick with those. For the intervention claim, I'll use a reasonable section reference and let the paper be updated if needed.

Now I'm mapping out the contribution order more carefully—the task lists them as 1-4 but specifies they should follow the sequence Claim 3→2→1→4, so contribution 1 corresponds to Claim 3 (pitfalls), contribution 2 to Claim 2 (regime map), contribution 3 to Claim 1 (canary), and contribution 4 to Claim 4 (intervention).

I'm also catching some phrasing issues—I have an -ing phrase ending a sentence that needs fixing. Instead of "making careful methodological control essential," I should restructure it to avoid that pattern, maybe something like "careful methodological control becomes essential" or "methodological control must be careful."

Let me verify the citations I'm planning to use actually exist in the bibliography before finalizing. I've verified all the references are correct. Now I need to update the roadmap section to match the current structure—keeping the same format but ensuring the section references align with what's actually in the paper. The experiments section includes method sensitivity, regime-dependent detectability, case study, consensus validation, and cross-architecture generalization, so I'll make sure those subsection references are consistent throughout. I should be conservative with changes and only update what's necessary to reflect the actual document structure. I'm establishing the motivation for developing canary metrics—cheap computational signals that can warn of model collapse before expensive evaluations catch it. The parallel to ecological early-warning systems shows this isn't a new idea, and I'm citing recent work that's attempted this (calibration error, spectral indicators, sampling dynamics), but the key gap is that nobody's rigorously tested whether these metrics actually *precede* degradation or just correlate with it through shared trends. Now I'm noting that iterative training produces short, noisy time series, which makes statistical validation tricky.

I'm identifying four concrete methodological gaps in existing analyses: no differencing tests to rule out spurious regression, no cross-validation across multiple statistical methods, no correction for multiple comparisons, and no analysis of how conclusions shift across different contamination regimes. The closest prior work is the calibration-accuracy study, but it's incomplete. I'm realizing I need to restructure this more carefully—the five-paragraph framework requires separating the problem importance from the methodological gaps. Let me reorganize: background on model collapse and canary metrics as P1, then dedicate P2 to why this matters methodologically, P3 to the four specific deficiencies in existing work, P4 to our multiverse approach with the three pitfalls and intervention strategy, and P5 to the contributions with a roadmap. I'm debating whether to merge the importance and deficiencies sections since they're closely related—the gap matters precisely because these specific problems exist throughout the field. I could either combine them into one cohesive paragraph, or keep them separate with importance focusing on why the gap matters (short time series, false positives, real consequences) and deficiencies listing the specific technical problems. Let me just start writing naturally and see what flows best.

So I'm laying out the background: model collapse happens when language models train on their own output, causing lexical diversity to narrow, calibration to degrade, and biases to compound across generations. As machine-generated text proliferates online, this creates real risks for production systems, which is why researchers are hunting for cheap canary metrics—early warning signals that catch distributional degradation before it becomes catastrophic. This mirrors how ecologists use proxy indicators to predict critical transitions before systems tip. Recent work has made progress here: some studies show calibration errors rise before accuracy drops, others propose spectral indicators, and some use sampling dynamics as collapse signals.

But the statistical rigor behind these lead-lag claims hasn't been thoroughly examined. little scrutiny. Whether a candidate canary genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends, is a question that existing analyses leave unresolved. Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}. Without proper controls, the same data can yield conclusions that range from universal significance to complete null, depending entirely on the analyst's choice of statistical method. This makes the validity of existing canary claims an open question with practical consequences for monitoring deployed models.

I'm laying out four critical gaps in how these lead-lag analyses are currently conducted. First, existing work doesn't test for non-stationary confounds that could produce spurious correlations between co-trending metrics. Second, researchers rely on a single statistical approach without examining its assumptions or validating findings across multiple methods. Third, there's no correction for multiple comparisons when testing numerous metric pairs, leaving the work vulnerable to false discoveries. Fourth, no one checks whether the same test produces different results at different contamination levels. The most relevant prior work examined calibration error preceding accuracy loss but only across a handful of generations with visual inspection rather than formal statistics, while the broader early-warning literature provides theory but hasn't been adapted to this training context.

Now I'm describing our solution: a multiverse-style analysis across six contamination levels and multiple random seeds, applying five different statistical methods to expose these methodological pitfalls and propose a consensus framework that weights results by false positive rate. We identify token entropy as a robust one-generation-ahead predictor of diversity collapse and show that using it to trigger intervention reduces peak perplexity substantially compared to waiting for actual collapse. I'm being careful to scope the claims—Granger precedence here establishes temporal prediction, not causality, and the canary finding applies specifically to diversity metrics rather than model collapse broadly.

To our knowledge, this is the first multiverse-style analysis examining lead-lag relationships in model collapse. Our key contributions include systematically exposing three methodological pitfalls—method sensitivity, spurious regression, and regime dependence—and proposing a consensus resolution. The data shows that method choice alone drives spurious signal rates up to at least 62.5%, with the five methods producing false discovery rates ranging from 25% to 100% and very low inter-method agreement. First-differencing the data eliminates the apparent canary-to-perplexity relationship entirely, revealing it as an artifact of co-trending rather than a genuine predictive signal.

We introduce the Multi-Method Consensus Test to address these issues, which uses pair-level false positive rate weighting and achieves 79.2% detection power at α=0.75—a 9.5× improvement over the naive uniform threshold approach. Shapley value decomposition pinpoints naive cross-correlation as the primary driver of false positives while identifying permutation Granger as the strongest corrective method. Our regime analysis across eight contamination levels reveals that permutation Granger exhibits a sharp threshold behavior, jumping from zero detections below α=0.25 to perfect detection at α=1.0, whereas our consensus method shows a more gradual dose-response curve.

A critical finding emerges at α=0.10: diversity metrics show measurable collapse (distinct-1 drops nearly 40%), yet the canary metrics remain statistically indistinguishable from baseline conditions, revealing a detection blind spot that establishes α≥0.25 as a practical lower bound for reliable identification. Token entropy emerges as an effective early warning signal for diversity collapse, with the full pipeline confirming strong directional asymmetry at α=1.0—all 24 forward-direction pairs show FDR significance while reverse pairs show none, consistently across multiple methods and random seeds. This directional effect replicates across different model architectures including GPT-2-medium.

At lower thresholds like α=0.75, the pattern holds with 19 of 24 forward pairs significant and zero reverse pairs, though with weaker consensus. The effect is specific to diversity metrics; the perplexity channel doesn't show the same predictive relationship. When applied to intervention, triggering on token entropy drops outperforms waiting for diversity collapse—the entropy-based trigger fires a generation earlier, cuts peak perplexity by 63%, and achieves full recovery two generations faster, validated at α=1.0.

The paper then outlines its structure: covering related work on model collapse and early-warning signals, establishing the formal framework and five detection methods, presenting the diagnostic approach and consensus pipeline, and reporting full experimental results including sensitivity analysis, regime-dependent detectability, and validation of the consensus framework.

Let me tally up the word counts more carefully to see if I'm hitting the target length.

I'm looking at the contributions section and roadmap, which come to about 405 words combined, and my current draft is sitting around 960 words total. I need roughly 140 more words to reach 1100, so I should expand the background section and add more detail to how my approach works, particularly around the regime map and identifying blind spots.

For the background, I can elaborate on what happens when models train on their own outputs—how the training distribution loses diversity, calibration suffers, and biases compound across generations. For the approach section, I want to give readers a clearer picture of the regime map framework and how it helps us spot failure modes. We address these gaps through a multiverse-style analysis of canary metrics for diversity collapse, examining how lexical diversity degrades across training generations. I'm testing this on Pythia-410M with varying contamination levels and multiple random seeds, applying five different statistical methods to uncover three key methodological issues: sensitivity to method choice, spurious correlations, and dependence on the regime. I'm proposing the Multi-Method Consensus Test as a formal framework that weights methods by their false positive rates, drawing inspiration from specification curve analysis. The analysis reveals a critical blind spot at low contamination levels where diversity has already collapsed but the canary metrics haven't yet signaled the problem.

I'm finding that token entropy emerges as a reliable one-step-ahead indicator of diversity collapse, and using it to trigger interventions cuts peak perplexity by 63% compared to waiting for the problem to manifest. The Granger causality tests show temporal precedence rather than true causality, so I'm being careful to scope the canary claim specifically to diversity metrics rather than claiming it predicts broader model collapse. What's striking is that this multiverse approach—same data, five methods, six regimes—produces conclusions ranging from universal significance to complete null, highlighting how fragile these lead-lag claims can be.

The statistical foundations here are surprisingly weak. Whether a candidate canary truly precedes degradation or just correlates through shared non-stationary trends remains unclear in the literature. Iterative training gives us short, noisy time series with often fewer than 15 points per sequence, which tanks detection power and inflates false positives. The same dataset analyzed under different methodological choices yields wildly divergent conclusions, which raises serious questions about the reliability of existing canary approaches for practical monitoring systems.

I'm identifying four core problems in how lead-lag analyses handle iterative training collapse: no differencing tests to rule out spurious regression from co-trending series, and several other methodological gaps that compound the issue.

The closest related work examines calibration error preceding accuracy loss in language models, but only across a single metric pair over 1-3 generations with visual comparisons rather than formal statistical tests. The early-warning framework exists theoretically but hasn't been rigorously applied to the constraints of short, non-stationary training sequences. I'm recounting the word distribution across sections to verify we're in the right ballpark. Let me work through P1 systematically—the opening sentences about model collapse and its mechanisms are running around 20-22 words each, and I need to see where the total lands before deciding if any adjustments are necessary.

The parallel to ecological tipping points and the existing canary metric proposals—calibration error, spectral indicators, center-edge sampling—give me concrete examples to anchor the discussion. But I'm noticing that the statistical rigor behind these lead-lag claims hasn't been thoroughly examined, and the core tension is whether these metrics actually precede degradation or just move in tandem with it under broader non-stationary shifts. The challenge is that iterative training produces sparse, noisy time series that make causal inference difficult.

Now I'm laying out the methodological gaps that undermine confidence in existing analyses. The core issues are the lack of differencing tests to rule out spurious correlation from shared trends, reliance on a single statistical method without cross-validation, absence of multiple comparison correction when screening many metric pairs, and no consideration of whether the lead-lag relationship holds across different training regimes.

The most relevant prior work shows that calibration error can precede accuracy loss in language models, but that analysis only examined one metric pair over a handful of generations and used visual inspection rather than formal statistical testing. There's theoretical grounding for early-warning frameworks, though they haven't been applied to training collapse with the methodological care that short, noisy time series require.

To address these gaps, I'm designing a multiverse-style analysis that tests whether diversity collapse—the progressive decline in lexical variety across training—can be predicted by canary metrics. I'm using Pythia-410M across multiple contamination levels and random seeds, applying five different statistical methods to systematically expose method sensitivity, spurious correlations, and other pitfalls.

I'm proposing the Multi-Method Consensus Test, a formal framework that weights results by false positive rate and draws inspiration from specification curve analysis. The analysis reveals a critical blind spot at alpha=0.10 where diversity has already collapsed but canary metrics show nothing, establishing that detection requires alpha≥0.25. Token entropy emerges as a reliable one-step-ahead predictor, and using it to trigger intervention reduces peak perplexity by 63% versus waiting for collapse. I'm being careful to frame this as temporal precedence rather than causality, and the canary claim applies specifically to diversity metrics, not model collapse in general. What makes this novel is that the same dataset analyzed five different ways across six regimes produces conclusions ranging from universal significance to complete null—the first multiverse analysis of this kind for model collapse prediction. I'm working through the word count carefully—accounting for LaTeX commands that don't actually count toward the total, I'm sitting around 1028 words. I could expand P1 with a sentence about the importance of distinguishing genuine early-warning signals from statistical artifacts, which would add about 25 words and bring me closer to 1050. I could also add a transition between P3 and P4 about cross-architecture validation confirming these findings transfer beyond the primary platform, though I need to avoid duplicating the similar point already at the end of P4. Let me add both expansions to get the piece to a solid length.

Actually, I'm overthinking the exact word count—anywhere in the 1000-1100 range works fine for this target. Let me just finalize the version and do a quick style check rather than continuing to optimize incrementally. I'm verifying the LaTeX conventions are correct—the double-hyphen in "Benjamini--Hochberg" and number ranges like "1--3" follow standard LaTeX formatting. I've also checked that percentage ranges use "from...to" phrasing rather than dashes, which keeps things consistent. Now I'm ready to write out the final version.

Actually, let me reconsider the overall structure. The outline calls for separating the problem's importance from the specific methodological deficiencies—P2 should establish why this gap matters (short time series, inconsistent conclusions from the same data), while P3 should detail what's actually wrong with existing approaches. My current draft already maps correctly to this distinction, so I'm on track.

Now I need to finalize the LaTeX version and make sure the five-part structure flows logically from motivation through contributions and into the roadmap. I'm deciding between \citeauthor and \citet for the citations—I'll stick with \citet since that's what the current intro uses. Scanning through for overuse of "we"—I have "We identify," "We address," "We then identify," "We note," plus "Our contributions" appearing a couple times, which feels balanced for academic writing. One thing I want to refine: the claim about being the first multiverse-style analysis of lead-lag claims in model collapse. I've positioned it at the end of P4, describing how the same dataset analyzed across five statistical methods and six contamination regimes produces conclusions spanning the full spectrum, which captures the novelty more naturally than the original phrasing.

Let me verify I'm respecting the key constraints: I'm careful never to claim the canary predicts model collapse itself—only diversity collapse. I use "regime map" consistently rather than "phase diagram." I've included the caveat that Granger precedence isn't true causality. And I'm working with a single dataset across multiple analytical approaches, which is the core of the multiverse framing.

Now I need to finalize the document structure. Let me cross-check the section references in the introduction against what I'm actually building—making sure the roadmap aligns with the labeled sections I'll have in the paper.

I'm adding \S\ref{sec:intervention} to the experiments subsections and will reference it in contribution 4. For the other contributions, I'll anchor them to their corresponding sections: contribution 1 ties to the method and sensitivity analysis, contribution 2 to the regime analysis, contribution 3 to the case studies and generalization results, and contribution 4 to the intervention section.

I'm also refining the language in P2's final sentence to be more concrete—replacing "practical consequences" with something that directly speaks to practitioners who use these signals to decide when to intervene in training. And I want to verify that the claim in P1 about progressive collapse is well-supported by the early warning signals framework, which it is. Now I'm ready to write out the final version.

Before I do, I need to double-check that all the specific numbers in the contribution list match exactly what the task specifies, so I'm going through each metric one by one to confirm they're accurate. I'm seeing the validation results continue across different experimental conditions—at full intervention strength, all 24 forward detections hold while reverse cases stay at zero, and this pattern shifts to 19/24 forward at the intermediate setting with transitional behavior between tiers. The scope is specifically on diversity metrics rather than broader model collapse signals. For the intervention strategies, the predictive approach using token entropy triggers one generation earlier and achieves substantially lower peak perplexity compared to the reactive method. I need to reconcile the phrasing from the task spec with what the data actually shows. The "at least 62.5%" claim about spurious-signal rate inflation should be presented alongside the full range of 25% to 100% across methods, since both pieces capture important aspects of the finding—the breadth of variation and the typical magnitude of the problem. I'm noticing the apparent tension between "at least 62.5%" and the range going down to 25%—but I think the task spec is distinguishing between the false positive rate on built-in null pairs versus the full range across methods, so I'll stick with the exact wording. Now I need to finalize the document and make sure I'm not ending any clauses with present participle phrases, which the constraint explicitly forbids.

Writing the LaTeX introduction section... collapse. The concept parallels early-warning signals for critical transitions in ecological systems, where proxy indicators allow intervention before a tipping point. Several recent studies have pursued this direction, observing that calibration error rises before accuracy degrades, proposing spectral indicators, and using center-edge sampling dynamics as collapse signals.

Yet the statistical methodology underlying these lead-lag claims has received little scrutiny. Whether a candidate canary genuinely precedes downstream degradation, or merely correlates with it under shared non-stationary trends, remains unresolved. Iterative training produces short, noisy time series—often fewer than 15 points per generation sequence—where detection power drops sharply and false positive rates can be high. The same data can yield wildly different conclusions depending on which statistical method the analyst chooses, making the validity of existing canary claims an open question with real consequences for practitioners relying on these signals to trigger interventions.

I'm identifying four key methodological gaps in how existing analyses approach lead-lag relationships during iterative training collapse: the absence of differencing tests to rule out spurious regression from co-trending time series, reliance on a single statistical method without examining its assumptions or conducting cross-validation, lack of multiple comparison correction when testing many metric pairs, and no regime-dependent analysis despite the possibility that results could flip at different contamination levels.

The closest prior work examined calibration error rising before accuracy degrades across a single metric pair over just a few generations using only visual comparisons, while the broader early-warning framework from ecological systems provides theoretical grounding but hasn't been applied to training collapse with the statistical rigor that short, non-stationary time series require. I'm addressing these gaps through a multiverse-style analysis of whether diversity collapse—the progressive loss of lexical diversity across training generations—can serve as a canary signal, testing this across multiple contamination levels and random seeds using five different statistical methods to expose how conclusions shift with methodological choices.

I'm identifying three key pitfalls: method sensitivity, spurious regression, and regime dependence. I'm proposing the Multi-Method Consensus Test as a formal framework that weights methods by their false positive rates, inspired by specification curve analysis. An expanded regime map reveals a critical blind spot where diversity has already measurably collapsed at low contamination levels but canary metrics still show null signals. Token entropy emerges as a reliable one-generation-ahead predictor, and using it to trigger intervention reduces peak perplexity substantially and accelerates recovery compared to waiting for collapse to occur. The Granger precedence analysis establishes temporal predictive ordering rather than true causal mechanisms.

Now I'm clarifying that this canary finding is specific to diversity metrics, not model collapse in general. This appears to be the first multiverse-style analysis of lead-lag relationships in model collapse—the same data analyzed across five different methods and six contamination regimes produces conclusions ranging from universal significance to complete null results. My main contributions are exposing these three methodological pitfalls and offering a consensus resolution through the MMCT framework. Method selection alone drives spurious signal rates above 60%, with the five approaches yielding significance rates spanning from 25% to 100% and minimal inter-method agreement. When I apply first-differencing, the canary-to-perplexity relationship vanishes entirely.

The Granger test demonstrates this instability dramatically—it shifts from finding all 24 pairs significant to finding zero significant pairs across different contamination levels. My proposed MMCT approach with pair-level FPR-inverse weighting achieves zero false positive rate and 79.2% detection power at α=0.75, representing a 9.5-fold improvement over the standard uniform threshold. Through Shapley-value decomposition across all possible coalitions, I've identified naive cross-correlation as the primary driver of false positives while permutation Granger emerges as the strongest suppressor of spurious findings.

Now examining how detection performance varies across different regime conditions, I'm mapping out an eight-point regime landscape that reveals permutation Granger exhibits a sharp threshold behavior—completely failing to detect anything until α reaches 1.0, then suddenly detecting all 24 pairs. In contrast, MMCT shows a smooth, dose-dependent response curve that gradually improves detection rates as the parameter increases.

There's a critical blind spot at α=0.10 where diversity has already substantially degraded but the canary metrics haven't diverged enough from baseline to signal the problem—entropy shifts by less than a percentage point despite distinct-1 dropping nearly 40%. This suggests reliable detection requires α≥0.25 as a practical threshold.

Moving to the full consensus pipeline at α=1.0, I'm seeing strong directional asymmetry: all 24 forward-direction pairs show FDR-significant relationships while zero reverse pairs do, consistently across four different methods and random seeds. The pattern holds up when I replicate across different model architectures like GPT-2-medium.

At the intermediate α=0.75 level, I get 19 out of 24forward pairs and zero reverse with permutation Granger causality, though the consensus tier drops to 2-3, suggesting this is where the signal starts becoming less robust. Importantly, this directional relationship only holds for diversity metrics like distinct-n; the perplexity channel doesn't show the same pattern.

For the practical intervention angle, I'm comparing two trigger strategies: one based on token entropy dropping more than 15% versus one based on distinct-1 dropping more than 10%. The entropy-based trigger fires a generation earlier, cuts peak perplexity roughly in half, and gets the model back to normal performance two generations faster than waiting for the diversity collapse signal.

The validation holds at α=1.0 across different seeds and precision settings, and the paper then moves into its roadmap—covering related work on model collapse and early-warning signals, the formal setup and detection methods, the diagnostic framework with consensus validation, and the full experimental results including sensitivity analysis and regime-dependent detectability. Checking for style consistency across the paper—making sure em-dashes, en-dashes, and sentence endings follow the right conventions. Going through each conclusion to verify none awkwardly end with -ing phrases, and confirming that LaTeX number ranges and name compounds use the standard `--` notation rather than explanatory dashes. I'm realizing the -ing phrase "exposing them as artifacts of co-trending" actually does end the sentence, so I need to restructure this to avoid the pattern I've been checking for. Let me rephrase it more directly: after first-differencing eliminates the association entirely, I can simply state that these are artifacts of co-trending rather than genuine temporal relationships. I'm working through the phrasing in the contributions section, checking each statement for dangling participles. The second contribution uses "with entropy differing by less than one percentage point," which is an absolute phrase rather than a dangling participial construction, so it's technically acceptable—but I could tighten it by rephrasing to "with entropy less than one percentage point from the baseline" to be more direct.

I've identified two spots that need revision: the first contribution's "exposing them as artifacts of co-trending" and the second's entropy phrasing. I'm also scanning the rest of the text for similar -ing patterns, particularly "depending entirely on the analyst's choice," which does read as a dangling participial phrase at the end of that sentence about statistical method selection.

I can reframe that as either a semicolon split or by making the analyst's choice the active subject—the second approach feels stronger since it puts agency front and center. Let me also verify the other -ing constructions: "Using Pythia-410M" is fine as a sentence opener, "training generations" isn't a participial phrase, and "followed by" is past participle so that's acceptable. So I've got three fixes to make: the "depending" clause, the C1 artifact phrasing, and the C2 entropy wording.

For P2, I'll go with "In the absence of proper controls, the choice of statistical method alone can shift conclusions on the same data from universal significance to complete null"—that keeps the emphasis on method choice driving the outcome without relying on -ing. Now I need to tackle C1 and C2 the same way.

For C1, first-differencing strips away the canary-to-perplexity relationship entirely (F approaches zero, p equals 0.99), revealing they're artifacts of shared trends rather than real temporal precedence.

For C2, at the 0.10 significance level, a blind spot appears: diversity has already tanked (distinct-1 drops nearly 40 percent) while canary metrics stay statistically indistinguishable from baseline (entropy shifts by less than a percentage point).

Now scanning the full text for -ing word endings. P1 looks clean—"training distribution," "training collapse," "training pipelines," "leading indicators," and "early-warning signals" are all compound nouns or adjectives, not problematic -ing constructions.

P2 also checks out: "underlying" and "existing analyses" are adjectives, "training produces" is a verb phrase, and "null-calibrated testing" is a compound noun.

P3 has "differencing tests" and "co-trending time series" as compounds, but there's an -ing phrase at the sentence end: "when correlating co-trending time series" closes out the statement about spurious regression hazards.

The issue is whether this adverbial -ing clause counts as the prohibited pattern. It's not a dangling participial phrase modifying the subject, but to stay consistent with the style guide, I should reframe it. Something like "...a well-documented hazard in analyses of co-trending time series" removes the -ing entirely and tightens the phrasing.

Similarly, "when testing many metric pairs simultaneously" in the multiple comparison section follows the same structure. I could reshape it to "...guards against false discoveries in multi-pair testing" or "...guards against false discoveries among many simultaneously tested metric pairs."

Actually, the cleanest version might be: "Multiple comparison correction (e.g., Benjamini–Hochberg FDR control) is absent, leaving false discoveries unchecked when many metric pairs are tested simultaneously." That keeps the passive voice acceptable for academic writing while avoiding the dangling -ing construction. I'm checking whether "when correlating" and "when testing" violate the prohibition on -ing endings. The rule specifically targets comma + -ing patterns like ", demonstrating" or ", highlighting", and the grep check looks for "ing," — neither of which matches my constructions since they're introduced by "when" rather than a comma. These are standard academic structures, so I'll keep them as-is. Let me verify my earlier fixes: P2 avoids the -ing ending cleanly, and C1 is on track with the first-differencing revision. I've verified the grammar throughout the text—checking for problematic "-ing" endings and comma patterns. The fixes look solid: "co-trending" works as a gerund noun, and all the other clause endings use proper nouns or verbs rather than participles. No lingering comma-plus-"-ing" issues remain.

Now I'm reconsidering the Shapley notation in the introduction. The subscript format with proper mathematical formatting looks cleaner than the parenthetical version, so I'll standardize on that approach for consistency across the document. I'm settling on the inline text and math mode format that matches the paper's existing convention—keeping "Shapley(FPR)" in text and the equation in math mode, then applying the same pattern to both the FPR driver and the suppressor terms. I should add a citation for Pythia-410M since we're introducing it as our main experimental model, and it's already in the bibliography. Now let me verify the paragraph transitions flow smoothly—the first paragraph leads into the second with a clear "Yet" to signal the shift from recent work to methodological gaps, and the third paragraph moves naturally from general importance to our specific contributions. I'm checking whether FDR needs to be defined—it appears in the text but I should verify if it's introduced with a full explanation earlier. The current writing mentions "FDR significance" but I need to confirm the definition is present where it's first used. I need to define FDR on first use in the Introduction since that's the requirement. Let me revise P3 to spell out "false discovery rate" with the acronym, then reference the Benjamini-Hochberg method as an example. The phrasing should be concise to avoid redundancy with "false discoveries" later in the sentence. I'm working through how to introduce FDR correction cleanly without overexplaining it. The simplest approach is to define FDR on first use and mention Benjamini--Hochberg as an example, keeping the sentence focused on the main point that no such correction is applied.

Now I'm double-checking that MMCT is properly introduced earlier in the document—it gets expanded on first use in P4, so later references don't need re-expansion. I'm also verifying the task description captures the key performance metrics accurately, particularly the FPR-inverse weighting and detection rates.

Let me finalize the phrasing for C4 around the intervention triggers, making sure I distinguish between the predictive token_entropy condition and the reactive distinct_1 condition with their respective thresholds.

Time to write out the complete file cleanly with all corrections incorporated. I'm finalizing the wording for the intervention section—keeping the prose clean and avoiding unnecessary math notation while making sure the trigger conditions are clear. Now I need to check that P3 isn't just repeating the same critique about time series rigor that I already made in P2. I need to verify I've addressed the style constraint about em-dashes and -ing phrase endings. The "exposing" construction I caught earlier—a comma followed by a present participle at the sentence end—is exactly what's prohibited, and I've already fixed it. Let me scan the rest of the text to make sure there are no other violations like that, then I'm ready to write out the final version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "b3a25906-62b5-4ad1-a88d-b194ef7d4611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169iBhGqrjDLarsU1chv1iK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 40440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 31_

Now I have all the context. Let me write the new introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "4711b0e7-3822-4c63-850f-07c9fce2cbc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169iBhGqrjDLarsU1chv1iK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 40440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 32_

<details open><summary>🔧 Tool call — Write · `toolu_015JhRH5XvetrgsrvQr3pJNo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\\cite{shumailov2024curse,alemohammad2024mad}.\nLexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.\nAs machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.\nBy the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.\nThis threat motivates the search for cheap-to-compute \\emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.\nThe concept parallels early-warning signals for critical transitions in ecological systems~\\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} observe that calibration error rises before accuracy degrades, SIGMA~\\cite{sigma2026spectral} proposes spectral indicators, and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\n\nYet the statistical methodology underlying these lead-lag claims has received little scrutiny.\nWhether a candidate canary genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends, is a question that existing analyses leave unresolved.\nIterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\\cite{boettiger2012limits}.\nIn the absence of proper controls, the choice of statistical method alone can shift conclusions on the same data from universal significance to complete null.\nThis makes the validity of existing canary claims an open question with direct consequences for practitioners who rely on such signals to trigger training interventions.\n\nWe identify four specific deficiencies that pervade existing lead-lag analyses of iterative training collapse.\n(1)~No differencing tests rule out spurious regression from shared non-stationary trends, a well-documented hazard in analyses of co-trending time series~\\cite{granger1974spurious}.\n(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined; no multi-method cross-validation is conducted.\n(3)~No false discovery rate (FDR) correction (e.g., Benjamini--Hochberg) guards against spurious findings when testing many metric pairs simultaneously.\n(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who report that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, covers a single metric pair, spans only 1--3 generations, and relies on visual comparisons without statistical tests.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating} provides theoretical motivation but has not been applied to training collapse with the rigor that such short, non-stationary series require.\n\nWe address these gaps through a multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of canary prediction of diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\\cite{li2016diversity}) across training generations.\nUsing Pythia-410M~\\cite{biderman2023pythia} across six contamination levels ($\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we apply five statistical methods to expose three methodological pitfalls (method sensitivity, spurious regression, and regime dependence) and propose the Multi-Method Consensus Test (MMCT), a formal FPR-inverse-weighted consensus framework inspired by specification curve analysis~\\cite{simonsohn2020specification}.\nAn extended eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals a canary blind spot: at $\\alpha{=}0.10$, diversity has already collapsed measurably but canary metrics remain at null levels, which places a detection lower bound at $\\alpha{\\geq}0.25$.\nWe identify token entropy as a robust one-generation-ahead canary for diversity collapse and demonstrate that canary-triggered predictive intervention reduces peak perplexity by 63\\% and accelerates recovery by two generations compared to reactive approaches.\nCross-architecture validation on GPT-2-medium and OPT-1.3B confirms that these findings transfer beyond the primary experimental platform.\nGranger precedence in our framework establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics, not model collapse broadly.\nTo our knowledge, this constitutes the first multiverse-style analysis of lead-lag claims in model collapse: the same dataset, analyzed with five methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls and a consensus resolution} (\\S\\ref{sec:method}, \\S\\ref{sec:method_sensitivity}).\n    Method choice alone inflates spurious-signal rates to at least 62.5\\%, with five methods yielding FDR significance rates from 25\\% to 100\\% and inter-method agreement of $\\kappa{=}0.185$.\n    First-differencing eliminates canary$\\to$perplexity associations entirely ($F{\\approx}0$, $p{=}0.99$); they are artifacts of co-trending, not genuine temporal precedence.\n    The same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    To resolve these pitfalls, we propose MMCT: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing, while MMCT's pair-level FPR-inverse weighting achieves FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$, a $9.5{\\times}$ improvement over the uniform threshold's 8.3\\%.\n    Shapley-value decomposition (exact 32-coalition enumeration) identifies naive cross-correlation as the sole FPR driver (Shapley(FPR)${=}{+}0.348$) and permutation Granger as the strongest suppressor (Shapley(FPR)${=}{-}0.194$).\n\n    \\item \\textbf{Regime-dependent detectability with a canary blind spot} (\\S\\ref{sec:regime}).\n    An eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals that permutation Granger follows a step function (0/24 at $\\alpha{\\leq}0.25$, 24/24 at $\\alpha{=}1.0$), while MMCT exhibits gradual dose-response (43.8\\%$\\to$58.3\\%$\\to$79.2\\% detection at $\\alpha{=}0.25/0.50/0.75$).\n    At $\\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed (distinct-1 drops 39.6\\%) but canary metrics remain indistinguishable from the null condition (entropy differs by less than one percentage point).\n    These results place a lower bound on reliable detection at $\\alpha{\\geq}0.25$.\n\n    \\item \\textbf{Token entropy as a one-generation-ahead canary for diversity collapse} (\\S\\ref{sec:case_study}, \\S\\ref{sec:generalization}).\n    At $\\alpha{=}1.0$, the full consensus pipeline confirms directional asymmetry: 24/24 forward-direction pairs are FDR-significant and 0/24 in the reverse direction, across four methods and four seeds.\n    Cross-architecture replication on GPT-2-medium and OPT-1.3B confirms the pattern.\n    At $\\alpha{=}0.75$, three-seed replication yields 19/24 forward and 0/24 reverse (permutation Granger), with transitional consensus (Tier~2--3).\n    This claim is scoped to diversity metrics (distinct-$n$); the perplexity channel is spurious.\n\n    \\item \\textbf{Canary-based early intervention} (\\S\\ref{sec:intervention}).\n    As a practical demonstration, we compare predictive intervention (triggered when token entropy drops ${>}15\\%$) against reactive intervention (triggered when distinct-1 drops ${>}10\\%$).\n    The predictive trigger fires one generation earlier, reduces peak perplexity by 63\\% (56.99 vs.\\ 157.09), and achieves full recovery two generations faster (Generation~2 vs.\\ Generation~4).\n    This result is validated at $\\alpha{=}1.0$ across two seeds (s42 fp32, s43 bf16).\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), canary prediction of diversity collapse (\\S\\ref{sec:case_study}), consensus framework validation (\\S\\ref{sec:consensus_validation}), cross-architecture generalization (\\S\\ref{sec:generalization}), and canary-based early intervention (\\S\\ref{sec:intervention}).\n\\S\\ref{sec:discussion} discusses implications and future directions, and \\S\\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\\S\\ref{sec:limitations}).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "de34fd6d-2798-4e38-96c4-e6a9b7a365b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169iBhGqrjDLarsU1chv1iK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 40440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 33 · 2026-05-19T04:38:59.751Z_

<details><summary>↩ Tool result · `toolu_015JhRH5XvetrgsrvQr3pJNo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "132cb541-e329-4793-abb4-e860f27f9c4d",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\\cite{shumailov2024curse,alemohammad2024mad}.\nLexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.\nAs machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.\nBy the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.\nThis threat motivates the search for cheap-to-compute \\emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.\nThe concept parallels early-warning signals for critical transitions in ecological systems~\\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} observe that calibration error rises before accuracy degrades, SIGMA~\\cite{sigma2026spectral} proposes spectral indicators, and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\n\nYet the statistical methodology underlying these lead-lag claims has received little scrutiny.\nWhether a candidate canary genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends, is a question that existing analyses leave unresolved.\nIterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\\cite{boettiger2012limits}.\nIn the absence of proper controls, the choice of statistical method alone can shift conclusions on the same data from universal significance to complete null.\nThis makes the validity of existing canary claims an open question with direct consequences for practitioners who rely on such signals to trigger training interventions.\n\nWe identify four specific deficiencies that pervade existing lead-lag analyses of iterative training collapse.\n(1)~No differencing tests rule out spurious regression from shared non-stationary trends, a well-documented hazard in analyses of co-trending time series~\\cite{granger1974spurious}.\n(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined; no multi-method cross-validation is conducted.\n(3)~No false discovery rate (FDR) correction (e.g., Benjamini--Hochberg) guards against spurious findings when testing many metric pairs simultaneously.\n(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who report that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, covers a single metric pair, spans only 1--3 generations, and relies on visual comparisons without statistical tests.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating} provides theoretical motivation but has not been applied to training collapse with the rigor that such short, non-stationary series require.\n\nWe address these gaps through a multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of canary prediction of diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\\cite{li2016diversity}) across training generations.\nUsing Pythia-410M~\\cite{biderman2023pythia} across six contamination levels ($\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we apply five statistical methods to expose three methodological pitfalls (method sensitivity, spurious regression, and regime dependence) and propose the Multi-Method Consensus Test (MMCT), a formal FPR-inverse-weighted consensus framework inspired by specification curve analysis~\\cite{simonsohn2020specification}.\nAn extended eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals a canary blind spot: at $\\alpha{=}0.10$, diversity has already collapsed measurably but canary metrics remain at null levels, which places a detection lower bound at $\\alpha{\\geq}0.25$.\nWe identify token entropy as a robust one-generation-ahead canary for diversity collapse and demonstrate that canary-triggered predictive intervention reduces peak perplexity by 63\\% and accelerates recovery by two generations compared to reactive approaches.\nCross-architecture validation on GPT-2-medium and OPT-1.3B confirms that these findings transfer beyond the primary experimental platform.\nGranger precedence in our framework establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics, not model collapse broadly.\nTo our knowledge, this constitutes the first multiverse-style analysis of lead-lag claims in model collapse: the same dataset, analyzed with five methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls and a consensus resolution} (\\S\\ref{sec:method}, \\S\\ref{sec:method_sensitivity}).\n    Method choice alone inflates spurious-signal rates to at least 62.5\\%, with five methods yielding FDR significance rates from 25\\% to 100\\% and inter-method agreement of $\\kappa{=}0.185$.\n    First-differencing eliminates canary$\\to$perplexity associations entirely ($F{\\approx}0$, $p{=}0.99$); they are artifacts of co-trending, not genuine temporal precedence.\n    The same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    To resolve these pitfalls, we propose MMCT: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing, while MMCT's pair-level FPR-inverse weighting achieves FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$, a $9.5{\\times}$ improvement over the uniform threshold's 8.3\\%.\n    Shapley-value decomposition (exact 32-coalition enumeration) identifies naive cross-correlation as the sole FPR driver (Shapley(FPR)${=}{+}0.348$) and permutation Granger as the strongest suppressor (Shapley(FPR)${=}{-}0.194$).\n\n    \\item \\textbf{Regime-dependent detectability with a canary blind spot} (\\S\\ref{sec:regime}).\n    An eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals that permutation Granger follows a step function (0/24 at $\\alpha{\\leq}0.25$, 24/24 at $\\alpha{=}1.0$), while MMCT exhibits gradual dose-response (43.8\\%$\\to$58.3\\%$\\to$79.2\\% detection at $\\alpha{=}0.25/0.50/0.75$).\n    At $\\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed (distinct-1 drops 39.6\\%) but canary metrics remain indistinguishable from the null condition (entropy differs by less than one percentage point).\n    These results place a lower bound on reliable detection at $\\alpha{\\geq}0.25$.\n\n    \\item \\textbf{Token entropy as a one-generation-ahead canary for diversity collapse} (\\S\\ref{sec:case_study}, \\S\\ref{sec:generalization}).\n    At $\\alpha{=}1.0$, the full consensus pipeline confirms directional asymmetry: 24/24 forward-direction pairs are FDR-significant and 0/24 in the reverse direction, across four methods and four seeds.\n    Cross-architecture replication on GPT-2-medium and OPT-1.3B confirms the pattern.\n    At $\\alpha{=}0.75$, three-seed replication yields 19/24 forward and 0/24 reverse (permutation Granger), with transitional consensus (Tier~2--3).\n    This claim is scoped to diversity metrics (distinct-$n$); the perplexity channel is spurious.\n\n    \\item \\textbf{Canary-based early intervention} (\\S\\ref{sec:intervention}).\n    As a practical demonstration, we compare predictive intervention (triggered when token entropy drops ${>}15\\%$) against reactive intervention (triggered when distinct-1 drops ${>}10\\%$).\n    The predictive trigger fires one generation earlier, reduces peak perplexity by 63\\% (56.99 vs.\\ 157.09), and achieves full recovery two generations faster (Generation~2 vs.\\ Generation~4).\n    This result is validated at $\\alpha{=}1.0$ across two seeds (s42 fp32, s43 bf16).\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), canary prediction of diversity collapse (\\S\\ref{sec:case_study}), consensus framework validation (\\S\\ref{sec:consensus_validation}), cross-architecture generalization (\\S\\ref{sec:generalization}), and canary-based early intervention (\\S\\ref{sec:intervention}).\n\\S\\ref{sec:discussion} discusses implications and future directions, and \\S\\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\\S\\ref{sec:limitations}).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 59,
        "newStart": 1,
        "newLines": 66,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:introduction}",
          " ",
          "-Practitioners monitoring iterative training pipelines face a diagnostic blind spot: the metrics most commonly used to detect distributional degradation can yield false positive rates of 62.5--100\\% when applied without proper statistical controls, yet no established protocol exists for distinguishing genuine early-warning signals from artifacts of shared non-stationary trends.",
          "-This blind spot is consequential because iterative training collapse, where models are unwittingly trained on output from earlier generations, is increasingly likely as machine-generated text proliferates on the web~\\cite{shumailov2024curse,alemohammad2024mad}.",
          "-Tail modes vanish, lexical diversity narrows, and calibration deteriorates across generations.",
          "-These failure modes motivate the search for cheap-to-compute \\emph{canary metrics} that provide early warning, analogous to early-warning signals for critical transitions in ecological and climate systems~\\cite{scheffer2009early,scheffer2012anticipating}.",
          "+When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\\cite{shumailov2024curse,alemohammad2024mad}.",
          "+Lexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.",
          "+As machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.",
          "+By the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.",
          "+This threat motivates the search for cheap-to-compute \\emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.",
          "+The concept parallels early-warning signals for critical transitions in ecological systems~\\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.",
          "+Several recent studies have pursued this direction: \\citet{du2026geometric} observe that calibration error rises before accuracy degrades, SIGMA~\\cite{sigma2026spectral} proposes spectral indicators, and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.",
          " ",
          "-Several recent studies have pursued this direction: \\citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.",
          "-Yet the statistical methodology underlying these lead-lag claims (whether a canary metric genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends) has received little scrutiny.",
          "+Yet the statistical methodology underlying these lead-lag claims has received little scrutiny.",
          "+Whether a candidate canary genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends, is a question that existing analyses leave unresolved.",
          "+Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\\cite{boettiger2012limits}.",
          "+In the absence of proper controls, the choice of statistical method alone can shift conclusions on the same data from universal significance to complete null.",
          "+This makes the validity of existing canary claims an open question with direct consequences for practitioners who rely on such signals to trigger training interventions.",
          " ",
          "-We identify several methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:",
          "-(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends, a well-known hazard when correlating co-trending time series;",
          "-(2)~no multi-method cross-validation; conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;",
          "-(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and",
          "-(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.",
          "-The closest predecessor is \\citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.",
          "-Their analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests, leaving open the question of whether the observed lead is genuine or an artifact of shared trends.",
          "-The early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating}, widely adopted in ecology for anticipating tipping points, provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\\cite{boettiger2012limits}.",
          "+We identify four specific deficiencies that pervade existing lead-lag analyses of iterative training collapse.",
          "+(1)~No differencing tests rule out spurious regression from shared non-stationary trends, a well-documented hazard in analyses of co-trending time series~\\cite{granger1974spurious}.",
          "+(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined; no multi-method cross-validation is conducted.",
          "+(3)~No false discovery rate (FDR) correction (e.g., Benjamini--Hochberg) guards against spurious findings when testing many metric pairs simultaneously.",
          "+(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.",
          "+The closest predecessor is \\citet{du2026geometric}, who report that calibration error rises before accuracy degrades in iteratively trained language models.",
          "+Their analysis, however, covers a single metric pair, spans only 1--3 generations, and relies on visual comparisons without statistical tests.",
          "+The early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating} provides theoretical motivation but has not been applied to training collapse with the rigor that such short, non-stationary series require.",
          " ",
          "-We address these gaps through a systematic case study of canary prediction of diversity collapse, the progressive loss of lexical diversity in model-generated text across training generations.",
          "-Using Pythia-410M across six contamination levels ($\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:",
          "-\\begin{enumerate}",
          "-    \\item \\textbf{Method sensitivity.} Applied to the same data (16 candidate canary$\\to$downstream pairs, including candidates later excluded; \\S\\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).",
          "-    \\item \\textbf{Spurious regression.} Canary$\\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.",
          "-    \\item \\textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\\to$diversity pairs FDR-significant at full synthetic replacement ($\\alpha{=}1.0$) but 0/24 at $\\alpha{\\leq}0.25$ (three seeds), with seed-dependent onset at $\\alpha{=}0.50$ (0/8--6/8, three seeds), demonstrating that detectability depends sharply on both contamination level and training stochasticity.",
          "-\\end{enumerate}",
          "-To move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.",
          "+We address these gaps through a multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of canary prediction of diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\\cite{li2016diversity}) across training generations.",
          "+Using Pythia-410M~\\cite{biderman2023pythia} across six contamination levels ($\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we apply five statistical methods to expose three methodological pitfalls (method sensitivity, spurious regression, and regime dependence) and propose the Multi-Method Consensus Test (MMCT), a formal FPR-inverse-weighted consensus framework inspired by specification curve analysis~\\cite{simonsohn2020specification}.",
          "+An extended eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals a canary blind spot: at $\\alpha{=}0.10$, diversity has already collapsed measurably but canary metrics remain at null levels, which places a detection lower bound at $\\alpha{\\geq}0.25$.",
          "+We identify token entropy as a robust one-generation-ahead canary for diversity collapse and demonstrate that canary-triggered predictive intervention reduces peak perplexity by 63\\% and accelerates recovery by two generations compared to reactive approaches.",
          "+Cross-architecture validation on GPT-2-medium and OPT-1.3B confirms that these findings transfer beyond the primary experimental platform.",
          "+Granger precedence in our framework establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics, not model collapse broadly.",
          "+To our knowledge, this constitutes the first multiverse-style analysis of lead-lag claims in model collapse: the same dataset, analyzed with five methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.",
          " ",
          "-The framework's utility is demonstrated by its calibration on built-in experimental controls.",
          "-Naive cross-correlation identifies 100\\% of canary--collapse metric pairs as FDR-significant; the uniform consensus pipeline ($K{\\geq}4/5$ methods) reduces this to 0\\% FPR but yields $p{=}0.16$ under null-calibrated testing, failing to reach conventional significance.",
          "-MMCT's FPR-inverse weighting resolves this gap, providing formal $p$-values with FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$ (a $9.5\\times$ improvement over the uniform threshold's 8.3\\%).",
          "-Applying the framework, we identify token entropy as a one-generation-ahead canary for diversity collapse at $\\alpha{=}1.0$: the full consensus pipeline confirms directional asymmetry with cross-correlation $|r|{>}0.99$, 24/24 forward-direction pairs FDR-significant, and 0/24 in the reverse direction.",
          "-Three-seed replication at $\\alpha{=}0.75$ extends this finding (19/24 forward, 0/24 reverse via permutation Granger), though method-level consensus remains transitional (Tier~2--3).",
          "-The onset boundary of causal detectability lies at $\\alpha{\\approx}0.25$--$0.50$, below which all seeds agree on null.",
          "-We note that Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.",
          "-Our work constitutes, to our knowledge, the first multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of lead-lag claims in model collapse: the same dataset, analyzed with five statistical methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.",
          "-",
          " Our contributions are:",
          " \\begin{enumerate}",
          "-    \\item \\textbf{Systematic exposure of three methodological pitfalls} (method sensitivity, spurious regression, regime dependence) in lead-lag analysis of iterative training collapse.",
          "-    Method choice alone inflates spurious-signal rates to at least 62.5\\%; first-differencing eliminates canary$\\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.",
          "-    These results demonstrate that single-method, single-regime analyses, the current norm in this literature, are unreliable.",
          "+    \\item \\textbf{Systematic exposure of three methodological pitfalls and a consensus resolution} (\\S\\ref{sec:method}, \\S\\ref{sec:method_sensitivity}).",
          "+    Method choice alone inflates spurious-signal rates to at least 62.5\\%, with five methods yielding FDR significance rates from 25\\% to 100\\% and inter-method agreement of $\\kappa{=}0.185$.",
          "+    First-differencing eliminates canary$\\to$perplexity associations entirely ($F{\\approx}0$, $p{=}0.99$); they are artifacts of co-trending, not genuine temporal precedence.",
          "+    The same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.",
          "+    To resolve these pitfalls, we propose MMCT: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing, while MMCT's pair-level FPR-inverse weighting achieves FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$, a $9.5{\\times}$ improvement over the uniform threshold's 8.3\\%.",
          "+    Shapley-value decomposition (exact 32-coalition enumeration) identifies naive cross-correlation as the sole FPR driver (Shapley(FPR)${=}{+}0.348$) and permutation Granger as the strongest suppressor (Shapley(FPR)${=}{-}0.194$).",
          " ",
          "-    \\item \\textbf{A Multi-Method Consensus Test (MMCT)} that moves beyond ad-hoc threshold voting to formal inference: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing; MMCT's pair-level FPR-inverse weighting provides formal $p$-values achieving FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$ (a $9.5\\times$ improvement over the uniform threshold's 8.3\\%).",
          "-    Shapley-value decomposition (exact 32-coalition enumeration) reveals that naive cross-correlation is the sole FPR driver (Shapley(FPR)${=}{+}0.348$) while permutation Granger is the strongest FPR suppressor (Shapley(FPR)${=}{-}0.194$); these diagnostics provide principled guidance for method panel selection.",
          "+    \\item \\textbf{Regime-dependent detectability with a canary blind spot} (\\S\\ref{sec:regime}).",
          "+    An eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals that permutation Granger follows a step function (0/24 at $\\alpha{\\leq}0.25$, 24/24 at $\\alpha{=}1.0$), while MMCT exhibits gradual dose-response (43.8\\%$\\to$58.3\\%$\\to$79.2\\% detection at $\\alpha{=}0.25/0.50/0.75$).",
          "+    At $\\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed (distinct-1 drops 39.6\\%) but canary metrics remain indistinguishable from the null condition (entropy differs by less than one percentage point).",
          "+    These results place a lower bound on reliable detection at $\\alpha{\\geq}0.25$.",
          " ",
          "-    \\item \\textbf{Identification of token entropy as a robust one-generation-ahead canary} for diversity collapse at $\\alpha{=}1.0$, confirmed by 4 independent methods, 4 seeds, and cross-architecture replication on GPT-2-medium and OPT-1.3B, with complete directional asymmetry (24/24 forward, 0/24 reverse); directional asymmetry extends to $\\alpha{=}0.75$ across 3~seeds (19/24 forward, 0/24 reverse) in a transitional consensus regime (Tier~2--3). The claim is scoped to diversity metrics (distinct-$n$), not model collapse broadly.",
          "+    \\item \\textbf{Token entropy as a one-generation-ahead canary for diversity collapse} (\\S\\ref{sec:case_study}, \\S\\ref{sec:generalization}).",
          "+    At $\\alpha{=}1.0$, the full consensus pipeline confirms directional asymmetry: 24/24 forward-direction pairs are FDR-significant and 0/24 in the reverse direction, across four methods and four seeds.",
          "+    Cross-architecture replication on GPT-2-medium and OPT-1.3B confirms the pattern.",
          "+    At $\\alpha{=}0.75$, three-seed replication yields 19/24 forward and 0/24 reverse (permutation Granger), with transitional consensus (Tier~2--3).",
          "+    This claim is scoped to diversity metrics (distinct-$n$); the perplexity channel is spurious.",
          " ",
          "-    \\item \\textbf{Cross-architecture generalization} (\\S\\ref{sec:generalization}): validation on three decoder-only transformer families (Pythia-410M, GPT-2-medium, OPT-1.3B) confirms that the entropy-leads-diversity pattern and the consensus framework's operating thresholds transfer across architectures, with all three families reaching Tier~3 consensus ($K{\\geq}4/5$) at $\\alpha{=}1.0$ and 0 reverse-direction pairs significant in any architecture.",
          "+    \\item \\textbf{Canary-based early intervention} (\\S\\ref{sec:intervention}).",
          "+    As a practical demonstration, we compare predictive intervention (triggered when token entropy drops ${>}15\\%$) against reactive intervention (triggered when distinct-1 drops ${>}10\\%$).",
          "+    The predictive trigger fires one generation earlier, reduces peak perplexity by 63\\% (56.99 vs.\\ 157.09), and achieves full recovery two generations faster (Generation~2 vs.\\ Generation~4).",
          "+    This result is validated at $\\alpha{=}1.0$ across two seeds (s42 fp32, s43 bf16).",
          " \\end{enumerate}",
          " ",
          " The remainder of this paper is organized as follows.",
          " \\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.",
          " \\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.",
          " \\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.",
          "-\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), a case study of canary prediction of diversity collapse (\\S\\ref{sec:case_study}), consensus framework validation (\\S\\ref{sec:consensus_validation}), and cross-architecture generalization (\\S\\ref{sec:generalization}).",
          "-\\S\\ref{sec:discussion} discusses implications (including the practical utility paradox, the token entropy--perplexity distinction, and NLP-specific constraints on lead-lag analysis) and outlines directions for future work.",
          "-\\S\\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\\S\\ref{sec:limitations}).",
          "\\ No newline at end of file",
          "+\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), canary prediction of diversity collapse (\\S\\ref{sec:case_study}), consensus framework validation (\\S\\ref{sec:consensus_validation}), cross-architecture generalization (\\S\\ref{sec:generalization}), and canary-based early intervention (\\S\\ref{sec:intervention}).",
          "+\\S\\ref{sec:discussion} discusses implications and future directions, and \\S\\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\\S\\ref{sec:limitations})."
        ]
      }
    ],
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nPractitioners monitoring iterative training pipelines face a diagnostic blind spot: the metrics most commonly used to detect distributional degradation can yield false positive rates of 62.5--100\\% when applied without proper statistical controls, yet no established protocol exists for distinguishing genuine early-warning signals from artifacts of shared non-stationary trends.\nThis blind spot is consequential because iterative training collapse, where models are unwittingly trained on output from earlier generations, is increasingly likely as machine-generated text proliferates on the web~\\cite{shumailov2024curse,alemohammad2024mad}.\nTail modes vanish, lexical diversity narrows, and calibration deteriorates across generations.\nThese failure modes motivate the search for cheap-to-compute \\emph{canary metrics} that provide early warning, analogous to early-warning signals for critical transitions in ecological and climate systems~\\cite{scheffer2009early,scheffer2012anticipating}.\n\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\nYet the statistical methodology underlying these lead-lag claims (whether a canary metric genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends) has received little scrutiny.\n\nWe identify several methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:\n(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends, a well-known hazard when correlating co-trending time series;\n(2)~no multi-method cross-validation; conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;\n(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and\n(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests, leaving open the question of whether the observed lead is genuine or an artifact of shared trends.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating}, widely adopted in ecology for anticipating tipping points, provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\\cite{boettiger2012limits}.\n\nWe address these gaps through a systematic case study of canary prediction of diversity collapse, the progressive loss of lexical diversity in model-generated text across training generations.\nUsing Pythia-410M across six contamination levels ($\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:\n\\begin{enumerate}\n    \\item \\textbf{Method sensitivity.} Applied to the same data (16 candidate canary$\\to$downstream pairs, including candidates later excluded; \\S\\ref{sec:case_study}), five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).\n    \\item \\textbf{Spurious regression.} Canary$\\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.\n    \\item \\textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\\to$diversity pairs FDR-significant at full synthetic replacement ($\\alpha{=}1.0$) but 0/24 at $\\alpha{\\leq}0.25$ (three seeds), with seed-dependent onset at $\\alpha{=}0.50$ (0/8--6/8, three seeds), demonstrating that detectability depends sharply on both contamination level and training stochasticity.\n\\end{enumerate}\nTo move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.\n\nThe framework's utility is demonstrated by its calibration on built-in experimental controls.\nNaive cross-correlation identifies 100\\% of canary--collapse metric pairs as FDR-significant; the uniform consensus pipeline ($K{\\geq}4/5$ methods) reduces this to 0\\% FPR but yields $p{=}0.16$ under null-calibrated testing, failing to reach conventional significance.\nMMCT's FPR-inverse weighting resolves this gap, providing formal $p$-values with FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$ (a $9.5\\times$ improvement over the uniform threshold's 8.3\\%).\nApplying the framework, we identify token entropy as a one-generation-ahead canary for diversity collapse at $\\alpha{=}1.0$: the full consensus pipeline confirms directional asymmetry with cross-correlation $|r|{>}0.99$, 24/24 forward-direction pairs FDR-significant, and 0/24 in the reverse direction.\nThree-seed replication at $\\alpha{=}0.75$ extends this finding (19/24 forward, 0/24 reverse via permutation Granger), though method-level consensus remains transitional (Tier~2--3).\nThe onset boundary of causal detectability lies at $\\alpha{\\approx}0.25$--$0.50$, below which all seeds agree on null.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\nOur work constitutes, to our knowledge, the first multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of lead-lag claims in model collapse: the same dataset, analyzed with five statistical methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls} (method sensitivity, spurious regression, regime dependence) in lead-lag analysis of iterative training collapse.\n    Method choice alone inflates spurious-signal rates to at least 62.5\\%; first-differencing eliminates canary$\\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    These results demonstrate that single-method, single-regime analyses, the current norm in this literature, are unreliable.\n\n    \\item \\textbf{A Multi-Method Consensus Test (MMCT)} that moves beyond ad-hoc threshold voting to formal inference: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing; MMCT's pair-level FPR-inverse weighting provides formal $p$-values achieving FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$ (a $9.5\\times$ improvement over the uniform threshold's 8.3\\%).\n    Shapley-value decomposition (exact 32-coalition enumeration) reveals that naive cross-correlation is the sole FPR driver (Shapley(FPR)${=}{+}0.348$) while permutation Granger is the strongest FPR suppressor (Shapley(FPR)${=}{-}0.194$); these diagnostics provide principled guidance for method panel selection.\n\n    \\item \\textbf{Identification of token entropy as a robust one-generation-ahead canary} for diversity collapse at $\\alpha{=}1.0$, confirmed by 4 independent methods, 4 seeds, and cross-architecture replication on GPT-2-medium and OPT-1.3B, with complete directional asymmetry (24/24 forward, 0/24 reverse); directional asymmetry extends to $\\alpha{=}0.75$ across 3~seeds (19/24 forward, 0/24 reverse) in a transitional consensus regime (Tier~2--3). The claim is scoped to diversity metrics (distinct-$n$), not model collapse broadly.\n\n    \\item \\textbf{Cross-architecture generalization} (\\S\\ref{sec:generalization}): validation on three decoder-only transformer families (Pythia-410M, GPT-2-medium, OPT-1.3B) confirms that the entropy-leads-diversity pattern and the consensus framework's operating thresholds transfer across architectures, with all three families reaching Tier~3 consensus ($K{\\geq}4/5$) at $\\alpha{=}1.0$ and 0 reverse-direction pairs significant in any architecture.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), a case study of canary prediction of diversity collapse (\\S\\ref{sec:case_study}), consensus framework validation (\\S\\ref{sec:consensus_validation}), and cross-architecture generalization (\\S\\ref{sec:generalization}).\n\\S\\ref{sec:discussion} discusses implications (including the practical utility paradox, the token entropy--perplexity distinction, and NLP-specific constraints on lead-lag analysis) and outlines directions for future work.\n\\S\\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\\S\\ref{sec:limitations}).",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the file was written correctly and do the style checks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "bbf61ffb-751f-4976-85a7-5f4b86a00680",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQfTpPXMsMATk38rTvznSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32420,
      "cache_read_input_tokens": 42140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32420
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

_source line 35_

Now let me verify the file and run style checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "81db860d-c227-4135-be1c-8dba51092e01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQfTpPXMsMATk38rTvznSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32420,
      "cache_read_input_tokens": 42140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32420
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

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_01Qg9jXF8uc7g58HCbAABAf8`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "41c69400-b81f-4908-bd76-5be8461a7636",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQfTpPXMsMATk38rTvznSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32420,
      "cache_read_input_tokens": 42140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32420
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

_source line 37 · 2026-05-19T04:39:07.184Z_

<details><summary>↩ Tool result · `toolu_01Qg9jXF8uc7g58HCbAABAf8`</summary>

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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "df4ce03c-8824-4e03-9b90-3a99dc07d15e",
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

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01HKZ41vooHnk4Yt2XokBxQt`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "4974a250-f57d-4fd2-906f-8fa9af91581b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQfTpPXMsMATk38rTvznSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32420,
      "cache_read_input_tokens": 42140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32420
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

_source line 39 · 2026-05-19T04:39:07.664Z_

<details><summary>↩ Tool result · `toolu_01HKZ41vooHnk4Yt2XokBxQt`</summary>

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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "7ec82cfa-d3bf-487a-b7b6-d2ab22f2b2fc",
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

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_014YEN7kYXwoojmyMqqxQ9mD`</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "6b43d131-c3ba-4016-9c83-3d3927614598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQfTpPXMsMATk38rTvznSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32420,
      "cache_read_input_tokens": 42140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32420
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

_source line 41 · 2026-05-19T04:39:08.608Z_

<details><summary>↩ Tool result · `toolu_014YEN7kYXwoojmyMqqxQ9mD`</summary>

```text
27:We address these gaps through a multiverse-style analysis~\cite{bell2022modeling,kapoor2024reforms} of canary prediction of diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\cite{li2016diversity}) across training generations.
39:    First-differencing eliminates canary$\to$perplexity associations entirely ($F{\approx}0$, $p{=}0.99$); they are artifacts of co-trending, not genuine temporal precedence.
41:    To resolve these pitfalls, we propose MMCT: the standard $K{\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing, while MMCT's pair-level FPR-inverse weighting achieves FPR${=}$0\% and 79.2\% detection at $\alpha{=}0.75$, a $9.5{\times}$ improvement over the uniform threshold's 8.3\%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "38aa5958-2553-4652-9c93-ccab0217247e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "27:We address these gaps through a multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of canary prediction of diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\\cite{li2016diversity}) across training generations.\n39:    First-differencing eliminates canary$\\to$perplexity associations entirely ($F{\\approx}0$, $p{=}0.99$); they are artifacts of co-trending, not genuine temporal precedence.\n41:    To resolve these pitfalls, we propose MMCT: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing, while MMCT's pair-level FPR-inverse weighting achieves FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$, a $9.5{\\times}$ improvement over the uniform threshold's 8.3\\%.",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Grep · `toolu_01QuZdhzG7M2rL6sPqh89mzq`</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate|myriad|plethora|Notably|It is worth noting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "627b9245-9fe7-4f56-bf4e-403c21cfdc0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQfTpPXMsMATk38rTvznSQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32420,
      "cache_read_input_tokens": 42140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32420
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

_source line 43 · 2026-05-19T04:39:10.132Z_

<details><summary>↩ Tool result · `toolu_01QuZdhzG7M2rL6sPqh89mzq`</summary>

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
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "7581f86d-1acc-4345-b62c-d78d70544b07",
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

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Let me check the "ing," matches:

1. "training generations." - "training" is an adjective modifying "generations", not a participial phrase. The grep matched "ing," in "training," but actually looking at the line: "across training generations." - there's no comma after "generations". Wait, the grep matched "ing," somewhere. Let me re-read:

Line 27: "...diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\cite{li2016diversity}) across training generations."
The match is "ing," in "training," wait no - it matched "ing," in "modeling," from the cite. No wait, let me look more carefully. The grep for "ing," found:


Line 27: `\cite{bell2022modeling,kapoor2024reforms}` - "modeling," is inside a citation. Similarly, "co-trending," on line 39 appears within a clause, and line 41 has "testing, while" also embedded in a clause rather than at the end of a sentence. These matches are all within citations or mid-clause, not standalone participial phrases ending sentences.

Looking at the pattern more carefully, the "ing," occurrences are either citation keys, gerunds in "X, not Y" constructions, or nouns in "X, while Y" structures—none of them match the prohibited ", -ing phrase" pattern like ", demonstrating." I'm also not finding any em-dashes, explanatory en-dashes, or blacklisted words, so the document appears clean on those fronts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "fc074d25-d177-4a5e-9942-b6d8d0d4166d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcbGgxXbfNe3fDLKRAnKGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 74560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
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

_source line 45_

All style checks pass:
- No em-dash (—): 0 matches
- No explanatory en-dash ( – ): 0 matches
- No blacklisted words: 0 matches
- The "ing," matches are all safe: citation keys (`bell2022modeling,`), nouns in contrast constructions (`co-trending, not`), and compound nouns (`testing, while`)

Let me do a rough word count and verify the final file reads correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "898df4fa-27c3-41d9-859b-5ed4e672c5ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcbGgxXbfNe3fDLKRAnKGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 74560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01R2ZawJgCZ4dAa4NH4vvZZW`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}~]//g; s/  */ /g' | wc -w",
  "description": "Rough word count excluding LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "6e3d06d1-814d-4026-9ede-11307e9c2862",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EcbGgxXbfNe3fDLKRAnKGq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 74560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 967
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

_source line 47 · 2026-05-19T04:39:31.673Z_

<details><summary>↩ Tool result · `toolu_01R2ZawJgCZ4dAa4NH4vvZZW`</summary>

```text
1044
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "5b691ea5-d591-4755-908b-dd668031a4a9",
  "tool_use_result": {
    "stdout": "1044",
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

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
~1044 words, which is close to the ~1100 target. Good enough.

Let me do a final read of the file to make sure everything is correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "e2783977-3a19-4bde-aded-886cccf34a1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAWx13DQ62u9yz1Q9w89oP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 75527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
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

_source line 49_

~1044 words, within range of the ~1100 target.

Let me do a final read to verify the complete file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "0b6438a7-a1c0-4029-9945-2c2cb734e844",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAWx13DQ62u9yz1Q9w89oP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 75527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
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

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_019gvZhBP3ZhsAoY3u2CGNm2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "cd803133-ff9b-4995-8e8c-c2fe59677194",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AAWx13DQ62u9yz1Q9w89oP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 75527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
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

_source line 51 · 2026-05-19T04:39:39.365Z_

<details><summary>↩ Tool result · `toolu_019gvZhBP3ZhsAoY3u2CGNm2`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	Lexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.
6	As machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.
7	By the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.
8	This threat motivates the search for cheap-to-compute \emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.
9	The concept parallels early-warning signals for critical transitions in ecological systems~\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.
10	Several recent studies have pursued this direction: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, SIGMA~\cite{sigma2026spectral} proposes spectral indicators, and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
11	
12	Yet the statistical methodology underlying these lead-lag claims has received little scrutiny.
13	Whether a candidate canary genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends, is a question that existing analyses leave unresolved.
14	Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
15	In the absence of proper controls, the choice of statistical method alone can shift conclusions on the same data from universal significance to complete null.
16	This makes the validity of existing canary claims an open question with direct consequences for practitioners who rely on such signals to trigger training interventions.
17	
18	We identify four specific deficiencies that pervade existing lead-lag analyses of iterative training collapse.
19	(1)~No differencing tests rule out spurious regression from shared non-stationary trends, a well-documented hazard in analyses of co-trending time series~\cite{granger1974spurious}.
20	(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined; no multi-method cross-validation is conducted.
21	(3)~No false discovery rate (FDR) correction (e.g., Benjamini--Hochberg) guards against spurious findings when testing many metric pairs simultaneously.
22	(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.
23	The closest predecessor is \citet{du2026geometric}, who report that calibration error rises before accuracy degrades in iteratively trained language models.
24	Their analysis, however, covers a single metric pair, spans only 1--3 generations, and relies on visual comparisons without statistical tests.
25	The early-warning framework of \citet{scheffer2009early,scheffer2012anticipating} provides theoretical motivation but has not been applied to training collapse with the rigor that such short, non-stationary series require.
26	
27	We address these gaps through a multiverse-style analysis~\cite{bell2022modeling,kapoor2024reforms} of canary prediction of diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\cite{li2016diversity}) across training generations.
28	Using Pythia-410M~\cite{biderman2023pythia} across six contamination levels ($\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$) and up to four random seeds, we apply five statistical methods to expose three methodological pitfalls (method sensitivity, spurious regression, and regime dependence) and propose the Multi-Method Consensus Test (MMCT), a formal FPR-inverse-weighted consensus framework inspired by specification curve analysis~\cite{simonsohn2020specification}.
29	An extended eight-point regime map ($\alpha \in \{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\}$) reveals a canary blind spot: at $\alpha{=}0.10$, diversity has already collapsed measurably but canary metrics remain at null levels, which places a detection lower bound at $\alpha{\geq}0.25$.
30	We identify token entropy as a robust one-generation-ahead canary for diversity collapse and demonstrate that canary-triggered predictive intervention reduces peak perplexity by 63\% and accelerates recovery by two generations compared to reactive approaches.
31	Cross-architecture validation on GPT-2-medium and OPT-1.3B confirms that these findings transfer beyond the primary experimental platform.
32	Granger precedence in our framework establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics, not model collapse broadly.
33	To our knowledge, this constitutes the first multiverse-style analysis of lead-lag claims in model collapse: the same dataset, analyzed with five methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.
34	
35	Our contributions are:
36	\begin{enumerate}
37	    \item \textbf{Systematic exposure of three methodological pitfalls and a consensus resolution} (\S\ref{sec:method}, \S\ref{sec:method_sensitivity}).
38	    Method choice alone inflates spurious-signal rates to at least 62.5\%, with five methods yielding FDR significance rates from 25\% to 100\% and inter-method agreement of $\kappa{=}0.185$.
39	    First-differencing eliminates canary$\to$perplexity associations entirely ($F{\approx}0$, $p{=}0.99$); they are artifacts of co-trending, not genuine temporal precedence.
40	    The same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.
41	    To resolve these pitfalls, we propose MMCT: the standard $K{\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing, while MMCT's pair-level FPR-inverse weighting achieves FPR${=}$0\% and 79.2\% detection at $\alpha{=}0.75$, a $9.5{\times}$ improvement over the uniform threshold's 8.3\%.
42	    Shapley-value decomposition (exact 32-coalition enumeration) identifies naive cross-correlation as the sole FPR driver (Shapley(FPR)${=}{+}0.348$) and permutation Granger as the strongest suppressor (Shapley(FPR)${=}{-}0.194$).
43	
44	    \item \textbf{Regime-dependent detectability with a canary blind spot} (\S\ref{sec:regime}).
45	    An eight-point regime map ($\alpha \in \{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\}$) reveals that permutation Granger follows a step function (0/24 at $\alpha{\leq}0.25$, 24/24 at $\alpha{=}1.0$), while MMCT exhibits gradual dose-response (43.8\%$\to$58.3\%$\to$79.2\% detection at $\alpha{=}0.25/0.50/0.75$).
46	    At $\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed (distinct-1 drops 39.6\%) but canary metrics remain indistinguishable from the null condition (entropy differs by less than one percentage point).
47	    These results place a lower bound on reliable detection at $\alpha{\geq}0.25$.
48	
49	    \item \textbf{Token entropy as a one-generation-ahead canary for diversity collapse} (\S\ref{sec:case_study}, \S\ref{sec:generalization}).
50	    At $\alpha{=}1.0$, the full consensus pipeline confirms directional asymmetry: 24/24 forward-direction pairs are FDR-significant and 0/24 in the reverse direction, across four methods and four seeds.
51	    Cross-architecture replication on GPT-2-medium and OPT-1.3B confirms the pattern.
52	    At $\alpha{=}0.75$, three-seed replication yields 19/24 forward and 0/24 reverse (permutation Granger), with transitional consensus (Tier~2--3).
53	    This claim is scoped to diversity metrics (distinct-$n$); the perplexity channel is spurious.
54	
55	    \item \textbf{Canary-based early intervention} (\S\ref{sec:intervention}).
56	    As a practical demonstration, we compare predictive intervention (triggered when token entropy drops ${>}15\%$) against reactive intervention (triggered when distinct-1 drops ${>}10\%$).
57	    The predictive trigger fires one generation earlier, reduces peak perplexity by 63\% (56.99 vs.\ 157.09), and achieves full recovery two generations faster (Generation~2 vs.\ Generation~4).
58	    This result is validated at $\alpha{=}1.0$ across two seeds (s42 fp32, s43 bf16).
59	\end{enumerate}
60	
61	The remainder of this paper is organized as follows.
62	\S\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.
63	\S\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.
64	\S\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.
65	\S\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\S\ref{sec:method_sensitivity}), regime-dependent detectability (\S\ref{sec:regime}), canary prediction of diversity collapse (\S\ref{sec:case_study}), consensus framework validation (\S\ref{sec:consensus_validation}), cross-architecture generalization (\S\ref{sec:generalization}), and canary-based early intervention (\S\ref{sec:intervention}).
66	\S\ref{sec:discussion} discusses implications and future directions, and \S\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\S\ref{sec:limitations}).
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "104fc562-678e-4501-9feb-24f65114e00c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\\cite{shumailov2024curse,alemohammad2024mad}.\nLexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.\nAs machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.\nBy the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.\nThis threat motivates the search for cheap-to-compute \\emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.\nThe concept parallels early-warning signals for critical transitions in ecological systems~\\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} observe that calibration error rises before accuracy degrades, SIGMA~\\cite{sigma2026spectral} proposes spectral indicators, and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\n\nYet the statistical methodology underlying these lead-lag claims has received little scrutiny.\nWhether a candidate canary genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends, is a question that existing analyses leave unresolved.\nIterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\\cite{boettiger2012limits}.\nIn the absence of proper controls, the choice of statistical method alone can shift conclusions on the same data from universal significance to complete null.\nThis makes the validity of existing canary claims an open question with direct consequences for practitioners who rely on such signals to trigger training interventions.\n\nWe identify four specific deficiencies that pervade existing lead-lag analyses of iterative training collapse.\n(1)~No differencing tests rule out spurious regression from shared non-stationary trends, a well-documented hazard in analyses of co-trending time series~\\cite{granger1974spurious}.\n(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and directionality are rarely examined; no multi-method cross-validation is conducted.\n(3)~No false discovery rate (FDR) correction (e.g., Benjamini--Hochberg) guards against spurious findings when testing many metric pairs simultaneously.\n(4)~No regime-dependent analysis is performed, despite the possibility that the same test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who report that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, covers a single metric pair, spans only 1--3 generations, and relies on visual comparisons without statistical tests.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating} provides theoretical motivation but has not been applied to training collapse with the rigor that such short, non-stationary series require.\n\nWe address these gaps through a multiverse-style analysis~\\cite{bell2022modeling,kapoor2024reforms} of canary prediction of diversity collapse, the progressive loss of lexical diversity (as measured by distinct-$n$~\\cite{li2016diversity}) across training generations.\nUsing Pythia-410M~\\cite{biderman2023pythia} across six contamination levels ($\\alpha \\in \\{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we apply five statistical methods to expose three methodological pitfalls (method sensitivity, spurious regression, and regime dependence) and propose the Multi-Method Consensus Test (MMCT), a formal FPR-inverse-weighted consensus framework inspired by specification curve analysis~\\cite{simonsohn2020specification}.\nAn extended eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals a canary blind spot: at $\\alpha{=}0.10$, diversity has already collapsed measurably but canary metrics remain at null levels, which places a detection lower bound at $\\alpha{\\geq}0.25$.\nWe identify token entropy as a robust one-generation-ahead canary for diversity collapse and demonstrate that canary-triggered predictive intervention reduces peak perplexity by 63\\% and accelerates recovery by two generations compared to reactive approaches.\nCross-architecture validation on GPT-2-medium and OPT-1.3B confirms that these findings transfer beyond the primary experimental platform.\nGranger precedence in our framework establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics, not model collapse broadly.\nTo our knowledge, this constitutes the first multiverse-style analysis of lead-lag claims in model collapse: the same dataset, analyzed with five methods across six contamination regimes, yields conclusions that span the full spectrum from universal significance to complete null.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls and a consensus resolution} (\\S\\ref{sec:method}, \\S\\ref{sec:method_sensitivity}).\n    Method choice alone inflates spurious-signal rates to at least 62.5\\%, with five methods yielding FDR significance rates from 25\\% to 100\\% and inter-method agreement of $\\kappa{=}0.185$.\n    First-differencing eliminates canary$\\to$perplexity associations entirely ($F{\\approx}0$, $p{=}0.99$); they are artifacts of co-trending, not genuine temporal precedence.\n    The same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    To resolve these pitfalls, we propose MMCT: the standard $K{\\geq}4/5$ uniform threshold yields $p{=}0.16$ under null-calibrated testing, while MMCT's pair-level FPR-inverse weighting achieves FPR${=}$0\\% and 79.2\\% detection at $\\alpha{=}0.75$, a $9.5{\\times}$ improvement over the uniform threshold's 8.3\\%.\n    Shapley-value decomposition (exact 32-coalition enumeration) identifies naive cross-correlation as the sole FPR driver (Shapley(FPR)${=}{+}0.348$) and permutation Granger as the strongest suppressor (Shapley(FPR)${=}{-}0.194$).\n\n    \\item \\textbf{Regime-dependent detectability with a canary blind spot} (\\S\\ref{sec:regime}).\n    An eight-point regime map ($\\alpha \\in \\{0.00, 0.05, 0.10, 0.25, 0.50, 0.60, 0.75, 1.00\\}$) reveals that permutation Granger follows a step function (0/24 at $\\alpha{\\leq}0.25$, 24/24 at $\\alpha{=}1.0$), while MMCT exhibits gradual dose-response (43.8\\%$\\to$58.3\\%$\\to$79.2\\% detection at $\\alpha{=}0.25/0.50/0.75$).\n    At $\\alpha{=}0.10$, a canary blind spot emerges: diversity has already collapsed (distinct-1 drops 39.6\\%) but canary metrics remain indistinguishable from the null condition (entropy differs by less than one percentage point).\n    These results place a lower bound on reliable detection at $\\alpha{\\geq}0.25$.\n\n    \\item \\textbf{Token entropy as a one-generation-ahead canary for diversity collapse} (\\S\\ref{sec:case_study}, \\S\\ref{sec:generalization}).\n    At $\\alpha{=}1.0$, the full consensus pipeline confirms directional asymmetry: 24/24 forward-direction pairs are FDR-significant and 0/24 in the reverse direction, across four methods and four seeds.\n    Cross-architecture replication on GPT-2-medium and OPT-1.3B confirms the pattern.\n    At $\\alpha{=}0.75$, three-seed replication yields 19/24 forward and 0/24 reverse (permutation Granger), with transitional consensus (Tier~2--3).\n    This claim is scoped to diversity metrics (distinct-$n$); the perplexity channel is spurious.\n\n    \\item \\textbf{Canary-based early intervention} (\\S\\ref{sec:intervention}).\n    As a practical demonstration, we compare predictive intervention (triggered when token entropy drops ${>}15\\%$) against reactive intervention (triggered when distinct-1 drops ${>}10\\%$).\n    The predictive trigger fires one generation earlier, reduces peak perplexity by 63\\% (56.99 vs.\\ 157.09), and achieves full recovery two generations faster (Generation~2 vs.\\ Generation~4).\n    This result is validated at $\\alpha{=}1.0$ across two seeds (s42 fp32, s43 bf16).\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), canary prediction of diversity collapse (\\S\\ref{sec:case_study}), consensus framework validation (\\S\\ref{sec:consensus_validation}), cross-architecture generalization (\\S\\ref{sec:generalization}), and canary-based early intervention (\\S\\ref{sec:intervention}).\n\\S\\ref{sec:discussion} discusses implications and future directions, and \\S\\ref{sec:conclusion} concludes, followed by a dedicated Limitations section (\\S\\ref{sec:limitations}).\n",
      "numLines": 67,
      "startLine": 1,
      "totalLines": 67
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

Introduction 已重写完成。~1044 words，结构为：

1. **P1 背景** (L4-10): model collapse + canary metrics 动机 + 现有尝试 (du2026geometric, SIGMA, DCES)
2. **P2 问题重要性** (L12-16): 方法论缺乏审视，短时序 + 假阳性风险
3. **P3 四项缺陷** (L18-25): 4 deficiencies + closest predecessor (du2026geometric) + ecological framework gap
4. **P4 核心方案** (L27-33): multiverse analysis + 3 pitfalls + MMCT + blind spot + intervention + causality caveat + diversity-only scope
5. **贡献列表** (L36-59): Claim 3→2→1→4 顺序，含 MMCT/Shapley/regime map/blind spot/canary/intervention 全部数字
6. **Roadmap** (L61-66): 新增 `\S{sec:intervention}`

风格检查通过：无 em-dash，无解释性 en-dash，无 -ing phrase endings，无黑名单词，FDR 首次出现已展开定义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "uuid": "c3f15635-6dcd-4728-ac7e-437886ec8d5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MXwckbCtmHBJhZXnRRqEsr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2882,
      "cache_read_input_tokens": 76374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2882
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

_source line 53_

Introduction 已重写完成。~1044 words，结构为：

1. **P1 背景** (L4-10): model collapse + canary metrics 动机 + 现有尝试 (du2026geometric, SIGMA, DCES)
2. **P2 问题重要性** (L12-16): 方法论缺乏审视，短时序 + 假阳性风险
3. **P3 四项缺陷** (L18-25): 4 deficiencies + closest predecessor (du2026geometric) + ecological framework gap
4. **P4 核心方案** (L27-33): multiverse analysis + 3 pitfalls + MMCT + blind spot + intervention + causality caveat + diversity-only scope
5. **贡献列表** (L36-59): Claim 3→2→1→4 顺序，含 MMCT/Shapley/regime map/blind spot/canary/intervention 全部数字
6. **Roadmap** (L61-66): 新增 `\S{sec:intervention}`

风格检查通过：无 em-dash，无解释性 en-dash，无 -ing phrase endings，无黑名单词，FDR 首次出现已展开定义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 627626,
  "duration_api_ms": 628659,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "55ee8b73-c0af-4603-89eb-8b43288477da",
  "total_cost_usd": 1.5410052,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 67415,
    "cache_read_input_tokens": 347986,
    "output_tokens": 35268,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 67415,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 329,
        "cache_read_input_tokens": 76374,
        "cache_creation_input_tokens": 2882,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2882
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3174,
      "outputTokens": 1327,
      "cacheReadInputTokens": 57332,
      "cacheCreationInputTokens": 38709,
      "webSearchRequests": 0,
      "costUSD": 0.06392845,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 35268,
      "cacheReadInputTokens": 347986,
      "cacheCreationInputTokens": 67415,
      "webSearchRequests": 0,
      "costUSD": 1.4770767500000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "38570920-f0ff-4941-ae0a-86a3cee8a0ec"
}
```

</details>

---
