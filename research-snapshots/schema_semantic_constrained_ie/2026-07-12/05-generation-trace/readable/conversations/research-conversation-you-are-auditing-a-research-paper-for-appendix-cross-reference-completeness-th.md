# Research conversation: You are auditing a research paper for appendix cross-reference completeness. The paper is at `/home/ubuntu/.agent-ml-res

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 99
- **Recorded user turns:** 1
- **Tool calls:** 42
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a3140ddb0efc16ba7.jsonl`
- **Structured JSON:** [`04b30180d81726f3bcfd.json`](../../sessions/04/04b30180d81726f3bcfd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

99 recorded events

### User

_source line 1 · 2026-05-24T05:01:42.151Z_

You are auditing a research paper for appendix cross-reference completeness. The paper is at `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`.

## Task

### Step 1: List all appendix sections
Read `main.tex` to find the appendix structure (which files are \input'd after \appendix). Then read each appendix .tex file to get its \section or \subsection title and \label.

### Step 2: For each appendix section, check if the main body references it
The main body files are: abstract.tex, section1_introduction_draft.tex, section2_background.tex, section3_method_draft.tex, section3_violation_landscape.tex, section4_composition_draft.tex, section5_scierc_draft.tex, section5_docred_draft.tex, section5_runtime.tex, section5_wikievents_draft.tex, section5_crossmodel_draft.tex, section6_related_work.tex, section7_conclusion_compressed.tex, main.tex (for limitations etc.)

For each appendix label (e.g., app:xxx), grep ALL .tex files in the paper directory for references like `\ref{app:xxx}` or `Appendix~\ref{app:xxx}`. Distinguish between:
- References FROM main body TO appendix (these are what we want)
- References FROM other appendix sections TO the same appendix (cross-appendix refs)
- Self-references within the appendix file

Mark each appendix as:
- ✅ Referenced from main body
- ❌ NOT referenced from main body (orphan)

### Step 3: For orphan appendices
Assess: Does it contain content reviewers would want? Suggest where in the main body to add a pointer, or suggest deletion.

### Step 4: Reverse check
Search the main body files for ALL `\ref{app:` patterns and verify each target label actually exists in some appendix file. Report any broken references.

Also check for `\ref{tab:` and `\ref{fig:` patterns in main body that point to tables/figures defined in appendix files — verify those exist too.

### Output format
```
## Appendix Sections
1. [file] Section Title (label: app:xxx) — ✅ main body refs: [list locations] / ❌ orphan
...

## Orphan Appendices
- app:xxx — [assessment and recommendation]

## Broken References (main body → nonexistent appendix)
- [location] \ref{app:xxx} — NOT FOUND
```

Be thorough — read every file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "838b4d42-d3be-444e-a33d-35b1fea09485",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T05:01:42.161Z_

```json
{
  "parentUuid": "838b4d42-d3be-444e-a33d-35b1fea09485",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f5363db6-a6ca-4ef2-9590-1a95a4a57ade",
  "timestamp": "2026-05-24T05:01:42.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

---

### Assistant

_source line 3 · 2026-05-24T05:01:45.327Z_



I'll start by reading `main.tex` to understand the paper structure, then systematically check all cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5363db6-a6ca-4ef2-9590-1a95a4a57ade",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojV34dXSGMY1Q6XPRj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a87e4519-22de-4259-b73a-a13c9b030245",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o2MD3LdgvJXGik1uTWfni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30002,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30002,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-24T05:01:45.844Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EtYLPL9UzTQdQNGXMRNMve`</summary>

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
  "parentUuid": "a87e4519-22de-4259-b73a-a13c9b030245",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojV34dXSGMY1Q6XPRj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d8c7be1-c21c-4804-8ca6-60e498d2a47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o2MD3LdgvJXGik1uTWfni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30002,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30002,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 5 · 2026-05-24T05:01:45.863Z_

<details><summary>↩ Tool result · `toolu_01EtYLPL9UzTQdQNGXMRNMve`</summary>

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
71	CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impact is model-dependent (S1 introduces CF for calibrated models but reduces it for poorly-calibrated ones).
72	Global entity-level type consensus during decoding offers the most direct path to resolving CF.
73	Entity-first generation order is an architectural constraint: the grammar enforces entities before relations, ensuring the registry is populated before type checks; alternative orderings would require deferred constraint evaluation.
74	Residual DR under fine-tuning (36 violations total) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors (28\%); schema gaps arise from training-data-derived constraints that may not cover all valid type pairs (Appendix~\ref{app:residual-dr-analysis}).
75	Our empirical constraints are derived from training data type-pair co-occurrences; schema evolution (adding new entity types or relations) would require constraint regeneration, and the 0.6--1.0\% uncovered valid type pairs suggest potential over-restriction during transition periods.
76	We do not decompose CF violations into first-seen cascading errors versus legitimate type ambiguity; this decomposition requires gold entity type annotations at the mention level, which SciERC provides only at the entity level.
77	Post-hoc type consensus re-voting eliminates all CF in our experiments, at the cost of DR regression (up to $+$9.38\,pp on DocRED zero-shot; Appendix~\ref{app:tcr}); integrating consensus into the decoding loop remains future work.
78	
79	\paragraph{Evaluation coverage.}
80	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on two 8B-class models (full datasets) and one 70B-class model (SciERC full, DocRED 200-document subset).
81	Scaling to smaller models has not been verified; the schema restrictiveness--enforcement difficulty relationship is based on three schemas.
82	Evaluation is limited to one fine-tuning method (LoRA); LoRA hyperparameters were tuned on SciERC and transferred to DocRED without dataset-specific optimization, which may underestimate DocRED potential.
83	WikiEvents fine-tuning is preliminary ($n{=}20$); DocRED uses the development set (test annotations unavailable).
84	All main experiments use greedy decoding; beam search compatibility is confirmed but comprehensive evaluation across all configurations remains future work (Appendices~\ref{app:sampling},~\ref{app:beam-search}).
85	Composability with training-based schema-aware systems (e.g., GoLLIE) is architecturally supported but not empirically validated in this work.
86	
87	\paragraph{Engineering considerations.}
88	Our approach requires access to model logits, excluding API-only models; continuation masking assumes distinguishable token prefixes per type name, which may be challenged by morphologically similar types (e.g., \texttt{Protein} vs.\ \texttt{Protein\_Complex}; Appendix~\ref{app:scalability}).
89	70B experiments use AWQ INT4 quantization; an 8B ablation confirms enforcement is unaffected (Appendix~\ref{app:quantization}), though a direct 70B FP16 comparison exceeds our hardware capacity.
90	Evaluation is limited to English-language datasets; the mechanism is language-independent but CJK tokenization fragmentation may increase masking steps (Appendix~\ref{app:scalability}).
91	While composability is validated with both LoRA and full fine-tuning (Appendix~\ref{app:full-ft}), different PEFT methods may affect logit distributions differently, and further validation across adapter methods is warranted.
92	The two-pass strategy (S2) exhibits scale-dependent degradation: at 70B, S2 reduces R-F1 by 8.45\,pp while 8B models show comparable S1/S2 performance, suggesting optimal constraint granularity varies with model capacity (Appendix~\ref{app:70b-ablation}).
93	
94	
95	% === Ethics Statement ===
96	\section*{Ethics Statement}
97	
98	This work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.
99	No human subjects were involved in the experiments.
100	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
101	Code and data will be released upon acceptance.
102	
103	% === Bibliography ===
104	\bibliography{relwork_new_entries}
105	
106	% === Appendix ===
107	\appendix
108	
109	\input{appendix_prompts}
110	\input{appendix_related_work}
111	\input{appendix_discussion}
112	\input{appendix_70b_ablation}
113	\input{appendix_llama_per_relation}
114	\input{appendix_sampling_table}
115	\input{appendix_beam_search}
116	\input{appendix_reproducibility}
117	\input{appendix_power_analysis}
118	\input{appendix_doc_length}
119	\input{appendix_prompt_sensitivity}
120	\input{appendix_case_studies}
121	\input{appendix_downstream_analysis}
122	\input{appendix_scalability}
123	\input{appendix_full_ft}
124	\input{appendix_tcr}
125	\input{appendix_kappa_case_study}
126	\input{appendix_high_kappa_analysis}
127	\input{appendix_order_invariance}
128	\input{appendix_pumping_lemma}
129	\input{appendix_wikievents_pilot}
130	\input{appendix_zs_crossmodel}
131	\input{appendix_quantization}
132	\input{appendix_gollie_comparison}
133	\input{appendix_ai_assistants}
134	
135	\end{document}
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d8c7be1-c21c-4804-8ca6-60e498d2a47a",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "79376dc4-4785-4d76-91fd-f2eb437949f1",
  "sourceToolAssistantUUID": "7d8c7be1-c21c-4804-8ca6-60e498d2a47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T05:01:46.329Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0158FLFTUjsMmVTFnTfYy5qw`</summary>

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
  "recorded_role": "assistant",
  "parentUuid": "79376dc4-4785-4d76-91fd-f2eb437949f1",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojV34dXSGMY1Q6XPRj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3949bcb8-ac6b-4f28-9faf-a66a10ff5ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o2MD3LdgvJXGik1uTWfni",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30002,
      "cache_read_input_tokens": 0,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 30002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 207,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 30002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 30002,
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

_source line 7 · 2026-05-24T05:01:46.353Z_

<details><summary>↩ Tool result · `toolu_0158FLFTUjsMmVTFnTfYy5qw`</summary>

```text
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
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/case_study_kappa_dr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section2_background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/fig1_framework.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis_523cc9.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_order_invariance.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_ai_assistants.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3949bcb8-ac6b-4f28-9faf-a66a10ff5ecf",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "b5323946-11fd-49d4-ac86-f13914dcd49a",
  "sourceToolAssistantUUID": "3949bcb8-ac6b-4f28-9faf-a66a10ff5ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-24T05:01:49.473Z_

Now let me read all the appendix files to get their labels, and simultaneously read the main body files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5323946-11fd-49d4-ac86-f13914dcd49a",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1338bfb-726f-408a-a383-5f8723e52896",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool call

_source line 9 · 2026-05-24T05:01:50.003Z_

<details open><summary>🔧 Tool call — Read · `toolu_011g12fszC4axwfQjqYbNK1F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1338bfb-726f-408a-a383-5f8723e52896",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6fd34f7-6323-43d6-a3ab-5cd094de2aa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 10 · 2026-05-24T05:01:50.016Z_

<details><summary>↩ Tool result · `toolu_011g12fszC4axwfQjqYbNK1F`</summary>

```text
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
39	\texttt{\ "relations": [\{"head": "head entity", "tail": "tail entity", "type": "relation name",} \\
40	\texttt{\ \ "head\_type": "ENTITY\_TYPE", "tail\_type": "ENTITY\_TYPE"\}]\}} \\[4pt]
41	\texttt{Output ONLY the JSON, no other text.} \\
42	\midrule
43	\textbf{DocRED --- User Prompt} \\
44	\midrule
45	\texttt{(Document text provided inline in the user message.)} \\
46	\bottomrule
47	\end{tabular}
48	\caption{Extraction prompts used in all experiments.
49	The same prompts are used for both unconstrained and constrained decoding; OntoCoDec's constraints operate at the logit level during generation.
50	Schema-informed prompts (\S\ref{sec:violation_landscape}) additionally include valid (head type, tail type) pairs per relation.}
51	\label{tab:prompts}
52	\end{table*}
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6fd34f7-6323-43d6-a3ab-5cd094de2aa1",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "5d827cea-839b-4f66-b246-762b44f0039a",
  "sourceToolAssistantUUID": "d6fd34f7-6323-43d6-a3ab-5cd094de2aa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T05:01:50.948Z_

<details open><summary>🔧 Tool call — Read · `toolu_01STcpZSE3x2cxekcP95FWDf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d827cea-839b-4f66-b246-762b44f0039a",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99b7a24f-c8c8-467e-bdd8-cb27cac4c40b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 12 · 2026-05-24T05:01:50.957Z_

<details><summary>↩ Tool result · `toolu_01STcpZSE3x2cxekcP95FWDf`</summary>

```text
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
14	Together, these advances have made grammar-constrained decoding both fast and statistically principled, and provide a robust foundation for structured generation.
15	However, all of these methods operate exclusively at the syntactic level: they ensure format validity (e.g., well-formed JSON, valid enum values) but cannot enforce cross-field semantic constraints such as ontology domain/range rules that depend on previously generated content.
16	This syntactic-only limitation motivates OntoCoDec's semantic extension: our grammar layer builds on XGrammar for structural (JSON schema and enum) constraints, while a second semantic layer enforces relational type constraints that are inherently beyond the expressive power of context-free grammars.
17	
18	% ===========================================================================
19	% Paradigm 1.5: Semantic Constrained Decoding for Code
20	% ===========================================================================
21	\paragraph{Semantic Constrained Decoding for Code.}
22	In programming-language generation, constrained decoding has been extended beyond syntax to enforce semantic properties such as type correctness; this work demonstrates that richer-than-CFG constraints can be compiled into token-level filtering.
23	In the text-to-SQL domain, PICARD~\cite{scholak2021picard} maintains an incremental SQL parsing state that rejects tokens violating syntax or referencing non-existent database columns at each decoding step, achieving state-of-the-art results on Spider and CoSQL without modifying model weights.
24	While mechanistically similar to OntoCoDec's token-level filtering, PICARD operates over a \emph{fixed, fully enumerated} schema (database table and column names known before decoding begins).
25	In contrast, OntoCoDec's entity registry is populated \emph{during} generation as entity spans are extracted from free text; constraint sets evolve with the decoding prefix, a fundamental distinction between querying a known schema and extracting from unstructured text.
26	Synchromesh~\cite{synchromesh_iclr2022} pioneers Constrained Semantic Decoding (CSD), which enforces syntax, type, and scope constraints simultaneously during code generation from pre-trained LMs without fine-tuning; this establishes that semantic constraints can be expressed as dynamic token masks conditioned on the generation prefix.
27	MGD~\cite{mgd_neurips2023} uses static-analysis monitors to perform incremental type checking at decode time; SantaCoder-1.1B with MGD outperforms text-davinci-003 on repository-level code completion by ensuring that every generated identifier is type-correct with respect to the surrounding code context.
28	Most recently, \citet{pldi2025_type_constrained_codegen} compile full type systems, including generic types and subtyping, into prefix automata for token-level logits masking and reduce compilation errors by over 50\%.
29	This last system is the closest mechanistic analog to OntoCoDec, applying the same ``type system $\to$ automaton $\to$ logits mask'' pipeline, though in a fundamentally different domain.
30	The key technical difference lies in the constraint structure: programming-language type systems feature deep subtyping hierarchies and parametric polymorphism, whereas IE ontology axioms specify flat domain/range sets; a relation $R$ accepts head entities from set $\mathcal{D}(R)$ and tail entities from set $\mathcal{R}(R)$, with no subtype chains.
31	Conversely, IE introduces a challenge absent in code generation: the constraint target (entity type) must be inferred from free-text spans rather than read from declared type annotations, so a stateful entity registry must track extracted types during autoregressive generation.
32	These methods collectively demonstrate that semantic (type) constraints at decode time are both feasible and highly effective, but exclusively in the code domain where type systems are formally specified.
33	OntoCoDec is the first to \emph{automatically compile} IE ontology axioms, including domain/range constraints, into token-level decoding masks for information extraction, migrating the type-constrained decoding paradigm from code generation to IE.
34	
35	% ===========================================================================
36	% Paradigm 2: Vocabulary/Type-Constrained Generation
37	% ===========================================================================
38	\paragraph{Vocabulary and Type-Constrained Generation.}
39	The idea of enforcing entity-type compatibility constraints for information extraction dates back to pre-neural methods.
40	\citet{roth_yih_2004} formulate joint entity and relation identification as an integer linear program (ILP) that enforces type constraints (e.g., \textsc{Emp-Org} only between \textsc{Per} and \textsc{Org} entities); this establishes the foundational principle that relational type compatibility should be a hard constraint, not a soft preference learned from data.
41	In the autoregressive era, GENRE~\cite{decao2021genre} pioneers trie-based constrained beam search for autoregressive entity retrieval, restricting each decoding step to tokens consistent with valid entity names from a predefined catalog.
42	GenIE~\cite{josifoski2022genie} extends this approach to end-to-end information extraction with state-based constraints that enforce valid triple structures, achieving strong performance on closed-world knowledge base population, though it requires task-specific fine-tuning on the target schema.
43	AdaKGC~\cite{adakgc_emnlp2023} introduces schema-constrained dynamic decoding with trie-based prefix trees that adapt to the target schema, enforcing that generated entity and relation names belong to a predefined inventory, a vocabulary-level constraint that ensures name validity but does not verify type compatibility between a relation and its arguments.
44	GCD~\cite{geng2023gcd} provides a unified grammar-constrained decoding framework for structured NLP tasks including IE, introducing input-dependent grammars that adapt constraints based on the source text. GCD is the closest precursor to OntoCoDec in applying logits masking to IE, though limited to syntactic constraints.
45	NeuroLogic Decoding~\cite{lu2021neurologic} expresses lexical inclusion and exclusion constraints as predicate logic formulas enforced during beam search, offering a general mechanism for token-level control that can encode vocabulary membership but not relational type rules.
46	These approaches constrain \emph{which tokens} can appear (vocabulary membership) but not \emph{which type combinations} are valid for a given relation.
47	OntoCoDec's semantic layer enforces relational constraints (e.g., that the head entity of relation $R$ must belong to type set $\mathcal{D}(R)$) which cannot be expressed as static vocabulary restrictions because the valid set depends on the relation type generated earlier in the same sequence.
48	While Roth \& Yih's ILP formulation shares the same type-compatibility motivation, it operates as a post-hoc reranker over discrete candidates; OntoCoDec integrates enforcement directly into autoregressive decoding, preventing violations rather than filtering them.
49	
50	% ===========================================================================
51	% Paradigm 3: Structural Constraints for IE
52	% ===========================================================================
53	\paragraph{Structural Constraints via Training and Prompting.}
54	An orthogonal approach encodes IE output structure through model training or prompt design rather than decoding-time enforcement, relying on learned representations to produce schema-compliant outputs.
55	UIE~\cite{lu2022uie} defines a Structured Extraction Language and trains a unified text-to-structure model across 13 IE datasets, relying on large-scale pre-training to internalize output format constraints.
56	GoLLIE~\cite{sainz2024gollie} expresses annotation guidelines as Python dataclass definitions and fine-tunes Code-LLaMA to generate typed code, achieving strong zero-shot transfer to unseen IE schemas through the implicit type structure of programming languages.
57	KnowCoder~\cite{knowcoder_acl2024} takes this further by encoding 29K entity types from Wikidata as a Python class hierarchy, training a Code-LLM to generate structured extraction code that implicitly respects type inheritance, the most comprehensive schema-as-code approach to date.
58	CodeIE~\cite{li2023codeie} similarly reformulates IE as code generation, using the structural regularity of programming languages to reduce output format errors.
59	ADELIE~\cite{qi2024adelie} uses SFT and DPO to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a hard constraint.
60	In the supervised setting, joint entity-relation architectures such as SpERT~\cite{eberts2020spert} and PFN~\cite{yan2021pfn} enforce type consistency implicitly through shared representations: SpERT classifies entity spans and relation pairs in a single BERT pass with span-level negative sampling, while PFN decomposes feature encoding into entity-specific, relation-specific, and shared partitions via gating mechanisms.
61	These models achieve strong performance but are limited to fixed, predefined schemas and cannot generalize to unseen ontologies without retraining, precisely the ontology-portable scenario requiring no constraint-specific training that OntoCoDec targets.
62	EnriCo~\cite{zaratiana2024enrico} applies Answer Set Programming (ASP) constraints during decoding of joint entity-relation extraction models, enforcing structural type compatibility at generation time. This is a decoding-time approach, though with model-specific, manually authored constraints rather than ontology-driven compilation.
63	Training-based methods provide \emph{soft} structural guidance: the model learns to prefer valid outputs but cannot enforce compliance at inference time, as demonstrated by non-trivial violation rates even in fine-tuned systems.
64	Importantly, training-based and decoding-time approaches are complementary rather than competing: a system like GoLLIE could be combined with OntoCoDec's constraint layers, using fine-tuning to maximize the probability of valid outputs while decoding-time enforcement eliminates residual violations.
65	OntoCoDec provides \emph{hard} decoding-time enforcement that requires no constraint-specific training, is automatically compiled from IE ontologies, and composable with any of these training-based approaches.
66	
67	% ===========================================================================
68	% Paradigm 4: Type-Checking / Ontology Validation
69	% ===========================================================================
70	\paragraph{Post-hoc Ontology Validation.}
71	Rather than constraining generation, several methods validate LLM outputs against ontological rules after generation, applying a detect-then-fix paradigm.
72	ODKE+~\cite{khorshidi2025odke} dynamically generates ontology snippets containing domain/range constraints as prompt context, achieving 98.8\% precision across 195 predicates at web scale, but constraint adherence relies on prompt-level guidance, not enforcement, leaving residual violations unaddressed.
73	SPIRES/OntoGPT~\cite{spires_2024} provides an ontology-based extraction framework that grounds LLM outputs against OBO ontologies post-generation: it validates extracted entities and relations through ontology lookup and corrects mismatches in a second pass, the prompt-then-validate paradigm in the biomedical domain.
74	OntoLogX~\cite{ontologx_2025} applies SHACL validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds. This demonstrates the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
75	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
76	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating RDF triple insertions against RDFS domain/range constraints, where each validation step requires a separate LLM call, effective but computationally expensive at scale.
77	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
78	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
79	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
80	Concurrently, \citet{zhou2026ontologytools} compile OWL ontologies into executable tool interfaces within The World Avatar framework; LLM agents must invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
81	This ``ontology-to-tools'' approach shares OntoCoDec's philosophy of compiling formal ontological knowledge into runtime enforcement mechanisms, but operates at the tool-call level (constraining which API functions the agent invokes) rather than at the token level (constraining which tokens the decoder produces), and requires an agentic multi-step workflow rather than single-pass autoregressive generation.
82	\citet{ekaw2024_ontology_beam} introduce ontology-constrained beam scoring for clinical summarization, applying soft biases (not hard masks) during beam search to steer outputs toward ontology-compliant terms, a middle ground between unconstrained generation and hard enforcement that reduces but cannot eliminate violations.
83	Post-hoc validation detects violations after generation and requires rejection or correction cycles that waste compute. In our setting, 15.37\% of generated triples contain domain/range violations under unconstrained decoding, a substantial waste of generation effort.
84	OntoCoDec \emph{prevents} violations during decoding, redirecting probability mass to valid alternatives rather than discarding invalid outputs, with only marginal overhead from logits masking compared to the cost of regenerating or correcting violated triples.
85	Soft-constraint approaches such as ontology-weighted beam scoring reduce violation frequency but cannot eliminate it, whereas OntoCoDec substantially reduces violations (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED depending on model).
86	
87	% ===========================================================================
88	% Paradigm 5: Constrained Decoding Quality Concerns
89	% ===========================================================================
90	\paragraph{Quality Impact of Constrained Decoding.}
91	A growing body of work raises concerns that constrained decoding degrades LLM generation quality, particularly for reasoning-intensive tasks where format enforcement interferes with chain-of-thought processes.
92	\citet{tam2024letmespeak} conduct a comprehensive evaluation showing that rigid format constraints (JSON, XML) harm performance on math and multi-hop QA benchmarks but \emph{benefit} classification-style tasks such as slot filling, a distinction directly relevant to IE, which is fundamentally an extraction (classification-like) task rather than a reasoning task.
93	CRANE~\cite{banerjee2025crane} provides theoretical analysis of why restricting outputs to narrow grammars suppresses chain-of-thought reasoning by eliminating intermediate reasoning tokens, and proposes an alternating strategy between unconstrained reasoning phases and constrained output phases to mitigate this effect.
94	\citet{schall2025hiddencost} conduct a systematic study across 11 models and multiple benchmarks, finding 10--30\% semantic correctness degradation on reasoning tasks under structural constraints, with larger models showing greater absolute degradation.
95	\citet{zhou2026snowballing} identify ``structure snowballing,'' a failure mode where format compliance cognitive load traps models in repetitive structural patterns rather than improving reasoning during self-correction iterations.
96	These findings establish a legitimate concern for constrained decoding in reasoning-heavy applications.
97	However, information extraction occupies a fundamentally different regime: the model extracts entities and relations from input text rather than generating novel reasoning chains, and \citet{tam2024letmespeak}'s own results show that extraction-style tasks are robust to, or even benefit from, format constraints.
98	OntoCoDec addresses this concern empirically: domain/range violations decrease by 94\% on SciERC (15.37\%$\to$0.93\%) and 45--90\% on DocRED across two models, with F1-neutral impact on SciERC ($+$0.13pp, $p{=}0.58$) and significant R-F1 gains on DocRED (Qwen $p{<}0.001$, Llama $p{=}0.013$).
99	Critically, OntoCoDec's constraints target only type tokens (entity types, relation labels), leaving free-text spans (entity surface forms and their boundaries) entirely unconstrained, which minimizes the distribution distortion that causes quality degradation in reasoning tasks.
100	A two-pass variant (S2), explored in ablation (Section~5), separates extraction and constraint enforcement into distinct passes, analogous to CRANE's alternating strategy; however, our primary single-pass approach already avoids reasoning interference by constraining only type tokens while leaving free-text spans unconstrained.
101	
102	% ===========================================================================
103	% Our Approach
104	% ===========================================================================
105	\paragraph{Our Approach.}
106	OntoCoDec occupies a unique position in this landscape: it is the first system to \emph{automatically compile} IE ontologies, including domain/range axioms, into token-level semantic masks, extending grammar-constrained decoding from syntactic to semantic enforcement without manually authored rules.
107	Unlike vocabulary-constrained methods that restrict individual tokens to a fixed set, OntoCoDec enforces \emph{cross-field relational constraints} through a stateful entity registry that tracks extracted types during autoregressive generation; constraint evaluation is dynamic and depends on previously decoded content.
108	This approach is orthogonal to supervised IE methods and applicable to autoregressive LMs with logits access without model modification or additional training (evaluated on 7B--70B models across three tokenizer families).
109	Unlike training-based IE systems, OntoCoDec requires no constraint-specific training and substantially reduces type violations at inference time (DR$\downarrow$94\% on SciERC, $\downarrow$45--90\% on DocRED); unlike post-hoc validation, it prevents violations rather than detecting them, redirecting probability mass to valid alternatives with significant R-F1 gains on DocRED ($p \leq 0.013$) and F1-neutral impact on SciERC.
110	The two constraint layers, grammar (structural) and semantic (relational), compose via bitwise AND with a scale-dependent interaction: the grammar layer ensures every generated type token belongs to the valid vocabulary, which enables the semantic layer to look up and enforce domain/range rules for that type.
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99b7a24f-c8c8-467e-bdd8-cb27cac4c40b",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "7c60c6c9-1f47-4b56-b7c4-edcee07f0758",
  "sourceToolAssistantUUID": "99b7a24f-c8c8-467e-bdd8-cb27cac4c40b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T05:01:51.421Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PkzFQTQB6iRdWZFuFkZsjz`</summary>

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
  "parentUuid": "7c60c6c9-1f47-4b56-b7c4-edcee07f0758",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe8342ad-de65-45e5-a51c-d739e146458d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 14 · 2026-05-24T05:01:51.719Z_

<details><summary>↩ Tool result · `toolu_01PkzFQTQB6iRdWZFuFkZsjz`</summary>

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
26	The two-layer architecture produces two distinct fallback mechanisms with different semantic consequences.
27	\emph{Grammar-first fallback} occurs when $S(t) \cap G(t) = \emptyset$: the semantic layer deactivates as a safety valve, preserving structural validity at the cost of potential type violations.
28	The token-level fallback rate (36.6\% on SciERC Llama) is inflated by continuation tokens of multi-token type names (e.g., \textsc{OtherScientificTerm}, averaging 2.87 BPE tokens); at semantically meaningful first-token positions, the rate is 0.04--5.7\% (zero-shot) and drops to $\leq$\,0.11\% under fine-tuning.
29	These events account for the residual DR that persists after constraint enforcement.
30	\emph{Registry-consistent fallback} (4.5\%) occurs when the entity's registered type conflicts with domain/range constraints; the system defaults to the registered type for cross-triple consistency.
31	Together, these mechanisms produce the characteristic profile of composable constraint systems: residual DR traces to grammar-first fallback events, while CF violations arise from registry override events where per-relation enforcement assigns conflicting types.
32	
33	We define \emph{effective semantic constraint coverage} as $1 - f_{\text{gf}}$, where $f_{\text{gf}}$ is the grammar-first fallback rate.
34	On SciERC, Llama-3.1-8B shows $f_{\text{gf}} = 36.6\%$ (6{,}237 of 17{,}024 mask calls), yielding 63.4\% effective coverage.
35	On DocRED, by contrast, Qwen3-8B shows $f_{\text{gf}} = 0.08\%$ (46 of 54{,}859), yielding 99.9\% coverage.
36	The large discrepancy is primarily a tokenization artifact: SciERC entity types are multi-token (e.g., \textsc{OtherScientificTerm}, averaging 2.87 mask calls per type field), and continuation tokens necessarily conflict with the semantic mask, inflating the per-mask-call fallback rate.
37	DocRED types (\textsc{PER}, \textsc{ORG}, \textsc{LOC}, \textsc{TIME}, \textsc{NUM}, \textsc{MISC}) are all single-token, eliminating this inflation.
38	This metric directly quantifies the layer interaction (\S\ref{sec:interaction}): it measures the fraction of decoding steps where both constraint layers are jointly active, providing a fine-grained view beyond aggregate violation rates.
39	Qwen3-8B, with zero grammar-first fallbacks, achieves 100\% effective coverage on SciERC, consistent with its lower residual DR (0.93\% vs.\ Llama's 0.08\%).
40	
41	%%% Fallback Causal Tracing %%%
42	% exp_ids: Task C causal tracing (Qwen/Llama × ZS/FT × S1)
43	
44	\paragraph{Fallback Causal Tracing.}
45	\label{app:causal-tracing}
46	
47	To establish that grammar-first fallback is the \emph{sole} mechanism producing residual DR violations, we instrument the constraint processor to log, for each violation, whether the semantic mask was active ($S(t) \cap G(t) \neq \emptyset$) or bypassed via fallback ($S(t) \cap G(t) = \emptyset$) at the type-bearing position.
48	Table~\ref{tab:causal-tracing} reports the results across four SciERC configurations.
49	
50	\begin{table}[t]
51	\centering
52	\small
53	\begin{tabular}{@{}ll rrr@{}}
54	\toprule
55	\textbf{Model} & \textbf{Setting} & \textbf{Fallback Rate} & \textbf{DR} & \textbf{From FB} \\
56	\midrule
57	Qwen3-8B  & FT S1 & 0/2256 (0\%)    & 0  & N/A \\
58	Qwen3-8B  & ZS S1 & 16/3458 (0.46\%) & 16 & 100\% \\
59	Llama-3.1-8B & FT S1 & 1/2162 (0.05\%) & 1  & 100\% \\
60	Llama-3.1-8B & ZS S1 & 1/2630 (0.04\%) & 1  & 100\% \\
61	\bottomrule
62	\end{tabular}
63	\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \cap G(t) = \emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\_type positions (range constraints are tighter than domain constraints).}
64	\label{tab:causal-tracing}
65	\end{table}
66	
67	When the semantic mask is active, $\text{DR}_{\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.
68	All 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.
69	Fine-tuning reduces fallback to near-zero ($\leq$0.05\%), effectively eliminating the sole source of residual violations.
70	All fallback events occur at tail\_type positions, where $|\operatorname{range}(r, \tau^h)|$ is smaller than $|\operatorname{dom}(r)|$, making the intersection $S(t) \cap G(t)$ more likely to be empty.
71	
72	%%% Enabling Dependency: Confound Analysis %%%
73	
74	\paragraph{Enabling Dependency: Confound Analysis.}
75	\label{app:enabling-confound}
76	
77	The scale-dependent layer interaction (\S\ref{sec:method}) shows that the semantic layer achieves only 24\% DR reduction without the grammar layer (Table~\ref{tab:scierc-ablation}).
78	A potential confound is that the semantic layer depends not only on grammar-enforced vocabulary membership but also on structural enforcement for positional awareness: the semantic layer identifies type-bearing positions by pattern-matching the decoded prefix against the JSON schema, which is reliable only when the grammar layer guarantees valid JSON structure.
79	Without grammar enforcement, malformed structure can cause the semantic layer to misidentify type-bearing positions, reducing effective coverage.
80	We quantify this via the semantic-only ablation (Table~\ref{tab:scierc-ablation}, row~3): CF rises from 0.08\% to 2.71\%, indicating that 2.63\,pp of additional violations trace to structural ambiguity.
81	However, the dominant enabling mechanism remains vocabulary membership: the semantic layer's domain/range lookup requires $r_j \in \mathcal{R}$, which only the grammar layer ensures; without it, OOV relation names produce null constraint lookups.
82	The confound reinforces rather than undermines this interaction: both vocabulary and structural contributions of the grammar layer are prerequisites for effective semantic enforcement.
83	
84	%%% CF-DR Trade-off Analysis %%%
85	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
86	
87	\paragraph{CF-DR Trade-off Analysis.}
88	\label{app:cf-dr-tradeoff}
89	
90	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
91	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
92	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\begin{tabular}{@{}l rrrr@{}}
98	\toprule
99	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
100	\midrule
101	S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
102	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
103	\midrule
104	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
105	\bottomrule
106	\end{tabular}
107	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
108	\label{tab:cf-dr-tradeoff}
109	\end{table}
110	
111	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
112	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
113	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
114	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
115	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
116	
117	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
118	Within this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
119	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
120	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
121	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
122	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
123	
124	Two complementary paths can lower CF without re-routing it to DR.
125	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
126	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
127	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
128	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
129	
130	%%% Dual-Factor Quantitative Analysis %%%
131	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
132	%          llama_scierc_full_s1, llama_docred_full_s1
133	
134	\paragraph{Dual-Factor Quantitative Analysis.}
135	\label{app:dual-factor}
136	
137	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
138	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
139	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
140	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
141	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
142	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
143	
144	\begin{figure}[t]
145	\centering
146	\includegraphics[width=0.75\columnwidth]{figures/dual_factor_scatter.pdf}
147	\caption{Residual DR vs.\ Schema Restrictiveness $\times$ Baseline Violation Rate ($\bar{\kappa} \times \text{RV}_{\text{baseline}}$) across four model$\times$dataset configurations ($n{=}3$ schemas; descriptive only).
148	Linear fit (calibrated models): $y = 0.366x - 0.138$, $R^2 = 0.886$, $p{=}0.058$ ($n{=}4$, df${=}2$; not significant); Mistral deviates due to entity misclassification.}
149	\label{fig:dual-factor-scatter}
150	\end{figure}
151	
152	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
153	% exp_ids: d012_bootstrap_ci (DocRED +0.49pp p<0.001, SciERC +0.13pp p=0.58),
154	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
155	
156	\paragraph{Dataset-Dependent F1 Impact.}
157	The divergence in F1 significance between DocRED ($+$0.49\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
158	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
159	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
160	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.49\,pp); F1 gain magnitude is proportional to baseline OOV rate.
161	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
162	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
163	
164	%%% Bootstrap CIs and Effect Sizes %%%
165	% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci
166	
167	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
168	\label{app:bootstrap-effect-sizes}
169	
170	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\ref{tab:composability}).
171	After Bonferroni correction for $k{=}4$ comparisons ($\alpha_{\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \leq 0.37$; Cohen, 1988).
172	Per-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.
173	Constraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \geq 3.0$, all $p_{\text{Bonf}} < 0.005$).
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\setlength{\tabcolsep}{3pt}
179	\begin{tabular}{@{}ll rrrr@{}}
180	\toprule
181	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{(pp)} & \textbf{95\% CI} & $p$ & $d$ \\
182	\midrule
183	\multicolumn{6}{@{}l}{\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\
184	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\
185	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\
186	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\
187	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\
188	\midrule
189	\multicolumn{6}{@{}l}{\textbf{DR\% reduction:}} \\
190	Qwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\
191	Qwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\
192	Llama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\
193	Llama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\
194	\bottomrule
195	\end{tabular}
196	\caption{Bootstrap CIs and Cohen's $d$ for Table~\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).
197	$d$: Cohen's $d$ from pooled bootstrap SD.
198	Top: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\alpha_{\text{adj}}{=}0.0125$); $|d| \leq 0.37$ (negligible--small).
199	Bottom: DR\% reduction; all $p_{\text{Bonf}} < 0.005$, $|d| \geq 3.0$ (large).}
200	\label{tab:bootstrap-effect-sizes}
201	\end{table}
202	
203	%%% Paragraph 1: Low F1 Practical Significance %%%
204	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
205	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
206	
207	\paragraph{Practical Significance of Zero-Shot F1.}
208	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
209	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
210	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
211	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
212	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
213	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
214	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
215	
216	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
217	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
218	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
219	
220	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
221	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
222	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
223	However, this precision gain comes at substantial cost.
224	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
225	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
226	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
227	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
228	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
229	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
230	
231	%%% CF Violation Distribution %%%
232	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
233	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
234	
235	\paragraph{Cross-Field Violation Distribution.}
236	\label{app:cf-distribution}
237	
238	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC zero-shot S1 (248 CF violations across 245 unique entity-document pairs; no mention triggered $\geq$3 types).
239	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
240	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
241	
242	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
243	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\begin{tabular}{@{}lr r@{}}
249	\toprule
250	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
251	\midrule
252	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
253	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
254	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
255	Method $\leftrightarrow$ Task & 20 & 8.2 \\
256	Material $\leftrightarrow$ Method & 17 & 6.9 \\
257	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
258	\midrule
259	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
260	\midrule
261	\textbf{Total} & \textbf{245} & 100.0 \\
262	\bottomrule
263	\end{tabular}
264	\caption{CF violation distribution on SciERC zero-shot S1 (Qwen3-8B, 551 documents).
265	All 245 unique entity-document pairs involve pairwise conflicts.
266	Conflicts involving \textsc{Generic} account for 63.3\%.}
267	\label{tab:cf-distribution}
268	\end{table}
269	
270	%%% Cascade Error Analysis %%%
271	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248), w5_lora_scierc_full_s1_eval (FT: CF=22)
272	
273	\paragraph{Cascade Error Analysis.}
274	\label{app:cascade-analysis}
275	
276	Table~\ref{tab:cascade-breakdown} decomposes zero-shot CF violations by source mechanism.
277	The dominant source is hallucinated entities (58.1\%): the model generates entity names absent from the input document, and the entity registry assigns a type based on the first occurrence that may conflict with a subsequent valid entity sharing the same surface form.
278	True cascade errors---where first-seen type registration for a \emph{real} entity locks an incorrect type that blocks a subsequent valid assignment---account for only 7.3\% (18/248).
279	Correct type locks (first-seen type is correct and prevents an incorrect subsequent assignment) are 2.5$\times$ more frequent (18.1\%, 45/248), indicating that the first-seen registration mechanism provides a net benefit for type consistency.
280	
281	Under fine-tuning (22 CF violations, 20 documents), cascade errors are completely eliminated (0/22): LoRA training calibrates entity typing sufficiently that first-seen registrations are consistently correct.
282	This confirms that cascade errors are a model calibration issue exposed by the constraint mechanism, not an inherent deficiency of first-seen registration.
283	
284	\begin{table}[h]
285	\centering
286	\small
287	\begin{tabular}{@{}l rr@{}}
288	\toprule
289	\textbf{CF Source Category} & \textbf{Count} & \textbf{\%} \\
290	\midrule
291	Hallucinated entity & 144 & 58.1 \\
292	Correct type lock & 45 & 18.1 \\
293	True cascade error & 18 & 7.3 \\
294	Other / ambiguous & 41 & 16.5 \\
295	\midrule
296	\textbf{Total} & \textbf{248} & 100.0 \\
297	\bottomrule
298	\end{tabular}
299	\caption{CF violation source breakdown on SciERC zero-shot S1 (Qwen3-8B, 551 documents; exp\_id: phase2\_scierc\_full\_s1).
300	``Hallucinated entity'': generated entity absent from input.
301	``True cascade error'': first-seen lock on incorrect type blocks valid subsequent assignment.
302	``Correct type lock'': first-seen type correct, prevents incorrect subsequent type.
303	Under fine-tuning, cascade errors are completely eliminated (0/22 CF violations; exp\_id: w5\_lora\_scierc\_full\_s1\_eval).}
304	\label{tab:cascade-breakdown}
305	\end{table}
306	
307	%%% Per-Relation DR Elimination under Fine-Tuning %%%
308	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
309	
310	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
311	\label{app:lora-per-relation}
312	
313	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
314	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
315	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
316	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
317	
318	\begin{table}[t]
319	\centering
320	\small
321	\begin{tabular}{@{}l r rr rr@{}}
322	\toprule
323	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
324	\cmidrule(lr){3-4} \cmidrule(l){5-6}
325	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
326	\midrule
327	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
328	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
329	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
330	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
331	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
332	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
333	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
334	\bottomrule
335	\end{tabular}
336	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
337	$\kappa$: constraint tightness; $n$: predicted triple count.
338	Used-for gains one triple from Evaluate-for redirection.}
339	\label{tab:lora-per-relation}
340	\end{table}
341	
342	%%% Fine-Tuned Four-Way Ablation %%%
343	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
344	
345	\paragraph{Fine-Tuned Four-Way Ablation.}
346	\label{app:ft-ablation}
347	
348	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
349	
350	\begin{table}[t]
351	\centering
352	\small
353	\setlength{\tabcolsep}{3pt}
354	\resizebox{\columnwidth}{!}{%
355	\begin{tabular}{@{}lll rrrrr rr@{}}
356	\toprule
357	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
358	\midrule
359	\multirow{8}{*}{SciERC}
360	  & \multirow{4}{*}{Qwen3-8B}
361	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
362	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
363	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
364	  & & S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
365	  \cmidrule(l){2-10}
366	  & \multirow{4}{*}{Llama-3.1-8B}
367	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
368	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
369	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
370	  & & S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
371	\midrule
372	\multirow{8}{*}{DocRED}
373	  & \multirow{4}{*}{Qwen3-8B}
374	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
375	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
376	  & & Semantic      & 0.19 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.85 \\
377	  & & S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
378	  \cmidrule(l){2-10}
379	  & \multirow{4}{*}{Llama-3.1-8B}
380	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\
381	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.72 \\
382	  & & Semantic      & 0.48 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.85 \\
383	  & & S1       & \textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\
384	\bottomrule
385	\end{tabular}}%
386	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
387	DR/RV/ET: violation rates (\%) over predicted relations; CF: over predicted entities; PF: parse failure rate (\%); F1 $\times$100.
388	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
389	Semantic layer is the sole effective DR defense (41--69\% on SciERC, 2--75\% on DocRED); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%).
390	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained).}
391	\label{tab:ft-ablation}
392	\end{table}
393	
394	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
395	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 41--69\% on SciERC (Qwen $-$69\%, Llama $-$41\%) and 2--75\% on DocRED (Qwen $-$75\%, Llama $-$2\%); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%, 80 violations in 16{,}074 triples), where the semantic layer has minimal room to improve.
396	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.21\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
397	F1 cost is negligible: the maximum R-F1 decrease across S1 vs.\ unconstrained is $-$0.30\,pp (Qwen DocRED).
398	
399	%%% DocRED Zero-Shot Ablation (moved from main text) %%%
400	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
401	%          phase2_docred_semantic_only, phase2_docred_full_s1
402	
403	\paragraph{DocRED Zero-Shot Ablation.}
404	\label{app:docred-zs-ablation}
405	
406	Table~\ref{tab:docred-ablation} presents the four-way constraint ablation on DocRED under zero-shot decoding, parallel to the SciERC ablation in Table~\ref{tab:scierc-ablation}.
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\setlength{\tabcolsep}{3.6pt}
412	\resizebox{\columnwidth}{!}{%
413	\begin{tabular}{@{}l rrrrrr rr@{}}
414	\toprule
415	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
416	& \multicolumn{2}{c}{\textbf{F1}} \\
417	\cmidrule(lr){2-7} \cmidrule(l){8-9}
418	\textbf{Mode}
419	  & DR\,$\downarrow$ & $\Delta$DR
420	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
421	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
422	\midrule
423	Unconstrained
424	  & 18.46 & ---
425	  & 29.66 & 2.48
426	  & 0.10  & 18.56
427	  & 7.74  & 58.15 \\
428	Grammar
429	  & 26.17 & $\uparrow$42\%
430	  & \textbf{0.03} & \textbf{0}
431	  & 0.07  & 26.24
432	  & \textbf{8.31}  & \textbf{59.38} \\
433	Semantic
434	  & 13.84 & $\downarrow$25\%
435	  & 29.87 & 4.22
436	  & 1.05  & 14.89
437	  & 7.70  & 57.81 \\
438	S1
439	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
440	  & \textbf{0.03} & \textbf{0}
441	  & 2.57  & \textbf{12.78}
442	  & 8.23  & 59.37 \\
443	\bottomrule
444	\end{tabular}}%
445	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
446	$\Delta$DR: relative change vs.\ unconstrained.
447	Tot.\ = DR + CF (total type-violation burden).
448	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
449	F1 $\times$100. Bootstrap significance: R-F1 $+$0.49\,pp ($p < 0.001$).
450	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see \S\ref{sec:docred-results}).}
451	\label{tab:docred-ablation}
452	\end{table}
453	
454	%%% Residual DR Error Analysis (Fine-Tuned) %%%
455	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
456	
457	\paragraph{Residual DR Error Analysis.}
458	\label{app:residual-dr-analysis}
459	
460	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ S1), only 36 domain/range violations remain.
461	Manual inspection reveals four root causes:
462	
463	\begin{enumerate}[nosep,leftmargin=*]
464	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
465	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
466	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
467	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
468	\end{enumerate}
469	
470	Two dataset-specific patterns emerge.
471	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
472	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
473	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 6 entity types) compared to Qwen, which achieves near-zero residual.
474	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
475	
476	%%% Post-Hoc Filtering Comparison (Extended) %%%
477	% exp_ids: posthoc_*_zs, posthoc_*_ft
478	
479	\paragraph{Post-Hoc Filtering: Extended Comparison.}
480	\label{app:posthoc-extended}
481	
482	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
483	
484	\begin{table}[t]
485	\centering
486	\small
487	\setlength{\tabcolsep}{3pt}
488	\resizebox{\columnwidth}{!}{%
489	\begin{tabular}{@{}lll rrr l@{}}
490	\toprule
491	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
492	\midrule
493	\multirow{6}{*}{ZS}
494	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
495	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
496	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
497	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
498	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
499	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
500	\midrule
501	\multirow{4}{*}{FT}
502	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
503	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
504	  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\
505	  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\
506	\bottomrule
507	\end{tabular}}%
508	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
509	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
510	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
511	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
512	F1 $\times$100.}
513	\label{tab:posthoc-extended}
514	\end{table}
515	
516	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
517	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
518	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
519	
520	%%% Zero-Shot Runtime Profiling %%%
521	
522	\paragraph{Zero-Shot Runtime Profiling.}
523	\label{app:runtime}
524	
525	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
526	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
527	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
528	
529	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
530	\paragraph{Fine-Tuned Latency Profiling.}
531	\label{app:ft-latency}
532	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
533	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
534	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
535	
536	%%% Fuzzy Relation Matching %%%
537	
538	\paragraph{Relation Matching Protocol.}
539	\label{app:fuzzy-matching}
540	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
541	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
542	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
543	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
544	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
545	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
546	
547	%%% Per-Relation Violation Landscape %%%
548	
549	\paragraph{Per-Relation Violation Landscape.}
550	\label{app:per-relation-landscape}
551	
552	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
553	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
554	
555	\begin{table}[t]
556	\centering
557	\small
558	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
559	\label{tab:prompt_comparison}
560	\resizebox{\columnwidth}{!}{%
561	\begin{tabular}{ll cccc}
562	\toprule
563	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
564	\midrule
565	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
566	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
567	\midrule
568	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
569	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
570	\bottomrule
571	\end{tabular}}
572	\end{table}
573	
574	\begin{figure}[t]
575	\centering
576	\includegraphics[width=\columnwidth]{figures/fig2_per_relation_dr.pdf}
577	\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\ref{app:llama-per-relation}).}
578	\label{fig:per_relation_dr}
579	\end{figure}
580	
581	%%% WikiEvents Extended %%%
582	
583	\paragraph{WikiEvents Dataset Details.}
584	\label{app:wikievents}
585	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
586	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
587	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
588	
589	\paragraph{Constraint Tightness in WikiEvents.}
590	\label{app:wikievents-kappa}
591	% Data source: artifacts/w1c_wikievents_kappa_results.md
592	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
593	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
594	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
595	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
596	
597	%%% Lucky Violation Analysis %%%
598	% exp_ids: task_e_lucky_violation_analysis
599	
600	\paragraph{Lucky Violation Analysis.}
601	\label{app:lucky-violations}
602	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
603	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
604	Across four fine-tuned configurations, lucky violations average 0.24\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
605	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
606	
607	\begin{table}[h]
608	\centering
609	\small
610	\resizebox{\columnwidth}{!}{%
611	\begin{tabular}{@{}llrrrr@{}}
612	\toprule
613	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
614	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
615	\midrule
616	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
617	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
618	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
619	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
620	\midrule
621	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.24\%} & $-$0.26 & 0.78 \\
622	\bottomrule
623	\end{tabular}}
624	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
625	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
626	$\Delta$Recall: recall change from unconstrained to constrained.
627	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
628	\label{tab:lucky-violations}
629	\end{table}
630	
631	%%% Trie-Only Baseline %%%
632	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
633	
634	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
635	\label{app:trie-baseline}
636	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
637	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
638	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
639	The effect is most dramatic for Llama-8B LoRA: 50.8\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.
640	
641	\begin{table}[h]
642	\centering
643	\small
644	\resizebox{\columnwidth}{!}{%
645	\begin{tabular}{@{}ll rrrr rr@{}}
646	\toprule
647	\textbf{Model} & \textbf{Setting}
648	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
649	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
650	\midrule
651	\multirow{2}{*}{Qwen3-8B}
652	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\
653	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
654	\multirow{2}{*}{Llama-8B}
655	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 19.95 & 50.8 \\
656	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
657	\midrule
658	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
659	\midrule
660	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
661	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
662	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
663	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
664	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
665	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
666	\bottomrule
667	\end{tabular}}
668	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
669	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
670	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
671	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
672	$^\dagger$50.8\% parse failure rate.}
673	\label{tab:trie-baseline}
674	\end{table}
675	
676	%%% GCD/BoostCD Equivalence Comparison %%%
677	
678	\paragraph{Comparison with Grammar-Based Constrained Decoding.}
679	\label{app:gcd-comparison}
680	
681	Table~\ref{tab:gcd-comparison} summarizes the relationship between OntoCoDec's constraint layers and existing grammar-based constrained decoding methods.
682	
683	\begin{table}[h]
684	\centering
685	\small
686	\resizebox{\columnwidth}{!}{%
687	\begin{tabular}{@{}l l l l l l@{}}
688	\toprule
689	\textbf{Method} & \textbf{Constraint Type} & \textbf{Level} & \textbf{DR Red.} & \textbf{CF} & \textbf{State} \\
690	\midrule
691	GCD~\cite{geng2023gcd} & CFG (JSON schema) & Grammar & ${\sim}$3\% & N/A & Stateless \\
692	BoostCD~\cite{boostcd2025} & CFG + beam rerank & Grammar & ${\sim}$3\%$^\dagger$ & N/A & Stateless \\
693	Trie-Only (Tab.~\ref{tab:trie-baseline}) & Prefix trie & Vocab & 0\%$^\ddagger$ & N/A & Stateless \\
694	\midrule
695	vLLM \texttt{guided\_json}~\cite{kwon2023vllm} & JSON Schema & Grammar & ${\sim}$3\%$^\S$ & N/A & Stateless \\
696	\midrule
697	OntoCoDec Grammar & CFG (XGrammar) & Grammar & ${\sim}$3\% & N/A & Stateless \\
698	OntoCoDec S1 & CFG + type constr. & Gram.+Sem. & 94--100\% (FT) & ${\leq}$1.4\% (FT) & Entity reg. \\
699	\bottomrule
700	\end{tabular}}
701	\caption{Comparison with grammar-based constrained decoding methods.
702	$^\dagger$Equivalent mechanism; BoostCD adds beam-level reranking but the CFG enforcement is identical.
703	$^\ddagger$Vocabulary-only constraints without JSON structure cause DR to \emph{increase} (15--96\%; Table~\ref{tab:trie-baseline}).
704	$^\S$Experimentally verified: DR${=}$15.26\% vs.\ grammar-only 14.84\% ($\Delta{<}$0.5\,pp; Table~\ref{tab:vllm-verification}).
705	Grammar-only results are analytically equivalent to GCD/BoostCD (same CFG enforcement; \S\ref{sec:related_work}).}
706	\label{tab:gcd-comparison}
707	\end{table}
708	
709	Our grammar layer implements the same CFG-based token masking as GCD and BoostCD---the mechanisms are formally identical (JSON schema $\to$ pushdown automaton $\to$ per-step allowed token set).
710	Table~\ref{tab:scierc-ablation} row~2 therefore constitutes a direct comparison: grammar-only enforcement achieves RV/ET$\to$0\% but only ${\sim}$3\% DR reduction, identical to what GCD-family methods would achieve on IE tasks.
711	
712	% exp_id: vllm_guided_json_scierc_zs
713	\paragraph{External verification via vLLM.}
714	To confirm this equivalence experimentally, we evaluated vLLM's \texttt{guided\_json} mode~\cite{kwon2023vllm}---an independent CFG enforcement implementation---on SciERC under identical conditions (Qwen3-8B, zero-shot, 551 documents).
715	
716	\begin{table}[h]
717	\centering
718	\small
719	\begin{tabular}{@{}l rrrr r@{}}
720	\toprule
721	\textbf{Method} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{R-F1\,$\uparrow$} \\
722	\midrule
723	Grammar-Only (XGrammar) & 14.84 & 0 & 0 & 9.90 & 8.23 \\
724	vLLM \texttt{guided\_json} & 15.26 & 0 & 0 & --- & 8.75 \\
725	\midrule
726	$\Delta$ & $+$0.42 & 0 & 0 & --- & $+$0.52 \\
727	\bottomrule
728	\end{tabular}
729	\caption{GCD-equivalence verification: OntoCoDec grammar-only vs.\ vLLM \texttt{guided\_json} on SciERC (Qwen3-8B, zero-shot, 551 documents). All differences $<$0.5\,pp, confirming that CFG-based approaches---regardless of implementation---leave ${\sim}$15\% DR violations unaddressed.}
730	\label{tab:vllm-verification}
731	\end{table}
732	
733	All metrics differ by $<$0.5\,pp (Table~\ref{tab:vllm-verification}), confirming that any CFG-based constrained decoding tool---whether GCD, BoostCD, or vLLM---enforces the same constraint class and leaves the same ${\sim}$15\% DR gap.
734	The critical gap these methods cannot address is cross-field type consistency (Level~2), which requires the stateful semantic layer that maintains an entity registry across relation slots and enforces per-relation domain/range constraints at each type-bearing position.
735	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe8342ad-de65-45e5-a51c-d739e146458d",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "fbe9f724-11d8-42b1-84fe-26e97e50e9e9",
  "sourceToolAssistantUUID": "fe8342ad-de65-45e5-a51c-d739e146458d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T05:01:51.910Z_

<details open><summary>🔧 Tool call — Read · `toolu_0183sz4UyoPXKuD2JrjVBf97`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbe9f724-11d8-42b1-84fe-26e97e50e9e9",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "795b7b1c-c2d8-4d59-91c7-2a5cd4895450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 16 · 2026-05-24T05:01:51.918Z_

<details><summary>↩ Tool result · `toolu_0183sz4UyoPXKuD2JrjVBf97`</summary>

```text
1	% Appendix: 70B-Class LoRA Ablation on SciERC
2	% exp_ids: eval_70b_lora_scierc_unconstrained, eval_70b_lora_scierc_grammar_only,
3	%          eval_70b_lora_scierc_semantic_only, eval_70b_lora_scierc_s1_constrained,
4	%          eval_70b_lora_scierc_s2_constrained, eval_70b_lora_scierc_beam4_s1
5	
6	\paragraph{70B-class fine-tuned ablation.}
7	\label{app:70b-ablation}
8	
9	Table~\ref{tab:70b-ft-ablation} presents the constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on SciERC (551 documents).
10	
11	\begin{table}[h]
12	\centering
13	\small
14	\setlength{\tabcolsep}{3.6pt}
15	\begin{tabular}{@{}l rrrr rr@{}}
16	\toprule
17	\textbf{Mode}
18	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
19	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
20	\midrule
21	Unconstrained & 1.50 & 0 & 0 & 0    & 44.73 & 64.86 \\
22	Grammar       & 1.50 & 0 & 0 & 0    & 44.63 & 64.82 \\
23	Semantic      & 0.60 & 0 & 0 & 9    & 44.73 & 64.86 \\
24	S1            & \textbf{0} & 0 & 0 & 15 & 44.53 & 64.76 \\
25	S2            & \textbf{0} & 0 & 0 & 18 & 36.28 & 62.35 \\
26	Beam4 S1      & \textbf{0} & 0 & 0 & \textbf{1} & \textbf{44.81} & \textbf{64.89} \\
27	\bottomrule
28	\end{tabular}
29	\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on SciERC (551 docs).
30	CF: violation count. F1 $\times$100.}
31	\label{tab:70b-ft-ablation}
32	\end{table}
33	
34	The grammar layer provides no independent DR benefit at 70B (1.50\%\,$\to$\,1.50\% on SciERC; on DocRED zero-shot, DR actually increases $+$3.58\,pp due to RV$\to$DR conversion in the high-$\bar{\kappa}$ schema; Table~\ref{tab:70b-docred-zs-ablation}).
35	The semantic layer is the sole effective defense (1.50\%\,$\to$\,0.60\%, 60\% reduction) with no R-F1 cost ($\Delta{=}$0\,pp), and full S1 eliminates all DR.
36	S2 eliminates DR but causes severe R-F1 degradation ($-$8.45\,pp), indicating that optimal constraint granularity is scale-dependent: the additional S2 constraints become overly restrictive at 70B, where stronger baseline generation makes fine-grained intervention counterproductive.
37	Beam ($k{=}4$) S1 remains the optimal configuration (DR${=}$0\%, CF${=}$1, R-F1${=}$44.81).
38	Notably, S2 increases CF from 15 (S1) to 18 despite its cross-field consistency design, suggesting that over-constraining induces cascading generation degradation that creates new violations.
39	
40	% exp_ids: eval_70b_lora_docred_200_unconstrained, eval_70b_lora_docred_200_grammar_only,
41	%          eval_70b_lora_docred_200_semantic_only, eval_70b_lora_docred_200_s1_constrained,
42	%          eval_70b_lora_docred_200_full_s2, eval_70b_lora_docred_200_beam4_s1
43	\paragraph{70B-class DocRED results.}
44	\label{app:70b-docred}
45	
46	Table~\ref{tab:70b-docred-ablation} presents the six-way constraint ablation on Llama-3.1-70B-Instruct (AWQ INT4) with LoRA fine-tuning on DocRED (998 documents).
47	
48	\begin{table}[h]
49	\centering
50	\small
51	\setlength{\tabcolsep}{3.6pt}
52	\begin{tabular}{@{}l rrrr rr@{}}
53	\toprule
54	\textbf{Mode}
55	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
56	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
57	\midrule
58	Unconstrained & 0.22 & 0.57 & 0 & 2      & 43.80 & 80.34 \\
59	Grammar       & 0.38 & 0    & 0 & 0.06\%$^\dagger$ & 43.96 & 80.13 \\
60	Semantic      & \textbf{0} & 0.51 & 0 & 0.21\%$^\dagger$ & 43.61 & 80.06 \\
61	S1            & \textbf{0} & 0 & 0 & 0.18\%$^\dagger$ & 43.95 & 79.38 \\
62	S2            & \textbf{0} & 0 & 0 & 0.34\%$^\dagger$ & 36.45 & 84.96 \\
63	Beam4 S1      & \textbf{0} & 0 & 0 & \textbf{0} & \textbf{48.14} & \textbf{85.57} \\
64	\bottomrule
65	\end{tabular}
66	\caption{70B-class (Llama-3.1-70B-Instruct (AWQ INT4)) LoRA ablation on DocRED (998 docs).
67	CF: violation count except $^\dagger$reported as percentage (raw count unavailable).
68	F1 $\times$100.
69	PF: greedy S1 12.5\% (25/200 docs), S2 0\% (0/200), beam4 S1 0.5\% (1/200).}
70	\label{tab:70b-docred-ablation}
71	\end{table}
72	
73	The DocRED LoRA ablation mirrors the SciERC pattern: grammar eliminates RV (0.57\%\,$\to$\,0\%) but DR increases slightly ($+$0.16\,pp); semantic-only independently eliminates DR (0.22\%\,$\to$\,0\%) but retains RV (0.51\%).
74	The complementary layer interaction is stable across datasets under LoRA fine-tuning.
75	S2 eliminates DR and parse failures (PF${=}$0\%) but causes severe R-F1 degradation ($-$7.50\,pp vs.\ S1), mirroring the SciERC pattern ($-$8.45\,pp; Table~\ref{tab:70b-ft-ablation}): at 70B, the repair layer over-constrains relation predictions where baseline DR is already near-zero (0.22\%).
76	CF increases from 0.18\% (S1) to 0.34\% (S2), confirming that over-constraining induces cascading inconsistencies across datasets.
77	The $+$4.19\,pp R-F1 gain from beam search (43.95\,$\to$\,48.14) is largely attributable to parse failure recovery: greedy S1 fails to parse 12.5\% of documents (25/200), while beam reduces this to 0.5\% (1/200), recovering $\sim$24 documents that contribute no triples under greedy decoding.
78	The controlled comparison on SciERC---where both greedy and beam achieve 0\% parse failure---isolates the pure beam quality gain at $+$0.28\,pp, consistent with the 8B pattern (Appendix~\ref{app:beam-search}).
79	
80	% exp_ids: r16_70b_docred_zs_unconstrained, r16_70b_docred_zs_grammar_only,
81	%          r16_70b_docred_zs_semantic_only
82	\paragraph{70B-class DocRED zero-shot ablation.}
83	\label{app:70b-docred-zs}
84	
85	Table~\ref{tab:70b-docred-zs-ablation} presents the layer ablation on DocRED under zero-shot decoding at 70B.
86	
87	\begin{table}[h]
88	\centering
89	\small
90	\setlength{\tabcolsep}{3.6pt}
91	\begin{tabular}{@{}l rrrr rr@{}}
92	\toprule
93	\textbf{Mode}
94	  & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF}
95	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$} \\
96	\midrule
97	Unconstrained & 13.45 & 7.88 & 0 & 0    & 13.25 & 70.14 \\
98	Grammar       & 17.03 & 0    & 0 & 0    & 13.23 & 70.12 \\
99	Semantic      & 1.66  & 8.24 & 0.12 & 132  & 13.05 & 70.10 \\
100	S1            & \textbf{0} & 0 & 0 & 173  & 13.25 & 70.05 \\
101	\bottomrule
102	\end{tabular}
103	\caption{70B-class zero-shot layer ablation on DocRED (200-document subset; baseline DR differs from \S\ref{sec:70b-results}'s 998-document evaluation).
104	CF: violation count. F1 $\times$100.}
105	\label{tab:70b-docred-zs-ablation}
106	\end{table}
107	
108	Grammar-only eliminates RV (7.88\%\,$\to$\,0\%) but DR increases by $+$3.58\,pp (13.45\%\,$\to$\,17.03\%): forced vocabulary mapping in DocRED's high-$\bar{\kappa}$ schema ($\bar{\kappa}{=}0.842$, ${\sim}$16\% type pairs valid) converts RV into DR violations.
109	Semantic-only independently achieves 87.7\% DR reduction (13.45\%\,$\to$\,1.66\%) with no R-F1 cost, confirming the pattern from SciERC (84\%; Table~\ref{tab:70b-ft-ablation}).
110	Full S1 eliminates all DR (13.45\%\,$\to$\,0\%) with zero R-F1 cost (13.25\,$=$\,13.25), confirming that the two layers compose correctly despite their opposing individual DR effects.
111	CF increases from 0 (unconstrained) to 173 (S1), consistent with the pattern that stricter constraint enforcement in ZS introduces more cross-field inconsistencies.
112	The two layers serve complementary roles: grammar provides the RV elimination foundation that semantic-layer DR enforcement requires, while the semantic layer addresses the DR that grammar alone cannot---and in high-$\bar{\kappa}$ schemas, exacerbates.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "795b7b1c-c2d8-4d59-91c7-2a5cd4895450",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "22b3578c-c1cb-4d40-91c9-231f40dbf3bf",
  "sourceToolAssistantUUID": "795b7b1c-c2d8-4d59-91c7-2a5cd4895450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T05:01:52.832Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LV8zgEx9TBdoZ7XcDT69nE`</summary>

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
  "parentUuid": "22b3578c-c1cb-4d40-91c9-231f40dbf3bf",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a7197c5-b1bb-4540-ad9d-d3f11df5df53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 18 · 2026-05-24T05:01:52.839Z_

<details><summary>↩ Tool result · `toolu_01LV8zgEx9TBdoZ7XcDT69nE`</summary>

```text
1	% Appendix C — Per-Relation Violation Analysis (Llama-3.1-8B)
2	% exp_ids: llama_docred_unconstrained, llama_docred_full_s1
3	
4	\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
5	
6	Table~\ref{tab:llama-per-relation-dr} presents the per-relation domain--range violation breakdown for Llama-3.1-8B on DocRED under S1 constraints.
7	The Llama baseline exhibits an RV rate of 16.03\%, substantially lower than Qwen's 29.66\%, which indicates stronger baseline vocabulary compliance.
8	% exp_ids: llama_docred_unconstrained (RV=16.03%), qwen_docred_unconstrained (RV=29.66%)
9	S1 completely eliminates RV violations and reduces the residual DR rate to 2.55\% (418/16{,}368 triples), with only three relations exceeding 10\%.
10	% exp_ids: llama_docred_full_s1 (DR=2.6%, 418/16368)
11	
12	\begin{table}[h]
13	\centering
14	\caption{Top 10 per-relation DR violation rates for Llama-3.1-8B on DocRED under S1 constraints. Relations with $>$20 triples and 0\% DR (e.g., P131, P206, P361, P170, P86) are omitted.}
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
36	Compared with Qwen, which retains a 10.21\% residual DR under S1 concentrated in P1198 (83\% fallback) and P171 (78\% fallback), Llama's residual DR on the same relations is markedly lower (P1198 reaches only 20.0\%) and no relation-level fallback concentration comparable to Qwen is observed.
37	% exp_ids: llama_docred_full_s1, qwen_docred_full_s1
38	The substantially lower residual DR for Llama (2.55\% vs.\ Qwen's 10.21\%) on the same ontology confirms that constraint tightness alone does not determine enforcement effectiveness: the model's baseline vocabulary compliance (RV) modulates the fraction of triples eligible for semantic-layer enforcement.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a7197c5-b1bb-4540-ad9d-d3f11df5df53",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "b3123309-981f-4466-9b3e-b76b9c20f46d",
  "sourceToolAssistantUUID": "9a7197c5-b1bb-4540-ad9d-d3f11df5df53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T05:01:53.309Z_

<details open><summary>🔧 Tool call — Read · `toolu_017hDtk4S2DkyYR8d6pSCjBN`</summary>

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
  "parentUuid": "b3123309-981f-4466-9b3e-b76b9c20f46d",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd140389-8019-4228-ac9a-edc5687fe284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 20 · 2026-05-24T05:01:53.315Z_

<details><summary>↩ Tool result · `toolu_017hDtk4S2DkyYR8d6pSCjBN`</summary>

```text
1	\section{Sampling Robustness}\label{app:sampling}
2	
3	\begin{table}[h]
4	\centering
5	\caption{Constraint robustness under nucleus sampling ($T$=0.7, $p$=0.9) vs.\ greedy decoding (Qwen3-8B, S1 constraints).}
6	\label{tab:sampling-robustness}
7	\resizebox{\columnwidth}{!}{%
8	\begin{tabular}{llcccccc}
9	\toprule
10	Dataset & Decoding & ET\% & RV\% & DR\% & CF\% & E-F1 & R-F1 \\
11	\midrule
12	\multirow{2}{*}{SciERC (551)} & Greedy & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
13	& Sampling & 0 & 0 & 0.75 & 9.90 & 31.28 & 7.42 \\
14	\midrule
15	\multirow{2}{*}{DocRED (114$^\dagger$)} & Greedy & 0 & 0.03 & 10.21 & 2.57 & 59.37 & 8.23 \\
16	& Sampling & 0 & 0 & 10.31 & 12.63 & 57.05 & 7.92 \\
17	\bottomrule
18	\end{tabular}}
19	\par\smallskip\footnotesize $^\dagger$Subset of 114 documents; full DocRED sampling requires ${\sim}300$h due to extended generation under high-temperature sampling with complex schemas.
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd140389-8019-4228-ac9a-edc5687fe284",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "8458c88c-f9f5-4cad-ad15-8c9e0efd1b71",
  "sourceToolAssistantUUID": "cd140389-8019-4228-ac9a-edc5687fe284",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T05:01:54.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_012tSmXbFYKAZhtW2viWwU9T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8458c88c-f9f5-4cad-ad15-8c9e0efd1b71",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15f33431-26df-4c8a-988b-8b3eaa26ca77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 22 · 2026-05-24T05:01:54.288Z_

<details><summary>↩ Tool result · `toolu_012tSmXbFYKAZhtW2viWwU9T`</summary>

```text
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
25	\label{tab:beam-search}
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{@{}llcccccc@{}}
28	\toprule
29	\textbf{Model / Dataset} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
30	\midrule
31	\multirow{2}{*}{Qwen3-8B / SciERC (551)}
32	  & Greedy      & 0 & 0 & 0.93 & 9.90 & 30.98 & 8.36 \\
33	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.53} & 32.00 & 8.56 \\
34	\midrule
35	\multirow{2}{*}{Qwen3-8B / DocRED (50)}
36	  & Greedy      & 0 & 0 & 8.69 & 2.08 & 59.08 & 8.33 \\
37	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.55} & 58.64 & 9.37 \\
38	\midrule
39	\multirow{2}{*}{Llama-3.1-8B / SciERC (551)}
40	  & Greedy      & 0 & 0 & 0.08 & 6.56 & 23.49 & 2.54 \\
41	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.93} & 25.04 & 3.33 \\
42	\midrule
43	\multirow{2}{*}{Llama-3.1-8B / DocRED (50)}
44	  & Greedy      & 0 & 0 & 1.58 & 6.85 & 55.35 & 6.12 \\
45	  & Beam ($k{=}4$) & 0 & 0 & \textbf{0} & \textbf{0.94} & 55.62 & 9.47 \\
46	\midrule
47	\multirow{2}{*}{Mistral-7B / SciERC (551)}
48	  & Greedy      & 0 & 0 & 13.40 & 1.27 & 27.46 & 3.67 \\
49	  & Beam ($k{=}4$) & 0 & 0 & 13.79 & \textbf{0.57} & 26.66 & 4.37 \\
50	\midrule
51	\multirow{2}{*}{Mistral-7B / DocRED (50)}
52	  & Greedy      & 0 & 0 & 28.37 & 0.34 & 51.60 & 4.19 \\
53	  & Beam ($k{=}4$) & 0 & 0 & \textbf{21.37} & \textbf{0.19} & 51.78 & 5.70 \\
54	\bottomrule
55	\end{tabular}}
56	\end{table}
57	
58	\paragraph{Discussion.}
59	For calibrated models (Qwen3-8B, Llama-3.1-8B), beam search achieves DR=0\% across all four model-dataset combinations (both SciERC with 6 entity types, 551 documents, and DocRED with 96 relation types, 50 documents), regardless of schema complexity.
60	On SciERC, beam search eliminates DR for both Qwen (0.93\%\,$\to$\,0\%) and Llama (0.08\%\,$\to$\,0\%), and substantially reduces CF (Qwen: 9.90\%\,$\to$\,0.53\%; Llama: 6.56\%\,$\to$\,0.93\%).
61	On DocRED (matched 50-document subsets), beam search eliminates DR for both Qwen (8.69\%\,$\to$\,0\%) and Llama (1.58\%\,$\to$\,0\%), with CF reductions of 74\% and 86\% respectively.
62	Llama DocRED shows the largest R-F1 gain ($+$3.4\,pp), consistent with beam search recovering valid type assignments that greedy decoding missed due to constraint fallback.
63	The CF reduction is an indirect effect: beam search reduces constraint-fallback frequency by exploring alternative token sequences that satisfy both grammar and semantic masks simultaneously, avoiding the fallback-to-grammar path that produces cross-field inconsistencies under greedy decoding.
64	
65	Mistral-7B-v0.3 constitutes a boundary condition on both datasets.
66	On SciERC (6 entity types), beam search does not reduce DR (13.4\%\,$\to$\,13.8\%), though CF drops by 55\% relative (1.27\%\,$\to$\,0.57\%) and R-F1 improves by $+$0.7\,pp; the unchanged DR confirms that all residual violations stem from entity type misclassification, not constraint-search failure.
67	On DocRED (96 relation types), beam search reduces DR by 25\% relative (28.4\%\,$\to$\,21.4\%): the more complex schema introduces constraint-search failures that beam exploration resolves, but the entity misclassification component remains.
68	This contrast reveals that beam search resolves constraint-search failure (where greedy decoding encounters $G(t) \cap S(t) = \emptyset$ conflicts) but cannot overcome fundamental model calibration limitations in entity typing.
69	
70	\paragraph{Beam width ablation.}
71	Table~\ref{tab:beam-ablation} varies beam width $k \in \{1,2,4,8\}$ on Qwen3-8B / SciERC (551 documents) under S1 constraints.
72	
73	\begin{table}[h]
74	\centering
75	\small
76	\caption{Effect of beam width on constraint satisfaction and extraction quality (Qwen3-8B, SciERC, 551 documents, S1 constraints). $k{=}1$ corresponds to greedy decoding.}
77	\label{tab:beam-ablation}
78	\begin{tabular}{@{}rcccc@{}}
79	\toprule
80	$k$ & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
81	\midrule
82	1 (greedy) & 0.93 & 9.90 & 30.98 & 8.36 \\
83	2          & 0.35 & 4.12 & 31.54 & \textbf{8.75} \\
84	4          & \textbf{0}    & 0.53 & 32.00 & 8.56 \\
85	8          & \textbf{0}    & \textbf{0.08} & \textbf{32.18} & 8.39 \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	DR elimination at $k{\geq}4$ confirms that constraint-search failure is resolved with moderate exploration width.
91	CF continues to decrease with larger beam (0.08\% at $k{=}8$, only 2 residual violations), while entity extraction quality improves monotonically.
92	$k{=}4$ represents the optimal cost-effectiveness trade-off: it eliminates all DR violations at roughly half the compute cost of $k{=}8$.
93	
94	\paragraph{Beam width--latency Pareto analysis (LoRA).}
95	% exp_id: d066_beam_sweep
96	Figure~\ref{fig:beam-pareto} and Table~\ref{tab:beam-sweep} extend the beam width analysis to LoRA fine-tuning, where the constrained--unconstrained interaction shifts qualitatively: LoRA + S1 already achieves DR=0\% at $k{=}1$ (greedy), so beam search targets CF reduction rather than DR elimination (contrast: zero-shot requires $k{\geq}4$ for DR=0\%).
97	Among constrained configurations, $k{=}2$ is Pareto optimal (R-F1 44.60, CF 0.11\%, 1.39$\times$ vs.\ greedy unconstrained; 1.18$\times$ vs.\ greedy S1); $k{\geq}4$ yields diminishing F1 returns with increasing latency (1.63--2.03$\times$).
98	
99	\begin{figure*}[ht]
100	\centering
101	\includegraphics[width=\textwidth]{figures/beam_pareto.pdf}
102	\caption{Beam width vs.\ R-F1 under LoRA fine-tuning. Left: SciERC (Qwen3-8B solid, Llama-3.1-8B dashed; 551 docs). Right: DocRED (Llama-3.1-8B, 200 docs). Bubble area $\propto$ total violation rate (DR+CF+RV); green rings mark zero-violation configurations. Star: Pareto-optimal ($k{=}2$).}
103	\label{fig:beam-pareto}
104	\end{figure*}
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Beam width sweep on SciERC (Qwen3-8B LoRA, 551 documents). \textsc{unc}: unconstrained; \textsc{con}: schema-constrained. Latency relative to $k{=}1$ unconstrained. Highlighted row: Pareto-optimal configuration.}
110	\label{tab:beam-sweep}
111	\resizebox{\columnwidth}{!}{%
112	\begin{tabular}{@{}cl cccc cc@{}}
113	\toprule
114	$k$ & Mode & E-F1 & R-F1 & DR (\%) & CF (\%) & Latency (s) & Rel.\ Lat. \\
115	\midrule
116	\multirow{2}{*}{1}
117	 & \textsc{unc} & 66.88 & 42.95 & 2.11 & 0    & 2.494 & 1.00$\times$ \\
118	 & \textsc{con} & 66.88 & 42.95 & \textbf{0} & 0.50 & 2.932 & 1.18$\times$ \\
119	\midrule
120	\multirow{2}{*}{2}
121	 & \textsc{unc} & 67.79 & 44.75 & 1.54 & 0    & 2.954 & 1.18$\times$ \\
122	 & \cellcolor{blue!8}\textsc{con} & \cellcolor{blue!8}67.71 & \cellcolor{blue!8}\textbf{44.60} & \cellcolor{blue!8}\textbf{0} & \cellcolor{blue!8}0.11 & \cellcolor{blue!8}3.463 & \cellcolor{blue!8}1.39$\times$ \\
123	\midrule
124	\multirow{2}{*}{4}
125	 & \textsc{unc} & 67.49 & 43.72 & 1.89 & 0    & 3.485 & 1.40$\times$ \\
126	 & \textsc{con} & 67.22 & 43.60 & \textbf{0} & 0    & 4.069 & 1.63$\times$ \\
127	\midrule
128	\multirow{2}{*}{8}
129	 & \textsc{unc} & 66.40 & 43.17 & 1.77 & 0    & 4.194 & 1.68$\times$ \\
130	 & \textsc{con} & 66.36 & 43.65 & \textbf{0} & 0    & 5.058 & 2.03$\times$ \\
131	\bottomrule
132	\end{tabular}}
133	\end{table}
134	
135	\paragraph{Composability with fine-tuning.}
136	Under greedy decoding, the fine-tuned Qwen3-8B (LoRA, SciERC) with S1 constraints already achieves DR=0\% but retains CF=1.18\% (22 cross-field violations across 551 documents), with E-F1=67.05 and R-F1=43.77.
137	Adding beam search ($k{=}4$) eliminates all residual CF violations (1.18\%\,$\to$\,0\%), yielding zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) while preserving extraction quality (E-F1=66.88, R-F1=43.60; changes within $\pm$0.5\,pp).
138	Llama-3.1-8B (LoRA, SciERC) with S1 constraints and beam search ($k{=}4$) likewise achieves zero violations across all four metrics (ET=0\%, RV=0\%, DR=0\%, CF=0\%) with R-F1=46.18; the zero-violation result thus generalizes across calibrated model families.
139	% exp_id: q1_llama_ft_beam_scierc
140	The three constraint mechanisms (grammar masking, semantic domain-range filtering, and beam exploration) are thus fully composable: each addresses a distinct violation source without interfering with the others or degrading task performance.
141	
142	The initial 50-document DocRED subset (Table~\ref{tab:beam-search}) was subsequently validated on the full 998-document set (Table~\ref{tab:beam-docred-998-zs}): both models achieve DR${=}$0\%, confirming subset representativeness.
143	Llama shows the larger improvement (CF 8.54\%\,$\to$\,1.00\%, 88\% reduction; R-F1 $+$2.6\,pp), consistent with beam search resolving constraint-search failures that greedy decoding cannot.
144	
145	\begin{table}[h]
146	\centering
147	\small
148	\caption{Zero-shot beam search ($k{=}4$) under S1 constraints on the full DocRED dev set (998 documents).
149	ET/RV/DR/CF: violation rates (\%); PF: parse failure rate (\%); F1 $\times$100.}
150	\label{tab:beam-docred-998-zs}
151	\begin{tabular}{@{}lcccccc@{}}
152	\toprule
153	\textbf{Model} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ \\
154	\midrule
155	Qwen3-8B  & 0 & 0 & \textbf{0} & 4.94 & 58.19 & 8.72 \\
156	Llama-3.1-8B & 0 & 0 & \textbf{0} & 1.00 & 57.81 & 8.83 \\
157	\bottomrule
158	\end{tabular}
159	\end{table}
160	
161	Table~\ref{tab:beam-docred-lora} reports LoRA + beam-4 results on the full DocRED dev set (998 documents), extending the fine-tuning composability evaluation from SciERC to the higher-$\bar{\kappa}$ regime.
162	Parse failure rates under LoRA beam-4 range from 1.3\% to 2.9\%, lower than the zero-shot rate.
163	
164	\begin{table}[h]
165	\centering
166	\small
167	\caption{LoRA greedy vs.\ beam search ($k{=}4$) on DocRED (998 dev documents) under S1 constraints.
168	ET = entity type, RV = relation vocabulary, DR = domain/range, CF = cross-field violation rates (\%); PF = parse failure rate (\%); F1 $\times$ 100.}
169	\label{tab:beam-docred-lora}
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{@{}llccccccc@{}}
172	\toprule
173	\textbf{Model} & \textbf{Decoding} & ET & RV & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ & PF \\
174	\midrule
175	\multirow{2}{*}{Qwen3-8B}
176	  & Greedy con & 0 & 0 & 0.01 & 0.41 & 81.43 & 40.56 & 8.52 \\ % d065_qwen_greedy_4096_r2
177	  & Beam-4 con & 0 & \textbf{0} & \textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\
178	\midrule
179	\multirow{2}{*}{Llama-3.1-8B}
180	  & Greedy con & 0 & 0 & 0.21 & 0.21 & 83.94 & 43.78 & 2.51 \\ % d065: 4096 context
181	  & Beam-4 con & 0 & 0 & 0 & \textbf{0} & \textbf{85.23} & \textbf{47.17} & \textbf{1.3} \\
182	\bottomrule
183	\end{tabular}}
184	\end{table}
185	
186	Llama-3.1-8B achieves zero violations across all four metrics (ET, RV, DR, CF = 0\%) on DocRED with LoRA + beam-4, extending the zero-violation result from SciERC to the high-$\bar{\kappa}$ regime.
187	Qwen3-8B achieves DR=0\% with near-zero CF (0.01\%); R-F1 is preserved ($\pm$0.06\,pp).
188	Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
189	
190	\paragraph{Latency overhead.}
191	Table~\ref{tab:beam-latency} reports wall-clock latency for greedy and beam search ($k{=}4$) under LoRA fine-tuning.
192	
193	\begin{table}[h]
194	\centering
195	\small
196	\begin{tabular}{@{}lrr@{}}
197	\toprule
198	\textbf{Condition} & \textbf{s/doc} & \textbf{Overhead} \\
199	\midrule
200	Greedy unconstrained   & 2.612 & 1.00$\times$ \\
201	Greedy constrained (S1)& 2.873 & 1.10$\times$ \\
202	Beam-4 unconstrained   & 3.446 & 1.32$\times$ \\
203	Beam-4 constrained (S1)& 4.013 & 1.54$\times$ \\
204	\bottomrule
205	\end{tabular}
206	\caption{Latency per document (SciERC, 551 docs, Qwen3-8B LoRA FT, RTX PRO 6000 Blackwell). Overhead relative to greedy unconstrained.}
207	\label{tab:beam-latency}
208	\end{table}
209	
210	Beam search itself adds 32\% latency (4 beams); constraint overhead increases from 10\% (greedy) to 17\% (beam) because each beam independently maintains grammar and semantic state.
211	Per-beam entity registry memory is $O(|\text{entities}|)$ per beam; at $k{=}8$ with typical document sizes, overhead is ${<}$1\,MB per beam, negligible relative to model memory.
212	The total 1.54$\times$ overhead is acceptable for offline batch IE; \texttt{early\_stopping} limits additional compute to partial-sequence exploration.
213	
214	We also explored a type-consensus constraint that forces identical entity types across all relations within a document.
215	However, CF violations occur precisely where the consensus type conflicts with domain-range constraints, creating a fundamental CF$\leftrightarrow$DR trade-off.
216	With DR-aware enforcement (skipping consensus when it would violate domain-range), the layer becomes a no-op (100\% skip rate on 551 SciERC documents and 50 DocRED documents).
217	This confirms that beam search resolves the CF$\leftrightarrow$DR tension through a fundamentally different mechanism: token-level exploration of paths satisfying both constraints simultaneously.
218	
219	\paragraph{TCR reranking under beam search.}
220	TCR reranking with beam search ($k{=}4$) showed no effect on either Qwen3-8B or Llama-3.1-8B under LoRA (0/551 SciERC candidates changed): fine-tuned beam candidates are already type-consistent (TCR score${=}$1.0 for all candidates), confirming that beam search implicitly subsumes post-hoc type consensus under fine-tuning.
221	This further strengthens the beam search deployment recommendation: beam not only eliminates all four violation types but also renders post-hoc CF resolution unnecessary.
222	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15f33431-26df-4c8a-988b-8b3eaa26ca77",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "fbcb0205-fb49-4a58-bf21-d86b27749b74",
  "sourceToolAssistantUUID": "15f33431-26df-4c8a-988b-8b3eaa26ca77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T05:01:54.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QdWH4HGh9AdunJxfmP73tP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbcb0205-fb49-4a58-bf21-d86b27749b74",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83beffc0-8a75-45c1-9056-5aacc7406a44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 24 · 2026-05-24T05:01:54.807Z_

<details><summary>↩ Tool result · `toolu_01QdWH4HGh9AdunJxfmP73tP`</summary>

```text
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
18	S1 constrained decoding adds $+$13.1\% wall-clock overhead on SciERC (Qwen3-8B, zero-shot greedy), lower on DocRED due to amortization over longer sequences; under LoRA fine-tuning, overhead is $+$10.0\% on SciERC.
19	
20	\paragraph{Greedy decoding determinism.}
21	\label{app:greedy-determinism}
22	% exp_id: d067_seed_variance
23	All main results use greedy decoding (temperature$\,{=}\,$0, argmax token selection).
24	Argmax is deterministic: the random seed controls \texttt{torch.manual\_seed} for sampling and dropout, neither of which is active during greedy inference.
25	We verify this with three seeds (42, 123, 456) across two LoRA fine-tuned models on all 551 SciERC documents.
26	Seeds 123 and 456, evaluated on the same GPU, produce byte-identical outputs for both Qwen3-8B and Llama-3.1-8B.
27	The residual variance in Table~\ref{tab:seed-variance} stems entirely from cross-hardware floating-point divergence: seed 42 was evaluated on a different server with a different CUDA driver version.
28	Even under this conservative upper bound, $\sigma(\text{E-F1}) \leq 0.16$\,pp, $\sigma(\text{R-F1}) \leq 0.43$\,pp, and $\sigma(\text{DR\%}) \leq 0.08$\,pp.
29	The constrained decoding DR\% reduction ($-$2.06\,pp for Qwen, $-$1.01\,pp for Llama) exceeds this variance by ${>}12\times$ (signal-to-noise ratio ${>}$\,12), confirming that observed improvements reflect genuine method effects rather than run-to-run noise.
30	We therefore report single-run results without error bars; bootstrap confidence intervals (10{,}000 iterations) are provided for F1 metrics.
31	
32	\begin{table}[h]
33	\centering
34	\caption{Cross-seed variance for LoRA fine-tuned models on SciERC (551 documents, greedy decoding, seeds 42/123/456). Values: mean $\pm$ population $\sigma$ across three seeds. Seeds 123 and 456 produce identical outputs on the same GPU; all observed $\sigma$ reflects cross-server floating-point divergence.}
35	\label{tab:seed-variance}
36	\small
37	\resizebox{\columnwidth}{!}{%
38	\begin{tabular}{@{}lllccc@{}}
39	\toprule
40	Model & Dataset & Mode & E-F1 & R-F1 & DR\% \\
41	\midrule
42	Qwen3-8B & SciERC & Unc & $66.94 \pm 0.08$ & $43.25 \pm 0.43$ & $2.06 \pm 0.08$ \\
43	Qwen3-8B & SciERC & Con & $66.94 \pm 0.08$ & $43.22 \pm 0.39$ & $0.00 \pm 0.00$ \\
44	Llama-3.1-8B & SciERC & Unc & $67.99 \pm 0.16$ & $45.38 \pm 0.05$ & $1.04 \pm 0.05$ \\
45	Llama-3.1-8B & SciERC & Con & $67.99 \pm 0.16$ & $45.40 \pm 0.05$ & $0.03 \pm 0.04$ \\
46	\bottomrule
47	\end{tabular}}
48	\end{table}
49	
50	\paragraph{Beam search non-determinism.}
51	Greedy decoding is deterministic (\S\ref{app:greedy-determinism} above).
52	Beam search ($k{\geq}2$) introduces non-determinism from GPU floating-point accumulation order; we report single-run results.
53	Based on the greedy cross-hardware variance ($\sigma < 0.5$\,pp, Table~\ref{tab:seed-variance}), beam search variance is expected to be of similar magnitude.
54	
55	\paragraph{200-document subset justification.}
56	\label{app:power-analysis}
57	The 70B LoRA evaluation on DocRED uses a 200-document subset (vs.\ the full 998-document dev set used for 8B models).
58	To verify that this subset provides sufficient statistical power, we conduct a bootstrap analysis using the full 998-document 8B LoRA results as a reference population.
59	Resampling 200 documents 5{,}000 times yields a relation F1 margin of error of $\pm$3.3 points (95\% CI) and a DR violation rate margin of error of $\pm$0.45 percentage points---precise enough to support our conclusions.
60	For zero-shot models, where DR violations are prevalent (15.0\% unconstrained), a 200-document subset achieves 100\% power to detect the constrained decoding effect (Cohen's $h = 0.80$); for fine-tuned models, where violations are already rare ($<$0.5\%), 94.9\% of 200-document subsamples correctly identify the direction of DR reduction, and the primary effect is established on the full 998-document evaluation.
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83beffc0-8a75-45c1-9056-5aacc7406a44",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "90c71eb9-a31e-4593-928c-94570404cf1a",
  "sourceToolAssistantUUID": "83beffc0-8a75-45c1-9056-5aacc7406a44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T05:01:55.186Z_

<details open><summary>🔧 Tool call — Read · `toolu_019R4DN8BS2hGqYerBFsNV9z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90c71eb9-a31e-4593-928c-94570404cf1a",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e374eb8a-78f6-45d9-a76e-64c71c54057a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 26 · 2026-05-24T05:01:55.193Z_

<details><summary>↩ Tool result · `toolu_019R4DN8BS2hGqYerBFsNV9z`</summary>

```text
1	% Appendix: Statistical Power Analysis for WikiEvents n=20
2	% Addresses reviewer concern about WikiEvents FT statistical power.
3	% Include via \input{appendix_power_analysis} in the appendix.
4	
5	\paragraph{Statistical power across evaluation settings.}
6	\label{app:power-analysis-full}
7	Table~\ref{tab:power-analysis} reports bootstrap confidence interval width and minimum detectable effect (MDE) for F1 across evaluation settings (${\geq}$1{,}000 bootstrap resamples; MDE at 80\% power, $\alpha{=}0.05$, paired test, $\rho{=}0.9$).
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\begin{tabular}{lrrr}
13	\toprule
14	\textbf{Dataset} & \textbf{$n$} & \textbf{95\% CI (F1)} & \textbf{MDE (F1)} \\
15	\midrule
16	SciERC & 551 & $\pm$1.8\,pp & 1.2\,pp \\
17	DocRED & 998 & $\pm$0.8\,pp & 0.5\,pp \\
18	DocRED (70B) & 200 & $\pm$3.3\,pp & 2.1\,pp \\
19	WikiEvents & 20 & $\pm$3.0\,pp & 2.0\,pp \\
20	\bottomrule
21	\end{tabular}
22	\caption{Statistical precision by dataset size.
23	95\% CI: bootstrap confidence interval half-width for per-configuration F1.
24	MDE: minimum detectable F1 difference at 80\% power ($\alpha{=}0.05$, paired test, conservative $\rho{=}0.9$).
25	SciERC/DocRED: zero-shot Rel-F1; DocRED (70B): LoRA Rel-F1 (200-doc subset); WikiEvents: LoRA Arg-F1.}
26	\label{tab:power-analysis}
27	\end{table}
28	
29	WikiEvents' $n{=}20$ yields an Arg-F1 margin of error of $\pm$3.0\,pp---comparable to the 200-document DocRED subset ($\pm$3.3\,pp)---with MDE${\approx}$2.0\,pp.
30	However, the primary WikiEvents claims concern violation elimination, not F1 improvement: RoV drops from 8.8--38.3\% to exactly 0\% across both models (bootstrap 95\% CI $[0\%,\,0\%]$ vs.\ $[2.4\%,\,15.4\%]$ / $[25.4\%,\,46.7\%]$; power${\approx}$1.0).
31	The small test set limits detection of subtle F1 shifts, but complete elimination of schema violations is unambiguous at $n{=}20$; the primary evidence for F1 preservation rests on SciERC ($n{=}551$) and DocRED ($n{=}998$), where CIs are ${\leq}$1.8\,pp.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e374eb8a-78f6-45d9-a76e-64c71c54057a",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "3f6fdcc6-a769-47c9-82c1-18662568aa55",
  "sourceToolAssistantUUID": "e374eb8a-78f6-45d9-a76e-64c71c54057a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T05:01:56.127Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CTWgkEBanGZkSv9V9eurUW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f6fdcc6-a769-47c9-82c1-18662568aa55",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13157eae-b052-4df9-b571-2d5951a0bf13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 28 · 2026-05-24T05:01:56.136Z_

<details><summary>↩ Tool result · `toolu_01CTWgkEBanGZkSv9V9eurUW`</summary>

```text
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
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{ll rrrrr rr}
13	\toprule
14	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
15	\midrule
16	Short (196)  & Uncon. &  1 &  5 &  57 & 0 &  63 & 32.4 &  8.9 \\
17	             & Const. &  0 &  0 &   5 & 5 &  10 & 32.4 &  8.9 \\
18	\midrule
19	Medium (180) & Uncon. &  6 &  9 & 104 & 0 & 119 & 27.8 &  6.7 \\
20	             & Const. &  0 &  0 &   7 & 15 & 22 & 27.8 &  6.7 \\
21	\midrule
22	Long (175)   & Uncon. &  3 & 10 & 104 & 1 & 118 & 29.9 &  7.0 \\
23	             & Const. &  0 &  0 &   4 & 20 & 24 & 30.0 &  7.3 \\
24	\bottomrule
25	\end{tabular}}
26	\end{table}
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\caption{Document length breakdown on DocRED (Qwen3-8B). Tertile boundaries: Short $\leq$ 160 words, Medium $\leq$ 208, Long $>$ 208.}
32	\label{tab:doc-length-docred}
33	\resizebox{\columnwidth}{!}{%
34	\begin{tabular}{ll rrrrr rr}
35	\toprule
36	\textbf{Bin} & \textbf{Mode} & \textbf{ET} & \textbf{RV} & \textbf{DR} & \textbf{CF} & \textbf{Total} & \textbf{E-F1} & \textbf{R-F1} \\
37	\midrule
38	Short (336)  & Uncon. & 177 & 1238 & 1021 &   9 & 2445 & 61.1 &  9.3 \\
39	             & Const. &   0 &    0 &  495 & 138 &  633 & 62.6 &  9.6 \\
40	\midrule
41	Medium (332) & Uncon. & 147 & 1742 & 1047 &   5 & 2941 & 59.3 &  7.9 \\
42	             & Const. &   0 &    5 &  544 & 180 &  729 & 60.7 &  8.5 \\
43	\midrule
44	Long (330)   & Uncon. & 176 & 2209 & 1162 &   3 & 3550 & 53.9 &  5.6 \\
45	             & Const. &   0 &    0 &  731 & 200 &  931 & 54.8 &  5.8 \\
46	\bottomrule
47	\end{tabular}}
48	\end{table}
49	
50	\begin{table}[h]
51	\centering
52	\small
53	\caption{Violation reduction percentage by document length bin (Qwen3-8B, S1 constraints).}
54	\label{tab:doc-length-reduction}
55	\resizebox{\columnwidth}{!}{%
56	\begin{tabular}{l rr rr}
57	\toprule
58	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{DocRED}} \\
59	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
60	\textbf{Bin} & \textbf{Viols (U$\to$C)} & \textbf{Red.\%} & \textbf{Viols (U$\to$C)} & \textbf{Red.\%} \\
61	\midrule
62	Short  & 63 $\to$ 10  & 84.1 & 2445 $\to$ 633  & 74.1 \\
63	Medium & 119 $\to$ 22 & 81.5 & 2941 $\to$ 729  & 75.2 \\
64	Long   & 118 $\to$ 24 & 79.7 & 3550 $\to$ 931  & 73.8 \\
65	\bottomrule
66	\end{tabular}}
67	\end{table}
68	
69	The violation reduction rate is consistent across all length bins: 80--84\% for SciERC and 74--75\% for DocRED.
70	Longer documents produce more violations in the unconstrained setting (e.g., DocRED long-bin: 3,550 vs.\ short-bin: 2,445), yet OntoCoDec achieves proportionally similar reduction; the constraint framework scales reliably with document complexity.
71	ET and RV violations are fully eliminated across all bins.
72	F1 scores are preserved or slightly improved under constrained decoding, with DocRED showing +0.9--1.5 E-F1 and +0.2--0.6 R-F1 improvement in the constrained setting.
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13157eae-b052-4df9-b571-2d5951a0bf13",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "91dd9ee0-aae7-4eab-ac6c-4498c252f2ab",
  "sourceToolAssistantUUID": "13157eae-b052-4df9-b571-2d5951a0bf13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T05:01:56.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VmyfLgPYAjhbg4D2aUPBQB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91dd9ee0-aae7-4eab-ac6c-4498c252f2ab",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f818fb2-f821-4517-8ce9-9343414c9844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 30 · 2026-05-24T05:01:56.605Z_

<details><summary>↩ Tool result · `toolu_01VmyfLgPYAjhbg4D2aUPBQB`</summary>

```text
1	\section{Prompt Sensitivity Analysis}
2	\label{app:prompt-sensitivity}
3	
4	To verify that OntoCoDec's constraint enforcement is robust to prompt variation, we evaluate three prompt variants on SciERC using Qwen3-8B (551 test documents): \textbf{Default} (the prompt used in all main experiments), \textbf{Minimal} (a shortened version listing only entity/relation types), and \textbf{Detailed} (an extended version with type definitions and extraction guidelines). All three variants share the same output JSON schema; only the instruction text differs. Each variant is decoded in both unconstrained and constrained (full Stage~1) modes.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Prompt sensitivity results on SciERC (551 documents). Top: Qwen3-8B; bottom: Llama-3.1-70B (AWQ INT4). ET, RV, DR denote entity-type, relation-vocabulary, and domain-range violation rates (\%), respectively. $\Delta$DR shows the relative reduction from unconstrained to constrained decoding.}
10	\label{tab:prompt-sensitivity}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{llcccccc}
13	\toprule
14	\textbf{Prompt} & \textbf{Mode} & \textbf{ET\%} & \textbf{RV\%} & \textbf{DR\%} & \textbf{$\Delta$DR} & \textbf{E-F1} & \textbf{R-F1} \\
15	\midrule
16	\multirow{2}{*}{Default}
17	  & Unconstrained & 0.40 & 1.39 & 15.37 & \multirow{2}{*}{94.0\%} & 31.01 & 8.23 \\
18	  & Constrained   & 0.00 & 0.00 &  0.93 &                         & 30.98 & 8.36 \\
19	\midrule
20	\multirow{2}{*}{Minimal}
21	  & Unconstrained & 0.58 & 1.16 & 16.91 & \multirow{2}{*}{94.6\%} & 31.98 & 7.91 \\
22	  & Constrained   & 0.00 & 0.00 &  0.92 &                         & 31.99 & 7.85 \\
23	\midrule
24	\multirow{2}{*}{Detailed}
25	  & Unconstrained & 0.22 & 0.45 & 11.07 & \multirow{2}{*}{94.2\%} & 33.55 & 10.48 \\
26	  & Constrained   & 0.00 & 0.00 &  0.64 &                         & 33.56 & 10.48 \\
27	\midrule
28	\multicolumn{8}{l}{\textit{Llama-3.1-70B-Instruct (AWQ INT4)}} \\
29	\midrule
30	\multirow{2}{*}{Default}
31	  & Unconstrained & 0.00 & 0.61 & 6.41 & \multirow{2}{*}{100\%} & 35.22 & 11.23 \\
32	  & Constrained   & 0.00 & 0.00 & 0.00 &                        & 35.19 & 11.24 \\
33	\midrule
34	\multirow{2}{*}{Minimal}
35	  & Unconstrained & 0.27 & 5.88 & 0.22 & \multirow{2}{*}{100\%} & 37.51 & 13.42 \\
36	  & Constrained   & 0.00 & 0.00 & 0.00 &                        & 37.22 & 11.35 \\
37	\midrule
38	\multirow{2}{*}{Detailed}
39	  & Unconstrained & 0.00 & 0.26 & 4.57 & \multirow{2}{*}{100\%} & 40.42 & 11.12 \\
40	  & Constrained   & 0.00 & 0.00 & 0.00 &                        & 40.35 & 11.16 \\
41	\bottomrule
42	\end{tabular}}
43	\end{table}
44	
45	Table~\ref{tab:prompt-sensitivity} shows that constrained decoding eliminates entity-type and relation-vocabulary violations entirely (ET and RV drop to 0\%) for all prompt variants at both scales. At 8B, domain-range violations are reduced by 94.0\%--94.6\% with a standard deviation of only 0.3\,pp across prompts; F1 scores remain effectively unchanged (max shift 0.13\,pp R-F1).
46	
47	At 70B, constrained decoding achieves DR${=}$0\% across all three prompts ($\Delta$DR${=}$100\%), consistent with the scale-dependent semantic layer interaction observed in the main experiments (\S\ref{sec:70b-results}). Baseline DR varies widely (0.22\%--6.41\%), yet constrained decoding converges to zero in all cases; CF is introduced as expected (0.62\%--3.50\%), consistent with the per-triple enforcement trade-off.
48	
49	Prompt variation has a measurable effect on baseline (unconstrained) violation rates at both scales: 8B DR ranges from 11.1\% (Detailed) to 16.9\% (Minimal); 70B from 0.22\% to 6.41\%. Under constrained decoding, this variance collapses, confirming that the mechanism is orthogonal to prompting and generalizes without prompt-specific tuning.
50	
51	% exp_id: sf2_70b_prompt_sensitivity
52	\paragraph{LoRA fine-tuned prompt invariance.}
53	Under LoRA fine-tuning at 70B, prompt invariance is preserved: Minimal and Detailed prompts both achieve DR${=}$0\% under S1, with CF at 0.62\% and 0.75\% respectively---consistent with the zero-shot 70B pattern above.
54	This confirms that OntoCoDec's constraint enforcement is robust to prompt variation across both zero-shot and fine-tuned regimes.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f818fb2-f821-4517-8ce9-9343414c9844",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "1b11187a-e808-4d38-b16a-7b59deb30067",
  "sourceToolAssistantUUID": "7f818fb2-f821-4517-8ce9-9343414c9844",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T05:01:57.094Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EHxTsTRvBSe12S97xv7aqt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b11187a-e808-4d38-b16a-7b59deb30067",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12464a19-7efc-4e57-9b76-f95eed64d557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 32 · 2026-05-24T05:01:57.101Z_

<details><summary>↩ Tool result · `toolu_01EHxTsTRvBSe12S97xv7aqt`</summary>

```text
1	% Appendix — Error Analysis and Case Studies
2	
3	\section{Error Analysis and Case Studies}
4	\label{app:case-studies}
5	
6	\definecolor{violation}{RGB}{220,50,50}
7	\definecolor{fixed}{RGB}{34,139,34}
8	\definecolor{cfwarn}{RGB}{200,120,0}
9	\newcommand{\viol}[1]{\textcolor{violation}{\st{#1}}}
10	\newcommand{\fixd}[1]{\textcolor{fixed}{\textbf{#1}}}
11	
12	We present four representative cases illustrating constraint behavior across violation types. Cases 1--3 demonstrate OntoCoDec's corrective mechanisms; Case 4 illustrates a limitation.
13	
14	\subsection{Domain-Range Correction}
15	\label{app:case-dr}
16	
17	\noindent\textbf{Input (SciERC, Qwen3-8B):} \textit{``We present a novel model-based approach to recover the shapes and the poses of transparent objects from known motion.''}
18	
19	The unconstrained model assigns \textsc{OtherScientificTerm} to ``shapes'' and ``poses,'' producing \textsc{Feature-of}(\textsc{Task}, \textsc{OtherScientificTerm}) triples that violate domain/range constraints. The semantic layer redirects the tail type to \textsc{Task}, yielding schema-compliant triples (Table~\ref{tab:case1}).
20	
21	\begin{table}[h]
22	\centering
23	\small
24	\caption{OntoCoDec corrects three Feature-of DR violations. \textcolor{violation}{Red}/\ding{55} = violation; \textcolor{fixed}{\textbf{green/bold}}/\ding{51} = corrected (shape markers provided for colorblind accessibility).}
25	\label{tab:case1}
26	\begin{tabular}{@{}p{3.2cm}lll@{}}
27	\toprule
28	\textbf{Triple} & \textbf{Head} & \textbf{Tail} & \textbf{DR} \\
29	\midrule
30	\multicolumn{4}{@{}l}{\textit{Unconstrained (3 violations)}} \\
31	\midrule
32	Feature-of(recover, shapes) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
33	Feature-of(recover, poses) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
34	Feature-of(recover, transp.\ obj.) & Task & \textcolor{violation}{OtherSciTerm} & \textcolor{violation}{\ding{55}} \\
35	Used-for(model approach, recover) & Method & Task & \ding{51} \\
36	\midrule
37	\multicolumn{4}{@{}l}{\textit{OntoCoDec (0 violations)}} \\
38	\midrule
39	Feature-of(recover, shapes) & Task & \textcolor{fixed}{Task} & \textcolor{fixed}{\ding{51}} \\
40	Feature-of(recover, poses) & Task & \textcolor{fixed}{Task} & \textcolor{fixed}{\ding{51}} \\
41	Used-for(model approach, recover) & Method & Task & \ding{51} \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	\subsection{Dual-Layer Vocabulary and Type Correction}
47	\label{app:case-rv-dr}
48	
49	\noindent\textbf{Input (DocRED, Qwen3-8B):} \textit{``Skai TV is a Greek free-to-air television network based in Piraeus. It is part of the Skai Group, one of the largest media groups in the country.''}
50	
51	The unconstrained model generates natural-language relation names (e.g., ``country of origin'') instead of Wikidata P-codes, triggering RV violations. The grammar layer forces valid P-codes; the semantic layer ensures type compatibility (Table~\ref{tab:case2}).
52	
53	\begin{table}[h]
54	\centering
55	\small
56	\caption{Layer~1 eliminates RV violations; Layer~2 corrects DR types on DocRED.}
57	\label{tab:case2}
58	\resizebox{\columnwidth}{!}{%
59	\begin{tabular}{@{}p{4.5cm}p{1.8cm}p{1.2cm}@{}}
60	\toprule
61	\textbf{Unconstrained Output} & \textbf{Violation} & \textbf{Type} \\
62	\midrule
63	rel=``country of origin'' & Not in schema & RV \\
64	rel=``headquarters location'' & Not in schema & RV \\
65	rel=``part of'' & Not in schema & RV \\
66	rel=``location of formation'' & Not in schema & RV \\
67	\midrule
68	\textbf{OntoCoDec Output} & & \\
69	\midrule
70	rel=P495 (Skai TV, Greece) & ORG$\to$LOC & \ding{51} \\
71	rel=P159 (Skai TV, Piraeus) & ORG$\to$LOC & \ding{51} \\
72	rel=P127 (Skai TV, Skai Group) & ORG$\to$ORG & \ding{51} \\
73	rel=P17 (Piraeus, Greece) & LOC$\to$LOC & \ding{51} \\
74	\bottomrule
75	\end{tabular}}
76	\end{table}
77	
78	\subsection{Scale Effect on Schema Compliance}
79	\label{app:case-scale}
80	
81	\noindent\textbf{Input (SciERC):} \textit{``This paper investigates the utility of applying standard MT evaluation methods (BLEU, NIST, WER and PER) to building classifiers to predict semantic equivalence and entailment.''}
82	
83	Both Qwen3-8B and Llama-3.1-70B-Instruct (AWQ INT4) mistype ``MT evaluation methods'' as \textsc{Method} (gold: \textsc{Metric}), but the downstream constraint behavior differs (Table~\ref{tab:case3}). The 70B model produces fewer violations (2 vs.\ 4) and chooses a different relation (Part-of vs.\ Hyponym-of), yet OntoCoDec corrects both.
84	
85	\begin{table}[h]
86	\centering
87	\small
88	\caption{8B vs.\ 70B on the same input. OntoCoDec corrects violations at both scales; CF arises when type corrections conflict with entity-list assignments.}
89	\label{tab:case3}
90	\resizebox{\columnwidth}{!}{%
91	\begin{tabular}{@{}llll@{}}
92	\toprule
93	\textbf{Setting} & \textbf{Relation} & \textbf{Types} & \textbf{DR} \\
94	\midrule
95	\multicolumn{4}{@{}l}{\textit{Qwen3-8B Unconstrained}} \\
96	Hyponym-of(MT eval, BLEU) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
97	Hyponym-of(MT eval, NIST) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
98	Hyponym-of(MT eval, WER) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
99	Hyponym-of(MT eval, PER) & Meth$\to$\textcolor{violation}{Metric} & \textcolor{violation}{\ding{55}} \\
100	\midrule
101	\multicolumn{4}{@{}l}{\textit{Qwen3-8B OntoCoDec}} \\
102	Hyponym-of(MT eval, BLEU) & Meth$\to$\textcolor{fixed}{Meth} & \textcolor{fixed}{\ding{51}} \\
103	Hyponym-of(MT eval, NIST) & Meth$\to$\textcolor{fixed}{Meth} & \textcolor{fixed}{\ding{51}} \\
104	\multicolumn{3}{@{}l}{\textcolor{cfwarn}{CF: BLEU typed Metric in entity list, Method in relation}} \\
105	\midrule
106	\multicolumn{4}{@{}l}{\textit{Llama-3.1-70B Unconstrained}} \\
107	Part-of(BLEU, MT eval) & Metric$\to$\textcolor{violation}{Meth} & \textcolor{violation}{\ding{55}} \\
108	Part-of(NIST, MT eval) & Metric$\to$\textcolor{violation}{Meth} & \textcolor{violation}{\ding{55}} \\
109	\midrule
110	\multicolumn{4}{@{}l}{\textit{Llama-3.1-70B OntoCoDec}} \\
111	Part-of(BLEU, MT eval) & Metric$\to$\textcolor{fixed}{Generic} & \textcolor{fixed}{\ding{51}} \\
112	Part-of(NIST, MT eval) & Metric$\to$\textcolor{fixed}{Generic} & \textcolor{fixed}{\ding{51}} \\
113	\bottomrule
114	\end{tabular}}
115	\end{table}
116	
117	\subsection{Limitation: Trajectory Divergence under Constraints}
118	\label{app:case-cf}
119	
120	\noindent\textbf{Input (SciERC, Mistral-7B):} \textit{``Amorph recognizes NE items in two stages: dictionary lookup and rule application.''}
121	
122	The gold annotation types ``Amorph'' as \textsc{Method} and ``NE items'' as \textsc{OtherScientificTerm}, with Used-for(Amorph, NE items). The unconstrained model mistypes ``Amorph'' but coincidentally produces the correct relation. Under OntoCoDec, modified token probabilities alter the generation trajectory entirely and produce a different (non-gold) relation (Table~\ref{tab:case4}). This illustrates a fundamental property of autoregressive generation under modified distributions: constraint enforcement can change the entire output path, not just individual token choices.
123	
124	\begin{table}[h]
125	\centering
126	\small
127	\caption{Constrained decoding changes the generation trajectory. The unconstrained model coincidentally produced the gold triple despite type errors.}
128	\label{tab:case4}
129	\resizebox{\columnwidth}{!}{%
130	\begin{tabular}{@{}p{4.2cm}ll@{}}
131	\toprule
132	\textbf{Setting} & \textbf{Output} & \textbf{Gold?} \\
133	\midrule
134	\textbf{Gold} & Used-for(Amorph\textsuperscript{Meth}, NE items\textsuperscript{OtherSci}) & -- \\
135	\midrule
136	\textbf{Unconstr.} & Used-for(Amorph\textsuperscript{OtherSci}, NE items\textsuperscript{Task}) & \textcolor{fixed}{\ding{51}} \\
137	\midrule
138	\textbf{OntoCoDec} & Used-for(Amorph\textsuperscript{OtherSci}, recognizes\textsuperscript{Gen}) & \textcolor{violation}{\ding{55}} \\
139	 & Feature-of(NE items\textsuperscript{Task}, in two stages\textsuperscript{Gen}) & \textcolor{violation}{\ding{55}} \\
140	\bottomrule
141	\end{tabular}}
142	\end{table}
143	
144	\subsection{Error Analysis: Constraint Impact on Prediction Quality}
145	\label{app:error-analysis}
146	
147	% exp_id: w5_lora_scierc_full_s1_eval (514 FN, 668 FP, 21 CF)
148	We analyze errors from Qwen3-8B LoRA + S1 on SciERC (551 documents; R-F1 43.77, 460 TP, 668 FP, 514 FN) across three categories.
149	
150	\paragraph{False negatives: constraint-blocked vs.\ model-limited.}
151	Of 514 false negatives, only one (0.2\%) is attributable to constraint enforcement:
152	
153	\noindent\textit{fn\_001} (constraint-blocked): ``\textit{Experiments on the TREC Blog track test set show that both groups of credibility indicators significantly improve retrieval effectiveness.}'' \\
154	Gold: Evaluate-for(retrieval effectiveness\textsuperscript{Metric}, credibility indicators\textsuperscript{OtherSci}).
155	The unconstrained model generates this triple correctly, but under S1, conflicting type assignments to `credibility indicators' (OtherScientificTerm in entity list vs.\ Method in Evaluate-for's tail) trigger a CF violation, redirecting generation to a reversed Used-for triple.
156	
157	\noindent\textit{fn\_004} (relation type confusion): ``\textit{Amorph recognizes NE items in two stages: dictionary lookup and rule application.}'' \\
158	Gold: Part-of(dictionary lookup\textsuperscript{Meth}, Amorph\textsuperscript{Meth}).
159	The model predicts Used-for instead of Part-of---both are schema-valid for Method$\to$Method pairs, so constraints provide no corrective signal. This Part-of$\leftrightarrow$Used-for confusion is the dominant FN pattern.
160	
161	\paragraph{False positives: schema-valid but incorrect.}
162	
163	\noindent\textit{fp\_001} (wrong relation type): Same sentence as fn\_004. The model generates Used-for(dictionary lookup, Amorph) where gold is Part-of. Used-for is the majority relation in SciERC (56\% of all relations), causing systematic over-prediction. Since both relation types are schema-valid for the entity type pair, constraints cannot distinguish them.
164	
165	\noindent\textit{fp\_007} (hallucinated relation): ``\textit{The classifiers show little gain from information about meeting context.}'' \\
166	No gold relation exists. The model generates Used-for(meeting context\textsuperscript{OtherSci}, classifiers\textsuperscript{Meth}), ignoring the negation in ``show little gain from.'' The instrumental preposition ``from'' triggers relation generation despite the negative result.
167	
168	\paragraph{CF violations: entity type polysemy.}
169	
170	\noindent\textit{cf\_001} (Generic$\leftrightarrow$Method): ``\textit{A basic reason behind this is that the overall approach extends the approach described in a companion paper\ldots}'' \\
171	The entity `approach' receives Generic in one Used-for relation and Method in another. The gold type is Generic; the polysemy of `approach' (generic reference vs.\ specific method) causes per-relation type assignment to diverge.
172	
173	\noindent\textit{cf\_005} (Material$\leftrightarrow$Task): ``\textit{Experimental evaluations on two challenging person re-identification datasets demonstrate the superiority of the proposed model\ldots}'' \\
174	The compound noun `person re-identification datasets' contains both a task component and a data component. The model assigns Material in one Evaluate-for relation and Task in another within the same sentence.
175	
176	\paragraph{Summary.}
177	Structural constraints eliminate type-invalid outputs (DR$\leq$0.21\%), but semantic ambiguity within schema-valid space---relation type confusion, entity type polysemy---remains the dominant error source. Only 1 of 514 false negatives (0.2\%) was attributable to constraint enforcement, confirming that the recall cost of type constraints is negligible.
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12464a19-7efc-4e57-9b76-f95eed64d557",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "24ae3015-94b7-4505-b75b-61749dd08ca7",
  "sourceToolAssistantUUID": "12464a19-7efc-4e57-9b76-f95eed64d557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T05:01:58.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VMVbDmxqNxwneNLcxtfvb7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24ae3015-94b7-4505-b75b-61749dd08ca7",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "133c72a4-8c27-473c-9886-75817345de8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 34 · 2026-05-24T05:01:58.017Z_

<details><summary>↩ Tool result · `toolu_01VMVbDmxqNxwneNLcxtfvb7`</summary>

```text
1	\paragraph{Downstream impact of violation removal.}
2	\label{app:downstream-impact}
3	
4	A natural concern with schema-constrained decoding is whether enforcing ontological validity removes \emph{lucky violations}---predictions that happen to be correct (true positives) yet violate the schema.
5	To quantify this trade-off, we audit all true-positive relation triples produced by unconstrained fine-tuned models and check whether any of them carry a domain--range (DR) violation, i.e., an entity-type pair \mbox{$\langle h_\tau, t_\tau \rangle$} not sanctioned by the ontology for that relation.
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\begin{tabular}{llrrrl}
11	\toprule
12	\textbf{Dataset} & \textbf{Model} & \textbf{TP} & \textbf{Lucky} & \textbf{\%\,TP} & \textbf{R drop} \\
13	\midrule
14	SciERC & Qwen-LoRA  & 461  & 4 & 0.87\% & 0.41\,pp \\
15	SciERC & Llama-LoRA & 467  & 5 & 1.07\% & 0.51\,pp \\
16	DocRED & Qwen-LoRA  & 5746 & 1 & 0.02\% & 0.01\,pp \\
17	DocRED & Llama-LoRA & 6226 & 1 & 0.02\% & 0.01\,pp \\
18	\bottomrule
19	\end{tabular}
20	\caption{Lucky violations: true-positive triples that carry a domain--range violation. \textbf{Lucky} counts such triples; \textbf{R drop} is the recall decrease (in percentage points) if they were removed.}
21	\label{tab:lucky-violations-detail}
22	\end{table}
23	
24	Across all four configurations, lucky violations account for at most 1.07\% of true positives (5 out of 467 on SciERC with Llama-LoRA) and as few as 0.02\% on DocRED.
25	The corresponding recall drop is negligible---at most 0.51 percentage points---while the vast majority of violated triples that constraints remove are false positives.
26	For example, on DocRED with Qwen-LoRA, constraints eliminate 164 schema-violating predictions but only 1 of them is actually correct; the other 163 are errors that would pollute a downstream knowledge graph.
27	
28	Inspecting the lucky violations qualitatively, they arise from borderline entity-type assignments rather than genuine schema gaps.
29	On SciERC, the recurring pattern involves \textsc{Metric}-typed entities (e.g., BLEU, NIST) appearing as heads of \texttt{Hyponym-of} relations, a pair absent from the training ontology because these metrics are rarely annotated as hyponyms.
30	On DocRED, the single lucky violation stems from an entity typed as \textsc{Misc} instead of \textsc{Org} (``Assassin's Creed Unity''), making its \texttt{developer} relation invalid under the schema despite being factually correct.
31	
32	These findings confirm that schema-constrained decoding introduces a minimal recall cost while providing a substantial precision gain.
33	Retaining these few lucky violations would allow schema-invalid triples into the knowledge graph, undermining the structural guarantees that motivate constrained decoding in the first place.
34	The net effect is overwhelmingly positive: constraints act as a high-precision filter that removes far more erroneous triples than correct ones.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "133c72a4-8c27-473c-9886-75817345de8c",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "97fd0efb-37e2-468a-ad7a-e7f71fcec461",
  "sourceToolAssistantUUID": "133c72a4-8c27-473c-9886-75817345de8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T05:01:58.484Z_

<details open><summary>🔧 Tool call — Read · `toolu_01931PA45GwBECw8tLyuVfQ2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97fd0efb-37e2-468a-ad7a-e7f71fcec461",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ef23d54-6e8c-471a-9fdd-b436221b7467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 36 · 2026-05-24T05:01:58.495Z_

<details><summary>↩ Tool result · `toolu_01931PA45GwBECw8tLyuVfQ2`</summary>

```text
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
22	Full constraint compilation (schema parsing + grammar build) scales sub-linearly (0.32\,s to 0.42\,s for 7$\to$1{,}000 relations; Table~\ref{tab:scalability}); within this, the XGrammar automaton accounts for $\sim$0.044\,s and semantic constraint compilation grows linearly but remains negligible (0.4\,ms to 17\,ms).
23	Inference overhead is constant at 2--3\% because XGrammar uses precompiled bitmasks ($O(1)$ per token) and the semantic layer checks only the active relation's domain/range set rather than the full ontology.
24	The practical limit is first-token uniqueness: when entity types exceed $\sim$200, prefix collisions in the tokenizer vocabulary may require fallback to multi-token disambiguation (\S\ref{sec:dynamic-masking}).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ef23d54-6e8c-471a-9fdd-b436221b7467",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "b9547410-1e11-40c3-b5f3-4e3810e861f8",
  "sourceToolAssistantUUID": "7ef23d54-6e8c-471a-9fdd-b436221b7467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T05:01:58.954Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Lx57ahkfs1ZrmmQdmctZ7w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9547410-1e11-40c3-b5f3-4e3810e861f8",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3df640f0-1b62-4278-832c-a7baf3f3239c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 38 · 2026-05-24T05:01:58.962Z_

<details><summary>↩ Tool result · `toolu_01Lx57ahkfs1ZrmmQdmctZ7w`</summary>

```text
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
16	LoRA unconstrained & 67.05 & 43.86 & 1.95 & 0 \\
17	LoRA + S1 & 67.05 & 43.77 & \textbf{0} & 1.18 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Full fine-tuning vs.\ LoRA on SciERC (Qwen3-8B, 551 docs). Constraints eliminate DR under both methods. Full FT underperforms LoRA, likely due to an untuned learning rate ($2{\times}10^{-4}$, standard for LoRA but high for full FT). F1 is unaffected by constraints in both cases.}
21	\label{tab:full-ft}
22	\end{table}
23	
24	Full fine-tuning retains 2.74\% DR violations (30 triples), concentrated in Part-of (14.6\%), Hyponym-of (9.6\%), and Evaluate-for (8.4\%). S1 eliminates all 30 violations with no F1 cost, demonstrating that constraint enforcement remains necessary even after full parameter updates. The CF$\leftrightarrow$DR trade-off persists (CF 0\%$\to$1.31\%), consistent with the LoRA pattern (1.18\%).
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df640f0-1b62-4278-832c-a7baf3f3239c",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "45781ee8-f8b9-4942-a968-ccc740434b75",
  "sourceToolAssistantUUID": "3df640f0-1b62-4278-832c-a7baf3f3239c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T05:01:59.902Z_

<details open><summary>🔧 Tool call — Read · `toolu_019vAtfozmfVjhC1Zftubkqq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45781ee8-f8b9-4942-a968-ccc740434b75",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1f01144-fb38-4e99-aaed-d317f6c18205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 40 · 2026-05-24T05:01:59.909Z_

<details><summary>↩ Tool result · `toolu_019vAtfozmfVjhC1Zftubkqq`</summary>

```text
1	% Appendix: Post-hoc Type Consistency Resolution (TCR)
2	% exp_ids: d065_tcr_pilot (all 10 configs)
3	
4	\section{Post-hoc Type Consistency Resolution}
5	\label{app:tcr}
6	
7	S1 enforces domain/range constraints per-triple but does not enforce global entity type consensus, leaving residual CF violations where the same entity receives different types across triples.
8	We evaluate a post-hoc resolution step (TCR): for each entity with conflicting type assignments, TCR selects the type that maximizes satisfaction count across all relations referencing that entity, subject to domain/range constraints.
9	Unlike naive majority voting (which ignores relational constraints and increases DR), TCR is constraint-aware: candidate types are scored by how many of the entity's relational contexts they satisfy.
10	TCR runs after S1 decoding completes and has access to the full document context.
11	
12	% ──────────────────────────────────────────
13	%  Table: TCR results on SciERC
14	% ──────────────────────────────────────────
15	\begin{table}[h]
16	\centering
17	\small
18	\resizebox{\columnwidth}{!}{%
19	\begin{tabular}{@{}ll rr rr r r@{}}
20	\toprule
21	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
22	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
23	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
24	\midrule
25	\multirow{3}{*}{Zero-shot}
26	  & Qwen    & 9.75 & \textbf{0} & 0.93  & 1.21  & $-$1.29 & 2.04 \\
27	  & Llama   & 6.40 & \textbf{0} & 0.08  & 0.30  & $-$1.78 & 1.85 \\
28	  & Mistral & 0.67 & \textbf{0} & 13.36 & 12.87 & $+$0.05 & 0 \\
29	\midrule
30	\multirow{2}{*}{LoRA}
31	  & Qwen    & 1.19 & \textbf{0} & 0     & 0     & $-$0.75 & 0 \\
32	  & Llama   & 0.46 & \textbf{0} & 0.09  & 0.09  & $-$0.18 & 0 \\
33	\bottomrule
34	\end{tabular}}
35	\caption{TCR on SciERC ($\bar{\kappa}{=}0.333$, 551 docs).
36	Pre/Post: before/after TCR.
37	$\Delta$E-F1: entity F1 change (F1$\times$100).
38	Fund.: percentage of conflicting entities where no single type satisfies all relational constraints (fundamental conflicts).
39	TCR eliminates all CF with DR increases $\leq$0.28\,pp; fundamental conflicts are 0--2\%.}
40	\label{tab:tcr-scierc}
41	\end{table}
42	
43	% ──────────────────────────────────────────
44	%  Table: TCR results on DocRED
45	% ──────────────────────────────────────────
46	\begin{table}[h]
47	\centering
48	\small
49	\resizebox{\columnwidth}{!}{%
50	\begin{tabular}{@{}ll rr rr r r@{}}
51	\toprule
52	& & \multicolumn{2}{c}{\textbf{CF (\%)}} & \multicolumn{2}{c}{\textbf{DR (\%)}} & \textbf{$\Delta$E-F1} & \textbf{Fund.} \\
53	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-7} \cmidrule(l){8-8}
54	\textbf{Config} & \textbf{Model} & Pre & Post & Pre & Post & (pp) & (\%) \\
55	\midrule
56	\multirow{3}{*}{Zero-shot}
57	  & Qwen    & 13.11 & \textbf{0} & 10.21 & 11.74 & $-$3.44 & 13.52 \\
58	  & Llama   & 23.71 & \textbf{0} &  2.55 & 11.93 & $-$5.21 & 22.78 \\
59	  & 70B     & 11.61 & \textbf{0} &  0    &  4.20 & $-$5.98 & 18.26 \\
60	\midrule
61	\multirow{2}{*}{LoRA}
62	  & Qwen    &  0.42 & \textbf{0} &  0.01 &  0.14 & $-$0.16 & 12.16 \\
63	  & Llama   &  0.36 & \textbf{0} &  0.21 &  0.20 & $-$0.17 & 11.59 \\
64	\bottomrule
65	\end{tabular}}
66	\caption{TCR on DocRED ($\bar{\kappa}{=}0.842$, 998 docs).
67	Under zero-shot, TCR introduces substantial DR regressions (up to $+$9.38\,pp for Llama) and E-F1 drops (up to $-$5.98\,pp for 70B).
68	Fundamental conflict rates are 12--23\%, an order of magnitude higher than SciERC.
69	Under LoRA, low baseline CF (0.36--0.42\%) limits both TCR impact and DR cost.}
70	\label{tab:tcr-docred}
71	\end{table}
72	
73	\paragraph{Analysis.}
74	TCR effectiveness varies inversely with schema constraint tightness $\bar{\kappa}$ (descriptive pattern across two schemas).
75	On SciERC ($\bar{\kappa}{=}0.333$), fundamental conflicts constitute 0--2\% of type disagreements: most conflicts are resolvable because the loose schema admits many valid type pairs, and TCR can find a type satisfying all relational contexts.
76	DR increases are bounded ($\leq$0.28\,pp), and E-F1 cost is modest ($\leq$1.78\,pp in zero-shot, $\leq$0.75\,pp under LoRA).
77	On DocRED ($\bar{\kappa}{=}0.842$), 13--23\% of conflicts are fundamental: the tight schema renders most type pairs invalid, so unifying an entity's type across all its relational contexts inevitably violates some domain/range constraints.
78	This produces severe DR regressions under zero-shot (Llama: 2.55\%$\to$11.93\%; 70B: 0\%$\to$4.20\%), where baseline CF is high enough that many entities require resolution.
79	Under LoRA, baseline CF is already low (0.36--0.42\%), limiting both the scope for TCR improvement and the DR cost.
80	
81	This $\bar{\kappa}$-dependent boundary is consistent with the constraint tightness analysis in \S\ref{sec:composition}: $\bar{\kappa}$ characterizes not only the decoding-time DR residual regime but also the feasibility of post-hoc type resolution.
82	Beam search (\S\ref{sec:beam-results}) resolves CF and DR simultaneously across all $\bar{\kappa}$ values (SciERC and DocRED (998 docs): DR$\to$0\% for calibrated models), making it the preferred approach for high-tightness schemas.
83	TCR is a zero-cost complement for low-tightness schemas where beam search latency (1.39$\times$) is undesirable.
84	Integrating TCR into the decoding loop would require global optimization over all generated triples, conflicting with the autoregressive generation paradigm.
85	TCR is complementary to OntoCoDec---it addresses CF (which OntoCoDec's per-triple enforcement cannot prevent) while OntoCoDec addresses DR (which post-hoc correction cannot guarantee).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1f01144-fb38-4e99-aaed-d317f6c18205",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "8b1e109f-487b-4602-8a0c-85fce5edff11",
  "sourceToolAssistantUUID": "f1f01144-fb38-4e99-aaed-d317f6c18205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T05:02:00.318Z_

<details open><summary>🔧 Tool call — Read · `toolu_017AkjGF7J9JRkxva6TKYoHh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b1e109f-487b-4602-8a0c-85fce5edff11",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec75b15a-b8ea-43ed-82ed-c747d5565f71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 42 · 2026-05-24T05:02:00.325Z_

<details><summary>↩ Tool result · `toolu_017AkjGF7J9JRkxva6TKYoHh`</summary>

```text
1	% Appendix: Constraint Tightness Case Study
2	% Data source: case_study_kappa_dr_dddc01.md (Qwen-2.5-7B zero-shot unconstrained)
3	
4	\section{Constraint Tightness Case Study}
5	\label{app:kappa-case-study}
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\resizebox{\columnwidth}{!}{%
11	\begin{tabular}{@{}llccc l@{}}
12	\toprule
13	\textbf{Relation} & \textbf{Dataset} & $\kappa$ & \textbf{DR\%} & $n$ & \textbf{Explanation} \\
14	\midrule
15	\multicolumn{6}{@{}l}{\textit{Highest DR violation rate}} \\
16	basin country        & DocRED & .97 & 74.6 &  63 & Sole valid pair \textsc{loc}$\to$\textsc{loc}; head mistyped as \textsc{org}/\textsc{misc} \\
17	product produced     & DocRED & .94 & 67.2 &  61 & Requires \textsc{org} head; model assigns \textsc{loc}/\textsc{per} \\
18	participant of       & DocRED & .81 & 58.6 & 326 & Hallucinated \textsc{event} type; \textsc{per}$\leftrightarrow$event confusion \\
19	\textsc{Compare}     & SciERC & .53 & 42.4 &  66 & Cross-category pairs violate same-type constraint \\
20	\textsc{Feature-of}  & SciERC & .28 & 33.5 & 486 & Fuzzy Task/OtherScientificTerm boundary \\
21	\midrule
22	\multicolumn{6}{@{}l}{\textit{High $\kappa$ with zero violations (DR = 0\%)}} \\
23	lyrics by            & DocRED & .94 &  0.0 &   9 & Unambiguous \textsc{per}$\to$\textsc{misc}; creative roles rarely mistyped \\
24	place of birth       & DocRED & .92 &  0.0 & 157 & Unambiguous \textsc{per}$\to$\textsc{loc}; no type confusion \\
25	place of death       & DocRED & .89 &  0.0 &  60 & Strong \textsc{per}$\to$\textsc{loc} prior; mirrors place of birth \\
26	subsidiary           & DocRED & .86 &  0.0 &   5 & Clear \textsc{org}$\to$\textsc{org} corporate semantics \\
27	father               & DocRED & .81 &  0.0 &  69 & Clear \textsc{per}$\to$\textsc{per} kinship semantics \\
28	\bottomrule
29	\end{tabular}}
30	\caption{Per-relation $\kappa$ vs.\ DR violation rate (Qwen3-8B, zero-shot, unconstrained).
31	High $\kappa$ is necessary but not sufficient for high DR: relations with unambiguous entity types (place of birth, $\kappa{=}0.92$) have zero violations, while equally tight relations with confusable types (basin country, $\kappa{=}0.97$) show 74.6\% DR.}
32	\label{tab:kappa-case-study}
33	\end{table}
34	
35	\paragraph{Analysis.}
36	The case study confirms that violation susceptibility is driven by the interaction of constraint tightness and entity type confusability, not tightness alone.
37	Among DocRED relations with $\kappa \geq 0.81$, those involving semantically unambiguous type pairs (\textsc{per}$\to$\textsc{loc} for kinship/geographic relations) achieve DR${=}$0\%, while those requiring the model to distinguish frequently confused types (\textsc{loc} vs.\ \textsc{org}, \textsc{per} vs.\ \textsc{misc}) show DR${>}$50\%.
38	On SciERC, the highest-DR relation (\textsc{Compare}, 42.4\%) has only moderate $\kappa$ (0.53) but high type confusability across scientific categories.
39	This two-factor pattern motivates constrained decoding: the largest gains come from high-$\kappa$, confusable-type relations where the model's type uncertainty is channeled into valid pairs.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec75b15a-b8ea-43ed-82ed-c747d5565f71",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "71f9b8b3-4d7f-4f66-9d01-18cb98293945",
  "sourceToolAssistantUUID": "ec75b15a-b8ea-43ed-82ed-c747d5565f71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-24T05:02:01.304Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A6PAbohRkd6zhriXSQiHsc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71f9b8b3-4d7f-4f66-9d01-18cb98293945",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3c06668-fd07-4184-9798-1642f9d4eddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 44 · 2026-05-24T05:02:01.310Z_

<details><summary>↩ Tool result · `toolu_01A6PAbohRkd6zhriXSQiHsc`</summary>

```text
1	% Appendix: Schema Ambiguity Analysis
2	% High-kappa relations and their impact on DR enforcement
3	
4	\paragraph{Schema ambiguity analysis.}
5	\label{app:kappa-analysis}
6	
7	We define the \emph{schema ambiguity} of a relation $r$ as the average fraction of relations that share each of $r$'s valid type pairs:
8	\begin{equation}
9	\alpha_r = \frac{1}{|\mathcal{P}_r|} \sum_{(h,t) \in \mathcal{P}_r} \frac{|\{r' \in \mathcal{R} : (h,t) \in \mathcal{P}_{r'}\}|}{|\mathcal{R}|}
10	\label{eq:schema-ambiguity}
11	\end{equation}
12	where $\mathcal{P}_r$ is the set of valid entity type pairs for relation $r$ and $\mathcal{R}$ is the full relation set.
13	High $\alpha_r$ indicates that $r$'s valid type pairs are shared by many other relations, limiting the discriminative power of type constraints for that relation.
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Schema ambiguity $\alpha$ for all SciERC relations and the 12 DocRED relations with $\alpha \geq 0.36$. \textbf{Gold \%}: fraction of all gold triples belonging to this relation. All SciERC relations exceed the threshold due to the small schema (7 relations, 6 entity types); in DocRED, only 12 of 96 relations qualify, covering 3.8\% of gold triples.}
19	\label{tab:high-kappa-rels}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{@{}llrrrr@{}}
22	\toprule
23	\textbf{Dataset} & \textbf{Relation} & $\alpha$ & \textbf{$|\mathcal{P}_r|$} & \textbf{Gold} & \textbf{Gold \%} \\
24	\midrule
25	\multicolumn{6}{@{}l}{\textit{SciERC (all 7 relations exceed $\alpha \geq 0.36$)}} \\
26	SciERC & Hyponym-of    & 0.83 & 21 &  298 &  9.3 \\
27	SciERC & Part-of       & 0.83 & 21 &  179 &  5.6 \\
28	SciERC & Compare       & 0.82 & 17 &  166 &  5.2 \\
29	SciERC & Conjunction   & 0.77 & 25 &  400 & 12.4 \\
30	SciERC & Feature-of    & 0.76 & 26 &  173 &  5.4 \\
31	SciERC & Evaluate-for  & 0.71 & 23 &  313 &  9.7 \\
32	SciERC & Used-for      & 0.67 & 35 & 1{,}690 & 52.5 \\
33	\midrule
34	\multicolumn{6}{@{}l}{\textit{DocRED (12 of 96 relations with $\alpha \geq 0.36$; 3.8\% of gold)}} \\
35	DocRED & sister city (P190)          & 0.42 &  1 &    4 & 0.01 \\
36	DocRED & basin country (P205)        & 0.42 &  1 &   85 & 0.22 \\
37	DocRED & mouth of watercourse (P403) & 0.42 &  1 &   95 & 0.25 \\
38	DocRED & separated from (P807)       & 0.41 &  2 &    2 & 0.01 \\
39	DocRED & replaces (P1365)            & 0.39 &  4 &   18 & 0.05 \\
40	DocRED & capital of (P1376)          & 0.37 &  3 &   76 & 0.20 \\
41	DocRED & place of birth (P19)        & 0.37 &  3 &  511 & 1.34 \\
42	DocRED & operator (P137)             & 0.36 &  7 &   95 & 0.25 \\
43	DocRED & military branch (P241)      & 0.36 &  5 &  108 & 0.28 \\
44	DocRED & production company (P272)   & 0.36 &  5 &   82 & 0.21 \\
45	DocRED & place of death (P20)        & 0.36 &  4 &  203 & 0.53 \\
46	DocRED & location (P276)             & 0.36 &  5 &  172 & 0.45 \\
47	\bottomrule
48	\end{tabular}}
49	\end{table}
50	
51	\begin{table}[h]
52	\centering
53	\small
54	\caption{DR violation rates partitioned by schema ambiguity. High-$\alpha$ relations ($\alpha \geq 0.36$) start with substantially higher unconstrained DR on DocRED, and retain elevated residual DR under S1 for Qwen but not for Llama.}
55	\label{tab:dr-by-ambiguity}
56	\begin{tabular}{@{}llrrrr@{}}
57	\toprule
58	& & \multicolumn{2}{c}{\textbf{Unconstrained}} & \multicolumn{2}{c}{\textbf{S1 (Constrained)}} \\
59	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
60	\textbf{Model} & \textbf{Partition} & DR\% & $n$ & DR\% & $n$ \\
61	\midrule
62	\multirow{2}{*}{Llama-3.1-8B}
63	 & High-$\alpha$ (12 rels) & 43.8 &   861 &  3.2 & 1{,}043 \\
64	 & Low-$\alpha$ (84 rels)  & 29.9 & 12{,}809 &  2.5 & 15{,}325 \\
65	\midrule
66	\multirow{2}{*}{Qwen3-8B}
67	 & High-$\alpha$ (12 rels) & 31.9 &   718 & 20.0 & 1{,}119 \\
68	 & Low-$\alpha$ (84 rels)  & 21.2 & 10{,}898 &  9.5 & 16{,}217 \\
69	\bottomrule
70	\end{tabular}
71	\end{table}
72	
73	Table~\ref{tab:high-kappa-rels} reveals a structural asymmetry between datasets.
74	In SciERC, all seven relations have $\alpha \geq 0.67$: with only 7 relations over $6^2 = 36$ entity type pair slots, extensive overlap is inevitable.
75	For example, the pair (Method, Method) is valid for all 7 relations ($\alpha = 1.0$).
76	In DocRED, 96 relations spread across the same 36 type pair slots yield much lower per-relation ambiguity; only 12 relations exceed $\alpha \geq 0.36$, and these collectively cover just 3.8\% of gold triples.
77	
78	Table~\ref{tab:dr-by-ambiguity} shows the DR impact stratified by ambiguity.
79	On DocRED, high-$\alpha$ relations exhibit substantially higher unconstrained DR (43.8\% for Llama vs.\ 29.9\% for low-$\alpha$), reflecting the inherent difficulty of relations whose valid type pairs are shared by dozens of other relations---the model frequently assigns a type combination that, while valid for \emph{some} relation, violates the constraints of the target relation.
80	Under S1 constraints, Llama reduces both groups to near-parity (3.2\% vs.\ 2.5\%), whereas Qwen retains a 2$\times$ gap (20.0\% vs.\ 9.5\%), indicating that constraint effectiveness on high-ambiguity relations depends on the model's baseline type accuracy.
81	Excluding the 12 high-$\alpha$ relations from the DocRED evaluation changes the overall S1 DR only marginally---from 2.55\% to 2.51\% for Llama and from 10.21\% to 9.53\% for Qwen---confirming that their small gold footprint (3.8\%) limits their aggregate impact despite elevated per-relation rates.
82	On SciERC, where all relations have high $\alpha$, the exclusion analysis is vacuous; yet OntoCoDec still reduces DR from 15.4\% to 0.9\% (Qwen) and from 13.3\% to 0.08\% (Llama), demonstrating that high schema ambiguity does not preclude effective constraint enforcement.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3c06668-fd07-4184-9798-1642f9d4eddd",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "5deb9556-2777-493f-9a23-5dd2c05747c3",
  "sourceToolAssistantUUID": "b3c06668-fd07-4184-9798-1642f9d4eddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-24T05:02:01.767Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KeR7m7sQWKj2KfrBuguhrJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_order_invariance.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5deb9556-2777-493f-9a23-5dd2c05747c3",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLojo51u84Jq1ejJJouR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e17716dd-e68a-4559-b58d-770094d789aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkdSXvnmzMpfEmFzj1AneM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5970,
      "cache_read_input_tokens": 30002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5970,
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

### Tool result

_source line 46 · 2026-05-24T05:02:01.772Z_

<details><summary>↩ Tool result · `toolu_01KeR7m7sQWKj2KfrBuguhrJ`</summary>

```text
1	% Appendix: Order Invariance of Compiled Constraints
2	
3	\paragraph{Order invariance.}
4	\label{app:order-invariance}
5	To verify that OntoCoDec's outputs are independent of schema enumeration order, we randomly shuffle the entity and relation type lists in the compiled constraint file (\texttt{ontology\_constraints.json}) and re-run greedy S1 decoding on all 551 SciERC documents.
6	The raw model outputs and parsed triples are byte-identical to the canonical-order run across all documents.
7	This holds because the grammar layer accepts the same token set at each type-bearing position regardless of the order in which types are listed in the schema, and greedy decoding is deterministic given identical logit masks.
8	The result confirms that OntoCoDec introduces no spurious order dependence from schema compilation.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e17716dd-e68a-4559-b58d-770094d789aa",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "bf43c29d-6fc3-468d-b1c7-e221d586fe16",
  "sourceToolAssistantUUID": "e17716dd-e68a-4559-b58d-770094d789aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-24T05:02:04.906Z_

Now let me read the remaining appendix files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf43c29d-6fc3-468d-b1c7-e221d586fe16",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLokwK9BF42DaaDBYQ6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86cecb14-41b3-4d4d-8c91-65a0170c0092",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpzQByuGcQE6umonMPASNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86329,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 86329,
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

### Tool call

_source line 48 · 2026-05-24T05:02:06.992Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H1kM1c2CDwHdXb1Jz98BaW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86cecb14-41b3-4d4d-8c91-65a0170c0092",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLokwK9BF42DaaDBYQ6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eed765aa-ddb2-475e-8eb4-56a9fe3dc719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpzQByuGcQE6umonMPASNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86329,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 86329,
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

### Tool result

_source line 49 · 2026-05-24T05:02:07.018Z_

<details><summary>↩ Tool result · `toolu_01H1kM1c2CDwHdXb1Jz98BaW`</summary>

```text
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
34	    \item $uv^i xy^i z \in L$ for all $i \geq 0$.
35	\end{enumerate}
36	
37	Choose $w = w_n$ with $n > p$.
38	The entity list portion $\tau_B^{n-1}\, \tau_A$ has length $n > p$, so the pumpable region $vxy$ (with $|vxy| \leq p$) must lie entirely within the entity list (it cannot span from the entity list to the relation reference, which is separated by $n - p > 0$ entity tokens from the start).
39	
40	\textbf{Case 1:} $v$ or $y$ contains entity tokens from the $\tau_B^{n-1}$ prefix.
41	Pumping up ($i = 2$): $uv^2 xy^2 z$ inserts additional $\tau_B$ entities, increasing $n$ to some $n' > n$.
42	But the relation reference still points to entity $e_n$ (at the original position), which is now at a different position in the longer entity list.
43	The entity at position $n$ in the pumped string is $\tau_B$ (since we inserted $\tau_B$ tokens before position $n$, shifting $\tau_A$ to position $n' > n$).
44	Thus $\tau^h = \tau_A \neq \tau_B = \tau_{a_n'}$, where $n'$ is the new position of entity $e_n$.
45	More precisely: the relation references a fixed entity name $e_k$, but pumping changes the entity-type binding at that name's position.
46	Since the pumped string assigns $\tau_B$ at position $k$ (which originally had $\tau_A$), the type-validity constraint $\tau^h = \tau_{a_k} \in \operatorname{dom}(r)$ is violated.
47	Hence $uv^2 xy^2 z \notin L$, contradicting condition (iii).
48	
49	\textbf{Case 2:} $v$ or $y$ contains the $\tau_A$ token at position $n$.
50	Pumping down ($i = 0$): $uxz$ removes the only $\tau_A$ entity.
51	The relation's head entity reference now points to a position that either does not exist or has type $\tau_B$.
52	In either case, $\tau^h = \tau_A \neq \tau_B$, violating type validity.
53	Hence $uxz \notin L$, contradicting condition (iii).
54	
55	In both cases, the pumping lemma is violated, so $L$ is not context-free.
56	The key insight is that type-validity requires a \emph{binding} between an entity's type (assigned at an earlier position) and the relation's type field (at a later position), with the binding target determined by the entity name.
57	Pumping disrupts this binding by changing which entity occupies a given position, while the relation reference remains fixed---a cross-position dependency that pushdown automata cannot track with their LIFO stack discipline.
58	
59	OntoCoDec's semantic layer addresses this with a runtime entity registry $\mathcal{D}$ (a finite map), operating as a deterministic stateful transducer that provides random-access type lookups, beyond the expressive power of context-free grammars.
60	\end{proof}
61	
62	\paragraph{Finite entity sets.}
63	For a finite entity set $\mathcal{E}$ with canonical identifiers, the valid language $L_{\text{valid}} = \bigcap_i L_i$ is theoretically regular (a finite intersection of regular languages).
64	However, the corresponding DFA requires $O(|\mathcal{T}|^{|\mathcal{E}|})$ states---for SciERC with 6 entity types and typical documents containing 20+ entities, this exceeds $10^{15}$ states, rendering explicit construction impractical.
65	Moreover, real IE operates over open-vocabulary text spans rather than closed identifier sets, making the general (non-regular) formulation the appropriate model.
66	Proposition~1 motivates the runtime state-tracking architecture for this general case.
67	
68	\paragraph{Position indexing vs.\ name referencing.}
69	The proof above uses position-based entity indexing ($e_k$ at position $k$) for expository clarity.
70	In OntoCoDec's actual JSON output, relation triples reference entities by name strings rather than positional indices.
71	Specifically, Case~1 of the pumping argument (position shift) does not directly apply under name-based referencing, since pumping does not change which entity a name refers to. However, the non-context-free conclusion still holds via a stronger argument:
72	validating type consistency requires a name$\to$type lookup over dynamically generated bindings, which is a random-access map operation.
73	A PDA's LIFO stack cannot perform random-access retrieval by key (it can only inspect the top element), so the non-context-free result holds regardless of whether entities are referenced by position or by name.
74	Name-based referencing strictly subsumes position-based indexing: any position-based constraint can be expressed via names (assign names $e_1, \ldots, e_n$ in order), but name-based constraints additionally permit cross-field coreference (the same entity name appearing in multiple triples must carry the same type), which position indexing cannot express.
75	Thus, the position-based formulation is a simplification that makes the pumping argument more transparent without weakening the conclusion.
76	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed765aa-ddb2-475e-8eb4-56a9fe3dc719",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "4108fd8f-35b9-425b-8067-9da33bfc0b66",
  "sourceToolAssistantUUID": "eed765aa-ddb2-475e-8eb4-56a9fe3dc719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T05:02:07.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MU8m1MUBzTSFVcbj3r48fg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4108fd8f-35b9-425b-8067-9da33bfc0b66",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLokwK9BF42DaaDBYQ6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d3f3257-a3eb-4e2b-83d2-a2b3d7514e1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpzQByuGcQE6umonMPASNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86329,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 86329,
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

### Tool result

_source line 51 · 2026-05-24T05:02:07.972Z_

<details><summary>↩ Tool result · `toolu_01MU8m1MUBzTSFVcbj3r48fg`</summary>

```text
1	% Appendix: WikiEvents Event Extraction Pilot (moved from §5 main text)
2	% exp_ids: ee_qwen_wikievents_unconstrained, ee_llama_wikievents_unconstrained,
3	%          ee_mistral_wikievents_unconstrained, ee_qwen_wikievents_constrained,
4	%          ee_llama_wikievents_constrained, ee_mistral_wikievents_constrained_v2
5	% v3 final data confirmed by Director 2026-05-18.
6	
7	\section{WikiEvents Event Extraction Pilot}
8	\label{app:wikievents-pilot}
9	
10	We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
11	Violations extend to EV (event vocabulary), RoV (role vocabulary), and AC (argument constraint, analogous to DR).
12	
13	% ──────────────────────────────────────────
14	%  Table: WikiEvents three-model comparison (v3 final)
15	%  exp_ids: ee_{qwen,llama,mistral}_wikievents_{unconstrained,grammar_only,constrained_v3}
16	% ──────────────────────────────────────────
17	\begin{table}[h]
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
34	  & S1    & \textbf{0} & \textbf{0} & 2.1 & 21.1 & 13.4 & 14.1 \\
35	\midrule
36	\multirow{3}{*}{\shortstack[l]{Llama\\3.1-8B}}
37	  & Unconstr.\ & 10.5 & 88.8 & 0.1 & 0 & 5.7 & 0 \\
38	  & Grammar    & \textbf{0} & 77.0 & 8.8 & --- & --- & --- \\
39	  & S1    & \textbf{0} & \textbf{0} & 3.8 & 17.2 & 7.5 & 17.6 \\
40	\midrule
41	\multirow{3}{*}{\shortstack[l]{Mistral\\7B}}
42	  & Unconstr.\ & 37.3 & 63.9 & 0 & 0 & 2.4 & 0 \\
43	  & Grammar    & \textbf{0} & 64.0 & 13.8 & --- & --- & --- \\
44	  & S1    & \textbf{0} & \textbf{0} & 1.3 & 14.9 & 3.9 & 11.7 \\
45	\bottomrule
46	\end{tabular}}%
47	\caption{WikiEvents EE results (zero-shot, $n{=}246$ documents).
48	Violation rates over parsed documents.
49	\textemdash{} indicates not applicable (grammar-only has no semantic-layer metrics).
50	F1 (\%). $n{=}20$ test documents for fine-tuning; MDE${\approx}\pm$5.0\,pp; results are directional only.}
51	\label{tab:wikievents}
52	\end{table}
53	
54	\paragraph{Results.}
55	Unconstrained EE produces extreme vocabulary violations (EV+RoV $>$85\%; Table~\ref{tab:wikievents}), with entity F1\,=\,0 because the parser cannot process off-schema output.
56	S1 eliminates EV and RoV across all models, validating tokenizer-agnostic design across byte-level BPE and SentencePiece.
57	Grammar-only eliminates EV but leaves RoV at 64--77\% and surfaces latent AC (8--14\%), consistent with DocRED's pattern (\S\ref{sec:docred-results}).
58	Residual AC (1.3--3.8\%) traces to semantically similar types; CF rises to 15--21\% due to EE's multi-argument entity reuse.
59	Unlike RE, EE shows measurable F1 gains: entity F1 0\%\,$\to$\,12--18\%, trigger F1 $+$1.5--1.8\,pp.
60	
61	% exp_ids: p1_ee_ft_qwen_wikievents_r5, p1_ee_ft_llama_wikievents_r5
62	\paragraph{Composability with fine-tuning (preliminary, $n{=}20$).}
63	On the full official test split (20 documents; 194/20/20~\cite{li2021document}), LoRA + S1 eliminates RoV (Qwen 38.31\%\,$\to$\,0\%, Llama 8.8\%\,$\to$\,0\%) and reduces AC to $\leq$0.8\%, with argument F1 within $\pm$1.1\,pp; trigger F1 shifts ($-$5.4/$-$0.6\,pp) have wide CIs consistent with n${=}$20.
64	CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences (power analysis in Appendix~\ref{app:power-analysis-full}).
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d3f3257-a3eb-4e2b-83d2-a2b3d7514e1a",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "80f20a11-d0b0-47bf-84b4-b875838938ca",
  "sourceToolAssistantUUID": "3d3f3257-a3eb-4e2b-83d2-a2b3d7514e1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T05:02:08.271Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V2ziKhGgKazA5m248PnhNA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80f20a11-d0b0-47bf-84b4-b875838938ca",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLokwK9BF42DaaDBYQ6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0459b83-e344-4396-bb56-6d4e2593bc31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpzQByuGcQE6umonMPASNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86329,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 86329,
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

### Tool result

_source line 53 · 2026-05-24T05:02:08.300Z_

<details><summary>↩ Tool result · `toolu_01V2ziKhGgKazA5m248PnhNA`</summary>

```text
1	% Appendix: Zero-Shot Cross-Model and Cross-Dataset Details
2	% Moved from main text §5.2--§5.3 per reviewer guidance to focus main text on fine-tuned results.
3	
4	\section{Zero-Shot Cross-Model Validation}
5	\label{app:cross-model-zs}
6	
7	\begin{table}[h]
8	\centering
9	\small
10	\setlength{\tabcolsep}{3.4pt}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}ll rrrr r@{}}
13	\toprule
14	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
15	& \textbf{R-F1} \\
16	\cmidrule(lr){3-6} \cmidrule(l){7-7}
17	\textbf{Dataset} & \textbf{Model}
18	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
19	  & $\uparrow$ \\
20	\midrule
21	\multirow{6}{*}{SciERC}
22	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
23	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
24	  \cmidrule(l){2-7}
25	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
26	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
27	  \cmidrule(l){2-7}
28	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
29	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
30	\midrule
31	\multirow{6}{*}{DocRED}
32	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
33	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
34	  \cmidrule(l){2-7}
35	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
36	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
37	  \cmidrule(l){2-7}
38	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
39	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
40	\bottomrule
41	\end{tabular}}%
42	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
43	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
44	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
45	F1 $\times$100.}
46	\label{tab:cross-model}
47	\end{table}
48	
49	\paragraph{Cross-model results.}
50	RV and ET reach $\leq$0.03\% for all models on both datasets.
51	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
52	CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%); fine-tuning resolves both (\S\ref{sec:composability}).
53	Post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates (Appendix~\ref{app:posthoc-extended}).
54	
55	\paragraph{Cross-dataset validation on DocRED.}
56	\label{sec:docred-results}
57	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
58	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.49\,pp ($p < 0.001$).
59	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
60	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) via \textit{latent violation surfacing}: grammar forces OOV$\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the scale-dependent layer interaction.
61	Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0459b83-e344-4396-bb56-6d4e2593bc31",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "88b46ac9-7fca-45d3-9404-967eb47a5b66",
  "sourceToolAssistantUUID": "a0459b83-e344-4396-bb56-6d4e2593bc31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T05:02:09.143Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J5Kn2DV8UA9MfZ7wY6dN5i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b46ac9-7fca-45d3-9404-967eb47a5b66",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLokwK9BF42DaaDBYQ6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffb5e9f0-fc02-4d16-b4db-5e4e0967080a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpzQByuGcQE6umonMPASNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86329,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 86329,
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

### Tool result

_source line 55 · 2026-05-24T05:02:09.149Z_

<details><summary>↩ Tool result · `toolu_01J5Kn2DV8UA9MfZ7wY6dN5i`</summary>

```text
1	% Appendix: Quantization Robustness (SF2 response)
2	% exp_ids: sf2_qwen_int4_scierc_s1, sf2_llama_int4_scierc_s1,
3	%          sf2_qwen_int4_docred_s1, sf2_llama_int4_docred_s1,
4	%          d065_qwen_greedy_4096_r2, d066_sweep_llama_docred_beam1_s1
5	
6	\section{Quantization Robustness}
7	\label{app:quantization}
8	
9	\begin{table}[h]
10	\centering
11	\small
12	\setlength{\tabcolsep}{3.2pt}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}l rrr rrr@{}}
15	\toprule
16	& \multicolumn{3}{c}{\textbf{Qwen3-8B}} & \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} \\
17	\cmidrule(lr){2-4} \cmidrule(l){5-7}
18	& FP16 & INT4 & $\Delta$ & FP16 & INT4 & $\Delta$ \\
19	\midrule
20	\multicolumn{7}{@{}l}{\textit{SciERC (551 docs)}} \\[2pt]
21	DR\,(\%)\,$\downarrow$  & 0     & 0     & 0      & 0.09  & 0     & $-$0.09 \\
22	R-F1\,$\uparrow$ & 43.77 & 41.71 & $-$2.06 & 45.47 & 43.98 & $-$1.49 \\
23	E-F1\,$\uparrow$ & 67.05 & 67.05 & 0.00   & 67.76 & 67.54 & $-$0.22 \\
24	\addlinespace[4pt]
25	\multicolumn{7}{@{}l}{\textit{DocRED (200 docs)}} \\[2pt]
26	DR\,(\%)\,$\downarrow$  & 0     & 0     & 0      & 0     & 0     & 0 \\
27	R-F1\,$\uparrow$ & 40.79\textsuperscript{\dag} & 40.07 & $-$0.72 & 47.35 & 48.04 & $+$0.69 \\
28	E-F1\,$\uparrow$ & 81.87\textsuperscript{\dag} & 74.84 & $-$7.03\textsuperscript{\ddag} & 85.43 & 84.18 & $-$1.25 \\
29	PF\,(\%) & 8.5\textsuperscript{\dag}  & 18.5  & $+$10.0\textsuperscript{\ddag} & 2.0   & 2.5   & $+$0.5 \\
30	\bottomrule
31	\end{tabular}}
32	\caption{FP16 vs.\ INT4 (AWQ) quantization under LoRA + S1 on SciERC and DocRED. F1 $\times$ 100; PF = parse-failure rate.
33	\textsuperscript{\dag}Qwen DocRED FP16 evaluated on 998 docs (all other configurations use matched subsets).
34	\textsuperscript{\ddag}E-F1 drop primarily attributable to increased parse failures under INT4 quantization on long documents rather than constraint interference (DR remains 0\%).}
35	\label{tab:quantization}
36	\end{table}
37	
38	INT4 (AWQ) quantization preserves constraint enforcement across both datasets: DR remains at 0\% for all four model--dataset configurations under INT4, with the sole FP16 violation (Llama SciERC, 0.09\%) disappearing after quantization.
39	R-F1 changes range from $-$2.06 to $+$0.69\,pp, consistent with expected quantization quality costs independent of the constraint layers.
40	On DocRED, Qwen INT4 exhibits elevated parse failures (18.5\% vs.\ 8.5\% FP16) due to timeout on long documents under quantized inference; the resulting E-F1 gap ($-$7.03\,pp) reflects generation-length degradation rather than constraint-layer interference, as DR remains 0\%.
41	These results provide indirect evidence that the 70B AWQ INT4 results (\S\ref{sec:70b-results}) are not confounded by quantization artifacts in the constraint enforcement mechanism.
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffb5e9f0-fc02-4d16-b4db-5e4e0967080a",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "bf97799b-1bdc-40b2-b653-2542a97b771a",
  "sourceToolAssistantUUID": "ffb5e9f0-fc02-4d16-b4db-5e4e0967080a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-24T05:02:10.234Z_

<details open><summary>🔧 Tool call — Read · `toolu_011E31ps2B6uGHoMBaizk4U1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf97799b-1bdc-40b2-b653-2542a97b771a",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLokwK9BF42DaaDBYQ6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "342617ac-58e8-4ba2-b61a-8ecfbdc90455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpzQByuGcQE6umonMPASNP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86329,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 86329,
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

### Tool result

_source line 57 · 2026-05-24T05:02:10.239Z_

<details><summary>↩ Tool result · `toolu_011E31ps2B6uGHoMBaizk4U1`</summary>

```text
1	% Appendix: GoLLIE Comparison (D4 response)
2	% exp_ids: gollie_7b_scierc_zs_100, ontcodec_qwen_ft_s1_scierc_100, ontcodec_llama_ft_s1_scierc_100
3	
4	\section{GoLLIE Comparison}
5	\label{app:gollie-comparison}
6	
7	GoLLIE~\cite{sainz2024gollie} and OntoCoDec represent complementary paradigms for schema compliance in IE:
8	
9	\begin{itemize}[nosep,leftmargin=*]
10	\item \emph{Training-time internalization} (GoLLIE, KnowCoder): Schema knowledge is encoded into model parameters via annotation-guideline-aware training. This achieves compliance through learned generation patterns but cannot guarantee zero violations at inference time, and requires schema-specific retraining when ontologies evolve.
11	\item \emph{Runtime constraint enforcement} (OntoCoDec): Schema constraints are compiled into decoding-time masks applied to any generative model. This provides formal enforcement without schema-specific training, but operates per-triple and cannot resolve cross-triple type consistency (CF) within a single pass.
12	\end{itemize}
13	
14	The two approaches are orthogonal: OntoCoDec can be composed with GoLLIE or similar training-based systems to provide runtime enforcement guarantees atop learned schema compliance.
15	Direct numerical comparison is methodologically constrained by incompatible evaluation settings (code-style schema encoding vs.\ natural language prompting, different model families and sizes); a controlled comparison would require running both approaches on the same model with matched prompting, which we leave to future work.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "342617ac-58e8-4ba2-b61a-8ecfbdc90455",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "b24969dd-845d-4ad0-bd32-de5c2411701d",
  "sourceToolAssistantUUID": "342617ac-58e8-4ba2-b61a-8ecfbdc90455",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T05:02:10.451Z_

<details open><summary>🔧 Tool call — Read · `toolu_0177VWtN4A5uRrpJCsqRm3LS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_ai_assistants.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b24969dd-845d-4ad0-bd32-de5c2411701d",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLokwK9BF42DaaDBYQ6Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30d08044-1df7-4f24-be18-5a7179c80c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpzQByuGcQE6umonMPASNP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86329,
      "cache_read_input_tokens": 8266,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 86329
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 515,
          "cache_read_input_tokens": 8266,
          "cache_creation_input_tokens": 86329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 86329,
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

_source line 59 · 2026-05-24T05:02:10.465Z_

<details><summary>↩ Tool result · `toolu_0177VWtN4A5uRrpJCsqRm3LS`</summary>

```text
1	\section{Use of AI Assistants}
2	\label{app:ai-assistants}
3	
4	We used Claude (Anthropic) as an AI coding and writing assistant
5	throughout this work. Specifically:
6	\begin{itemize}
7	    \item \textbf{Code:} drafting experiment scripts, data-processing
8	    pipelines, and analysis utilities; debugging and refactoring.
9	    \item \textbf{Writing:} drafting and revising paper sections,
10	    polishing prose, and reformatting \LaTeX{}.
11	    \item \textbf{Literature:} summarizing related papers to inform
12	    the related-work section.
13	\end{itemize}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30d08044-1df7-4f24-be18-5a7179c80c82",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "4c215495-ec1d-43bf-8c84-32a1cc513241",
  "sourceToolAssistantUUID": "30d08044-1df7-4f24-be18-5a7179c80c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-24T05:02:16.300Z_

Now I have all the appendix labels. Let me search for all `\ref{app:` patterns across all .tex files to find cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c215495-ec1d-43bf-8c84-32a1cc513241",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLomaWH4c5Abd5FdRMLr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06f29f17-b3f8-4e73-805d-c05084c579ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rg3J9HZUfCssC98gNs9cBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8150,
      "cache_read_input_tokens": 94595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8150,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 61 · 2026-05-24T05:02:19.662Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NLjp5bmT68v5uNvo8tYptJ`</summary>

```json
{
  "pattern": "\\\\ref\\{app:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06f29f17-b3f8-4e73-805d-c05084c579ad",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLomaWH4c5Abd5FdRMLr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b25813f2-b33a-43df-88a8-50826f8c8075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rg3J9HZUfCssC98gNs9cBD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8150,
      "cache_read_input_tokens": 94595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8150,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 62 · 2026-05-24T05:02:19.695Z_

<details><summary>↩ Tool result · `toolu_01NLjp5bmT68v5uNvo8tYptJ`</summary>

```text
&lt;persisted-output>
Output too large (20.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-agent-f7c2f8cc/d74ed321-94ae-476c-899f-c11688aa3239/tool-results/toolu_01NLjp5bmT68v5uNvo8tYptJ.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:78:The controlled comparison on SciERC---where both greedy and beam achieve 0\% parse failure---isolates the pure beam quality gain at $+$0.28\,pp, consistent with the 8B pattern (Appendix~\ref{app:beam-search}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:Post-hoc filtering discards up to 74\% of predictions including true positives (Appendix~\ref{app:cross-model-zs}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.4\% fine-tuned); zero-shot DR drops 76--99\% on SciERC and 42--90\% on DocRED, with total violations (DR+CF) decreasing 30--51\% (Appendix~\ref{app:cross-model-zs}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:71:CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impact is model-dependent (S1 introduces CF for calibrated models but reduces it for poorly-calibrated ones).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:74:Residual DR under fine-tuning (36 violations total) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors (28\%); schema gaps arise from training-data-derived constraints that may not cover all valid type pairs (Appendix~\ref{app:residual-dr-analysis}).
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b25813f2-b33a-43df-88a8-50826f8c8075",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "d8374237-b9c9-46ee-8788-9cbf81d395d7",
  "sourceToolAssistantUUID": "b25813f2-b33a-43df-88a8-50826f8c8075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-24T05:02:20.285Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01W1SQmxjxyAcgku3q3XEN8q`</summary>

```json
{
  "pattern": "\\\\label\\{app:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8374237-b9c9-46ee-8788-9cbf81d395d7",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLomaWH4c5Abd5FdRMLr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5572f385-a697-4a44-9f11-bac71862e6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rg3J9HZUfCssC98gNs9cBD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8150,
      "cache_read_input_tokens": 94595,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8150
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 345,
          "cache_read_input_tokens": 94595,
          "cache_creation_input_tokens": 8150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8150,
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

_source line 64 · 2026-05-24T05:02:20.306Z_

<details><summary>↩ Tool result · `toolu_01W1SQmxjxyAcgku3q3XEN8q`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex:1:\section{Sampling Robustness}\label{app:sampling}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:7:\label{app:70b-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:44:\label{app:70b-docred}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:83:\label{app:70b-docred-zs}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_pumping_lemma.tex:5:\label{app:pumping-lemma}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex:2:\label{app:full-ft}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:2:\label{app:doc-length}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:2:\label{app:reproducibility}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:21:\label{app:greedy-determinism}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:56:\label{app:power-analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:5:\label{app:prompts}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_related_work.tex:2:\label{app:related_work}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex:6:\label{app:power-analysis-full}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex:7:\label{app:quantization}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex:5:\label{app:kappa-analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex:5:\label{app:tcr}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_ai_assistants.tex:2:\label{app:ai-assistants}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex:5:\label{app:kappa-case-study}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex:8:\label{app:wikievents-pilot}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:4:\section{Extended Discussion}\label{app:discussion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:25:\label{app:fallback-coverage}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:45:\label{app:causal-tracing}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:75:\label{app:enabling-confound}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:88:\label{app:cf-dr-tradeoff}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:135:\label{app:dual-factor}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:168:\label{app:bootstrap-effect-sizes}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:236:\label{app:cf-distribution}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:274:\label{app:cascade-analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:311:\label{app:lora-per-relation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:346:\label{app:ft-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:404:\label{app:docred-zs-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:458:\label{app:residual-dr-analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:480:\label{app:posthoc-extended}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:523:\label{app:runtime}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:531:\label{app:ft-latency}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:539:\label{app:fuzzy-matching}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:550:\label{app:per-relation-landscape}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:584:\label{app:wikievents}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:590:\label{app:wikievents-kappa}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:601:\label{app:lucky-violations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:635:\label{app:trie-baseline}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:679:\label{app:gcd-comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex:2:\label{app:downstream-impact}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:2:\label{app:beam-search}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_order_invariance.tex:4:\label{app:order-invariance}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:2:\label{app:prompt-sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:4:\section{Per-Relation Violation Analysis (Llama-3.1-8B)}\label{app:llama-per-relation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex:5:\label{app:cross-model-zs}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex:2:\label{app:scalability}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis_523cc9.tex:6:\label{app:power-analysis-full}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_type_consensus.tex.archived:1:\section{Type Consensus Constraint (Layer 3)}\label{app:type-consensus}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_gollie_comparison.tex:5:\label{app:gollie-comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:4:\label{app:case-studies}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:15:\label{app:case-dr}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:47:\label{app:case-rv-dr}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:79:\label{app:case-scale}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:118:\label{app:case-cf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:145:\label{app:error-analysis}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5572f385-a697-4a44-9f11-bac71862e6cc",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "d3feba29-96d9-453e-b609-db96fac58be3",
  "sourceToolAssistantUUID": "5572f385-a697-4a44-9f11-bac71862e6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-24T05:02:23.244Z_

Let me read the full reference output file to get all references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3feba29-96d9-453e-b609-db96fac58be3",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLonJPBuvVkdkfCpQvGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8a0aabe-f494-4ab8-9aaa-210147de7593",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jN9NgDSMCeBKkbRYiqk4v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4526,
      "cache_read_input_tokens": 102745,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4526,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 66 · 2026-05-24T05:02:27.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_012UiMcA8EXA4YwoHNkc2rpc`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie--claude-sessions-agent-f7c2f8cc/d74ed321-94ae-476c-899f-c11688aa3239/tool-results/toolu_01NLjp5bmT68v5uNvo8tYptJ.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8a0aabe-f494-4ab8-9aaa-210147de7593",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLonJPBuvVkdkfCpQvGV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a9cef00-ed2a-4d90-9771-e4704c9d2fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jN9NgDSMCeBKkbRYiqk4v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4526,
      "cache_read_input_tokens": 102745,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 102745,
          "cache_creation_input_tokens": 4526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4526,
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

_source line 67 · 2026-05-24T05:02:27.365Z_

<details><summary>↩ Tool result · `toolu_012UiMcA8EXA4YwoHNkc2rpc`</summary>

```text
1	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:78:The controlled comparison on SciERC---where both greedy and beam achieve 0\% parse failure---isolates the pure beam quality gain at $+$0.28\,pp, consistent with the 8B pattern (Appendix~\ref{app:beam-search}).
2	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:14:Post-hoc filtering discards up to 74\% of predictions including true positives (Appendix~\ref{app:cross-model-zs}).
3	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section1_introduction_draft.tex:21:DR enforcement converts ontologically invalid violations to individually valid but type-inconsistent ones (CF\,$\leq$\,1.4\% fine-tuned); zero-shot DR drops 76--99\% on SciERC and 42--90\% on DocRED, with total violations (DR+CF) decreasing 30--51\% (Appendix~\ref{app:cross-model-zs}).
4	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:71:CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impact is model-dependent (S1 introduces CF for calibrated models but reduces it for poorly-calibrated ones).
5	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:74:Residual DR under fine-tuning (36 violations total) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors (28\%); schema gaps arise from training-data-derived constraints that may not cover all valid type pairs (Appendix~\ref{app:residual-dr-analysis}).
6	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:77:Post-hoc type consensus re-voting eliminates all CF in our experiments, at the cost of DR regression (up to $+$9.38\,pp on DocRED zero-shot; Appendix~\ref{app:tcr}); integrating consensus into the decoding loop remains future work.
7	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:84:All main experiments use greedy decoding; beam search compatibility is confirmed but comprehensive evaluation across all configurations remains future work (Appendices~\ref{app:sampling},~\ref{app:beam-search}).
8	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:88:Our approach requires access to model logits, excluding API-only models; continuation masking assumes distinguishable token prefixes per type name, which may be challenged by morphologically similar types (e.g., \texttt{Protein} vs.\ \texttt{Protein\_Complex}; Appendix~\ref{app:scalability}).
9	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:89:70B experiments use AWQ INT4 quantization; an 8B ablation confirms enforcement is unaffected (Appendix~\ref{app:quantization}), though a direct 70B FP16 comparison exceeds our hardware capacity.
10	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:90:Evaluation is limited to English-language datasets; the mechanism is language-independent but CJK tokenization fragmentation may increase masking steps (Appendix~\ref{app:scalability}).
11	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:91:While composability is validated with both LoRA and full fine-tuning (Appendix~\ref{app:full-ft}), different PEFT methods may affect logit distributions differently, and further validation across adapter methods is warranted.
12	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex:92:The two-pass strategy (S2) exhibits scale-dependent degradation: at 70B, S2 reduces R-F1 by 8.45\,pp while 8B models show comparable S1/S2 performance, suggesting optimal constraint granularity varies with model capacity (Appendix~\ref{app:70b-ablation}).
13	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:17:Inference timing is reported in Appendix~\ref{app:runtime} (NVIDIA RTX PRO 6000 Blackwell Server Edition GPU, same hardware as training).
14	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:51:Greedy decoding is deterministic (\S\ref{app:greedy-determinism} above).
15	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex:24:\\ Yes. All datasets, models, and libraries are cited in \S2, \S5, and Appendix~\ref{app:reproducibility}.
16	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex:27:\\ Yes. SciERC (Apache 2.0), DocRED (MIT), WikiEvents (publicly released by \citet{li2021document}). Model licenses are noted in Appendix~\ref{app:reproducibility}.
17	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex:36:\\ Yes. Dataset statistics (relation/entity type counts, document counts, constraint tightness) are reported in \S2, \S5, and Appendix~\ref{app:wikievents}.
18	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex:47:\\ Yes. Model sizes (7B--70B) in \S5. GPU infrastructure, LoRA configuration, and runtime overhead in \S\ref{sec:runtime} and Appendix~\ref{app:reproducibility}.
19	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex:50:\\ Yes. LoRA rank, learning rate, training epochs, and batch size are reported in Appendix~\ref{app:reproducibility}. Prompt templates are in Appendix~\ref{app:prompts}.
20	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/checklist.tex:56:\\ Yes. XGrammar (grammar-constrained decoding), vLLM (inference engine), PEFT/LoRA (fine-tuning) are cited with version information in Appendix~\ref{app:reproducibility}.
21	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:59:Post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates (Appendix~\ref{app:posthoc-extended}).
22	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:17:OntoCoDec enforces levels 1--2 (grammar and semantic layers, respectively); level~3 is addressed by beam search or post-hoc resolution (Appendix~\ref{app:tcr}).
23	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:24:Formally, domain/range constraints for unbounded entity sets are not context-free (\textbf{Proposition~1}; proof via pumping argument in Appendix~\ref{app:pumping-lemma}): a PDA cannot retrieve the type of entity $e_k$ without destroying stack entries above it.
24	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex:10:We apply OntoCoDec to event extraction (EE) on WikiEvents~\cite{li2021document,lu2021text2event} (56 event types, 80 roles, 27 entity types, 245 constraints; Appendix~\ref{app:wikievents}) without modification.
25	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex:64:CF remains low (0.77--1.18\%); per-document variance is high (Arg-F1 std/mean ${>}$\,0.5), confirming sufficient power to detect violation elimination but not small F1 differences (power analysis in Appendix~\ref{app:power-analysis-full}).
26	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:577:\caption{Per-relation DR violation rates on SciERC (Qwen3-8B, unconstrained). Rates correlate with constraint tightness $\kappa(r)$. Llama-3.1-8B shows similar per-relation patterns (Appendix~\ref{app:llama-per-relation}).}
27	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:5:The main experiments (\S\ref{sec:experiments}) use greedy decoding; Appendix~\ref{app:sampling} validates nucleus sampling.
28	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:188:Combined with the sampling robustness results (Appendix~\ref{app:sampling}), these findings confirm that OntoCoDec's constraint enforcement is compatible with greedy, sampling, and beam search decoding without modification to the core constraint logic.
29	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:7:We evaluate OntoCoDec in two deployment configurations: greedy S1 (DR\,$\leq$\,0.21\%, $+$10\% latency) and beam S1 (all violations\,$\to$\,0\%, 1.39$\times$ latency); zero-shot evaluation (\S\ref{sec:scierc-results}; Appendix~\ref{app:cross-model-zs}) serves as a diagnostic probe for the fine-tuned setting (R-F1 40--46\%).
30	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:13:Primary model: Qwen3-8B~\cite{qwen2025qwen3}, zero-shot greedy decoding; cross-model validation in Appendix~\ref{app:cross-model-zs}, composability with fine-tuning in \S\ref{sec:composability}.
31	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_violation_landscape.tex:19:Baseline DR: 15.37\% (SciERC), 18.46\% (DocRED); schema-informed prompting reduces DR by 62\% but is per-relation unreliable (Appendix~\ref{app:per-relation-landscape}).
32	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex:22:Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$ captures schema restrictiveness; DR reduction correlates descriptively with schema-mean $\bar{\kappa}$ across our three evaluation schemas ($n{=}3$), though entity type confusability is a significant co-factor (Appendix~\ref{app:kappa-case-study},~\ref{app:tcr}).
33	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex:28:Fallback triggers on 0.5--5.7\% of type-bearing positions (zero-shot), virtually eliminated by fine-tuning ($\leq$\,0.11\%); all residual DR occurs at fallback positions (Appendix~\ref{app:causal-tracing}).
34	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex:33:Shuffling type order produces byte-identical outputs across all 551 SciERC documents, confirming order invariance (Appendix~\ref{app:order-invariance}).
35	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:67:Deterministic (greedy, $T{=}$0); robustness evidence in Table~\ref{tab:cross-model} and Appendices~\ref{app:bootstrap-effect-sizes},~\ref{app:prompt-sensitivity}.}
36	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:77:On DocRED (96 relations, $\bar{\kappa}{=}0.842$), grammar-only \emph{increases} DR via \textit{latent violation surfacing}: forcing OOV$\to$valid relation mapping exposes violations previously masked by vocabulary errors (Appendix~\ref{app:cross-model-zs}).
37	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:79:DR-to-CF conversion represents a severity downgrade: DR is irrecoverable without re-extraction, while CF---individually valid triples with cross-triple inconsistency---is amenable to post-hoc resolution (TCR eliminates all CF in our experiments, with bounded DR regression; Appendix~\ref{app:tcr}).
38	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:88:Fine-tuning alone reduces DR to 0.5--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.21\% with no significant $\Delta$R-F1 (Bonferroni-corrected; 95\% CIs $\subseteq [-0.69, {+}0.25]$\,pp; removed triples are 97.6--100\% false positives; Appendix~\ref{app:downstream-impact}).
39	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:89:Under fine-tuning, grammar becomes a no-op ($\Delta$DR$<$0.2\,pp), making the semantic layer the sole DR defense (41--69\% on SciERC, 2--75\% on DocRED; Appendix~\ref{app:ft-ablation}); three relations with $\kappa \geq 0.36$ retain DR, all eliminated by S1 (Appendix~\ref{app:lora-per-relation}).
40	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:91:CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned), concentrated in \textsc{Generic}$\leftrightarrow$X ambiguity (63.3\% of zero-shot CF; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) eliminates all violation types at 8B (R-F1 43--46; \S\ref{sec:beam-results}).
41	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:98:Under zero-shot greedy S1, CF is the sole residual violation type (DR, RV, ET all eliminated): 248 cross-field violations arise across 167 documents, of which 63.3\% involve \textsc{Generic}$\leftrightarrow$X type ambiguity (Appendix~\ref{app:cf-distribution}), concentrated in \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} (34.7\%) and \textsc{Generic}$\leftrightarrow$\textsc{Material} (12.3\%).
42	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:99:A source breakdown (Appendix~\ref{app:cascade-analysis}) shows 58.1\% originate from hallucinated entities (a model capacity issue), while true cascade errors---where first-seen registration locks an incorrect type---account for only 7.3\%; correct locks are 2.5$\times$ more frequent, confirming first-seen registration as a net-positive mechanism.
43	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:146:Constraint removal affects only 0.24\% of gold triples (Appendix~\ref{app:lucky-violations}); error analysis of 514 false negatives confirms only one (0.2\%) was blocked by constraints, with dominant sources (relation confusion, entity type polysemy) schema-valid and beyond constraint reach (Appendix~\ref{app:error-analysis}).
44	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:147:Across fine-tuned settings, 36 residual DR violations decompose into entity type errors (39\%), schema coverage gaps (33\%), and relation/direction errors (28\%); the irreducible floor is $\sim$3 violations (Appendix~\ref{app:residual-dr-analysis}).
45	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex:53:Post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates (Appendix~\ref{app:posthoc-extended}).
46	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex:61:Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
47	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:4:We provide a detailed survey in Appendix~\ref{app:related_work}; here we position OntoCoDec along three axes.
48	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section6_related_work.tex:13:GoLLIE achieves schema compliance through annotation-guideline-guided generation at training time (reporting 63.6--70.1\% RE F1 on ACE05 in supervised settings; SciERC RE not evaluated); OntoCoDec provides orthogonal runtime enforcement, composable with any generative IE system including GoLLIE itself (Appendix~\ref{app:gollie-comparison}).
49	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_wikievents_draft.tex:6:Zero-shot evaluation on WikiEvents (246 documents, 3 models; Appendix~\ref{app:wikievents-pilot}) confirms constraint applicability to event extraction, with EV and RoV violations eliminated across all models; fine-tuning composability is preliminary ($n{=}20$).
50	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:12:Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
51	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:8:We offer a speculative hypothesis: larger models exhibit improved vocabulary calibration, assigning higher probability to ontology-valid tokens and reducing the semantic layer's dependence on grammar-enforced vocabulary membership (Appendix~\ref{app:causal-tracing}); confirming this causal mechanism requires cross-family verification beyond our current scope.
52	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:10:Grammar-constrained decoding is thus necessary but increasingly insufficient as models improve; constraint enforcement is preserved under INT4 quantization (4$\times$ compression; Appendix~\ref{app:quantization}).
53	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:16:Net effect: total violations (DR+CF) decrease 30--51\% in zero-shot and 26--52\% under fine-tuned greedy S1; beam $k{=}4$ eliminates all. DR is irrecoverable while CF is amenable to post-hoc resolution (TCR; Appendix~\ref{app:tcr}).
54	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:6:Constraint compilation is one-time $<$0.5\,s; scaling benchmarks confirm constant overhead (2--3\%) up to 200 entity types and 1{,}000 relations (Appendix~\ref{app:scalability}).
55	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:11:With LoRA, beam search~\cite{anderson2017guided} eliminates all four violation types at 8B on both SciERC and DocRED; at 70B, beam $k{=}4$ achieves DR${=}$RV${=}$ET${=}$0\% with one residual CF on SciERC (Appendix~\ref{app:beam-search}).
56	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:20:All 70B experiments use Llama-3.1-70B-Instruct under AWQ INT4 quantization; an 8B ablation confirms constraint enforcement is unaffected by quantization (Appendix~\ref{app:quantization}).
57	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:27:Beam ($k{=}4$) reduces DocRED parse failures (12.5\%\,$\to$\,0.5\%, R-F1 $+$4.19\,pp); SciERC controlled comparison isolates pure beam gain at $+$0.28\,pp (Appendix~\ref{app:70b-ablation}).
58	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:32:Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}; vLLM \texttt{guided\_json}~\cite{kwon2023vllm} confirms equivalence on Qwen3-8B (DR${=}$15.26\%; other models use the same backend; Appendix~\ref{app:gcd-comparison}).
59	/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:33:The ${\sim}$15\% residual DR is the gap our semantic layer addresses (94\% total reduction); trie-only constraints without JSON enforcement yield 9--51\% parse failure (Appendix~\ref{app:trie-baseline}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a9cef00-ed2a-4d90-9771-e4704c9d2fb9",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "649d2fb0-901f-4902-9cda-8478d44dcaf0",
  "sourceToolAssistantUUID": "1a9cef00-ed2a-4d90-9771-e4704c9d2fb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-24T05:02:41.829Z_

Now let me also read the main body files I haven't read yet to check for any additional refs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649d2fb0-901f-4902-9cda-8478d44dcaf0",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLonpjKML8zc6NfNUeNL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "569c2e3f-ac66-478f-8b7c-c129d9e7d2e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQGyQbwF9P1gur9yP6oDwK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7222,
      "cache_read_input_tokens": 107271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7222,
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

### Tool call

_source line 69 · 2026-05-24T05:02:43.776Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016y83rM4nbEh5rGoxHVhFaC`</summary>

```json
{
  "pattern": "\\\\ref\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "section*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "569c2e3f-ac66-478f-8b7c-c129d9e7d2e4",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLonpjKML8zc6NfNUeNL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e05afc34-b02a-4093-963b-9752fa398bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQGyQbwF9P1gur9yP6oDwK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7222,
      "cache_read_input_tokens": 107271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7222,
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

### Tool result

_source line 70 · 2026-05-24T05:02:43.791Z_

<details><summary>↩ Tool result · `toolu_016y83rM4nbEh5rGoxHVhFaC`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:11:Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED,
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:10:Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:27:\noindent\textbf{Empirical Observation} (scale-dependent enabling dependency)\textbf{.} The grammar layer alone cannot enforce domain/range constraints (Proposition~1), while the semantic layer alone achieves only 24\% DR reduction at 8B without grammar-enforced vocabulary membership (\S\ref{sec:scierc-results}, Table~\ref{tab:scierc-ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex:32:Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement admits 33--37\% spurious pairs, eliminated by fine-tuning (Table~\ref{tab:composability}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:10:Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:67:Deterministic (greedy, $T{=}$0); robustness evidence in Table~\ref{tab:cross-model} and Appendices~\ref{app:bootstrap-effect-sizes},~\ref{app:prompt-sensitivity}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:76:Table~\ref{tab:scierc-ablation} establishes that DR violations are pervasive (15--18\% across datasets) and that constraint layers interact non-additively: grammar-only achieves 3\% DR reduction on SciERC, semantic-only 24\%, but their composition yields 94\%---the \emph{empirical enabling dependency}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:78:Cross-model validation (3 models $\times$ 2 datasets; Table~\ref{tab:cross-model}) confirms DR drops of 76--99\% on SciERC and 42--90\% on DocRED, with R-F1 improving in 5/6 settings; post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:88:Fine-tuning alone reduces DR to 0.5--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.21\% with no significant $\Delta$R-F1 (Bonferroni-corrected; 95\% CIs $\subseteq [-0.69, {+}0.25]$\,pp; removed triples are 97.6--100\% false positives; Appendix~\ref{app:downstream-impact}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:90:Fallback frequency is model-dependent: Qwen triggers 0 fallbacks under LoRA + S1 on SciERC, while Llama triggers 5{,}882 (Table~\ref{tab:ft-ablation}), reflecting weaker entity typing; despite this, DR reaches 0.09\% on SciERC (0.21\% on DocRED), confirming that even frequent fallback does not compromise enforcement.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:10:Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:8:DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:12:Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:9:Supporting evidence includes the fallback frequency gap: under LoRA + S1, Qwen-8B triggers 0 grammar-first fallbacks on SciERC while Llama-8B triggers 5{,}882 (Table~\ref{tab:ft-ablation}), yet both achieve DR\,$\leq$\,0.21\%, confirming that fallback frequency does not determine enforcement effectiveness.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:12:A beam-width sweep ($k \in \{1,2,4,8\}$) on SciERC reveals $k{=}2$ as Pareto-optimal: R-F1 44.60 (highest), CF 0.11\%, at only 1.18$\times$ greedy S1 latency; $k{=}4$ achieves CF${=}$0\% but lower R-F1 (43.60) at 1.39$\times$ (Table~\ref{tab:beam-sweep}; latencies relative to greedy S1).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:23:A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:32:Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}; vLLM \texttt{guided\_json}~\cite{kwon2023vllm} confirms equivalence on Qwen3-8B (DR${=}$15.26\%; other models use the same backend; Appendix~\ref{app:gcd-comparison}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e05afc34-b02a-4093-963b-9752fa398bba",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "caeea140-cc36-4ced-88d0-792f910b6fa7",
  "sourceToolAssistantUUID": "e05afc34-b02a-4093-963b-9752fa398bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T05:02:44.696Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Kw13mVUKAJY5nMUa7nwNxL`</summary>

```json
{
  "pattern": "\\\\ref\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caeea140-cc36-4ced-88d0-792f910b6fa7",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLonpjKML8zc6NfNUeNL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edfbc1b6-0002-407a-b8e2-e8f5d9494c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQGyQbwF9P1gur9yP6oDwK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7222,
      "cache_read_input_tokens": 107271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7222,
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

### Tool result

_source line 72 · 2026-05-24T05:02:44.706Z_

<details><summary>↩ Tool result · `toolu_01Kw13mVUKAJY5nMUa7nwNxL`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edfbc1b6-0002-407a-b8e2-e8f5d9494c26",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "f0230bf6-a61f-4602-a165-d2d1f468d623",
  "sourceToolAssistantUUID": "edfbc1b6-0002-407a-b8e2-e8f5d9494c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-24T05:02:45.872Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01KFhfbwieEqagVqjEBEuUgq`</summary>

```json
{
  "pattern": "\\\\ref\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "section*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0230bf6-a61f-4602-a165-d2d1f468d623",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLonpjKML8zc6NfNUeNL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0cb253d-2479-47fb-afa1-0a1eb273cea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQGyQbwF9P1gur9yP6oDwK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7222,
      "cache_read_input_tokens": 107271,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 522,
          "cache_read_input_tokens": 107271,
          "cache_creation_input_tokens": 7222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7222,
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

_source line 74 · 2026-05-24T05:02:45.887Z_

<details><summary>↩ Tool result · `toolu_01KFhfbwieEqagVqjEBEuUgq`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0cb253d-2479-47fb-afa1-0a1eb273cea3",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "d11f2e91-4ca8-4697-82c1-d006a9f891c5",
  "sourceToolAssistantUUID": "b0cb253d-2479-47fb-afa1-0a1eb273cea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-24T05:02:49.283Z_

Now let me check which `tab:` and `fig:` refs from main body point to appendix-defined labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d11f2e91-4ca8-4697-82c1-d006a9f891c5",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLopBZj4PZWLNejZbEeB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7a05bce-e528-402a-95de-26ce78e436c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ntc5sLfkKxCjUzogpR6wZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 114493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2775,
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

### Tool call

_source line 76 · 2026-05-24T05:02:51.218Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TFskaAVjD6E1ZaLRf5f4WV`</summary>

```json
{
  "pattern": "\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "appendix_*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a05bce-e528-402a-95de-26ce78e436c9",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLopBZj4PZWLNejZbEeB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d60013d4-07a2-46bd-a697-57fa451ad5cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ntc5sLfkKxCjUzogpR6wZz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 114493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2775,
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

### Tool result

_source line 77 · 2026-05-24T05:02:51.252Z_

<details><summary>↩ Tool result · `toolu_01TFskaAVjD6E1ZaLRf5f4WV`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_sampling_table.tex:6:\label{tab:sampling-robustness}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:31:\label{tab:70b-ft-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:70:\label{tab:70b-docred-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_70b_ablation.tex:105:\label{tab:70b-docred-zs-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_full_ft.tex:21:\label{tab:full-ft}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:10:\label{tab:doc-length-scierc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:32:\label{tab:doc-length-docred}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_doc_length.tex:54:\label{tab:doc-length-reduction}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_reproducibility.tex:35:\label{tab:seed-variance}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompts.tex:51:\label{tab:prompts}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis.tex:26:\label{tab:power-analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_quantization.tex:35:\label{tab:quantization}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex:19:\label{tab:high-kappa-rels}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_high_kappa_analysis.tex:55:\label{tab:dr-by-ambiguity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex:40:\label{tab:tcr-scierc}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_tcr.tex:70:\label{tab:tcr-docred}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_kappa_case_study.tex:32:\label{tab:kappa-case-study}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_wikievents_pilot.tex:51:\label{tab:wikievents}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:64:\label{tab:causal-tracing}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:108:\label{tab:cf-dr-tradeoff}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:200:\label{tab:bootstrap-effect-sizes}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:267:\label{tab:cf-distribution}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:304:\label{tab:cascade-breakdown}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:339:\label{tab:lora-per-relation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:391:\label{tab:ft-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:451:\label{tab:docred-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:513:\label{tab:posthoc-extended}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:559:\label{tab:prompt_comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:628:\label{tab:lucky-violations}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:673:\label{tab:trie-baseline}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:706:\label{tab:gcd-comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:730:\label{tab:vllm-verification}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_downstream_analysis.tex:21:\label{tab:lucky-violations-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:25:\label{tab:beam-search}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:77:\label{tab:beam-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:110:\label{tab:beam-sweep}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:150:\label{tab:beam-docred-998-zs}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:169:\label{tab:beam-docred-lora}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:207:\label{tab:beam-latency}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_prompt_sensitivity.tex:10:\label{tab:prompt-sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_llama_per_relation.tex:15:\label{tab:llama-per-relation-dr}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_zs_crossmodel.tex:46:\label{tab:cross-model}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_scalability.tex:19:\label{tab:scalability}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_power_analysis_523cc9.tex:26:\label{tab:power-analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:25:\label{tab:case1}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:57:\label{tab:case2}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:89:\label{tab:case3}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_case_studies.tex:128:\label{tab:case4}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d60013d4-07a2-46bd-a697-57fa451ad5cd",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "77da73ba-b4d0-44b7-974e-a811d862be7b",
  "sourceToolAssistantUUID": "d60013d4-07a2-46bd-a697-57fa451ad5cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-24T05:02:52.385Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01B4TaQiNmnh3xaL5DKv6iKA`</summary>

```json
{
  "pattern": "\\\\label\\{fig:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "appendix_*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77da73ba-b4d0-44b7-974e-a811d862be7b",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLopBZj4PZWLNejZbEeB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac20245b-dc47-44c3-be4a-221c5246aab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ntc5sLfkKxCjUzogpR6wZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 114493,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2775
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 114493,
          "cache_creation_input_tokens": 2775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2775,
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

_source line 79 · 2026-05-24T05:02:52.407Z_

<details><summary>↩ Tool result · `toolu_01B4TaQiNmnh3xaL5DKv6iKA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:149:\label{fig:dual-factor-scatter}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_discussion.tex:578:\label{fig:per_relation_dr}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/appendix_beam_search.tex:103:\label{fig:beam-pareto}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac20245b-dc47-44c3-be4a-221c5246aab2",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "9fec483d-532d-460c-a100-a54744be4d40",
  "sourceToolAssistantUUID": "ac20245b-dc47-44c3-be4a-221c5246aab2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 80 · 2026-05-24T05:02:56.440Z_

Now I need to check which `tab:` labels defined in appendix files are referenced from main body files. Let me check the key ones referenced in main body sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fec483d-532d-460c-a100-a54744be4d40",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLopfbCnmhQwg92vLA1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bc4f9ce-ed4b-4d28-9cb9-aa269deb10de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dUxZ1YCNc6C5B4eE4SLwG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3411,
      "cache_read_input_tokens": 117268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3411,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 81 · 2026-05-24T05:02:58.934Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013CEnkdK4hEVPvQ27no4hGB`</summary>

```json
{
  "pattern": "\\\\ref\\{tab:(cross-model|docred-ablation|composability|scierc-ablation|ft-ablation|beam-sweep)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "section*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bc4f9ce-ed4b-4d28-9cb9-aa269deb10de",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLopfbCnmhQwg92vLA1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83b9b7a0-d0d8-4c1d-ad01-0ce824cf2870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dUxZ1YCNc6C5B4eE4SLwG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3411,
      "cache_read_input_tokens": 117268,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3411,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 82 · 2026-05-24T05:02:58.955Z_

<details><summary>↩ Tool result · `toolu_013CEnkdK4hEVPvQ27no4hGB`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:11:Table~\ref{tab:docred-ablation} presents the four-way ablation on DocRED,
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:10:Table~\ref{tab:cross-model} replicates S1 with Llama-3.1-8B and Mistral-7B under identical prompts.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section3_method_draft.tex:27:\noindent\textbf{Empirical Observation} (scale-dependent enabling dependency)\textbf{.} The grammar layer alone cannot enforce domain/range constraints (Proposition~1), while the semantic layer alone achieves only 24\% DR reduction at 8B without grammar-enforced vocabulary membership (\S\ref{sec:scierc-results}, Table~\ref{tab:scierc-ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex:32:Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement admits 33--37\% spurious pairs, eliminated by fine-tuning (Table~\ref{tab:composability}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:10:Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:67:Deterministic (greedy, $T{=}$0); robustness evidence in Table~\ref{tab:cross-model} and Appendices~\ref{app:bootstrap-effect-sizes},~\ref{app:prompt-sensitivity}.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:76:Table~\ref{tab:scierc-ablation} establishes that DR violations are pervasive (15--18\% across datasets) and that constraint layers interact non-additively: grammar-only achieves 3\% DR reduction on SciERC, semantic-only 24\%, but their composition yields 94\%---the \emph{empirical enabling dependency}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:78:Cross-model validation (3 models $\times$ 2 datasets; Table~\ref{tab:cross-model}) confirms DR drops of 76--99\% on SciERC and 42--90\% on DocRED, with R-F1 improving in 5/6 settings; post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:88:Fine-tuning alone reduces DR to 0.5--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.21\% with no significant $\Delta$R-F1 (Bonferroni-corrected; 95\% CIs $\subseteq [-0.69, {+}0.25]$\,pp; removed triples are 97.6--100\% false positives; Appendix~\ref{app:downstream-impact}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:90:Fallback frequency is model-dependent: Qwen triggers 0 fallbacks under LoRA + S1 on SciERC, while Llama triggers 5{,}882 (Table~\ref{tab:ft-ablation}), reflecting weaker entity typing; despite this, DR reaches 0.09\% on SciERC (0.21\% on DocRED), confirming that even frequent fallback does not compromise enforcement.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:10:Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC,
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:8:DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex:12:Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion_compressed.tex:9:Supporting evidence includes the fallback frequency gap: under LoRA + S1, Qwen-8B triggers 0 grammar-first fallbacks on SciERC while Llama-8B triggers 5{,}882 (Table~\ref{tab:ft-ablation}), yet both achieve DR\,$\leq$\,0.21\%, confirming that fallback frequency does not determine enforcement effectiveness.
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:12:A beam-width sweep ($k \in \{1,2,4,8\}$) on SciERC reveals $k{=}2$ as Pareto-optimal: R-F1 44.60 (highest), CF 0.11\%, at only 1.18$\times$ greedy S1 latency; $k{=}4$ achieves CF${=}$0\% but lower R-F1 (43.60) at 1.39$\times$ (Table~\ref{tab:beam-sweep}; latencies relative to greedy S1).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:23:A four-way ablation reveals scale-dependent layer interaction: semantic-only achieves 84\% DR reduction vs.\ 8B's 24\% (Table~\ref{tab:scierc-ablation}), though grammar remains necessary for RV elimination and CF control (semantic-only CF${=}$76).
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_runtime.tex:32:Our grammar-only ablation (Table~\ref{tab:scierc-ablation}, row~2) implements the same constraints as GCD~\cite{geng2023gcd} and BoostCD~\cite{boostcd2025}; vLLM \texttt{guided\_json}~\cite{kwon2023vllm} confirms equivalence on Qwen3-8B (DR${=}$15.26\%; other models use the same backend; Appendix~\ref{app:gcd-comparison}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83b9b7a0-d0d8-4c1d-ad01-0ce824cf2870",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "c3bb254c-b957-43a8-9629-3fae30c0c7ae",
  "sourceToolAssistantUUID": "83b9b7a0-d0d8-4c1d-ad01-0ce824cf2870",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-24T05:03:00.154Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017TmSRa1GoLYoyk1XcrHDnD`</summary>

```json
{
  "pattern": "\\\\label\\{tab:(cross-model|docred-ablation|composability|scierc-ablation)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "glob": "section*.tex",
  "output_mode": "content",
  "-n": true,
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3bb254c-b957-43a8-9629-3fae30c0c7ae",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLopfbCnmhQwg92vLA1G",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74d4cb05-a0e2-4c6d-a493-f6bc906fdc69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016dUxZ1YCNc6C5B4eE4SLwG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3411,
      "cache_read_input_tokens": 117268,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3411
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 434,
          "cache_read_input_tokens": 117268,
          "cache_creation_input_tokens": 3411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3411,
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

_source line 84 · 2026-05-24T05:03:00.169Z_

<details><summary>↩ Tool result · `toolu_017TmSRa1GoLYoyk1XcrHDnD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft_9b84f1.tex:71:\label{tab:docred-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_crossmodel_draft.tex:51:\label{tab:cross-model}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:68:\label{tab:scierc-ablation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex:137:\label{tab:composability}
/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft_4796e8.tex:69:\label{tab:scierc-ablation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74d4cb05-a0e2-4c6d-a493-f6bc906fdc69",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "2f0c2841-1212-4353-aa33-dc2cd17ae953",
  "sourceToolAssistantUUID": "74d4cb05-a0e2-4c6d-a493-f6bc906fdc69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-24T05:03:10.293Z_

Now I have all the data needed. Let me verify the main body tables referencing appendix-defined tables. The key ones are `tab:ft-ablation`, `tab:beam-sweep`, `tab:cross-model`, and `tab:docred-ablation`. Let me check where those are defined.

`tab:cross-model` is defined in `section5_crossmodel_draft.tex` (main body file) -- but wait, it's also in `appendix_zs_crossmodel.tex`. Let me verify which one is actually included in `main.tex`.

Looking at `main.tex`, the crossmodel section is NOT in the appendix section -- `section5_crossmodel_draft.tex` is NOT listed in `main.tex` as an `\input`. Let me check.

Looking at `main.tex` lines 48-56, I see `section5_scierc_draft`, `section5_wikievents_draft`, `section5_runtime`, but NOT `section5_crossmodel_draft` or `section5_docred_draft`. Let me re-check.

Actually, looking more carefully at `main.tex`:
- Lines 54-56: `section5_scierc_draft`, `section5_wikievents_draft`, `section5_runtime`
- `section5_docred_draft` and `section5_crossmodel_draft` are NOT listed

But wait, the user specified these as main body files. Let me check if they are actually included.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f0c2841-1212-4353-aa33-dc2cd17ae953",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLoqEmUwDpM46awGokj4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1023f2da-a0cd-475c-8264-1789147a12ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXvHn5EVhrgCrUPybz3e2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 120679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2965,
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

### Tool call

_source line 86 · 2026-05-24T05:03:11.475Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011sTg6DjrPps223yhKPPTgQ`</summary>

```json
{
  "pattern": "\\\\input\\{section5",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1023f2da-a0cd-475c-8264-1789147a12ad",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLoqEmUwDpM46awGokj4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e905696-1070-495a-a1d3-1286294cd37a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXvHn5EVhrgCrUPybz3e2C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2965,
      "cache_read_input_tokens": 120679,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2965
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 120679,
          "cache_creation_input_tokens": 2965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2965,
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

_source line 87 · 2026-05-24T05:03:11.488Z_

<details><summary>↩ Tool result · `toolu_011sTg6DjrPps223yhKPPTgQ`</summary>

```text
54:\input{section5_scierc_draft}
55:\input{section5_wikievents_draft}
56:\input{section5_runtime}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e905696-1070-495a-a1d3-1286294cd37a",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "cac35936-223a-4b2f-83f2-d3817643948b",
  "sourceToolAssistantUUID": "4e905696-1070-495a-a1d3-1286294cd37a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 88 · 2026-05-24T05:03:16.901Z_

So `section5_docred_draft`, `section5_crossmodel_draft` are NOT included in `main.tex`. The user listed them as main body files, but they are actually not `\input`'d. Let me check if they're included from within other files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cac35936-223a-4b2f-83f2-d3817643948b",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLor51dk1mXcTanUe8Yj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c7465b3-a5df-4c46-ad75-d3c5b3435d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018z4KfayC1TRyHDYgiMSgVj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 123644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 89 · 2026-05-24T05:03:17.877Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CWkvQcyxbp9rUNQLCfBrqh`</summary>

```json
{
  "pattern": "\\\\input\\{section5_docred",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c7465b3-a5df-4c46-ad75-d3c5b3435d9e",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLor51dk1mXcTanUe8Yj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0de3ad32-73f3-4625-b02c-610650d60256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018z4KfayC1TRyHDYgiMSgVj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 123644,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 538,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 90 · 2026-05-24T05:03:17.899Z_

<details><summary>↩ Tool result · `toolu_01CWkvQcyxbp9rUNQLCfBrqh`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0de3ad32-73f3-4625-b02c-610650d60256",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "fab3c340-4c55-4091-afc3-0c07fdb01dda",
  "sourceToolAssistantUUID": "0de3ad32-73f3-4625-b02c-610650d60256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-24T05:03:18.844Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01EktYVKU6VCaJazt5id1SMk`</summary>

```json
{
  "pattern": "\\\\input\\{section5_crossmodel",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fab3c340-4c55-4091-afc3-0c07fdb01dda",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLor51dk1mXcTanUe8Yj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff24b17b-9aae-41c1-9d0e-18663884dd0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018z4KfayC1TRyHDYgiMSgVj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 123644,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 538
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 343,
          "cache_read_input_tokens": 123644,
          "cache_creation_input_tokens": 538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 538,
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

_source line 92 · 2026-05-24T05:03:18.858Z_

<details><summary>↩ Tool result · `toolu_01EktYVKU6VCaJazt5id1SMk`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff24b17b-9aae-41c1-9d0e-18663884dd0f",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "883a73ce-1477-45a9-8bdc-ad404ca665e2",
  "sourceToolAssistantUUID": "ff24b17b-9aae-41c1-9d0e-18663884dd0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-24T05:03:22.134Z_

Interesting -- `section5_docred_draft.tex` and `section5_crossmodel_draft.tex` are NOT included anywhere. But maybe they are included inline from `section5_scierc_draft.tex`? Let me check.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "883a73ce-1477-45a9-8bdc-ad404ca665e2",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLorceQF8TPsDugXKgdw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2012266-6fd0-4ba4-b4ae-a02f17a46eb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9TSjLq7JKCNdae8tDZp4F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 124182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 410,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 94 · 2026-05-24T05:03:22.790Z_

<details open><summary>🔧 Tool call — Grep · `toolu_019Skmsk2vadvGvYfWXfaDdZ`</summary>

```json
{
  "pattern": "\\\\input",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2012266-6fd0-4ba4-b4ae-a02f17a46eb9",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLorceQF8TPsDugXKgdw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83f8be00-0d91-45a9-ac92-af8d3d684f96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9TSjLq7JKCNdae8tDZp4F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 124182,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 124182,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 410,
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

_source line 95 · 2026-05-24T05:03:22.808Z_

<details><summary>↩ Tool result · `toolu_019Skmsk2vadvGvYfWXfaDdZ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83f8be00-0d91-45a9-ac92-af8d3d684f96",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "b505df0b-5f84-459f-a1b9-15b01971d22c",
  "sourceToolAssistantUUID": "83f8be00-0d91-45a9-ac92-af8d3d684f96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 96 · 2026-05-24T05:03:44.085Z_

So `section5_docred_draft.tex` and `section5_crossmodel_draft.tex` are orphan files not included in the build. But the user listed them as main body files for this audit. I'll still check references from them, but note they're not actually compiled. Now let me also verify `section3_violation_landscape.tex` -- it IS included via line 52 of main.tex.

Now I have all the information needed. Let me compile the complete audit.

Here is the complete inventory of all `app:` labels defined in appendix files:

**appendix_prompts.tex**: `app:prompts`
**appendix_related_work.tex**: `app:related_work`
**appendix_discussion.tex**: `app:discussion`, `app:fallback-coverage`, `app:causal-tracing`, `app:enabling-confound`, `app:cf-dr-tradeoff`, `app:dual-factor`, `app:bootstrap-effect-sizes`, `app:cf-distribution`, `app:cascade-analysis`, `app:lora-per-relation`, `app:ft-ablation`, `app:docred-zs-ablation`, `app:residual-dr-analysis`, `app:posthoc-extended`, `app:runtime`, `app:ft-latency`, `app:fuzzy-matching`, `app:per-relation-landscape`, `app:wikievents`, `app:wikievents-kappa`, `app:lucky-violations`, `app:trie-baseline`, `app:gcd-comparison`
**appendix_70b_ablation.tex**: `app:70b-ablation`, `app:70b-docred`, `app:70b-docred-zs`
**appendix_llama_per_relation.tex**: `app:llama-per-relation`
**appendix_sampling_table.tex**: `app:sampling`
**appendix_beam_search.tex**: `app:beam-search`
**appendix_reproducibility.tex**: `app:reproducibility`, `app:greedy-determinism`, `app:power-analysis`
**appendix_power_analysis.tex**: `app:power-analysis-full`
**appendix_doc_length.tex**: `app:doc-length`
**appendix_prompt_sensitivity.tex**: `app:prompt-sensitivity`
**appendix_case_studies.tex**: `app:case-studies`, `app:case-dr`, `app:case-rv-dr`, `app:case-scale`, `app:case-cf`, `app:error-analysis`
**appendix_downstream_analysis.tex**: `app:downstream-impact`
**appendix_scalability.tex**: `app:scalability`
**appendix_full_ft.tex**: `app:full-ft`
**appendix_tcr.tex**: `app:tcr`
**appendix_kappa_case_study.tex**: `app:kappa-case-study`
**appendix_high_kappa_analysis.tex**: `app:kappa-analysis`
**appendix_order_invariance.tex**: `app:order-invariance`
**appendix_pumping_lemma.tex**: `app:pumping-lemma`
**appendix_wikievents_pilot.tex**: `app:wikievents-pilot`
**appendix_zs_crossmodel.tex**: `app:cross-model-zs`
**appendix_quantization.tex**: `app:quantization`
**appendix_gollie_comparison.tex**: `app:gollie-comparison`
**appendix_ai_assistants.tex**: `app:ai-assistants`

Now let me map each label to whether it's referenced from the main body (the actually-included files).

The **main body files** (actually compiled via `\input` in main.tex) are:
- `abstract.tex`
- `section1_introduction_draft.tex`
- `section2_background.tex`
- `section3_method_draft.tex`
- `section3_violation_landscape.tex`
- `section4_composition_draft.tex`
- `section5_scierc_draft.tex`
- `section5_wikievents_draft.tex`
- `section5_runtime.tex`
- `section6_related_work.tex`
- `section7_conclusion_compressed.tex`
- `main.tex` (Limitations, Ethics)
- `checklist.tex` (not \input'd in main.tex but may be separate)

Let me check if checklist.tex is included.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b505df0b-5f84-459f-a1b9-15b01971d22c",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLoruZ9LawDQ3mQgmKTQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "895f5c08-fb2f-467d-b70f-f21b582c6403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZvrWeZxMhBEg1vvMcUMW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 124592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 224,
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

### Tool call

_source line 97 · 2026-05-24T05:03:44.644Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QVAZyrvL62gXCRntu166QQ`</summary>

```json
{
  "pattern": "\\\\input\\{checklist",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "895f5c08-fb2f-467d-b70f-f21b582c6403",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLoruZ9LawDQ3mQgmKTQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "829ceb17-98fd-4c63-b07f-2e236a084088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZvrWeZxMhBEg1vvMcUMW6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 224,
      "cache_read_input_tokens": 124592,
      "output_tokens": 1213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1213,
          "cache_read_input_tokens": 124592,
          "cache_creation_input_tokens": 224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 224,
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

_source line 98 · 2026-05-24T05:03:44.672Z_

<details><summary>↩ Tool result · `toolu_01QVAZyrvL62gXCRntu166QQ`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "829ceb17-98fd-4c63-b07f-2e236a084088",
  "isSidechain": true,
  "promptId": "f7077fc8-66b5-44e3-a911-eceea60d9908",
  "agentId": "a3140ddb0efc16ba7",
  "type": "user",
  "uuid": "9b2f7e5c-7718-4592-9609-a76a18ea1cb6",
  "sourceToolAssistantUUID": "829ceb17-98fd-4c63-b07f-2e236a084088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard"
}
```

</details>

---

### Assistant

_source line 99 · 2026-05-24T05:05:07.190Z_

`checklist.tex` is also not included in `main.tex`. It references `app:reproducibility`, `app:wikievents`, `app:prompts` but is not compiled. I'll note this separately.

Now I have all the data. Here is the full audit:

---

## Appendix Sections

### appendix_prompts.tex
1. **Section: Prompt Templates** (label: `app:prompts`) -- **REFERENCED from main body**: `checklist.tex:50` BUT `checklist.tex` is not `\input`'d in `main.tex`. No reference from any actually-compiled main body file. **ORPHAN from compiled main body.**

### appendix_related_work.tex
2. **Section: Extended Related Work** (label: `app:related_work`) -- **REFERENCED from main body**: `section6_related_work.tex:4` ("We provide a detailed survey in Appendix~\ref{app:related_work}"). **REFERENCED.**

### appendix_discussion.tex (contains many paragraph-level labels)
3. **Section: Extended Discussion** (label: `app:discussion`) -- No direct `\ref{app:discussion}` found anywhere. **ORPHAN** (section-level label never referenced, though sub-labels within it are).

4. **Paragraph: Fallback Behavior** (label: `app:fallback-coverage`) -- No `\ref{app:fallback-coverage}` found. **ORPHAN.**

5. **Paragraph: Fallback Causal Tracing** (label: `app:causal-tracing`) -- **REFERENCED from main body**: `section4_composition_draft.tex:28`, `section7_conclusion_compressed.tex:8`. **REFERENCED.**

6. **Paragraph: Enabling Dependency Confound** (label: `app:enabling-confound`) -- No `\ref{app:enabling-confound}` found. **ORPHAN.**

7. **Paragraph: CF-DR Trade-off** (label: `app:cf-dr-tradeoff`) -- **REFERENCED from main body**: `main.tex:71` (Limitations). **REFERENCED.**

8. **Paragraph: Dual-Factor Quantitative Analysis** (label: `app:dual-factor`) -- No `\ref{app:dual-factor}` found. **ORPHAN.**

9. **Paragraph: Bootstrap CIs** (label: `app:bootstrap-effect-sizes`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:67`. **REFERENCED.**

10. **Paragraph: CF Distribution** (label: `app:cf-distribution`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:91,98`. **REFERENCED.**

11. **Paragraph: Cascade Analysis** (label: `app:cascade-analysis`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:99`. **REFERENCED.**

12. **Paragraph: LoRA Per-Relation** (label: `app:lora-per-relation`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:89`. **REFERENCED.**

13. **Paragraph: FT Ablation** (label: `app:ft-ablation`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:89`. **REFERENCED.**

14. **Paragraph: DocRED ZS Ablation** (label: `app:docred-zs-ablation`) -- No `\ref{app:docred-zs-ablation}` found from main body. **ORPHAN.**

15. **Paragraph: Residual DR Analysis** (label: `app:residual-dr-analysis`) -- **REFERENCED from main body**: `main.tex:74`, `section5_scierc_draft.tex:147`, `section5_docred_draft.tex:12`. **REFERENCED.**

16. **Paragraph: Post-Hoc Extended** (label: `app:posthoc-extended`) -- **REFERENCED from main body**: `section5_crossmodel_draft.tex:59` -- but this file is NOT compiled. Also referenced from `appendix_zs_crossmodel.tex:53` (appendix-to-appendix). **ORPHAN from compiled main body.**

17. **Paragraph: Runtime** (label: `app:runtime`) -- Referenced from `appendix_reproducibility.tex:17` (appendix-to-appendix). No main body ref. **ORPHAN from main body.**

18. **Paragraph: FT Latency** (label: `app:ft-latency`) -- No `\ref{app:ft-latency}` found. **ORPHAN.**

19. **Paragraph: Fuzzy Matching** (label: `app:fuzzy-matching`) -- No `\ref{app:fuzzy-matching}` found. **ORPHAN.**

20. **Paragraph: Per-Relation Landscape** (label: `app:per-relation-landscape`) -- **REFERENCED from main body**: `section3_violation_landscape.tex:19`. **REFERENCED.**

21. **Paragraph: WikiEvents Dataset Details** (label: `app:wikievents`) -- **REFERENCED from main body**: `checklist.tex:36` (not compiled). Also referenced from `appendix_wikievents_pilot.tex:10` (appendix-to-appendix). **ORPHAN from compiled main body.**

22. **Paragraph: WikiEvents Kappa** (label: `app:wikievents-kappa`) -- No `\ref{app:wikievents-kappa}` found. **ORPHAN.**

23. **Paragraph: Lucky Violations** (label: `app:lucky-violations`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:146`. **REFERENCED.**

24. **Paragraph: Trie Baseline** (label: `app:trie-baseline`) -- **REFERENCED from main body**: `section5_runtime.tex:33`. **REFERENCED.**

25. **Paragraph: GCD Comparison** (label: `app:gcd-comparison`) -- **REFERENCED from main body**: `section5_runtime.tex:32`. **REFERENCED.**

### appendix_70b_ablation.tex
26. **Paragraph: 70B Ablation** (label: `app:70b-ablation`) -- **REFERENCED from main body**: `main.tex:92`, `section5_runtime.tex:27`. **REFERENCED.**

27. **Paragraph: 70B DocRED** (label: `app:70b-docred`) -- No `\ref{app:70b-docred}` found. **ORPHAN.**

28. **Paragraph: 70B DocRED ZS** (label: `app:70b-docred-zs`) -- No `\ref{app:70b-docred-zs}` found. **ORPHAN.**

### appendix_llama_per_relation.tex
29. **Section: Per-Relation Violation Analysis (Llama)** (label: `app:llama-per-relation`) -- Referenced from `appendix_discussion.tex:577` (appendix-to-appendix). No main body ref. **ORPHAN from main body.**

### appendix_sampling_table.tex
30. **Section: Sampling Robustness** (label: `app:sampling`) -- **REFERENCED from main body**: `main.tex:84`. **REFERENCED.**

### appendix_beam_search.tex
31. **Section: Beam Search Compatibility** (label: `app:beam-search`) -- **REFERENCED from main body**: `main.tex:84`, `section5_runtime.tex:11`. **REFERENCED.**

### appendix_reproducibility.tex
32. **Section: Reproducibility Details** (label: `app:reproducibility`) -- **REFERENCED from main body**: `checklist.tex:24,27,47,50,56` (not compiled). No ref from compiled main body files. **ORPHAN from compiled main body.**

33. **Paragraph: Greedy Determinism** (label: `app:greedy-determinism`) -- Referenced only from within `appendix_reproducibility.tex:51` (self-reference). **ORPHAN.**

34. **Paragraph: Power Analysis** (label: `app:power-analysis`) -- No `\ref{app:power-analysis}` from main body. **ORPHAN.**

### appendix_power_analysis.tex
35. **Paragraph: Power Analysis Full** (label: `app:power-analysis-full`) -- Referenced from `appendix_wikievents_pilot.tex:64` (appendix-to-appendix). No main body ref. **ORPHAN from main body.**

### appendix_doc_length.tex
36. **Section: Document Length** (label: `app:doc-length`) -- No `\ref{app:doc-length}` found anywhere. **ORPHAN.**

### appendix_prompt_sensitivity.tex
37. **Section: Prompt Sensitivity** (label: `app:prompt-sensitivity`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:67`. **REFERENCED.**

### appendix_case_studies.tex
38. **Section: Error Analysis and Case Studies** (label: `app:case-studies`) -- No `\ref{app:case-studies}` from main body. **ORPHAN.**

39. **Subsection: DR Correction** (label: `app:case-dr`) -- No `\ref{app:case-dr}` found. **ORPHAN.**

40. **Subsection: RV-DR Correction** (label: `app:case-rv-dr`) -- No `\ref{app:case-rv-dr}` found. **ORPHAN.**

41. **Subsection: Scale Effect** (label: `app:case-scale`) -- No `\ref{app:case-scale}` found. **ORPHAN.**

42. **Subsection: Limitation CF** (label: `app:case-cf`) -- No `\ref{app:case-cf}` found. **ORPHAN.**

43. **Subsection: Error Analysis** (label: `app:error-analysis`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:146`. **REFERENCED.**

### appendix_downstream_analysis.tex
44. **Paragraph: Downstream Impact** (label: `app:downstream-impact`) -- **REFERENCED from main body**: `section5_scierc_draft.tex:88`. **REFERENCED.**

### appendix_scalability.tex
45. **Section: Ontology Scalability** (label: `app:scalability`) -- **REFERENCED from main body**: `main.tex:88,90`, `section5_runtime.tex:6`. **REFERENCED.**

### appendix_full_ft.tex
46. **Section: Full Fine-Tuning Baseline** (label: `app:full-ft`) -- **REFERENCED from main body**: `main.tex:91`. **REFERENCED.**

### appendix_tcr.tex
47. **Section: Post-hoc Type Consistency Resolution** (label: `app:tcr`) -- **REFERENCED from main body**: `main.tex:77`, `section3_method_draft.tex:17`, `section5_scierc_draft.tex:79`, `section7_conclusion_compressed.tex:16`. **REFERENCED.**

### appendix_kappa_case_study.tex
48. **Section: Constraint Tightness Case Study** (label: `app:kappa-case-study`) -- **REFERENCED from main body**: `section4_composition_draft.tex:22`. **REFERENCED.**

### appendix_high_kappa_analysis.tex
49. **Paragraph: Schema Ambiguity Analysis** (label: `app:kappa-analysis`) -- No `\ref{app:kappa-analysis}` from main body. **ORPHAN.**

### appendix_order_invariance.tex
50. **Paragraph: Order Invariance** (label: `app:order-invariance`) -- **REFERENCED from main body**: `section4_composition_draft.tex:33`. **REFERENCED.**

### appendix_pumping_lemma.tex
51. **Section: Full Proof of Proposition 1** (label: `app:pumping-lemma`) -- **REFERENCED from main body**: `section3_method_draft.tex:24`. **REFERENCED.**

### appendix_wikievents_pilot.tex
52. **Section: WikiEvents Event Extraction Pilot** (label: `app:wikievents-pilot`) -- **REFERENCED from main body**: `section5_wikievents_draft.tex:6`. **REFERENCED.**

### appendix_zs_crossmodel.tex
53. **Section: Zero-Shot Cross-Model Validation** (label: `app:cross-model-zs`) -- **REFERENCED from main body**: `section1_introduction_draft.tex:14,21`, `section3_violation_landscape.tex:7,13`, `section5_scierc_draft.tex:77`. **REFERENCED.**

### appendix_quantization.tex
54. **Section: Quantization Robustness** (label: `app:quantization`) -- **REFERENCED from main body**: `main.tex:89`, `section5_runtime.tex:20`, `section7_conclusion_compressed.tex:10`. **REFERENCED.**

### appendix_gollie_comparison.tex
55. **Section: GoLLIE Comparison** (label: `app:gollie-comparison`) -- **REFERENCED from main body**: `section6_related_work.tex:13`. **REFERENCED.**

### appendix_ai_assistants.tex
56. **Section: Use of AI Assistants** (label: `app:ai-assistants`) -- No `\ref{app:ai-assistants}` found. **ORPHAN.**

---

## Summary

### Appendix Sections Referenced from Main Body (24 labels)
1. `app:related_work` -- section6_related_work.tex
2. `app:causal-tracing` -- section4_composition_draft.tex, section7_conclusion_compressed.tex
3. `app:cf-dr-tradeoff` -- main.tex (Limitations)
4. `app:bootstrap-effect-sizes` -- section5_scierc_draft.tex
5. `app:cf-distribution` -- section5_scierc_draft.tex
6. `app:cascade-analysis` -- section5_scierc_draft.tex
7. `app:lora-per-relation` -- section5_scierc_draft.tex
8. `app:ft-ablation` -- section5_scierc_draft.tex, section7_conclusion_compressed.tex
9. `app:residual-dr-analysis` -- main.tex, section5_scierc_draft.tex
10. `app:per-relation-landscape` -- section3_violation_landscape.tex
11. `app:lucky-violations` -- section5_scierc_draft.tex
12. `app:trie-baseline` -- section5_runtime.tex
13. `app:gcd-comparison` -- section5_runtime.tex
14. `app:70b-ablation` -- main.tex, section5_runtime.tex
15. `app:sampling` -- main.tex
16. `app:beam-search` -- main.tex, section5_runtime.tex
17. `app:prompt-sensitivity` -- section5_scierc_draft.tex
18. `app:error-analysis` -- section5_scierc_draft.tex
19. `app:downstream-impact` -- section5_scierc_draft.tex
20. `app:scalability` -- main.tex, section5_runtime.tex
21. `app:full-ft` -- main.tex
22. `app:tcr` -- main.tex, section3_method_draft.tex, section5_scierc_draft.tex, section7_conclusion_compressed.tex
23. `app:kappa-case-study` -- section4_composition_draft.tex
24. `app:order-invariance` -- section4_composition_draft.tex
25. `app:pumping-lemma` -- section3_method_draft.tex
26. `app:wikievents-pilot` -- section5_wikievents_draft.tex
27. `app:cross-model-zs` -- section1_introduction_draft.tex, section3_violation_landscape.tex, section5_scierc_draft.tex
28. `app:quantization` -- main.tex, section5_runtime.tex, section7_conclusion_compressed.tex
29. `app:gollie-comparison` -- section6_related_work.tex

### Orphan Appendices (NOT referenced from compiled main body -- 27 labels)

**Section-level orphans** (entire appendix section/file with no main body pointer):
- `app:prompts` -- Prompt Templates. Only referenced from `checklist.tex` which is not compiled. **Recommendation**: Add a reference in the Experiments setup text, e.g. "Prompt templates are provided in Appendix~\ref{app:prompts}."
- `app:discussion` -- Extended Discussion section-level label. Sub-labels within it ARE referenced; the section-level label itself is never used. **Low priority** -- the sub-labels provide navigation.
- `app:doc-length` -- Document Length analysis. Valuable robustness analysis. **Recommendation**: Add pointer in section5 (e.g., "Constraint effectiveness is consistent across document lengths (Appendix~\ref{app:doc-length})").
- `app:case-studies` -- Error Analysis and Case Studies (section-level). `app:error-analysis` subsection IS referenced but the parent section label is not. **Low priority.**
- `app:reproducibility` -- Reproducibility Details. Only referenced from `checklist.tex` (not compiled). **Recommendation**: Add pointer from Experiments section or Limitations (e.g., "Full reproducibility details including hyperparameters are in Appendix~\ref{app:reproducibility}").
- `app:ai-assistants` -- Use of AI Assistants. Standard disclosure, typically not cross-referenced. **No action needed.**
- `app:kappa-analysis` -- Schema Ambiguity Analysis. Extends `app:kappa-case-study` analysis. **Recommendation**: Add pointer alongside the existing `app:kappa-case-study` reference in section4_composition_draft.tex.
- `app:llama-per-relation` -- Per-Relation Violation Analysis (Llama). Only referenced from appendix_discussion.tex. **Recommendation**: Add pointer from section5 cross-model results (e.g., alongside the existing cross-model reference).

**Paragraph-level orphans** (sub-sections within appendix files with no main body pointer):
- `app:fallback-coverage` -- Fallback coverage analysis in appendix_discussion.tex. **Recommendation**: Could be referenced from section4_composition_draft.tex alongside `app:causal-tracing`.
- `app:enabling-confound` -- Confound analysis. **Recommendation**: Reference from section4_composition_draft.tex where the enabling dependency is discussed.
- `app:dual-factor` -- Dual-factor quantitative analysis. **Recommendation**: Reference from section4_composition_draft.tex near the constraint tightness discussion.
- `app:docred-zs-ablation` -- DocRED zero-shot ablation table. **Recommendation**: Reference from section5's DocRED discussion or section5_runtime.tex.
- `app:posthoc-extended` -- Post-hoc filtering extended comparison. Only referenced from non-compiled files and appendix-to-appendix. **Recommendation**: Add pointer from section5_scierc_draft.tex where post-hoc filtering is mentioned.
- `app:runtime` -- Zero-shot runtime profiling. Only referenced from appendix_reproducibility.tex. **Recommendation**: Reference from section5_runtime.tex.
- `app:ft-latency` -- Fine-tuned latency. Never referenced. **Recommendation**: Reference from section5_runtime.tex.
- `app:fuzzy-matching` -- Relation matching protocol. Never referenced. **Recommendation**: Reference from Experiments setup or Reproducibility.
- `app:wikievents` -- WikiEvents dataset details. Referenced only from non-compiled checklist and appendix. **Recommendation**: Reference from section5_wikievents_draft.tex.
- `app:wikievents-kappa` -- WikiEvents constraint tightness. Never referenced. **Recommendation**: Reference from section5_wikievents_draft.tex.
- `app:case-dr`, `app:case-rv-dr`, `app:case-scale`, `app:case-cf` -- Individual case study subsections. **Low priority** -- `app:error-analysis` is referenced, and readers navigate to individual cases from there.
- `app:greedy-determinism` -- Self-referenced only. **Low priority** -- contained within `app:reproducibility`.
- `app:power-analysis` -- 200-doc subset justification. **Recommendation**: Reference from section5_runtime.tex where 70B/200-doc is discussed.
- `app:power-analysis-full` -- Statistical power for WikiEvents n=20. Referenced only from appendix. **Recommendation**: Reference from section5_wikievents_draft.tex where n=20 is mentioned.
- `app:70b-docred` -- 70B DocRED FT results. Never referenced from main body. **Recommendation**: Reference from section5_runtime.tex alongside `app:70b-ablation`.
- `app:70b-docred-zs` -- 70B DocRED ZS ablation. Never referenced. **Recommendation**: Same as above.

### Broken References (main body referencing nonexistent appendix labels)

No broken `\ref{app:...}` references found. All `app:` labels referenced from main body files exist in the appendix files.

### Additional Findings

1. **Non-compiled main body files**: `section5_docred_draft.tex` and `section5_crossmodel_draft.tex` exist but are NOT `\input`'d in `main.tex` or any other compiled file. They contain `\ref{app:...}` references. If these files were intended to be part of the paper, they need to be added to `main.tex`. If they are deprecated, their content may need to be verified as covered elsewhere.

2. **Non-compiled checklist.tex**: `checklist.tex` references `app:reproducibility`, `app:wikievents`, `app:prompts` but is not `\input`'d in `main.tex`. If this is meant to be submitted as a separate document, these references may cause undefined label warnings.

3. **Tab/fig references from main body to appendix tables**: The main body references `tab:cross-model` (defined in `appendix_zs_crossmodel.tex`), `tab:ft-ablation` (defined in `appendix_discussion.tex`), `tab:beam-sweep` (defined in `appendix_beam_search.tex`), and `tab:docred-ablation` (defined in `appendix_discussion.tex`). All exist and are valid. **No broken tab/fig references found.**

### Priority Orphans (most impactful to fix)

The following orphan appendices contain substantive content that reviewers would want to see referenced:

1. **`app:prompts`** -- Reviewers expect prompt templates to be pointed to. Add ref in Experiments setup.
2. **`app:reproducibility`** -- Reproducibility section is required by ARR. Add ref in Experiments or main text.
3. **`app:doc-length`** -- Robustness analysis across document lengths. Add ref in Results.
4. **`app:docred-zs-ablation`** -- Full DocRED ablation table parallel to SciERC. Add ref near DocRED discussion.
5. **`app:posthoc-extended`** -- Extended post-hoc comparison. Add ref from main body post-hoc discussion.
6. **`app:runtime`** and **`app:ft-latency`** -- Latency details. Add refs from section5_runtime.tex.
7. **`app:wikievents`** and **`app:wikievents-kappa`** -- WikiEvents dataset details. Add refs from section5_wikievents_draft.tex.
8. **`app:70b-docred`** and **`app:70b-docred-zs`** -- 70B DocRED results. Add refs from 70B discussion in section5_runtime.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b2f7e5c-7718-4592-9609-a76a18ea1cb6",
  "isSidechain": true,
  "agentId": "a3140ddb0efc16ba7",
  "requestId": "req_011CbLotY3dezrmNk5jprpXh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "552819c6-64c2-4a72-a982-adf1c75c2868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJ25pQYJKgMb991gSqJstm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 124816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1228,
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
