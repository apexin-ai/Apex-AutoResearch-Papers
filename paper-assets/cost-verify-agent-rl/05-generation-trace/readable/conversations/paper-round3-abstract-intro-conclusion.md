# paper round3 abstract intro conclusion

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_paper_round3_abstract_intro_conclusion_20260523T164649.jsonl`
- **Structured JSON:** [`2af4204edac77f6c9617.json`](../../sessions/2a/2af4204edac77f6c9617.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-23T16:49:37.085562+00:00_

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
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T16:49:37.086144+00:00_

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
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T16:49:37.086331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T16:49:37.086490+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{amsthm}
15	\usepackage{enumitem}
16	
17	\title{Sign Misattribution in Step-Independent Agent RL:\\Dual Mechanism Diagnosis and Episode-Level Correction}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Reinforcement learning for multi-turn LLM agents requires credit assignment across long interaction trajectories. The dominant training paradigm decomposes these trajectories into fixed-size windows optimized independently via Group Relative Policy Optimization (GRPO), yet this ubiquitous design choice has received little scrutiny. We identify a structural credit assignment pathology driven by two distinct mechanisms: \textit{policy information loss}, which truncates cross-window context and imposes a constant performance ceiling, and \textit{advantage sign misattribution}, which causes the majority of gradient updates for locally correct actions to carry incorrect sign. A factorial experiment isolates each mechanism: removing sign misattribution converts catastrophic collapse into bounded learning; removing information loss enables out-of-distribution (OOD) generalization. Direct sign measurement confirms the theoretical prediction, with credit agreement dropping to near-random levels. Episode-level GRPO, which treats the full trajectory as a single optimization sample, eliminates both failure modes. However, a systematic multi-seed evaluation reveals that avoiding collapse is necessary but not sufficient: 73\% of seeds stabilize, yet only 36\% achieve statistically significant OOD transfer. Cross-scale verification at 8B parameters and cross-environment validation on ScienceWorld provide preliminary evidence that the patholog
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T16:49:37.086659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T16:49:37.086850+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Reinforcement learning from sparse terminal reward has emerged as a promising paradigm for training LLM agents on multi-turn interactive tasks spanning 30--50 interaction steps~\cite{kim2025reflact,digiRL2024,wang2022scienceworld}. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, with its critic-free design, has become the algorithm of choice. Yet a gap persists between the promise of RL-driven agent improvement and the reality of training outcomes: recent agent RL systems~\cite{ragen2025,selfguide2026,spear2025,feng2025gigpo} share a common, unscrutinized implementation pattern (decomposing trajectories into fixed-size windows, each optimized independently) and frequently report training instability without diagnosing its root cause.
5	
6	We show this \textit{step-independent} default introduces a fundamental credit assignment pathology. Step-independent training partitions trajectories into non-overlapping $h$-step windows, each optimized via GRPO. This produces a two-phase collapse: task success drops to 0\% while action validity initially remains high, then continued training destroys even basic formatting. Standard remedies (dense reward shaping, discount tuning) fail. Concurrent methods that improve per-step credit quality (GiGPO~\cite{feng2025gigpo}, GAGPO~\cite{gagpo2026}, Turn-PPO~\cite{turnppo2026}, HCAPO~\cite{hcapo2026}) address the symptom through improved credit assignment mechanisms, validating that sign correctness is the critical factor. Our contribution is orthogonal: we formally diagnose \textit{why} the default windowing fails.
7	
8	We trace the collapse to two mechanisms at different layers. \textit{\textbf{Policy information loss}} (M1) operates at the inference layer: each window lacks access to earlier observations, imposing a constant performance ceiling. \textit{\textbf{Advantage sign misattribution}} (M2) operates at the training layer: under binary reward, the 
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T16:49:37.087024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T16:49:37.087155+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Step-independent training fails through two mechanisms: information loss imposes a constant performance ceiling while sign misattribution causes cumulative degradation, with the majority of gradient updates carrying incorrect sign. Episode-level GRPO addresses both failure modes, achieving substantial OOD improvement at both 1.7B and 8B scales, though only a minority of seeds achieve statistically significant generalization. Sign errors are more destructive than magnitude imprecision; this finding applies to any agent RL method combining step-level windowing, sparse binary reward, and group-relative normalization.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T16:49:37.087350+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
  "old_string": "which causes the majority of gradient updates for locally correct actions to carry incorrect sign",
  "new_string": "which causes a substantial fraction of gradient updates for locally correct actions to carry incorrect sign"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
    "old_string": "which causes the majority of gradient updates for locally correct actions to carry incorrect sign",
    "new_string": "which causes a substantial fraction of gradient updates for locally correct actions to carry incorrect sign"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T16:49:37.087514+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T16:49:37.087676+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
  "old_string": "eliminates both failure modes",
  "new_string": "addresses both failure modes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
    "old_string": "eliminates both failure modes",
    "new_string": "addresses both failure modes"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T16:49:37.087825+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T16:49:37.087965+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "old_string": "Our theoretical analysis shows that the majority of gradient updates for locally correct actions carry incorrect sign",
  "new_string": "Our theoretical analysis shows that a substantial fraction of gradient updates for locally correct actions carry incorrect sign"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "old_string": "Our theoretical analysis shows that the majority of gradient updates for locally correct actions carry incorrect sign",
    "new_string": "Our theoretical analysis shows that a substantial fraction of gradient updates for locally correct actions carry incorrect sign"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T16:49:37.088116+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T16:49:37.088242+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "old_string": "with effects persisting at 8B scale",
  "new_string": "with preliminary evidence of persistence at 8B scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "old_string": "with effects persisting at 8B scale",
    "new_string": "with preliminary evidence of persistence at 8B scale"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T16:49:37.088380+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T16:49:37.088514+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "old_string": "\\item \\textbf{Empirical separation.} A factorial experiment isolates each mechanism, direct sign measurement confirms the theoretical prediction at near-random levels, and preliminary cross-scale (8B) and cross-environment (ScienceWorld) evidence supports generality of the pathology.\n\\item \\textbf{Episode-level fix: necessary but not sufficient.} GRPO's original episode-level design addresses both mechanisms, but a systematic multi-seed evaluation reveals that most seeds avoid collapse while only a minority achieve statistically significant OOD generalization. We analyze this seed-dependent transfer gap.",
  "new_string": "\\item \\textbf{Empirical validation.} We validate this diagnosis through a factorial experiment that isolates each mechanism, direct sign measurement confirms the theoretical prediction at near-random levels, and preliminary cross-scale (8B) and cross-environment (ScienceWorld) evidence supports generality. Episode-level training (reverting to GRPO's original design) addresses both mechanisms, but a systematic 11-seed evaluation reveals seed-dependent generalization: 73\\% of seeds avoid collapse while only 36\\% achieve statistically significant OOD improvement."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "old_string": "\\item \\textbf{Empirical separation.} A factorial experiment isolates each mechanism, direct sign measurement confirms the theoretical prediction at near-random levels, and preliminary cross-scale (8B) and cross-environment (ScienceWorld) evidence supports generality of the pathology.\n\\item \\textbf{Episode-level fix: necessary but not sufficient.} GRPO's original episode-level design addresses both mechanisms, but a systematic multi-seed evaluation reveals that most seeds avoid collapse while only a minority achieve statistically significant OOD generalization. We analyze this seed-dependent transfer gap.",
    "new_string": "\\item \\textbf{Empirical validation.} We validate this diagnosis through a factorial experiment that isolates each mechanism, direct sign measurement confirms the theoretical prediction at near-random levels, and preliminary cross-scale (8B) and cross-environment (ScienceWorld) evidence supports generality. Episode-level training (reverting to GRPO's original design) addresses both mechanisms, but a systematic 11-seed evaluation reveals seed-dependent generalization: 73\\% of seeds avoid collapse while only 36\\% achieve statistically significant OOD improvement."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T16:49:37.088686+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T16:49:37.088820+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex",
  "old_string": "with the majority of gradient updates carrying incorrect sign",
  "new_string": "with a substantial fraction of gradient updates carrying incorrect sign"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex",
    "old_string": "with the majority of gradient updates carrying incorrect sign",
    "new_string": "with a substantial fraction of gradient updates carrying incorrect sign"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T16:49:37.088946+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T16:49:37.089070+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex",
  "old_string": "achieving substantial OOD improvement at both 1.7B and 8B scales",
  "new_string": "achieving substantial OOD improvement at 1.7B scale, with preliminary single-seed evidence at 8B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex",
    "old_string": "achieving substantial OOD improvement at both 1.7B and 8B scales",
    "new_string": "achieving substantial OOD improvement at 1.7B scale, with preliminary single-seed evidence at 8B"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T16:49:37.089197+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T16:49:37.089325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
  "offset": "23",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex",
    "offset": "23",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T16:49:37.089447+00:00_

23	
24	\begin{abstract}
25	Reinforcement learning for multi-turn LLM agents requires credit assignment across long interaction trajectories. The dominant training paradigm decomposes these trajectories into fixed-size windows optimized independently via Group Relative Policy Optimization (GRPO), yet this ubiquitous design choice has received little scrutiny. We identify a structural credit assignment pathology driven by two distinct mechanisms: \textit{policy information loss}, which truncates cross-window context and imposes a constant performance ceiling, and \textit{advantage sign misattribution}, which causes a substantial fraction of gradient updates for locally correct actions to carry incorrect sign. A factorial experiment isolates each mechanism: removing sign misattribution converts catastrophic collapse into bounded learning; removing information loss enables out-of-distribution (OOD) generalization. Direct sign measurement confirms the theoretical prediction, with credit agreement dropping to near-random levels. Episode-level GRPO, which treats the full trajectory as a single optimization sample, addresses both failure modes. However, a systematic multi-seed evaluation reveals that avoiding collapse is necessary but not sufficient: 73\% of seeds stabilize, yet only 36\% achieve statistically significant OOD transfer. Cross-scale verification at 8B parameters and cross-environment validation on ScienceWorld provide preliminary evidence that the pathology extends beyond our primary setting.
26	\end{abstract}
27	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T16:49:37.089588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T16:49:37.089733+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Reinforcement learning from sparse terminal reward has emerged as a promising paradigm for training LLM agents on multi-turn interactive tasks spanning 30--50 interaction steps~\cite{kim2025reflact,digiRL2024,wang2022scienceworld}. Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath}, with its critic-free design, has become the algorithm of choice. Yet a gap persists between the promise of RL-driven agent improvement and the reality of training outcomes: recent agent RL systems~\cite{ragen2025,selfguide2026,spear2025,feng2025gigpo} share a common, unscrutinized implementation pattern (decomposing trajectories into fixed-size windows, each optimized independently) and frequently report training instability without diagnosing its root cause.
5	
6	We show this \textit{step-independent} default introduces a fundamental credit assignment pathology. Step-independent training partitions trajectories into non-overlapping $h$-step windows, each optimized via GRPO. This produces a two-phase collapse: task success drops to 0\% while action validity initially remains high, then continued training destroys even basic formatting. Standard remedies (dense reward shaping, discount tuning) fail. Concurrent methods that improve per-step credit quality (GiGPO~\cite{feng2025gigpo}, GAGPO~\cite{gagpo2026}, Turn-PPO~\cite{turnppo2026}, HCAPO~\cite{hcapo2026}) address the symptom through improved credit assignment mechanisms, validating that sign correctness is the critical factor. Our contribution is orthogonal: we formally diagnose \textit{why} the default windowing fails.
7	
8	We trace the collapse to two mechanisms at different layers. \textit{\textbf{Policy information loss}} (M1) operates at the inference layer: each window lacks access to earlier observations, imposing a constant performance ceiling. \textit{\textbf{Advantage sign misattribution}} (M2) operates at the training layer: under binary reward, the 
…[truncated 1860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T16:49:37.089876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T16:49:37.089997+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Step-independent training fails through two mechanisms: information loss imposes a constant performance ceiling while sign misattribution causes cumulative degradation, with a substantial fraction of gradient updates carrying incorrect sign. Episode-level GRPO addresses both failure modes, achieving substantial OOD improvement at 1.7B scale, with preliminary single-seed evidence at 8B, though only a minority of seeds achieve statistically significant generalization. Sign errors are more destructive than magnitude imprecision; this finding applies to any agent RL method combining step-level windowing, sparse binary reward, and group-relative normalization.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T16:49:37.090148+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eliminates",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eliminates",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T16:49:37.090268+00:00_

docs/paper/experiments.tex:20:Cell~B eliminates sign misattribution while retaining information loss: training success improves, but OOD generalization is bounded by the information-loss ceiling. Both seeds converge to the same OOD ceiling despite different training trajectories, confirming the bottleneck is architectural rather than statistical.% exp_id: factorial_h2_episodeadv_seed1, factorial_h2_episodeadv_seed2
docs/paper/introduction.tex:8:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T16:49:37.090384+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sed -n '/\\\\begin{abstract}/,/\\\\end{abstract}/p' /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex | sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g' | sed 's/[{}~]//g' | wc -w",
  "description": "Count abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Bash",
  "tool_args": {
    "command": "sed -n '/\\\\begin{abstract}/,/\\\\end{abstract}/p' /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/main.tex | sed 's/\\\\begin{abstract}//' | sed 's/\\\\end{abstract}//' | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g' | sed 's/[{}~]//g' | wc -w",
    "description": "Count abstract word count"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T16:49:37.090503+00:00_

180

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T16:49:37.090635+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eliminates",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eliminates",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T16:49:37.090751+00:00_

8:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T16:49:37.090860+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eliminates both mechanisms",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eliminates both mechanisms",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T16:49:37.090969+00:00_

8:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T16:49:37.091076+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -o 'eliminates[^.]*' /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "description": "Extract exact \"eliminates\" context from introduction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -o 'eliminates[^.]*' /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "description": "Extract exact \"eliminates\" context from introduction"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T16:49:37.091186+00:00_

eliminates both mechanisms by treating the full trajectory as a single optimization sample, achieving substantial OOD improvement where step-independent collapses to 0\%, with preliminary evidence of persistence at 8B scale

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T16:49:37.091364+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
  "old_string": "eliminates both mechanisms by treating",
  "new_string": "addresses both mechanisms by treating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
    "old_string": "eliminates both mechanisms by treating",
    "new_string": "addresses both mechanisms by treating"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T16:49:37.091525+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T16:49:37.091677+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "majority",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "tool_args": {
    "pattern": "majority",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T16:49:37.091800+00:00_

docs/paper/theoretical_analysis.tex:27:\caption{Upper bound on the probability of correct gradient sign as a function of episode success rate $p$ (Proposition~2). At typical agent task success rates ($p < 0.2$, shaded), the majority of gradient updates carry incorrect sign regardless of group size $K$. At ALFWorld's baseline ($p{=}12.5\%$, $K{=}8$), at most 19.1\% of updates are correct. The dashed diagonal shows the large-$K$ limit $P_{\text{correct}} \to p$.}
docs/paper/experiments.tex:9:[Omitted long matching line]
docs/paper/main.aux:327:[Omitted long matching line]
docs/paper/main.aux:328:\newlabel{fig:theory_curve}{{2}{4}{Probability of correct gradient sign as a function of episode success rate $p$ (Proposition~2). At typical agent task success rates ($p < 0.2$, shaded), the majority of gradient updates carry incorrect sign regardless of group size $K$. At ALFWorld's baseline ($p{=}12.5\%$, $K{=}8$), only 19.1\% of updates are correct. The dashed diagonal shows the large-$K$ limit $P_{\text {correct}} \to p$}{figure.caption.2}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T16:49:37.091926+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "eliminates",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "tool_args": {
    "pattern": "eliminates",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T16:49:37.092041+00:00_

docs/paper/experiments.tex:20:Cell~B eliminates sign misattribution while retaining information loss: training success improves, but OOD generalization is bounded by the information-loss ceiling. Both seeds converge to the same OOD ceiling despite different training trajectories, confirming the bottleneck is architectural rather than statistical.% exp_id: factorial_h2_episodeadv_seed1, factorial_h2_episodeadv_seed2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T16:49:37.092194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
  "offset": "5",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/experiments.tex",
    "offset": "5",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T16:49:37.092321+00:00_

5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	We evaluate on ALFWorld~\cite{shridhar2021alfworld}, a text-based household environment with six task types requiring sequential reasoning over up to 50 steps. Reward is binary: $R \in \{0, r_+\}$. The base policy is Qwen3-1.7B fine-tuned on expert demonstrations (SFT baseline: 12.5\% in-distribution). At this baseline success rate, Proposition~2 predicts the majority of gradient updates carry incorrect sign. All conditions use RAGEN~\cite{ragen2025} (v0.1, commit \texttt{3a6b48b})\footnote{Our implementation extends RAGEN v0.1 with episode-level training support. Code: \url{https://github.com/RAGEN-AI/RAGEN}.} with GRPO~\cite{shao2024deepseekmath} ($K{=}8$; full hyperparameters in Appendix~\ref{app:hyperparameters}). We report success rate on a 134-task OOD set (primary) and 32-task in-distribution set (secondary). Seed counts are noted per condition.
10	
11	\subsection{Factorial Mechanism Separation}
12	\label{sec:factorial_experiments}
13	
14	We implement the factorial design from Section~\ref{sec:factorial_design} with two seeds per condition. Cell~C (full observation, step-level advantage) would isolate M2 without M1, but we encountered persistent training instability in this configuration (Appendix~\ref{app:cell_c}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T16:49:37.092489+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "8B",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "tool_args": {
    "pattern": "8B",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T16:49:37.092646+00:00_

docs/paper/experiments.tex:117:A single-seed experiment on Qwen3-8B provides preliminary evidence that both failure and fix persist at scale. Cell~A collapses within two steps; Cell~D reaches 90.3\% OOD, substantially exceeding the SFT baseline (full results in Appendix~\ref{app:8b_results}). Restricting context to $h{=}2$ produces a large M1 gap, confirming that information loss remains severe at scale. Single-seed due to memory constraints.% exp_id: 8b_cell_c_episode_v9d, 8b_v9d_ood_eval_v5
docs/paper/experiments.tex:118:Step-independent training also collapses on ScienceWorld~\cite{wang2022scienceworld}: Cell~A drops to 0\% throughout all 15 steps. Restricting context to $h{=}2$ produces a comparable M1 gap to the 8B ALFWorld setting, suggesting the pathology is environment-general.% exp_id: scienceworld_grpo_cell_a, sw_info_loss_bjb1
docs/paper/main.tex:25:[Omitted long matching line]
docs/paper/main.tex:38:[Omitted long matching line]
docs/paper/conclusion.tex:4:[Omitted long matching line]
docs/paper/appendix.tex:86:All 1.7B experiments were conducted on a single NVIDIA A100 80\,GB GPU. Each training run (15 steps, $K{=}8$ rollouts per task, 16 tasks per step) required approximately 6--8 GPU-hours. The 11-seed evaluation totaled ${\sim}$80 GPU-hours. The 8B experiment used 4$\times$ A100 80\,GB with Fully Sharded Data Parallel (FSDP), requiring ${\sim}$24 GPU-hours per run. ScienceWorld experiments used the same single-GPU setup as the 1.7B ALFWorld runs.
docs/paper/appendix.tex:96:\caption{(a)~Cross-scale verification (single seed): both collapse (Cell~A) and fix (Cell~D) are observed from 1.7B to 8B. The episode-level fix appears more effective at 8B (96.9\% vs.\ 34.4\% in-distribution). (b)~Information loss (M1) quantification (single seed each): restricting context to $h{=}2$ drops SFT performance by 37.5pp at 8B ALFWorld and 30.3pp on ScienceWorld.}
docs/paper/appendix.tex:102:\caption{8B results on ALFWorld. SFT and $h{=}2$ use decoding temperature $\tau
…[truncated 210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-23T16:49:37.092864+00:00_

All 8B mentions are properly qualified with "preliminary," "single-seed," or both.

### 验证结果

| 检查项 | 状态 |
|--------|------|
| Abstract word count | 180 words (≤ 200) |
| Introduction \item count | 2 (Dual mechanism diagnosis + Empirical validation) |
| "majority" → "substantial fraction" | Abstract ✓, Introduction ✓, Conclusion ✓ (experiments/theory 中的 "majority" 引用 Proposition 2 的数学结论 80.9% incorrect，保留正确) |
| 8B + "preliminary" | Abstract ✓, Introduction (line 8 + contribution) ✓, Conclusion ✓ |
| "eliminates" → "addresses" | Abstract ✓, Introduction ✓, Conclusion ✓ (experiments.tex "Cell B eliminates" 描述实验设计，保留) |
| Conclusion scope narrowing | 已包含 "combining step-level windowing, sparse binary reward, and group-relative normalization" |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_round3_abstract_intro_conclusion_20260523T164649"
}
```

</details>

---
