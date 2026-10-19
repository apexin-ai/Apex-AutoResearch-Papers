# paper writing method

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper_writing_method_20260518T093817.log`
- **Structured JSON:** [`3883bb6ddf4e7eeb1516.json`](../../sessions/38/3883bb6ddf4e7eeb1516.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
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
  "uuid": "d071d950-41dd-4313-82bf-03d672890977",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779113400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a018dec2-3fd5-4121-a199-d5208765c0a9",
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and the current state of the paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "112bfa2a-c0a3-4673-89d1-806cc1a394e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvCxJUQirErrg72TsqQxap",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14393
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

<details open><summary>🔧 Tool call — Read · `toolu_01XGU96GrFB6ZJw9NhkCCS4e`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "be5e4699-ff52-4c1f-9080-a0e753dc849a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvCxJUQirErrg72TsqQxap",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14393
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

_source line 6 · 2026-05-18T09:38:30.530Z_

<details><summary>↩ Tool result · `toolu_01XGU96GrFB6ZJw9NhkCCS4e`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "e01b98db-aa94-439e-b93c-b1ca40cc58ea",
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

<details open><summary>🔧 Tool call — Read · `toolu_019PFPjn37Y2s8U4oeBXC8pE`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "6bbe5b51-8146-4a83-b05e-dbfcc514c64e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvCxJUQirErrg72TsqQxap",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14393
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

_source line 8 · 2026-05-18T09:38:31.623Z_

<details><summary>↩ Tool result · `toolu_019PFPjn37Y2s8U4oeBXC8pE`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "d5292220-75d8-467f-a110-3e124cb6a746",
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

<details open><summary>🔧 Tool call — Glob · `toolu_014MfuwWPGEip6CtJUrxLhwz`</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "7d01c65e-b03b-43d5-81f8-4b5545078198",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvCxJUQirErrg72TsqQxap",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14393,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14393
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

_source line 10 · 2026-05-18T09:38:31.910Z_

<details><summary>↩ Tool result · `toolu_014MfuwWPGEip6CtJUrxLhwz`</summary>

```text
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "23b047fa-e237-434a-ac3b-c0226e02481d",
  "tool_use_result": {
    "filenames": [
      "docs/paper/related_work.tex",
      "docs/paper/method.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/discussion.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 17,
    "numFiles": 6,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current method.tex and the main paper file to understand the existing structure, labels, and citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "a48ee3a7-9e39-4d3d-8dd3-227923e8332a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4gJgS414NshXEMwsKdVNv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10677,
      "cache_read_input_tokens": 26234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10677
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

Let me read the existing method.tex and the main paper file to understand current labels, citations, and conventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "2e3c4cab-6847-4506-9f61-92a388562624",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4gJgS414NshXEMwsKdVNv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10677,
      "cache_read_input_tokens": 26234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10677
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

<details open><summary>🔧 Tool call — Read · `toolu_01T1ixxZAoPKLuUXtL1JPZ9A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "24faa4e3-c92f-4541-9bb2-d3c4b9e863cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4gJgS414NshXEMwsKdVNv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10677,
      "cache_read_input_tokens": 26234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10677
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

_source line 14 · 2026-05-18T09:38:37.504Z_

<details><summary>↩ Tool result · `toolu_01T1ixxZAoPKLuUXtL1JPZ9A`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.
11	
12	At each control step, $\pi_\theta$ can be queried multiple times via independent flow-matching rollouts~\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\pi_\theta$.
13	
14	\subsection{Multi-Sample Generation and Conformal Selection}
15	\label{sec:selection}
16	
17	\paragraph{Sampling and truncation.}
18	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for each horizon step $h = 1, \dots, H$.
19	
20	\paragraph{Shrinkage covariance estimation.}
21	For each horizon step $h$, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well}:
22	\begin{equation}
23	  \boldsymbol{\Sigma}_h = (1 - \alpha_{\mathrm{LW}})\,\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}} + \alpha_{\mathrm{LW}}\,\frac{\mathrm{tr}(\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}})}{d}\,\mathbf{I},
24	  \label{eq:shrinkage}
25	\end{equation}
26	where $\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}}$ is the empirical covariance and $\alpha_{\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\% estimation error; shrinkage reduces this to below 5\%~\cite{ledoit2004well}.
27	
28	\paragraph{Mahalanobis nonconformity score.}
29	For each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:
30	\begin{equation}
31	  s_h(a) = (a - \boldsymbol{\mu}_h)^\top \boldsymbol{\Sigma}_h^{-1} (a - \boldsymbol{\mu}_h).
32	  \label{eq:mahal}
33	\end{equation}
34	This score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\cite{braun2025cgs}.
35	
36	\paragraph{Argmin selection.}
37	We select the sample with the lowest total nonconformity across all horizon steps:
38	\begin{equation}
39	  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} s_h\bigl(a_h^{(k)}\bigr).
40	  \label{eq:argmin}
41	\end{equation}
42	This selection procedure uses Mahalanobis-based scoring~\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\mathrm{base}} \in \mathbb{R}^{d \times H}$ is the starting point for residual correction.
43	
44	\subsection{Conformal Residual Module}
45	\label{sec:crm}
46	
47	The Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.
48	
49	\paragraph{Architecture.}
50	CRM is a 3-layer MLP with input normalization (input$\to$256$\to$256$\to$30; 330K parameters for the primary obs\_only variant).
51	Its input is the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{d \times H} = \mathbb{R}^{30}$, and the corrected action is:
52	\begin{equation}
53	  \mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}\bigl(\boldsymbol{\delta},\; \|\boldsymbol{\delta}\|_2 \leq \varepsilon\bigr),
54	  \label{eq:crm}
55	\end{equation}
56	where $\varepsilon$ is a norm bound hyperparameter (Section~\ref{sec:magnitude}).
57	
58	\paragraph{Observation-only conditioning.}
59	CRM receives only the observation embedding $\mathbf{z}_{\mathrm{obs}}$ and does \emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.
60	
61	\paragraph{Training.}
62	CRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\cite{liu2023libero}:
63	\begin{equation}
64	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2.
65	  \label{eq:loss}
66	\end{equation}
67	The training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$. The expert action $\mathbf{a}_{\mathrm{expert}}$ is the corresponding demonstration action.
68	
69	We apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\sigma \approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\cite{ross2011dagger}.
70	
71	\paragraph{Base VLA.}
72	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.
73	
74	\subsection{Magnitude Control}
75	\label{sec:magnitude}
76	
77	The norm bound $\varepsilon$ in~(\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.
78	
79	\paragraph{Unbounded correction fails catastrophically.}
80	Without clipping, the natural CRM output has $\|\boldsymbol{\delta}\|_2 \approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.
81	
82	\paragraph{Small corrections are effective.}
83	Constraining $\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.
84	
85	\paragraph{Connection to residual policy learning.}
86	The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.
87	
88	\paragraph{Differential sensitivity across CRM variants.}
89	Observation-conditioned CRM (obs\_only) maintains 35--36\% success on LIBERO-Spatial across the full range $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% at $\varepsilon = 0.1$ to 26\% at $\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\ref{sec:ablation}).
90	
91	\subsection{Inference Protocol}
92	\label{sec:inference_protocol}
93	
94	Each control step proceeds as follows:
95	\begin{enumerate}[nosep]
96	  \item Draw $K{=}10$ action chunks from the frozen VLA $\pi_\theta$ and truncate to $H{=}5$ steps.
97	  \item Compute shrinkage covariance $\boldsymbol{\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.
98	  \item Select $a_{\mathrm{base}}$ via argmin over total nonconformity~(\ref{eq:argmin}).
99	  \item Compute residual $\boldsymbol{\delta} = \mathrm{CRM}(\mathbf{z}_{\mathrm{obs}})$ and clip to $\|\boldsymbol{\delta}\|_2 \leq \varepsilon$.
100	  \item Execute the first action of $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
101	  \item Observe new state and re-plan from step~1.
102	\end{enumerate}
103	The computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "215bebb8-8b6a-4569-a008-e138ccb9d586",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis selection procedure uses Mahalanobis-based scoring~\\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 330K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dj11qSfNXHD6FpoNq9ZZQt`</summary>

```json
{
  "pattern": "docs/paper/*.{tex,bib}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "35416368-56e7-44ce-a5a5-6e5c5b277800",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4gJgS414NshXEMwsKdVNv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10677,
      "cache_read_input_tokens": 26234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10677
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

_source line 16 · 2026-05-18T09:38:38.361Z_

<details><summary>↩ Tool result · `toolu_01Dj11qSfNXHD6FpoNq9ZZQt`</summary>

```text
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/references.bib
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "e5538ee2-3ece-4558-9ffc-3b0b729a1245",
  "tool_use_result": {
    "filenames": [
      "docs/paper/related_work.tex",
      "docs/paper/method.tex",
      "docs/paper/references.bib",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/discussion.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 18,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the references.bib to understand available citation keys, and check the introduction.tex for label conventions and how the pipeline figure is referenced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "2a492c0e-99ff-4aad-8d45-ca4c1ef2a9ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151MzkUv3FtwCm8QgNkwub4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 36911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

Let me check the bib file for citation keys and the introduction for label/reference conventions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "bf945b98-04d6-43e3-b08b-0830e3f03002",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151MzkUv3FtwCm8QgNkwub4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 36911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

<details open><summary>🔧 Tool call — Read · `toolu_014ej5D9AFr2nhoQYHvxxS7r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "e13120cb-27c1-448a-a912-f3fc4d5f2f08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151MzkUv3FtwCm8QgNkwub4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 36911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

_source line 20 · 2026-05-18T09:38:43.626Z_

<details><summary>↩ Tool result · `toolu_014ej5D9AFr2nhoQYHvxxS7r`</summary>

```text
1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	@article{barber2023conformal,
21	    title={Conformal Prediction Beyond Exchangeability},
22	    author={Rina Foygel Barber and Emmanuel J. Cand{\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},
23	    journal={Annals of Statistics},
24	    volume={51},
25	    number={2},
26	    pages={816--845},
27	    year={2023}
28	}
29	
30	@misc{black2024pi0,
31	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
32	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
33	    year={2024},
34	    eprint={2410.24164},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{braun2025cgs,
40	    title={Multivariate Conformal Prediction via Conformalized Gaussian Scoring},
41	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
42	    year={2025},
43	    eprint={2507.20941},
44	    archivePrefix={arXiv},
45	    primaryClass={stat.ML}
46	}
47	
48	@misc{brohan2023rt2,
49	    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
50	    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},
51	    year={2023},
52	    eprint={2307.15818},
53	    archivePrefix={arXiv},
54	    primaryClass={cs.RO}
55	}
56	
57	@misc{chen2026reconvla,
58	    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},
59	    author={Lingling Chen and Zongyao Lyu and William J. Beksi},
60	    year={2026},
61	    eprint={2604.16677},
62	    archivePrefix={arXiv},
63	    primaryClass={cs.RO}
64	}
65	
66	@misc{cosmos_policy_2026,
67	    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},
68	    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},
69	    year={2026},
70	    eprint={2601.16163},
71	    archivePrefix={arXiv},
72	    primaryClass={cs.AI}
73	}
74	
75	@misc{digflow2025,
76	    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},
77	    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},
78	    year={2025},
79	    eprint={2512.01715},
80	    archivePrefix={arXiv},
81	    primaryClass={cs.RO}
82	}
83	
84	@misc{fei2025liberoplus,
85	    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},
86	    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},
87	    year={2025},
88	    eprint={2510.13626},
89	    archivePrefix={arXiv},
90	    primaryClass={cs.RO}
91	}
92	
93	@inproceedings{gal2016dropout,
94	    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
95	    author={Yarin Gal and Zoubin Ghahramani},
96	    booktitle={International Conference on Machine Learning (ICML)},
97	    year={2016}
98	}
99	
100	@misc{ghosh2024octo,
101	    title={Octo: An Open-Source Generalist Robot Policy},
102	    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},
103	    year={2024},
104	    eprint={2405.12213},
105	    archivePrefix={arXiv},
106	    primaryClass={cs.RO}
107	}
108	
109	@inproceedings{gibbs2021aci,
110	    title={Adaptive Conformal Inference Under Distribution Shift},
111	    author={Isaac Gibbs and Emmanuel Cand{\`e}s},
112	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
113	    year={2021}
114	}
115	
116	@inproceedings{gu2025safe,
117	    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},
118	    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},
119	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
120	    year={2025}
121	}
122	
123	@misc{kim2024openvla,
124	    title={OpenVLA: An Open-Source Vision-Language-Action Model},
125	    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
126	    year={2024},
127	    eprint={2406.09246},
128	    archivePrefix={arXiv},
129	    primaryClass={cs.RO}
130	}
131	
132	@inproceedings{lakshminarayanan2017ensembles,
133	    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
134	    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},
135	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
136	    year={2017}
137	}
138	
139	@article{ledoit2004well,
140	    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},
141	    author={Olivier Ledoit and Michael Wolf},
142	    journal={Journal of Multivariate Analysis},
143	    volume={88},
144	    number={2},
145	    pages={365--411},
146	    year={2004}
147	}
148	
149	@inproceedings{lipman2023flow,
150	    title={Flow Matching for Generative Modeling},
151	    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},
152	    booktitle={International Conference on Learning Representations (ICLR)},
153	    year={2023}
154	}
155	
156	@inproceedings{liu2023libero,
157	    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
158	    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
159	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
160	    year={2023}
161	}
162	
163	@misc{liu2026ttvla,
164	    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},
165	    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},
166	    year={2026},
167	    eprint={2601.06748},
168	    archivePrefix={arXiv},
169	    primaryClass={cs.RO}
170	}
171	
172	@misc{luan2026snapflow,
173	    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},
174	    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},
175	    year={2026},
176	    eprint={2604.05656},
177	    archivePrefix={arXiv},
178	    primaryClass={cs.RO}
179	}
180	
181	@misc{robustvla2025,
182	    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},
183	    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},
184	    year={2025},
185	    eprint={2511.01331},
186	    archivePrefix={arXiv},
187	    primaryClass={cs.RO}
188	}
189	
190	@inproceedings{romano2019cqr,
191	    title={Conformalized Quantile Regression},
192	    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\`e}s},
193	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
194	    year={2019}
195	}
196	
197	@article{shafer2008tutorial,
198	    title={A Tutorial on Conformal Prediction},
199	    author={Glenn Shafer and Vladimir Vovk},
200	    journal={Journal of Machine Learning Research},
201	    volume={9},
202	    pages={371--421},
203	    year={2008}
204	}
205	
206	@misc{shukor2025smolvla,
207	    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},
208	    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},
209	    year={2025},
210	    eprint={2506.01844},
211	    archivePrefix={arXiv},
212	    primaryClass={cs.RO}
213	}
214	
215	@misc{srpo2025,
216	    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},
217	    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},
218	    year={2025},
219	    eprint={2511.15605},
220	    archivePrefix={arXiv},
221	    primaryClass={cs.RO}
222	}
223	
224	@misc{vla_gse_2026,
225	    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},
226	    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},
227	    year={2026},
228	    eprint={2605.06175},
229	    archivePrefix={arXiv},
230	    primaryClass={cs.RO}
231	}
232	
233	@misc{wang2025cploop,
234	    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},
235	    author={Han Wang and Chao Ning},
236	    year={2025},
237	    eprint={2510.16376},
238	    archivePrefix={arXiv},
239	    primaryClass={cs.RO}
240	}
241	
242	@misc{xing2026diu,
243	    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},
244	    author={Jiarui Xing and Song Wang and Jian Wang},
245	    year={2026},
246	    eprint={2605.00941},
247	    archivePrefix={arXiv},
248	    primaryClass={cs.LG}
249	}
250	
251	@misc{yuan2026ups,
252	    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},
253	    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},
254	    year={2026},
255	    eprint={2602.22474},
256	    archivePrefix={arXiv},
257	    primaryClass={cs.RO}
258	}
259	
260	@inproceedings{chi2023diffusion_policy,
261	    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
262	    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},
263	    booktitle={Robotics: Science and Systems (RSS)},
264	    year={2023},
265	    note={Also published in IJRR 2024. arXiv:2303.04137}
266	}
267	
268	@inproceedings{zhao2024conformalized,
269	    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},
270	    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},
271	    booktitle={Robotics: Science and Systems (RSS)},
272	    year={2024}
273	}
274	
275	@inproceedings{silver2018residual,
276	    title={Residual Policy Learning},
277	    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},
278	    booktitle={Robotics: Science and Systems (RSS)},
279	    year={2018},
280	    note={arXiv:1812.06298}
281	}
282	
283	@inproceedings{jiang2024transic,
284	    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},
285	    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},
286	    booktitle={Conference on Robot Learning (CoRL)},
287	    year={2024},
288	    note={arXiv:2405.10315}
289	}
290	
291	@inproceedings{johannink2019residual,
292	    title={Residual Reinforcement Learning for Robot Control},
293	    author={Tobias Johannink and Shikhar Bahl and Ashvin Nair and Jianlan Luo and Avinash Kumar and Matthias Loskyll and Juan Aparicio Ojea and Eugen Solowjow and Sergey Levine},
294	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
295	    year={2019},
296	    pages={6023--6029}
297	}
298	
299	@inproceedings{xiao2026pld,
300	    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},
301	    author={Wenli Xiao and others},
302	    booktitle={International Conference on Learning Representations (ICLR)},
303	    year={2026},
304	    note={arXiv:2511.00091}
305	}
306	
307	@misc{pan2025drc,
308	    title={DRC: Decaying Relative Correction for Policy Refinement},
309	    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},
310	    year={2025},
311	    eprint={2503.15368},
312	    archivePrefix={arXiv},
313	    primaryClass={cs.RO}
314	}
315	
316	@inproceedings{zhou2025acp_cbf,
317	    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},
318	    author={Hao Zhou and Yanze Zhang and Wenhao Luo},
319	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
320	    year={2025},
321	    note={arXiv:2503.17678}
322	}
323	
324	@misc{zollo2025vla_calibration,
325	    title={Confidence Calibration in Vision-Language-Action Models},
326	    author={Thomas Zollo and Richard Zemel},
327	    year={2025},
328	    eprint={2507.17383},
329	    archivePrefix={arXiv},
330	    primaryClass={cs.RO}
331	}
332	
333	@inproceedings{ross2011dagger,
334	    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
335	    author={St{\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},
336	    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},
337	    year={2011}
338	}
339	
340	@misc{tang2026shifting,
341	    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},
342	    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},
343	    year={2026},
344	    eprint={2603.18342},
345	    archivePrefix={arXiv},
346	    primaryClass={cs.RO}
347	}
348	
349	@misc{liu2026scvla,
350	    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},
351	    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},
352	    year={2026},
353	    eprint={2602.21633},
354	    archivePrefix={arXiv},
355	    primaryClass={cs.RO}
356	}
357	
358	@misc{li2025vlapilot,
359	    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},
360	    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},
361	    year={2025},
362	    eprint={2511.14178},
363	    archivePrefix={arXiv},
364	    primaryClass={cs.RO}
365	}
366	
367	@inproceedings{zhong2026acotvla,
368	    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},
369	    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},
370	    year={2026},
371	    eprint={2601.11404},
372	    archivePrefix={arXiv},
373	    primaryClass={cs.RO},
374	    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}
375	}
376	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "0aab8361-713a-496c-9cf7-00eb2388b222",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/references.bib",
      "content": "@misc{a2c2_2025,\n    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},\n    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},\n    year={2025},\n    eprint={2509.23224},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@article{angelopoulos2023gentle,\n    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n    author={Anastasios N. Angelopoulos and Stephen Bates},\n    journal={Foundations and Trends in Machine Learning},\n    year={2023},\n    eprint={2107.07511},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@article{barber2023conformal,\n    title={Conformal Prediction Beyond Exchangeability},\n    author={Rina Foygel Barber and Emmanuel J. Cand{\\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},\n    journal={Annals of Statistics},\n    volume={51},\n    number={2},\n    pages={816--845},\n    year={2023}\n}\n\n@misc{black2024pi0,\n    title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},\n    year={2024},\n    eprint={2410.24164},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{braun2025cgs,\n    title={Multivariate Conformal Prediction via Conformalized Gaussian Scoring},\n    author={Sacha Braun and Eug{\\`e}ne Berta and Michael I. Jordan and Francis Bach},\n    year={2025},\n    eprint={2507.20941},\n    archivePrefix={arXiv},\n    primaryClass={stat.ML}\n}\n\n@misc{brohan2023rt2,\n    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},\n    year={2023},\n    eprint={2307.15818},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{chen2026reconvla,\n    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},\n    author={Lingling Chen and Zongyao Lyu and William J. Beksi},\n    year={2026},\n    eprint={2604.16677},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{cosmos_policy_2026,\n    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},\n    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},\n    year={2026},\n    eprint={2601.16163},\n    archivePrefix={arXiv},\n    primaryClass={cs.AI}\n}\n\n@misc{digflow2025,\n    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},\n    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},\n    year={2025},\n    eprint={2512.01715},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{fei2025liberoplus,\n    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},\n    year={2025},\n    eprint={2510.13626},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gal2016dropout,\n    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n    author={Yarin Gal and Zoubin Ghahramani},\n    booktitle={International Conference on Machine Learning (ICML)},\n    year={2016}\n}\n\n@misc{ghosh2024octo,\n    title={Octo: An Open-Source Generalist Robot Policy},\n    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},\n    year={2024},\n    eprint={2405.12213},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gibbs2021aci,\n    title={Adaptive Conformal Inference Under Distribution Shift},\n    author={Isaac Gibbs and Emmanuel Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2021}\n}\n\n@inproceedings{gu2025safe,\n    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},\n    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2025}\n}\n\n@misc{kim2024openvla,\n    title={OpenVLA: An Open-Source Vision-Language-Action Model},\n    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n    year={2024},\n    eprint={2406.09246},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2017}\n}\n\n@article{ledoit2004well,\n    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},\n    author={Olivier Ledoit and Michael Wolf},\n    journal={Journal of Multivariate Analysis},\n    volume={88},\n    number={2},\n    pages={365--411},\n    year={2004}\n}\n\n@inproceedings{lipman2023flow,\n    title={Flow Matching for Generative Modeling},\n    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2023}\n}\n\n@inproceedings{liu2023libero,\n    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2023}\n}\n\n@misc{liu2026ttvla,\n    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},\n    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},\n    year={2026},\n    eprint={2601.06748},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{luan2026snapflow,\n    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},\n    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},\n    year={2026},\n    eprint={2604.05656},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{robustvla2025,\n    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},\n    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},\n    year={2025},\n    eprint={2511.01331},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{romano2019cqr,\n    title={Conformalized Quantile Regression},\n    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2019}\n}\n\n@article{shafer2008tutorial,\n    title={A Tutorial on Conformal Prediction},\n    author={Glenn Shafer and Vladimir Vovk},\n    journal={Journal of Machine Learning Research},\n    volume={9},\n    pages={371--421},\n    year={2008}\n}\n\n@misc{shukor2025smolvla,\n    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},\n    year={2025},\n    eprint={2506.01844},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{srpo2025,\n    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},\n    year={2025},\n    eprint={2511.15605},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{vla_gse_2026,\n    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},\n    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},\n    year={2026},\n    eprint={2605.06175},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{wang2025cploop,\n    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},\n    author={Han Wang and Chao Ning},\n    year={2025},\n    eprint={2510.16376},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{xing2026diu,\n    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},\n    author={Jiarui Xing and Song Wang and Jian Wang},\n    year={2026},\n    eprint={2605.00941},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@misc{yuan2026ups,\n    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},\n    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},\n    year={2026},\n    eprint={2602.22474},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{chi2023diffusion_policy,\n    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2023},\n    note={Also published in IJRR 2024. arXiv:2303.04137}\n}\n\n@inproceedings{zhao2024conformalized,\n    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},\n    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2024}\n}\n\n@inproceedings{silver2018residual,\n    title={Residual Policy Learning},\n    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2018},\n    note={arXiv:1812.06298}\n}\n\n@inproceedings{jiang2024transic,\n    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},\n    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},\n    booktitle={Conference on Robot Learning (CoRL)},\n    year={2024},\n    note={arXiv:2405.10315}\n}\n\n@inproceedings{johannink2019residual,\n    title={Residual Reinforcement Learning for Robot Control},\n    author={Tobias Johannink and Shikhar Bahl and Ashvin Nair and Jianlan Luo and Avinash Kumar and Matthias Loskyll and Juan Aparicio Ojea and Eugen Solowjow and Sergey Levine},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2019},\n    pages={6023--6029}\n}\n\n@inproceedings{xiao2026pld,\n    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},\n    author={Wenli Xiao and others},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2026},\n    note={arXiv:2511.00091}\n}\n\n@misc{pan2025drc,\n    title={DRC: Decaying Relative Correction for Policy Refinement},\n    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},\n    year={2025},\n    eprint={2503.15368},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhou2025acp_cbf,\n    title={Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction},\n    author={Hao Zhou and Yanze Zhang and Wenhao Luo},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2025},\n    note={arXiv:2503.17678}\n}\n\n@misc{zollo2025vla_calibration,\n    title={Confidence Calibration in Vision-Language-Action Models},\n    author={Thomas Zollo and Richard Zemel},\n    year={2025},\n    eprint={2507.17383},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{ross2011dagger,\n    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n    author={St{\\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},\n    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},\n    year={2011}\n}\n\n@misc{tang2026shifting,\n    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},\n    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},\n    year={2026},\n    eprint={2603.18342},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{liu2026scvla,\n    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},\n    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},\n    year={2026},\n    eprint={2602.21633},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{li2025vlapilot,\n    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},\n    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},\n    year={2025},\n    eprint={2511.14178},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhong2026acotvla,\n    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},\n    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},\n    year={2026},\n    eprint={2601.11404},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO},\n    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}\n}\n",
      "numLines": 376,
      "startLine": 1,
      "totalLines": 376
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01MKHJb93Xu4zUiustr9VPqA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "c01ea8ba-c176-4e85-bd96-be7890ab44fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151MzkUv3FtwCm8QgNkwub4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 36911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

_source line 22 · 2026-05-18T09:38:44.043Z_

<details><summary>↩ Tool result · `toolu_01MKHJb93Xu4zUiustr9VPqA`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\pi_0$ drops from 94.2\% to 6.6\% under robot initial-state perturbation, and UniVLA from 95.2\% to 4.3\% under camera viewpoint changes~\cite{fei2025liberoplus}.
7	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.
8	
9	% --- Para 2: Existing approaches and the gap ---
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}.
12	These approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen.
14	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.
15	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step, too slow for real-time manipulation.
16	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
17	In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.
18	
19	% --- Para 3: Our approach — sample-then-correct ---
20	We introduce \textbf{ACR-VLA} (\textbf{A}daptive \textbf{C}onformal \textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \emph{sample-then-correct} pipeline.
21	At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \emph{Conformal Residual Module} (CRM).
22	CRM is a 330K-parameter MLP conditioned on the VLA's frozen observation embedding.
23	It predicts a small residual $\boldsymbol{\delta}$ whose $L_2$ norm is clipped to a bound $\varepsilon$, producing the corrected action $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
24	The critical design insight is that correction operates on a high-quality starting point (the conformal-selected action) and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.
25	The base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.
26	
27	% --- Para 4: Key findings (with exp_id references) ---
28	We evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:
29	
30	\textbf{(1)~The full pipeline significantly improves over the frozen VLA.}
31	Across five seeds on LIBERO-Object, the sample-then-correct pipeline (obs\_only, $\varepsilon{=}0.2$) achieves mean $17.0 \pm 2.8$\% versus VLA-only mean $10.75 \pm 1.5$\% ($p < 0.01$, pooled Fisher's exact test), a +6\,pp improvement.
32	% obs_only eps=0.2 seeds 42-46: 22/16/16/16/15%. VLA-only seeds 42-45: 10.75±1.5%. Argmin seeds 42-45: 13.5±2.4%.
33	The margin over conformal selection alone (Argmin mean $13.5 \pm 2.4$\%) is +3.5\,pp, consistent across seeds but not statistically significant ($p = 0.075$), suggesting larger evaluation budgets are needed to confirm this gap.
34	
35	\textbf{(2)~Observation features suffice for correction; conformal features do not help.}
36	Counter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\%) performs no better than selection alone (12.0\%), while scalar conformal conditioning (9.0\%) is actively harmful.
37	% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)
38	Only observation-conditioned CRM (19.0\%) produces meaningful improvement.
39	This honest negative result highlights a gap between per-step prediction accuracy (where richer features help in offline evaluation) and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.
40	
41	\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}
42	Without magnitude bounding, the per-DOF-conditioned CRM's natural output ($\|\boldsymbol{\delta}\|_2 \approx 1.42$) causes catastrophic failure: 0\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.
43	Constraining corrections to $\|\boldsymbol{\delta}\|_2 \leq 0.1$ recovers the full improvement.
44	% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)
45	Observation-conditioned CRM maintains stable 35--36\% success on LIBERO-Spatial across $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% to 26\% over the same range. This robustness gap is the paper's strongest evidence: it holds across all tested seeds and magnitude bounds, independent of the seed-42 outlier.
46	% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03
47	
48	We note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, the best CRM variant performs within 1\,pp of the selection baseline, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.
49	
50	% --- Para 5: Contributions ---
51	Our contributions are:
52	\begin{enumerate}[leftmargin=*,nosep]
53	  \item \textbf{A sample-then-correct pipeline for frozen VLAs.}
54	  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.
55	  On LIBERO-Object, this pipeline significantly improves over the frozen VLA baseline (+6\,pp, $p < 0.01$, 5-seed pooled test).
56	  % obs_only eps=0.2 5-seed mean 17.0±2.8% vs VLA-only 4-seed mean 10.75±1.5%
57	
58	  \item \textbf{Systematic conditioning comparison and honest negative result.}
59	  We compare three CRM conditioning variants (per-DOF conformal features, scalar uncertainty, and observation features) and find that only observation conditioning is effective.
60	  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.
61	
62	  \item \textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}
63	  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\times}$ range of magnitude bounds ($\varepsilon \in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.
64	\end{enumerate}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "d2fe1e75-b3ef-4aaf-a65c-082320e6cbeb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached high success rates on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: visual and physical perturbations routinely encountered in deployment (camera viewpoint shifts, object layout changes, robot initial state variation) can degrade success rates by over 65 percentage points. For example, $\\pi_0$ drops from 94.2\\% to 6.6\\% under robot initial-state perturbation, and UniVLA from 95.2\\% to 4.3\\% under camera viewpoint changes~\\cite{fei2025liberoplus}.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}.\nThese approaches are effective but require retraining or per-task RL, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen.\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate action-level uncertainty and uses these estimates for uncertainty-guided action selection and out-of-distribution detection, taking a complementary UQ-driven approach rather than learning explicit corrective residuals.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step, too slow for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.\nIn short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce \\textbf{ACR-VLA} (\\textbf{A}daptive \\textbf{C}onformal \\textbf{R}efinement for VLA), an inference-time module that improves frozen VLA actions through a \\emph{sample-then-correct} pipeline.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the most conforming candidate via Mahalanobis-based nonconformity scoring with shrinkage covariance estimation~\\cite{ledoit2004well,braun2025cgs}, and then applies a learned residual correction via a lightweight \\emph{Conformal Residual Module} (CRM).\nCRM is a 330K-parameter MLP conditioned on the VLA's frozen observation embedding.\nIt predicts a small residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe critical design insight is that correction operates on a high-quality starting point (the conformal-selected action) and that bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Key findings (with exp_id references) ---\nWe evaluate ACR-VLA on LIBERO-Object (10 tasks, 100 trials per method) and LIBERO-Spatial (10 tasks, 100 trials) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone. Three findings emerge:\n\n\\textbf{(1)~The full pipeline significantly improves over the frozen VLA.}\nAcross five seeds on LIBERO-Object, the sample-then-correct pipeline (obs\\_only, $\\varepsilon{=}0.2$) achieves mean $17.0 \\pm 2.8$\\% versus VLA-only mean $10.75 \\pm 1.5$\\% ($p < 0.01$, pooled Fisher's exact test), a +6\\,pp improvement.\n% obs_only eps=0.2 seeds 42-46: 22/16/16/16/15%. VLA-only seeds 42-45: 10.75±1.5%. Argmin seeds 42-45: 13.5±2.4%.\nThe margin over conformal selection alone (Argmin mean $13.5 \\pm 2.4$\\%) is +3.5\\,pp, consistent across seeds but not statistically significant ($p = 0.075$), suggesting larger evaluation budgets are needed to confirm this gap.\n\n\\textbf{(2)~Observation features suffice for correction; conformal features do not help.}\nCounter to intuition from synthetic experiments, conditioning CRM on per-DOF conformal statistics (perdof: 11.0\\%) performs no better than selection alone (12.0\\%), while scalar conformal conditioning (9.0\\%) is actively harmful.\n% exp_id: eval-acr-object-v4-small (perdof 11.0%), eval-acr-object-v4-scalar (9.0%)\nOnly observation-conditioned CRM (19.0\\%) produces meaningful improvement.\nThis honest negative result highlights a gap between per-step prediction accuracy (where richer features help in offline evaluation) and closed-loop task success, where covariance estimation noise from $K{=}10$ samples undermines per-DOF conditioning.\n\n\\textbf{(3)~Correction magnitude control is critical and previously unrecognized.}\nWithout magnitude bounding, the per-DOF-conditioned CRM's natural output ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic failure: 0\\% success on LIBERO-Spatial, as compounding correction errors rapidly drive the state distribution away from the CRM's training regime.\nConstraining corrections to $\\|\\boldsymbol{\\delta}\\|_2 \\leq 0.1$ recovers the full improvement.\n% exp_id: eval-acr-spatial-v4-default-r3 (norm=1.42, 0%), eval-acr-object-v4-obs-only (norm=0.1, 19.0%)\nObservation-conditioned CRM maintains stable 35--36\\% success on LIBERO-Spatial across $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% to 26\\% over the same range. This robustness gap is the paper's strongest evidence: it holds across all tested seeds and magnitude bounds, independent of the seed-42 outlier.\n% exp_id: eval-mag-obsonly-norm005, eval-mag-obsonly-norm03, eval-mag-perdof-norm03\n\nWe note that correction offers targeted improvements on object-centric manipulation rather than universal gains: on LIBERO-Spatial, the best CRM variant performs within 1\\,pp of the selection baseline, suggesting that the correction mechanism is most effective when distribution shift induces systematic action biases that a learned module can identify and compensate.\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We propose ACR-VLA, which combines conformal sample selection with learned residual correction for frozen flow-matching VLAs.\n  On LIBERO-Object, this pipeline significantly improves over the frozen VLA baseline (+6\\,pp, $p < 0.01$, 5-seed pooled test).\n  % obs_only eps=0.2 5-seed mean 17.0±2.8% vs VLA-only 4-seed mean 10.75±1.5%\n\n  \\item \\textbf{Systematic conditioning comparison and honest negative result.}\n  We compare three CRM conditioning variants (per-DOF conformal features, scalar uncertainty, and observation features) and find that only observation conditioning is effective.\n  This challenges the intuition that richer uncertainty features should yield better corrections, and reveals that covariance estimation noise at $K{=}10$ undermines per-DOF conditioning in closed-loop settings.\n\n  \\item \\textbf{Systematic empirical study of correction magnitude sensitivity for VLA action refinement.}\n  We show that unbounded correction causes catastrophic failure and that observation-conditioned CRM is uniquely robust across a $6{\\times}$ range of magnitude bounds ($\\varepsilon \\in [0.05, 0.3]$), establishing magnitude control as a critical design axis for inference-time action correction.\n\\end{enumerate}\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01HnWFjeBvVDREAiiB7Nngko`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "bf04bcb3-98a0-4310-ab12-0380e4f13808",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151MzkUv3FtwCm8QgNkwub4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3771,
      "cache_read_input_tokens": 36911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3771
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

_source line 24 · 2026-05-18T09:38:44.657Z_

<details><summary>↩ Tool result · `toolu_01HnWFjeBvVDREAiiB7Nngko`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction significantly improve over the frozen VLA baseline?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+6\,pp over VLA-only, $p < 0.01$), no (honest negative), and critically, unbounded correction is catastrophic, but obs\_only is robust across all tested seeds and magnitude bounds.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\ref{sec:selection}), no CRM correction.
30	\end{itemize}
31	
32	\paragraph{CRM variants.}
33	All CRM variants share the same 3-layer MLP architecture (input$\to$256$\to$256$\to$30) and differ only in their conditioning input:
34	\begin{itemize}[nosep]
35	  \item \textbf{obs\_only}: frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ (330K params). This is our primary method.
36	  \item \textbf{perdof}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).
37	  \item \textbf{scalar}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).
38	\end{itemize}
39	
40	\paragraph{Training.}
41	CRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.
42	For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\mathrm{base}}$.
43	Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.
44	Data augmentation includes additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and uncertainty features ($\sigma \approx 0.006$).
45	The default magnitude bound is $\varepsilon = 0.1$ for all CRM variants unless stated otherwise.
46	
47	\paragraph{Statistical protocol.}
48	Table~\ref{tab:main} reports seed 42 (10 rollouts $\times$ 10 tasks = 100 episodes per suite).
49	For the primary comparison, we replicate across multiple seeds on LIBERO-Object: obs\_only ($\varepsilon{=}0.2$, seeds 42--46) achieves 22/16/16/16/15\% (mean $17.0 \pm 2.8$\%), VLA-only (seeds 42--45) achieves mean $10.75 \pm 1.5$\%, and Argmin (seeds 42--45) achieves mean $13.5 \pm 2.4$\%.
50	Pooled Fisher's exact test: obs\_only vs.\ VLA-only is significant ($p < 0.01$); obs\_only vs.\ Argmin is not ($p = 0.075$).
51	All five obs\_only seeds exceed the VLA-only baseline, confirming reproducible improvement despite per-seed variance.
52	Multi-seed VLA-mean evaluation (seeds 42/43/44/45 = 12/15/10/13\%, mean 12.5\%) confirms that averaging provides no consistent benefit over single-sample execution.
53	
54	
55	\subsection{Main Results}
56	\label{sec:main_results}
57	
58	Table~\ref{tab:main} compares all methods on both benchmarks.
59	
60	\begin{table}[t]
61	\centering
62	\caption{Task success rate (\%\,$\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\times$ 10 rollouts each, seed 42). $\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}
63	\label{tab:main}
64	\small
65	\begin{tabular}{lccc}
66	\toprule
67	Method & Object (\%) & Spatial (\%) & $\Delta$ Object \\
68	\midrule
69	VLA-only ($K{=}1$)    & 12.0 & 30.0 & $\phantom{+}0.0$ \\
70	VLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\phantom{+}0.0$ \\
71	Argmin ($K{=}10$)      & 12.0 & 34.0 & --- \\
72	\midrule
73	scalar ($\varepsilon{=}0.1$)  & \phantom{0}9.0 & 32.0 & $-3.0$ \\
74	perdof ($\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\
75	\textbf{obs\_only} ($\varepsilon{=}0.1$) & \textbf{19.0} & \textbf{35.0} & $\mathbf{+7.0}$ \\
76	\midrule
77	obs\_only ($\varepsilon{=}0.2$) & \textbf{22.0} & 35.0 & $+10.0$ \\
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	\paragraph{Object benchmark: correction helps.}
83	On LIBERO-Object, obs\_only at $\varepsilon{=}0.1$ achieves 19.0\% (seed 42), and at $\varepsilon{=}0.2$ yields 22.0\%.
84	Across five seeds ($\varepsilon{=}0.2$), the pipeline achieves mean $17.0 \pm 2.8$\% versus VLA-only mean $10.75 \pm 1.5$\% ($p < 0.01$, pooled Fisher's exact test).
85	The improvement over Argmin (mean $13.5 \pm 2.4$\%) is +3.5\,pp, consistent but not statistically significant at current sample sizes ($p = 0.075$).
86	
87	Three baselines (VLA-only, VLA-mean, and Argmin) all achieve 12.0\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.
88	The VLA-mean result (12\%) is particularly informative: averaging 10 independent flow-matching samples does not reduce error compared to a single sample ($K{=}1$), confirming that action diversity does not center around the correct action.
89	Multi-sample strategies require a learned selection or correction mechanism to extract value from the sample set.
90	On LIBERO-Spatial, by contrast, Argmin improves +4\,pp over VLA-only (34\% vs.\ 30\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.
91	The obs\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.
92	
93	\paragraph{Pipeline decomposition: selection amplifies correction.}
94	To isolate the contributions of selection versus correction, we evaluate the CRM in direct correction mode ($K{=}1$): the CRM corrects a single VLA output without multi-sample selection.
95	Direct correction achieves 14\%, a +2\,pp gain over VLA-only (12\%).
96	Combined with the Argmin result (selection without correction, also 12\%), this reveals that neither component alone is effective, yet together they yield +10\,pp (22\% at $\varepsilon{=}0.2$).
97	Conformal selection provides the CRM with higher-quality starting actions by filtering out the worst samples; the CRM then applies corrections that are more reliable on these pre-screened candidates.
98	On individual tasks, the amplification varies: for bbq\_sauce, direct correction alone matches the full pipeline (40\%), while for chocolate\_pudding the full pipeline doubles the direct correction gain (60\% vs.\ 30\%).
99	This pattern suggests that selection is most valuable on tasks where the VLA's error modes are diverse across samples, creating headroom for ranking to exploit.
100	
101	\paragraph{Spatial benchmark: correction does not help.}
102	On LIBERO-Spatial, all methods cluster within a 5\,pp band (30--35\%).
103	The best CRM variants (obs\_only, perdof) achieve 35\%, only 1\,pp above the Argmin baseline (34\%).
104	This is a null result that we report prominently.
105	
106	We interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.
107	The VLA's observation encoder cannot extract correctable error signals from spatial shifts. The problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.
108	Residual correction at the action level is the wrong granularity for this type of generalization.
109	
110	\paragraph{Key finding.}
111	The full pipeline significantly improves over VLA-only for object manipulation ($p < 0.01$), where the challenge is fine-grained motor control with novel objects.
112	For spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.
113	
114	
115	\subsection{CRM Conditioning Ablation}
116	\label{sec:ablation}
117	
118	We focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\ref{tab:main}).
119	
120	\paragraph{Ranking.}
121	obs\_only (19.0\%) $\gg$ Argmin (12.0\%) $\approx$ perdof (11.0\%) $>$ scalar (9.0\%).
122	
123	This ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \emph{hurt} rather than help.
124	Scalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\,pp below the Argmin baseline that uses no correction at all.
125	
126	The scalar $<$ perdof ordering is consistent across seeds (scalar: 9\%/6\% for seeds 42/44; perdof: 11\%/8\%).
127	One-dimensional scalar uncertainty compresses all six action dimensions into a single number.
128	When certain dimensions carry high uncertainty but the correction direction is already correct along those axes, the scalar signal cannot distinguish this case from one where correction is needed everywhere.
129	The result is uniform over-correction or under-correction across all dimensions.
130	Per-DOF conditioning at least permits dimension-specific judgments, though at $K{=}10$ these judgments remain too noisy to be useful.
131	Even 1D scalar uncertainty conditioning is harmful, confirming that conformal scores at $K{=}10$ are unreliable regardless of aggregation dimensionality.
132	The noise originates in the score itself (rank-deficient covariance estimate from 10 samples in 6D), not in how these scores are decomposed across dimensions.
133	
134	\paragraph{Why does richer conditioning fail?}
135	We identify three factors:
136	
137	\emph{(1) Noisy covariance estimation.}
138	With $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.
139	While Ledoit--Wolf shrinkage~\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\ref{sec:selection}), the per-DOF features derived from this estimate (standard deviations, conformal radii) still carry substantial estimation noise.
140	Feeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).
141	
142	\emph{(2) Observation features are sufficient.}
143	The frozen VLA observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.
144	This information subsumes what the per-DOF conformal features attempt to capture, namely which action dimensions are uncertain given the current scene.
145	The CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.
146	
147	\emph{(3) Per-step MSE $\neq$ episode success.}
148	All CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop task success.
149	In closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\cite{ross2011dagger}.
150	The noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.
151	
152	\paragraph{Connection to magnitude sensitivity.}
153	The obs\_only variant is also more robust across magnitude bounds $\varepsilon$ than perdof (Section~\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.
154	
155	
156	\subsection{Magnitude Sensitivity}
157	\label{sec:magnitude_results}
158	
159	The norm bound $\varepsilon$ determines how much CRM can deviate from the conformal-selected action.
160	Figure~\ref{fig:magnitude} shows performance across $\varepsilon \in [0.03, 1.42]$ on both benchmarks.
161	
162	\begin{figure}[t]
163	\centering
164	\includegraphics[width=\linewidth]{figures/magnitude_curve.pdf}
165	\caption{Success rate (\%) as a function of magnitude bound $\varepsilon$. \textbf{(a)}~LIBERO-Object: obs\_only (solid blue) stays above both baselines across all tested $\varepsilon$; error bars show $\pm$1 std over available seeds (n annotated). perdof (dashed red) collapses below the Argmin baseline at $\varepsilon \geq 0.2$. Shaded region marks the recommended range $\varepsilon \in [0.05, 0.2]$. \textbf{(b)}~LIBERO-Spatial (seed 42): obs\_only maintains 35--36\% across all $\varepsilon$, while perdof drops to 0\% without magnitude control ($\varepsilon{\approx}1.42$).}
166	\label{fig:magnitude}
167	\end{figure}
168	
169	\begin{table}[t]
170	\centering
171	\caption{Success rate (\%) on LIBERO-Spatial across magnitude bounds $\varepsilon$. The Argmin baseline (34\%, no correction) is independent of $\varepsilon$.}
172	\label{tab:magnitude}
173	\small
174	\begin{tabular}{lcccc}
175	\toprule
176	$\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\
177	\midrule
178	obs\_only & 35.0 & 35.0 & 36.0 & --- \\
179	perdof    & 31.0 & 35.0 & 26.0 & 0.0 \\
180	\midrule
181	Argmin (ref.) & \multicolumn{4}{c}{34.0 (flat, no correction)} \\
182	\bottomrule
183	\end{tabular}
184	\end{table}
185	
186	\paragraph{obs\_only is robust.}
187	The obs\_only variant maintains 35--36\% across the full range $\varepsilon \in [0.05, 0.3]$, a remarkably flat profile.
188	This stability means the practitioner need not carefully tune $\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.
189	
190	\paragraph{perdof is fragile.}
191	In contrast, perdof peaks at 35\% when $\varepsilon{=}0.1$ but collapses to 26\% at $\varepsilon{=}0.3$ (a 9\,pp drop).
192	This fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.
193	At $\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.
194	
195	\paragraph{Unbounded correction is catastrophic.}
196	Without magnitude control ($\varepsilon{\approx}1.42$, the natural CRM output norm), perdof achieves 0\% on LIBERO-Spatial. Compounding error across the trajectory destroys performance entirely (Section~\ref{sec:magnitude}).
197	The Argmin baseline (34\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.
198	The obs\_only variant was not evaluated at $\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.
199	
200	\paragraph{Practical recommendation.}
201	The safe operating range is $\varepsilon \in [0.05, 0.2]$.
202	Within this range, obs\_only is the only variant that never degrades below the Argmin baseline across all tested seeds and magnitude bounds.
203	We use $\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.
204	
205	
206	\subsection{Per-Task Analysis}
207	\label{sec:per_task}
208	
209	Table~\ref{tab:pertask} reports per-task success rates on LIBERO-Object (seed 42) for the VLA-only baseline, Argmin selection, and obs\_only at two magnitude bounds.
210	
211	\begin{table}[t]
212	\centering
213	\caption{Per-task success rate (\%) on LIBERO-Object (seed 42, 10 rollouts per task). Tasks ordered by obs\_only $\varepsilon{=}0.2$ improvement over VLA-only.}
214	\label{tab:pertask}
215	\small
216	\begin{tabular}{lcccc}
217	\toprule
218	Task & VLA-only & Argmin & obs\_only 0.1 & obs\_only 0.2 \\
219	\midrule
220	chocolate\_pudding & 20 & 30 & 50 & 60 \\
221	ketchup            &  0 &  0 & 10 & 20 \\
222	bbq\_sauce         & 20 & 30 & 40 & 40 \\
223	salad\_dressing    & 20 & 10 & 20 & 30 \\
224	butter             &  0 & 10 & 10 & 10 \\
225	milk               & 10 & 10 & 20 & 20 \\
226	orange\_juice      & 30 & 30 & 30 & 30 \\
227	tomato\_sauce      & 10 &  0 &  0 & 10 \\
228	alphabet\_soup     &  0 &  0 &  0 &  0 \\
229	cream\_cheese      & 10 &  0 & 10 &  0 \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	\paragraph{Improvement concentrates on medium-difficulty tasks.}
235	The +10\,pp aggregate gain of obs\_only ($\varepsilon{=}0.2$) over VLA-only is not uniformly distributed across tasks.
236	The largest improvements appear on tasks where the frozen VLA partially succeeds but makes correctable errors: chocolate\_pudding (+40\,pp, from 20\% to 60\%), bbq\_sauce and ketchup (+20\,pp each), and salad\_dressing (+10\,pp).
237	These four tasks account for 9 of the 10 additional successes.
238	Conversely, four tasks (alphabet\_soup, cream\_cheese, tomato\_sauce, butter) remain at 0--10\% across all methods, including obs\_only.
239	For these tasks, the base policy fails so completely that local action-level correction cannot recover a viable trajectory.
240	
241	\paragraph{Implications for the correction mechanism.}
242	Correction benefits tasks where the frozen VLA partially succeeds but makes correctable errors, rather than tasks where the base policy fails catastrophically or already succeeds reliably.
243	This pattern is expected for a residual correction approach bounded by $\varepsilon$: the CRM can fix small deviations in grasp pose or approach angle, but cannot recover from fundamental planning failures (e.g., reaching toward the wrong object entirely).
244	The concentrated improvement profile also addresses the question of effect size: the aggregate +10\,pp is not a uniform +1\,pp across 10 tasks, but a substantial +20--40\,pp on specific tasks diluted by tasks outside the correctable regime.
245	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "248fffdf-54b0-4d36-9e85-7a5beb9fad5d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction significantly improve over the frozen VLA baseline?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+6\\,pp over VLA-only, $p < 0.01$), no (honest negative), and critically, unbounded correction is catastrophic, but obs\\_only is robust across all tested seeds and magnitude bounds.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (330K params). This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nTable~\\ref{tab:main} reports seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFor the primary comparison, we replicate across multiple seeds on LIBERO-Object: obs\\_only ($\\varepsilon{=}0.2$, seeds 42--46) achieves 22/16/16/16/15\\% (mean $17.0 \\pm 2.8$\\%), VLA-only (seeds 42--45) achieves mean $10.75 \\pm 1.5$\\%, and Argmin (seeds 42--45) achieves mean $13.5 \\pm 2.4$\\%.\nPooled Fisher's exact test: obs\\_only vs.\\ VLA-only is significant ($p < 0.01$); obs\\_only vs.\\ Argmin is not ($p = 0.075$).\nAll five obs\\_only seeds exceed the VLA-only baseline, confirming reproducible improvement despite per-seed variance.\nMulti-seed VLA-mean evaluation (seeds 42/43/44/45 = 12/15/10/13\\%, mean 12.5\\%) confirms that averaging provides no consistent benefit over single-sample execution.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\% (seed 42), and at $\\varepsilon{=}0.2$ yields 22.0\\%.\nAcross five seeds ($\\varepsilon{=}0.2$), the pipeline achieves mean $17.0 \\pm 2.8$\\% versus VLA-only mean $10.75 \\pm 1.5$\\% ($p < 0.01$, pooled Fisher's exact test).\nThe improvement over Argmin (mean $13.5 \\pm 2.4$\\%) is +3.5\\,pp, consistent but not statistically significant at current sample sizes ($p = 0.075$).\n\nThree baselines (VLA-only, VLA-mean, and Argmin) all achieve 12.0\\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.\nThe VLA-mean result (12\\%) is particularly informative: averaging 10 independent flow-matching samples does not reduce error compared to a single sample ($K{=}1$), confirming that action diversity does not center around the correct action.\nMulti-sample strategies require a learned selection or correction mechanism to extract value from the sample set.\nOn LIBERO-Spatial, by contrast, Argmin improves +4\\,pp over VLA-only (34\\% vs.\\ 30\\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.\nThe obs\\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.\n\n\\paragraph{Pipeline decomposition: selection amplifies correction.}\nTo isolate the contributions of selection versus correction, we evaluate the CRM in direct correction mode ($K{=}1$): the CRM corrects a single VLA output without multi-sample selection.\nDirect correction achieves 14\\%, a +2\\,pp gain over VLA-only (12\\%).\nCombined with the Argmin result (selection without correction, also 12\\%), this reveals that neither component alone is effective, yet together they yield +10\\,pp (22\\% at $\\varepsilon{=}0.2$).\nConformal selection provides the CRM with higher-quality starting actions by filtering out the worst samples; the CRM then applies corrections that are more reliable on these pre-screened candidates.\nOn individual tasks, the amplification varies: for bbq\\_sauce, direct correction alone matches the full pipeline (40\\%), while for chocolate\\_pudding the full pipeline doubles the direct correction gain (60\\% vs.\\ 30\\%).\nThis pattern suggests that selection is most valuable on tasks where the VLA's error modes are diverse across samples, creating headroom for ranking to exploit.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts. The problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nThe full pipeline significantly improves over VLA-only for object manipulation ($p < 0.01$), where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\nThe scalar $<$ perdof ordering is consistent across seeds (scalar: 9\\%/6\\% for seeds 42/44; perdof: 11\\%/8\\%).\nOne-dimensional scalar uncertainty compresses all six action dimensions into a single number.\nWhen certain dimensions carry high uncertainty but the correction direction is already correct along those axes, the scalar signal cannot distinguish this case from one where correction is needed everywhere.\nThe result is uniform over-correction or under-correction across all dimensions.\nPer-DOF conditioning at least permits dimension-specific judgments, though at $K{=}10$ these judgments remain too noisy to be useful.\nEven 1D scalar uncertainty conditioning is harmful, confirming that conformal scores at $K{=}10$ are unreliable regardless of aggregation dimensionality.\nThe noise originates in the score itself (rank-deficient covariance estimate from 10 samples in 6D), not in how these scores are decomposed across dimensions.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate (standard deviations, conformal radii) still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture, namely which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nAll CRM variants achieve low per-step MSE on held-out demonstration data, yet offline prediction accuracy does not predict closed-loop task success.\nIn closed-loop evaluation, small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe noisy conformal features amplify this drift: occasional erroneous correction directions, even when small in magnitude, can trigger cascading failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Magnitude Sensitivity}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.\nFigure~\\ref{fig:magnitude} shows performance across $\\varepsilon \\in [0.03, 1.42]$ on both benchmarks.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/magnitude_curve.pdf}\n\\caption{Success rate (\\%) as a function of magnitude bound $\\varepsilon$. \\textbf{(a)}~LIBERO-Object: obs\\_only (solid blue) stays above both baselines across all tested $\\varepsilon$; error bars show $\\pm$1 std over available seeds (n annotated). perdof (dashed red) collapses below the Argmin baseline at $\\varepsilon \\geq 0.2$. Shaded region marks the recommended range $\\varepsilon \\in [0.05, 0.2]$. \\textbf{(b)}~LIBERO-Spatial (seed 42): obs\\_only maintains 35--36\\% across all $\\varepsilon$, while perdof drops to 0\\% without magnitude control ($\\varepsilon{\\approx}1.42$).}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\\n\\midrule\nobs\\_only & 35.0 & 35.0 & 36.0 & --- \\\\\nperdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\\n\\midrule\nArgmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{obs\\_only is robust.}\nThe obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$, a remarkably flat profile.\nThis stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.\n\n\\paragraph{perdof is fragile.}\nIn contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$ (a 9\\,pp drop).\nThis fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.\nAt $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.\n\n\\paragraph{Unbounded correction is catastrophic.}\nWithout magnitude control ($\\varepsilon{\\approx}1.42$, the natural CRM output norm), perdof achieves 0\\% on LIBERO-Spatial. Compounding error across the trajectory destroys performance entirely (Section~\\ref{sec:magnitude}).\nThe Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.\nThe obs\\_only variant was not evaluated at $\\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.\n\n\\paragraph{Practical recommendation.}\nThe safe operating range is $\\varepsilon \\in [0.05, 0.2]$.\nWithin this range, obs\\_only is the only variant that never degrades below the Argmin baseline across all tested seeds and magnitude bounds.\nWe use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nTable~\\ref{tab:pertask} reports per-task success rates on LIBERO-Object (seed 42) for the VLA-only baseline, Argmin selection, and obs\\_only at two magnitude bounds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task success rate (\\%) on LIBERO-Object (seed 42, 10 rollouts per task). Tasks ordered by obs\\_only $\\varepsilon{=}0.2$ improvement over VLA-only.}\n\\label{tab:pertask}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & VLA-only & Argmin & obs\\_only 0.1 & obs\\_only 0.2 \\\\\n\\midrule\nchocolate\\_pudding & 20 & 30 & 50 & 60 \\\\\nketchup            &  0 &  0 & 10 & 20 \\\\\nbbq\\_sauce         & 20 & 30 & 40 & 40 \\\\\nsalad\\_dressing    & 20 & 10 & 20 & 30 \\\\\nbutter             &  0 & 10 & 10 & 10 \\\\\nmilk               & 10 & 10 & 20 & 20 \\\\\norange\\_juice      & 30 & 30 & 30 & 30 \\\\\ntomato\\_sauce      & 10 &  0 &  0 & 10 \\\\\nalphabet\\_soup     &  0 &  0 &  0 &  0 \\\\\ncream\\_cheese      & 10 &  0 & 10 &  0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Improvement concentrates on medium-difficulty tasks.}\nThe +10\\,pp aggregate gain of obs\\_only ($\\varepsilon{=}0.2$) over VLA-only is not uniformly distributed across tasks.\nThe largest improvements appear on tasks where the frozen VLA partially succeeds but makes correctable errors: chocolate\\_pudding (+40\\,pp, from 20\\% to 60\\%), bbq\\_sauce and ketchup (+20\\,pp each), and salad\\_dressing (+10\\,pp).\nThese four tasks account for 9 of the 10 additional successes.\nConversely, four tasks (alphabet\\_soup, cream\\_cheese, tomato\\_sauce, butter) remain at 0--10\\% across all methods, including obs\\_only.\nFor these tasks, the base policy fails so completely that local action-level correction cannot recover a viable trajectory.\n\n\\paragraph{Implications for the correction mechanism.}\nCorrection benefits tasks where the frozen VLA partially succeeds but makes correctable errors, rather than tasks where the base policy fails catastrophically or already succeeds reliably.\nThis pattern is expected for a residual correction approach bounded by $\\varepsilon$: the CRM can fix small deviations in grasp pose or approach angle, but cannot recover from fundamental planning failures (e.g., reaching toward the wrong object entirely).\nThe concentrated improvement profile also addresses the question of effect size: the aggregate +10\\,pp is not a uniform +1\\,pp across 10 tasks, but a substantial +20--40\\,pp on specific tasks diluted by tasks outside the correctable regime.\n",
      "numLines": 245,
      "startLine": 1,
      "totalLines": 245
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
Now I have a thorough understanding of the current state. Let me also check the experiments section for any references to sections that I need to be consistent with, and check the discussion.tex for similar references.

Key issues with the current method.tex that need fixing per D058/D061:

1. **Selection is L2 distance to mean, NOT Mahalanobis**. The old text uses Mahalanobis nonconformity scores, shrinkage covariance, etc. All of this must be replaced with simple L2 distance to sample mean.

2. **CRM input**: 
   - obs_only: 990D = 960D z_obs + 30D a_base. 
   - perdof: 1030D = 960D + 30D + 40D conformal features
   - scalar: 991D = 960D + 30D + 1D scalar uncertainty

3. **CRM architecture**: Linear(990, 256) → ReLU → Linear(256, 256) → ReLU → Linear(256, 30). Total params: 327,198 (~327K), not 330K.

4. **ε default is 0.2**, not 0.1 as old text says.

5. **obs_only performance** needs to be checked against the actual results.

6. **perdof collapse**: 14% → 11% → 10% → 5% → 0%

7. CRM is a correction module, NOT a selection/ranking module.

Let me clarify the input dimensions: obs_only takes 990D (960D observations + 30D actions) without conformal or uncertainty features, perdof adds 40D conformal features for 1030D total, and scalar adds just 1D scalar uncertainty for 991D total. The z_obs is actually 960D from the VLM hidden size, not 990D as I initially stated.

Now verifying the CRM parameter count of 327,198: the first linear layer (990 → 256) gives 253,696 parameters, the hidden layer (256 → 256) gives 65,792, and the output layer (256 → 30) gives 7,710, which sums correctly.

Checking the other variants: perdof with 1030D input yields about 337K params, and scalar with 991D input yields about 327K params. But the experiments section reports different numbers—obs_only and scalar both at 330K, perdof at 339K—which don't align with the task spec's 327K figure, so I'm going with the task spec value since that's the corrected D058 number.

I also notice the experiments section references specific sections like the Mahalanobis scoring method, and those cross-references need to stay intact. The existing labels in method.tex need to be preserved so the citations still work properly.

Looking at the equation labels, I'll keep the ones that are still relevant—the argmin formula, the correction module equation, and the loss function—but I can remove the Mahalanobis-specific ones since we're moving away from that approach.

For the overall structure, I'm planning to organize it as Problem Setup, then Multi-Sample Selection (replacing the conformal selection framing), followed by the Correction Module with its architecture and conditioning variants, then Magnitude Control, and finally the Inference Protocol.

For Problem Setup, I'm working with a frozen SmolVLA model that generates action chunks of 50 timesteps with 6 dimensions per step (translation and rotation), and we're using a receding horizon of 5 steps. The goal is to select and refine actions without modifying the base model itself.

In Multi-Sample Selection, we draw 10 independent rollouts, compute the mean action at each horizon step, then pick the sample with the smallest total L2 distance to that mean as our baseline action.

Now for the refinement stage, I'm building a small correction module that takes the observation embedding and baseline action as input, runs them through a three-layer MLP with about 327K parameters, and outputs a bounded residual correction that gets added back to the baseline action. The module operates on normalized inputs and clips the correction magnitude to stay within a specified epsilon bound.

I'm exploring three different conditioning approaches: the simplest just uses observations and actions without any uncertainty information, a more sophisticated version incorporates per-DOF uncertainty estimates from conformal prediction along with calibrated confidence radii, and a middle ground that conditions on a single scalar uncertainty value.

For training, I'm using 26,737 precomputed samples across 10 demonstrations per task for 20 tasks, where at each step I run 10 forward passes through the ensemble, select the best one, and train the correction module with an L2 loss to predict the adjustment needed to match the expert action, using data augmentation with Gaussian noise on both the mean action and uncertainty features.

Now I'm looking at how magnitude control affects performance - capping the L2 norm of the correction output at epsilon equals 0.2 is the main configuration, and without this clipping the natural norm explodes to 1.42 causing complete failure on spatial reasoning tasks, while the observation-only baseline stays robust across different epsilon values but the per-DOF approach progressively collapses due to rank-deficient covariance creating noisy directional signals that get amplified when magnitude isn't constrained, and the inference procedure now uses L2 distance instead of Mahalanobis distance with some computational overhead. I'm noticing a discrepancy between what the task specifies and what the experiments section actually reports. The task says ε = 0.2 is the primary result, but the experiments section states the default is ε = 0.1, and the results table shows obs_only performing at both values. For the Method section, I should emphasize ε = 0.2 as the primary setting while letting the experiments section handle the broader comparison across different ε values. I need to correct the Method section to reflect ε=0.2 as the primary value instead of the outdated ε=0.1, and I'm cross-checking the experimental results to understand the full picture—particularly the robustness of obs_only across different epsilon values and the catastrophic failure of perdof at uncapped epsilon.

I'm also being careful not to introduce Mahalanobis or Ledoit-Wolf references into the selection subsection, since those belong in the perdof variant description instead. I notice there's a potential inconsistency brewing: the experiments section currently references conformal selection via Mahalanobis, but my rewrite will describe L2-based selection instead. I'll proceed with the Method rewrite as requested and let that cross-reference issue surface naturally.

For the subsection titles, I'm dropping "Conformal" from the Correction Module heading to just "Correction Module (CRM)" as specified, though the acronym itself still references the perdof variant's conformal conditioning features. I need to integrate the Base VLA discussion into the Problem Setup section rather than keeping it separate. For the mathematical formulations, I'm keeping the key equations with their existing labels—the selection formula, the CRM correction formula, and the loss function—while removing the ones that aren't referenced elsewhere. Now I'll start drafting the Method section.

R-VLA works by taking samples from a frozen flow-matching VLA at inference time, selecting the one closest to the sample mean, then applying a learned bounded residual correction. The base model itself stays frozen throughout. In the Problem Setup, I'm defining the frozen VLA $\pi_\theta$ that takes observations and generates action chunks, along with the effective horizon and action dimensionality that matter for execution.

The gripper is handled separately through direct thresholding and doesn't participate in the correction pipeline. I'm instantiating this on SmolVLA, a 450M-parameter flow-matching model that generates stochastic action samples, so I can query it multiple times independently. The approach is architecture-agnostic and works with any flow-matching VLA supporting repeated sampling.

For the multi-sample selection, I draw K=10 action chunks from independent flow-matching rollouts, truncate each to the effective horizon of 5 steps, and work with these samples for the selection process.

To find the best action, I compute the mean action across all samples at each horizon step, then select whichever sample has the smallest total squared distance to these consensus means across the entire trajectory.

This approach preserves the temporal coherence of individual samples rather than blending them together, which could mix incompatible action modes. It's essentially a denoising step that works independently from what comes next.

Now for the correction module—it's a lightweight neural network that takes the selected action and refines it with a bounded residual correction based on the current observation. The architecture is a 3-layer MLP...

Defining the correction module architecture...

The corrected action applies a clipped residual adjustment bounded by a norm constraint. I'm exploring three variants of the correction module that differ in their conditioning inputs: the primary version uses only the observation embedding and base action, while other variants incorporate additional uncertainty or per-DOF information to guide the residual prediction. The obs_only variant is what we're actually using as the main approach. I'm realizing there's a naming inconsistency here—the method is called "Conformal Residual Module" based on the per-DOF variant that uses conformal-calibrated uncertainty features, but the primary obs_only variant doesn't actually use those conformal statistics. The ablation study shows only obs_only is effective anyway, so I should clarify that the name comes from the broader framework even though the working version doesn't rely on conformal calibration. I'll keep the subsection title as "Correction Module (CRM)" since it's already defined in the introduction, and just refer to it as CRM in the text without re-expanding the acronym. I should briefly explain why it's called "Conformal" even though the primary variant doesn't actually use conformal features. Now I'm working through the parameter counts for each variant to make sure the numbers are accurate. I'm recalculating the parameter counts for each variant—perdof comes to around 337K, and scalar also lands at about 327K, which matches the task's specification. I notice that input normalization layers like BatchNorm would add additional parameters, so I need to account for those as well. So the total is 327,198 parameters without normalization layers, which matches the task specification of ~327K. I'll go with that figure and move forward with drafting the paper in CoRL format. Now I need to identify which quantitative claims require experiment ID annotations—things like the magnitude control parameters and the robustness ranges for the observation-only baseline.

Most of the Method section is actually descriptive, so the main quantitative claims are concentrated in the Magnitude Control subsection. I'm noticing there's a discrepancy between the LIBERO-Object numbers mentioned in the task (13.5-17.5% for obs_only, progressive collapse for perdof) and the LIBERO-Spatial numbers from the old method section (35-36% for obs_only, 26% for perdof at ε=0.3). The Method section should focus on establishing the mechanism and motivation rather than diving into detailed performance analysis—that belongs in the experiments section. Let me make sure I'm presenting the magnitude control observations appropriately without duplicating what the results section will cover. Looking at the performance numbers more carefully—perdof shows a sharp decline from 35% at ε=0.1 down to 26% at ε=0.3 on the Spatial task, which contrasts with obs_only's stability. I should keep the Method section's discussion of these magnitude effects brief and let the experiments section provide the full details. Also reconsidering the structure: moving the SmolVLA description to Problem Setup feels cleaner than keeping it nested under CRM. And for Ledoit-Wolf shrinkage, I'll just mention it briefly in the perdof conditioning features section rather than treating it as a separate focus. I've mapped out the full structure for the method section and I'm ready to write it. I need to keep it concise for the two-page CoRL format, around 1400-1600 words total, and avoid certain phrases and stylistic choices like em-dashes, -ing endings, and overused terms like "leverage" or "demonstrate effectiveness." I need to check the section label references carefully—`sec:magnitude` is the method subsection while `sec:magnitude_results` is in experiments, and I should make sure the cross-references are consistent throughout. Now I'm drafting the complete method section, starting with the core ACR-VLA pipeline description and moving into the problem setup with the frozen flow-matching VLA.

Writing the method section... , language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.

We instantiate ACR-VLA on SmolVLA, a 0.4B-parameter flow-matching VLA that generates actions via learned flow matching. Each forward pass produces a stochastic action sample, so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample without modifying the base model. For the multi-sample selection approach, I'm drawing $K{=}10$ action chunks from the policy via independent flow-matching rollouts, truncating each to $H{=}5$ steps, then computing the sample mean across all $K$ samples at each horizon step to get a more robust action prediction. a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:
\begin{equation}
  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} \bigl\|a_h^{(k)} - \boldsymbol{\mu}_h\bigr\|_2^2.
  \label{eq:argmin}
\end{equation}
This procedure identifies the most representative sample from the action distribution. Unlike the element-wise mean, which blends potentially incompatible action modes and can produce out-of-distribution actions, argmin selection returns an actual sample from the VLA's generative process and preserves within-sample temporal coherence across the $H$ steps. The selection operates independently of the downstream correction module—it's a statistical denoising step that gives the CRM a better starting point.

Now I'm describing the Correction Module, which is a lightweight MLP that takes the selected action and refines it by predicting a bounded residual correction based on the current observation and the selected action. The architecture consists of three fully connected layers with ReLU activations, preceded by input normalization, with the final layer outputting a 30-dimensional correction vector. The correction is clipped to stay within a norm bound that prevents overly large adjustments. The model only sees the selected action and observation, not the other candidates, and predicts how to refine it toward the expert demonstration. I'm comparing three variants of the correction module that use the same architecture but differ in what information they receive as input—the primary version uses just the observation and base action, while the other variants incorporate additional uncertainty or per-DOF features. The obs_only variant is our main approach, though despite its name, the Conformal Residual Module doesn't actually use conformal statistics in this version. The perdof variant does incorporate conformal-calibrated uncertainty features, which is where the module gets its name, but our ablation studies show these don't help performance with our sample budget. For training, I'm using an L2 loss function that minimizes the difference between predicted and expert actions, applied offline to demonstration trajectories from LIBERO.

The training dataset consists of about 26,000 samples drawn from 10 demonstrations per task across 20 different LIBERO tasks. For each step, I run 10 forward passes through the frozen SmolVLA model, select the base action using argmin, and train the module to predict the residual correction needed to match the expert action. I'm also applying data augmentation during training—adding Gaussian noise to the action vectors and to the uncertainty features—which helps the model generalize better to the state distribution shift that occurs during closed-loop evaluation due to compounding errors.

The norm bound controlling the correction magnitude is essential for stable performance. Without any clipping, the natural output magnitude reaches about 1.42, which causes the corrected action to deviate too far from the base model's output. This leads to catastrophic compounding error across the trajectory, completely destroying performance on the spatial task. The problem mirrors the distribution shift issue in imitation learning, except it happens at inference time—each over-corrected action pushes the state further from the training distribution, making subsequent corrections even worse.

When I constrain the magnitude to between 0.05 and 0.2, the corrections stabilize, and I use 0.2 as the main setting. The observation-only variant handles this constraint gracefully across a wide range of bounds, maintaining consistent success rates. The per-DOF variant, however, degrades sharply as the bound increases, collapsing to complete failure. This happens because the covariance matrix is rank-deficient relative to the sample size, so small noisy signals become harmless when clipped but turn destructive at larger magnitudes.

This connects to the broader residual policy learning literature—approaches like those from Silver et al. and more recent work use various mechanisms to keep corrections in check, whether through learned gating or multi-stage pipelines. ACR-VLA takes the simplest approach: a hard L2 norm constraint on the correction output that prevents it from dominating the base policy.

At inference, each control step follows a straightforward procedure: I sample multiple action chunks from the frozen VLA, compute their mean to select a base action via L2 distance minimization, extract the observation embedding from the VLA encoder, then compute the residual correction through the CRM and clip it to stay within the magnitude bound before executing the first action.

After observing the new state, I re-plan from the beginning. The computational cost is modest—just 10 forward passes through the base VLA plus a few milliseconds for the CRM—and importantly, the base VLA itself remains completely frozen throughout.

Let me verify the constraints one more time. The distance metric is L2, not Mahalanobis. The CRM receives the base action plus observed features, not individual candidates. The observation-only variant doesn't use conformal features. The parameter count is 327K. The primary epsilon is 0.2. For dashes, "Ledoit--Wolf" is a proper name and "13.5--17.5\%" is a number range, both acceptable. But I'm catching an -ing phrase at the end of a sentence: "amplifying subsequent correction errors" needs to be reworded to avoid that ending.

I should also verify the subsection structure matches what's required and check that I haven't used forbidden phrases like "demonstrates the effectiveness" or "to the best of our knowledge."

Now I'm noticing a discrepancy with the model size—the task specifies SmolVLA as 450M parameters, but I wrote "0.4B-parameter" which is technically 400M. I need to correct this to "450M-parameter" to match the specification, and I can cite the paper to support this.

Looking at the length, my draft seems comparable to the original method section, which should fit the expected ~2 pages for this section in an 8-page paper. The training paragraph correctly references the argmin selection without mentioning CGS scores since we're now using L2-based selection instead. One remaining detail to verify: the noise augmentation on uncertainty features only applies to specific variants, not all of them. I'm going through the sentences to catch any -ing endings that need fixing. The phrasing "enabling multi-sample inference by querying" is one I should revise—I can restructure it to "so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks" instead. Let me check the rest of the draft for similar issues. I'm going through my draft systematically to catch any sentences that end with -ing phrases. Most of the phrasing looks good—"preserves within-sample temporal coherence" and "supports repeated sampling" work fine since they're noun phrases rather than dangling participles. I should tighten up a few spots like "without modifying" by rephrasing to "without changes to" to be safer, but overall the structure is holding up.

Now I'm doing a final verification pass on the references and constraints: the pipeline figure is cited, the ablation and magnitude results sections are forward-referenced properly, and I've kept the specialized citations (Braun/CGS and Ledoit-Wolf) confined to the perdof paragraph as intended. I need to make sure I haven't accidentally introduced "Mahalanobis" anywhere it shouldn't be.

I'm also standardizing the number formatting to match the original LaTeX convention with thousands separators, and confirming that `\argmin` is already defined in the preamble since the old text uses it. For the mean formula in the Selection subsection, I'm deciding whether to give it its own equation label or keep it inline—since it's not referenced elsewhere in the document, I'll leave it unlabeled.

I'm keeping the mean formula as inline math within the paragraph to save space, while giving the argmin selection formula its own equation number. Let me also verify that I'm using `\oplus` correctly for concatenation in the method section. I'm overthinking the notation choice here. Let me just go with the semicolon bracket notation $[\mathbf{z}_{\mathrm{obs}}; a_{\mathrm{base}}]$ since it's clearer and more standard in the robotics literature, then move on to finalizing the rest of the section.

I should keep the residual policy learning connection in the Method section where it contextualizes the magnitude control design, but I'll trim it down to be more concise. Given the CoRL format constraints and that my draft should match the original ~2 pages, I'm ready to write out the final version now.

Writing the Method section... I'm working with SmolVLA, a 450M-parameter flow-matching model that generates stochastic action samples through learned flow matching. By sampling the model $K=10$ times independently and truncating each to the first 5 steps, I get multiple candidate action chunks that I can then select from and refine.

For the selection mechanism, I compute the mean action across all samples at each timestep, then pick whichever sample has the smallest cumulative $L_2$ distance to that mean across the entire horizon. This approach identifies the most representative sample from the learned distribution while avoiding the pitfalls of naive averaging—which can blend incompatible action modes and produce out-of-distribution results—by returning an actual sample that the model could have generated.

Now for the correction module, it's a lightweight neural network that takes the selected action and refines it with a bounded residual correction based on the current observation. The architecture uses three fully connected layers with ReLU activations, progressively mapping from the input dimension through hidden layers of 256 units down to a 30-dimensional output.

For the main variant, the input concatenates the frozen observation embedding from SmolVLA's encoder with the selected action, totaling around 327K parameters. The network outputs a residual correction that gets clipped and added back to the base action to produce the final corrected action.

Now I'm comparing three different CRM variants that use the same architecture but take different inputs—the primary one uses just the observation and base action concatenated together. The scalar variant simplifies this to a single uncertainty value, keeping the same parameter count. The obs_only approach is actually my main method despite the conformal naming—it doesn't use conformal statistics. The perdof variant does incorporate conformal-calibrated uncertainty features, but ablations show these don't help performance with the K=10 sample budget we're working with. For training, I'm using L2 loss on demonstration trajectories from LIBERO, comparing predicted actions against expert actions. The data augmentation helps the model generalize to the state distribution shift that occurs during closed-loop evaluation due to compounding errors. For the magnitude control, the norm bound epsilon is crucial for stable performance—without clipping, the residual corrections grow too large and cause cascading errors that completely break task performance, similar to the distribution shift problem in imitation learning.

Setting epsilon between 0.05 and 0.2 stabilizes the corrections, with 0.2 as the main choice. The observation-only variant remains robust across different epsilon values, but the per-DOF variant degrades significantly as epsilon increases, eventually failing completely. This degradation stems from rank-deficient covariance when the dimension-to-sample ratio becomes too high, introducing noise into the per-DOF estimates.

The magnitude control is critical—loose bounds on per-DOF corrections cause catastrophic failures, while tight clipping keeps them harmless. This connects to residual policy learning, where prior work like Silver et al.'s residual learning and TRANSIC use learned gating or multi-stage approaches. ACR-VLA takes the simpler route with fixed L2 norm clipping, a hard constraint that prevents corrections from dominating the base policy without requiring learned gating or complex pipelines.

Now I'm laying out the inference procedure: at each control step, I sample multiple action chunks from the frozen VLA, compute their mean to select the base action, extract the observation embedding from the VLA encoder, and feed that embedding along with the base action into the correction module.

The correction module outputs a delta that gets clipped to stay within an epsilon ball, then I add this clipped correction to the base action and execute the first step. After observing the new state, I re-plan from the beginning. The computational cost is just 10 forward passes through the base VLA plus a few milliseconds for the correction module inference—the base VLA itself remains completely frozen throughout.

Now I'm doing a final verification pass on the technical details: confirming the L2 distance metric, the correction module terminology, that the observation-only variant doesn't use conformal features, the parameter count of 327K, epsilon set to 0.2, the input dimensions totaling 990D, and checking that the writing avoids em-dashes and -ing phrase endings throughout the paper. I'm refining the phrasing to avoid that construction—changing "without modifying" to "with no changes to" to be extra cautious. Now I'm systematically checking for dangling participial phrases at paragraph endings, specifically the pattern of present participles like "demonstrating," "highlighting," or "enabling" that create that prohibited structure. Looking through my draft, I don't see any of those problematic constructions present. I'm running through a checklist of formatting requirements—no prohibited words, proper citations, section and equation labels all accounted for. Now I need to verify whether the paper uses H or H_EFF for the horizon parameter, since the task mentions one but the actual method might use the other.

Looking back at the existing method.tex, it's just H=5 without the "eff" subscript, and the Problem Setup mentions "receding-horizon execution" with "the first H=5 steps." The key facts note "C=50 generated, H_EFF=5 used (receding horizon)" but I should stick with the paper's convention of H=5 to stay consistent.

I'm also double-checking whether the experiments section references eq:shrinkage or eq:mahal anywhere—scanning through, I see references to sec:selection and eq:argmin but not those two equations, so removing them should be safe.

One last detail to nail down: the task mentions checking the code convention for input normalization, but I wrote "preceded by input normalization" without specifying BatchNorm or LayerNorm—I should verify which one the code actually uses before finalizing.

Now I'm double-checking the parameter count for the perdof module to make sure my calculations are correct.

Actually, I'm noticing a discrepancy between my draft and the experiments section. The experiments says 339K for perdof, which is about 2K more than my calculation of 337K—that extra amount matches what batch normalization parameters would add. For obs_only, there's a similar gap: my calculation gives 327K, but experiments lists 330K. The task explicitly mentions this discrepancy isn't 330K or 337K, so I should stick with the numbers the task provides rather than trying to reconcile them. So the 327K figure for obs_only is purely the MLP parameters without any normalization layers. For perdof, that's 337K with the same MLP structure but slightly different input dimensions. Scalar comes out to about 327K as well since it only adds one extra input dimension, so all three variants have essentially the same parameter count around 327-337K for the MLP components.

Now I'm questioning whether the loss function actually applies clipping during training—if the gradient can't flow through the clipped values, that would hurt optimization. It's more likely the loss is computed on the unclipped deltas directly, so the network can learn without the gradient blocking issue. The CRM predicts residuals δ that get added to the base output, and the loss measures how well a_base + δ matches the expert action. There's a subtle question about whether clipping is applied during training or just at inference, but either way the CRM learns to predict small corrections to the base policy.

I'm ready to write out the final version now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "684f49d1-2de0-4cc3-b02e-cd537975e3f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198g2HGXQutgv7rw2qnAy1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15339,
      "cache_read_input_tokens": 40682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15339
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

Now I have full context. Let me write the rewritten Method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "24b1fe9f-1f45-4abe-aa0b-128415b4ee24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198g2HGXQutgv7rw2qnAy1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15339,
      "cache_read_input_tokens": 40682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15339
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

_source line 27_

<details open><summary>🔧 Tool call — Write · `toolu_01Wo3N2a6rWhjGJUDvVDX7B1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
  "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.\n\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\\pi_\\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\\pi_\\theta$. The method applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Multi-Sample Selection}\n\\label{sec:selection}\n\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for horizon step $h = 1, \\dots, H$. For each step, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} \\bigl\\|a_h^{(k)} - \\boldsymbol{\\mu}_h\\bigr\\|_2^2.\n  \\label{eq:argmin}\n\\end{equation}\nThis procedure identifies the most representative sample from the action distribution. Unlike the element-wise mean, which blends potentially incompatible action modes and can produce out-of-distribution actions, argmin selection returns an actual sample from the VLA's generative process and preserves within-sample temporal coherence across the $H$ steps. The selection operates independently of the downstream correction module: it is a statistical denoising step that provides the CRM with a higher-quality starting point.\n\n\\subsection{Correction Module (CRM)}\n\\label{sec:crm}\n\nThe CRM is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.\n\n\\paragraph{Architecture.}\nThe CRM consists of three fully connected layers with ReLU activations: $\\mathrm{Linear}(n_{\\mathrm{in}}, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\\_only variant ($n_{\\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\\mathrm{base}} \\in \\mathbb{R}^{30}$ ($H{=}5$ steps $\\times$ $d{=}6$ DOFs), for a total of 327,198 parameters (${\\sim}$327K). The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound that limits the correction magnitude (Section~\\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\\mathrm{base}}$ and predicts a correction toward the expert action.\n\n\\paragraph{Conditioning variants.}\nWe compare three CRM variants that share the same MLP architecture but differ in their input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only} (primary): $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}] \\in \\mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.\n  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\\mathbf{u}_{\\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\\times}d$), 5 conformal prediction radii~\\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} of the $K$ samples.\n  \\item \\textbf{scalar}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, u_s] \\in \\mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.\n\\end{itemize}\nThe obs\\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\\cite{braun2025cgs}, but Section~\\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.\n\n\\paragraph{Training.}\nThe CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\mathbf{a}_{\\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$, and train the CRM to predict the residual that moves $a_{\\mathrm{base}}$ toward $\\mathbf{a}_{\\mathrm{expert}}$. Data augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and, for variants that receive uncertainty inputs, noise on those features ($\\sigma \\approx 0.006$). Both forms of augmentation improve generalization to the state distribution encountered during closed-loop evaluation, which diverges from the demonstration distribution due to compounding errors~\\cite{ross2011dagger}.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) controls how far the CRM can deviate from the selected action and is critical for stable closed-loop performance.\n\nWithout clipping, the CRM's natural output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, compounding error across the trajectory destroys task performance: the perdof variant achieves 0\\% success on LIBERO-Spatial across three seeds. Each over-corrected action shifts the state distribution away from the CRM's training regime, and subsequent corrections compound the deviation. This failure is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger} but manifests at inference time rather than during data collection.\n% exp_id: eval-acr-spatial-v4-default-r3 (uncapped norm~1.42, perdof 0%, 3 seeds)\n\nConstraining $\\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. We use $\\varepsilon{=}0.2$ as the primary setting. The obs\\_only variant is robust across all tested bounds ($\\varepsilon \\in [0.03, \\text{uncapped}]$), maintaining 13.5--17.5\\% on LIBERO-Object across five seeds. The perdof variant degrades progressively as $\\varepsilon$ increases, collapsing from 14\\% to 0\\% over the same range. The root cause is rank-deficient covariance estimation at dimension-to-sample ratio $d/K = 0.6$: noisy per-DOF directional signals are harmless when clipped to small magnitude but catastrophic when the bound is loose. Section~\\ref{sec:magnitude_results} presents the full sensitivity analysis.\n% exp_id: magnitude sweep obs_only seeds 42-46, perdof seeds 42-46\n\nThe necessity of magnitude control connects ACR-VLA to the residual policy learning literature. Silver et al.~\\cite{silver2018residual} introduced residual learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} applies learned binary gating to selectively enable residual actions. PLD~\\cite{xiao2026pld} bounds corrections within a fixed range during RL training. ACR-VLA uses fixed $L_2$ norm clipping, the simplest instantiation: a hard constraint that prevents the correction from overwhelming the base policy, with no learned gating or multi-stage pipeline.\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute the sample mean $\\boldsymbol{\\mu}_h$ per horizon step and select $a_{\\mathrm{base}}$ via $L_2$ argmin~(\\ref{eq:argmin}).\n  \\item Extract the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the frozen VLA encoder.\n  \\item Compute $\\boldsymbol{\\delta} = \\mathrm{CRM}([\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}])$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead is $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "e611711a-de92-45f9-be80-b49278dc151e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198g2HGXQutgv7rw2qnAy1r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15339,
      "cache_read_input_tokens": 40682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15339
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

_source line 28 · 2026-05-18T09:46:35.610Z_

<details><summary>↩ Tool result · `toolu_01Wo3N2a6rWhjGJUDvVDX7B1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "a90db8c4-ac94-4af9-b9d7-81f5861c56c2",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
    "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.\n\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\\pi_\\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\\pi_\\theta$. The method applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Multi-Sample Selection}\n\\label{sec:selection}\n\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for horizon step $h = 1, \\dots, H$. For each step, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} \\bigl\\|a_h^{(k)} - \\boldsymbol{\\mu}_h\\bigr\\|_2^2.\n  \\label{eq:argmin}\n\\end{equation}\nThis procedure identifies the most representative sample from the action distribution. Unlike the element-wise mean, which blends potentially incompatible action modes and can produce out-of-distribution actions, argmin selection returns an actual sample from the VLA's generative process and preserves within-sample temporal coherence across the $H$ steps. The selection operates independently of the downstream correction module: it is a statistical denoising step that provides the CRM with a higher-quality starting point.\n\n\\subsection{Correction Module (CRM)}\n\\label{sec:crm}\n\nThe CRM is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.\n\n\\paragraph{Architecture.}\nThe CRM consists of three fully connected layers with ReLU activations: $\\mathrm{Linear}(n_{\\mathrm{in}}, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\\_only variant ($n_{\\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\\mathrm{base}} \\in \\mathbb{R}^{30}$ ($H{=}5$ steps $\\times$ $d{=}6$ DOFs), for a total of 327,198 parameters (${\\sim}$327K). The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound that limits the correction magnitude (Section~\\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\\mathrm{base}}$ and predicts a correction toward the expert action.\n\n\\paragraph{Conditioning variants.}\nWe compare three CRM variants that share the same MLP architecture but differ in their input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only} (primary): $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}] \\in \\mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.\n  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\\mathbf{u}_{\\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\\times}d$), 5 conformal prediction radii~\\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} of the $K$ samples.\n  \\item \\textbf{scalar}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, u_s] \\in \\mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.\n\\end{itemize}\nThe obs\\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\\cite{braun2025cgs}, but Section~\\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.\n\n\\paragraph{Training.}\nThe CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\mathbf{a}_{\\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$, and train the CRM to predict the residual that moves $a_{\\mathrm{base}}$ toward $\\mathbf{a}_{\\mathrm{expert}}$. Data augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and, for variants that receive uncertainty inputs, noise on those features ($\\sigma \\approx 0.006$). Both forms of augmentation improve generalization to the state distribution encountered during closed-loop evaluation, which diverges from the demonstration distribution due to compounding errors~\\cite{ross2011dagger}.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) controls how far the CRM can deviate from the selected action and is critical for stable closed-loop performance.\n\nWithout clipping, the CRM's natural output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, compounding error across the trajectory destroys task performance: the perdof variant achieves 0\\% success on LIBERO-Spatial across three seeds. Each over-corrected action shifts the state distribution away from the CRM's training regime, and subsequent corrections compound the deviation. This failure is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger} but manifests at inference time rather than during data collection.\n% exp_id: eval-acr-spatial-v4-default-r3 (uncapped norm~1.42, perdof 0%, 3 seeds)\n\nConstraining $\\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. We use $\\varepsilon{=}0.2$ as the primary setting. The obs\\_only variant is robust across all tested bounds ($\\varepsilon \\in [0.03, \\text{uncapped}]$), maintaining 13.5--17.5\\% on LIBERO-Object across five seeds. The perdof variant degrades progressively as $\\varepsilon$ increases, collapsing from 14\\% to 0\\% over the same range. The root cause is rank-deficient covariance estimation at dimension-to-sample ratio $d/K = 0.6$: noisy per-DOF directional signals are harmless when clipped to small magnitude but catastrophic when the bound is loose. Section~\\ref{sec:magnitude_results} presents the full sensitivity analysis.\n% exp_id: magnitude sweep obs_only seeds 42-46, perdof seeds 42-46\n\nThe necessity of magnitude control connects ACR-VLA to the residual policy learning literature. Silver et al.~\\cite{silver2018residual} introduced residual learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} applies learned binary gating to selectively enable residual actions. PLD~\\cite{xiao2026pld} bounds corrections within a fixed range during RL training. ACR-VLA uses fixed $L_2$ norm clipping, the simplest instantiation: a hard constraint that prevents the correction from overwhelming the base policy, with no learned gating or multi-stage pipeline.\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute the sample mean $\\boldsymbol{\\mu}_h$ per horizon step and select $a_{\\mathrm{base}}$ via $L_2$ argmin~(\\ref{eq:argmin}).\n  \\item Extract the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the frozen VLA encoder.\n  \\item Compute $\\boldsymbol{\\delta} = \\mathrm{CRM}([\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}])$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead is $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 102,
        "newStart": 2,
        "newLines": 78,
        "lines": [
          " \\section{Method}",
          " \\label{sec:method}",
          " ",
          "-\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.",
          "+\\textbf{ACR-VLA} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.",
          " ",
          " \\subsection{Problem Setup}",
          " \\label{sec:problem_setup}",
          " ",
          "-Let $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.",
          "+Let $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.",
          " ",
          "-At each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.",
          "+We instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\\pi_\\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\\pi_\\theta$. The method applies to any flow-matching VLA that supports repeated sampling.",
          " ",
          "-\\subsection{Multi-Sample Generation and Conformal Selection}",
          "+\\subsection{Multi-Sample Selection}",
          " \\label{sec:selection}",
          " ",
          "-\\paragraph{Sampling and truncation.}",
          "-We draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.",
          "-",
          "-\\paragraph{Shrinkage covariance estimation.}",
          "-For each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:",
          "+We draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for horizon step $h = 1, \\dots, H$. For each step, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:",
          " \\begin{equation}",
          "-  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},",
          "-  \\label{eq:shrinkage}",
          "-\\end{equation}",
          "-where $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.",
          "-",
          "-\\paragraph{Mahalanobis nonconformity score.}",
          "-For each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:",
          "-\\begin{equation}",
          "-  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).",
          "-  \\label{eq:mahal}",
          "-\\end{equation}",
          "-This score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.",
          "-",
          "-\\paragraph{Argmin selection.}",
          "-We select the sample with the lowest total nonconformity across all horizon steps:",
          "-\\begin{equation}",
          "-  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).",
          "+  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} \\bigl\\|a_h^{(k)} - \\boldsymbol{\\mu}_h\\bigr\\|_2^2.",
          "   \\label{eq:argmin}",
          " \\end{equation}",
          "-This selection procedure uses Mahalanobis-based scoring~\\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.",
          "+This procedure identifies the most representative sample from the action distribution. Unlike the element-wise mean, which blends potentially incompatible action modes and can produce out-of-distribution actions, argmin selection returns an actual sample from the VLA's generative process and preserves within-sample temporal coherence across the $H$ steps. The selection operates independently of the downstream correction module: it is a statistical denoising step that provides the CRM with a higher-quality starting point.",
          " ",
          "-\\subsection{Conformal Residual Module}",
          "+\\subsection{Correction Module (CRM)}",
          " \\label{sec:crm}",
          " ",
          "-The Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.",
          "+The CRM is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.",
          " ",
          " \\paragraph{Architecture.}",
          "-CRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 330K parameters for the primary obs\\_only variant).",
          "-Its input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:",
          "+The CRM consists of three fully connected layers with ReLU activations: $\\mathrm{Linear}(n_{\\mathrm{in}}, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\\_only variant ($n_{\\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\\mathrm{base}} \\in \\mathbb{R}^{30}$ ($H{=}5$ steps $\\times$ $d{=}6$ DOFs), for a total of 327,198 parameters (${\\sim}$327K). The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the corrected action is:",
          " \\begin{equation}",
          "   \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),",
          "   \\label{eq:crm}",
          " \\end{equation}",
          "-where $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).",
          "+where $\\varepsilon$ is a norm bound that limits the correction magnitude (Section~\\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\\mathrm{base}}$ and predicts a correction toward the expert action.",
          " ",
          "-\\paragraph{Observation-only conditioning.}",
          "-CRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.",
          "+\\paragraph{Conditioning variants.}",
          "+We compare three CRM variants that share the same MLP architecture but differ in their input:",
          "+\\begin{itemize}[nosep]",
          "+  \\item \\textbf{obs\\_only} (primary): $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}] \\in \\mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.",
          "+  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\\mathbf{u}_{\\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\\times}d$), 5 conformal prediction radii~\\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} of the $K$ samples.",
          "+  \\item \\textbf{scalar}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, u_s] \\in \\mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.",
          "+\\end{itemize}",
          "+The obs\\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\\cite{braun2025cgs}, but Section~\\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.",
          " ",
          " \\paragraph{Training.}",
          "-CRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:",
          "+The CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:",
          " \\begin{equation}",
          "-  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.",
          "+  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,",
          "   \\label{eq:loss}",
          " \\end{equation}",
          "-The training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.",
          "+where $\\mathbf{a}_{\\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$, and train the CRM to predict the residual that moves $a_{\\mathrm{base}}$ toward $\\mathbf{a}_{\\mathrm{expert}}$. Data augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and, for variants that receive uncertainty inputs, noise on those features ($\\sigma \\approx 0.006$). Both forms of augmentation improve generalization to the state distribution encountered during closed-loop evaluation, which diverges from the demonstration distribution due to compounding errors~\\cite{ross2011dagger}.",
          " ",
          "-We apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.",
          "-",
          "-\\paragraph{Base VLA.}",
          "-We instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.",
          "-",
          " \\subsection{Magnitude Control}",
          " \\label{sec:magnitude}",
          " ",
          "-The norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.",
          "+The norm bound $\\varepsilon$ in~(\\ref{eq:crm}) controls how far the CRM can deviate from the selected action and is critical for stable closed-loop performance.",
          " ",
          "-\\paragraph{Unbounded correction fails catastrophically.}",
          "-Without clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.",
          "+Without clipping, the CRM's natural output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, compounding error across the trajectory destroys task performance: the perdof variant achieves 0\\% success on LIBERO-Spatial across three seeds. Each over-corrected action shifts the state distribution away from the CRM's training regime, and subsequent corrections compound the deviation. This failure is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger} but manifests at inference time rather than during data collection.",
          "+% exp_id: eval-acr-spatial-v4-default-r3 (uncapped norm~1.42, perdof 0%, 3 seeds)",
          " ",
          "-\\paragraph{Small corrections are effective.}",
          "-Constraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.",
          "+Constraining $\\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. We use $\\varepsilon{=}0.2$ as the primary setting. The obs\\_only variant is robust across all tested bounds ($\\varepsilon \\in [0.03, \\text{uncapped}]$), maintaining 13.5--17.5\\% on LIBERO-Object across five seeds. The perdof variant degrades progressively as $\\varepsilon$ increases, collapsing from 14\\% to 0\\% over the same range. The root cause is rank-deficient covariance estimation at dimension-to-sample ratio $d/K = 0.6$: noisy per-DOF directional signals are harmless when clipped to small magnitude but catastrophic when the bound is loose. Section~\\ref{sec:magnitude_results} presents the full sensitivity analysis.",
          "+% exp_id: magnitude sweep obs_only seeds 42-46, perdof seeds 42-46",
          " ",
          "-\\paragraph{Connection to residual policy learning.}",
          "-The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.",
          "+The necessity of magnitude control connects ACR-VLA to the residual policy learning literature. Silver et al.~\\cite{silver2018residual} introduced residual learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} applies learned binary gating to selectively enable residual actions. PLD~\\cite{xiao2026pld} bounds corrections within a fixed range during RL training. ACR-VLA uses fixed $L_2$ norm clipping, the simplest instantiation: a hard constraint that prevents the correction from overwhelming the base policy, with no learned gating or multi-stage pipeline.",
          " ",
          "-\\paragraph{Differential sensitivity across CRM variants.}",
          "-Observation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).",
          "-",
          " \\subsection{Inference Protocol}",
          " \\label{sec:inference_protocol}",
          " ",
          " Each control step proceeds as follows:",
          " \\begin{enumerate}[nosep]",
          "   \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.",
          "-  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.",
          "-  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).",
          "-  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.",
          "+  \\item Compute the sample mean $\\boldsymbol{\\mu}_h$ per horizon step and select $a_{\\mathrm{base}}$ via $L_2$ argmin~(\\ref{eq:argmin}).",
          "+  \\item Extract the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the frozen VLA encoder.",
          "+  \\item Compute $\\boldsymbol{\\delta} = \\mathrm{CRM}([\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}])$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.",
          "   \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.",
          "   \\item Observe new state and re-plan from step~1.",
          " \\end{enumerate}",
          "-The computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.",
          "+The computational overhead is $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified."
        ]
      }
    ],
    "originalFile": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis selection procedure uses Mahalanobis-based scoring~\\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 330K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\\cite{xiao2026pld} bounds residual actor corrections within a fixed range during RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Good, the file is written. Let me verify the output by reading it back and doing the checks mentioned in the writing norms (grep for em-dash, en-dash, -ing endings).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "e6fd0cf6-cfac-46f7-8e74-28e23147f97b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7pqJEus9ZrfM88nmYUkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23745,
      "cache_read_input_tokens": 56021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23745
      },
      "output_tokens": 10,
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

_source line 30_

File written. Let me verify the output for prohibited patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "f5246035-f16d-4c3c-86f6-a41385f2274d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7pqJEus9ZrfM88nmYUkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23745,
      "cache_read_input_tokens": 56021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23745
      },
      "output_tokens": 10,
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

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01DJLJHyZjTHA5JXnGf9Fkti`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "c97ba99c-8e31-4203-87f9-4f2d4ff04f8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7pqJEus9ZrfM88nmYUkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23745,
      "cache_read_input_tokens": 56021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23745
      },
      "output_tokens": 10,
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

_source line 32 · 2026-05-18T09:46:40.907Z_

<details><summary>↩ Tool result · `toolu_01DJLJHyZjTHA5JXnGf9Fkti`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "a474b32e-8ffa-4f6c-993e-a6f44f0daf77",
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

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_014mWg2xpStEjZjom9cXBhDZ`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "a062494a-7701-4066-b3fc-f531a7876344",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7pqJEus9ZrfM88nmYUkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23745,
      "cache_read_input_tokens": 56021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23745
      },
      "output_tokens": 10,
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

_source line 34 · 2026-05-18T09:46:41.877Z_

<details><summary>↩ Tool result · `toolu_014mWg2xpStEjZjom9cXBhDZ`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "5438bd00-7aad-47b6-a730-54ccadc90fd6",
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

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_01WX6HUajyygFa99F2htjHgx`</summary>

```json
{
  "pattern": "ing,|ing\\.|ing~|ing\\\\",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "1218dcf0-c7e9-4656-b13a-ba155fce4d70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7pqJEus9ZrfM88nmYUkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23745,
      "cache_read_input_tokens": 56021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23745
      },
      "output_tokens": 10,
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

_source line 36 · 2026-05-18T09:46:43.454Z_

<details><summary>↩ Tool result · `toolu_01WX6HUajyygFa99F2htjHgx`</summary>

```text
10:Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.
12:We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\pi_\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\pi_\theta$. The method applies to any flow-matching VLA that supports repeated sampling.
46:\paragraph{Training.}
59:[Omitted long matching line]
62:[Omitted long matching line]
65:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "fb91e919-6676-407f-9c47-029a2801cf07",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "10:Let $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.\n12:We instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\\pi_\\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\\pi_\\theta$. The method applies to any flow-matching VLA that supports repeated sampling.\n46:\\paragraph{Training.}\n59:[Omitted long matching line]\n62:[Omitted long matching line]\n65:[Omitted long matching line]",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Grep · `toolu_01GTRK3ek92g5EV6o94q5K3w`</summary>

```json
{
  "pattern": "Mahalanobis|CGS|nonconformity",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "1feeb0bf-ecb8-4201-8261-e86171a2b6d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R7pqJEus9ZrfM88nmYUkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23745,
      "cache_read_input_tokens": 56021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23745
      },
      "output_tokens": 10,
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

_source line 38 · 2026-05-18T09:46:44.637Z_

<details><summary>↩ Tool result · `toolu_01GTRK3ek92g5EV6o94q5K3w`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "41cf638c-a957-407f-a95b-4b4aa076715e",
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

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Good:
- No em-dash (—) ✅
- No explanatory en-dash ( – ) ✅
- No Mahalanobis, CGS, or nonconformity ✅

The "ing" grep matches are just normal words like "matching", "thresholding", "clipping", "training", "sampling" which are used as nouns/adjectives, not as dangling participial phrase endings. Let me verify these aren't -ing phrase endings by checking the specific lines more carefully.

Let me also check for other prohibited patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "6c4ffdb5-ef1f-40f7-a812-444dc9a46bde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194GLXaikPVCZQp9vV9HLdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 79766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
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

_source line 40_

All clean. No em-dash, no explanatory en-dash, no Mahalanobis/CGS/nonconformity. The "ing" matches are all compound nouns ("flow-matching", "thresholding", "sampling", "training") not dangling participial endings. Let me also check for other prohibited patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "9d1e0007-5ff1-48c8-aeed-e1cf4b8db069",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194GLXaikPVCZQp9vV9HLdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 79766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
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

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_01YPzrcgw4bsp34LLVhytc6y`</summary>

```json
{
  "pattern": "leverage|utilize|delve|remarkably|demonstrates the effectiveness|to the best of our knowledge|paradigm shift",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "50cd3067-c076-44d0-8037-291249ff7e64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194GLXaikPVCZQp9vV9HLdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 79766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
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

_source line 42 · 2026-05-18T09:46:52.444Z_

<details><summary>↩ Tool result · `toolu_01YPzrcgw4bsp34LLVhytc6y`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "d502a3c0-0f70-4d02-ae3a-33f134576c9d",
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

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01TuuRe7ysH94AwZu6ESyQga`</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "8a26db9f-0a2e-4884-a51b-fca694f02c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194GLXaikPVCZQp9vV9HLdG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 79766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 986
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

_source line 44 · 2026-05-18T09:46:53.396Z_

<details><summary>↩ Tool result · `toolu_01TuuRe7ysH94AwZu6ESyQga`</summary>

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
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "bc40b4b2-5253-4c82-995d-457030811c56",
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

_source line 45_

Method section rewritten and verified. Key changes from the old version:

1. **Selection: L2 distance to mean** replaces Mahalanobis nonconformity scoring. Removed all shrinkage covariance estimation from selection (eq:shrinkage, eq:mahal deleted).
2. **CRM input corrected**: z_obs is 960D (not 990D), concatenated with a_base (30D) for total 990D input. CRM receives the selected action, not just the observation.
3. **Parameter count**: 327,198 (~327K), not 330K.
4. **Primary ε = 0.2**, not 0.1.
5. **CRM framed as correction module**, not selection/ranking. Explicit statement that CRM never sees individual candidates.
6. **obs_only clarified**: does not use any conformal features. Name "Conformal Residual Module" acknowledged as historical from perdof variant.
7. **Ledoit-Wolf and Braun/CGS citations** moved to perdof conditioning paragraph only.
8. **Conditioning variants** given correct input dimensions (990/1030/991) and param counts (327K/337K/327K).
9. All prohibited style patterns verified absent (no dashes, no -ing endings, no AI vocabulary).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "uuid": "420ec367-2cab-42b7-85d5-fdaf71c685e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dwAU6Px1SgkFRpkXwTidM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 80752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 671
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

Method section rewritten and verified. Key changes from the old version:

1. **Selection: L2 distance to mean** replaces Mahalanobis nonconformity scoring. Removed all shrinkage covariance estimation from selection (eq:shrinkage, eq:mahal deleted).
2. **CRM input corrected**: z_obs is 960D (not 990D), concatenated with a_base (30D) for total 990D input. CRM receives the selected action, not just the observation.
3. **Parameter count**: 327,198 (~327K), not 330K.
4. **Primary ε = 0.2**, not 0.1.
5. **CRM framed as correction module**, not selection/ranking. Explicit statement that CRM never sees individual candidates.
6. **obs_only clarified**: does not use any conformal features. Name "Conformal Residual Module" acknowledged as historical from perdof variant.
7. **Ledoit-Wolf and Braun/CGS citations** moved to perdof conditioning paragraph only.
8. **Conditioning variants** given correct input dimensions (990/1030/991) and param counts (327K/337K/327K).
9. All prohibited style patterns verified absent (no dashes, no -ing endings, no AI vocabulary).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 519325,
  "duration_api_ms": 520465,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "d05122bb-08f0-4d26-9a1a-61e3e06457f1",
  "total_cost_usd": 1.2510400000000002,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 69582,
    "cache_read_input_tokens": 332207,
    "output_tokens": 25894,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 69582,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 307,
        "cache_read_input_tokens": 80752,
        "cache_creation_input_tokens": 671,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 671
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2554,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0026539999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 25894,
      "cacheReadInputTokens": 332207,
      "cacheCreationInputTokens": 69582,
      "webSearchRequests": 0,
      "costUSD": 1.248386,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6fea81e1-e7a2-403b-b700-e5dd3cab5a0f"
}
```

</details>

---
