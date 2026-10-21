# paper writing conclusion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_writing_conclusion_20260517T192902.jsonl`
- **Structured JSON:** [`863217471f1da6ab7c65.json`](../../sessions/86/863217471f1da6ab7c65.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-17T19:31:11.315189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T19:31:11.315537+00:00_

1	\begin{abstract}
2	Neuro-symbolic methods propose extracting first-order logic (FOL) constraints from Large Language Model (LLM) reasoning traces to improve answer aggregation beyond majority voting. Whether the reasoning model itself can produce useful constraints through self-extraction has not been systematically evaluated. If self-extraction works, it eliminates the need for trained verifiers, external provers, or domain-specific infrastructure. We evaluate Symbolic Invariant Consensus Aggregation (SICA), which formulates a weighted partial Maximum Satisfiability (MAX-SAT) problem over self-extracted FOL constraints, across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. We include an oracle control that replaces self-extraction with gold FOL annotations verified by Z3 to isolate extraction quality from aggregation effectiveness. Self-extracted SICA provides no statistically significant improvement over Self-Consistency (SC) in any tested condition. The oracle variant achieves $+8.82$ percentage points over SC ($p < 0.001$), which proves the aggregation mechanism is sound when supplied with high-quality constraints. We identify this failure as a \emph{capability trap}: because the same model that produced potentially flawed reasoning also extracts the constraints, those constraints are semantically coupled to their source answers and carry no independent discriminative signal. Only 11.5\% of self-extracted constraints evaluate differently across candidate answers. This result establishes that same-model constraint extraction cannot improve LLM answer aggregation without independent sources of formal knowledge.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T19:31:11.315719+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T19:31:11.315910+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Neuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \citep{xu2026dylos}, apply logic-complete decomposition \citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \citep{wang2025fover}, or employ multi-perspective grounding \citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.
4	
5	These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.
6	

…[truncated 3946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T19:31:11.316090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T19:31:11.316239+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The oracle experiment (Table~\ref{tab:main_results}, bottom) constitutes a causal intervention that isolates the source of failure. By replacing only the constraint source while holding all other pipeline components fixed, we establish that aggregation is not the bottleneck: the $+8.82$\,pp improvement ($p < 0.001$) pinpoints same-model self-extraction as the single point of failure. This oracle design follows established methodology where component-level interventions isolate error sources \citep{press2023compositionality, trivedi2023ircot, saparov2023greedy}.
5	
6	Manual analysis of constraint quality explains the mechanism. Across 43 pilot problems (23 with multiple candidates), only 11.5\% of unique constraints evaluated differently across candidates. The remainder encoded shared domain facts (predicate definitions, background implications, intermediate steps) satisfied equally by every candidate. In only 4 of 23 multi-answer problems (17.4\%) did discriminative constraints favor a non-majority answer, accounting for the 803/804 agreement between MAX-SAT and count-only (Table~\ref{tab:ablation}).
7	
8	The computational cost is substantial: constraint extraction accounts for 48.7\% of total SICA pipeline time, roughly doubling wall-clock cost compared to SC alone. Among 31 disagreements with SC, wins and losses approximately cancel (16 vs.\ 14), yielding zero net accuracy gain.
9	
10	The $+8.82$\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three concrete paths can unlock it. First, trained FOL extractors supervised on datasets with gold annotations (such as FOLIO) can learn extraction patterns that exceed same-model capabilities; FoVer \citep{wang2025fover} demonstrates this approach with a dedicated verifier. Second, external provers that verify constraints independently of the reasoning model eliminate the circular dependency between generation and verification. Third, cross-
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T19:31:11.316380+00:00_

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
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T19:31:11.316716+00:00_

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
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T19:31:11.316920+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We term this the \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal.\n\nThe practical consequences are clear. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers, and MAX-SAT agrees with count-only aggregation on 803 of 804 predictions. Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected benefit. The multi-candidate rate $C_0$ serves as a zero-cost diagnostic: practitioners can compute it from trace samples alone, before committing resources to extraction. These findings establish that same-model constraint extraction cannot improve LLM answer aggregation without independent sources of formal knowledge.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck identified by our analysis and leaves the aggregation mechanism intact.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We term this the \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal.\n\nThe practical consequences are clear. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers, and MAX-SAT agrees with count-only aggregation on 803 of 804 predictions. Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected benefit. The multi-candidate rate $C_0$ serves as a zero-cost diagnostic: practitioners can compute it from trace samples alone, before committing resources to extraction. These findings establish that same-model constraint extraction cannot improve LLM answer aggregation without independent sources of formal knowledge.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck identified by our analysis and leaves the aggregation mechanism intact.\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T19:31:11.317079+00:00_

&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T19:31:11.317201+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex 2>&1 || echo \"FILE_NOT_EXISTS\"",
  "description": "Check if conclusion.tex exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex 2>&1 || echo \"FILE_NOT_EXISTS\"",
    "description": "Check if conclusion.tex exists"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T19:31:11.317317+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T19:31:11.317430+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T19:31:11.317550+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	This work presents a systematic evaluation of symbolic constraint aggregation for LLM majority voting across five models, three reasoning domains, and more than 1,300 instances. The central finding is negative: when an LLM extracts first-order logic constraints from its own reasoning traces and a MAX-SAT solver aggregates them, accuracy does not improve over standard majority voting. The gap ranges from $-3.3$ to $+3.3$ percentage points, with no condition reaching statistical significance. We trace this failure to a capability trap: self-extracted constraints are semantically coupled to the answers they accompany and carry no independent discriminative signal. The MAX-SAT solver agrees with simple constraint counting on 803 of 804 instances, which confirms that satisfiability structure adds nothing when constraints are redundant with votes.
5	
6	An oracle control experiment isolates constraint quality as the sole bottleneck. Replacing self-extracted constraints with gold FOL annotations yields $+8.82$ percentage points over majority voting ($p < 0.001$), while all other pipeline components remain fixed. The aggregation mechanism is sound; the problem lies entirely in same-model self-extraction. This result quantifies an $8.82$-point gap that remains recoverable through higher-quality constraint sources.
7	
8	For practitioners, we identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: when $C_0$ falls below 5\%, constraint-based methods cannot improve over majority voting regardless of constraint quality, and investment in extraction is unwarranted. For the field, our results suggest that productive directions include trained FOL extractors, external theorem provers, and cross-model constraint extraction, all of which break the circular dependency between generation and verification that defines the capability trap.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T19:31:11.317702+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We term this the \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal.\n\nThe practical consequences are clear. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers, and MAX-SAT agrees with count-only aggregation on 803 of 804 predictions. Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected benefit. The multi-candidate rate $C_0$ serves as a zero-cost diagnostic: practitioners can compute it from trace samples alone, before committing resources to extraction. These findings establish that same-model constraint extraction cannot improve LLM answer aggregation without independent sources of formal knowledge.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck identified by our analysis and leaves the aggregation mechanism intact.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We term this the \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal.\n\nThe practical consequences are clear. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers, and MAX-SAT agrees with count-only aggregation on 803 of 804 predictions. Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected benefit. The multi-candidate rate $C_0$ serves as a zero-cost diagnostic: practitioners can compute it from trace samples alone, before committing resources to extraction. These findings establish that same-model constraint extraction cannot improve LLM answer aggregation without independent sources of formal knowledge.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck identified by our analysis and leaves the aggregation mechanism intact.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T19:31:11.317854+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T19:31:11.318015+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && grep -n \"—\\|–\" conclusion.tex; echo \"---\"; grep -c \"ing,\" conclusion.tex; echo \"---\"; wc -w conclusion.tex",
  "description": "Check for dashes, -ing patterns, and word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && grep -n \"—\\|–\" conclusion.tex; echo \"---\"; grep -c \"ing,\" conclusion.tex; echo \"---\"; wc -w conclusion.tex",
    "description": "Check for dashes, -ing patterns, and word count"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T19:31:11.318140+00:00_

---
0
---
269 conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T19:31:11.318274+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "detex conclusion.tex 2>/dev/null | wc -w || sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$]//g' conclusion.tex | wc -w",
  "description": "Count words excluding LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "tool_args": {
    "command": "detex conclusion.tex 2>/dev/null | wc -w || sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$]//g' conclusion.tex | wc -w",
    "description": "Count words excluding LaTeX commands"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T19:31:11.318390+00:00_

265

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T19:31:11.318517+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition, with accuracy gaps ranging from $-3.3$ to $+3.3$\\,pp. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We identify this as a \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal. The failure is not one of aggregation design but of the circular dependency between generation and verification within a single model.\n\nThe practical consequences are substantial. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected accuracy benefit. For practitioners considering constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constraint quality audit before full deployment.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential and points to three concrete paths forward. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop that produces non-discriminative constraints. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck directly; the aggregation mechanism requires no modification.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition, with accuracy gaps ranging from $-3.3$ to $+3.3$\\,pp. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We identify this as a \\emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal. The failure is not one of aggregation design but of the circular dependency between generation and verification within a single model.\n\nThe practical consequences are substantial. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected accuracy benefit. For practitioners considering constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constraint quality audit before full deployment.\n\nThe $+8.82$\\,pp oracle gap quantifies recoverable potential and points to three concrete paths forward. Trained FOL extractors supervised on gold annotations (such as FOLIO) can learn extraction patterns beyond same-model capabilities. Cross-model extraction, where a separate model formalizes another model's traces, breaks the self-reference loop that produces non-discriminative constraints. External provers that verify constraints independently of the reasoning model eliminate the circular dependency entirely. Each path targets the extraction bottleneck directly; the aggregation mechanism requires no modification.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T19:31:11.318678+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T19:31:11.318803+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -cn \"—\\|–\" conclusion.tex && echo \"---\" && grep -n \"ing,\" conclusion.tex && echo \"---\" && wc -w conclusion.tex",
  "description": "Final check: dashes, -ing phrases, word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -cn \"—\\|–\" conclusion.tex && echo \"---\" && grep -n \"ing,\" conclusion.tex && echo \"---\" && wc -w conclusion.tex",
    "description": "Final check: dashes, -ing phrases, word count"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T19:31:11.318948+00:00_

Exit code 1
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T19:31:11.319091+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" conclusion.tex; grep -n \"–\" conclusion.tex; echo \"=== ing comma ===\"; grep -n \"ing,\" conclusion.tex; echo \"=== word count ===\"; wc -w conclusion.tex",
  "description": "Final validation of conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" conclusion.tex; grep -n \"–\" conclusion.tex; echo \"=== ing comma ===\"; grep -n \"ing,\" conclusion.tex; echo \"=== word count ===\"; wc -w conclusion.tex",
    "description": "Final validation of conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T19:31:11.319244+00:00_

=== ing comma ===
5:The practical consequences are substantial. Only 11.5\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\% of total pipeline time, roughly doubling computational cost for zero expected accuracy benefit. For practitioners considering constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constraint quality audit before full deployment.
=== word count ===
344 conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T19:31:11.319385+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "old_string": "For practitioners considering constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic",
  "new_string": "For practitioners who evaluate constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "old_string": "For practitioners considering constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic",
    "new_string": "For practitioners who evaluate constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T19:31:11.319525+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T19:31:11.319640+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "description": "Re-check -ing comma patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "description": "Re-check -ing comma patterns"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T19:31:11.319756+00:00_

5:The practical consequences are substantial. Only 11.5\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\% of total pipeline time, roughly doubling computational cost for zero expected accuracy benefit. For practitioners who evaluate constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constraint quality audit before full deployment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T19:31:11.319939+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "old_string": "Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected accuracy benefit.",
  "new_string": "Constraint extraction accounts for 48.7\\% of total pipeline time and roughly doubles computational cost for zero expected accuracy benefit."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "old_string": "Constraint extraction accounts for 48.7\\% of total pipeline time, roughly doubling computational cost for zero expected accuracy benefit.",
    "new_string": "Constraint extraction accounts for 48.7\\% of total pipeline time and roughly doubles computational cost for zero expected accuracy benefit."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T19:31:11.320089+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T19:31:11.320205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T19:31:11.320332+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluated Symbolic Invariant Consensus Aggregation across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. Self-extracted SICA provides no statistically significant improvement over Self-Consistency in any tested condition, with accuracy gaps ranging from $-3.3$ to $+3.3$\,pp. The oracle experiment, which replaces self-extraction with gold FOL annotations verified by Z3, achieves $+8.82$ percentage points over SC ($p < 0.001$). This result causally localizes the failure to extraction quality: the MAX-SAT aggregation mechanism is sound when supplied with high-quality constraints, but same-model self-extraction cannot produce them. We identify this as a \emph{capability trap}: because the reasoning model also extracts the constraints, those constraints inherit the same biases that produced potentially flawed answers and carry no independent discriminative signal. The failure is not one of aggregation design but of the circular dependency between generation and verification within a single model.
4	
5	The practical consequences are substantial. Only 11.5\% of self-extracted constraints evaluate differently across candidate answers; the remainder encode shared domain facts satisfied equally by every candidate. MAX-SAT agrees with count-only aggregation on 803 of 804 predictions, which confirms that satisfiability structure adds nothing when constraints are non-discriminative. Constraint extraction accounts for 48.7\% of total pipeline time and roughly doubles computational cost for zero expected accuracy benefit. For practitioners who evaluate constraint-based voting, the multi-candidate rate $C_0$ serves as a zero-cost diagnostic: it is computable from trace samples alone, before any investment in constraint extraction or solver invocation. Low $C_0$ rules out any possible SICA gain by construction, and high $C_0$ signals the need for a small-scale constrain
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T19:31:11.320465+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
  "description": "Final word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex",
    "description": "Final word count"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T19:31:11.320574+00:00_

346 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_conclusion_20260517T192902",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-17T19:31:11.320714+00:00_

Done. `conclusion.tex` written at 346 words (including LaTeX commands). All required numbers match the Abstract and Introduction exactly, no em-dashes/en-dashes, no -ing phrase endings, no filler openers. Three paragraphs: findings summary with capability trap framing, practical implications with all key metrics, and future directions targeting the extraction bottleneck.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_conclusion_20260517T192902"
}
```

</details>

---
