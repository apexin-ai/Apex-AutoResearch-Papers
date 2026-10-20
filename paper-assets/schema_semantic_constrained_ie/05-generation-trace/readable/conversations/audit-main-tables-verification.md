# audit main tables verification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_audit_main-tables-verification_20260523T102235.jsonl`
- **Structured JSON:** [`60658d7378f6f5fb943a.json`](../../sessions/60/60658d7378f6f5fb943a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-23T10:30:22.447562+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T10:30:22.447966+00:00_

abstract.tex
abstract_d3264e.tex
abstract_fd4b26.tex
acl.sty
acl_natbib.bst
appendix_70b_ablation.tex
appendix_beam_search.tex
appendix_case_studies.tex
appendix_discussion.tex
appendix_doc_length.tex
appendix_downstream_analysis.tex
appendix_full_ft.tex
appendix_gollie_comparison.tex
appendix_high_kappa_analysis.tex
appendix_kappa_case_study.tex
appendix_llama_per_relation.tex
appendix_order_invariance.tex
appendix_power_analysis.tex
appendix_power_analysis_523cc9.tex
appendix_prompt_sensitivity.tex
appendix_prompts.tex
appendix_pumping_lemma.tex
appendix_quantization.tex
appendix_related_work.tex
appendix_reproducibility.tex
appendix_sampling_table.tex
appendix_scalability.tex
appendix_tcr.tex
appendix_type_consensus.tex.archived
appendix_wikievents_pilot.tex
appendix_zs_crossmodel.tex
case_study_kappa_dr.tex
checklist.tex
discussion_paragraphs.tex
discussion_paragraphs_cf83d1.tex
error_analysis_cases.json
fig1_framework.tex
figures
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
new_citations.bib
ontocodec_paper_r10_final.pdf
ontocodec_paper_r9_final.pdf
p3_case_studies.tex
p3_case_studies_861a0d.tex
paper_tables_draft.tex
r12_fallback_cascade_text.txt
relwork_new_entries.bib
section1_introduction_draft.tex
section2_background.tex
section3_method_draft.tex
section3_violation_landscape.tex
section4_composition_draft.tex
section5_crossmodel_draft.tex
section5_docred_draft.tex
section5_docred_draft_9b84f1.tex
section5_runtime.tex
section5_scierc_draft.tex
section5_scierc_draft_4796e8.tex
section5_wikievents_draft.tex
section6_related_work.tex
section6_relwork_additions.tex
section6_relwork_outline.tex
section7_conclusion_550cbf_DEPRECATED.tex
section7_conclusion_DEPRECATED.tex
section7_conclusion_compressed.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T10:30:22.448162+00:00_

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
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T10:30:22.448372+00:00_

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
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_wikievents_draft}
56	\input{section5_runtime}
57	
58	% === §6 Related Work ===
59	\input{section6_related_work}
60	
61	% === §7 Discussion and Conclusion ===
62	\section{Discussion and Conclusion}
63	\label{sec:discussion}
64	\input{section7_conclusion_compressed}
65	
66	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
67	\clearpage
68	\section*{Limitations}
69	
70	\paragraph{Constraint scope.}
71	CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impa
…[truncated 4686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T10:30:22.448572+00:00_

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
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T10:30:22.448839+00:00_

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
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs
…[truncated 7290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T10:30:22.449057+00:00_

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
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T10:30:22.449251+00:00_

1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the scale-dependent layer interaction (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
13	
14	\paragraph{Grammar-First Fallback.}
15	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
16	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
17	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$, with schema mean $\bar{\kappa}$.
23	Across WikiEvents ($\bar{\kappa}{=}0.029$), SciERC
…[truncated 1621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T10:30:22.449409+00:00_

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
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T10:30:22.449554+00:00_

1	% Section 5 — DocRED Results (compressed; full ablation in Appendix)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	
5	\subsection{Cross-Dataset Validation on DocRED}
6	\label{sec:docred-results}
7	
8	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
9	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.50\,pp ($p < 0.001$).
10	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
11	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) via \textit{latent violation surfacing}: grammar forces OOV$\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the empirical enabling dependency.
12	Fine-tuning resolves residual DR entirely (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T10:30:22.449768+00:00_

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
  "session": "worker_audit_main-tables-verification_20260523T102235",
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

_source line 12 · 2026-05-23T10:30:22.449919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T10:30:22.450066+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "limit": "0",
  "fields": "['exp_id', 'status', 'metrics', 'conclusion']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "limit": "0",
    "fields": "['exp_id', 'status', 'metrics', 'conclusion']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T10:30:22.450567+00:00_

Error: result (72,312 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T10:30:22.450791+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": "{'exp_id': 'phase2_scierc_unconstrained'}",
  "fields": "['exp_id', 'metrics', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "filters": "{'exp_id': 'phase2_scierc_unconstrained'}",
    "fields": "['exp_id', 'metrics', 'status']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T10:30:22.450956+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5254}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T10:30:22.451085+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": "{'exp_id': 'phase2_scierc_grammar_only'}",
  "fields": "['exp_id', 'metrics', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "filters": "{'exp_id': 'phase2_scierc_grammar_only'}",
    "fields": "['exp_id', 'metrics', 'status']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T10:30:22.451214+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4833}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T10:30:22.451334+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": "{'exp_id': 'phase2_scierc_semantic_only'}",
  "fields": "['exp_id', 'metrics', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "filters": "{'exp_id': 'phase2_scierc_semantic_only'}",
    "fields": "['exp_id', 'metrics', 'status']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T10:30:22.451530+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.455}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T10:30:22.451725+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": "{'exp_id': 'phase2_scierc_full_s1'}",
  "fields": "['exp_id', 'metrics', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "filters": "{'exp_id': 'phase2_scierc_full_s1'}",
    "fields": "['exp_id', 'metrics', 'status']"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T10:30:22.451951+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": "{'exp_id': 'phase2_scierc_full_s2'}",
  "fields": "['exp_id', 'metrics', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "schema_semantic_constrained_ie",
    "filters": "{'exp_id': 'phase2_scierc_full_s2'}",
    "fields": "['exp_id', 'metrics', 'status']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T10:30:22.452152+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4664}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T10:30:22.452361+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5173}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T10:30:22.452577+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\nfor eid in exps:\n    print(eid)\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\nfor eid in exps:\n    print(eid)\n\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T10:30:22.452841+00:00_

eval_70b_lora_docred_200_full_s2
sf2_qwen_int4_docred_s1
sf2_llama_int4_docred_s1
sf2_70b_prompt_sensitivity
sf2_llama_int4_scierc_s1
sf2_qwen_int4_scierc_s1
sf2_gollie_scierc_violation
eval_70b_zs_docred_200_full_s1
eval_70b_lora_docred_200_grammar_only
eval_70b_lora_docred_200_semantic_only
eval_70b_zs_docred_200_unconstrained
eval_70b_zs_docred_200_grammar_only
eval_70b_zs_docred_200_semantic_only
eval_70b_lora_docred_200_beam4_s1
eval_70b_lora_scierc_grammar_only
eval_70b_zs_scierc_unconstrained
eval_70b_lora_scierc_full_s2
eval_70b_lora_scierc_semantic_only
entity_order_ablation_qwen_scierc
eval_70b_zs_scierc_semantic_only
eval_70b_zs_scierc_grammar_only
eval_70b_lora_scierc_beam4_s1
tcr_beam4_llama_scierc
tcr_beam4_qwen_scierc
vllm_guided_json_scierc_zs
eval_70b_lora_docred_200_s1_constrained
d066_beam_sweep
w8_llama_docred_ft_grammar_only
w8_llama_docred_ft_semantic_only
w8_qwen_docred_ft_semantic_only
r16_trie_qwen_ft_scierc
r16_trie_llama_ft_scierc
eval_70b_lora_docred_200_unconstrained
eval_70b_lora_scierc_s1_constrained
eval_70b_lora_scierc_unconstrained
r16_70b_docred_zs_s1
d066_sweep_llama_beam8_unc
d066_sweep_llama_beam2_s1
d066_sweep_llama_docred_beam4_s1
r16_70b_lora_scierc_eval
r16_70b_lora_docred
r16_70b_lora_scierc
r16_70b_scierc_zs_s1
r14_qwen_docred_beam4_998
r16_trie_llama_zs_scierc
r16_trie_qwen_zs_scierc
r14_llama_docred_beam4_998
d066_sweep_llama_scierc_beam8_s1_551
d066_sweep_llama_scierc_beam4_s1_551
d066_sweep_llama_docred_beam4_unc
d066_sweep_llama_docred_beam1_s1
d066_sweep_llama_beam8_s1
d065_qwen_greedy_4096_r2
d066_sweep_llama_scierc_beam2_s1_551
d066_sweep_llama_scierc_beam1_unc
d066_sweep_llama_docred_beam1_unc
d066_sweep_21461_gpu1
w5_llama_docred_lora_constrained_eval
d066_sweep_16980_gpu1
d065_qwen_greedy_4096
d066_docred_beam_sweep
d067_seed_variance
d068_constraint_guided_beam_pilot
d064_docred_full_beam
d065_tcr_full
d065_tcr_pilot
d063_gollie_violation_rate
d062_full_ft_scierc
d062_beam_latency
d062_ontology_scalability
d062
…[truncated 2602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T10:30:22.453117+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Table 1 experiments\ntable1_ids = [\n    'phase2_scierc_unconstrained',\n    'phase2_scierc_grammar_only', \n    'phase2_scierc_semantic_only',\n    'phase2_scierc_full_s1',\n    'phase2_scierc_full_s2',\n    'vllm_guided_json_scierc_zs',\n]\n\n# Table 2 experiments  \ntable2_ids = [\n    'w5_lora_scierc_unconstrained_eval',\n    'w5_lora_scierc_constrained_eval',\n    'w5_qwen_docred_lora_unconstrained_eval',\n    'w5_qwen_docred_lora_constrained_eval',\n    'w5_llama_lora_scierc_unconstrained_eval',\n    'w5_llama_lora_scierc_constrained_eval',\n    'w5_llama_docred_lora_unconstrained_eval',\n    'w5_llama_docred_lora_constrained_eval',\n]\n\nprint('=== TABLE 1 EXPERIMENTS ===')\nfor eid in table1_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f'\\n--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\", {}), indent=4)}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")[:200]}')\n    else:\n        print(f'\\n--- {eid} --- NOT FOUND')\n\nprint('\\n\\n=== TABLE 2 EXPERIMENTS ===')\nfor eid in table2_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f'\\n--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\", {}), indent=4)}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")[:200]}')\n    else:\n        print(f'\\n--- {eid} --- NOT FOUND')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Table 1 experiments\ntable1_ids = [\n    'phase2_scierc_unconstrained',\n    'phase2_scierc_grammar_only', \n    'phase2_scierc_semantic_only',\n    'phase2_scierc_full_s1',\n    'phase2_scierc_full_s2',\n    'vllm_guided_json_scierc_zs',\n]\n\n# Table 2 experiments  \ntable2_ids = [\n    'w5_lora_scierc_unconstrained_eval',\n    'w5_lora_scierc_constrained_eval',\n    'w5_qwen_docred_lora_unconstrained_eval',\n    'w5_qwen_docred_lora_constrained_eval',\n    'w5_llama_lora_scierc_unconstrained_eval',\n    'w5_llama_lora_scierc_constrained_eval',\n    'w5_llama_docred_lora_unconstrained_eval',\n    'w5_llama_docred_lora_constrained_eval',\n]\n\nprint('=== TABLE 1 EXPERIMENTS ===')\nfor eid in table1_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f'\\n--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\", {}), indent=4)}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")[:200]}')\n    else:\n        print(f'\\n--- {eid} --- NOT FOUND')\n\nprint('\\n\\n=== TABLE 2 EXPERIMENTS ===')\nfor eid in table2_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f'\\n--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\", {}), indent=4)}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")[:200]}')\n    else:\n        print(f'\\n--- {eid} --- NOT FOUND')\n\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T10:30:22.453376+00:00_

=== TABLE 1 EXPERIMENTS ===

--- phase2_scierc_unconstrained ---
  status: DONE
  metrics: {
    "json_parse_rate": 1,
    "entity_f1": 0.3101,
    "entity_precision": 0.2605,
    "entity_recall": 0.3831,
    "relation_f1": 0.0823,
    "relation_precision": 0.0644,
    "relation_recall": 0.114,
    "entity_type_violation_rate": 0.004,
    "relation_vocabulary_violation_rate": 0.0139,
    "domain_range_violation_rate": 0.1537,
    "cross_field_consistency_violation_rate": 0.0008,
    "total_triples": 1724,
    "total_entities": 2474,
    "total_samples": 551,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- phase2_scierc_grammar_only ---
  status: DONE
  metrics: {
    "total_samples": 551,
    "total_triples": 1725,
    "total_entities": 2474,
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0,
    "relation_vocabulary_violation_rate": 0,
    "domain_range_violation_rate": 0.1484,
    "cross_field_consistency_violation_rate": 0.0008,
    "entity_f1": 0.3098,
    "entity_precision": 0.2598,
    "entity_recall": 0.3837,
    "relation_f1": 0.0823,
    "relation_precision": 0.0643,
    "relation_recall": 0.114,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- phase2_scierc_semantic_only ---
  status: DONE
  metrics: {
    "total_samples": 551,
    "total_triples": 1726,
    "total_entities": 2474,
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0.004,
    "relation_vocabulary_violation_rate": 0.0151,
    "domain_range_violation_rate": 0.1165,
    "cross_field_consistency_violation_rate": 0.0271,
    "entity_f1": 0.3101,
    "entity_precision": 0.2605,
    "entity_recall": 0.3831,
    "relation_f1": 0.0815,
    "relation_precision": 0.0637,
    "relation_recall": 0.1129,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- phase2_scierc_full_s1 ---
  status: DONE
  metrics: {
    "total_samples": 551,

…[truncated 6861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T10:30:22.453609+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Look for any DocRED FT experiments\nfor eid in sorted(exps.keys()):\n    if 'docred' in eid.lower() and ('lora' in eid.lower() or 'ft' in eid.lower() or 'w5' in eid.lower() or 'w8' in eid.lower()):\n        e = exps[eid]\n        print(f'--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        m = e.get('metrics', {})\n        # Print all metric keys\n        for k in sorted(m.keys()):\n            print(f'  {k}: {m[k]}')\n        print()\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Look for any DocRED FT experiments\nfor eid in sorted(exps.keys()):\n    if 'docred' in eid.lower() and ('lora' in eid.lower() or 'ft' in eid.lower() or 'w5' in eid.lower() or 'w8' in eid.lower()):\n        e = exps[eid]\n        print(f'--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        m = e.get('metrics', {})\n        # Print all metric keys\n        for k in sorted(m.keys()):\n            print(f'  {k}: {m[k]}')\n        print()\n\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T10:30:22.453842+00:00_

--- eval_70b_lora_docred_200_beam4_s1 ---
  status: DONE
  CF%: 0
  DR%: 0
  E-F1: 85.57
  E-P: 85.45
  E-R: 85.68
  ET%: 0
  R-F1: 48.14
  R-P: 44.24
  R-R: 52.79
  RV%: 0
  entities_pred: 3790
  parse_fail: 1/200 (0.5%)
  relations_pred: 3030

--- eval_70b_lora_docred_200_full_s2 ---
  status: DONE
  CF_count: 13
  CF_pct: 0.34
  DR_pct: 0
  ET_pct: 0
  E_F1: 84.96
  E_P: 84.6
  E_R: 85.34
  RV_pct: 0
  R_F1: 36.45
  R_P: 31.25
  R_R: 43.72
  entity_fn: 553
  entity_fp: 586
  entity_tp: 3218
  parse_fail_pct: 0
  pred_entities: 3819
  pred_relations: 3546
  relation_fn: 1421
  relation_fp: 2429
  relation_tp: 1104

--- eval_70b_lora_docred_200_grammar_only ---
  status: DONE
  CF_pct: 0.06
  DR_pct: 0.38
  ET_pct: 0
  E_F1: 80.13
  E_P: 85.16
  E_R: 75.66
  RV_pct: 0
  R_F1: 43.96
  R_P: 39.78
  R_R: 49.11
  entities_pred: 3362
  parse_fail_pct: 10.5
  relations_pred: 3154
  samples: 200

--- eval_70b_lora_docred_200_s1_constrained ---
  status: DONE
  CF_pct: 0.18
  DR_pct: 0
  ET_pct: 0
  E_F1: 79.38
  E_P: 85.24
  E_R: 74.28
  RV_pct: 0
  R_F1: 43.95
  R_P: 40.48
  R_R: 48.08
  parse_fail_pct: 12.5
  samples: 200

--- eval_70b_lora_docred_200_semantic_only ---
  status: DONE
  CF_pct: 0.21
  DR_pct: 0
  ET_pct: 0
  E_F1: 80.06
  E_P: 85.21
  E_R: 75.5
  RV_pct: 0.51
  R_F1: 43.61
  R_P: 39.44
  R_R: 48.75
  entities_pred: 3351
  parse_fail_pct: 11
  relations_pred: 3148
  samples: 200

--- eval_70b_lora_docred_200_unconstrained ---
  status: DONE
  CF_count: 2
  CF_pct: 0.06
  DR_count: 7
  DR_pct: 0.22
  ET_pct: 0
  E_F1: 80.34
  E_P: 85.13
  E_R: 76.05
  RV_count: 18
  RV_pct: 0.57
  R_F1: 43.8
  R_P: 39.6
  R_R: 48.99
  parse_fail_pct: 10
  relations: 3159
  samples: 200

--- r16_70b_lora_docred ---
  status: DONE
  epochs: 3
  eval_loss: 0.0635
  steps_completed: 1146
  token_acc: 97.94
  train_loss_end: 0.056
  train_loss_start: 0.147

--- w5_docred_sft_data_gen ---
  status: DONE
  dev_entities: 19528
  dev_relations: 12275
  dev_samples: 998
  train_enti
…[truncated 4075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T10:30:22.454153+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check for correction notes, CORRECTED tags\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    m = e.get('metrics', {})\n    c = e.get('conclusion', '')\n    # Look for CORRECTED, provenance, note, bug mentions\n    for k, v in m.items():\n        sv = str(v)\n        if any(w in sv.lower() for w in ['corrected', 'bug', 'old registry', 'provenance', 'updated']):\n            print(f'{eid}.metrics.{k}: {v}')\n    if 'note' in m:\n        print(f'{eid}.metrics.note: {m[\\\"note\\\"]}')\n    if 'provenance' in m:\n        print(f'{eid}.metrics.provenance: {m[\\\"provenance\\\"]}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check for correction notes, CORRECTED tags\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    m = e.get('metrics', {})\n    c = e.get('conclusion', '')\n    # Look for CORRECTED, provenance, note, bug mentions\n    for k, v in m.items():\n        sv = str(v)\n        if any(w in sv.lower() for w in ['corrected', 'bug', 'old registry', 'provenance', 'updated']):\n            print(f'{eid}.metrics.{k}: {v}')\n    if 'note' in m:\n        print(f'{eid}.metrics.note: {m[\\\"note\\\"]}')\n    if 'provenance' in m:\n        print(f'{eid}.metrics.provenance: {m[\\\"provenance\\\"]}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T10:30:22.454423+00:00_

d066_sweep_21461_gpu1.metrics.note: Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)
d066_sweep_llama_scierc_beam1_unc.metrics.note: INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.
d066_sweep_llama_scierc_beam2_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam2_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam4_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam4_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam8_s1_551.metrics.note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.
d066_sweep_llama_scierc_beam8_s1_551.metrics.note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.
ee_llama_wikievents_constrained.metrics.note: after retry with max_new_tokens=8192
ee_mistral_wikievents_constrained.metrics.note: grammar_only baseline (old code without semantic mask fix)
ee_qwen_wikievents_constrained.metrics.note: after retry with max_new_tokens=8192
entity_order_ablation_qwen_scierc.metrics.note: CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.
entity_order_ablation_qwen_scierc.metrics.note: CORREC
…[truncated 3421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T10:30:22.454657+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Look for w8_ft_posthoc_baseline and any posthoc_filtering experiments\nfor eid in ['w8_ft_posthoc_baseline', 'posthoc_filtering_baseline']:\n    if eid in exps:\n        e = exps[eid]\n        print(f'--- {eid} ---')\n        m = e.get('metrics', {})\n        for k in sorted(m.keys()):\n            print(f'  {k}: {m[k]}')\n        print()\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Look for w8_ft_posthoc_baseline and any posthoc_filtering experiments\nfor eid in ['w8_ft_posthoc_baseline', 'posthoc_filtering_baseline']:\n    if eid in exps:\n        e = exps[eid]\n        print(f'--- {eid} ---')\n        m = e.get('metrics', {})\n        for k in sorted(m.keys()):\n            print(f'  {k}: {m[k]}')\n        print()\n\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T10:30:22.454916+00:00_

--- w8_ft_posthoc_baseline ---
  ft_regime: {'qwen_scierc': {'R_F1_before': 43.86, 'R_F1_posthoc': 43.94, 'R_F1_constrained': 43.77, 'reject_rate_pct': 1.95, 'TP_lost': 4}, 'llama_scierc': {'R_F1_before': 45.45, 'R_F1_posthoc': 45.23, 'R_F1_constrained': 45.47, 'reject_rate_pct': 1.11, 'TP_lost': 5}, 'qwen_docred': {'R_F1_before': 40.91, 'R_F1_posthoc': 41.11, 'R_F1_constrained': 'TBD', 'reject_rate_pct': 1.03, 'TP_lost': 1}, 'llama_docred': {'R_F1_before': 43.77, 'R_F1_posthoc': 43.92, 'R_F1_constrained': 44.23, 'reject_rate_pct': 0.64, 'TP_lost': 1}}
  key_finding: ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.
  zs_regime: {'mistral_scierc': {'triples': 1584, 'reject_pct': 20.27, 'R_F1_before': 0.0376, 'R_F1_posthoc': 0.0394, 'R_F1_constrained': 0.0367, 'TP_before': 48, 'TP_after': 44, 'TP_lost': 4}, 'qwen_scierc': {'triples': 1724, 'reject_pct': 16.76, 'R_F1_before': 0.0823, 'R_F1_posthoc': 0.0863, 'R_F1_constrained': 0.0836, 'TP_before': 111, 'TP_after': 104, 'TP_lost': 7}, 'llama_scierc': {'triples': 1274, 'reject_pct': 13.89, 'R_F1_before': 0.0268, 'R_F1_posthoc': 0.0271, 'R_F1_constrained': 0.0254, 'TP_before': 30, 'TP_after': 28, 'TP_lost': 2}, 'qwen_docred': {'triples': 17497, 'reject_pct': 48.12, 'R_F1_before': 0.0774, 'R_F1_posthoc': 0.0961, 'R_F1_constrained': 0.0823, 'TP_before': 1137, 'TP_after': 1010, 'TP_lost': 127}, 'llama_docred': {'triples': 16437, 'reject_pct': 42.18, 'R_F1_before': 0.0598, 'R_F1_posthoc': 0.0744, 'R_F1_constrained': 0.0627, 'TP_before': 850, 'TP_after': 802, 'TP_lost': 48}, 'mistral_docred': {'triples': 11836, 'reject_pct': 73.73, 'R_F1_before': 0.0434, 'R_F1_posthoc': 0.0385, 'R_F1_constrained': 0.0552, 'TP_before': 518, 'TP_after': 292, 'TP_lost': 226, 'removed_RV': 4172, 'removed_ET': 3382, 'removed_DR': 1173, 'note': 'Only ZS ca
…[truncated 593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_main-tables-verification_20260523T102235",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-23T10:30:22.455296+00:00_

I now have all the data needed. Here is the complete audit report.

---

## Table 1 审计报告 (`tab:scierc-ablation`)
**SciERC 551 docs, Qwen3-8B, zero-shot**

Registry metrics use decimal (e.g., 0.1537 = 15.37%); vLLM experiment uses percent directly.

### Row: Unconstrained — `phase2_scierc_unconstrained`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 15.37 | 0.1537 → 15.37% | ✅ |
| ΔDR | --- | --- | ✅ |
| RV | 1.39 | 0.0139 → 1.39% | ✅ |
| ET | 0.40 | 0.004 → 0.40% | ✅ |
| CF | 0.08 | 0.0008 → 0.08% | ✅ |
| Tot. | 15.45 | 15.37+0.08=15.45 | ✅ |
| Rel. F1 | 8.23 | 0.0823 → 8.23% | ✅ |
| Ent. F1 | 31.01 | 0.3101 → 31.01% | ✅ |

### Row: Grammar — `phase2_scierc_grammar_only`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 14.84 | 0.1484 → 14.84% | ✅ |
| ΔDR | ↓3% | (15.37-14.84)/15.37=3.4%≈3% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 0.08 | 0.0008 → 0.08% | ✅ |
| Tot. | 14.92 | 14.84+0.08=14.92 | ✅ |
| Rel. F1 | 8.23 | 0.0823 → 8.23% | ✅ |
| Ent. F1 | 30.98 | 0.3098 → 30.98% | ✅ |

### Row: GCD-equiv.† — `vllm_guided_json_scierc_zs`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 15.26 | 15.26% | ✅ |
| ΔDR | ↓1% | (15.37-15.26)/15.37=0.7%≈1% | ✅ |
| RV | 0 | 0% | ✅ |
| ET | 0 | 0% | ✅ |
| CF | 0.04 | 0.04% | ✅ |
| Tot. | 15.30 | 15.26+0.04=15.30 | ✅ |
| Rel. F1 | 8.75 | 8.75% | ✅ |
| Ent. F1 | 30.91 | 30.91% | ✅ |

### Row: Semantic — `phase2_scierc_semantic_only`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 11.65 | 0.1165 → 11.65% | ✅ |
| ΔDR | ↓24% | (15.37-11.65)/15.37=24.2%≈24% | ✅ |
| RV | 1.51 | 0.0151 → 1.51% | ✅ |
| ET | 0.40 | 0.004 → 0.40% | ✅ |
| CF | 2.71 | 0.0271 → 2.71% | ✅ |
| Tot. | 14.36 | 11.65+2.71=14.36 | ✅ |
| Rel. F1 | 8.15 | 0.0815 → 8.15% | ✅ |
| Ent. F1 | 31.01 | 0.3101 → 31.01% | ✅ |

### Row: S1 — `phase2_scierc_full_s1`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 0.93 | 0.0093 → 0.93% | ✅ |
| ΔDR | ↓94% | (15.37-0.93)/15.37=93.9%≈94% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 9.90 | 0.099 → 9.90% | ✅ |
| Tot. | 10.83 | 0.93+9.90=10.83 | ✅ |
| Rel. F1 | 8.36 | 0.0836 → 8.36% | ✅ |
| Ent. F1 | 30.98 | 0.3098 → 30.98% | ✅ |

### Row: S2 — `phase2_scierc_full_s2`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 0.97 | 0.0097 → 0.97% | ✅ |
| ΔDR | ↓94% | (15.37-0.97)/15.37=93.7%≈94% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 8.03 | 0.0803 → 8.03% | ✅ |
| Tot. | 9.00 | 0.97+8.03=9.00 | ✅ |
| Rel. F1 | 8.03 | 0.0803 → 8.03% | ✅ |
| Ent. F1 | 31.90 | 0.319 → 31.90% | ✅ |

**Table 1 结论: 48/48 cells 全部通过 ✅**

---

## Table 2 审计报告 (`tab:composability`)
**Fine-tuning composability: LoRA × unconstrained vs. S1**

### Qwen3-8B × SciERC — `w5_lora_scierc_*_eval`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| Unconstr. DR | 1.95 | 0.0195 → 1.95% | ✅ |
| Unconstr. CF | 0 | 0 | ✅ |
| Unconstr. R-F1 | 43.86 | 0.4386 → 43.86% | ✅ |
| Unconstr. E-F1 | 67.05 | 0.6705 → 67.05% | ✅ |
| S1 DR | **0** | 0 | ✅ |
| S1 CF | 1.18 | 0.0118 → 1.18% | ✅ |
| S1 R-F1 | 43.77 | 0.4377 → 43.77% | ✅ |
| S1 E-F1 | 67.05 | 0.6705 → 67.05% | ✅ |
| S1 ΔDR | ↓100% | (1.95→0)/1.95=100% | ✅ |

**Qwen SciERC: 9/9 ✅**

### Llama 3.1-8B × SciERC — `w5_llama_lora_scierc_*_eval`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| Unconstr. DR | 1.11 | 0.0111 → 1.11% | ✅ |
| Unconstr. CF | 0 | 0 | ✅ |
| Unconstr. R-F1 | 45.45 | 0.4545 → 45.45% | ✅ |
| Unconstr. E-F1 | 67.76 | 0.6776 → 67.76% | ✅ |
| S1 DR | 0.09 | 0.0009 → 0.09% | ✅ |
| S1 CF | 0.46 | 0.0046 → 0.46% | ✅ |
| S1 R-F1 | 45.47 | 0.4547 → 45.47% | ✅ |
| S1 E-F1 | 67.76 | 0.6776 → 67.76% | ✅ |
| S1 ΔDR | ↓92% | (1.11-0.09)/1.11=91.9%≈92% | ✅ |

**Llama SciERC: 9/9 ✅**

### Qwen3-8B × DocRED — `w5_qwen_docred_lora_*_eval`

| Cell | Paper | Registry (corrected) | Verified |
|------|-------|---------------------|----------|
| Unconstr. DR | 0.56 | DR_pct=**0.76** | ❌ (diff=0.20) |
| Unconstr. CF | 0.08 | CF_pct=**0.12** | ❌ (diff=0.04) |
| Unconstr. R-F1 | 40.89 | R_F1=**40.86** | ❌ (diff=0.03) |
| Unconstr. E-F1 | 82.35 | E_F1=**82.15** | ❌ (diff=0.20) |
| S1 DR | 0.00 | DR_pct=**0.01** | ❌ (diff=0.01) |
| S1 CF | 0.22 | CF_pct=**0.41** | ❌ (diff=0.19) |
| S1 R-F1 | 40.79 | R_F1=**40.56** | ❌ (diff=0.23) |
| S1 E-F1 | 81.87 | E_F1=**81.43** | ❌ (diff=0.44) |
| S1 ΔDR | ↓100% | (0.76→0.01)=**↓98.7%** | ❌ |

**Qwen DocRED: 0/9 — 全部不一致 ❌**

### Llama 3.1-8B × DocRED — `w5_llama_docred_lora_*_eval`

| Cell | Paper | Registry (corrected) | Verified |
|------|-------|---------------------|----------|
| Unconstr. DR | 0.49 | DR_pct=**0.49** | ✅ |
| Unconstr. CF | 0.08 | **无 CF 字段** | ⚠️ 无法核实 |
| Unconstr. R-F1 | 44.55 | R_F1=**43.72** | ❌ (diff=0.83) |
| Unconstr. E-F1 | 84.77 | E_F1=**83.93** | ❌ (diff=0.84) |
| S1 DR | 0.00 | dr_violation_rate=**0.21** | ❌ (diff=0.21) |
| S1 CF | 0.26 | CF_pct=**0.21** | ❌ (diff=0.05) |
| S1 R-F1 | 44.70 | relation_f1_all_set=**43.78** | ❌ (diff=0.92) |
| S1 E-F1 | 84.71 | entity_f1=**83.94** | ❌ (diff=0.77) |
| S1 ΔDR | ↓100% | (0.49→0.21)=**↓57%** | ❌ |

**Llama DocRED: 1/9 通过, 1 无法核实, 7 不一致 ❌**

---

## 根因分析

Registry 有多条修正记录表明 `violation_checker.py` 和 `unified_f1_eval.py` 存在 **parse-failure bug**，已于 2026-05-20/22 用 `eval_d064.py` 修正：

- `w8_qwen_docred_ft_semantic_only`: "Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug)"
- `w5_llama_docred_lora_constrained_eval`: "P/R corrected 2026-05-20 per Director"
- `r16_trie_*_ft_scierc`: "CORRECTED: violation_checker.py parse-failure bug fixed. Old R-F1 was inflated (gold dropped for parse failures)"

**论文 Table 2 的 DocRED 四行使用了修正前的旧值**。SciERC 行不受影响（parse fail rate = 0%）。

## 不一致汇总

| 位置 | 论文值 | 正确值 (registry) | 严重程度 |
|------|--------|-------------------|----------|
| Qwen DocRED Unc. DR | 0.56 | **0.76** | 高 |
| Qwen DocRED Unc. CF | 0.08 | **0.12** | 中 |
| Qwen DocRED Unc. R-F1 | 40.89 | **40.86** | 低 |
| Qwen DocRED Unc. E-F1 | 82.35 | **82.15** | 中 |
| Qwen DocRED S1 DR | 0.00 | **0.01** | 低 |
| Qwen DocRED S1 CF | 0.22 | **0.41** | 高 |
| Qwen DocRED S1 R-F1 | 40.79 | **40.56** | 中 |
| Qwen DocRED S1 E-F1 | 81.87 | **81.43** | 中 |
| Qwen DocRED S1 ΔDR | ↓100% | **↓98.7%** | 中 |
| Llama DocRED Unc. R-F1 | 44.55 | **43.72** | 高 |
| Llama DocRED Unc. E-F1 | 84.77 | **83.93** | 高 |
| Llama DocRED S1 DR | 0.00 | **0.21** | 高 |
| Llama DocRED S1 CF | 0.26 | **0.21** | 低 |
| Llama DocRED S1 R-F1 | 44.70 | **43.78** | 高 |
| Llama DocRED S1 E-F1 | 84.71 | **83.94** | 高 |
| Llama DocRED S1 ΔDR | ↓100% | **↓57%** | 极高 |
| Llama DocRED Unc. CF | 0.08 | **缺失** | ⚠️ |

最严重问题：Llama DocRED S1 ΔDR 从 ↓100% 降为 ↓57%，且 DR 从 0.00 变为 0.21%。这会影响论文 "fine-tuning practically eliminates DR" 的核心结论强度。

Table 2 的 DocRED 四行全部需要用 `eval_d064.py` 的修正值重写。同时需检查正文中引用这些数字的段落（至少 `\paragraph{Composability with fine-tuning.}` 中的 "DR≤0.09%" 等表述）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_main-tables-verification_20260523T102235"
}
```

</details>

---
