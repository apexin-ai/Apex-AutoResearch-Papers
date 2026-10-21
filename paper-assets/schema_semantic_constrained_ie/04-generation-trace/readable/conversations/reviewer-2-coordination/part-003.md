# Reviewer 2 coordination — Part 3 of 5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-2-coordination.md) · [Part 4 →](part-004.md) · [Structured JSON](../../../sessions/16/16fda77cba37e7ffdcac.json)

## Round 22

### Tool result

_source line 1017 · 2026-05-20T18:38:47.558235+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that compiles IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec guarantees levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types ($a_i \in \{
…[truncated 6860 chars]

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

_source line 1018 · 2026-05-20T18:38:47.558718+00:00_

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

_source line 1019 · 2026-05-20T18:38:47.663136+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} guarantee format validity via CFG-based token masking; GCD~\cite{geng2023gcd} applies this to IE.
8	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata, but these type environments are fully known at compile time and cover all legal programs.
9	IE differs structurally: the entity registry accumulates dynamically during generation, type assignments depend on the co-occurring relation, and the schema may not cover all valid outputs, necessitating fallback (\S\ref{sec:composition}).
10	OntoCoDec's contribution is not the type-to-mask paradigm itself, but (1)~formal decidability analysis guiding constraint layering, (2)~mechanisms for dynamic registry and incomplete coverage, and (3)~systematic validation across three IE tasks and four models.
11	
12	\paragraph{Schema-aware IE.}
13	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, and GUIDEX~\cite{guidex2025} encode ontology structure as typed code; REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} unify extraction via structured training, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
14	Code-generation approaches achieve type compliance via format constraints but produce 45\% empty outputs on zero-shot RE (vs.\ 0\% for OntoCoDec), reflecting a coverage--compliance trade-off that decoding-time enforcement avoids.
15	
16	\paragraph{Constraint enforcement in IE.}
17	\citet{roth_yih_2004} first formulated
…[truncated 1177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 1020 · 2026-05-20T18:38:54.957062+00:00_

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

_source line 1021 · 2026-05-20T18:38:54.957463+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), eliminating DR with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations at 1.54$\times$ latency.
8	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe to isolate constraint effects; R-F1 2--8 reflects absent task-specific training, not method failure.
9	The deployment-relevant evaluation is the fine-tuned setting (R-F1 40--46\%), where constraints compose with parameter optimization without degrading performance.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates asso
…[truncated 222 chars]

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

_source line 1022 · 2026-05-20T18:38:55.058108+00:00_

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

_source line 1023 · 2026-05-20T18:38:55.259709+00:00_

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
…[truncated 5714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1024 · 2026-05-20T18:38:55.310342+00:00_

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

_source line 1025 · 2026-05-20T18:38:55.763104+00:00_

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
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
56	Grammar-only $\uparrow$DR: vocabula
…[truncated 1687 chars]

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

_source line 1026 · 2026-05-20T18:38:55.763792+00:00_

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

_source line 1027 · 2026-05-20T18:38:56.316901+00:00_

1	% Section 7 — Discussion and Conclusion
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec formally compiles IE ontologies into composable token-level constraints via a decidability-guided architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.09\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	For deployment, we recommend beam search with $k{\geq}4$ as the default: it resolves the CF trade-off inherent in greedy constrained decoding, eliminating all four violation types on both datasets at 1.54$\times$ latency.
6	$\bar{\kappa}$ provides a descriptive diagnostic correlating schema restrictiveness with enforcement outcomes, with entity type confusability as the critical co-factor (Appendix~\ref{app:kappa-case-study}); together with the decidability taxonomy, it yields a principled deployment workflow.
7	Our evaluation is validated primarily on 7--8B parameter models with preliminary 70B results; scaling behavior at other model sizes remains to be confirmed.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1028 · 2026-05-20T18:38:56.317386+00:00_

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

_source line 1029 · 2026-05-20T18:38:56.368026+00:00_

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
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
17	
18	\paragraph{Constraint Tightness.}
19	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}):\footnote{For symmetric relations, $|\sigma(r)|$ counts ordered pairs; the normalization $|\mathcal{E}|^2$ remains appropriate since we evaluate on directed triples.}
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	The mean $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes schema restrictiveness; tighter constraints force more frequent fal
…[truncated 2157 chars]

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

_source line 1030 · 2026-05-20T18:39:05.402832+00:00_

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

_source line 1031 · 2026-05-20T18:39:05.504328+00:00_

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
…[truncated 1384 chars]

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

_source line 1032 · 2026-05-20T18:39:05.657879+00:00_

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

_source line 1033 · 2026-05-20T18:39:05.658446+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction}
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
42	  & Uncon
…[truncated 2297 chars]

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

_source line 1034 · 2026-05-20T18:39:05.809937+00:00_

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

_source line 1035 · 2026-05-20T18:39:05.864192+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Full constraint compilation (schema parsing + grammar build): one-time $<$0.5\,s across all tested scales (Appendix~\ref{app:scalability}).
7	Scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
8	
9	\paragraph{Beam search compatibility.}
10	\label{sec:beam-results}
11	Beam search ($k{=}4$) explores paths satisfying both layers jointly.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both models (R-F1 44--47); under zero-shot, beam reduces DR to 0\% and CF substantially (9.90\%\,$\to$\,0.53\% Qwen on SciERC; Appendix~\ref{app:beam-search}).
13	DocRED zero-shot beam evaluates on a 50-document subset (compute cost; LoRA beam uses the full 998-document set).
14	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Preliminary 70B evaluation.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on both SciERC (R-F1 $-$0.03\,pp) and DocRED (R-F1 $+$0.04\,pp), one of three configurations to eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%), partly because constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Scale reduces but does not eliminate violations.
22	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool call

_source line 1036 · 2026-05-20T18:39:05.965224+00:00_

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

_source line 1037 · 2026-05-20T18:39:06.116336+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (Eq.~\ref{eq:tightness}, \S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field sema
…[truncated 910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1038 · 2026-05-20T18:40:56.330797+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "14-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "14-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1039 · 2026-05-20T18:40:57.183767+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 609.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 369.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.6}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.8}], \"total_pages\": 33, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 852
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-20T18:42:52.208625+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的分层架构：grammar layer（CFG）保证 JSON 结构和词汇约束，semantic layer（prefix-decidable with state）通过运行时 entity registry 执行 domain/range 类型约束。在 SciERC、DocRED、WikiEvents 上对 3–4 个模型（7–70B）进行了系统评估，表明 LoRA + S1 可将 DR 违规降至 ≤0.09%，R-F1 变化在 ±0.6pp 内。论文同时引入 constraint tightness κ̄ 作为描述性指标。\n\n## Strengths\n\n**S1. 系统性的实验设计与全面的消融分析。** 五路消融（Unconstrained / Grammar / Semantic / Full S1 / Full S2）清晰分离了各层贡献；跨三个数据集（RE + EE）、四个模型、三个 tokenizer 族的验证令人信服。Bootstrap 显著性检验（B=10,000）和配对统计比较体现了严谨的实验方法论。这是我见过的 constrained decoding for IE 领域最全面的评估之一。\n\n**S2. 有 principled 的形式化分析支撑架构决策。** Proposition 1（domain/range 约束不是 CF 的）给出了两层架构的 formal justification，pumping lemma 证明（Appendix）是严格的。Enabling dependency 的概念——grammar layer 必须先保证词汇有效性，semantic layer 才能有效运作——在 Table 1 中得到了实验验证（Semantic-only 仅降 24% DR）。\n\n**S3. 工程上的完整性和可部署性。** Tokenizer-agnostic continuation masking 处理了 BPE/SentencePiece 差异；grammar-first fallback 保证了 JSON 完整性；运行时开销适中（+10–13%）；编译时间 <0.5s。框架无需修改即可从 RE 扩展到 EE（WikiEvents，245 constraints），体现了良好的泛化设计。\n\n**S4. Fine-tuning composability 是重要的实用价值。** Table 2 表明约束可以与 LoRA 组合使用而不损害 R-F1（p>0.05），将残余 DR 从 1–2% 压到 ≤0.09%。对于实际部署场景，这比零样本结果更具说服力。\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [critical] 正文超过 8 页限制。**\n- 具体位置：Page 9（行号 650–660）\n- 问题：Discussion and Conclusion 的最后约 11 行溢出到第 9 页。`\\clearpage` 在 Limitations 之前（main.tex:68），Limitations 从第 10 页开始。EMNLP 2026 (via ARR) 严格限制长文正文 ≤ 8 页。\n- 为什么影响接收：格式违规可能导致 desk reject 或被 AC 标记为不合规。\n- 建议修改方向：压缩 §7 Discussion and Conclusion（当前约 120 词）、§6 Related Work、或 §5 实验叙述中的冗余描述（如 per-relation 细节可移至 Appendix），确保正文在第 8 页底部结束。\n\n**W2 [critical] CF 代价在 Abstract 和 Introduction 中被系统性低估。**\n- 具体位置：Abstract（\"with modest cross-field (CF) costs resolvable via beam search\"）; Introduction 无 CF 提及\n- 问题：\n  - 零样本 CF：SciERC 0.08%→9.90%（+123×），DocRED 0.10%→2.57%（Table 1, 3）\n  - WikiEvents CF：15–21%（Table 5）——极高\n  - Fine-tuned CF：0→1.18%（Table 2）——虽小但非零\n  - Abstract 用 \"modest\" 描述 9.90% 的 CF 率是误导性的。WikiEvents 的 15–21% CF 更无法称为 modest。\n- 为什么影响接收：审稿人和读者依赖 Abstract/Introduction 判断方法的 trade-off profile。隐藏主要副作用降低了论文的可信度。\n- 建议修改方向：Abstract 应明确写出 CF 范围（例如 \"with CF trade-offs of up to X% under zero-shot, reduced to Y% with fine-tuning or beam search\"）。Introduction 应有一段讨论 DR↔CF trade-off。\n\n**W3 [critical] κ̄ 作为独立贡献（Contribution 2）的定位过高。**\n- 具体位置：§1 Contribution 2; §4 Eq. (3)\n- 问题：κ̄ = 1 − |σ(r)|/|E|² 本质上是约束表的归一化密度。论文自身承认 \"κ is necessary but not sufficient—entity type confusability is the critical co-factor\"（§4）。一个需要额外协变量才能有意义的描述统计量，不应作为独立 contribution 列出。\n  - κ̄ 只在两个数据集上验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842），这是两个数据点的相关性——不足以支撑 \"deployment guidance\" 的声称。\n  - κ̄ 没有预测能力：Mistral 在 SciERC（κ̄=0.333）上 DR 降幅仅 76%，而 Qwen/Llama 达 94–99%（Table 4），说明 κ̄ 无法独立预测 enforcement 效果。\n- 为什么影响接收：将简单描述统计包装为 contribution 会被审稿人视为 overclaiming。\n- 建议修改方向：将 κ̄ 降级为分析工具（analysis tool），整合入实验讨论而非单独列为 contribution。或提供更多数据集的 κ̄ 值来验证其泛化性。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W4 [warning] \"any autoregressive LM\" 声称与实际验证范围不符。**\n- 具体位置：§1（\"applies to any autoregressive LM\"）、Abstract（\"validated primarily on 7–8B parameter models\"）\n- 问题：主要实验在 7–8B 模型上完成；70B 仅有初步结果（§5.5, SciERC + DocRED 各一个模型）；无小模型（<7B）验证；无 API-only 模型验证（Limitations 承认排除 GPT-4/Claude）。\"any autoregressive LM\" 的声称未经充分验证。\n- 建议：改为 \"applies to autoregressive LMs with logit access\" 或 \"validated on 7–70B parameter models\"。\n\n**W5 [warning] DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%），论文对此差异的讨论不充分。**\n- 具体位置：Table 3, §5.2\n- 问题：论文将此归因于 κ̄ 差异（0.333 vs 0.842），但这只是 restate 了问题（κ̄ 高→fallback 多→DR 高→κ̄ 相关）。更深层的问题是：对于 tight schema（实际应用中常见），零样本约束的 DR elimination 能力有限。论文没有讨论这对方法的实用性意味着什么。\n  - 残余 DR 10.21% 意味着每 10 个 triple 仍有 1 个类型违规，这对 \"type-safe extraction\" 的目标构成挑战。\n- 建议：在正文中明确讨论 tight-schema 场景下的局限性，而非仅在 Limitations 中提及。\n\n**W6 [warning] WikiEvents 评估的局限性未充分说明。**\n- 具体位置：§5.4, Table 5\n- 问题：\n  - Fine-tuning composability 基于 20-document test set，CIs 很宽（±0.05–0.06 for trigger F1），统计功效不足。\n  - 零样本 entity F1=0（unconstrained）→12–18%（constrained）——这说明无约束时 parser 完全无法处理输出，而非约束改善了 extraction 质量。F1 提升主要来自格式修复而非语义改善。\n  - Grammar-only 行缺少 F1 数据（\"---\"），但 Table caption 没有充分解释原因。\n- 建议：承认 WikiEvents 结果是 preliminary，且 F1 提升的来源是格式合规而非 extraction 能力。\n\n**W7 [warning] \"formally compiles\" 的表述与 code generation 领域的 type-constrained decoding 技术区分不够清晰。**\n- 具体位置：Abstract、§1、§6\n- 问题：§6 第二段确实讨论了与 PICARD 和 Mündler et al. (2025) 的区别——IE 的 entity registry 是动态构建的，而代码生成的类型环境在编译时完全已知。但 \"formally compiles\" 这个术语暗示了超出实际贡献的理论深度。实际实现是：(1) 从 ontology 生成 JSON Schema + enum constraints 交给 XGrammar，(2) 构建一个 stateful logit processor 做 type masking。这更接近 \"automatic constraint generation\" 而非 PL 意义上的 \"compilation\"。\n- 建议：可以保留 \"compile\" 用于框架描述，但避免在贡献声称中过度使用 \"formally compiles\"。\n\n### Minor 问题（不影响接收）\n\n**M1.** 孤立 bib entry：`schmidt2025grammar`（在 .bib 中但未被任何 .tex 文件引用）。\n\n**M2.** 表格字体偏小：Table 1, 3, 4 使用 `\\resizebox{\\columnwidth}` 压缩了 8+ 列表格，打印时可读性可能受影响。\n\n**M3.** S1/S2 命名不够直观。第一次出现时（§3.4）应在括号内给出描述性名称，后续可以用 \"single-pass S1\" / \"two-pass S2\" 保持一致。当前正文中混用 \"S1 (joint extraction)\" 和 \"Full (S1)\"。\n\n**M4.** §4 Constraint Tightness 的脚注 1 说 \"for symmetric relations, |σ(r)| counts ordered pairs\"——这个处理选择应该在正文中讨论而非藏在脚注里，因为它影响 κ̄ 的计算。\n\n**M5.** 引用验证发现 `formattax2026` 和 `regino2025kgcurator` 在 OpenAlex 中未找到匹配（可能是极新论文），建议确认这两篇引用的完整性。\n\n## Questions（需要作者澄清）\n\n**Q1.** Grammar-first fallback 触发时，semantic layer 完全放弃约束。论文报告 fallback 在 36.6% 的 type-bearing positions 触发（§4, SciERC 零样本）。这是否意味着约三分之一的类型位置实际上没有任何类型约束？如果是，\"type-constrained extraction\" 的标题是否过度承诺？\n\n**Q2.** Table 2 显示 Llama SciERC fine-tuned DR 从 1.11% 降至 0.09%（而非 0%），但 Qwen 达到 0%。Llama 残余 0.09% 的 36 个违规分解（entity type errors 39%, schema coverage gaps 33%, model errors 28%——来自 Limitations）是否意味着约束的有效性受限于 schema coverage？如果 training data 的类型对覆盖不全（33% 的残余违规来源），这对新领域的部署有何影响？\n\n**Q3.** Beam search（k=4）在 SciERC LoRA 上消除了所有违规。但 DocRED 零样本 beam 仅在 50-document subset 上评估（§5.5）。为什么不在完整 998-document set 上运行？\"compute cost\" 是否意味着 beam search 在大规模 schema（96 relations）上不实用？\n\n**Q4.** WikiEvents 的 Grammar-only 行在 Table 5 中 F1 标记为 \"---\"（\"not applicable\"），但 grammar-only 模式应该可以生成结构化输出并计算 F1。是因为 RoV 仍高达 64–77% 导致无法可靠评估吗？这需要更清晰的解释。\n\n**Q5.** 论文声称 \"extraction tasks are robust to format constraints\" 引用 Tam et al. (2024)，但 Tam et al. 的实验是在 general NLP tasks 上而非 IE-specific tasks 上。是否有 IE-specific 的证据表明 constrained decoding 不损害 extraction reasoning？CRANE (Banerjee et al., 2025) 的发现暗示即使在结构化任务中，constrained decoding 也可能有隐性代价。\n\n## Missing References\n\n论文的 related work 覆盖总体较好。可能遗漏：\n\n1. **Fei et al. (2022)** \"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model\"——结构化生成 + IE 的早期工作。\n2. 论文未讨论 **closed-book vs open-book** 约束设置的区别：OntoCoDec 的约束表从 training data 提取，这与 formal ontology 驱动的方法有本质区别（coverage gap 问题）。\n\n## Scores\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 技术方法正确，形式化分析严格，实验设计全面；但 CF 代价被低估，κ̄ 验证不充分（仅 2 个数据点），DocRED 零样本 DR 降幅有限 |\n| Excitement | 2.5/5 | 解决了真实问题（IE 类型违规），但核心机制（logit masking at type positions + entity registry）是已有技术的自然组合；decidability analysis 形式化了直觉但未带来新 insight |\n| Reproducibility | 4/5 | 实验细节充分（prompt templates in Appendix, hyperparameters, bootstrap settings），承诺代码发布；但部分评估依赖特定 XGrammar 版本 |\n| Overall | 3.0/5 | **Findings 级别**。技术扎实，评估全面，但新颖性有限（constrained decoding + stateful masking 的组合）；κ̄ contribution 过度包装；CF 代价透明度不足；正文超页（must-fix format violation） |\n| Confidence | 4/5 | 熟悉 constrained decoding、structured generation 和 IE 领域 |\n\n### 自定义维度\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Novelty | 2.5/5 | 两层架构的 decidability justification 是新的形式化贡献，但核心机制（grammar mask ∩ semantic mask）是已有思路的工程化实现 |\n| Clarity | 3.5/5 | 方法描述清晰，实验组织良好；但 CF 代价的呈现方式（buried in tables, \"modest\" in abstract）损害了透明度 |\n\n### 一句话总结\n\n一篇技术扎实、评估全面的系统论文，但核心新颖性有限（constrained decoding for IE 的 principled engineering），且 CF 代价透明度和 κ̄ contribution 定位存在显著问题。\n",
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
    "text": "\n# Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的分层架构：grammar layer（CFG）保证 JSON 结构和词汇约束，semantic layer（prefix-decidable with state）通过运行时 entity registry 执行 domain/range 类型约束。在 SciERC、DocRED、WikiEvents 上对 3–4 个模型（7–70B）进行了系统评估，表明 LoRA + S1 可将 DR 违规降至 ≤0.09%，R-F1 变化在 ±0.6pp 内。论文同时引入 constraint tightness κ̄ 作为描述性指标。\n\n## Strengths\n\n**S1. 系统性的实验设计与全面的消融分析。** 五路消融（Unconstrained / Grammar / Semantic / Full S1 / Full S2）清晰分离了各层贡献；跨三个数据集（RE + EE）、四个模型、三个 tokenizer 族的验证令人信服。Bootstrap 显著性检验（B=10,000）和配对统计比较体现了严谨的实验方法论。这是我见过的 constrained decoding for IE 领域最全面的评估之一。\n\n**S2. 有 principled 的形式化分析支撑架构决策。** Proposition 1（domain/range 约束不是 CF 的）给出了两层架构的 formal justification，pumping lemma 证明（Appendix）是严格的。Enabling dependency 的概念——grammar layer 必须先保证词汇有效性，semantic layer 才能有效运作——在 Table 1 中得到了实验验证（Semantic-only 仅降 24% DR）。\n\n**S3. 工程上的完整性和可部署性。** Tokenizer-agnostic continuation masking 处理了 BPE/SentencePiece 差异；grammar-first fallback 保证了 JSON 完整性；运行时开销适中（+10–13%）；编译时间 <0.5s。框架无需修改即可从 RE 扩展到 EE（WikiEvents，245 constraints），体现了良好的泛化设计。\n\n**S4. Fine-tuning composability 是重要的实用价值。** Table 2 表明约束可以与 LoRA 组合使用而不损害 R-F1（p>0.05），将残余 DR 从 1–2% 压到 ≤0.09%。对于实际部署场景，这比零样本结果更具说服力。\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [critical] 正文超过 8 页限制。**\n- 具体位置：Page 9（行号 650–660）\n- 问题：Discussion and Conclusion 的最后约 11 行溢出到第 9 页。`\\clearpage` 在 Limitations 之前（main.tex:68），Limitations 从第 10 页开始。EMNLP 2026 (via ARR) 严格限制长文正文 ≤ 8 页。\n- 为什么影响接收：格式违规可能导致 desk reject 或被 AC 标记为不合规。\n- 建议修改方向：压缩 §7 Discussion and Conclusion（当前约 120 词）、§6 Related Work、或 §5 实验叙述中的冗余描述（如 per-relation 细节可移至 Appendix），确保正文在第 8 页底部结束。\n\n**W2 [critical] CF 代价在 Abstract 和 Introduction 中被系统性低估。**\n- 具体位置：Abstract（\"with modest cross-field (CF) costs resolvable via beam search\"）; Introduction 无 CF 提及\n- 问题：\n  - 零样本 CF：SciERC 0.08%→9.90%（+123×），DocRED 0.10%→2.57%（Table 1, 3）\n  - WikiEvents CF：15–21%（Table 5）——极高\n  - Fine-tuned CF：0→1.18%（Table 2）——虽小但非零\n  - Abstract 用 \"modest\" 描述 9.90% 的 CF 率是误导性的。WikiEvents 的 15–21% CF 更无法称为 modest。\n- 为什么影响接收：审稿人和读者依赖 Abstract/Introduction 判断方法的 trade-off profile。隐藏主要副作用降低了论文的可信度。\n- 建议修改方向：Abstract 应明确写出 CF 范围（例如 \"with CF trade-offs of up to X% under zero-shot, reduced to Y% with fine-tuning or beam search\"）。Introduction 应有一段讨论 DR↔CF trade-off。\n\n**W3 [critical] κ̄ 作为独立贡献（Contribution 2）的定位过高。**\n- 具体位置：§1 Contribution 2; §4 Eq. (3)\n- 问题：κ̄ = 1 − |σ(r)|/|E|² 本质上是约束表的归一化密度。论文自身承认 \"κ is necessary but not sufficient—entity type confusability is the critical co-factor\"（§4）。一个需要额外协变量才能有意义的描述统计量，不应作为独立 contribution 列出。\n  - κ̄ 只在两个数据集上验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842），这是两个数据点的相关性——不足以支撑 \"deployment guidance\" 的声称。\n  - κ̄ 没有预测能力：Mistral 在 SciERC（κ̄=0.333）上 DR 降幅仅 76%，而 Qwen/Llama 达 94–99%（Table 4），说明 κ̄ 无法独立预测 enforcement 效果。\n- 为什么影响接收：将简单描述统计包装为 contribution 会被审稿人视为 overclaiming。\n- 建议修改方向：将 κ̄ 降级为分析工具（analysis tool），整合入实验讨论而非单独列为 contribution。或提供更多数据集的 κ̄ 值来验证其泛化性。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W4 [warning] \"any autoregressive LM\" 声称与实际验证范围不符。**\n- 具体位置：§1（\"applies to any autoregressive LM\"）、Abstract（\"validated primarily on 7–8B parameter models\"）\n- 问题：主要实验在 7–8B 模型上完成；70B 仅有初步结果（§5.5, SciERC + DocRED 各一个模型）；无小模型（<7B）验证；无 API-only 模型验证（Limitations 承认排除 GPT-4/Claude）。\"any autoregressive LM\" 的声称未经充分验证。\n- 建议：改为 \"applies to autoregressive LMs with logit access\" 或 \"validated on 7–70B parameter models\"。\n\n**W5 [warning] DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%），论文对此差异的讨论不充分。**\n- 具体位置：Table 3, §5.2\n- 问题：论文将此归因于 κ̄ 差异（0.333 vs 0.842），但这只是 restate 了问题（κ̄ 高→fallback 多→DR 高→κ̄ 相关）。更深层的问题是：对于 tight schema（实际应用中常见），零样本约束的 DR elimination 能力有限。论文没有讨论这对方法的实用性意味着什么。\n  - 残余 DR 10.21% 意味着每 10 个 triple 仍有 1 个类型违规，这对 \"type-safe extraction\" 的目标构成挑战。\n- 建议：在正文中明确讨论 tight-schema 场景下的局限性，而非仅在 Limitations 中提及。\n\n**W6 [warning] WikiEvents 评估的局限性未充分说明。**\n- 具体位置：§5.4, Table 5\n- 问题：\n  - Fine-tuning composability 基于 20-document test set，CIs 很宽（±0.05–0.06 for trigger F1），统计功效不足。\n  - 零样本 entity F1=0（unconstrained）→12–18%（constrained）——这说明无约束时 parser 完全无法处理输出，而非约束改善了 extraction 质量。F1 提升主要来自格式修复而非语义改善。\n  - Grammar-only 行缺少 F1 数据（\"---\"），但 Table caption 没有充分解释原因。\n- 建议：承认 WikiEvents 结果是 preliminary，且 F1 提升的来源是格式合规而非 extraction 能力。\n\n**W7 [warning] \"formally compiles\" 的表述与 code generation 领域的 type-constrained decoding 技术区分不够清晰。**\n- 具体位置：Abstract、§1、§6\n- 问题：§6 第二段确实讨论了与 PICARD 和 Mündler et al. (2025) 的区别——IE 的 entity registry 是动态构建的，而代码生成的类型环境在编译时完全已知。但 \"formally compiles\" 这个术语暗示了超出实际贡献的理论深度。实际实现是：(1) 从 ontology 生成 JSON Schema + enum constraints 交给 XGrammar，(2) 构建一个 stateful logit processor 做 type masking。这更接近 \"automatic constraint generation\" 而非 PL 意义上的 \"compilation\"。\n- 建议：可以保留 \"compile\" 用于框架描述，但避免在贡献声称中过度使用 \"formally compiles\"。\n\n### Minor 问题（不影响接收）\n\n**M1.** 孤立 bib entry：`schmidt2025grammar`（在 .bib 中但未被任何 .tex 文件引用）。\n\n**M2.** 表格字体偏小：Table 1, 3, 4 使用 `\\resizebox{\\columnwidth}` 压缩了 8+ 列表格，打印时可读性可能受影响。\n\n**M3.** S1/S2 命名不够直观。第一次出现时（§3.4）应在括号内给出描述性名称，后续可以用 \"single-pass S1\" / \"two-pass S2\" 保持一致。当前正文中混用 \"S1 (joint extraction)\" 和 \"Full (S1)\"。\n\n**M4.** §4 Constraint Tightness 的脚注 1 说 \"for symmetric relations, |σ(r)| counts ordered pairs\"——这个处理选择应该在正文中讨论而非藏在脚注里，因为它影响 κ̄ 的计算。\n\n**M5.** 引用验证发现 `formattax2026` 和 `regino2025kgcurator` 在 OpenAlex 中未找到匹配（可能是极新论文），建议确认这两篇引用的完整性。\n\n## Questions（需要作者澄清）\n\n**Q1.** Grammar-first fallback 触发时，semantic layer 完全放弃约束。论文报告 fallback 在 36.6% 的 type-bearing positions 触发（§4, SciERC 零样本）。这是否意味着约三分之一的类型位置实际上没有任何类型约束？如果是，\"type-constrained extraction\" 的标题是否过度承诺？\n\n**Q2.** Table 2 显示 Llama SciERC fine-tuned DR 从 1.11% 降至 0.09%（而非 0%），但 Qwen 达到 0%。Llama 残余 0.09% 的 36 个违规分解（entity type errors 39%, schema coverage gaps 33%, model errors 28%——来自 Limitations）是否意味着约束的有效性受限于 schema coverage？如果 training data 的类型对覆盖不全（33% 的残余违规来源），这对新领域的部署有何影响？\n\n**Q3.** Beam search（k=4）在 SciERC LoRA 上消除了所有违规。但 DocRED 零样本 beam 仅在 50-document subset 上评估（§5.5）。为什么不在完整 998-document set 上运行？\"compute cost\" 是否意味着 beam search 在大规模 schema（96 relations）上不实用？\n\n**Q4.** WikiEvents 的 Grammar-only 行在 Table 5 中 F1 标记为 \"---\"（\"not applicable\"），但 grammar-only 模式应该可以生成结构化输出并计算 F1。是因为 RoV 仍高达 64–77% 导致无法可靠评估吗？这需要更清晰的解释。\n\n**Q5.** 论文声称 \"extraction tasks are robust to format constraints\" 引用 Tam et al. (2024)，但 Tam et al. 的实验是在 general NLP tasks 上而非 IE-specific tasks 上。是否有 IE-specific 的证据表明 constrained decoding 不损害 extraction reasoning？CRANE (Banerjee et al., 2025) 的发现暗示即使在结构化任务中，constrained decoding 也可能有隐性代价。\n\n## Missing References\n\n论文的 related work 覆盖总体较好。可能遗漏：\n\n1. **Fei et al. (2022)** \"LasUIE: Unifying Information Extraction with Latent Adaptive Structure-aware Generative Language Model\"——结构化生成 + IE 的早期工作。\n2. 论文未讨论 **closed-book vs open-book** 约束设置的区别：OntoCoDec 的约束表从 training data 提取，这与 formal ontology 驱动的方法有本质区别（coverage gap 问题）。\n\n## Scores\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 技术方法正确，形式化分析严格，实验设计全面；但 CF 代价被低估，κ̄ 验证不充分（仅 2 个数据点），DocRED 零样本 DR 降幅有限 |\n| Excitement | 2.5/5 | 解决了真实问题（IE 类型违规），但核心机制（logit masking at type positions + entity registry）是已有技术的自然组合；decidability analysis 形式化了直觉但未带来新 insight |\n| Reproducibility | 4/5 | 实验细节充分（prompt templates in Appendix, hyperparameters, bootstrap settings），承诺代码发布；但部分评估依赖特定 XGrammar 版本 |\n| Overall | 3.0/5 | **Findings 级别**。技术扎实，评估全面，但新颖性有限（constrained decoding + stateful masking 的组合）；κ̄ contribution 过度包装；CF 代价透明度不足；正文超页（must-fix format violation） |\n| Confidence | 4/5 | 熟悉 constrained decoding、structured generation 和 IE 领域 |\n\n### 自定义维度\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Novelty | 2.5/5 | 两层架构的 decidability justification 是新的形式化贡献，但核心机制（grammar mask ∩ semantic mask）是已有思路的工程化实现 |\n| Clarity | 3.5/5 | 方法描述清晰，实验组织良好；但 CF 代价的呈现方式（buried in tables, \"modest\" in abstract）损害了透明度 |\n\n### 一句话总结\n\n一篇技术扎实、评估全面的系统论文，但核心新颖性有限（constrained decoding for IE 的 principled engineering），且 CF 代价透明度和 κ̄ contribution 定位存在显著问题。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1041 · 2026-05-20T18:42:56.190840+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3982
}
```

</details>

---


### Tool call

_source line 1042 · 2026-05-20T18:43:02.653973+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
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
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1043 · 2026-05-20T18:43:02.804770+00:00_



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

_source line 1044 · 2026-05-20T18:43:06.922154+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1045 · 2026-05-20T18:43:07.073102+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 150
}
```

</details>

---


### Assistant

_source line 1046 · 2026-05-20T18:43:17.050404+00:00_

审稿意见已提交给 Review Director。

**审稿结论：Overall 3.0/5（Findings 级别）**

核心发现：
- **3 个 Must-Fix**：正文超 8 页限制（~11 行溢出到第 9 页）；Abstract/Introduction 系统性低估 CF 代价（零样本 SciERC 9.90%、WikiEvents 15–21%，用 "modest" 描述是误导）；κ̄ 作为独立 Contribution 定位过高（仅 2 个数据点的描述统计量）
- **4 个 Should-Fix**：`any autoregressive LM` 声称超出验证范围；DocRED 零样本 DR 降幅仅 45% 的讨论不充分；WikiEvents 评估统计功效不足（20-doc test set）；"formally compiles" 措辞与实际技术贡献不匹配
- **优势**：实验设计是该领域最全面的之一（5-way ablation × 3 datasets × 4 models × bootstrap）；decidability analysis 给出了 principled 的架构 justification；fine-tuning composability 有实用部署价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 23

## Round 23

4 recorded events


### User

_source line 1047 · 2026-05-20T18:46:08.822260+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿意见：

### Summary
本文提出 OntoCoDec，一个将 IE 本体编译为 token 级约束的框架。系统采用双层架构：grammar layer（EBNF + XGrammar）和 semantic layer（有状态 logits processor）。论文提出三级 decidability taxonomy，用 pumping lemma 证明 Level 2 约束非 context-free，并在 SciERC、DocRED、WikiEvents 三个数据集上用 4 个模型验证。

### Must-Fix

**W1. [critical] 缺少最直接可比的 constrained decoding baseline 对比**
BoostCD (Sakota et al., 2025) 和 IterGen (Ugare et al., 2025) 在 Related Work 中被引用但实验中完全没有对比。BoostCD 发表于 EMNLP 2025，专门做 IE constrained decoding，是最自然的 baseline。如果它们在相同 benchmark 上能达到类似效果，OntoCoDec 的增量贡献将大幅缩水。

**W2. [critical] WikiEvents EE 评估统计效力严重不足**
WikiEvents 测试集仅 20 篇文档。Contribution 3 将 WikiEvents EE 列为三大贡献之一（"systematic evaluation"），但 20 篇文档无法支撑此措辞。建议限定为 "preliminary demonstration"。

### Should-Fix

**W3. [warning] Pumping lemma 证明的形式化与实际系统存在 gap**
证明假设实体引用基于位置索引，而实际 JSON 使用实体名称（字符串引用）。在名称引用下 pumping 的破坏机制需要更明确说明。

**W4. [warning] DocRED beam search 仅用 50 文档子集评估**
关键 claim "CF is resolvable via beam search" 在 DocRED 上的证据基础仅为 5% 子集。Table 15（Appendix F）显示 DocRED beam CF 从 28.4%→21.4%，远未 "resolve"。

**W5. [warning] "Formally compiles" 措辞过度**
Grammar layer 是编译，但 semantic layer 是运行时规则解释。

**W6. [warning] 与 GoLLIE 等 schema-aware IE 系统缺乏量化对比**
读者需要知道 OntoCoDec + unconstrained LLM 与 GoLLIE 的 F1 差距。

**W7. [warning] κ̄ 部署指导的证据不足**
仅 2 个数据集，样本量极小，无法建立有意义的预测关系。

### Minor
**M1.** 主文似超 8 页（Section 7 延伸至 page 9 约 10 行）
**M2.** Table 密度极高，部分可用图表替代
**M3.** "Best-effort pair-based enforcement" 精确含义可更明确
**M4.** 1 orphan bib entry, 2 篇在 OpenAlex 未找到
**M5.** Grammar-first fallback 的极端情况（G(t)=∅）未讨论

### Scores
Soundness 3.5/5, Excitement 3/5, Overall 3.5/5 (Borderline Conference), Confidence 4/5, Reproducibility 4/5

---

请逐条回应，特别关注：
1. 你是否同意 BoostCD/IterGen 缺失对比是 must-fix？你此前未将此列为 must-fix，而是 should-fix (你的 W5)——为什么？
2. R1 对 pumping lemma 的形式化 gap 分析（位置索引 vs 名称引用）——你是否同意这是一个问题？
3. R1 给 Overall 3.5 vs 你给 3.0——分歧在哪？你认为差距的核心原因是什么？
4. R1 给 Excitement 3/5 vs 你给 2.5/5——decidability taxonomy 的理论价值是否被你低估了？

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

_source line 1048 · 2026-05-20T18:48:47.339992+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应：Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n### R1-W1: 缺少 BoostCD/IterGen baseline 对比\n\n**[AGREE]** R1-W1 正确指出了我审稿中的一个疏漏。我在 Missing References 中仅评价 related work 覆盖\"总体较好\"，但未将缺失的实验对比单独列为 weakness。\n\n具体而言：BoostCD（Sakota et al., EMNLP 2025）由 GCD 团队（Geng, Josifoski, West）开发，而 GCD 在 §5.1 和 §6 中被引用且 GCD 的原始工作评估了 SciERC，因此 BoostCD 极可能覆盖相同 benchmark。论文在 §6 中称 \"different benchmarks preclude direct comparison\"，但未提供证据支撑该断言——如果 BoostCD 确实在 SciERC 上有结果，这个回避是不可接受的。\n\n**我同意将此提升为 must-fix。** 即使 OntoCoDec 的贡献定位是 framework + formal analysis 而非 SOTA 追求，在 EMNLP 层面，与最直接的 IE constrained decoding 竞争者缺乏量化对比会让 Contribution 3（\"first systematic evaluation\"）的声称站不住脚。至少需要在 SciERC 上对比 GCD 和/或 BoostCD 的 DR 降幅和 F1。\n\n补充说明：IterGen 的对比优先级略低，因为其 backtracking 机制涉及不同的 efficiency trade-off（论文在 §6 中已定性讨论）。但 BoostCD 作为同一任务、同一范式（decoding-time constraint for IE）的直接竞争者，缺失对比是 critical 的。\n\n---\n\n### R1-W2: WikiEvents 统计效力不足\n\n**[AGREE]** 与我的 W6 一致，但我同意 R1 将其提升至更高严重度的理由。\n\n关键区分：零样本评估覆盖全部 246 篇文档，统计效力尚可；但 fine-tuning composability 仅基于 20-document test set，CIs 宽达 ±0.05–0.06（§5.4），这不是 \"systematic evaluation\" 而是 preliminary demonstration。\n\nContribution 3 明确声称 \"the framework generalizes to event extraction with 245 constraints across three tokenizer families\"——零样本泛化确实有 246 篇文档支撑，但 fine-tuning composability 的 20 篇数据量不足以支撑此力度。R1 建议将此降级为 \"preliminary demonstration\" 是合理的。\n\n---\n\n## Should-Fix 逐条回应\n\n### R1-W3: Pumping lemma 的形式化 gap（位置索引 vs 名称引用）\n\n**[AGREE]，但认为这是 presentation gap 而非 correctness gap。**\n\nR1 观察到 Proposition 1 的 proof sketch（§3, main.tex:30–33）使用位置索引模型（\"a relation referencing head $e_k$ for arbitrary $k \\leq n$\"），但实际 JSON schema（Eq. 1）使用名称字符串引用。这是一个有效的形式化缺口。\n\n然而，核心论证在名称引用模型下仍然成立：PDA 需要根据名称字符串查找对应的类型，而名称集合无界、查找是随机访问的——PDA 的 LIFO stack 同样无法支持。实质上，位置索引和名称字符串在 expressiveness 上是等价的（name→type 映射等价于 position→type 映射，因为名称空间也是无界的）。\n\n建议作者在 proof sketch 或 Appendix O 中增加一段明确说明：位置索引模型是名称引用模型的 abstraction，核心的 random-access 困难在两种模型下均成立。\n\n---\n\n### R1-W4: DocRED beam search 仅用 50 文档子集\n\n**[AGREE]，并补充更强的证据。**\n\n这与我的 Q3 一致。R1 补充了关键细节：Appendix Table 15 显示 DocRED zero-shot beam 的 CF 仅从 28.4% 降至 21.4%，远不是 \"resolve\"。\n\n论文在多处使用 \"resolvable via beam search\" 这一表述（Abstract, §5.5, §7），但这一声称的证据基础严重不对称：\n- SciERC：beam 确实消除所有违规（§5.5, full 551/998 doc）✓\n- DocRED zero-shot：仅 50 docs，CF 从 28.4%→21.4%，残余巨大 ✗\n- DocRED fine-tuned：beam on full 998 docs 消除所有违规 ✓\n\n\"Resolvable via beam search\" 的声称只在 fine-tuned 或低 κ̄ 设置下成立。对于 high-κ̄ zero-shot 场景，beam 并不 \"resolve\" CF。论文应修正此声称的适用范围。\n\n---\n\n### R1-W5: \"Formally compiles\" 措辞过度\n\n**[AGREE]** 与我的 W7 完全一致。R1 的表述更精炼：\"grammar layer 是编译，semantic layer 是运行时规则解释。\" 我补充：整个 pipeline 更准确的描述是 \"compile-time grammar generation + runtime constraint interpretation\"，而非端到端的 \"formal compilation\"。\n\n---\n\n### R1-W6: 与 GoLLIE 缺乏量化对比\n\n**[AGREE]，但优先级低于 R1-W1（BoostCD 对比）。**\n\nGoLLIE 是 training-based schema-aware IE，与 OntoCoDec（inference-time constraint）解决问题的路径不同，直接 F1 对比可能 misleading（GoLLIE 需要 schema-specific fine-tuning，OntoCoDec 不需要）。\n\n但 R1 的核心诉求合理：读者需要一个 reference point 来理解 \"7-8B model + OntoCoDec constraints\" 的 R-F1 40-46% 在领域中处于什么水平。即使不做严格对比，提供一个表格行展示 GoLLIE 或类似系统在相同数据集上的 published numbers 即可。这是 contextual information，不需要重新跑实验。\n\n---\n\n### R1-W7: κ̄ 部署指导证据不足\n\n**[AGREE]，并重申我的 W3 中更强的立场。**\n\nR1 将此定为 should-fix，我将其定为 must-fix（W3）。核心分歧在于 κ̄ 是否应该作为 Contribution 2。R1 认为证据不足但允许保留 contribution 定位；我认为仅 2 个数据点的描述统计量不应作为独立 contribution。\n\n补充论据：κ̄ 对 Mistral 的预测完全失效（SciERC κ̄=0.333 理论上应 \"near-complete DR elimination\"，但 Mistral 仅达 76%——Table 4），说明没有 confusability 这个协变量，κ̄ 的 guidance 价值极有限。两个变量、两个数据点——这是无法拟合任何有意义模型的。\n\n---\n\n## Minor 逐条回应\n\n### R1-M1: 主文超 8 页\n**[AGREE]** 与我的 W1（must-fix）一致。我将此列为 critical，R1 列为 minor。**我认为应提升为 must-fix**——EMNLP 2026 的 8 页限制是硬约束，违反可能导致 desk reject。\n\n### R1-M2: Table 密度\n**[AGREE]** 与我的 M2 一致。\n\n### R1-M3: \"Best-effort pair-based enforcement\" 含义\n**[AGREE]** 我未单独标注此点，但 R1 的观察合理。该术语在 §3.1 和 §3.3 中定义但含义跨两处分散——第一次出现时应给出完整的 inline definition。\n\n### R1-M4: Orphan bib + OpenAlex 未找到\n**[AGREE]** 与我的 M1/M5 一致。\n\n### R1-M5: G(t)=∅ 的边界情况\n**[REBUT]** 这不应是实际问题。XGrammar 的 pushdown automaton 保证在合法 JSON 生成路径上 G(t) ≠ ∅（至少有一个合法 continuation token）。G(t)=∅ 意味着 grammar 本身有 bug（dead state），这是 XGrammar 实现的问题而非 OntoCoDec 框架的问题。论文的 grammar-first fallback 已经处理了 G(t) ∩ S(t) = ∅ 的情况（§4），而 G(t)=∅ 属于 XGrammar 层的 invariant 保证。\n\n---\n\n## Director 指定的 4 个问题\n\n### Q1: BoostCD/IterGen 缺失对比——must-fix vs should-fix？\n\n**我现在同意 R1 将此列为 must-fix。**\n\n我此前未单独标注此问题的原因有二：(1) 我更关注框架和 formal analysis 层面的贡献定位问题（κ̄ overclaiming、CF 透明度），(2) 论文在 §6 中明确声称 \"different benchmarks preclude direct comparison\"，我当时接受了这一声称而未深入质疑。\n\nR1 的分析让我重新审视：BoostCD 团队的前序工作 GCD 确实在 SciERC 上评估过（论文在 Table 1 caption 中引用 GCD 作为 \"ceiling of grammar-constrained decoding\"），因此 BoostCD 极可能覆盖相同 benchmark。在此前提下，\"different benchmarks\" 的回避是不充分的，缺失对比确实是 must-fix。\n\n### Q2: Pumping lemma 形式化 gap\n\n**部分同意。** 如上 R1-W3 回应所述，这是 presentation gap 而非 correctness gap。核心论证在名称引用模型下仍成立（名称→类型的随机访问同样超出 PDA 能力），但 proof sketch 应明确说明从位置索引到名称引用的 abstraction 关系。作为 formal contribution 的一部分，这种精度的缺失值得修正，但不影响结论的 validity。\n\n### Q3: Overall 3.5 vs 3.0——分歧核心\n\n我给 3.0（Findings），R1 给 3.5（Borderline Conference）。分歧核心在三点：\n\n1. **CF 代价的权重**：我将 CF 透明度问题列为 must-fix（W2），认为 Abstract 中的 \"modest\" 误导性地低估了 9.90%–21% 的 CF 率。R1 未单独标注 CF 透明度问题。如果 CF 的呈现方式修正，论文的 overall trade-off profile 会更 honest，但也更不 appealing。\n\n2. **κ̄ contribution 的严重度**：我将 κ̄ overclaiming 列为 must-fix，R1 列为 should-fix。如果 κ̄ 从独立 contribution 降级为分析工具，论文只剩两个 contribution（framework + evaluation），对主会议而言可能不够。\n\n3. **缺失 baseline 对比的影响**：R1 将 BoostCD 缺失列为 must-fix 但仍给 3.5——这意味着 R1 认为即使加上这个 must-fix，论文的 framework contribution 仍有可能达到主会议水平。我现在加上这个 must-fix，结合 CF 透明度和 κ̄ 问题，三个 must-fix 叠加使 3.0 更合理。\n\n**总结**：如果所有 must-fix 都被妥善修正（压缩页数、增加 baseline 对比、修正 CF 叙述、降级 κ̄），论文有可能达到 3.5。但在当前状态下，3.0 更准确地反映了累积问题的严重度。\n\n### Q4: Decidability taxonomy 的理论价值——是否被我低估？\n\n**R1 的 Excitement 3/5 有一定道理，但我维持 2.5/5，理由如下：**\n\nR1 可能更看重 decidability taxonomy 的 reusability——三级分类（CF / prefix-decidable with state / non-local）可以迁移到其他 structured generation 任务（如 knowledge graph completion、SQL generation with schema constraints）。从这个角度看，taxonomy 的贡献超越了本文的 IE 场景。\n\n但我认为 taxonomy 的 insight density 有限：\n- Level 1（JSON structure = CF）是 trivially known\n- Level 2（type constraints need state）是 formally interesting 但 intuitively obvious——任何熟悉 PDA 限制的人都会预期此结果\n- Level 3（cross-entity consistency = non-local）的分析在论文中最弱——仅靠 beam search 和 post-hoc 处理，没有 formal guarantee\n\nProposition 1 的证明是正确的，但 **confirmatory**（证实预期）而非 **surprising**（揭示意外）。对于 Excitement 这个维度，confirmatory formalization 的价值低于 surprising insight。\n\n如果论文能展示 taxonomy 指导了一个非直觉的设计决策（例如，某个看似应该在 Level 2 的约束实际上是 Level 3，从而改变了架构），我会提高 Excitement 到 3/5。但当前的 taxonomy 与最终架构之间的映射过于自然——grammar layer → Level 1, semantic layer → Level 2, beam search → Level 3——没有 surprise。\n\n**我将 Excitement 从 2.5 微调至 2.75（如果允许的话），承认 formalization 有 marginal 的迁移价值，但不足以达到 3/5。**\n\n---\n\n## 更新后的综合评估\n\n交叉审稿后，我新增一个 must-fix（BoostCD baseline 缺失，原被我遗漏），其余评分维持不变：\n\n| 维度 | 原始分数 | 交叉后分数 | 变化理由 |\n|------|---------|-----------|---------|\n| Soundness | 3.5 | 3.5 | 无变化——R1 未提出影响 soundness 的新问题 |\n| Excitement | 2.5 | 2.5 | R1 对 taxonomy 的正面评价有道理，但 confirmatory formalization 的 excitement 有限 |\n| Overall | 3.0 | 3.0 | 新增 BoostCD must-fix 被 R1 的正面观点（taxonomy reusability）部分抵消 |\n| Confidence | 4 | 4 | 无变化 |\n\n**Must-Fix 汇总（4 项）**：\n1. 正文超 8 页（W1, 与 R1-M1 一致但我认为应升为 must-fix）\n2. CF 代价透明度（W2）\n3. κ̄ contribution 定位过高（W3）\n4. **[新增]** 缺少 BoostCD 等最直接 baseline 的量化对比（采纳 R1-W1）\n",
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
    "text": "\n# Reviewer 2 交叉回应：Reviewer 1 审稿意见\n\n---\n\n## Must-Fix 逐条回应\n\n### R1-W1: 缺少 BoostCD/IterGen baseline 对比\n\n**[AGREE]** R1-W1 正确指出了我审稿中的一个疏漏。我在 Missing References 中仅评价 related work 覆盖\"总体较好\"，但未将缺失的实验对比单独列为 weakness。\n\n具体而言：BoostCD（Sakota et al., EMNLP 2025）由 GCD 团队（Geng, Josifoski, West）开发，而 GCD 在 §5.1 和 §6 中被引用且 GCD 的原始工作评估了 SciERC，因此 BoostCD 极可能覆盖相同 benchmark。论文在 §6 中称 \"different benchmarks preclude direct comparison\"，但未提供证据支撑该断言——如果 BoostCD 确实在 SciERC 上有结果，这个回避是不可接受的。\n\n**我同意将此提升为 must-fix。** 即使 OntoCoDec 的贡献定位是 framework + formal analysis 而非 SOTA 追求，在 EMNLP 层面，与最直接的 IE constrained decoding 竞争者缺乏量化对比会让 Contribution 3（\"first systematic evaluation\"）的声称站不住脚。至少需要在 SciERC 上对比 GCD 和/或 BoostCD 的 DR 降幅和 F1。\n\n补充说明：IterGen 的对比优先级略低，因为其 backtracking 机制涉及不同的 efficiency trade-off（论文在 §6 中已定性讨论）。但 BoostCD 作为同一任务、同一范式（decoding-time constraint for IE）的直接竞争者，缺失对比是 critical 的。\n\n---\n\n### R1-W2: WikiEvents 统计效力不足\n\n**[AGREE]** 与我的 W6 一致，但我同意 R1 将其提升至更高严重度的理由。\n\n关键区分：零样本评估覆盖全部 246 篇文档，统计效力尚可；但 fine-tuning composability 仅基于 20-document test set，CIs 宽达 ±0.05–0.06（§5.4），这不是 \"systematic evaluation\" 而是 preliminary demonstration。\n\nContribution 3 明确声称 \"the framework generalizes to event extraction with 245 constraints across three tokenizer families\"——零样本泛化确实有 246 篇文档支撑，但 fine-tuning composability 的 20 篇数据量不足以支撑此力度。R1 建议将此降级为 \"preliminary demonstration\" 是合理的。\n\n---\n\n## Should-Fix 逐条回应\n\n### R1-W3: Pumping lemma 的形式化 gap（位置索引 vs 名称引用）\n\n**[AGREE]，但认为这是 presentation gap 而非 correctness gap。**\n\nR1 观察到 Proposition 1 的 proof sketch（§3, main.tex:30–33）使用位置索引模型（\"a relation referencing head $e_k$ for arbitrary $k \\leq n$\"），但实际 JSON schema（Eq. 1）使用名称字符串引用。这是一个有效的形式化缺口。\n\n然而，核心论证在名称引用模型下仍然成立：PDA 需要根据名称字符串查找对应的类型，而名称集合无界、查找是随机访问的——PDA 的 LIFO stack 同样无法支持。实质上，位置索引和名称字符串在 expressiveness 上是等价的（name→type 映射等价于 position→type 映射，因为名称空间也是无界的）。\n\n建议作者在 proof sketch 或 Appendix O 中增加一段明确说明：位置索引模型是名称引用模型的 abstraction，核心的 random-access 困难在两种模型下均成立。\n\n---\n\n### R1-W4: DocRED beam search 仅用 50 文档子集\n\n**[AGREE]，并补充更强的证据。**\n\n这与我的 Q3 一致。R1 补充了关键细节：Appendix Table 15 显示 DocRED zero-shot beam 的 CF 仅从 28.4% 降至 21.4%，远不是 \"resolve\"。\n\n论文在多处使用 \"resolvable via beam search\" 这一表述（Abstract, §5.5, §7），但这一声称的证据基础严重不对称：\n- SciERC：beam 确实消除所有违规（§5.5, full 551/998 doc）✓\n- DocRED zero-shot：仅 50 docs，CF 从 28.4%→21.4%，残余巨大 ✗\n- DocRED fine-tuned：beam on full 998 docs 消除所有违规 ✓\n\n\"Resolvable via beam search\" 的声称只在 fine-tuned 或低 κ̄ 设置下成立。对于 high-κ̄ zero-shot 场景，beam 并不 \"resolve\" CF。论文应修正此声称的适用范围。\n\n---\n\n### R1-W5: \"Formally compiles\" 措辞过度\n\n**[AGREE]** 与我的 W7 完全一致。R1 的表述更精炼：\"grammar layer 是编译，semantic layer 是运行时规则解释。\" 我补充：整个 pipeline 更准确的描述是 \"compile-time grammar generation + runtime constraint interpretation\"，而非端到端的 \"formal compilation\"。\n\n---\n\n### R1-W6: 与 GoLLIE 缺乏量化对比\n\n**[AGREE]，但优先级低于 R1-W1（BoostCD 对比）。**\n\nGoLLIE 是 training-based schema-aware IE，与 OntoCoDec（inference-time constraint）解决问题的路径不同，直接 F1 对比可能 misleading（GoLLIE 需要 schema-specific fine-tuning，OntoCoDec 不需要）。\n\n但 R1 的核心诉求合理：读者需要一个 reference point 来理解 \"7-8B model + OntoCoDec constraints\" 的 R-F1 40-46% 在领域中处于什么水平。即使不做严格对比，提供一个表格行展示 GoLLIE 或类似系统在相同数据集上的 published numbers 即可。这是 contextual information，不需要重新跑实验。\n\n---\n\n### R1-W7: κ̄ 部署指导证据不足\n\n**[AGREE]，并重申我的 W3 中更强的立场。**\n\nR1 将此定为 should-fix，我将其定为 must-fix（W3）。核心分歧在于 κ̄ 是否应该作为 Contribution 2。R1 认为证据不足但允许保留 contribution 定位；我认为仅 2 个数据点的描述统计量不应作为独立 contribution。\n\n补充论据：κ̄ 对 Mistral 的预测完全失效（SciERC κ̄=0.333 理论上应 \"near-complete DR elimination\"，但 Mistral 仅达 76%——Table 4），说明没有 confusability 这个协变量，κ̄ 的 guidance 价值极有限。两个变量、两个数据点——这是无法拟合任何有意义模型的。\n\n---\n\n## Minor 逐条回应\n\n### R1-M1: 主文超 8 页\n**[AGREE]** 与我的 W1（must-fix）一致。我将此列为 critical，R1 列为 minor。**我认为应提升为 must-fix**——EMNLP 2026 的 8 页限制是硬约束，违反可能导致 desk reject。\n\n### R1-M2: Table 密度\n**[AGREE]** 与我的 M2 一致。\n\n### R1-M3: \"Best-effort pair-based enforcement\" 含义\n**[AGREE]** 我未单独标注此点，但 R1 的观察合理。该术语在 §3.1 和 §3.3 中定义但含义跨两处分散——第一次出现时应给出完整的 inline definition。\n\n### R1-M4: Orphan bib + OpenAlex 未找到\n**[AGREE]** 与我的 M1/M5 一致。\n\n### R1-M5: G(t)=∅ 的边界情况\n**[REBUT]** 这不应是实际问题。XGrammar 的 pushdown automaton 保证在合法 JSON 生成路径上 G(t) ≠ ∅（至少有一个合法 continuation token）。G(t)=∅ 意味着 grammar 本身有 bug（dead state），这是 XGrammar 实现的问题而非 OntoCoDec 框架的问题。论文的 grammar-first fallback 已经处理了 G(t) ∩ S(t) = ∅ 的情况（§4），而 G(t)=∅ 属于 XGrammar 层的 invariant 保证。\n\n---\n\n## Director 指定的 4 个问题\n\n### Q1: BoostCD/IterGen 缺失对比——must-fix vs should-fix？\n\n**我现在同意 R1 将此列为 must-fix。**\n\n我此前未单独标注此问题的原因有二：(1) 我更关注框架和 formal analysis 层面的贡献定位问题（κ̄ overclaiming、CF 透明度），(2) 论文在 §6 中明确声称 \"different benchmarks preclude direct comparison\"，我当时接受了这一声称而未深入质疑。\n\nR1 的分析让我重新审视：BoostCD 团队的前序工作 GCD 确实在 SciERC 上评估过（论文在 Table 1 caption 中引用 GCD 作为 \"ceiling of grammar-constrained decoding\"），因此 BoostCD 极可能覆盖相同 benchmark。在此前提下，\"different benchmarks\" 的回避是不充分的，缺失对比确实是 must-fix。\n\n### Q2: Pumping lemma 形式化 gap\n\n**部分同意。** 如上 R1-W3 回应所述，这是 presentation gap 而非 correctness gap。核心论证在名称引用模型下仍成立（名称→类型的随机访问同样超出 PDA 能力），但 proof sketch 应明确说明从位置索引到名称引用的 abstraction 关系。作为 formal contribution 的一部分，这种精度的缺失值得修正，但不影响结论的 validity。\n\n### Q3: Overall 3.5 vs 3.0——分歧核心\n\n我给 3.0（Findings），R1 给 3.5（Borderline Conference）。分歧核心在三点：\n\n1. **CF 代价的权重**：我将 CF 透明度问题列为 must-fix（W2），认为 Abstract 中的 \"modest\" 误导性地低估了 9.90%–21% 的 CF 率。R1 未单独标注 CF 透明度问题。如果 CF 的呈现方式修正，论文的 overall trade-off profile 会更 honest，但也更不 appealing。\n\n2. **κ̄ contribution 的严重度**：我将 κ̄ overclaiming 列为 must-fix，R1 列为 should-fix。如果 κ̄ 从独立 contribution 降级为分析工具，论文只剩两个 contribution（framework + evaluation），对主会议而言可能不够。\n\n3. **缺失 baseline 对比的影响**：R1 将 BoostCD 缺失列为 must-fix 但仍给 3.5——这意味着 R1 认为即使加上这个 must-fix，论文的 framework contribution 仍有可能达到主会议水平。我现在加上这个 must-fix，结合 CF 透明度和 κ̄ 问题，三个 must-fix 叠加使 3.0 更合理。\n\n**总结**：如果所有 must-fix 都被妥善修正（压缩页数、增加 baseline 对比、修正 CF 叙述、降级 κ̄），论文有可能达到 3.5。但在当前状态下，3.0 更准确地反映了累积问题的严重度。\n\n### Q4: Decidability taxonomy 的理论价值——是否被我低估？\n\n**R1 的 Excitement 3/5 有一定道理，但我维持 2.5/5，理由如下：**\n\nR1 可能更看重 decidability taxonomy 的 reusability——三级分类（CF / prefix-decidable with state / non-local）可以迁移到其他 structured generation 任务（如 knowledge graph completion、SQL generation with schema constraints）。从这个角度看，taxonomy 的贡献超越了本文的 IE 场景。\n\n但我认为 taxonomy 的 insight density 有限：\n- Level 1（JSON structure = CF）是 trivially known\n- Level 2（type constraints need state）是 formally interesting 但 intuitively obvious——任何熟悉 PDA 限制的人都会预期此结果\n- Level 3（cross-entity consistency = non-local）的分析在论文中最弱——仅靠 beam search 和 post-hoc 处理，没有 formal guarantee\n\nProposition 1 的证明是正确的，但 **confirmatory**（证实预期）而非 **surprising**（揭示意外）。对于 Excitement 这个维度，confirmatory formalization 的价值低于 surprising insight。\n\n如果论文能展示 taxonomy 指导了一个非直觉的设计决策（例如，某个看似应该在 Level 2 的约束实际上是 Level 3，从而改变了架构），我会提高 Excitement 到 3/5。但当前的 taxonomy 与最终架构之间的映射过于自然——grammar layer → Level 1, semantic layer → Level 2, beam search → Level 3——没有 surprise。\n\n**我将 Excitement 从 2.5 微调至 2.75（如果允许的话），承认 formalization 有 marginal 的迁移价值，但不足以达到 3/5。**\n\n---\n\n## 更新后的综合评估\n\n交叉审稿后，我新增一个 must-fix（BoostCD baseline 缺失，原被我遗漏），其余评分维持不变：\n\n| 维度 | 原始分数 | 交叉后分数 | 变化理由 |\n|------|---------|-----------|---------|\n| Soundness | 3.5 | 3.5 | 无变化——R1 未提出影响 soundness 的新问题 |\n| Excitement | 2.5 | 2.5 | R1 对 taxonomy 的正面评价有道理，但 confirmatory formalization 的 excitement 有限 |\n| Overall | 3.0 | 3.0 | 新增 BoostCD must-fix 被 R1 的正面观点（taxonomy reusability）部分抵消 |\n| Confidence | 4 | 4 | 无变化 |\n\n**Must-Fix 汇总（4 项）**：\n1. 正文超 8 页（W1, 与 R1-M1 一致但我认为应升为 must-fix）\n2. CF 代价透明度（W2）\n3. κ̄ contribution 定位过高（W3）\n4. **[新增]** 缺少 BoostCD 等最直接 baseline 的量化对比（采纳 R1-W1）\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1049 · 2026-05-20T18:48:51.205702+00:00_

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

_source line 1050 · 2026-05-20T18:48:58.047096+00:00_

交叉回应已提交给 Director。

核心结论：
- 对 R1 的 8 条意见中，7 条 [AGREE]（含 1 条升级为 must-fix），1 条 [REBUT]（G(t)=∅ 边界情况）
- 新增采纳 R1-W1 为 must-fix（BoostCD baseline 缺失）
- 维持 Overall 3.0（Findings），R1 给 3.5 的分歧主要在 CF 透明度权重和 κ̄ severity 判定上
- Excitement 维持 2.5，承认 taxonomy 有 marginal 迁移价值但 confirmatory formalization 的 surprise 不足

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 24

## Round 24

94 recorded events


### User

_source line 1051 · 2026-05-20T19:46:23.526584+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 论文完整性 + 写作质量 + Related Work**。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`
- **目标 venue**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25

## Venue 格式要求（已从 CFP 实时确认）
- 正文严格 **8 页**限制，参考文献不限页数
- Limitations 和 Ethics 章节不计入页数（不含过多额外内容）
- ACL 模板，`[review]` 选项
- Double-blind 审稿
- 必须有 Limitations section
- ARR Responsible NLP Research Checklist 必须提交
- Overall Assessment 评分标准：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

### 1. 新颖性评估
- 相对于 XGrammar、Outlines、SynCode 等 grammar-constrained decoding 工作的增量贡献
- 相对于 GoLLIE、KnowCoder、GUIDEX 等 schema-aware IE 工作的定位
- 相对于 BoostCD、GCD、IterGen、EnriCo 等 constraint enforcement 工作的区分度
- Decidability taxonomy（三级分类）的理论迁移价值
- "Enabling dependency" 概念的原创性和实用价值

### 2. 论文完整性
- Abstract 是否准确反映论文实际贡献（是否有 overclaiming）
- Introduction 的 claims 是否都有实验支持
- Contribution 列表是否恰当（数量、粒度、claim 强度）
- Limitations section 是否全面、诚实
- Ethics statement 是否充分
- 论文叙事的完整性（是否有逻辑缺口）

### 3. 写作质量
- 论文结构和叙事流畅度
- 术语一致性（S1/S2 命名、"compile"/"interpret" 措辞分层）
- 表格和图表的清晰度、可读性
- 数学符号的规范性
- 是否有 AI 生成痕迹（过度使用 hedge words、不自然的措辞）

### 4. Related Work
- 覆盖面是否充分（grammar-constrained decoding、schema-aware IE、constraint enforcement、constrained decoding degradation）
- 是否有遗漏的重要工作
- 与竞品的定位是否清晰和公正
- 引用是否真实、完整（注意 unverified/hallucinated citations）

请按以下格式输出审稿报告：
1. Summary（2-3 句）
2. Strengths（逐条，S1/S2/...）
3. Weaknesses（逐条，W1/W2/...，标注严重度：[critical]/[major]/[minor]）
4. Questions for Authors（Q1/Q2/...）
5. Missing References
6. Overall Assessment（评分 + 置信度 + 1-2 句总评）

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

_source line 1052 · 2026-05-20T19:46:34.665020+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
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
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1053 · 2026-05-20T19:46:34.665606+00:00_



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

_source line 1054 · 2026-05-20T19:46:34.873695+00:00_

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

_source line 1055 · 2026-05-20T19:46:34.924333+00:00_



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

_source line 1056 · 2026-05-20T19:46:40.298461+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
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
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1057 · 2026-05-20T19:46:41.455716+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "1-10",
  "project": "schema_semantic_constrained_ie",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "1-10",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1058 · 2026-05-20T19:46:46.896967+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about the ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Criteria

For Findings papers, the main criteria are soundness and reproducibility. Conference recommendatio
…[truncated 1040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6598
}
```

</details>

---


### Tool result

_source line 1059 · 2026-05-20T19:46:49.112930+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.5}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.9}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.1}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"w
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7657
}
```

</details>

---


### Tool call

_source line 1060 · 2026-05-20T19:46:56.397960+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract all review form dimensions/criteria with their scoring scales. I need the exact names of each dimension (e.g., Soundness, Excitement/Novelty, Clarity, etc.), their score ranges, and brief descriptions of what each score means."
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
    "prompt": "Extract all review form dimensions/criteria with their scoring scales. I need the exact names of each dimension (e.g., Soundness, Excitement/Novelty, Clarity, etc.), their score ranges, and brief descriptions of what each score means."
  }
}
```

</details>

---


### Tool call

_source line 1061 · 2026-05-20T19:46:56.939737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1062 · 2026-05-20T19:46:57.978718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1063 · 2026-05-20T19:46:58.309112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1369
}
```

</details>

---


### Tool call

_source line 1064 · 2026-05-20T19:46:58.309591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1065 · 2026-05-20T19:46:59.065640+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1086
}
```

</details>

---


### Tool result

_source line 1066 · 2026-05-20T19:46:59.470929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool result

_source line 1067 · 2026-05-20T19:47:02.849951+00:00_

# ACL Rolling Review Form Dimensions

## 1. **Reviewer Confidence**
**Scale:** 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure, unlikely to have missed important points
- 3: Fairly confident, but may have missed details
- 2: Willing to defend evaluation, but likely missed some aspects
- 1: Outside expertise area or paper unclear

## 2. **Soundness**
**Scale:** 1-5 (with .5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong support for claims; extra experiments optional
- 3: Acceptable; main claims supported with minor gaps
- 2: Poor; main claims lack sufficient support
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
**Scale:** 1-5 (with .5 increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to colleagues
- 3: Interesting; might attend presentation
- 2: Potentially interesting but doesn't resonate personally
- 1: "Not Exciting" and unlikely to interest ACL community

## 4. **Overall Assessment**
**Scale:** 1-5 (with .5 increments)
- 5: "Consider for Award"
- 4: Conference acceptance
- 3: Findings track acceptance
- 2: Resubmit next cycle
- 1: "Do not resubmit"

## 5. **Reproducibility**
**Scale:** 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty; underspecified parameters
- 2: Difficult; unavailable data or insufficient details
- 1: Cannot reproduce

## 6. **Datasets** (if applicable)
**Scale:** 1-5
- 5: Enabling new research directions
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No datasets submitted

## 7. **Software** (if applicable)
**Scale:** 1-5
- 5: Enabling new research directions
- 4: Useful for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No software released

## 8. **Author Identity Knowledge**
**Scale:** 1-5 (transpare
…[truncated 102 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6451
}
```

</details>

---


### Tool call

_source line 1068 · 2026-05-20T19:47:06.857882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1069 · 2026-05-20T19:47:07.414069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1070 · 2026-05-20T19:47:08.420156+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1562
}
```

</details>

---


### Tool call

_source line 1071 · 2026-05-20T19:47:08.621324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1072 · 2026-05-20T19:47:08.822543+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1073 · 2026-05-20T19:47:09.278293+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1864
}
```

</details>

---


### Tool call

_source line 1074 · 2026-05-20T19:47:09.278759+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1075 · 2026-05-20T19:47:09.933248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1076 · 2026-05-20T19:47:10.588953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1077 · 2026-05-20T19:47:11.094178+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2472
}
```

</details>

---


### Tool result

_source line 1078 · 2026-05-20T19:47:12.202874+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3380
}
```

</details>

---


### Tool result

_source line 1079 · 2026-05-20T19:47:13.112253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3833
}
```

</details>

---


### Tool result

_source line 1080 · 2026-05-20T19:47:13.619083+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3685
}
```

</details>

---


### Tool result

_source line 1081 · 2026-05-20T19:47:13.823396+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3234
}
```

</details>

---


### Tool call

_source line 1082 · 2026-05-20T19:47:20.362885+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "11-20",
  "project": "schema_semantic_constrained_ie",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "11-20",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-20T19:47:21.120597+00:00_

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

_source line 1084 · 2026-05-20T19:47:22.075949+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 560.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 613.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 613.2}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 560.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 375.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.9}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 541.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1713
}
```

</details>

---


### Tool result

_source line 1085 · 2026-05-20T19:48:04.601077+00:00_

&lt;persisted-output>
Output too large (50.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/70f718cb-864e-4efb-8277-0f3c245777c0/tool-results/toolu_01FvkajVCdW6wv9sCjL4rnV2.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 59, \"total_citations\": 96, \"unique_cited_keys\": 57, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 47, \"online_not_found\": 2, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [\"chen2024agentre\", \"fan2024fsn\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 43480
}
```

</details>

---


### Tool call

_source line 1086 · 2026-05-20T19:48:08.996876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/70f718cb-864e-4efb-8277-0f3c245777c0/tool-results/toolu_01FvkajVCdW6wv9sCjL4rnV2.txt",
  "offset": "0",
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
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/70f718cb-864e-4efb-8277-0f3c245777c0/tool-results/toolu_01FvkajVCdW6wv9sCjL4rnV2.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1087 · 2026-05-20T19:48:09.853217+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 59, \"total_citations\": 96, \"unique_cited_keys\": 57, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 47, \"online_not_found\": 2, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [\"chen2024agentre\", \"fan2024fsn\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang...\", \
…[truncated 49428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1088 · 2026-05-20T19:48:09.853761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1089 · 2026-05-20T19:48:10.355723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1090 · 2026-05-20T19:48:10.760549+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 1091 · 2026-05-20T19:48:10.761069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1092 · 2026-05-20T19:48:11.215245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool result

_source line 1093 · 2026-05-20T19:48:11.618659+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1094 · 2026-05-20T19:48:18.044576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1095 · 2026-05-20T19:48:18.546873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1096 · 2026-05-20T19:48:19.502054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool result

_source line 1097 · 2026-05-20T19:48:19.504887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 1098 · 2026-05-20T19:48:19.505316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 1099 · 2026-05-20T19:48:20.007420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1100 · 2026-05-20T19:48:20.562501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 1101 · 2026-05-20T19:48:20.562975+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1102 · 2026-05-20T19:48:21.316860+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool result

_source line 1103 · 2026-05-20T19:48:21.318138+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 755
}
```

</details>

---


### Tool call

_source line 1104 · 2026-05-20T19:48:21.368653+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 1105 · 2026-05-20T19:48:21.670363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1106 · 2026-05-20T19:48:22.225932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 1107 · 2026-05-20T19:48:22.478402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 808
}
```

</details>

---


### Tool call

_source line 1108 · 2026-05-20T19:48:27.800634+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "21-32",
  "project": "schema_semantic_constrained_ie",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "21-32",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1109 · 2026-05-20T19:48:29.156187+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.3}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.0}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.4}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.4}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.7}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.8}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.0}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.3}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 1110 · 2026-05-20T19:48:32.370875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
  }
}
```

</details>

---


### Tool call

_source line 1111 · 2026-05-20T19:48:32.823877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 1112 · 2026-05-20T19:48:33.778565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool result

_source line 1113 · 2026-05-20T19:48:33.779963+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1114 · 2026-05-20T19:48:33.780342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 1115 · 2026-05-20T19:48:34.232879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 1116 · 2026-05-20T19:48:34.736235+00:00_



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

_source line 1117 · 2026-05-20T19:48:34.788917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 1118 · 2026-05-20T19:48:35.263640+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1030
}
```

</details>

---


### Tool call

_source line 1119 · 2026-05-20T19:48:35.264123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 1120 · 2026-05-20T19:48:35.716727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 927
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-20T19:48:36.120433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-20T19:48:40.540171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
  }
}
```

</details>

---


### Tool call

_source line 1123 · 2026-05-20T19:48:41.093121+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1124 · 2026-05-20T19:48:41.495951+00:00_



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

_source line 1125 · 2026-05-20T19:48:41.546734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 1126 · 2026-05-20T19:48:41.952625+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 859
}
```

</details>

---


### Tool call

_source line 1127 · 2026-05-20T19:48:41.953112+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 1128 · 2026-05-20T19:48:42.908885+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 1129 · 2026-05-20T19:48:42.910198+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1130 · 2026-05-20T19:48:42.910582+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
  }
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-20T19:48:43.112893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p32.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p32.png"
  }
}
```

</details>

---


### Tool result

_source line 1132 · 2026-05-20T19:48:43.820263+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 1133 · 2026-05-20T19:48:44.022277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1134 · 2026-05-20T19:50:08.529188+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TANL structured prediction augmented natural language Paolini 2021 ACL"
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
    "query": "TANL structured prediction augmented natural language Paolini 2021 ACL"
  }
}
```

</details>

---


### Tool call

_source line 1135 · 2026-05-20T19:50:08.931410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structured output LLM constrained generation information extraction 2025 2026 survey"
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
    "query": "structured output LLM constrained generation information extraction 2025 2026 survey"
  }
}
```

</details>

---


### Tool result

_source line 1136 · 2026-05-20T19:50:13.048415+00:00_

Web search results for query: "TANL structured prediction augmented natural language Paolini 2021 ACL"

Links: [{"title":"(PDF) Structured Prediction as Translation between Augmented Natural Languages","url":"https://www.researchgate.net/publication/348487215_Structured_Prediction_as_Translation_between_Augmented_Natural_Languages"},{"title":"[2101.05779] Structured Prediction as Translation between Augmented Natural Languages","url":"https://arxiv.org/abs/2101.05779"},{"title":"Structured Prediction as Translation between Augmented Natural Languages","url":"https://arxiv.org/pdf/2101.05779"},{"title":"[2101.05779v1] Structured Prediction as Translation between Augmented Natural Languages","url":"https://arxiv.org/abs/2101.05779v1"},{"title":"TANL: Structured prediction as translation between augmented natural languages - Amazon Science","url":"https://www.amazon.science/code-and-datasets/tanl-structured-prediction-as-translation-between-augmented-natural-languages"},{"title":"[PDF] Structured Prediction as Translation between Augmented Natural Languages | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Structured-Prediction-as-Translation-between-Paolini-Athiwaratkun/1cb3f6d545b68db3e7fc6055dcf44099c3ac4672"},{"title":"GitHub - amazon-science/tanl: Structured Prediction as Translation between Augmented Natural Languages · GitHub","url":"https://github.com/amazon-science/tanl"},{"title":"Structured prediction as translation between augmented natural languages - Amazon Science","url":"https://www.amazon.science/publications/structured-prediction-as-translation-between-augmented-natural-languages"},{"title":"DEEPSTRUCT: Pretraining of Language Models for Structure Prediction","url":"https://aclanthology.org/2022.findings-acl.67v2.pdf"},{"title":"Structured Prediction as Translation between Augmented Natural Languages | OpenReview","url":"https://openreview.net/forum?id=US-TP-xnXI"}]

I found the paper you're searching for! Here's what I found:

The TANL
…[truncated 1113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4519
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-20T19:50:17.467032+00:00_

Web search results for query: "structured output LLM constrained generation information extraction 2025 2026 survey"

Links: [{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/pdf/2505.04016"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"A Simple but Effective Approach to Improve Structured Language Model   Output for Information Extraction","url":"https://arxiv.org/pdf/2402.13364"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"}]

Based on the web search results, here's what I found regarding structured output, constrained generation, and information extraction for LLMs in 2025-2026:

## Evolution of Structured Output Approaches

The field has evolved through four phases: prompt engineering (2020-2023) with 5-20% failure rates, JSON mode (2023-2024) with guaranteed syntax but no schema enforcement, schema enforcement (2024-2025) with offerings from OpenAI (August 2024), Google Gemini (May 2024), and Anthropic (November 2025), and high-performance engines (2025-2026) like XGrammar and llguidance achieving near-zero overhead constrained decoding.

## Performance and Technical Advances

XGrammar is the default structured generation backend for vLLM, SGLang, and TensorRT-LLM as of March 2026, achieving under 40 microseconds per token with near-zero overhead in JSO
…[truncated 945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8535
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-20T19:52:23.350838+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告：OntoCoDec\n\n## 1. Summary\n\nOntoCoDec proposes a two-layer constrained decoding framework for information extraction that compiles IE ontologies into token-level constraints: a grammar layer (context-free, via XGrammar) for JSON validity and vocabulary membership, and a semantic layer (prefix-decidable with state) for domain/range type constraints via a runtime entity registry. The paper introduces a three-level decidability taxonomy of IE type constraints and the concept of \"enabling dependency\" between layers. Evaluation on SciERC (551 docs), DocRED (998 docs), and WikiEvents (246 docs) with 7-8B models shows near-elimination of ontology violations with 1.54× latency overhead.\n\n---\n\n## 2. Strengths\n\n**S1. 理论基础扎实：决策性分类体系 (decidability taxonomy) 提供了清晰的形式化框架。**\n三级分类（context-free / prefix-decidable with state / non-local）为理解不同约束执行机制的能力边界提供了干净的理论基础。Proposition 1（Appendix O）通过 pumping lemma 证明了具有无界实体集的 domain/range 约束不是 context-free 的，这一证明正确且直接支撑了两层设计的必要性。\n\n**S2. 消融实验极其充分。**\n论文提供了全面的消融：层级贡献分析（Table 1-3）、S1 vs S2 配置对比、与 fine-tuning 的组合性（Section 5.1）、跨数据集验证（Section 5.2, Table 3）、beam search 兼容性（Appendix F）、文档长度分析（Appendix H）、prompt 敏感性分析（Appendix I）、以及 4 个 case study（Appendix J）。32 页附录虽大，但提供了实质性的深度，而非凑篇幅。\n\n**S3. \"Enabling dependency\" 是一个有价值的概念贡献。**\nTable 1 和 Section 5.1 清楚地展示了：grammar layer 单独只能减少 24% DR（无语义约束时），而 semantic layer 单独无法保证词汇合规性。这种层间相互依赖关系并不显而易见，具有实际指导意义——它说明了为什么单纯堆叠 XGrammar 或单纯做 type checking 都不够。\n\n**S4. 工程设计干净、可复用。**\n系统从任意 IE 本体（JSON Schema 编码）自动编译约束，无需约束专属训练。tokenizer-agnostic masking（Section 3.3）和 grammar-first fallback（Section 4）是合理的设计选择。适用于任何提供 logit 访问的自回归 LM——这是一个合理的部署假设。\n\n**S5. violation 消除效果强。**\nSciERC + LoRA fine-tuning 下实现零违规；DocRED 上 DR 从 15.37% 降至 0.03%（Table 2）。与 fine-tuning 的组合性（Section 5.1）得到充分验证，表明约束执行和参数优化是互补的。\n\n---\n\n## 3. Weaknesses\n\n**W1 [major] 新颖性适中——架构本质上是已有技术的 well-motivated 组合。**\n- Grammar layer 明确是 XGrammar（Dong et al., 2025）应用于 IE JSON schema——Section 3.2 直接写 \"compiled into a pushdown automaton via XGrammar\"。贡献在于 *应用*，而非机制本身。\n- Semantic layer 是一个带状态的查找表（entity registry D: name→type），在 type-bearing positions 做 logit masking。decidability 分析解释了 *why* 需要它，但机制本身（维护 registry + 在特定位置限制类型）是直接的工程实现。\n- Decidability taxonomy 将已知的形式语言理论结果（CFG 不能执行跨字段依赖）重述于 IE 语境。Proposition 1 的 pumping lemma 证明正确但标准。\n- 主要新颖性在于 *组合* 和 *形式化*，而非单个组件。这是有效的贡献，但论文 framing（\"a framework that translates IE ontologies into composable token-level decoding constraints via a decidability-guided architecture\"）可能对概念新颖性有所高估。\n\n**W2 [major] 评估范围相对于泛化性声明偏窄。**\n- 仅 3 个数据集：SciERC（551 docs, 7 entity types）、DocRED（998 docs, 96 relation types）、WikiEvents（246 docs, 56 event types）。全部英语、常用 benchmark。\n- Abstract 和 Section 1 的 Contribution 3 声称 \"compiles constraints automatically from any IE ontology\"，但实际仅测试了 3 个本体。无生物医学、工业级或大规模本体评估。\n- WikiEvents 结果被论文自身描述为 \"preliminary\"（Section 5.4），仅 20 个文档的测试集。\n- 所有模型均为 7B-8B。无 ≥13B 模型或商业 API 评估。Limitations 中承认了这一点，但泛化性声明仍显不足。\n\n**W3 [major] 约束执行对下游任务性能（F1）的实际影响不够清晰。**\n- SciERC 上，约束引入后 F1 基本不变或轻微提升（Table 1: R-F1 44→46 with beam search），增益小且可能在置信区间内。\n- DocRED 上，LoRA + beam S1 的 R-F1 从 7.74 提升至 8.23（Table 3），但绝对 F1 仍然很低。\n- 论文以 DR reduction 为主要指标，但读者会追问：如果违规在本体层面无效但很少影响下游 precision/recall，这些工程开销是否值得？constraint tightness 分析（Section 4, Appendix N）部分回应了这一问题（展示了 tight constraints 与 high DR 的相关性），但未完全弥合 \"violation reduction → practical value\" 的论证缺口。\n\n**W4 [minor] Related Work（Section 6）压缩过度，关键定位论述被推至 Appendix B。**\n- 正文 Related Work 仅约 0.6 页。三个主要线索（grammar-constrained decoding, schema-aware IE, constraint enforcement + degradation）各仅 1-2 句话配 citation 列表，无法实现有意义的定位。\n- **TANL**（Paolini et al., 2021, ICLR 2021）——\"Structured Prediction as Translation between Augmented Natural Languages\"——未被引用。这是生成式结构化预测范式的基础性工作，直接催生了 OntoCoDec 所构建的 IE-as-generation 范式，属于值得注意的遗漏。\n- Appendix B（pages 14-18）的扩展 Related Work 覆盖面广且详细，但将关键定位论述放在附录中削弱了正文叙事。\n\n**W5 [minor] 部分术语和符号密度较高，可能影响可读性。**\n- 论文在 Section 2-4 中引入了大量形式化：G(t), S(t), V, D（entity registry）, M_final, 三级 decidability taxonomy, \"enabling dependency\", \"grammar-first fallback\", \"constraint tightness κ\"——密度较高。\n- Constraint tightness κ（Eq. 3）在 Section 4 引入并贯穿分析，但对非专家读者的直觉解释可以更清晰。\n- 整体写作质量良好，无明显 AI 生成痕迹，术语使用一致（S1/S2 命名、compile/interpret 层次分明），结构流畅。\n\n**W6 [minor] 两个孤立 bib 条目和轻微引用问题。**\n- `chen2024agentre` 和 `fan2024fsn` 在 bibliography 中但从未被引用。\n- `formattax2026`（\"The Format Tax\"）和 `regino2025kgcurator` 无法通过 OpenAlex 验证（前者可能太新，后者为 workshop paper）。这两篇并非幻觉引用——看起来是真实工作——但应确认。\n- 其余 10 条 \"mismatch\" 均为作者名 LaTeX 编码差异（如 šakota vs sakota），属于良性问题。\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** Enabling dependency 通过 Table 1 的 layer-level 消融进行了展示，但能否提供更受控的消融？具体来说：(a) grammar layer 有词汇约束但 *无* domain/range 执行 vs. (b) semantic layer 有 domain/range 执行但 *无* grammar 保证的词汇合规性。这将超越 layer-level 消融，隔离每种约束类型的具体贡献。\n\n**Q2.** OntoCoDec 在具有显著更多 entity/relation types 的本体（如 Wikidata 的数千种类型）上表现如何？Appendix K（Table 29）展示了编译时间可达 1,000 relations，但大规模推理时的运行时开销未报告。\n\n**Q3.** 论文报告 full S1 constrained decoding 的 latency overhead 为 1.54×（Section 5, Appendix G）。这一开销如何随序列长度和 schema 复杂度缩放？开销是由 grammar compilation、semantic masking 还是两者共同主导？\n\n**Q4.** WikiEvents（Section 5.4）中，full S1 结果显示极端的词汇违规（EV+RoV >85%, Table 5），entity F1=0。这表明 grammar-only layer 对 event extraction 严重不足。能否讨论为什么 EE 对 grammar-constrained 方法特别具有挑战性，是否需要额外的架构组件？\n\n**Q5.** CF→DR trade-off（Section 5.1, Appendix C）显示消除 CF 会将违规重新路由至 DR。这是任何两层约束系统的固有限制，还是 OntoCoDec 设计的特定产物？\n\n---\n\n## 5. Missing References\n\n1. **TANL**（Paolini et al., 2021, ICLR）: \"Structured Prediction as Translation between Augmented Natural Languages\" ——生成式结构化预测的基础性工作，直接催生了 OntoCoDec 所依赖的 IE-as-generation 范式。\n2. 可考虑引用 **SLOT**（2025, EMNLP Industry）: \"Structuring the Output of Large Language Models\" ——与生产环境中的结构化输出执行相关。\n\n---\n\n## 6. Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 技术方法正确，两层架构由 decidability 分析良好支撑。消融充分。但评估仅覆盖 3 个英语数据集和 7-8B 模型，相对泛化性声明不足。Proposition 1 正确但标准。 |\n| **Excitement** | 3/5 | Decidability taxonomy 和 enabling dependency 是有价值的概念贡献，但架构本质是已有技术的组合（XGrammar + 查找表式 type masking）。不开辟根本性新方向，但提供了有用的形式化框架。 |\n| **Reproducibility** | 4/5 | 实验设置描述详细（Appendix G: 硬件、超参数、随机种子）；prompt templates 完整给出（Appendix A, Table 6）；数据集公开可用。代码未提供但方法描述足以复现。 |\n| **Overall Assessment** | **3.5 — Borderline Conference** | |\n| **Confidence** | 4/5 | 对 constrained decoding 和 IE 文献较熟悉，仔细阅读了全文含附录。 |\n\n### 一句话总评\n\nOntoCoDec 提供了一个工程质量高、理论动机清晰的约束解码框架，但新颖性适中（主要是已有技术的 principled composition），评估范围（3 个英语数据集、仅 7-8B 模型）相对其泛化性声明偏窄，且约束执行对下游 F1 的实际增益有限。是一篇扎实的 Findings 水平工作，若能拓展评估覆盖面或从理论框架中导出更意外的洞察，可冲击 Conference。\n",
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
    "text": "\n# Reviewer 2 审稿报告：OntoCoDec\n\n## 1. Summary\n\nOntoCoDec proposes a two-layer constrained decoding framework for information extraction that compiles IE ontologies into token-level constraints: a grammar layer (context-free, via XGrammar) for JSON validity and vocabulary membership, and a semantic layer (prefix-decidable with state) for domain/range type constraints via a runtime entity registry. The paper introduces a three-level decidability taxonomy of IE type constraints and the concept of \"enabling dependency\" between layers. Evaluation on SciERC (551 docs), DocRED (998 docs), and WikiEvents (246 docs) with 7-8B models shows near-elimination of ontology violations with 1.54× latency overhead.\n\n---\n\n## 2. Strengths\n\n**S1. 理论基础扎实：决策性分类体系 (decidability taxonomy) 提供了清晰的形式化框架。**\n三级分类（context-free / prefix-decidable with state / non-local）为理解不同约束执行机制的能力边界提供了干净的理论基础。Proposition 1（Appendix O）通过 pumping lemma 证明了具有无界实体集的 domain/range 约束不是 context-free 的，这一证明正确且直接支撑了两层设计的必要性。\n\n**S2. 消融实验极其充分。**\n论文提供了全面的消融：层级贡献分析（Table 1-3）、S1 vs S2 配置对比、与 fine-tuning 的组合性（Section 5.1）、跨数据集验证（Section 5.2, Table 3）、beam search 兼容性（Appendix F）、文档长度分析（Appendix H）、prompt 敏感性分析（Appendix I）、以及 4 个 case study（Appendix J）。32 页附录虽大，但提供了实质性的深度，而非凑篇幅。\n\n**S3. \"Enabling dependency\" 是一个有价值的概念贡献。**\nTable 1 和 Section 5.1 清楚地展示了：grammar layer 单独只能减少 24% DR（无语义约束时），而 semantic layer 单独无法保证词汇合规性。这种层间相互依赖关系并不显而易见，具有实际指导意义——它说明了为什么单纯堆叠 XGrammar 或单纯做 type checking 都不够。\n\n**S4. 工程设计干净、可复用。**\n系统从任意 IE 本体（JSON Schema 编码）自动编译约束，无需约束专属训练。tokenizer-agnostic masking（Section 3.3）和 grammar-first fallback（Section 4）是合理的设计选择。适用于任何提供 logit 访问的自回归 LM——这是一个合理的部署假设。\n\n**S5. violation 消除效果强。**\nSciERC + LoRA fine-tuning 下实现零违规；DocRED 上 DR 从 15.37% 降至 0.03%（Table 2）。与 fine-tuning 的组合性（Section 5.1）得到充分验证，表明约束执行和参数优化是互补的。\n\n---\n\n## 3. Weaknesses\n\n**W1 [major] 新颖性适中——架构本质上是已有技术的 well-motivated 组合。**\n- Grammar layer 明确是 XGrammar（Dong et al., 2025）应用于 IE JSON schema——Section 3.2 直接写 \"compiled into a pushdown automaton via XGrammar\"。贡献在于 *应用*，而非机制本身。\n- Semantic layer 是一个带状态的查找表（entity registry D: name→type），在 type-bearing positions 做 logit masking。decidability 分析解释了 *why* 需要它，但机制本身（维护 registry + 在特定位置限制类型）是直接的工程实现。\n- Decidability taxonomy 将已知的形式语言理论结果（CFG 不能执行跨字段依赖）重述于 IE 语境。Proposition 1 的 pumping lemma 证明正确但标准。\n- 主要新颖性在于 *组合* 和 *形式化*，而非单个组件。这是有效的贡献，但论文 framing（\"a framework that translates IE ontologies into composable token-level decoding constraints via a decidability-guided architecture\"）可能对概念新颖性有所高估。\n\n**W2 [major] 评估范围相对于泛化性声明偏窄。**\n- 仅 3 个数据集：SciERC（551 docs, 7 entity types）、DocRED（998 docs, 96 relation types）、WikiEvents（246 docs, 56 event types）。全部英语、常用 benchmark。\n- Abstract 和 Section 1 的 Contribution 3 声称 \"compiles constraints automatically from any IE ontology\"，但实际仅测试了 3 个本体。无生物医学、工业级或大规模本体评估。\n- WikiEvents 结果被论文自身描述为 \"preliminary\"（Section 5.4），仅 20 个文档的测试集。\n- 所有模型均为 7B-8B。无 ≥13B 模型或商业 API 评估。Limitations 中承认了这一点，但泛化性声明仍显不足。\n\n**W3 [major] 约束执行对下游任务性能（F1）的实际影响不够清晰。**\n- SciERC 上，约束引入后 F1 基本不变或轻微提升（Table 1: R-F1 44→46 with beam search），增益小且可能在置信区间内。\n- DocRED 上，LoRA + beam S1 的 R-F1 从 7.74 提升至 8.23（Table 3），但绝对 F1 仍然很低。\n- 论文以 DR reduction 为主要指标，但读者会追问：如果违规在本体层面无效但很少影响下游 precision/recall，这些工程开销是否值得？constraint tightness 分析（Section 4, Appendix N）部分回应了这一问题（展示了 tight constraints 与 high DR 的相关性），但未完全弥合 \"violation reduction → practical value\" 的论证缺口。\n\n**W4 [minor] Related Work（Section 6）压缩过度，关键定位论述被推至 Appendix B。**\n- 正文 Related Work 仅约 0.6 页。三个主要线索（grammar-constrained decoding, schema-aware IE, constraint enforcement + degradation）各仅 1-2 句话配 citation 列表，无法实现有意义的定位。\n- **TANL**（Paolini et al., 2021, ICLR 2021）——\"Structured Prediction as Translation between Augmented Natural Languages\"——未被引用。这是生成式结构化预测范式的基础性工作，直接催生了 OntoCoDec 所构建的 IE-as-generation 范式，属于值得注意的遗漏。\n- Appendix B（pages 14-18）的扩展 Related Work 覆盖面广且详细，但将关键定位论述放在附录中削弱了正文叙事。\n\n**W5 [minor] 部分术语和符号密度较高，可能影响可读性。**\n- 论文在 Section 2-4 中引入了大量形式化：G(t), S(t), V, D（entity registry）, M_final, 三级 decidability taxonomy, \"enabling dependency\", \"grammar-first fallback\", \"constraint tightness κ\"——密度较高。\n- Constraint tightness κ（Eq. 3）在 Section 4 引入并贯穿分析，但对非专家读者的直觉解释可以更清晰。\n- 整体写作质量良好，无明显 AI 生成痕迹，术语使用一致（S1/S2 命名、compile/interpret 层次分明），结构流畅。\n\n**W6 [minor] 两个孤立 bib 条目和轻微引用问题。**\n- `chen2024agentre` 和 `fan2024fsn` 在 bibliography 中但从未被引用。\n- `formattax2026`（\"The Format Tax\"）和 `regino2025kgcurator` 无法通过 OpenAlex 验证（前者可能太新，后者为 workshop paper）。这两篇并非幻觉引用——看起来是真实工作——但应确认。\n- 其余 10 条 \"mismatch\" 均为作者名 LaTeX 编码差异（如 šakota vs sakota），属于良性问题。\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** Enabling dependency 通过 Table 1 的 layer-level 消融进行了展示，但能否提供更受控的消融？具体来说：(a) grammar layer 有词汇约束但 *无* domain/range 执行 vs. (b) semantic layer 有 domain/range 执行但 *无* grammar 保证的词汇合规性。这将超越 layer-level 消融，隔离每种约束类型的具体贡献。\n\n**Q2.** OntoCoDec 在具有显著更多 entity/relation types 的本体（如 Wikidata 的数千种类型）上表现如何？Appendix K（Table 29）展示了编译时间可达 1,000 relations，但大规模推理时的运行时开销未报告。\n\n**Q3.** 论文报告 full S1 constrained decoding 的 latency overhead 为 1.54×（Section 5, Appendix G）。这一开销如何随序列长度和 schema 复杂度缩放？开销是由 grammar compilation、semantic masking 还是两者共同主导？\n\n**Q4.** WikiEvents（Section 5.4）中，full S1 结果显示极端的词汇违规（EV+RoV >85%, Table 5），entity F1=0。这表明 grammar-only layer 对 event extraction 严重不足。能否讨论为什么 EE 对 grammar-constrained 方法特别具有挑战性，是否需要额外的架构组件？\n\n**Q5.** CF→DR trade-off（Section 5.1, Appendix C）显示消除 CF 会将违规重新路由至 DR。这是任何两层约束系统的固有限制，还是 OntoCoDec 设计的特定产物？\n\n---\n\n## 5. Missing References\n\n1. **TANL**（Paolini et al., 2021, ICLR）: \"Structured Prediction as Translation between Augmented Natural Languages\" ——生成式结构化预测的基础性工作，直接催生了 OntoCoDec 所依赖的 IE-as-generation 范式。\n2. 可考虑引用 **SLOT**（2025, EMNLP Industry）: \"Structuring the Output of Large Language Models\" ——与生产环境中的结构化输出执行相关。\n\n---\n\n## 6. Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 技术方法正确，两层架构由 decidability 分析良好支撑。消融充分。但评估仅覆盖 3 个英语数据集和 7-8B 模型，相对泛化性声明不足。Proposition 1 正确但标准。 |\n| **Excitement** | 3/5 | Decidability taxonomy 和 enabling dependency 是有价值的概念贡献，但架构本质是已有技术的组合（XGrammar + 查找表式 type masking）。不开辟根本性新方向，但提供了有用的形式化框架。 |\n| **Reproducibility** | 4/5 | 实验设置描述详细（Appendix G: 硬件、超参数、随机种子）；prompt templates 完整给出（Appendix A, Table 6）；数据集公开可用。代码未提供但方法描述足以复现。 |\n| **Overall Assessment** | **3.5 — Borderline Conference** | |\n| **Confidence** | 4/5 | 对 constrained decoding 和 IE 文献较熟悉，仔细阅读了全文含附录。 |\n\n### 一句话总评\n\nOntoCoDec 提供了一个工程质量高、理论动机清晰的约束解码框架，但新颖性适中（主要是已有技术的 principled composition），评估范围（3 个英语数据集、仅 7-8B 模型）相对其泛化性声明偏窄，且约束执行对下游 F1 的实际增益有限。是一篇扎实的 Findings 水平工作，若能拓展评估覆盖面或从理论框架中导出更意外的洞察，可冲击 Conference。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1139 · 2026-05-20T19:52:26.965373+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3614
}
```

</details>

---


### Tool call

_source line 1140 · 2026-05-20T19:52:31.939290+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
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
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1141 · 2026-05-20T19:52:31.990067+00:00_



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

_source line 1142 · 2026-05-20T19:52:36.326414+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1143 · 2026-05-20T19:52:36.377577+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 1144 · 2026-05-20T19:52:43.963201+00:00_

审稿报告已提交给 Review Director。

**审稿结论：3.5 — Borderline Conference**

核心判断：
- **新颖性适中**：两层架构本质是 XGrammar + 查找表式 type masking 的 principled composition，decidability taxonomy 是有价值的形式化但非突破性贡献
- **评估范围偏窄**：仅 3 个英语数据集、7-8B 模型，相对 "any IE ontology" 的泛化性声明不足
- **F1 增益有限**：violation reduction 显著，但对下游任务性能的实际影响不清晰
- **主要优势**：消融极充分、enabling dependency 概念有价值、工程质量高、写作质量良好

关键遗漏引用：TANL（Paolini et al., 2021, ICLR）——生成式结构化预测的基础性工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 25

## Round 25

4 recorded events


### User

_source line 1145 · 2026-05-20T19:54:49.619832+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每条 Weakness 和 Question，使用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿报告：OntoCoDec

**审查侧重**: 方法严谨性 + 实验设计与评估

## 2. Strengths

**S1. 理论基础扎实且有原创性。** Proposition 1 的 pumping lemma 证明（Appendix O, pp. 31-32）正确地建立了 domain/range type constraint 超出 context-free 语言能力的结论，为两层架构提供了形式化动机。三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）是对 constrained decoding 领域的概念性贡献，清晰地界定了不同约束类别的计算复杂度。

**S2. 消融设计严谨，enabling dependency 论证清晰。** SciERC 五路消融（Table 1）和 DocRED 四路消融（Table 2-3）有效证明了各层的独立贡献：grammar-only 仅减少 24% DR（Section 5.1），semantic layer 是消除 domain/range violations 的关键，fine-tuning 与约束可组合（DR ≤ 0.09% across all fine-tuned settings）。层间 enabling dependency 的论证是本文的一大亮点。

**S3. 统计检验规范。** Bootstrap 10,000 paired significance tests（§5.1, §5.2）覆盖关键对比，p 值均有报告。fine-tuning composability 的显著性检验（p<0.001 for DR, p=0.06 for R-F1）展现了负责任的统计实践。

**S4. 跨模型一致性好。** 3 models（Qwen3-8B, Llama-3.1-8B, Mistral-7B）× 2 datasets 的交叉验证（Tables 1-4）显示约束效果在不同 tokenizer 家族间一致，支持了 tokenizer-agnostic 的声称。

**S5. 工程贡献实用。** 运行时开销低（S1: +13.1% SciERC, +2.43% DocRED），continuation masking 的 tokenizer-agnostic 设计（§4）和 grammar-first fallback（§4）都是实际可部署的设计选择。Appendix G 的完整复现细节值得肯定。

**S6. 论文写作清晰，结构合理。** 正文 8 页内完成了理论动机→方法→实验→讨论的完整叙事，appendix 提供了充分的补充材料。Figure 1 的架构概览信息密度高。

## 3. Weaknesses

**W1 [critical] 缺少与最相关 constrained decoding baselines 的实验对比。**
论文在 Related Work 中引用了 BoostCD、GCD、IterGen、SynCode 和 DOMINO，但实验中未与任何一个进行实验对比。特别是 BoostCD 是唯一一个明确将 constrained decoding 应用于 IE 的工作，完全没有实验对比是不可接受的。GCD 作为 grammar-constrained decoding for structured NLP 的直接前驱，也应纳入 baseline。

**W2 [critical] Grammar-first fallback 频率过高（36.6%），削弱了 type constraint enforcement 的核心声称。**
在 SciERC 上，grammar-first fallback 在 36.64% 的 type-bearing positions 触发（Table 7）。这意味着超过三分之一的关键位置上，semantic layer 的 type constraints 被完全放弃，仅保留 grammar layer 的结构约束。论文称 fallback 的 CF 消除"只 re-routes violations to DR"，但这实际上意味着系统在大量位置上退化为 grammar-only 模式。

**W3 [major] WikiEvents 评估（20-doc test set）统计功效极低。**
20 个文档不足以支撑对 56 event types 的约束效果评估——平均每个 event type 不到 0.4 个测试文档。

**W4 [major] Proposition 1 证明中的 position-indexing 简化未被充分讨论。**
Proposition 1 的完整证明使用 position-based entity indexing，但 OntoCoDec 的实际 JSON 输出通过 name strings 引用实体。从简化版本到实际系统的 gap 需要更精确的处理。

**W5 [major] Constraint tightness κ̄ 的 predictive value 基于仅 2 个数据点。**
κ̄ 仅在 SciERC 和 DocRED 上计算。Appendix D 的 dual-factor analysis 报告 Spearman ρ = -0.77 with n=6，统计功效极低。

**W6 [major] Beam search 评估不完整：DocRED 仅 50-doc 子集。**
DocRED zero-shot beam search 仅在 50-doc 子集上评估，而非完整 998-doc dev set。

**W7 [minor] 70B 评估过于 preliminary，贡献有限。**
仅量化推理，未测试 70B+LoRA fine-tuning，INT4 量化可能影响 baseline 质量。

**W8 [minor] Entity registry 的顺序依赖假设缺少量化验证。**
论文未报告 S1 下实体-关系生成顺序违反的频率。

## 4. Questions

Q1. BoostCD 为何未作为 experimental baseline？
Q2. Grammar-first fallback 在 DocRED 上的触发比例？fallback root causes 分布？
Q3. 如果 output format 改为 canonical entity IDs，Proposition 1 是否仍然成立？
Q4. 更 aggressive 的约束策略（backtrack/resample）能否同时降低 DR 和 CF？
Q5. 能否量化 "well-calibrated" 的具体条件？
Q6. WikiEvents 20-doc test set 上的 document-level variance？

## 6. Overall Assessment
- Soundness: 3.5/5
- Excitement: 3.5/5
- Reproducibility: 4/5
- **Overall: 3.5 — Borderline Conference**
- Confidence: 4/5

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

_source line 1146 · 2026-05-20T19:57:13.325901+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n## 逐条回应\n\n### Weaknesses\n\n**[AGREE] R1-W1 (缺少 BoostCD/GCD baseline):** 完全同意这是最大缺陷之一。BoostCD 是唯一明确将 constrained decoding 应用于 IE 的同期工作，在 SciERC/DocRED 上有公开结果，完全没有实验对比不可接受。GCD 作为直接前驱也应纳入。论文在 Section 5 中仅做间接引用（引用其他工作的数字），而非受控对比。\n\n**[AGREE with nuance] R1-W2 (Fallback 36.6%):** 同意问题存在，但我判断 [major] 而非 [critical]。两个缓解因素：(1) 36.6% 是 zero-shot 下的数据，fine-tuning 后应降低（但论文未报告 fine-tuned fallback 率——这本身是缺失）；(2) 即使有此 fallback 率，整体 DR 仍显著下降（zero-shot ~1%, fine-tuned ≤0.09%）。但论文确实应在正文中更诚实地量化这一退化。\n\n**[AGREE] R1-W3 (WikiEvents 20-doc):** 完全同意。我在自己的审稿中也指出了这一点（我的 W2）。20 docs / 56 event types 无法支撑可靠评估。\n\n**[REBUT] R1-W4 (Proposition 1 position-indexing):** Appendix O 第 32 页底部 \"Position indexing vs. name referencing\" 段落已讨论了这一 gap。论文论述 name-based referencing 的约束严格性不弱于 position-based（name→type binding 同样创建跨位置依赖），position-based 是简化而非弱化。non-context-free 结论在 name-based 系统中仍然成立。但 R1 的 Q3（canonical IDs 下是否成立）是更尖锐的问题——有限实体集下约束退化为 regular language，Proposition 1 不成立。论文应更明确讨论这一边界。\n\n**[AGREE] R1-W5 (κ̄ 统计功效):** n=6 做 Spearman 相关不严谨。建议将 κ̄ 仅作为定性分析工具，移除 Appendix D 中的推断统计数字。\n\n**[AGREE] R1-W6 (DocRED beam search 50-doc):** 同意。Beam search 是宣称的关键配置，仅 50/998 docs 的覆盖不足。\n\n**[AGREE] R1-W7 (70B preliminary):** 同意但确实仅为 minor。定位为 preliminary evidence 尚可接受。\n\n**[AGREE] R1-W8 (顺序依赖量化):** 同意。应报告 S1 下 entity-before-relation ordering 的保持率。\n\n### Questions\n\n- Q1: 见 W1。AGREE。\n- Q2: 有效。DocRED 的 fallback 数据确实缺失。\n- Q3: 尖锐问题。有限实体集 + canonical IDs 下 Proposition 1 不成立。但论文假设 unbounded entity sets，对 open-domain IE 合理。应更明确讨论。\n- Q4: 有价值建议。IterGen 式 backtracking 可能改善 DR-CF trade-off 但增加延迟。\n- Q5: 合理。\"Well-calibrated\" 应被显式定义和量化。\n- Q6: 同意。应报告 per-document variance。\n\n## 总评\n\nR1 审稿质量很高。8 条 Weakness 中我同意 7 条，仅对 W4 反驳（论文已有讨论），对 W2 同意但降低严重度至 major。两位 reviewer 核心判断一致：technically sound、well-executed 但 novelty 适中、evaluation scope 偏窄。R1 的 3.5 (Borderline Conference) 与我评分相同。R1 侧重方法/实验严谨性，我侧重新颖性/写作/Related Work，两份意见互补。\n",
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
    "text": "\n# Reviewer 2 交叉回应 Reviewer 1 审稿意见\n\n## 逐条回应\n\n### Weaknesses\n\n**[AGREE] R1-W1 (缺少 BoostCD/GCD baseline):** 完全同意这是最大缺陷之一。BoostCD 是唯一明确将 constrained decoding 应用于 IE 的同期工作，在 SciERC/DocRED 上有公开结果，完全没有实验对比不可接受。GCD 作为直接前驱也应纳入。论文在 Section 5 中仅做间接引用（引用其他工作的数字），而非受控对比。\n\n**[AGREE with nuance] R1-W2 (Fallback 36.6%):** 同意问题存在，但我判断 [major] 而非 [critical]。两个缓解因素：(1) 36.6% 是 zero-shot 下的数据，fine-tuning 后应降低（但论文未报告 fine-tuned fallback 率——这本身是缺失）；(2) 即使有此 fallback 率，整体 DR 仍显著下降（zero-shot ~1%, fine-tuned ≤0.09%）。但论文确实应在正文中更诚实地量化这一退化。\n\n**[AGREE] R1-W3 (WikiEvents 20-doc):** 完全同意。我在自己的审稿中也指出了这一点（我的 W2）。20 docs / 56 event types 无法支撑可靠评估。\n\n**[REBUT] R1-W4 (Proposition 1 position-indexing):** Appendix O 第 32 页底部 \"Position indexing vs. name referencing\" 段落已讨论了这一 gap。论文论述 name-based referencing 的约束严格性不弱于 position-based（name→type binding 同样创建跨位置依赖），position-based 是简化而非弱化。non-context-free 结论在 name-based 系统中仍然成立。但 R1 的 Q3（canonical IDs 下是否成立）是更尖锐的问题——有限实体集下约束退化为 regular language，Proposition 1 不成立。论文应更明确讨论这一边界。\n\n**[AGREE] R1-W5 (κ̄ 统计功效):** n=6 做 Spearman 相关不严谨。建议将 κ̄ 仅作为定性分析工具，移除 Appendix D 中的推断统计数字。\n\n**[AGREE] R1-W6 (DocRED beam search 50-doc):** 同意。Beam search 是宣称的关键配置，仅 50/998 docs 的覆盖不足。\n\n**[AGREE] R1-W7 (70B preliminary):** 同意但确实仅为 minor。定位为 preliminary evidence 尚可接受。\n\n**[AGREE] R1-W8 (顺序依赖量化):** 同意。应报告 S1 下 entity-before-relation ordering 的保持率。\n\n### Questions\n\n- Q1: 见 W1。AGREE。\n- Q2: 有效。DocRED 的 fallback 数据确实缺失。\n- Q3: 尖锐问题。有限实体集 + canonical IDs 下 Proposition 1 不成立。但论文假设 unbounded entity sets，对 open-domain IE 合理。应更明确讨论。\n- Q4: 有价值建议。IterGen 式 backtracking 可能改善 DR-CF trade-off 但增加延迟。\n- Q5: 合理。\"Well-calibrated\" 应被显式定义和量化。\n- Q6: 同意。应报告 per-document variance。\n\n## 总评\n\nR1 审稿质量很高。8 条 Weakness 中我同意 7 条，仅对 W4 反驳（论文已有讨论），对 W2 同意但降低严重度至 major。两位 reviewer 核心判断一致：technically sound、well-executed 但 novelty 适中、evaluation scope 偏窄。R1 的 3.5 (Borderline Conference) 与我评分相同。R1 侧重方法/实验严谨性，我侧重新颖性/写作/Related Work，两份意见互补。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1147 · 2026-05-20T19:57:17.750490+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4424
}
```

</details>

---


### Assistant

_source line 1148 · 2026-05-20T19:57:22.652525+00:00_

交叉回应已提交。

总结：在 R1 的 8 条 Weakness 中，我同意 7 条（W1/W3/W5/W6/W7/W8 完全同意，W2 同意但降为 major），仅对 W4（Proposition 1 的 position-indexing）提出反驳——Appendix O 已有 "Position indexing vs. name referencing" 的讨论。两位 Reviewer 的核心判断一致：3.5 Borderline Conference，technically sound 但 novelty 适中、evaluation scope 偏窄。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 26

## Round 26

104 recorded events


### User

_source line 1149 · 2026-05-21T01:19:25.866056+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 论文完整性 + 格式合规** 审查。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`

## Venue 要求（已通过 web search 确认）
- **目标**: EMNLP 2026, ARR May 2026 cycle
- **截止日期**: 2026-05-25
- **页数**: Long paper 8 页正文 + 无限参考文献
- **Limitations**: 必须有独立 Limitations section，不计入页数
- **模板**: ACL 模板，必须使用 `[review]` 选项
- **匿名**: Double-blind review（论文中不得出现作者信息、去匿名化的自引）
- **附录**: 双栏格式
- **Checklist**: ARR Responsible NLP Research Checklist 必须填写
- **特别注意**: 从 2025年7月起，附录不使用双栏格式会被 desk reject

## 你的审查侧重

### 新颖性评估
1. **核心创新定位**：OntoCoDec 的主要创新是什么？是组件级创新（grammar/semantic layer 各自新颖）还是系统级创新（composition + formalization）？在 constrained decoding 和 schema-aware IE 的既有工作中，新颖性是否足够？
2. **与最近竞品的差异化**：与 BoostCD (Sakota et al., 2025)、GCD (Geng et al., 2023)、EnriCo (Zaratiana et al., 2024)、IterGen (Ugare et al., 2024) 的区别是否清晰？论文是否充分论证了 OntoCoDec 超越这些方法的地方？
3. **Decidability taxonomy 的理论贡献**：三层分类作为理论贡献是否足够有意义？是否有类似的分类在先前工作中已存在？
4. **Constraint tightness κ̄**：作为新概念的价值如何？是否 trivial（即 schema 越松约束效果越好这一直觉的量化）？

### 论文完整性
1. **Related Work 覆盖**：是否遗漏重要相关工作？特别注意：(a) constrained decoding 领域（PICARD, SynCode, BoostCD, GCD）；(b) schema-aware IE（GoLLIE, TANL, InstructUIE）；(c) type constraint enforcement in KG（KGCURATOR, FormaTax）
2. **论述逻辑**：Introduction → Background → Method → Experiments → Related Work → Conclusion 的叙事是否连贯？各 Section 之间的过渡是否自然？
3. **声称与证据的一致性**：Abstract/Intro 中的声称是否都有实验支撑？是否有过度声称（overclaim）的情况？
4. **Limitations 完整性**：是否诚实地报告了所有重要限制？CF 问题、WikiEvents 小样本、仅英语数据集等是否充分讨论？

### 格式合规（逐项检查）
1. **页数**：正文是否 ≤ 8 页？
2. **匿名**：是否有泄露作者身份的信息？（检查自引方式、代码链接、acknowledgment）
3. **模板**：是否使用 ACL 模板 + `[review]` 选项？
4. **Limitations section**：是否存在？位置是否在 conclusion 之后、references 之前？
5. **Checklist**：ARR Responsible NLP Checklist 是否填写？
6. **附录格式**：是否双栏？
7. **引用格式**：是否使用 natbib？
8. **Ethics Statement**：是否存在？

### 评分标准（EMNLP 2026 ARR）
5 = Consider for Award, 4 = Conference, 3.5 = Borderline Conference, 3 = Findings, 2.5 = Borderline Findings, 2 = Resubmit next cycle

请给出完整审稿意见，包括：Summary (2-3 句) → Strengths (逐条) → Weaknesses (逐条，标明严重程度 critical/major/minor) → Questions → Missing References → Overall Assessment (评分+置信度+理由)。

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

_source line 1150 · 2026-05-21T01:19:36.708589+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
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
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1151 · 2026-05-21T01:19:36.809866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-21T01:19:44.378848+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-10",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1153 · 2026-05-21T01:19:46.438496+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.7}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"w
…[truncated 519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2059
}
```

</details>

---


### Tool call

_source line 1154 · 2026-05-21T01:19:52.151852+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "11-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1155 · 2026-05-21T01:19:53.670514+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 560.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 633.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 611.4}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 375.1}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 554.8}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.1}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1518
}
```

</details>

---


### Tool call

_source line 1156 · 2026-05-21T01:19:57.509230+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "21-34",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "21-34",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1157 · 2026-05-21T01:20:01.835100+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 530.3}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 515.5}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.7}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 486.4}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.3}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 485.3}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.0}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4325
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-21T01:20:06.372085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-21T01:20:07.080523+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-21T01:20:14.085862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-21T01:20:15.092427+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-21T01:20:18.210613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-21T01:20:18.865655+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-21T01:20:21.379841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-21T01:20:22.287637+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-21T01:20:24.907417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-21T01:20:25.915119+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-21T01:20:31.200993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-21T01:20:32.134151+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 933
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-21T01:20:34.756942+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-21T01:20:35.866121+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-21T01:20:39.653102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-21T01:20:40.359021+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-21T01:20:44.592892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 1175 · 2026-05-21T01:20:44.644539+00:00_



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

_source line 1176 · 2026-05-21T01:20:57.452096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1177 · 2026-05-21T01:20:58.458281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1178 · 2026-05-21T01:21:01.475883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1179 · 2026-05-21T01:21:02.362214+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 886
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-21T01:21:04.968251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-21T01:21:05.622585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 1182 · 2026-05-21T01:21:09.291879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1183 · 2026-05-21T01:21:09.945420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-21T01:21:12.662001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-21T01:21:13.471062+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 1186 · 2026-05-21T01:21:16.486442+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1187 · 2026-05-21T01:21:17.142918+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1188 · 2026-05-21T01:21:20.159510+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1189 · 2026-05-21T01:21:20.615104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 1190 · 2026-05-21T01:21:23.632027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1191 · 2026-05-21T01:21:24.238904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 1192 · 2026-05-21T01:21:27.151527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1193 · 2026-05-21T01:21:27.806830+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 1194 · 2026-05-21T01:21:34.200286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1195 · 2026-05-21T01:21:34.856373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1196 · 2026-05-21T01:21:38.473873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1197 · 2026-05-21T01:21:39.179862+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1198 · 2026-05-21T01:21:42.896091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 1199 · 2026-05-21T01:21:43.500477+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1200 · 2026-05-21T01:21:46.815117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 1201 · 2026-05-21T01:21:47.470668+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 1202 · 2026-05-21T01:21:50.444933+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 1203 · 2026-05-21T01:21:51.416631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 971
}
```

</details>

---


### Tool call

_source line 1204 · 2026-05-21T01:21:54.280618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 1205 · 2026-05-21T01:21:54.886831+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 606
}
```

</details>

---


### Tool call

_source line 1206 · 2026-05-21T01:22:02.605225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 1207 · 2026-05-21T01:22:03.312974+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 1208 · 2026-05-21T01:22:06.686710+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 1209 · 2026-05-21T01:22:07.290738+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-21T01:22:10.705201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-21T01:22:11.309467+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1212 · 2026-05-21T01:22:23.221905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1213 · 2026-05-21T01:22:23.931112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 709
}
```

</details>

---


### Tool call

_source line 1214 · 2026-05-21T01:22:29.927941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 1215 · 2026-05-21T01:22:30.633714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1216 · 2026-05-21T01:22:34.002067+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 1217 · 2026-05-21T01:22:34.667270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 665
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-21T01:22:38.384214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-21T01:22:39.089549+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1220 · 2026-05-21T01:22:43.065620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p32.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p32.png"
  }
}
```

</details>

---


### Tool result

_source line 1221 · 2026-05-21T01:22:43.721658+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1222 · 2026-05-21T01:22:46.990816+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p33.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p33.png"
  }
}
```

</details>

---


### Tool result

_source line 1223 · 2026-05-21T01:22:47.544541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1224 · 2026-05-21T01:22:51.219866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p34.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p34.png"
  }
}
```

</details>

---


### Tool result

_source line 1225 · 2026-05-21T01:22:51.221163+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1226 · 2026-05-21T01:22:59.424093+00:00_

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

_source line 1227 · 2026-05-21T01:22:59.525365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-21T01:23:03.296301+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
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
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-21T01:23:09.567654+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here are the key findings about ACL ARR 2025-2026 reviewer guidelines:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Review Requirements

The soundness scores must be justified by the text of the review. All papers recommended for Findings or main conference are expected to be sound and reproducible.

## Reviewer Guidelines and Compliance

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## New Policies for 2025

Starting in May 2025, ARR adopts a new policy on the 'highly irresponsible' (meta-)reviewers, including cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews.

The complete reviewer guidelines are available at the official ARR website at aclrollingreview.org/reviewerguidelines.


REMINDER: You MUST include the sources above in your 
…[truncated 47 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6271
}
```

</details>

---


### Tool call

_source line 1230 · 2026-05-21T01:23:13.337698+00:00_

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

_source line 1231 · 2026-05-21T01:23:13.488932+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1232 · 2026-05-21T01:23:18.762359+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions and scoring criteria. I need: 1) All scoring dimensions (soundness, excitement, overall assessment, etc.) with their scales and descriptions. 2) What each score level means. 3) Any specific instructions about what reviewers should evaluate. Return the full details."
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
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions and scoring criteria. I need: 1) All scoring dimensions (soundness, excitement, overall assessment, etc.) with their scales and descriptions. 2) What each score level means. 3) Any specific instructions about what reviewers should evaluate. Return the full details."
  }
}
```

</details>

---


### Tool result

_source line 1233 · 2026-05-21T01:23:24.644351+00:00_

# ARR Review Form Dimensions and Scoring Criteria

Based on the guidelines provided, I can identify the following review scoring dimensions:

## Three Primary Scoring Dimensions

**1. Soundness**
The guidelines state reviewers assess whether papers are "technically sound and appropriately scoped." Soundness scores "must be justified by the text of the review" - if you assign a low soundness rating without identifying substantial faults, your review lacks internal consistency.

**2. Excitement**
This dimension captures subjective personal interest, described as "orthogonal to the assessment of the soundness of the paper." A reviewer might find work technically sound but personally unexciting, or vice versa.

**3. Overall Assessment**
This represents "an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue." It's a "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact."

## Key Evaluation Instruction

The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," though reviewers may recommend main conference acceptance for papers they personally find unexciting if they recognize significant potential impact.

**Note:** The document doesn't specify exact numerical scales (1-5, 1-10, etc.) for these dimensions—only the conceptual framework and relationship between them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5881
}
```

</details>

---


### Tool call

_source line 1234 · 2026-05-21T01:23:33.194066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 soundness excitement overall assessment score scale 1-5"
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
    "query": "ACL ARR review form 2025 soundness excitement overall assessment score scale 1-5"
  }
}
```

</details>

---


### Tool result

_source line 1235 · 2026-05-21T01:23:39.834798+00:00_

Web search results for query: "ACL ARR review form 2025 soundness excitement overall assessment score scale 1-5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/acl-statistics/acl-2025-statistics/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ACL ARR review form for 2025:

## Three Score Categories

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score
The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

## Excitement Score
Personal preferences should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. Excitement scores reflect our personal taste, and so do not ne
…[truncated 628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6640
}
```

</details>

---


### Tool call

_source line 1236 · 2026-05-21T01:23:45.362517+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract ALL scoring dimensions, their exact numerical scales, and what each score level means. I need the complete review form with all fields, scores, and their descriptions. Include soundness scale, excitement scale, overall assessment scale, confidence scale, and any other dimensions."
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
    "prompt": "Extract ALL scoring dimensions, their exact numerical scales, and what each score level means. I need the complete review form with all fields, scores, and their descriptions. Include soundness scale, excitement scale, overall assessment scale, confidence scale, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 1237 · 2026-05-21T01:23:52.555241+00:00_

# ACL Rolling Review Form: Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all claims."
- **3**: "Acceptable: This study provides sufficient support for main claims."
- **2**: "Poor: Some main claims are not sufficiently supported."
- **1**: "Major Issues: Not yet sufficiently thorough to warrant publication."

## 3. Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points to others."
- **2**: "Potentially Interesting: does not resonate with me."
- **1**: "Not Exciting: does not resonate with me."

## 4. Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4.5**: Borderline Award
- **4**: Conference acceptance
- **3.5**: Borderline Conference
- **3**: Findings acceptance
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle
- **1.5**: Resubmit after next cycle
- **1**: Do not resubmit

## 5. Reproducibility
Scale: 1-5
- **5**: Readers could easily reproduce results
- **4**: Readers could mostly reproduce with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data
- **1**: Cannot reproduce results

## 6. Datasets Value
Scale: 1-5
- **5**: Enabling for research choices
- **4**: Useful for ongoing 
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7192
}
```

</details>

---


### Tool call

_source line 1238 · 2026-05-21T01:24:00.090841+00:00_

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

_source line 1239 · 2026-05-21T01:24:33.915474+00:00_

&lt;persisted-output>
Output too large (50.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/53952a4f-2a34-4cb3-82c9-7c7d08583f3a/tool-results/toolu_01NNwyxVwJXFekS7ybxWGif8.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 97, \"unique_cited_keys\": 58, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 48, \"online_not_found\": 2, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [\"chen2024agentre\", \"fan2024fsn\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 33824
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-21T01:24:38.308951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/53952a4f-2a34-4cb3-82c9-7c7d08583f3a/tool-results/toolu_01NNwyxVwJXFekS7ybxWGif8.txt",
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
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/53952a4f-2a34-4cb3-82c9-7c7d08583f3a/tool-results/toolu_01NNwyxVwJXFekS7ybxWGif8.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1241 · 2026-05-21T01:24:38.562772+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 97, \"unique_cited_keys\": 58, \"orphan_bib\": 2, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 48, \"online_not_found\": 2, \"online_mismatch\": 10}, \"cross_check\": {\"orphan_bib\": [\"chen2024agentre\", \"fan2024fsn\"], \"missing_bib\": [], \"orphan_count\": 2, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang...\", \
…[truncated 50130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-21T01:24:46.052310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-21T01:24:46.052976+00:00_

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
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 1662 chars]

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

_source line 1244 · 2026-05-21T01:24:51.577579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "offset": "80",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "offset": "80",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1245 · 2026-05-21T01:24:51.578231+00:00_

80	
81	\paragraph{Evaluation coverage.}
82	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
83	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated only on 8B-class models.
84	Scaling to smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
85	Composability with fine-tuned models is validated on SciERC, DocRED, and WikiEvents with Qwen3-8B and Llama-3.1-8B (RE: DR\,$\leq$\,0.09\%, R-F1 within $\pm$0.6\,pp; EE: RoV$\to$0\%, AC$\leq$0.8\%), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
86	WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split).
87	All main experiments use greedy decoding; our evaluation of beam search on the full SciERC test set (551 documents) and DocRED (50 zero-shot, 998 fine-tuned documents) across three models confirms compatibility (Appendices~\ref{app:sampling},~\ref{app:beam-search}), but comprehensive evaluation across all decoding configurations remains future work.
88	
89	\paragraph{Engineering considerations.}
90	Scalability benchmarks up to 200 entity types and 1,000 relations show constant 2--3\% inference overhead and sub-second compilation ($<$0.5\,s; Appendix~\ref{app:scalability}); however, the first-token uniqueness requirement for continuation masking may become a tokenizer-dependent bottleneck beyond this scale.
91	Our approach requires access to model logits for token-level masking, which excludes API-only models (e.g., GPT-4, Claude) where only output text is available; extending to API-only settings would require alternative enforcement mechanisms such as constrained sampling APIs or output reranking.
92	Continuation m
…[truncated 2028 chars]

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

_source line 1246 · 2026-05-21T01:26:52.284144+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
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
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1247 · 2026-05-21T01:26:52.334769+00:00_



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

_source line 1248 · 2026-05-21T01:26:57.569148+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1249 · 2026-05-21T01:26:57.569794+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-21T01:28:59.897168+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**审查侧重：新颖性 + 论文完整性 + 格式合规**\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 形式化贡献（可判定性分类 + pumping lemma 证明）有理论价值，工程执行扎实，但组件级新颖性有限（grammar layer = XGrammar 直接应用，semantic layer = 运行时类型检查），且正文超出 8 页限制。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claims 有充分实验支撑（DR reduction 94-100%），但 CF trade-off 未解决（CF 高达 12.02%），WikiEvents 结果基于 20 文档初步验证 |\n| Excitement | 2.5/5 | 形式化视角有趣（IE 约束的可判定性分析在该领域属首次），但实际方法是 XGrammar + 类型查找表的组合，算法层面无突破 |\n| Reproducibility | 4/5 | 超参数、prompt 模板、数据集划分、硬件配置等均有详细记录（Appendix G），代码承诺公开 |\n| Overall Assessment | 3.0 | Findings 级别：执行质量高、评估全面，但新颖性偏工程集成而非方法论突破 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 schema-aware IE 领域，仔细阅读了全文 34 页 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文超出 8 页限制\n- 具体位置：PDF 第 9 页，行号 653-660\n- 问题：Section 7 \"Discussion and Conclusion\" 从第 8 页底部开始，溢出至第 9 页（约 8 行文字）。LaTeX 源码在 Limitations 前使用 `\\clearpage`（main.tex line 69），确认结论文本确实在第 9 页。EMNLP 2026 / ARR 规定 long paper 正文严格 ≤ 8 页。\n- 为什么影响接收：ARR 明确规定 \"strict 8-page limit for main text\"。超页可能导致 desk reject 或 area chair 标记。\n- 建议修改方向：压缩 Section 6 (Related Work) 或 Section 7 (Discussion and Conclusion)，将结论完全收进第 8 页。Related Work 已有完整版本在 Appendix B，主文可进一步精简。\n\n**N2** [critical] 核心新颖性定位不清：系统集成 vs. 算法创新\n- 具体位置：Section 1 (Introduction), Section 3 (Method)\n- 问题：论文的核心贡献描述为 \"a two-layer constrained decoding framework guided by a decidability analysis\"（Section 1, contributions list）。但逐层拆解后：\n  - **Grammar layer**（§3.2）：将 JSON Schema 编译为 pushdown automaton，直接使用 XGrammar（Dong et al., 2025）。论文明确写到 \"A JSON Schema encoding Eq. (1) with enum constraints (E, R) is compiled into a pushdown automaton via XGrammar\"——这是对现有工具的应用，非方法创新。\n  - **Semantic layer**（§3.3）：运行时实体注册表 D + continuation masking。本质是一个有状态的类型查找表，在每个 token 位置做 domain/range 检查。概念上是 runtime type-checking 的直接实现。\n  - **Proposition 1**（§3.1）：domain/range 约束不是 context-free 的 pumping lemma 证明——这是真正的理论贡献，但它更多是 *motivation* 而非 *method*。\n- 论文缺少对 \"what is genuinely new here beyond combining XGrammar with a type-checking registry\" 的直接回应。Introduction 中的贡献列表（page 2）将 \"decidability analysis\" 和 \"composable layers\" 并列，但前者是分析结果、后者是工程集成。\n- 为什么影响接收：Excitement 评分的核心考量。如果 reviewer/AC 认为贡献主要是工程集成（well-executed but incremental），则难以进入主会议。\n- 建议修改方向：(1) 更清楚地分离理论贡献（decidability taxonomy, Prop 1, κ̄）和系统贡献（two-layer architecture）；(2) 直接论证为什么 semantic layer 的设计不是 trivial——例如，enabling dependency（§3.1 Corollary）意味着两层不能简单并行，composition 的正确性需要形式化保证；(3) 在 Related Work 中更明确地对比与 IterGen（Ugare et al., 2025）的 backtracking 方案，说明 OntoCoDec 的 forward-only + fallback 设计在效率和正确性上的取舍。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] DR↔CF trade-off 是结构性限制，削弱 \"near-eliminates violations\" 的核心声明\n- 具体位置：Abstract (\"near-eliminates DR (94-100% reduction)\"); Table 1 (CF 列); Limitations §Constraint scope; Appendix C (§C \"CF-DR Trade-off Analysis\")\n- 问题：Abstract 声称 \"near-eliminates DR\"，但 Table 1 显示在 Full S1 unconstrained 设置下，CF violations 从 0 增至 12.02%（Llama ScIERC），grammar-only CF 近零但 DR 仅减少 24%。Appendix C 的双因子分析（Figure 2）确认 DR 和 CF 反向相关（r = -0.366, p = 0.138, n=6）。论文自身承认 \"CF↔DR thus represents a fundamental trade-off in composable constraint systems\"（Limitations, line 74）。\n- 当 CF 被考虑时，总 violation rate（DR + CF）的净减少量远小于 94-100%。例如 Table 1 SciERC Llama Full S1：DR 从 13.37→0, 但 CF 从 0→12.02, 净 violation 减少仅 ~1.35pp。\n- 建议：Abstract 和 Introduction 中应同时报告 DR reduction 和 CF 增加，或使用一个综合指标（如 total violation rate）来避免选择性报告。\n\n**W2** [major] κ̄（constraint tightness）作为理论贡献的价值有限\n- 具体位置：§4.1 \"Constraint Tightness\"; Appendix N (κ̄ case study)\n- 问题：κ̄ 定义为 κ(r) = 1 - |σ(r)|/|E|² 的平均值，即 schema 允许的类型对占所有可能类型对的比例的补数。这是一个直觉明显的度量——schema 约束越紧（允许的类型越少），violation reduction 越大。论文承认 \"the dual-factor pattern motivates constrained decoding\"（Appendix C, p.21），但 κ̄ 本身并未提供超出直觉的洞见。\n- Appendix C 的回归分析（Figure 2, n=6）样本量太小，无法得出统计显著的结论（论文自身承认 \"n=6 is insufficient for statistical inference\"）。\n- 建议：将 κ̄ 定位为 \"diagnostic metric\"（论文在 Limitations 中已部分这样做）而非独立贡献。在 contributions list 中降低 κ̄ 的权重。\n\n**W3** [major] WikiEvents 事件抽取结果过于初步，不足以支撑 \"extension to event extraction\" 声明\n- 具体位置：§5.4 \"Extension to Event Extraction\"; Table 5\n- 问题：WikiEvents 评估仅覆盖 5 种 event types、27 种 entity types（论文原文 \"5 event types, 80 event types, 27 entity types\"——Table 5 标题说 n=246 zero-shot, n=20 fine-tuning）。Fine-tuning 仅 20 文档，论文自身称 \"results are preliminary due to the 20-document test set\"（§5.4）。Zero-shot 性能很低（ET/RV/DR 均有大量 violations），fine-tuning 结果虽然 RoV→0% 但样本太小。\n- 更重要的是，EE 的 schema 结构（event types → argument roles → entity types）比 RE 的（entity types → relation types → entity types）更复杂，但论文对 OntoCoDec 如何处理这种层次结构的讨论不足。\n- 建议：(1) 将 WikiEvents 结果明确标记为 \"preliminary/pilot study\"；(2) 在 Section 5.4 中更详细地讨论 EE schema 的约束编译过程和与 RE 的差异。\n\n**W4** [minor-major] 缺少与 supervised IE baselines 的对比\n- 具体位置：Tables 1-5\n- 问题：论文所有实验均在 LLM-based IE pipeline 内对比（unconstrained vs. constrained），但缺少与 supervised IE 系统（如 PURE/PL-Marker、SpERT (Eberts & Ulges, 2020)）的 F1 对比。虽然 OntoCoDec 的贡献是约束层而非 IE accuracy，但读者需要知道 constrained LLM pipeline 在 F1 上处于什么水平，才能判断 violation reduction 的实际价值。\n- 论文在 Appendix C 提到 \"supervised state-of-the-art systems on SciERC achieve approximately 49-53% relation F1 with full training data (Zhong and Chen, 2021)\"，但这是附录中的一句带过，未进入主文比较。\n- 建议：在 Table 1 或 Table 2 中加一行 supervised baseline 的 F1 作为 oracle/upper-bound 参考。\n\n---\n\n## 小问题（不影响接收）\n\n- **m1** [minor] 两个 orphan bib entries（chen2024agentre, fan2024fsn）未被引用，应清理。\n- **m2** [minor] Abstract 中 \"1-2% even after LoRA fine-tuning\" 与 Table 2 中 fine-tuned DR 数据（LoRA + S1: DR ≤ 0.09% on SciERC, ≤ 0.28% on DocRED）不完全一致。Abstract 的 \"1-2%\" 似乎指 unconstrained fine-tuning 的残余 violation rate，但表述容易误解为 constrained 后的残余。\n- **m3** [minor] Figure 1 的 overview 图过于抽象，难以传达两层架构的具体交互机制。建议增加一个 running example 的 figure，展示 grammar mask 和 semantic mask 在具体 token 位置如何交互。\n- **m4** [minor] Appendix O (pumping lemma proof) 跨 3 页（pp.32-34），对于一个相对直接的不可判定性证明来说偏长，部分辅助引理可压缩。\n- **m5** [minor] 引用格式：部分 arXiv preprint（如 formattax2026, dccd2026）在 OpenAlex 中未能验证——应确认这些论文确实存在且引用信息准确。\n\n---\n\n## Questions to Authors\n\n1. **Entity registry 与共指消解**：当同一实体在文档中以不同表面形式出现时（如 \"Barack Obama\" 和 \"Obama\"），entity registry D 是否将它们视为同一实体？如果是，如何确定共指？如果否，是否会导致同一实体被赋予不同类型？\n2. **Grammar-first fallback 的级联效应**：当 §4 中的 grammar-first fallback（S(t)∩G(t)=∅ 时跳过 semantic layer）触发时，被分配的类型可能违反 domain/range 约束。这些 fallback-induced CF violations 在后续 triple 的类型约束中是否会级联传播？\n3. **与 IterGen 的 backtracking 方案的实验对比**：论文在 Related Work 中讨论了 IterGen（Ugare et al., 2025），但未进行实验对比。是否有技术障碍阻止了这一对比？IterGen 的 backtracking 是否可以作为 OntoCoDec 的替代 semantic enforcement 策略？\n\n---\n\n## Missing References\n\n- **ASP/Markov Logic for structured IE constraints**: Riedel et al. (2009) \"Markov Logic Networks for Information Extraction\" 和相关 probabilistic constraint enforcement 工作。OntoCoDec 的 hard constraint approach 与 soft constraint approaches 的对比讨论缺失。\n- **Constrained beam search in NLG**: Anderson et al. (2017) \"Guided Open Vocabulary Image Captioning with Constrained Beam Search\" — 早期将约束融入 beam search 的工作，与 OntoCoDec 的 beam search compatibility (Appendix F) 相关。\n- **Type-constrained link prediction in KGE**: Krompaß et al. (2015) \"Type-Constrained Representation Learning in Knowledge Graphs\" — KG embedding 中的类型约束方法，虽然领域不同但概念相关。\n\n---\n\n## 主要优势\n\n1. **形式化分析有深度**：将 IE 类型约束映射到形式语言理论（Proposition 1 的 pumping lemma 证明）是该领域的首次尝试，提供了理论 grounding 来解释为什么 grammar-only constrained decoding 不足以处理 domain/range 约束。\n2. **实验评估极为全面**：3 个数据集 × 4 个模型 × 多种解码策略 × zero-shot + fine-tuning × 大量消融实验（5-way ablation, per-relation analysis, document length breakdown, prompt sensitivity, sampling robustness, beam search compatibility, scalability）。附录从 A 到 O，覆盖了几乎所有可预见的 reviewer 问题。\n3. **诚实的 Limitations 讨论**：CF trade-off、WikiEvents 初步性、模型依赖性、工程约束（API-only models 不适用）等均有坦诚讨论，这在投稿论文中并不常见。\n4. **Reproducibility 准备充分**：Prompt 模板（Appendix A）、超参数（Appendix G）、随机种子验证（Table 20）、硬件规格均有记录。\n5. **Cross-dataset generalization**：在 SciERC（学术）、DocRED（Wikipedia）、WikiEvents（新闻事件）三种不同领域验证，展示了方法的通用性。\n\n---\n\n## 格式合规检查\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 页数 ≤ 8 | ❌ | 正文溢出至第 9 页（8 行结论文字）|\n| 匿名 | ✅ | `\\author{Anonymous ACL submission}`，无可识别自引 |\n| ACL 模板 + [review] | ✅ | `\\usepackage[review]{acl}`（main.tex line 3）|\n| Limitations section | ✅ | 独立 section，在 conclusion 后、references 前（main.tex lines 70-94）|\n| Ethics Statement | ✅ | 存在（main.tex lines 98-103）|\n| ARR Checklist | ✅ | 已填写（main.tex line 106, pages 11-12）|\n| 附录双栏 | ✅ | 所有附录页面（15-34）均为双栏格式 |\n| natbib 引用 | ✅ | 通过 acl package 使用 natbib |\n| 引用完整性 | ✅ | 58/60 bib entries 被引用，0 missing bib，48/60 online verified |\n",
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
    "text": "\n## Reviewer 2 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**审查侧重：新颖性 + 论文完整性 + 格式合规**\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 (Findings)\n**一句话总结**: 形式化贡献（可判定性分类 + pumping lemma 证明）有理论价值，工程执行扎实，但组件级新颖性有限（grammar layer = XGrammar 直接应用，semantic layer = 运行时类型检查），且正文超出 8 页限制。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 主要 claims 有充分实验支撑（DR reduction 94-100%），但 CF trade-off 未解决（CF 高达 12.02%），WikiEvents 结果基于 20 文档初步验证 |\n| Excitement | 2.5/5 | 形式化视角有趣（IE 约束的可判定性分析在该领域属首次），但实际方法是 XGrammar + 类型查找表的组合，算法层面无突破 |\n| Reproducibility | 4/5 | 超参数、prompt 模板、数据集划分、硬件配置等均有详细记录（Appendix G），代码承诺公开 |\n| Overall Assessment | 3.0 | Findings 级别：执行质量高、评估全面，但新颖性偏工程集成而非方法论突破 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 schema-aware IE 领域，仔细阅读了全文 34 页 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 正文超出 8 页限制\n- 具体位置：PDF 第 9 页，行号 653-660\n- 问题：Section 7 \"Discussion and Conclusion\" 从第 8 页底部开始，溢出至第 9 页（约 8 行文字）。LaTeX 源码在 Limitations 前使用 `\\clearpage`（main.tex line 69），确认结论文本确实在第 9 页。EMNLP 2026 / ARR 规定 long paper 正文严格 ≤ 8 页。\n- 为什么影响接收：ARR 明确规定 \"strict 8-page limit for main text\"。超页可能导致 desk reject 或 area chair 标记。\n- 建议修改方向：压缩 Section 6 (Related Work) 或 Section 7 (Discussion and Conclusion)，将结论完全收进第 8 页。Related Work 已有完整版本在 Appendix B，主文可进一步精简。\n\n**N2** [critical] 核心新颖性定位不清：系统集成 vs. 算法创新\n- 具体位置：Section 1 (Introduction), Section 3 (Method)\n- 问题：论文的核心贡献描述为 \"a two-layer constrained decoding framework guided by a decidability analysis\"（Section 1, contributions list）。但逐层拆解后：\n  - **Grammar layer**（§3.2）：将 JSON Schema 编译为 pushdown automaton，直接使用 XGrammar（Dong et al., 2025）。论文明确写到 \"A JSON Schema encoding Eq. (1) with enum constraints (E, R) is compiled into a pushdown automaton via XGrammar\"——这是对现有工具的应用，非方法创新。\n  - **Semantic layer**（§3.3）：运行时实体注册表 D + continuation masking。本质是一个有状态的类型查找表，在每个 token 位置做 domain/range 检查。概念上是 runtime type-checking 的直接实现。\n  - **Proposition 1**（§3.1）：domain/range 约束不是 context-free 的 pumping lemma 证明——这是真正的理论贡献，但它更多是 *motivation* 而非 *method*。\n- 论文缺少对 \"what is genuinely new here beyond combining XGrammar with a type-checking registry\" 的直接回应。Introduction 中的贡献列表（page 2）将 \"decidability analysis\" 和 \"composable layers\" 并列，但前者是分析结果、后者是工程集成。\n- 为什么影响接收：Excitement 评分的核心考量。如果 reviewer/AC 认为贡献主要是工程集成（well-executed but incremental），则难以进入主会议。\n- 建议修改方向：(1) 更清楚地分离理论贡献（decidability taxonomy, Prop 1, κ̄）和系统贡献（two-layer architecture）；(2) 直接论证为什么 semantic layer 的设计不是 trivial——例如，enabling dependency（§3.1 Corollary）意味着两层不能简单并行，composition 的正确性需要形式化保证；(3) 在 Related Work 中更明确地对比与 IterGen（Ugare et al., 2025）的 backtracking 方案，说明 OntoCoDec 的 forward-only + fallback 设计在效率和正确性上的取舍。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] DR↔CF trade-off 是结构性限制，削弱 \"near-eliminates violations\" 的核心声明\n- 具体位置：Abstract (\"near-eliminates DR (94-100% reduction)\"); Table 1 (CF 列); Limitations §Constraint scope; Appendix C (§C \"CF-DR Trade-off Analysis\")\n- 问题：Abstract 声称 \"near-eliminates DR\"，但 Table 1 显示在 Full S1 unconstrained 设置下，CF violations 从 0 增至 12.02%（Llama ScIERC），grammar-only CF 近零但 DR 仅减少 24%。Appendix C 的双因子分析（Figure 2）确认 DR 和 CF 反向相关（r = -0.366, p = 0.138, n=6）。论文自身承认 \"CF↔DR thus represents a fundamental trade-off in composable constraint systems\"（Limitations, line 74）。\n- 当 CF 被考虑时，总 violation rate（DR + CF）的净减少量远小于 94-100%。例如 Table 1 SciERC Llama Full S1：DR 从 13.37→0, 但 CF 从 0→12.02, 净 violation 减少仅 ~1.35pp。\n- 建议：Abstract 和 Introduction 中应同时报告 DR reduction 和 CF 增加，或使用一个综合指标（如 total violation rate）来避免选择性报告。\n\n**W2** [major] κ̄（constraint tightness）作为理论贡献的价值有限\n- 具体位置：§4.1 \"Constraint Tightness\"; Appendix N (κ̄ case study)\n- 问题：κ̄ 定义为 κ(r) = 1 - |σ(r)|/|E|² 的平均值，即 schema 允许的类型对占所有可能类型对的比例的补数。这是一个直觉明显的度量——schema 约束越紧（允许的类型越少），violation reduction 越大。论文承认 \"the dual-factor pattern motivates constrained decoding\"（Appendix C, p.21），但 κ̄ 本身并未提供超出直觉的洞见。\n- Appendix C 的回归分析（Figure 2, n=6）样本量太小，无法得出统计显著的结论（论文自身承认 \"n=6 is insufficient for statistical inference\"）。\n- 建议：将 κ̄ 定位为 \"diagnostic metric\"（论文在 Limitations 中已部分这样做）而非独立贡献。在 contributions list 中降低 κ̄ 的权重。\n\n**W3** [major] WikiEvents 事件抽取结果过于初步，不足以支撑 \"extension to event extraction\" 声明\n- 具体位置：§5.4 \"Extension to Event Extraction\"; Table 5\n- 问题：WikiEvents 评估仅覆盖 5 种 event types、27 种 entity types（论文原文 \"5 event types, 80 event types, 27 entity types\"——Table 5 标题说 n=246 zero-shot, n=20 fine-tuning）。Fine-tuning 仅 20 文档，论文自身称 \"results are preliminary due to the 20-document test set\"（§5.4）。Zero-shot 性能很低（ET/RV/DR 均有大量 violations），fine-tuning 结果虽然 RoV→0% 但样本太小。\n- 更重要的是，EE 的 schema 结构（event types → argument roles → entity types）比 RE 的（entity types → relation types → entity types）更复杂，但论文对 OntoCoDec 如何处理这种层次结构的讨论不足。\n- 建议：(1) 将 WikiEvents 结果明确标记为 \"preliminary/pilot study\"；(2) 在 Section 5.4 中更详细地讨论 EE schema 的约束编译过程和与 RE 的差异。\n\n**W4** [minor-major] 缺少与 supervised IE baselines 的对比\n- 具体位置：Tables 1-5\n- 问题：论文所有实验均在 LLM-based IE pipeline 内对比（unconstrained vs. constrained），但缺少与 supervised IE 系统（如 PURE/PL-Marker、SpERT (Eberts & Ulges, 2020)）的 F1 对比。虽然 OntoCoDec 的贡献是约束层而非 IE accuracy，但读者需要知道 constrained LLM pipeline 在 F1 上处于什么水平，才能判断 violation reduction 的实际价值。\n- 论文在 Appendix C 提到 \"supervised state-of-the-art systems on SciERC achieve approximately 49-53% relation F1 with full training data (Zhong and Chen, 2021)\"，但这是附录中的一句带过，未进入主文比较。\n- 建议：在 Table 1 或 Table 2 中加一行 supervised baseline 的 F1 作为 oracle/upper-bound 参考。\n\n---\n\n## 小问题（不影响接收）\n\n- **m1** [minor] 两个 orphan bib entries（chen2024agentre, fan2024fsn）未被引用，应清理。\n- **m2** [minor] Abstract 中 \"1-2% even after LoRA fine-tuning\" 与 Table 2 中 fine-tuned DR 数据（LoRA + S1: DR ≤ 0.09% on SciERC, ≤ 0.28% on DocRED）不完全一致。Abstract 的 \"1-2%\" 似乎指 unconstrained fine-tuning 的残余 violation rate，但表述容易误解为 constrained 后的残余。\n- **m3** [minor] Figure 1 的 overview 图过于抽象，难以传达两层架构的具体交互机制。建议增加一个 running example 的 figure，展示 grammar mask 和 semantic mask 在具体 token 位置如何交互。\n- **m4** [minor] Appendix O (pumping lemma proof) 跨 3 页（pp.32-34），对于一个相对直接的不可判定性证明来说偏长，部分辅助引理可压缩。\n- **m5** [minor] 引用格式：部分 arXiv preprint（如 formattax2026, dccd2026）在 OpenAlex 中未能验证——应确认这些论文确实存在且引用信息准确。\n\n---\n\n## Questions to Authors\n\n1. **Entity registry 与共指消解**：当同一实体在文档中以不同表面形式出现时（如 \"Barack Obama\" 和 \"Obama\"），entity registry D 是否将它们视为同一实体？如果是，如何确定共指？如果否，是否会导致同一实体被赋予不同类型？\n2. **Grammar-first fallback 的级联效应**：当 §4 中的 grammar-first fallback（S(t)∩G(t)=∅ 时跳过 semantic layer）触发时，被分配的类型可能违反 domain/range 约束。这些 fallback-induced CF violations 在后续 triple 的类型约束中是否会级联传播？\n3. **与 IterGen 的 backtracking 方案的实验对比**：论文在 Related Work 中讨论了 IterGen（Ugare et al., 2025），但未进行实验对比。是否有技术障碍阻止了这一对比？IterGen 的 backtracking 是否可以作为 OntoCoDec 的替代 semantic enforcement 策略？\n\n---\n\n## Missing References\n\n- **ASP/Markov Logic for structured IE constraints**: Riedel et al. (2009) \"Markov Logic Networks for Information Extraction\" 和相关 probabilistic constraint enforcement 工作。OntoCoDec 的 hard constraint approach 与 soft constraint approaches 的对比讨论缺失。\n- **Constrained beam search in NLG**: Anderson et al. (2017) \"Guided Open Vocabulary Image Captioning with Constrained Beam Search\" — 早期将约束融入 beam search 的工作，与 OntoCoDec 的 beam search compatibility (Appendix F) 相关。\n- **Type-constrained link prediction in KGE**: Krompaß et al. (2015) \"Type-Constrained Representation Learning in Knowledge Graphs\" — KG embedding 中的类型约束方法，虽然领域不同但概念相关。\n\n---\n\n## 主要优势\n\n1. **形式化分析有深度**：将 IE 类型约束映射到形式语言理论（Proposition 1 的 pumping lemma 证明）是该领域的首次尝试，提供了理论 grounding 来解释为什么 grammar-only constrained decoding 不足以处理 domain/range 约束。\n2. **实验评估极为全面**：3 个数据集 × 4 个模型 × 多种解码策略 × zero-shot + fine-tuning × 大量消融实验（5-way ablation, per-relation analysis, document length breakdown, prompt sensitivity, sampling robustness, beam search compatibility, scalability）。附录从 A 到 O，覆盖了几乎所有可预见的 reviewer 问题。\n3. **诚实的 Limitations 讨论**：CF trade-off、WikiEvents 初步性、模型依赖性、工程约束（API-only models 不适用）等均有坦诚讨论，这在投稿论文中并不常见。\n4. **Reproducibility 准备充分**：Prompt 模板（Appendix A）、超参数（Appendix G）、随机种子验证（Table 20）、硬件规格均有记录。\n5. **Cross-dataset generalization**：在 SciERC（学术）、DocRED（Wikipedia）、WikiEvents（新闻事件）三种不同领域验证，展示了方法的通用性。\n\n---\n\n## 格式合规检查\n\n| 检查项 | 结果 | 备注 |\n|--------|------|------|\n| 页数 ≤ 8 | ❌ | 正文溢出至第 9 页（8 行结论文字）|\n| 匿名 | ✅ | `\\author{Anonymous ACL submission}`，无可识别自引 |\n| ACL 模板 + [review] | ✅ | `\\usepackage[review]{acl}`（main.tex line 3）|\n| Limitations section | ✅ | 独立 section，在 conclusion 后、references 前（main.tex lines 70-94）|\n| Ethics Statement | ✅ | 存在（main.tex lines 98-103）|\n| ARR Checklist | ✅ | 已填写（main.tex line 106, pages 11-12）|\n| 附录双栏 | ✅ | 所有附录页面（15-34）均为双栏格式 |\n| natbib 引用 | ✅ | 通过 acl package 使用 natbib |\n| 引用完整性 | ✅ | 58/60 bib entries 被引用，0 missing bib，48/60 online verified |\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-21T01:29:04.172249+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4275
}
```

</details>

---


### Assistant

_source line 1252 · 2026-05-21T01:29:17.314389+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)。主要发现：

1. **格式违规 [critical]**：正文溢出至第 9 页（8 行结论文字），违反 EMNLP 2026 严格 8 页限制
2. **新颖性定位不清 [critical]**：组件级创新有限（grammar layer = XGrammar 应用，semantic layer = 运行时类型检查），系统集成 vs. 算法创新的界限模糊
3. **DR↔CF trade-off [major]**：约束强制减少 DR 但引入 CF（高达 12.02%），Abstract 的 "near-eliminates" 声明有选择性报告之嫌
4. **κ̄ 贡献有限 [major]**：定义直觉明显，回归分析样本量不足（n=6）
5. **WikiEvents 初步 [major]**：仅 20 文档 fine-tuning 评估

**优势**：形式化分析（Proposition 1 pumping lemma）有真正理论贡献；实验评估极全面（34 页含 15 个附录）；Limitations 讨论诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 27

## Round 27

20 recorded events


### User

_source line 1253 · 2026-05-21T01:30:00.141130+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 审稿意见

### 总体评分
Overall: 3.0 / 5（Findings），Confidence: 4 / 5

### 官方维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | Decidability 分析和证明基本严谨，但"guarantee"措辞与 fallback 机制存在内在矛盾；κ̄ 分析数据点不足（n=6）|
| Excitement | 3.0 / 5 | Decidability-guided 设计在 IE constrained decoding 中有新意，但缺乏 baseline 对比难以评估边际贡献 |
| Reproducibility | 4.0 / 5 | 附录详尽，声称开源 |
| Clarity | 3.5 / 5 | 结构清晰但信息密度极高，enabling dependency 主文解释不充分 |

### Must-Fix 问题

**N1** [critical] 缺少与 constrained-decoding 竞争方法的实验对比
- 论文在 Related Work 中详细讨论了 BoostCD、CRANE、IterGen、GCD、EnriCo，但实验中唯一对比是 unconstrained decoding 和 post-hoc filtering。
- 尤其 BoostCD 和 GCD 同样基于 grammar-constrained decoding 处理 IE 任务，且在 SciERC 上有结果。
- 建议至少在 SciERC 上与 GCD 和 BoostCD 做 head-to-head 对比（R-F1、DR、CF、latency）。

**N2** [critical] "Guarantee" 措辞与实际机制不匹配
- Abstract ("formal guarantees at each layer")、Section 1 ("formal guarantees") 与 Section 3.3 ("best-effort pair-based enforcement")、Section 3.4 ("grammar-first fallback") 存在矛盾。
- 三个保证缺口：(a) grammar-first fallback 时 semantic layer 被跳过；(b) Level 3 constraints 未强制；(c) 残余 CF 0.08-0.35%。
- 建议将"guarantee"替换为"enforcement"或"near-elimination"。

**N3** [major] WikiEvents 评估统计效能不足
- Fine-tuning 仅 20 篇文档（n=20），结论基于此的 bootstrap CI 可信度有限。
- 建议明确标记为"indicative only"或在完整测试集上报告。

**N4** [major] 70B 评估不足以支撑广泛声称
- 完整评估仅覆盖 7-8B 模型，70B 仅 1 个模型、无 ablation、无 fine-tuning。
- Abstract "applicable to autoregressive LMs" 过宽。

### Should-Fix 问题

**W1** [warning] κ̄ 基于 n=6 数据点的关联分析
- Figure 2 仅 4 个 model-dataset 组合。论文承认 p>0.05，但 §1 仍列为主要贡献。

**W2** [warning] Fallback 机制与核心 claim 的张力未充分分析
- 未分析 residual DR violations 中有多少源自 fallback 事件。
- 建议追踪 residual violations 到 fallback vs non-fallback positions。

**W3** [warning] S1 vs S2 配置选择缺乏充分论证
- S2 R-F1 略高但 CF 更差，cost-benefit 分析缺失。

**W4** [warning] 仅英语数据集评估
- 跨语言泛化是开放问题。Limitations 未明确标注语言覆盖缺口。

**W5** [warning] Post-hoc filtering 对比可能不够公平
- post-hoc correction（替换而非丢弃）可能是更公平的 baseline。

### 小问题
- 页数溢出（~8行结论在第9页）
- Table 1 "Tgt." 列含义不直观
- Enabling dependency 概念在主文中未正式定义
- Figure 1 信息密度高，visual hierarchy 不够清晰
- Orphan bib entries（chen2024agentre, fan2024fsn）
- 引用格式 encoding mismatch

### 主要优势
1. Decidability taxonomy 是真正的理论贡献
2. Ablation 设计全面（5-way + 4-way fine-tuned）
3. Fine-tuning composability 有实际价值
4. 附录极其详尽（24页）
5. DR 消减效果显著
6. 统计实践良好

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

_source line 1254 · 2026-05-21T01:30:38.093529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1255 · 2026-05-21T01:30:38.144422+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

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

_source line 1256 · 2026-05-21T01:30:43.744749+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-2,5-6,8-10",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-2,5-6,8-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-21T01:30:44.901992+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 524.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.3}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 56.6}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.6}], \"total_pages\": 34, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1157
}
```

</details>

---


### Tool call

_source line 1258 · 2026-05-21T01:30:48.631743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1259 · 2026-05-21T01:30:49.388414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-21T01:30:57.033795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-21T01:30:57.687568+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-21T01:31:02.238579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-21T01:31:03.095631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-21T01:31:07.389878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-21T01:31:08.148094+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-21T01:31:12.946841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-21T01:31:13.940628+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 993
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-21T01:32:59.845022+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 缺少与 constrained-decoding 竞争方法的实验对比**\n\n同意这是论文最显著的实验缺陷。论文 Related Work（Section 6, p.8）详细讨论了 GCD、BoostCD、IterGen、EnriCo，但实验中唯一 baseline 是 unconstrained vs. OntoCoDec 的内部消融（Table 1 五路消融）和 post-hoc filtering（§5.1 最后一段）。\n\n需要补充一点：直接对比存在技术复杂性。GCD（Geng et al., 2023）使用 grammar-constrained decoding 但不处理 domain/range 约束——它在 OntoCoDec 的 decidability taxonomy 中属于 Level 1-2（§3.1），而 OntoCoDec 的核心贡献是 Level 2 的 semantic layer。因此 GCD 的 grammar-only 结果本质上就是论文 Table 1 中 \"Grammar\" 行（grammar-only ablation）。论文在 §5.1 提到 \"grammar-only represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\" —— 这隐含了 GCD 对比，但应当显式化。\n\nBoostCD 的情况更棘手：它 boost constrained + unconstrained 分布，其 DR 减少机制与 OntoCoDec 完全不同。但既然论文声称 OntoCoDec \"超越\"这些方法，至少应提供 SciERC 上的 head-to-head 数字。\n\n**[AGREE] R1-N2: \"Guarantee\" 措辞与实际机制不匹配**\n\n完全同意。我在自己的审稿中也注意到了这一矛盾（我的 N2 关于新颖性定位）。具体证据：\n\n- Abstract (p.1): \"formal guarantees at each layer\" \n- Section 2 (p.2): \"formal enforcement with formal guarantees at each level\"\n- 但 Section 4 (p.4): \"grammar-first fallback\" 在 S(t)∩G(t)=∅ 时跳过 semantic layer，此时类型约束不被强制\n- Section 3.3 (p.3): semantic layer 使用 \"best-effort pair-based enforcement\"\n- Table 1 (p.6): Fine-tuned Full S1 仍有残余 CF 0.08-9.90%\n\n\"Guarantee\" 一词暗示零 residual violations，但数据显示这并非如此。R1 建议改为 \"enforcement\" 或 \"near-elimination\" 是合理的。论文在 Limitations（p.10）中诚实地讨论了这些缺口，但 Abstract/Introduction 的措辞应与 Limitations 保持一致。\n\n**[AGREE] R1-N3: WikiEvents 评估统计效能不足**\n\n完全同意，这与我自己的 W3 一致。Fine-tuning 仅 20 文档（§5.4, p.7: \"results are preliminary due to the 20-document test set\"），论文自身已承认。补充一个 R1 未提到的细节：WikiEvents zero-shot 评估（Table 5, n=246）规模尚可，但 fine-tuning composability 验证（n=20）确实不足以得出可靠结论。建议至少在正文中标注 \"preliminary/pilot\" 以管理读者预期。\n\n**[REBUT] R1-N4: 70B 评估不足以支撑广泛声称**\n\n部分不同意 R1 将此列为 Must-Fix。\n\n理由：(1) Abstract 的表述是 \"applicable to autoregressive LMs with logits access\"（p.1），这是对方法适用范围的事实性声明（只要有 logit access 就能用），不是性能保证。OntoCoDec 的约束编译是模型无关的——grammar layer 通过 XGrammar 在 token 层面操作，semantic layer 通过 entity registry 跟踪已生成内容。两层均不依赖模型参数或架构细节。\n\n(2) 论文确实提供了 70B 结果（Table 4, p.7: Llama-3.1-70B 在 SciERC 和 DocRED 上的 zero-shot 评估），虽然没有 fine-tuning ablation，但显示了相同的 DR 消减模式。Table 4 显示 Llama-3.1-70B 在 SciERC 上 DR 从 56.97→1.50（grammar）→0（Full S1），在 DocRED 上 DR 30.77→16.03→0.17。约束机制在 70B 上的有效性是可验证的。\n\n(3) 更重要的 gap 是 Mistral 在 Table 4 中的表现差异（SciERC 零 violations 但 DocRED zero-shot 后 CF 很高），这表明 model calibration 而非 model scale 是关键变量——论文在 §5.3 和 Limitations 中充分讨论了这一点。\n\n建议：将 N4 降为 Should-Fix。可以在 Limitations 中加一句明确承认 70B scale 验证有限，但不需要改 Abstract 的适用范围声明。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: κ̄ 基于 n=6 数据点的关联分析**\n\n完全同意，与我的 W2 一致。论文自身在 Appendix C (p.21) 承认 \"n=6 is insufficient for statistical inference on this correlation\"。n=6 的回归分析（Figure 2）不能支撑因果或强相关性结论。κ̄ 应被定位为 diagnostic metric 而非独立理论贡献。\n\n**[AGREE] R1-W2: Fallback 机制与核心 claim 的张力未充分分析**\n\n同意。这是一个我在第一轮审稿中未充分关注的有价值观察。论文在 Appendix C (p.19-20) 讨论了 CF dual mechanisms（\"Grammar-first fallback\" 和 \"Grammar-first\"），也在 Limitations (p.10, §Constraint scope) 讨论了 CF↔DR trade-off，但缺少的关键分析是：**residual DR violations（如 Table 10 中 fine-tuned 设置下的 36 个残余 violations）有多少发生在 fallback 位置**。\n\nAppendix D (p.25, Table 13) 提供了 per-relation violation breakdown，但按 violation type（entity type error, schema coverage gap 等）分类，不是按 fallback vs non-fallback 位置分类。追踪 fallback 事件与 residual violations 的关联性将直接回答 \"fallback 是否是 residual DR 的主要来源\" 这一问题。\n\n**[REBUT] R1-W3: S1 vs S2 配置选择缺乏充分论证**\n\n部分不同意。论文在 §5.1 (p.5) 提供了明确的比较：\"S1 vs S2. S2 achieves comparable DR (0.97%) but lower R-F1 (8.03 vs. 8.36) without resolving CF (8.03% vs. 9.90%); we adopt S1.\" 这给出了三个维度（DR, R-F1, CF）的对比，结论清晰：S1 在 R-F1 和 CF 上均优于 S2，DR 可比。\n\n不过，R1 要求更深入的 cost-benefit 分析也有道理——尤其是 S2 的两阶段 pipeline（§3.4: \"A first pass extracts entities; these compile an input-dependent grammar for the second pass\"）在特定场景（如 entity types 非常多时）可能有优势。这属于 minor improvement 而非 must-fix。\n\n**[AGREE] R1-W4: 仅英语数据集评估**\n\n同意。论文 Limitations section (p.10) 在 \"Engineering considerations\" 段讨论了 tokenizer 依赖性和 API-only 模型限制，但未明确提及语言覆盖缺口。SciERC（英语学术文本）、DocRED（英语 Wikipedia）、WikiEvents（英语新闻）均为英语。对于依赖 subword tokenization 的 continuation masking 机制（§3.3），跨语言泛化（尤其中日韩等非空格分词语言）是一个实质性开放问题。应在 Limitations 中加一句明确标注。\n\n**[AGREE] R1-W5: Post-hoc filtering 对比可能不够公平**\n\n同意。论文的 post-hoc filtering baseline（§5.1, p.5: \"Post-hoc filtering achieves DR→0% but with 15-74% rejection rates\"）是 discard-based（丢弃 invalid triples），而非 correction-based（将 invalid types 替换为最近的 valid type）。\n\n一个 post-hoc correction baseline（如用 embedding 距离最近的合法类型替换违规类型）可能在 DR 和 F1 之间取得比 discard 更好的平衡，从而构成更强的 baseline。论文在 Appendix C (p.22, \"Post-Hoc Filtering: Extended Comparison\", Table 11) 提供了更详细的 post-hoc 分析，但仍是 discard-based。\n\n不过，需要指出：post-hoc correction 作为 baseline 的公平性也有争议——因为 correction 需要额外的 type similarity 信息（如 type embedding），这引入了 OntoCoDec 未使用的外部知识。论文的 discard-based filtering 是一个 assumption-minimal 的 baseline。\n\n---\n\n### 小问题\n\n**[AGREE]** 页数溢出（~8行结论在第9页）：与我的 N1 一致，我将其列为 critical。\n\n**[AGREE]** Table 1 \"Tgt.\" 列含义不直观：确实，\"Tgt.\" 代表 \"Target\"（全部 violations 为 0 的目标），但未在表注中解释。\n\n**[AGREE]** Enabling dependency 概念在主文中未正式定义：§3.1 Corollary 提到 \"the enabling dependency is necessary\" 但 enabling dependency 本身（grammar layer 不能替代 semantic layer）在主文中仅用自然语言描述，没有形式化定义。\n\n**[AGREE]** Figure 1 信息密度高：与我的 m3 一致。\n\n**[AGREE]** Orphan bib entries：与我的 m1 一致。\n\n**[AGREE]** 引用格式 encoding mismatch：verify_references 工具确认 10/60 entries 有 minor mismatches（主要是作者姓名编码，如 Šakota vs Sakota），2 entries 在 OpenAlex 中未找到（regino2025kgcurator, formattax2026）。\n\n---\n\n### 对 R1 主要优势的回应\n\nR1 列出的 6 项优势与我的评估基本一致：\n\n1. **Decidability taxonomy 是真正的理论贡献** — 完全同意，这是论文最显著的学术贡献。\n2. **Ablation 设计全面** — 同意，5-way ablation (Table 1) + 4-way fine-tuned ablation (Table 10) 设计精良。\n3. **Fine-tuning composability 有实际价值** — 同意，Table 2 显示 LoRA fine-tuning 后约束仍然有效（DR ≤ 0.09% on SciERC）。\n4. **附录极其详尽** — 同意，24 页附录覆盖从 prompts 到 pumping lemma 证明的几乎所有细节。\n5. **DR 消减效果显著** — 同意，但需加 caveat：在 favorable conditions 下（LoRA + beam S1）。\n6. **统计实践良好** — 同意，bootstrap CI、cross-seed validation (Table 20) 等。\n\n---\n\n### 总结\n\nR1 与 R2（我）在以下关键判断上一致：\n- **Overall 3.0 (Findings)**：执行质量高但新颖性偏增量\n- **Soundness 3.5**：主要 claims 有支撑但存在 guarantee/fallback 矛盾\n- **WikiEvents 初步性**：两位 reviewer 均标记\n- **κ̄ 样本量不足**：两位 reviewer 均标记\n- **页数超限**：两位 reviewer 均标记\n\n两位 reviewer 的分歧点：\n- **R1-N4 (70B 评估)**：R1 列为 Must-Fix，我认为应降为 Should-Fix。Abstract 的 \"applicable to autoregressive LMs\" 是方法适用范围声明而非性能保证，且 Table 4 已提供 70B 验证数据。\n- **R1-W3 (S1 vs S2 选择)**：R1 认为缺乏论证，我认为 §5.1 已提供足够的三维度对比。\n- **Baseline 对比 (R1-N1)**：R1 标记为最严重的 critical issue。我同意其重要性，但补充指出 grammar-only ablation 隐含了 GCD 对比——论文应将此显式化而非要求完全重新实验。\n",
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
    "text": "\n## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 缺少与 constrained-decoding 竞争方法的实验对比**\n\n同意这是论文最显著的实验缺陷。论文 Related Work（Section 6, p.8）详细讨论了 GCD、BoostCD、IterGen、EnriCo，但实验中唯一 baseline 是 unconstrained vs. OntoCoDec 的内部消融（Table 1 五路消融）和 post-hoc filtering（§5.1 最后一段）。\n\n需要补充一点：直接对比存在技术复杂性。GCD（Geng et al., 2023）使用 grammar-constrained decoding 但不处理 domain/range 约束——它在 OntoCoDec 的 decidability taxonomy 中属于 Level 1-2（§3.1），而 OntoCoDec 的核心贡献是 Level 2 的 semantic layer。因此 GCD 的 grammar-only 结果本质上就是论文 Table 1 中 \"Grammar\" 行（grammar-only ablation）。论文在 §5.1 提到 \"grammar-only represents the ceiling of grammar-constrained decoding (Geng et al., 2023)\" —— 这隐含了 GCD 对比，但应当显式化。\n\nBoostCD 的情况更棘手：它 boost constrained + unconstrained 分布，其 DR 减少机制与 OntoCoDec 完全不同。但既然论文声称 OntoCoDec \"超越\"这些方法，至少应提供 SciERC 上的 head-to-head 数字。\n\n**[AGREE] R1-N2: \"Guarantee\" 措辞与实际机制不匹配**\n\n完全同意。我在自己的审稿中也注意到了这一矛盾（我的 N2 关于新颖性定位）。具体证据：\n\n- Abstract (p.1): \"formal guarantees at each layer\" \n- Section 2 (p.2): \"formal enforcement with formal guarantees at each level\"\n- 但 Section 4 (p.4): \"grammar-first fallback\" 在 S(t)∩G(t)=∅ 时跳过 semantic layer，此时类型约束不被强制\n- Section 3.3 (p.3): semantic layer 使用 \"best-effort pair-based enforcement\"\n- Table 1 (p.6): Fine-tuned Full S1 仍有残余 CF 0.08-9.90%\n\n\"Guarantee\" 一词暗示零 residual violations，但数据显示这并非如此。R1 建议改为 \"enforcement\" 或 \"near-elimination\" 是合理的。论文在 Limitations（p.10）中诚实地讨论了这些缺口，但 Abstract/Introduction 的措辞应与 Limitations 保持一致。\n\n**[AGREE] R1-N3: WikiEvents 评估统计效能不足**\n\n完全同意，这与我自己的 W3 一致。Fine-tuning 仅 20 文档（§5.4, p.7: \"results are preliminary due to the 20-document test set\"），论文自身已承认。补充一个 R1 未提到的细节：WikiEvents zero-shot 评估（Table 5, n=246）规模尚可，但 fine-tuning composability 验证（n=20）确实不足以得出可靠结论。建议至少在正文中标注 \"preliminary/pilot\" 以管理读者预期。\n\n**[REBUT] R1-N4: 70B 评估不足以支撑广泛声称**\n\n部分不同意 R1 将此列为 Must-Fix。\n\n理由：(1) Abstract 的表述是 \"applicable to autoregressive LMs with logits access\"（p.1），这是对方法适用范围的事实性声明（只要有 logit access 就能用），不是性能保证。OntoCoDec 的约束编译是模型无关的——grammar layer 通过 XGrammar 在 token 层面操作，semantic layer 通过 entity registry 跟踪已生成内容。两层均不依赖模型参数或架构细节。\n\n(2) 论文确实提供了 70B 结果（Table 4, p.7: Llama-3.1-70B 在 SciERC 和 DocRED 上的 zero-shot 评估），虽然没有 fine-tuning ablation，但显示了相同的 DR 消减模式。Table 4 显示 Llama-3.1-70B 在 SciERC 上 DR 从 56.97→1.50（grammar）→0（Full S1），在 DocRED 上 DR 30.77→16.03→0.17。约束机制在 70B 上的有效性是可验证的。\n\n(3) 更重要的 gap 是 Mistral 在 Table 4 中的表现差异（SciERC 零 violations 但 DocRED zero-shot 后 CF 很高），这表明 model calibration 而非 model scale 是关键变量——论文在 §5.3 和 Limitations 中充分讨论了这一点。\n\n建议：将 N4 降为 Should-Fix。可以在 Limitations 中加一句明确承认 70B scale 验证有限，但不需要改 Abstract 的适用范围声明。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: κ̄ 基于 n=6 数据点的关联分析**\n\n完全同意，与我的 W2 一致。论文自身在 Appendix C (p.21) 承认 \"n=6 is insufficient for statistical inference on this correlation\"。n=6 的回归分析（Figure 2）不能支撑因果或强相关性结论。κ̄ 应被定位为 diagnostic metric 而非独立理论贡献。\n\n**[AGREE] R1-W2: Fallback 机制与核心 claim 的张力未充分分析**\n\n同意。这是一个我在第一轮审稿中未充分关注的有价值观察。论文在 Appendix C (p.19-20) 讨论了 CF dual mechanisms（\"Grammar-first fallback\" 和 \"Grammar-first\"），也在 Limitations (p.10, §Constraint scope) 讨论了 CF↔DR trade-off，但缺少的关键分析是：**residual DR violations（如 Table 10 中 fine-tuned 设置下的 36 个残余 violations）有多少发生在 fallback 位置**。\n\nAppendix D (p.25, Table 13) 提供了 per-relation violation breakdown，但按 violation type（entity type error, schema coverage gap 等）分类，不是按 fallback vs non-fallback 位置分类。追踪 fallback 事件与 residual violations 的关联性将直接回答 \"fallback 是否是 residual DR 的主要来源\" 这一问题。\n\n**[REBUT] R1-W3: S1 vs S2 配置选择缺乏充分论证**\n\n部分不同意。论文在 §5.1 (p.5) 提供了明确的比较：\"S1 vs S2. S2 achieves comparable DR (0.97%) but lower R-F1 (8.03 vs. 8.36) without resolving CF (8.03% vs. 9.90%); we adopt S1.\" 这给出了三个维度（DR, R-F1, CF）的对比，结论清晰：S1 在 R-F1 和 CF 上均优于 S2，DR 可比。\n\n不过，R1 要求更深入的 cost-benefit 分析也有道理——尤其是 S2 的两阶段 pipeline（§3.4: \"A first pass extracts entities; these compile an input-dependent grammar for the second pass\"）在特定场景（如 entity types 非常多时）可能有优势。这属于 minor improvement 而非 must-fix。\n\n**[AGREE] R1-W4: 仅英语数据集评估**\n\n同意。论文 Limitations section (p.10) 在 \"Engineering considerations\" 段讨论了 tokenizer 依赖性和 API-only 模型限制，但未明确提及语言覆盖缺口。SciERC（英语学术文本）、DocRED（英语 Wikipedia）、WikiEvents（英语新闻）均为英语。对于依赖 subword tokenization 的 continuation masking 机制（§3.3），跨语言泛化（尤其中日韩等非空格分词语言）是一个实质性开放问题。应在 Limitations 中加一句明确标注。\n\n**[AGREE] R1-W5: Post-hoc filtering 对比可能不够公平**\n\n同意。论文的 post-hoc filtering baseline（§5.1, p.5: \"Post-hoc filtering achieves DR→0% but with 15-74% rejection rates\"）是 discard-based（丢弃 invalid triples），而非 correction-based（将 invalid types 替换为最近的 valid type）。\n\n一个 post-hoc correction baseline（如用 embedding 距离最近的合法类型替换违规类型）可能在 DR 和 F1 之间取得比 discard 更好的平衡，从而构成更强的 baseline。论文在 Appendix C (p.22, \"Post-Hoc Filtering: Extended Comparison\", Table 11) 提供了更详细的 post-hoc 分析，但仍是 discard-based。\n\n不过，需要指出：post-hoc correction 作为 baseline 的公平性也有争议——因为 correction 需要额外的 type similarity 信息（如 type embedding），这引入了 OntoCoDec 未使用的外部知识。论文的 discard-based filtering 是一个 assumption-minimal 的 baseline。\n\n---\n\n### 小问题\n\n**[AGREE]** 页数溢出（~8行结论在第9页）：与我的 N1 一致，我将其列为 critical。\n\n**[AGREE]** Table 1 \"Tgt.\" 列含义不直观：确实，\"Tgt.\" 代表 \"Target\"（全部 violations 为 0 的目标），但未在表注中解释。\n\n**[AGREE]** Enabling dependency 概念在主文中未正式定义：§3.1 Corollary 提到 \"the enabling dependency is necessary\" 但 enabling dependency 本身（grammar layer 不能替代 semantic layer）在主文中仅用自然语言描述，没有形式化定义。\n\n**[AGREE]** Figure 1 信息密度高：与我的 m3 一致。\n\n**[AGREE]** Orphan bib entries：与我的 m1 一致。\n\n**[AGREE]** 引用格式 encoding mismatch：verify_references 工具确认 10/60 entries 有 minor mismatches（主要是作者姓名编码，如 Šakota vs Sakota），2 entries 在 OpenAlex 中未找到（regino2025kgcurator, formattax2026）。\n\n---\n\n### 对 R1 主要优势的回应\n\nR1 列出的 6 项优势与我的评估基本一致：\n\n1. **Decidability taxonomy 是真正的理论贡献** — 完全同意，这是论文最显著的学术贡献。\n2. **Ablation 设计全面** — 同意，5-way ablation (Table 1) + 4-way fine-tuned ablation (Table 10) 设计精良。\n3. **Fine-tuning composability 有实际价值** — 同意，Table 2 显示 LoRA fine-tuning 后约束仍然有效（DR ≤ 0.09% on SciERC）。\n4. **附录极其详尽** — 同意，24 页附录覆盖从 prompts 到 pumping lemma 证明的几乎所有细节。\n5. **DR 消减效果显著** — 同意，但需加 caveat：在 favorable conditions 下（LoRA + beam S1）。\n6. **统计实践良好** — 同意，bootstrap CI、cross-seed validation (Table 20) 等。\n\n---\n\n### 总结\n\nR1 与 R2（我）在以下关键判断上一致：\n- **Overall 3.0 (Findings)**：执行质量高但新颖性偏增量\n- **Soundness 3.5**：主要 claims 有支撑但存在 guarantee/fallback 矛盾\n- **WikiEvents 初步性**：两位 reviewer 均标记\n- **κ̄ 样本量不足**：两位 reviewer 均标记\n- **页数超限**：两位 reviewer 均标记\n\n两位 reviewer 的分歧点：\n- **R1-N4 (70B 评估)**：R1 列为 Must-Fix，我认为应降为 Should-Fix。Abstract 的 \"applicable to autoregressive LMs\" 是方法适用范围声明而非性能保证，且 Table 4 已提供 70B 验证数据。\n- **R1-W3 (S1 vs S2 选择)**：R1 认为缺乏论证，我认为 §5.1 已提供足够的三维度对比。\n- **Baseline 对比 (R1-N1)**：R1 标记为最严重的 critical issue。我同意其重要性，但补充指出 grammar-only ablation 隐含了 GCD 对比——论文应将此显式化而非要求完全重新实验。\n",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-21T01:33:04.438937+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4593
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-21T01:33:10.187173+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-21T01:33:10.237947+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1272 · 2026-05-21T01:33:20.404113+00:00_

交叉回应已提交。对 R1 的 4 个 Must-Fix 和 5 个 Should-Fix 逐条回应：

- **N1 (缺 baseline 对比)**: [AGREE]，但补充指出 grammar-only ablation 隐含了 GCD 对比
- **N2 ("guarantee" 措辞)**: [AGREE]，与我的发现一致
- **N3 (WikiEvents 不足)**: [AGREE]，与我的 W3 一致
- **N4 (70B 评估)**: [REBUT]，认为应降为 Should-Fix——Abstract 是适用范围声明而非性能保证，Table 4 已有 70B 数据
- **W1-W5**: 4 个 AGREE，1 个部分 REBUT (W3 S1/S2 选择已在 §5.1 有三维度对比)

两位 reviewer 在 Overall 3.0 (Findings)、Soundness 3.5、κ̄ 样本不足、WikiEvents 初步性、页数超限等核心判断上高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 28

## Round 28

72 recorded events


### User

_source line 1273 · 2026-05-21T02:27:30.847648+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 格式合规**。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- **Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)
- **类别**: Long Paper (ARR)
- **格式要求**: 正文 ≤8 页（严格），参考文献不限页数，Limitations 和 Ethics 不计入页数，ACL 模板（\usepackage[review]{acl}），double-blind 匿名审稿
- **Deadline**: 2026-05-25
- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
- **PDF 路径**: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf

## 你的审查侧重

### 1. 新颖性评估
- **核心贡献定位**: "systematic engineering contribution with theoretical grounding" 是否足以支撑 EMNLP main conference？这是系统集成还是算法创新？
- **Proposition 1**: 形式化证明 IE type constraints 超出 CFG expressiveness——这是 motivation 还是独立理论贡献？结论是否 trivially obvious？
- **κ̄ (constraint tightness)**: 定义为 1 - |σ(r)|/|E|²，n=6 数据点。是独立贡献还是 diagnostic metric？在 §1 contribution list 中的定位是否过高？
- **与已有工作的区分**: 相对于 GCD、BoostCD、CRANE、GoLLIE、EnriCo、TANL、REBEL 等，OntoCoDec 的独特贡献是什么？增量 novelty 是否足够？
- **两层架构**: grammar (XGrammar) + semantic (entity registry + dynamic masking) 的组合是否有足够技术深度？

### 2. 完整性评估
- **Claims 与证据匹配**: Abstract/Introduction 中的每个 claim 是否都有实验数据支撑？特别注意：
  - "near-eliminates DR" 但 CF 最高 12.02%——是否选择性报告？
  - "94-100% DR reduction" 在 Abstract 但 DocRED zero-shot 仅 45%
  - "1-2% even after LoRA fine-tuning" 与 Table 2 数据的一致性
  - "formal guarantees" vs "best-effort" 措辞矛盾
- **实验覆盖的缺口**: 
  - 仅英语数据集
  - 仅 LoRA 一种 fine-tuning 方法
  - WikiEvents 仅 20-doc test set
  - 70B 仅 INT4 推理
  - 无 head-to-head baseline comparison with BoostCD/GCD（grammar-only ablation 是否等价？）
- **Related Work 完整性**: 是否遗漏重要相关工作？主文 §6 仅 1/3 页是否过于压缩？
- **Limitations 充分性**: 是否如实报告所有限制？跨语言泛化是否提及？

### 3. 格式合规（EMNLP 2026 硬性要求）
- **页数**: 正文是否 ≤8 页？结论是否溢出到第 9 页？（之前 R13/R15 已标记此问题回归）
- **匿名性**: 是否有匿名违规？检查作者标识、仓库链接、致谢等
- **参考文献格式**: 是否使用 natbib？bib entries 是否完整？是否有 orphan entries？
- **Checklist**: ARR Responsible NLP Research Checklist 是否包含？
- **图表质量**: Figure 1 信息密度、Table caption 完整性
- **ACL 模板**: \usepackage[review]{acl} 是否正确使用？

### 4. 评分标准（EMNLP 2026 ARR）
- 5 = Consider for Award（约前2.5%）
- 4 = Conference（可被主会议接收）
- 3.5 = Borderline Conference
- 3 = Findings
- 2.5 = Borderline Findings
- 2 = Resubmit next cycle

请给出：Summary → Strengths → Weaknesses（按 Must-Fix / Major / Minor 分级） → Questions → Missing References → Novelty (1-5) → Completeness (1-5) → Overall Assessment (1-5) → Confidence (1-5)

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

_source line 1274 · 2026-05-21T02:27:40.651433+00:00_

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

_source line 1275 · 2026-05-21T02:27:41.226230+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 574
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-21T02:27:41.279890+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
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
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-21T02:27:41.330594+00:00_



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

_source line 1278 · 2026-05-21T02:27:47.385022+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria dimensions"
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
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1279 · 2026-05-21T02:27:48.848201+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "1-10",
  "project": "schema_semantic_constrained_ie",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "1-10",
    "project": "schema_semantic_constrained_ie",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-21T02:27:49.552753+00:00_

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


### Tool call

_source line 1281 · 2026-05-21T02:27:49.856518+00:00_

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

_source line 1282 · 2026-05-21T02:27:54.028965+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

I found information about ACL Rolling Review (ARR) 2026. Based on the search results, here's what I found:

## ARR 2026 Reviewer Guidelines

ARR has developed detailed guidelines and suggestions for each step of the review process, including a list of common problems in both reviews and NLP papers to watch out for.

## Review Form and Criteria

The reviewer and AC guidelines may be seen by authors during the response period, with some sections having codes for (meta-)review issues (I1-I12) that can be reported by authors.

## Key Policies for 2026

The deadline for completing the registration form is January 7th 2026 EoD AoE.

Starting in May 2025, ARR adopts a new policy on 'highly irresponsible' (meta-)reviewers, with the program chairs and ARR EiCs considering egregious cases reported by chairs, including extremely terse reviews, unprofessional tone, and LLM-
…[truncated 339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6643
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-21T02:27:55.487710+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 521.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.7}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 522.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 490.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 462.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"w
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6639
}
```

</details>

---


### Tool result

_source line 1284 · 2026-05-21T02:28:54.168414+00:00_

&lt;persisted-output>
Output too large (51.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/5ba9ac0f-a4bd-4671-8cb6-0fea130e3e22/tool-results/toolu_01Lf2mhKb9LAbvUtC6SbXBDr.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 100, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 50, \"online_not_found\": 2, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proc
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 64615
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-21T02:28:54.169563+00:00_

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
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 5919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 64313
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-21T02:29:01.810030+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions/criteria, scoring scales, and any specific instructions for reviewers. I need: 1) All review form fields and their scales (e.g., soundness, excitement, overall assessment) 2) Definitions for each score level 3) Any specific criteria or guidelines for each dimension"
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
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions/criteria, scoring scales, and any specific instructions for reviewers. I need: 1) All review form fields and their scales (e.g., soundness, excitement, overall assessment) 2) Definitions for each score level 3) Any specific criteria or guidelines for each dimension"
  }
}
```

</details>

---


### Tool call

_source line 1287 · 2026-05-21T02:29:02.816891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-21T02:29:03.321875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-21T02:29:03.825099+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-21T02:29:03.825609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-21T02:29:04.689099+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1367
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-21T02:29:04.739893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-21T02:29:05.195179+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1369
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-21T02:29:05.197917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 1295 · 2026-05-21T02:29:05.754875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 1296 · 2026-05-21T02:29:06.209189+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1469
}
```

</details>

---


### Tool call

_source line 1297 · 2026-05-21T02:29:06.209656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1298 · 2026-05-21T02:29:07.116577+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1920
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-21T02:29:07.117855+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-21T02:29:07.118214+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-21T02:29:07.620628+00:00_

# ARR Review Form Dimensions

Based on the reviewer guidelines, the ARR review form includes these primary scoring dimensions:

## Main Scoring Dimensions

**1. Soundness**
- Must be justified by review text
- Low scores require substantive evidence of faults
- Measures technical validity and methodological rigor

**2. Excitement**
- Orthogonal to soundness assessment
- Reflects personal interest/subjective taste
- Does not require explicit justification

**3. Overall Assessment**
- Composite recommendation for venue acceptance
- Balances soundness, excitement, novelty, and impact
- Guides commitment decisions to ACL conferences

## Additional Form Components

The guidelines reference several other assessment areas:

- **Confidence score**: Indicates reviewer expertise level for the specific paper
- **Author identity disclosure**: Whether reviewers know or suspect authorship
- **Reproducibility score**: Justified assessment of replicability

## Key Instruction

The document states that "soundness scores must be justified by the text of the review." Reviews lacking substantive support for low soundness ratings require revision before submission.

The guidelines emphasize that "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," though excitement varies by reviewer preference.

**Note**: The full review form specifications are described in a separate ["ARR review form" post](https://aclrollingreview.org/reviewform) linked within the guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5810
}
```

</details>

---


### Tool result

_source line 1302 · 2026-05-21T02:29:07.622142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool call

_source line 1303 · 2026-05-21T02:29:07.629018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-21T02:29:08.186006+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-21T02:29:08.438546+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1320
}
```

</details>

---


### Tool result

_source line 1306 · 2026-05-21T02:29:09.043626+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-21T02:29:09.346096+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1160
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-21T02:29:40.923881+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their scales, and definitions. I need every field: soundness, excitement/novelty, overall assessment, confidence, reproducibility, etc. Include the exact scale definitions (what each number means)."
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
    "prompt": "Extract the COMPLETE review form with ALL scoring dimensions, their scales, and definitions. I need every field: soundness, excitement/novelty, overall assessment, confidence, reproducibility, etc. Include the exact scale definitions (what each number means)."
  }
}
```

</details>

---


### Tool call

_source line 1309 · 2026-05-21T02:29:45.499049+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/5ba9ac0f-a4bd-4671-8cb6-0fea130e3e22/tool-results/toolu_01Lf2mhKb9LAbvUtC6SbXBDr.txt",
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
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-2-cbe93d98/5ba9ac0f-a4bd-4671-8cb6-0fea130e3e22/tool-results/toolu_01Lf2mhKb9LAbvUtC6SbXBDr.txt",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1310 · 2026-05-21T02:29:45.852623+00:00_

1	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 100, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 50, \"online_not_found\": 2, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang...\", \"year\": \"2023\", \"venue\": \"Fin
…[truncated 50311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-21T02:29:48.062553+00:00_

# ACL Rolling Review Form – Complete Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1–5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1–5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1–5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment**
Scale: 1–5 (with .5 increments)
- **5**: "Consider for Award"
- **4**: "Conference"
- **3**: "Findings"
- **2**: "Resubmit next cycle"
- **1.5**: "Resubmit after next cycle"
- **1**: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1–5
- **5**: "They could easily reproduce the results."
- **4**: "They could mostly reproduce the results, but there may be some variation."
- **3**: "They could reproduce the results with some difficulty."
- **2**: "They would be hard pressed to reproduce the results
…[truncated 1348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7138
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-21T02:29:57.383662+00:00_

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

_source line 1313 · 2026-05-21T02:29:57.685144+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes.
4	The two layers exhibit a formal enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} near-eliminates DR (94--100\% reduction) with negligible R-F1 impact ($\pm$0.6\,pp) but introduces cross-field (CF) violations as a trade-off (0--9.9\% zero-shot, $\leq$1.2\% fine-tuned; \S\ref{sec:scierc-results}).
7	CF is substantially reduced by beam search under favorable conditions (low $\bar{\kappa}$ or fine-tuned settings).
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across four autoregressive LMs (7--70B; 70B evaluated in INT4 only, \S\ref{sec:70b-results}) with logits access and three tokenizer families (up to 96 relation types).
9	\end{abstract}
10	

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

_source line 1314 · 2026-05-21T02:29:57.836133+00:00_

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

_source line 1315 · 2026-05-21T02:29:58.639606+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption; type violation elimination ensures ontological consistency of constructed KGs independent of extraction F1, making reliable constraint enforcement necessary.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
16	Training-based approaches~\cite{s
…[truncated 2783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-21T02:29:58.640026+00:00_

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

_source line 1317 · 2026-05-21T02:29:59.144061+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	\input{fig1_framework}
9	
10	We present OntoCoDec, a framework that translates IE ontologies into token-level constraints enforced during autoregressive generation.
11	The design is guided by a decidability analysis of IE type constraints.
12	
13	\paragraph{Constraint decidability taxonomy.}
14	\label{sec:decidability}
15	We classify IE type constraints into three levels: (1)~\emph{context-free}: vocabulary membership and JSON structure; (2)~\emph{prefix-decidable with state}: domain/range type validity, determined at each type-bearing position given the decoded relation type and entity registry; (3)~\emph{non-local}: cross-entity type consistency, which depends on the full output.
16	Unlike code generation where types are statically declared, IE constraints fall into level~2: entity types are inferred from text, the registry is built dynamically, and constraint targets depend on the co-occurring relation.
17	OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
18	
19	\smallskip
20	\noindent
21	Existing grammar-constrained decoding frameworks (e.g., XGrammar) enforce level~1 constraints---structural validity and vocabulary membership---but IE domain/range rules require cross-position entity-type state that context-free grammars cannot express.
22	We formalize this gap:
23	
24	\smallskip
25	\noindent\textbf{Proposition 1} (Level 2 $\not\subseteq$ Level 1)\textbf{.}
26	\textit{Domain/range type constraints for IE with unbounded entity sets are not context-free.}
27	
28	\smallskip
29	\noindent\textit{Proof sketch.}
30	Consider $\mathcal{E} = \{\tau_A, \tau_B\}$ and a relation $r$ with $\operatorname{dom}(r) = \{\tau_A\}$.
31	An output contains $n$ entities with independently chosen types ($a_i \in \{
…[truncated 7166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-21T02:29:59.144451+00:00_

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

_source line 1319 · 2026-05-21T02:29:59.646878+00:00_

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
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the enabling dependency (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	
13	\paragraph{Grammar-First Fallback.}
14	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
15	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
16	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
17	
18	\paragraph{Constraint Tightness.}
19	For relation $r$:
20	%
21	\begin{equation}\label{eq:tightness}
22	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathcal{E}|^2},
23	\end{equation}
24	%
25	The mean $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes schema restrictiveness: SciERC ($\bar{\kappa}{=}0.333$) achieves 94--99\% DR reduction vs.\ DocRED ($\bar{\kappa}{=}0.842$) at 42--90\%; entity type confusability is a critical co-factor (Appendix~\ref{app:kappa-case-study},~\ref{app:tcr}).
26	
27	\paragraph{Greedy limitation and 
…[truncated 1497 chars]

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

_source line 1320 · 2026-05-21T02:29:59.647495+00:00_

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

_source line 1321 · 2026-05-21T02:30:00.254642+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata, but IE type environments accumulate dynamically (\S\ref{sec:composition}).
9	
10	\paragraph{Schema-aware IE.}
11	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
12	
13	\paragraph{Constraint enforcement in IE.}
14	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via ILP; post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation; EnriCo~\cite{zaratiana2024enrico}, IterGen~\cite{ugare2025itergen}, and DCCD~\cite{dccd2026} enforce constraints via ASP, backtracking, or draft-conditioning.
15	Grammar-only enforcement (GCD~\cite{geng2023gcd}, BoostCD~\cite{boostcd2025}) achieves only partial DR reduction; the quantitative gap is analyzed in \S\ref{sec:constrained-baselines}.
16	OntoCoDec uses \emph{preventive} forward-only token masking at $O(|V|)$ per step; while constrained decoding can degrade reasoning~\cite{banerjee2025crane,schall2025hiddencost,formattax2026}, extraction tasks are robust to format co
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 607
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-21T02:30:00.305421+00:00_

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

_source line 1323 · 2026-05-21T02:30:00.406869+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec translates IE ontologies into composable token-level constraints via a decidability-guided two-layer architecture.
4	LoRA + greedy S1 achieves DR\,$\leq$\,0.09\%, CF\,$\leq$\,1.2\%; beam ($k{=}4$) eliminates all violations on SciERC under favorable conditions (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models.
5	Beam search substantially reduces CF under fine-tuned conditions; evaluation covers primarily 7--8B models with preliminary 70B results.
6	

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

_source line 1324 · 2026-05-21T02:30:06.202217+00:00_

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

_source line 1325 · 2026-05-21T02:30:07.106999+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), near-eliminating DR (DR\,$\leq$\,0.09\%) with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations on SciERC under favorable conditions (1.54$\times$ latency).
8	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe to isolate constraint effects; R-F1 2--8 reflects absent task-specific training, not method failure.
9	The deployment-relevant evaluation is the fine-tuned setting (R-F1 40--46\%), where constraints compose with parameter optimization without degrading performance.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations ar
…[truncated 284 chars]

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

_source line 1326 · 2026-05-21T02:30:07.258031+00:00_

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

_source line 1327 · 2026-05-21T02:30:07.560043+00:00_

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
…[truncated 5249 chars]

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

_source line 1328 · 2026-05-21T02:30:07.560713+00:00_

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

_source line 1329 · 2026-05-21T02:30:08.670333+00:00_

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
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
56	Grammar-only $\uparrow$DR: vocabula
…[truncated 1557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-21T02:30:08.822420+00:00_

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

_source line 1331 · 2026-05-21T02:30:09.075031+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction}
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
42	  & Uncon
…[truncated 2383 chars]

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

_source line 1332 · 2026-05-21T02:30:09.075980+00:00_

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

_source line 1333 · 2026-05-21T02:30:09.428373+00:00_

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
…[truncated 1206 chars]

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

_source line 1334 · 2026-05-21T02:30:09.429434+00:00_

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

_source line 1335 · 2026-05-21T02:30:09.480478+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC and $+$2.43\% on DocRED (amortized over longer sequences); under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	Beam search ($k{=}4$), following the constrained beam search paradigm~\cite{anderson2017guided}, explores paths satisfying both layers jointly.
11	With LoRA, beam S1 eliminates all four violation types on SciERC for both models (R-F1 44--47); under zero-shot, beam reduces DR to 0\% and CF substantially (9.90\%\,$\to$\,0.53\% Qwen on SciERC; Appendix~\ref{app:beam-search}).
12	DocRED zero-shot beam evaluates on a 50-document subset (compute cost; LoRA beam uses the full 998-document set).
13	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
14	
15	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
16	\paragraph{Preliminary 70B evaluation.}
17	\label{sec:70b-results}
18	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on both SciERC (R-F1 $-$0.03\,pp) and DocRED (R-F1 $+$0.04\,pp), one of three configurations to eliminate DR on DocRED.
19	CF rises to 7.01\% (from 0.07\%), partly because constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
20	
21	\paragraph{Comparison with grammar-constrained approaches.}
22	\label{sec:constrained-baselines}
23	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same class of constraints---vocabulary membership via context-free grammars---as grammar-constrained decoding systems such as GCD~\cite{geng2023gcd} and t
…[truncated 521 chars]

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

_source line 1336 · 2026-05-21T02:30:17.511689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-21T02:30:18.316214+00:00_

1	% Appendix: Full Proof of Proposition 1
2	% Level 2 (prefix-decidable with state) constraints are not context-free.
3	
4	\section{Full Proof of Proposition 1}
5	\label{app:pumping-lemma}
6	
7	We prove that domain/range type constraints for IE with unbounded entity sets cannot be expressed by any context-free grammar, using the pumping lemma for context-free languages.
8	
9	\begin{proof}
10	Define the language $L$ of valid IE outputs over ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ with $\mathcal{E} = \{\tau_A, \tau_B\}$, $\mathcal{R} = \{r\}$, and $\sigma(r) = \{(\tau_A, \tau_A)\}$ (i.e., $r$ requires both head and tail to be type $\tau_A$).
11	
12	An output string has the form:
13	\[
14	w = e_1\, e_2\, \cdots\, e_n\;\; \texttt{REL}(h{=}e_k,\, r,\, \tau^h)
15	\]
16	where each $e_i$ is an entity with type $\tau_{a_i} \in \{\tau_A, \tau_B\}$, and $\tau^h$ is the head type field of a relation triple referencing entity $e_k$ ($1 \leq k \leq n$).
17	
18	The type-validity constraint requires $\tau^h = \tau_{a_k}$ (the head type must match the referenced entity's type) \emph{and} $\tau^h \in \operatorname{dom}(r) = \{\tau_A\}$.
19	Combined: a string $w \in L$ if and only if $\tau_{a_k} = \tau_A$.
20	
21	Now consider strings of the specific form:
22	\[
23	w_n = \underbrace{\tau_B\; \tau_B\; \cdots\; \tau_B}_{n-1}\; \tau_A\;\; \texttt{REL}(h{=}e_n,\, r,\, \tau_A)
24	\]
25	where the first $n{-}1$ entities have type $\tau_B$ and only entity $e_n$ has type $\tau_A$.
26	The relation references $e_n$, so $\tau^h = \tau_A = \tau_{a_n}$, satisfying both the registry consistency and domain constraint.
27	Thus $w_n \in L$ for all $n$.
28	
29	Assume for contradiction that $L$ is context-free.
30	By the pumping lemma, there exists a pumping length $p$ such that any $w \in L$ with $|w| \geq p$ can be written as $w = uvxyz$ where:
31	\begin{enumerate}[label=(\roman*)]
32	    \item $|vy| \geq 1$,
33	    \item $|vxy| \leq p$,
34	    \item $uv^i xy^i z \in L$ for all $i \g
…[truncated 4106 chars]

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

_source line 1338 · 2026-05-21T02:30:18.316629+00:00_

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

_source line 1339 · 2026-05-21T02:30:18.669534+00:00_

1	\section{Extended Related Work}
2	\label{app:related_work}
3	
4	% ===========================================================================
5	% Paradigm 1: Grammar-Constrained Decoding
6	% ===========================================================================
7	\paragraph{Grammar-Constrained Decoding.}
8	Recent work has established efficient algorithms for restricting LLM outputs to conform to context-free grammars, making grammar-constrained decoding the de facto standard for obtaining structured output from language models.
9	XGrammar~\cite{dong2025xgrammar} partitions the vocabulary into context-independent and context-dependent tokens and maintains persistent pushdown automata across decoding steps, achieving up to 100$\times$ speedup over prior CFG-constrained decoding methods.
10	Outlines~\cite{willard2023outlines} reformulates constrained generation as finite-state machine transitions with offline vocabulary indexing, which enables efficient enforcement of regular-expression and JSON-schema constraints without runtime overhead per token.
11	LMQL~\cite{beurer-kellner2023lmql} introduces a declarative query language that compiles type, length, and regex constraints into token-level masks, providing a programmable interface for specifying multi-variable output structures.
12	These systems ensure that every generated token belongs to a grammar-valid continuation, but they do not address the \emph{distribution distortion} introduced by naive token masking.
13	A parallel line of work tackles this problem directly: DOMINO~\cite{beurer-kellner2024domino} minimizes distributional divergence during CFG enforcement by formulating mask selection as an optimization problem, and ASAp~\cite{park2024grammar} provides a provably unbiased sampling algorithm that preserves the original LM distribution under grammar constraints.
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for 
…[truncated 19901 chars]

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

_source line 1340 · 2026-05-21T02:30:18.670097+00:00_

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

_source line 1341 · 2026-05-21T02:30:18.721667+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$, where $\mathcal{P}(\cdot)$ denotes the power set, specifying valid (head type, tail type) pairs per relation.
9	A triple $(h, r, t)$ is \emph{type-valid} if $(\mathrm{type}(h), \mathrm{type}(t)) \in \sigma(r)$.
10	We quantify constraint restrictiveness via \emph{constraint tightness} $\kappa(r)$ (Eq.~\ref{eq:tightness}, \S\ref{sec:composition}): tighter constraints leave fewer valid type pairs per relation.
11	We define ontology constraints broadly to encompass both formal ontology specifications (e.g., the KAIROS event ontology with explicit role-entity type mappings) and empirically derived type-pair constraints extracted from annotated training data.
12	The latter applies when datasets lack a formal ontology but provide typed annotations (SciERC, DocRED); OntoCoDec compiles both sources into the same constraint representation without modification.
13	Empirical constraints achieve 99\%+ instance-level coverage on held-out data (SciERC 99.0\%, DocRED 99.4\%); uncovered type pairs trigger grammar-first fallback (\S\ref{sec:composition}), ensuring no valid triples are blocked.
14	
15	\paragraph{Grammar-Constrained Decoding.}
16	\label{sec:bg:gcd}
17	Grammar-constrained decoding restricts each token $y_t$ to a mask $M_g \in \{0, 1\}^{|V|}$ derived from a target grammar.
18	XGrammar~\citep{dong2025xgrammar} compiles JSON Schemas into pushdown automata for efficient enforcement of structural constraints; Outlines~\citep{willard2023outlines} and SGLang~\citep{zheng2024sglang} offer similar capabilities.
19	However, these methods are limited to context-free constraints and cannot enforce cross-field sema
…[truncated 910 chars]

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

_source line 1342 · 2026-05-21T02:34:15.244281+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n**审查侧重**: 新颖性 + 完整性 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的工程贡献，解决了 IE 中 type violation 的实际问题，但算法新颖性有限、claim 与 evidence 存在可量化的不匹配，且缺少与最直接竞争方法的 head-to-head 对比。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法技术上正确，ablation 设计系统化，bootstrap 统计检验规范；但 abstract 数字与表格数据存在可验证的不一致，\"formal guarantee\" 措辞与 best-effort fallback 存在张力 |\n| Excitement | 2.5/5 | 实际应用价值明确，但方法是已知技术（XGrammar + 有限状态注册表 + logit masking）的领域迁移组合，不会根本改变 IE 研究方向 |\n| Reproducibility | 4/5 | 实验设置详尽（Appendix G），prompts 完整（Appendix A），统计检验充分；代码未开源但 checklist 承诺 acceptance 后发布 |\n| Confidence | 4/5 | 我仔细核对了所有表格数字与 claim 的一致性，熟悉 constrained decoding 和 IE 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 中 \"94–100% DR reduction\" 与 Table 2 数据不一致\n- 具体位置：Abstract 第 6 行；Table 2（§5.1）\n- 问题：Abstract 声称 \"Composed with LoRA fine-tuning, OntoCoDec near-eliminates DR (94–100% reduction)\"。然而 Table 2 中 Llama-3.1-8B SciERC 的 fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置的实际范围是 92–100%，而非 94–100%。\n- 为什么影响接收：这是 Abstract 中的核心定量 claim，可直接验证。数字不准确会严重损害可信度。\n- 建议：将 Abstract 改为 \"92–100% reduction\" 或 \"≥92% reduction\"；如果要保留 94%，需明确排除 Llama-SciERC 并说明理由。\n\n**N2** [critical] CF 率在 Abstract 中选择性报告，隐藏了非 SciERC 场景的较高 CF\n- 具体位置：Abstract 第 6 行 \"(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)\"；Table 4（§5.3）；Table 5（§5.4）\n- 问题：Abstract 通过 \"(§5.1)\" 将 CF 范围限定为 SciERC 一个数据集，但同一段中提到了 DocRED 和 WikiEvents 的验证。实际上：\n  - DocRED zero-shot: Llama CF = **12.02%**（Table 4），远超 \"0–9.9%\"\n  - WikiEvents zero-shot: CF = **14.9–21.1%**（Table 5）\n  - 读者很容易将 \"(0–9.9%)\" 误解为全局范围\n- 为什么影响接收：这构成选择性报告（cherry-picking）。CF 是本文方法的核心 trade-off，不完整披露会误导 AC/Reviewer 对方法局限性的判断。\n- 建议：Abstract 应报告全数据集范围，如 \"CF 0–21.1% zero-shot (dataset-dependent), ≤1.2% fine-tuned\"，或至少明确标注 \"on SciERC\"。\n\n**N3** [critical] 缺少与最直接竞争方法的 head-to-head 实验对比\n- 具体位置：§5, §6（Related Work）\n- 问题：论文将 grammar-only ablation 作为 GCD/BoostCD 的代理，但 BoostCD 的 boosting mechanism（交替 constrained/unconstrained decoding）是其核心贡献，grammar-only ablation 无法代表。同样，IterGen（backtracking-based semantic constraint）和 EnriCo（ASP-based decoding constraints）是做 semantic-level constrained decoding 的最直接竞品，均未进行实验对比。\n- 为什么影响接收：没有 head-to-head comparison，无法判断 OntoCoDec 的相对优势。Reviewer 和 AC 会质疑：既然已有方法也做 semantic constraint enforcement（IterGen via backtracking, EnriCo via ASP），OntoCoDec 的 forward-only masking 相比之下真正好在哪里？只有主观论述没有定量证据。\n- 建议：至少与 BoostCD 在 SciERC/DocRED 上做 head-to-head RE 实验（BoostCD 有开源代码）；如 IterGen/EnriCo 不可直接复现，应明确说明不可比原因。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] DocRED zero-shot DR 仅 45%，与论文整体 narrative 存在张力\n- 具体位置：Table 3（§5.2）；§1 contribution item 2\n- 问题：DocRED zero-shot Full S1 的 DR 从 18.46% 降至 10.21%，相对降幅仅 **45%**，远低于 SciERC 的 94%。论文通过将 zero-shot 定位为 \"diagnostic probe\"（§5 开头）来弱化此结果，但 zero-shot 正是 constrained decoding 最核心的使用场景——不需要 task-specific training 的即插即用方案。45% 的 DR 降幅意味着仍有过半违规未被消除。\n  §1 contribution item 2 说 \"yields 94–100%\"，但 this 94% 仅来自 SciERC 的 zero-shot 五路 ablation，DocRED zero-shot 的 45% 被排除在外。\n- 建议：在 §1 contribution 中诚实报告范围（如 \"45–100% depending on schema tightness\"）。同时讨论：对 high-κ̄ schema，zero-shot 下 semantic layer 为何效力下降——是 fallback 太频繁还是 entity registry 不准确？\n\n**W2** [major] κ̄ (constraint tightness) 证据不足以支撑其 prominence\n- 具体位置：Eq. (3)（§4）；§2 Background\n- 问题：κ̄ = 1 − |σ(r)|/|E|² 仅在 n=2 个数据集上验证了相关性（SciERC κ̄=0.333 vs. DocRED κ̄=0.842）。n=2 不足以建立任何统计意义上的相关。§2 将 κ̄ 提升为 Background 概念，§4 给予独立方程编号和段落——这种 prominence 远超 \"two data points show a pattern\" 的证据强度。\n  WikiEvents 有 245 constraints，但未报告 κ̄ 值或其与 AC reduction 的相关。\n- 建议：降低 κ̄ 的定位——作为 diagnostic observation 而非 contribution；报告 WikiEvents κ̄ 值；如果要保留 κ̄ 作为有意义的 metric，需要更多数据集（或 per-relation κ(r) 与 per-relation DR 的相关分析）。\n\n**W3** [major] Proposition 1 作为 \"贡献\" 的定位偏高\n- 具体位置：§1 contribution item 1；§3 Proposition 1\n- 问题：Proposition 1 证明 IE type constraints 超出 CFG expressiveness。证明本身是正确的（pumping lemma argument, Appendix O, 两个 case 完整）。但这个结论对 formal language theory 背景的读者而言是 **expected** 的——cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理的基本知识（参见 attribute grammars 的经典动机）。论文在 §1 将 Proposition 1 作为第一个贡献列出，且用 \"establishing that IE type constraints require runtime state beyond CFG expressiveness\" 的措辞暗示这是一个独立理论发现。\n- 建议：将 Proposition 1 重新定位为 *motivation*（\"we formalize a well-known intuition...\"），而非 *contribution*。真正的贡献是实验验证 enabling dependency（grammar-only 24% vs. full 94%），这不需要 Proposition 1 的形式化证明也能成立。\n\n**W4** [major] WikiEvents 评估的可靠性不足以支撑 contribution claim\n- 具体位置：§5.4, Table 5；§1 contribution item 2b\n- 问题：WikiEvents fine-tuning composability 基于 **20 文档** test set（论文自己承认 \"preliminary\"）。Per-document variance 极高（Arg-F1 std/mean > 0.5, 35–47% documents scoring zero）。Zero-shot CF 率 14.9–21.1% 显著高于 RE 任务。尽管如此，§1 将 WikiEvents 列为 contribution item 2b (\"preliminary event extraction results on WikiEvents demonstrate generalization\")。\n  用 \"demonstrate generalization\" 描述一个 20-doc preliminary experiment，claim 强度与 evidence 强度不匹配。\n- 建议：保留 WikiEvents 结果但降级为 \"exploratory\" 或 \"case study\"；从 contribution list 中移除或用 \"initial evidence for\" 替代 \"demonstrate\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: §1 \"0.5–2% even after LoRA fine-tuning\" — Table 2 显示 Llama DocRED 是 0.49%，rounded 应为 \"~0.5–2%\" 或 \"0.5–2.0%\"，目前是准确的但边界很紧。\n\n- **M2**: Table 3 脚注中 XGrammar 残余 0.03% RV 来自 \"chimeric values\"（子词 token 拼接错误）——这是 XGrammar 已知 bug 还是 OntoCoDec 集成问题？应简要说明是否已上报/修复。\n\n- **M3**: §6 Related Work 主文仅 ~1/3 页。虽有 Appendix B（~2 页详细版），但主文中三段式（grammar-constrained decoding / schema-aware IE / constraint enforcement in IE）过于压缩，每段都是引用堆叠，缺乏对关键区分点的展开论述。对不看 Appendix 的读者，这降低了 positioning 的说服力。\n\n- **M4**: \"formal guarantees\" 措辞（§3.3 \"pair-based enforcement\" 描述）与 \"best-effort\" fallback（§4 grammar-first fallback）存在术语张力。DR 在 fallback 位置 structurally 无法为零（§4 \"all residual DR violations occur exclusively at fallback positions\"），所以 \"guarantee\" 不准确。建议统一为 \"best-effort with soft degradation\" 或类似表述。\n\n- **M5**: 引用验证结果：`regino2025kgcurator` 和 `formattax2026` 两条引用在 OpenAlex 中未找到匹配。`formattax2026` 标注为 arXiv:2604.03616，可能太新未索引，但应确认存在。8 条 mismatch 均为作者名编码差异（如 `šakota` vs `sakota`），非实质错误。\n\n- **M6**: §1 \"zero-shot DR drops 76–99% for calibrated models\" — 但 DocRED Mistral 的 DR 降幅 = (57.42−33.20)/57.42 = **42%**。Mistral 被排除为 \"boundary condition\"，但这个排除条件（\"calibrated models\"）在 §1 中不够透明。\n\n---\n\n## Missing References\n\n未发现重大遗漏。论文引用覆盖了 constrained decoding、schema-aware IE、post-hoc validation 三个维度的主要工作。Appendix B 的 extended related work 尤为全面。\n\n可能有价值的补充（非必须）：\n- Qi et al., 2024 \"AutoAct\" 或类似的 agentic IE 工作（作为 API-only models 场景的参考）\n- 更多关于 attribute grammars 的经典参考（支撑 Proposition 1 的 \"well-known\" 定位）\n\n---\n\n## 主要优势\n\n1. **问题定义清晰，实用价值明确**：IE 中 domain/range violation 是一个真实存在且系统性的问题（15–18% baseline violation rates），论文精确地量化了问题规模并提供了可操作的解决方案。\n\n2. **Ablation 设计系统化**：五路 ablation（unconstrained / grammar-only / semantic-only / full S1 / full S2）清楚地隔离了各层的贡献，enabling dependency 的实验证据（grammar-only 3% vs. semantic-only 24% vs. full 94%）比 Proposition 1 更有说服力。\n\n3. **Limitations section 异常诚实和全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎回答了 reviewer 想问的所有问题。这是论文最大的优点之一。\n\n4. **统计严谨性**：所有 F1 比较均有 10,000-iteration paired bootstrap，report p-values 和 confidence intervals。DR reduction 在所有 fine-tuned settings 中均 significant (p<0.001)。\n\n5. **跨模型/跨 tokenizer 泛化**：在三种不同 tokenizer 架构（byte-level BPE × 2, SentencePiece）和 4 个模型上验证，证明方法不依赖特定模型架构。\n\n6. **CF↔DR trade-off 的诚实报告**：没有回避 CF 上升的问题，提供了因果分析（fallback positions, GENERIC↔X ambiguity）和缓解方案（beam search, fine-tuning）。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Novelty | 2.5/5 |\n| Completeness | 3.0/5 |\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Overall Assessment | **3.0/5 (Findings)** |\n| Confidence | 4/5 |\n\n**主要判断依据**：\n- 算法新颖性有限：两层架构是 XGrammar（off-the-shelf）+ 有限状态注册表（dict + lookup + masking）的组合，技术深度不高。\n- Proposition 1 正确但 expected，κ̄ 证据不足，均不构成独立贡献。\n- 缺少与 BoostCD/IterGen/EnriCo 的 head-to-head 对比是最大实验缺口。\n- Abstract 中存在可验证的数字不一致（N1）和选择性报告（N2），损害 credibility。\n- 论文的实际价值（解决 IE violation 问题）和工程完整度（ablation + 统计 + 跨模型验证 + 诚实 limitations）适合 Findings 级别。\n- 若修复 N1–N3（数字准确性 + 补充 baseline 对比），可重新评估是否达到 Borderline Conference (3.5)。",
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
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (ACL Rolling Review, May 2026 cycle)\n**审查侧重**: 新颖性 + 完整性 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n**一句话总结**: 扎实的工程贡献，解决了 IE 中 type violation 的实际问题，但算法新颖性有限、claim 与 evidence 存在可量化的不匹配，且缺少与最直接竞争方法的 head-to-head 对比。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法技术上正确，ablation 设计系统化，bootstrap 统计检验规范；但 abstract 数字与表格数据存在可验证的不一致，\"formal guarantee\" 措辞与 best-effort fallback 存在张力 |\n| Excitement | 2.5/5 | 实际应用价值明确，但方法是已知技术（XGrammar + 有限状态注册表 + logit masking）的领域迁移组合，不会根本改变 IE 研究方向 |\n| Reproducibility | 4/5 | 实验设置详尽（Appendix G），prompts 完整（Appendix A），统计检验充分；代码未开源但 checklist 承诺 acceptance 后发布 |\n| Confidence | 4/5 | 我仔细核对了所有表格数字与 claim 的一致性，熟悉 constrained decoding 和 IE 领域 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 中 \"94–100% DR reduction\" 与 Table 2 数据不一致\n- 具体位置：Abstract 第 6 行；Table 2（§5.1）\n- 问题：Abstract 声称 \"Composed with LoRA fine-tuning, OntoCoDec near-eliminates DR (94–100% reduction)\"。然而 Table 2 中 Llama-3.1-8B SciERC 的 fine-tuned DR 从 1.11% 降至 0.09%，相对降幅 = (1.11−0.09)/1.11 = **91.9%**，低于所声称的 94% 下限。四组 fine-tuned 设置的实际范围是 92–100%，而非 94–100%。\n- 为什么影响接收：这是 Abstract 中的核心定量 claim，可直接验证。数字不准确会严重损害可信度。\n- 建议：将 Abstract 改为 \"92–100% reduction\" 或 \"≥92% reduction\"；如果要保留 94%，需明确排除 Llama-SciERC 并说明理由。\n\n**N2** [critical] CF 率在 Abstract 中选择性报告，隐藏了非 SciERC 场景的较高 CF\n- 具体位置：Abstract 第 6 行 \"(0–9.9% zero-shot, ≤1.2% fine-tuned; §5.1)\"；Table 4（§5.3）；Table 5（§5.4）\n- 问题：Abstract 通过 \"(§5.1)\" 将 CF 范围限定为 SciERC 一个数据集，但同一段中提到了 DocRED 和 WikiEvents 的验证。实际上：\n  - DocRED zero-shot: Llama CF = **12.02%**（Table 4），远超 \"0–9.9%\"\n  - WikiEvents zero-shot: CF = **14.9–21.1%**（Table 5）\n  - 读者很容易将 \"(0–9.9%)\" 误解为全局范围\n- 为什么影响接收：这构成选择性报告（cherry-picking）。CF 是本文方法的核心 trade-off，不完整披露会误导 AC/Reviewer 对方法局限性的判断。\n- 建议：Abstract 应报告全数据集范围，如 \"CF 0–21.1% zero-shot (dataset-dependent), ≤1.2% fine-tuned\"，或至少明确标注 \"on SciERC\"。\n\n**N3** [critical] 缺少与最直接竞争方法的 head-to-head 实验对比\n- 具体位置：§5, §6（Related Work）\n- 问题：论文将 grammar-only ablation 作为 GCD/BoostCD 的代理，但 BoostCD 的 boosting mechanism（交替 constrained/unconstrained decoding）是其核心贡献，grammar-only ablation 无法代表。同样，IterGen（backtracking-based semantic constraint）和 EnriCo（ASP-based decoding constraints）是做 semantic-level constrained decoding 的最直接竞品，均未进行实验对比。\n- 为什么影响接收：没有 head-to-head comparison，无法判断 OntoCoDec 的相对优势。Reviewer 和 AC 会质疑：既然已有方法也做 semantic constraint enforcement（IterGen via backtracking, EnriCo via ASP），OntoCoDec 的 forward-only masking 相比之下真正好在哪里？只有主观论述没有定量证据。\n- 建议：至少与 BoostCD 在 SciERC/DocRED 上做 head-to-head RE 实验（BoostCD 有开源代码）；如 IterGen/EnriCo 不可直接复现，应明确说明不可比原因。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [major] DocRED zero-shot DR 仅 45%，与论文整体 narrative 存在张力\n- 具体位置：Table 3（§5.2）；§1 contribution item 2\n- 问题：DocRED zero-shot Full S1 的 DR 从 18.46% 降至 10.21%，相对降幅仅 **45%**，远低于 SciERC 的 94%。论文通过将 zero-shot 定位为 \"diagnostic probe\"（§5 开头）来弱化此结果，但 zero-shot 正是 constrained decoding 最核心的使用场景——不需要 task-specific training 的即插即用方案。45% 的 DR 降幅意味着仍有过半违规未被消除。\n  §1 contribution item 2 说 \"yields 94–100%\"，但 this 94% 仅来自 SciERC 的 zero-shot 五路 ablation，DocRED zero-shot 的 45% 被排除在外。\n- 建议：在 §1 contribution 中诚实报告范围（如 \"45–100% depending on schema tightness\"）。同时讨论：对 high-κ̄ schema，zero-shot 下 semantic layer 为何效力下降——是 fallback 太频繁还是 entity registry 不准确？\n\n**W2** [major] κ̄ (constraint tightness) 证据不足以支撑其 prominence\n- 具体位置：Eq. (3)（§4）；§2 Background\n- 问题：κ̄ = 1 − |σ(r)|/|E|² 仅在 n=2 个数据集上验证了相关性（SciERC κ̄=0.333 vs. DocRED κ̄=0.842）。n=2 不足以建立任何统计意义上的相关。§2 将 κ̄ 提升为 Background 概念，§4 给予独立方程编号和段落——这种 prominence 远超 \"two data points show a pattern\" 的证据强度。\n  WikiEvents 有 245 constraints，但未报告 κ̄ 值或其与 AC reduction 的相关。\n- 建议：降低 κ̄ 的定位——作为 diagnostic observation 而非 contribution；报告 WikiEvents κ̄ 值；如果要保留 κ̄ 作为有意义的 metric，需要更多数据集（或 per-relation κ(r) 与 per-relation DR 的相关分析）。\n\n**W3** [major] Proposition 1 作为 \"贡献\" 的定位偏高\n- 具体位置：§1 contribution item 1；§3 Proposition 1\n- 问题：Proposition 1 证明 IE type constraints 超出 CFG expressiveness。证明本身是正确的（pumping lemma argument, Appendix O, 两个 case 完整）。但这个结论对 formal language theory 背景的读者而言是 **expected** 的——cross-field dependencies requiring random-access lookup 超出 PDA 能力是编译原理的基本知识（参见 attribute grammars 的经典动机）。论文在 §1 将 Proposition 1 作为第一个贡献列出，且用 \"establishing that IE type constraints require runtime state beyond CFG expressiveness\" 的措辞暗示这是一个独立理论发现。\n- 建议：将 Proposition 1 重新定位为 *motivation*（\"we formalize a well-known intuition...\"），而非 *contribution*。真正的贡献是实验验证 enabling dependency（grammar-only 24% vs. full 94%），这不需要 Proposition 1 的形式化证明也能成立。\n\n**W4** [major] WikiEvents 评估的可靠性不足以支撑 contribution claim\n- 具体位置：§5.4, Table 5；§1 contribution item 2b\n- 问题：WikiEvents fine-tuning composability 基于 **20 文档** test set（论文自己承认 \"preliminary\"）。Per-document variance 极高（Arg-F1 std/mean > 0.5, 35–47% documents scoring zero）。Zero-shot CF 率 14.9–21.1% 显著高于 RE 任务。尽管如此，§1 将 WikiEvents 列为 contribution item 2b (\"preliminary event extraction results on WikiEvents demonstrate generalization\")。\n  用 \"demonstrate generalization\" 描述一个 20-doc preliminary experiment，claim 强度与 evidence 强度不匹配。\n- 建议：保留 WikiEvents 结果但降级为 \"exploratory\" 或 \"case study\"；从 contribution list 中移除或用 \"initial evidence for\" 替代 \"demonstrate\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: §1 \"0.5–2% even after LoRA fine-tuning\" — Table 2 显示 Llama DocRED 是 0.49%，rounded 应为 \"~0.5–2%\" 或 \"0.5–2.0%\"，目前是准确的但边界很紧。\n\n- **M2**: Table 3 脚注中 XGrammar 残余 0.03% RV 来自 \"chimeric values\"（子词 token 拼接错误）——这是 XGrammar 已知 bug 还是 OntoCoDec 集成问题？应简要说明是否已上报/修复。\n\n- **M3**: §6 Related Work 主文仅 ~1/3 页。虽有 Appendix B（~2 页详细版），但主文中三段式（grammar-constrained decoding / schema-aware IE / constraint enforcement in IE）过于压缩，每段都是引用堆叠，缺乏对关键区分点的展开论述。对不看 Appendix 的读者，这降低了 positioning 的说服力。\n\n- **M4**: \"formal guarantees\" 措辞（§3.3 \"pair-based enforcement\" 描述）与 \"best-effort\" fallback（§4 grammar-first fallback）存在术语张力。DR 在 fallback 位置 structurally 无法为零（§4 \"all residual DR violations occur exclusively at fallback positions\"），所以 \"guarantee\" 不准确。建议统一为 \"best-effort with soft degradation\" 或类似表述。\n\n- **M5**: 引用验证结果：`regino2025kgcurator` 和 `formattax2026` 两条引用在 OpenAlex 中未找到匹配。`formattax2026` 标注为 arXiv:2604.03616，可能太新未索引，但应确认存在。8 条 mismatch 均为作者名编码差异（如 `šakota` vs `sakota`），非实质错误。\n\n- **M6**: §1 \"zero-shot DR drops 76–99% for calibrated models\" — 但 DocRED Mistral 的 DR 降幅 = (57.42−33.20)/57.42 = **42%**。Mistral 被排除为 \"boundary condition\"，但这个排除条件（\"calibrated models\"）在 §1 中不够透明。\n\n---\n\n## Missing References\n\n未发现重大遗漏。论文引用覆盖了 constrained decoding、schema-aware IE、post-hoc validation 三个维度的主要工作。Appendix B 的 extended related work 尤为全面。\n\n可能有价值的补充（非必须）：\n- Qi et al., 2024 \"AutoAct\" 或类似的 agentic IE 工作（作为 API-only models 场景的参考）\n- 更多关于 attribute grammars 的经典参考（支撑 Proposition 1 的 \"well-known\" 定位）\n\n---\n\n## 主要优势\n\n1. **问题定义清晰，实用价值明确**：IE 中 domain/range violation 是一个真实存在且系统性的问题（15–18% baseline violation rates），论文精确地量化了问题规模并提供了可操作的解决方案。\n\n2. **Ablation 设计系统化**：五路 ablation（unconstrained / grammar-only / semantic-only / full S1 / full S2）清楚地隔离了各层的贡献，enabling dependency 的实验证据（grammar-only 3% vs. semantic-only 24% vs. full 94%）比 Proposition 1 更有说服力。\n\n3. **Limitations section 异常诚实和全面**：涵盖 CF trade-off、English-only、LoRA-only、WikiEvents small test set、70B INT4 only、tokenizer assumptions、API-only models 排除——几乎回答了 reviewer 想问的所有问题。这是论文最大的优点之一。\n\n4. **统计严谨性**：所有 F1 比较均有 10,000-iteration paired bootstrap，report p-values 和 confidence intervals。DR reduction 在所有 fine-tuned settings 中均 significant (p<0.001)。\n\n5. **跨模型/跨 tokenizer 泛化**：在三种不同 tokenizer 架构（byte-level BPE × 2, SentencePiece）和 4 个模型上验证，证明方法不依赖特定模型架构。\n\n6. **CF↔DR trade-off 的诚实报告**：没有回避 CF 上升的问题，提供了因果分析（fallback positions, GENERIC↔X ambiguity）和缓解方案（beam search, fine-tuning）。\n\n---\n\n## 评分总结\n\n| 维度 | 分数 |\n|------|------|\n| Novelty | 2.5/5 |\n| Completeness | 3.0/5 |\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Overall Assessment | **3.0/5 (Findings)** |\n| Confidence | 4/5 |\n\n**主要判断依据**：\n- 算法新颖性有限：两层架构是 XGrammar（off-the-shelf）+ 有限状态注册表（dict + lookup + masking）的组合，技术深度不高。\n- Proposition 1 正确但 expected，κ̄ 证据不足，均不构成独立贡献。\n- 缺少与 BoostCD/IterGen/EnriCo 的 head-to-head 对比是最大实验缺口。\n- Abstract 中存在可验证的数字不一致（N1）和选择性报告（N2），损害 credibility。\n- 论文的实际价值（解决 IE violation 问题）和工程完整度（ablation + 统计 + 跨模型验证 + 诚实 limitations）适合 Findings 级别。\n- 若修复 N1–N3（数字准确性 + 补充 baseline 对比），可重新评估是否达到 Borderline Conference (3.5)。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-21T02:34:19.972104+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4727
}
```

</details>

---


### Assistant

_source line 1344 · 2026-05-21T02:34:27.325006+00:00_

审稿意见已提交给 Review Director。

总结：

**Overall: 3.0/5 (Findings)**

三个 Must-Fix 问题：
1. Abstract "94–100% DR reduction" 与 Table 2 不一致（Llama SciERC fine-tuned 实际为 91.9%）
2. CF 率选择性报告（Abstract 仅报 SciERC 的 0–9.9%，隐藏了 DocRED 12.02% 和 WikiEvents 21.1%）
3. 缺少与 BoostCD/IterGen/EnriCo 的 head-to-head 实验对比

四个 Should-Fix 问题：DocRED zero-shot 仅 45% 与整体 narrative 存在张力、κ̄ metric 证据不足（n=2）、Proposition 1 定位偏高、WikiEvents 20-doc 评估不足以支撑 contribution claim。

主要优势：问题定义清晰、ablation 系统化、Limitations 异常诚实、统计严谨、跨模型泛化验证充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 29

## Round 29

4 recorded events


### User

_source line 1345 · 2026-05-21T02:37:53.200855+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请对每个 Must-Fix 和 Should-Fix 问题逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注：你和 R1 是否在关键问题上有共识或分歧。

---

## Reviewer 1 — Round 1 审稿意见

**Overall Assessment**: 3.5 / 5 (Borderline Conference)

### Must-Fix 问题

**N1** [critical] 缺乏与现有 constrained decoding baseline 的直接实验对比
- grammar-only ablation 声称 "implements the same class of constraints" as GCD，但没有运行 GCD、BoostCD 或 CRANE 的实际代码。无法判断改进来自 semantic layer 创新还是实现差异。

**N2** [critical] κ̄ 作为预测性指标缺乏统计支撑
- 线性回归拟合（R²=0.86）仅基于 n=4 数据点（2 datasets × 2 models, df=2）。p=0.07。per-relation 分析进一步削弱解释力。

### Should-Fix 问题

**W1** [major] DocRED zero-shot DR 仅降 45%，主文讨论不足
- 详细错误分析仅在 Appendix D。对声称 "near-eliminates DR" 的论文而言，55% DR violations 在 DocRED 上幸存是核心发现。

**W2** [major] WikiEvents 评估统计功效不足
- 20 文档 test set，Clopper-Pearson 95% CI 上界 5.83%。应标记为 proof-of-concept。

**W3** [major] 70B 评估过于单薄
- 仅 INT4 推理，无消融、无微调。CF 0.07%→7.01%。单一配置无法提供两层架构在更大模型上是否 scale 的洞察。

**W4** [major] CF 在 Abstract/Conclusion 中的措辞与正文证据不一致
- Abstract 将 CF 以 "introduces CF side-effects" 轻描淡写。但 zero-shot CF 可达 12.02%（Table 3），且 CF-DR 是根本性耦合的。

**W5** [warning] Proposition 1 对无界实体集成立，但实际 IE 操作在有界集上
- 对有限实体集语言在技术上是 regular 的，但状态数呈指数增长使 DFA 不可行。这个 gap 仅在 Appendix 末尾简短提及。

### 小问题 M1-M5
- M1: "enabling dependency" 非标准形式化概念
- M2: DocRED 使用 dev set 应在主文说明
- M3: Figure 3 per-relation DR 仅 Llama
- M4: 评估协议描述可更清晰
- M5: Table 2 "(555 docs)" vs Table 1 "(551 docs)" 不一致

### 优势
1. 理论驱动架构设计原则清晰新颖
2. 消融实验设计充分
3. DR↔CF trade-off 诚实讨论
4. 实用部署导向
5. Appendix 体量大信息密度高

### 评分
| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 3.5/5 |
| Reproducibility | 4/5 |
| Overall | 3.5/5 (Borderline Conference) |
| Confidence | 4/5 |

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

_source line 1346 · 2026-05-21T02:39:50.077059+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 对 Reviewer 1 的交叉回应\n\n### 逐条回应总结\n\n**Must-Fix:**\n- **[AGREE] R1-N1** (缺 baseline 对比): 完全同意，与我的 N3 完全一致。补充：EnriCo (ASP-based) 也应纳入比较。\n- **[AGREE] R1-N2** (κ̄ 统计不足): 同意。补充：κ̄ 独立取值仅 n=2（schema 属性不随模型变化），自由度为零，任何回归无意义。WikiEvents 未报告 κ̄ 是遗漏。\n\n**Should-Fix:**\n- **[AGREE] R1-W1** (DocRED 45%): 完全同意，与我的 W1 一致。§1 contribution \"yields 94–100%\" 排除了 DocRED 45% 却未说明。\n- **[AGREE] R1-W2** (WikiEvents 20-doc): 同意，与我的 W4 一致。\"demonstrate generalization\" 应降级为 \"initial evidence\"。\n- **[AGREE] R1-W3** (70B 单薄): 同意。CF 0.07%→7.01% 未充分分析。\"7–70B\" 范围声明可能给人不恰当的覆盖印象。\n- **[AGREE] R1-W4** (CF 措辞不一致): 强烈同意，且认为应**升级为 Must-Fix**。Abstract \"(0–9.9% zero-shot)\" 仅覆盖 SciERC，但 DocRED CF=12.02%, WikiEvents CF=21.1%。这是选择性报告。\n- **[REBUT] R1-W5** (Proposition 1 bounded gap): 部分反驳。Appendix O 已讨论 finite entity sets（exponential DFA + open-vocabulary text spans 使 unbounded 模型更贴近实际）。建议在主文加一句限定即可。我从不同角度（overclaimed positioning）也批评了 Proposition 1。\n\n**Minor:**\n- [AGREE] M1, M3, M4\n- [REBUT] M2: DocRED dev set 已在主文脚注和 Table 3 caption 中说明\n- [未能验证] M5: 我在 LaTeX 源文件中 Table 1 和 Table 2 都看到 \"551 docs\"，未找到 \"555\"\n\n### 关键共识与分歧\n\n**强共识**: baseline 对比缺失、DocRED 45%、WikiEvents 20-doc、CF 选择性报告\n**分歧**: Excitement（R1: 3.5, R2: 2.5）。R1 更认可理论驱动设计的新颖性，R2 认为 Proposition 1 结论 expected、两层架构技术深度有限。\n**R2 独有发现**: Abstract \"94–100%\" 与 Table 2 Llama-SciERC 91.9% 的数字不一致（N1）\n\n**Overall: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)**\n差异根源在 novelty/excitement 判断，soundness 一致 (3.5/5)。",
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
    "text": "## Reviewer 2 — 对 Reviewer 1 的交叉回应\n\n### 逐条回应总结\n\n**Must-Fix:**\n- **[AGREE] R1-N1** (缺 baseline 对比): 完全同意，与我的 N3 完全一致。补充：EnriCo (ASP-based) 也应纳入比较。\n- **[AGREE] R1-N2** (κ̄ 统计不足): 同意。补充：κ̄ 独立取值仅 n=2（schema 属性不随模型变化），自由度为零，任何回归无意义。WikiEvents 未报告 κ̄ 是遗漏。\n\n**Should-Fix:**\n- **[AGREE] R1-W1** (DocRED 45%): 完全同意，与我的 W1 一致。§1 contribution \"yields 94–100%\" 排除了 DocRED 45% 却未说明。\n- **[AGREE] R1-W2** (WikiEvents 20-doc): 同意，与我的 W4 一致。\"demonstrate generalization\" 应降级为 \"initial evidence\"。\n- **[AGREE] R1-W3** (70B 单薄): 同意。CF 0.07%→7.01% 未充分分析。\"7–70B\" 范围声明可能给人不恰当的覆盖印象。\n- **[AGREE] R1-W4** (CF 措辞不一致): 强烈同意，且认为应**升级为 Must-Fix**。Abstract \"(0–9.9% zero-shot)\" 仅覆盖 SciERC，但 DocRED CF=12.02%, WikiEvents CF=21.1%。这是选择性报告。\n- **[REBUT] R1-W5** (Proposition 1 bounded gap): 部分反驳。Appendix O 已讨论 finite entity sets（exponential DFA + open-vocabulary text spans 使 unbounded 模型更贴近实际）。建议在主文加一句限定即可。我从不同角度（overclaimed positioning）也批评了 Proposition 1。\n\n**Minor:**\n- [AGREE] M1, M3, M4\n- [REBUT] M2: DocRED dev set 已在主文脚注和 Table 3 caption 中说明\n- [未能验证] M5: 我在 LaTeX 源文件中 Table 1 和 Table 2 都看到 \"551 docs\"，未找到 \"555\"\n\n### 关键共识与分歧\n\n**强共识**: baseline 对比缺失、DocRED 45%、WikiEvents 20-doc、CF 选择性报告\n**分歧**: Excitement（R1: 3.5, R2: 2.5）。R1 更认可理论驱动设计的新颖性，R2 认为 Proposition 1 结论 expected、两层架构技术深度有限。\n**R2 独有发现**: Abstract \"94–100%\" 与 Table 2 Llama-SciERC 91.9% 的数字不一致（N1）\n\n**Overall: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)**\n差异根源在 novelty/excitement 判断，soundness 一致 (3.5/5)。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-21T02:39:54.258524+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4181
}
```

</details>

---


### Assistant

_source line 1348 · 2026-05-21T02:39:59.474327+00:00_

交叉回应已提交。

核心结论：R1 和 R2 在 4 个关键问题上有强共识（baseline 缺失、DocRED 45%、WikiEvents 20-doc、CF 选择性报告）。主要分歧在 Excitement/Novelty 评估——R1 认为理论驱动设计有价值（3.5），R2 认为技术深度不足（2.5）。R2 独有发现是 Abstract "94–100%" 的数字不一致（实际 91.9–100%）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 30

## Round 30

126 recorded events


### User

_source line 1349 · 2026-05-22T10:43:23.766893+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## 审稿目标
对以下论文进行严格审稿，像顶会最严格的审稿人一样评估。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf`

## Venue 要求
- **Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **类型**: Long paper, ≤8 页正文 + 无限参考文献页
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名**: Double-blind
- **Limitations/Ethics**: 不计入页数限制，但必须包含
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit

## 你的审查重点

### 1. 新颖性评估
- 核心贡献（两层 grammar+semantic 约束、自动编译 IE ontology 为 token-level masks）的新颖度如何？
- 与现有工作的差异化是否充分？特别是 vs. GCD (Geng et al., 2023)、XGrammar (Dong et al., 2025)、PICARD (Scholak et al., 2021)、Mündler et al. (2025)
- Proposition 1 是否是一个 novel contribution，还是 well-known intuition 的形式化？定位是否恰当？
- κ̄ (constraint tightness) 作为度量的贡献是否足够？

### 2. 叙事一致性 & 写作质量
- Abstract 中的数字声明是否与正文 Table 数据一致？特别关注：
  - "DR ≤ 0.09%" 是否在所有配置下成立？
  - "CF ≤ 1.3%" 是否仅限于特定配置？是否选择性报告？
  - DR reduction 范围（"45-99%"、"76-99%"、"94%"等不同表述）是否一致？
- Introduction 中的 contribution claims 是否与实验结果完全匹配？
- "enforcement" vs "guarantee" 等术语使用是否一致？
- WikiEvents 结果是否被 overclaim 为 "generalization" 而实际仅 20 文档？
- 70B 结果的定位是否恰当（feasibility check vs. full evaluation）？

### 3. 相关工作覆盖
- §6 Related Work + Appendix B 是否充分覆盖了：
  - Constrained decoding for structured generation (GCD, BoostCD, XGrammar, Outlines, SynCode, CRANE)
  - Schema-aware IE (GoLLIE, KnowCoder, CodeIE, ADELIE)
  - Post-hoc validation (ODKE+, SPIRES/OntoGPT, OntoLogX, EnriCo, IterGen)
- 是否有遗漏的关键近期工作（2024-2026）？
- 引用是否全部真实？特别注意 arXiv preprints 的引用格式和真实性

### 4. 完整性检查
- Limitations 是否充分覆盖了方法的关键限制？
- Ethics Statement 是否恰当？
- Responsible NLP Checklist 填写是否准确？
- 论文是否 self-contained（读者是否需要阅读 Appendix 才能理解主文核心论点）？

### 5. 格式审查
- 正文 ≤8 页？
- 匿名合规（无 self-citation leaks、无 identifying information）？
- Figure/Table 标注是否清晰？
- 参考文献格式是否统一？

## 输出格式
请按以下结构输出你的审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条，S1, S2, ...)
3. **Weaknesses** (逐条，W1, W2, ...，按严重度排序：Must-Fix → Should-Fix → Minor)
4. **Questions** (需要作者澄清的问题)
5. **Missing References** (遗漏的重要相关工作)
6. **Overall Assessment** (评分 + 置信度 + 1-2 句总评)
7. **Detailed Comments** (逐节详细意见)

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

_source line 1350 · 2026-05-22T10:43:35.830510+00:00_

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

_source line 1351 · 2026-05-22T10:43:36.487085+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-22T10:43:36.640018+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
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
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-22T10:43:36.640478+00:00_



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

_source line 1354 · 2026-05-22T10:43:41.237884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
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
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 1355 · 2026-05-22T10:43:42.195865+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-10",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1356 · 2026-05-22T10:43:42.497314+00:00_

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

_source line 1357 · 2026-05-22T10:43:47.756943+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the web search results, here's what I found about ACL Rolling Review 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to read the paper and get a first impression, search for related work, and state in the review if they did not check some major parts, such as proofs. Reviewers are provided with a checklist to flag problems that other people may have missed.

Cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews are considered egregious.

## Revie
…[truncated 945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6519
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-22T10:43:49.112869+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifac
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6917
}
```

</details>

---


### Tool result

_source line 1359 · 2026-05-22T10:43:49.113520+00:00_

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
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 6217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6616
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-22T10:43:54.989150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1361 · 2026-05-22T10:43:55.543797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 1362 · 2026-05-22T10:43:55.947878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 1363 · 2026-05-22T10:43:55.948343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-22T10:43:56.910784+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1366
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-22T10:43:56.913964+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 965
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-22T10:43:56.914418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1367 · 2026-05-22T10:43:57.467478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1368 · 2026-05-22T10:43:57.920261+00:00_



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


### Tool result

_source line 1369 · 2026-05-22T10:43:58.925119+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-22T10:43:58.925530+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all dimensions/criteria, their scales, and descriptions. Include Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other criteria."
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
    "prompt": "Extract the complete review form: all dimensions/criteria, their scales, and descriptions. Include Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other criteria."
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-22T10:44:04.005690+00:00_

# ACL Rolling Review Form - Complete Structure

## Primary Review Dimensions

**Soundness** (1-5 scale with 0.5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong with minor gaps
- 3: Acceptable with minor support needed
- 2: Poor - main claims lack support
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with 0.5 increments)
- 5: Highly Exciting - would recommend to others
- 4: Exciting - would mention to others
- 3: Interesting - might attend presentation
- 2: Potentially Interesting - limited personal resonance
- 1: "Not Exciting: this paper does not resonate with me"

**Overall Assessment** (1-5 scale with 0.5 increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Resubmit next cycle
- 1: Do not resubmit

## Secondary Evaluation Criteria

**Reproducibility** (1-5 scale): Assesses whether readers can replicate results or build upon findings

**Reviewer Confidence** (1-5 scale): Evaluates reviewer's familiarity and thoroughness

**Datasets & Software** (1-5 scales): Rates value of released resources to the community

**Ethics & Limitations**: Sections for societal impact, ethical concerns, and potential ethics committee referral

**Author Identity** (1-5 scale): Tracks reviewer's knowledge of authorship

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5080
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-22T10:44:09.090970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1373 · 2026-05-22T10:44:10.152027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1374 · 2026-05-22T10:44:10.806307+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1715
}
```

</details>

---


### Tool call

_source line 1375 · 2026-05-22T10:44:10.806788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-22T10:44:11.112459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1377 · 2026-05-22T10:44:12.272394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1378 · 2026-05-22T10:44:12.929210+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2777
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-22T10:44:14.626664+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3819
}
```

</details>

---


### Tool result

_source line 1380 · 2026-05-22T10:44:14.778381+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3665
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-22T10:44:15.131622+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2859
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-22T10:44:23.118125+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "11-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-22T10:44:27.453323+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 612.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 615.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.6}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 372.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.0}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.8}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4335
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-22T10:44:27.555901+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read LaTeX source sections",
  "subagent_type": "Explore",
  "prompt": "I need to read several LaTeX source files for a paper review. The paper is at:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/\n\nRead the following files completely and report their full contents back to me:\n1. abstract.tex (or abstract.*)\n2. section1_introduction_draft.tex (or similar)\n3. section6_related_work.tex (or similar)\n4. section7_conclusion_compressed.tex (or similar)\n\nAlso find and read the bibliography file (relwork_new_entries.bib) to check reference entries.\n\nFor each file, report the complete text content. This is for a paper review - I need exact text to verify claims.\n\nSearch breadth: medium"
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
    "description": "Read LaTeX source sections",
    "subagent_type": "Explore",
    "prompt": "I need to read several LaTeX source files for a paper review. The paper is at:\n/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/\n\nRead the following files completely and report their full contents back to me:\n1. abstract.tex (or abstract.*)\n2. section1_introduction_draft.tex (or similar)\n3. section6_related_work.tex (or similar)\n4. section7_conclusion_compressed.tex (or similar)\n\nAlso find and read the bibliography file (relwork_new_entries.bib) to check reference entries.\n\nFor each file, report the complete text content. This is for a paper review - I need exact text to verify claims.\n\nSearch breadth: medium"
  }
}
```

</details>

---


### Tool call

_source line 1385 · 2026-05-22T10:44:29.415554+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper -type f \\( -name \"*.tex\" -o -name \"*.bib\" \\) | head -50"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper -type f \\( -name \"*.tex\" -o -name \"*.bib\" \\) | head -50"
  }
}
```

</details>

---


### Tool result

_source line 1386 · 2026-05-22T10:44:29.566639+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/relwork_new_entries.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/case_study_kappa_dr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic
…[truncated 4530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1387 · 2026-05-22T10:44:31.274472+00:00_

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

_source line 1388 · 2026-05-22T10:44:31.676788+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
4	The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} achieves deployment-grade type compliance: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $<$0.5\% true-positive loss); residual CF ($\leq$1.3\%) represents \emph{violation conversion}---ontologically invalid triples (DR) are replaced by individually valid but type-inconsistent ones---resolved by beam search on SciERC (\S\ref{sec:beam-results}).
7	Zero-shot evaluation serves as a diagnostic, revealing dataset- and calibration-dependent effectiveness (45--99\% DR reduction, total violation reduction 31\%; \S\ref{sec:experiments}) and establishing constraint tightness ($\bar{\kappa}$) as a predictive factor.
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across five autoregressive LMs (7--70B; 70B zero-shot and LoRA in \S\ref{sec:70b-re
…[truncated 103 chars]

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

_source line 1389 · 2026-05-22T10:44:31.677245+00:00_

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

_source line 1390 · 2026-05-22T10:44:31.878365+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement; no method provides both semantic awareness and hard constraint enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time con
…[truncated 2290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1391 · 2026-05-22T10:44:31.878828+00:00_

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

_source line 1392 · 2026-05-22T10:44:32.130099+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, SynCode~\cite{ugare2024syncode}, and related systems~\cite{beurer-kellner2023lmql,park2024grammar,jsonschemabench2025} enforce format validity via CFG-based token masking.
8	NeuroLogic Decoding~\cite{lu2021neurologic} enforces predicate-logic constraints via beam-level reranking; OntoCoDec applies constraints per-token via forward masking, avoiding beam-width dependence.
9	In code generation, PICARD~\cite{scholak2021picard} and \citet{pldi2025_type_constrained_codegen} compile type systems into prefix automata, but IE type environments accumulate dynamically (\S\ref{sec:composition}).
10	
11	\paragraph{Schema-aware IE.}
12	GoLLIE~\cite{sainz2024gollie}, KnowCoder~\cite{knowcoder_acl2024}, GUIDEX~\cite{guidex2025}, GenIE~\cite{josifoski2022genie}, TANL~\cite{paolini2021tanl}, REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, and others~\cite{fei2022lasuie,wang2022deepstruct,lu2022uie,lou2023usm,zhou2024universalner} encode ontology structure or frame IE as structured generation, though schema compliance gaps persist~\cite{wadhwa2023revisiting}.
13	GoLLIE and KnowCoder embed schema knowledge via code-style prompts, achieving structural compliance without runtime enforcement; GoLLIE-7B eliminates DR via its dataclass format but at severe coverage cost (R-F1${=}$0.0, 46\% empty output), while OntoCoDec with LoRA achieves R-F1${=}$45.47 at DR${=}$0.09\%, surpassing KnowCoder-7B (supervised R-F1${=}$40.0)~\cite{knowcoder_acl2024}.
14	
15	\paragraph{Constraint enforcement in IE.}
16	\citet{roth_yih_2004} and \citet{riedel2010modeling} formulated hard type constraints via ILP; post-hoc validation~\cite{khorshidi2025odke,spires_2024,ontologx_2025} detects violations after generation
…[truncated 638 chars]

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

_source line 1393 · 2026-05-22T10:44:32.130498+00:00_

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

_source line 1394 · 2026-05-22T10:44:32.130707+00:00_

1	% Section 7 — Discussion and Conclusion
2	
3	OntoCoDec translates IE ontologies into composable token-level constraints via a two-layer architecture: LoRA + greedy S1 achieves DR\,$\leq$\,0.09\% ($<$0.5\% recall cost), CF\,$\leq$\,1.3\%; beam ($k{=}4$) eliminates all violations on SciERC (1.54$\times$ latency); zero-shot DR drops 76--99\% for calibrated models (7--8B; 70B LoRA in \S\ref{sec:70b-results}); triple validity analysis (\S\ref{sec:downstream-impact}) confirms 100\% schema compliance.
4	

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

_source line 1395 · 2026-05-22T10:44:32.482388+00:00_

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

_source line 1396 · 2026-05-22T10:44:32.734192+00:00_

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
…[truncated 33103 chars]

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


### Tool result

_source line 1397 · 2026-05-22T10:44:52.106518+00:00_

Perfect! I've successfully read all the requested files. Here's the complete content report for your paper review:

## File Contents Report

### 1. abstract.tex
Complete text (10 lines):
The abstract presents **OntoCoDec**, a framework translating IE ontologies into composable token-level decoding constraints via a two-layer architecture:
- Grammar layer: compiles ontology constraints into context-free grammars (JSON, vocabulary)
- Semantic layer: interprets type constraints at runtime via stateful token masking over an entity registry

Key claims:
- Achieves DR ≤ 0.09% at R-F1 43-46% (±0.8 pp, <0.5% true-positive loss)
- Residual CF ≤ 1.3% represents violation conversion (resolved by beam search on SciERC)
- Zero-shot evaluation: 45-99% DR reduction, 31% total violation reduction
- Validated on RE (SciERC, DocRED) + WikiEvents, across five LMs (7-70B), three tokenizer families

### 2. section1_introduction_draft.tex
Complete text (28 lines):
Key claims include:
- Baseline violations: 15.4% on SciERC, 18.5% on DocRED under zero-shot; 0.5-2% after LoRA fine-tuning
- Schema-informed prompting reduces violations by 62% on average but per-relation unreliable (Evaluate-for increases by 5.8 pp)
- Grammar-constrained decoding ensures syntactic well-formedness but cannot encode cross-field semantic constraints
- Post-hoc filtering discards up to 48% of predictions including true positives
- OntoCoDec contributions: decidability analysis, two-layer architecture, automatic compilation from IE ontologies, no constraint-specific training
- Results: DR ≤ 0.09% at R-F1 43-46%, CF ≤ 1.3% fine-tuned; zero-shot DR drops 76-99%; beam (k=4) eliminates all violations on SciERC (1.54× latency)
- Empirical enabling dependency: neither layer alone exceeds 24% DR reduction

### 3. section6_related_work.tex
Complete text (20 lines):
Three positioning axes:
1. **Constrained decoding**: XGrammar, Outlines, SynCode enforce format validity; NeuroLogic uses beam-level reranking; PICARD/type-cons
…[truncated 2328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 24550
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-22T10:44:57.084926+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 1399 · 2026-05-22T10:44:57.437868+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 1400 · 2026-05-22T10:44:57.941657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 1401 · 2026-05-22T10:44:58.042660+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1402 · 2026-05-22T10:44:58.846600+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-22T10:44:58.999321+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-22T10:44:58.999692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 1405 · 2026-05-22T10:44:59.352471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 1406 · 2026-05-22T10:44:59.907153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1407 · 2026-05-22T10:44:59.907587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1408 · 2026-05-22T10:45:00.011997+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 659
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-22T10:45:00.766389+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-22T10:45:06.799860+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "21-30",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "21-30",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1411 · 2026-05-22T10:45:08.056455+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.1}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 478.2}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 532.4}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.0}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 451.0}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.0}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.0}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.3}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1256
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-22T10:45:11.672893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 1413 · 2026-05-22T10:45:12.177877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 1414 · 2026-05-22T10:45:13.086870+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1413
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-22T10:45:13.090067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 912
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-22T10:45:13.091248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-22T10:45:13.594928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1418 · 2026-05-22T10:45:14.048287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 1419 · 2026-05-22T10:45:14.099042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p21.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-22T10:45:14.652494+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 1421 · 2026-05-22T10:45:14.657018+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p22.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 1422 · 2026-05-22T10:45:15.229190+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1130
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-22T10:45:15.531458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 874
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-22T10:45:20.704934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p23.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 1425 · 2026-05-22T10:45:21.260091+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p24.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-22T10:45:21.661437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p25.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-22T10:45:22.875218+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2170
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-22T10:45:22.878182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p26.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-22T10:45:23.991656+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2731
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-22T10:45:23.992263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p27.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool call

_source line 1431 · 2026-05-22T10:45:23.992500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p28.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1432 · 2026-05-22T10:45:23.997542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2336
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-22T10:45:25.457033+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2578
}
```

</details>

---


### Tool result

_source line 1434 · 2026-05-22T10:45:25.859846+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1867
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-22T10:45:25.911103+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1918
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-22T10:45:31.943694+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p29.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 1437 · 2026-05-22T10:45:32.797927+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

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

_source line 1438 · 2026-05-22T10:45:32.949068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p30.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 1439 · 2026-05-22T10:45:33.300749+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98.

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

_source line 1440 · 2026-05-22T10:45:33.809261+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "31-34",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "31-34",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-22T10:45:34.547883+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 31, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p31.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 468.9}, {\"page\": 32, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p32.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 479.6}, {\"page\": 33, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p33.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.5}, {\"page\": 34, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p34.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 225.0}], \"total_pages\": 34, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 738
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-22T10:45:37.923395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p31.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---


### Tool call

_source line 1443 · 2026-05-22T10:45:38.425890+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p32.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---


### Tool result

_source line 1444 · 2026-05-22T10:45:39.331580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-22T10:45:39.332958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-22T10:45:39.333392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p33.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---


### Tool call

_source line 1447 · 2026-05-22T10:45:39.636892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p34.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_17/_pdf_images/submitted_p34.png"
  }
}
```

</details>

---


### Tool result

_source line 1448 · 2026-05-22T10:45:40.242344+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool result

_source line 1449 · 2026-05-22T10:45:40.345885+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-22T10:45:48.838364+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read abstract and intro LaTeX",
  "subagent_type": "Explore",
  "prompt": "Read the following files in full from the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/ and return their complete text:\n\n1. abstract.tex\n2. section1_introduction_draft.tex\n3. section5_scierc_draft.tex\n4. section5_docred_draft.tex\n5. section5_wikievents_draft.tex\n6. section5_crossmodel_draft.tex\n7. section3_violation_landscape.tex (violation landscape section)\n8. section5_runtime.tex\n\nI need the EXACT text of each file to verify numerical claims. Return verbatim content.\n\nSearch breadth: quick"
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
    "description": "Read abstract and intro LaTeX",
    "subagent_type": "Explore",
    "prompt": "Read the following files in full from the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/ and return their complete text:\n\n1. abstract.tex\n2. section1_introduction_draft.tex\n3. section5_scierc_draft.tex\n4. section5_docred_draft.tex\n5. section5_wikievents_draft.tex\n6. section5_crossmodel_draft.tex\n7. section3_violation_landscape.tex (violation landscape section)\n8. section5_runtime.tex\n\nI need the EXACT text of each file to verify numerical claims. Return verbatim content.\n\nSearch breadth: quick"
  }
}
```

</details>

---


### Tool call

_source line 1451 · 2026-05-22T10:45:50.394862+00:00_

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

_source line 1452 · 2026-05-22T10:45:50.445474+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
4	The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} achieves deployment-grade type compliance: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $<$0.5\% true-positive loss); residual CF ($\leq$1.3\%) represents \emph{violation conversion}---ontologically invalid triples (DR) are replaced by individually valid but type-inconsistent ones---resolved by beam search on SciERC (\S\ref{sec:beam-results}).
7	Zero-shot evaluation serves as a diagnostic, revealing dataset- and calibration-dependent effectiveness (45--99\% DR reduction, total violation reduction 31\%; \S\ref{sec:experiments}) and establishing constraint tightness ($\bar{\kappa}$) as a predictive factor.
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across five autoregressive LMs (7--70B; 70B zero-shot and LoRA in \S\ref{sec:70b-re
…[truncated 103 chars]

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

_source line 1453 · 2026-05-22T10:45:50.546392+00:00_

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

_source line 1454 · 2026-05-22T10:45:50.647303+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
9	At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
15	Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement; no method provides both semantic awareness and hard constraint enforcement.
16	
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time con
…[truncated 2290 chars]

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

_source line 1455 · 2026-05-22T10:45:50.697927+00:00_

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

_source line 1456 · 2026-05-22T10:45:50.899278+00:00_

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
…[truncated 5863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-22T10:45:50.899667+00:00_

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

_source line 1458 · 2026-05-22T10:45:51.301656+00:00_

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
55	F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
56	Grammar-only $\uparrow$DR: vocabula
…[truncated 1717 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1459 · 2026-05-22T10:45:51.302148+00:00_

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

_source line 1460 · 2026-05-22T10:45:51.503409+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Extension to Event Extraction}
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
42	  & Uncon
…[truncated 2120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1461 · 2026-05-22T10:45:51.503865+00:00_

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

_source line 1462 · 2026-05-22T10:45:51.705059+00:00_

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
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1463 · 2026-05-22T10:45:51.705461+00:00_

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

_source line 1464 · 2026-05-22T10:45:51.906587+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), near-eliminating DR (DR\,$\leq$\,0.09\%) with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations on SciERC under favorable conditions (1.54$\times$ latency).
8	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe to isolate constraint effects; R-F1 2--8 reflects absent task-specific training, not method failure.
9	The deployment-relevant evaluation is the fine-tuned setting (R-F1 40--46\%), where constraints compose with parameter optimization without degrading performance.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	All constraints are defined from schema-level supervision, independently of the evaluation split.
15	The framework handles both sources without modification.
16	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
17	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), 
…[truncated 385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1465 · 2026-05-22T10:45:51.907110+00:00_

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

_source line 1466 · 2026-05-22T10:45:51.957669+00:00_

1	% Runtime overhead (inline paragraph, no subsection header to save space)
2	
3	\paragraph{Runtime overhead.}
4	\label{sec:runtime}
5	S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
6	Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
7	
8	\paragraph{Beam search compatibility.}
9	\label{sec:beam-results}
10	With LoRA, beam search ($k{=}4$)~\cite{anderson2017guided} eliminates all four violation types on SciERC (R-F1 44--46); zero-shot beam achieves DR${=}$0\% on both datasets (CF response is model-dependent; Appendix~\ref{app:beam-search}).
11	Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
12	
13	% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
14	\paragraph{70B evaluation.}
15	\label{sec:70b-results}
16	On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on both datasets: SciERC 6.41\%\,$\to$\,0\% (R-F1 11.24), DocRED 14.98\%\,$\to$\,0\% (R-F1 13.05); CF rises to 3.50--7.01\%, comparable to 8B zero-shot CF.
17	% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
18	LoRA fine-tuning confirms scale-independent composability: SciERC DR 1.50\%\,$\to$\,0\% (R-F1 44.53, $-$0.20\,pp); DocRED (200-document subset; Appendix~\ref{app:power-analysis}) DR 0.22\%\,$\to$\,0\% (R-F1 43.95, $+$0.15\,pp); CF drops from 3.50\% (zero-shot) to 0.18--1.33\% (LoRA), consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).
19	
20	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
21	\paragraph{Comparison with grammar-constrained approaches.}
22	\label{sec:constrained-baselines}
23	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, ro
…[truncated 581 chars]

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

_source line 1467 · 2026-05-22T10:47:39.459306+00:00_

Here are the complete texts of all requested files from the paper directory:

---

## 1. abstract.tex

```
\begin{abstract}
We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
Composed with LoRA fine-tuning, \textsc{OntoCoDec} achieves deployment-grade type compliance: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $<$0.5\% true-positive loss); residual CF ($\leq$1.3\%) represents \emph{violation conversion}---ontologically invalid triples (DR) are replaced by individually valid but type-inconsistent ones---resolved by beam search on SciERC (\S\ref{sec:beam-results}).
Zero-shot evaluation serves as a diagnostic, revealing dataset- and calibration-dependent effectiveness (45--99\% DR reduction, total violation reduction 31\%; \S\ref{sec:experiments}) and establishing constraint tightness ($\bar{\kappa}$) as a predictive factor.
The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on Wiki
…[truncated 27421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 110620
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-22T10:50:32.501875+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained decoding structured information extraction 2025 2026 ACL EMNLP"
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
    "query": "constrained decoding structured information extraction 2025 2026 ACL EMNLP"
  }
}
```

</details>

---


### Tool call

_source line 1469 · 2026-05-22T10:50:32.502352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "schema-guided constrained generation ontology LLM 2025 NLP"
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
    "query": "schema-guided constrained generation ontology LLM 2025 NLP"
  }
}
```

</details>

---


### Tool result

_source line 1470 · 2026-05-22T10:50:40.085274+00:00_

Web search results for query: "constrained decoding structured information extraction 2025 2026 ACL EMNLP"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-industry/"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/pdf/2506.14901"},{"title":"Beyond Free-Form Text: How Constrained Decoding is Reshaping Structured Generation in LLMs | by Brijesh Nambiar | Medium","url":"https://medium.com/@brijeshrn/beyond-free-form-text-how-constrained-decoding-is-reshaping-structured-generation-in-llms-5f7a38bef259"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"}]

Based on the search results, here's what I found regarding constrained decoding and structured information extraction in 2025-2026:

## Recent Publications and Work

A 2025 paper by David M. Schmidt and Philipp Cimiano titled "Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied
…[truncated 1394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7583
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-22T10:50:40.788550+00:00_

Web search results for query: "schema-guided constrained generation ontology LLM 2025 NLP"

Links: [{"title":"Schema-Constrained Grammar-Guided Generation of GQL ...","url":"https://ceur-ws.org/Vol-4085/paper12.pdf"},{"title":"Ontology-Grounded LLM Construction","url":"https://www.emergentmind.com/topics/ontology-grounded-llm-construction"},{"title":"LLM-Empowered Knowledge Graphs","url":"https://www.emergentmind.com/topics/llm-empowered-knowledge-graph-construction"},{"title":"Knowledge Graphs generation using LLMs for Ontology Instantiation and Development | by Sachish Binha | Medium","url":"https://medium.com/@sachish.binha/knowledge-graphs-generation-using-llms-for-ontology-instantiation-and-development-89097bde4339"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Conversational Control with Ontologies for Large Language Models: A Lightweight Framework for Constrained Generation","url":"https://arxiv.org/pdf/2604.04450"}]

Based on the search results, here's what I found regarding schema-guided constrained generation, ontology, and LLMs in 2025 NLP:

## Schema-Guided Constrained Generation

Grammar-constrained generation can enhance the LLM's graph query generation capabilities and improve the syntactic accuracy without requiring any fine-tuning or additional specialised models.

## Ontology-Grounded LLM Approaches

Extraction prompts specify the connection map (allowed (entity, predicate, entity) patterns), required fields, cardinalities, and ID conventions. Few-shot examples and natural language class definitions are embedded directly in the prompt, ensuring schema compliance at output time.

## LLM-Empowered Knowledge Graph Construction (2025)

Recent 2025 research shows two complementary paradigms: Schema-Based Approaches leverage LLMs to instantiate or expand upon predefined ontologies, with extraction closely guided by explicit schemas, which may originate from expert-designed frameworks 
…[truncated 824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8286
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-22T10:53:37.084013+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见 — Round 1 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 1. Summary\n\n本文提出 OntoCoDec，一个将 IE ontology 自动编译为 token-level 解码约束的框架。核心设计是两层架构：grammar layer（基于 XGrammar 的 CFG）保证 JSON 结构和词表合规，semantic layer（基于运行时实体注册表的有状态 logit masking）执行 domain/range 类型约束。论文通过 Proposition 1（pumping lemma 证明）论证跨字段类型约束超出 CFG 表达能力，并在 3 个数据集、5 个模型、2 个 IE 任务上进行了系统评估。LoRA + 约束解码在 R-F1 43–46% 下将 DR 降至 ≤0.09%，但引入 CF 违规（≤1.3%）作为 violation conversion 的代价。\n\n---\n\n## 2. Strengths\n\n**S1. 问题驱动的系统化框架设计**\n将 IE ontology 约束自动编译为解码时约束是一个实际且有价值的工程贡献。与需要约束特定训练的方法（GoLLIE, KnowCoder）相比，OntoCoDec 的\"零训练开销\"和自动编译特性有明确的实用优势。ontology → grammar → mask 的编译管道有清晰的工程逻辑。\n\n**S2. 评估的系统性和全面性**\n3 个数据集（SciERC, DocRED, WikiEvents）、5 个模型（7B–70B）、3 个 tokenizer family、zero-shot + LoRA fine-tuning、greedy + beam search、五路消融，加上 bootstrap 显著性检验和 Bonferroni 校正——评估覆盖度在同类工作中属于上乘。Table 1 的五路消融清楚地隔离了各层贡献。\n\n**S3. 诚实透明的 Limitations**\nLimitations section 覆盖了 CF trade-off、评估范围（模型规模、fine-tuning 方法、语言限制）、工程约束（API-only 模型不适用、tokenizer 依赖性）等关键限制，比多数投稿更加坦诚。CF↔DR trade-off 的分析（Appendix C, causal tracing）提供了对失败模式的真实理解。\n\n**S4. 低运行时开销**\ngreedy S1 仅增加 10–13% 延迟，编译为 one-time < 0.5s，scalability benchmark 到 200 entity types / 1000 relations 仍保持 2–3% overhead。这对实际部署有直接价值。\n\n**S5. Decidability analysis 提供理论基础**\nProposition 1 及其 pumping lemma 证明（Appendix O）为两层架构的必要性提供了形式化依据，而非仅凭直觉。Appendix 中的 finite entity set 分析补充了理论与实践之间的联系。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [critical] Abstract 与 Introduction 的 DR 降幅数字不一致**\n- Abstract: \"45–99% DR reduction\"（§Abstract）\n- Introduction: \"DR drops 76–99% for calibrated models\"（§1, Contribution 2）\n- Table 4 的实际数据覆盖 6 个 model-dataset 组合（8B zero-shot）：\n  - SciERC: Qwen 94%, Llama 99%, Mistral 76%\n  - DocRED: Qwen 45%, Llama 90%, Mistral 42%\n- 全范围为 **42–99%**，而非 45–99%（Mistral DocRED 为 42%，被排除且未说明）\n- Introduction 声称\"76–99% for calibrated models\"，但 DocRED Qwen（calibrated model）仅 45%，远低于 76%。除非 Qwen 在 DocRED 上不被视为\"calibrated\"，否则此声明与数据矛盾。\n- **建议**：统一为准确范围\"42–99%\"或明确限定条件（如\"76–99% on SciERC\"），并在 abstract 中说明 Mistral 排除的理由。\n\n**W2. [critical] CF ≤ 1.3% 声明被 70B 结果违反**\n- Abstract: \"residual CF (≤1.3%)\"\n- §5.4 (70B evaluation): \"CF drops from 3.50% (zero-shot) to 0.18–**1.33%** (LoRA)\"\n- 1.33% > 1.3%。虽然差异微小，但 abstract 将其作为 bound 呈现，且 70B 是论文明确涵盖的配置（abstract 说\"five autoregressive LMs (7–70B)\"）。\n- **建议**：将 bound 修正为 \"≤1.4%\" 或明确限定为 8B 模型。\n\n**W3. [critical] 新颖性定位问题——核心贡献的组件均为已知技术**\n- Grammar layer 是 XGrammar 的直接应用（论文自述\"via XGrammar\"）\n- Semantic layer 是运行时类型检查的 mask 实现——概念上直截了当\n- Proposition 1 formalizes \"cross-field type constraints require runtime state beyond CFG\"——论文自称\"we formalize a well-known intuition\"，但将其列为 Contribution #1\n- 真正的新颖性在于：(a) 自动编译 IE ontology 为 token-level 约束的端到端管道，(b) 两层组合的系统评估\n- 目前的贡献表述将\"engineering integration\"包装为\"novel architecture\"，可能引起 reviewer 质疑\n- **建议**：将贡献重心从\"two-layer architecture is novel\"转向\"first systematic study of automatically compiling IE ontologies into composable decoding constraints\"，强调系统工程和实证发现而非架构创新。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. [warning] κ̄ (constraint tightness) 作为\"predictive factor\"但 n=3**\n- Abstract: \"establishing constraint tightness (κ̄) as a predictive factor\"\n- 实际仅在 3 个 schema 上验证（SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄≈0.82）\n- n=3 无法\"establish\"任何统计意义上的预测能力。Appendix 中的 dual-factor analysis（Figure 2）用 4 个数据点拟合线性模型（R²=0.886），但 p=0.058 不显著（文中诚实承认），且 4 个点中 Mistral 7B DocRED 偏离线性趋势\n- 目前的证据仅支持\"descriptive observation\"而非\"predictive factor\"\n- **建议**：将 abstract 中的\"establishing...as a predictive factor\"改为\"introducing...as a descriptive metric\"（与 Limitations section 的措辞一致），或增加更多 schema 的验证。\n\n**W5. [warning] WikiEvents fine-tuning composability 基于 n=20 极不充分**\n- §5.4: \"On the full official test split (20 documents; 194/20/20)\"\n- 论文承认\"per-document variance is high (Arg-F1 std/mean > 0.5)\"和\"confirming sufficient power to detect violation elimination but not small F1 differences\"\n- 但 Table 5 和正文仍报告 CF=0.77–1.18%、AC≤0.8% 等具体数字，读者可能高估这些估计的可靠性\n- Abstract 将 WikiEvents 与 SciERC/DocRED 并列作为验证（\"validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents\"），但 fine-tuning 的\"validation\"实际非常初步\n- **建议**：在 Table 5 caption 或 footnote 中加入 confidence interval，让读者评估 n=20 的统计效力。\n\n**W6. [warning] \"Deployment-grade compliance\" 叙事被 CF trade-off 削弱**\n- Abstract/Introduction 反复使用\"deployment-grade type compliance\"\n- 但 CF 是 DR enforcement 的系统性副产品：zero-shot 最高 12.02%（Llama DocRED），fine-tuned 最高 1.18%（8B）\n- Beam search 在 SciERC 上消除所有违规，但对 DocRED 的 beam search 仅在 50-document subset 上验证，且 CF 仍有 0.93%（Table 22, Llama DocRED）\n- 全数据集 beam search 结果（Table 22, 998 docs）Qwen DR=0% CF=0.93%, Llama DR=0% CF reductions from 74-86%——并非\"完全消除\"\n- \"Deployment-grade\"通常暗示接近零违规；当前系统在 CF 维度上做不到这一点\n- **建议**：将 framing 从\"deployment-grade compliance\"软化为\"near-complete DR elimination with residual CF trade-off\"，或明确定义\"deployment-grade\"的具体含义。\n\n**W7. [warning] \"Enabling dependency\" 声明范围不清**\n- Introduction Contribution 2: \"neither layer alone exceeds 24% DR reduction\"\n- 这仅在 SciERC 上成立（grammar-only 3%, semantic-only 24%）\n- DocRED: semantic-only 实际达到 25%（超过 24%）；更严重的是，grammar-only 在 DocRED 上**增加** DR 42%（18.46% → 26.17%）\n- 虽然引用了\"(§5.1)\"暗示限于 SciERC，但读者自然会理解为通用结论\n- **建议**：改为\"on SciERC, neither layer alone exceeds 24%\"，并讨论 DocRED 上 grammar-only 增加 DR 的原因及其对 enabling dependency 叙事的影响。\n\n### Minor（不影响接收）\n\n**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B（~4 页）。主文读者无法仅从 §6 评估相关工作覆盖的充分性。建议将 Appendix B 中最关键的对比（尤其是 vs. GCD, GoLLIE, EnriCo 的定性差异）移入主文。\n\n**M2.** \"S1\" 和 \"Full S1\" 在正文中交替使用（如 §5.1 \"Full S1\" vs. §5.4 \"S1\"），应统一术语。\n\n**M3.** Figure 1 信息密度过高，同时展示 grammar 和 semantic 两层的内部机制。考虑分为两个子图或简化。\n\n**M4.** Table 4 的 Mistral SciERC unconstrained CF=56.87% 通过 dagger (†) 脚注解释，但读者第一次看到时仍会困惑——建议在表格上方或 caption 中更早引入\"poor calibration\"的背景。\n\n**M5.** Introduction 中\"Post-hoc filtering improves precision but discards up to 48% of predictions including true positives\"——\"48%\"仅在 Appendix 中有详细支撑（SciERC Qwen zero-shot），主文首次出现时未 cite 来源表格。\n\n---\n\n## 4. Questions（需要作者澄清）\n\n**Q1.** Abstract/Intro 的 DR 降幅范围不一致（45–99% vs. 76–99%），具体是指哪些配置？DocRED Qwen 的 45% 为什么不影响 intro 的\"76–99% for calibrated models\"声明？\n\n**Q2.** Beam search 在 DocRED 全数据集上的 CF 表现如何？Table 22 显示 Qwen CF=0.93%（beam k=4, 998 docs）——这与\"eliminates all four violation types\"的叙述如何调和？\n\n**Q3.** 70B LoRA CF=1.33% 超过 abstract 的\"≤1.3%\"bound。是否考虑更新此 bound？\n\n**Q4.** Proposition 1 的证明（Appendix O）使用 position-based formulation，但实际系统使用 name-based entity referencing。Appendix 最后一段讨论了这个简化，但核心证明是否因此与实际系统存在 gap？\n\n**Q5.** Grammar-only 在 DocRED 上增加 DR（+42%）。这是否意味着在某些 ontology 配置下，grammar layer 可能损害而非帮助 DR？这对\"enabling dependency\"的通用性有什么影响？\n\n---\n\n## 5. Missing References\n\n论文的相关工作覆盖在 constrained decoding + IE 领域相当全面。以下可能值得提及但非必要：\n\n- **Schmidt & Cimiano (2025)**, \"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts\" (Bioinformatics)——biomedical IE 中 grammar-constrained decoding 的直接应用，与本文方法高度相关但独立发展。\n- **Microsoft Guidance** library——虽然是工程工具而非研究论文，但在 constrained generation 讨论中经常被提及，可在 Appendix B 中简要提及。\n- 论文未引用任何 **EMNLP 2025** 相关工作（proceedings 已发布），建议检查是否有遗漏的近期 accepted papers。\n\n**引用真实性**: 所有 46 个 bib 条目均来自已知的真实论文/预印本。arXiv preprints 的引用格式基本统一（使用 arXiv preprint arXiv:XXXX.XXXXX 格式）。未发现伪造引用。\n\n---\n\n## 6. Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference\n\n**Confidence**: 4/5 — 对 constrained decoding 和 IE 领域有较好了解，仔细阅读了全文（含 34 页附录）并验证了关键数字声明。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计全面，方法论合理，但 abstract/intro 数字不一致（W1, W2）削弱可信度；CF trade-off 削弱核心声明（W6） |\n| Excitement | 2.5/5 | 实用价值明确但概念新颖性有限——grammar layer 为 XGrammar 应用，semantic layer 为直观的类型检查实现，Proposition 1 形式化已知直觉。主要贡献是系统集成和全面评估 |\n| Reproducibility | 4/5 | exp_id 标注、bootstrap CI、seed 报告、Appendix G 的完整再现细节，\"code and data will be released upon acceptance\"。唯一扣分项是 70B 结果使用 AWQ INT4 量化（可能引入不确定性） |\n| Overall Assessment | 3.5/5 | Borderline Conference |\n\n### 一句话总评\n\n一项系统化但新颖性有限的工程贡献：将已知组件（CFG enforcement + runtime type checking）组合为 IE ontology 约束解码管道，配以出色的评估覆盖度，但 abstract/intro 的数字不一致和 CF trade-off 削弱了核心叙事。\n\n---\n\n## 7. Detailed Comments（逐节）\n\n### Abstract\n- \"45–99% DR reduction\"与 intro 的\"76–99%\"不一致（W1）\n- \"CF ≤ 1.3%\"被 70B 的 1.33% 违反（W2）\n- \"establishing constraint tightness (κ̄) as a predictive factor\"过度声称（W4）\n- 整体写作质量高，信息密度适当\n\n### §1 Introduction\n- Contribution 1 将 Proposition 1 定位为\"formalize a well-known intuition\"是准确的，但同时将其作为 headlined contribution 可能引起期望错位\n- Contribution 2 中\"neither layer alone exceeds 24%\"仅限 SciERC（W7）\n- \"deployment-grade type compliance\"措辞需要审视（W6）\n- 写作清晰，问题动机充分\n\n### §2 Background\n- IE ontology 的形式化定义清楚\n- 约束可判定性的三级分类（context-free / prefix-decidable / non-local）是有用的概念框架\n- Proposition 1 定位为\"necessary condition\"恰当\n\n### §3 Method\n- Grammar layer 和 semantic layer 的实现描述清晰\n- \"Continuation masking\"机制的解释充分\n- \"Grammar-first fallback\"的设计决策合理，且有 causal tracing 验证（Appendix Table 7）\n\n### §4 Constraint Composition\n- Mask composition 公式简洁\n- asymmetric conjunction（S(t) defined only over G(t)）的解释清楚\n\n### §5 Experiments\n- Table 1 的五路消融是最强的实验贡献之一\n- DocRED 的 grammar-only DR 增加现象值得在主文中更详细讨论（W7）\n- WikiEvents 结果的统计效力受限于 n=20（W5）\n- 70B 结果定位为 \"feasibility check\" 基本恰当，但仍被纳入 abstract 的统计声明中\n\n### §6 Related Work\n- 覆盖面合理但主文过于压缩（M1）\n- GCD, GoLLIE, EnriCo 的对比定位准确\n\n### §7 Conclusion\n- 数字与前文一致（继承了 W1 中的 \"76–99%\" 问题）\n\n### Limitations\n- 全面且诚实（S3）\n- 三段分别覆盖约束范围、评估覆盖、工程考量\n- 将 CF trade-off 定性为\"fundamental trade-off in composable constraint systems\"是合理的\n\n### Ethics Statement & Checklist\n- Ethics statement 简洁但充分\n- Checklist 填写认真（page 10），各项回答与论文内容一致\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（符合 EMNLP 2026 要求），PDF 中的 checklist 作为补充\n\n### 格式\n- 正文 8 页 ✓\n- `\\usepackage[review]{acl}` ✓（匿名，行号）\n- 作者行 \"Anonymous ACL submission\" ✓\n- 未发现 self-citation leaks 或 identifying information\n- Limitations/Ethics 在 \\clearpage 后，不计入页数 ✓\n- 参考文献格式基本统一，arXiv preprints 使用一致格式\n\n---\n\n**总结**: 论文在实际问题上提供了系统化的工程解决方案，评估全面且 limitations 诚实。主要顾虑是概念新颖性有限（已知组件的集成）和 abstract/intro 中数字声明的精确性问题。修正数字不一致并调整贡献定位后，可达到 Conference/Findings 接收水平。",
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
    "text": "## Reviewer 2 审稿意见 — Round 1 (Fresh Review)\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 1. Summary\n\n本文提出 OntoCoDec，一个将 IE ontology 自动编译为 token-level 解码约束的框架。核心设计是两层架构：grammar layer（基于 XGrammar 的 CFG）保证 JSON 结构和词表合规，semantic layer（基于运行时实体注册表的有状态 logit masking）执行 domain/range 类型约束。论文通过 Proposition 1（pumping lemma 证明）论证跨字段类型约束超出 CFG 表达能力，并在 3 个数据集、5 个模型、2 个 IE 任务上进行了系统评估。LoRA + 约束解码在 R-F1 43–46% 下将 DR 降至 ≤0.09%，但引入 CF 违规（≤1.3%）作为 violation conversion 的代价。\n\n---\n\n## 2. Strengths\n\n**S1. 问题驱动的系统化框架设计**\n将 IE ontology 约束自动编译为解码时约束是一个实际且有价值的工程贡献。与需要约束特定训练的方法（GoLLIE, KnowCoder）相比，OntoCoDec 的\"零训练开销\"和自动编译特性有明确的实用优势。ontology → grammar → mask 的编译管道有清晰的工程逻辑。\n\n**S2. 评估的系统性和全面性**\n3 个数据集（SciERC, DocRED, WikiEvents）、5 个模型（7B–70B）、3 个 tokenizer family、zero-shot + LoRA fine-tuning、greedy + beam search、五路消融，加上 bootstrap 显著性检验和 Bonferroni 校正——评估覆盖度在同类工作中属于上乘。Table 1 的五路消融清楚地隔离了各层贡献。\n\n**S3. 诚实透明的 Limitations**\nLimitations section 覆盖了 CF trade-off、评估范围（模型规模、fine-tuning 方法、语言限制）、工程约束（API-only 模型不适用、tokenizer 依赖性）等关键限制，比多数投稿更加坦诚。CF↔DR trade-off 的分析（Appendix C, causal tracing）提供了对失败模式的真实理解。\n\n**S4. 低运行时开销**\ngreedy S1 仅增加 10–13% 延迟，编译为 one-time < 0.5s，scalability benchmark 到 200 entity types / 1000 relations 仍保持 2–3% overhead。这对实际部署有直接价值。\n\n**S5. Decidability analysis 提供理论基础**\nProposition 1 及其 pumping lemma 证明（Appendix O）为两层架构的必要性提供了形式化依据，而非仅凭直觉。Appendix 中的 finite entity set 分析补充了理论与实践之间的联系。\n\n---\n\n## 3. Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [critical] Abstract 与 Introduction 的 DR 降幅数字不一致**\n- Abstract: \"45–99% DR reduction\"（§Abstract）\n- Introduction: \"DR drops 76–99% for calibrated models\"（§1, Contribution 2）\n- Table 4 的实际数据覆盖 6 个 model-dataset 组合（8B zero-shot）：\n  - SciERC: Qwen 94%, Llama 99%, Mistral 76%\n  - DocRED: Qwen 45%, Llama 90%, Mistral 42%\n- 全范围为 **42–99%**，而非 45–99%（Mistral DocRED 为 42%，被排除且未说明）\n- Introduction 声称\"76–99% for calibrated models\"，但 DocRED Qwen（calibrated model）仅 45%，远低于 76%。除非 Qwen 在 DocRED 上不被视为\"calibrated\"，否则此声明与数据矛盾。\n- **建议**：统一为准确范围\"42–99%\"或明确限定条件（如\"76–99% on SciERC\"），并在 abstract 中说明 Mistral 排除的理由。\n\n**W2. [critical] CF ≤ 1.3% 声明被 70B 结果违反**\n- Abstract: \"residual CF (≤1.3%)\"\n- §5.4 (70B evaluation): \"CF drops from 3.50% (zero-shot) to 0.18–**1.33%** (LoRA)\"\n- 1.33% > 1.3%。虽然差异微小，但 abstract 将其作为 bound 呈现，且 70B 是论文明确涵盖的配置（abstract 说\"five autoregressive LMs (7–70B)\"）。\n- **建议**：将 bound 修正为 \"≤1.4%\" 或明确限定为 8B 模型。\n\n**W3. [critical] 新颖性定位问题——核心贡献的组件均为已知技术**\n- Grammar layer 是 XGrammar 的直接应用（论文自述\"via XGrammar\"）\n- Semantic layer 是运行时类型检查的 mask 实现——概念上直截了当\n- Proposition 1 formalizes \"cross-field type constraints require runtime state beyond CFG\"——论文自称\"we formalize a well-known intuition\"，但将其列为 Contribution #1\n- 真正的新颖性在于：(a) 自动编译 IE ontology 为 token-level 约束的端到端管道，(b) 两层组合的系统评估\n- 目前的贡献表述将\"engineering integration\"包装为\"novel architecture\"，可能引起 reviewer 质疑\n- **建议**：将贡献重心从\"two-layer architecture is novel\"转向\"first systematic study of automatically compiling IE ontologies into composable decoding constraints\"，强调系统工程和实证发现而非架构创新。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. [warning] κ̄ (constraint tightness) 作为\"predictive factor\"但 n=3**\n- Abstract: \"establishing constraint tightness (κ̄) as a predictive factor\"\n- 实际仅在 3 个 schema 上验证（SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄≈0.82）\n- n=3 无法\"establish\"任何统计意义上的预测能力。Appendix 中的 dual-factor analysis（Figure 2）用 4 个数据点拟合线性模型（R²=0.886），但 p=0.058 不显著（文中诚实承认），且 4 个点中 Mistral 7B DocRED 偏离线性趋势\n- 目前的证据仅支持\"descriptive observation\"而非\"predictive factor\"\n- **建议**：将 abstract 中的\"establishing...as a predictive factor\"改为\"introducing...as a descriptive metric\"（与 Limitations section 的措辞一致），或增加更多 schema 的验证。\n\n**W5. [warning] WikiEvents fine-tuning composability 基于 n=20 极不充分**\n- §5.4: \"On the full official test split (20 documents; 194/20/20)\"\n- 论文承认\"per-document variance is high (Arg-F1 std/mean > 0.5)\"和\"confirming sufficient power to detect violation elimination but not small F1 differences\"\n- 但 Table 5 和正文仍报告 CF=0.77–1.18%、AC≤0.8% 等具体数字，读者可能高估这些估计的可靠性\n- Abstract 将 WikiEvents 与 SciERC/DocRED 并列作为验证（\"validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents\"），但 fine-tuning 的\"validation\"实际非常初步\n- **建议**：在 Table 5 caption 或 footnote 中加入 confidence interval，让读者评估 n=20 的统计效力。\n\n**W6. [warning] \"Deployment-grade compliance\" 叙事被 CF trade-off 削弱**\n- Abstract/Introduction 反复使用\"deployment-grade type compliance\"\n- 但 CF 是 DR enforcement 的系统性副产品：zero-shot 最高 12.02%（Llama DocRED），fine-tuned 最高 1.18%（8B）\n- Beam search 在 SciERC 上消除所有违规，但对 DocRED 的 beam search 仅在 50-document subset 上验证，且 CF 仍有 0.93%（Table 22, Llama DocRED）\n- 全数据集 beam search 结果（Table 22, 998 docs）Qwen DR=0% CF=0.93%, Llama DR=0% CF reductions from 74-86%——并非\"完全消除\"\n- \"Deployment-grade\"通常暗示接近零违规；当前系统在 CF 维度上做不到这一点\n- **建议**：将 framing 从\"deployment-grade compliance\"软化为\"near-complete DR elimination with residual CF trade-off\"，或明确定义\"deployment-grade\"的具体含义。\n\n**W7. [warning] \"Enabling dependency\" 声明范围不清**\n- Introduction Contribution 2: \"neither layer alone exceeds 24% DR reduction\"\n- 这仅在 SciERC 上成立（grammar-only 3%, semantic-only 24%）\n- DocRED: semantic-only 实际达到 25%（超过 24%）；更严重的是，grammar-only 在 DocRED 上**增加** DR 42%（18.46% → 26.17%）\n- 虽然引用了\"(§5.1)\"暗示限于 SciERC，但读者自然会理解为通用结论\n- **建议**：改为\"on SciERC, neither layer alone exceeds 24%\"，并讨论 DocRED 上 grammar-only 增加 DR 的原因及其对 enabling dependency 叙事的影响。\n\n### Minor（不影响接收）\n\n**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B（~4 页）。主文读者无法仅从 §6 评估相关工作覆盖的充分性。建议将 Appendix B 中最关键的对比（尤其是 vs. GCD, GoLLIE, EnriCo 的定性差异）移入主文。\n\n**M2.** \"S1\" 和 \"Full S1\" 在正文中交替使用（如 §5.1 \"Full S1\" vs. §5.4 \"S1\"），应统一术语。\n\n**M3.** Figure 1 信息密度过高，同时展示 grammar 和 semantic 两层的内部机制。考虑分为两个子图或简化。\n\n**M4.** Table 4 的 Mistral SciERC unconstrained CF=56.87% 通过 dagger (†) 脚注解释，但读者第一次看到时仍会困惑——建议在表格上方或 caption 中更早引入\"poor calibration\"的背景。\n\n**M5.** Introduction 中\"Post-hoc filtering improves precision but discards up to 48% of predictions including true positives\"——\"48%\"仅在 Appendix 中有详细支撑（SciERC Qwen zero-shot），主文首次出现时未 cite 来源表格。\n\n---\n\n## 4. Questions（需要作者澄清）\n\n**Q1.** Abstract/Intro 的 DR 降幅范围不一致（45–99% vs. 76–99%），具体是指哪些配置？DocRED Qwen 的 45% 为什么不影响 intro 的\"76–99% for calibrated models\"声明？\n\n**Q2.** Beam search 在 DocRED 全数据集上的 CF 表现如何？Table 22 显示 Qwen CF=0.93%（beam k=4, 998 docs）——这与\"eliminates all four violation types\"的叙述如何调和？\n\n**Q3.** 70B LoRA CF=1.33% 超过 abstract 的\"≤1.3%\"bound。是否考虑更新此 bound？\n\n**Q4.** Proposition 1 的证明（Appendix O）使用 position-based formulation，但实际系统使用 name-based entity referencing。Appendix 最后一段讨论了这个简化，但核心证明是否因此与实际系统存在 gap？\n\n**Q5.** Grammar-only 在 DocRED 上增加 DR（+42%）。这是否意味着在某些 ontology 配置下，grammar layer 可能损害而非帮助 DR？这对\"enabling dependency\"的通用性有什么影响？\n\n---\n\n## 5. Missing References\n\n论文的相关工作覆盖在 constrained decoding + IE 领域相当全面。以下可能值得提及但非必要：\n\n- **Schmidt & Cimiano (2025)**, \"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts\" (Bioinformatics)——biomedical IE 中 grammar-constrained decoding 的直接应用，与本文方法高度相关但独立发展。\n- **Microsoft Guidance** library——虽然是工程工具而非研究论文，但在 constrained generation 讨论中经常被提及，可在 Appendix B 中简要提及。\n- 论文未引用任何 **EMNLP 2025** 相关工作（proceedings 已发布），建议检查是否有遗漏的近期 accepted papers。\n\n**引用真实性**: 所有 46 个 bib 条目均来自已知的真实论文/预印本。arXiv preprints 的引用格式基本统一（使用 arXiv preprint arXiv:XXXX.XXXXX 格式）。未发现伪造引用。\n\n---\n\n## 6. Overall Assessment\n\n**Overall**: 3.5 — Borderline Conference\n\n**Confidence**: 4/5 — 对 constrained decoding 和 IE 领域有较好了解，仔细阅读了全文（含 34 页附录）并验证了关键数字声明。\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验设计全面，方法论合理，但 abstract/intro 数字不一致（W1, W2）削弱可信度；CF trade-off 削弱核心声明（W6） |\n| Excitement | 2.5/5 | 实用价值明确但概念新颖性有限——grammar layer 为 XGrammar 应用，semantic layer 为直观的类型检查实现，Proposition 1 形式化已知直觉。主要贡献是系统集成和全面评估 |\n| Reproducibility | 4/5 | exp_id 标注、bootstrap CI、seed 报告、Appendix G 的完整再现细节，\"code and data will be released upon acceptance\"。唯一扣分项是 70B 结果使用 AWQ INT4 量化（可能引入不确定性） |\n| Overall Assessment | 3.5/5 | Borderline Conference |\n\n### 一句话总评\n\n一项系统化但新颖性有限的工程贡献：将已知组件（CFG enforcement + runtime type checking）组合为 IE ontology 约束解码管道，配以出色的评估覆盖度，但 abstract/intro 的数字不一致和 CF trade-off 削弱了核心叙事。\n\n---\n\n## 7. Detailed Comments（逐节）\n\n### Abstract\n- \"45–99% DR reduction\"与 intro 的\"76–99%\"不一致（W1）\n- \"CF ≤ 1.3%\"被 70B 的 1.33% 违反（W2）\n- \"establishing constraint tightness (κ̄) as a predictive factor\"过度声称（W4）\n- 整体写作质量高，信息密度适当\n\n### §1 Introduction\n- Contribution 1 将 Proposition 1 定位为\"formalize a well-known intuition\"是准确的，但同时将其作为 headlined contribution 可能引起期望错位\n- Contribution 2 中\"neither layer alone exceeds 24%\"仅限 SciERC（W7）\n- \"deployment-grade type compliance\"措辞需要审视（W6）\n- 写作清晰，问题动机充分\n\n### §2 Background\n- IE ontology 的形式化定义清楚\n- 约束可判定性的三级分类（context-free / prefix-decidable / non-local）是有用的概念框架\n- Proposition 1 定位为\"necessary condition\"恰当\n\n### §3 Method\n- Grammar layer 和 semantic layer 的实现描述清晰\n- \"Continuation masking\"机制的解释充分\n- \"Grammar-first fallback\"的设计决策合理，且有 causal tracing 验证（Appendix Table 7）\n\n### §4 Constraint Composition\n- Mask composition 公式简洁\n- asymmetric conjunction（S(t) defined only over G(t)）的解释清楚\n\n### §5 Experiments\n- Table 1 的五路消融是最强的实验贡献之一\n- DocRED 的 grammar-only DR 增加现象值得在主文中更详细讨论（W7）\n- WikiEvents 结果的统计效力受限于 n=20（W5）\n- 70B 结果定位为 \"feasibility check\" 基本恰当，但仍被纳入 abstract 的统计声明中\n\n### §6 Related Work\n- 覆盖面合理但主文过于压缩（M1）\n- GCD, GoLLIE, EnriCo 的对比定位准确\n\n### §7 Conclusion\n- 数字与前文一致（继承了 W1 中的 \"76–99%\" 问题）\n\n### Limitations\n- 全面且诚实（S3）\n- 三段分别覆盖约束范围、评估覆盖、工程考量\n- 将 CF trade-off 定性为\"fundamental trade-off in composable constraint systems\"是合理的\n\n### Ethics Statement & Checklist\n- Ethics statement 简洁但充分\n- Checklist 填写认真（page 10），各项回答与论文内容一致\n- Responsible NLP Checklist 在 OpenReview submission form 中填写（符合 EMNLP 2026 要求），PDF 中的 checklist 作为补充\n\n### 格式\n- 正文 8 页 ✓\n- `\\usepackage[review]{acl}` ✓（匿名，行号）\n- 作者行 \"Anonymous ACL submission\" ✓\n- 未发现 self-citation leaks 或 identifying information\n- Limitations/Ethics 在 \\clearpage 后，不计入页数 ✓\n- 参考文献格式基本统一，arXiv preprints 使用一致格式\n\n---\n\n**总结**: 论文在实际问题上提供了系统化的工程解决方案，评估全面且 limitations 诚实。主要顾虑是概念新颖性有限（已知组件的集成）和 abstract/intro 中数字声明的精确性问题。修正数字不一致并调整贡献定位后，可达到 Conference/Findings 接收水平。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1473 · 2026-05-22T10:53:41.150819+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1474 · 2026-05-22T10:53:54.757393+00:00_

审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall**: 3.5 (Borderline Conference)
- **核心判断**：系统化但新颖性有限的工程贡献，评估全面但 abstract/intro 存在数字不一致
- **3 个 Must-Fix**：(1) DR 降幅范围 45–99% vs 76–99% 自相矛盾，实际为 42–99%；(2) CF≤1.3% 被 70B 的 1.33% 违反；(3) 新颖性定位——核心组件均为已知技术，应重新定位为工程贡献
- **4 个 Should-Fix**：κ̄ 在 n=3 上声称"predictive"、WikiEvents n=20 统计效力不足、"deployment-grade"措辞被 CF trade-off 削弱、"enabling dependency"范围不清
- **Excitement**: 2.5/5——实用但概念创新有限

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 31

## Round 31

4 recorded events


### User

_source line 1475 · 2026-05-22T10:54:54.803540+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Round 1

以下是 **Reviewer 1** 的完整审稿意见（侧重：方法严谨性 + 实验设计）。请逐条回应其 Weaknesses 和 Questions，使用以下格式：

- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注：你们是否在以下问题上有分歧？
- 缺少 baseline 实验对比的严重程度
- CF violation 主文呈现问题
- κ̄ 统计功效
- WikiEvents 评估

---

## Reviewer 1 完整审稿意见

### Strengths
S1. 理论基础扎实——Decidability taxonomy + Proposition 1 pumping lemma 证明。
S2. 消融实验设计系统完整——五路/四路消融逐层隔离。
S3. CF-DR trade-off 诚实分析——causal tracing, CF-priority fallback 消融, dual-factor 分析。
S4. 跨模型/跨数据集/跨设置覆盖广——4 模型族 × 3 数据集 × ZS/FT + beam/prompt/length 维度。
S5. 可复现性优秀——Appendix G 硬件/种子/超参/3 seeds variance。
S6. 工程贡献实用——10% latency overhead 可部署。

### Weaknesses

**W1 [critical]** 缺少与现有 constrained decoding 方法的直接实验对比——大量讨论 GCD/BoostCD/CRANE/GoLLIE 但无 head-to-head 实验。唯一"对比"是自行实现的 Trie-Only Baseline（Table 15）。§5.4 声称 BoostCD "only 3% DR reduction"来自方法论推断而非实验。

**W2 [critical]** CF violation 增加在主文中被低估呈现——Llama DocRED CF 12.02% 完全未在主文出现，主文仅报 "CF ≤ 1.3%"。Abstract "substantially reduces type violations"在 DR↓+CF↑时高估 total violation burden 改善。

**W3 [warning]** κ̄ 统计功效不足——n=2-3 schema，Figure 2 仅 4 点，p>0.05。

**W4 [warning]** Entity registry 顺序依赖问题未量化——首次类型分配错误会传播，Limitations 承认但无量化。

**W5 [warning]** WikiEvents fine-tuned 仅 20 文档，bootstrap CI 极宽。

**W6 [warning]** S2（two-pass pipeline）花半页描述但实验中一句带过，无完整结果。

**W7 [minor]** Proposition 1 证明中 position-based vs name-based 桥接缺乏形式化。
**W8 [minor]** 70B AWQ INT4 量化对约束 enforcement 的影响未讨论。
**W9 [minor]** "five models" 但实际 4 个模型族。

### Questions
Q1. Multi-type entity 如何处理？
Q2. Triple-level fallback 触发比例？
Q3. Llama DocRED 12.02% CF 根因？
Q4. Constrained decoding + post-hoc filtering 组合？
Q5. BoostCD "3% DR reduction" 来自分析还是实验？

### Overall Assessment
3.5 — Borderline Conference, Confidence 4/5
Soundness 3.5, Excitement 3, Reproducibility 4.5

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

_source line 1476 · 2026-05-22T10:57:59.917040+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — Reviewer 1 Weaknesses & Questions\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: 缺少直接 baseline 实验对比**\n\n同意这是一个值得指出的弱点，但我对严重程度的判断与 R1 略有不同。\n\n同意的部分：论文讨论了 GCD/BoostCD/GoLLIE 等多个方法但无 head-to-head 实验，确实削弱了实验的说服力。Trie-Only Baseline（Table 15, Appendix）是自行实现而非官方代码复现。\"BoostCD 仅 3% DR reduction\"实际来自论文自己的 grammar-only ablation（Table 1, row 2: DR 15.37% → 14.84%），而非运行 BoostCD 代码——这一推断虽然在方法论上合理（两者约束范围相同：vocabulary membership），但应明确标注为\"methodological equivalence\"而非实验结论。\n\n不同意的部分：我认为此问题的严重程度应区分对待：\n1. **GCD → grammar-only ablation 作为代理是合理的**：GCD 的核心约束是 vocabulary membership via trie，这正是论文 grammar layer 单独运行时做的事（Table 1 row 2）。除非 GCD 的实现有额外优化（如 search strategy），grammar-only 行是一个公平的上界估计。\n2. **GoLLIE 的缺失更严重**：GoLLIE 通过 annotation guidelines 作为 prompt 实现类型合规，是一个 training-based 但目标相近的 baseline。论文仅在 §6 定性讨论（\"GoLLIE-7B eliminates DR but at severe coverage cost (R-F1=0.0, 46% empty output)\"），但这个数字来源不清——是论文自己运行的结果还是 GoLLIE 论文中的数字？若是后者，在不同评估设置下的对比不公平。\n3. **CRANE/EnriCo 作为 post-hoc 方法，与 decoding-time 方法不在同一类别**，缺少对比可以理解。\n\n**建议**：至少运行 GCD 官方代码（或详细论证 grammar-only = GCD），并澄清 GoLLIE R-F1=0.0 的数据来源。\n\n---\n\n**[AGREE] R1-W2: CF violation 增加在主文中被低估呈现**\n\n完全同意。这与我的 W6（\"deployment-grade compliance\"叙事被 CF trade-off 削弱）高度一致。\n\n具体补充：\n- Table 4（主文 page 7）**确实**展示了 Llama DocRED CF=12.02%，但正文叙述（§5.3）仅说\"S1 introduces CF for calibrated models (up to 12.02%)\"——这一句中\"up to\"弱化了严重性\n- 更关键的是 Abstract 的叙事逻辑：先说\"DR ≤ 0.09%\"，再说\"residual CF (≤1.3%) represents violation conversion\"——1.3% 仅限 fine-tuned 设置，但 Abstract 未区分 zero-shot 和 fine-tuned CF。读者可能误解为所有配置下 CF ≤ 1.3%\n- Abstract 说\"substantially reduces type violations\"，但 zero-shot 的 Total violation（DR+CF）在 DocRED Llama 上是 26.07+0.17=26.24%（unconstrained）→ 2.55+12.02=14.57%（S1），改善约 44%——虽然 DR 大幅下降，但 CF 的涌入使 total 改善远不如 DR 单项的\"90%\"那么惊人\n\nR1 正确指出这是一个 framing 问题而非方法论错误——数据在 Table 4 中透明呈现，但叙事不匹配。\n\n---\n\n**[AGREE] R1-W3: κ̄ 统计功效不足**\n\n完全同意，与我的 W4 一致。\n\n补充一点 R1 未提及的问题：Figure 2（Appendix, page 21）的 dual-factor analysis 拟合 4 个数据点（3 models × 2 datasets 中去掉 outlier 后），p=0.058。但更根本的问题是：κ̄ 是在 schema 层面定义的（SciERC, DocRED, WikiEvents），而 Figure 2 的 x 轴是 κ × RV_baseline（model-dataset 交叉），这实际上是在用 model-dependent 的变量（RV_baseline）来补充 κ̄ 的不足，使得 κ̄ 本身的 predictive power 更加不明确。\n\n---\n\n**[AGREE] R1-W4: Entity registry 顺序依赖问题未量化**\n\n同意这是方法论弱点。补充：\n\n- CF 违规率本身就是这个问题的间接量化——CF 衡量的是\"同一实体被分配不同类型\"，这正是顺序依赖的表现\n- 但 R1 的要求更精确：量化\"首次类型分配错误的传播率\"。这需要一个 counterfactual 实验（如果首次分配正确，后续 triple 的 DR/CF 会如何变化），论文未做\n- Appendix C 的 causal tracing（Table 7）分析了 fallback 触发位置但不是 registry propagation 的量化\n- 这个问题在 fine-tuned 设置下影响较小（CF ≤ 1.3%），但在 zero-shot 下（CF 最高 12.02%）可能是主要错误来源\n\n---\n\n**[AGREE] R1-W5: WikiEvents fine-tuned 仅 20 文档**\n\n完全同意，与我的 W5 一致。我补充了一个具体建议：在 Table 5 caption 或 footnote 中加入 confidence interval。\n\n---\n\n**[AGREE] R1-W6: S2 花半页描述但实验中一句带过**\n\n同意。§3.4 用约半页描述 S2（two-pass pipeline），但实验中仅 Table 1 有一行 S2 结果（SciERC zero-shot），§5.1 用一句话带过（\"S2 achieves comparable DR (0.97%) but lower R-F1 and CF; we adopt S1\"）。\n\n这是典型的 space allocation 问题：\n- 方案 A：删除 S2 的方法描述，节省空间用于更完整的 S1 评估或 Related Work\n- 方案 B：保留 S2 并补充完整实验（至少 DocRED + fine-tuning）\n\n当前处于两者之间的尴尬状态——描述了但未验证。在 8 页限制下，方案 A 可能更务实。\n\n---\n\n**[AGREE] R1-W7: Proposition 1 position-based vs name-based 桥接**\n\n同意存在 gap，但认为严重程度低于 R1 可能暗示的水平。\n\nAppendix O 最后一段明确讨论了这个简化（\"The position-based formulation is a simplification that makes the pumping argument more transparent without weakening the conclusion\"），并指出在实际系统中 name-based referencing 的核心论点不变——类型一致性仍然依赖跨位置的绑定关系，这是 CFG 无法表达的。\n\n但\"without weakening the conclusion\"这一声明本身缺乏形式化证明。一个简短的 corollary 或 reduction 论证（name-based → position-based 的 reduction）会消除这个 gap。\n\n---\n\n**[AGREE] R1-W8: 70B AWQ INT4 量化影响未讨论**\n\n同意。INT4 量化改变 logit 分布，可能影响 mask 在 boundary cases 的行为。具体而言：\n- 量化后的 logit 精度降低可能使得原本被 mask 抑制的 token 在量化后的排名发生变化\n- 论文的 70B 结果（DR=0% on both datasets, zero-shot）反而显示约束在量化模型上可能更强（因为量化降低了模型对 ontology 的 \"记忆\"，增加了对约束的依赖），但这是推测而非验证\n- 简单的补救：加一句 disclaimer 即可\n\n---\n\n**[AGREE] R1-W9: \"five models\" 但实际 4 个**\n\n同意。我仔细检查了全文，只找到 4 个模型：\n1. Qwen3-8B\n2. Llama-3.1-8B\n3. Mistral-7B\n4. Llama-3.3-70B-Instruct\n\nAbstract 和 Introduction 都声称\"five autoregressive LMs\"，但 Limitations section 说\"three 8B-class and one 70B-class model\"=4。这是一个需要修正的事实错误。\n\n可能的解释：早期版本可能包含第 5 个模型（如 Qwen-72B 或 Gemma），在修改过程中被删除但 abstract 数字未更新。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1: Multi-type entity 处理**\n\n论文未明确讨论 multi-type entity（一个 entity 在 ontology 中合法地拥有多个类型，如 Person + Scientist）。当前的 entity registry 设计是 first-assignment-wins（§3.3: \"each completed entry [h_i, τ_i] adds (n_i, τ_i) to D\"），这意味着 multi-type entity 会被强制为单一类型。这对某些 ontology（如 DocRED 的 Wikidata types）可能导致 false positive CF violations。R1 提出此问题是合理的。\n\n---\n\n**[REBUT] R1-Q2: Triple-level fallback 触发比例**\n\n论文实际上提供了 fallback 量化数据，R1 可能遗漏：\n- Table 7（Appendix, page 19）: causal tracing 显示 SciERC 551 docs 上 18 个 residual DR violations 全部发生在 fallback positions（grammar-first fallback 触发时）\n- §5.1 提到\"token-level grammar-first fallback rate 0.46% at first-token positions\"（SciERC）\n- Appendix C（page 19-20）详细分解了 fallback 机制：token-level fallback rate 在 SciERC 为 0.46%，fallback 触发时的 type-bearing positions 中 50.8% 的 DR violations 来自 fallback\n\n数据存在，但分散在多个 Appendix 中，主文确实未给出 consolidated 的 fallback 比例。R1 的问题可能源于信息分散而非缺失。\n\n---\n\n**[AGREE] R1-Q3: Llama DocRED 12.02% CF 根因**\n\n论文在 Appendix C 有部分分析（CF-DR Trade-off 节）——CF 来自 per-entity sequential enforcement，当 DocRED 的高 κ̄ (0.842) 使得约束空间狭窄时，entity 的首次类型分配更容易与后续 triple 的 domain/range 要求冲突。但论文未单独分析\"为什么 Llama 比 Qwen 高很多\"（Qwen DocRED CF=2.57% vs Llama 12.02%）——这可能与 Llama 的 entity typing 能力较弱有关（Limitations 提到 \"weaker entity typing\"），导致首次分配错误率更高，进而通过 registry 传播。\n\n---\n\n**[AGREE] R1-Q4: Constrained decoding + post-hoc filtering 组合**\n\n同意这是一个值得探索的方向。论文将两者定位为替代方案（§5.3: \"Post-hoc filtering achieves DR=0% but with 15-74% rejection rates\"），但实际上它们是互补的：constrained decoding 消除大部分 DR，post-hoc filtering 清理残余 CF。Appendix 的 post-hoc 对比（Table 12）显示两者组合可行，但主文未讨论。\n\n---\n\n**[AGREE] R1-Q5: BoostCD \"3% DR reduction\" 来源**\n\n同意 R1 的质疑。§5.4 原文：\"Our grammar-only ablation (Table 1, row 2) implements the same constraints as GCD and BoostCD: RV/ET→0% but only 3% DR reduction vs. Full S1's 94%.\"\n\n这是将自己的 grammar-only ablation 结果归因于 GCD/BoostCD 的约束范围等价性推断，而非运行 BoostCD 代码。推断逻辑本身成立（BoostCD 的约束范围确实限于 vocabulary membership），但表述方式容易被误读为实验结果。应标注为 analytical equivalence。\n\n---\n\n### 综合评估：R2 与 R1 的分歧点\n\n| 议题 | R1 | R2 | 分歧程度 |\n|------|-----|-----|---------|\n| 缺少 baseline 的严重性 | Critical | Should-Fix | **中等分歧** — R2 认为 grammar-only 作为 GCD 代理是合理的，但同意 GoLLIE 缺失更严重 |\n| CF 主文呈现问题 | Critical | Should-Fix (我的 W6) | **轻微分歧** — 都认为是问题，R1 定为 critical，R2 定为 warning。CF 数据在 Table 4 中透明呈现，问题是叙事 framing 而非隐瞒 |\n| κ̄ 统计功效 | Warning | Warning (我的 W4) | **无分歧** — 都认为 n=3 不够 |\n| WikiEvents 评估 | Warning | Warning (我的 W5) | **无分歧** — 都认为 n=20 太弱 |\n| 新颖性 | 未重点讨论 (Excitement 3/5) | Critical (我的 W3) | **分歧** — R1 侧重方法严谨性不太关注新颖性，R2 认为核心组件均为已知技术的集成是主要弱点 |\n| 总分 | 3.5 Borderline Conference | 3.5 Borderline Conference | **无分歧** |\n\nR1 和 R2 在 overall 评分上一致（3.5 Borderline Conference），但关注点互补：R1 聚焦方法严谨性和实验设计缺陷，R2 聚焦新颖性和叙事一致性。两份 review 共同揭示的核心问题是：*论文的评估全面性是其最大优势，但 abstract/intro 的叙事精确性和概念新颖性是制约接收的主要因素。*",
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
    "text": "## Reviewer 2 交叉回应 — Reviewer 1 Weaknesses & Questions\n\n---\n\n### Weaknesses 回应\n\n**[AGREE] R1-W1: 缺少直接 baseline 实验对比**\n\n同意这是一个值得指出的弱点，但我对严重程度的判断与 R1 略有不同。\n\n同意的部分：论文讨论了 GCD/BoostCD/GoLLIE 等多个方法但无 head-to-head 实验，确实削弱了实验的说服力。Trie-Only Baseline（Table 15, Appendix）是自行实现而非官方代码复现。\"BoostCD 仅 3% DR reduction\"实际来自论文自己的 grammar-only ablation（Table 1, row 2: DR 15.37% → 14.84%），而非运行 BoostCD 代码——这一推断虽然在方法论上合理（两者约束范围相同：vocabulary membership），但应明确标注为\"methodological equivalence\"而非实验结论。\n\n不同意的部分：我认为此问题的严重程度应区分对待：\n1. **GCD → grammar-only ablation 作为代理是合理的**：GCD 的核心约束是 vocabulary membership via trie，这正是论文 grammar layer 单独运行时做的事（Table 1 row 2）。除非 GCD 的实现有额外优化（如 search strategy），grammar-only 行是一个公平的上界估计。\n2. **GoLLIE 的缺失更严重**：GoLLIE 通过 annotation guidelines 作为 prompt 实现类型合规，是一个 training-based 但目标相近的 baseline。论文仅在 §6 定性讨论（\"GoLLIE-7B eliminates DR but at severe coverage cost (R-F1=0.0, 46% empty output)\"），但这个数字来源不清——是论文自己运行的结果还是 GoLLIE 论文中的数字？若是后者，在不同评估设置下的对比不公平。\n3. **CRANE/EnriCo 作为 post-hoc 方法，与 decoding-time 方法不在同一类别**，缺少对比可以理解。\n\n**建议**：至少运行 GCD 官方代码（或详细论证 grammar-only = GCD），并澄清 GoLLIE R-F1=0.0 的数据来源。\n\n---\n\n**[AGREE] R1-W2: CF violation 增加在主文中被低估呈现**\n\n完全同意。这与我的 W6（\"deployment-grade compliance\"叙事被 CF trade-off 削弱）高度一致。\n\n具体补充：\n- Table 4（主文 page 7）**确实**展示了 Llama DocRED CF=12.02%，但正文叙述（§5.3）仅说\"S1 introduces CF for calibrated models (up to 12.02%)\"——这一句中\"up to\"弱化了严重性\n- 更关键的是 Abstract 的叙事逻辑：先说\"DR ≤ 0.09%\"，再说\"residual CF (≤1.3%) represents violation conversion\"——1.3% 仅限 fine-tuned 设置，但 Abstract 未区分 zero-shot 和 fine-tuned CF。读者可能误解为所有配置下 CF ≤ 1.3%\n- Abstract 说\"substantially reduces type violations\"，但 zero-shot 的 Total violation（DR+CF）在 DocRED Llama 上是 26.07+0.17=26.24%（unconstrained）→ 2.55+12.02=14.57%（S1），改善约 44%——虽然 DR 大幅下降，但 CF 的涌入使 total 改善远不如 DR 单项的\"90%\"那么惊人\n\nR1 正确指出这是一个 framing 问题而非方法论错误——数据在 Table 4 中透明呈现，但叙事不匹配。\n\n---\n\n**[AGREE] R1-W3: κ̄ 统计功效不足**\n\n完全同意，与我的 W4 一致。\n\n补充一点 R1 未提及的问题：Figure 2（Appendix, page 21）的 dual-factor analysis 拟合 4 个数据点（3 models × 2 datasets 中去掉 outlier 后），p=0.058。但更根本的问题是：κ̄ 是在 schema 层面定义的（SciERC, DocRED, WikiEvents），而 Figure 2 的 x 轴是 κ × RV_baseline（model-dataset 交叉），这实际上是在用 model-dependent 的变量（RV_baseline）来补充 κ̄ 的不足，使得 κ̄ 本身的 predictive power 更加不明确。\n\n---\n\n**[AGREE] R1-W4: Entity registry 顺序依赖问题未量化**\n\n同意这是方法论弱点。补充：\n\n- CF 违规率本身就是这个问题的间接量化——CF 衡量的是\"同一实体被分配不同类型\"，这正是顺序依赖的表现\n- 但 R1 的要求更精确：量化\"首次类型分配错误的传播率\"。这需要一个 counterfactual 实验（如果首次分配正确，后续 triple 的 DR/CF 会如何变化），论文未做\n- Appendix C 的 causal tracing（Table 7）分析了 fallback 触发位置但不是 registry propagation 的量化\n- 这个问题在 fine-tuned 设置下影响较小（CF ≤ 1.3%），但在 zero-shot 下（CF 最高 12.02%）可能是主要错误来源\n\n---\n\n**[AGREE] R1-W5: WikiEvents fine-tuned 仅 20 文档**\n\n完全同意，与我的 W5 一致。我补充了一个具体建议：在 Table 5 caption 或 footnote 中加入 confidence interval。\n\n---\n\n**[AGREE] R1-W6: S2 花半页描述但实验中一句带过**\n\n同意。§3.4 用约半页描述 S2（two-pass pipeline），但实验中仅 Table 1 有一行 S2 结果（SciERC zero-shot），§5.1 用一句话带过（\"S2 achieves comparable DR (0.97%) but lower R-F1 and CF; we adopt S1\"）。\n\n这是典型的 space allocation 问题：\n- 方案 A：删除 S2 的方法描述，节省空间用于更完整的 S1 评估或 Related Work\n- 方案 B：保留 S2 并补充完整实验（至少 DocRED + fine-tuning）\n\n当前处于两者之间的尴尬状态——描述了但未验证。在 8 页限制下，方案 A 可能更务实。\n\n---\n\n**[AGREE] R1-W7: Proposition 1 position-based vs name-based 桥接**\n\n同意存在 gap，但认为严重程度低于 R1 可能暗示的水平。\n\nAppendix O 最后一段明确讨论了这个简化（\"The position-based formulation is a simplification that makes the pumping argument more transparent without weakening the conclusion\"），并指出在实际系统中 name-based referencing 的核心论点不变——类型一致性仍然依赖跨位置的绑定关系，这是 CFG 无法表达的。\n\n但\"without weakening the conclusion\"这一声明本身缺乏形式化证明。一个简短的 corollary 或 reduction 论证（name-based → position-based 的 reduction）会消除这个 gap。\n\n---\n\n**[AGREE] R1-W8: 70B AWQ INT4 量化影响未讨论**\n\n同意。INT4 量化改变 logit 分布，可能影响 mask 在 boundary cases 的行为。具体而言：\n- 量化后的 logit 精度降低可能使得原本被 mask 抑制的 token 在量化后的排名发生变化\n- 论文的 70B 结果（DR=0% on both datasets, zero-shot）反而显示约束在量化模型上可能更强（因为量化降低了模型对 ontology 的 \"记忆\"，增加了对约束的依赖），但这是推测而非验证\n- 简单的补救：加一句 disclaimer 即可\n\n---\n\n**[AGREE] R1-W9: \"five models\" 但实际 4 个**\n\n同意。我仔细检查了全文，只找到 4 个模型：\n1. Qwen3-8B\n2. Llama-3.1-8B\n3. Mistral-7B\n4. Llama-3.3-70B-Instruct\n\nAbstract 和 Introduction 都声称\"five autoregressive LMs\"，但 Limitations section 说\"three 8B-class and one 70B-class model\"=4。这是一个需要修正的事实错误。\n\n可能的解释：早期版本可能包含第 5 个模型（如 Qwen-72B 或 Gemma），在修改过程中被删除但 abstract 数字未更新。\n\n---\n\n### Questions 回应\n\n**[AGREE] R1-Q1: Multi-type entity 处理**\n\n论文未明确讨论 multi-type entity（一个 entity 在 ontology 中合法地拥有多个类型，如 Person + Scientist）。当前的 entity registry 设计是 first-assignment-wins（§3.3: \"each completed entry [h_i, τ_i] adds (n_i, τ_i) to D\"），这意味着 multi-type entity 会被强制为单一类型。这对某些 ontology（如 DocRED 的 Wikidata types）可能导致 false positive CF violations。R1 提出此问题是合理的。\n\n---\n\n**[REBUT] R1-Q2: Triple-level fallback 触发比例**\n\n论文实际上提供了 fallback 量化数据，R1 可能遗漏：\n- Table 7（Appendix, page 19）: causal tracing 显示 SciERC 551 docs 上 18 个 residual DR violations 全部发生在 fallback positions（grammar-first fallback 触发时）\n- §5.1 提到\"token-level grammar-first fallback rate 0.46% at first-token positions\"（SciERC）\n- Appendix C（page 19-20）详细分解了 fallback 机制：token-level fallback rate 在 SciERC 为 0.46%，fallback 触发时的 type-bearing positions 中 50.8% 的 DR violations 来自 fallback\n\n数据存在，但分散在多个 Appendix 中，主文确实未给出 consolidated 的 fallback 比例。R1 的问题可能源于信息分散而非缺失。\n\n---\n\n**[AGREE] R1-Q3: Llama DocRED 12.02% CF 根因**\n\n论文在 Appendix C 有部分分析（CF-DR Trade-off 节）——CF 来自 per-entity sequential enforcement，当 DocRED 的高 κ̄ (0.842) 使得约束空间狭窄时，entity 的首次类型分配更容易与后续 triple 的 domain/range 要求冲突。但论文未单独分析\"为什么 Llama 比 Qwen 高很多\"（Qwen DocRED CF=2.57% vs Llama 12.02%）——这可能与 Llama 的 entity typing 能力较弱有关（Limitations 提到 \"weaker entity typing\"），导致首次分配错误率更高，进而通过 registry 传播。\n\n---\n\n**[AGREE] R1-Q4: Constrained decoding + post-hoc filtering 组合**\n\n同意这是一个值得探索的方向。论文将两者定位为替代方案（§5.3: \"Post-hoc filtering achieves DR=0% but with 15-74% rejection rates\"），但实际上它们是互补的：constrained decoding 消除大部分 DR，post-hoc filtering 清理残余 CF。Appendix 的 post-hoc 对比（Table 12）显示两者组合可行，但主文未讨论。\n\n---\n\n**[AGREE] R1-Q5: BoostCD \"3% DR reduction\" 来源**\n\n同意 R1 的质疑。§5.4 原文：\"Our grammar-only ablation (Table 1, row 2) implements the same constraints as GCD and BoostCD: RV/ET→0% but only 3% DR reduction vs. Full S1's 94%.\"\n\n这是将自己的 grammar-only ablation 结果归因于 GCD/BoostCD 的约束范围等价性推断，而非运行 BoostCD 代码。推断逻辑本身成立（BoostCD 的约束范围确实限于 vocabulary membership），但表述方式容易被误读为实验结果。应标注为 analytical equivalence。\n\n---\n\n### 综合评估：R2 与 R1 的分歧点\n\n| 议题 | R1 | R2 | 分歧程度 |\n|------|-----|-----|---------|\n| 缺少 baseline 的严重性 | Critical | Should-Fix | **中等分歧** — R2 认为 grammar-only 作为 GCD 代理是合理的，但同意 GoLLIE 缺失更严重 |\n| CF 主文呈现问题 | Critical | Should-Fix (我的 W6) | **轻微分歧** — 都认为是问题，R1 定为 critical，R2 定为 warning。CF 数据在 Table 4 中透明呈现，问题是叙事 framing 而非隐瞒 |\n| κ̄ 统计功效 | Warning | Warning (我的 W4) | **无分歧** — 都认为 n=3 不够 |\n| WikiEvents 评估 | Warning | Warning (我的 W5) | **无分歧** — 都认为 n=20 太弱 |\n| 新颖性 | 未重点讨论 (Excitement 3/5) | Critical (我的 W3) | **分歧** — R1 侧重方法严谨性不太关注新颖性，R2 认为核心组件均为已知技术的集成是主要弱点 |\n| 总分 | 3.5 Borderline Conference | 3.5 Borderline Conference | **无分歧** |\n\nR1 和 R2 在 overall 评分上一致（3.5 Borderline Conference），但关注点互补：R1 聚焦方法严谨性和实验设计缺陷，R2 聚焦新颖性和叙事一致性。两份 review 共同揭示的核心问题是：*论文的评估全面性是其最大优势，但 abstract/intro 的叙事精确性和概念新颖性是制约接收的主要因素。*",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-22T10:58:03.885843+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3968
}
```

</details>

---


### Assistant

_source line 1478 · 2026-05-22T10:58:13.622209+00:00_

交叉回应已提交给 Review Director。

核心结论：R1 和 R2 在总分（3.5 Borderline Conference）上一致，在 κ̄ 和 WikiEvents 问题上完全一致。主要分歧在于 baseline 缺失的严重程度（R1 定 critical，我认为 grammar-only 作为 GCD 代理部分缓解了这个问题）和 CF 呈现问题的定级（R1 critical vs. 我的 warning，因为数据实际在 Table 4 中透明展示，问题在于叙事 framing）。我额外指出了 R1 未重点讨论的新颖性问题（W3），这是我认为的最大制约因素。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 32

## Round 32

116 recorded events


### User

_source line 1479 · 2026-05-22T12:28:22.142139+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性 + 写作质量**

### 投稿信息
- **Venue**: EMNLP 2026（通过 ACL Rolling Review 提交）
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页（Long paper），参考文献不限，Limitations 和 Ethics 不计入页数
- **模板**: ACL style (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF**: `projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf`

### 论文概要
**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints**

将 IE ontology 编译为 token-level 约束的两层框架（grammar layer + semantic layer），在 SciERC、DocRED、WikiEvents 上验证，覆盖 4 个模型（7-70B）、3 个 tokenizer family。

### 你的审查重点

1. **新颖性评估**：
   - 核心贡献的新颖性——grammar layer 基于 XGrammar（已有技术），semantic layer 是 runtime type check（已知概念）。系统集成的新颖性是否足够支撑顶会发表？
   - 与 GoLLIE（training-time schema internalization）、GCD（grammar-constrained decoding）、EnriCo（ASP-based）、BoostCD 等方法的技术差异化是否清晰？
   - Proposition 1 的理论贡献——是否只是形式化了已知直觉？
   - κ̄（constraint tightness）作为 metric 的新颖性和实用性。

2. **完整性评估**：
   - Related Work 是否充分覆盖该领域？是否有遗漏的重要工作？
   - 实验覆盖是否全面——数据集选择、模型选择、decoding 策略？
   - 是否有必要的分析缺失（如 error analysis、failure mode 分析）？
   - Limitations 是否诚实、完整地覆盖了论文的局限性？
   - Appendix 材料是否合理组织、是否过度依赖 appendix 来支撑核心论点？

3. **写作质量**：
   - Abstract 和 Intro 中的 claim 是否与实验结果一致？是否存在 overclaiming？
   - 术语使用是否一致（如 'S1'/'Full S1' 是否统一）？
   - 数字引用是否准确——Abstract/Intro 中的百分比是否能在表格中找到对应？
   - 论文叙事是否连贯——从 motivation → method → experiments → conclusion 的逻辑链是否清晰？
   - Figure 和 Table 的质量、可读性、caption 的信息量。
   - 引用是否完整和准确（验证 bib 条目的真实性——抽查至少 10 个关键引用）。

4. **格式合规**：
   - 正文是否 ≤ 8 页？
   - Limitations 是否放在正确位置（conclusion 之后、references 之前），且不包含新实验/分析？
   - Ethics Statement 是否存在？
   - 匿名性检查——是否有 GitHub 链接、作者姓名、机构标识等泄露？
   - 模型名数量——论文声称的模型数量是否与实际使用的一致？

请提供完整的结构化审稿报告：Summary → Strengths (S1, S2, ...) → Weaknesses (W1, W2, ..., 按严重度排序) → Questions → Missing References → Overall Assessment（使用 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

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

_source line 1480 · 2026-05-22T12:28:33.942865+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
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
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-22T12:28:34.002941+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 60
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-22T12:28:37.402009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
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
    "query": "ACL ARR 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 1483 · 2026-05-22T12:28:38.205472+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1-10",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1484 · 2026-05-22T12:28:45.161544+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR 2026 reviewer guidelines and review form:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Review Score Scale

The review form uses the following scoring dimensions:

- 5 = Consider for Aw
…[truncated 979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7759
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-22T12:28:46.618837+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 528.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 403.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 570.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifac
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8413
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-22T12:28:52.050497+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review review form soundness excitement reproducibility scoring 1-5"
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
    "query": "ACL Rolling Review review form soundness excitement reproducibility scoring 1-5"
  }
}
```

</details>

---


### Tool call

_source line 1487 · 2026-05-22T12:28:52.559866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1488 · 2026-05-22T12:28:53.166014+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p2.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 1489 · 2026-05-22T12:28:54.422940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p3.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 1490 · 2026-05-22T12:28:54.624736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2064
}
```

</details>

---


### Tool call

_source line 1491 · 2026-05-22T12:28:54.625199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p4.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-22T12:28:55.383291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p5.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-22T12:28:56.041246+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2875
}
```

</details>

---


### Tool call

_source line 1494 · 2026-05-22T12:28:56.041692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p6.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 1495 · 2026-05-22T12:28:56.348185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p7.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 1496 · 2026-05-22T12:28:56.806353+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2383
}
```

</details>

---


### Tool call

_source line 1497 · 2026-05-22T12:28:56.857837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p8.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-22T12:28:58.118972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p9.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 1499 · 2026-05-22T12:28:58.119446+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p10.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 1500 · 2026-05-22T12:28:58.575130+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3949
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-22T12:28:59.583540+00:00_

Web search results for query: "ACL Rolling Review review form soundness excitement reproducibility scoring 1-5"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's what I found about the ACL Rolling Review's scoring system:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness

For Findings papers, the main criteria are soundness and reproducibility. The scale ranges from 5 = Excellent (one of the most thorough studies) to 4 = Strong (provides sufficient support for all claims). Soundness scores must be justified by the text of the review.

## Excitement

Excitement captures the more subjective evaluations of the novelty/significance of the contributions, and their potential interesting-ness to the community. Excitement is a separate score that is orthogonal to the assessment of the soundness of the paper. A score of 1 = Not Exciting means the paper does not resonate with the reviewer and they don't think it would with others in the *ACL community.

## Ov
…[truncated 578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7533
}
```

</details>

---


### Tool result

_source line 1502 · 2026-05-22T12:29:00.592923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5209
}
```

</details>

---


### Tool result

_source line 1503 · 2026-05-22T12:29:01.851926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5810
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-22T12:29:02.154034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5805
}
```

</details>

---


### Tool result

_source line 1505 · 2026-05-22T12:29:02.609900+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5752
}
```

</details>

---


### Tool result

_source line 1506 · 2026-05-22T12:29:03.214958+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5095
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-22T12:29:03.266413+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5147
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-22T12:29:13.338496+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "11-20",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "11-20",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 1509 · 2026-05-22T12:29:13.589986+00:00_

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

_source line 1510 · 2026-05-22T12:29:14.545001+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 627.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 614.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 559.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 368.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.3}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.5}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 558.6}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-22T12:29:14.545578+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1512 · 2026-05-22T12:29:19.382005+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions. I need the exact criteria for Soundness, Excitement/Novelty, Overall Assessment, Reproducibility, and any other dimensions."
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
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions. I need the exact criteria for Soundness, Excitement/Novelty, Overall Assessment, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 1513 · 2026-05-22T12:29:19.837855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p11.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 1514 · 2026-05-22T12:29:20.793219+00:00_



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

_source line 1515 · 2026-05-22T12:29:20.794085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p12.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 1516 · 2026-05-22T12:29:21.346837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p13.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-22T12:29:21.800104+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1518 · 2026-05-22T12:29:21.800546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p14.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 1519 · 2026-05-22T12:29:22.707368+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool result

_source line 1520 · 2026-05-22T12:29:22.710176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool call

_source line 1521 · 2026-05-22T12:29:22.711323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p15.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-22T12:29:23.214384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p16.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-22T12:29:23.719865+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-22T12:29:23.720318+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p17.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 1525 · 2026-05-22T12:29:24.576609+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1362
}
```

</details>

---


### Tool result

_source line 1526 · 2026-05-22T12:29:24.578802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---


### Tool call

_source line 1527 · 2026-05-22T12:29:24.579213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p18.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p18.png"
  }
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-22T12:29:25.081825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p19.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p19.png"
  }
}
```

</details>

---


### Tool result

_source line 1529 · 2026-05-22T12:29:25.384243+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-22T12:29:25.385805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p20.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-22T12:29:26.141939+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1060
}
```

</details>

---


### Tool result

_source line 1532 · 2026-05-22T12:29:26.396132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-22T12:29:26.748392+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** Quite sure with careful checking; unlikely to have missed relevant details
- **3:** Reasonably confident but possible gaps in technical verification
- **2:** Willing to defend evaluation, though likely some details were missed
- **1:** "Not my area, or paper is very hard to understand"

## Soundness
Scale: 1-5 (with half-point options)
- **5:** "Excellent: This study is one of the most thorough I have seen"
- **4:** Strong support for all claims; additional experiments optional
- **3:** "Acceptable: This study provides sufficient support for its main claims"
- **2:** Poor - major claims lack adequate support; significant methodological problems
- **1:** "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with half-point options)
- **5:** "Highly Exciting: I would recommend this paper to others"
- **4:** Exciting; would mention to colleagues or attend presentation
- **3:** Interesting but may attend only if time permits
- **2:** "Potentially Interesting: does not resonate with me, but it might with others"
- **1:** Not exciting; unlikely to resonate with broader community

## Overall Assessment
Scale: 1-5 (with half-point options)
- **5:** Consider for Award (top 2.5% papers)
- **4:** Conference acceptance recommended
- **3:** Findings acceptance recommended
- **2:** Resubmit after substantial revisions next cycle
- **1:** Do not resubmit or lacks relevance to computational linguistics

## Reproducibility
Scale: 1-5
- **5:** Results easily reproducible
- **4:** Mostly reproducible with minor variations possible
- **3:** Reproducible with difficulty; underspecified parameters
- **2:** "Hard pressed to reproduce"; unavailable data or insufficient details
- **1:** "Would not be able to reproduce the results"
…[truncated 241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7366
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-22T12:29:45.090013+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "21-34",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "21-34",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-22T12:29:48.520356+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.0}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.8}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.1}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.1}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.2}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.9}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 403.4}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.4}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_const
…[truncated 1519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3430
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-22T12:29:52.651170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p21.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p21.png"
  }
}
```

</details>

---


### Tool call

_source line 1537 · 2026-05-22T12:29:53.157848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p22.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p22.png"
  }
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-22T12:29:54.263900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p23.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p23.png"
  }
}
```

</details>

---


### Tool call

_source line 1539 · 2026-05-22T12:29:54.718867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p24.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 1540 · 2026-05-22T12:29:55.330727+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2679
}
```

</details>

---


### Tool call

_source line 1541 · 2026-05-22T12:29:55.331240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p25.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 1542 · 2026-05-22T12:29:56.089723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2931
}
```

</details>

---


### Tool call

_source line 1543 · 2026-05-22T12:29:56.090249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p26.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p26.png"
  }
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-22T12:29:56.543188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p27.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-22T12:29:56.947739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2683
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-22T12:29:56.949204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p28.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1547 · 2026-05-22T12:29:58.108788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3389
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-22T12:29:58.109267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p29.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p29.png"
  }
}
```

</details>

---


### Tool call

_source line 1549 · 2026-05-22T12:29:58.109518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p30.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 1550 · 2026-05-22T12:29:58.515642+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3184
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-22T12:29:58.924319+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2381
}
```

</details>

---


### Tool result

_source line 1552 · 2026-05-22T12:29:59.378746+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3288
}
```

</details>

---


### Tool result

_source line 1553 · 2026-05-22T12:30:00.285399+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3336
}
```

</details>

---


### Tool result

_source line 1554 · 2026-05-22T12:30:00.789586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2680
}
```

</details>

---


### Tool result

_source line 1555 · 2026-05-22T12:30:00.941507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2832
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-22T12:30:06.786876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p31.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p31.png"
  }
}
```

</details>

---


### Tool call

_source line 1557 · 2026-05-22T12:30:07.191162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p32.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p32.png"
  }
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-22T12:30:08.401877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p33.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p33.png"
  }
}
```

</details>

---


### Tool call

_source line 1559 · 2026-05-22T12:30:08.604157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p34.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p34.png"
  }
}
```

</details>

---


### Tool result

_source line 1560 · 2026-05-22T12:30:08.856596+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2069
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-22T12:30:10.472007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3280
}
```

</details>

---


### Tool result

_source line 1562 · 2026-05-22T12:30:10.774463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2170
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-22T12:30:11.234902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2833
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-22T12:32:13.162479+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "XGrammar Dong et al 2025 flexible efficient grammar-guided LLM generation"
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
    "query": "XGrammar Dong et al 2025 flexible efficient grammar-guided LLM generation"
  }
}
```

</details>

---


### Tool call

_source line 1565 · 2026-05-22T12:32:13.263665+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GoLLIE Sainz et al 2024 annotation guidelines information extraction zero-shot learning"
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
    "query": "GoLLIE Sainz et al 2024 annotation guidelines information extraction zero-shot learning"
  }
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-22T12:32:14.267957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SciERC Luan et al 2018 multi-task identification entities relations coreference scientific knowledge graph"
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
    "query": "SciERC Luan et al 2018 multi-task identification entities relations coreference scientific knowledge graph"
  }
}
```

</details>

---


### Tool call

_source line 1567 · 2026-05-22T12:32:15.272925+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geng et al 2023 grammar-constrained decoding structured NLP tasks without finetuning EMNLP"
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
    "query": "Geng et al 2023 grammar-constrained decoding structured NLP tasks without finetuning EMNLP"
  }
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-22T12:32:15.273377+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EnriCo Zaratiana et al 2024 ASP answer set programming joint entity relation extraction generation"
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
    "query": "EnriCo Zaratiana et al 2024 ASP answer set programming joint entity relation extraction generation"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-22T12:32:18.637906+00:00_

Web search results for query: "XGrammar Dong et al 2025 flexible efficient grammar-guided LLM generation"

Links: [{"title":"Catalyst: XGrammar","url":"https://catalyst.cs.cmu.edu/projects/xgrammar.html"},{"title":"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=rjQfX0YgDl"},{"title":"[2411.15100] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100"},{"title":"[2411.15100v1] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://arxiv.org/abs/2411.15100v1"},{"title":"XGrammar: Flexible and Efficient Structured Generation ...","url":"https://arxiv.org/pdf/2411.15100"},{"title":"MLSys Poster XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models","url":"https://mlsys.org/virtual/2025/poster/3235"},{"title":"GitHub - mlc-ai/xgrammar: Fast, Flexible and Portable Structured Generation · GitHub","url":"https://github.com/mlc-ai/xgrammar"},{"title":"Track: Session 10: LLM and Diffusion Model Serving","url":"https://mlsys.org/virtual/2025/session/3161"},{"title":"[PDF] XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGrammar:-Flexible-and-Efficient-Structured-Engine-Dong-Ruan/274ca059ee4997f1e008bc8962aef3d22897f17a"}]

Based on the search results, here's what I found about XGrammar:

XGrammar is an open-source library for efficient, flexible, and portable structured generation. The paper was authored by Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang Lai, Ziyi Xu, Yilong Zhao, and Tianqi Chen, published in MLSys 2025.

**Key Technical Approach:**
XGrammar accelerates context-free grammar execution by dividing the vocabulary into context-independent tokens that can be prechecked and context-dependent tokens that need to be
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5475
}
```

</details>

---


### Tool result

_source line 1570 · 2026-05-22T12:32:20.396866+00:00_

Web search results for query: "SciERC Luan et al 2018 multi-task identification entities relations coreference scientific knowledge graph"

Links: [{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/D18-1360/"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://www.researchgate.net/publication/327303141_Multi-Task_Identification_of_Entities_Relations_and_Coreference_for_Scientific_Knowledge_Graph_Construction"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - Consensus","url":"https://k8s.consensus.app/papers/details/ce11b64546755e678612cfea3b404121/"},{"title":"[PDF] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multi-Task-Identification-of-Entities,-Relations,-Luan-He/b21b927c251c415b601b6d7f785a42cc5c292635"},{"title":"[1808.09602] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602"},{"title":"[1808.09602v1] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602v1"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ORKG","url":"https://orkg.org/paper/R36010"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for   Scientific Knowledge Graph Construction","url":"https://arxiv.org/pdf/1808.09602"},{"title":"Multi-Task Identification of Entities, Relations, and ...","url":"https://aclanthology.org/D18-1360.pdf"}]

Based on the search results, here's the information about the Luan 
…[truncated 1187 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6128
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-22T12:32:20.497642+00:00_

Web search results for query: "GoLLIE Sainz et al 2024 annotation guidelines information extraction zero-shot learning"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"},{"title":"Translation and Fusion Improves Zero-shot Cross-lingual Information   Extraction","url":"https://arxiv.org/pdf/2305.13582"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"}]

Based on the search results, here's information about the GoLLIE paper by Sainz et al. 2024:

## Overview

GoLLIE (Guideline-following Large Language Model for IE) was authored by Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, and Eneko Agirre, and was presented at the 12th International Conference on Learning Representations (ICLR) 2024.

## Key Contribution

GoLLIE is a model able to improve zero-shot results on unseen IE tasks by virtue of being 
…[truncated 866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7233
}
```

</details>

---


### Tool result

_source line 1572 · 2026-05-22T12:32:21.751524+00:00_

Web search results for query: "EnriCo Zaratiana et al 2024 ASP answer set programming joint entity relation extraction generation"

Links: [{"title":"GitHub - urchade/EnriCo: EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://github.com/urchade/EnriCo"},{"title":"[2305.15374] ASPER: Answer Set Programming Enhanced Neural Network Models for Joint Entity-Relation Extraction","url":"https://arxiv.org/abs/2305.15374"},{"title":"ASPER: Answer Set Programming Enhanced Neural Network Models for Joint Entity-Relation Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230515374H/abstract"},{"title":"EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/html/2404.12493v1"},{"title":"ASPER: Answer Set Programming Enhanced Neural Network Models for Joint   Entity-Relation Extraction","url":"https://arxiv.org/pdf/2305.15374"},{"title":"urchade (Urchade Zaratiana) · GitHub","url":"https://github.com/urchade"},{"title":"Urchade Zaratiana","url":"https://urchade.github.io/"},{"title":"[2404.12493] EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction","url":"https://arxiv.org/abs/2404.12493"}]

Based on the search results, I found information about the papers you're looking for:

## EnriCo (2024)

EnriCo addresses joint entity and relation extraction, which plays a pivotal role in various applications, notably in the construction of knowledge graphs. The model leverages attention mechanisms for rich representation, and introduces decoding algorithms designed to infer the highest scoring solutions while adhering to task and dataset-specific constraints.

The paper is titled "EnriCo: Enriched Representation and Globally Constrained Inference for Entity and Relation Extraction" by Urchade Zaratiana, Nadi Tomeh, Yann Dauxais, Pierre Holat and Thierry Charnois (2024).

## ASPER - Answ
…[truncated 792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6478
}
```

</details>

---


### Tool result

_source line 1573 · 2026-05-22T12:32:21.802607+00:00_

Web search results for query: "Geng et al 2023 grammar-constrained decoding structured NLP tasks without finetuning EMNLP"

Links: [{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.674/"},{"title":"[PDF] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Grammar-Constrained-Decoding-for-Structured-NLP-Geng-Josifosky/7e269bfabb451765a16ca0357de6b497cefb60bf"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"[2305.13971] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/abs/2305.13971"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"Flexible and Efficient Grammar-Constrained Decoding","url":"https://arxiv.org/pdf/2502.05111"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Request PDF","url":"https://www.researchgate.net/publication/376402267_Grammar-Constrained_Decoding_for_Structured_NLP_Tasks_without_Finetuning"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning","url":"https://arxiv.org/pdf/2305.13971"}]

I found the paper! Here's the information about the Geng et al. 2023 paper:

**Citation Information:**

The paper "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning" was authored by Saibo Geng, Martin Josifoski, Maxime Peyrard, and Robert West and published at the 2023 Conference on Empirical Methods in Natural Language Processing in Decembe
…[truncated 1009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6529
}
```

</details>

---


### Tool call

_source line 1574 · 2026-05-22T12:32:52.703114+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Scholak et al 2021 PICARD parsing incrementally constrained autoregressive decoding SQL"
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
    "query": "Scholak et al 2021 PICARD parsing incrementally constrained autoregressive decoding SQL"
  }
}
```

</details>

---


### Tool call

_source line 1575 · 2026-05-22T12:32:53.004818+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schall Gerard de Melo 2025 \"hidden cost of structure\" constrained decoding language model performance"
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
    "query": "Schall Gerard de Melo 2025 \"hidden cost of structure\" constrained decoding language model performance"
  }
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-22T12:32:54.059647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Costi Drago OntologyCL ontology-guided knowledge graph extraction 2025 arXiv"
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
    "query": "Costi Drago OntologyCL ontology-guided knowledge graph extraction 2025 arXiv"
  }
}
```

</details>

---


### Tool call

_source line 1577 · 2026-05-22T12:32:55.014120+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mundler et al 2025 \"code-to-code\" compilation executable semantic constraints LLM agents arXiv"
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
    "query": "Mundler et al 2025 \"code-to-code\" compilation executable semantic constraints LLM agents arXiv"
  }
}
```

</details>

---


### Tool call

_source line 1578 · 2026-05-22T12:32:55.265567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BoostCD constrained decoding information extraction LLM 2024 2025"
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
    "query": "BoostCD constrained decoding information extraction LLM 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-22T12:32:58.581198+00:00_

Web search results for query: "Scholak et al 2021 PICARD parsing incrementally constrained autoregressive decoding SQL"

Links: [{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | DeepAI","url":"https://deepai.org/publication/picard-parsing-incrementally-for-constrained-auto-regressive-decoding-from-language-models"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.779/"},{"title":"GitHub - ServiceNow/picard: PICARD - Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models. PICARD is a ServiceNow Research project that was started at Element AI. · GitHub","url":"https://github.com/ServiceNow/picard"},{"title":"[2109.05093] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://arxiv.org/abs/2109.05093"},{"title":"[2109.05093v1] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://arxiv.org/abs/2109.05093v1"},{"title":"[Quick Review] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://liner.com/review/picard-parsing-incrementally-for-constrained-autoregressive-decoding-from-language-models"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models","url":"https://tscholak.github.io/publications/picard"},{"title":"[PDF] PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PICARD:-Parsing-Incrementally-for-Constrained-from-Scholak-Schucher/5fbcfccd3736969d95ed660d8e6962c86b7a9113"},{"title":"tscholak/1wnr382e · Hugging Face","url":"https://huggingface.co/tscholak/1wnr382e"},{"title":"PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language 
…[truncated 1344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5878
}
```

</details>

---


### Tool result

_source line 1580 · 2026-05-22T12:32:59.385055+00:00_

Web search results for query: "Schall Gerard de Melo 2025 "hidden cost of structure" constrained decoding language model performance"

Links: [{"title":"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance - ACL Anthology","url":"https://aclanthology.org/2025.ranlp-1.124/"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"How Constrained Decoding Affects Language Model ...","url":"https://aclanthology.org/2025.ranlp-1.124.pdf"},{"title":"From Hallucination to Structure Snowballing: The Alignment Tax of Constrained Decoding in LLM Reflection","url":"https://arxiv.org/pdf/2604.06066"},{"title":"The Format Tax","url":"https://arxiv.org/pdf/2604.03616"},{"title":"Draft-Conditioned Constrained Decoding for Structured Generation in LLMs","url":"https://arxiv.org/pdf/2603.03305"}]

I found the paper you were searching for! Here are the search results:

"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" is a paper by Maximilian Schall and Gerard de Melo, published at RANLP 2025 in Varna, Bulgaria.

The paper investigates how Large Language Models can generate structured outputs like JSON that can be programmatically processed, while also examining how this affects task performance. The researchers conducted comprehensive experiments across 11 models and multiple benchmarks, uncovering a fundamental divergence between base and instruction-tuned models under structural constraints.

Key findings include:

- Successful constrained generation requires both adapted prompts and sufficient few-shot examples, with constrained models showing steeper performance gains from additional demonstrations compared to unconstrained generation.

- Base model performance under constraints can serve as an early indicator of post-training structured output capabilities, offering a practical evaluation tool 
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6380
}
```

</details>

---


### Tool result

_source line 1581 · 2026-05-22T12:33:00.994797+00:00_

Web search results for query: "Mundler et al 2025 "code-to-code" compilation executable semantic constraints LLM agents arXiv"

Links: [{"title":"[2602.03439] Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents","url":"https://arxiv.org/abs/2602.03439"},{"title":"Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents","url":"https://arxiv.org/pdf/2602.03439"},{"title":"[2504.09246] Type-Constrained Code Generation with Language Models","url":"https://arxiv.org/abs/2504.09246"},{"title":"Executable Code Actions Elicit Better LLM Agents","url":"https://arxiv.org/pdf/2402.01030"},{"title":"Agentic Code Reasoning","url":"https://arxiv.org/pdf/2603.01896"}]

Based on the search results, I found a closely related paper but not exactly the query you specified. Here's what I found:

The search returned "Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents" by Xiaochi Zhou and co-authors, which appears on arXiv as paper 2602.03439 (released February 4, 2026).

However, the paper you're searching for appears to be "Type-Constrained Code Generation with Language Models" by Niels Mündler et al., which was updated on May 8, 2025 (arXiv 2504.09246). This paper seems more aligned with your query about "code-to-code" compilation and constraints on LLM agents.

The Mündler et al. paper focuses on constraining LLM code generation using formal type system rules, which relates to your search for executable semantic constraints. Would you like more information about either of these papers?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5980
}
```

</details>

---


### Tool result

_source line 1582 · 2026-05-22T12:33:02.551649+00:00_

Web search results for query: "Costi Drago OntologyCL ontology-guided knowledge graph extraction 2025 arXiv"

Links: [{"title":"[2510.01409] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409"},{"title":"[2510.01409v1] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409v1"},{"title":"[2507.20643] Ontology-Enhanced Knowledge Graph Completion using Large Language Models","url":"https://arxiv.org/abs/2507.20643"},{"title":"OntoLogX: Ontology‐Guided Knowledge Graph Extraction From Cybersecurity Logs With Large Language Models - Cotti - Advanced Intelligent Systems - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501381"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/html/2510.01409v2"},{"title":"OntoMetric: An Ontology-Driven LLM-Assisted Framework for Automated ESG Metric Knowledge Graph Generation","url":"https://arxiv.org/pdf/2512.01289"}]

I found relevant research related to your query. The search results show work on ontology-guided knowledge graph extraction, though the primary result is "OntoLogX" rather than "OntologyCL":

OntoLogX is an autonomous AI agent that leverages Large Language Models to transform raw logs into ontology-grounded Knowledge Graphs, integrating a lightweight log ontology with Retrieval Augmented Generation and iterative correction steps to ensure syntactically and semantically valid KGs. The authors include Idilio Drago from the University of Turin.

The paper was published on arXiv as paper 2510.01409 in October 2025. The search results don't show a paper specifically titled "OntologyCL," but this OntoLogX work appears to be the most recent arXiv publication on ontology-guided knowledge graph extraction with similar aut
…[truncated 151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8492
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-22T12:33:02.753055+00:00_

Web search results for query: "BoostCD constrained decoding information extraction LLM 2024 2025"

Links: [{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/pdf/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901v1"},{"title":"Sketch-Guided Constrained Decoding for Boosting Blackbox Large Language   Models without Logit Access","url":"https://arxiv.org/pdf/2401.09967"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"}]

I found relevant information about BoostCD. Here's what the search results show:

## BoostCD Overview

BoostCD (Boosted Constrained Decoding) combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice in constrained and unconstrained mode to obtain two weak predictions, and in phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction.

## How It Works

The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance.

## Application to Information Extraction

BoostCD is applied to closed information extraction in a model called BoostIE, which outperforms pr
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7487
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-22T12:35:17.567457+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.01409 OntoLogX authors Cotti Drago exact title"
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
    "query": "arXiv 2510.01409 OntoLogX authors Cotti Drago exact title"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-22T12:35:23.797075+00:00_

Web search results for query: "arXiv 2510.01409 OntoLogX authors Cotti Drago exact title"

Links: [{"title":"[2510.01409] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409"},{"title":"[2510.01409v1] OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/abs/2510.01409v1"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models","url":"https://arxiv.org/html/2510.01409"},{"title":"OntoLogX: Ontology‐Guided Knowledge Graph Extraction From Cybersecurity Logs With Large Language Models - Cotti - Advanced Intelligent Systems - Wiley Online Library","url":"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501381?af=R"},{"title":"OntoLogX: Ontology-Guided Knowledge Graph Extraction from","url":"https://arxiv.org/pdf/2510.01409"}]

Based on the search results, here is the information about arXiv paper 2510.01409:

**Exact Title:** OntoLogX: Ontology-Guided Knowledge Graph Extraction from Cybersecurity Logs with Large Language Models

**Authors:** Luca Cotti, Idilio Drago, Anisa Rula, Devis Bianchini, Federico Cerutti

**Submission Date:** October 1, 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6229
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-22T12:35:42.288209+00:00_

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

_source line 1587 · 2026-05-22T12:35:42.464337+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 176
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-22T12:37:29.491308+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 工程集成扎实、实验极其充分，但核心技术贡献是已有组件（XGrammar + runtime type checking）的系统集成，算法层面新颖性不足以支撑主会议接收；同时存在一个疑似 AI 生成的错误引用。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 实验设计严谨，3 数据集 × 多模型 × 大量消融；Proposition 1 证明完整（Appendix O）。WikiEvents fine-tuning 标注\"preliminary\"略减分。 |\n| Excitement | 2.5 / 5 | Grammar layer 直接套用 XGrammar，semantic layer 是 runtime type check（PICARD 式思路移植到 IE），Proposition 1 是标准 pumping lemma 论证。集成虽精心但不令人兴奋。 |\n| Overall Assessment | 3.0 / 5 | Findings 级别——sound + thorough，但 novelty 不够主会议。 |\n| Reproducibility | 4 / 5 | Prompt 模板（Appendix A）、超参（Appendix G）、seed 方差分析（Appendix G）均提供，但代码未开源（承诺 acceptance 后发布）。 |\n| Confidence | 4 / 5 | 熟悉 constrained decoding 和 IE 领域，仔细阅读全文含 25 页 appendix。 |\n\n---\n\n## 主要优势\n\n**S1: 实验深度罕见。** 3 个 IE 任务（NER+RE / RE / EE）、4 个模型（3×8B + 1×70B）、3 个 tokenizer family、zero-shot + LoRA fine-tuning、S1/S2 两种 decoding 策略、beam search（Appendix F）、文档长度分析（Appendix H）、prompt 敏感性（Appendix I）、采样鲁棒性（Appendix E）。25 页 appendix 的分析密度在 constrained decoding 论文中几乎没有见过。\n\n**S2: 理论基础扎实。** Proposition 1（Appendix O 完整证明）形式化地证明了 IE type constraints 超越 CFG 的表达能力，为两层架构提供了必要性论证。这不只是工程直觉，而是有证明支撑的设计。Decidability taxonomy（§2）将 IE 约束分为 3 级，分析框架可复用。\n\n**S3: 实用设计选择。** Grammar-first fallback（§3.3）在语义约束过紧时优雅降级到 grammar-only enforcement，避免生成无效 JSON。框架不需要模型修改，兼容 LoRA fine-tuning（Table 2）。Tokenizer-agnostic type masking（§3.3）通过 continuation masking 处理跨 tokenizer 差异。\n\n**S4: Empirical enabling dependency 是非平凡发现。** Table 1 显示 grammar layer 是 semantic layer 有效运作的前提——去掉 grammar layer 后 semantic layer 只能降低 DR 24%（vs. 完整系统 42-99%）。这种层间依赖关系不是先验可预测的。\n\n**S5: 分析诚实透明。** 论文坦诚讨论 CF trade-off（§5.1）、模型依赖性、GENERIC→X schema ambiguity、DR 与 CF 的 dual-factor pattern（Appendix D, Figure 2），以及 fine-tuning 与 constraint 的正交关系。Limitations section 涵盖了 7+ 个具体局限点。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心新颖性不足——系统集成而非算法创新**\n- 具体位置：§3.2 Grammar Layer, §3.3 Semantic Layer, §2 Proposition 1\n- 问题：Grammar layer 直接将 IE JSON schema 编译为 XGrammar（Dong et al., 2025）的 CFG——这是对已有工具的直接应用，Section 3.2 仅描述了 \"JSON Schema encoding Eq. (1) with *n* enum constraints is compiled into a pushdown automaton via XGrammar\"。Semantic layer 实现 runtime entity registry + dynamic masking，概念上与 PICARD（Scholak et al., 2021）的 incremental constraint checking 同构——只是从 SQL 域移植到 IE 域。Proposition 1 使用标准 pumping lemma 证明 IE type constraints 超出 CFG，这形式化了从业者已有的直觉（关系类型依赖于实体类型，而实体是动态生成的），但证明本身是 routine 的。\n- 为什么影响接收：ACL 主会议期望 substantial novelty。本文的贡献更接近 \"careful engineering + thorough evaluation\" 而非 \"novel algorithm/method\"。Findings 标准（sound + useful）是满足的。\n- 建议修改方向：(1) 更清晰地阐述与 PICARD 的技术区别——不仅是领域不同，机制上的差异是什么？(2) 强调 empirical enabling dependency（S4）作为核心科学发现而非附属分析 (3) 考虑将 κ̄ metric 发展为更通用的 constrained decoding 分析工具。\n\n**N2** [critical] **引用准确性问题——疑似 AI 生成的错误引用**\n- 具体位置：References, page 10\n- 问题：引用 \"Luca Cotti, Ildio Drago, Anna Ruia, Devis Bianchini, and Federico Creviti. 2025. OntologyCL: Ontology-guided knowledge graph extraction from synchronous logs with large language models. Preprint, arXiv:2510.01409\" 存在**多处事实错误**。arXiv:2510.01409 的实际信息为：\n  - 标题：**OntoLogX**（非 \"OntologyCL\"）\n  - 副标题：**Cybersecurity Logs**（非 \"synchronous logs\"）\n  - 作者：**Idilio Drago**（非 \"Ildio Drago\"）、**Anisa Rula**（非 \"Anna Ruia\"）、**Federico Cerutti**（非 \"Federico Creviti\"）\n  标题、领域描述、三个作者名同时出错，这种模式与 AI hallucination 一致，不像简单 typo。\n- 为什么影响接收：引用准确性是学术诚信的基本要求。ARR reviewer guidelines 明确要求 reviewer 检查引用。一个 fabricated/hallucinated citation 会严重损害论文可信度，并可能引发 reviewer 对其他引用的怀疑。\n- 建议修改方向：立即核实并修正该引用。建议对全部 references 做一次人工核查。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **\"四个模型\"声称具有误导性**\n- 具体位置：Abstract (\"four models (7-70B)\"), §1 Introduction, §5 Experiments\n- 问题：Abstract 和 Introduction 突出宣称 \"four models (7-70B), three tokenizer families\"，但 70B 模型（Llama-3.3-70B, page 8）仅有一段文字报告两个数据集的 zero-shot 结果（DR=0%, CF=5.50-7.01%）。没有独立表格、没有 fine-tuning、没有消融、没有 beam search。其他三个 8B 模型各有完整的多节评估。这种不对称使读者高估了评估广度。\n- 建议：要么完善 70B 评估至少包含一个数据集的 fine-tuning + 消融，要么将 70B 降级为 \"preliminary exploration\" 而非 headline claim。\n\n**W2** [warning] **WikiEvents fine-tuning 结果明确标注为 \"preliminary\"**\n- 具体位置：§5.4, page 7 (\"Fine-tuning results are preliminary\")\n- 问题：论文声称 3 数据集全面评估，但 WikiEvents 的 fine-tuning 仅有初步结果（n=20, 非完整数据集）。Zero-shot 评估完整但 fine-tuning——也就是论文定位为 \"deployment-relevant\" 的设置——不完整。\n- 建议：完成 WikiEvents fine-tuning 实验，或在 abstract/introduction 中明确标注 WikiEvents 为 \"preliminary extension\"。\n\n**W3** [warning] **Zero-shot 实验占比过大但 F1 极低**\n- 具体位置：§5.1-§5.4, Tables 1/3/4/5, Appendix C-F\n- 问题：SciERC zero-shot R-F1 范围为 1.30-8.05（Table 1），DocRED 为 0.03-10.03。虽然论文在 page 5 明确将 zero-shot 定位为 \"diagnostic\"，但论文的大部分实验空间（主文 + appendix）都花在 zero-shot 分析上。在如此低的绝对 F1 下，constraint enforcement 的实际意义有限（减少的 violations 对应的是几乎不可用的抽取结果）。Fine-tuned setting（R-F1 40-46%）更有实际价值但篇幅较少。\n- 建议：考虑重新平衡 zero-shot vs. fine-tuned 的篇幅分配，或更清晰地论证为什么在 R-F1 < 10% 的场景下 constraint enforcement 仍有独立价值。\n\n**W4** [warning] **κ̄ metric 的可复用性和实用性论证不足**\n- 具体位置：§5, Definition of κ̄; Figure 2; Appendix D\n- 问题：κ̄ 定义为 1 - |valid|/|all| 的 schema 级平均。Figure 2 展示了 κ̄ 与 residual DR 的线性相关。但这接近于 tautology——更严格的约束留下更少合法选项，因此违反更难被约束系统解决（或更容易，取决于角度）。论文没有论证 practitioner 在什么场景下会独立计算和使用 κ̄。\n- 建议：展示 κ̄ 在 ontology 设计阶段的指导价值——例如，ontology 设计者如何根据 κ̄ 调整 schema 以获得更好的 constraint enforcement 效果。\n\n**W5** [warning] **Abstract 数值密度过高，部分 range 可能误导**\n- 具体位置：Abstract\n- 问题：\"DR drops 42-99% across models and datasets\" 跨越了所有配置的 min-max 范围，掩盖了典型表现。Abstract 中 zero-shot 和 fine-tuned 统计数字交替出现（DR ≤ 0.09%, CF ≤ 1.4% fine-tuned, up to 12% zero-shot），读者难以快速区分两种设置的预期效果。\n- 建议：在 abstract 中分开报告 zero-shot 和 fine-tuned 的 key metrics，避免跨设置的 min-max range。\n\n**W6** [warning] **GCD-equivalent baseline 对比放在 appendix 而非主文**\n- 具体位置：Appendix D (Table 15)\n- 问题：Table 15 展示了 grammar-only（GCD-equivalent）baseline 的效果：ET=0%, RV=0% 但 DR 升至 15-96%。由于 GCD（Geng et al., 2023）是最直接的 prior work，这个对比理应出现在主文中，而非隐藏在 appendix。\n- 建议：将 Table 15 的核心数据整合到主文实验部分。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 密度极高（6+ 列 × 多行 × 多 metric），考虑拆分或使用 heatmap 提升可读性。\n- Figure 1 (page 3) 的 overview diagram 信息量充足但视觉层次不够分明——grammar layer 和 semantic layer 的视觉区分可以更强。\n- §3.3 \"Grammar-semantic interaction\" 部分描述 G(t) ∩ S(t) 的交集操作，公式 (2) 的 asymmetric conjunction 说明可以更直观（例如加一个 Venn 图）。\n- Appendix 标签从 A 到 O 共 15 个，部分标签引用在正文中密度很高（如 page 5 的 \"Appendix N, M\"），读者追踪成本高。\n- References 格式中部分 arXiv preprint 缺少 submission date（仅有年份），与已发表论文混排时不够清晰。\n\n---\n\n## 引用抽查结果（10+ 篇）\n\n| 引用 | 状态 | 备注 |\n|------|------|------|\n| XGrammar (Dong et al., 2025) — MLSys | ✅ 正确 | 标题、作者、venue 均匹配 |\n| GoLLIE (Sainz et al., 2024) — ICLR | ✅ 正确 | |\n| SciERC (Luan et al., 2018) — EMNLP | ✅ 正确 | |\n| GCD (Geng et al., 2023) — EMNLP | ✅ 正确 | |\n| PICARD (Scholak et al., 2021) — EMNLP | ✅ 正确 | |\n| Schall & de Melo, 2025 — RANLP | ✅ 正确 | |\n| EnriCo (Zaratiana et al., 2024) | ✅ 正确 | 论文描述为 constrained inference，准确 |\n| DocRED (Yao et al., 2019) | ✅ 正确 | |\n| BoostCD (EMNLP 2025) | ✅ 正确 | 实际存在，引用可查 |\n| **OntologyCL (Cotti et al., 2025)** | ❌ **多处错误** | 标题、副标题、3个作者名均与 arXiv:2510.01409 实际内容不符（详见 N2） |\n\n---\n\n## 主要优势总结\n\n1. **实验深度在同类工作中名列前茅**——消融、鲁棒性、跨模型、跨 tokenizer、跨文档长度的评估极为全面\n2. **理论与实践结合**——Proposition 1 提供 formal justification，empirical enabling dependency 提供实验验证\n3. **Grammar-first fallback 机制设计精巧**——在约束过严时优雅降级，避免系统脆性\n4. **透明诚实的局限性讨论**——CF trade-off、模型依赖性、schema ambiguity 均坦诚讨论\n5. **可复现性良好**——Prompt 模板、超参、seed 方差分析均提供\n\n---\n\n## 最终评分\n\n**Overall Assessment: 3.0 / 5 (Findings)**\n\n理由：论文在工程层面执行出色——实验之全面在 constrained decoding 文献中罕见，grammar-first fallback 和 empirical enabling dependency 是有价值的贡献。但核心技术新颖性有限：grammar layer 是 XGrammar 的直接应用，semantic layer 是 PICARD 式 runtime constraint checking 向 IE 域的移植，Proposition 1 是标准 pumping lemma。\"Careful integration of known components + exhaustive evaluation\" 是 Findings 的典型 profile。引用准确性问题（N2）进一步拉低了整体印象。完成 W1-W3 的修改可能将评分提至 3.5（Borderline Conference），但 novelty ceiling 仍是主要限制因素。",
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
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 (via ACL Rolling Review)\n**审查侧重**: 新颖性 + 完整性 + 写作质量 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall**: 3.0 / 5 — Findings\n**一句话总结**: 工程集成扎实、实验极其充分，但核心技术贡献是已有组件（XGrammar + runtime type checking）的系统集成，算法层面新颖性不足以支撑主会议接收；同时存在一个疑似 AI 生成的错误引用。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4 / 5 | 实验设计严谨，3 数据集 × 多模型 × 大量消融；Proposition 1 证明完整（Appendix O）。WikiEvents fine-tuning 标注\"preliminary\"略减分。 |\n| Excitement | 2.5 / 5 | Grammar layer 直接套用 XGrammar，semantic layer 是 runtime type check（PICARD 式思路移植到 IE），Proposition 1 是标准 pumping lemma 论证。集成虽精心但不令人兴奋。 |\n| Overall Assessment | 3.0 / 5 | Findings 级别——sound + thorough，但 novelty 不够主会议。 |\n| Reproducibility | 4 / 5 | Prompt 模板（Appendix A）、超参（Appendix G）、seed 方差分析（Appendix G）均提供，但代码未开源（承诺 acceptance 后发布）。 |\n| Confidence | 4 / 5 | 熟悉 constrained decoding 和 IE 领域，仔细阅读全文含 25 页 appendix。 |\n\n---\n\n## 主要优势\n\n**S1: 实验深度罕见。** 3 个 IE 任务（NER+RE / RE / EE）、4 个模型（3×8B + 1×70B）、3 个 tokenizer family、zero-shot + LoRA fine-tuning、S1/S2 两种 decoding 策略、beam search（Appendix F）、文档长度分析（Appendix H）、prompt 敏感性（Appendix I）、采样鲁棒性（Appendix E）。25 页 appendix 的分析密度在 constrained decoding 论文中几乎没有见过。\n\n**S2: 理论基础扎实。** Proposition 1（Appendix O 完整证明）形式化地证明了 IE type constraints 超越 CFG 的表达能力，为两层架构提供了必要性论证。这不只是工程直觉，而是有证明支撑的设计。Decidability taxonomy（§2）将 IE 约束分为 3 级，分析框架可复用。\n\n**S3: 实用设计选择。** Grammar-first fallback（§3.3）在语义约束过紧时优雅降级到 grammar-only enforcement，避免生成无效 JSON。框架不需要模型修改，兼容 LoRA fine-tuning（Table 2）。Tokenizer-agnostic type masking（§3.3）通过 continuation masking 处理跨 tokenizer 差异。\n\n**S4: Empirical enabling dependency 是非平凡发现。** Table 1 显示 grammar layer 是 semantic layer 有效运作的前提——去掉 grammar layer 后 semantic layer 只能降低 DR 24%（vs. 完整系统 42-99%）。这种层间依赖关系不是先验可预测的。\n\n**S5: 分析诚实透明。** 论文坦诚讨论 CF trade-off（§5.1）、模型依赖性、GENERIC→X schema ambiguity、DR 与 CF 的 dual-factor pattern（Appendix D, Figure 2），以及 fine-tuning 与 constraint 的正交关系。Limitations section 涵盖了 7+ 个具体局限点。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **核心新颖性不足——系统集成而非算法创新**\n- 具体位置：§3.2 Grammar Layer, §3.3 Semantic Layer, §2 Proposition 1\n- 问题：Grammar layer 直接将 IE JSON schema 编译为 XGrammar（Dong et al., 2025）的 CFG——这是对已有工具的直接应用，Section 3.2 仅描述了 \"JSON Schema encoding Eq. (1) with *n* enum constraints is compiled into a pushdown automaton via XGrammar\"。Semantic layer 实现 runtime entity registry + dynamic masking，概念上与 PICARD（Scholak et al., 2021）的 incremental constraint checking 同构——只是从 SQL 域移植到 IE 域。Proposition 1 使用标准 pumping lemma 证明 IE type constraints 超出 CFG，这形式化了从业者已有的直觉（关系类型依赖于实体类型，而实体是动态生成的），但证明本身是 routine 的。\n- 为什么影响接收：ACL 主会议期望 substantial novelty。本文的贡献更接近 \"careful engineering + thorough evaluation\" 而非 \"novel algorithm/method\"。Findings 标准（sound + useful）是满足的。\n- 建议修改方向：(1) 更清晰地阐述与 PICARD 的技术区别——不仅是领域不同，机制上的差异是什么？(2) 强调 empirical enabling dependency（S4）作为核心科学发现而非附属分析 (3) 考虑将 κ̄ metric 发展为更通用的 constrained decoding 分析工具。\n\n**N2** [critical] **引用准确性问题——疑似 AI 生成的错误引用**\n- 具体位置：References, page 10\n- 问题：引用 \"Luca Cotti, Ildio Drago, Anna Ruia, Devis Bianchini, and Federico Creviti. 2025. OntologyCL: Ontology-guided knowledge graph extraction from synchronous logs with large language models. Preprint, arXiv:2510.01409\" 存在**多处事实错误**。arXiv:2510.01409 的实际信息为：\n  - 标题：**OntoLogX**（非 \"OntologyCL\"）\n  - 副标题：**Cybersecurity Logs**（非 \"synchronous logs\"）\n  - 作者：**Idilio Drago**（非 \"Ildio Drago\"）、**Anisa Rula**（非 \"Anna Ruia\"）、**Federico Cerutti**（非 \"Federico Creviti\"）\n  标题、领域描述、三个作者名同时出错，这种模式与 AI hallucination 一致，不像简单 typo。\n- 为什么影响接收：引用准确性是学术诚信的基本要求。ARR reviewer guidelines 明确要求 reviewer 检查引用。一个 fabricated/hallucinated citation 会严重损害论文可信度，并可能引发 reviewer 对其他引用的怀疑。\n- 建议修改方向：立即核实并修正该引用。建议对全部 references 做一次人工核查。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **\"四个模型\"声称具有误导性**\n- 具体位置：Abstract (\"four models (7-70B)\"), §1 Introduction, §5 Experiments\n- 问题：Abstract 和 Introduction 突出宣称 \"four models (7-70B), three tokenizer families\"，但 70B 模型（Llama-3.3-70B, page 8）仅有一段文字报告两个数据集的 zero-shot 结果（DR=0%, CF=5.50-7.01%）。没有独立表格、没有 fine-tuning、没有消融、没有 beam search。其他三个 8B 模型各有完整的多节评估。这种不对称使读者高估了评估广度。\n- 建议：要么完善 70B 评估至少包含一个数据集的 fine-tuning + 消融，要么将 70B 降级为 \"preliminary exploration\" 而非 headline claim。\n\n**W2** [warning] **WikiEvents fine-tuning 结果明确标注为 \"preliminary\"**\n- 具体位置：§5.4, page 7 (\"Fine-tuning results are preliminary\")\n- 问题：论文声称 3 数据集全面评估，但 WikiEvents 的 fine-tuning 仅有初步结果（n=20, 非完整数据集）。Zero-shot 评估完整但 fine-tuning——也就是论文定位为 \"deployment-relevant\" 的设置——不完整。\n- 建议：完成 WikiEvents fine-tuning 实验，或在 abstract/introduction 中明确标注 WikiEvents 为 \"preliminary extension\"。\n\n**W3** [warning] **Zero-shot 实验占比过大但 F1 极低**\n- 具体位置：§5.1-§5.4, Tables 1/3/4/5, Appendix C-F\n- 问题：SciERC zero-shot R-F1 范围为 1.30-8.05（Table 1），DocRED 为 0.03-10.03。虽然论文在 page 5 明确将 zero-shot 定位为 \"diagnostic\"，但论文的大部分实验空间（主文 + appendix）都花在 zero-shot 分析上。在如此低的绝对 F1 下，constraint enforcement 的实际意义有限（减少的 violations 对应的是几乎不可用的抽取结果）。Fine-tuned setting（R-F1 40-46%）更有实际价值但篇幅较少。\n- 建议：考虑重新平衡 zero-shot vs. fine-tuned 的篇幅分配，或更清晰地论证为什么在 R-F1 < 10% 的场景下 constraint enforcement 仍有独立价值。\n\n**W4** [warning] **κ̄ metric 的可复用性和实用性论证不足**\n- 具体位置：§5, Definition of κ̄; Figure 2; Appendix D\n- 问题：κ̄ 定义为 1 - |valid|/|all| 的 schema 级平均。Figure 2 展示了 κ̄ 与 residual DR 的线性相关。但这接近于 tautology——更严格的约束留下更少合法选项，因此违反更难被约束系统解决（或更容易，取决于角度）。论文没有论证 practitioner 在什么场景下会独立计算和使用 κ̄。\n- 建议：展示 κ̄ 在 ontology 设计阶段的指导价值——例如，ontology 设计者如何根据 κ̄ 调整 schema 以获得更好的 constraint enforcement 效果。\n\n**W5** [warning] **Abstract 数值密度过高，部分 range 可能误导**\n- 具体位置：Abstract\n- 问题：\"DR drops 42-99% across models and datasets\" 跨越了所有配置的 min-max 范围，掩盖了典型表现。Abstract 中 zero-shot 和 fine-tuned 统计数字交替出现（DR ≤ 0.09%, CF ≤ 1.4% fine-tuned, up to 12% zero-shot），读者难以快速区分两种设置的预期效果。\n- 建议：在 abstract 中分开报告 zero-shot 和 fine-tuned 的 key metrics，避免跨设置的 min-max range。\n\n**W6** [warning] **GCD-equivalent baseline 对比放在 appendix 而非主文**\n- 具体位置：Appendix D (Table 15)\n- 问题：Table 15 展示了 grammar-only（GCD-equivalent）baseline 的效果：ET=0%, RV=0% 但 DR 升至 15-96%。由于 GCD（Geng et al., 2023）是最直接的 prior work，这个对比理应出现在主文中，而非隐藏在 appendix。\n- 建议：将 Table 15 的核心数据整合到主文实验部分。\n\n---\n\n## 小问题（不影响接收）\n\n- Table 1 密度极高（6+ 列 × 多行 × 多 metric），考虑拆分或使用 heatmap 提升可读性。\n- Figure 1 (page 3) 的 overview diagram 信息量充足但视觉层次不够分明——grammar layer 和 semantic layer 的视觉区分可以更强。\n- §3.3 \"Grammar-semantic interaction\" 部分描述 G(t) ∩ S(t) 的交集操作，公式 (2) 的 asymmetric conjunction 说明可以更直观（例如加一个 Venn 图）。\n- Appendix 标签从 A 到 O 共 15 个，部分标签引用在正文中密度很高（如 page 5 的 \"Appendix N, M\"），读者追踪成本高。\n- References 格式中部分 arXiv preprint 缺少 submission date（仅有年份），与已发表论文混排时不够清晰。\n\n---\n\n## 引用抽查结果（10+ 篇）\n\n| 引用 | 状态 | 备注 |\n|------|------|------|\n| XGrammar (Dong et al., 2025) — MLSys | ✅ 正确 | 标题、作者、venue 均匹配 |\n| GoLLIE (Sainz et al., 2024) — ICLR | ✅ 正确 | |\n| SciERC (Luan et al., 2018) — EMNLP | ✅ 正确 | |\n| GCD (Geng et al., 2023) — EMNLP | ✅ 正确 | |\n| PICARD (Scholak et al., 2021) — EMNLP | ✅ 正确 | |\n| Schall & de Melo, 2025 — RANLP | ✅ 正确 | |\n| EnriCo (Zaratiana et al., 2024) | ✅ 正确 | 论文描述为 constrained inference，准确 |\n| DocRED (Yao et al., 2019) | ✅ 正确 | |\n| BoostCD (EMNLP 2025) | ✅ 正确 | 实际存在，引用可查 |\n| **OntologyCL (Cotti et al., 2025)** | ❌ **多处错误** | 标题、副标题、3个作者名均与 arXiv:2510.01409 实际内容不符（详见 N2） |\n\n---\n\n## 主要优势总结\n\n1. **实验深度在同类工作中名列前茅**——消融、鲁棒性、跨模型、跨 tokenizer、跨文档长度的评估极为全面\n2. **理论与实践结合**——Proposition 1 提供 formal justification，empirical enabling dependency 提供实验验证\n3. **Grammar-first fallback 机制设计精巧**——在约束过严时优雅降级，避免系统脆性\n4. **透明诚实的局限性讨论**——CF trade-off、模型依赖性、schema ambiguity 均坦诚讨论\n5. **可复现性良好**——Prompt 模板、超参、seed 方差分析均提供\n\n---\n\n## 最终评分\n\n**Overall Assessment: 3.0 / 5 (Findings)**\n\n理由：论文在工程层面执行出色——实验之全面在 constrained decoding 文献中罕见，grammar-first fallback 和 empirical enabling dependency 是有价值的贡献。但核心技术新颖性有限：grammar layer 是 XGrammar 的直接应用，semantic layer 是 PICARD 式 runtime constraint checking 向 IE 域的移植，Proposition 1 是标准 pumping lemma。\"Careful integration of known components + exhaustive evaluation\" 是 Findings 的典型 profile。引用准确性问题（N2）进一步拉低了整体印象。完成 W1-W3 的修改可能将评分提至 3.5（Borderline Conference），但 novelty ceiling 仍是主要限制因素。",
    "reviewer_id": "2",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-22T12:37:33.460016+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3968
}
```

</details>

---


### Tool call

_source line 1590 · 2026-05-22T12:37:40.044872+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
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
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1591 · 2026-05-22T12:37:40.095584+00:00_



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

_source line 1592 · 2026-05-22T12:37:44.411832+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-22T12:37:44.471273+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 59
}
```

</details>

---


### Assistant

_source line 1594 · 2026-05-22T12:37:52.333870+00:00_

Round 1 审稿完成。核心结论：

- **Overall 3.0 (Findings)**：工程执行优秀但算法新颖性不足
- **2 个 Must-Fix**：(N1) 核心贡献是已知组件的系统集成，novelty ceiling 有限；(N2) 发现一个引用（OntologyCL/arXiv:2510.01409）标题、副标题、3个作者名均与实际论文不符，疑似 AI hallucination
- **6 个 Should-Fix**：70B 评估过浅但 headline claim "four models"、WikiEvents fine-tuning 标注 preliminary、zero-shot 占比过大但 F1 极低、κ̄ 实用性论证不足、abstract 数值密度过高、GCD baseline 对比藏在 appendix
- **引用抽查**：10 篇中 9 篇正确，1 篇多处错误

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2"
}
```

</details>

---


## Round 33

## Round 33

24 recorded events


### User

_source line 1595 · 2026-05-22T12:40:06.239940+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注 Reviewer 1 提出的你可能遗漏的问题。

---

## Reviewer 1 — Round 1 审稿报告

**Overall**: 3.5 / 5 — Borderline Conference

### 官方维度打分

| 维度 | 分数 |
|------|------|
| Soundness | 3.5 / 5 |
| Excitement | 3 / 5 |
| Overall Assessment | 3.5 / 5 |
| Reproducibility | 4 / 5 |
| Confidence | 4 / 5 |

### Weaknesses（按严重度排序）

**W1 [critical] 缺乏与外部 constrained IE 基线的直接实验对比**
- 所有实验对比均为内部 ablation 或 post-hoc filtering 对比。Table 15-16（Appendix D）的 "Trie-Only Baseline (GCD-Equivalent)" 是自身 grammar layer 的简化版，非外部系统直接运行结果。GoLLIE、KnowCoder、CodeIE 等仅在 §6/Appendix B 有概念讨论，无相同 evaluation protocol 下的实验数据。
- 论文声称 "the first system to autonomously compile IE ontology constraints into token-level semantic masks"，但缺 head-to-head 对比。

**W2 [critical] Abstract 关于 beam search 的声明与实验数据不一致**
- Abstract 称 "beam (k=3) eliminates all violation types on SciERC"，但：(a) Table 20 仅测试 k∈{1,2,4,8}，不含 k=3；(b) "eliminates all" 仅对 Llama 成立，Qwen k=8 时 CF 仍 0.08%；(c) k=3 若为插值推断则方法论不可接受。

**W3 [major] Proposition 1 的实际相关性被高估**
- Prop 1 证明无界 entity set 下非 CF，但所有实际 schema entity type 集合有限（SciERC: 6, DocRED: 96）。有限情形下语言是 regular（DFA 可实现），只是 DFA 状态数为 O(|T|^n) 工程上不可行。这是 engineering argument 非 formal impossibility。建议添加 caveat。

**W4 [major] κ̄ 统计支撑不足 (n=3)**
- Figure 2 对 6 个数据点拟合线性模型，R²=0.886 但 p=0.138（>0.05），统计不显著。论文将 κ̄ 定位为 "descriptive metric" 但在多处作为解释变量使用。

**W5 [major] Entity registry 顺序依赖未被实验量化**
- Entity registry 递增构建，早期 type 错误传播到后续 relation 约束。论文讨论了 S1/S2 和 fallback 作为缓解机制，但无实验直接量化 entity ordering 影响。建议对比 gold/shuffled/predicted order 下的 violation rate。

**W6 [moderate] WikiEvents fine-tuning 统计效力不足**
- n=20 document，bootstrap 95% CI ±3-5 pp。F1 差异大多在 CI 范围内。abstract/introduction 引用时 preliminary qualification 不够显著。

**W7 [moderate] 70B 量化推理影响未隔离**
- AWQ INT4 quantization 改变 logit 分布，可能影响 constraint mask 有效性，无 quantized vs non-quantized 对比。

**W8 [minor] DR reduction 42-99% 范围过宽，信息量有限**
- 建议报告 median/IQR 或按数据集分别报告。

### Questions

**Q1.** GoLLIE 代码已开源，能否在 SciERC 上直接运行并报告 violation rate + F1？

**Q2.** κ̄ 在 SciERC 和 WikiEvents 上几乎相同（均 0.020），但 constraint enforcement 效果差异显著——κ̄ 作为 predictor 的解释力是否不足？

**Q3.** Grammar-first fallback rate 跨模型差异大（Qwen 0.93% vs Llama 12.02%）——哪些模型特征决定 fallback rate？

**Q4.** 对 SciERC 的 6 entity types，是否可构造等价 DFA 作为 comparison point？

**Q5.** Entity registry "first-registered-type" 语义——如果同一 entity 在不同 context 应有不同 type（如 "Python" 既可以是 Method 也可以是 OtherScientificTerm），如何处理？

### Missing References
参考文献覆盖较全面。建议补充 InstructUIE（Wang et al., 2023）的 type violation 行为讨论。

---

请对以上每个 Weakness（W1-W8）、Questions（Q1-Q5）和你认为重要的观点逐条给出 [AGREE] 或 [REBUT] 回应。

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

_source line 1596 · 2026-05-22T12:41:00.394533+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "1,5,6,7,8,27,28,33",
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
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/submitted.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "1,5,6,7,8,27,28,33",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-22T12:41:01.549954+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 508.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 570.7}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 403.4}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.4}, {\"page\": 33, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p33.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.2}], \"total_pages\": 34, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_g
…[truncated 128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-22T12:41:05.014245+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p1.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 1599 · 2026-05-22T12:41:05.518856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p27.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p27.png"
  }
}
```

</details>

---


### Tool result

_source line 1600 · 2026-05-22T12:41:06.222481+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1208
}
```

</details>

---


### Tool result

_source line 1601 · 2026-05-22T12:41:06.224142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 1602 · 2026-05-22T12:41:06.626877+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p28.png"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/review_round_18/_pdf_images/submitted_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-22T12:41:07.231212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-22T12:41:47.770621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-22T12:41:47.821356+00:00_

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
55	\input{section5_docred_draft}
56	\input{section5_crossmodel_draft}
57	\input{section5_wikievents_draft}
58	\input{section5_runtime}
59	
60	% === §6 Related Work ===
61	\input{section6_related_work}
62	
63	% === §7 Discussion and Conclusion ===
64	\section{Discussion and Conclusion}
65	\label{sec:discussion}
66	\input{section7_conclusion_compressed}
67	
68	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
69	\clearpage
70	\section*{Limitations}
71	
72	\paragraph{Constraint scope.}
73	CF impact is model-dependent: for well-calibrated models (Qwen, Llama; DR\,$\leq$\,1\% under greedy constrained decoding), S1 introduces CF violations (u
…[truncated 1889 chars]

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

_source line 1606 · 2026-05-22T12:41:51.564505+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/abstract*",
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
    "pattern": "**/abstract*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 1607 · 2026-05-22T12:41:51.665529+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex

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


### Tool call

_source line 1608 · 2026-05-22T12:41:54.929324+00:00_

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

_source line 1609 · 2026-05-22T12:41:54.980029+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
4	The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} achieves near-complete DR elimination: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $<$0.5\% true-positive loss); residual CF ($\leq$1.4\% fine-tuned; up to 12\% zero-shot) represents \emph{violation conversion}---ontologically invalid triples (DR) are replaced by individually valid but type-inconsistent ones---resolved by beam search on SciERC (\S\ref{sec:beam-results}).
7	Zero-shot evaluation serves as a diagnostic, revealing dataset- and calibration-dependent effectiveness (42--99\% DR reduction, total violation reduction 31\%; \S\ref{sec:experiments}) and characterizing constraint tightness ($\bar{\kappa}$) as a descriptive correlate ($n{=}3$ schemas).
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across four autoregressive LMs
…[truncated 156 chars]

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

_source line 1610 · 2026-05-22T12:42:01.710004+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "beam-results|beam.search|Table 20|\\\\label\\{.*beam",
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
    "pattern": "beam-results|beam.search|Table 20|\\\\label\\{.*beam",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-22T12:42:01.761002+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:552:INPUT ./appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:553:INPUT ./appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:554:INPUT ./appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:555:INPUT ./appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.fls:556:INPUT appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:2:\label{app:beam-search}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:6:Here we verify compatibility with beam search, completing coverage of the three standard decoding strategies.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:9:Two stateful components require adaptation for beam search.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:17:Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under S1 constraints across six model-dataset combinations.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:25:\label{tab:beam-search}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/
…[truncated 17658 chars]

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

_source line 1612 · 2026-05-22T12:42:37.713440+00:00_

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

_source line 1613 · 2026-05-22T12:42:37.814520+00:00_

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
17	Table~\ref{tab:beam-search} compares beam search ($k{=}4$, \texttt{early\_stopping=True}) against greedy decoding under S1 constraints across six model-dataset combinations.
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{Beam search ($k{=}4$) vs.\ greedy decoding under S1 constraints (zero-shot).
23	SciERC: 551 documents; DocRED: matched 50-document subsets (same documents for greedy and beam); full 998-doc DocRED results in Table~\ref{tab:beam-docred-998-zs}.
24	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field consistency violation rates (\%); F1 $\times$ 100.}
25	\label{t
…[truncated 13069 chars]

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
