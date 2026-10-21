# Reviewer 1 coordination — Part 2 of 5

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-1-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/84/84a449ac02ef93e8d750.json)

## Round 12

### Tool result

_source line 423 · 2026-05-19T06:24:41.203869+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-19T06:24:41.255040+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-19T06:24:41.958219+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-19T06:24:41.958750+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-19T06:24:42.009648+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-19T06:24:46.280590+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-19T06:24:47.184545+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-19T06:24:47.335581+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-19T06:24:47.637269+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-19T06:24:47.637665+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-19T06:24:48.139881+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-19T06:24:48.191850+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-19T06:24:48.192221+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec.
5	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql,ugare2024syncode,park2024grammar,beurer-kellner2024domino,jsonschemabench2025} guarantees format validity but cannot enforce cross-field semantic constraints; type-constrained code generation~\cite{synchromesh_iclr2022,scholak2021picard,pldi2025_type_constrained_codegen} compiles type systems into token-level masks but operates on static type declarations, whereas IE requires a dynamic entity registry built during generation.
6	Vocabulary-constrained IE methods~\cite{geng2023gcd,sainz2024gollie,josifoski2022genie,guidex2025,vukovic2024dore,boostcd2025} restrict which tokens can appear but not which type combinations are valid per relation; EnriCo~\cite{zaratiana2024enrico} enforces structural constraints via ASP but requires supervised training and hand-crafted rules; IterGen~\cite{ugare2025itergen} supports semantic constraints via backtracking but requires manual implementation per constraint.
7	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie,schema_rl2025} provide soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025,slot2025} validate outputs after generation.
8	OntoCoDec prevents violations during decoding, is training-free, and compiles constraints automatically from ontology schemas.
9	Recent work shows constrained decoding can degrade reasoning~\cite{banerjee2025crane,grammar_aligned_2024,schall2025hiddencost,formattax2026,dccd2026}; however, extraction tasks are robust to format constraints~\cite{tam2024letmespeak}, and OntoCoDec constrains only type tokens while leaving entity spans unconstrained.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-19T06:24:52.414607+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-19T06:24:52.818181+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints that compose losslessly with standard fine-tuning across both RE and EE: DR reaches $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp on RE (R-F1 40--46), RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types under fine-tuned decoding for calibrated models (\S\ref{sec:beam-results}).
5	Under zero-shot decoding, which stress-tests constraint robustness at R-F1 2--8\%, DR drops by 42--99\% across three models $\times$ three datasets with no significant F1 cost; constraint effectiveness holds across the full quality spectrum.
6	CF remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct resolution path.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-19T06:24:52.818580+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-19T06:24:53.473493+00:00_

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
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 30822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-19T06:24:53.625885+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-19T06:24:53.626443+00:00_

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
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-19T06:24:59.308803+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-19T06:24:59.761285+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, full S1 constraints).}
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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-19T06:24:59.761702+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-19T06:25:00.220758+00:00_

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
…[truncated 7979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-19T06:25:00.221164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-19T06:25:00.824328+00:00_

1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Grammar compilation scales sub-linearly (0.33\,s to 0.37\,s for 7$\to$1{,}000 relations); semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-19T06:25:00.874983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-19T06:25:00.925723+00:00_

1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, confirming that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-19T06:25:05.297445+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-19T06:25:05.448763+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-19T06:25:06.253583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-19T06:25:06.714040+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (E
…[truncated 967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 460
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-19T06:25:06.817965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-19T06:25:07.178791+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1448 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 360
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-19T06:25:07.229916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-19T06:25:07.282208+00:00_

1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixe
…[truncated 5951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-19T06:25:13.136789+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-19T06:25:13.690128+00:00_

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
…[truncated 19788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-19T06:25:13.690561+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "projects/schema_semantic_constrained_ie/artifacts/_project/paper",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-19T06:25:13.741747+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/projects/schema_semantic_constrained_ie/artifacts/_project/paper\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-19T06:25:17.659901+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-19T06:26:09.143348+00:00_

&lt;persisted-output>
Output too large (53.4KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/f849b54c-578b-4e3b-902c-4e1a3f3bd4f9/tool-results/toolu_01FPQiNVejopn9FDMZpjwsqN.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 65, \"total_citations\": 92, \"unique_cited_keys\": 56, \"orphan_bib\": 8, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 48, \"online_not_found\": 4, \"online_mismatch\": 12}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"shen2025slot\"], \"missing_bib\": [], \"orphan_count\": 8, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceeding
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 51483
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-19T06:26:12.962488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/f849b54c-578b-4e3b-902c-4e1a3f3bd4f9/tool-results/toolu_01FPQiNVejopn9FDMZpjwsqN.txt",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/f849b54c-578b-4e3b-902c-4e1a3f3bd4f9/tool-results/toolu_01FPQiNVejopn9FDMZpjwsqN.txt",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-19T06:26:13.266603+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 65, \"total_citations\": 92, \"unique_cited_keys\": 56, \"orphan_bib\": 8, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 48, \"online_not_found\": 4, \"online_mismatch\": 12}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"shen2025slot\"], \"missing_bib\": [], \"orphan_count\": 8, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Sche
…[truncated 52650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 304
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-19T06:29:02.993746+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 — Round 1 审稿完成（方法严谨性 + 实验设计）\n\n### 总体评分\n**Overall**: 3.5（Borderline Conference）\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Confidence**: 4/5\n\n### 一句话总结\n核心两层约束架构设计合理、实验覆盖面广、limitation 讨论诚实，但关键统计声明基于极小样本（n=4/6）、EE composability 验证仅 20 篇 test set、缺少与 schema-aware IE baseline 的直接对比。\n\n### Must-Fix（2 条）\n**W1** dual-factor pattern R²=0.886 基于 n=4（p≈0.058 不显著），Spearman ρ=-0.77 基于 n=6（临界值~0.886），正文用词\"predicts\"过强。需降级措辞或增加数据点。\n\n**W2** WikiEvents fine-tuning composability test set 仅 20 篇，trigger F1 shift -5.4pp 可能纯粹是噪声，但支撑了 Abstract/Contribution 中的 EE composability claim。需报告 CI/p-value 并说明为何不用更大 test set。\n\n### Should-Fix（5 条）\n**W3** 无 schema-aware IE baseline（GoLLIE/KnowCoder/BoostCD/GCD）的实验对比。\n**W4** Abstract \"DR drops by 42-99%\" 可能误导——42% 对应 Mistral DocRED 仍残留 33% violation。\n**W5** EE fine-tuned CF 率未报告。\n**W6** DocRED beam search 仅 50 doc 子集。\n**W7** 约束表基于频率统计而非完整 ontology schema 导致不可消除的 coverage gap，需解释原因。\n\n### Minor（2 条）\n**W8** bib 有 8 个 orphan 条目（实为 duplicate keys）。\n**W9** Limitations section 需分条/分段提高可读性。\n\n### 主要优势\n清晰的问题定义和形式化；pair-based enforcement 的非矩形分析有说服力；跨模型×跨任务×跨规模验证覆盖面广；CF trade-off 的诚实讨论和 beam search 缓解路径。\n\n完整审稿意见已在本 session 中输出。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 — Round 1 审稿完成（方法严谨性 + 实验设计）\n\n### 总体评分\n**Overall**: 3.5（Borderline Conference）\n**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Confidence**: 4/5\n\n### 一句话总结\n核心两层约束架构设计合理、实验覆盖面广、limitation 讨论诚实，但关键统计声明基于极小样本（n=4/6）、EE composability 验证仅 20 篇 test set、缺少与 schema-aware IE baseline 的直接对比。\n\n### Must-Fix（2 条）\n**W1** dual-factor pattern R²=0.886 基于 n=4（p≈0.058 不显著），Spearman ρ=-0.77 基于 n=6（临界值~0.886），正文用词\"predicts\"过强。需降级措辞或增加数据点。\n\n**W2** WikiEvents fine-tuning composability test set 仅 20 篇，trigger F1 shift -5.4pp 可能纯粹是噪声，但支撑了 Abstract/Contribution 中的 EE composability claim。需报告 CI/p-value 并说明为何不用更大 test set。\n\n### Should-Fix（5 条）\n**W3** 无 schema-aware IE baseline（GoLLIE/KnowCoder/BoostCD/GCD）的实验对比。\n**W4** Abstract \"DR drops by 42-99%\" 可能误导——42% 对应 Mistral DocRED 仍残留 33% violation。\n**W5** EE fine-tuned CF 率未报告。\n**W6** DocRED beam search 仅 50 doc 子集。\n**W7** 约束表基于频率统计而非完整 ontology schema 导致不可消除的 coverage gap，需解释原因。\n\n### Minor（2 条）\n**W8** bib 有 8 个 orphan 条目（实为 duplicate keys）。\n**W9** Limitations section 需分条/分段提高可读性。\n\n### 主要优势\n清晰的问题定义和形式化；pair-based enforcement 的非矩形分析有说服力；跨模型×跨任务×跨规模验证覆盖面广；CF trade-off 的诚实讨论和 beam search 缓解路径。\n\n完整审稿意见已在本 session 中输出。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-19T06:29:07.019144+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4025
}
```

</details>

---


### Assistant

_source line 468 · 2026-05-19T06:29:13.844597+00:00_

审稿完成，已汇报 Director。

总结：给出 **3.5（Borderline Conference）** 评分。核心方法（两层约束编译 + pair-based sequential masking）设计正确、实验覆盖面广。两个 Must-Fix 问题：(1) dual-factor 和 Spearman 统计声明基于 n=4/6 样本不显著但正文措辞过强；(2) WikiEvents FT composability 仅 20 篇 test set 统计效力不足。五个 Should-Fix 包括缺少 schema-aware IE baseline 对比、Abstract 数字可能误导、EE fine-tuned CF 未报告等。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

8 recorded events


### User

_source line 469 · 2026-05-19T06:31:35.321158+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应，对每条 Weakness 标注 [AGREE] 或 [REBUT]，并给出理由。如果你同意，说明为什么；如果你反驳，请引用论文中的具体 Section/Table/Figure 作为证据。

---

### Reviewer 2 审稿意见原文

**Overall: 3.5（Borderline Conference）| Soundness 4/5 | Excitement 3/5 | Reproducibility 5/5**

**Summary**: 本文提出 OntoCoDec，将 IE ontology schema 编译为两层 token-level 解码约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上跨 4 个模型评估，zero-shot DR 降低 42-99%，与 LoRA 组合后 DR ≤ 0.20% 且 R-F1 波动 < 0.6pp。实验全面但核心技术新颖性有限（code domain 类型约束解码的迁移），CF trade-off 削弱 zero-shot 故事。

**Strengths**:
- S1: 问题定义清晰，violation 分类体系完整
- S2: Enabling dependency 有实验支撑（semantic-only 24% vs full 94%）
- S3: Fine-tuning composability 是最强贡献（DR ≤0.20%, F1 neutral）
- S4: 实验覆盖面异常全面（3 datasets × 4 models × 多 decoding strategies）
- S5: Limitations 处理诚实透明
- S6: 可复现性极佳

**Weaknesses**:

**W1 [Should-Fix]** 核心技术相对 code domain type-constrained decoding 的增量贡献有限。核心机制（类型约束→token masks）在 PICARD、Synchromesh、MGD、Mündler et al. (PLDI 2025) 已充分验证。IE 特有贡献（dynamic entity registry, pair-based sequential masking）属于适配而非根本性算法创新。"Enabling dependency" 本质上是一个 obvious 的架构设计选择。

**W2 [Should-Fix]** Constraint tightness (κ) 分析价值被高估。κ 是直接归一化，dual-factor 拟合仅 n=4 (p≈0.058)，但 Contribution #1 用 causal language "driven by"。SciERC/DocRED DR 相近（15.37% vs 18.46%）可能是巧合。

**W3 [Should-Fix]** Zero-shot framing 与实际价值不一致。论文最强结果（fine-tuning composability）被埋在 zero-shot 分析之后。Zero-shot 下 total violation burden (DR+CF) 从 15.45% 降到 10.83%（SciERC），净减少仅 ~30%。

**W4 [Should-Fix]** Appendix Extended Related Work 中 AI 写作痕迹密集（-ing 分词短语 10+ 次，", confirming" 14 次）。

**W5 [Should-Fix]** WikiEvents fine-tuning 评估仅 20 文档。

**W6 [Should-Fix]** Abstract 数字堆砌（~15 个数字），信息密度过高。

**W7 [Minor]** Contribution #3 和 #4 高度重叠，可合并。

**W8 [Minor]** Table 3 Grammar-only 行 R-F1/E-F1 标粗叙事矛盾。

**W9 [Minor]** DocRED beam search 仅 50 文档子集。

**Questions**:
- Q1: CF↔DR total violation burden 净变化？Pareto 分析？
- Q2: WikiEvents FT 为什么只 20 文档？
- Q3: 能否 single integrated layer 避免 enabling dependency？
- Q4: WikiEvents 的 κ 值和预测力？
- Q5: 完整 ontology schema vs frequency-based 约束表能否消除 coverage gap？

**Missing References**: Hokamp & Liu (2017), DEGREE (Hsu et al., 2022), Roth & Yih (2004) 移入正文。

---

请逐条回应每个 Weakness（W1-W9），对每条标注 **[AGREE]** 或 **[REBUT]**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-19T06:32:16.823725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex",
  "limit": "32"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex",
    "limit": "32"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-19T06:32:17.426914+00:00_

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
…[truncated 2586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-19T06:32:17.477884+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-19T06:32:17.528989+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-19T06:33:42.149128+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条回应\n\n### 逐条回应\n\n**[AGREE] R2-W1 (novelty)**: 核心 type→mask 范式确实源自 code domain。IE adaptations (dynamic registry, pair-based masking) 是真实工程挑战但非算法创新。不过，enabling dependency 的 ablation 定量拆解（semantic-only 24% vs full 94%, Table 1）有独立价值，\"obvious\" 稍过强。总体 novelty 是本文相对弱项。\n\n**[AGREE] R2-W2 (κ overvalued)**: 与我的 W1 一致。\"driven by\" 是因果性语言，n=4 不足以支撑。补充：baseline DR 相近但 residual DR 差异极大（0.93% vs 10.21%），论文未充分区分这两者的驱动因素。\n\n**[REBUT] R2-W3 (zero-shot framing)**: DR+CF 简单相加低估了 DR 消除的价值——§4 明确区分 DR（triple 不可用）和 CF（individually valid, globally inconsistent）。但叙事结构确实将最强结果（fine-tuning composability）埋在 zero-shot 之后，presentation 批评合理。\n\n**[AGREE] R2-W4 (AI writing traces)**: 未在初审逐句检查，R2 的观察（\", confirming\" 14次等）与写作规范冲突。附录也在 ARR 审稿范围内，需系统清理。\n\n**[AGREE] R2-W5 (WikiEvents 20 docs)**: 与我的 W2 完全一致。核心共识点。\n\n**[REBUT] R2-W6 (Abstract 数字堆砌)**: 作为量化约束消除论文，violation rate 数字不可避免。问题在于叙事结构（同时覆盖 4 条线）而非数字本身。建议聚焦 fine-tuning composability，beam/EE 细节留给 Introduction。\n\n**[AGREE] R2-W7 (Contribution overlap)**: #3 和 #4 确有重叠，建议重新划分边界。\n\n**[REBUT] R2-W8 (Table 3 bolding)**: 标粗规则在 caption 中有声明（\"best per column\"），factually correct。但 visual communication 确实可能误导，属 minor presentation issue。\n\n**[AGREE] R2-W9 (DocRED beam 50 docs)**: 与我的 W6 一致。核心共识点。\n\n### 两位 Reviewer 共识点\n1. WikiEvents FT 20 docs 样本量不足（R1-W2, R2-W5）\n2. Dual-factor n=4 统计声明过强（R1-W1, R2-W2）\n3. DocRED beam search 仅 50 docs（R1-W6, R2-W9）\n4. 缺少 schema-aware IE baseline（R1-W3, R2 未直接提但 Q3/Q5 暗示）\n\n### 两位 Reviewer 分歧点\n1. Zero-shot DR+CF 净变化的解读（R2 认为仅 30% 减少，R1 认为 DR/CF 不等权）\n2. Abstract 数字密度（R2 认为堆砌，R1 认为问题在叙事结构不在数字数量）\n3. Novelty 严重程度（R2 列为 Should-Fix，R1 认为是相对弱项但 ablation 有独立价值）",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条回应\n\n### 逐条回应\n\n**[AGREE] R2-W1 (novelty)**: 核心 type→mask 范式确实源自 code domain。IE adaptations (dynamic registry, pair-based masking) 是真实工程挑战但非算法创新。不过，enabling dependency 的 ablation 定量拆解（semantic-only 24% vs full 94%, Table 1）有独立价值，\"obvious\" 稍过强。总体 novelty 是本文相对弱项。\n\n**[AGREE] R2-W2 (κ overvalued)**: 与我的 W1 一致。\"driven by\" 是因果性语言，n=4 不足以支撑。补充：baseline DR 相近但 residual DR 差异极大（0.93% vs 10.21%），论文未充分区分这两者的驱动因素。\n\n**[REBUT] R2-W3 (zero-shot framing)**: DR+CF 简单相加低估了 DR 消除的价值——§4 明确区分 DR（triple 不可用）和 CF（individually valid, globally inconsistent）。但叙事结构确实将最强结果（fine-tuning composability）埋在 zero-shot 之后，presentation 批评合理。\n\n**[AGREE] R2-W4 (AI writing traces)**: 未在初审逐句检查，R2 的观察（\", confirming\" 14次等）与写作规范冲突。附录也在 ARR 审稿范围内，需系统清理。\n\n**[AGREE] R2-W5 (WikiEvents 20 docs)**: 与我的 W2 完全一致。核心共识点。\n\n**[REBUT] R2-W6 (Abstract 数字堆砌)**: 作为量化约束消除论文，violation rate 数字不可避免。问题在于叙事结构（同时覆盖 4 条线）而非数字本身。建议聚焦 fine-tuning composability，beam/EE 细节留给 Introduction。\n\n**[AGREE] R2-W7 (Contribution overlap)**: #3 和 #4 确有重叠，建议重新划分边界。\n\n**[REBUT] R2-W8 (Table 3 bolding)**: 标粗规则在 caption 中有声明（\"best per column\"），factually correct。但 visual communication 确实可能误导，属 minor presentation issue。\n\n**[AGREE] R2-W9 (DocRED beam 50 docs)**: 与我的 W6 一致。核心共识点。\n\n### 两位 Reviewer 共识点\n1. WikiEvents FT 20 docs 样本量不足（R1-W2, R2-W5）\n2. Dual-factor n=4 统计声明过强（R1-W1, R2-W2）\n3. DocRED beam search 仅 50 docs（R1-W6, R2-W9）\n4. 缺少 schema-aware IE baseline（R1-W3, R2 未直接提但 Q3/Q5 暗示）\n\n### 两位 Reviewer 分歧点\n1. Zero-shot DR+CF 净变化的解读（R2 认为仅 30% 减少，R1 认为 DR/CF 不等权）\n2. Abstract 数字密度（R2 认为堆砌，R1 认为问题在叙事结构不在数字数量）\n3. Novelty 严重程度（R2 列为 Should-Fix，R1 认为是相对弱项但 ablation 有独立价值）",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-19T06:33:46.622927+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4473
}
```

</details>

---


### Assistant

_source line 476 · 2026-05-19T06:33:52.902526+00:00_

交叉回应已完成并汇报 Director。

总结：9 条中 **5 条 AGREE**（W1 novelty, W2 κ overvalued, W4 AI writing, W5 WikiEvents 20 docs, W7 contribution overlap, W9 DocRED beam 50 docs），**3 条 REBUT**（W3 zero-shot framing—DR/CF 不等权, W6 Abstract—问题在叙事结构非数字数量, W8 Table 3 bolding—规则在 caption 中有声明），W9 也 AGREE。两位 reviewer 的核心共识集中在 WikiEvents 样本量、dual-factor 统计效力、DocRED beam 子集大小三个问题上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

76 recorded events


### User

_source line 477 · 2026-05-19T07:08:11.378883+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

**你的审查侧重：方法严谨性 + 实验设计与完整性 + 可复现性**

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **目标 venue**: EMNLP 2026 (ARR May 2026 cycle)
- **截止日期**: 2026-05-25
- **论文路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **论文目录**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/`

### Venue 格式要求
- Long paper: 8 页正文 + unlimited references + Limitations section（不计页数）
- 模板: ACL style (`\usepackage[review]{acl}`)
- 匿名规则: Double-blind
- 附录: double-column format
- 必须包含: Limitations section, Responsible NLP Research Checklist
- EMNLP 2026 评分标准: 5=Consider for Award, 4.5=Borderline Award, 4=Conference（主会议接收）, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

### 你的审查重点

请按以下维度深入评估：

1. **方法严谨性**
   - 核心方法（编译 ontology 约束 → constrained decoding）的技术正确性
   - 约束组合（grammar + semantic constraints）的理论基础是否充分
   - 方法假设是否明确列出，是否合理
   - 是否存在方法论上的漏洞或循环论证

2. **实验设计与完整性**
   - 数据集选择（SciERC, DocRED, WikiEvents）是否足够、有代表性
   - Baseline 对比是否公平、充分（是否缺少关键 baseline）
   - 消融实验是否充分揭示各组件贡献
   - 统计显著性：关键 claim 是否有充分统计支持（sample size, confidence intervals, p-values）
   - Zero-shot vs fine-tuned 实验设计的合理性
   - 负面结果的处理是否诚实
   - 每个 claim 是否有对应的实验证据支撑

3. **可复现性**
   - 方法描述是否足够详细，能否独立复现
   - 超参数、训练细节、评测流程是否完整
   - 代码/数据承诺是否明确

### 输出格式

请按 ACL/ARR 标准审稿格式输出：
- **Summary**: 2-3 句论文概述
- **Strengths**: 优点逐条列出（S1, S2, ...）
- **Weaknesses**: 缺点逐条列出（W1, W2, ...），区分 Must-Fix / Should-Fix / Minor
- **Questions**: 需要作者回答的问题（Q1, Q2, ...）
- **Missing References**: 遗漏的重要相关工作
- **Overall Assessment**: 评分（使用 EMNLP 2026 评分标准 1-5）+ 置信度（1-5）+ 简要理由
- **Detailed Comments**: 逐节详细意见（§1-§7 + Limitations + Appendix）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-19T07:08:20.333903+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-19T07:08:20.786212+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_1_11179fb2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-19T07:08:20.937240+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-19T07:08:20.987929+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/fig2_per_relation_dr.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/dual_factor_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_g
…[truncated 5669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-19T07:08:24.405106+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-19T07:08:24.456576+00:00_

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
67	\paragraph{Constraint scope.}
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation sh
…[truncated 4385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-19T07:08:27.772846+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-19T07:08:28.690074+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints:
3	(1)~a \emph{grammar layer} (XGrammar) that guarantees JSON structural validity and vocabulary membership; and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist even after fine-tuning; violation rates correlate with \emph{constraint tightness} rather than ontology or model scale.
6	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} reduces DR to $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp of unconstrained baselines: near-lossless composability at deployment-grade extraction quality.
7	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
8	Under zero-shot decoding, DR drops by 76--99\% for calibrated models (Qwen3-8B, Llama-3.1-8B); Mistral-7B, a boundary condition, shows 42\% reduction.
9	Beam search ($k{=}4$) with LoRA eliminates all four violation types on SciERC (both Qwen3-8B and Llama-3.1-8B).
10	The framework generalizes to event extraction on WikiEvents (56 event types, 80 roles) without modification, eliminating vocabulary violations ($\to$\,0\%); fine-tuning composability extends to EE (preliminary, 20-document test set).
11	Per-slot enforcement introduces a cross-field consistency trade-off (resolved to $\leq$1.2\% by fine-tuning on both RE and EE).
12	OntoCoDec composes losslessly with standard fine-tuning across four models (8B--70B), three tokenizer families, and three IE tasks.
13	\end{abstract}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 917
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-19T07:08:28.744694+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-19T07:08:29.266196+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Constraint enforcement matters most at deployment-grade quality (R-F1 40--46\%): at this level, residual type violations propagate directly into knowledge graphs and decision-support pipelines; reliable type-safety enforcement is needed.
10	
11	Existing approaches leave a fundamental gap.
12	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
13	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
14	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
15	OntoCoDec preserves recall by enforcing constraints during generation rather than discarding non-compliant outputs.
16	Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance tha
…[truncated 2561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 521
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-19T07:08:29.266709+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-19T07:08:29.520053+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 253
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-19T07:08:29.520549+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-19T07:08:29.571210+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-19T07:08:34.349130+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-19T07:08:35.305445+00:00_

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
…[truncated 1385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-19T07:08:35.406658+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-19T07:08:35.809558+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two complementary regimes.
8	Fine-tuning composability (\S\ref{sec:composability}) tests whether constraints compose losslessly with standard training at deployment-grade quality (R-F1 40--46).
9	Zero-shot evaluation stress-tests constraint robustness when the model has no task-specific supervision (R-F1 2--8).
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-19T07:08:35.810415+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-19T07:08:36.414095+00:00_

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
…[truncated 5095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-19T07:08:36.464903+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-19T07:08:36.465422+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-19T07:08:41.049355+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-19T07:08:41.853581+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-19T07:08:42.004765+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-19T07:08:42.407652+00:00_

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
…[truncated 2360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-19T07:08:42.558861+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-19T07:08:42.810319+00:00_

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
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models (Qwen, Llama) and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Model scale reduces
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-19T07:08:42.861737+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-19T07:08:42.912488+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec.
5	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql,ugare2024syncode,park2024grammar,beurer-kellner2024domino,jsonschemabench2025} guarantees format validity but cannot enforce cross-field semantic constraints; type-constrained code generation~\cite{synchromesh_iclr2022,scholak2021picard,pldi2025_type_constrained_codegen} compiles type systems into token-level masks but operates on static type declarations, whereas IE requires a dynamic entity registry built during generation.
6	Vocabulary-constrained IE methods~\cite{geng2023gcd,sainz2024gollie,josifoski2022genie,guidex2025,vukovic2024dore,boostcd2025} restrict which tokens can appear but not which type combinations are valid per relation; EnriCo~\cite{zaratiana2024enrico} enforces structural constraints via ASP but requires supervised training and hand-crafted rules; IterGen~\cite{ugare2025itergen} supports semantic constraints via backtracking but requires manual implementation per constraint.
7	Training-based methods~\cite{paolini2021tanl,cabot2021rebel,lu2022uie,knowcoder_acl2024,li2023codeie,schema_rl2025} provide soft guidance; post-hoc approaches~\cite{khorshidi2025odke,spires_2024,ontologx_2025,slot2025} validate outputs after generation.
8	OntoCoDec prevents violations during decoding, is training-free, and compiles constraints automatically from ontology schemas.
9	\citet{roth_yih_2004} first introduced hard type constraints in IE via integer linear programming for global inference; OntoCoDec achieves analogous type enforcement within autoregressive decoding.
10	Schema-aware training methods~\cite{sainz2024gollie,knowcoder_acl2024} internalize type constraints via training; OntoCoDec enforces them at decoding time without retraining, and the two approaches are complementary.
11	Recent work shows constrained decodi
…[truncated 283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-19T07:08:47.339327+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-19T07:08:48.151884+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints that compose losslessly with standard fine-tuning across both RE and EE: DR reaches $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp on RE (R-F1 40--46), RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types under fine-tuned decoding for calibrated models (\S\ref{sec:beam-results}).
5	Under zero-shot decoding, which stress-tests constraint robustness at R-F1 2--8\%, DR drops by 42--99\% across three models $\times$ three datasets with no significant F1 cost; constraint effectiveness holds across the full quality spectrum.
6	CF remains an open challenge for per-slot enforcement; global entity-level type consensus during decoding offers the most direct resolution path.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 812
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-19T07:08:48.252920+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 511 · 2026-05-19T07:08:48.655435+00:00_

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
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-19T07:08:48.656015+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 513 · 2026-05-19T07:08:49.009101+00:00_

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
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 31971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-19T07:08:49.060163+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-19T07:08:49.112223+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-19T07:08:53.850667+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-19T07:08:54.303092+00:00_

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
…[truncated 19750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-19T07:08:54.303580+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-19T07:08:55.258324+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, full S1 constraints).}
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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-19T07:08:55.409441+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-19T07:08:55.610967+00:00_

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
…[truncated 8172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-19T07:08:55.661912+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-19T07:08:55.712742+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, which indicates stronger baseline vocabulary compliance.
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
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-19T07:09:00.242515+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-19T07:09:00.696418+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-19T07:09:00.797203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-19T07:09:01.651670+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (E
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-19T07:09:01.652197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-19T07:09:01.953639+00:00_

1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixe
…[truncated 5952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-19T07:09:01.954077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-19T07:09:02.004571+00:00_

1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Grammar compilation scales sub-linearly (0.33\,s to 0.37\,s for 7$\to$1{,}000 relations); semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-19T07:09:06.281115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-19T07:09:06.281648+00:00_

1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, which confirms that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-19T07:09:14.043875+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 535 · 2026-05-19T07:09:14.094593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-19T07:09:17.265369+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"
  }
}
```

</details>

---


### Tool call

_source line 537 · 2026-05-19T07:09:17.567895+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR review form overall assessment soundness excitement reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR review form overall assessment soundness excitement reproducibility"
  }
}
```

</details>

---


### Tool result

_source line 538 · 2026-05-19T07:09:25.739330+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2025-2026 reviewer guidelines:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Subjective preferences about whether work is interesting should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Area Chair Recommendations
The ARR metareview score has changed in February 2025 to be more aligned 
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8473
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-19T07:09:25.790272+00:00_

Web search results for query: "EMNLP 2026 ARR review form overall assessment soundness excitement reproducibility"

Links: [{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"TrustNLP","url":"https://trustnlpworkshop.github.io/"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ConfReady: A RAG based Assistant and Dataset for Conference Checklist Responses","url":"https://arxiv.org/pdf/2408.04675"}]

Based on the search results, here's what I found about the EMNLP 2026 ARR review form:

## ARR Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement
You may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

### Overall Assessment
The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact.

### Reproducib
…[truncated 269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8222
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-19T07:09:28.809005+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclrollingreview.org reviewform review form 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclrollingreview.org reviewform review form 2025"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-19T07:09:35.045393+00:00_

Web search results for query: "site:aclrollingreview.org reviewform review form 2025"

Links: [{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Forms","url":"https://aclrollingreview.org/reviewforms/"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found search results for your query. The search returned information about the ACL Rolling Review platform and its review form. Here are the key findings:

The first result directly addresses your search—the Review Form page at aclrollingreview.org/reviewform, which discusses the ACL code of ethics and instructions for reviewing papers, including guidance on identifying ethical issues and the extent to which they have been acknowledged or addressed by the authors.

Additionally
…[truncated 474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6236
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-19T07:09:39.121900+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 543 · 2026-05-19T07:09:39.373064+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 544 · 2026-05-19T07:09:43.696669+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any additional fields reviewers must fill in. I need the exact scoring criteria for soundness, excitement, overall assessment, reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), descriptions of each score level, and any additional fields reviewers must fill in. I need the exact scoring criteria for soundness, excitement, overall assessment, reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 545 · 2026-05-19T07:09:44.801902+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what dimensions reviewers should evaluate, scoring scales, definitions of each score level for soundness/excitement/overall assessment/reproducibility, and any specific instructions about how to weigh different aspects of a paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines: what dimensions reviewers should evaluate, scoring scales, definitions of each score level for soundness/excitement/overall assessment/reproducibility, and any specific instructions about how to weigh different aspects of a paper."
  }
}
```

</details>

---


### Tool result

_source line 546 · 2026-05-19T07:09:50.187547+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Scoring Dimensions

**Soundness** (1-5 scale)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some main claims not sufficiently supported"
- 1: "Major Issues: not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper"
- 2: "Potentially Interesting: does not resonate with me"
- 1: "Not Exciting: does not resonate with me"

**Overall Assessment** (1-5 scale)
- 5: Consider for Award (top 2.5% papers)
- 4: Conference acceptance recommendation
- 3: Findings track acceptance
- 2: Resubmit next cycle (substantial revisions needed)
- 1: Do not resubmit

**Reviewer Confidence** (1-5 scale)
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" but conceivable something was missed
- 3: "Pretty sure, but there's a chance I missed something"
- 2: Likely missed details or uncertain about novelty
- 1: "Not my area, or paper is very hard to understand"

## Additional Required Fields

- **Reproducibility** (1-5): Assessment of detail sufficiency
- **Datasets** (1-5): Value of released datasets
- **Software** (1-5): Value of released software
- **Author Identity Knowledge** (1-5): Anonymity status

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6490
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-19T07:09:52.501935+00:00_

# ARR Reviewer Guidelines: Evaluation Dimensions and Scoring

## Evaluation Dimensions

Reviewers assess papers across these primary dimensions:

1. **Soundness** - Technical correctness and validity of methodology
2. **Excitement** - Personal interest and perceived significance
3. **Overall Assessment** - Final recommendation for acceptance
4. **Reproducibility** - Sufficiency of details for replicating experiments

## Scoring Scales

The guidelines specify that reviewers provide "three scores: soundness, excitement, and overall recommendation" starting February 2025, though specific numerical scales aren't detailed in the document. The overall assessment represents "an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue."

## Score Level Definitions

**Soundness**: Papers must demonstrate technical validity. Low soundness scores "must be justified by the text of the review." If technical flaws aren't identified, the review lacks credibility. The guideline emphasizes that reviewers should verify their low scores reflect genuine methodological problems rather than unconscious bias.

**Excitement**: This score reflects "our personal taste" and remains "orthogonal to the assessment of the soundness of the paper." A reviewer may find work sound yet personally uninteresting—these should register as separate evaluations.

**Overall Assessment**: This composite score balances "soundness, excitement, and also other factors like novelty and impact." Critically, "all papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," though excitement isn't mandatory for acceptance.

**Reproducibility**: Low reproducibility scores require justification, typically addressing whether "enough details/code is provided for reproducibility."

## Weighting Instructions

The guidelines discourage treating limitations as automatic weaknesses. They emphasize that "a paper only needs to present sufficien
…[truncated 279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7700
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-19T07:11:02.227289+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 549 · 2026-05-19T07:11:02.227918+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-19T07:13:58.474060+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计与完整性 + 可复现性\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，将 IE ontology schema 编译为两层可组合的 token-level 解码约束：(1) grammar layer (XGrammar) 保证 JSON 结构合法性和词汇成员资格；(2) semantic layer 通过有状态实体注册表和动态 logit masking 执行 per-triple domain/range 类型约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上评估，覆盖 4 个模型（8B-70B）、3 种 tokenizer 族、zero-shot 和 LoRA fine-tuning 两种 regime。核心结果：fine-tuning 组合下 DR ≤ 0.20%、R-F1 ±0.6pp；zero-shot 下 DR 降低 42-99%。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 核心两层组合机制技术正确，但 CF 副作用是结构性缺陷（非可修复 bug），constraint table 来源于训练数据而非形式本体削弱了核心 claim，部分统计证据不足 |\n| Excitement | 3/5 (Interesting) | 问题定义清晰，violation taxonomy 有用，enabling dependency 洞察有趣；但实际收益受限于 CF trade-off 和 post-hoc filtering 在多数 setting 下 F1 更高 |\n| Reproducibility | 4/5 | 超参数、prompt、硬件、评估协议描述详尽；代码承诺 acceptance 后发布但当前不可用 |\n| Overall Assessment | **3.0 (Findings)** | 扎实的技术贡献和充分的实验覆盖，但 CF trade-off、constraint table 来源问题、缺少关键 baseline 阻止 Conference 推荐 |\n| Confidence | 4/5 | 对 constrained decoding 和 IE 领域较为熟悉 |\n\n---\n\n## Strengths\n\n**S1. 问题定义清晰，violation taxonomy 系统化。** §2 对 IE ontology 的形式化定义（$\\mathcal{O} = (\\mathcal{E}, \\mathcal{R}, \\sigma)$）和四类 violation（DR/RV/ET/CF）的分类是干净的，constraint tightness（Eq. 2）作为预测 violation 难度的指标有独立分析价值。\n\n**S2. 两层组合架构设计合理，enabling dependency 洞察有价值。** Table 1 ablation 清楚展示 semantic-only 仅降低 24% DR（因缺乏词汇保证），而 grammar+semantic 组合降低 94%。这一 enabling dependency 不是 trivial 的，值得报告。Sequential masking 对 non-rectangular type signatures 的必要性分析（§4, footnote 1: 独立检查会多放 33-37% spurious pairs）是严谨的。\n\n**S3. 实验覆盖面广。** 3 数据集 × 4 模型 × 2 regime（zero-shot/fine-tuned）× 3 解码策略（greedy/sampling/beam）× 3 prompt 变体 × 3 文档长度分层，加上 full FT baseline、scalability benchmark。附录覆盖了大部分可预见的 reviewer 质疑点。\n\n**S4. Fine-tuning composability 结果实用。** Table 2 和 Appendix B Table 5 展示 LoRA+S1 在 4 个 model×dataset 设置下 DR ≤ 0.20%、R-F1 ±0.6pp，这是有部署价值的。beam search 进一步消除所有四类 violation（SciERC, 两个 calibrated models），是一个令人印象深刻的结果。\n\n**S5. 工程开销低。** +2-13% inference overhead、sub-second compilation、constant overhead up to 1,000 relations（Appendix L）使方法在实际部署中可行。\n\n**S6. 诚实讨论局限。** CF trade-off 的分析（Appendix B Table 4, Spearman ρ=-0.77）和 Mistral boundary condition 的处理是坦诚的，优于许多同类论文。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [critical] Constraint table 来源于训练数据，非形式本体，与标题/framing 不符。**\n- 具体位置：§5 Setup（\"RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology)\"）\n- 问题：论文标题为 \"Compiled Ontology Constraints\"，Abstract 和 Introduction 反复使用 \"ontology schema\" 一词。但对于 SciERC 和 DocRED（论文的两个主要 RE 数据集），约束表是从训练集共现统计中提取的，而非正式本体。这导致：(a) 约束表不完整——Appendix B 残留 DR error analysis 显示 33% 的残留 violation 源于 \"schema coverage gaps\"；(b) 约束的质量取决于训练集的统计特性，而非领域知识；(c) 论文没有报告约束表的覆盖率（训练集 type pairs 覆盖测试集 type pairs 的比例）。只有 WikiEvents 使用了真正的形式本体（KAIROS），但 WikiEvents 结果被标记为 \"preliminary\"（20 文档测试集）。\n- 为什么影响接收：这是 framing integrity 问题。论文的核心叙事——\"编译本体约束\"——在其主要实验中并不成立。\n- 建议修改方向：(1) 明确区分 \"formal ontology constraints\"（WikiEvents）和 \"empirical type-pair constraints\"（SciERC/DocRED），在标题或 Introduction 中体现；(2) 报告 constraint table 的覆盖率和 test set 中 unseen type pairs 的比例；(3) 分析 constraint table completeness 对方法效果的敏感性。\n\n**W2 [critical] CF 副作用严重且为结构性问题，削弱核心贡献。**\n- 具体位置：Table 1（CF 0.08% → 9.90%）、Table 3（CF up to 12.02%）、Table 4（CF 15-21% on WikiEvents）、Appendix B Table 4（CF fallback ablation）\n- 问题：OntoCoDec 在解决 DR 的同时引入了新的 violation 类型 CF，zero-shot 下可达 12.02%（Llama DocRED）和 21.1%（Qwen WikiEvents）。Appendix B 的 CF-DR trade-off ablation 证实这是结构性的：消除 CF 会将 violation re-route 到 DR（+13.85pp），总 violation 反而增加。这意味着：(a) 论文的核心 claim——\"减少 type violations\"——需要附加条件：减少 DR 的代价是增加 CF；(b) zero-shot 下 total type-violation burden（DR+CF）从 15.45% 降至 10.83%（SciERC），降幅仅 30%，远不如 \"94% DR reduction\" 的 headline number 暗示的效果；(c) fine-tuning 将 CF 降至 ~1%，但这意味着 OntoCoDec 只在与 fine-tuning 组合时真正有效，与 \"training-free\" 的定位有张力。\n- 为什么影响接收：核心 claim 的表述方式（\"DR ↓94%\"）遮蔽了 total violation 的真实变化。审稿人需要确认 headline number 不具误导性。\n- 建议修改方向：(1) 在 Abstract 和 Introduction 中报告 total type-violation burden 的变化（DR+CF），而非仅报告 DR；(2) 明确 \"training-free\" 的适用范围——zero-shot 下 CF 严重，方法的实际价值主要在 fine-tuning 组合场景；(3) 考虑将 total violation reduction 作为主指标。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W3 [warning] 缺少关键 baseline 对比。**\n- 具体位置：§6 Related Work, §5 Experiments\n- 问题：Related Work 讨论了多种 constrained IE 方法（GoLLIE、GenIE、EnriCo、GCD），但实验中唯一的 baseline 是 post-hoc filtering。缺少：(a) GoLLIE（schema-as-code, 同样 address type compliance）；(b) EnriCo（ASP constraints at decode time, 最直接的 constrained decoding for IE 对比）；(c) GCD（grammar-constrained decoding for IE, 论文自己称其为 \"closest precursor\"）。Post-hoc filtering 在 5/6 zero-shot settings 下 F1 更高（Appendix B Table 8），这使得 OntoCoDec 在 zero-shot 场景的实际优势不明确。\n- 建议：至少与 GCD 做实验对比（论文已实现 grammar-only 行，但 GCD 还有 input-dependent grammar 功能），或者说明为什么 GoLLIE/EnriCo 不可比（如需要 training 或 domain-specific rules）。\n\n**W4 [warning] 多个关键实验的样本量不足，统计可信度存疑。**\n- 具体位置：Appendix B（dual-factor: n=4, p≈0.058）、Appendix D（sampling: DocRED 114/998 docs）、§5.4（WikiEvents FT: 20 docs）、Appendix F（beam DocRED: 50 docs）\n- 问题：(a) Dual-factor 线性拟合 R²=0.886 但 n=4, df=2, p≈0.058——论文承认是 \"descriptive characterization\" 但仍构建了围绕 \"dual-factor pattern\" 的叙事（§4, §5.3）；(b) DocRED sampling 仅 114/998 documents（原因：\"~300h due to extended generation\"），但 CF 从 2.57% 跳至 12.63%，这个差异是否由小样本噪声驱动？(c) WikiEvents FT composability 仅 20 documents，bootstrap CI 极宽（如 RoV [0%, 1.73%]），trigger F1 变化为 -5.4pp，confidence interval 在此样本量下是否可信？(d) Beam search DocRED 仅 50 documents——Clopper-Pearson 95% CI upper bound 5.8% 并不能强有力地支持 \"eliminates DR\"。\n- 建议：(a) 降低 dual-factor pattern 在主文叙事中的比重，或增加数据点（更多 model×dataset 配置）；(b) 对小样本实验明确标注置信区间并在 claim 中使用 hedging language；(c) WikiEvents 和 beam search DocRED 实验应在条件允许时扩展样本量。\n\n**W5 [warning] Zero-shot R-F1 过低（2-8%），该 regime 下的 violation rate 分析对实际部署的指导意义有限。**\n- 具体位置：§5 全节、Appendix B \"Practical Significance of Zero-Shot F1\"\n- 问题：R-F1 2-8% 意味着模型几乎无法正确抽取。在此质量水平下：(a) violation rate 的分母（predicted triples）中绝大多数是错误预测，rate 的变化可能由 prediction distribution 的全局偏移驱动而非 constraint 的精准修正；(b) 论文的叙事重心放在 zero-shot（§5.1-5.3 占实验部分 ~60%），fine-tuning composability 的篇幅相对不足。Appendix B 试图解释 \"F1 serves as a control variable\"，但论文的核心 contribution 不应需要附录来辩护其主要实验 regime 的意义。\n- 建议：重新平衡叙事，将 fine-tuning composability 提升为主要实验（这是方法有部署价值的场景），将 zero-shot 明确定位为 stress test / robustness analysis。\n\n**W6 [warning] Mistral 结果显著弱于叙事暗示。**\n- 具体位置：Table 3（Mistral SciERC DR 13.40%, DocRED DR 33.20%）、Appendix B dual-factor\n- 问题：Mistral 在 SciERC 仅 42% DR reduction（vs. Qwen 94%, Llama 99%），DocRED 残留 33.20% DR。论文将 Mistral 定义为 \"boundary condition\" 并提出 ET>5% 排除准则，但：(a) 这个准则是 post-hoc 的（在看到结果后制定）；(b) ET>5% 的 threshold 没有理论或实证依据；(c) 对于 \"poorly-calibrated models\" 这一大类来说，方法的有效性成疑。如果 OntoCoDec 对 entity typing 质量有前提条件，这是一个重要的适用范围限制，不应被弱化为 \"boundary condition\"。\n- 建议：明确将 entity typing quality 列为方法的前提假设，讨论如何在部署前判断模型是否满足此前提。\n\n**W7 [warning] 未评估下游影响。**\n- 具体位置：§1（\"residual type violations propagate directly into knowledge graphs and decision-support pipelines\"）\n- 问题：Introduction 以 KG/下游 pipeline 的 violation propagation 作为动机，但全文无任何下游评估。DR 从 15% 降至 0.93%（zero-shot）或 0%（fine-tuned）是否实际改善了 KG 质量或下游 QA 性能？CF violation 是否对下游同样有害？Limitations section 承认 \"CF type inconsistencies may propagate to downstream tasks... the impact of such propagation has not been evaluated\"，但如果动机来自下游影响，至少需要 pilot 评估。\n- 建议：至少在一个下游任务（如 KG triple validation、simple QA over extracted triples）上做 pilot evaluation，或将动机从 downstream propagation 调整为 intrinsic type correctness。\n\n### Minor 问题（不影响接收）\n\n**M1.** Table 2 caption 称 \"DR ≤ 0.09%\"，但 table 内 Llama LoRA S1 DR=0.09%、Qwen LoRA S1 DR=0（SciERC only）。同表同时展示 DocRED 结果（caption 提到 \"DocRED: Qwen DR -99%, Llama DR -59%\"），但 DocRED 数据不在表中——读者需要去 Appendix 找。\n\n**M2.** §3.2 \"Logit masking\" 段落提到 \"all others receive logits $-\\infty$\"——实现中是 float('-inf') 还是一个很大的负数？对 numerical stability 的讨论缺失。\n\n**M3.** Appendix B fuzzy matching protocol（token overlap >80% AND edit distance ≤2）的 threshold 选择无 justification。虽然主要影响 Mistral（+0.84pp），但这是评估协议中需要明确说明的 design choice。\n\n**M4.** §4 Constraint Composition 中 comment \"% Data source: artifacts/rebuttal/w2_rectangularity_report.md\" 残留在 LaTeX 源码中（line 34）——虽然不影响 PDF 输出（是注释），但如果 source code 作为 supplementary material 提交，可能泄露 internal artifact 路径。\n\n**M5.** Grammar layer 在 DocRED 上 RV 残留 0.03%（Table 3 footnote: \"rare XGrammar automaton edge case\"）。这是 XGrammar 的 bug 还是 OntoCoDec implementation 的问题？如果是前者，是否已上报？\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** Constraint table 构建细节：SciERC/DocRED 的 constraint table 是否仅包含 training set 中出现过的 (head_type, tail_type) pairs？如果 test set 中存在 training set 未见过的合法 type pairs，这些 triple 会被错误地标记为 DR violation 吗？请报告 constraint table 对 test set 的覆盖率。\n\n**Q2.** CF 对下游的影响：CF violation 意味着同一实体在不同 triple 中被赋予不同类型。在 KG construction 场景中，这会导致什么？是否每个 triple 独立入库（则 CF 无影响），还是需要全局一致的 entity typing（则 CF 严重）？\n\n**Q3.** Post-hoc filtering 在 5/6 zero-shot settings 下 F1 更高（Appendix B Table 8）。在 fine-tuned setting 下两者基本持平（±0.55pp）。那么 OntoCoDec 相对于 post-hoc filtering 的实际优势在哪里？仅仅是 recall preservation 吗？是否有 reject rate 达到实际不可用程度的 real-world scenario？\n\n**Q4.** Beam search ($k$=4) 在 fine-tuned SciERC 上消除所有四类 violation，为什么 beam search 不是默认推荐配置？1.54× latency overhead 在离线 batch IE 中似乎可以接受。\n\n**Q5.** Sequential masking 要求 head → tail → relation → head_type → tail_type 的固定字段顺序（§3.1）。如果模型生成顺序与此不符（如先生成 relation 再生成 head），约束如何处理？这是否限制了 prompt template 的灵活性？\n\n---\n\n## Missing References\n\n1. **InstructUIE** (Wang et al., 2023): 统一 IE instruction-tuning 框架，与 GoLLIE/UIE 同类但更新，应在 Related Work 讨论。\n2. **DeepStruct** (Wang et al., 2022): 预训练 structured prediction 模型，将多种 IE 任务统一为 structure generation。\n3. **USM** (Lou et al., 2023): Universal Structure Model for IE，与 UIE 类似路线。\n4. **REBEL** (Cabot and Navigli, 2021): 已引用但缺少实验对比——作为 end-to-end RE generation baseline，至少应讨论为什么不做实验对比。\n5. **MarkupLM/GraphIE** 系列 document-level IE 工作：DocRED 是 document-level RE，相关 baseline 需要更全面的覆盖。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**一句话总结**: 技术上正确且实验覆盖广泛的 constrained decoding for IE 工作，但 CF 副作用作为结构性缺陷削弱了核心 claim、constraint table 的训练数据来源与 \"ontology\" framing 不符、缺少关键 baseline，整体处于 Findings 水平。\n\n**推荐理由**: 本文的积极面不可忽视：问题定义清晰（S1）、两层组合架构有新意（S2）、实验覆盖面在同类论文中属于上乘（S3）、fine-tuning composability 有实用价值（S4）、局限讨论诚实（S6）。然而，W1（constraint table vs. ontology framing）和 W2（CF trade-off）是两个互相关联的结构性问题——当约束来自不完整的训练数据统计时，enforcement 更容易触发 fallback 从而放大 CF，而 CF 正是方法的主要副作用。W3（missing baselines）使得无法判断 OntoCoDec 相对于已有 constrained IE 方法的真实增量。这三个问题共同将论文定位在 Findings 而非 Conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### §1 Introduction\n- 叙事结构清晰，从 violation 问题 → 现有方法不足 → OntoCoDec → contributions。但 Contribution 3 过于密集——将 RE composability、EE composability、zero-shot robustness、beam search 结果全部压在一条 contribution 中，建议拆分。\n- \"training-free\" 这一 framing 在 Introduction 中隐含出现（\"compiles constraints automatically from ontology schemas\"），但实际上 fine-tuning 是方法真正有效的必要条件（zero-shot 下 CF 严重）。\n\n### §2 Background\n- 清晰、简洁、必要。Constraint tightness 定义（Eq. 2 在 §4）和 prefix-decidability 的讨论是有价值的前置知识。\n\n### §3 Method\n- 技术描述清楚。Entity registry 的 incremental construction、position detection via prefix pattern matching、continuation masking for tokenizer-agnostic type masking 都描述充分。\n- 但缺少 failure mode 分析：如果 prefix pattern matching 失败（如模型生成 unexpected JSON structure），semantic layer 如何 gracefully degrade？§3.4 的 grammar-first fallback 仅处理 $S(t) \\cap G(t) = \\emptyset$，但 position detection failure 是另一类问题。\n\n### §4 Constraint Composition\n- Non-rectangularity 分析（0/7 SciERC, 23/96 DocRED 是 rectangular）说服力强。\n- Constraint tightness 公式（Eq. 2）使用 $|\\mathcal{E}|^2$ 作为分母，假设所有 type pair 等概率出现——实际上 type pair 分布高度不均匀，是否应该用加权版本？\n\n### §5 Experiments\n- §5.1 SciERC ablation 是论文最扎实的部分。\n- §5.2 DocRED: Grammar-only 增加 DR（18.46% → 26.17%）这一现象值得更多讨论——它揭示了一个评估方法论问题：不同 constraint 配置下 evaluable triples 的集合不同，violation rate 的比较不完全是 apples-to-apples。\n- §5.3 Cross-model: Mistral 的结果相对于另外两个模型差距极大（DR 42% reduction vs. 94-99%），将其简单标为 \"boundary condition\" 不够充分。\n- §5.4 WikiEvents: CF 高达 15-21%——如果用户部署 OntoCoDec 做 EE，他们会面临 ~1/5 的实体类型不一致。这在 zero-shot 下是否实际可用？\n- Runtime paragraph: 数据充分，overhead 合理。\n\n### §6 Related Work\n- 主文过于压缩（一个段落），实质性比较不足。Appendix 详尽但主文读者无法获得必要的 positioning 信息。建议在主文增加 1-2 句与 GCD、GoLLIE 的关键区别。\n\n### §7 Discussion and Conclusion\n- 过于简短（约 80 words）。缺少对主要发现的综合解读、对 CF 问题的前瞻展望、对 method 适用范围的总结。\n\n### Limitations\n- 内容详尽且诚实，覆盖了 CF scope、evaluation coverage、engineering considerations。但 \"WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split)\" 需要更明确——20 document 是数据集限制还是实验设计选择？如果是前者，OK；如果是后者，应扩展。\n\n### Appendix\n- 覆盖面优秀（prompts, extended discussion, per-relation analysis, sampling, beam search, reproducibility, doc length, prompt sensitivity, case studies, scalability, full FT）。\n- Case studies（Appendix K）特别有用，Case 4 展示了 trajectory divergence 的 failure mode。\n- 但附录之间存在信息重复（如 CF-DR trade-off 在多处重复讨论），可以精简。\n",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 — Round 1 审稿报告\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审查侧重**: 方法严谨性 + 实验设计与完整性 + 可复现性\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，将 IE ontology schema 编译为两层可组合的 token-level 解码约束：(1) grammar layer (XGrammar) 保证 JSON 结构合法性和词汇成员资格；(2) semantic layer 通过有状态实体注册表和动态 logit masking 执行 per-triple domain/range 类型约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上评估，覆盖 4 个模型（8B-70B）、3 种 tokenizer 族、zero-shot 和 LoRA fine-tuning 两种 regime。核心结果：fine-tuning 组合下 DR ≤ 0.20%、R-F1 ±0.6pp；zero-shot 下 DR 降低 42-99%。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 (Acceptable) | 核心两层组合机制技术正确，但 CF 副作用是结构性缺陷（非可修复 bug），constraint table 来源于训练数据而非形式本体削弱了核心 claim，部分统计证据不足 |\n| Excitement | 3/5 (Interesting) | 问题定义清晰，violation taxonomy 有用，enabling dependency 洞察有趣；但实际收益受限于 CF trade-off 和 post-hoc filtering 在多数 setting 下 F1 更高 |\n| Reproducibility | 4/5 | 超参数、prompt、硬件、评估协议描述详尽；代码承诺 acceptance 后发布但当前不可用 |\n| Overall Assessment | **3.0 (Findings)** | 扎实的技术贡献和充分的实验覆盖，但 CF trade-off、constraint table 来源问题、缺少关键 baseline 阻止 Conference 推荐 |\n| Confidence | 4/5 | 对 constrained decoding 和 IE 领域较为熟悉 |\n\n---\n\n## Strengths\n\n**S1. 问题定义清晰，violation taxonomy 系统化。** §2 对 IE ontology 的形式化定义（$\\mathcal{O} = (\\mathcal{E}, \\mathcal{R}, \\sigma)$）和四类 violation（DR/RV/ET/CF）的分类是干净的，constraint tightness（Eq. 2）作为预测 violation 难度的指标有独立分析价值。\n\n**S2. 两层组合架构设计合理，enabling dependency 洞察有价值。** Table 1 ablation 清楚展示 semantic-only 仅降低 24% DR（因缺乏词汇保证），而 grammar+semantic 组合降低 94%。这一 enabling dependency 不是 trivial 的，值得报告。Sequential masking 对 non-rectangular type signatures 的必要性分析（§4, footnote 1: 独立检查会多放 33-37% spurious pairs）是严谨的。\n\n**S3. 实验覆盖面广。** 3 数据集 × 4 模型 × 2 regime（zero-shot/fine-tuned）× 3 解码策略（greedy/sampling/beam）× 3 prompt 变体 × 3 文档长度分层，加上 full FT baseline、scalability benchmark。附录覆盖了大部分可预见的 reviewer 质疑点。\n\n**S4. Fine-tuning composability 结果实用。** Table 2 和 Appendix B Table 5 展示 LoRA+S1 在 4 个 model×dataset 设置下 DR ≤ 0.20%、R-F1 ±0.6pp，这是有部署价值的。beam search 进一步消除所有四类 violation（SciERC, 两个 calibrated models），是一个令人印象深刻的结果。\n\n**S5. 工程开销低。** +2-13% inference overhead、sub-second compilation、constant overhead up to 1,000 relations（Appendix L）使方法在实际部署中可行。\n\n**S6. 诚实讨论局限。** CF trade-off 的分析（Appendix B Table 4, Spearman ρ=-0.77）和 Mistral boundary condition 的处理是坦诚的，优于许多同类论文。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [critical] Constraint table 来源于训练数据，非形式本体，与标题/framing 不符。**\n- 具体位置：§5 Setup（\"RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology)\"）\n- 问题：论文标题为 \"Compiled Ontology Constraints\"，Abstract 和 Introduction 反复使用 \"ontology schema\" 一词。但对于 SciERC 和 DocRED（论文的两个主要 RE 数据集），约束表是从训练集共现统计中提取的，而非正式本体。这导致：(a) 约束表不完整——Appendix B 残留 DR error analysis 显示 33% 的残留 violation 源于 \"schema coverage gaps\"；(b) 约束的质量取决于训练集的统计特性，而非领域知识；(c) 论文没有报告约束表的覆盖率（训练集 type pairs 覆盖测试集 type pairs 的比例）。只有 WikiEvents 使用了真正的形式本体（KAIROS），但 WikiEvents 结果被标记为 \"preliminary\"（20 文档测试集）。\n- 为什么影响接收：这是 framing integrity 问题。论文的核心叙事——\"编译本体约束\"——在其主要实验中并不成立。\n- 建议修改方向：(1) 明确区分 \"formal ontology constraints\"（WikiEvents）和 \"empirical type-pair constraints\"（SciERC/DocRED），在标题或 Introduction 中体现；(2) 报告 constraint table 的覆盖率和 test set 中 unseen type pairs 的比例；(3) 分析 constraint table completeness 对方法效果的敏感性。\n\n**W2 [critical] CF 副作用严重且为结构性问题，削弱核心贡献。**\n- 具体位置：Table 1（CF 0.08% → 9.90%）、Table 3（CF up to 12.02%）、Table 4（CF 15-21% on WikiEvents）、Appendix B Table 4（CF fallback ablation）\n- 问题：OntoCoDec 在解决 DR 的同时引入了新的 violation 类型 CF，zero-shot 下可达 12.02%（Llama DocRED）和 21.1%（Qwen WikiEvents）。Appendix B 的 CF-DR trade-off ablation 证实这是结构性的：消除 CF 会将 violation re-route 到 DR（+13.85pp），总 violation 反而增加。这意味着：(a) 论文的核心 claim——\"减少 type violations\"——需要附加条件：减少 DR 的代价是增加 CF；(b) zero-shot 下 total type-violation burden（DR+CF）从 15.45% 降至 10.83%（SciERC），降幅仅 30%，远不如 \"94% DR reduction\" 的 headline number 暗示的效果；(c) fine-tuning 将 CF 降至 ~1%，但这意味着 OntoCoDec 只在与 fine-tuning 组合时真正有效，与 \"training-free\" 的定位有张力。\n- 为什么影响接收：核心 claim 的表述方式（\"DR ↓94%\"）遮蔽了 total violation 的真实变化。审稿人需要确认 headline number 不具误导性。\n- 建议修改方向：(1) 在 Abstract 和 Introduction 中报告 total type-violation burden 的变化（DR+CF），而非仅报告 DR；(2) 明确 \"training-free\" 的适用范围——zero-shot 下 CF 严重，方法的实际价值主要在 fine-tuning 组合场景；(3) 考虑将 total violation reduction 作为主指标。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W3 [warning] 缺少关键 baseline 对比。**\n- 具体位置：§6 Related Work, §5 Experiments\n- 问题：Related Work 讨论了多种 constrained IE 方法（GoLLIE、GenIE、EnriCo、GCD），但实验中唯一的 baseline 是 post-hoc filtering。缺少：(a) GoLLIE（schema-as-code, 同样 address type compliance）；(b) EnriCo（ASP constraints at decode time, 最直接的 constrained decoding for IE 对比）；(c) GCD（grammar-constrained decoding for IE, 论文自己称其为 \"closest precursor\"）。Post-hoc filtering 在 5/6 zero-shot settings 下 F1 更高（Appendix B Table 8），这使得 OntoCoDec 在 zero-shot 场景的实际优势不明确。\n- 建议：至少与 GCD 做实验对比（论文已实现 grammar-only 行，但 GCD 还有 input-dependent grammar 功能），或者说明为什么 GoLLIE/EnriCo 不可比（如需要 training 或 domain-specific rules）。\n\n**W4 [warning] 多个关键实验的样本量不足，统计可信度存疑。**\n- 具体位置：Appendix B（dual-factor: n=4, p≈0.058）、Appendix D（sampling: DocRED 114/998 docs）、§5.4（WikiEvents FT: 20 docs）、Appendix F（beam DocRED: 50 docs）\n- 问题：(a) Dual-factor 线性拟合 R²=0.886 但 n=4, df=2, p≈0.058——论文承认是 \"descriptive characterization\" 但仍构建了围绕 \"dual-factor pattern\" 的叙事（§4, §5.3）；(b) DocRED sampling 仅 114/998 documents（原因：\"~300h due to extended generation\"），但 CF 从 2.57% 跳至 12.63%，这个差异是否由小样本噪声驱动？(c) WikiEvents FT composability 仅 20 documents，bootstrap CI 极宽（如 RoV [0%, 1.73%]），trigger F1 变化为 -5.4pp，confidence interval 在此样本量下是否可信？(d) Beam search DocRED 仅 50 documents——Clopper-Pearson 95% CI upper bound 5.8% 并不能强有力地支持 \"eliminates DR\"。\n- 建议：(a) 降低 dual-factor pattern 在主文叙事中的比重，或增加数据点（更多 model×dataset 配置）；(b) 对小样本实验明确标注置信区间并在 claim 中使用 hedging language；(c) WikiEvents 和 beam search DocRED 实验应在条件允许时扩展样本量。\n\n**W5 [warning] Zero-shot R-F1 过低（2-8%），该 regime 下的 violation rate 分析对实际部署的指导意义有限。**\n- 具体位置：§5 全节、Appendix B \"Practical Significance of Zero-Shot F1\"\n- 问题：R-F1 2-8% 意味着模型几乎无法正确抽取。在此质量水平下：(a) violation rate 的分母（predicted triples）中绝大多数是错误预测，rate 的变化可能由 prediction distribution 的全局偏移驱动而非 constraint 的精准修正；(b) 论文的叙事重心放在 zero-shot（§5.1-5.3 占实验部分 ~60%），fine-tuning composability 的篇幅相对不足。Appendix B 试图解释 \"F1 serves as a control variable\"，但论文的核心 contribution 不应需要附录来辩护其主要实验 regime 的意义。\n- 建议：重新平衡叙事，将 fine-tuning composability 提升为主要实验（这是方法有部署价值的场景），将 zero-shot 明确定位为 stress test / robustness analysis。\n\n**W6 [warning] Mistral 结果显著弱于叙事暗示。**\n- 具体位置：Table 3（Mistral SciERC DR 13.40%, DocRED DR 33.20%）、Appendix B dual-factor\n- 问题：Mistral 在 SciERC 仅 42% DR reduction（vs. Qwen 94%, Llama 99%），DocRED 残留 33.20% DR。论文将 Mistral 定义为 \"boundary condition\" 并提出 ET>5% 排除准则，但：(a) 这个准则是 post-hoc 的（在看到结果后制定）；(b) ET>5% 的 threshold 没有理论或实证依据；(c) 对于 \"poorly-calibrated models\" 这一大类来说，方法的有效性成疑。如果 OntoCoDec 对 entity typing 质量有前提条件，这是一个重要的适用范围限制，不应被弱化为 \"boundary condition\"。\n- 建议：明确将 entity typing quality 列为方法的前提假设，讨论如何在部署前判断模型是否满足此前提。\n\n**W7 [warning] 未评估下游影响。**\n- 具体位置：§1（\"residual type violations propagate directly into knowledge graphs and decision-support pipelines\"）\n- 问题：Introduction 以 KG/下游 pipeline 的 violation propagation 作为动机，但全文无任何下游评估。DR 从 15% 降至 0.93%（zero-shot）或 0%（fine-tuned）是否实际改善了 KG 质量或下游 QA 性能？CF violation 是否对下游同样有害？Limitations section 承认 \"CF type inconsistencies may propagate to downstream tasks... the impact of such propagation has not been evaluated\"，但如果动机来自下游影响，至少需要 pilot 评估。\n- 建议：至少在一个下游任务（如 KG triple validation、simple QA over extracted triples）上做 pilot evaluation，或将动机从 downstream propagation 调整为 intrinsic type correctness。\n\n### Minor 问题（不影响接收）\n\n**M1.** Table 2 caption 称 \"DR ≤ 0.09%\"，但 table 内 Llama LoRA S1 DR=0.09%、Qwen LoRA S1 DR=0（SciERC only）。同表同时展示 DocRED 结果（caption 提到 \"DocRED: Qwen DR -99%, Llama DR -59%\"），但 DocRED 数据不在表中——读者需要去 Appendix 找。\n\n**M2.** §3.2 \"Logit masking\" 段落提到 \"all others receive logits $-\\infty$\"——实现中是 float('-inf') 还是一个很大的负数？对 numerical stability 的讨论缺失。\n\n**M3.** Appendix B fuzzy matching protocol（token overlap >80% AND edit distance ≤2）的 threshold 选择无 justification。虽然主要影响 Mistral（+0.84pp），但这是评估协议中需要明确说明的 design choice。\n\n**M4.** §4 Constraint Composition 中 comment \"% Data source: artifacts/rebuttal/w2_rectangularity_report.md\" 残留在 LaTeX 源码中（line 34）——虽然不影响 PDF 输出（是注释），但如果 source code 作为 supplementary material 提交，可能泄露 internal artifact 路径。\n\n**M5.** Grammar layer 在 DocRED 上 RV 残留 0.03%（Table 3 footnote: \"rare XGrammar automaton edge case\"）。这是 XGrammar 的 bug 还是 OntoCoDec implementation 的问题？如果是前者，是否已上报？\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** Constraint table 构建细节：SciERC/DocRED 的 constraint table 是否仅包含 training set 中出现过的 (head_type, tail_type) pairs？如果 test set 中存在 training set 未见过的合法 type pairs，这些 triple 会被错误地标记为 DR violation 吗？请报告 constraint table 对 test set 的覆盖率。\n\n**Q2.** CF 对下游的影响：CF violation 意味着同一实体在不同 triple 中被赋予不同类型。在 KG construction 场景中，这会导致什么？是否每个 triple 独立入库（则 CF 无影响），还是需要全局一致的 entity typing（则 CF 严重）？\n\n**Q3.** Post-hoc filtering 在 5/6 zero-shot settings 下 F1 更高（Appendix B Table 8）。在 fine-tuned setting 下两者基本持平（±0.55pp）。那么 OntoCoDec 相对于 post-hoc filtering 的实际优势在哪里？仅仅是 recall preservation 吗？是否有 reject rate 达到实际不可用程度的 real-world scenario？\n\n**Q4.** Beam search ($k$=4) 在 fine-tuned SciERC 上消除所有四类 violation，为什么 beam search 不是默认推荐配置？1.54× latency overhead 在离线 batch IE 中似乎可以接受。\n\n**Q5.** Sequential masking 要求 head → tail → relation → head_type → tail_type 的固定字段顺序（§3.1）。如果模型生成顺序与此不符（如先生成 relation 再生成 head），约束如何处理？这是否限制了 prompt template 的灵活性？\n\n---\n\n## Missing References\n\n1. **InstructUIE** (Wang et al., 2023): 统一 IE instruction-tuning 框架，与 GoLLIE/UIE 同类但更新，应在 Related Work 讨论。\n2. **DeepStruct** (Wang et al., 2022): 预训练 structured prediction 模型，将多种 IE 任务统一为 structure generation。\n3. **USM** (Lou et al., 2023): Universal Structure Model for IE，与 UIE 类似路线。\n4. **REBEL** (Cabot and Navigli, 2021): 已引用但缺少实验对比——作为 end-to-end RE generation baseline，至少应讨论为什么不做实验对比。\n5. **MarkupLM/GraphIE** 系列 document-level IE 工作：DocRED 是 document-level RE，相关 baseline 需要更全面的覆盖。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**一句话总结**: 技术上正确且实验覆盖广泛的 constrained decoding for IE 工作，但 CF 副作用作为结构性缺陷削弱了核心 claim、constraint table 的训练数据来源与 \"ontology\" framing 不符、缺少关键 baseline，整体处于 Findings 水平。\n\n**推荐理由**: 本文的积极面不可忽视：问题定义清晰（S1）、两层组合架构有新意（S2）、实验覆盖面在同类论文中属于上乘（S3）、fine-tuning composability 有实用价值（S4）、局限讨论诚实（S6）。然而，W1（constraint table vs. ontology framing）和 W2（CF trade-off）是两个互相关联的结构性问题——当约束来自不完整的训练数据统计时，enforcement 更容易触发 fallback 从而放大 CF，而 CF 正是方法的主要副作用。W3（missing baselines）使得无法判断 OntoCoDec 相对于已有 constrained IE 方法的真实增量。这三个问题共同将论文定位在 Findings 而非 Conference。\n\n---\n\n## Detailed Comments（逐节）\n\n### §1 Introduction\n- 叙事结构清晰，从 violation 问题 → 现有方法不足 → OntoCoDec → contributions。但 Contribution 3 过于密集——将 RE composability、EE composability、zero-shot robustness、beam search 结果全部压在一条 contribution 中，建议拆分。\n- \"training-free\" 这一 framing 在 Introduction 中隐含出现（\"compiles constraints automatically from ontology schemas\"），但实际上 fine-tuning 是方法真正有效的必要条件（zero-shot 下 CF 严重）。\n\n### §2 Background\n- 清晰、简洁、必要。Constraint tightness 定义（Eq. 2 在 §4）和 prefix-decidability 的讨论是有价值的前置知识。\n\n### §3 Method\n- 技术描述清楚。Entity registry 的 incremental construction、position detection via prefix pattern matching、continuation masking for tokenizer-agnostic type masking 都描述充分。\n- 但缺少 failure mode 分析：如果 prefix pattern matching 失败（如模型生成 unexpected JSON structure），semantic layer 如何 gracefully degrade？§3.4 的 grammar-first fallback 仅处理 $S(t) \\cap G(t) = \\emptyset$，但 position detection failure 是另一类问题。\n\n### §4 Constraint Composition\n- Non-rectangularity 分析（0/7 SciERC, 23/96 DocRED 是 rectangular）说服力强。\n- Constraint tightness 公式（Eq. 2）使用 $|\\mathcal{E}|^2$ 作为分母，假设所有 type pair 等概率出现——实际上 type pair 分布高度不均匀，是否应该用加权版本？\n\n### §5 Experiments\n- §5.1 SciERC ablation 是论文最扎实的部分。\n- §5.2 DocRED: Grammar-only 增加 DR（18.46% → 26.17%）这一现象值得更多讨论——它揭示了一个评估方法论问题：不同 constraint 配置下 evaluable triples 的集合不同，violation rate 的比较不完全是 apples-to-apples。\n- §5.3 Cross-model: Mistral 的结果相对于另外两个模型差距极大（DR 42% reduction vs. 94-99%），将其简单标为 \"boundary condition\" 不够充分。\n- §5.4 WikiEvents: CF 高达 15-21%——如果用户部署 OntoCoDec 做 EE，他们会面临 ~1/5 的实体类型不一致。这在 zero-shot 下是否实际可用？\n- Runtime paragraph: 数据充分，overhead 合理。\n\n### §6 Related Work\n- 主文过于压缩（一个段落），实质性比较不足。Appendix 详尽但主文读者无法获得必要的 positioning 信息。建议在主文增加 1-2 句与 GCD、GoLLIE 的关键区别。\n\n### §7 Discussion and Conclusion\n- 过于简短（约 80 words）。缺少对主要发现的综合解读、对 CF 问题的前瞻展望、对 method 适用范围的总结。\n\n### Limitations\n- 内容详尽且诚实，覆盖了 CF scope、evaluation coverage、engineering considerations。但 \"WikiEvents fine-tuning composability is preliminary (20-document test set, the full official split)\" 需要更明确——20 document 是数据集限制还是实验设计选择？如果是前者，OK；如果是后者，应扩展。\n\n### Appendix\n- 覆盖面优秀（prompts, extended discussion, per-relation analysis, sampling, beam search, reproducibility, doc length, prompt sensitivity, case studies, scalability, full FT）。\n- Case studies（Appendix K）特别有用，Case 4 展示了 trajectory divergence 的 failure mode。\n- 但附录之间存在信息重复（如 CF-DR trade-off 在多处重复讨论），可以精简。\n",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-19T07:14:03.048529+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4574
}
```

</details>

---


### Assistant

_source line 552 · 2026-05-19T07:14:12.997104+00:00_

Round 1 审稿报告已提交给 Review Director。

**评分总结**:
- **Overall: 3.0 (Findings)**，Confidence 4/5
- Soundness 3/5, Excitement 3/5, Reproducibility 4/5

**核心判断**: 两个结构性问题阻止 Conference 推荐：
1. **W1**: 标题称 "Compiled Ontology Constraints"，但 SciERC/DocRED 的约束表来自训练数据共现而非形式本体，framing 与实际不符
2. **W2**: CF 副作用严重（zero-shot 下 9-21%），且为不可解的结构性 trade-off，headline number "DR↓94%" 遮蔽了 total violation 仅降 30% 的事实

另有缺少关键 baseline（W3）、多个实验样本量不足（W4）、zero-shot F1 过低（W5）等 should-fix 问题。

积极面：问题定义清晰、两层组合设计有新意、fine-tuning composability 有部署价值、实验覆盖面广、局限讨论诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

4 recorded events


### User

_source line 553 · 2026-05-19T07:16:48.447800+00:00_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 2 的 Must-Fix 问题

**N1 [critical] CF trade-off 与 "near-lossless composability" claim 不一致。**
- Abstract 声称 "near-lossless composability" 但仅报告 DR 下降，忽略 CF 从 0→9.90%。SciERC 上 total violation burden 仅减少约 30%，非 Abstract 暗示的 94%。"near-lossless" 在 zero-shot 下不成立。

**N2 [critical] WikiEvents 评估过于初步但在 Abstract/Contributions 中占较大权重。**
- 仅 20 个测试文档，论文自称 "preliminary"，但 Abstract 和 Contribution 中将 EE 与 RE 并列。

**N3 [critical] 缺少 Responsible NLP Research Checklist。**
- ARR 2026 要求该 checklist，缺失可能导致 desk reject。

### Reviewer 2 的 Should-Fix 问题

**W1** Related Work 主体过于压缩（§6 仅 12 行，一个段落）。
**W2** Abstract 数据密度过高（201 词含约 15 个数字、7 个缩写）。
**W3** Contribution 3 信息过载（5+ 独立 claim 压在一条中）。
**W4** Dual-factor pattern 统计支撑不足（n=4, p≈0.058）。
**W5** DocRED grammar-only DR 增加（18.46%→26.17%）解释不充分。
**W6** §7 Discussion and Conclusion 过于简短（6 行，1 段）。

### Reviewer 2 的小问题

- Bib 有 8 个 orphan entries + 1 个 duplicate key
- 3 篇引用未在 OpenAlex 找到完全匹配
- Constraint tightness 在 §2 和 §4 重复定义
- Table 1 caption 含不必要 claim

### Reviewer 2 的 Questions

**Q1**: CF↔DR Pareto 前沿是否意味着 per-slot enforcement 框架内无法同时降低两者？
**Q2**: Qwen LoRA DR=0% vs Llama LoRA DR=0.09% 是否统计显著？
**Q3**: Constraint table coverage gap 对 DR 和 F1 的影响多大？
**Q4**: Mistral 排除在 dual-factor 但保留在 cross-model validation 中，适用范围如何框定？
**Q5**: Beam search + LoRA 消除所有 violation 在 DocRED 上是否成立？

### Reviewer 2 的 Missing References
InstructUIE, UniversalNER, Wadhwa et al. (2023), DeepStruct, BioREx

---

请对以上 N1-N3、W1-W6、每条小问题、Q1-Q5 逐条给出 [AGREE] 或 [REBUT]，并简述理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-19T07:18:31.443004+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条评判\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: CF trade-off 与 \"near-lossless composability\" claim 不一致。**\n完全同意，这与我的 W2 判断一致。Abstract 第 6 行 \"near-lossless composability\" 仅以 DR 和 R-F1 衡量，但 CF 从 0.08% 升至 9.90%（Table 1）。SciERC total violation burden (DR+CF) 从 15.45% 降至 10.83%，降幅仅 30%，与 \"94% DR reduction\" 的 headline 形成强烈反差。更关键的是，Appendix B Table 4 的 CF fallback ablation 证实 CF↔DR 是结构性 trade-off（消除 CF 导致 DR +13.85pp），因此 \"near-lossless\" 在 zero-shot regime 下是不准确的表述。Fine-tuning 下 CF 降至 ≤1.18%（Table 2），此时 \"near-lossless\" 勉强成立，但 Abstract 没有区分两种 regime。R2 对此问题的定位准确。\n\n**[AGREE] R2-N2: WikiEvents 评估过于初步但在 Abstract/Contributions 中占较大权重。**\n同意。我在 W4 中也标记了 20-document test set 的统计可信度问题。补充一个 R2 未提及的细节：§5.4 报告 trigger F1 变化为 -5.4pp（Qwen），在 20 文档上 bootstrap CI 必然极宽，无法支撑有意义的结论。然而，需要公平指出 §5.4 明确声明 \"WikiEvents uses a 194/20/20 train/dev/test split; the 20-document test set is a dataset constraint, not a design choice\"。所以问题不在作者选择了小样本，而在于 Abstract 和 Contribution 3 将 EE 结果与 RE 结果并列呈现时没有充分 hedge。R2 的建议——降低 EE 在 Abstract/Contributions 中的权重或增加 hedging language——是合理的。\n\n**[REBUT] R2-N3: 缺少 Responsible NLP Research Checklist。**\nR2 将此标记为 critical (可能导致 desk reject)。我认为严重性判断过高，应降为 Should-Fix。理由：(1) Responsible NLP Research Checklist 通常在 OpenReview 投稿系统中以单独表单提交，而非嵌入论文 PDF——ARR 的提交流程是 PDF + checklist form 分开填写；(2) 我们审查的是 main.tex 源文件，而非最终提交的 OpenReview submission，无法确认 checklist 是否已通过系统填写；(3) 论文已包含 Ethics Statement（main.tex line 90-95）和 detailed Limitations section（line 65-87），这些覆盖了 checklist 的核心内容。如果作者确实计划提交但未填写 checklist form，这是投稿工程问题而非论文质量问题，不应列为 critical。建议降级为 administrative reminder。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: Related Work 主体过于压缩。**\n同意，与我的 §6 detailed comments 一致。§6 主文仅一个密集段落，将 grammar-constrained decoding、type-constrained code gen、vocabulary-constrained IE、training-based methods、post-hoc approaches 全部压缩在 ~12 行中。读者无法从主文获得必要的 positioning 信息。Appendix A 的 Extended Related Work 虽然详尽（~110 行），但主文的读者（包括很多审稿人）可能不会翻到附录。建议在主文中至少增加 2-3 小段，分别覆盖最相关的范式。\n\n**[AGREE] R2-W2: Abstract 数据密度过高。**\n同意。重读 abstract.tex，确实在 ~200 词内堆砌了大量数字：DR ≤ 0.20%, R-F1 ±0.6pp, 76-99%, 42%, k=4, ≤1.2%, 56 event types, 80 roles 等。这违反了论文写作规范中 Abstract \"最多引用 2-3 个关键数字\" 的原则。Abstract 的功能是讲清故事（问题→洞察→方法→结果），不是压缩所有 headline numbers。\n\n**[AGREE] R2-W3: Contribution 3 信息过载。**\n同意，我在 §1 detailed comments 中也指出了同样问题。Contribution 3（section1_introduction_draft.tex line 30）将 RE composability, EE composability, zero-shot robustness, beam search 结果全部压在一条中。建议拆分为至少两条：一条 RE/EE composability，一条 robustness/generalization。\n\n**[AGREE] R2-W4: Dual-factor pattern 统计支撑不足。**\n同意，与我的 W4 完全一致。Appendix B 已承认 n=4, df=2, p≈0.058 是 \"descriptive characterization rather than a confirmatory statistical test\"，但 §4（section4_composition_draft.tex line 29）和 §5.3 仍以 \"dual-factor pattern\" 构建叙事，给人一种已确认的统计规律的印象。建议：在主文引用 dual-factor pattern 时增加 \"descriptive\"/\"tentative\" 等限定词。\n\n**[REBUT] R2-W5: DocRED grammar-only DR 增加（18.46%→26.17%）解释不充分。**\n部分反驳。R2 认为解释不充分，但我认为 §5.2 的解释是技术上正确且合理的：grammar-only 消除了 OOV relation predictions（baseline RV=29.66%），使这些 triples 变为可评估状态，暴露了潜在的 type incompatibilities。这不是 constraint \"恶化\" DR，而是评估分母变化导致的 rate 变化。section5_docred_draft.tex line 67 明确写到 \"OOV triples become evaluable and expose latent type incompatibilities\"。**不过**，我认为论文可以做得更好的一点是：报告 DR violation 的 absolute count（而非仅 rate），这样读者可以看到 grammar-only 下的 DR violation 绝对数量是增加还是只是因为分母（evaluable triples）增大而 rate 升高。这是一个 presentation clarity 问题，非 explanation correctness 问题。建议从 Should-Fix 降为 Minor presentation improvement。\n\n**[AGREE] R2-W6: §7 Discussion and Conclusion 过于简短。**\n同意，与我的 §7 detailed comments 一致。section7_conclusion_compressed.tex 仅 ~80 words/6 行，缺少对主要发现的综合解读、CF 问题的前瞻展望、适用范围总结。即使 extended discussion 在 Appendix B，主文的 conclusion 仍需要 standalone 的总结能力。\n\n---\n\n## 小问题\n\n**[AGREE] Bib 有 8 个 orphan entries + 1 个 duplicate key。**\n我未检查 bib 文件，R2 的发现如果准确则应修复。orphan entries 不影响论文质量但 duplicate key 可能导致编译问题。\n\n**[AGREE] 3 篇引用未在 OpenAlex 找到完全匹配。**\n引用真实性是审稿的重要维度。如果 R2 确认了具体哪 3 篇（应该是预印本或非常新的工作），作者需要提供可验证的来源。\n\n**[AGREE] Constraint tightness 在 §2 和 §4 重复定义。**\n确实，§2 Background（section2_background.tex line 10）和 §4 Composition（section4_composition_draft.tex Eq. 2）都给出了 constraint tightness 定义。这是空间浪费，建议在 §2 定义一次，§4 引用。\n\n**[REBUT] Table 1 caption 含不必要 claim。**\n部分反驳。Table 1 caption（section5_scierc_draft.tex line 62）包含 \"Grammar-only represents the ceiling of grammar-constrained decoding [citation]\"。这不完全是 \"不必要 claim\"——它为 Grammar-only 行提供了有用的解释性 context（明确了这一行的意义：它代表了 existing grammar-constrained decoding 方法所能达到的上限）。但可以更简洁地表达，如移到正文而非 caption。Minor style issue。\n\n---\n\n## Questions\n\n**[AGREE] R2-Q1: CF↔DR Pareto 前沿是否意味着 per-slot enforcement 框架内无法同时降低两者？**\n好问题。根据 Appendix B Table 4 的 CF fallback ablation 和 Spearman ρ=-0.77 的 inverse association，答案是：在 **greedy decoding + per-slot enforcement** 框架内，CF 和 DR 确实无法同时降低。但 beam search 提供了一条绕过此 trade-off 的路径（SciERC beam k=4: DR→0%, CF 0.53%，Appendix F Table 7），因为 beam exploration 可以找到同时满足 grammar 和 semantic masks 的 token paths。因此 Pareto 限制是 greedy per-slot enforcement 的属性，非框架的绝对限制。论文可以更清楚地说明这一点。\n\n**[AGREE] R2-Q2: Qwen LoRA DR=0% vs Llama LoRA DR=0.09% 是否统计显著？**\n合理质疑。Table 2 Qwen LoRA S1 DR=0%（0/n triples）vs Llama 0.09%（~1-2 triples out of ~2000）。在如此低的绝对数量下，差异很可能不显著。论文未报告此对比的 p 值或 CI。这不影响核心结论（两者都 ≤0.20%），但 \"DR=0%\" 作为 headline 可能给人过强的 elimination impression。\n\n**[AGREE] R2-Q3: Constraint table coverage gap 对 DR 和 F1 的影响多大？**\n这与我的 W1 高度相关。Appendix B residual DR error analysis 报告 schema coverage gaps 占 33% of 36 residual violations（fine-tuned），但缺少对 zero-shot 下 coverage gap 的定量分析。更关键的是：constraint table coverage 直接决定了方法的理论上限，但论文未报告 coverage rate。\n\n**[AGREE] R2-Q4: Mistral 排除在 dual-factor 但保留在 cross-model validation 中，适用范围如何框定？**\n这与我的 W6 一致。Mistral 在 dual-factor analysis 中被排除（ET>5% criterion），但在 §5.3 cross-model validation 中仍然被报告且计入 \"42-99% DR reduction\" 的 claim range。这两个处理方式之间有张力：如果 Mistral 不适合 dual-factor model，为什么它的结果可以支撑 cross-model generalization claim？论文需要更清晰地定义 OntoCoDec 的适用前提。\n\n**[REBUT] R2-Q5: Beam search + LoRA 消除所有 violation 在 DocRED 上是否成立？**\n部分反驳。R2 质疑 beam+LoRA 的 DocRED 结果。Appendix F（appendix_beam_search.tex）的 zero-shot beam search 在 DocRED 50-document subset 上 Qwen DR→0%, Llama DR→0%。但 R2 问的是 fine-tuned beam search on DocRED——论文确实只报告了 SciERC fine-tuned beam（两个 model 都 all-zero violations），**未报告 DocRED fine-tuned beam**。所以 R2 的隐含质疑是合理的：论文不能 claim \"beam search + LoRA eliminates all violations\" on DocRED without showing the data。但论文在 §5.5（section5_runtime.tex line 12）的 claim \"beam S1 eliminates all four violation types on SciERC for both Qwen and Llama\" 是 precisely scoped to SciERC 的，并未 overclaim DocRED。仍然，缺少 DocRED fine-tuned beam 结果是一个 gap。\n\n---\n\n## Missing References\n\n**[AGREE] InstructUIE**: 同意应引用，我在 missing references 中也列出了此条。\n**[AGREE] UniversalNER**: 合理补充——NER 侧的 universal IE 工作，与 type constraint 相关。\n**[AGREE] Wadhwa et al. (2023)**: 如果是 revisiting relation extraction in the era of LLMs 相关工作，应引用。\n**[AGREE] DeepStruct**: 同意，我也列出了此条。\n**[AGREE] BioREx**: 如果论文讨论了 domain adaptation（如 biomedical），应引用；但论文的评估不涉及 biomedical domain，可作为 Related Work 补充但非必须。\n\n---\n\n## 总结\n\n与 R2 的 17 条意见中，我 **[AGREE] 13 条**，**[REBUT] 3 条**（N3 严重性过高、W5 解释实际充分、Q5 claim 未 overclaim），**partial** 1 条（Table 1 caption style issue）。\n\nR2 的审稿在写作质量和格式合规方面提供了我未充分覆盖的补充视角（bib orphans、checklist、Abstract 数据密度），与我的审稿形成有效互补。我们在核心判断上高度一致：**CF trade-off 是最大的方法论问题，WikiEvents 的 preliminary 状态与 contribution 权重不匹配，dual-factor 统计支撑不足**。\n\n我维持 **Overall 3.0 (Findings)** 的评分不变。\n",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见的逐条评判\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-N1: CF trade-off 与 \"near-lossless composability\" claim 不一致。**\n完全同意，这与我的 W2 判断一致。Abstract 第 6 行 \"near-lossless composability\" 仅以 DR 和 R-F1 衡量，但 CF 从 0.08% 升至 9.90%（Table 1）。SciERC total violation burden (DR+CF) 从 15.45% 降至 10.83%，降幅仅 30%，与 \"94% DR reduction\" 的 headline 形成强烈反差。更关键的是，Appendix B Table 4 的 CF fallback ablation 证实 CF↔DR 是结构性 trade-off（消除 CF 导致 DR +13.85pp），因此 \"near-lossless\" 在 zero-shot regime 下是不准确的表述。Fine-tuning 下 CF 降至 ≤1.18%（Table 2），此时 \"near-lossless\" 勉强成立，但 Abstract 没有区分两种 regime。R2 对此问题的定位准确。\n\n**[AGREE] R2-N2: WikiEvents 评估过于初步但在 Abstract/Contributions 中占较大权重。**\n同意。我在 W4 中也标记了 20-document test set 的统计可信度问题。补充一个 R2 未提及的细节：§5.4 报告 trigger F1 变化为 -5.4pp（Qwen），在 20 文档上 bootstrap CI 必然极宽，无法支撑有意义的结论。然而，需要公平指出 §5.4 明确声明 \"WikiEvents uses a 194/20/20 train/dev/test split; the 20-document test set is a dataset constraint, not a design choice\"。所以问题不在作者选择了小样本，而在于 Abstract 和 Contribution 3 将 EE 结果与 RE 结果并列呈现时没有充分 hedge。R2 的建议——降低 EE 在 Abstract/Contributions 中的权重或增加 hedging language——是合理的。\n\n**[REBUT] R2-N3: 缺少 Responsible NLP Research Checklist。**\nR2 将此标记为 critical (可能导致 desk reject)。我认为严重性判断过高，应降为 Should-Fix。理由：(1) Responsible NLP Research Checklist 通常在 OpenReview 投稿系统中以单独表单提交，而非嵌入论文 PDF——ARR 的提交流程是 PDF + checklist form 分开填写；(2) 我们审查的是 main.tex 源文件，而非最终提交的 OpenReview submission，无法确认 checklist 是否已通过系统填写；(3) 论文已包含 Ethics Statement（main.tex line 90-95）和 detailed Limitations section（line 65-87），这些覆盖了 checklist 的核心内容。如果作者确实计划提交但未填写 checklist form，这是投稿工程问题而非论文质量问题，不应列为 critical。建议降级为 administrative reminder。\n\n---\n\n## Should-Fix 问题\n\n**[AGREE] R2-W1: Related Work 主体过于压缩。**\n同意，与我的 §6 detailed comments 一致。§6 主文仅一个密集段落，将 grammar-constrained decoding、type-constrained code gen、vocabulary-constrained IE、training-based methods、post-hoc approaches 全部压缩在 ~12 行中。读者无法从主文获得必要的 positioning 信息。Appendix A 的 Extended Related Work 虽然详尽（~110 行），但主文的读者（包括很多审稿人）可能不会翻到附录。建议在主文中至少增加 2-3 小段，分别覆盖最相关的范式。\n\n**[AGREE] R2-W2: Abstract 数据密度过高。**\n同意。重读 abstract.tex，确实在 ~200 词内堆砌了大量数字：DR ≤ 0.20%, R-F1 ±0.6pp, 76-99%, 42%, k=4, ≤1.2%, 56 event types, 80 roles 等。这违反了论文写作规范中 Abstract \"最多引用 2-3 个关键数字\" 的原则。Abstract 的功能是讲清故事（问题→洞察→方法→结果），不是压缩所有 headline numbers。\n\n**[AGREE] R2-W3: Contribution 3 信息过载。**\n同意，我在 §1 detailed comments 中也指出了同样问题。Contribution 3（section1_introduction_draft.tex line 30）将 RE composability, EE composability, zero-shot robustness, beam search 结果全部压在一条中。建议拆分为至少两条：一条 RE/EE composability，一条 robustness/generalization。\n\n**[AGREE] R2-W4: Dual-factor pattern 统计支撑不足。**\n同意，与我的 W4 完全一致。Appendix B 已承认 n=4, df=2, p≈0.058 是 \"descriptive characterization rather than a confirmatory statistical test\"，但 §4（section4_composition_draft.tex line 29）和 §5.3 仍以 \"dual-factor pattern\" 构建叙事，给人一种已确认的统计规律的印象。建议：在主文引用 dual-factor pattern 时增加 \"descriptive\"/\"tentative\" 等限定词。\n\n**[REBUT] R2-W5: DocRED grammar-only DR 增加（18.46%→26.17%）解释不充分。**\n部分反驳。R2 认为解释不充分，但我认为 §5.2 的解释是技术上正确且合理的：grammar-only 消除了 OOV relation predictions（baseline RV=29.66%），使这些 triples 变为可评估状态，暴露了潜在的 type incompatibilities。这不是 constraint \"恶化\" DR，而是评估分母变化导致的 rate 变化。section5_docred_draft.tex line 67 明确写到 \"OOV triples become evaluable and expose latent type incompatibilities\"。**不过**，我认为论文可以做得更好的一点是：报告 DR violation 的 absolute count（而非仅 rate），这样读者可以看到 grammar-only 下的 DR violation 绝对数量是增加还是只是因为分母（evaluable triples）增大而 rate 升高。这是一个 presentation clarity 问题，非 explanation correctness 问题。建议从 Should-Fix 降为 Minor presentation improvement。\n\n**[AGREE] R2-W6: §7 Discussion and Conclusion 过于简短。**\n同意，与我的 §7 detailed comments 一致。section7_conclusion_compressed.tex 仅 ~80 words/6 行，缺少对主要发现的综合解读、CF 问题的前瞻展望、适用范围总结。即使 extended discussion 在 Appendix B，主文的 conclusion 仍需要 standalone 的总结能力。\n\n---\n\n## 小问题\n\n**[AGREE] Bib 有 8 个 orphan entries + 1 个 duplicate key。**\n我未检查 bib 文件，R2 的发现如果准确则应修复。orphan entries 不影响论文质量但 duplicate key 可能导致编译问题。\n\n**[AGREE] 3 篇引用未在 OpenAlex 找到完全匹配。**\n引用真实性是审稿的重要维度。如果 R2 确认了具体哪 3 篇（应该是预印本或非常新的工作），作者需要提供可验证的来源。\n\n**[AGREE] Constraint tightness 在 §2 和 §4 重复定义。**\n确实，§2 Background（section2_background.tex line 10）和 §4 Composition（section4_composition_draft.tex Eq. 2）都给出了 constraint tightness 定义。这是空间浪费，建议在 §2 定义一次，§4 引用。\n\n**[REBUT] Table 1 caption 含不必要 claim。**\n部分反驳。Table 1 caption（section5_scierc_draft.tex line 62）包含 \"Grammar-only represents the ceiling of grammar-constrained decoding [citation]\"。这不完全是 \"不必要 claim\"——它为 Grammar-only 行提供了有用的解释性 context（明确了这一行的意义：它代表了 existing grammar-constrained decoding 方法所能达到的上限）。但可以更简洁地表达，如移到正文而非 caption。Minor style issue。\n\n---\n\n## Questions\n\n**[AGREE] R2-Q1: CF↔DR Pareto 前沿是否意味着 per-slot enforcement 框架内无法同时降低两者？**\n好问题。根据 Appendix B Table 4 的 CF fallback ablation 和 Spearman ρ=-0.77 的 inverse association，答案是：在 **greedy decoding + per-slot enforcement** 框架内，CF 和 DR 确实无法同时降低。但 beam search 提供了一条绕过此 trade-off 的路径（SciERC beam k=4: DR→0%, CF 0.53%，Appendix F Table 7），因为 beam exploration 可以找到同时满足 grammar 和 semantic masks 的 token paths。因此 Pareto 限制是 greedy per-slot enforcement 的属性，非框架的绝对限制。论文可以更清楚地说明这一点。\n\n**[AGREE] R2-Q2: Qwen LoRA DR=0% vs Llama LoRA DR=0.09% 是否统计显著？**\n合理质疑。Table 2 Qwen LoRA S1 DR=0%（0/n triples）vs Llama 0.09%（~1-2 triples out of ~2000）。在如此低的绝对数量下，差异很可能不显著。论文未报告此对比的 p 值或 CI。这不影响核心结论（两者都 ≤0.20%），但 \"DR=0%\" 作为 headline 可能给人过强的 elimination impression。\n\n**[AGREE] R2-Q3: Constraint table coverage gap 对 DR 和 F1 的影响多大？**\n这与我的 W1 高度相关。Appendix B residual DR error analysis 报告 schema coverage gaps 占 33% of 36 residual violations（fine-tuned），但缺少对 zero-shot 下 coverage gap 的定量分析。更关键的是：constraint table coverage 直接决定了方法的理论上限，但论文未报告 coverage rate。\n\n**[AGREE] R2-Q4: Mistral 排除在 dual-factor 但保留在 cross-model validation 中，适用范围如何框定？**\n这与我的 W6 一致。Mistral 在 dual-factor analysis 中被排除（ET>5% criterion），但在 §5.3 cross-model validation 中仍然被报告且计入 \"42-99% DR reduction\" 的 claim range。这两个处理方式之间有张力：如果 Mistral 不适合 dual-factor model，为什么它的结果可以支撑 cross-model generalization claim？论文需要更清晰地定义 OntoCoDec 的适用前提。\n\n**[REBUT] R2-Q5: Beam search + LoRA 消除所有 violation 在 DocRED 上是否成立？**\n部分反驳。R2 质疑 beam+LoRA 的 DocRED 结果。Appendix F（appendix_beam_search.tex）的 zero-shot beam search 在 DocRED 50-document subset 上 Qwen DR→0%, Llama DR→0%。但 R2 问的是 fine-tuned beam search on DocRED——论文确实只报告了 SciERC fine-tuned beam（两个 model 都 all-zero violations），**未报告 DocRED fine-tuned beam**。所以 R2 的隐含质疑是合理的：论文不能 claim \"beam search + LoRA eliminates all violations\" on DocRED without showing the data。但论文在 §5.5（section5_runtime.tex line 12）的 claim \"beam S1 eliminates all four violation types on SciERC for both Qwen and Llama\" 是 precisely scoped to SciERC 的，并未 overclaim DocRED。仍然，缺少 DocRED fine-tuned beam 结果是一个 gap。\n\n---\n\n## Missing References\n\n**[AGREE] InstructUIE**: 同意应引用，我在 missing references 中也列出了此条。\n**[AGREE] UniversalNER**: 合理补充——NER 侧的 universal IE 工作，与 type constraint 相关。\n**[AGREE] Wadhwa et al. (2023)**: 如果是 revisiting relation extraction in the era of LLMs 相关工作，应引用。\n**[AGREE] DeepStruct**: 同意，我也列出了此条。\n**[AGREE] BioREx**: 如果论文讨论了 domain adaptation（如 biomedical），应引用；但论文的评估不涉及 biomedical domain，可作为 Related Work 补充但非必须。\n\n---\n\n## 总结\n\n与 R2 的 17 条意见中，我 **[AGREE] 13 条**，**[REBUT] 3 条**（N3 严重性过高、W5 解释实际充分、Q5 claim 未 overclaim），**partial** 1 条（Table 1 caption style issue）。\n\nR2 的审稿在写作质量和格式合规方面提供了我未充分覆盖的补充视角（bib orphans、checklist、Abstract 数据密度），与我的审稿形成有效互补。我们在核心判断上高度一致：**CF trade-off 是最大的方法论问题，WikiEvents 的 preliminary 状态与 contribution 权重不匹配，dual-factor 统计支撑不足**。\n\n我维持 **Overall 3.0 (Findings)** 的评分不变。\n",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-19T07:18:36.123013+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4680
}
```

</details>

---


### Assistant

_source line 556 · 2026-05-19T07:18:40.526444+00:00_

交叉回应已提交。对 R2 的 17 条意见：AGREE 13 条，REBUT 3 条（N3 严重性过高、W5 解释实际充分、Q5 claim 未 overclaim），1 条 partial。核心判断与 R2 高度一致：CF trade-off 是最大问题，WikiEvents preliminary 与 contribution 权重不匹配。维持 Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 16

## Round 16

68 recorded events


### User

_source line 557 · 2026-05-19T07:52:11.003641+00:00_

[Round 10 审稿请求]:
## Round 10 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）

### 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
- **路径**: `projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **目标 venue**: EMNLP 2026 via ACL Rolling Review (ARR)
- **Deadline**: 2026-05-25

### Venue 格式要求（实时搜索确认）
- **页数**: Long paper ≤ 8 页正文（Limitations/Ethics/References/Appendix 不计）
- **模板**: ACL 官方模板，`\usepackage[review]{acl}`
- **匿名**: Double-blind（作者信息不得出现）
- **必须包含**: Limitations section（缺失 = desk reject）
- **Checklist**: Responsible NLP Research checklist 必须填写
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit

### 你的审查侧重

**主要职责：方法严谨性 + 实验设计 + Baseline 对比**

请重点审查以下方面：

1. **方法正确性**：
   - 两层约束（grammar + semantic）的形式化是否严密？
   - Entity registry 的动态构建机制是否存在边界情况？
   - Grammar-first fallback 的设计是否合理？CF↔DR trade-off 的分析是否充分？
   - Constraint tightness κ(r) 的定义和 dual-factor pattern 的统计支撑是否足够？

2. **实验设计**：
   - Ablation 设计是否充分（grammar-only, semantic-only, full S1, S2）？
   - 统计显著性检验是否正确（bootstrap, p-value, CI）？
   - 样本量是否足以支撑 claim（特别关注 dual-factor n=4、WikiEvents 20 docs、DocRED beam 50 docs）？
   - Zero-shot vs Fine-tuned 两种 regime 的实验设计和叙事平衡

3. **Baseline 对比**：
   - 是否缺少关键 baseline？（GoLLIE, EnriCo, KnowCoder, 显式 GCD baseline）
   - Post-hoc filtering 对比是否公平？
   - Cross-model/cross-dataset 验证是否充分？

4. **Claim 与证据匹配**：
   - Abstract/Introduction 中的每条 claim 是否有实验数据支撑？
   - "near-lossless composability" claim 在考虑 CF 后是否仍然成立？
   - "ontology constraints" vs 实际使用 training data 提取的约束表——framing 是否准确？
   - WikiEvents EE 结果标注为 "preliminary" 但在 Abstract/Contribution 中的权重是否恰当？

### 输出格式

请按以下结构输出审稿意见：

```
## Summary
[2-3 句概述]

## Strengths
[S1] ...
[S2] ...

## Weaknesses
[W1] [Must-Fix / Should-Fix / Minor] ...
[W2] ...

## Questions
[Q1] ...

## Missing References
...

## Overall Assessment
Score: X.X (按 EMNLP 2026 ARR 评分标准)
Confidence: X/5
[简短总评]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-19T07:52:30.158409+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 559 · 2026-05-19T07:52:30.209182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-19T07:52:36.289813+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 561 · 2026-05-19T07:52:37.445585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 562 · 2026-05-19T07:52:37.546650+00:00_

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
67	\paragraph{Constraint scope.}
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation sh
…[truncated 4385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-19T07:52:48.913463+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"}]

Based on the search results, here's what I found regarding ACL ARR 2025-2026 reviewer guidelines:

## Reviewer Scoring Criteria

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
You may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Guidelines

All pap
…[truncated 729 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 12623
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-19T07:52:53.185459+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring dimensions, score ranges, and any specific instructions for reviewers. Include all score definitions (soundness, excitement, overall assessment, confidence, etc.) with their numeric scales and descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring dimensions, score ranges, and any specific instructions for reviewers. Include all score definitions (soundness, excitement, overall assessment, confidence, etc.) with their numeric scales and descriptions."
  }
}
```

</details>

---


### Tool call

_source line 565 · 2026-05-19T07:52:53.921235+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 566 · 2026-05-19T07:52:53.978003+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_fd4b26.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract_d3264e.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_550cbf_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs_cf83d1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_additions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/discussion_paragraphs.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_relwork_outline.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/p3_case_studies_861a0d.tex
/home/ubuntu/.agent-ml-re
…[truncated 3453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 56
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-19T07:52:59.254524+00:00_

# ARR Review Form Criteria and Scoring

Based on the ARR Reviewer Guidelines, the document references a review form but **does not provide complete scoring rubrics or numeric scales** within this page. However, it specifies the following scoring dimensions:

## Stated Scoring Dimensions

The guidelines mention three primary scores "Starting with February 2025":

1. **Soundness** - "must be justified by the text of the review"
2. **Excitement** - "reflects our personal taste" and is "orthogonal to the assessment of the soundness"
3. **Overall Assessment** - "an explicit recommendation for the outcome of this paper" that combines "soundness, excitement, and also other factors like novelty and impact"

## Additional Score References

The document also mentions:
- **Confidence score** - reviewers can "indicate your confidence score"
- **Reproducibility scores** - "low reproducibility scores should be justified"

## Critical Gap

The page states: "We have a [tutorial]...for performing common actions on OpenReview" and references "a post describing the [ARR review form](https://aclrollingreview.org/reviewform) in detail," indicating the actual numeric scales and detailed definitions exist in external resources rather than in these guidelines.

**To access complete scoring definitions, consult the linked ARR review form documentation directly.**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6069
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-19T07:53:02.903165+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their numeric scales, and definitions for each score level. Include soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their numeric scales, and definitions for each score level. Include soundness, excitement, overall assessment, confidence, reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 569 · 2026-05-19T07:53:03.406216+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 570 · 2026-05-19T07:53:04.311829+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) ontology schemas into two composable token-level decoding constraints:
3	(1)~a \emph{grammar layer} (XGrammar) that guarantees JSON structural validity and vocabulary membership; and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning; violation rates correlate with \emph{constraint tightness} rather than ontology or model scale.
6	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
7	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} achieves near-lossless composability under fine-tuning: DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp.
8	Under zero-shot decoding, DR drops by 76--99\% for calibrated models, with an accompanying cross-field consistency (CF) increase (9--21\% zero-shot, resolved to $\leq$1.2\% by fine-tuning on both RE and EE).
9	Beam search with LoRA eliminates all four violation types on SciERC.
10	The framework extends to event extraction without modification (preliminary, 20-document test set).
11	OntoCoDec is training-free and applies to any autoregressive LM across four models (8B--70B) and three tokenizer families.
12	\end{abstract}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 571 · 2026-05-19T07:53:04.312218+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 572 · 2026-05-19T07:53:04.463501+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), where extracted triples feed directly into knowledge graphs, reliable type-safety enforcement is needed.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
16	OntoCoDec preserves recall by enforcing constraints during generation rather than discardi
…[truncated 2815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 573 · 2026-05-19T07:53:04.464089+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 574 · 2026-05-19T07:53:04.564924+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
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
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, t
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-19T07:53:09.136823+00:00_

# ARR Review Form Scoring Dimensions

## Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure with unlikely but conceivable gaps
- **3**: Pretty sure but chance of missing details
- **2**: Can defend evaluation but likely missed some details
- **1**: Outside expertise area or paper very difficult to understand

## Soundness
Scale: 1-5 (with .5 increments)
- **5**: "one of the most thorough I have seen, given its type"
- **4**: Strong; provides sufficient support with optional extra experiments
- **3**: Acceptable; supports main claims with minor gaps
- **2**: Poor; main claims lack sufficient support
- **1**: "Major Issues: not yet sufficiently thorough to warrant publication"

## Excitement
Scale: 1-5 (with .5 increments)
- **5**: Highly Exciting; would recommend to others
- **4**: Exciting; would mention to others
- **3**: Interesting; might mention to others
- **2**: Potentially Interesting; doesn't resonate personally
- **1**: "Not Exciting: does not resonate with me"

## Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## Reproducibility
Scale: 1-5
- **5**: "easily reproduce the results"
- **4**: Mostly reproducible despite minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data/insufficient details
- **1**: "not be able to reproduce the results"

## Datasets & Software
Scale: 1-5 each
- **5**: Enabling; affects research direction
- **4**: Useful; recommended for ongoing work
- **3**: Potentially useful
- **2**: Documentary; useful for replication
- **1**: None submitted/released

## Author Identity Knowledge
Scale: 1-5
- **5**: Direct violation of double-blind rules
- **4**: From preprint or workshop paper
- **3**: From submission contents
- **2**: From soci
…[truncated 41 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6233
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-19T07:53:13.861268+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-19T07:53:14.263412+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-19T07:53:14.264011+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-19T07:53:15.268869+00:00_

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
20	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}):
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathcal{E}|^2},
24	\end{equation}
25	%
26	The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
27	Tighter 
…[truncated 1297 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-19T07:53:15.269369+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-19T07:53:15.672763+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two complementary regimes.
8	Fine-tuning composability (\S\ref{sec:composability}) demonstrates deployment readiness: constraints compose losslessly with standard LoRA training at R-F1 40--46, our recommended configuration.
9	Zero-shot evaluation stress-tests constraint robustness under adversarial conditions (no task supervision, R-F1 2--8), where CF trade-offs are expected and documented (\S\ref{sec:cross-model}).
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliab
…[truncated 51 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-19T07:53:15.673349+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-19T07:53:15.724174+00:00_

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
…[truncated 5095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-19T07:53:20.195016+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-19T07:53:21.049241+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-19T07:53:21.049799+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-19T07:53:21.502001+00:00_

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
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-19T07:53:21.502395+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-19T07:53:21.954600+00:00_

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
…[truncated 2360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-19T07:53:22.005391+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-19T07:53:22.056810+00:00_

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
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models (Qwen, Llama) and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consistency check (\S\ref{sec:discussion}).
21	Model scale reduces
…[truncated 39 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-19T07:53:27.482576+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-19T07:53:27.784579+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, SynCode~\cite{ugare2024syncode}, and Grammar-Aligned Decoding~\cite{park2024grammar} guarantee format validity via CFG-based token masking; JSONSchemaBench~\cite{jsonschemabench2025} benchmarks these systems.
8	GCD~\cite{geng2023gcd} applies grammar constraints to IE tasks.
9	In code generation, PICARD~\cite{scholak2021picard} and Synchromesh~\cite{synchromesh_iclr2022} enforce type constraints via incremental parsing, and \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata.
10	These methods ensure syntactic or type-level validity but operate on static type declarations; IE requires a dynamic entity registry built during generation, where constraint targets depend on the co-occurring relation type.
11	OntoCoDec's grammar layer builds on XGrammar; its semantic layer extends constrained decoding from syntax to ontology-level type enforcement.
12	
13	\paragraph{Schema-aware IE.}
14	GoLLIE~\cite{sainz2024gollie} and KnowCoder~\cite{knowcoder_acl2024} encode ontology structure as Python dataclasses and train models to generate typed code.
15	InstructUIE~\cite{wang2023instructuie}, DeepStruct~\cite{wang2022deepstruct}, UIE~\cite{lu2022uie}, and USM~\cite{lou2023usm} unify extraction tasks via structured output formats with task-specific training.
16	UniversalNER~\cite{zhou2024universalner} achieves strong zero-shot NER via targeted distillation.
17	\citet{wadhwa2023revisiting} benchmark LLM-based RE and find persistent schema compliance gaps.
18	These methods internalize constraints through training; OntoCoDec enforces them at decoding time without retraining, and the two approaches are complementary (a GoLLIE-trained 
…[truncated 1203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-19T07:53:27.835535+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-19T07:53:27.936566+00:00_

1	% Section 7 — Discussion and Conclusion (maximally compressed)
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE ontology schemas into composable token-level decoding constraints.
5	The core finding is that ontology type constraints can be compiled into token-level masks that compose near-losslessly with standard fine-tuning: DR reaches $\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp on RE (R-F1 40--46), RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types for calibrated models (\S\ref{sec:beam-results}).
6	Under zero-shot decoding (R-F1 2--8\%), DR drops by 42--99\% across three models and three datasets with no significant F1 cost.
7	
8	CF remains an open challenge for per-slot enforcement: the current architecture enforces type constraints independently per relation slot, so the same entity can receive different type assignments across triples.
9	Global entity-level type consensus during decoding, where all slots referencing the same entity must agree on its type, offers the most direct resolution path.
10	
11	The framework applies to any autoregressive IE system without model modification or additional training: the constraint compiler takes an ontology schema as input and produces token-level masks compatible with any LM vocabulary.
12	This generality is validated across four models (8B--70B), three tokenizer families, and two IE tasks (RE, EE).
13	The interaction between constraint tightness and model calibration is consistent across three datasets but would benefit from validation on a broader range of ontologies and model scales.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-19T07:53:28.691457+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-19T07:53:28.894051+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-19T07:53:28.945013+00:00_

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
…[truncated 8172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-19T07:53:29.046659+00:00_

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
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 31971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-19T07:53:34.727233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-19T07:53:35.682123+00:00_

1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Grammar compilation scales sub-linearly (0.33\,s to 0.37\,s for 7$\to$1{,}000 relations); semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-19T07:53:35.732850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-19T07:53:36.638045+00:00_

1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, which confirms that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 604 · 2026-05-19T07:53:36.638420+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-19T07:53:36.789258+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, full S1 constraints).}
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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-19T07:53:36.840044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-19T07:53:36.890833+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (E
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-19T07:53:41.118955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-19T07:53:41.420731+00:00_

1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixe
…[truncated 5952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-19T07:53:41.571799+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-19T07:53:41.873740+00:00_

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
…[truncated 19750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-19T07:53:41.874253+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 613 · 2026-05-19T07:53:42.326931+00:00_

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
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 614 · 2026-05-19T07:53:42.327335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-19T07:53:42.378080+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-19T07:53:50.166643+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 617 · 2026-05-19T07:53:50.870253+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-19T07:54:41.043369+00:00_

&lt;persisted-output>
Output too large (56KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/a58c226f-7842-4f51-911b-b9f2f1f6d19d/tool-results/toolu_01VxmHgLHyTjhiVj1FX8NrfR.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 69, \"total_citations\": 90, \"unique_cited_keys\": 54, \"orphan_bib\": 14, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 53, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"cabot2021rebel\", \"dccd2026\", \"delafuente2025guidex\", \"geng2025jsonschemabench\", \"guidex2025\", \"lee2026formattax\", \"lu2025schemarl\", \"paolini2021tanl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"vukovic2024dore\"], \"missing_bib\": [], \"orphan_count\": 14, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 50876
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-19T07:54:41.044096+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50173
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-19T07:54:45.014488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/a58c226f-7842-4f51-911b-b9f2f1f6d19d/tool-results/toolu_01VxmHgLHyTjhiVj1FX8NrfR.txt",
  "limit": "100",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/a58c226f-7842-4f51-911b-b9f2f1f6d19d/tool-results/toolu_01VxmHgLHyTjhiVj1FX8NrfR.txt",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-19T07:54:45.270702+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 69, \"total_citations\": 90, \"unique_cited_keys\": 54, \"orphan_bib\": 14, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 53, \"online_not_found\": 4, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"cabot2021rebel\", \"dccd2026\", \"delafuente2025guidex\", \"geng2025jsonschemabench\", \"guidex2025\", \"lee2026formattax\", \"lu2025schemarl\", \"paolini2021tanl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"vukovic2024dore\"], \"missing_bib\": [], \"orphan_count\": 14, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational
…[truncated 55395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 256
}
```

</details>

---


### Tool call

_source line 622 · 2026-05-19T07:57:31.156228+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Summary\n\nOntoCoDec 提出了一个两层约束解码框架，将 IE 本体 schema 编译为 token 级别的 logit mask：grammar 层保证 JSON 结构和词汇有效性，semantic 层通过动态 entity registry 和 logit masking 执行 per-triple domain/range 类型约束。论文在 SciERC、DocRED（RE）和 WikiEvents（EE）上验证了该方法在 zero-shot 和 LoRA fine-tuning 下的有效性，覆盖 4 个模型（8B-70B）和 3 种 tokenizer。核心实验表明 DR 违约率在 fine-tuning 下降至 ≤0.20%，R-F1 变化在 ±0.6pp 以内。\n\n论文整体工程完成度很高，实验设计系统且诚实（特别是 CF 权衡的透明处理），但在方法 framing 的准确性、统计支撑的充分性、以及若干关键 claim 与证据的匹配度上存在需要修正的问题。\n\n---\n\n## Strengths\n\n**[S1] 形式化清晰、架构设计合理。** 两层约束的分解（grammar for structure, semantic for cross-field type constraints）具有良好的理论动机。Sequential masking（先 head type domain check → 再 tail type conditioned range check）保证了 pair-based enforcement，严格强于独立的 domain/range 检查。Non-rectangularity 分析（§4, Section 3.1 footnote: SciERC 7/7、DocRED 73/96 关系非矩形）为 sequential masking 的必要性提供了实证支撑。Enabling dependency 概念（semantic layer 依赖 grammar layer 保证的词汇有效性）通过 semantic-only 消融实验（DR 仅降 24%）得到了验证。\n\n**[S2] 系统且诚实的实验设计。** 五路消融（Table 1: unconstrained / grammar / semantic / S1 / S2）清楚地隔离了各层贡献。CF↔DR trade-off 公开展示（Appendix B, Table 6: CF fallback 消除 CF 但 DR 从 0.93% 升至 14.78%），没有回避局限性。Cross-model 验证覆盖 3 个模型和 2 个数据集，Mistral 作为 boundary condition 的诚实处理（§5.3）展示了方法的适用边界。Beam search、sampling、prompt sensitivity 等鲁棒性实验也较为全面。\n\n**[S3] 实用价值明确。** Training-free，运行时开销低（SciERC +13.1%，DocRED +2.43%），跨 tokenizer 兼容（byte-level BPE 和 SentencePiece），scalability 测试到 200 entity types / 1000 relations 仍保持 2-3% overhead。与 LoRA 的 composability 结果（DR ≤ 0.20%，R-F1 ±0.6pp）证明了部署可行性。\n\n**[S4] 充分的附录支撑。** 错误分析（Appendix B: 36 个残余 DR 违约的 4 类根因分解）、case studies（4 个代表性案例）、doc-length 分析、per-relation 分解等都增强了可信度。Fine-tuned four-way ablation（Appendix Table 9）额外验证了 fine-tuning 后 grammar 层成为 no-op 而 semantic 层独自承担 DR 防御的结论。\n\n---\n\n## Weaknesses\n\n**[W1] [Must-Fix] \"Ontology Constraints\" framing 与实际实现不匹配。**\n- 具体位置：Title, Abstract line 2 (\"compiles IE ontology schemas\"), §2 lines 11-13, §5 Setup\n- 问题：论文标题为 \"Compiled **Ontology** Constraints\"，Abstract 说 \"compiles Information Extraction (IE) **ontology schemas**\"，但 SciERC 和 DocRED 的约束表是从训练数据的类型对共现中自动提取的——这不是本体（ontology），而是基于频率统计的经验约束。只有 WikiEvents 使用了真正的形式本体（KAIROS）。§2 Background 第一段承认了这一点（\"empirically derived type-pair constraints extracted from annotated training data\"），但标题和 Abstract 的措辞强烈暗示了从形式本体编译。\n- 为什么影响接收：审稿人会质疑核心 framing 的诚实性。\"Ontology\" 一词在 NLP/KG 领域有特定含义（形式化的概念层次和公理系统）；将训练集统计称为 \"ontology constraints\" 是 overclaiming。§2 提到 99%+ 的 instance-level coverage，但这实际上意味着约束表可能存在 coverage gap（§7 Limitations: \"schema coverage gaps (one-third of residual violations)\"），而真正的本体约束不应有此问题。\n- 建议修改方向：(1) 将标题和 Abstract 中的 \"ontology\" 替换为更准确的术语（如 \"schema constraints\" 或 \"type constraints\"），或 (2) 在 Abstract/Introduction 中明确区分两种约束来源（formal ontology vs. empirically extracted），强调方法对两者的统一处理是贡献之一，而非隐含所有约束都来自形式本体。\n\n**[W2] [Must-Fix] Dual-factor pattern 的统计支撑不足以支撑其在论文中的 prominence。**\n- 具体位置：§4 Constraint Tightness, Appendix B \"Dual-Factor Quantitative Analysis\" (Figure 2, n=4, p≈0.058)\n- 问题：Constraint tightness κ(r) 与 baseline violation rate 的乘积预测残余 DR 的 dual-factor pattern 是论文叙事的核心组件（§1 Contribution #1, §4, §5.2-5.4 反复引用），但该线性关系仅基于 n=4 个 calibrated model×dataset 组合拟合，df=2，p≈0.058 > 0.05。论文自己承认是 \"descriptive characterization rather than a confirmatory statistical test\"（Appendix B），但在正文中将其作为解释框架反复使用，读者容易将其误读为已验证的规律。\n- 为什么影响接收：将 n=4 的描述性趋势提升为论文的核心贡献之一（Contribution #1），在统计上不够严谨。审稿人期望要么 (a) 有更多数据点支撑（更多模型或数据集），要么 (b) 在行文中明确降低该 pattern 的 claim 强度。\n- 建议修改方向：(1) 增加 1-2 个数据集或模型以增加 n，或 (2) 在 §1 Contribution #1 和 §4 中明确标注为 \"empirical observation\" 而非 \"systematic study\"，避免读者将其理解为已确认的因果关系。\n\n**[W3] [Must-Fix] WikiEvents EE 结果标注为 \"preliminary\" 但在 Abstract/Contribution 中权重过高。**\n- 具体位置：Abstract line 10 (\"The framework extends to event extraction without modification\"), §1 Contribution #4, Table 5, §5.5, Limitations §\"Evaluation coverage\" line 81\n- 问题：WikiEvents fine-tuning composability 基于 20 个测试文档（论文承认是 \"a dataset constraint, not a design choice\"），zero-shot 评估 246 个文档但 F1 极低（Trigger F1 2-13%）。Limitations 明确标注为 \"preliminary\"。然而，Abstract 用一整句话突出 EE extension，§1 将其列为 Contribution #4（\"Preliminary extension to event extraction (WikiEvents, 20-document test set): vocabulary violations eliminated without architectural modification; fine-tuning composability analysis\"）——虽然标注了 \"preliminary\"，但作为正式 Contribution 列出仍赋予了过高权重。\n- 为什么影响接收：审稿人会质疑：如果 EE 结果本身被作者认为是 preliminary，为何将其列为 Contribution？20-document test set 的 trigger F1 CI 非常宽（论文提到 \"wide confidence intervals at this sample size\"），fine-tuning composability 的可信度有限。\n- 建议修改方向：(1) 将 EE 从 Contribution #4 降级为 Discussion 中的初步验证，或 (2) 在 Contribution 列表中将其与 RE 结果明确分层（如 \"Additionally, we provide preliminary evidence that...\"），并在 Abstract 中减少 EE 的篇幅。\n\n**[W4] [Should-Fix] 缺少关键 baseline 对比。**\n- 具体位置：§6 Related Work, §5 Experiments\n- 问题：\n  (a) **GoLLIE / KnowCoder**：论文在 §6 讨论了与 GoLLIE 和 KnowCoder 的互补性（\"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"），但未提供任何实证验证。这是论文 positioning 的核心论点之一（training-based + decoding-time = complementary），缺少实验支撑是显著缺口。\n  (b) **显式 GCD baseline**：Grammar-only 消融（Table 1, Table 3）可视为 GCD 上界，但 GCD [Geng et al., 2023] 使用 input-dependent grammar，可能比简单的 JSON Schema grammar 更强。论文没有与 GCD 的官方实现做公平对比。\n  (c) **Post-hoc filtering 在 F1 上赢了**：Table 10 显示 post-hoc filtering 在 5/6 zero-shot 和 2/4 fine-tuned 设置中 F1 更高。论文的论点是 recall preservation，这合理但应更突出地讨论这一 trade-off。\n- 建议：(1) 至少提供 GoLLIE 在 SciERC 上的残余违约率数据作为 complementarity 的间接证据；(2) 与 GCD 做 head-to-head 对比；(3) 在 §5 主表中直接包含 post-hoc filtering 结果而非仅放附录。\n\n**[W5] [Should-Fix] \"Near-lossless composability\" claim 在考虑 CF 后需要重新审视。**\n- 具体位置：Abstract line 7 (\"near-lossless composability\"), §1 Contribution #3, §7 Conclusion\n- 问题：\"Near-lossless composability\" 的量化标准是 \"DR ≤ 0.20% with R-F1 within ±0.6pp\"——但 CF 从 0% 升至 1.18%（fine-tuning）或 9.90%（zero-shot SciERC）。如果 \"lossless\" 仅指 DR 和 F1，那应当明确说明 CF 不在此 claim 范围内；如果审稿人将 CF 也视为 loss（它确实是一种新引入的违约），则 \"near-lossless\" 不成立。Table 1 中 Tot. (DR+CF) 从 unconstrained 15.45% 降至 constrained 10.83%——总违约确实降了，但 CF 从 0.08% 暴涨至 9.90%。\n- 建议：在 Abstract 和 Contribution 中将 \"near-lossless composability\" 的定义范围明确限定为 \"near-lossless in DR and F1\"，并在同一句中 acknowledge CF trade-off。\n\n**[W6] [Should-Fix] DocRED beam search 仅 50 文档，claim 偏强。**\n- 具体位置：§5.6 Beam search compatibility, Table 7, Appendix D\n- 问题：DocRED beam search 评估使用 50 文档子集（vs. 998 full dev set for greedy），论文给出 Clopper-Pearson 95% CI 上限 5.8%。对于 \"eliminates DR on DocRED\" 的 claim，5.8% 的上限意味着真实 DR 可能非零。论文在 Appendix 中是诚实的，但 §5.6 主文中的措辞（\"beam search eliminates all four violation types on SciERC for both Qwen and Llama\"）可能被误读为包含 DocRED。\n- 建议：(1) §5.6 中明确区分 SciERC（551 docs, complete）和 DocRED（50 docs, subset）的 claim 强度，或 (2) 在 full DocRED dev set 上运行 beam search。\n\n**[W7] [Should-Fix] Zero-shot regime 占据了大量实验空间，但实用价值有限。**\n- 具体位置：§5 整体结构, Tables 1-4\n- 问题：Zero-shot R-F1 约 2-8%，实际不可部署。论文将其定位为 \"stress-test constraint robustness under adversarial conditions\"（§5 Setup），这个 framing 合理，但：(a) §5 的 4 个 subsection 中有 3 个主要展示 zero-shot 结果（Tables 1-4），composability 仅占 1 段 + Table 2；(b) Abstract 给 zero-shot 和 fine-tuned 大致相等的篇幅。建议平衡：fine-tuning composability 是论文的核心 practical value，应在 §5 中给予更多空间。\n- 建议：考虑将 fine-tuning composability 提升为独立 subsection，而非嵌入 SciERC results 中。\n\n**[W8] [Minor] Bootstrap CI 未在主表中报告。**\n- 具体位置：Tables 1-5\n- 问题：论文提到 \"Bootstrap: 10,000 iterations\"（Table 1 caption）并在文中报告个别 p 值，但主表只有点估计。F1 差异很小（±0.6pp），没有 CI 无法判断统计意义。\n\n**[W9] [Minor] BibTeX 有 14 个 orphan entries 和若干重复。**\n- 引用验证发现：14 个 bib entries 未被引用（cabot2021rebel, paolini2021tanl 等）；存在重复条目（formattax2026/lee2026formattax, dccd2026/reddy2026dccd, slot2025/shen2025slot 等是同一论文的两个 key）；1 个 duplicate key (schall2025hiddencost)。这是编辑问题，不影响学术内容，但应在提交前清理。\n\n---\n\n## Questions\n\n**[Q1]** Entity registry 中的错误如何传播？如果生成过程早期为某实体分配了错误类型（如 \"Amorph\" 被标为 OtherScientificTerm），后续所有引用该实体的 relation 都会基于此错误类型做 domain/range 检查。Case Study 4 (Appendix E.4) 展示了这种 trajectory divergence，但论文未系统量化错误传播的频率和影响。\n\n**[Q2]** 对于真正具有多义类型的实体（如某实体在不同上下文中确实可以是 Method 或 Task），当前的 entity registry 设计是否过于刚性？Per-slot enforcement 强制一致性（CF 违约），但某些 CF 可能反映了合法的类型多义性而非错误。论文是否考虑过区分 \"true CF\"（错误）和 \"legitimate polymorphism\"（合法多义）？\n\n**[Q3]** Constraint tightness κ(r) = 1 - |σ(r)|/|E|² 使用 |E|² 作为分母，但有些 (head_type, tail_type) 组合在任何关系中都不出现。是否考虑过更 informative 的归一化方式（如只除以实际出现过的类型对数量）？\n\n**[Q4]** 论文声称与 GoLLIE 等 training-based 方法互补，但未提供实验证据。GoLLIE 在 SciERC 上的零样本 RE 表现如何？其残余违约率是多少？如果 GoLLIE 的违约率已经很低（因为训练中隐式学了类型约束），OntoCoDec 的增量价值可能有限。\n\n---\n\n## Missing References\n\n- **BoostCD** [Sakota et al., 2025]：论文引用了但未在实验中对比。BoostCD 结合 constrained 和 unconstrained decoding for IE，是最直接的方法论竞品。\n- **SchemaRL** [Lu et al., 2025]：bib 中存在但未被引用。Schema Reinforcement Learning 通过 RL 学习满足 schema 约束的生成策略，与 OntoCoDec 的 training-free 方法形成对比。\n- **GUIDEX** [De La Fuente et al., 2025]：bib 中存在但未被引用。零样本 IE 的 synthetic data 方法，与论文的零样本实验设置相关。\n- 建议增加：近期 LLM-based RE 的 SOTA 结果引用（如 ADELIE 在 SciERC/DocRED 上的 fine-tuned F1），以便读者 calibrate 论文报告的 F1 数字。\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\n论文提出了一个技术上合理、工程上实用的两层约束解码框架，实验设计系统且诚实，附录充实。核心问题是：(1) \"ontology constraints\" 的 framing 与实际实现（训练集统计提取）之间存在不匹配，这是标题级别的 overclaim；(2) dual-factor pattern 作为 Contribution #1 的统计支撑（n=4, p=0.058）不够；(3) WikiEvents preliminary 结果在 Abstract/Contribution 中的权重过高。如果这三个 framing 问题得到修正（更准确的术语、降低 dual-factor 的 claim 强度、调整 EE 的呈现层级），论文的技术贡献（composable constraint enforcement for IE）在 constrained decoding 子领域是有价值的。缺少 GoLLIE/GCD 的直接对比是实验上的较大遗憾，但不是致命缺陷。\n\n当前版本 Borderline Conference：核心方法可靠、实验充实，但 framing 需要校准以准确反映实际贡献的边界。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Summary\n\nOntoCoDec 提出了一个两层约束解码框架，将 IE 本体 schema 编译为 token 级别的 logit mask：grammar 层保证 JSON 结构和词汇有效性，semantic 层通过动态 entity registry 和 logit masking 执行 per-triple domain/range 类型约束。论文在 SciERC、DocRED（RE）和 WikiEvents（EE）上验证了该方法在 zero-shot 和 LoRA fine-tuning 下的有效性，覆盖 4 个模型（8B-70B）和 3 种 tokenizer。核心实验表明 DR 违约率在 fine-tuning 下降至 ≤0.20%，R-F1 变化在 ±0.6pp 以内。\n\n论文整体工程完成度很高，实验设计系统且诚实（特别是 CF 权衡的透明处理），但在方法 framing 的准确性、统计支撑的充分性、以及若干关键 claim 与证据的匹配度上存在需要修正的问题。\n\n---\n\n## Strengths\n\n**[S1] 形式化清晰、架构设计合理。** 两层约束的分解（grammar for structure, semantic for cross-field type constraints）具有良好的理论动机。Sequential masking（先 head type domain check → 再 tail type conditioned range check）保证了 pair-based enforcement，严格强于独立的 domain/range 检查。Non-rectangularity 分析（§4, Section 3.1 footnote: SciERC 7/7、DocRED 73/96 关系非矩形）为 sequential masking 的必要性提供了实证支撑。Enabling dependency 概念（semantic layer 依赖 grammar layer 保证的词汇有效性）通过 semantic-only 消融实验（DR 仅降 24%）得到了验证。\n\n**[S2] 系统且诚实的实验设计。** 五路消融（Table 1: unconstrained / grammar / semantic / S1 / S2）清楚地隔离了各层贡献。CF↔DR trade-off 公开展示（Appendix B, Table 6: CF fallback 消除 CF 但 DR 从 0.93% 升至 14.78%），没有回避局限性。Cross-model 验证覆盖 3 个模型和 2 个数据集，Mistral 作为 boundary condition 的诚实处理（§5.3）展示了方法的适用边界。Beam search、sampling、prompt sensitivity 等鲁棒性实验也较为全面。\n\n**[S3] 实用价值明确。** Training-free，运行时开销低（SciERC +13.1%，DocRED +2.43%），跨 tokenizer 兼容（byte-level BPE 和 SentencePiece），scalability 测试到 200 entity types / 1000 relations 仍保持 2-3% overhead。与 LoRA 的 composability 结果（DR ≤ 0.20%，R-F1 ±0.6pp）证明了部署可行性。\n\n**[S4] 充分的附录支撑。** 错误分析（Appendix B: 36 个残余 DR 违约的 4 类根因分解）、case studies（4 个代表性案例）、doc-length 分析、per-relation 分解等都增强了可信度。Fine-tuned four-way ablation（Appendix Table 9）额外验证了 fine-tuning 后 grammar 层成为 no-op 而 semantic 层独自承担 DR 防御的结论。\n\n---\n\n## Weaknesses\n\n**[W1] [Must-Fix] \"Ontology Constraints\" framing 与实际实现不匹配。**\n- 具体位置：Title, Abstract line 2 (\"compiles IE ontology schemas\"), §2 lines 11-13, §5 Setup\n- 问题：论文标题为 \"Compiled **Ontology** Constraints\"，Abstract 说 \"compiles Information Extraction (IE) **ontology schemas**\"，但 SciERC 和 DocRED 的约束表是从训练数据的类型对共现中自动提取的——这不是本体（ontology），而是基于频率统计的经验约束。只有 WikiEvents 使用了真正的形式本体（KAIROS）。§2 Background 第一段承认了这一点（\"empirically derived type-pair constraints extracted from annotated training data\"），但标题和 Abstract 的措辞强烈暗示了从形式本体编译。\n- 为什么影响接收：审稿人会质疑核心 framing 的诚实性。\"Ontology\" 一词在 NLP/KG 领域有特定含义（形式化的概念层次和公理系统）；将训练集统计称为 \"ontology constraints\" 是 overclaiming。§2 提到 99%+ 的 instance-level coverage，但这实际上意味着约束表可能存在 coverage gap（§7 Limitations: \"schema coverage gaps (one-third of residual violations)\"），而真正的本体约束不应有此问题。\n- 建议修改方向：(1) 将标题和 Abstract 中的 \"ontology\" 替换为更准确的术语（如 \"schema constraints\" 或 \"type constraints\"），或 (2) 在 Abstract/Introduction 中明确区分两种约束来源（formal ontology vs. empirically extracted），强调方法对两者的统一处理是贡献之一，而非隐含所有约束都来自形式本体。\n\n**[W2] [Must-Fix] Dual-factor pattern 的统计支撑不足以支撑其在论文中的 prominence。**\n- 具体位置：§4 Constraint Tightness, Appendix B \"Dual-Factor Quantitative Analysis\" (Figure 2, n=4, p≈0.058)\n- 问题：Constraint tightness κ(r) 与 baseline violation rate 的乘积预测残余 DR 的 dual-factor pattern 是论文叙事的核心组件（§1 Contribution #1, §4, §5.2-5.4 反复引用），但该线性关系仅基于 n=4 个 calibrated model×dataset 组合拟合，df=2，p≈0.058 > 0.05。论文自己承认是 \"descriptive characterization rather than a confirmatory statistical test\"（Appendix B），但在正文中将其作为解释框架反复使用，读者容易将其误读为已验证的规律。\n- 为什么影响接收：将 n=4 的描述性趋势提升为论文的核心贡献之一（Contribution #1），在统计上不够严谨。审稿人期望要么 (a) 有更多数据点支撑（更多模型或数据集），要么 (b) 在行文中明确降低该 pattern 的 claim 强度。\n- 建议修改方向：(1) 增加 1-2 个数据集或模型以增加 n，或 (2) 在 §1 Contribution #1 和 §4 中明确标注为 \"empirical observation\" 而非 \"systematic study\"，避免读者将其理解为已确认的因果关系。\n\n**[W3] [Must-Fix] WikiEvents EE 结果标注为 \"preliminary\" 但在 Abstract/Contribution 中权重过高。**\n- 具体位置：Abstract line 10 (\"The framework extends to event extraction without modification\"), §1 Contribution #4, Table 5, §5.5, Limitations §\"Evaluation coverage\" line 81\n- 问题：WikiEvents fine-tuning composability 基于 20 个测试文档（论文承认是 \"a dataset constraint, not a design choice\"），zero-shot 评估 246 个文档但 F1 极低（Trigger F1 2-13%）。Limitations 明确标注为 \"preliminary\"。然而，Abstract 用一整句话突出 EE extension，§1 将其列为 Contribution #4（\"Preliminary extension to event extraction (WikiEvents, 20-document test set): vocabulary violations eliminated without architectural modification; fine-tuning composability analysis\"）——虽然标注了 \"preliminary\"，但作为正式 Contribution 列出仍赋予了过高权重。\n- 为什么影响接收：审稿人会质疑：如果 EE 结果本身被作者认为是 preliminary，为何将其列为 Contribution？20-document test set 的 trigger F1 CI 非常宽（论文提到 \"wide confidence intervals at this sample size\"），fine-tuning composability 的可信度有限。\n- 建议修改方向：(1) 将 EE 从 Contribution #4 降级为 Discussion 中的初步验证，或 (2) 在 Contribution 列表中将其与 RE 结果明确分层（如 \"Additionally, we provide preliminary evidence that...\"），并在 Abstract 中减少 EE 的篇幅。\n\n**[W4] [Should-Fix] 缺少关键 baseline 对比。**\n- 具体位置：§6 Related Work, §5 Experiments\n- 问题：\n  (a) **GoLLIE / KnowCoder**：论文在 §6 讨论了与 GoLLIE 和 KnowCoder 的互补性（\"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"），但未提供任何实证验证。这是论文 positioning 的核心论点之一（training-based + decoding-time = complementary），缺少实验支撑是显著缺口。\n  (b) **显式 GCD baseline**：Grammar-only 消融（Table 1, Table 3）可视为 GCD 上界，但 GCD [Geng et al., 2023] 使用 input-dependent grammar，可能比简单的 JSON Schema grammar 更强。论文没有与 GCD 的官方实现做公平对比。\n  (c) **Post-hoc filtering 在 F1 上赢了**：Table 10 显示 post-hoc filtering 在 5/6 zero-shot 和 2/4 fine-tuned 设置中 F1 更高。论文的论点是 recall preservation，这合理但应更突出地讨论这一 trade-off。\n- 建议：(1) 至少提供 GoLLIE 在 SciERC 上的残余违约率数据作为 complementarity 的间接证据；(2) 与 GCD 做 head-to-head 对比；(3) 在 §5 主表中直接包含 post-hoc filtering 结果而非仅放附录。\n\n**[W5] [Should-Fix] \"Near-lossless composability\" claim 在考虑 CF 后需要重新审视。**\n- 具体位置：Abstract line 7 (\"near-lossless composability\"), §1 Contribution #3, §7 Conclusion\n- 问题：\"Near-lossless composability\" 的量化标准是 \"DR ≤ 0.20% with R-F1 within ±0.6pp\"——但 CF 从 0% 升至 1.18%（fine-tuning）或 9.90%（zero-shot SciERC）。如果 \"lossless\" 仅指 DR 和 F1，那应当明确说明 CF 不在此 claim 范围内；如果审稿人将 CF 也视为 loss（它确实是一种新引入的违约），则 \"near-lossless\" 不成立。Table 1 中 Tot. (DR+CF) 从 unconstrained 15.45% 降至 constrained 10.83%——总违约确实降了，但 CF 从 0.08% 暴涨至 9.90%。\n- 建议：在 Abstract 和 Contribution 中将 \"near-lossless composability\" 的定义范围明确限定为 \"near-lossless in DR and F1\"，并在同一句中 acknowledge CF trade-off。\n\n**[W6] [Should-Fix] DocRED beam search 仅 50 文档，claim 偏强。**\n- 具体位置：§5.6 Beam search compatibility, Table 7, Appendix D\n- 问题：DocRED beam search 评估使用 50 文档子集（vs. 998 full dev set for greedy），论文给出 Clopper-Pearson 95% CI 上限 5.8%。对于 \"eliminates DR on DocRED\" 的 claim，5.8% 的上限意味着真实 DR 可能非零。论文在 Appendix 中是诚实的，但 §5.6 主文中的措辞（\"beam search eliminates all four violation types on SciERC for both Qwen and Llama\"）可能被误读为包含 DocRED。\n- 建议：(1) §5.6 中明确区分 SciERC（551 docs, complete）和 DocRED（50 docs, subset）的 claim 强度，或 (2) 在 full DocRED dev set 上运行 beam search。\n\n**[W7] [Should-Fix] Zero-shot regime 占据了大量实验空间，但实用价值有限。**\n- 具体位置：§5 整体结构, Tables 1-4\n- 问题：Zero-shot R-F1 约 2-8%，实际不可部署。论文将其定位为 \"stress-test constraint robustness under adversarial conditions\"（§5 Setup），这个 framing 合理，但：(a) §5 的 4 个 subsection 中有 3 个主要展示 zero-shot 结果（Tables 1-4），composability 仅占 1 段 + Table 2；(b) Abstract 给 zero-shot 和 fine-tuned 大致相等的篇幅。建议平衡：fine-tuning composability 是论文的核心 practical value，应在 §5 中给予更多空间。\n- 建议：考虑将 fine-tuning composability 提升为独立 subsection，而非嵌入 SciERC results 中。\n\n**[W8] [Minor] Bootstrap CI 未在主表中报告。**\n- 具体位置：Tables 1-5\n- 问题：论文提到 \"Bootstrap: 10,000 iterations\"（Table 1 caption）并在文中报告个别 p 值，但主表只有点估计。F1 差异很小（±0.6pp），没有 CI 无法判断统计意义。\n\n**[W9] [Minor] BibTeX 有 14 个 orphan entries 和若干重复。**\n- 引用验证发现：14 个 bib entries 未被引用（cabot2021rebel, paolini2021tanl 等）；存在重复条目（formattax2026/lee2026formattax, dccd2026/reddy2026dccd, slot2025/shen2025slot 等是同一论文的两个 key）；1 个 duplicate key (schall2025hiddencost)。这是编辑问题，不影响学术内容，但应在提交前清理。\n\n---\n\n## Questions\n\n**[Q1]** Entity registry 中的错误如何传播？如果生成过程早期为某实体分配了错误类型（如 \"Amorph\" 被标为 OtherScientificTerm），后续所有引用该实体的 relation 都会基于此错误类型做 domain/range 检查。Case Study 4 (Appendix E.4) 展示了这种 trajectory divergence，但论文未系统量化错误传播的频率和影响。\n\n**[Q2]** 对于真正具有多义类型的实体（如某实体在不同上下文中确实可以是 Method 或 Task），当前的 entity registry 设计是否过于刚性？Per-slot enforcement 强制一致性（CF 违约），但某些 CF 可能反映了合法的类型多义性而非错误。论文是否考虑过区分 \"true CF\"（错误）和 \"legitimate polymorphism\"（合法多义）？\n\n**[Q3]** Constraint tightness κ(r) = 1 - |σ(r)|/|E|² 使用 |E|² 作为分母，但有些 (head_type, tail_type) 组合在任何关系中都不出现。是否考虑过更 informative 的归一化方式（如只除以实际出现过的类型对数量）？\n\n**[Q4]** 论文声称与 GoLLIE 等 training-based 方法互补，但未提供实验证据。GoLLIE 在 SciERC 上的零样本 RE 表现如何？其残余违约率是多少？如果 GoLLIE 的违约率已经很低（因为训练中隐式学了类型约束），OntoCoDec 的增量价值可能有限。\n\n---\n\n## Missing References\n\n- **BoostCD** [Sakota et al., 2025]：论文引用了但未在实验中对比。BoostCD 结合 constrained 和 unconstrained decoding for IE，是最直接的方法论竞品。\n- **SchemaRL** [Lu et al., 2025]：bib 中存在但未被引用。Schema Reinforcement Learning 通过 RL 学习满足 schema 约束的生成策略，与 OntoCoDec 的 training-free 方法形成对比。\n- **GUIDEX** [De La Fuente et al., 2025]：bib 中存在但未被引用。零样本 IE 的 synthetic data 方法，与论文的零样本实验设置相关。\n- 建议增加：近期 LLM-based RE 的 SOTA 结果引用（如 ADELIE 在 SciERC/DocRED 上的 fine-tuned F1），以便读者 calibrate 论文报告的 F1 数字。\n\n---\n\n## Overall Assessment\n\n**Score: 3.5 (Borderline Conference)**\n**Confidence: 4/5**\n\n论文提出了一个技术上合理、工程上实用的两层约束解码框架，实验设计系统且诚实，附录充实。核心问题是：(1) \"ontology constraints\" 的 framing 与实际实现（训练集统计提取）之间存在不匹配，这是标题级别的 overclaim；(2) dual-factor pattern 作为 Contribution #1 的统计支撑（n=4, p=0.058）不够；(3) WikiEvents preliminary 结果在 Abstract/Contribution 中的权重过高。如果这三个 framing 问题得到修正（更准确的术语、降低 dual-factor 的 claim 强度、调整 EE 的呈现层级），论文的技术贡献（composable constraint enforcement for IE）在 constrained decoding 子领域是有价值的。缺少 GoLLIE/GCD 的直接对比是实验上的较大遗憾，但不是致命缺陷。\n\n当前版本 Borderline Conference：核心方法可靠、实验充实，但 framing 需要校准以准确反映实际贡献的边界。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-19T07:57:35.658538+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4502
}
```

</details>

---


### Assistant

_source line 624 · 2026-05-19T07:57:43.798950+00:00_

审稿意见已提交给 Review Director。

总结：评分 **3.5 (Borderline Conference)**，Confidence 4/5。

核心问题三项 Must-Fix：
1. **"Ontology Constraints" framing 不匹配**：SciERC/DocRED 的约束来自训练集统计而非形式本体，标题级别的 overclaim
2. **Dual-factor pattern 统计支撑不足**：n=4, p≈0.058，不足以作为 Contribution #1
3. **WikiEvents preliminary 结果权重过高**：20-document test set 被列为正式 Contribution

四项 Should-Fix：缺少 GoLLIE/GCD 直接对比、"near-lossless" claim 未充分考虑 CF、DocRED beam search 仅 50 docs、zero-shot vs fine-tuned 实验空间失衡。

方法本身技术可靠，实验系统且诚实（特别是 CF trade-off 的透明处理），修正 framing 问题后有 Conference 潜力。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 17

## Round 17

4 recorded events


### User

_source line 625 · 2026-05-19T08:01:25.729552+00:00_

[Round 10 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见

以下是 Reviewer 2 的完整审稿意见。请逐条回应每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
  
---

### Reviewer 2 Weaknesses:

**[W1] [Must-Fix] 缺少 Responsible NLP Research Checklist。**
ARR 硬性要求，缺失可能导致 desk reject。

**[W2] [Should-Fix] Zero-shot 下 CF trade-off 削弱核心 claim。**
SciERC Tot. 15.45%→10.83%，DocRED 18.56%→12.78%。"Type-constrained" 承诺在 ZS 下部分落空。Abstract 对 CF 的提及读起来像解释局限而非讲故事。

**[W3] [Should-Fix] 新颖性偏增量。**
Grammar layer 复用 XGrammar，semantic layer 的 prefix-conditioned logit masking + entity registry 是已有范式向 IE 的移植。Appendix B 自己承认 PLDI 2025 work 是 "closest mechanistic analog"，区别仅在于动态 entity registry。

**[W4] [Should-Fix] WikiEvents 评估过于初步。**
20-doc test set，trigger F1 shift -5.4pp 不具统计意义。列入 Contribution 可能误导。

**[W5] [Should-Fix] 缺少下游任务评估。**
以 type safety 为核心卖点但无 KG construction/QA 等端到端评估。

**[W6] [Should-Fix] §7 Discussion and Conclusion 过短。**
~150 words，缺少与 supervised SOTA 的对比讨论、使用指导、方法组合路线图。

**[W7] [Minor] Abstract 数据密度过高。**
~190 words 中 10+ 数字/百分比。

**[W8] [Minor] BibTeX orphan/duplicate。**

**[W9] [Minor] Dual-factor pattern 统计基础薄弱。**

### Reviewer 2 Questions:

**[Q1]** κ(r) 归一化：对称关系是否应使用 |E|×(|E|+1)/2？
**[Q2]** Table 2 为何不包含 DocRED FT 的完整数据？
**[Q3]** 约束为何增加 parse failure（Llama 9.1% vs 6.8%）？
**[Q4]** WikiEvents Qwen trigger F1 下降 5.4pp 的原因？

### Reviewer 2 Novelty Concern:
R2 认为新颖性偏增量，核心是已有 constrained decoding 技术向 IE 的移植。Excitement 评分 3.0/5。你是否同意这一评价？

---

请对每条 Weakness 和 Question 给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 626 · 2026-05-19T08:03:01.537322+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 交叉回应：Reviewer 2 审稿意见\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 缺少 Responsible NLP Research Checklist。**\n完全同意。我在审稿时也检查了 main.tex（lines 63-96），确认论文包含 Limitations section 和 Ethics Statement，但没有 ARR 要求的 Responsible NLP Research Checklist。这是 ARR 硬性要求，缺失确实可能导致 desk reject。属于纯格式合规问题，修复成本低但优先级最高。\n\n**[AGREE] R2-W2: Zero-shot 下 CF trade-off 削弱核心 claim。**\n同意，且这与我的 W5 相呼应。补充证据：Table 1 中 Tot. (DR+CF) 从 15.45% 降至 10.83%，降幅仅 30%；Table 3 DocRED 从 18.56% 降至 12.78%，降幅 31%。但 Llama DocRED (Table 4) 更严重：DR 26.07%→2.55% 的同时 CF 从 0.17% 暴涨至 12.02%，Tot. 从 26.24% 仅降至 14.57%。\n\n不过需要补充一点 nuance：论文在 §5 Setup 中明确将 zero-shot 定位为 \"stress-tests constraint robustness under adversarial conditions (no task supervision, R-F1 2-8), where CF trade-offs are expected and documented\"。Fine-tuning regime 下 CF 降至 ≤1.18%（Table 2），Tot. 显著改善。所以 R2 的批评对 zero-shot 完全成立，但论文推荐的部署配置（LoRA + S1）确实实现了 near-lossless。建议作者在 Abstract 中更清晰地分层：fine-tuning = deployment claim, zero-shot = robustness diagnostic。\n\n**[REBUT] R2-W3: 新颖性偏增量。**\n部分不同意。R2 将 OntoCoDec 定性为 \"已有范式向 IE 的移植\" 低估了 IE 场景的独特技术挑战。具体反驳：\n\n1. **动态 entity registry 不是简单适配。** 代码生成中的类型系统是静态声明的（变量类型在编译时已知），而 IE 的 entity registry 在生成过程中动态构建——每个新实体被解码后才加入 registry，后续 relation 的 constraint target 依赖于已解码的 prefix（§3.1 \"unlike type-constrained code generation where types are statically declared, IE requires a dynamic entity registry built during generation\"）。这不是 engineering detail，而是 fundamentally different constraint structure。\n\n2. **Grammar-first fallback 及其产生的 CF↔DR trade-off 是 IE-specific 的发现。** PLDI 2025 的代码类型系统不存在 cross-field consistency 问题（每个变量只有一个类型声明），而 IE 中同一实体可出现在多个 triple 中，产生了 per-relation enforcement vs. global consistency 的张力。Appendix B 的 CF-DR trade-off analysis（Table 6）揭示了 composable constraint system 的 fundamental tension，这是本文的分析贡献，不是移植可以获得的。\n\n3. **Pair-based sequential masking 的必要性分析是新的。** §4 Non-Rectangularity 分析（SciERC 7/7、DocRED 73/96 关系非矩形，独立检查会引入 33-37% spurious pairs）在 constrained decoding 文献中未见讨论。\n\n4. **Constraint tightness 作为跨数据集行为预测器。** 虽然 n=4 的统计支撑不足（我在 W2 中已指出），但 tightness 概念本身为理解 constrained decoding 在不同 schema 上的表现差异提供了分析工具。\n\n综合判断：核心机制确实与 code-generation constrained decoding 有 mechanistic analogy，但 IE-specific 的挑战（dynamic registry, CF trade-off, non-rectangularity）构成了实质性的技术贡献。Excitement 3.0/5 可能偏低，我认为 3.5 更合理——不是开创性的新范式，但在 constrained decoding 应用于 IE 的具体问题上有明确增量。\n\n**[AGREE] R2-W4: WikiEvents 评估过于初步。**\n完全同意，与我的 W3 一致。补充：§5.5 自己报告 \"trigger F1 shows larger shifts (−5.4/−0.6 pp) with wide confidence intervals at this sample size\"。20 个测试文档的 bootstrap CI 对 trigger F1 的变化方向都无法确定。将其列为 Contribution #4 确实可能误导。\n\n**[REBUT] R2-W5: 缺少下游任务评估。**\n部分不同意。R2 的理想化要求（KG construction / QA 端到端评估）虽然有价值，但超出了本文的合理 scope：\n\n1. **论文的 contribution 是 constraint enforcement method，不是 end-to-end IE system。** §1 明确定义了问题：\"ensuring type-valid triples during autoregressive generation\"。Type validity 是一个 well-defined 的形式化目标，不依赖下游任务来定义其价值——ontologically invalid triple 无论在什么下游场景中都是 invalid。\n\n2. **下游影响需要额外的实验基础设施。** KG construction 评估需要完整的 entity linking + graph merging pipeline；QA 评估需要构建 QA 系统。这些是独立的研究问题，要求在本文中完成不合理。\n\n3. **论文已经在 Limitations 中 acknowledge 了这一点**（§Limitations line 71: \"CF type inconsistencies may propagate to downstream tasks...the impact of such propagation has not been evaluated\"），这是诚实且适当的处理。\n\n建议作者在 Discussion 中增加 1-2 句话 frame 下游评估为 future work，但不应作为 must-fix。\n\n**[AGREE] R2-W6: §7 Discussion and Conclusion 过短。**\n同意。§7 仅约 150 words（section7_conclusion_compressed.tex），主要重复了 Abstract 的数字。缺少：(1) 与 supervised SOTA (R-F1 49-53%, Zhong 2021, Ye 2022) 的差距讨论——论文的 fine-tuned R-F1 40-46 与 SOTA 差距的原因未分析（是 LoRA vs full FT？是 prompt format？）；(2) OntoCoDec 与 GoLLIE/KnowCoder 等 training-based 方法组合的具体路线图；(3) 对 CF 问题的 future work direction（global entity consensus）的展开。不过大量讨论已移至 Appendix B，所以这更多是空间分配问题而非内容缺失。\n\n**[AGREE] R2-W7: Abstract 数据密度过高。**\n同意。Abstract 约 190 words 中包含 DR≤0.20%、±0.6pp、76-99%、9-21%、≤1.2%、R-F1 40-46 等 10+ 个数字。审稿人在 30 秒内无法消化这些数字，反而影响了 Abstract 讲故事的效果。建议将具体数字减至 3-4 个关键数字，其余用定性描述替代。\n\n**[AGREE] R2-W8: BibTeX orphan/duplicate。**\n同意，与我的 W9 一致。引用验证确认 14 个 orphan entries、若干重复条目（formattax2026/lee2026formattax, dccd2026/reddy2026dccd, slot2025/shen2025slot 等）。\n\n**[AGREE] R2-W9: Dual-factor pattern 统计基础薄弱。**\n完全同意，与我的 W2 一致。n=4, p≈0.058, df=2。论文自己在 Appendix B 承认是 descriptive characterization。\n\n---\n\n### Questions 逐条回应\n\n**[REBUT] R2-Q1: κ(r) 对称关系归一化。**\n这个问题在技术上有道理但实际影响很小。κ(r) = 1 - |σ(r)|/|E|² 用 |E|² 作为理论最大值，对对称关系来说确实 overcounts（因为 (A,B) 和 (B,A) 是同一对）。但：(1) SciERC 和 DocRED 中大多数关系是非对称的（§4 Non-Rectangularity 分析隐含了方向性）；(2) κ(r) 在论文中主要用于 cross-relation 和 cross-dataset 比较（SciERC κ̄=0.333 vs DocRED κ̄=0.842），归一化方式只要一致就不影响比较结论；(3) 对称关系的 κ 修正（除以 |E|×(|E|+1)/2）会使 κ 值更小（约束更松），但相对排序不变。这是一个 valid 的 technical note，但不影响论文结论。建议作者在 footnote 中 acknowledge。\n\n**[AGREE] R2-Q2: Table 2 DocRED FT 数据不完整。**\n合理的要求。Table 2 标题提到 \"DocRED: Qwen DR −99%, Llama DR −59%\"，但表格本身只显示 SciERC 的详细四行对比。DocRED FT 的完整数据（Qwen: 0.76%→0.01%, Llama: 0.49%→0.20%）散布在正文中（§5.4 lines 104-106）和 Appendix Table 9 中。审稿人期望在 Table 2 中看到完整的 2 models × 2 datasets 对比。这是 presentation 问题。\n\n**[AGREE] R2-Q3: 约束为何增加 parse failure。**\n好问题，论文未充分解释。Table 4 注释提到 \"Parse failures: Llama DocRED 9.1%; others ≤1.1%\"，Appendix Table 9 显示 Qwen DocRED Full S1 的 PF 从 7.11% 升至 8.52%。可能的机制：constrained decoding 改变了 token probability distribution，在长文档中可能导致模型进入不利的 generation trajectory，产生结构上有效但 parser 无法处理的输出（如嵌套过深、字段顺序异常）。论文应当解释这一现象。\n\n**[REBUT] R2-Q4: WikiEvents Qwen trigger F1 下降 5.4pp 原因。**\n§5.5 确实报告了这个数字但未充分解释。不过需要注意上下文：这是 20 个文档上的结果，\"with wide confidence intervals at this sample size\"（§5.5 line 66）。5.4pp 的下降可能完全在 noise range 内。此外，argument F1 是 within ±1.1pp，这是 constraint enforcement 的直接目标（type validity for arguments），而 trigger F1 不受 semantic constraints 影响（constraints target entity/role types, not trigger spans）。Trigger F1 下降更可能是 constrained decoding 改变 generation trajectory 的间接效应（类似 Case Study 4, Appendix E.4），而非 constraint enforcement 的直接结果。论文应在 §5.5 中增加 1 句解释。\n\n---\n\n### Novelty Concern 综合评价\n\nR2 给 Excitement 3.0/5，认为核心是增量移植。我给出的整体评价（Overall 3.5, Borderline Conference）已隐含对 novelty 的更积极判断。\n\n**我的立场：novelty 确实不是 paradigm-shifting，但 \"增量移植\" 的定性过于简化。**\n\n具体而言：\n- **移植部分**（grammar layer 复用 XGrammar, logit masking 机制）的 novelty 确实有限——这一点 R2 是对的。\n- **非移植部分**（dynamic entity registry、CF↔DR trade-off 的发现和分析、pair-based vs independent enforcement 的 non-rectangularity 分析、constraint tightness 作为预测器）构成了实质性的分析和方法贡献。\n\n如果将 novelty 分解为 \"mechanism novelty\"（低-中）和 \"analytical contribution\"（中-高），综合 Excitement 约 3.0-3.5 是合理的。R2 的 3.0 偏保守但不离谱；我的判断偏向 3.5。\n\n关键在于：这篇论文的 value proposition 不是发明了新的 decoding paradigm，而是 (1) 证明了 IE 的 ontological constraints 可以被 compiled into composable token-level masks，(2) 系统分析了 composable constraint systems 的 fundamental trade-offs（CF↔DR），(3) 证明了与 fine-tuning 的 near-lossless composability。如果接受这个 framing（前提是 W1 中的 \"ontology\" overclaim 被修正），贡献是 solid 的。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 交叉回应：Reviewer 2 审稿意见\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 缺少 Responsible NLP Research Checklist。**\n完全同意。我在审稿时也检查了 main.tex（lines 63-96），确认论文包含 Limitations section 和 Ethics Statement，但没有 ARR 要求的 Responsible NLP Research Checklist。这是 ARR 硬性要求，缺失确实可能导致 desk reject。属于纯格式合规问题，修复成本低但优先级最高。\n\n**[AGREE] R2-W2: Zero-shot 下 CF trade-off 削弱核心 claim。**\n同意，且这与我的 W5 相呼应。补充证据：Table 1 中 Tot. (DR+CF) 从 15.45% 降至 10.83%，降幅仅 30%；Table 3 DocRED 从 18.56% 降至 12.78%，降幅 31%。但 Llama DocRED (Table 4) 更严重：DR 26.07%→2.55% 的同时 CF 从 0.17% 暴涨至 12.02%，Tot. 从 26.24% 仅降至 14.57%。\n\n不过需要补充一点 nuance：论文在 §5 Setup 中明确将 zero-shot 定位为 \"stress-tests constraint robustness under adversarial conditions (no task supervision, R-F1 2-8), where CF trade-offs are expected and documented\"。Fine-tuning regime 下 CF 降至 ≤1.18%（Table 2），Tot. 显著改善。所以 R2 的批评对 zero-shot 完全成立，但论文推荐的部署配置（LoRA + S1）确实实现了 near-lossless。建议作者在 Abstract 中更清晰地分层：fine-tuning = deployment claim, zero-shot = robustness diagnostic。\n\n**[REBUT] R2-W3: 新颖性偏增量。**\n部分不同意。R2 将 OntoCoDec 定性为 \"已有范式向 IE 的移植\" 低估了 IE 场景的独特技术挑战。具体反驳：\n\n1. **动态 entity registry 不是简单适配。** 代码生成中的类型系统是静态声明的（变量类型在编译时已知），而 IE 的 entity registry 在生成过程中动态构建——每个新实体被解码后才加入 registry，后续 relation 的 constraint target 依赖于已解码的 prefix（§3.1 \"unlike type-constrained code generation where types are statically declared, IE requires a dynamic entity registry built during generation\"）。这不是 engineering detail，而是 fundamentally different constraint structure。\n\n2. **Grammar-first fallback 及其产生的 CF↔DR trade-off 是 IE-specific 的发现。** PLDI 2025 的代码类型系统不存在 cross-field consistency 问题（每个变量只有一个类型声明），而 IE 中同一实体可出现在多个 triple 中，产生了 per-relation enforcement vs. global consistency 的张力。Appendix B 的 CF-DR trade-off analysis（Table 6）揭示了 composable constraint system 的 fundamental tension，这是本文的分析贡献，不是移植可以获得的。\n\n3. **Pair-based sequential masking 的必要性分析是新的。** §4 Non-Rectangularity 分析（SciERC 7/7、DocRED 73/96 关系非矩形，独立检查会引入 33-37% spurious pairs）在 constrained decoding 文献中未见讨论。\n\n4. **Constraint tightness 作为跨数据集行为预测器。** 虽然 n=4 的统计支撑不足（我在 W2 中已指出），但 tightness 概念本身为理解 constrained decoding 在不同 schema 上的表现差异提供了分析工具。\n\n综合判断：核心机制确实与 code-generation constrained decoding 有 mechanistic analogy，但 IE-specific 的挑战（dynamic registry, CF trade-off, non-rectangularity）构成了实质性的技术贡献。Excitement 3.0/5 可能偏低，我认为 3.5 更合理——不是开创性的新范式，但在 constrained decoding 应用于 IE 的具体问题上有明确增量。\n\n**[AGREE] R2-W4: WikiEvents 评估过于初步。**\n完全同意，与我的 W3 一致。补充：§5.5 自己报告 \"trigger F1 shows larger shifts (−5.4/−0.6 pp) with wide confidence intervals at this sample size\"。20 个测试文档的 bootstrap CI 对 trigger F1 的变化方向都无法确定。将其列为 Contribution #4 确实可能误导。\n\n**[REBUT] R2-W5: 缺少下游任务评估。**\n部分不同意。R2 的理想化要求（KG construction / QA 端到端评估）虽然有价值，但超出了本文的合理 scope：\n\n1. **论文的 contribution 是 constraint enforcement method，不是 end-to-end IE system。** §1 明确定义了问题：\"ensuring type-valid triples during autoregressive generation\"。Type validity 是一个 well-defined 的形式化目标，不依赖下游任务来定义其价值——ontologically invalid triple 无论在什么下游场景中都是 invalid。\n\n2. **下游影响需要额外的实验基础设施。** KG construction 评估需要完整的 entity linking + graph merging pipeline；QA 评估需要构建 QA 系统。这些是独立的研究问题，要求在本文中完成不合理。\n\n3. **论文已经在 Limitations 中 acknowledge 了这一点**（§Limitations line 71: \"CF type inconsistencies may propagate to downstream tasks...the impact of such propagation has not been evaluated\"），这是诚实且适当的处理。\n\n建议作者在 Discussion 中增加 1-2 句话 frame 下游评估为 future work，但不应作为 must-fix。\n\n**[AGREE] R2-W6: §7 Discussion and Conclusion 过短。**\n同意。§7 仅约 150 words（section7_conclusion_compressed.tex），主要重复了 Abstract 的数字。缺少：(1) 与 supervised SOTA (R-F1 49-53%, Zhong 2021, Ye 2022) 的差距讨论——论文的 fine-tuned R-F1 40-46 与 SOTA 差距的原因未分析（是 LoRA vs full FT？是 prompt format？）；(2) OntoCoDec 与 GoLLIE/KnowCoder 等 training-based 方法组合的具体路线图；(3) 对 CF 问题的 future work direction（global entity consensus）的展开。不过大量讨论已移至 Appendix B，所以这更多是空间分配问题而非内容缺失。\n\n**[AGREE] R2-W7: Abstract 数据密度过高。**\n同意。Abstract 约 190 words 中包含 DR≤0.20%、±0.6pp、76-99%、9-21%、≤1.2%、R-F1 40-46 等 10+ 个数字。审稿人在 30 秒内无法消化这些数字，反而影响了 Abstract 讲故事的效果。建议将具体数字减至 3-4 个关键数字，其余用定性描述替代。\n\n**[AGREE] R2-W8: BibTeX orphan/duplicate。**\n同意，与我的 W9 一致。引用验证确认 14 个 orphan entries、若干重复条目（formattax2026/lee2026formattax, dccd2026/reddy2026dccd, slot2025/shen2025slot 等）。\n\n**[AGREE] R2-W9: Dual-factor pattern 统计基础薄弱。**\n完全同意，与我的 W2 一致。n=4, p≈0.058, df=2。论文自己在 Appendix B 承认是 descriptive characterization。\n\n---\n\n### Questions 逐条回应\n\n**[REBUT] R2-Q1: κ(r) 对称关系归一化。**\n这个问题在技术上有道理但实际影响很小。κ(r) = 1 - |σ(r)|/|E|² 用 |E|² 作为理论最大值，对对称关系来说确实 overcounts（因为 (A,B) 和 (B,A) 是同一对）。但：(1) SciERC 和 DocRED 中大多数关系是非对称的（§4 Non-Rectangularity 分析隐含了方向性）；(2) κ(r) 在论文中主要用于 cross-relation 和 cross-dataset 比较（SciERC κ̄=0.333 vs DocRED κ̄=0.842），归一化方式只要一致就不影响比较结论；(3) 对称关系的 κ 修正（除以 |E|×(|E|+1)/2）会使 κ 值更小（约束更松），但相对排序不变。这是一个 valid 的 technical note，但不影响论文结论。建议作者在 footnote 中 acknowledge。\n\n**[AGREE] R2-Q2: Table 2 DocRED FT 数据不完整。**\n合理的要求。Table 2 标题提到 \"DocRED: Qwen DR −99%, Llama DR −59%\"，但表格本身只显示 SciERC 的详细四行对比。DocRED FT 的完整数据（Qwen: 0.76%→0.01%, Llama: 0.49%→0.20%）散布在正文中（§5.4 lines 104-106）和 Appendix Table 9 中。审稿人期望在 Table 2 中看到完整的 2 models × 2 datasets 对比。这是 presentation 问题。\n\n**[AGREE] R2-Q3: 约束为何增加 parse failure。**\n好问题，论文未充分解释。Table 4 注释提到 \"Parse failures: Llama DocRED 9.1%; others ≤1.1%\"，Appendix Table 9 显示 Qwen DocRED Full S1 的 PF 从 7.11% 升至 8.52%。可能的机制：constrained decoding 改变了 token probability distribution，在长文档中可能导致模型进入不利的 generation trajectory，产生结构上有效但 parser 无法处理的输出（如嵌套过深、字段顺序异常）。论文应当解释这一现象。\n\n**[REBUT] R2-Q4: WikiEvents Qwen trigger F1 下降 5.4pp 原因。**\n§5.5 确实报告了这个数字但未充分解释。不过需要注意上下文：这是 20 个文档上的结果，\"with wide confidence intervals at this sample size\"（§5.5 line 66）。5.4pp 的下降可能完全在 noise range 内。此外，argument F1 是 within ±1.1pp，这是 constraint enforcement 的直接目标（type validity for arguments），而 trigger F1 不受 semantic constraints 影响（constraints target entity/role types, not trigger spans）。Trigger F1 下降更可能是 constrained decoding 改变 generation trajectory 的间接效应（类似 Case Study 4, Appendix E.4），而非 constraint enforcement 的直接结果。论文应在 §5.5 中增加 1 句解释。\n\n---\n\n### Novelty Concern 综合评价\n\nR2 给 Excitement 3.0/5，认为核心是增量移植。我给出的整体评价（Overall 3.5, Borderline Conference）已隐含对 novelty 的更积极判断。\n\n**我的立场：novelty 确实不是 paradigm-shifting，但 \"增量移植\" 的定性过于简化。**\n\n具体而言：\n- **移植部分**（grammar layer 复用 XGrammar, logit masking 机制）的 novelty 确实有限——这一点 R2 是对的。\n- **非移植部分**（dynamic entity registry、CF↔DR trade-off 的发现和分析、pair-based vs independent enforcement 的 non-rectangularity 分析、constraint tightness 作为预测器）构成了实质性的分析和方法贡献。\n\n如果将 novelty 分解为 \"mechanism novelty\"（低-中）和 \"analytical contribution\"（中-高），综合 Excitement 约 3.0-3.5 是合理的。R2 的 3.0 偏保守但不离谱；我的判断偏向 3.5。\n\n关键在于：这篇论文的 value proposition 不是发明了新的 decoding paradigm，而是 (1) 证明了 IE 的 ontological constraints 可以被 compiled into composable token-level masks，(2) 系统分析了 composable constraint systems 的 fundamental trade-offs（CF↔DR），(3) 证明了与 fine-tuning 的 near-lossless composability。如果接受这个 framing（前提是 W1 中的 \"ontology\" overclaim 被修正），贡献是 solid 的。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-19T08:03:06.201046+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4663
}
```

</details>

---


### Assistant

_source line 628 · 2026-05-19T08:03:13.790099+00:00_

交叉回应已提交给 Review Director。

总结：对 R2 的 9 条 Weakness 中，6 条 [AGREE]（W1 Checklist、W2 CF trade-off、W4 WikiEvents、W6 Conclusion 过短、W7 Abstract 数据密度、W8/W9 BibTeX 和 dual-factor），2 条 [REBUT]（W3 novelty 偏增量——IE-specific 挑战构成实质贡献；W5 下游评估——超出合理 scope）。4 个 Question 中 2 条 [REBUT]（Q1 κ归一化实际影响小、Q4 trigger F1 下降在 noise range 内），2 条 [AGREE]（Q2 Table 2 不完整、Q3 parse failure 未解释）。对 novelty concern，我认为 R2 的 3.0 Excitement 偏保守，3.5 更合理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 18

## Round 18

72 recorded events


### User

_source line 629 · 2026-05-19T08:42:44.551755+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 1

### Venue 信息
- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR) May cycle
- **截止日期**: 2026-05-25
- **格式要求**: ACL 两栏模板（`\usepackage[review]{acl}`），Long paper 8 页正文，附录/参考文献不计页数
- **匿名规则**: Double-blind（作者信息匿名）
- **其他要求**: Limitations section（必须，不计页数）、Ethics Statement、ARR Responsible NLP Research Checklist
- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment 评分：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit

### 论文路径
`projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
（main.tex 通过 \input 引入各 section 和 appendix 文件，同目录下有 abstract.tex, section1-7, appendix_*.tex, checklist.tex 等）

### 你的审查侧重：方法严谨性 + 实验设计 + 统计声明

请重点审查以下方面：

1. **方法严谨性**：
   - 两层约束（grammar layer + semantic layer）的形式化是否准确、完备
   - entity registry 的动态构建机制是否有边界条件遗漏
   - grammar-first fallback 的设计是否合理，对 DR↔CF trade-off 的分析是否充分
   - constraint tightness κ(r) 的定义和使用是否严谨
   - 与 code generation 类型约束的区分论述是否成立

2. **实验设计**：
   - ablation 设计是否充分（5-way SciERC, 4-way DocRED）
   - 数据集选择是否有代表性（SciERC 7 relations vs DocRED 96 relations vs WikiEvents EE）
   - baseline 比较是否公平（unconstrained, grammar-only, semantic-only, post-hoc filtering）
   - fine-tuning composability 实验是否充分验证了核心 claim
   - WikiEvents EE 扩展（20-doc test set）的证据强度

3. **统计声明**：
   - 所有数值 claim 是否有充分统计支持（bootstrap p-values, CIs）
   - "near-lossless DR composability" claim 是否被数据支持（DR≤0.20%, R-F1 ±0.6pp）
   - "76-99% DR reduction" 等 range claim 是否准确反映跨模型变异
   - cross-model validation（3 models × 2 datasets）是否足以支撑泛化性 claim
   - beam search 结果（SciERC 全量 + DocRED 50-doc subset）的推广性

4. **Limitations 是否充分**：遗漏的重要限制

请以 ARR reviewer 标准输出完整审稿意见，包含：Strengths（逐条）、Weaknesses（逐条，带严重程度 Must-Fix/Should-Fix/Minor）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准给分）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-19T08:42:52.756423+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-19T08:42:52.757205+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_1_11179fb2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-19T08:42:55.067909+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 633 · 2026-05-19T08:42:55.169122+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-19T08:42:57.329114+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-19T08:42:57.430442+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-19T08:43:01.607547+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 637 · 2026-05-19T08:43:01.608024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-19T08:43:05.476516+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 639 · 2026-05-19T08:43:07.135779+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 640 · 2026-05-19T08:43:07.186723+00:00_

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
19	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
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
67	\paragraph{Constraint scope.}
68	CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	CF fallback ablation show
…[truncated 4463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-19T08:43:11.919360+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects of the paper but not others, please state in the review if you did not check some major parts, such as proofs, which is helpful for the AC to tell what asp
…[truncated 900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6442
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-19T08:43:17.497649+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form fields, scoring dimensions, and their scales (1-5 or other). List every field a reviewer needs to fill out, including: overall assessment, soundness, excitement/novelty, reproducibility, confidence, and any other dimensions. Include the description/rubric for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form fields, scoring dimensions, and their scales (1-5 or other). List every field a reviewer needs to fill out, including: overall assessment, soundness, excitement/novelty, reproducibility, confidence, and any other dimensions. Include the description/rubric for each score level."
  }
}
```

</details>

---


### Tool call

_source line 643 · 2026-05-19T08:43:19.456875+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 644 · 2026-05-19T08:43:20.211130+00:00_

1	\begin{abstract}
2	We present \textsc{OntoCoDec}, which compiles Information Extraction (IE) schemas into two composable token-level decoding constraints:
3	(1)~a \emph{grammar layer} (XGrammar) that guarantees JSON structural validity and vocabulary membership; and
4	(2)~a \emph{semantic layer} that enforces per-triple domain/range type constraints via a stateful entity registry and dynamic logit masking, with grammar-first fallback when constraints conflict.
5	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning; violation rates correlate with \emph{constraint tightness} rather than ontology or model scale.
6	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
7	Composed with Low-Rank Adaptation (LoRA), \textsc{OntoCoDec} achieves near-lossless DR composability under fine-tuning: DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp, CF\,$\leq$\,1.2\%.
8	Under zero-shot decoding, DR drops by 76--99\% for calibrated models, with an accompanying cross-field consistency (CF) increase (9--21\% zero-shot, resolved to $\leq$1.2\% by fine-tuning on both RE and EE).
9	Beam search with LoRA eliminates all four violation types on SciERC.
10	The framework extends to event extraction without modification (preliminary, 20-document test set).
11	OntoCoDec is training-free and applies to any autoregressive LM across four models (8B--70B) and three tokenizer families.
12	\end{abstract}
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 645 · 2026-05-19T08:43:20.211698+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 646 · 2026-05-19T08:43:20.664045+00:00_

1	% Section 1: Introduction (compressed, 669→~550 words)
2	
3	\section{Introduction}
4	\label{sec:introduction}
5	
6	Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
7	We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
8	Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 1--2\% even after LoRA fine-tuning; rates correlate with \emph{constraint tightness} (few valid type pairs per relation) rather than ontology or model scale.
9	Type violations are ontologically invalid regardless of downstream application: a triple whose head or tail type lies outside the relation's domain/range specification contradicts the schema definition.
10	At deployment-grade quality (R-F1 40--46\%), where extracted triples feed directly into knowledge graphs, reliable type-safety enforcement is needed.
11	
12	Existing approaches leave a fundamental gap.
13	Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
14	Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
15	Post-hoc filtering achieves higher F1 in most zero-shot settings via precision gains, but at the cost of discarding up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it discards the majority of outputs and becomes impractical.
16	OntoCoDec preserves recall by enforcing constraints during generation rather than discardi
…[truncated 2670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 647 · 2026-05-19T08:43:20.666066+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex"
  }
}
```

</details>

---


### Tool result

_source line 648 · 2026-05-19T08:43:21.319262+00:00_

1	% Section 2: Background (compressed)
2	
3	\section{Background}
4	\label{sec:background}
5	
6	\paragraph{IE Ontology Structure.}
7	\label{sec:bg:ontology}
8	An IE ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$ defines entity types $\mathcal{E}$, relation types $\mathcal{R}$, and a mapping $\sigma: \mathcal{R} \to \mathcal{P}(\mathcal{E} \times \mathcal{E})$ specifying valid (head type, tail type) pairs per relation.
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
19	However, these methods are limited to context-free constraints and cannot enforce cross-field semantic rules (e.g., ``if $r$ = \textsc{Feature-of}, t
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 649 · 2026-05-19T08:43:21.319771+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 650 · 2026-05-19T08:43:21.372076+00:00_

1	% Section 3 — Method (Draft)
2	% OntoCoDec: Type-Valid Information Extraction
3	% via Compiled Ontology Constraints
4	
5	\section{Method}
6	\label{sec:method}
7	
8	We present OntoCoDec, a two-layer constrained decoding framework that compiles IE schemas into token-level masks enforced during autoregressive generation.
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
29	This ordering ensures 
…[truncated 6604 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-19T08:43:26.504807+00:00_

# ACL Rolling Review Form Fields & Scoring Dimensions

## Required Text Fields
1. **Paper Summary** – Describe the paper's topic and highlight potential misunderstandings
2. **Summary of Strengths** – Reasons to publish at selective *ACL venue
3. **Summary of Weaknesses** – Concerns about prioritization; numbered for author response
4. **Comments/Suggestions/Typos** – Additional improvement suggestions
5. **Best Paper Justification** – Required only if rating "Consider for Award" or "Borderline Award"
6. **Limitations and Societal Impact** – Assessment of authors' discussion of limitations and impacts
7. **Ethical Concerns** – Review against ACL code of ethics
8. **Needs Ethics Review** – Explanation if paper warrants in-depth ethics committee review
9. **Conjecture as to Author Identity** – Optional; authors won't see response

## Scoring Dimensions

### Reviewer Confidence (1–5)
- 5: "Positive that my evaluation is correct"
- 4: Quite sure; unlikely to have missed important details
- 3: Pretty sure; possible oversight in details
- 2: Willing to defend but likely missed some details
- 1: "Not my area, or paper is very hard to understand"

### Soundness (1–5, with .5 increments)
- 5: "Excellent: This study is one of the most thorough"
- 4: Strong; sufficient support for claims
- 3: Acceptable; main claims supported
- 2: Poor; major technical/methodological problems
- 1: "Major Issues: This study is not yet sufficiently thorough"

### Excitement (1–5, with .5 increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; would mention to others
- 3: Interesting; might mention or attend
- 2: Potentially Interesting; doesn't resonate personally
- 1: "Not Exciting: this paper does not resonate with me"

### Overall Assessment (1–5, with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1
…[truncated 1006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 9007
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-19T08:43:33.443880+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-19T08:43:33.896429+00:00_

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
20	Recall the tightness of relation $r$ (\S\ref{sec:bg:ontology}):\footnote{For symmetric relations, $|\sigma(r)|$ counts ordered pairs; the normalization $|\mathcal{E}|^2$ remains appropriate since we evaluate on directed triples.}
21	%
22	\begin{equation}\label{eq:tightness}
23	  \kappa(r) = 1 - \frac{|\sigma(r)|}{|\mathc
…[truncated 1461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-19T08:43:33.997642+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-19T08:43:34.852035+00:00_

1	% §5 Setup (compressed from Violation Landscape)
2	% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
3	%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema
4	
5	\label{sec:violation_landscape}
6	
7	We evaluate OntoCoDec in two regimes.
8	Fine-tuning composability (\S\ref{sec:composability}) tests the recommended deployment configuration: LoRA + S1 constraints at R-F1 40--46.
9	Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) isolates layer contributions and stress-tests constraint robustness without task supervision; R-F1 2--8 reflects the absence of task-specific training, not method failure.
10	
11	\paragraph{Setup.}
12	We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
13	RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
14	The framework handles both sources without modification.
15	Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
16	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
17	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\re
…[truncated 35 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-19T08:43:34.902892+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-19T08:43:35.405456+00:00_

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
…[truncated 5798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-19T08:43:35.456229+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-19T08:43:35.658285+00:00_

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
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-19T08:43:35.709061+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-19T08:43:35.759883+00:00_

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
…[truncated 1797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 662 · 2026-05-19T08:43:42.060416+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
  }
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-19T08:43:42.880992+00:00_

1	% Section 5 — Event Extraction on WikiEvents (compact, inline)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\subsection{Preliminary Extension: Event Extraction}
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
…[truncated 2360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 820
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-19T08:43:43.012438+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-19T08:43:43.400414+00:00_

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
11	Under greedy S1, the grammar-first fallback resolves DR$\leftrightarrow$CF conflicts one token at a time; beam search ($k{=}4$) explores paths that satisfy both layers jointly and reduces DR and CF simultaneously.
12	With LoRA, beam S1 eliminates all four violation types on SciERC (551 docs) for both Qwen and Llama (R-F1 44.23, 46.11; Table~\ref{tab:beam-search}).
13	Under zero-shot, beam reduces DR to 0\% for calibrated models on SciERC (551 docs) and a DocRED 50-document subset, and CF substantially (9.90\%\,$\to$\,0.53\% Qwen; 6.56\%\,$\to$\,0.93\% Llama on SciERC); Mistral remains a boundary condition (DR 7.99\%, CF 1.27\%) due to high baseline violations (Appendix~\ref{app:beam-search}).
14	Total latency overhead is 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).
15	
16	% exp_ids: 70b_scierc_unconstrained, 70b_scierc_constrained, 70b_docred_unconstrained, 70b_docred_constrained
17	\paragraph{Cross-scale generalizability.}
18	\label{sec:70b-results}
19	On Llama-3.1-70B (AWQ INT4), OntoCoDec achieves DR$\to$0\% on SciERC (R-F1 $-$0.03\,pp) and \textbf{0\%} across ET, RV, and DR on the full DocRED 998-document set (R-F1 $+$0.04\,pp), the only configuration to completely eliminate DR on DocRED.
20	CF rises to 7.01\% (from 0.07\%); the low baseline reflects under-measurement (malformed outputs bypass the checker), while constrained decoding exposes more triples to the consi
…[truncated 100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 387
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-19T08:43:43.400856+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-19T08:43:43.954006+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
5	
6	\paragraph{Grammar-constrained decoding.}
7	XGrammar~\cite{dong2025xgrammar}, Outlines~\cite{willard2023outlines}, LMQL~\cite{beurer-kellner2023lmql}, SynCode~\cite{ugare2024syncode}, and Grammar-Aligned Decoding~\cite{park2024grammar} guarantee format validity via CFG-based token masking; JSONSchemaBench~\cite{jsonschemabench2025} benchmarks these systems.
8	GCD~\cite{geng2023gcd} applies grammar constraints to IE tasks.
9	In code generation, PICARD~\cite{scholak2021picard} and Synchromesh~\cite{synchromesh_iclr2022} enforce type constraints via incremental parsing, and \citet{pldi2025_type_constrained_codegen} compile full type systems into prefix automata.
10	These methods ensure syntactic or type-level validity but operate on static type declarations; IE requires a dynamic entity registry built during generation, where constraint targets depend on the co-occurring relation type.
11	OntoCoDec's grammar layer builds on XGrammar; its semantic layer extends constrained decoding from syntax to ontology-level type enforcement.
12	
13	\paragraph{Schema-aware IE.}
14	GoLLIE~\cite{sainz2024gollie}, GUIDEX~\cite{guidex2025}, and KnowCoder~\cite{knowcoder_acl2024} encode ontology structure as Python dataclasses and train models to generate typed code.
15	REBEL~\cite{cabot2021rebel}, InstructUIE~\cite{wang2023instructuie}, DeepStruct~\cite{wang2022deepstruct}, UIE~\cite{lu2022uie}, and USM~\cite{lou2023usm} unify extraction tasks via structured output formats with task-specific training.
16	UniversalNER~\cite{zhou2024universalner} achieves strong zero-shot NER via targeted distillation.
17	\citet{wadhwa2023revisiting} benchmark LLM-based RE and find persistent schema compliance gaps.
18	These methods internalize constraints through training; OntoCoDec enforces them at decoding time without retraining, and
…[truncated 1444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-19T08:43:44.004774+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-19T08:43:44.055560+00:00_

1	% Section 7 — Discussion and Conclusion
2	% Full discussion in Appendix; Mistral boundary condition in app:dual-factor.
3	
4	OntoCoDec compiles IE schemas into composable token-level decoding constraints that achieve near-lossless DR composability under fine-tuning: DR\,$\leq$\,0.20\% with R-F1 within $\pm$0.6\,pp (R-F1 40--46), CF\,$\leq$\,1.2\% on RE, RoV$\to$0\% and AC$\leq$0.8\% on EE, and beam search ($k{=}4$) eliminates all four RE violation types (\S\ref{sec:beam-results}).
5	Under zero-shot decoding, DR drops by 42--99\% across three models and three datasets with no significant F1 cost.
6	The R-F1 gap with supervised systems (49--53~\citep{zhong2021frustratingly,ye2022packed}) traces to base model IE ability, not constraint overhead; a GoLLIE-trained model could use OntoCoDec to eliminate residual violations.
7	
8	CF remains an open challenge: per-slot enforcement can assign different types to the same entity across triples. Global entity-level type consensus during decoding offers the most direct resolution path; registry type errors and grammar-first fallback partially mitigate but do not eliminate this.
9	The framework applies to any autoregressive IE system without modification, validated across four models (8B--70B), three tokenizer families, and two tasks.
10	Evaluating type-safety impact on downstream tasks and validating the tightness-calibration interaction on broader schemas remain future work.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-19T08:43:49.682184+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-19T08:43:50.486694+00:00_

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
13	(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type, which may differ from the entity's registered type.
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
26	The two-layer architecture produces two distinct fallback mechanisms with different semant
…[truncated 31971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-19T08:43:50.537428+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-19T08:43:51.040292+00:00_

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
…[truncated 8172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-19T08:43:51.040746+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-19T08:43:51.493426+00:00_

1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, full S1 constraints).}
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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-19T08:43:51.544183+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-19T08:43:51.594979+00:00_

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
17	Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
18	Full S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC and $+$2.43\% on DocRED (Qwen3-8B, zero-shot greedy); under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-19T08:43:58.227276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-19T08:43:58.680451+00:00_

1	\section{Ontology Scalability}
2	\label{app:scalability}
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{@{}lrrrr@{}}
9	\toprule
10	\textbf{Scale} & \textbf{Types} & \textbf{Rels} & \textbf{Compile (s)} & \textbf{Overhead} \\
11	\midrule
12	Small (SciERC) & 6 & 7 & 0.33 & 1.02$\times$ \\
13	Medium (DocRED) & 6 & 96 & 0.32 & 1.03$\times$ \\
14	Large (synth.) & 100 & 500 & 0.35 & 1.03$\times$ \\
15	XLarge (synth.) & 200 & 1{,}000 & 0.42 & 1.03$\times$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Compilation time (one-time) and per-token inference overhead across ontology scales. Small and Medium use real ontologies; Large and XLarge use synthetic ontologies with random domain/range constraints. Overhead measured on Qwen3-8B, 10 documents per scale.}
19	\label{tab:scalability}
20	\end{table}
21	
22	Grammar compilation scales sub-linearly (0.33\,s to 0.37\,s for 7$\to$1{,}000 relations); semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-19T08:43:58.680879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-19T08:43:59.635914+00:00_

1	\section{Full Fine-Tuning Baseline}
2	\label{app:full-ft}
3	
4	To verify that constraint effectiveness generalizes beyond LoRA, we evaluate Qwen3-8B with full-parameter fine-tuning on SciERC (same data, 3 epochs, lr=$2{\times}10^{-4}$, seed 42).
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{@{}lrrrr@{}}
10	\toprule
11	& \textbf{E-F1} & \textbf{R-F1} & \textbf{DR\%} & \textbf{CF\%} \\
12	\midrule
13	Full FT unconstrained & 64.78 & 37.89 & 2.74 & 0 \\
14	Full FT + S1 & 64.78 & 37.89 & \textbf{0} & 1.31 \\
15	\midrule
16	LoRA unconstrained & 66.86 & 43.65 & 0.31 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, which confirms that constraint enforcement is effective regardless of the fine-tuning method. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-19T08:43:59.636438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-19T08:43:59.837797+00:00_

1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (Qwen3-8B, 551 documents). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\begin{tabular}{llcccccc}
12	\toprule
13	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	\multirow{2}{*}{Default}
16	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
17	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
18	\midrule
19	\multirow{2}{*}{Minimal}
20	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
21	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
22	\midrule
23	\multirow{2}{*}{Detailed}
24	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
25	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (E
…[truncated 954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-19T08:43:59.838195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-19T08:43:59.888750+00:00_

1	% ARR Responsible NLP Research Checklist
2	% Sections A--E, per https://aclrollingreview.org/responsibleNLPresearch/
3	
4	\section*{Responsible NLP Research Checklist}
5	
6	\subsection*{A \hspace{0.5em} For Every Submission}
7	
8	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=2.5em]
9	\item \textbf{Did you describe the limitations of your work?}
10	\\ Yes. See the Limitations section (after \S7), which covers constraint scope (CF trade-off, residual DR decomposition), evaluation coverage (model scales, decoding configurations), and engineering considerations (scalability bounds, tokenizer dependency).
11	
12	\item \textbf{Did you discuss any potential risks of your work?}
13	\\ Yes. See the Ethics Statement. The method operates on model outputs using publicly available datasets with no PII. Constrained decoding does not introduce new privacy or safety risks beyond those of base LMs.
14	
15	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
16	\\ Yes. The abstract states three main contributions; \S1 elaborates each with supporting evidence and section pointers.
17	\end{enumerate}
18	
19	\subsection*{B \hspace{0.5em} Did you use or create scientific artifacts?}
20	Yes. We use existing datasets (SciERC, DocRED, WikiEvents), pre-trained models (Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.1-70B), and software libraries (XGrammar, vLLM, PEFT).
21	
22	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=2.5em]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	\\ Yes. All datasets, models, and libraries are cited in \S2, \S5, and Appendix~\ref{app:reproducibility}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	\\ Yes. SciERC (Apache 2.0), DocRED (MIT), WikiEvents (publicly released by \citet{li2021document}). Model licenses are noted in Appendix~\ref{app:reproducibility}.
28	
29	\item \textbf{Did you discuss if your use of existing artifacts was con
…[truncated 3197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-19T08:44:05.668200+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-19T08:44:06.020310+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-19T08:44:06.020857+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-19T08:44:06.975646+00:00_

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
…[truncated 19735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-19T08:44:06.976038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-19T08:44:07.228101+00:00_

1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	
10	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
11	
12	\subsection{Domain-Range Correction}
13	\label{app:case-dr}
14	
15	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
16	
17	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
18	
19	\begin{table}[h]
20	\centering
21	\small
22	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red} = violation; \textcolor{fixed}{green} = corrected.}
23	\label{tab:case1}
24	\begin{tabular}{@{}p{3.2cm}lll@{}}
25	\toprule
26	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
27	\midrule
28	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
29	\midrule
30	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
31	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
32	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Used-for(model approach, recover) & Method & Task & \ding{51} \\
34	\midrule
35	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
36	\midrule
37	Feature-of(recover, shapes) & Task & \textcolor{fixe
…[truncated 5952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-19T08:44:07.278905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
  }
}
```

</details>

---


### Tool result

_source line 693 · 2026-05-19T08:44:07.329726+00:00_

1	\section{Effect of Document Length on Constraint Effectiveness}
2	\label{app:doc-length}
3	
4	To examine whether OntoCoDec's constraint effectiveness varies with document complexity, we partition test documents into three length bins (tertile split by word count) and report per-bin violation counts and F1.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Document length breakdown on SciERC (Qwen3-8B). Tertile boundaries: Short $\leq$ 19 words, Medium $\leq$ 27, Long $>$ 27.}
10	\label{tab:doc-length-scierc}
11	\begin{tabular}{ll rrrrr rr}
12	\toprule
13	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
14	\midrule
15	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
16	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
17	\midrule
18	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
19	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
20	\midrule
21	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
22	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
31	\label{tab:doc-length-docred}
32	\begin{tabular}{ll rrrrr rr}
33	\toprule
34	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
35	\midrule
36	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
37	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
38	\midrule
39	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
40	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
41	\midrule
42	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 
…[truncated 1432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-19T08:44:12.286442+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-19T08:44:12.337303+00:00_

1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, which indicates stronger baseline vocabulary compliance.
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
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 696 · 2026-05-19T08:45:50.377865+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 697 · 2026-05-19T08:45:50.428584+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-19T08:47:46.363079+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — Round 1 完整审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 方法严谨性 + 实验设计 + 统计声明\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法设计清晰、实验分析诚实透彻，但\"near-lossless\"叙事被 CF trade-off 削弱，缺少与 schema-aware IE 系统的直接对比，部分统计声明证据不足。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 两层约束形式化准确，sequential masking 等价性论证正确；但 dual-factor 回归仅 n=4 且 p=0.058，\"near-lossless\" claim 未充分纳入 CF 代价 |\n| Excitement | 3/5 | 问题重要且实际，但贡献偏增量：grammar 层是 XGrammar 现有能力，semantic 层是自然扩展；分析深度是亮点 |\n| Reproducibility | 4/5 | LoRA 超参、硬件、软件版本、种子均报告；承诺开源；prompt 模板完整 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 领域 |\n\n---\n\n## 主要优势\n\n**S1.** 问题定义精确且实用。将 IE 中的 type violation 分为 DR/RV/ET/CF 四类，定义清晰，violation landscape 的实证分析（§5, Table 1-2）为后续方法评估提供了可靠基线。\n\n**S2.** 两层架构设计合理。Grammar 层保证结构有效性，semantic 层通过 stateful entity registry 执行 domain/range 约束，enabling dependency 通过消融实验有力验证（semantic-only 仅降低 DR 24%，加入 grammar 后降至 94%，Table 1）。Sequential masking 的等价性论证（§3.1 脚注，SciERC 33.3%/DocRED 36.8% spurious pairs）严谨。\n\n**S3.** 分析诚实透彻。CF↔DR trade-off 的 pilot ablation（Appendix B, Table 5）、Mistral 作为 boundary condition 的讨论（§5.4）、residual DR 的 4 类 root cause 分解（Appendix B）、Case Study 4 展示约束导致 trajectory divergence 的失败案例，均体现了高质量的科学诚实度。\n\n**S4.** 实验覆盖面广。3 个数据集（SciERC/DocRED/WikiEvents）× 4 个模型（Qwen/Llama/Mistral 8B + Llama 70B）× 3 种解码策略（greedy/sampling/beam），附录实验丰富（prompt sensitivity、document length、scalability、full fine-tuning）。\n\n**S5.** 工程贡献扎实。Tokenizer-agnostic continuation masking 处理 prefix-shared types（§3.2），beam search 适配仅需 125 行代码（Appendix F），runtime overhead 控制在 2-13%（§5.6）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 和 Introduction 的 \"near-lossless\" 叙事未充分呈现 CF 代价\n\n- 具体位置：Abstract line 7-8, §1 line 25\n- 问题：Abstract 声称 \"near-lossless DR composability: DR≤0.20% with R-F1 within ±0.6pp, CF≤1.2%\"，但这仅限于 LoRA + S1 推荐配置。在 zero-shot 下，CF 从 0.08% 飙升至 9.90%（SciERC）甚至 12.02%（Llama DocRED），即方法将 DR violations 部分转化为 CF violations。Abstract 第 8 行虽提及 \"CF increase (9-21% zero-shot)\"，但措辞将其作为附带现象而非核心 trade-off。\n- 为什么影响接收：审稿人会质疑方法是否真正\"解决\"了 type violation，还是将一种 violation 转化为另一种。Total type-violation burden（DR+CF）在 SciERC zero-shot 下从 15.45% 降至 10.83%（Table 1），降幅仅 30%，远不如 \"94% DR reduction\" 给人的印象。\n- 建议修改方向：（1）Abstract 中明确 \"near-lossless\" 仅指 LoRA+S1 配置，zero-shot 下存在显著 CF trade-off；（2）在 Introduction 的 contribution 列表中加入 CF trade-off 作为 honest limitation；（3）考虑在 Abstract 中报告 total violation (DR+CF) 的变化，而非仅报告 DR。\n\n**N2** [critical] 缺少与 schema-aware IE 系统的直接对比\n\n- 具体位置：§6 Related Work, §5 Experiments\n- 问题：论文在 Related Work（§6）中详细讨论了 GoLLIE、GenIE、KnowCoder、UIE 等 schema-aware IE 系统，并指出它们与 OntoCoDec \"互补\"（§6 para 2: \"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"）。但实验部分完全没有与这些系统比较 violation rates。GoLLIE 将 schema 编码为 Python dataclass 并训练模型生成 typed code，其 type violation rate 是多少？如果 GoLLIE 的 violation rate 已经很低，OntoCoDec 的增量价值就需要重新评估。\n- 为什么影响接收：缺少与最相关 baseline 的比较，审稿人无法判断 OntoCoDec 相对于现有方法的实际增量。论文的 baseline 仅包括 unconstrained/grammar-only/semantic-only/post-hoc filtering，这些都是 ablation 变体而非外部竞争方法。\n- 建议修改方向：（1）至少报告 GoLLIE 或 KnowCoder 在 SciERC/DocRED 上的 violation rates（即使 F1 不直接可比）；（2）如果无法复现这些系统，至少引用它们论文中报告的 schema compliance 数据；（3）或者明确论述为什么这些系统不适合作为 baseline（例如它们需要特定训练、不支持相同数据集等）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Dual-factor pattern 的统计支撑不足\n\n- 具体位置：§4 Constraint Composition, Appendix B (app:dual-factor)\n- 问题：dual-factor regression（residual DR vs. κ̄ × RV_baseline）仅有 n=4 个数据点（calibrated models only），p≈0.058（不显著），df=2。论文自己承认这是 \"descriptive characterization rather than a confirmatory statistical test\"（Appendix B），但在正文§4中使用 \"consistent with\" 和 \"supports\" 等措辞，并将其作为全文的核心解释框架（§1, §4, §5.2, §5.4 均引用）。\n- 建议：（1）降低正文中对该 pattern 的依赖程度，避免将其作为 causal explanation；（2）Spearman ρ = -0.77（n=6）for DR↔CF 同样缺乏统计功效，应注明 n 太小无法做有意义的相关性检验；（3）考虑 dual-factor 框架是否是 over-fitting 4 个点的事后解释。\n\n**W2** [warning] WikiEvents 证据强度不足以支撑 \"extends to event extraction without modification\" claim\n\n- 具体位置：Abstract line 10, §5.5, Contribution 3 (§1 line 32)\n- 问题：WikiEvents 的 fine-tuning composability 基于 20-document test set（§5.5 line 65），confidence intervals 很宽（如 Llama RoV CI [0%, 1.73%]）。Trigger F1 变化大（-5.4/-0.6pp）且 CI 宽。零-shot 结果（246 docs）更稳健但 CF 高达 15-21%。论文自己标注 \"preliminary\"，但 Abstract 和 Contribution 列表中的表述（\"The framework extends to event extraction without modification\"）缺乏 \"preliminary\" 限定。\n- 建议：（1）Abstract 和 Contribution 3 中加入 \"preliminary\" 限定词；（2）讨论 20-doc test set 下的统计功效限制。\n\n**W3** [warning] Beam search DocRED 结果基于 50-doc subset，推广性受限\n\n- 具体位置：§5.6, Appendix F (Table 7)\n- 问题：Beam search 在 DocRED 上仅评估 50-document subset（Table 7 caption: \"DocRED evaluated on matched 50-document subsets\"），而全量 DocRED 有 998 docs。虽然 Clopper-Pearson 95% CI 上界为 5.8%，但 50 docs 的 DR=0% 结果的统计功效有限（998 docs 上可能出现 long-tail violations）。SciERC beam search 评估了全量 551 docs，这一不对称性削弱了 DocRED beam search claim 的可信度。\n- 建议：（1）解释为什么只用 50-doc subset（计算成本？）；（2）在正文中明确标注 subset 限制；（3）讨论 50-doc DR=0% 对全量 998-doc 的可推广性。\n\n**W4** [warning] Fine-tuning composability 仅验证 LoRA 一种方法\n\n- 具体位置：§5.1 (sec:composability), Limitations, Appendix K\n- 问题：论文的推荐部署配置是 \"LoRA + S1\"，但 composability 仅用 LoRA 全面验证（2 models × 3 datasets）。Appendix K 的 full fine-tuning 实验用了 untuned learning rate（2×10⁻⁴，论文自己承认 \"likely due to an untuned learning rate\"），导致 R-F1 比 LoRA 低 5.88pp（37.89 vs 43.77）。这不是 fair comparison——一个超参未调优的实验无法证明 \"constraint effectiveness generalizes beyond LoRA\"。\n- 建议：（1）用 full fine-tuning 的标准 learning rate（如 5×10⁻⁶）重做实验，或删除 \"generalizes beyond LoRA\" 的 claim；（2）至少承认 full FT 实验的超参未调优限制了结论的泛化性。\n\n**W5** [warning] Checklist 中 WikiEvents 文档数不一致\n\n- 具体位置：Checklist B6, §5.5 Table 4 caption\n- 问题：Checklist B6 声称 \"WikiEvents: 246 test documents\"，但 §5.5 报告的 train/dev/test split 为 194/20/20，总计 234 ≠ 246。Table 4 caption 也写 \"246 documents\"。这可能是用了全部文档做 zero-shot 评估，但 234 ≠ 246 的数值不一致需要解释。\n- 建议：核实实际文档数并统一。\n\n---\n\n## 小问题（不影响接收）\n\n- §2 Background 中定义 σ: R → P(E × E) 但未说明 P 表示幂集。建议加注。\n- §3.2 Entity Registry（line 59）：\"each completed entry {n_i, τ_i} adds (n_i, τ_i) to D\"——应明确 entity list 在 relation list 之前生成（output schema Eq.1 隐含但未显式说明生成顺序）。\n- Table 2（DocRED ablation）：Grammar-only 模式下 DR 从 18.46% 上升至 26.17%（+42%），这个 counter-intuitive 结果在正文中有解释（OOV triples 变得可评估），但建议在 Table caption 中也加注以避免读者误解。\n- §5.4 Cross-Model Validation：Table 3 中 Llama DocRED CF 值为 \"---\"（unconstrained），但 Table 6（fine-tuned ablation）中该值也为 \"---\"。应统一处理或解释为何未计算。\n- Appendix B (app:discussion) 中 \"effective semantic constraint coverage\" 定义为 1 - f_gf，但 Qwen SciERC 的 coverage 是 100%（零 fallback），而 Llama SciERC 是 63.4%。这个巨大差异（100% vs 63.4%）值得在正文中简要提及。\n- Grammar compile time 在 Appendix B 报告为 0.044s，但 Appendix J 报告 SciERC 为 0.33s。应统一或解释差异（可能前者是 semantic compile，后者是 grammar compile）。\n\n---\n\n## Questions to Authors\n\n**Q1.** 在 LoRA + S1 推荐配置下，total violation burden (DR+CF) 的净变化是多少？例如 Qwen SciERC：unconstrained DR=1.95%, CF=0%, total=1.95% → constrained DR=0%, CF=1.18%, total=1.18%。这说明净减少仅 0.77pp。是否有更多 model×dataset 配置的 total violation 数据？\n\n**Q2.** 为什么不比较 GoLLIE 或类似 schema-aware 系统的 violation rates？即使 F1 不直接可比，violation rates 应该可以在相同数据集上测量。\n\n**Q3.** Entity registry 如何处理 entity list 中未出现但在 relation 中首次出现的实体？（例如模型在 relation 中引用了一个未在 entity list 中生成的实体名）\n\n**Q4.** 论文声称 beam search + LoRA 在 SciERC 上消除所有四种 violation。但 beam search 在 DocRED 全量（998 docs）上的结果是什么？只有 50-doc subset 的 DR=0% 结果。\n\n**Q5.** Constraint tightness κ(r) 使用 |E|² 归一化（Eq. 2），但 SciERC 有 6 个 entity types（|E|²=36）而 DocRED 也有 6 个（|E|²=36）。那么两个数据集的 κ 差异完全来自 |σ(r)| 的差异？请确认。\n\n---\n\n## Missing References\n\n- Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\" 已引用（§6），但未引用其 violation rate 数据作为 baseline comparison point。\n- Josifoski et al. (2022) GenIE 在 Related Work appendix 中提及但未在主体实验中比较。\n- Paolini et al. (2021) \"Structured Prediction as Translation between Augmented Natural Languages\" 可作为 structured generation for IE 的 baseline 参考。\n- TANL / DeepStruct 等 structured generation IE 系统的 violation rates 未被讨论。\n\n---\n\n## Limitations and Societal Impact 评估\n\nLimitations section 是本文的亮点之一，覆盖了 constraint scope（CF trade-off、residual DR 分解）、evaluation coverage（model scale、decoding configurations、LoRA-only validation）、engineering considerations（tokenizer、scalability bounds）。两个遗漏：（1）empirically derived constraints 继承训练数据偏差/覆盖率不足的风险（§2 提到 99%+ coverage 但未讨论 bias）；（2）low zero-shot F1 (2-8%) 下的约束行为是否外推到更高 F1 operating points 未讨论。\n\nEthics Statement 简洁适当。\n",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — Round 1 完整审稿意见\n\n**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**审查侧重**: 方法严谨性 + 实验设计 + 统计声明\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法设计清晰、实验分析诚实透彻，但\"near-lossless\"叙事被 CF trade-off 削弱，缺少与 schema-aware IE 系统的直接对比，部分统计声明证据不足。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 两层约束形式化准确，sequential masking 等价性论证正确；但 dual-factor 回归仅 n=4 且 p=0.058，\"near-lossless\" claim 未充分纳入 CF 代价 |\n| Excitement | 3/5 | 问题重要且实际，但贡献偏增量：grammar 层是 XGrammar 现有能力，semantic 层是自然扩展；分析深度是亮点 |\n| Reproducibility | 4/5 | LoRA 超参、硬件、软件版本、种子均报告；承诺开源；prompt 模板完整 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 IE 领域 |\n\n---\n\n## 主要优势\n\n**S1.** 问题定义精确且实用。将 IE 中的 type violation 分为 DR/RV/ET/CF 四类，定义清晰，violation landscape 的实证分析（§5, Table 1-2）为后续方法评估提供了可靠基线。\n\n**S2.** 两层架构设计合理。Grammar 层保证结构有效性，semantic 层通过 stateful entity registry 执行 domain/range 约束，enabling dependency 通过消融实验有力验证（semantic-only 仅降低 DR 24%，加入 grammar 后降至 94%，Table 1）。Sequential masking 的等价性论证（§3.1 脚注，SciERC 33.3%/DocRED 36.8% spurious pairs）严谨。\n\n**S3.** 分析诚实透彻。CF↔DR trade-off 的 pilot ablation（Appendix B, Table 5）、Mistral 作为 boundary condition 的讨论（§5.4）、residual DR 的 4 类 root cause 分解（Appendix B）、Case Study 4 展示约束导致 trajectory divergence 的失败案例，均体现了高质量的科学诚实度。\n\n**S4.** 实验覆盖面广。3 个数据集（SciERC/DocRED/WikiEvents）× 4 个模型（Qwen/Llama/Mistral 8B + Llama 70B）× 3 种解码策略（greedy/sampling/beam），附录实验丰富（prompt sensitivity、document length、scalability、full fine-tuning）。\n\n**S5.** 工程贡献扎实。Tokenizer-agnostic continuation masking 处理 prefix-shared types（§3.2），beam search 适配仅需 125 行代码（Appendix F），runtime overhead 控制在 2-13%（§5.6）。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Abstract 和 Introduction 的 \"near-lossless\" 叙事未充分呈现 CF 代价\n\n- 具体位置：Abstract line 7-8, §1 line 25\n- 问题：Abstract 声称 \"near-lossless DR composability: DR≤0.20% with R-F1 within ±0.6pp, CF≤1.2%\"，但这仅限于 LoRA + S1 推荐配置。在 zero-shot 下，CF 从 0.08% 飙升至 9.90%（SciERC）甚至 12.02%（Llama DocRED），即方法将 DR violations 部分转化为 CF violations。Abstract 第 8 行虽提及 \"CF increase (9-21% zero-shot)\"，但措辞将其作为附带现象而非核心 trade-off。\n- 为什么影响接收：审稿人会质疑方法是否真正\"解决\"了 type violation，还是将一种 violation 转化为另一种。Total type-violation burden（DR+CF）在 SciERC zero-shot 下从 15.45% 降至 10.83%（Table 1），降幅仅 30%，远不如 \"94% DR reduction\" 给人的印象。\n- 建议修改方向：（1）Abstract 中明确 \"near-lossless\" 仅指 LoRA+S1 配置，zero-shot 下存在显著 CF trade-off；（2）在 Introduction 的 contribution 列表中加入 CF trade-off 作为 honest limitation；（3）考虑在 Abstract 中报告 total violation (DR+CF) 的变化，而非仅报告 DR。\n\n**N2** [critical] 缺少与 schema-aware IE 系统的直接对比\n\n- 具体位置：§6 Related Work, §5 Experiments\n- 问题：论文在 Related Work（§6）中详细讨论了 GoLLIE、GenIE、KnowCoder、UIE 等 schema-aware IE 系统，并指出它们与 OntoCoDec \"互补\"（§6 para 2: \"a GoLLIE-trained model could use OntoCoDec to eliminate residual violations\"）。但实验部分完全没有与这些系统比较 violation rates。GoLLIE 将 schema 编码为 Python dataclass 并训练模型生成 typed code，其 type violation rate 是多少？如果 GoLLIE 的 violation rate 已经很低，OntoCoDec 的增量价值就需要重新评估。\n- 为什么影响接收：缺少与最相关 baseline 的比较，审稿人无法判断 OntoCoDec 相对于现有方法的实际增量。论文的 baseline 仅包括 unconstrained/grammar-only/semantic-only/post-hoc filtering，这些都是 ablation 变体而非外部竞争方法。\n- 建议修改方向：（1）至少报告 GoLLIE 或 KnowCoder 在 SciERC/DocRED 上的 violation rates（即使 F1 不直接可比）；（2）如果无法复现这些系统，至少引用它们论文中报告的 schema compliance 数据；（3）或者明确论述为什么这些系统不适合作为 baseline（例如它们需要特定训练、不支持相同数据集等）。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Dual-factor pattern 的统计支撑不足\n\n- 具体位置：§4 Constraint Composition, Appendix B (app:dual-factor)\n- 问题：dual-factor regression（residual DR vs. κ̄ × RV_baseline）仅有 n=4 个数据点（calibrated models only），p≈0.058（不显著），df=2。论文自己承认这是 \"descriptive characterization rather than a confirmatory statistical test\"（Appendix B），但在正文§4中使用 \"consistent with\" 和 \"supports\" 等措辞，并将其作为全文的核心解释框架（§1, §4, §5.2, §5.4 均引用）。\n- 建议：（1）降低正文中对该 pattern 的依赖程度，避免将其作为 causal explanation；（2）Spearman ρ = -0.77（n=6）for DR↔CF 同样缺乏统计功效，应注明 n 太小无法做有意义的相关性检验；（3）考虑 dual-factor 框架是否是 over-fitting 4 个点的事后解释。\n\n**W2** [warning] WikiEvents 证据强度不足以支撑 \"extends to event extraction without modification\" claim\n\n- 具体位置：Abstract line 10, §5.5, Contribution 3 (§1 line 32)\n- 问题：WikiEvents 的 fine-tuning composability 基于 20-document test set（§5.5 line 65），confidence intervals 很宽（如 Llama RoV CI [0%, 1.73%]）。Trigger F1 变化大（-5.4/-0.6pp）且 CI 宽。零-shot 结果（246 docs）更稳健但 CF 高达 15-21%。论文自己标注 \"preliminary\"，但 Abstract 和 Contribution 列表中的表述（\"The framework extends to event extraction without modification\"）缺乏 \"preliminary\" 限定。\n- 建议：（1）Abstract 和 Contribution 3 中加入 \"preliminary\" 限定词；（2）讨论 20-doc test set 下的统计功效限制。\n\n**W3** [warning] Beam search DocRED 结果基于 50-doc subset，推广性受限\n\n- 具体位置：§5.6, Appendix F (Table 7)\n- 问题：Beam search 在 DocRED 上仅评估 50-document subset（Table 7 caption: \"DocRED evaluated on matched 50-document subsets\"），而全量 DocRED 有 998 docs。虽然 Clopper-Pearson 95% CI 上界为 5.8%，但 50 docs 的 DR=0% 结果的统计功效有限（998 docs 上可能出现 long-tail violations）。SciERC beam search 评估了全量 551 docs，这一不对称性削弱了 DocRED beam search claim 的可信度。\n- 建议：（1）解释为什么只用 50-doc subset（计算成本？）；（2）在正文中明确标注 subset 限制；（3）讨论 50-doc DR=0% 对全量 998-doc 的可推广性。\n\n**W4** [warning] Fine-tuning composability 仅验证 LoRA 一种方法\n\n- 具体位置：§5.1 (sec:composability), Limitations, Appendix K\n- 问题：论文的推荐部署配置是 \"LoRA + S1\"，但 composability 仅用 LoRA 全面验证（2 models × 3 datasets）。Appendix K 的 full fine-tuning 实验用了 untuned learning rate（2×10⁻⁴，论文自己承认 \"likely due to an untuned learning rate\"），导致 R-F1 比 LoRA 低 5.88pp（37.89 vs 43.77）。这不是 fair comparison——一个超参未调优的实验无法证明 \"constraint effectiveness generalizes beyond LoRA\"。\n- 建议：（1）用 full fine-tuning 的标准 learning rate（如 5×10⁻⁶）重做实验，或删除 \"generalizes beyond LoRA\" 的 claim；（2）至少承认 full FT 实验的超参未调优限制了结论的泛化性。\n\n**W5** [warning] Checklist 中 WikiEvents 文档数不一致\n\n- 具体位置：Checklist B6, §5.5 Table 4 caption\n- 问题：Checklist B6 声称 \"WikiEvents: 246 test documents\"，但 §5.5 报告的 train/dev/test split 为 194/20/20，总计 234 ≠ 246。Table 4 caption 也写 \"246 documents\"。这可能是用了全部文档做 zero-shot 评估，但 234 ≠ 246 的数值不一致需要解释。\n- 建议：核实实际文档数并统一。\n\n---\n\n## 小问题（不影响接收）\n\n- §2 Background 中定义 σ: R → P(E × E) 但未说明 P 表示幂集。建议加注。\n- §3.2 Entity Registry（line 59）：\"each completed entry {n_i, τ_i} adds (n_i, τ_i) to D\"——应明确 entity list 在 relation list 之前生成（output schema Eq.1 隐含但未显式说明生成顺序）。\n- Table 2（DocRED ablation）：Grammar-only 模式下 DR 从 18.46% 上升至 26.17%（+42%），这个 counter-intuitive 结果在正文中有解释（OOV triples 变得可评估），但建议在 Table caption 中也加注以避免读者误解。\n- §5.4 Cross-Model Validation：Table 3 中 Llama DocRED CF 值为 \"---\"（unconstrained），但 Table 6（fine-tuned ablation）中该值也为 \"---\"。应统一处理或解释为何未计算。\n- Appendix B (app:discussion) 中 \"effective semantic constraint coverage\" 定义为 1 - f_gf，但 Qwen SciERC 的 coverage 是 100%（零 fallback），而 Llama SciERC 是 63.4%。这个巨大差异（100% vs 63.4%）值得在正文中简要提及。\n- Grammar compile time 在 Appendix B 报告为 0.044s，但 Appendix J 报告 SciERC 为 0.33s。应统一或解释差异（可能前者是 semantic compile，后者是 grammar compile）。\n\n---\n\n## Questions to Authors\n\n**Q1.** 在 LoRA + S1 推荐配置下，total violation burden (DR+CF) 的净变化是多少？例如 Qwen SciERC：unconstrained DR=1.95%, CF=0%, total=1.95% → constrained DR=0%, CF=1.18%, total=1.18%。这说明净减少仅 0.77pp。是否有更多 model×dataset 配置的 total violation 数据？\n\n**Q2.** 为什么不比较 GoLLIE 或类似 schema-aware 系统的 violation rates？即使 F1 不直接可比，violation rates 应该可以在相同数据集上测量。\n\n**Q3.** Entity registry 如何处理 entity list 中未出现但在 relation 中首次出现的实体？（例如模型在 relation 中引用了一个未在 entity list 中生成的实体名）\n\n**Q4.** 论文声称 beam search + LoRA 在 SciERC 上消除所有四种 violation。但 beam search 在 DocRED 全量（998 docs）上的结果是什么？只有 50-doc subset 的 DR=0% 结果。\n\n**Q5.** Constraint tightness κ(r) 使用 |E|² 归一化（Eq. 2），但 SciERC 有 6 个 entity types（|E|²=36）而 DocRED 也有 6 个（|E|²=36）。那么两个数据集的 κ 差异完全来自 |σ(r)| 的差异？请确认。\n\n---\n\n## Missing References\n\n- Wadhwa et al. (2023) \"Revisiting Relation Extraction in the era of Large Language Models\" 已引用（§6），但未引用其 violation rate 数据作为 baseline comparison point。\n- Josifoski et al. (2022) GenIE 在 Related Work appendix 中提及但未在主体实验中比较。\n- Paolini et al. (2021) \"Structured Prediction as Translation between Augmented Natural Languages\" 可作为 structured generation for IE 的 baseline 参考。\n- TANL / DeepStruct 等 structured generation IE 系统的 violation rates 未被讨论。\n\n---\n\n## Limitations and Societal Impact 评估\n\nLimitations section 是本文的亮点之一，覆盖了 constraint scope（CF trade-off、residual DR 分解）、evaluation coverage（model scale、decoding configurations、LoRA-only validation）、engineering considerations（tokenizer、scalability bounds）。两个遗漏：（1）empirically derived constraints 继承训练数据偏差/覆盖率不足的风险（§2 提到 99%+ coverage 但未讨论 bias）；（2）low zero-shot F1 (2-8%) 下的约束行为是否外推到更高 F1 operating points 未讨论。\n\nEthics Statement 简洁适当。\n",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-19T08:47:51.381588+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5018
}
```

</details>

---


### Assistant

_source line 700 · 2026-05-19T08:47:59.104222+00:00_

审稿意见已提交给 Review Director。

总结：论文评分 **3.5 (Borderline Conference)**。核心贡献（将 IE schema 编译为两层 token-level 约束）技术上合理，实验分析诚实且深入。主要问题：（1）"near-lossless" 叙事被 CF trade-off 削弱（zero-shot CF 最高 12%），Abstract 需更诚实地呈现；（2）缺少与 GoLLIE 等 schema-aware IE 系统的直接 violation rate 对比；（3）dual-factor pattern 仅 4 个数据点（p=0.058）支撑不够。如果作者能解决 CF 叙事问题并补充 baseline 对比，有潜力提升至 Conference 档位。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 19

## Round 19

4 recorded events


### User

_source line 701 · 2026-05-19T08:48:49.476939+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见

以下是 Reviewer 2 的完整审稿原文，请逐条回应：对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

**Reviewer 2 评分**: 3.0 (Findings)
**一句话总结**: 工程完成度高、实验全面的 schema 约束解码系统，但核心技术贡献（entity registry + dynamic masking）的算法新颖性有限，且 CF 副作用是未解决的根本性缺陷。

**官方维度打分**: Soundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5, Confidence 4/5

### Strengths
**S1.** 全面且诚实的实验评估（3数据集×4模型×3解码策略，bootstrap显著性检验，Mistral boundary condition讨论，CF trade-off坦率承认）
**S2.** Constraint tightness 分析提供有价值的 insight（κ(r) 量化约束与违规率关系）
**S3.** 实用性强的部署配置（LoRA+S1: DR≤0.20%, R-F1 ±0.6pp, +10% latency）
**S4.** Fine-tuning 可组合性验证充分（Table 2, Appendix B Table 5）
**S5.** 附录信息密度高（14个附录，CF-DR trade-off pilot ablation Table 4）

### Must-Fix
**N1** [critical] 核心技术新颖性不足——Grammar层完全复用XGrammar，semantic层是字典查找+条件masking的直接实现。与type-constrained code generation的区别（"动态entity registry"）在实现层面仅体现为解码时维护字典并查询。论文未能充分回答：为什么字典查找+条件masking构成足够的算法贡献，而不仅是已有范式的工程适配？

**N2** [critical] CF trade-off是未解决的根本缺陷——zero-shot CF从0.08%升至9.90%(SciERC)、12.02%(Llama DocRED)。Table 4 pilot ablation证明CF优先化会推DR至14.78%，是结构性不可调和trade-off。Total violation burden(DR+CF)仅减少30%。论文将大量篇幅（~40%）用于zero-shot场景，但如果zero-shot因CF不可用，应重新分配。

### Should-Fix
**W1** [warning] Zero-shot R-F1过低（2-8%），实验主体实际意义有限——正文~40%围绕zero-shot，但辩护出现在附录
**W2** [warning] 缺少GoLLIE直接对比——"complementary"声称无实验验证
**W3** [warning] Dual-factor分析仅n=4，p≈0.058，正文措辞超出统计证据支撑
**W4** [warning] WikiEvents "preliminary"但Abstract中占显著位置
**W5** [warning] Abstract数字密度过高（~15个数字）
**W6** [warning] Entity registry correctness依赖生成顺序假设，未充分讨论字段顺序强制机制

### Minor
- BibTeX 10个orphan entries + 1 duplicate key
- DocRED dev set标注不一致
- S1/S2命名在Table 1中需简要定义
- Compile time不一致（44ms vs 0.33s）
- "Training-free"措辞与推荐配置（LoRA+S1需fine-tuning）矛盾

### Missing References
- TANL (Paolini et al., 2021)
- BoostCD (Sakota et al., 2025) 应是最重要baseline之一

---

请对以上每个要点逐条回应 [AGREE] 或 [REBUT]，特别关注：
1. R2 认为技术新颖性不足（N1），你的评估是什么？
2. R2 给出 Excitement 2.5/5，你给 3/5，分歧原因是什么？
3. R2 建议将贡献定位为"系统性实证研究+工程框架"而非方法论创新，你是否同意？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-19T08:51:00.461018+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 — 交叉回应 Reviewer 2\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1**: 同意。实验评估的全面性和诚实度是本文最大亮点，我在 S3/S4 中也给出了类似评价。特别是 CF trade-off pilot ablation（Appendix B, Table 5）和 Mistral boundary condition 分析展示了少见的科学诚实度。\n\n**[AGREE] R2-S2**: 同意。κ(r) 作为解释框架有分析价值，但我在 W1 中指出了 n=4 的统计局限性。R2 在 W3 中也有同样的担忧，我们在此一致。\n\n**[AGREE] R2-S3**: 同意。LoRA+S1 配置的实用性（DR≤0.20%, +10% latency）是论文最有价值的工程贡献。\n\n**[AGREE] R2-S4**: 同意。Table 2 + Appendix B Table 8 的 4-way fine-tuned ablation 验证了两层约束在 fine-tuning 后各自的独立贡献（semantic layer 单独贡献 39-72% DR reduction）。\n\n**[AGREE] R2-S5**: 同意。附录信息密度高，特别是 residual DR error analysis（Appendix B, 4类root cause分解）和 per-relation DR elimination（Appendix B Table 7）。\n\n---\n\n### Must-Fix 回应\n\n**[REBUT] R2-N1**: 核心技术新颖性不足\n\nR2 将 semantic 层简化为\"字典查找+条件masking的直接实现\"，我认为这一评价过于简化，低估了以下设计贡献：\n\n1. **Sequential pair-based enforcement 不是 trivial 的字典查找。** §3.1 的形式化证明了 sequential masking（先 τ^h ∈ dom(r)，再 τ^t ∈ range(r, τ^h)）等价于完整 pair check (τ^h, τ^t) ∈ σ(r)，且严格强于 independent enforcement。脚注量化了 independent check 的 over-permission：SciERC 1.50×，DocRED 1.58×（33-37% spurious pairs）。这不是工程选择，而是正确性要求。\n\n2. **Enabling dependency 是经实证验证的架构洞察。** Table 1 的消融表明 semantic-only 仅降 DR 24%，加入 grammar 层后降至 94%。这不是\"叠加两个组件\"的简单结果——原因是 semantic 层依赖 grammar 层保证的 vocabulary membership 才能执行 domain/range 查找（§4, Eq. 3）。这一依赖关系在 constrained decoding 文献中未被形式化过。\n\n3. **Continuation masking 解决了非平凡的 tokenizer 兼容性问题。** §3.2 描述的 prefix-shared types 问题（如 WikiEvents 的 SEN/SID/Side）不是简单的 token mapping——SentencePiece 和 byte-level BPE 的 context-dependent tokenization 使得同一 type name 在不同 prefix 下产生不同 token 序列。compile-time prefix map + decode-time continuation 的方案覆盖了 3 种 tokenizer 家族。\n\n4. **与 code generation 的区别不仅是\"动态字典\"。** §3 第 9 行明确了三个区别：(1) entity types 从 free text 推断而非 declared，(2) entity registry 在生成中动态构建，(3) constraint targets 是 context-dependent 而非 fixed grammar productions。PICARD/Synchromesh 操作在 fully enumerated schema 上（所有 column names 预知），而 OntoCoDec 的 constraint set 随 decoded prefix 演化。\n\n**但我也承认 R2 的担忧有一定道理。** 从纯算法角度看，individual components 确实不复杂。论文的贡献更在于：(a) 将 type-constrained decoding 从 code generation 迁移到 IE 领域（§6 Related Work appendix 最后一段明确了这一定位），(b) 系统性地分析了约束与模型能力的交互（tightness, calibration, CF trade-off）。我在 Excitement 评分中反映了这一判断（3/5 而非更高）。\n\n**结论：R2-N1 作为 Should-Fix（W 级）更合适，不应是 Must-Fix。** 论文的贡献是 methods + empirical analysis 的组合，而非纯算法创新。降级为 Should-Fix 的条件是作者在 Introduction 中更清晰地定位贡献类型。\n\n---\n\n**[AGREE] R2-N2**: CF trade-off 是根本性限制\n\n我在 N1 中提出了本质相同的问题。补充 R2 的分析：\n\n- Total violation burden (DR+CF) 在 SciERC zero-shot 下：15.45% → 10.83%，净减仅 30%（我和 R2 的计算一致）\n- 但在推荐配置 LoRA+S1 下：Qwen SciERC 1.95% → 1.18%（净减 39%），Qwen DocRED 0.88% → 0.42%（净减 52%）——虽然幅度较小，但方向是正确的\n- Beam search + LoRA 在 SciERC 上消除所有四种 violation（§5.6, Appendix F），完全解决 CF\n\n**与 R2 的微分歧：** R2 建议\"如果 zero-shot 因 CF 不可用，应重新分配篇幅\"。我认为 zero-shot 实验作为 constraint robustness 的 stress-test 仍有价值（§5 开头明确了这一定位），但 Abstract 和 Introduction 的叙事权重确实应向 fine-tuning 配置倾斜。问题不是 zero-shot 实验不该做，而是 narrative framing 给了 zero-shot 过多的 prominence。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R2-W1**: Zero-shot R-F1 实际意义有限\n\n同意 R2 的判断。论文在 Appendix B（Practical Significance of Zero-Shot F1）中辩护 zero-shot F1 是 \"control variable\" 而非 \"optimization target\"，这一论点合理但放在附录中弱化了说服力。我在审稿中未将此列为独立问题，但认同 R2 的观察：正文 ~40% 篇幅围绕 zero-shot，与其在总体贡献中的权重不匹配。\n\n**[AGREE] R2-W2**: 缺少 GoLLIE 对比\n\n与我的 N2 完全一致。GoLLIE 将 schema 编码为 Python dataclass 并在 SciERC 上有公开结果，至少应报告其 violation rates 作为参照。\n\n**[AGREE] R2-W3**: Dual-factor n=4\n\n与我的 W1 完全一致。n=4, p≈0.058, df=2。论文在 Appendix B 中措辞谨慎（\"descriptive characterization\"），但正文§4中使用 \"consistent with\" 和 \"supports\" 等措辞暗示了因果性。\n\n**[AGREE] R2-W4**: WikiEvents \"preliminary\" 但 Abstract 位置显著\n\n与我的 W2 一致。Abstract line 10 和 Contribution 3 应加 \"preliminary\" 限定。\n\n**[REBUT] R2-W5**: Abstract 数字密度过高\n\n部分反驳。Abstract 确实包含约 15 个数字，但多数服务于核心 claim 的量化支撑。对于一篇以实证分析为主要贡献的论文，Abstract 中缺少关键数字反而会削弱可信度。**但 R2 的建议方向是对的**——可以合并部分数字（如 \"DR≤0.20% with R-F1 within ±0.6pp\" 已经是高效的压缩表述），去掉 beam search 数字（正文已有）可减少 2-3 个数字而不损失叙事。这是 minor-level 问题而非 Should-Fix。\n\n**[AGREE] R2-W6**: Entity registry 字段顺序假设\n\n我在 minor issues 中也提到了这一点。§3.1 line 28 确实说明了 \"fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation\"，Eq.1 的 output schema 也隐含了 entities 在 relations 之前生成。但 R2 指出的问题更深层：如果模型在 relation 中引用了 entity list 未生成的实体怎么办？§3.2 line 70-71 部分回答了这个问题（\"if h_j ∈ D ... Otherwise, if r_j is known, the mask falls back to all domain-valid types\"），但这个 fallback 行为及其对 CF 的影响值得更显式的讨论。\n\n---\n\n### Minor 回应\n\n**[AGREE]** BibTeX orphan entries + duplicate key：文献管理问题，应在提交前清理。\n\n**[AGREE]** S1/S2 命名在 Table 1 中需定义：Table 1 caption 未解释 S1/S2，读者需翻到 §3.3 才能理解。建议在 Table 1 caption 或脚注中加一句。\n\n**[AGREE]** Compile time 不一致（44ms vs 0.33s）：我也标记了这个问题。Appendix B 的 0.044s 可能是 semantic compile，Appendix J 的 0.33s 是 grammar compile（XGrammar EBNF 编译），论文未区分。\n\n**[REBUT]** \"Training-free\" 措辞矛盾：部分反驳。OntoCoDec 本身确实是 training-free 的——约束编译和执行不需要训练。推荐配置中的 LoRA 是 base model 的 fine-tuning，不是 OntoCoDec 的组成部分。§1 line 31 的表述 \"OntoCoDec is training-free and applies to any autoregressive LM\" 准确描述了 OntoCoDec 本身的性质。但 R2 的担忧是合理的：读者可能将 \"training-free\" 理解为整个推荐流程不需要训练。建议在 Introduction 中明确：\"OntoCoDec is training-free; it composes with optional fine-tuning for deployment.\"\n\n**[AGREE]** DocRED dev set 标注不一致：§5（sec:violation_landscape）脚注已说明 \"DocRED test annotations are not publicly available; we evaluate on the development set\"，这是 DocRED 社区标准做法，但在表格中应统一标注。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** TANL (Paolini et al., 2021)：structured prediction as translation，与 OntoCoDec 的 structured generation 框架直接相关，应引用。\n\n**[REBUT]** BoostCD 作为\"最重要 baseline 之一\"：BoostCD 已在 §6 Related Work 中引用（line 24: \"BoostCD~\\cite{boostcd2025} combines constrained and unconstrained decoding for IE\"）。R2 可能指应在实验中比较，而非仅引用。但 BoostCD 的 constrained + unconstrained 混合解码与 OntoCoDec 的 full-time constraint enforcement 是不同的设计哲学，作为 baseline 的可比性有限。如果 R2 的意思是实验对比，建议作者讨论 BoostCD 的 violation rates（如果可获得），但不应列为 \"最重要 baseline\"。\n\n---\n\n### Director 提问的三个问题\n\n**Q1: R2 认为技术新颖性不足（N1），我的评估是什么？**\n\n我认为 R2 的评估部分正确但过于严苛。论文的贡献不是纯算法创新，而是：(a) 将 type-constrained decoding 范式从 code generation 迁移到 IE，识别并解决了迁移中的关键差异（dynamic registry, non-rectangular σ(r), tokenizer 兼容性）；(b) 系统性的实证分析（violation landscape, tightness-violation correlation, CF trade-off characterization, enabling dependency）。这类 \"formalization + systematic analysis\" 的贡献在 ACL/EMNLP 中是被接受的贡献类型，尽管不如纯 novel algorithm 令人兴奋。我将 N1 评为 Should-Fix 而非 Must-Fix 更合适。\n\n**Q2: Excitement 2.5 vs 3.0 的分歧原因**\n\nR2 的 2.5/5 重度权衡了算法新颖性，将论文视为\"已有范式的工程适配\"。我的 3/5 额外 credit 了：(1) 问题定义的精确性（四类 violation 分类学）；(2) 实证分析的深度（CF dual mechanism, boundary condition, residual DR decomposition）；(3) 对 constrained decoding 文献的推进（enabling dependency 的形式化验证）。在 *ACL 系统中，thorough empirical contribution 历来是 3/5 Excitement 的典型水平。2.5/5 意味着\"potentially interesting but doesn't resonate\"，我认为对这篇论文过低——它对 IE 社区有实际参考价值。\n\n**Q3: 是否同意定位为\"系统性实证研究+工程框架\"而非方法论创新？**\n\n**部分同意。** 论文最强的贡献确实是实证分析（violation landscape、tightness 分析、CF trade-off 表征、enabling dependency 验证）和可部署的工程框架（LoRA+S1 配置）。重新定位可以：(1) 避免审稿人对 \"novel method\" 的更高期待；(2) 更好地匹配论文的实际优势。但完全放弃方法贡献也不合适——sequential pair-based enforcement 的正确性论证、enabling dependency 的形式化、continuation masking 的跨 tokenizer 方案都超出了纯工程实现的范畴。建议定位为 **\"methods-informed empirical study\"**：以方法框架为载体，核心贡献是对 type violation 问题的系统性分析和可验证的解决方案。\n\n---\n\n### 综合评估\n\n两位 Reviewer 在以下问题上达成共识：\n1. CF trade-off 是核心叙事问题（R1-N1 ≈ R2-N2）\n2. 缺少 GoLLIE 等 schema-aware baseline（R1-N2 ≈ R2-W2）\n3. Dual-factor 统计不足（R1-W1 ≈ R2-W3）\n4. WikiEvents preliminary 但 Abstract 位置过高（R1-W2 ≈ R2-W4）\n\n主要分歧在 R2-N1（技术新颖性）。我认为 R2 的评价偏严苛，论文的 formalization + empirical analysis 组合足以支撑 Borderline Conference (3.5) 而非 Findings (3.0)。\n\n**我维持 Overall 3.5 (Borderline Conference) 的评分。**\n",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 — 交叉回应 Reviewer 2\n\n---\n\n### Strengths 回应\n\n**[AGREE] R2-S1**: 同意。实验评估的全面性和诚实度是本文最大亮点，我在 S3/S4 中也给出了类似评价。特别是 CF trade-off pilot ablation（Appendix B, Table 5）和 Mistral boundary condition 分析展示了少见的科学诚实度。\n\n**[AGREE] R2-S2**: 同意。κ(r) 作为解释框架有分析价值，但我在 W1 中指出了 n=4 的统计局限性。R2 在 W3 中也有同样的担忧，我们在此一致。\n\n**[AGREE] R2-S3**: 同意。LoRA+S1 配置的实用性（DR≤0.20%, +10% latency）是论文最有价值的工程贡献。\n\n**[AGREE] R2-S4**: 同意。Table 2 + Appendix B Table 8 的 4-way fine-tuned ablation 验证了两层约束在 fine-tuning 后各自的独立贡献（semantic layer 单独贡献 39-72% DR reduction）。\n\n**[AGREE] R2-S5**: 同意。附录信息密度高，特别是 residual DR error analysis（Appendix B, 4类root cause分解）和 per-relation DR elimination（Appendix B Table 7）。\n\n---\n\n### Must-Fix 回应\n\n**[REBUT] R2-N1**: 核心技术新颖性不足\n\nR2 将 semantic 层简化为\"字典查找+条件masking的直接实现\"，我认为这一评价过于简化，低估了以下设计贡献：\n\n1. **Sequential pair-based enforcement 不是 trivial 的字典查找。** §3.1 的形式化证明了 sequential masking（先 τ^h ∈ dom(r)，再 τ^t ∈ range(r, τ^h)）等价于完整 pair check (τ^h, τ^t) ∈ σ(r)，且严格强于 independent enforcement。脚注量化了 independent check 的 over-permission：SciERC 1.50×，DocRED 1.58×（33-37% spurious pairs）。这不是工程选择，而是正确性要求。\n\n2. **Enabling dependency 是经实证验证的架构洞察。** Table 1 的消融表明 semantic-only 仅降 DR 24%，加入 grammar 层后降至 94%。这不是\"叠加两个组件\"的简单结果——原因是 semantic 层依赖 grammar 层保证的 vocabulary membership 才能执行 domain/range 查找（§4, Eq. 3）。这一依赖关系在 constrained decoding 文献中未被形式化过。\n\n3. **Continuation masking 解决了非平凡的 tokenizer 兼容性问题。** §3.2 描述的 prefix-shared types 问题（如 WikiEvents 的 SEN/SID/Side）不是简单的 token mapping——SentencePiece 和 byte-level BPE 的 context-dependent tokenization 使得同一 type name 在不同 prefix 下产生不同 token 序列。compile-time prefix map + decode-time continuation 的方案覆盖了 3 种 tokenizer 家族。\n\n4. **与 code generation 的区别不仅是\"动态字典\"。** §3 第 9 行明确了三个区别：(1) entity types 从 free text 推断而非 declared，(2) entity registry 在生成中动态构建，(3) constraint targets 是 context-dependent 而非 fixed grammar productions。PICARD/Synchromesh 操作在 fully enumerated schema 上（所有 column names 预知），而 OntoCoDec 的 constraint set 随 decoded prefix 演化。\n\n**但我也承认 R2 的担忧有一定道理。** 从纯算法角度看，individual components 确实不复杂。论文的贡献更在于：(a) 将 type-constrained decoding 从 code generation 迁移到 IE 领域（§6 Related Work appendix 最后一段明确了这一定位），(b) 系统性地分析了约束与模型能力的交互（tightness, calibration, CF trade-off）。我在 Excitement 评分中反映了这一判断（3/5 而非更高）。\n\n**结论：R2-N1 作为 Should-Fix（W 级）更合适，不应是 Must-Fix。** 论文的贡献是 methods + empirical analysis 的组合，而非纯算法创新。降级为 Should-Fix 的条件是作者在 Introduction 中更清晰地定位贡献类型。\n\n---\n\n**[AGREE] R2-N2**: CF trade-off 是根本性限制\n\n我在 N1 中提出了本质相同的问题。补充 R2 的分析：\n\n- Total violation burden (DR+CF) 在 SciERC zero-shot 下：15.45% → 10.83%，净减仅 30%（我和 R2 的计算一致）\n- 但在推荐配置 LoRA+S1 下：Qwen SciERC 1.95% → 1.18%（净减 39%），Qwen DocRED 0.88% → 0.42%（净减 52%）——虽然幅度较小，但方向是正确的\n- Beam search + LoRA 在 SciERC 上消除所有四种 violation（§5.6, Appendix F），完全解决 CF\n\n**与 R2 的微分歧：** R2 建议\"如果 zero-shot 因 CF 不可用，应重新分配篇幅\"。我认为 zero-shot 实验作为 constraint robustness 的 stress-test 仍有价值（§5 开头明确了这一定位），但 Abstract 和 Introduction 的叙事权重确实应向 fine-tuning 配置倾斜。问题不是 zero-shot 实验不该做，而是 narrative framing 给了 zero-shot 过多的 prominence。\n\n---\n\n### Should-Fix 回应\n\n**[AGREE] R2-W1**: Zero-shot R-F1 实际意义有限\n\n同意 R2 的判断。论文在 Appendix B（Practical Significance of Zero-Shot F1）中辩护 zero-shot F1 是 \"control variable\" 而非 \"optimization target\"，这一论点合理但放在附录中弱化了说服力。我在审稿中未将此列为独立问题，但认同 R2 的观察：正文 ~40% 篇幅围绕 zero-shot，与其在总体贡献中的权重不匹配。\n\n**[AGREE] R2-W2**: 缺少 GoLLIE 对比\n\n与我的 N2 完全一致。GoLLIE 将 schema 编码为 Python dataclass 并在 SciERC 上有公开结果，至少应报告其 violation rates 作为参照。\n\n**[AGREE] R2-W3**: Dual-factor n=4\n\n与我的 W1 完全一致。n=4, p≈0.058, df=2。论文在 Appendix B 中措辞谨慎（\"descriptive characterization\"），但正文§4中使用 \"consistent with\" 和 \"supports\" 等措辞暗示了因果性。\n\n**[AGREE] R2-W4**: WikiEvents \"preliminary\" 但 Abstract 位置显著\n\n与我的 W2 一致。Abstract line 10 和 Contribution 3 应加 \"preliminary\" 限定。\n\n**[REBUT] R2-W5**: Abstract 数字密度过高\n\n部分反驳。Abstract 确实包含约 15 个数字，但多数服务于核心 claim 的量化支撑。对于一篇以实证分析为主要贡献的论文，Abstract 中缺少关键数字反而会削弱可信度。**但 R2 的建议方向是对的**——可以合并部分数字（如 \"DR≤0.20% with R-F1 within ±0.6pp\" 已经是高效的压缩表述），去掉 beam search 数字（正文已有）可减少 2-3 个数字而不损失叙事。这是 minor-level 问题而非 Should-Fix。\n\n**[AGREE] R2-W6**: Entity registry 字段顺序假设\n\n我在 minor issues 中也提到了这一点。§3.1 line 28 确实说明了 \"fixed field ordering (head → tail → relation → head_type → tail_type) via deterministic grammar compilation\"，Eq.1 的 output schema 也隐含了 entities 在 relations 之前生成。但 R2 指出的问题更深层：如果模型在 relation 中引用了 entity list 未生成的实体怎么办？§3.2 line 70-71 部分回答了这个问题（\"if h_j ∈ D ... Otherwise, if r_j is known, the mask falls back to all domain-valid types\"），但这个 fallback 行为及其对 CF 的影响值得更显式的讨论。\n\n---\n\n### Minor 回应\n\n**[AGREE]** BibTeX orphan entries + duplicate key：文献管理问题，应在提交前清理。\n\n**[AGREE]** S1/S2 命名在 Table 1 中需定义：Table 1 caption 未解释 S1/S2，读者需翻到 §3.3 才能理解。建议在 Table 1 caption 或脚注中加一句。\n\n**[AGREE]** Compile time 不一致（44ms vs 0.33s）：我也标记了这个问题。Appendix B 的 0.044s 可能是 semantic compile，Appendix J 的 0.33s 是 grammar compile（XGrammar EBNF 编译），论文未区分。\n\n**[REBUT]** \"Training-free\" 措辞矛盾：部分反驳。OntoCoDec 本身确实是 training-free 的——约束编译和执行不需要训练。推荐配置中的 LoRA 是 base model 的 fine-tuning，不是 OntoCoDec 的组成部分。§1 line 31 的表述 \"OntoCoDec is training-free and applies to any autoregressive LM\" 准确描述了 OntoCoDec 本身的性质。但 R2 的担忧是合理的：读者可能将 \"training-free\" 理解为整个推荐流程不需要训练。建议在 Introduction 中明确：\"OntoCoDec is training-free; it composes with optional fine-tuning for deployment.\"\n\n**[AGREE]** DocRED dev set 标注不一致：§5（sec:violation_landscape）脚注已说明 \"DocRED test annotations are not publicly available; we evaluate on the development set\"，这是 DocRED 社区标准做法，但在表格中应统一标注。\n\n---\n\n### Missing References 回应\n\n**[AGREE]** TANL (Paolini et al., 2021)：structured prediction as translation，与 OntoCoDec 的 structured generation 框架直接相关，应引用。\n\n**[REBUT]** BoostCD 作为\"最重要 baseline 之一\"：BoostCD 已在 §6 Related Work 中引用（line 24: \"BoostCD~\\cite{boostcd2025} combines constrained and unconstrained decoding for IE\"）。R2 可能指应在实验中比较，而非仅引用。但 BoostCD 的 constrained + unconstrained 混合解码与 OntoCoDec 的 full-time constraint enforcement 是不同的设计哲学，作为 baseline 的可比性有限。如果 R2 的意思是实验对比，建议作者讨论 BoostCD 的 violation rates（如果可获得），但不应列为 \"最重要 baseline\"。\n\n---\n\n### Director 提问的三个问题\n\n**Q1: R2 认为技术新颖性不足（N1），我的评估是什么？**\n\n我认为 R2 的评估部分正确但过于严苛。论文的贡献不是纯算法创新，而是：(a) 将 type-constrained decoding 范式从 code generation 迁移到 IE，识别并解决了迁移中的关键差异（dynamic registry, non-rectangular σ(r), tokenizer 兼容性）；(b) 系统性的实证分析（violation landscape, tightness-violation correlation, CF trade-off characterization, enabling dependency）。这类 \"formalization + systematic analysis\" 的贡献在 ACL/EMNLP 中是被接受的贡献类型，尽管不如纯 novel algorithm 令人兴奋。我将 N1 评为 Should-Fix 而非 Must-Fix 更合适。\n\n**Q2: Excitement 2.5 vs 3.0 的分歧原因**\n\nR2 的 2.5/5 重度权衡了算法新颖性，将论文视为\"已有范式的工程适配\"。我的 3/5 额外 credit 了：(1) 问题定义的精确性（四类 violation 分类学）；(2) 实证分析的深度（CF dual mechanism, boundary condition, residual DR decomposition）；(3) 对 constrained decoding 文献的推进（enabling dependency 的形式化验证）。在 *ACL 系统中，thorough empirical contribution 历来是 3/5 Excitement 的典型水平。2.5/5 意味着\"potentially interesting but doesn't resonate\"，我认为对这篇论文过低——它对 IE 社区有实际参考价值。\n\n**Q3: 是否同意定位为\"系统性实证研究+工程框架\"而非方法论创新？**\n\n**部分同意。** 论文最强的贡献确实是实证分析（violation landscape、tightness 分析、CF trade-off 表征、enabling dependency 验证）和可部署的工程框架（LoRA+S1 配置）。重新定位可以：(1) 避免审稿人对 \"novel method\" 的更高期待；(2) 更好地匹配论文的实际优势。但完全放弃方法贡献也不合适——sequential pair-based enforcement 的正确性论证、enabling dependency 的形式化、continuation masking 的跨 tokenizer 方案都超出了纯工程实现的范畴。建议定位为 **\"methods-informed empirical study\"**：以方法框架为载体，核心贡献是对 type violation 问题的系统性分析和可验证的解决方案。\n\n---\n\n### 综合评估\n\n两位 Reviewer 在以下问题上达成共识：\n1. CF trade-off 是核心叙事问题（R1-N1 ≈ R2-N2）\n2. 缺少 GoLLIE 等 schema-aware baseline（R1-N2 ≈ R2-W2）\n3. Dual-factor 统计不足（R1-W1 ≈ R2-W3）\n4. WikiEvents preliminary 但 Abstract 位置过高（R1-W2 ≈ R2-W4）\n\n主要分歧在 R2-N1（技术新颖性）。我认为 R2 的评价偏严苛，论文的 formalization + empirical analysis 组合足以支撑 Borderline Conference (3.5) 而非 Findings (3.0)。\n\n**我维持 Overall 3.5 (Borderline Conference) 的评分。**\n",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-19T08:51:04.827896+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4366
}
```

</details>

---


### Assistant

_source line 704 · 2026-05-19T08:51:10.399120+00:00_

交叉回应已提交。

共识点：CF trade-off 叙事问题、缺少 schema-aware baseline、dual-factor 统计不足、WikiEvents 限定词缺失。

主要分歧在 R2-N1（技术新颖性）：我认为 R2 的"纯工程适配"评价过于严苛，sequential pair-based enforcement 的正确性论证、enabling dependency 的形式化验证、continuation masking 的跨 tokenizer 方案超越了纯工程范畴。将 N1 评为 Should-Fix 更合适。维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 20

## Round 20

88 recorded events


### User

_source line 705 · 2026-05-20T17:09:05.300513+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**。

## 论文信息
- **标题**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`

## Venue 要求
- **目标**: EMNLP 2026 via ARR May 2026
- **截止**: 2026-05-25
- **格式**: ACL 模板 [review] 模式，Long paper 正文 8 页，参考文献不限
- **匿名**: Double-blind（不得透露作者身份）
- **必需**: Limitations section（不计页数）+ ARR Responsible NLP Research Checklist
- **附录**: 允许，但审稿人无义务阅读

## 你的审查侧重

### 1. 形式化与方法论
- Proposition 1（Level 2 ⊄ Level 1）的证明是否严谨？有无逻辑漏洞？
- 约束可决性分类（context-free / prefix-decidable with state / non-local）是否完备且互斥？
- Grammar-first fallback 的正确性保证——是否存在 corner case 导致无效输出？
- Entity registry 的 soundness：动态构建过程中的 race condition 或顺序依赖问题
- Sequential pair-based enforcement 的 exact 声称是否成立？

### 2. 实验设计与统计
- Five-way ablation 设计是否充分隔离了各层贡献？
- Bootstrap 检验的使用是否规范（样本量、迭代次数、报告格式）
- Cross-model validation（3 models）和 cross-dataset（SciERC/DocRED/WikiEvents）的覆盖是否足够
- Fine-tuning composability 实验中的 confound 控制（LoRA 超参、learning rate）
- Beam search 实验的规模（SciERC 551 docs full set vs DocRED 50/998 docs）
- Zero-shot R-F1 2-8% 是否有意义作为 diagnostic——是否混淆了 constraint 效果与模型能力
- WikiEvents 20-doc test set 的统计效力
- Runtime overhead 测量方法和环境控制

### 3. 可复现性
- 实验是否提供了足够的细节以支持独立复现
- Constraint compilation 代码是否有开源承诺
- 数据集处理细节（DocRED dev set 选择原因、WikiEvents split）

请以 ARR reviewer 标准完成审稿，输出包含：Summary、Strengths（逐条）、Weaknesses（逐条，按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-20T17:09:14.306016+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-20T17:09:14.408177+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_1_11179fb2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-20T17:09:15.365346+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 709 · 2026-05-20T17:09:15.416885+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-20T17:09:20.742403+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-20T17:09:22.295384+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "1-10",
  "dpi": "150",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "1-10",
    "dpi": "150",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-20T17:09:22.821398+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 713 · 2026-05-20T17:09:28.404938+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ACL ARR reviewer guidelines for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation, and you need to revise it.

### Excitement Score
Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper.

## Area Chair Guidelines

Area chairs should mostly follow the soundness assessment of the reviewers when they are in agreement, and they can weigh in when there is a disagreement or serious issues with reviews. The Findings/main conference distin
…[truncated 569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7662
}
```

</details>

---


### Tool result

_source line 714 · 2026-05-20T17:09:29.815850+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.6}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 510.3}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 531.0}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 527.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 481.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"w
…[truncated 520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7520
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-20T17:10:27.091435+00:00_

&lt;persisted-output>
Output too large (54.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/5f790f87-b907-45b5-94a2-b64118852f83/tool-results/toolu_01HC8uMkxq5GQAa77Pr173z8.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 67, \"total_citations\": 93, \"unique_cited_keys\": 56, \"orphan_bib\": 10, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 52, \"online_not_found\": 3, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"slot2025\"], \"missing_bib\": [], \"orphan_count\": 10, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_y
…[truncated 371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 64270
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-20T17:10:33.517940+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer scoring criteria, review form dimensions, scoring scales (1-5), and what each score means. Include all dimensions: soundness, excitement, overall assessment, confidence, etc. Also extract any guidelines about what constitutes a good review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer scoring criteria, review form dimensions, scoring scales (1-5), and what each score means. Include all dimensions: soundness, excitement, overall assessment, confidence, etc. Also extract any guidelines about what constitutes a good review."
  }
}
```

</details>

---


### Tool call

_source line 717 · 2026-05-20T17:10:34.377867+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-20T17:10:34.831767+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 719 · 2026-05-20T17:10:35.754781+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-20T17:10:35.955688+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-20T17:10:36.614346+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2236
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-20T17:10:36.614834+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-20T17:10:37.121272+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2289
}
```

</details>

---


### Tool result

_source line 724 · 2026-05-20T17:10:37.979286+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2224
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-20T17:10:38.030732+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2075
}
```

</details>

---


### Tool result

_source line 726 · 2026-05-20T17:10:38.333127+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1718
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-20T17:10:39.890334+00:00_

# ARR Reviewer Scoring Criteria and Guidelines

## Scoring Dimensions

Based on the guidelines, ARR reviewers provide **three primary scores**:

1. **Soundness**: Assesses technical validity and methodological rigor. Scores must be justified by review text; low soundness scores require explicit fault identification.

2. **Excitement**: Reflects personal interest and subjective appeal, orthogonal to soundness assessment. This captures reviewer enthusiasm independent of technical merit.

3. **Overall Assessment**: An explicit recommendation for paper outcome (main conference, findings, reject, etc.). This composite score balances soundness, excitement, novelty, and potential impact.

## Additional Scoring Elements

- **Confidence Score**: Indicates reviewer certainty in their evaluation
- **Reproducibility Score**: Must be justified; assesses whether sufficient details exist for experiment reproduction

## Key Scoring Principles

**Alignment requirement**: "The soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

**Balanced perspective**: Papers need not achieve SOTA status for acceptance; reviewers should recognize contributions across "efficiency, generalizability, interpretability, fairness, etc."

## Good Review Hallmarks

- Specific, evidence-based critiques with concrete references
- Professional, neutral tone avoiding sarcasm
- Clear distinction between weaknesses and personal preferences
- Engagement with author responses
- Awareness of common reviewer biases (H1-H17 heuristics listed in guidelines)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6372
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-20T17:10:44.761838+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 729 · 2026-05-20T17:10:45.314846+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 730 · 2026-05-20T17:10:45.823932+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 731 · 2026-05-20T17:10:46.677395+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1915
}
```

</details>

---


### Tool call

_source line 732 · 2026-05-20T17:10:46.678906+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 733 · 2026-05-20T17:10:47.135831+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-20T17:10:47.590131+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2275
}
```

</details>

---


### Tool result

_source line 735 · 2026-05-20T17:10:49.150853+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3326
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-20T17:10:50.160254+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3024
}
```

</details>

---


### Tool result

_source line 737 · 2026-05-20T17:10:50.161492+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3482
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-20T17:10:56.949344+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "11-20",
  "dpi": "150",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "11-20",
    "dpi": "150",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-20T17:11:00.066171+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 603.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 620.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 369.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.4}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.9}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.3}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 569.3}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3116
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-20T17:11:00.367879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/5f790f87-b907-45b5-94a2-b64118852f83/tool-results/toolu_01HC8uMkxq5GQAa77Pr173z8.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-review-reviewer-1-11179fb2/5f790f87-b907-45b5-94a2-b64118852f83/tool-results/toolu_01HC8uMkxq5GQAa77Pr173z8.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-20T17:11:00.671198+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 67, \"total_citations\": 93, \"unique_cited_keys\": 56, \"orphan_bib\": 10, \"missing_bib\": 0, \"duplicate_keys\": 1, \"online_verified\": 52, \"online_not_found\": 3, \"online_mismatch\": 11}, \"cross_check\": {\"orphan_bib\": [\"delafuente2025guidex\", \"geng2025jsonschemabench\", \"lee2026formattax\", \"lu2025schemarl\", \"park2024grammaraligned\", \"reddy2026dccd\", \"sakota2025boostcd\", \"schema_rl2025\", \"shen2025slot\", \"slot2025\"], \"missing_bib\": [], \"orphan_count\": 10, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \
…[truncated 54221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 742 · 2026-05-20T17:11:09.804872+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 743 · 2026-05-20T17:11:10.309915+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 744 · 2026-05-20T17:11:10.916548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool call

_source line 745 · 2026-05-20T17:11:10.917078+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 746 · 2026-05-20T17:11:11.721141+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-20T17:11:11.721937+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-20T17:11:11.823982+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 749 · 2026-05-20T17:11:12.025303+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 750 · 2026-05-20T17:11:12.230555+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 406
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-20T17:11:12.834993+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-20T17:11:17.001646+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool call

_source line 753 · 2026-05-20T17:11:17.656005+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool result

_source line 754 · 2026-05-20T17:11:18.012907+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1011
}
```

</details>

---


### Tool call

_source line 755 · 2026-05-20T17:11:18.015215+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 756 · 2026-05-20T17:11:18.973607+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1317
}
```

</details>

---


### Tool call

_source line 757 · 2026-05-20T17:11:18.974114+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 758 · 2026-05-20T17:11:19.780552+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-20T17:11:20.686668+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2671
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-20T17:11:20.687108+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "pages": "21-31",
  "dpi": "150",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "pages": "21-31",
    "dpi": "150",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 761 · 2026-05-20T17:11:21.042538+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2068
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-20T17:11:21.599616+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1819
}
```

</details>

---


### Tool result

_source line 763 · 2026-05-20T17:11:23.008342+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 483.5}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.3}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.0}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.9}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.5}, {\"page\": 26, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.4}, {\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 494.5}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.7}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2321
}
```

</details>

---


### Tool call

_source line 764 · 2026-05-20T17:11:27.329734+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
  }
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-20T17:11:27.832373+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
  }
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-20T17:11:28.235061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 767 · 2026-05-20T17:11:28.386880+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 768 · 2026-05-20T17:11:28.539409+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 769 · 2026-05-20T17:11:28.540094+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
  }
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-20T17:11:29.198192+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-20T17:11:29.552790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1165
}
```

</details>

---


### Tool result

_source line 772 · 2026-05-20T17:11:30.005843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1465
}
```

</details>

---


### Tool result

_source line 773 · 2026-05-20T17:11:30.308227+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---


### Tool call

_source line 774 · 2026-05-20T17:11:34.777231+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 775 · 2026-05-20T17:11:35.679804+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 776 · 2026-05-20T17:11:35.680235+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
  }
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-20T17:11:36.132790+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-20T17:11:36.636829+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 779 · 2026-05-20T17:11:36.637281+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
  }
}
```

</details>

---


### Tool result

_source line 780 · 2026-05-20T17:11:37.090983+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 781 · 2026-05-20T17:11:37.091430+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 782 · 2026-05-20T17:11:37.896891+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1259
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-20T17:11:37.897714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 784 · 2026-05-20T17:11:37.998412+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
  }
}
```

</details>

---


### Tool result

_source line 785 · 2026-05-20T17:11:38.403590+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-20T17:19:22.779534+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**审查侧重**：方法严谨性 + 实验设计\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体形式化编译为 token-level 解码约束的框架。核心思路是对 IE 类型约束进行可判定性分析（decidability analysis），将其分为三层：(1) context-free（JSON 结构 + 词汇表）由 XGrammar 语法层处理；(2) prefix-decidable with state（domain/range 类型合法性）由语义层通过动态 entity registry + semantic masking 处理；(3) non-local（跨 field 语义一致性）由 beam search 或 post-hoc 解决。实验覆盖 SciERC、DocRED、WikiEvents 三个数据集，Qwen3-8B / Llama-3.1-8B / Mistral-7B 三个模型，包含五路消融、beam search 兼容性、LoRA 微调组合性等多维评估。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 可判定性引导的约束分层是新颖且有工程价值的，但核心形式化结果缺乏严格证明，\"exact enforcement\" 声称与 36.64% CF fallback rate 矛盾，部分实验统计效力不足。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 形式化框架有洞见但 Proposition 1 仅为 proof sketch；\"exact\" enforcement 声称被 CF fallback 显著削弱；实验方法论整体规范但 WikiEvents 统计效力不足 |\n| Excitement | 3.5/5 | 将形式语言理论的可判定性分析引入 IE 约束解码是新颖的视角；自动编译任意 IE 本体为约束有实际价值；但与 grammar-only baseline 相比语义层的边际增益在部分场景有限 |\n| Reproducibility | 4/5 | 附录提供了详尽的超参数、硬件配置、seed 验证、prompt 模板；承诺代码开源；但部分实验（DocRED beam search 仅 50 文档子集）的完整复现需要澄清 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 information extraction 领域，通读全文含 22 页附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Proposition 1 证明不严格，与论文的形式化定位不匹配\n- 具体位置：Section 3, §3.1, \"Proof sketch\"\n- 问题：论文的核心贡献之一是\"可判定性引导的约束分类\"（decidability-guided constraint classification），Proposition 1（Level 2 ⊄ Level 1）是支撑这一框架的关键理论结果。然而论文仅给出 \"proof sketch\"：构造了一个 relation r with dom(r) = {τ₁, τ₂} 和 n 个独立选类型的 entity，论证 head-type field 需要回读 τ_{e(i)}，因此 PDDA 是必要的。这个论证是直觉性的，缺少：(a) 到已知不可判定性/语言层次结果的形式化归约；(b) 对 \"independently unbound\" 的精确定义（实际中 schema 的 JSON 结构会限制 n 和 k 的范围）；(c) 完整的数学证明（至少应放在附录中）。\n- 为什么影响接收：如果论文将自身定位为\"第一个形式化编译 IE 本体约束\"的工作（Abstract: \"formally compiles\"），形式化结果的严格性是核心可信度的基础。一个仅有 proof sketch 的 proposition 无法支撑 \"formal\" 的声称。\n- 建议修改方向：(1) 在附录中提供完整的形式化证明，包括明确的语言定义、CFG 无法识别该语言的泵引理论证或闭包性质论证；(2) 或者降低形式化声称的力度，将 Proposition 1 明确标注为 conjecture/informal argument，并相应调整 abstract 和 introduction 的措辞。\n\n**N2** [critical] \"Exact enforcement\" 声称与 36.64% CF fallback rate 存在根本矛盾\n- 具体位置：Abstract (\"constraint tightness\"), §3.3 (\"exact pair-based enforcement\"), §4 (Constraint Composition), Appendix C Table 7-8\n- 问题：论文多处声称语义层实现了 \"exact\" 的 pair-based domain/range enforcement（§3.3）。但 Appendix C Table 8 显示 SciERC 上 GENERIC 类型的 conflicting-type pairs 占全部 CF violations 的 63.3%（155/245），grammar-first fallback 在 36.64% 的 type-bearing positions 被触发。当 fallback 触发时，语义约束被完全丢弃，退化为 grammar-only。这意味着约 1/3 的关键决策点上，系统实际并未执行语义约束。论文将此描述为\"a soft error detectable by downstream validation\"，但这与 \"exact enforcement\" 的声称矛盾。\n- 进一步的问题：fallback 是否会级联？一次 fallback 导致的错误类型赋值是否会影响后续 entity registry 的状态，从而触发更多 fallback？论文未分析级联失败（cascading failures）的可能性。\n- 为什么影响接收：如果核心技术声称（exact enforcement）在实践中有 1/3 的时间不成立，审稿人和读者会质疑方法的可靠性。这不是一个小的精度问题，而是核心 narrative 的准确性问题。\n- 建议修改方向：(1) 将 \"exact\" 修改为更精确的表述，如 \"best-effort pair-based enforcement with grammar-first fallback\"；(2) 分析 fallback 的级联行为；(3) 报告 fallback 后的 entity registry 状态一致性。\n\n**N3** [critical] WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力严重不足\n- 具体位置：§5.4 (Extension to Event Extraction), Table 5, Limitations (page 9)\n- 问题：WikiEvents 的 fine-tuning 评估使用标准 194/20/20 split（Li et al., 2021），测试集仅 20 篇文档。在如此小的样本上：(a) bootstrap p-values 不可靠；(b) 单个异常文档可大幅影响指标；(c) 置信区间极宽。论文在 Limitations 中披露了这一问题（\"WikiEvents fine-tuning composability is preliminary (20-document test set)\"），但正文 §5.4 的结论语气并未相应降低。例如 Table 5 直接与 SciERC/DocRED 的结果并列呈现，暗示同等可信度。\n- 为什么影响接收：20-doc 测试集上的数字无法支撑 \"framework generalizes to event extraction\" 的声称（§5.4 标题为 \"Extension to Event Extraction\"）。即使零样本评估用了 246 文档（更好），fine-tuning 组合性的结论仍然不够可靠。\n- 建议修改方向：(1) 在 §5.4 正文中明确标注测试集规模限制，降低结论语气；(2) 报告 WikiEvents fine-tuning 结果的 95% bootstrap 置信区间；(3) 考虑使用完整 246 文档进行 cross-validation 或 leave-one-out 评估来增强统计效力。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少与最相关并发工作的直接实验对比\n- 具体位置：§6 (Related Work), §5 (Experiments)\n- 问题：论文在 Related Work 中讨论了 BoostCD (Sakota et al., 2025)、CRANE (Banerjee et al., 2025)、IterGen (Ugare et al., 2025) 等同期工作，但实验中未与其直接对比。BoostCD 尤其相关——它也针对 IE 任务使用 constrained decoding，并在相同数据集（SciERC）上有结果。论文的 S1（grammar-only）配置隐式对标了 GCD (Geng et al., 2023)，但未明确展示 head-to-head 数字。\n- 为什么影响评分：缺乏直接对比使读者难以判断 OntoCoDec 相对于最新竞争方法的增量贡献。\n- 建议：至少在 SciERC 上与 BoostCD、GCD 进行直接数字对比（即使引用其论文报告的数字），并讨论评估设置差异。\n\n**W2** [warning] 跨模型验证局限于 7-8B 参数规模，泛化性声称不充分\n- 具体位置：§5 (Experiments), Limitations (page 9)\n- 问题：三个模型（Qwen3-8B, Llama-3.1-8B, Mistral-7B）均为 7-8B 参数量级。论文在 Limitations 中承认\"scaling to smaller models has not been verified\"，但正文的泛化性声称（如 Abstract: \"applies to any autoregressive LM\"）未加限定。更小的模型（1-3B）可能因能力不足导致更多 fallback；更大的模型（70B+）可能因基础能力更强而改变约束效果的模式。\n- 建议：(1) 在 Abstract/Introduction 中限定为 \"7-8B scale models\"；(2) 或增加至少一个不同规模的模型（如 Qwen3-1.8B 或 Llama-3.1-70B）的实验。\n\n**W3** [warning] 零样本 R-F1（0.08-8%）场景下 violation rate 分析的实际意义需要更明确的讨论\n- 具体位置：§5.1 Table 1, §5.2 Table 3, §5.3 Table 4\n- 问题：零样本设置下 R-F1 极低（SciERC 上 Qwen: 0.96%, Llama: ~0.08%），此时模型输出质量接近噪声水平。在这种条件下，violation rate（DR）的下降主要反映约束系统阻止了结构性错误，而非改善了抽取质量。论文将此定位为 \"diagnostic\"（§5 开头），这一定位是恰当的，但正文表格中零样本和微调结果并排呈现，读者可能误解零样本 DR 下降的实际价值。\n- 建议：在 §5.1 开头更明确地说明：零样本 ablation 的目的是隔离各层贡献的违规消除效果（而非抽取质量提升），R-F1 过低意味着该场景下的约束主要价值是结构合规而非 task performance。\n\n**W4** [warning] Entity registry 的顺序依赖可能导致 globally suboptimal type assignment\n- 具体位置：§3.3 (Entity Registry), §3.3 (Dynamic Masking)\n- 问题：Entity registry 在生成过程中动态构建，entity 类型赋值在生成时刻贪心确定。考虑以下场景：entity A 可被标注为类型 X 或 Y；如果贪心赋值为 X，后续某个 relation 需要类型 Y 的 head entity，导致 fallback 触发。如果赋值为 Y，则所有约束可满足。当前的贪心策略可能是局部最优但全局次优的。论文在 Appendix D 中通过 TCR（post-hoc type consistency resolution）部分解决了这个问题，但 TCR 是事后修复，不是生成时的 exact enforcement。\n- 建议：讨论 entity type assignment 的顺序依赖性和贪心策略的局限性，将其作为 Level 3（non-local）约束的一个实例。\n\n**W5** [warning] DocRED beam search 实验仅使用 50 文档子集\n- 具体位置：Appendix E, Table 15\n- 问题：SciERC 上 beam search 使用了完整 551 文档，但 DocRED 仅使用\"matched 50-document subsets\"。DocRED 文档更长（mean 198 tokens vs SciERC ~120 tokens）、关系类型更多（96 vs 7），beam search 在这类复杂文档上的表现可能与简单文档不同。50 文档子集可能不具代表性。\n- 建议：报告 50 文档的选择标准和代表性分析；或至少在全 998 文档的子样本上运行 beam search (k=2) 以验证趋势一致性。\n\n---\n\n## Questions to Authors\n\nQ1. Proposition 1 是否可以通过 pumping lemma for CFLs 或 Ogden's lemma 给出完整证明？当前的 proof sketch 中 \"n and k are independently unbound\" 的论证是否依赖于特定的 schema 结构？如果 schema 对 entity 数量设置上限（实际场景中常见），Proposition 1 是否仍然成立？\n\nQ2. Grammar-first fallback 的级联行为：当一次 fallback 导致 entity 被赋予非预期类型时，该 entity 会被注册到 entity registry 中。后续引用该 entity 的 relation 是否会因此触发更多 fallback？是否有实验数据量化这种级联效应？\n\nQ3. Table 1 中 S2（two-pass）的 DR 反而高于 Full S1——这是否说明 two-pass 架构引入了额外的错误来源（如第一阶段 entity extraction 的错误传播到第二阶段）？\n\nQ4. LoRA fine-tuning 使用统一超参数（r=16, α=32）对三个不同模型，是否做过超参数敏感性分析？特别是 Mistral-7B 在多个指标上表现弱于 Qwen 和 Llama——这是模型能力差异还是超参数不匹配？\n\nQ5. Constraint tightness κ（§4, Table 19 footnote area）的计算中，对称关系的处理方式是什么？论文 footnote 1 提到\"for symmetric relations, σ(r) counts ordered pairs; the denominator 2τ² remains appropriate since we evaluate on directed triples\"——这是否意味着对称关系的实际约束比 κ 值显示的更紧？\n\n---\n\n## Missing References / 比较\n\n1. **BoostCD (Sakota et al., 2025)**: 已引用但未实验对比。作为同样在 SciERC 上做 IE constrained decoding 的工作，缺乏直接数字对比是显著遗漏。\n2. **GCD (Geng et al., 2023)**: 已引用，S1 配置隐式对标，但应在实验部分明确展示 GCD 的数字作为 baseline。\n3. 可考虑引用 **Schema-RL (Lu et al., 2025)** 在正文中（目前仅在 bib 中未被引用），作为 training-based structured output 的对比方法。\n\n引用审计结果：\n- 10 条 orphan bib entries（在 .bib 中但未被引用）：包括 delafuente2025guidex, geng2025jsonschemabench, lee2026formattax 等，均为与已引用条目的重复版本。\n- 1 条重复 bib key: schall2025hiddencost 出现两次。\n- 3 条 online not found: regino2025kgcurator, formattax2026, lee2026formattax（后两者为同一论文的重复条目，arXiv 2604.03616 可能尚未被 OpenAlex 索引）。\n- 这些都是 minor cleanup 问题，不影响审稿判断。\n\n---\n\n## 小问题（不影响接收）\n\n- §4 Eq.(2)：M_final = M_grammar(t) ∧ M_semantic(t) 的 conjunction 是逐位 AND——应明确说明这是 token-level 的逐位操作而非 set intersection 的简写，避免歧义。\n- Table 1-3 中 \"CF\" 列的含义（context-free violation 即 cross-field violation）在首次出现时未充分解释，需要回读 §3 才能理解。建议在表格 caption 或首次引用处加注。\n- Figure 1（page 20）的 scatter plot：x 轴 label \"κ · RV_baseline\" 的物理含义不直观，建议在 caption 中补充解释。\n- Appendix G 报告 \"completion-only loss for 3 epochs\"——对于 DocRED（3,053 examples / 998 dev）仅 3 epochs 是否充分？是否观察到 loss 收敛？\n- Page 8, §6 Related Work 最后一段提到 \"the decidability taxonomy and a κ-diagnostic yield a principled deployment workflow\"——这读起来更像 contribution 声称而非 related work 讨论，建议调整位置。\n\n---\n\n## 主要优势\n\n1. **新颖的形式化视角**：将 formal language theory 的可判定性分析引入 IE 约束解码，提出 context-free / prefix-decidable with state / non-local 的三层分类。这在 constrained decoding for NLP 领域是新颖的，为系统设计提供了有原则的指导。\n\n2. **全面的实验设计**：五路消融清晰隔离了 grammar 层和 semantic 层的贡献；跨模型（3 个）、跨数据集（3 个）、跨任务（RE + EE）的覆盖在 systems paper 中高于平均水平。\n\n3. **诚实的局限性讨论**：论文对 WikiEvents 样本量、模型规模限制、CF trade-off 等问题的披露异常坦诚，这在投稿论文中值得肯定。\n\n4. **实际工程价值**：框架自动从任意 IE 本体编译约束，无需约束特定训练，可与任意自回归 LM 配合——这使其具有即插即用的实际部署价值。LoRA fine-tuning 组合性实验表明约束不干扰微调效果。\n\n5. **丰富的附录**：22 页附录包含详尽的错误分析（Appendix J case studies）、scalability benchmarks（Appendix K）、prompt 敏感性（Appendix I）、document length 分析（Appendix H）、TCR 机制（Appendix D/Tables 30-31）。这些内容显著增强了论文的可复现性和可信度。\n\n6. **Constraint tightness κ 指标**：作为部署指导工具（§4 末尾、Appendix C），κ 与 DR reduction 的相关性（Figure 2, r=0.886）为实践者提供了预测约束效果的依据——这是有实用价值的贡献。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n本文提出了一个有新意的框架，将形式语言理论的可判定性分析引入 IE 约束解码，实验覆盖面广且附录详尽。主要顾虑是：(1) 核心形式化结果（Proposition 1）仅为 proof sketch，与论文的 \"formally compiles\" 定位不匹配；(2) \"exact enforcement\" 的核心声称被 36.64% CF fallback rate 实质性削弱；(3) WikiEvents fine-tuning 评估的统计效力不足。如果作者能在修改中加强证明严格性、校准技术声称的精确度、并补充 WikiEvents 的统计分析，本文有潜力成为 solid conference paper。当前状态下，建议 Borderline Conference / strong Findings。\n\n**Confidence: 4/5** — 熟悉 constrained decoding 和 information extraction 领域，通读全文含全部 22 页附录及引用验证。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n**审查侧重**：方法严谨性 + 实验设计\n\n---\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体形式化编译为 token-level 解码约束的框架。核心思路是对 IE 类型约束进行可判定性分析（decidability analysis），将其分为三层：(1) context-free（JSON 结构 + 词汇表）由 XGrammar 语法层处理；(2) prefix-decidable with state（domain/range 类型合法性）由语义层通过动态 entity registry + semantic masking 处理；(3) non-local（跨 field 语义一致性）由 beam search 或 post-hoc 解决。实验覆盖 SciERC、DocRED、WikiEvents 三个数据集，Qwen3-8B / Llama-3.1-8B / Mistral-7B 三个模型，包含五路消融、beam search 兼容性、LoRA 微调组合性等多维评估。\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 可判定性引导的约束分层是新颖且有工程价值的，但核心形式化结果缺乏严格证明，\"exact enforcement\" 声称与 36.64% CF fallback rate 矛盾，部分实验统计效力不足。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 形式化框架有洞见但 Proposition 1 仅为 proof sketch；\"exact\" enforcement 声称被 CF fallback 显著削弱；实验方法论整体规范但 WikiEvents 统计效力不足 |\n| Excitement | 3.5/5 | 将形式语言理论的可判定性分析引入 IE 约束解码是新颖的视角；自动编译任意 IE 本体为约束有实际价值；但与 grammar-only baseline 相比语义层的边际增益在部分场景有限 |\n| Reproducibility | 4/5 | 附录提供了详尽的超参数、硬件配置、seed 验证、prompt 模板；承诺代码开源；但部分实验（DocRED beam search 仅 50 文档子集）的完整复现需要澄清 |\n| Confidence | 4/5 | 熟悉 constrained decoding 和 information extraction 领域，通读全文含 22 页附录 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Proposition 1 证明不严格，与论文的形式化定位不匹配\n- 具体位置：Section 3, §3.1, \"Proof sketch\"\n- 问题：论文的核心贡献之一是\"可判定性引导的约束分类\"（decidability-guided constraint classification），Proposition 1（Level 2 ⊄ Level 1）是支撑这一框架的关键理论结果。然而论文仅给出 \"proof sketch\"：构造了一个 relation r with dom(r) = {τ₁, τ₂} 和 n 个独立选类型的 entity，论证 head-type field 需要回读 τ_{e(i)}，因此 PDDA 是必要的。这个论证是直觉性的，缺少：(a) 到已知不可判定性/语言层次结果的形式化归约；(b) 对 \"independently unbound\" 的精确定义（实际中 schema 的 JSON 结构会限制 n 和 k 的范围）；(c) 完整的数学证明（至少应放在附录中）。\n- 为什么影响接收：如果论文将自身定位为\"第一个形式化编译 IE 本体约束\"的工作（Abstract: \"formally compiles\"），形式化结果的严格性是核心可信度的基础。一个仅有 proof sketch 的 proposition 无法支撑 \"formal\" 的声称。\n- 建议修改方向：(1) 在附录中提供完整的形式化证明，包括明确的语言定义、CFG 无法识别该语言的泵引理论证或闭包性质论证；(2) 或者降低形式化声称的力度，将 Proposition 1 明确标注为 conjecture/informal argument，并相应调整 abstract 和 introduction 的措辞。\n\n**N2** [critical] \"Exact enforcement\" 声称与 36.64% CF fallback rate 存在根本矛盾\n- 具体位置：Abstract (\"constraint tightness\"), §3.3 (\"exact pair-based enforcement\"), §4 (Constraint Composition), Appendix C Table 7-8\n- 问题：论文多处声称语义层实现了 \"exact\" 的 pair-based domain/range enforcement（§3.3）。但 Appendix C Table 8 显示 SciERC 上 GENERIC 类型的 conflicting-type pairs 占全部 CF violations 的 63.3%（155/245），grammar-first fallback 在 36.64% 的 type-bearing positions 被触发。当 fallback 触发时，语义约束被完全丢弃，退化为 grammar-only。这意味着约 1/3 的关键决策点上，系统实际并未执行语义约束。论文将此描述为\"a soft error detectable by downstream validation\"，但这与 \"exact enforcement\" 的声称矛盾。\n- 进一步的问题：fallback 是否会级联？一次 fallback 导致的错误类型赋值是否会影响后续 entity registry 的状态，从而触发更多 fallback？论文未分析级联失败（cascading failures）的可能性。\n- 为什么影响接收：如果核心技术声称（exact enforcement）在实践中有 1/3 的时间不成立，审稿人和读者会质疑方法的可靠性。这不是一个小的精度问题，而是核心 narrative 的准确性问题。\n- 建议修改方向：(1) 将 \"exact\" 修改为更精确的表述，如 \"best-effort pair-based enforcement with grammar-first fallback\"；(2) 分析 fallback 的级联行为；(3) 报告 fallback 后的 entity registry 状态一致性。\n\n**N3** [critical] WikiEvents fine-tuning 评估仅 20 文档测试集，统计效力严重不足\n- 具体位置：§5.4 (Extension to Event Extraction), Table 5, Limitations (page 9)\n- 问题：WikiEvents 的 fine-tuning 评估使用标准 194/20/20 split（Li et al., 2021），测试集仅 20 篇文档。在如此小的样本上：(a) bootstrap p-values 不可靠；(b) 单个异常文档可大幅影响指标；(c) 置信区间极宽。论文在 Limitations 中披露了这一问题（\"WikiEvents fine-tuning composability is preliminary (20-document test set)\"），但正文 §5.4 的结论语气并未相应降低。例如 Table 5 直接与 SciERC/DocRED 的结果并列呈现，暗示同等可信度。\n- 为什么影响接收：20-doc 测试集上的数字无法支撑 \"framework generalizes to event extraction\" 的声称（§5.4 标题为 \"Extension to Event Extraction\"）。即使零样本评估用了 246 文档（更好），fine-tuning 组合性的结论仍然不够可靠。\n- 建议修改方向：(1) 在 §5.4 正文中明确标注测试集规模限制，降低结论语气；(2) 报告 WikiEvents fine-tuning 结果的 95% bootstrap 置信区间；(3) 考虑使用完整 246 文档进行 cross-validation 或 leave-one-out 评估来增强统计效力。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 缺少与最相关并发工作的直接实验对比\n- 具体位置：§6 (Related Work), §5 (Experiments)\n- 问题：论文在 Related Work 中讨论了 BoostCD (Sakota et al., 2025)、CRANE (Banerjee et al., 2025)、IterGen (Ugare et al., 2025) 等同期工作，但实验中未与其直接对比。BoostCD 尤其相关——它也针对 IE 任务使用 constrained decoding，并在相同数据集（SciERC）上有结果。论文的 S1（grammar-only）配置隐式对标了 GCD (Geng et al., 2023)，但未明确展示 head-to-head 数字。\n- 为什么影响评分：缺乏直接对比使读者难以判断 OntoCoDec 相对于最新竞争方法的增量贡献。\n- 建议：至少在 SciERC 上与 BoostCD、GCD 进行直接数字对比（即使引用其论文报告的数字），并讨论评估设置差异。\n\n**W2** [warning] 跨模型验证局限于 7-8B 参数规模，泛化性声称不充分\n- 具体位置：§5 (Experiments), Limitations (page 9)\n- 问题：三个模型（Qwen3-8B, Llama-3.1-8B, Mistral-7B）均为 7-8B 参数量级。论文在 Limitations 中承认\"scaling to smaller models has not been verified\"，但正文的泛化性声称（如 Abstract: \"applies to any autoregressive LM\"）未加限定。更小的模型（1-3B）可能因能力不足导致更多 fallback；更大的模型（70B+）可能因基础能力更强而改变约束效果的模式。\n- 建议：(1) 在 Abstract/Introduction 中限定为 \"7-8B scale models\"；(2) 或增加至少一个不同规模的模型（如 Qwen3-1.8B 或 Llama-3.1-70B）的实验。\n\n**W3** [warning] 零样本 R-F1（0.08-8%）场景下 violation rate 分析的实际意义需要更明确的讨论\n- 具体位置：§5.1 Table 1, §5.2 Table 3, §5.3 Table 4\n- 问题：零样本设置下 R-F1 极低（SciERC 上 Qwen: 0.96%, Llama: ~0.08%），此时模型输出质量接近噪声水平。在这种条件下，violation rate（DR）的下降主要反映约束系统阻止了结构性错误，而非改善了抽取质量。论文将此定位为 \"diagnostic\"（§5 开头），这一定位是恰当的，但正文表格中零样本和微调结果并排呈现，读者可能误解零样本 DR 下降的实际价值。\n- 建议：在 §5.1 开头更明确地说明：零样本 ablation 的目的是隔离各层贡献的违规消除效果（而非抽取质量提升），R-F1 过低意味着该场景下的约束主要价值是结构合规而非 task performance。\n\n**W4** [warning] Entity registry 的顺序依赖可能导致 globally suboptimal type assignment\n- 具体位置：§3.3 (Entity Registry), §3.3 (Dynamic Masking)\n- 问题：Entity registry 在生成过程中动态构建，entity 类型赋值在生成时刻贪心确定。考虑以下场景：entity A 可被标注为类型 X 或 Y；如果贪心赋值为 X，后续某个 relation 需要类型 Y 的 head entity，导致 fallback 触发。如果赋值为 Y，则所有约束可满足。当前的贪心策略可能是局部最优但全局次优的。论文在 Appendix D 中通过 TCR（post-hoc type consistency resolution）部分解决了这个问题，但 TCR 是事后修复，不是生成时的 exact enforcement。\n- 建议：讨论 entity type assignment 的顺序依赖性和贪心策略的局限性，将其作为 Level 3（non-local）约束的一个实例。\n\n**W5** [warning] DocRED beam search 实验仅使用 50 文档子集\n- 具体位置：Appendix E, Table 15\n- 问题：SciERC 上 beam search 使用了完整 551 文档，但 DocRED 仅使用\"matched 50-document subsets\"。DocRED 文档更长（mean 198 tokens vs SciERC ~120 tokens）、关系类型更多（96 vs 7），beam search 在这类复杂文档上的表现可能与简单文档不同。50 文档子集可能不具代表性。\n- 建议：报告 50 文档的选择标准和代表性分析；或至少在全 998 文档的子样本上运行 beam search (k=2) 以验证趋势一致性。\n\n---\n\n## Questions to Authors\n\nQ1. Proposition 1 是否可以通过 pumping lemma for CFLs 或 Ogden's lemma 给出完整证明？当前的 proof sketch 中 \"n and k are independently unbound\" 的论证是否依赖于特定的 schema 结构？如果 schema 对 entity 数量设置上限（实际场景中常见），Proposition 1 是否仍然成立？\n\nQ2. Grammar-first fallback 的级联行为：当一次 fallback 导致 entity 被赋予非预期类型时，该 entity 会被注册到 entity registry 中。后续引用该 entity 的 relation 是否会因此触发更多 fallback？是否有实验数据量化这种级联效应？\n\nQ3. Table 1 中 S2（two-pass）的 DR 反而高于 Full S1——这是否说明 two-pass 架构引入了额外的错误来源（如第一阶段 entity extraction 的错误传播到第二阶段）？\n\nQ4. LoRA fine-tuning 使用统一超参数（r=16, α=32）对三个不同模型，是否做过超参数敏感性分析？特别是 Mistral-7B 在多个指标上表现弱于 Qwen 和 Llama——这是模型能力差异还是超参数不匹配？\n\nQ5. Constraint tightness κ（§4, Table 19 footnote area）的计算中，对称关系的处理方式是什么？论文 footnote 1 提到\"for symmetric relations, σ(r) counts ordered pairs; the denominator 2τ² remains appropriate since we evaluate on directed triples\"——这是否意味着对称关系的实际约束比 κ 值显示的更紧？\n\n---\n\n## Missing References / 比较\n\n1. **BoostCD (Sakota et al., 2025)**: 已引用但未实验对比。作为同样在 SciERC 上做 IE constrained decoding 的工作，缺乏直接数字对比是显著遗漏。\n2. **GCD (Geng et al., 2023)**: 已引用，S1 配置隐式对标，但应在实验部分明确展示 GCD 的数字作为 baseline。\n3. 可考虑引用 **Schema-RL (Lu et al., 2025)** 在正文中（目前仅在 bib 中未被引用），作为 training-based structured output 的对比方法。\n\n引用审计结果：\n- 10 条 orphan bib entries（在 .bib 中但未被引用）：包括 delafuente2025guidex, geng2025jsonschemabench, lee2026formattax 等，均为与已引用条目的重复版本。\n- 1 条重复 bib key: schall2025hiddencost 出现两次。\n- 3 条 online not found: regino2025kgcurator, formattax2026, lee2026formattax（后两者为同一论文的重复条目，arXiv 2604.03616 可能尚未被 OpenAlex 索引）。\n- 这些都是 minor cleanup 问题，不影响审稿判断。\n\n---\n\n## 小问题（不影响接收）\n\n- §4 Eq.(2)：M_final = M_grammar(t) ∧ M_semantic(t) 的 conjunction 是逐位 AND——应明确说明这是 token-level 的逐位操作而非 set intersection 的简写，避免歧义。\n- Table 1-3 中 \"CF\" 列的含义（context-free violation 即 cross-field violation）在首次出现时未充分解释，需要回读 §3 才能理解。建议在表格 caption 或首次引用处加注。\n- Figure 1（page 20）的 scatter plot：x 轴 label \"κ · RV_baseline\" 的物理含义不直观，建议在 caption 中补充解释。\n- Appendix G 报告 \"completion-only loss for 3 epochs\"——对于 DocRED（3,053 examples / 998 dev）仅 3 epochs 是否充分？是否观察到 loss 收敛？\n- Page 8, §6 Related Work 最后一段提到 \"the decidability taxonomy and a κ-diagnostic yield a principled deployment workflow\"——这读起来更像 contribution 声称而非 related work 讨论，建议调整位置。\n\n---\n\n## 主要优势\n\n1. **新颖的形式化视角**：将 formal language theory 的可判定性分析引入 IE 约束解码，提出 context-free / prefix-decidable with state / non-local 的三层分类。这在 constrained decoding for NLP 领域是新颖的，为系统设计提供了有原则的指导。\n\n2. **全面的实验设计**：五路消融清晰隔离了 grammar 层和 semantic 层的贡献；跨模型（3 个）、跨数据集（3 个）、跨任务（RE + EE）的覆盖在 systems paper 中高于平均水平。\n\n3. **诚实的局限性讨论**：论文对 WikiEvents 样本量、模型规模限制、CF trade-off 等问题的披露异常坦诚，这在投稿论文中值得肯定。\n\n4. **实际工程价值**：框架自动从任意 IE 本体编译约束，无需约束特定训练，可与任意自回归 LM 配合——这使其具有即插即用的实际部署价值。LoRA fine-tuning 组合性实验表明约束不干扰微调效果。\n\n5. **丰富的附录**：22 页附录包含详尽的错误分析（Appendix J case studies）、scalability benchmarks（Appendix K）、prompt 敏感性（Appendix I）、document length 分析（Appendix H）、TCR 机制（Appendix D/Tables 30-31）。这些内容显著增强了论文的可复现性和可信度。\n\n6. **Constraint tightness κ 指标**：作为部署指导工具（§4 末尾、Appendix C），κ 与 DR reduction 的相关性（Figure 2, r=0.886）为实践者提供了预测约束效果的依据——这是有实用价值的贡献。\n\n---\n\n## Overall Assessment\n\n**评分：3.5 — Borderline Conference**\n\n本文提出了一个有新意的框架，将形式语言理论的可判定性分析引入 IE 约束解码，实验覆盖面广且附录详尽。主要顾虑是：(1) 核心形式化结果（Proposition 1）仅为 proof sketch，与论文的 \"formally compiles\" 定位不匹配；(2) \"exact enforcement\" 的核心声称被 36.64% CF fallback rate 实质性削弱；(3) WikiEvents fine-tuning 评估的统计效力不足。如果作者能在修改中加强证明严格性、校准技术声称的精确度、并补充 WikiEvents 的统计分析，本文有潜力成为 solid conference paper。当前状态下，建议 Borderline Conference / strong Findings。\n\n**Confidence: 4/5** — 熟悉 constrained decoding 和 information extraction 领域，通读全文含全部 22 页附录及引用验证。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-20T17:19:26.594711+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 788 · 2026-05-20T17:19:34.571616+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 789 · 2026-05-20T17:19:34.622284+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-20T17:19:40.806294+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-20T17:19:40.806654+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 792 · 2026-05-20T17:19:49.709439+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference），Soundness 3.5/5，Excitement 3.5/5，Confidence 4/5。

三个 Must-Fix 问题：
1. Proposition 1 仅为 proof sketch，与 "formally compiles" 定位不匹配
2. "Exact enforcement" 声称与 36.64% CF fallback rate 矛盾
3. WikiEvents fine-tuning 仅 20 文档测试集，统计效力不足

五个 Should-Fix 问题涉及：缺少与 BoostCD/CRANE 的直接对比、跨模型验证局限于 7-8B 规模、零样本 R-F1 过低时 violation 分析的意义、entity registry 顺序依赖、DocRED beam search 仅 50 文档子集。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 21

## Round 21

4 recorded events


### User

_source line 793 · 2026-05-20T17:20:21.126920+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Minor 问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（新颖性 + 完整性 + 写作质量）

**Overall: 3.5 Borderline Conference | Soundness 4/5 | Excitement 3/5 | Reproducibility 4/5 | Confidence 4/5**

### Must-Fix

**N1** [critical] 语义层核心机制（entity registry + dynamic masking）与 IterGen 的概念区分不充分
- §6 Related Work（p8）, Appendix B（p13-17）
- IterGen（Ugare et al., 2025, ICLR 2025）同样在 grammar 层之上叠加语义约束，在生成过程中检测违规并通过 backtracking 修正。OntoCoDec 的 dynamic masking 与 IterGen 的 semantic check + backtracking 是解决同一类问题（grammar-valid 但 semantically-invalid 输出）的两种机制。论文在 §6 和 Appendix B 中仅将 IterGen 列为相关工作之一，未深入对比两者在机制设计（preventive masking vs. corrective backtracking）、效率特性（OntoCoDec 无需回退 vs. IterGen 需要 KV cache 管理）、和约束表达能力（OntoCoDec 限于 domain/range vs. IterGen 支持任意 semantic predicate）上的差异。类似地，PICARD（Scholak et al., 2021）的 incremental parsing monitor 与 OntoCoDec 的 runtime entity registry 在概念上高度相似。
- 建议：§6 增加显式机制对比表（OntoCoDec vs. IterGen vs. PICARD）。

**N2** [critical] κ̄ 作为 Contribution 2（"analytical linking framework"）被过度声称
- Abstract（p1）, §1 Contributions 列表 item 2（p2）, §4（p4-5）
- κ̄ 本质上是描述性统计量（|S(r)|/|E|² 的归一化比例），论文自身在 Appendix C 承认 "descriptive characterization rather than a confirmatory statistical test"（df=2, p>0.05）。但 Abstract 和 Contribution 列表仍将其定位为 "analytical linking framework"。
- 建议：降级为 "descriptive metric that correlates with enforcement outcomes"。

### Should-Fix

**W1** [warning] 无直接实验对比最接近的 IE 基线 BoostCD
- BoostCD（Sakota et al., 2025）同样将 constrained decoding 应用于 IE，使用了 SciERC 和 DocRED。

**W2** [warning] "Ontology-agnostic" 声称的实验支撑不充分
- 仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 来自训练数据经验统计。

**W3** [warning] 正文 Related Work（§6）过于压缩（约 15 行），实质讨论全部推迟到附录

**W4** [warning] Abstract 信息密度过高，关键 message 被数字淹没

**W5** [warning] 模型规模限于 7-8B，正文泛化性声称未充分 hedge

**W6** [warning] CF 代价在 Abstract/Contribution 中不够透明

### Minor
- M1: .bib 文件中有 10 个 orphan entries
- M2: schall2025hiddencost bib key 重复
- M3: S1/S2 命名与层级编号初读易混淆
- M4: Table 5 "—" 标记缺少表注
- M5: Beam search seed 信息不完整

### Questions
Q1: 是否考虑将 OntoCoDec 扩展到更一般的语义约束（cardinality, temporal ordering）？
Q2: Per-relation DR 在 COMPARE 关系上（κ=0.528）未完全消除，why？
Q3: Fine-tuning 后 R-F1 仅提升 0.5pp 但 DR 大幅下降——被消除的 DR violations 对 F1 影响微乎其微？
Q4: S1 模式下第一个 triple 的 domain/range 如何处理（registry 为空时）？

### Missing References
1. Koldehoff et al. (Frontiers in AI, 2025) — grammar-constrained decoding + 本体约束应用于临床试验 IE
2. Schema RL (Lu et al., ACL 2025) — 存在于 bib 但未被引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-20T17:22:05.047073+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with nuance] R2-N1: 语义层机制与 IterGen 的概念区分不充分**\n\n同意论文应更深入对比 OntoCoDec vs. IterGen vs. PICARD 的机制差异。但我认为 R2 略低估了这三者之间的架构差异程度：\n\n- **OntoCoDec (preventive masking)**：在每个 decoding step 预计算合法 token 集合，从源头阻止无效 token 生成——零回退开销，但约束表达力受限于 prefix-decidable 性质（仅 domain/range）。\n- **IterGen (corrective backtracking)**：允许生成后检测违规并回退到 checkpoint——支持任意 semantic predicate，但需要 KV cache 管理和回退开销（Ugare et al., 2025 报告 backtracking 增加 15-40% latency）。\n- **PICARD (incremental parsing monitor)**：在 text-to-SQL 场景中做 incremental validity check，丢弃无效 beam candidates——介于两者之间，但绑定于 SQL grammar，不处理本体约束。\n\n论文确实应在 §6 或 Appendix B 中增加一个显式的机制对比表，清晰呈现 preventive vs. corrective 的 trade-off（约束表达力 vs. 效率开销）。但我不认为这上升到 \"critical\" 级别——核心机制差异（masking vs. backtracking）在领域内是公认的不同设计范式，不存在 novelty 混淆的风险。建议降级为 Should-Fix。\n\n**[AGREE] R2-N2: κ̄ 作为 Contribution 2 被过度声称**\n\n完全同意。论文在 Appendix C 自身承认 κ̄ 的 Kruskal-Wallis 检验 df=2、p>0.05，未通过确认性统计检验。在此前提下，将 κ̄ 定位为 \"analytical linking framework\"（Abstract）并列为独立贡献（Contribution 2）确实属于过度声称。\n\n我在自己的审稿中也注意到了这一点：κ 与 DR reduction 的 Pearson 相关 r=0.886（Figure 2/Appendix C）是有价值的描述性发现，但不能上升为 \"analytical framework\"。R2 的建议——降级为 \"descriptive metric that correlates with enforcement outcomes\"——是准确的修改方向。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 无直接实验对比 BoostCD**\n\n与我自己的 W1 一致。BoostCD (Sakota et al., 2025) 在 SciERC 上做了 grammar-constrained IE，是最直接的竞争方法。缺乏 head-to-head 数字对比是两位 reviewer 共同识别的问题。\n\n**[AGREE with nuance] R2-W2: \"Ontology-agnostic\" 声称实验支撑不充分**\n\nR2 指出仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 的 schema 来自经验统计。这个观察是准确的。但我认为需要区分两个层面：\n1. **编译机制的 agnosticism**：OntoCoDec 的编译流程（schema → grammar + semantic masks）确实不依赖本体来源——无论 schema 来自 KAIROS ontology 还是训练集统计，编译过程相同。这一点有充分支撑。\n2. **\"Ontology\" 一词的准确性**：SciERC/DocRED 的 schema 本质上是 type inventory + domain/range mapping，不是完整的本体（无 subsumption hierarchy、无 axioms）。论文标题用 \"Schema Constraints\" 而非 \"Ontology Constraints\" 是恰当的，但正文中 \"ontology-agnostic\" 的表述确实应改为 \"schema-agnostic\"。\n\n**[REBUT] R2-W3: 正文 Related Work 过于压缩**\n\n不完全同意。对于 long paper（8 页正文），将核心对比放在 §6 约 15 行、详细讨论放在 Appendix B 4 页是合理的空间分配策略。§6 正文覆盖了三个关键维度（grammar-constrained decoding、schema-guided IE、ontology-constrained generation），并引用了 20+ 篇文献。关键定位信息（与 GCD、PICARD、GoLLIE 等的区分）在正文中可获取。\n\n但我同意 R2 的 N1——§6 中对 IterGen 的讨论不够深入。建议在正文 §6 中增加与 IterGen 的显式机制对比（2-3 行即可），而不需要将整个 Appendix B 搬入正文。\n\n**[AGREE] R2-W4: Abstract 信息密度过高**\n\n同意。Abstract 试图在一段中塞入可判定性分类、三层架构、κ 指标、跨模型/跨数据集数字、beam search 结果、fine-tuning composability，关键 message 被淹没。建议 Abstract 聚焦于核心 message（可判定性引导的约束分层 + grammar-first fallback）和最重要的 1-2 个数字（如 DR reduction 幅度），将细节推到 Introduction。\n\n**[AGREE] R2-W5: 模型规模 hedging 不充分**\n\n与我自己的 W2 一致。\n\n**[AGREE] R2-W6: CF 代价在 Abstract/Contribution 中不够透明**\n\n与我自己的 N2 一致且互补。R2 的 W6 从写作透明度角度提出，我的 N2 从技术声称准确性角度提出。两者共同指向一个问题：论文在最显眼的位置（Abstract、Contributions）对 CF trade-off 的呈现不充分。Grammar-first fallback rate 36.64%（SciERC）这个数字应在 Abstract 或 §1 Contributions 中被提及，而非仅出现在 Appendix C Table 8。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1**: 10 orphan bib entries，与我的观察一致。\n\n**[AGREE] R2-M2**: 重复 bib key，与我的观察一致。\n\n**[AGREE] R2-M3**: S1/S2 命名确实初读易混淆。S1 = single-pass (grammar+semantic), S2 = two-pass sequential——但 \"S1\" 容易被读为 \"Stage 1\" 或 \"Semantic layer 1\"。建议改为更具描述性的缩写（如 JOINT vs. SEQ）。\n\n**[AGREE] R2-M4**: Table 5 \"—\" 标记确实缺少表注说明。\n\n**[REBUT] R2-M5**: Beam search seed 信息。论文 Appendix G 明确报告了 seed 验证：\"We verify this with three seeds (42, 123, 456) across two LoRA fine-tuned models on all 551 SciERC documents\"，并指出 \"Argmax is deterministic; the random seed controls torch.cuda.manual_seed for sampling and dropout, neither of which is active during greedy inference\"。Beam search (k>1) 同样是确定性的（给定相同模型状态），不依赖随机 seed。这一点在 Appendix G 中已充分说明。\n\n---\n\n### Questions 评论\n\n**R2-Q1**（扩展到 cardinality/temporal ordering）：好问题，直接关联 Level 3 non-local 约束的未来方向。这也呼应了我在 W4 中关于 entity registry 顺序依赖的讨论——cardinality constraints（\"至少 N 个某类 entity\"）和 temporal ordering 本质上都是 non-local 的，论文的框架目前无法在解码时精确处理。\n\n**R2-Q2**（COMPARE 关系 κ=0.528 未完全消除 DR）：有价值的 diagnostic 问题。结合 Appendix N Table 35 的 case study，COMPARE 关系的 domain/range 允许多种 entity type pair，κ 值中等偏高意味着约束不够紧，部分 valid-by-schema-but-wrong-in-context 的 pair 无法被 Level 2 约束过滤。这实际上是 κ 指标的一个良好验证——它预测了约束效果的边界。\n\n**R2-Q3**（DR 下降但 F1 仅提升 0.5pp）：非常敏锐的观察。这暗示被消除的 violations 大多出现在已经错误的输出中（即模型提取了错误的 triple，约束修正了其类型但 triple 本身仍是错的）。这进一步支持了我的 W3——零样本/低 F1 场景下 violation rate 分析的实际价值有限。\n\n**R2-Q4**（S1 模式下 registry 为空时的处理）：这涉及 §3.3 的 entity registry 初始化逻辑。在 OntoCoDec 的 schema 中，entities 在 relations 之前生成（top-level ordering），因此 registry 在 relation generation 开始前已被填充。但如果模型在第一个 entity 生成时 registry 为空，语义层应退化为 grammar-only（所有 entity types 均合法）。论文应在 §3.3 中显式说明这一边界条件。\n\n---\n\n### Missing References 评论\n\n**[AGREE] Koldehoff et al. (Frontiers in AI, 2025)**：如果该工作确实将 grammar-constrained decoding + 本体约束应用于临床试验 IE，与 OntoCoDec 的方法论相关性很高，应在 §6 或 Appendix B 中讨论。\n\n**[AGREE] Schema RL (Lu et al., ACL 2025)**：在 bib 中存在（lu2025schemarl）但未被引用。作为 training-based structured output 方法，可作为 §6 中 training-based vs. decoding-time 对比的参照点。",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE with nuance] R2-N1: 语义层机制与 IterGen 的概念区分不充分**\n\n同意论文应更深入对比 OntoCoDec vs. IterGen vs. PICARD 的机制差异。但我认为 R2 略低估了这三者之间的架构差异程度：\n\n- **OntoCoDec (preventive masking)**：在每个 decoding step 预计算合法 token 集合，从源头阻止无效 token 生成——零回退开销，但约束表达力受限于 prefix-decidable 性质（仅 domain/range）。\n- **IterGen (corrective backtracking)**：允许生成后检测违规并回退到 checkpoint——支持任意 semantic predicate，但需要 KV cache 管理和回退开销（Ugare et al., 2025 报告 backtracking 增加 15-40% latency）。\n- **PICARD (incremental parsing monitor)**：在 text-to-SQL 场景中做 incremental validity check，丢弃无效 beam candidates——介于两者之间，但绑定于 SQL grammar，不处理本体约束。\n\n论文确实应在 §6 或 Appendix B 中增加一个显式的机制对比表，清晰呈现 preventive vs. corrective 的 trade-off（约束表达力 vs. 效率开销）。但我不认为这上升到 \"critical\" 级别——核心机制差异（masking vs. backtracking）在领域内是公认的不同设计范式，不存在 novelty 混淆的风险。建议降级为 Should-Fix。\n\n**[AGREE] R2-N2: κ̄ 作为 Contribution 2 被过度声称**\n\n完全同意。论文在 Appendix C 自身承认 κ̄ 的 Kruskal-Wallis 检验 df=2、p>0.05，未通过确认性统计检验。在此前提下，将 κ̄ 定位为 \"analytical linking framework\"（Abstract）并列为独立贡献（Contribution 2）确实属于过度声称。\n\n我在自己的审稿中也注意到了这一点：κ 与 DR reduction 的 Pearson 相关 r=0.886（Figure 2/Appendix C）是有价值的描述性发现，但不能上升为 \"analytical framework\"。R2 的建议——降级为 \"descriptive metric that correlates with enforcement outcomes\"——是准确的修改方向。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: 无直接实验对比 BoostCD**\n\n与我自己的 W1 一致。BoostCD (Sakota et al., 2025) 在 SciERC 上做了 grammar-constrained IE，是最直接的竞争方法。缺乏 head-to-head 数字对比是两位 reviewer 共同识别的问题。\n\n**[AGREE with nuance] R2-W2: \"Ontology-agnostic\" 声称实验支撑不充分**\n\nR2 指出仅 WikiEvents 使用正式本体（KAIROS），SciERC/DocRED 的 schema 来自经验统计。这个观察是准确的。但我认为需要区分两个层面：\n1. **编译机制的 agnosticism**：OntoCoDec 的编译流程（schema → grammar + semantic masks）确实不依赖本体来源——无论 schema 来自 KAIROS ontology 还是训练集统计，编译过程相同。这一点有充分支撑。\n2. **\"Ontology\" 一词的准确性**：SciERC/DocRED 的 schema 本质上是 type inventory + domain/range mapping，不是完整的本体（无 subsumption hierarchy、无 axioms）。论文标题用 \"Schema Constraints\" 而非 \"Ontology Constraints\" 是恰当的，但正文中 \"ontology-agnostic\" 的表述确实应改为 \"schema-agnostic\"。\n\n**[REBUT] R2-W3: 正文 Related Work 过于压缩**\n\n不完全同意。对于 long paper（8 页正文），将核心对比放在 §6 约 15 行、详细讨论放在 Appendix B 4 页是合理的空间分配策略。§6 正文覆盖了三个关键维度（grammar-constrained decoding、schema-guided IE、ontology-constrained generation），并引用了 20+ 篇文献。关键定位信息（与 GCD、PICARD、GoLLIE 等的区分）在正文中可获取。\n\n但我同意 R2 的 N1——§6 中对 IterGen 的讨论不够深入。建议在正文 §6 中增加与 IterGen 的显式机制对比（2-3 行即可），而不需要将整个 Appendix B 搬入正文。\n\n**[AGREE] R2-W4: Abstract 信息密度过高**\n\n同意。Abstract 试图在一段中塞入可判定性分类、三层架构、κ 指标、跨模型/跨数据集数字、beam search 结果、fine-tuning composability，关键 message 被淹没。建议 Abstract 聚焦于核心 message（可判定性引导的约束分层 + grammar-first fallback）和最重要的 1-2 个数字（如 DR reduction 幅度），将细节推到 Introduction。\n\n**[AGREE] R2-W5: 模型规模 hedging 不充分**\n\n与我自己的 W2 一致。\n\n**[AGREE] R2-W6: CF 代价在 Abstract/Contribution 中不够透明**\n\n与我自己的 N2 一致且互补。R2 的 W6 从写作透明度角度提出，我的 N2 从技术声称准确性角度提出。两者共同指向一个问题：论文在最显眼的位置（Abstract、Contributions）对 CF trade-off 的呈现不充分。Grammar-first fallback rate 36.64%（SciERC）这个数字应在 Abstract 或 §1 Contributions 中被提及，而非仅出现在 Appendix C Table 8。\n\n---\n\n### Minor\n\n**[AGREE] R2-M1**: 10 orphan bib entries，与我的观察一致。\n\n**[AGREE] R2-M2**: 重复 bib key，与我的观察一致。\n\n**[AGREE] R2-M3**: S1/S2 命名确实初读易混淆。S1 = single-pass (grammar+semantic), S2 = two-pass sequential——但 \"S1\" 容易被读为 \"Stage 1\" 或 \"Semantic layer 1\"。建议改为更具描述性的缩写（如 JOINT vs. SEQ）。\n\n**[AGREE] R2-M4**: Table 5 \"—\" 标记确实缺少表注说明。\n\n**[REBUT] R2-M5**: Beam search seed 信息。论文 Appendix G 明确报告了 seed 验证：\"We verify this with three seeds (42, 123, 456) across two LoRA fine-tuned models on all 551 SciERC documents\"，并指出 \"Argmax is deterministic; the random seed controls torch.cuda.manual_seed for sampling and dropout, neither of which is active during greedy inference\"。Beam search (k>1) 同样是确定性的（给定相同模型状态），不依赖随机 seed。这一点在 Appendix G 中已充分说明。\n\n---\n\n### Questions 评论\n\n**R2-Q1**（扩展到 cardinality/temporal ordering）：好问题，直接关联 Level 3 non-local 约束的未来方向。这也呼应了我在 W4 中关于 entity registry 顺序依赖的讨论——cardinality constraints（\"至少 N 个某类 entity\"）和 temporal ordering 本质上都是 non-local 的，论文的框架目前无法在解码时精确处理。\n\n**R2-Q2**（COMPARE 关系 κ=0.528 未完全消除 DR）：有价值的 diagnostic 问题。结合 Appendix N Table 35 的 case study，COMPARE 关系的 domain/range 允许多种 entity type pair，κ 值中等偏高意味着约束不够紧，部分 valid-by-schema-but-wrong-in-context 的 pair 无法被 Level 2 约束过滤。这实际上是 κ 指标的一个良好验证——它预测了约束效果的边界。\n\n**R2-Q3**（DR 下降但 F1 仅提升 0.5pp）：非常敏锐的观察。这暗示被消除的 violations 大多出现在已经错误的输出中（即模型提取了错误的 triple，约束修正了其类型但 triple 本身仍是错的）。这进一步支持了我的 W3——零样本/低 F1 场景下 violation rate 分析的实际价值有限。\n\n**R2-Q4**（S1 模式下 registry 为空时的处理）：这涉及 §3.3 的 entity registry 初始化逻辑。在 OntoCoDec 的 schema 中，entities 在 relations 之前生成（top-level ordering），因此 registry 在 relation generation 开始前已被填充。但如果模型在第一个 entity 生成时 registry 为空，语义层应退化为 grammar-only（所有 entity types 均合法）。论文应在 §3.3 中显式说明这一边界条件。\n\n---\n\n### Missing References 评论\n\n**[AGREE] Koldehoff et al. (Frontiers in AI, 2025)**：如果该工作确实将 grammar-constrained decoding + 本体约束应用于临床试验 IE，与 OntoCoDec 的方法论相关性很高，应在 §6 或 Appendix B 中讨论。\n\n**[AGREE] Schema RL (Lu et al., ACL 2025)**：在 bib 中存在（lu2025schemarl）但未被引用。作为 training-based structured output 方法，可作为 §6 中 training-based vs. decoding-time 对比的参照点。",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 795 · 2026-05-20T17:22:08.772513+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3725
}
```

</details>

---


### Assistant

_source line 796 · 2026-05-20T17:22:18.863035+00:00_

交叉回应已提交。总结：

- **R2 的 2 个 Must-Fix**：N1（IterGen 区分）我同意需加强但建议降级为 Should-Fix（preventive vs. corrective 是公认不同范式）；N2（κ̄ 过度声称）完全同意。
- **R2 的 6 个 Should-Fix**：W1/W4/W5/W6 均同意，与我自己的发现一致或互补；W2 部分同意（编译机制确实 agnostic，但"ontology"用词不准确）；W3 反驳（RW 空间分配合理，但 IterGen 讨论需加深）。
- **5 个 Minor**：M1-M4 同意，M5 反驳（beam search 是确定性的，seed 信息已在 Appendix G 充分说明）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 22

## Round 22

88 recorded events


### User

_source line 797 · 2026-05-20T18:36:51.267002+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。

## 论文信息
- 标题: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf`
- 目标 venue: EMNLP 2026（via ARR May cycle）
- Deadline: 2026-05-25

## Venue 要求
- 长文正文 ≤ 8 页，参考文献无限制
- Limitations 必须有，不计入页数
- ACL 模板，double-blind 审稿
- 附录不要求审稿人审查

## 你的审查侧重

### A. 形式化声称与证明
1. Proposition 1 声称 Level 2 约束非 context-free——proof sketch 是否充分？附录 pumping lemma 完整证明是否严密？
2. "best-effort pair-based enforcement" 的精确含义——是否有遗漏的 corner case？
3. 三级 decidability taxonomy 是否 well-motivated？分类边界是否清晰？
4. 论文声称 "formally compiles"——实际实现是否匹配这一措辞？
5. grammar-first fallback 是否有严格的正确性保证？级联失败分析是否充分？

### B. 实验设计与统计严谨性
1. 五路消融实验设计是否充分隔离各层贡献？
2. CF trade-off：论文声称 CF 是 "resolvable via beam search"——证据是否充分（特别是 DocRED）？
3. 统计显著性：bootstrap 检验设置是否合理？样本量是否足够？
4. WikiEvents EE fine-tuning 仅 20 文档测试集——统计效力如何？
5. DocRED beam search 零样本仅 50 文档子集——是否影响结论可靠性？
6. 70B 评估仅为 "preliminary"——声称范围是否合理？
7. Constraint tightness κ̄ 作为 "descriptive metric"——是否有足够的预测性证据支持其 deployment guidance 价值？

### C. 实验公平性
1. Baseline 选择是否充分？是否遗漏了最接近的 IE constrained decoding 基线（如 BoostCD、IterGen）？
2. 与 GoLLIE 等 schema-aware IE 系统的对比是否公平？
3. Post-hoc filtering 对比是否公平？

### D. 输出格式
请按以下结构输出审稿意见：
1. **Summary** (2-3 句)
2. **Strengths** (逐条 S1, S2, ...)
3. **Weaknesses** (逐条 W1, W2, ... 区分 Must-Fix / Should-Fix / Minor)
4. **Questions** (需要作者澄清的)
5. **Missing References**
6. **Scores**: Soundness (1-5), Excitement (1-5), Overall (1-5, 按 EMNLP 2026 ARR 评分标准: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit), Confidence (1-5)

严格评审，不留情面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-20T18:37:00.631590+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 799 · 2026-05-20T18:37:01.991887+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_1_11179fb2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1360
}
```

</details>

---


### Tool call

_source line 800 · 2026-05-20T18:37:02.042609+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 801 · 2026-05-20T18:37:02.095912+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 802 · 2026-05-20T18:37:08.275898+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-20T18:37:11.149303+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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


### Tool call

_source line 804 · 2026-05-20T18:37:11.601367+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 805 · 2026-05-20T18:37:16.124979+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Assessment Criteria

The Overall assessment score is an explicit recommendation for the outcome of this paper, if it were committed to an *ACL venue. This is a composite 
…[truncated 1178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7849
}
```

</details>

---


### Tool result

_source line 806 · 2026-05-20T18:37:17.481793+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.8}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 525.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.5}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 539.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png\", \"w
…[truncated 519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6332
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-20T18:38:05.128656+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 57, \"total_citations\": 94, \"unique_cited_keys\": 56, \"orphan_bib\": 1, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 47, \"online_not_found\": 2, \"online_mismatch\": 8}, \"cross_check\": {\"orphan_bib\": [\"schmidt2025grammar\"], \"missing_bib\": [], \"orphan_count\": 1, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"synchromesh_iclr2022\", \"type\": \"inproceedings\", \"title\": \"Synchromesh: Reliable Code Generation from Pre-trained Language Models\", \"authors\": \"Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares,...\", \"year\": \"2022\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"mgd_neurips2023\", \"type\": \"inproceedings\", \"title\": \"Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context\", \"authors\": \"Agrawal, Lakshya A. and Kanade, Aditya and Goyal, Navin and Lahiri, Shuvendu K. ...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"pldi2025_type_constrained_codegen\", \"type\": \"article\", \"title\": \"Type-Constrained Code Generation with Language Models\", \"authors\": \"M\\\\\\\"undler, Niels and He, Jingxuan and Wang, Hao and Sen, Koushik and Song, Dawn ...\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM on Programming Languages\"}, {\"key\": \"roth_yih_2004\", \"type\": \"inproceedings\", \"title\": \"A Linear Programming Formulation for Global Inference in Natural Language Tasks\", \"authors\": \"Roth, Dan and Yih, Wen-tau\", \"year\": \"2004\", \"venue\": \"Proceedings of the Eighth Conference on Computational Natural Language Learning ...\"}, {\"key\": \"adakgc_emnlp2023\", \"type\": \"inproceedings\", \"title\": \"Schema-adaptable Knowledge Graph Construction\", \"authors\": \"Ye, Hongbin and Gui, Honghao and Xu, Xin and Chen, Xi and Chen, Huajun and Zhang...\", \"year\": \"2023\
…[truncated 47786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 53527
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-20T18:38:17.135399+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions for each score level. Focus on: Soundness, Excitement/Novelty, Overall Assessment, Confidence, Reproducibility, and any other dimensions. List the exact score descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions for each score level. Focus on: Soundness, Excitement/Novelty, Overall Assessment, Confidence, Reproducibility, and any other dimensions. List the exact score descriptions."
  }
}
```

</details>

---


### Tool call

_source line 809 · 2026-05-20T18:38:19.445524+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 810 · 2026-05-20T18:38:20.401489+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 811 · 2026-05-20T18:38:20.402005+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 812 · 2026-05-20T18:38:21.007863+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 813 · 2026-05-20T18:38:21.359387+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 814 · 2026-05-20T18:38:21.867799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1465
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-20T18:38:23.293416+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2285
}
```

</details>

---


### Tool result

_source line 816 · 2026-05-20T18:38:23.698153+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2338
}
```

</details>

---


### Tool result

_source line 817 · 2026-05-20T18:38:25.820984+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure. I tried to check the important points carefully"
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## Soundness
**Scale: 1-5 (with half-point increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale: 1-5 (with half-point increments)**
- 5: "Highly Exciting: I would recommend this paper to others and/or attend"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper to others"
- 2: "Potentially Interesting: does not resonate with me, but might with others"
- 1: "Not Exciting: does not resonate with me, and I don't think it would"

## Overall Assessment
**Scale: 1-5 (with half-point increments)**
- 5: "Consider for Award: top 2.5% papers"
- 4: "Conference: could be accepted to an ACL conference"
- 3: "Findings: could be accepted to the Findings of the ACL"
- 2: "Resubmit next cycle: needs substantial revisions"
- 1: "Do not resubmit: has to be fully redone"

## Reproducibility
**Scale: 1-5**
- 5: "They could easily reproduce the results"
- 4: "They could mostly reproduce the results"
- 3: "They could reproduce the results with some difficulty"
- 2: "They would be hard pressed to reproduce the results"
- 1: "They would not be able to reproduce the results"

## Datasets & Software Value
**Scale: 1-5** (identical scales)
- 5: 
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8685
}
```

</details>

---


### Tool call

_source line 818 · 2026-05-20T18:38:33.259539+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 819 · 2026-05-20T18:38:33.864031+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 820 · 2026-05-20T18:38:34.770736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1511
}
```

</details>

---


### Tool result

_source line 821 · 2026-05-20T18:38:34.774100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 822 · 2026-05-20T18:38:34.774561+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-20T18:38:35.378208+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-20T18:38:35.781545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 825 · 2026-05-20T18:38:35.882530+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-20T18:38:36.185234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-20T18:38:36.186421+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-20T18:38:36.188984+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 829 · 2026-05-20T18:38:36.792253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 830 · 2026-05-20T18:38:57.459891+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 831 · 2026-05-20T18:38:58.664801+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 429.4}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 549.7}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 605.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 609.9}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 552.5}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 369.8}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1204
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-20T18:39:05.799243+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 833 · 2026-05-20T18:39:06.402163+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 834 · 2026-05-20T18:39:07.261491+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1462
}
```

</details>

---


### Tool call

_source line 835 · 2026-05-20T18:39:07.261997+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 836 · 2026-05-20T18:39:07.664802+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1262
}
```

</details>

---


### Tool call

_source line 837 · 2026-05-20T18:39:07.665251+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 838 · 2026-05-20T18:39:08.167994+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-20T18:39:08.168441+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 840 · 2026-05-20T18:39:08.723380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1058
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-20T18:39:08.723846+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-20T18:39:09.279690+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool result

_source line 843 · 2026-05-20T18:39:09.383196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 659
}
```

</details>

---


### Tool call

_source line 844 · 2026-05-20T18:39:17.971730+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "17-26",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "17-26",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 845 · 2026-05-20T18:39:19.179563+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.6}, {\"page\": 18, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 555.5}, {\"page\": 19, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.6}, {\"page\": 20, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.8}, {\"page\": 21, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.1}, {\"page\": 22, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 514.4}, {\"page\": 23, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 516.2}, {\"page\": 24, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 506.3}, {\"page\": 25, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/m
…[truncated 538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool call

_source line 846 · 2026-05-20T18:39:28.887841+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p17.png"
  }
}
```

</details>

---


### Tool call

_source line 847 · 2026-05-20T18:39:29.189870+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p18.png"
  }
}
```

</details>

---


### Tool result

_source line 848 · 2026-05-20T18:39:30.095155+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool result

_source line 849 · 2026-05-20T18:39:30.097736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 850 · 2026-05-20T18:39:30.098228+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p19.png"
  }
}
```

</details>

---


### Tool call

_source line 851 · 2026-05-20T18:39:30.601870+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p20.png"
  }
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-20T18:39:31.305779+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1207
}
```

</details>

---


### Tool call

_source line 853 · 2026-05-20T18:39:31.306270+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p21.png"
  }
}
```

</details>

---


### Tool result

_source line 854 · 2026-05-20T18:39:32.013468+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1411
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-20T18:39:32.017115+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 710
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-20T18:39:32.017634+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p22.png"
  }
}
```

</details>

---


### Tool call

_source line 857 · 2026-05-20T18:39:32.521160+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p23.png"
  }
}
```

</details>

---


### Tool result

_source line 858 · 2026-05-20T18:39:32.974056+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 859 · 2026-05-20T18:39:32.974518+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p24.png"
  }
}
```

</details>

---


### Tool result

_source line 860 · 2026-05-20T18:39:33.431911+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 861 · 2026-05-20T18:39:33.432357+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p25.png"
  }
}
```

</details>

---


### Tool result

_source line 862 · 2026-05-20T18:39:34.087328+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1112
}
```

</details>

---


### Tool call

_source line 863 · 2026-05-20T18:39:34.087851+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p26.png"
  }
}
```

</details>

---


### Tool result

_source line 864 · 2026-05-20T18:39:34.541278+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-20T18:39:34.893847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-20T18:39:46.342328+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
  "project": "schema_semantic_constrained_ie",
  "pages": "27-33",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.pdf",
    "project": "schema_semantic_constrained_ie",
    "pages": "27-33",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-20T18:39:47.147638+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 27, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.2}, {\"page\": 28, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 533.1}, {\"page\": 29, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 460.0}, {\"page\": 30, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 452.3}, {\"page\": 31, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.1}, {\"page\": 32, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p32.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.1}, {\"page\": 33, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p33.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 302.5}], \"total_pages\": 33, \"rendered_pages\": 7, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-20T18:39:54.848717+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p27.png"
  }
}
```

</details>

---


### Tool call

_source line 869 · 2026-05-20T18:39:55.401886+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p28.png"
  }
}
```

</details>

---


### Tool result

_source line 870 · 2026-05-20T18:39:56.206852+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1358
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-20T18:39:56.209182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-20T18:39:56.209762+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p29.png"
  }
}
```

</details>

---


### Tool call

_source line 873 · 2026-05-20T18:39:56.661897+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p30.png"
  }
}
```

</details>

---


### Tool result

_source line 874 · 2026-05-20T18:39:57.114841+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 875 · 2026-05-20T18:39:57.215704+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p31.png"
  }
}
```

</details>

---


### Tool result

_source line 876 · 2026-05-20T18:39:58.072522+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-20T18:39:58.075956+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 878 · 2026-05-20T18:39:58.076399+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p32.png"
  }
}
```

</details>

---


### Tool call

_source line 879 · 2026-05-20T18:39:58.377840+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/_pdf_images/main_p33.png"
  }
}
```

</details>

---


### Tool result

_source line 880 · 2026-05-20T18:39:58.983129+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-20T18:39:59.037903+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 660
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-20T18:44:54.448014+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级约束的框架，用于自回归 LLM 生成时的类型约束执行。系统采用双层架构：grammar layer（EBNF + XGrammar，执行 JSON 结构和词汇约束）和 semantic layer（有状态 logits processor，维护实体注册表执行 domain/range 类型约束）。论文提出三级 decidability taxonomy（context-free / prefixes-decidable / non-local），用 pumping lemma 证明 Level 2 约束非 context-free，并在 SciERC、DocRED、WikiEvents 三个数据集上用 4 个模型（7-8B 规模为主）验证约束执行效果。\n\n## Strengths\n\n**S1.** 三级 decidability taxonomy 是本文最突出的理论贡献。将 IE 类型约束按可判定性分层（Level 1: context-free 可用 PDA 执行；Level 2: prefixes-decidable 需有状态转换器；Level 3: non-local 不可在 token 级执行）的框架清晰、well-motivated，为后续研究提供了有用的分析工具。分类边界通过形式化分析建立，不是 ad hoc 的。\n\n**S2.** 双层架构设计干净，grammar 与 semantic 层的关注点分离（structural validity vs. type validity）优雅地匹配了 decidability taxonomy 的前两级。Grammar-first fallback（§4）是合理的设计选择：当两层冲突时优先保证 JSON 结构完整性，CF 率作为代价指标被诚实地报告和分析。\n\n**S3.** 消融实验设计细致。Table 1（SciERC 五路消融）有效隔离了各约束类型（RV、ET、CF、DR）的贡献：Full S1 将 DR 从 15.37% 降至 0.93%，R-F1 基本不变（±0.06 pp），证明约束执行不损害提取质量。Table 2（DocRED fine-tuning 四路消融）进一步在 2 模型 × 2 数据集 × full S1 上验证了一致性。\n\n**S4.** 诚实的 limitation 讨论。论文明确承认 CF 的模型依赖性、WikiEvents 的初步性质、70B 评估的有限性，以及 κ̄ 仅为描述性指标。这种自我批评意识在投稿论文中值得肯定。\n\n**S5.** 附录内容极其丰富（23 页），包括完整的 pumping lemma 证明（Appendix O）、per-relation 违规分析（Appendix D）、beam search 兼容性（Appendix F）、prompt sensitivity（Appendix I）、错误案例分析（Appendix J）、post-hoc type consistency resolution（Appendix M）等。这体现了扎实的研究工作。\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1. [critical] 缺少最直接可比的 constrained decoding baseline 对比**\n- 具体位置：Section 5, Section 6 (Related Work)\n- 问题：论文在 Related Work（Section 6, page 8）明确引用了 BoostCD (Sakota et al., 2025) 和 IterGen (Ugare et al., 2025) 这两个最接近的系统——前者将 constrained 和 unconstrained decoding 通过 boosting 结合并**专门应用于 IE**，后者实现了 iterative semantic-aware structured generation with backtracking。然而实验中**完全没有与它们对比**，仅与 unconstrained、grammar-only、post-hoc filtering 对比。\n- 为什么影响接收：如果 BoostCD 或 IterGen 在相同 benchmark 上能达到类似的类型约束执行效果（或更好的 F1），OntoCoDec 的增量贡献将大幅缩水。BoostCD 发表于 EMNLP 2025，专门做 IE constrained decoding，是最自然的 baseline。论文将它们定位为\"不同方法\"（boosting vs. compilation）但这恰恰需要实验验证而非定性陈述。\n- 建议：在 SciERC 和 DocRED 上至少复现 BoostCD 的 zero-shot 设置进行对比。如果因为实现原因无法复现，需要明确讨论为什么不可比，并引用这些系统报告的相关数字进行间接对比。\n\n**W2. [critical] WikiEvents EE 评估统计效力严重不足**\n- 具体位置：Section 5.4, Table 5 (page 7)\n- 问题：WikiEvents 测试集仅 20 篇文档（194/20/20 split，per Li et al., 2021）。论文报告 R-F1 with ±1.1 pp 95% CI，但在如此小的样本上：(a) 置信区间实际上可能被低估（bootstrap 在小样本上的覆盖率偏低）；(b) 论文仍从中得出 EE 泛化性结论（\"The framework generalizes to event extraction with 245 constraints across three tokenizer families\"，page 2, Contribution 3），这个 claim 的证据基础太薄弱。\n- 为什么影响接收：Contribution 3 明确将 WikiEvents EE 列为三大贡献之一（\"systematic evaluation of type constraint enforcement in LM-based IE: the first evaluation...extends to event extraction\"），但 20 篇文档的测试集无法支撑\"systematic evaluation\"的措辞。\n- 建议：(a) 在 Contribution 3 中明确限定 EE 结果为\"preliminary demonstration\"而非\"systematic evaluation\"；(b) 讨论统计效力限制（effect size 需要多大才能在 n=20 下被检测到）；(c) 如果可能，补充更大规模 EE 数据集的结果。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W3. [warning] Pumping lemma 证明的形式化与实际系统存在 gap**\n- 具体位置：Appendix O (pages 32-33), Proposition 1 (page 3)\n- 问题：Appendix O 的证明构造了一个语言 L，其中类型合法性依赖于跨位置的实体-关系引用关系。证明的核心论点——PDA 的 LIFO stack 无法追踪实体位置与关系 head/tail 类型字段的跨位置依赖——是正确的。但证明存在一个形式化 gap：它假设实体引用是基于**位置索引**的（pumping 改变位置导致引用错误），而实际的 JSON 输出格式使用**实体名称**（字符串引用）。在名称引用下，pumping 一个实体条目不会改变其他实体的名称引用，但会改变实体注册表中的类型绑定。证明应更明确地说明：非 CF 性来源于\"实体名称到类型的绑定\"在串行生成中的跨位置依赖，而不仅是位置索引的偏移。\n- 建议：在证明中增加一段说明，将形式语言的字符串结构与实际 JSON 格式的对应关系明确化，特别是解释为什么名称引用下 pumping 仍然破坏类型一致性。\n\n**W4. [warning] DocRED beam search 仅用 50 文档子集评估**\n- 具体位置：Section 5.2, Table 3 footnote (page 6), Appendix F (page 25-26)\n- 问题：DocRED 的 beam search zero-shot 评估仅用 50 文档子集（998 文档中的 5%），论文解释为\"due to extended generation under high-temperature sampling with complex schema\"。然而论文的关键 claim 之一是\"CF is resolvable via beam search\"（Abstract, Section 5），这个 claim 在 DocRED 上的证据基础仅为 5% 子集。Table 15（Appendix F）显示 beam search 在 DocRED 上的 CF 从 28.4% 降至 21.4%，远未\"resolve\"。\n- 建议：(a) 在 Abstract 和 Section 5 中限定 beam search 的 CF resolution claim（\"substantially reduces\" 而非 \"resolves\"）；(b) 明确报告 50-document 子集与全集的分布差异分析。\n\n**W5. [warning] \"Formally compiles\" 措辞过度**\n- 具体位置：Abstract (\"formally compiles\"), Section 3 (\"OntoCoDec compiles\"), Section 7\n- 问题：Grammar layer 确实是编译（ontology → EBNF grammar → PDA），符合 PL 传统意义上的 compilation。但 semantic layer 是**运行时规则解释**（runtime rule-based masking via stateful logits processor），不是传统意义上的编译。\"Compile\" 隐含着离线、静态的转换过程，而 semantic layer 的实体注册表是在生成过程中动态维护的。\n- 建议：区分两层的\"编译\"性质——grammar layer 是 ahead-of-time compilation，semantic layer 是 rule-based runtime enforcement derived from the ontology。或使用更准确的术语如 \"translates IE ontologies into composable token-level constraints\"。\n\n**W6. [warning] 与 GoLLIE 等 schema-aware IE 系统缺乏量化对比**\n- 具体位置：Section 6 (page 8)\n- 问题：论文将 GoLLIE (Sainz et al., 2024)、KnowCoder (Li et al., 2024) 等 training-based schema-aware IE 系统定位为\"complementary rather than competing\"。这个定位在概念上合理（decoding-time enforcement vs. training-time schema awareness），但读者仍然需要知道：在相同 benchmark（如 SciERC zero-shot）上，OntoCoDec + unconstrained LLM 与 GoLLIE 的 F1 差距是多少？如果 GoLLIE 的 F1 远高于 OntoCoDec，那么\"complementary\"的说法需要更具体地解释 complementary 的价值。\n- 建议：在 Related Work 或 Discussion 中引用 GoLLIE 在 SciERC/DocRED 上的报告数字，进行间接对比，并讨论 OntoCoDec 在 GoLLIE 之上是否能提供额外收益。\n\n**W7. [warning] κ̄ 部署指导的证据不足**\n- 具体位置：Section 4 (Eq. 3), Appendix N (page 32)\n- 问题：κ̄ 被提议为部署指导的描述性指标（\"descriptive metric correlating schema restrictiveness with enforcement outcomes\"）。但实证支撑仅来自 2 个数据集（SciERC κ̄=0.333 vs. DocRED κ̄=0.812），样本量极小。且 κ̄ 与 DR 的关系受模型、fine-tuning 状态、beam search 等多因素影响，仅凭 2 个点无法建立有意义的预测关系。\n- 建议：(a) 更明确地标记 κ̄ 为 exploratory/preliminary metric；(b) 如果可能，增加更多不同 κ̄ 值的数据集/子集点；(c) 讨论 κ̄ 与其他因素（模型能力、fine-tuning 状态）的交互作用。\n\n### Minor 问题（不影响接收）\n\n**M1.** 主体文本似乎略超 8 页：Section 7 结论延伸至 page 9 约 10 行（lines 650-660）。建议检查是否严格符合 EMNLP 2026 的 8 页限制。\n\n**M2.** Table 密度极高（主体 5 张表 + 附录 20+ 张表），部分主体表格（如 Table 4 的 cross-model zero-shot）信息密度可以通过图表更好地传达。\n\n**M3.** \"Best-effort pair-based enforcement\"（Section 3.3）的精确含义可以更明确定义：(a) 当 head 位置的类型在 head 生成时尚不能确定（如 GENERIC 类型歧义），fallback 行为是什么？(b) 是否存在 head 类型 ambiguity 导致错误 tail 类型约束的 corner case？附录 J 的错误分析部分涵盖了这些情况但主体文本应更明确。\n\n**M4.** 引用审计发现：1 个 orphan bib entry（schmidt2025grammar，在 .bib 中但未被引用）；2 篇论文在 OpenAlex 中未找到（regino2025kgcurator, formattax2026），可能是非常新的 preprint；8 个 minor author name mismatches（多为 unicode/格式差异，不影响正确性）。\n\n**M5.** Grammar-first fallback 的级联失败分析：如果 grammar mask 也为空集（G(t) = ∅），系统行为如何？虽然理论上 grammar 层保证至少有合法 JSON 延续，但在极端 tokenizer edge case（如 rare byte-level tokens）下是否有保障？论文未讨论。\n\n## Questions（需要作者澄清）\n\n**Q1.** Proposition 1 的证明（Appendix O）中，pumping 操作具体如何破坏名称引用下的类型一致性？如果实体名称是唯一的，pump 一个新的实体条目后，关系引用的实体名称仍然存在于输出中，只是其位置变了。类型绑定是由名称到类型的映射决定的，不依赖位置。请澄清证明中\"位置偏移导致类型违规\"的推理如何适用于名称引用格式。\n\n**Q2.** BoostCD (Sakota et al., 2025) 在 SciERC 和 DocRED 上报告的 constrained decoding 结果是什么？如果作者认为 BoostCD 不可比，请解释具体原因（是约束类型不同、输出格式不同、还是其他原因）。\n\n**Q3.** 论文的 grammar-first fallback 在 DocRED 上的 CF 率（fallback 频率）相当高（zero-shot: ~9.90%）。这意味着约 10% 的解码步骤中 semantic layer 被跳过。这些被跳过的位置是否集中在特定类型的 relation（如高 κ 的 relation）？是否存在某些 relation 类型的约束实际上从未被有效执行？\n\n**Q4.** Fine-tuning（LoRA）的 composability 实验（Table 2）中，LoRA 是在**有**约束解码的条件下训练的，还是在**无**约束解码的条件下训练的？如果是无约束训练，那么 fine-tuned 模型的输出分布与 constrained decoding 的 mask 之间可能存在 distribution mismatch。如果是有约束训练，请说明训练时的约束配置。\n\n**Q5.** Semantic layer 的实体注册表（entity registry）在生成过程中动态维护，这意味着实体的注册顺序可能影响后续关系的约束执行。如果 LLM 先生成了一个 GENERIC 类型的实体，后续所有引用该实体的关系都会受到 GENERIC 歧义的影响。论文是否分析过实体生成顺序对最终约束执行效果的影响？\n\n## Missing References\n\n1. **GENRE** (De Cao et al., 2021) 虽已引用，但 **GenIE** (Josifoski et al., 2022) 作为最早将 constrained decoding 系统化应用于 IE 的工作之一，在主体 Related Work 中被遗漏（仅在附录 B 中出现），应在主体中提及。\n2. 论文未引用 **NNF** (Nusgart et al., 2025, \"Constrained Decoding with Grammars and Lookahead\") 等关于 grammar-constrained decoding lookahead 的最新工作，与本文的 grammar-first fallback 机制相关。\n\n## Scores\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 形式化框架合理但 pumping lemma 证明与实际格式存在 gap；实验方法论整体可靠但 WikiEvents (n=20) 和 DocRED beam search (n=50) 统计效力不足 |\n| Excitement | 3/5 | Decidability taxonomy 是有用的理论贡献，双层架构设计干净；但实际影响受限于评估规模（7-8B 为主）和缺乏与最接近 baseline 的对比 |\n| Overall | 3.5/5 | Borderline Conference。核心贡献（decidability taxonomy + 双层编译约束执行）扎实且有新意；实验评估全面但有关键缺陷（missing baselines、统计效力）。修订后（补充 BoostCD/IterGen 对比、增强形式化、限定 claims 范围）有望达到 Conference 水平 |\n| Confidence | 4/5 | 对 constrained decoding 和 IE 有研究经验，仔细阅读了全文含 33 页附录 |\n| Reproducibility | 4/5 | 实验设置详细（Appendix A/G），prompt templates 公开（Table 6），bootstrap 参数报告，但代码未提交 |\n\n**Overall Assessment: 3.5** — Borderline Conference\n\n**一句话总结**：一篇理论动机清晰、系统设计干净的约束解码论文，但缺少与最直接可比系统（BoostCD、IterGen）的实验对比，且部分实验的统计效力不足以支撑其 claim 的范围。\n",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints\n\n## Summary\n\n本文提出 OntoCoDec，一个将 IE 本体编译为 token 级约束的框架，用于自回归 LLM 生成时的类型约束执行。系统采用双层架构：grammar layer（EBNF + XGrammar，执行 JSON 结构和词汇约束）和 semantic layer（有状态 logits processor，维护实体注册表执行 domain/range 类型约束）。论文提出三级 decidability taxonomy（context-free / prefixes-decidable / non-local），用 pumping lemma 证明 Level 2 约束非 context-free，并在 SciERC、DocRED、WikiEvents 三个数据集上用 4 个模型（7-8B 规模为主）验证约束执行效果。\n\n## Strengths\n\n**S1.** 三级 decidability taxonomy 是本文最突出的理论贡献。将 IE 类型约束按可判定性分层（Level 1: context-free 可用 PDA 执行；Level 2: prefixes-decidable 需有状态转换器；Level 3: non-local 不可在 token 级执行）的框架清晰、well-motivated，为后续研究提供了有用的分析工具。分类边界通过形式化分析建立，不是 ad hoc 的。\n\n**S2.** 双层架构设计干净，grammar 与 semantic 层的关注点分离（structural validity vs. type validity）优雅地匹配了 decidability taxonomy 的前两级。Grammar-first fallback（§4）是合理的设计选择：当两层冲突时优先保证 JSON 结构完整性，CF 率作为代价指标被诚实地报告和分析。\n\n**S3.** 消融实验设计细致。Table 1（SciERC 五路消融）有效隔离了各约束类型（RV、ET、CF、DR）的贡献：Full S1 将 DR 从 15.37% 降至 0.93%，R-F1 基本不变（±0.06 pp），证明约束执行不损害提取质量。Table 2（DocRED fine-tuning 四路消融）进一步在 2 模型 × 2 数据集 × full S1 上验证了一致性。\n\n**S4.** 诚实的 limitation 讨论。论文明确承认 CF 的模型依赖性、WikiEvents 的初步性质、70B 评估的有限性，以及 κ̄ 仅为描述性指标。这种自我批评意识在投稿论文中值得肯定。\n\n**S5.** 附录内容极其丰富（23 页），包括完整的 pumping lemma 证明（Appendix O）、per-relation 违规分析（Appendix D）、beam search 兼容性（Appendix F）、prompt sensitivity（Appendix I）、错误案例分析（Appendix J）、post-hoc type consistency resolution（Appendix M）等。这体现了扎实的研究工作。\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1. [critical] 缺少最直接可比的 constrained decoding baseline 对比**\n- 具体位置：Section 5, Section 6 (Related Work)\n- 问题：论文在 Related Work（Section 6, page 8）明确引用了 BoostCD (Sakota et al., 2025) 和 IterGen (Ugare et al., 2025) 这两个最接近的系统——前者将 constrained 和 unconstrained decoding 通过 boosting 结合并**专门应用于 IE**，后者实现了 iterative semantic-aware structured generation with backtracking。然而实验中**完全没有与它们对比**，仅与 unconstrained、grammar-only、post-hoc filtering 对比。\n- 为什么影响接收：如果 BoostCD 或 IterGen 在相同 benchmark 上能达到类似的类型约束执行效果（或更好的 F1），OntoCoDec 的增量贡献将大幅缩水。BoostCD 发表于 EMNLP 2025，专门做 IE constrained decoding，是最自然的 baseline。论文将它们定位为\"不同方法\"（boosting vs. compilation）但这恰恰需要实验验证而非定性陈述。\n- 建议：在 SciERC 和 DocRED 上至少复现 BoostCD 的 zero-shot 设置进行对比。如果因为实现原因无法复现，需要明确讨论为什么不可比，并引用这些系统报告的相关数字进行间接对比。\n\n**W2. [critical] WikiEvents EE 评估统计效力严重不足**\n- 具体位置：Section 5.4, Table 5 (page 7)\n- 问题：WikiEvents 测试集仅 20 篇文档（194/20/20 split，per Li et al., 2021）。论文报告 R-F1 with ±1.1 pp 95% CI，但在如此小的样本上：(a) 置信区间实际上可能被低估（bootstrap 在小样本上的覆盖率偏低）；(b) 论文仍从中得出 EE 泛化性结论（\"The framework generalizes to event extraction with 245 constraints across three tokenizer families\"，page 2, Contribution 3），这个 claim 的证据基础太薄弱。\n- 为什么影响接收：Contribution 3 明确将 WikiEvents EE 列为三大贡献之一（\"systematic evaluation of type constraint enforcement in LM-based IE: the first evaluation...extends to event extraction\"），但 20 篇文档的测试集无法支撑\"systematic evaluation\"的措辞。\n- 建议：(a) 在 Contribution 3 中明确限定 EE 结果为\"preliminary demonstration\"而非\"systematic evaluation\"；(b) 讨论统计效力限制（effect size 需要多大才能在 n=20 下被检测到）；(c) 如果可能，补充更大规模 EE 数据集的结果。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W3. [warning] Pumping lemma 证明的形式化与实际系统存在 gap**\n- 具体位置：Appendix O (pages 32-33), Proposition 1 (page 3)\n- 问题：Appendix O 的证明构造了一个语言 L，其中类型合法性依赖于跨位置的实体-关系引用关系。证明的核心论点——PDA 的 LIFO stack 无法追踪实体位置与关系 head/tail 类型字段的跨位置依赖——是正确的。但证明存在一个形式化 gap：它假设实体引用是基于**位置索引**的（pumping 改变位置导致引用错误），而实际的 JSON 输出格式使用**实体名称**（字符串引用）。在名称引用下，pumping 一个实体条目不会改变其他实体的名称引用，但会改变实体注册表中的类型绑定。证明应更明确地说明：非 CF 性来源于\"实体名称到类型的绑定\"在串行生成中的跨位置依赖，而不仅是位置索引的偏移。\n- 建议：在证明中增加一段说明，将形式语言的字符串结构与实际 JSON 格式的对应关系明确化，特别是解释为什么名称引用下 pumping 仍然破坏类型一致性。\n\n**W4. [warning] DocRED beam search 仅用 50 文档子集评估**\n- 具体位置：Section 5.2, Table 3 footnote (page 6), Appendix F (page 25-26)\n- 问题：DocRED 的 beam search zero-shot 评估仅用 50 文档子集（998 文档中的 5%），论文解释为\"due to extended generation under high-temperature sampling with complex schema\"。然而论文的关键 claim 之一是\"CF is resolvable via beam search\"（Abstract, Section 5），这个 claim 在 DocRED 上的证据基础仅为 5% 子集。Table 15（Appendix F）显示 beam search 在 DocRED 上的 CF 从 28.4% 降至 21.4%，远未\"resolve\"。\n- 建议：(a) 在 Abstract 和 Section 5 中限定 beam search 的 CF resolution claim（\"substantially reduces\" 而非 \"resolves\"）；(b) 明确报告 50-document 子集与全集的分布差异分析。\n\n**W5. [warning] \"Formally compiles\" 措辞过度**\n- 具体位置：Abstract (\"formally compiles\"), Section 3 (\"OntoCoDec compiles\"), Section 7\n- 问题：Grammar layer 确实是编译（ontology → EBNF grammar → PDA），符合 PL 传统意义上的 compilation。但 semantic layer 是**运行时规则解释**（runtime rule-based masking via stateful logits processor），不是传统意义上的编译。\"Compile\" 隐含着离线、静态的转换过程，而 semantic layer 的实体注册表是在生成过程中动态维护的。\n- 建议：区分两层的\"编译\"性质——grammar layer 是 ahead-of-time compilation，semantic layer 是 rule-based runtime enforcement derived from the ontology。或使用更准确的术语如 \"translates IE ontologies into composable token-level constraints\"。\n\n**W6. [warning] 与 GoLLIE 等 schema-aware IE 系统缺乏量化对比**\n- 具体位置：Section 6 (page 8)\n- 问题：论文将 GoLLIE (Sainz et al., 2024)、KnowCoder (Li et al., 2024) 等 training-based schema-aware IE 系统定位为\"complementary rather than competing\"。这个定位在概念上合理（decoding-time enforcement vs. training-time schema awareness），但读者仍然需要知道：在相同 benchmark（如 SciERC zero-shot）上，OntoCoDec + unconstrained LLM 与 GoLLIE 的 F1 差距是多少？如果 GoLLIE 的 F1 远高于 OntoCoDec，那么\"complementary\"的说法需要更具体地解释 complementary 的价值。\n- 建议：在 Related Work 或 Discussion 中引用 GoLLIE 在 SciERC/DocRED 上的报告数字，进行间接对比，并讨论 OntoCoDec 在 GoLLIE 之上是否能提供额外收益。\n\n**W7. [warning] κ̄ 部署指导的证据不足**\n- 具体位置：Section 4 (Eq. 3), Appendix N (page 32)\n- 问题：κ̄ 被提议为部署指导的描述性指标（\"descriptive metric correlating schema restrictiveness with enforcement outcomes\"）。但实证支撑仅来自 2 个数据集（SciERC κ̄=0.333 vs. DocRED κ̄=0.812），样本量极小。且 κ̄ 与 DR 的关系受模型、fine-tuning 状态、beam search 等多因素影响，仅凭 2 个点无法建立有意义的预测关系。\n- 建议：(a) 更明确地标记 κ̄ 为 exploratory/preliminary metric；(b) 如果可能，增加更多不同 κ̄ 值的数据集/子集点；(c) 讨论 κ̄ 与其他因素（模型能力、fine-tuning 状态）的交互作用。\n\n### Minor 问题（不影响接收）\n\n**M1.** 主体文本似乎略超 8 页：Section 7 结论延伸至 page 9 约 10 行（lines 650-660）。建议检查是否严格符合 EMNLP 2026 的 8 页限制。\n\n**M2.** Table 密度极高（主体 5 张表 + 附录 20+ 张表），部分主体表格（如 Table 4 的 cross-model zero-shot）信息密度可以通过图表更好地传达。\n\n**M3.** \"Best-effort pair-based enforcement\"（Section 3.3）的精确含义可以更明确定义：(a) 当 head 位置的类型在 head 生成时尚不能确定（如 GENERIC 类型歧义），fallback 行为是什么？(b) 是否存在 head 类型 ambiguity 导致错误 tail 类型约束的 corner case？附录 J 的错误分析部分涵盖了这些情况但主体文本应更明确。\n\n**M4.** 引用审计发现：1 个 orphan bib entry（schmidt2025grammar，在 .bib 中但未被引用）；2 篇论文在 OpenAlex 中未找到（regino2025kgcurator, formattax2026），可能是非常新的 preprint；8 个 minor author name mismatches（多为 unicode/格式差异，不影响正确性）。\n\n**M5.** Grammar-first fallback 的级联失败分析：如果 grammar mask 也为空集（G(t) = ∅），系统行为如何？虽然理论上 grammar 层保证至少有合法 JSON 延续，但在极端 tokenizer edge case（如 rare byte-level tokens）下是否有保障？论文未讨论。\n\n## Questions（需要作者澄清）\n\n**Q1.** Proposition 1 的证明（Appendix O）中，pumping 操作具体如何破坏名称引用下的类型一致性？如果实体名称是唯一的，pump 一个新的实体条目后，关系引用的实体名称仍然存在于输出中，只是其位置变了。类型绑定是由名称到类型的映射决定的，不依赖位置。请澄清证明中\"位置偏移导致类型违规\"的推理如何适用于名称引用格式。\n\n**Q2.** BoostCD (Sakota et al., 2025) 在 SciERC 和 DocRED 上报告的 constrained decoding 结果是什么？如果作者认为 BoostCD 不可比，请解释具体原因（是约束类型不同、输出格式不同、还是其他原因）。\n\n**Q3.** 论文的 grammar-first fallback 在 DocRED 上的 CF 率（fallback 频率）相当高（zero-shot: ~9.90%）。这意味着约 10% 的解码步骤中 semantic layer 被跳过。这些被跳过的位置是否集中在特定类型的 relation（如高 κ 的 relation）？是否存在某些 relation 类型的约束实际上从未被有效执行？\n\n**Q4.** Fine-tuning（LoRA）的 composability 实验（Table 2）中，LoRA 是在**有**约束解码的条件下训练的，还是在**无**约束解码的条件下训练的？如果是无约束训练，那么 fine-tuned 模型的输出分布与 constrained decoding 的 mask 之间可能存在 distribution mismatch。如果是有约束训练，请说明训练时的约束配置。\n\n**Q5.** Semantic layer 的实体注册表（entity registry）在生成过程中动态维护，这意味着实体的注册顺序可能影响后续关系的约束执行。如果 LLM 先生成了一个 GENERIC 类型的实体，后续所有引用该实体的关系都会受到 GENERIC 歧义的影响。论文是否分析过实体生成顺序对最终约束执行效果的影响？\n\n## Missing References\n\n1. **GENRE** (De Cao et al., 2021) 虽已引用，但 **GenIE** (Josifoski et al., 2022) 作为最早将 constrained decoding 系统化应用于 IE 的工作之一，在主体 Related Work 中被遗漏（仅在附录 B 中出现），应在主体中提及。\n2. 论文未引用 **NNF** (Nusgart et al., 2025, \"Constrained Decoding with Grammars and Lookahead\") 等关于 grammar-constrained decoding lookahead 的最新工作，与本文的 grammar-first fallback 机制相关。\n\n## Scores\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 形式化框架合理但 pumping lemma 证明与实际格式存在 gap；实验方法论整体可靠但 WikiEvents (n=20) 和 DocRED beam search (n=50) 统计效力不足 |\n| Excitement | 3/5 | Decidability taxonomy 是有用的理论贡献，双层架构设计干净；但实际影响受限于评估规模（7-8B 为主）和缺乏与最接近 baseline 的对比 |\n| Overall | 3.5/5 | Borderline Conference。核心贡献（decidability taxonomy + 双层编译约束执行）扎实且有新意；实验评估全面但有关键缺陷（missing baselines、统计效力）。修订后（补充 BoostCD/IterGen 对比、增强形式化、限定 claims 范围）有望达到 Conference 水平 |\n| Confidence | 4/5 | 对 constrained decoding 和 IE 有研究经验，仔细阅读了全文含 33 页附录 |\n| Reproducibility | 4/5 | 实验设置详细（Appendix A/G），prompt templates 公开（Table 6），bootstrap 参数报告，但代码未提交 |\n\n**Overall Assessment: 3.5** — Borderline Conference\n\n**一句话总结**：一篇理论动机清晰、系统设计干净的约束解码论文，但缺少与最直接可比系统（BoostCD、IterGen）的实验对比，且部分实验的统计效力不足以支撑其 claim 的范围。\n",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-20T18:44:58.478985+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4030
}
```

</details>

---


### Assistant

_source line 884 · 2026-05-20T18:45:13.021279+00:00_

审稿意见已提交给 Review Director。

审查要点总结：

- **Overall: 3.5**（Borderline Conference）
- **2 个 Must-Fix**：(1) 缺少 BoostCD/IterGen 这两个最直接可比的 constrained decoding baseline 对比；(2) WikiEvents 仅 20 文档测试集，无法支撑 "systematic evaluation" 的 claim
- **5 个 Should-Fix**：pumping lemma 证明与实际 JSON 格式存在形式化 gap；DocRED beam search 仅 50 文档子集；"formally compiles" 措辞对 semantic layer 过度；缺乏与 GoLLIE 等系统的量化对比；κ̄ 部署指导证据不足
- **5 个 Minor**：页数可能略超限、表格密度高、best-effort 定义需更精确、引用审计小问题、级联失败 edge case 未讨论
- **5 个 Questions**：要求作者澄清 pumping lemma 在名称引用下的适用性、BoostCD 不可比的具体原因、fallback 的 per-relation 分布、LoRA 训练时是否有约束、实体生成顺序的影响

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 23

## Round 23

4 recorded events


### User

_source line 885 · 2026-05-20T18:45:52.451559+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

请逐条回应以下 Reviewer 2 的意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 2 的完整审稿意见：

### Summary
本文提出 OntoCoDec，一个将 IE 本体编译为 token 级解码约束的框架。设计基于 decidability analysis 的分层架构：grammar layer（CFG）保证 JSON 结构和词汇约束，semantic layer（prefix-decidable with state）通过运行时 entity registry 执行 domain/range 类型约束。在 SciERC、DocRED、WikiEvents 上对 3–4 个模型（7–70B）进行了系统评估，表明 LoRA + S1 可将 DR 违规降至 ≤0.09%，R-F1 变化在 ±0.6pp 内。论文同时引入 constraint tightness κ̄ 作为描述性指标。

### Must-Fix

**W1 [critical] 正文超过 8 页限制。**
Discussion and Conclusion 的最后约 11 行溢出到第 9 页。EMNLP 2026 (via ARR) 严格限制长文正文 ≤ 8 页。格式违规可能导致 desk reject。

**W2 [critical] CF 代价在 Abstract 和 Introduction 中被系统性低估。**
Abstract 用 "modest" 描述零样本 SciERC 9.90% 和 WikiEvents 15–21% 的 CF 率是误导性的。Introduction 完全没提 CF。隐藏主要副作用降低论文可信度。

**W3 [critical] κ̄ 作为独立贡献（Contribution 2）的定位过高。**
κ̄ = 1 − |σ(r)|/|E|² 本质上是约束表的归一化密度。仅在 2 个数据集上验证（SciERC κ̄=0.333 vs DocRED κ̄=0.842），且 κ̄ 无法独立预测 enforcement 效果（Mistral SciERC DR 降幅仅 76% vs Qwen/Llama 94–99%）。

### Should-Fix

**W4 [warning] "any autoregressive LM" 声称与实际验证范围不符。**
主要实验在 7–8B 模型上，70B 仅初步结果，无小模型/API-only 验证。

**W5 [warning] DocRED 零样本 DR 降幅仅 45%（vs SciERC 94%），讨论不充分。**
论文将此归因于 κ̄ 差异，但这只是 restate 了问题。残余 DR 10.21% 对 "type-safe extraction" 目标构成挑战。

**W6 [warning] WikiEvents 评估局限性。**
Fine-tuning 基于 20-doc test set，CIs 很宽。零样本 entity F1 从 0→12-18% 主要来自格式修复而非语义改善。Grammar-only 行缺少 F1。

**W7 [warning] "formally compiles" 措辞与实际技术贡献不匹配。**
Grammar layer 是编译，但 semantic layer 是运行时规则解释。"Compile" 隐含离线、静态转换，与 semantic layer 的动态维护不符。

### Minor
**M1.** 孤立 bib entry（schmidt2025grammar）
**M2.** 表格字体偏小（Table 1, 3, 4）
**M3.** S1/S2 命名不直观，混用 "S1 (joint extraction)" 和 "Full (S1)"
**M4.** §4 脚注 1 关于对称 relation 的处理应在正文讨论
**M5.** formattax2026 和 regino2025kgcurator 在 OpenAlex 未找到

### Scores
Soundness 3.5/5, Excitement 2.5/5, Overall 3.0/5 (Findings), Confidence 4/5, Novelty 2.5/5, Clarity 3.5/5

---

请逐条回应，特别关注：
1. 你是否同意正文超页是 must-fix？
2. 你是否同意 CF 代价被低估？R2 认为 "modest" 描述 9.90% CF 是误导——你的判断？
3. R2 给 Excitement 2.5/5 vs 你给 3/5——分歧在哪？
4. R2 的 Overall 3.0 vs 你的 3.5——你认为差距的核心原因是什么？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-20T18:48:11.732975+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应：逐条回应 Reviewer 2\n\n---\n\n## Must-Fix\n\n**[AGREE] R2-W1: 正文超过 8 页限制**\n同意这需要修复。Section 7 结论确实延伸至 page 9 约 11 行（lines 650–660）。我在初审中将此列为 Minor（M1），但 R2 升级为 critical 有其道理：EMNLP 2026 via ARR 的格式要求明确写了\"strict 8-page limit\"，格式违规可能导致 desk reject。不过我补充一点：这是**机械性可修复问题**（压缩结论段或调整排版即可），不反映论文的实质性缺陷。我倾向于将此归类为 **must-fix 但 low-effort**，不应影响学术评分。\n\n**[AGREE] R2-W2: CF 代价在 Abstract/Introduction 被低估**\n同意。我重新检查了 Abstract（page 1）原文：\"with modest CF costs from per-relation independence\"。对照实际数据：\n- SciERC zero-shot CF = 9.90%（Table 1, page 5）\n- WikiEvents zero-shot CF = 15–21%（Table 5, page 7）\n- DocRED zero-shot CF = 9.90%（Table 3, page 6）\n\n用 \"modest\" 描述接近 10% 的 fallback 率确实有误导之嫌。尤其 Introduction（Section 1）完全未提及 CF，只在 Section 4 和 5 才展开讨论。R2 的判断是对的——**隐藏主要副作用降低可信度**。\n\n我在初审中将 CF 的 claim 问题放在 W4（should-fix），聚焦于 \"resolvable via beam search\" 的措辞。R2 的角度更全面：不仅 beam search claim 需要限定，Abstract/Intro 本身就应当 upfront 呈现 CF 代价。我接受 R2 的升级，同意这应当是 **must-fix**。\n\n不过有一个 nuance：CF=9.90% 的含义需要澄清。CF 是 grammar-first fallback 的**触发率**（semantic mask 与 grammar mask 冲突的比例），不是\"输出错误率\"。当 fallback 触发时，grammar layer 仍保证 JSON 结构合法性，只是跳过了该位置的 semantic 类型约束。因此 CF=9.90% 不等于 9.90% 的输出不可用，但确实意味着约 10% 的类型约束检查被绕过。作者应在 Abstract 中区分这一点，而非笼统地说 \"modest\"。\n\n**[AGREE with nuance] R2-W3: κ̄ 作为独立贡献定位过高**\n基本同意，但对严重性判断略有保留。\n\n同意的部分：\n- κ̄ = 1 − |σ(r)|/|E|² 确实只是约束表的归一化密度，数学上 trivial\n- 仅 2 个数据点（SciERC κ̄=0.333, DocRED κ̄=0.842）无法建立有意义的预测关系\n- R2 指出的 Mistral 异常（DR 降幅仅 76% vs Qwen/Llama 94–99%，同一 κ̄）有力地说明 κ̄ 不能独立预测效果\n\n保留的部分：\n- 论文 Contribution 2 的原文是 \"A descriptive metric, constraint tightness κ̄, that correlates schema restrictiveness with enforcement outcomes and provides deployment guidance\"（page 2）。作者用了 \"descriptive\" 和 \"correlates\"，没有声称 predictive power。这与 R2 说的\"独立贡献定位过高\"之间存在程度差异\n- 作为一个 deployment heuristic（高 κ̄ → 更需要 beam search 或 fine-tuning），即使只有 2 个数据点，方向性的指导仍然有价值\n\n我倾向于将此保留为 **should-fix**（降级 Contribution 2 的措辞，改为 \"we additionally introduce...\" 而非独立贡献条目）而非 must-fix。但 R2 的核心批评——将一个 trivial metric 列为三大贡献之一——我认同这影响了论文的定位可信度。\n\n---\n\n## Should-Fix\n\n**[AGREE] R2-W4: \"any autoregressive LM\" 过度声称**\n同意。Abstract 的 \"applicable to any autoregressive LM\" 与实际验证范围（7–8B 为主，70B 仅 preliminary）不匹配。我在初审中漏掉了这个具体措辞问题。补充：论文也未验证 (a) <7B 小模型（约束执行可能因能力不足导致更高 CF），(b) API-only 模型（如 GPT-4、Claude，无法直接操作 logits），(c) 非 Transformer 架构。建议改为 \"applicable to autoregressive LMs with logits access\"。\n\n**[AGREE] R2-W5: DocRED 零样本 DR 降幅讨论不足**\n同意。DocRED zero-shot DR 从 18.46% 降至 10.21%（Table 3, page 6），降幅约 45%，远低于 SciERC 的 94%。论文将此归因于 κ̄ 差异（Section 5.2: \"reflects higher tightness κ̄=0.842 vs 0.333\"），但正如 R2 所说，这只是 restate 了现象而非解释了原因。\n\n我在初审中通过 W4（DocRED 50-doc subset）间接涉及了这个问题，但 R2 更直接地指出了核心矛盾：10.21% 的残余 DR 与论文标题中 \"Type-Constrained\" 的承诺之间存在张力。补充一个具体证据：Appendix D（page 22, Table 9）显示 DocRED 的 GENERIC←→OtherScientificTerm 冲突占 63.3% 的 CF violations，这表明残余 DR 主要来自**实体类型歧义**（GENERIC catch-all type），不是约束执行本身的失败，而是 schema 设计的固有模糊性。论文应更明确地讨论这一区分。\n\n**[AGREE] R2-W6: WikiEvents 评估局限性**\n同意。R2 的观察补充了我的初审（W2, critical）中未涉及的细节：\n- Zero-shot entity F1 从 0 → 12–18%（Table 5, page 7）主要是格式修复（unconstrained 输出无法被解析为合法 entity，constrained 输出至少结构合法），而非语义提取能力的改善。这一点我漏掉了，R2 判断精准\n- Grammar-only 行（Table 5）确实缺少 F1 数值（仅报告 violation rates），使得无法判断 semantic layer 在 EE 上的 incremental F1 贡献\n\n不过我仍然认为 WikiEvents 评估的**统计效力问题**（n=20 test docs）是更根本的 concern，应为 critical 而非 R2 标注的 warning。\n\n**[AGREE] R2-W7: \"formally compiles\" 措辞**\n完全同意，与我的初审 W5 一致。不再赘述。\n\n---\n\n## Minor\n\n**[AGREE] R2-M1:** 确认 orphan bib entry schmidt2025grammar，与我的 M4 一致。\n\n**[AGREE] R2-M2:** 表格字体偏小，Table 1/3/4 信息密度高，但在 ACL 双栏排版中普遍存在，属于 cosmetic issue。\n\n**[AGREE] R2-M3:** S1/S2 命名确实不直观。\"S1 (joint extraction)\" vs \"S2 (two-pass pipeline)\" 的缩写需要在首次使用时更明确定义，且 \"Full (S1)\" 的嵌套命名增加了阅读障碍。\n\n**[AGREE] R2-M4:** 对称 relation 的处理（脚注 1, page 4）确实重要到值得在正文讨论，因为它直接影响 κ̄ 的计算和约束的 asymmetry 语义。\n\n**[AGREE] R2-M5:** 与我的 M4 一致。formattax2026（Lee et al., 2026）和 regino2025kgcurator 在 OpenAlex 未找到，可能是极新的 preprint 尚未被索引。不影响引用正确性但建议验证。\n\n---\n\n## Director 提出的具体问题回应\n\n### 1. 正文超页是否 must-fix？\n\n**是。** R2 正确。EMNLP 2026 via ARR 规则明确且严格。虽然机械修复容易（压缩 11 行），但格式违规的 desk reject 风险不可忽视。我将此从 minor 升级为 must-fix。\n\n### 2. CF 代价被低估？\"modest\" 描述 9.90% CF 是否误导？\n\n**同意 R2 判断。** \"modest\" 用于描述 9.90% CF 确实具有误导性。一个有用的参照：post-hoc filtering 在 DocRED 上丢弃 48% 的 triples（Appendix C, page 22）——OntoCoDec 的 CF 确实远低于 post-hoc 的代价，但用 \"modest\" 而非给出具体数字掩盖了这一事实。Abstract 应直接报告 representative CF 数值（如 \"with CF rates of 0–9.9% depending on schema complexity\"），让读者自行判断是否 \"modest\"。\n\n### 3. Excitement 2.5 vs 3.0 的分歧\n\nR2 给 Excitement 2.5（\"Potentially interesting\"），我给 3.0（\"Interesting\"）。分歧来源：\n\n**R2 更低的原因可能是：**\n- R2 更看重 practical novelty——双层架构虽然设计干净，但 grammar-constrained decoding（Level 1）是已有工作（XGrammar、Outlines），OntoCoDec 的 incremental contribution 是 semantic layer（Level 2），且这个 layer 的效果受限于 schema 复杂度（DocRED 45% vs SciERC 94% 降幅）\n- R2 给 Novelty 2.5/5 进一步印证了这一判断：认为方法论新意有限\n\n**我给 3.0 的原因：**\n- Decidability taxonomy（三级分类）本身是有价值的理论贡献，为社区提供了分析 IE 约束执行问题的框架，超越了具体系统的实现\n- 将 PL/formal language theory 的分析工具引入 IE 问题是一个有趣的 cross-pollination\n\n**我的修正判断：** 在看到 R2 的完整意见后，我认为 2.5 偏低——decidability taxonomy 的理论价值不应因为系统 novelty 有限而被完全折价。但我也承认 3.0 可能偏高——taxonomy 本身虽然 well-motivated，但三级分类相当直观（CF 可解/有状态可解/不可在线解），不是深刻的理论发现。**维持 3.0 不变。**\n\n### 4. Overall 3.0 vs 3.5 的核心差距\n\nR2 给 3.0（Findings），我给 3.5（Borderline Conference）。半分差距的核心原因：\n\n**R2 的 3.0 逻辑（我的理解）：**\nR2 识别出一个**系统性 overclaiming 模式**——\"modest\" CF、κ̄ 作为独立贡献、\"any autoregressive LM\"、\"formally compiles\"——并认为这些不是孤立的措辞问题，而是论文对自身贡献的定位整体偏高。当多个 claim 同时被高估时，论文的可信度遭受累积损害。加上 Excitement 2.5，3.0 是合理的。\n\n**我的 3.5 逻辑：**\n我更看重论文的**实质贡献**而非措辞问题。核心技术（decidability taxonomy + 双层约束执行）是 sound 的，实验覆盖面广（3 datasets × 4 models × 多配置），消融设计细致。措辞问题可以在 revision 中修正而不改变技术贡献。缺少 BoostCD/IterGen baseline 是最实质性的缺陷。\n\n**交叉回应后的修正判断：**\nR2 的 overclaiming pattern 论点在我重新审视后确实成立：不是单个 claim 的问题，而是 Abstract/Intro/Contributions 整体呈现了比实际支撑更强的 narrative。这在 ARR 审稿中会降低 reviewer 信任度。\n\n但我仍然认为 3.5 比 3.0 更准确：\n- 论文的 Limitations section（page 10）诚实地覆盖了多数局限性\n- 附录中的分析深度（33 页）远超平均水平\n- 核心技术 contribution 是 sound 的，overclaiming 是 presentation 问题不是 substance 问题\n- 修订后（限定 claims + 补充 baselines）有明确的升级路径\n\n**最终维持 Overall 3.5**，但承认 R2 的 3.0 也在合理范围内。如果 BoostCD 对比实验显示 OntoCoDec 的 incremental gain 很小，我会倾向于降至 3.0。\n",
  "reviewer_id": "1",
  "project": "schema_semantic_constrained_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应：逐条回应 Reviewer 2\n\n---\n\n## Must-Fix\n\n**[AGREE] R2-W1: 正文超过 8 页限制**\n同意这需要修复。Section 7 结论确实延伸至 page 9 约 11 行（lines 650–660）。我在初审中将此列为 Minor（M1），但 R2 升级为 critical 有其道理：EMNLP 2026 via ARR 的格式要求明确写了\"strict 8-page limit\"，格式违规可能导致 desk reject。不过我补充一点：这是**机械性可修复问题**（压缩结论段或调整排版即可），不反映论文的实质性缺陷。我倾向于将此归类为 **must-fix 但 low-effort**，不应影响学术评分。\n\n**[AGREE] R2-W2: CF 代价在 Abstract/Introduction 被低估**\n同意。我重新检查了 Abstract（page 1）原文：\"with modest CF costs from per-relation independence\"。对照实际数据：\n- SciERC zero-shot CF = 9.90%（Table 1, page 5）\n- WikiEvents zero-shot CF = 15–21%（Table 5, page 7）\n- DocRED zero-shot CF = 9.90%（Table 3, page 6）\n\n用 \"modest\" 描述接近 10% 的 fallback 率确实有误导之嫌。尤其 Introduction（Section 1）完全未提及 CF，只在 Section 4 和 5 才展开讨论。R2 的判断是对的——**隐藏主要副作用降低可信度**。\n\n我在初审中将 CF 的 claim 问题放在 W4（should-fix），聚焦于 \"resolvable via beam search\" 的措辞。R2 的角度更全面：不仅 beam search claim 需要限定，Abstract/Intro 本身就应当 upfront 呈现 CF 代价。我接受 R2 的升级，同意这应当是 **must-fix**。\n\n不过有一个 nuance：CF=9.90% 的含义需要澄清。CF 是 grammar-first fallback 的**触发率**（semantic mask 与 grammar mask 冲突的比例），不是\"输出错误率\"。当 fallback 触发时，grammar layer 仍保证 JSON 结构合法性，只是跳过了该位置的 semantic 类型约束。因此 CF=9.90% 不等于 9.90% 的输出不可用，但确实意味着约 10% 的类型约束检查被绕过。作者应在 Abstract 中区分这一点，而非笼统地说 \"modest\"。\n\n**[AGREE with nuance] R2-W3: κ̄ 作为独立贡献定位过高**\n基本同意，但对严重性判断略有保留。\n\n同意的部分：\n- κ̄ = 1 − |σ(r)|/|E|² 确实只是约束表的归一化密度，数学上 trivial\n- 仅 2 个数据点（SciERC κ̄=0.333, DocRED κ̄=0.842）无法建立有意义的预测关系\n- R2 指出的 Mistral 异常（DR 降幅仅 76% vs Qwen/Llama 94–99%，同一 κ̄）有力地说明 κ̄ 不能独立预测效果\n\n保留的部分：\n- 论文 Contribution 2 的原文是 \"A descriptive metric, constraint tightness κ̄, that correlates schema restrictiveness with enforcement outcomes and provides deployment guidance\"（page 2）。作者用了 \"descriptive\" 和 \"correlates\"，没有声称 predictive power。这与 R2 说的\"独立贡献定位过高\"之间存在程度差异\n- 作为一个 deployment heuristic（高 κ̄ → 更需要 beam search 或 fine-tuning），即使只有 2 个数据点，方向性的指导仍然有价值\n\n我倾向于将此保留为 **should-fix**（降级 Contribution 2 的措辞，改为 \"we additionally introduce...\" 而非独立贡献条目）而非 must-fix。但 R2 的核心批评——将一个 trivial metric 列为三大贡献之一——我认同这影响了论文的定位可信度。\n\n---\n\n## Should-Fix\n\n**[AGREE] R2-W4: \"any autoregressive LM\" 过度声称**\n同意。Abstract 的 \"applicable to any autoregressive LM\" 与实际验证范围（7–8B 为主，70B 仅 preliminary）不匹配。我在初审中漏掉了这个具体措辞问题。补充：论文也未验证 (a) <7B 小模型（约束执行可能因能力不足导致更高 CF），(b) API-only 模型（如 GPT-4、Claude，无法直接操作 logits），(c) 非 Transformer 架构。建议改为 \"applicable to autoregressive LMs with logits access\"。\n\n**[AGREE] R2-W5: DocRED 零样本 DR 降幅讨论不足**\n同意。DocRED zero-shot DR 从 18.46% 降至 10.21%（Table 3, page 6），降幅约 45%，远低于 SciERC 的 94%。论文将此归因于 κ̄ 差异（Section 5.2: \"reflects higher tightness κ̄=0.842 vs 0.333\"），但正如 R2 所说，这只是 restate 了现象而非解释了原因。\n\n我在初审中通过 W4（DocRED 50-doc subset）间接涉及了这个问题，但 R2 更直接地指出了核心矛盾：10.21% 的残余 DR 与论文标题中 \"Type-Constrained\" 的承诺之间存在张力。补充一个具体证据：Appendix D（page 22, Table 9）显示 DocRED 的 GENERIC←→OtherScientificTerm 冲突占 63.3% 的 CF violations，这表明残余 DR 主要来自**实体类型歧义**（GENERIC catch-all type），不是约束执行本身的失败，而是 schema 设计的固有模糊性。论文应更明确地讨论这一区分。\n\n**[AGREE] R2-W6: WikiEvents 评估局限性**\n同意。R2 的观察补充了我的初审（W2, critical）中未涉及的细节：\n- Zero-shot entity F1 从 0 → 12–18%（Table 5, page 7）主要是格式修复（unconstrained 输出无法被解析为合法 entity，constrained 输出至少结构合法），而非语义提取能力的改善。这一点我漏掉了，R2 判断精准\n- Grammar-only 行（Table 5）确实缺少 F1 数值（仅报告 violation rates），使得无法判断 semantic layer 在 EE 上的 incremental F1 贡献\n\n不过我仍然认为 WikiEvents 评估的**统计效力问题**（n=20 test docs）是更根本的 concern，应为 critical 而非 R2 标注的 warning。\n\n**[AGREE] R2-W7: \"formally compiles\" 措辞**\n完全同意，与我的初审 W5 一致。不再赘述。\n\n---\n\n## Minor\n\n**[AGREE] R2-M1:** 确认 orphan bib entry schmidt2025grammar，与我的 M4 一致。\n\n**[AGREE] R2-M2:** 表格字体偏小，Table 1/3/4 信息密度高，但在 ACL 双栏排版中普遍存在，属于 cosmetic issue。\n\n**[AGREE] R2-M3:** S1/S2 命名确实不直观。\"S1 (joint extraction)\" vs \"S2 (two-pass pipeline)\" 的缩写需要在首次使用时更明确定义，且 \"Full (S1)\" 的嵌套命名增加了阅读障碍。\n\n**[AGREE] R2-M4:** 对称 relation 的处理（脚注 1, page 4）确实重要到值得在正文讨论，因为它直接影响 κ̄ 的计算和约束的 asymmetry 语义。\n\n**[AGREE] R2-M5:** 与我的 M4 一致。formattax2026（Lee et al., 2026）和 regino2025kgcurator 在 OpenAlex 未找到，可能是极新的 preprint 尚未被索引。不影响引用正确性但建议验证。\n\n---\n\n## Director 提出的具体问题回应\n\n### 1. 正文超页是否 must-fix？\n\n**是。** R2 正确。EMNLP 2026 via ARR 规则明确且严格。虽然机械修复容易（压缩 11 行），但格式违规的 desk reject 风险不可忽视。我将此从 minor 升级为 must-fix。\n\n### 2. CF 代价被低估？\"modest\" 描述 9.90% CF 是否误导？\n\n**同意 R2 判断。** \"modest\" 用于描述 9.90% CF 确实具有误导性。一个有用的参照：post-hoc filtering 在 DocRED 上丢弃 48% 的 triples（Appendix C, page 22）——OntoCoDec 的 CF 确实远低于 post-hoc 的代价，但用 \"modest\" 而非给出具体数字掩盖了这一事实。Abstract 应直接报告 representative CF 数值（如 \"with CF rates of 0–9.9% depending on schema complexity\"），让读者自行判断是否 \"modest\"。\n\n### 3. Excitement 2.5 vs 3.0 的分歧\n\nR2 给 Excitement 2.5（\"Potentially interesting\"），我给 3.0（\"Interesting\"）。分歧来源：\n\n**R2 更低的原因可能是：**\n- R2 更看重 practical novelty——双层架构虽然设计干净，但 grammar-constrained decoding（Level 1）是已有工作（XGrammar、Outlines），OntoCoDec 的 incremental contribution 是 semantic layer（Level 2），且这个 layer 的效果受限于 schema 复杂度（DocRED 45% vs SciERC 94% 降幅）\n- R2 给 Novelty 2.5/5 进一步印证了这一判断：认为方法论新意有限\n\n**我给 3.0 的原因：**\n- Decidability taxonomy（三级分类）本身是有价值的理论贡献，为社区提供了分析 IE 约束执行问题的框架，超越了具体系统的实现\n- 将 PL/formal language theory 的分析工具引入 IE 问题是一个有趣的 cross-pollination\n\n**我的修正判断：** 在看到 R2 的完整意见后，我认为 2.5 偏低——decidability taxonomy 的理论价值不应因为系统 novelty 有限而被完全折价。但我也承认 3.0 可能偏高——taxonomy 本身虽然 well-motivated，但三级分类相当直观（CF 可解/有状态可解/不可在线解），不是深刻的理论发现。**维持 3.0 不变。**\n\n### 4. Overall 3.0 vs 3.5 的核心差距\n\nR2 给 3.0（Findings），我给 3.5（Borderline Conference）。半分差距的核心原因：\n\n**R2 的 3.0 逻辑（我的理解）：**\nR2 识别出一个**系统性 overclaiming 模式**——\"modest\" CF、κ̄ 作为独立贡献、\"any autoregressive LM\"、\"formally compiles\"——并认为这些不是孤立的措辞问题，而是论文对自身贡献的定位整体偏高。当多个 claim 同时被高估时，论文的可信度遭受累积损害。加上 Excitement 2.5，3.0 是合理的。\n\n**我的 3.5 逻辑：**\n我更看重论文的**实质贡献**而非措辞问题。核心技术（decidability taxonomy + 双层约束执行）是 sound 的，实验覆盖面广（3 datasets × 4 models × 多配置），消融设计细致。措辞问题可以在 revision 中修正而不改变技术贡献。缺少 BoostCD/IterGen baseline 是最实质性的缺陷。\n\n**交叉回应后的修正判断：**\nR2 的 overclaiming pattern 论点在我重新审视后确实成立：不是单个 claim 的问题，而是 Abstract/Intro/Contributions 整体呈现了比实际支撑更强的 narrative。这在 ARR 审稿中会降低 reviewer 信任度。\n\n但我仍然认为 3.5 比 3.0 更准确：\n- 论文的 Limitations section（page 10）诚实地覆盖了多数局限性\n- 附录中的分析深度（33 页）远超平均水平\n- 核心技术 contribution 是 sound 的，overclaiming 是 presentation 问题不是 substance 问题\n- 修订后（限定 claims + 补充 baselines）有明确的升级路径\n\n**最终维持 Overall 3.5**，但承认 R2 的 3.0 也在合理范围内。如果 BoostCD 对比实验显示 OntoCoDec 的 incremental gain 很小，我会倾向于降至 3.0。\n",
    "reviewer_id": "1",
    "project": "schema_semantic_constrained_ie"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-20T18:48:15.449544+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_01fc90ae186a4ed432770f7601995139:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3716
}
```

</details>

---


### Assistant

_source line 888 · 2026-05-20T18:48:24.571358+00:00_

交叉回应已提交。总结：

- **W1 超页、W2 CF低估、W4-W7**：全部 [AGREE]，其中 W1/W2 我接受 R2 的升级（从我初审的 minor/should-fix 升至 must-fix）
- **W3 κ̄ 定位过高**：[AGREE with nuance]，同意 trivial metric 不应列为独立贡献，但保留 should-fix（非 critical）
- **评分分歧**：Excitement 维持 3.0 vs R2 的 2.5（decidability taxonomy 的理论价值不应完全折价）；Overall 维持 3.5 vs R2 的 3.0（overclaiming 是 presentation 问题而非 substance 问题，修订路径明确）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1"
}
```

</details>

---


## Round 24

## Round 24

92 recorded events


### User

_source line 889 · 2026-05-20T19:46:07.476444+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计与评估**。

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

### 1. 方法严谨性
- Proposition 1 及其 proof sketch 的正确性和严谨度
- 三级 decidability taxonomy（context-free / prefix-decidable with state / non-local）分类是否准确
- Grammar-first fallback 设计是否合理，"best-effort pair-based enforcement" 的保证边界
- Entity registry 的正确性保证（顺序依赖、动态构建）
- Continuation masking 的 tokenizer-agnostic 声称是否有充分支持
- Constraint tightness κ̄ 作为描述性指标的合理性（仅 2 个数据点 SciERC/DocRED）

### 2. 实验设计与评估
- 五路消融设计（SciERC Table 1）和四路消融（DocRED Table 2）是否充分证明 enabling dependency
- Fine-tuning composability 实验的统计显著性（bootstrap 10,000, paired）
- Cross-model validation（3 models × 2 datasets）的设计合理性
- WikiEvents EE 扩展的证据强度（20-doc test set 的局限性）
- Beam search 评估的完整性（DocRED zero-shot 仅 50-doc 子集）
- 70B 评估作为 "preliminary" 的定位是否充分
- 缺少哪些关键 baseline（特别是 BoostCD、GCD、IterGen 等同领域 constrained decoding 方法）
- 运行时开销评估的充分性
- 统计检验方法是否恰当

### 3. 格式检查
- 正文是否在 8 页以内
- 是否符合 double-blind 要求

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 890 · 2026-05-20T19:46:16.536053+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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

_source line 891 · 2026-05-20T19:46:16.586842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 892 · 2026-05-20T19:46:20.300434+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 review form criteria dimensions scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 review form criteria dimensions scoring"
  }
}
```

</details>

---


### Tool call

_source line 893 · 2026-05-20T19:46:21.054464+00:00_

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
  "session": "feishu:group:oc_01fc90ae186a4ed432770f7601995139:reviewer_1",
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
