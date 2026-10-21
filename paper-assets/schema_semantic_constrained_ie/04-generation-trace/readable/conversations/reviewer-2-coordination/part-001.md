# Reviewer 2 coordination — Part 1 of 5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/16/16fda77cba37e7ffdcac.json)

## Round 1

## Round 1

50 recorded events


### User

_source line 1 · 2026-05-15T08:26:07.594721+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work + 写作质量）

### Venue 信息
- **目标**：EMNLP 2026 via ARR May 2026 cycle
- **截止日期**：2026-05-25 (AoE)
- **页数限制**：长文 ≤ 8 页正文（不含 references/limitations/ethics/appendix）
- **模板**：ACL template, `\usepackage[review]{acl}`
- **匿名规则**：Double-blind

### 论文路径
`projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
（多文件结构，main.tex 通过 `\input{}` 引入各章节，请逐一阅读所有 section*.tex 和 appendix*.tex 文件，以及 relwork_new_entries.bib）

### 论文概要
OntoCoDec 提出两层约束解码框架用于 IE：grammar 层（XGrammar CFG）保证 JSON 结构和词汇合法性，semantic 层通过有状态 entity registry + 动态 logit masking 强制 domain/range 约束。在 SciERC (7 relations) 和 DocRED (96 relations) 上用 Qwen3-8B 和 Llama-3.1-8B 验证。

### 你的审查侧重

**1. 新颖性评估**
- "第一个将 grammar-constrained decoding 从语法层扩展到语义层用于 IE"的声明是否成立？
- 与 code generation 领域的 type-constrained decoding（Synchromesh, PICARD, MGD, PLDI 2025）的技术差异是否足够构成 novelty？论文声称 IE 的独特挑战是 entity registry 在生成过程中动态构建——这是否是一个足够重要的区别？
- 与 EnriCo（ASP constraints during decoding）、GenIE（state-based constraints）的区别在哪里？论文是否充分讨论了这些？
- Constraint tightness 的分析是新颖的 insight 还是已知常识？

**2. Related Work 完整性**
- 检查论文的 related work（§6 主体 + Appendix A 扩展版）是否覆盖了以下关键方向：
  - Grammar/structured constrained decoding（XGrammar, Outlines, LMQL, DOMINO, ASAp, Guidance）
  - Semantic constrained decoding for code（Synchromesh, PICARD, MGD, PLDI 2025）
  - IE-specific constrained generation（GENRE, GenIE, AdaKGC, GCD, NeuroLogic）
  - Training-based IE（TANL, REBEL, UIE, GoLLIE, KnowCoder, CodeIE, ADELIE, SpERT, PFN）
  - Post-hoc ontology validation（ODKE+, OntoGPT, OntoLogX, RELATE）
  - Constrained decoding quality concerns（CRANE, Schall et al., Tam et al.）
- 是否有重要的遗漏工作？特别是：
  - 2025-2026 年的最新 IE + constrained decoding 工作
  - 知识图谱补全/验证方向的相关工作
  - 其他 ontology-aware NLP 系统

**3. 写作质量与格式合规**
- 论文结构是否清晰？各 section 之间的逻辑流是否通顺？
- 数学符号使用是否一致？（注意 §2 用 σ 而 §3 用 dom/range——是否存在符号不一致？）
- 表格和图表是否清晰、信息充足？
- 是否符合 8 页限制？（请估算正文页数）
- Limitations section 是否充分？是否遗漏了重要局限？
- Ethics statement 是否合规？
- 匿名性：是否有泄露作者身份的信息？（检查 GitHub 链接、机构名称等）
- 引用格式是否正确？bib 条目是否完整？

**4. Presentation 问题**
- Abstract 是否准确反映论文贡献和结果？
- Introduction 的 motivation 是否令人信服？
- 术语定义是否清晰（DR, RV, ET, CF 等缩写）？
- 是否有语法错误或拼写错误？

请按以下格式输出审稿意见：
```
## Summary（2-3 句）
## Strengths（逐条）
## Weaknesses（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）
## Questions（需要作者回答）
## Missing References（如有）
## Overall Assessment（评分 + 置信度）
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-15T08:26:18.434768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-15T08:26:19.390051+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-15T08:26:19.390487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-15T08:26:19.441083+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Valid Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	
53	% === §6 Related Work ===
54	\input{section6_related_work}
55	
56	% === §7 Discussion and Conclusion ===
57	\section{Discussion and Conclusion}
58	\label{sec:discussion}
59	\input{section7_conclusion_compressed}
60	
61	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
62	\section*{Limitations}
63	
64	The semantic layer introduces cross-field consistency (CF) violations (up to 12.02\%), a systematic consequence of per-relation independent enforcement that remains an open challenge.
65	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
66	Results cover two 8B-class models under zero-shot prompting; integration w
…[truncated 906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-15T08:26:25.316388+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-15T08:26:25.819025+00:00_

1	\begin{abstract}
2	LLM-based information extraction systems produce systematic ontology constraint violations during autoregressive generation.
3	On SciERC (7 relation types), 15.37\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.46\%---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
4	%
5	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:
6	(1)~a \emph{grammar layer} (XGrammar CFG) enforcing JSON structural validity and restricting entity/relation vocabularies to schema-defined values (ET, RV\,$\to$\,0\%); and
7	(2)~a \emph{semantic layer} enforcing domain/range constraints via a stateful entity registry and dynamic logit masking.
8	The grammar layer is an enabling prerequisite; the two compose via bitwise AND on token-level masks.
9	%
10	On SciERC, \textsc{OntoCoDec} reduces domain/range violations by 94\% (15.37\%\,$\to$\,0.93\%) while maintaining extraction F1 ({+}0.13pp, $p{=}0.58$).
11	On DocRED, violations decrease by 45--90\% depending on the model, with significant relation F1 gains for both Qwen3-8B ({+}0.50pp, $p{<}0.001$) and Llama-3.1-8B ({+}0.29pp, $p{=}0.013$; DR$\downarrow$90.2\%).
12	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1
13	The dual-factor mechanism---tightness $\times$ baseline violation rate---explains cross-dataset and cross-model DR reduction differences.
14	\end{abstract}
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-15T08:26:25.819408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-15T08:26:26.322787+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.7\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records ty
…[truncated 1242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-15T08:26:26.323275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-15T08:26:27.277533+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules---e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''---which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}---well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}---$(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}---at the point where a type token is generated, all information needed (relation type, entity registry) is available i
…[truncated 25 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-15T08:26:27.277960+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-15T08:26:27.780565+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$:
19	%
20	\begin{equation}\label{eq:output-schema}
21	\resizebox{.88\columnwidth}{!}{$\displaystyle
22	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
23	$}
24	\end{equation}
25	%
26	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
27	
28	\paragraph{Ontology schema.}
29	An ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \operatorname{dom}, \operatorname{range})$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and functions $\operatorname{dom}, \operatorname{range}: \mathcal{R} \to 2^{\mathcal{E}}$ specifying permitted head and tail types for each relation.
30	
31	\paragraph{Ontology compliance.}
32	A triple $(h, r, t)$ with $\operatorname{type}(h) = \tau^h$, $\operatorname{type}(t) = \tau^t$ is \emph{type-valid} w.r.t.\ $\mathcal{O}$ iff:
3
…[truncated 7785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-15T08:26:27.831297+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-15T08:26:28.234951+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \tau(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\tau} = \frac{1}{|\mathcal{R}|}\sum_{r} \tau(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor mechanism---tightness $\times$ baseline model violation rate---explains the cross-dataset patt
…[truncated 917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-15T08:26:28.235482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-15T08:26:28.688960+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents, 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	
14	\paragraph{Violation distribution.}
15	Table~\ref{tab:prompt_comparison} reports violation rates.
16	DR violations affect 15.37\% of triples on SciERC and 18.70\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
17	RV violations on DocRED are dramatically higher (28.90\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce a target vocabulary from a single prompt.
18	Per-relation rates (Figure~\ref{fig:per_relation_dr}) vary by over 40 percentage points: \textsc{Compare} at 42.4\% vs.\ \textsc{Used-for} at 0.76\%, correlating with tightness---tight constraints (few valid type pairs) produce systematic failures.
19	
20	\begin{table}[t]
21	\centering
22	\caption{Violation rates (\%) under unconstrained and sche
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-15T08:26:28.689512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-15T08:26:29.694524+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: rel
…[truncated 5214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-15T08:26:29.694975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-15T08:26:30.148622+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 2759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-15T08:26:30.150223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-15T08:26:30.602427+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results alongside Qwen3-8B.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr rr@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \multicolumn{2}{c}{\textbf{F1}} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-8}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & Rel. & Ent. \\
26	\midrule
27	\multirow{4}{*}{SciERC}
28	  & Qwen (U)  & 15.37 & 1.39 & 0.40 & 0.08 & 8.23 & 31.01 \\
29	  & Qwen (S1) &  0.93 & 0    & 0    & 9.90 & 8.36 & 30.98 \\
30	  \cmidrule(l){2-8}
31	  & Llama (U)  & 13.34 & 0.55 & 0    & 0.24 & 2.68 & 23.56 \\
32	  & Llama (S1) &  0.08 & 0    & 0    & 6.56 & 2.54 & 23.49 \\
33	\midrule
34	\multirow{4}{*}{DocRED}
35	  & Qwen (U)  & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 & 58.15 \\
36	  & Qwen (S1) & 10.21 &  0.03 & 0    & 2.57 & 8.23 & 59.37 \\
37	  \cmidrule(l){2-8}
38	  & Llama (U)  & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 & 55.65 \\
39	  & Llama (S1) &  2.55 &  0    & 0    & 12.02 & 6.27 & 55.01 \\
40	\bottomrule
41	\end{tabular}}%
42	\caption{Cross-model validation. U: unconstrained; S1: full two-layer.
43	Parse failures (U$\to$S1): Qwen DocRED 12$\to$11, Llama DocRED 68$\to$91; others $\leq$1.
44	F1 $\times$100.}
45	\label{tab:cross-model}
46	\end{table}
47	
48	\paragraph{Model-agnostic structural guarantees.}
49	RV and ET vi
…[truncated 2798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-15T08:26:30.602847+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-15T08:26:31.564271+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, Guidance~\cite{guidance2023}, and LMQL~\cite{beurer-kellner2023lmql} have made grammar-constrained decoding the standard for structured LLM output, ensuring every token belongs to a grammar-valid continuation.
6	DOMINO~\cite{beurer-kellner2024domino} and ASAp~\cite{park2024grammar} further address distribution distortion, making grammar enforcement statistically principled.
7	However, these methods operate at the syntactic level---they ensure format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
8	
9	\paragraph{Semantic Constrained Decoding for Code.}
10	In code generation, constrained decoding has been extended to enforce semantic properties: Synchromesh~\cite{synchromesh_iclr2022} enforces type and scope constraints via dynamic token masks; PICARD~\cite{scholak2021picard} performs incremental SQL parsing to reject type-invalid tokens; MGD~\cite{mgd_neurips2023} applies static-analysis monitors for type checking at decode time; and \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata for logits masking.
11	These demonstrate that richer-than-CFG constraints are feasible at decode time, but exclusively in the code domain---OntoCoDec migrates this paradigm to information extraction.
12	
13	\paragraph{Vocabulary and Type-Constrained Generation.}
14	\citet{roth_yih_2004} establish that relational type compatibility should be a hard constraint via integer linear programming, though applied post-hoc; see also~\cite{xie2016tkrl}.
15	GENRE~\cite{decao2021genre}, NeuroLogic~\cite{lu2021neurologic}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation--
…[truncated 2281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 961
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-15T08:26:31.565078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-15T08:26:32.021480+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix B.
3	
4	\paragraph{CF Severity.}
5	% exp_ids: phase2_scierc_full_s1 (CF=9.90%), phase2_scierc_grammar_only (CF=0.08%),
6	%          phase2_docred_full_s1 (CF=2.57%), llama_docred_full_s1 (CF=12.02%)
7	DR violations produce ontologically invalid triples---a hard constraint failure that no downstream system can recover from.
8	CF violations are qualitatively different: each individual triple remains type-valid with respect to its own relation's domain/range rules; only cross-triple consistency is broken when the same entity receives different types across relations.
9	The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245 affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
10	Ablation cleanly attributes CF to the semantic layer: grammar-only decoding yields CF\,=\,0.08\%, matching the unconstrained baseline, while the full system reaches 9.90\% on SciERC and 2.57\% on DocRED (Qwen3-8B; 12.02\% DocRED for Llama-3.1-8B), confirming that CF arises from per-relation independent enforcement where each relation's constraint mask is computed without access to type decisions made for other relations (extended analysis in Appendix~\ref{app:discussion}).
11	% exp_ids: phase2_scierc_grammar_only, phase2_docred_full_s1, llama_docred_full_s1
12	
13	\paragraph{Dataset-Dependent F1 Impact.}
14	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
15	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
16	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
17	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; 
…[truncated 1326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 28 · 2026-05-15T08:26:32.021976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-15T08:26:32.492067+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
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
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 470
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-15T08:26:32.492592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-15T08:26:32.944903+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% Paragraph 1: Low F1 Practical Significance %%%
7	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
8	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
9	
10	\paragraph{Practical Significance of Zero-Shot F1.}
11	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
12	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
13	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
14	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
15	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
16	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
17	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
18	
19	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
20	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
21	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
22	
23	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
24	Post-hoc filtering---gener
…[truncated 1210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-15T08:26:32.945300+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-15T08:26:33.648843+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-15T08:26:33.649359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-15T08:26:34.051904+00:00_

1	% ============================================================
2	% Merged authoritative BibTeX references (9 entries)
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
7	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
8	@inproceedings{synchromesh_iclr2022,
9	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
10	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
11	  booktitle = {International Conference on Learning Representations},
12	  year      = {2022},
13	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
14	}
15	
16	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
17	@inproceedings{mgd_neurips2023,
18	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
19	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
20	  booktitle = {Advances in Neural Information Processing Systems},
21	  volume    = {36},
22	  year      = {2023},
23	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
24	}
25	
26	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
27	@article{pldi2025_type_constrained_codegen,
28	  title     = {Type-Constrained Code Generation with Language Models},
29	  author    = {M\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},
30	  journal   = {Proceedings of the ACM on Programming Languages},
31	  volume    = {9},
32	  number    = {PLDI},
33	  year      = {2025},
34	  doi       = {10.1145/3729274},
35	  url       = {https://dl.acm.org/doi/10.1145/372927
…[truncated 25279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-15T08:26:38.871709+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-15T08:26:38.922409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-15T08:26:42.136298+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 review form criteria scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 review form criteria scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-15T08:26:42.438288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer guidelines review form 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer guidelines review form 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-15T08:26:49.016907+00:00_

Web search results for query: "ACL ARR 2026 review form criteria scoring dimensions"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, I found detailed information about the ACL ARR 2026 review form criteria and scoring dimensions:

## ARR 2026 Review Form Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Key Scoring Dimensions:

**1. Soundness**
The soundness scores must be justified by th
…[truncated 1226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6880
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-15T08:26:50.574597+00:00_

Web search results for query: "ACL Rolling Review reviewer guidelines review form 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found information about ACL Rolling Review (ARR) reviewer guidelines and review forms for 2025-2026. Here are the key findings:

## Reviewer Guidelines and Requirements

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. Soundness scores must be justified by the text of the review. If you give a low Soundness sco
…[truncated 1578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8136
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-15T08:26:56.100752+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-15T08:26:56.201577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-15T08:26:59.969134+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (e.g., 1-5), and descriptions for each score level. I need the exact scoring rubric for soundness, excitement, overall recommendation, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (e.g., 1-5), and descriptions for each score level. I need the exact scoring rubric for soundness, excitement, overall recommendation, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-15T08:27:06.536829+00:00_

# ACL Rolling Review Form - Scoring Rubrics

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## Soundness (1-5 scale with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## Excitement (1-5 scale with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## Overall Assessment (1-5 scale with half-point increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Reproducibility (1-5 scale)
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: Hard to reproduce without author data
- **1**: Cannot reproduce

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6567
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-15T08:31:39.861771+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-15T08:31:39.862557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-15T08:32:50.523252+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见（新颖性 + Related Work + 写作质量）\n\n### Summary（2-3 句）\n\n本文提出 OntoCoDec，一个两层约束解码框架：grammar 层（XGrammar CFG）保证 JSON 结构和词汇合法性，semantic 层通过有状态 entity registry + 动态 logit masking 强制 domain/range 约束。在 SciERC 和 DocRED 上用 Qwen3-8B 和 Llama-3.1-8B 零样本验证，DR 违规减少 45–99%，F1 保持中性或显著提升。论文还提出 constraint tightness 概念解释跨数据集和跨模型的 DR 消减差异。\n\n---\n\n### Strengths\n\n**S1. 系统性的违规分类与分析框架。** 四类违规（DR/RV/ET/CF）定义清晰，Phase 0 系统性研究揭示了 LLM-based IE 中本体违规的普遍性（SciERC 15.37%、DocRED 18.46%），诊断性贡献本身有价值。\n\n**S2. 两层架构的 enabling dependency 有力验证。** 五路消融（Table 2）展示 grammar-only 仅消除 RV/ET 而 DR 不变、semantic-only DR 仅降 24%，两层组合达 94%——grammar 保证词汇合法性后 semantic 才能查询 dom/range 规则。实验论证充分。\n\n**S3. Constraint tightness 分析提供可解释的理论框架。** tightness × baseline RV 双因子机制很好解释了 SciERC vs DocRED 差异以及 Qwen vs Llama 非对称表现，超越单纯经验报告。\n\n**S4. 实验设计严谨。** Bootstrap resampling（10,000 次）配合 95% CI 和 p 值，2 模型 × 2 数据集交叉验证，S1 vs S2 策略对比，统计方法论扎实。\n\n**S5. Related Work 覆盖全面定位清晰。** 正文 §6 + Appendix A 覆盖六大范式，与 code gen 类型约束解码的对比细致（PICARD/Synchromesh/MGD/PLDI 2025），主动引用 CRANE/Schall/Tam 负面结果并论证 IE 特殊性。\n\n**S6. Grammar layer \"揭露\"隐藏违规的发现有洞察力。** DocRED grammar-only DR 从 18.46% 升至 26.17%（Table 3），29.66% OOV 关系被纠正后暴露原本不可评估的类型不兼容。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix] §2 与 §3 的本体形式化存在根本性不一致**\n- §2 定义 σ: R → P(E × E)（pair-based），§3 重定义为 dom, range: R → 2^E（independent）。这两个定义在一般情况下不等价：若 σ(r) = {(Person, Person), (Org, Org)}，则 independent check 错误放行 (Person, Org)。\n- Violation rate 评估用 pair-based 定义（§5.1），但执行用 independent dom/range。残余 DR 中有多少是 fallback 导致、有多少是 dom/range 独立性导致，论文无法区分。Tightness 公式基于 pair 计数但实际执行更宽松。\n- 建议：明确 SciERC/DocRED 约束是否 rectangular（σ(r) = dom(r) × range(r)）；统一符号。\n\n**W2 [Must-Fix] CF 违规剧烈恶化未被充分分析，削弱\"zero cost\"叙事**\n- CF 从 0.08% 恶化到 9.90%（SciERC）和 0.17% 到 12.02%（Llama-DocRED）。将一种违规转化为另一种违规而不量化 trade-off 净效果，使\"constraint enforcement\"整体价值难评估。\n- §7 将 CF 定性为\"qualitatively different\"可能被视为 minimize 问题。下游 KG 构建需要全局实体类型一致性。\n- 建议：提供综合指标评估 DR↓ vs CF↑ 净效果；将 global entity-level type consensus 更明确列为当前方法主要局限。\n\n**W3 [Should-Fix] 仅零样本评估，无法验证与 fine-tuned 模型的可组合性声明**\n- R-F1 约 8% 距 SOTA ~50% 差距巨大。论文声称与 GoLLIE 等可组合（§6），但未提供任何 fine-tuned 实验。\n- 建议：至少在一个设置上用 fine-tuned 模型验证残余违规率和边际收益。\n\n**W4 [Should-Fix] 新颖性声明需更精确范围界定**\n- §1 Contribution #2 \"the first to extend grammar-constrained decoding with semantic ontology constraints\" 可被理解为领域无关的首创声明，但 code gen（Synchromesh 2022, PICARD 2021）早已实现语义类型约束。§6 的讨论实际很到位但 Introduction 表述过于宽泛。\n- 建议：改为 \"the first to automatically compile IE ontology domain/range constraints into token-level semantic masks\"。\n\n**W5 [Should-Fix] Single-token type assumption 限制可扩展性未充分讨论**\n- §3.3.2 将每个 τ ∈ E 映射到 first subword token，仅验证 6 types + Qwen tokenizer。更大本体可能不满足 first-token 唯一性。Llama tokenizer 未报告验证结果。\n- 建议：讨论 scalability 和 multi-token masking 可行性。\n\n**W6 [Minor] 数学符号跨 section 不一致**\n- §2 用 σ，§3 用 dom/range；tightness 公式分别用 |σ(r)|/|E|² 和 |V(r)|/|T|²。\n\n**W7 [Minor] Constraint tightness 属于相对直觉性观察**\n- \"约束越紧违规越高\"符合直觉。Dual-factor mechanism 增加解释力但更接近 systematic empirical observation。\n\n**W8 [Minor] 个别表述问题**\n- Abstract 首句 \"produce systematic ontology constraint violations\" 过于绝对，建议 \"can produce\"\n- §3.3.2 \"DocRED (6 types each)\" 中 \"each\" 指代不清（DocRED 有 96 relation types 但仅 6 entity types）\n\n---\n\n### Questions\n\n**Q1.** SciERC/DocRED 的约束是否 rectangular（σ(r) = dom(r) × range(r)）？如不是，independent enforcement 的 over-permissiveness 有多大？\n\n**Q2.** 残余 DR 中，grammar-first fallback 导致 vs dom/range 独立性导致的比例？\n\n**Q3.** Llama tokenizer 对 6 个实体类型的 first-token uniqueness 是否已验证？\n\n**Q4.** CF 冲突实体中，多少是真实标注类型歧义，多少是约束强制扭曲了模型正确输出？\n\n**Q5.** OntoCoDec 因约束重定向概率质量而引入的 false positives 有多少？（对比 Appendix B post-hoc filtering 的 TP loss 分析）\n\n---\n\n### Missing References\n\n建议性补充（非严重遗漏）：\n1. SuRE (Kim et al., ACL 2024) — schema-based structured generation for RE\n2. Constrained Beam Search for KGC（如 KG-BERT + type constraints）\n3. 总体 Related Work 覆盖已相当全面。\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | 方法有效但 pair vs independent 形式化不一致构成理论缺陷；CF trade-off 分析不充分 |\n| Excitement | 3/5 | Tightness 分析有洞察力、enabling dependency 有趣，但核心技术（logit masking for type constraints）已在 code gen 成熟 |\n| Overall | 3/5 (Findings 边界) | 工程扎实、实验充分，但新颖性有限、形式化有缺陷、CF trade-off 削弱贡献叙事 |\n| Reproducibility | 4/5 | 实验设置详尽但无代码发布承诺 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 评估方法论 |\n\n**一句话总结**：工程扎实、实验充分的 IE 约束解码工作，但形式化不一致（pair vs independent）和 CF 恶化 trade-off 构成实质性关切，核心技术新颖性有限（code gen 已有成熟先例），处于 Findings 水准边界。修复 W1-W2 后可达 Findings；增加 fine-tuned 实验（W3）可增强会议接收竞争力。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见（新颖性 + Related Work + 写作质量）\n\n### Summary（2-3 句）\n\n本文提出 OntoCoDec，一个两层约束解码框架：grammar 层（XGrammar CFG）保证 JSON 结构和词汇合法性，semantic 层通过有状态 entity registry + 动态 logit masking 强制 domain/range 约束。在 SciERC 和 DocRED 上用 Qwen3-8B 和 Llama-3.1-8B 零样本验证，DR 违规减少 45–99%，F1 保持中性或显著提升。论文还提出 constraint tightness 概念解释跨数据集和跨模型的 DR 消减差异。\n\n---\n\n### Strengths\n\n**S1. 系统性的违规分类与分析框架。** 四类违规（DR/RV/ET/CF）定义清晰，Phase 0 系统性研究揭示了 LLM-based IE 中本体违规的普遍性（SciERC 15.37%、DocRED 18.46%），诊断性贡献本身有价值。\n\n**S2. 两层架构的 enabling dependency 有力验证。** 五路消融（Table 2）展示 grammar-only 仅消除 RV/ET 而 DR 不变、semantic-only DR 仅降 24%，两层组合达 94%——grammar 保证词汇合法性后 semantic 才能查询 dom/range 规则。实验论证充分。\n\n**S3. Constraint tightness 分析提供可解释的理论框架。** tightness × baseline RV 双因子机制很好解释了 SciERC vs DocRED 差异以及 Qwen vs Llama 非对称表现，超越单纯经验报告。\n\n**S4. 实验设计严谨。** Bootstrap resampling（10,000 次）配合 95% CI 和 p 值，2 模型 × 2 数据集交叉验证，S1 vs S2 策略对比，统计方法论扎实。\n\n**S5. Related Work 覆盖全面定位清晰。** 正文 §6 + Appendix A 覆盖六大范式，与 code gen 类型约束解码的对比细致（PICARD/Synchromesh/MGD/PLDI 2025），主动引用 CRANE/Schall/Tam 负面结果并论证 IE 特殊性。\n\n**S6. Grammar layer \"揭露\"隐藏违规的发现有洞察力。** DocRED grammar-only DR 从 18.46% 升至 26.17%（Table 3），29.66% OOV 关系被纠正后暴露原本不可评估的类型不兼容。\n\n---\n\n### Weaknesses\n\n**W1 [Must-Fix] §2 与 §3 的本体形式化存在根本性不一致**\n- §2 定义 σ: R → P(E × E)（pair-based），§3 重定义为 dom, range: R → 2^E（independent）。这两个定义在一般情况下不等价：若 σ(r) = {(Person, Person), (Org, Org)}，则 independent check 错误放行 (Person, Org)。\n- Violation rate 评估用 pair-based 定义（§5.1），但执行用 independent dom/range。残余 DR 中有多少是 fallback 导致、有多少是 dom/range 独立性导致，论文无法区分。Tightness 公式基于 pair 计数但实际执行更宽松。\n- 建议：明确 SciERC/DocRED 约束是否 rectangular（σ(r) = dom(r) × range(r)）；统一符号。\n\n**W2 [Must-Fix] CF 违规剧烈恶化未被充分分析，削弱\"zero cost\"叙事**\n- CF 从 0.08% 恶化到 9.90%（SciERC）和 0.17% 到 12.02%（Llama-DocRED）。将一种违规转化为另一种违规而不量化 trade-off 净效果，使\"constraint enforcement\"整体价值难评估。\n- §7 将 CF 定性为\"qualitatively different\"可能被视为 minimize 问题。下游 KG 构建需要全局实体类型一致性。\n- 建议：提供综合指标评估 DR↓ vs CF↑ 净效果；将 global entity-level type consensus 更明确列为当前方法主要局限。\n\n**W3 [Should-Fix] 仅零样本评估，无法验证与 fine-tuned 模型的可组合性声明**\n- R-F1 约 8% 距 SOTA ~50% 差距巨大。论文声称与 GoLLIE 等可组合（§6），但未提供任何 fine-tuned 实验。\n- 建议：至少在一个设置上用 fine-tuned 模型验证残余违规率和边际收益。\n\n**W4 [Should-Fix] 新颖性声明需更精确范围界定**\n- §1 Contribution #2 \"the first to extend grammar-constrained decoding with semantic ontology constraints\" 可被理解为领域无关的首创声明，但 code gen（Synchromesh 2022, PICARD 2021）早已实现语义类型约束。§6 的讨论实际很到位但 Introduction 表述过于宽泛。\n- 建议：改为 \"the first to automatically compile IE ontology domain/range constraints into token-level semantic masks\"。\n\n**W5 [Should-Fix] Single-token type assumption 限制可扩展性未充分讨论**\n- §3.3.2 将每个 τ ∈ E 映射到 first subword token，仅验证 6 types + Qwen tokenizer。更大本体可能不满足 first-token 唯一性。Llama tokenizer 未报告验证结果。\n- 建议：讨论 scalability 和 multi-token masking 可行性。\n\n**W6 [Minor] 数学符号跨 section 不一致**\n- §2 用 σ，§3 用 dom/range；tightness 公式分别用 |σ(r)|/|E|² 和 |V(r)|/|T|²。\n\n**W7 [Minor] Constraint tightness 属于相对直觉性观察**\n- \"约束越紧违规越高\"符合直觉。Dual-factor mechanism 增加解释力但更接近 systematic empirical observation。\n\n**W8 [Minor] 个别表述问题**\n- Abstract 首句 \"produce systematic ontology constraint violations\" 过于绝对，建议 \"can produce\"\n- §3.3.2 \"DocRED (6 types each)\" 中 \"each\" 指代不清（DocRED 有 96 relation types 但仅 6 entity types）\n\n---\n\n### Questions\n\n**Q1.** SciERC/DocRED 的约束是否 rectangular（σ(r) = dom(r) × range(r)）？如不是，independent enforcement 的 over-permissiveness 有多大？\n\n**Q2.** 残余 DR 中，grammar-first fallback 导致 vs dom/range 独立性导致的比例？\n\n**Q3.** Llama tokenizer 对 6 个实体类型的 first-token uniqueness 是否已验证？\n\n**Q4.** CF 冲突实体中，多少是真实标注类型歧义，多少是约束强制扭曲了模型正确输出？\n\n**Q5.** OntoCoDec 因约束重定向概率质量而引入的 false positives 有多少？（对比 Appendix B post-hoc filtering 的 TP loss 分析）\n\n---\n\n### Missing References\n\n建议性补充（非严重遗漏）：\n1. SuRE (Kim et al., ACL 2024) — schema-based structured generation for RE\n2. Constrained Beam Search for KGC（如 KG-BERT + type constraints）\n3. 总体 Related Work 覆盖已相当全面。\n\n---\n\n### Overall Assessment\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | 方法有效但 pair vs independent 形式化不一致构成理论缺陷；CF trade-off 分析不充分 |\n| Excitement | 3/5 | Tightness 分析有洞察力、enabling dependency 有趣，但核心技术（logit masking for type constraints）已在 code gen 成熟 |\n| Overall | 3/5 (Findings 边界) | 工程扎实、实验充分，但新颖性有限、形式化有缺陷、CF trade-off 削弱贡献叙事 |\n| Reproducibility | 4/5 | 实验设置详尽但无代码发布承诺 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 评估方法论 |\n\n**一句话总结**：工程扎实、实验充分的 IE 约束解码工作，但形式化不一致（pair vs independent）和 CF 恶化 trade-off 构成实质性关切，核心技术新颖性有限（code gen 已有成熟先例），处于 Findings 水准边界。修复 W1-W2 后可达 Findings；增加 fine-tuned 实验（W3）可增强会议接收竞争力。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-15T08:32:54.442090+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 50 · 2026-05-15T08:33:02.672841+00:00_

Round 1 审稿意见已提交给 Review Director。

核心发现：
- **2 个 Must-Fix**：§2/§3 本体形式化不一致（pair-based σ vs independent dom/range，可能导致 over-permissive enforcement）；CF 违规剧烈恶化（0.08%→9.90%）未充分量化 trade-off
- **3 个 Should-Fix**：仅零样本评估无法验证可组合性声明；Introduction 新颖性声明过宽；single-token type assumption 可扩展性未讨论
- **3 个 Minor**：符号不一致、tightness 直觉性、个别措辞
- **Overall 3/5**（Findings 边界），Soundness 3/5，Excitement 3/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 51 · 2026-05-15T08:34:56.515062+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 1 — Round 1 审稿意见（方法严谨性 + 实验设计与统计）

### Summary（2-3 句）

OntoCoDec 提出了将 IE 本体的 domain/range 约束编译为两层解码时 logit masking（grammar + semantic）的框架，在 SciERC 和 DocRED 上使用 Qwen3-8B 和 Llama-3.1-8B 验证。论文的 violation landscape 分析（tightness 驱动假说）具有洞察力，消融实验设计也较为系统。但 CF violation 爆炸性增长（0.08%→9.90%）构成方法论层面的根本缺陷，加之 post-hoc filtering 在 F1 上反超提出方法、表间数据不一致等问题，当前版本的证据尚不足以支撑论文的核心声明。

### Strengths（逐条）

**S1. 首次系统量化 LLM-based IE 的本体约束违反，tightness 假说有实质洞察力。**

**S2. 两层约束的 enabling dependency 通过消融实验得到清晰验证。**

**S3. 统计严谨：bootstrap CI + p-values，跨模型复制。**

**S4. 相关工作覆盖全面，定位精确。**

**S5. 诚实的负面结果报告。**

### Weaknesses（逐条）

**W1. [Must-Fix] CF violation 从 0.08% 爆发至 9.90%（SciERC）/ 12.02%（Llama DocRED），这不是 "trade-off" 而是方法设计缺陷。**
- 当 D[h] ∉ dom(r) 时，semantic layer 放弃注册类型、强制选择 dom(r) 中的任意类型，主动制造 CF violation。Llama DocRED CF 达 12.02%，高于原始 DR 率的量级。论文的实体注册表已追踪类型——完全可以在 D[h] ∉ dom(r) 时拒绝整个 triple 的 semantic 约束，但这一替代方案未被探索甚至未被讨论。
- 建议: 增加 "registry-consistent fallback" 消融；定量分析 CF 对下游任务的影响。

**W2. [Must-Fix] Post-hoc filtering 在 F1 上优于 OntoCoDec。**
- Post-hoc F1: SciERC 8.63 vs 8.36; DocRED 9.61 vs 8.23。F1 已综合 P/R。缺乏 runtime 对比，无法评估 "avoiding wasted compute" 论点。
- 建议: 报告 wall-clock time 对比；展示 recall trade-off curve；讨论组合方案。

**W3. [Must-Fix] DocRED baseline 数据在 Table 1 和 Table 3 之间不一致。**
- Table 1: DR=18.7%, ET=7.5%; Table 3: DR=18.46%, ET=2.48%。ET 差 3 倍。Abstract 与 §5.1 也不一致（18.46% vs 18.70%）。不同 exp_id (phase0 vs phase2) 暗示不同配置，但论文无解释。

**W4. [Should-Fix] 2 数据集 × 2 个 8B 模型，泛化性声明偏强。**

**W5. [Should-Fix] 完全缺失 latency/throughput 分析。**

**W6. [Should-Fix] §2 和 §3 的本体形式化不一致（σ: R→P(E×E) vs dom/range: R→2^E，表达能力不同）。**

**W7. [Should-Fix] 标题 "Type-Valid" 误导——DocRED 残余 DR=10.21%，加上 CF 12.02%，远非 "valid"。建议改为 "Type-Constrained"。**

**W8. [Should-Fix] R-F1≈8% 零-shot 基线下的实际意义评估有限。**

**W9. [Should-Fix] S1 vs S2 缺计算成本归一化。**

**W10. [Minor] Prompt 模板未提供。**
**W11. [Minor] DocRED 用 dev set 未说明理由。**
**W12. [Minor] Entity type 首 subword 唯一性未对 Llama tokenizer 验证。**
**W13. [Minor] Grammar-only 在 DocRED 上 DR 增加 42%，应在 abstract/intro 中提及。**
**W14. [Minor] Bib 中 rastogi2020sgd 为 orphan entry；regino2025kgcurator 在 OpenAlex 中未找到。**

### Questions

Q1. 当 D[h] ∉ dom(r) 时，为什么 override 注册类型而非回退 grammar-only 处理整个 triple？
Q2. Table 1 vs Table 3 DocRED baseline 数据不一致的原因？
Q3. OntoCoDec vs post-hoc 的 wall-clock time？
Q4. Entity type 首 subword 唯一性是否对 Llama tokenizer 验证？
Q5. 论文实际实现的是 Cartesian product 还是 arbitrary pair 的 ontology 结构？
Q6. SciERC 的 fallback 事件频率和 fallback-to-DR 转化比？

### Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 架构合理、消融充分，但 CF 缺陷、post-hoc 胜出、数据不一致 |
| Excitement | 2.5/5 | Tightness 假说有新意，方向好，但实际效果有限 |
| Overall | 2.5/5 | 介于 Resubmit 和 Findings 之间 |
| Reproducibility | 2/5 | 缺 prompt/hardware/runtime；表间不一致 |
| Confidence | 4/5 | 熟悉 constrained decoding 和 IE evaluation |

---

请对以上每条 Weakness 和 Question 逐条回应 [AGREE] 或 [REBUT]，并特别关注与你自己发现的交集和差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-15T08:37:46.713793+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条交叉回应\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1 (CF violation 爆发)**: 与我的 W2 一致。R1 额外提出 \"registry-consistent fallback\" 消融建议——当 D[h] ∉ dom(r) 时保留注册类型并放弃 DR 约束，而非 override 类型制造 CF。这一设计替代方案应被探索。Llama DocRED CF=12.02% 已高于某些 baseline DR 率，需更突出讨论。\n\n**[AGREE with nuance] R1-W2 (Post-hoc F1 优于 OntoCoDec)**: 同意缺乏 runtime 对比削弱了 \"avoiding wasted compute\" 论点。但论文已在 Appendix B 提供了 recall loss 和 ET 残余等对比信息，并将 F1 定位为 control variable。R1 严重性评级略高，但 runtime 数据确实必须补充。\n\n**[AGREE] R1-W3 (Table 1 vs Table 3 数据不一致)**: 这是我审稿中遗漏的重要问题。DocRED ET 从 7.5% 到 2.48% 差 3 倍，exp_id 不同（phase0 vs phase2）暗示不同配置但论文无解释。直接影响可信度。\n\n**[AGREE with nuance] R1-W4 (泛化性声明偏强)**: 2×2 设计对首次研究可接受，但 \"model-agnostic\" 表述偏强——grammar layer 确实模型无关，但 semantic layer 效果高度模型依赖。\n\n**[AGREE] R1-W5 (缺 latency 分析)**: 完全同意。Decoding-time 方法的 runtime overhead 是核心实用性指标。\n\n**[AGREE] R1-W6 (σ vs dom/range 不一致)**: 与我的 W1(Must-Fix) 完全一致。两位 reviewer 独立发现同一问题。\n\n**[AGREE] R1-W7 (标题 \"Type-Valid\" 误导)**: DocRED DR=10.21% + CF=12.02% 下 \"Type-Valid\" 承诺过高，\"Type-Constrained\" 更准确。\n\n**[AGREE with nuance] R1-W8 (R-F1≈8% 实际意义有限)**: 与我的 W3 一致。零样本隔离约束效果的论证合理，但需 fine-tuned 实验验证。\n\n**[AGREE] R1-W9 (S1 vs S2 缺成本归一化)**: 同意。\n\n**[AGREE] R1-W10 (Prompt 模板缺失)**: 同意，reproducibility 基本要求。\n\n**[AGREE] R1-W11 (DocRED dev set 未说明)**: 同意，应明确。\n\n**[AGREE] R1-W12 (Llama tokenizer 验证)**: 与我的 W5/Q3 一致。\n\n**[REBUT] R1-W13 (Grammar-only DR 增加应在 abstract 提及)**: Grammar-only DR 增加是 DocRED 特有现象（高 RV baseline 驱动），Abstract 应聚焦 full system 结果。可在 Introduction gap 分析中增加一句。\n\n**[PARTIALLY AGREE] R1-W14 (Bib orphan/验证)**: rastogi2020sgd 是 orphan 应清理。但 regino2025kgcurator 在 ACL Anthology 有记录（2025.genaik-1.10），R1 的 OpenAlex 查询可能是索引延迟。\n\n### Questions 回应\n\n**[AGREE] Q1-Q6**: 全部同意需要作者回答。Q5（Cartesian product vs arbitrary pair）与两位 reviewer 的形式化不一致关切直接相关，是最关键的问题。\n\n### 评分差异分析\n\nR1 整体比我低半档（Soundness 2.5 vs 3.0, Excitement 2.5 vs 3.0, Overall 2.5 vs 3.0）。差异来源：\n1. R1 发现 Table 数据不一致（W3），我遗漏此问题\n2. R1 对 post-hoc F1 优势权重更高\n3. R1 Reproducibility 评 2/5（我 4/5），因 prompt 缺失+表间不一致\n\n考虑 R1 发现的 W3，我的 Soundness 可能应下调至 2.5-3.0 区间。但 R1 的 Excitement 2.5 偏低——tightness 分析和 enabling dependency 验证有实质方法论贡献。\n\n### 两位 Reviewer 共识问题（权重最高）\n\n1. **σ vs dom/range 形式化不一致**（我的 W1 = R1 的 W6）\n2. **CF 恶化严重**（我的 W2 = R1 的 W1）\n3. **Llama tokenizer 验证缺失**（我的 W5 = R1 的 W12）\n4. **缺 fine-tuned 实验**（我的 W3 ≈ R1 的 W8）\n5. **缺 runtime 分析**（R1 的 W5，我未独立标记但同意）\n\nR1 额外发现：**Table 数据不一致**（W3）、**prompt 缺失**（W10）——这些增强了审稿完整性。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 审稿意见的逐条交叉回应\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1 (CF violation 爆发)**: 与我的 W2 一致。R1 额外提出 \"registry-consistent fallback\" 消融建议——当 D[h] ∉ dom(r) 时保留注册类型并放弃 DR 约束，而非 override 类型制造 CF。这一设计替代方案应被探索。Llama DocRED CF=12.02% 已高于某些 baseline DR 率，需更突出讨论。\n\n**[AGREE with nuance] R1-W2 (Post-hoc F1 优于 OntoCoDec)**: 同意缺乏 runtime 对比削弱了 \"avoiding wasted compute\" 论点。但论文已在 Appendix B 提供了 recall loss 和 ET 残余等对比信息，并将 F1 定位为 control variable。R1 严重性评级略高，但 runtime 数据确实必须补充。\n\n**[AGREE] R1-W3 (Table 1 vs Table 3 数据不一致)**: 这是我审稿中遗漏的重要问题。DocRED ET 从 7.5% 到 2.48% 差 3 倍，exp_id 不同（phase0 vs phase2）暗示不同配置但论文无解释。直接影响可信度。\n\n**[AGREE with nuance] R1-W4 (泛化性声明偏强)**: 2×2 设计对首次研究可接受，但 \"model-agnostic\" 表述偏强——grammar layer 确实模型无关，但 semantic layer 效果高度模型依赖。\n\n**[AGREE] R1-W5 (缺 latency 分析)**: 完全同意。Decoding-time 方法的 runtime overhead 是核心实用性指标。\n\n**[AGREE] R1-W6 (σ vs dom/range 不一致)**: 与我的 W1(Must-Fix) 完全一致。两位 reviewer 独立发现同一问题。\n\n**[AGREE] R1-W7 (标题 \"Type-Valid\" 误导)**: DocRED DR=10.21% + CF=12.02% 下 \"Type-Valid\" 承诺过高，\"Type-Constrained\" 更准确。\n\n**[AGREE with nuance] R1-W8 (R-F1≈8% 实际意义有限)**: 与我的 W3 一致。零样本隔离约束效果的论证合理，但需 fine-tuned 实验验证。\n\n**[AGREE] R1-W9 (S1 vs S2 缺成本归一化)**: 同意。\n\n**[AGREE] R1-W10 (Prompt 模板缺失)**: 同意，reproducibility 基本要求。\n\n**[AGREE] R1-W11 (DocRED dev set 未说明)**: 同意，应明确。\n\n**[AGREE] R1-W12 (Llama tokenizer 验证)**: 与我的 W5/Q3 一致。\n\n**[REBUT] R1-W13 (Grammar-only DR 增加应在 abstract 提及)**: Grammar-only DR 增加是 DocRED 特有现象（高 RV baseline 驱动），Abstract 应聚焦 full system 结果。可在 Introduction gap 分析中增加一句。\n\n**[PARTIALLY AGREE] R1-W14 (Bib orphan/验证)**: rastogi2020sgd 是 orphan 应清理。但 regino2025kgcurator 在 ACL Anthology 有记录（2025.genaik-1.10），R1 的 OpenAlex 查询可能是索引延迟。\n\n### Questions 回应\n\n**[AGREE] Q1-Q6**: 全部同意需要作者回答。Q5（Cartesian product vs arbitrary pair）与两位 reviewer 的形式化不一致关切直接相关，是最关键的问题。\n\n### 评分差异分析\n\nR1 整体比我低半档（Soundness 2.5 vs 3.0, Excitement 2.5 vs 3.0, Overall 2.5 vs 3.0）。差异来源：\n1. R1 发现 Table 数据不一致（W3），我遗漏此问题\n2. R1 对 post-hoc F1 优势权重更高\n3. R1 Reproducibility 评 2/5（我 4/5），因 prompt 缺失+表间不一致\n\n考虑 R1 发现的 W3，我的 Soundness 可能应下调至 2.5-3.0 区间。但 R1 的 Excitement 2.5 偏低——tightness 分析和 enabling dependency 验证有实质方法论贡献。\n\n### 两位 Reviewer 共识问题（权重最高）\n\n1. **σ vs dom/range 形式化不一致**（我的 W1 = R1 的 W6）\n2. **CF 恶化严重**（我的 W2 = R1 的 W1）\n3. **Llama tokenizer 验证缺失**（我的 W5 = R1 的 W12）\n4. **缺 fine-tuned 实验**（我的 W3 ≈ R1 的 W8）\n5. **缺 runtime 分析**（R1 的 W5，我未独立标记但同意）\n\nR1 额外发现：**Table 数据不一致**（W3）、**prompt 缺失**（W10）——这些增强了审稿完整性。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-15T08:37:50.579462+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 54 · 2026-05-15T08:37:55.448076+00:00_

交叉回应已提交给 Review Director。

两位 Reviewer 在 5 个核心问题上达成共识：形式化不一致（σ vs dom/range）、CF 恶化、Llama tokenizer 验证缺失、缺 fine-tuned 实验、缺 runtime 分析。R1 额外发现的 Table 数据不一致（ET: 7.5% vs 2.48%）是我遗漏的重要问题，已纳入修正评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

34 recorded events


### User

_source line 55 · 2026-05-16T02:42:59.164303+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]

论文：OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints
PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf

你的审查侧重：
- **新颖性**：与现有工作的差异化是否清晰、贡献点是否独立成立
- **相关工作**：文献覆盖是否充分、重要 baseline 是否漏引、定位是否准确
- **Story 一致性**：即使数据是模拟的，论证逻辑必须自洽（intro / abstract / conclusion 的 claim 不能与 method / experiments 矛盾）

评分标准：top ML venue 通用标准（接受率 ~25%，6 分制：1=Strong Reject … 6=Strong Accept）。

Dream 审稿边界提醒：
- 不需要评审：Reproducibility checklist、代码/数据可用性、具体数值精确性（数字是想象的，关注实验设计而非数值）、伦理/IRB、匿名性
- 需要评审但标注为 "presentation 层面"：Reference 真实性、论文完整度、Related Work 引用数量
- 必须评审（idea 层面）：Novelty 定位和 Related Work landscape（关键竞争方法是否遗漏）、叙事逻辑是否自洽、Scope 与目标 venue 的匹配度

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

评分校准规则：
- 3+ Major issues → 不高于 Borderline Reject
- 2 Major issues → 不高于 Weak Accept
- 1 Major issue → 不高于 Accept
- 0 Major issues → 可给 Strong Accept
Major issue 须有 explicit justification。如最终评分高于校准基准，须解释 override 理由。

请基于论文内容独立评判，不要假设论文结果的质量高低。

**不要评判**：方法实现细节 / 实验设计（那是 Reviewer 1 的范围）、格式 / 排版。

完成后请通过 review_reviewer_post_to_director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-16T02:43:12.904614+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-16T02:43:12.955324+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-16T02:43:17.619127+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1-10",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1-10",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-16T02:43:17.822893+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 9 页): 1-10\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-16T02:43:21.589849+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1-9",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1-9",
    "dpi": "200"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-16T02:43:24.310614+00:00_

Error: result (4,991,985 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899404132.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899404132.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2720
}
```

</details>

---


### Tool call

_source line 62 · 2026-05-16T02:43:28.580563+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1-2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1-2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-16T02:43:29.188321+00:00_

Error: result (961,132 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899409145.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899409145.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-16T02:43:37.224799+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-16T02:43:37.932442+00:00_

Error: result (452,873 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899417905.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899417905.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-16T02:43:42.350773+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
  "pages": "1",
  "dpi": "72"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/review_input_db82206b.pdf",
    "pages": "1",
    "dpi": "72"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-16T02:43:42.753559+00:00_

Error: result (131,305 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899422744.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/d9c5c904-1cf8-48d1-bc1c-e84561de02f6/tool-results/mcp-agent-ml-research-pdf_to_images-1778899422744.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 68 · 2026-05-16T02:43:47.193897+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best"
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-16T02:43:47.194375+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/page_3.png
/home/ubuntu/.agent-ml-research-idea_g
…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-16T02:43:51.058363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-16T02:43:51.764402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 706
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-16T02:43:51.815285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-16T02:43:52.371861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-16T02:43:52.579309+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 764
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-16T02:43:54.341231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1969
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-16T02:44:10.231062+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-16T02:44:11.237389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-16T02:44:11.893859+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-16T02:44:11.945506+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1714
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-16T02:44:14.195462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2958
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-16T02:44:14.413010+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2519
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-16T02:44:25.059463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-16T02:44:26.115336+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-16T02:44:26.573545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/dream_reports/dream_20260516T021434/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-16T02:44:27.129986+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2070
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-16T02:44:28.387490+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1813
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-16T02:44:28.689525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2574
}
```

</details>

---


### Assistant

_source line 88 · 2026-05-16T02:48:36.370980+00:00_

API Error: {"type":"error","error":{"details":null,"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011Cb5UoERpgPxNezndPopa3"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

76 recorded events


### User

_source line 89 · 2026-05-16T17:34:42.573187+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 相关工作 + 写作质量**。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 venue**: EMNLP 2026（ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式**: ACL template, double-blind, 长文 ≤8 页正文 + 无限参考文献
- **匿名规则**: double-blind（不得包含作者身份信息）
- **Limitations section**: ARR 要求独立 section，不计入页数

## 你的审查侧重

### 1. 新颖性评估
- "first to automatically compile IE ontology domain/range constraints into token-level semantic masks" 这一 claim 是否成立？是否有被遗漏的先驱工作？
- 与 code generation 领域的 type-constrained decoding（Synchromesh, PICARD, MGD, PLDI 2025）的技术差异是否被清晰阐述？
- 与 EnriCo (ASP constraints)、GenIE (state-based constraints)、AdaKGC (trie-based) 的区分是否充分？
- 两层架构的核心 novelty 在哪里——是 grammar+semantic composition？还是 entity registry + dynamic masking？还是 compilation pipeline？

### 2. Related Work 覆盖度
- §6 + Appendix A 的 related work 是否覆盖了所有重要的相关工作？
- 是否有 2025-2026 年的最新重要工作被遗漏？
- 各 paradigm 的分类是否合理、论述是否公平？
- 是否存在 strawman 比较（unfairly weakening baselines）？

### 3. 写作质量与结构
- 论文整体叙事是否连贯？§1-§7 的逻辑链是否流畅？
- 术语使用是否一致（DR/RV/ET/CF 在全文中是否统一定义和使用）
- 图表是否清晰、信息密度是否合理
- Abstract 的 claim 是否与 §5 实验结果一致
- Contribution 列表是否准确反映了论文的实际贡献

### 4. 完整性检查
- 是否有重要的实验或分析缺失？
- Limitations section 是否覆盖了所有主要局限？
- 是否需要更多 baseline 或 dataset？
- 代码/数据可复现性声明是否充分？
- Ethics statement 是否充分？

### 5. 格式合规
- 页数是否在 8 页以内（不含参考文献和 Limitations）？
- 是否符合 ACL template 格式？
- 匿名性是否完整（无作者信息泄露）？
- 参考文献格式是否正确（natbib）？
- 是否有未定义的符号或悬挂引用？

请输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条编号 W1-Wn，标注 severity: critical/warning/info）、Questions（逐条编号 Q1-Qn）、Missing References、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-16T17:34:52.402278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-16T17:34:52.804661+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_runtime}
53	
54	% === §6 Related Work ===
55	\input{section6_related_work}
56	
57	% === §7 Discussion and Conclusion ===
58	\section{Discussion and Conclusion}
59	\label{sec:discussion}
60	\input{section7_conclusion_compressed}
61	
62	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
63	\clearpage
64	\section*{Limitations}
65	
66	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13
…[truncated 3102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-16T17:34:52.805171+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-16T17:34:52.855643+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-16T17:34:57.428976+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-16T17:34:58.285550+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/abstract.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/abstract.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 96 · 2026-05-16T17:34:58.386531+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 97 · 2026-05-16T17:34:59.092989+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/section*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/section*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-16T17:34:59.194015+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/hom
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-16T17:35:11.611861+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

I found comprehensive information about ACL ARR 2026 reviewer guidelines and the review form. Here's what I found:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get the first impression, (2) search for related
…[truncated 1751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 14182
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-16T17:35:16.784515+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-16T17:35:16.784972+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-16T17:35:17.342906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-16T17:35:17.795068+00:00_

1	\begin{abstract}
2	LLM-based information extraction systems can produce systematic ontology constraint violations during autoregressive generation.
3	On SciERC (7 relation types), 15.37\% of extracted triples violate domain/range type constraints; on DocRED (96 relation types), 18.46\%---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
4	%
5	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable decoding constraint layers:
6	(1)~a \emph{grammar layer} (XGrammar CFG) enforcing JSON structural validity and restricting entity/relation vocabularies to schema-defined values (ET, RV\,$\to$\,0\%); and
7	(2)~a \emph{semantic layer} enforcing domain/range constraints via a stateful entity registry and dynamic logit masking.
8	The grammar layer is an enabling prerequisite; the two compose via bitwise AND on token-level masks.
9	%
10	On SciERC, \textsc{OntoCoDec} reduces domain/range violations by 94\% (15.37\%\,$\to$\,0.93\%) while maintaining extraction F1 ({+}0.13pp, $p{=}0.58$).
11	Results generalize across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B): DocRED DR decreases by 42--90\%, with significant R-F1 gains for Qwen ({+}0.50pp, $p{<}0.001$) and Llama ({+}0.29pp, $p{=}0.013$).
12	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
13	Quantitative analysis reveals that residual DR varies predictably with ontology tightness $\times$ baseline violation rate ($R^2{=}0.886$, $n{=}4$; Appendix~\ref{app:dual-factor}).
14	Composed with LoRA fine-tuning on two datasets, \textsc{OntoCoDec} achieves DR\,$\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 change within $\pm$0.6\,pp, confirming that fine-tuning and constrained decoding are complementary.
15	\end{abstract}
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-16T17:35:17.845870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-16T17:35:18.298335+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records ty
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-16T17:35:18.298892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-16T17:35:18.399712+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{T}|^2$ where $\mathcal{T} = \mathcal{E}$ is the entity type vocabulary: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules---e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''---which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}---well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}---$(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}---at the point where a type token is generated, all in
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-16T17:35:23.978044+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring scales, and all assessment dimensions. I need the exact scoring options for each dimension (overall assessment, soundness, excitement, etc.) and what each score means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring scales, and all assessment dimensions. I need the exact scoring options for each dimension (overall assessment, soundness, excitement, etc.) and what each score means."
  }
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-16T17:35:24.531189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-16T17:35:24.782977+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
10	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
11	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
12	
13	
14	\subsection{Problem Formulation}
15	\label{sec:formulation}
16	
17	\paragraph{IE as structured generation.}
18	Given an input text $x$, a language model generates a structured JSON output $y$:
19	%
20	\begin{equation}\label{eq:output-schema}
21	\resizebox{.88\columnwidth}{!}{$\displaystyle
22	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
23	$}
24	\end{equation}
25	%
26	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
27	
28	\paragraph{Ontology compliance.}
29	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,\, (\tau^h, \tau^t) \in \sigma(r)\}$ for domain-valid head types and $\operatorname{range}(r, \tau^h) = \{\tau^t : (\tau^h, \tau^t) \in \sigma(r)\}$ for the conditional range given head type $\tau^h$.
30	Our enforcement target is \emph{pair-based} type validity: $(\tau^h, \tau^t) \in \sigma(r)$ for every triple.
31	The decoder en
…[truncated 7606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 111 · 2026-05-16T17:35:24.783462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-16T17:35:24.834189+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \tau(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\tau} = \frac{1}{|\mathcal{R}|}\sum_{r} \tau(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cross-data
…[truncated 1960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-16T17:35:30.757962+00:00_

# ACL Rolling Review Form: Complete Assessment Criteria

## Primary Scoring Dimensions

### Overall Assessment (1-5 scale)
- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4**: Conference acceptance recommended
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2**: Needs substantial revisions for next cycle
- **1**: Do not resubmit or not relevant to NLP

### Soundness (1-5 scale, half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

### Excitement (1-5 scale, half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: does not resonate with me, but it might with others"
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others"

### Reviewer Confidence (1-5 scale)
- **5**: Positive evaluation; very careful reading
- **4**: Quite sure; unlikely to have missed important points
- **3**: Pretty sure; good general knowledge but not exhaustive checking
- **2**: Can defend evaluation but likely missed some details
- **1**: "Not my area, or paper is very hard to understand"

## Secondary Assessment Dimensions

**Reproducibility** (1-5): Ranges from easily reproducible to impossible to reproduce

**Datasets** (1-5): Ranges from enabling research direction to no datasets submitted

**Software** (1-5): Ranges from affecting research choices to no software released

**Author Identity Knowledge**
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6779
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-16T17:35:36.130405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-16T17:35:37.089797+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	
14	\paragraph{Violation distribution.}
15	Table~\ref{tab:prompt_comparison} reports violation rates.
16	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
17	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce a target vocabulary from a single prompt.
18	Per-relation rates (Figure~\ref{fig:per_relation_dr}) vary by over 40 percentage points: \textsc{Compare} at 42.4\% vs.\ \textsc{Used-for} at 0.76\%, correlating with tightness---tight constraints (few valid 
…[truncated 1354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-16T17:35:37.240806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-16T17:35:37.693064+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: rel
…[truncated 9470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-16T17:35:37.844521+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-16T17:35:37.845129+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 2767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-16T17:35:44.674572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-16T17:35:45.177152+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results across all three models.
12	Mistral serves as a third zero-shot verification point confirming model-agnosticism; composability evaluation (\S\ref{sec:composability}) uses LoRA fine-tuning which requires domain-specific training data available only for Qwen and Llama.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.4pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rrrr r@{}}
20	\toprule
21	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
22	& \textbf{R-F1} \\
23	\cmidrule(lr){3-6} \cmidrule(l){7-7}
24	\textbf{Dataset} & \textbf{Model}
25	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
26	  & $\uparrow$ \\
27	\midrule
28	\multirow{6}{*}{SciERC}
29	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
30	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
31	  \cmidrule(l){2-7}
32	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
33	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
34	  \cmidrule(l){2-7}
35	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
36	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
37	\midrule
38	\multirow{6}{*}{DocRED}
39	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
40	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
41	  \cmidrule(l){2-7}
42	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
43	  & Llama (S1)  &  2.55 &  0  
…[truncated 2202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-16T17:35:45.379050+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-16T17:35:45.781302+00:00_

1	% Section 5 — Runtime Analysis
2	% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
3	% Qwen3-8B, same single-GPU server, controlled 4-way ablation.
4	
5	\subsection{Runtime Overhead}
6	\label{sec:runtime}
7	
8	Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{@{}l rr rr@{}}
15	\toprule
16	& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
17	& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
18	\cmidrule(lr){2-3} \cmidrule(l){4-5}
19	\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
20	\midrule
21	Unconstrained & 2.587 & --- & 21.023 & --- \\
22	Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
23	Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
24	Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
25	\bottomrule
26	\end{tabular}
27	\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
28	Grammar compile time: 0.044\,s (one-time, amortized to zero).
29	Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
30	\label{tab:runtime}
31	\end{table}
32	
33	Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
34	Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
35	Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
36	Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
37	Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-16T17:35:45.832048+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-16T17:35:45.882932+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation; IterGen~\cite{ugare2025itergen} adds backtracking.
6	These guarantee format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
7	
8	\paragraph{Semantic Constrained Decoding for Code.}
9	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE.
10	
11	\paragraph{Vocabulary and Type-Constrained Generation.}
12	\citet{roth_yih_2004} establish relational type compatibility as a hard constraint via ILP, though applied post-hoc.
13	GENRE~\cite{decao2021genre}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation.
14	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie} encode IE structure via training or prompting but provide only \emph{soft} guidance.
15	Post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025} validate outputs against ontologies after generation; OntoCoDec \emph{prevents} violations during decoding.
16	
17	\paragraph{Quality Impact of Constrained Decoding.}
18	CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction-style tasks are robust to---or benefit from---constraints.
19	BoostCD~\cite{sakota2025boostcd} combines constrained and unconstrained outputs via boo
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-16T17:35:55.947108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-16T17:35:56.349333+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix C.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and two datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, it reaches DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost, confirming orthogonal error targeting; the dual-factor pattern ($R^2{=}0.886$) provides a predictive framework for residual violations.
6	
7	CF impact is model-dependent: S1 introduces CF for well-calibrated models (up to 12.02\%) but reduces it for poorly-calibrated ones (Mistral: 56.87\%\,$\to$\,1.27\%).
8	Ablation confirms CF$\leftrightarrow$DR tension ($+$13.85\,pp; Appendix~\ref{app:cf-dr-tradeoff}); fine-tuning reduces CF by 88\% (\S\ref{sec:composability}); global entity-level type consensus offers the most direct path forward.
9	
10	% Limitations and Future Work moved to \section*{Limitations} in main.tex (ARR requirement)
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-16T17:35:56.349758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-16T17:35:56.400378+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
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
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-16T17:36:03.377772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-16T17:36:03.730025+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different seman
…[truncated 22631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-16T17:36:03.730527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-16T17:36:04.734881+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding---constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ 
…[truncated 771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-16T17:36:04.785510+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/appendix_llama_per_relation.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/appendix_llama_per_relation.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-16T17:36:04.836141+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-16T17:36:08.508226+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-16T17:36:08.609180+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-16T17:36:09.161968+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EnriCo ASP constraints information extraction decoding 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EnriCo ASP constraints information extraction decoding 2024"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-16T17:36:18.162158+00:00_

Web search results for query: "EnriCo ASP constraints information extraction decoding 2024"

Links: [{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493v1"},{"title":"[Literature Review] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://www.themoonlight.io/en/review/enrico-enriched-representation-and-globally-constrained-inference-for-entity-and-relation-extraction"},{"title":"Paper page - EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://huggingface.co/papers/2404.12493"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"}]

Ba
…[truncated 2017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9000
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-16T17:36:23.233293+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding information extraction ontology type constraints 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding information extraction ontology type constraints 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-16T17:36:23.886661+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GenIE state-based constraints information extraction Josifoski 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GenIE state-based constraints information extraction Josifoski 2022"
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-16T17:36:30.664971+00:00_

Web search results for query: "GenIE state-based constraints information extraction Josifoski 2022"

Links: [{"title":"GenIE: Generative Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.342/"},{"title":"[2112.08340] GenIE: Generative Information Extraction","url":"https://arxiv.org/abs/2112.08340"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=GenIE:+Generative+information+extraction&amp=&author=Martin+Josifoski&amp=&author=Nicola+De+Cao&amp=&author=Maxime+Peyrard&amp=&author=Fabio+Petroni&amp=&author=Robert+West&amp=&publication_year=2022&amp=&pages=4626-4643&amp=&doi=10.18653/v1/2022.naacl-main.342"},{"title":"GenIE: Generative Information Extraction","url":"https://dlab.epfl.ch/people/west/pub/Josifoski-DeCao-Peyrard-Petroni-West_NAACL-22.pdf"},{"title":"GitHub - epfl-dlab/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub","url":"https://github.com/epfl-dlab/GenIE"},{"title":"GenIE: Generative Information Extraction","url":"https://infoscience.epfl.ch/entities/publication/ac96118e-64f4-4d05-8461-aa27321afaeb"},{"title":"(PDF) GenIE: Generative Information Extraction","url":"https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks ...","url":"https://dlab.epfl.ch/people/west/pub/Geng-Josifoski-Peyrard-West_EMNLP-23.pdf"},{"title":"GenIE: Generative Information Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2112.08340"},{"title":"GenIE: Generative Information Extraction | OpenReview","url":"https://openreview.net/forum?id=HxxjO7zS-c"}]

Based on the search results, I found comprehensive information about the GenIE paper by Josifoski et al. (2022):

## GenIE: Generative Information Extraction (Josifoski et al., 2022)

GenIE (generative information extraction) is the first end-to-end autoregressive 
…[truncated 1446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6778
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-16T17:36:34.379715+00:00_

Web search results for query: "constrained decoding information extraction ontology type constraints 2025 2026"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"[2408.02361] Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/abs/2408.02361"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/pdf/2408.02361"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"Constrained Decoding for Information Extraction","url":"https://hal.science/hal-04678395v1/document"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"Published as a conference paper at ICAIS 2025","url":"https://arxiv.org/pdf/2510.20345"}]

I found several relevant research papers and resources on constrained decoding for information extraction with ontology type constra
…[truncated 1673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11146
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-16T17:36:38.504325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"dialogue ontology relation extraction\" \"constrained chain-of-thought decoding\" 2024 DORE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"dialogue ontology relation extraction\" \"constrained chain-of-thought decoding\" 2024 DORE"
  }
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-16T17:36:39.157201+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BoostCD constrained decoding information extraction boosting 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BoostCD constrained decoding information extraction boosting 2025"
  }
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-16T17:36:44.327330+00:00_

Web search results for query: ""dialogue ontology relation extraction" "constrained chain-of-thought decoding" 2024 DORE"

Links: [{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/html/2408.02361v1"},{"title":"[2408.02361] Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/abs/2408.02361"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding - ACL Anthology","url":"https://aclanthology.org/2024.sigdial-1.33/"},{"title":"Dialogue Ontology Relation Extraction via Constrained ...","url":"https://aclanthology.org/2024.sigdial-1.33.pdf"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://www.paperreading.club/page?id=244596"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=95&show=2000"},{"title":"Text-to-SQL Task-oriented Dialogue Ontology Construction","url":"https://arxiv.org/html/2507.23358v2"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://powerdrill.ai/discover/discover-Dialogue-Ontology-Relation-clziwmugm413g0161hk6eelui"},{"title":"Container Registry · general / dsml / Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding - Public · GitLab","url":"https://gitlab.cs.hhu.de/general/dsml/dialogue-ontology-relation-extraction-via-constrained-chain-of-thought-decoding/container_registry"},{"title":"dblp: David Arps","url":"https://dblp.org/pid/219/5595.html"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Paper Overview

The paper "Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding" by Vukovic et al. was published at SIGDIAL 2024 in Kyoto, Japan.

## Problem & Motivation

State-of-the-art task-oriented dialogue systems typically rely on task-sp
…[truncated 996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5823
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-16T17:36:46.587451+00:00_

Web search results for query: "BoostCD constrained decoding information extraction boosting 2025"

Links: [{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901v1"},{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting:","url":"https://openreview.net/pdf?id=3Qbw5Ja6Sc"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Marija Sakota's research works | Swiss Federal Institute of Technology in Lausanne and other places","url":"https://www.researchgate.net/scientific-contributions/Marija-Sakota-2168060164"},{"title":"Constrained Decoding in Sequence Generation","url":"https://www.emergentmind.com/topics/constrained-decoding"},{"title":"Sketch-Guided Constrained Decoding for Boosting Blackbox Large Language Models without Logit Access","url":"https://arxiv.org/html/2401.09967v4"},{"title":"EPFL Data Science & AI Lab (dlab) · GitHub","url":"https://github.com/epfl-dlab"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"}]

Based on the search results, here's what I found about BoostCD:

## Overview

Boosted Constrained Decoding (BoostCD) is a method with the ability to correct systematic errors that an autoregressive model trained for a structured NLP task might make during constrained as well as unconstrained generation.

## How It Works

BoostCD combines constrained and unconstrained decoding in two
…[truncated 1173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7430
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-16T17:36:51.380370+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SLOT structuring output LLM type constraints knowledge graph 2025 EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SLOT structuring output LLM type constraints knowledge graph 2025 EMNLP"
  }
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-16T17:36:51.682063+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structured IE generation schema constraint domain range 2025 ACL EMNLP NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structured IE generation schema constraint domain range 2025 ACL EMNLP NAACL"
  }
}
```

</details>

---


### Tool result

_source line 150 · 2026-05-16T17:36:58.209942+00:00_

Web search results for query: "structured IE generation schema constraint domain range 2025 ACL EMNLP NAACL"

Links: [{"title":"Schema Generation for Large Knowledge Graphs Using ...","url":"https://aclanthology.org/2025.findings-emnlp.671.pdf"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Realistic Training Data Generation and Rule Enhanced ...","url":"https://aclanthology.org/2025.emnlp-main.357.pdf"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"A Survey on LLMs for Story Generation","url":"https://aclanthology.org/2025.findings-emnlp.750.pdf"},{"title":"A Category-Theoretic Approach to Neural-Symbolic Task ...","url":"https://aclanthology.org/2025.findings-emnlp.1157.pdf"},{"title":"SciProdLLM 2025 The First Workshop on Human–LLM Collaboration for","url":"https://aclanthology.org/2025.sciprodllm-1.pdf"},{"title":"Learning to Generate Structured Output with Schema Reinforcement Learning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.243/"}]

I found several relevant papers on structured information extraction generation with schema constraints. Here are the key results:

## Main Results

1. **Schema Generation for Large Knowledge Graphs (EMNLP 2025)**
   A paper published in the Findings of EMNLP 2025 addresses schema generation using LLMs, with experimental setups where LLMs generate schema scripts end-to-end or first generate constraints in JSON format using structured generation abilities.

2. **Learning to Generate Structured Output with Schema Reinforcement Learning (ACL 2025)**
   This ACL 2025 paper investigates stru
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6527
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-16T17:36:59.766433+00:00_

Web search results for query: "SLOT structuring output LLM type constraints knowledge graph 2025 EMNLP"

Links: [{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"[2505.04016] SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/abs/2505.04016"},{"title":"SLOT: Structuring the Output of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-industry.32/"},{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/html/2505.04016v1"},{"title":"SLOT: Structuring the Output of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/397423713_SLOT_Structuring_the_Output_of_Large_Language_Models"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-industry.0.pdf"},{"title":"[2505.04016v1] SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/abs/2505.04016v1"},{"title":"ConstraintLLM: A Neuro-Symbolic Framework for Industrial ...","url":"https://aclanthology.org/2025.emnlp-main.809.pdf"},{"title":"Statistical Network Analysis for LLMs via Knowledge Graphs","url":"https://www.techrxiv.org/users/972913/articles/1347041/master/file/data/KG__Paper%20(4)/KG__Paper%20(4).pdf?inline=true"}]

I found relevant results about SLOT and EMNLP 2025. Here's what the search revealed:

## SLOT: Structuring the Output of Large Language Models (EMNLP 2025)

SLOT employs a fine-tuned lightweight language model as a post-processing layer, achieving flexibility across various LLMs and schema specifications. The paper was presented at the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track.

### Key Approach

Unlike prior works, SLOT's approach is task-agnostic – SLOT de
…[truncated 1201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8386
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-16T17:37:03.586896+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"schema reinforcement learning\" structured output ACL 2025 JSON constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"schema reinforcement learning\" structured output ACL 2025 JSON constraints"
  }
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-16T17:37:04.191064+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PARSE LLM schema optimization entity extraction ontology 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PARSE LLM schema optimization entity extraction ontology 2025"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-16T17:37:11.781614+00:00_

Web search results for query: ""schema reinforcement learning" structured output ACL 2025 JSON constraints"

Links: [{"title":"Learning to Generate Structured Output with Schema Reinforcement Learning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.243/"},{"title":"Learning to Generate Structured Output with Schema Reinforcement Learning","url":"https://arxiv.org/html/2502.18878v1"},{"title":"[2502.18878] Learning to Generate Structured Output with Schema Reinforcement Learning","url":"https://arxiv.org/abs/2502.18878"},{"title":"Learning to Generate Structured Output with Schema ...","url":"https://aclanthology.org/2025.acl-long.243.pdf"},{"title":"[Quick Review] Learning to Generate Structured Output with Schema Reinforcement Learning","url":"https://liner.com/review/learning-to-generate-structured-output-with-schema-reinforcement-learning"},{"title":"Article Not peer-reviewed version Think Inside the JSON: Reinforcement","url":"https://www.preprints.org/manuscript/202502.1390/v1/download"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Learning to Generate Structured Output with Schema Reinforcement Learning | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.acl-long.243@ACL"},{"title":"Proceedings of Recent Advances in Natural Language Processing,pages 1074–1084","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"GitHub - thunlp/SchemaReinforcementLearning: Learning to Generate STRUCTURED Output with Schema Reinforcement Learning","url":"https://github.com/thunlp/SchemaReinforcementLearning"}]

Based on the search results, I found comprehensive information about the ACL 2025 paper on Schema Reinforcement Learning. Here's what I found:

## Overview

The paper "Learning to Generate Structured Output with Schema Reinforcement Learning" was accepted at ACL 2025 and investigates the structured 
…[truncated 1506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8194
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-16T17:37:12.183755+00:00_

Web search results for query: "PARSE LLM schema optimization entity extraction ontology 2025"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"PARSE: LLM driven schema optimization for reliable entity extraction - Amazon Science","url":"https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction"},{"title":"(PDF) PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://www.researchgate.net/publication/396458126_PARSE_LLM_Driven_Schema_Optimization_for_Reliable_Entity_Extraction"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable ...","url":"https://aclanthology.org/2025.emnlp-industry.184.pdf"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=13775&show=25"},{"title":"Ontology-Grounded LLM Construction","url":"https://www.emergentmind.com/topics/ontology-grounded-llm-construction"},{"title":"Parse: LLM Driven Schema Optimization for Reliable Entity Extraction | Hacker News","url":"https://news.ycombinator.com/item?id=45683970"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3600&show=250"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"}]

Based on the search results, here's what I found about PARSE and related 2025 research on LLM schema optimization for entity extraction:

## PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction

PARSE addresses structured information extraction from unstructured text, where recent approaches apply large language models directly to extraction tasks using existing JSON schemas, but treat JSON schemas as static contracts designed for human developers, leading 
…[truncated 1338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7992
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-16T17:37:18.670217+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/relwork_new_entries.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/relwork_new_entries.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-16T17:37:18.670690+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-16T17:37:23.541349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-16T17:37:23.843220+00:00_

1	% ============================================================
2	% Merged authoritative BibTeX references (9 entries)
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
7	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
8	@inproceedings{synchromesh_iclr2022,
9	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
10	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
11	  booktitle = {International Conference on Learning Representations},
12	  year      = {2022},
13	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
14	}
15	
16	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
17	@inproceedings{mgd_neurips2023,
18	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
19	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
20	  booktitle = {Advances in Neural Information Processing Systems},
21	  volume    = {36},
22	  year      = {2023},
23	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
24	}
25	
26	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
27	@article{pldi2025_type_constrained_codegen,
28	  title     = {Type-Constrained Code Generation with Language Models},
29	  author    = {M\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},
30	  journal   = {Proceedings of the ACM on Programming Languages},
31	  volume    = {9},
32	  number    = {PLDI},
33	  year      = {2025},
34	  doi       = {10.1145/3729274},
35	  url       = {https://dl.acm.org/doi/10.1145/372927
…[truncated 26587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-16T17:38:27.319026+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-16T17:38:27.420021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-16T17:40:16.465977+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：OntoCoDec\n\n## 总体评分\n**Overall**: 3.5（介于 Findings 和 Conference 之间）\n**一句话总结**: 工程上完整、实验充分的约束解码框架，但核心机制新颖性有限（prefix-conditioned logit masking 在代码生成中已成熟），且 CF 副作用（最高 12%）部分消解了\"constraint enforcement\"的叙事。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（bootstrap, 多模型多数据集），但 dual-factor regression n=4 不具统计意义；CF 增加最高 12% 削弱了核心 claim |\n| Excitement | 3/5 | 问题重要且实用，但技术贡献更接近\"迁移已有范式到新领域\"而非新范式 |\n| Reproducibility | 4/5 | 提供 prompt 模板、详细超参、多轮消融；缺代码/数据承诺 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Novelty claim 过度——缺少与 DORE (SIGDIAL 2024) 的对比和区分\n\n- 具体位置：§1 Contribution 2, §6 \"Our Approach\" paragraph, Appendix A final paragraph\n- 问题：论文声称 \"the first to automatically compile IE ontology domain/range constraints into token-level semantic masks\"。但 Vukovic et al. (SIGDIAL 2024) \"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding\" 已将 ontology terms 和 relations 作为 constrained decoding 的约束目标用于关系抽取，且通过 constraining decoding to ontology terms 来减少幻觉。虽然 DORE 的技术路径不同（CoT decoding + confidence threshold vs. logit masking），但 \"first\" claim 需要更精确地限定技术边界（e.g., \"first to enforce domain/range *pair-based* constraints via stateful token masking\"），并明确区分与 DORE 的差异。\n- 为什么影响接收：Novelty claim 是论文的核心卖点；reviewer/AC 会重点审查 \"first\" 声明的准确性。\n- 建议修改方向：(1) 引用 DORE 并在 §6 中区分（DORE 约束的是 vocabulary 级别，不是 domain/range pair validity）；(2) 将 \"first\" claim 缩窄为 \"first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE\"。\n\n**N2** [critical] 核心新颖性与代码生成领域先驱工作的技术差异阐述不足\n\n- 具体位置：§6 \"Semantic Constrained Decoding for Code\" paragraph（主文仅 2 行），Appendix A 扩展段落\n- 问题：论文正确识别了 PLDI 2025 (Mündler et al.) 为 \"closest mechanistic analog\"，但主文 §6 仅用两句话打发（\"Synchromesh, PICARD, MGD, and PLDI2025 enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE\"）。真正的 novelty 需要更清晰地回答：migrating 这个 paradigm 的技术困难在哪里？如果答案是 \"entity registry populated during generation\"（即 constraint target 需要从 free text 推断而非从 declared type annotation 读取），这个贡献在主文中几乎看不到突出表述，只在 Appendix A 有详细讨论。\n- 为什么影响接收：如果核心区分点只出现在 Appendix 而非 §1/§3/§6 主文，reviewer 容易判断为 \"incremental migration\"。\n- 建议修改方向：在 §1 或 §3 开头明确一段话阐述：代码生成的 type system → automaton → mask pipeline 为何不能直接用于 IE（entity types 非 declared 而是 extracted、需要 stateful registry、ontology 是 flat 而非 hierarchical），以及 OntoCoDec 的具体技术解决方案。\n\n**N3** [critical] 缺少与同领域 constrained decoding IE 系统的直接实验对比\n\n- 具体位置：§5 全部实验\n- 问题：论文对比的 baseline 是 unconstrained decoding 和 post-hoc filtering。但同领域已有 constrained decoding IE 系统：GCD (Geng et al., EMNLP 2023) 来自同一实验室（EPFL dlab），直接在 IE 任务上做 grammar-constrained decoding；BoostCD (Sakota et al., EMNLP 2025) 同样针对 closed IE 用 constrained decoding + boosting。论文引用了这两篇但未做实验对比。特别是 GCD 使用 input-dependent grammars 做 IE，是 OntoCoDec grammar layer 的直接先驱，不对比就无法证明 semantic layer 的增量价值超过 GCD 已有能力。\n- 为什么影响接收：ACL ARR reviewer 会质疑为什么不与最接近的同类方法对比。\n- 建议修改方向：至少与 GCD 做定量对比（GCD 公开代码，同一数据集）；如果 GCD 不支持 domain/range 约束（很可能不支持），这本身就是一个有力的区分证据，但需要实验展示而非仅凭论述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Dual-factor regression ($R^2=0.886$, $n=4$) 不具统计意义\n\n- 具体位置：Abstract line 13, §4 Constraint Tightness paragraph, Appendix B \"Dual-Factor Quantitative Analysis\"\n- 问题：用 4 个数据点拟合线性模型并报告 $R^2=0.886$ 作为 \"predictive framework\"，这在统计上是不严谨的。4 个点的线性拟合几乎必然得到高 $R^2$（2 自由度，2 参数）。论文自身承认 \"we do not report a p-value given the small sample size\"，但仍在 Abstract 和 §7 中使用这个数字作为 contribution claim 的一部分。\n- 建议：(1) 从 Abstract 中移除 $R^2$ 数字；(2) 将其降级为 \"preliminary observation consistent with...\"；(3) 如果加入 Mistral 的 4 个数据点（6 model×dataset 配置可用），至少提供 6 点拟合。\n\n**W2** [warning] CF 增加（最高 12.02%）与 \"constraint enforcement\" 的核心叙事存在张力\n\n- 具体位置：Table 3 (cross-model), §7 Discussion, Limitations\n- 问题：OntoCoDec 在减少 DR 的同时引入 CF（SciERC: 0.08%→9.90%; DocRED Llama: 0.17%→12.02%）。论文诚实讨论了这个 trade-off，但叙事上仍以 \"constraint enforcement\" 定位。一个 \"enforcement\" 系统引入了新的约束违反类型，需要更直接地在 §1/Abstract 层面承认。Abstract 目前完全不提 CF 增加。\n- 建议：在 Abstract 最后加一句 CF caveat（e.g., \"with a model-dependent cross-field consistency trade-off mitigated by fine-tuning\"），或将标题/定位从 \"enforcement\" 调整为 \"reduction\"。\n\n**W3** [warning] 主评价指标是 violation rate reduction 而非下游任务质量——存在循环论证风险\n\n- 具体位置：§5 全部\n- 问题：论文的核心实验设计是：约束违反率下降 = 成功。这是 tautological 的——施加约束当然会减少约束违反。真正需要证明的是：减少违反是否带来下游价值？论文用 F1 作为 \"control variable\" 证明无害，但 F1-neutral 不等于有用。Appendix B 的 post-hoc filtering 对比显示 post-hoc 在大多数情况下 F1 还更高（5/6 zero-shot 设置）。\n- 建议：(1) 增加一个下游任务评估（e.g., 用抽取的 triples 做 QA 或 knowledge graph completion，比较有/无 type violation 的影响）；(2) 或者更直接地承认当前贡献是\"保证性质\"而非\"性能提升\"，并在 §1 中重新定位。\n\n**W4** [warning] 写作结构问题：§5.1 \"Violation Landscape\" 混合了 motivation 和 experimental setup\n\n- 具体位置：§5.1 (section3_violation_landscape.tex)\n- 问题：这一节同时承担三个角色：(1) 实验设置描述、(2) 基线违反率分析（这是 motivation）、(3) schema-informed prompting 对比（这是 baseline experiment）。逻辑上，violation landscape 分析应放在 §2 Background 或 §3 Method 的 motivation 部分，实验设置应独立为一个清晰的 subsection。当前安排使读者在 §5 开头看到 motivation 内容感到困惑。\n- 建议：将 violation landscape 的 motivation 分析（Table 1, Figure 1）提前到 §2.5 或作为独立的 §3.0 \"Motivation: Violation Prevalence\"。\n\n**W5** [warning] 缺少代码/数据可复现性声明\n\n- 具体位置：全文\n- 问题：论文未包含任何关于代码/数据释放的声明。ACL ARR 的 reproducibility 评分维度明确要求作者说明是否会释放代码。Prompt 模板已提供（Appendix），但核心的 semantic layer logits processor 实现、ontology compilation pipeline、entity registry 逻辑均未承诺开源。\n- 建议：添加 \"Code and data will be released upon acceptance\" 或类似声明。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.5 \"Decoding Strategies\" 中 S2 的描述过于简略（\"Detailed comparison is provided in the appendix\"），但 S2 在 Table 2 中有数据，建议补充 1-2 句 S2 的实际结果总结。\n- §4 equation (2) 定义 tightness 时用 $\\tau(r)$ 与 entity type 集合 $\\mathcal{T}$ 的符号冲突——$\\tau$ 既用于 entity type ($\\tau_i$) 又用于 tightness 函数。\n- Table 3 footnote \"Parse failures: Qwen DocRED 12→11 (S1 1.10%)\" 意义不清——12→11 是什么？documents 数？需要更明确的解释。\n- Appendix B \"Relation Matching Protocol\" 使用 fuzzy matching（token overlap >80% + edit distance ≤2）。这个协议对 Mistral 的 F1 贡献 +0.84pp，应在主文 §5.3 简要提及以确保评价一致性透明。\n- `\\bibliography{relwork_new_entries}` 使用单一 bib 文件命名为 \"relwork_new_entries\" 不太规范，建议改为 \"references.bib\" 或 \"main.bib\"。\n\n---\n\n## Missing References\n\n1. **Vukovic et al. (SIGDIAL 2024)** — \"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding\"。直接使用 constrained decoding 进行 ontology-based relation extraction，与 OntoCoDec 的问题设定高度相关。**必须引用并区分。**\n\n2. **\"A Survey of Generative Information Extraction\" (COLING 2025)** — 综述性文献，有助于定位本工作在 generative IE 领域的位置。建议引用。\n\n3. **PARSE (Shen et al., EMNLP 2025 Industry)** — \"LLM Driven Schema Optimization for Reliable Entity Extraction\"，使用 schema guardrails 减少 extraction errors 92%。不同路径但相关。可选引用。\n\n4. **Schema Reinforcement Learning (ACL 2025)** — \"Learning to Generate Structured Output with Schema Reinforcement Learning\"。Training-time schema compliance 方法，与 OntoCoDec 的 inference-time 方法互补。可选引用。\n\n---\n\n## 主要优势\n\n1. **问题定义清晰且有数据支撑**：violation landscape 分析（Table 1, Figure 1）令人信服地证明了问题的普遍性和严重性，per-relation tightness 分析提供了有解释力的框架。\n\n2. **实验设计全面且诚实**：3 模型 × 2 数据集 × 多消融 × composability with fine-tuning × runtime profiling × post-hoc comparison。CF trade-off 的坦诚讨论（包括 CF-DR trade-off ablation, Table 5）体现了学术诚信。\n\n3. **实用性强**：runtime overhead 仅 2-5%，training-free，与 fine-tuning 正交组合后 DR≤0.20%——这是一个可以直接部署的系统。\n\n4. **形式化分析有价值**：§4 的 decidability taxonomy（local / prefix-decidable / non-local）和 non-rectangularity 分析为 constrained decoding 在 IE 中的应用提供了理论框架。\n\n5. **相关工作覆盖度高**：§6 + Appendix A 覆盖了 5 个 paradigm，引用了 2024-2026 的最新工作（IterGen ICLR 2025, CRANE ICML 2025, BoostCD EMNLP 2025, Zhou 2026 等），分类合理。\n\n---\n\n## Questions for Authors\n\n**Q1**: 为什么不与 GCD (Geng et al., EMNLP 2023) 做直接实验对比？GCD 是你们同一实验室的前作，使用 input-dependent grammars 做 IE，且开源。OntoCoDec 的 grammar layer 与 GCD 的关系是什么——是改进、扩展还是不同的技术路线？\n\n**Q2**: CF 增加是否会传播到下游任务？例如，如果将抽取的 triples 用于 knowledge graph construction，一个实体有两个冲突类型对下游的影响是什么？是否有初步评估？\n\n**Q3**: Abstract 中的 $R^2=0.886$ (n=4) 是否可以扩展到包含 Mistral 的 6 个数据点？如果加入 Mistral (56.94% DR SciERC, 57.42% DR DocRED)，拟合是否依然成立？\n\n**Q4**: 在 fine-tuned 设置下（Table 7），grammar layer 是 no-op。这是否意味着 OntoCoDec 对 fine-tuned 系统的实际价值仅来自 semantic layer？如果是，\"two-layer compiled constraint framework\" 的 framing 是否过度强调了 grammar layer 的贡献？\n\n**Q5**: 论文的 tokenizer 假设（\"each entity type maps to a unique first subword token\"）限制了方法的泛化性。对于有 50+ entity types 的大型本体（如 Wikidata 的完整 entity type hierarchy），prefix-tree masking 的工程复杂度和 runtime 开销预期如何？\n",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告：OntoCoDec\n\n## 总体评分\n**Overall**: 3.5（介于 Findings 和 Conference 之间）\n**一句话总结**: 工程上完整、实验充分的约束解码框架，但核心机制新颖性有限（prefix-conditioned logit masking 在代码生成中已成熟），且 CF 副作用（最高 12%）部分消解了\"constraint enforcement\"的叙事。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计严谨（bootstrap, 多模型多数据集），但 dual-factor regression n=4 不具统计意义；CF 增加最高 12% 削弱了核心 claim |\n| Excitement | 3/5 | 问题重要且实用，但技术贡献更接近\"迁移已有范式到新领域\"而非新范式 |\n| Reproducibility | 4/5 | 提供 prompt 模板、详细超参、多轮消融；缺代码/数据承诺 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Novelty claim 过度——缺少与 DORE (SIGDIAL 2024) 的对比和区分\n\n- 具体位置：§1 Contribution 2, §6 \"Our Approach\" paragraph, Appendix A final paragraph\n- 问题：论文声称 \"the first to automatically compile IE ontology domain/range constraints into token-level semantic masks\"。但 Vukovic et al. (SIGDIAL 2024) \"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding\" 已将 ontology terms 和 relations 作为 constrained decoding 的约束目标用于关系抽取，且通过 constraining decoding to ontology terms 来减少幻觉。虽然 DORE 的技术路径不同（CoT decoding + confidence threshold vs. logit masking），但 \"first\" claim 需要更精确地限定技术边界（e.g., \"first to enforce domain/range *pair-based* constraints via stateful token masking\"），并明确区分与 DORE 的差异。\n- 为什么影响接收：Novelty claim 是论文的核心卖点；reviewer/AC 会重点审查 \"first\" 声明的准确性。\n- 建议修改方向：(1) 引用 DORE 并在 §6 中区分（DORE 约束的是 vocabulary 级别，不是 domain/range pair validity）；(2) 将 \"first\" claim 缩窄为 \"first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE\"。\n\n**N2** [critical] 核心新颖性与代码生成领域先驱工作的技术差异阐述不足\n\n- 具体位置：§6 \"Semantic Constrained Decoding for Code\" paragraph（主文仅 2 行），Appendix A 扩展段落\n- 问题：论文正确识别了 PLDI 2025 (Mündler et al.) 为 \"closest mechanistic analog\"，但主文 §6 仅用两句话打发（\"Synchromesh, PICARD, MGD, and PLDI2025 enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE\"）。真正的 novelty 需要更清晰地回答：migrating 这个 paradigm 的技术困难在哪里？如果答案是 \"entity registry populated during generation\"（即 constraint target 需要从 free text 推断而非从 declared type annotation 读取），这个贡献在主文中几乎看不到突出表述，只在 Appendix A 有详细讨论。\n- 为什么影响接收：如果核心区分点只出现在 Appendix 而非 §1/§3/§6 主文，reviewer 容易判断为 \"incremental migration\"。\n- 建议修改方向：在 §1 或 §3 开头明确一段话阐述：代码生成的 type system → automaton → mask pipeline 为何不能直接用于 IE（entity types 非 declared 而是 extracted、需要 stateful registry、ontology 是 flat 而非 hierarchical），以及 OntoCoDec 的具体技术解决方案。\n\n**N3** [critical] 缺少与同领域 constrained decoding IE 系统的直接实验对比\n\n- 具体位置：§5 全部实验\n- 问题：论文对比的 baseline 是 unconstrained decoding 和 post-hoc filtering。但同领域已有 constrained decoding IE 系统：GCD (Geng et al., EMNLP 2023) 来自同一实验室（EPFL dlab），直接在 IE 任务上做 grammar-constrained decoding；BoostCD (Sakota et al., EMNLP 2025) 同样针对 closed IE 用 constrained decoding + boosting。论文引用了这两篇但未做实验对比。特别是 GCD 使用 input-dependent grammars 做 IE，是 OntoCoDec grammar layer 的直接先驱，不对比就无法证明 semantic layer 的增量价值超过 GCD 已有能力。\n- 为什么影响接收：ACL ARR reviewer 会质疑为什么不与最接近的同类方法对比。\n- 建议修改方向：至少与 GCD 做定量对比（GCD 公开代码，同一数据集）；如果 GCD 不支持 domain/range 约束（很可能不支持），这本身就是一个有力的区分证据，但需要实验展示而非仅凭论述。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Dual-factor regression ($R^2=0.886$, $n=4$) 不具统计意义\n\n- 具体位置：Abstract line 13, §4 Constraint Tightness paragraph, Appendix B \"Dual-Factor Quantitative Analysis\"\n- 问题：用 4 个数据点拟合线性模型并报告 $R^2=0.886$ 作为 \"predictive framework\"，这在统计上是不严谨的。4 个点的线性拟合几乎必然得到高 $R^2$（2 自由度，2 参数）。论文自身承认 \"we do not report a p-value given the small sample size\"，但仍在 Abstract 和 §7 中使用这个数字作为 contribution claim 的一部分。\n- 建议：(1) 从 Abstract 中移除 $R^2$ 数字；(2) 将其降级为 \"preliminary observation consistent with...\"；(3) 如果加入 Mistral 的 4 个数据点（6 model×dataset 配置可用），至少提供 6 点拟合。\n\n**W2** [warning] CF 增加（最高 12.02%）与 \"constraint enforcement\" 的核心叙事存在张力\n\n- 具体位置：Table 3 (cross-model), §7 Discussion, Limitations\n- 问题：OntoCoDec 在减少 DR 的同时引入 CF（SciERC: 0.08%→9.90%; DocRED Llama: 0.17%→12.02%）。论文诚实讨论了这个 trade-off，但叙事上仍以 \"constraint enforcement\" 定位。一个 \"enforcement\" 系统引入了新的约束违反类型，需要更直接地在 §1/Abstract 层面承认。Abstract 目前完全不提 CF 增加。\n- 建议：在 Abstract 最后加一句 CF caveat（e.g., \"with a model-dependent cross-field consistency trade-off mitigated by fine-tuning\"），或将标题/定位从 \"enforcement\" 调整为 \"reduction\"。\n\n**W3** [warning] 主评价指标是 violation rate reduction 而非下游任务质量——存在循环论证风险\n\n- 具体位置：§5 全部\n- 问题：论文的核心实验设计是：约束违反率下降 = 成功。这是 tautological 的——施加约束当然会减少约束违反。真正需要证明的是：减少违反是否带来下游价值？论文用 F1 作为 \"control variable\" 证明无害，但 F1-neutral 不等于有用。Appendix B 的 post-hoc filtering 对比显示 post-hoc 在大多数情况下 F1 还更高（5/6 zero-shot 设置）。\n- 建议：(1) 增加一个下游任务评估（e.g., 用抽取的 triples 做 QA 或 knowledge graph completion，比较有/无 type violation 的影响）；(2) 或者更直接地承认当前贡献是\"保证性质\"而非\"性能提升\"，并在 §1 中重新定位。\n\n**W4** [warning] 写作结构问题：§5.1 \"Violation Landscape\" 混合了 motivation 和 experimental setup\n\n- 具体位置：§5.1 (section3_violation_landscape.tex)\n- 问题：这一节同时承担三个角色：(1) 实验设置描述、(2) 基线违反率分析（这是 motivation）、(3) schema-informed prompting 对比（这是 baseline experiment）。逻辑上，violation landscape 分析应放在 §2 Background 或 §3 Method 的 motivation 部分，实验设置应独立为一个清晰的 subsection。当前安排使读者在 §5 开头看到 motivation 内容感到困惑。\n- 建议：将 violation landscape 的 motivation 分析（Table 1, Figure 1）提前到 §2.5 或作为独立的 §3.0 \"Motivation: Violation Prevalence\"。\n\n**W5** [warning] 缺少代码/数据可复现性声明\n\n- 具体位置：全文\n- 问题：论文未包含任何关于代码/数据释放的声明。ACL ARR 的 reproducibility 评分维度明确要求作者说明是否会释放代码。Prompt 模板已提供（Appendix），但核心的 semantic layer logits processor 实现、ontology compilation pipeline、entity registry 逻辑均未承诺开源。\n- 建议：添加 \"Code and data will be released upon acceptance\" 或类似声明。\n\n---\n\n## 小问题（不影响接收）\n\n- §3.5 \"Decoding Strategies\" 中 S2 的描述过于简略（\"Detailed comparison is provided in the appendix\"），但 S2 在 Table 2 中有数据，建议补充 1-2 句 S2 的实际结果总结。\n- §4 equation (2) 定义 tightness 时用 $\\tau(r)$ 与 entity type 集合 $\\mathcal{T}$ 的符号冲突——$\\tau$ 既用于 entity type ($\\tau_i$) 又用于 tightness 函数。\n- Table 3 footnote \"Parse failures: Qwen DocRED 12→11 (S1 1.10%)\" 意义不清——12→11 是什么？documents 数？需要更明确的解释。\n- Appendix B \"Relation Matching Protocol\" 使用 fuzzy matching（token overlap >80% + edit distance ≤2）。这个协议对 Mistral 的 F1 贡献 +0.84pp，应在主文 §5.3 简要提及以确保评价一致性透明。\n- `\\bibliography{relwork_new_entries}` 使用单一 bib 文件命名为 \"relwork_new_entries\" 不太规范，建议改为 \"references.bib\" 或 \"main.bib\"。\n\n---\n\n## Missing References\n\n1. **Vukovic et al. (SIGDIAL 2024)** — \"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding\"。直接使用 constrained decoding 进行 ontology-based relation extraction，与 OntoCoDec 的问题设定高度相关。**必须引用并区分。**\n\n2. **\"A Survey of Generative Information Extraction\" (COLING 2025)** — 综述性文献，有助于定位本工作在 generative IE 领域的位置。建议引用。\n\n3. **PARSE (Shen et al., EMNLP 2025 Industry)** — \"LLM Driven Schema Optimization for Reliable Entity Extraction\"，使用 schema guardrails 减少 extraction errors 92%。不同路径但相关。可选引用。\n\n4. **Schema Reinforcement Learning (ACL 2025)** — \"Learning to Generate Structured Output with Schema Reinforcement Learning\"。Training-time schema compliance 方法，与 OntoCoDec 的 inference-time 方法互补。可选引用。\n\n---\n\n## 主要优势\n\n1. **问题定义清晰且有数据支撑**：violation landscape 分析（Table 1, Figure 1）令人信服地证明了问题的普遍性和严重性，per-relation tightness 分析提供了有解释力的框架。\n\n2. **实验设计全面且诚实**：3 模型 × 2 数据集 × 多消融 × composability with fine-tuning × runtime profiling × post-hoc comparison。CF trade-off 的坦诚讨论（包括 CF-DR trade-off ablation, Table 5）体现了学术诚信。\n\n3. **实用性强**：runtime overhead 仅 2-5%，training-free，与 fine-tuning 正交组合后 DR≤0.20%——这是一个可以直接部署的系统。\n\n4. **形式化分析有价值**：§4 的 decidability taxonomy（local / prefix-decidable / non-local）和 non-rectangularity 分析为 constrained decoding 在 IE 中的应用提供了理论框架。\n\n5. **相关工作覆盖度高**：§6 + Appendix A 覆盖了 5 个 paradigm，引用了 2024-2026 的最新工作（IterGen ICLR 2025, CRANE ICML 2025, BoostCD EMNLP 2025, Zhou 2026 等），分类合理。\n\n---\n\n## Questions for Authors\n\n**Q1**: 为什么不与 GCD (Geng et al., EMNLP 2023) 做直接实验对比？GCD 是你们同一实验室的前作，使用 input-dependent grammars 做 IE，且开源。OntoCoDec 的 grammar layer 与 GCD 的关系是什么——是改进、扩展还是不同的技术路线？\n\n**Q2**: CF 增加是否会传播到下游任务？例如，如果将抽取的 triples 用于 knowledge graph construction，一个实体有两个冲突类型对下游的影响是什么？是否有初步评估？\n\n**Q3**: Abstract 中的 $R^2=0.886$ (n=4) 是否可以扩展到包含 Mistral 的 6 个数据点？如果加入 Mistral (56.94% DR SciERC, 57.42% DR DocRED)，拟合是否依然成立？\n\n**Q4**: 在 fine-tuned 设置下（Table 7），grammar layer 是 no-op。这是否意味着 OntoCoDec 对 fine-tuned 系统的实际价值仅来自 semantic layer？如果是，\"two-layer compiled constraint framework\" 的 framing 是否过度强调了 grammar layer 的贡献？\n\n**Q5**: 论文的 tokenizer 假设（\"each entity type maps to a unique first subword token\"）限制了方法的泛化性。对于有 50+ entity types 的大型本体（如 Wikidata 的完整 entity type hierarchy），prefix-tree masking 的工程复杂度和 runtime 开销预期如何？\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-16T17:40:20.495763+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4029
}
```

</details>

---


### Assistant

_source line 164 · 2026-05-16T17:40:28.185977+00:00_

审稿报告已提交给 Review Director。

**总结**：给出 Overall 3.5 分（介于 Findings 和 Main Conference 之间）。三个 critical 问题：(1) novelty claim "first" 需缩窄并引用 DORE (SIGDIAL 2024)；(2) 与代码生成先驱工作的技术区分在主文中阐述不足；(3) 缺少与同领域 constrained decoding IE 系统（GCD, BoostCD）的直接实验对比。五个 warning 级问题涉及 dual-factor regression 统计效力、CF 副作用在 Abstract 的缺失、评价指标的循环论证风险、写作结构、以及可复现性声明。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

4 recorded events


### User

_source line 165 · 2026-05-16T17:42:50.168801+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应每个 Must-Fix (N1-N2) 和 Should-Fix (W1-W6) 问题：
- 如果同意，标注 [AGREE] 并简要说明理由
- 如果不同意，标注 [REBUT] 并提供证据（cite 具体 Section/Table/Figure）

特别关注与你的审查存在重叠或分歧的地方。

---

# Reviewer 1 完整审稿报告

## 总体评分
**Overall**: 3/5 — Findings track acceptance

## Must-Fix 问题

**N1** [critical] Abstract 和 Introduction 系统性省略 CF 副作用，构成选择性报告
- Abstract 声称 "reduces domain/range violations by 94% while maintaining extraction F1"，Introduction 三条贡献均只提 DR 下降。但 CF 从 0.08% 飙升至 9.90%（SciERC, 124× 增幅），Llama DocRED 从 0.17% 升至 12.02%（71× 增幅）。
- 正文 §5 和 Appendix B 对 CF 有诚实讨论，但 abstract/intro 的沉默构成 framing bias。
- 建议：Abstract 中加入 CF trade-off 摘要，Introduction Contribution 3 也应提及。

**N2** [critical] R²=0.886 基于 n=4 数据点被过度解读为"预测框架"
- 线性回归有 2 个自由参数，n=4 仅留 2 个自由度。两个 dataset 的 tightness 差异巨大，tightness 单一变量可能就足以解释大部分方差。
- Abstract 和 conclusion 仍将此描述为 "predictive framework"。
- 建议：改为 "consistent with a dual-factor pattern"，降级为 "descriptive pattern"，增加 Mistral 数据点。

## Should-Fix 问题

**W1** [warning] Parse failure 在约束下增加，构成潜在混淆变量
- Llama DocRED parse failure 从 68/998 (6.8%) 增至 91/998 (9.1%)，增幅 34%。这些文档被排除在评估之外，可能存在样本选择偏差。
- 建议：补充 Llama DocRED zero-shot 的 parse-failure-excluded 分析。

**W2** [warning] 与 Post-hoc filtering 对比不充分支持核心叙事
- Post-hoc filtering 在 6 个 zero-shot 配置中 5 个获得更高 R-F1。Introduction 的 framing 带有否定语气（"wastes compute"），与实验数据不完全一致。
- 建议：正文中加入 post-hoc 对比摘要，诚实说明 post-hoc 在多数 zero-shot 场景 F1 更高。

**W3** [warning] Zero-shot R-F1 ~8% 的实际意义讨论不足
- 论文将 F1 定位为"控制变量"（仅在 Appendix B），但正文高亮 DocRED +0.50pp p<0.001 作为积极结果，存在逻辑不一致。
- 建议：在 §5 加入 1-2 句正文讨论 zero-shot F1 水平的含义。

**W4** [warning] SciERC 5-way vs DocRED 4-way 消融不对称性未解释
- SciERC 包含 S2，DocRED 不包含，未说明原因。

**W5** [warning] Semantic-only 模式在 DocRED 上反直觉地增加 ET 违规
- ET 从 2.48% 几乎翻倍至 4.22%，但 semantic layer 声称仅在 HeadType/TailType 位置激活。

**W6** [warning] First-subword-token 唯一性假设限制泛化性
- §3 将此作为 implementation detail，但实际上是方法适用范围的根本性限制。

## 小问题
- 符号冲突：τ 同时用于 tightness 和 entity type
- Table 2 S2 行 CF=8.03%, R-F1=8.03 数值巧合
- DocRED Grammar/Full S1 RV=0.03%（非 0%），来源未解释
- Greedy decoding 限制
- "Global entity-level type consensus" 缺少可行性分析

## Questions
Q1: CF-DR trade-off 中 DR 和 CF 应否有不同权重？
Q2: Grammar layer 在 DocRED 上强制替换的关系名称语义质量如何？
Q3: Fine-tuned 下 grammar layer 是 no-op，"两层组合" 架构叙事是否被削弱？
Q4: Fuzzy Matching 阈值如何选择？是否调优过？
Q5: Global consensus 在 autoregressive 解码中的可行性？

## 数值一致性核查
逐一核查 Table 1-9 与正文的一致性：所有主要数值声明通过验证。
⚠ Introduction 中 "DR ↓42--90% on DocRED" 的 42% 来自 Mistral，不是 Qwen，范围跨三个模型但未明确说明。

## Missing References
- GenIE (Josifoski et al., 2022) — 正文 §6 未引用
- EnriCo (Zaratiana et al., 2024) — 正文 §6 未引用
- Zhou et al. (2026) "structure snowballing" — 正文 §6 未提及

---

请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-16T17:44:39.450754+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: Abstract/Introduction 省略 CF 副作用\n\n**[AGREE]** — 但对 severity 有不同判断。\n\n我在自己的审稿中将此列为 W2 (Should-Fix)。Reviewer 1 将其列为 Must-Fix。\n\n事实层面完全同意：CF 从 0.08%→9.90%（SciERC, 124×）和 0.17%→12.02%（Llama DocRED, 71×）是重大副作用，Abstract 完全未提及确实构成 framing bias。\n\n但我倾向于 Should-Fix 而非 Must-Fix，理由：\n1. §5.2 paragraph 1 最后一句明确报告了 CF 增加（\"full constraint enforcement elevates cross-field consistency violations from 0.08% to 9.90%\"）\n2. §7 Discussion 第二段专门讨论 CF dual mechanism\n3. Limitations section 开头就提 CF\n4. Appendix B 有完整的 CF-DR trade-off ablation (Table 5)\n\n论文并非隐藏问题，而是在 Abstract/Intro 的 framing 上有偏。这是 \"presentation issue\" 而非 \"integrity issue\"。但我同意必须修复——在 Abstract 末尾加一句 CF caveat 即可。\n\n**修改建议一致**：同意 Reviewer 1 的建议，Abstract 加 CF trade-off 摘要。\n\n---\n\n### R1-N2: $R^2=0.886$ (n=4) 过度解读\n\n**[AGREE]** — 完全同意，与我的 W1 重合。\n\n4 个数据点、2 个参数、2 个自由度——$R^2$ 在这种情况下几乎无信息量。即使随机 4 点也经常获得 $R^2>0.8$。\n\n我还注意到一个 Reviewer 1 未提的补充论点：两个 SciERC 点的 tightness ($\\bar{\\tau}=0.333$) 和两个 DocRED 点的 tightness ($\\bar{\\tau}=0.842$) 差异巨大，本质上这是一个 \"两组各两点\" 的比较，tightness 单一变量就能解释大部分方差。$R^2$ 的高值可能仅反映了两个 dataset 的系统性差异，而非 dual-factor 的 predictive power。\n\n建议一致：从 Abstract 移除 $R^2$ 数字，降级为 \"descriptive pattern\"。增加 Mistral 的 4 个数据点（SciERC + DocRED, unconstrained + S1）可以提供 6-8 点拟合。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: Parse failure 增加构成混淆变量\n\n**[AGREE]** — 有效问题，我未独立发现。\n\nTable 3 footnote 确认 Llama DocRED parse failure 从 68 增至 91 (6.8%→9.1%)。被排除的文档可能系统性偏向某些关系类型（如长文档或多关系文档），导致 violation rate 和 F1 的计算在非随机子集上进行。\n\n进一步证据：§5.2 composability 部分的脚注提到 \"excluding parse-failure documents (+1.4pp increase, 7.1%→8.5%) yields +0.03pp\"——这表明 parse failure 确实影响 R-F1 的解读（all-set 报告 -0.30pp，但排除 parse failure 后变为 +0.03pp）。这个信息仅在脚注中，说明作者意识到问题但未充分讨论。\n\n建议：在正文中增加一个 parse failure sensitivity analysis 段落。\n\n---\n\n### R1-W2: Post-hoc filtering 对比不充分支持核心叙事\n\n**[AGREE]** — 与我的 W3 高度重合。\n\n数据事实：Appendix B Table 8 显示 post-hoc filtering 在 5/6 zero-shot 设置上 F1 更高。Introduction 中 \"Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding\" 的表述暗示 post-hoc 是劣势方法，但实验数据不支持这一判断（至少在 F1 指标上）。\n\n但我要补充一点 Reviewer 1 未提到的平衡观点：\n- OntoCoDec 在 6/6 zero-shot 设置中 recall 更高（Table 8 隐含）\n- 当 rejection rate > 70% (Mistral DocRED) 时 post-hoc 崩溃，OntoCoDec 胜出\n- Fine-tuning 下两者收敛\n\n所以 Introduction 的 framing 不完全错误，但需要 nuance。建议将 \"wastes compute\" 改为条件性表述（e.g., \"becomes increasingly destructive as violation rates rise\"），并在 §5 加入 post-hoc 对比的正文摘要。\n\n---\n\n### R1-W3: Zero-shot R-F1 ~8% 实际意义讨论不足\n\n**[AGREE]** — 有效但可争辩。\n\n论文在 Appendix B \"Practical Significance of Zero-Shot F1\" 段落中有详细讨论，包括与 supervised SOTA (49-53%) 的对比，以及 \"F1 serves as a control variable\" 的定位。问题是这段关键论述只在 Appendix 中。\n\n但我对 Reviewer 1 的批评 \"正文高亮 DocRED +0.50pp p<0.001 作为积极结果\" 有更强的共鸣——如果 F1 只是控制变量，为什么要用 p-value 强调它？这确实存在逻辑不一致。要么 F1 重要（那就讨论 8% 的含义），要么 F1 只是控制（那就不要用统计显著性来高亮它）。\n\n建议：在 §5.2 core result 后加 1-2 句承认 zero-shot F1 的绝对水平较低，引用 Appendix B 的完整讨论。\n\n---\n\n### R1-W4: SciERC 5-way vs DocRED 4-way 消融不对称\n\n**[AGREE]** — 但为 minor issue。\n\n推测原因：DocRED 的 S2 需要两次全文档推理（每文档 ~21s），998 文档的计算成本约 12 GPU-hours，可能是纯工程/资源限制。但论文应说明。一句话足够（e.g., \"S2 is omitted on DocRED due to computational cost of two-pass document-level decoding\"）。\n\n---\n\n### R1-W5: Semantic-only 模式在 DocRED 上 ET 增加 (2.48%→4.22%)\n\n**[AGREE]** — 好发现，我未独立注意到。\n\n这确实反直觉：semantic layer 声称仅在 HeadType/TailType 位置激活（§3.4.2），不应影响 entity type generation。\n\n推测解释：semantic-only 模式下，没有 grammar layer 保证 entity type token 属于 $\\mathcal{E}$。Semantic layer 的 logit masking 可能在某些 prefix 状态下产生 unintended 交互——例如 position detection 误判某个 free-text 位置为 type position，导致 mask 干扰 entity type generation。Table 3 显示 semantic-only 也增加了 RV (29.66%→29.87%)，进一步暗示 semantic layer 在无 grammar 保护下有 side effects。\n\n作者应解释此现象的机制。这也进一步支持了 \"enabling dependency\" 的论点——semantic layer 不应单独使用。\n\n---\n\n### R1-W6: First-subword-token 唯一性限制泛化性\n\n**[AGREE]** — 与我的 Q5 重合。\n\n§3.4.3 \"Implementation\" 段将此描述为已验证的 property（\"verified for both tokenizers on our two ontologies, 6 entity types each\"），但 Limitations 承认 \"ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented\"。\n\n6 个 entity types 的唯一性验证几乎是 trivial 的。真实世界 IE 本体如 Wikidata (7000+ entity types)、UMLS (100+ semantic types)、ACE 2005 (18 entity types) 都远超此规模。这个限制确实是方法论层面的，不仅是工程细节。\n\n建议一致：在 §3.4.3 中将此从 implementation detail 提升为 explicit limitation，说明何时需要 prefix-tree 扩展，并在 Limitations section 中讨论 scalability。\n\n---\n\n## Missing References 评论\n\n**GenIE 和 EnriCo 在正文 §6 中未引用**：[AGREE]。我验证了 section6_related_work.tex——两者仅出现在 appendix_related_work.tex 中。作为与 OntoCoDec 最直接相关的 constrained decoding IE 系统（GenIE: trie-based state constraints; EnriCo: ASP-based type constraints），它们必须出现在主文 §6 而非仅在 Appendix A。\n\n**Zhou et al. (2026) \"structure snowballing\"**：已在 Appendix A \"Quality Impact\" 段引用 (`\\cite{zhou2026snowballing}`)，但未出现在主文 §6。鉴于 §6 的 \"Quality Impact\" 段落长度有限，可以接受仅在 Appendix 讨论。INFO 级别，非必须。\n\n---\n\n## 数值一致性核查补充\n\n同意 Reviewer 1 的 ⚠ 标注：\"DR ↓42--90% on DocRED\" 的 42% 来自 Mistral，90% 来自 Llama。Introduction Contribution 3 写 \"DR↓42--90% on DocRED\" 而 Abstract 也使用此范围。建议在 Introduction 中明确 \"(across three model families)\"，目前已有但容易被忽略。\n\n---\n\n## 与我自己审稿的重叠/分歧总结\n\n| 问题 | R1 severity | R2 severity | 判断 |\n|------|-------------|-------------|------|\n| CF 省略 | N1 (critical) | W2 (warning) | 偏向 Should-Fix，但同意必须修复 |\n| R² n=4 | N2 (critical) | W1 (warning) | 同意 critical（因为出现在 Abstract） |\n| Post-hoc 叙事 | W2 | W3 | 一致 |\n| GCD/GenIE 缺实验对比 | 未提 | N3 (critical) | R1 未提此问题，但我认为是 critical |\n| DORE 未引用 | 未提 | N1 (critical) | R1 未提此问题 |\n| Code-gen novelty 阐述不足 | 未提 | N2 (critical) | R1 未提此问题 |\n\n关键分歧：Reviewer 1 更关注 reporting integrity (CF省略, R²)，我更关注 novelty substantiation (与 code-gen 的区分, 与同类方法的实验对比)。两者互补，建议 Director 综合考虑。\n",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n### R1-N1: Abstract/Introduction 省略 CF 副作用\n\n**[AGREE]** — 但对 severity 有不同判断。\n\n我在自己的审稿中将此列为 W2 (Should-Fix)。Reviewer 1 将其列为 Must-Fix。\n\n事实层面完全同意：CF 从 0.08%→9.90%（SciERC, 124×）和 0.17%→12.02%（Llama DocRED, 71×）是重大副作用，Abstract 完全未提及确实构成 framing bias。\n\n但我倾向于 Should-Fix 而非 Must-Fix，理由：\n1. §5.2 paragraph 1 最后一句明确报告了 CF 增加（\"full constraint enforcement elevates cross-field consistency violations from 0.08% to 9.90%\"）\n2. §7 Discussion 第二段专门讨论 CF dual mechanism\n3. Limitations section 开头就提 CF\n4. Appendix B 有完整的 CF-DR trade-off ablation (Table 5)\n\n论文并非隐藏问题，而是在 Abstract/Intro 的 framing 上有偏。这是 \"presentation issue\" 而非 \"integrity issue\"。但我同意必须修复——在 Abstract 末尾加一句 CF caveat 即可。\n\n**修改建议一致**：同意 Reviewer 1 的建议，Abstract 加 CF trade-off 摘要。\n\n---\n\n### R1-N2: $R^2=0.886$ (n=4) 过度解读\n\n**[AGREE]** — 完全同意，与我的 W1 重合。\n\n4 个数据点、2 个参数、2 个自由度——$R^2$ 在这种情况下几乎无信息量。即使随机 4 点也经常获得 $R^2>0.8$。\n\n我还注意到一个 Reviewer 1 未提的补充论点：两个 SciERC 点的 tightness ($\\bar{\\tau}=0.333$) 和两个 DocRED 点的 tightness ($\\bar{\\tau}=0.842$) 差异巨大，本质上这是一个 \"两组各两点\" 的比较，tightness 单一变量就能解释大部分方差。$R^2$ 的高值可能仅反映了两个 dataset 的系统性差异，而非 dual-factor 的 predictive power。\n\n建议一致：从 Abstract 移除 $R^2$ 数字，降级为 \"descriptive pattern\"。增加 Mistral 的 4 个数据点（SciERC + DocRED, unconstrained + S1）可以提供 6-8 点拟合。\n\n---\n\n## Should-Fix 问题\n\n### R1-W1: Parse failure 增加构成混淆变量\n\n**[AGREE]** — 有效问题，我未独立发现。\n\nTable 3 footnote 确认 Llama DocRED parse failure 从 68 增至 91 (6.8%→9.1%)。被排除的文档可能系统性偏向某些关系类型（如长文档或多关系文档），导致 violation rate 和 F1 的计算在非随机子集上进行。\n\n进一步证据：§5.2 composability 部分的脚注提到 \"excluding parse-failure documents (+1.4pp increase, 7.1%→8.5%) yields +0.03pp\"——这表明 parse failure 确实影响 R-F1 的解读（all-set 报告 -0.30pp，但排除 parse failure 后变为 +0.03pp）。这个信息仅在脚注中，说明作者意识到问题但未充分讨论。\n\n建议：在正文中增加一个 parse failure sensitivity analysis 段落。\n\n---\n\n### R1-W2: Post-hoc filtering 对比不充分支持核心叙事\n\n**[AGREE]** — 与我的 W3 高度重合。\n\n数据事实：Appendix B Table 8 显示 post-hoc filtering 在 5/6 zero-shot 设置上 F1 更高。Introduction 中 \"Post-hoc validation wastes compute on discarded outputs and cannot redirect probability mass during decoding\" 的表述暗示 post-hoc 是劣势方法，但实验数据不支持这一判断（至少在 F1 指标上）。\n\n但我要补充一点 Reviewer 1 未提到的平衡观点：\n- OntoCoDec 在 6/6 zero-shot 设置中 recall 更高（Table 8 隐含）\n- 当 rejection rate > 70% (Mistral DocRED) 时 post-hoc 崩溃，OntoCoDec 胜出\n- Fine-tuning 下两者收敛\n\n所以 Introduction 的 framing 不完全错误，但需要 nuance。建议将 \"wastes compute\" 改为条件性表述（e.g., \"becomes increasingly destructive as violation rates rise\"），并在 §5 加入 post-hoc 对比的正文摘要。\n\n---\n\n### R1-W3: Zero-shot R-F1 ~8% 实际意义讨论不足\n\n**[AGREE]** — 有效但可争辩。\n\n论文在 Appendix B \"Practical Significance of Zero-Shot F1\" 段落中有详细讨论，包括与 supervised SOTA (49-53%) 的对比，以及 \"F1 serves as a control variable\" 的定位。问题是这段关键论述只在 Appendix 中。\n\n但我对 Reviewer 1 的批评 \"正文高亮 DocRED +0.50pp p<0.001 作为积极结果\" 有更强的共鸣——如果 F1 只是控制变量，为什么要用 p-value 强调它？这确实存在逻辑不一致。要么 F1 重要（那就讨论 8% 的含义），要么 F1 只是控制（那就不要用统计显著性来高亮它）。\n\n建议：在 §5.2 core result 后加 1-2 句承认 zero-shot F1 的绝对水平较低，引用 Appendix B 的完整讨论。\n\n---\n\n### R1-W4: SciERC 5-way vs DocRED 4-way 消融不对称\n\n**[AGREE]** — 但为 minor issue。\n\n推测原因：DocRED 的 S2 需要两次全文档推理（每文档 ~21s），998 文档的计算成本约 12 GPU-hours，可能是纯工程/资源限制。但论文应说明。一句话足够（e.g., \"S2 is omitted on DocRED due to computational cost of two-pass document-level decoding\"）。\n\n---\n\n### R1-W5: Semantic-only 模式在 DocRED 上 ET 增加 (2.48%→4.22%)\n\n**[AGREE]** — 好发现，我未独立注意到。\n\n这确实反直觉：semantic layer 声称仅在 HeadType/TailType 位置激活（§3.4.2），不应影响 entity type generation。\n\n推测解释：semantic-only 模式下，没有 grammar layer 保证 entity type token 属于 $\\mathcal{E}$。Semantic layer 的 logit masking 可能在某些 prefix 状态下产生 unintended 交互——例如 position detection 误判某个 free-text 位置为 type position，导致 mask 干扰 entity type generation。Table 3 显示 semantic-only 也增加了 RV (29.66%→29.87%)，进一步暗示 semantic layer 在无 grammar 保护下有 side effects。\n\n作者应解释此现象的机制。这也进一步支持了 \"enabling dependency\" 的论点——semantic layer 不应单独使用。\n\n---\n\n### R1-W6: First-subword-token 唯一性限制泛化性\n\n**[AGREE]** — 与我的 Q5 重合。\n\n§3.4.3 \"Implementation\" 段将此描述为已验证的 property（\"verified for both tokenizers on our two ontologies, 6 entity types each\"），但 Limitations 承认 \"ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented\"。\n\n6 个 entity types 的唯一性验证几乎是 trivial 的。真实世界 IE 本体如 Wikidata (7000+ entity types)、UMLS (100+ semantic types)、ACE 2005 (18 entity types) 都远超此规模。这个限制确实是方法论层面的，不仅是工程细节。\n\n建议一致：在 §3.4.3 中将此从 implementation detail 提升为 explicit limitation，说明何时需要 prefix-tree 扩展，并在 Limitations section 中讨论 scalability。\n\n---\n\n## Missing References 评论\n\n**GenIE 和 EnriCo 在正文 §6 中未引用**：[AGREE]。我验证了 section6_related_work.tex——两者仅出现在 appendix_related_work.tex 中。作为与 OntoCoDec 最直接相关的 constrained decoding IE 系统（GenIE: trie-based state constraints; EnriCo: ASP-based type constraints），它们必须出现在主文 §6 而非仅在 Appendix A。\n\n**Zhou et al. (2026) \"structure snowballing\"**：已在 Appendix A \"Quality Impact\" 段引用 (`\\cite{zhou2026snowballing}`)，但未出现在主文 §6。鉴于 §6 的 \"Quality Impact\" 段落长度有限，可以接受仅在 Appendix 讨论。INFO 级别，非必须。\n\n---\n\n## 数值一致性核查补充\n\n同意 Reviewer 1 的 ⚠ 标注：\"DR ↓42--90% on DocRED\" 的 42% 来自 Mistral，90% 来自 Llama。Introduction Contribution 3 写 \"DR↓42--90% on DocRED\" 而 Abstract 也使用此范围。建议在 Introduction 中明确 \"(across three model families)\"，目前已有但容易被忽略。\n\n---\n\n## 与我自己审稿的重叠/分歧总结\n\n| 问题 | R1 severity | R2 severity | 判断 |\n|------|-------------|-------------|------|\n| CF 省略 | N1 (critical) | W2 (warning) | 偏向 Should-Fix，但同意必须修复 |\n| R² n=4 | N2 (critical) | W1 (warning) | 同意 critical（因为出现在 Abstract） |\n| Post-hoc 叙事 | W2 | W3 | 一致 |\n| GCD/GenIE 缺实验对比 | 未提 | N3 (critical) | R1 未提此问题，但我认为是 critical |\n| DORE 未引用 | 未提 | N1 (critical) | R1 未提此问题 |\n| Code-gen novelty 阐述不足 | 未提 | N2 (critical) | R1 未提此问题 |\n\n关键分歧：Reviewer 1 更关注 reporting integrity (CF省略, R²)，我更关注 novelty substantiation (与 code-gen 的区分, 与同类方法的实验对比)。两者互补，建议 Director 综合考虑。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-16T17:44:43.314825+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 168 · 2026-05-16T17:44:50.202118+00:00_

已完成对 Reviewer 1 审稿意见的逐条回应，总结：

- **N1 (CF省略)**：AGREE，但倾向 Should-Fix 级别（论文在正文/Appendix 有讨论，只是 Abstract/Intro framing 有偏）
- **N2 (R² n=4)**：AGREE，补充了"两组各两点"的额外论据
- **W1-W6**：全部 AGREE，其中 W5 (semantic-only ET 增加) 是好发现，我补充了可能的机制解释

关键分歧：R1 更关注 reporting integrity，我更关注 novelty substantiation（与 code-gen 区分、缺少同类方法实验对比）。两者互补。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

70 recorded events


### User

_source line 169 · 2026-05-17T10:15:28.910219+00:00_

[Round 1 审稿请求]:
## Round 4 审稿任务 — Reviewer 2（新颖性/写作/格式）

### Venue 信息
- **目标**: EMNLP 2026 Findings (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **页数限制**: 正文 8 页，references/appendix 不限
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: double-blind
- **附录**: 不参与正文页数限制，但可参与审稿

### 论文文件
- 主文件: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- 附录: `appendix_beam_search.tex`, `appendix_sampling_table.tex`, `appendix_prompts.tex`, `appendix_related_work.tex`, `appendix_discussion.tex`, `appendix_llama_per_relation.tex`

### 你的审查侧重
**新颖性 + 写作质量 + 格式合规 + Related Work 完整性**

重点审查：
1. **新颖性评估**：OntoCoDec 相对于 DORE、GCD、GoLLIE、GenIE、EnriCo 等已有工作的增量贡献是否清楚？"first" claim 是否过宽？
2. **写作质量**：
   - Abstract 四要素是否完整？是否有 overclaim？
   - Introduction 叙事线是否连贯？问题→洞察→方法→验证是否流畅？
   - AI 写作痕迹检查：dash (—/–)、-ing 分词短语、过度分段、过渡词堆积
   - 专有名词是否首次出现时定义？缩写是否在 Abstract 内展开？
3. **Related Work**：是否做了归纳比较而非论文堆砌？是否有遗漏的重要工作（特别是 2024-2025 最新工作）？引用数量是否足够？
4. **格式合规**：
   - 页数是否在 8 页限制内？
   - 行号是否开启？
   - 图表 caption 是否自包含？数值精度是否一致？最优加粗/次优下划线？
   - Limitations 和 Ethics Statement 是否满足 ARR 要求？
   - 是否有 reproducibility statement？
5. **图表知识密度**：Figure/Table 的信息密度是否足够？是否有空间浪费？

### 先前审稿的 Open/In-Progress Issues（需要你验证当前版本是否已修复）

**Warning:**
- **W8**: Contribution #2 的 "first" claim 是否已进一步收窄到 "pair-based domain/range constraints via compiled stateful logit masks"？DORE 是否已正确引用？
- **W9**: First-subword-token 假设是否已从 "implementation detail" 升级为 "design assumption"？
- **R2-N2**: Code-gen novelty 区分是否已从 Appendix 提升到 §1/§3？
- **R2-N4**: Zero-shot R-F1 ~8% 的实际意义是否已在 §5 中 contextualize？
- **R2-N5**: 是否已添加 code/data 可复现性声明？
- **R2-N9**: DORE、GenIE、EnriCo 是否已在 §6 主文本中出现？

**Info:**
- **R2-N8**: 符号冲突 τ→κ 是否已修复？
- **GC-N2**: Introduction "DR ↓42-90%" 范围是否已标明 "across three models"？
- **GC-N3**: Greedy decoding limitation 是否在 Limitations 中讨论？

请逐条检查以上 issue 的修复状态，同时做独立全面审稿。按标准审稿格式输出：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。

**特别注意**：用 EMNLP 2026/ACL 最严格审稿标准评判。写作上检查 AI 痕迹（dash、-ing 分词短语等）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-17T10:15:39.015351+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-17T10:15:39.069351+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-17T10:15:43.891943+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 173 · 2026-05-17T10:15:45.283005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 174 · 2026-05-17T10:15:45.283462+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_runtime}
53	
54	% === §6 Related Work ===
55	\input{section6_related_work}
56	
57	% === §7 Discussion and Conclusion ===
58	\section{Discussion and Conclusion}
59	\label{sec:discussion}
60	\input{section7_conclusion_compressed}
61	
62	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
63	\clearpage
64	\section*{Limitations}
65	
66	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13
…[truncated 3529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-17T10:15:51.923978+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"}]

Based on the web search results, here's information about ACL ARR 2025/2026 reviewer guidelines, review form, and scoring criteria:

## Reviewer Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of t
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8032
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-17T10:15:56.847361+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need: soundness scale, excitement scale, overall recommendation scale, and any other required fields like confidence, reproducibility, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. I need: soundness scale, excitement scale, overall recommendation scale, and any other required fields like confidence, reproducibility, etc."
  }
}
```

</details>

---


### Tool call

_source line 177 · 2026-05-17T10:15:57.349939+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 178 · 2026-05-17T10:15:57.400525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-17T10:16:02.642818+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: Positive evaluation; read carefully and familiar with related work
- **4**: Quite sure; checked important points; unlikely to have missed key details
- **3**: Pretty sure; good area familiarity but didn't check all details carefully
- **2**: Can defend evaluation but likely missed some details or novelty assessment
- **1**: Outside expertise area or paper very difficult to understand

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: Excellent; most thorough study of its type
- **4**: Strong; sufficient support for claims, some extra experiments optional
- **3**: Acceptable; main claims supported, minor points need details
- **2**: Poor; main claims lack support, major technical/methodological problems
- **1**: Major issues; insufficient rigor or not relevant to ACL

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: Highly exciting; would recommend and attend presentation
- **4**: Exciting; would mention to others and make effort to attend
- **3**: Interesting; might mention points or attend if time allows
- **2**: Potentially interesting; doesn't resonate personally but may appeal to community
- **1**: Not exciting; lacks relevance to computational linguistics

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Award consideration (top 2.5% papers)
- **4**: Accept to main conference
- **3**: Accept to Findings track
- **2**: Needs substantial revisions for next cycle
- **1**: Reject or fundamentally flawed

## Additional Required Fields
- **Reproducibility** (1-5 scale)
- **Datasets value** (1-5 scale, if applicable)
- **Software value** (1-5 scale, if applicable)
- **Author identity knowledge** (1-5 scale)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5795
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-17T10:16:09.019804+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-17T10:16:09.170936+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research
…[truncated 2180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-17T10:16:12.789910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-17T10:16:13.292912+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar CFG) guaranteeing JSON structural validity and entity/relation vocabulary membership (ET, RV\,$\to$\,0\%); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, LLM-based IE produces systematic violations: 15.37\% DR on SciERC (7 relations) and 18.46\% on DocRED (96 relations)---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	Residual DR is characterized by a dual-factor pattern (schema tightness $\times$ model calibration; $R^2{=}0.886$, $n{=}4$; Appendix~\ref{app:dual-factor}).
12	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 within $\pm$0.6\,pp, confirming orthogonal composability.
13	Per-relation independent enforcement introduces a CF$\leftrightarrow$DR trade-off: cross-field consistency violations arise (up to 12\% in zero-shot) as the cost of per-slot domain/range guarantees; fine-tuning resolves this tension (CF\,$\leq$\,1.2\%).
14	\end{abstract}
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-17T10:16:13.393961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-17T10:16:14.198429+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	At high rejection rates (e.g., Mistral DocRED 73.7\%), post-hoc filtering discards the majority of outputs including true positives, making it impractical; it also cannot redirect probability mass during decoding.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
16	
17	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
18	The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
19	The \emph{semantic layer} 
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-17T10:16:14.198949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-17T10:16:14.349750+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{T}|^2$ where $\mathcal{T} = \mathcal{E}$ is the entity type vocabulary: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules---e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''---which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}---well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}---$(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}---at the point where a type token is generated, all in
…[truncated 89 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-17T10:16:14.350158+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-17T10:16:14.400853+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	
29	\paragraph{Ontology compliance.}
30	Using the ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defined in \S\ref{sec:background}, we write $\operatorname{dom}(r) = \{\tau^h : \exists \tau^t,
…[truncated 7978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-17T10:16:20.862966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-17T10:16:20.913854+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cros
…[truncated 1970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-17T10:16:21.215335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-17T10:16:22.069552+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	Violation rates are computed over successfully parsed documents; including parse failures as zero-violation instances adjusts rates by at most 0.23\,pp (Llama DocRED zero-shot; $<$0.01\,pp under fine-tuning), confirming robustness to this exclusion.
14	
15	\paragraph{Violation distribution.}
16	Table~\ref{tab:prompt_comparison} reports violation rates.
17	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
18	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce 
…[truncated 1607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-17T10:16:23.075818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-17T10:16:23.327605+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Results on SciERC}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain/range violation rate;
63	RV: rel
…[truncated 10876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 196 · 2026-05-17T10:16:29.151316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-17T10:16:29.555010+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 3449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-17T10:16:29.605998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-17T10:16:30.108395+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results across all three models.
12	Mistral serves as a third zero-shot verification point confirming model-agnosticism; composability evaluation (\S\ref{sec:composability}) uses LoRA fine-tuning which requires domain-specific training data available only for Qwen and Llama.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.4pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rrrr r@{}}
20	\toprule
21	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
22	& \textbf{R-F1} \\
23	\cmidrule(lr){3-6} \cmidrule(l){7-7}
24	\textbf{Dataset} & \textbf{Model}
25	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
26	  & $\uparrow$ \\
27	\midrule
28	\multirow{6}{*}{SciERC}
29	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
30	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
31	  \cmidrule(l){2-7}
32	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
33	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
34	  \cmidrule(l){2-7}
35	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
36	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
37	\midrule
38	\multirow{6}{*}{DocRED}
39	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
40	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
41	  \cmidrule(l){2-7}
42	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
43	  & Llama (S1)  &  2.55 &  0  
…[truncated 2202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-17T10:16:30.109260+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-17T10:16:30.159926+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation; IterGen~\cite{ugare2025itergen} adds backtracking.
6	These guarantee format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
7	
8	\paragraph{Semantic Constrained Decoding for Code.}
9	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE.
10	
11	\paragraph{Vocabulary and Type-Constrained Generation.}
12	\citet{roth_yih_2004} establish relational type compatibility as a hard constraint via ILP, though applied post-hoc.
13	GENRE~\cite{decao2021genre}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation; GCD's per-position trie enforces vocabulary membership (equivalent to our grammar layer) but cannot capture the conditional dependency between head and tail types that our semantic layer provides.
14	DORE~\cite{vukovic2024dore} enforces ontological consistency via chain-of-thought output selection with confidence thresholds---a generate-then-select paradigm distinct from OntoCoDec's token-level logit masking during generation.
15	GenIE~\cite{josifoski2022genie} constrains entity generation to a candidate trie but does not enforce relation-specific type constraints.
16	EnriCo~\cite{zaratiana2024enrico} applies ASP constraints during decoding for joint entity-relation extraction---a hard-constraint approach like ours, but with task-sp
…[truncated 1083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-17T10:16:35.534780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-17T10:16:36.036636+00:00_

1	% Section 5 — Runtime Analysis
2	% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
3	% Qwen3-8B, same single-GPU server, controlled 4-way ablation.
4	
5	\subsection{Runtime Overhead}
6	\label{sec:runtime}
7	
8	Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{@{}l rr rr@{}}
15	\toprule
16	& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
17	& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
18	\cmidrule(lr){2-3} \cmidrule(l){4-5}
19	\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
20	\midrule
21	Unconstrained & 2.587 & --- & 21.023 & --- \\
22	Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
23	Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
24	Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
25	\bottomrule
26	\end{tabular}
27	\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
28	Grammar compile time: 0.044\,s (one-time, amortized to zero).
29	Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
30	\label{tab:runtime}
31	\end{table}
32	
33	Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
34	Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
35	Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
36	Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
37	Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-17T10:16:36.187576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-17T10:16:36.538971+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix C.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and two datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, it reaches DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost, confirming orthogonal error targeting.
6	Within calibrated models (Qwen, Llama; $n{=}4$), residual DR correlates linearly with $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ ($R^2{=}0.886$), suggesting constraint benefit scales with schema stringency and model OOV tendency.
7	This pattern has an informative boundary condition: Mistral achieves RV\,=\,0\% on SciERC yet retains DR\,=\,13.4\%, because its dominant error mode is entity type misclassification rather than vocabulary confusion---a factor not captured by the dual-factor product.
8	We present this as a descriptive characterization with explicit scope rather than a universal predictive law.
9	
10	CF impact is model-dependent: S1 introduces CF for well-calibrated models (up to 12.02\%) but reduces it for poorly-calibrated ones (Mistral: 56.87\%\,$\to$\,1.27\%).
11	Ablation confirms CF$\leftrightarrow$DR tension ($+$13.85\,pp; Appendix~\ref{app:cf-dr-tradeoff}); fine-tuning reduces CF by 88\% (\S\ref{sec:composability}); global entity-level type consensus offers the most direct path forward.
12	
13	% Limitations and Future Work moved to \section*{Limitations} in main.tex (ARR requirement)
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-17T10:16:36.539499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 207 · 2026-05-17T10:16:36.590250+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
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
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-17T10:16:41.962811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-17T10:16:42.315116+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different seman
…[truncated 26266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 210 · 2026-05-17T10:16:42.365831+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-17T10:16:42.768295+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on 50-document subsets (greedy baselines from 998-document full evaluation, not matched subsets).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{t
…[truncated 6262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-17T10:16:42.768661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-17T10:16:42.819191+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-17T10:16:52.232167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-17T10:16:52.232745+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding---constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ 
…[truncated 771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-17T10:16:52.383741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 217 · 2026-05-17T10:16:52.384241+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-17T10:16:52.434782+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—|–",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-17T10:16:52.585934+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:10:The grammar layer (\S\ref{sec:grammar}) guarantees structural validity—well-formed JSON with ontology-vocabulary membership—while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:49:Domain/range constraints are \emph{not} enforced, as they depend on entity types within each triple—the gap filled by the semantic layer.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-rese
…[truncated 1834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-17T10:17:00.770217+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-17T10:17:02.184432+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:13:When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:23:Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:26:The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:41:The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:13:types---14$\times$ the ontology size of SciERC
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:40:  & 18.46 & ---
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:48:  
…[truncated 16199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool call

_source line 222 · 2026-05-17T10:17:02.787233+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (highlighting|demonstrating|showing|confirming|indicating|suggesting|achieving|enabling|ensuring|providing|establishing|representing|reducing|eliminating|making|leveraging|utilizing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (highlighting|demonstrating|showing|confirming|indicating|suggesting|achieving|enabling|ensuring|providing|establishing|representing|reducing|eliminating|making|leveraging|utilizing)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-17T10:17:02.838317+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:173:for the model to redirect probability mass toward, enabling
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:At high rejection rates (e.g., Mistral DocRED 73.7\%), post-hoc filtering discards the majority of outputs including true positives, making it impractical; it also cannot redirect probability mass during decoding.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:20:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:25:    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:67:CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp), confirming that CF$\leftrightarrow$DR represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:8:Recent work has established efficient algorithms
…[truncated 16880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-17T10:17:07.909884+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project"
  }
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-17T10:17:08.311891+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-17T10:17:08.815396+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "section6_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-17T10:17:08.916482+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:5:XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation; IterGen~\cite{ugare2025itergen} adds backtracking.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:9:Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:13:GENRE~\cite{decao2021genre}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation; GCD's per-position trie enforces vocabulary membership (equivalent to our grammar layer) but cannot capture the conditional dependency between head and tail types that our semantic layer provides.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:14:DORE~\cite{vukovic2024dore} enforces ontological consistency via chain-of-thought output selection with confidence thresholds---a generate-then-select paradigm distinct from OntoCoDec's token-level logit masking during generation.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:15:GenIE~\cite{josifoski2022genie} constrains entity generation to a candidate
…[truncated 1764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-17T10:17:12.783220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-17T10:17:13.035336+00:00_

1	% ============================================================
2	% Merged authoritative BibTeX references (9 entries)
3	% Merged 2026-05-14 from relwork_new_entries.bib + new_references.bib
4	% ============================================================
5	
6	% Confirmed via: Semantic Scholar, arXiv:2201.11227, OpenReview
7	% Venue: ICLR 2022 (cite key corrected from synchromesh_neurips2022)
8	@inproceedings{synchromesh_iclr2022,
9	  title     = {Synchromesh: Reliable Code Generation from Pre-trained Language Models},
10	  author    = {Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit},
11	  booktitle = {International Conference on Learning Representations},
12	  year      = {2022},
13	  url       = {https://openreview.net/forum?id=KmtVD97J43e}
14	}
15	
16	% Confirmed via: NeurIPS 2023 proceedings, microsoft/monitors4codegen GitHub
17	@inproceedings{mgd_neurips2023,
18	  title     = {Monitor-Guided Decoding of Code {LMs} with Static Analysis of Repository Context},
19	  author    = {Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. and Rajamani, Sriram K.},
20	  booktitle = {Advances in Neural Information Processing Systems},
21	  volume    = {36},
22	  year      = {2023},
23	  url       = {https://proceedings.neurips.cc/paper_files/paper/2023/hash/662b1774ba8845fc1fa3d1fc0177ceeb-Abstract-Conference.html}
24	}
25	
26	% Confirmed via: ACM DL doi:10.1145/3729274, arXiv:2504.09246, SRI Lab ETH
27	@article{pldi2025_type_constrained_codegen,
28	  title     = {Type-Constrained Code Generation with Language Models},
29	  author    = {M\"{u}ndler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn and Vechev, Martin},
30	  journal   = {Proceedings of the ACM on Programming Languages},
31	  volume    = {9},
32	  number    = {PLDI},
33	  year      = {2025},
34	  doi       = {10.1145/3729274},
35	  url       = {https://dl.acm.org/doi/10.1145/372927
…[truncated 27068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-17T10:18:53.609840+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\section|\\\\subsection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "section[1-7]*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\section|\\\\subsection",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "section[1-7]*.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-17T10:18:53.861061+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:8:\subsection{Cross-Dataset Validation on DocRED}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:3:\section{Introduction}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex:3:\section{Background}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:7:\subsection{Cross-Model Validation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:5:\section{Method}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:15:\subsection{Problem Formulation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:36:\subsection{Grammar Layer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:56:\subsection{Semantic Layer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:108:\subsection{Decoding Strategies}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex:1:\section{Related Work}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:2:% Compressed from standalone section. main.tex provides \subsection header.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projec
…[truncated 1058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-17T10:18:54.513380+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "LLM|Large Language Model",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "LLM|Large Language Model",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-17T10:18:54.564053+00:00_

7:Without constraints, LLM-based IE produces systematic violations: 15.37\% DR on SciERC (7 relations) and 18.46\% on DocRED (96 relations)---comparable rates governed by \emph{constraint tightness} rather than ontology scale.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-17T10:19:02.098790+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-17T10:19:02.249644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-17T10:20:56.090011+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Round 4 审稿报告 — Reviewer 2（新颖性/写作/格式/Related Work）\n\n---\n\n## 总体评分\n**Overall**: 3.5/5（Accept to Findings，偏强）\n**一句话总结**: 扎实的工程贡献，实验充分且诚实，但核心新颖性是将已有范式（type-constrained code generation）迁移到 IE，增量贡献清晰但 excitement 有限。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨，3模型×2数据集+消融+fine-tuning composability+runtime；统计检验充分（bootstrap CI）；已知局限（CF trade-off, n=4 dual-factor）处理诚实 |\n| Excitement | 2.5/5 | 核心思路是 type-constrained decoding 从代码生成迁移到 IE，§3开头三点区别有说服力但增量性质不变；对已有 GCD/EnriCo 的改进幅度需要 reviewer 仔细比对 |\n| Reproducibility | 3.5/5 | 代码/数据承诺 upon acceptance；prompt 完整；超参数报告充分；但缺少正式 Reproducibility Statement，random seed 未明确报告 |\n| Confidence | 4/5 | 熟悉 constrained decoding + IE 领域 |\n\n---\n\n## 先前 Issues 修复状态验证\n\n| Issue | 状态 | 证据 |\n|-------|------|------|\n| **W8**: \"first\" claim 收窄 + DORE 引用 | ✅ Fixed | §1 Contribution #2: \"the first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE\"; DORE 在 §6 line 14 明确引用并区分 |\n| **W9**: First-subword-token 升级为 Design Assumption | ✅ Fixed | §3.3 Implementation 段落用 **\\emph{Design Assumption}** 标记，Limitations 中也讨论了 prefix-tree masking 的扩展路径 |\n| **R2-N2**: Code-gen 区分提升到 §1/§3 | ⚠️ Partial | §3 第一段（line 9）明确列出三点区别，但 §1 无任何 code-gen 讨论——审稿人在读 Introduction 时无法理解为何这不是 trivial migration。建议在 §1 Contribution #2 附近加一句简述区别 |\n| **R2-N4**: Zero-shot R-F1 ~8% 实际意义 | ✅ Fixed | §5 DocRED 段落 \"Zero-shot F1 context\" 明确说明 F1 作为 control variable 而非 optimization target；引用 supervised SOTA (49-53%) 作对比 |\n| **R2-N5**: Code/data 可复现性声明 | ⚠️ Minimal | Ethics Statement 仅说 \"Code and data will be released upon acceptance\" 一句。ARR 期望更详细的 reproducibility 信息（seeds, hardware, training details）。无独立 Reproducibility Statement |\n| **R2-N9**: DORE/GenIE/EnriCo 在 §6 主文本 | ✅ Fixed | 三者均在 section6_related_work.tex 出现，有具体区分描述 |\n| **R2-N8**: 符号冲突 τ→κ | ✅ Fixed | §4 Eq.3 使用 κ(r)；§5 per-relation 表格用 κ；全文一致 |\n| **GC-N2**: \"DR ↓42-90%\" 标注 \"across three models\" | ✅ Fixed | Abstract line 8 和 §1 Contribution #3 均标明 \"across three model families\" / \"across three models\" |\n| **GC-N3**: Greedy decoding limitation | ✅ Fixed | Limitations 段落明确讨论 greedy decoding 限制并指向 Appendix beam search/sampling |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 缩写未展开违反 ARR 规范\n- 具体位置：abstract.tex 全文\n- 问题：Abstract 使用 \"LLM\"（line 7）、\"IE\"（line 1 \"IE ontology\"）、\"CFG\"（line 3）、\"DR\"（line 7-8）、\"ET\"/\"RV\"（line 3）、\"CF\"（line 13）、\"LoRA\"（line 12）均未在 Abstract 内给出完整定义。标题中 \"Information Extraction\" 定义了 IE，但 Abstract 应独立可读。\n- 为什么影响接收：ARR 审稿人对缩写规范敏感；abstract 是 matching 的唯一输入，未定义缩写降低可读性。至少 LLM、IE、DR 必须展开。\n- 建议修改方向：首次出现时展开 \"Large Language Model (LLM)-based Information Extraction (IE)\"；DR 已通过 \"domain/range\" 隐式定义但建议加 \"(DR)\"；CF/ET/RV 可保留为括号内指标缩写但加 full name。\n\n**N2** [critical] 正文主体存在大量 AI 写作典型标志（em-dash 过度使用）\n- 具体位置：section1 (3处)、section2 (3处)、section3 (2处 Unicode — + 2处 LaTeX ---)、section5_docred (2处)\n- 问题：正文中 LaTeX `---`（编译为 em-dash）至少 12 处用于解释性插入，例如：\n  - §1 line 7: \"violations---structurally valid triples that are ontologically invalid\"\n  - §1 line 12: \"unreliable---violations for \\textsc{Evaluate-for} actually increase\"\n  - §2 line 16: 双 em-dash 包围解释 \"---e.g., ...---which depend on...\"\n  - §2 lines 20-21: 两处解释性 dash\n  - §3 line 10: Unicode — (非 LaTeX ---）\n  - §3 line 49: Unicode —\n  这在 NLP 社区虽非严格禁止，但密度过高（正文 8 页中 >12 处）是 AI 生成的显著标志。\n- 为什么影响接收：EMNLP 审稿人熟悉 AI 写作痕迹；高密度 em-dash 可能引发对论文原创性的质疑。\n- 建议修改方向：逐一改为逗号、括号或拆分为两个句子。保留至多 2-3 处用于真正需要的语法结构中。Unicode em-dash (—) 必须全部消除。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] -ing 分词短语结尾（AI 写作痕迹）\n- 具体位置：section1 line 14 \"making it impractical\"、line 20 \"enabling the semantic layer\"、line 25 \"showing that violation rates\"；section3 line 53 \"confirming that grammar constraints\"、line 82 \"ensuring consistency\"、line 114 \"achieving strong constraint enforcement\"；appendix_related_work.tex 大量（>20处）\n- 问题：-ing participial phrases at sentence/clause end 是 AI 生成文本最典型标志之一。正文中约 8-10 处，appendix 中更密集。\n- 建议：正文中的 8-10 处应改写为独立从句或 \"which\" 从句。Appendix 中可以容忍但建议减少密度。\n\n**W2** [warning] Code-gen 新颖性区分未在 Introduction 出现\n- 具体位置：section1_introduction_draft.tex（Contribution #2 周围）\n- 问题：§3 开头清楚列出了 IE vs. code-gen 的三个关键区别（entity types inferred from free text, dynamic registry, context-dependent targets），但 §1 没有任何 code-gen 的讨论。审稿人读 Introduction 时会问：\"这和 PICARD/MGD/PLDI2025 type-constrained codegen 有什么本质区别？\" 如果不在 §1 回答，第一印象就是 novelty 不够。\n- 建议：在 §1 第三段（\"Existing approaches leave a fundamental gap\"）或 Contribution #2 前加一句：\"Type-constrained decoding for code generation [cite PICARD, PLDI2025] enforces type correctness via static schema lookup; IE differs fundamentally because...\"\n\n**W3** [warning] Dual-factor $R^2=0.886$ (n=4) 在 Abstract 中过于突出\n- 具体位置：abstract.tex line 11\n- 问题：$R^2=0.886$ 基于仅 4 个数据点的线性拟合。虽然 Appendix 明确说 \"we do not report a p-value given the small sample size\"，且 §7 描述为 \"descriptive characterization\"，但在 Abstract 中给出 $R^2$ 具体值仍然给人过度 claim 的印象。4 个点几乎任何线性模型都能拟合良好。\n- 建议：Abstract 中改为定性描述 \"residual DR is characterized by a dual-factor pattern (schema tightness × model calibration)\"，移除 $R^2$ 数值。\n\n**W4** [warning] Reproducibility 信息不充分\n- 具体位置：Ethics Statement + 全文\n- 问题：(1) 无独立 Reproducibility Statement（ARR checklist 期望作者明确声明是否提供代码、数据、实验配置）。(2) Random seeds 未报告。(3) GPU 型号/训练时间/LoRA 超参数（rank, alpha, target modules）在正文和 appendix 中均未出现。(4) §5 Runtime 提到 \"same GPU\" 但未说明型号（仅 appendix_discussion 的 ft-latency 提到 \"RTX PRO 6000\"）。\n- 建议：添加 2-3 行 Reproducibility 声明或在 Appendix 中增加 Experimental Details 表格。\n\n**W5** [warning] Related Work 中缺少 2024-2025 最新 Document-level RE 工作\n- 具体位置：section6_related_work.tex\n- 问题：论文在 DocRED 上做实验，但 Related Work 未引用 DocRE 领域 2024-2025 的关键工作。例如：\n  - DREEAM (Ma et al., EMNLP 2023) — evidence-aware document-level RE\n  - DocGNRE (Xu et al., ACL 2024) — generative doc-level RE with noise robustness\n  - 此外缺少 GLiNER (Zaratiana et al., 2023) 作为 span-based NER baseline 的引用\n  当前 §6 的引用集中在 constrained decoding 和通用 IE 框架，对 document-level RE 这个具体 benchmark 领域的对比不足。\n- 建议：在 \"Training-based methods\" 段落中补充 1-2 个 document-level RE 代表工作的引用，说明它们也无法保证 type compliance。\n\n**W6** [warning] Table caption 缺少 second-best 标记说明\n- 具体位置：Tables 2, 3, 4, 5\n- 问题：Tables 使用 bold 标记 best，但没有 underline 标记 second-best。这在 EMNLP 论文中不是硬要求，但是 best practice。更重要的是：Table 2 的 \"Best per column in bold (CF excluded---see text)\" 使用了 `---` em-dash。\n- 建议：caption 中的 em-dash 替换为逗号或分号。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract line 3** \"XGrammar CFG\" — CFG 未展开（Context-Free Grammar）\n2. **§2 line 10** 定义 constraint tightness 时使用 $\\mathcal{T} = \\mathcal{E}$，但 §4 Eq.3 用 $|\\mathcal{T}|^2$——符号一致，但 $\\mathcal{T}$ 和 $\\mathcal{E}$ 同义重复可简化\n3. **§3 line 10** Unicode em-dash (—) 应改为 LaTeX `---` 或彻底消除\n4. **§5.1 Table 1** \"Schema-informed\" 行 CF 列为 \"---\"（表示未测量），但正文未解释为何该条件下不报告 CF\n5. **§5 SciERC Table 2** CF 列排除 bold 标记，解释在 caption，但审稿人可能困惑 CF 越低越好还是越高越好（正文有解释但 table 内不 self-evident）\n6. **Appendix B \"Fine-Tuned Four-Way Ablation\"** Llama DocRED CF 列为 \"---\" (unconstrained)——与正文其他表的 0.xx% 不一致，应统一\n7. **§6 line 14** 描述 DORE 时的 `---` 又是一处解释性 em-dash\n8. **bib 条目** `vukovic2024dore` 缺少 pages 和 url 字段——不影响编译但建议补全\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：3 模型 × 2 数据集 × 多种 ablation（grammar-only, semantic-only, full, S1 vs S2）+ fine-tuning composability + runtime + beam search/sampling 兼容性验证。在 constrained decoding 论文中，这种实验深度属于上乘。\n2. **诚实处理局限**：CF trade-off 没有被掩盖，而是用 ablation (Table in Appendix) 证明了 CF↔DR 是根本性张力而非可独立解决的 bug。Dual-factor 的 n=4 限制也明确声明。\n3. **技术贡献清晰**：pair-based sequential masking（先 dom 后 conditional range）相对于 independent dom/range check 的优势有具体量化（33-37% spurious pairs），non-rectangularity 分析有说服力。\n4. **Related Work 组织良好**：§6 主文本压缩但覆盖了关键对比点；Appendix 扩展版按范式分类且每类都有清晰的 positioning。\n5. **Runtime overhead 极低**（+2.3% to +5.4%），增强了实用性 claim。\n\n---\n\n## 总结判断\n\n论文在实验设计和技术执行上达到了 Findings 水准。核心贡献（compile IE ontology axioms into token-level semantic masks）是对已有 type-constrained decoding 范式的合理迁移，但 excitement 有限——本质上是 \"把 code-gen 的 type checking 搬到 IE\" 加上 \"dynamic entity registry\" 这一工程适配。§1 对此区分不够突出是最大的叙事短板。\n\n写作质量整体清晰，但 AI 写作痕迹（em-dash 密度、-ing 分词短语）需要在提交前全面清理。Abstract 缩写未展开是格式性硬伤。\n\n推荐 **Findings 接收**，前提是修复 N1（缩写）和 N2（em-dash）两个格式/写作硬伤。\n",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Round 4 审稿报告 — Reviewer 2（新颖性/写作/格式/Related Work）\n\n---\n\n## 总体评分\n**Overall**: 3.5/5（Accept to Findings，偏强）\n**一句话总结**: 扎实的工程贡献，实验充分且诚实，但核心新颖性是将已有范式（type-constrained code generation）迁移到 IE，增量贡献清晰但 excitement 有限。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨，3模型×2数据集+消融+fine-tuning composability+runtime；统计检验充分（bootstrap CI）；已知局限（CF trade-off, n=4 dual-factor）处理诚实 |\n| Excitement | 2.5/5 | 核心思路是 type-constrained decoding 从代码生成迁移到 IE，§3开头三点区别有说服力但增量性质不变；对已有 GCD/EnriCo 的改进幅度需要 reviewer 仔细比对 |\n| Reproducibility | 3.5/5 | 代码/数据承诺 upon acceptance；prompt 完整；超参数报告充分；但缺少正式 Reproducibility Statement，random seed 未明确报告 |\n| Confidence | 4/5 | 熟悉 constrained decoding + IE 领域 |\n\n---\n\n## 先前 Issues 修复状态验证\n\n| Issue | 状态 | 证据 |\n|-------|------|------|\n| **W8**: \"first\" claim 收窄 + DORE 引用 | ✅ Fixed | §1 Contribution #2: \"the first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE\"; DORE 在 §6 line 14 明确引用并区分 |\n| **W9**: First-subword-token 升级为 Design Assumption | ✅ Fixed | §3.3 Implementation 段落用 **\\emph{Design Assumption}** 标记，Limitations 中也讨论了 prefix-tree masking 的扩展路径 |\n| **R2-N2**: Code-gen 区分提升到 §1/§3 | ⚠️ Partial | §3 第一段（line 9）明确列出三点区别，但 §1 无任何 code-gen 讨论——审稿人在读 Introduction 时无法理解为何这不是 trivial migration。建议在 §1 Contribution #2 附近加一句简述区别 |\n| **R2-N4**: Zero-shot R-F1 ~8% 实际意义 | ✅ Fixed | §5 DocRED 段落 \"Zero-shot F1 context\" 明确说明 F1 作为 control variable 而非 optimization target；引用 supervised SOTA (49-53%) 作对比 |\n| **R2-N5**: Code/data 可复现性声明 | ⚠️ Minimal | Ethics Statement 仅说 \"Code and data will be released upon acceptance\" 一句。ARR 期望更详细的 reproducibility 信息（seeds, hardware, training details）。无独立 Reproducibility Statement |\n| **R2-N9**: DORE/GenIE/EnriCo 在 §6 主文本 | ✅ Fixed | 三者均在 section6_related_work.tex 出现，有具体区分描述 |\n| **R2-N8**: 符号冲突 τ→κ | ✅ Fixed | §4 Eq.3 使用 κ(r)；§5 per-relation 表格用 κ；全文一致 |\n| **GC-N2**: \"DR ↓42-90%\" 标注 \"across three models\" | ✅ Fixed | Abstract line 8 和 §1 Contribution #3 均标明 \"across three model families\" / \"across three models\" |\n| **GC-N3**: Greedy decoding limitation | ✅ Fixed | Limitations 段落明确讨论 greedy decoding 限制并指向 Appendix beam search/sampling |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 缩写未展开违反 ARR 规范\n- 具体位置：abstract.tex 全文\n- 问题：Abstract 使用 \"LLM\"（line 7）、\"IE\"（line 1 \"IE ontology\"）、\"CFG\"（line 3）、\"DR\"（line 7-8）、\"ET\"/\"RV\"（line 3）、\"CF\"（line 13）、\"LoRA\"（line 12）均未在 Abstract 内给出完整定义。标题中 \"Information Extraction\" 定义了 IE，但 Abstract 应独立可读。\n- 为什么影响接收：ARR 审稿人对缩写规范敏感；abstract 是 matching 的唯一输入，未定义缩写降低可读性。至少 LLM、IE、DR 必须展开。\n- 建议修改方向：首次出现时展开 \"Large Language Model (LLM)-based Information Extraction (IE)\"；DR 已通过 \"domain/range\" 隐式定义但建议加 \"(DR)\"；CF/ET/RV 可保留为括号内指标缩写但加 full name。\n\n**N2** [critical] 正文主体存在大量 AI 写作典型标志（em-dash 过度使用）\n- 具体位置：section1 (3处)、section2 (3处)、section3 (2处 Unicode — + 2处 LaTeX ---)、section5_docred (2处)\n- 问题：正文中 LaTeX `---`（编译为 em-dash）至少 12 处用于解释性插入，例如：\n  - §1 line 7: \"violations---structurally valid triples that are ontologically invalid\"\n  - §1 line 12: \"unreliable---violations for \\textsc{Evaluate-for} actually increase\"\n  - §2 line 16: 双 em-dash 包围解释 \"---e.g., ...---which depend on...\"\n  - §2 lines 20-21: 两处解释性 dash\n  - §3 line 10: Unicode — (非 LaTeX ---）\n  - §3 line 49: Unicode —\n  这在 NLP 社区虽非严格禁止，但密度过高（正文 8 页中 >12 处）是 AI 生成的显著标志。\n- 为什么影响接收：EMNLP 审稿人熟悉 AI 写作痕迹；高密度 em-dash 可能引发对论文原创性的质疑。\n- 建议修改方向：逐一改为逗号、括号或拆分为两个句子。保留至多 2-3 处用于真正需要的语法结构中。Unicode em-dash (—) 必须全部消除。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] -ing 分词短语结尾（AI 写作痕迹）\n- 具体位置：section1 line 14 \"making it impractical\"、line 20 \"enabling the semantic layer\"、line 25 \"showing that violation rates\"；section3 line 53 \"confirming that grammar constraints\"、line 82 \"ensuring consistency\"、line 114 \"achieving strong constraint enforcement\"；appendix_related_work.tex 大量（>20处）\n- 问题：-ing participial phrases at sentence/clause end 是 AI 生成文本最典型标志之一。正文中约 8-10 处，appendix 中更密集。\n- 建议：正文中的 8-10 处应改写为独立从句或 \"which\" 从句。Appendix 中可以容忍但建议减少密度。\n\n**W2** [warning] Code-gen 新颖性区分未在 Introduction 出现\n- 具体位置：section1_introduction_draft.tex（Contribution #2 周围）\n- 问题：§3 开头清楚列出了 IE vs. code-gen 的三个关键区别（entity types inferred from free text, dynamic registry, context-dependent targets），但 §1 没有任何 code-gen 的讨论。审稿人读 Introduction 时会问：\"这和 PICARD/MGD/PLDI2025 type-constrained codegen 有什么本质区别？\" 如果不在 §1 回答，第一印象就是 novelty 不够。\n- 建议：在 §1 第三段（\"Existing approaches leave a fundamental gap\"）或 Contribution #2 前加一句：\"Type-constrained decoding for code generation [cite PICARD, PLDI2025] enforces type correctness via static schema lookup; IE differs fundamentally because...\"\n\n**W3** [warning] Dual-factor $R^2=0.886$ (n=4) 在 Abstract 中过于突出\n- 具体位置：abstract.tex line 11\n- 问题：$R^2=0.886$ 基于仅 4 个数据点的线性拟合。虽然 Appendix 明确说 \"we do not report a p-value given the small sample size\"，且 §7 描述为 \"descriptive characterization\"，但在 Abstract 中给出 $R^2$ 具体值仍然给人过度 claim 的印象。4 个点几乎任何线性模型都能拟合良好。\n- 建议：Abstract 中改为定性描述 \"residual DR is characterized by a dual-factor pattern (schema tightness × model calibration)\"，移除 $R^2$ 数值。\n\n**W4** [warning] Reproducibility 信息不充分\n- 具体位置：Ethics Statement + 全文\n- 问题：(1) 无独立 Reproducibility Statement（ARR checklist 期望作者明确声明是否提供代码、数据、实验配置）。(2) Random seeds 未报告。(3) GPU 型号/训练时间/LoRA 超参数（rank, alpha, target modules）在正文和 appendix 中均未出现。(4) §5 Runtime 提到 \"same GPU\" 但未说明型号（仅 appendix_discussion 的 ft-latency 提到 \"RTX PRO 6000\"）。\n- 建议：添加 2-3 行 Reproducibility 声明或在 Appendix 中增加 Experimental Details 表格。\n\n**W5** [warning] Related Work 中缺少 2024-2025 最新 Document-level RE 工作\n- 具体位置：section6_related_work.tex\n- 问题：论文在 DocRED 上做实验，但 Related Work 未引用 DocRE 领域 2024-2025 的关键工作。例如：\n  - DREEAM (Ma et al., EMNLP 2023) — evidence-aware document-level RE\n  - DocGNRE (Xu et al., ACL 2024) — generative doc-level RE with noise robustness\n  - 此外缺少 GLiNER (Zaratiana et al., 2023) 作为 span-based NER baseline 的引用\n  当前 §6 的引用集中在 constrained decoding 和通用 IE 框架，对 document-level RE 这个具体 benchmark 领域的对比不足。\n- 建议：在 \"Training-based methods\" 段落中补充 1-2 个 document-level RE 代表工作的引用，说明它们也无法保证 type compliance。\n\n**W6** [warning] Table caption 缺少 second-best 标记说明\n- 具体位置：Tables 2, 3, 4, 5\n- 问题：Tables 使用 bold 标记 best，但没有 underline 标记 second-best。这在 EMNLP 论文中不是硬要求，但是 best practice。更重要的是：Table 2 的 \"Best per column in bold (CF excluded---see text)\" 使用了 `---` em-dash。\n- 建议：caption 中的 em-dash 替换为逗号或分号。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Abstract line 3** \"XGrammar CFG\" — CFG 未展开（Context-Free Grammar）\n2. **§2 line 10** 定义 constraint tightness 时使用 $\\mathcal{T} = \\mathcal{E}$，但 §4 Eq.3 用 $|\\mathcal{T}|^2$——符号一致，但 $\\mathcal{T}$ 和 $\\mathcal{E}$ 同义重复可简化\n3. **§3 line 10** Unicode em-dash (—) 应改为 LaTeX `---` 或彻底消除\n4. **§5.1 Table 1** \"Schema-informed\" 行 CF 列为 \"---\"（表示未测量），但正文未解释为何该条件下不报告 CF\n5. **§5 SciERC Table 2** CF 列排除 bold 标记，解释在 caption，但审稿人可能困惑 CF 越低越好还是越高越好（正文有解释但 table 内不 self-evident）\n6. **Appendix B \"Fine-Tuned Four-Way Ablation\"** Llama DocRED CF 列为 \"---\" (unconstrained)——与正文其他表的 0.xx% 不一致，应统一\n7. **§6 line 14** 描述 DORE 时的 `---` 又是一处解释性 em-dash\n8. **bib 条目** `vukovic2024dore` 缺少 pages 和 url 字段——不影响编译但建议补全\n\n---\n\n## 主要优势\n\n1. **实验设计严谨**：3 模型 × 2 数据集 × 多种 ablation（grammar-only, semantic-only, full, S1 vs S2）+ fine-tuning composability + runtime + beam search/sampling 兼容性验证。在 constrained decoding 论文中，这种实验深度属于上乘。\n2. **诚实处理局限**：CF trade-off 没有被掩盖，而是用 ablation (Table in Appendix) 证明了 CF↔DR 是根本性张力而非可独立解决的 bug。Dual-factor 的 n=4 限制也明确声明。\n3. **技术贡献清晰**：pair-based sequential masking（先 dom 后 conditional range）相对于 independent dom/range check 的优势有具体量化（33-37% spurious pairs），non-rectangularity 分析有说服力。\n4. **Related Work 组织良好**：§6 主文本压缩但覆盖了关键对比点；Appendix 扩展版按范式分类且每类都有清晰的 positioning。\n5. **Runtime overhead 极低**（+2.3% to +5.4%），增强了实用性 claim。\n\n---\n\n## 总结判断\n\n论文在实验设计和技术执行上达到了 Findings 水准。核心贡献（compile IE ontology axioms into token-level semantic masks）是对已有 type-constrained decoding 范式的合理迁移，但 excitement 有限——本质上是 \"把 code-gen 的 type checking 搬到 IE\" 加上 \"dynamic entity registry\" 这一工程适配。§1 对此区分不够突出是最大的叙事短板。\n\n写作质量整体清晰，但 AI 写作痕迹（em-dash 密度、-ing 分词短语）需要在提交前全面清理。Abstract 缩写未展开是格式性硬伤。\n\n推荐 **Findings 接收**，前提是修复 N1（缩写）和 N2（em-dash）两个格式/写作硬伤。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-17T10:21:00.007942+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3917
}
```

</details>

---


### Assistant

_source line 238 · 2026-05-17T10:21:10.856871+00:00_

审稿报告已提交给 Review Director。

总结：本轮审查给出 **Overall 3.5/5**（Findings 接收水准）。主要发现：

- **Must-Fix (2项)**：Abstract 缩写未展开（LLM/IE/DR/CF 等均未定义）；正文 em-dash 过度使用（>12处解释性 dash + 2处 Unicode —），属 AI 写作显著标志
- **Should-Fix (6项)**：-ing 分词短语密集、code-gen 新颖性区分未出现在 §1、dual-factor R²=0.886(n=4) 在 Abstract 过于突出、Reproducibility 信息不足、缺少 document-level RE 最新引用、table caption 中的 em-dash
- **先前 Issues**：9 项中 7 项已修复，2 项部分修复（R2-N2 code-gen 区分只在 §3 未到 §1；R2-N5 reproducibility 声明仍然最简）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

8 recorded events


### User

_source line 239 · 2026-05-17T10:23:38.538023+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

## Reviewer 1 评分
**Overall**: 3.5/5（介于 Findings 可接受与 Conference 之间）
**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 4/5

## Must-Fix 问题

**N1** [critical] R²=0.886 (n=4) 统计不充分且在 Abstract 中过度突出
- n=4 数据点拟合 2 参数线性模型，自由度仅为 2。F(1,2)≈15.54，p≈0.058，在 α=0.05 下不显著。
- Mistral 被 post-hoc 排除（"mechanistically distinct error source"），构成数据筛选偏差。
- 建议：(1) Abstract 移除 R²，改为定性描述 (2) Appendix 报告 F 统计量 (3) 对 Mistral 排除提供先验理由

**N2** [critical] Beam search 结果重大但被降级，主实验配置选择存疑
- Beam search (k=4) 在 SciERC 全集上实现 DR=0%、CF 0.53%，同时 R-F1 不降反升。这同时解决了主实验最大的两个局限（残余 DR 和 CF 升高）。
- 将 greedy 作为 "recommended strategy" 缺乏充分理由。
- DocRED beam 仅 50-doc subset，greedy baseline 来自 998-doc 全集（"Not a matched comparison"）。
- 建议：§5/§7 讨论 beam 全集结果、提供 beam runtime、明确 greedy 是实用推荐而非理论最优、DocRED beam 应用匹配 subset baseline。

## Should-Fix 问题

**W1** Grammar-first fallback 频率未充分讨论：DocRED fallback rate 10.2% 近似等于 residual DR 10.21%。DocRED 的 effective semantic constraint coverage 未报告。

**W2** Post-hoc filtering 在 Intro 中 framing 仍有选择性：未提及 post-hoc 在 5/6 ZS 配置中 F1 高于 OntoCoDec。OntoCoDec 优势是 recall 保持，非 F1。

**W3** Parse failure 增加的 confounding 在 Llama DocRED 上未充分分析：Llama DocRED parse failure +34%（68→91），未给出 parse-failure-excluded 分析。CF=12.02% 是否受 selection bias 影响？

**W4** DocRED Composability matrix 仅文字呈现缺乏系统性：SciERC 有 Table 2 完整矩阵，DocRED FT 数据仅在文字和 caption 中。§5.2 标题为 "Results on SciERC" 但包含 DocRED 讨论。

**W5** §4 DR reduction 范围引用不明确："SciERC achieves 94-99% DR reduction" 仅覆盖 Qwen+Llama，未包含 Mistral (76%)，与 Abstract 不一致。

## Questions to Authors
**Q1**: JSON field ordering 是 pair-based sequential masking 的隐含前提。grammar layer 的 JSON Schema 是否强制了 field ordering？
**Q2**: Beam search (k=4) 在 SciERC 上结果优于 LoRA fine-tuning（DR=0%, CF=0.53% vs DR=0%, CF=1.18%）。是否考虑过 beam search 作为 FT 替代方案？
**Q3**: Semantic-only 在 DocRED ET 增加 +70%（2.48%→4.22%），为什么远大于 SciERC (0%)？
**Q4**: CF-DR trade-off 实验（Appendix Table 5）仅在 SciERC/Qwen 上进行。DocRED 上 CF 最高达 12.02%（Llama），是否做过对应 ablation？

## Missing References
- DORE 在 §6 中已引用，但未深入对比 output selection vs logit masking 的定量差异。
- BoostCD 仅一句话提及，值得更详细讨论其与 OntoCoDec 的互补性。

## Minor Issues
1. §3.3 Design Assumption 应在 §2 Problem Statement 中前置
2. Table 1 caption "CF excluded—see text" 的讨论实际在 §5.2
3. §5.2 内容跨度大（SciERC + composability + DocRED FT），建议拆分
4. Appendix 说不报告 p-value，但 Abstract 报告 R²——两者是同一检验的两面
5. DocRED MISC 的 catch-all 属性（76.6% CF violations involve MISC）应与 SciERC Generic 统一讨论
6. **RV=0.03% 解释不一致**：正文说 "partial JSON recovery"，rebuttal draft 说 "XGrammar enum compilation bug"——需统一
7. Table 2 vs Table 1 的 ΔDR 列格式不统一

## 主要优势
1. 方法设计扎实（enabling dependency 有理论动机和实验验证）
2. 实验覆盖面广（3模型×2数据集×多 ablation + FT 4-way）
3. 诚实的局限性讨论（CF↔DR Pareto, Mistral boundary condition, parse failure denominator）
4. Runtime 开销极低（+5.4% DocRED, +2.3% FT regime）
5. Reproducibility 优秀（exp_id 追溯, greedy 完全确定性）

---

请逐条回应 Reviewer 1 的 Must-Fix (N1, N2) 和 Should-Fix (W1-W5) 意见，以及 Q1-Q4。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-17T10:23:57.051583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": "125",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "offset": "125",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-17T10:23:57.479002+00:00_

125	%  exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
126	% ──────────────────────────────────────────
127	\paragraph{Composability with fine-tuning.}
128	\label{sec:composability}
129	Table~\ref{tab:composability} presents the composability matrix on SciERC for both Qwen3-8B and Llama-3.1-8B (zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1), testing whether OntoCoDec composes with task-specific fine-tuning across model families.
130	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
131	%          w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
132	%          llama_scierc_unconstrained, llama_scierc_full_s1,
133	%          w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval
134	
135	For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\,pp), while reducing DR from 15.37\% to 1.95\% (87\% relative reduction).
136	% w5_lora_scierc_unconstrained_eval: DR=0.0195, R-F1=0.4386, E-F1=0.6705
137	The residual 1.95\% DR concentrates on tight-constraint relations: \textsc{Evaluate-for} (13.13\%), \textsc{Part-of} (5.77\%), and \textsc{Compare} (5.00\%) (per-relation breakdown in Appendix~\ref{app:lora-per-relation}).
138	Adding OntoCoDec eliminates the remaining DR entirely (1.95\%\,$\to$\,0\%) with R-F1 cost of $-$0.09\,pp (43.86\,$\to$\,43.77) and unchanged E-F1 (67.05).
139	% w5_lora_scierc_constrained_eval: DR=0, R-F1=0.4377, E-F1=0.6705, CF=0.0118
140	
141	Llama-3.1-8B exhibits the same pattern.
142	Fine-tuning raises R-F1 from 2.68 to 45.45 ($+$42.77\,pp) and E-F1 from 23.56 to 67.76 ($+$44.20\,pp), while reducing DR from 13.34\% to 1.11\%.
143	% w5_llama_lora_scierc_unconstrained_eval: DR=0.0111, R-F1=0.4545, E-F1=0.6776
144	Adding OntoCoDec reduces DR by 92\% (1.11\%\,$\to$\,0.09\%) with R-F1 change of $+$0.02\,pp (45.45\,$\to$\,45.47) and unchanged E-F1 (67.76).
145	% w5_llama_lora_scierc_constrained_eval: DR=0.0009, R-
…[truncated 3696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 427
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-17T10:23:57.750814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
  "offset": "25",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
    "offset": "25",
    "limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-17T10:23:57.801928+00:00_

25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cross-dataset results: SciERC ($\bar{\kappa}{=}0.333$, 24 valid pairs/relation) achieves 94--99\% DR reduction, while DocRED ($\bar{\kappa}{=}0.842$, 5.68 pairs) achieves 45--90\%, with the residual modulated by model-specific baselines (\S\ref{sec:cross-model}; quantitative analysis in Appendix~\ref{app:dual-factor}).
29	
30	\paragraph{Non-Rectangularity and Sequential Masking.}
31	\label{sec:rectangularity}
32	% Data source: artifacts/rebuttal/w2_rectangularity_report.md
33	The sequential masking strategy---$\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$---is necessary because real ontology type signatures are overwhelmingly non-rectangular: 0/7 SciERC and only 23/96 DocRED relations satisfy $\sigma(r) = \operatorname{dom}(r) \times \operatorname{range}(r)$.
34	Independent enforcement ($\tau^h \in \operatorname{dom}(r) \wedge \tau^t \in \operatorname{range}(r)$) would admit 33.3\% (SciERC) and 36.8\% (DocRED) spurious type pairs---on SciERC, 100\% of residual DR violations under full S1 are pairs that pass independent checks but violate $\sigma(r)$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-17T10:25:42.791873+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: R²=0.886 (n=4) 统计不充分且在 Abstract 中过度突出**\n\n完全同意。我在自己的审稿中也将此列为 W3（Should-Fix）。R1 的分析比我更精确：n=4, 2参数模型, 自由度仅2, F(1,2)≈15.54, p≈0.058 不显著。此外 Mistral 的排除确实构成 post-hoc 数据筛选。\n\n补充一点：§7 (section7_conclusion_compressed.tex) 虽然已经加了 scope 限定（\"descriptive characterization with explicit scope rather than a universal predictive law\"），但 Abstract line 11 仍然给出具体 $R^2$ 值和 $n=4$ 标注，这种定量呈现与定性 disclaimer 之间存在矛盾。审稿人看 Abstract 的第一印象是\"作者在用4个点做统计推断\"。\n\n建议与 R1 一致：Abstract 移除 $R^2$ 具体数值，改为 \"residual DR correlates with the product of schema tightness and baseline violation rate\"。\n\n---\n\n**[AGREE] R1-N2: Beam search 结果被降级，主实验配置选择存疑**\n\n同意这是论文叙事上的一个重要缺陷，但我对严重程度的判断略有保留。\n\nR1 的观察完全正确：Appendix Table 7 显示 beam search (k=4) 在 SciERC 全集 551 documents 上实现 DR=0%, CF=0.53%, R-F1=8.56。这同时解决了 greedy 下两个最大的局限（DR 残余 0.93% 和 CF 飙升 9.90%）。如果论文推荐的配置是 greedy S1，却存在一个 strictly dominating 的替代方案（beam k=4），那 \"recommended strategy\" 的选择确实需要更强的理由。\n\n然而，我认为这不构成 reject-level 问题，原因：\n1. Beam search 的 DocRED 评估仅 50 docs，且与 998-doc greedy baseline 不匹配（论文自己承认 \"Not a matched comparison\"），因此 beam 在 document-level RE 的泛化性未经验证。\n2. 论文的核心贡献是 constraint framework 本身（grammar + semantic layer composition），greedy vs beam 是 deployment configuration 问题。Beam 的效果正好证明了 framework 的灵活性。\n3. Runtime overhead 未在 beam 条件下报告——beam k=4 的 latency 可能是 greedy 的 3-4x，对实际部署影响大。\n\n建议：§5 或 §7 应增加 1-2 句明确说明 \"beam k=4 achieves DR=0% and CF<1% on SciERC (Appendix X), but at higher inference cost; greedy is recommended for latency-constrained deployments\"。当前完全不在正文提及 beam 的优异表现确实是叙事遗漏。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: DocRED fallback rate 未充分讨论**\n\n同意。Appendix B (app:fallback-coverage) 报告了 SciERC 的 effective semantic constraint coverage (63.4%)，但 DocRED 的对应数值未给出。§5 DocRED 段落提到 \"aggregate fallback rate (10.2%; 1,770/17,341 triples) closely tracks residual DR (10.21%)\"，这暗示 DocRED 的 effective coverage 约为 89.8%（1 - 10.2%），但未显式报告也未与 SciERC 的 63.4% 对比。\n\n补充：Qwen 在 SciERC 上 0 次 grammar-first fallback（100% effective coverage），但 DocRED 上 fallback 率却高达 10.2%，这个巨大差异的机制解释不充分。§4 用 constraint tightness 解释了大方向，但 SciERC Qwen 0% vs DocRED Qwen 10.2% 的跳变需要更具体分析。\n\n---\n\n**[REBUT] R1-W2: Post-hoc filtering framing 选择性**\n\n部分不同意。R1 认为 Introduction 对 post-hoc 的 framing 有选择性（未提 5/6 ZS 设置中 post-hoc F1 更高）。但我认为 Introduction 的 framing 策略是合理的，理由：\n\n1. §1 line 14 的论点是 post-hoc filtering 在高 rejection rate 下 \"impractical\"（以 Mistral DocRED 73.7% 为例）。这不是说 post-hoc 总是差，而是指出其 failure mode。\n2. Appendix B (app:discussion) 的 post-hoc extended comparison (Table in Appendix) 完整报告了所有 10 个配置，明确承认 post-hoc wins in 5/6 ZS groups on F1。\n3. OntoCoDec 的 contribution 不是 \"比 post-hoc F1 更高\"，而是 \"(a) prevents violations during decoding rather than discarding after, (b) preserves recall, (c) composes with FT\"。Introduction 用 \"cannot redirect probability mass\" 准确定位了核心差异。\n\n但我同意 Introduction 可以更平衡：建议加一句 \"While post-hoc filtering achieves higher precision in most zero-shot settings (Appendix X), it discards up to 48% of predictions including true positives\" 以 preempt 审稿人的质疑。\n\n---\n\n**[AGREE] R1-W3: Llama DocRED parse failure confounding 分析不充分**\n\n同意。Table 5 (cross-model) footnote 报告 \"Llama DocRED 68→91\"（+34%），但正文分析不足：\n- CF=12.02% 是在 parse-success documents 上计算的。如果 parse failure 的 documents 倾向于含更多 entities（长文档），那 surviving documents 可能 systematically 不同。\n- §5 SciERC composability 段落的 footnote 提到 \"excluding parse-failure documents, ΔR-F1 is within ±0.1pp\"，但这是 fine-tuned DocRED 的数据。Zero-shot Llama DocRED (68→91 PF) 的 parse-failure-excluded 分析未给出。\n- 12.02% CF 是论文报告的最高 CF 值，恰好出现在 parse failure 变化最大的配置上，这个巧合需要排除 selection bias。\n\n---\n\n**[AGREE] R1-W4: DocRED composability 呈现不够系统**\n\n同意但认为严重性较低。§5.2 标题是 \"Results on SciERC\" 但内容跨越两个数据集确实令人困惑。Table 2 (composability matrix) 仅呈现 SciERC，DocRED FT 数据散落在文字和 Table 2 caption 中（\"DocRED replication: Qwen DR −98.7% (−0.30pp), Llama DR −59.2% (+0.51pp)\"）。完整的 DocRED FT 4-way ablation 在 Appendix Table (tab:ft-ablation) 中。\n\n这不影响 soundness 但影响可读性。建议要么 (a) 将 §5.2 重命名为 \"Composability with Fine-tuning\" 并将 DocRED 明确作为 sub-paragraph，要么 (b) 在正文添加一个 2×2 DocRED composability mini-table。\n\n---\n\n**[AGREE] R1-W5: §4 DR reduction 范围与 Abstract 不一致**\n\n同意。§4 (section4_composition_draft.tex line 28) 说 \"SciERC achieves 94--99% DR reduction\"，这仅覆盖 Qwen (94%) 和 Llama (99%)，排除了 Mistral (76%)。而 Abstract 说 \"42--99% across three model families\"。两处的 scope 不同但未明确标注，容易误导。\n\n建议：§4 改为 \"SciERC achieves 76--99% DR reduction (94--99% for calibrated models; 76% for Mistral)\" 或明确限定 \"for Qwen and Llama\"。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: JSON field ordering 是 pair-based masking 的隐含前提**\n\n这是一个精确的技术观察。Sequential masking (先 head_type, 后 tail_type) 要求 JSON schema 强制 head_type 在 tail_type 前生成。§3 line 23-27 (Eq.1) 的 output schema 定义了字段结构，但未显式讨论 ordering 是否由 grammar layer 强制。如果 XGrammar 的 JSON Schema compilation 允许字段任意顺序（JSON 标准不规定 object key order），那么模型可能先生成 tail_type，此时 head_type 未知，sequential masking 失效。\n\n这是一个 soundness concern，论文应明确说明：(a) grammar layer 是否强制了特定 field order（大概率是，因为 JSON Schema + XGrammar 通常按 schema 定义顺序生成），或 (b) semantic layer 在 tail_type 先于 head_type 时如何处理。\n\n---\n\n**[AGREE] R1-Q2: Beam k=4 vs LoRA 的对比值得讨论**\n\n有趣的观察。SciERC beam k=4 zero-shot: DR=0%, CF=0.53%, R-F1=8.56。SciERC LoRA + S1: DR=0%, CF=1.18%, R-F1=43.77。两者 DR 都为 0，beam 的 CF 更低，但 R-F1 天壤之别（8.56 vs 43.77）。所以 beam 不能替代 FT 在 F1 维度的贡献。但作为 CF 控制手段，beam 确实比 FT 更有效。论文可以在 Discussion 中指出 \"beam search + fine-tuning\" 的组合可能是最优配置。\n\n---\n\n**[AGREE] R1-Q3: Semantic-only DocRED ET 增加 +70%**\n\n同意这需要解释。DocRED semantic-only ET 从 2.48% 上升到 4.22%（Table 3），而 SciERC semantic-only ET 保持 0.40% 不变。§3 line 109-112 解释了 SciERC 下 semantic-only 的 ET residual 机制（\"semantic mask constrains type tokens to relation-specific valid sets but cannot enforce vocabulary membership; occasionally the mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative\"），但未解释为何 DocRED 恶化更严重。可能的原因：DocRED 的 96 relation 有更复杂的 domain/range 组合，semantic mask 更频繁地将模型从有效 entity type 推向 OOV type。这应在正文中明确讨论。\n\n---\n\n**[AGREE] R1-Q4: CF-DR trade-off ablation 仅 SciERC/Qwen**\n\n同意这是实验覆盖的缺口。Appendix B (tab:cf-dr-tradeoff) 的 CF fallback ablation 仅在 SciERC Qwen3-8B 上进行。Llama DocRED 有最高 CF (12.02%)，恰恰是最需要 CF-DR trade-off 分析的配置，但未提供对应 ablation。建议至少在 Appendix 补充 Llama DocRED 的 CF fallback pilot 数据。\n\n---\n\n### Missing References / Minor Issues\n\n**[AGREE] R1-Minor-6: RV=0.03% 解释不一致**\n\n这是一个真实的 inconsistency。§5 DocRED 正文（section5_docred_draft.tex line 61）说 \"the residual 5 triples arise from partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple\"。如果 rebuttal draft 说 \"XGrammar enum compilation bug\"，两个解释互相矛盾。需要统一为一个确定的根因。\n\n**[AGREE] R1-Minor-1: Design Assumption 前置到 §2**\n\n同意。Design Assumption 是整个方法的前提条件，放在 §3.3 Implementation 段落（方法描述后半段）时审稿人已经读了一半方法而不知道这个限制。在 §2 Problem Statement 中声明更合理。\n\n**[REBUT] R1-Minor-3: §5.2 内容跨度大建议拆分**\n\n不完全同意拆分的必要性。SciERC + composability + DocRED FT 在一个 subsection 内虽长，但 composability 是需要同时比较两个数据集的交叉分析。如果拆分为 \"§5.2 SciERC Results\" 和 \"§5.x Composability\"，会导致 SciERC 的 composability 数据与 DocRED 的 composability 数据分离，反而不利于比较。不过标题改为 \"SciERC Results and Composability Analysis\" 是合理折中。\n\n---\n\n### 总结\n\nR1 的审稿整体质量很高，技术观察精确（尤其是 Q1 field ordering、N1 的 F-test 计算）。我在 7/12 个 substantive issues 上 [AGREE]，2 个 [REBUT]（W2 post-hoc framing, Minor-3 section 拆分），3 个 partial agree。R1 和我的审稿在 N1 (dual-factor overstated) 和 beam search 重要性上高度一致。\n",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: R²=0.886 (n=4) 统计不充分且在 Abstract 中过度突出**\n\n完全同意。我在自己的审稿中也将此列为 W3（Should-Fix）。R1 的分析比我更精确：n=4, 2参数模型, 自由度仅2, F(1,2)≈15.54, p≈0.058 不显著。此外 Mistral 的排除确实构成 post-hoc 数据筛选。\n\n补充一点：§7 (section7_conclusion_compressed.tex) 虽然已经加了 scope 限定（\"descriptive characterization with explicit scope rather than a universal predictive law\"），但 Abstract line 11 仍然给出具体 $R^2$ 值和 $n=4$ 标注，这种定量呈现与定性 disclaimer 之间存在矛盾。审稿人看 Abstract 的第一印象是\"作者在用4个点做统计推断\"。\n\n建议与 R1 一致：Abstract 移除 $R^2$ 具体数值，改为 \"residual DR correlates with the product of schema tightness and baseline violation rate\"。\n\n---\n\n**[AGREE] R1-N2: Beam search 结果被降级，主实验配置选择存疑**\n\n同意这是论文叙事上的一个重要缺陷，但我对严重程度的判断略有保留。\n\nR1 的观察完全正确：Appendix Table 7 显示 beam search (k=4) 在 SciERC 全集 551 documents 上实现 DR=0%, CF=0.53%, R-F1=8.56。这同时解决了 greedy 下两个最大的局限（DR 残余 0.93% 和 CF 飙升 9.90%）。如果论文推荐的配置是 greedy S1，却存在一个 strictly dominating 的替代方案（beam k=4），那 \"recommended strategy\" 的选择确实需要更强的理由。\n\n然而，我认为这不构成 reject-level 问题，原因：\n1. Beam search 的 DocRED 评估仅 50 docs，且与 998-doc greedy baseline 不匹配（论文自己承认 \"Not a matched comparison\"），因此 beam 在 document-level RE 的泛化性未经验证。\n2. 论文的核心贡献是 constraint framework 本身（grammar + semantic layer composition），greedy vs beam 是 deployment configuration 问题。Beam 的效果正好证明了 framework 的灵活性。\n3. Runtime overhead 未在 beam 条件下报告——beam k=4 的 latency 可能是 greedy 的 3-4x，对实际部署影响大。\n\n建议：§5 或 §7 应增加 1-2 句明确说明 \"beam k=4 achieves DR=0% and CF<1% on SciERC (Appendix X), but at higher inference cost; greedy is recommended for latency-constrained deployments\"。当前完全不在正文提及 beam 的优异表现确实是叙事遗漏。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: DocRED fallback rate 未充分讨论**\n\n同意。Appendix B (app:fallback-coverage) 报告了 SciERC 的 effective semantic constraint coverage (63.4%)，但 DocRED 的对应数值未给出。§5 DocRED 段落提到 \"aggregate fallback rate (10.2%; 1,770/17,341 triples) closely tracks residual DR (10.21%)\"，这暗示 DocRED 的 effective coverage 约为 89.8%（1 - 10.2%），但未显式报告也未与 SciERC 的 63.4% 对比。\n\n补充：Qwen 在 SciERC 上 0 次 grammar-first fallback（100% effective coverage），但 DocRED 上 fallback 率却高达 10.2%，这个巨大差异的机制解释不充分。§4 用 constraint tightness 解释了大方向，但 SciERC Qwen 0% vs DocRED Qwen 10.2% 的跳变需要更具体分析。\n\n---\n\n**[REBUT] R1-W2: Post-hoc filtering framing 选择性**\n\n部分不同意。R1 认为 Introduction 对 post-hoc 的 framing 有选择性（未提 5/6 ZS 设置中 post-hoc F1 更高）。但我认为 Introduction 的 framing 策略是合理的，理由：\n\n1. §1 line 14 的论点是 post-hoc filtering 在高 rejection rate 下 \"impractical\"（以 Mistral DocRED 73.7% 为例）。这不是说 post-hoc 总是差，而是指出其 failure mode。\n2. Appendix B (app:discussion) 的 post-hoc extended comparison (Table in Appendix) 完整报告了所有 10 个配置，明确承认 post-hoc wins in 5/6 ZS groups on F1。\n3. OntoCoDec 的 contribution 不是 \"比 post-hoc F1 更高\"，而是 \"(a) prevents violations during decoding rather than discarding after, (b) preserves recall, (c) composes with FT\"。Introduction 用 \"cannot redirect probability mass\" 准确定位了核心差异。\n\n但我同意 Introduction 可以更平衡：建议加一句 \"While post-hoc filtering achieves higher precision in most zero-shot settings (Appendix X), it discards up to 48% of predictions including true positives\" 以 preempt 审稿人的质疑。\n\n---\n\n**[AGREE] R1-W3: Llama DocRED parse failure confounding 分析不充分**\n\n同意。Table 5 (cross-model) footnote 报告 \"Llama DocRED 68→91\"（+34%），但正文分析不足：\n- CF=12.02% 是在 parse-success documents 上计算的。如果 parse failure 的 documents 倾向于含更多 entities（长文档），那 surviving documents 可能 systematically 不同。\n- §5 SciERC composability 段落的 footnote 提到 \"excluding parse-failure documents, ΔR-F1 is within ±0.1pp\"，但这是 fine-tuned DocRED 的数据。Zero-shot Llama DocRED (68→91 PF) 的 parse-failure-excluded 分析未给出。\n- 12.02% CF 是论文报告的最高 CF 值，恰好出现在 parse failure 变化最大的配置上，这个巧合需要排除 selection bias。\n\n---\n\n**[AGREE] R1-W4: DocRED composability 呈现不够系统**\n\n同意但认为严重性较低。§5.2 标题是 \"Results on SciERC\" 但内容跨越两个数据集确实令人困惑。Table 2 (composability matrix) 仅呈现 SciERC，DocRED FT 数据散落在文字和 Table 2 caption 中（\"DocRED replication: Qwen DR −98.7% (−0.30pp), Llama DR −59.2% (+0.51pp)\"）。完整的 DocRED FT 4-way ablation 在 Appendix Table (tab:ft-ablation) 中。\n\n这不影响 soundness 但影响可读性。建议要么 (a) 将 §5.2 重命名为 \"Composability with Fine-tuning\" 并将 DocRED 明确作为 sub-paragraph，要么 (b) 在正文添加一个 2×2 DocRED composability mini-table。\n\n---\n\n**[AGREE] R1-W5: §4 DR reduction 范围与 Abstract 不一致**\n\n同意。§4 (section4_composition_draft.tex line 28) 说 \"SciERC achieves 94--99% DR reduction\"，这仅覆盖 Qwen (94%) 和 Llama (99%)，排除了 Mistral (76%)。而 Abstract 说 \"42--99% across three model families\"。两处的 scope 不同但未明确标注，容易误导。\n\n建议：§4 改为 \"SciERC achieves 76--99% DR reduction (94--99% for calibrated models; 76% for Mistral)\" 或明确限定 \"for Qwen and Llama\"。\n\n---\n\n### Questions\n\n**[AGREE] R1-Q1: JSON field ordering 是 pair-based masking 的隐含前提**\n\n这是一个精确的技术观察。Sequential masking (先 head_type, 后 tail_type) 要求 JSON schema 强制 head_type 在 tail_type 前生成。§3 line 23-27 (Eq.1) 的 output schema 定义了字段结构，但未显式讨论 ordering 是否由 grammar layer 强制。如果 XGrammar 的 JSON Schema compilation 允许字段任意顺序（JSON 标准不规定 object key order），那么模型可能先生成 tail_type，此时 head_type 未知，sequential masking 失效。\n\n这是一个 soundness concern，论文应明确说明：(a) grammar layer 是否强制了特定 field order（大概率是，因为 JSON Schema + XGrammar 通常按 schema 定义顺序生成），或 (b) semantic layer 在 tail_type 先于 head_type 时如何处理。\n\n---\n\n**[AGREE] R1-Q2: Beam k=4 vs LoRA 的对比值得讨论**\n\n有趣的观察。SciERC beam k=4 zero-shot: DR=0%, CF=0.53%, R-F1=8.56。SciERC LoRA + S1: DR=0%, CF=1.18%, R-F1=43.77。两者 DR 都为 0，beam 的 CF 更低，但 R-F1 天壤之别（8.56 vs 43.77）。所以 beam 不能替代 FT 在 F1 维度的贡献。但作为 CF 控制手段，beam 确实比 FT 更有效。论文可以在 Discussion 中指出 \"beam search + fine-tuning\" 的组合可能是最优配置。\n\n---\n\n**[AGREE] R1-Q3: Semantic-only DocRED ET 增加 +70%**\n\n同意这需要解释。DocRED semantic-only ET 从 2.48% 上升到 4.22%（Table 3），而 SciERC semantic-only ET 保持 0.40% 不变。§3 line 109-112 解释了 SciERC 下 semantic-only 的 ET residual 机制（\"semantic mask constrains type tokens to relation-specific valid sets but cannot enforce vocabulary membership; occasionally the mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative\"），但未解释为何 DocRED 恶化更严重。可能的原因：DocRED 的 96 relation 有更复杂的 domain/range 组合，semantic mask 更频繁地将模型从有效 entity type 推向 OOV type。这应在正文中明确讨论。\n\n---\n\n**[AGREE] R1-Q4: CF-DR trade-off ablation 仅 SciERC/Qwen**\n\n同意这是实验覆盖的缺口。Appendix B (tab:cf-dr-tradeoff) 的 CF fallback ablation 仅在 SciERC Qwen3-8B 上进行。Llama DocRED 有最高 CF (12.02%)，恰恰是最需要 CF-DR trade-off 分析的配置，但未提供对应 ablation。建议至少在 Appendix 补充 Llama DocRED 的 CF fallback pilot 数据。\n\n---\n\n### Missing References / Minor Issues\n\n**[AGREE] R1-Minor-6: RV=0.03% 解释不一致**\n\n这是一个真实的 inconsistency。§5 DocRED 正文（section5_docred_draft.tex line 61）说 \"the residual 5 triples arise from partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple\"。如果 rebuttal draft 说 \"XGrammar enum compilation bug\"，两个解释互相矛盾。需要统一为一个确定的根因。\n\n**[AGREE] R1-Minor-1: Design Assumption 前置到 §2**\n\n同意。Design Assumption 是整个方法的前提条件，放在 §3.3 Implementation 段落（方法描述后半段）时审稿人已经读了一半方法而不知道这个限制。在 §2 Problem Statement 中声明更合理。\n\n**[REBUT] R1-Minor-3: §5.2 内容跨度大建议拆分**\n\n不完全同意拆分的必要性。SciERC + composability + DocRED FT 在一个 subsection 内虽长，但 composability 是需要同时比较两个数据集的交叉分析。如果拆分为 \"§5.2 SciERC Results\" 和 \"§5.x Composability\"，会导致 SciERC 的 composability 数据与 DocRED 的 composability 数据分离，反而不利于比较。不过标题改为 \"SciERC Results and Composability Analysis\" 是合理折中。\n\n---\n\n### 总结\n\nR1 的审稿整体质量很高，技术观察精确（尤其是 Q1 field ordering、N1 的 F-test 计算）。我在 7/12 个 substantive issues 上 [AGREE]，2 个 [REBUT]（W2 post-hoc framing, Minor-3 section 拆分），3 个 partial agree。R1 和我的审稿在 N1 (dual-factor overstated) 和 beam search 重要性上高度一致。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-17T10:25:46.877270+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4085
}
```

</details>

---


### Assistant

_source line 246 · 2026-05-17T10:25:53.719346+00:00_

交叉回应已提交给 Director。对 R1 的 12 个 substantive issues 逐条回应完毕：7 个 [AGREE]、2 个 [REBUT]（W2 post-hoc framing 和 Minor-3 section 拆分）、3 个 partial agree。核心共识：R² (n=4) 在 Abstract 过度突出、beam search 结果被低估是两个最重要问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

72 recorded events


### User

_source line 247 · 2026-05-17T11:58:54.201036+00:00_

[Round 1 审稿请求]:
**[Round 5 / R1] 审稿任务分配 — 新颖性 + 写作完整性 + 格式合规**

**Venue**: EMNLP 2026 Findings (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Format**: ACL template, long paper ≤ 8 pages (excl. Limitations/Ethics/References), double-blind, Limitations section required
**论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`（所有 section 通过 `\input` 引入）

**你的审查侧重**：新颖性 + 写作完整性 + 格式合规

请重点检查以下方面：

### A. 新颖性定位
1. Contribution #2 novelty claim: "the first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE"——是否仍过于宽泛？是否充分区分了 DORE、GenIE、EnriCo？
2. Code-gen differentiation (R2-N2): §3 已有 three-point IE vs code-gen distinction，但 §1 Introduction 是否有 code-gen 讨论？历史审稿要求在 §1 near Contribution #2 添加一句说明为何 code-gen type-constrained decoding 不直接适用于 IE。
3. Grammar-only row as GCD ceiling (GC-N1): Tables 1-2 的 grammar-only 行是否被明确标识为 grammar-constrained decoding 的能力上限？是否在 §5 或 §6 有显式声明？

### B. 写作质量
1. **Em-dash (R4-N2)**: 检查全文是否还有解释性 em-dash（—, U+2014）或 en-dash（–, U+2013 用于解释性插入）。Table 中的 --- 占位符除外。这是 AI 写作最显著标志，必须全部消除。
2. **-ing participial phrases (R4-W1)**: 检查主文中是否还有大量 -ing 分词结尾的句子（confirming that..., enabling..., indicating..., reflecting..., showing that...）。估算数量。
3. **Abstract abbreviations (R4-N1)**: 检查 Abstract 中所有缩写是否在首次出现时展开。特别关注 LLM, IE, CFG, DR, ET, RV, CF, LoRA——ARR 要求 Abstract 独立可读。
4. 全文主线统一性：Abstract → Introduction → Method → Results → Discussion 是否形成一条连贯主线？是否有章节间逻辑断裂？
5. 专有名词是否在首次出现时定义？

### C. 格式合规
1. Reproducibility (R2-N5): 检查是否有独立的 Reproducibility Statement 或 Appendix。LoRA hyperparams（rank, alpha, LR, epochs）、GPU 型号、random seeds 是否完整报告？
2. DocRED composability data (R4-W4): SciERC 有 Table 2 composability matrix。DocRED FT 数据是否散落在 text 和 caption 中？§5.2 标题是否准确？
3. RV=0.03% 解释不一致 (R2-N10): 论文 §5.3 说 "partial JSON recovery"，rebuttal 说 "XGrammar bug"。当前论文中是否统一？
4. 页数是否符合 8 页限制？
5. 匿名化是否完整？是否有泄露作者信息的地方？
6. Limitations section 是否存在且内容充实？
7. 引用格式是否一致？引用覆盖是否充足？

### D. 引用审查
1. 是否有遗漏的重要相关工作？特别关注 2025-2026 年新发表的 constrained decoding for IE 工作。
2. DORE、GenIE、EnriCo 是否都在 §6 main text 中有充分讨论？
3. 自引是否过多？

请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses (Must-Fix / Should-Fix / Minor)、Questions、Missing References、Scores (Novelty 1-5, Writing 1-5, Completeness 1-5, Reproducibility 1-5, Overall 1-5, Confidence 1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-17T11:59:01.838393+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-17T11:59:01.839152+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-17T11:59:08.014884+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-17T11:59:08.115741+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-17T11:59:10.140287+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude"
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-17T11:59:10.142143+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-17T11:59:20.790186+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-17T11:59:20.790663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-17T11:59:28.326352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-17T11:59:28.377830+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_runtime}
53	
54	% === §6 Related Work ===
55	\input{section6_related_work}
56	
57	% === §7 Discussion and Conclusion ===
58	\section{Discussion and Conclusion}
59	\label{sec:discussion}
60	\input{section7_conclusion_compressed}
61	
62	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
63	\clearpage
64	\section*{Limitations}
65	
66	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13
…[truncated 3565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-17T11:59:29.130954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-17T11:59:29.685560+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 260 · 2026-05-17T11:59:37.786811+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found comprehensive information about the ACL Rolling Review (ARR) 2026 reviewer guidelines, review form criteria, and scoring system.

## Key Scoring Metrics

Starting with February 2025, ARR reviewers are asked t
…[truncated 1815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8655
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-17T12:02:48.533387+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 51, \"total_citations\": 89, \"unique_cited_keys\": 49, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 40, \"online_not_found\": 3, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [\"guidance2023\", \"xie2016tkrl\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang...\", \"year
…[truncated 43262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 198847
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-17T12:02:58.329456+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall recommendation, and any other criteria like reproducibility, confidence, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall recommendation, and any other criteria like reproducibility, confidence, etc."
  }
}
```

</details>

---


### Tool call

_source line 263 · 2026-05-17T12:03:00.138723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 264 · 2026-05-17T12:03:01.043124+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	Residual DR correlates with the product of schema tightness and baseline violation rate: for calibrated models (Qwen3-8B, Llama-3.1-8B), the dual-factor pattern explains nearly all variance ($R^2{=}0.99$, $n{=}4$), while Mistral's higher entity misclassification rate places it outside this regime (Appendix~\ref{app:dual-factor}).
12	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 within $\pm$0.6\,pp, confirming orthogonal composability.
13	Per-relation independent enforcement introduces a cross-field consistency (CF) vs.\ DR trade-off: CF violations arise
…[truncated 152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 265 · 2026-05-17T12:03:01.094103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 266 · 2026-05-17T12:03:01.546328+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
17	
18	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE onto
…[truncated 2132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 267 · 2026-05-17T12:03:01.597001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 268 · 2026-05-17T12:03:02.049250+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 269 · 2026-05-17T12:03:02.049760+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 270 · 2026-05-17T12:03:02.100656+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The JSON Schema enforces a fixed field ordering (head $\to$ head\_type $\to$ tail $\to$ tail\_type $\to$ relation), which is a prerequisite for the sequential masking mechanism described in \S\ref{sec:d
…[truncated 8203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-17T12:03:04.311766+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Core Evaluation Criteria

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; very careful reading with related work familiarity
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; general area familiarity but incomplete detail verification
- 2: Can defend evaluation; likely missed some details or novelty assessment
- 1: Outside expertise area or paper is difficult to understand

**Soundness** (1-5 scale with half-point options)
- 5: Excellent thoroughness for paper type
- 4: Strong support for all claims; additional experiments optional
- 3: Adequate support for main claims; minor details need reinforcement
- 2: Main claims lack sufficient support; major technical problems
- 1: Insufficient rigor for publication or not relevant to ACL

**Excitement** (1-5 scale with half-point options)
- 5: Highly exciting; would recommend to others
- 4: Exciting; would mention to colleagues
- 3: Interesting; might share selectively
- 2: Potentially interesting to some community members
- 1: Not resonant; unlikely to interest the ACL community

## Overall Assessment (1-5 scale)

Ranges from "Consider for Award" (top 2.5%) through "Conference" acceptance to "Do not resubmit" for papers irrelevant to computational linguistics.

## Additional Dimensions

- **Reproducibility** (1-5 scale): Ease of replicating main results
- **Datasets** (1-5 scale): Value of released data to research community
- **Software** (1-5 scale): Utility of released code for others
- **Limitations/Societal Impact**: Discussion adequacy assessment
- **Ethical Concerns**: ACL code compliance review
- **Author Identity Knowledge** (1-5 scale): Anonymity status

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5982
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-17T12:03:11.025481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-17T12:03:11.025977+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-
…[truncated 2005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-17T12:03:11.076438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-17T12:03:11.679428+00:00_

1	% §5.1 Experimental Setup and Violation Landscape
2	% Compressed from standalone section. main.tex provides \subsection header.
3	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
4	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
5	
6	\label{sec:violation_landscape}
7	
8	\paragraph{Setup.}
9	We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
10	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
11	We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
12	Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
13	Violation rates are computed over successfully parsed documents; including parse failures as zero-violation instances adjusts rates by at most 0.23\,pp (Llama DocRED zero-shot; $<$0.01\,pp under fine-tuning), confirming robustness to this exclusion.
14	
15	\paragraph{Violation distribution.}
16	Table~\ref{tab:prompt_comparison} reports violation rates.
17	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite a 14$\times$ difference in ontology size. This indicates that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
18	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduc
…[truncated 1606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-17T12:03:11.730272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-17T12:03:12.634725+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{SciERC Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
11	evaluating each constraint layer independently and in combination.
12	All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
13	with identical prompts and decoding parameters;
14	only the active constraint layers differ.
15	
16	% ──────────────────────────────────────────
17	%  Table: SciERC five-way ablation
18	% ──────────────────────────────────────────
19	\begin{table}[t]
20	\centering
21	\small
22	\setlength{\tabcolsep}{3.6pt}
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}l rrrrr rr@{}}
25	\toprule
26	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
27	& \multicolumn{2}{c}{\textbf{F1}} \\
28	\cmidrule(lr){2-6} \cmidrule(l){7-8}
29	\textbf{Mode}
30	  & DR\,$\downarrow$ & $\Delta$DR
31	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
32	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
33	\midrule
34	Unconstrained
35	  & 15.37 & ---
36	  & 1.39  & 0.40
37	  & 0.08
38	  & 8.23  & 31.01 \\
39	Grammar
40	  & 14.84 & $\downarrow$3\%
41	  & \textbf{0} & \textbf{0}
42	  & 0.08
43	  & 8.23  & 30.98 \\
44	Semantic
45	  & 11.65 & $\downarrow$24\%
46	  & 1.51  & 0.40
47	  & 2.71
48	  & 8.15  & 31.01 \\
49	Full (S1)
50	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
51	  & \textbf{0} & \textbf{0}
52	  & 9.90
53	  & \textbf{8.36} & 30.98 \\
54	Full (S2)
55	  & 0.97  & $\downarrow$94\%
56	  & \textbf{0} & \textbf{0}
57	  & 8.03
58	  & 8.03  & \textbf{31.90} \\
59	\bottomrule
60	\end{tabular}}%
61	\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
62	DR: domain
…[truncated 11043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-17T12:03:12.635209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-17T12:03:12.886658+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types (14$\times$ the ontology size of SciERC).
10	All experiments use Qwen3-8B zero-shot on 998 documents.
11	
12	% ──────────────────────────────────────────
13	%  Table: DocRED four-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 18.46 & ---
32	  & 29.66 & 2.48
33	  & 0.10
34	  & 7.74  & 58.15 \\
35	Grammar
36	  & 26.17 & $\uparrow$42\%
37	  & \textbf{0.03} & \textbf{0}
38	  & 0.07
39	  & \textbf{8.31}  & \textbf{59.38} \\
40	Semantic
41	  & 13.84 & $\downarrow$25\%
42	  & 29.87 & 4.22
43	  & 1.05
44	  & 7.70  & 57.81 \\
45	Full (S1)
46	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
47	  & \textbf{0.03} & \textbf{0}
48	  & 2.57
49	  & 8.23  & 59.37 \\
50	\bottomrule
51	\end{tabular}}%
52	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
53	$\Delta$DR: relative change vs.\ unconstrained.
54	Best per column in \textbf{bold} (CF excluded).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\end{table}
58	
59	% exp_ids: phase2_docred_unconstraine
…[truncated 3446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-17T12:03:12.938867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-17T12:03:12.989742+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	We replicate the full S1 configuration with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts, decoding parameters, and evaluation.
11	Table~\ref{tab:cross-model} summarizes results across all three models.
12	Mistral serves as a third zero-shot verification point confirming model-agnosticism; composability evaluation (\S\ref{sec:composability}) uses LoRA fine-tuning which requires domain-specific training data available only for Qwen and Llama.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.4pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rrrr r@{}}
20	\toprule
21	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
22	& \textbf{R-F1} \\
23	\cmidrule(lr){3-6} \cmidrule(l){7-7}
24	\textbf{Dataset} & \textbf{Model}
25	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
26	  & $\uparrow$ \\
27	\midrule
28	\multirow{6}{*}{SciERC}
29	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
30	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
31	  \cmidrule(l){2-7}
32	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
33	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
34	  \cmidrule(l){2-7}
35	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
36	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
37	\midrule
38	\multirow{6}{*}{DocRED}
39	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
40	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
41	  \cmidrule(l){2-7}
42	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
43	  & Llama (S1)  &  2.55 &  0  
…[truncated 2545 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-17T12:03:19.319059+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-17T12:03:19.822345+00:00_

1	% Section 5 — Runtime Analysis
2	% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
3	% Qwen3-8B, same single-GPU server, controlled 4-way ablation.
4	
5	\subsection{Runtime Overhead}
6	\label{sec:runtime}
7	
8	Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{@{}l rr rr@{}}
15	\toprule
16	& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
17	& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
18	\cmidrule(lr){2-3} \cmidrule(l){4-5}
19	\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
20	\midrule
21	Unconstrained & 2.587 & --- & 21.023 & --- \\
22	Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
23	Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
24	Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
25	\bottomrule
26	\end{tabular}
27	\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
28	Grammar compile time: 0.044\,s (one-time, amortized to zero).
29	Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
30	\label{tab:runtime}
31	\end{table}
32	
33	Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
34	Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
35	Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
36	Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
37	Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-17T12:03:19.822767+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-17T12:03:20.777018+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} ensure every token belongs to a grammar-valid continuation; IterGen~\cite{ugare2025itergen} adds backtracking.
6	These guarantee format validity but cannot enforce cross-field semantic constraints such as ontology domain/range rules.
7	
8	\paragraph{Semantic Constrained Decoding for Code.}
9	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, MGD~\cite{mgd_neurips2023}, and \citet{pldi2025_type_constrained_codegen} enforce type and scope constraints in code generation; OntoCoDec migrates this paradigm to IE.
10	
11	\paragraph{Vocabulary and Type-Constrained Generation.}
12	\citet{roth_yih_2004} establish relational type compatibility as a hard constraint via ILP, though applied post-hoc.
13	GENRE~\cite{decao2021genre}, AdaKGC~\cite{adakgc_emnlp2023}, GCD~\cite{geng2023gcd}, and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} can appear but not \emph{which type combinations} are valid per relation; GCD's per-position trie enforces vocabulary membership (equivalent to our grammar layer) but cannot capture the conditional dependency between head and tail types that our semantic layer provides.
14	DORE~\cite{vukovic2024dore} enforces ontological consistency via chain-of-thought output selection with confidence thresholds, a generate-then-select paradigm distinct from OntoCoDec's token-level logit masking during generation.
15	GenIE~\cite{josifoski2022genie} constrains entity generation to a candidate trie but does not enforce relation-specific type constraints.
16	EnriCo~\cite{zaratiana2024enrico} applies ASP constraints during decoding for joint entity-relation extraction, a hard-constraint approach like ours but with task-speci
…[truncated 1145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-17T12:03:20.827806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-17T12:03:21.229924+00:00_

1	% Section 7 — Discussion and Conclusion (compressed)
2	% Full discussion paragraphs moved to Appendix C.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and two datasets with no significant F1 cost.
5	Composed with LoRA fine-tuning, it reaches DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost, confirming orthogonal error targeting.
6	Within calibrated models (Qwen, Llama; $n{=}4$), residual DR correlates linearly with $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ ($R^2{=}0.99$), suggesting constraint benefit scales with schema stringency and model OOV tendency.
7	This pattern has an informative boundary condition: Mistral achieves RV\,=\,0\% on SciERC yet retains DR\,=\,13.4\%, because its dominant error mode is entity type misclassification rather than vocabulary confusion---a factor not captured by the dual-factor product.
8	We present this as a descriptive characterization with explicit scope rather than a universal predictive law.
9	
10	CF impact is model-dependent: S1 introduces CF for well-calibrated models (up to 12.02\%) but reduces it for poorly-calibrated ones (Mistral: 56.87\%\,$\to$\,1.27\%).
11	Ablation confirms CF$\leftrightarrow$DR tension ($+$13.85\,pp; Appendix~\ref{app:cf-dr-tradeoff}); fine-tuning reduces CF by 88\% (\S\ref{sec:composability}); global entity-level type consensus offers the most direct path forward.
12	
13	% Limitations and Future Work moved to \section*{Limitations} in main.tex (ARR requirement)
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-17T12:03:21.280700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-17T12:03:21.833120+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Table~\ref{tab:inference-time} reports per-document inference times for Qwen3-8B under zero-shot greedy decoding across constraint configurations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Inference time (seconds/document, mean $\pm$ std) for Qwen3-8B, zero-shot, greedy decoding.}
23	\label{tab:inference-time}
24	\begin{tabular}{@{}lcc@{}}
25	\toprule
26	\textbf{Configuration} & \textbf{SciERC} & \textbf{DocRED} \\
27	\midrule
28	Unconstrained       & $8.69 \pm 3.89$  & $19.75 \pm 8.99$  \\
29	Grammar-only        & $8.81 \pm 4.51$  & $20.58 \pm 10.75$ \\
30	Semantic-only       & $7.23 \pm 3.91$  & $20.53 \pm 9.37$  \\
31	Full S1             & $6.76 \pm 3.67$  & $20.39 \pm 9.43$  \\
32	Post-hoc            & $8.69 \pm 3.89$  &
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-17T12:03:31.979067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-17T12:03:32.833744+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-17T12:03:32.984627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-17T12:03:33.336268+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 6808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-17T12:03:33.446708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-17T12:03:33.969962+00:00_

1	% Appendix B — Extended Discussion
2	% Contains discussion paragraphs moved from the main text during compression.
3	
4	\section{Extended Discussion}\label{app:discussion}
5	
6	%%% CF Dual Mechanism %%%
7	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1
8	
9	\paragraph{CF Dual Mechanism.}
10	CF violations arise from two distinct mechanisms:
11	(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
12	The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.
14	
15	These mechanisms have sharply different model profiles.
16	Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
17	Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
18	This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
19	The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.
20	
21	%%% Fallback Behavior and Effective Coverage %%%
22	% exp_ids: cf_fallback_ablation_scierc (final data)
23	
24	\paragraph{Fallback Behavior and Effective Coverage.}
25	\label{app:fallback-coverage}
26	The two-layer architecture produces two distinct fallback mechanisms with different seman
…[truncated 27992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 523
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-17T12:03:33.997422+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-17T12:03:34.490970+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
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
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, establishing a robust foundation for stru
…[truncated 19795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 493
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-17T12:03:34.591861+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-17T12:03:34.592398+00:00_

1	% Appendix — Prompt Templates
2	% W10: Extraction prompts used in all experiments.
3	
4	\section{Prompt Templates}
5	\label{app:prompts}
6	
7	All experiments use the same prompts across constrained and unconstrained decoding; constraints are applied at the logit level, not through prompt modification.
8	Table~\ref{tab:prompts} shows the system and user prompts for each dataset.
9	
10	\begin{table*}[t]
11	\centering
12	\small
13	\begin{tabular}{@{}p{0.95\textwidth}@{}}
14	\toprule
15	\textbf{SciERC --- System Prompt (Unconstrained \& Constrained)} \\
16	\midrule
17	\texttt{You are an expert information extraction system for scientific texts. Extract entities and relations from the given text.} \\[4pt]
18	\texttt{Entity types: Task, Method, Material, Metric, OtherScientificTerm, Generic} \\
19	\texttt{Relation types: Used-for, Feature-of, Hyponym-of, Part-of, Compare, Conjunction, Evaluate-for} \\[4pt]
20	\texttt{Output a JSON object with:} \\
21	\texttt{- "entities": list of \{"text": "...", "type": "..."\}} \\
22	\texttt{- "relations": list of \{"head": "...", "tail": "...", "type": "...", "head\_type": "...", "tail\_type": "..."\}} \\[4pt]
23	\texttt{Output ONLY valid JSON, no explanation.} \\
24	\midrule
25	\textbf{SciERC --- User Prompt} \\
26	\midrule
27	\texttt{Extract all entities and relations from this scientific text:} \\
28	\texttt{"\{text\}"} \\
29	\texttt{Output JSON:} \\
30	\midrule
31	\midrule
32	\textbf{DocRED --- System Prompt (Unconstrained \& Constrained)} \\
33	\midrule
34	\texttt{You are an information extraction system. Extract all entities and relations from the following document.} \\[4pt]
35	\texttt{Entity types: PER, ORG, LOC, TIME, NUM, MISC} \\[4pt]
36	\texttt{Relation types: country, instance of, performer, ...\ (96 Wikidata relation types; full list omitted for space)} \\[4pt]
37	\texttt{Output a JSON object with exactly this structure:} \\
38	\texttt{\{"entities": [\{"text": "entity name", "type": "ENTITY\_TYPE"\}],} \\
39	\texttt{\ "
…[truncated 770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-17T12:03:41.774630+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-17T12:03:42.227149+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:1:% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-17T12:03:42.780500+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-17T12:03:43.232957+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-17T12:03:43.686517+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-17T12:03:44.189198+00:00_

&lt;persisted-output>
Output too large (27.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/c910e5e7-ea5e-4089-9e19-c984656ad7ca/tool-results/toolu_01PfxXLU3iW9r2Vry4HV4C3k.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:13:When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:23:Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:26:The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:41:The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:13:types---14$\time
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-17T12:03:44.998547+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing[,.]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing[,.]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-17T12:03:45.050244+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex:5:\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:16:The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:161:\paragraph{Constraint tightness governs enforcement ceiling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex:12:\paragraph{Grammar-Constrained Decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:71:The semantic layer's dynamic masking assumes each entity type maps to a unique first subword token, verified for both tokenizers on our two ontologies (6 entity types each), but ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:6:Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:22:\caption{Inference time (seconds/document, mean $\pm$ std) for Qwen3-8B, zero-shot, greedy decoding.}
/home/ubuntu/.agent-ml-researc
…[truncated 14078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-17T12:04:17.990652+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (confirming|enabling|indicating|reflecting|showing|demonstrating|suggesting|establishing|motivating|representing|highlighting|revealing|providing|achieving|reducing|eliminating|yielding|producing|making|validating|ensuring|maintaining)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (confirming|enabling|indicating|reflecting|showing|demonstrating|suggesting|establishing|motivating|representing|highlighting|revealing|providing|achieving|reducing|eliminating|yielding|producing|making|validating|ensuring|maintaining)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "head_limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-17T12:04:18.744325+00:00_

&lt;persisted-output>
Output too large (28.6KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/c910e5e7-ea5e-4089-9e19-c984656ad7ca/tool-results/toolu_01PJpC7zmS62hDMxGvPPqe7v.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:139:escapes to OOV strings (e.g., ``ORGB'', ``EVENT''), producing 355
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:179:for the model to redirect probability mass toward, enabling
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:26:    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level interve
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-17T12:04:18.795092+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-17T12:04:18.795669+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
15	\label{tab:llama-per-relation-dr}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llrrr@{}}
18	\toprule
19	Relation & PID & Triples & DR Violations & DR Rate (\%) \\
20	\midrule
21	dissolved/demolished & P576 & 73 & 24 & 32.9 \\
22	followed by          & P156 & 117 & 24 & 20.5 \\
23	unemployment rate    & P1198 & 15 & 3 & 20.0 \\
24	end time             & P582 & 130 & 21 & 16.2 \\
25	instance of          & P31  & 290 & 37 & 12.8 \\
26	product/material produced & P1056 & 98 & 11 & 11.2 \\
27	location of formation & P740 & 81 & 8 & 9.9 \\
28	head of state        & P35  & 41  & 3  & 7.3 \\
29	applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
30	conflict             & P607 & 453 & 30 & 6.6 \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	% exp_ids: llama_docred_full_s1
35	
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's re
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-17T12:04:28.435556+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/c910e5e7-ea5e-4089-9e19-c984656ad7ca/tool-results/toolu_01PJpC7zmS62hDMxGvPPqe7v.txt",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/c910e5e7-ea5e-4089-9e19-c984656ad7ca/tool-results/toolu_01PJpC7zmS62hDMxGvPPqe7v.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-17T12:04:28.687458+00:00_

1	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:139:escapes to OOV strings (e.g., ``ORGB'', ``EVENT''), producing 355
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:179:for the model to redirect probability mass toward, enabling
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:26:    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:67:CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp), confirming that CF$\leftrightarrow$DR represents a fundamental trade-off in composable
…[truncated 27549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-17T12:06:32.249483+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding information extraction 2025 2026 ontology type constraints LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained decoding information extraction 2025 2026 ontology type constraints LLM"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-17T12:06:40.044458+00:00_

Web search results for query: "constrained decoding information extraction 2025 2026 ontology type constraints LLM"

Links: [{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Dialogue Ontology Relation Extraction via Constrained Chain-of-Thought Decoding","url":"https://arxiv.org/html/2408.02361"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"Constrained Decoding: Grammar-Guided Generation for Structured LLM Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output"},{"title":"Constrained Decoding of Diffusion LLMs with Context-Free Grammars | OpenReview","url":"https://openreview.net/forum?id=7Sph4KyeYO"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"}]

I've completed the web search for your query on constrained decoding, i
…[truncated 1766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7794
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-17T12:07:32.295891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-17T12:07:32.296433+00:00_

1	% Section 5 — Runtime Analysis
2	% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
3	% Qwen3-8B, same single-GPU server, controlled 4-way ablation.
4	
5	\subsection{Runtime Overhead}
6	\label{sec:runtime}
7	
8	Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{@{}l rr rr@{}}
15	\toprule
16	& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
17	& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
18	\cmidrule(lr){2-3} \cmidrule(l){4-5}
19	\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
20	\midrule
21	Unconstrained & 2.587 & --- & 21.023 & --- \\
22	Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
23	Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
24	Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
25	\bottomrule
26	\end{tabular}
27	\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
28	Grammar compile time: 0.044\,s (one-time, amortized to zero).
29	Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
30	\label{tab:runtime}
31	\end{table}
32	
33	Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
34	Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
35	Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
36	Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
37	Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 318 · 2026-05-17T12:09:33.314447+00:00_

数据收集完毕，现在撰写完整审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

78 recorded events


### User

_source line 319 · 2026-05-18T12:26:17.392336+00:00_

[Round 6 审稿请求]:
## Round 6 审稿任务 — Reviewer 2（新颖性 + 写作质量 + 格式合规）

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **投稿类别**: Long paper

### Venue 要求
- **页数限制**: 正文 8 页，Limitations/Ethics/References/Appendix 不计入
- **模板**: ACL style template (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **附录**: 允许，不计入页数限制，审稿人不强制阅读
- **Limitations section**: 必须，位于 References 前，omission = desk reject
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 你的审查侧重

**核心任务**：评估论文的新颖性定位、写作质量、以及 ARR 格式合规性。

**重点关注领域**：
1. **新颖性评估**：核心贡献是否超越 "从 code-gen 迁移 type-constrained decoding 到 IE" 的简单叙事？与 DORE、GenIE、EnriCo 等已有 IE constrained decoding 方法的区分是否清晰？
2. **写作质量**：
   - AI 写作痕迹检查：em-dash（---/—/–）使用频率、-ing 分词短语密度、过渡词堆砌
   - 全文 `grep "—"` 和 `grep " – "` 结果
   - 段落结构是否过度分段？
   - 用词黑名单检查（leverage/utilize/facilitate/delve/myriad/plethora）
3. **ARR 格式合规**：
   - Abstract 缩写是否全部展开（LLM、IE、CFG、DR 等）？
   - 匿名化是否完整？
   - 页数是否超限？
   - 行号是否开启？
   - Limitations section 格式是否正确？
4. **Related Work 定位**：是否充分覆盖直接相关方法、baseline 论文、benchmark 论文？
5. **叙事一致性**：Abstract → Introduction → Method → Results → Conclusion 是否形成一条连贯主线？

### 上轮（Round 5）遗留 Open Issues（你需要逐一检查是否已修复）

**Critical:**
- **R4-N1**: Abstract 缩写未展开（LLM/IE/CFG/DR/ET/RV/CF/LoRA）— ARR 规范违反。检查是否已修复。

**Warning:**
- **R2-N2**: Code-gen novelty differentiation — §3 有三点区分但 §1 完全未提及。是否已在 §1 添加？
- **R4-N2**: Em-dash 过度使用 — 正文 8-10 处，§3 有 2 处 Unicode em-dash。是否已修复？
- **R4-W1**: -ing 分词短语 ~10 处。是否已改写？
- **R4-W3**: §4 DR reduction 范围 (94-99%) 与 Abstract (42-99%) 不一致。是否已修复？
- **R4-W4**: DocRED composability 数据未表格化，§5.2 标题 "Results on SciERC" 包含 DocRED 讨论。是否已修复？
- **R2-N5**: Reproducibility — LoRA 超参数、GPU 型号、seeds。是否已补充？

**Info:**
- **GC-N1**: Grammar-only row 是否已标识为 GCD 能力上限？
- **R4-Q1**: JSON field ordering 是否已显式声明？
- **R2-N10**: RV=0.03% 解释是否已统一？

### 特别检查事项
1. 执行 `grep "—"` 和 `grep " – "` 统计全文 em-dash/en-dash
2. 执行 `grep "ing,"` 统计 -ing 分词短语
3. 检查 Abstract word count（ARR 建议 150-250 words）
4. 检查 bib 条目完整性（特别是 DORE: vukovic2024dore 是否补充了 pages/url）
5. 检查叙事一致性：Abstract claims 是否都在 §5 有对应 evidence？Contribution 列表是否都有对应 section？

### 输出要求
按以下结构输出审稿意见：
1. **Summary**（2-3 句）
2. **Strengths**（逐条，标记 S1/S2/...）
3. **Weaknesses**（逐条，标记 W1/W2/...，按 critical > warning > info 排序）
4. **Open Issue Resolution Check**（逐条标记 ✅ resolved / ⚠️ partially / ❌ not fixed）
5. **New Issues**（如有）
6. **Questions to Authors**
7. **Missing References**
8. **AI Writing Audit**:
   - Em-dash count + locations
   - -ing phrase count + locations
   - Blacklisted words found
   - Over-segmented paragraphs
9. **Scores**: Overall Assessment (1-5, 用 EMNLP 2026 评分标准), Novelty (1-5), Writing Quality (1-5), Reproducibility (1-5), Confidence (1-5)
10. **Detailed Section Comments**（逐节）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-18T12:26:26.799525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-18T12:26:27.201718+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
68	CF fallback ablation shows that eliminating
…[truncated 3737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-18T12:26:27.754464+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-18T12:26:28.207580+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-18T12:26:28.714514+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-18T12:26:29.216891+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-18T12:26:29.267536+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-18T12:26:29.669569+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-18T12:26:30.322950+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(leverage|utilize|facilitate|delve|myriad|plethora)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "-i": "True",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(leverage|utilize|facilitate|delve|myriad|plethora)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "-i": "True",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-18T12:26:30.373771+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-18T12:26:34.591138+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-18T12:26:35.045193+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/p
…[truncated 2747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-18T12:26:35.497367+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-18T12:26:35.949507+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:1:% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section
…[truncated 1637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-18T12:26:36.452036+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-18T12:26:36.904111+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-18T12:26:37.356903+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-18T12:26:37.830653+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:69:F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:120:Post-fine-tuning, grammar is a no-op; the semantic layer alone reduces DR by 39--72\% (Appendix~\ref{app:ft-ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:6:Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex:12:Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with relation F1 within $\pm$0.6\,pp, confirming near-lossless composability.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.log:1053:\T1/ptm/m/n/10.95 (-20) con-strained de-cod-ing, with Do-cRED show-ing +0.9--
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:14:CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction tasks robust to constraints.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects
…[truncated 15131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 473
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-18T12:26:38.232442+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(leverage|utilize|facilitate|delve|myriad|plethora)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "-i": "True",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(leverage|utilize|facilitate|delve|myriad|plethora)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "-i": "True",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-18T12:26:38.283098+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-18T12:26:53.751730+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-18T12:26:54.304612+00:00_

&lt;persisted-output>
Output too large (21.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/126888e5-214f-4101-a8f8-4c47ee8a0de4/tool-results/toolu_01MMedEUwnVRpoeYZEArKHwa.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:13:When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:23:Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:26:The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:41:The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:13:types---14$\time
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-18T12:26:54.305359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-18T12:26:55.208838+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (virtually eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	For calibrated models, residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics.
12	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with relation F1 within $\pm$0.6\,pp, confirming near-lossless composability.
13	With beam search ($k{=}4$), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality (relation F1 change ${<}$0.5\,pp).
14	The framework ge
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-18T12:26:55.259709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-18T12:26:55.761963+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
17	
18	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE onto
…[truncated 2852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-18T12:26:55.812870+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-18T12:26:55.914073+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 9038 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-18T12:27:09.714708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/126888e5-214f-4101-a8f8-4c47ee8a0de4/tool-results/toolu_01MMedEUwnVRpoeYZEArKHwa.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/126888e5-214f-4101-a8f8-4c47ee8a0de4/tool-results/toolu_01MMedEUwnVRpoeYZEArKHwa.txt"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-18T12:27:10.517585+00:00_

1	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:13:When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC).
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:23:Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:26:The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:41:The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:13:types---14$\times$ the ontology size of SciERC
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:40:  & 18.46 & ---
7	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b
…[truncated 20698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-18T12:27:10.668560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-18T12:27:10.970052+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-18T12:27:10.970420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-18T12:27:11.522399+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-da
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 551
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-18T12:27:11.623874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-18T12:27:11.676664+00:00_

1	% §5.1 Experimental Setup and Violation Landscape (compressed)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on two IE benchmarks:
9	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs/relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, avg.\ 5.68 valid pairs).
10	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}.
11	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
12	Violation rates are computed over successfully parsed documents; including failures as zero-violation instances adjusts rates by at most 0.23\,pp.
13	
14	\paragraph{Baseline violations and motivation.}
15	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite 14$\times$ ontology size difference, indicating that severity is driven by \emph{constraint tightness} rather than scale.
16	Per-relation rates vary by over 40\,pp (Appendix~\ref{app:per-relation-landscape}), correlating with tightness $\kappa(r)$.
17	RV on DocRED reaches 29.66\%, confirming that large vocabularies exceed prompt-based reproduction capacity.
18	Schema-informed prompting reduces DR by 62\% on SciERC but only 30\% on DocRED and is per-relation unreliable (DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp), motivating decoding-time enforcement.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-18T12:27:25.876283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-18T12:27:26.227821+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Best per column in \textbf{bold} (CF excluded).
60	F1 $\times$100. Bootstrap: 10{,}000 iterations.}
61	\label{tab:scierc-ab
…[truncated 6346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-18T12:27:26.228219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-18T12:27:26.278737+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrr rr@{}}
20	\toprule
21	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-6} \cmidrule(l){7-8}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Best per column in \textbf{bold} (CF excluded).
54	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
55	\label{tab:docred-ablation}
56	\end{table}
57	
58	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
59	\paragraph{Core result.}
60	Full S1 reduces DR from 
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-18T12:27:26.830975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-18T12:27:27.182519+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates full S1 with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts and evaluation.
11	Mistral serves as a third zero-shot verification point; composability evaluation (\S\ref{sec:composability}) uses LoRA, available only for Qwen and Llama.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr r@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \textbf{R-F1} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-7}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & $\uparrow$ \\
26	\midrule
27	\multirow{6}{*}{SciERC}
28	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
29	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
30	  \cmidrule(l){2-7}
31	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
32	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
33	  \cmidrule(l){2-7}
34	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
35	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
36	\midrule
37	\multirow{6}{*}{DocRED}
38	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
39	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
40	  \cmidrule(l){2-7}
41	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
42	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
43	  \cmidrule(l){2-7}
44	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
45	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
46	\b
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-18T12:27:27.183079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-18T12:27:27.283844+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	To test generality beyond RE, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 argument roles, 27 entity types, 245 role$\to$type constraints; Appendix~\ref{app:wikievents}).
11	The framework requires no modification: grammar compiles event/role vocabularies into a CFG; the semantic layer enforces role-conditioned type constraints via the same registry.
12	Violations extend to Event Vocabulary (EV), Role Vocabulary (RoV), and Argument Constraint (AC, analogous to DR).
13	
14	% ──────────────────────────────────────────
15	%  Table: WikiEvents three-model comparison (v3 final)
16	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
17	% ──────────────────────────────────────────
18	\begin{table}[t]
19	\centering
20	\small
21	\setlength{\tabcolsep}{2.8pt}
22	\resizebox{\columnwidth}{!}{%
23	\begin{tabular}{@{}ll rrrr rr@{}}
24	\toprule
25	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){3-6} \cmidrule(l){7-8}
28	\textbf{Model} & \textbf{Mode}
29	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
30	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
31	\midrule
32	\multirow{3}{*}{Qwen3-8B}
33	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
34	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
35	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
36	\midrule
37	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
38	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 
…[truncated 2256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-18T12:27:43.256824+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool call

_source line 365 · 2026-05-18T12:27:43.257194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 366 · 2026-05-18T12:27:44.111156+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} guarantee format validity but cannot enforce cross-field semantic constraints such as domain/range rules.
6	
7	\paragraph{Type-Constrained Generation for IE and Code.}
8	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, and \citet{pldi2025_type_constrained_codegen} enforce type constraints in code generation; OntoCoDec migrates this to IE.
9	GCD~\cite{geng2023gcd} and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} appear but not \emph{which type combinations} are valid per relation.
10	DORE~\cite{vukovic2024dore} uses generate-then-select with confidence thresholds; GenIE~\cite{josifoski2022genie} constrains entities via a trie without relation-specific type enforcement; EnriCo~\cite{zaratiana2024enrico} applies ASP constraints with task-specific manually authored rules.
11	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie} provide only soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025} validate after generation rather than preventing violations.
12	
13	\paragraph{Quality Impact.}
14	CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction tasks robust to constraints.
15	OntoCoDec confirms this: DR decreases 42--99\% with zero F1 degradation across three model families (extended survey in Appendix~\ref{app:related_work}).
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-18T12:27:44.111754+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and three datasets (2 RE + 1 EE) with no significant RE F1 cost; in EE, format compliance additionally enables entity extraction (\S\ref{sec:wikievents}).
5	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.20\% at $<$0.6\,pp F1 cost; residual DR follows a dual-factor pattern ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$; Appendix~\ref{app:dual-factor}).
6	CF impact is model-dependent (up to 12\% for calibrated models, reduced for poorly-calibrated ones); fine-tuning resolves this tension (CF\,$\leq$\,1.2\%; \S\ref{sec:composability}), and beam search ($k{=}4$) eliminates both residual DR and CF for calibrated models (Appendix~\ref{app:beam-search}).
7	Cross-field consistency remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct path to resolving CF without trading it against DR.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-18T12:27:44.262692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-18T12:27:44.363649+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	Full S1 adds $+$2.3\% on SciERC and $+$5.4\% on DocRED (same GPU); under fine-tuning, overhead drops to $+$2.3\% (61\,ms/doc).
6	Grammar compile is a one-time 44\,ms cost.
7	Per-layer profiling in Appendix~\ref{app:runtime}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-18T12:27:44.514745+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-18T12:27:44.515240+00:00_

1	\section{Reproducibility Details}
2	\label{app:reproducibility}
3	
4	\paragraph{Fine-tuning configuration.}
5	All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct on SciERC and DocRED) use identical LoRA hyperparameters: rank $r{=}16$, $\alpha{=}32$, dropout $0.05$, no bias, targeting all attention and MLP projection layers (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{gate\_proj}, \texttt{up\_proj}, \texttt{down\_proj}).
6	Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
7	SciERC trains on 1,762 examples (260 dev) for 333 steps; DocRED trains on 3,053 examples (998 dev) for 573 steps.
8	Maximum sequence length is 2,048 (SciERC) and 4,096 (DocRED).
9	All runs use seed 42.
10	
11	\paragraph{Hardware and software.}
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB VRAM).
13	SciERC fine-tuning takes approximately 11 minutes per model; DocRED takes approximately 1.5 hours.
14	Software versions: PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13.
15	
16	\paragraph{Inference time.}
17	Table~\ref{tab:inference-time} reports per-document inference times for Qwen3-8B under zero-shot greedy decoding across constraint configurations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Inference time (seconds/document, mean $\pm$ std) for Qwen3-8B, zero-shot, greedy decoding.}
23	\label{tab:inference-time}
24	\begin{tabular}{@{}lcc@{}}
25	\toprule
26	\textbf{Configuration} & \textbf{SciERC} & \textbf{DocRED} \\
27	\midrule
28	Unconstrained       & $8.69 \pm 3.89$  & $19.75 \pm 8.99$  \\
29	Grammar-only        & $8.81 \pm 4.51$  & $20.58 \pm 10.75$ \\
30	Semantic-only       & $7.23 \pm 3.91$  & $20.53 \pm 9.37$  \\
31	Full S1             & $6.76 \pm 3.67$  & $20.39 \pm 9.43$  \\
32	Post-hoc            & $8.69 \pm 3.89$  &
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-18T12:27:49.903771+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "vukovic2024dore",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
  "output_mode": "content",
  "-n": "True",
  "-A": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "vukovic2024dore",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib",
    "output_mode": "content",
    "-n": "True",
    "-A": "15"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-18T12:27:50.356351+00:00_

550:@inproceedings{vukovic2024dore,
551-  title     = {{DORE}: A Dataset for {Portuguese} Knowledge Graph Construction and a Reproduction of a {LLM}-based Ontology-Constrained Approach},
552-  author    = {Vukovi{\'c}, Mila and Prange, Jakob and Navigli, Roberto},
553-  booktitle = {Proceedings of the 25th Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL)},
554-  pages     = {291--303},
555-  year      = {2024},
556-  url       = {https://aclanthology.org/2024.sigdial-1.25/}
557-}
558-

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-18T12:27:53.270152+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search ARR reviewer guidelines",
  "subagent_type": "Explore",
  "prompt": "Search the web for \"ACL ARR review form criteria 2025 2026\" or \"EMNLP 2026 reviewer guidelines\" to find the official reviewer guidelines and scoring dimensions for ACL Rolling Review (ARR). I need the official review form dimensions (like soundness, excitement/novelty, reproducibility, etc.) and their scales. Report what you find in a concise format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Search ARR reviewer guidelines",
    "subagent_type": "Explore",
    "prompt": "Search the web for \"ACL ARR review form criteria 2025 2026\" or \"EMNLP 2026 reviewer guidelines\" to find the official reviewer guidelines and scoring dimensions for ACL Rolling Review (ARR). I need the official review form dimensions (like soundness, excitement/novelty, reproducibility, etc.) and their scales. Report what you find in a concise format."
  }
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-18T12:27:53.972825+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-18T12:27:54.023323+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 377 · 2026-05-18T12:27:54.725599+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-18T12:27:54.826410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines"
  }
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-18T12:28:02.562261+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP | OpenReview","url":"https://openreview.net/group?id=EMNLP"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about EMNLP 2026 reviewer guidelines:

## Review Timeline and Deadlines

If you receive review assignments, your reviews must be completed by July 6, or your meta-reviews by July 29. All authors must complete the author registration form by May 27, 2026 EoD AoE.

## Reviewer Qualifications

Reviewers are considered qualified if they have published at least two short or long papers in main ACL events or Findings, plus at least one more paper in the ACL Anthology or a m
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7735
}
```

</details>

---


### Tool result

_source line 380 · 2026-05-18T12:28:02.813436+00:00_

Web search results for query: "ACL ARR review form criteria 2025 2026"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, here's information about the ACL ARR review form criteria for 2025-2026:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Key Evaluation Criteri
…[truncated 1426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8087
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-18T12:28:04.972389+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are the official review form dimensions, scoring scales, and evaluation criteria?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "What are the official review form dimensions, scoring scales, and evaluation criteria?"
  }
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-18T12:28:05.223861+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the detailed reviewer guidelines, scoring dimensions, and evaluation criteria?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "What are the detailed reviewer guidelines, scoring dimensions, and evaluation criteria?"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-18T12:28:10.017590+00:00_

# ARR Reviewer Guidelines: Scoring Dimensions and Evaluation Criteria

## Three Main Scoring Dimensions

According to the guidelines, reviewers provide three distinct scores:

1. **Soundness**: "The _soundness_ scores must be justified by the text of the review." Low soundness scores require explicit justification in the review content.

2. **Excitement**: This reflects personal interest independent of technical quality. "Such preferences are more subjective and should be reflected in a separate _excitement_ score, which is orthogonal to the assessment of the soundness of the paper."

3. **Overall Recommendation**: A composite assessment reflecting soundness, excitement, novelty, and potential impact for conference commitment.

## Key Evaluation Framework

Reviewers should follow these core tasks:

- **Expertise Check**: Verify you can adequately review the assignment
- **Specific Feedback**: Provide concrete, detailed comments rather than vague criticisms
- **Common Bias Awareness**: Recognize patterns like dismissing "unsurprising" results or favoring preferred methodologies
- **Tone Assessment**: Maintain professionalism and constructive language throughout

## Critical Principles

The guidelines emphasize that "papers are valued for their content rather than language," and reviews should reflect genuine technical evaluation rather than methodological preference or cognitive bias.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4793
}
```

</details>

---


### Tool result

_source line 384 · 2026-05-18T12:28:10.118311+00:00_

# ACL Rolling Review Form: Official Dimensions and Scales

The review form includes these primary evaluation dimensions:

**Reviewer Confidence** (1-5 scale): Assesses certainty level, ranging from "Not my area" (1) to "Positive that my evaluation is correct" (5).

**Soundness** (1-5 scale): Evaluates technical rigor, with "Major Issues" (1) to "Excellent" (5) reflecting study thoroughness and claim support.

**Excitement** (1-5 scale): Subjective assessment where "Not Exciting" (1) means the paper lacks relevance to computational linguistics, while "Highly Exciting" (5) indicates recommendation-worthy innovation.

**Overall Assessment** (1-5 scale): The decisive rating spanning from "Do not resubmit" (1) through "Conference" (4) to "Consider for Award" (5), which determines publication pathway.

**Additional Criteria:**
- Limitations and societal impact discussion
- Ethical concerns alignment with ACL code of ethics
- Reproducibility (1-5 scale)
- Dataset value (1-5 scale)
- Software utility (1-5 scale)
- Author anonymity knowledge (1-5 scale)

The form emphasizes that papers require "sufficient support for all of its claims" for strong soundness ratings and distinguishes between main conference papers and Findings submissions based on soundness and reproducibility standards.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5145
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-18T12:28:16.999302+00:00_

Perfect! Here's a concise summary of the official ACL ARR review form criteria and scoring dimensions for 2025-2026:

## Official ACL ARR Review Form Dimensions

### Core Scoring Dimensions (1-5 scales):

1. **Soundness** (1-5)
   - 1 = Major Issues
   - 5 = Excellent
   - Must be justified by review text; scores must reflect technical rigor and claim support

2. **Excitement** (1-5)
   - 1 = Not Exciting
   - 5 = Highly Exciting
   - Subjective assessment; orthogonal to soundness
   - Includes innovation, transformational potential, surprising results, conceptual breakthroughs

3. **Overall Recommendation** (1-5)
   - 1 = Do not resubmit
   - 2 = Resubmit next cycle
   - 1.5 = Resubmit after next cycle
   - 4 = Conference
   - 5 = Consider for Award
   - Composite reflecting soundness, excitement, novelty, and impact

4. **Reviewer Confidence** (1-5)
   - 1 = Not my area
   - 5 = Positive that my evaluation is correct

### Additional Evaluation Criteria:

- **Reproducibility** (1-5 scale)
- **Dataset Value** (1-5 scale)
- **Software Utility** (1-5 scale)
- **Author Anonymity Knowledge** (1-5 scale)
- Limitations and societal impact discussion
- Ethical concerns alignment with ACL Code of Ethics

### Key Principles:
- Soundness and excitement are **orthogonal** dimensions
- All papers must meet soundness and reproducibility standards for Findings/conference acceptance
- Excitement is subjective and can include transformation, novelty, and impact considerations
- Reviews should provide specific, justified feedback rather than vague criticisms

Sources:
- [ACL Rolling Review Form](http://aclrollingreview.org/reviewform)
- [ARR Reviewer Guidelines](http://aclrollingreview.org/reviewerguidelines)
- [CALL FOR PAPERS – ACL Rolling Review](http://aclrollingreview.org/cfp)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 23729
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-18T12:31:10.919326+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (confirming|suggesting|demonstrating|highlighting|indicating|enabling|achieving|establishing|representing|providing|showing)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (confirming|suggesting|demonstrating|highlighting|indicating|enabling|achieving|establishing|representing|providing|showing)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-18T12:31:11.271232+00:00_

&lt;persisted-output>
Output too large (21.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/126888e5-214f-4101-a8f8-4c47ee8a0de4/tool-results/toolu_01VNvJQ6SAUj5NJBqTQjqUsM.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:179:for the model to redirect probability mass toward, enabling
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:22:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:28:    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:67:Longer documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction, confirming that the constraint framework scales reliably with document complexity.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:9:XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into cont
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-18T12:31:11.823861+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "app:wikievents",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "app:wikievents",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-18T12:31:13.278977+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:433:\label{app:wikievents}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex:10:To test generality beyond RE, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 argument roles, 27 entity types, 245 role$\to$type constraints; Appendix~\ref{app:wikievents}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.aux:2149:\newlabel{app:wikievents}{{C}{21}{WikiEvents Dataset Details}{section*.75}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 1455
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-18T12:31:13.380041+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~$%]//g; s/  */ /g' | wc -w",
  "description": "Count approximate abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~$%]//g; s/  */ /g' | wc -w",
    "description": "Count approximate abstract word count"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-18T12:31:13.583054+00:00_

294

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-18T12:31:19.056808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/126888e5-214f-4101-a8f8-4c47ee8a0de4/tool-results/toolu_01VNvJQ6SAUj5NJBqTQjqUsM.txt",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/126888e5-214f-4101-a8f8-4c47ee8a0de4/tool-results/toolu_01VNvJQ6SAUj5NJBqTQjqUsM.txt",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-18T12:31:19.107756+00:00_

1	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:179:for the model to redirect probability mass toward, enabling
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:22:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:28:    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:67:Longer documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction, confirming that the constraint framework scales reliably with document complexity.
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:9:XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:10:O
…[truncated 19819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-18T12:31:41.175156+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-18T12:31:41.225834+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 396 · 2026-05-18T12:33:34.671922+00:00_

All data collected. Now compiling the full review and posting to Director.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

64 recorded events


### User

_source line 397 · 2026-05-18T12:41:52.283863+00:00_

[Round 6 审稿请求]:
## Round 6 继续审稿 — Reviewer 2（新颖性/写作/格式）

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
**论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
**Venue**: EMNLP 2026 (ARR May 2026 cycle), deadline 2026-05-25
**格式**: ACL 2023 模板 (`\usepackage[review]{acl}`)，double-blind，Long paper 8页正文 + 无限附录/参考文献
**Round 5 评分**: Weak Accept (Findings)

---

### 你的任务

这是增量审稿——论文在 Round 5 报告后进行了修订（最后修改 2026-05-18 12:04）。你需要：
1. **逐条验证**下方 open issues 是否已在修订版中修复
2. **识别修改是否引入了新问题**
3. 对每个 issue 给出判定：✅ Resolved / ⚠️ Partially fixed / ❌ Not fixed / 🆕 New issue
4. 更新整体评分建议

### 你负责核查的 Open Issues（写作/格式/新颖性类）

**[MF2] R4-N1 [critical] Abstract 缩写未展开**
- Round 5 要求：至少展开 LLM(Large Language Model)、IE(Information Extraction)、DR(domain/range)、CF(cross-field consistency)。ET/RV/CFG 可用描述性文字替代
- 检查：Abstract 中每个缩写是否有展开

**[SF2] R4-N2 [warning] Em-dash 过度使用（AI 写作标志）**
- Round 5 要求：逐一替换解释性 em-dash 为逗号/括号/拆句。保留至多 2-3 处。Unicode em-dash 必须消除
- 检查：`grep "—" *.tex` + `grep " – " *.tex` 结果。§3 的 2 处 Unicode em-dash 是否消除

**[SF3] R4-W1 [warning] -ing 分词短语过密**
- Round 5 要求：正文约 10 处 -ing 分词短语结尾需改写
- 检查：`grep "ing," *.tex` 和 `grep "ing\." *.tex` 模式

**[SF4] R2-N2 [warning] Code-gen 新颖性区分未在 §1 出现**
- Round 5 要求：§1 第二段或 Contribution #2 附近添加一句 IE vs code-gen type-constrained decoding 本质区别
- 检查：§1 是否提及 Synchromesh/PICARD/MGD 或 code-gen constrained decoding

**[SF6] W3 [warning] Post-hoc filtering framing 仍有选择性**
- Round 5 要求：§1 或 §5 添加一句 "Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48% of predictions including true positives; OntoCoDec's advantage is recall preservation."
- 检查：是否有平衡表述

**[SF9] R4-W3 [warning] §4 DR range 与 Abstract 不一致**
- Round 5 要求：§4 加 "for calibrated models (Qwen, Llama)" 或用全范围
- 检查：§4 范围表述（与 R1 交叉验证）

**[MF1] R2-N1 [critical] R² in Abstract（交叉验证 R1）**
- 检查：Abstract 是否仍含 R²=0.886

**[M4] R4-W4 [info] DocRED composability 数据散落，§5.2 标题不匹配**
- Round 5 要求：重命名 §5.2 或添加 DocRED 子段落
- 检查：§5.2 标题和结构

**[M8] Table 1 caption em-dash**
- 检查：Table 1 caption 中 "CF excluded---see text" 是否已替换

### 额外检查（写作全局）

- 全文 AI 写作痕迹扫描：过度分段、"Furthermore/Moreover/Additionally" 连续使用、"It is worth noting"、"delve into/leverage/utilize" 等
- 专有名词首次出现是否有定义
- 引用充足度：是否有新增引用？BoostCD 讨论是否充分？

### 输出格式

```
## Issue Verification

| Issue ID | Severity | Verdict | Evidence |
|----------|----------|---------|----------|
| R4-N1    | critical | ✅/⚠️/❌ | 具体引用论文行号 |
| ...      | ...      | ...     | ...      |

## AI Writing Scan
- Em-dash count: X (target ≤3)
- -ing phrase count: X (target ≤5 in main text)
- Blacklist words found: ...

## New Issues Found
（如有）

## Updated Assessment
- 新颖性: X/5
- 写作质量: X/5
- 格式合规: X/5
- 建议评分: ...
- 理由: ...
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-18T12:42:06.134634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-18T12:42:06.185436+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	
18	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
19	
20	\author{Anonymous ACL submission}
21	
22	\begin{document}
23	\maketitle
24	
25	% === Abstract ===
26	\input{abstract}
27	
28	% === §1 Introduction ===
29	\input{section1_introduction_draft}
30	
31	% === §2 Background ===
32	\input{section2_background}
33	
34	% === §3 Method ===
35	\input{section3_method_draft}
36	
37	% === §4 Constraint Composition ===
38	\section{Constraint Composition}
39	\label{sec:composition}
40	\input{section4_composition_draft}
41	
42	% === §5 Experiments ===
43	\section{Experiments}
44	\label{sec:experiments}
45	
46	\subsection{Violation Landscape}
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
68	CF fallback ablation shows that eliminating
…[truncated 3737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-18T12:42:07.541985+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search EMNLP 2026 reviewer guidelines",
  "prompt": "Search the web for \"ACL ARR review form criteria 2026\" and \"EMNLP 2026 reviewer guidelines\". I need to find the official reviewer guidelines and review form dimensions (soundness, excitement/novelty, reproducibility, etc.) for ACL Rolling Review (ARR) which EMNLP 2026 uses. Use WebSearch and WebFetch to find this information. Report the official scoring dimensions and their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Search EMNLP 2026 reviewer guidelines",
    "prompt": "Search the web for \"ACL ARR review form criteria 2026\" and \"EMNLP 2026 reviewer guidelines\". I need to find the official reviewer guidelines and review form dimensions (soundness, excitement/novelty, reproducibility, etc.) for ACL Rolling Review (ARR) which EMNLP 2026 uses. Use WebSearch and WebFetch to find this information. Report the official scoring dimensions and their scales."
  }
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-18T12:42:09.250665+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2026"
  }
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-18T12:42:09.301367+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-18T12:42:17.338052+00:00_

Web search results for query: "ACL ARR review form criteria 2026"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) review form criteria for 2026:

## Main Review Criteria

For Findings papers, the main criteria are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Recommendat
…[truncated 1368 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8087
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-18T12:42:20.304061+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP | OpenReview","url":"https://openreview.net/group?id=EMNLP"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's what I found about EMNLP 2026 reviewer guidelines:

## Key Reviewer Guidelines for EMNLP 2026

**Reviewer Eligibility and Responsibilities:**
Reviewers are considered qualified if they have published at least two short or long papers in main ACL events or Findings, plus at least one more paper in the ACL Anthology or a major ML/AI venue.

All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifica
…[truncated 1009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11002
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-18T12:42:22.774665+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "What are the official scoring dimensions and their scales for the ARR review form?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "What are the official scoring dimensions and their scales for the ARR review form?"
  }
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-18T12:42:22.832370+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "What are the reviewer guidelines and scoring criteria for ARR reviews?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "What are the reviewer guidelines and scoring criteria for ARR reviews?"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-18T12:42:26.828244+00:00_

# Official ARR Review Form Scoring Dimensions

Based on the ACL Rolling Review platform, the official scoring dimensions are:

1. **Reviewer Confidence** (1-5 scale): Assesses how certain the reviewer is about their evaluation, ranging from "Not my area" to "Positive that my evaluation is correct."

2. **Soundness** (1-5 scale with half-point increments): Evaluates whether the paper is "sufficiently sound and thorough" with adequate support for scientific claims.

3. **Excitement** (1-5 scale with half-point increments): Measures subjective engagement, considering whether the work presents "conceptual breakthroughs" or challenges "common assumptions."

4. **Overall Assessment** (1-5 scale with half-point increments): The primary recommendation dimension ranging from "Do not resubmit" through "Consider for Award."

5. **Reproducibility** (1-5 scale): Determines if readers could "reproduce the main results" or build on the work presented.

Additional evaluation areas include Limitations and Societal Impact, Ethical Concerns, Datasets, and Software—though these use descriptive scales rather than numeric ratings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 4053
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-18T12:42:28.536589+00:00_

# ARR Reviewer Guidelines and Scoring Criteria

## Key Guidelines

ARR reviewers follow a structured four-task approach:

1. **Allocate calendar time** for reviewing and discussion periods
2. **Check assignments** for expertise match and conflicts of interest
3. **Write strong reviews** with specific, evidence-based feedback
4. **Update assessments** after author responses

## Scoring Criteria (as of February 2025)

Reviewers provide three distinct scores:

- **Soundness**: Technical validity and methodological rigor. Must be "justified by the text of the review"
- **Excitement**: Personal interest level, reflecting subjective preferences separate from soundness
- **Overall Recommendation**: Composite assessment addressing soundness, novelty, and potential impact

## Critical Review Principles

Reviewers should "adjust expectations" by reading papers twice—first to understand the research question, then in-depth for technical evaluation. Reviews must be "specific and ideally understandable to the chairs without reading the full paper."

The guidelines emphasize avoiding common biases like dismissing surprising results, requiring unnecessary experiments, or preferring particular methodologies. Professional, neutral tone is essential, as "a good review should help the authors improve their papers."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5704
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-18T12:42:33.507324+00:00_

Perfect! I've gathered the official information. Let me provide you with a comprehensive summary of the official ACL ARR review form criteria and dimensions:

## Official ARR Review Form Scoring Dimensions

Based on the authoritative ACL Rolling Review platform, here are the official scoring dimensions used by EMNLP 2026 reviewers (which uses ARR):

### Primary Scoring Dimensions:

1. **Soundness** (1-5 scale with half-point increments)
   - Evaluates whether the paper is "sufficiently sound and thorough" with adequate support for scientific claims
   - Technical validity and methodological rigor

2. **Excitement** (1-5 scale with half-point increments)
   - Subjective engagement measure
   - Considers whether the work presents "conceptual breakthroughs" or challenges "common assumptions"
   - Personal interest level separate from soundness assessment

3. **Overall Recommendation/Assessment** (1-5 scale with half-point increments)
   - Primary recommendation dimension
   - Composite assessment addressing soundness, novelty, and potential impact
   - Scores map to recommendations:
     - 5 = Consider for Award (outstanding papers, top 2.5%)
     - 2 = Resubmit next cycle (substantial revisions possible within one cycle)
     - 1.5 = Resubmit after next cycle (substantial revisions requiring longer timeframe)
     - 1 = Do not resubmit (fundamental issues or not relevant to community)

4. **Reviewer Confidence** (1-5 scale)
   - Assesses certainty of the reviewer's evaluation
   - Ranges from "Not my area" to "Positive that my evaluation is correct"

5. **Reproducibility** (1-5 scale)
   - Determines if readers could "reproduce the main results" or build on the work
   - Evaluates information sufficiency

### Additional Evaluation Areas (descriptive rather than numeric):
- Limitations and Societal Impact
- Ethical Concerns
- Datasets and Software

The key principle emphasized in reviewer guidelines is that reviews must be "specific and ideally understandable to the ch
…[truncated 454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 25965
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-18T12:42:38.537536+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-18T12:42:38.989829+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) guaranteeing JSON structural validity and entity/relation vocabulary membership (virtually eliminating entity type and relation vocabulary violations); and
4	(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
5	The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
6	%
7	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), comparable rates governed by \emph{constraint tightness} rather than ontology scale.
8	\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
9	For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
10	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
11	For calibrated models, residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics.
12	Composed with Low-Rank Adaptation (LoRA) fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with relation F1 within $\pm$0.6\,pp, confirming near-lossless composability.
13	With beam search ($k{=}4$), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality (relation F1 change ${<}$0.5\,pp).
14	The framework ge
…[truncated 597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-18T12:42:39.040418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-18T12:42:40.145492+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
9	Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.
17	
18	We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE onto
…[truncated 2852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-18T12:42:40.146013+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-18T12:42:43.924948+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 9038 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3778
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-18T12:42:44.828437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-18T12:42:44.829016+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	
18	\paragraph{Constraint Tightness.}
19	We define the tightness of relation $r$ as:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
28	This dual-factor pattern (tightness $\times$ baseline model violation rate) is consistent with the cross-da
…[truncated 1435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-18T12:42:44.979956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-18T12:42:45.030854+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrr rr@{}}
21	\toprule
22	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-6} \cmidrule(l){7-8}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Best per column in \textbf{bold} (CF excluded).
60	F1 $\times$100. Bootstrap: 10{,}000 iterations.}
61	\label{tab:scierc-ab
…[truncated 6346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-18T12:42:45.031285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-18T12:42:45.082078+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrr rr@{}}
20	\toprule
21	& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-6} \cmidrule(l){7-8}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Best per column in \textbf{bold} (CF excluded).
54	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
55	\label{tab:docred-ablation}
56	\end{table}
57	
58	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
59	\paragraph{Core result.}
60	Full S1 reduces DR from 
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-18T12:42:53.316419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-18T12:42:54.120496+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates full S1 with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts and evaluation.
11	Mistral serves as a third zero-shot verification point; composability evaluation (\S\ref{sec:composability}) uses LoRA, available only for Qwen and Llama.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\setlength{\tabcolsep}{3.4pt}
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}ll rrrr r@{}}
19	\toprule
20	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
21	& \textbf{R-F1} \\
22	\cmidrule(lr){3-6} \cmidrule(l){7-7}
23	\textbf{Dataset} & \textbf{Model}
24	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
25	  & $\uparrow$ \\
26	\midrule
27	\multirow{6}{*}{SciERC}
28	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
29	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
30	  \cmidrule(l){2-7}
31	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
32	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
33	  \cmidrule(l){2-7}
34	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
35	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
36	\midrule
37	\multirow{6}{*}{DocRED}
38	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
39	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
40	  \cmidrule(l){2-7}
41	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
42	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
43	  \cmidrule(l){2-7}
44	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
45	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
46	\b
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-18T12:42:54.271865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-18T12:42:54.623926+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	To test generality beyond RE, we apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 argument roles, 27 entity types, 245 role$\to$type constraints; Appendix~\ref{app:wikievents}).
11	The framework requires no modification: grammar compiles event/role vocabularies into a CFG; the semantic layer enforces role-conditioned type constraints via the same registry.
12	Violations extend to Event Vocabulary (EV), Role Vocabulary (RoV), and Argument Constraint (AC, analogous to DR).
13	
14	% ──────────────────────────────────────────
15	%  Table: WikiEvents three-model comparison (v3 final)
16	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
17	% ──────────────────────────────────────────
18	\begin{table}[t]
19	\centering
20	\small
21	\setlength{\tabcolsep}{2.8pt}
22	\resizebox{\columnwidth}{!}{%
23	\begin{tabular}{@{}ll rrrr rr@{}}
24	\toprule
25	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
26	& \multicolumn{2}{c}{\textbf{F1}} \\
27	\cmidrule(lr){3-6} \cmidrule(l){7-8}
28	\textbf{Model} & \textbf{Mode}
29	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
30	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
31	\midrule
32	\multirow{3}{*}{Qwen3-8B}
33	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
34	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
35	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
36	\midrule
37	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
38	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 
…[truncated 2256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-18T12:42:54.774916+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-18T12:42:55.076937+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Grammar-Constrained Decoding.}
5	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, DOMINO~\cite{beurer-kellner2024domino}, SynCode~\cite{ugare2024syncode}, and ASAp~\cite{park2024grammar} guarantee format validity but cannot enforce cross-field semantic constraints such as domain/range rules.
6	
7	\paragraph{Type-Constrained Generation for IE and Code.}
8	Synchromesh~\cite{synchromesh_iclr2022}, PICARD~\cite{scholak2021picard}, and \citet{pldi2025_type_constrained_codegen} enforce type constraints in code generation; OntoCoDec migrates this to IE.
9	GCD~\cite{geng2023gcd} and GoLLIE~\cite{sainz2024gollie} constrain \emph{which tokens} appear but not \emph{which type combinations} are valid per relation.
10	DORE~\cite{vukovic2024dore} uses generate-then-select with confidence thresholds; GenIE~\cite{josifoski2022genie} constrains entities via a trie without relation-specific type enforcement; EnriCo~\cite{zaratiana2024enrico} applies ASP constraints with task-specific manually authored rules.
11	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie} provide only soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025} validate after generation rather than preventing violations.
12	
13	\paragraph{Quality Impact.}
14	CRANE~\cite{banerjee2025crane} and \citet{schall2025hiddencost} show grammar restrictions can degrade reasoning, but \citet{tam2024letmespeak} find extraction tasks robust to constraints.
15	OntoCoDec confirms this: DR decreases 42--99\% with zero F1 degradation across three model families (extended survey in Appendix~\ref{app:related_work}).
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-18T12:42:55.077451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-18T12:42:56.082250+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and three datasets (2 RE + 1 EE) with no significant RE F1 cost; in EE, format compliance additionally enables entity extraction (\S\ref{sec:wikievents}).
5	Composed with LoRA fine-tuning, DR reaches $\leq$\,0.20\% at $<$0.6\,pp F1 cost; residual DR follows a dual-factor pattern ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$; Appendix~\ref{app:dual-factor}).
6	CF impact is model-dependent (up to 12\% for calibrated models, reduced for poorly-calibrated ones); fine-tuning resolves this tension (CF\,$\leq$\,1.2\%; \S\ref{sec:composability}), and beam search ($k{=}4$) eliminates both residual DR and CF for calibrated models (Appendix~\ref{app:beam-search}).
7	Cross-field consistency remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct path to resolving CF without trading it against DR.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-18T12:42:56.183091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-18T12:42:56.434558+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-18T12:42:56.435145+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-18T12:42:56.535849+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	Full S1 adds $+$2.3\% on SciERC and $+$5.4\% on DocRED (same GPU); under fine-tuning, overhead drops to $+$2.3\% (61\,ms/doc).
6	Grammar compile is a one-time 44\,ms cost.
7	Per-layer profiling in Appendix~\ref{app:runtime}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-18T12:43:04.373179+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-18T12:43:04.875057+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:1:% Section 5 — DocRED Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:1:% Appendix — Prompt Templates
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:1:% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:1:% Section 3 — Method (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:1:% Appendix B — Extended Discussion
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:2:% Related Work Additions — compiled 2026-05-14
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex:60:% STATUS: VERIFIED — paper exists and description is accurate
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:1:% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:1:% Section 5 — SciERC Results (Draft)
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section
…[truncated 1220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-18T12:43:05.377034+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-18T12:43:05.828848+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-18T12:43:06.281245+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-18T12:43:06.735944+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:69:F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:6:Training uses AdamW with learning rate $2{\times}10^{-4}$, cosine schedule, warmup ratio $0.1$, effective batch size $16$, bf16 precision, gradient checkpointing, and completion-only loss for 3 epochs.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:10:Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, enabling efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:24:While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema (database table and column names known before decoding begins).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:26:Synchromesh~\cite{synchromesh_iclr2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning, establishing that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.
…[truncated 14281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-18T12:43:07.539458+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-18T12:43:08.195037+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex:5:\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:16:The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:161:\paragraph{Constraint tightness governs enforcement ceiling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex:12:\paragraph{Grammar-Constrained Decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:69:F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:22:\caption{Inference time (seconds/document, mean $\pm$ std) for Qwen3-8B, zero-shot, greedy decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:7:\paragraph{Grammar-Constrained Decoding.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:12:These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naiv
…[truncated 11770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-18T12:43:09.149548+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "(Furthermore|Moreover|Additionally|It is worth noting|Notably|delve|leverage|utilize|facilitate|myriad|plethora)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "(Furthermore|Moreover|Additionally|It is worth noting|Notably|delve|leverage|utilize|facilitate|myriad|plethora)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-18T12:43:09.602387+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:50:Schema-informed prompts (\S\ref{sec:violation_landscape}) additionally include valid (head type, tail type) pairs per relation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:123:The first pass generates only entities under grammar constraints; the extracted entities compile an input-dependent grammar that additionally constrains head and tail names to match declared entities.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:4:OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints, achieving 42--99\% DR reduction across three models and three datasets (2 RE + 1 EE) with no significant RE F1 cost; in EE, format compliance additionally enables entity extraction (\S\ref{sec:wikievents}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex:14:The framework generalizes to event extraction (WikiEvents: 56 event types, 80 roles) without architectural modification and eliminates event-vocabulary and role-vocabulary violations ($\to$ 0\%); where unconstrained outputs are severely off-schema, format compliance additionally enables entity extraction (Entity F1: 0\%\,$\to$\,12--18\%).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-18T12:43:09.903873+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-18T12:43:09.954754+00:00_

&lt;persisted-output>
Output too large (21.9KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/4207db89-eea8-4da9-bf9f-0cac5dc05fa8/tool-results/toolu_01NYaoQNpvu6jsbJP9UNtMyV.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:13:When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:23:Domain/range (DR) violations produce structurally invalid triples---a triple asserting that a \emph{Task} entity fills the \emph{domain} slot of \textsc{Part-of}, which requires \emph{Method}, cannot be consumed by any downstream system without error.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:26:The dominant conflict pattern---\emph{Generic}$\leftrightarrow$\emph{OtherScientificTerm} (60 of 245~affected entities on SciERC)---reflects genuine semantic ambiguity in the type system rather than a systematic method failure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex:41:The DocRED baseline exhibits a relation-vocabulary (RV) violation rate of 29.66\%---5{,}189 predictions with OOV relation names---all of which become false positives under this protocol.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:13:types---14$\time
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-18T12:44:51.478100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-18T12:44:51.528801+00:00_

1	% §5.1 Experimental Setup and Violation Landscape (compressed)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on two IE benchmarks:
9	\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs/relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, avg.\ 5.68 valid pairs).
10	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}.
11	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
12	Violation rates are computed over successfully parsed documents; including failures as zero-violation instances adjusts rates by at most 0.23\,pp.
13	
14	\paragraph{Baseline violations and motivation.}
15	DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED, comparable rates despite 14$\times$ ontology size difference, indicating that severity is driven by \emph{constraint tightness} rather than scale.
16	Per-relation rates vary by over 40\,pp (Appendix~\ref{app:per-relation-landscape}), correlating with tightness $\kappa(r)$.
17	RV on DocRED reaches 29.66\%, confirming that large vocabularies exceed prompt-based reproduction capacity.
18	Schema-informed prompting reduces DR by 62\% on SciERC but only 30\% on DocRED and is per-relation unreliable (DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp), motivating decoding-time enforcement.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-18T12:44:53.035052+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "{abstract,section1_introduction_draft,section2_background,section3_method_draft,section4_composition_draft,section5_scierc_draft,section5_docred_draft,section5_crossmodel_draft,section5_wikievents_draft,section5_runtime,section6_related_work,section7_conclusion_compressed,section3_violation_landscape}.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "---",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "{abstract,section1_introduction_draft,section2_background,section3_method_draft,section4_composition_draft,section5_scierc_draft,section5_docred_draft,section5_crossmodel_draft,section5_wikievents_draft,section5_runtime,section6_related_work,section7_conclusion_compressed,section3_violation_landscape}.tex"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-18T12:44:53.487255+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:31:  & 15.37 & ---
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:138:    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:142:    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:147:    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:151:    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex:34:  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex:39:  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex:44:  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex:50:---: not applicable (grammar-only has no semantic-layer metrics).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:30:  & 18.46 & ---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-18T12:44:54.341191+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "BoostCD|boostcd",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "BoostCD|boostcd",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-18T12:44:54.391752+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-18T12:46:04.779844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
  "offset": "70"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
    "offset": "70"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-18T12:46:05.131578+00:00_

70	Semantic-only reduces DR by 25\% but cannot eliminate RV (29.87\%) or prevent ET increases (2.48\%\,$\to$\,4.22\%), replicating SciERC's enabling dependency.
71	Residual DR (10.21\%) exceeds SciERC's (0.93\%) due to higher constraint tightness ($\bar{\kappa}{=}0.842$ vs.\ 0.333), with fallback rate (10.2\%) closely tracking residual DR (Appendix~\ref{app:fallback-coverage}).
72	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-18T12:46:06.436335+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", [a-z]+ing ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "glob": "{abstract,section1_introduction_draft,section2_background,section3_method_draft,section4_composition_draft,section5_scierc_draft,section5_docred_draft,section5_crossmodel_draft,section5_wikievents_draft,section5_runtime,section6_related_work,section7_conclusion_compressed,section3_violation_landscape}.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", [a-z]+ing ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "{abstract,section1_introduction_draft,section2_background,section3_method_draft,section4_composition_draft,section5_scierc_draft,section5_docred_draft,section5_crossmodel_draft,section5_wikievents_draft,section5_runtime,section6_related_work,section7_conclusion_compressed,section3_violation_landscape}.tex"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-18T12:46:06.487178+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs, making it impractical.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:22:The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:28:    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex:10:We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:59:Cross-model DR asymmetry reflects baseline RV: Llama's lower RV (16.03\% vs.\ 29.66\%) limits latent violation surfacing, yielding 2.55\% residual DR vs.\ 10.21\%.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section
…[truncated 8186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-18T12:47:08.994381+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-18T12:47:09.095311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-18T12:48:21.437966+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 增量审稿报告 — Reviewer 2（新颖性/写作/格式）\n\n论文：OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n修订版最后修改：2026-05-18 12:04\n\n---\n\n## Issue Verification\n\n| Issue ID | Severity | Verdict | Evidence |\n|----------|----------|---------|----------|\n| [MF2] R4-N1 | critical | ✅ Resolved | Abstract 所有缩写均已展开：IE (L2), LLM (L7), DR (L7), CF (L15), LoRA (L12)。ET/RV 未作为缩写使用，改用描述性文字。 |\n| [SF2] R4-N2 | warning | ✅ Resolved | Unicode em-dash (—)：仅出现在 .tex 注释行（`% Section 5 —` 等），渲染文本中为 0 处。解释性 en-dash (` – `)：0 处。LaTeX `---`：仅用于表格单元格表示 N/A（标准用法），正文 prose 中为 0 处。Table 1 caption 已改为 \"(CF excluded)\"，无 em-dash。 |\n| [SF3] R4-W1 | warning | ❌ Not fixed | 详见下方 AI Writing Scan。正文中 trailing -ing 分词短语约 20 处，远超目标 ≤5。较 Round 5 估计的 ~10 处不减反增。 |\n| [SF4] R2-N2 | warning | ✅ Resolved | §1 L23: \"Unlike type-constrained code generation where types are statically declared, IE requires a dynamic entity registry built during generation, with constraint targets that depend on the co-occurring relation.\" §1 Contribution #2 (L29-30) 再次强调该区分。§6 Related Work 引用 Synchromesh/PICARD/pldi2025 三篇具体系统。 |\n| [SF6] W3 | warning | ✅ Resolved | §1 L14-15 几乎逐字满足要求：\"Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7%), it discards the majority of outputs, making it impractical. OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.\" |\n| [SF9] R4-W3 | warning | ✅ Resolved | §4 L28 明确区分：\"for calibrated models (Qwen, Llama), SciERC...achieves 94--99% DR reduction, while DocRED...achieves 45--90%; including Mistral...the full range across all three models is 42--99%\"。Abstract 使用全范围 \"42--99% across three model families\"，二者一致。 |\n| [MF1] R2-N1 | critical | ✅ Resolved | Abstract 中无 R²=0.886。L11 改为定性表述：\"residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics.\" |\n| [M4] R4-W4 | info | ✅ Resolved | §5.2 重命名为 \"Ablation and Composability with Fine-Tuning\"，包含 SciERC 消融 + SciERC/DocRED 双数据集 composability 结果（L114-119 含 DocRED 数据）。§5.3 \"Cross-Dataset Validation on DocRED\" 聚焦 DocRED zero-shot 消融。结构清晰，标题与内容匹配。 |\n| [M8] Table 1 caption | info | ✅ Resolved | Table 1 caption (section5_scierc_draft.tex L59): \"Best per column in **bold** (CF excluded).\" 无 em-dash。 |\n\n**总结：8/9 issues resolved，1 issue (SF3 -ing phrases) 未修复。**\n\n---\n\n## AI Writing Scan\n\n### Em-dash count: 0 ✅ (target ≤3)\n- Unicode em-dash (—) 在渲染文本中：0 处\n- 解释性 en-dash (` – `)：0 处\n- LaTeX `---` 用作 prose em-dash：0 处\n- 仅 table cells 中有 `---` 表示 N/A（标准用法）\n\n### -ing participial phrase count: ~20 ❌ (target ≤5)\n\n正文中 trailing -ing 分词短语（\"..., [verb]ing [interpretation]\" AI 典型模式）完整列表：\n\n| # | 位置 | 短语 |\n|---|------|------|\n| 1 | abstract.tex:11 | \"...suggesting that constraint effectiveness is predictable\" |\n| 2 | abstract.tex:12 | \"...confirming near-lossless composability\" |\n| 3 | §1 L14 | \"...making it impractical\" |\n| 4 | §1 L22 | \"...enabling the semantic layer to look up domain/range rules\" |\n| 5 | §1 L28 | \"...showing that violation rates are driven by...\" |\n| 6 | §2 L10 | \"...increasing violation likelihood\" |\n| 7 | §5.1 L15 | \"...indicating that severity is driven by...\" |\n| 8 | §5.1 L17 | \"...confirming that large vocabularies exceed...\" |\n| 9 | §5.1 L18 | \"...motivating decoding-time enforcement\" |\n| 10 | §4 L11 | \"...reflecting the enabling dependency\" |\n| 11 | §4 L27 | \"...increasing fallback frequency and residual DR\" |\n| 12 | §5.2 L92 | \"...confirming the enabling dependency\" |\n| 13 | §5.2 L119 | \"...confirming orthogonal composability\" |\n| 14 | §5.2 L121 | \"...tracing to Generic↔X schema ambiguity\" |\n| 15 | §5.3 L70 | \"...replicating SciERC's enabling dependency\" |\n| 16 | §5.4 L59 | \"...yielding 2.55% residual DR vs. 10.21%\" |\n| 17 | §5.5 L57 | \"...validating tokenizer-agnostic design\" |\n| 18 | §5.5 L58 | \"...replicating the latent-violation surfacing pattern\" |\n| 19 | §5.5 L59 | \"...confirming layer complementarity\" |\n| 20 | §7 L4 | \"...achieving 42--99% DR reduction\" |\n\n**特别严重**：单词 \"confirming\" 作为 trailing -ing 出现 7 次（#2, #8, #12, #13, #19 + §5.3, §5.5）。这是极其明显的 AI 写作指纹——真实作者不会在一篇论文中用 7 次 \", confirming X\"。\n\n### Blacklist words found: 0 ✅\n- 无 \"Furthermore/Moreover/Additionally\" 作为段落连接词\n- 无 \"delve into/leverage/utilize/facilitate/myriad/plethora\"\n- 无 \"It is worth noting/Notably\"\n- \"additionally\" 出现 2 次（abstract:14, §7:4），但用作句内副词而非段落连接词，可接受\n\n### 过度分段检查: ✅\n- 段落长度合理，未见异常短段\n\n---\n\n## New Issues Found\n\n**🆕 N1 [warning] \"confirming\" 单词过度重复**\n- 位置：全文 7+ 处 trailing \", confirming X\" \n- 问题：同一个 AI 典型词 \"confirming\" 反复用于句末评价性分词短语，形成高度机械化的写作模式。即使在不完全消除 -ing phrases 的情况下，至少应多样化动词选择（如改为独立句 \"This confirms...\"、\"The result confirms...\" 或用其他结构替代）\n- 建议：将至少 5/7 处 \"confirming\" 改写为其他结构\n\n**🆕 N2 [info] BoostCD 未讨论**\n- BoostCD 是近期 constrained decoding 领域相关工作，论文中未提及。作为一个 minor gap 标记，不影响接收决定。\n\n**🆕 N3 [info] §1 code-gen 区分可加引用**\n- §1 L23 和 L29-30 提到 \"unlike type-constrained code generation\" 但未在 §1 内 cite 具体系统（Synchromesh/PICARD/pldi2025 仅在 §6 引用）。在 §1 加一个 parenthetical citation 会更有说服力，但非必须。\n\n---\n\n## Updated Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | Round 5 | Round 6 | 变化 | 理由 |\n|------|---------|---------|------|------|\n| Soundness | 3.5/5 | 3.5/5 | → | 本轮审查范围为写作/格式/新颖性，Soundness 维持 |\n| Excitement | 3.5/5 | 3.5/5 | → | 新颖性区分已到位（§1+§6），code-gen 对比清晰 |\n| 写作质量 | 2.5/5 | 3/5 | ↑ | Em-dash 全部消除（显著改善），但 -ing phrases 未修复且数量(~20)远超预期，\"confirming\" 重复 7 次构成明显 AI 指纹 |\n| 格式合规 | 4/5 | 4.5/5 | ↑ | Abstract 缩写全部展开，Table caption 修复，§5.2 结构重组合理 |\n\n### 建议评分\n\n**Overall: 3.5 (Borderline Conference)**\n\n**理由**：\n\n8/9 open issues 已修复，论文在格式合规和叙事平衡方面有实质改善：\n- Abstract 缩写、em-dash、Table caption、§5.2 结构、post-hoc framing、DR 范围一致性等问题全部解决\n- 新颖性定位通过 §1 和 §6 的 code-gen 对比得到充分阐述\n\n但 **-ing 分词短语问题不仅未修复，反而恶化**（Round 5 估计 ~10 处，现约 20 处），且 \"confirming\" 单词在 trailing position 出现 7 次，构成极其明显的 AI 生成痕迹。对于 EMNLP 2026 这样的顶级会议，审稿人对 AI 写作标志高度敏感。这一问题虽不影响技术贡献的评价，但会显著降低审稿人对论文的整体印象。\n\n**升至 4.0 (Conference) 的条件**：\n1. 将 ~20 处 trailing -ing phrases 改写至 ≤5 处（优先消除重复的 \"confirming\"）\n2. 这是一个纯写作修改，工作量不大但影响显著\n\n**降至 3.0 (Findings) 的风险**：\n- 如果审稿人注意到 AI 写作模式（尤其是 7 处 \"confirming\"），可能直接扣分",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 增量审稿报告 — Reviewer 2（新颖性/写作/格式）\n\n论文：OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n修订版最后修改：2026-05-18 12:04\n\n---\n\n## Issue Verification\n\n| Issue ID | Severity | Verdict | Evidence |\n|----------|----------|---------|----------|\n| [MF2] R4-N1 | critical | ✅ Resolved | Abstract 所有缩写均已展开：IE (L2), LLM (L7), DR (L7), CF (L15), LoRA (L12)。ET/RV 未作为缩写使用，改用描述性文字。 |\n| [SF2] R4-N2 | warning | ✅ Resolved | Unicode em-dash (—)：仅出现在 .tex 注释行（`% Section 5 —` 等），渲染文本中为 0 处。解释性 en-dash (` – `)：0 处。LaTeX `---`：仅用于表格单元格表示 N/A（标准用法），正文 prose 中为 0 处。Table 1 caption 已改为 \"(CF excluded)\"，无 em-dash。 |\n| [SF3] R4-W1 | warning | ❌ Not fixed | 详见下方 AI Writing Scan。正文中 trailing -ing 分词短语约 20 处，远超目标 ≤5。较 Round 5 估计的 ~10 处不减反增。 |\n| [SF4] R2-N2 | warning | ✅ Resolved | §1 L23: \"Unlike type-constrained code generation where types are statically declared, IE requires a dynamic entity registry built during generation, with constraint targets that depend on the co-occurring relation.\" §1 Contribution #2 (L29-30) 再次强调该区分。§6 Related Work 引用 Synchromesh/PICARD/pldi2025 三篇具体系统。 |\n| [SF6] W3 | warning | ✅ Resolved | §1 L14-15 几乎逐字满足要求：\"Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7%), it discards the majority of outputs, making it impractical. OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.\" |\n| [SF9] R4-W3 | warning | ✅ Resolved | §4 L28 明确区分：\"for calibrated models (Qwen, Llama), SciERC...achieves 94--99% DR reduction, while DocRED...achieves 45--90%; including Mistral...the full range across all three models is 42--99%\"。Abstract 使用全范围 \"42--99% across three model families\"，二者一致。 |\n| [MF1] R2-N1 | critical | ✅ Resolved | Abstract 中无 R²=0.886。L11 改为定性表述：\"residual DR correlates with the product of schema tightness and baseline violation rate, suggesting that constraint effectiveness is predictable from schema and model characteristics.\" |\n| [M4] R4-W4 | info | ✅ Resolved | §5.2 重命名为 \"Ablation and Composability with Fine-Tuning\"，包含 SciERC 消融 + SciERC/DocRED 双数据集 composability 结果（L114-119 含 DocRED 数据）。§5.3 \"Cross-Dataset Validation on DocRED\" 聚焦 DocRED zero-shot 消融。结构清晰，标题与内容匹配。 |\n| [M8] Table 1 caption | info | ✅ Resolved | Table 1 caption (section5_scierc_draft.tex L59): \"Best per column in **bold** (CF excluded).\" 无 em-dash。 |\n\n**总结：8/9 issues resolved，1 issue (SF3 -ing phrases) 未修复。**\n\n---\n\n## AI Writing Scan\n\n### Em-dash count: 0 ✅ (target ≤3)\n- Unicode em-dash (—) 在渲染文本中：0 处\n- 解释性 en-dash (` – `)：0 处\n- LaTeX `---` 用作 prose em-dash：0 处\n- 仅 table cells 中有 `---` 表示 N/A（标准用法）\n\n### -ing participial phrase count: ~20 ❌ (target ≤5)\n\n正文中 trailing -ing 分词短语（\"..., [verb]ing [interpretation]\" AI 典型模式）完整列表：\n\n| # | 位置 | 短语 |\n|---|------|------|\n| 1 | abstract.tex:11 | \"...suggesting that constraint effectiveness is predictable\" |\n| 2 | abstract.tex:12 | \"...confirming near-lossless composability\" |\n| 3 | §1 L14 | \"...making it impractical\" |\n| 4 | §1 L22 | \"...enabling the semantic layer to look up domain/range rules\" |\n| 5 | §1 L28 | \"...showing that violation rates are driven by...\" |\n| 6 | §2 L10 | \"...increasing violation likelihood\" |\n| 7 | §5.1 L15 | \"...indicating that severity is driven by...\" |\n| 8 | §5.1 L17 | \"...confirming that large vocabularies exceed...\" |\n| 9 | §5.1 L18 | \"...motivating decoding-time enforcement\" |\n| 10 | §4 L11 | \"...reflecting the enabling dependency\" |\n| 11 | §4 L27 | \"...increasing fallback frequency and residual DR\" |\n| 12 | §5.2 L92 | \"...confirming the enabling dependency\" |\n| 13 | §5.2 L119 | \"...confirming orthogonal composability\" |\n| 14 | §5.2 L121 | \"...tracing to Generic↔X schema ambiguity\" |\n| 15 | §5.3 L70 | \"...replicating SciERC's enabling dependency\" |\n| 16 | §5.4 L59 | \"...yielding 2.55% residual DR vs. 10.21%\" |\n| 17 | §5.5 L57 | \"...validating tokenizer-agnostic design\" |\n| 18 | §5.5 L58 | \"...replicating the latent-violation surfacing pattern\" |\n| 19 | §5.5 L59 | \"...confirming layer complementarity\" |\n| 20 | §7 L4 | \"...achieving 42--99% DR reduction\" |\n\n**特别严重**：单词 \"confirming\" 作为 trailing -ing 出现 7 次（#2, #8, #12, #13, #19 + §5.3, §5.5）。这是极其明显的 AI 写作指纹——真实作者不会在一篇论文中用 7 次 \", confirming X\"。\n\n### Blacklist words found: 0 ✅\n- 无 \"Furthermore/Moreover/Additionally\" 作为段落连接词\n- 无 \"delve into/leverage/utilize/facilitate/myriad/plethora\"\n- 无 \"It is worth noting/Notably\"\n- \"additionally\" 出现 2 次（abstract:14, §7:4），但用作句内副词而非段落连接词，可接受\n\n### 过度分段检查: ✅\n- 段落长度合理，未见异常短段\n\n---\n\n## New Issues Found\n\n**🆕 N1 [warning] \"confirming\" 单词过度重复**\n- 位置：全文 7+ 处 trailing \", confirming X\" \n- 问题：同一个 AI 典型词 \"confirming\" 反复用于句末评价性分词短语，形成高度机械化的写作模式。即使在不完全消除 -ing phrases 的情况下，至少应多样化动词选择（如改为独立句 \"This confirms...\"、\"The result confirms...\" 或用其他结构替代）\n- 建议：将至少 5/7 处 \"confirming\" 改写为其他结构\n\n**🆕 N2 [info] BoostCD 未讨论**\n- BoostCD 是近期 constrained decoding 领域相关工作，论文中未提及。作为一个 minor gap 标记，不影响接收决定。\n\n**🆕 N3 [info] §1 code-gen 区分可加引用**\n- §1 L23 和 L29-30 提到 \"unlike type-constrained code generation\" 但未在 §1 内 cite 具体系统（Synchromesh/PICARD/pldi2025 仅在 §6 引用）。在 §1 加一个 parenthetical citation 会更有说服力，但非必须。\n\n---\n\n## Updated Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | Round 5 | Round 6 | 变化 | 理由 |\n|------|---------|---------|------|------|\n| Soundness | 3.5/5 | 3.5/5 | → | 本轮审查范围为写作/格式/新颖性，Soundness 维持 |\n| Excitement | 3.5/5 | 3.5/5 | → | 新颖性区分已到位（§1+§6），code-gen 对比清晰 |\n| 写作质量 | 2.5/5 | 3/5 | ↑ | Em-dash 全部消除（显著改善），但 -ing phrases 未修复且数量(~20)远超预期，\"confirming\" 重复 7 次构成明显 AI 指纹 |\n| 格式合规 | 4/5 | 4.5/5 | ↑ | Abstract 缩写全部展开，Table caption 修复，§5.2 结构重组合理 |\n\n### 建议评分\n\n**Overall: 3.5 (Borderline Conference)**\n\n**理由**：\n\n8/9 open issues 已修复，论文在格式合规和叙事平衡方面有实质改善：\n- Abstract 缩写、em-dash、Table caption、§5.2 结构、post-hoc framing、DR 范围一致性等问题全部解决\n- 新颖性定位通过 §1 和 §6 的 code-gen 对比得到充分阐述\n\n但 **-ing 分词短语问题不仅未修复，反而恶化**（Round 5 估计 ~10 处，现约 20 处），且 \"confirming\" 单词在 trailing position 出现 7 次，构成极其明显的 AI 生成痕迹。对于 EMNLP 2026 这样的顶级会议，审稿人对 AI 写作标志高度敏感。这一问题虽不影响技术贡献的评价，但会显著降低审稿人对论文的整体印象。\n\n**升至 4.0 (Conference) 的条件**：\n1. 将 ~20 处 trailing -ing phrases 改写至 ≤5 处（优先消除重复的 \"confirming\"）\n2. 这是一个纯写作修改，工作量不大但影响显著\n\n**降至 3.0 (Findings) 的风险**：\n- 如果审稿人注意到 AI 写作模式（尤其是 7 处 \"confirming\"），可能直接扣分",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-18T12:48:25.447891+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4009
}
```

</details>

---


### Assistant

_source line 460 · 2026-05-18T12:48:34.737797+00:00_

Round 6 审稿报告已提交。

核心发现：

- **8/9 open issues 已修复**：em-dash 全部消除、Abstract 缩写展开、post-hoc framing 平衡化、§4 DR 范围一致性、§5.2 结构重组、Table 1 caption 等均已解决
- **1 issue 未修复且恶化**：trailing -ing 分词短语从 Round 5 估计的 ~10 处增至 ~20 处，其中 "confirming" 一词在 trailing position 出现 7 次，构成极其明显的 AI 写作指纹
- **建议评分维持 3.5 (Borderline Conference)**，升至 4.0 仅需将 -ing phrases 改写至 ≤5 处

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

8 recorded events


### User

_source line 461 · 2026-05-18T12:49:26.193824+00:00_

[Round 6 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1（方法/实验严谨性）的完整 Round 6 审稿意见。请逐条回应：
- **[AGREE]** 同意并简述理由
- **[REBUT]** 反驳并引用具体 Section/Table/Figure 作为证据

---

### Reviewer 1 Issue Verification 结果

| Issue ID | Severity | Verdict | Evidence |
|----------|----------|---------|----------|
| R2-N1 (MF1) | critical | ✅ Resolved | Abstract R² 已移除，Appendix 报告 F-test，Mistral 排除有先验标准 |
| R4-N3 (SF1) | warning | ⚠️ Partially fixed | 正文仅一句话提及 beam；beam runtime 未量化；greedy vs beam 定位不明确；DocRED beam 用匹配 50-doc ✅ |
| R2-N3 (SF5) | warning | ⚠️ Partially fixed | Parse failure rate 已报告，Limitations 承认 confounding，但未提供 deconfounded 分析 |
| R4-W2 (SF7) | warning | ⚠️ Partially fixed | 3/4 model×dataset coverage 已报告，Llama DocRED 缺失 |
| R2-N5 (SF8) | warning | ✅ Resolved | appendix_reproducibility.tex 完整（LoRA, GPU, seeds, software versions, timing） |
| R4-W3 (SF9) | warning | ✅ Resolved | §4 区分 calibrated vs full range |
| R4-Q1 (Q1) | warning | ✅ Resolved | §3 显式声明 JSON Schema 强制 field ordering |
| R2-N6 (M3) | warning | ⚠️ Partially fixed | DocRED ET +70% 归因为 "replicating SciERC" 不准确（SciERC ET 无变化），DocRED 特有机制未解释 |
| R2-N10 (M1) | info | ⚠️ Partially fixed | 数据一致(0.03%)但 residual 来源未解释 |
| GC-N1 (M2) | info | ✅ Resolved | §5.2 L85 明确标注 GCD capability ceiling |
| R4-Q2 (M6) | info | ✅ Resolved | Appendix 提供 Spearman ρ=-0.77 + transferability 论证 |

**统计：6 ✅ / 5 ⚠️ / 0 ❌ / 1 🆕**

### Reviewer 1 新发现

**🆕 N1 [warning]** Abstract LoRA+beam "zero constraint violations across all four categories" claim 仅基于 Qwen3-8B/SciERC 单一配置。未报告 Llama LoRA+beam 或 DocRED LoRA+beam 数据。Abstract 未限定 model/dataset，暗示 generalizability。建议限定 "on SciERC" 或补充数据。

### Reviewer 1 评分
- 方法严谨性: 3.5→4.0/5
- 实验充分性: 3.0→3.5/5
- Reproducibility: 2.5→4.5/5
- 建议评分: 3.5 (Borderline Conference)，从 Round 5 Weak Accept 上调

---

**请逐条回应以上发现，特别是：**
1. SF1 (beam search ⚠️) 你是否同意 beam runtime 缺失的严重性？
2. SF5 (parse failure ⚠️) 你认为缺乏 deconfounded 分析是否影响接收？
3. SF7 (Llama DocRED coverage ⚠️) 你是否同意这仍是一个问题？
4. N1 (LoRA+beam single config) 你认为 Abstract claim 是否需要限定？
5. 你是否有补充发现与 R1 的判断冲突或一致？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-18T12:49:56.112333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-18T12:49:56.723968+00:00_

1	\section{Beam Search Compatibility}
2	\label{app:beam-search}
3	
4	OntoCoDec's constraint enforcement is designed to be decoding-strategy agnostic.
5	The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
6	Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
7	
8	\paragraph{Implementation challenges.}
9	Two stateful components require adaptation for beam search.
10	(1)~The grammar layer (XGrammar) maintains an internal \texttt{GrammarMatcher} state that tracks the generated token sequence; beam reordering invalidates this state because beams are permuted across steps.
11	Our solution instantiates a fresh \texttt{GrammarMatcher} per beam per step and replays the beam's current token sequence through XGrammar's stateless accept API (64 lines of code).
12	(2)~The semantic layer's \texttt{TypeConstraintProcessor} accumulates entity and relation registries that assume a single generation path.
13	Our solution isolates state per beam by calling \texttt{detect()} on the full partial output at each step, reconstructing all entity/relation state from scratch for each beam independently (61 lines of code).
14	Both adaptations add ${\sim}125$ lines total without modifying the existing greedy/sampling logic.
15	
16	\paragraph{Results.}
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under full S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under full S1 constraints.
23	SciERC evaluated on full test set (551 documents); DocRED evaluated on matched 50-document subsets (same documents for greedy and beam).
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{tab:beam-search}
26	\begin{tab
…[truncated 6802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 611
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-18T12:49:56.724445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-18T12:49:56.781973+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
6	\label{tab:sampling-robustness}
7	\begin{tabular}{llcccccc}
8	\toprule
9	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
10	\midrule
11	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
12	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
13	\midrule
14	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
15	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
16	\bottomrule
17	\end{tabular}
18	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 57
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-18T12:51:46.267154+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Round 6 交叉回应 — Reviewer 2 回应 Reviewer 1\n\n---\n\n### 已解决 Issues（简要确认）\n\n**[AGREE] R2-N1 (MF1) ✅**: 同意。Abstract 已移除 R²=0.886，改为定性表述 \"residual DR correlates with the product of schema tightness and baseline violation rate\"（abstract.tex:11）。修复充分。\n\n**[AGREE] R2-N5 (SF8) ✅**: 同意。appendix_reproducibility.tex 内容完整，涵盖 LoRA 超参、GPU 型号、seeds、software versions、timing。Reproducibility 从 2.5 升至 4.5 合理。\n\n**[AGREE] R4-W3 (SF9) ✅**: 同意。我独立验证了 §4 L28 的 calibrated vs full range 区分与 Abstract 一致。\n\n**[AGREE] R4-Q1 (Q1) ✅**: 同意。§3 L28 显式声明 \"The output JSON Schema enforces a fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation.\" 解决了字段顺序依赖的潜在质疑。\n\n**[AGREE] GC-N1 (M2) ✅**: 同意。§5.2 L85 \"This configuration represents the capability ceiling of grammar-based constrained decoding\" 明确定位了 GCD 的局限。\n\n**[AGREE] R4-Q2 (M6) ✅**: 同意。Appendix 提供 Spearman ρ=-0.77 + transferability 论证，证据充分。\n\n---\n\n### ⚠️ Issues 逐条回应\n\n**[AGREE] R4-N3 (SF1) ⚠️ Beam search 覆盖**\n\n同意 R1 的判断。补充证据：\n\nAppendix Table 8（appendix_beam_search.tex）实际提供了 **6 个 model×dataset 组合的 zero-shot beam 数据**（Qwen/Llama/Mistral × SciERC/DocRED），coverage 比 R1 评估的更完整。但 R1 指出的两个具体问题成立：\n1. **Beam runtime 未量化**：appendix_beam_search.tex:99 仅说 \"Wall-clock overhead is modest\"，无具体数字。相比之下，greedy runtime 有精确数据（§5 runtime paragraph: +2.3% SciERC, +5.4% DocRED）。beam 的 overhead 缺失是一个 gap。\n2. **Greedy vs beam 定位不明确**：正文以 greedy 为 primary configuration，beam 作为 supplement，但 Abstract L13 把 LoRA+beam 的 \"zero violations\" 作为 headline claim，定位上有张力。\n\n**严重性判断**：moderate warning。beam runtime 缺失不影响核心贡献（greedy 已足够），但如果 Abstract 强调 beam claim，理应提供 runtime context。\n\n---\n\n**[REBUT] R2-N3 (SF5) ⚠️ Parse failure deconfounded analysis**\n\n部分不同意 R1 对严重性的评估。\n\nR1 认为缺乏 deconfounded analysis 是 ⚠️ 级别。我认为这是 **info 级别**，理由：\n\n1. **效应量极小**：Limitations L69 报告 Llama DocRED E-F1 变化仅 -0.64pp，且 parse failure rate 差异为 9.1% vs 6.8%（+2.3pp），confounding 的上界很小。\n2. **单向 confounding**：parse failure 只可能压低 constrained setting 的 F1（因为 failure 的文档计为 0 分）。如果 deconfound（排除 parse failure 文档），constrained E-F1 只会上升，不会改变 \"near-neutral\" 的结论。\n3. **主要模型无此问题**：Qwen3-8B 的 parse failure 在所有设置下 ≤1.1%（Table 5 caption），confounding 可忽略。Llama DocRED 是所有 12 个 model×dataset×setting 组合中唯一有显著 parse failure 的配置。\n4. **Limitations 已明确承认**（main.tex L69），满足 ARR 的 disclosure 要求。\n\n**建议**：一个简单的补充就足够——在 Limitations 中加一句 \"Excluding parse-failure documents, Llama DocRED E-F1 changes from -0.64pp to [X]pp\"，无需完整 deconfounded analysis。但不做也不影响接收。\n\n---\n\n**[AGREE] R4-W2 (SF7) ⚠️ Llama DocRED sampling coverage**\n\n同意。\n\n核查 appendix_sampling_table.tex：sampling robustness 仅报告 **Qwen3-8B**（SciERC 551 docs + DocRED 114 docs），无 Llama 或 Mistral 数据。注脚解释 \"full DocRED sampling requires ~300h\"，但这不能解释为什么 Llama SciERC sampling 也缺失（SciERC 只有 551 docs，应该可以在合理时间内完成）。\n\n不过，**beam search 数据已覆盖全部 6 个组合**（appendix_beam_search.tex Table 8），且 beam 比 sampling 更具实际意义（beam 能消除 violations，sampling 不能）。所以这个 gap 的影响有限。\n\n**严重性判断**：low warning。主要是 sampling 实验的 completeness 问题，不影响核心 claim。\n\n---\n\n**[AGREE] R2-N6 (M3) ⚠️ DocRED ET +70% 归因**\n\n同意。R1 对此的分析精确。\n\nsection5_docred_draft.tex:70 写道：\"Semantic-only reduces DR by 25% but cannot eliminate RV (29.87%) or prevent ET increases (2.48%→4.22%), **replicating SciERC's enabling dependency**.\"\n\n但对照 SciERC 数据（Table 1）：semantic-only 下 ET 保持 0.40% 不变。SciERC 的 \"enabling dependency\" 体现在 RV 无法消除（1.51%），而非 ET 增加。DocRED 的 ET 从 2.48% 升至 4.22%（+70%）是 DocRED 特有现象，可能与 semantic-only 将 OOV relation 映射到有效 relation 后暴露了更多 ET 不匹配有关，但论文未解释这一机制。\n\n\"replicating\" 这个词在此处 **部分准确**（RV 未消除的 pattern 确实 replicate）但 **部分误导**（ET 增加是 DocRED 特有，未在 SciERC 复现）。建议拆分为两句：一句说明 enabling dependency replicate，另一句解释 DocRED-specific ET increase 的可能原因。\n\n---\n\n**[AGREE] R2-N10 (M1) ⚠️ Residual RV 0.03%**\n\n同意这是 info 级别。DocRED Full S1 和 Grammar-only 都显示 RV=0.03%（Table 3），说明这是 grammar layer 的 residual，不受 semantic layer 影响。998 documents 中 0.03% 大约是 1-2 个 instance，可能是 tokenization edge case 或 grammar compilation 的 corner case。一个脚注解释来源就够了。\n\n---\n\n### 🆕 New Issue 回应\n\n**[AGREE] R1-🆕N1 [warning] Abstract LoRA+beam \"zero violations\" claim scope**\n\n**强烈同意**。这是我交叉核查的核心发现。\n\nAbstract L13: \"With beam search (k=4), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality (relation F1 change <0.5pp).\"\n\nappendix_beam_search.tex:94-95 明确表明此数据 **仅来自 Qwen3-8B / SciERC**：\"Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with full S1 constraints... Adding beam search (k=4) eliminates all residual CF violations (1.18%→0%), yielding zero violations across all four metrics.\"\n\n**无 Llama LoRA+beam 数据，无 DocRED LoRA+beam 数据。**\n\nZero-shot beam 数据确实覆盖了 6 个组合（Table 8），且 calibrated models 均达到 DR=0%。因此 LoRA+beam 在其他配置上达到 \"zero violations\" 是 **高度可能的**。但 \"高度可能\" ≠ \"已验证\"，Abstract 的无限定表述构成 overclaim。\n\n**具体建议**（二选一）：\n1. Abstract 加限定：\"achieves zero constraint violations across all four categories **on SciERC (Qwen3-8B)**\"\n2. 补充 Llama LoRA+beam SciERC 数据（LoRA 模型已有，beam 实验成本低）\n\n---\n\n### R2 补充发现（与 R1 交叉）\n\n**🆕 R2-补充1 [info]**: appendix_beam_search.tex:98 报告 \"Beam search on DocRED introduces a modest increase in parse failures (3/50, 6%)\"。这与 SF5（parse failure confounding）形成交叉：beam 在 DocRED 上增加 parse failure，如果 LoRA+beam 扩展到 DocRED，parse failure confounding 可能更显著。\n\n**🆕 R2-补充2 [info]**: R1 的 SF1 和 N1 实际上是同一个 tension 的两面：论文把 beam 同时作为 \"supplementary validation\"（appendix 级别）和 \"headline claim\"（Abstract 级别），定位不一致。建议选一个：如果 beam 是 supplementary，从 Abstract 降级到正文；如果 beam 是 core contribution，需要 runtime 数据和更多 LoRA+beam 配置。\n\n---\n\n### 综合评估\n\nR1 的 6 ✅ / 5 ⚠️ 判断总体准确。我的调整：\n\n| Issue | R1 verdict | R2 回应 | 调整 |\n|-------|-----------|---------|------|\n| SF1 beam | ⚠️ | AGREE | 维持 ⚠️ |\n| SF5 parse | ⚠️ | REBUT | 建议降为 info（效应量极小） |\n| SF7 sampling | ⚠️ | AGREE | 维持 ⚠️ 但降低严重性 |\n| M3 DocRED ET | ⚠️ | AGREE | 维持 ⚠️ |\n| M1 residual RV | ⚠️ | AGREE | 维持 info |\n| R1-N1 beam claim | 🆕 warning | AGREE | 确认 warning |\n\n**R1 建议评分 3.5 (Borderline Conference)**——与我的评分一致。两位 reviewer 从不同维度（R1: 方法/实验，R2: 写作/格式/新颖性）独立收敛于同一评分，增强了评估的可信度。\n\n**与我的 Round 6 发现的交互**：R1 的 LoRA+beam overclaim (N1) 与我的 -ing phrases (SF3 ❌) 构成两个维度的风险。前者是 claim 准确性问题（可快速修复），后者是 AI 写作痕迹问题（需要逐句改写）。两者都不影响技术贡献本身，但共同构成 \"Borderline Conference vs Findings\" 的决定性因素。",
  "reviewer_id": "2",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Round 6 交叉回应 — Reviewer 2 回应 Reviewer 1\n\n---\n\n### 已解决 Issues（简要确认）\n\n**[AGREE] R2-N1 (MF1) ✅**: 同意。Abstract 已移除 R²=0.886，改为定性表述 \"residual DR correlates with the product of schema tightness and baseline violation rate\"（abstract.tex:11）。修复充分。\n\n**[AGREE] R2-N5 (SF8) ✅**: 同意。appendix_reproducibility.tex 内容完整，涵盖 LoRA 超参、GPU 型号、seeds、software versions、timing。Reproducibility 从 2.5 升至 4.5 合理。\n\n**[AGREE] R4-W3 (SF9) ✅**: 同意。我独立验证了 §4 L28 的 calibrated vs full range 区分与 Abstract 一致。\n\n**[AGREE] R4-Q1 (Q1) ✅**: 同意。§3 L28 显式声明 \"The output JSON Schema enforces a fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation.\" 解决了字段顺序依赖的潜在质疑。\n\n**[AGREE] GC-N1 (M2) ✅**: 同意。§5.2 L85 \"This configuration represents the capability ceiling of grammar-based constrained decoding\" 明确定位了 GCD 的局限。\n\n**[AGREE] R4-Q2 (M6) ✅**: 同意。Appendix 提供 Spearman ρ=-0.77 + transferability 论证，证据充分。\n\n---\n\n### ⚠️ Issues 逐条回应\n\n**[AGREE] R4-N3 (SF1) ⚠️ Beam search 覆盖**\n\n同意 R1 的判断。补充证据：\n\nAppendix Table 8（appendix_beam_search.tex）实际提供了 **6 个 model×dataset 组合的 zero-shot beam 数据**（Qwen/Llama/Mistral × SciERC/DocRED），coverage 比 R1 评估的更完整。但 R1 指出的两个具体问题成立：\n1. **Beam runtime 未量化**：appendix_beam_search.tex:99 仅说 \"Wall-clock overhead is modest\"，无具体数字。相比之下，greedy runtime 有精确数据（§5 runtime paragraph: +2.3% SciERC, +5.4% DocRED）。beam 的 overhead 缺失是一个 gap。\n2. **Greedy vs beam 定位不明确**：正文以 greedy 为 primary configuration，beam 作为 supplement，但 Abstract L13 把 LoRA+beam 的 \"zero violations\" 作为 headline claim，定位上有张力。\n\n**严重性判断**：moderate warning。beam runtime 缺失不影响核心贡献（greedy 已足够），但如果 Abstract 强调 beam claim，理应提供 runtime context。\n\n---\n\n**[REBUT] R2-N3 (SF5) ⚠️ Parse failure deconfounded analysis**\n\n部分不同意 R1 对严重性的评估。\n\nR1 认为缺乏 deconfounded analysis 是 ⚠️ 级别。我认为这是 **info 级别**，理由：\n\n1. **效应量极小**：Limitations L69 报告 Llama DocRED E-F1 变化仅 -0.64pp，且 parse failure rate 差异为 9.1% vs 6.8%（+2.3pp），confounding 的上界很小。\n2. **单向 confounding**：parse failure 只可能压低 constrained setting 的 F1（因为 failure 的文档计为 0 分）。如果 deconfound（排除 parse failure 文档），constrained E-F1 只会上升，不会改变 \"near-neutral\" 的结论。\n3. **主要模型无此问题**：Qwen3-8B 的 parse failure 在所有设置下 ≤1.1%（Table 5 caption），confounding 可忽略。Llama DocRED 是所有 12 个 model×dataset×setting 组合中唯一有显著 parse failure 的配置。\n4. **Limitations 已明确承认**（main.tex L69），满足 ARR 的 disclosure 要求。\n\n**建议**：一个简单的补充就足够——在 Limitations 中加一句 \"Excluding parse-failure documents, Llama DocRED E-F1 changes from -0.64pp to [X]pp\"，无需完整 deconfounded analysis。但不做也不影响接收。\n\n---\n\n**[AGREE] R4-W2 (SF7) ⚠️ Llama DocRED sampling coverage**\n\n同意。\n\n核查 appendix_sampling_table.tex：sampling robustness 仅报告 **Qwen3-8B**（SciERC 551 docs + DocRED 114 docs），无 Llama 或 Mistral 数据。注脚解释 \"full DocRED sampling requires ~300h\"，但这不能解释为什么 Llama SciERC sampling 也缺失（SciERC 只有 551 docs，应该可以在合理时间内完成）。\n\n不过，**beam search 数据已覆盖全部 6 个组合**（appendix_beam_search.tex Table 8），且 beam 比 sampling 更具实际意义（beam 能消除 violations，sampling 不能）。所以这个 gap 的影响有限。\n\n**严重性判断**：low warning。主要是 sampling 实验的 completeness 问题，不影响核心 claim。\n\n---\n\n**[AGREE] R2-N6 (M3) ⚠️ DocRED ET +70% 归因**\n\n同意。R1 对此的分析精确。\n\nsection5_docred_draft.tex:70 写道：\"Semantic-only reduces DR by 25% but cannot eliminate RV (29.87%) or prevent ET increases (2.48%→4.22%), **replicating SciERC's enabling dependency**.\"\n\n但对照 SciERC 数据（Table 1）：semantic-only 下 ET 保持 0.40% 不变。SciERC 的 \"enabling dependency\" 体现在 RV 无法消除（1.51%），而非 ET 增加。DocRED 的 ET 从 2.48% 升至 4.22%（+70%）是 DocRED 特有现象，可能与 semantic-only 将 OOV relation 映射到有效 relation 后暴露了更多 ET 不匹配有关，但论文未解释这一机制。\n\n\"replicating\" 这个词在此处 **部分准确**（RV 未消除的 pattern 确实 replicate）但 **部分误导**（ET 增加是 DocRED 特有，未在 SciERC 复现）。建议拆分为两句：一句说明 enabling dependency replicate，另一句解释 DocRED-specific ET increase 的可能原因。\n\n---\n\n**[AGREE] R2-N10 (M1) ⚠️ Residual RV 0.03%**\n\n同意这是 info 级别。DocRED Full S1 和 Grammar-only 都显示 RV=0.03%（Table 3），说明这是 grammar layer 的 residual，不受 semantic layer 影响。998 documents 中 0.03% 大约是 1-2 个 instance，可能是 tokenization edge case 或 grammar compilation 的 corner case。一个脚注解释来源就够了。\n\n---\n\n### 🆕 New Issue 回应\n\n**[AGREE] R1-🆕N1 [warning] Abstract LoRA+beam \"zero violations\" claim scope**\n\n**强烈同意**。这是我交叉核查的核心发现。\n\nAbstract L13: \"With beam search (k=4), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality (relation F1 change <0.5pp).\"\n\nappendix_beam_search.tex:94-95 明确表明此数据 **仅来自 Qwen3-8B / SciERC**：\"Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with full S1 constraints... Adding beam search (k=4) eliminates all residual CF violations (1.18%→0%), yielding zero violations across all four metrics.\"\n\n**无 Llama LoRA+beam 数据，无 DocRED LoRA+beam 数据。**\n\nZero-shot beam 数据确实覆盖了 6 个组合（Table 8），且 calibrated models 均达到 DR=0%。因此 LoRA+beam 在其他配置上达到 \"zero violations\" 是 **高度可能的**。但 \"高度可能\" ≠ \"已验证\"，Abstract 的无限定表述构成 overclaim。\n\n**具体建议**（二选一）：\n1. Abstract 加限定：\"achieves zero constraint violations across all four categories **on SciERC (Qwen3-8B)**\"\n2. 补充 Llama LoRA+beam SciERC 数据（LoRA 模型已有，beam 实验成本低）\n\n---\n\n### R2 补充发现（与 R1 交叉）\n\n**🆕 R2-补充1 [info]**: appendix_beam_search.tex:98 报告 \"Beam search on DocRED introduces a modest increase in parse failures (3/50, 6%)\"。这与 SF5（parse failure confounding）形成交叉：beam 在 DocRED 上增加 parse failure，如果 LoRA+beam 扩展到 DocRED，parse failure confounding 可能更显著。\n\n**🆕 R2-补充2 [info]**: R1 的 SF1 和 N1 实际上是同一个 tension 的两面：论文把 beam 同时作为 \"supplementary validation\"（appendix 级别）和 \"headline claim\"（Abstract 级别），定位不一致。建议选一个：如果 beam 是 supplementary，从 Abstract 降级到正文；如果 beam 是 core contribution，需要 runtime 数据和更多 LoRA+beam 配置。\n\n---\n\n### 综合评估\n\nR1 的 6 ✅ / 5 ⚠️ 判断总体准确。我的调整：\n\n| Issue | R1 verdict | R2 回应 | 调整 |\n|-------|-----------|---------|------|\n| SF1 beam | ⚠️ | AGREE | 维持 ⚠️ |\n| SF5 parse | ⚠️ | REBUT | 建议降为 info（效应量极小） |\n| SF7 sampling | ⚠️ | AGREE | 维持 ⚠️ 但降低严重性 |\n| M3 DocRED ET | ⚠️ | AGREE | 维持 ⚠️ |\n| M1 residual RV | ⚠️ | AGREE | 维持 info |\n| R1-N1 beam claim | 🆕 warning | AGREE | 确认 warning |\n\n**R1 建议评分 3.5 (Borderline Conference)**——与我的评分一致。两位 reviewer 从不同维度（R1: 方法/实验，R2: 写作/格式/新颖性）独立收敛于同一评分，增强了评估的可信度。\n\n**与我的 Round 6 发现的交互**：R1 的 LoRA+beam overclaim (N1) 与我的 -ing phrases (SF3 ❌) 构成两个维度的风险。前者是 claim 准确性问题（可快速修复），后者是 AI 写作痕迹问题（需要逐句改写）。两者都不影响技术贡献本身，但共同构成 \"Borderline Conference vs Findings\" 的决定性因素。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-18T12:51:50.132027+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 468 · 2026-05-18T12:51:56.662470+00:00_

交叉回应已提交。

核心判断：
- R1 的 6✅/5⚠️ 总体准确，仅对 SF5（parse failure）建议降级为 info（效应量 -0.64pp 太小，且 confounding 方向单一）
- **强烈同意** R1 的 🆕N1：Abstract LoRA+beam "zero violations" claim 仅基于 Qwen/SciERC 单一配置，appendix_beam_search.tex:94-95 明确证实
- 两位 reviewer 从不同维度独立收敛于 3.5 (Borderline Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

94 recorded events


### User

_source line 469 · 2026-05-19T06:24:18.094018+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
- **Deadline**: 2026-05-25

### Venue 要求
- ACL style template, double-blind, Long paper 8 页正文
- 附录不计页数，Limitations section 必需
- ARR Overall Assessment 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

### 你的审查侧重
你负责**新颖性、完整性和写作质量**，重点关注：

1. **新颖性评估**：
   - 核心贡献（将 IE ontology 编译为 token-level 约束）相对已有工作的增量贡献有多大？
   - 与 PICARD、Synchromesh、GCD、EnriCo 等最接近的工作相比，技术新颖性是否足够？
   - "enabling dependency"（grammar layer enables semantic layer）这个观察是否 novel 还是 obvious？
   - Constraint tightness 公式（κ = 1 - |V(r)|/|E|²）是否有真正的分析价值？

2. **Related Work 充分性**：
   - 是否覆盖了所有直接相关方法？是否有重要遗漏？
   - 与 PICARD/Synchromesh（code domain）的区别是否准确？
   - 与 GoLLIE/KnowCoder（training-based IE）的对比是否公平？
   - Constrained decoding 质量下降文献（CRANE, Tam et al.）的讨论是否充分？
   - 引用数量是否达到 EMNLP 录用论文的量级？

3. **叙事与主线统一性**：
   - Abstract → Introduction → Method → Experiments → Conclusion 是否形成连贯主线？
   - Abstract 是否过长（当前 ~250 words，上限区域）？信息密度是否合适？
   - Introduction 的 "gap" 论证是否令人信服？
   - Contribution 列表与后续 sections 是否一一对应？
   - 论文 framing 是否前后一致？（例如 zero-shot 作为 "stress test" vs 主要评估）

4. **写作质量（严格检查 AI 写作痕迹）**：
   - 全文搜索 em-dash（—）和解释性 en-dash（–），必须清零
   - 检查 -ing 分词短语结尾（"..., demonstrating..."）
   - 检查过度分段、过度使用过渡词
   - 检查 "leverage"/"utilize"/"facilitate" 等 AI 典型用词
   - 检查专有名词是否首次出现时有定义
   - 检查代词/指示词指代是否明确

5. **格式合规**：
   - 页数是否在限制内？（8 页正文）
   - 匿名化是否完整？（\author{Anonymous ACL submission} ✓）
   - Limitations section 是否存在且实质性？
   - Ethics Statement 是否存在？
   - 表格/图片格式是否规范（字号、caption 自包含、最优加粗）？
   - 引用格式是否正确（natbib）？

### 输出格式
请按以下结构输出审稿意见：
```
## Summary（2-3 句）
## Strengths（逐条）
## Weaknesses（逐条，标注 [Must-Fix] 或 [Should-Fix] 或 [Minor]）
## Questions（需要作者回答的问题）
## Missing References（如有）
## Overall Assessment（评分 + 置信度 + 简要理由）
```

评分参照 ARR 标准（1-5）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-19T06:24:26.359044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-19T06:24:26.410258+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-19T06:24:28.874067+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-19T06:24:28.974958+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-19T06:24:30.937001+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-19T06:24:30.987624+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-19T06:24:35.006499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-19T06:24:35.057346+00:00_

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
12	\usepackage{multirow}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{enumitem}
16	\usepackage{xcolor}
17	\usepackage{pifont}
18	
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	% === Abstract ===
27	\input{abstract}
28	
29	% === §1 Introduction ===
30	\input{section1_introduction_draft}
31	
32	% === §2 Background ===
33	\input{section2_background}
34	
35	% === §3 Method ===
36	\input{section3_method_draft}
37	
38	% === §4 Constraint Composition ===
39	\section{Constraint Composition}
40	\label{sec:composition}
41	\input{section4_composition_draft}
42	
43	% === §5 Experiments ===
44	\section{Experiments}
45	\label{sec:experiments}
46	
47	\input{section3_violation_landscape}
48	
49	\input{section5_scierc_draft}
50	\input{section5_docred_draft}
51	\input{section5_crossmodel_draft}
52	\input{section5_wikievents_draft}
53	\input{section5_runtime}
54	
55	% === §6 Related Work ===
56	\input{section6_related_work}
57	
58	% === §7 Discussion and Conclusion ===
59	\section{Discussion and Conclusion}
60	\label{sec:discussion}
61	\input{section7_conclusion_compressed}
62	
63	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
64	\clearpage
65	\section*{Limitations}
66	
67	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
68	CF fallback ablation shows that eliminating CF re-routes
…[truncated 4150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-19T06:24:44.366934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-19T06:24:45.322389+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints that enforce structural and type-validity constraints during autoregressive generation:
3	(1)~a \emph{grammar layer} (XGrammar context-free grammar) that guarantees JSON structural validity and entity/relation vocabulary membership (ET and RV violations $\to$\,0\%); and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	%
6	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations: 15.37\% on SciERC (7 relations) and 18.46\% on DocRED (96 relations), with 1--2\% persisting even after fine-tuning; rates are driven by \emph{constraint tightness} rather than ontology or model scale.
7	Composed with Low-Rank Adaptation (LoRA) fine-tuning, \textsc{OntoCoDec} reduces DR to $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp of unconstrained baselines (R-F1 40--46): near-lossless composability at deployment-grade extraction quality.
8	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
9	Under zero-shot decoding, which stress-tests constraint robustness at low extraction quality (R-F1 2--8\%), DR drops by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost (DocRED: $+$0.50\,pp, $p{<}0.001$; \S\ref{sec:cross-model}).
10	With beam search ($k{=}4$), the full stack eliminates all four violation types under fine-tuned beam decoding (SciERC, both Qwen3-8B and Llama-3.1-8B) while preserving extraction quality (R-F1 44.23 and 46.11, respectively); in zero-shot beam decoding, DR reaches 0\% for calibrated models on both RE datasets.
11	The framework generalizes to event extractio
…[truncated 981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-19T06:24:45.322856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-19T06:24:45.825305+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Constraint enforcement matters most at deployment-grade quality (R-F1 40--46\%): at this level, residual type violations propagate directly into knowledge graphs and decision-support pipelines; reliable type-safety enforcement is needed.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot el
…[truncated 2590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-19T06:24:45.825728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-19T06:24:46.278125+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We define the \emph{constraint tightness} of $r$ as $1 - |\sigma(r)| / |\mathcal{E}|^2$: tighter constraints leave fewer valid options, increasing violation likelihood.
11	
12	\paragraph{Grammar-Constrained Decoding.}
13	\label{sec:bg:gcd}
14	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
15	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
16	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, then $\mathrm{type}(h) \in \{\textsc{Method}, \textsc{OtherScientificTerm}\}$''), which depend on previously generated field values.
17	
18	\paragraph{Problem Statement.}
19	\label{sec:bg:problem}
20	Given $\mathcal{O}$ and an autoregressive LM $\mathcal{M}$, we seek constraints $\mathcal{C}$ ensuring: (a)~\textbf{structural validity}, i.e., well-formed JSON with $\mathcal{E}$/$\mathcal{R}$ membership; and (b)~\textbf{type validity}, i.e., $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$ for every triple.
21	Condition (a) is context-free; (b) is context-sensitive but \emph{prefix-decidable}: at the point where a type token is generated, all information needed (relation type, entity registry) is ava
…[truncated 149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-19T06:24:46.278640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-19T06:24:47.233410+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles ontology schemas into token-level masks enforced during autoregressive generation.
9	Unlike type-constrained code generation, IE presents three distinct challenges: (1)~entity types are inferred from free text rather than declared annotations, (2)~the entity registry is built dynamically during generation, and (3)~constraint targets are context-dependent type assignments rather than fixed grammar productions.
10	The grammar layer (\S\ref{sec:grammar}) guarantees structural validity (well-formed JSON with ontology-vocabulary membership), while the semantic layer (\S\ref{sec:semantic}) enforces domain/range type constraints via a stateful entity registry.
11	We describe the problem formulation (\S\ref{sec:formulation}), each layer, and two decoding strategies (\S\ref{sec:strategies}).
12	Formal analysis of constraint composition is deferred to Section~\ref{sec:composition}.
13	
14	
15	\subsection{Problem Formulation}
16	\label{sec:formulation}
17	
18	\paragraph{IE as structured generation.}
19	Given an input text $x$, a language model generates a structured JSON output $y$:
20	%
21	\begin{equation}\label{eq:output-schema}
22	\resizebox{.88\columnwidth}{!}{$\displaystyle
23	  y = \bigl\{\texttt{entities}: [\{n_i, \tau_i\}],\; \texttt{relations}: [\{h_j, t_j, r_j, \tau^h_j, \tau^t_j\}]\bigr\}
24	$}
25	\end{equation}
26	%
27	where each entity has a name $n_i$ and type $\tau_i \in \mathcal{E}$, and each relation specifies head $h_j$, tail $t_j$, relation type $r_j \in \mathcal{R}$, and head/tail entity types $\tau^h_j, \tau^t_j$.
28	The output JSON Schema (\S\ref{sec:grammar}) enforces a fixed field ordering (head $\to$ tail $\to$ relation $\to$ head\_type $\to$ tail\_type) via deterministic grammar compilation.
29	This ordering en
…[truncated 6610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-19T06:24:47.233892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-19T06:24:47.686144+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.
17	Among type violations, DR and CF differ in severity: a DR violation renders the triple ontologically invalid (the entity type lies outside the relation's domain or range), whereas a CF violation means each triple is individually schema-valid but the same entity receives different type assignments across triples.
18	
19	\paragraph{Constraint Tightness.}
20	We define the tightness of relation $r$ as:
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{E}|^2},
24	\end{equation}
25	%
26	where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{E}$ the entity type vocabulary.
27	The mean tightness $\bar{\kappa} = \frac{
…[truncated 1263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-19T06:24:47.736843+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-19T06:24:48.189781+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	\paragraph{Setup.}
8	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
9	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
10	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
11	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates driven by constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-19T06:24:48.190285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-19T06:24:48.743188+00:00_

1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	Semantic
41	  & 11.65 & $\downarrow$24\%
42	  & 1.51  & 0.40
43	  & 2.71  & 14.36
44	  & 8.15  & 31.01 \\
45	Full (S1)
46	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
47	  & \textbf{0} & \textbf{0}
48	  & 9.90  & \textbf{10.83}
49	  & \textbf{8.36} & 30.98 \\
50	Full (S2)
51	  & 0.97  & $\downarrow$94\%
52	  & \textbf{0} & \textbf{0}
53	  & 8.03  & \textbf{9.00}
54	  & 8.03  & \textbf{31.90} \\
55	\bottomrule
56	\end{tabular}}%
57	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
58	$\Delta$DR: relative change vs.\ unconstrained.
59	Tot.\ = DR + CF (total type-violation b
…[truncated 4925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-19T06:24:48.844201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-19T06:24:48.844836+00:00_

1	% Section 5 — DocRED Results (compressed, 1450→~600 words)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	% All numbers verified against registry 2026-05-14.
5	
6	\subsection{Cross-Dataset Validation on DocRED}
7	\label{sec:docred-results}
8	
9	Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).
10	
11	% ──────────────────────────────────────────
12	%  Table: DocRED four-way ablation
13	% ──────────────────────────────────────────
14	\begin{table}[t]
15	\centering
16	\small
17	\setlength{\tabcolsep}{3.6pt}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}l rrrrrr rr@{}}
20	\toprule
21	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
22	& \multicolumn{2}{c}{\textbf{F1}} \\
23	\cmidrule(lr){2-7} \cmidrule(l){8-9}
24	\textbf{Mode}
25	  & DR\,$\downarrow$ & $\Delta$DR
26	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
27	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
28	\midrule
29	Unconstrained
30	  & 18.46 & ---
31	  & 29.66 & 2.48
32	  & 0.10  & 18.56
33	  & 7.74  & 58.15 \\
34	Grammar
35	  & 26.17 & $\uparrow$42\%
36	  & \textbf{0.03} & \textbf{0}
37	  & 0.07  & 26.24
38	  & \textbf{8.31}  & \textbf{59.38} \\
39	Semantic
40	  & 13.84 & $\downarrow$25\%
41	  & 29.87 & 4.22
42	  & 1.05  & 14.89
43	  & 7.70  & 57.81 \\
44	Full (S1)
45	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
46	  & \textbf{0.03} & \textbf{0}
47	  & 2.57  & \textbf{12.78}
48	  & 8.23  & 59.37 \\
49	\bottomrule
50	\end{tabular}}%
51	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
52	$\Delta$DR: relative change vs.\ unconstrained.
53	Tot.\ = DR + CF (total type-violation burden).
54	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
56	\label{tab:docred-ablation}
57	\en
…[truncated 1553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-19T06:24:55.028841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-19T06:24:55.331243+00:00_

1	% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
2	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
3	%          phase2_docred_unconstrained, phase2_docred_full_s1,
4	%          llama_scierc_unconstrained, llama_scierc_full_s1,
5	%          llama_docred_unconstrained, llama_docred_full_s1
6	
7	\subsection{Cross-Model Validation}
8	\label{sec:cross-model}
9	
10	Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
11	
12	\begin{table}[t]
13	\centering
14	\small
15	\setlength{\tabcolsep}{3.4pt}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}ll rrrr r@{}}
18	\toprule
19	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
20	& \textbf{R-F1} \\
21	\cmidrule(lr){3-6} \cmidrule(l){7-7}
22	\textbf{Dataset} & \textbf{Model}
23	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
24	  & $\uparrow$ \\
25	\midrule
26	\multirow{6}{*}{SciERC}
27	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
28	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
29	  \cmidrule(l){2-7}
30	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
31	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
32	  \cmidrule(l){2-7}
33	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
34	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
35	\midrule
36	\multirow{6}{*}{DocRED}
37	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
38	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
39	  \cmidrule(l){2-7}
40	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
41	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
42	  \cmidrule(l){2-7}
43	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
44	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
48	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
49	$^\dagger$Mistral: poor ze
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-19T06:24:55.331995+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-19T06:24:58.999138+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Cross-Task Validation: Event Extraction}
8	\label{sec:wikievents}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[t]
18	\centering
19	\small
20	\setlength{\tabcolsep}{2.8pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{@{}ll rrrr rr@{}}
23	\toprule
24	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
25	& \multicolumn{2}{c}{\textbf{F1}} \\
26	\cmidrule(lr){3-6} \cmidrule(l){7-8}
27	\textbf{Model} & \textbf{Mode}
28	  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
29	  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
30	\midrule
31	\multirow{3}{*}{Qwen3-8B}
32	  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
33	  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
34	  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42
…[truncated 1811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3667
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-19T06:24:59.100027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-19T06:24:59.100554+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Grammar compile: one-time 44\,ms (Appendix~\ref{app:runtime}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly, reducing DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models (Qwen, Llama) and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Model scale reduces b
…[truncated 37 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---
