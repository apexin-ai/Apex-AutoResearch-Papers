# paper writing experiments setup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper_writing_experiments_setup_20260518T201250.log`
- **Structured JSON:** [`50e63d83c3b977fc2c97.json`](../../sessions/50/50e63d83c3b977fc2c97.json)

## Before a recorded user message

48 recorded events

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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
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
  "uuid": "2f8a1707-bd75-462f-91eb-e48ea8cb3d26",
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
  "uuid": "2f90f1df-99ee-4601-aa40-0821e8ac874f",
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417"
}
```

---

### Assistant

_source line 4_

I'll start by reading the writing norms, LaTeX skill, and current experiments.tex in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "f30ae0f7-556c-442a-b53e-9d73adce6754",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUcBtCq7kmJRankCmohf4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9010,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9010
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

<details open><summary>🔧 Tool call — Read · `toolu_0164nNYSE94gXrCn4hNXNbbV`</summary>

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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "1b9a9fda-3f27-4ade-a294-1a290390eb97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUcBtCq7kmJRankCmohf4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9010,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9010
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

_source line 6 · 2026-05-18T20:13:01.692Z_

<details><summary>↩ Tool result · `toolu_0164nNYSE94gXrCn4hNXNbbV`</summary>

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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "d9203c06-0c5b-4813-812f-cbb1a1a723d4",
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

<details open><summary>🔧 Tool call — Read · `toolu_018kLmwkwnJtAhxTuym9z6VW`</summary>

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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "22bb8f5d-77b1-47ba-9cb7-d002e18f185c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUcBtCq7kmJRankCmohf4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9010,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9010
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

_source line 8 · 2026-05-18T20:13:02.032Z_

<details><summary>↩ Tool result · `toolu_018kLmwkwnJtAhxTuym9z6VW`</summary>

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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "75aa8ebe-211d-4d10-a025-3ed6eedaa397",
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

<details open><summary>🔧 Tool call — Read · `toolu_01R5cckQnGh973mLYbYK1tVd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "9eb26e44-eef5-4a98-a3fa-f15332b0a77c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUcBtCq7kmJRankCmohf4s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9010,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9010
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

_source line 10 · 2026-05-18T20:13:02.757Z_

<details><summary>↩ Tool result · `toolu_01R5cckQnGh973mLYbYK1tVd`</summary>

```text
1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\ref{sec:m2_sign_misattribution}?
7	
8	\subsection{Experimental Setup}
9	\label{sec:experimental_setup}
10	
11	\paragraph{Environment.}
12	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands.
13	ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R \in \{0, r_+\}$, with $r_+$ for successful task completion and $0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.
14	
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.
16	
17	\paragraph{Base model.}
18	We use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\% success rate on a held-out 32-episode validation set (4/32 episodes), providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.125$ with group size $K = 8$, Proposition 2 (Section~\ref{sec:formal_probability}) predicts that approximately 80.9\% of gradient updates carry incorrect sign under step-independent training.
19	
20	\paragraph{RL training configuration.}
21	We train using the RAGEN framework~\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:
22	\begin{itemize}
23	    \item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)
24	    \item Learning rate: $1 \times 10^{-6}$
25	    \item KL penalty coefficient: $\beta = 0.01$ (low-variance KL)
26	    \item Discount factor: $\gamma = 0.95$ (applied in step-independent return computation via Equation~\ref{eq:step_return}; not applicable to episode-level mode)
27	    \item Invalid action penalty coefficient: 0.1
28	    \item Training data: 16 task instances per training step
29	    \item Training steps: 15 (early-stopped based on convergence)
30	\end{itemize}
31	
32	\paragraph{Evaluation protocol.}
33	We evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \in \{2, 4, 8\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.
34	
35	\subsection{Window-Size Ablation}
36	\label{sec:window_ablation}
37	
38	To disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.
39	
40	\paragraph{Conditions.}
41	We vary the step-independent history length $h \in \{2, 5, 10, 20\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \texttt{step\_independent} training mode with \texttt{step\_independent\_history\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.
42	
43	\paragraph{Design rationale.}
44	The five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.
45	
46	\paragraph{Controls.}
47	All conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. \placeholder{plan\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}
48	
49	\paragraph{Post-hoc evaluation.}
50	To isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).
51	
52	\subsection{Results}
53	\label{sec:results}
54	
55	\subsubsection{Episode-Level vs. Step-Independent Training}
56	\label{sec:results_main}
57	
58	The central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\% validation success at training step 15, a 2.25$\times$ improvement over the SFT baseline of 12.5\%. Step-independent training with $h = 2$ collapses to 0\% training success by step 11.
59	
60	\placeholder{tab1\_main\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\%), Action Valid (\%), Pass@8. Multi-seed mean$\pm$std from plan\_003.}
61	
62	\placeholder{fig6\_training\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}
63	
64	The collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), training success drops from 18.75\% to single digits while training action validity remains high at approximately 89.3\% (training, step 2). The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), training action validity itself collapses from 89.3\% to 43.1\% (training, steps 2$\to$4). Note that training success (computed from rollouts during optimization) differs from validation success (pass@1 on the held-out 32-episode set evaluated every 5 steps); the 18.75\% training success at step 0 reflects the SFT checkpoint's performance across the training task distribution. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.
65	
66	Episode-level training exhibits no such collapse. Success rate shows consistent improvement from the SFT baseline to 28.1\% at step 15, with action validity at 54.5\%. This pattern is consistent with the policy acquiring task-solving strategies that operate outside the predefined action template vocabulary. Notably, task success (the primary objective) improves despite lower template compliance, suggesting the model develops effective but syntactically unconventional action sequences. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.
67	
68	\subsubsection{Window-Size Ablation}
69	\label{sec:results_hsweep}
70	
71	\placeholder{tab2\_h\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \in \{2, 5, 10, 20, \text{full}\}$, 3 seeds per $h$.}
72	
73	\placeholder{fig5\_h\_sweep\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (12.5\%).}
74	
75	The ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.
76	
77	The dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.
78	
79	From the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Training action validity at step 2 is 89.3\%, dropping to 43.1\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.
80	
81	\subsubsection{Dense Reward Baseline}
82	\label{sec:results_dense}
83	
84	A natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.
85	
86	The dense reward baseline produces a clear dissociation. Action validity increases from 60\% to 97.5\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, validation success remains at 0\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.
87	
88	This result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.
89	
90	\subsection{Empirical Verification of Sign Misattribution}
91	\label{sec:sign_verification}
92	
93	The theoretical analysis of Section~\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions. Crucially, the empirical verification uses the full reward structure including invalid action penalties (coefficient 0.1), not the simplified binary reward assumed by Proposition~2. Confirmation under non-binary rewards strengthens the generality of the sign misattribution mechanism beyond the analytical assumptions.
94	
95	\paragraph{Methodology.}
96	During step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\text{sign}(\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\text{episode}}^{(i)} \in \{0, 1\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:
97	\begin{itemize}
98	    \item \textbf{Sign-outcome correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and $R_{\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.
99	    \item \textbf{Sign-quality correlation}: the Pearson correlation between $\text{sign}(\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.
100	    \item \textbf{Correct sign fraction}: $P(\text{correct sign} \mid \text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\ref{sec:formal_probability}) predicts this equals approximately 19.1\% at $p = 12.5\%$, $K = 8$.
101	\end{itemize}
102	
103	\paragraph{Predictions.}
104	The sign misattribution mechanism makes three testable predictions:
105	\begin{enumerate}
106	    \item Sign-outcome correlation $\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)
107	    \item Sign-quality correlation $\approx 0$ (advantage sign is independent of whether local actions were good)
108	    \item $P(\text{correct sign}) \approx 19.1\%$ (derived from Proposition 2 at the observed success rate)
109	\end{enumerate}
110	If all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.
111	
112	\placeholder{tab3\_mechanism\_verification: Sign misattribution empirical verification. Columns: Metric, Measured Value, Theoretical Prediction, Agreement. Rows: sign-outcome correlation, sign-quality correlation, $P(\text{correct sign})$. Data from plan\_004 per-window advantage logging.}
113	
114	\subsection{Additional Baselines}
115	\label{sec:additional_baselines}
116	
117	\paragraph{GAE baselines.}
118	To distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} under two configurations. GAE($\lambda = 0.95$, $\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\lambda = 1$, $\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \placeholder{plan\_003b: GAE baseline execution. Columns: Method, Val Success (\%), Action Valid (\%), Training Stability (variance across steps).}
119	
120	\paragraph{Selective verification.}
121	\label{sec:selective_experiments}
122	Building on the episode-level trained agent (Section~\ref{sec:selective_verification}), we propose training a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and would demonstrate a downstream application of the competent base agent produced by episode-level training. \placeholder{tab4\_selective\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\%), Verify Rate (\%), Cost Reduction (\%). Pending Phase B experiments.}
123	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "81388e1b-dafa-4f3f-8b02-8f8b2fa5ed00",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
      "content": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\\ref{sec:m2_sign_misattribution}?\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\n\\paragraph{Environment.}\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands.\nALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ for successful task completion and $0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.\n\nALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.\n\n\\paragraph{Base model.}\nWe use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-episode validation set (4/32 episodes), providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.125$ with group size $K = 8$, Proposition 2 (Section~\\ref{sec:formal_probability}) predicts that approximately 80.9\\% of gradient updates carry incorrect sign under step-independent training.\n\n\\paragraph{RL training configuration.}\nWe train using the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:\n\\begin{itemize}\n    \\item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)\n    \\item Learning rate: $1 \\times 10^{-6}$\n    \\item KL penalty coefficient: $\\beta = 0.01$ (low-variance KL)\n    \\item Discount factor: $\\gamma = 0.95$ (applied in step-independent return computation via Equation~\\ref{eq:step_return}; not applicable to episode-level mode)\n    \\item Invalid action penalty coefficient: 0.1\n    \\item Training data: 16 task instances per training step\n    \\item Training steps: 15 (early-stopped based on convergence)\n\\end{itemize}\n\n\\paragraph{Evaluation protocol.}\nWe evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \\in \\{2, 4, 8\\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \\textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.\n\n\\subsection{Window-Size Ablation}\n\\label{sec:window_ablation}\n\nTo disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.\n\n\\paragraph{Conditions.}\nWe vary the step-independent history length $h \\in \\{2, 5, 10, 20\\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \\texttt{step\\_independent} training mode with \\texttt{step\\_independent\\_history\\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.\n\n\\paragraph{Design rationale.}\nThe five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.\n\n\\paragraph{Controls.}\nAll conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. \\placeholder{plan\\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}\n\n\\paragraph{Post-hoc evaluation.}\nTo isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).\n\n\\subsection{Results}\n\\label{sec:results}\n\n\\subsubsection{Episode-Level vs. Step-Independent Training}\n\\label{sec:results_main}\n\nThe central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\\% validation success at training step 15, a 2.25$\\times$ improvement over the SFT baseline of 12.5\\%. Step-independent training with $h = 2$ collapses to 0\\% training success by step 11.\n\n\\placeholder{tab1\\_main\\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\\%), Action Valid (\\%), Pass@8. Multi-seed mean$\\pm$std from plan\\_003.}\n\n\\placeholder{fig6\\_training\\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}\n\nThe collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), training success drops from 18.75\\% to single digits while training action validity remains high at approximately 89.3\\% (training, step 2). The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), training action validity itself collapses from 89.3\\% to 43.1\\% (training, steps 2$\\to$4). Note that training success (computed from rollouts during optimization) differs from validation success (pass@1 on the held-out 32-episode set evaluated every 5 steps); the 18.75\\% training success at step 0 reflects the SFT checkpoint's performance across the training task distribution. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.\n\nEpisode-level training exhibits no such collapse. Success rate shows consistent improvement from the SFT baseline to 28.1\\% at step 15, with action validity at 54.5\\%. This pattern is consistent with the policy acquiring task-solving strategies that operate outside the predefined action template vocabulary. Notably, task success (the primary objective) improves despite lower template compliance, suggesting the model develops effective but syntactically unconventional action sequences. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.\n\n\\subsubsection{Window-Size Ablation}\n\\label{sec:results_hsweep}\n\n\\placeholder{tab2\\_h\\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \\in \\{2, 5, 10, 20, \\text{full}\\}$, 3 seeds per $h$.}\n\n\\placeholder{fig5\\_h\\_sweep\\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (12.5\\%).}\n\nThe ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.\n\nThe dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.\n\nFrom the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Training action validity at step 2 is 89.3\\%, dropping to 43.1\\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.\n\n\\subsubsection{Dense Reward Baseline}\n\\label{sec:results_dense}\n\nA natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.\n\nThe dense reward baseline produces a clear dissociation. Action validity increases from 60\\% to 97.5\\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, validation success remains at 0\\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.\n\nThis result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.\n\n\\subsection{Empirical Verification of Sign Misattribution}\n\\label{sec:sign_verification}\n\nThe theoretical analysis of Section~\\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions. Crucially, the empirical verification uses the full reward structure including invalid action penalties (coefficient 0.1), not the simplified binary reward assumed by Proposition~2. Confirmation under non-binary rewards strengthens the generality of the sign misattribution mechanism beyond the analytical assumptions.\n\n\\paragraph{Methodology.}\nDuring step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\\text{sign}(\\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\\text{episode}}^{(i)} \\in \\{0, 1\\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:\n\\begin{itemize}\n    \\item \\textbf{Sign-outcome correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and $R_{\\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.\n    \\item \\textbf{Sign-quality correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.\n    \\item \\textbf{Correct sign fraction}: $P(\\text{correct sign} \\mid \\text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\\ref{sec:formal_probability}) predicts this equals approximately 19.1\\% at $p = 12.5\\%$, $K = 8$.\n\\end{itemize}\n\n\\paragraph{Predictions.}\nThe sign misattribution mechanism makes three testable predictions:\n\\begin{enumerate}\n    \\item Sign-outcome correlation $\\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)\n    \\item Sign-quality correlation $\\approx 0$ (advantage sign is independent of whether local actions were good)\n    \\item $P(\\text{correct sign}) \\approx 19.1\\%$ (derived from Proposition 2 at the observed success rate)\n\\end{enumerate}\nIf all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.\n\n\\placeholder{tab3\\_mechanism\\_verification: Sign misattribution empirical verification. Columns: Metric, Measured Value, Theoretical Prediction, Agreement. Rows: sign-outcome correlation, sign-quality correlation, $P(\\text{correct sign})$. Data from plan\\_004 per-window advantage logging.}\n\n\\subsection{Additional Baselines}\n\\label{sec:additional_baselines}\n\n\\paragraph{GAE baselines.}\nTo distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} under two configurations. GAE($\\lambda = 0.95$, $\\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\\lambda = 1$, $\\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \\placeholder{plan\\_003b: GAE baseline execution. Columns: Method, Val Success (\\%), Action Valid (\\%), Training Stability (variance across steps).}\n\n\\paragraph{Selective verification.}\n\\label{sec:selective_experiments}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we propose training a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and would demonstrate a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}\n",
      "numLines": 123,
      "startLine": 1,
      "totalLines": 123
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
Now I have all the context I need. Let me also check the references.bib to make sure I reference the right citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "7fea23f4-32a5-4648-b0b7-f2e002e80736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7giNChgjF64mDTbjuStku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21682,
      "cache_read_input_tokens": 20711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21682
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

Let me check the references.bib for citation keys I'll need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "01e1f332-a6b6-4d9a-911c-beb10a40cf0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7giNChgjF64mDTbjuStku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21682,
      "cache_read_input_tokens": 20711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21682
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

<details open><summary>🔧 Tool call — Grep · `toolu_01HLJDcLCf4ZS6n5sWbx3dHb`</summary>

```json
{
  "pattern": "@\\w+\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "dcc9342b-ae1b-4568-8c38-2cdbeb73730a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7giNChgjF64mDTbjuStku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21682,
      "cache_read_input_tokens": 20711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21682
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

_source line 14 · 2026-05-18T20:13:08.571Z_

<details><summary>↩ Tool result · `toolu_01HLJDcLCf4ZS6n5sWbx3dHb`</summary>

```text
1:@inproceedings{shridhar2021alfworld,
8:@inproceedings{agent-omit2026,
15:@article{choudhury2025agentprm,
22:@article{dapo2025,
29:@inproceedings{foerster2018coma,
36:@inproceedings{digiRL2024,
43:@inproceedings{du2025thinkless,
50:@inproceedings{feng2025gigpo,
57:@article{hcapo2026,
64:@article{kamoi2024self-correction-survey,
71:@inproceedings{kim2025reflact,
78:@article{li2025sorl,
85:@article{long2026selfverification,
92:@inproceedings{rashid2018qmix,
99:@article{ragen2025,
106:@inproceedings{yao2023react,
113:@inproceedings{schulman2016gae,
120:@article{schulman2017ppo,
127:@article{selfbudgeter2025,
134:@article{selfguide2026,
141:@article{shao2024deepseekmath,
148:@article{sherlock2025,
155:@article{skillmaster2026,
162:@inproceedings{spear2025,
169:@article{sutton1988td,
179:@inproceedings{tie2025correctbench,
186:@inproceedings{tu2025autothink,
193:@inproceedings{verifiagent2025,
200:@inproceedings{wan2025derailer-rerailer,
207:@inproceedings{wang2022scienceworld,
214:@inproceedings{yao2022webshop,
221:@inproceedings{zhou2024webarena,
228:@inproceedings{wei2025webagent-r1,
235:@article{williams1992reinforce,
245:@inproceedings{xi2025agentprm,
252:@article{yang2026ares,
259:@article{irc2026,
266:@article{mcgrpo2025,
273:@article{gra2025,
280:@article{grpolambda2025,
287:@article{oar2026,
294:@article{decoupledca2026,
302:@article{ragen2_2026,
309:@article{grpocollapse2025,
316:@article{gradientcoupling2025,
323:@article{turnppo2026,
330:@article{gagpo2026,
337:@inproceedings{istar2025,
344:@article{mtgrpo2025,
351:@article{sweetrl2025,
358:@inproceedings{rudder2019,
365:@article{ca_survey2026,
372:@inproceedings{archer2024,
379:@article{hiper2026,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "0221d8f6-4188-420b-95be-53e8f1542f25",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:@inproceedings{shridhar2021alfworld,\n8:@inproceedings{agent-omit2026,\n15:@article{choudhury2025agentprm,\n22:@article{dapo2025,\n29:@inproceedings{foerster2018coma,\n36:@inproceedings{digiRL2024,\n43:@inproceedings{du2025thinkless,\n50:@inproceedings{feng2025gigpo,\n57:@article{hcapo2026,\n64:@article{kamoi2024self-correction-survey,\n71:@inproceedings{kim2025reflact,\n78:@article{li2025sorl,\n85:@article{long2026selfverification,\n92:@inproceedings{rashid2018qmix,\n99:@article{ragen2025,\n106:@inproceedings{yao2023react,\n113:@inproceedings{schulman2016gae,\n120:@article{schulman2017ppo,\n127:@article{selfbudgeter2025,\n134:@article{selfguide2026,\n141:@article{shao2024deepseekmath,\n148:@article{sherlock2025,\n155:@article{skillmaster2026,\n162:@inproceedings{spear2025,\n169:@article{sutton1988td,\n179:@inproceedings{tie2025correctbench,\n186:@inproceedings{tu2025autothink,\n193:@inproceedings{verifiagent2025,\n200:@inproceedings{wan2025derailer-rerailer,\n207:@inproceedings{wang2022scienceworld,\n214:@inproceedings{yao2022webshop,\n221:@inproceedings{zhou2024webarena,\n228:@inproceedings{wei2025webagent-r1,\n235:@article{williams1992reinforce,\n245:@inproceedings{xi2025agentprm,\n252:@article{yang2026ares,\n259:@article{irc2026,\n266:@article{mcgrpo2025,\n273:@article{gra2025,\n280:@article{grpolambda2025,\n287:@article{oar2026,\n294:@article{decoupledca2026,\n302:@article{ragen2_2026,\n309:@article{grpocollapse2025,\n316:@article{gradientcoupling2025,\n323:@article{turnppo2026,\n330:@article{gagpo2026,\n337:@inproceedings{istar2025,\n344:@article{mtgrpo2025,\n351:@article{sweetrl2025,\n358:@inproceedings{rudder2019,\n365:@article{ca_survey2026,\n372:@inproceedings{archer2024,\n379:@article{hiper2026,",
    "numLines": 54
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the citation keys. Let me also check the registry for exp028_prereq_zeroshot and exp029 data to see if I can get SFT OOD baseline numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "db0d57c9-bc23-411b-aa14-bf0102ade3d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjdmDBXdkTgXHzB8cYY2nM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 42393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 953
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

Now let me check for OOD baseline data from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "520e5e14-a33d-42a2-a756-3a2581b5dfa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjdmDBXdkTgXHzB8cYY2nM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 42393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 953
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013Wg8mfStqV8BfCQuKP2WwK`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "49df5330-2487-4218-9a93-d0c8a9d1637a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjdmDBXdkTgXHzB8cYY2nM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 42393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 953
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

_source line 18 · 2026-05-18T20:13:13.170Z_

<details><summary>↩ Tool result · `toolu_013Wg8mfStqV8BfCQuKP2WwK`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "cefac10b-12b8-48a4-86d2-eb71e6e5d61c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AnLRAvg56kcicXNvC7nyTr`</summary>

```json
{
  "filters": {
    "experiment_id": "exp029"
  },
  "project": "cost-verify-agent-rl",
  "fields": [
    "*"
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "849b501e-d377-4bf1-9580-6c9f6f3ccb87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U7whEW6xMvC26fqCehXtM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 43346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
      },
      "output_tokens": 48,
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

_source line 20 · 2026-05-18T20:13:16.998Z_

<details><summary>↩ Tool result · `toolu_01AnLRAvg56kcicXNvC7nyTr`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2319}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "3da66e27-df20-46af-be5a-b4eb92174392",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2319}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2319}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_0124CnP7KPjs2eixaSLfoyfk`</summary>

```json
{
  "filters": {
    "experiment_id": "exp028_prereq_zeroshot"
  },
  "project": "cost-verify-agent-rl",
  "fields": [
    "*"
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "1bb50d5b-a609-4132-b0af-e26b3c0a65bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U7whEW6xMvC26fqCehXtM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 43346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
      },
      "output_tokens": 48,
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

_source line 22 · 2026-05-18T20:13:17.359Z_

<details><summary>↩ Tool result · `toolu_0124CnP7KPjs2eixaSLfoyfk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2029}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "363cc845-226b-4a5b-8b41-df654c408704",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2029}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2029}}"
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
The registry doesn't have exp029 or exp028_prereq_zeroshot. Let me check with different filter approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "05c4122f-9668-4c85-8c6b-e6b94cab6600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kk7zyh4t9FLTERKSv2o7XR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 43866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 533
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

Let me check the registry more broadly for relevant experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "7ef78d6f-0dba-486d-9cfa-ded1e0b45cc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kk7zyh4t9FLTERKSv2o7XR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 43866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 533
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01KrzbmLXD3V7V5Abf5vVbBG`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "db0c3c81-ad18-42f6-8548-76ee9ef3df79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kk7zyh4t9FLTERKSv2o7XR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 43866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 533
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

_source line 26 · 2026-05-18T20:13:21.293Z_

<details><summary>↩ Tool result · `toolu_01KrzbmLXD3V7V5Abf5vVbBG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"hsweep_h20_seed1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-18T18:04:42.684Z\", \"updated_at\": \"2026-05-18T19:14:40.086Z\", \"hypothesis\": \"h=20 with step_independent generation provides 20-step observation windows. Key data point for fig5 cliff figure: with h=10 and h=5 both collapsing, h=20 tests whether 20 steps of context is sufficient for recovery. If h=20 recovers (val > 0% at step 5+), the cliff is between h=10 and h=20. If still collapsed, the minimum viable context window is larger than 20 steps.\", \"parent\": \"hsweep_h10_seed1\", \"notes\": \"诊断中: worker_diagnose_hsweep_h20_seed1_20260518T184044 正在 SSH 深查失败原因。日志尾部无 Traceback，疑似系统级 kill (OOM/磁盘)。\"}, \"hsweep_h10_seed1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T17:30:46.964Z\", \"updated_at\": \"2026-05-18T19:09:46.781Z\", \"hypothesis\": \"h=10 with step_independent generation provides 10-step observation windows. Key data point for fig5 cliff figure: if h=10 shows recovery (val > 0%), the cliff is between h=5 and h=10. If still collapsed, cliff is between h=10 and full context (h=28).\", \"parent\": \"hsweep_h2_seed1\", \"notes\": \"Director 批准临时 kill（刚启动几分钟，无进度损失）以释放 bjb1 cuda:0,1 跑 exp029 + hsweep_h2_seed2 双 reeval。Reeval 完成后重启。原由 auto_next_hsweep.sh 自动启动，未经正式审批。\"}, \"factorial_h2_episodeadv_seed2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-18T04:48:02.228Z\", \"updated_at\": \"2026-05-18T18:25:27.297Z\", \"hypothesis\": \"Replicate factorial experiment (step-independent + episode-level advantage) with different seed to confirm that sign misattribution elimination is robust, not single-seed artifact. Same config, different seed, 15 steps.\", \"parent\": \"factorial_h2_episodeadv_seed1\"}, \"exp029_episode_level_seed2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:48:01.826Z\", \"updated_at\": \"2026-05-18T18:25:16.249Z\", \"hypothesis\": \"Replicate exp029 episode-level result (23.88% OOD) with different seed to confirm statistical robustness. P0 priority: core positive claim built on single seed is desk-reject risk. Same SFT checkpoint, same config, seed=43, 15 steps, AlfworldSG_OOD 134 tasks eval.\", \"parent\": \"exp029_episode_level\", \"conclusion\": \"killed\", \"notes\": \"Director 止损 kill。bjb1 累计 10+ 次失败。step 15 val=21.875% (32 tasks)，数据保留在 /root/autodl-tmp/checkpoints/exp029-seed2/。计划转移到 westd cuda:0,1 继续（factorial 完成后）。\"}, \"gsweep_g100_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:58.033Z\", \"updated_at\": \"2026-05-18T17:36:39.529Z\", \"hypothesis\": \"γ=1.0 (no discount) tests whether collapse in h=5 is caused by sign misattribution from magnitude decay. If γ=1.0 also collapses, sign misattribution is not solely from discount-induced magnitude decay.\", \"parent\": \"gsweep_g095_h5_seed1\", \"conclusion\": \"negative\", \"metrics\": {\"conclusion_reason\": \"collapsed, γ=1.0 also collapses confirming sign misattribution not solely from magnitude decay\"}}, \"gsweep_g095_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:55.994Z\", \"updated_at\": \"2026-05-18T13:11:09.941Z\", \"hypothesis\": \"γ=0.95 with h=5 is the control condition matching hsweep_h5. Early windows retain γ^9 ≈ 0.95^9 ≈ 63% of terminal return. Expected to reproduce h5 behavior from h-sweep.\", \"parent\": \"hsweep_h2_seed1\", \"conclusion\": \"negative\", \"metrics\": {\"val_success_step5\": 0, \"conclusion_reason\": \"collapsed at step 5, val=0%\"}}, \"factorial_h2_episodeadv_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:17:23.327Z\", \"updated_at\": \"2026-05-18T10:22:36.071Z\", \"hypothesis\": \"Step_independent generation (h=2) with episode-level advantage eliminates sign misattribution while preserving truncated-context inference. If success >> h=2 step-level (0%), information loss alone does not cause collapse — sign misattribution is the primary driver. If success ≈ 0%, information loss is sufficient to cause collapse regardless of advantage computation. This is the key factorial experiment separating the two mechanisms.\", \"parent\": \"hsweep_h2_seed1\", \"metrics\": {\"completed_steps\": \"15/15\", \"wandb_run_id\": \"6liw7fm1\", \"val_step5\": {\"success\": 0.0597, \"dataset\": \"AlfworldOOD_134tasks\"}, \"val_step15\": {\"success\": 0.0075}, \"kl_loss_trajectory\": {\"step1\": 0.238, \"step5\": 0.735, \"step10\": 1.029, \"step15\": 2.845}, \"ppo_kl_range\": \"0.025-0.096\", \"best_checkpoint\": \"global_step_5\", \"best_val_success\": 0.0597, \"train_step1\": {\"success\": 0.203, \"pass_at_8\": 0.688}, \"train_step6\": {\"success\": 0.258, \"pass_at_8\": 0.813}, \"checkpoint_paths\": {\"step5\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_5/\", \"step10\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_10/\", \"step15\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_15/\"}, \"exit_cause\": \"W&B atexit BrokenPipeError (false positive)\", \"kl_issue\": \"kl_loss_coef=0.01 too low, policy drifted after step 5\", \"status_note\": \"COMPLETED. Best val OOD 5.97% at step 5. Degraded to 0.75% by step 15 due to KL drift. Sign misattribution elimination confirmed: 5.97% vs 0% (step-level h=2).\"}, \"notes\": \"W&B 深度分析确认：sign misattribution 是 collapse 的 primary driver。关键证据：step 3→4 hsweep action_valid 91.3%→43.1% (catastrophic collapse) vs factorial 保�� 79-85% (无崩溃)。V-shaped recovery (20.3%→3.1%→15.63%) 是探索期波动非不可逆退化。3-cell 贡献：sign misattribution ~6pp (0%→5.97% val), information loss ~22pp (5.97%→28.1% val)。Sign misattribution pp 贡献较小但是 catastrophic collapse 的质变 trigger。\", \"conclusion\": \"success\"}, \"gsweep_g080_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:53.634Z\", \"updated_at\": \"2026-05-18T09:35:23.404Z\", \"hypothesis\": \"γ=0.8 with h=5 represents an intermediate decay rate where early windows retain γ^9 ≈ 0.8^9 ≈ 13% of terminal return, potentially showing delayed but still present collapse compared to γ=0.95 (39%).\", \"parent\": \"hsweep_h2_seed1\", \"metrics\": {\"step5_val_success\": \"3.125%\", \"step5_entropy\": 0.185, \"subsequent_steps\": \"all 0%\", \"conclusion_note\": \"Complete collapse confirmed. γ=0.80 with h=5 shows catastrophic failure — killed early by Director as no new information expected. Supports hypothesis that lower gamma accelerates collapse.\"}, \"conclusion\": \"negative\"}, \"hsweep_h2_seed2_reeval_ood\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:12:03.656Z\", \"updated_at\": \"2026-05-18T05:13:33.875Z\", \"hypothesis\": \"Evaluate hsweep_h2_seed2 checkpoint (step 15) on OOD 134 tasks to get comparable metric with exp029 reeval (23.88%). If val success remains low (~9% in-distribution), confirms collapse is real even with late recovery.\", \"parent\": \"hsweep_h2_seed2\", \"metrics\": {\"success\": 0.0373, \"action_is_valid\": 0.994, \"action_is_effective\": 1, \"pass_at_1\": 0.0373, \"num_actions\": 48.53, \"response_length\": 8501, \"dataset\": \"AlfworldSG_OOD_134tasks\", \"date\": \"2026-05-18\", \"note\": \"Valid actions (99.4%) but cannot complete tasks - generates long ineffective sequences\"}, \"conclusion\": \"success\"}, \"exp029_episode_level\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:49:53.280Z\", \"updated_at\": \"2026-05-18T04:11:39.305Z\", \"hypothesis\": \"Episode-level 训练（context_window_mode: full）解决 step_independent h=2 的信用分配缺陷，模型能学到跨步规划策略，val success 不再停滞于 baseline。\", \"parent\": \"exp028c_selfguide_recipe\", \"notes\": \"Director 决策 early-stop at step 15（val success 28.125%, pass@8=92.9%）释放 GPU 给 h-sweep。MVP 已通过（step 5 val=25%, 2x baseline）。Episode-level 训练假设确认：从 12.5% baseline 提升到 28.125%，而 step-independent 崩塌到 0%。Checkpoint: global_step_15。\", \"conclusion\": \"success\", \"metrics\": {\"reeval_ood_134tasks\": {\"success\": 0.2388, \"action_is_valid\": 0.5683, \"action_is_effective\": 0.916, \"manager_invalid_action\": 0.0839, \"reward_mean\": 2.388, \"best_at_8\": 8.88, \"dataset\": \"AlfworldSG_OOD_134tasks\", \"date\": \"2026-05-18\"}}}, \"gsweep_g050_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:51.277Z\", \"updated_at\": \"2026-05-18T02:56:21.234Z\", \"hypothesis\": \"γ=0.5 with h=5 will show accelerated collapse compared to default γ=0.95, because γ^k decay compounds: early windows receive only γ^(N-1) ≈ 0.5^9 ≈ 0.2% of terminal return, making sign misattribution maximally severe.\", \"parent\": \"hsweep_h2_seed1\", \"notes\": \"Director 批准 early kill (step 12/15)。Hypothesis 完全确认：γ=0.5 加速 collapse，从 step 1 起 train success 基本为 0%，val step 5/10 全零，KL step 8 spike 到 0.209。step 10 checkpoint 已保存。数据足够用于论文 gamma sweep figure。Watchdog 预期自动启动 g080。\", \"metrics\": {\"current_step\": \"12/15\", \"train_success_collapsed_at\": \"step 1\", \"train_success_all_steps\": \"0-2.3% (effectively 0%)\", \"val_step0\": {\"success\": 0.094}, \"val_step5\": {\"success\": 0, \"reward\": 0}, \"val_step10\": {\"success\": 0, \"reward\": 0, \"response_length\": 1412}, \"kl_sequence\": [0.019, 0.025, 0.018, 0.014, 0.01, 0.009, 0.009, 0.209, 0.018], \"kl_spike_step8\": 0.209, \"checkpoint\": \"global_step_10\", \"eta\": \"~5h from 02:46 UTC\", \"status_note\": \"COMPLETELY COLLAPSED. Train success 0% from step 1. KL spike 20x at step 8. Val all zeros. Remaining 3 steps waste GPU. Recommend early kill.\"}, \"conclusion\": \"killed\"}, \"hsweep_h2_seed2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:37:14.817Z\", \"updated_at\": \"2026-05-18T02:55:38.705Z\", \"hypothesis\": \"h=2 seed 2 replicates seed 1 catastrophic collapse (step 3-4 onset, 0% by step 9+), confirming collapse is robust not single-run artifact. Additionally LOG_PER_SAMPLE_ADV=1 collects per-window advantage data for plan_004 sign misattribution empirical verification.\", \"parent\": \"hsweep_h2_seed1\", \"metrics\": {\"current_step\": \"15/15\", \"completed\": true, \"val_step5\": {\"success\": 0}, \"val_step10\": {\"success\": 0}, \"val_step15\": {\"success\": 0.09375}, \"train_step14\": {\"success\": 0.2656, \"pass_at_8\": 0.6875}, \"train_step15\": {\"success\": 0.2812, \"pass_at_8\": 0.625, \"entropy\": 0.401, \"ppo_kl\": 0.006}, \"train_success_peak\": {\"step\": 15, \"value\": 0.2812}, \"adv_log_lines\": 3000, \"adv_episodes\": {\"total\": 128, \"success\": 65, \"fail\": 63}, \"adv_analysis\": {\"sign_outcome_agreement\": 0.5207, \"point_biserial_r\": 0.068, \"p_adv_pos_given_success\": 0.3706, \"p_adv_pos_given_failure\": 0.306, \"magnitude_decay_gamma\": 0.9426, \"distribution_overlap\": 0.878, \"verdict\": \"52% agreement confirms advantage signal nearly uninformative about episode outcome = sign misattribution\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15/\", \"checkpoint_warning\": \"seed2 overwrote seed1 step15 checkpoint in same directory\", \"status_note\": \"COMPLETED 15/15. Late recovery at step 14-15 (train 26-28%). Val 9.375% on 16 in-dist tasks. ADV: 52% sign agreement = near-random.\"}, \"conclusion\": \"success\", \"notes\": \"15/15 步正常完成 + final val。Hypothesis NOT confirmed：seed2 未复现 seed1 的 catastrophic collapse。关键差异：(1) action_is_valid 始终 88-100%（seed1 崩至 0.06%）(2) val step 15 恢复到 9.375%（seed1 终值 0%）(3) train step 15 success=28.1%（seed1 终值 0%）。Val step 0/5/10 确实为 0%，说明 h=2 确实造成学习困难，但不是 seed1 那样的不可逆 catastrophic collapse。Collapse 行为是 seed-dependent 的，不是 robust finding。ADV log 3000 行可用于 sign misattribution 分析。注意：checkpoint 写入 hsweep-h2/ 目录（与 seed1 共享，global_step_15 被覆盖）。\"}, \"gae_baseline_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:05:31.533Z\", \"updated_at\": \"2026-05-17T19:19:48.391Z\", \"hypothesis\": \"REINFORCE++ (running-mean baseline, no critic) provides modest improvement over episode-level GRPO due to per-token advantage normalization. Fallback from GAE due to TRL 1.1.0 removing AutoModelForCausalLMWithValueHead (critic head unavailable).\", \"parent\": \"exp029_episode_level\", \"metrics\": {\"wandb_run_id\": \"dt79qyd9\", \"pid\": 40267, \"val_step0\": {\"success\": 0.0625, \"action_is_valid\": 0.7796}, \"val_step5\": {\"success\": 0.125, \"action_is_valid\": 0.6926}, \"val_step10\": {\"success\": 0.125, \"pass_at_1\": 0.125, \"reward_mean\": 1.25}, \"train_step9\": {\"success\": 0.0313, \"action_is_valid\": 0.6033, \"pass_at_8\": 0.25}, \"server\": \"westd-47453\", \"gpu\": \"cuda:0,1\", \"method\": \"reinforce_plus_plus\", \"fallback_reason\": \"TRL 1.1.0 removed AutoModelForCausalLMWithValueHead\", \"current_step\": \"11/15\"}, \"notes\": \"实际运行 REINFORCE++ (adv_estimator=reinforce_plus_plus_baseline)，非 GAE。GAE 因 TRL 1.1.0 移除 AutoModelForCausalLMWithValueHead 不可用 (D060)。\", \"conclusion\": \"killed\"}, \"hsweep_h2_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:37:11.061Z\", \"updated_at\": \"2026-05-17T14:36:40.246Z\", \"hypothesis\": \"Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality\", \"parent\": \"exp029_episode_level\", \"metrics\": {\"train_step\": 15, \"total_steps\": 15, \"wandb_run_id\": \"7o9bjszm\", \"step1\": {\"success\": 0.1875, \"pass_at_8\": 0.4375, \"invalid_action\": 0.027}, \"step2\": {\"success\": 0.1484, \"pass_at_8\": 0.5, \"invalid_action\": 0.02}, \"step3\": {\"success\": 0.1875, \"pass_at_8\": 0.625, \"invalid_action\": 0.028}, \"step4\": {\"success\": 0.0547, \"pass_at_8\": 0.25, \"invalid_action\": 0.264}, \"step5\": {\"success\": 0.0156, \"pass_at_8\": 0.0625, \"invalid_action\": 0.369}, \"step6\": {\"success\": 0.0313, \"pass_at_8\": 0.25, \"invalid_action\": 0.471}, \"step7\": {\"success\": 0.0469, \"pass_at_8\": 0.1875, \"invalid_action\": 0.502}, \"step8\": {\"success\": 0.0156, \"pass_at_8\": 0.125, \"invalid_action\": 0.542}, \"step9\": {\"success\": 0, \"pass_at_8\": 0, \"invalid_action\": 0.641}, \"step10\": {\"success\": 0.0234}, \"step11_15\": {\"success\": 0, \"invalid_action\": 0.972}, \"val_final\": {\"success\": 0, \"invalid_action\": 0.999, \"action_is_valid\": 0.0006}, \"checkpoint\": \"global_step_5,10,15\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/\", \"log_path\": \"~/runs/cost-verify-agent-rl/hsweep_h2_s1.log\", \"gpu_util\": \"95-100%\", \"collapse_onset\": \"step3→step4\", \"elapsed_hours\": 10.04, \"step15_entropy\": 0.342, \"step15_kl_loss\": 0.777, \"step15_grad_norm\": 1.611, \"auto_next_triggered\": true, \"seed2_pid\": 945877, \"seed2_wandb\": \"jhwyg4tc\"}, \"conclusion\": \"success\", \"notes\": \"15 steps 完成。Hypothesis 验证：h=2 step_independent 确实灾难性崩溃（step 3→4 onset, step 9 归零, step 11-15 持续为零）。Final val: success=0%, invalid_action=99.9%, action_is_valid=0.06%。模型彻底退化到几乎只输出无效动作。\"}, \"exp025c\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T08:09:29.393Z\", \"updated_at\": \"2026-05-17T10:53:00.425Z\", \"notes\": \"项目已 pivot 到 h-sweep + sign misattribution 诊断方向（D054/D057）。exp025c 属于 pivot 前的实验设计，不在当前 experiment_plan.yaml 中，与论文核心 claims 无关联。GPU 资源优先用于 h-sweep 和 GAE baseline。\", \"conclusion\": \"killed\"}, \"exp026_step_independent_grpo\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:34:33.675Z\", \"updated_at\": \"2026-05-17T03:14:31.315Z\", \"notes\": \"exp026 negative: step-independent GRPO 在 step 2 达峰 train success=32.81% 后连续崩塌至 step 4 的 0%。Step 5 val eval 未完成即被 kill（val 生成阶段启动后进程被终止），无法对比 step 0 vs step 5 val。无 checkpoint（save_freq=25 未触发）。根因分析（Reviewer）：sparse reward + 小 env_groups(4=64 rollouts) 导致全零 batch 概率高，advantage 只有负信号把策略推回 reference。action_is_valid 在 step 2-4 保持 ~72% 但 success 归零，模型学会了\\\"看起来合理\\\"的 action 但丧失任务完成能力。教训：(1) save_freq 必须 ≤5 捕获早期峰值 (2) env_groups 需 ≥8 降低全零 batch 概率 (3) WANDB_MODE=disabled 导致 cron 误判 (4) cron 应监控 Ray TaskRunner PID 而非 shell wrapper PID。\", \"metrics\": {\"val_before_train_success\": 0.0625, \"val_before_train_action_is_valid\": 0.631, \"val_before_train_episodes\": 16, \"train_step1_success\": 0.2188, \"train_step1_action_is_valid\": 0.686, \"train_step1_entropy\": 0.2672, \"train_step1_kl_loss\": 0.1797, \"train_step1_grad_norm\": 14.43, \"train_step1_reward_mean\": 1.218, \"train_step1_pass_at_16\": 1, \"train_step2_success\": 0.3281, \"train_step2_action_is_valid\": 0.603, \"train_step2_entropy\": 0.317, \"train_step2_kl_loss\": 0.0974, \"train_step2_grad_norm\": 15.62, \"train_step2_reward_mean\": 1.62, \"train_step2_pass_at_16\": 1, \"train_step3_success\": 0.1719, \"train_step3_action_is_valid\": 0.641, \"train_step3_entropy\": 0.387, \"train_step3_kl_loss\": 0.2617, \"train_step3_grad_norm\": 15.65, \"train_step3_reward_mean\": 1.079, \"train_step3_pass_at_16\": 0.75, \"train_step4_success\": 0, \"train_step4_action_is_valid\": 0.717, \"train_step4_entropy\": 0.387, \"train_step4_kl_loss\": 0.054, \"train_step4_grad_norm\": 13.81, \"train_step4_pass_at_16\": 0}, \"conclusion\": \"negative\", \"hypothesis\": \"Step-independent GRPO（每步独立优化、不建模跨步依赖）能在ALFWorld多步任务中学到有效策略，因为每步的local reward信号足以引导正确行为选择\", \"parent\": \"exp021_ragen_sft_v4\"}, \"exp019b_expert_sft_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:30:00.085Z\", \"updated_at\": \"2026-05-17T03:14:30.703Z\", \"hypothesis\": \"Two-stage Expert SFT: exp008_sft checkpoint + v3 data (original move actions + admissible actions). LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096. Pass: success>=10%, format_ok>=90%, action_is_valid>=85%.\", \"notes\": \"训练成功完成 320/320 steps (2 epochs, 47:49)。Cron 多次误报 failed（监控错误 PID / 无法区分正常退出与崩溃）。Checkpoint: /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.0718, \"eval_loss\": 0.0428, \"eval_mean_token_accuracy\": 0.9869, \"train_runtime_seconds\": 2869.8, \"steps\": 320, \"epochs\": 2, \"eval_success_rate\": 0.2, \"eval_format_ok\": 1, \"eval_action_is_valid\": 0.8533, \"eval_episodes\": 20, \"eval_avg_steps\": 25.4, \"eval_time_seconds\": 146}, \"parent\": \"exp008_sft\"}, \"exp013f\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:21:46.227Z\", \"updated_at\": \"2026-05-17T03:14:29.725Z\", \"hypothesis\": \"Dense reward shaping(valid_action_bonus=0.15)为全失败GRPO group提供非零方差梯度信号，使模型在避免梯度collapse的同时学到task success而非仅优化bonus\", \"parent\": \"exp013e\", \"metrics\": {\"step\": 30, \"total_steps\": 30, \"completed\": true, \"exit_code\": 0, \"training_time_s\": 10683, \"step6_success\": 0.0156, \"step7_success\": 0.0781, \"step10_success\": 0, \"step17_success\": 0.0156, \"final_val_success\": 0, \"final_val_action_is_valid\": 0.975, \"final_val_action_is_effective\": 1, \"final_val_reward_mean_at4\": 4.388, \"final_val_reward_std_at4\": 0.195, \"final_val_reward_best_at4\": 4.499, \"final_val_pass_at1\": 0, \"action_is_valid_trend\": \"60%→65.9%→77.1%→97.5%\", \"success_trend\": \"0%→1.56%→7.81%→0%→1.56%→0%\", \"grad_norm_range\": \"1.7-2.9 (no collapse)\", \"conclusion_reason\": \"Dense reward gaming: model optimized valid_action_bonus (action_is_valid 60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse prevented but task completion not learned.\"}, \"conclusion\": \"negative\", \"notes\": \"30/30 步完成，EXIT_CODE=0。Dense reward shaping 成功解决了 exp012b 的 catastrophic collapse（grad_norm 稳定 1.7-2.9），但产生 reward gaming：模型最大化 valid_action_bonus 而非 success_reward。action_is_valid 60%→97.5%（学会合法命令），success 始终 0-8%（未学会完成任务）。final_val reward/mean@4=4.388 ≈ 29 valid_actions × 0.15，几乎无 success_reward 贡献。Disk warning: /root/autodl-tmp 95% full (4.1GB remaining)。Ray log 备份失败（脚本执行时 session 已清理）。Checkpoint: global_step_30 已保存。\"}, \"exp028_prereq_zeroshot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:11:06.120Z\", \"updated_at\": \"2026-05-17T03:14:28.598Z\", \"conclusion\": \"negative\", \"wandb_run_id\": \"qdvv09da\", \"metrics\": {\"success\": 0, \"action_is_valid\": 0.75, \"num_actions\": 50, \"pass_at_1\": 0, \"response_length\": 75.07}, \"notes\": \"Qwen3-1.7B（本身就是 instruct 模型）零样本 ALFWorld eval = 0% success。证明 SFT 从 0%→6.25% 是有益的，D044 '不做SFT' 假设不成立。W&B run: qdvv09da\", \"hypothesis\": \"Qwen3-1.7B base模型具备ALFWorld零样本能力(success>0%)，无需SFT即可作为GRPO冷启动点——如成立则SFT引入的分布偏差可能反而有害\"}, \"exp008_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:04:47.496Z\", \"updated_at\": \"2026-05-17T03:14:25.946Z\", \"notes\": \"SFT 转换脚本修复后重跑成功。Eval 方法: 独立脚本 eval_sft_model.py, 4 episodes (seed=0,1,2,3), HF generate() + AlfredTXTEnv, cuda:1, max_steps=50。action_is_valid=90% (180/200 actions), format_ok=100%, success_rate=0%。完整 50-episode eval 未完成（为 GRPO 让出 GPU）。\", \"conclusion\": \"success\", \"metrics\": {\"action_is_valid\": 0.9, \"format_ok\": 1, \"success_rate\": 0, \"final_loss\": 0.069, \"final_token_accuracy\": 0.973, \"data_count\": 1200, \"epochs\": 3, \"total_steps\": 225, \"training_time_s\": 576}, \"hypothesis\": \"基础格式SFT使Qwen3-1.7B学会ALFWorld动作格式和有效动作选择(format_ok+action_is_valid)，建立可训练基线，为后续expert SFT和GRPO提供非随机起点\"}, \"exp028c_selfguide_recipe\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:38:48.089Z\", \"updated_at\": \"2026-05-16T08:29:53.723Z\", \"wandb_run_id\": \"4yu6qz1m\", \"notes\": \"D052 终止。step_independent h=2 导致灾难性过拟合：step_5_val best@128=10.0 → step_10_val best@800=0.0。train success 波动上升(peak 21.88%)=局部动作过拟合，但无法泛化到新 game。根因：(1) step_independent 破坏长程信用分配 (2) self-guidance reward 缺失 (3) val 仅 16 episodes。参见 selfguide_setup_audit.md。\", \"metrics\": {\"step_0_val\": {\"success\": 6.25, \"pass_at_1\": 6.25, \"action_is_valid\": 74.5, \"score_mean\": 0.119}, \"step_1_train\": {\"success\": 13.28, \"pass_at_8\": 37.5, \"action_is_valid\": 76.4, \"action_is_effective\": 96.37, \"entropy\": 0.2634, \"kl_loss\": 0.0128, \"ppo_kl\": 0.019, \"grad_norm\": 16.88, \"score_mean\": 0.843, \"time_s\": 3252, \"note\": \"三方交叉验证通过\"}, \"step_2_train\": {\"success\": 6.25, \"pass_at_8\": 25, \"action_is_valid\": 83.2, \"entropy\": 0.247, \"kl_loss\": 0.1706, \"pg_loss\": 0.007, \"grad_norm\": 17.3, \"score_mean\": 0.274, \"time_s\": 3120}, \"step_3_train\": {\"success\": 15.63, \"pass_at_8\": 68.75, \"action_is_valid\": 85.9, \"entropy\": 0.2488, \"kl_loss\": 0.1118, \"grad_norm\": 12.57, \"score_mean\": 0.661, \"time_s\": 2760}, \"step_4_train\": {\"success\": 18.75, \"pass_at_8\": 62.5, \"action_is_valid\": 87.94, \"entropy\": 0.234, \"kl_loss\": 0.031, \"ppo_kl\": 0.015}, \"step_5_train\": {\"success\": 9.4, \"pass_at_8\": 37.5, \"action_is_valid\": 89.6, \"entropy\": 0.236, \"kl_loss\": 0.824, \"grad_norm\": 13.1}, \"step_5_val\": {\"success\": 6.25, \"pass_at_1\": 6.25, \"action_is_valid\": 96.5, \"action_is_effective\": 100, \"num_actions\": 49.4, \"score_mean\": 0.518}, \"step_6_train\": {\"success\": 10.94, \"action_is_valid\": 90.4, \"entropy\": 0.234, \"kl_loss\": 0.098, \"grad_norm\": 12.54}, \"step_7_train\": {\"success\": 21.88, \"pass_at_8\": 56.25, \"action_is_valid\": 91.8, \"entropy\": 0.224, \"kl_loss\": 0.046}, \"step_8_train\": {\"success\": 15.6, \"pass_at_8\": 50, \"action_is_valid\": 92.7, \"kl_loss\": 0.039, \"entropy\": 0.204}, \"step_9_train\": {\"success\": 18, \"pass_at_8\": 56.3, \"action_is_valid\": 93.6, \"kl_loss\": 0.047, \"entropy\": 0.204}, \"step_10_train\": {\"success\": 18.75, \"action_is_valid\": 90.7, \"kl_loss\": 0.197}, \"step_10_val\": {\"success\": 0, \"pass_at_1\": 0, \"best_at_128\": 0, \"best_at_800\": 0, \"action_is_valid\": 93.6, \"num_actions\": 49.8, \"reward_mean\": 0, \"note\": \"灾难性崩溃，模型完全遗忘\"}}, \"conclusion\": \"failed\"}, \"exp028a_recipe_fix\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:08:53.131Z\", \"updated_at\": \"2026-05-15T21:25:46.006Z\", \"hypothesis\": \"invalid_action_penalty (-0.1) 为全失败 GRPO group 提供非零方差梯度信号。从 exp021 SFT checkpoint (6.25% success) 出发，仅增加 invalid_action_penalty_coef=0.1，其余参数与 exp027 完全一致。预期：penalty 让失败 trajectory 间有区分（invalid action 多=reward更低），解决 ~43% group 零梯度问题。Pass: success ≥20%（稳定，非瞬时 peak）。\", \"parent\": \"exp027_stable_grpo\", \"wandb_run_id\": \"lu42su82\", \"conclusion\": \"killed\", \"notes\": \"与 exp027 功能等价（penalty getattr 默认值=0.1 在 exp027 中已生效）。Director 指令停止。\"}, \"exp028_prereq_zeroshot_instruct\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T20:59:57.529Z\", \"updated_at\": \"2026-05-15T21:06:09.982Z\", \"hypothesis\": \"Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\\\"SFT是毒药\\\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。\", \"parent\": \"exp027_stable_grpo\", \"notes\": \"Qwen3-1.7B 确认就是 instruct 模型（无独立 Instruct 变体）。零样本 eval 0% success / 0.75% valid（与之前结果一致）。关键结论：\\\"SFT是毒药\\\"假设(D044)不成立——SFT 实际提升了 0%→6.25%。62pp gap 根因排除 SFT，聚焦于 binary reward 零梯度 + mini-batch 过小 + 训练步数不足。\"}, \"exp027_stable_grpo\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:04:13.123Z\", \"updated_at\": \"2026-05-15T20:44:26.582Z\", \"notes\": \"进程退出原因：Ray raylet 被异常终止（ActorUnavailableError: RPC error: Socket closed rpc_code: 14）。Raylet termination unexpected — 可能 SIGKILL by OOM killer 或内存访问错误。退出发生在 step 4 完成后、step 5 开始前。EXIT_CODE=1。D045 已判定 MVP 未通过（train success 13.28% < 20% 阈值）。Recipe Gap 诊断三大根因：(1) SFT 起点反效果 (2) Binary reward 零梯度 (3) Mini-batch 8× 过小。exp028 配置准备中（5 个 Worker 活跃）。\", \"hypothesis\": \"Stabilized step-independent GRPO: 针对 exp026 死亡螺旋根因（sparse reward + 小 env_groups 导致全零 batch），增加 rollouts（env_groups 4→8, 128 trajectories）、降低 LR（1e-6→5e-7）、降低 KL（0.01→0.005）、新增 entropy bonus（0.01）、save_freq 5 捕获峰值。50 步快速验证。Pass: success ≥20% 且无连续 2 步归零。\", \"parent\": \"exp026_step_independent_grpo\", \"wandb_run_id\": \"y7jiibqk\", \"metrics\": {\"step_0_val_before_train\": {\"success\": 6.25, \"action_is_valid\": 63.125, \"action_is_effective\": 87.875, \"num_actions\": 42.375, \"response_length\": 114.67, \"reward_mean\": 0.3226, \"val_generation_time_s\": 502.57}, \"step_1_train\": {\"success\": 35.94, \"kl_loss\": 0.058, \"batch_size\": 5152, \"training_time_s\": 4342}, \"step_2_train\": {\"success\": 10.16, \"kl_loss\": 0.413, \"batch_size\": 6144, \"training_time_s\": 5886}, \"step_3_train\": {\"success\": 10.16, \"kl_loss\": 0.248, \"entropy\": 0.385, \"pass_at_16\": 0.5, \"grad_norm\": 21.31, \"reward_mean\": 0.483, \"batch_size\": 6048, \"training_time_s\": 4689}, \"step_4_train\": {\"success\": 13.28, \"pass_at_16\": 0.375, \"note\": \"Director判定: 趋势确认, MVP未通过\"}}, \"conclusion\": \"failed\"}, \"exp025b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:34:34.283Z\", \"updated_at\": \"2026-05-15T07:44:26.903Z\", \"parent\": \"exp025\", \"notes\": \"三次提交均失败。第三次：pre-flight 清理后 Ray 主进程启动成功、数据加载成功（8810 train / 494 val），但 AlfworldWorker 进程初始化时线程创建失败（Resource temporarily unavailable, EAGAIN）。36+ 次 system:11 错误，43+ 次 Fatal Python error: Aborted。jemalloc arena background thread creation failed。根因：系统 nproc/线程上限不足，8 个 AlfworldWorker + Ray 内部线程总数超限。需排查 ulimit -u 和 /proc/sys/kernel/threads-max。\", \"conclusion\": \"failed\"}, \"exp025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:52:48.190Z\", \"updated_at\": \"2026-05-15T07:34:25.374Z\", \"notes\": \"崩溃原因：(1) conda activate base 错误，应用 /root/autodl-tmp/conda-envs/verl-agent 环境 (2) save_freq=-1 未修改为 25。ModuleNotFoundError — base 环境缺 verl-agent 依赖。教训：提交前必须验证 which python 指向正确环境 + 关键参数在 config 中与预期一致。\", \"conclusion\": \"failed\"}, \"exp021_ragen_sft_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:09:31.719Z\", \"updated_at\": \"2026-05-15T06:24:16.570Z\", \"hypothesis\": \"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer&gt; tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"negative\", \"metrics\": {\"train_loss_final\": 0.038, \"train_token_accuracy\": 0.988, \"train_steps\": 320, \"train_epochs\": 2, \"train_time_min\": 47.8, \"ragen_val_success\": 0.25, \"ragen_val_action_is_valid\": 0.875, \"eval_sft_fast_success\": 0, \"eval_sft_fast_format_ok\": 1, \"eval_sft_fast_action_is_valid\": 0.71, \"checkpoint_size_gb\": 3.3, \"ragen_val_success_16ep\": 0.0625, \"ragen_val_action_is_valid_16ep\": 0.6875}, \"notes\": \"D024: conclusion 降级为 negative (原 success)。16ep eval 数据: success=6.25%, action_is_valid=68.75%。原 4ep eval 的 25%/87.5% 为 unreliable_small_sample，不作为决策依据。Registry 无 inconclusive 选项，用 negative 代替。\"}, \"exp024_success_gated_grpo\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:03:10.298Z\", \"updated_at\": \"2026-05-15T06:04:06.454Z\", \"hypothesis\": \"Success-gated GRPO from exp021 checkpoint. D026 终止 RAGEN GRPO 后不再适用，success-gated 不解决 context 爆炸根因。关联 D027。\", \"conclusion\": \"killed\", \"notes\": \"D027: Kill exp024 — D026 终止 RAGEN GRPO 后 success-gated 变体不再适用，不解决 context 爆炸根因。关联 D025/D026/D027。\"}, \"exp023c_grpo_serial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T04:20:22.909Z\", \"updated_at\": \"2026-05-15T05:11:22.083Z\", \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint. Serial mode (parallel_friendly=false, max_workers=1) to avoid tatsu race. reward scale=10.0, kl_loss_coef=0.5, LR=5e-7, val env_groups=16, gpu_memory_utilization=0.6, 30 steps. Pass: success ≥ 25%, step time baseline comparison with exp022 (~208s/step).\", \"parent\": \"exp023_grpo_parallel\", \"metrics\": {\"val_step0_success\": 0.0625, \"val_step0_action_is_valid\": 0.6875, \"val_step0_episodes\": 16, \"train_step1_success\": 0.297, \"train_step1_action_is_valid\": 0.791, \"train_step1_entropy\": 0.0652, \"train_step1_pass16\": 0.75, \"train_step1_kl\": 0.000156, \"train_step8_success\": 0.234, \"train_step8_action_is_valid\": 0.779, \"train_step8_entropy\": 0.0555, \"train_step8_pass16\": 0.5, \"train_step8_kl\": 0.000475, \"steps_completed\": 8, \"steps_planned\": 30, \"step_time_seconds_start\": 240, \"step_time_seconds_end\": 365}, \"notes\": \"磁盘满崩溃 (step 9, /root/autodl-tmp 94% 233G/250G, OSError Errno 28)。但 8 步 metrics 趋势已显示退化：train success 29.7%→23.4%↓, pass@16 75%→50%↓, entropy 0.065→0.056↓, KL 0.00016→0.00048↑, step time 240s→365s↓。GRPO 未能在 SFT baseline 上产生改善，反而在退化。注意 step 0 val success=6.25% 与 train step 1 success=29.7% 差异大（val 用不同 game set + 16 episodes vs train 64 trajectories）。Checkpoint: global_step_5 only (save_freq=5, 第二次保存在 step 10 未到)。\", \"conclusion\": \"failed\"}, \"exp023_grpo_parallel\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T04:06:02.056Z\", \"updated_at\": \"2026-05-15T04:12:41.878Z\", \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint with 3 key fixes: (1) reward scale 10.0→1.0 (align with Self-Guide paper binary reward), (2) parallel rollout (max_workers=4, thread-safe env), (3) val env_groups=16 for reliable eval. kl_loss_coef=0.5, LR=5e-7, 30 steps. Pass: success ≥ 25% (maintain SFT baseline), step time < 200s (vs exp022 ~208s serial).\", \"parent\": \"exp022_grpo_from_sft_v4\", \"conclusion\": \"failed\", \"notes\": \"失败原因: textworld PDDL parser (tatsu) 在 val env reset 时崩溃 — tatsu.exceptions.FailedToken: expecting 'action', got template :: \\\"take {o} from {r}\\\". val env_groups=16 加载了更多 game files，触发了某个 game file 与当前 tatsu 版本不兼容的 PDDL grammar. | 已有成果: 无（val_before_train 阶段即崩溃，未开始训练） | 建议: 诊断具体哪个 game file 有问题，降低 val env_groups 或修复 game file/tatsu 兼容性\"}, \"exp022_grpo_from_sft_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:17:34.035Z\", \"updated_at\": \"2026-05-15T03:52:55.267Z\", \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint (25% RAGEN val success baseline). Sparse reward (won=10.0), LR=5e-7, kl_loss_coef=0.5 (5x stronger than exp020b to prevent entropy collapse), max_grad_norm=1.0, 30 steps, val env_groups=8. Pass: success ≥ 25% (maintain SFT baseline).\", \"parent\": \"exp021_ragen_sft_v4\", \"notes\": \"Step 0 val: success=12.5% (1/8), action_is_valid=48.75%。Step 1 完成后 kill。action_is_valid 远低于 SFT eval 结果（87.5%/68.75%），说明 RAGEN GRPO 框架中模型表现显著退化。kl_loss_coef=0.5, env_groups=8 均已确认生效。训练速度 ~208s/step。Checkpoint: global_step_1 可能已保存。\", \"conclusion\": \"killed\", \"metrics\": {\"steps_completed\": 1, \"steps_planned\": 30, \"val_step0_success\": 0.125, \"val_step0_action_is_valid\": 0.4875, \"val_step0_action_is_effective\": 1, \"val_step0_reward_mean\": 1.25, \"val_step0_reward_best\": 6.61, \"val_step0_episodes\": 8, \"step_time_seconds\": 208}}, \"exp021_sft_ragen_format\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T22:35:48.559Z\", \"updated_at\": \"2026-05-15T02:11:46.204Z\", \"hypothesis\": \"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\", \"parent\": \"exp019b_expert_sft_v3\", \"notes\": \"被 exp021_ragen_sft_v4 取代。\", \"conclusion\": \"killed\"}, \"exp020d_grpo_from_sft\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T22:19:30.993Z\", \"updated_at\": \"2026-05-15T02:01:10.192Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"failed\", \"notes\": \"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\"}, \"exp020c_grpo_from_sft\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T22:15:37.659Z\", \"updated_at\": \"2026-05-15T02:01:08.768Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"failed\", \"notes\": \"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\"}, \"exp020b_grpo_from_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:12:38.928Z\", \"updated_at\": \"2026-05-15T02:00:56.016Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink with \\\"qwen\\\" in path to pass response_mask assertion (exp020 crashed on this).\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"negative\", \"metrics\": {\"steps_completed\": 22, \"steps_planned\": 30, \"hung_at_step\": 23, \"step1_train_success\": 0.1875, \"step10_train_success\": 0.1875, \"step20_train_success\": 0.125, \"step22_train_success\": 0.0469, \"val_success_step0\": 0, \"val_success_step20\": 0, \"entropy_initial\": 0.107, \"entropy_final\": 0.042, \"grad_norm_initial\": 2.78, \"grad_norm_step20\": 5.58, \"ppo_kl_final\": 0.00918, \"pass_at_16_step1\": 0.75, \"pass_at_16_step22\": 0.25, \"checkpoint_latest\": \"global_step_20\", \"training_status\": \"hung_at_step23_rollout\"}, \"notes\": \"Negative 结论：GRPO from SFT 导致策略坍缩。训练 22/30 步后卡死在 step 23 rollout（环境交互死锁，GPU 0% 利用率但显存仍占 40GB×2）。关键指标全线恶化：train success 18.75%→4.69%（远低于 SFT baseline 20%），val success 始终 0%，entropy 0.107→0.042（坍缩 61%），pass@16 从 75%降到 25%。GRPO 不仅未提升 SFT 性能，反而严重退化。根因分析：sparse reward（won=10.0）学习信号不足以维持 SFT 学到的 task knowledge，KL coef=0.1 不足以约束策略偏移。Checkpoint: /root/autodl-tmp/checkpoints/exp020b/global_step_20/\"}, \"exp020_grpo_from_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:07:16.290Z\", \"updated_at\": \"2026-05-14T22:11:05.341Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline) can maintain or improve success rate. Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%.\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"failed\", \"notes\": \"失败原因: AssertionError at train.py:137 — model_path=/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final 不含 \\\"qwen\\\" 字符串，enable_response_mask=true 断言失败。模型实际是 Qwen3-1.7B 微调 checkpoint，路径命名问题。error_type=infrastructure | 建议: 创建含 \\\"qwen\\\" 的 symlink 或添加 enable_response_mask=false override 后重提交\"}, \"exp019c_expert_sft_v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T21:03:02.685Z\", \"updated_at\": \"2026-05-14T21:05:37.494Z\", \"hypothesis\": \"Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。\", \"parent\": \"exp019b_expert_sft_v3\", \"notes\": \"废弃。submit_training_job 因 GPU 被占（exp019b nohup 进程仍在跑）EXIT_CODE=1 退出。实际训练由 exp019b 的 nohup 进程完成。\", \"conclusion\": \"killed\"}, \"exp019_expert_sft_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T16:38:05.515Z\", \"updated_at\": \"2026-05-14T17:11:09.024Z\", \"conclusion\": \"killed\", \"notes\": \"D019 kill：move→put 替换方向错误。ALFWorld admissible_commands 包含 move X to Y，不含 put。用 put 替换的数据会使 action_is_valid 更差。改用原始 expert data（保留 move）+ admissible actions augmentation。\"}, \"exp019b_expert_sft_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T16:49:30.246Z\", \"updated_at\": \"2026-05-14T16:49:30.246Z\"}, \"exp018_sft_grpo\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T15:43:08.545Z\", \"updated_at\": \"2026-05-14T16:45:33.314Z\", \"hypothesis\": \"Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），使 GRPO 有足够非零 reward group 产生有效梯度。LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, won=10.0, 无 bonus/penalty, GRPO 30 步。Pass: success ≥ 20%。\", \"parent\": \"exp017_expert_sft\", \"conclusion\": \"killed\", \"notes\": \"D018 取消：exp017 eval 5% success 与 base 4.7% 差异太小，GRPO 大概率重蹈覆辙。等 exp019 v2 SFT（修复 move→put + admissible actions 数据增强）后再考虑 GRPO。\"}, \"exp017_expert_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:36:28.291Z\", \"updated_at\": \"2026-05-14T16:36:17.637Z\", \"hypothesis\": \"Expert SFT: 用 PDDL expert trajectory 数据 SFT Qwen3-1.7B instruct 模型，提升 ALFWorld baseline success rate，为后续 GRPO 提供更好的冷启动点。LR=2e-5, 3 epochs, batch_size=4, grad_accum=4。Pass 标准: success ≥ 10%。\", \"parent\": \"exp008_sft\", \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.1434, \"final_step_loss\": 0.04, \"final_token_accuracy\": 0.983, \"epochs\": 3, \"total_steps\": 462, \"training_time_min\": 26, \"data_count_train\": 2460, \"data_count_val\": 129, \"checkpoint_size_gb\": 3.44, \"eval_success_rate\": 0.05, \"eval_success\": \"1/20\", \"eval_action_is_valid\": 0.638, \"eval_format_ok\": 0.75, \"eval_avg_steps\": 22, \"eval_time_s\": 149.6, \"eval_per_task\": {\"put\": \"0/10\", \"clean\": \"0/4\", \"cool\": \"1/3\", \"heat\": \"0/2\", \"examine\": \"0/1\"}, \"eval_parse_failures\": \"5/20 episodes (EP 7/12/16/17/18)\"}, \"notes\": \"训练成功完成。Expert PDDL trajectory 2460 条 SFT Qwen3-1.7B，3 epochs 462 steps 26 min。Final loss=0.1434。Checkpoint: /root/autodl-tmp/checkpoints/exp017_expert_sft/final/ (3.44GB)。\\n\\nEval 结果（20 episodes, vLLM 推理, max_steps=30）：success=5% (1/20), action_is_valid=63.8%, format_ok=75%。唯一成功是 1 个 cool 任务（EP 8, 15 步）。5/20 episodes parse 失败（1 步即退出）。put 任务 0/10 全失败。\\n\\n对比 exp008_sft（1200 条普通 SFT）：action_is_valid 90%→63.8%（下降！）, format_ok 100%→75%（下降！）, success 0%→5%（略升）。Expert data SFT 提升了 success 但 format/valid 反而退步，可能因为 expert trajectory 格式与 RAGEN 的 &lt;think>/&lt;answer> 格式不完全匹配。\"}, \"exp016\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:44:58.883Z\", \"updated_at\": \"2026-05-14T15:36:27.432Z\", \"hypothesis\": \"LR 折中方案：LR=5e-7（exp012b 1e-6 collapse vs exp015 1e-7 零梯度的中间值）。kl_loss_coef=0.1, max_grad_norm=1.0 保持。纯 sparse reward（won=10.0，无 bonus，无 format_penalty）。从 exp015/global_step_5 checkpoint 恢复，GRPO 30 步。\", \"parent\": \"exp015\", \"metrics\": {\"step\": 12, \"total_steps\": 30, \"elapsed_min\": 51, \"step6_success\": 0, \"step6_action_is_valid\": 0.521, \"step6_pg_loss\": 0, \"step6_grad_norm\": 0.841, \"step7_success\": 0.047, \"step7_pass_at16\": 0.5, \"step7_action_is_valid\": 0.655, \"step10_success\": 0, \"step10_action_is_valid\": 0.664, \"step10_pg_loss\": 0, \"step10_grad_norm\": 0.856, \"step10_entropy\": 0.1046, \"step10_ppo_kl\": -9.1e-05, \"all_raw_rewards\": 0, \"all_advantages\": 0, \"all_returns\": 0, \"reward_signal\": \"BROKEN — success episodes get reward=0\", \"action_is_valid_trend\": \"52.1%→65.5%→66.4%\", \"manager_invalid_action_trend\": \"13.5%→11.2%→9.6%\"}, \"conclusion\": \"failed\", \"notes\": \"D015 kill。训练 12 步，pg_loss 恒为 0。原因：base success ~4.7%（仅 val，train temperature=1.0 下接近 0%），纯 sparse reward 下 GRPO 无有效学习信号。raw_reward=0 是日志 artifact（info dict 缺 raw_reward 字段），实际训练 reward pipeline 正常（critic/score 正确传递，step 7 score/mean=0.46875=3/64×10.0）。NaiveRewardManager 是 pass-through，不覆盖 env reward。LR=5e-7 本身无问题，根因是 sparse reward 冷启动。\"}, \"exp015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:48:38.065Z\", \"updated_at\": \"2026-05-14T13:44:57.940Z\", \"hypothesis\": \"Sparse GRPO + 训练稳定性修复。纯 sparse reward（won=10.0，无 valid_action_bonus，无 format_penalty）。针对 exp012b 的 step 7 catastrophic collapse（grad_norm 1.48→0.094），三项修复：LR 1e-7（降 10 倍防单步更新过激）、kl_loss_coef 0.1（增 10 倍约束策略偏移）、max_grad_norm=1.0（梯度裁剪）。从 exp008 step 5 checkpoint 恢复，GRPO 30 步。\", \"parent\": \"exp012b\", \"notes\": \"D014 kill。Steps 3-5 连续零梯度（pg_loss=0, grad_norm~0），LR=1e-7 过保守导致无有效学习。Step 0 val: action_is_valid=85.8%, success=0%。训练稳定性修复验证成功（无 catastrophic collapse），但学习率不足以产生有意义的 policy update。Checkpoint: global_step_5 已保存，供 exp016 恢复。\", \"metrics\": {\"step\": 1, \"total_steps\": 30, \"val_step0_success\": 0, \"val_step0_action_is_valid\": 0.858, \"val_step0_pass_at1\": 0, \"val_step0_episodic_return\": 0, \"val_step0_response_length\": 2797.5, \"val_train_transition\": \"passed\", \"estimated_total_time_min\": 163, \"time_per_step_min\": 5.6}, \"conclusion\": \"killed\"}, \"exp014b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T12:45:27.876Z\", \"updated_at\": \"2026-05-14T12:48:37.433Z\", \"hypothesis\": \"极低 Dense Reward: valid_action_bonus=0.01（1:1000 比例），测试极弱 bonus 能否防 collapse 又不引发 gaming。如果 bonus 弱到不影响 GRPO reward ranking，模型不会被诱导走捷径。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\", \"parent\": \"exp013f\", \"conclusion\": \"killed\", \"notes\": \"D013 撤销：Director 修订决策，改为 exp015。exp014b 等 exp015 结果后再决定。\"}, \"exp014a\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T12:45:27.347Z\", \"updated_at\": \"2026-05-14T12:48:35.102Z\", \"hypothesis\": \"Success-Gated Dense Reward: valid_action_bonus=0.15 只在 group 内至少一条 trajectory success 时才给。消除 reward gaming 的独立最大化路径——没有 success 就没有 bonus，模型必须探索 success。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\", \"parent\": \"exp013f\", \"conclusion\": \"killed\", \"notes\": \"D013 撤销：Director 修订决策，success-gated bonus 有 bootstrap 问题（初始 success=0 时 bonus 永远为 0，退化为 sparse reward），改为 exp015 纯 sparse GRPO + 训练稳定性修复。\"}, \"exp014c\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T12:45:21.231Z\", \"updated_at\": \"2026-05-14T12:45:25.025Z\", \"hypothesis\": \"Success-gated valid_action_bonus：bonus 仅在 episode 成功时累加到 reward，消除独立最大化路径。valid_action_bonus=0.15, success_reward=10.0。解决 exp013f reward gaming（unconditional bonus 导致 agent 放弃 success 追求 valid action）。从 step 5 checkpoint 恢复 GRPO 30 步。\", \"parent\": \"exp013f\"}, \"exp013e\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:02:52.837Z\", \"updated_at\": \"2026-05-14T09:21:08.911Z\", \"hypothesis\": \"exp013d 基础设施修复重试。Ray object_store_memory 改用 Hydra config override (ray_kwargs.ray_init.object_store_memory=32212254720) 替代无效的环境变量。其余同 exp013d: dense reward shaping (valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0), env_groups=4, 从 step 5 checkpoint 恢复。\", \"parent\": \"exp013d\", \"conclusion\": \"failed\", \"notes\": \"ActorUnavailableError: RPC error: Socket closed rpc_code: 14。validation step 5 完成后向 training step 6 过渡时崩溃。诊断排除: cgroup OOM (oom_kill=0)、系统 OOM (dmesg 无记录)、CUDA OOM (无日志)、磁盘满 (118GB剩余)。Ray worker 日志被 ray stop --force 清除，最可能原因: vLLM worker 在 val→train 切换时的内存峰值或内部错误。object_store_memory=30GB 设置正确(train.py:203)。validation 指标: success=0, action_is_valid=0.656, reward_mean=2.953, reward_std=1.608。结论: 瞬态崩溃，可安全重提交。建议加 HYDRA_FULL_ERROR=1。\"}, \"exp013d\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:34:37.036Z\", \"updated_at\": \"2026-05-14T08:52:25.371Z\", \"hypothesis\": \"exp013b/c 内存修复重试。Dense reward shaping (valid_action_bonus=0.15) 已验证有效 (reward_std=1.608>0)。修复: env_groups 8→4 (64并发, 峰值~158GB < 220GB cgroup限制) + RAY_object_store_memory=30GB。\", \"parent\": \"exp013c\", \"notes\": \"RAY_object_store_memory env var 未生效，Ray 仍分配 70.36GB object store（默认值）。env_groups=4 生效但不够。Raylet 被 cgroup OOM killer SIGKILL。修复: 用 Hydra config override ray_kwargs.ray_init.object_store_memory=32212254720 显式传给 ray.init()。\", \"conclusion\": \"failed\"}, \"exp013c\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:30:44.623Z\", \"updated_at\": \"2026-05-14T08:34:10.517Z\", \"hypothesis\": \"exp013b 基础设施重试。Dense reward shaping (valid_action_bonus=0.15 + success=10.0) 已验证有效 (reward_std=1.608>0)。exp013b 因 OOM/Ray 崩溃，非算法问题。\", \"parent\": \"exp013b\", \"notes\": \"预防性kill。诊断确认 exp013b 崩溃根因: cgroup 内存限制 220GB, Ray object_store 70GB + memory 164GB = 234GB 超限。128并发ALFWorld游戏(8 env_groups × 16 group_size)在 step 6 rollout 触发 Plasma mmap ENOMEM。exp013c 同配置会重现。修复: env_groups 8→4 + RAY_object_store_memory=30GB。\", \"conclusion\": \"killed\"}, \"exp013b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:15:44.247Z\", \"updated_at\": \"2026-05-14T08:27:21.850Z\", \"hypothesis\": \"Dense reward shaping: valid_action_bonus=0.15 per valid action + success_reward=10.0 + kl_loss_coef=0.01。每步有效动作获得 0.15 奖励提供持续 GRPO 学习信号（30步累计上限4.5 vs 终局10.0），KL 约束防止 policy 过激更新。format_penalty=0，从 step 5 checkpoint 恢复 GRPO 30 步。\", \"parent\": \"exp013\", \"notes\": \"Dense reward shaping 有效性已确认：val reward_mean=2.953, reward_std=1.608 (>0)。崩溃是基础设施问题（OOM/Ray），非算法问题。清理后重试。超参: valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0, format_penalty=0, group_size=16。\", \"conclusion\": \"failed\"}}, \"count\": 50, \"total\": 69, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1919}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "a997a201-29c4-414d-a165-d8aa1c327343",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"hsweep_h20_seed1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-18T18:04:42.684Z\\\", \\\"updated_at\\\": \\\"2026-05-18T19:14:40.086Z\\\", \\\"hypothesis\\\": \\\"h=20 with step_independent generation provides 20-step observation windows. Key data point for fig5 cliff figure: with h=10 and h=5 both collapsing, h=20 tests whether 20 steps of context is sufficient for recovery. If h=20 recovers (val > 0% at step 5+), the cliff is between h=10 and h=20. If still collapsed, the minimum viable context window is larger than 20 steps.\\\", \\\"parent\\\": \\\"hsweep_h10_seed1\\\", \\\"notes\\\": \\\"诊断中: worker_diagnose_hsweep_h20_seed1_20260518T184044 正在 SSH 深查失败原因。日志尾部无 Traceback，疑似系统级 kill (OOM/磁盘)。\\\"}, \\\"hsweep_h10_seed1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-17T17:30:46.964Z\\\", \\\"updated_at\\\": \\\"2026-05-18T19:09:46.781Z\\\", \\\"hypothesis\\\": \\\"h=10 with step_independent generation provides 10-step observation windows. Key data point for fig5 cliff figure: if h=10 shows recovery (val > 0%), the cliff is between h=5 and h=10. If still collapsed, cliff is between h=10 and full context (h=28).\\\", \\\"parent\\\": \\\"hsweep_h2_seed1\\\", \\\"notes\\\": \\\"Director 批准临时 kill（刚启动几分钟，无进度损失）以释放 bjb1 cuda:0,1 跑 exp029 + hsweep_h2_seed2 双 reeval。Reeval 完成后重启。原由 auto_next_hsweep.sh 自动启动，未经正式审批。\\\"}, \\\"factorial_h2_episodeadv_seed2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-18T04:48:02.228Z\\\", \\\"updated_at\\\": \\\"2026-05-18T18:25:27.297Z\\\", \\\"hypothesis\\\": \\\"Replicate factorial experiment (step-independent + episode-level advantage) with different seed to confirm that sign misattribution elimination is robust, not single-seed artifact. Same config, different seed, 15 steps.\\\", \\\"parent\\\": \\\"factorial_h2_episodeadv_seed1\\\"}, \\\"exp029_episode_level_seed2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T04:48:01.826Z\\\", \\\"updated_at\\\": \\\"2026-05-18T18:25:16.249Z\\\", \\\"hypothesis\\\": \\\"Replicate exp029 episode-level result (23.88% OOD) with different seed to confirm statistical robustness. P0 priority: core positive claim built on single seed is desk-reject risk. Same SFT checkpoint, same config, seed=43, 15 steps, AlfworldSG_OOD 134 tasks eval.\\\", \\\"parent\\\": \\\"exp029_episode_level\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"Director 止损 kill。bjb1 累计 10+ 次失败。step 15 val=21.875% (32 tasks)，数据保留在 /root/autodl-tmp/checkpoints/exp029-seed2/。计划转移到 westd cuda:0,1 继续（factorial 完成后）。\\\"}, \\\"gsweep_g100_h5_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T13:56:58.033Z\\\", \\\"updated_at\\\": \\\"2026-05-18T17:36:39.529Z\\\", \\\"hypothesis\\\": \\\"γ=1.0 (no discount) tests whether collapse in h=5 is caused by sign misattribution from magnitude decay. If γ=1.0 also collapses, sign misattribution is not solely from discount-induced magnitude decay.\\\", \\\"parent\\\": \\\"gsweep_g095_h5_seed1\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"conclusion_reason\\\": \\\"collapsed, γ=1.0 also collapses confirming sign misattribution not solely from magnitude decay\\\"}}, \\\"gsweep_g095_h5_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T13:56:55.994Z\\\", \\\"updated_at\\\": \\\"2026-05-18T13:11:09.941Z\\\", \\\"hypothesis\\\": \\\"γ=0.95 with h=5 is the control condition matching hsweep_h5. Early windows retain γ^9 ≈ 0.95^9 ≈ 63% of terminal return. Expected to reproduce h5 behavior from h-sweep.\\\", \\\"parent\\\": \\\"hsweep_h2_seed1\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"val_success_step5\\\": 0, \\\"conclusion_reason\\\": \\\"collapsed at step 5, val=0%\\\"}}, \\\"factorial_h2_episodeadv_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T18:17:23.327Z\\\", \\\"updated_at\\\": \\\"2026-05-18T10:22:36.071Z\\\", \\\"hypothesis\\\": \\\"Step_independent generation (h=2) with episode-level advantage eliminates sign misattribution while preserving truncated-context inference. If success >> h=2 step-level (0%), information loss alone does not cause collapse — sign misattribution is the primary driver. If success ≈ 0%, information loss is sufficient to cause collapse regardless of advantage computation. This is the key factorial experiment separating the two mechanisms.\\\", \\\"parent\\\": \\\"hsweep_h2_seed1\\\", \\\"metrics\\\": {\\\"completed_steps\\\": \\\"15/15\\\", \\\"wandb_run_id\\\": \\\"6liw7fm1\\\", \\\"val_step5\\\": {\\\"success\\\": 0.0597, \\\"dataset\\\": \\\"AlfworldOOD_134tasks\\\"}, \\\"val_step15\\\": {\\\"success\\\": 0.0075}, \\\"kl_loss_trajectory\\\": {\\\"step1\\\": 0.238, \\\"step5\\\": 0.735, \\\"step10\\\": 1.029, \\\"step15\\\": 2.845}, \\\"ppo_kl_range\\\": \\\"0.025-0.096\\\", \\\"best_checkpoint\\\": \\\"global_step_5\\\", \\\"best_val_success\\\": 0.0597, \\\"train_step1\\\": {\\\"success\\\": 0.203, \\\"pass_at_8\\\": 0.688}, \\\"train_step6\\\": {\\\"success\\\": 0.258, \\\"pass_at_8\\\": 0.813}, \\\"checkpoint_paths\\\": {\\\"step5\\\": \\\"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_5/\\\", \\\"step10\\\": \\\"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_10/\\\", \\\"step15\\\": \\\"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_15/\\\"}, \\\"exit_cause\\\": \\\"W&B atexit BrokenPipeError (false positive)\\\", \\\"kl_issue\\\": \\\"kl_loss_coef=0.01 too low, policy drifted after step 5\\\", \\\"status_note\\\": \\\"COMPLETED. Best val OOD 5.97% at step 5. Degraded to 0.75% by step 15 due to KL drift. Sign misattribution elimination confirmed: 5.97% vs 0% (step-level h=2).\\\"}, \\\"notes\\\": \\\"W&B 深度分析确认：sign misattribution 是 collapse 的 primary driver。关键证据：step 3→4 hsweep action_valid 91.3%→43.1% (catastrophic collapse) vs factorial 保�� 79-85% (无崩溃)。V-shaped recovery (20.3%→3.1%→15.63%) 是探索期波动非不可逆退化。3-cell 贡献：sign misattribution ~6pp (0%→5.97% val), information loss ~22pp (5.97%→28.1% val)。Sign misattribution pp 贡献较小但是 catastrophic collapse 的质变 trigger。\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"gsweep_g080_h5_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T13:56:53.634Z\\\", \\\"updated_at\\\": \\\"2026-05-18T09:35:23.404Z\\\", \\\"hypothesis\\\": \\\"γ=0.8 with h=5 represents an intermediate decay rate where early windows retain γ^9 ≈ 0.8^9 ≈ 13% of terminal return, potentially showing delayed but still present collapse compared to γ=0.95 (39%).\\\", \\\"parent\\\": \\\"hsweep_h2_seed1\\\", \\\"metrics\\\": {\\\"step5_val_success\\\": \\\"3.125%\\\", \\\"step5_entropy\\\": 0.185, \\\"subsequent_steps\\\": \\\"all 0%\\\", \\\"conclusion_note\\\": \\\"Complete collapse confirmed. γ=0.80 with h=5 shows catastrophic failure — killed early by Director as no new information expected. Supports hypothesis that lower gamma accelerates collapse.\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"hsweep_h2_seed2_reeval_ood\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T04:12:03.656Z\\\", \\\"updated_at\\\": \\\"2026-05-18T05:13:33.875Z\\\", \\\"hypothesis\\\": \\\"Evaluate hsweep_h2_seed2 checkpoint (step 15) on OOD 134 tasks to get comparable metric with exp029 reeval (23.88%). If val success remains low (~9% in-distribution), confirms collapse is real even with late recovery.\\\", \\\"parent\\\": \\\"hsweep_h2_seed2\\\", \\\"metrics\\\": {\\\"success\\\": 0.0373, \\\"action_is_valid\\\": 0.994, \\\"action_is_effective\\\": 1, \\\"pass_at_1\\\": 0.0373, \\\"num_actions\\\": 48.53, \\\"response_length\\\": 8501, \\\"dataset\\\": \\\"AlfworldSG_OOD_134tasks\\\", \\\"date\\\": \\\"2026-05-18\\\", \\\"note\\\": \\\"Valid actions (99.4%) but cannot complete tasks - generates long ineffective sequences\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp029_episode_level\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-16T08:49:53.280Z\\\", \\\"updated_at\\\": \\\"2026-05-18T04:11:39.305Z\\\", \\\"hypothesis\\\": \\\"Episode-level 训练（context_window_mode: full）解决 step_independent h=2 的信用分配缺陷，模型能学到跨步规划策略，val success 不再停滞于 baseline。\\\", \\\"parent\\\": \\\"exp028c_selfguide_recipe\\\", \\\"notes\\\": \\\"Director 决策 early-stop at step 15（val success 28.125%, pass@8=92.9%）释放 GPU 给 h-sweep。MVP 已通过（step 5 val=25%, 2x baseline）。Episode-level 训练假设确认：从 12.5% baseline 提升到 28.125%，而 step-independent 崩塌到 0%。Checkpoint: global_step_15。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"reeval_ood_134tasks\\\": {\\\"success\\\": 0.2388, \\\"action_is_valid\\\": 0.5683, \\\"action_is_effective\\\": 0.916, \\\"manager_invalid_action\\\": 0.0839, \\\"reward_mean\\\": 2.388, \\\"best_at_8\\\": 8.88, \\\"dataset\\\": \\\"AlfworldSG_OOD_134tasks\\\", \\\"date\\\": \\\"2026-05-18\\\"}}}, \\\"gsweep_g050_h5_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T13:56:51.277Z\\\", \\\"updated_at\\\": \\\"2026-05-18T02:56:21.234Z\\\", \\\"hypothesis\\\": \\\"γ=0.5 with h=5 will show accelerated collapse compared to default γ=0.95, because γ^k decay compounds: early windows receive only γ^(N-1) ≈ 0.5^9 ≈ 0.2% of terminal return, making sign misattribution maximally severe.\\\", \\\"parent\\\": \\\"hsweep_h2_seed1\\\", \\\"notes\\\": \\\"Director 批准 early kill (step 12/15)。Hypothesis 完全确认：γ=0.5 加速 collapse，从 step 1 起 train success 基本为 0%，val step 5/10 全零，KL step 8 spike 到 0.209。step 10 checkpoint 已保存。数据足够用于论文 gamma sweep figure。Watchdog 预期自动启动 g080。\\\", \\\"metrics\\\": {\\\"current_step\\\": \\\"12/15\\\", \\\"train_success_collapsed_at\\\": \\\"step 1\\\", \\\"train_success_all_steps\\\": \\\"0-2.3% (effectively 0%)\\\", \\\"val_step0\\\": {\\\"success\\\": 0.094}, \\\"val_step5\\\": {\\\"success\\\": 0, \\\"reward\\\": 0}, \\\"val_step10\\\": {\\\"success\\\": 0, \\\"reward\\\": 0, \\\"response_length\\\": 1412}, \\\"kl_sequence\\\": [0.019, 0.025, 0.018, 0.014, 0.01, 0.009, 0.009, 0.209, 0.018], \\\"kl_spike_step8\\\": 0.209, \\\"checkpoint\\\": \\\"global_step_10\\\", \\\"eta\\\": \\\"~5h from 02:46 UTC\\\", \\\"status_note\\\": \\\"COMPLETELY COLLAPSED. Train success 0% from step 1. KL spike 20x at step 8. Val all zeros. Remaining 3 steps waste GPU. Recommend early kill.\\\"}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"hsweep_h2_seed2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T14:37:14.817Z\\\", \\\"updated_at\\\": \\\"2026-05-18T02:55:38.705Z\\\", \\\"hypothesis\\\": \\\"h=2 seed 2 replicates seed 1 catastrophic collapse (step 3-4 onset, 0% by step 9+), confirming collapse is robust not single-run artifact. Additionally LOG_PER_SAMPLE_ADV=1 collects per-window advantage data for plan_004 sign misattribution empirical verification.\\\", \\\"parent\\\": \\\"hsweep_h2_seed1\\\", \\\"metrics\\\": {\\\"current_step\\\": \\\"15/15\\\", \\\"completed\\\": true, \\\"val_step5\\\": {\\\"success\\\": 0}, \\\"val_step10\\\": {\\\"success\\\": 0}, \\\"val_step15\\\": {\\\"success\\\": 0.09375}, \\\"train_step14\\\": {\\\"success\\\": 0.2656, \\\"pass_at_8\\\": 0.6875}, \\\"train_step15\\\": {\\\"success\\\": 0.2812, \\\"pass_at_8\\\": 0.625, \\\"entropy\\\": 0.401, \\\"ppo_kl\\\": 0.006}, \\\"train_success_peak\\\": {\\\"step\\\": 15, \\\"value\\\": 0.2812}, \\\"adv_log_lines\\\": 3000, \\\"adv_episodes\\\": {\\\"total\\\": 128, \\\"success\\\": 65, \\\"fail\\\": 63}, \\\"adv_analysis\\\": {\\\"sign_outcome_agreement\\\": 0.5207, \\\"point_biserial_r\\\": 0.068, \\\"p_adv_pos_given_success\\\": 0.3706, \\\"p_adv_pos_given_failure\\\": 0.306, \\\"magnitude_decay_gamma\\\": 0.9426, \\\"distribution_overlap\\\": 0.878, \\\"verdict\\\": \\\"52% agreement confirms advantage signal nearly uninformative about episode outcome = sign misattribution\\\"}, \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15/\\\", \\\"checkpoint_warning\\\": \\\"seed2 overwrote seed1 step15 checkpoint in same directory\\\", \\\"status_note\\\": \\\"COMPLETED 15/15. Late recovery at step 14-15 (train 26-28%). Val 9.375% on 16 in-dist tasks. ADV: 52% sign agreement = near-random.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"15/15 步正常完成 + final val。Hypothesis NOT confirmed：seed2 未复现 seed1 的 catastrophic collapse。关键差异：(1) action_is_valid 始终 88-100%（seed1 崩至 0.06%）(2) val step 15 恢复到 9.375%（seed1 终值 0%）(3) train step 15 success=28.1%（seed1 终值 0%）。Val step 0/5/10 确实为 0%，说明 h=2 确实造成学习困难，但不是 seed1 那样的不可逆 catastrophic collapse。Collapse 行为是 seed-dependent 的，不是 robust finding。ADV log 3000 行可用于 sign misattribution 分析。注意：checkpoint 写入 hsweep-h2/ 目录（与 seed1 共享，global_step_15 被覆盖）。\\\"}, \\\"gae_baseline_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T14:05:31.533Z\\\", \\\"updated_at\\\": \\\"2026-05-17T19:19:48.391Z\\\", \\\"hypothesis\\\": \\\"REINFORCE++ (running-mean baseline, no critic) provides modest improvement over episode-level GRPO due to per-token advantage normalization. Fallback from GAE due to TRL 1.1.0 removing AutoModelForCausalLMWithValueHead (critic head unavailable).\\\", \\\"parent\\\": \\\"exp029_episode_level\\\", \\\"metrics\\\": {\\\"wandb_run_id\\\": \\\"dt79qyd9\\\", \\\"pid\\\": 40267, \\\"val_step0\\\": {\\\"success\\\": 0.0625, \\\"action_is_valid\\\": 0.7796}, \\\"val_step5\\\": {\\\"success\\\": 0.125, \\\"action_is_valid\\\": 0.6926}, \\\"val_step10\\\": {\\\"success\\\": 0.125, \\\"pass_at_1\\\": 0.125, \\\"reward_mean\\\": 1.25}, \\\"train_step9\\\": {\\\"success\\\": 0.0313, \\\"action_is_valid\\\": 0.6033, \\\"pass_at_8\\\": 0.25}, \\\"server\\\": \\\"westd-47453\\\", \\\"gpu\\\": \\\"cuda:0,1\\\", \\\"method\\\": \\\"reinforce_plus_plus\\\", \\\"fallback_reason\\\": \\\"TRL 1.1.0 removed AutoModelForCausalLMWithValueHead\\\", \\\"current_step\\\": \\\"11/15\\\"}, \\\"notes\\\": \\\"实际运行 REINFORCE++ (adv_estimator=reinforce_plus_plus_baseline)，非 GAE。GAE 因 TRL 1.1.0 移除 AutoModelForCausalLMWithValueHead 不可用 (D060)。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"hsweep_h2_seed1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-17T04:37:11.061Z\\\", \\\"updated_at\\\": \\\"2026-05-17T14:36:40.246Z\\\", \\\"hypothesis\\\": \\\"Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality\\\", \\\"parent\\\": \\\"exp029_episode_level\\\", \\\"metrics\\\": {\\\"train_step\\\": 15, \\\"total_steps\\\": 15, \\\"wandb_run_id\\\": \\\"7o9bjszm\\\", \\\"step1\\\": {\\\"success\\\": 0.1875, \\\"pass_at_8\\\": 0.4375, \\\"invalid_action\\\": 0.027}, \\\"step2\\\": {\\\"success\\\": 0.1484, \\\"pass_at_8\\\": 0.5, \\\"invalid_action\\\": 0.02}, \\\"step3\\\": {\\\"success\\\": 0.1875, \\\"pass_at_8\\\": 0.625, \\\"invalid_action\\\": 0.028}, \\\"step4\\\": {\\\"success\\\": 0.0547, \\\"pass_at_8\\\": 0.25, \\\"invalid_action\\\": 0.264}, \\\"step5\\\": {\\\"success\\\": 0.0156, \\\"pass_at_8\\\": 0.0625, \\\"invalid_action\\\": 0.369}, \\\"step6\\\": {\\\"success\\\": 0.0313, \\\"pass_at_8\\\": 0.25, \\\"invalid_action\\\": 0.471}, \\\"step7\\\": {\\\"success\\\": 0.0469, \\\"pass_at_8\\\": 0.1875, \\\"invalid_action\\\": 0.502}, \\\"step8\\\": {\\\"success\\\": 0.0156, \\\"pass_at_8\\\": 0.125, \\\"invalid_action\\\": 0.542}, \\\"step9\\\": {\\\"success\\\": 0, \\\"pass_at_8\\\": 0, \\\"invalid_action\\\": 0.641}, \\\"step10\\\": {\\\"success\\\": 0.0234}, \\\"step11_15\\\": {\\\"success\\\": 0, \\\"invalid_action\\\": 0.972}, \\\"val_final\\\": {\\\"success\\\": 0, \\\"invalid_action\\\": 0.999, \\\"action_is_valid\\\": 0.0006}, \\\"checkpoint\\\": \\\"global_step_5,10,15\\\", \\\"checkpoint_path\\\": \\\"/root/autodl-tmp/checkpoints/hsweep-h2/\\\", \\\"log_path\\\": \\\"~/runs/cost-verify-agent-rl/hsweep_h2_s1.log\\\", \\\"gpu_util\\\": \\\"95-100%\\\", \\\"collapse_onset\\\": \\\"step3→step4\\\", \\\"elapsed_hours\\\": 10.04, \\\"step15_entropy\\\": 0.342, \\\"step15_kl_loss\\\": 0.777, \\\"step15_grad_norm\\\": 1.611, \\\"auto_next_triggered\\\": true, \\\"seed2_pid\\\": 945877, \\\"seed2_wandb\\\": \\\"jhwyg4tc\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"notes\\\": \\\"15 steps 完成。Hypothesis 验证：h=2 step_independent 确实灾难性崩溃（step 3→4 onset, step 9 归零, step 11-15 持续为零）。Final val: success=0%, invalid_action=99.9%, action_is_valid=0.06%。模型彻底退化到几乎只输出无效动作。\\\"}, \\\"exp025c\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T08:09:29.393Z\\\", \\\"updated_at\\\": \\\"2026-05-17T10:53:00.425Z\\\", \\\"notes\\\": \\\"项目已 pivot 到 h-sweep + sign misattribution 诊断方向（D054/D057）。exp025c 属于 pivot 前的实验设计，不在当前 experiment_plan.yaml 中，与论文核心 claims 无关联。GPU 资源优先用于 h-sweep 和 GAE baseline。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp026_step_independent_grpo\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T09:34:33.675Z\\\", \\\"updated_at\\\": \\\"2026-05-17T03:14:31.315Z\\\", \\\"notes\\\": \\\"exp026 negative: step-independent GRPO 在 step 2 达峰 train success=32.81% 后连续崩塌至 step 4 的 0%。Step 5 val eval 未完成即被 kill（val 生成阶段启动后进程被终止），无法对比 step 0 vs step 5 val。无 checkpoint（save_freq=25 未触发）。根因分析（Reviewer）：sparse reward + 小 env_groups(4=64 rollouts) 导致全零 batch 概率高，advantage 只有负信号把策略推回 reference。action_is_valid 在 step 2-4 保持 ~72% 但 success 归零，模型学会了\\\\\\\"看起来合理\\\\\\\"的 action 但丧失任务完成能力。教训：(1) save_freq 必须 ≤5 捕获早期峰值 (2) env_groups 需 ≥8 降低全零 batch 概率 (3) WANDB_MODE=disabled 导致 cron 误判 (4) cron 应监控 Ray TaskRunner PID 而非 shell wrapper PID。\\\", \\\"metrics\\\": {\\\"val_before_train_success\\\": 0.0625, \\\"val_before_train_action_is_valid\\\": 0.631, \\\"val_before_train_episodes\\\": 16, \\\"train_step1_success\\\": 0.2188, \\\"train_step1_action_is_valid\\\": 0.686, \\\"train_step1_entropy\\\": 0.2672, \\\"train_step1_kl_loss\\\": 0.1797, \\\"train_step1_grad_norm\\\": 14.43, \\\"train_step1_reward_mean\\\": 1.218, \\\"train_step1_pass_at_16\\\": 1, \\\"train_step2_success\\\": 0.3281, \\\"train_step2_action_is_valid\\\": 0.603, \\\"train_step2_entropy\\\": 0.317, \\\"train_step2_kl_loss\\\": 0.0974, \\\"train_step2_grad_norm\\\": 15.62, \\\"train_step2_reward_mean\\\": 1.62, \\\"train_step2_pass_at_16\\\": 1, \\\"train_step3_success\\\": 0.1719, \\\"train_step3_action_is_valid\\\": 0.641, \\\"train_step3_entropy\\\": 0.387, \\\"train_step3_kl_loss\\\": 0.2617, \\\"train_step3_grad_norm\\\": 15.65, \\\"train_step3_reward_mean\\\": 1.079, \\\"train_step3_pass_at_16\\\": 0.75, \\\"train_step4_success\\\": 0, \\\"train_step4_action_is_valid\\\": 0.717, \\\"train_step4_entropy\\\": 0.387, \\\"train_step4_kl_loss\\\": 0.054, \\\"train_step4_grad_norm\\\": 13.81, \\\"train_step4_pass_at_16\\\": 0}, \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"Step-independent GRPO（每步独立优化、不建模跨步依赖）能在ALFWorld多步任务中学到有效策略，因为每步的local reward信号足以引导正确行为选择\\\", \\\"parent\\\": \\\"exp021_ragen_sft_v4\\\"}, \\\"exp019b_expert_sft_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T17:30:00.085Z\\\", \\\"updated_at\\\": \\\"2026-05-17T03:14:30.703Z\\\", \\\"hypothesis\\\": \\\"Two-stage Expert SFT: exp008_sft checkpoint + v3 data (original move actions + admissible actions). LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096. Pass: success>=10%, format_ok>=90%, action_is_valid>=85%.\\\", \\\"notes\\\": \\\"训练成功完成 320/320 steps (2 epochs, 47:49)。Cron 多次误报 failed（监控错误 PID / 无法区分正常退出与崩溃）。Checkpoint: /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.0718, \\\"eval_loss\\\": 0.0428, \\\"eval_mean_token_accuracy\\\": 0.9869, \\\"train_runtime_seconds\\\": 2869.8, \\\"steps\\\": 320, \\\"epochs\\\": 2, \\\"eval_success_rate\\\": 0.2, \\\"eval_format_ok\\\": 1, \\\"eval_action_is_valid\\\": 0.8533, \\\"eval_episodes\\\": 20, \\\"eval_avg_steps\\\": 25.4, \\\"eval_time_seconds\\\": 146}, \\\"parent\\\": \\\"exp008_sft\\\"}, \\\"exp013f\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:21:46.227Z\\\", \\\"updated_at\\\": \\\"2026-05-17T03:14:29.725Z\\\", \\\"hypothesis\\\": \\\"Dense reward shaping(valid_action_bonus=0.15)为全失败GRPO group提供非零方差梯度信号，使模型在避免梯度collapse的同时学到task success而非仅优化bonus\\\", \\\"parent\\\": \\\"exp013e\\\", \\\"metrics\\\": {\\\"step\\\": 30, \\\"total_steps\\\": 30, \\\"completed\\\": true, \\\"exit_code\\\": 0, \\\"training_time_s\\\": 10683, \\\"step6_success\\\": 0.0156, \\\"step7_success\\\": 0.0781, \\\"step10_success\\\": 0, \\\"step17_success\\\": 0.0156, \\\"final_val_success\\\": 0, \\\"final_val_action_is_valid\\\": 0.975, \\\"final_val_action_is_effective\\\": 1, \\\"final_val_reward_mean_at4\\\": 4.388, \\\"final_val_reward_std_at4\\\": 0.195, \\\"final_val_reward_best_at4\\\": 4.499, \\\"final_val_pass_at1\\\": 0, \\\"action_is_valid_trend\\\": \\\"60%→65.9%→77.1%→97.5%\\\", \\\"success_trend\\\": \\\"0%→1.56%→7.81%→0%→1.56%→0%\\\", \\\"grad_norm_range\\\": \\\"1.7-2.9 (no collapse)\\\", \\\"conclusion_reason\\\": \\\"Dense reward gaming: model optimized valid_action_bonus (action_is_valid 60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse prevented but task completion not learned.\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"notes\\\": \\\"30/30 步完成，EXIT_CODE=0。Dense reward shaping 成功解决了 exp012b 的 catastrophic collapse（grad_norm 稳定 1.7-2.9），但产生 reward gaming：模型最大化 valid_action_bonus 而非 success_reward。action_is_valid 60%→97.5%（学会合法命令），success 始终 0-8%（未学会完成任务）。final_val reward/mean@4=4.388 ≈ 29 valid_actions × 0.15，几乎无 success_reward 贡献。Disk warning: /root/autodl-tmp 95% full (4.1GB remaining)。Ray log 备份失败（脚本执行时 session 已清理）。Checkpoint: global_step_30 已保存。\\\"}, \\\"exp028_prereq_zeroshot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T21:11:06.120Z\\\", \\\"updated_at\\\": \\\"2026-05-17T03:14:28.598Z\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"wandb_run_id\\\": \\\"qdvv09da\\\", \\\"metrics\\\": {\\\"success\\\": 0, \\\"action_is_valid\\\": 0.75, \\\"num_actions\\\": 50, \\\"pass_at_1\\\": 0, \\\"response_length\\\": 75.07}, \\\"notes\\\": \\\"Qwen3-1.7B（本身就是 instruct 模型）零样本 ALFWorld eval = 0% success。证明 SFT 从 0%→6.25% 是有益的，D044 '不做SFT' 假设不成立。W&B run: qdvv09da\\\", \\\"hypothesis\\\": \\\"Qwen3-1.7B base模型具备ALFWorld零样本能力(success>0%)，无需SFT即可作为GRPO冷启动点——如成立则SFT引入的分布偏差可能反而有害\\\"}, \\\"exp008_sft\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T03:04:47.496Z\\\", \\\"updated_at\\\": \\\"2026-05-17T03:14:25.946Z\\\", \\\"notes\\\": \\\"SFT 转换脚本修复后重跑成功。Eval 方法: 独立脚本 eval_sft_model.py, 4 episodes (seed=0,1,2,3), HF generate() + AlfredTXTEnv, cuda:1, max_steps=50。action_is_valid=90% (180/200 actions), format_ok=100%, success_rate=0%。完整 50-episode eval 未完成（为 GRPO 让出 GPU）。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"action_is_valid\\\": 0.9, \\\"format_ok\\\": 1, \\\"success_rate\\\": 0, \\\"final_loss\\\": 0.069, \\\"final_token_accuracy\\\": 0.973, \\\"data_count\\\": 1200, \\\"epochs\\\": 3, \\\"total_steps\\\": 225, \\\"training_time_s\\\": 576}, \\\"hypothesis\\\": \\\"基础格式SFT使Qwen3-1.7B学会ALFWorld动作格式和有效动作选择(format_ok+action_is_valid)，建立可训练基线，为后续expert SFT和GRPO提供非随机起点\\\"}, \\\"exp028c_selfguide_recipe\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T21:38:48.089Z\\\", \\\"updated_at\\\": \\\"2026-05-16T08:29:53.723Z\\\", \\\"wandb_run_id\\\": \\\"4yu6qz1m\\\", \\\"notes\\\": \\\"D052 终止。step_independent h=2 导致灾难性过拟合：step_5_val best@128=10.0 → step_10_val best@800=0.0。train success 波动上升(peak 21.88%)=局部动作过拟合，但无法泛化到新 game。根因：(1) step_independent 破坏长程信用分配 (2) self-guidance reward 缺失 (3) val 仅 16 episodes。参见 selfguide_setup_audit.md。\\\", \\\"metrics\\\": {\\\"step_0_val\\\": {\\\"success\\\": 6.25, \\\"pass_at_1\\\": 6.25, \\\"action_is_valid\\\": 74.5, \\\"score_mean\\\": 0.119}, \\\"step_1_train\\\": {\\\"success\\\": 13.28, \\\"pass_at_8\\\": 37.5, \\\"action_is_valid\\\": 76.4, \\\"action_is_effective\\\": 96.37, \\\"entropy\\\": 0.2634, \\\"kl_loss\\\": 0.0128, \\\"ppo_kl\\\": 0.019, \\\"grad_norm\\\": 16.88, \\\"score_mean\\\": 0.843, \\\"time_s\\\": 3252, \\\"note\\\": \\\"三方交叉验证通过\\\"}, \\\"step_2_train\\\": {\\\"success\\\": 6.25, \\\"pass_at_8\\\": 25, \\\"action_is_valid\\\": 83.2, \\\"entropy\\\": 0.247, \\\"kl_loss\\\": 0.1706, \\\"pg_loss\\\": 0.007, \\\"grad_norm\\\": 17.3, \\\"score_mean\\\": 0.274, \\\"time_s\\\": 3120}, \\\"step_3_train\\\": {\\\"success\\\": 15.63, \\\"pass_at_8\\\": 68.75, \\\"action_is_valid\\\": 85.9, \\\"entropy\\\": 0.2488, \\\"kl_loss\\\": 0.1118, \\\"grad_norm\\\": 12.57, \\\"score_mean\\\": 0.661, \\\"time_s\\\": 2760}, \\\"step_4_train\\\": {\\\"success\\\": 18.75, \\\"pass_at_8\\\": 62.5, \\\"action_is_valid\\\": 87.94, \\\"entropy\\\": 0.234, \\\"kl_loss\\\": 0.031, \\\"ppo_kl\\\": 0.015}, \\\"step_5_train\\\": {\\\"success\\\": 9.4, \\\"pass_at_8\\\": 37.5, \\\"action_is_valid\\\": 89.6, \\\"entropy\\\": 0.236, \\\"kl_loss\\\": 0.824, \\\"grad_norm\\\": 13.1}, \\\"step_5_val\\\": {\\\"success\\\": 6.25, \\\"pass_at_1\\\": 6.25, \\\"action_is_valid\\\": 96.5, \\\"action_is_effective\\\": 100, \\\"num_actions\\\": 49.4, \\\"score_mean\\\": 0.518}, \\\"step_6_train\\\": {\\\"success\\\": 10.94, \\\"action_is_valid\\\": 90.4, \\\"entropy\\\": 0.234, \\\"kl_loss\\\": 0.098, \\\"grad_norm\\\": 12.54}, \\\"step_7_train\\\": {\\\"success\\\": 21.88, \\\"pass_at_8\\\": 56.25, \\\"action_is_valid\\\": 91.8, \\\"entropy\\\": 0.224, \\\"kl_loss\\\": 0.046}, \\\"step_8_train\\\": {\\\"success\\\": 15.6, \\\"pass_at_8\\\": 50, \\\"action_is_valid\\\": 92.7, \\\"kl_loss\\\": 0.039, \\\"entropy\\\": 0.204}, \\\"step_9_train\\\": {\\\"success\\\": 18, \\\"pass_at_8\\\": 56.3, \\\"action_is_valid\\\": 93.6, \\\"kl_loss\\\": 0.047, \\\"entropy\\\": 0.204}, \\\"step_10_train\\\": {\\\"success\\\": 18.75, \\\"action_is_valid\\\": 90.7, \\\"kl_loss\\\": 0.197}, \\\"step_10_val\\\": {\\\"success\\\": 0, \\\"pass_at_1\\\": 0, \\\"best_at_128\\\": 0, \\\"best_at_800\\\": 0, \\\"action_is_valid\\\": 93.6, \\\"num_actions\\\": 49.8, \\\"reward_mean\\\": 0, \\\"note\\\": \\\"灾难性崩溃，模型完全遗忘\\\"}}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp028a_recipe_fix\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T21:08:53.131Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:25:46.006Z\\\", \\\"hypothesis\\\": \\\"invalid_action_penalty (-0.1) 为全失败 GRPO group 提供非零方差梯度信号。从 exp021 SFT checkpoint (6.25% success) 出发，仅增加 invalid_action_penalty_coef=0.1，其余参数与 exp027 完全一致。预期：penalty 让失败 trajectory 间有区分（invalid action 多=reward更低），解决 ~43% group 零梯度问题。Pass: success ≥20%（稳定，非瞬时 peak）。\\\", \\\"parent\\\": \\\"exp027_stable_grpo\\\", \\\"wandb_run_id\\\": \\\"lu42su82\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"与 exp027 功能等价（penalty getattr 默认值=0.1 在 exp027 中已生效）。Director 指令停止。\\\"}, \\\"exp028_prereq_zeroshot_instruct\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-15T20:59:57.529Z\\\", \\\"updated_at\\\": \\\"2026-05-15T21:06:09.982Z\\\", \\\"hypothesis\\\": \\\"Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\\\\\\\"SFT是毒药\\\\\\\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。\\\", \\\"parent\\\": \\\"exp027_stable_grpo\\\", \\\"notes\\\": \\\"Qwen3-1.7B 确认就是 instruct 模型（无独立 Instruct 变体）。零样本 eval 0% success / 0.75% valid（与之前结果一致）。关键结论：\\\\\\\"SFT是毒药\\\\\\\"假设(D044)不成立——SFT 实际提升了 0%→6.25%。62pp gap 根因排除 SFT，聚焦于 binary reward 零梯度 + mini-batch 过小 + 训练步数不足。\\\"}, \\\"exp027_stable_grpo\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T14:04:13.123Z\\\", \\\"updated_at\\\": \\\"2026-05-15T20:44:26.582Z\\\", \\\"notes\\\": \\\"进程退出原因：Ray raylet 被异常终止（ActorUnavailableError: RPC error: Socket closed rpc_code: 14）。Raylet termination unexpected — 可能 SIGKILL by OOM killer 或内存访问错误。退出发生在 step 4 完成后、step 5 开始前。EXIT_CODE=1。D045 已判定 MVP 未通过（train success 13.28% < 20% 阈值）。Recipe Gap 诊断三大根因：(1) SFT 起点反效果 (2) Binary reward 零梯度 (3) Mini-batch 8× 过小。exp028 配置准备中（5 个 Worker 活跃）。\\\", \\\"hypothesis\\\": \\\"Stabilized step-independent GRPO: 针对 exp026 死亡螺旋根因（sparse reward + 小 env_groups 导致全零 batch），增加 rollouts（env_groups 4→8, 128 trajectories）、降低 LR（1e-6→5e-7）、降低 KL（0.01→0.005）、新增 entropy bonus（0.01）、save_freq 5 捕获峰值。50 步快速验证。Pass: success ≥20% 且无连续 2 步归零。\\\", \\\"parent\\\": \\\"exp026_step_independent_grpo\\\", \\\"wandb_run_id\\\": \\\"y7jiibqk\\\", \\\"metrics\\\": {\\\"step_0_val_before_train\\\": {\\\"success\\\": 6.25, \\\"action_is_valid\\\": 63.125, \\\"action_is_effective\\\": 87.875, \\\"num_actions\\\": 42.375, \\\"response_length\\\": 114.67, \\\"reward_mean\\\": 0.3226, \\\"val_generation_time_s\\\": 502.57}, \\\"step_1_train\\\": {\\\"success\\\": 35.94, \\\"kl_loss\\\": 0.058, \\\"batch_size\\\": 5152, \\\"training_time_s\\\": 4342}, \\\"step_2_train\\\": {\\\"success\\\": 10.16, \\\"kl_loss\\\": 0.413, \\\"batch_size\\\": 6144, \\\"training_time_s\\\": 5886}, \\\"step_3_train\\\": {\\\"success\\\": 10.16, \\\"kl_loss\\\": 0.248, \\\"entropy\\\": 0.385, \\\"pass_at_16\\\": 0.5, \\\"grad_norm\\\": 21.31, \\\"reward_mean\\\": 0.483, \\\"batch_size\\\": 6048, \\\"training_time_s\\\": 4689}, \\\"step_4_train\\\": {\\\"success\\\": 13.28, \\\"pass_at_16\\\": 0.375, \\\"note\\\": \\\"Director判定: 趋势确认, MVP未通过\\\"}}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp025b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T07:34:34.283Z\\\", \\\"updated_at\\\": \\\"2026-05-15T07:44:26.903Z\\\", \\\"parent\\\": \\\"exp025\\\", \\\"notes\\\": \\\"三次提交均失败。第三次：pre-flight 清理后 Ray 主进程启动成功、数据加载成功（8810 train / 494 val），但 AlfworldWorker 进程初始化时线程创建失败（Resource temporarily unavailable, EAGAIN）。36+ 次 system:11 错误，43+ 次 Fatal Python error: Aborted。jemalloc arena background thread creation failed。根因：系统 nproc/线程上限不足，8 个 AlfworldWorker + Ray 内部线程总数超限。需排查 ulimit -u 和 /proc/sys/kernel/threads-max。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp025\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T06:52:48.190Z\\\", \\\"updated_at\\\": \\\"2026-05-15T07:34:25.374Z\\\", \\\"notes\\\": \\\"崩溃原因：(1) conda activate base 错误，应用 /root/autodl-tmp/conda-envs/verl-agent 环境 (2) save_freq=-1 未修改为 25。ModuleNotFoundError — base 环境缺 verl-agent 依赖。教训：提交前必须验证 which python 指向正确环境 + 关键参数在 config 中与预期一致。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp021_ragen_sft_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T02:09:31.719Z\\\", \\\"updated_at\\\": \\\"2026-05-15T06:24:16.570Z\\\", \\\"hypothesis\\\": \\\"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer&gt; tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\\\", \\\"parent\\\": \\\"exp019b_expert_sft_v3\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"train_loss_final\\\": 0.038, \\\"train_token_accuracy\\\": 0.988, \\\"train_steps\\\": 320, \\\"train_epochs\\\": 2, \\\"train_time_min\\\": 47.8, \\\"ragen_val_success\\\": 0.25, \\\"ragen_val_action_is_valid\\\": 0.875, \\\"eval_sft_fast_success\\\": 0, \\\"eval_sft_fast_format_ok\\\": 1, \\\"eval_sft_fast_action_is_valid\\\": 0.71, \\\"checkpoint_size_gb\\\": 3.3, \\\"ragen_val_success_16ep\\\": 0.0625, \\\"ragen_val_action_is_valid_16ep\\\": 0.6875}, \\\"notes\\\": \\\"D024: conclusion 降级为 negative (原 success)。16ep eval 数据: success=6.25%, action_is_valid=68.75%。原 4ep eval 的 25%/87.5% 为 unreliable_small_sample，不作为决策依据。Registry 无 inconclusive 选项，用 negative 代替。\\\"}, \\\"exp024_success_gated_grpo\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T06:03:10.298Z\\\", \\\"updated_at\\\": \\\"2026-05-15T06:04:06.454Z\\\", \\\"hypothesis\\\": \\\"Success-gated GRPO from exp021 checkpoint. D026 终止 RAGEN GRPO 后不再适用，success-gated 不解决 context 爆炸根因。关联 D027。\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"D027: Kill exp024 — D026 终止 RAGEN GRPO 后 success-gated 变体不再适用，不解决 context 爆炸根因。关联 D025/D026/D027。\\\"}, \\\"exp023c_grpo_serial\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T04:20:22.909Z\\\", \\\"updated_at\\\": \\\"2026-05-15T05:11:22.083Z\\\", \\\"hypothesis\\\": \\\"GRPO from exp021 RAGEN-format SFT checkpoint. Serial mode (parallel_friendly=false, max_workers=1) to avoid tatsu race. reward scale=10.0, kl_loss_coef=0.5, LR=5e-7, val env_groups=16, gpu_memory_utilization=0.6, 30 steps. Pass: success ≥ 25%, step time baseline comparison with exp022 (~208s/step).\\\", \\\"parent\\\": \\\"exp023_grpo_parallel\\\", \\\"metrics\\\": {\\\"val_step0_success\\\": 0.0625, \\\"val_step0_action_is_valid\\\": 0.6875, \\\"val_step0_episodes\\\": 16, \\\"train_step1_success\\\": 0.297, \\\"train_step1_action_is_valid\\\": 0.791, \\\"train_step1_entropy\\\": 0.0652, \\\"train_step1_pass16\\\": 0.75, \\\"train_step1_kl\\\": 0.000156, \\\"train_step8_success\\\": 0.234, \\\"train_step8_action_is_valid\\\": 0.779, \\\"train_step8_entropy\\\": 0.0555, \\\"train_step8_pass16\\\": 0.5, \\\"train_step8_kl\\\": 0.000475, \\\"steps_completed\\\": 8, \\\"steps_planned\\\": 30, \\\"step_time_seconds_start\\\": 240, \\\"step_time_seconds_end\\\": 365}, \\\"notes\\\": \\\"磁盘满崩溃 (step 9, /root/autodl-tmp 94% 233G/250G, OSError Errno 28)。但 8 步 metrics 趋势已显示退化：train success 29.7%→23.4%↓, pass@16 75%→50%↓, entropy 0.065→0.056↓, KL 0.00016→0.00048↑, step time 240s→365s↓。GRPO 未能在 SFT baseline 上产生改善，反而在退化。注意 step 0 val success=6.25% 与 train step 1 success=29.7% 差异大（val 用不同 game set + 16 episodes vs train 64 trajectories）。Checkpoint: global_step_5 only (save_freq=5, 第二次保存在 step 10 未到)。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp023_grpo_parallel\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T04:06:02.056Z\\\", \\\"updated_at\\\": \\\"2026-05-15T04:12:41.878Z\\\", \\\"hypothesis\\\": \\\"GRPO from exp021 RAGEN-format SFT checkpoint with 3 key fixes: (1) reward scale 10.0→1.0 (align with Self-Guide paper binary reward), (2) parallel rollout (max_workers=4, thread-safe env), (3) val env_groups=16 for reliable eval. kl_loss_coef=0.5, LR=5e-7, 30 steps. Pass: success ≥ 25% (maintain SFT baseline), step time < 200s (vs exp022 ~208s serial).\\\", \\\"parent\\\": \\\"exp022_grpo_from_sft_v4\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: textworld PDDL parser (tatsu) 在 val env reset 时崩溃 — tatsu.exceptions.FailedToken: expecting 'action', got template :: \\\\\\\"take {o} from {r}\\\\\\\". val env_groups=16 加载了更多 game files，触发了某个 game file 与当前 tatsu 版本不兼容的 PDDL grammar. | 已有成果: 无（val_before_train 阶段即崩溃，未开始训练） | 建议: 诊断具体哪个 game file 有问题，降低 val env_groups 或修复 game file/tatsu 兼容性\\\"}, \\\"exp022_grpo_from_sft_v4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-15T03:17:34.035Z\\\", \\\"updated_at\\\": \\\"2026-05-15T03:52:55.267Z\\\", \\\"hypothesis\\\": \\\"GRPO from exp021 RAGEN-format SFT checkpoint (25% RAGEN val success baseline). Sparse reward (won=10.0), LR=5e-7, kl_loss_coef=0.5 (5x stronger than exp020b to prevent entropy collapse), max_grad_norm=1.0, 30 steps, val env_groups=8. Pass: success ≥ 25% (maintain SFT baseline).\\\", \\\"parent\\\": \\\"exp021_ragen_sft_v4\\\", \\\"notes\\\": \\\"Step 0 val: success=12.5% (1/8), action_is_valid=48.75%。Step 1 完成后 kill。action_is_valid 远低于 SFT eval 结果（87.5%/68.75%），说明 RAGEN GRPO 框架中模型表现显著退化。kl_loss_coef=0.5, env_groups=8 均已确认生效。训练速度 ~208s/step。Checkpoint: global_step_1 可能已保存。\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"metrics\\\": {\\\"steps_completed\\\": 1, \\\"steps_planned\\\": 30, \\\"val_step0_success\\\": 0.125, \\\"val_step0_action_is_valid\\\": 0.4875, \\\"val_step0_action_is_effective\\\": 1, \\\"val_step0_reward_mean\\\": 1.25, \\\"val_step0_reward_best\\\": 6.61, \\\"val_step0_episodes\\\": 8, \\\"step_time_seconds\\\": 208}}, \\\"exp021_sft_ragen_format\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T22:35:48.559Z\\\", \\\"updated_at\\\": \\\"2026-05-15T02:11:46.204Z\\\", \\\"hypothesis\\\": \\\"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\\\", \\\"parent\\\": \\\"exp019b_expert_sft_v3\\\", \\\"notes\\\": \\\"被 exp021_ragen_sft_v4 取代。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp020d_grpo_from_sft\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T22:19:30.993Z\\\", \\\"updated_at\\\": \\\"2026-05-15T02:01:10.192Z\\\", \\\"hypothesis\\\": \\\"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.\\\", \\\"parent\\\": \\\"exp019b_expert_sft_v3\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\\\"}, \\\"exp020c_grpo_from_sft\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T22:15:37.659Z\\\", \\\"updated_at\\\": \\\"2026-05-15T02:01:08.768Z\\\", \\\"hypothesis\\\": \\\"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).\\\", \\\"parent\\\": \\\"exp019b_expert_sft_v3\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\\\"}, \\\"exp020b_grpo_from_sft\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T22:12:38.928Z\\\", \\\"updated_at\\\": \\\"2026-05-15T02:00:56.016Z\\\", \\\"hypothesis\\\": \\\"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink with \\\\\\\"qwen\\\\\\\" in path to pass response_mask assertion (exp020 crashed on this).\\\", \\\"parent\\\": \\\"exp019b_expert_sft_v3\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"steps_completed\\\": 22, \\\"steps_planned\\\": 30, \\\"hung_at_step\\\": 23, \\\"step1_train_success\\\": 0.1875, \\\"step10_train_success\\\": 0.1875, \\\"step20_train_success\\\": 0.125, \\\"step22_train_success\\\": 0.0469, \\\"val_success_step0\\\": 0, \\\"val_success_step20\\\": 0, \\\"entropy_initial\\\": 0.107, \\\"entropy_final\\\": 0.042, \\\"grad_norm_initial\\\": 2.78, \\\"grad_norm_step20\\\": 5.58, \\\"ppo_kl_final\\\": 0.00918, \\\"pass_at_16_step1\\\": 0.75, \\\"pass_at_16_step22\\\": 0.25, \\\"checkpoint_latest\\\": \\\"global_step_20\\\", \\\"training_status\\\": \\\"hung_at_step23_rollout\\\"}, \\\"notes\\\": \\\"Negative 结论：GRPO from SFT 导致策略坍缩。训练 22/30 步后卡死在 step 23 rollout（环境交互死锁，GPU 0% 利用率但显存仍占 40GB×2）。关键指标全线恶化：train success 18.75%→4.69%（远低于 SFT baseline 20%），val success 始终 0%，entropy 0.107→0.042（坍缩 61%），pass@16 从 75%降到 25%。GRPO 不仅未提升 SFT 性能，反而严重退化。根因分析：sparse reward（won=10.0）学习信号不足以维持 SFT 学到的 task knowledge，KL coef=0.1 不足以约束策略偏移。Checkpoint: /root/autodl-tmp/checkpoints/exp020b/global_step_20/\\\"}, \\\"exp020_grpo_from_sft\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T22:07:16.290Z\\\", \\\"updated_at\\\": \\\"2026-05-14T22:11:05.341Z\\\", \\\"hypothesis\\\": \\\"GRPO from exp019b SFT checkpoint (20% success baseline) can maintain or improve success rate. Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%.\\\", \\\"parent\\\": \\\"exp019b_expert_sft_v3\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"失败原因: AssertionError at train.py:137 — model_path=/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final 不含 \\\\\\\"qwen\\\\\\\" 字符串，enable_response_mask=true 断言失败。模型实际是 Qwen3-1.7B 微调 checkpoint，路径命名问题。error_type=infrastructure | 建议: 创建含 \\\\\\\"qwen\\\\\\\" 的 symlink 或添加 enable_response_mask=false override 后重提交\\\"}, \\\"exp019c_expert_sft_v3\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T21:03:02.685Z\\\", \\\"updated_at\\\": \\\"2026-05-14T21:05:37.494Z\\\", \\\"hypothesis\\\": \\\"Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。\\\", \\\"parent\\\": \\\"exp019b_expert_sft_v3\\\", \\\"notes\\\": \\\"废弃。submit_training_job 因 GPU 被占（exp019b nohup 进程仍在跑）EXIT_CODE=1 退出。实际训练由 exp019b 的 nohup 进程完成。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp019_expert_sft_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T16:38:05.515Z\\\", \\\"updated_at\\\": \\\"2026-05-14T17:11:09.024Z\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"D019 kill：move→put 替换方向错误。ALFWorld admissible_commands 包含 move X to Y，不含 put。用 put 替换的数据会使 action_is_valid 更差。改用原始 expert data（保留 move）+ admissible actions augmentation。\\\"}, \\\"exp019b_expert_sft_v2\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T16:49:30.246Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:49:30.246Z\\\"}, \\\"exp018_sft_grpo\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T15:43:08.545Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:45:33.314Z\\\", \\\"hypothesis\\\": \\\"Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），使 GRPO 有足够非零 reward group 产生有效梯度。LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, won=10.0, 无 bonus/penalty, GRPO 30 步。Pass: success ≥ 20%。\\\", \\\"parent\\\": \\\"exp017_expert_sft\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"D018 取消：exp017 eval 5% success 与 base 4.7% 差异太小，GRPO 大概率重蹈覆辙。等 exp019 v2 SFT（修复 move→put + admissible actions 数据增强）后再考虑 GRPO。\\\"}, \\\"exp017_expert_sft\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T15:36:28.291Z\\\", \\\"updated_at\\\": \\\"2026-05-14T16:36:17.637Z\\\", \\\"hypothesis\\\": \\\"Expert SFT: 用 PDDL expert trajectory 数据 SFT Qwen3-1.7B instruct 模型，提升 ALFWorld baseline success rate，为后续 GRPO 提供更好的冷启动点。LR=2e-5, 3 epochs, batch_size=4, grad_accum=4。Pass 标准: success ≥ 10%。\\\", \\\"parent\\\": \\\"exp008_sft\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_train_loss\\\": 0.1434, \\\"final_step_loss\\\": 0.04, \\\"final_token_accuracy\\\": 0.983, \\\"epochs\\\": 3, \\\"total_steps\\\": 462, \\\"training_time_min\\\": 26, \\\"data_count_train\\\": 2460, \\\"data_count_val\\\": 129, \\\"checkpoint_size_gb\\\": 3.44, \\\"eval_success_rate\\\": 0.05, \\\"eval_success\\\": \\\"1/20\\\", \\\"eval_action_is_valid\\\": 0.638, \\\"eval_format_ok\\\": 0.75, \\\"eval_avg_steps\\\": 22, \\\"eval_time_s\\\": 149.6, \\\"eval_per_task\\\": {\\\"put\\\": \\\"0/10\\\", \\\"clean\\\": \\\"0/4\\\", \\\"cool\\\": \\\"1/3\\\", \\\"heat\\\": \\\"0/2\\\", \\\"examine\\\": \\\"0/1\\\"}, \\\"eval_parse_failures\\\": \\\"5/20 episodes (EP 7/12/16/17/18)\\\"}, \\\"notes\\\": \\\"训练成功完成。Expert PDDL trajectory 2460 条 SFT Qwen3-1.7B，3 epochs 462 steps 26 min。Final loss=0.1434。Checkpoint: /root/autodl-tmp/checkpoints/exp017_expert_sft/final/ (3.44GB)。\\\\n\\\\nEval 结果（20 episodes, vLLM 推理, max_steps=30）：success=5% (1/20), action_is_valid=63.8%, format_ok=75%。唯一成功是 1 个 cool 任务（EP 8, 15 步）。5/20 episodes parse 失败（1 步即退出）。put 任务 0/10 全失败。\\\\n\\\\n对比 exp008_sft（1200 条普通 SFT）：action_is_valid 90%→63.8%（下降！）, format_ok 100%→75%（下降！）, success 0%→5%（略升）。Expert data SFT 提升了 success 但 format/valid 反而退步，可能因为 expert trajectory 格式与 RAGEN 的 &lt;think>/&lt;answer> 格式不完全匹配。\\\"}, \\\"exp016\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T13:44:58.883Z\\\", \\\"updated_at\\\": \\\"2026-05-14T15:36:27.432Z\\\", \\\"hypothesis\\\": \\\"LR 折中方案：LR=5e-7（exp012b 1e-6 collapse vs exp015 1e-7 零梯度的中间值）。kl_loss_coef=0.1, max_grad_norm=1.0 保持。纯 sparse reward（won=10.0，无 bonus，无 format_penalty）。从 exp015/global_step_5 checkpoint 恢复，GRPO 30 步。\\\", \\\"parent\\\": \\\"exp015\\\", \\\"metrics\\\": {\\\"step\\\": 12, \\\"total_steps\\\": 30, \\\"elapsed_min\\\": 51, \\\"step6_success\\\": 0, \\\"step6_action_is_valid\\\": 0.521, \\\"step6_pg_loss\\\": 0, \\\"step6_grad_norm\\\": 0.841, \\\"step7_success\\\": 0.047, \\\"step7_pass_at16\\\": 0.5, \\\"step7_action_is_valid\\\": 0.655, \\\"step10_success\\\": 0, \\\"step10_action_is_valid\\\": 0.664, \\\"step10_pg_loss\\\": 0, \\\"step10_grad_norm\\\": 0.856, \\\"step10_entropy\\\": 0.1046, \\\"step10_ppo_kl\\\": -9.1e-05, \\\"all_raw_rewards\\\": 0, \\\"all_advantages\\\": 0, \\\"all_returns\\\": 0, \\\"reward_signal\\\": \\\"BROKEN — success episodes get reward=0\\\", \\\"action_is_valid_trend\\\": \\\"52.1%→65.5%→66.4%\\\", \\\"manager_invalid_action_trend\\\": \\\"13.5%→11.2%→9.6%\\\"}, \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"D015 kill。训练 12 步，pg_loss 恒为 0。原因：base success ~4.7%（仅 val，train temperature=1.0 下接近 0%），纯 sparse reward 下 GRPO 无有效学习信号。raw_reward=0 是日志 artifact（info dict 缺 raw_reward 字段），实际训练 reward pipeline 正常（critic/score 正确传递，step 7 score/mean=0.46875=3/64×10.0）。NaiveRewardManager 是 pass-through，不覆盖 env reward。LR=5e-7 本身无问题，根因是 sparse reward 冷启动。\\\"}, \\\"exp015\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T12:48:38.065Z\\\", \\\"updated_at\\\": \\\"2026-05-14T13:44:57.940Z\\\", \\\"hypothesis\\\": \\\"Sparse GRPO + 训练稳定性修复。纯 sparse reward（won=10.0，无 valid_action_bonus，无 format_penalty）。针对 exp012b 的 step 7 catastrophic collapse（grad_norm 1.48→0.094），三项修复：LR 1e-7（降 10 倍防单步更新过激）、kl_loss_coef 0.1（增 10 倍约束策略偏移）、max_grad_norm=1.0（梯度裁剪）。从 exp008 step 5 checkpoint 恢复，GRPO 30 步。\\\", \\\"parent\\\": \\\"exp012b\\\", \\\"notes\\\": \\\"D014 kill。Steps 3-5 连续零梯度（pg_loss=0, grad_norm~0），LR=1e-7 过保守导致无有效学习。Step 0 val: action_is_valid=85.8%, success=0%。训练稳定性修复验证成功（无 catastrophic collapse），但学习率不足以产生有意义的 policy update。Checkpoint: global_step_5 已保存，供 exp016 恢复。\\\", \\\"metrics\\\": {\\\"step\\\": 1, \\\"total_steps\\\": 30, \\\"val_step0_success\\\": 0, \\\"val_step0_action_is_valid\\\": 0.858, \\\"val_step0_pass_at1\\\": 0, \\\"val_step0_episodic_return\\\": 0, \\\"val_step0_response_length\\\": 2797.5, \\\"val_train_transition\\\": \\\"passed\\\", \\\"estimated_total_time_min\\\": 163, \\\"time_per_step_min\\\": 5.6}, \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp014b\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T12:45:27.876Z\\\", \\\"updated_at\\\": \\\"2026-05-14T12:48:37.433Z\\\", \\\"hypothesis\\\": \\\"极低 Dense Reward: valid_action_bonus=0.01（1:1000 比例），测试极弱 bonus 能否防 collapse 又不引发 gaming。如果 bonus 弱到不影响 GRPO reward ranking，模型不会被诱导走捷径。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\\\", \\\"parent\\\": \\\"exp013f\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"D013 撤销：Director 修订决策，改为 exp015。exp014b 等 exp015 结果后再决定。\\\"}, \\\"exp014a\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T12:45:27.347Z\\\", \\\"updated_at\\\": \\\"2026-05-14T12:48:35.102Z\\\", \\\"hypothesis\\\": \\\"Success-Gated Dense Reward: valid_action_bonus=0.15 只在 group 内至少一条 trajectory success 时才给。消除 reward gaming 的独立最大化路径——没有 success 就没有 bonus，模型必须探索 success。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\\\", \\\"parent\\\": \\\"exp013f\\\", \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"D013 撤销：Director 修订决策，success-gated bonus 有 bootstrap 问题（初始 success=0 时 bonus 永远为 0，退化为 sparse reward），改为 exp015 纯 sparse GRPO + 训练稳定性修复。\\\"}, \\\"exp014c\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"created_at\\\": \\\"2026-05-14T12:45:21.231Z\\\", \\\"updated_at\\\": \\\"2026-05-14T12:45:25.025Z\\\", \\\"hypothesis\\\": \\\"Success-gated valid_action_bonus：bonus 仅在 episode 成功时累加到 reward，消除独立最大化路径。valid_action_bonus=0.15, success_reward=10.0。解决 exp013f reward gaming（unconditional bonus 导致 agent 放弃 success 追求 valid action）。从 step 5 checkpoint 恢复 GRPO 30 步。\\\", \\\"parent\\\": \\\"exp013f\\\"}, \\\"exp013e\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T09:02:52.837Z\\\", \\\"updated_at\\\": \\\"2026-05-14T09:21:08.911Z\\\", \\\"hypothesis\\\": \\\"exp013d 基础设施修复重试。Ray object_store_memory 改用 Hydra config override (ray_kwargs.ray_init.object_store_memory=32212254720) 替代无效的环境变量。其余同 exp013d: dense reward shaping (valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0), env_groups=4, 从 step 5 checkpoint 恢复。\\\", \\\"parent\\\": \\\"exp013d\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"ActorUnavailableError: RPC error: Socket closed rpc_code: 14。validation step 5 完成后向 training step 6 过渡时崩溃。诊断排除: cgroup OOM (oom_kill=0)、系统 OOM (dmesg 无记录)、CUDA OOM (无日志)、磁盘满 (118GB剩余)。Ray worker 日志被 ray stop --force 清除，最可能原因: vLLM worker 在 val→train 切换时的内存峰值或内部错误。object_store_memory=30GB 设置正确(train.py:203)。validation 指标: success=0, action_is_valid=0.656, reward_mean=2.953, reward_std=1.608。结论: 瞬态崩溃，可安全重提交。建议加 HYDRA_FULL_ERROR=1。\\\"}, \\\"exp013d\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:34:37.036Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:52:25.371Z\\\", \\\"hypothesis\\\": \\\"exp013b/c 内存修复重试。Dense reward shaping (valid_action_bonus=0.15) 已验证有效 (reward_std=1.608>0)。修复: env_groups 8→4 (64并发, 峰值~158GB < 220GB cgroup限制) + RAY_object_store_memory=30GB。\\\", \\\"parent\\\": \\\"exp013c\\\", \\\"notes\\\": \\\"RAY_object_store_memory env var 未生效，Ray 仍分配 70.36GB object store（默认值）。env_groups=4 生效但不够。Raylet 被 cgroup OOM killer SIGKILL。修复: 用 Hydra config override ray_kwargs.ray_init.object_store_memory=32212254720 显式传给 ray.init()。\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp013c\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:30:44.623Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:34:10.517Z\\\", \\\"hypothesis\\\": \\\"exp013b 基础设施重试。Dense reward shaping (valid_action_bonus=0.15 + success=10.0) 已验证有效 (reward_std=1.608>0)。exp013b 因 OOM/Ray 崩溃，非算法问题。\\\", \\\"parent\\\": \\\"exp013b\\\", \\\"notes\\\": \\\"预防性kill。诊断确认 exp013b 崩溃根因: cgroup 内存限制 220GB, Ray object_store 70GB + memory 164GB = 234GB 超限。128并发ALFWorld游戏(8 env_groups × 16 group_size)在 step 6 rollout 触发 Plasma mmap ENOMEM。exp013c 同配置会重现。修复: env_groups 8→4 + RAY_object_store_memory=30GB。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp013b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-14T08:15:44.247Z\\\", \\\"updated_at\\\": \\\"2026-05-14T08:27:21.850Z\\\", \\\"hypothesis\\\": \\\"Dense reward shaping: valid_action_bonus=0.15 per valid action + success_reward=10.0 + kl_loss_coef=0.01。每步有效动作获得 0.15 奖励提供持续 GRPO 学习信号（30步累计上限4.5 vs 终局10.0），KL 约束防止 policy 过激更新。format_penalty=0，从 step 5 checkpoint 恢复 GRPO 30 步。\\\", \\\"parent\\\": \\\"exp013\\\", \\\"notes\\\": \\\"Dense reward shaping 有效性已确认：val reward_mean=2.953, reward_std=1.608 (>0)。崩溃是基础设施问题（OOM/Ray），非算法问题。清理后重试。超参: valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0, format_penalty=0, group_size=16。\\\", \\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 50, \\\"total\\\": 69, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1919}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"hsweep_h20_seed1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-18T18:04:42.684Z\", \"updated_at\": \"2026-05-18T19:14:40.086Z\", \"hypothesis\": \"h=20 with step_independent generation provides 20-step observation windows. Key data point for fig5 cliff figure: with h=10 and h=5 both collapsing, h=20 tests whether 20 steps of context is sufficient for recovery. If h=20 recovers (val > 0% at step 5+), the cliff is between h=10 and h=20. If still collapsed, the minimum viable context window is larger than 20 steps.\", \"parent\": \"hsweep_h10_seed1\", \"notes\": \"诊断中: worker_diagnose_hsweep_h20_seed1_20260518T184044 正在 SSH 深查失败原因。日志尾部无 Traceback，疑似系统级 kill (OOM/磁盘)。\"}, \"hsweep_h10_seed1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T17:30:46.964Z\", \"updated_at\": \"2026-05-18T19:09:46.781Z\", \"hypothesis\": \"h=10 with step_independent generation provides 10-step observation windows. Key data point for fig5 cliff figure: if h=10 shows recovery (val > 0%), the cliff is between h=5 and h=10. If still collapsed, cliff is between h=10 and full context (h=28).\", \"parent\": \"hsweep_h2_seed1\", \"notes\": \"Director 批准临时 kill（刚启动几分钟，无进度损失）以释放 bjb1 cuda:0,1 跑 exp029 + hsweep_h2_seed2 双 reeval。Reeval 完成后重启。原由 auto_next_hsweep.sh 自动启动，未经正式审批。\"}, \"factorial_h2_episodeadv_seed2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-18T04:48:02.228Z\", \"updated_at\": \"2026-05-18T18:25:27.297Z\", \"hypothesis\": \"Replicate factorial experiment (step-independent + episode-level advantage) with different seed to confirm that sign misattribution elimination is robust, not single-seed artifact. Same config, different seed, 15 steps.\", \"parent\": \"factorial_h2_episodeadv_seed1\"}, \"exp029_episode_level_seed2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:48:01.826Z\", \"updated_at\": \"2026-05-18T18:25:16.249Z\", \"hypothesis\": \"Replicate exp029 episode-level result (23.88% OOD) with different seed to confirm statistical robustness. P0 priority: core positive claim built on single seed is desk-reject risk. Same SFT checkpoint, same config, seed=43, 15 steps, AlfworldSG_OOD 134 tasks eval.\", \"parent\": \"exp029_episode_level\", \"conclusion\": \"killed\", \"notes\": \"Director 止损 kill。bjb1 累计 10+ 次失败。step 15 val=21.875% (32 tasks)，数据保留在 /root/autodl-tmp/checkpoints/exp029-seed2/。计划转移到 westd cuda:0,1 继续（factorial 完成后）。\"}, \"gsweep_g100_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:58.033Z\", \"updated_at\": \"2026-05-18T17:36:39.529Z\", \"hypothesis\": \"γ=1.0 (no discount) tests whether collapse in h=5 is caused by sign misattribution from magnitude decay. If γ=1.0 also collapses, sign misattribution is not solely from discount-induced magnitude decay.\", \"parent\": \"gsweep_g095_h5_seed1\", \"conclusion\": \"negative\", \"metrics\": {\"conclusion_reason\": \"collapsed, γ=1.0 also collapses confirming sign misattribution not solely from magnitude decay\"}}, \"gsweep_g095_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:55.994Z\", \"updated_at\": \"2026-05-18T13:11:09.941Z\", \"hypothesis\": \"γ=0.95 with h=5 is the control condition matching hsweep_h5. Early windows retain γ^9 ≈ 0.95^9 ≈ 63% of terminal return. Expected to reproduce h5 behavior from h-sweep.\", \"parent\": \"hsweep_h2_seed1\", \"conclusion\": \"negative\", \"metrics\": {\"val_success_step5\": 0, \"conclusion_reason\": \"collapsed at step 5, val=0%\"}}, \"factorial_h2_episodeadv_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T18:17:23.327Z\", \"updated_at\": \"2026-05-18T10:22:36.071Z\", \"hypothesis\": \"Step_independent generation (h=2) with episode-level advantage eliminates sign misattribution while preserving truncated-context inference. If success >> h=2 step-level (0%), information loss alone does not cause collapse — sign misattribution is the primary driver. If success ≈ 0%, information loss is sufficient to cause collapse regardless of advantage computation. This is the key factorial experiment separating the two mechanisms.\", \"parent\": \"hsweep_h2_seed1\", \"metrics\": {\"completed_steps\": \"15/15\", \"wandb_run_id\": \"6liw7fm1\", \"val_step5\": {\"success\": 0.0597, \"dataset\": \"AlfworldOOD_134tasks\"}, \"val_step15\": {\"success\": 0.0075}, \"kl_loss_trajectory\": {\"step1\": 0.238, \"step5\": 0.735, \"step10\": 1.029, \"step15\": 2.845}, \"ppo_kl_range\": \"0.025-0.096\", \"best_checkpoint\": \"global_step_5\", \"best_val_success\": 0.0597, \"train_step1\": {\"success\": 0.203, \"pass_at_8\": 0.688}, \"train_step6\": {\"success\": 0.258, \"pass_at_8\": 0.813}, \"checkpoint_paths\": {\"step5\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_5/\", \"step10\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_10/\", \"step15\": \"/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_15/\"}, \"exit_cause\": \"W&B atexit BrokenPipeError (false positive)\", \"kl_issue\": \"kl_loss_coef=0.01 too low, policy drifted after step 5\", \"status_note\": \"COMPLETED. Best val OOD 5.97% at step 5. Degraded to 0.75% by step 15 due to KL drift. Sign misattribution elimination confirmed: 5.97% vs 0% (step-level h=2).\"}, \"notes\": \"W&B 深度分析确认：sign misattribution 是 collapse 的 primary driver。关键证据：step 3→4 hsweep action_valid 91.3%→43.1% (catastrophic collapse) vs factorial 保�� 79-85% (无崩溃)。V-shaped recovery (20.3%→3.1%→15.63%) 是探索期波动非不可逆退化。3-cell 贡献：sign misattribution ~6pp (0%→5.97% val), information loss ~22pp (5.97%→28.1% val)。Sign misattribution pp 贡献较小但是 catastrophic collapse 的质变 trigger。\", \"conclusion\": \"success\"}, \"gsweep_g080_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:53.634Z\", \"updated_at\": \"2026-05-18T09:35:23.404Z\", \"hypothesis\": \"γ=0.8 with h=5 represents an intermediate decay rate where early windows retain γ^9 ≈ 0.8^9 ≈ 13% of terminal return, potentially showing delayed but still present collapse compared to γ=0.95 (39%).\", \"parent\": \"hsweep_h2_seed1\", \"metrics\": {\"step5_val_success\": \"3.125%\", \"step5_entropy\": 0.185, \"subsequent_steps\": \"all 0%\", \"conclusion_note\": \"Complete collapse confirmed. γ=0.80 with h=5 shows catastrophic failure — killed early by Director as no new information expected. Supports hypothesis that lower gamma accelerates collapse.\"}, \"conclusion\": \"negative\"}, \"hsweep_h2_seed2_reeval_ood\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:12:03.656Z\", \"updated_at\": \"2026-05-18T05:13:33.875Z\", \"hypothesis\": \"Evaluate hsweep_h2_seed2 checkpoint (step 15) on OOD 134 tasks to get comparable metric with exp029 reeval (23.88%). If val success remains low (~9% in-distribution), confirms collapse is real even with late recovery.\", \"parent\": \"hsweep_h2_seed2\", \"metrics\": {\"success\": 0.0373, \"action_is_valid\": 0.994, \"action_is_effective\": 1, \"pass_at_1\": 0.0373, \"num_actions\": 48.53, \"response_length\": 8501, \"dataset\": \"AlfworldSG_OOD_134tasks\", \"date\": \"2026-05-18\", \"note\": \"Valid actions (99.4%) but cannot complete tasks - generates long ineffective sequences\"}, \"conclusion\": \"success\"}, \"exp029_episode_level\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:49:53.280Z\", \"updated_at\": \"2026-05-18T04:11:39.305Z\", \"hypothesis\": \"Episode-level 训练（context_window_mode: full）解决 step_independent h=2 的信用分配缺陷，模型能学到跨步规划策略，val success 不再停滞于 baseline。\", \"parent\": \"exp028c_selfguide_recipe\", \"notes\": \"Director 决策 early-stop at step 15（val success 28.125%, pass@8=92.9%）释放 GPU 给 h-sweep。MVP 已通过（step 5 val=25%, 2x baseline）。Episode-level 训练假设确认：从 12.5% baseline 提升到 28.125%，而 step-independent 崩塌到 0%。Checkpoint: global_step_15。\", \"conclusion\": \"success\", \"metrics\": {\"reeval_ood_134tasks\": {\"success\": 0.2388, \"action_is_valid\": 0.5683, \"action_is_effective\": 0.916, \"manager_invalid_action\": 0.0839, \"reward_mean\": 2.388, \"best_at_8\": 8.88, \"dataset\": \"AlfworldSG_OOD_134tasks\", \"date\": \"2026-05-18\"}}}, \"gsweep_g050_h5_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:56:51.277Z\", \"updated_at\": \"2026-05-18T02:56:21.234Z\", \"hypothesis\": \"γ=0.5 with h=5 will show accelerated collapse compared to default γ=0.95, because γ^k decay compounds: early windows receive only γ^(N-1) ≈ 0.5^9 ≈ 0.2% of terminal return, making sign misattribution maximally severe.\", \"parent\": \"hsweep_h2_seed1\", \"notes\": \"Director 批准 early kill (step 12/15)。Hypothesis 完全确认：γ=0.5 加速 collapse，从 step 1 起 train success 基本为 0%，val step 5/10 全零，KL step 8 spike 到 0.209。step 10 checkpoint 已保存。数据足够用于论文 gamma sweep figure。Watchdog 预期自动启动 g080。\", \"metrics\": {\"current_step\": \"12/15\", \"train_success_collapsed_at\": \"step 1\", \"train_success_all_steps\": \"0-2.3% (effectively 0%)\", \"val_step0\": {\"success\": 0.094}, \"val_step5\": {\"success\": 0, \"reward\": 0}, \"val_step10\": {\"success\": 0, \"reward\": 0, \"response_length\": 1412}, \"kl_sequence\": [0.019, 0.025, 0.018, 0.014, 0.01, 0.009, 0.009, 0.209, 0.018], \"kl_spike_step8\": 0.209, \"checkpoint\": \"global_step_10\", \"eta\": \"~5h from 02:46 UTC\", \"status_note\": \"COMPLETELY COLLAPSED. Train success 0% from step 1. KL spike 20x at step 8. Val all zeros. Remaining 3 steps waste GPU. Recommend early kill.\"}, \"conclusion\": \"killed\"}, \"hsweep_h2_seed2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:37:14.817Z\", \"updated_at\": \"2026-05-18T02:55:38.705Z\", \"hypothesis\": \"h=2 seed 2 replicates seed 1 catastrophic collapse (step 3-4 onset, 0% by step 9+), confirming collapse is robust not single-run artifact. Additionally LOG_PER_SAMPLE_ADV=1 collects per-window advantage data for plan_004 sign misattribution empirical verification.\", \"parent\": \"hsweep_h2_seed1\", \"metrics\": {\"current_step\": \"15/15\", \"completed\": true, \"val_step5\": {\"success\": 0}, \"val_step10\": {\"success\": 0}, \"val_step15\": {\"success\": 0.09375}, \"train_step14\": {\"success\": 0.2656, \"pass_at_8\": 0.6875}, \"train_step15\": {\"success\": 0.2812, \"pass_at_8\": 0.625, \"entropy\": 0.401, \"ppo_kl\": 0.006}, \"train_success_peak\": {\"step\": 15, \"value\": 0.2812}, \"adv_log_lines\": 3000, \"adv_episodes\": {\"total\": 128, \"success\": 65, \"fail\": 63}, \"adv_analysis\": {\"sign_outcome_agreement\": 0.5207, \"point_biserial_r\": 0.068, \"p_adv_pos_given_success\": 0.3706, \"p_adv_pos_given_failure\": 0.306, \"magnitude_decay_gamma\": 0.9426, \"distribution_overlap\": 0.878, \"verdict\": \"52% agreement confirms advantage signal nearly uninformative about episode outcome = sign misattribution\"}, \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/global_step_15/\", \"checkpoint_warning\": \"seed2 overwrote seed1 step15 checkpoint in same directory\", \"status_note\": \"COMPLETED 15/15. Late recovery at step 14-15 (train 26-28%). Val 9.375% on 16 in-dist tasks. ADV: 52% sign agreement = near-random.\"}, \"conclusion\": \"success\", \"notes\": \"15/15 步正常完成 + final val。Hypothesis NOT confirmed：seed2 未复现 seed1 的 catastrophic collapse。关键差异：(1) action_is_valid 始终 88-100%（seed1 崩至 0.06%）(2) val step 15 恢复到 9.375%（seed1 终值 0%）(3) train step 15 success=28.1%（seed1 终值 0%）。Val step 0/5/10 确实为 0%，说明 h=2 确实造成学习困难，但不是 seed1 那样的不可逆 catastrophic collapse。Collapse 行为是 seed-dependent 的，不是 robust finding。ADV log 3000 行可用于 sign misattribution 分析。注意：checkpoint 写入 hsweep-h2/ 目录（与 seed1 共享，global_step_15 被覆盖）。\"}, \"gae_baseline_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:05:31.533Z\", \"updated_at\": \"2026-05-17T19:19:48.391Z\", \"hypothesis\": \"REINFORCE++ (running-mean baseline, no critic) provides modest improvement over episode-level GRPO due to per-token advantage normalization. Fallback from GAE due to TRL 1.1.0 removing AutoModelForCausalLMWithValueHead (critic head unavailable).\", \"parent\": \"exp029_episode_level\", \"metrics\": {\"wandb_run_id\": \"dt79qyd9\", \"pid\": 40267, \"val_step0\": {\"success\": 0.0625, \"action_is_valid\": 0.7796}, \"val_step5\": {\"success\": 0.125, \"action_is_valid\": 0.6926}, \"val_step10\": {\"success\": 0.125, \"pass_at_1\": 0.125, \"reward_mean\": 1.25}, \"train_step9\": {\"success\": 0.0313, \"action_is_valid\": 0.6033, \"pass_at_8\": 0.25}, \"server\": \"westd-47453\", \"gpu\": \"cuda:0,1\", \"method\": \"reinforce_plus_plus\", \"fallback_reason\": \"TRL 1.1.0 removed AutoModelForCausalLMWithValueHead\", \"current_step\": \"11/15\"}, \"notes\": \"实际运行 REINFORCE++ (adv_estimator=reinforce_plus_plus_baseline)，非 GAE。GAE 因 TRL 1.1.0 移除 AutoModelForCausalLMWithValueHead 不可用 (D060)。\", \"conclusion\": \"killed\"}, \"hsweep_h2_seed1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T04:37:11.061Z\", \"updated_at\": \"2026-05-17T14:36:40.246Z\", \"hypothesis\": \"Step-independent GRPO with h=2 (minimal context, N=25 windows per episode) will catastrophically collapse due to advantage sign misattribution: early windows retain only γ^24=0.95^24≈29% of terminal return, and all windows in failed episodes receive undifferentiated negative advantage regardless of action quality\", \"parent\": \"exp029_episode_level\", \"metrics\": {\"train_step\": 15, \"total_steps\": 15, \"wandb_run_id\": \"7o9bjszm\", \"step1\": {\"success\": 0.1875, \"pass_at_8\": 0.4375, \"invalid_action\": 0.027}, \"step2\": {\"success\": 0.1484, \"pass_at_8\": 0.5, \"invalid_action\": 0.02}, \"step3\": {\"success\": 0.1875, \"pass_at_8\": 0.625, \"invalid_action\": 0.028}, \"step4\": {\"success\": 0.0547, \"pass_at_8\": 0.25, \"invalid_action\": 0.264}, \"step5\": {\"success\": 0.0156, \"pass_at_8\": 0.0625, \"invalid_action\": 0.369}, \"step6\": {\"success\": 0.0313, \"pass_at_8\": 0.25, \"invalid_action\": 0.471}, \"step7\": {\"success\": 0.0469, \"pass_at_8\": 0.1875, \"invalid_action\": 0.502}, \"step8\": {\"success\": 0.0156, \"pass_at_8\": 0.125, \"invalid_action\": 0.542}, \"step9\": {\"success\": 0, \"pass_at_8\": 0, \"invalid_action\": 0.641}, \"step10\": {\"success\": 0.0234}, \"step11_15\": {\"success\": 0, \"invalid_action\": 0.972}, \"val_final\": {\"success\": 0, \"invalid_action\": 0.999, \"action_is_valid\": 0.0006}, \"checkpoint\": \"global_step_5,10,15\", \"checkpoint_path\": \"/root/autodl-tmp/checkpoints/hsweep-h2/\", \"log_path\": \"~/runs/cost-verify-agent-rl/hsweep_h2_s1.log\", \"gpu_util\": \"95-100%\", \"collapse_onset\": \"step3→step4\", \"elapsed_hours\": 10.04, \"step15_entropy\": 0.342, \"step15_kl_loss\": 0.777, \"step15_grad_norm\": 1.611, \"auto_next_triggered\": true, \"seed2_pid\": 945877, \"seed2_wandb\": \"jhwyg4tc\"}, \"conclusion\": \"success\", \"notes\": \"15 steps 完成。Hypothesis 验证：h=2 step_independent 确实灾难性崩溃（step 3→4 onset, step 9 归零, step 11-15 持续为零）。Final val: success=0%, invalid_action=99.9%, action_is_valid=0.06%。模型彻底退化到几乎只输出无效动作。\"}, \"exp025c\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T08:09:29.393Z\", \"updated_at\": \"2026-05-17T10:53:00.425Z\", \"notes\": \"项目已 pivot 到 h-sweep + sign misattribution 诊断方向（D054/D057）。exp025c 属于 pivot 前的实验设计，不在当前 experiment_plan.yaml 中，与论文核心 claims 无关联。GPU 资源优先用于 h-sweep 和 GAE baseline。\", \"conclusion\": \"killed\"}, \"exp026_step_independent_grpo\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:34:33.675Z\", \"updated_at\": \"2026-05-17T03:14:31.315Z\", \"notes\": \"exp026 negative: step-independent GRPO 在 step 2 达峰 train success=32.81% 后连续崩塌至 step 4 的 0%。Step 5 val eval 未完成即被 kill（val 生成阶段启动后进程被终止），无法对比 step 0 vs step 5 val。无 checkpoint（save_freq=25 未触发）。根因分析（Reviewer）：sparse reward + 小 env_groups(4=64 rollouts) 导致全零 batch 概率高，advantage 只有负信号把策略推回 reference。action_is_valid 在 step 2-4 保持 ~72% 但 success 归零，模型学会了\\\"看起来合理\\\"的 action 但丧失任务完成能力。教训：(1) save_freq 必须 ≤5 捕获早期峰值 (2) env_groups 需 ≥8 降低全零 batch 概率 (3) WANDB_MODE=disabled 导致 cron 误判 (4) cron 应监控 Ray TaskRunner PID 而非 shell wrapper PID。\", \"metrics\": {\"val_before_train_success\": 0.0625, \"val_before_train_action_is_valid\": 0.631, \"val_before_train_episodes\": 16, \"train_step1_success\": 0.2188, \"train_step1_action_is_valid\": 0.686, \"train_step1_entropy\": 0.2672, \"train_step1_kl_loss\": 0.1797, \"train_step1_grad_norm\": 14.43, \"train_step1_reward_mean\": 1.218, \"train_step1_pass_at_16\": 1, \"train_step2_success\": 0.3281, \"train_step2_action_is_valid\": 0.603, \"train_step2_entropy\": 0.317, \"train_step2_kl_loss\": 0.0974, \"train_step2_grad_norm\": 15.62, \"train_step2_reward_mean\": 1.62, \"train_step2_pass_at_16\": 1, \"train_step3_success\": 0.1719, \"train_step3_action_is_valid\": 0.641, \"train_step3_entropy\": 0.387, \"train_step3_kl_loss\": 0.2617, \"train_step3_grad_norm\": 15.65, \"train_step3_reward_mean\": 1.079, \"train_step3_pass_at_16\": 0.75, \"train_step4_success\": 0, \"train_step4_action_is_valid\": 0.717, \"train_step4_entropy\": 0.387, \"train_step4_kl_loss\": 0.054, \"train_step4_grad_norm\": 13.81, \"train_step4_pass_at_16\": 0}, \"conclusion\": \"negative\", \"hypothesis\": \"Step-independent GRPO（每步独立优化、不建模跨步依赖）能在ALFWorld多步任务中学到有效策略，因为每步的local reward信号足以引导正确行为选择\", \"parent\": \"exp021_ragen_sft_v4\"}, \"exp019b_expert_sft_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:30:00.085Z\", \"updated_at\": \"2026-05-17T03:14:30.703Z\", \"hypothesis\": \"Two-stage Expert SFT: exp008_sft checkpoint + v3 data (original move actions + admissible actions). LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096. Pass: success>=10%, format_ok>=90%, action_is_valid>=85%.\", \"notes\": \"训练成功完成 320/320 steps (2 epochs, 47:49)。Cron 多次误报 failed（监控错误 PID / 无法区分正常退出与崩溃）。Checkpoint: /root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.0718, \"eval_loss\": 0.0428, \"eval_mean_token_accuracy\": 0.9869, \"train_runtime_seconds\": 2869.8, \"steps\": 320, \"epochs\": 2, \"eval_success_rate\": 0.2, \"eval_format_ok\": 1, \"eval_action_is_valid\": 0.8533, \"eval_episodes\": 20, \"eval_avg_steps\": 25.4, \"eval_time_seconds\": 146}, \"parent\": \"exp008_sft\"}, \"exp013f\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:21:46.227Z\", \"updated_at\": \"2026-05-17T03:14:29.725Z\", \"hypothesis\": \"Dense reward shaping(valid_action_bonus=0.15)为全失败GRPO group提供非零方差梯度信号，使模型在避免梯度collapse的同时学到task success而非仅优化bonus\", \"parent\": \"exp013e\", \"metrics\": {\"step\": 30, \"total_steps\": 30, \"completed\": true, \"exit_code\": 0, \"training_time_s\": 10683, \"step6_success\": 0.0156, \"step7_success\": 0.0781, \"step10_success\": 0, \"step17_success\": 0.0156, \"final_val_success\": 0, \"final_val_action_is_valid\": 0.975, \"final_val_action_is_effective\": 1, \"final_val_reward_mean_at4\": 4.388, \"final_val_reward_std_at4\": 0.195, \"final_val_reward_best_at4\": 4.499, \"final_val_pass_at1\": 0, \"action_is_valid_trend\": \"60%→65.9%→77.1%→97.5%\", \"success_trend\": \"0%→1.56%→7.81%→0%→1.56%→0%\", \"grad_norm_range\": \"1.7-2.9 (no collapse)\", \"conclusion_reason\": \"Dense reward gaming: model optimized valid_action_bonus (action_is_valid 60%→97.5%) but success stayed 0%. Reward ratio 1:67 too weak — cumulative valid_action_bonus (4.5) dominated learning signal vs sparse success_reward (10.0). GRPO collapse prevented but task completion not learned.\"}, \"conclusion\": \"negative\", \"notes\": \"30/30 步完成，EXIT_CODE=0。Dense reward shaping 成功解决了 exp012b 的 catastrophic collapse（grad_norm 稳定 1.7-2.9），但产生 reward gaming：模型最大化 valid_action_bonus 而非 success_reward。action_is_valid 60%→97.5%（学会合法命令），success 始终 0-8%（未学会完成任务）。final_val reward/mean@4=4.388 ≈ 29 valid_actions × 0.15，几乎无 success_reward 贡献。Disk warning: /root/autodl-tmp 95% full (4.1GB remaining)。Ray log 备份失败（脚本执行时 session 已清理）。Checkpoint: global_step_30 已保存。\"}, \"exp028_prereq_zeroshot\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:11:06.120Z\", \"updated_at\": \"2026-05-17T03:14:28.598Z\", \"conclusion\": \"negative\", \"wandb_run_id\": \"qdvv09da\", \"metrics\": {\"success\": 0, \"action_is_valid\": 0.75, \"num_actions\": 50, \"pass_at_1\": 0, \"response_length\": 75.07}, \"notes\": \"Qwen3-1.7B（本身就是 instruct 模型）零样本 ALFWorld eval = 0% success。证明 SFT 从 0%→6.25% 是有益的，D044 '不做SFT' 假设不成立。W&B run: qdvv09da\", \"hypothesis\": \"Qwen3-1.7B base模型具备ALFWorld零样本能力(success>0%)，无需SFT即可作为GRPO冷启动点——如成立则SFT引入的分布偏差可能反而有害\"}, \"exp008_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T03:04:47.496Z\", \"updated_at\": \"2026-05-17T03:14:25.946Z\", \"notes\": \"SFT 转换脚本修复后重跑成功。Eval 方法: 独立脚本 eval_sft_model.py, 4 episodes (seed=0,1,2,3), HF generate() + AlfredTXTEnv, cuda:1, max_steps=50。action_is_valid=90% (180/200 actions), format_ok=100%, success_rate=0%。完整 50-episode eval 未完成（为 GRPO 让出 GPU）。\", \"conclusion\": \"success\", \"metrics\": {\"action_is_valid\": 0.9, \"format_ok\": 1, \"success_rate\": 0, \"final_loss\": 0.069, \"final_token_accuracy\": 0.973, \"data_count\": 1200, \"epochs\": 3, \"total_steps\": 225, \"training_time_s\": 576}, \"hypothesis\": \"基础格式SFT使Qwen3-1.7B学会ALFWorld动作格式和有效动作选择(format_ok+action_is_valid)，建立可训练基线，为后续expert SFT和GRPO提供非随机起点\"}, \"exp028c_selfguide_recipe\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:38:48.089Z\", \"updated_at\": \"2026-05-16T08:29:53.723Z\", \"wandb_run_id\": \"4yu6qz1m\", \"notes\": \"D052 终止。step_independent h=2 导致灾难性过拟合：step_5_val best@128=10.0 → step_10_val best@800=0.0。train success 波动上升(peak 21.88%)=局部动作过拟合，但无法泛化到新 game。根因：(1) step_independent 破坏长程信用分配 (2) self-guidance reward 缺失 (3) val 仅 16 episodes。参见 selfguide_setup_audit.md。\", \"metrics\": {\"step_0_val\": {\"success\": 6.25, \"pass_at_1\": 6.25, \"action_is_valid\": 74.5, \"score_mean\": 0.119}, \"step_1_train\": {\"success\": 13.28, \"pass_at_8\": 37.5, \"action_is_valid\": 76.4, \"action_is_effective\": 96.37, \"entropy\": 0.2634, \"kl_loss\": 0.0128, \"ppo_kl\": 0.019, \"grad_norm\": 16.88, \"score_mean\": 0.843, \"time_s\": 3252, \"note\": \"三方交叉验证通过\"}, \"step_2_train\": {\"success\": 6.25, \"pass_at_8\": 25, \"action_is_valid\": 83.2, \"entropy\": 0.247, \"kl_loss\": 0.1706, \"pg_loss\": 0.007, \"grad_norm\": 17.3, \"score_mean\": 0.274, \"time_s\": 3120}, \"step_3_train\": {\"success\": 15.63, \"pass_at_8\": 68.75, \"action_is_valid\": 85.9, \"entropy\": 0.2488, \"kl_loss\": 0.1118, \"grad_norm\": 12.57, \"score_mean\": 0.661, \"time_s\": 2760}, \"step_4_train\": {\"success\": 18.75, \"pass_at_8\": 62.5, \"action_is_valid\": 87.94, \"entropy\": 0.234, \"kl_loss\": 0.031, \"ppo_kl\": 0.015}, \"step_5_train\": {\"success\": 9.4, \"pass_at_8\": 37.5, \"action_is_valid\": 89.6, \"entropy\": 0.236, \"kl_loss\": 0.824, \"grad_norm\": 13.1}, \"step_5_val\": {\"success\": 6.25, \"pass_at_1\": 6.25, \"action_is_valid\": 96.5, \"action_is_effective\": 100, \"num_actions\": 49.4, \"score_mean\": 0.518}, \"step_6_train\": {\"success\": 10.94, \"action_is_valid\": 90.4, \"entropy\": 0.234, \"kl_loss\": 0.098, \"grad_norm\": 12.54}, \"step_7_train\": {\"success\": 21.88, \"pass_at_8\": 56.25, \"action_is_valid\": 91.8, \"entropy\": 0.224, \"kl_loss\": 0.046}, \"step_8_train\": {\"success\": 15.6, \"pass_at_8\": 50, \"action_is_valid\": 92.7, \"kl_loss\": 0.039, \"entropy\": 0.204}, \"step_9_train\": {\"success\": 18, \"pass_at_8\": 56.3, \"action_is_valid\": 93.6, \"kl_loss\": 0.047, \"entropy\": 0.204}, \"step_10_train\": {\"success\": 18.75, \"action_is_valid\": 90.7, \"kl_loss\": 0.197}, \"step_10_val\": {\"success\": 0, \"pass_at_1\": 0, \"best_at_128\": 0, \"best_at_800\": 0, \"action_is_valid\": 93.6, \"num_actions\": 49.8, \"reward_mean\": 0, \"note\": \"灾难性崩溃，模型完全遗忘\"}}, \"conclusion\": \"failed\"}, \"exp028a_recipe_fix\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:08:53.131Z\", \"updated_at\": \"2026-05-15T21:25:46.006Z\", \"hypothesis\": \"invalid_action_penalty (-0.1) 为全失败 GRPO group 提供非零方差梯度信号。从 exp021 SFT checkpoint (6.25% success) 出发，仅增加 invalid_action_penalty_coef=0.1，其余参数与 exp027 完全一致。预期：penalty 让失败 trajectory 间有区分（invalid action 多=reward更低），解决 ~43% group 零梯度问题。Pass: success ≥20%（稳定，非瞬时 peak）。\", \"parent\": \"exp027_stable_grpo\", \"wandb_run_id\": \"lu42su82\", \"conclusion\": \"killed\", \"notes\": \"与 exp027 功能等价（penalty getattr 默认值=0.1 在 exp027 中已生效）。Director 指令停止。\"}, \"exp028_prereq_zeroshot_instruct\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T20:59:57.529Z\", \"updated_at\": \"2026-05-15T21:06:09.982Z\", \"hypothesis\": \"Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证\\\"SFT是毒药\\\"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。\", \"parent\": \"exp027_stable_grpo\", \"notes\": \"Qwen3-1.7B 确认就是 instruct 模型（无独立 Instruct 变体）。零样本 eval 0% success / 0.75% valid（与之前结果一致）。关键结论：\\\"SFT是毒药\\\"假设(D044)不成立——SFT 实际提升了 0%→6.25%。62pp gap 根因排除 SFT，聚焦于 binary reward 零梯度 + mini-batch 过小 + 训练步数不足。\"}, \"exp027_stable_grpo\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:04:13.123Z\", \"updated_at\": \"2026-05-15T20:44:26.582Z\", \"notes\": \"进程退出原因：Ray raylet 被异常终止（ActorUnavailableError: RPC error: Socket closed rpc_code: 14）。Raylet termination unexpected — 可能 SIGKILL by OOM killer 或内存访问错误。退出发生在 step 4 完成后、step 5 开始前。EXIT_CODE=1。D045 已判定 MVP 未通过（train success 13.28% < 20% 阈值）。Recipe Gap 诊断三大根因：(1) SFT 起点反效果 (2) Binary reward 零梯度 (3) Mini-batch 8× 过小。exp028 配置准备中（5 个 Worker 活跃）。\", \"hypothesis\": \"Stabilized step-independent GRPO: 针对 exp026 死亡螺旋根因（sparse reward + 小 env_groups 导致全零 batch），增加 rollouts（env_groups 4→8, 128 trajectories）、降低 LR（1e-6→5e-7）、降低 KL（0.01→0.005）、新增 entropy bonus（0.01）、save_freq 5 捕获峰值。50 步快速验证。Pass: success ≥20% 且无连续 2 步归零。\", \"parent\": \"exp026_step_independent_grpo\", \"wandb_run_id\": \"y7jiibqk\", \"metrics\": {\"step_0_val_before_train\": {\"success\": 6.25, \"action_is_valid\": 63.125, \"action_is_effective\": 87.875, \"num_actions\": 42.375, \"response_length\": 114.67, \"reward_mean\": 0.3226, \"val_generation_time_s\": 502.57}, \"step_1_train\": {\"success\": 35.94, \"kl_loss\": 0.058, \"batch_size\": 5152, \"training_time_s\": 4342}, \"step_2_train\": {\"success\": 10.16, \"kl_loss\": 0.413, \"batch_size\": 6144, \"training_time_s\": 5886}, \"step_3_train\": {\"success\": 10.16, \"kl_loss\": 0.248, \"entropy\": 0.385, \"pass_at_16\": 0.5, \"grad_norm\": 21.31, \"reward_mean\": 0.483, \"batch_size\": 6048, \"training_time_s\": 4689}, \"step_4_train\": {\"success\": 13.28, \"pass_at_16\": 0.375, \"note\": \"Director判定: 趋势确认, MVP未通过\"}}, \"conclusion\": \"failed\"}, \"exp025b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:34:34.283Z\", \"updated_at\": \"2026-05-15T07:44:26.903Z\", \"parent\": \"exp025\", \"notes\": \"三次提交均失败。第三次：pre-flight 清理后 Ray 主进程启动成功、数据加载成功（8810 train / 494 val），但 AlfworldWorker 进程初始化时线程创建失败（Resource temporarily unavailable, EAGAIN）。36+ 次 system:11 错误，43+ 次 Fatal Python error: Aborted。jemalloc arena background thread creation failed。根因：系统 nproc/线程上限不足，8 个 AlfworldWorker + Ray 内部线程总数超限。需排查 ulimit -u 和 /proc/sys/kernel/threads-max。\", \"conclusion\": \"failed\"}, \"exp025\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:52:48.190Z\", \"updated_at\": \"2026-05-15T07:34:25.374Z\", \"notes\": \"崩溃原因：(1) conda activate base 错误，应用 /root/autodl-tmp/conda-envs/verl-agent 环境 (2) save_freq=-1 未修改为 25。ModuleNotFoundError — base 环境缺 verl-agent 依赖。教训：提交前必须验证 which python 指向正确环境 + 关键参数在 config 中与预期一致。\", \"conclusion\": \"failed\"}, \"exp021_ragen_sft_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T02:09:31.719Z\", \"updated_at\": \"2026-05-15T06:24:16.570Z\", \"hypothesis\": \"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer&gt; tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"negative\", \"metrics\": {\"train_loss_final\": 0.038, \"train_token_accuracy\": 0.988, \"train_steps\": 320, \"train_epochs\": 2, \"train_time_min\": 47.8, \"ragen_val_success\": 0.25, \"ragen_val_action_is_valid\": 0.875, \"eval_sft_fast_success\": 0, \"eval_sft_fast_format_ok\": 1, \"eval_sft_fast_action_is_valid\": 0.71, \"checkpoint_size_gb\": 3.3, \"ragen_val_success_16ep\": 0.0625, \"ragen_val_action_is_valid_16ep\": 0.6875}, \"notes\": \"D024: conclusion 降级为 negative (原 success)。16ep eval 数据: success=6.25%, action_is_valid=68.75%。原 4ep eval 的 25%/87.5% 为 unreliable_small_sample，不作为决策依据。Registry 无 inconclusive 选项，用 negative 代替。\"}, \"exp024_success_gated_grpo\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T06:03:10.298Z\", \"updated_at\": \"2026-05-15T06:04:06.454Z\", \"hypothesis\": \"Success-gated GRPO from exp021 checkpoint. D026 终止 RAGEN GRPO 后不再适用，success-gated 不解决 context 爆炸根因。关联 D027。\", \"conclusion\": \"killed\", \"notes\": \"D027: Kill exp024 — D026 终止 RAGEN GRPO 后 success-gated 变体不再适用，不解决 context 爆炸根因。关联 D025/D026/D027。\"}, \"exp023c_grpo_serial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T04:20:22.909Z\", \"updated_at\": \"2026-05-15T05:11:22.083Z\", \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint. Serial mode (parallel_friendly=false, max_workers=1) to avoid tatsu race. reward scale=10.0, kl_loss_coef=0.5, LR=5e-7, val env_groups=16, gpu_memory_utilization=0.6, 30 steps. Pass: success ≥ 25%, step time baseline comparison with exp022 (~208s/step).\", \"parent\": \"exp023_grpo_parallel\", \"metrics\": {\"val_step0_success\": 0.0625, \"val_step0_action_is_valid\": 0.6875, \"val_step0_episodes\": 16, \"train_step1_success\": 0.297, \"train_step1_action_is_valid\": 0.791, \"train_step1_entropy\": 0.0652, \"train_step1_pass16\": 0.75, \"train_step1_kl\": 0.000156, \"train_step8_success\": 0.234, \"train_step8_action_is_valid\": 0.779, \"train_step8_entropy\": 0.0555, \"train_step8_pass16\": 0.5, \"train_step8_kl\": 0.000475, \"steps_completed\": 8, \"steps_planned\": 30, \"step_time_seconds_start\": 240, \"step_time_seconds_end\": 365}, \"notes\": \"磁盘满崩溃 (step 9, /root/autodl-tmp 94% 233G/250G, OSError Errno 28)。但 8 步 metrics 趋势已显示退化：train success 29.7%→23.4%↓, pass@16 75%→50%↓, entropy 0.065→0.056↓, KL 0.00016→0.00048↑, step time 240s→365s↓。GRPO 未能在 SFT baseline 上产生改善，反而在退化。注意 step 0 val success=6.25% 与 train step 1 success=29.7% 差异大（val 用不同 game set + 16 episodes vs train 64 trajectories）。Checkpoint: global_step_5 only (save_freq=5, 第二次保存在 step 10 未到)。\", \"conclusion\": \"failed\"}, \"exp023_grpo_parallel\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T04:06:02.056Z\", \"updated_at\": \"2026-05-15T04:12:41.878Z\", \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint with 3 key fixes: (1) reward scale 10.0→1.0 (align with Self-Guide paper binary reward), (2) parallel rollout (max_workers=4, thread-safe env), (3) val env_groups=16 for reliable eval. kl_loss_coef=0.5, LR=5e-7, 30 steps. Pass: success ≥ 25% (maintain SFT baseline), step time < 200s (vs exp022 ~208s serial).\", \"parent\": \"exp022_grpo_from_sft_v4\", \"conclusion\": \"failed\", \"notes\": \"失败原因: textworld PDDL parser (tatsu) 在 val env reset 时崩溃 — tatsu.exceptions.FailedToken: expecting 'action', got template :: \\\"take {o} from {r}\\\". val env_groups=16 加载了更多 game files，触发了某个 game file 与当前 tatsu 版本不兼容的 PDDL grammar. | 已有成果: 无（val_before_train 阶段即崩溃，未开始训练） | 建议: 诊断具体哪个 game file 有问题，降低 val env_groups 或修复 game file/tatsu 兼容性\"}, \"exp022_grpo_from_sft_v4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T03:17:34.035Z\", \"updated_at\": \"2026-05-15T03:52:55.267Z\", \"hypothesis\": \"GRPO from exp021 RAGEN-format SFT checkpoint (25% RAGEN val success baseline). Sparse reward (won=10.0), LR=5e-7, kl_loss_coef=0.5 (5x stronger than exp020b to prevent entropy collapse), max_grad_norm=1.0, 30 steps, val env_groups=8. Pass: success ≥ 25% (maintain SFT baseline).\", \"parent\": \"exp021_ragen_sft_v4\", \"notes\": \"Step 0 val: success=12.5% (1/8), action_is_valid=48.75%。Step 1 完成后 kill。action_is_valid 远低于 SFT eval 结果（87.5%/68.75%），说明 RAGEN GRPO 框架中模型表现显著退化。kl_loss_coef=0.5, env_groups=8 均已确认生效。训练速度 ~208s/step。Checkpoint: global_step_1 可能已保存。\", \"conclusion\": \"killed\", \"metrics\": {\"steps_completed\": 1, \"steps_planned\": 30, \"val_step0_success\": 0.125, \"val_step0_action_is_valid\": 0.4875, \"val_step0_action_is_effective\": 1, \"val_step0_reward_mean\": 1.25, \"val_step0_reward_best\": 6.61, \"val_step0_episodes\": 8, \"step_time_seconds\": 208}}, \"exp021_sft_ragen_format\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T22:35:48.559Z\", \"updated_at\": \"2026-05-15T02:11:46.204Z\", \"hypothesis\": \"Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.\", \"parent\": \"exp019b_expert_sft_v3\", \"notes\": \"被 exp021_ragen_sft_v4 取代。\", \"conclusion\": \"killed\"}, \"exp020d_grpo_from_sft\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T22:19:30.993Z\", \"updated_at\": \"2026-05-15T02:01:10.192Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"failed\", \"notes\": \"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\"}, \"exp020c_grpo_from_sft\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T22:15:37.659Z\", \"updated_at\": \"2026-05-15T02:01:08.768Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"failed\", \"notes\": \"D022 废弃。exp020b 确认 GRPO from SFT 因 RAGEN 格式不兼容导致 val success = 0%。exp020c/d 同样会遇到此问题。改走 exp021（RAGEN 格式 SFT 数据重训）。\"}, \"exp020b_grpo_from_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:12:38.928Z\", \"updated_at\": \"2026-05-15T02:00:56.016Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink with \\\"qwen\\\" in path to pass response_mask assertion (exp020 crashed on this).\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"negative\", \"metrics\": {\"steps_completed\": 22, \"steps_planned\": 30, \"hung_at_step\": 23, \"step1_train_success\": 0.1875, \"step10_train_success\": 0.1875, \"step20_train_success\": 0.125, \"step22_train_success\": 0.0469, \"val_success_step0\": 0, \"val_success_step20\": 0, \"entropy_initial\": 0.107, \"entropy_final\": 0.042, \"grad_norm_initial\": 2.78, \"grad_norm_step20\": 5.58, \"ppo_kl_final\": 0.00918, \"pass_at_16_step1\": 0.75, \"pass_at_16_step22\": 0.25, \"checkpoint_latest\": \"global_step_20\", \"training_status\": \"hung_at_step23_rollout\"}, \"notes\": \"Negative 结论：GRPO from SFT 导致策略坍缩。训练 22/30 步后卡死在 step 23 rollout（环境交互死锁，GPU 0% 利用率但显存仍占 40GB×2）。关键指标全线恶化：train success 18.75%→4.69%（远低于 SFT baseline 20%），val success 始终 0%，entropy 0.107→0.042（坍缩 61%），pass@16 从 75%降到 25%。GRPO 不仅未提升 SFT 性能，反而严重退化。根因分析：sparse reward（won=10.0）学习信号不足以维持 SFT 学到的 task knowledge，KL coef=0.1 不足以约束策略偏移。Checkpoint: /root/autodl-tmp/checkpoints/exp020b/global_step_20/\"}, \"exp020_grpo_from_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:07:16.290Z\", \"updated_at\": \"2026-05-14T22:11:05.341Z\", \"hypothesis\": \"GRPO from exp019b SFT checkpoint (20% success baseline) can maintain or improve success rate. Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%.\", \"parent\": \"exp019b_expert_sft_v3\", \"conclusion\": \"failed\", \"notes\": \"失败原因: AssertionError at train.py:137 — model_path=/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final 不含 \\\"qwen\\\" 字符串，enable_response_mask=true 断言失败。模型实际是 Qwen3-1.7B 微调 checkpoint，路径命名问题。error_type=infrastructure | 建议: 创建含 \\\"qwen\\\" 的 symlink 或添加 enable_response_mask=false override 后重提交\"}, \"exp019c_expert_sft_v3\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T21:03:02.685Z\", \"updated_at\": \"2026-05-14T21:05:37.494Z\", \"hypothesis\": \"Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。\", \"parent\": \"exp019b_expert_sft_v3\", \"notes\": \"废弃。submit_training_job 因 GPU 被占（exp019b nohup 进程仍在跑）EXIT_CODE=1 退出。实际训练由 exp019b 的 nohup 进程完成。\", \"conclusion\": \"killed\"}, \"exp019_expert_sft_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T16:38:05.515Z\", \"updated_at\": \"2026-05-14T17:11:09.024Z\", \"conclusion\": \"killed\", \"notes\": \"D019 kill：move→put 替换方向错误。ALFWorld admissible_commands 包含 move X to Y，不含 put。用 put 替换的数据会使 action_is_valid 更差。改用原始 expert data（保留 move）+ admissible actions augmentation。\"}, \"exp019b_expert_sft_v2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T16:49:30.246Z\", \"updated_at\": \"2026-05-14T16:49:30.246Z\"}, \"exp018_sft_grpo\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T15:43:08.545Z\", \"updated_at\": \"2026-05-14T16:45:33.314Z\", \"hypothesis\": \"Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），使 GRPO 有足够非零 reward group 产生有效梯度。LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, won=10.0, 无 bonus/penalty, GRPO 30 步。Pass: success ≥ 20%。\", \"parent\": \"exp017_expert_sft\", \"conclusion\": \"killed\", \"notes\": \"D018 取消：exp017 eval 5% success 与 base 4.7% 差异太小，GRPO 大概率重蹈覆辙。等 exp019 v2 SFT（修复 move→put + admissible actions 数据增强）后再考虑 GRPO。\"}, \"exp017_expert_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:36:28.291Z\", \"updated_at\": \"2026-05-14T16:36:17.637Z\", \"hypothesis\": \"Expert SFT: 用 PDDL expert trajectory 数据 SFT Qwen3-1.7B instruct 模型，提升 ALFWorld baseline success rate，为后续 GRPO 提供更好的冷启动点。LR=2e-5, 3 epochs, batch_size=4, grad_accum=4。Pass 标准: success ≥ 10%。\", \"parent\": \"exp008_sft\", \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.1434, \"final_step_loss\": 0.04, \"final_token_accuracy\": 0.983, \"epochs\": 3, \"total_steps\": 462, \"training_time_min\": 26, \"data_count_train\": 2460, \"data_count_val\": 129, \"checkpoint_size_gb\": 3.44, \"eval_success_rate\": 0.05, \"eval_success\": \"1/20\", \"eval_action_is_valid\": 0.638, \"eval_format_ok\": 0.75, \"eval_avg_steps\": 22, \"eval_time_s\": 149.6, \"eval_per_task\": {\"put\": \"0/10\", \"clean\": \"0/4\", \"cool\": \"1/3\", \"heat\": \"0/2\", \"examine\": \"0/1\"}, \"eval_parse_failures\": \"5/20 episodes (EP 7/12/16/17/18)\"}, \"notes\": \"训练成功完成。Expert PDDL trajectory 2460 条 SFT Qwen3-1.7B，3 epochs 462 steps 26 min。Final loss=0.1434。Checkpoint: /root/autodl-tmp/checkpoints/exp017_expert_sft/final/ (3.44GB)。\\n\\nEval 结果（20 episodes, vLLM 推理, max_steps=30）：success=5% (1/20), action_is_valid=63.8%, format_ok=75%。唯一成功是 1 个 cool 任务（EP 8, 15 步）。5/20 episodes parse 失败（1 步即退出）。put 任务 0/10 全失败。\\n\\n对比 exp008_sft（1200 条普通 SFT）：action_is_valid 90%→63.8%（下降！）, format_ok 100%→75%（下降！）, success 0%→5%（略升）。Expert data SFT 提升了 success 但 format/valid 反而退步，可能因为 expert trajectory 格式与 RAGEN 的 &lt;think>/&lt;answer> 格式不完全匹配。\"}, \"exp016\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:44:58.883Z\", \"updated_at\": \"2026-05-14T15:36:27.432Z\", \"hypothesis\": \"LR 折中方案：LR=5e-7（exp012b 1e-6 collapse vs exp015 1e-7 零梯度的中间值）。kl_loss_coef=0.1, max_grad_norm=1.0 保持。纯 sparse reward（won=10.0，无 bonus，无 format_penalty）。从 exp015/global_step_5 checkpoint 恢复，GRPO 30 步。\", \"parent\": \"exp015\", \"metrics\": {\"step\": 12, \"total_steps\": 30, \"elapsed_min\": 51, \"step6_success\": 0, \"step6_action_is_valid\": 0.521, \"step6_pg_loss\": 0, \"step6_grad_norm\": 0.841, \"step7_success\": 0.047, \"step7_pass_at16\": 0.5, \"step7_action_is_valid\": 0.655, \"step10_success\": 0, \"step10_action_is_valid\": 0.664, \"step10_pg_loss\": 0, \"step10_grad_norm\": 0.856, \"step10_entropy\": 0.1046, \"step10_ppo_kl\": -9.1e-05, \"all_raw_rewards\": 0, \"all_advantages\": 0, \"all_returns\": 0, \"reward_signal\": \"BROKEN — success episodes get reward=0\", \"action_is_valid_trend\": \"52.1%→65.5%→66.4%\", \"manager_invalid_action_trend\": \"13.5%→11.2%→9.6%\"}, \"conclusion\": \"failed\", \"notes\": \"D015 kill。训练 12 步，pg_loss 恒为 0。原因：base success ~4.7%（仅 val，train temperature=1.0 下接近 0%），纯 sparse reward 下 GRPO 无有效学习信号。raw_reward=0 是日志 artifact（info dict 缺 raw_reward 字段），实际训练 reward pipeline 正常（critic/score 正确传递，step 7 score/mean=0.46875=3/64×10.0）。NaiveRewardManager 是 pass-through，不覆盖 env reward。LR=5e-7 本身无问题，根因是 sparse reward 冷启动。\"}, \"exp015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:48:38.065Z\", \"updated_at\": \"2026-05-14T13:44:57.940Z\", \"hypothesis\": \"Sparse GRPO + 训练稳定性修复。纯 sparse reward（won=10.0，无 valid_action_bonus，无 format_penalty）。针对 exp012b 的 step 7 catastrophic collapse（grad_norm 1.48→0.094），三项修复：LR 1e-7（降 10 倍防单步更新过激）、kl_loss_coef 0.1（增 10 倍约束策略偏移）、max_grad_norm=1.0（梯度裁剪）。从 exp008 step 5 checkpoint 恢复，GRPO 30 步。\", \"parent\": \"exp012b\", \"notes\": \"D014 kill。Steps 3-5 连续零梯度（pg_loss=0, grad_norm~0），LR=1e-7 过保守导致无有效学习。Step 0 val: action_is_valid=85.8%, success=0%。训练稳定性修复验证成功（无 catastrophic collapse），但学习率不足以产生有意义的 policy update。Checkpoint: global_step_5 已保存，供 exp016 恢复。\", \"metrics\": {\"step\": 1, \"total_steps\": 30, \"val_step0_success\": 0, \"val_step0_action_is_valid\": 0.858, \"val_step0_pass_at1\": 0, \"val_step0_episodic_return\": 0, \"val_step0_response_length\": 2797.5, \"val_train_transition\": \"passed\", \"estimated_total_time_min\": 163, \"time_per_step_min\": 5.6}, \"conclusion\": \"killed\"}, \"exp014b\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T12:45:27.876Z\", \"updated_at\": \"2026-05-14T12:48:37.433Z\", \"hypothesis\": \"极低 Dense Reward: valid_action_bonus=0.01（1:1000 比例），测试极弱 bonus 能否防 collapse 又不引发 gaming。如果 bonus 弱到不影响 GRPO reward ranking，模型不会被诱导走捷径。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\", \"parent\": \"exp013f\", \"conclusion\": \"killed\", \"notes\": \"D013 撤销：Director 修订决策，改为 exp015。exp014b 等 exp015 结果后再决定。\"}, \"exp014a\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T12:45:27.347Z\", \"updated_at\": \"2026-05-14T12:48:35.102Z\", \"hypothesis\": \"Success-Gated Dense Reward: valid_action_bonus=0.15 只在 group 内至少一条 trajectory success 时才给。消除 reward gaming 的独立最大化路径——没有 success 就没有 bonus，模型必须探索 success。success_reward=10.0, format_penalty=0, 从 exp008 step 5 checkpoint 恢复, GRPO 30 步。\", \"parent\": \"exp013f\", \"conclusion\": \"killed\", \"notes\": \"D013 撤销：Director 修订决策，success-gated bonus 有 bootstrap 问题（初始 success=0 时 bonus 永远为 0，退化为 sparse reward），改为 exp015 纯 sparse GRPO + 训练稳定性修复。\"}, \"exp014c\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T12:45:21.231Z\", \"updated_at\": \"2026-05-14T12:45:25.025Z\", \"hypothesis\": \"Success-gated valid_action_bonus：bonus 仅在 episode 成功时累加到 reward，消除独立最大化路径。valid_action_bonus=0.15, success_reward=10.0。解决 exp013f reward gaming（unconditional bonus 导致 agent 放弃 success 追求 valid action）。从 step 5 checkpoint 恢复 GRPO 30 步。\", \"parent\": \"exp013f\"}, \"exp013e\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T09:02:52.837Z\", \"updated_at\": \"2026-05-14T09:21:08.911Z\", \"hypothesis\": \"exp013d 基础设施修复重试。Ray object_store_memory 改用 Hydra config override (ray_kwargs.ray_init.object_store_memory=32212254720) 替代无效的环境变量。其余同 exp013d: dense reward shaping (valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0), env_groups=4, 从 step 5 checkpoint 恢复。\", \"parent\": \"exp013d\", \"conclusion\": \"failed\", \"notes\": \"ActorUnavailableError: RPC error: Socket closed rpc_code: 14。validation step 5 完成后向 training step 6 过渡时崩溃。诊断排除: cgroup OOM (oom_kill=0)、系统 OOM (dmesg 无记录)、CUDA OOM (无日志)、磁盘满 (118GB剩余)。Ray worker 日志被 ray stop --force 清除，最可能原因: vLLM worker 在 val→train 切换时的内存峰值或内部错误。object_store_memory=30GB 设置正确(train.py:203)。validation 指标: success=0, action_is_valid=0.656, reward_mean=2.953, reward_std=1.608。结论: 瞬态崩溃，可安全重提交。建议加 HYDRA_FULL_ERROR=1。\"}, \"exp013d\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:34:37.036Z\", \"updated_at\": \"2026-05-14T08:52:25.371Z\", \"hypothesis\": \"exp013b/c 内存修复重试。Dense reward shaping (valid_action_bonus=0.15) 已验证有效 (reward_std=1.608>0)。修复: env_groups 8→4 (64并发, 峰值~158GB < 220GB cgroup限制) + RAY_object_store_memory=30GB。\", \"parent\": \"exp013c\", \"notes\": \"RAY_object_store_memory env var 未生效，Ray 仍分配 70.36GB object store（默认值）。env_groups=4 生效但不够。Raylet 被 cgroup OOM killer SIGKILL。修复: 用 Hydra config override ray_kwargs.ray_init.object_store_memory=32212254720 显式传给 ray.init()。\", \"conclusion\": \"failed\"}, \"exp013c\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:30:44.623Z\", \"updated_at\": \"2026-05-14T08:34:10.517Z\", \"hypothesis\": \"exp013b 基础设施重试。Dense reward shaping (valid_action_bonus=0.15 + success=10.0) 已验证有效 (reward_std=1.608>0)。exp013b 因 OOM/Ray 崩溃，非算法问题。\", \"parent\": \"exp013b\", \"notes\": \"预防性kill。诊断确认 exp013b 崩溃根因: cgroup 内存限制 220GB, Ray object_store 70GB + memory 164GB = 234GB 超限。128并发ALFWorld游戏(8 env_groups × 16 group_size)在 step 6 rollout 触发 Plasma mmap ENOMEM。exp013c 同配置会重现。修复: env_groups 8→4 + RAY_object_store_memory=30GB。\", \"conclusion\": \"killed\"}, \"exp013b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:15:44.247Z\", \"updated_at\": \"2026-05-14T08:27:21.850Z\", \"hypothesis\": \"Dense reward shaping: valid_action_bonus=0.15 per valid action + success_reward=10.0 + kl_loss_coef=0.01。每步有效动作获得 0.15 奖励提供持续 GRPO 学习信号（30步累计上限4.5 vs 终局10.0），KL 约束防止 policy 过激更新。format_penalty=0，从 step 5 checkpoint 恢复 GRPO 30 步。\", \"parent\": \"exp013\", \"notes\": \"Dense reward shaping 有效性已确认：val reward_mean=2.953, reward_std=1.608 (>0)。崩溃是基础设施问题（OOM/Ray），非算法问题。清理后重试。超参: valid_action_bonus=0.15, kl_loss_coef=0.01, success_reward=10.0, format_penalty=0, group_size=16。\", \"conclusion\": \"failed\"}}, \"count\": 50, \"total\": 69, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1919}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data from the registry. Let me extract the key numbers I need:

**SFT baseline:**
- 32 in-distribution tasks: 12.5% (4/32) - from exp029_episode_level notes
- Zero-shot: 0% (exp028_prereq_zeroshot)
- SFT on 134 OOD tasks: I need to find this. From exp029_episode_level, reeval_ood_134tasks success was 0.2388 (23.88%) at step 15. But what about SFT step 0? Let me look...


- From exp028c_selfguide_recipe: step_0_val success=6.25% (but that's 16 episodes in-distribution)
- From exp021_ragen_sft_v4: ragen_val_success_16ep = 0.0625 (6.25%)
- For OOD 134 tasks SFT baseline, I can see factorial_h2_episodeadv_seed1 has val_step5 success=0.0597 on AlfworldOOD_134tasks. But that's step 5, not step 0.

I'm looking more carefully at the baseline numbers to pin down the exact step 0 performance on the OOD tasks. Looking at the exp029 reeval data, I found that step 15 with h=2 achieved 23.88% on OOD 134. Since there's no direct SFT baseline measurement for OOD, I'll note the zero-shot baseline at 0% and the in-distribution SFT performance at 12.5% for reference. Now I'm drafting the experiments section, making sure to follow the formatting constraints—avoiding em-dashes and -ing phrase endings, using booktabs for tables, and keeping the setup around 900 words while preserving the placeholder command definition. I'll start laying out the full LaTeX file with the key metrics like the 2546 expert trajectories for SFT.

Now I'm reviewing the experimental results across different configurations: the episode-level approach peaked at 23.88% OOD accuracy, the step-independent variant collapsed entirely, the factorial combination with episode advantage showed promise at 5.97% early on, and the dense reward variant improved action validity substantially but didn't translate to success gains.

Looking at the extended runs to 30 steps, the GAE/REINFORCE++ baseline holds steady at 12.5%, the discount factor sweeps all failed to improve, and I'm still tracking the hyperparameter h sweeps across different values. I'm also mapping out the seven experimental conditions from the paper with their corresponding seed runs to ensure I have the right experiment IDs for each configuration.

Now I'm drafting the appendix sections with specific word targets for each part—the ALFWorld environment description, base model setup, RL training configuration with a table, evaluation protocol, and the experimental conditions breakdown, followed by results stubs.

Generating LaTeX table...

Now I'm thinking through the cross-references I need to maintain, particularly the section references and citation keys for ALFWorld, the RAGEN framework, and the GRPO paper. The structure needs to be reorganized into a proper section hierarchy with subsections 5.1 through 5.6, moving from Environment setup through to Results, replacing the current subsection-only format.

As I'm composing the full content, I need to be careful about the writing style—avoiding em-dashes, -ing phrase endings, and repetitive transition words. The setup section should be around 900 words with complete content and no placeholders. I'm also reviewing the baseline performance data to make sure I have the right numbers for the zero-shot evaluation and the SFT results across different task distributions. Looking at the registry more carefully, exp029 step0 data isn't explicitly available for the OOD evaluation either—the OOD reeval happened later at step 15. The in-distribution SFT baseline from exp028c shows 6.25% on 16 episodes at step 0, and the gamma sweep checkpoint (gsweep_g050_h5_seed1) gives 9.4%, though I'm uncertain which eval set that's on. Given these gaps, I'll stick with reporting the 12.5% in-dist SFT baseline and 0% zero-shot, then note that OOD results come from the 134-task evaluation without a clean step0 SFT comparison. I'm seeing that the step 0 validation numbers vary across experiments due to different evaluation sets and episode counts, so the canonical 12.5% baseline on 32 in-distribution tasks is what I'll use. Now I'm planning out section 5.5 to describe each experimental condition clearly—episode-level GRPO that processes full trajectories as single samples, step-independent configurations with h=2, and the other variants I need to detail.

For the remaining conditions, I'm laying out the factorial cell with h=2 and episode-level advantage that isolates M1, the dense reward variant testing if per-step bonuses help, a REINFORCE++ baseline using running-mean instead of value functions, and sweeps over discount factors and window sizes to understand what drives the step-independent failures.

Now I'm drafting the LaTeX for the experiments section, starting with the research questions and environment setup.

Writing the paper structure... The gradient sign issue becomes critical at this success rate. Now I'm setting up the RL training with RAGEN and GRPO, using a group size of 8 and a learning rate of 1×10⁻⁶, where the discount factor only applies to step-independent returns while episode-level training uses undiscounted returns.

For evaluation, I'm using two task sets—a 32-task in-distribution validation set and a 134-task out-of-distribution set for generalization—with success rate as the primary metric, measuring whether episodes complete within 50 steps, plus pass@k variants for k in {2, 4, 8}.

I'm also tracking action validity rate as a diagnostic to see what fraction of outputs are syntactically valid commands versus malformed or repeated text, which gives me a sense of basic policy coherence separate from actual task performance. Now I'm thinking through how to structure the experimental conditions section—I need to describe seven conditions organized around three experimental designs, and I'm deciding whether to use a table or write them out systematically condition by condition to explain their relationships and purposes. I'm thinking through the relationships between the experimental conditions—conditions 1-3 form a factorial 2×2 design, condition 6 isolates the effects of magnitude decay versus sign misattribution, and condition 7 sweeps across different levels of information loss severity. I'm also tracking the seed allocations across all conditions: most get 2 seeds, dense reward and REINFORCE++ each use 1 seed, the γ-sweep uses 1 seed per value, and the h-sweep is still collecting data for h=5/10/20. Now I need to write the complete section while maintaining the writing standards and checking that I have the right citation for GRPO and DeepSeekMath. I'm checking the cross-references in the current file to make sure I preserve them—there are several equation and section labels being cited throughout, like the step return equation and the sign correlation equation. Now I'm drafting the complete LaTeX file, making sure to keep the placeholder command definition at the top and being careful not to use placeholders in the setup sections, only in the results stub.

Writing the experiments section... sign misattribution (M2) through factorial manipulation? Third, how does the window size $h$ modulate both mechanisms?

\subsection{Environment}
\label{sec:environment}

We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with simulated rooms through natural language commands. ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \in \{0, r_+\}$, with $r_+$ awarded only upon task completion.

ALFWorld tasks exhibit strong sequential dependencies: a typical task requires the agent to locate an object, pick it up, navigate to a target receptacle, and place it. With step-independent windowing at small window sizes, the window containing the placement action loses access to the exploration steps that identified the target object, making this environment ideal for studying how context truncation breaks the policy's ability to ground late actions in early observations.

\subsection{Base Model and Supervised Fine-Tuning}
\label{sec:base_model}

I'm using Qwen3-1.7B as the base policy model and performing supervised fine-tuning on expert demonstrations before RL training. The SFT checkpoint achieves a baseline success rate on held-out tasks, but the pre-SFT model fails completely on out-of-distribution tasks, confirming that fine-tuning is essential for initialization. This low baseline is analytically important because it means a large fraction of gradient updates during step-independent training will have incorrect advantage signs, which directly relates to the theoretical predictions about when the algorithm struggles.

Now I'm setting up the RL training configuration using the RAGEN framework with the GRPO algorithm, and I need to specify how the discount factor applies differently depending on whether we're computing returns step-independently or over full episodes.

Generating hyperparameter table...

Now I'm laying out the evaluation setup: we're testing on 32 in-distribution tasks and 134 out-of-distribution tasks to assess generalization, with evaluation happening every 5 training steps. The main metric is success rate—how many episodes complete within 50 steps—plus pass@k variants, and I'm also tracking action validity rate to measure whether the agent's outputs are syntactically correct commands. Moving into the experimental conditions next, which involve seven different setups organized around three main designs.

I'm comparing three factorial conditions that isolate different mechanisms: the first uses episode-level GRPO where the entire trajectory is one sample with a shared advantage signal across all tokens, eliminating both context truncation and per-window advantage attribution issues. The second follows the standard RAGEN approach with windows of 2 steps, each with its own advantage, which activates both the context truncation and per-window advantage problems. The third condition combines step-independent windowing with episode-level advantage to isolate the factorial effects. Conditions 1 and 2. Windows are constructed identically to Condition 2 ($h = 2$), but all windows within an episode share a single episode-level advantage rather than receiving independent per-window advantages. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign misattribution). This isolates the effect of sign misattribution: any performance gap between Conditions 2 and 3 is attributable to M2 alone. Two seeds.

Conditions 1--3 form a $2 \times 2$ factorial design over observation scope (windowed vs.\ full) and advantage scope (per-window vs.\ episode-level). The missing cell would combine full observation with per-window advantage, but that's degenerate since full-context windows produce only one window per episode.

Condition 4 tests whether dense reward shaping can overcome credit assignment failures by adding a $+0.15$ bonus for each syntactically valid action during step-independent training with $h=2$, running for 30 steps to allow convergence. Condition 5 replaces GRPO group normalization with a per-token running-mean baseline in episode-level training, using REINFORCE++ as a value-free alternative since the value head was removed from TRL. Condition 6 is cut off but appears to be introducing another experimental variant. Discount factor sweep with $h = 5$ and $\gamma \in \{0.50, 0.80, 0.95, 1.00\}$ to isolate magnitude decay's role—at $\gamma = 1.0$, equal weighting across windows means any collapse stems from sign misattribution rather than discounting. Window-size sweep across $h \in \{2, 5, 10, 20\}$ versus full-episode training tests how context length affects both mechanisms, with smaller windows intensifying M1 and amplifying M2's per-update impact; data collection for larger windows is still in progress.

Now I'm organizing the results around three main comparisons: episode-level versus step-independent dynamics, the factorial mechanism separation, and the ablation studies on window size and discount factors. The SFT checkpoint reaches 12.5% success on the in-distribution test set, while the pre-trained model fails completely on out-of-distribution tasks, establishing that supervised fine-tuning is essential. This baseline performance is analytically useful because at that success rate with a group size of 8, the theory predicts roughly 80% of gradient updates will have the wrong advantage sign under step-independent training.

Now I'm planning the structure for the remaining experimental sections—RL training configuration around 100 words, evaluation protocol at 120 words, and the core experimental conditions section at 300 words. I should organize these as separate subsections rather than paragraphs to match the section numbering scheme.

I need to verify the cross-reference labels I'm using, particularly for the factorial design reference and proposition citations, to ensure they align with what's defined elsewhere in the paper. For the en-dash formatting in LaTeX, I'll use the standard double-hyphen convention.

I'm also being careful about participial phrase endings—while constructions like "making ALFWorld a natural testbed" are acceptable, I should avoid sentences that end with explanatory participial phrases. Let me refine the phrasing to steer clear of any ambiguous cases and ensure the draft adheres to the style constraints. I'm finalizing the experiments.tex file now, making sure to completely rewrite it while preserving the newcommand definitions. I'll keep the setup section detailed and leave results as a stub for now. For the SFT out-of-distribution numbers, I'll stick with what I can cleanly report: zero-shot baseline at 0% and in-distribution SFT at 12.5%, without speculating on OOD performance I don't have solid data for. $r_+$ awarded only upon successful task completion.

ALFWorld tasks have strong sequential dependencies—a typical episode involves locating an object, picking it up, navigating to a target location, and placing it. With step-independent windowing at small window sizes, later actions lose access to earlier observations that established context, directly undermining the policy's ability to condition decisions on prior information.

For the base model, I'm using Qwen3-1.7B and performing supervised fine-tuning on expert demonstrations from ALFWorld before moving to reinforcement learning.

The SFT checkpoint reaches 12.5% success on the validation set, while the pre-trained model achieves 0% in zero-shot evaluation, establishing that fine-tuning is essential for RL. This low baseline is analytically useful because at this success probability with the group size used, the theory predicts that roughly 80% of gradient updates will have incorrect advantage signs under step-independent training, creating a regime where sign misattribution is nearly maximal.

For RL training, I'm using the RAGEN framework with the GRPO algorithm, and I'm setting up the shared hyperparameters including the discount factor.

Now I'm looking at the evaluation setup across two task sets: the 32-task in-distribution validation set and a 134-task out-of-distribution set to measure generalization.

The main metric is success rate (pass@1) for episodes completed within 50 steps, with pass@k variants for k=2,4,8. I'm also tracking action validity rate as a diagnostic to measure whether the agent outputs syntactically valid commands, which gives insight into policy coherence independent of task completion. Most results are single-seed runs with two-seed replication reported where available.

I'm organizing the experimental conditions into three groups: factorial mechanism separation for the first three conditions, auxiliary baselines for conditions 4-5, and parameter sweeps for 6-7. The first condition implements the proposed episode-level GRPO method where complete trajectories are treated as units.

Now I'm describing the comparison conditions. Condition 2 uses the RAGEN default with windows of 2 steps and per-window advantages, activating both mechanisms I'm trying to isolate. Condition 3 keeps the windowed structure but applies episode-level advantages instead, isolating the effect of advantage attribution while maintaining truncated context.

These three conditions form a factorial design across observation scope and advantage scope, though the fourth cell would be degenerate since full context means only one window per episode. Condition 4 tests whether dense per-step rewards can overcome the credit assignment issues by extending training to 30 steps. Condition 5 is cut off but appears to be introducing another variant.

Condition 5 uses REINFORCE++ with episode-level training and a per-token running-mean baseline instead of the group normalization in GRPO—this was adapted after a library update removed the value head class. Condition 6 sweeps the discount factor across values from 0.50 to 1.00 with step-independent h=5, where γ=1.0 would eliminate magnitude decay and isolate whether sign misattribution alone drives the failure.

For Condition 7, I'm testing different window sizes from 2 to 20 tokens in step-independent training, plus full episode-level training, to see how context window affects the severity of the magnitude problem and the number of windows generated per episode—data collection for the larger windows is still underway. The results will be organized around three main comparisons: episode-level versus step-independent dynamics, factorial mechanism separation across conditions, and the ablations on window and discount factor. I need to add more content to reach the target word count, so I'm expanding §5.3 with reasoning about the hyperparameter choices and beefing up §5.5 with more detail on each experimental condition. For the OOD SFT baseline, I'm hesitant to cite a specific number I can't confidently verify from the data, so I'll skip that rather than risk inaccuracy. I need to finalize the draft and make sure I've covered all the relationships between conditions—the factorial 2×2 design for conditions 1-3, condition 6 isolating magnitude decay versus sign misattribution, and condition 7 sweeping information loss severity. Let me also verify the seed counts from the registry and confirm I have the right experimental configurations listed. I've got the results section structure laid out with those three comparisons, and I'm keeping it close to the specified format. Now I'm doing a final check for any forbidden patterns—scanning through for -ing endings that shouldn't be there, making sure the phrasing stays clean and direct. I'm catching myself on the phrasing here—that trailing "-ing" construction violates the style guide, so I need to restructure it. Using a semicolon to separate the clauses works better: "At γ = 1.0, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains." I should also scan the rest of the text for similar participial endings that need fixing, like the phrase about SFT providing initialization for RL. I'm going through each section systematically to verify that sentence endings avoid -ing phrases, checking that constructions like "confirming" get replaced with cleaner alternatives like "initialization for RL." I'm working through how to present this condition more clearly. Rather than starting with a terse statement, I should integrate it into the explanation: in the proposed method, each complete trajectory becomes a single GRPO sample with shared advantage across all tokens, which eliminates both failure mechanisms—the full context stays intact without the M1 problem, and there's no per-window advantage to cause sign misattribution like in M2. Two seeds were used.

For the other conditions, I'm laying out the specifics: Condition 2 segments trajectories into windows of h=2 steps where each gets its own advantage, activating both M1 and M2 as the standard multi-turn RL setup. Condition 3 keeps the same windowing structure but pools all windows in an episode under a single episode-level advantage rather than independent per-window values.

Now I'm moving past the condition descriptions and thinking about the broader paper structure. I should skip the experiment IDs since those are just internal tracking—the paper only needs the conceptual setup. Let me finalize the full section and check the word counts across each part to make sure everything fits properly. I'm checking the cross-reference for the factorial design section and making sure it points to the right label. For condition 5, I need to explain the REINFORCE++ baseline clearly without dwelling on the implementation change from GAE—just noting that it uses a per-token running-mean baseline instead of group normalization, and that there's no separate value function or critic network involved.

I'm also deciding whether to use `\paragraph{}` formatting for the conditions in section 5.5, which keeps things compact and consistent with the existing style. The intro paragraph sets up the three design types nicely, and then each condition gets its own heading. After condition 3, I should keep the factorial design explanation as a regular paragraph continuation rather than making it its own `\paragraph{}` block.

Now I'm checking the OOD baseline data for section 5.2. The task mentions I should reference the SFT results if available, and from the registry I can see exp028_prereq_zeroshot shows 0% zero-shot success on ALFWorld tasks with the Qwen3-1.7B model, while exp029 has the SFT data I should reference.

I'll note the 0% zero-shot result without getting too specific about the exact eval set since the context makes it clear. Now I need to verify whether there's a citation for Qwen3 in the bibliography before I finalize this section. how the window size $h$ affects the severity of both mechanisms? Now I'm describing the experimental environment—ALFWorld, a text-based household simulation where agents navigate rooms and complete tasks through natural language commands across six task types, with binary rewards only for successful completion. The tasks have strong sequential dependencies, requiring agents to locate objects, manipulate them, navigate to targets, and place them in specific locations.

With small windows like $h = 2$, the placement action loses access to the earlier exploration steps that identified the target object, so context truncation directly undermines the policy's ability to condition later actions on earlier observations. I'm detailing the base model setup: using Qwen3-1.7B with supervised fine-tuning on expert demonstrations, achieving 12.5% success rate on validation—a deliberately low baseline that creates a regime where sign misattribution is near-maximal, providing a stringent test of the proposed mechanism. For RL training, I'm noting the shared configuration across all conditions using RAGEN with GRPO, including the hyperparameters like group size 8, learning rate $1 \times 10^{-6}$, KL penalty 0.01, and discount factor 0.95.

Now I'm describing the evaluation setup: testing on both a 32-task in-distribution set and a 134-task out-of-distribution set for generalization, with the primary metric being success rate (pass@1) over 50 steps, plus pass@$k$ variants and action validity rate as a diagnostic measure of policy coherence.

For the experimental conditions, I'm laying out seven different setups across three design categories: the first isolates episode-level GRPO without context truncation or per-window advantage issues, the second introduces fixed 2-step windows with both mechanisms present, and the remaining conditions explore auxiliary baselines and parameter variations. The fourth condition completes the factorial design—with full observations, there's only one window per episode, so per-window and episode-level advantages are equivalent. Condition 4 tests whether dense reward shaping with a small bonus for valid actions can overcome the credit assignment problem in step-independent training. Conditions 5 and 6 explore alternative baselines and discount factors, including a REINFORCE++ variant with running-mean normalization and a sweep across different gamma values to assess their impact on learning.

For Condition 7, I'm varying the window size from 2 to 20 steps in step-independent training and comparing against full-episode training, with data collection still underway for the larger window sizes. The results section will organize findings around three main comparisons: episode-level versus step-independent dynamics, factorial mechanism separation, and ablations on window size and discount factors. I'm double-checking the constraint about -ing phrase endings more carefully. That participial phrase "requiring sequential reasoning" is embedded within a clause modifying "task types," not trailing at the end, so it should be acceptable under the rule. The constraint seems to target trailing participial phrases like "demonstrating X" at sentence ends, not reduced relative clauses in the middle of sentences.

But to be safer, I could restructure it to use "that require" instead—it's cleaner anyway and avoids any ambiguity. Let me scan the rest of the setup for similar patterns: the other sentences look fine, no trailing -ing constructions that would violate the guideline.

Now I'm finalizing the edits. I'll swap out "each requiring" for "that require" in section 5.1, and I've already adjusted the SFT sentence from "confirming" to "so" which reads better. The Experiments section intro is solid as-is—it directly lays out the three research questions without unnecessary elaboration.

For the factorial design paragraph, I need to verify the cross-reference points to the right section. I'm using the label reference and assuming it's correctly set up, then I'll save the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "1a34aacb-a3cb-4db8-8230-c16aaa1629d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xTPr7axTjv8wa3nNjDhBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21803,
      "cache_read_input_tokens": 44399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21803
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

_source line 28_

I've read all sources and gathered registry data. Now writing the complete rewrite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "5ea3bf1d-3f39-47e2-8877-ee102580a1f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xTPr7axTjv8wa3nNjDhBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21803,
      "cache_read_input_tokens": 44399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21803
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

_source line 29_

<details open><summary>🔧 Tool call — Write · `toolu_018rBxEBvYJL8EFM9PJZj4uY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
  "content": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?\n\n\\subsection{Environment}\n\\label{sec:environment}\n\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.\n\nALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.\n\n\\subsection{Base Model and Supervised Fine-Tuning}\n\\label{sec:base_model}\n\nWe use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n\nThis low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.\n\n\\subsection{RL Training Configuration}\n\\label{sec:rl_config}\n\nAll conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Shared RL training hyperparameters across all conditions.}\n\\label{tab:hyperparameters}\n\\begin{tabular}{lc}\n\\toprule\nParameter & Value \\\\\n\\midrule\nGroup size $K$ & 8 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nKL penalty $\\beta$ & 0.01 \\\\\nDiscount $\\gamma$ & 0.95 \\\\\nInvalid action penalty & 0.1 \\\\\nTasks per training step & 16 \\\\\nTraining steps & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.\n\nThe primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. All results are single-seed unless stated otherwise; two-seed replication is reported where available.\n\n\\subsection{Experimental Conditions}\n\\label{sec:conditions}\n\nWe evaluate seven conditions organized around three designs: factorial mechanism separation (Conditions~1--3), auxiliary baselines (Conditions~4--5), and parameter sweeps (Conditions~6--7).\n\n\\paragraph{Condition 1: Episode-level GRPO.}\nEach complete trajectory serves as a single GRPO sample with one shared advantage for all tokens. Both failure mechanisms are absent: the full context is preserved (no M1) and no per-window advantage can carry misattributed sign (no M2). Two seeds.\n\n\\paragraph{Condition 2: Step-independent $h{=}2$.}\nEach trajectory is segmented into fixed windows of $h = 2$ interaction steps, with each window receiving its own GRPO advantage. Both M1 (truncated context) and M2 (advantage sign determined by episode outcome rather than local action quality) are active. This is the default RAGEN configuration and represents the standard approach for multi-turn agent RL. Two seeds.\n\n\\paragraph{Condition 3: Step-independent $h{=}2$ with episode advantage.}\nThe factorial complement. Windows are constructed identically to Condition~2, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign assignment). The performance gap between Conditions~2 and~3 is therefore attributable to M2 alone. Two seeds.\n\nConditions~1--3 form a $2 \\times 2$ factorial design over observation scope (windowed vs.\\ full) and advantage scope (per-window vs.\\ episode-level), as described in Section~\\ref{sec:factorial_design}. The fourth cell (full observation with per-window advantage) is degenerate: with full context, only one window exists per episode, so per-window and episode-level advantage coincide.\n\n\\paragraph{Condition 4: Dense reward.}\nStep-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.\n\n\\paragraph{Condition 5: REINFORCE++ baseline.}\nEpisode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used. This condition was originally planned as a GAE baseline with a learned critic; we substituted REINFORCE++ after TRL~1.1.0 removed the required \\texttt{AutoModelForCausalLMWithValueHead} class.\n\n\\paragraph{Condition 6: Discount factor sweep.}\nStep-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. At $\\gamma = 1.0$, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains. Collapse at $\\gamma = 1.0$ would confirm that sign misattribution alone suffices to cause failure, independent of discount-induced magnitude variation.\n\n\\paragraph{Condition 7: Window-size sweep.}\nStep-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.\n\n\\subsection{Results}\n\\label{sec:results}\n\nResults are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size and discount-factor ablations (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "2e7f8073-a7bc-43ad-8acd-51420f3aebff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xTPr7axTjv8wa3nNjDhBy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21803,
      "cache_read_input_tokens": 44399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21803
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

_source line 30 · 2026-05-18T20:18:50.098Z_

<details><summary>↩ Tool result · `toolu_018rBxEBvYJL8EFM9PJZj4uY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "19ff78b9-5058-4fec-aa80-457cd35fca16",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "content": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?\n\n\\subsection{Environment}\n\\label{sec:environment}\n\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.\n\nALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.\n\n\\subsection{Base Model and Supervised Fine-Tuning}\n\\label{sec:base_model}\n\nWe use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n\nThis low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.\n\n\\subsection{RL Training Configuration}\n\\label{sec:rl_config}\n\nAll conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Shared RL training hyperparameters across all conditions.}\n\\label{tab:hyperparameters}\n\\begin{tabular}{lc}\n\\toprule\nParameter & Value \\\\\n\\midrule\nGroup size $K$ & 8 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nKL penalty $\\beta$ & 0.01 \\\\\nDiscount $\\gamma$ & 0.95 \\\\\nInvalid action penalty & 0.1 \\\\\nTasks per training step & 16 \\\\\nTraining steps & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.\n\nThe primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. All results are single-seed unless stated otherwise; two-seed replication is reported where available.\n\n\\subsection{Experimental Conditions}\n\\label{sec:conditions}\n\nWe evaluate seven conditions organized around three designs: factorial mechanism separation (Conditions~1--3), auxiliary baselines (Conditions~4--5), and parameter sweeps (Conditions~6--7).\n\n\\paragraph{Condition 1: Episode-level GRPO.}\nEach complete trajectory serves as a single GRPO sample with one shared advantage for all tokens. Both failure mechanisms are absent: the full context is preserved (no M1) and no per-window advantage can carry misattributed sign (no M2). Two seeds.\n\n\\paragraph{Condition 2: Step-independent $h{=}2$.}\nEach trajectory is segmented into fixed windows of $h = 2$ interaction steps, with each window receiving its own GRPO advantage. Both M1 (truncated context) and M2 (advantage sign determined by episode outcome rather than local action quality) are active. This is the default RAGEN configuration and represents the standard approach for multi-turn agent RL. Two seeds.\n\n\\paragraph{Condition 3: Step-independent $h{=}2$ with episode advantage.}\nThe factorial complement. Windows are constructed identically to Condition~2, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign assignment). The performance gap between Conditions~2 and~3 is therefore attributable to M2 alone. Two seeds.\n\nConditions~1--3 form a $2 \\times 2$ factorial design over observation scope (windowed vs.\\ full) and advantage scope (per-window vs.\\ episode-level), as described in Section~\\ref{sec:factorial_design}. The fourth cell (full observation with per-window advantage) is degenerate: with full context, only one window exists per episode, so per-window and episode-level advantage coincide.\n\n\\paragraph{Condition 4: Dense reward.}\nStep-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.\n\n\\paragraph{Condition 5: REINFORCE++ baseline.}\nEpisode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used. This condition was originally planned as a GAE baseline with a learned critic; we substituted REINFORCE++ after TRL~1.1.0 removed the required \\texttt{AutoModelForCausalLMWithValueHead} class.\n\n\\paragraph{Condition 6: Discount factor sweep.}\nStep-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. At $\\gamma = 1.0$, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains. Collapse at $\\gamma = 1.0$ would confirm that sign misattribution alone suffices to cause failure, independent of discount-induced magnitude variation.\n\n\\paragraph{Condition 7: Window-size sweep.}\nStep-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.\n\n\\subsection{Results}\n\\label{sec:results}\n\nResults are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size and discount-factor ablations (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 120,
        "newStart": 3,
        "newLines": 83,
        "lines": [
          " \\section{Experiments}",
          " \\label{sec:experiments}",
          " ",
          "-We design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\\ref{sec:m2_sign_misattribution}?",
          "+We design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?",
          " ",
          "-\\subsection{Experimental Setup}",
          "-\\label{sec:experimental_setup}",
          "+\\subsection{Environment}",
          "+\\label{sec:environment}",
          " ",
          "-\\paragraph{Environment.}",
          "-We evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands.",
          "-ALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ for successful task completion and $0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.",
          "+We evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.",
          " ",
          "-ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.",
          "+ALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.",
          " ",
          "-\\paragraph{Base model.}",
          "-We use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-episode validation set (4/32 episodes), providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.125$ with group size $K = 8$, Proposition 2 (Section~\\ref{sec:formal_probability}) predicts that approximately 80.9\\% of gradient updates carry incorrect sign under step-independent training.",
          "+\\subsection{Base Model and Supervised Fine-Tuning}",
          "+\\label{sec:base_model}",
          " ",
          "-\\paragraph{RL training configuration.}",
          "-We train using the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:",
          "-\\begin{itemize}",
          "-    \\item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)",
          "-    \\item Learning rate: $1 \\times 10^{-6}$",
          "-    \\item KL penalty coefficient: $\\beta = 0.01$ (low-variance KL)",
          "-    \\item Discount factor: $\\gamma = 0.95$ (applied in step-independent return computation via Equation~\\ref{eq:step_return}; not applicable to episode-level mode)",
          "-    \\item Invalid action penalty coefficient: 0.1",
          "-    \\item Training data: 16 task instances per training step",
          "-    \\item Training steps: 15 (early-stopped based on convergence)",
          "-\\end{itemize}",
          "+We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.",
          " ",
          "-\\paragraph{Evaluation protocol.}",
          "-We evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \\in \\{2, 4, 8\\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \\textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.",
          "+This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.",
          " ",
          "-\\subsection{Window-Size Ablation}",
          "-\\label{sec:window_ablation}",
          "+\\subsection{RL Training Configuration}",
          "+\\label{sec:rl_config}",
          " ",
          "-To disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.",
          "+All conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.",
          " ",
          "-\\paragraph{Conditions.}",
          "-We vary the step-independent history length $h \\in \\{2, 5, 10, 20\\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \\texttt{step\\_independent} training mode with \\texttt{step\\_independent\\_history\\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{Shared RL training hyperparameters across all conditions.}",
          "+\\label{tab:hyperparameters}",
          "+\\begin{tabular}{lc}",
          "+\\toprule",
          "+Parameter & Value \\\\",
          "+\\midrule",
          "+Group size $K$ & 8 \\\\",
          "+Learning rate & $1 \\times 10^{-6}$ \\\\",
          "+KL penalty $\\beta$ & 0.01 \\\\",
          "+Discount $\\gamma$ & 0.95 \\\\",
          "+Invalid action penalty & 0.1 \\\\",
          "+Tasks per training step & 16 \\\\",
          "+Training steps & 15 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          " ",
          "-\\paragraph{Design rationale.}",
          "-The five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.",
          "+\\subsection{Evaluation Protocol}",
          "+\\label{sec:eval_protocol}",
          " ",
          "-\\paragraph{Controls.}",
          "-All conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. \\placeholder{plan\\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}",
          "+We evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.",
          " ",
          "-\\paragraph{Post-hoc evaluation.}",
          "-To isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).",
          "+The primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. All results are single-seed unless stated otherwise; two-seed replication is reported where available.",
          " ",
          "-\\subsection{Results}",
          "-\\label{sec:results}",
          "+\\subsection{Experimental Conditions}",
          "+\\label{sec:conditions}",
          " ",
          "-\\subsubsection{Episode-Level vs. Step-Independent Training}",
          "-\\label{sec:results_main}",
          "+We evaluate seven conditions organized around three designs: factorial mechanism separation (Conditions~1--3), auxiliary baselines (Conditions~4--5), and parameter sweeps (Conditions~6--7).",
          " ",
          "-The central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\\% validation success at training step 15, a 2.25$\\times$ improvement over the SFT baseline of 12.5\\%. Step-independent training with $h = 2$ collapses to 0\\% training success by step 11.",
          "+\\paragraph{Condition 1: Episode-level GRPO.}",
          "+Each complete trajectory serves as a single GRPO sample with one shared advantage for all tokens. Both failure mechanisms are absent: the full context is preserved (no M1) and no per-window advantage can carry misattributed sign (no M2). Two seeds.",
          " ",
          "-\\placeholder{tab1\\_main\\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\\%), Action Valid (\\%), Pass@8. Multi-seed mean$\\pm$std from plan\\_003.}",
          "+\\paragraph{Condition 2: Step-independent $h{=}2$.}",
          "+Each trajectory is segmented into fixed windows of $h = 2$ interaction steps, with each window receiving its own GRPO advantage. Both M1 (truncated context) and M2 (advantage sign determined by episode outcome rather than local action quality) are active. This is the default RAGEN configuration and represents the standard approach for multi-turn agent RL. Two seeds.",
          " ",
          "-\\placeholder{fig6\\_training\\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}",
          "+\\paragraph{Condition 3: Step-independent $h{=}2$ with episode advantage.}",
          "+The factorial complement. Windows are constructed identically to Condition~2, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign assignment). The performance gap between Conditions~2 and~3 is therefore attributable to M2 alone. Two seeds.",
          " ",
          "-The collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), training success drops from 18.75\\% to single digits while training action validity remains high at approximately 89.3\\% (training, step 2). The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), training action validity itself collapses from 89.3\\% to 43.1\\% (training, steps 2$\\to$4). Note that training success (computed from rollouts during optimization) differs from validation success (pass@1 on the held-out 32-episode set evaluated every 5 steps); the 18.75\\% training success at step 0 reflects the SFT checkpoint's performance across the training task distribution. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.",
          "+Conditions~1--3 form a $2 \\times 2$ factorial design over observation scope (windowed vs.\\ full) and advantage scope (per-window vs.\\ episode-level), as described in Section~\\ref{sec:factorial_design}. The fourth cell (full observation with per-window advantage) is degenerate: with full context, only one window exists per episode, so per-window and episode-level advantage coincide.",
          " ",
          "-Episode-level training exhibits no such collapse. Success rate shows consistent improvement from the SFT baseline to 28.1\\% at step 15, with action validity at 54.5\\%. This pattern is consistent with the policy acquiring task-solving strategies that operate outside the predefined action template vocabulary. Notably, task success (the primary objective) improves despite lower template compliance, suggesting the model develops effective but syntactically unconventional action sequences. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.",
          "+\\paragraph{Condition 4: Dense reward.}",
          "+Step-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.",
          " ",
          "-\\subsubsection{Window-Size Ablation}",
          "-\\label{sec:results_hsweep}",
          "+\\paragraph{Condition 5: REINFORCE++ baseline.}",
          "+Episode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used. This condition was originally planned as a GAE baseline with a learned critic; we substituted REINFORCE++ after TRL~1.1.0 removed the required \\texttt{AutoModelForCausalLMWithValueHead} class.",
          " ",
          "-\\placeholder{tab2\\_h\\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \\in \\{2, 5, 10, 20, \\text{full}\\}$, 3 seeds per $h$.}",
          "+\\paragraph{Condition 6: Discount factor sweep.}",
          "+Step-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. At $\\gamma = 1.0$, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains. Collapse at $\\gamma = 1.0$ would confirm that sign misattribution alone suffices to cause failure, independent of discount-induced magnitude variation.",
          " ",
          "-\\placeholder{fig5\\_h\\_sweep\\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (12.5\\%).}",
          "+\\paragraph{Condition 7: Window-size sweep.}",
          "+Step-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.",
          " ",
          "-The ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.",
          "+\\subsection{Results}",
          "+\\label{sec:results}",
          " ",
          "-The dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.",
          "-",
          "-From the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Training action validity at step 2 is 89.3\\%, dropping to 43.1\\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.",
          "-",
          "-\\subsubsection{Dense Reward Baseline}",
          "-\\label{sec:results_dense}",
          "-",
          "-A natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.",
          "-",
          "-The dense reward baseline produces a clear dissociation. Action validity increases from 60\\% to 97.5\\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, validation success remains at 0\\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.",
          "-",
          "-This result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.",
          "-",
          "-\\subsection{Empirical Verification of Sign Misattribution}",
          "-\\label{sec:sign_verification}",
          "-",
          "-The theoretical analysis of Section~\\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions. Crucially, the empirical verification uses the full reward structure including invalid action penalties (coefficient 0.1), not the simplified binary reward assumed by Proposition~2. Confirmation under non-binary rewards strengthens the generality of the sign misattribution mechanism beyond the analytical assumptions.",
          "-",
          "-\\paragraph{Methodology.}",
          "-During step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\\text{sign}(\\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\\text{episode}}^{(i)} \\in \\{0, 1\\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:",
          "-\\begin{itemize}",
          "-    \\item \\textbf{Sign-outcome correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and $R_{\\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.",
          "-    \\item \\textbf{Sign-quality correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.",
          "-    \\item \\textbf{Correct sign fraction}: $P(\\text{correct sign} \\mid \\text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\\ref{sec:formal_probability}) predicts this equals approximately 19.1\\% at $p = 12.5\\%$, $K = 8$.",
          "-\\end{itemize}",
          "-",
          "-\\paragraph{Predictions.}",
          "-The sign misattribution mechanism makes three testable predictions:",
          "-\\begin{enumerate}",
          "-    \\item Sign-outcome correlation $\\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)",
          "-    \\item Sign-quality correlation $\\approx 0$ (advantage sign is independent of whether local actions were good)",
          "-    \\item $P(\\text{correct sign}) \\approx 19.1\\%$ (derived from Proposition 2 at the observed success rate)",
          "-\\end{enumerate}",
          "-If all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.",
          "-",
          "-\\placeholder{tab3\\_mechanism\\_verification: Sign misattribution empirical verification. Columns: Metric, Measured Value, Theoretical Prediction, Agreement. Rows: sign-outcome correlation, sign-quality correlation, $P(\\text{correct sign})$. Data from plan\\_004 per-window advantage logging.}",
          "-",
          "-\\subsection{Additional Baselines}",
          "-\\label{sec:additional_baselines}",
          "-",
          "-\\paragraph{GAE baselines.}",
          "-To distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} under two configurations. GAE($\\lambda = 0.95$, $\\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\\lambda = 1$, $\\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \\placeholder{plan\\_003b: GAE baseline execution. Columns: Method, Val Success (\\%), Action Valid (\\%), Training Stability (variance across steps).}",
          "-",
          "-\\paragraph{Selective verification.}",
          "-\\label{sec:selective_experiments}",
          "-Building on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we propose training a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and would demonstrate a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}",
          "+Results are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size and discount-factor ablations (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}"
        ]
      }
    ],
    "originalFile": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to answer three questions. First, does step-independent training collapse as predicted by our dual mechanism analysis, and does episode-level training avoid this collapse? Second, how does the window size $h$ modulate the severity of failure, and is there a credit assignment cliff below some critical threshold? Third, can we directly measure advantage sign misattribution during training to validate the theoretical predictions of Section~\\ref{sec:m2_sign_misattribution}?\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\n\\paragraph{Environment.}\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment where an agent interacts with a simulated kitchen, bedroom, and living room through natural language commands.\nALFWorld provides six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., ``go to countertop 1'', ``take knife 2 from drawer 3'') and receives textual observations describing the environment state. Episodes terminate after task completion or a maximum of 50 interaction steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ for successful task completion and $0$ for failure. This binary reward structure makes ALFWorld a particularly challenging testbed for credit assignment: the only learning signal arrives at episode termination, and intermediate steps receive no direct feedback.\n\nALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement action has no access to the exploration steps that determined which object to pick up.\n\n\\paragraph{Base model.}\nWe use Qwen3-1.7B (instruct variant) as the policy model. Before RL training, we perform supervised fine-tuning (SFT) on 2546 expert demonstrations collected from ALFWorld, training for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-episode validation set (4/32 episodes), providing a minimal but non-trivial starting point for RL. This low baseline success rate is important for our analysis: at $p = 0.125$ with group size $K = 8$, Proposition 2 (Section~\\ref{sec:formal_probability}) predicts that approximately 80.9\\% of gradient updates carry incorrect sign under step-independent training.\n\n\\paragraph{RL training configuration.}\nWe train using the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm. The shared hyperparameters across all conditions are:\n\\begin{itemize}\n    \\item Group size $K = 8$ (8 rollouts per task instance for advantage estimation)\n    \\item Learning rate: $1 \\times 10^{-6}$\n    \\item KL penalty coefficient: $\\beta = 0.01$ (low-variance KL)\n    \\item Discount factor: $\\gamma = 0.95$ (applied in step-independent return computation via Equation~\\ref{eq:step_return}; not applicable to episode-level mode)\n    \\item Invalid action penalty coefficient: 0.1\n    \\item Training data: 16 task instances per training step\n    \\item Training steps: 15 (early-stopped based on convergence)\n\\end{itemize}\n\n\\paragraph{Evaluation protocol.}\nWe evaluate on a fixed 32-episode validation set every 5 training steps. The primary metric is success rate (pass@1): the fraction of episodes where the agent completes the task within 50 steps. We also report pass@$k$ ($k \\in \\{2, 4, 8\\}$), computed by sampling $k$ rollouts per episode and counting success if any rollout succeeds. As a diagnostic metric, we track \\textit{action validity rate}: the fraction of agent outputs that are syntactically valid environment commands (as opposed to malformed text, repeated outputs, or empty responses). Action validity serves as a proxy for basic policy coherence, distinct from task-solving capability. All reported numbers are single-seed unless otherwise noted; multi-seed results (3 seeds per condition) are marked as pending where applicable.\n\n\\subsection{Window-Size Ablation}\n\\label{sec:window_ablation}\n\nTo disentangle the effects of information loss (Mechanism 1) and sign misattribution (Mechanism 2) across different context lengths, we conduct a systematic ablation over window size $h$.\n\n\\paragraph{Conditions.}\nWe vary the step-independent history length $h \\in \\{2, 5, 10, 20\\}$ and compare against episode-level training (equivalent to $h = T$, the full trajectory). Each condition uses the \\texttt{step\\_independent} training mode with \\texttt{step\\_independent\\_history\\_length} $= h$, except the episode-level condition which processes the complete trajectory as a single GRPO sample.\n\n\\paragraph{Design rationale.}\nThe five conditions span the spectrum from minimal context ($h = 2$, producing $N = 25$ windows per episode at $T = 50$) to full context ($h = T$, one sample per episode). Theory predicts two observable effects. Mechanism 1 (information loss) produces a performance ceiling that varies with $h$: smaller windows restrict the representable strategy space more severely, so step-1 performance should decrease monotonically with $h$. Mechanism 2 (sign misattribution) produces a training-time degradation that is present for all $h < T$: as long as windows exist, the advantage sign is determined by episode outcome rather than local action quality, so performance should decline over training steps regardless of window size. The combined prediction is a credit assignment cliff: performance drops sharply below a critical $h$ value, with smaller $h$ exhibiting both lower initial performance and faster collapse.\n\n\\paragraph{Controls.}\nAll conditions share the same GRPO hyperparameters (group size, learning rate, KL penalty, discount factor). Each condition runs for 15 training steps with validation every 5 steps. We plan 3 seeds per $h$ value to assess variance. \\placeholder{plan\\_002: 3-seed h-sweep execution status. Currently single-seed for h=2 (exp028c) and episode-level (exp029).}\n\n\\paragraph{Post-hoc evaluation.}\nTo isolate the training-layer effect of sign misattribution from the inference-layer effect of context truncation, we conduct full-context evaluation of checkpoints trained with truncated windows. Concretely, a model trained with $h = 2$ is evaluated using the complete interaction history at inference time. If the trained model performs better under full-context evaluation than under $h = 2$ evaluation, the difference reflects pure inference-time information loss (Mechanism 1). If it still performs worse than the episode-level trained model even under full-context evaluation, the gap reflects training-layer damage from sign misattribution (Mechanism 2).\n\n\\subsection{Results}\n\\label{sec:results}\n\n\\subsubsection{Episode-Level vs. Step-Independent Training}\n\\label{sec:results_main}\n\nThe central empirical finding is the contrast between episode-level and step-independent training. Episode-level GRPO achieves 28.125\\% validation success at training step 15, a 2.25$\\times$ improvement over the SFT baseline of 12.5\\%. Step-independent training with $h = 2$ collapses to 0\\% training success by step 11.\n\n\\placeholder{tab1\\_main\\_results: Episode-level vs step-independent comparison. Columns: Method, $h$-value, Val Success (\\%), Action Valid (\\%), Pass@8. Multi-seed mean$\\pm$std from plan\\_003.}\n\n\\placeholder{fig6\\_training\\_curves: Training curves showing episode-level vs step-independent $h=2$. Dual y-axis: success rate (left) and action validity (right). X-axis: training steps 0--15.}\n\nThe collapse under step-independent training follows the two-phase pattern predicted by our analysis. In the first phase (steps 0--2), training success drops from 18.75\\% to single digits while training action validity remains high at approximately 89.3\\% (training, step 2). The model retains basic command formatting but loses the ability to compose multi-step strategies. In the second phase (steps 2--4), training action validity itself collapses from 89.3\\% to 43.1\\% (training, steps 2$\\to$4). Note that training success (computed from rollouts during optimization) differs from validation success (pass@1 on the held-out 32-episode set evaluated every 5 steps); the 18.75\\% training success at step 0 reflects the SFT checkpoint's performance across the training task distribution. Accumulated wrong-sign gradient updates, which initially eroded only strategic capability, propagate to corrupt the action space representation. By step 10, the agent produces predominantly malformed outputs and achieves no task completions.\n\nEpisode-level training exhibits no such collapse. Success rate shows consistent improvement from the SFT baseline to 28.1\\% at step 15, with action validity at 54.5\\%. This pattern is consistent with the policy acquiring task-solving strategies that operate outside the predefined action template vocabulary. Notably, task success (the primary objective) improves despite lower template compliance, suggesting the model develops effective but syntactically unconventional action sequences. The single advantage shared across all steps in an episode preserves correct actions even within failed episodes (since all steps receive the same sign, no individual step is singled out for incorrect suppression). Cross-step dependencies are maintained through the full interaction history, so the model can learn conditional strategies that require information from early exploration steps.\n\n\\subsubsection{Window-Size Ablation}\n\\label{sec:results_hsweep}\n\n\\placeholder{tab2\\_h\\_sweep: $h$-sweep ablation results. Columns: $h$, Seed 1/2/3, Mean$\\pm$Std, Collapse Step (first step where val success $= 0$). Rows: $h \\in \\{2, 5, 10, 20, \\text{full}\\}$, 3 seeds per $h$.}\n\n\\placeholder{fig5\\_h\\_sweep\\_curve: $h$ vs. validation success at step 15. Error bars from 3 seeds. Shows credit assignment cliff. Horizontal dashed line at SFT baseline (12.5\\%).}\n\nThe ablation reveals a credit assignment cliff consistent with our theoretical predictions. We describe the expected pattern below; precise numbers await multi-seed completion.\n\nThe dual mechanism theory predicts three observable signatures in the $h$-sweep. First, step-1 performance should vary across $h$ values, reflecting different information-loss ceilings (Mechanism 1). Second, for all $h < T$, performance should decline over training steps as sign misattribution accumulates (Mechanism 2). Third, the rate of decline should be approximately constant across $h$ values (since the sign correlation from Equation~\\ref{eq:sign_correlation} depends on the success rate $p$ and group size $K$, not on $h$ directly), but the onset of visible collapse should be earlier for smaller $h$ because the lower ceiling leaves less room before reaching zero.\n\nFrom the single-seed data available, the two-phase collapse at $h = 2$ is confirmed. Training action validity at step 2 is 89.3\\%, dropping to 43.1\\% by step 4. This pattern, strategic collapse preceding formatting collapse, is the empirical signature of sign misattribution operating on a model that initially retains valid action representations. The progressive nature distinguishes Mechanism 2 from Mechanism 1: information loss would produce a constant (low) performance from step 1, not a declining trajectory.\n\n\\subsubsection{Dense Reward Baseline}\n\\label{sec:results_dense}\n\nA natural hypothesis is that step-independent training fails due to sparse reward, and that providing dense per-step rewards might resolve the credit assignment problem. We test this with a dense reward configuration that adds $+0.15$ bonus for each syntactically valid action, applied under step-independent training with $h = 2$.\n\nThe dense reward baseline produces a clear dissociation. Action validity increases from 60\\% to 97.5\\% over training. The per-step bonus successfully shapes low-level formatting behavior. However, validation success remains at 0\\% throughout training. The agent learns to produce perfectly formatted commands that satisfy the validity reward without solving any tasks.\n\nThis result confirms that the failure of step-independent training is not a sparse reward problem. Dense reward shaping creates an optimization target that the agent can maximize (action formatting) without addressing the underlying credit assignment pathology. The sign of the task-level advantage still corrupts multi-step strategy learning, while the dense reward merely teaches the agent to produce syntactically correct (but strategically meaningless) outputs. Reward shaping and sign misattribution operate on different dimensions of behavior and cannot compensate for each other.\n\n\\subsection{Empirical Verification of Sign Misattribution}\n\\label{sec:sign_verification}\n\nThe theoretical analysis of Section~\\ref{sec:m2_sign_misattribution} predicts specific quantitative properties of the advantage signal under step-independent training. We design a direct measurement protocol to validate these predictions. Crucially, the empirical verification uses the full reward structure including invalid action penalties (coefficient 0.1), not the simplified binary reward assumed by Proposition~2. Confirmation under non-binary rewards strengthens the generality of the sign misattribution mechanism beyond the analytical assumptions.\n\n\\paragraph{Methodology.}\nDuring step-independent training, we log per-window advantage information for each training episode. For window $k$ in episode $i$, we record: (1) the advantage sign $\\text{sign}(\\hat{A}_k^{(i)})$, (2) the episode outcome $R_{\\text{episode}}^{(i)} \\in \\{0, 1\\}$, and (3) a local action quality proxy based on the fraction of valid actions within the window. We then compute three statistics across all training windows:\n\\begin{itemize}\n    \\item \\textbf{Sign-outcome correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and $R_{\\text{episode}}$. Theory predicts this correlation approaches 1.0, since the advantage sign is determined almost entirely by whether the episode succeeded.\n    \\item \\textbf{Sign-quality correlation}: the Pearson correlation between $\\text{sign}(\\hat{A}_k)$ and local action quality. Theory predicts this correlation approaches 0, since the advantage sign carries no information about whether the window's actions were locally correct.\n    \\item \\textbf{Correct sign fraction}: $P(\\text{correct sign} \\mid \\text{update})$, defined as the probability that a window with locally good actions receives a positive advantage and a window with locally bad actions receives a negative advantage. Proposition 2 (Section~\\ref{sec:formal_probability}) predicts this equals approximately 19.1\\% at $p = 12.5\\%$, $K = 8$.\n\\end{itemize}\n\n\\paragraph{Predictions.}\nThe sign misattribution mechanism makes three testable predictions:\n\\begin{enumerate}\n    \\item Sign-outcome correlation $\\approx 1.0$ (advantage sign is a proxy for episode success, not local quality)\n    \\item Sign-quality correlation $\\approx 0$ (advantage sign is independent of whether local actions were good)\n    \\item $P(\\text{correct sign}) \\approx 19.1\\%$ (derived from Proposition 2 at the observed success rate)\n\\end{enumerate}\nIf all three predictions are confirmed empirically, the sign misattribution mechanism is validated as the causal driver of training collapse, rather than alternative explanations such as reward sparsity, KL divergence, or optimization instability.\n\n\\placeholder{tab3\\_mechanism\\_verification: Sign misattribution empirical verification. Columns: Metric, Measured Value, Theoretical Prediction, Agreement. Rows: sign-outcome correlation, sign-quality correlation, $P(\\text{correct sign})$. Data from plan\\_004 per-window advantage logging.}\n\n\\subsection{Additional Baselines}\n\\label{sec:additional_baselines}\n\n\\paragraph{GAE baselines.}\nTo distinguish the effect of episode-level optimization from GRPO-specific design choices (group normalization, no value function), we compare against Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} under two configurations. GAE($\\lambda = 0.95$, $\\gamma = 0.95$) provides standard TD-based advantage estimation with a learned value function, representing the conventional actor-critic approach to temporal credit assignment. GAE($\\lambda = 1$, $\\gamma = 1$) computes Monte Carlo returns equivalent to episode-level GRPO without group normalization, isolating the contribution of group-relative advantage computation. \\placeholder{plan\\_003b: GAE baseline execution. Columns: Method, Val Success (\\%), Action Valid (\\%), Training Stability (variance across steps).}\n\n\\paragraph{Selective verification.}\n\\label{sec:selective_experiments}\nBuilding on the episode-level trained agent (Section~\\ref{sec:selective_verification}), we propose training a selective verification policy that decides when self-checking is informative. This component is orthogonal to the credit assignment analysis and would demonstrate a downstream application of the competent base agent produced by episode-level training. \\placeholder{tab4\\_selective\\_comparison: Selective verification results. Columns: Method (Always-Verify, Never-Verify, Selective), Success (\\%), Verify Rate (\\%), Cost Reduction (\\%). Pending Phase B experiments.}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 31_

Now let me verify the file and check for forbidden patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "905edf1c-3e56-49a2-870c-89c08a564817",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWvspFayjoGTzCTsp8YPA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21109,
      "cache_read_input_tokens": 66202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21109
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01JMiNEZSiZx7otka9mPeMLi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "058cf49a-ed44-479e-94a0-dda8b3ed8fe8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWvspFayjoGTzCTsp8YPA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21109,
      "cache_read_input_tokens": 66202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21109
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

_source line 33 · 2026-05-18T20:18:54.017Z_

<details><summary>↩ Tool result · `toolu_01JMiNEZSiZx7otka9mPeMLi`</summary>

```text
1	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	We design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?
7	
8	\subsection{Environment}
9	\label{sec:environment}
10	
11	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \texttt{go to countertop 1}, \texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \in \{0, r_+\}$, with $r_+$ awarded only upon successful task completion.
12	
13	ALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.
14	
15	\subsection{Base Model and Supervised Fine-Tuning}
16	\label{sec:base_model}
17	
18	We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.
19	
20	This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\ref{prop:correct_sign} predicts that approximately 80.9\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.
21	
22	\subsection{RL Training Configuration}
23	\label{sec:rl_config}
24	
25	All conditions use the RAGEN framework~\cite{ragen2025} with the GRPO algorithm~\cite{shao2024deepseekmath}. Table~\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\gamma$ applies only to step-independent return computation (Equation~\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\caption{Shared RL training hyperparameters across all conditions.}
31	\label{tab:hyperparameters}
32	\begin{tabular}{lc}
33	\toprule
34	Parameter & Value \\
35	\midrule
36	Group size $K$ & 8 \\
37	Learning rate & $1 \times 10^{-6}$ \\
38	KL penalty $\beta$ & 0.01 \\
39	Discount $\gamma$ & 0.95 \\
40	Invalid action penalty & 0.1 \\
41	Tasks per training step & 16 \\
42	Training steps & 15 \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	\subsection{Evaluation Protocol}
48	\label{sec:eval_protocol}
49	
50	We evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.
51	
52	The primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \in \{2, 4, 8\}$. As a diagnostic, we track \textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. All results are single-seed unless stated otherwise; two-seed replication is reported where available.
53	
54	\subsection{Experimental Conditions}
55	\label{sec:conditions}
56	
57	We evaluate seven conditions organized around three designs: factorial mechanism separation (Conditions~1--3), auxiliary baselines (Conditions~4--5), and parameter sweeps (Conditions~6--7).
58	
59	\paragraph{Condition 1: Episode-level GRPO.}
60	Each complete trajectory serves as a single GRPO sample with one shared advantage for all tokens. Both failure mechanisms are absent: the full context is preserved (no M1) and no per-window advantage can carry misattributed sign (no M2). Two seeds.
61	
62	\paragraph{Condition 2: Step-independent $h{=}2$.}
63	Each trajectory is segmented into fixed windows of $h = 2$ interaction steps, with each window receiving its own GRPO advantage. Both M1 (truncated context) and M2 (advantage sign determined by episode outcome rather than local action quality) are active. This is the default RAGEN configuration and represents the standard approach for multi-turn agent RL. Two seeds.
64	
65	\paragraph{Condition 3: Step-independent $h{=}2$ with episode advantage.}
66	The factorial complement. Windows are constructed identically to Condition~2, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign assignment). The performance gap between Conditions~2 and~3 is therefore attributable to M2 alone. Two seeds.
67	
68	Conditions~1--3 form a $2 \times 2$ factorial design over observation scope (windowed vs.\ full) and advantage scope (per-window vs.\ episode-level), as described in Section~\ref{sec:factorial_design}. The fourth cell (full observation with per-window advantage) is degenerate: with full context, only one window exists per episode, so per-window and episode-level advantage coincide.
69	
70	\paragraph{Condition 4: Dense reward.}
71	Step-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.
72	
73	\paragraph{Condition 5: REINFORCE++ baseline.}
74	Episode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used. This condition was originally planned as a GAE baseline with a learned critic; we substituted REINFORCE++ after TRL~1.1.0 removed the required \texttt{AutoModelForCausalLMWithValueHead} class.
75	
76	\paragraph{Condition 6: Discount factor sweep.}
77	Step-independent $h{=}5$ with $\gamma \in \{0.50, 0.80, 0.95, 1.00\}$. At $\gamma = 1.0$, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains. Collapse at $\gamma = 1.0$ would confirm that sign misattribution alone suffices to cause failure, independent of discount-induced magnitude variation.
78	
79	\paragraph{Condition 7: Window-size sweep.}
80	Step-independent training with $h \in \{2, 5, 10, 20\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \in \{10, 20\}$ is in progress.
81	
82	\subsection{Results}
83	\label{sec:results}
84	
85	Results are organized around three comparisons: (1)~episode-level vs.\ step-independent training dynamics (Section~\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\ref{sec:results_factorial}), and (3)~window-size and discount-factor ablations (Section~\ref{sec:results_hsweep}). \placeholder{Results sections to follow.}
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "9d3c1116-f0bb-424b-93a4-f019ff13406a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
      "content": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?\n\n\\subsection{Environment}\n\\label{sec:environment}\n\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.\n\nALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.\n\n\\subsection{Base Model and Supervised Fine-Tuning}\n\\label{sec:base_model}\n\nWe use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n\nThis low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.\n\n\\subsection{RL Training Configuration}\n\\label{sec:rl_config}\n\nAll conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Shared RL training hyperparameters across all conditions.}\n\\label{tab:hyperparameters}\n\\begin{tabular}{lc}\n\\toprule\nParameter & Value \\\\\n\\midrule\nGroup size $K$ & 8 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nKL penalty $\\beta$ & 0.01 \\\\\nDiscount $\\gamma$ & 0.95 \\\\\nInvalid action penalty & 0.1 \\\\\nTasks per training step & 16 \\\\\nTraining steps & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.\n\nThe primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. All results are single-seed unless stated otherwise; two-seed replication is reported where available.\n\n\\subsection{Experimental Conditions}\n\\label{sec:conditions}\n\nWe evaluate seven conditions organized around three designs: factorial mechanism separation (Conditions~1--3), auxiliary baselines (Conditions~4--5), and parameter sweeps (Conditions~6--7).\n\n\\paragraph{Condition 1: Episode-level GRPO.}\nEach complete trajectory serves as a single GRPO sample with one shared advantage for all tokens. Both failure mechanisms are absent: the full context is preserved (no M1) and no per-window advantage can carry misattributed sign (no M2). Two seeds.\n\n\\paragraph{Condition 2: Step-independent $h{=}2$.}\nEach trajectory is segmented into fixed windows of $h = 2$ interaction steps, with each window receiving its own GRPO advantage. Both M1 (truncated context) and M2 (advantage sign determined by episode outcome rather than local action quality) are active. This is the default RAGEN configuration and represents the standard approach for multi-turn agent RL. Two seeds.\n\n\\paragraph{Condition 3: Step-independent $h{=}2$ with episode advantage.}\nThe factorial complement. Windows are constructed identically to Condition~2, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign assignment). The performance gap between Conditions~2 and~3 is therefore attributable to M2 alone. Two seeds.\n\nConditions~1--3 form a $2 \\times 2$ factorial design over observation scope (windowed vs.\\ full) and advantage scope (per-window vs.\\ episode-level), as described in Section~\\ref{sec:factorial_design}. The fourth cell (full observation with per-window advantage) is degenerate: with full context, only one window exists per episode, so per-window and episode-level advantage coincide.\n\n\\paragraph{Condition 4: Dense reward.}\nStep-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.\n\n\\paragraph{Condition 5: REINFORCE++ baseline.}\nEpisode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used. This condition was originally planned as a GAE baseline with a learned critic; we substituted REINFORCE++ after TRL~1.1.0 removed the required \\texttt{AutoModelForCausalLMWithValueHead} class.\n\n\\paragraph{Condition 6: Discount factor sweep.}\nStep-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. At $\\gamma = 1.0$, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains. Collapse at $\\gamma = 1.0$ would confirm that sign misattribution alone suffices to cause failure, independent of discount-induced magnitude variation.\n\n\\paragraph{Condition 7: Window-size sweep.}\nStep-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.\n\n\\subsection{Results}\n\\label{sec:results}\n\nResults are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size and discount-factor ablations (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_01FSabBy2J4bzYh2McEFhm4X`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "481c8eae-7d17-4f59-8bf2-d14f0f505909",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWvspFayjoGTzCTsp8YPA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21109,
      "cache_read_input_tokens": 66202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21109
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

_source line 35 · 2026-05-18T20:18:54.806Z_

<details><summary>↩ Tool result · `toolu_01FSabBy2J4bzYh2McEFhm4X`</summary>

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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "03b40cac-6e5c-4bf6-8eb4-cb873c69a68d",
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

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_0136CTiRSggGAA1BzoqTZYaV`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "b4f561df-6899-40be-86e7-368eb43d3420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWvspFayjoGTzCTsp8YPA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21109,
      "cache_read_input_tokens": 66202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21109
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

_source line 37 · 2026-05-18T20:18:55.836Z_

<details><summary>↩ Tool result · `toolu_0136CTiRSggGAA1BzoqTZYaV`</summary>

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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "cdadf7c2-19e3-4ed1-a380-b15fb0eddf3b",
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

<details open><summary>🔧 Tool call — Grep · `toolu_01V9K4KJj6HtdboHj7nKxeSm`</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "f3b7c18b-3486-462d-8ada-7965e725e0a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWvspFayjoGTzCTsp8YPA2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21109,
      "cache_read_input_tokens": 66202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21109
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

_source line 39 · 2026-05-18T20:18:58.217Z_

<details><summary>↩ Tool result · `toolu_01V9K4KJj6HtdboHj7nKxeSm`</summary>

```text
18:We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.
20:This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\ref{prop:correct_sign} predicts that approximately 80.9\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "e2101163-664c-4061-92a1-55a1597320fe",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "18:We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n20:This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
The grep for "ing[,.]" found two lines. Let me check for -ing phrase endings specifically:

Line 18: "...fine-tuning (SFT)..." - "tuning" is part of a compound noun "fine-tuning", not a trailing participial phrase. "...resulting SFT checkpoint..." - "resulting" is an adjective. These are fine.

Line 20: "...producing a stringent test of the mechanism." - This IS a trailing participial phrase at the end of a sentence. I should fix this.

Let me rephrase line 20: "The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, which makes it a stringent test of the mechanism." Hmm, that adds a "which" clause. 

I could combine it as "The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal and provides a stringent test of the mechanism." Or restructure it more sharply: "The SFT checkpoint thus sits in the regime of near-maximal sign misattribution, and any training collapse is predicted to be rapid." Actually, the simplest fix is just "The SFT checkpoint therefore occupies the regime where sign misattribution is most severe." Let me go with that.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "526b2c89-3bdb-4000-bbca-9630383c7a69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bFftRehdLqSMdfRnPaKNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3143,
      "cache_read_input_tokens": 87311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3143
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

_source line 41_

Line 20 has a trailing "-ing" phrase ("producing a stringent test"). Let me fix it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "c5be194b-0d26-4be4-be63-0fbd70499fa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bFftRehdLqSMdfRnPaKNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3143,
      "cache_read_input_tokens": 87311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3143
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_017oyUSMbvXXc3Q5T6AHitAr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
  "old_string": "The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.",
  "new_string": "The SFT checkpoint therefore occupies the regime where sign misattribution is most severe."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "05a7def5-9e1a-4a1b-86d6-1e6ca00b2500",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bFftRehdLqSMdfRnPaKNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3143,
      "cache_read_input_tokens": 87311,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3143
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

_source line 43 · 2026-05-18T20:19:09.375Z_

<details><summary>↩ Tool result · `toolu_017oyUSMbvXXc3Q5T6AHitAr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "289fd9de-59fe-47d1-8679-e7cb939ea6b6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "oldString": "The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.",
    "newString": "The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.",
    "originalFile": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?\n\n\\subsection{Environment}\n\\label{sec:environment}\n\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.\n\nALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.\n\n\\subsection{Base Model and Supervised Fine-Tuning}\n\\label{sec:base_model}\n\nWe use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n\nThis low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.\n\n\\subsection{RL Training Configuration}\n\\label{sec:rl_config}\n\nAll conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Shared RL training hyperparameters across all conditions.}\n\\label{tab:hyperparameters}\n\\begin{tabular}{lc}\n\\toprule\nParameter & Value \\\\\n\\midrule\nGroup size $K$ & 8 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nKL penalty $\\beta$ & 0.01 \\\\\nDiscount $\\gamma$ & 0.95 \\\\\nInvalid action penalty & 0.1 \\\\\nTasks per training step & 16 \\\\\nTraining steps & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.\n\nThe primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. All results are single-seed unless stated otherwise; two-seed replication is reported where available.\n\n\\subsection{Experimental Conditions}\n\\label{sec:conditions}\n\nWe evaluate seven conditions organized around three designs: factorial mechanism separation (Conditions~1--3), auxiliary baselines (Conditions~4--5), and parameter sweeps (Conditions~6--7).\n\n\\paragraph{Condition 1: Episode-level GRPO.}\nEach complete trajectory serves as a single GRPO sample with one shared advantage for all tokens. Both failure mechanisms are absent: the full context is preserved (no M1) and no per-window advantage can carry misattributed sign (no M2). Two seeds.\n\n\\paragraph{Condition 2: Step-independent $h{=}2$.}\nEach trajectory is segmented into fixed windows of $h = 2$ interaction steps, with each window receiving its own GRPO advantage. Both M1 (truncated context) and M2 (advantage sign determined by episode outcome rather than local action quality) are active. This is the default RAGEN configuration and represents the standard approach for multi-turn agent RL. Two seeds.\n\n\\paragraph{Condition 3: Step-independent $h{=}2$ with episode advantage.}\nThe factorial complement. Windows are constructed identically to Condition~2, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign assignment). The performance gap between Conditions~2 and~3 is therefore attributable to M2 alone. Two seeds.\n\nConditions~1--3 form a $2 \\times 2$ factorial design over observation scope (windowed vs.\\ full) and advantage scope (per-window vs.\\ episode-level), as described in Section~\\ref{sec:factorial_design}. The fourth cell (full observation with per-window advantage) is degenerate: with full context, only one window exists per episode, so per-window and episode-level advantage coincide.\n\n\\paragraph{Condition 4: Dense reward.}\nStep-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.\n\n\\paragraph{Condition 5: REINFORCE++ baseline.}\nEpisode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used. This condition was originally planned as a GAE baseline with a learned critic; we substituted REINFORCE++ after TRL~1.1.0 removed the required \\texttt{AutoModelForCausalLMWithValueHead} class.\n\n\\paragraph{Condition 6: Discount factor sweep.}\nStep-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. At $\\gamma = 1.0$, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains. Collapse at $\\gamma = 1.0$ would confirm that sign misattribution alone suffices to cause failure, independent of discount-induced magnitude variation.\n\n\\paragraph{Condition 7: Window-size sweep.}\nStep-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.\n\n\\subsection{Results}\n\\label{sec:results}\n\nResults are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size and discount-factor ablations (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}\n",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 7,
        "newStart": 17,
        "newLines": 7,
        "lines": [
          " ",
          " We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.",
          " ",
          "-This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.",
          "+This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.",
          " ",
          " \\subsection{RL Training Configuration}",
          " \\label{sec:rl_config}"
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

_source line 44_

<details open><summary>🔧 Tool call — Grep · `toolu_01BA9VkUgo2YGhvo58uG5C3G`</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
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
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "fdd7dfd8-27ae-456f-b459-d22337a33505",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MhnMjXdSgTPKdwYQMLQGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 90454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 709
      },
      "output_tokens": 62,
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

_source line 45 · 2026-05-18T20:19:12.856Z_

<details><summary>↩ Tool result · `toolu_01BA9VkUgo2YGhvo58uG5C3G`</summary>

```text
18:We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.
20:This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\ref{prop:correct_sign} predicts that approximately 80.9\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "983fe3f9-9645-471b-a4e5-92e98993cf93",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "18:We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n20:This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
The remaining "ing" matches are:
- Line 18: "fine-tuning" (compound noun), "resulting" (adjective), "training" (noun). None are trailing participial phrases.
- Line 20: "training" (noun in "step-independent training"). Not a trailing participial phrase.

All clean. The file is complete and correct. Let me do a final read to confirm everything is in order.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "c7b15ae9-c6ee-4276-a21e-63b9241d7982",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvdbboitCq81LHEkXGdar2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 91163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 372
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

_source line 47_

Remaining "ing" matches are all nouns/adjectives ("fine-tuning", "resulting", "training"), not trailing participial phrases. File is clean.

Rewrite complete. The setup (§5.1--5.5) covers ~850 words across five subsections: Environment, Base Model/SFT, RL Config (with booktabs table), Evaluation Protocol (32 in-dist + 134 OOD), and Experimental Conditions (7 conditions with factorial design, baselines, and sweeps). Results stub preserved as placeholder. No em-dashes, no trailing -ing phrases, no \placeholder in setup content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "uuid": "eb0e4324-6648-48dc-a503-60fd086e2d22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvdbboitCq81LHEkXGdar2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 372,
      "cache_read_input_tokens": 91163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 372
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

_source line 48_

Remaining "ing" matches are all nouns/adjectives ("fine-tuning", "resulting", "training"), not trailing participial phrases. File is clean.

Rewrite complete. The setup (§5.1--5.5) covers ~850 words across five subsections: Environment, Base Model/SFT, RL Config (with booktabs table), Evaluation Protocol (32 in-dist + 134 OOD), and Experimental Conditions (7 conditions with factorial design, baselines, and sweeps). Results stub preserved as placeholder. No em-dashes, no trailing -ing phrases, no \placeholder in setup content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 383853,
  "duration_api_ms": 384551,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "2be5c6b0-f1a1-4f4a-8b3b-23185f6d3417",
  "total_cost_usd": 1.3576814999999998,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 79834,
    "cache_read_input_tokens": 541546,
    "output_tokens": 23373,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 79834,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 255,
        "cache_read_input_tokens": 91163,
        "cache_creation_input_tokens": 372,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 372
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3441,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003551,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 23373,
      "cacheReadInputTokens": 541546,
      "cacheCreationInputTokens": 79834,
      "webSearchRequests": 0,
      "costUSD": 1.3541304999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "85edcc72-b2d2-462e-9aa7-ecad4c1e5614"
}
```

</details>

---
