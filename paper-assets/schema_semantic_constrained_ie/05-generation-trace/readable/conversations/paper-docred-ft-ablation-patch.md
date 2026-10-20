# paper docred ft ablation patch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_paper_docred_ft_ablation_patch_20260516T205702.jsonl`
- **Structured JSON:** [`469bb12ccc62fe862f06.json`](../../sessions/46/469bb12ccc62fe862f06.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-16T21:02:05.876211+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T21:02:05.876806+00:00_

1	# FT-Regime Ablation: Complete Results
2	
3	Generated: 2026-05-16
4	
5	## Table 1: SciERC FT Ablation
6	
7	| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 |
8	|-------|------|-----|-----|-----|-----|------|------|
9	| Qwen3-8B | Unconstrained | 0 | 0 | 1.95 | 0 | 67.05 | 43.86 |
10	| Qwen3-8B | Grammar Only | 0 | 0 | 1.95 | 0 | 67.05 | 43.86 |
11	| Qwen3-8B | Semantic Only | 0 | 0 | 0.62 | 0.84 | 67.05 | 43.69 |
12	| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |
13	| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
14	| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
15	| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |
16	| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |
17	
18	Notes:
19	- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation
20	- Grammar layer constrains ET and RV; Semantic layer constrains DR
21	- Grammar Only = grammar constraints active, semantic off; Semantic Only = semantic constraints active, grammar off
22	- All values from registry metrics; DR% for grammar_only computed as violations/total_relations×100
23	
24	## Table 2: DocRED FT Ablation
25	
26	| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |
27	|-------|------|-----|-----|-----|-----|------|------|-------------|
28	| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |
29	| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |
30	| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |
31	| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |
32	| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |
33	| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |
34	| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |
35	| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.
…[truncated 3689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T21:02:05.877139+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/ft_ablation_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T21:02:05.877462+00:00_

1	# FT-Regime Ablation: Complete Results
2	
3	Generated: 2026-05-16 (updated: all 8 experiments complete)
4	
5	## Table 1: SciERC FT Ablation
6	
7	| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 |
8	|-------|------|-----|-----|-----|-----|------|------|
9	| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |
10	| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |
11	| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |
12	| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |
13	| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
14	| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
15	| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |
16	| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |
17	
18	Notes:
19	- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation
20	- Grammar layer constrains ET and RV; Semantic layer constrains DR
21	- Grammar Only = grammar constraints active, semantic off; Semantic Only = semantic constraints active, grammar off
22	- All values from registry metrics; DR% for grammar_only computed as violations/total_relations×100
23	
24	## Table 2: DocRED FT Ablation
25	
26	| Model | Mode | ET% | RV% | DR% | CF% | E_F1 | R_F1 | Parse Fail% |
27	|-------|------|-----|-----|-----|-----|------|------|-------------|
28	| Qwen3-8B | Unconstrained | 0 | 0.27 | 0.76 | 0.12 | 82.15 | 40.86 | 7.11 |
29	| Qwen3-8B | Grammar Only | 0 | 0 | 0.61 | 0.11 | 82.19 | 40.85 | 7.01 |
30	| Qwen3-8B | Semantic Only | 0 | 0.23 | 0.21 | 0.27 | 82.15 | 40.89 | 7.52 |
31	| Qwen3-8B | Full (G+S) | 0 | 0 | 0.01 | 0.41 | 81.43 | 40.56 | 8.52 |
32	| Llama-3.1-8B | Unconstrained | 0 | 0.15 | 0.49 | — | 83.93 | 43.72 | 2.30 |
33	| Llama-3.1-8B | Grammar Only | 0 | 0 | 0.51 | 0.12 | 84.04 | 43.77 | 2.30 |
34	| Llama-3.1-8B | Semantic Only | 0 | 0.15 | 0.30 | 0.16 | 84.02 | 43.90 | 2.40 |
35	| 
…[truncated 4985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T21:02:05.877752+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/section*draft*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/section*draft*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T21:02:05.877958+00:00_

artifacts/_project/paper/section5_scierc_draft_4796e8.tex
artifacts/_project/paper/section5_docred_draft_9b84f1.tex
artifacts/_project/paper/section5_crossmodel_draft.tex
artifacts/_project/paper/section3_method_draft.tex
artifacts/_project/paper/section5_scierc_draft.tex
artifacts/_project/paper/section4_composition_draft.tex
artifacts/_project/paper/section5_docred_draft.tex
artifacts/_project/paper/section1_introduction_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T21:02:05.878173+00:00_

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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T21:02:05.878445+00:00_

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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T21:02:05.878732+00:00_

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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T21:02:05.879043+00:00_

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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T21:02:05.879306+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper_tables_draft*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper_tables_draft*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T21:02:05.879542+00:00_

artifacts/_project/paper/paper_tables_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T21:02:05.879778+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T21:02:05.880071+00:00_

1	% =============================================================
2	% Paper Tables Draft — Schema-Semantic Constrained IE
3	% Generated from experiment registry, 2026-05-14
4	% Model: Qwen3-8B (zero-shot), all percentages to 1 d.p.
5	% =============================================================
6	
7	% ------------------------------------------------------------
8	% Table 1: SciERC 5-way Ablation
9	% ------------------------------------------------------------
10	\begin{table}[t]
11	\centering
12	\caption{Ablation study on SciERC test set (551 samples, Qwen3-8B zero-shot).
13	DR = Domain/Range violation rate, RV = Relation Vocabulary violation rate,
14	ET = Entity Type violation rate, CF = Cross-Field consistency violation rate.
15	$\downarrow$: lower is better; $\uparrow$: higher is better.
16	$\Delta$DR shows the absolute change (pp) relative to the unconstrained baseline.}
17	\label{tab:scierc-ablation}
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{l cccc cc c}
20	\toprule
21	Mode & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ & R-F1$\uparrow$ & E-F1$\uparrow$ & $\Delta$DR (pp) \\
22	\midrule
23	Unconstrained      & 15.4 & 1.4          & 0.4          & \textbf{0.1} & 8.2          & 31.0          & ---                    \\
24	Grammar-only       & 14.8 & \textbf{0.0} & \textbf{0.0} & \textbf{0.1} & 8.2          & 31.0          & $-$0.5                 \\
25	Semantic-only      & 11.7 & 1.5          & 0.4          & 2.7          & 8.2          & 31.0          & $-$3.7                 \\
26	Full (S1)          & \textbf{0.9} & \textbf{0.0} & \textbf{0.0} & 9.9  & \textbf{8.4} & 31.0          & \textbf{$-$14.4}       \\
27	Full (S2)          & 1.0  & \textbf{0.0} & \textbf{0.0} & 8.0          & 8.0          & \textbf{31.9} & $-$14.4                \\
28	\bottomrule
29	\end{tabular}%
30	}
31	\vspace{2pt}
32	{\footnotesize
33	\textit{Exp IDs:}
34	\texttt{phase2\_scierc\_unconstrained},
35	\texttt{phase2\_scierc\_grammar\_only},
36	\texttt{phas
…[truncated 3661 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T21:02:05.880313+00:00_

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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T21:02:05.880691+00:00_

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
…[truncated 9811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T21:02:05.880963+00:00_

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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T21:02:05.881240+00:00_

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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T21:02:05.881578+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/appendix*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/appendix*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T21:02:05.881818+00:00_

artifacts/_project/paper/appendix_llama_per_relation.tex
artifacts/_project/paper/appendix_prompts.tex
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/appendix_related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T21:02:05.882005+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ft.ablation|ft_ablation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ft.ablation|ft_ablation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T21:02:05.882183+00:00_

Found 3 files
artifacts/_project/paper/main.aux
artifacts/_project/paper/appendix_discussion.tex
artifacts/_project/paper/section5_scierc_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T21:02:05.882353+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ft.ablation|ft_ablation|app:ft-ablation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "output_mode": "content",
  "-C": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ft.ablation|ft_ablation|app:ft-ablation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "output_mode": "content",
    "-C": "5"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T21:02:05.882550+00:00_

212-
213-%%% Fine-Tuned Four-Way Ablation %%%
214-% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
215-
216-\paragraph{Fine-Tuned Four-Way Ablation.}
217:\label{app:ft-ablation}
218-
219:Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
220-
221-\begin{table}[t]
222-\centering
223-\small
224-\setlength{\tabcolsep}{3pt}
--
257-\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
258-DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
259-Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
260-Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
261-F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED full vs.\ unconstrained).}
262:\label{tab:ft-ablation}
263-\end{table}
264-
265-The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
266-The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
267-Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings), confirming that even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate---specifically on tight-constraint relations where the valid type-pair space is small.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T21:02:05.882788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "212",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "212",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T21:02:05.883050+00:00_

212	
213	%%% Fine-Tuned Four-Way Ablation %%%
214	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
215	
216	\paragraph{Fine-Tuned Four-Way Ablation.}
217	\label{app:ft-ablation}
218	
219	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
220	
221	\begin{table}[t]
222	\centering
223	\small
224	\setlength{\tabcolsep}{3pt}
225	\resizebox{\columnwidth}{!}{%
226	\begin{tabular}{@{}lll rrrrr rr@{}}
227	\toprule
228	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
229	\midrule
230	\multirow{8}{*}{SciERC}
231	  & \multirow{4}{*}{Qwen3-8B}
232	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
233	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
234	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
235	  & & Full S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
236	  \cmidrule(l){2-10}
237	  & \multirow{4}{*}{Llama-3.1-8B}
238	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
239	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
240	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
241	  & & Full S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
242	\midrule
243	\multirow{8}{*}{DocRED}
244	  & \multirow{4}{*}{Qwen3-8B}
245	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
246	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
247	  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
248	  & & Full S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 
…[truncated 4462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T21:02:05.883370+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
  "old_string": "| Qwen3-8B | Unconstrained | 0 | 0 | 1.95 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.95 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.62 | 0.84 | 67.05 | 43.69 |",
  "new_string": "| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
    "old_string": "| Qwen3-8B | Unconstrained | 0 | 0 | 1.95 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.95 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.62 | 0.84 | 67.05 | 43.69 |",
    "new_string": "| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |\n| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T21:02:05.883642+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T21:02:05.883884+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
  "old_string": "2. **Semantic layer provides the marginal value in FT**: The semantic constraint reduces DR violations by 68% (Qwen: 1.95→0.62%) and 41% (Llama: 1.11→0.65%) in semantic-only mode. The full system achieves near-complete DR elimination (Qwen: 0%, Llama: 0.09%), demonstrating that some DR violations require both layers cooperating.\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR (0.62% Qwen, 0.65% Llama) is eliminated only when grammar constraints co-operate with semantic constraints in full mode.",
  "new_string": "2. **Semantic layer provides the marginal value in FT**: The semantic constraint reduces DR violations by 68% (Qwen: 1.90→0.60%) and 41% (Llama: 1.11→0.65%) in semantic-only mode. The full system achieves near-complete DR elimination (Qwen: 0%, Llama: 0.09%), demonstrating that some DR violations require both layers cooperating.\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR (0.60% Qwen, 0.65% Llama) is eliminated only when grammar constraints co-operate with semantic constraints in full mode."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
    "old_string": "2. **Semantic layer provides the marginal value in FT**: The semantic constraint reduces DR violations by 68% (Qwen: 1.95→0.62%) and 41% (Llama: 1.11→0.65%) in semantic-only mode. The full system achieves near-complete DR elimination (Qwen: 0%, Llama: 0.09%), demonstrating that some DR violations require both layers cooperating.\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR (0.62% Qwen, 0.65% Llama) is eliminated only when grammar constraints co-operate with semantic constraints in full mode.",
    "new_string": "2. **Semantic layer provides the marginal value in FT**: The semantic constraint reduces DR violations by 68% (Qwen: 1.90→0.60%) and 41% (Llama: 1.11→0.65%) in semantic-only mode. The full system achieves near-complete DR elimination (Qwen: 0%, Llama: 0.09%), demonstrating that some DR violations require both layers cooperating.\n\n3. **Two layers are complementary, not redundant**: Semantic-only reduces DR substantially but not to zero. The residual DR (0.60% Qwen, 0.65% Llama) is eliminated only when grammar constraints co-operate with semantic constraints in full mode."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T21:02:05.884162+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T21:02:05.884375+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\",
  "new_string": "    & Unconstrained & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\",
    "new_string": "    & Unconstrained & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T21:02:05.884746+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T21:02:05.884990+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).",
  "new_string": "The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$68\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$69\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%).",
    "new_string": "The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\\% across all settings (SciERC: Qwen $-$68\\%, Llama $-$41\\%; DocRED: Qwen $-$72\\%, Llama $-$39\\%)."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T21:02:05.885365+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T21:02:05.885639+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\\,pp), while reducing DR from 15.37\\% to 1.95\\% (87\\% relative reduction).\n% w5_lora_scierc_unconstrained_eval: DR=0.0195, R-F1=0.4386, E-F1=0.6705\nThe residual 1.95\\% DR concentrates on tight-constraint relations: \\textsc{Evaluate-for} (13.13\\%), \\textsc{Part-of} (5.77\\%), and \\textsc{Compare} (5.00\\%) (per-relation breakdown in Appendix~\\ref{app:lora-per-relation}).\nAdding OntoCoDec eliminates the remaining DR entirely (1.95\\%\\,$\\to$\\,0\\%) with R-F1 cost of $-$0.09\\,pp (43.86\\,$\\to$\\,43.77) and unchanged E-F1 (67.05).",
  "new_string": "For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\\,pp), while reducing DR from 15.37\\% to 1.90\\% (88\\% relative reduction).\n% w5_lora_scierc_unconstrained_eval: DR=0.0190, R-F1=0.4386, E-F1=0.6705\nThe residual 1.90\\% DR concentrates on tight-constraint relations: \\textsc{Evaluate-for} (13.13\\%), \\textsc{Part-of} (5.77\\%), and \\textsc{Compare} (5.00\\%) (per-relation breakdown in Appendix~\\ref{app:lora-per-relation}).\nAdding OntoCoDec eliminates the remaining DR entirely (1.90\\%\\,$\\to$\\,0\\%) with R-F1 cost of $-$0.09\\,pp (43.86\\,$\\to$\\,43.77) and unchanged E-F1 (67.05)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\\,pp), while reducing DR from 15.37\\% to 1.95\\% (87\\% relative reduction).\n% w5_lora_scierc_unconstrained_eval: DR=0.0195, R-F1=0.4386, E-F1=0.6705\nThe residual 1.95\\% DR concentrates on tight-constraint relations: \\textsc{Evaluate-for} (13.13\\%), \\textsc{Part-of} (5.77\\%), and \\textsc{Compare} (5.00\\%) (per-relation breakdown in Appendix~\\ref{app:lora-per-relation}).\nAdding OntoCoDec eliminates the remaining DR entirely (1.95\\%\\,$\\to$\\,0\\%) with R-F1 cost of $-$0.09\\,pp (43.86\\,$\\to$\\,43.77) and unchanged E-F1 (67.05).",
    "new_string": "For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\\,pp), while reducing DR from 15.37\\% to 1.90\\% (88\\% relative reduction).\n% w5_lora_scierc_unconstrained_eval: DR=0.0190, R-F1=0.4386, E-F1=0.6705\nThe residual 1.90\\% DR concentrates on tight-constraint relations: \\textsc{Evaluate-for} (13.13\\%), \\textsc{Part-of} (5.77\\%), and \\textsc{Compare} (5.00\\%) (per-relation breakdown in Appendix~\\ref{app:lora-per-relation}).\nAdding OntoCoDec eliminates the remaining DR entirely (1.90\\%\\,$\\to$\\,0\\%) with R-F1 cost of $-$0.09\\,pp (43.86\\,$\\to$\\,43.77) and unchanged E-F1 (67.05)."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T21:02:05.886776+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T21:02:05.887039+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "On DocRED, the same pattern holds: adding S1 to fine-tuned Qwen yields DR 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%, R-F1 $-$0.30\\,pp)\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents ($+$1.4\\,pp increase, 7.1\\%\\,$\\to$\\,8.5\\%) yields $+$0.03\\,pp. We report all-set as primary.} and to Llama DR 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%, R-F1 $+$0.51\\,pp).\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nFour-way ablation (Appendix~\\ref{app:ft-ablation}) confirms: grammar is a no-op post-fine-tuning (DR change $<$0.2\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%, making it the sole effective constraint defense in fine-tuned regimes.",
  "new_string": "On DocRED (96 relation types, document-level), the four-way ablation (Table~\\ref{tab:ft-ablation}) reveals a nuanced pattern.\nUnlike SciERC, unconstrained fine-tuned models retain non-zero RV violations (Qwen 0.27\\%, Llama 0.15\\%), indicating that the larger relation vocabulary is not fully internalized through training alone; the grammar layer eliminates these (RV\\,$\\to$\\,0\\%).\nHowever, the grammar layer remains ineffective against DR: grammar-only DR is indistinguishable from unconstrained (Qwen 0.61\\% vs.\\ 0.76\\%, Llama 0.51\\% vs.\\ 0.49\\%; $|\\Delta| < 0.2$\\,pp).\nThe semantic layer provides the effective DR defense, reducing violations by 72\\% for Qwen (0.76\\%\\,$\\to$\\,0.21\\%) and 39\\% for Llama (0.49\\%\\,$\\to$\\,0.30\\%) in isolation.\nThe full system achieves near-complete DR elimination: Qwen 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%), Llama 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%), with R-F1 changes of $-$0.30\\,pp and $+$0.51\\,pp respectively.\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents (7.1\\%\\,$\\to$\\,8.5\\%) yields $+$0.03\\,pp. We report all-set as primary.}\nParse failure rates on DocRED are non-trivial (7--8.5\\%) due to document length but do not differentially affect constraint modes: excluding failed documents, $\\Delta$R-F1 is within $\\pm$0.1\\,pp across all configurations.\n% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nThe four-way ablation consistently shows across all four model$\\times$dataset settings (Appendix~\\ref{app:ft-ablation}): grammar is a no-op for DR post-fine-tuning ($|\\Delta\\text{DR}| < 0.2$\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%; and full constraint enforcement drives DR to near-zero while preserving R-F1."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "On DocRED, the same pattern holds: adding S1 to fine-tuned Qwen yields DR 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%, R-F1 $-$0.30\\,pp)\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents ($+$1.4\\,pp increase, 7.1\\%\\,$\\to$\\,8.5\\%) yields $+$0.03\\,pp. We report all-set as primary.} and to Llama DR 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%, R-F1 $+$0.51\\,pp).\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nFour-way ablation (Appendix~\\ref{app:ft-ablation}) confirms: grammar is a no-op post-fine-tuning (DR change $<$0.2\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%, making it the sole effective constraint defense in fine-tuned regimes.",
    "new_string": "On DocRED (96 relation types, document-level), the four-way ablation (Table~\\ref{tab:ft-ablation}) reveals a nuanced pattern.\nUnlike SciERC, unconstrained fine-tuned models retain non-zero RV violations (Qwen 0.27\\%, Llama 0.15\\%), indicating that the larger relation vocabulary is not fully internalized through training alone; the grammar layer eliminates these (RV\\,$\\to$\\,0\\%).\nHowever, the grammar layer remains ineffective against DR: grammar-only DR is indistinguishable from unconstrained (Qwen 0.61\\% vs.\\ 0.76\\%, Llama 0.51\\% vs.\\ 0.49\\%; $|\\Delta| < 0.2$\\,pp).\nThe semantic layer provides the effective DR defense, reducing violations by 72\\% for Qwen (0.76\\%\\,$\\to$\\,0.21\\%) and 39\\% for Llama (0.49\\%\\,$\\to$\\,0.30\\%) in isolation.\nThe full system achieves near-complete DR elimination: Qwen 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%), Llama 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%), with R-F1 changes of $-$0.30\\,pp and $+$0.51\\,pp respectively.\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents (7.1\\%\\,$\\to$\\,8.5\\%) yields $+$0.03\\,pp. We report all-set as primary.}\nParse failure rates on DocRED are non-trivial (7--8.5\\%) due to document length but do not differentially affect constraint modes: excluding failed documents, $\\Delta$R-F1 is within $\\pm$0.1\\,pp across all configurations.\n% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nThe four-way ablation consistently shows across all four model$\\times$dataset settings (Appendix~\\ref{app:ft-ablation}): grammar is a no-op for DR post-fine-tuning ($|\\Delta\\text{DR}| < 0.2$\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%; and full constraint enforcement drives DR to near-zero while preserving R-F1."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T21:02:05.887293+00:00_

&lt;tool_use_error>String to replace not found in file.
String: On DocRED, the same pattern holds: adding S1 to fine-tuned Qwen yields DR 0.76\%\,$\to$\,0.01\% ($-$98.7\%, R-F1 $-$0.30\,pp)\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\,pp (40.86\,$\to$\,40.56); excluding parse-failure documents ($+$1.4\,pp increase, 7.1\%\,$\to$\,8.5\%) yields $+$0.03\,pp. We report all-set as primary.} and to Llama DR 0.49\%\,$\to$\,0.20\% ($-$59.2\%, R-F1 $+$0.51\,pp).

Across both models and both datasets, fine-tuned + S1 yields DR\,$\leq$\,0.20\% with R-F1 change within $\pm$0.6\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.
Four-way ablation (Appendix~\ref{app:ft-ablation}) confirms: grammar is a no-op post-fine-tuning (DR change $<$0.2\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\%, making it the sole effective constraint defense in fine-tuned regimes.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T21:02:05.887527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": "145",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "offset": "145",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T21:02:05.887758+00:00_

145	% w5_llama_lora_scierc_constrained_eval: DR=0.0009, R-F1=0.4547, E-F1=0.6776, CF=0.0046
146	
147	On DocRED, the same pattern holds: adding S1 to fine-tuned Qwen yields DR 0.76\%\,$\to$\,0.01\% ($-$98.7\%, R-F1 $-$0.30\,pp)\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\,pp (40.86\,$\to$\,40.56); excluding parse-failure documents ($+$1.4\,pp increase, 7.1\%\,$\to$\,8.5\%) yields $+$0.03\,pp. We report all-set as primary.} and to Llama DR 0.49\%\,$\to$\,0.20\% ($-$59.2\%, R-F1 $+$0.51\,pp).
148	% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23
149	
150	Across both models and both datasets, fine-tuned + S1 yields DR\,$\leq$\,0.20\% with R-F1 change within $\pm$0.6\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.
151	Four-way ablation (Appendix~\ref{app:ft-ablation}) confirms: grammar is a no-op post-fine-tuning (DR change $<$0.2\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\%, making it the sole effective constraint defense in fine-tuned regimes.
152	
153	Two secondary observations support this interpretation.
154	First, CF interference drops substantially under fine-tuning for both models: Qwen from $+$9.82\,pp to $+$1.18\,pp, Llama from $+$6.32\,pp to $+$0.46\,pp,
155	% Qwen: ZS CF delta = 9.90-0.08 = 9.82pp, FT CF delta = 1.18-0 = 1.18pp
156	% Llama: ZS CF delta = 6.56-0.24 = 6.32pp, FT CF delta = 0.46-0 = 0.46pp
157	because fine-tuned per-slot type predictions are more consistent with the entity registry;
158	for Qwen, the residual 1.18\% traces to \textsc{Generic}$\leftrightarrow$X schema-level ambiguity (Appendix~\ref{app:cf-distribution}) rather than enforcement failure.
159	Second, in the zero-shot setting, S1 R-F1 impact is negligible for both models (Qwen $+$0.13\,pp, Llama $-$0.14\,pp),

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T21:02:05.887996+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "On DocRED, the same pattern holds: adding S1 to fine-tuned Qwen yields DR 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%, R-F1 $-$0.30\\,pp)\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents ($+$1.4\\,pp increase, 7.1\\%\\,$\\to$\\,8.5\\%) yields $+$0.03\\,pp. We report all-set as primary.} and to Llama DR 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%, R-F1 $+$0.51\\,pp).\n% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nFour-way ablation (Appendix~\\ref{app:ft-ablation}) confirms: grammar is a no-op post-fine-tuning (DR change $<$0.2\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%, making it the sole effective constraint defense in fine-tuned regimes.",
  "new_string": "On DocRED (96 relation types, document-level), the four-way ablation (Table~\\ref{tab:ft-ablation}) reveals a nuanced pattern.\nUnlike SciERC, unconstrained fine-tuned models retain non-zero RV violations (Qwen 0.27\\%, Llama 0.15\\%), indicating that the larger relation vocabulary is not fully internalized through training alone; the grammar layer eliminates these (RV\\,$\\to$\\,0\\%).\nHowever, the grammar layer remains ineffective against DR: grammar-only DR is indistinguishable from unconstrained (Qwen 0.61\\% vs.\\ 0.76\\%, Llama 0.51\\% vs.\\ 0.49\\%; $|\\Delta| < 0.2$\\,pp).\nThe semantic layer provides the effective DR defense, reducing violations by 72\\% for Qwen (0.76\\%\\,$\\to$\\,0.21\\%) and 39\\% for Llama (0.49\\%\\,$\\to$\\,0.30\\%) in isolation.\nThe full system achieves near-complete DR elimination: Qwen 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%), Llama 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%), with R-F1 changes of $-$0.30\\,pp and $+$0.51\\,pp respectively.\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents (7.1\\%\\,$\\to$\\,8.5\\%) yields $\\Delta$R-F1 $+$0.03\\,pp. We report all-set as primary.}\nParse failure rates on DocRED are non-trivial (7--8.5\\%) due to document length but do not differentially affect constraint modes: excluding failed documents, $\\Delta$R-F1 is within $\\pm$0.1\\,pp across all configurations.\n% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nThe four-way ablation consistently shows across all four model$\\times$dataset settings (Appendix~\\ref{app:ft-ablation}): grammar is a no-op for DR post-fine-tuning ($|\\Delta\\text{DR}| < 0.2$\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%; and full constraint enforcement drives DR to near-zero while preserving R-F1."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "On DocRED, the same pattern holds: adding S1 to fine-tuned Qwen yields DR 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%, R-F1 $-$0.30\\,pp)\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents ($+$1.4\\,pp increase, 7.1\\%\\,$\\to$\\,8.5\\%) yields $+$0.03\\,pp. We report all-set as primary.} and to Llama DR 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%, R-F1 $+$0.51\\,pp).\n% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nFour-way ablation (Appendix~\\ref{app:ft-ablation}) confirms: grammar is a no-op post-fine-tuning (DR change $<$0.2\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%, making it the sole effective constraint defense in fine-tuned regimes.",
    "new_string": "On DocRED (96 relation types, document-level), the four-way ablation (Table~\\ref{tab:ft-ablation}) reveals a nuanced pattern.\nUnlike SciERC, unconstrained fine-tuned models retain non-zero RV violations (Qwen 0.27\\%, Llama 0.15\\%), indicating that the larger relation vocabulary is not fully internalized through training alone; the grammar layer eliminates these (RV\\,$\\to$\\,0\\%).\nHowever, the grammar layer remains ineffective against DR: grammar-only DR is indistinguishable from unconstrained (Qwen 0.61\\% vs.\\ 0.76\\%, Llama 0.51\\% vs.\\ 0.49\\%; $|\\Delta| < 0.2$\\,pp).\nThe semantic layer provides the effective DR defense, reducing violations by 72\\% for Qwen (0.76\\%\\,$\\to$\\,0.21\\%) and 39\\% for Llama (0.49\\%\\,$\\to$\\,0.30\\%) in isolation.\nThe full system achieves near-complete DR elimination: Qwen 0.76\\%\\,$\\to$\\,0.01\\% ($-$98.7\\%), Llama 0.49\\%\\,$\\to$\\,0.20\\% ($-$59.2\\%), with R-F1 changes of $-$0.30\\,pp and $+$0.51\\,pp respectively.\\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\\,pp (40.86\\,$\\to$\\,40.56); excluding parse-failure documents (7.1\\%\\,$\\to$\\,8.5\\%) yields $\\Delta$R-F1 $+$0.03\\,pp. We report all-set as primary.}\nParse failure rates on DocRED are non-trivial (7--8.5\\%) due to document length but do not differentially affect constraint modes: excluding failed documents, $\\Delta$R-F1 is within $\\pm$0.1\\,pp across all configurations.\n% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23\n\nAcross both models and both datasets, fine-tuned + S1 yields DR\\,$\\leq$\\,0.20\\% with R-F1 change within $\\pm$0.6\\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.\nThe four-way ablation consistently shows across all four model$\\times$dataset settings (Appendix~\\ref{app:ft-ablation}): grammar is a no-op for DR post-fine-tuning ($|\\Delta\\text{DR}| < 0.2$\\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\\%; and full constraint enforcement drives DR to near-zero while preserving R-F1."
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T21:02:05.888338+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T21:02:05.888574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": "178",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "offset": "178",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T21:02:05.888813+00:00_

178	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
179	  & \textbf{$\Delta$DR} \\
180	\midrule
181	\multirow{4}{*}{Qwen3-8B}
182	  & \multirow{2}{*}{Zero-shot}
183	    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
184	  & & Full S1    &  0.93 & 9.90 & 8.36  & 30.98 & $\downarrow$94\% \\
185	\cmidrule(l){2-8}
186	  & \multirow{2}{*}{LoRA}
187	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T21:02:05.889011+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "old_string": "    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\",
  "new_string": "    & Unconstr.\\ &  1.90 & 0    & 43.86 & 67.05 & --- \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "old_string": "    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\",
    "new_string": "    & Unconstr.\\ &  1.90 & 0    & 43.86 & 67.05 & --- \\\\"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T21:02:05.889293+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T21:02:05.889530+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.95",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.95",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T21:02:05.889764+00:00_

artifacts/_project/paper/main.log:689:\T1/ptm/m/n/10.95 (+20) re-duc-tion). The resid-ual 1.95% DR con-cen-
artifacts/_project/paper/appendix_discussion.tex:318:  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T21:02:05.889942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "314",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "314",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T21:02:05.890129+00:00_

314	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
315	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
316	\midrule
317	\multirow{4}{*}{FT}
318	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
319	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
320	  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\
321	  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\
322	\bottomrule
323	\end{tabular}}%

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T21:02:05.890342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "offset": "293",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "offset": "293",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T21:02:05.890566+00:00_

293	% exp_ids: posthoc_*_zs, posthoc_*_ft
294	
295	\paragraph{Post-Hoc Filtering: Extended Comparison.}
296	\label{app:posthoc-extended}
297	
298	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
299	
300	\begin{table}[t]
301	\centering
302	\small
303	\setlength{\tabcolsep}{3pt}
304	\resizebox{\columnwidth}{!}{%
305	\begin{tabular}{@{}lll rrr l@{}}
306	\toprule
307	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
308	\midrule
309	\multirow{6}{*}{ZS}
310	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
311	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
312	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
313	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
314	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
315	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
316	\midrule
317	\multirow{4}{*}{FT}
318	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
319	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
320	  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\
321	  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\
322	\bottomrule
323	\end{tabular}}%
324	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
325	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
326	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
327	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T21:02:05.890887+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
  "old_string": "  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\",
  "new_string": "  & Qwen    & SciERC & 1.90 & 43.94 & 43.77 & ph \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex",
    "old_string": "  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\\\",
    "new_string": "  & Qwen    & SciERC & 1.90 & 43.94 & 43.77 & ph \\\\"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T21:02:05.891247+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T21:02:05.891514+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.95",
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
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.95",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T21:02:05.891750+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T21:02:05.891970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
  "offset": "8",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
    "offset": "8",
    "limit": "12"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T21:02:05.892179+00:00_

8	|-------|------|-----|-----|-----|-----|------|------|
9	| Qwen3-8B | Unconstrained | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |
10	| Qwen3-8B | Grammar Only | 0 | 0 | 1.90 | 0 | 67.05 | 43.86 |
11	| Qwen3-8B | Semantic Only | 0 | 0 | 0.60 | 0.84 | 67.05 | 43.69 |
12	| Qwen3-8B | Full (G+S) | 0 | 0 | 0 | 1.18 | 67.05 | 43.77 |
13	| Llama-3.1-8B | Unconstrained | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
14	| Llama-3.1-8B | Grammar Only | 0 | 0 | 1.11 | 0 | 67.76 | 45.45 |
15	| Llama-3.1-8B | Semantic Only | 0 | 0 | 0.65 | 0.11 | 67.76 | 45.47 |
16	| Llama-3.1-8B | Full (G+S) | 0 | 0 | 0.09 | 0.46 | 67.76 | 45.47 |
17	
18	Notes:
19	- ET = Entity Type violation, RV = Relation Vocabulary violation, DR = Domain-Range violation, CF = Cross-Field consistency violation

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T21:02:05.892398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "offset": "135",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
    "offset": "135",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T21:02:05.892659+00:00_

135	For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\,pp), while reducing DR from 15.37\% to 1.90\% (88\% relative reduction).
136	% w5_lora_scierc_unconstrained_eval: DR=0.0190, R-F1=0.4386, E-F1=0.6705
137	The residual 1.90\% DR concentrates on tight-constraint relations: \textsc{Evaluate-for} (13.13\%), \textsc{Part-of} (5.77\%), and \textsc{Compare} (5.00\%) (per-relation breakdown in Appendix~\ref{app:lora-per-relation}).
138	Adding OntoCoDec eliminates the remaining DR entirely (1.90\%\,$\to$\,0\%) with R-F1 cost of $-$0.09\,pp (43.86\,$\to$\,43.77) and unchanged E-F1 (67.05).
139	% w5_lora_scierc_constrained_eval: DR=0, R-F1=0.4377, E-F1=0.6705, CF=0.0118
140	
141	Llama-3.1-8B exhibits the same pattern.
142	Fine-tuning raises R-F1 from 2.68 to 45.45 ($+$42.77\,pp) and E-F1 from 23.56 to 67.76 ($+$44.20\,pp), while reducing DR from 13.34\% to 1.11\%.
143	% w5_llama_lora_scierc_unconstrained_eval: DR=0.0111, R-F1=0.4545, E-F1=0.6776
144	Adding OntoCoDec reduces DR by 92\% (1.11\%\,$\to$\,0.09\%) with R-F1 change of $+$0.02\,pp (45.45\,$\to$\,45.47) and unchanged E-F1 (67.76).
145	% w5_llama_lora_scierc_constrained_eval: DR=0.0009, R-F1=0.4547, E-F1=0.6776, CF=0.0046
146	
147	On DocRED (96 relation types, document-level), the four-way ablation (Table~\ref{tab:ft-ablation}) reveals a nuanced pattern.
148	Unlike SciERC, unconstrained fine-tuned models retain non-zero RV violations (Qwen 0.27\%, Llama 0.15\%), indicating that the larger relation vocabulary is not fully internalized through training alone; the grammar layer eliminates these (RV\,$\to$\,0\%).
149	However, the grammar layer remains ineffective against DR: grammar-only DR is indistinguishable from unconstrained (Qwen 0.61\% vs.\ 0.76\%, Llama 0.51\% vs.\ 0.49\%; $|\Delta| < 0.2$\,pp).
150	The semantic layer provides the effective DR defense, reducing violations by 72\% for Qwen (0.76\%\,$\to$\,0.21\%) and 39\% for Llama (0.49\%\,$\to$\
…[truncated 1546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T21:02:05.892953+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.62",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.62",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/report/ft_ablation_analysis.md",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T21:02:05.893165+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-16T21:02:05.893429+00:00_

All done. Summary of changes:

**1. `artifacts/_project/report/ft_ablation_analysis.md`** — Fixed SciERC Table 1 values:
- Qwen Unconstrained/Grammar Only DR: 1.95% → 1.90%
- Qwen Semantic Only DR: 0.62% → 0.60%
- Updated corresponding mentions in Key Findings (68% reduction text and residual DR text)

**2. `artifacts/_project/paper/section5_scierc_draft.tex`** — Two changes:
- Fixed all `1.95%` references to `1.90%` (narrative text + composability table)
- Expanded the one-line DocRED FT mention into a full paragraph covering the four-way ablation: grammar layer eliminates RV but not DR, semantic layer reduces DR 72%/39%, full system achieves near-zero DR, parse failure context

**3. `artifacts/_project/paper/appendix_discussion.tex`** — Fixed:
- FT ablation table: SciERC Qwen Unconstrained DR 1.95 → 1.90
- Narrative: Qwen SciERC semantic reduction 69% → 68%
- Post-hoc comparison table: Qwen SciERC FT Reject% 1.95 → 1.90

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_docred_ft_ablation_patch_20260516T205702"
}
```

</details>

---
