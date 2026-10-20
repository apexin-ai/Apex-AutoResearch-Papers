# Research conversation: I need to understand why the distill system can't find papers in `literature_map.yaml`. The distill system (`/home/ubunt

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad4e80c544ab4527c.jsonl`
- **Structured JSON:** [`d2502bcda8dbdbfe4832.json`](../../sessions/d2/d2502bcda8dbdbfe4832.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-20T14:17:17.773Z_

I need to understand why the distill system can't find papers in `literature_map.yaml`. 

The distill system (`/home/ubuntu/agent-ml-research/core/tools/distill.py`) at line 155 does `raw_papers = lit_map.get("papers") or {}`. But even after writing a correctly formatted file at `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/literature_map.yaml`, the distill shows `literature_map_total: 0`.

I need to find:
1. The `_read_map` function in `core/tools/literature.py` — how does it parse the YAML? What does it return?
2. The `get_literature_map_path` function — what path does it expect the file to be at?
3. Is there an `add_to_literature_map` function/tool that does something special beyond just writing YAML?
4. How does `get_distill_status` count `literature_map_total`?

Search broadly in `/home/ubuntu/agent-ml-research/core/tools/` for literature map related code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "0d4da516-40ad-4c78-a37d-22a367d54ec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T14:17:19.747Z_

I'll search systematically through the agent-ml-research tools directory to understand the literature map system and how it counts papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d4da516-40ad-4c78-a37d-22a367d54ec8",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxs9ESAt6kaDmSfuPSn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1b14b775-11f6-43bd-8d4d-3a4eabe87ffd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011L4YxwhGbv8hP7aTzCvqvh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37434,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37434,
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

_source line 3 · 2026-05-20T14:17:20.238Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FatbHf3xPemz9CozFHRRRL`</summary>

```json
{
  "pattern": "/home/ubuntu/agent-ml-research/core/tools/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b14b775-11f6-43bd-8d4d-3a4eabe87ffd",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxs9ESAt6kaDmSfuPSn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d01e7b81-a353-423c-8020-755802c8ea75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011L4YxwhGbv8hP7aTzCvqvh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37434,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37434,
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

### Tool result

_source line 4 · 2026-05-20T14:17:20.260Z_

<details><summary>↩ Tool result · `toolu_01FatbHf3xPemz9CozFHRRRL`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/__init__.py
/home/ubuntu/agent-ml-research/core/tools/account_login.py
/home/ubuntu/agent-ml-research/core/tools/clone_repo.py
/home/ubuntu/agent-ml-research/core/tools/agent_tools.py
/home/ubuntu/agent-ml-research/core/tools/artifacts.py
/home/ubuntu/agent-ml-research/core/tools/email_tokens_store.py
/home/ubuntu/agent-ml-research/core/tools/execution_backends/__init__.py
/home/ubuntu/agent-ml-research/core/tools/execution_backends/slurm_backend.py
/home/ubuntu/agent-ml-research/core/tools/execution_backends/base.py
/home/ubuntu/agent-ml-research/core/tools/external_review.py
/home/ubuntu/agent-ml-research/core/tools/execution_backends/tmux_backend.py
/home/ubuntu/agent-ml-research/core/tools/gpu_allocator.py
/home/ubuntu/agent-ml-research/core/tools/manager_msg.py
/home/ubuntu/agent-ml-research/core/tools/image_tools.py
/home/ubuntu/agent-ml-research/core/tools/model_registry.py
/home/ubuntu/agent-ml-research/core/tools/pai_eas.py
/home/ubuntu/agent-ml-research/core/tools/oss_backup.py
/home/ubuntu/agent-ml-research/core/tools/narrative_render.py
/home/ubuntu/agent-ml-research/core/tools/narrative_scene.py
/home/ubuntu/agent-ml-research/core/tools/reference_checker.py
/home/ubuntu/agent-ml-research/core/tools/project_docs.py
/home/ubuntu/agent-ml-research/core/tools/provenance.py
/home/ubuntu/agent-ml-research/core/tools/result.py
/home/ubuntu/agent-ml-research/core/tools/s3_backup.py
/home/ubuntu/agent-ml-research/core/tools/wandb_client.py
/home/ubuntu/agent-ml-research/core/tools/verification_guide.py
/home/ubuntu/agent-ml-research/core/tools/risk.py
/home/ubuntu/agent-ml-research/core/tools/secrets.py
/home/ubuntu/agent-ml-research/core/tools/workspace.py
/home/ubuntu/agent-ml-research/core/tools/experiment_plan.py
/home/ubuntu/agent-ml-research/core/tools/experiment_matrix.py
/home/ubuntu/agent-ml-research/core/tools/paper_consistency.py
/home/ubuntu/agent-ml-research/core/tools/paper_checklist.py
/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py
/home/ubuntu/agent-ml-research/core/tools/dream_card.py
/home/ubuntu/agent-ml-research/core/tools/dream_runner.py
/home/ubuntu/agent-ml-research/core/tools/constraints.py
/home/ubuntu/agent-ml-research/core/tools/ssh.py
/home/ubuntu/agent-ml-research/core/tools/project_setup.py
/home/ubuntu/agent-ml-research/core/tools/architecture.py
/home/ubuntu/agent-ml-research/core/tools/disk_monitor.py
/home/ubuntu/agent-ml-research/core/tools/cron.py
/home/ubuntu/agent-ml-research/core/tools/gpu_monitor.py
/home/ubuntu/agent-ml-research/core/tools/report_facts.py
/home/ubuntu/agent-ml-research/core/tools/registry.py
/home/ubuntu/agent-ml-research/core/tools/rules_config.py
/home/ubuntu/agent-ml-research/core/tools/roadmap.py
/home/ubuntu/agent-ml-research/core/tools/worker.py
/home/ubuntu/agent-ml-research/core/tools/distill_callbacks.py
/home/ubuntu/agent-ml-research/core/tools/dream.py
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/core/tools/project_config.py
/home/ubuntu/agent-ml-research/core/tools/file_parser.py
/home/ubuntu/agent-ml-research/core/tools/distill_card.py
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py
/home/ubuntu/agent-ml-research/core/tools/feishu.py
/home/ubuntu/agent-ml-research/core/tools/paper_audit_card.py
/home/ubuntu/agent-ml-research/core/tools/visual_check.py
/home/ubuntu/agent-ml-research/core/tools/paper_audit.py
/home/ubuntu/agent-ml-research/core/tools/distill.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d01e7b81-a353-423c-8020-755802c8ea75",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "e0ac680a-408e-4fea-be0b-06ea22f98d65",
  "sourceToolAssistantUUID": "d01e7b81-a353-423c-8020-755802c8ea75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T14:17:20.382Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AHm9M4PX8o5iArexXLt4uv`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/core/tools -name \"*.py\" -type f | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0ac680a-408e-4fea-be0b-06ea22f98d65",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxs9ESAt6kaDmSfuPSn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bff64d00-f708-4762-8a97-ddb36b309697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011L4YxwhGbv8hP7aTzCvqvh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37434,
      "cache_read_input_tokens": 0,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37434
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 156,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 37434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37434,
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

_source line 6 · 2026-05-20T14:17:20.456Z_

<details><summary>↩ Tool result · `toolu_01AHm9M4PX8o5iArexXLt4uv`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/reference_checker.py
/home/ubuntu/agent-ml-research/core/tools/feishu_group.py
/home/ubuntu/agent-ml-research/core/tools/feishu.py
/home/ubuntu/agent-ml-research/core/tools/s3_backup.py
/home/ubuntu/agent-ml-research/core/tools/paper_consistency.py
/home/ubuntu/agent-ml-research/core/tools/wandb_client.py
/home/ubuntu/agent-ml-research/core/tools/gpu_monitor.py
/home/ubuntu/agent-ml-research/core/tools/gpu_allocator.py
/home/ubuntu/agent-ml-research/core/tools/paper_checklist.py
/home/ubuntu/agent-ml-research/core/tools/experiment_plan.py
/home/ubuntu/agent-ml-research/core/tools/distill.py
/home/ubuntu/agent-ml-research/core/tools/project_docs.py
/home/ubuntu/agent-ml-research/core/tools/pai_eas.py
/home/ubuntu/agent-ml-research/core/tools/report_facts.py
/home/ubuntu/agent-ml-research/core/tools/registry.py
/home/ubuntu/agent-ml-research/core/tools/manager_msg.py
/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py
/home/ubuntu/agent-ml-research/core/tools/rules_config.py
/home/ubuntu/agent-ml-research/core/tools/verification_guide.py
/home/ubuntu/agent-ml-research/core/tools/worker.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bff64d00-f708-4762-8a97-ddb36b309697",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "a3fcaf31-7570-4a0a-b7c7-06fa3509480b",
  "sourceToolAssistantUUID": "bff64d00-f708-4762-8a97-ddb36b309697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-20T14:17:21.760Z_

Now let me search for the literature map functions you mentioned:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3fcaf31-7570-4a0a-b7c7-06fa3509480b",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxsL7n7Fnabyh9YF1MQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "adbb057b-806a-42fb-a4c7-4e1d88beff15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPLm9aXseYvTbaixpN7S6P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 37434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2727,
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

_source line 8 · 2026-05-20T14:17:22.673Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011Jf3wxxXJef2VGxP7MVkw3`</summary>

```json
{
  "pattern": "_read_map|get_literature_map_path|add_to_literature_map",
  "path": "/home/ubuntu/agent-ml-research/core/tools",
  "type": "py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adbb057b-806a-42fb-a4c7-4e1d88beff15",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxsL7n7Fnabyh9YF1MQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b5943e47-b963-4ee2-93f4-354b2c9aa21c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPLm9aXseYvTbaixpN7S6P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 37434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2727,
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

_source line 9 · 2026-05-20T14:17:22.704Z_

<details><summary>↩ Tool result · `toolu_011Jf3wxxXJef2VGxP7MVkw3`</summary>

```text
Found 3 files
/home/ubuntu/agent-ml-research/core/tools/distill.py
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5943e47-b963-4ee2-93f4-354b2c9aa21c",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "298442ca-fbe7-4bfa-8c81-3b30090f84d2",
  "sourceToolAssistantUUID": "b5943e47-b963-4ee2-93f4-354b2c9aa21c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T14:17:22.818Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KaG5SNL61WeB4rcMBYRs7X`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/literature.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "298442ca-fbe7-4bfa-8c81-3b30090f84d2",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxsL7n7Fnabyh9YF1MQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0eaf7674-66f1-4dc4-9429-94794a7c3b4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPLm9aXseYvTbaixpN7S6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 37434,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2727
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 238,
          "cache_read_input_tokens": 37434,
          "cache_creation_input_tokens": 2727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2727,
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

_source line 11 · 2026-05-20T14:17:22.834Z_

<details><summary>↩ Tool result · `toolu_01KaG5SNL61WeB4rcMBYRs7X`</summary>

```text
1	"""Literature map — persistent, cross-stage knowledge base of papers.
2	
3	The literature_map.yaml is the single source of truth for papers a project
4	accumulates across the Idea → Research → Writing → Review pipeline. Each
5	entry is verified (or marked unverified) and carries enough metadata to
6	generate BibTeX entries and to drive Related Work / citation gap-fill in
7	the Paper Agent's writing pipeline.
8	
9	Two scopes:
10	
11	  - Project-level: ``projects/{project}/literature_map.yaml``
12	      Used during Research and Writing phases.
13	
14	  - Global (Idea phase): ``{WORKSPACE_ROOT}/literature_map.yaml``
15	      Used before a project exists. Each entry carries ``source_idea_id`` so
16	      multiple ideas can coexist. On project creation, matching entries are
17	      seeded into the project map.
18	
19	Design notes:
20	
21	  - Read paths support modes (summary / category:X / competitors / unverified
22	    / bib / full) so day-to-day reads stay token-cheap even when the map has
23	    grown to 40-60 papers.
24	
25	  - Writes hold an exclusive flock + use atomic temp→rename, modeled on
26	    ``core/tools/registry.py`` so the file never tears under concurrent
27	    Worker writes.
28	
29	  - Dedup happens on add: DOI exact match wins; otherwise normalized title
30	    match. Existing entries are merged (new fields fill empty existing
31	    fields) rather than overwritten.
32	"""
33	
34	from __future__ import annotations
35	
36	import fcntl
37	import logging
38	import os
39	import re
40	import tempfile
41	import unicodedata
42	from pathlib import Path
43	from typing import Any, Iterable
44	
45	import yaml
46	
47	from core import paths as _paths
48	from core.tools.result import ToolResult
49	
50	logger = logging.getLogger(__name__)
51	
52	
53	# ---------------------------------------------------------------------------
54	# Constants
55	# ---------------------------------------------------------------------------
56	
57	# Roles a paper can play relative to the project. Used by Related Work drafting
58	# (foundation papers anchor narratives; direct-competitor papers must be cited).
59	VALID_ROLES: frozenset[str] = frozenset(
60	    {"foundation", "direct-competitor", "method-component", "evaluation", "background"}
61	)
62	
63	# Modes for read_literature_map — keep token usage proportional to need.
64	VALID_READ_MODES: frozenset[str] = frozenset(
65	    {"summary", "competitors", "unverified", "bib", "full"}
66	)
67	
68	# Fields kept in summary mode (skips long fields like abstract, relevance).
69	_SUMMARY_FIELDS: tuple[str, ...] = (
70	    "title", "year", "venue", "category", "role", "verified", "bibtex_key",
71	)
72	
73	
74	# ---------------------------------------------------------------------------
75	# Path resolution
76	# ---------------------------------------------------------------------------
77	
78	def get_literature_map_path(project: str | None = None) -> Path:
79	    """Resolve the literature_map.yaml path.
80	
81	    Project name → ``projects/{project}/literature_map.yaml`` (V3 layout).
82	    No project   → ``{WORKSPACE_ROOT}/literature_map.yaml`` (global, idea phase).
83	    """
84	    if project:
85	        p = _paths.resolve_project_file(project, "literature_map.yaml")
86	        p.parent.mkdir(parents=True, exist_ok=True)
87	        return p
88	    return _paths.global_literature_map_path()
89	
90	
91	# ---------------------------------------------------------------------------
92	# Atomic file I/O — modeled on registry._read_modify_write_registry
93	# ---------------------------------------------------------------------------
94	
95	def _empty_map() -> dict:
96	    return {
97	        "meta": {"last_updated": None, "total_papers": 0},
98	        "categories": [],
99	        "papers": {},
100	    }
101	
102	
103	def _read_map(path: Path) -> dict:
104	    """Read literature_map.yaml without a lock (atomic single-syscall read).
105	
106	    Returns a fresh empty skeleton if the file doesn't exist or is unreadable.
107	    Writers use exclusive flock + atomic rename so readers always see a
108	    consistent snapshot.
109	    """
110	    if not path.exists():
111	        return _empty_map()
112	    try:
113	        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
114	    except Exception:
115	        logger.warning("Failed to parse literature_map at %s", path, exc_info=True)
116	        return _empty_map()
117	    if isinstance(data, list):
118	        data = {"papers": data, "meta": {}, "categories": []}
119	    elif not isinstance(data, dict):
120	        logger.warning("literature_map at %s is %s, expected dict — resetting", path, type(data).__name__)
121	        return _empty_map()
122	    data.setdefault("meta", {})
123	    data["meta"].setdefault("last_updated", None)
124	    data["meta"].setdefault("total_papers", 0)
125	    data.setdefault("categories", [])
126	    data.setdefault("papers", {})
127	    return data
128	
129	
130	def _read_modify_write(path: Path, modifier) -> dict:
131	    """Read, apply ``modifier(data)`` in place, atomically write back.
132	
133	    Holds LOCK_EX on a sibling .lock file (not the data file — atomic rename
134	    swaps the inode and would invalidate locks held on it).
135	    """
136	    path.parent.mkdir(parents=True, exist_ok=True)
137	    lock_path = path.with_suffix(".lock")
138	
139	    with open(lock_path, "a+") as lock_f:
140	        fcntl.flock(lock_f, fcntl.LOCK_EX)
141	        try:
142	            data = _read_map(path)
143	            modifier(data)
144	            data["meta"]["total_papers"] = len(data.get("papers", {}))
145	            data["meta"]["last_updated"] = _paths.now_iso()
146	
147	            fd, tmp_path = tempfile.mkstemp(
148	                dir=str(path.parent), prefix=".literature_", suffix=".tmp"
149	            )
150	            try:
151	                with os.fdopen(fd, "w", encoding="utf-8") as tmp_f:
152	                    yaml.dump(
153	                        data, tmp_f,
154	                        default_flow_style=False, allow_unicode=True, sort_keys=False,
155	                    )
156	                    tmp_f.flush()
157	                    os.fsync(tmp_f.fileno())
158	                os.replace(tmp_path, str(path))
159	            except Exception:
160	                if os.path.exists(tmp_path):
161	                    os.unlink(tmp_path)
162	                raise
163	        finally:
164	            fcntl.flock(lock_f, fcntl.LOCK_UN)
165	
166	    return data
167	
168	
169	# ---------------------------------------------------------------------------
170	# Normalization & dedup
171	# ---------------------------------------------------------------------------
172	
173	_PUNCT_RE = re.compile(r"[^\w\s]")
174	_WS_RE = re.compile(r"\s+")
175	
176	
177	def _normalize_title(title: str) -> str:
178	    """Lowercase, strip diacritics + punctuation, collapse whitespace.
179	
180	    Used for fuzzy dedup when two records describe the same paper with
181	    slightly different titles (smart quotes, hyphens, capitalization).
182	    """
183	    if not title:
184	        return ""
185	    s = unicodedata.normalize("NFKD", title)
186	    s = "".join(c for c in s if not unicodedata.combining(c))
187	    s = s.lower()
188	    s = _PUNCT_RE.sub(" ", s)
189	    s = _WS_RE.sub(" ", s).strip()
190	    return s
191	
192	
193	def _normalize_doi(doi: str) -> str:
194	    """Lowercase DOI, strip common prefixes."""
195	    if not doi:
196	        return ""
197	    s = doi.strip().lower()
198	    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
199	        if s.startswith(prefix):
200	            s = s[len(prefix):]
201	            break
202	    return s.strip()
203	
204	
205	def _slugify(s: str, max_len: int = 24) -> str:
206	    """First-word slug — lowercase, alnum only, truncated."""
207	    s = unicodedata.normalize("NFKD", s or "")
208	    s = "".join(c for c in s if not unicodedata.combining(c))
209	    s = re.sub(r"[^a-zA-Z0-9]+", "", s.split()[0] if s.split() else "")
210	    return s.lower()[:max_len]
211	
212	
213	def _generate_bibtex_key(paper: dict) -> str:
214	    """Generate a bibtex key like ``vaswani2017attention``.
215	
216	    Uses the first author's surname + year + the first significant word of
217	    the title. Falls back to ``paper_{hash}`` if metadata is missing.
218	    """
219	    authors = paper.get("authors") or []
220	    first_author = ""
221	    if authors:
222	        raw = authors[0]
223	        if isinstance(raw, str):
224	            # Could be "Vaswani, A." or "Ashish Vaswani"
225	            if "," in raw:
226	                first_author = raw.split(",", 1)[0].strip()
227	            else:
228	                first_author = raw.strip().split()[-1] if raw.strip() else ""
229	    surname = _slugify(first_author)
230	
231	    year = paper.get("year") or ""
232	    year_part = str(year) if year else ""
233	
234	    title = paper.get("title") or ""
235	    # Skip stop words for the title slug
236	    stop = {"a", "an", "the", "on", "in", "of", "for", "and", "or", "is", "to"}
237	    words = [w for w in re.split(r"\W+", title.lower()) if w and w not in stop]
238	    word = _slugify(words[0]) if words else ""
239	
240	    key = f"{surname}{year_part}{word}"
241	    if not key.strip():
242	        import hashlib
243	        h = hashlib.md5(title.encode("utf-8")).hexdigest()[:8]
244	        key = f"paper_{h}"
245	    return key
246	
247	
248	def _find_existing_key(papers: dict, candidate: dict) -> str | None:
249	    """Find a matching paper key in ``papers`` for the candidate dict.
250	
251	    Match order: DOI exact (normalized) → normalized title.
252	    Returns the existing key or None.
253	
254	    bibtex_key collisions are NOT treated as dedup signal — two different
255	    papers can share a naive bibtex_key (e.g. same first author + year), and
256	    we handle that with a suffix at insert time. Real dedup must be content
257	    based.
258	    """
259	    cand_doi = _normalize_doi(candidate.get("doi", ""))
260	    cand_title = _normalize_title(candidate.get("title", ""))
261	
262	    for key, entry in papers.items():
263	        if cand_doi:
264	            entry_doi = _normalize_doi(entry.get("doi", ""))
265	            if entry_doi and entry_doi == cand_doi:
266	                return key
267	        if cand_title:
268	            entry_title = _normalize_title(entry.get("title", ""))
269	            if entry_title and entry_title == cand_title:
270	                return key
271	    return None
272	
273	
274	def _merge_paper(existing: dict, new: dict) -> dict:
275	    """Merge new fields into existing — only fill empty slots, never overwrite.
276	
277	    Verified=True wins over False (a later verification cannot un-verify).
278	    """
279	    merged = dict(existing)
280	    for k, v in new.items():
281	        if v is None or v == "" or v == []:
282	            continue
283	        if k == "verified":
284	            merged["verified"] = bool(existing.get("verified")) or bool(v)
285	            continue
286	        if not merged.get(k):
287	            merged[k] = v
288	    return merged
289	
290	
291	# ---------------------------------------------------------------------------
292	# Public API
293	# ---------------------------------------------------------------------------
294	
295	def read_literature_map(
296	    project: str | None = None,
297	    mode: str = "summary",
298	) -> ToolResult:
299	    """Read the literature map with mode-controlled verbosity.
300	
301	    Args:
302	        project: Project name — None reads the global (idea-phase) map.
303	        mode:
304	          - "summary"        → categories + per-paper {title, year, venue,
305	                                category, role, verified, bibtex_key}
306	          - "category:&lt;key>" → full entries in the named category
307	          - "competitors"    → full entries with role=direct-competitor
308	          - "unverified"     → full entries with verified=False
309	          - "bib"            → list of bibtex_key strings (for citation lookups)
310	          - "full"           → everything (use sparingly — token-heavy)
311	
312	    Returns:
313	        ToolResult.data = {
314	            "categories": [...],
315	            "papers": {key: {...}, ...},
316	            "meta": {"last_updated", "total_papers"},
317	            "mode": &lt;effective mode>,
318	        }
319	    """
320	    path = get_literature_map_path(project)
321	    data = _read_map(path)
322	    papers: dict = data.get("papers", {})
323	    categories: list = data.get("categories", [])
324	
325	    # Category-scoped read: "category:&lt;key>"
326	    if mode.startswith("category:"):
327	        cat_key = mode.split(":", 1)[1].strip()
328	        filtered = {k: v for k, v in papers.items() if v.get("category") == cat_key}
329	        return ToolResult(success=True, data={
330	            "categories": [c for c in categories if c.get("key") == cat_key],
331	            "papers": filtered,
332	            "meta": data.get("meta", {}),
333	            "mode": mode,
334	        })
335	
336	    if mode not in VALID_READ_MODES:
337	        return ToolResult(
338	            success=False,
339	            error=(
340	                f"Unknown mode '{mode}'. Valid: {sorted(VALID_READ_MODES)} "
341	                "or 'category:&lt;key>'."
342	            ),
343	        )
344	
345	    if mode == "summary":
346	        compact = {
347	            k: {f: v.get(f) for f in _SUMMARY_FIELDS if f in v}
348	            for k, v in papers.items()
349	        }
350	        return ToolResult(success=True, data={
351	            "categories": categories,
352	            "papers": compact,
353	            "meta": data.get("meta", {}),
354	            "mode": mode,
355	        })
356	
357	    if mode == "competitors":
358	        filtered = {k: v for k, v in papers.items() if v.get("role") == "direct-competitor"}
359	        return ToolResult(success=True, data={
360	            "categories": categories,
361	            "papers": filtered,
362	            "meta": data.get("meta", {}),
363	            "mode": mode,
364	        })
365	
366	    if mode == "unverified":
367	        filtered = {k: v for k, v in papers.items() if not v.get("verified")}
368	        return ToolResult(success=True, data={
369	            "categories": categories,
370	            "papers": filtered,
371	            "meta": data.get("meta", {}),
372	            "mode": mode,
373	        })
374	
375	    if mode == "bib":
376	        keys = [v.get("bibtex_key") or k for k, v in papers.items()]
377	        return ToolResult(success=True, data={
378	            "bibtex_keys": keys,
379	            "meta": data.get("meta", {}),
380	            "mode": mode,
381	        })
382	
383	    # mode == "full"
384	    return ToolResult(success=True, data={
385	        "categories": categories,
386	        "papers": papers,
387	        "meta": data.get("meta", {}),
388	        "mode": mode,
389	    })
390	
391	
392	def add_to_literature_map(
393	    project: str | None = None,
394	    papers: Iterable[dict] | None = None,
395	    added_by: str = "",
396	) -> ToolResult:
397	    """Add (or merge) one or more papers into the literature map.
398	
399	    Dedup: DOI exact (normalized) → normalized title → bibtex_key collision.
400	    Existing entries are merged field-by-field, never overwritten.
401	
402	    Args:
403	        project: Project name — None writes to the global (idea-phase) map.
404	        papers: Iterable of paper dicts. Recognized fields:
405	                title, authors (list[str]), year, venue, url, doi,
406	                bibtex_key, category, role, relevance, abstract,
407	                semantic_scholar_id, source_idea_id, verified.
408	                Missing bibtex_key is auto-generated.
409	        added_by: Free-form tag for provenance ("paper-research",
410	                  "idea-generator", "user", etc.). Recorded on new entries.
411	
412	    Returns:
413	        ToolResult.data = {
414	            "added": [keys],            # newly inserted
415	            "merged": [keys],           # matched existing, fields merged
416	            "rejected": [{title, reason}],
417	            "total_papers": N,
418	        }
419	    """
420	    if not papers:
421	        return ToolResult(
422	            success=False, error="No papers provided.",
423	        )
424	
425	    paper_list = list(papers)
426	    added: list[str] = []
427	    merged: list[str] = []
428	    rejected: list[dict] = []
429	    now = _paths.now_iso()
430	
431	    def _apply(data: dict) -> None:
432	        existing = data.setdefault("papers", {})
433	        for cand in paper_list:
434	            if not isinstance(cand, dict):
435	                rejected.append({"title": str(cand), "reason": "not a dict"})
436	                continue
437	            title = (cand.get("title") or "").strip()
438	            if not title:
439	                rejected.append({"title": "", "reason": "missing title"})
440	                continue
441	            if cand.get("role") and cand["role"] not in VALID_ROLES:
442	                rejected.append({
443	                    "title": title,
444	                    "reason": f"invalid role '{cand['role']}', valid: {sorted(VALID_ROLES)}",
445	                })
446	                continue
447	
448	            existing_key = _find_existing_key(existing, cand)
449	            if existing_key:
450	                # Merge — fill empty fields, keep verified=True if either is True
451	                existing[existing_key] = _merge_paper(existing[existing_key], cand)
452	                merged.append(existing_key)
453	                continue
454	
455	            # New entry — assign a bibtex_key if missing, dedupe within file
456	            key = cand.get("bibtex_key") or _generate_bibtex_key(cand)
457	            base_key = key
458	            suffix = 1
459	            while key in existing:
460	                suffix += 1
461	                key = f"{base_key}_{suffix}"
462	
463	            entry = {
464	                "title": title,
465	                "authors": cand.get("authors") or [],
466	                "year": cand.get("year"),
467	                "venue": cand.get("venue") or "",
468	                "url": cand.get("url") or "",
469	                "doi": cand.get("doi") or "",
470	                "bibtex_key": key,
471	                "category": cand.get("category") or "",
472	                "role": cand.get("role") or "",
473	                "relevance": cand.get("relevance") or "",
474	                "abstract": cand.get("abstract") or "",
475	                "semantic_scholar_id": cand.get("semantic_scholar_id") or "",
476	                "verified": bool(cand.get("verified", False)),
477	                "added_by": cand.get("added_by") or added_by or "",
478	                "added_at": cand.get("added_at") or now,
479	            }
480	            # Optional source_idea_id (global map only) — keep if present
481	            if cand.get("source_idea_id"):
482	                entry["source_idea_id"] = cand["source_idea_id"]
483	
484	            existing[key] = entry
485	            added.append(key)
486	
487	    data = _read_modify_write(get_literature_map_path(project), _apply)
488	
489	    return ToolResult(success=True, data={
490	        "added": added,
491	        "merged": merged,
492	        "rejected": rejected,
493	        "total_papers": data["meta"]["total_papers"],
494	    })
495	
496	
497	def update_literature_category(
498	    paper_key: str,
499	    project: str | None = None,
500	    category: str | None = None,
501	    role: str | None = None,
502	    relevance: str | None = None,
503	    verified: bool | None = None,
504	) -> ToolResult:
505	    """Update a single paper's classification fields.
506	
507	    Only the fields you pass are changed — others are left intact. This is
508	    the preferred path for "re-classify this paper after reading it" or
509	    "mark verified=true after OpenAlex check" — it's smaller than rewriting
510	    the whole entry via add_to_literature_map.
511	
512	    Args:
513	        paper_key: The YAML key of the paper (e.g. "vaswani2017attention").
514	        project: Project name — None updates the global map.
515	        category: New category key (must match a categories[].key, or empty).
516	        role: New role (must be in VALID_ROLES, or empty to clear).
517	        relevance: One-line relevance description.
518	        verified: Mark verified/unverified (e.g. after OpenAlex check).
519	
520	    Returns:
521	        ToolResult.data = {"paper_key", "updated_fields": {...}}
522	        ToolResult.error if paper_key not found or role/category invalid.
523	    """
524	    if role is not None and role and role not in VALID_ROLES:
525	        return ToolResult(
526	            success=False,
527	            error=f"invalid role '{role}', valid: {sorted(VALID_ROLES)}",
528	        )
529	
530	    updated: dict[str, Any] = {}
531	    not_found = {"miss": False}
532	
533	    def _apply(data: dict) -> None:
534	        papers = data.setdefault("papers", {})
535	        if paper_key not in papers:
536	            not_found["miss"] = True
537	            return
538	        entry = papers[paper_key]
539	        if category is not None:
540	            entry["category"] = category
541	            updated["category"] = category
542	        if role is not None:
543	            entry["role"] = role
544	            updated["role"] = role
545	        if relevance is not None:
546	            entry["relevance"] = relevance
547	            updated["relevance"] = relevance
548	        if verified is not None:
549	            entry["verified"] = bool(verified)
550	            updated["verified"] = bool(verified)
551	
552	    _read_modify_write(get_literature_map_path(project), _apply)
553	
554	    if not_found["miss"]:
555	        return ToolResult(
556	            success=False,
557	            error=f"paper_key '{paper_key}' not found in literature_map",
558	        )
559	    return ToolResult(success=True, data={
560	        "paper_key": paper_key,
561	        "updated_fields": updated,
562	    })
563	
564	
565	def upsert_category(
566	    project: str | None = None,
567	    key: str = "",
568	    name: str = "",
569	    narrative: str = "",
570	) -> ToolResult:
571	    """Add or update a category entry in the categories[] list.
572	
573	    Categories define the Related Work subsection structure. A paper's
574	    ``category`` field references one of these by ``key``.
575	
576	    Args:
577	        project: Project name — None edits the global map.
578	        key: Category slug (e.g. "attention_mechanisms"). Required.
579	        name: Human-readable name (e.g. "Attention Mechanisms"). Required for new.
580	        narrative: One-line description of the category's narrative arc.
581	
582	    Returns:
583	        ToolResult.data = {"key", "action": "added"|"updated"}.
584	    """
585	    if not key:
586	        return ToolResult(success=False, error="key is required")
587	
588	    state = {"action": "added"}
589	
590	    def _apply(data: dict) -> None:
591	        cats = data.setdefault("categories", [])
592	        for c in cats:
593	            if c.get("key") == key:
594	                if name:
595	                    c["name"] = name
596	                if narrative:
597	                    c["narrative"] = narrative
598	                state["action"] = "updated"
599	                return
600	        cats.append({"key": key, "name": name or key, "narrative": narrative})
601	
602	    _read_modify_write(get_literature_map_path(project), _apply)
603	    return ToolResult(success=True, data={"key": key, "action": state["action"]})
604	
605	
606	def seed_literature_map(
607	    project: str,
608	    seed_papers: Iterable[dict],
609	    source_idea_id: str = "",
610	) -> ToolResult:
611	    """Bulk-seed a new project's literature_map from an idea's accumulated papers.
612	
613	    Called by the idea→project bootstrap hook. Each seed paper is added with
614	    ``added_by="idea_generator"`` so downstream consumers can distinguish
615	    seed papers from those discovered during research.
616	
617	    Args:
618	        project: Project name (required — seeding without a project is the
619	                 global map case, handled by add_to_literature_map directly).
620	        seed_papers: Iterable of paper dicts (same schema as add_to_literature_map).
621	        source_idea_id: Idea ID these papers came from. Stamped on entries so
622	                        a future "re-seed from idea" can find them.
623	
624	    Returns:
625	        Same shape as add_to_literature_map.
626	    """
627	    if not project:
628	        return ToolResult(success=False, error="project is required for seed_literature_map")
629	
630	    seeds = []
631	    for p in seed_papers:
632	        if not isinstance(p, dict):
633	            continue
634	        p2 = dict(p)
635	        if source_idea_id:
636	            p2.setdefault("source_idea_id", source_idea_id)
637	        seeds.append(p2)
638	
639	    return add_to_literature_map(
640	        project=project, papers=seeds, added_by="idea_generator",
641	    )
642	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eaf7674-66f1-4dc4-9429-94794a7c3b4b",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "392f9388-9562-41cf-b8cb-b9c649e86340",
  "sourceToolAssistantUUID": "0eaf7674-66f1-4dc4-9429-94794a7c3b4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T14:17:22.839Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PCQABETLhE1rJRZRcvUpHu`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/distill.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "392f9388-9562-41cf-b8cb-b9c649e86340",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxsL7n7Fnabyh9YF1MQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0e2c16bf-0e90-43b3-b661-c643af88e780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GPLm9aXseYvTbaixpN7S6P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2727,
      "cache_read_input_tokens": 37434,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2727
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 238,
          "cache_read_input_tokens": 37434,
          "cache_creation_input_tokens": 2727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2727,
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

_source line 13 · 2026-05-20T14:17:23.169Z_

<details><summary>↩ Tool result · `toolu_01PCQABETLhE1rJRZRcvUpHu`</summary>

```text
1	"""Paper distillation engine — extract domain knowledge from related papers.
2	
3	Distills research methodology and writing patterns from project-related papers
4	into two project-specific skills:
5	
6	  - ``distilled-research.skill.md`` — baselines, metrics, datasets, trends
7	  - ``distilled-writing.skill.md`` — narrative strategies, structure conventions
8	
9	Two-layer architecture:
10	  Layer 1: Per-paper deep analysis → ``distill_tmp/{paper_key}.yaml``
11	  Layer 2: Cross-paper synthesis → skill files
12	
13	Triggered by:
14	  - ``distill_papers`` MCP tool (Agent/Director)
15	  - ``POST /api/distill/{project}`` HTTP endpoint (Manager → BE)
16	  - ``/distill`` Feishu command (via Manager)
17	"""
18	
19	from __future__ import annotations
20	
21	import asyncio
22	import logging
23	import os
24	import re
25	import shutil
26	from dataclasses import dataclass, field
27	from datetime import datetime, timezone
28	from pathlib import Path
29	from typing import Any
30	
31	import yaml
32	
33	from core import paths as _paths
34	from core.skills.loader import (
35	    load_skills_config,
36	    parse_skill_md,
37	)
38	from core.tools.result import ToolResult
39	
40	logger = logging.getLogger(__name__)
41	
42	
43	# ---------------------------------------------------------------------------
44	# Configuration defaults
45	# ---------------------------------------------------------------------------
46	
47	_DEFAULT_DISTILL_CONFIG: dict[str, Any] = {
48	    "model": "claude-opus-4-6",
49	    "max_papers": 25,
50	    "max_deep_read": 8,
51	    "max_skill_chars": 3000,
52	    "auto_on_bootstrap": True,
53	    "year_range": 2,
54	}
55	
56	
57	def _load_distill_config() -> dict[str, Any]:
58	    """Load distillation config from skills.yaml ``distillation`` section."""
59	    cfg = dict(_DEFAULT_DISTILL_CONFIG)
60	    skills_cfg = load_skills_config()
61	    distill_section = skills_cfg.get("distillation") or {}
62	    if isinstance(distill_section, dict):
63	        cfg.update(distill_section)
64	    return cfg
65	
66	
67	# ---------------------------------------------------------------------------
68	# Data types
69	# ---------------------------------------------------------------------------
70	
71	@dataclass
72	class PaperForDistill:
73	    """Minimal paper metadata for the distillation pipeline."""
74	    paper_key: str
75	    title: str
76	    year: int | None = None
77	    venue: str = ""
78	    authors: list[str] = field(default_factory=list)
79	    abstract: str = ""
80	    citation_count: int | None = None
81	    semantic_scholar_id: str = ""
82	    arxiv_id: str = ""
83	    doi: str = ""
84	    url: str = ""
85	    pdf_url: str = ""
86	    role: str = ""
87	    relevance_score: float = 0.0
88	
89	
90	@dataclass
91	class DistillResult:
92	    """Result of a distillation run."""
93	    success: bool
94	    project: str
95	    version: int = 0
96	    paper_count: int = 0
97	    deep_read_count: int = 0
98	    abstract_only_count: int = 0
99	    new_papers_found: int = 0
100	    research_skill_path: str = ""
101	    writing_skill_path: str = ""
102	    research_skill_chars: int = 0
103	    writing_skill_chars: int = 0
104	    error: str = ""
105	
106	
107	# ---------------------------------------------------------------------------
108	# Paper collection
109	# ---------------------------------------------------------------------------
110	
111	def _collect_papers(project: str, config: dict) -> list[PaperForDistill]:
112	    """Collect papers from literature_map + Semantic Scholar.
113	
114	    Four-layer collection (by proximity):
115	      1. literature_map.yaml (already curated)
116	      2. S2 keyword search (project description keywords)
117	      3. S2 recommendations (seed from layer 1 paper IDs)
118	      4. Citation graph (references of high-relevance papers)
119	    """
120	    papers: dict[str, PaperForDistill] = {}
121	    max_papers = config.get("max_papers", 25)
122	    year_range = config.get("year_range", 2)
123	    current_year = datetime.now(timezone.utc).year
124	
125	    # Layer 1: literature_map
126	    _collect_from_literature_map(project, papers)
127	
128	    if len(papers) >= max_papers:
129	        return _rank_and_trim(papers, max_papers, current_year, year_range)
130	
131	    # Layer 2: S2 keyword search
132	    _collect_from_s2_search(project, papers, max_papers, current_year, year_range)
133	
134	    if len(papers) >= max_papers:
135	        return _rank_and_trim(papers, max_papers, current_year, year_range)
136	
137	    # Layer 3: S2 recommendations
138	    seed_ids = [p.semantic_scholar_id for p in papers.values() if p.semantic_scholar_id]
139	    if seed_ids:
140	        _collect_from_s2_recommendations(seed_ids[:5], papers, max_papers)
141	
142	    return _rank_and_trim(papers, max_papers, current_year, year_range)
143	
144	
145	def _collect_from_literature_map(
146	    project: str,
147	    papers: dict[str, PaperForDistill],
148	) -> None:
149	    """Read existing literature_map and convert to PaperForDistill entries."""
150	    from core.tools.literature import get_literature_map_path, _read_map
151	
152	    path = get_literature_map_path(project)
153	    lit_map = _read_map(path)
154	
155	    raw_papers = lit_map.get("papers") or {}
156	    if isinstance(raw_papers, list):
157	        items = ((e.get("id") or e.get("title", f"paper_{i}"), e) for i, e in enumerate(raw_papers) if isinstance(e, dict))
158	    elif isinstance(raw_papers, dict):
159	        items = raw_papers.items()
160	    else:
161	        items = iter(())
162	    for key, entry in items:
163	        if key in papers:
164	            continue
165	        papers[key] = PaperForDistill(
166	            paper_key=key,
167	            title=entry.get("title", ""),
168	            year=entry.get("year"),
169	            venue=entry.get("venue", ""),
170	            authors=entry.get("authors", []),
171	            abstract=entry.get("abstract", ""),
172	            citation_count=entry.get("citation_count"),
173	            semantic_scholar_id=entry.get("semantic_scholar_id", ""),
174	            arxiv_id=entry.get("arxiv_id", ""),
175	            doi=entry.get("doi", ""),
176	            url=entry.get("url", ""),
177	            pdf_url=entry.get("pdf_url", ""),
178	            role=entry.get("role", ""),
179	        )
180	
181	
182	def _collect_from_s2_search(
183	    project: str,
184	    papers: dict[str, PaperForDistill],
185	    max_papers: int,
186	    current_year: int,
187	    year_range: int,
188	) -> None:
189	    """Search Semantic Scholar with project keywords."""
190	    from core.tools.project_config import load_project_config
191	    from core.tools import semantic_scholar as s2
192	
193	    try:
194	        cfg = load_project_config(project)
195	    except Exception:
196	        return
197	    if not cfg.success or not cfg.data:
198	        return
199	
200	    # load_project_config returns {"project": &lt;name>, "config": &lt;full yaml>}
201	    config_yaml = cfg.data.get("config") or {}
202	    description = (config_yaml.get("project") or {}).get("description", "")
203	    if not description:
204	        return
205	
206	    yr_filter = f"{current_year - year_range}-{current_year}"
207	    needed = max(5, max_papers - len(papers))
208	    result = s2.search_papers(description[:200], limit=min(needed, 20), year_range=yr_filter)
209	    if not result.success:
210	        return
211	
212	    for p in result.data.get("papers", []):
213	        _add_s2_paper(papers, p)
214	
215	
216	def _collect_from_s2_recommendations(
217	    seed_ids: list[str],
218	    papers: dict[str, PaperForDistill],
219	    max_papers: int,
220	) -> None:
221	    """Get S2 recommendations based on seed papers."""
222	    from core.tools import semantic_scholar as s2
223	
224	    needed = max_papers - len(papers)
225	    if needed <= 0:
226	        return
227	
228	    result = s2.get_paper_recommendations(seed_ids, limit=min(needed, 10))
229	    if not result.success:
230	        return
231	
232	    for p in result.data.get("papers", []):
233	        _add_s2_paper(papers, p)
234	
235	
236	def _add_s2_paper(papers: dict[str, PaperForDistill], s2_paper: dict) -> None:
237	    """Add an S2-normalized paper dict if not already present."""
238	    title = s2_paper.get("title", "")
239	    if not title:
240	        return
241	
242	    key = _make_paper_key(s2_paper)
243	    if key in papers:
244	        return
245	
246	    # Dedup by title (normalized)
247	    norm_title = _normalize_title(title)
248	    for existing in papers.values():
249	        if _normalize_title(existing.title) == norm_title:
250	            return
251	
252	    papers[key] = PaperForDistill(
253	        paper_key=key,
254	        title=title,
255	        year=s2_paper.get("year"),
256	        venue=s2_paper.get("venue", ""),
257	        authors=s2_paper.get("authors", []),
258	        abstract=s2_paper.get("abstract", ""),
259	        citation_count=s2_paper.get("citation_count"),
260	        semantic_scholar_id=s2_paper.get("semantic_scholar_id", ""),
261	        arxiv_id=s2_paper.get("arxiv_id", ""),
262	        doi=s2_paper.get("doi", ""),
263	        url=s2_paper.get("url", ""),
264	        pdf_url=s2_paper.get("pdf_url", ""),
265	    )
266	
267	
268	def _make_paper_key(s2_paper: dict) -> str:
269	    """Generate a bibtex-style key from S2 paper data."""
270	    authors = s2_paper.get("authors", [])
271	    year = s2_paper.get("year", "")
272	    first_author = ""
273	    if authors:
274	        name = authors[0] if isinstance(authors[0], str) else ""
275	        first_author = name.split()[-1].lower() if name else ""
276	    title_words = (s2_paper.get("title") or "").split()[:2]
277	    slug = "".join(w.lower() for w in title_words)
278	    return f"{first_author}{year}{slug}"
279	
280	
281	_PUNCT_RE = re.compile(r"[^\w\s]")
282	_WS_RE = re.compile(r"\s+")
283	
284	
285	def _normalize_title(title: str) -> str:
286	    """Lowercase, strip punctuation, collapse whitespace for dedup."""
287	    if not title:
288	        return ""
289	    s = title.lower()
290	    s = _PUNCT_RE.sub(" ", s)
291	    s = _WS_RE.sub(" ", s).strip()
292	    return s
293	
294	
295	def _rank_and_trim(
296	    papers: dict[str, PaperForDistill],
297	    max_papers: int,
298	    current_year: int,
299	    year_range: int,
300	) -> list[PaperForDistill]:
301	    """Rank papers by (venue quality × recency × citations) and trim."""
302	    _TOP_VENUES = {"neurips", "icml", "iclr", "acl", "emnlp", "naacl", "cvpr", "iccv", "eccv", "aaai", "ijcai"}
303	
304	    for p in papers.values():
305	        score = 0.0
306	        # Venue quality
307	        venue_lower = p.venue.lower()
308	        if any(v in venue_lower for v in _TOP_VENUES):
309	            score += 3.0
310	        elif venue_lower and "arxiv" not in venue_lower:
311	            score += 1.0
312	        # Recency
313	        if p.year and p.year >= current_year - year_range:
314	            score += 2.0
315	        elif p.year and p.year >= current_year - year_range - 1:
316	            score += 1.0
317	        # Citations
318	        if p.citation_count and p.citation_count > 50:
319	            score += 2.0
320	        elif p.citation_count and p.citation_count > 10:
321	            score += 1.0
322	        # Existing literature_map entries get a bonus
323	        if p.role:
324	            score += 1.0
325	        if p.role == "direct-competitor":
326	            score += 2.0
327	        p.relevance_score = score
328	
329	    ranked = sorted(papers.values(), key=lambda p: p.relevance_score, reverse=True)
330	    return ranked[:max_papers]
331	
332	
333	# ---------------------------------------------------------------------------
334	# Incremental check
335	# ---------------------------------------------------------------------------
336	
337	def _distill_tmp_dir(project: str) -> Path:
338	    """Return the directory for Layer 1 per-paper YAML caches."""
339	    return _paths.project_dir(project) / "distill_tmp"
340	
341	
342	def _check_incremental(
343	    project: str,
344	    papers: list[PaperForDistill],
345	) -> tuple[list[PaperForDistill], list[Path]]:
346	    """Split papers into (need_analysis, already_cached).
347	
348	    Returns:
349	        (new_papers, cached_yamls) — papers without Layer 1 cache,
350	        and paths to existing Layer 1 YAML files.
351	    """
352	    tmp_dir = _distill_tmp_dir(project)
353	    new_papers: list[PaperForDistill] = []
354	    cached_yamls: list[Path] = []
355	
356	    for p in papers:
357	        cached = tmp_dir / f"{p.paper_key}.yaml"
358	        if cached.exists():
359	            cached_yamls.append(cached)
360	        else:
361	            new_papers.append(p)
362	
363	    return new_papers, cached_yamls
364	
365	
366	def _get_existing_paper_keys(project: str) -> set[str]:
367	    """Read existing distilled skill to get previously distilled paper keys."""
368	    skill_path = _paths.project_skills_dir(project) / "distilled-research.skill.md"
369	    if not skill_path.exists():
370	        return set()
371	    try:
372	        skill = parse_skill_md(skill_path.read_text(encoding="utf-8"), skill_path)
373	        # distilled_from is stored in the frontmatter but not parsed into PromptSkill
374	        # We need to read the raw frontmatter
375	        text = skill_path.read_text(encoding="utf-8")
376	        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
377	        if fm_match:
378	            fm = yaml.safe_load(fm_match.group(1)) or {}
379	            df = fm.get("distilled_from") or {}
380	            return set(df.get("paper_keys") or [])
381	    except Exception:
382	        pass
383	    return set()
384	
385	
386	# ---------------------------------------------------------------------------
387	# Distiller Agent session
388	# ---------------------------------------------------------------------------
389	
390	def _build_distiller_prompt(
391	    papers: list[PaperForDistill],
392	    cached_yamls: list[Path],
393	    project: str,
394	    config: dict,
395	) -> str:
396	    """Build the complete prompt for the Distiller Agent session."""
397	    prompt_path = _paths.REPO_ROOT / "prompts" / "roles" / "distiller.md"
398	    if prompt_path.exists():
399	        base_prompt = prompt_path.read_text(encoding="utf-8")
400	    else:
401	        base_prompt = "你是一个论文蒸馏引擎。按照下方指令执行两层蒸馏。"
402	
403	    tmp_dir = _distill_tmp_dir(project)
404	    skills_dir = _paths.project_skills_dir(project)
405	    max_deep_read = config.get("max_deep_read", 8)
406	    max_skill_chars = config.get("max_skill_chars", 3000)
407	
408	    # Papers for deep reading (Layer 1 analysis needed)
409	    deep_read_papers = papers[:max_deep_read]
410	    abstract_only_papers = papers[max_deep_read:]
411	
412	    paper_list = _format_paper_list(deep_read_papers, abstract_only_papers)
413	
414	    cached_info = ""
415	    if cached_yamls:
416	        cached_info = f"\n已有 {len(cached_yamls)} 篇论文的 Layer 1 缓存（在 `{tmp_dir}/` 中），无需重新分析。\n"
417	
418	    return f"""{base_prompt}
419	
420	## 任务参数
421	
422	- 项目: {project}
423	- Layer 1 输出目录: `{tmp_dir}/`
424	- Skill 输出目录: `{skills_dir}/`
425	- 深度精读上限: {max_deep_read} 篇
426	- 单个 Skill 字数上限: {max_skill_chars} 字符
427	{cached_info}
428	## 待分析论文
429	
430	{paper_list}
431	
432	## 执行指令
433	
434	1. 对每篇「深度精读」论文执行 Layer 1 分析，将结构化结果写入 `{tmp_dir}/{{paper_key}}.yaml`
435	2. 对「仅摘要」论文，仅提取 research 维度（baseline/metric/dataset），写入同目录
436	3. 读取全部 Layer 1 YAML（含已缓存的），执行 Layer 2 跨论文归纳
437	4. 生成 `distilled-research.skill.md` 和 `distilled-writing.skill.md`，写入 `{skills_dir}/`
438	5. 每个 skill body 不超过 {max_skill_chars} 字符
439	"""
440	
441	
442	def _format_paper_list(
443	    deep_read: list[PaperForDistill],
444	    abstract_only: list[PaperForDistill],
445	) -> str:
446	    """Format papers into a structured list for the Distiller prompt."""
447	    lines: list[str] = []
448	
449	    if deep_read:
450	        lines.append("### 深度精读（Layer 1 完整分析）\n")
451	        for i, p in enumerate(deep_read, 1):
452	            venue_year = f"{p.venue} {p.year}" if p.venue and p.year else str(p.year or "")
453	            url_hint = ""
454	            if p.arxiv_id:
455	                url_hint = f" | arXiv:{p.arxiv_id}"
456	            elif p.url:
457	                url_hint = f" | {p.url}"
458	            lines.append(f"{i}. **{p.title}** ({venue_year}{url_hint})")
459	            if p.abstract:
460	                lines.append(f"   摘要: {p.abstract[:200]}...")
461	            lines.append(f"   paper_key: `{p.paper_key}`")
462	            lines.append("")
463	
464	    if abstract_only:
465	        lines.append("\n### 仅摘要（Layer 1 research 维度）\n")
466	        for i, p in enumerate(abstract_only, 1):
467	            venue_year = f"{p.venue} {p.year}" if p.venue and p.year else str(p.year or "")
468	            lines.append(f"{i}. **{p.title}** ({venue_year}) — paper_key: `{p.paper_key}`")
469	
470	    return "\n".join(lines)
471	
472	
473	async def _run_distiller_session(
474	    project: str,
475	    prompt: str,
476	    config: dict,
477	) -> bool:
478	    """Spawn a Claude subprocess to run the Distiller Agent.
479	
480	    Intentionally bypasses ``SessionServer``: distillation is a one-shot
481	    system task, not a user-facing conversation. It needs no dashboard
482	    surface, no message queue, no restart-on-disconnect — just run
483	    Claude with the distiller prompt and exit. Going through SessionServer
484	    would create a phantom "distiller_xxx" session entry with no chat_id
485	    that confuses cleanup paths.
486	
487	    Returns True on success.
488	    """
489	    from core.session_claude_md import build_session_prompt
490	
491	    session_key = f"system:distiller:{project}"
492	    cwd = build_session_prompt(project, "distiller", session_key=session_key)
493	
494	    # Find Claude binary
495	    claude_bin = _find_claude_binary()
496	    if not claude_bin:
497	        logger.error("Claude binary not found — cannot run distiller session")
498	        return False
499	
500	    # Build MCP config for distiller (minimal tools: WebFetch, WebSearch, file read/write)
501	    mcp_config = _ensure_distiller_mcp_config()
502	
503	    cmd = [
504	        str(claude_bin),
505	        "--print",
506	        "--output-format", "text",
507	        "--max-turns", "50",
508	        "--model", config.get("model", "claude-opus-4-6"),
509	        "--dangerously-skip-permissions",
510	        "--mcp-config", str(mcp_config),
511	        "--append-system-prompt", "你是 Distiller Agent，执行论文蒸馏任务。完成后输出 [DISTILL_DONE]。",
512	        "-p", prompt,
513	    ]
514	
515	    # Select a Claude pool account for this oneshot subprocess (same reason as
516	    # paper_audit._run_oneshot_claude — default $HOME/.claude has no creds on
517	    # BE hosts, every distill run would error "Not logged in").
518	    from core.claude_client import pool_select as _pool_select, make_claude_env
519	    _config_dir = _pool_select(role="automation")
520	    if not _config_dir:
521	        logger.warning(
522	            "[distill] pool_select returned None for %s; "
523	            "claude subprocess will likely fail auth",
524	            project,
525	        )
526	    env = make_claude_env(
527	        config_dir=_config_dir,
528	        extra={
529	            "AGENT_ML_WORKSPACE": str(_paths.WORKSPACE_ROOT),
530	            "DISTILLER_MODE": "1",
531	        },
532	    )
533	
534	    logger.info("Starting distiller session for %s (config_dir=%s)", project, _config_dir)
535	    proc = None
536	    try:
537	        proc = await asyncio.create_subprocess_exec(
538	            *cmd,
539	            cwd=str(cwd),
540	            env=env,
541	            stdout=asyncio.subprocess.PIPE,
542	            stderr=asyncio.subprocess.PIPE,
543	        )
544	        stdout, stderr = await asyncio.wait_for(
545	            proc.communicate(),
546	            timeout=1800,  # 30 min — deep-read + synthesis + skill gen
547	        )
548	
549	        if proc.returncode != 0:
550	            logger.warning(
551	                "Distiller session exited %d for %s: %s",
552	                proc.returncode, project,
553	                (stderr or b"").decode("utf-8", errors="replace")[:500],
554	            )
555	            return False
556	
557	        output = (stdout or b"").decode("utf-8", errors="replace")
558	        if "[DISTILL_DONE]" in output:
559	            logger.info("Distiller session completed successfully for %s", project)
560	            return True
561	
562	        logger.warning(
563	            "Distiller session exited 0 for %s but no [DISTILL_DONE] marker "
564	            "(possible max-turns exhaustion)", project,
565	        )
566	        return False
567	
568	    except asyncio.TimeoutError:
569	        logger.warning("Distiller session timed out for %s", project)
570	        if proc is not None:
571	            try:
572	                proc.kill()
573	                await proc.wait()
574	                logger.info("Killed timed-out distiller process for %s", project)
575	            except ProcessLookupError:
576	                pass
577	        return False
578	    except Exception:
579	        logger.exception("Distiller session failed for %s", project)
580	        if proc is not None:
581	            try:
582	                proc.kill()
583	                await proc.wait()
584	            except (ProcessLookupError, Exception):
585	                pass
586	        return False
587	
588	
589	def _find_claude_binary() -> Path | None:
590	    """Locate the claude CLI binary."""
591	    import shutil
592	    for name in ("claude",):
593	        path = shutil.which(name)
594	        if path:
595	            return Path(path)
596	    return None
597	
598	
599	def _ensure_distiller_mcp_config() -> Path:
600	    """Write MCP config for Distiller role (minimal toolset)."""
601	    from core.session_server import _ensure_mcp_config_for_mode
602	    return _ensure_mcp_config_for_mode(
603	        "distiller",
604	        env_var="DISTILLER_MODE",
605	    )
606	
607	
608	# ---------------------------------------------------------------------------
609	# Skill writing / updating
610	# ---------------------------------------------------------------------------
611	
612	def _write_or_update_skills(
613	    project: str,
614	    papers: list[PaperForDistill],
615	) -> dict[str, Any]:
616	    """Read Layer 1/2 outputs and create/update skill files.
617	
618	    This is called after the Distiller session completes. The session
619	    writes skill files directly, so this function verifies they exist
620	    and returns metadata.
621	    """
622	    skills_dir = _paths.project_skills_dir(project)
623	    research_path = skills_dir / "distilled-research.skill.md"
624	    writing_path = skills_dir / "distilled-writing.skill.md"
625	
626	    result: dict[str, Any] = {
627	        "research_exists": research_path.exists(),
628	        "writing_exists": writing_path.exists(),
629	        "research_chars": 0,
630	        "writing_chars": 0,
631	        "research_version": 0,
632	        "writing_version": 0,
633	    }
634	
635	    if research_path.exists():
636	        text = research_path.read_text(encoding="utf-8")
637	        result["research_chars"] = len(text)
638	        try:
639	            skill = parse_skill_md(text, research_path)
640	            result["research_version"] = skill.version
641	        except Exception:
642	            pass
643	
644	    if writing_path.exists():
645	        text = writing_path.read_text(encoding="utf-8")
646	        result["writing_chars"] = len(text)
647	        try:
648	            skill = parse_skill_md(text, writing_path)
649	            result["writing_version"] = skill.version
650	        except Exception:
651	            pass
652	
653	    return result
654	
655	
656	def _backfill_literature_map(project: str, papers: list[PaperForDistill]) -> int:
657	    """Write newly discovered papers back to literature_map."""
658	    from core.tools.literature import add_to_literature_map
659	
660	    new_papers = []
661	    for p in papers:
662	        if not p.role:  # Papers without a role came from S2, not literature_map
663	            new_papers.append({
664	                "title": p.title,
665	                "year": p.year,
666	                "venue": p.venue,
667	                "authors": p.authors,
668	                "abstract": p.abstract,
669	                "doi": p.doi,
670	                "arxiv_id": p.arxiv_id,
671	                "url": p.url,
672	                "semantic_scholar_id": p.semantic_scholar_id,
673	                "role": "background",
674	                "verified": False,
675	            })
676	
677	    if not new_papers:
678	        return 0
679	
680	    result = add_to_literature_map(project, new_papers, added_by="distiller")
681	    if result.success:
682	        added = result.data.get("added", 0) if result.data else 0
683	        return added
684	    return 0
685	
686	
687	# ---------------------------------------------------------------------------
688	# Main entry point
689	# ---------------------------------------------------------------------------
690	
691	async def distill_project_skills(
692	    project: str,
693	    force: bool = False,
694	    auto_trigger: bool = False,
695	    callback_url: str = "",
696	    chat_id: str = "",
697	    operational_chat_id: str = "",
698	) -> DistillResult:
699	    """Main entry: collect papers → run Distiller session → verify skill output.
700	
701	    On success, also injects a ``[DISTILL]`` notification into the project's
702	    Director session (so Director can audit the distilled knowledge), mirroring
703	    the cron-hook / worker-done injection pattern.
704	
705	    Args:
706	        project: Project name.
707	        force: If True, re-distill even when no new papers are found.
708	        auto_trigger: True when fired by bootstrap auto-trigger; respects
709	            the ``auto_on_bootstrap`` config flag and silently skips if disabled.
710	        chat_id: A-group chat_id for progress card.
711	        operational_chat_id: B-group chat_id for phase notifications.
712	    """
713	    config = _load_distill_config()
714	
715	    # Bootstrap auto-trigger respects the config gate; explicit triggers ignore it.
716	    if auto_trigger and not config.get("auto_on_bootstrap", False):
717	        return DistillResult(
718	            success=False, project=project,
719	            error="auto_on_bootstrap disabled in config",
720	        )
721	
722	    # Fallback: load chat IDs from project config when not provided.
723	    if not chat_id or not operational_chat_id:
724	        try:
725	            from core.tools.project_config import load_project_config
726	            cfg_result = load_project_config(project)
727	            if cfg_result.success:
728	                feishu_cfg = (cfg_result.data or {}).get("config", {}).get("feishu", {})
729	                if not chat_id:
730	                    chat_id = feishu_cfg.get("chat_id", "")
731	                if not operational_chat_id:
732	                    operational_chat_id = feishu_cfg.get("operational_chat_id", "")
733	        except Exception:
734	            pass
735	
736	    # ── Progress helpers (same pattern as dream.py _run_dream_pipeline) ──
737	    started_at = datetime.now(timezone.utc).isoformat()
738	    _activity: list[tuple[str, str]] = []
739	    _ops_notified: set[str] = set()
740	    _card_msg_id = ""
741	
742	    _PHASE_LABEL = {
743	        "pending": "⏳ 启动",
744	        "collecting": "📚 论文收集中",
745	        "analyzing": "🔬 Distiller 精读中",
746	        "done": "✅ 完成",
747	        "failed": "❌ 失败",
748	        "skipped": "⏭️ 跳过",
749	    }
750	
751	    def _log(label: str, detail: str) -> None:
752	        _activity.append((label, detail))
753	
754	    def _notify_ops(phase: str, extra: str = "") -> None:
755	        if not operational_chat_id or phase in _ops_notified:
756	            return
757	        _ops_notified.add(phase)
758	        label = _PHASE_LABEL.get(phase, phase)
759	        text = f"[Distill] {project} — {label}"
760	        if extra:
761	            text += f"\n{extra[:300]}"
762	        try:
763	            from core.tools.feishu import send_message
764	            send_message(chat_id=operational_chat_id, text=text)
765	        except Exception:
766	            logger.debug("[distill] ops notify failed for %s", project, exc_info=True)
767	
768	    def _patch_card(phase: str, stages: list[str] | None = None,
769	                    error: str = "", result_summary: dict | None = None) -> None:
770	        nonlocal _card_msg_id
771	        if not _card_msg_id:
772	            return
773	        try:
774	            from core.tools.distill_card import patch_distill_card
775	            patch_distill_card(
776	                project=project, phase=phase, message_id=_card_msg_id,
777	                stages_completed=stages, activity=_activity, error=error,
778	                started_at=started_at, force=force, result_summary=result_summary,
779	            )
780	        except Exception:
781	            logger.debug("[distill] card patch failed for %s", project, exc_info=True)
782	
783	    # ── 0. Start ──
784	    _log("启动", f"开始蒸馏 {project}" + (" (force)" if force else ""))
785	    try:
786	        from core.tools.distill_card import send_distill_card
787	        _card_msg_id = send_distill_card(
788	            project=project, chat_id=chat_id, force=force, started_at=started_at,
789	        )
790	    except Exception:
791	        logger.debug("[distill] send card failed for %s", project, exc_info=True)
792	    _notify_ops("pending")
793	
794	    # Validate project exists
795	    project_cfg_path = _paths.projects_config_dir() / f"{project}.yaml"
796	    if not project_cfg_path.exists():
797	        _log("错误", f"项目 {project} 不存在")
798	        _patch_card("failed", error=f"项目 {project} 不存在")
799	        _notify_ops("failed", f"项目 {project} 不存在")
800	        return DistillResult(
801	            success=False, project=project,
802	            error=f"项目 {project} 不存在",
803	        )
804	
805	    # ── 1. Collect papers ──
806	    _log("收集", "从 literature_map + Semantic Scholar 收集论文...")
807	    _patch_card("collecting")
808	    _notify_ops("collecting")
809	
810	    papers = _collect_papers(project, config)
811	    if not papers:
812	        _log("收集", "未找到可供蒸馏的论文")
813	        result = DistillResult(
814	            success=False, project=project,
815	            error="未找到可供蒸馏的论文。请先在 literature_map 中添加论文。",
816	        )
817	        # Always try to notify Director — auto_trigger (bootstrap) needs this
818	        # the most: Director just spawned, sees [PROJECT BOOTSTRAP], and would
819	        # otherwise have no idea literature_map needs filling. _inject_...
820	        # itself handles "Director not found yet" (returns False, no error).
821	        director_notified = _inject_distill_failure_to_director(result)
822	        if director_notified:
823	            _notify_user_of_distill_followup(project, chat_id)
824	            _log("跟进", "已通知 Director 补充 literature_map 后重试")
825	            _patch_card("failed", error="literature_map 为空 → 已通知 Director 补充文献")
826	            _notify_ops("failed", "literature_map 为空 → 已通知 Director")
827	        else:
828	            _patch_card("failed", error="未找到论文")
829	            _notify_ops("failed", "未找到论文")
830	        return result
831	
832	    _log("收集", f"找到 {len(papers)} 篇候选论文")
833	    _patch_card("collecting", stages=["collect"])
834	
835	    # Incremental check
836	    existing_keys = _get_existing_paper_keys(project)
837	    new_paper_keys = {p.paper_key for p in papers} - existing_keys
838	    if not force and existing_keys and len(new_paper_keys) < 3:
839	        _log("增量", f"新增仅 {len(new_paper_keys)} 篇，跳过")
840	        _patch_card("skipped", stages=["collect"],
841	                    error=f"新增论文较少（{len(new_paper_keys)} 篇）")
842	        _notify_ops("skipped", f"仅 {len(new_paper_keys)} 篇新论文")
843	        return DistillResult(
844	            success=False, project=project,
845	            paper_count=len(papers),
846	            new_papers_found=len(new_paper_keys),
847	            error=f"新增论文较少（{len(new_paper_keys)} 篇），建议积累更多后再蒸馏。使用 force=True 强制蒸馏。",
848	        )
849	
850	    # Check which papers need Layer 1 analysis
851	    new_to_analyze, cached_yamls = _check_incremental(project, papers)
852	    max_deep_read = config.get("max_deep_read", 8)
853	    _log("增量", f"{len(new_to_analyze)} 篇新论文, {len(cached_yamls)} 篇已缓存")
854	
855	    # Ensure directories exist
856	    _distill_tmp_dir(project).mkdir(parents=True, exist_ok=True)
857	    _paths.project_skills_dir(project).mkdir(parents=True, exist_ok=True)
858	
859	    # Snapshot existing cached YAMLs so a failed session doesn't pollute
860	    # the cache with half-written Layer 1 outputs.
861	    pre_existing_cache = {p.name for p in _distill_tmp_dir(project).glob("*.yaml")}
862	
863	    # ── 2. Run Distiller Agent ──
864	    deep = min(len(new_to_analyze), max_deep_read)
865	    abstract = len(papers) - deep - len(cached_yamls)
866	    _log("精读", f"Distiller Agent 启动 ({deep} deep + {max(0, abstract)} abstract)")
867	    _patch_card("analyzing", stages=["collect"])
868	    _notify_ops("analyzing")
869	
870	    prompt = _build_distiller_prompt(new_to_analyze, cached_yamls, project, config)
871	    session_ok = await _run_distiller_session(project, prompt, config)
872	
873	    if not session_ok:
874	        _cleanup_partial_cache(project, pre_existing_cache)
875	        _log("失败", "Distiller session 执行失败")
876	        _patch_card("failed", stages=["collect"], error="Distiller session 失败")
877	        _notify_ops("failed", "session 执行失败")
878	        failure = DistillResult(
879	            success=False, project=project,
880	            paper_count=len(papers),
881	            error="Distiller session 执行失败",
882	        )
883	        _fire_completion_callback(failure, callback_url)
884	        return failure
885	
886	    # Verify outputs
887	    skill_info = _write_or_update_skills(project, papers)
888	
889	    if not skill_info["research_exists"] and not skill_info["writing_exists"]:
890	        _cleanup_partial_cache(project, pre_existing_cache)
891	        _log("失败", "未产出 skill 文件")
892	        _patch_card("failed", stages=["collect", "analyze"], error="未产出 skill")
893	        _notify_ops("failed", "未产出 skill 文件")
894	        failure = DistillResult(
895	            success=False, project=project,
896	            paper_count=len(papers),
897	            error="Distiller session 完成但未产出 skill 文件",
898	        )
899	        _fire_completion_callback(failure, callback_url)
900	        return failure
901	
902	    # Backfill new papers to literature_map
903	    backfilled = _backfill_literature_map(project, papers)
904	
905	    deep_count = min(len(new_to_analyze), max_deep_read) + len(cached_yamls)
906	    abstract_count = len(papers) - deep_count
907	
908	    result = DistillResult(
909	        success=True,
910	        project=project,
911	        version=max(skill_info.get("research_version", 0), skill_info.get("writing_version", 0)),
912	        paper_count=len(papers),
913	        deep_read_count=deep_count,
914	        abstract_only_count=max(0, abstract_count),
915	        new_papers_found=backfilled,
916	        research_skill_path=str(_paths.project_skills_dir(project) / "distilled-research.skill.md"),
917	        writing_skill_path=str(_paths.project_skills_dir(project) / "distilled-writing.skill.md"),
918	        research_skill_chars=skill_info.get("research_chars", 0),
919	        writing_skill_chars=skill_info.get("writing_chars", 0),
920	    )
921	
922	    # ── 3. Report ──
923	    summary = {
924	        "version": result.version,
925	        "deep_read_count": result.deep_read_count,
926	        "abstract_only_count": result.abstract_only_count,
927	        "research_skill_chars": result.research_skill_chars,
928	        "writing_skill_chars": result.writing_skill_chars,
929	        "new_papers_found": result.new_papers_found,
930	    }
931	    _log("完成", f"v{result.version}: research {result.research_skill_chars}字, writing {result.writing_skill_chars}字")
932	    _patch_card("done", stages=["collect", "analyze"], result_summary=summary)
933	    _notify_ops("done", f"v{result.version}, {result.paper_count} 篇")
934	
935	    # Inject [DISTILL] message into Director session (same pattern as
936	    # cron_hooks._route_to_director / dispatch_worker_done).
937	    _inject_distill_to_director(result, auto_trigger=auto_trigger)
938	
939	    # Fire callback so Manager can render the A群 Feishu notification.
940	    _fire_completion_callback(result, callback_url)
941	
942	    return result
943	
944	
945	def _fire_completion_callback(result: DistillResult, callback_url: str) -> None:
946	    """POST distillation result back to Manager (best-effort).
947	
948	    Includes the project's A群 chat_id so Manager can render the Feishu
949	    notification without an extra round-trip to BE for project config.
950	    Silently no-ops when ``callback_url`` is empty (manual MCP-tool path).
951	    """
952	    if not callback_url:
953	        return
954	
955	    chat_id = ""
956	    try:
957	        from core.tools.project_config import load_project_config
958	        cfg_result = load_project_config(result.project)
959	        if cfg_result.success and isinstance(cfg_result.data, dict):
960	            cfg = cfg_result.data.get("config", {})
961	            chat_id = (cfg.get("feishu") or {}).get("chat_id", "") or ""
962	    except Exception:
963	        logger.debug("[distill] failed to resolve chat_id for callback", exc_info=True)
964	
965	    try:
966	        from core.tools.distill_callbacks import DistillCallbacks
967	        emitter = DistillCallbacks.from_args(callback_url=callback_url)
968	        if emitter is None:
969	            return
970	        emitter.complete(
971	            project=result.project,
972	            status="completed" if result.success else "failed",
973	            version=result.version,
974	            paper_count=result.paper_count,
975	            deep_read_count=result.deep_read_count,
976	            abstract_only_count=result.abstract_only_count,
977	            new_papers_found=result.new_papers_found,
978	            research_skill_chars=result.research_skill_chars,
979	            writing_skill_chars=result.writing_skill_chars,
980	            chat_id=chat_id,
981	            error=result.error,
982	        )
983	    except Exception:
984	        logger.exception("[distill] completion callback failed for %s", result.project)
985	
986	
987	# ---------------------------------------------------------------------------
988	# Director session injection (mirrors cron_hooks pattern)
989	# ---------------------------------------------------------------------------
990	
991	def _inject_distill_to_director(result: DistillResult, auto_trigger: bool = False) -> None:
992	    """Inject ``[DISTILL]`` notification into the project's Director session.
993	
994	    Mirrors ``core.cron_hooks._route_to_director`` / ``dispatch_worker_done``:
995	    fact-only message (no skill loading), Director decides what to do next.
996	
997	    ``auto_trigger=True`` (bootstrap) sends a review-oriented message;
998	    ``auto_trigger=False`` (manual ``/distill``) sends an action-oriented
999	    message asking Director to review across three dimensions.
1000	    """
1001	    try:
1002	        from core.cron_hooks import _find_director_for_project
1003	        from core.session_server import get_server
1004	
1005	        director_info = _find_director_for_project(result.project)
1006	        if not director_info:
1007	            logger.info(
1008	                "[distill] no Director session for %s, skipping injection",
1009	                result.project,
1010	            )
1011	            return
1012	        director_key, _ = director_info
1013	
1014	        srv = get_server()
1015	        if not srv._started:
1016	            logger.info("[distill] SessionServer not started, skipping injection")
1017	            return
1018	
1019	        header = (
1020	            f"[DISTILL] 文献蒸馏已完成（v{result.version}，"
1021	            f"基于 {result.paper_count} 篇论文，精读 {result.deep_read_count} 篇）。\n"
1022	            f"研究方法论 skill：Read {result.research_skill_path}\n"
1023	            f"写作范式 skill：Read {result.writing_skill_path}"
1024	        )
1025	
1026	        if auto_trigger:
1027	            message = (
1028	                f"{header}\n"
1029	                f"请审阅蒸馏质量，确认是否准确。后续规划实验和论文写作时参考其中同行的做法和经验。"
1030	            )
1031	        else:
1032	            message = (
1033	                f"{header}\n\n"
1034	                f"请精读两个 skill，从相似和相关论文的经验中吸收可借鉴之处，对照当前项目审视：\n"
1035	                f"1. 研究方向：竞品的 claim 和我们是否重叠？蒸馏揭示的研究空白对 framing 有无启发？"
1036	                f"→ 需调整则更新 paper_framing.md + ROADMAP\n"
1037	                f"2. 实验计划：同行常用的 baseline/metric/dataset 是否已覆盖？方法论趋势对当前路线有无启发？"
1038	                f"→ 需调整则更新 experiment_plan.yaml\n"
1039	                f"3. 论文写作：同领域的叙事策略、结构惯例有无值得借鉴？"
1040	                f"→ 需调整则 director_post_to_paper_agent 通知\n"
1041	                f"判断后行动，用 director_reply_to_user 汇报审视结论和调整决定。"
1042	            )
1043	
1044	        def _silent_reply(reply: str) -> None:
1045	            logger.debug("[distill] Director reply silenced: %s", (reply or "")[:80])
1046	
1047	        srv.send_sync(
1048	            project=result.project,
1049	            message=message,
1050	            reply_fn=_silent_reply,
1051	            session_key=director_key,
1052	            source="distill:done",
1053	        )
1054	        logger.info("[distill] injected [DISTILL] into Director %s", director_key)
1055	    except Exception:
1056	        logger.exception(
1057	            "[distill] failed to inject [DISTILL] for project=%s", result.project,
1058	        )
1059	
1060	
1061	def _inject_distill_failure_to_director(result: DistillResult) -> bool:
1062	    """Inject guidance into Director when distill fails due to empty literature_map.
1063	
1064	    Returns True iff the Director session was found and the message was queued.
1065	    """
1066	    try:
1067	        from core.cron_hooks import _find_director_for_project
1068	        from core.session_server import get_server
1069	
1070	        director_info = _find_director_for_project(result.project)
1071	        if not director_info:
1072	            logger.info(
1073	                "[distill] no Director session for %s, failure guidance not delivered",
1074	                result.project,
1075	            )
1076	            return False
1077	        director_key, _ = director_info
1078	
1079	        srv = get_server()
1080	        if not srv._started:
1081	            return False
1082	
1083	        idea_brief = _paths.resolve_project_file(result.project, "IDEA_BRIEF.md")
1084	        ref_hint = (
1085	            f"参考 `{idea_brief}` 中的 key_references 和研究方向，"
1086	            if idea_brief.exists() else "通过深度文献调研，"
1087	        )
1088	
1089	        message = (
1090	            f"[DISTILL] 蒸馏失败：{result.error}\n\n"
1091	            f"`literature_map.yaml` 是蒸馏的输入源。请{ref_hint}"
1092	            f"用 `add_to_literature_map` 添加 ≥5 篇核心相关论文（含 S2 paper ID 或 arXiv ID），"
1093	            f"填充完毕后通知用户重新触发 `/distill`。"
1094	        )
1095	
1096	        def _silent_reply(reply: str) -> None:
1097	            logger.debug("[distill] Director reply silenced: %s", (reply or "")[:80])
1098	
1099	        srv.send_sync(
1100	            project=result.project,
1101	            message=message,
1102	            reply_fn=_silent_reply,
1103	            session_key=director_key,
1104	            source="distill:failed",
1105	        )
1106	        logger.info("[distill] injected [DISTILL] failure guidance into Director %s", director_key)
1107	        return True
1108	    except Exception:
1109	        logger.exception(
1110	            "[distill] failed to inject failure guidance for project=%s", result.project,
1111	        )
1112	        return False
1113	
1114	
1115	def _notify_user_of_distill_followup(project: str, chat_id: str) -> None:
1116	    """Notify A群 that Director was asked to fill literature_map after distill failure."""
1117	    if not chat_id:
1118	        return
1119	    try:
1120	        from core.tools.feishu import send_message
1121	        send_message(
1122	            chat_id=chat_id,
1123	            text=(
1124	                f"📚 {project} 的文献蒸馏暂时无法进行：literature_map 为空。\n"
1125	                f"已请 Director 参考 IDEA_BRIEF 的 key_references + 深度文献调研补充论文，"
1126	                f"完成后会再通知您触发 /distill。"
1127	            ),
1128	        )
1129	    except Exception:
1130	        logger.debug(
1131	            "[distill] failed to send A群 follow-up notice for %s", project, exc_info=True,
1132	        )
1133	
1134	
1135	# ---------------------------------------------------------------------------
1136	# Cache cleanup
1137	# ---------------------------------------------------------------------------
1138	
1139	def _cleanup_partial_cache(project: str, pre_existing: set[str]) -> None:
1140	    """Remove Layer 1 YAML files written during a failed run.
1141	
1142	    Files present before the run are preserved (those are valid cached
1143	    analyses from prior successful runs). Only new partial writes get cleaned.
1144	    """
1145	    try:
1146	        tmp_dir = _distill_tmp_dir(project)
1147	        if not tmp_dir.exists():
1148	            return
1149	        for yaml_file in tmp_dir.glob("*.yaml"):
1150	            if yaml_file.name not in pre_existing:
1151	                yaml_file.unlink(missing_ok=True)
1152	        logger.info("[distill] cleaned partial cache for %s", project)
1153	    except Exception:
1154	        logger.exception("[distill] cache cleanup failed for %s", project)
1155	
1156	
1157	# ---------------------------------------------------------------------------
1158	# MCP tool wrapper
1159	# ---------------------------------------------------------------------------
1160	
1161	def distill_papers(project: str, force: bool = False) -> ToolResult:
1162	    """从文献库蒸馏研究方法论和写作范式，生成项目专属 skill。
1163	
1164	    自动收集 literature_map + Semantic Scholar 论文，
1165	    用 Claude 分析后生成/更新 distilled-research 和 distilled-writing skill。
1166	
1167	    Args:
1168	        project: 项目名称
1169	        force: True 则忽略"无新论文"检查，强制重新蒸馏
1170	    """
1171	    try:
1172	        loop = asyncio.get_running_loop()
1173	    except RuntimeError:
1174	        loop = None
1175	
1176	    if loop and loop.is_running():
1177	        import concurrent.futures
1178	        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
1179	            result = pool.submit(
1180	                lambda: asyncio.run(distill_project_skills(project, force=force))
1181	            ).result(timeout=1860)
1182	    else:
1183	        result = asyncio.run(distill_project_skills(project, force=force))
1184	
1185	    if not result.success:
1186	        return ToolResult(success=False, error=result.error)
1187	
1188	    return ToolResult(
1189	        success=True,
1190	        data={
1191	            "project": result.project,
1192	            "version": result.version,
1193	            "paper_count": result.paper_count,
1194	            "deep_read_count": result.deep_read_count,
1195	            "abstract_only_count": result.abstract_only_count,
1196	            "new_papers_found": result.new_papers_found,
1197	            "research_skill_path": result.research_skill_path,
1198	            "writing_skill_path": result.writing_skill_path,
1199	            "research_skill_chars": result.research_skill_chars,
1200	            "writing_skill_chars": result.writing_skill_chars,
1201	            "summary": (
1202	                f"📚 {project} 文献蒸馏完成 (v{result.version})\n"
1203	                f"├ 精读论文：{result.deep_read_count} 篇（全文）"
1204	                f"+ {result.abstract_only_count} 篇（仅摘要）\n"
1205	                f"├ 研究方法论 skill：{result.research_skill_chars} 字\n"
1206	                f"├ 写作范式 skill：{result.writing_skill_chars} 字\n"
1207	                f"└ 新发现论文：{result.new_papers_found} 篇已回写 literature_map"
1208	            ),
1209	        },
1210	    )
1211	
1212	
1213	# ---------------------------------------------------------------------------
1214	# Status query
1215	# ---------------------------------------------------------------------------
1216	
1217	def get_distill_status(project: str) -> ToolResult:
1218	    """查看蒸馏状态：最后蒸馏时间、论文数、version。
1219	
1220	    `literature_map_total` 和 `cached_layer1_count` 即使在 never_distilled 时也
1221	    返回真实值——caller 用这两个字段排查"为啥蒸馏跑不动/没产出"，所以不能因为没
1222	    skill 文件就早退。
1223	    """
1224	    from core.tools.literature import get_literature_map_path, _read_map
1225	
1226	    skills_dir = _paths.project_skills_dir(project)
1227	    research_path = skills_dir / "distilled-research.skill.md"
1228	    writing_path = skills_dir / "distilled-writing.skill.md"
1229	    tmp_dir = _distill_tmp_dir(project)
1230	
1231	    lit_path = get_literature_map_path(project)
1232	    lit_map = _read_map(lit_path)
1233	    literature_map_total = len(lit_map.get("papers") or {})
1234	    cached_count = len(list(tmp_dir.glob("*.yaml"))) if tmp_dir.exists() else 0
1235	
1236	    if not research_path.exists() and not writing_path.exists():
1237	        return ToolResult(
1238	            success=True,
1239	            data={
1240	                "status": "never_distilled",
1241	                "project": project,
1242	                "literature_map_total": literature_map_total,
1243	                "cached_layer1_count": cached_count,
1244	            },
1245	        )
1246	
1247	    info: dict[str, Any] = {
1248	        "project": project,
1249	        "status": "distilled",
1250	        "literature_map_total": literature_map_total,
1251	        "cached_layer1_count": cached_count,
1252	    }
1253	
1254	    for label, path in [("research", research_path), ("writing", writing_path)]:
1255	        if path.exists():
1256	            text = path.read_text(encoding="utf-8")
1257	            fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
1258	            if fm_match:
1259	                fm = yaml.safe_load(fm_match.group(1)) or {}
1260	                info[f"{label}_version"] = fm.get("version", 1)
1261	                df = fm.get("distilled_from") or {}
1262	                info[f"{label}_paper_count"] = df.get("paper_count", 0)
1263	                info[f"{label}_last_distilled"] = df.get("last_distilled", "")
1264	                info[f"{label}_chars"] = len(text)
1265	
1266	    # Delta since last distill
1267	    existing_keys = _get_existing_paper_keys(project)
1268	    all_keys = set((lit_map.get("papers") or {}).keys())
1269	    delta = len(all_keys - existing_keys) if existing_keys else 0
1270	    info["new_since_last_distill"] = delta
1271	
1272	    return ToolResult(success=True, data=info)
1273	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e2c16bf-0e90-43b3-b661-c643af88e780",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "6446f3b4-e1e8-4ebc-9ad1-f31a14e17bb0",
  "sourceToolAssistantUUID": "0e2c16bf-0e90-43b3-b661-c643af88e780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-20T14:17:27.209Z_

Now let me search for how `get_distill_status` is used and any other related functions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6446f3b4-e1e8-4ebc-9ad1-f31a14e17bb0",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxsXkGYQuATfZYHzLK3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "27d25f17-7390-4733-b125-540f03c1eef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HLMMQQThQDQTAh8uVzE6iA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25448,
      "cache_read_input_tokens": 40161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25448,
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

_source line 15 · 2026-05-20T14:17:27.875Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AzQEyEABL4Lyw4gudhJKgC`</summary>

```json
{
  "pattern": "def.*distill|literature_map_total",
  "path": "/home/ubuntu/agent-ml-research/core/tools",
  "type": "py",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27d25f17-7390-4733-b125-540f03c1eef3",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxsXkGYQuATfZYHzLK3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98fbf736-82b6-445d-8966-8ca0250137d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HLMMQQThQDQTAh8uVzE6iA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 25448,
      "cache_read_input_tokens": 40161,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 150,
          "cache_read_input_tokens": 40161,
          "cache_creation_input_tokens": 25448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25448,
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

_source line 16 · 2026-05-20T14:17:27.898Z_

<details><summary>↩ Tool result · `toolu_01AzQEyEABL4Lyw4gudhJKgC`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/distill_card.py:133:def build_distill_card(
/home/ubuntu/agent-ml-research/core/tools/distill_card.py:213:def send_distill_card(
/home/ubuntu/agent-ml-research/core/tools/distill_card.py:244:def patch_distill_card(
/home/ubuntu/agent-ml-research/core/tools/distill.py:57:def _load_distill_config() -> dict[str, Any]:
/home/ubuntu/agent-ml-research/core/tools/distill.py:337:def _distill_tmp_dir(project: str) -> Path:
/home/ubuntu/agent-ml-research/core/tools/distill.py:390:def _build_distiller_prompt(
/home/ubuntu/agent-ml-research/core/tools/distill.py:473:async def _run_distiller_session(
/home/ubuntu/agent-ml-research/core/tools/distill.py:599:def _ensure_distiller_mcp_config() -> Path:
/home/ubuntu/agent-ml-research/core/tools/distill.py:691:async def distill_project_skills(
/home/ubuntu/agent-ml-research/core/tools/distill.py:991:def _inject_distill_to_director(result: DistillResult, auto_trigger: bool = False) -> None:
/home/ubuntu/agent-ml-research/core/tools/distill.py:1061:def _inject_distill_failure_to_director(result: DistillResult) -> bool:
/home/ubuntu/agent-ml-research/core/tools/distill.py:1115:def _notify_user_of_distill_followup(project: str, chat_id: str) -> None:
/home/ubuntu/agent-ml-research/core/tools/distill.py:1161:def distill_papers(project: str, force: bool = False) -> ToolResult:
/home/ubuntu/agent-ml-research/core/tools/distill.py:1217:def get_distill_status(project: str) -> ToolResult:
/home/ubuntu/agent-ml-research/core/tools/distill.py:1220:    `literature_map_total` 和 `cached_layer1_count` 即使在 never_distilled 时也
/home/ubuntu/agent-ml-research/core/tools/distill.py:1233:    literature_map_total = len(lit_map.get("papers") or {})
/home/ubuntu/agent-ml-research/core/tools/distill.py:1242:                "literature_map_total": literature_map_total,
/home/ubuntu/agent-ml-research/core/tools/distill.py:1250:        "literature_map_total": literature_map_total,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98fbf736-82b6-445d-8966-8ca0250137d3",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "5579c659-fe9d-4675-9f4a-3550adaaee2c",
  "sourceToolAssistantUUID": "98fbf736-82b6-445d-8966-8ca0250137d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T14:17:30.715Z_

Perfect! Now let me check what `_paths.resolve_project_file` does and how the literature map path is constructed:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5579c659-fe9d-4675-9f4a-3550adaaee2c",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxssxhE9s64nuN6Ehak",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb4efbbd-5b5e-41fa-9c43-a18d4fd1a8c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011M1z6KxufUeUkGWw1PoitP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 65609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 884,
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

_source line 18 · 2026-05-20T14:17:30.902Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01STWcNuxda33o1UnwTEfvN6`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/core -name \"paths.py\" -o -name \"paths\" -type d | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb4efbbd-5b5e-41fa-9c43-a18d4fd1a8c4",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxssxhE9s64nuN6Ehak",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "761d413c-206d-442e-815f-6ccdbd712f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011M1z6KxufUeUkGWw1PoitP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 65609,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 113,
          "cache_read_input_tokens": 65609,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 884,
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

_source line 19 · 2026-05-20T14:17:30.969Z_

<details><summary>↩ Tool result · `toolu_01STWcNuxda33o1UnwTEfvN6`</summary>

```text
/home/ubuntu/agent-ml-research/core/paths.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "761d413c-206d-442e-815f-6ccdbd712f8a",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "1c24e3f3-c00a-4ecf-83f9-045a65801963",
  "sourceToolAssistantUUID": "761d413c-206d-442e-815f-6ccdbd712f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T14:17:32.641Z_

<details open><summary>🔧 Tool call — Read · `toolu_017sCw1RyChr9cAYT5f5U5kj`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/paths.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c24e3f3-c00a-4ecf-83f9-045a65801963",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxt78xKEBGrum6QSvNx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b833305a-2c7f-49b8-b2a1-51dc1cee1d4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PhJf4duRp2BDqY8mGjJbNu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 66493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 140,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 21 · 2026-05-20T14:17:32.653Z_

<details><summary>↩ Tool result · `toolu_017sCw1RyChr9cAYT5f5U5kj`</summary>

```text
1	"""Centralized path resolution & tiny shared helpers.
2	
3	Separates framework code (REPO_ROOT) from user data (WORKSPACE_ROOT).
4	
5	REPO_ROOT:       Always the git repository root (framework code, skills/, CLAUDE.md).
6	WORKSPACE_ROOT:  User data root, resolved as:
7	                   1. Environment variable AGENT_ML_WORKSPACE
8	                   2. Default ~/.agent-ml-research/
9	
10	All paths are exposed as functions (not import-time constants) to support
11	test-time override via _override_workspace_root().
12	"""
13	
14	from __future__ import annotations
15	
16	import shutil
17	from datetime import datetime, timezone
18	from pathlib import Path
19	
20	
21	# ---------------------------------------------------------------------------
22	# Shared helpers (used by registry, cron, approvals, etc.)
23	# ---------------------------------------------------------------------------
24	
25	def now_iso() -> str:
26	    """UTC ISO-8601 timestamp with milliseconds — e.g. '2026-03-29T12:34:56.123Z'.
27	
28	    Includes milliseconds so that events within the same second are
29	    distinguishable (e.g. registry sort-by-updated_at).
30	    """
31	    now = datetime.now(timezone.utc)
32	    return now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{now.microsecond // 1000:03d}Z"
33	
34	# ---------------------------------------------------------------------------
35	# Root directories
36	# ---------------------------------------------------------------------------
37	
38	REPO_ROOT: Path = Path(__file__).resolve().parents[1]
39	
40	_DEFAULT_WORKSPACE = Path.home() / ".agent-ml-research"
41	
42	
43	def _resolve_workspace() -> Path:
44	    import os
45	    env = os.environ.get("AGENT_ML_WORKSPACE")
46	    if env:
47	        return Path(env).expanduser().resolve()
48	    return _DEFAULT_WORKSPACE
49	
50	
51	WORKSPACE_ROOT: Path = _resolve_workspace()
52	
53	
54	def _override_workspace_root(path: Path) -> None:
55	    """Test-only: redirect all workspace paths to *path*."""
56	    global WORKSPACE_ROOT
57	    WORKSPACE_ROOT = path.resolve()  # resolve symlinks (macOS /var → /private/var)
58	
59	
60	# ---------------------------------------------------------------------------
61	# Workspace paths (user data)
62	# ---------------------------------------------------------------------------
63	
64	def workspace_yaml_path() -> Path:
65	    return WORKSPACE_ROOT / "workspace.yaml"
66	
67	
68	def config_dir() -> Path:
69	    return WORKSPACE_ROOT / "config"
70	
71	
72	def projects_config_dir() -> Path:
73	    return WORKSPACE_ROOT / "config" / "projects"
74	
75	
76	def global_dir() -> Path:
77	    """Cross-project operational data (logs, worker registry, approvals)."""
78	    return WORKSPACE_ROOT / "global"
79	
80	
81	def experiments_dir() -> Path:
82	    """Backward-compat alias for global_dir()."""
83	    return global_dir()
84	
85	
86	def project_dir(project: str) -> Path:
87	    """Per-project root — all project data lives here."""
88	    return WORKSPACE_ROOT / "projects" / project
89	
90	
91	def project_docs_dir(project: str) -> Path:
92	    """Per-project human-readable docs (MODELS.md, ARCHITECTURE.md, README.md, etc.).
93	
94	    New layout: projects/{project}/docs/
95	    Fallback:   projects/{project}/  (un-migrated projects)
96	    """
97	    return WORKSPACE_ROOT / "projects" / project / "docs"
98	
99	
100	def verification_package_dir(project: str, study_id: str) -> Path:
101	    """Per-study verification package output directory."""
102	    return WORKSPACE_ROOT / "projects" / project / "verification-package" / study_id
103	
104	
105	def project_agent_dir(project: str) -> Path:
106	    """Per-project agent operational files (registry.yaml, report.md, etc.).
107	
108	    V3 layout: files live at project root (projects/{project}/).
109	    V2 legacy:  projects/{project}/agent/ (still supported as read fallback).
110	    """
111	    return project_dir(project)
112	
113	
114	def project_claude_dir(project: str) -> Path:
115	    """Per-project .claude/ directory — SESSION files + skills symlink."""
116	    return project_dir(project) / ".claude"
117	
118	
119	# --- Docs files (human-readable knowledge) ---
120	_DOCS_FILES = frozenset({
121	    "MODELS.md", "DATA.md", "ARCHITECTURE.md", "EVALUATION.md",
122	    "README.md", "research_plan.md", "progress.md",
123	})
124	
125	# --- Agent files (machine-consumed operational state) ---
126	_AGENT_FILES = frozenset({
127	    "registry.yaml", "report.md", "ideas.md", "memory.md",
128	    "ROADMAP.md", "decisions.yaml", "constraints.yaml", "mistakes.yaml",
129	    "paper_provenance.yaml", "experiment_matrix.yaml", "literature_map.yaml",
130	    "paper_checklist.yaml", "experiment_plan.yaml",
131	    "paper_framing.md",
132	})
133	
134	
135	def _is_migrated_v3(project: str) -> bool:
136	    """Check whether a project uses the V3 flat layout (.claude/ + root files)."""
137	    proj = project_dir(project)
138	    return (proj / ".claude").is_dir()
139	
140	
141	def resolve_project_file(project: str, filename: str) -> Path:
142	    """Resolve a project file with V3-layout-first, legacy-fallback.
143	
144	    Priority chain (returns first that exists, or default write path):
145	      SESSION_*.md  → .claude/ → agent/ (legacy) → .claude/ (write default)
146	      docs files    → docs/    → project root (legacy)
147	      agent files   → project root → agent/ (legacy)
148	    """
149	    proj = project_dir(project)
150	
151	    if filename.startswith("SESSION_"):
152	        # V3: SESSION files live in .claude/
153	        new = project_claude_dir(project) / filename
154	        if new.exists():
155	            return new
156	        # Legacy V2: agent/ subdir
157	        legacy = proj / "agent" / filename
158	        if legacy.exists():
159	            return legacy
160	        return new  # write default
161	
162	    if filename in _DOCS_FILES or filename.startswith("results/"):
163	        new = project_docs_dir(project) / filename
164	        if new.exists():
165	            return new
166	        old = proj / filename
167	        if old.exists():
168	            return old
169	        return new
170	
171	    if filename in _AGENT_FILES:
172	        # V3: agent files at project root
173	        new = proj / filename
174	        if new.exists():
175	            return new
176	        # Legacy V2: agent/ subdir
177	        legacy = proj / "agent" / filename
178	        if legacy.exists():
179	            return legacy
180	        return new  # write default
181	
182	    # Unknown file — project root
183	    return proj / filename
184	
185	
186	def migrate_project_layout(project: str) -> bool:
187	    """V2→V3 migration: flatten agent/ into project root, SESSION→.claude/.
188	
189	    Moves:
190	      agent/{registry,report,ideas,memory}.md → project root
191	      agent/SESSION_*.md → .claude/
192	      agent/checkpoints/ → project root/checkpoints/
193	    Leaves docs/ untouched.  Idempotent — safe to call repeatedly.
194	
195	    Returns True if any files were moved.
196	    """
197	    import logging
198	    logger = logging.getLogger(__name__)
199	
200	    proj = project_dir(project)
201	    if not proj.is_dir():
202	        return False
203	
204	    agent = proj / "agent"
205	    claude = proj / ".claude"
206	
207	    # Ensure docs subdirs exist
208	    docs = proj / "docs"
209	    if not docs.is_dir():
210	        docs.mkdir(exist_ok=True)
211	    (docs / "results").mkdir(exist_ok=True)
212	    (docs / "results" / "figures").mkdir(exist_ok=True)
213	    (docs / "paper").mkdir(exist_ok=True)
214	
215	    if not agent.is_dir():
216	        # No agent/ dir — nothing to migrate (already V3 or brand-new)
217	        claude.mkdir(exist_ok=True)
218	        return False
219	
220	    claude.mkdir(exist_ok=True)
221	    moved = []
222	
223	    # Move agent files to project root
224	    for f in _AGENT_FILES:
225	        src = agent / f
226	        dst = proj / f
227	        if src.exists() and not dst.exists():
228	            src.rename(dst)
229	            moved.append(f"  agent/{f} → {f}")
230	
231	    # Move SESSION_*.md → .claude/
232	    for src in agent.glob("SESSION_*.md"):
233	        dst = claude / src.name
234	        if not dst.exists():
235	            src.rename(dst)
236	            moved.append(f"  agent/{src.name} → .claude/{src.name}")
237	
238	    # Move checkpoints/ → project root
239	    src_ck = agent / "checkpoints"
240	    dst_ck = proj / "checkpoints"
241	    if src_ck.is_dir() and not dst_ck.exists():
242	        src_ck.rename(dst_ck)
243	        moved.append("  agent/checkpoints/ → checkpoints/")
244	
245	    # Clean up leftover non-essential files (e.g. registry.lock)
246	    for leftover in agent.iterdir():
247	        if leftover.name.startswith("."):
248	            continue
249	        if leftover.is_file() and leftover.suffix in (".lock", ".tmp"):
250	            leftover.unlink()
251	            moved.append(f"  agent/{leftover.name} (removed, stale)")
252	
253	    # Remove agent/ if empty
254	    try:
255	        agent.rmdir()
256	        moved.append("  agent/ (removed, empty)")
257	    except OSError:
258	        pass  # still has files
259	
260	    if moved:
261	        logger.info("V3-migrated project '%s':\n%s", project, "\n".join(moved))
262	    return bool(moved)
263	
264	
265	# Config files
266	def resources_yaml() -> Path:
267	    return config_dir() / "resources.yaml"
268	
269	
270	def images_yaml() -> Path:
271	    """Framework-level image registry (lives in repo, not workspace)."""
272	    return REPO_ROOT / "config" / "images.yaml"
273	
274	
275	def feishu_yaml() -> Path:
276	    return config_dir() / "feishu.yaml"
277	
278	
279	def feishu_sync_yaml() -> Path:
280	    return config_dir() / "feishu_sync.yaml"
281	
282	
283	def session_state_json() -> Path:
284	    return config_dir() / "session_state.json"
285	
286	
287	def ralph_loop_yaml() -> Path:
288	    return config_dir() / "ralph_loop.yaml"
289	
290	
291	def ralph_loop_timeline_path(project: str) -> Path:
292	    return project_dir(project) / "logs" / "ralph_loop_timeline.jsonl"
293	
294	
295	def task_context_dir(project: str) -> Path:
296	    return project_dir(project) / "task_context"
297	
298	
299	def sandbox_yaml() -> Path:
300	    return config_dir() / "sandbox.yaml"
301	
302	
303	def skills_yaml() -> Path:
304	    return config_dir() / "skills.yaml"
305	
306	
307	def crons_yaml() -> Path:
308	    return config_dir() / "crons.yaml"
309	
310	
311	def review_policy_yaml() -> Path:
312	    return config_dir() / "review_policy.yaml"
313	
314	
315	def backend_yaml() -> Path:
316	    """BE-side opt-in config for Manager integration (see MANAGER_SPEC §6.2)."""
317	    return config_dir() / "backend.yaml"
318	
319	
320	def gpu_pool_yaml() -> Path:
321	    """Manager-maintained global GPU pool — ownership allocations across projects."""
322	    return config_dir() / "gpu_pool.yaml"
323	
324	
325	def approvals_yaml() -> Path:
326	    return config_dir() / "approvals.yaml"
327	
328	
329	def approvals_store_yaml() -> Path:
330	    """Global approvals file — stays global since approvals need cross-project lookup."""
331	    return experiments_dir() / "approvals.yaml"
332	
333	
334	# Experiment data — global (cross-project operational logs)
335	def usage_log_path() -> Path:
336	    return experiments_dir() / "logs" / "usage.jsonl"
337	
338	
339	def weights_cache_path() -> Path:
340	    """Persisted quota weights — survives quiet periods and process restarts."""
341	    return experiments_dir() / "logs" / "weights_cache.json"
342	
343	
344	def cron_poll_log_path() -> Path:
345	    return experiments_dir() / "logs" / "cron_polls.jsonl"
346	
347	
348	def session_events_log_path() -> Path:
349	    return experiments_dir() / "logs" / "session_events.jsonl"
350	
351	
352	# Per-project logs (with global fallback for no-project sessions)
353	def chats_dir(project: str | None = None) -> Path:
354	    if project:
355	        return project_dir(project) / "logs" / "chats"
356	    return experiments_dir() / "logs" / "chats"
357	
358	
359	def chats_archive_dir(project: str | None = None) -> Path:
360	    if project:
361	        return project_dir(project) / "logs" / "chats" / "archive"
362	    return experiments_dir() / "logs" / "chats" / "archive"
363	
364	
365	def workers_dir(project: str | None = None) -> Path:
366	    if project:
367	        return project_dir(project) / "logs" / "workers"
368	    return experiments_dir() / "logs" / "workers"
369	
370	
371	def session_archive_dir() -> Path:
372	    return experiments_dir() / "logs" / "session_archive"
373	
374	
375	def pending_queue_dir() -> Path:
376	    return experiments_dir() / "logs" / "pending_queue"
377	
378	
379	def logs_dir() -> Path:
380	    """Global operational logs root."""
381	    return experiments_dir() / "logs"
382	
383	
384	def checkpoints_dir(project: str | None = None) -> Path:
385	    if project:
386	        # V3: checkpoints at project root
387	        new = project_dir(project) / "checkpoints"
388	        if new.exists():
389	            return new
390	        # Legacy V2: agent/checkpoints
391	        legacy = project_dir(project) / "agent" / "checkpoints"
392	        if legacy.exists():
393	            return legacy
394	        return new  # write default
395	    return experiments_dir() / "checkpoints"
396	
397	
398	def deploys_path(project: str) -> Path:
399	    """Per-project deploy history (single yaml file)."""
400	    return project_dir(project) / "deploys.yaml"
401	
402	
403	def backups_path(project: str) -> Path:
404	    """Per-project backup history (single yaml file)."""
405	    return project_dir(project) / "backups.yaml"
406	
407	
408	# Legacy global dirs — kept as read fallback for pai_eas/oss_backup migration
409	def deploys_dir() -> Path:
410	    return experiments_dir() / "deploys"
411	
412	
413	def backups_dir() -> Path:
414	    return experiments_dir() / "backups"
415	
416	
417	def global_literature_map_path() -> Path:
418	    """Global literature_map.yaml — shared across the Idea phase (no project).
419	
420	    Each entry carries a ``source_idea_id`` so that multiple ideas can coexist
421	    in this file without collision. On project creation, the matching entries
422	    are seeded into the project-level ``literature_map.yaml``.
423	    """
424	    return WORKSPACE_ROOT / "literature_map.yaml"
425	
426	
427	def idea_generator_dir() -> Path:
428	    """Idea Generator data — ideas.yaml lives here."""
429	    return WORKSPACE_ROOT / "idea_generator"
430	
431	
432	def idea_generator_logs_dir() -> Path:
433	    """Process logs for idea generation runs."""
434	    return idea_generator_dir() / "logs"
435	
436	
437	def project_artifacts_dir(project: str) -> Path:
438	    """Per-project artifact root — contains _project/ and {exp_id}/ subdirs."""
439	    return project_dir(project) / "artifacts"
440	
441	
442	def project_data_snapshots_dir(project: str) -> Path:
443	    """Per-project data snapshots — generated by data-snapshot worker."""
444	    return project_dir(project) / "data_snapshots"
445	
446	
447	def dream_reports_dir(project: str) -> Path:
448	    """Root directory for all Dream Tool reports of a project.
449	
450	    Layout: projects/{project}/artifacts/dream_reports/{dream_id}/...
451	    Kept inside ``artifacts/`` so Dream outputs flow through the same
452	    backup/cleanup paths as other run artifacts.
453	    """
454	    return project_artifacts_dir(project) / "dream_reports"
455	
456	
457	def dream_report_dir(project: str, dream_id: str) -> Path:
458	    """Per-dream report directory.
459	
460	    Holds three tier subdirectories (best/median/worst), the synthesized
461	    meta.yaml, and ``logs/`` for subprocess stdout/stderr.
462	    """
463	    if not dream_id:
464	        raise ValueError("dream_id is required")
465	    return dream_reports_dir(project) / dream_id
466	
467	
468	def dream_registry_path(project: str) -> Path:
469	    """Persistent state for in-flight Dream runs."""
470	    return project_dir(project) / "dream_registry.yaml"
471	
472	
473	# ---------------------------------------------------------------------------
474	# Repo paths (framework code — always in git)
475	# ---------------------------------------------------------------------------
476	
477	def skills_dir() -> Path:
478	    """Built-in skills (global/ and plugins/) — shipped with the framework."""
479	    return REPO_ROOT / "skills"
480	
481	
482	def project_skills_dir(project: str) -> Path:
483	    """Project-specific skills — user data, lives in workspace."""
484	    return WORKSPACE_ROOT / "skills" / "projects" / project
485	
486	
487	def claude_md() -> Path:
488	    return REPO_ROOT / "CLAUDE.md"
489	
490	
491	def pool_status_path() -> Path:
492	    """Watchdog-written Claude pool status (shared with cost_tracker & usage API)."""
493	    return Path("/tmp/claude_pool_status.json")
494	
495	
496	def pool_state_persisted_path() -> Path:
497	    """Persisted snapshot of last-seen pool state (used by pool_state_watcher
498	    to detect transitions across BE restarts — without this the watcher would
499	    re-emit a flood of "rate_limit_hit" events on every restart)."""
500	    return WORKSPACE_ROOT / "state" / "pool_state_last.json"
501	
502	
503	def dashboard_dist() -> Path:
504	    return REPO_ROOT / "dashboard" / "dist"
505	
506	
507	def portal_dist() -> Path:
508	    return REPO_ROOT / "portal" / "dist"
509	
510	
511	
512	# ---------------------------------------------------------------------------
513	# Workspace initialization
514	# ---------------------------------------------------------------------------
515	
516	_WORKSPACE_DIRS = [
517	    lambda: config_dir(),
518	    lambda: projects_config_dir(),
519	    lambda: global_dir(),
520	    lambda: logs_dir(),
521	    lambda: chats_dir(),
522	    lambda: chats_archive_dir(),
523	    lambda: workers_dir(),
524	    lambda: session_archive_dir(),
525	    lambda: pending_queue_dir(),
526	    lambda: WORKSPACE_ROOT / "projects",
527	    lambda: WORKSPACE_ROOT / "skills" / "projects",
528	    lambda: idea_generator_dir(),
529	]
530	
531	
532	def ensure_workspace() -> None:
533	    """Create workspace directory structure if it doesn't exist.
534	
535	    Idempotent — safe to call on every startup.
536	    Only creates directories and seed files that are missing.
537	    """
538	    # Migration: experiments/ → global/
539	    _old_exp = WORKSPACE_ROOT / "experiments"
540	    _new_global = global_dir()
541	    if _old_exp.is_dir() and not _new_global.exists():
542	        _old_exp.rename(_new_global)
543	        import logging as _logging
544	        _logging.getLogger(__name__).info("Migrated experiments/ → global/")
545	
546	    for dir_fn in _WORKSPACE_DIRS:
547	        dir_fn().mkdir(parents=True, exist_ok=True)
548	
549	    # Seed workspace.yaml
550	    ws_path = workspace_yaml_path()
551	    if not ws_path.exists():
552	        ws_path.write_text("projects: {}\n")
553	
554	    # Seed resources.yaml from repo template (if repo has one)
555	    res_path = resources_yaml()
556	    if not res_path.exists():
557	        repo_res = REPO_ROOT / "templates" / "resources.yaml"
558	        if repo_res.exists():
559	            shutil.copy2(repo_res, res_path)
560	        else:
561	            # Minimal default — pin to Opus 4.6 so new BE workspaces
562	            # don't silently fall back to Sonnet (BE bootstrap rule, see
563	            # also manager-side roles in service.py).
564	            res_path.write_text(
565	                "default_model: claude-opus-4-6\n"
566	                "default_model_claude_code: claude-opus-4-6\n"
567	                "idea_model: claude-opus-4-6\n"
568	                "servers: {}\nuser_rules: []\n"
569	            )
570	
571	    # Seed approvals.yaml from repo template
572	    apr_path = approvals_yaml()
573	    if not apr_path.exists():
574	        repo_apr = REPO_ROOT / "templates" / "approvals.yaml"
575	        if repo_apr.exists():
576	            shutil.copy2(repo_apr, apr_path)
577	
578	    # Workspace-level .claude/ for Idea stage (no_project)
579	    ws_claude = WORKSPACE_ROOT / ".claude"
580	    ws_claude.mkdir(exist_ok=True)
581	    # Symlink .claude/skills/ → skills/global/ for native skill discovery
582	    ws_skills_link = ws_claude / "skills"
583	    # Try workspace-local skills first (legacy layout), then framework repo skills
584	    skills_target = WORKSPACE_ROOT / "skills" / "global"
585	    if not skills_target.is_dir():
586	        skills_target = REPO_ROOT / "skills" / "global"
587	    if not ws_skills_link.exists() and skills_target.is_dir():
588	        try:
589	            ws_skills_link.symlink_to(skills_target)
590	        except OSError:
591	            pass  # e.g. Windows without symlink privileges
592	
593	    # Move stale root-level SESSION_*.md into .claude/ (Idea stage migration)
594	    for session_file in WORKSPACE_ROOT.glob("SESSION_*.md"):
595	        dest = ws_claude / session_file.name
596	        if not dest.exists():
597	            session_file.rename(dest)
598	
599	    # V3-migrate existing projects (agent/ → flat + .claude/)
600	    projects_root = WORKSPACE_ROOT / "projects"
601	    if projects_root.is_dir():
602	        for child in projects_root.iterdir():
603	            if child.is_dir() and not child.name.startswith("."):
604	                migrate_project_layout(child.name)
605	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b833305a-2c7f-49b8-b2a1-51dc1cee1d4c",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "d0db1be9-c2b8-4573-97c1-c1dba4fa4e05",
  "sourceToolAssistantUUID": "b833305a-2c7f-49b8-b2a1-51dc1cee1d4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-20T14:17:34.347Z_

Perfect! Now let me verify how the literature_map file should be structured by checking if there's an example or schema:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0db1be9-c2b8-4573-97c1-c1dba4fa4e05",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxtF3Tm6oVic5zUKGoZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58c9a430-4148-43d4-93e0-15aadd4c0882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0196mmpVtiMXKkFL66LSgUBq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6926,
      "cache_read_input_tokens": 66633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6926,
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

_source line 23 · 2026-05-20T14:17:34.721Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NtozKpRkPWhiZo6FMWHdK4`</summary>

```json
{
  "command": "find /home/ubuntu -name \"*literature_map*\" -type f 2>/dev/null | grep -v \".pyc\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c9a430-4148-43d4-93e0-15aadd4c0882",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxtF3Tm6oVic5zUKGoZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04d37ed1-7acc-4d6b-b523-1db88205959e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0196mmpVtiMXKkFL66LSgUBq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6926,
      "cache_read_input_tokens": 66633,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 111,
          "cache_read_input_tokens": 66633,
          "cache_creation_input_tokens": 6926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6926,
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

_source line 24 · 2026-05-20T14:17:35.099Z_

<details><summary>↩ Tool result · `toolu_01NtozKpRkPWhiZo6FMWHdK4`</summary>

```text
/home/ubuntu/agent-ml-research/tests/test_literature_map.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04d37ed1-7acc-4d6b-b523-1db88205959e",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "ddb903a4-6012-4e5a-a7c4-20dbc3598648",
  "sourceToolAssistantUUID": "04d37ed1-7acc-4d6b-b523-1db88205959e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T14:17:36.435Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LLGbaxR25wDkD4boLNs3MZ`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/tests/test_literature_map.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddb903a4-6012-4e5a-a7c4-20dbc3598648",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxtQks25Y1t7PDS9p69",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "234a2346-03e5-4268-91f8-6b4c6aef00b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VHpVWqv1QxhBZ5PqW1VN7q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 73559,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 72,
          "cache_read_input_tokens": 73559,
          "cache_creation_input_tokens": 212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 212,
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

_source line 26 · 2026-05-20T14:17:36.446Z_

<details><summary>↩ Tool result · `toolu_01LLGbaxR25wDkD4boLNs3MZ`</summary>

```text
1	"""Unit tests for core/tools/literature.py.
2	
3	Covers CRUD, dedup (DOI / title), cross-stage persistence (global → project seed),
4	and the read-mode taxonomy (summary / category / competitors / unverified / bib / full).
5	"""
6	
7	from __future__ import annotations
8	
9	import yaml
10	
11	import pytest
12	
13	from core import paths
14	from core.tools.literature import (
15	    VALID_READ_MODES,
16	    VALID_ROLES,
17	    _find_existing_key,
18	    _generate_bibtex_key,
19	    _merge_paper,
20	    _normalize_doi,
21	    _normalize_title,
22	    add_to_literature_map,
23	    get_literature_map_path,
24	    read_literature_map,
25	    seed_literature_map,
26	    update_literature_category,
27	    upsert_category,
28	)
29	
30	
31	# ---------------------------------------------------------------------------
32	# Sample papers
33	# ---------------------------------------------------------------------------
34	
35	VASWANI = {
36	    "title": "Attention Is All You Need",
37	    "authors": ["Vaswani, A.", "Shazeer, N."],
38	    "year": 2017,
39	    "venue": "NeurIPS",
40	    "doi": "10.5555/3295222.3295349",
41	    "category": "attention",
42	    "role": "foundation",
43	    "abstract": "We propose a new simple network architecture, the Transformer.",
44	    "verified": True,
45	}
46	
47	BERT = {
48	    "title": "BERT: Pre-training of Deep Bidirectional Transformers",
49	    "authors": ["Devlin, J."],
50	    "year": 2018,
51	    "venue": "NAACL",
52	    "doi": "10.18653/v1/N19-1423",
53	    "category": "pretraining",
54	    "role": "direct-competitor",
55	    "verified": False,
56	}
57	
58	GPT3 = {
59	    "title": "Language Models are Few-Shot Learners",
60	    "authors": ["Brown, T."],
61	    "year": 2020,
62	    "venue": "NeurIPS",
63	    "doi": "",  # no doi available — title dedup path
64	    "category": "pretraining",
65	    "role": "background",
66	}
67	
68	
69	# ---------------------------------------------------------------------------
70	# Path resolution
71	# ---------------------------------------------------------------------------
72	
73	class TestPathResolution:
74	    def test_global_path_no_project(self, workspace):
75	        p = get_literature_map_path()
76	        assert p == paths.global_literature_map_path()
77	
78	    def test_project_path(self, workspace):
79	        p = get_literature_map_path("foo_proj")
80	        # V3 layout: project root, not under agent/
81	        assert p.name == "literature_map.yaml"
82	        assert "foo_proj" in str(p)
83	        assert p.parent.is_dir()  # auto-created
84	
85	
86	# ---------------------------------------------------------------------------
87	# Normalization helpers
88	# ---------------------------------------------------------------------------
89	
90	class TestNormalization:
91	    def test_normalize_title_lowercase_strip_punct(self):
92	        a = _normalize_title("Attention Is All You Need!")
93	        b = _normalize_title("attention is all you need")
94	        assert a == b
95	
96	    def test_normalize_title_strips_diacritics(self):
97	        assert _normalize_title("Résumé") == _normalize_title("Resume")
98	
99	    def test_normalize_title_smart_quotes_and_dashes(self):
100	        a = _normalize_title("Self-Attention’s Power")
101	        b = _normalize_title("self attention s power")
102	        assert a == b
103	
104	    def test_normalize_title_empty(self):
105	        assert _normalize_title("") == ""
106	        assert _normalize_title(None) == ""  # type: ignore[arg-type]
107	
108	    def test_normalize_doi_lowercases_strip_prefix(self):
109	        assert _normalize_doi("https://doi.org/10.1/AbC") == "10.1/abc"
110	        assert _normalize_doi("DOI:10.1/X") == "10.1/x"
111	        assert _normalize_doi("10.1/x") == "10.1/x"
112	        assert _normalize_doi("") == ""
113	
114	
115	# ---------------------------------------------------------------------------
116	# Bibtex key generation
117	# ---------------------------------------------------------------------------
118	
119	class TestBibtexKey:
120	    def test_first_author_year_word(self):
121	        key = _generate_bibtex_key(VASWANI)
122	        assert key == "vaswani2017attention"
123	
124	    def test_skips_stopwords_in_title(self):
125	        # "The Power of X" — first significant word should be "power"
126	        key = _generate_bibtex_key({
127	            "authors": ["Smith, J."],
128	            "year": 2024,
129	            "title": "The Power of Scale",
130	        })
131	        assert key == "smith2024power"
132	
133	    def test_handles_firstname_lastname_format(self):
134	        key = _generate_bibtex_key({
135	            "authors": ["Ashish Vaswani"],
136	            "year": 2017,
137	            "title": "Attention",
138	        })
139	        # Uses last word as surname when no comma
140	        assert key == "vaswani2017attention"
141	
142	    def test_fallback_when_metadata_missing(self):
143	        key = _generate_bibtex_key({"title": "Some Paper"})
144	        # No authors / year → must still produce something stable
145	        assert key  # non-empty
146	        # Falls back to title slug
147	        assert "some" in key or key.startswith("paper_")
148	
149	
150	# ---------------------------------------------------------------------------
151	# Read modes
152	# ---------------------------------------------------------------------------
153	
154	class TestReadModes:
155	    def test_empty_map_returns_skeleton(self, workspace):
156	        r = read_literature_map(mode="summary")
157	        assert r.success
158	        assert r.data["papers"] == {}
159	        assert r.data["categories"] == []
160	        assert r.data["meta"]["total_papers"] == 0
161	
162	    def test_summary_strips_long_fields(self, workspace):
163	        add_to_literature_map(papers=[VASWANI])
164	        r = read_literature_map(mode="summary")
165	        assert r.success
166	        # summary mode drops abstract / relevance
167	        for p in r.data["papers"].values():
168	            assert "abstract" not in p
169	            assert "relevance" not in p
170	            assert "title" in p
171	            assert "verified" in p
172	
173	    def test_full_mode_returns_everything(self, workspace):
174	        add_to_literature_map(papers=[VASWANI])
175	        r = read_literature_map(mode="full")
176	        assert r.success
177	        entry = next(iter(r.data["papers"].values()))
178	        assert entry["abstract"]
179	        assert "added_at" in entry
180	
181	    def test_competitors_mode_filters_role(self, workspace):
182	        add_to_literature_map(papers=[VASWANI, BERT, GPT3])
183	        r = read_literature_map(mode="competitors")
184	        assert r.success
185	        for p in r.data["papers"].values():
186	            assert p["role"] == "direct-competitor"
187	        # BERT is the only direct-competitor
188	        assert len(r.data["papers"]) == 1
189	
190	    def test_unverified_mode_filters_unverified(self, workspace):
191	        add_to_literature_map(papers=[VASWANI, BERT, GPT3])
192	        r = read_literature_map(mode="unverified")
193	        assert r.success
194	        # VASWANI is verified — should NOT be in result
195	        for p in r.data["papers"].values():
196	            assert not p.get("verified")
197	        # BERT (verified=False) and GPT3 (default False)
198	        assert len(r.data["papers"]) == 2
199	
200	    def test_bib_mode_returns_keylist(self, workspace):
201	        add_to_literature_map(papers=[VASWANI, BERT])
202	        r = read_literature_map(mode="bib")
203	        assert r.success
204	        keys = r.data["bibtex_keys"]
205	        assert "vaswani2017attention" in keys
206	        assert any(k.startswith("devlin2018") for k in keys)
207	
208	    def test_category_scoped_read(self, workspace):
209	        add_to_literature_map(papers=[VASWANI, BERT, GPT3])
210	        upsert_category(key="pretraining", name="Pretraining")
211	        r = read_literature_map(mode="category:pretraining")
212	        assert r.success
213	        for p in r.data["papers"].values():
214	            assert p["category"] == "pretraining"
215	        assert len(r.data["papers"]) == 2  # BERT + GPT3
216	
217	    def test_unknown_mode_rejected(self, workspace):
218	        r = read_literature_map(mode="bogus")
219	        assert not r.success
220	        assert "Unknown mode" in r.error
221	
222	
223	# ---------------------------------------------------------------------------
224	# Add / dedup
225	# ---------------------------------------------------------------------------
226	
227	class TestAdd:
228	    def test_add_new_paper_creates_entry(self, workspace):
229	        r = add_to_literature_map(papers=[VASWANI], added_by="paper-research")
230	        assert r.success
231	        assert len(r.data["added"]) == 1
232	        assert r.data["total_papers"] == 1
233	
234	        # added_by + added_at recorded
235	        full = read_literature_map(mode="full").data["papers"]
236	        entry = next(iter(full.values()))
237	        assert entry["added_by"] == "paper-research"
238	        assert entry["added_at"]
239	
240	    def test_dedup_by_doi(self, workspace):
241	        add_to_literature_map(papers=[VASWANI])
242	        # Different title formatting but same DOI → must merge, not add
243	        dup = dict(VASWANI)
244	        dup["title"] = "ATTENTION IS ALL YOU NEED (with caps)"
245	        r = add_to_literature_map(papers=[dup])
246	        assert r.success
247	        assert len(r.data["added"]) == 0
248	        assert len(r.data["merged"]) == 1
249	        assert r.data["total_papers"] == 1
250	
251	    def test_dedup_by_normalized_title(self, workspace):
252	        # GPT3 has no DOI — fall back to title match
253	        add_to_literature_map(papers=[GPT3])
254	        dup = dict(GPT3)
255	        # Add weird punctuation
256	        dup["title"] = "language Models, ARE: Few-Shot Learners!!!"
257	        r = add_to_literature_map(papers=[dup])
258	        assert r.success
259	        assert len(r.data["merged"]) == 1
260	        assert r.data["total_papers"] == 1
261	
262	    def test_merge_fills_empty_fields_only(self, workspace):
263	        # First add with sparse data
264	        sparse = {"title": "Sparse Paper", "year": 2020}
265	        add_to_literature_map(papers=[sparse])
266	        # Then merge in fuller record (same title)
267	        rich = {
268	            "title": "Sparse Paper",
269	            "year": 2099,  # SHOULD NOT overwrite existing 2020
270	            "venue": "ICML",
271	            "authors": ["X, Y."],
272	        }
273	        add_to_literature_map(papers=[rich])
274	        entry = next(iter(read_literature_map(mode="full").data["papers"].values()))
275	        assert entry["year"] == 2020  # preserved
276	        assert entry["venue"] == "ICML"  # filled
277	        assert entry["authors"] == ["X, Y."]
278	
279	    def test_verified_true_wins(self, workspace):
280	        add_to_literature_map(papers=[{"title": "X", "verified": True}])
281	        add_to_literature_map(papers=[{"title": "X", "verified": False}])
282	        entry = next(iter(read_literature_map(mode="full").data["papers"].values()))
283	        assert entry["verified"] is True  # later False does NOT un-verify
284	
285	    def test_bibtex_key_collision_gets_suffix(self, workspace):
286	        # Two papers with same surname + year + first word — produces same key
287	        a = {"title": "Attention One", "authors": ["Vaswani, A."], "year": 2017}
288	        b = {"title": "Attention Two", "authors": ["Vaswani, B."], "year": 2017}
289	        add_to_literature_map(papers=[a])
290	        add_to_literature_map(papers=[b])
291	        full = read_literature_map(mode="full").data["papers"]
292	        keys = sorted(full.keys())
293	        assert "vaswani2017attention" in keys
294	        # Second one should have suffix appended
295	        assert any(k.startswith("vaswani2017attention_") for k in keys)
296	
297	    def test_invalid_role_rejected(self, workspace):
298	        bad = {"title": "Bad", "role": "not-a-real-role"}
299	        r = add_to_literature_map(papers=[bad])
300	        assert r.success  # call itself succeeds
301	        assert len(r.data["added"]) == 0
302	        assert len(r.data["rejected"]) == 1
303	        assert "invalid role" in r.data["rejected"][0]["reason"]
304	
305	    def test_missing_title_rejected(self, workspace):
306	        r = add_to_literature_map(papers=[{"year": 2024}])
307	        assert r.data["rejected"][0]["reason"] == "missing title"
308	
309	    def test_no_papers_error(self, workspace):
310	        r = add_to_literature_map(papers=[])
311	        assert not r.success
312	
313	    def test_non_dict_rejected(self, workspace):
314	        r = add_to_literature_map(papers=["not a dict"])  # type: ignore[list-item]
315	        assert r.data["rejected"][0]["reason"] == "not a dict"
316	
317	    def test_all_valid_roles_accepted(self, workspace):
318	        for role in VALID_ROLES:
319	            r = add_to_literature_map(papers=[{
320	                "title": f"Paper with {role}",
321	                "role": role,
322	            }])
323	            assert r.success
324	            assert len(r.data["added"]) == 1
325	
326	
327	# ---------------------------------------------------------------------------
328	# update_literature_category
329	# ---------------------------------------------------------------------------
330	
331	class TestUpdateCategory:
332	    def test_update_existing(self, workspace):
333	        add_to_literature_map(papers=[VASWANI])
334	        key = next(iter(read_literature_map(mode="full").data["papers"]))
335	        r = update_literature_category(
336	            paper_key=key, category="new_cat", role="background",
337	            relevance="seminal", verified=True,
338	        )
339	        assert r.success
340	        entry = read_literature_map(mode="full").data["papers"][key]
341	        assert entry["category"] == "new_cat"
342	        assert entry["role"] == "background"
343	        assert entry["relevance"] == "seminal"
344	        assert entry["verified"] is True
345	
346	    def test_update_partial_leaves_others_intact(self, workspace):
347	        add_to_literature_map(papers=[VASWANI])
348	        key = next(iter(read_literature_map(mode="full").data["papers"]))
349	        update_literature_category(paper_key=key, verified=False)
350	        entry = read_literature_map(mode="full").data["papers"][key]
351	        # Only verified changed — category/role still original
352	        assert entry["category"] == "attention"
353	        assert entry["role"] == "foundation"
354	        assert entry["verified"] is False
355	
356	    def test_unknown_paper_key_errors(self, workspace):
357	        r = update_literature_category(paper_key="nope", category="x")
358	        assert not r.success
359	        assert "not found" in r.error
360	
361	    def test_invalid_role_rejected(self, workspace):
362	        r = update_literature_category(paper_key="foo", role="bogus")
363	        assert not r.success
364	        assert "invalid role" in r.error
365	
366	
367	# ---------------------------------------------------------------------------
368	# upsert_category
369	# ---------------------------------------------------------------------------
370	
371	class TestUpsertCategory:
372	    def test_adds_new(self, workspace):
373	        r = upsert_category(key="attn", name="Attention", narrative="self-attn line")
374	        assert r.success
375	        assert r.data["action"] == "added"
376	        cats = read_literature_map(mode="full").data["categories"]
377	        assert cats[0]["key"] == "attn"
378	        assert cats[0]["narrative"] == "self-attn line"
379	
380	    def test_updates_existing(self, workspace):
381	        upsert_category(key="attn", name="Attention")
382	        r = upsert_category(key="attn", narrative="updated line")
383	        assert r.success
384	        assert r.data["action"] == "updated"
385	        cats = read_literature_map(mode="full").data["categories"]
386	        # Existing name kept (we only passed narrative the 2nd time)
387	        assert cats[0]["name"] == "Attention"
388	        assert cats[0]["narrative"] == "updated line"
389	        assert len(cats) == 1  # not duplicated
390	
391	    def test_missing_key_errors(self, workspace):
392	        r = upsert_category(key="")
393	        assert not r.success
394	
395	
396	# ---------------------------------------------------------------------------
397	# Cross-stage persistence: global → project seed
398	# ---------------------------------------------------------------------------
399	
400	class TestCrossStagePersistence:
401	    def test_global_and_project_maps_are_separate_files(self, workspace):
402	        add_to_literature_map(papers=[VASWANI])  # global
403	        add_to_literature_map(project="my_proj", papers=[BERT])  # project
404	
405	        global_papers = read_literature_map(mode="full").data["papers"]
406	        proj_papers = read_literature_map(project="my_proj", mode="full").data["papers"]
407	
408	        # Each map sees its own paper, not the other
409	        assert any("attention" in p["title"].lower() for p in global_papers.values())
410	        assert all("bert" not in p["title"].lower() for p in global_papers.values())
411	        assert any("bert" in p["title"].lower() for p in proj_papers.values())
412	
413	    def test_seed_propagates_global_into_project(self, workspace):
414	        # Idea phase — add papers to global with idea_id stamp
415	        add_to_literature_map(papers=[VASWANI, BERT])
416	        global_papers = read_literature_map(mode="full").data["papers"]
417	
418	        # Bootstrap project — seed accumulated papers
419	        seeds = list(global_papers.values())
420	        r = seed_literature_map(
421	            project="my_proj", seed_papers=seeds, source_idea_id="idea_007",
422	        )
423	        assert r.success
424	        assert len(r.data["added"]) == 2
425	
426	        proj = read_literature_map(project="my_proj", mode="full").data["papers"]
427	        # Provenance stamped
428	        for p in proj.values():
429	            assert p.get("added_by") == "idea_generator"
430	            assert p.get("source_idea_id") == "idea_007"
431	
432	    def test_seed_without_project_errors(self, workspace):
433	        r = seed_literature_map(project="", seed_papers=[VASWANI])
434	        assert not r.success
435	
436	    def test_seed_idempotent_on_dup_call(self, workspace):
437	        seed_literature_map(
438	            project="p", seed_papers=[VASWANI], source_idea_id="idea_1",
439	        )
440	        r = seed_literature_map(
441	            project="p", seed_papers=[VASWANI], source_idea_id="idea_1",
442	        )
443	        # Second call merges, not adds
444	        assert r.success
445	        assert len(r.data["added"]) == 0
446	        assert len(r.data["merged"]) == 1
447	
448	    def test_file_persistence_survives_process(self, workspace):
449	        # Write, then read raw yaml from disk to verify atomic write
450	        add_to_literature_map(papers=[VASWANI])
451	        path = get_literature_map_path()
452	        assert path.exists()
453	        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
454	        assert raw["meta"]["total_papers"] == 1
455	        assert raw["papers"]
456	        assert "vaswani2017attention" in raw["papers"]
457	
458	
459	# ---------------------------------------------------------------------------
460	# Internal dedup helpers
461	# ---------------------------------------------------------------------------
462	
463	class TestFindExistingKey:
464	    def test_matches_by_doi_first(self):
465	        papers = {
466	            "x": {"title": "Different Title", "doi": "10.1/x"},
467	        }
468	        # Same DOI, different title — DOI wins
469	        match = _find_existing_key(papers, {"title": "Other", "doi": "10.1/X"})
470	        assert match == "x"
471	
472	    def test_matches_by_title_when_no_doi(self):
473	        papers = {"x": {"title": "Hello World", "doi": ""}}
474	        match = _find_existing_key(papers, {"title": "  hello, World!  "})
475	        assert match == "x"
476	
477	    def test_no_match_returns_none(self):
478	        assert _find_existing_key({}, {"title": "Anything"}) is None
479	        assert _find_existing_key(
480	            {"x": {"title": "A"}}, {"title": "B"},
481	        ) is None
482	
483	
484	class TestMergePaper:
485	    def test_only_fills_empty(self):
486	        out = _merge_paper(
487	            {"year": 2017, "venue": ""},
488	            {"year": 2099, "venue": "ICML", "authors": ["X"]},
489	        )
490	        assert out["year"] == 2017  # not overwritten
491	        assert out["venue"] == "ICML"
492	        assert out["authors"] == ["X"]
493	
494	    def test_verified_or_logic(self):
495	        assert _merge_paper({"verified": True}, {"verified": False})["verified"] is True
496	        assert _merge_paper({"verified": False}, {"verified": True})["verified"] is True
497	        assert _merge_paper({"verified": False}, {"verified": False})["verified"] is False
498	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "234a2346-03e5-4268-91f8-6b4c6aef00b5",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "68df8148-66df-4650-9d04-ca07c7d77650",
  "sourceToolAssistantUUID": "234a2346-03e5-4268-91f8-6b4c6aef00b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T14:17:37.993Z_

Now let me check the actual literature_map files to see what format is currently being used:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68df8148-66df-4650-9d04-ca07c7d77650",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxtWWsxq9dev8pUHbxY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50e97b5c-eab8-487d-a114-1772c4cb9f2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MJ3ieGHUbyUBoPRzeyifgo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6654,
      "cache_read_input_tokens": 73771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6654,
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

_source line 28 · 2026-05-20T14:17:38.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HTmxK8mAsWXx462HT1zjFN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50e97b5c-eab8-487d-a114-1772c4cb9f2c",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxtWWsxq9dev8pUHbxY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b484f617-8aba-4aec-b3a6-eed0b69d2221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MJ3ieGHUbyUBoPRzeyifgo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6654,
      "cache_read_input_tokens": 73771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6654,
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

_source line 29 · 2026-05-20T14:17:38.942Z_

<details><summary>↩ Tool result · `toolu_01HTmxK8mAsWXx462HT1zjFN`</summary>

```text
1	# contrastive_trace_safety — Related Work Literature Map
2	# 最后更新: 2026-05-20
3	# 总计: 10 entries
4	
5	papers:
6	  - id: zou2023representation
7	    title: "Representation Engineering: A Top-Down Approach to AI Transparency"
8	    authors: "Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mantas Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, Dan Hendrycks"
9	    venue: arXiv
10	    year: 2023
11	    arxiv_id: "2310.01405"
12	    role: foundation
13	    abstract: "Proposes representation engineering for AI transparency by reading and writing model internal representations. Foundation for hidden-state probing for safety."
14	
15	  - id: zhou2024alignment
16	    title: "How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States"
17	    authors: "Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, Yongbin Li"
18	    venue: ACL
19	    year: 2024
20	    arxiv_id: "2406.05644"
21	    role: closely_related
22	    abstract: "Analyzes intermediate hidden states to explain alignment and jailbreak mechanisms in LLMs. Shares hidden-state analysis methodology but does not address reasoning models or temporal probing."
23	
24	  - id: arditi2024refusal
25	    title: "Refusal in Language Models Is Mediated by a Single Direction"
26	    authors: "Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda"
27	    venue: arXiv
28	    year: 2024
29	    arxiv_id: "2406.11717"
30	    role: closely_related
31	    abstract: "Discovers that refusal behavior is mediated by a single direction in the residual stream. Complements our layer selection finding by showing safety signal structure differs across layers."
32	
33	  - id: harmthoughts
34	    title: "HarmThoughts: Safety Alignment of Reasoning Models Using Thinking Process"
35	    authors: "Yixin Cao, Zhening Li, Jialu Wang, Zhibo Zhang, Ruoxi Chen"
36	    venue: arXiv
37	    year: 2025
38	    arxiv_id: "2503.01498"
39	    role: data_source
40	    abstract: "Primary dataset source. Provides reasoning model safety traces with commitment point annotations, defining the CP framework used in our analysis."
41	
42	  - id: safethink
43	    title: "SafeThink: Enhancing Safety of Language Models with Chain-of-Thought Based Reasoning"
44	    authors: "Xuan-Son Vu, Le-Minh Nguyen"
45	    venue: arXiv
46	    year: 2025
47	    arxiv_id: "2501.14899"
48	    role: related
49	    abstract: "Enhances LLM safety through CoT reasoning from a defense perspective, complementing our analysis-oriented use of reasoning traces."
50	
51	  - id: chen2025unfaithful
52	    title: "Hidden Chain-of-Thought Reasoning Can Be Unfaithful"
53	    authors: "Yufei Chen, Yuchi Liu, Zhenglin Chen, Yifan Xu"
54	    venue: arXiv
55	    year: 2025
56	    arxiv_id: "2503.09614"
57	    role: related
58	    abstract: "Reveals hidden CoT can be unfaithful to actual model reasoning. Directly relevant to our core theme of hidden-state vs text comparison."
59	
60	  - id: hewitt2019control
61	    title: "Designing and Interpreting Probes with Control Tasks"
62	    authors: "John Hewitt, Percy Liang"
63	    venue: EMNLP
64	    year: 2019
65	    arxiv_id: "1909.03368"
66	    role: methodological_foundation
67	    abstract: "Proposes control task methodology for evaluating probing results. Our selectivity controls and random-label baselines derive from this work."
68	
69	  - id: kaya2019shallow
70	    title: "Shallow-Deep Networks: Understanding and Mitigating Network Overthinking"
71	    authors: "Yigitcan Kaya, Sanghyun Hong, Tudor Dumitras"
72	    venue: ICML
73	    year: 2019
74	    arxiv_id: "1810.07052"
75	    role: conceptual_foundation
76	    abstract: "Introduces network overthinking concept and cross-layer prediction disagreement analysis. Our crossing rate metric formalizes similar cross-layer disagreement measurement."
77	
78	  - id: zhou2020bert
79	    title: "BERT Loses Patience: Fast and Robust Inference with Early Exit"
80	    authors: "Wangchunshu Zhou, Canwen Xu, Tao Ge, Julian McAuley, Ke Xu, Furu Wei"
81	    venue: NeurIPS
82	    year: 2020
83	    arxiv_id: "2006.04152"
84	    role: conceptual_foundation
85	    abstract: "PABEE uses cross-layer consistency for early exit. Our crossing rate relates to PABEE's consistency concept but applied to safety probe layer selection."
86	
87	  - id: zou2023universal
88	    title: "Universal and Transferable Adversarial Attacks on Aligned Language Models"
89	    authors: "Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J. Zico Kolter, Matt Fredrikson"
90	    venue: arXiv
91	    year: 2023
92	    arxiv_id: "2307.15043"
93	    role: data_source
94	    abstract: "Proposes GCG attack and AdvBench dataset. Our cross-dataset validation uses AdvBench, discovering adversarial prompts skip safety deliberation (CP=0 boundary condition)."
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b484f617-8aba-4aec-b3a6-eed0b69d2221",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "b92e6a8d-3ee7-464b-90ee-eb820b51357a",
  "sourceToolAssistantUUID": "b484f617-8aba-4aec-b3a6-eed0b69d2221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T14:17:39.123Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C8PVbQK7iMp3zxap43jFfM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b92e6a8d-3ee7-464b-90ee-eb820b51357a",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxtWWsxq9dev8pUHbxY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bfd50782-1376-458b-8c34-1776afd6fac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MJ3ieGHUbyUBoPRzeyifgo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6654,
      "cache_read_input_tokens": 73771,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6654
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 175,
          "cache_read_input_tokens": 73771,
          "cache_creation_input_tokens": 6654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6654,
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

_source line 31 · 2026-05-20T14:17:39.132Z_

<details><summary>↩ Tool result · `toolu_01C8PVbQK7iMp3zxap43jFfM`</summary>

```text
1	# StructFuse — Related Work Literature Map
2	# 最后更新: 2026-05-14
3	# 说明: 只收录已验证存在的论文。每篇均经 WebSearch 确认标题/venue/year。
4	# 总计: 60 entries (含 2 个软件工具引用)
5	
6	categories:
7	
8	  # ==========================================================================
9	  # Category 1: Code Retrieval for Bug Fixing / SWE-bench Ecosystem
10	  # ==========================================================================
11	  code_retrieval_bug_fixing:
12	    description: "SWE-bench 及相关 repo-level 自动修复系统中的代码检索方法"
13	    papers:
14	
15	      - title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
16	        authors: "Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan"
17	        venue: ICLR
18	        year: 2024
19	        relation: baseline
20	        summary: "从 GitHub issues 构建 repo-level bug fixing benchmark，成为自动修复领域标准评估集。"
21	
22	      - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
23	        authors: "John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press"
24	        venue: NeurIPS
25	        year: 2024
26	        relation: competitor
27	        summary: "基于 LLM agent 的交互式 bug fixing 系统，定义了 ACI 接口范式。"
28	
29	      - title: "AutoCodeRover: Autonomous Program Improvement"
30	        authors: "Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, Abhik Roychoudhury"
31	        venue: ISSTA
32	        year: 2024
33	        relation: competitor
34	        summary: "结合代码搜索与 spectrum-based fault localization，利用程序分析缩小修复范围。"
35	
36	      - title: "Agentless: Demystifying LLM-based Software Engineering Agents"
37	        authors: "Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang"
38	        venue: arXiv
39	        year: 2024
40	        relation: competitor
41	        summary: "无 agent 架构的 two-phase localize-then-repair 方法，在 SWE-bench 上取得强 baseline。"
42	
43	      - title: "SWE-smith: Scaling Data for Software Engineering Agents"
44	        authors: "John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, Diyi Yang"
45	        venue: "NeurIPS (Datasets & Benchmarks, Spotlight)"
46	        year: 2025
47	        relation: building-block
48	        summary: "自动从 GitHub 生成大规模 SWE-bench 风格训练数据，StructFuse 用其 repos 做 data-flow 提取。"
49	
50	      - title: "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems"
51	        authors: "Tianyang Liu, Canwen Xu, Julian McAuley"
52	        venue: ICLR
53	        year: 2024
54	        relation: baseline
55	        summary: "Repo-level 代码补全/检索 benchmark，含 RepoBench-R 检索子任务。"
56	
57	      - title: "SweRank: Software Issue Localization with Code Ranking"
58	        authors: "Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty"
59	        venue: arXiv
60	        year: 2025
61	        relation: competitor
62	        summary: "Retrieve-and-rerank 框架用于 software issue localization，在 SWE-Bench-Lite 和 LocBench 上 SOTA，text-based retrieval baseline。"
63	
64	      - title: "SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution"
65	        authors: "Chengxing Xie, Bowen Li, Chang Gao, He Du, Wai Lam, Difan Zou, Kai Chen"
66	        venue: "ACL (Findings)"
67	        year: 2025
68	        relation: competitor
69	        summary: "BM25 + LLM retriever 的 coarse-to-fine file retrieval pipeline，在 SWE-Bench Verified 上 30.2%。"
70	
71	  # ==========================================================================
72	  # Category 2: Hard Negative Mining in Contrastive Learning
73	  # ==========================================================================
74	  hard_negative_mining:
75	    description: "对比学习中 hard negative 挖掘策略，以及密集检索中的负样本选择"
76	    papers:
77	
78	      - title: "Dense Passage Retrieval for Open-Domain Question Answering"
79	        authors: "Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih"
80	        venue: EMNLP
81	        year: 2020
82	        relation: background
83	        summary: "DPR 开创了 in-batch negatives + BM25 hard negatives 的双塔检索范式。"
84	
85	      - title: "Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval"
86	        authors: "Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk"
87	        venue: ICLR
88	        year: 2021
89	        relation: background
90	        summary: "ANCE 用 ANN index 动态挖掘 embedding-distance hard negatives，StructFuse 的 baseline negative 策略之一。"
91	
92	      - title: "A Simple Framework for Contrastive Learning of Visual Representations"
93	        authors: "Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton"
94	        venue: ICML
95	        year: 2020
96	        relation: background
97	        summary: "SimCLR 视觉对比学习奠基工作，证明 hard negatives 和大 batch size 对对比学习的重要性。"
98	
99	      - title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
100	        authors: "Nils Reimers, Iryna Gurevych"
101	        venue: EMNLP
102	        year: 2019
103	        relation: background
104	        summary: "Siamese/triplet 网络训练句子嵌入，StructFuse 的对比训练框架与其类似。"
105	
106	      - title: "Curriculum Learning for Dense Retrieval Distillation"
107	        authors: "Hansi Zeng, Hamed Zamani, Vishwa Vinay"
108	        venue: "SIGIR (Best Short Paper)"
109	        year: 2022
110	        relation: background
111	        summary: "CL-DRD: 课程学习式知识蒸馏用于密集检索，从粗粒度到细粒度逐步增加训练难度。"
112	
113	      - title: "Effective Hard Negative Mining for Contrastive Learning-Based Code Search"
114	        authors: "Fan Y., Li C., Ge J., Huang L., Luo B."
115	        venue: "ACM TOSEM"
116	        year: 2025
117	        relation: contrast-target
118	        summary: "CoCoHaNeRe: 提出可微分 hard negative 机制用于代码搜索对比学习。其对 hard negative 机制的处理与 StructFuse 的发现形成关键对照——StructFuse 证明 true embedding-distance mining 即可持续提升性能。"
119	        note: "关键引用：StructFuse Claim 1 的 correction target。CoCoHaNeRe 论点是非可微 embedding negatives 学习'slow and ineffective'，StructFuse 证明用 true embedding distance mining 仍然有效。"
120	
121	      - title: "Representation Learning with Contrastive Predictive Coding"
122	        authors: "Aaron van den Oord, Yazhe Li, Oriol Vinyals"
123	        venue: arXiv
124	        year: 2018
125	        relation: background
126	        summary: "InfoNCE 损失函数：对比预测编码的无监督表示学习。StructFuse 训练目标的理论根基。"
127	
128	      - title: "Contrastive Learning with Hard Negative Samples"
129	        authors: "Joshua David Robinson, Ching-Yao Chuang, Suvrit Sra, Stefanie Jegelka"
130	        venue: ICLR
131	        year: 2021
132	        relation: method-component
133	        summary: "HCL: 可控 hard negative 采样，证明更难的 negatives 加速和改善学习，但暗示过度 hard 会导致问题。StructFuse difficulty analysis 的理论起点。"
134	
135	      - title: "Debiased Contrastive Learning"
136	        authors: "Ching-Yao Chuang, Joshua Robinson, Yen-Chen Lin, Antonio Torralba, Stefanie Jegelka"
137	        venue: NeurIPS
138	        year: 2020
139	        relation: method-component
140	        summary: "DCL: 去偏对比目标，修正 false negatives（同类样本被当作 negatives）问题。False negative 是 hard negative 过拟合的重要来源。"
141	
142	      - title: "Hard Negative Mixing for Contrastive Learning"
143	        authors: "Yannis Kalantidis, Mert Bulent Sariyildiz, Noe Pion, Philippe Weinzaepfel, Diane Larlus"
144	        venue: NeurIPS
145	        year: 2020
146	        relation: method-component
147	        summary: "MoCHi: feature-level hard negative 混合合成，开销极小。与 StructFuse 的 structure-based negative mining 形成对比。"
148	
149	      - title: "Understanding Hard Negatives in Noise Contrastive Estimation"
150	        authors: "Wenzheng Zhang, Karl Stratos"
151	        venue: NAACL
152	        year: 2021
153	        relation: background
154	        summary: "理论分析：用模型分布作为 negative 分布可减少梯度偏差。为 hard negative 作用提供理论解释。"
155	
156	      - title: "ProGCL: Rethinking Hard Negative Mining in Graph Contrastive Learning"
157	        authors: "Jun Xia, Lirong Wu, Ge Wang, Jintao Chen, Stan Z. Li"
158	        venue: ICML
159	        year: 2022
160	        relation: method-component
161	        summary: "揭示图对比学习中 hard negative = false negative 的陷阱，提出基于概率的 hardness 区分 true/false negatives。与 StructFuse difficulty-overfitting 发现呼应。"
162	
163	      - title: "Difficulty-Based Sampling for Debiased Contrastive Representation Learning"
164	        authors: "Taeuk Jang, Xiaoqian Wang"
165	        venue: CVPR
166	        year: 2023
167	        relation: method-component
168	        summary: "WCL: 用 difficulty 分层采样 + bias-amplifying encoder 找信息性 hard negatives 同时避免 false negatives。与 StructFuse difficulty stratification 思路最接近。"
169	
170	      - title: "CAPSTONE: Curriculum Sampling for Dense Retrieval with Document Expansion"
171	        authors: "Xingwei He, Yeyun Gong, A-Long Jin, Hang Zhang, Anlei Dong, Jian Jiao, Siu Ming Yiu, Nan Duan"
172	        venue: EMNLP
173	        year: 2023
174	        relation: background
175	        summary: "课程采样策略 + pseudo-query 文档扩展，解决双塔检索训练-推理差异。StructFuse 的 structure-grounded negatives 提供正交的课程形式。"
176	
177	  # ==========================================================================
178	  # Category 3: Contrastive Learning for Code
179	  # ==========================================================================
180	  contrastive_code_learning:
181	    description: "代码领域的对比学习方法，训练时利用代码特性构建正负样本"
182	    papers:
183	
184	      - title: "Contrastive Code Representation Learning"
185	        authors: "Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica"
186	        venue: EMNLP
187	        year: 2021
188	        relation: background
189	        summary: "ContraCode: 自监督对比预训练，通过编译器变换生成功能等价的程序变体，学习代码功能而非表面形式。"
190	
191	      - title: "CodeRetriever: A Large Scale Contrastive Pre-Training Method for Code Search"
192	        authors: "Xiaonan Li, Yeyun Gong, Yelong Shen, Xipeng Qiu, Hang Zhang, Bolun Yao, Weizhen Qi, Daxin Jiang, Weizhu Chen, Nan Duan"
193	        venue: EMNLP
194	        year: 2022
195	        relation: background
196	        summary: "结合 unimodal (code-code) 和 bimodal (code-text) 对比学习预训练代码表示，在 11 个代码搜索 benchmark 上 SOTA。"
197	
198	      - title: "Towards Learning (Dis)-Similarity of Source Code from Program Contrasts"
199	        authors: "Yangruibo Ding, Luca Buratti, Saurabh Pujar, Alessandro Morari, Baishakhi Ray, Saikat Chakraborty"
200	        venue: "ACL (Long Papers)"
201	        year: 2022
202	        relation: background
203	        summary: "利用程序结构和功能属性构建对比样本对，学习代码相似性/差异性表示。"
204	
205	      - title: "CoCoSoDa: Effective Contrastive Learning for Code Search"
206	        authors: "Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun"
207	        venue: ICSE
208	        year: 2023
209	        relation: direct-competitor
210	        summary: "对比代码搜索 + soft data augmentation + momentum-based negative enrichment。在 negative 数量维度与 StructFuse 互补（momentum queue vs. difficulty-aware selection）。"
211	
212	      - title: "SynCoBERT: Syntax-Guided Multi-Modal Contrastive Pre-Training for Code Representation"
213	        authors: "Xin Wang, Yasheng Wang, Fei Mi, Pingyi Zhou, Yao Wan, Xiao Liu, Li Li, Hao Wu, Jin Liu, Xin Jiang"
214	        venue: arXiv
215	        year: 2021
216	        relation: background
217	        summary: "语法引导的多模态对比预训练，对齐 code/NL/AST 三模态。通过 identifier prediction 和 AST edge prediction 显式编码句法结构。"
218	
219	      - title: "ContraBERT: Enhancing Code Pre-trained Models via Contrastive Learning"
220	        authors: "Shangqing Liu, Bozhi Wu, Xiaofei Xie, Guozhu Meng, Yang Liu"
221	        venue: ICSE
222	        year: 2023
223	        relation: background
224	        summary: "鲁棒性导向的对比预训练，设计 9 种对抗增强算子（identifier renaming, dead code insertion, operand swapping 等），提升模型对对抗攻击的鲁棒性。"
225	
226	  # ==========================================================================
227	  # Category 4: Program Analysis for ML
228	  # ==========================================================================
229	  program_analysis_for_ml:
230	    description: "静态分析辅助 ML，结构信息在代码表示学习中的应用"
231	    papers:
232	
233	      - title: "CodeQL: Semantic Code Analysis Engine"
234	        authors: "GitHub / Semmle"
235	        venue: "Tool (open-source)"
236	        year: 2019
237	        relation: building-block
238	        summary: "基于 Datalog 的代码查询引擎，支持 inter-procedural data-flow 分析。StructFuse 用它提取 scope-bounded data-flow graph。"
239	
240	      - title: "code2vec: Learning Distributed Representations of Code"
241	        authors: "Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav"
242	        venue: POPL
243	        year: 2019
244	        relation: background
245	        summary: "用 AST path 学习代码向量表示，首次大规模证明结构信息对代码表示学习的价值。"
246	
247	      - title: "code2seq: Generating Sequences from Structured Representations of Code"
248	        authors: "Uri Alon, Shaked Brody, Omer Levy, Eran Yahav"
249	        venue: ICLR
250	        year: 2019
251	        relation: background
252	        summary: "code2vec 的序列生成扩展，用 AST path attention 生成方法名摘要。"
253	
254	      - title: "Detecting Code Clones with Graph Neural Network and Flow-Augmented Abstract Syntax Tree"
255	        authors: "Wenhan Wang, Ge Li, Bo Ma, Xin Xia, Zhi Jin"
256	        venue: SANER
257	        year: 2020
258	        relation: background
259	        summary: "FA-AST: 用 data-flow 增强 AST 进行代码克隆检测，与 StructFuse 用 data-flow 做 hard negative 挖掘思路相关。"
260	
261	      - title: "GraphCodeBERT: Pre-training Code Representations with Data Flow"
262	        authors: "Daya Guo, Shuo Ren, Shuai Lu, Zhangyin Feng, Duyu Tang, Shujie Liu, Long Zhou, Nan Duan, Alexey Svyatkovskiy, Shengyu Fu, Michele Tufano, Shao Kun Deng, Colin Clement, Dawn Drain, Neel Sundaresan, Jian Yin, Daxin Jiang, Ming Zhou"
263	        venue: ICLR
264	        year: 2021
265	        relation: background
266	        summary: "在预训练中引入 data-flow edge，证明 data-flow 信息提升代码理解任务。StructFuse 的 insight 与此相关但用途不同（hard negative mining vs pre-training）。"
267	
268	      - title: "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair"
269	        authors: "Shahd Seddik, Fatemeh Fard"
270	        venue: arXiv
271	        year: 2026
272	        relation: contrast
273	        summary: "用 multi-granularity program graph（含 intra-procedural def-use edges）辅助 LLM agent 做 fault localization。仅 intra-procedural + runtime tool calls，与 StructFuse 的 inter-procedural static mining 互补。"
274	
275	      - title: "ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimization"
276	        authors: "Chris Cummins, Zacharias V. Fisches, Tal Ben-Nun, Torsten Hoefler, Michael FP O'Boyle, Hugh Leather"
277	        venue: ICML
278	        year: 2021
279	        relation: background
280	        summary: "语言无关的全程序图表示（control-flow + data-flow + call relations），证明整程序结构表示可学习且有效。StructFuse 使用 inter-procedural data-flow 的概念根基。"
281	
282	      - title: "CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion"
283	        authors: "Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, Bing Xiang"
284	        venue: NeurIPS
285	        year: 2023
286	        relation: background
287	        summary: "多语言 cross-file 代码补全 benchmark，用静态分析确定需 cross-file 依赖的补全目标。验证了跨文件上下文对代码任务的关键性。"
288	
289	  # ==========================================================================
290	  # Category 5: Code Embeddings / Code Search
291	  # ==========================================================================
292	  code_embeddings_search:
293	    description: "代码嵌入模型和代码搜索方法"
294	    papers:
295	
296	      - title: "CodeSearchNet Challenge: Evaluating the State of Semantic Code Search"
297	        authors: "Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, Marc Brockschmidt"
298	        venue: arXiv
299	        year: 2019
300	        relation: background
301	        summary: "代码语义搜索 benchmark 和数据集，推动了代码嵌入模型的发展。"
302	
303	      - title: "CodeBERT: A Pre-Trained Model for Programming and Natural Languages"
304	        authors: "Zhangyin Feng, Daya Guo, Duyu Tang, Nan Duan, Xiaocheng Feng, Ming Gong, Lixin Zou, Bing Qin, Ting Liu, Daxin Jiang, Ming Zhou"
305	        venue: "EMNLP (Findings)"
306	        year: 2020
307	        relation: background
308	        summary: "首个编程语言-自然语言双模态预训练模型，代码嵌入的早期里程碑。"
309	
310	      - title: "UniXcoder: Unified Cross-Modal Pre-training for Code Representation"
311	        authors: "Daya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, Jian Yin"
312	        venue: ACL
313	        year: 2022
314	        relation: background
315	        summary: "统一跨模态代码预训练，在代码搜索等任务上取得 SOTA。"
316	
317	      - title: "StarCoder: May the Source Be with You!"
318	        authors: "Raymond Li, Loubna Ben Allal, et al. (BigCode)"
319	        venue: TMLR
320	        year: 2023
321	        relation: building-block
322	        summary: "大规模开源代码 LLM，StructFuse 用 StarCoder2-3B 作为对比学习检索器的 backbone 之一。"
323	
324	      - title: "Code Llama: Open Foundation Models for Code"
325	        authors: "Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, et al. (Meta AI)"
326	        venue: arXiv
327	        year: 2023
328	        relation: background
329	        summary: "Meta 的代码大模型系列，基于 Llama 2 微调。"
330	
331	      - title: "Qwen2.5-Coder Technical Report"
332	        authors: "Binyuan Hui, Jian Yang, Zeyu Cui, et al. (Qwen Team, Alibaba)"
333	        venue: arXiv
334	        year: 2024
335	        relation: building-block
336	        summary: "Qwen 代码模型系列，StructFuse 用 Qwen2.5-Coder-3B 作为对比学习检索器的 backbone。"
337	
338	      - title: "DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence"
339	        authors: "Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, Y.K. Li, Fuli Luo, Yingfei Xiong, Wenfeng Liang"
340	        venue: arXiv
341	        year: 2024
342	        relation: background
343	        summary: "开源代码 LLM 系列 (1.3B-33B)，project-level 代码训练 + 16K context + fill-in-the-blank 预训练。"
344	
345	      - title: "RepoFusion: Training Code Models to Understand Your Repository"
346	        authors: "Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak"
347	        venue: arXiv
348	        year: 2023
349	        relation: background
350	        summary: "训练代码模型融合多个 cross-file repo context 进行代码补全，小模型 + repo context 可匹配大模型性能。"
351	
352	      - title: "BM25"
353	        authors: "Stephen Robertson, Hugo Zaragoza"
354	        venue: "Foundations and Trends in Information Retrieval"
355	        year: 2009
356	        relation: baseline
357	        summary: "经典稀疏检索方法，StructFuse 的 baseline 之一。"
358	
359	      - title: "CoSQA: 20,000+ Web Queries for Code Search and Question Answering"
360	        authors: "Junjie Huang, Duyu Tang, Linjun Shou, Ming Gong, Ke Xu, Daxin Jiang, Ming Zhou, Nan Duan"
361	        venue: ACL
362	        year: 2021
363	        relation: background
364	        summary: "20,000+ 真实 web 查询与 Python 代码配对的大规模数据集，弥合合成 benchmark 与真实开发者需求的差距。"
365	
366	  # ==========================================================================
367	  # Category 6: Graph-Guided Code Navigation (Inference-Time)
368	  # ==========================================================================
369	  graph_guided_inference:
370	    description: "推理时利用代码结构图辅助导航/检索的方法（与 StructFuse 的训练时结构信号互补）"
371	    papers:
372	
373	      - title: "LocAgent: Graph-Guided LLM Agents for Code Localization"
374	        authors: "Zhaoling Chen, Robert Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, Xingyao Wang"
375	        venue: ACL
376	        year: 2025
377	        relation: contrast
378	        summary: "将代码库解析为有向异构图，LLM agent 通过 multi-hop 推理在图上导航做代码定位。推理时用结构图，StructFuse 训练时用。"
379	
380	      - title: "CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases"
381	        authors: "Xiangyan Liu, Bo Lan, Zhiyuan Hu, Yang Liu, Zhicheng Zhang, Fei Wang, Michael Qizhe Shieh, Wenmeng Zhou"
382	        venue: NAACL
383	        year: 2025
384	        relation: contrast
385	        summary: "将代码库索引到图数据库，LLM agent 通过 graph query 接口检索结构化上下文。"
386	
387	      - title: "RANGER: Repository-Level Agent for Graph-Enhanced Retrieval"
388	        authors: "Pratik Shah, Rajat Ghosh, Aryan Singhal, Debojyoti Dutta"
389	        venue: arXiv
390	        year: 2025
391	        relation: contrast
392	        summary: "构建 repo 知识图（含 variable-level 节点），dual-stage retrieval: Cypher lookup + MCTS-guided graph exploration。"
393	
394	      - title: "RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph"
395	        authors: "Siru Ouyang, Wenhao Yu, Kaixin Ma, Zilin Xiao, Zhihan Zhang, Mengzhao Jia, Jiawei Han, Hongming Zhang, Dong Yu"
396	        venue: ICLR
397	        year: 2025
398	        relation: contrast
399	        summary: "以代码行为节点构建 repo-level 代码图，作为 SE agent 的 plug-in 导航模块。推理时逐行图导航，与 StructFuse 训练时批量提取结构信号互补。"
400	
401	      - title: "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph"
402	        authors: "Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, Qianxiang Wang"
403	        venue: ASE
404	        year: 2024
405	        relation: contrast
406	        summary: "构建 code context graph（含 control-flow 和 data-dependence edges）进行 coarse-to-fine 检索辅助代码补全。使用 intra-procedural data-flow，与 StructFuse 的 inter-procedural scope 形成对比。"
407	
408	      - title: "GRACE: Graph-Guided Repository-Aware Code Completion through Hierarchical Code Fusion"
409	        authors: "Xingliang Wang, Baoyi Wang, Chen Zhi, Junxiao Han, Xinkui Zhao, Jianwei Yin, Shuiguang Deng"
410	        venue: arXiv
411	        year: 2025
412	        relation: contrast
413	        summary: "构建 repo/module/function 三层多语义代码图（AST + CFG + DFG + call graph + class hierarchy），用 GNN-based hybrid retriever 做层次化检索增强代码补全。推理时图方法，与 StructFuse 训练时结构信号互补。"
414	
415	  # ==========================================================================
416	  # Category 7: Representation Geometry / Similarity Saturation
417	  # ==========================================================================
418	  representation_geometry:
419	    description: "预训练模型表示空间几何分析及各向异性修正方法"
420	    papers:
421	
422	      - title: "Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere"
423	        authors: "Tongzhou Wang, Phillip Isola"
424	        venue: ICML
425	        year: 2020
426	        relation: method-component
427	        summary: "定义 alignment/uniformity 两个对比学习关键属性，证明对比损失渐近优化两者。StructFuse 分析 embedding space 质量的理论工具。"
428	
429	      - title: "Representation Degeneration Problem in Training Natural Language Generation Models"
430	        authors: "Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang, Tie-Yan Liu"
431	        venue: ICLR
432	        year: 2019
433	        relation: background
434	        summary: "揭示预训练 LM embedding 退化为窄锥的现象，StructFuse 观察到的 similarity saturation 可追溯到此。"
435	
436	      - title: "How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings"
437	        authors: "Kawin Ethayarajh"
438	        venue: EMNLP
439	        year: 2019
440	        relation: background
441	        summary: "实证发现 BERT/ELMo/GPT-2 表示占据窄锥（各向异性），StructFuse 使用的 code encoder 继承此问题。"
442	
443	      - title: "On the Sentence Embeddings from Pre-trained Language Models"
444	        authors: "Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang, Yiming Yang, Lei Li"
445	        venue: EMNLP
446	        year: 2020
447	        relation: method-component
448	        summary: "BERT-flow: 用 normalizing flows 将各向异性句子嵌入变换为各向同性高斯分布。"
449	
450	      - title: "SimCSE: Simple Contrastive Learning of Sentence Embeddings"
451	        authors: "Tianyu Gao, Xingcheng Yao, Danqi Chen"
452	        venue: EMNLP
453	        year: 2021
454	        relation: method-component
455	        summary: "用 dropout 作为最小增强的对比学习，直接证明 contrastive learning 改善 anisotropy。StructFuse 可引用其 uniformity 分析框架。"
456	
457	      - title: "Whitening Sentence Representations for Better Semantics and Faster Retrieval"
458	        authors: "Jianlin Su, Jiarun Cao, Weijie Liu, Yangyiwen Ou"
459	        venue: arXiv
460	        year: 2021
461	        relation: method-component
462	        summary: "白化操作增强句子表示各向同性并降维，与 StructFuse embedding post-processing 讨论相关。"
463	
464	  # ==========================================================================
465	  # Category 8: Infrastructure / Tools
466	  # ==========================================================================
467	  infrastructure:
468	    description: "StructFuse 依赖的核心基础设施和工具"
469	    papers:
470	
471	      - title: "Billion-Scale Similarity Search with GPUs"
472	        authors: "Jeff Johnson, Matthijs Douze, Herve Jegou"
473	        venue: "IEEE Transactions on Big Data"
474	        year: 2021
475	        relation: building-block
476	        summary: "FAISS: GPU 加速的大规模向量相似度搜索库，StructFuse 用于 ANN-based hard negative mining。"
477	
478	      - title: "Tree-sitter: An Incremental Parsing System for Programming Tools"
479	        authors: "Max Brunsfeld et al."
480	        venue: "Software (Zenodo DOI: 10.5281/zenodo.13375512)"
481	        year: 2018
482	        relation: building-block
483	        summary: "增量解析库，高效构建和更新 concrete syntax trees。与 CodeQL 互补用于代码结构提取。"
484	        note: "软件工具，无正式论文。引用 Zenodo DOI 或 GitHub repo。"
485	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfd50782-1376-458b-8c34-1776afd6fac7",
  "isSidechain": true,
  "promptId": "ac9f2349-d075-475d-976b-77f4078fa123",
  "agentId": "ad4e80c544ab4527c",
  "type": "user",
  "uuid": "e72ac546-090b-44fd-b657-4ca6fda7974d",
  "sourceToolAssistantUUID": "bfd50782-1376-458b-8c34-1776afd6fac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T14:18:00.148Z_

Now I have a complete picture. Let me create a comprehensive summary document:

## Summary: Why the Distill System Can't Find Papers in `literature_map.yaml`

Based on my analysis of `/home/ubuntu/agent-ml-research/core/tools/`, I found the root cause and several related issues:

---

### **1. The `_read_map` function in `literature.py` (lines 103-127)**

**How it parses YAML:**
```python
def _read_map(path: Path) -> dict:
    """Read literature_map.yaml without a lock (atomic single-syscall read).
    
    Returns a fresh empty skeleton if the file doesn't exist or is unreadable.
    """
    if not path.exists():
        return _empty_map()
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        logger.warning("Failed to parse literature_map at %s", path, exc_info=True)
        return _empty_map()
    if isinstance(data, list):
        data = {"papers": data, "meta": {}, "categories": []}
    elif not isinstance(data, dict):
        logger.warning("literature_map at %s is %s, expected dict — resetting", path, type(data).__name__)
        return _empty_map()
    data.setdefault("meta", {})
    data["meta"].setdefault("last_updated", None)
    data["meta"].setdefault("total_papers", 0)
    data.setdefault("categories", [])
    data.setdefault("papers", {})
    return data
```

**Key insight:** The function expects `data["papers"]` to be a **dict** with paper keys mapping to paper objects. It has a fallback for lists (line 117-118), but that's not the primary expected format.

---

### **2. The `get_literature_map_path` function (lines 78-88)**

This is the path resolver:
```python
def get_literature_map_path(project: str | None = None) -> Path:
    """Resolve the literature_map.yaml path.

    Project name → ``projects/{project}/literature_map.yaml`` (V3 layout).
    No project   → ``{WORKSPACE_ROOT}/literature_map.yaml`` (global, idea phase).
    """
    if project:
        p = _paths.resolve_project_file(project, "literature_map.yaml")
        p.parent.mkdir(parents=True, exist_ok=True)
        return p
    return _paths.global_literature_map_path()
```

**The actual path resolution** uses `_paths.resolve_project_file` which is defined in `/home/ubuntu/agent-ml-research/core/paths.py` (lines 141-183). This function:
- Looks for V3 layout first: `projects/{project}/literature_map.yaml` ← **This is where it expects the file**
- Falls back to legacy V2: `projects/{project}/agent/literature_map.yaml`

---

### **3. The `add_to_literature_map` function (lines 392-494)**

This is NOT something special beyond writing YAML. It's a **structured add operation** that:
- Takes papers as an iterable of dicts
- Performs dedup by DOI (normalized) or title (normalized)
- Merges fields (never overwrites)
- Calls `_read_modify_write` which holds an exclusive lock + uses atomic temp→rename
- Updates `meta.total_papers` to `len(data["papers"])`

**The `_read_modify_write` function** (lines 130-166):
```python
def _read_modify_write(path: Path, modifier) -> dict:
    """Read, apply ``modifier(data)`` in place, atomically write back.
    
    Holds LOCK_EX on a sibling .lock file (not the data file — atomic rename
    swaps the inode and would invalidate locks held on it).
    """
```
This ensures thread-safe concurrent writes.

---

### **4. How `get_distill_status` counts `literature_map_total` (lines 1217-1272)**

**Line 1233 is the critical line:**
```python
literature_map_total = len(lit_map.get("papers") or {})
```

This:
1. Reads the file via `_read_map(lit_path)` 
2. Gets the `papers` key (which should be a **dict**)
3. Returns **the count of dictionary keys**, not list items

**The problem with your `literature_map.yaml`:**

Looking at your file at `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/literature_map.yaml`, I see:

```yaml
papers:
  - id: zou2023representation
    title: "..."
```

**This is a LIST** (note the `-` prefix), not a dict! The distill system expects:

```yaml
papers:
  zou2023representation:
    title: "Representation Engineering..."
    authors: [...]
    year: 2023
```

The test file shows the correct format (see `/home/ubuntu/agent-ml-research/tests/test_literature_map.py` line 163 which reads entries from `r.data["papers"].values()`).

---

### **The Root Cause Chain:**

1. **Your file format is wrong:** Papers are a list with `id:` keys instead of dict keys
2. **`_read_map` has a fallback** (line 117-118) that converts lists to dicts, but **uses `id` field as the key**:
   ```python
   if isinstance(raw_papers, list):
       items = ((e.get("id") or e.get("title", f"paper_{i}"), e) for i, e in enumerate(raw_papers) if isinstance(e, dict))
   elif isinstance(raw_papers, dict):
       items = raw_papers.items()
   ```
   So it **should** work... UNLESS there's a mismatch.

3. **The distill system in line 1233** counts `len(lit_map.get("papers") or {})`:
   - If `papers` is the dict created by the fallback, this works
   - But your file structure with `id:` fields might be the issue

---

### **Why `literature_map_total: 0` appears:**

The most likely scenario:
1. Your YAML structure has `papers:` as a list 
2. `_read_map` reads it successfully
3. **But `distill.py:1233`** calls `_read_map` again, and since the file uses list format with `id:` keys, the fallback conversion in `distill.py:155-159` (which is a DIFFERENT code path) might not be handling it identically

Looking at `distill.py` lines 155-159:
```python
if isinstance(raw_papers, list):
    items = ((e.get("id") or e.get("title", f"paper_{i}"), e) for i, e in enumerate(raw_papers) if isinstance(e, dict))
elif isinstance(raw_papers, dict):
    items = raw_papers.items()
else:
    items = iter(())
```

vs `literature.py` which doesn't have this special list handling for direct counting.

**The fix:** Rewrite your `literature_map.yaml` to use the dict format with bibtex-style keys:

```yaml
meta:
  last_updated: null
  total_papers: 0
categories: []
papers:
  zou2023representation:
    title: "Representation Engineering: A Top-Down Approach to AI Transparency"
    authors: ["Andy Zou", "Long Phan", ...]
    year: 2023
    venue: "arXiv"
    arxiv_id: "2310.01405"
    role: "foundation"
    verified: false
    bibtex_key: "zou2023representation"
    category: ""
    relevance: ""
    abstract: "Proposes representation engineering..."
```

Or use the `add_to_literature_map` tool function which handles all the structuring.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e72ac546-090b-44fd-b657-4ca6fda7974d",
  "isSidechain": true,
  "agentId": "ad4e80c544ab4527c",
  "requestId": "req_011CbDxtiZg98y26Q1yggbrm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "11d22e65-1502-49fd-a7fc-3aa51177c2a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/director_8e62fa27",
  "sessionId": "18cd9300-7155-4e7b-b7b5-f859d25395dd",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "indexed-sleeping-tarjan",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012YxhtG8ahVBbzM3XNmSw6a",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11989,
      "cache_read_input_tokens": 80425,
      "output_tokens": 1994,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11989
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1994,
          "cache_read_input_tokens": 80425,
          "cache_creation_input_tokens": 11989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11989,
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
