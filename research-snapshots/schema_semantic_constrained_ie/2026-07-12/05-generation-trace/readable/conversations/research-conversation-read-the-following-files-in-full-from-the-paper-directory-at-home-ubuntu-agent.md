# Research conversation: Read the following files in full from the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/sc

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a14ef1cbba04e7ca5.jsonl`
- **Structured JSON:** [`29000721315dc08f3a86.json`](../../sessions/29/29000721315dc08f3a86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-22T10:45:48.826Z_

Read the following files in full from the paper directory at /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/ and return their complete text:

1. abstract.tex
2. section1_introduction_draft.tex
3. section5_scierc_draft.tex
4. section5_docred_draft.tex
5. section5_wikievents_draft.tex
6. section5_crossmodel_draft.tex
7. section3_violation_landscape.tex (violation landscape section)
8. section5_runtime.tex

I need the EXACT text of each file to verify numerical claims. Return verbatim content.

Search breadth: quick

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "d44f49bd-7d0c-4811-8f16-d884d688c9bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T10:45:49.795Z_

I'll read all the requested files from the paper directory for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d44f49bd-7d0c-4811-8f16-d884d688c9bd",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbd7d3f9-f093-4d9c-9345-857b1086f5eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T10:45:50.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X26RSm9MCCjzQJnaAidSWw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbd7d3f9-f093-4d9c-9345-857b1086f5eb",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1965fbf7-5ada-45bf-8c61-eda607464919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T10:45:50.361Z_

<details><summary>↩ Tool result · `toolu_01X26RSm9MCCjzQJnaAidSWw`</summary>

```text
1	\begin{abstract}
2	We present \textsc{OntoCoDec}, a framework that translates Information Extraction (IE) ontologies into composable token-level decoding constraints via a decidability-guided architecture: a \emph{grammar layer} (context-free) compiles ontology constraints into grammars ensuring JSON validity and vocabulary membership; a \emph{semantic layer} (prefix-decidable with state) interprets type constraints at runtime via stateful token masking over a dynamic entity registry, with grammar-first fallback when constraints conflict.
3	Without constraints, Large Language Model (LLM) based IE produces systematic domain/range (DR) violations that persist after fine-tuning, with rates characterized by \emph{constraint tightness} ($\bar{\kappa}$), a descriptive metric correlating schema restrictiveness with enforcement outcomes ($n{=}3$ schemas).
4	The two layers exhibit an empirical enabling dependency (Proposition~1): neither achieves this reduction alone.
5	% exp_ids: w5_lora_scierc_constrained_eval, w5_qwen_docred_lora_constrained_eval, w5_llama_lora_scierc_constrained_eval, w5_llama_docred_lora_constrained_eval
6	Composed with LoRA fine-tuning, \textsc{OntoCoDec} achieves deployment-grade type compliance: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $<$0.5\% true-positive loss); residual CF ($\leq$1.3\%) represents \emph{violation conversion}---ontologically invalid triples (DR) are replaced by individually valid but type-inconsistent ones---resolved by beam search on SciERC (\S\ref{sec:beam-results}).
7	Zero-shot evaluation serves as a diagnostic, revealing dataset- and calibration-dependent effectiveness (45--99\% DR reduction, total violation reduction 31\%; \S\ref{sec:experiments}) and establishing constraint tightness ($\bar{\kappa}$) as a predictive factor.
8	The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across five autoregressive LMs (7--70B; 70B zero-shot and LoRA in \S\ref{sec:70b-results}) with logits access and three tokenizer families (up to 96 relation types).
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1965fbf7-5ada-45bf-8c61-eda607464919",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "aa11dfa7-6198-4788-aa70-cd59114b70e3",
  "sourceToolAssistantUUID": "1965fbf7-5ada-45bf-8c61-eda607464919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T10:45:50.505Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E6afnFpLB1R3yvpc3H9VDD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa11dfa7-6198-4788-aa70-cd59114b70e3",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "108dc231-63b4-420f-9040-c85ae2661922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T10:45:50.513Z_

<details><summary>↩ Tool result · `toolu_01E6afnFpLB1R3yvpc3H9VDD`</summary>

```text
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
17	We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
18	A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with an \emph{empirical enabling dependency} between layers.
19	OntoCoDec compiles constraints automatically from IE ontologies, requires no constraint-specific training, and is applicable to autoregressive LMs with logits access; we validate on three English datasets (up to 96 relation types), five models (7--70B), and three tokenizer families (Llama, Qwen, Mistral).
20	LoRA + greedy S1 achieves deployment-grade compliance: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $+$10\% latency); beam ($k{=}4$) eliminates all violation types on SciERC (1.54$\times$ latency).
21	DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.3\% fine-tuned; \S\ref{sec:scierc-results}); zero-shot evaluation (7--70B) reveals DR drops 76--99\% for calibrated models, but total violations (DR+CF) decrease by $\sim$31\%, reflecting conversion that fine-tuning resolves (\S\ref{sec:cross-model}).
22	
23	We make a systematic engineering contribution with theoretical grounding:
24	\begin{enumerate}[leftmargin=*,itemsep=2pt]
25	    \item A two-layer constrained decoding framework: we formalize a well-known intuition that cross-field type constraints require runtime state beyond context-free expressiveness (Proposition~1), yielding pair-based sequential enforcement at each level (\S\ref{sec:decidability}). Constraints compile automatically from IE ontologies, validated on schemas of varying restrictiveness with up to 96 relation types.
26	    \item A comprehensive evaluation across 3 IE datasets, 5 models (7--70B), and 2 tasks: under fine-tuning, DR\,$\leq$\,0.09\% at R-F1 43--46\% with CF\,$\leq$\,1.3\%; zero-shot ablation reveals an enabling dependency where neither layer alone exceeds 24\% DR reduction (\S\ref{sec:scierc-results}); event extraction on WikiEvents validates applicability beyond RE (\S\ref{sec:wikievents}).
27	\end{enumerate}
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "108dc231-63b4-420f-9040-c85ae2661922",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "f0562bfa-42cc-4fbf-a38b-fdeb96da7c3f",
  "sourceToolAssistantUUID": "108dc231-63b4-420f-9040-c85ae2661922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T10:45:50.648Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XRhyBpDAonvcQd6N9PSaFg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0562bfa-42cc-4fbf-a38b-fdeb96da7c3f",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2d6373d-c650-4bab-9f6d-d87f0cbdb322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T10:45:50.654Z_

<details><summary>↩ Tool result · `toolu_01XRhyBpDAonvcQd6N9PSaFg`</summary>

```text
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
59	Tot.\ = DR + CF (total type-violation burden).
60	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
61	F1 $\times$100. Bootstrap: 10{,}000 iterations.
62	CF: same entity assigned conflicting types across triples.
63	S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
64	Grammar-only represents the ceiling of grammar-constrained decoding~\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}
65	\label{tab:scierc-ablation}
66	\end{table}
67	
68	% ──────────────────────────────────────────
69	%  (a) Core result
70	% ──────────────────────────────────────────
71	\paragraph{Zero-shot diagnostic.}
72	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
73	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
74	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
75	Full S1 reduces DR from 15.37\% to 0.93\% ($\downarrow$94\%) while R-F1 is unchanged (8.23\,$\to$\,8.36, $p{=}0.58$).
76	Per-relation DR drops to $\leq$2.82\%, reaching 0\% on 4/7 relations (Appendix~\ref{app:per-relation-landscape}).
77	Post-hoc filtering discards up to 48\% of predictions rather than correcting them (Appendix~\ref{app:posthoc-extended}).
78	Total type-violation burden (Tot.\,=\,DR+CF) decreases from 15.45\% to 10.83\% ($\downarrow$30\%), reflecting \emph{violation conversion}: DR enforcement replaces ontologically invalid triples with individually valid but type-inconsistent ones (CF 0.08\%\,$\to$\,9.90\%); under fine-tuning, Tot.\ drops to 1.18\% with CF\,$\leq$\,1.3\% (Table~\ref{tab:composability}).
79	
80	% ──────────────────────────────────────────
81	%  (b) Grammar layer
82	% ──────────────────────────────────────────
83	\paragraph{Layer contributions.}
84	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
85	Grammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\%, the ceiling of grammar-based decoding~\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\%), so CF originates from the semantic layer.
86	Semantic-only reduces DR by only 24\% and cannot eliminate RV or ET; this is the \emph{empirical enabling dependency}: adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).
87	
88	
89	% ──────────────────────────────────────────
90	%  (d) S1 vs S2
91	% ──────────────────────────────────────────
92	\paragraph{S1 vs.\ S2.}
93	S2 achieves comparable DR (0.97\%) but lower R-F1 and CF; we adopt S1.
94	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
95	
96	% ──────────────────────────────────────────
97	%  (e) Composability with Fine-Tuning
98	%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
99	%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,
100	%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,
101	%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval
102	% ──────────────────────────────────────────
103	\paragraph{Composability with fine-tuning.}
104	\label{sec:composability}
105	% exp_ids: bootstrap_ci_ft_composability.json
106	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.09\% with no significant $\Delta$R-F1 after Bonferroni correction (min.\ $p{=}0.014$; 95\% CIs $\subseteq [-0.76, {+}0.22]$\,pp; removed triples are 97.6--100\% false positives).
107	CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) with LoRA eliminates all four violation types on SciERC (R-F1 43.60, 46.18; \S\ref{sec:beam-results}).
108	
109	\begin{table}[t]
110	\centering
111	\small
112	\setlength{\tabcolsep}{3pt}
113	\resizebox{\columnwidth}{!}{%
114	\begin{tabular}{@{}lll rrrr r@{}}
115	\toprule
116	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
117	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
118	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
119	  & \textbf{$\Delta$DR} \\
120	\midrule
121	\multirow{4}{*}{Qwen3-8B}
122	  & \multirow{2}{*}{SciERC}
123	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
124	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
125	\cmidrule(l){2-8}
126	  & \multirow{2}{*}{DocRED}
127	    & Unconstr.\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\
128	  & & Full S1    & \textbf{0.00} & 0.22 & 40.79 & 81.87 & $\downarrow$100\% \\
129	\midrule
130	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
131	  & \multirow{2}{*}{SciERC}
132	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
133	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
134	\cmidrule(l){2-8}
135	  & \multirow{2}{*}{DocRED}
136	    & Unconstr.\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\
137	  & & Full S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\downarrow$100\% \\
138	\bottomrule
139	\end{tabular}}%
140	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
141	F1\,$\times$100. No $\Delta$R-F1 is significant (Bonferroni-corrected; details in text); all DR reductions are ($p{<}0.001$).
142	E-F1 includes parse-failure documents (Qwen PF: 7--8\%; Llama PF: 2--3\%).}
143	\label{tab:composability}
144	\end{table}
145	
146	% ──────────────────────────────────────────
147	%  (f) Downstream impact of DR elimination
148	%  exp_ids: task_e_lucky_violation_analysis
149	% ──────────────────────────────────────────
150	\paragraph{Downstream impact.}
151	\label{sec:downstream-impact}
152	Among constraint-removed triples, only 0.49\% match gold labels on average (``lucky violations''), confirming $<$0.5\% recall cost; on Llama SciERC all five are recovered via legal type paths (zero churn; Appendix~\ref{app:lucky-violations}).
153	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2d6373d-c650-4bab-9f6d-d87f0cbdb322",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "40a36bed-70ef-4808-bc4a-607d2c407453",
  "sourceToolAssistantUUID": "a2d6373d-c650-4bab-9f6d-d87f0cbdb322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T10:45:50.851Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ADKxdSFH2joPRZoZ3gDEgR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40a36bed-70ef-4808-bc4a-607d2c407453",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7288d91a-ec46-47e0-ae08-05c87dfca797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T10:45:50.856Z_

<details><summary>↩ Tool result · `toolu_01ADKxdSFH2joPRZoZ3gDEgR`</summary>

```text
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
56	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see text).}
57	\label{tab:docred-ablation}
58	\end{table}
59	
60	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
61	\paragraph{Zero-shot diagnostic.}
62	Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET ($\to$\,0\%), and eliminates RV (29.66\%\,$\to$\,0.03\%).\footnote{Residual 0.03\% RV traces to a rare XGrammar automaton edge case (chimeric subword tokens across enum entries); reported upstream.}
63	R-F1 improves from 7.74 to 8.23 ($+$0.50\,pp; $p < 0.001$), attributable to elimination of 5{,}189 OOV relation predictions.
64	CF increases from 0.10\% to 2.57\%, consistent with the CF$\leftrightarrow$DR trade-off (\S\ref{sec:discussion}).
65	Residual zero-shot DR (10.21\%) traces to grammar-first fallback under tight constraints ($\bar{\kappa}{=}0.842$; \S\ref{sec:greedy-limitation}); causal tracing confirms all residual DR occurs at fallback positions (Appendix~\ref{app:causal-tracing}).
66	
67	% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1
68	\paragraph{Layer contributions.}
69	Grammar-only eliminates RV and ET but \emph{increases} DR to 26.17\%: vocabulary restriction makes OOV outputs evaluable, exposing latent type incompatibilities.
70	Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same empirical enabling dependency observed on SciERC.
71	Residual DR (10.21\% vs.\ 0.93\% on SciERC) reflects high $\bar{\kappa}$ (0.842) and \textsc{Generic}$\leftrightarrow$X ambiguity; fine-tuning narrows DR to $\leq$\,0.09\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7288d91a-ec46-47e0-ae08-05c87dfca797",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "42b1a087-ec77-4c7e-9daa-4f538308c78c",
  "sourceToolAssistantUUID": "7288d91a-ec46-47e0-ae08-05c87dfca797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T10:45:51.273Z_

<details open><summary>🔧 Tool call — Read · `toolu_019YkVBsQgASz2ESKMBfBdgq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42b1a087-ec77-4c7e-9daa-4f538308c78c",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ffa20556-6103-4435-87fc-6cd7a0d03d40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T10:45:51.279Z_

<details><summary>↩ Tool result · `toolu_019YkVBsQgASz2ESKMBfBdgq`</summary>

```text
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
42	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
43	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
44	  & Full S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{WikiEvents EE results. Zero-shot rows (n$=$246): full WikiEvents corpus; fine-tuning (\S\ref{sec:wikievents}, n$=$20): standard 194/20/20 split~\cite{li2021document}.
48	Violation rates over parsed documents.
49	\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).
50	F1 $\times$ 100.}
51	\label{tab:wikievents}
52	\end{table}
53	
54	\paragraph{Results.}
55	Unconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\%; Table~\ref{tab:wikievents}), with entity F1\,=\,0 because the parser cannot process off-schema output.
56	Full S1 eliminates EV and RoV across all models, which validates the tokenizer-agnostic design across byte-level BPE and SentencePiece.
57	Grammar-only eliminates EV but leaves RoV at 64--77\% and surfaces latent AC (8--14\%), consistent with DocRED's pattern (\S\ref{sec:docred-results}); full S1 drives RoV to 0\%.
58	Residual AC (1.3--3.8\%) traces to semantically similar types (e.g., SID vs.\ SEN).
59	CF rises to 15--21\%, exceeding RE levels (10--12\%) because EE's multi-argument structures increase entity reuse across slots.
60	Post-hoc filtering is impractical ($<$0.5\% arguments retained).
61	Unlike RE, EE shows measurable F1 gains: entity F1 0\%\,$\to$\,12--18\%, trigger F1 $+$1.5--1.8\,pp.
62	
63	% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5
64	\paragraph{Composability with fine-tuning.}
65	On the full official test split (20 documents; 194/20/20~\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\%\,$\to$\,0\%, Llama 8.8\%\,$\to$\,0\%) and reduces AC to $\leq$0.8\%, with argument F1 within $\pm$1.1\,pp; trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20.
66	CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences.
67	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffa20556-6103-4435-87fc-6cd7a0d03d40",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "d6cb656f-7719-4c27-a631-96d78e713595",
  "sourceToolAssistantUUID": "ffa20556-6103-4435-87fc-6cd7a0d03d40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T10:45:51.485Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DcCfSMfeyXXg7Mu82qvcch`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6cb656f-7719-4c27-a631-96d78e713595",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99d5239a-92d2-44a0-8100-16905f17fbfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T10:45:51.489Z_

<details><summary>↩ Tool result · `toolu_01DcCfSMfeyXXg7Mu82qvcch`</summary>

```text
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
49	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
50	F1 $\times$100.}
51	\label{tab:cross-model}
52	\end{table}
53	
54	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
55	\paragraph{Results.}
56	RV and ET reach $\leq$0.03\% for all models on both datasets.
57	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
58	CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%; poor entity typing limits DR reduction to 42\%); fine-tuning resolves both (\S\ref{sec:composability}).
59	
60	\paragraph{Post-hoc filtering comparison.}
61	Post-hoc filtering achieves DR${=}$0\% but with 15--74\% rejection rates (DocRED Qwen: 48\% discarded); under fine-tuning, both achieve comparable F1 (Appendix~\ref{app:posthoc-extended}).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99d5239a-92d2-44a0-8100-16905f17fbfa",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "e73ba1f5-ff9c-4714-bef6-de23e6c882db",
  "sourceToolAssistantUUID": "99d5239a-92d2-44a0-8100-16905f17fbfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T10:45:51.696Z_

<details open><summary>🔧 Tool call — Read · `toolu_016sFFVxBmJbRwUwUVvwGgTC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e73ba1f5-ff9c-4714-bef6-de23e6c882db",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8a0b3ef8-3afb-4ea1-bddc-94d8b3d3c130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T10:45:51.700Z_

<details><summary>↩ Tool result · `toolu_016sFFVxBmJbRwUwUVvwGgTC`</summary>

```text
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
17	We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
18	Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a0b3ef8-3afb-4ea1-bddc-94d8b3d3c130",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "4ce010b0-187f-46be-9247-60a76d703a30",
  "sourceToolAssistantUUID": "8a0b3ef8-3afb-4ea1-bddc-94d8b3d3c130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T10:45:51.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_014FYy1vKn8QdSpCBQFAcUWT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ce010b0-187f-46be-9247-60a76d703a30",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMcAbfZbmm9o4xDxqX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4bde2f58-4cd7-4e9f-9289-dbf47da6270a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Lo26N9rv9QFN6BtF84YoMU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 15106,
      "output_tokens": 671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 671,
          "cache_read_input_tokens": 15106,
          "cache_creation_input_tokens": 595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 595,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T10:45:51.893Z_

<details><summary>↩ Tool result · `toolu_014FYy1vKn8QdSpCBQFAcUWT`</summary>

```text
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
23	Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}: RV/ET$\to$0\% but only 3\% DR reduction vs.\ Full S1's 94\%.
24	Without JSON structural enforcement, trie-only vocabulary constraints yield R-F1 19.95--41.16 on SciERC LoRA (vs.\ OntoCoDec's 43.77--45.47) with 9.1--50.8\% parse failure (Appendix~\ref{app:trie-baseline}); the model-dependent disparity confirms grammar enforcement provides a model-independent structural guarantee.
25	BoostCD's~\cite{boostcd2025} boosting is complementary and potentially integrable with OntoCoDec.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bde2f58-4cd7-4e9f-9289-dbf47da6270a",
  "isSidechain": true,
  "promptId": "ae940423-81f3-4577-b8d9-e96197e13299",
  "agentId": "a14ef1cbba04e7ca5",
  "type": "user",
  "uuid": "4d0c008d-1c8a-4c48-ab70-ca63af9b16de",
  "sourceToolAssistantUUID": "4bde2f58-4cd7-4e9f-9289-dbf47da6270a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T10:47:39.387Z_

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
The framework is validated on RE (SciERC, DocRED) with preliminary event extraction results on WikiEvents, across five autoregressive LMs (7--70B; 70B zero-shot and LoRA in \S\ref{sec:70b-results}) with logits access and three tokenizer families (up to 96 relation types).
\end{abstract}
```

---

## 2. section1_introduction_draft.tex

```
% Section 1: Introduction (compressed, 669→~550 words)

\section{Introduction}
\label{sec:introduction}

Large language models are increasingly used for information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity necessarily carries a type consistent with the ontology's domain/range constraints for $r$.
We call such outputs \emph{domain/range violations}: structurally valid triples that are ontologically invalid.
Violations persist across the capability spectrum: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred} under zero-shot decoding, and 0.5--2\% even after LoRA fine-tuning; rates correlate with schema restrictiveness (few valid type pairs per relation) rather than ontology or model scale.
At deployment-grade quality (R-F1 40--46\%), even 1--2\% residual violations compound across thousands of documents into systematic knowledge graph corruption, making reliable constraint enforcement necessary.

Existing approaches leave a fundamental gap.
Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable (violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp).
Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} ensures syntactic well-formedness but cannot encode cross-field semantic constraints.
Post-hoc filtering improves precision but discards up to 48\% of predictions including true positives; at high rejection rates (e.g., Mistral DocRED 73.7\%), it becomes impractical.
Training-based approaches~\cite{sainz2024gollie,lu2022uie} internalize schema knowledge but provide only soft guidance without runtime enforcement; no method provides both semantic awareness and hard constraint enforcement.

We propose \textbf{OntoCoDec}, a framework that translates IE ontologies into composable layers of decoding-time constraints.
A decidability analysis of IE type constraints (\S\ref{sec:decidability}) yields a two-layer architecture: the \emph{grammar layer} compiles ontology constraints into context-free grammars (JSON structure, vocabulary membership) via XGrammar; the \emph{semantic layer} interprets type constraints at runtime via dynamic logit masking over an entity registry, with an \emph{empirical enabling dependency} between layers.
OntoCoDec compiles constraints automatically from IE ontologies, requires no constraint-specific training, and is applicable to autoregressive LMs with logits access; we validate on three English datasets (up to 96 relation types), five models (7--70B), and three tokenizer families (Llama, Qwen, Mistral).
LoRA + greedy S1 achieves deployment-grade compliance: DR\,$\leq$\,0.09\% at R-F1 43--46\% ($\pm$0.8\,pp, $+$10\% latency); beam ($k{=}4$) eliminates all violation types on SciERC (1.54$\times$ latency).
DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.3\% fine-tuned; \S\ref{sec:scierc-results}); zero-shot evaluation (7--70B) reveals DR drops 76--99\% for calibrated models, but total violations (DR+CF) decrease by $\sim$31\%, reflecting conversion that fine-tuning resolves (\S\ref{sec:cross-model}).

We make a systematic engineering contribution with theoretical grounding:
\begin{enumerate}[leftmargin=*,itemsep=2pt]
    \item A two-layer constrained decoding framework: we formalize a well-known intuition that cross-field type constraints require runtime state beyond context-free expressiveness (Proposition~1), yielding pair-based sequential enforcement at each level (\S\ref{sec:decidability}). Constraints compile automatically from IE ontologies, validated on schemas of varying restrictiveness with up to 96 relation types.
    \item A comprehensive evaluation across 3 IE datasets, 5 models (7--70B), and 2 tasks: under fine-tuning, DR\,$\leq$\,0.09\% at R-F1 43--46\% with CF\,$\leq$\,1.3\%; zero-shot ablation reveals an enabling dependency where neither layer alone exceeds 24\% DR reduction (\S\ref{sec:scierc-results}); event extraction on WikiEvents validates applicability beyond RE (\S\ref{sec:wikievents}).
\end{enumerate}
```

---

## 3. section5_scierc_draft.tex

```
% Section 5 — SciERC Results (Draft)
% Data source: Phase 2 SciERC registry experiments
% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
% All numbers verified against registry 2026-05-14.

\subsection{Ablation and Composability with Fine-Tuning}
\label{sec:scierc-results}

Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.

% ──────────────────────────────────────────
%  Table: SciERC five-way ablation
% ──────────────────────────────────────────
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3.6pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}l rrrrrr rr@{}}
\toprule
& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
& \multicolumn{2}{c}{\textbf{F1}} \\
\cmidrule(lr){2-7} \cmidrule(l){8-9}
\textbf{Mode}
  & DR\,$\downarrow$ & $\Delta$DR
  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
\midrule
Unconstrained
  & 15.37 & ---
  & 1.39  & 0.40
  & 0.08  & 15.45
  & 8.23  & 31.01 \\
Grammar
  & 14.84 & $\downarrow$3\%
  & \textbf{0} & \textbf{0}
  & 0.08  & 14.92
  & 8.23  & 30.98 \\
Semantic
  & 11.65 & $\downarrow$24\%
  & 1.51  & 0.40
  & 2.71  & 14.36
  & 8.15  & 31.01 \\
Full (S1)
  & \textbf{0.93} & $\downarrow$\textbf{94\%}
  & \textbf{0} & \textbf{0}
  & 9.90  & \textbf{10.83}
  & \textbf{8.36} & 30.98 \\
Full (S2)
  & 0.97  & $\downarrow$94\%
  & \textbf{0} & \textbf{0}
  & 8.03  & \textbf{9.00}
  & 8.03  & \textbf{31.90} \\
\bottomrule
\end{tabular}}%
\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
$\Delta$DR: relative change vs.\ unconstrained.
Tot.\ = DR + CF (total type-violation burden).
Best per column in \textbf{bold} (CF excluded; Tot.\ included).
F1 $\times$100. Bootstrap: 10{,}000 iterations.
CF: same entity assigned conflicting types across triples.
S1 = single-pass (\S\ref{sec:strategies}), S2 = two-pass (\S\ref{sec:s2}).
Grammar-only represents the ceiling of grammar-constrained decoding~\cite{geng2023gcd}: vocabulary membership is enforced but cross-field semantic constraints are not.}
\label{tab:scierc-ablation}
\end{table}

% ──────────────────────────────────────────
%  (a) Core result
% ──────────────────────────────────────────
\paragraph{Zero-shot diagnostic.}
% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
Full S1 reduces DR from 15.37\% to 0.93\% ($\downarrow$94\%) while R-F1 is unchanged (8.23\,$\to$\,8.36, $p{=}0.58$).
Per-relation DR drops to $\leq$2.82\%, reaching 0\% on 4/7 relations (Appendix~\ref{app:per-relation-landscape}).
Post-hoc filtering discards up to 48\% of predictions rather than correcting them (Appendix~\ref{app:posthoc-extended}).
Total type-violation burden (Tot.\,=\,DR+CF) decreases from 15.45\% to 10.83\% ($\downarrow$30\%), reflecting \emph{violation conversion}: DR enforcement replaces ontologically invalid triples with individually valid but type-inconsistent ones (CF 0.08\%\,$\to$\,9.90\%); under fine-tuning, Tot.\ drops to 1.18\% with CF\,$\leq$\,1.3\% (Table~\ref{tab:composability}).

% ──────────────────────────────────────────
%  (b) Grammar layer
% ──────────────────────────────────────────
\paragraph{Layer contributions.}
% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
Grammar-only eliminates RV and ET with no F1 impact while DR remains at 14.84\%, the ceiling of grammar-based decoding~\cite{geng2023gcd}; grammar-only CF is near-zero (0.08\%), so CF originates from the semantic layer.
Semantic-only reduces DR by only 24\% and cannot eliminate RV or ET; this is the \emph{empirical enabling dependency}: adding the grammar layer yields a further 92\% reduction (11.65\%\,$\to$\,0.93\%).


% ──────────────────────────────────────────
%  (d) S1 vs S2
% ──────────────────────────────────────────
\paragraph{S1 vs.\ S2.}
S2 achieves comparable DR (0.97\%) but lower R-F1 and CF; we adopt S1.
% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644

% ──────────────────────────────────────────
%  (e) Composability with Fine-Tuning
%  exp_ids: w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
%           w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval,
%           w5_qwen_docred_lora_unconstrained_eval, w5_qwen_docred_lora_constrained_eval,
%           w5_llama_docred_lora_unconstrained_eval, w5_llama_docred_lora_constrained_eval
% ──────────────────────────────────────────
\paragraph{Composability with fine-tuning.}
\label{sec:composability}
% exp_ids: bootstrap_ci_ft_composability.json
Fine-tuning alone reduces DR to 1--2\% but leaves residual violations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.09\% with no significant $\Delta$R-F1 after Bonferroni correction (min.\ $p{=}0.014$; 95\% CIs $\subseteq [-0.76, {+}0.22]$\,pp; removed triples are 97.6--100\% false positives).
CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) with LoRA eliminates all four violation types on SciERC (R-F1 43.60, 46.18; \S\ref{sec:beam-results}).

\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lll rrrr r@{}}
\toprule
\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
  & \textbf{DR\,$\downarrow$} & \textbf{CF}
  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
  & \textbf{$\Delta$DR} \\
\midrule
\multirow{4}{*}{Qwen3-8B}
  & \multirow{2}{*}{SciERC}
    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
\cmidrule(l){2-8}
  & \multirow{2}{*}{DocRED}
    & Unconstr.\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\
  & & Full S1    & \textbf{0.00} & 0.22 & 40.79 & 81.87 & $\downarrow$100\% \\
\midrule
\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
  & \multirow{2}{*}{SciERC}
    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
\cmidrule(l){2-8}
  & \multirow{2}{*}{DocRED}
    & Unconstr.\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\
  & & Full S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\downarrow$100\% \\
\bottomrule
\end{tabular}}%
\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
F1\,$\times$100. No $\Delta$R-F1 is significant (Bonferroni-corrected; details in text); all DR reductions are ($p{<}0.001$).
E-F1 includes parse-failure documents (Qwen PF: 7--8\%; Llama PF: 2--3\%).}
\label{tab:composability}
\end{table}

% ──────────────────────────────────────────
%  (f) Downstream impact of DR elimination
%  exp_ids: task_e_lucky_violation_analysis
% ──────────────────────────────────────────
\paragraph{Downstream impact.}
\label{sec:downstream-impact}
Among constraint-removed triples, only 0.49\% match gold labels on average (``lucky violations''), confirming $<$0.5\% recall cost; on Llama SciERC all five are recovered via legal type paths (zero churn; Appendix~\ref{app:lucky-violations}).
```

---

## 4. section5_docred_draft.tex

```
% Section 5 — DocRED Results (compressed, 1450→~600 words)
% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
%          phase2_docred_semantic_only, phase2_docred_full_s1
% All numbers verified against registry 2026-05-14.

\subsection{Cross-Dataset Validation on DocRED}
\label{sec:docred-results}

Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED (96 Wikidata relation types, 14$\times$ SciERC; Qwen3-8B, zero-shot, 998 documents).

% ──────────────────────────────────────────
%  Table: DocRED four-way ablation
% ──────────────────────────────────────────
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3.6pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}l rrrrrr rr@{}}
\toprule
& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
& \multicolumn{2}{c}{\textbf{F1}} \\
\cmidrule(lr){2-7} \cmidrule(l){8-9}
\textbf{Mode}
  & DR\,$\downarrow$ & $\Delta$DR
  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
\midrule
Unconstrained
  & 18.46 & ---
  & 29.66 & 2.48
  & 0.10  & 18.56
  & 7.74  & 58.15 \\
Grammar
  & 26.17 & $\uparrow$42\%
  & \textbf{0.03} & \textbf{0}
  & 0.07  & 26.24
  & \textbf{8.31}  & \textbf{59.38} \\
Semantic
  & 13.84 & $\downarrow$25\%
  & 29.87 & 4.22
  & 1.05  & 14.89
  & 7.70  & 57.81 \\
Full (S1)
  & \textbf{10.21} & $\downarrow$\textbf{45\%}
  & \textbf{0.03} & \textbf{0}
  & 2.57  & \textbf{12.78}
  & 8.23  & 59.37 \\
\bottomrule
\end{tabular}}%
\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
$\Delta$DR: relative change vs.\ unconstrained.
Tot.\ = DR + CF (total type-violation burden).
Best per column in \textbf{bold} (CF excluded; Tot.\ included).
F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).
Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see text).}
\label{tab:docred-ablation}
\end{table}

% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
\paragraph{Zero-shot diagnostic.}
Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET ($\to$\,0\%), and eliminates RV (29.66\%\,$\to$\,0.03\%).\footnote{Residual 0.03\% RV traces to a rare XGrammar automaton edge case (chimeric subword tokens across enum entries); reported upstream.}
R-F1 improves from 7.74 to 8.23 ($+$0.50\,pp; $p < 0.001$), attributable to elimination of 5{,}189 OOV relation predictions.
CF increases from 0.10\% to 2.57\%, consistent with the CF$\leftrightarrow$DR trade-off (\S\ref{sec:discussion}).
Residual zero-shot DR (10.21\%) traces to grammar-first fallback under tight constraints ($\bar{\kappa}{=}0.842$; \S\ref{sec:greedy-limitation}); causal tracing confirms all residual DR occurs at fallback positions (Appendix~\ref{app:causal-tracing}).

% exp_ids: phase2_docred_grammar_only, phase2_docred_semantic_only, phase2_docred_full_s1
\paragraph{Layer contributions.}
Grammar-only eliminates RV and ET but \emph{increases} DR to 26.17\%: vocabulary restriction makes OOV outputs evaluable, exposing latent type incompatibilities.
Semantic-only reduces DR by 25\% but cannot eliminate RV or ET, the same empirical enabling dependency observed on SciERC.
Residual DR (10.21\% vs.\ 0.93\% on SciERC) reflects high $\bar{\kappa}$ (0.842) and \textsc{Generic}$\leftrightarrow$X ambiguity; fine-tuning narrows DR to $\leq$\,0.09\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
```

---

## 5. section5_wikievents_draft.tex

```
% Section 5 — Event Extraction on WikiEvents (compact, inline)
% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
% v3 final data confirmed by Director 2026-05-18.

\subsection{Extension to Event Extraction}
\label{sec:wikievents}

We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).

% ──────────────────────────────────────────
%  Table: WikiEvents three-model comparison (v3 final)
%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
% ──────────────────────────────────────────
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{2.8pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}ll rrrr rr@{}}
\toprule
& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
& \multicolumn{2}{c}{\textbf{F1}} \\
\cmidrule(lr){3-6} \cmidrule(l){7-8}
\textbf{Model} & \textbf{Mode}
  & EV\,$\downarrow$ & RoV\,$\downarrow$ & AC & CF
  & Trig.\,$\uparrow$ & Ent.\,$\uparrow$ \\
\midrule
\multirow{3}{*}{Qwen3-8B}
  & Unconstr.\ & 24.0 & 74.9 & 0.3 & 0 & 11.8 & 0 \\
  & Grammar    & \textbf{0} & 76.1 & 8.2 & --- & --- & --- \\
  & Full S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
\midrule
\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
  & Full S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
\midrule
\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
  & Full S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
\bottomrule
\end{tabular}}%
\caption{WikiEvents EE results. Zero-shot rows (n$=$246): full WikiEvents corpus; fine-tuning (\S\ref{sec:wikievents}, n$=$20): standard 194/20/20 split~\cite{li2021document}.
Violation rates over parsed documents.
\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).
F1 $\times$ 100.}
\label{tab:wikievents}
\end{table}

\paragraph{Results.}
Unconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\%; Table~\ref{tab:wikievents}), with entity F1\,=\,0 because the parser cannot process off-schema output.
Full S1 eliminates EV and RoV across all models, which validates the tokenizer-agnostic design across byte-level BPE and SentencePiece.
Grammar-only eliminates EV but leaves RoV at 64--77\% and surfaces latent AC (8--14\%), consistent with DocRED's pattern (\S\ref{sec:docred-results}); full S1 drives RoV to 0\%.
Residual AC (1.3--3.8\%) traces to semantically similar types (e.g., SID vs.\ SEN).
CF rises to 15--21\%, exceeding RE levels (10--12\%) because EE's multi-argument structures increase entity reuse across slots.
Post-hoc filtering is impractical ($<$0.5\% arguments retained).
Unlike RE, EE shows measurable F1 gains: entity F1 0\%\,$\to$\,12--18\%, trigger F1 $+$1.5--1.8\,pp.

% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5
\paragraph{Composability with fine-tuning.}
On the full official test split (20 documents; 194/20/20~\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\%\,$\to$\,0\%, Llama 8.8\%\,$\to$\,0\%) and reduces AC to $\leq$0.8\%, with argument F1 within $\pm$1.1\,pp; trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20.
CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences.
```

---

## 6. section5_crossmodel_draft.tex

```
% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
%          phase2_docred_unconstrained, phase2_docred_full_s1,
%          llama_scierc_unconstrained, llama_scierc_full_s1,
%          llama_docred_unconstrained, llama_docred_full_s1

\subsection{Cross-Model Validation}
\label{sec:cross-model}

Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.

\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3.4pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}ll rrrr r@{}}
\toprule
& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
& \textbf{R-F1} \\
\cmidrule(lr){3-6} \cmidrule(l){7-7}
\textbf{Dataset} & \textbf{Model}
  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
  & $\uparrow$ \\
\midrule
\multirow{6}{*}{SciERC}
  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
  \cmidrule(l){2-7}
  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
  \cmidrule(l){2-7}
  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
\midrule
\multirow{6}{*}{DocRED}
  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
  \cmidrule(l){2-7}
  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
  \cmidrule(l){2-7}
  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
\bottomrule
\end{tabular}}%
\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
F1 $\times$100.}
\label{tab:cross-model}
\end{table}

% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
\paragraph{Results.}
RV and ET reach $\leq$0.03\% for all models on both datasets.
DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%; \S\ref{sec:discussion}) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%; poor entity typing limits DR reduction to 42\%); fine-tuning resolves both (\S\ref{sec:composability}).

\paragraph{Post-hoc filtering comparison.}
Post-hoc filtering achieves DR${=}$0\% but with 15--74\% rejection rates (DocRED Qwen: 48\% discarded); under fine-tuning, both achieve comparable F1 (Appendix~\ref{app:posthoc-extended}).
```

---

## 7. section3_violation_landscape.tex

```
% §5 Setup (compressed from Violation Landscape)
% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema

\label{sec:violation_landscape}

We evaluate OntoCoDec in two deployment configurations: LoRA + greedy S1 (\S\ref{sec:composability}), near-eliminating DR (DR\,$\leq$\,0.09\%) with minimal overhead; and LoRA + beam S1 (\S\ref{sec:beam-results}), achieving zero total violations on SciERC under favorable conditions (1.54$\times$ latency).
Zero-shot evaluation (\S\ref{sec:scierc-results}--\S\ref{sec:cross-model}) serves as a diagnostic probe to isolate constraint effects; R-F1 2--8 reflects absent task-specific training, not method failure.
The deployment-relevant evaluation is the fine-tuned setting (R-F1 40--46\%), where constraints compose with parameter optimization without degrading performance.

\paragraph{Setup.}
We evaluate on SciERC~\cite{luan2018scierc} (551 test sentences, 7 relations, $\bar{\kappa}{=}0.333$) and DocRED~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test annotations are not publicly available; we evaluate on the development set.} 96 relations, $\bar{\kappa}{=}0.842$).
RE type constraints are extracted automatically from observed type pairs in training data (neither dataset provides a formal ontology); EE constraints on WikiEvents (\S\ref{sec:wikievents}) are derived from the KAIROS ontology.
All constraints are defined from schema-level supervision, independently of the evaluation split.
The framework handles both sources without modification.
Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in \S\ref{sec:cross-model}, composability with fine-tuning in \S\ref{sec:composability}.
We measure four violation categories: \textbf{DR} (domain/range type pair $\notin \sigma(r)$), \textbf{RV} (relation $\notin \mathcal{R}$), \textbf{ET} (entity type $\notin \mathcal{E}$), and \textbf{CF} (same entity assigned conflicting types across triples).
Baseline DR violations are 15.37\% (SciERC) and 18.46\% (DocRED), comparable rates associated with constraint tightness rather than ontology scale (\S\ref{sec:introduction}); schema-informed prompting reduces DR by 62\% on SciERC but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
```

---

## 8. section5_runtime.tex

```
% Runtime overhead (inline paragraph, no subsection header to save space)

\paragraph{Runtime overhead.}
\label{sec:runtime}
S1 overhead is $+$13.1\% on SciERC, lower on DocRED due to amortization over longer sequences; under LoRA, $+$10.0\% with 37\% lower absolute latency.
Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).

\paragraph{Beam search compatibility.}
\label{sec:beam-results}
With LoRA, beam search ($k{=}4$)~\cite{anderson2017guided} eliminates all four violation types on SciERC (R-F1 44--46); zero-shot beam achieves DR${=}$0\% on both datasets (CF response is model-dependent; Appendix~\ref{app:beam-search}).
Total latency: 1.54$\times$ (beam 1.32$\times$ $+$ constraint 1.17$\times$; Table~\ref{tab:beam-latency}).

% exp_ids: r16_70b_scierc_zs_s1, r16_70b_docred_zs_s1, 70b_lora_scierc, 70b_lora_docred_200
\paragraph{70B evaluation.}
\label{sec:70b-results}
On Llama-3.3-70B-Instruct (AWQ INT4), zero-shot S1 eliminates DR on both datasets: SciERC 6.41\%\,$\to$\,0\% (R-F1 11.24), DocRED 14.98\%\,$\to$\,0\% (R-F1 13.05); CF rises to 3.50--7.01\%, comparable to 8B zero-shot CF.
% exp_ids: eval_70b_lora_scierc_s1_constrained, eval_70b_lora_docred_200_s1_constrained
LoRA fine-tuning confirms scale-independent composability: SciERC DR 1.50\%\,$\to$\,0\% (R-F1 44.53, $-$0.20\,pp); DocRED (200-document subset; Appendix~\ref{app:power-analysis}) DR 0.22\%\,$\to$\,0\% (R-F1 43.95, $+$0.15\,pp); CF drops from 3.50\% (zero-shot) to 0.18--1.33\% (LoRA), consistent with the 8B pattern (9.90\%\,$\to$\,1.18\%; \S\ref{sec:composability}).

% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
\paragraph{Comparison with grammar-constrained approaches.}
\label{sec:constrained-baselines}
Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}: RV/ET$\to$0\% but only 3\% DR reduction vs.\ Full S1's 94\%.
Without JSON structural enforcement, trie-only vocabulary constraints yield R-F1 19.95--41.16 on SciERC LoRA (vs.\ OntoCoDec's 43.77--45.47) with 9.1--50.8\% parse failure (Appendix~\ref{app:trie-baseline}); the model-dependent disparity confirms grammar enforcement provides a model-independent structural guarantee.
BoostCD's~\cite{boostcd2025} boosting is complementary and potentially integrable with OntoCoDec.
```

---

All files have been read in full and returned verbatim. The text captures key numerical claims across the abstract, introduction, and all major results sections for SciERC, DocRED, WikiEvents, cross-model validation, and runtime analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d0c008d-1c8a-4c48-ab70-ca63af9b16de",
  "isSidechain": true,
  "agentId": "a14ef1cbba04e7ca5",
  "requestId": "req_011CbHUMqWXdsy6GNhRZvifM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3145a5c2-37cd-4479-a594-cbf951ae09e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/review_reviewer_2_cbe93d98",
  "sessionId": "a8eeabe9-3cac-4081-abfa-975136506fe2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017fsXDzMYYou1c4spUFbCYq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13850,
      "cache_read_input_tokens": 15701,
      "output_tokens": 11462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13850
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 11462,
          "cache_read_input_tokens": 15701,
          "cache_creation_input_tokens": 13850,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13850,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
