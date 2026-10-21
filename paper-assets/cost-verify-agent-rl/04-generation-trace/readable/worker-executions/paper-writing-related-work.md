# paper writing related work

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260518T195445.log`
- **Structured JSON:** [`784b8b49b0964288a097.json`](../../sessions/78/784b8b49b0964288a097.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1",
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
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
  "uuid": "c3a82981-977a-4b64-93ec-59fac615c2aa",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1/memory/"
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
    "resetsAt": 1779149400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "12695d73-52ee-4e48-a3ba-3bfcc7be2405",
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required files in parallel: the two skill files, the current related_work.tex, and the current references.bib.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "909ea43c-1a0e-4fc7-80ee-846ca363cd77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5eiqnV7Vpm4S19kEnSKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11036,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11036
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — Read · `toolu_01Q1RwYBZ159V7yvVbbqf7Ra`</summary>

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
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "a0203dce-ee6a-4cef-b731-85813992835a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5eiqnV7Vpm4S19kEnSKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11036,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11036
      },
      "output_tokens": 21,
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

_source line 6 · 2026-05-18T19:54:55.360Z_

<details><summary>↩ Tool result · `toolu_01Q1RwYBZ159V7yvVbbqf7Ra`</summary>

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
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "813c8467-6bb9-4cb1-a99d-a4957848b31d",
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

<details open><summary>🔧 Tool call — Read · `toolu_01V1kSqF86ysAdVULTFyxBsj`</summary>

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
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "da6eae4f-1ac8-44d6-80b8-8db3d0b5a4a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5eiqnV7Vpm4S19kEnSKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11036,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11036
      },
      "output_tokens": 21,
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

_source line 8 · 2026-05-18T19:54:55.810Z_

<details><summary>↩ Tool result · `toolu_01V1kSqF86ysAdVULTFyxBsj`</summary>

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
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "3f5c97ae-ae41-410d-80a9-75fb2fec25bc",
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

<details open><summary>🔧 Tool call — Read · `toolu_012ngkM8AN84mf94TLwNwSNb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "6aa743ce-9500-4d13-942f-041c814c61bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5eiqnV7Vpm4S19kEnSKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11036,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11036
      },
      "output_tokens": 21,
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

_source line 10 · 2026-05-18T19:54:56.280Z_

<details><summary>↩ Tool result · `toolu_012ngkM8AN84mf94TLwNwSNb`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL Training for LLM Agents.}
5	The ReAct paradigm~\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. DigiRL~\cite{digiRL2024} demonstrates autonomous online RL for device-control agents, achieving substantial gains over supervised fine-tuning. WebAgent-R1~\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechanism itself as a source of systematic sign misattribution, which is the structural failure we identify and formalize.
6	
7	\paragraph{Credit Assignment in Reinforcement Learning.}
8	The temporal credit assignment problem has a long history. REINFORCE~\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\cite{schulman2017ppo} reduces variance through a learned value function and clipped surrogate objectives. Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} interpolates between one-step bootstrap and Monte Carlo returns via the $\lambda$ parameter, offering a continuous spectrum from TD(0) to full-episode credit. The TD($\lambda$) family~\cite{sutton1988td} established this interpolation in the tabular setting. In the LLM agent context, process reward models provide step-level supervision: AgentPRM~\cite{choudhury2025agentprm,xi2025agentprm} estimates per-step value through Monte Carlo rollouts or TD-based estimation with GAE. SkillMaster~\cite{skillmaster2026} proposes DualAdv-GRPO, which separately estimates advantages for task-solving and skill-editing decisions. In cooperative multi-agent RL, the analogous problem of shared team reward has been addressed through counterfactual baselines (COMA~\cite{foerster2018coma}) and value decomposition (QMIX~\cite{rashid2018qmix}), which estimate individual agent contributions to the team outcome. Episode-level GRPO, as we advocate, is equivalent to GAE(1,1) without a critic: it assigns uniform advantage across all steps, forgoing per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard adaptation of GRPO (step-independent windowing) produces catastrophic sign errors in multi-turn settings.
9	
10	\paragraph{Selective Verification and Adaptive Computation.}
11	A growing body of work trains models to allocate computation adaptively rather than uniformly. In the reasoning domain, Thinkless~\cite{du2025thinkless} introduces an RL-trained control token that decides whether to invoke extended thinking for each query. AutoThink~\cite{tu2025autothink} uses multi-stage RL to shape when reasoning-capable models activate their chain-of-thought. SelfBudgeter~\cite{selfbudgeter2025} frames adaptive computation as token budget allocation trained via budget-guided GRPO. In the agent domain, ARES~\cite{yang2026ares} trains an SFT-initialized router that selects reasoning effort levels per step, refined via GRPO with a combined outcome and token-efficiency reward. Agent-Omit~\cite{agent-omit2026} learns to omit redundant thoughts and observations through agentic RL, reducing context length without sacrificing performance. Sherlock~\cite{sherlock2025} performs selective verification at the workflow level through offline counterfactual analysis and speculative execution. Derailer-Rerailer~\cite{wan2025derailer-rerailer} detects instability triggers in reasoning chains and invokes targeted verification. These approaches operate at the reasoning-token level (Thinkless, AutoThink, SelfBudgeter), workflow-DAG level (Sherlock), or use heuristic triggers (Derailer-Rerailer) and SFT-initialized routers (ARES). Our selective verification differs in scope and mechanism: it makes a binary verify-or-skip decision at each agent interaction step, trained end-to-end via RL with an action-change informativeness signal that requires no external annotations or heuristic design.
12	
13	\paragraph{Self-Verification and Self-Correction.}
14	Self-verification has received significant attention as a mechanism for improving LLM reliability. Kamoi et al.~\cite{kamoi2024self-correction-survey} survey self-correction in LLMs and establish that pure intrinsic self-correction (without external feedback) is unreliable across most settings. Long et al.~\cite{long2026selfverification} quantify the verification dilemma empirically: over 90\% of self-verification instances are confirmatory, with only approximately 2\% producing corrective changes. CorrectBench~\cite{tie2025correctbench} further demonstrates that uniform self-correction exhibits diminishing returns, as models repeatedly ``correct'' already-correct answers. VerifiAgent~\cite{verifiagent2025} proposes a unified verification framework with meta-verification and tool-based adaptive strategies, focusing on improving verification quality through better methods. These findings collectively establish two facts: verification quality is limited by confirmatory bias, and uniform application of verification wastes computation on uninformative instances. Our work addresses a complementary question: given that most verification is confirmatory, \textit{when} should an agent verify? The 90\% confirmatory rate reported by Long et al. directly motivates learning a selective policy that triggers verification only at steps where action change is likely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "8c0c913d-64f7-47dd-92e0-ecb90e798ae7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for LLM Agents.}\nThe ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents, achieving substantial gains over supervised fine-tuning. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechanism itself as a source of systematic sign misattribution, which is the structural failure we identify and formalize.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nThe temporal credit assignment problem has a long history. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance through a learned value function and clipped surrogate objectives. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} interpolates between one-step bootstrap and Monte Carlo returns via the $\\lambda$ parameter, offering a continuous spectrum from TD(0) to full-episode credit. The TD($\\lambda$) family~\\cite{sutton1988td} established this interpolation in the tabular setting. In the LLM agent context, process reward models provide step-level supervision: AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates per-step value through Monte Carlo rollouts or TD-based estimation with GAE. SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO, which separately estimates advantages for task-solving and skill-editing decisions. In cooperative multi-agent RL, the analogous problem of shared team reward has been addressed through counterfactual baselines (COMA~\\cite{foerster2018coma}) and value decomposition (QMIX~\\cite{rashid2018qmix}), which estimate individual agent contributions to the team outcome. Episode-level GRPO, as we advocate, is equivalent to GAE(1,1) without a critic: it assigns uniform advantage across all steps, forgoing per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard adaptation of GRPO (step-independent windowing) produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Selective Verification and Adaptive Computation.}\nA growing body of work trains models to allocate computation adaptively rather than uniformly. In the reasoning domain, Thinkless~\\cite{du2025thinkless} introduces an RL-trained control token that decides whether to invoke extended thinking for each query. AutoThink~\\cite{tu2025autothink} uses multi-stage RL to shape when reasoning-capable models activate their chain-of-thought. SelfBudgeter~\\cite{selfbudgeter2025} frames adaptive computation as token budget allocation trained via budget-guided GRPO. In the agent domain, ARES~\\cite{yang2026ares} trains an SFT-initialized router that selects reasoning effort levels per step, refined via GRPO with a combined outcome and token-efficiency reward. Agent-Omit~\\cite{agent-omit2026} learns to omit redundant thoughts and observations through agentic RL, reducing context length without sacrificing performance. Sherlock~\\cite{sherlock2025} performs selective verification at the workflow level through offline counterfactual analysis and speculative execution. Derailer-Rerailer~\\cite{wan2025derailer-rerailer} detects instability triggers in reasoning chains and invokes targeted verification. These approaches operate at the reasoning-token level (Thinkless, AutoThink, SelfBudgeter), workflow-DAG level (Sherlock), or use heuristic triggers (Derailer-Rerailer) and SFT-initialized routers (ARES). Our selective verification differs in scope and mechanism: it makes a binary verify-or-skip decision at each agent interaction step, trained end-to-end via RL with an action-change informativeness signal that requires no external annotations or heuristic design.\n\n\\paragraph{Self-Verification and Self-Correction.}\nSelf-verification has received significant attention as a mechanism for improving LLM reliability. Kamoi et al.~\\cite{kamoi2024self-correction-survey} survey self-correction in LLMs and establish that pure intrinsic self-correction (without external feedback) is unreliable across most settings. Long et al.~\\cite{long2026selfverification} quantify the verification dilemma empirically: over 90\\% of self-verification instances are confirmatory, with only approximately 2\\% producing corrective changes. CorrectBench~\\cite{tie2025correctbench} further demonstrates that uniform self-correction exhibits diminishing returns, as models repeatedly ``correct'' already-correct answers. VerifiAgent~\\cite{verifiagent2025} proposes a unified verification framework with meta-verification and tool-based adaptive strategies, focusing on improving verification quality through better methods. These findings collectively establish two facts: verification quality is limited by confirmatory bias, and uniform application of verification wastes computation on uninformative instances. Our work addresses a complementary question: given that most verification is confirmatory, \\textit{when} should an agent verify? The 90\\% confirmatory rate reported by Long et al. directly motivates learning a selective policy that triggers verification only at steps where action change is likely.",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Y9FGkqyqgartJ67NeJsevW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "82e3e312-ef84-4316-8848-31e224bea1d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5eiqnV7Vpm4S19kEnSKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11036,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11036
      },
      "output_tokens": 21,
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

_source line 12 · 2026-05-18T19:54:56.542Z_

<details><summary>↩ Tool result · `toolu_01Y9FGkqyqgartJ67NeJsevW`</summary>

```text
1	@inproceedings{shridhar2021alfworld,
2	  title     = {{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},
3	  author    = {Shridhar, Mohit and Yuan, Xingdi and C\^{o}t\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},
4	  booktitle = {International Conference on Learning Representations},
5	  year      = {2021},
6	}
7	
8	@inproceedings{agent-omit2026,
9	  title     = {Agent-Omit: Training Efficient {LLM} Agents for Adaptive Thought and Observation Omission via Agentic {RL}},
10	  author    = {Ning, Yansong and Fang, Jun and Tan, Naiqiang and Liu, Hao},
11	  booktitle = {Proceedings of the International Conference on Machine Learning},
12	  year      = {2026},
13	}
14	
15	@article{choudhury2025agentprm,
16	  title   = {Process Reward Models for {LLM} Agents: Practical Framework and Directions},
17	  author  = {Choudhury, Sanjiban},
18	  journal = {arXiv preprint arXiv:2502.10325},
19	  year    = {2025},
20	}
21	
22	@article{dapo2025,
23	  title   = {{DAPO}: An Open-Source {LLM} Reinforcement Learning System at Scale},
24	  author  = {Yu, Qiying and Zhang, Zheng and Zhu, Ruofei and Yuan, Yufeng and Zuo, Xiaochen and Yue, Yu and Dai, Weinan and Fan, Tiantian and Liu, Gaohong and Liu, Lingjun and Liu, Xin and Lin, Haibin and Lin, Zhiqi and Ma, Bole and Sheng, Guangming and Tong, Yuxuan and Zhang, Chi and Zhang, Mofan and Zhang, Wang and Zhu, Hang and Zhu, Jinhua and Chen, Jiaze and Chen, Jiangjie and Wang, Chengyi and Yu, Hongli and Song, Yuxuan and Wei, Xiangpeng and Zhou, Hao and Liu, Jingjing and Ma, Wei-Ying and Zhang, Ya-Qin and Yan, Lin and Qiao, Mu and Wu, Yonghui and Wang, Mingxuan},
25	  journal = {arXiv preprint arXiv:2503.14476},
26	  year    = {2025},
27	}
28	
29	@inproceedings{foerster2018coma,
30	  title     = {Counterfactual Multi-Agent Policy Gradients},
31	  author    = {Foerster, Jakob and Farquhar, Gregory and Afouras, Triantafyllos and Nardelli, Nantas and Whiteson, Shimon},
32	  booktitle = {AAAI Conference on Artificial Intelligence},
33	  year      = {2018},
34	}
35	
36	@inproceedings{digiRL2024,
37	  title     = {{DigiRL}: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning},
38	  author    = {Bai, Hao and Zhou, Yifei and Cemri, Mert and Pan, Jiayi and Suhr, Alane and Levine, Sergey and Kumar, Aviral},
39	  booktitle = {Advances in Neural Information Processing Systems},
40	  year      = {2024},
41	}
42	
43	@inproceedings{du2025thinkless,
44	  title     = {Thinkless: {LLM} Learns When to Think},
45	  author    = {Fang, Gongfan and Ma, Xinyin and Wang, Xinchao},
46	  booktitle = {Advances in Neural Information Processing Systems},
47	  year      = {2025},
48	}
49	
50	@inproceedings{feng2025gigpo,
51	  title     = {{GiGPO}: Group-in-Group Policy Optimization for {LLM} Agent Training},
52	  author    = {Feng, Lang and Xue, Zhenghai and Liu, Tingcong and An, Bo},
53	  booktitle = {Advances in Neural Information Processing Systems},
54	  year      = {2025},
55	}
56	
57	@article{hcapo2026,
58	  title   = {{HCAPO}: Hindsight Credit Assignment for Long-Horizon {LLM} Agents},
59	  author  = {Tan, Hui-Ze and Yang, Xiao-Wen and Chen, Hao and Shao, Jie-Jing and Wen, Yi and Shen, Yuteng and Luo, Weihong and Du, Xiku and Guo, Lan-Zhe and Li, Yu-Feng},
60	  journal = {arXiv preprint arXiv:2603.08754},
61	  year    = {2026},
62	}
63	
64	@article{kamoi2024self-correction-survey,
65	  title   = {When Can {LLMs} Actually Correct Their Own Mistakes? {A} Critical Survey of Self-Correction of {LLMs}},
66	  author  = {Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui},
67	  journal = {arXiv preprint arXiv:2406.01297},
68	  year    = {2024},
69	}
70	
71	@inproceedings{kim2025reflact,
72	  title     = {{ReflAct}: World-Grounded Decision Making in {LLM} Agents via Goal-State Reflection},
73	  author    = {Kim, Jeonghye and Rhee, Sojeong and Kim, Minbeom and Kim, Dohyung and Lee, Sangmook and Sung, Youngchul and Jung, Kyomin},
74	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
75	  year      = {2025},
76	}
77	
78	@article{li2025sorl,
79	  title   = {{SORL}: Stabilizing Off-Policy {RL} for Long-Horizon Agent Training},
80	  author  = {Li, Chenliang and Elmahdy, Adel and Boyd, Alex and Wang, Zhongruo and Zeng, Siliang and Garcia, Alfredo and Bhatia, Parminder and Kass-Hout, Taha and Xiao, Cao and Hong, Mingyi},
81	  journal = {arXiv preprint arXiv:2511.20718},
82	  year    = {2025},
83	}
84	
85	@article{long2026selfverification,
86	  title   = {Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in {LLM} Reasoning},
87	  author  = {Long, Quanyu and Jiang, Kai Jie and Chen, Jianda and Guo, Xu and Gan, Leilei and Wang, Wenya},
88	  journal = {arXiv preprint arXiv:2602.03485},
89	  year    = {2026},
90	}
91	
92	@inproceedings{rashid2018qmix,
93	  title     = {{QMIX}: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning},
94	  author    = {Rashid, Tabish and Samvelyan, Mikayel and De Witt, Christian Schroeder and Farquhar, Gregory and Foerster, Jakob and Whiteson, Shimon},
95	  booktitle = {International Conference on Machine Learning},
96	  year      = {2018},
97	}
98	
99	@article{ragen2025,
100	  title   = {{RAGEN}: Understanding Self-Evolution in {LLM} Agents via Multi-Turn Reinforcement Learning},
101	  author  = {Wang, Zihan and Wang, Kangrui and Wang, Qineng and Zhang, Pingyue and Li, Linjie and Yang, Zhengyuan and Jin, Xing and Yu, Kefan and Nguyen, Minh Nhat and Liu, Licheng and Gottlieb, Eli and Lu, Yiping and Cho, Kyunghyun and Wu, Jiajun and Li, Fei-Fei and Wang, Lijuan and Choi, Yejin and Li, Manling},
102	  journal = {arXiv preprint arXiv:2504.20073},
103	  year    = {2025},
104	}
105	
106	@inproceedings{yao2023react,
107	  title     = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
108	  author    = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
109	  booktitle = {International Conference on Learning Representations},
110	  year      = {2023},
111	}
112	
113	@inproceedings{schulman2016gae,
114	  title     = {High-Dimensional Continuous Control Using Generalized Advantage Estimation},
115	  author    = {Schulman, John and Moritz, Philipp and Levine, Sergey and Jordan, Michael and Abbeel, Pieter},
116	  booktitle = {Proceedings of the International Conference on Learning Representations},
117	  year      = {2016},
118	}
119	
120	@article{schulman2017ppo,
121	  title   = {Proximal Policy Optimization Algorithms},
122	  author  = {Schulman, John and Wolski, Filip and Dhariwal, Prafulla and Radford, Alec and Klimov, Oleg},
123	  journal = {arXiv preprint arXiv:1707.06347},
124	  year    = {2017},
125	}
126	
127	@article{selfbudgeter2025,
128	  title   = {{SelfBudgeter}: Adaptive Token Allocation for Efficient {LLM} Reasoning},
129	  author  = {Li, Zheng and Dong, Qingxiu and Ma, Jingyuan and Zhang, Di and Jia, Kai and Sui, Zhifang},
130	  journal = {arXiv preprint arXiv:2505.11274},
131	  year    = {2025},
132	}
133	
134	@article{selfguide2026,
135	  title   = {Co-Evolution of Policy and Internal Reward for Language Agents},
136	  author  = {Wang, Xinyu and Wu, Hanwei and Song, Jingwei and Zhang, Shuyuan and Zhang, Jiayi and Kong, Fanqi and Kwok, Tung Sum Thomas and Chang, Xiao-Wen and Luo, Yuyu and Wu, Chenglin and Liu, Bang},
137	  journal = {arXiv preprint arXiv:2604.03098},
138	  year    = {2026},
139	}
140	
141	@article{shao2024deepseekmath,
142	  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},
143	  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
144	  journal = {arXiv preprint arXiv:2402.03300},
145	  year    = {2024},
146	}
147	
148	@article{sherlock2025,
149	  title   = {Sherlock: Reliable and Efficient Agentic Workflow Execution},
150	  author  = {Ro, Yeonju and Qiu, Haoran and Goiri, {\'\I}{\~n}igo and Fonseca, Rodrigo and Bianchini, Ricardo and Akella, Aditya and Wang, Zhangyang and Erez, Mattan and Choukse, Esha},
151	  journal = {arXiv preprint arXiv:2511.00330},
152	  year    = {2025},
153	}
154	
155	@article{skillmaster2026,
156	  title   = {{SkillMaster}: Toward Autonomous Skill Mastery in {LLM} Agents},
157	  author  = {Yang, Min and Piao, Jinghua and Xia, Xu and Lan, Xiaochong and Chen, Jiaju and Gong, Yongshun and Li, Yong},
158	  journal = {arXiv preprint arXiv:2605.08693},
159	  year    = {2026},
160	}
161	
162	@inproceedings{spear2025,
163	  title     = {Learn the Ropes, Then Trust the Wins: Self-Imitation with Progressive Exploration for Agentic Reinforcement Learning},
164	  author    = {Qin, Yulei and Tan, Xiaoyu and He, Zhengbao and Li, Gang and Lin, Haojia and Li, Zongyi and Xu, Zihan and Shi, Yuchen and Cai, Siqi and Rui, Renting and Cai, Shaofei and Cai, Yuzheng and Zhang, Xuan and Ye, Sheng and Li, Ke and Sun, Xing},
165	  booktitle = {Proceedings of the International Conference on Learning Representations},
166	  year      = {2026},
167	}
168	
169	@article{sutton1988td,
170	  title   = {Learning to Predict by the Methods of Temporal Differences},
171	  author  = {Sutton, Richard S.},
172	  journal = {Machine Learning},
173	  volume  = {3},
174	  number  = {1},
175	  pages   = {9--44},
176	  year    = {1988},
177	}
178	
179	@inproceedings{tie2025correctbench,
180	  title     = {Can {LLMs} Correct Themselves? {A} Benchmark of Self-Correction in {LLMs}},
181	  author    = {Tie, Guiyao and Yuan, Zenghui and Zhao, Zeli and Hu, Chaoran and Gu, Tianhe and Zhang, Ruihang and Zhang, Sizhe and Wu, Junran and Tu, Xiaoyue and Jin, Ming and Wen, Qingsong and Chen, Lixing and Zhou, Pan and Sun, Lichao},
182	  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},
183	  year      = {2025},
184	}
185	
186	@inproceedings{tu2025autothink,
187	  title     = {Learning When to Think: Shaping Adaptive Reasoning in {R1}-Style Models via Multi-Stage {RL}},
188	  author    = {Tu, Songjun and Lin, Jiahao and Zhang, Qichao and Tian, Xiangyu and Li, Linjing and Lan, Xiangyuan and Zhao, Dongbin},
189	  booktitle = {Advances in Neural Information Processing Systems},
190	  year      = {2025},
191	}
192	
193	@inproceedings{verifiagent2025,
194	  title     = {{VerifiAgent}: A Unified Verification Agent in Language Model Reasoning},
195	  author    = {Han, Jiuzhou and Buntine, Wray and Shareghi, Ehsan},
196	  booktitle = {Findings of the Conference on Empirical Methods in Natural Language Processing},
197	  year      = {2025},
198	}
199	
200	@inproceedings{wan2025derailer-rerailer,
201	  title     = {Derailer-Rerailer: Adaptive Verification for Efficient and Reliable {LM} Reasoning},
202	  author    = {Wan, Guangya and Wu, Yuqi and Wang, Hao and Zhao, Shengming and Chen, Jie and Li, Sheng},
203	  booktitle = {Findings of the Annual Meeting of the Association for Computational Linguistics},
204	  year      = {2025},
205	}
206	
207	@inproceedings{wang2022scienceworld,
208	  title     = {{ScienceWorld}: Is Your Agent Smarter Than a 5th Grader?},
209	  author    = {Wang, Ruoyao and Jansen, Peter and C\^{o}t\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
210	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
211	  year      = {2022},
212	}
213	
214	@inproceedings{yao2022webshop,
215	  title     = {{WebShop}: Towards Scalable Real-World Web Interaction with Grounded Language Agents},
216	  author    = {Yao, Shunyu and Chen, Howard and Yang, John and Narasimhan, Karthik},
217	  booktitle = {Advances in Neural Information Processing Systems},
218	  year      = {2022},
219	}
220	
221	@inproceedings{zhou2024webarena,
222	  title     = {{WebArena}: A Realistic Web Environment for Building Autonomous Agents},
223	  author    = {Zhou, Shuyan and Xu, Frank F. and Zhu, Hao and Zhou, Xuhui and Lo, Robert and Sridhar, Abishek and Cheng, Xianyi and Ou, Tianyue and Bisk, Yonatan and Fried, Daniel and Alon, Uri and Neubig, Graham},
224	  booktitle = {International Conference on Learning Representations},
225	  year      = {2024},
226	}
227	
228	@inproceedings{wei2025webagent-r1,
229	  title     = {{WebAgent-R1}: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning},
230	  author    = {Wei, Zhepei and Yao, Wenlin and Liu, Yao and Zhang, Weizhi and Lu, Qin and Qiu, Liang and Yu, Changlong and Xu, Puyang and Zhang, Chao and Yin, Bing and Yun, Hyokun and Li, Lihong},
231	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
232	  year      = {2025},
233	}
234	
235	@article{williams1992reinforce,
236	  title   = {Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning},
237	  author  = {Williams, Ronald J.},
238	  journal = {Machine Learning},
239	  volume  = {8},
240	  number  = {3--4},
241	  pages   = {229--256},
242	  year    = {1992},
243	}
244	
245	@inproceedings{xi2025agentprm,
246	  title     = {{AgentPRM}: Process Reward Models for {LLM} Agents via Step-Wise Promise and Progress},
247	  author    = {Xi, Zhiheng and Liao, Chenyang and Li, Guanyu and Yang, Yajie and Chen, Wenxiang and Zhang, Zhihao and Wang, Binghai and Jin, Senjie and Zhou, Yuhao and Guan, Jian and Wu, Wei and Ji, Tao and Gui, Tao and Zhang, Qi and Huang, Xuanjing},
248	  booktitle = {Proceedings of the {ACM} Web Conference},
249	  year      = {2026},
250	}
251	
252	@article{yang2026ares,
253	  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},
254	  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},
255	  journal = {arXiv preprint arXiv:2603.07915},
256	  year    = {2026},
257	}
258	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "c0145a44-e981-4ea4-884d-51b06c75c4f0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
      "content": "@inproceedings{shridhar2021alfworld,\n  title     = {{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},\n  author    = {Shridhar, Mohit and Yuan, Xingdi and C\\^{o}t\\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2021},\n}\n\n@inproceedings{agent-omit2026,\n  title     = {Agent-Omit: Training Efficient {LLM} Agents for Adaptive Thought and Observation Omission via Agentic {RL}},\n  author    = {Ning, Yansong and Fang, Jun and Tan, Naiqiang and Liu, Hao},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year      = {2026},\n}\n\n@article{choudhury2025agentprm,\n  title   = {Process Reward Models for {LLM} Agents: Practical Framework and Directions},\n  author  = {Choudhury, Sanjiban},\n  journal = {arXiv preprint arXiv:2502.10325},\n  year    = {2025},\n}\n\n@article{dapo2025,\n  title   = {{DAPO}: An Open-Source {LLM} Reinforcement Learning System at Scale},\n  author  = {Yu, Qiying and Zhang, Zheng and Zhu, Ruofei and Yuan, Yufeng and Zuo, Xiaochen and Yue, Yu and Dai, Weinan and Fan, Tiantian and Liu, Gaohong and Liu, Lingjun and Liu, Xin and Lin, Haibin and Lin, Zhiqi and Ma, Bole and Sheng, Guangming and Tong, Yuxuan and Zhang, Chi and Zhang, Mofan and Zhang, Wang and Zhu, Hang and Zhu, Jinhua and Chen, Jiaze and Chen, Jiangjie and Wang, Chengyi and Yu, Hongli and Song, Yuxuan and Wei, Xiangpeng and Zhou, Hao and Liu, Jingjing and Ma, Wei-Ying and Zhang, Ya-Qin and Yan, Lin and Qiao, Mu and Wu, Yonghui and Wang, Mingxuan},\n  journal = {arXiv preprint arXiv:2503.14476},\n  year    = {2025},\n}\n\n@inproceedings{foerster2018coma,\n  title     = {Counterfactual Multi-Agent Policy Gradients},\n  author    = {Foerster, Jakob and Farquhar, Gregory and Afouras, Triantafyllos and Nardelli, Nantas and Whiteson, Shimon},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n  year      = {2018},\n}\n\n@inproceedings{digiRL2024,\n  title     = {{DigiRL}: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning},\n  author    = {Bai, Hao and Zhou, Yifei and Cemri, Mert and Pan, Jiayi and Suhr, Alane and Levine, Sergey and Kumar, Aviral},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n}\n\n@inproceedings{du2025thinkless,\n  title     = {Thinkless: {LLM} Learns When to Think},\n  author    = {Fang, Gongfan and Ma, Xinyin and Wang, Xinchao},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n}\n\n@inproceedings{feng2025gigpo,\n  title     = {{GiGPO}: Group-in-Group Policy Optimization for {LLM} Agent Training},\n  author    = {Feng, Lang and Xue, Zhenghai and Liu, Tingcong and An, Bo},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n}\n\n@article{hcapo2026,\n  title   = {{HCAPO}: Hindsight Credit Assignment for Long-Horizon {LLM} Agents},\n  author  = {Tan, Hui-Ze and Yang, Xiao-Wen and Chen, Hao and Shao, Jie-Jing and Wen, Yi and Shen, Yuteng and Luo, Weihong and Du, Xiku and Guo, Lan-Zhe and Li, Yu-Feng},\n  journal = {arXiv preprint arXiv:2603.08754},\n  year    = {2026},\n}\n\n@article{kamoi2024self-correction-survey,\n  title   = {When Can {LLMs} Actually Correct Their Own Mistakes? {A} Critical Survey of Self-Correction of {LLMs}},\n  author  = {Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui},\n  journal = {arXiv preprint arXiv:2406.01297},\n  year    = {2024},\n}\n\n@inproceedings{kim2025reflact,\n  title     = {{ReflAct}: World-Grounded Decision Making in {LLM} Agents via Goal-State Reflection},\n  author    = {Kim, Jeonghye and Rhee, Sojeong and Kim, Minbeom and Kim, Dohyung and Lee, Sangmook and Sung, Youngchul and Jung, Kyomin},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year      = {2025},\n}\n\n@article{li2025sorl,\n  title   = {{SORL}: Stabilizing Off-Policy {RL} for Long-Horizon Agent Training},\n  author  = {Li, Chenliang and Elmahdy, Adel and Boyd, Alex and Wang, Zhongruo and Zeng, Siliang and Garcia, Alfredo and Bhatia, Parminder and Kass-Hout, Taha and Xiao, Cao and Hong, Mingyi},\n  journal = {arXiv preprint arXiv:2511.20718},\n  year    = {2025},\n}\n\n@article{long2026selfverification,\n  title   = {Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in {LLM} Reasoning},\n  author  = {Long, Quanyu and Jiang, Kai Jie and Chen, Jianda and Guo, Xu and Gan, Leilei and Wang, Wenya},\n  journal = {arXiv preprint arXiv:2602.03485},\n  year    = {2026},\n}\n\n@inproceedings{rashid2018qmix,\n  title     = {{QMIX}: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning},\n  author    = {Rashid, Tabish and Samvelyan, Mikayel and De Witt, Christian Schroeder and Farquhar, Gregory and Foerster, Jakob and Whiteson, Shimon},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2018},\n}\n\n@article{ragen2025,\n  title   = {{RAGEN}: Understanding Self-Evolution in {LLM} Agents via Multi-Turn Reinforcement Learning},\n  author  = {Wang, Zihan and Wang, Kangrui and Wang, Qineng and Zhang, Pingyue and Li, Linjie and Yang, Zhengyuan and Jin, Xing and Yu, Kefan and Nguyen, Minh Nhat and Liu, Licheng and Gottlieb, Eli and Lu, Yiping and Cho, Kyunghyun and Wu, Jiajun and Li, Fei-Fei and Wang, Lijuan and Choi, Yejin and Li, Manling},\n  journal = {arXiv preprint arXiv:2504.20073},\n  year    = {2025},\n}\n\n@inproceedings{yao2023react,\n  title     = {{ReAct}: Synergizing Reasoning and Acting in Language Models},\n  author    = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2023},\n}\n\n@inproceedings{schulman2016gae,\n  title     = {High-Dimensional Continuous Control Using Generalized Advantage Estimation},\n  author    = {Schulman, John and Moritz, Philipp and Levine, Sergey and Jordan, Michael and Abbeel, Pieter},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year      = {2016},\n}\n\n@article{schulman2017ppo,\n  title   = {Proximal Policy Optimization Algorithms},\n  author  = {Schulman, John and Wolski, Filip and Dhariwal, Prafulla and Radford, Alec and Klimov, Oleg},\n  journal = {arXiv preprint arXiv:1707.06347},\n  year    = {2017},\n}\n\n@article{selfbudgeter2025,\n  title   = {{SelfBudgeter}: Adaptive Token Allocation for Efficient {LLM} Reasoning},\n  author  = {Li, Zheng and Dong, Qingxiu and Ma, Jingyuan and Zhang, Di and Jia, Kai and Sui, Zhifang},\n  journal = {arXiv preprint arXiv:2505.11274},\n  year    = {2025},\n}\n\n@article{selfguide2026,\n  title   = {Co-Evolution of Policy and Internal Reward for Language Agents},\n  author  = {Wang, Xinyu and Wu, Hanwei and Song, Jingwei and Zhang, Shuyuan and Zhang, Jiayi and Kong, Fanqi and Kwok, Tung Sum Thomas and Chang, Xiao-Wen and Luo, Yuyu and Wu, Chenglin and Liu, Bang},\n  journal = {arXiv preprint arXiv:2604.03098},\n  year    = {2026},\n}\n\n@article{shao2024deepseekmath,\n  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal = {arXiv preprint arXiv:2402.03300},\n  year    = {2024},\n}\n\n@article{sherlock2025,\n  title   = {Sherlock: Reliable and Efficient Agentic Workflow Execution},\n  author  = {Ro, Yeonju and Qiu, Haoran and Goiri, {\\'\\I}{\\~n}igo and Fonseca, Rodrigo and Bianchini, Ricardo and Akella, Aditya and Wang, Zhangyang and Erez, Mattan and Choukse, Esha},\n  journal = {arXiv preprint arXiv:2511.00330},\n  year    = {2025},\n}\n\n@article{skillmaster2026,\n  title   = {{SkillMaster}: Toward Autonomous Skill Mastery in {LLM} Agents},\n  author  = {Yang, Min and Piao, Jinghua and Xia, Xu and Lan, Xiaochong and Chen, Jiaju and Gong, Yongshun and Li, Yong},\n  journal = {arXiv preprint arXiv:2605.08693},\n  year    = {2026},\n}\n\n@inproceedings{spear2025,\n  title     = {Learn the Ropes, Then Trust the Wins: Self-Imitation with Progressive Exploration for Agentic Reinforcement Learning},\n  author    = {Qin, Yulei and Tan, Xiaoyu and He, Zhengbao and Li, Gang and Lin, Haojia and Li, Zongyi and Xu, Zihan and Shi, Yuchen and Cai, Siqi and Rui, Renting and Cai, Shaofei and Cai, Yuzheng and Zhang, Xuan and Ye, Sheng and Li, Ke and Sun, Xing},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year      = {2026},\n}\n\n@article{sutton1988td,\n  title   = {Learning to Predict by the Methods of Temporal Differences},\n  author  = {Sutton, Richard S.},\n  journal = {Machine Learning},\n  volume  = {3},\n  number  = {1},\n  pages   = {9--44},\n  year    = {1988},\n}\n\n@inproceedings{tie2025correctbench,\n  title     = {Can {LLMs} Correct Themselves? {A} Benchmark of Self-Correction in {LLMs}},\n  author    = {Tie, Guiyao and Yuan, Zenghui and Zhao, Zeli and Hu, Chaoran and Gu, Tianhe and Zhang, Ruihang and Zhang, Sizhe and Wu, Junran and Tu, Xiaoyue and Jin, Ming and Wen, Qingsong and Chen, Lixing and Zhou, Pan and Sun, Lichao},\n  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},\n  year      = {2025},\n}\n\n@inproceedings{tu2025autothink,\n  title     = {Learning When to Think: Shaping Adaptive Reasoning in {R1}-Style Models via Multi-Stage {RL}},\n  author    = {Tu, Songjun and Lin, Jiahao and Zhang, Qichao and Tian, Xiangyu and Li, Linjing and Lan, Xiangyuan and Zhao, Dongbin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n}\n\n@inproceedings{verifiagent2025,\n  title     = {{VerifiAgent}: A Unified Verification Agent in Language Model Reasoning},\n  author    = {Han, Jiuzhou and Buntine, Wray and Shareghi, Ehsan},\n  booktitle = {Findings of the Conference on Empirical Methods in Natural Language Processing},\n  year      = {2025},\n}\n\n@inproceedings{wan2025derailer-rerailer,\n  title     = {Derailer-Rerailer: Adaptive Verification for Efficient and Reliable {LM} Reasoning},\n  author    = {Wan, Guangya and Wu, Yuqi and Wang, Hao and Zhao, Shengming and Chen, Jie and Li, Sheng},\n  booktitle = {Findings of the Annual Meeting of the Association for Computational Linguistics},\n  year      = {2025},\n}\n\n@inproceedings{wang2022scienceworld,\n  title     = {{ScienceWorld}: Is Your Agent Smarter Than a 5th Grader?},\n  author    = {Wang, Ruoyao and Jansen, Peter and C\\^{o}t\\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2022},\n}\n\n@inproceedings{yao2022webshop,\n  title     = {{WebShop}: Towards Scalable Real-World Web Interaction with Grounded Language Agents},\n  author    = {Yao, Shunyu and Chen, Howard and Yang, John and Narasimhan, Karthik},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n}\n\n@inproceedings{zhou2024webarena,\n  title     = {{WebArena}: A Realistic Web Environment for Building Autonomous Agents},\n  author    = {Zhou, Shuyan and Xu, Frank F. and Zhu, Hao and Zhou, Xuhui and Lo, Robert and Sridhar, Abishek and Cheng, Xianyi and Ou, Tianyue and Bisk, Yonatan and Fried, Daniel and Alon, Uri and Neubig, Graham},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{wei2025webagent-r1,\n  title     = {{WebAgent-R1}: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning},\n  author    = {Wei, Zhepei and Yao, Wenlin and Liu, Yao and Zhang, Weizhi and Lu, Qin and Qiu, Liang and Yu, Changlong and Xu, Puyang and Zhang, Chao and Yin, Bing and Yun, Hyokun and Li, Lihong},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year      = {2025},\n}\n\n@article{williams1992reinforce,\n  title   = {Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning},\n  author  = {Williams, Ronald J.},\n  journal = {Machine Learning},\n  volume  = {8},\n  number  = {3--4},\n  pages   = {229--256},\n  year    = {1992},\n}\n\n@inproceedings{xi2025agentprm,\n  title     = {{AgentPRM}: Process Reward Models for {LLM} Agents via Step-Wise Promise and Progress},\n  author    = {Xi, Zhiheng and Liao, Chenyang and Li, Guanyu and Yang, Yajie and Chen, Wenxiang and Zhang, Zhihao and Wang, Binghai and Jin, Senjie and Zhou, Yuhao and Guan, Jian and Wu, Wei and Ji, Tao and Gui, Tao and Zhang, Qi and Huang, Xuanjing},\n  booktitle = {Proceedings of the {ACM} Web Conference},\n  year      = {2026},\n}\n\n@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}\n",
      "numLines": 258,
      "startLine": 1,
      "totalLines": 258
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
Now I have all the information I need. Let me analyze what's already in the bib file to avoid duplicates, then write the new related_work.tex and add missing bib entries.

Existing bib entries (keys):
- shridhar2021alfworld
- agent-omit2026
- choudhury2025agentprm
- dapo2025
- foerster2018coma
- digiRL2024
- du2025thinkless
- feng2025gigpo
- hcapo2026
- kamoi2024self-correction-survey
- kim2025reflact


- li2025sorl
- long2026selfverification
- rashid2018qmix
- ragen2025
- yao2023react
- schulman2016gae
- schulman2017ppo
- selfbudgeter2025
- selfguide2026
- shao2024deepseekmath
- sherlock2025
- skillmaster2026
- spear2025
- sutton1988td
- tie2025correctbench
- tu2025autothink
- verifiagent2025
- wan2025derailer-rerailer
- wang2022scienceworld
- yao2022
- webshop
- zhou2024webarena
- wei2025webagent-r1
- williams1992reinforce
- xi2025agentprm
- yang2026ares
- irc2026
- mcgrpo2025
- gra2025
- grpolambda2025
- oar2026
- decoupledca2026
- ragen2_2026
- grpocollapse2025
- gradientcoupling2025
- turnppo2026
- gagpo2026
- istar2025
- mtgrpo2025
- sweetrl2025
- rudder2019
- ca_survey2026

Now I'm organizing these references into the related work section with four paragraphs that align with the D073 narrative structure.

I need to keep the writing to roughly 900 words, avoid dashes except in ranges, eliminate gerund phrase endings, vary my transition words, and structure each cluster with a clear positioning sentence. I'm also tracking the specific citation constraints: GRPO-λ's value estimation error bound, OAR's reward aliasing mechanism, Decoupled-CA's under-review status, and RAGEN's collapse timing around step 170.

Writing the related_work.tex now...

**Paragraph 1** covers the algorithmic progression from ReAct through recent variants like GiGPO and WebAgent-R1. The key positioning is that while these methods refine training procedures and reward signals, they don't explain the systematic sign errors that emerge from step-independent windowing.

**Paragraph 2** traces credit assignment from foundational RL techniques like REINFORCE and PPO through modern approaches in multi-agent and LLM contexts. I'm noting AgentPRM and SkillMaster for agent-specific credit assignment, then positioning how these classical and contemporary methods address temporal credit but miss the particular failure mode we're investigating.

**Paragraph 3** focuses on multi-turn specific solutions—Turn-PPO, GAGPO, iStar, MT-GRPO, SWEET-RL—that attempt to fix credit assignment in sequential agent tasks. The distinction here is that these papers propose solutions while we're providing the mechanistic diagnosis of what's actually breaking.

**Paragraph 4** gathers independent evidence of GRPO collapse from RAGEN-2, search-based variants, and gradient coupling observations. This positioning shows our diagnosis is corroborated by separate empirical findings rather than being an isolated observation.

Now drafting the section itself. I'm establishing the ReAct framework as foundational, then explaining how GRPO was adapted to multi-turn settings through windowing approaches like RAGEN's step-independent baseline normalization. The key is showing that while subsequent work improves within this framework, the underlying mechanism we're diagnosing hasn't been addressed. I'm moving into how GiGPO estimates step-level advantages and where the existing approaches fall short. or the training pipeline at various granularities, but the core issue is that step-independent windowing itself creates systematic sign errors—a structural flaw that hasn't been diagnosed before. Now I'm reviewing how credit assignment works across the RL landscape, from REINFORCE's high-variance episode-level approach through PPO's variance reduction with learned critics, GAE's flexible interpolation between bootstrapping and Monte Carlo returns, and more recent methods like RUDDER that decompose delayed rewards through sequence modeling, though each introduces its own trade-offs.

For LLM agents specifically, methods like AgentPRM use Monte Carlo rollouts to estimate step-level values, while SkillMaster proposes separate advantage streams for task-solving versus skill-editing. In multi-agent settings, COMA and QMIX tackle the parallel problem of attributing team rewards to individuals through counterfactual reasoning and value decomposition. What's striking is that multiple independent studies now show direct evidence that step-independent credit assignment produces sign-level errors—IRC demonstrates that per-turn advantages frequently disagree in sign with outcome advantages.

Now I'm looking at empirical measurements of this problem across different approaches. MC-GRPO reports a 5% sign-flip rate that alone accounts for roughly 4% accuracy loss, while GRPO-λ proves that value estimation error grows with sequence position due to baseline bias. Several other methods—OAR, G-RA, and Decoupled-CA—identify related phenomena like reward aliasing and accumulated reward divergence, with one study finding that invalid actions compound the issue.

Our approach of using episode-level GRPO without a critic is essentially GAE(1,1)—it trades per-step granularity for correct gradient direction across the entire trajectory. The key insight isn't proposing a new algorithm but recognizing why standard practice fails catastrophically in multi-turn settings.

Looking at parallel work on multi-turn agents, Turn-PPO shows that standard GRPO actually crashes on complex environments like WebShop and Sokoban, with their proposed fixes all falling short. GiGPO takes a different approach by structuring advantages at both episode and step levels, though the ablations are still being evaluated.

Other recent methods like GAGPO, iStar, MT-GRPO, and SWEET-RL each tackle the problem differently—some using recursive TD/GAE estimation, others merging advantages at the token level or contrasting turn-level methods against outcome-only baselines. The performance gaps are striking: MT-GRPO achieves 0.50 exact match versus 0.04 for outcome-only GRPO, a 12× difference that really highlights how severe this credit assignment problem is. These works all propose solutions, and I'm building on them with a mechanistic diagnosis of two specific failure modes.

The first is policy information loss at the inference layer, and the second is advantage sign misattribution during training—both explain why step-independent windowing fails and why episode-level assignment eliminates them. Now I'm looking at independent documentation of GRPO collapse phenomena that support this analysis. RAGEN-2 provides a mathematical proof showing how advantage collapse occurs when within-prompt reward variance drops near zero, causing task-relevant gradients to vanish while KL regularization pushes the policy back toward the reference. GRPO-Collapse identifies a specific failure pattern in Search-R1 where all four tested models collapse within 300 steps, and Gradient Coupling challenges the reward miscalibration hypothesis with a different explanation.

The key insight is that flawed actions naturally have negative expected advantage, but the real problem is gradient coupling from high input similarity across consecutive steps. This expected-value perspective aligns with my per-sample sign analysis—aggregate advantages can look correct when averaged across many samples, yet individual sample signs remain nearly random under high variance, which is exactly the condition where step-independent windowing breaks down. These separate observations about advantage collapse and gradient coupling all point to the same underlying instability in multi-turn GRPO training, and my work ties them together through the dual-mechanism diagnosis while validating episode-level training as the structural solution. Now I'm verifying the citation assertions across all the methods I discussed, checking that each claim is properly grounded in the literature and that my style guidelines are met throughout the document. Once I confirm everything checks out, I'll write the files and add the bibliography entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "252b80b9-6604-494c-a675-b1f7baab21a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9zWqtzTvWoR8hdhbuj3J3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24400,
      "cache_read_input_tokens": 22737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24400
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

I'll now write the new related_work.tex and add bib entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "7def2ebc-aded-41ce-80b5-8381eaaaff2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9zWqtzTvWoR8hdhbuj3J3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24400,
      "cache_read_input_tokens": 22737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24400
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

<details open><summary>🔧 Tool call — Write · `toolu_01EASNvLQzarL2FZgDKrkDSe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for Multi-Turn LLM Agents.}\nThe ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nTemporal credit assignment spans a well-studied spectrum. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance via a learned critic and clipped surrogate objectives. GAE~\\cite{schulman2016gae} interpolates between one-step TD and Monte Carlo returns through the $\\lambda$ parameter, with TD($\\lambda$)~\\cite{sutton1988td} establishing this interpolation in the tabular setting. RUDDER~\\cite{rudder2019} decomposes delayed rewards via sequence-to-sequence modeling but introduces bias whose correction slows exponentially with horizon. For LLM agents, AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates step-level value through Monte Carlo rollouts, and SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO with separate advantages for task-solving and skill-editing. In cooperative multi-agent RL, COMA~\\cite{foerster2018coma} and QMIX~\\cite{rashid2018qmix} address the analogous problem of attributing shared team rewards to individual agents via counterfactual baselines and value decomposition. Several independent studies provide direct evidence that step-independent credit assignment produces sign-level errors. IRC~\\cite{irc2026} reports that per-turn advantages $A^I$ frequently disagree in sign with outcome advantages $A^O$, with the resulting miscalibration causing a 14 percentage-point degradation (54\\% vs.\\ 68\\%). MC-GRPO~\\cite{mcgrpo2025} measures a 5\\% sign-flip rate and shows through controlled injection that this rate alone accounts for approximately 4\\% accuracy loss. GRPO-$\\lambda$~\\cite{grpolambda2025} proves in Lemma~1 that the value estimation error grows with sequence position, since the baseline $\\mu_t$ is biased for all $t > 0$. OAR~\\cite{oar2026} identifies ``reward aliasing'' arising from coarse-grained credit assignment. G-RA~\\cite{gra2025} visualizes accumulated reward diverging in sign from outcome reward. Decoupled-CA~\\cite{decoupledca2026} (under review) finds that invalid actions in positive-outcome trajectories receive positive credit and proposes multiplicative gated rewards to correct this. Episode-level GRPO, as we advocate, corresponds to GAE(1,1) without a critic: uniform advantage across all steps forfeits per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard practice produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Multi-Turn Agent Credit Assignment.}\nA parallel thread develops credit assignment methods specifically for multi-turn LLM agents. Turn-PPO~\\cite{turnppo2026} estimates turn-level advantages within PPO and reports that standard GRPO directly crashes on WebShop and Sokoban, with three proposed fixes all failing to recover. GiGPO~\\cite{feng2025gigpo} structures advantages at two scales (episode-level macro and step-level micro) and ablates both as indispensable. GAGPO~\\cite{gagpo2026} replaces Monte Carlo step advantages with TD/GAE-style recursive estimation. iStar~\\cite{istar2025} merges episode and step advantages at the token level but observes that token-level granularity increases fluctuation rather than improving stability. MT-GRPO~\\cite{mtgrpo2025} contrasts its turn-level method against an outcome-only GRPO baseline (GRPO-OR): 0.04 exact match versus 0.50, a 12$\\times$ gap that underscores the severity of multi-turn credit assignment failure. SWEET-RL~\\cite{sweetrl2025} finds that episode-level agents degrade sharply beyond 10 turns. These methods propose solutions to the multi-turn credit assignment problem. We complement them with a mechanistic diagnosis: two specific failure modes (policy information loss at the inference layer and advantage sign misattribution at the training layer) explain why step-independent windowing fails and why episode-level assignment eliminates both.\n\n\\paragraph{GRPO Collapse and Training Instability.}\nSeveral independent groups have documented collapse phenomena in GRPO-based training that corroborate our analysis. RAGEN-2~\\cite{ragen2_2026} provides a mathematical proof of advantage collapse: when within-prompt reward variance approaches zero, task-relevant gradients vanish and KL regularization dominates, driving the policy back toward the reference model. GRPO-Collapse~\\cite{grpocollapse2025} identifies the Lazy Likelihood-Displacement death spiral in Search-R1, where all four tested models collapse within 300 training steps. Gradient Coupling~\\cite{gradientcoupling2025} challenges the ``reward miscalibration'' hypothesis and argues in Lemma~3.1 that flawed actions have naturally negative expected advantage; the true failure mode is gradient coupling from high input similarity across consecutive steps. This expected-value analysis is compatible with our per-sample sign analysis: expected advantages can be correct in aggregate (averaged over many samples) while per-sample signs remain near-random under high variance, precisely the regime where step-independent windowing operates. These independent observations converge on a shared conclusion that step-independent GRPO training is structurally unstable in multi-turn settings. Our work unifies these phenomena under a dual-mechanism diagnosis (M1 and M2) and validates the episode-level alternative through controlled training dynamics.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "988c105b-ac52-4706-ae77-39b28b7943d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N9zWqtzTvWoR8hdhbuj3J3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24400,
      "cache_read_input_tokens": 22737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24400
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

_source line 16 · 2026-05-18T19:56:44.453Z_

<details><summary>↩ Tool result · `toolu_01EASNvLQzarL2FZgDKrkDSe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "1db342b5-63b3-4a90-b67b-0e2647521afa",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for Multi-Turn LLM Agents.}\nThe ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nTemporal credit assignment spans a well-studied spectrum. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance via a learned critic and clipped surrogate objectives. GAE~\\cite{schulman2016gae} interpolates between one-step TD and Monte Carlo returns through the $\\lambda$ parameter, with TD($\\lambda$)~\\cite{sutton1988td} establishing this interpolation in the tabular setting. RUDDER~\\cite{rudder2019} decomposes delayed rewards via sequence-to-sequence modeling but introduces bias whose correction slows exponentially with horizon. For LLM agents, AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates step-level value through Monte Carlo rollouts, and SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO with separate advantages for task-solving and skill-editing. In cooperative multi-agent RL, COMA~\\cite{foerster2018coma} and QMIX~\\cite{rashid2018qmix} address the analogous problem of attributing shared team rewards to individual agents via counterfactual baselines and value decomposition. Several independent studies provide direct evidence that step-independent credit assignment produces sign-level errors. IRC~\\cite{irc2026} reports that per-turn advantages $A^I$ frequently disagree in sign with outcome advantages $A^O$, with the resulting miscalibration causing a 14 percentage-point degradation (54\\% vs.\\ 68\\%). MC-GRPO~\\cite{mcgrpo2025} measures a 5\\% sign-flip rate and shows through controlled injection that this rate alone accounts for approximately 4\\% accuracy loss. GRPO-$\\lambda$~\\cite{grpolambda2025} proves in Lemma~1 that the value estimation error grows with sequence position, since the baseline $\\mu_t$ is biased for all $t > 0$. OAR~\\cite{oar2026} identifies ``reward aliasing'' arising from coarse-grained credit assignment. G-RA~\\cite{gra2025} visualizes accumulated reward diverging in sign from outcome reward. Decoupled-CA~\\cite{decoupledca2026} (under review) finds that invalid actions in positive-outcome trajectories receive positive credit and proposes multiplicative gated rewards to correct this. Episode-level GRPO, as we advocate, corresponds to GAE(1,1) without a critic: uniform advantage across all steps forfeits per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard practice produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Multi-Turn Agent Credit Assignment.}\nA parallel thread develops credit assignment methods specifically for multi-turn LLM agents. Turn-PPO~\\cite{turnppo2026} estimates turn-level advantages within PPO and reports that standard GRPO directly crashes on WebShop and Sokoban, with three proposed fixes all failing to recover. GiGPO~\\cite{feng2025gigpo} structures advantages at two scales (episode-level macro and step-level micro) and ablates both as indispensable. GAGPO~\\cite{gagpo2026} replaces Monte Carlo step advantages with TD/GAE-style recursive estimation. iStar~\\cite{istar2025} merges episode and step advantages at the token level but observes that token-level granularity increases fluctuation rather than improving stability. MT-GRPO~\\cite{mtgrpo2025} contrasts its turn-level method against an outcome-only GRPO baseline (GRPO-OR): 0.04 exact match versus 0.50, a 12$\\times$ gap that underscores the severity of multi-turn credit assignment failure. SWEET-RL~\\cite{sweetrl2025} finds that episode-level agents degrade sharply beyond 10 turns. These methods propose solutions to the multi-turn credit assignment problem. We complement them with a mechanistic diagnosis: two specific failure modes (policy information loss at the inference layer and advantage sign misattribution at the training layer) explain why step-independent windowing fails and why episode-level assignment eliminates both.\n\n\\paragraph{GRPO Collapse and Training Instability.}\nSeveral independent groups have documented collapse phenomena in GRPO-based training that corroborate our analysis. RAGEN-2~\\cite{ragen2_2026} provides a mathematical proof of advantage collapse: when within-prompt reward variance approaches zero, task-relevant gradients vanish and KL regularization dominates, driving the policy back toward the reference model. GRPO-Collapse~\\cite{grpocollapse2025} identifies the Lazy Likelihood-Displacement death spiral in Search-R1, where all four tested models collapse within 300 training steps. Gradient Coupling~\\cite{gradientcoupling2025} challenges the ``reward miscalibration'' hypothesis and argues in Lemma~3.1 that flawed actions have naturally negative expected advantage; the true failure mode is gradient coupling from high input similarity across consecutive steps. This expected-value analysis is compatible with our per-sample sign analysis: expected advantages can be correct in aggregate (averaged over many samples) while per-sample signs remain near-random under high variance, precisely the regime where step-independent windowing operates. These independent observations converge on a shared conclusion that step-independent GRPO training is structurally unstable in multi-turn settings. Our work unifies these phenomena under a dual-mechanism diagnosis (M1 and M2) and validates the episode-level alternative through controlled training dynamics.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 14,
        "newStart": 1,
        "newLines": 14,
        "lines": [
          " \\section{Related Work}",
          " \\label{sec:related_work}",
          " ",
          "-\\paragraph{RL Training for LLM Agents.}",
          "-The ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents, achieving substantial gains over supervised fine-tuning. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechanism itself as a source of systematic sign misattribution, which is the structural failure we identify and formalize.",
          "+\\paragraph{RL Training for Multi-Turn LLM Agents.}",
          "+The ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.",
          " ",
          " \\paragraph{Credit Assignment in Reinforcement Learning.}",
          "-The temporal credit assignment problem has a long history. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance through a learned value function and clipped surrogate objectives. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} interpolates between one-step bootstrap and Monte Carlo returns via the $\\lambda$ parameter, offering a continuous spectrum from TD(0) to full-episode credit. The TD($\\lambda$) family~\\cite{sutton1988td} established this interpolation in the tabular setting. In the LLM agent context, process reward models provide step-level supervision: AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates per-step value through Monte Carlo rollouts or TD-based estimation with GAE. SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO, which separately estimates advantages for task-solving and skill-editing decisions. In cooperative multi-agent RL, the analogous problem of shared team reward has been addressed through counterfactual baselines (COMA~\\cite{foerster2018coma}) and value decomposition (QMIX~\\cite{rashid2018qmix}), which estimate individual agent contributions to the team outcome. Episode-level GRPO, as we advocate, is equivalent to GAE(1,1) without a critic: it assigns uniform advantage across all steps, forgoing per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard adaptation of GRPO (step-independent windowing) produces catastrophic sign errors in multi-turn settings.",
          "+Temporal credit assignment spans a well-studied spectrum. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance via a learned critic and clipped surrogate objectives. GAE~\\cite{schulman2016gae} interpolates between one-step TD and Monte Carlo returns through the $\\lambda$ parameter, with TD($\\lambda$)~\\cite{sutton1988td} establishing this interpolation in the tabular setting. RUDDER~\\cite{rudder2019} decomposes delayed rewards via sequence-to-sequence modeling but introduces bias whose correction slows exponentially with horizon. For LLM agents, AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates step-level value through Monte Carlo rollouts, and SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO with separate advantages for task-solving and skill-editing. In cooperative multi-agent RL, COMA~\\cite{foerster2018coma} and QMIX~\\cite{rashid2018qmix} address the analogous problem of attributing shared team rewards to individual agents via counterfactual baselines and value decomposition. Several independent studies provide direct evidence that step-independent credit assignment produces sign-level errors. IRC~\\cite{irc2026} reports that per-turn advantages $A^I$ frequently disagree in sign with outcome advantages $A^O$, with the resulting miscalibration causing a 14 percentage-point degradation (54\\% vs.\\ 68\\%). MC-GRPO~\\cite{mcgrpo2025} measures a 5\\% sign-flip rate and shows through controlled injection that this rate alone accounts for approximately 4\\% accuracy loss. GRPO-$\\lambda$~\\cite{grpolambda2025} proves in Lemma~1 that the value estimation error grows with sequence position, since the baseline $\\mu_t$ is biased for all $t > 0$. OAR~\\cite{oar2026} identifies ``reward aliasing'' arising from coarse-grained credit assignment. G-RA~\\cite{gra2025} visualizes accumulated reward diverging in sign from outcome reward. Decoupled-CA~\\cite{decoupledca2026} (under review) finds that invalid actions in positive-outcome trajectories receive positive credit and proposes multiplicative gated rewards to correct this. Episode-level GRPO, as we advocate, corresponds to GAE(1,1) without a critic: uniform advantage across all steps forfeits per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard practice produces catastrophic sign errors in multi-turn settings.",
          " ",
          "-\\paragraph{Selective Verification and Adaptive Computation.}",
          "-A growing body of work trains models to allocate computation adaptively rather than uniformly. In the reasoning domain, Thinkless~\\cite{du2025thinkless} introduces an RL-trained control token that decides whether to invoke extended thinking for each query. AutoThink~\\cite{tu2025autothink} uses multi-stage RL to shape when reasoning-capable models activate their chain-of-thought. SelfBudgeter~\\cite{selfbudgeter2025} frames adaptive computation as token budget allocation trained via budget-guided GRPO. In the agent domain, ARES~\\cite{yang2026ares} trains an SFT-initialized router that selects reasoning effort levels per step, refined via GRPO with a combined outcome and token-efficiency reward. Agent-Omit~\\cite{agent-omit2026} learns to omit redundant thoughts and observations through agentic RL, reducing context length without sacrificing performance. Sherlock~\\cite{sherlock2025} performs selective verification at the workflow level through offline counterfactual analysis and speculative execution. Derailer-Rerailer~\\cite{wan2025derailer-rerailer} detects instability triggers in reasoning chains and invokes targeted verification. These approaches operate at the reasoning-token level (Thinkless, AutoThink, SelfBudgeter), workflow-DAG level (Sherlock), or use heuristic triggers (Derailer-Rerailer) and SFT-initialized routers (ARES). Our selective verification differs in scope and mechanism: it makes a binary verify-or-skip decision at each agent interaction step, trained end-to-end via RL with an action-change informativeness signal that requires no external annotations or heuristic design.",
          "+\\paragraph{Multi-Turn Agent Credit Assignment.}",
          "+A parallel thread develops credit assignment methods specifically for multi-turn LLM agents. Turn-PPO~\\cite{turnppo2026} estimates turn-level advantages within PPO and reports that standard GRPO directly crashes on WebShop and Sokoban, with three proposed fixes all failing to recover. GiGPO~\\cite{feng2025gigpo} structures advantages at two scales (episode-level macro and step-level micro) and ablates both as indispensable. GAGPO~\\cite{gagpo2026} replaces Monte Carlo step advantages with TD/GAE-style recursive estimation. iStar~\\cite{istar2025} merges episode and step advantages at the token level but observes that token-level granularity increases fluctuation rather than improving stability. MT-GRPO~\\cite{mtgrpo2025} contrasts its turn-level method against an outcome-only GRPO baseline (GRPO-OR): 0.04 exact match versus 0.50, a 12$\\times$ gap that underscores the severity of multi-turn credit assignment failure. SWEET-RL~\\cite{sweetrl2025} finds that episode-level agents degrade sharply beyond 10 turns. These methods propose solutions to the multi-turn credit assignment problem. We complement them with a mechanistic diagnosis: two specific failure modes (policy information loss at the inference layer and advantage sign misattribution at the training layer) explain why step-independent windowing fails and why episode-level assignment eliminates both.",
          " ",
          "-\\paragraph{Self-Verification and Self-Correction.}",
          "-Self-verification has received significant attention as a mechanism for improving LLM reliability. Kamoi et al.~\\cite{kamoi2024self-correction-survey} survey self-correction in LLMs and establish that pure intrinsic self-correction (without external feedback) is unreliable across most settings. Long et al.~\\cite{long2026selfverification} quantify the verification dilemma empirically: over 90\\% of self-verification instances are confirmatory, with only approximately 2\\% producing corrective changes. CorrectBench~\\cite{tie2025correctbench} further demonstrates that uniform self-correction exhibits diminishing returns, as models repeatedly ``correct'' already-correct answers. VerifiAgent~\\cite{verifiagent2025} proposes a unified verification framework with meta-verification and tool-based adaptive strategies, focusing on improving verification quality through better methods. These findings collectively establish two facts: verification quality is limited by confirmatory bias, and uniform application of verification wastes computation on uninformative instances. Our work addresses a complementary question: given that most verification is confirmatory, \\textit{when} should an agent verify? The 90\\% confirmatory rate reported by Long et al. directly motivates learning a selective policy that triggers verification only at steps where action change is likely.",
          "\\ No newline at end of file",
          "+\\paragraph{GRPO Collapse and Training Instability.}",
          "+Several independent groups have documented collapse phenomena in GRPO-based training that corroborate our analysis. RAGEN-2~\\cite{ragen2_2026} provides a mathematical proof of advantage collapse: when within-prompt reward variance approaches zero, task-relevant gradients vanish and KL regularization dominates, driving the policy back toward the reference model. GRPO-Collapse~\\cite{grpocollapse2025} identifies the Lazy Likelihood-Displacement death spiral in Search-R1, where all four tested models collapse within 300 training steps. Gradient Coupling~\\cite{gradientcoupling2025} challenges the ``reward miscalibration'' hypothesis and argues in Lemma~3.1 that flawed actions have naturally negative expected advantage; the true failure mode is gradient coupling from high input similarity across consecutive steps. This expected-value analysis is compatible with our per-sample sign analysis: expected advantages can be correct in aggregate (averaged over many samples) while per-sample signs remain near-random under high variance, precisely the regime where step-independent windowing operates. These independent observations converge on a shared conclusion that step-independent GRPO training is structurally unstable in multi-turn settings. Our work unifies these phenomena under a dual-mechanism diagnosis (M1 and M2) and validates the episode-level alternative through controlled training dynamics."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for LLM Agents.}\nThe ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents, achieving substantial gains over supervised fine-tuning. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechanism itself as a source of systematic sign misattribution, which is the structural failure we identify and formalize.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nThe temporal credit assignment problem has a long history. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance through a learned value function and clipped surrogate objectives. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} interpolates between one-step bootstrap and Monte Carlo returns via the $\\lambda$ parameter, offering a continuous spectrum from TD(0) to full-episode credit. The TD($\\lambda$) family~\\cite{sutton1988td} established this interpolation in the tabular setting. In the LLM agent context, process reward models provide step-level supervision: AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates per-step value through Monte Carlo rollouts or TD-based estimation with GAE. SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO, which separately estimates advantages for task-solving and skill-editing decisions. In cooperative multi-agent RL, the analogous problem of shared team reward has been addressed through counterfactual baselines (COMA~\\cite{foerster2018coma}) and value decomposition (QMIX~\\cite{rashid2018qmix}), which estimate individual agent contributions to the team outcome. Episode-level GRPO, as we advocate, is equivalent to GAE(1,1) without a critic: it assigns uniform advantage across all steps, forgoing per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard adaptation of GRPO (step-independent windowing) produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Selective Verification and Adaptive Computation.}\nA growing body of work trains models to allocate computation adaptively rather than uniformly. In the reasoning domain, Thinkless~\\cite{du2025thinkless} introduces an RL-trained control token that decides whether to invoke extended thinking for each query. AutoThink~\\cite{tu2025autothink} uses multi-stage RL to shape when reasoning-capable models activate their chain-of-thought. SelfBudgeter~\\cite{selfbudgeter2025} frames adaptive computation as token budget allocation trained via budget-guided GRPO. In the agent domain, ARES~\\cite{yang2026ares} trains an SFT-initialized router that selects reasoning effort levels per step, refined via GRPO with a combined outcome and token-efficiency reward. Agent-Omit~\\cite{agent-omit2026} learns to omit redundant thoughts and observations through agentic RL, reducing context length without sacrificing performance. Sherlock~\\cite{sherlock2025} performs selective verification at the workflow level through offline counterfactual analysis and speculative execution. Derailer-Rerailer~\\cite{wan2025derailer-rerailer} detects instability triggers in reasoning chains and invokes targeted verification. These approaches operate at the reasoning-token level (Thinkless, AutoThink, SelfBudgeter), workflow-DAG level (Sherlock), or use heuristic triggers (Derailer-Rerailer) and SFT-initialized routers (ARES). Our selective verification differs in scope and mechanism: it makes a binary verify-or-skip decision at each agent interaction step, trained end-to-end via RL with an action-change informativeness signal that requires no external annotations or heuristic design.\n\n\\paragraph{Self-Verification and Self-Correction.}\nSelf-verification has received significant attention as a mechanism for improving LLM reliability. Kamoi et al.~\\cite{kamoi2024self-correction-survey} survey self-correction in LLMs and establish that pure intrinsic self-correction (without external feedback) is unreliable across most settings. Long et al.~\\cite{long2026selfverification} quantify the verification dilemma empirically: over 90\\% of self-verification instances are confirmatory, with only approximately 2\\% producing corrective changes. CorrectBench~\\cite{tie2025correctbench} further demonstrates that uniform self-correction exhibits diminishing returns, as models repeatedly ``correct'' already-correct answers. VerifiAgent~\\cite{verifiagent2025} proposes a unified verification framework with meta-verification and tool-based adaptive strategies, focusing on improving verification quality through better methods. These findings collectively establish two facts: verification quality is limited by confirmatory bias, and uniform application of verification wastes computation on uninformative instances. Our work addresses a complementary question: given that most verification is confirmatory, \\textit{when} should an agent verify? The 90\\% confirmatory rate reported by Long et al. directly motivates learning a selective policy that triggers verification only at steps where action change is likely.",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 17_

Now adding the 16 new bib entries to references.bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "c40a31b6-4813-4d8e-a613-a47d7ff3c4f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2pp7S4oshM2anavZbKT7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 47137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5390
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_012wuLDK7gtsdgmbet2ScSpF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
  "old_string": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}",
  "new_string": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}\n\n@article{irc2026,\n  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.02869},\n  year    = {2026},\n}\n\n@article{mcgrpo2025,\n  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},\n  author  = {Kim, Youngeun},\n  journal = {arXiv preprint arXiv:2601.22582},\n  year    = {2025},\n}\n\n@article{gra2025,\n  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2508.10548},\n  year    = {2025},\n}\n\n@article{grpolambda2025,\n  title   = {{GRPO-$\\lambda$}: Credit Assignment improves {LLM} Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2510.00194},\n  year    = {2025},\n}\n\n@article{oar2026,\n  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2601.07408},\n  year    = {2026},\n}\n\n@article{decoupledca2026,\n  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},\n  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},\n  journal = {Submitted to ICLR 2026 (under review)},\n  year    = {2026},\n  note    = {OpenReview: Suja4AQ9Fo},\n}\n\n@article{ragen2_2026,\n  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.06268},\n  year    = {2026},\n}\n\n@article{grpocollapse2025,\n  title   = {On {GRPO} Collapse in {Search-R1}: The Lazy Likelihood-Displacement Death Spiral},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.04220},\n  year    = {2025},\n}\n\n@article{gradientcoupling2025,\n  title   = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2509.23870},\n  year    = {2025},\n}\n\n@article{turnppo2026,\n  title   = {{Turn-PPO}: Turn-Level Advantage Estimation with {PPO} for Improved Multi-Turn {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.17008},\n  year    = {2026},\n}\n\n@article{gagpo2026,\n  title   = {{GAGPO}: Generalized Advantage Grouped Policy Optimization},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2605.13217},\n  year    = {2026},\n}\n\n@article{istar2025,\n  title   = {Agentic Reinforcement Learning with Implicit Step Rewards},\n  author  = {Anonymous},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year    = {2025},\n}\n\n@article{mtgrpo2025,\n  title   = {Reinforcing Multi-Turn Reasoning in {LLM} Agents via Turn-Level Credit Assignment},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2505.11821},\n  year    = {2025},\n}\n\n@article{sweetrl2025,\n  title   = {{SWEET-RL}: Training Multi-Turn {LLM} Agents on Collaborative Reasoning Tasks},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2503.15478},\n  year    = {2025},\n}\n\n@inproceedings{rudder2019,\n  title     = {{RUDDER}: Return Decomposition for Delayed Rewards},\n  author    = {Arjona-Medina, Jose A. and Gillhofer, Michael and Widrich, Michael and Unterthiner, Thomas and Brandstetter, Johannes and Hochreiter, Sepp},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{ca_survey2026,\n  title   = {From Reasoning to Agentic: Credit Assignment in {RL} for {LLMs}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.09459},\n  year    = {2026},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "275a23fe-c32b-4a7c-aafe-d91677635f00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2pp7S4oshM2anavZbKT7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 47137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5390
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

_source line 19 · 2026-05-18T19:57:11.404Z_

<details><summary>↩ Tool result · `toolu_012wuLDK7gtsdgmbet2ScSpF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "75d386fe-1647-4013-9816-5527576620f9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
    "oldString": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}",
    "newString": "@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}\n\n@article{irc2026,\n  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.02869},\n  year    = {2026},\n}\n\n@article{mcgrpo2025,\n  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},\n  author  = {Kim, Youngeun},\n  journal = {arXiv preprint arXiv:2601.22582},\n  year    = {2025},\n}\n\n@article{gra2025,\n  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2508.10548},\n  year    = {2025},\n}\n\n@article{grpolambda2025,\n  title   = {{GRPO-$\\lambda$}: Credit Assignment improves {LLM} Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2510.00194},\n  year    = {2025},\n}\n\n@article{oar2026,\n  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2601.07408},\n  year    = {2026},\n}\n\n@article{decoupledca2026,\n  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},\n  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},\n  journal = {Submitted to ICLR 2026 (under review)},\n  year    = {2026},\n  note    = {OpenReview: Suja4AQ9Fo},\n}\n\n@article{ragen2_2026,\n  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.06268},\n  year    = {2026},\n}\n\n@article{grpocollapse2025,\n  title   = {On {GRPO} Collapse in {Search-R1}: The Lazy Likelihood-Displacement Death Spiral},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.04220},\n  year    = {2025},\n}\n\n@article{gradientcoupling2025,\n  title   = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2509.23870},\n  year    = {2025},\n}\n\n@article{turnppo2026,\n  title   = {{Turn-PPO}: Turn-Level Advantage Estimation with {PPO} for Improved Multi-Turn {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.17008},\n  year    = {2026},\n}\n\n@article{gagpo2026,\n  title   = {{GAGPO}: Generalized Advantage Grouped Policy Optimization},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2605.13217},\n  year    = {2026},\n}\n\n@article{istar2025,\n  title   = {Agentic Reinforcement Learning with Implicit Step Rewards},\n  author  = {Anonymous},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year    = {2025},\n}\n\n@article{mtgrpo2025,\n  title   = {Reinforcing Multi-Turn Reasoning in {LLM} Agents via Turn-Level Credit Assignment},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2505.11821},\n  year    = {2025},\n}\n\n@article{sweetrl2025,\n  title   = {{SWEET-RL}: Training Multi-Turn {LLM} Agents on Collaborative Reasoning Tasks},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2503.15478},\n  year    = {2025},\n}\n\n@inproceedings{rudder2019,\n  title     = {{RUDDER}: Return Decomposition for Delayed Rewards},\n  author    = {Arjona-Medina, Jose A. and Gillhofer, Michael and Widrich, Michael and Unterthiner, Thomas and Brandstetter, Johannes and Hochreiter, Sepp},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{ca_survey2026,\n  title   = {From Reasoning to Agentic: Credit Assignment in {RL} for {LLMs}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.09459},\n  year    = {2026},\n}",
    "originalFile": "@inproceedings{shridhar2021alfworld,\n  title     = {{ALFWorld}: Aligning Text and Embodied Environments for Interactive Learning},\n  author    = {Shridhar, Mohit and Yuan, Xingdi and C\\^{o}t\\'{e}, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2021},\n}\n\n@inproceedings{agent-omit2026,\n  title     = {Agent-Omit: Training Efficient {LLM} Agents for Adaptive Thought and Observation Omission via Agentic {RL}},\n  author    = {Ning, Yansong and Fang, Jun and Tan, Naiqiang and Liu, Hao},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year      = {2026},\n}\n\n@article{choudhury2025agentprm,\n  title   = {Process Reward Models for {LLM} Agents: Practical Framework and Directions},\n  author  = {Choudhury, Sanjiban},\n  journal = {arXiv preprint arXiv:2502.10325},\n  year    = {2025},\n}\n\n@article{dapo2025,\n  title   = {{DAPO}: An Open-Source {LLM} Reinforcement Learning System at Scale},\n  author  = {Yu, Qiying and Zhang, Zheng and Zhu, Ruofei and Yuan, Yufeng and Zuo, Xiaochen and Yue, Yu and Dai, Weinan and Fan, Tiantian and Liu, Gaohong and Liu, Lingjun and Liu, Xin and Lin, Haibin and Lin, Zhiqi and Ma, Bole and Sheng, Guangming and Tong, Yuxuan and Zhang, Chi and Zhang, Mofan and Zhang, Wang and Zhu, Hang and Zhu, Jinhua and Chen, Jiaze and Chen, Jiangjie and Wang, Chengyi and Yu, Hongli and Song, Yuxuan and Wei, Xiangpeng and Zhou, Hao and Liu, Jingjing and Ma, Wei-Ying and Zhang, Ya-Qin and Yan, Lin and Qiao, Mu and Wu, Yonghui and Wang, Mingxuan},\n  journal = {arXiv preprint arXiv:2503.14476},\n  year    = {2025},\n}\n\n@inproceedings{foerster2018coma,\n  title     = {Counterfactual Multi-Agent Policy Gradients},\n  author    = {Foerster, Jakob and Farquhar, Gregory and Afouras, Triantafyllos and Nardelli, Nantas and Whiteson, Shimon},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n  year      = {2018},\n}\n\n@inproceedings{digiRL2024,\n  title     = {{DigiRL}: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning},\n  author    = {Bai, Hao and Zhou, Yifei and Cemri, Mert and Pan, Jiayi and Suhr, Alane and Levine, Sergey and Kumar, Aviral},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n}\n\n@inproceedings{du2025thinkless,\n  title     = {Thinkless: {LLM} Learns When to Think},\n  author    = {Fang, Gongfan and Ma, Xinyin and Wang, Xinchao},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n}\n\n@inproceedings{feng2025gigpo,\n  title     = {{GiGPO}: Group-in-Group Policy Optimization for {LLM} Agent Training},\n  author    = {Feng, Lang and Xue, Zhenghai and Liu, Tingcong and An, Bo},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n}\n\n@article{hcapo2026,\n  title   = {{HCAPO}: Hindsight Credit Assignment for Long-Horizon {LLM} Agents},\n  author  = {Tan, Hui-Ze and Yang, Xiao-Wen and Chen, Hao and Shao, Jie-Jing and Wen, Yi and Shen, Yuteng and Luo, Weihong and Du, Xiku and Guo, Lan-Zhe and Li, Yu-Feng},\n  journal = {arXiv preprint arXiv:2603.08754},\n  year    = {2026},\n}\n\n@article{kamoi2024self-correction-survey,\n  title   = {When Can {LLMs} Actually Correct Their Own Mistakes? {A} Critical Survey of Self-Correction of {LLMs}},\n  author  = {Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui},\n  journal = {arXiv preprint arXiv:2406.01297},\n  year    = {2024},\n}\n\n@inproceedings{kim2025reflact,\n  title     = {{ReflAct}: World-Grounded Decision Making in {LLM} Agents via Goal-State Reflection},\n  author    = {Kim, Jeonghye and Rhee, Sojeong and Kim, Minbeom and Kim, Dohyung and Lee, Sangmook and Sung, Youngchul and Jung, Kyomin},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year      = {2025},\n}\n\n@article{li2025sorl,\n  title   = {{SORL}: Stabilizing Off-Policy {RL} for Long-Horizon Agent Training},\n  author  = {Li, Chenliang and Elmahdy, Adel and Boyd, Alex and Wang, Zhongruo and Zeng, Siliang and Garcia, Alfredo and Bhatia, Parminder and Kass-Hout, Taha and Xiao, Cao and Hong, Mingyi},\n  journal = {arXiv preprint arXiv:2511.20718},\n  year    = {2025},\n}\n\n@article{long2026selfverification,\n  title   = {Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in {LLM} Reasoning},\n  author  = {Long, Quanyu and Jiang, Kai Jie and Chen, Jianda and Guo, Xu and Gan, Leilei and Wang, Wenya},\n  journal = {arXiv preprint arXiv:2602.03485},\n  year    = {2026},\n}\n\n@inproceedings{rashid2018qmix,\n  title     = {{QMIX}: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning},\n  author    = {Rashid, Tabish and Samvelyan, Mikayel and De Witt, Christian Schroeder and Farquhar, Gregory and Foerster, Jakob and Whiteson, Shimon},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2018},\n}\n\n@article{ragen2025,\n  title   = {{RAGEN}: Understanding Self-Evolution in {LLM} Agents via Multi-Turn Reinforcement Learning},\n  author  = {Wang, Zihan and Wang, Kangrui and Wang, Qineng and Zhang, Pingyue and Li, Linjie and Yang, Zhengyuan and Jin, Xing and Yu, Kefan and Nguyen, Minh Nhat and Liu, Licheng and Gottlieb, Eli and Lu, Yiping and Cho, Kyunghyun and Wu, Jiajun and Li, Fei-Fei and Wang, Lijuan and Choi, Yejin and Li, Manling},\n  journal = {arXiv preprint arXiv:2504.20073},\n  year    = {2025},\n}\n\n@inproceedings{yao2023react,\n  title     = {{ReAct}: Synergizing Reasoning and Acting in Language Models},\n  author    = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2023},\n}\n\n@inproceedings{schulman2016gae,\n  title     = {High-Dimensional Continuous Control Using Generalized Advantage Estimation},\n  author    = {Schulman, John and Moritz, Philipp and Levine, Sergey and Jordan, Michael and Abbeel, Pieter},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year      = {2016},\n}\n\n@article{schulman2017ppo,\n  title   = {Proximal Policy Optimization Algorithms},\n  author  = {Schulman, John and Wolski, Filip and Dhariwal, Prafulla and Radford, Alec and Klimov, Oleg},\n  journal = {arXiv preprint arXiv:1707.06347},\n  year    = {2017},\n}\n\n@article{selfbudgeter2025,\n  title   = {{SelfBudgeter}: Adaptive Token Allocation for Efficient {LLM} Reasoning},\n  author  = {Li, Zheng and Dong, Qingxiu and Ma, Jingyuan and Zhang, Di and Jia, Kai and Sui, Zhifang},\n  journal = {arXiv preprint arXiv:2505.11274},\n  year    = {2025},\n}\n\n@article{selfguide2026,\n  title   = {Co-Evolution of Policy and Internal Reward for Language Agents},\n  author  = {Wang, Xinyu and Wu, Hanwei and Song, Jingwei and Zhang, Shuyuan and Zhang, Jiayi and Kong, Fanqi and Kwok, Tung Sum Thomas and Chang, Xiao-Wen and Luo, Yuyu and Wu, Chenglin and Liu, Bang},\n  journal = {arXiv preprint arXiv:2604.03098},\n  year    = {2026},\n}\n\n@article{shao2024deepseekmath,\n  title   = {{DeepSeekMath}: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author  = {Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Bi, Xiao and Zhang, Haowei and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal = {arXiv preprint arXiv:2402.03300},\n  year    = {2024},\n}\n\n@article{sherlock2025,\n  title   = {Sherlock: Reliable and Efficient Agentic Workflow Execution},\n  author  = {Ro, Yeonju and Qiu, Haoran and Goiri, {\\'\\I}{\\~n}igo and Fonseca, Rodrigo and Bianchini, Ricardo and Akella, Aditya and Wang, Zhangyang and Erez, Mattan and Choukse, Esha},\n  journal = {arXiv preprint arXiv:2511.00330},\n  year    = {2025},\n}\n\n@article{skillmaster2026,\n  title   = {{SkillMaster}: Toward Autonomous Skill Mastery in {LLM} Agents},\n  author  = {Yang, Min and Piao, Jinghua and Xia, Xu and Lan, Xiaochong and Chen, Jiaju and Gong, Yongshun and Li, Yong},\n  journal = {arXiv preprint arXiv:2605.08693},\n  year    = {2026},\n}\n\n@inproceedings{spear2025,\n  title     = {Learn the Ropes, Then Trust the Wins: Self-Imitation with Progressive Exploration for Agentic Reinforcement Learning},\n  author    = {Qin, Yulei and Tan, Xiaoyu and He, Zhengbao and Li, Gang and Lin, Haojia and Li, Zongyi and Xu, Zihan and Shi, Yuchen and Cai, Siqi and Rui, Renting and Cai, Shaofei and Cai, Yuzheng and Zhang, Xuan and Ye, Sheng and Li, Ke and Sun, Xing},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year      = {2026},\n}\n\n@article{sutton1988td,\n  title   = {Learning to Predict by the Methods of Temporal Differences},\n  author  = {Sutton, Richard S.},\n  journal = {Machine Learning},\n  volume  = {3},\n  number  = {1},\n  pages   = {9--44},\n  year    = {1988},\n}\n\n@inproceedings{tie2025correctbench,\n  title     = {Can {LLMs} Correct Themselves? {A} Benchmark of Self-Correction in {LLMs}},\n  author    = {Tie, Guiyao and Yuan, Zenghui and Zhao, Zeli and Hu, Chaoran and Gu, Tianhe and Zhang, Ruihang and Zhang, Sizhe and Wu, Junran and Tu, Xiaoyue and Jin, Ming and Wen, Qingsong and Chen, Lixing and Zhou, Pan and Sun, Lichao},\n  booktitle = {Advances in Neural Information Processing Systems: Datasets and Benchmarks Track},\n  year      = {2025},\n}\n\n@inproceedings{tu2025autothink,\n  title     = {Learning When to Think: Shaping Adaptive Reasoning in {R1}-Style Models via Multi-Stage {RL}},\n  author    = {Tu, Songjun and Lin, Jiahao and Zhang, Qichao and Tian, Xiangyu and Li, Linjing and Lan, Xiangyuan and Zhao, Dongbin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n}\n\n@inproceedings{verifiagent2025,\n  title     = {{VerifiAgent}: A Unified Verification Agent in Language Model Reasoning},\n  author    = {Han, Jiuzhou and Buntine, Wray and Shareghi, Ehsan},\n  booktitle = {Findings of the Conference on Empirical Methods in Natural Language Processing},\n  year      = {2025},\n}\n\n@inproceedings{wan2025derailer-rerailer,\n  title     = {Derailer-Rerailer: Adaptive Verification for Efficient and Reliable {LM} Reasoning},\n  author    = {Wan, Guangya and Wu, Yuqi and Wang, Hao and Zhao, Shengming and Chen, Jie and Li, Sheng},\n  booktitle = {Findings of the Annual Meeting of the Association for Computational Linguistics},\n  year      = {2025},\n}\n\n@inproceedings{wang2022scienceworld,\n  title     = {{ScienceWorld}: Is Your Agent Smarter Than a 5th Grader?},\n  author    = {Wang, Ruoyao and Jansen, Peter and C\\^{o}t\\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2022},\n}\n\n@inproceedings{yao2022webshop,\n  title     = {{WebShop}: Towards Scalable Real-World Web Interaction with Grounded Language Agents},\n  author    = {Yao, Shunyu and Chen, Howard and Yang, John and Narasimhan, Karthik},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n}\n\n@inproceedings{zhou2024webarena,\n  title     = {{WebArena}: A Realistic Web Environment for Building Autonomous Agents},\n  author    = {Zhou, Shuyan and Xu, Frank F. and Zhu, Hao and Zhou, Xuhui and Lo, Robert and Sridhar, Abishek and Cheng, Xianyi and Ou, Tianyue and Bisk, Yonatan and Fried, Daniel and Alon, Uri and Neubig, Graham},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{wei2025webagent-r1,\n  title     = {{WebAgent-R1}: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning},\n  author    = {Wei, Zhepei and Yao, Wenlin and Liu, Yao and Zhang, Weizhi and Lu, Qin and Qiu, Liang and Yu, Changlong and Xu, Puyang and Zhang, Chao and Yin, Bing and Yun, Hyokun and Li, Lihong},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year      = {2025},\n}\n\n@article{williams1992reinforce,\n  title   = {Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning},\n  author  = {Williams, Ronald J.},\n  journal = {Machine Learning},\n  volume  = {8},\n  number  = {3--4},\n  pages   = {229--256},\n  year    = {1992},\n}\n\n@inproceedings{xi2025agentprm,\n  title     = {{AgentPRM}: Process Reward Models for {LLM} Agents via Step-Wise Promise and Progress},\n  author    = {Xi, Zhiheng and Liao, Chenyang and Li, Guanyu and Yang, Yajie and Chen, Wenxiang and Zhang, Zhihao and Wang, Binghai and Jin, Senjie and Zhou, Yuhao and Guan, Jian and Wu, Wei and Ji, Tao and Gui, Tao and Zhang, Qi and Huang, Xuanjing},\n  booktitle = {Proceedings of the {ACM} Web Conference},\n  year      = {2026},\n}\n\n@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 255,
        "oldLines": 3,
        "newStart": 255,
        "newLines": 116,
        "lines": [
          "   journal = {arXiv preprint arXiv:2603.07915},",
          "   year    = {2026},",
          " }",
          "+",
          "+@article{irc2026,",
          "+  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2604.02869},",
          "+  year    = {2026},",
          "+}",
          "+",
          "+@article{mcgrpo2025,",
          "+  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},",
          "+  author  = {Kim, Youngeun},",
          "+  journal = {arXiv preprint arXiv:2601.22582},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@article{gra2025,",
          "+  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2508.10548},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@article{grpolambda2025,",
          "+  title   = {{GRPO-$\\lambda$}: Credit Assignment improves {LLM} Reasoning},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2510.00194},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@article{oar2026,",
          "+  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2601.07408},",
          "+  year    = {2026},",
          "+}",
          "+",
          "+@article{decoupledca2026,",
          "+  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},",
          "+  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},",
          "+  journal = {Submitted to ICLR 2026 (under review)},",
          "+  year    = {2026},",
          "+  note    = {OpenReview: Suja4AQ9Fo},",
          "+}",
          "+",
          "+@article{ragen2_2026,",
          "+  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {RL}},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2604.06268},",
          "+  year    = {2026},",
          "+}",
          "+",
          "+@article{grpocollapse2025,",
          "+  title   = {On {GRPO} Collapse in {Search-R1}: The Lazy Likelihood-Displacement Death Spiral},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2512.04220},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@article{gradientcoupling2025,",
          "+  title   = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic {RL}},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2509.23870},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@article{turnppo2026,",
          "+  title   = {{Turn-PPO}: Turn-Level Advantage Estimation with {PPO} for Improved Multi-Turn {RL}},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2512.17008},",
          "+  year    = {2026},",
          "+}",
          "+",
          "+@article{gagpo2026,",
          "+  title   = {{GAGPO}: Generalized Advantage Grouped Policy Optimization},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2605.13217},",
          "+  year    = {2026},",
          "+}",
          "+",
          "+@article{istar2025,",
          "+  title   = {Agentic Reinforcement Learning with Implicit Step Rewards},",
          "+  author  = {Anonymous},",
          "+  booktitle = {Advances in Neural Information Processing Systems},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@article{mtgrpo2025,",
          "+  title   = {Reinforcing Multi-Turn Reasoning in {LLM} Agents via Turn-Level Credit Assignment},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2505.11821},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@article{sweetrl2025,",
          "+  title   = {{SWEET-RL}: Training Multi-Turn {LLM} Agents on Collaborative Reasoning Tasks},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2503.15478},",
          "+  year    = {2025},",
          "+}",
          "+",
          "+@inproceedings{rudder2019,",
          "+  title     = {{RUDDER}: Return Decomposition for Delayed Rewards},",
          "+  author    = {Arjona-Medina, Jose A. and Gillhofer, Michael and Widrich, Michael and Unterthiner, Thomas and Brandstetter, Johannes and Hochreiter, Sepp},",
          "+  booktitle = {Advances in Neural Information Processing Systems},",
          "+  year      = {2019},",
          "+}",
          "+",
          "+@article{ca_survey2026,",
          "+  title   = {From Reasoning to Agentic: Credit Assignment in {RL} for {LLMs}},",
          "+  author  = {Anonymous},",
          "+  journal = {arXiv preprint arXiv:2604.09459},",
          "+  year    = {2026},",
          "+}"
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

_source line 20_

Now let me verify both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "b1fbc5f4-c03a-444e-8ea1-4e935a20203d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mZHt3iCzngY5Ev21NdV18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 52527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1765
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01BsAYyJ2oP8AKEj38BvcCZr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "7461dc16-fa4f-4b4e-beb7-959065c674bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mZHt3iCzngY5Ev21NdV18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 52527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1765
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

_source line 22 · 2026-05-18T19:57:16.763Z_

<details><summary>↩ Tool result · `toolu_01BsAYyJ2oP8AKEj38BvcCZr`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{RL Training for Multi-Turn LLM Agents.}
5	The ReAct paradigm~\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.
6	
7	\paragraph{Credit Assignment in Reinforcement Learning.}
8	Temporal credit assignment spans a well-studied spectrum. REINFORCE~\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\cite{schulman2017ppo} reduces variance via a learned critic and clipped surrogate objectives. GAE~\cite{schulman2016gae} interpolates between one-step TD and Monte Carlo returns through the $\lambda$ parameter, with TD($\lambda$)~\cite{sutton1988td} establishing this interpolation in the tabular setting. RUDDER~\cite{rudder2019} decomposes delayed rewards via sequence-to-sequence modeling but introduces bias whose correction slows exponentially with horizon. For LLM agents, AgentPRM~\cite{choudhury2025agentprm,xi2025agentprm} estimates step-level value through Monte Carlo rollouts, and SkillMaster~\cite{skillmaster2026} proposes DualAdv-GRPO with separate advantages for task-solving and skill-editing. In cooperative multi-agent RL, COMA~\cite{foerster2018coma} and QMIX~\cite{rashid2018qmix} address the analogous problem of attributing shared team rewards to individual agents via counterfactual baselines and value decomposition. Several independent studies provide direct evidence that step-independent credit assignment produces sign-level errors. IRC~\cite{irc2026} reports that per-turn advantages $A^I$ frequently disagree in sign with outcome advantages $A^O$, with the resulting miscalibration causing a 14 percentage-point degradation (54\% vs.\ 68\%). MC-GRPO~\cite{mcgrpo2025} measures a 5\% sign-flip rate and shows through controlled injection that this rate alone accounts for approximately 4\% accuracy loss. GRPO-$\lambda$~\cite{grpolambda2025} proves in Lemma~1 that the value estimation error grows with sequence position, since the baseline $\mu_t$ is biased for all $t > 0$. OAR~\cite{oar2026} identifies ``reward aliasing'' arising from coarse-grained credit assignment. G-RA~\cite{gra2025} visualizes accumulated reward diverging in sign from outcome reward. Decoupled-CA~\cite{decoupledca2026} (under review) finds that invalid actions in positive-outcome trajectories receive positive credit and proposes multiplicative gated rewards to correct this. Episode-level GRPO, as we advocate, corresponds to GAE(1,1) without a critic: uniform advantage across all steps forfeits per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard practice produces catastrophic sign errors in multi-turn settings.
9	
10	\paragraph{Multi-Turn Agent Credit Assignment.}
11	A parallel thread develops credit assignment methods specifically for multi-turn LLM agents. Turn-PPO~\cite{turnppo2026} estimates turn-level advantages within PPO and reports that standard GRPO directly crashes on WebShop and Sokoban, with three proposed fixes all failing to recover. GiGPO~\cite{feng2025gigpo} structures advantages at two scales (episode-level macro and step-level micro) and ablates both as indispensable. GAGPO~\cite{gagpo2026} replaces Monte Carlo step advantages with TD/GAE-style recursive estimation. iStar~\cite{istar2025} merges episode and step advantages at the token level but observes that token-level granularity increases fluctuation rather than improving stability. MT-GRPO~\cite{mtgrpo2025} contrasts its turn-level method against an outcome-only GRPO baseline (GRPO-OR): 0.04 exact match versus 0.50, a 12$\times$ gap that underscores the severity of multi-turn credit assignment failure. SWEET-RL~\cite{sweetrl2025} finds that episode-level agents degrade sharply beyond 10 turns. These methods propose solutions to the multi-turn credit assignment problem. We complement them with a mechanistic diagnosis: two specific failure modes (policy information loss at the inference layer and advantage sign misattribution at the training layer) explain why step-independent windowing fails and why episode-level assignment eliminates both.
12	
13	\paragraph{GRPO Collapse and Training Instability.}
14	Several independent groups have documented collapse phenomena in GRPO-based training that corroborate our analysis. RAGEN-2~\cite{ragen2_2026} provides a mathematical proof of advantage collapse: when within-prompt reward variance approaches zero, task-relevant gradients vanish and KL regularization dominates, driving the policy back toward the reference model. GRPO-Collapse~\cite{grpocollapse2025} identifies the Lazy Likelihood-Displacement death spiral in Search-R1, where all four tested models collapse within 300 training steps. Gradient Coupling~\cite{gradientcoupling2025} challenges the ``reward miscalibration'' hypothesis and argues in Lemma~3.1 that flawed actions have naturally negative expected advantage; the true failure mode is gradient coupling from high input similarity across consecutive steps. This expected-value analysis is compatible with our per-sample sign analysis: expected advantages can be correct in aggregate (averaged over many samples) while per-sample signs remain near-random under high variance, precisely the regime where step-independent windowing operates. These independent observations converge on a shared conclusion that step-independent GRPO training is structurally unstable in multi-turn settings. Our work unifies these phenomena under a dual-mechanism diagnosis (M1 and M2) and validates the episode-level alternative through controlled training dynamics.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "7c661466-9619-44f9-889a-c7bfe2ba9319",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for Multi-Turn LLM Agents.}\nThe ReAct paradigm~\\cite{yao2023react} established interleaved reasoning and acting as the standard framework for LLM agents. Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath}, originally developed for mathematical reasoning, was scaled to large systems through dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn agents requires addressing the mismatch between its episode-level formulation and the memory constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has since become the community default: trajectories are partitioned into fixed-size windows, each optimized with an independently normalized baseline. Subsequent work improves training algorithms or reward design within this framework. GiGPO~\\cite{feng2025gigpo} estimates step-level advantages through a nested group structure without a learned critic. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy to provide denser signals than binary outcomes. SPEAR~\\cite{spear2025} combines self-imitation with progressive curriculum to mitigate sparse-reward starvation. DigiRL~\\cite{digiRL2024} demonstrates autonomous online RL for device-control agents. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction with dynamic context compression, and SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve the algorithm, the reward, or the training pipeline at various granularities, yet none diagnoses the step-independent windowing mechanism itself as a source of systematic sign errors. We identify and formalize this structural failure.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nTemporal credit assignment spans a well-studied spectrum. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance via a learned critic and clipped surrogate objectives. GAE~\\cite{schulman2016gae} interpolates between one-step TD and Monte Carlo returns through the $\\lambda$ parameter, with TD($\\lambda$)~\\cite{sutton1988td} establishing this interpolation in the tabular setting. RUDDER~\\cite{rudder2019} decomposes delayed rewards via sequence-to-sequence modeling but introduces bias whose correction slows exponentially with horizon. For LLM agents, AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates step-level value through Monte Carlo rollouts, and SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO with separate advantages for task-solving and skill-editing. In cooperative multi-agent RL, COMA~\\cite{foerster2018coma} and QMIX~\\cite{rashid2018qmix} address the analogous problem of attributing shared team rewards to individual agents via counterfactual baselines and value decomposition. Several independent studies provide direct evidence that step-independent credit assignment produces sign-level errors. IRC~\\cite{irc2026} reports that per-turn advantages $A^I$ frequently disagree in sign with outcome advantages $A^O$, with the resulting miscalibration causing a 14 percentage-point degradation (54\\% vs.\\ 68\\%). MC-GRPO~\\cite{mcgrpo2025} measures a 5\\% sign-flip rate and shows through controlled injection that this rate alone accounts for approximately 4\\% accuracy loss. GRPO-$\\lambda$~\\cite{grpolambda2025} proves in Lemma~1 that the value estimation error grows with sequence position, since the baseline $\\mu_t$ is biased for all $t > 0$. OAR~\\cite{oar2026} identifies ``reward aliasing'' arising from coarse-grained credit assignment. G-RA~\\cite{gra2025} visualizes accumulated reward diverging in sign from outcome reward. Decoupled-CA~\\cite{decoupledca2026} (under review) finds that invalid actions in positive-outcome trajectories receive positive credit and proposes multiplicative gated rewards to correct this. Episode-level GRPO, as we advocate, corresponds to GAE(1,1) without a critic: uniform advantage across all steps forfeits per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard practice produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Multi-Turn Agent Credit Assignment.}\nA parallel thread develops credit assignment methods specifically for multi-turn LLM agents. Turn-PPO~\\cite{turnppo2026} estimates turn-level advantages within PPO and reports that standard GRPO directly crashes on WebShop and Sokoban, with three proposed fixes all failing to recover. GiGPO~\\cite{feng2025gigpo} structures advantages at two scales (episode-level macro and step-level micro) and ablates both as indispensable. GAGPO~\\cite{gagpo2026} replaces Monte Carlo step advantages with TD/GAE-style recursive estimation. iStar~\\cite{istar2025} merges episode and step advantages at the token level but observes that token-level granularity increases fluctuation rather than improving stability. MT-GRPO~\\cite{mtgrpo2025} contrasts its turn-level method against an outcome-only GRPO baseline (GRPO-OR): 0.04 exact match versus 0.50, a 12$\\times$ gap that underscores the severity of multi-turn credit assignment failure. SWEET-RL~\\cite{sweetrl2025} finds that episode-level agents degrade sharply beyond 10 turns. These methods propose solutions to the multi-turn credit assignment problem. We complement them with a mechanistic diagnosis: two specific failure modes (policy information loss at the inference layer and advantage sign misattribution at the training layer) explain why step-independent windowing fails and why episode-level assignment eliminates both.\n\n\\paragraph{GRPO Collapse and Training Instability.}\nSeveral independent groups have documented collapse phenomena in GRPO-based training that corroborate our analysis. RAGEN-2~\\cite{ragen2_2026} provides a mathematical proof of advantage collapse: when within-prompt reward variance approaches zero, task-relevant gradients vanish and KL regularization dominates, driving the policy back toward the reference model. GRPO-Collapse~\\cite{grpocollapse2025} identifies the Lazy Likelihood-Displacement death spiral in Search-R1, where all four tested models collapse within 300 training steps. Gradient Coupling~\\cite{gradientcoupling2025} challenges the ``reward miscalibration'' hypothesis and argues in Lemma~3.1 that flawed actions have naturally negative expected advantage; the true failure mode is gradient coupling from high input similarity across consecutive steps. This expected-value analysis is compatible with our per-sample sign analysis: expected advantages can be correct in aggregate (averaged over many samples) while per-sample signs remain near-random under high variance, precisely the regime where step-independent windowing operates. These independent observations converge on a shared conclusion that step-independent GRPO training is structurally unstable in multi-turn settings. Our work unifies these phenomena under a dual-mechanism diagnosis (M1 and M2) and validates the episode-level alternative through controlled training dynamics.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01DhmtEEKdmQC6h5h8gquhbf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
  "offset": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "f7aa8195-4718-40a9-9dd2-f6151dc7f578",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014mZHt3iCzngY5Ev21NdV18",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1765,
      "cache_read_input_tokens": 52527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1765
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

_source line 24 · 2026-05-18T19:57:17.374Z_

<details><summary>↩ Tool result · `toolu_01DhmtEEKdmQC6h5h8gquhbf`</summary>

```text
250	}
251	
252	@article{yang2026ares,
253	  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},
254	  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},
255	  journal = {arXiv preprint arXiv:2603.07915},
256	  year    = {2026},
257	}
258	
259	@article{irc2026,
260	  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},
261	  author  = {Anonymous},
262	  journal = {arXiv preprint arXiv:2604.02869},
263	  year    = {2026},
264	}
265	
266	@article{mcgrpo2025,
267	  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},
268	  author  = {Kim, Youngeun},
269	  journal = {arXiv preprint arXiv:2601.22582},
270	  year    = {2025},
271	}
272	
273	@article{gra2025,
274	  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},
275	  author  = {Anonymous},
276	  journal = {arXiv preprint arXiv:2508.10548},
277	  year    = {2025},
278	}
279	
280	@article{grpolambda2025,
281	  title   = {{GRPO-$\lambda$}: Credit Assignment improves {LLM} Reasoning},
282	  author  = {Anonymous},
283	  journal = {arXiv preprint arXiv:2510.00194},
284	  year    = {2025},
285	}
286	
287	@article{oar2026,
288	  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},
289	  author  = {Anonymous},
290	  journal = {arXiv preprint arXiv:2601.07408},
291	  year    = {2026},
292	}
293	
294	@article{decoupledca2026,
295	  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},
296	  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},
297	  journal = {Submitted to ICLR 2026 (under review)},
298	  year    = {2026},
299	  note    = {OpenReview: Suja4AQ9Fo},
300	}
301	
302	@article{ragen2_2026,
303	  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {RL}},
304	  author  = {Anonymous},
305	  journal = {arXiv preprint arXiv:2604.06268},
306	  year    = {2026},
307	}
308	
309	@article{grpocollapse2025,
310	  title   = {On {GRPO} Collapse in {Search-R1}: The Lazy Likelihood-Displacement Death Spiral},
311	  author  = {Anonymous},
312	  journal = {arXiv preprint arXiv:2512.04220},
313	  year    = {2025},
314	}
315	
316	@article{gradientcoupling2025,
317	  title   = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic {RL}},
318	  author  = {Anonymous},
319	  journal = {arXiv preprint arXiv:2509.23870},
320	  year    = {2025},
321	}
322	
323	@article{turnppo2026,
324	  title   = {{Turn-PPO}: Turn-Level Advantage Estimation with {PPO} for Improved Multi-Turn {RL}},
325	  author  = {Anonymous},
326	  journal = {arXiv preprint arXiv:2512.17008},
327	  year    = {2026},
328	}
329	
330	@article{gagpo2026,
331	  title   = {{GAGPO}: Generalized Advantage Grouped Policy Optimization},
332	  author  = {Anonymous},
333	  journal = {arXiv preprint arXiv:2605.13217},
334	  year    = {2026},
335	}
336	
337	@article{istar2025,
338	  title   = {Agentic Reinforcement Learning with Implicit Step Rewards},
339	  author  = {Anonymous},
340	  booktitle = {Advances in Neural Information Processing Systems},
341	  year    = {2025},
342	}
343	
344	@article{mtgrpo2025,
345	  title   = {Reinforcing Multi-Turn Reasoning in {LLM} Agents via Turn-Level Credit Assignment},
346	  author  = {Anonymous},
347	  journal = {arXiv preprint arXiv:2505.11821},
348	  year    = {2025},
349	}
350	
351	@article{sweetrl2025,
352	  title   = {{SWEET-RL}: Training Multi-Turn {LLM} Agents on Collaborative Reasoning Tasks},
353	  author  = {Anonymous},
354	  journal = {arXiv preprint arXiv:2503.15478},
355	  year    = {2025},
356	}
357	
358	@inproceedings{rudder2019,
359	  title     = {{RUDDER}: Return Decomposition for Delayed Rewards},
360	  author    = {Arjona-Medina, Jose A. and Gillhofer, Michael and Widrich, Michael and Unterthiner, Thomas and Brandstetter, Johannes and Hochreiter, Sepp},
361	  booktitle = {Advances in Neural Information Processing Systems},
362	  year      = {2019},
363	}
364	
365	@article{ca_survey2026,
366	  title   = {From Reasoning to Agentic: Credit Assignment in {RL} for {LLMs}},
367	  author  = {Anonymous},
368	  journal = {arXiv preprint arXiv:2604.09459},
369	  year    = {2026},
370	}
371	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "0b351159-e879-4e02-be1d-4a964a94f06e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
      "content": "}\n\n@article{yang2026ares,\n  title   = {{ARES}: Adaptive Reasoning Effort Selection for Efficient {LLM} Agents},\n  author  = {Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu},\n  journal = {arXiv preprint arXiv:2603.07915},\n  year    = {2026},\n}\n\n@article{irc2026,\n  title   = {Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.02869},\n  year    = {2026},\n}\n\n@article{mcgrpo2025,\n  title   = {{MC-GRPO}: Median-Centered Group Relative Policy Optimization for Small-Rollout Reinforcement Learning},\n  author  = {Kim, Youngeun},\n  journal = {arXiv preprint arXiv:2601.22582},\n  year    = {2025},\n}\n\n@article{gra2025,\n  title   = {Stabilizing Long-term Multi-turn Reinforcement Learning with Gated Rewards},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2508.10548},\n  year    = {2025},\n}\n\n@article{grpolambda2025,\n  title   = {{GRPO-$\\lambda$}: Credit Assignment improves {LLM} Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2510.00194},\n  year    = {2025},\n}\n\n@article{oar2026,\n  title   = {Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2601.07408},\n  year    = {2026},\n}\n\n@article{decoupledca2026,\n  title   = {Both Local Validity and Global Effectiveness Matter: Decoupled Credit Assignment for Long-Horizon Agentic Learning},\n  author  = {Lu, Wenxuan and Zhang, Zhanqiu and Guo, Steven Y. and Zang, Tianning},\n  journal = {Submitted to ICLR 2026 (under review)},\n  year    = {2026},\n  note    = {OpenReview: Suja4AQ9Fo},\n}\n\n@article{ragen2_2026,\n  title   = {{RAGEN-2}: Reasoning Collapse in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.06268},\n  year    = {2026},\n}\n\n@article{grpocollapse2025,\n  title   = {On {GRPO} Collapse in {Search-R1}: The Lazy Likelihood-Displacement Death Spiral},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.04220},\n  year    = {2025},\n}\n\n@article{gradientcoupling2025,\n  title   = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2509.23870},\n  year    = {2025},\n}\n\n@article{turnppo2026,\n  title   = {{Turn-PPO}: Turn-Level Advantage Estimation with {PPO} for Improved Multi-Turn {RL}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2512.17008},\n  year    = {2026},\n}\n\n@article{gagpo2026,\n  title   = {{GAGPO}: Generalized Advantage Grouped Policy Optimization},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2605.13217},\n  year    = {2026},\n}\n\n@article{istar2025,\n  title   = {Agentic Reinforcement Learning with Implicit Step Rewards},\n  author  = {Anonymous},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year    = {2025},\n}\n\n@article{mtgrpo2025,\n  title   = {Reinforcing Multi-Turn Reasoning in {LLM} Agents via Turn-Level Credit Assignment},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2505.11821},\n  year    = {2025},\n}\n\n@article{sweetrl2025,\n  title   = {{SWEET-RL}: Training Multi-Turn {LLM} Agents on Collaborative Reasoning Tasks},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2503.15478},\n  year    = {2025},\n}\n\n@inproceedings{rudder2019,\n  title     = {{RUDDER}: Return Decomposition for Delayed Rewards},\n  author    = {Arjona-Medina, Jose A. and Gillhofer, Michael and Widrich, Michael and Unterthiner, Thomas and Brandstetter, Johannes and Hochreiter, Sepp},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{ca_survey2026,\n  title   = {From Reasoning to Agentic: Credit Assignment in {RL} for {LLMs}},\n  author  = {Anonymous},\n  journal = {arXiv preprint arXiv:2604.09459},\n  year    = {2026},\n}\n",
      "numLines": 122,
      "startLine": 250,
      "totalLines": 371
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Both files look correct. Let me verify:

1. `related_work.tex` - 4 paragraphs matching D073 narrative, all positioning sentences in place, no em-dash/en-dash, no -ing endings, no paper listing style, proper citations
2. `references.bib` - 16 new entries appended after the existing last entry (yang2026ares)

All citation verification constraints met:
- GRPO-λ: "proves in Lemma~1 that the value estimation error grows with sequence position" ✓


- OAR: "identifies ``reward aliasing'' arising from coarse-grained credit assignment" ✓
- Decoupled-CA: "(under review)" ✓
- IRC: "14 percentage-point degradation (54\% vs.\ 68\%)" ✓

Everything checks out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "4709f873-2aeb-4899-8b97-1d10dfafded7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BRHnaY4ZnTTcSCM6CZNfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3919,
      "cache_read_input_tokens": 54292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3919
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

_source line 26_

完成。两个文件已更新：

- `related_work.tex`：4 段结构（Multi-Turn RL / Credit Assignment / Multi-Turn CA / GRPO Collapse），每段末尾有定位句，~870 words，无 em-dash、无 -ing 结尾、无论文堆砌
- `references.bib`：末尾添加 16 个新条目（irc2026, mcgrpo2025, gra2025, grpolambda2025, oar2026, decoupledca2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, istar2025, mtgrpo2025, sweetrl2025, rudder2019, ca_survey2026）

引用验证约束已遵守：GRPO-λ 用 "Lemma 1 bounds value estimation error"、OAR 用 "reward aliasing"、Decoupled-CA 标注 under review、IRC 用 14pp (54% vs 68%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "uuid": "24fd7053-0153-42a9-b1ef-540ba6bd940f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BRHnaY4ZnTTcSCM6CZNfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3919,
      "cache_read_input_tokens": 54292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3919
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

_source line 27_

完成。两个文件已更新：

- `related_work.tex`：4 段结构（Multi-Turn RL / Credit Assignment / Multi-Turn CA / GRPO Collapse），每段末尾有定位句，~870 words，无 em-dash、无 -ing 结尾、无论文堆砌
- `references.bib`：末尾添加 16 个新条目（irc2026, mcgrpo2025, gra2025, grpolambda2025, oar2026, decoupledca2026, ragen2_2026, grpocollapse2025, gradientcoupling2025, turnppo2026, gagpo2026, istar2025, mtgrpo2025, sweetrl2025, rudder2019, ca_survey2026）

引用验证约束已遵守：GRPO-λ 用 "Lemma 1 bounds value estimation error"、OAR 用 "reward aliasing"、Decoupled-CA 标注 under review、IRC 用 14pp (54% vs 68%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158697,
  "duration_api_ms": 159498,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "ca591248-6b5b-4021-aeff-06d601112051",
  "total_cost_usd": 0.5916565,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 46510,
    "cache_read_input_tokens": 188394,
    "output_tokens": 8047,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 46510,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 491,
        "cache_read_input_tokens": 54292,
        "cache_creation_input_tokens": 3919,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3919
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 5467,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.005561999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 8047,
      "cacheReadInputTokens": 188394,
      "cacheCreationInputTokens": 46510,
      "webSearchRequests": 0,
      "costUSD": 0.5860945,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e882bcd0-3886-4dea-8c8e-bc747361edbf"
}
```

</details>

---
