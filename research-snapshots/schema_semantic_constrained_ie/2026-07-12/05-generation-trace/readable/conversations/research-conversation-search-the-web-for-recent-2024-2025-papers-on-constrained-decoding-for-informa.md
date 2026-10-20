# Research conversation: Search the web for recent (2024-2025) papers on constrained decoding for information extraction and schema-guided relati

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac9fd08629cd2c59a.jsonl`
- **Structured JSON:** [`f9cca0c9b55c2ce0209a.json`](../../sessions/f9/f9cca0c9b55c2ce0209a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

18 recorded events

### User

_source line 1 · 2026-05-23T22:58:44.256Z_

Search the web for recent (2024-2025) papers on constrained decoding for information extraction and schema-guided relation extraction. I need to check if there are important papers we might be missing in our Related Work section.

Do TWO web searches:
1. "constrained decoding information extraction 2024 2025"
2. "schema-guided relation extraction 2024 2025"

Our paper (OntoCoDec) already cites these 2024-2025 works:
- XGrammar (2025), SynCode (2024), SGLang (2024)
- KG-Trie (Luo 2025), PLDI 2025 type-constrained codegen (Mündler et al.)
- GoLLIE (Sainz 2024), KnowCoder (Li 2024), ADELIE (Qi 2024)
- GCD (Geng 2023), BoostCD (2025)
- EnriCo (Zaratiana 2024), IterGen (Ugare 2025)
- ODKE+ (Khorshidi 2025), OntoLogX (2025), RELATE (Olasunkanmi 2025)
- Zhou 2026 ontology-to-tools, Ekaw 2024 ontology beam
- CRANE (Banerjee 2025), Schall 2025 hidden cost, Zhou 2026 snowballing
- Tam 2024 let me speak, JSONSchemaBench (2025), GuidEx (2025)
- Vukovic 2024 dialogue RE with ontology constraints
- GuidEx (2025), UniversalNER (Zhou 2024)

Report back with:
1. Any notable 2024-2025 papers NOT in our list above that are directly relevant (constrained decoding + IE, or schema-guided RE)
2. For each found paper: title, authors, venue, and one-line description of relevance
3. Your assessment: are any of these critical omissions, or is our coverage adequate?

Keep response under 400 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "96db1024-ae2d-439a-af35-2dfb20088752",
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

_source line 2 · 2026-05-23T22:58:44.264Z_

```json
{
  "parentUuid": "96db1024-ae2d-439a-af35-2dfb20088752",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
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
  "uuid": "ce74a5f2-1f96-43c9-9520-e4671c0b836f",
  "timestamp": "2026-05-23T22:58:44.264Z",
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

_source line 3 · 2026-05-23T22:58:46.854Z_



I'll search for recent papers on both topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce74a5f2-1f96-43c9-9520-e4671c0b836f",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL49DUEX6FCaUTd7GmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45262d9b-eb42-4330-b626-a338be5d195f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTxKsSpz97JnxuG1Wjj3nt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29898,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29898,
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

_source line 4 · 2026-05-23T22:58:47.444Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014AUgZw8a59Q2uTyZRFwY23`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45262d9b-eb42-4330-b626-a338be5d195f",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL49DUEX6FCaUTd7GmQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4a5a7f7-1c23-4555-990c-9ff0b2e50e2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BTxKsSpz97JnxuG1Wjj3nt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29898,
      "cache_read_input_tokens": 0,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29898
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 29898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29898,
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

_source line 5 · 2026-05-23T22:58:47.449Z_

<details><summary>↩ Tool result · `toolu_014AUgZw8a59Q2uTyZRFwY23`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4a5a7f7-1c23-4555-990c-9ff0b2e50e2a",
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "ac90b3b9-06c7-4ca5-9ebb-9d64b373f411",
  "sourceToolAssistantUUID": "b4a5a7f7-1c23-4555-990c-9ff0b2e50e2a",
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

_source line 6 · 2026-05-23T22:58:50.086Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011kgbR5x7ueMqvDSomHPKPD`</summary>

```json
{
  "query": "constrained decoding information extraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac90b3b9-06c7-4ca5-9ebb-9d64b373f411",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL4P1ggEtxPhxxkVs87",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebbaa860-9363-4678-b4d7-c7131ee00521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BECZqhdgZPuZcqjfJ3HmGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 29898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

### Tool call

_source line 7 · 2026-05-23T22:58:50.432Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MkN7tMNZj7VZJT74h4urbb`</summary>

```json
{
  "query": "schema-guided relation extraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebbaa860-9363-4678-b4d7-c7131ee00521",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL4P1ggEtxPhxxkVs87",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "696822e0-bbfc-4e16-be49-c2db0b9a4dc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BECZqhdgZPuZcqjfJ3HmGU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 29898,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 29898,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 8 · 2026-05-23T22:58:57.689Z_

<details><summary>↩ Tool result · `toolu_01MkN7tMNZj7VZJT74h4urbb`</summary>

```text
Web search results for query: "schema-guided relation extraction 2024 2025"

Links: [{"title":"Published as a conference paper at ICAIS 2025","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"},{"title":"Adaptive Schema-aware Event Extraction with Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.419.pdf"},{"title":"Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation","url":"https://arxiv.org/html/2502.12737v3"},{"title":"[2412.20005] OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://arxiv.org/abs/2412.20005"},{"title":"A Few-Shot Approach for Relation Extraction Domain Adaptation using Large Language Models","url":"https://arxiv.org/pdf/2408.02377"},{"title":"LexRel: Benchmarking Legal Relation Extraction for Chinese Civil Cases","url":"https://arxiv.org/pdf/2512.12643"}]

Based on the search results, here are some key findings on schema-guided relation extraction in 2024-2025:

## Recent Approaches and Frameworks

The KARMA framework (Lu & Wang, 2025) adopts a multi-agent architecture, in which each agent executes schema-guided extraction tasks to guarantee accurate entity normalization and relation classification within a fixed ontological boundary.

OneKE is a dockerized schema-guided knowledge extraction system, which can extract knowledge from the Web and raw PDF Books, and support various domains (science, news, etc.).

## Few-Shot and LLM-Based Methods

Recent work leverages LLMs to generate explanation-driven knowledge and schema-constrained synthetic data, implementing a two-stage knowledge-guided pre-training framework to enhance the model's ability to understand relational structures and contextual dependencies.

Schema information is combined with few-shot examples prompts to elicit LLMs' comprehension of the relation extraction task.

## Specialized Applications

The ASEE (Adaptive Schema-aware Event Extraction) architecture comprises two primary components: Schema Paraphrasing (SP) and Schema-Retrieval Augmented Generation (SRAG, including Schema Retrieval and Schema-aware Extraction).

A comprehensive schema to model legal relations in Chinese civil law has been presented, addressing the underexplored area of legal relation extraction.

These developments show a trend toward using LLMs in conjunction with predefined schemas for more accurate and interpretable extraction tasks across various domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "696822e0-bbfc-4e16-be49-c2db0b9a4dc0",
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "6790524f-1ad6-493d-a41c-6df95c954533",
  "sourceToolAssistantUUID": "696822e0-bbfc-4e16-be49-c2db0b9a4dc0",
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

### Tool result

_source line 9 · 2026-05-23T22:58:58.256Z_

<details><summary>↩ Tool result · `toolu_011kgbR5x7ueMqvDSomHPKPD`</summary>

```text
Web search results for query: "constrained decoding information extraction 2024 2025"

Links: [{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/pdf/2506.14901"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"How Structured Outputs and Constrained Decoding Work | Let's Data Science","url":"https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"}]

I found relevant results on constrained decoding for information extraction from 2024-2025. Here's a summary:

## Recent Developments in Constrained Decoding for Information Extraction

In structured information extraction, there are typically semantic and syntactic constraints on the output of IE systems, which standard encoder-decoder architectures cannot guarantee. This has led to the development of constrained decoding approaches that allow specifying constraints in form of context-free grammars.

### Types of Constraints

Tries enable step-wise restriction to only those outputs that can continue towards a valid sequence, for example, quadruple formats in ACOS sentiment tasks. For tasks such as program slicing, constraints may enforce that only tokens from the input are produced (lexical), or the sequence of outputs remains a monotonic subsequence in terms of abstract syntax tree similarity (syntactic/TSED monotonicity).

### Recent Approaches and Tools

A schema enforcement phase occurred from 2024 to 2025, with OpenAI releasing Structured Outputs in August 2024 with response_format: { type: "json_schema" }, and Google Gemini adding response_schema at Google I/O in May 2024.

BoostCD is a recent approach that applies the base model twice on input (unconstrained and constrained), then combines the two resulting weak predictions using a boosted model that learns to undo mistakes made by the base model.

### Current Challenges

Constrained decoding guarantees syntactic validity but not semantic correctness; the values in JSON may be wrong, hallucinated, or low-quality even when the structure is perfect.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebbaa860-9363-4678-b4d7-c7131ee00521",
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "cd9555f0-25c6-40a9-8643-99f17d343b67",
  "sourceToolAssistantUUID": "ebbaa860-9363-4678-b4d7-c7131ee00521",
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

_source line 10 · 2026-05-23T22:59:00.622Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QKsLyjg7sCDw84L31MGrqQ`</summary>

```json
{
  "query": "OneKE schema-guided knowledge extraction 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9555f0-25c6-40a9-8643-99f17d343b67",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL5AyAX36Ert2t4UVtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfdfc7e0-0f04-492c-b6d5-e040079b4a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALL8chK6T3g3bVaWiDPQcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 695,
      "cache_creation_input_tokens": 989,
      "cache_read_input_tokens": 31349,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 989,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 11 · 2026-05-23T22:59:01.015Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cz4inaEvQjVQRFCR5gy1ZV`</summary>

```json
{
  "query": "grammar constrained decoding clinical NER structured extraction 2024 frontiers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfdfc7e0-0f04-492c-b6d5-e040079b4a64",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL5AyAX36Ert2t4UVtj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b11cf193-bb84-42e8-868b-76e48d12a7ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALL8chK6T3g3bVaWiDPQcC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 695,
      "cache_creation_input_tokens": 989,
      "cache_read_input_tokens": 31349,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 989
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 695,
          "output_tokens": 115,
          "cache_read_input_tokens": 31349,
          "cache_creation_input_tokens": 989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 989,
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

_source line 12 · 2026-05-23T22:59:07.474Z_

<details><summary>↩ Tool result · `toolu_01QKsLyjg7sCDw84L31MGrqQ`</summary>

```text
Web search results for query: "OneKE schema-guided knowledge extraction 2024 arxiv"

Links: [{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/oneke-dockerized-schema-guided-llm-agent-based"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241220005L/abstract"},{"title":"Paper page - OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://huggingface.co/papers/2412.20005"},{"title":"[2412.20005] OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://arxiv.org/abs/2412.20005"},{"title":"[PDF] OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OneKE:-A-Dockerized-Schema-Guided-LLM-Agent-based-Luo-Ru/0b4206ee29e10f6e2156a66b0419f0e18fa13e63"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://arxiv.org/html/2412.20005v2"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://www.researchgate.net/publication/387539869_OneKE_A_Dockerized_Schema-Guided_LLM_Agent-based_Knowledge_Extraction_System"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction   System","url":"https://arxiv.org/pdf/2412.20005"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"},{"title":"(PDF) ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://www.researchgate.net/publication/395338944_ODKE_Ontology-Guided_Open-Domain_Knowledge_Extraction_with_LLMs"}]

Based on the search results, I found comprehensive information about OneKE:

## OneKE: Schema-Guided Knowledge Extraction System

OneKE is a dockerized schema-guided knowledge extraction system that can extract knowledge from the Web and raw PDF Books, and support various domains (science, news, etc.)

### System Architecture

OneKE is designed with multiple agents and a configurable knowledge base. Different agents perform their respective roles, enabling support for various extraction scenarios. The configurable knowledge base facilitates schema configuration, error case debugging and correction, further improving the performance.

The system includes three agents: Schema Agent for schema analysis with various data types, Extraction Agent for extracting knowledge with various LLMs, and Reflection Agent to debug and handle erroneous cases.

### Capabilities and Evaluation

Empirical evaluations on benchmark datasets demonstrate OneKE's efficacy, while case studies further elucidate its adaptability to diverse tasks across multiple domains, highlighting its potential for broad applications.

### Publication and Resources

The paper was published on 12/31/2024 (arxiv 2412.20005), and the code has been open-sourced at https://github.com/zjunlp/OneKE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfdfc7e0-0f04-492c-b6d5-e040079b4a64",
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "a8b02a76-202a-43d5-8644-ca6a6b095016",
  "sourceToolAssistantUUID": "bfdfc7e0-0f04-492c-b6d5-e040079b4a64",
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

### Tool result

_source line 13 · 2026-05-23T22:59:08.388Z_

<details><summary>↩ Tool result · `toolu_01Cz4inaEvQjVQRFCR5gy1ZV`</summary>

```text
Web search results for query: "grammar constrained decoding clinical NER structured extraction 2024 frontiers"

Links: [{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"[PDF] Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Grammar-Constrained-Decoding-for-Structured-NLP-Geng-Josifosky/7e269bfabb451765a16ca0357de6b497cefb60bf"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11747381/"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning | Request PDF","url":"https://www.researchgate.net/publication/376402267_Grammar-Constrained_Decoding_for_Structured_NLP_Tasks_without_Finetuning"}]

I found relevant research on this topic. Here are the key findings:

## Grammar-Constrained Decoding for Clinical Information Extraction

A recent study published in Frontiers in Artificial Intelligence (2025) by Schmidt and Cimiano from Bielefeld University investigates grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts.

### Key Research Focus

The research addresses the open question of how far an information extraction system can be effectively guided by a domain-specific grammar to ensure that the output structures follow the requirements of a certain domain data model.

### Methods

The work experimentally investigates the influence of grammar-constrained decoding as well as pointer generators on the performance of a domain-specific information extraction system, considering fine-tuned encoder-decoder models like Longformer and Flan-T5. The task involves inducing structured representations from abstracts describing clinical trials, relying on the C-TrO ontology.

### Core Approach

Grammar-constrained decoding approaches ensure that the decoded structure follows the production rules of a given semantic grammar.

### Significance

This work investigates the impact of grammar-constrained decoding in a fine-tuning setting, particularly on the task of structured information extraction focusing on low-resource settings, which had not been investigated before.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b11cf193-bb84-42e8-868b-76e48d12a7ed",
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "507f8230-e3f0-489c-87ff-ef567e8fca0f",
  "sourceToolAssistantUUID": "b11cf193-bb84-42e8-868b-76e48d12a7ed",
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

_source line 14 · 2026-05-23T22:59:12.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NDXsSJrujyWCZQDUpKBemo`</summary>

```json
{
  "query": "KARMA multi-agent schema knowledge extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "507f8230-e3f0-489c-87ff-ef567e8fca0f",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL5vH9fqrUAq9AKGKZX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84e7930b-2c4c-4eeb-9a51-3b45acd85fef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kkw9hKnmexpk3KicPXnAYT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2545,
      "cache_read_input_tokens": 32338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2545,
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

### Tool call

_source line 15 · 2026-05-23T22:59:12.372Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DQxcgzJXXy1LRDxj3Sf7Q8`</summary>

```json
{
  "query": "ASEE adaptive schema-aware event extraction 2025 EMNLP findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84e7930b-2c4c-4eeb-9a51-3b45acd85fef",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL5vH9fqrUAq9AKGKZX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19011c5d-95b6-40b7-a1ae-ae9d14f1e46a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kkw9hKnmexpk3KicPXnAYT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2545,
      "cache_read_input_tokens": 32338,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2545
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 32338,
          "cache_creation_input_tokens": 2545,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2545,
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

_source line 16 · 2026-05-23T22:59:17.017Z_

<details><summary>↩ Tool result · `toolu_01NDXsSJrujyWCZQDUpKBemo`</summary>

```text
Web search results for query: "KARMA multi-agent schema knowledge extraction 2025"

Links: [{"title":"KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment | OpenReview","url":"https://openreview.net/forum?id=k0wyi4cOGy"},{"title":"KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment","url":"https://arxiv.org/pdf/2502.06472"},{"title":"GitHub - YuxingLu613/KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment","url":"https://github.com/YuxingLu613/KARMA"},{"title":"(PDF) KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment","url":"https://www.researchgate.net/publication/388884012_KARMA_Leveraging_Multi-Agent_LLMs_for_Automated_Knowledge_Graph_Enrichment"},{"title":"NeurIPS Poster KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment","url":"https://neurips.cc/virtual/2025/poster/116417"},{"title":"KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment | GraphRAG","url":"https://graphrag.com/appendices/research/2502.06472/"},{"title":"Paper page - KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment","url":"https://huggingface.co/papers/2502.06472"},{"title":"[2502.06472v1] KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment","url":"https://arxiv.org/abs/2502.06472v1"},{"title":"[2502.06472] KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment","url":"https://arxiv.org/abs/2502.06472"},{"title":"Building a Multi-Agent System for Knowledge Graph Enrichment: Implementing KARMA | atal upadhyay","url":"https://atalupadhyay.wordpress.com/2025/03/12/building-a-multi-agent-system-for-knowledge-graph-enrichment-implementing-karma/"}]

Based on the search results, here's what I found about KARMA:

## Overview

KARMA is a multi-agent LLM framework that automatically updates and expands knowledge graphs from scientific papers. The framework employs multi-agent large language models (LLMs) to automate KG enrichment through structured analysis of unstructured text.

## Key Architecture

The approach employs nine collaborative agents, spanning entity discovery, relation extraction, schema alignment, and conflict resolution that iteratively parse documents, verify extracted knowledge, and integrate it into existing graph structures while adhering to domain-specific schema.

## Specific Agent Functions

The nine agents include: document retrieval, filtering, summarization, entity extraction, relationship extraction, schema alignment, conflict resolution, evaluation, and a central controller.

## Performance Results

Experiments on 1,200 PubMed articles from three different domains demonstrate the effectiveness of KARMA in knowledge graph enrichment, with the identification of up to 38,230 new entities while achieving 83.1% LLM-verified correctness and reducing conflict edges by 18.6% through multi-layer assessments.

## Publication

KARMA was published on September 18, 2025, as a NeurIPS 2025 spotlight paper. The work is available on arXiv and has an open-source implementation on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84e7930b-2c4c-4eeb-9a51-3b45acd85fef",
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "f501f502-0b3b-4a85-8456-f5332237de6c",
  "sourceToolAssistantUUID": "84e7930b-2c4c-4eeb-9a51-3b45acd85fef",
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

### Tool result

_source line 17 · 2026-05-23T22:59:19.508Z_

<details><summary>↩ Tool result · `toolu_01DQxcgzJXXy1LRDxj3Sf7Q8`</summary>

```text
Web search results for query: "ASEE adaptive schema-aware event extraction 2025 EMNLP findings"

Links: [{"title":"Adaptive Schema-aware Event Extraction with Retrieval- ...","url":"https://aclanthology.org/2025.findings-emnlp.419.pdf"},{"title":"[2505.08690v1] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.08690v1"},{"title":"[2505.08690] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.08690"},{"title":"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.08690"},{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/html/2505.14992"},{"title":"Effective and Efficient Schema-aware Information ...","url":"https://www.arxiv.org/pdf/2505.14992"},{"title":"[Literature Review] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://www.themoonlight.io/en/review/adaptive-schema-aware-event-extraction-with-retrieval-augmented-generation"},{"title":"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.08690v1"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"}]

Based on the search results, I found detailed information about the ASEE (Adaptive Schema-aware Event Extraction) paper from EMNLP 2025 Findings.

## Overview

ASEE is a novel paradigm combining schema paraphrasing with schema retrieval-augmented generation. The paper was authored by Sheng Liang, Hang Lv, Zhihao Wen, Yaxiong Wu, Yongyue Zhang, Hao Wang, and Yong Liu.

## Key Problem Addressed

Event extraction is a fundamental task in NLP that involves identifying and extracting event information from unstructured text, requiring two key steps: selecting appropriate schemas from hundreds of candidates and executing the extraction process. Although large language models offer potential solutions, their schema hallucination tendencies and context window limitations pose challenges for practical deployment.

## Approach

The architecture of ASEE comprises two primary components: Schema Paraphrasing (SP) and Schema-Retrieval Augmented Generation (SRAG, including Schema Retrieval (SR) and Schema-aware Extraction (SE)).

## Evaluation and Results

To facilitate rigorous evaluation, the authors constructed the Multi-Dimensional Schema-aware Event Extraction (MD-SEE) benchmark, which systematically consolidates 12 datasets across diverse domains, complexity levels, and language settings. Extensive evaluations on MD-SEE show that ASEE demonstrates strong adaptability across various scenarios, significantly improving the accuracy of event extraction.

The paper was published in Findings of the Association for Computational Linguistics: EMNLP 2025 on November 4-9, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19011c5d-95b6-40b7-a1ae-ae9d14f1e46a",
  "isSidechain": true,
  "promptId": "091a8fb8-bce6-44a2-b686-9016cb2f4742",
  "agentId": "ac9fd08629cd2c59a",
  "type": "user",
  "uuid": "a7e48816-9f75-4250-82c7-63198199e4b9",
  "sourceToolAssistantUUID": "19011c5d-95b6-40b7-a1ae-ae9d14f1e46a",
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

_source line 18 · 2026-05-23T22:59:39.155Z_

Based on the two searches, here are the findings:

## Papers NOT in our citation list that are potentially relevant

1. **OneKE** (Luo et al., Dec 2024, arXiv 2412.20005) — Dockerized schema-guided LLM agent system for knowledge extraction with Schema/Extraction/Reflection agents. Multi-domain, open-sourced by ZJUNLP. **Moderate relevance** — schema-guided IE system but agent-based, not constrained decoding.

2. **Schmidt & Cimiano (Frontiers in AI, 2025)** — Grammar-constrained decoding for structured IE on clinical trial abstracts using fine-tuned encoder-decoder models (Longformer, Flan-T5) with domain-specific grammars. **High relevance** — directly studies grammar-constrained decoding for IE in a fine-tuning setting, complementary to our zero/few-shot focus.

3. **ASEE** (Liang et al., EMNLP 2025 Findings) — Adaptive Schema-aware Event Extraction with retrieval-augmented generation; addresses schema hallucination via schema paraphrasing + retrieval. **Moderate relevance** — schema-aware extraction but RAG-based, not constrained decoding.

4. **KARMA** (Lu & Wang, NeurIPS 2025) — Multi-agent LLMs for KG enrichment with schema alignment agents. **Low relevance** — KG enrichment focus, tangential to our constrained decoding angle.

5. **Effective and Efficient Schema-aware IE Using On-Device LLMs** (arXiv 2505.14992, May 2025) — Schema-aware IE optimized for on-device LLMs. **Moderate relevance** — schema-aware IE but efficiency-focused.

## Assessment

Coverage is **adequate**. The one paper worth considering adding is **Schmidt & Cimiano (2025)** — it's the most directly relevant omission as it explicitly studies grammar-constrained decoding for structured IE tasks, which is core to our narrative. OneKE could merit a brief mention in the schema-guided IE paragraph as a concurrent system-level approach. The others (ASEE, KARMA) are tangential enough to safely omit.

No critical omissions found.

Sources:
- [Schmidt & Cimiano - Grammar-constrained decoding for structured IE](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full)
- [OneKE - Schema-Guided LLM Agent-based KE](https://arxiv.org/abs/2412.20005)
- [ASEE - Adaptive Schema-aware Event Extraction](https://arxiv.org/abs/2505.08690)
- [KARMA - Multi-Agent LLMs for KG Enrichment](https://arxiv.org/abs/2502.06472)
- [Schema-aware IE on On-Device LLMs](https://arxiv.org/abs/2505.14992)
- [Awesome LLM Constrained Decoding survey list](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7e48816-9f75-4250-82c7-63198199e4b9",
  "isSidechain": true,
  "agentId": "ac9fd08629cd2c59a",
  "requestId": "req_011CbLL6jq8WrXN2iYA5udwr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06d2a8e3-e7fc-4d52-9351-a60388e6a8a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/.claude/sessions/agent_f7c2f8cc",
  "sessionId": "d74ed321-94ae-476c-899f-c11688aa3239",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jiggly-watching-nygaard",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN7JoEiSNdJg2h9D2xoEYn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 34883,
      "output_tokens": 771,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 771,
          "cache_read_input_tokens": 34883,
          "cache_creation_input_tokens": 1860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1860,
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
