# Research conversation: Read ALL appendix .tex files of the paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_co

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a16b2408c4cfcd2a6.jsonl`
- **Structured JSON:** [`d14ab0adb0b0ab443834.json`](../../sessions/d1/d14ab0adb0b0ab443834.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-25T19:41:55.359Z_

Read ALL appendix .tex files of the paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/ and extract EVERY numerical claim.

The appendix files are (read each one fully):
1. appendix_prompts.tex
2. appendix_related_work.tex
3. appendix_discussion.tex
4. appendix_70b_ablation.tex
5. appendix_llama_per_relation.tex
6. appendix_sampling_table.tex
7. appendix_beam_search.tex
8. appendix_reproducibility.tex
9. appendix_power_analysis.tex
10. appendix_doc_length.tex
11. appendix_prompt_sensitivity.tex
12. appendix_case_studies.tex
13. appendix_downstream_analysis.tex
14. appendix_scalability.tex
15. appendix_full_ft.tex
16. appendix_tcr.tex
17. appendix_kappa_case_study.tex
18. appendix_high_kappa_analysis.tex
19. appendix_order_invariance.tex
20. appendix_pumping_lemma.tex
21. appendix_wikievents_pilot.tex
22. appendix_zs_crossmodel.tex
23. appendix_quantization.tex
24. appendix_gollie_comparison.tex
25. appendix_ai_assistants.tex

For each file, extract EVERY number (percentages, counts, F1 scores, p-values, confidence intervals, dataset sizes, etc.). Format as:

```
## [filename]
- "73.18%" — description (line ~N)
- "551" — description (line ~N)
...
```

Focus especially on:
- Tables with numerical data (every cell value)
- Statistical test results (p-values, CIs, effect sizes)
- Dataset statistics
- Hyperparameters
- Any number that also appears in the main text (cross-reference candidates)

Be thorough — this is a data integrity audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "ff5b4683-6bca-4dc7-bec9-fbb66e4a1c42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:41:55.365Z_

```json
{
  "parentUuid": "ff5b4683-6bca-4dc7-bec9-fbb66e4a1c42",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "accd34e6-ca84-418e-b587-0c4b0325a99c",
  "timestamp": "2026-05-25T19:41:55.365Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:41:57.503Z_

I'll read all 25 appendix files in parallel to extract every numerical claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "accd34e6-ca84-418e-b587-0c4b0325a99c",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrfVEToVNwXyRAv5taB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5818ec86-a528-46bb-a43f-e15e01e08aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HxBrancg45LTeb2d1j9JxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25258,
      "cache_read_input_tokens": 7257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25258,
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

_source line 4 · 2026-05-25T19:41:58.413Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ya1TiLwDAbiKAvYtzW7HoC`</summary>

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
  "parentUuid": "5818ec86-a528-46bb-a43f-e15e01e08aa4",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrfVEToVNwXyRAv5taB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39753715-612c-470c-b34e-d40f87c4fa6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HxBrancg45LTeb2d1j9JxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25258,
      "cache_read_input_tokens": 7257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25258,
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

_source line 5 · 2026-05-25T19:41:58.418Z_

<details><summary>↩ Tool result · `toolu_01Ya1TiLwDAbiKAvYtzW7HoC`</summary>

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
  "parentUuid": "39753715-612c-470c-b34e-d40f87c4fa6d",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "01a6e588-e9f5-4e75-aa32-b1a6faeef758",
  "sourceToolAssistantUUID": "39753715-612c-470c-b34e-d40f87c4fa6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T19:41:58.860Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QBNWRcJqSyRWyE89zoc8HS`</summary>

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
  "parentUuid": "01a6e588-e9f5-4e75-aa32-b1a6faeef758",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrfVEToVNwXyRAv5taB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2115e428-533f-49f0-8e8e-f0051d2c5ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HxBrancg45LTeb2d1j9JxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25258,
      "cache_read_input_tokens": 7257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25258,
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

_source line 7 · 2026-05-25T19:41:58.864Z_

<details><summary>↩ Tool result · `toolu_01QBNWRcJqSyRWyE89zoc8HS`</summary>

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
59	ADELIE~\cite{qi2024adelie} uses supervised fine-tuning (SFT) and Direct Preference Optimization (DPO) to align LLMs on IE tasks, achieving state-of-the-art results among open-source models while preserving general capabilities, though compliance with ontological constraints remains a learned soft preference rather than a hard constraint.
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
74	OntoLogX~\cite{ontologx_2025} applies Shapes Constraint Language (SHACL) validation to LLM-generated knowledge graphs, iteratively re-prompting the LLM to correct constraint violations and reducing them by approximately 10$\times$ across multiple correction rounds. This demonstrates the detect-then-fix paradigm's effectiveness but also its inherent multi-pass cost.
75	\citet{upadhyay2023openie} inject entity-type knowledge as constraints into Open IE via both constrained inference and constraint-aware training, improving F1 by 29\% on CaRB, though their constrained inference operates over a discrete candidate set rather than during autoregressive generation.
76	\citet{regino2025kgcurator} propose a multi-stage LLM pipeline for validating Resource Description Framework (RDF) triple insertions against RDF Schema (RDFS) domain/range constraints, where each validation step requires a separate LLM call, effective but computationally expensive at scale.
77	RELATE~\cite{olasunkanmi2025relate} addresses the alignment gap between LLM-extracted biomedical relations and standardized ontology predicates through a three-stage pipeline: ontology preprocessing with predicate embeddings, similarity-based retrieval via SapBERT, and LLM-based reranking with negation handling, achieving 94\% accuracy@10 on ChemProt.
78	While RELATE demonstrates effective ontology grounding for relation extraction, its constraints are applied \emph{post-extraction} through retrieval and reranking rather than during generation, and it requires domain-specific embedding models trained on biomedical corpora.
79	OntoCoDec enforces ontology constraints \emph{during} autoregressive decoding and requires no additional trained components beyond the base LLM.
80	Concurrently, \citet{zhou2026ontologytools} compile Web Ontology Language (OWL) ontologies into executable tool interfaces within The World Avatar framework; LLM agents must invoke ontology-aware tools that enforce semantic constraints during knowledge graph construction from scientific text.
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
  "parentUuid": "2115e428-533f-49f0-8e8e-f0051d2c5ab1",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "e07f20ed-85f2-4307-af0c-0f0e3aaf0fb0",
  "sourceToolAssistantUUID": "2115e428-533f-49f0-8e8e-f0051d2c5ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T19:41:59.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_014mEQW9FKV5HRPXQJWNvwyq`</summary>

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
  "parentUuid": "e07f20ed-85f2-4307-af0c-0f0e3aaf0fb0",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrfVEToVNwXyRAv5taB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90c41da8-090d-4de3-abe3-d07168db98e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HxBrancg45LTeb2d1j9JxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25258,
      "cache_read_input_tokens": 7257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25258,
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

_source line 9 · 2026-05-25T19:42:00.055Z_

<details><summary>↩ Tool result · `toolu_014mEQW9FKV5HRPXQJWNvwyq`</summary>

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
53	\setlength{\tabcolsep}{4pt}
54	\resizebox{\columnwidth}{!}{%
55	\begin{tabular}{@{}ll rrr@{}}
56	\toprule
57	\textbf{Model} & \textbf{Setting} & \textbf{Fallback Rate} & \textbf{DR} & \textbf{From FB} \\
58	\midrule
59	Qwen3-8B  & FT S1 & 0/2256 (0\%)    & 0  & N/A \\
60	Qwen3-8B  & ZS S1 & 16/3458 (0.46\%) & 16 & 100\% \\
61	Llama-3.1-8B & FT S1 & 1/2162 (0.05\%) & 1  & 100\% \\
62	Llama-3.1-8B & ZS S1 & 1/2630 (0.04\%) & 1  & 100\% \\
63	\bottomrule
64	\end{tabular}}
65	\caption{Fallback causal tracing on SciERC (551 documents). Fallback Rate: type-bearing positions where $S(t) \cap G(t) = \emptyset$ triggers grammar-first fallback. DR: residual domain/range violations. From FB: fraction of DR violations occurring at fallback positions. All violations occur exclusively at tail\_type positions (range constraints are tighter than domain constraints).}
66	\label{tab:causal-tracing}
67	\end{table}
68	
69	When the semantic mask is active, $\text{DR}_{\text{independent}} = 0$: the type constraint processor structurally prevents domain/range violations.
70	All 18 residual DR violations across four configurations occur exclusively at fallback positions, confirming that grammar-first fallback is a necessary condition for residual DR.
71	Fine-tuning reduces fallback to near-zero ($\leq$0.05\%), effectively eliminating the sole source of residual violations.
72	All fallback events occur at tail\_type positions, where $|\operatorname{range}(r, \tau^h)|$ is smaller than $|\operatorname{dom}(r)|$, making the intersection $S(t) \cap G(t)$ more likely to be empty.
73	
74	%%% Enabling Dependency: Confound Analysis %%%
75	
76	\paragraph{Enabling Dependency: Confound Analysis.}
77	\label{app:enabling-confound}
78	
79	The scale-dependent layer interaction (\S\ref{sec:method}) shows that the semantic layer achieves only 24\% DR reduction without the grammar layer (Table~\ref{tab:scierc-ablation}).
80	A potential confound is that the semantic layer depends not only on grammar-enforced vocabulary membership but also on structural enforcement for positional awareness: the semantic layer identifies type-bearing positions by pattern-matching the decoded prefix against the JSON schema, which is reliable only when the grammar layer guarantees valid JSON structure.
81	Without grammar enforcement, malformed structure can cause the semantic layer to misidentify type-bearing positions, reducing effective coverage.
82	We quantify this via the semantic-only ablation (Table~\ref{tab:scierc-ablation}, row~3): CF rises from 0.08\% to 2.71\%, indicating that 2.63\,pp of additional violations trace to structural ambiguity.
83	However, the dominant enabling mechanism remains vocabulary membership: the semantic layer's domain/range lookup requires $r_j \in \mathcal{R}$, which only the grammar layer ensures; without it, OOV relation names produce null constraint lookups.
84	The confound reinforces rather than undermines this interaction: both vocabulary and structural contributions of the grammar layer are prerequisites for effective semantic enforcement.
85	
86	%%% CF-DR Trade-off Analysis %%%
87	% exp_ids: cf_fallback_ablation_scierc (CF fallback vs full_s1 baseline)
88	
89	\paragraph{CF-DR Trade-off Analysis.}
90	\label{app:cf-dr-tradeoff}
91	
92	CF violations are the most prominent residual limitation of OntoCoDec under zero-shot decoding (9.90\% on SciERC, up to 12.02\% on Llama DocRED).
93	We treat this honestly: per-relation independent enforcement cannot eliminate CF without trading it against DR.
94	Table~\ref{tab:cf-dr-tradeoff} reports a pilot ablation in which we replace the grammar-first fallback with a CF-priority fallback that forces the entity's registered type when it conflicts with $\sigma(r)$.
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\begin{tabular}{@{}l rrrr@{}}
100	\toprule
101	\textbf{Configuration} & \textbf{DR\,(\%)} & \textbf{CF\,(\%)} & \textbf{DR+CF} & \textbf{$f_{\text{gf}}$\,(\%)} \\
102	\midrule
103	S1 (baseline) & 0.93 & 9.90 & 10.83 & --- \\
104	CF fallback        & 14.78 & 0.04 & 14.82 & 36.64 \\
105	\midrule
106	$\Delta$ & $+$13.85 & $-$9.86 & $+$3.99 & --- \\
107	\bottomrule
108	\end{tabular}
109	\caption{CF-DR trade-off pilot on SciERC (Qwen3-8B, 551 documents; \texttt{w1\_cf\_fallback\_scierc\_pilot}). CF fallback eliminates CF but re-routes violations to DR, increasing total violations (DR+CF) by 3.99\,pp. $f_{\text{gf}}$: token-level grammar-first fallback rate at type-bearing positions (includes continuation tokens of multi-token type names; first-token position fallback rate is 0.46\% for SciERC Qwen; \S\ref{sec:greedy-limitation}).}
110	\label{tab:cf-dr-tradeoff}
111	\end{table}
112	
113	The CF fallback variant nearly eliminates CF (9.90\%\,$\to$\,0.04\%, $-$9.86\,pp) but at the cost of a 15.9$\times$ increase in DR (0.93\%\,$\to$\,14.78\%, $+$13.85\,pp).
114	% exp_id: w1_cf_fallback_scierc_pilot: DR=0.1478, CF=0.0004, f_gf=0.3664
115	This is not a net improvement: total violations (DR+CF) rise from 10.83\% to 14.82\% ($+$3.99\,pp), so the change \emph{re-routes} violations rather than reducing them.
116	The mechanism is mechanical: each token position with conflicting masks must commit to one violation type; when the CF fallback forces the system to emit the entity's registered type even though it lies outside $\sigma(r)$, the resulting triple satisfies cross-entity consistency but violates domain/range.
117	The token-level grammar-first fallback is triggered at 36.64\% of type-bearing positions (0.46\% at first-token positions; \S\ref{sec:greedy-limitation}); this conflict is structural, not a tunable hyperparameter.
118	
119	We interpret this as a fundamental tension in composable constraint systems with \emph{per-relation independent} enforcement: enforcement priority can be allocated between DR and CF but cannot independently minimize both.
120	Within this design, the current S1 configuration sits near the Pareto frontier of the trade-off, achieving 0.93\% DR at the cost of 9.90\% CF.
121	The direction of the trade-off is consistent beyond SciERC/Qwen3-8B: across all six zero-shot configurations (3 models $\times$ 2 datasets), DR and CF are descriptively inversely associated, with no setting showing both high DR and high CF simultaneously (Table~\ref{tab:cross-model}); however, $n{=}6$ is insufficient for statistical inference on this correlation.
122	The pattern is a structural consequence of per-relation enforcement with grammar-first fallback, not a model- or dataset-specific artifact; we select SciERC/Qwen3-8B for detailed ablation because it exhibits the highest CF (9.90\%), making the trade-off most visible.
123	While the inverse association holds across all configurations, the absolute trade-off magnitude may differ in settings with higher baseline CF, such as Llama DocRED (CF = 12.02\%), where the larger CF headroom could yield proportionally larger shifts under alternative fallback priorities.
124	The CF residual is concentrated in schema ambiguity rather than enforcement failure: 63.3\% of CF violations on SciERC involve the catch-all \textsc{Generic} type (Table~\ref{tab:cf-distribution}), which competes with every content type depending on anaphoric vs.\ referential use, a distinction the per-slot decoder cannot resolve without document-level coreference.
125	
126	Two complementary paths can lower CF without re-routing it to DR.
127	(i)~\emph{Reduce the baseline conflict rate.} Composing OntoCoDec with LoRA fine-tuning on SciERC reduces CF by 88\% relative to the zero-shot setting (9.90\%\,$\to$\,1.18\%; Table~\ref{tab:composability}), because the fine-tuned model's per-slot type predictions agree more often with the entity registry, so the per-relation mask and the registry intersect more frequently.
128	% exp_id: w5_lora_scierc_constrained_eval: CF=0.0118
129	The remaining 1.18\% still traces to \textsc{Generic}$\leftrightarrow$X schema ambiguity, so this path is empirically validated on one dataset and one fine-tuning method but does not generalize without further evidence.
130	(ii)~\emph{Replace per-relation enforcement with global entity-level type consensus during decoding.} This is outside the scope of OntoCoDec's forward-only autoregressive design and is left to future work.
131	
132	%%% Dual-Factor Quantitative Analysis %%%
133	% exp_ids: phase2_scierc_full_s1, phase2_docred_full_s1,
134	%          llama_scierc_full_s1, llama_docred_full_s1
135	
136	\paragraph{Dual-Factor Quantitative Analysis.}
137	\label{app:dual-factor}
138	
139	Figure~\ref{fig:dual-factor-scatter} plots residual DR against the product $\bar{\kappa} \times \text{RV}_{\text{baseline}}$ for model$\times$dataset configurations.
140	For \emph{calibrated} models (Qwen3-8B, Llama-3.1-8B; unconstrained ET${<}$3\% on both datasets), a linear fit yields $y = 0.366x - 0.138$ with $R^2 = 0.886$ ($n{=}4$, $F(1,2) = 15.54$, $p \approx 0.058$); with only four data points (df $= 2$) and $p > 0.05$, this constitutes a descriptive characterization rather than a confirmatory statistical test.
141	The strong fit supports the dual-factor pattern from \S\ref{sec:composition}: residual DR is governed by the product of schema tightness and baseline violation rate.
142	Mistral-7B (unconstrained ET${=}$7.58\% on DocRED) deviates from this pattern: its residual DR on DocRED (33.21\%) substantially exceeds the linear prediction. When model calibration is insufficient (ET${>}$5\% on either dataset), residual DR is dominated by entity misclassification rather than constraint-search failure.
143	This motivates a principled exclusion criterion: models with unconstrained ET${>}$5\% on either dataset fall outside the regime where the tightness$\times$RV product is the primary DR driver.
144	The two DocRED points (high $\bar{\kappa}{=}0.842$) separate cleanly from the two SciERC points (low $\bar{\kappa}{=}0.333$), and within each dataset the model with higher baseline RV shows higher residual DR.
145	
146	% Dual-factor scatter moved to main text (Figure~\ref{fig:dual-factor-scatter}).
147	
148	%%% Dataset-Dependent F1 Impact (moved from §7) %%%
149	% exp_ids: d012_bootstrap_ci (DocRED +0.49pp p<0.001, SciERC +0.13pp p=0.58),
150	%          phase0_docred_unconstrained (RV=29.66%), phase0_scierc_unconstrained (RV=1.39%)
151	
152	\paragraph{Dataset-Dependent F1 Impact.}
153	The divergence in F1 significance between DocRED ($+$0.49\,pp, $p < 0.001$) and SciERC ($+$0.13\,pp, $p = 0.58$) traces to a single mechanism: grammar-layer elimination of out-of-vocabulary relation names.
154	DocRED's baseline RV of 29.66\% produces 5{,}189 OOV predictions counted as false positives; eliminating them yields a significant precision gain.
155	SciERC's baseline RV is only 1.39\% (24 OOV predictions), too few to produce a detectable F1 effect.
156	Llama-3.1-8B's lower baseline RV (16.03\%) yields a smaller but directionally consistent improvement ($+$0.29\,pp vs.\ $+$0.49\,pp); F1 gain magnitude is proportional to baseline OOV rate.
157	% exp_ids: phase0_docred_unconstrained, phase0_scierc_unconstrained
158	% exp_ids: llama_docred_unconstrained (RV=16.03%), llama_docred_full_s1 (R-F1 delta=+0.29pp)
159	
160	%%% Bootstrap CIs and Effect Sizes %%%
161	% exp_ids: bootstrap_ci_ft_composability, r12_table2_bootstrap_ci
162	
163	\paragraph{Bootstrap Confidence Intervals and Effect Sizes.}
164	\label{app:bootstrap-effect-sizes}
165	
166	Table~\ref{tab:bootstrap-effect-sizes} reports per-configuration bootstrap CIs and Cohen's $d$ effect sizes (10{,}000 iterations, document-level resampling, seed=42) for the fine-tuning composability results (Table~\ref{tab:composability}).
167	After Bonferroni correction for $k{=}4$ comparisons ($\alpha_{\text{adj}}{=}0.0125$), no R-F1 difference reaches significance; all R-F1 effect sizes are negligible to small ($|d| \leq 0.37$; Cohen, 1988).
168	Per-configuration corrected $p$-values: Qwen3-8B/SciERC $p_B{=}1.00$, Qwen3-8B/DocRED $p_B{=}0.224$, Llama-3.1-8B/SciERC $p_B{=}1.00$, Llama-3.1-8B/DocRED $p_B{=}1.00$.
169	Constraint enforcement thus preserves extraction quality while achieving large, highly significant reductions in domain-range violations ($|d| \geq 3.0$, all $p_{\text{Bonf}} < 0.005$).
170	
171	\begin{table}[t]
172	\centering
173	\small
174	\setlength{\tabcolsep}{3pt}
175	\resizebox{\columnwidth}{!}{%
176	\begin{tabular}{@{}ll rrrr@{}}
177	\toprule
178	\textbf{Model} & \textbf{Dataset} & $\Delta$\textbf{(pp)} & \textbf{95\% CI} & $p$ & $d$ \\
179	\midrule
180	\multicolumn{6}{@{}l}{\textbf{R-F1 difference (S1 $-$ unconstrained):}} \\
181	Qwen3-8B & SciERC & $-$0.10 & [$-$0.30, 0.00] & .726 & $-$0.05 \\
182	Qwen3-8B & DocRED & $-$0.31 & [$-$0.69, $+$0.01] & .056 & $-$0.37 \\
183	Llama-3.1-8B & SciERC & $+$0.02 & [0.00, $+$0.07] & .736 & $+$0.01 \\
184	Llama-3.1-8B & DocRED & $+$0.06 & [$-$0.11, $+$0.25] & .535 & $+$0.07 \\
185	\midrule
186	\multicolumn{6}{@{}l}{\textbf{DR\% reduction:}} \\
187	Qwen3-8B & SciERC & $-$1.95 & [$-$2.87, $-$1.11] & $<$.001 & $-$6.15 \\
188	Qwen3-8B & DocRED & $-$0.75 & [$-$1.07, $-$0.48] & $<$.001 & $-$7.00 \\
189	Llama-3.1-8B & SciERC & $-$1.02 & [$-$1.98, $-$0.29] & $<$.001 & $-$3.17 \\
190	Llama-3.1-8B & DocRED & $-$0.29 & [$-$0.53, $-$0.10] & $<$.001 & $-$3.02 \\
191	\bottomrule
192	\end{tabular}}
193	\caption{Bootstrap CIs and Cohen's $d$ for Table~\ref{tab:composability} (10{,}000 iterations, document-level resampling, seed=42).
194	$d$: Cohen's $d$ from pooled bootstrap SD.
195	Top: R-F1 (S1 $-$ unconstrained); no comparison significant after Bonferroni correction ($k{=}4$, $\alpha_{\text{adj}}{=}0.0125$); $|d| \leq 0.37$ (negligible--small).
196	Bottom: DR\% reduction; all $p_{\text{Bonf}} < 0.005$, $|d| \geq 3.0$ (large).}
197	\label{tab:bootstrap-effect-sizes}
198	\end{table}
199	
200	%%% Paragraph 1: Low F1 Practical Significance %%%
201	% exp_ids: phase2_scierc_full_s1 (R-F1=8.36%), phase2_docred_full_s1 (R-F1=8.23%),
202	%          phase0_scierc_unconstrained (DR=15.37%), phase2_docred_unconstrained (DR=18.46%)
203	
204	\paragraph{Practical Significance of Zero-Shot F1.}
205	Our reported relation F1 of approximately 8\% on both SciERC and DocRED reflects the inherent difficulty of zero-shot closed IE, where the model receives no task-specific training examples.
206	For reference, supervised state-of-the-art systems on SciERC achieve approximately 49--53\% relation F1 with full training data~\citep{zhong2021frustratingly,ye2022packed}.
207	Constraint enforcement operates largely independently of the extraction model's intrinsic capability: it restricts the output space to ontologically valid triples regardless of the underlying model's accuracy.
208	Even after LoRA fine-tuning, residual DR of 1--2\% persists on tight-constraint relations (Table~\ref{tab:composability}); constraints remain necessary at deployment-grade quality.
209	% exp_ids: w5_lora_scierc_unconstrained_eval, w5_llama_lora_scierc_unconstrained_eval
210	In our evaluation, F1 serves as a \emph{control variable} verifying that constraint enforcement does not degrade extraction quality, not as an optimization target.
211	The contribution of this work is the constraint enforcement method itself; the zero-shot setting stress-tests constraint robustness under maximum model uncertainty, while composability with fine-tuning (\S\ref{sec:composability}) validates practical deployment value.
212	
213	%%% Paragraph 4: Decoding-Time vs. Post-Hoc Enforcement %%%
214	% exp_ids: posthoc_filtering_baseline, phase2_scierc_full_s1 (R-F1=8.36%),
215	%          phase2_docred_full_s1 (R-F1=8.23%, ET=0%)
216	
217	\paragraph{Decoding-Time vs.\ Post-Hoc Enforcement.}
218	Post-hoc filtering (generating triples without constraints, then removing schema-violating predictions) yields higher precision and consequently higher F1 than OntoCoDec on both datasets (SciERC 8.63 vs.\ 8.36; DocRED 9.61 vs.\ 8.23).
219	% posthoc: SciERC F1=8.63, DocRED F1=9.61; OntoCoDec: SciERC R-F1=8.36, DocRED R-F1=8.23
220	However, this precision gain comes at substantial cost.
221	On DocRED, post-hoc filtering discards 48.1\% of all predicted triples, including 127 true positives (11.2\% of correct predictions); recall drops from 9.46\% to 8.40\%.
222	% posthoc_docred: rejection=48.1%, tp_lost=127/1137, R: 9.46→8.40
223	Entity type violations remain unresolved (ET\,=\,2.47\% vs.\ OntoCoDec's 0\%), as filtering targets only domain/range and vocabulary violations.
224	% posthoc_docred: ET_residual=2.47%; phase2_docred_full_s1: ET=0%
225	OntoCoDec's decoding-time approach avoids this information loss by guiding generation toward compliant outputs rather than discarding non-compliant ones, preserving both recall and entity type validity.
226	The two strategies are complementary: post-hoc filtering can serve as an additional safety net for residual violations that decoding-time enforcement does not fully resolve.
227	
228	%%% CF Violation Distribution %%%
229	% exp_ids: phase2_scierc_full_s1 (CF=245), llama_scierc_full_s1 (CF=162),
230	%          phase2_docred_full_s1 (CF=2670), llama_docred_full_s1 (CF=3824)
231	
232	\paragraph{Cross-Field Violation Distribution.}
233	\label{app:cf-distribution}
234	
235	Table~\ref{tab:cf-distribution} reports the complete distribution of conflicting-type pairs for SciERC zero-shot S1 (248 CF violations across 245 unique entity-document pairs; no mention triggered $\geq$3 types).
236	Conflicts involving the \textsc{Generic} type account for 63.3\% (155/245) of all violations.
237	\textsc{Generic} is SciERC's anaphoric/placeholder label (``this approach'', ``the method''), which competes with every content type depending on whether the mention is used anaphorically or referentially, a distinction the per-slot constrained decoder cannot resolve without document-level coreference.
238	
239	The pattern generalizes across models and datasets: on Llama-3.1-8B SciERC, \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} remains the top pair (53/162, 32.7\%); on DocRED, the analogous catch-all type \textsc{MISC} drives 76.6\% of Qwen's CF violations.
240	Under unconstrained decoding, CF rates collapse to $\leq$1\% on both datasets; CF violations are a side-effect of per-slot type commitment rather than a model deficiency.
241	
242	\begin{table}[t]
243	\centering
244	\small
245	\begin{tabular}{@{}lr r@{}}
246	\toprule
247	\textbf{Conflicting Type Pair} & \textbf{Count} & \textbf{\%} \\
248	\midrule
249	Generic $\leftrightarrow$ OtherScientificTerm & 85 & 34.7 \\
250	Generic $\leftrightarrow$ Material & 35 & 14.3 \\
251	Generic $\leftrightarrow$ Metric & 30 & 12.2 \\
252	Method $\leftrightarrow$ Task & 20 & 8.2 \\
253	Material $\leftrightarrow$ Method & 17 & 6.9 \\
254	OtherScientificTerm $\leftrightarrow$ Task & 12 & 4.9 \\
255	\midrule
256	10 further pairs (each $\leq$3.3\%) & 46 & 18.8 \\
257	\midrule
258	\textbf{Total} & \textbf{245} & 100.0 \\
259	\bottomrule
260	\end{tabular}
261	\caption{CF violation distribution on SciERC zero-shot S1 (Qwen3-8B, 551 documents).
262	All 245 unique entity-document pairs involve pairwise conflicts.
263	Conflicts involving \textsc{Generic} account for 63.3\%.}
264	\label{tab:cf-distribution}
265	\end{table}
266	
267	%%% Cascade Error Analysis %%%
268	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248), w5_lora_scierc_full_s1_eval (FT: CF=22)
269	
270	\paragraph{Cascade Error Analysis.}
271	\label{app:cascade-analysis}
272	
273	Table~\ref{tab:cascade-breakdown} decomposes zero-shot CF violations by source mechanism.
274	The dominant source is hallucinated entities (58.1\%): the model generates entity names absent from the input document, and the entity registry assigns a type based on the first occurrence that may conflict with a subsequent valid entity sharing the same surface form.
275	True cascade errors---where first-seen type registration for a \emph{real} entity locks an incorrect type that blocks a subsequent valid assignment---account for only 7.3\% (18/248).
276	Correct type locks (first-seen type is correct and prevents an incorrect subsequent assignment) are 2.5$\times$ more frequent (18.1\%, 45/248), indicating that the first-seen registration mechanism provides a net benefit for type consistency.
277	
278	Under fine-tuning (22 CF violations, 20 documents), cascade errors are completely eliminated (0/22): LoRA training calibrates entity typing sufficiently that first-seen registrations are consistently correct.
279	This confirms that cascade errors are a model calibration issue exposed by the constraint mechanism, not an inherent deficiency of first-seen registration.
280	
281	\begin{table}[h]
282	\centering
283	\small
284	\begin{tabular}{@{}l rr@{}}
285	\toprule
286	\textbf{CF Source Category} & \textbf{Count} & \textbf{\%} \\
287	\midrule
288	Hallucinated entity & 144 & 58.1 \\
289	Correct type lock & 45 & 18.1 \\
290	True cascade error & 18 & 7.3 \\
291	Other / ambiguous & 41 & 16.5 \\
292	\midrule
293	\textbf{Total} & \textbf{248} & 100.0 \\
294	\bottomrule
295	\end{tabular}
296	\caption{CF violation source breakdown on SciERC zero-shot S1 (Qwen3-8B, 551 documents; exp\_id: phase2\_scierc\_full\_s1).
297	``Hallucinated entity'': generated entity absent from input.
298	``True cascade error'': first-seen lock on incorrect type blocks valid subsequent assignment.
299	``Correct type lock'': first-seen type correct, prevents incorrect subsequent type.
300	Under fine-tuning, cascade errors are completely eliminated (0/22 CF violations; exp\_id: w5\_lora\_scierc\_full\_s1\_eval).}
301	\label{tab:cascade-breakdown}
302	\end{table}
303	
304	%%% Per-Relation DR Elimination under Fine-Tuning %%%
305	% exp_ids: lora_scierc_unconstrained, lora_scierc_full_s1
306	
307	\paragraph{Per-Relation DR Elimination under Fine-Tuning.}
308	\label{app:lora-per-relation}
309	
310	Table~\ref{tab:lora-per-relation} presents the per-relation breakdown of DR elimination when OntoCoDec is composed with LoRA fine-tuning on SciERC.
311	Fine-tuning alone eliminates DR on four of seven relations but leaves non-zero violations on the three tightest-constraint relations: \textsc{Evaluate-for} ($\kappa{=}0.361$, 13.13\%), \textsc{Part-of} ($\kappa{=}0.417$, 5.77\%), and \textsc{Compare} ($\kappa{=}0.528$, 5.00\%).
312	Adding OntoCoDec constraints eliminates all remaining violations across all relations.
313	One \textsc{Evaluate-for} triple (99\,$\to$\,98) is redirected to \textsc{Used-for} (634\,$\to$\,635) by token-level masking: the head entity's registered type falls outside \textsc{Evaluate-for}'s domain, and the semantic mask steers generation to the nearest valid relation.
314	
315	\begin{table}[t]
316	\centering
317	\small
318	\begin{tabular}{@{}l r rr rr@{}}
319	\toprule
320	& & \multicolumn{2}{c}{\textbf{LoRA Unconstr.}} & \multicolumn{2}{c}{\textbf{LoRA + S1}} \\
321	\cmidrule(lr){3-4} \cmidrule(l){5-6}
322	\textbf{Relation} & $\kappa$ & DR\,(\%) & $n$ & DR\,(\%) & $n$ \\
323	\midrule
324	Evaluate-for & 0.361 & 13.13 & 99 & \textbf{0} & 98 \\
325	Part-of      & 0.417 & 5.77  & 52 & \textbf{0} & 52 \\
326	Compare      & 0.528 & 5.00  & 40 & \textbf{0} & 40 \\
327	Conjunction  & 0.306 & 1.31  & 153 & \textbf{0} & 153 \\
328	Feature-of   & 0.278 & 1.35  & 74 & \textbf{0} & 74 \\
329	Used-for     & 0.028 & 0.16  & 634 & \textbf{0} & 635 \\
330	Hyponym-of   & 0.417 & 0     & --- & \textbf{0} & --- \\
331	\bottomrule
332	\end{tabular}
333	\caption{Per-relation DR elimination on SciERC with LoRA fine-tuning (Qwen3-8B).
334	$\kappa$: constraint tightness; $n$: predicted triple count.
335	Used-for gains one triple from Evaluate-for redirection.}
336	\label{tab:lora-per-relation}
337	\end{table}
338	
339	%%% Fine-Tuned Four-Way Ablation %%%
340	% exp_ids: w5_lora_scierc_*, w5_llama_lora_scierc_*, w5_qwen_docred_*, w5_llama_docred_*, w8_*
341	
342	\paragraph{Fine-Tuned Four-Way Ablation.}
343	\label{app:ft-ablation}
344	
345	Table~\ref{tab:ft-ablation} presents the four-way constraint ablation on fine-tuned models across both datasets, isolating each layer's contribution when the base model has already internalized schema knowledge.
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\setlength{\tabcolsep}{3pt}
351	\resizebox{\columnwidth}{!}{%
352	\begin{tabular}{@{}lll rrrrr rr@{}}
353	\toprule
354	\textbf{Dataset} & \textbf{Model} & \textbf{Mode} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{PF} & \textbf{E-F1\,$\uparrow$} & \textbf{R-F1\,$\uparrow$} \\
355	\midrule
356	\multirow{8}{*}{SciERC}
357	  & \multirow{4}{*}{Qwen3-8B}
358	    & Unconstrained & 1.95 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
359	  & & Grammar       & 1.90 & 0.00 & 0.00 & 0.00 & 0.00 & 67.05 & 43.86 \\
360	  & & Semantic      & 0.60 & 0.00 & 0.00 & 0.18 & 0.00 & 67.05 & 43.69 \\
361	  & & S1       & \textbf{0}    & 0.00 & 0.00 & 1.18 & 0.00 & 67.05 & 43.77 \\
362	  \cmidrule(l){2-10}
363	  & \multirow{4}{*}{Llama-3.1-8B}
364	    & Unconstrained & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
365	  & & Grammar       & 1.11 & 0.00 & 0.00 & 0.00 & 0.00 & 67.76 & 45.45 \\
366	  & & Semantic      & 0.65 & 0.00 & 0.00 & 0.10 & 0.00 & 67.76 & 45.47 \\
367	  & & S1       & \textbf{0.09} & 0.00 & 0.00 & 0.46 & 0.00 & 67.76 & 45.47 \\
368	\midrule
369	\multirow{8}{*}{DocRED}
370	  & \multirow{4}{*}{Qwen3-8B}
371	    & Unconstrained & 0.76 & 0.27 & 0.00 & 0.12 & 7.11 & 82.15 & 40.86 \\
372	  & & Grammar       & 0.61 & 0.00 & 0.00 & 0.11 & 7.01 & 82.19 & 40.85 \\
373	  & & Semantic      & 0.19 & 0.23 & 0.00 & 0.27 & 7.52 & 82.15 & 40.85 \\
374	  & & S1       & \textbf{0.01} & 0.00 & 0.00 & 0.41 & 8.52 & 81.43 & 40.56 \\
375	  \cmidrule(l){2-10}
376	  & \multirow{4}{*}{Llama-3.1-8B}
377	    & Unconstrained & 0.49 & 0.15 & 0.00 & 0.08 & 2.30 & 83.93 & 43.72 \\
378	  & & Grammar       & 0.51 & 0.00 & 0.00 & 0.12 & 2.30 & 84.04 & 43.72 \\
379	  & & Semantic      & 0.48 & 0.15 & 0.00 & 0.16 & 2.40 & 84.02 & 43.85 \\
380	  & & S1       & \textbf{0.21} & 0.00 & 0.00 & 0.21 & 2.51 & 83.94 & 43.78 \\
381	\bottomrule
382	\end{tabular}}%
383	\caption{Four-way constraint ablation on fine-tuned models (LoRA, 2 models $\times$ 2 datasets).
384	DR/RV/ET: violation rates (\%) over predicted relations; CF: over predicted entities; PF: parse failure rate (\%); F1 $\times$100.
385	Grammar layer is a no-op post-fine-tuning (DR change $<$0.2\,pp in all 4 settings; RV and ET already 0\% without constraints).
386	Semantic layer is the sole effective DR defense (41--69\% on SciERC, 2--75\% on DocRED); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%).
387	F1 cost is negligible: max $\Delta$R-F1 = $-$0.30\,pp (Qwen DocRED, full vs.\ unconstrained).}
388	\label{tab:ft-ablation}
389	\end{table}
390	
391	The grammar layer is effectively a no-op for fine-tuned models across all four settings: RV and ET are already 0\% without constraints, and grammar-only DR change is $<$0.2\,pp (4/4 settings).
392	The semantic layer is the sole effective DR defense under fine-tuning, independently reducing DR by 41--69\% on SciERC (Qwen $-$69\%, Llama $-$41\%) and 2--75\% on DocRED (Qwen $-$75\%, Llama $-$2\%); the near-zero Llama DocRED reduction reflects a near-floor baseline (DR${=}$0.49\%, 80 violations in 16{,}074 triples), where the semantic layer has minimal room to improve.
393	Adding both layers achieves near-complete elimination (DR\,$\leq$\,0.21\% in all 4 settings): even after fine-tuning, the semantic layer's pair-based enforcement captures violations that training alone cannot eliminate, specifically on tight-constraint relations where the valid type-pair space is small.
394	F1 cost is negligible: the maximum R-F1 decrease across S1 vs.\ unconstrained is $-$0.30\,pp (Qwen DocRED).
395	
396	%%% DocRED Zero-Shot Ablation (moved from main text) %%%
397	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
398	%          phase2_docred_semantic_only, phase2_docred_full_s1
399	
400	\paragraph{DocRED Zero-Shot Ablation.}
401	\label{app:docred-zs-ablation}
402	
403	Table~\ref{tab:docred-ablation} presents the four-way constraint ablation on DocRED under zero-shot decoding, parallel to the SciERC ablation in Table~\ref{tab:scierc-ablation}.
404	
405	\begin{table}[t]
406	\centering
407	\small
408	\setlength{\tabcolsep}{3.6pt}
409	\resizebox{\columnwidth}{!}{%
410	\begin{tabular}{@{}l rrrrrr rr@{}}
411	\toprule
412	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
413	& \multicolumn{2}{c}{\textbf{F1}} \\
414	\cmidrule(lr){2-7} \cmidrule(l){8-9}
415	\textbf{Mode}
416	  & DR\,$\downarrow$ & $\Delta$DR
417	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
418	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
419	\midrule
420	Unconstrained
421	  & 18.46 & ---
422	  & 29.66 & 2.48
423	  & 0.10  & 18.56
424	  & 7.74  & 58.15 \\
425	Grammar
426	  & 26.17 & $\uparrow$42\%
427	  & \textbf{0.03} & \textbf{0}
428	  & 0.07  & 26.24
429	  & \textbf{8.31}  & \textbf{59.38} \\
430	Semantic
431	  & 13.84 & $\downarrow$25\%
432	  & 29.87 & 4.22
433	  & 1.05  & 14.89
434	  & 7.70  & 57.81 \\
435	S1
436	  & \textbf{10.21} & $\downarrow$\textbf{45\%}
437	  & \textbf{0.03} & \textbf{0}
438	  & 2.57  & \textbf{12.78}
439	  & 8.23  & 59.37 \\
440	\bottomrule
441	\end{tabular}}%
442	\caption{Four-way ablation on DocRED (998 documents, Qwen3-8B, zero-shot).
443	$\Delta$DR: relative change vs.\ unconstrained.
444	Tot.\ = DR + CF (total type-violation burden).
445	Best per column in \textbf{bold} (CF excluded; Tot.\ included).
446	F1 $\times$100. Bootstrap significance: R-F1 $+$0.49\,pp ($p < 0.001$).
447	Grammar-only $\uparrow$DR: vocabulary enforcement makes OOV outputs evaluable, exposing latent violations (see \S\ref{sec:docred-results}).}
448	\label{tab:docred-ablation}
449	\end{table}
450	
451	%%% Residual DR Error Analysis (Fine-Tuned) %%%
452	% exp_ids: w5_qwen_docred_*, w5_llama_docred_*, w5_lora_scierc_*, w5_llama_lora_scierc_*
453	
454	\paragraph{Residual DR Error Analysis.}
455	\label{app:residual-dr-analysis}
456	
457	Across all fine-tuned settings (2 models $\times$ 2 datasets $\times$ S1), only 36 domain/range violations remain.
458	Manual inspection reveals four root causes:
459	
460	\begin{enumerate}[nosep,leftmargin=*]
461	\item \emph{Entity type errors} (39\%): the LLM assigns an incorrect entity type (e.g., labeling a geographic entity as \textsc{LOC} when the gold standard requires \textsc{MISC}), causing the semantic mask to permit a domain/range-incompatible relation.
462	\item \emph{Schema coverage gaps} (33\%): the frequency-based constraint table, constructed from training-set co-occurrence statistics, does not cover long-tail type pairs that are ontologically valid but rare. These violations are irreducible by decoding-time constraints alone.
463	\item \emph{Incorrect relation selection} (17\%): the model selects a semantically inappropriate relation whose domain/range constraints are incompatible with the correctly typed entities.
464	\item \emph{Direction reversal} (11\%): the model assigns the correct relation but inverts head/tail roles, placing entities in positions that violate the relation's asymmetric domain/range specification.
465	\end{enumerate}
466	
467	Two dataset-specific patterns emerge.
468	Outside Llama DocRED, all residual violations (3 of 36, spanning Llama SciERC and Qwen DocRED) trace exclusively to schema coverage gaps: the model's entity typing is accurate, and the constraint system has reached its theoretical ceiling given the frequency-based constraint table.
469	On DocRED, Llama-3.1-8B contributes 33 of 36 residual violations (92\%), with entity type errors as the dominant cause (14/33, 42\%).
470	This asymmetry reflects Llama's weaker fine-tuned entity typing on DocRED's larger ontology (96 relations, 6 entity types) compared to Qwen, which achieves near-zero residual.
471	The implication is twofold: (i)~the irreducible floor from schema gaps is small ($\sim$3 violations across 4 settings), so the constraint system operates near its theoretical optimum; (ii)~residual violations from entity typing errors are addressable through stronger base models or improved entity typing modules, without modifying the constraint architecture.
472	
473	%%% Post-Hoc Filtering Comparison (Extended) %%%
474	% exp_ids: posthoc_*_zs, posthoc_*_ft
475	
476	\paragraph{Post-Hoc Filtering: Extended Comparison.}
477	\label{app:posthoc-extended}
478	
479	Table~\ref{tab:posthoc-extended} presents the full comparison across all six zero-shot and four fine-tuned configurations.
480	
481	\begin{table}[t]
482	\centering
483	\small
484	\setlength{\tabcolsep}{3pt}
485	\resizebox{\columnwidth}{!}{%
486	\begin{tabular}{@{}lll rrr l@{}}
487	\toprule
488	\textbf{Setting} & \textbf{Model} & \textbf{Dataset} & \textbf{Reject\%} & \textbf{R-F1$_{\text{ph}}$} & \textbf{R-F1$_{\text{cd}}$} & \textbf{Winner} \\
489	\midrule
490	\multirow{6}{*}{ZS}
491	  & Qwen    & SciERC & 16.8 & 8.63  & 8.36  & ph \\
492	  & Llama   & SciERC & 13.9 & 2.71  & 2.54  & ph \\
493	  & Mistral & SciERC & 20.3 & 3.94  & 3.67  & ph \\
494	  & Qwen    & DocRED & 48.1 & 9.61  & 8.23  & ph \\
495	  & Llama   & DocRED & 42.2 & 7.44  & 6.27  & ph \\
496	  & Mistral & DocRED & \textbf{73.7} & 3.85  & \textbf{5.52} & cd \\
497	\midrule
498	\multirow{4}{*}{FT}
499	  & Qwen    & SciERC & 1.95 & 43.94 & 43.77 & ph \\
500	  & Llama   & SciERC & 1.11 & 45.23 & 45.47 & cd \\
501	  & Qwen    & DocRED & 1.03 & 41.11 & 40.79 & ph \\
502	  & Llama   & DocRED & 0.64 & 43.92 & 43.78 & cd \\
503	\bottomrule
504	\end{tabular}}%
505	\caption{Post-hoc filtering (ph) vs.\ constrained decoding (cd).
506	In zero-shot settings, post-hoc F1 is higher in 5/6 groups (precision-dominated), but constrained decoding preserves higher recall in all 6/6 groups.
507	At reject rate $>$70\% (Mistral DocRED), post-hoc F1 collapses below constrained.
508	Under fine-tuning, rejection rates drop to 0.6--2.0\% and the two strategies are equivalent ($\Delta \leq 0.55$\,pp; each wins two groups).
509	F1 $\times$100.}
510	\label{tab:posthoc-extended}
511	\end{table}
512	
513	The crossover point occurs when post-hoc rejection exceeds $\sim$70\%: Mistral DocRED rejects 73.7\% of predicted triples, discarding enough true positives that constrained decoding's recall advantage dominates ($+$1.67\,pp).
514	OntoCoDec's advantage thus scales with violation severity: precisely when constraints are most needed, post-hoc filtering is most destructive.
515	Under fine-tuning, both strategies converge because few violations remain to filter or constrain ($\Delta \leq 0.55$\,pp across all four FT groups, with each strategy winning two).
516	
517	%%% Zero-Shot Runtime Profiling %%%
518	
519	\paragraph{Zero-Shot Runtime Profiling.}
520	\label{app:runtime}
521	
522	On SciERC (Qwen3-8B, zero-shot greedy, NVIDIA RTX PRO 6000 Blackwell Server Edition), unconstrained inference averages 4.163\,s/doc and S1 constrained decoding averages 4.710\,s/doc ($+$13.1\% overhead).
523	On DocRED (same configuration), relative overhead is lower due to amortization: the fixed per-token constraint cost is spread over longer generation sequences.
524	XGrammar automaton compilation takes 0.044\,s; the full constraint pipeline (schema parsing, JSON Schema generation, grammar compilation) takes 0.33\,s on SciERC (Table~\ref{tab:scalability}), amortized to zero over the evaluation set.
525	
526	% exp_id: p8c_ft_scierc_latency — Reviewer Report #23 verified
527	\paragraph{Fine-Tuned Latency Profiling.}
528	\label{app:ft-latency}
529	Under LoRA fine-tuning (same hardware and dataset), unconstrained inference averages 2.612\,s/doc and S1 constrained decoding averages 2.873\,s/doc ($+$10.0\% overhead, $n{=}551$).
530	Fine-tuned models generate shorter, more structured outputs than zero-shot models (2.612\,s vs.\ 4.163\,s/doc unconstrained); absolute generation time drops by 37\%.
531	The relative overhead ($+$10.0\%) is slightly lower than zero-shot ($+$13.1\%), consistent with shorter sequences requiring fewer constraint checks per document.
532	
533	%%% Fuzzy Relation Matching %%%
534	
535	\paragraph{Relation Matching Protocol.}
536	\label{app:fuzzy-matching}
537	Relation F1 evaluation uses fuzzy normalization to handle model-specific formatting variants (e.g., underscores vs.\ spaces, abbreviations).
538	A predicted relation $r_p$ matches gold relation $r_g$ if: (1)~exact string match after case-insensitive normalization, or (2)~token overlap $>$80\% \emph{and} edit distance $\leq 2$.
539	This protocol affects primarily Mistral, which produces underscore-separated variants (e.g., ``head\_of\_government'' for ``head of government'').
540	On Mistral DocRED, fuzzy matching contributes 98 additional TPs ($+$0.84\,pp R-F1; strict R-F1\,=\,3.50\% vs.\ fuzzy 4.34\%).
541	For Qwen and Llama under grammar constraints, the grammar layer enforces exact relation names, making fuzzy matching irrelevant (0 additional matches).
542	All F1 figures in the main text use fuzzy normalization consistently across all models and conditions.
543	
544	%%% Per-Relation Violation Landscape %%%
545	
546	\paragraph{Per-Relation Violation Landscape.}
547	\label{app:per-relation-landscape}
548	
549	Table~\ref{tab:prompt_comparison} compares violation rates under unconstrained and schema-informed prompting.
550	Figure~\ref{fig:per_relation_dr} shows the per-relation DR distribution on SciERC.
551	
552	\begin{table}[t]
553	\centering
554	\small
555	\caption{Violation rates (\%) under unconstrained and schema-informed prompting (Qwen3-8B, zero-shot).}
556	\label{tab:prompt_comparison}
557	\resizebox{\columnwidth}{!}{%
558	\begin{tabular}{ll cccc}
559	\toprule
560	Dataset & Prompt & DR$\downarrow$ & RV$\downarrow$ & ET$\downarrow$ & CF$\downarrow$ \\
561	\midrule
562	\multirow{2}{*}{SciERC} & Unconstrained & 15.4 & 1.4 & 0.4 & 0.1 \\
563	 & Schema-informed & 5.8 & 0.3 & \textbf{0.0} & --- \\
564	\midrule
565	\multirow{2}{*}{DocRED} & Unconstrained & 18.5 & 29.7 & 2.5 & 0.1 \\
566	 & Schema-informed & 12.8 & 18.4 & 0.2 & 0.2 \\
567	\bottomrule
568	\end{tabular}}
569	\end{table}
570	
571	%%% WikiEvents Extended %%%
572	
573	\paragraph{WikiEvents Dataset Details.}
574	\label{app:wikievents}
575	WikiEvents~\cite{li2021document} is a document-level event argument extraction benchmark grounded in the DARPA KAIROS ontology.
576	It defines 56 event types, 80 argument roles, and 27 entity types, with 245 (event\_type, role)$\to$allowed\_entity\_types constraints.
577	The grammar layer targets EV (event vocabulary), RoV (role vocabulary), and ET; the semantic layer enforces AC (argument constraint) via role-conditioned masking, analogous to RE domain/range enforcement.
578	
579	\paragraph{Constraint Tightness in WikiEvents.}
580	\label{app:wikievents-kappa}
581	% Data source: artifacts/w1c_wikievents_kappa_results.md
582	WikiEvents role-level tightness (with $|\mathcal{E}|{=}27$) has mean $\bar{\kappa}{=}0.82$ and median 0.89; 84\% of roles have $\kappa \geq 0.80$ (4 or fewer valid entity types out of 27).
583	The tightness-violation pattern extends to event extraction: roles with $\kappa \geq 0.90$ exhibit the highest AC rate (50\%), compared to 21\% for medium-tightness ($0.80 \leq \kappa < 0.90$) and 30\% for loose ($\kappa < 0.80$) roles; this is consistent with the RE observation that constraint tightness correlates with violation frequency.
584	However, the correlation is modulated by entity type prototypicality: semantically intuitive roles (e.g., Transportation.Vehicle$\to$VEH) show 0\% AC despite $\kappa{=}0.963$, while roles that require rare KAIROS-specific types (e.g., Crime$\to$CRM, Sentence$\to$SEN) show near-100\% AC because LLMs default to common types (PER, ORG).
585	The loose group's elevated rate (30\%) is driven by high-frequency roles such as Attack.Target (126 args, 34\% AC, $\kappa{=}0.59$), where systematic model errors outweigh the permissive constraint space.
586	
587	%%% Lucky Violation Analysis %%%
588	% exp_ids: task_e_lucky_violation_analysis
589	
590	\paragraph{Lucky Violation Analysis.}
591	\label{app:lucky-violations}
592	Table~\ref{tab:lucky-violations} quantifies the recall cost of DR elimination.
593	A ``lucky violation'' is a constraint-removed triple that happens to match a gold label---an ontologically invalid prediction that is nonetheless correct.
594	Across four fine-tuned configurations, lucky violations average 0.24\% of gold triples (range 0.01--0.51\%), confirming that nearly all removed DR violations are false positives.
595	On Llama SciERC, all five lucky violations are recovered as legal type paths under constrained decoding (zero churn): the model finds an ontology-compliant route to the same prediction.
596	
597	\begin{table}[h]
598	\centering
599	\small
600	\resizebox{\columnwidth}{!}{%
601	\begin{tabular}{@{}llrrrr@{}}
602	\toprule
603	\textbf{Model} & \textbf{Dataset} & \textbf{DR (\%)} & \textbf{Lucky} & \textbf{$\Delta$Recall} & \textbf{Churn} \\
604	& & \textbf{unc$\to$con} & \textbf{(\% gold)} & \textbf{(pp)} & \textbf{(\%)} \\
605	\midrule
606	Qwen3-8B  & SciERC & 1.95$\to$0    & 4 (0.41\%) & $-$0.10 & 0.22 \\
607	Llama-8B  & SciERC & 1.11$\to$0.09 & 5 (0.51\%) & $\pm$0.00 & 0 \\
608	Qwen3-8B  & DocRED & 1.03$\to$0.01 & 1 (0.01\%) & $-$0.84 & 2.05 \\
609	Llama-8B  & DocRED & 0.64$\to$0.21 & 1 (0.01\%) & $-$0.10 & 0.86 \\
610	\midrule
611	\multicolumn{2}{@{}l}{\textit{Average}} & & \textit{0.24\%} & $-$0.26 & 0.78 \\
612	\bottomrule
613	\end{tabular}}
614	\caption{Lucky violation analysis across four LoRA fine-tuned configurations.
615	Lucky: count (and \% of gold triples) of constraint-removed violations matching gold labels.
616	$\Delta$Recall: recall change from unconstrained to constrained.
617	Churn: fraction of gold-matching triples whose predictions change (including recovery via legal type paths).}
618	\label{tab:lucky-violations}
619	\end{table}
620	
621	%%% Trie-Only Baseline %%%
622	% exp_ids: trie_qwen_ft_scierc, trie_qwen_zs_scierc, trie_llama_ft_scierc, trie_llama_zs_scierc
623	
624	\paragraph{Trie-Only Baseline (GCD-Equivalent).}
625	\label{app:trie-baseline}
626	Table~\ref{tab:trie-baseline} isolates the effect of vocabulary membership constraints without JSON structural enforcement.
627	The trie constrains entity type and relation tokens to schema-valid values (achieving ET${=}$0\%, RV${=}$0\% across all configurations), functionally equivalent to GCD's~\cite{geng2023gcd} constrained decoding.
628	However, without grammar-level JSON enforcement, models systematically omit entity type fields (83\% of triples) or produce malformed JSON (0--51\% parse failure), causing DR to rise to 15--96\%---far worse than unconstrained baselines.
629	The effect is most dramatic for Llama-8B LoRA: 50.8\% parse failure causes R-F1 to collapse from 45.47 (OntoCoDec S1) to 19.95, demonstrating that the grammar layer is not merely helpful but a structural prerequisite---vocabulary constraints require JSON scaffolding to reach the positions where they apply.
630	
631	\begin{table}[h]
632	\centering
633	\small
634	\resizebox{\columnwidth}{!}{%
635	\begin{tabular}{@{}ll rrrr rr@{}}
636	\toprule
637	\textbf{Model} & \textbf{Setting}
638	  & \textbf{ET\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{DR\,$\downarrow$} & \textbf{CF}
639	  & \textbf{R-F1\,$\uparrow$} & \textbf{PF\,(\%)} \\
640	\midrule
641	\multirow{2}{*}{Qwen3-8B}
642	  & LoRA  & 0 & 0 & 95.5  & 0.09 & 41.16 & 9.1 \\
643	  & ZS    & 0 & 0 & 29.3  & 0    & 8.64  & 0 \\
644	\multirow{2}{*}{Llama-8B}
645	  & LoRA  & 0 & 0 & 15.2$^\dagger$  & 0    & 19.95 & 50.8 \\
646	  & ZS    & 0 & 0 & 84.4  & 0.36 & 2.90  & 0 \\
647	\midrule
648	\multicolumn{8}{@{}l}{\textit{Comparison with OntoCoDec S1:}} \\
649	\midrule
650	& & \multicolumn{2}{c}{\textbf{S1 DR\,(\%)}} & \textbf{Trie DR\,(\%)} & \multicolumn{2}{c}{\textbf{DR Gap (pp)}} & \\
651	\cmidrule(lr){3-4} \cmidrule(lr){5-5} \cmidrule(lr){6-7}
652	Qwen3-8B  & LoRA  & \multicolumn{2}{c}{0}    & 95.5  & \multicolumn{2}{c}{95.5}  & \\
653	Qwen3-8B  & ZS    & \multicolumn{2}{c}{0.93} & 29.3  & \multicolumn{2}{c}{28.4}  & \\
654	Llama-8B  & LoRA  & \multicolumn{2}{c}{0.09} & 15.2  & \multicolumn{2}{c}{15.1}  & \\
655	Llama-8B  & ZS    & \multicolumn{2}{c}{0.08} & 84.4  & \multicolumn{2}{c}{84.3}  & \\
656	\bottomrule
657	\end{tabular}}
658	\caption{Trie-only baseline (GCD-equivalent, vocabulary membership without JSON grammar) on SciERC.
659	Top: full trie-only metrics (ET/RV/DR/CF: violation rates \%; R-F1 $\times$100; PF: parse failure rate).
660	Trie achieves ET${=}$0\%, RV${=}$0\% but DR rises to 15--96\% because models omit type fields without structural enforcement.
661	Bottom: DR gap between OntoCoDec S1 and trie-only, quantifying the grammar layer's contribution.
662	$^\dagger$50.8\% parse failure rate.}
663	\label{tab:trie-baseline}
664	\end{table}
665	
666	%%% GCD/BoostCD Equivalence Comparison %%%
667	
668	\paragraph{Comparison with Grammar-Based Constrained Decoding.}
669	\label{app:gcd-comparison}
670	
671	The trie-only results above isolate vocabulary constraints in the absence of structural enforcement.
672	Table~\ref{tab:gcd-comparison} places this finding in the broader context of grammar-based constrained decoding methods, comparing the constraint class, enforcement level, and DR reduction achieved by each approach---including OntoCoDec's grammar layer, which is analytically equivalent to GCD-family methods.
673	
674	\begin{table*}[t]
675	\centering
676	\small
677	\begin{tabular}{@{}l l l l l l@{}}
678	\toprule
679	\textbf{Method} & \textbf{Constraint Type} & \textbf{Level} & \textbf{DR Red.} & \textbf{CF} & \textbf{State} \\
680	\midrule
681	GCD~\cite{geng2023gcd} & CFG (JSON schema) & Grammar & ${\sim}$3\% & N/A & Stateless \\
682	BoostCD~\cite{boostcd2025} & CFG + beam rerank & Grammar & ${\sim}$3\%$^\dagger$ & N/A & Stateless \\
683	Trie-Only (Tab.~\ref{tab:trie-baseline}) & Prefix trie & Vocab & 0\%$^\ddagger$ & N/A & Stateless \\
684	\midrule
685	vLLM \texttt{guided\_json}~\cite{kwon2023vllm} & JSON Schema & Grammar & ${\sim}$3\%$^\S$ & N/A & Stateless \\
686	\midrule
687	OntoCoDec Grammar & CFG (XGrammar) & Grammar & ${\sim}$3\% & N/A & Stateless \\
688	OntoCoDec S1 & CFG + type constr. & Gram.+Sem. & 94--100\% (FT) & ${\leq}$1.4\% (FT) & Entity reg. \\
689	\bottomrule
690	\end{tabular}
691	\caption{Comparison with grammar-based constrained decoding methods.
692	$^\dagger$Equivalent mechanism; BoostCD adds beam-level reranking but the CFG enforcement is identical.
693	$^\ddagger$Vocabulary-only constraints without JSON structure cause DR to \emph{increase} (15--96\%; Table~\ref{tab:trie-baseline}).
694	$^\S$Experimentally verified: DR${=}$15.26\% vs.\ grammar-only 14.84\% ($\Delta{<}$0.5\,pp; Table~\ref{tab:vllm-verification}).
695	Grammar-only results are analytically equivalent to GCD/BoostCD (same CFG enforcement; \S\ref{sec:related_work}).}
696	\label{tab:gcd-comparison}
697	\end{table*}
698	
699	Our grammar layer implements the same CFG-based token masking as GCD and BoostCD---the mechanisms are formally identical (JSON schema $\to$ pushdown automaton $\to$ per-step allowed token set).
700	Table~\ref{tab:scierc-ablation} row~2 therefore constitutes a direct comparison: grammar-only enforcement achieves RV/ET$\to$0\% but only ${\sim}$3\% DR reduction, identical to what GCD-family methods would achieve on IE tasks.
701	
702	% exp_id: vllm_guided_json_scierc_zs
703	\paragraph{External verification via vLLM.}
704	To confirm this equivalence experimentally, we evaluated vLLM's \texttt{guided\_json} mode~\cite{kwon2023vllm}---an independent CFG enforcement implementation---on SciERC under identical conditions (Qwen3-8B, zero-shot, 551 documents).
705	
706	\begin{table}[h]
707	\centering
708	\small
709	\resizebox{\columnwidth}{!}{%
710	\begin{tabular}{@{}l rrrr r@{}}
711	\toprule
712	\textbf{Method} & \textbf{DR\,$\downarrow$} & \textbf{RV\,$\downarrow$} & \textbf{ET\,$\downarrow$} & \textbf{CF} & \textbf{R-F1\,$\uparrow$} \\
713	\midrule
714	Grammar-Only (XGrammar) & 14.84 & 0 & 0 & 9.90 & 8.23 \\
715	vLLM \texttt{guided\_json} & 15.26 & 0 & 0 & --- & 8.75 \\
716	\midrule
717	$\Delta$ & $+$0.42 & 0 & 0 & --- & $+$0.52 \\
718	\bottomrule
719	\end{tabular}}
720	\caption{GCD-equivalence verification: OntoCoDec grammar-only vs.\ vLLM \texttt{guided\_json} on SciERC (Qwen3-8B, zero-shot, 551 documents). All differences $<$0.5\,pp, confirming that CFG-based approaches---regardless of implementation---leave ${\sim}$15\% DR violations unaddressed.}
721	\label{tab:vllm-verification}
722	\end{table}
723	
724	All metrics differ by $<$0.5\,pp (Table~\ref{tab:vllm-verification}), confirming that any CFG-based constrained decoding tool---whether GCD, BoostCD, or vLLM---enforces the same constraint class and leaves the same ${\sim}$15\% DR gap.
725	The critical gap these methods cannot address is cross-field type consistency (Level~2), which requires the stateful semantic layer that maintains an entity registry across relation slots and enforces per-relation domain/range constraints at each type-bearing position.
726	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90c41da8-090d-4de3-abe3-d07168db98e5",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "cc31f185-8130-41e4-8ea2-9ecefac21c54",
  "sourceToolAssistantUUID": "90c41da8-090d-4de3-abe3-d07168db98e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:42:00.203Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VMrKN6vWjuW3DQaEspc4cK`</summary>

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
  "parentUuid": "cc31f185-8130-41e4-8ea2-9ecefac21c54",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrfVEToVNwXyRAv5taB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "035a124f-64af-4075-9565-7658c4ba0562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HxBrancg45LTeb2d1j9JxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25258,
      "cache_read_input_tokens": 7257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25258,
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

_source line 11 · 2026-05-25T19:42:00.208Z_

<details><summary>↩ Tool result · `toolu_01VMrKN6vWjuW3DQaEspc4cK`</summary>

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
  "parentUuid": "035a124f-64af-4075-9565-7658c4ba0562",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "24406380-b1e8-4078-8d9a-76c45f9f9117",
  "sourceToolAssistantUUID": "035a124f-64af-4075-9565-7658c4ba0562",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:42:00.659Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UA47aDfRuPbrCKKTmGjA51`</summary>

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
  "parentUuid": "24406380-b1e8-4078-8d9a-76c45f9f9117",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrfVEToVNwXyRAv5taB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33e4eba8-4472-419c-a13e-8b92f6b9274d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HxBrancg45LTeb2d1j9JxD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25258,
      "cache_read_input_tokens": 7257,
      "output_tokens": 438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25258
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 438,
          "cache_read_input_tokens": 7257,
          "cache_creation_input_tokens": 25258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25258,
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

_source line 13 · 2026-05-25T19:42:00.669Z_

<details><summary>↩ Tool result · `toolu_01UA47aDfRuPbrCKKTmGjA51`</summary>

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
  "parentUuid": "33e4eba8-4472-419c-a13e-8b92f6b9274d",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "6f45cf87-685c-47d5-853b-31c543166fc6",
  "sourceToolAssistantUUID": "33e4eba8-4472-419c-a13e-8b92f6b9274d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:42:05.661Z_

<details open><summary>🔧 Tool call — Read · `toolu_016d3uxvJiGHy74ZvxzTrG2v`</summary>

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
  "parentUuid": "6f45cf87-685c-47d5-853b-31c543166fc6",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrftA7LmQ6ZpURwzK1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e638616f-c5b2-49d2-98ee-b7b0c27ad641",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014ZGGgBmqc6Hkgr2t4tkc3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 32515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 15 · 2026-05-25T19:42:05.677Z_

<details><summary>↩ Tool result · `toolu_016d3uxvJiGHy74ZvxzTrG2v`</summary>

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
  "parentUuid": "e638616f-c5b2-49d2-98ee-b7b0c27ad641",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "b3fefa6e-e621-4397-b511-2ee67c6aadc7",
  "sourceToolAssistantUUID": "e638616f-c5b2-49d2-98ee-b7b0c27ad641",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:42:06.466Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B1vsHvxhNRqhREG5HwnNwK`</summary>

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
  "parentUuid": "b3fefa6e-e621-4397-b511-2ee67c6aadc7",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrftA7LmQ6ZpURwzK1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1430c242-ac73-4185-a47a-2de9fdf009c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014ZGGgBmqc6Hkgr2t4tkc3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 32515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 17 · 2026-05-25T19:42:06.471Z_

<details><summary>↩ Tool result · `toolu_01B1vsHvxhNRqhREG5HwnNwK`</summary>

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
102	\caption{Beam width vs.\ R-F1 under LoRA fine-tuning. Left: SciERC (Qwen3-8B solid, Llama-3.1-8B dashed; 551 docs). Right: DocRED (Llama-3.1-8B, 200 docs). Bubble area $\propto$ total violation rate (DR+CF+RV); rings mark zero-violation configurations. Star: Pareto-optimal ($k{=}2$).}
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
168	DR = domain/range, CF = cross-field violation rates (\%); PF = parse failure rate (\%); F1 $\times$ 100. ET and RV are 0\% in all rows.}
169	\label{tab:beam-docred-lora}
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{@{}llccccc@{}}
172	\toprule
173	\textbf{Model} & \textbf{Decoding} & DR$\,\downarrow$ & CF$\,\downarrow$ & E-F1$\,\uparrow$ & R-F1$\,\uparrow$ & PF \\
174	\midrule
175	\multirow{2}{*}{Qwen3-8B}
176	  & Greedy  & 0.01 & 0.41 & 81.43 & 40.56 & 8.52 \\
177	  & Beam-4  & \textbf{0} & 0.01 & 84.00 & 44.46 & 2.9 \\
178	\midrule
179	\multirow{2}{*}{Llama-3.1-8B}
180	  & Greedy  & 0.21 & 0.21 & 83.94 & 43.78 & 2.51 \\
181	  & Beam-4  & 0 & \textbf{0} & \textbf{85.23} & \textbf{47.17} & \textbf{1.3} \\
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
221	This further strengthens the beam search deployment recommendation: beam achieves near-zero violations across all four types and renders post-hoc CF resolution unnecessary.
222	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1430c242-ac73-4185-a47a-2de9fdf009c9",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "13490007-ac05-47ca-b913-17f12889a33b",
  "sourceToolAssistantUUID": "1430c242-ac73-4185-a47a-2de9fdf009c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T19:42:06.927Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TrFLkkFDAef3BaHUHrAuwf`</summary>

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
  "parentUuid": "13490007-ac05-47ca-b913-17f12889a33b",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrftA7LmQ6ZpURwzK1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e6ec8c9-2870-4c72-ae66-c6cc40f672b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014ZGGgBmqc6Hkgr2t4tkc3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 32515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 19 · 2026-05-25T19:42:06.932Z_

<details><summary>↩ Tool result · `toolu_01TrFLkkFDAef3BaHUHrAuwf`</summary>

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
12	Training runs on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (98\,GB video RAM (VRAM)).
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
  "parentUuid": "2e6ec8c9-2870-4c72-ae66-c6cc40f672b9",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "50aac0c5-0cc3-4e69-ae36-338f475c0217",
  "sourceToolAssistantUUID": "2e6ec8c9-2870-4c72-ae66-c6cc40f672b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T19:42:07.367Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SoaYKJuye9aeLf16vNx9Hx`</summary>

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
  "parentUuid": "50aac0c5-0cc3-4e69-ae36-338f475c0217",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrftA7LmQ6ZpURwzK1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0ac8493-c448-4c59-8d6e-e1a1b06ce143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014ZGGgBmqc6Hkgr2t4tkc3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 32515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 21 · 2026-05-25T19:42:07.371Z_

<details><summary>↩ Tool result · `toolu_01SoaYKJuye9aeLf16vNx9Hx`</summary>

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
  "parentUuid": "e0ac8493-c448-4c59-8d6e-e1a1b06ce143",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "6fa9859f-8c3e-45ac-bdcb-dd490245c7dc",
  "sourceToolAssistantUUID": "e0ac8493-c448-4c59-8d6e-e1a1b06ce143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T19:42:08.172Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FfDYBsXz6iCXKWpusaqyPw`</summary>

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
  "parentUuid": "6fa9859f-8c3e-45ac-bdcb-dd490245c7dc",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrftA7LmQ6ZpURwzK1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dca0c2c3-53a0-4cf3-bb84-a85b094145dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014ZGGgBmqc6Hkgr2t4tkc3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31975,
      "cache_read_input_tokens": 32515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 23 · 2026-05-25T19:42:08.183Z_

<details><summary>↩ Tool result · `toolu_01FfDYBsXz6iCXKWpusaqyPw`</summary>

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
  "parentUuid": "dca0c2c3-53a0-4cf3-bb84-a85b094145dc",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "b94f28b6-e2e1-4a70-95b2-8b870b6cb53a",
  "sourceToolAssistantUUID": "dca0c2c3-53a0-4cf3-bb84-a85b094145dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T19:42:16.226Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RrJvoWfRpWaBnbfogUZaGx`</summary>

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
  "parentUuid": "b94f28b6-e2e1-4a70-95b2-8b870b6cb53a",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrgS8xp1KEezLuUj8nq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7513b706-501e-4a34-a31e-746d418fea67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NZ7ruSeckrAVLLK6ed2HMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11888,
      "cache_read_input_tokens": 64490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 25 · 2026-05-25T19:42:16.231Z_

<details><summary>↩ Tool result · `toolu_01RrJvoWfRpWaBnbfogUZaGx`</summary>

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
  "parentUuid": "7513b706-501e-4a34-a31e-746d418fea67",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "7575d971-9425-489c-b9c5-715c69d3de5b",
  "sourceToolAssistantUUID": "7513b706-501e-4a34-a31e-746d418fea67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T19:42:16.680Z_

<details open><summary>🔧 Tool call — Read · `toolu_018TpGegQ12AJbBtiCRt7eBD`</summary>

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
  "parentUuid": "7575d971-9425-489c-b9c5-715c69d3de5b",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrgS8xp1KEezLuUj8nq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54bcc985-c97e-4b02-907d-95abdfa83a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NZ7ruSeckrAVLLK6ed2HMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11888,
      "cache_read_input_tokens": 64490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 27 · 2026-05-25T19:42:16.685Z_

<details><summary>↩ Tool result · `toolu_018TpGegQ12AJbBtiCRt7eBD`</summary>

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
  "parentUuid": "54bcc985-c97e-4b02-907d-95abdfa83a78",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "a90e3221-c1a1-442a-8fec-84b1e1874963",
  "sourceToolAssistantUUID": "54bcc985-c97e-4b02-907d-95abdfa83a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T19:42:17.626Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Co2LvALZy3fmfxXLrVqJA6`</summary>

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
  "parentUuid": "a90e3221-c1a1-442a-8fec-84b1e1874963",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrgS8xp1KEezLuUj8nq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9225e5aa-9696-48e6-aeab-c9d781aaa73a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NZ7ruSeckrAVLLK6ed2HMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11888,
      "cache_read_input_tokens": 64490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 29 · 2026-05-25T19:42:17.630Z_

<details><summary>↩ Tool result · `toolu_01Co2LvALZy3fmfxXLrVqJA6`</summary>

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
  "parentUuid": "9225e5aa-9696-48e6-aeab-c9d781aaa73a",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "cc4aebb7-1735-4ec0-9939-1cd79f392f6e",
  "sourceToolAssistantUUID": "9225e5aa-9696-48e6-aeab-c9d781aaa73a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T19:42:18.073Z_

<details open><summary>🔧 Tool call — Read · `toolu_011qjnfBefLiui3rUMbP2Qsx`</summary>

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
  "parentUuid": "cc4aebb7-1735-4ec0-9939-1cd79f392f6e",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrgS8xp1KEezLuUj8nq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0c3ba25-72a9-49ae-a51d-d08cf3823b55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NZ7ruSeckrAVLLK6ed2HMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11888,
      "cache_read_input_tokens": 64490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 31 · 2026-05-25T19:42:18.077Z_

<details><summary>↩ Tool result · `toolu_011qjnfBefLiui3rUMbP2Qsx`</summary>

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
  "parentUuid": "d0c3ba25-72a9-49ae-a51d-d08cf3823b55",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "a07d6d84-d2a5-47f9-9b20-37dff13e0590",
  "sourceToolAssistantUUID": "d0c3ba25-72a9-49ae-a51d-d08cf3823b55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T19:42:18.780Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RgC165e4Kt3wgBw41oNhce`</summary>

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
  "parentUuid": "a07d6d84-d2a5-47f9-9b20-37dff13e0590",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrgS8xp1KEezLuUj8nq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff2ed166-16ec-4589-bd1d-51b4c7c42112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NZ7ruSeckrAVLLK6ed2HMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11888,
      "cache_read_input_tokens": 64490,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11888
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 64490,
          "cache_creation_input_tokens": 11888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11888,
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

_source line 33 · 2026-05-25T19:42:18.783Z_

<details><summary>↩ Tool result · `toolu_01RgC165e4Kt3wgBw41oNhce`</summary>

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
  "parentUuid": "ff2ed166-16ec-4589-bd1d-51b4c7c42112",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "0951a248-b19d-40e9-9889-bdceb1501320",
  "sourceToolAssistantUUID": "ff2ed166-16ec-4589-bd1d-51b4c7c42112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T19:42:22.231Z_

<details open><summary>🔧 Tool call — Read · `toolu_019kvjTxMJjRFzGYHuGwXv7x`</summary>

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
  "parentUuid": "0951a248-b19d-40e9-9889-bdceb1501320",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhDbBGEKxmmxCyEqe7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1a6295f-3ec0-4f4c-b291-dc349596d1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RDcA7w8scz76GVD2V6U3As",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8776,
      "cache_read_input_tokens": 76378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8776,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 35 · 2026-05-25T19:42:22.235Z_

<details><summary>↩ Tool result · `toolu_019kvjTxMJjRFzGYHuGwXv7x`</summary>

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
  "parentUuid": "f1a6295f-3ec0-4f4c-b291-dc349596d1cc",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "14a76176-c06a-46c8-b6da-d79efbfc7415",
  "sourceToolAssistantUUID": "f1a6295f-3ec0-4f4c-b291-dc349596d1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T19:42:23.268Z_

<details open><summary>🔧 Tool call — Read · `toolu_0179Rxuj9QT82LxHhuZe1q5Q`</summary>

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
  "parentUuid": "14a76176-c06a-46c8-b6da-d79efbfc7415",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhDbBGEKxmmxCyEqe7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09dbe42e-b687-46b2-88b1-fe4fffbcea09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RDcA7w8scz76GVD2V6U3As",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8776,
      "cache_read_input_tokens": 76378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8776,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 37 · 2026-05-25T19:42:23.276Z_

<details><summary>↩ Tool result · `toolu_0179Rxuj9QT82LxHhuZe1q5Q`</summary>

```text
1	% Appendix: Constraint Tightness Case Study
2	% Data source: case_study_kappa_dr_dddc01.md (Qwen-2.5-7B zero-shot unconstrained)
3	
4	\section{Constraint Tightness Case Study}
5	\label{app:kappa-case-study}
6	
7	\begin{table*}[h]
8	\centering
9	\small
10	\begin{tabular}{@{}llccc l@{}}
11	\toprule
12	\textbf{Relation} & \textbf{Dataset} & $\kappa$ & \textbf{DR\%} & $n$ & \textbf{Explanation} \\
13	\midrule
14	\multicolumn{6}{@{}l}{\textit{Highest DR violation rate}} \\
15	basin country        & DocRED & .97 & 74.6 &  63 & Sole valid pair \textsc{loc}$\to$\textsc{loc}; head mistyped as \textsc{org}/\textsc{misc} \\
16	product produced     & DocRED & .94 & 67.2 &  61 & Requires \textsc{org} head; model assigns \textsc{loc}/\textsc{per} \\
17	participant of       & DocRED & .81 & 58.6 & 326 & Hallucinated \textsc{event} type; \textsc{per}$\leftrightarrow$event confusion \\
18	\textsc{Compare}     & SciERC & .53 & 42.4 &  66 & Cross-category pairs violate same-type constraint \\
19	\textsc{Feature-of}  & SciERC & .28 & 33.5 & 486 & Fuzzy Task/OtherScientificTerm boundary \\
20	\midrule
21	\multicolumn{6}{@{}l}{\textit{High $\kappa$ with zero violations (DR = 0\%)}} \\
22	lyrics by            & DocRED & .94 &  0.0 &   9 & Unambiguous \textsc{per}$\to$\textsc{misc}; creative roles rarely mistyped \\
23	place of birth       & DocRED & .92 &  0.0 & 157 & Unambiguous \textsc{per}$\to$\textsc{loc}; no type confusion \\
24	place of death       & DocRED & .89 &  0.0 &  60 & Strong \textsc{per}$\to$\textsc{loc} prior; mirrors place of birth \\
25	subsidiary           & DocRED & .86 &  0.0 &   5 & Clear \textsc{org}$\to$\textsc{org} corporate semantics \\
26	father               & DocRED & .81 &  0.0 &  69 & Clear \textsc{per}$\to$\textsc{per} kinship semantics \\
27	\bottomrule
28	\end{tabular}
29	\caption{Per-relation $\kappa$ vs.\ DR violation rate (Qwen3-8B, zero-shot, unconstrained).
30	High $\kappa$ is necessary but not sufficient for high DR: relations with unambiguous entity types (place of birth, $\kappa{=}0.92$) have zero violations, while equally tight relations with confusable types (basin country, $\kappa{=}0.97$) show 74.6\% DR.}
31	\label{tab:kappa-case-study}
32	\end{table*}
33	
34	\paragraph{Analysis.}
35	The case study confirms that violation susceptibility is driven by the interaction of constraint tightness and entity type confusability, not tightness alone.
36	Among DocRED relations with $\kappa \geq 0.81$, those involving semantically unambiguous type pairs (\textsc{per}$\to$\textsc{loc} for kinship/geographic relations) achieve DR${=}$0\%, while those requiring the model to distinguish frequently confused types (\textsc{loc} vs.\ \textsc{org}, \textsc{per} vs.\ \textsc{misc}) show DR${>}$50\%.
37	On SciERC, the highest-DR relation (\textsc{Compare}, 42.4\%) has only moderate $\kappa$ (0.53) but high type confusability across scientific categories.
38	This two-factor pattern motivates constrained decoding: the largest gains come from high-$\kappa$, confusable-type relations where the model's type uncertainty is channeled into valid pairs.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09dbe42e-b687-46b2-88b1-fe4fffbcea09",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "bf509ab2-18d6-44ed-a15e-22d00ccb3f1d",
  "sourceToolAssistantUUID": "09dbe42e-b687-46b2-88b1-fe4fffbcea09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T19:42:24.068Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BLpLaedZdBBXLTbcCtdqDE`</summary>

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
  "parentUuid": "bf509ab2-18d6-44ed-a15e-22d00ccb3f1d",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhDbBGEKxmmxCyEqe7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12db5279-a752-4519-88f5-8093123839a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RDcA7w8scz76GVD2V6U3As",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8776,
      "cache_read_input_tokens": 76378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8776,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 39 · 2026-05-25T19:42:24.075Z_

<details><summary>↩ Tool result · `toolu_01BLpLaedZdBBXLTbcCtdqDE`</summary>

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
56	\resizebox{\columnwidth}{!}{%
57	\begin{tabular}{@{}llrrrr@{}}
58	\toprule
59	& & \multicolumn{2}{c}{\textbf{Unconstrained}} & \multicolumn{2}{c}{\textbf{S1 (Constrained)}} \\
60	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
61	\textbf{Model} & \textbf{Partition} & DR\% & $n$ & DR\% & $n$ \\
62	\midrule
63	\multirow{2}{*}{Llama-3.1-8B}
64	 & High-$\alpha$ (12 rels) & 43.8 &   861 &  3.2 & 1{,}043 \\
65	 & Low-$\alpha$ (84 rels)  & 29.9 & 12{,}809 &  2.5 & 15{,}325 \\
66	\midrule
67	\multirow{2}{*}{Qwen3-8B}
68	 & High-$\alpha$ (12 rels) & 31.9 &   718 & 20.0 & 1{,}119 \\
69	 & Low-$\alpha$ (84 rels)  & 21.2 & 10{,}898 &  9.5 & 16{,}217 \\
70	\bottomrule
71	\end{tabular}}
72	\end{table}
73	
74	Table~\ref{tab:high-kappa-rels} reveals a structural asymmetry between datasets.
75	In SciERC, all seven relations have $\alpha \geq 0.67$: with only 7 relations over $6^2 = 36$ entity type pair slots, extensive overlap is inevitable.
76	For example, the pair (Method, Method) is valid for all 7 relations ($\alpha = 1.0$).
77	In DocRED, 96 relations spread across the same 36 type pair slots yield much lower per-relation ambiguity; only 12 relations exceed $\alpha \geq 0.36$, and these collectively cover just 3.8\% of gold triples.
78	
79	Table~\ref{tab:dr-by-ambiguity} shows the DR impact stratified by ambiguity.
80	On DocRED, high-$\alpha$ relations exhibit substantially higher unconstrained DR (43.8\% for Llama vs.\ 29.9\% for low-$\alpha$), reflecting the inherent difficulty of relations whose valid type pairs are shared by dozens of other relations---the model frequently assigns a type combination that, while valid for \emph{some} relation, violates the constraints of the target relation.
81	Under S1 constraints, Llama reduces both groups to near-parity (3.2\% vs.\ 2.5\%), whereas Qwen retains a 2$\times$ gap (20.0\% vs.\ 9.5\%), indicating that constraint effectiveness on high-ambiguity relations depends on the model's baseline type accuracy.
82	Excluding the 12 high-$\alpha$ relations from the DocRED evaluation changes the overall S1 DR only marginally---from 2.55\% to 2.51\% for Llama and from 10.21\% to 9.53\% for Qwen---confirming that their small gold footprint (3.8\%) limits their aggregate impact despite elevated per-relation rates.
83	On SciERC, where all relations have high $\alpha$, the exclusion analysis is vacuous; yet OntoCoDec still reduces DR from 15.4\% to 0.9\% (Qwen) and from 13.3\% to 0.08\% (Llama), demonstrating that high schema ambiguity does not preclude effective constraint enforcement.
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12db5279-a752-4519-88f5-8093123839a4",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "e7cca98a-1785-487e-8884-4763f8531e41",
  "sourceToolAssistantUUID": "12db5279-a752-4519-88f5-8093123839a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-25T19:42:24.979Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GnPwmfmgK9m4Z4kTTrVr4J`</summary>

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
  "parentUuid": "e7cca98a-1785-487e-8884-4763f8531e41",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhDbBGEKxmmxCyEqe7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a64b29d7-e9ec-4c20-be27-9d8f447418db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RDcA7w8scz76GVD2V6U3As",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8776,
      "cache_read_input_tokens": 76378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8776,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 41 · 2026-05-25T19:42:24.985Z_

<details><summary>↩ Tool result · `toolu_01GnPwmfmgK9m4Z4kTTrVr4J`</summary>

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
  "parentUuid": "a64b29d7-e9ec-4c20-be27-9d8f447418db",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "a4497d11-02c3-4c40-bf11-3c133f5996c6",
  "sourceToolAssistantUUID": "a64b29d7-e9ec-4c20-be27-9d8f447418db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T19:42:25.336Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C2VxD6gREbPGXMR6L3JU7d`</summary>

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
  "parentUuid": "a4497d11-02c3-4c40-bf11-3c133f5996c6",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhDbBGEKxmmxCyEqe7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66bd4365-2506-4f2f-b77e-404f66d9b478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RDcA7w8scz76GVD2V6U3As",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8776,
      "cache_read_input_tokens": 76378,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 425,
          "cache_read_input_tokens": 76378,
          "cache_creation_input_tokens": 8776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8776,
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

_source line 43 · 2026-05-25T19:42:25.339Z_

<details><summary>↩ Tool result · `toolu_01C2VxD6gREbPGXMR6L3JU7d`</summary>

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
  "parentUuid": "66bd4365-2506-4f2f-b77e-404f66d9b478",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "93156dca-60bc-4400-93c7-ccedf934c237",
  "sourceToolAssistantUUID": "66bd4365-2506-4f2f-b77e-404f66d9b478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T19:42:29.193Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fh9n6Z74aGuzgxCvkgXsCM`</summary>

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
  "parentUuid": "93156dca-60bc-4400-93c7-ccedf934c237",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhhbR6pU1DiMkecUfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "441c775e-c54a-4fc7-af47-53c962e79fd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W64aLHgoEmSjS9hS1rkfXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8955,
      "cache_read_input_tokens": 85154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8955,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 45 · 2026-05-25T19:42:29.197Z_

<details><summary>↩ Tool result · `toolu_01Fh9n6Z74aGuzgxCvkgXsCM`</summary>

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
  "parentUuid": "441c775e-c54a-4fc7-af47-53c962e79fd4",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "60d4ebfb-c336-4d9a-95b3-c63dfcd1f104",
  "sourceToolAssistantUUID": "441c775e-c54a-4fc7-af47-53c962e79fd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T19:42:29.641Z_

<details open><summary>🔧 Tool call — Read · `toolu_018cyMrzWwFpSnEZ4T5232KM`</summary>

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
  "parentUuid": "60d4ebfb-c336-4d9a-95b3-c63dfcd1f104",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhhbR6pU1DiMkecUfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "824c5de4-c315-4c93-9343-44d2b8bd5be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W64aLHgoEmSjS9hS1rkfXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8955,
      "cache_read_input_tokens": 85154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8955,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 47 · 2026-05-25T19:42:29.645Z_

<details><summary>↩ Tool result · `toolu_018cyMrzWwFpSnEZ4T5232KM`</summary>

```text
1	% Appendix: Zero-Shot Cross-Model and Cross-Dataset Details
2	% Moved from main text §5.2--§5.3 per reviewer guidance to focus main text on fine-tuned results.
3	
4	\section{Zero-Shot Cross-Model Validation}
5	\label{app:cross-model-zs}
6	
7	Table~\ref{tab:cross-model} reports the full cross-model zero-shot violation breakdown.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\setlength{\tabcolsep}{3.4pt}
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{@{}ll rrrr r@{}}
15	\toprule
16	& & \multicolumn{4}{c}{\textbf{Violation Rates (\%)}}
17	& \textbf{R-F1} \\
18	\cmidrule(lr){3-6} \cmidrule(l){7-7}
19	\textbf{Dataset} & \textbf{Model}
20	  & DR\,$\downarrow$ & RV\,$\downarrow$ & ET\,$\downarrow$ & CF
21	  & $\uparrow$ \\
22	\midrule
23	\multirow{6}{*}{SciERC}
24	  & Qwen (U)    & 15.37 & 1.39  & 0.40 & 0.08 & 8.23 \\
25	  & Qwen (S1)   &  0.93 & 0     & 0    & 9.90 & 8.36 \\
26	  \cmidrule(l){2-7}
27	  & Llama (U)   & 13.34 & 0.55  & 0    & 0.24 & 2.68 \\
28	  & Llama (S1)  &  0.08 & 0     & 0    & 6.56 & 2.54 \\
29	  \cmidrule(l){2-7}
30	  & Mistral (U) & 56.94 & 0     & 1.50 & 56.87$^\dagger$ & 3.66 \\
31	  & Mistral (S1)& 13.40 & 0     & 0    & 1.27  & 3.67 \\
32	\midrule
33	\multirow{6}{*}{DocRED}
34	  & Qwen (U)    & 18.46 & 29.66 & 2.48 & 0.10 & 7.74 \\
35	  & Qwen (S1)   & 10.21 &  0.03 & 0    & 2.57 & 8.23 \\
36	  \cmidrule(l){2-7}
37	  & Llama (U)   & 26.07 & 16.03 & 0.13 & 0.17 & 5.98 \\
38	  & Llama (S1)  &  2.55 &  0    & 0    & 12.02& 6.27 \\
39	  \cmidrule(l){2-7}
40	  & Mistral (U) & 57.42 & 42.35 & 7.58 & 24.78 & 4.34 \\
41	  & Mistral (S1)& 33.20 &  0    & 0    & 0.19  & 5.52 \\
42	\bottomrule
43	\end{tabular}}%
44	\caption{Three-model zero-shot validation. U: unconstrained; S1: full two-layer.
45	Parse failures: Llama DocRED 9.1\%; others $\leq$1.1\%.
46	$^\dagger$Mistral: poor zero-shot calibration causes pervasive type inconsistencies.
47	F1 $\times$100.}
48	\label{tab:cross-model}
49	\end{table}
50	
51	\paragraph{Cross-model results.}
52	RV and ET reach $\leq$0.03\% for all models on both datasets.
53	DR drops 76--99\% on SciERC and 42--90\% on DocRED; R-F1 improves in 5/6 settings.
54	CF direction depends on calibration: S1 introduces CF for calibrated models (up to 12.02\%) but reduces it for Mistral (56.87\%\,$\to$\,1.27\%); fine-tuning resolves both (\S\ref{sec:composability}).
55	Post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates (Appendix~\ref{app:posthoc-extended}).
56	
57	\paragraph{Cross-dataset validation on DocRED.}
58	\label{sec:docred-results}
59	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
60	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.49\,pp ($p < 0.001$).
61	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
62	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) via \textit{latent violation surfacing}: grammar forces OOV$\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the scale-dependent layer interaction.
63	Fine-tuning reduces residual DR to $\leq$\,0.21\% (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "824c5de4-c315-4c93-9343-44d2b8bd5be8",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "63879266-d087-4b63-bbdb-c03b8a7f9390",
  "sourceToolAssistantUUID": "824c5de4-c315-4c93-9343-44d2b8bd5be8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T19:42:30.607Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TwFy1Ln1GViMKHbnUkE21p`</summary>

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
  "parentUuid": "63879266-d087-4b63-bbdb-c03b8a7f9390",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhhbR6pU1DiMkecUfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50438a25-6fbc-415a-a8aa-e798a06e110a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W64aLHgoEmSjS9hS1rkfXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8955,
      "cache_read_input_tokens": 85154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8955,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 49 · 2026-05-25T19:42:30.613Z_

<details><summary>↩ Tool result · `toolu_01TwFy1Ln1GViMKHbnUkE21p`</summary>

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
  "parentUuid": "50438a25-6fbc-415a-a8aa-e798a06e110a",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "07edb405-d59d-4cea-93af-e0b9163b9ee0",
  "sourceToolAssistantUUID": "50438a25-6fbc-415a-a8aa-e798a06e110a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T19:42:31.499Z_

<details open><summary>🔧 Tool call — Read · `toolu_018igxogS4Ratwe66PTuVvAh`</summary>

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
  "parentUuid": "07edb405-d59d-4cea-93af-e0b9163b9ee0",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhhbR6pU1DiMkecUfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c525a33a-0d16-43ca-aae7-16d213f5d73b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W64aLHgoEmSjS9hS1rkfXG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8955,
      "cache_read_input_tokens": 85154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8955,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 51 · 2026-05-25T19:42:31.503Z_

<details><summary>↩ Tool result · `toolu_018igxogS4Ratwe66PTuVvAh`</summary>

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
14	The two approaches are orthogonal: OntoCoDec can be composed with GoLLIE or similar training-based systems to add runtime enforcement atop learned schema compliance.
15	Direct numerical comparison is methodologically constrained by incompatible evaluation settings (code-style schema encoding vs.\ natural language prompting, different model families and sizes); a controlled comparison would require running both approaches on the same model with matched prompting, which we leave to future work.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c525a33a-0d16-43ca-aae7-16d213f5d73b",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "7dc5b383-7fca-43c7-b632-31141f7efea6",
  "sourceToolAssistantUUID": "c525a33a-0d16-43ca-aae7-16d213f5d73b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T19:42:31.893Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X9p8DZv8kwdRgzfVWCnkhy`</summary>

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
  "parentUuid": "7dc5b383-7fca-43c7-b632-31141f7efea6",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPrhhbR6pU1DiMkecUfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5489ec4-a7fc-43c5-b555-b5c670c00ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W64aLHgoEmSjS9hS1rkfXG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8955,
      "cache_read_input_tokens": 85154,
      "output_tokens": 422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8955
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 422,
          "cache_read_input_tokens": 85154,
          "cache_creation_input_tokens": 8955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8955,
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

_source line 53 · 2026-05-25T19:42:31.896Z_

<details><summary>↩ Tool result · `toolu_01X9p8DZv8kwdRgzfVWCnkhy`</summary>

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
  "parentUuid": "b5489ec4-a7fc-43c5-b555-b5c670c00ad3",
  "isSidechain": true,
  "promptId": "a8890410-35c9-4ceb-8603-c0bc8f1daf5c",
  "agentId": "a16b2408c4cfcd2a6",
  "type": "user",
  "uuid": "0381da55-6886-4871-bb21-24f13da765e5",
  "sourceToolAssistantUUID": "b5489ec4-a7fc-43c5-b555-b5c670c00ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-25T19:48:10.917Z_

Now I have read all 25 appendix files. Let me compile the complete numerical extraction.

---

## appendix_prompts.tex
- "96" — number of Wikidata relation types in DocRED system prompt (line ~36)
- "6" — entity types listed for DocRED (line ~35)

---

## appendix_related_work.tex
- "100×" — speedup of XGrammar over prior CFG-constrained decoding (line ~9)
- "13" — number of IE datasets UIE trains on (line ~55)
- "29K" — number of entity types from Wikidata encoded in KnowCoder (line ~57)
- "50%" — reduction in compilation errors by type-constrained codegen (line ~28)
- "98.8%" — ODKE+ precision across 195 predicates (line ~72)
- "195" — number of predicates in ODKE+ (line ~72)
- "10×" — violation reduction by OntoLogX iterative re-prompting (line ~74)
- "29%" — F1 improvement by constrained inference on CaRB (line ~75)
- "94%" — F1 accuracy@10 achieved by RELATE on ChemProt (line ~77)
- "15.37%" — fraction of generated triples with domain/range violations under unconstrained decoding (line ~83)
- "DR↓94% on SciERC" — DR reduction claim (line ~85)
- "↓45–90% on DocRED" — DR reduction range on DocRED (line ~85)
- "+0.13pp" — F1 gain on SciERC (p=0.58) (line ~98)
- "p=0.58" — p-value for SciERC F1 (line ~98)
- "p<0.001" — p-value for DocRED Qwen R-F1 (line ~98)
- "p=0.013" — p-value for DocRED Llama R-F1 (line ~98)
- "7B–70B" — model scale range evaluated (line ~108)
- "p≤0.013" — significance threshold for DocRED R-F1 gains (line ~109)
- "15.37%→0.93%" — DR reduction on SciERC (line ~98)
- "45–90%" — DR reduction range on DocRED (line ~109)

---

## appendix_discussion.tex
- "100%" — fraction of Qwen3-8B CF violations from registry override (line ~17)
- "5,882" — Llama-3.1-8B grammar-first fallbacks on SciERC (line ~17)
- "10.7" — fallbacks per document on SciERC for Llama (line ~17)
- "57,825" — Llama-3.1-8B grammar-first fallbacks on DocRED (line ~17)
- "63.8" — fallbacks per document on DocRED for Llama (line ~17)
- "2.57%" — Qwen CF on DocRED (line ~18)
- "12.02%" — Llama CF on DocRED (line ~18)
- "36.6%" — token-level fallback rate on SciERC Llama (line ~28)
- "2.87" — average BPE tokens for OtherScientificTerm type name (line ~28)
- "0.04–5.7%" — first-token fallback rate range zero-shot (line ~28)
- "≤0.11%" — fallback rate under fine-tuning (line ~28)
- "4.5%" — registry-consistent fallback rate (line ~31)
- "36.6%" — grammar-first fallback rate (f_gf), SciERC Llama (line ~34)
- "6,237 of 17,024" — mask calls resulting in fallback on SciERC Llama (line ~34)
- "63.4%" — effective semantic constraint coverage on SciERC Llama (line ~34)
- "46 of 54,859" — fallback events on DocRED Qwen (line ~35)
- "0.08%" — f_gf on DocRED Qwen (line ~35)
- "99.9%" — effective coverage on DocRED Qwen (line ~35)
- "2.87" — mask calls per type field for OtherScientificTerm (line ~36)
- "100%" — effective coverage Qwen3-8B on SciERC (line ~39)
- "0.93% vs. Llama's 0.08%" — residual DR comparison (line ~39, note: Qwen vs Llama reversed from main text)
- "24%" — DR reduction by semantic layer without grammar layer (line ~79)
- "2.71%" — CF rises to this under semantic-only ablation (line ~82)
- "0.08%" — CF without semantic-only ablation (line ~82)
- "2.63pp" — additional violations from structural ambiguity (line ~82)
- "9.90%" — CF on SciERC zero-shot (line ~92)
- "12.02%" — CF on Llama DocRED (line ~92)
- "0.93%" — S1 DR on SciERC (table line ~103)
- "9.90%" — S1 CF on SciERC (table line ~103)
- "10.83%" — DR+CF total under S1 (table line ~103)
- "14.78%" — DR under CF fallback (table line ~104)
- "0.04%" — CF under CF fallback (table line ~104)
- "14.82%" — DR+CF total under CF fallback (table line ~104)
- "36.64%" — f_gf under CF fallback (table line ~104)
- "+13.85pp" — DR increase from CF fallback (line ~106)
- "-9.86pp" — CF decrease from CF fallback (line ~106)
- "+3.99pp" — total violation increase from CF fallback (line ~106)
- "15.9×" — DR increase multiplier (0.93%→14.78%) (line ~113)
- "36.64%" — token-level fallback rate at type-bearing positions (line ~117)
- "0.46%" — first-token position fallback rate (line ~117)
- "3 models × 2 datasets" — scope of DR/CF inverse association (line ~121)
- "63.3%" — fraction of CF violations involving Generic type on SciERC (line ~124)
- "9.90%→1.18%" — CF reduction with LoRA fine-tuning (line ~127)
- "88%" — relative CF reduction from LoRA (line ~127)
- "1.18%" — residual CF after LoRA (line ~128)
- "551" — SciERC document count (multiple occurrences)

**Causal tracing table (lines 59–64):**
- Qwen3-8B FT S1: Fallback 0/2256 (0%), DR=0
- Qwen3-8B ZS S1: Fallback 16/3458 (0.46%), DR=16, From FB=100%
- Llama-3.1-8B FT S1: Fallback 1/2162 (0.05%), DR=1, From FB=100%
- Llama-3.1-8B ZS S1: Fallback 1/2630 (0.04%), DR=1, From FB=100%
- "18" — total residual DR violations across four configurations (line ~70)
- "≤0.05%" — fallback rate after fine-tuning (line ~71)

**CF-DR trade-off table:**
- "0.93" DR, "9.90" CF, "10.83" DR+CF — S1 baseline (line ~103)
- "14.78" DR, "0.04" CF, "14.82" DR+CF, "36.64" f_gf — CF fallback (line ~104)

**Bootstrap CIs table (lines 181–191):**
- Qwen3-8B/SciERC: ΔR-F1 = −0.10pp, 95% CI [−0.30, 0.00], p=.726, d=−0.05
- Qwen3-8B/DocRED: ΔR-F1 = −0.31pp, 95% CI [−0.69, +0.01], p=.056, d=−0.37
- Llama-3.1-8B/SciERC: ΔR-F1 = +0.02pp, 95% CI [0.00, +0.07], p=.736, d=+0.01
- Llama-3.1-8B/DocRED: ΔR-F1 = +0.06pp, 95% CI [−0.11, +0.25], p=.535, d=+0.07
- Qwen3-8B/SciERC DR: Δ=−1.95, CI [−2.87, −1.11], p<.001, d=−6.15
- Qwen3-8B/DocRED DR: Δ=−0.75, CI [−1.07, −0.48], p<.001, d=−7.00
- Llama-3.1-8B/SciERC DR: Δ=−1.02, CI [−1.98, −0.29], p<.001, d=−3.17
- Llama-3.1-8B/DocRED DR: Δ=−0.29, CI [−0.53, −0.10], p<.001, d=−3.02
- "k=4" — comparisons for Bonferroni correction (line ~167)
- "α_adj=0.0125" — adjusted alpha (line ~167)
- "|d|≤0.37" — max effect size for R-F1 (line ~167)
- "p_B=1.00" — Qwen3-8B/SciERC corrected p (line ~168)
- "p_B=0.224" — Qwen3-8B/DocRED corrected p (line ~168)
- "p_B=1.00" — Llama-3.1-8B/SciERC corrected p (line ~168)
- "p_B=1.00" — Llama-3.1-8B/DocRED corrected p (line ~168)
- "|d|≥3.0" — minimum DR effect size (line ~169)
- "all p_Bonf<0.005" — DR reduction significance (line ~169)
- "10,000" — bootstrap iterations (line ~166)
- "seed=42" — bootstrap seed (line ~166)

**Practical significance:**
- "~8%" — zero-shot relation F1 on both datasets (line ~205)
- "49–53%" — supervised SOTA on SciERC (line ~206)
- "1–2%" — residual DR after LoRA (line ~208)

**Post-hoc filtering comparison:**
- "8.63 vs. 8.36" — SciERC post-hoc vs. OntoCoDec F1 (line ~218)
- "9.61 vs. 8.23" — DocRED post-hoc vs. OntoCoDec F1 (line ~218)
- "48.1%" — DocRED triples discarded by post-hoc filtering (line ~221)
- "127" — true positives lost in DocRED post-hoc (line ~221)
- "11.2%" — fraction of correct predictions lost (line ~221)
- "9.46%→8.40%" — recall drop from post-hoc filtering (line ~221)
- "2.47%" — residual ET for post-hoc (line ~223)
- "0%" — OntoCoDec ET (line ~223)

**CF violation distribution table (lines 249–260):**
- Generic ↔ OtherScientificTerm: 85 (34.7%)
- Generic ↔ Material: 35 (14.3%)
- Generic ↔ Metric: 30 (12.2%)
- Method ↔ Task: 20 (8.2%)
- Material ↔ Method: 17 (6.9%)
- OtherScientificTerm ↔ Task: 12 (4.9%)
- 10 further pairs (each ≤3.3%): 46 (18.8%)
- Total: 245 (100.0%)
- "248 CF violations" / "245 unique entity-document pairs" (line ~235)
- "63.3%" — Generic-involving violations (line ~236)
- "155/245" — count/total for Generic (line ~236)
- "53/162, 32.7%" — Generic↔OtherScientificTerm on Llama SciERC (line ~239)
- "76.6%" — MISC-driven Qwen DocRED CF violations (line ~239)
- "≤1%" — CF rates under unconstrained decoding (line ~240)

**Cascade error breakdown table (lines 289–296):**
- Hallucinated entity: 144 (58.1%)
- Correct type lock: 45 (18.1%)
- True cascade error: 18 (7.3%)
- Other/ambiguous: 41 (16.5%)
- Total: 248 (100.0%)
- "2.5×" — correct type locks more frequent than true cascade errors (line ~276)
- "22 CF violations, 20 documents" — fine-tuned CF (line ~278)
- "0/22" — cascade errors under fine-tuning (line ~279)

**Per-relation DR elimination table (lines 324–331):**
- Evaluate-for: κ=0.361, LoRA DR=13.13%, n=99; S1 DR=0%, n=98
- Part-of: κ=0.417, LoRA DR=5.77%, n=52; S1 DR=0%, n=52
- Compare: κ=0.528, LoRA DR=5.00%, n=40; S1 DR=0%, n=40
- Conjunction: κ=0.306, LoRA DR=1.31%, n=153; S1 DR=0%, n=153
- Feature-of: κ=0.278, LoRA DR=1.35%, n=74; S1 DR=0%, n=74
- Used-for: κ=0.028, LoRA DR=0.16%, n=634; S1 DR=0%, n=635
- Hyponym-of: κ=0.417, DR=0%

**Fine-tuned four-way ablation table (lines 357–381):**
SciERC Qwen3-8B:
- Unconstrained: DR=1.95, RV=0, ET=0, CF=0, PF=0, E-F1=67.05, R-F1=43.86
- Grammar: DR=1.90, RV=0, ET=0, CF=0, PF=0, E-F1=67.05, R-F1=43.86
- Semantic: DR=0.60, RV=0, ET=0, CF=0.18, PF=0, E-F1=67.05, R-F1=43.69
- S1: DR=0, RV=0, ET=0, CF=1.18, PF=0, E-F1=67.05, R-F1=43.77

SciERC Llama-3.1-8B:
- Unconstrained: DR=1.11, RV=0, ET=0, CF=0, PF=0, E-F1=67.76, R-F1=45.45
- Grammar: DR=1.11, RV=0, ET=0, CF=0, PF=0, E-F1=67.76, R-F1=45.45
- Semantic: DR=0.65, RV=0, ET=0, CF=0.10, PF=0, E-F1=67.76, R-F1=45.47
- S1: DR=0.09, RV=0, ET=0, CF=0.46, PF=0, E-F1=67.76, R-F1=45.47

DocRED Qwen3-8B:
- Unconstrained: DR=0.76, RV=0.27, ET=0, CF=0.12, PF=7.11, E-F1=82.15, R-F1=40.86
- Grammar: DR=0.61, RV=0, ET=0, CF=0.11, PF=7.01, E-F1=82.19, R-F1=40.85
- Semantic: DR=0.19, RV=0.23, ET=0, CF=0.27, PF=7.52, E-F1=82.15, R-F1=40.85
- S1: DR=0.01, RV=0, ET=0, CF=0.41, PF=8.52, E-F1=81.43, R-F1=40.56

DocRED Llama-3.1-8B:
- Unconstrained: DR=0.49, RV=0.15, ET=0, CF=0.08, PF=2.30, E-F1=83.93, R-F1=43.72
- Grammar: DR=0.51, RV=0, ET=0, CF=0.12, PF=2.30, E-F1=84.04, R-F1=43.72
- Semantic: DR=0.48, RV=0.15, ET=0, CF=0.16, PF=2.40, E-F1=84.02, R-F1=43.85
- S1: DR=0.21, RV=0, ET=0, CF=0.21, PF=2.51, E-F1=83.94, R-F1=43.78

- "41–69%" — semantic layer DR reduction on SciERC FT (line ~392)
- "2–75%" — semantic layer DR reduction on DocRED FT (line ~392)
- "80 violations in 16,074 triples" — Llama DocRED DR denominator (line ~392)
- "DR≤0.21%" — near-complete elimination in all 4 FT settings (line ~393)
- "-0.30pp" — max R-F1 decrease S1 vs. unconstrained (line ~394)

**DocRED Zero-Shot Ablation table (lines 420–439):**
- Unconstrained: DR=18.46, ΔDR=---, RV=29.66, ET=2.48, CF=0.10, Total=18.56, Rel.=7.74, Ent.=58.15
- Grammar: DR=26.17, ΔDR=↑42%, RV=0.03, ET=0, CF=0.07, Total=26.24, Rel.=8.31, Ent.=59.38
- Semantic: DR=13.84, ΔDR=↓25%, RV=29.87, ET=4.22, CF=1.05, Total=14.89, Rel.=7.70, Ent.=57.81
- S1: DR=10.21, ΔDR=↓45%, RV=0.03, ET=0, CF=2.57, Total=12.78, Rel.=8.23, Ent.=59.37
- "+0.49pp" — R-F1 bootstrap significance (p<0.001) (line ~446)

**Residual DR error analysis (lines 461–465):**
- Entity type errors: 39%
- Schema coverage gaps: 33%
- Incorrect relation selection: 17%
- Direction reversal: 11%
- "3 of 36" — non-Llama DocRED residual violations (line ~468)
- "33 of 36" — Llama DocRED residual violations (line ~469)
- "92%" — Llama DocRED share of residual (line ~469)
- "14/33, 42%" — entity type errors in Llama DocRED (line ~469)
- "36" — total fine-tuned residual DR violations (line ~457)

**Post-hoc extended table (lines 490–510):**
ZS:
- Qwen/SciERC: Reject=16.8%, R-F1_ph=8.63, R-F1_cd=8.36, ph wins
- Llama/SciERC: Reject=13.9%, R-F1_ph=2.71, R-F1_cd=2.54, ph wins
- Mistral/SciERC: Reject=20.3%, R-F1_ph=3.94, R-F1_cd=3.67, ph wins
- Qwen/DocRED: Reject=48.1%, R-F1_ph=9.61, R-F1_cd=8.23, ph wins
- Llama/DocRED: Reject=42.2%, R-F1_ph=7.44, R-F1_cd=6.27, ph wins
- Mistral/DocRED: Reject=73.7%, R-F1_ph=3.85, R-F1_cd=5.52, cd wins
FT:
- Qwen/SciERC: Reject=1.95%, R-F1_ph=43.94, R-F1_cd=43.77, ph wins
- Llama/SciERC: Reject=1.11%, R-F1_ph=45.23, R-F1_cd=45.47, cd wins
- Qwen/DocRED: Reject=1.03%, R-F1_ph=41.11, R-F1_cd=40.79, ph wins (note: likely 40.56 in main FT table — potential inconsistency)
- Llama/DocRED: Reject=0.64%, R-F1_ph=43.92, R-F1_cd=43.78, cd wins
- "~70%" — crossover rejection rate (line ~513)
- "+1.67pp" — cd advantage at >70% rejection (line ~513)
- "Δ≤0.55pp" — FT convergence (line ~515)

**Runtime:**
- "4.163 s/doc" — SciERC unconstrained inference (line ~522)
- "4.710 s/doc" — SciERC S1 constrained decoding (line ~522)
- "+13.1%" — overhead (line ~522)
- "0.044 s" — XGrammar compilation (line ~524)
- "0.33 s" — full constraint pipeline compilation on SciERC (line ~524)
- "2.612 s/doc" — fine-tuned unconstrained inference (line ~529)
- "2.873 s/doc" — fine-tuned S1 constrained (line ~529)
- "+10.0%" — fine-tuned overhead (line ~529)
- "n=551" — document count for fine-tuned latency (line ~529)
- "37%" — absolute generation time drop under FT vs. ZS (line ~530)

**Fuzzy matching:**
- "80%" — token overlap threshold (line ~538)
- "≤2" — edit distance threshold (line ~538)
- "98" — additional TPs from fuzzy matching on Mistral DocRED (line ~540)
- "+0.84pp" — R-F1 from fuzzy matching (line ~540)
- "3.50% vs. 4.34%" — strict vs. fuzzy R-F1 for Mistral (line ~540)

**Prompt comparison table (lines 562–568):**
SciERC Unconstrained: DR=15.4, RV=1.4, ET=0.4, CF=0.1
SciERC Schema-informed: DR=5.8, RV=0.3, ET=0.0
DocRED Unconstrained: DR=18.5, RV=29.7, ET=2.5, CF=0.1
DocRED Schema-informed: DR=12.8, RV=18.4, ET=0.2, CF=0.2

**WikiEvents:**
- "56" — event types (line ~576)
- "80" — argument roles (line ~576)
- "27" — entity types (line ~576)
- "245" — (event_type, role)→allowed_entity_types constraints (line ~576)
- "mean κ̄=0.82" — WikiEvents role-level tightness (line ~582)
- "median 0.89" — WikiEvents median κ (line ~582)
- "84%" — fraction of roles with κ≥0.80 (line ~582)
- "4 or fewer" — valid entity types for roles with κ≥0.80 (line ~582)
- "50%" — AC rate for roles with κ≥0.90 (line ~583)
- "21%" — AC rate for 0.80≤κ<0.90 (line ~583)
- "30%" — AC rate for loose (κ<0.80) roles (line ~583)
- "0%" — AC for Transportation.Vehicle→VEH (line ~584)
- "κ=0.963" — tightness for Transportation.Vehicle→VEH (line ~584)
- "126 args, 34% AC, κ=0.59" — Attack.Target role (line ~585)

**Lucky violations table (lines 606–611):**
- Qwen3-8B/SciERC: DR 1.95→0, Lucky=4 (0.41%), ΔRecall=−0.10, Churn=0.22%
- Llama-8B/SciERC: DR 1.11→0.09, Lucky=5 (0.51%), ΔRecall=±0.00, Churn=0%
- Qwen3-8B/DocRED: DR 1.03→0.01, Lucky=1 (0.01%), ΔRecall=−0.84, Churn=2.05%
- Llama-8B/DocRED: DR 0.64→0.21, Lucky=1 (0.01%), ΔRecall=−0.10, Churn=0.86%
- Average lucky: 0.24%, average ΔRecall=−0.26, average churn=0.78%

**Trie-only baseline table (lines 642–655):**
- Qwen3-8B LoRA: ET=0, RV=0, DR=95.5%, CF=0.09, R-F1=41.16, PF=9.1%
- Qwen3-8B ZS: ET=0, RV=0, DR=29.3%, CF=0, R-F1=8.64, PF=0%
- Llama-8B LoRA: ET=0, RV=0, DR=15.2%, CF=0, R-F1=19.95, PF=50.8%
- Llama-8B ZS: ET=0, RV=0, DR=84.4%, CF=0.36, R-F1=2.90, PF=0%
DR gaps vs S1:
- Qwen3-8B LoRA: S1=0%, Trie=95.5%, Gap=95.5pp
- Qwen3-8B ZS: S1=0.93%, Trie=29.3%, Gap=28.4pp
- Llama-8B LoRA: S1=0.09%, Trie=15.2%, Gap=15.1pp
- Llama-8B ZS: S1=0.08%, Trie=84.4%, Gap=84.3pp
- "83%" — fraction of triples with entity type fields omitted under trie-only (line ~628)
- "0–51%" — parse failure range for trie-only (line ~628)
- "15–96%" — DR range for trie-only (line ~628)
- "50.8%" — Llama LoRA parse failure (line ~629)
- "45.47→19.95" — R-F1 collapse (line ~629)

**vLLM verification table (lines 714–717):**
- Grammar-Only (XGrammar): DR=14.84, RV=0, ET=0, CF=9.90, R-F1=8.23
- vLLM guided_json: DR=15.26, RV=0, ET=0, R-F1=8.75
- Δ: DR=+0.42, R-F1=+0.52
- "~15%" — DR left unaddressed by CFG-based approaches (line ~724)

**Dual-factor analysis:**
- "y=0.366x−0.138" — linear fit (line ~140)
- "R²=0.886" — fit quality (line ~140)
- "n=4" — data points (line ~140)
- "F(1,2)=15.54" — F-statistic (line ~140)
- "p≈0.058" — p-value (line ~140)
- "7.58%" — Mistral-7B unconstrained ET on DocRED (line ~142)
- "33.21%" — Mistral residual DR on DocRED (line ~142)
- ">5%" — ET threshold for principled exclusion (line ~143)
- "0.842" — DocRED κ̄ (line ~144)
- "0.333" — SciERC κ̄ (line ~144)

**Dataset-dependent F1:**
- "+0.49pp" — DocRED R-F1 gain (p<0.001) (line ~153)
- "+0.13pp" — SciERC R-F1 gain (p=0.58) (line ~153)
- "29.66%" — DocRED baseline RV (line ~154)
- "5,189" — OOV predictions as false positives (line ~154)
- "1.39%" — SciERC baseline RV (line ~155)
- "24" — SciERC OOV predictions (line ~155)
- "16.03%" — Llama DocRED baseline RV (line ~156)
- "+0.29pp" — Llama DocRED R-F1 gain (line ~156)

---

## appendix_70b_ablation.tex

**SciERC 70B table (lines 21–27):**
- Unconstrained: DR=1.50, RV=0, ET=0, CF=0, R-F1=44.73, E-F1=64.86
- Grammar: DR=1.50, RV=0, ET=0, CF=0, R-F1=44.63, E-F1=64.82
- Semantic: DR=0.60, RV=0, ET=0, CF=9, R-F1=44.73, E-F1=64.86
- S1: DR=0, RV=0, ET=0, CF=15, R-F1=44.53, E-F1=64.76
- S2: DR=0, RV=0, ET=0, CF=18, R-F1=36.28, E-F1=62.35
- Beam4 S1: DR=0, RV=0, ET=0, CF=1, R-F1=44.81, E-F1=64.89
- "+3.58pp" — DR increase from grammar-only on DocRED ZS (line ~34)
- "60%" — semantic layer DR reduction at 70B (line ~35)
- "−8.45pp" — S2 R-F1 degradation vs. S1 on SciERC (line ~36)
- "k=4" — optimal beam width (line ~37)

**DocRED LoRA 70B table (lines 58–64):**
- Unconstrained: DR=0.22, RV=0.57, ET=0, CF=2, R-F1=43.80, E-F1=80.34
- Grammar: DR=0.38, RV=0, ET=0, CF=0.06%, R-F1=43.96, E-F1=80.13
- Semantic: DR=0, RV=0.51, ET=0, CF=0.21%, R-F1=43.61, E-F1=80.06
- S1: DR=0, RV=0, ET=0, CF=0.18%, R-F1=43.95, E-F1=79.38
- S2: DR=0, RV=0, ET=0, CF=0.34%, R-F1=36.45, E-F1=84.96
- Beam4 S1: DR=0, RV=0, ET=0, CF=0, R-F1=48.14, E-F1=85.57
- PF: greedy S1=12.5% (25/200), S2=0% (0/200), beam4=0.5% (1/200) (line ~69)
- "+0.16pp" — grammar DR increase (line ~73)
- "−7.50pp" — S2 R-F1 degradation on DocRED (line ~75)
- "+4.19pp" — R-F1 gain from beam search (43.95→48.14) (line ~77)
- "12.5%" — greedy S1 parse failures (25/200) (line ~77)
- "0.5%" — beam parse failures (1/200) (line ~77)
- "+0.28pp" — pure beam quality gain on SciERC (line ~78)

**DocRED ZS 70B table (lines 97–101):**
- Unconstrained: DR=13.45, RV=7.88, ET=0, CF=0, R-F1=13.25, E-F1=70.14
- Grammar: DR=17.03, RV=0, ET=0, CF=0, R-F1=13.23, E-F1=70.12
- Semantic: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10
- S1: DR=0, RV=0, ET=0, CF=173, R-F1=13.25, E-F1=70.05
- "+3.58pp" — grammar DR increase on DocRED ZS 70B (line ~108)
- "87.7%" — semantic-only DR reduction (line ~109)
- "200-document subset" — evaluation size (line ~103)

---

## appendix_llama_per_relation.tex

**Per-relation table (lines 21–31):**
- dissolved/demolished (P576): 73 triples, 24 violations, 32.9% DR
- followed by (P156): 117 triples, 24 violations, 20.5% DR
- unemployment rate (P1198): 15 triples, 3 violations, 20.0% DR
- end time (P582): 130 triples, 21 violations, 16.2% DR
- instance of (P31): 290 triples, 37 violations, 12.8% DR
- product/material produced (P1056): 98 triples, 11 violations, 11.2% DR
- location of formation (P740): 81 triples, 8 violations, 9.9% DR
- head of state (P35): 41 triples, 3 violations, 7.3% DR
- applies to jurisdiction (P1001): 637 triples, 45 violations, 7.1% DR
- conflict (P607): 453 triples, 30 violations, 6.6% DR
- "16.03%" — Llama baseline RV (line ~8)
- "29.66%" — Qwen baseline RV (line ~8)
- "2.55%" — Llama residual DR under S1 (line ~9)
- "418/16,368 triples" — DR violations/total (line ~9)
- "10.21%" — Qwen residual DR under S1 (line ~36)
- "83%" — P1198 fallback rate (Qwen) (line ~36)
- "78%" — P171 fallback rate (Qwen) (line ~36)
- "20.0%" — Llama P1198 DR rate (line ~36)
- "2.55% vs. 10.21%" — Llama vs. Qwen residual DR (line ~38)

---

## appendix_sampling_table.tex

**Sampling table (lines 12–17):**
SciERC (551):
- Greedy: ET=0, RV=0, DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36
- Sampling (T=0.7, p=0.9): ET=0, RV=0, DR=0.75, CF=9.90, E-F1=31.28, R-F1=7.42
DocRED (114†):
- Greedy: ET=0, RV=0.03, DR=10.21, CF=2.57, E-F1=59.37, R-F1=8.23
- Sampling: ET=0, RV=0, DR=10.31, CF=12.63, E-F1=57.05, R-F1=7.92
- "T=0.7" — sampling temperature (line ~7)
- "p=0.9" — nucleus sampling parameter (line ~7)
- "114" — DocRED sampling subset size (line ~15)
- "~300h" — estimated time for full DocRED sampling (line ~19)

---

## appendix_beam_search.tex

**Beam search table (lines 31–54):**
- Qwen3-8B/SciERC: Greedy DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36; Beam DR=0, CF=0.53, E-F1=32.00, R-F1=8.56
- Qwen3-8B/DocRED(50): Greedy DR=8.69, CF=2.08, E-F1=59.08, R-F1=8.33; Beam DR=0, CF=0.55, E-F1=58.64, R-F1=9.37
- Llama/SciERC: Greedy DR=0.08, CF=6.56, E-F1=23.49, R-F1=2.54; Beam DR=0, CF=0.93, E-F1=25.04, R-F1=3.33
- Llama/DocRED(50): Greedy DR=1.58, CF=6.85, E-F1=55.35, R-F1=6.12; Beam DR=0, CF=0.94, E-F1=55.62, R-F1=9.47
- Mistral/SciERC: Greedy DR=13.40, CF=1.27, E-F1=27.46, R-F1=3.67; Beam DR=13.79, CF=0.57, E-F1=26.66, R-F1=4.37
- Mistral/DocRED(50): Greedy DR=28.37, CF=0.34, E-F1=51.60, R-F1=4.19; Beam DR=21.37, CF=0.19, E-F1=51.78, R-F1=5.70
- "64 lines of code" — GrammarMatcher adaptation (line ~11)
- "61 lines of code" — TypeConstraintProcessor adaptation (line ~13)
- "~125 lines total" — beam search adaptation (line ~14)
- "k=4" — beam width (line ~17)
- "74%" — CF reduction Qwen DocRED (8 → 50-doc subset) (line ~61)
- "86%" — CF reduction Llama DocRED (line ~61)
- "+3.4pp" — Llama DocRED R-F1 gain (line ~62)
- "55%" — Mistral SciERC CF relative reduction (line ~66)
- "+0.7pp" — Mistral SciERC R-F1 improvement (line ~66)
- "25%" — Mistral DocRED DR relative reduction (line ~67)

**Beam ablation table (lines 82–86):**
- k=1: DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36
- k=2: DR=0.35, CF=4.12, E-F1=31.54, R-F1=8.75
- k=4: DR=0, CF=0.53, E-F1=32.00, R-F1=8.56
- k=8: DR=0, CF=0.08, E-F1=32.18, R-F1=8.39
- "2 residual violations" — at k=8 (line ~91)

**Beam width-latency Pareto (LoRA) table (lines 116–131):**
- k=1 unc: E-F1=66.88, R-F1=42.95, DR=2.11, CF=0, Lat=2.494s, Rel=1.00×
- k=1 con: E-F1=66.88, R-F1=42.95, DR=0, CF=0.50, Lat=2.932s, Rel=1.18×
- k=2 unc: E-F1=67.79, R-F1=44.75, DR=1.54, CF=0, Lat=2.954s, Rel=1.18×
- k=2 con (Pareto optimal): E-F1=67.71, R-F1=44.60, DR=0, CF=0.11, Lat=3.463s, Rel=1.39×
- k=4 unc: E-F1=67.49, R-F1=43.72, DR=1.89, CF=0, Lat=3.485s, Rel=1.40×
- k=4 con: E-F1=67.22, R-F1=43.60, DR=0, CF=0, Lat=4.069s, Rel=1.63×
- k=8 unc: E-F1=66.40, R-F1=43.17, DR=1.77, CF=0, Lat=4.194s, Rel=1.68×
- k=8 con: E-F1=66.36, R-F1=43.65, DR=0, CF=0, Lat=5.058s, Rel=2.03×

**LoRA + beam composability:**
- "1.18%→0%" — CF elimination with beam k=4 on SciERC LoRA (line ~137)
- R-F1=43.60, E-F1=66.88 — Qwen LoRA beam-4 SciERC (line ~137)
- "0% across all four metrics" — zero-violation result (line ~138)
- "R-F1=46.18" — Llama LoRA beam-4 SciERC (line ~138)

**Full DocRED 998-doc zero-shot beam (lines 155–157):**
- Qwen3-8B: ET=0, RV=0, DR=0, CF=4.94, E-F1=58.19, R-F1=8.72
- Llama-3.1-8B: ET=0, RV=0, DR=0, CF=1.00, E-F1=57.81, R-F1=8.83
- "8.54%→1.00%, 88% reduction" — Llama CF improvement (line ~143)
- "+2.6pp" — Llama R-F1 gain (line ~143)

**DocRED LoRA beam table (lines 175–183):**
- Qwen3-8B Greedy: DR=0.01, CF=0.41, E-F1=81.43, R-F1=40.56, PF=8.52
- Qwen3-8B Beam-4: DR=0, CF=0.01, E-F1=84.00, R-F1=44.46, PF=2.9
- Llama-3.1-8B Greedy: DR=0.21, CF=0.21, E-F1=83.94, R-F1=43.78, PF=2.51
- Llama-3.1-8B Beam-4: DR=0, CF=0, E-F1=85.23, R-F1=47.17, PF=1.3
- "1.3% to 2.9%" — LoRA beam-4 parse failure range (line ~162)

**Beam latency table (lines 199–204):**
- Greedy unconstrained: 2.612 s/doc, 1.00×
- Greedy constrained (S1): 2.873 s/doc, 1.10×
- Beam-4 unconstrained: 3.446 s/doc, 1.32×
- Beam-4 constrained (S1): 4.013 s/doc, 1.54×
- "32%" — beam search latency overhead (line ~210)
- "10%→17%" — constraint overhead increase greedy→beam (line ~210)
- "<1 MB" — per-beam entity registry memory at k=8 (line ~211)
- "100% skip rate" — type-consensus constraint on 551 SciERC/50 DocRED (line ~216)
- "0/551" — SciERC candidates changed by TCR with beam (line ~220)

---

## appendix_reproducibility.tex

**LoRA hyperparameters:**
- "r=16" — rank (line ~5)
- "α=32" — alpha (line ~5)
- "dropout 0.05" — dropout rate (line ~5)
- "lr 2×10⁻⁴" — learning rate (line ~6)
- "warmup ratio 0.1" — warmup (line ~6)
- "effective batch size 16" — batch size (line ~6)
- "3 epochs" — training epochs (line ~6)
- "SciERC: 1,762 examples (260 dev), 333 steps" (line ~7)
- "DocRED: 3,053 examples (998 dev), 573 steps" (line ~7)
- "2,048" — max sequence length SciERC (line ~8)
- "4,096" — max sequence length DocRED (line ~8)
- "seed 42" — random seed (line ~9)
- "98 GB VRAM" — GPU memory (line ~12)
- "~11 minutes" — SciERC fine-tuning time (line ~13)
- "~1.5 hours" — DocRED fine-tuning time (line ~13)
- "PyTorch 2.10, Transformers 4.57, PEFT 0.19, TRL 1.1, Accelerate 1.13" — software versions (line ~14)
- "+13.1%" — ZS S1 overhead on SciERC (line ~18)
- "+10.0%" — FT S1 overhead on SciERC (line ~18)
- "seeds 42, 123, 456" — seeds tested (line ~25)

**Seed variance table (lines 42–45):**
- Qwen3-8B Unc: E-F1=66.94±0.08, R-F1=43.25±0.43, DR=2.06±0.08
- Qwen3-8B Con: E-F1=66.94±0.08, R-F1=43.22±0.39, DR=0.00±0.00
- Llama-3.1-8B Unc: E-F1=67.99±0.16, R-F1=45.38±0.05, DR=1.04±0.05
- Llama-3.1-8B Con: E-F1=67.99±0.16, R-F1=45.40±0.05, DR=0.03±0.04
- "σ(E-F1)≤0.16pp" (line ~28)
- "σ(R-F1)≤0.43pp" (line ~28)
- "σ(DR%)≤0.08pp" (line ~28)
- "−2.06pp (Qwen), −1.01pp (Llama)" — DR reduction vs. variance (line ~29)
- ">12×" — signal-to-noise ratio (line ~29)
- "5,000" — bootstrap resamples for 200-doc justification (line ~58)
- "±3.3 points" — 95% CI for 200-doc R-F1 (line ~59)
- "±0.45pp" — 200-doc DR margin of error (line ~59)
- "15.0%" — unconstrained DR for ZS power analysis (line ~60)
- "Cohen's h=0.80" — effect size for ZS power (line ~60)
- "100% power" — ZS 200-doc power (line ~60)
- "<0.5%" — FT violation rate for fine-tuned power (line ~60)
- "94.9%" — fraction of 200-doc subsamples correctly identifying DR direction (line ~60)

---

## appendix_power_analysis.tex

**Power analysis table (lines 15–20):**
- SciERC: n=551, 95% CI=±1.8pp, MDE=1.2pp
- DocRED: n=998, 95% CI=±0.8pp, MDE=0.5pp
- DocRED (70B): n=200, 95% CI=±3.3pp, MDE=2.1pp
- WikiEvents: n=20, 95% CI=±3.0pp, MDE=2.0pp
- "≥1,000 bootstrap resamples" (line ~7)
- "80% power, α=0.05" — test parameters (line ~7)
- "ρ=0.9" — assumed correlation (line ~7)
- "8.8–38.3%" — WikiEvents RoV before constraints (line ~30)
- "0%" — WikiEvents RoV after constraints (line ~30)
- "[0%,0%]" — constrained bootstrap CI (line ~30)
- "[2.4%,15.4%]" and "[25.4%,46.7%]" — unconstrained CIs (line ~30)
- "power≈1.0" — power for violation elimination (line ~30)
- "n=20" — WikiEvents test size (line ~29)
- "n=551, n=998" — SciERC/DocRED CI evaluation sizes (line ~31)
- "≤1.8pp" — CI bound (line ~31)

---

## appendix_doc_length.tex

**SciERC doc length table (lines 16–23):**
- Short (196 docs): Uncon. ET=1, RV=5, DR=57, CF=0, Total=63, E-F1=32.4, R-F1=8.9; Const. ET=0, RV=0, DR=5, CF=5, Total=10, E-F1=32.4, R-F1=8.9
- Medium (180 docs): Uncon. ET=6, RV=9, DR=104, CF=0, Total=119, E-F1=27.8, R-F1=6.7; Const. ET=0, RV=0, DR=7, CF=15, Total=22, E-F1=27.8, R-F1=6.7
- Long (175 docs): Uncon. ET=3, RV=10, DR=104, CF=1, Total=118, E-F1=29.9, R-F1=7.0; Const. ET=0, RV=0, DR=4, CF=20, Total=24, E-F1=30.0, R-F1=7.3
- "≤19 words" — short bin boundary (line ~9)
- "≤27 words" — medium bin boundary (line ~9)
- ">27 words" — long bin boundary (line ~9)

**DocRED doc length table (lines 37–45):**
- Short (336 docs): Uncon. ET=177, RV=1238, DR=1021, CF=9, Total=2445, E-F1=61.1, R-F1=9.3; Const. ET=0, RV=0, DR=495, CF=138, Total=633, E-F1=62.6, R-F1=9.6
- Medium (332 docs): Uncon. ET=147, RV=1742, DR=1047, CF=5, Total=2941, E-F1=59.3, R-F1=7.9; Const. ET=0, RV=5, DR=544, CF=180, Total=729, E-F1=60.7, R-F1=8.5
- Long (330 docs): Uncon. ET=176, RV=2209, DR=1162, CF=3, Total=3550, E-F1=53.9, R-F1=5.6; Const. ET=0, RV=0, DR=731, CF=200, Total=931, E-F1=54.8, R-F1=5.8
- "≤160 words" — short bin DocRED (line ~31)
- "≤208 words" — medium bin DocRED (line ~31)
- ">208 words" — long bin DocRED (line ~31)

**Violation reduction table (lines 62–64):**
- SciERC Short: 63→10, 84.1% reduction
- SciERC Medium: 119→22, 81.5% reduction
- SciERC Long: 118→24, 79.7% reduction
- DocRED Short: 2445→633, 74.1% reduction
- DocRED Medium: 2941→729, 75.2% reduction
- DocRED Long: 3550→931, 73.8% reduction
- "80–84%" — SciERC reduction range (line ~69)
- "74–75%" — DocRED reduction range (line ~69)
- "+0.9–1.5 E-F1" — DocRED E-F1 improvement (line ~72)
- "+0.2–0.6 R-F1" — DocRED R-F1 improvement (line ~72)

---

## appendix_prompt_sensitivity.tex

**Prompt sensitivity table (lines 17–41):**
Qwen3-8B:
- Default Unconstrained: ET=0.40, RV=1.39, DR=15.37, E-F1=31.01, R-F1=8.23
- Default Constrained: ET=0, RV=0, DR=0.93, ΔDR=94.0%, E-F1=30.98, R-F1=8.36
- Minimal Unconstrained: ET=0.58, RV=1.16, DR=16.91, E-F1=31.98, R-F1=7.91
- Minimal Constrained: ET=0, RV=0, DR=0.92, ΔDR=94.6%, E-F1=31.99, R-F1=7.85
- Detailed Unconstrained: ET=0.22, RV=0.45, DR=11.07, E-F1=33.55, R-F1=10.48
- Detailed Constrained: ET=0, RV=0, DR=0.64, ΔDR=94.2%, E-F1=33.56, R-F1=10.48

Llama-3.1-70B (AWQ INT4):
- Default Unconstrained: ET=0, RV=0.61, DR=6.41, E-F1=35.22, R-F1=11.23
- Default Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=35.19, R-F1=11.24
- Minimal Unconstrained: ET=0.27, RV=5.88, DR=0.22, E-F1=37.51, R-F1=13.42
- Minimal Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=37.22, R-F1=11.35
- Detailed Unconstrained: ET=0, RV=0.26, DR=4.57, E-F1=40.42, R-F1=11.12
- Detailed Constrained: ET=0, RV=0, DR=0, ΔDR=100%, E-F1=40.35, R-F1=11.16

- "94.0%–94.6%" — 8B ΔDR range across prompts (line ~45)
- "0.3pp" — standard deviation across prompts (line ~45)
- "0.13pp max" — R-F1 shift (line ~45)
- "11.1%–16.9%" — 8B baseline DR range (line ~49)
- "0.22%–6.41%" — 70B baseline DR range (line ~49)
- "0.62%–3.50%" — CF introduced at 70B (line ~47)
- "0.62% and 0.75%" — LoRA 70B CF under Minimal/Detailed prompts (line ~53)

---

## appendix_case_studies.tex

**Error analysis (lines 148–177):**
- "514 FN, 668 FP, 21 CF" — LoRA S1 SciERC errors (line ~148)
- "460 TP" — true positives (line ~148)
- "R-F1=43.77" — LoRA S1 SciERC R-F1 (line ~148)
- "1 of 514 (0.2%)" — constraint-blocked false negatives (line ~177)
- "56%" — Used-for fraction of all SciERC relations (line ~163)
- "DR≤0.21%" — constraint enforcement leaves type-invalid outputs at this rate (line ~177)

---

## appendix_downstream_analysis.tex

**Lucky violations detail table (lines 13–18):**
- SciERC/Qwen-LoRA: TP=461, Lucky=4, %TP=0.87%, R drop=0.41pp
- SciERC/Llama-LoRA: TP=467, Lucky=5, %TP=1.07%, R drop=0.51pp
- DocRED/Qwen-LoRA: TP=5746, Lucky=1, %TP=0.02%, R drop=0.01pp
- DocRED/Llama-LoRA: TP=6226, Lucky=1, %TP=0.02%, R drop=0.01pp
- "1.07%" — max lucky violation fraction (5/467) (line ~24)
- "0.02%" — min lucky violation fraction (DocRED) (line ~24)
- "0.51pp" — max recall drop (line ~25)
- "164" — schema-violating predictions eliminated on Qwen DocRED (line ~26)
- "1" — correct predictions removed (line ~26)
- "163" — false positive predictions removed (line ~26)

---

## appendix_scalability.tex

**Scalability table (lines 12–15):**
- Small (SciERC): 6 types, 7 relations, compile=0.33s, overhead=1.02×
- Medium (DocRED): 6 types, 96 relations, compile=0.32s, overhead=1.03×
- Large (synth.): 100 types, 500 relations, compile=0.35s, overhead=1.03×
- XLarge (synth.): 200 types, 1,000 relations, compile=0.42s, overhead=1.03×
- "0.32s to 0.42s" — compilation range (7→1,000 relations) (line ~22)
- "~0.044s" — XGrammar automaton compilation (line ~22)
- "0.4ms to 17ms" — semantic constraint compilation range (line ~22)
- "2–3%" — constant inference overhead (line ~23)
- "~200" — entity type limit before prefix collisions (line ~24)
- "10 documents" — measurement sample per scale (caption line ~17)

---

## appendix_full_ft.tex

**Full FT table (lines 12–17):**
- Full FT unconstrained: E-F1=64.78, R-F1=37.89, DR=2.74%, CF=0%
- Full FT + S1: E-F1=64.78, R-F1=37.89, DR=0%, CF=1.31%
- LoRA unconstrained: E-F1=67.05, R-F1=43.86, DR=1.95%, CF=0%
- LoRA + S1: E-F1=67.05, R-F1=43.77, DR=0%, CF=1.18%
- "30 triples" — full FT DR violations (line ~24)
- "Part-of: 14.6%, Hyponym-of: 9.6%, Evaluate-for: 8.4%" — violation distribution by relation (line ~24)
- "lr=2×10⁻⁴" — learning rate (line ~4)
- "3 epochs, seed 42" — training config (line ~4)
- "0%→1.31%" — CF increase (line ~24)

---

## appendix_tcr.tex

**TCR SciERC table (lines 26–33):**
Zero-shot:
- Qwen: CF pre=9.75%, post=0%, DR pre=0.93%, post=1.21%, ΔE-F1=−1.29pp, Fund.=2.04%
- Llama: CF pre=6.40%, post=0%, DR pre=0.08%, post=0.30%, ΔE-F1=−1.78pp, Fund.=1.85%
- Mistral: CF pre=0.67%, post=0%, DR pre=13.36%, post=12.87%, ΔE-F1=+0.05pp, Fund.=0%
LoRA:
- Qwen: CF pre=1.19%, post=0%, DR pre=0%, post=0%, ΔE-F1=−0.75pp, Fund.=0%
- Llama: CF pre=0.46%, post=0%, DR pre=0.09%, post=0.09%, ΔE-F1=−0.18pp, Fund.=0%
- "κ̄=0.333" — SciERC (line ~35)
- "≤0.28pp" — max DR increase from TCR on SciERC (line ~39)
- "0–2%" — fundamental conflict rate SciERC (line ~39)

**TCR DocRED table (lines 56–65):**
Zero-shot:
- Qwen: CF pre=13.11%, post=0%, DR pre=10.21%, post=11.74%, ΔE-F1=−3.44pp, Fund.=13.52%
- Llama: CF pre=23.71%, post=0%, DR pre=2.55%, post=11.93%, ΔE-F1=−5.21pp, Fund.=22.78%
- 70B: CF pre=11.61%, post=0%, DR pre=0%, post=4.20%, ΔE-F1=−5.98pp, Fund.=18.26%
LoRA:
- Qwen: CF pre=0.42%, post=0%, DR pre=0.01%, post=0.14%, ΔE-F1=−0.16pp, Fund.=12.16%
- Llama: CF pre=0.36%, post=0%, DR pre=0.21%, post=0.20%, ΔE-F1=−0.17pp, Fund.=11.59%
- "κ̄=0.842" — DocRED (line ~67)
- "+9.38pp" — max DR regression from Llama TCR (line ~67)
- "−5.98pp" — max E-F1 drop from 70B TCR (line ~67)
- "12–23%" — fundamental conflict rates DocRED (line ~67)
- "2.55%→11.93%" — Llama DR regression (line ~78)
- "0%→4.20%" — 70B DR regression (line ~78)
- "0.36–0.42%" — LoRA baseline CF on DocRED (line ~79)
- "1.39×" — beam search latency (line ~83)

---

## appendix_kappa_case_study.tex

**Kappa case study table (lines 14–28):**
High DR:
- basin country (DocRED): κ=0.97, DR=74.6%, n=63
- product produced (DocRED): κ=0.94, DR=67.2%, n=61
- participant of (DocRED): κ=0.81, DR=58.6%, n=326
- Compare (SciERC): κ=0.53, DR=42.4%, n=66
- Feature-of (SciERC): κ=0.28, DR=33.5%, n=486
High κ, zero violations:
- lyrics by (DocRED): κ=0.94, DR=0.0%, n=9
- place of birth (DocRED): κ=0.92, DR=0.0%, n=157
- place of death (DocRED): κ=0.89, DR=0.0%, n=60
- subsidiary (DocRED): κ=0.86, DR=0.0%, n=5
- father (DocRED): κ=0.81, DR=0.0%, n=69
- ">50%" — DR for confusable-type relations (line ~36)

---

## appendix_high_kappa_analysis.tex

**Schema ambiguity table (lines 26–47):**
SciERC:
- Hyponym-of: α=0.83, |P_r|=21, Gold=298, Gold%=9.3%
- Part-of: α=0.83, |P_r|=21, Gold=179, Gold%=5.6%
- Compare: α=0.82, |P_r|=17, Gold=166, Gold%=5.2%
- Conjunction: α=0.77, |P_r|=25, Gold=400, Gold%=12.4%
- Feature-of: α=0.76, |P_r|=26, Gold=173, Gold%=5.4%
- Evaluate-for: α=0.71, |P_r|=23, Gold=313, Gold%=9.7%
- Used-for: α=0.67, |P_r|=35, Gold=1,690, Gold%=52.5%
DocRED (high α, 12 of 96 relations):
- sister city (P190): α=0.42, |P_r|=1, Gold=4, Gold%=0.01%
- basin country (P205): α=0.42, |P_r|=1, Gold=85, Gold%=0.22%
- mouth of watercourse (P403): α=0.42, |P_r|=1, Gold=95, Gold%=0.25%
- separated from (P807): α=0.41, |P_r|=2, Gold=2, Gold%=0.01%
- replaces (P1365): α=0.39, |P_r|=4, Gold=18, Gold%=0.05%
- capital of (P1376): α=0.37, |P_r|=3, Gold=76, Gold%=0.20%
- place of birth (P19): α=0.37, |P_r|=3, Gold=511, Gold%=1.34%
- operator (P137): α=0.36, |P_r|=7, Gold=95, Gold%=0.25%
- military branch (P241): α=0.36, |P_r|=5, Gold=108, Gold%=0.28%
- production company (P272): α=0.36, |P_r|=5, Gold=82, Gold%=0.21%
- place of death (P20): α=0.36, |P_r|=4, Gold=203, Gold%=0.53%
- location (P276): α=0.36, |P_r|=5, Gold=172, Gold%=0.45%
- "3.8%" — fraction of gold triples in high-α DocRED relations (line ~19)
- "36" — type pair slots (6²) (line ~75)
- "7 relations" — SciERC total (line ~75)
- "α≥0.36" — threshold (line ~18)
- "12 relations" — DocRED high-α count (line ~34)
- "(Method, Method)" — valid for all 7 SciERC relations; α=1.0 (line ~76)

**DR by ambiguity table (lines 62–70):**
Llama-3.1-8B:
- High-α (12 rels): Unconstrained DR=43.8%, n=861; S1 DR=3.2%, n=1,043
- Low-α (84 rels): Unconstrained DR=29.9%, n=12,809; S1 DR=2.5%, n=15,325
Qwen3-8B:
- High-α (12 rels): Unconstrained DR=31.9%, n=718; S1 DR=20.0%, n=1,119
- Low-α (84 rels): Unconstrained DR=21.2%, n=10,898; S1 DR=9.5%, n=16,217
- "2×" — gap Qwen retains high vs. low α under S1 (line ~81)
- "2.55%→2.51% for Llama" — exclusion analysis result (line ~82)
- "10.21%→9.53% for Qwen" — exclusion analysis result (line ~82)
- "15.4%→0.9% (Qwen), 13.3%→0.08% (Llama)" — SciERC DR reduction (line ~83)

---

## appendix_order_invariance.tex
- "551" — SciERC documents (line ~6)
- No other numerical data; purely qualitative result (byte-identical outputs)

---

## appendix_pumping_lemma.tex
- "6 entity types, 20+ entities" → "exceeds 10¹⁵ states" — DFA state count (line ~64)
- "O(|T|^|E|)" — DFA state complexity (line ~64)

---

## appendix_wikievents_pilot.tex

**WikiEvents table (lines 32–44):**
Qwen3-8B:
- Unconstrained: EV=24.0%, RoV=74.9%, AC=0.3%, CF=0, Trig.=11.8, Ent.=0
- Grammar: EV=0%, RoV=76.1%, AC=8.2%, CF=---
- S1: EV=0%, RoV=0%, AC=2.1%, CF=21.1%, Trig.=13.4, Ent.=14.1
Llama-3.1-8B:
- Unconstrained: EV=10.5%, RoV=88.8%, AC=0.1%, CF=0, Trig.=5.7, Ent.=0
- Grammar: EV=0%, RoV=77.0%, AC=8.8%, CF=---
- S1: EV=0%, RoV=0%, AC=3.8%, CF=17.2%, Trig.=7.5, Ent.=17.6
Mistral-7B:
- Unconstrained: EV=37.3%, RoV=63.9%, AC=0%, CF=0, Trig.=2.4, Ent.=0
- Grammar: EV=0%, RoV=64.0%, AC=13.8%, CF=---
- S1: EV=0%, RoV=0%, AC=1.3%, CF=14.9%, Trig.=3.9, Ent.=11.7
- "n=246 documents" — WikiEvents ZS evaluation (caption line ~47)
- "EV+RoV>85%" — combined vocabulary violations (line ~55)
- "entity F1=0" — unconstrained baseline (line ~55)
- "8–14%" — grammar-only AC rate range (line ~57)
- "64–77%" — grammar-only residual RoV range (line ~57)
- "1.3–3.8%" — residual AC range under S1 (line ~58)
- "15–21%" — CF range under S1 (line ~58)
- "0%→12–18%" — entity F1 gain (line ~59)
- "+1.5–1.8pp" — trigger F1 gain (line ~59)
- "n=20" — WikiEvents FT test split (line ~62)
- "194/20/20" — train/dev/test split (line ~62)
- "Qwen 38.31%→0%" — LoRA RoV elimination (line ~63)
- "Llama 8.8%→0%" — LoRA RoV elimination (line ~63)
- "≤0.8%" — LoRA AC rate (line ~63)
- "±1.1pp" — argument F1 range (line ~63)
- "−5.4/−0.6pp" — trigger F1 shifts (line ~63)
- "0.77–1.18%" — CF under FT (line ~64)
- "Arg-F1 std/mean>0.5" — high per-document variance (line ~64)
- "MDE≈±5.0pp" — WikiEvents FT MDE note (caption line ~50)

---

## appendix_zs_crossmodel.tex

**Cross-model table (lines 23–42):**
SciERC:
- Qwen (U): DR=15.37, RV=1.39, ET=0.40, CF=0.08, R-F1=8.23
- Qwen (S1): DR=0.93, RV=0, ET=0, CF=9.90, R-F1=8.36
- Llama (U): DR=13.34, RV=0.55, ET=0, CF=0.24, R-F1=2.68
- Llama (S1): DR=0.08, RV=0, ET=0, CF=6.56, R-F1=2.54
- Mistral (U): DR=56.94, RV=0, ET=1.50, CF=56.87†, R-F1=3.66
- Mistral (S1): DR=13.40, RV=0, ET=0, CF=1.27, R-F1=3.67
DocRED:
- Qwen (U): DR=18.46, RV=29.66, ET=2.48, CF=0.10, R-F1=7.74
- Qwen (S1): DR=10.21, RV=0.03, ET=0, CF=2.57, R-F1=8.23
- Llama (U): DR=26.07, RV=16.03, ET=0.13, CF=0.17, R-F1=5.98
- Llama (S1): DR=2.55, RV=0, ET=0, CF=12.02, R-F1=6.27
- Mistral (U): DR=57.42, RV=42.35, ET=7.58, CF=24.78, R-F1=4.34
- Mistral (S1): DR=33.20, RV=0, ET=0, CF=0.19, R-F1=5.52
- "Llama DocRED 9.1%" — parse failure rate (line ~45)
- "≤1.1%" — other parse failure rates (line ~45)
- "76–99% on SciERC" — DR reduction range (line ~53)
- "42–90% on DocRED" — DR reduction range (line ~53)
- "5/6 settings" — R-F1 improvements (line ~53)
- "12.02%" — max CF introduced (line ~54)
- "56.87%→1.27%" — Mistral CF reduction (line ~54)
- "15–74%" — post-hoc rejection rates (line ~55)
- "14×" — DocRED scale relative to SciERC (line ~59)

---

## appendix_quantization.tex

**Quantization table (lines 20–29):**
SciERC (551 docs):
- Qwen3-8B FP16: DR=0, R-F1=43.77, E-F1=67.05
- Qwen3-8B INT4: DR=0, R-F1=41.71, E-F1=67.05, Δ R-F1=−2.06
- Llama-3.1-8B FP16: DR=0.09, R-F1=45.47, E-F1=67.76
- Llama-3.1-8B INT4: DR=0, R-F1=43.98, E-F1=67.54, ΔDR=−0.09, ΔR-F1=−1.49, ΔE-F1=−0.22
DocRED (200 docs):
- Qwen3-8B FP16†: DR=0, R-F1=40.79†, E-F1=81.87†, PF=8.5%†
- Qwen3-8B INT4: DR=0, R-F1=40.07, E-F1=74.84, ΔR-F1=−0.72, ΔE-F1=−7.03‡, PF=18.5%
- Llama-3.1-8B FP16: DR=0, R-F1=47.35, E-F1=85.43, PF=2.0%
- Llama-3.1-8B INT4: DR=0, R-F1=48.04, E-F1=84.18, ΔR-F1=+0.69, ΔE-F1=−1.25, PF=2.5%
- "−2.06 to +0.69pp" — R-F1 change range (line ~39)
- "18.5% vs. 8.5%" — Qwen INT4 vs FP16 parse failures (line ~40)
- "−7.03pp" — Qwen DocRED E-F1 gap (line ~40)
- "†Qwen DocRED FP16 evaluated on 998 docs" (note line ~33)

---

## appendix_gollie_comparison.tex
No numerical data (qualitative comparison only)

---

## appendix_ai_assistants.tex
No numerical data

---

**Summary of key numbers by category for cross-reference audit:**

Key numbers appearing in multiple places (cross-reference candidates):
- "551" — SciERC document count (reproducibility, sampling, beam, causal tracing, fallback coverage, CF tables, error analysis, doc length, prompt sensitivity, order invariance, seed variance, scalability, quantization)
- "998" — DocRED document count (reproducibility, power analysis, DocRED ablation, beam, TCR)
- "15.37%" — SciERC baseline DR (related work, discussion, prompt sensitivity, cross-model table)
- "0.93%" — SciERC Qwen S1 DR (sampling, beam, causal tracing, CF-DR tradeoff, bootstrap table)
- "10.21%" — DocRED Qwen S1 DR (sampling, Llama per-relation, TCR, DocRED ablation, cross-model)
- "94%" — SciERC DR reduction (related work, discussion, prompt sensitivity)
- "29.66%" — DocRED baseline RV (discussion, DocRED ablation, cross-model)
- "18.46%" — DocRED baseline DR (discussion, DocRED ablation, cross-model)
- "8.36" — SciERC Qwen ZS R-F1 (sampling, beam ablation, beam pareto k=1, vLLM table, prompt sensitivity)
- "8.23" — DocRED Qwen ZS R-F1 (sampling, DocRED ablation, cross-model, vLLM)
- "43.77" — SciERC Qwen LoRA+S1 R-F1 (FT ablation, full FT, quantization, error analysis, beam composability)
- "67.05" — SciERC Qwen LoRA E-F1 (FT ablation, full FT, quantization, beam composability)
- "κ̄=0.333" (SciERC) and "κ̄=0.842" (DocRED) — appear in dual-factor, TCR, Llama per-relation
- "+0.49pp p<0.001" — DocRED R-F1 gain (discussion, DocRED ablation, cross-model)
- "2.87 BPE tokens" — OtherScientificTerm tokenization (discussion, twice)
- "seed=42" — reproducibility, bootstrap, full FT, beam pareto
- "10,000 bootstrap iterations" — discussion (bootstrap CI), reproducibility

**Potential inconsistency flagged:**
- In `appendix_discussion.tex` line ~39, text says "Qwen achieves CF=2.57% on DocRED vs. Llama's 12.02%", and also "Qwen3-8B shows f_gf=0.08% ... yielding 99.9% coverage" and "residual DR (0.93% vs. Llama's 0.08%)" — note this implies Qwen DR=0.93% and Llama DR=0.08% on SciERC, which is consistent with the main tables.
- In `appendix_discussion.tex` line ~39: "consistent with its lower residual DR (0.93% vs. Llama's 0.08%)" — but this is Qwen's DR vs Llama's DR on SciERC (both ZS S1), consistent with causal tracing table.
- `appendix_posthoc_extended` table: Qwen DocRED FT shows R-F1_cd=40.79, but `appendix_ft_ablation` table shows Qwen DocRED S1 R-F1=40.56 — **potential inconsistency** between these two tables for Qwen DocRED FT constrained R-F1 (40.79 vs 40.56).
- `appendix_beam_search.tex`: DocRED LoRA Qwen Greedy shows R-F1=40.56, PF=8.52 — matches FT ablation table.
- `appendix_quantization.tex`: Qwen DocRED FP16 R-F1=40.79† with note "evaluated on 998 docs" — explains discrepancy (subset vs. full set).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0381da55-6886-4871-bb21-24f13da765e5",
  "isSidechain": true,
  "agentId": "a16b2408c4cfcd2a6",
  "requestId": "req_011CbPriBctrfJ61aKR6GrQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4262678-5696-4bc1-97dd-f9d10e106d93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/director_8494441a",
  "sessionId": "485a49b0-2f8a-4e9c-b75d-f286f7540b25",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cosmic-coalescing-lagoon",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WuiDi2BwX1PXJyxsqaGLkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 94109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5853,
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
