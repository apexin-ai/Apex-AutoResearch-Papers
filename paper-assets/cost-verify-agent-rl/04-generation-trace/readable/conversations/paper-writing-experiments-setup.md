# paper writing experiments setup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_writing_experiments_setup_20260518T201250.jsonl`
- **Structured JSON:** [`b2c910357af5b96781cb.json`](../../sessions/b2/b2c910357af5b96781cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-18T20:19:21.334218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T20:19:21.334855+00:00_

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
74	- **
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T20:19:21.335056+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T20:19:21.335410+00:00_

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
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T20:19:21.335596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T20:19:21.335823+00:00_

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
15	ALFWorld is well-suited for studying the step-independent failure because its tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place the object (step 11). With step-independent windowing at $h = 2$, the window containing the placement acti
…[truncated 15889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T20:19:21.336054+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

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
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "tool_args": {
    "pattern": "@\\w+\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/references.bib",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T20:19:21.336210+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T20:19:21.336373+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T20:19:21.336497+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T20:19:21.336652+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'experiment_id': 'exp029'}",
  "project": "cost-verify-agent-rl",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'experiment_id': 'exp029'}",
    "project": "cost-verify-agent-rl",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T20:19:21.336793+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2319}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T20:19:21.336914+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'experiment_id': 'exp028_prereq_zeroshot'}",
  "project": "cost-verify-agent-rl",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'experiment_id': 'exp028_prereq_zeroshot'}",
    "project": "cost-verify-agent-rl",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T20:19:21.337036+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2029}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T20:19:21.337173+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T20:19:21.337854+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"hsweep_h20_seed1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-18T18:04:42.684Z\", \"updated_at\": \"2026-05-18T19:14:40.086Z\", \"hypothesis\": \"h=20 with step_independent generation provides 20-step observation windows. Key data point for fig5 cliff figure: with h=10 and h=5 both collapsing, h=20 tests whether 20 steps of context is sufficient for recovery. If h=20 recovers (val > 0% at step 5+), the cliff is between h=10 and h=20. If still collapsed, the minimum viable context window is larger than 20 steps.\", \"parent\": \"hsweep_h10_seed1\", \"notes\": \"诊断中: worker_diagnose_hsweep_h20_seed1_20260518T184044 正在 SSH 深查失败原因。日志尾部无 Traceback，疑似系统级 kill (OOM/磁盘)。\"}, \"hsweep_h10_seed1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T17:30:46.964Z\", \"updated_at\": \"2026-05-18T19:09:46.781Z\", \"hypothesis\": \"h=10 with step_independent generation provides 10-step observation windows. Key data point for fig5 cliff figure: if h=10 shows recovery (val > 0%), the cliff is between h=5 and h=10. If still collapsed, cliff is between h=10 and full context (h=28).\", \"parent\": \"hsweep_h2_seed1\", \"notes\": \"Director 批准临时 kill（刚启动几分钟，无进度损失）以释放 bjb1 cuda:0,1 跑 exp029 + hsweep_h2_seed2 双 reeval。Reeval 完成后重启。原由 auto_next_hsweep.sh 自动启动，未经正式审批。\"}, \"factorial_h2_episodeadv_seed2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-18T04:48:02.228Z\", \"updated_at\": \"2026-05-18T18:25:27.297Z\", \"hypothesis\": \"Replicate factorial experiment (step-independent + episode-level advantage) with different seed to confirm that sign misattribution elimination is robust, not single-seed artifact. Same config, different seed, 15 steps.\", \"parent\": \"factorial_h2_episodeadv_seed1\"}, \"exp029_episode_level_seed2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T04:48:01.826Z\", \"updated_at\": \"2026-05-18T18:25:16.249Z\", \"hypothesis\": \"Replicate exp029 episode-level result (23.88% OO
…[truncated 44694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T20:19:21.338315+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "content": "\\newcommand{\\placeholder}[1]{\\textcolor{red}{[#1]}}\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe design experiments to test three predictions of the dual-mechanism analysis. First, does step-independent training collapse while episode-level training avoids collapse? Second, can we separate the individual contributions of information loss (M1) and sign misattribution (M2) through factorial manipulation? Third, how does window size $h$ modulate the severity of both mechanisms?\n\n\\subsection{Environment}\n\\label{sec:environment}\n\nWe evaluate on ALFWorld~\\cite{shridhar2021alfworld}, a text-based household environment in which an agent interacts with simulated rooms through natural language commands. ALFWorld defines six task types (pick, clean, heat, cool, examine, pick two) that require sequential reasoning over multiple interaction steps. The agent issues text commands (e.g., \\texttt{go to countertop 1}, \\texttt{take knife 2 from drawer 3}) and receives textual observations of the environment state. Episodes terminate after task completion or a maximum of 50 steps. The reward is binary: $R \\in \\{0, r_+\\}$, with $r_+$ awarded only upon successful task completion.\n\nALFWorld tasks exhibit strong sequential dependencies. A typical task requires the agent to locate an object (steps 1--5), pick it up (step 6), navigate to a target receptacle (steps 7--10), and place it (step 11). Under step-independent windowing with $h = 2$, the window containing the placement action has no access to the exploration steps that determined the target object. Context truncation therefore directly impairs the policy's ability to condition late actions on early observations.\n\n\\subsection{Base Model and Supervised Fine-Tuning}\n\\label{sec:base_model}\n\nWe use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \\times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.\n\nThis low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\\ref{prop:correct_sign} predicts that approximately 80.9\\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.\n\n\\subsection{RL Training Configuration}\n\\label{sec:rl_config}\n\nAll conditions use the RAGEN framework~\\cite{ragen2025} with the GRPO algorithm~\\cite{shao2024deepseekmath}. Table~\\ref{tab:hyperparameters} lists the shared hyperparameters. The discount factor $\\gamma$ applies only to step-independent return computation (Equation~\\ref{eq:step_return}); episode-level conditions use undiscounted returns over the complete trajectory.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Shared RL training hyperparameters across all conditions.}\n\\label{tab:hyperparameters}\n\\begin{tabular}{lc}\n\\toprule\nParameter & Value \\\\\n\\midrule\nGroup size $K$ & 8 \\\\\nLearning rate & $1 \\times 10^{-6}$ \\\\\nKL penalty $\\beta$ & 0.01 \\\\\nDiscount $\\gamma$ & 0.95 \\\\\nInvalid action penalty & 0.1 \\\\\nTasks per training step & 16 \\\\\nTraining steps & 15 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation Protocol}\n\\label{sec:eval_protocol}\n\nWe evaluate on two task sets: (1)~a 32-task in-distribution set from the original RAGEN validation split, and (2)~a 134-task out-of-distribution (OOD) set for generalization assessment. All main results report the 134-task OOD set; in-distribution numbers serve as secondary references. Evaluation runs every 5 training steps.\n\nThe primary metric is success rate (pass@1): the fraction of episodes completed within 50 steps. We also report pass@$k$ for $k \\in \\{2, 4, 8\\}$. As a diagnostic, we track \\textit{action validity rate}, defined as the fraction of agent outputs that constitute syntactically valid environment commands (as opposed to malformed, empty, or repeated text). Action validity measures basic policy coherence, distinct from task completion. All results are single-seed unless stated otherwise; two-seed replication is reported where available.\n\n\\subsection{Experimental Conditions}\n\\label{sec:conditions}\n\nWe evaluate seven conditions organized around three designs: factorial mechanism separation (Conditions~1--3), auxiliary baselines (Conditions~4--5), and parameter sweeps (Conditions~6--7).\n\n\\paragraph{Condition 1: Episode-level GRPO.}\nEach complete trajectory serves as a single GRPO sample with one shared advantage for all tokens. Both failure mechanisms are absent: the full context is preserved (no M1) and no per-window advantage can carry misattributed sign (no M2). Two seeds.\n\n\\paragraph{Condition 2: Step-independent $h{=}2$.}\nEach trajectory is segmented into fixed windows of $h = 2$ interaction steps, with each window receiving its own GRPO advantage. Both M1 (truncated context) and M2 (advantage sign determined by episode outcome rather than local action quality) are active. This is the default RAGEN configuration and represents the standard approach for multi-turn agent RL. Two seeds.\n\n\\paragraph{Condition 3: Step-independent $h{=}2$ with episode advantage.}\nThe factorial complement. Windows are constructed identically to Condition~2, but all windows within an episode share a single episode-level advantage instead of independent per-window values. M1 remains active (truncated observations) while M2 is eliminated (no per-window sign assignment). The performance gap between Conditions~2 and~3 is therefore attributable to M2 alone. Two seeds.\n\nConditions~1--3 form a $2 \\times 2$ factorial design over observation scope (windowed vs.\\ full) and advantage scope (per-window vs.\\ episode-level), as described in Section~\\ref{sec:factorial_design}. The fourth cell (full observation with per-window advantage) is degenerate: with full context, only one window exists per episode, so per-window and episode-level advantage coincide.\n\n\\paragraph{Condition 4: Dense reward.}\nStep-independent $h{=}2$ with a per-step bonus of $+0.15$ for each syntactically valid action. This tests whether dense reward shaping can compensate for step-independent credit assignment failure. Training extends to 30 steps.\n\n\\paragraph{Condition 5: REINFORCE++ baseline.}\nEpisode-level training with a per-token running-mean baseline instead of GRPO group normalization. No value function is used. This condition was originally planned as a GAE baseline with a learned critic; we substituted REINFORCE++ after TRL~1.1.0 removed the required \\texttt{AutoModelForCausalLMWithValueHead} class.\n\n\\paragraph{Condition 6: Discount factor sweep.}\nStep-independent $h{=}5$ with $\\gamma \\in \\{0.50, 0.80, 0.95, 1.00\\}$. At $\\gamma = 1.0$, all windows receive identical magnitude from the terminal return; magnitude decay vanishes but sign misattribution remains. Collapse at $\\gamma = 1.0$ would confirm that sign misattribution alone suffices to cause failure, independent of discount-induced magnitude variation.\n\n\\paragraph{Condition 7: Window-size sweep.}\nStep-independent training with $h \\in \\{2, 5, 10, 20\\}$ compared against episode-level training ($h = T$, the full trajectory). Smaller $h$ increases M1 severity through reduced per-window context and produces more windows per episode. Data collection for $h \\in \\{10, 20\\}$ is in progress.\n\n\\subsection{Results}\n\\label{sec:results}\n\nResults are organized around three comparisons: (1)~episode-level vs.\\ step-independent training dynamics (Section~\\ref{sec:results_main}), (2)~factorial mechanism separation (Section~\\ref{sec:results_factorial}), and (3)~window-size and discount-factor ablations (Section~\\ref{sec:results_hsweep}). \\placeholder{Results sections to follow.}\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T20:19:21.338711+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T20:19:21.338883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T20:19:21.339062+00:00_

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
18	We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \
…[truncated 6247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T20:19:21.339221+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

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
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T20:19:21.339350+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T20:19:21.339469+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

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
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T20:19:21.339610+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T20:19:21.339732+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

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
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T20:19:21.339852+00:00_

18:We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.
20:This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\ref{prop:correct_sign} predicts that approximately 80.9\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T20:19:21.340005+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
  "old_string": "The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.",
  "new_string": "The SFT checkpoint therefore occupies the regime where sign misattribution is most severe."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "old_string": "The SFT checkpoint thus places the system in a regime where sign misattribution is near-maximal, producing a stringent test of the mechanism.",
    "new_string": "The SFT checkpoint therefore occupies the regime where sign misattribution is most severe."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T20:19:21.340154+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T20:19:21.340271+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

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
  "recorded_role": "tool",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T20:19:21.340388+00:00_

18:We use Qwen3-1.7B (instruct variant) as the base policy. Before RL training, we perform supervised fine-tuning (SFT) on 2{,}546 expert demonstrations from ALFWorld for 2 epochs with learning rate $5 \times 10^{-6}$. The resulting SFT checkpoint achieves 12.5\% success rate on a held-out 32-task in-distribution validation set (4 of 32 tasks). The pre-SFT model achieves 0\% success in zero-shot evaluation, so SFT provides a necessary initialization for RL.
20:This low baseline is analytically significant. At success probability $p = 0.125$ with group size $K = 8$, Proposition~\ref{prop:correct_sign} predicts that approximately 80.9\% of gradient updates carry incorrect advantage sign under step-independent training. The SFT checkpoint therefore occupies the regime where sign misattribution is most severe.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experiments_setup_20260518T201250",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-18T20:19:21.340586+00:00_

Remaining "ing" matches are all nouns/adjectives ("fine-tuning", "resulting", "training"), not trailing participial phrases. File is clean.

Rewrite complete. The setup (§5.1--5.5) covers ~850 words across five subsections: Environment, Base Model/SFT, RL Config (with booktabs table), Evaluation Protocol (32 in-dist + 134 OOD), and Experimental Conditions (7 conditions with factorial design, baselines, and sweeps). Results stub preserved as placeholder. No em-dashes, no trailing -ing phrases, no \placeholder in setup content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experiments_setup_20260518T201250"
}
```

</details>

---
