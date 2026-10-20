# paper writing compress related work

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_writing_compress_related_work_20260514T212724.jsonl`
- **Structured JSON:** [`837db5ef58de7fad8676.json`](../../sessions/83/837db5ef58de7fad8676.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-14T21:29:14.348361+00:00_

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
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:29:14.349064+00:00_

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
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:29:14.349256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T21:29:14.349501+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for structured ge
…[truncated 19776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:29:14.349738+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Grammar-Constrained Decoding.}\nXGrammar~\\cite{dong2025xgrammar}, Outlines~\\cite{willard2023outlines}, and LMQL~\\cite{beurer-kellner2023lmql} have made grammar-constrained decoding the standard for obtaining structured LLM output, ensuring every token belongs to a grammar-valid continuation via pushdown automata, finite-state machines, or compiled constraint masks.\nDOMINO~\\cite{beurer-kellner2024domino} and ASAp~\\cite{park2024grammar} further address distribution distortion from naive token masking, making grammar enforcement both fast and statistically principled.\nHowever, all these methods operate exclusively at the syntactic level---they ensure format validity (e.g., well-formed JSON) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.\n\n\\paragraph{Semantic Constrained Decoding for Code.}\nIn programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties.\nSynchromesh~\\cite{synchromesh_iclr2022} pioneers constrained semantic decoding with dynamic token masks conditioned on the generation prefix; PICARD~\\cite{scholak2021picard} performs incremental SQL parsing to reject type-invalid tokens; MGD~\\cite{mgd_neurips2023} applies static-analysis monitors for incremental type checking at decode time; and \\citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for logits masking, reducing compilation errors by over 50\\%.\nThese methods demonstrate that richer-than-CFG semantic constraints are feasible at decode time, but exclusively in the code domain---OntoCoDec migrates this type-constrained decoding paradigm from code generation to information extraction.\n\n\\paragraph{Vocabulary and Type-Constrained Generation.}\n\\citet{roth_yih_2004} establish the foundational principle that relational type compatibility should be a hard constraint via integer linear programming, though applied post-hoc over discrete candidates.\nIn the autoregressive era, GENRE~\\cite{decao2021genre}, AdaKGC~\\cite{adakgc_emnlp2023}, GCD~\\cite{geng2023gcd}, and GoLLIE~\\cite{sainz2024gollie} constrain \\emph{which tokens} can appear (vocabulary membership) but not \\emph{which type combinations} are valid for a given relation---OntoCoDec's semantic layer enforces relational constraints where the valid set depends on the relation type generated earlier in the same sequence.\n\n\\paragraph{Structural Constraints via Training.}\nUIE~\\cite{lu2022uie}, GoLLIE~\\cite{sainz2024gollie}, KnowCoder~\\cite{knowcoder_acl2024}, and CodeIE~\\cite{li2023codeie} encode IE output structure through model training or schema-as-code prompting, relying on learned representations to produce schema-compliant outputs.\nThese methods provide \\emph{soft} structural guidance---the model learns to prefer valid outputs but cannot guarantee compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.\nTraining-based and decoding-time approaches are complementary: OntoCoDec provides \\emph{hard} enforcement that is training-free and composable with any of these methods.\n\n\\paragraph{Post-hoc Ontology Validation.}\nODKE+~\\cite{khorshidi2025odke} uses ontology snippets as prompt context for constraint guidance; OntoGPT~\\cite{spires_2024} validates extracted outputs against OBO ontologies in a second pass; OntoLogX~\\cite{ontologx_2025} applies SHACL validation with iterative re-prompting, reducing violations by approximately $10\\times$ across multiple correction rounds.\nThese detect-then-fix approaches waste compute on violated outputs---in our setting, 15.37\\% of generated triples contain domain/range violations under unconstrained decoding---whereas OntoCoDec \\emph{prevents} violations during decoding, redirecting probability mass to valid alternatives.\n\n\\paragraph{Quality Impact of Constrained Decoding.}\nRecent work raises concerns that constrained decoding degrades generation quality: CRANE~\\cite{banerjee2025crane} shows grammar restrictions suppress chain-of-thought reasoning, \\citet{schall2025hiddencost} find 10--30\\% semantic degradation on reasoning tasks, and \\citet{tam2024letmespeak} demonstrate that rigid format constraints harm reasoning benchmarks.\nCrucially, however, \\citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to---or even benefit from---format constraints, and IE is fundamentally extraction rather than reasoning.\nOntoCoDec confirms this empirically: domain/range violations decrease by 94\\% on SciERC with zero F1 degradation, as constraints target only type tokens while leaving free-text entity spans unconstrained.\n\n\\medskip\n\\noindent\nOntoCoDec is the first system to automatically compile IE ontology domain/range constraints into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement for information extraction.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Grammar-Constrained Decoding.}\nXGrammar~\\cite{dong2025xgrammar}, Outlines~\\cite{willard2023outlines}, and LMQL~\\cite{beurer-kellner2023lmql} have made grammar-constrained decoding the standard for obtaining structured LLM output, ensuring every token belongs to a grammar-valid continuation via pushdown automata, finite-state machines, or compiled constraint masks.\nDOMINO~\\cite{beurer-kellner2024domino} and ASAp~\\cite{park2024grammar} further address distribution distortion from naive token masking, making grammar enforcement both fast and statistically principled.\nHowever, all these methods operate exclusively at the syntactic level---they ensure format validity (e.g., well-formed JSON) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.\n\n\\paragraph{Semantic Constrained Decoding for Code.}\nIn programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties.\nSynchromesh~\\cite{synchromesh_iclr2022} pioneers constrained semantic decoding with dynamic token masks conditioned on the generation prefix; PICARD~\\cite{scholak2021picard} performs incremental SQL parsing to reject type-invalid tokens; MGD~\\cite{mgd_neurips2023} applies static-analysis monitors for incremental type checking at decode time; and \\citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for logits masking, reducing compilation errors by over 50\\%.\nThese methods demonstrate that richer-than-CFG semantic constraints are feasible at decode time, but exclusively in the code domain---OntoCoDec migrates this type-constrained decoding paradigm from code generation to information extraction.\n\n\\paragraph{Vocabulary and Type-Constrained Generation.}\n\\citet{roth_yih_2004} establish the foundational principle that relational type compatibility should be a hard constraint via integer linear programming, though applied post-hoc over discrete candidates.\nIn the autoregressive era, GENRE~\\cite{decao2021genre}, AdaKGC~\\cite{adakgc_emnlp2023}, GCD~\\cite{geng2023gcd}, and GoLLIE~\\cite{sainz2024gollie} constrain \\emph{which tokens} can appear (vocabulary membership) but not \\emph{which type combinations} are valid for a given relation---OntoCoDec's semantic layer enforces relational constraints where the valid set depends on the relation type generated earlier in the same sequence.\n\n\\paragraph{Structural Constraints via Training.}\nUIE~\\cite{lu2022uie}, GoLLIE~\\cite{sainz2024gollie}, KnowCoder~\\cite{knowcoder_acl2024}, and CodeIE~\\cite{li2023codeie} encode IE output structure through model training or schema-as-code prompting, relying on learned representations to produce schema-compliant outputs.\nThese methods provide \\emph{soft} structural guidance---the model learns to prefer valid outputs but cannot guarantee compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.\nTraining-based and decoding-time approaches are complementary: OntoCoDec provides \\emph{hard} enforcement that is training-free and composable with any of these methods.\n\n\\paragraph{Post-hoc Ontology Validation.}\nODKE+~\\cite{khorshidi2025odke} uses ontology snippets as prompt context for constraint guidance; OntoGPT~\\cite{spires_2024} validates extracted outputs against OBO ontologies in a second pass; OntoLogX~\\cite{ontologx_2025} applies SHACL validation with iterative re-prompting, reducing violations by approximately $10\\times$ across multiple correction rounds.\nThese detect-then-fix approaches waste compute on violated outputs---in our setting, 15.37\\% of generated triples contain domain/range violations under unconstrained decoding---whereas OntoCoDec \\emph{prevents} violations during decoding, redirecting probability mass to valid alternatives.\n\n\\paragraph{Quality Impact of Constrained Decoding.}\nRecent work raises concerns that constrained decoding degrades generation quality: CRANE~\\cite{banerjee2025crane} shows grammar restrictions suppress chain-of-thought reasoning, \\citet{schall2025hiddencost} find 10--30\\% semantic degradation on reasoning tasks, and \\citet{tam2024letmespeak} demonstrate that rigid format constraints harm reasoning benchmarks.\nCrucially, however, \\citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to---or even benefit from---format constraints, and IE is fundamentally extraction rather than reasoning.\nOntoCoDec confirms this empirically: domain/range violations decrease by 94\\% on SciERC with zero F1 degradation, as constraints target only type tokens while leaving free-text entity spans unconstrained.\n\n\\medskip\n\\noindent\nOntoCoDec is the first system to automatically compile IE ontology domain/range constraints into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement for information extraction.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T21:29:14.350062+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T21:29:14.350210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex | sed 's/\\\\cite{[^}]*}//g; s/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/---/ /g; s/--/ /g; s/\\\\%//g' | wc -w",
  "description": "Count words in related work section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex | sed 's/\\\\cite{[^}]*}//g; s/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/---/ /g; s/--/ /g; s/\\\\%//g' | wc -w",
    "description": "Count words in related work section"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:29:14.350342+00:00_

500

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:29:14.350493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:29:14.350646+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, and LMQL~\cite{beurer-kellner2023lmql} have made grammar-constrained decoding the standard for obtaining structured LLM output, ensuring every token belongs to a grammar-valid continuation via pushdown automata, finite-state machines, or compiled constraint masks.
6	DOMINO~\cite{beurer-kellner2024domino} and ASAp~\cite{park2024grammar} further address distribution distortion from naive token masking, making grammar enforcement both fast and statistically principled.
7	However, all these methods operate exclusively at the syntactic level---they ensure format validity (e.g., well-formed JSON) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
8	
9	\paragraph{Semantic Constrained Decoding for Code.}
10	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties.
11	Synchromesh~\cite{synchromesh_iclr2022} pioneers constrained semantic decoding with dynamic token masks conditioned on the generation prefix; PICARD~\cite{scholak2021picard} performs incremental SQL parsing to reject type-invalid tokens; MGD~\cite{mgd_neurips2023} applies static-analysis monitors for incremental type checking at decode time; and \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for logits masking, reducing compilation errors by over 50\%.
12	These methods demonstrate that richer-than-CFG semantic constraints are feasible at decode time, but exclusively in the code domain---OntoCoDec migrates this type-constrained decoding paradigm from code generation to information extraction.
13	
14	\paragraph{Vocabulary and Type-Constrained Generation.}
15	\citet{roth_yih_2004} establish the foundational principle that relational type compatibility should be 
…[truncated 3079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:29:14.350823+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Grammar-Constrained Decoding.}\nXGrammar~\\cite{dong2025xgrammar}, Outlines~\\cite{willard2023outlines}, and LMQL~\\cite{beurer-kellner2023lmql} have made grammar-constrained decoding the standard for structured LLM output, ensuring every token belongs to a grammar-valid continuation.\nDOMINO~\\cite{beurer-kellner2024domino} and ASAp~\\cite{park2024grammar} further address distribution distortion, making grammar enforcement statistically principled.\nHowever, these methods operate at the syntactic level---they ensure format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.\n\n\\paragraph{Semantic Constrained Decoding for Code.}\nIn code generation, constrained decoding has been extended to enforce semantic properties: Synchromesh~\\cite{synchromesh_iclr2022} enforces type and scope constraints via dynamic token masks; PICARD~\\cite{scholak2021picard} performs incremental SQL parsing to reject type-invalid tokens; MGD~\\cite{mgd_neurips2023} applies static-analysis monitors for type checking at decode time; and \\citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for logits masking.\nThese demonstrate that richer-than-CFG constraints are feasible at decode time, but exclusively in the code domain---OntoCoDec migrates this paradigm to information extraction.\n\n\\paragraph{Vocabulary and Type-Constrained Generation.}\n\\citet{roth_yih_2004} establish that relational type compatibility should be a hard constraint via integer linear programming, though applied post-hoc.\nGENRE~\\cite{decao2021genre}, AdaKGC~\\cite{adakgc_emnlp2023}, GCD~\\cite{geng2023gcd}, and GoLLIE~\\cite{sainz2024gollie} constrain \\emph{which tokens} can appear (vocabulary membership) but not \\emph{which type combinations} are valid for a given relation---OntoCoDec enforces relational constraints where the valid set depends on the relation type generated earlier in the same sequence.\n\n\\paragraph{Structural Constraints via Training.}\nUIE~\\cite{lu2022uie}, GoLLIE~\\cite{sainz2024gollie}, KnowCoder~\\cite{knowcoder_acl2024}, and CodeIE~\\cite{li2023codeie} encode IE structure through training or schema-as-code prompting.\nThese provide \\emph{soft} guidance---the model learns to prefer valid outputs but cannot guarantee compliance, as shown by non-trivial violation rates even in fine-tuned systems.\nOntoCoDec provides complementary \\emph{hard} enforcement that is training-free and composable with these methods.\n\n\\paragraph{Post-hoc Ontology Validation.}\nODKE+~\\cite{khorshidi2025odke} uses ontology snippets as prompt context; OntoGPT~\\cite{spires_2024} validates outputs against ontologies in a second pass; OntoLogX~\\cite{ontologx_2025} applies SHACL validation with iterative re-prompting, reducing violations by ${\\sim}10\\times$ across correction rounds.\nThese detect-then-fix approaches waste compute on violated outputs, whereas OntoCoDec \\emph{prevents} violations during decoding by redirecting probability mass to valid alternatives.\n\n\\paragraph{Quality Impact of Constrained Decoding.}\nCRANE~\\cite{banerjee2025crane} shows grammar restrictions suppress chain-of-thought reasoning, \\citet{schall2025hiddencost} find 10--30\\% degradation on reasoning tasks, and \\citet{tam2024letmespeak} demonstrate that format constraints harm reasoning benchmarks.\nHowever, \\citet{tam2024letmespeak}'s results also show extraction-style tasks are robust to---or benefit from---constraints, and IE is fundamentally extraction rather than reasoning.\nOntoCoDec confirms this: violations decrease by 94\\% on SciERC with zero F1 degradation, as constraints target only type tokens while leaving entity spans unconstrained.\n\n\\medskip\n\\noindent\nOntoCoDec is the first system to automatically compile IE ontology domain/range constraints into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement for information extraction.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Grammar-Constrained Decoding.}\nXGrammar~\\cite{dong2025xgrammar}, Outlines~\\cite{willard2023outlines}, and LMQL~\\cite{beurer-kellner2023lmql} have made grammar-constrained decoding the standard for structured LLM output, ensuring every token belongs to a grammar-valid continuation.\nDOMINO~\\cite{beurer-kellner2024domino} and ASAp~\\cite{park2024grammar} further address distribution distortion, making grammar enforcement statistically principled.\nHowever, these methods operate at the syntactic level---they ensure format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.\n\n\\paragraph{Semantic Constrained Decoding for Code.}\nIn code generation, constrained decoding has been extended to enforce semantic properties: Synchromesh~\\cite{synchromesh_iclr2022} enforces type and scope constraints via dynamic token masks; PICARD~\\cite{scholak2021picard} performs incremental SQL parsing to reject type-invalid tokens; MGD~\\cite{mgd_neurips2023} applies static-analysis monitors for type checking at decode time; and \\citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for logits masking.\nThese demonstrate that richer-than-CFG constraints are feasible at decode time, but exclusively in the code domain---OntoCoDec migrates this paradigm to information extraction.\n\n\\paragraph{Vocabulary and Type-Constrained Generation.}\n\\citet{roth_yih_2004} establish that relational type compatibility should be a hard constraint via integer linear programming, though applied post-hoc.\nGENRE~\\cite{decao2021genre}, AdaKGC~\\cite{adakgc_emnlp2023}, GCD~\\cite{geng2023gcd}, and GoLLIE~\\cite{sainz2024gollie} constrain \\emph{which tokens} can appear (vocabulary membership) but not \\emph{which type combinations} are valid for a given relation---OntoCoDec enforces relational constraints where the valid set depends on the relation type generated earlier in the same sequence.\n\n\\paragraph{Structural Constraints via Training.}\nUIE~\\cite{lu2022uie}, GoLLIE~\\cite{sainz2024gollie}, KnowCoder~\\cite{knowcoder_acl2024}, and CodeIE~\\cite{li2023codeie} encode IE structure through training or schema-as-code prompting.\nThese provide \\emph{soft} guidance---the model learns to prefer valid outputs but cannot guarantee compliance, as shown by non-trivial violation rates even in fine-tuned systems.\nOntoCoDec provides complementary \\emph{hard} enforcement that is training-free and composable with these methods.\n\n\\paragraph{Post-hoc Ontology Validation.}\nODKE+~\\cite{khorshidi2025odke} uses ontology snippets as prompt context; OntoGPT~\\cite{spires_2024} validates outputs against ontologies in a second pass; OntoLogX~\\cite{ontologx_2025} applies SHACL validation with iterative re-prompting, reducing violations by ${\\sim}10\\times$ across correction rounds.\nThese detect-then-fix approaches waste compute on violated outputs, whereas OntoCoDec \\emph{prevents} violations during decoding by redirecting probability mass to valid alternatives.\n\n\\paragraph{Quality Impact of Constrained Decoding.}\nCRANE~\\cite{banerjee2025crane} shows grammar restrictions suppress chain-of-thought reasoning, \\citet{schall2025hiddencost} find 10--30\\% degradation on reasoning tasks, and \\citet{tam2024letmespeak} demonstrate that format constraints harm reasoning benchmarks.\nHowever, \\citet{tam2024letmespeak}'s results also show extraction-style tasks are robust to---or benefit from---constraints, and IE is fundamentally extraction rather than reasoning.\nOntoCoDec confirms this: violations decrease by 94\\% on SciERC with zero F1 degradation, as constraints target only type tokens while leaving entity spans unconstrained.\n\n\\medskip\n\\noindent\nOntoCoDec is the first system to automatically compile IE ontology domain/range constraints into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement for information extraction.\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T21:29:14.351035+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:29:14.351167+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex | sed 's/\\\\cite{[^}]*}//g; s/\\\\citet{[^}]*}//g; s/\\\\emph{//g; s/\\\\textsc{//g; s/\\\\paragraph{//g; s/\\\\section{//g; s/\\\\label{[^}]*}//g; s/\\\\medskip//g; s/\\\\noindent//g; s/{\\\\sim}//g; s/\\$[^$]*\\$//g; s/---/ /g; s/--/ /g; s/~/ /g; s/[{}%\\\\]//g; s/  */ /g' | wc -w",
  "description": "Count words in compressed related work"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex | sed 's/\\\\cite{[^}]*}//g; s/\\\\citet{[^}]*}//g; s/\\\\emph{//g; s/\\\\textsc{//g; s/\\\\paragraph{//g; s/\\\\section{//g; s/\\\\label{[^}]*}//g; s/\\\\medskip//g; s/\\\\noindent//g; s/{\\\\sim}//g; s/\\$[^$]*\\$//g; s/---/ /g; s/--/ /g; s/~/ /g; s/[{}%\\\\]//g; s/  */ /g' | wc -w",
    "description": "Count words in compressed related work"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T21:29:14.351295+00:00_

420

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_compress_related_work_20260514T212724",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T21:29:14.351448+00:00_

420 words, within the 400–450 target. All 6 paragraphs present with required citations, plus the final positioning sentence.

Written to `section6_related_work.tex` — 420 words (down from 2441), 6 `\paragraph{}` sections + closing positioning statement. All specified citations retained, no new citations added.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_compress_related_work_20260514T212724"
}
```

</details>

---
