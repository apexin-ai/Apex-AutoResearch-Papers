# paper writing experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260517T131612.log`
- **Structured JSON:** [`6548ea6ad6b1b9152a3a.json`](../../sessions/65/6548ea6ad6b1b9152a3a.json)

## Before a recorded user message

42 recorded events

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
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
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
  "uuid": "f85f0899-a0de-4c30-83c7-8673536dfe23",
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
    "resetsAt": 1779030600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f360a1d1-d104-4a93-b579-e670f4fcd3ce",
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and checking the current state of the output directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "8305dfc2-b771-41e5-8d78-b4a10aed8a48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CH4cBEc8ED66iw8X9tC4SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14025,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14025
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

<details open><summary>🔧 Tool call — Read · `toolu_014dMr992bV1aKajkP2gtVLM`</summary>

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
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "8105b4d8-433d-4530-b3b5-25c9be365fca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CH4cBEc8ED66iw8X9tC4SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14025,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14025
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

_source line 6 · 2026-05-17T13:16:26.797Z_

<details><summary>↩ Tool result · `toolu_014dMr992bV1aKajkP2gtVLM`</summary>

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
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "1223ed12-9c5f-4820-b5eb-7dac01d6a78c",
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

<details open><summary>🔧 Tool call — Read · `toolu_013YLsgFR1mPFzxXRdhfiC9r`</summary>

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
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "aeeba945-24fd-4e66-9032-ca43cb6bfe5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CH4cBEc8ED66iw8X9tC4SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14025,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14025
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

_source line 8 · 2026-05-17T13:16:27.369Z_

<details><summary>↩ Tool result · `toolu_013YLsgFR1mPFzxXRdhfiC9r`</summary>

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
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "36ab7178-b40d-40d1-b49f-81adfad52552",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01MGiibs9TTYxRmcdW2Bb6Rw`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/ 2>/dev/null || echo \"Directory does not exist\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "bcb7d809-53df-43bf-9890-72084d8290f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CH4cBEc8ED66iw8X9tC4SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14025,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14025
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

_source line 10 · 2026-05-17T13:16:28.580Z_

<details><summary>↩ Tool result · `toolu_01MGiibs9TTYxRmcdW2Bb6Rw`</summary>

```text
Directory does not exist
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "766cd60a-810a-4701-9bc3-eab745019491",
  "tool_use_result": {
    "stdout": "Directory does not exist",
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
The output directory doesn't exist yet. Let me check what exists in the docs/paper directory structure and also look at any existing paper content for context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "b07da131-baf9-4f41-9900-214b17b59d00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgLLqfcnEoQbEYnaNWPmHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10652,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10652
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

Let me check the existing paper structure and any related files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "37f28c66-bacc-4fea-bc52-c0ffcb7f5b4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgLLqfcnEoQbEYnaNWPmHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10652,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10652
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

<details open><summary>🔧 Tool call — Bash · `toolu_01GLPHjF9zo4x99VdDprk6YT`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/",
  "description": "Create output directory for paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "2179855d-d5fc-4ba0-9424-6676da8f6055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgLLqfcnEoQbEYnaNWPmHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10652,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10652
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

_source line 14 · 2026-05-17T13:16:34.937Z_

<details><summary>↩ Tool result · `toolu_01GLPHjF9zo4x99VdDprk6YT`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "ca6984d3-0e17-45c6-b8a5-293f20efb48f",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_0151UiENui4ZXwwbnEHFwBAp`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "9c943239-e827-4a48-b4a6-becd3df640e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgLLqfcnEoQbEYnaNWPmHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10652,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10652
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

_source line 16 · 2026-05-17T13:16:35.860Z_

<details><summary>↩ Tool result · `toolu_0151UiENui4ZXwwbnEHFwBAp`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "f9b8e355-3e17-4532-9c2f-af207e65e266",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 12,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01H2h7SimwKqDBcFvs8178H4`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "7f3b6456-f0cd-4532-944c-17509f125065",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TgLLqfcnEoQbEYnaNWPmHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10652,
      "cache_read_input_tokens": 25866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10652
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

_source line 18 · 2026-05-17T13:16:36.343Z_

<details><summary>↩ Tool result · `toolu_01H2h7SimwKqDBcFvs8178H4`</summary>

```text
docs/paper/corl_2026.cls
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "6a433b98-855b-48f8-afb4-e4ba4e5342ed",
  "tool_use_result": {
    "filenames": [
      "docs/paper/corl_2026.cls",
      "docs/paper/references.bib"
    ],
    "durationMs": 11,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01E6xwSa6kXXYVV14yMuXFuR`</summary>

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
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "fde474d2-651a-4cbb-ac9f-13496111b81f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FDMgL8xeudNVGwwj3kgqp4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 36518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 465
      },
      "output_tokens": 45,
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

_source line 20 · 2026-05-17T13:16:38.429Z_

<details><summary>↩ Tool result · `toolu_01E6xwSa6kXXYVV14yMuXFuR`</summary>

```text
1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Models
8	% ============================================================
9	
10	@article{shukor2025smolvla,
11	  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
12	  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},
13	  journal={arXiv preprint arXiv:2506.01844},
14	  year={2025}
15	}
16	
17	@inproceedings{kim2024openvla,
18	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
19	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},
20	  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},
21	  year={2024}
22	}
23	
24	@inproceedings{zitkovich2023rt2,
25	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
26	  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},
27	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
28	  year={2023}
29	}
30	
31	@article{ghosh2024octo,
32	  title={Octo: An Open-Source Generalist Robot Policy},
33	  author={Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others},
34	  journal={arXiv preprint arXiv:2405.12213},
35	  year={2024}
36	}
37	
38	@article{black2024pi0,
39	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
40	  author={Black, Kevin and Brown, Noah and Driess, Danny and others},
41	  journal={arXiv preprint arXiv:2410.24164},
42	  year={2024}
43	}
44	
45	@inproceedings{openxembodiment2024,
46	  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},
47	  author={{Open X-Embodiment Collaboration}},
48	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
49	  year={2024}
50	}
51	
52	% ============================================================
53	% VLM/LLM Token Efficiency
54	% ============================================================
55	
56	@inproceedings{chen2024fastv,
57	  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},
58	  author={Chen, Liang and others},
59	  booktitle={European Conference on Computer Vision (ECCV)},
60	  year={2024},
61	  note={Oral presentation}
62	}
63	
64	@inproceedings{zhang2023h2o,
65	  title={{H$_2$O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
66	  author={Zhang, Zhenyu and others},
67	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
68	  year={2023}
69	}
70	
71	@inproceedings{xiao2024streamingllm,
72	  title={Efficient Streaming Language Models with Attention Sinks},
73	  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},
74	  booktitle={International Conference on Learning Representations (ICLR)},
75	  year={2024}
76	}
77	
78	@inproceedings{hsu2025vlacache,
79	  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},
80	  author={Hsu, Siyu and others},
81	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
82	  year={2025}
83	}
84	
85	@article{wang2026vlaiap,
86	  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},
87	  author={Wang, others},
88	  journal={arXiv preprint arXiv:2603.22991},
89	  year={2026}
90	}
91	
92	% ============================================================
93	% ViT Token Pruning/Merging
94	% ============================================================
95	
96	@inproceedings{rao2021dynamicvit,
97	  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},
98	  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},
99	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
100	  year={2021}
101	}
102	
103	@inproceedings{bolya2023tome,
104	  title={Token Merging: Your {ViT} But Faster},
105	  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},
106	  booktitle={International Conference on Learning Representations (ICLR)},
107	  year={2023}
108	}
109	
110	@inproceedings{liang2022evit,
111	  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},
112	  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},
113	  booktitle={International Conference on Learning Representations (ICLR)},
114	  year={2022}
115	}
116	
117	% ============================================================
118	% Closed-Loop Evaluation
119	% ============================================================
120	
121	@inproceedings{liu2023libero,
122	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
123	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
124	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
125	  year={2023}
126	}
127	
128	@article{mees2022calvin,
129	  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},
130	  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},
131	  journal={IEEE Robotics and Automation Letters},
132	  year={2022}
133	}
134	
135	@inproceedings{chi2023diffusionpolicy,
136	  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
137	  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
138	  booktitle={Robotics: Science and Systems (RSS)},
139	  year={2023}
140	}
141	
142	% ============================================================
143	% Negative Results & Evaluation Pitfalls
144	% ============================================================
145	
146	@inproceedings{zeng2023transformers_tsf,
147	  title={Are Transformers Effective for Time Series Forecasting?},
148	  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},
149	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
150	  volume={37},
151	  number={9},
152	  pages={11121--11128},
153	  year={2023}
154	}
155	
156	@inproceedings{bouthillier2024negative,
157	  title={Position: Embracing Negative Results in Machine Learning},
158	  author={Bouthillier, Xavier and others},
159	  booktitle={International Conference on Machine Learning (ICML)},
160	  year={2024}
161	}
162	
163	% ============================================================
164	% Background / Architecture
165	% ============================================================
166	
167	@inproceedings{zhai2023siglip,
168	  title={Sigmoid Loss for Language Image Pre-Training},
169	  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
170	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
171	  year={2023}
172	}
173	
174	@article{yang2024qwen2,
175	  title={Qwen2 Technical Report},
176	  author={Yang, An and others},
177	  journal={arXiv preprint arXiv:2407.10671},
178	  year={2024}
179	}
180	
181	@inproceedings{lipman2023flow,
182	  title={Flow Matching for Generative Modeling},
183	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
184	  booktitle={International Conference on Learning Representations (ICLR)},
185	  year={2023}
186	}
187	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "1598aa22-363e-4d8f-ba5f-a3f565ee9a94",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n@article{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others},\n  journal={arXiv preprint arXiv:2405.12213},\n  year={2024}\n}\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024}\n}\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}\n\n@inproceedings{zhang2023h2o,\n  title={{H$_2$O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@inproceedings{hsu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Hsu, Siyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{wang2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Wang, others},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},\n  volume={37},\n  number={9},\n  pages={11121--11128},\n  year={2023}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n",
      "numLines": 187,
      "startLine": 1,
      "totalLines": 187
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me also check if there are any other relevant files like the literature_map.yaml or any existing sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "48c72b3a-216c-4d24-82cf-9ebb11c312ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ejyjihmNnk2suFjmAMQGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 36983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2782
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

_source line 22_

Now let me check for any existing paper sections or figures to understand the broader paper context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "7a85aa87-c431-4ffb-a2cb-22ed900faf65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ejyjihmNnk2suFjmAMQGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 36983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2782
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

_source line 23_

<details open><summary>🔧 Tool call — Glob · `toolu_01BuQsQP3a3jxpz5o78ki5mz`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "7ba6c0be-9d74-4959-9e7b-d62cc4548327",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ejyjihmNnk2suFjmAMQGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 36983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2782
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

_source line 24 · 2026-05-17T13:16:44.134Z_

<details><summary>↩ Tool result · `toolu_01BuQsQP3a3jxpz5o78ki5mz`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "114f0738-cacf-4642-8044-e3f7d1f57199",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 5,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Glob · `toolu_01Jip1xbUtyXGZeqPqvguAdj`</summary>

```json
{
  "pattern": "**/figures/**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "a0870703-6f5d-47d7-aa02-d6faf305e0ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ejyjihmNnk2suFjmAMQGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 36983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2782
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

_source line 26 · 2026-05-17T13:16:44.645Z_

<details><summary>↩ Tool result · `toolu_01Jip1xbUtyXGZeqPqvguAdj`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "dd22cfd4-bd00-40f3-9eb6-8b77a584c0a8",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 13,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 27_

Now I have all the context. Writing the experiments section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "e23f11d7-c35f-44ae-892f-fac54f84f420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgJpBT98wec5bEs7pb9oUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 39765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 433
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

_source line 28_

<details open><summary>🔧 Tool call — Write · `toolu_01MkFJXS3SfR2FjiZr9HA7xn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
  "content": "% experiments.tex — Section 4: Main Results\n% Experiment IDs (provenance):\n%   Baseline 44.8%:              eval_stage1_only\n%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed\n%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask\n%   ACIS k=0.9 zero-mask:       eval_stage1only_k09\n%   Random k=0.5:               eval_random_prune_k05\n%   True removal k=0.5:         eval_true_removal_k05\n%   Merge k=0.5:                eval_merge_k05\n%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)\n%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)\n\n\\section{Main Results}\n\\label{sec:results}\n\nVision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.\nDynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\nEViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\nThese results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{hsu2025vlacache,wang2026vlaiap}.\nOur experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\nThe result is unambiguous.\nEvery configuration produces 0\\% SR, a complete collapse we term the \\emph{cliff edge}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility.}\n\\label{tab:ablation_matrix}\n\\small\n\\begin{tabular}{@{}llccrrc@{}}\n\\toprule\nMethod & Scoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\textbf{Baseline} & \\textbf{--} & \\textbf{1.0} & \\textbf{--} & \\textbf{44.8} & \\textbf{500} & \\textbf{[40.5, 49.2]} \\\\\n\\midrule\nACIS & Learned & 0.5 & Zero-mask & 0.0 & 300+ & [0.0, 1.26] \\\\\nACIS & Learned & 0.7 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.9 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nRandom & Random & 0.5 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.5 & True removal & 0.0 & 500 & [0.0, 0.80] \\\\\nACIS & Learned & 0.5 & Merge & 0.0 & 500 & [0.0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation_matrix} presents the full ablation matrix.\nWe systematically vary three axes: (1)~the scoring function that selects which tokens to prune, (2)~the retention ratio $k$ that controls how many tokens survive, and (3)~the mechanism by which pruned tokens are handled.\nThe baseline achieves 44.8\\% SR across 500 episodes using the identical model checkpoint with pruning disabled.\nAll six pruning conditions collapse to 0\\% SR.\n\n\\paragraph{Scoring axis.}\nIf the failure were caused by a poor scoring function that discards the wrong tokens, replacing the learned Attention-weighted Cumulative Importance Score (ACIS) scorer with uniform random selection should produce a different outcome.\nIt does not: random pruning at $k{=}0.5$ also yields 0\\% SR over 500 episodes (Table~\\ref{tab:ablation_matrix}, row~5).\nThe cliff edge is therefore not a scoring quality problem.\nNo matter which tokens are selected for removal, the policy collapses.\n\n\\paragraph{Ratio axis.}\nIf the failure were caused by removing too many tokens, retaining 90\\% of tokens ($k{=}0.9$, removing only 10\\%) should preserve most task-relevant information.\nYet $k{=}0.9$ also produces 0\\% SR (Table~\\ref{tab:ablation_matrix}, row~3).\nThis rules out the hypothesis that a gentler pruning ratio would recover graceful degradation.\nThe transition from functional to non-functional is binary, not gradual.\n\n\\paragraph{Mechanism axis.}\nThree distinct mechanisms for handling pruned tokens produce identical failure.\nZero-masking replaces pruned token embeddings with zeros, which could inject out-of-distribution (OOD) activation patterns.\nTrue removal eliminates the tokens entirely, changing the sequence length but avoiding OOD injection.\nToken merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\nAll three mechanisms yield 0\\% SR (Table~\\ref{tab:ablation_matrix}, rows~2, 6, 7).\nThe collapse is therefore not caused by OOD activations from a particular masking strategy; it is a property of any alteration to the vision token sequence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_cliff_edge.pdf}\n\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\n\\label{fig:cliff_edge}\n\\end{figure}\n\n\\paragraph{Cross-suite confirmation.}\nTo verify that the cliff edge is not an artifact of a single task distribution, we evaluate ACIS pruning at $k{=}0.5$ across three LIBERO suites with distinct characteristics.\nOn LIBERO-Object (object manipulation), SR drops from 44.8\\% to 0\\%.\nOn LIBERO-Spatial (spatial reasoning), SR drops from 51.8\\% to 0\\%.\nOn LIBERO-Goal (goal-conditioned tasks), SR drops from 63.0\\% to 0\\%.\nThe cliff edge is consistent across all three suites, and the absolute SR gap is largest for the suite where the baseline performs best (63 percentage points for Goal).\nFigure~\\ref{fig:cliff_edge} visualizes this collapse pattern.\nThese results establish that the cliff edge is method-agnostic: it persists regardless of which tokens are pruned, how aggressively they are pruned, and how the pruning is implemented.\nThe phenomenon is not a failure of any particular pruning algorithm but a structural property of how VLA policies consume vision tokens during closed-loop control.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "ce225db3-ffab-4106-8d1d-9097f5d4ce14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgJpBT98wec5bEs7pb9oUD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 39765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 433
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

_source line 29 · 2026-05-17T13:17:30.506Z_

<details><summary>↩ Tool result · `toolu_01MkFJXS3SfR2FjiZr9HA7xn`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "6d80161f-4475-46e3-bd80-a002b15e1a4f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
    "content": "% experiments.tex — Section 4: Main Results\n% Experiment IDs (provenance):\n%   Baseline 44.8%:              eval_stage1_only\n%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed\n%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask\n%   ACIS k=0.9 zero-mask:       eval_stage1only_k09\n%   Random k=0.5:               eval_random_prune_k05\n%   True removal k=0.5:         eval_true_removal_k05\n%   Merge k=0.5:                eval_merge_k05\n%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)\n%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)\n\n\\section{Main Results}\n\\label{sec:results}\n\nVision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.\nDynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\nEViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\nThese results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{hsu2025vlacache,wang2026vlaiap}.\nOur experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\nThe result is unambiguous.\nEvery configuration produces 0\\% SR, a complete collapse we term the \\emph{cliff edge}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility.}\n\\label{tab:ablation_matrix}\n\\small\n\\begin{tabular}{@{}llccrrc@{}}\n\\toprule\nMethod & Scoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\textbf{Baseline} & \\textbf{--} & \\textbf{1.0} & \\textbf{--} & \\textbf{44.8} & \\textbf{500} & \\textbf{[40.5, 49.2]} \\\\\n\\midrule\nACIS & Learned & 0.5 & Zero-mask & 0.0 & 300+ & [0.0, 1.26] \\\\\nACIS & Learned & 0.7 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.9 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nRandom & Random & 0.5 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.5 & True removal & 0.0 & 500 & [0.0, 0.80] \\\\\nACIS & Learned & 0.5 & Merge & 0.0 & 500 & [0.0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation_matrix} presents the full ablation matrix.\nWe systematically vary three axes: (1)~the scoring function that selects which tokens to prune, (2)~the retention ratio $k$ that controls how many tokens survive, and (3)~the mechanism by which pruned tokens are handled.\nThe baseline achieves 44.8\\% SR across 500 episodes using the identical model checkpoint with pruning disabled.\nAll six pruning conditions collapse to 0\\% SR.\n\n\\paragraph{Scoring axis.}\nIf the failure were caused by a poor scoring function that discards the wrong tokens, replacing the learned Attention-weighted Cumulative Importance Score (ACIS) scorer with uniform random selection should produce a different outcome.\nIt does not: random pruning at $k{=}0.5$ also yields 0\\% SR over 500 episodes (Table~\\ref{tab:ablation_matrix}, row~5).\nThe cliff edge is therefore not a scoring quality problem.\nNo matter which tokens are selected for removal, the policy collapses.\n\n\\paragraph{Ratio axis.}\nIf the failure were caused by removing too many tokens, retaining 90\\% of tokens ($k{=}0.9$, removing only 10\\%) should preserve most task-relevant information.\nYet $k{=}0.9$ also produces 0\\% SR (Table~\\ref{tab:ablation_matrix}, row~3).\nThis rules out the hypothesis that a gentler pruning ratio would recover graceful degradation.\nThe transition from functional to non-functional is binary, not gradual.\n\n\\paragraph{Mechanism axis.}\nThree distinct mechanisms for handling pruned tokens produce identical failure.\nZero-masking replaces pruned token embeddings with zeros, which could inject out-of-distribution (OOD) activation patterns.\nTrue removal eliminates the tokens entirely, changing the sequence length but avoiding OOD injection.\nToken merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\nAll three mechanisms yield 0\\% SR (Table~\\ref{tab:ablation_matrix}, rows~2, 6, 7).\nThe collapse is therefore not caused by OOD activations from a particular masking strategy; it is a property of any alteration to the vision token sequence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_cliff_edge.pdf}\n\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\n\\label{fig:cliff_edge}\n\\end{figure}\n\n\\paragraph{Cross-suite confirmation.}\nTo verify that the cliff edge is not an artifact of a single task distribution, we evaluate ACIS pruning at $k{=}0.5$ across three LIBERO suites with distinct characteristics.\nOn LIBERO-Object (object manipulation), SR drops from 44.8\\% to 0\\%.\nOn LIBERO-Spatial (spatial reasoning), SR drops from 51.8\\% to 0\\%.\nOn LIBERO-Goal (goal-conditioned tasks), SR drops from 63.0\\% to 0\\%.\nThe cliff edge is consistent across all three suites, and the absolute SR gap is largest for the suite where the baseline performs best (63 percentage points for Goal).\nFigure~\\ref{fig:cliff_edge} visualizes this collapse pattern.\nThese results establish that the cliff edge is method-agnostic: it persists regardless of which tokens are pruned, how aggressively they are pruned, and how the pruning is implemented.\nThe phenomenon is not a failure of any particular pruning algorithm but a structural property of how VLA policies consume vision tokens during closed-loop control.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 30_

Let me verify the output against the style constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "ad820e97-98f8-477c-ab5b-a905df3aa58c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzwCf14yvEF26ZqMzwiB5H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2149,
      "cache_read_input_tokens": 40198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2149
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

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_0185vHyXq9bpJmmf7cmnaY4X`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections && echo \"=== em-dash ===\" && grep -n \"—\" experiments.tex; echo \"=== explanatory en-dash ===\" && grep -n \" – \" experiments.tex; echo \"=== -ing phrase endings ===\" && grep -n \"ing\\.\" experiments.tex | grep -i \", [a-z]*ing\\.\" || true; echo \"=== -ing comma ===\" && grep -n \"ing,\" experiments.tex || true; echo \"=== Furthermore/Moreover/Additionally ===\" && grep -ni \"furthermore\\|moreover\\|additionally\" experiments.tex || echo \"none\"; echo \"=== worth noting / notably ===\" && grep -ni \"worth noting\\|notably\" experiments.tex || echo \"none\"; echo \"=== leverage/utilize/delve/facilitate ===\" && grep -ni \"leverage\\|utilize\\|delve\\|facilitate\" experiments.tex || echo \"none\"; echo \"=== word count ===\" && detex experiments.tex 2>/dev/null | wc -w || cat experiments.tex | sed 's/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/%.*//g' | wc -w",
  "description": "Check style compliance: dashes, -ing phrases, banned words, word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "4b647431-0d3c-4a71-9a53-498cd102be72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzwCf14yvEF26ZqMzwiB5H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2149,
      "cache_read_input_tokens": 40198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2149
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

_source line 32 · 2026-05-17T13:17:38.937Z_

<details><summary>↩ Tool result · `toolu_0185vHyXq9bpJmmf7cmnaY4X`</summary>

```text
=== em-dash ===
1:% experiments.tex — Section 4: Main Results
=== explanatory en-dash ===
=== -ing phrase endings ===
=== -ing comma ===
=== Furthermore/Moreover/Additionally ===
none
=== worth noting / notably ===
none
=== leverage/utilize/delve/facilitate ===
none
=== word count ===
787
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "c077f83a-e248-4d2b-b90d-45b9256be37e",
  "tool_use_result": {
    "stdout": "=== em-dash ===\n1:% experiments.tex — Section 4: Main Results\n=== explanatory en-dash ===\n=== -ing phrase endings ===\n=== -ing comma ===\n=== Furthermore/Moreover/Additionally ===\nnone\n=== worth noting / notably ===\nnone\n=== leverage/utilize/delve/facilitate ===\nnone\n=== word count ===\n787",
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

_source line 33_

The em-dash is only in the comment line (line 1), not in the actual LaTeX content. Let me fix that comment and do a final check on -ing patterns more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "02f600d6-ee34-480f-891c-7db135cda87a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaoyknmXBY5hmBRNk8KiRa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 42347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01AM3nFB2Mjkf6AMTjuKvvCe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
  "old_string": "% experiments.tex — Section 4: Main Results",
  "new_string": "% experiments.tex -- Section 4: Main Results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "6e1e9847-bb90-4408-a305-46af4fb9c555",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EaoyknmXBY5hmBRNk8KiRa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 42347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
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

_source line 35 · 2026-05-17T13:17:42.853Z_

<details><summary>↩ Tool result · `toolu_01AM3nFB2Mjkf6AMTjuKvvCe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "81d5fde8-0b4b-4bbe-a73c-bf316463a972",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
    "oldString": "% experiments.tex — Section 4: Main Results",
    "newString": "% experiments.tex -- Section 4: Main Results",
    "originalFile": "% experiments.tex — Section 4: Main Results\n% Experiment IDs (provenance):\n%   Baseline 44.8%:              eval_stage1_only\n%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed\n%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask\n%   ACIS k=0.9 zero-mask:       eval_stage1only_k09\n%   Random k=0.5:               eval_random_prune_k05\n%   True removal k=0.5:         eval_true_removal_k05\n%   Merge k=0.5:                eval_merge_k05\n%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)\n%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)\n\n\\section{Main Results}\n\\label{sec:results}\n\nVision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.\nDynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\nEViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\nThese results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{hsu2025vlacache,wang2026vlaiap}.\nOur experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\nThe result is unambiguous.\nEvery configuration produces 0\\% SR, a complete collapse we term the \\emph{cliff edge}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility.}\n\\label{tab:ablation_matrix}\n\\small\n\\begin{tabular}{@{}llccrrc@{}}\n\\toprule\nMethod & Scoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\textbf{Baseline} & \\textbf{--} & \\textbf{1.0} & \\textbf{--} & \\textbf{44.8} & \\textbf{500} & \\textbf{[40.5, 49.2]} \\\\\n\\midrule\nACIS & Learned & 0.5 & Zero-mask & 0.0 & 300+ & [0.0, 1.26] \\\\\nACIS & Learned & 0.7 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.9 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nRandom & Random & 0.5 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.5 & True removal & 0.0 & 500 & [0.0, 0.80] \\\\\nACIS & Learned & 0.5 & Merge & 0.0 & 500 & [0.0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation_matrix} presents the full ablation matrix.\nWe systematically vary three axes: (1)~the scoring function that selects which tokens to prune, (2)~the retention ratio $k$ that controls how many tokens survive, and (3)~the mechanism by which pruned tokens are handled.\nThe baseline achieves 44.8\\% SR across 500 episodes using the identical model checkpoint with pruning disabled.\nAll six pruning conditions collapse to 0\\% SR.\n\n\\paragraph{Scoring axis.}\nIf the failure were caused by a poor scoring function that discards the wrong tokens, replacing the learned Attention-weighted Cumulative Importance Score (ACIS) scorer with uniform random selection should produce a different outcome.\nIt does not: random pruning at $k{=}0.5$ also yields 0\\% SR over 500 episodes (Table~\\ref{tab:ablation_matrix}, row~5).\nThe cliff edge is therefore not a scoring quality problem.\nNo matter which tokens are selected for removal, the policy collapses.\n\n\\paragraph{Ratio axis.}\nIf the failure were caused by removing too many tokens, retaining 90\\% of tokens ($k{=}0.9$, removing only 10\\%) should preserve most task-relevant information.\nYet $k{=}0.9$ also produces 0\\% SR (Table~\\ref{tab:ablation_matrix}, row~3).\nThis rules out the hypothesis that a gentler pruning ratio would recover graceful degradation.\nThe transition from functional to non-functional is binary, not gradual.\n\n\\paragraph{Mechanism axis.}\nThree distinct mechanisms for handling pruned tokens produce identical failure.\nZero-masking replaces pruned token embeddings with zeros, which could inject out-of-distribution (OOD) activation patterns.\nTrue removal eliminates the tokens entirely, changing the sequence length but avoiding OOD injection.\nToken merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\nAll three mechanisms yield 0\\% SR (Table~\\ref{tab:ablation_matrix}, rows~2, 6, 7).\nThe collapse is therefore not caused by OOD activations from a particular masking strategy; it is a property of any alteration to the vision token sequence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_cliff_edge.pdf}\n\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\n\\label{fig:cliff_edge}\n\\end{figure}\n\n\\paragraph{Cross-suite confirmation.}\nTo verify that the cliff edge is not an artifact of a single task distribution, we evaluate ACIS pruning at $k{=}0.5$ across three LIBERO suites with distinct characteristics.\nOn LIBERO-Object (object manipulation), SR drops from 44.8\\% to 0\\%.\nOn LIBERO-Spatial (spatial reasoning), SR drops from 51.8\\% to 0\\%.\nOn LIBERO-Goal (goal-conditioned tasks), SR drops from 63.0\\% to 0\\%.\nThe cliff edge is consistent across all three suites, and the absolute SR gap is largest for the suite where the baseline performs best (63 percentage points for Goal).\nFigure~\\ref{fig:cliff_edge} visualizes this collapse pattern.\nThese results establish that the cliff edge is method-agnostic: it persists regardless of which tokens are pruned, how aggressively they are pruned, and how the pruning is implemented.\nThe phenomenon is not a failure of any particular pruning algorithm but a structural property of how VLA policies consume vision tokens during closed-loop control.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 4,
        "newStart": 1,
        "newLines": 4,
        "lines": [
          "-% experiments.tex — Section 4: Main Results",
          "+% experiments.tex -- Section 4: Main Results",
          " % Experiment IDs (provenance):",
          " %   Baseline 44.8%:              eval_stage1_only",
          " %   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed"
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_0122JC3Szj8EfadxbN9n7R6Q`</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex || echo \"No dashes found\"",
  "description": "Final dash check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "65beb84d-7c86-4d0b-8beb-dc8562b8b58c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TKZhrbhZTBDCXnqM1dSBaW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 42856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
      },
      "output_tokens": 38,
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

_source line 37 · 2026-05-17T13:17:45.611Z_

<details><summary>↩ Tool result · `toolu_0122JC3Szj8EfadxbN9n7R6Q`</summary>

```text
No dashes found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "24188433-2468-4e71-b2c4-ab804e9cf94c",
  "tool_use_result": {
    "stdout": "No dashes found",
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

_source line 38_

Clean. Let me also verify the LaTeX number-range dashes use the correct `--` syntax and that all abbreviations are defined on first use.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "1a68e924-be7d-45dc-a720-7b3903aebac5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASmQZbfmJmrBjCLFBurdku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 43128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01U1W3tpLtxN2HcqBUwvxwcf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "00088858-ae34-43e2-abe6-9b9ae3dde734",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASmQZbfmJmrBjCLFBurdku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 145,
      "cache_read_input_tokens": 43128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 145
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

_source line 40 · 2026-05-17T13:17:48.503Z_

<details><summary>↩ Tool result · `toolu_01U1W3tpLtxN2HcqBUwvxwcf`</summary>

```text
1	% experiments.tex -- Section 4: Main Results
2	% Experiment IDs (provenance):
3	%   Baseline 44.8%:              eval_stage1_only
4	%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed
5	%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask
6	%   ACIS k=0.9 zero-mask:       eval_stage1only_k09
7	%   Random k=0.5:               eval_random_prune_k05
8	%   True removal k=0.5:         eval_true_removal_k05
9	%   Merge k=0.5:                eval_merge_k05
10	%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)
11	%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)
12	
13	\section{Main Results}
14	\label{sec:results}
15	
16	Vision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.
17	DynamicViT~\cite{rao2021dynamicvit} removes 30\%--50\% of tokens with less than 0.5\% accuracy loss on ImageNet, and Token Merging (ToMe)~\cite{bolya2023tome} merges up to 40\% of tokens while retaining over 99\% of classification accuracy.
18	EViT~\cite{liang2022evit} similarly discards 50\% of inattentive tokens with negligible degradation.
19	These results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\cite{hsu2025vlacache,wang2026vlaiap}.
20	Our experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\cite{liu2023libero}.
21	The result is unambiguous.
22	Every configuration produces 0\% SR, a complete collapse we term the \emph{cliff edge}.
23	
24	\begin{table}[t]
25	\centering
26	\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility.}
27	\label{tab:ablation_matrix}
28	\small
29	\begin{tabular}{@{}llccrrc@{}}
30	\toprule
31	Method & Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
32	\midrule
33	\textbf{Baseline} & \textbf{--} & \textbf{1.0} & \textbf{--} & \textbf{44.8} & \textbf{500} & \textbf{[40.5, 49.2]} \\
34	\midrule
35	ACIS & Learned & 0.5 & Zero-mask & 0.0 & 300+ & [0.0, 1.26] \\
36	ACIS & Learned & 0.7 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
37	ACIS & Learned & 0.9 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
38	Random & Random & 0.5 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\
39	ACIS & Learned & 0.5 & True removal & 0.0 & 500 & [0.0, 0.80] \\
40	ACIS & Learned & 0.5 & Merge & 0.0 & 500 & [0.0, 0.76] \\
41	\bottomrule
42	\end{tabular}
43	\end{table}
44	
45	Table~\ref{tab:ablation_matrix} presents the full ablation matrix.
46	We systematically vary three axes: (1)~the scoring function that selects which tokens to prune, (2)~the retention ratio $k$ that controls how many tokens survive, and (3)~the mechanism by which pruned tokens are handled.
47	The baseline achieves 44.8\% SR across 500 episodes using the identical model checkpoint with pruning disabled.
48	All six pruning conditions collapse to 0\% SR.
49	
50	\paragraph{Scoring axis.}
51	If the failure were caused by a poor scoring function that discards the wrong tokens, replacing the learned Attention-weighted Cumulative Importance Score (ACIS) scorer with uniform random selection should produce a different outcome.
52	It does not: random pruning at $k{=}0.5$ also yields 0\% SR over 500 episodes (Table~\ref{tab:ablation_matrix}, row~5).
53	The cliff edge is therefore not a scoring quality problem.
54	No matter which tokens are selected for removal, the policy collapses.
55	
56	\paragraph{Ratio axis.}
57	If the failure were caused by removing too many tokens, retaining 90\% of tokens ($k{=}0.9$, removing only 10\%) should preserve most task-relevant information.
58	Yet $k{=}0.9$ also produces 0\% SR (Table~\ref{tab:ablation_matrix}, row~3).
59	This rules out the hypothesis that a gentler pruning ratio would recover graceful degradation.
60	The transition from functional to non-functional is binary, not gradual.
61	
62	\paragraph{Mechanism axis.}
63	Three distinct mechanisms for handling pruned tokens produce identical failure.
64	Zero-masking replaces pruned token embeddings with zeros, which could inject out-of-distribution (OOD) activation patterns.
65	True removal eliminates the tokens entirely, changing the sequence length but avoiding OOD injection.
66	Token merging (following ToMe~\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.
67	All three mechanisms yield 0\% SR (Table~\ref{tab:ablation_matrix}, rows~2, 6, 7).
68	The collapse is therefore not caused by OOD activations from a particular masking strategy; it is a property of any alteration to the vision token sequence.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\linewidth]{figures/paper/fig_cliff_edge.pdf}
73	\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\% accuracy on classification benchmarks even at aggressive retention ratios~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}
74	\label{fig:cliff_edge}
75	\end{figure}
76	
77	\paragraph{Cross-suite confirmation.}
78	To verify that the cliff edge is not an artifact of a single task distribution, we evaluate ACIS pruning at $k{=}0.5$ across three LIBERO suites with distinct characteristics.
79	On LIBERO-Object (object manipulation), SR drops from 44.8\% to 0\%.
80	On LIBERO-Spatial (spatial reasoning), SR drops from 51.8\% to 0\%.
81	On LIBERO-Goal (goal-conditioned tasks), SR drops from 63.0\% to 0\%.
82	The cliff edge is consistent across all three suites, and the absolute SR gap is largest for the suite where the baseline performs best (63 percentage points for Goal).
83	Figure~\ref{fig:cliff_edge} visualizes this collapse pattern.
84	These results establish that the cliff edge is method-agnostic: it persists regardless of which tokens are pruned, how aggressively they are pruned, and how the pruning is implemented.
85	The phenomenon is not a failure of any particular pruning algorithm but a structural property of how VLA policies consume vision tokens during closed-loop control.
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "a8e591f3-c260-45cd-849c-fdbd5d106f26",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex",
      "content": "% experiments.tex -- Section 4: Main Results\n% Experiment IDs (provenance):\n%   Baseline 44.8%:              eval_stage1_only\n%   ACIS k=0.5 zero-mask:       eval_stage1only_object_v2_fixed\n%   ACIS k=0.7 zero-mask:       eval_k07_zero_mask\n%   ACIS k=0.9 zero-mask:       eval_stage1only_k09\n%   Random k=0.5:               eval_random_prune_k05\n%   True removal k=0.5:         eval_true_removal_k05\n%   Merge k=0.5:                eval_merge_k05\n%   Spatial suite:              eval_spatial_prune_k05 (baseline 51.8%)\n%   Goal suite:                 eval_goal_prune_k05 (baseline 63%)\n\n\\section{Main Results}\n\\label{sec:results}\n\nVision token pruning in Vision Transformers (ViTs) is widely regarded as a reliable efficiency technique.\nDynamicViT~\\cite{rao2021dynamicvit} removes 30\\%--50\\% of tokens with less than 0.5\\% accuracy loss on ImageNet, and Token Merging (ToMe)~\\cite{bolya2023tome} merges up to 40\\% of tokens while retaining over 99\\% of classification accuracy.\nEViT~\\cite{liang2022evit} similarly discards 50\\% of inattentive tokens with negligible degradation.\nThese results have motivated recent proposals to apply similar strategies to Vision-Language-Action (VLA) models for real-time robotic control~\\cite{hsu2025vlacache,wang2026vlaiap}.\nOur experiments test whether this transfer holds: we apply six pruning configurations to a VLA policy and evaluate closed-loop Success Rate (SR) on the LIBERO benchmark~\\cite{liu2023libero}.\nThe result is unambiguous.\nEvery configuration produces 0\\% SR, a complete collapse we term the \\emph{cliff edge}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation matrix across scoring functions, retention ratios, and pruning mechanisms. All six pruning conditions produce 0\\% SR. The baseline runs the same checkpoint with pruning disabled (bypass mode). Wilson 95\\% confidence intervals (CI) are computed over independent episodes. Experiment IDs are listed for reproducibility.}\n\\label{tab:ablation_matrix}\n\\small\n\\begin{tabular}{@{}llccrrc@{}}\n\\toprule\nMethod & Scoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\textbf{Baseline} & \\textbf{--} & \\textbf{1.0} & \\textbf{--} & \\textbf{44.8} & \\textbf{500} & \\textbf{[40.5, 49.2]} \\\\\n\\midrule\nACIS & Learned & 0.5 & Zero-mask & 0.0 & 300+ & [0.0, 1.26] \\\\\nACIS & Learned & 0.7 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.9 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nRandom & Random & 0.5 & Zero-mask & 0.0 & 500 & [0.0, 0.76] \\\\\nACIS & Learned & 0.5 & True removal & 0.0 & 500 & [0.0, 0.80] \\\\\nACIS & Learned & 0.5 & Merge & 0.0 & 500 & [0.0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation_matrix} presents the full ablation matrix.\nWe systematically vary three axes: (1)~the scoring function that selects which tokens to prune, (2)~the retention ratio $k$ that controls how many tokens survive, and (3)~the mechanism by which pruned tokens are handled.\nThe baseline achieves 44.8\\% SR across 500 episodes using the identical model checkpoint with pruning disabled.\nAll six pruning conditions collapse to 0\\% SR.\n\n\\paragraph{Scoring axis.}\nIf the failure were caused by a poor scoring function that discards the wrong tokens, replacing the learned Attention-weighted Cumulative Importance Score (ACIS) scorer with uniform random selection should produce a different outcome.\nIt does not: random pruning at $k{=}0.5$ also yields 0\\% SR over 500 episodes (Table~\\ref{tab:ablation_matrix}, row~5).\nThe cliff edge is therefore not a scoring quality problem.\nNo matter which tokens are selected for removal, the policy collapses.\n\n\\paragraph{Ratio axis.}\nIf the failure were caused by removing too many tokens, retaining 90\\% of tokens ($k{=}0.9$, removing only 10\\%) should preserve most task-relevant information.\nYet $k{=}0.9$ also produces 0\\% SR (Table~\\ref{tab:ablation_matrix}, row~3).\nThis rules out the hypothesis that a gentler pruning ratio would recover graceful degradation.\nThe transition from functional to non-functional is binary, not gradual.\n\n\\paragraph{Mechanism axis.}\nThree distinct mechanisms for handling pruned tokens produce identical failure.\nZero-masking replaces pruned token embeddings with zeros, which could inject out-of-distribution (OOD) activation patterns.\nTrue removal eliminates the tokens entirely, changing the sequence length but avoiding OOD injection.\nToken merging (following ToMe~\\cite{bolya2023tome}) combines pruned tokens with their nearest neighbors, preserving sequence length and total information.\nAll three mechanisms yield 0\\% SR (Table~\\ref{tab:ablation_matrix}, rows~2, 6, 7).\nThe collapse is therefore not caused by OOD activations from a particular masking strategy; it is a property of any alteration to the vision token sequence.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_cliff_edge.pdf}\n\\caption{The cliff edge in VLA token pruning. While ViT pruning methods retain $>$99\\% accuracy on classification benchmarks even at aggressive retention ratios~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit}, applying any form of token reduction to a VLA policy causes immediate collapse to 0\\% SR across all LIBERO suites. The transition from functional to non-functional is binary, with no intermediate degradation regime.}\n\\label{fig:cliff_edge}\n\\end{figure}\n\n\\paragraph{Cross-suite confirmation.}\nTo verify that the cliff edge is not an artifact of a single task distribution, we evaluate ACIS pruning at $k{=}0.5$ across three LIBERO suites with distinct characteristics.\nOn LIBERO-Object (object manipulation), SR drops from 44.8\\% to 0\\%.\nOn LIBERO-Spatial (spatial reasoning), SR drops from 51.8\\% to 0\\%.\nOn LIBERO-Goal (goal-conditioned tasks), SR drops from 63.0\\% to 0\\%.\nThe cliff edge is consistent across all three suites, and the absolute SR gap is largest for the suite where the baseline performs best (63 percentage points for Goal).\nFigure~\\ref{fig:cliff_edge} visualizes this collapse pattern.\nThese results establish that the cliff edge is method-agnostic: it persists regardless of which tokens are pruned, how aggressively they are pruned, and how the pruning is implemented.\nThe phenomenon is not a failure of any particular pruning algorithm but a structural property of how VLA policies consume vision tokens during closed-loop control.\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

All checks pass:
- No em-dashes or explanatory en-dashes (only LaTeX `--` for number ranges and table placeholders)
- No `-ing` phrase endings
- No `Furthermore`/`Moreover`/`Additionally`
- No `It is worth noting`/`Notably`
- No banned words (`leverage`/`utilize`/`delve`/`facilitate`)
- All abbreviations defined on first use: ViTs, ToMe, VLA, SR, ACIS, OOD, CI
- ~787 words (within ~1000 target)
- Provenance experiment IDs recorded in header comments
- Table 1 includes all 7 rows with Wilson CIs
- Three-axis analysis (scoring, ratio, mechanism) each in one paragraph
- Cross-suite confirmation paragraph with all three LIBERO suites
- Figure reference to `fig_cliff_edge.pdf`
- ViT pruning citations include specific ratios and accuracy retention numbers
- Narrative opens with classification-world expectations, then reveals the VLA cliff-edge contrast

Section written to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "uuid": "544ec7df-9223-4cf2-b508-c324bc594f1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvcX9qs3e72Ja39CR196m2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2287,
      "cache_read_input_tokens": 43273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2287
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

_source line 42_

All checks pass:
- No em-dashes or explanatory en-dashes (only LaTeX `--` for number ranges and table placeholders)
- No `-ing` phrase endings
- No `Furthermore`/`Moreover`/`Additionally`
- No `It is worth noting`/`Notably`
- No banned words (`leverage`/`utilize`/`delve`/`facilitate`)
- All abbreviations defined on first use: ViTs, ToMe, VLA, SR, ACIS, OOD, CI
- ~787 words (within ~1000 target)
- Provenance experiment IDs recorded in header comments
- Table 1 includes all 7 rows with Wilson CIs
- Three-axis analysis (scoring, ratio, mechanism) each in one paragraph
- Cross-suite confirmation paragraph with all three LIBERO suites
- Figure reference to `fig_cliff_edge.pdf`
- ViT pruning citations include specific ratios and accuracy retention numbers
- Narrative opens with classification-world expectations, then reveals the VLA cliff-edge contrast

Section written to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experiments.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 98842,
  "duration_api_ms": 100133,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "81664f6c-f54a-4d98-a02d-909e9b955fde",
  "total_cost_usd": 0.49966324999999995,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 33719,
    "cache_read_input_tokens": 362775,
    "output_tokens": 4208,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33719,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 295,
        "cache_read_input_tokens": 43273,
        "cache_creation_input_tokens": 2287,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2287
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2187,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002277,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 4208,
      "cacheReadInputTokens": 362775,
      "cacheCreationInputTokens": 33719,
      "webSearchRequests": 0,
      "costUSD": 0.4973862499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f1381096-c6a4-408e-a6c0-379350efb441"
}
```

</details>

---
