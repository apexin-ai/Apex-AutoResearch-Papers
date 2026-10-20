# Research conversation: Read the following .tex files in full and return their complete contents. These are in the directory `/home/ubuntu/.agen

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aae59a1bf14556cf7.jsonl`
- **Structured JSON:** [`154473d0a561dc17d34c.json`](../../sessions/15/154473d0a561dc17d34c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-17T00:02:58.633Z_

Read the following .tex files in full and return their complete contents. These are in the directory `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`. Read ALL of these files completely:

1. main.tex
2. abstract.tex
3. section1_introduction_draft.tex
4. section3_violation_landscape.tex
5. section4_composition_draft.tex
6. section5_scierc_draft.tex
7. section5_docred_draft.tex
8. section5_crossmodel_draft.tex
9. section5_runtime.tex
10. paper_tables_draft.tex
11. appendix_sampling_table.tex
12. appendix_discussion.tex
13. appendix_llama_per_relation.tex

For each file, output the filename as a header, then the full content. Do NOT summarize - I need the raw text to check numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "87829892-2575-45da-af81-4de49da89354",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T00:02:58.637Z_

```json
{
  "parentUuid": "87829892-2575-45da-af81-4de49da89354",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8932a750-958d-4206-bf11-5b976e829a95",
  "timestamp": "2026-05-17T00:02:58.637Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T00:03:04.365Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X1pdcuYXstbVAuNDzRpfow`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8932a750-958d-4206-bf11-5b976e829a95",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AHrW4V6fXhUwndpLZc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74b204dc-d2d2-4e12-be83-7ecb84114d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrQsJ7h8ahASRrwdqfjynZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15585,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 4 · 2026-05-17T00:03:04.387Z_

<details><summary>↩ Tool result · `toolu_01X1pdcuYXstbVAuNDzRpfow`</summary>

```text
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
67	CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp), confirming that CF$\leftrightarrow$DR represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
68	Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
69	Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
70	Composability with fine-tuned models is validated on both SciERC and DocRED with Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,0.20\%, R-F1 change within $\pm$0.6\,pp), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
71	The semantic layer's dynamic masking assumes each entity type maps to a unique first subword token---verified for both tokenizers on our two ontologies (6 entity types each), but ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented.
72	Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
73	All models tested are 7--8B-parameter class; scaling behavior to larger (70B+) or smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
74	CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.
75	Residual DR under fine-tuning (36 violations across all fine-tuned settings, both models and both datasets) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors correctly caught by constraints (28\%); Llama DocRED alone accounts for 33 of 36 residual violations (92\%), reflecting weaker entity typing (Appendix~\ref{app:residual-dr-analysis}).
76	Schema coverage gaps (one-third of residual violations) are irreducible by decoding-time constraints alone (training-set frequency coverage), motivating complementary approaches such as global type consensus or post-hoc correction.
77	All experiments use greedy decoding; interaction between constrained masking and sampling-based strategies (nucleus, top-$k$) has not been evaluated and may exhibit different fallback dynamics.
78	Validation with fine-tuned models, larger scales, and non-English ontologies remains to be explored.
79	
80	% === Ethics Statement ===
81	\section*{Ethics Statement}
82	
83	This work uses publicly available benchmark datasets (SciERC and DocRED) with no personally identifiable information.
84	No human subjects were involved in the experiments.
85	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
86	Code and data will be released upon acceptance.
87	
88	% === Bibliography ===
89	\bibliography{relwork_new_entries}
90	
91	% === Appendix ===
92	\appendix
93	
94	\input{appendix_prompts}
95	\input{appendix_related_work}
96	\input{appendix_discussion}
97	\input{appendix_llama_per_relation}
98	
99	\end{document}
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74b204dc-d2d2-4e12-be83-7ecb84114d2e",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "7983e4f3-54c5-4afd-9c91-63d8c6bf243f",
  "sourceToolAssistantUUID": "74b204dc-d2d2-4e12-be83-7ecb84114d2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T00:03:04.482Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R2jN2GnGknWsgmFNJRDFhS`</summary>

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
  "parentUuid": "7983e4f3-54c5-4afd-9c91-63d8c6bf243f",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AHrW4V6fXhUwndpLZc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb524f21-9c46-4df1-8612-300ffc90f726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrQsJ7h8ahASRrwdqfjynZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15585,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 6 · 2026-05-17T00:03:04.490Z_

<details><summary>↩ Tool result · `toolu_01R2jN2GnGknWsgmFNJRDFhS`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb524f21-9c46-4df1-8612-300ffc90f726",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "487aea4f-baa3-42a3-a44c-69eedcfac26b",
  "sourceToolAssistantUUID": "cb524f21-9c46-4df1-8612-300ffc90f726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T00:03:05.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RYvvAzY6UZjVyi3mGLk3QL`</summary>

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
  "parentUuid": "487aea4f-baa3-42a3-a44c-69eedcfac26b",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AHrW4V6fXhUwndpLZc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fd1d0f9-c5aa-4058-9f21-ddfb821e1f4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LrQsJ7h8ahASRrwdqfjynZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15585,
      "cache_read_input_tokens": 0,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 248,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15585,
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

_source line 8 · 2026-05-17T00:03:05.052Z_

<details><summary>↩ Tool result · `toolu_01RYvvAzY6UZjVyi3mGLk3QL`</summary>

```text
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
19	The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records type assignments; when relation arguments are generated, dynamic logit masking restricts output to types compatible with the relation's domain/range specification.
20	The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
21	On SciERC, OntoCoDec reduces DR violations from 15.37\% to 0.93\% ($\downarrow$94\%) while remaining F1-neutral ($+$0.13\,pp).
22	
23	Our contributions:
24	\begin{enumerate}
25	    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
26	    \item OntoCoDec, a two-layer compiled constraint framework---the first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE.
27	    \item Empirical validation on 3 models $\times$ 2 datasets: DR $\downarrow$76--99\% on SciERC and $\downarrow$42--90\% across three models on DocRED, with significant R-F1 gains on DocRED (Qwen $p{<}0.001$, Llama $p{=}0.013$), model-agnostic structural guarantees, composability with fine-tuning (DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost), and characterization of the CF$\leftrightarrow$DR trade-off inherent to per-relation enforcement (resolved by fine-tuning to CF\,$\leq$\,1.2\%).
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fd1d0f9-c5aa-4058-9f21-ddfb821e1f4e",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "9cd497c9-76fe-4b86-8204-d3587d679ece",
  "sourceToolAssistantUUID": "5fd1d0f9-c5aa-4058-9f21-ddfb821e1f4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T00:03:09.893Z_

<details open><summary>🔧 Tool call — Read · `toolu_012iw2L2fHSUAoHLvHdTUsCn`</summary>

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
  "parentUuid": "9cd497c9-76fe-4b86-8204-d3587d679ece",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJLQLxeD8YqfC6338D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f160e6d-ef8c-45f9-9fee-0cefe0782138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5vuVFtBUPEP3fiRjHgzPr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4611,
      "cache_read_input_tokens": 15585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4611,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 10 · 2026-05-17T00:03:09.898Z_

<details><summary>↩ Tool result · `toolu_012iw2L2fHSUAoHLvHdTUsCn`</summary>

```text
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
18	RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce a target vocabulary from a single prompt.
19	Per-relation rates (Figure~\ref{fig:per_relation_dr}) vary by over 40 percentage points: \textsc{Compare} at 42.4\% vs.\ \textsc{Used-for} at 0.76\%, correlating with tightness---tight constraints (few valid type pairs) produce systematic failures.
20	
21	\begin{table}[t]
22	\centering
23	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
24	\label{tab:prompt_comparison}
25	\resizebox{\columnwidth}{!}{%
26	\begin{tabular}{ll cccc}
27	\toprule
28	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
29	\midrule
30	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
31	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
32	\midrule
33	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
34	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
35	\bottomrule
36	\end{tabular}%
37	}
38	\end{table}
39	
40	\begin{figure}[t]
41	\centering
42	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
43	\caption{Per-relation DR violation rates on SciERC. Rates correlate with constraint tightness.}
44	\label{fig:per_relation_dr}
45	\end{figure}
46	
47	\paragraph{Prompt insufficiency.}
48	Schema-informed prompting---augmenting the prompt with valid type pairs---reduces DR by 62.4\% on SciERC but only 30.4\% on DocRED (Table~\ref{tab:prompt_comparison}), and is unreliable per-relation: DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp.
49	These limitations motivate decoding-time enforcement (\S\ref{sec:method}).
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f160e6d-ef8c-45f9-9fee-0cefe0782138",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "ff29257f-ef68-4dac-8024-bc4e5e1be644",
  "sourceToolAssistantUUID": "4f160e6d-ef8c-45f9-9fee-0cefe0782138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T00:03:10.720Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XNGBoeseuhEoEHpYLycHAk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff29257f-ef68-4dac-8024-bc4e5e1be644",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJLQLxeD8YqfC6338D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b178bcc-f969-4bb9-bfb9-b3a27b2e2b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5vuVFtBUPEP3fiRjHgzPr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4611,
      "cache_read_input_tokens": 15585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4611,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 12 · 2026-05-17T00:03:10.725Z_

<details><summary>↩ Tool result · `toolu_01XNGBoeseuhEoEHpYLycHAk`</summary>

```text
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
28	This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cross-dataset results: SciERC ($\bar{\kappa}{=}0.333$, 24 valid pairs/relation) achieves 94--99\% DR reduction, while DocRED ($\bar{\kappa}{=}0.842$, 5.68 pairs) achieves 45--90\%, with the residual modulated by model-specific baselines (\S\ref{sec:cross-model}; quantitative analysis in Appendix~\ref{app:dual-factor}).
29	
30	\paragraph{Non-Rectangularity and Sequential Masking.}
31	\label{sec:rectangularity}
32	% Data source: artifacts/rebuttal/w2_rectangularity_report.md
33	The sequential masking strategy---$\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$---is necessary because real ontology type signatures are overwhelmingly non-rectangular: 0/7 SciERC and only 23/96 DocRED relations satisfy $\sigma(r) = \operatorname{dom}(r) \times \operatorname{range}(r)$.
34	Independent enforcement ($\tau^h \in \operatorname{dom}(r) \wedge \tau^t \in \operatorname{range}(r)$) would admit 33.3\% (SciERC) and 36.8\% (DocRED) spurious type pairs---on SciERC, 100\% of residual DR violations under full S1 are pairs that pass independent checks but violate $\sigma(r)$.
35	OntoCoDec's sequential approach achieves exact pair-based enforcement without explicit enumeration of $\sigma(r)$ at each step, exploiting the autoregressive left-to-right generation order.
36	
37	\paragraph{Decidability Taxonomy.}
38	We classify ontology constraints by when sufficient information becomes available:
39	%
40	\begin{enumerate}[leftmargin=*,nosep]
41	  \item \textbf{Local}: require only the current token (entity/relation vocabulary membership). Handled by the grammar layer.
42	  \item \textbf{Prefix-decidable}: require the decoded prefix (domain/range constraints). Handled by the semantic layer via the entity registry.
43	  \item \textbf{Non-local}: require information not yet generated (forward coreference). Outside the scope of single-pass decoding; partially addressed by the two-pass strategy (S2, \S\ref{sec:s2}).
44	\end{enumerate}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b178bcc-f969-4bb9-bfb9-b3a27b2e2b35",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "845eb233-97c7-44e6-8e61-04acb69bf06e",
  "sourceToolAssistantUUID": "7b178bcc-f969-4bb9-bfb9-b3a27b2e2b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T00:03:11.203Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VVK1Q14n9AnqgYhDVVwYUY`</summary>

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
  "parentUuid": "845eb233-97c7-44e6-8e61-04acb69bf06e",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJLQLxeD8YqfC6338D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7959bf64-4bd8-48f5-8961-7f1580788607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5vuVFtBUPEP3fiRjHgzPr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4611,
      "cache_read_input_tokens": 15585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4611,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 14 · 2026-05-17T00:03:11.209Z_

<details><summary>↩ Tool result · `toolu_01VVK1Q14n9AnqgYhDVVwYUY`</summary>

```text
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
63	RV: relation vocabulary violation rate;
64	ET: entity type violation rate;
65	CF: cross-field consistency violation rate.
66	$\Delta$DR: relative DR reduction vs.\ the unconstrained baseline.
67	$\downarrow$\,/\,$\uparrow$: lower\,/\,higher is better.
68	Best per column in \textbf{bold} (CF excluded---see text).
69	F1 scores are multiplied by 100.
70	Statistical significance assessed via bootstrap resampling (10{,}000 iterations).}
71	\label{tab:scierc-ablation}
72	\end{table}
73	
74	% ──────────────────────────────────────────
75	%  (a) Core result
76	% ──────────────────────────────────────────
77	\paragraph{Core result: DR elimination at zero F1 cost.}
78	The full two-layer constraint configuration (S1) reduces domain/range
79	violations from 15.37\% to 0.93\%, a 94\% relative reduction,
80	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
81	while relation F1 moves from 8.23 to 8.36 ($+$0.13\,pp; bootstrap 95\% CI [$-$0.24, $+$0.58]\,pp, $p = 0.58$, 10{,}000 iterations).
82	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
83	% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
84	The difference is not statistically significant ($p = 0.58$), confirming
85	that constraint enforcement is F1-neutral on this dataset.
86	At the per-relation level, violations drop from 42.42\% to 2.82\% on
87	\textsc{Compare}, from 33.54\% to 1.21\% on \textsc{Feature-of}, and
88	reach 0\% on four of seven relation types
89	(\textsc{Conjunction}, \textsc{Hyponym-of}, \textsc{Part-of},
90	\textsc{Used-for}).
91	% phase2_scierc_full_s1 per_relation_dr: Compare=0.0282,
92	%   Feature-of=0.0121, Hyponym-of=0, Part-of=0, Used-for=0, Conjunction=0
93	However, full constraint enforcement elevates cross-field consistency
94	violations from 0.08\% to 9.90\%;
95	% phase2_scierc_unconstrained: CF=0.0008; phase2_scierc_full_s1: CF=0.099
96	we analyze this trade-off in Section~\ref{sec:discussion}.
97	
98	% ──────────────────────────────────────────
99	%  (b) Grammar layer
100	% ──────────────────────────────────────────
101	\paragraph{Grammar layer: cost-free structural guarantees.}
102	Grammar-only constraints eliminate RV (1.39\%\,$\to$\,0\%) and ET (0.40\%\,$\to$\,0\%) with no F1 impact, while DR remains unchanged (15.37\%\,$\to$\,14.84\%), confirming that grammar constraints enforce structural validity but not semantic constraints.
103	% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823
104	
105	% ──────────────────────────────────────────
106	%  (c) Enabling dependency
107	% ──────────────────────────────────────────
108	\paragraph{Enabling dependency.}
109	Semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) and cannot eliminate RV (1.51\%) or ET (0.40\%).
110	% phase2_scierc_semantic_only: DR=0.1165, RV=0.0151, ET=0.004
111	The residual ET under semantic-only arises because the semantic mask constrains type tokens to relation-specific valid sets but cannot enforce vocabulary membership; occasionally the mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative.
112	Under full mode, the grammar layer's intersection prevents this, confirming the \emph{enabling dependency}: without grammar-enforced vocabulary, the semantic layer encounters OOV relation types with no domain/range rules.
113	Adding the grammar layer yields a further 92\% relative reduction (11.65\%\,$\to$\,0.93\%).
114	% phase2_scierc_full_s1: DR=0.0093
115	
116	% ──────────────────────────────────────────
117	%  (d) S1 vs S2
118	% ──────────────────────────────────────────
119	\paragraph{S1 vs.\ S2.}
120	S2 achieves comparable DR (0.97\%) but lower R-F1 (8.03 vs.\ 8.36) with fewer triples (1{,}644 vs.\ 1{,}729) and does not resolve the CF trade-off (8.03\% vs.\ 9.90\%); we adopt S1 as the primary configuration.
121	% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644
122	
123	% ──────────────────────────────────────────
124	%  (e) Composability with Fine-Tuning
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
145	% w5_llama_lora_scierc_constrained_eval: DR=0.0009, R-F1=0.4547, E-F1=0.6776, CF=0.0046
146	
147	On DocRED (96 relation types, document-level), the four-way ablation (Table~\ref{tab:ft-ablation}) reveals a nuanced pattern.
148	Unlike SciERC, unconstrained fine-tuned models retain non-zero RV violations (Qwen 0.27\%, Llama 0.15\%), indicating that the larger relation vocabulary is not fully internalized through training alone; the grammar layer eliminates these (RV\,$\to$\,0\%).
149	However, the grammar layer remains ineffective against DR: grammar-only DR is indistinguishable from unconstrained (Qwen 0.61\% vs.\ 0.76\%, Llama 0.51\% vs.\ 0.49\%; $|\Delta| < 0.2$\,pp).
150	The semantic layer provides the effective DR defense, reducing violations by 72\% for Qwen (0.76\%\,$\to$\,0.21\%) and 39\% for Llama (0.49\%\,$\to$\,0.30\%) in isolation.
151	The full system achieves near-complete DR elimination: Qwen 0.76\%\,$\to$\,0.01\% ($-$98.7\%), Llama 0.49\%\,$\to$\,0.20\% ($-$59.2\%), with R-F1 changes of $-$0.30\,pp and $+$0.51\,pp respectively.\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\,pp (40.86\,$\to$\,40.56); excluding parse-failure documents (7.1\%\,$\to$\,8.5\%) yields $\Delta$R-F1 $+$0.03\,pp. We report all-set as primary.}
152	Parse failure rates on DocRED are non-trivial (7--8.5\%) due to document length but do not differentially affect constraint modes: excluding failed documents, $\Delta$R-F1 is within $\pm$0.1\,pp across all configurations.
153	% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23
154	
155	Across both models and both datasets, fine-tuned + S1 yields DR\,$\leq$\,0.20\% with R-F1 change within $\pm$0.6\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.
156	The four-way ablation consistently shows across all four model$\times$dataset settings (Appendix~\ref{app:ft-ablation}): grammar is a no-op for DR post-fine-tuning ($|\Delta\text{DR}| < 0.2$\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\%; and full constraint enforcement drives DR to near-zero while preserving R-F1.
157	
158	Two secondary observations support this interpretation.
159	First, CF interference drops substantially under fine-tuning for both models: Qwen from $+$9.82\,pp to $+$1.18\,pp, Llama from $+$6.32\,pp to $+$0.46\,pp,
160	% Qwen: ZS CF delta = 9.90-0.08 = 9.82pp, FT CF delta = 1.18-0 = 1.18pp
161	% Llama: ZS CF delta = 6.56-0.24 = 6.32pp, FT CF delta = 0.46-0 = 0.46pp
162	because fine-tuned per-slot type predictions are more consistent with the entity registry;
163	for Qwen, the residual 1.18\% traces to \textsc{Generic}$\leftrightarrow$X schema-level ambiguity (Appendix~\ref{app:cf-distribution}) rather than enforcement failure.
164	Second, in the zero-shot setting, S1 R-F1 impact is negligible for both models (Qwen $+$0.13\,pp, Llama $-$0.14\,pp),
165	% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
166	% llama_scierc_unconstrained: R-F1=0.0268; llama_scierc_full_s1: R-F1=0.0254
167	confirming that constraint enforcement is F1-neutral regardless of base model quality.
168	
169	\begin{table}[t]
170	\centering
171	\small
172	\setlength{\tabcolsep}{3pt}
173	\resizebox{\columnwidth}{!}{%
174	\begin{tabular}{@{}lll rrrr r@{}}
175	\toprule
176	\textbf{Model} & \textbf{Setting} & \textbf{Mode}
177	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
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
188	  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
189	\midrule
190	\multirow{4}{*}{Llama-3.1-8B}
191	  & \multirow{2}{*}{Zero-shot}
192	    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
193	  & & Full S1    &  0.08 & 6.56 & 2.54  & 23.49 & $\downarrow$99\% \\
194	\cmidrule(l){2-8}
195	  & \multirow{2}{*}{LoRA}
196	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
197	  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
198	\bottomrule
199	\end{tabular}}%
200	\caption{Composability matrix on SciERC (551 documents):
201	zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1
202	for Qwen3-8B and Llama-3.1-8B.
203	$\Delta$DR: relative DR reduction vs.\ the same-row unconstrained baseline.
204	Fine-tuning alone leaves residual DR (1--2\%);
205	adding S1 reduces it to $\leq$\,0.09\% with R-F1 change within $\pm$0.1\,pp.
206	DocRED replication: Qwen DR $-$98.7\% ($-$0.30\,pp), Llama DR $-$59.2\% ($+$0.51\,pp).
207	F1\,$\times$100.}
208	\label{tab:composability}
209	\end{table}
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7959bf64-4bd8-48f5-8961-7f1580788607",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "18c334fd-523a-4222-9d9a-7238e931580a",
  "sourceToolAssistantUUID": "7959bf64-4bd8-48f5-8961-7f1580788607",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T00:03:11.489Z_

<details open><summary>🔧 Tool call — Read · `toolu_017DK8i4S4h4s7zCBBAVihrR`</summary>

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
  "parentUuid": "18c334fd-523a-4222-9d9a-7238e931580a",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJLQLxeD8YqfC6338D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26dcb8d2-3ace-4465-b001-dd5853e19b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5vuVFtBUPEP3fiRjHgzPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4611,
      "cache_read_input_tokens": 15585,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4611
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 15585,
          "cache_creation_input_tokens": 4611,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4611,
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

_source line 16 · 2026-05-17T00:03:11.496Z_

<details><summary>↩ Tool result · `toolu_017DK8i4S4h4s7zCBBAVihrR`</summary>

```text
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
59	% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
60	\paragraph{Core result.}
61	Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET (2.48\%\,$\to$\,0\%), and near-eliminates RV (29.66\%\,$\to$\,0.03\%; the residual 5 triples arise from partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple).
62	Relation F1 improves from 7.74 to 8.23 ($+$0.50\,pp; bootstrap 95\% CI [$+$0.23, $+$0.81], $p < 0.001$), attributable to grammar-layer elimination of 5{,}189 OOV relation predictions counted as false positives.
63	CF increases modestly (0.10\%\,$\to$\,2.57\%), lower than SciERC's 9.90\%.
64	
65	% exp_ids: phase2_docred_grammar_only
66	\paragraph{Grammar layer surfaces latent violations.}
67	Grammar-only constraints eliminate RV and ET but \emph{increase} DR from 18.46\% to 26.17\% ($+$42\%).
68	This counter-intuitive result has a structural explanation: the unconstrained baseline's 29.66\% OOV relation triples cannot be evaluated for DR (no schema entry exists); grammar enforcement assigns these triples valid relation names whose domain/range rules the associated entity types frequently violate.
69	The grammar layer thus \emph{reveals} latent type incompatibilities, directly motivating the semantic layer.
70	
71	% exp_ids: phase2_docred_semantic_only, phase2_docred_full_s1
72	\paragraph{Enabling dependency.}
73	Semantic-only constraints reduce DR by only 25\% (18.46\%\,$\to$\,13.84\%) while failing to eliminate RV (29.87\%) or ET (4.22\%).
74	Full S1 achieves a further 26\% relative reduction over semantic-only (13.84\%\,$\to$\,10.21\%), replicating the enabling dependency from SciERC: without grammar-enforced vocabulary, the semantic layer encounters OOV relation types for which no domain/range rules exist.
75	
76	% exp_ids: phase2_docred_full_s1, llama_docred_full_s1
77	\paragraph{Zero-shot F1 context.}
78	Zero-shot R-F1 values (6--8\%) reflect zero-shot RE difficulty; supervised SOTA achieves 49--53\% on SciERC~\citep{zhong2021frustratingly}.
79	F1 serves primarily as a control variable verifying constraint enforcement preserves extraction quality, not as an optimization target.
80	
81	\paragraph{Constraint tightness governs enforcement ceiling.}
82	The residual DR on DocRED (10.21\%) exceeds SciERC (0.93\%) due to per-relation \emph{constraint tightness}: DocRED relations average 5.68 valid type pairs ($\bar{\kappa}{=}0.842$) vs.\ 24 on SciERC ($\bar{\kappa}{=}0.333$).
83	Tighter constraints produce narrower grammar$\cap$semantic mask intersections, increasing fallback frequency---the aggregate fallback rate (10.2\%; 1{,}770/17{,}341 triples) closely tracks residual DR (10.21\%), confirming a near-bijection between fallback events and residual violations.
84	Crucially, tightness interacts with the model's baseline violation profile: Qwen's high RV (29.66\%) causes grammar enforcement to surface many latent DR violations, yielding 10.21\% residual DR; Llama's lower RV (16.03\%) limits this surfacing, achieving 2.55\% residual ($\downarrow$90.2\%) on the same ontology (\S\ref{sec:cross-model}).
85	This dual-factor pattern---tightness $\times$ baseline RV---is consistent with cross-dataset and cross-model DR reduction differences.
86	We omit S2 on DocRED because S1 already achieves near-complete RV/ET elimination and the two-pass overhead is less justified when residual DR is dominated by fallback events rather than forward coreference.
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26dcb8d2-3ace-4465-b001-dd5853e19b2e",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "eb42e971-e700-4420-aaf1-90725501aae9",
  "sourceToolAssistantUUID": "26dcb8d2-3ace-4465-b001-dd5853e19b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T00:03:16.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vkc8s8T7bjJLFGt2MiS9X3`</summary>

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
  "parentUuid": "eb42e971-e700-4420-aaf1-90725501aae9",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJoiesw76912QjZ3gW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba73feb9-56d6-4f0b-8de3-e8143ae80c6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjP1MyPsFG2LMa4P2ReNse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10700,
      "cache_read_input_tokens": 20196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10700,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 18 · 2026-05-17T00:03:16.761Z_

<details><summary>↩ Tool result · `toolu_01Vkc8s8T7bjJLFGt2MiS9X3`</summary>

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
43	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
44	  \cmidrule(l){2-7}
45	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
46	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
47	\bottomrule
48	\end{tabular}}%
49	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
50	Parse failures: Qwen DocRED 12$\to$11 (S1 1.10\%), Llama DocRED 68$\to$91; others $\leq$1.
51	$^\dagger$Mistral's poor zero-shot type calibration leads to pervasive entity type assignment inconsistencies across triples.
52	F1 $\times$100.}
53	\label{tab:cross-model}
54	\end{table}
55	
56	\paragraph{Model-agnostic structural guarantees.}
57	RV and ET violations are eliminated ($\leq$0.03\%) for all three models on both datasets, confirming that grammar-layer enforcement depends on the decoding mechanism, not model-specific generation patterns.
58	
59	% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
60	\paragraph{DR reduction generalizes across models.}
61	SciERC DR drops 94\% (Qwen), 99\% (Llama), 76\% (Mistral); DocRED DR drops 45\% (Qwen), 90\% (Llama), 42\% (Mistral).
62	Mistral exhibits the highest baseline DR (56--57\%) due to poor zero-shot type calibration, yet still benefits substantially.
63	R-F1 is preserved or improves in five of six settings; on DocRED, gains are significant for Qwen ($+$0.50\,pp, $p{<}0.001$) and Llama ($+$0.29\,pp, $p{=}0.013$).
64	
65	\paragraph{Cross-model DR asymmetry.}
66	Llama's higher DR reduction reflects lower baseline RV (16.03\% vs.\ 29.66\% on DocRED): with fewer OOV relations to surface, grammar enforcement exposes fewer latent type incompatibilities, yielding residual DR of 2.55\% vs.\ Qwen's 10.21\%.
67	Llama's per-relation DR shows no correlation with tightness ($\rho{=}0.069$, $p{=}0.52$; Appendix~\ref{app:llama-per-relation}), confirming uniform enforcement once baseline RV is low.
68	CF direction depends on baseline calibration: S1 introduces CF for well-calibrated Qwen and Llama (up to 12.02\%; \S\ref{sec:discussion}), while reducing CF for poorly-calibrated Mistral (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
69	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba73feb9-56d6-4f0b-8de3-e8143ae80c6f",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "31f48952-b773-45f6-84ad-3829a8eb55c0",
  "sourceToolAssistantUUID": "ba73feb9-56d6-4f0b-8de3-e8143ae80c6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T00:03:17.132Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SeaotCGxVmgrk44x1E4hwC`</summary>

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
  "parentUuid": "31f48952-b773-45f6-84ad-3829a8eb55c0",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJoiesw76912QjZ3gW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fc3fac9-87d5-4784-9e67-5109e13ede80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjP1MyPsFG2LMa4P2ReNse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10700,
      "cache_read_input_tokens": 20196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10700,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 20 · 2026-05-17T00:03:17.137Z_

<details><summary>↩ Tool result · `toolu_01SeaotCGxVmgrk44x1E4hwC`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fc3fac9-87d5-4784-9e67-5109e13ede80",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "f25613bd-2014-4de8-8fda-182b699bf522",
  "sourceToolAssistantUUID": "4fc3fac9-87d5-4784-9e67-5109e13ede80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T00:03:18.159Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AUxywqU2YQWnMJiz99mNfH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/paper_tables_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f25613bd-2014-4de8-8fda-182b699bf522",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJoiesw76912QjZ3gW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27bae0c5-9da9-408c-9b19-034bf877e535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjP1MyPsFG2LMa4P2ReNse",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10700,
      "cache_read_input_tokens": 20196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10700,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 22 · 2026-05-17T00:03:18.164Z_

<details><summary>↩ Tool result · `toolu_01AUxywqU2YQWnMJiz99mNfH`</summary>

```text
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
36	\texttt{phase2\_scierc\_semantic\_only},
37	\texttt{phase2\_scierc\_full\_s1},
38	\texttt{phase2\_scierc\_full\_s2}.
39	}
40	\end{table}
41	
42	
43	% ------------------------------------------------------------
44	% Table 2: Per-Relation DR Violation Analysis (SciERC)
45	% ------------------------------------------------------------
46	\begin{table}[t]
47	\centering
48	\caption{Per-relation Domain/Range violation rates on SciERC:
49	Unconstrained baseline vs.\ Full (S1) constrained decoding.
50	$n$ = predicted triples of that relation type (unconstrained).
51	$\Delta$ = absolute change in violation rate (pp).}
52	\label{tab:scierc-per-relation-dr}
53	\begin{tabular}{l r rr r}
54	\toprule
55	Relation & $n$ & Uncon.\ (\%) & S1 (\%) & $\Delta$ (pp) \\
56	\midrule
57	Compare      &  66 & 42.4 &  2.8 & $-$39.6 \\
58	Feature-of   & 486 & 33.5 &  1.2 & $-$32.3 \\
59	Part-of      &  72 & 25.0 & \textbf{0.0} & $-$25.0 \\
60	Evaluate-for & 133 & 24.1 &  5.8 & $-$18.3 \\
61	Hyponym-of   & 124 & 14.5 & \textbf{0.0} & $-$14.5 \\
62	Used-for     & 787 &  0.8 & \textbf{0.0} & $-$0.8  \\
63	Conjunction  &  32 &  0.0 & \textbf{0.0} &    0.0  \\
64	\midrule
65	\textit{Overall} & \textit{1724} & \textit{15.4} & \textit{0.9} & \textit{$-$14.4} \\
66	\bottomrule
67	\end{tabular}
68	\vspace{2pt}
69	{\footnotesize
70	\textit{Exp IDs:}
71	\texttt{phase2\_scierc\_unconstrained} (Uncon.),
72	\texttt{phase2\_scierc\_full\_s1} (S1).
73	}
74	\end{table}
75	
76	
77	% ------------------------------------------------------------
78	% Table 3: DocRED Phase 0 — Prompt-level Intervention
79	% ------------------------------------------------------------
80	\begin{table}[t]
81	\centering
82	\caption{Prompt-level intervention on DocRED dev set (998 documents, 96 relation types, Qwen3-8B zero-shot).
83	Comparing minimal prompt vs.\ schema-informed prompt that explicitly lists valid relation types
84	and domain/range constraints.}
85	\label{tab:docred-phase0}
86	\begin{tabular}{l cccc}
87	\toprule
88	Mode & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & JSON Parse$\uparrow$ \\
89	\midrule
90	Minimal          & 18.5          & 29.7          & 2.5          & \textbf{96.4} \\
91	Schema-informed  & \textbf{12.8} & \textbf{18.4} & \textbf{0.2} & 94.5          \\
92	\midrule
93	$\Delta$         & $-$5.7        & $-$11.3       & $-$2.3       & $-$1.9        \\
94	\bottomrule
95	\end{tabular}
96	\vspace{2pt}
97	{\footnotesize
98	\textit{Exp IDs:}
99	\texttt{mvp\_phase0\_violation\_rate\_docred} (Minimal),
100	\texttt{mvp\_phase0\_docred\_schema} (Schema-informed).
101	}
102	\end{table}
103	
104	
105	% ------------------------------------------------------------
106	% Table 4: Cross-dataset Violation Comparison
107	% ------------------------------------------------------------
108	\begin{table}[t]
109	\centering
110	\caption{Cross-dataset comparison of ontology violation rates.
111	Baseline = unconstrained Qwen3-8B zero-shot; S1 = Grammar + Semantic constrained decoding.}
112	\label{tab:cross-dataset}
113	\begin{tabular}{l c ccc cc}
114	\toprule
115	Dataset & \#Rels & DR\textsubscript{base} & RV\textsubscript{base} & ET\textsubscript{base} & DR\textsubscript{S1} & $\Delta$DR (pp) \\
116	\midrule
117	SciERC & 7  & 15.4 & 1.4  & 0.4 & 0.9          & $-$14.4 \\
118	DocRED & 96 & 18.5 & 29.7 & 2.5 & 10.21 & $-$8.3 \\
119	\bottomrule
120	\end{tabular}
121	\vspace{2pt}
122	{\footnotesize
123	\textit{Exp IDs:}
124	SciERC base = \texttt{phase2\_scierc\_unconstrained},
125	SciERC S1 = \texttt{phase2\_scierc\_full\_s1},
126	DocRED base = \texttt{mvp\_phase0\_violation\_rate\_docred},
127	DocRED S1 = \texttt{phase2\_docred\_full\_s1}.
128	}
129	\end{table}
130	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27bae0c5-9da9-408c-9b19-034bf877e535",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "24de98d0-4536-4629-90fa-80799a49df82",
  "sourceToolAssistantUUID": "27bae0c5-9da9-408c-9b19-034bf877e535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T00:03:18.631Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PNiqGNKvZC1vabxj2wgQv1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24de98d0-4536-4629-90fa-80799a49df82",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AJoiesw76912QjZ3gW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a6f3e74-27a3-4fec-9f36-2543040a2f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjP1MyPsFG2LMa4P2ReNse",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10700,
      "cache_read_input_tokens": 20196,
      "output_tokens": 335,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10700
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 335,
          "cache_read_input_tokens": 20196,
          "cache_creation_input_tokens": 10700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10700,
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

_source line 24 · 2026-05-17T00:03:18.637Z_

<details><summary>↩ Tool result · `toolu_01PNiqGNKvZC1vabxj2wgQv1`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
4	\label{tab:sampling-robustness}
5	\begin{tabular}{llcccccc}
6	\toprule
7	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
8	\midrule
9	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.82 & 30.98 & 8.36 \\
10	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
11	\midrule
12	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
13	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
14	\bottomrule
15	\end{tabular}
16	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a6f3e74-27a3-4fec-9f36-2543040a2f4b",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "68a98b59-780d-43b6-8611-b82a13ea4f58",
  "sourceToolAssistantUUID": "4a6f3e74-27a3-4fec-9f36-2543040a2f4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T00:03:24.203Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HNn3649oaXoSBLNAEsc13W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68a98b59-780d-43b6-8611-b82a13ea4f58",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AKLEhoQhjF4uMX7U4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8b1bcda-3647-443d-af28-891aba0a0193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPpaP2qVqoCBHxPLadVH4e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5906,
      "cache_read_input_tokens": 30896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5906,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
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

_source line 26 · 2026-05-17T00:03:24.459Z_

<details><summary>↩ Tool result · `toolu_01HNn3649oaXoSBLNAEsc13W`</summary>

```text
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
26	The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
27	\emph{Grammar-first fallback} (36.6\% of type-bearing positions on SciERC) occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations---these events account for the residual DR that persists after constraint enforcement.
28	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
29	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
30	
31	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
32	On SciERC, this yields 63.4\% coverage---at 63.4\% of type-bearing positions, the semantic layer actively constrains generation.
33	This metric directly quantifies the enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
34	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
35	
36	%%% CF-DR Trade-off Analysis %%%
37	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
38	
39	\paragraph{CF-DR Trade-off Analysis.}
40	\label{app:cf-dr-tradeoff}
41	
42	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
43	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
44	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
45	
46	\begin{table}[t]
47	\centering
48	\small
49	\begin{tabular}{@{}l rrrr@{}}
50	\toprule
51	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
52	\midrule
53	Full S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
54	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
55	\midrule
56	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
57	\bottomrule
58	\end{tabular}
59	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: grammar-first fallback rate at type-bearing positions.}
60	\label{tab:cf-dr-tradeoff}
61	\end{table}
62	
63	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
64	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
65	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
66	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
67	The grammar-first fallback is triggered at 36.64\% of type-bearing positions, indicating that this conflict is structural, not a tunable hyperparameter.
68	
69	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
70	Within this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
71	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use---a distinction the per-slot decoder cannot resolve without document-level coreference.
72	
73	Two complementary paths can lower CF without re-routing it to DR.
74	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
75	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
76	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
77	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
78	
79	%%% Dual-Factor Quantitative Analysis %%%
80	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
81	%          llama_scierc_full_s1, llama_docred_full_s1
82	
83	\paragraph{Dual-Factor Quantitative Analysis.}
84	\label{app:dual-factor}
85	
86	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for all four model$\times$dataset configurations.
87	A linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$; we do not report a $p$-value given the small sample size).
88	The strong fit is consistent with the dual-factor pattern described in \S\ref{sec:composition}: configurations with higher tightness and higher baseline violation rate exhibit proportionally higher residual DR after constraint enforcement.
89	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
90	
91	\begin{figure}[t]
92	\centering
93	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
94	\caption{Residual DR vs.\ $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ across four model$\times$dataset configurations.
95	Linear fit: $y = 0.366x - 0.138$, $R^2 = 0.886$.}
96	\label{fig:dual-factor-scatter}
97	\end{figure}
98	
99	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
100	% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
101	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
102	
103	\paragraph{Dataset-Dependent F1 Impact.}
104	The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
105	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
106	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
107	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that F1 gain magnitude is proportional to baseline OOV rate.
108	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
109	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
110	
111	%%% Paragraph 1: Low F1 Practical Significance %%%
112	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
113	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
114	
115	\paragraph{Practical Significance of Zero-Shot F1.}
116	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
117	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
118	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
119	When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
120	% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
121	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
122	The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.
123	
124	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
125	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
126	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
127	
128	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
129	Post-hoc filtering---generating triples without constraints, then removing schema-violating predictions---yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
130	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
131	However, this precision gain comes at substantial cost.
132	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions), reducing recall from 9.46\% to 8.40\%.
133	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
134	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
135	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
136	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
137	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
138	
139	%%% CF Violation Distribution %%%
140	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
141	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
142	
143	\paragraph{Cross-Field Violation Distribution.}
144	\label{app:cf-distribution}
145	
146	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise---no mention triggered $\geq$3 types).
147	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
148	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially---a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
149	
150	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
151	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets, confirming that CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
152	
153	\begin{table}[t]
154	\centering
155	\small
156	\begin{tabular}{@{}lr r@{}}
157	\toprule
158	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
159	\midrule
160	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
161	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
162	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
163	Method $\leftrightarrow$ Task & 20 & 8.2 \\
164	Material $\leftrightarrow$ Method & 17 & 6.9 \\
165	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
166	\midrule
167	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
168	\midrule
169	\textbf{Total} & \textbf{245} & 100.0 \\
170	\bottomrule
171	\end{tabular}
172	\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).
173	All 245 violations are pairwise conflicts.
174	Conflicts involving \textsc{Generic} account for 63.3\%.}
175	\label{tab:cf-distribution}
176	\end{table}
177	
178	%%% Per-Relation DR Elimination under Fine-Tuning %%%
179	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
180	
181	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
182	\label{app:lora-per-relation}
183	
184	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
185	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
186	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
187	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
188	
189	\begin{table}[t]
190	\centering
191	\small
192	\begin{tabular}{@{}l r rr rr@{}}
193	\toprule
194	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
195	\cmidrule(lr){3-4} \cmidrule(l){5-6}
196	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
197	\midrule
198	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
199	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
200	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
201	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
202	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
203	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
204	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
205	\bottomrule
206	\end{tabular}
207	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
208	$\kappa$: constraint tightness; $n$: predicted triple count.
209	Used-for gains one triple from Evaluate-for redirection.}
210	\label{tab:lora-per-relation}
211	\end{table}
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
248	  & & Full S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
249	  \cmidrule(l){2-10}
250	  & \multirow{4}{*}{Llama-3.1-8B}
251	    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\
252	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
253	  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
254	  & & Full S1       & \textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 85.23 & 44.23 \\
255	\bottomrule
256	\end{tabular}}%
257	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
258	DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
259	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
260	Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
261	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED full vs.\ unconstrained).}
262	\label{tab:ft-ablation}
263	\end{table}
264	
265	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
266	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
267	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings), confirming that even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate---specifically on tight-constraint relations where the valid type-pair space is small.
268	F1 cost is negligible: the maximum R-F1 decrease across all 16 model$\times$dataset$\times$mode combinations is $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained), attributable to parse failure increase (7.11\%\,$\to$\,8.52\%) rather than constraint-induced extraction degradation.
269	
270	%%% Residual DR Error Analysis (Fine-Tuned) %%%
271	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
272	
273	\paragraph{Residual DR Error Analysis.}
274	\label{app:residual-dr-analysis}
275	
276	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ full S1), only 36 domain/range violations remain.
277	Manual inspection reveals four root causes:
278	
279	\begin{enumerate}[nosep,leftmargin=*]
280	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
281	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
282	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
283	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
284	\end{enumerate}
285	
286	Two dataset-specific patterns emerge.
287	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps---the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
288	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
289	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
290	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), confirming that the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
291	
292	%%% Post-Hoc Filtering Comparison (Extended) %%%
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
328	F1 $\times$100.}
329	\label{tab:posthoc-extended}
330	\end{table}
331	
332	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
333	OntoCoDec's advantage thus scales with violation severity---precisely when constraints are most needed, post-hoc filtering is most destructive.
334	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
335	
336	%%% FT Latency %%%
337	
338	\paragraph{Fine-Tuned Latency Profiling.}
339	\label{app:ft-latency}
340	Under LoRA fine-tuning (Qwen3-8B, SciERC, 100 documents, RTX PRO 6000), per-document inference times are: unconstrained 2.594\,s, grammar-only 2.637\,s ($+$1.7\%), semantic-only 2.625\,s ($+$1.2\%), full S1 2.655\,s ($+$2.3\%, $p{<}0.0001$ paired $t$-test).
341	The combined overhead is sub-additive (2.3\% $<$ 1.7\%$+$1.2\%) because fine-tuned models produce fewer grammar-first fallback events (the semantic mask conflicts with grammar-valid tokens less often when per-slot predictions are better calibrated), reducing the number of active masking calls per document.
342	Compared to the zero-shot regime (Table~\ref{tab:runtime}), absolute overhead decreases from seconds-scale to milliseconds-scale: the fine-tuned model generates shorter, more structured outputs, compressing total generation time from 8.69\,s to 2.594\,s per document.
343	
344	%%% Fuzzy Relation Matching %%%
345	
346	\paragraph{Relation Matching Protocol.}
347	\label{app:fuzzy-matching}
348	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
349	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
350	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
351	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
352	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
353	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
354	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8b1bcda-3647-443d-af28-891aba0a0193",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "560695d3-7658-407c-b6b6-a31effe1939f",
  "sourceToolAssistantUUID": "f8b1bcda-3647-443d-af28-891aba0a0193",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T00:03:24.599Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BGm4YdAAHiJ4Nha4vvfG2W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "560695d3-7658-407c-b6b6-a31effe1939f",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AKLEhoQhjF4uMX7U4F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "391c5c5e-c579-435f-b7ae-5fe5307ff074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPpaP2qVqoCBHxPLadVH4e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5906,
      "cache_read_input_tokens": 30896,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 30896,
          "cache_creation_input_tokens": 5906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5906,
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

_source line 28 · 2026-05-17T00:03:24.607Z_

<details><summary>↩ Tool result · `toolu_01BGm4YdAAHiJ4Nha4vvfG2W`</summary>

```text
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
36	Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's residual DR on the same relations is markedly lower---P1198 reaches only 20.0\% and no relation-level fallback concentration comparable to Qwen is observed.
37	% exp_ids: llama_docred_full_s1, qwen_docred_full_s1
38	The substantially lower residual DR for Llama (2.55\% vs.\ Qwen's 10.21\%) on the same ontology confirms that constraint tightness alone does not determine enforcement effectiveness: the model's baseline vocabulary compliance (RV) modulates the fraction of triples eligible for semantic-layer enforcement.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "391c5c5e-c579-435f-b7ae-5fe5307ff074",
  "isSidechain": true,
  "promptId": "b8c1bcdc-89bc-4fdd-940d-295cdbce2c49",
  "agentId": "aae59a1bf14556cf7",
  "type": "user",
  "uuid": "e402e11d-4bf7-4fc0-820a-96048565af20",
  "sourceToolAssistantUUID": "391c5c5e-c579-435f-b7ae-5fe5307ff074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-17T00:12:50.166Z_

Here are the complete contents of all 13 requested files:

---

## 1. main.tex

```latex
\documentclass[11pt]{article}

\usepackage[review]{acl}

\usepackage{times}
\usepackage{latexsym}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{enumitem}
\usepackage{xcolor}

\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Ontology Constraints}

\author{Anonymous ACL submission}

\begin{document}
\maketitle

% === Abstract ===
\input{abstract}

% === §1 Introduction ===
\input{section1_introduction_draft}

% === §2 Background ===
\input{section2_background}

% === §3 Method ===
\input{section3_method_draft}

% === §4 Constraint Composition ===
\section{Constraint Composition}
\label{sec:composition}
\input{section4_composition_draft}

% === §5 Experiments ===
\section{Experiments}
\label{sec:experiments}

\subsection{Violation Landscape}
\input{section3_violation_landscape}

\input{section5_scierc_draft}
\input{section5_docred_draft}
\input{section5_crossmodel_draft}
\input{section5_runtime}

% === §6 Related Work ===
\input{section6_related_work}

% === §7 Discussion and Conclusion ===
\section{Discussion and Conclusion}
\label{sec:discussion}
\input{section7_conclusion_compressed}

% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
\clearpage
\section*{Limitations}

CF impact is model-dependent: for well-calibrated models (Qwen, Llama), S1 introduces CF violations (up to 12.02\%) as a consequence of per-relation independent enforcement; for poorly-calibrated models (Mistral), S1 substantially reduces CF (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
CF fallback ablation shows that eliminating CF re-routes violations to DR ($+$13.85\,pp), confirming that CF$\leftrightarrow$DR represents a fundamental trade-off in composable constraint systems rather than an independently resolvable limitation (Appendix~\ref{app:cf-dr-tradeoff}).
Entity F1 impact is model-dependent ($+$1.22\,pp for Qwen vs.\ $-$0.64\,pp for Llama on DocRED), partially confounded by increased parse failures under constraints (Llama: 9.1\% vs.\ 6.8\%).
Zero-shot results cover three 7--8B-class models, where relation F1 remains around 4--8\% compared to $\sim$45\% for fine-tuned systems.
Composability with fine-tuned models is validated on both SciERC and DocRED with Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,0.20\%, R-F1 change within $\pm$0.6\,pp), but evaluation is limited to one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\% on SciERC) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
The semantic layer's dynamic masking assumes each entity type maps to a unique first subword token---verified for both tokenizers on our two ontologies (6 entity types each), but ontologies with many types or multi-token type names would require prefix-tree masking, which we have not implemented.
Global entity-level type consensus during decoding offers the most direct path to resolving CF violations.
All models tested are 7--8B-parameter class; scaling behavior to larger (70B+) or smaller models has not been verified, and the dual-factor pattern's predictive scope may differ at other scales.
CF type inconsistencies may propagate to downstream tasks that consume extracted triples (e.g., knowledge graph construction, question answering); the impact of such propagation has not been evaluated.
Residual DR under fine-tuning (36 violations across all fine-tuned settings, both models and both datasets) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors correctly caught by constraints (28\%); Llama DocRED alone accounts for 33 of 36 residual violations (92\%), reflecting weaker entity typing (Appendix~\ref{app:residual-dr-analysis}).
Schema coverage gaps (one-third of residual violations) are irreducible by decoding-time constraints alone (training-set frequency coverage), motivating complementary approaches such as global type consensus or post-hoc correction.
All experiments use greedy decoding; interaction between constrained masking and sampling-based strategies (nucleus, top-$k$) has not been evaluated and may exhibit different fallback dynamics.
Validation with fine-tuned models, larger scales, and non-English ontologies remains to be explored.

% === Ethics Statement ===
\section*{Ethics Statement}

This work uses publicly available benchmark datasets (SciERC and DocRED) with no personally identifiable information.
No human subjects were involved in the experiments.
The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
Code and data will be released upon acceptance.

% === Bibliography ===
\bibliography{relwork_new_entries}

% === Appendix ===
\appendix

\input{appendix_prompts}
\input{appendix_related_work}
\input{appendix_discussion}
\input{appendix_llama_per_relation}

\end{document}
```

---

## 2. abstract.tex

```latex
\begin{abstract}
We present \textsc{OntoCoDec}, which compiles IE ontology schemas into two composable token-level decoding constraints that provide formal guarantees during autoregressive generation:
(1)~a \emph{grammar layer} (XGrammar CFG) guaranteeing JSON structural validity and entity/relation vocabulary membership (ET, RV\,$\to$\,0\%); and
(2)~a \emph{semantic layer} guaranteeing per-triple domain/range type compliance via a stateful entity registry and dynamic logit masking.
The two layers compose via bitwise AND on logit masks, with the grammar layer as an enabling prerequisite.
%
Without constraints, LLM-based IE produces systematic violations: 15.37\% DR on SciERC (7 relations) and 18.46\% on DocRED (96 relations)---comparable rates governed by \emph{constraint tightness} rather than ontology scale.
\textsc{OntoCoDec} reduces DR by 42--99\% across three model families (Qwen3-8B, Llama-3.1-8B, Mistral-7B) with no significant F1 cost.
For the primary model (Qwen3-8B): SciERC $+$0.13\,pp ($p{=}0.58$), DocRED $+$0.50\,pp ($p{<}0.001$); other models show comparable or larger gains (\S\ref{sec:cross-model}).
% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_docred
Residual DR is characterized by a dual-factor pattern (schema tightness $\times$ model calibration; $R^2{=}0.886$, $n{=}4$; Appendix~\ref{app:dual-factor}).
Composed with LoRA fine-tuning, DR reaches $\leq$\,0.09\% (SciERC) and 0.20\% (DocRED) with R-F1 within $\pm$0.6\,pp, confirming orthogonal composability.
Per-relation independent enforcement introduces a CF$\leftrightarrow$DR trade-off: cross-field consistency violations arise (up to 12\% in zero-shot) as the cost of per-slot domain/range guarantees; fine-tuning resolves this tension (CF\,$\leq$\,1.2\%).
\end{abstract}
```

---

## 3. section1_introduction_draft.tex

```latex
% Section 1: Introduction (compressed, 669→~550 words)

\section{Introduction}
\label{sec:introduction}

Large language models are increasingly deployed for zero-shot information extraction~\cite{li2023codeie,sainz2024gollie,wei2023zeroshot}, but when generating relation triples $(h, r, t)$, neither entity is guaranteed to carry a type consistent with the ontology's domain/range constraints for $r$.
We call such outputs \emph{domain/range violations}---structurally valid triples that are ontologically invalid.
In a systematic study, we find violations are pervasive: 15.4\% of triples on SciERC~\cite{luan2018scierc} and 18.5\% on DocRED~\cite{yao2019docred}, driven by \emph{constraint tightness} (few valid type pairs per relation) rather than ontology scale.
Relations with tight constraints exhibit far higher rates (\textsc{Compare}: 42.4\%) than loosely constrained ones (\textsc{Used-for}: 0.8\%).

Existing approaches leave a fundamental gap.
Schema-informed prompting reduces violations by 62\% on average but is per-relation unreliable---violations for \textsc{Evaluate-for} actually \emph{increase} by 5.8\,pp.
Grammar-constrained decoding~\cite{dong2025xgrammar,willard2023outlines,beurer-kellner2023lmql} guarantees syntactic well-formedness but cannot encode cross-field semantic constraints.
At high rejection rates (e.g., Mistral DocRED 73.7\%), post-hoc filtering discards the majority of outputs including true positives, making it impractical; it also cannot redirect probability mass during decoding.
Training-based approaches~\cite{sainz2024gollie,lu2022uie} provide only soft guidance that cannot eliminate violations.

We propose \textbf{OntoCoDec} (\textbf{Onto}logy-\textbf{Co}mpiled \textbf{Dec}oding), a framework that compiles an IE ontology into two composable layers of decoding-time constraints.
The \emph{grammar layer} enforces JSON well-formedness and vocabulary validity via XGrammar.
The \emph{semantic layer} maintains a stateful entity registry during generation: as entities are decoded, the registry records type assignments; when relation arguments are generated, dynamic logit masking restricts output to types compatible with the relation's domain/range specification.
The layers compose via bitwise AND with an \emph{enabling dependency}: the grammar layer guarantees vocabulary membership, enabling the semantic layer to look up domain/range rules.
On SciERC, OntoCoDec reduces DR violations from 15.37\% to 0.93\% ($\downarrow$94\%) while remaining F1-neutral ($+$0.13\,pp).

Our contributions:
\begin{enumerate}
    \item The first systematic study of ontological constraint violations in LLM-based IE (spanning per-relation tightness analysis, dual-factor characterization, and post-hoc baseline comparison), showing that violation rates are driven by constraint tightness rather than ontology size, and that prompt-level intervention is per-relation unreliable.
    \item OntoCoDec, a two-layer compiled constraint framework---the first to enforce pair-based domain/range type constraints via compiled stateful logit masks during autoregressive IE.
    \item Empirical validation on 3 models $\times$ 2 datasets: DR $\downarrow$76--99\% on SciERC and $\downarrow$42--90\% across three models on DocRED, with significant R-F1 gains on DocRED (Qwen $p{<}0.001$, Llama $p{=}0.013$), model-agnostic structural guarantees, composability with fine-tuning (DR\,$\leq$\,0.20\% at $<$0.6\,pp F1 cost), and characterization of the CF$\leftrightarrow$DR trade-off inherent to per-relation enforcement (resolved by fine-tuning to CF\,$\leq$\,1.2\%).
\end{enumerate}
```

---

## 4. section3_violation_landscape.tex

```latex
% §5.1 Experimental Setup and Violation Landscape
% Compressed from standalone section. main.tex provides \subsection header.
% exp_ids: mvp_phase0_violation_rate, mvp_phase0_scierc_schema,
%          mvp_phase0_violation_rate_docred, mvp_phase0_docred_schema

\label{sec:violation_landscape}

\paragraph{Setup.}
We evaluate Qwen3-8B~\cite{qwen2025qwen3} under zero-shot greedy decoding on two IE benchmarks:
\textbf{SciERC}~\cite{luan2018scierc} (551 test sentences, 7 relations, avg.\ 26.1 valid type pairs per relation) and \textbf{DocRED}~\cite{yao2019docred} (998 dev documents,\footnote{DocRED test set annotations are not publicly available; following prior work, we evaluate on the development set (998 documents).} 96 relations, avg.\ 5.68 valid pairs).
We measure four violation categories: \textbf{Domain/Range (DR)} violations where $(\mathrm{type}(h), \mathrm{type}(t)) \notin \sigma(r)$; \textbf{Relation Vocabulary (RV)} where $r \notin \mathcal{R}$; \textbf{Entity Type (ET)} where $e \notin \mathcal{E}$; and \textbf{Cross-Field Consistency (CF)} where the same entity receives different types across triples.
Cross-model validation with Llama-3.1-8B-Instruct is reported in \S\ref{sec:cross-model}.
Violation rates are computed over successfully parsed documents; including parse failures as zero-violation instances adjusts rates by at most 0.23\,pp (Llama DocRED zero-shot; $<$0.01\,pp under fine-tuning), confirming robustness to this exclusion.

\paragraph{Violation distribution.}
Table~\ref{tab:prompt_comparison} reports violation rates.
DR violations affect 15.37\% of triples on SciERC and 18.46\% on DocRED---comparable rates despite a 14$\times$ difference in ontology size---indicating that violation severity is driven by \emph{constraint tightness} rather than ontology scale.
RV violations on DocRED are dramatically higher (29.66\% vs.\ 1.39\%), indicating that 96 relation types exceed the model's capacity to reproduce a target vocabulary from a single prompt.
Per-relation rates (Figure~\ref{fig:per_relation_dr}) vary by over 40 percentage points: \textsc{Compare} at 42.4\% vs.\ \textsc{Used-for} at 0.76\%, correlating with tightness---tight constraints (few valid type pairs) produce systematic failures.

\begin{table}[t]
\centering
\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
\label{tab:prompt_comparison}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{ll cccc}
\toprule
Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
\midrule
\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
\midrule
\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
\caption{Per-relation DR violation rates on SciERC. Rates correlate with constraint tightness.}
\label{fig:per_relation_dr}
\end{figure}

\paragraph{Prompt insufficiency.}
Schema-informed prompting---augmenting the prompt with valid type pairs---reduces DR by 62.4\% on SciERC but only 30.4\% on DocRED (Table~\ref{tab:prompt_comparison}), and is unreliable per-relation: DR for \textsc{Evaluate-for} \emph{increases} by 5.8\,pp.
These limitations motivate decoding-time enforcement (\S\ref{sec:method}).
```

---

## 5. section4_composition_draft.tex

```latex
% Section: Constraint Composition (compressed, 787→~500 words)

At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
The final mask is their conjunction:
%
\begin{equation}\label{eq:composition}
  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
\end{equation}
%
so a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$, reflecting the enabling dependency (\S\ref{sec:method})---the semantic layer requires the relation type to belong to $\mathcal{R}$, a property guaranteed only by the grammar layer.

\paragraph{Grammar-First Fallback.}
When $S(t) \cap G(t) = \emptyset$---tight constraints leave no token that is both grammar-valid and semantically valid---na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
We enforce a \emph{grammar-first fallback}: if no semantically valid token survives grammar filtering, semantic masking is skipped and the grammar layer alone controls selection.
Structural integrity is a hard constraint; a type violation is a soft error detectable by downstream validation.

\paragraph{Constraint Tightness.}
We define the tightness of relation $r$ as:
%
\begin{equation}\label{eq:tightness}
  \kappa(r) = 1 - \frac{|\mathcal{V}(r)|}{|\mathcal{T}|^2},
\end{equation}
%
where $\mathcal{V}(r)$ is the set of valid type pairs and $\mathcal{T}$ the entity type vocabulary.
The mean tightness $\bar{\kappa} = \frac{1}{|\mathcal{R}|}\sum_{r} \kappa(r)$ characterizes ontology restrictiveness.
Tighter constraints eliminate more grammar-valid tokens at type-bearing positions, increasing fallback frequency and residual DR.
This dual-factor pattern---tightness $\times$ baseline model violation rate---is consistent with the cross-dataset results: SciERC ($\bar{\kappa}{=}0.333$, 24 valid pairs/relation) achieves 94--99\% DR reduction, while DocRED ($\bar{\kappa}{=}0.842$, 5.68 pairs) achieves 45--90\%, with the residual modulated by model-specific baselines (\S\ref{sec:cross-model}; quantitative analysis in Appendix~\ref{app:dual-factor}).

\paragraph{Non-Rectangularity and Sequential Masking.}
\label{sec:rectangularity}
% Data source: artifacts/rebuttal/w2_rectangularity_report.md
The sequential masking strategy---$\tau^h \in \operatorname{dom}(r)$, then $\tau^t \in \operatorname{range}(r, \tau^h)$---is necessary because real ontology type signatures are overwhelmingly non-rectangular: 0/7 SciERC and only 23/96 DocRED relations satisfy $\sigma(r) = \operatorname{dom}(r) \times \operatorname{range}(r)$.
Independent enforcement ($\tau^h \in \operatorname{dom}(r) \wedge \tau^t \in \operatorname{range}(r)$) would admit 33.3\% (SciERC) and 36.8\% (DocRED) spurious type pairs---on SciERC, 100\% of residual DR violations under full S1 are pairs that pass independent checks but violate $\sigma(r)$.
OntoCoDec's sequential approach achieves exact pair-based enforcement without explicit enumeration of $\sigma(r)$ at each step, exploiting the autoregressive left-to-right generation order.

\paragraph{Decidability Taxonomy.}
We classify ontology constraints by when sufficient information becomes available:
%
\begin{enumerate}[leftmargin=*,nosep]
  \item \textbf{Local}: require only the current token (entity/relation vocabulary membership). Handled by the grammar layer.
  \item \textbf{Prefix-decidable}: require the decoded prefix (domain/range constraints). Handled by the semantic layer via the entity registry.
  \item \textbf{Non-local}: require information not yet generated (forward coreference). Outside the scope of single-pass decoding; partially addressed by the two-pass strategy (S2, \S\ref{sec:s2}).
\end{enumerate}
```

---

## 6. section5_scierc_draft.tex

```latex
% Section 5 — SciERC Results (Draft)
% Data source: Phase 2 SciERC registry experiments
% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
% All numbers verified against registry 2026-05-14.

\subsection{Results on SciERC}
\label{sec:scierc-results}

Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
evaluating each constraint layer independently and in combination.
All experiments use Qwen3-8B in a zero-shot setting on 551 test documents
with identical prompts and decoding parameters;
only the active constraint layers differ.

% ──────────────────────────────────────────
%  Table: SciERC five-way ablation
% ──────────────────────────────────────────
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3.6pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}l rrrrr rr@{}}
\toprule
& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
& \multicolumn{2}{c}{\textbf{F1}} \\
\cmidrule(lr){2-6} \cmidrule(l){7-8}
\textbf{Mode}
  & DR\,$\downarrow$ & $\Delta$DR
  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
\midrule
Unconstrained
  & 15.37 & ---
  & 1.39  & 0.40
  & 0.08
  & 8.23  & 31.01 \\
Grammar
  & 14.84 & $\downarrow$3\%
  & \textbf{0} & \textbf{0}
  & 0.08
  & 8.23  & 30.98 \\
Semantic
  & 11.65 & $\downarrow$24\%
  & 1.51  & 0.40
  & 2.71
  & 8.15  & 31.01 \\
Full (S1)
  & \textbf{0.93} & $\downarrow$\textbf{94\%}
  & \textbf{0} & \textbf{0}
  & 9.90
  & \textbf{8.36} & 30.98 \\
Full (S2)
  & 0.97  & $\downarrow$94\%
  & \textbf{0} & \textbf{0}
  & 8.03
  & 8.03  & \textbf{31.90} \\
\bottomrule
\end{tabular}}%
\caption{Five-way ablation on SciERC (551 documents, Qwen3-8B, zero-shot).
DR: domain/range violation rate;
RV: relation vocabulary violation rate;
ET: entity type violation rate;
CF: cross-field consistency violation rate.
$\Delta$DR: relative DR reduction vs.\ the unconstrained baseline.
$\downarrow$\,/\,$\uparrow$: lower\,/\,higher is better.
Best per column in \textbf{bold} (CF excluded---see text).
F1 scores are multiplied by 100.
Statistical significance assessed via bootstrap resampling (10{,}000 iterations).}
\label{tab:scierc-ablation}
\end{table}

% ──────────────────────────────────────────
%  (a) Core result
% ──────────────────────────────────────────
\paragraph{Core result: DR elimination at zero F1 cost.}
The full two-layer constraint configuration (S1) reduces domain/range
violations from 15.37\% to 0.93\%, a 94\% relative reduction,
% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
while relation F1 moves from 8.23 to 8.36 ($+$0.13\,pp; bootstrap 95\% CI [$-$0.24, $+$0.58]\,pp, $p = 0.58$, 10{,}000 iterations).
% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
% bootstrap: delta=+0.13pp, CI=[-0.24,+0.58], p=0.5824
The difference is not statistically significant ($p = 0.58$), confirming
that constraint enforcement is F1-neutral on this dataset.
At the per-relation level, violations drop from 42.42\% to 2.82\% on
\textsc{Compare}, from 33.54\% to 1.21\% on \textsc{Feature-of}, and
reach 0\% on four of seven relation types
(\textsc{Conjunction}, \textsc{Hyponym-of}, \textsc{Part-of},
\textsc{Used-for}).
% phase2_scierc_full_s1 per_relation_dr: Compare=0.0282,
%   Feature-of=0.0121, Hyponym-of=0, Part-of=0, Used-for=0, Conjunction=0
However, full constraint enforcement elevates cross-field consistency
violations from 0.08\% to 9.90\%;
% phase2_scierc_unconstrained: CF=0.0008; phase2_scierc_full_s1: CF=0.099
we analyze this trade-off in Section~\ref{sec:discussion}.

% ──────────────────────────────────────────
%  (b) Grammar layer
% ──────────────────────────────────────────
\paragraph{Grammar layer: cost-free structural guarantees.}
Grammar-only constraints eliminate RV (1.39\%\,$\to$\,0\%) and ET (0.40\%\,$\to$\,0\%) with no F1 impact, while DR remains unchanged (15.37\%\,$\to$\,14.84\%), confirming that grammar constraints enforce structural validity but not semantic constraints.
% phase2_scierc_grammar_only: RV=0, ET=0, DR=0.1484, R-F1=0.0823

% ──────────────────────────────────────────
%  (c) Enabling dependency
% ──────────────────────────────────────────
\paragraph{Enabling dependency.}
Semantic-only constraints reduce DR by only 24\% (15.37\%\,$\to$\,11.65\%) and cannot eliminate RV (1.51\%) or ET (0.40\%).
% phase2_scierc_semantic_only: DR=0.1165, RV=0.0151, ET=0.004
The residual ET under semantic-only arises because the semantic mask constrains type tokens to relation-specific valid sets but cannot enforce vocabulary membership; occasionally the mask excludes the model's preferred valid-vocabulary type, forcing an OOV alternative.
Under full mode, the grammar layer's intersection prevents this, confirming the \emph{enabling dependency}: without grammar-enforced vocabulary, the semantic layer encounters OOV relation types with no domain/range rules.
Adding the grammar layer yields a further 92\% relative reduction (11.65\%\,$\to$\,0.93\%).
% phase2_scierc_full_s1: DR=0.0093

% ──────────────────────────────────────────
%  (d) S1 vs S2
% ──────────────────────────────────────────
\paragraph{S1 vs.\ S2.}
S2 achieves comparable DR (0.97\%) but lower R-F1 (8.03 vs.\ 8.36) with fewer triples (1{,}644 vs.\ 1{,}729) and does not resolve the CF trade-off (8.03\% vs.\ 9.90\%); we adopt S1 as the primary configuration.
% phase2_scierc_full_s2: DR=0.0097, R-F1=0.0803, CF=0.0803, triples=1644

% ──────────────────────────────────────────
%  (e) Composability with Fine-Tuning
%  exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
% ──────────────────────────────────────────
\paragraph{Composability with fine-tuning.}
\label{sec:composability}
Table~\ref{tab:composability} presents the composability matrix on SciERC for both Qwen3-8B and Llama-3.1-8B (zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1), testing whether OntoCoDec composes with task-specific fine-tuning across model families.
% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
%          w5_lora_scierc_unconstrained_eval, w5_lora_scierc_constrained_eval,
%          llama_scierc_unconstrained, llama_scierc_full_s1,
%          w5_llama_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_constrained_eval

For Qwen3-8B, fine-tuning alone raises R-F1 from 8.23 to 43.86 ($+$35.63\,pp) and E-F1 from 31.01 to 67.05 ($+$36.04\,pp), while reducing DR from 15.37\% to 1.95\% (87\% relative reduction).
% w5_lora_scierc_unconstrained_eval: DR=0.0195, R-F1=0.4386, E-F1=0.6705
The residual 1.95\% DR concentrates on tight-constraint relations: \textsc{Evaluate-for} (13.13\%), \textsc{Part-of} (5.77\%), and \textsc{Compare} (5.00\%) (per-relation breakdown in Appendix~\ref{app:lora-per-relation}).
Adding OntoCoDec eliminates the remaining DR entirely (1.95\%\,$\to$\,0\%) with R-F1 cost of $-$0.09\,pp (43.86\,$\to$\,43.77) and unchanged E-F1 (67.05).
% w5_lora_scierc_constrained_eval: DR=0, R-F1=0.4377, E-F1=0.6705, CF=0.0118

Llama-3.1-8B exhibits the same pattern.
Fine-tuning raises R-F1 from 2.68 to 45.45 ($+$42.77\,pp) and E-F1 from 23.56 to 67.76 ($+$44.20\,pp), while reducing DR from 13.34\% to 1.11\%.
% w5_llama_lora_scierc_unconstrained_eval: DR=0.0111, R-F1=0.4545, E-F1=0.6776
Adding OntoCoDec reduces DR by 92\% (1.11\%\,$\to$\,0.09\%) with R-F1 change of $+$0.02\,pp (45.45\,$\to$\,45.47) and unchanged E-F1 (67.76).
% w5_llama_lora_scierc_constrained_eval: DR=0.0009, R-F1=0.4547, E-F1=0.6776, CF=0.0046

On DocRED (96 relation types, document-level), the four-way ablation (Table~\ref{tab:ft-ablation}) reveals a nuanced pattern.
Unlike SciERC, unconstrained fine-tuned models retain non-zero RV violations (Qwen 0.27\%, Llama 0.15\%), indicating that the larger relation vocabulary is not fully internalized through training alone; the grammar layer eliminates these (RV\,$\to$\,0\%).
However, the grammar layer remains ineffective against DR: grammar-only DR is indistinguishable from unconstrained (Qwen 0.61\% vs.\ 0.76\%, Llama 0.51\% vs.\ 0.49\%; $|\Delta| < 0.2$\,pp).
The semantic layer provides the effective DR defense, reducing violations by 72\% for Qwen (0.76\%\,$\to$\,0.21\%) and 39\% for Llama (0.49\%\,$\to$\,0.30\%) in isolation.
The full system achieves near-complete DR elimination: Qwen 0.76\%\,$\to$\,0.01\% ($-$98.7\%), Llama 0.49\%\,$\to$\,0.20\% ($-$59.2\%), with R-F1 changes of $-$0.30\,pp and $+$0.51\,pp respectively.\footnote{Qwen DocRED all-set R-F1 change is $-$0.30\,pp (40.86\,$\to$\,40.56); excluding parse-failure documents (7.1\%\,$\to$\,8.5\%) yields $\Delta$R-F1 $+$0.03\,pp. We report all-set as primary.}
Parse failure rates on DocRED are non-trivial (7--8.5\%) due to document length but do not differentially affect constraint modes: excluding failed documents, $\Delta$R-F1 is within $\pm$0.1\,pp across all configurations.
% w5_qwen_docred_lora_constrained_eval: DR=0.01%, R-F1=40.56; w5_llama_docred_lora_constrained_eval: DR=0.20%, R-F1=44.23

Across both models and both datasets, fine-tuned + S1 yields DR\,$\leq$\,0.20\% with R-F1 change within $\pm$0.6\,pp, validating Claim~3: fine-tuning and OntoCoDec compose along orthogonal axes.
The four-way ablation consistently shows across all four model$\times$dataset settings (Appendix~\ref{app:ft-ablation}): grammar is a no-op for DR post-fine-tuning ($|\Delta\text{DR}| < 0.2$\,pp, 4/4 settings); the semantic layer alone reduces DR by 39--72\%; and full constraint enforcement drives DR to near-zero while preserving R-F1.

Two secondary observations support this interpretation.
First, CF interference drops substantially under fine-tuning for both models: Qwen from $+$9.82\,pp to $+$1.18\,pp, Llama from $+$6.32\,pp to $+$0.46\,pp,
% Qwen: ZS CF delta = 9.90-0.08 = 9.82pp, FT CF delta = 1.18-0 = 1.18pp
% Llama: ZS CF delta = 6.56-0.24 = 6.32pp, FT CF delta = 0.46-0 = 0.46pp
because fine-tuned per-slot type predictions are more consistent with the entity registry;
for Qwen, the residual 1.18\% traces to \textsc{Generic}$\leftrightarrow$X schema-level ambiguity (Appendix~\ref{app:cf-distribution}) rather than enforcement failure.
Second, in the zero-shot setting, S1 R-F1 impact is negligible for both models (Qwen $+$0.13\,pp, Llama $-$0.14\,pp),
% phase2_scierc_unconstrained: R-F1=0.0823; phase2_scierc_full_s1: R-F1=0.0836
% llama_scierc_unconstrained: R-F1=0.0268; llama_scierc_full_s1: R-F1=0.0254
confirming that constraint enforcement is F1-neutral regardless of base model quality.

\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lll rrrr r@{}}
\toprule
\textbf{Model} & \textbf{Setting} & \textbf{Mode}
  & \textbf{DR\,$\downarrow$} & \textbf{CF}
  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
  & \textbf{$\Delta$DR} \\
\midrule
\multirow{4}{*}{Qwen3-8B}
  & \multirow{2}{*}{Zero-shot}
    & Unconstr.\ & 15.37 & 0.08 & 8.23  & 31.01 & --- \\
  & & Full S1    &  0.93 & 9.90 & 8.36  & 30.98 & $\downarrow$94\% \\
\cmidrule(l){2-8}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
  & & Full S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
\midrule
\multirow{4}{*}{Llama-3.1-8B}
  & \multirow{2}{*}{Zero-shot}
    & Unconstr.\ & 13.34 & 0.24 & 2.68  & 23.56 & --- \\
  & & Full S1    &  0.08 & 6.56 & 2.54  & 23.49 & $\downarrow$99\% \\
\cmidrule(l){2-8}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
  & & Full S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
\bottomrule
\end{tabular}}%
\caption{Composability matrix on SciERC (551 documents):
zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1
for Qwen3-8B and Llama-3.1-8B.
$\Delta$DR: relative DR reduction vs.\ the same-row unconstrained baseline.
Fine-tuning alone leaves residual DR (1--2\%);
adding S1 reduces it to $\leq$\,0.09\% with R-F1 change within $\pm$0.1\,pp.
DocRED replication: Qwen DR $-$98.7\% ($-$0.30\,pp), Llama DR $-$59.2\% ($+$0.51\,pp).
F1\,$\times$100.}
\label{tab:composability}
\end{table}
```

---

## 7. section5_docred_draft.tex

```latex
% Section 5 — DocRED Results (compressed, 1450→~600 words)
% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
%          phase2_docred_semantic_only, phase2_docred_full_s1
% All numbers verified against registry 2026-05-14.

\subsection{Cross-Dataset Validation on DocRED}
\label{sec:docred-results}

Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED, a document-level RE benchmark with 96 Wikidata relation types---14$\times$ the ontology size of SciERC.
All experiments use Qwen3-8B zero-shot on 998 documents.

% ──────────────────────────────────────────
%  Table: DocRED four-way ablation
% ──────────────────────────────────────────
\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3.6pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}l rrrrr rr@{}}
\toprule
& \multicolumn{5}{c}{\textbf{Violation Rates (\%)}}
& \multicolumn{2}{c}{\textbf{F1}} \\
\cmidrule(lr){2-6} \cmidrule(l){7-8}
\textbf{Mode}
  & DR\,$\downarrow$ & $\Delta$DR
  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
\midrule
Unconstrained
  & 18.46 & ---
  & 29.66 & 2.48
  & 0.10
  & 7.74  & 58.15 \\
Grammar
  & 26.17 & $\uparrow$42\%
  & \textbf{0.03} & \textbf{0}
  & 0.07
  & \textbf{8.31}  & \textbf{59.38} \\
Semantic
  & 13.84 & $\downarrow$25\%
  & 29.87 & 4.22
  & 1.05
  & 7.70  & 57.81 \\
Full (S1)
  & \textbf{10.21} & $\downarrow$\textbf{45\%}
  & \textbf{0.03} & \textbf{0}
  & 2.57
  & 8.23  & 59.37 \\
\bottomrule
\end{tabular}}%
\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
$\Delta$DR: relative change vs.\ unconstrained.
Best per column in \textbf{bold} (CF excluded).
F1 $\times$100. Bootstrap significance: R-F1 $+$0.50\,pp ($p < 0.001$).}
\label{tab:docred-ablation}
\end{table}

% exp_ids: phase2_docred_unconstrained, phase2_docred_full_s1
\paragraph{Core result.}
Full S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates ET (2.48\%\,$\to$\,0\%), and near-eliminates RV (29.66\%\,$\to$\,0.03\%; the residual 5 triples arise from partial JSON recovery where the grammar FSM completes a structurally valid but relation-name-truncated triple).
Relation F1 improves from 7.74 to 8.23 ($+$0.50\,pp; bootstrap 95\% CI [$+$0.23, $+$0.81], $p < 0.001$), attributable to grammar-layer elimination of 5{,}189 OOV relation predictions counted as false positives.
CF increases modestly (0.10\%\,$\to$\,2.57\%), lower than SciERC's 9.90\%.

% exp_ids: phase2_docred_grammar_only
\paragraph{Grammar layer surfaces latent violations.}
Grammar-only constraints eliminate RV and ET but \emph{increase} DR from 18.46\% to 26.17\% ($+$42\%).
This counter-intuitive result has a structural explanation: the unconstrained baseline's 29.66\% OOV relation triples cannot be evaluated for DR (no schema entry exists); grammar enforcement assigns these triples valid relation names whose domain/range rules the associated entity types frequently violate.
The grammar layer thus \emph{reveals} latent type incompatibilities, directly motivating the semantic layer.

% exp_ids: phase2_docred_semantic_only, phase2_docred_full_s1
\paragraph{Enabling dependency.}
Semantic-only constraints reduce DR by only 25\% (18.46\%\,$\to$\,13.84\%) while failing to eliminate RV (29.87\%) or ET (4.22\%).
Full S1 achieves a further 26\% relative reduction over semantic-only (13.84\%\,$\to$\,10.21\%), replicating the enabling dependency from SciERC: without grammar-enforced vocabulary, the semantic layer encounters OOV relation types for which no domain/range rules exist.

% exp_ids: phase2_docred_full_s1, llama_docred_full_s1
\paragraph{Zero-shot F1 context.}
Zero-shot R-F1 values (6--8\%) reflect zero-shot RE difficulty; supervised SOTA achieves 49--53\% on SciERC~\citep{zhong2021frustratingly}.
F1 serves primarily as a control variable verifying constraint enforcement preserves extraction quality, not as an optimization target.

\paragraph{Constraint tightness governs enforcement ceiling.}
The residual DR on DocRED (10.21\%) exceeds SciERC (0.93\%) due to per-relation \emph{constraint tightness}: DocRED relations average 5.68 valid type pairs ($\bar{\kappa}{=}0.842$) vs.\ 24 on SciERC ($\bar{\kappa}{=}0.333$).
Tighter constraints produce narrower grammar$\cap$semantic mask intersections, increasing fallback frequency---the aggregate fallback rate (10.2\%; 1{,}770/17{,}341 triples) closely tracks residual DR (10.21\%), confirming a near-bijection between fallback events and residual violations.
Crucially, tightness interacts with the model's baseline violation profile: Qwen's high RV (29.66\%) causes grammar enforcement to surface many latent DR violations, yielding 10.21\% residual DR; Llama's lower RV (16.03\%) limits this surfacing, achieving 2.55\% residual ($\downarrow$90.2\%) on the same ontology (\S\ref{sec:cross-model}).
This dual-factor pattern---tightness $\times$ baseline RV---is consistent with cross-dataset and cross-model DR reduction differences.
We omit S2 on DocRED because S1 already achieves near-complete RV/ET elimination and the two-pass overhead is less justified when residual DR is dominated by fallback events rather than forward coreference.
```

---

## 8. section5_crossmodel_draft.tex

```latex
% Section 5 — Cross-Model Validation (compressed, 830→~400 words)
% exp_ids: phase2_scierc_unconstrained, phase2_scierc_full_s1,
%          phase2_docred_unconstrained, phase2_docred_full_s1,
%          llama_scierc_unconstrained, llama_scierc_full_s1,
%          llama_docred_unconstrained, llama_docred_full_s1

\subsection{Cross-Model Validation}
\label{sec:cross-model}

We replicate the full S1 configuration with Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 under identical prompts, decoding parameters, and evaluation.
Table~\ref{tab:cross-model} summarizes results across all three models.
Mistral serves as a third zero-shot verification point confirming model-agnosticism; composability evaluation (\S\ref{sec:composability}) uses LoRA fine-tuning which requires domain-specific training data available only for Qwen and Llama.

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
Parse failures: Qwen DocRED 12$\to$11 (S1 1.10\%), Llama DocRED 68$\to$91; others $\leq$1.
$^\dagger$Mistral's poor zero-shot type calibration leads to pervasive entity type assignment inconsistencies across triples.
F1 $\times$100.}
\label{tab:cross-model}
\end{table}

\paragraph{Model-agnostic structural guarantees.}
RV and ET violations are eliminated ($\leq$0.03\%) for all three models on both datasets, confirming that grammar-layer enforcement depends on the decoding mechanism, not model-specific generation patterns.

% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, phase2_docred_full_s1, llama_docred_full_s1, mistral_scierc, mistral_docred
\paragraph{DR reduction generalizes across models.}
SciERC DR drops 94\% (Qwen), 99\% (Llama), 76\% (Mistral); DocRED DR drops 45\% (Qwen), 90\% (Llama), 42\% (Mistral).
Mistral exhibits the highest baseline DR (56--57\%) due to poor zero-shot type calibration, yet still benefits substantially.
R-F1 is preserved or improves in five of six settings; on DocRED, gains are significant for Qwen ($+$0.50\,pp, $p{<}0.001$) and Llama ($+$0.29\,pp, $p{=}0.013$).

\paragraph{Cross-model DR asymmetry.}
Llama's higher DR reduction reflects lower baseline RV (16.03\% vs.\ 29.66\% on DocRED): with fewer OOV relations to surface, grammar enforcement exposes fewer latent type incompatibilities, yielding residual DR of 2.55\% vs.\ Qwen's 10.21\%.
Llama's per-relation DR shows no correlation with tightness ($\rho{=}0.069$, $p{=}0.52$; Appendix~\ref{app:llama-per-relation}), confirming uniform enforcement once baseline RV is low.
CF direction depends on baseline calibration: S1 introduces CF for well-calibrated Qwen and Llama (up to 12.02\%; \S\ref{sec:discussion}), while reducing CF for poorly-calibrated Mistral (56.87\%\,$\to$\,1.27\%) by constraining type assignments to schema-valid values.
```

---

## 9. section5_runtime.tex

```latex
% Section 5 — Runtime Analysis
% Data source: DocRED latency profiling (exp_id: docred_latency_profiling)
% Qwen3-8B, same single-GPU server, controlled 4-way ablation.

\subsection{Runtime Overhead}
\label{sec:runtime}

Table~\ref{tab:runtime} reports per-document inference time for each constraint layer combination on both datasets (Qwen3-8B, same GPU).

\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}l rr rr@{}}
\toprule
& \multicolumn{2}{c}{\textbf{SciERC (7 rels)}}
& \multicolumn{2}{c}{\textbf{DocRED (96 rels)}} \\
\cmidrule(lr){2-3} \cmidrule(l){4-5}
\textbf{Mode} & Avg (s) & Overhead & Avg (s) & Overhead \\
\midrule
Unconstrained & 2.587 & --- & 21.023 & --- \\
Grammar       & 2.631 & $+$1.7\% & 21.366 & $+$1.6\% \\
Semantic      & 2.618 & $+$1.2\% & 21.912 & $+$4.2\% \\
Full (S1)     & 2.647 & $+$2.3\% & 22.147 & $+$5.4\% \\
\bottomrule
\end{tabular}
\caption{Per-document inference time by constraint layer (Qwen3-8B, same GPU).
Grammar compile time: 0.044\,s (one-time, amortized to zero).
Full-mode overhead is sub-additive (DocRED: 1.6\%$+$4.2\%$=$5.8\% expected vs.\ 5.4\% observed).}
\label{tab:runtime}
\end{table}

Grammar-layer overhead is consistent across datasets ($+$1.6--1.7\%), independent of schema complexity.
Semantic-layer overhead scales with the number of relation types (SciERC 7 types: $+$1.2\%; DocRED 96 types: $+$4.2\%), reflecting increased domain-range lookup frequency.
Full-mode overhead is sub-additive on both datasets because the two layers share token-set computation.
Even in the most complex setting (DocRED, 96 relations), total overhead is $+$5.4\%---practically negligible.
Under fine-tuning, S1 overhead drops further to $+$2.3\% (61\,ms/doc; Appendix~\ref{app:ft-latency}).
```

---

## 10. paper_tables_draft.tex

```latex
% =============================================================
% Paper Tables Draft — Schema-Semantic Constrained IE
% Generated from experiment registry, 2026-05-14
% Model: Qwen3-8B (zero-shot), all percentages to 1 d.p.
% =============================================================

% ------------------------------------------------------------
% Table 1: SciERC 5-way Ablation
% ------------------------------------------------------------
\begin{table}[t]
\centering
\caption{Ablation study on SciERC test set (551 samples, Qwen3-8B zero-shot).
DR = Domain/Range violation rate, RV = Relation Vocabulary violation rate,
ET = Entity Type violation rate, CF = Cross-Field consistency violation rate.
$\downarrow$: lower is better; $\uparrow$: higher is better.
$\Delta$DR shows the absolute change (pp) relative to the unconstrained baseline.}
\label{tab:scierc-ablation}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{l cccc cc c}
\toprule
Mode & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ & R-F1$\uparrow$ & E-F1$\uparrow$ & $\Delta$DR (pp) \\
\midrule
Unconstrained      & 15.4 & 1.4          & 0.4          & \textbf{0.1} & 8.2          & 31.0          & ---                    \\
Grammar-only       & 14.8 & \textbf{0.0} & \textbf{0.0} & \textbf{0.1} & 8.2          & 31.0          & $-$0.5                 \\
Semantic-only      & 11.7 & 1.5          & 0.4          & 2.7          & 8.2          & 31.0          & $-$3.7                 \\
Full (S1)          & \textbf{0.9} & \textbf{0.0} & \textbf{0.0} & 9.9  & \textbf{8.4} & 31.0          & \textbf{$-$14.4}       \\
Full (S2)          & 1.0  & \textbf{0.0} & \textbf{0.0} & 8.0          & 8.0          & \textbf{31.9} & $-$14.4                \\
\bottomrule
\end{tabular}%
}
\vspace{2pt}
{\footnotesize
\textit{Exp IDs:}
\texttt{phase2\_scierc\_unconstrained},
\texttt{phase2\_scierc\_grammar\_only},
\texttt{phase2\_scierc\_semantic\_only},
\texttt{phase2\_scierc\_full\_s1},
\texttt{phase2\_scierc\_full\_s2}.
}
\end{table}


% ------------------------------------------------------------
% Table 2: Per-Relation DR Violation Analysis (SciERC)
% ------------------------------------------------------------
\begin{table}[t]
\centering
\caption{Per-relation Domain/Range violation rates on SciERC:
Unconstrained baseline vs.\ Full (S1) constrained decoding.
$n$ = predicted triples of that relation type (unconstrained).
$\Delta$ = absolute change in violation rate (pp).}
\label{tab:scierc-per-relation-dr}
\begin{tabular}{l r rr r}
\toprule
Relation & $n$ & Uncon.\ (\%) & S1 (\%) & $\Delta$ (pp) \\
\midrule
Compare      &  66 & 42.4 &  2.8 & $-$39.6 \\
Feature-of   & 486 & 33.5 &  1.2 & $-$32.3 \\
Part-of      &  72 & 25.0 & \textbf{0.0} & $-$25.0 \\
Evaluate-for & 133 & 24.1 &  5.8 & $-$18.3 \\
Hyponym-of   & 124 & 14.5 & \textbf{0.0} & $-$14.5 \\
Used-for     & 787 &  0.8 & \textbf{0.0} & $-$0.8  \\
Conjunction  &  32 &  0.0 & \textbf{0.0} &    0.0  \\
\midrule
\textit{Overall} & \textit{1724} & \textit{15.4} & \textit{0.9} & \textit{$-$14.4} \\
\bottomrule
\end{tabular}
\vspace{2pt}
{\footnotesize
\textit{Exp IDs:}
\texttt{phase2\_scierc\_unconstrained} (Uncon.),
\texttt{phase2\_scierc\_full\_s1} (S1).
}
\end{table}


% ------------------------------------------------------------
% Table 3: DocRED Phase 0 — Prompt-level Intervention
% ------------------------------------------------------------
\begin{table}[t]
\centering
\caption{Prompt-level intervention on DocRED dev set (998 documents, 96 relation types, Qwen3-8B zero-shot).
Comparing minimal prompt vs.\ schema-informed prompt that explicitly lists valid relation types
and domain/range constraints.}
\label{tab:docred-phase0}
\begin{tabular}{l cccc}
\toprule
Mode & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & JSON Parse$\uparrow$ \\
\midrule
Minimal          & 18.5          & 29.7          & 2.5          & \textbf{96.4} \\
Schema-informed  & \textbf{12.8} & \textbf{18.4} & \textbf{0.2} & 94.5          \\
\midrule
$\Delta$         & $-$5.7        & $-$11.3       & $-$2.3       & $-$1.9        \\
\bottomrule
\end{tabular}
\vspace{2pt}
{\footnotesize
\textit{Exp IDs:}
\texttt{mvp\_phase0\_violation\_rate\_docred} (Minimal),
\texttt{mvp\_phase0\_docred\_schema} (Schema-informed).
}
\end{table}


% ------------------------------------------------------------
% Table 4: Cross-dataset Violation Comparison
% ------------------------------------------------------------
\begin{table}[t]
\centering
\caption{Cross-dataset comparison of ontology violation rates.
Baseline = unconstrained Qwen3-8B zero-shot; S1 = Grammar + Semantic constrained decoding.}
\label{tab:cross-dataset}
\begin{tabular}{l c ccc cc}
\toprule
Dataset & \#Rels & DR\textsubscript{base} & RV\textsubscript{base} & ET\textsubscript{base} & DR\textsubscript{S1} & $\Delta$DR (pp) \\
\midrule
SciERC & 7  & 15.4 & 1.4  & 0.4 & 0.9          & $-$14.4 \\
DocRED & 96 & 18.5 & 29.7 & 2.5 & 10.21 & $-$8.3 \\
\bottomrule
\end{tabular}
\vspace{2pt}
{\footnotesize
\textit{Exp IDs:}
SciERC base = \texttt{phase2\_scierc\_unconstrained},
SciERC S1 = \texttt{phase2\_scierc\_full\_s1},
DocRED base = \texttt{mvp\_phase0\_violation\_rate\_docred},
DocRED S1 = \texttt{phase2\_docred\_full\_s1}.
}
\end{table}
```

---

## 11. appendix_sampling_table.tex

```latex
\begin{table}[h]
\centering
\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding.}
\label{tab:sampling-robustness}
\begin{tabular}{llcccccc}
\toprule
Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
\midrule
\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.82 & 30.98 & 8.36 \\
& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
\midrule
\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
\bottomrule
\end{tabular}
\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
\end{table}
```

---

## 12. appendix_discussion.tex

```latex
% Appendix B — Extended Discussion
% Contains discussion paragraphs moved from the main text during compression.

\section{Extended Discussion}\label{app:discussion}

%%% CF Dual Mechanism %%%
% exp_ids: phase2_scierc_full_s1, llama_scierc_full_s1, llama_docred_full_s1

\paragraph{CF Dual Mechanism.}
CF violations arise from two distinct mechanisms:
(1)~\emph{Registry override}: the semantic constraint forces a domain-compatible type that conflicts with the entity's previously registered type.
The entity appears in multiple relations with different type requirements, and the per-relation mask selects the locally valid type without consulting prior assignments.
(2)~\emph{Grammar-first fallback} (\S\ref{sec:interaction}): when the semantic mask conflicts with all grammar-valid tokens, the semantic layer is dropped entirely, allowing the grammar layer to generate any structurally valid type---which may differ from the entity's registered type.

These mechanisms have sharply different model profiles.
Qwen3-8B triggers zero grammar-first fallbacks across all experiments, attributing 100\% of its CF violations to registry override.
Llama-3.1-8B, by contrast, triggers 5{,}882 fallbacks on SciERC (10.7 per document) and 57{,}825 on DocRED (63.8 per document), making grammar-first fallback the dominant CF source.
This asymmetry is consistent with the cross-model CF gap: Qwen achieves CF\,=\,2.57\% on DocRED vs.\ Llama's 12.02\%, despite both using identical constraint configurations.
The difference traces to Llama's less calibrated type predictions, which more frequently conflict with the semantic mask's valid set, triggering fallback.

%%% Fallback Behavior and Effective Coverage %%%
% exp_ids: cf_fallback_ablation_scierc (final data)

\paragraph{Fallback Behavior and Effective Coverage.}
\label{app:fallback-coverage}
The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
\emph{Grammar-first fallback} (36.6\% of type-bearing positions on SciERC) occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations---these events account for the residual DR that persists after constraint enforcement.
\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.

We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
On SciERC, this yields 63.4\% coverage---at 63.4\% of type-bearing positions, the semantic layer actively constrains generation.
This metric directly quantifies the enabling dependency (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).

%%% CF-DR Trade-off Analysis %%%
% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)

\paragraph{CF-DR Trade-off Analysis.}
\label{app:cf-dr-tradeoff}

CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.

\begin{table}[t]
\centering
\small
\begin{tabular}{@{}l rrrr@{}}
\toprule
\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
\midrule
Full S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
\midrule
$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
\bottomrule
\end{tabular}
\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: grammar-first fallback rate at type-bearing positions.}
\label{tab:cf-dr-tradeoff}
\end{table}

The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
The grammar-first fallback is triggered at 36.64\% of type-bearing positions, indicating that this conflict is structural, not a tunable hyperparameter.

We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
Within this design, the current full S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use---a distinction the per-slot decoder cannot resolve without document-level coreference.

Two complementary paths can lower CF without re-routing it to DR.
(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.

%%% Dual-Factor Quantitative Analysis %%%
% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
%          llama_scierc_full_s1, llama_docred_full_s1

\paragraph{Dual-Factor Quantitative Analysis.}
\label{app:dual-factor}

Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for all four model$\times$dataset configurations.
A linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$; we do not report a $p$-value given the small sample size).
The strong fit is consistent with the dual-factor pattern described in \S\ref{sec:composition}: configurations with higher tightness and higher baseline violation rate exhibit proportionally higher residual DR after constraint enforcement.
The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.

\begin{figure}[t]
\centering
\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
\caption{Residual DR vs.\ $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ across four model$\times$dataset configurations.
Linear fit: $y = 0.366x - 0.138$, $R^2 = 0.886$.}
\label{fig:dual-factor-scatter}
\end{figure}

%%% Dataset-Dependent F1 Impact (moved from §7) %%%
% exp_ids: d012_bootstrap_ci (DocRED +0.50pp p<0.001, SciERC +0.13pp p=0.58),
%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)

\paragraph{Dataset-Dependent F1 Impact.}
The divergence in F1 significance between DocRED ($+$0.50\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.50\,pp), confirming that F1 gain magnitude is proportional to baseline OOV rate.
% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)

%%% Paragraph 1: Low F1 Practical Significance %%%
% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)

\paragraph{Practical Significance of Zero-Shot F1.}
Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary---Phase~0 analysis confirms that even well-prompted models exhibit non-trivial violation rates (15.37\% DR on SciERC, 18.46\% on DocRED).
% exp_ids: phase0_scierc_unconstrained, phase2_docred_unconstrained
In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
The contribution of this work is the constraint enforcement method itself; the zero-shot setting isolates its effect from confounds introduced by task-specific fine-tuning.

%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)

\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
Post-hoc filtering---generating triples without constraints, then removing schema-violating predictions---yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
However, this precision gain comes at substantial cost.
On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions), reducing recall from 9.46\% to 8.40\%.
% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.

%%% CF Violation Distribution %%%
% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)

\paragraph{Cross-Field Violation Distribution.}
\label{app:cf-distribution}

Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC full S1 (245 CF violations, all pairwise---no mention triggered $\geq$3 types).
Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially---a distinction the per-slot constrained decoder cannot resolve without document-level coreference.

The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets, confirming that CF violations are a side-effect of per-slot type commitment rather than a model deficiency.

\begin{table}[t]
\centering
\small
\begin{tabular}{@{}lr r@{}}
\toprule
\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
\midrule
Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
Generic $\leftrightarrow$ Material & 35 & 14.3 \\
Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
Method $\leftrightarrow$ Task & 20 & 8.2 \\
Material $\leftrightarrow$ Method & 17 & 6.9 \\
OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
\midrule
10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
\midrule
\textbf{Total} & \textbf{245} & 100.0 \\
\bottomrule
\end{tabular}
\caption{CF violation distribution on SciERC full S1 (Qwen3-8B, 551 documents).
All 245 violations are pairwise conflicts.
Conflicts involving \textsc{Generic} account for 63.3\%.}
\label{tab:cf-distribution}
\end{table}

%%% Per-Relation DR Elimination under Fine-Tuning %%%
% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1

\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
\label{app:lora-per-relation}

Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
Adding OntoCoDec constraints eliminates all remaining violations across all relations.
One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.

\begin{table}[t]
\centering
\small
\begin{tabular}{@{}l r rr rr@{}}
\toprule
& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
\cmidrule(lr){3-4} \cmidrule(l){5-6}
\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
\midrule
Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
\bottomrule
\end{tabular}
\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
$\kappa$: constraint tightness; $n$: predicted triple count.
Used-for gains one triple from Evaluate-for redirection.}
\label{tab:lora-per-relation}
\end{table}

%%% Fine-Tuned Four-Way Ablation %%%
% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*

\paragraph{Fine-Tuned Four-Way Ablation.}
\label{app:ft-ablation}

Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.

\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lll rrrrr rr@{}}
\toprule
\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
\midrule
\multirow{8}{*}{SciERC}
  & \multirow{4}{*}{Qwen3-8B}
    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
  & & Full S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
  \cmidrule(l){2-10}
  & \multirow{4}{*}{Llama-3.1-8B}
    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
  & & Full S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
\midrule
\multirow{8}{*}{DocRED}
  & \multirow{4}{*}{Qwen3-8B}
    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
  & & Semantic      & 0.21 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.89 \\
  & & Full S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
  \cmidrule(l){2-10}
  & \multirow{4}{*}{Llama-3.1-8B}
    & Unconstrained & 0.49 & 0.15 & 0.00 & ---  & 2.30 & 83.93 & 43.72 \\
  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.77 \\
  & & Semantic      & 0.30 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.90 \\
  & & Full S1       & \textbf{0.20} & 0.00 & 0.00 & 0.26 & 2.51 & 85.23 & 44.23 \\
\bottomrule
\end{tabular}}%
\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
DR/RV/ET/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.
Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
Semantic layer is the sole effective DR defense, providing 39--72\% reduction.
F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED full vs.\ unconstrained).}
\label{tab:ft-ablation}
\end{table}

The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 39--72\% across all settings (SciERC: Qwen $-$69\%, Llama $-$41\%; DocRED: Qwen $-$72\%, Llama $-$39\%).
Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.20\% in all 4 settings), confirming that even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate---specifically on tight-constraint relations where the valid type-pair space is small.
F1 cost is negligible: the maximum R-F1 decrease across all 16 model$\times$dataset$\times$mode combinations is $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained), attributable to parse failure increase (7.11\%\,$\to$\,8.52\%) rather than constraint-induced extraction degradation.

%%% Residual DR Error Analysis (Fine-Tuned) %%%
% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*

\paragraph{Residual DR Error Analysis.}
\label{app:residual-dr-analysis}

Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ full S1), only 36 domain/range violations remain.
Manual inspection reveals four root causes:

\begin{enumerate}[nosep,leftmargin=*]
\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
\end{enumerate}

Two dataset-specific patterns emerge.
Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps---the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 7 entity types) compared to Qwen, which achieves near-zero residual.
The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), confirming that the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.

%%% Post-Hoc Filtering Comparison (Extended) %%%
% exp_ids: posthoc_*_zs, posthoc_*_ft

\paragraph{Post-Hoc Filtering: Extended Comparison.}
\label{app:posthoc-extended}

Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.

\begin{table}[t]
\centering
\small
\setlength{\tabcolsep}{3pt}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lll rrr l@{}}
\toprule
\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
\midrule
\multirow{6}{*}{ZS}
  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
\midrule
\multirow{4}{*}{FT}
  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
  & Qwen    & DocRED & 1.03 & 41.11 & 40.56 & ph \\
  & Llama   & DocRED & 0.64 & 43.92 & 44.23 & cd \\
\bottomrule
\end{tabular}}%
\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
F1 $\times$100.}
\label{tab:posthoc-extended}
\end{table}

The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
OntoCoDec's advantage thus scales with violation severity---precisely when constraints are most needed, post-hoc filtering is most destructive.
Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).

%%% FT Latency %%%

\paragraph{Fine-Tuned Latency Profiling.}
\label{app:ft-latency}
Under LoRA fine-tuning (Qwen3-8B, SciERC, 100 documents, RTX PRO 6000), per-document inference times are: unconstrained 2.594\,s, grammar-only 2.637\,s ($+$1.7\%), semantic-only 2.625\,s ($+$1.2\%), full S1 2.655\,s ($+$2.3\%, $p{<}0.0001$ paired $t$-test).
The combined overhead is sub-additive (2.3\% $<$ 1.7\%$+$1.2\%) because fine-tuned models produce fewer grammar-first fallback events (the semantic mask conflicts with grammar-valid tokens less often when per-slot predictions are better calibrated), reducing the number of active masking calls per document.
Compared to the zero-shot regime (Table~\ref{tab:runtime}), absolute overhead decreases from seconds-scale to milliseconds-scale: the fine-tuned model generates shorter, more structured outputs, compressing total generation time from 8.69\,s to 2.594\,s per document.

%%% Fuzzy Relation Matching %%%

\paragraph{Relation Matching Protocol.}
\label{app:fuzzy-matching}
Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
```

---

## 13. appendix_llama_per_relation.tex

```latex
% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
% exp_ids: llama_docred_unconstrained, llama_docred_full_s1

\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}

Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under full S1 constraints.
The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, indicating stronger baseline vocabulary compliance.
% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
Full S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)

\begin{table}[h]
\centering
\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under full S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
\label{tab:llama-per-relation-dr}
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}llrrr@{}}
\toprule
Relation & PID & Triples & DR Violations & DR Rate (\%) \\
\midrule
dissolved/demolished & P576 & 73 & 24 & 32.9 \\
followed by          & P156 & 117 & 24 & 20.5 \\
unemployment rate    & P1198 & 15 & 3 & 20.0 \\
end time             & P582 & 130 & 21 & 16.2 \\
instance of          & P31  & 290 & 37 & 12.8 \\
product/material produced & P1056 & 98 & 11 & 11.2 \\
location of formation & P740 & 81 & 8 & 9.9 \\
head of state        & P35  & 41  & 3  & 7.3 \\
applies to jurisdiction & P1001 & 637 & 45 & 7.1 \\
conflict             & P607 & 453 & 30 & 6.6 \\
\bottomrule
\end{tabular}}
\end{table}
% exp_ids: llama_docred_full_s1

Compared with Qwen, which retains a 10.21\% residual DR under full S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's residual DR on the same relations is markedly lower---P1198 reaches only 20.0\% and no relation-level fallback concentration comparable to Qwen is observed.
% exp_ids: llama_docred_full_s1, qwen_docred_full_s1
The substantially lower residual DR for Llama (2.55\% vs.\ Qwen's 10.21\%) on the same ontology confirms that constraint tightness alone does not determine enforcement effectiveness: the model's baseline vocabulary compliance (RV) modulates the fraction of triples eligible for semantic-layer enforcement.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e402e11d-4bf7-4fc0-820a-96048565af20",
  "isSidechain": true,
  "agentId": "aae59a1bf14556cf7",
  "requestId": "req_011Cb7AKmYiScpg3Mn7Qe9uq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "012148a0-932f-4104-9c42-22d39161fca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "f80c60c0-3051-47f4-a420-937bb8ca84ad",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvMfQnqdnB1qGSq322Jixi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11548,
      "cache_read_input_tokens": 36802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11548,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
