# paper writing method

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 97
- **Recorded user turns:** 0
- **Tool calls:** 48
- **Original source:** `logs/chats/worker_paper_writing_method_20260517T070859.jsonl`
- **Structured JSON:** [`d6ee1f41c7bb8c285889.json`](../../sessions/d6/d6ee1f41c7bb8c285889.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

97 recorded events

### Tool call

_source line 1 · 2026-05-17T07:13:04.127509+00:00_

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
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T07:13:04.128145+00:00_

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
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T07:13:04.128346+00:00_

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
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T07:13:04.128731+00:00_

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
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T07:13:04.128925+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find project context files",
  "subagent_type": "Explore",
  "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ for:\n1. Any literature_map file (yaml or json) - read its contents\n2. Any existing paper files in docs/paper/ directory\n3. The ROADMAP.md or ideas.md file for context on the research\n4. Any registry file that might have experiment results\n\nSearch breadth: very thorough"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Agent",
  "tool_args": {
    "description": "Find project context files",
    "subagent_type": "Explore",
    "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ for:\n1. Any literature_map file (yaml or json) - read its contents\n2. Any existing paper files in docs/paper/ directory\n3. The ROADMAP.md or ideas.md file for context on the research\n4. Any registry file that might have experiment results\n\nSearch breadth: very thorough"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T07:13:04.129105+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/literature_map.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/literature_map.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T07:13:04.129232+00:00_

artifacts/_project/report/literature_map.yaml
literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T07:13:04.129367+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T07:13:04.129492+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T07:13:04.129614+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/ROADMAP.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/ROADMAP.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T07:13:04.129756+00:00_

ROADMAP.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T07:13:04.129877+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/ideas.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/ideas.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T07:13:04.130002+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T07:13:04.130153+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/registry*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/registry*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T07:13:04.130286+00:00_

registry.lock
registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T07:13:04.130417+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl -type f -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl -type f -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | head -50"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T07:13:04.130561+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_monitor_exp_001_check_20260513T191117_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_diagnose_exp013d_20260514T083812_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_monitor_exp028c_step5_val_20260516T030007_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_research_inference-diff-diagnosis_20260515T042541_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_code_verify-alfworld-score_20260514T055837_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_monitor_exp015-val-train-transition_20260514T130554_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_code_exp028_config_prep_20260515T202818_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_ops_exp012-restart_20260514T063030_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_check_exp029_progress_2h20m_20260516T150629_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_monitor_exp013b-early-steps_20260514T081847_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_fix_recreate-checkpoint-dir_20260514T211131_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs/workers/worker_code_exp006_config_20260513T232524_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/logs
…[truncated 5540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T07:13:04.130741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T07:13:04.130873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T07:13:04.131130+00:00_

1	# B-IAVR Literature Map
2	# Updated: 2026-05-16
3	# Categories: direct-competitor, method-component, background, evaluation
4	# Roles: predecessor, competitor, baseline, evaluation, background
5	
6	papers:
7	
8	  # ============================================================
9	  # Direction 1: Self-Verification / Self-Correction in LLM Agents
10	  # ============================================================
11	
12	  - id: kamoi2024self-correction-survey
13	    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
14	    authors: "Kamoi et al."
15	    venue: "arXiv"
16	    year: 2024
17	    arxiv_id: "2406.01297"
18	    category: background
19	    role: background
20	    relevance_note: >
21	      Foundational survey establishing that pure intrinsic self-correction is unreliable.
22	      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.
23	
24	  - id: tie2025correctbench
25	    title: "Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs"
26	    authors: "Tie et al."
27	    venue: "NeurIPS 2025 Datasets & Benchmarks"
28	    year: 2025
29	    arxiv_id: "2510.16062"
30	    category: background
31	    role: background
32	    relevance_note: >
33	      Benchmark showing self-correction has diminishing returns when applied uniformly.
34	      Supports B-IAVR's selective verification design over blanket correction.
35	
36	  - id: self-verification-dilemma-2026
37	    title: "Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning"
38	    authors: "Long et al."
39	    venue: "arXiv"
40	    year: 2026
41	    arxiv_id: "2602.03485"
42	    category: background
43	    role: background
44	    relevance_note: >
45	      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.
46	      Directly supports B-IAVR's core thesis that verification should be selective.
47	      Their experience-p
…[truncated 25608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T07:13:04.131321+00:00_

1	# cost-verify-agent-rl — Research Dashboard
2	
3	> 最后更新: 2026-05-16 23:52 UTC | 更新原因: Post-MVP: 进入 research phase, 新 framing + experiment plan 完成
4	
5	## 核心方向
6	Training interactive agents for selective self-verification via RL. Dual contribution:
7	1. **Training methodology**: Episode-level credit assignment is critical for multi-turn RL (step-independent catastrophically collapses)
8	2. **Selective verification**: Action-change as intrinsic reward for learning WHEN to verify
9	
10	详见 paper_framing.md。
11	
12	## 当前阶段
13	🔬 **Research Phase** (MVP 通过 2026-05-16, D053)
14	
15	### MVP 结果总结
16	- exp029 episode-level GRPO: step 5 val = 25% (2x baseline 12.5%) ✅
17	- exp028c step-independent (h=2): step 10 val = 0% (catastrophic collapse) ❌
18	- 机制: gamma^49 = 7.7%, 长 horizon credit assignment 完全失效
19	
20	### 当前状态
21	- exp029 训练状态待确认（registry auto-watchdog 标记 failed，可能误判）
22	- paper_framing.md 已重写（dual contribution framing）
23	- experiment_plan.yaml 已重写（16 experiments, 918 GPU-h total）
24	- Dream simulate 待完成
25	
26	## 近期任务
27	- [ ] 确认 exp029 训练是否仍在运行，报告最新 step/metrics
28	- [ ] 如训练已死：重启 + 部署 tatsu parallel patch
29	- [ ] Dream simulate 完成后：审阅 + 决定 P0 实验启动顺序
30	- [ ] 启动 plan_002 (h-sweep) 和 plan_003 (multi-seed) — 可并行
31	- [ ] plan_004 credit assignment analysis (分析/绘图，低 GPU)
32	
33	## GPU 预算
34	- 分配：bjb1-17606 cuda:0,1（2x RTX PRO 6000 96GB）
35	- P0 预算：268 GPU-h (~6 days)
36	- P0+P1 预算：652 GPU-h (~14 days)
37	- 全部：918 GPU-h (~18 days)
38	
39	## 关键风险
40	1. **收敛上限**: exp029 step 5=25%，能否达 40%+ 支撑 cost-efficiency story？
41	2. **Episode-level novelty**: reviewer 可能认为 "episode-level RL is obvious" — h-sweep + 机制分析是关键防御
42	3. **Phase B 可行性**: 如果收敛后 success < 40%，selective verification story 弱 → 退到 Plan A (pure methodology paper)
43	
44	## 竞争格局
45	| 系统 | 方法 | ALFWorld | 差异 |
46	|------|------|----------|------|
47	| Self-Guide (2026) | Always-on verification | 72.7% | 我们做 selective |
48	| ARES (2603.07915) | SFT router | 52.7% token↓ | SFT vs RL |
49	| RAGEN (2025) | GRPO for a
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T07:13:04.131501+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T07:13:04.131645+00:00_

File content (39578 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T07:13:04.131802+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ | grep -E \"\\.md|\\.yaml|\\.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ | grep -E \"\\.md|\\.yaml|\\.json\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T07:13:04.131978+00:00_

-rw-r--r--  1 ubuntu ubuntu  16408 May 17 07:06 AGENTS.md
-rw-------  1 ubuntu ubuntu   3867 May 17 06:22 ROADMAP.md
-rw-------  1 ubuntu ubuntu   1121 May 15 03:21 constraints.yaml
-rw-------  1 ubuntu ubuntu  55669 May 17 06:22 decisions.yaml
-rw-------  1 ubuntu ubuntu    877 May 17 00:31 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu    882 May 17 00:31 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu  17175 May 17 06:26 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  25212 May 16 00:19 literature_map.yaml
-rw-r--r--  1 ubuntu ubuntu   1741 May 15 20:45 memory.md
-rw-r--r--  1 ubuntu ubuntu   8100 May 17 06:26 paper_framing.md
-rw-------  1 ubuntu ubuntu 101606 May 17 04:37 registry.yaml
-rw-r--r--  1 ubuntu ubuntu   5691 May 17 04:37 report.md
-rw-r--r--  1 ubuntu ubuntu  15730 May 17 07:06 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T07:13:04.132174+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl -type d -name \"paper\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl -type d -name \"paper\" | head -5"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T07:13:04.132306+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/_project/paper

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T07:13:04.132437+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl -type f -name \"paper_*.yaml\" -o -name \"paper_*.md\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl -type f -name \"paper_*.yaml\" -o -name \"paper_*.md\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T07:13:04.132556+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260516T235255/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260516T235255/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/dream_reports/dream_20260516T235255/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T07:13:04.132725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T07:13:04.132891+00:00_

1	# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents
2	
3	> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)
4	
5	## Core Insight
6	
7	Multi-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：
8	
9	1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 "先探索 drawer 再去 countertop"）
10	2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：
11	   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）
12	   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）
13	   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality
14	   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^48 ≈ 8%），但方向错误比幅度衰减更致命
15	
16	Episode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。
17	
18	**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。
19	
20	## Story Arc
21	
22	**Dual contribution**: Training methodology diagnosis + Selective verification system
23	
24	叙事线：
25	1. Self-verification 对 interactive agents 有用，但 always-on 成本高
26	2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）
27	3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决
28	4. 分析 "为什么社区默认走向 step-independent"（context window 限制 + token-level training 惯性 + framework design accident）
29	5. 在 episode-level 基础上，用 actio
…[truncated 4871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T07:13:04.133063+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper -type f 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T07:13:04.133186+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T07:13:04.133310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-17T07:13:04.133465+00:00_

1	# Writing Plan — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents
2	# Generated: 2026-05-17
3	# Phase 1 focus: Method + Theoretical Analysis (does not depend on h-sweep data)
4	
5	meta:
6	  venue: "NeurIPS 2026 / ICLR 2026 (TBD)"
7	  track: main
8	  template: null  # TODO: download NeurIPS 2026 official template via WebSearch
9	  template_note: "Template not yet available locally. Will fetch from official site before Step 4."
10	  page_limit: 9
11	  deadline: null  # TBD by Director
12	  core_claim: >
13	    LLM agent community's default step-independent RL training catastrophically collapses
14	    in multi-turn tasks due to dual mechanism failure (policy information loss + advantage
15	    sign misattribution); episode-level GRPO resolves both, enabling selective verification
16	    policy training via action-change reward.
17	  created_at: "2026-05-17T12:00:00Z"
18	  phase_1_scope: "Method + Theoretical Analysis sections only"
19	
20	paper_outline:
21	  - section: abstract
22	    word_budget: 220
23	    core_bullets:
24	      - "Problem: LLM agents trained with step-independent RL catastrophically collapse in multi-turn interactive tasks (0% success by step 10)"
25	      - "Diagnosis: Dual mechanism failure -- (1) policy information loss from h-step truncation, (2) advantage sign misattribution where gradient direction reflects episode outcome not local action quality"
26	      - "Solution: Episode-level GRPO resolves both mechanisms; on this foundation, train selective verification policy using action-change as informativeness signal"
27	      - "Results: Episode-level achieves 28% vs 0% step-independent; selective verification reduces cost 40%+ while maintaining performance [Phase B TBD]"
28	    dependencies: [experiments, method, theoretical_analysis]
29	
30	  - section: introduction
31	    word_budget: 1400
32	    core_bullets:
33	      - "Hook: Multi-turn interactive agents (ALFWorld, WebArena) need RL training, but co
…[truncated 5594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T07:13:04.133647+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T07:13:04.133780+00:00_

total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 14 17:57 .
drwxr-xr-x 4 ubuntu ubuntu 4096 May 15 12:13 ..

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T07:13:04.133909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -150 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "head -150 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T07:13:04.134059+00:00_

baseline: null
experiments:
  exp_001:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T18:26:40.715Z'
    updated_at: '2026-05-13T19:13:39.086Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/cost-verify-agent-rl/RAGEN && ALFWORLD_DATA=/root/autodl-tmp/alfworld
        CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp001"
      server: bjb1-17606
      gpu:
      - cuda:0
      - cuda:1
      pid: '87845'
      log_path: ~/runs/cost-verify-agent-rl/exp_001.log
      submitted_at: '2026-05-13T18:34:53.576Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      checkpoint_path: N/A
      failure_reason: 'ValueError: decoder prompt (4096 tokens) + output tokens >
        max_model_len (4096). Multi-turn rollout prompt exceeded limit at step 7.'
      wall_clock_seconds: 2325.5
      gpu_hours: 1.29
    conclusion: failed
    completed_at: '2026-05-13T19:13:39.086Z'
  exp_001b:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T19:14:10.718Z'
    updated_at: '2026-05-13T19:29:05.714Z'
    spec:
      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
        base && cd /root/cost-verify-agent-rl/RAGEN && ALFWORLD_DATA=/root/autodl-tmp/alfworld
        CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _alfworld_exp001b"
      server: bjb1-17606
      gpu:
      - cuda:0
      - cuda:1
      pid: '93789'
      log_path: ~/runs/cost-verify-agent-rl/exp_001b.log
      submitted_at: '2026-05-13T19:15:38.523Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      failure_reason: 'Same bootstrap failure as exp_001: base model (Qwen3-1.7B)
        cannot produce &lt;think>/&lt;answer> format. pg_loss≈0, KL=0, 95.6% invalid actions.
        Killed at step 4/50.'
      checkpoint_path: N/A
      wall_clock_seconds: 807.2
      gpu_hours: 0.45
    conclusion: fai
…[truncated 3555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T07:13:04.134252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T07:13:04.134387+00:00_

1	# Citation Audit — 2026-05-15
2	
3	完整审计结果已写入 artifacts/citation_audit.md。
4	
5	## 审计摘要
6	
7	- 验证论文：27 篇（literature_map.yaml 全部条目）+ 1 篇额外（Thinkless）
8	- 验证通过：20 篇
9	- 需要修正：7 篇（3 个严重问题，2 个中等问题，2 个轻微问题）
10	- 关键发现：AgentPRM arXiv ID/作者/标题全错；Huang2024 作者不匹配；DAPO 标题错误；CFGM 会议和年份错误
11	
12	# Adaptive KL 可行性 — 2026-05-15
13	
14	verl 框架已内置 `AdaptiveKLController`（Ziegler 2019），RAGEN `agent_trainer.py` 已完整接入 reward-level KL adaptive 链路。**零代码修改，纯 YAML 配置切换**（~8 行）：
15	- `algorithm.use_kl_in_reward: True` + `kl_ctrl.type: adaptive`
16	- `actor.use_kl_loss: False`
17	- `target_kl: 0.1`, `kl_coef: 0.005`（初始值），`horizon: 10000`
18	
19	当前 exp027 用的是 loss-level KL（`use_kl_loss` + 静态 `kl_loss_coef`）。如需切换，实现 <1h，验证 2-4h。
20	
21	风险：reward-level KL 通过 advantage 间接影响梯度，与 loss-level 直接约束不同。如 reward-level 效果不理想，备选 Plan C（loss-level adaptive）需 ~30 行代码，半天可完成。
22	
23	# 失败模式记录
24	
25	- [失败模式] Ray raylet 异常终止：ActorUnavailableError RPC error Socket closed rpc_code: 14，Raylet 被 SIGKILL（OOM killer 或内存访问错误）。出现于 exp013e（val→train 过渡）和 exp027（step 4→5 过渡）。→ 修复方案：(1) 检查 cgroup 内存限制 vs Ray object_store + worker 内存总和 (2) 降低 env_groups 减少并发内存峰值 (3) 显式设置 ray_kwargs.ray_init.object_store_memory 限制 Ray 内存分配 (4) 用 RAY_memory_monitor_refresh_ms=0 禁用内存监控阈值冲突。
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-17T07:13:04.134547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/experiment_plan.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/experiment_plan.yaml",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T07:13:04.134737+00:00_

1	# Experiment Plan — Learning When to Verify
2	# Post-MVP rewrite: 2026-05-17 (Dream Review feedback integrated)
3	# Based on: paper_framing.md (dual mechanism theory + dual contribution)
4	#
5	# Claims:
6	#   claim_1: Step-independent GRPO catastrophically fails for multi-turn agents (dual mechanism)
7	#   claim_2: Action-change is effective intrinsic reward for verification informativeness
8	#   claim_3: Learned selective policy matches always-on at reduced cost
9	#
10	# Phases:
11	#   A+  — Episode-level training to convergence + consolidation (Claim 1)
12	#   B   — Selective verification implementation + training (Claims 2 & 3)
13	#   C   — Ablations & baselines (all claims, includes GAE)
14	#   D   — Scaling & generalization (reviewer defense)
15	#
16	# GPU budget: 2x RTX PRO 6000 96GB (cuda:0, cuda:1) @ bjb1-17606
17	# Key: h-sweep/GAE only 15 steps (sufficient to observe collapse pattern)
18	# Timeline at full utilization: P0 ~8 days, P0+P1 ~14 days, all ~20 days
19	
20	experiments:
21	
22	  # ============================================================
23	  # Phase A+: Episode-Level Training to Convergence
24	  # ============================================================
25	
26	  - id: "plan_001"
27	    title: "Episode-level GRPO convergence (exp029 continuation)"
28	    claim: "Claim 1"
29	    phase: "A+"
30	    priority: "P0"
31	    depends_on: []
32	    registry_id: "exp029_episode_level"
33	    status: "done"
34	    description: >
35	      Episode-level GRPO (context_window_mode: full) on Qwen3-1.7B + ALFWorld.
36	      50 steps, dual-GPU. MVP passed at step 5 (val=25%, 2x baseline 12.5%).
37	      Continue to convergence (step 20+) with tatsu parallel patch for 4x val speedup.
38	    hypothesis: >
39	      Episode-level training enables stable RL for multi-turn agents,
40	      reaching ≥40% success by convergence.
41	    metrics: ["success_rate", "action_is_valid", "kl_divergence", "entropy"]
42	    gpu_hours_estimate: 48
43	    framing_ref: "claim_
…[truncated 7640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-17T07:13:04.134909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/*.md 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/*.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/*.md 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T07:13:04.135039+00:00_

    20 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/constraints.yaml
  1052 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml
    25 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/dream_registry.yaml
   411 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/experiment_plan.yaml
   626 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml
  2329 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/registry.yaml
   296 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml
   269 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/AGENTS.md
    66 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ROADMAP.md
    25 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md
   101 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md
    66 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/report.md
  5286 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-17T07:13:04.135177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/AGENTS.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/AGENTS.md"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-17T07:13:04.135350+00:00_

1	## 当前项目
2	当前绑定项目：**cost-verify-agent-rl**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("cost-verify-agent-rl")` 或 `load_project_config("cost-verify-agent-rl", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## Worker 操作规范
11	
12	### paper-writing-norms
13	
14	# 论文写作风格规范
15	
16	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
17	
18	---
19	
20	## 一、总体写作哲学
21	
22	### 1.1 故事驱动，不是数据堆砌
23	
24	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
25	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
26	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
27	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
28	
29	### 1.2 主线统一性
30	
31	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
32	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
33	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
34	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
35	
36	### 1.3 专有名词必须有定义
37	
38	- 首次出现的专有名词/缩写必须给出完整定义和解释
39	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
40	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
41	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
42	
43	### 1.4 写作前必读同类优秀论文
44	
45	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
46	- 重点学：
47	  - Abstract 怎么用最少篇幅讲完故事
48	  - Introduction 怎么从大问题切入到具体贡献
49	  - Related Work 怎么 positioning 自己（不是 survey）
50	  - Table/Figure 怎么压缩信息密度
51	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
52	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
53	
54	---
55	
56	## 二、Abstract 写作规范
57	
58	### 2.1 四个必答问题（150-250 words）
59	
60	Abstract 必须在很短的篇幅内清楚回答：
61	1. **研究什么问题** — 1-2 句话交代背景和痛点
62	2. **为什么重要** — 现有方法的不足（不用写太多）
63	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
6
…[truncated 8512 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T07:13:04.135514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/report.md"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T07:13:04.135679+00:00_

1	# Handover — 2026-05-17
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| hsweep_h2_seed1 | Step-independent GRPO with h=2 (minimal context window) will catastrophically collapse within 5 steps due to extreme credit assignment failure (gamma^48 ≈ 8%), providing systematic evidence for the episode-level advantage | — | — | — |
9	
10	## 待处理
11	- exp025c（等待人工审批）
12	- exp028_prereq_zeroshot_instruct: Qwen3-1.7B-Instruct 零样本 ALFWorld eval，验证"SFT是毒药"假设。如果 Instruct ≥15% success（vs SFT checkpoint 6.25%），则确认 SFT 起点有害，exp028a 可跳过 SFT 直接 GRPO。（准备中）
13	- exp021_sft_ragen_format: Two-stage SFT with RAGEN-format data (v4). From exp008_sft checkpoint, fine-tune with v4 data (RAGEN Turn/State/Reward structure, fixed system prompt with consistent &lt;answer> tag instruction). LR=5e-6, 2 epochs. Validate via RAGEN val_before_train (not eval_sft_fast). Pass: RAGEN val success >= 10%, action_is_valid >= 85%.（准备中）
14	- exp020d_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Symlink fix for response_mask assertion (proven in exp020b). exp020c failed: Hydra key path wrong.（准备中）
15	- exp020c_grpo_from_sft: GRPO from exp019b SFT checkpoint (20% success baseline). Sparse reward only (won=10.0), LR=5e-7, kl_loss_coef=0.1, max_grad_norm=1.0, 30 steps. Pass: success ≥ 20%. Fix: symlink + enable_response_mask=false (exp020/020b crashed on response_mask assertion).（准备中）
16	- exp019c_expert_sft_v3: Two-stage Expert SFT（重试）: 从 exp008_sft checkpoint 出发，用 v3 数据（保留原始 move actions + admissible actions augmentation）微调。LR=5e-6, 2 epochs, batch=4, grad_accum=4, max_seq=4096。Pass: success ≥ 10%, format_ok ≥ 90%, action_is_valid ≥ 85%。（准备中）
17	- exp019b_expert_sft_v2（准备中）
18	- exp018_sft_grpo: Expert SFT → Sparse GRPO：从 exp017 SFT checkpoint 开始纯 sparse GRPO 训练。SFT 提升 baseline success rate（≥10%），
…[truncated 2811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T07:13:04.135918+00:00_

Perfect! Now I have a comprehensive overview. Let me create a summary report of all the findings.

## Summary Report: Project Search — cost-verify-agent-rl

I've completed a thorough search of the project directory at `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/`. Here are all the key findings:

---

### 1. **Literature Map**

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml` (626 lines)

**Contents:** Comprehensive bibliography organized into 4 categories and 5 research directions:

- **Direction 1: Self-Verification/Self-Correction in LLM Agents** (6 papers) — Including foundational work by Kamoi et al. (2024), Self-Verification Dilemma (2026), and Zhang et al. on incentivizing verification
  
- **Direction 2: Agent RL Training** (17 papers) — Core methods like GiGPO (Feng et al., NeurIPS 2025), Self-Guide (Wang et al., 2026), RAGEN, DAPO, SORL, and newer work like PA-MoE, SDAR, HCAPO, ACT, RWML, SKILL0, etc.

- **Direction 3: Selective Verification/Adaptive Computation** (13 papers) — Direct competitors including Derailer-Rerailer (ACL 2025), Sherlock, ARES, Agent-Omit, AutoThink, Thinkless, and related work on verification timing

- **Direction 4: ALFWorld/Interactive Environment Benchmarks** (7 papers) — ReflAct (93.3% SOTA on ALFWorld), AgentPRM, Retrospex, CFGM

**Last Updated:** 2026-05-16

---

### 2. **Paper Files**

**Docs/Paper Directory:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/` — Empty (no LaTeX files yet)

**Paper-Related Files in Root:**

- **paper_framing.md** (101 lines) — Core research framing document with:
  - **Core Insight:** Multi-turn agents need selective verification; step-independent RL training catastrophically fails on long horizons
  - **Dual Mechanism Failure:** (1) Policy Information Loss from h-step truncation, (2) Advantage Sign Misattribution (γ^k decay)
  - **Solution:** Episode-level 
…[truncated 6896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T07:13:04.136091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T07:13:04.136269+00:00_

1	# Paper Framing — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents
2	
3	> Post-MVP 重写 (2026-05-17) | D054 framing pivot + Dream Review feedback (weak reject → 修正理论)
4	
5	## Core Insight
6	
7	Multi-turn interactive agents 的 self-verification 大部分是 confirmatory（不改变行为）而非 corrective。训练 agent 学 selective verification 的前提是 RL 训练本身能 work。我们发现 LLM agent 社区默认的 step-independent training 在长 horizon 任务中灾难性崩溃，根因是**双机制失效**：
8	
9	1. **Policy Information Loss**: 短窗口（h 步）的 policy 无法学习跨步策略（如 "先探索 drawer 再去 countertop"）
10	2. **Advantage Sign Misattribution**: step_independent 中，per-window advantage 的**符号**由 episode 成败决定，而非 window-local action quality：
11	   - 失败 episode 中的好 action → 获得负 advantage（被错误惩罚）
12	   - 成功 episode 中的差 action → 获得正 advantage（被错误强化）
13	   - 梯度方向（reinforce/suppress）反映 episode outcome 而非 local decision quality
14	   - 附加：γ^k magnitude decay 使早期 window 信号更弱（γ^48 ≈ 8%），但方向错误比幅度衰减更致命
15	
16	Episode-level training 同时解决两者：policy 看全历史（解决 1），整条 trajectory 作为一个 GRPO 样本，所有 tokens 共享同一 advantage — 虽然仍是 episode-level credit（非 per-token），但消除了 window 间的 sign misattribution，因为不再需要将 episode reward 分配到独立优化的子窗口（解决 2）。
17	
18	**技术澄清**：GRPO 算法本身是 bandit-style（advantage = (R-μ)/σ，无显式 γ），但 RAGEN 的 step_independent 实现在 `compute_step_discounted_returns()` 中引入 γ 计算每个 window 的 return（代码：`agent_trainer.py:271-340`）。γ^(T-t) decay 对 step_independent 模式是代码事实，不是类比。Episode-level 模式下无此问题：整条 trajectory 只有一个 return = episode_reward。
19	
20	## Story Arc
21	
22	**Dual contribution**: Training methodology diagnosis + Selective verification system
23	
24	叙事线：
25	1. Self-verification 对 interactive agents 有用，但 always-on 成本高
26	2. 训练 agent 学 WHEN to verify 需要 RL → 但 LLM agent 社区默认的 step-independent training 在多轮任务上灾难性崩溃（0% at step 10）
27	3. 我们诊断双机制根因（information loss + advantage sign misattribution），提出 episode-level GRPO 解决
28	4. 分析 "为什么社区默认走向 step-independent"（context window 限制 + token-level training 惯性 + framework design accident）
29	5. 在 episode-level 基础上，用 actio
…[truncated 4871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T07:13:04.136427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/writing_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T07:13:04.136677+00:00_

1	# Writing Plan — Learning When to Verify: RL-Trained Selective Self-Verification for Interactive Agents
2	# Generated: 2026-05-17
3	# Phase 1 focus: Method + Theoretical Analysis (does not depend on h-sweep data)
4	
5	meta:
6	  venue: "NeurIPS 2026 / ICLR 2026 (TBD)"
7	  track: main
8	  template: null  # TODO: download NeurIPS 2026 official template via WebSearch
9	  template_note: "Template not yet available locally. Will fetch from official site before Step 4."
10	  page_limit: 9
11	  deadline: null  # TBD by Director
12	  core_claim: >
13	    LLM agent community's default step-independent RL training catastrophically collapses
14	    in multi-turn tasks due to dual mechanism failure (policy information loss + advantage
15	    sign misattribution); episode-level GRPO resolves both, enabling selective verification
16	    policy training via action-change reward.
17	  created_at: "2026-05-17T12:00:00Z"
18	  phase_1_scope: "Method + Theoretical Analysis sections only"
19	
20	paper_outline:
21	  - section: abstract
22	    word_budget: 220
23	    core_bullets:
24	      - "Problem: LLM agents trained with step-independent RL catastrophically collapse in multi-turn interactive tasks (0% success by step 10)"
25	      - "Diagnosis: Dual mechanism failure -- (1) policy information loss from h-step truncation, (2) advantage sign misattribution where gradient direction reflects episode outcome not local action quality"
26	      - "Solution: Episode-level GRPO resolves both mechanisms; on this foundation, train selective verification policy using action-change as informativeness signal"
27	      - "Results: Episode-level achieves 28% vs 0% step-independent; selective verification reduces cost 40%+ while maintaining performance [Phase B TBD]"
28	    dependencies: [experiments, method, theoretical_analysis]
29	
30	  - section: introduction
31	    word_budget: 1400
32	    core_bullets:
33	      - "Hook: Multi-turn interactive agents (ALFWorld, WebArena) need RL training, but co
…[truncated 14808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T07:13:04.136853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T07:13:04.137027+00:00_

0	_next_id: 59
1	decisions:
2	- id: D001
3	  date: 2026-05-13 17:33 UTC
4	  summary: MVP 选择 ALFWorld + Qwen3-1.7B 单环境验证 B-IAVR 核心假设
5	  rationale: ALFWorld 离散动作空间使 action_changed 信号最清晰，semantic canonicalization 简单（verb,object,receptacle三元组）。Qwen3-1.7B
6	    有充分 headroom（+8.6pp on ALFWorld）。MVP 只需验证"agent 能学会选择性验证"这一核心假设，不需要跨环境/跨模型。2×GPU
7	    足够 1.7B+LoRA 训练。
8	  related_experiments: []
9	  depends_on: []
10	- id: D002
11	  date: 2026-05-13 18:39 UTC
12	  summary: Phase A 使用全量微调（非 LoRA），匹配 Self-Guide 原始论文设置
13	  rationale: Self-Guide 原文用全量微调 GRPO。1.7B 模型在 94GB VRAM 下全量微调显存仅 38.5GB，完全可行。匹配 baseline
14	    设置确保公平对比。IDEA_BRIEF 提及 LoRA 是基于 H100 80GB 的资源估算，RTX PRO 6000 94GB 无需节省。
15	  related_experiments:
16	  - exp_id: exp_001
17	    role: Phase A baseline
18	    result: running
19	  depends_on:
20	  - D001
21	- id: D003
22	  date: 2026-05-13 23:55 UTC
23	  summary: Kill exp003，Phase A bootstrap 失败确认，等待 invalid action 根因诊断后决定修复方向
24	  rationale: 'exp003 step 1: invalid_action=95.3%, pg_loss≈0, 每步 1.6h（100步=160h）。GRPO
25	    从 0.125% valid action 中无法获得有效学习信号。Qwen3 无独立 Instruct 版，Plan B 失效。需先诊断 invalid
26	    action 根因（格式冲突 / token 问题 / prompt 不兼容）再选修复路径。'
27	  related_experiments:
28	  - exp_id: exp003
29	    role: primary
30	    result: failed - bootstrap failure, 95% invalid actions, pg_loss≈0
31	  depends_on:
32	  - D002
33	- id: D004
34	  date: 2026-05-14 00:10 UTC
35	  summary: 采用方案 A（修改解析器适配 Qwen3 格式）+ prompt 增强 + 速度优化，解决 bootstrap 失败
36	  rationale: 根因确认：Qwen3-1.7B 原生输出 &lt;think>...&lt;/think> 后直接跟自然语言，不生成 &lt;answer> 标签。RAGEN
37	    解析器正则要求 &lt;answer> 导致 95% invalid。方案 A 最快（1-2h 改代码）、最低风险（不换模型不加训练阶段），同时优化速度（关闭 collapse
38	    multi_turn 省 35% 步耗时 + 减 traj/step）。
39	  related_experiments:
40	  - exp_id: exp003
41	    role: diagnostic
42	    result: '32/32 samples confirm: no &lt;answer> tag in Qwen3 output'
43	  depends_on:
44	  - D003
45	- id: D005
46	  date: 2026-05-14 02:56 UTC
47	  summary: exp007 borderline 但不 pivot SFT，提高 LR 到 5e-6 重跑 GRPO
48	  rationale: exp007 step 10 
…[truncated 2448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T07:13:04.137180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml",
  "offset": "990",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/decisions.yaml",
    "offset": "990",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T07:13:04.137337+00:00_

990	  - exp_id: exp028c_selfguide_recipe
991	    role: basis
992	    result: step10_val=0%
993	  depends_on:
994	  - D054
995	  - D053
996	- id: D056
997	  date: 2026-05-17 03:32 UTC
998	  summary: Negative 复盘发现：episode-level + valid_action_bonus 可能安全（exp013f gaming 是
999	    step_independent 特有），加入 h-sweep 批次验证
1000	  rationale: exp013f 证伪了 "dense reward shaping 帮助 GRPO"，但其 gaming 行为（action_is_valid
1001	    97% + task success 0%）是 step_independent 特有的：每步独立优化允许只最大化 per-step bonus。Episode-level
1002	    下模型必须优化 trajectory-level total reward，无法独立 game。当前 exp029 的 action_is_valid=55.9%
1003	    且在下降，加小 bonus 可能提供额外信号打破 23-25% plateau。这是从 negative 推导的假设，有明确的 parent 链。
1004	  related_experiments:
1005	  - exp_id: exp013f
1006	    role: parent_negative
1007	    result: reward gaming under step_independent
1008	  - exp_id: exp029_episode_level
1009	    role: target
1010	    result: plateau at 23-25%, action_is_valid declining
1011	  depends_on:
1012	  - D055
1013	  - D051
1014	- id: D057
1015	  date: 2026-05-17 04:16 UTC
1016	  summary: Early-stop exp029 at step 15 (val=28%, pass@8=92.9%), release GPUs for
1017	    h-sweep (plan_002, paper core figure)
1018	  rationale: 'Step 15 val=28.125% (marginal +3pp over step 5-10), action_is_valid
1019	    degrading (78→55%), action_is_effective dropped to 77%. Continuing has low ROI:
1020	    pass@8=92.9% already proves capability exists, main problem is consistency which
1021	    current config won''t fix. h-sweep (plan_002) is P0 for paper — shows the cliff
1022	    mechanism, directly addresses Dream C1/C2 reviewer concerns. Checkpoint preserved
1023	    for future resume. Plan_003c (bonus variant) included in h-sweep batch.'
1024	  related_experiments:
1025	  - exp_id: exp029_episode_level
1026	    role: early_stopped
1027	    result: step15_val=28.125%_pass@8=92.9%
1028	  - exp_id: exp028c_selfguide_recipe
1029	    role: comparison
1030	    result: step10_val=0%
1031	  depends_on:
1032	  - D056
1033	  - D055
1034	- id: D058
1
…[truncated 839 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T07:13:04.137529+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
  "description": "Create paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
    "description": "Create paper directory"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T07:13:04.137678+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T07:13:04.137842+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, T, O, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $T: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $O: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context window. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(T - kh)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $\\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization, receiving its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\\lceil T/h \\rceil$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context window limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\\ref{sec:experiments}, step-independent training collapses to 0\\% task success within 10 training steps, while action validity remains above 90\\%, indicating the policy degenerates in task strategy rather than action formatting.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nUnder step-independent training, the policy optimized on window $k$ observes only a local $h$-step history. Cross-step strategies that require conditioning on earlier outcomes become invisible to the optimization process. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4. The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism is more subtle and more damaging. Under step-independent training, each window receives a return $R_k = \\gamma^{(T-kh)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution erodes learned strategies: the agent cannot maintain locally correct behaviors if they frequently co-occur with episode failure.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(T-kh)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.99$), the return magnitude is $\\gamma^{48} \\approx 0.62$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful. Magnitude decay slows learning but preserves the correct optimization direction; sign misattribution actively drives the policy away from good behaviors. A gradient with correct sign but attenuated magnitude yields slow convergence. A gradient with wrong sign yields divergence.\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nWith a competent base agent trained via episode-level GRPO, we address the complementary problem of verification efficiency. Interactive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory, meaning the agent does not change its action after checking~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, can reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, T, O, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $T: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $O: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context window. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(T - kh)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $\\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization, receiving its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\\lceil T/h \\rceil$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context window limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\\ref{sec:experiments}, step-independent training collapses to 0\\% task success within 10 training steps, while action validity remains above 90\\%, indicating the policy degenerates in task strategy rather than action formatting.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nUnder step-independent training, the policy optimized on window $k$ observes only a local $h$-step history. Cross-step strategies that require conditioning on earlier outcomes become invisible to the optimization process. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4. The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism is more subtle and more damaging. Under step-independent training, each window receives a return $R_k = \\gamma^{(T-kh)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution erodes learned strategies: the agent cannot maintain locally correct behaviors if they frequently co-occur with episode failure.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(T-kh)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.99$), the return magnitude is $\\gamma^{48} \\approx 0.62$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful. Magnitude decay slows learning but preserves the correct optimization direction; sign misattribution actively drives the policy away from good behaviors. A gradient with correct sign but attenuated magnitude yields slow convergence. A gradient with wrong sign yields divergence.\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nWith a competent base agent trained via episode-level GRPO, we address the complementary problem of verification efficiency. Interactive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory, meaning the agent does not change its action after checking~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, can reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.\n"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T07:13:04.138160+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T07:13:04.138333+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T07:13:04.138464+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T07:13:04.138588+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T07:13:04.138735+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-17T07:13:04.138855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T07:13:04.138975+00:00_

45:We identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\ref{sec:experiments}, step-independent training collapses to 0\% task success within 10 training steps, while action validity remains above 90\%, indicating the policy degenerates in task strategy rather than action formatting.
50:[Omitted long matching line]
52:[Omitted long matching line]
57:The second mechanism is more subtle and more damaging. Under step-independent training, each window receives a return $R_k = \gamma^{(T-kh)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). After group normalization, the advantage $\hat{A}_k$ has a \textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T07:13:04.139097+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", \\w+ing ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", \\w+ing ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-17T07:13:04.139216+00:00_

7:[Omitted long matching line]
9:[Omitted long matching line]
36:where $\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization, receiving its own group-normalized advantage $\hat{A}_k$ via Equation~\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\lceil T/h \rceil$.
38:[Omitted long matching line]
45:We identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\ref{sec:experiments}, step-independent training collapses to 0\% task success within 10 training steps, while action validity remains above 90\%, indicating the policy degenerates in task strategy rather than action formatting.
52:[Omitted long matching line]
59:[Omitted long matching line]
86:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T07:13:04.139343+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "leverage|utilize|facilitate|delve|myriad|plethora",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": "leverage|utilize|facilitate|delve|myriad|plethora",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T07:13:04.139457+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T07:13:04.139571+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally|Notably|It is worth noting",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T07:13:04.139703+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-17T07:13:04.139832+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", \\w+ing (the|that|this|a|an|its|how|what|where)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", \\w+ing (the|that|this|a|an|its|how|what|where)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T07:13:04.139951+00:00_

36:where $\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization, receiving its own group-normalized advantage $\hat{A}_k$ via Equation~\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\lceil T/h \rceil$.
45:We identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\ref{sec:experiments}, step-independent training collapses to 0\% task success within 10 training steps, while action validity remains above 90\%, indicating the policy degenerates in task strategy rather than action formatting.
52:[Omitted long matching line]
86:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T07:13:04.140070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "offset": "44",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "offset": "44",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-17T07:13:04.140187+00:00_

44	
45	We identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\ref{sec:experiments}, step-independent training collapses to 0\% task success within 10 training steps, while action validity remains above 90\%, indicating the policy degenerates in task strategy rather than action formatting.
46	
47	\subsubsection{Mechanism 1: Policy Information Loss}
48	\label{sec:m1_information_loss}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T07:13:04.140308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "offset": "84",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "offset": "84",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T07:13:04.140431+00:00_

84	\label{sec:selective_verification}
85	
86	With a competent base agent trained via episode-level GRPO, we address the complementary problem of verification efficiency. Interactive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\% of verification instances are confirmatory, meaning the agent does not change its action after checking~\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, can reduce computational cost without sacrificing task performance.
87	
88	We formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \in \{\texttt{VERIFY}, \texttt{SKIP}\}$ before generating its action $a_t$. When $v_t = \texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-17T07:13:04.140569+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "while action validity remains above 90\\%, indicating the policy degenerates in task strategy rather than action formatting.",
  "new_string": "while action validity remains above 90\\%. This pattern indicates that the policy degenerates in task strategy rather than action formatting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "old_string": "while action validity remains above 90\\%, indicating the policy degenerates in task strategy rather than action formatting.",
    "new_string": "while action validity remains above 90\\%. This pattern indicates that the policy degenerates in task strategy rather than action formatting."
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-17T07:13:04.140756+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-17T07:13:04.140884+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "but empirical analysis shows that over 90\\% of verification instances are confirmatory, meaning the agent does not change its action after checking~\\cite{long2026selfverification}.",
  "new_string": "but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "old_string": "but empirical analysis shows that over 90\\% of verification instances are confirmatory, meaning the agent does not change its action after checking~\\cite{long2026selfverification}.",
    "new_string": "but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}."
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-17T07:13:04.141051+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-17T07:13:04.141187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "offset": "35",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "offset": "35",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-17T07:13:04.141312+00:00_

35	\end{equation}
36	where $\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization, receiving its own group-normalized advantage $\hat{A}_k$ via Equation~\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\lceil T/h \rceil$.
37	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-17T07:13:04.141437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "offset": "51",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "offset": "51",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-17T07:13:04.141560+00:00_

51	
52	More formally, let $\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\pi^*$ and the full history, $I(\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\pi^*; h_{\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\pi^*; h_T) \gg I(\pi^*; h_{\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-17T07:13:04.141717+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "where $\\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization, receiving its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\\lceil T/h \\rceil$.",
  "new_string": "where $\\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\\lceil T/h \\rceil$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "old_string": "where $\\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization, receiving its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\\lceil T/h \\rceil$.",
    "new_string": "where $\\gamma$ is a discount factor (typically 0.99). Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $\\lceil T/h \\rceil$."
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-17T07:13:04.141891+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-17T07:13:04.142028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-17T07:13:04.142364+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem_formulation}
6	
7	We formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{O}, T, O, R, \gamma)$, where $\mathcal{S}$ is the state space of the environment, $\mathcal{A}$ is the action space (natural language commands), $\mathcal{O}$ is the observation space (textual feedback from the environment), $T: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}$ is the transition function, $O: \mathcal{S} \rightarrow \mathcal{O}$ is the observation function, $R$ is the reward function, and $\gamma \in [0,1]$ is a discount factor. The agent policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \ldots, o_t)$, where $\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \in \{0, r_+\}$ that indicates task success or failure.
8	
9	In practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context window. This motivates the \textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.
10	
11	\subsection{GRPO for Language Agents}
12	\label{sec:grpo}
13	
14	Gr
…[truncated 11822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-17T07:13:04.142535+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "description": "Count words in method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "description": "Count words in method.tex"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-17T07:13:04.142681+00:00_

1741 /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-17T07:13:04.142818+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "--",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "tool_args": {
    "pattern": "--",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-17T07:13:04.142939+00:00_

50:[Omitted long matching line]
75:This design directly addresses Mechanism 1. The policy $\pi_\phi(a_t \mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260517T070859",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 97 · 2026-05-17T07:13:04.143109+00:00_

Both are number ranges (steps 3--4) which are valid LaTeX en-dash usage for ranges.

Method section written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex`.

Structure:
- **3.1** Problem Formulation: POMDP, step-independent windowing definition
- **3.2** GRPO: bandit-style formulation, no inherent γ
- **3.3** Step-Independent Implementation: RAGEN's γ-discounted per-window returns, practical motivations
- **3.4** Dual Mechanism Analysis: M1 (policy information loss) + M2 (advantage sign misattribution with γ decay as secondary)
- **3.5** Episode-Level Training: resolves both mechanisms, trade-off analysis, connection to GRPO's original design
- **3.6** Selective Verification: placeholder with action-change formulation, defers to Section 5

All style checks pass: no em-dash/en-dash violations, no banned words, no trailing -ing phrases, no consecutive transition words. Notation consistent with spec ($T$, $h$, $\gamma$, $\hat{A}_k$, $R_k$, $K$, $\pi_\phi$). Experiment data referenced briefly for motivation without tables or detailed numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260517T070859"
}
```

</details>

---
