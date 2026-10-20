# Research conversation: Search the codebase under /home/ubuntu/agent-ml-research/ for how literature_map.yaml is parsed and what format the dist

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a7eceb99bbc693860.jsonl`
- **Structured JSON:** [`e873deb3c430db8db7da.json`](../../sessions/e8/e873deb3c430db8db7da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-20T04:41:36.739Z_

Search the codebase under /home/ubuntu/agent-ml-research/ for how literature_map.yaml is parsed and what format the distill system expects. Specifically:

1. Find any Python code that reads/parses literature_map.yaml (grep for "literature_map" in .py files)
2. Look for an `add_to_literature_map` function or tool definition
3. Find how `distill_papers` or the distill system counts papers from the literature_map
4. Check if there's a specific schema expected (flat list of papers? nested structure?)

Report: the expected YAML structure for literature_map.yaml that the distill system can parse, and whether an `add_to_literature_map` tool/function exists anywhere.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "f729d318-dc7b-4a75-b3b0-cfb0e0ede987",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T04:41:38.594Z_

I'll search the codebase to understand how literature_map.yaml is parsed and what the distill system expects.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f729d318-dc7b-4a75-b3b0-cfb0e0ede987",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCxye24S3FT2WfCJxXH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "369959b8-f2c5-4045-8d5e-b236aeaab3fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YCvPuko3yAx3CDDQzEoqKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33424,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33424,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-20T04:41:38.834Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PmyMHtfWmKJJi6f6vqeFc8`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "369959b8-f2c5-4045-8d5e-b236aeaab3fc",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCxye24S3FT2WfCJxXH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2b9dbf81-f72d-47b3-8985-5fda748735fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YCvPuko3yAx3CDDQzEoqKB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33424,
      "cache_read_input_tokens": 0,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33424
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33424,
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

_source line 4 · 2026-05-20T04:41:38.888Z_

<details><summary>↩ Tool result · `toolu_01PmyMHtfWmKJJi6f6vqeFc8`</summary>

```text
/home/ubuntu/agent-ml-research/scripts/smoke_test.py
/home/ubuntu/agent-ml-research/scripts/mark_pool_sheet_deprecated.py
/home/ubuntu/agent-ml-research/scripts/feishu_chat.py
/home/ubuntu/agent-ml-research/scripts/instance_monitor.py
/home/ubuntu/agent-ml-research/scripts/evaluation/gen_review_html.py
/home/ubuntu/agent-ml-research/scripts/migrate_experiments_to_projects.py
/home/ubuntu/agent-ml-research/scripts/verify_migrations.py
/home/ubuntu/agent-ml-research/scripts/migrate_bot_pool_to_db.py
/home/ubuntu/agent-ml-research/scripts/migrate_pool_sheet_to_db.py
/home/ubuntu/agent-ml-research/scripts/migrate_v2_layout.py
/home/ubuntu/agent-ml-research/scripts/migrate_registry.py
/home/ubuntu/agent-ml-research/scripts/migrate_workspace.py
/home/ubuntu/agent-ml-research/scripts/split_active_workspaces.py
/home/ubuntu/agent-ml-research/scripts/migrate_ideas_to_db.py
/home/ubuntu/agent-ml-research/scripts/resample_split2_neg5.py
/home/ubuntu/agent-ml-research/scripts/simulate_user.py
/home/ubuntu/agent-ml-research/scripts/compare_weight_methods.py
/home/ubuntu/agent-ml-research/.venv/bin/pdf2txt.py
/home/ubuntu/agent-ml-research/.venv/bin/dumppdf.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b9dbf81-f72d-47b3-8985-5fda748735fb",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "b8448c62-bd01-4b35-96bd-7bb097d3583d",
  "sourceToolAssistantUUID": "2b9dbf81-f72d-47b3-8985-5fda748735fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T04:41:40.165Z_

Let me search for files related to literature_map parsing:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8448c62-bd01-4b35-96bd-7bb097d3583d",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCy8JAnpK3ehD6w7KdY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e6e66aa0-4a19-4af3-b01e-f3d396afa1eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ck9ivQyKMTzACttyqZaGcs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 33424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1394,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 6 · 2026-05-20T04:41:40.626Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VFrNQrtRDjTJmvn8cxdB6Q`</summary>

```json
{
  "pattern": "literature_map",
  "type": "py",
  "path": "/home/ubuntu/agent-ml-research",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6e66aa0-4a19-4af3-b01e-f3d396afa1eb",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCy8JAnpK3ehD6w7KdY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3863259c-e1ad-4fd9-b4e7-90b52f39212a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ck9ivQyKMTzACttyqZaGcs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 33424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1394,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 7 · 2026-05-20T04:41:40.793Z_

<details><summary>↩ Tool result · `toolu_01VFrNQrtRDjTJmvn8cxdB6Q`</summary>

```text
Found 20 files
/home/ubuntu/agent-ml-research/core/tools/distill.py
/home/ubuntu/agent-ml-research/tests/test_distill.py
/home/ubuntu/agent-ml-research/tests/test_progress_edge_cases.py
/home/ubuntu/agent-ml-research/tests/test_distill_progress.py
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/session_claude_md.py
/home/ubuntu/agent-ml-research/core/agents/message_router.py
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/core/api/routers/manager_api.py
/home/ubuntu/agent-ml-research/manager/api/distill_runs.py
/home/ubuntu/agent-ml-research/core/tools/architecture.py
/home/ubuntu/agent-ml-research/core/paths.py
/home/ubuntu/agent-ml-research/core/cron_hooks.py
/home/ubuntu/agent-ml-research/tests/test_semantic_scholar.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_reframe_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_full_draft_e2e.py
/home/ubuntu/agent-ml-research/tests/test_paper_agent_patch_e2e.py
/home/ubuntu/agent-ml-research/tests/test_literature_gap_fill.py
/home/ubuntu/agent-ml-research/tests/test_literature_map.py
/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3863259c-e1ad-4fd9-b4e7-90b52f39212a",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "5b6b0d07-7574-48b6-9b6c-cd0799057a79",
  "sourceToolAssistantUUID": "3863259c-e1ad-4fd9-b4e7-90b52f39212a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T04:41:40.927Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VyhBb67M4pJpPYyMzwTYsB`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -type f -name \"literature_map.yaml\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b6b0d07-7574-48b6-9b6c-cd0799057a79",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCy8JAnpK3ehD6w7KdY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "422f26e8-f9b0-4473-a0c8-4abeeacda228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ck9ivQyKMTzACttyqZaGcs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 33424,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 200,
          "cache_read_input_tokens": 33424,
          "cache_creation_input_tokens": 1394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1394,
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

_source line 9 · 2026-05-20T04:41:41.091Z_

<details><summary>↩ Tool result · `toolu_01VyhBb67M4pJpPYyMzwTYsB`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "422f26e8-f9b0-4473-a0c8-4abeeacda228",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "1df54fcb-822b-4ef9-aa84-bdfbfb70d033",
  "sourceToolAssistantUUID": "422f26e8-f9b0-4473-a0c8-4abeeacda228",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-20T04:41:42.124Z_

Now let me examine the key files that handle literature_map:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1df54fcb-822b-4ef9-aa84-bdfbfb70d033",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyHUaSj7rEh7tKDAFb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ee1fedf5-bf09-4fae-a1ec-6a4f0f738f83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011pCGrJo1ENhj258jepnBdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 34818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 11 · 2026-05-20T04:41:42.415Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HgPVzCqg2c9J6XavdmjRxT`</summary>

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
  "parentUuid": "ee1fedf5-bf09-4fae-a1ec-6a4f0f738f83",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyHUaSj7rEh7tKDAFb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5db21a0b-b5f5-4926-91ba-c45099b6845f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011pCGrJo1ENhj258jepnBdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 34818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 12 · 2026-05-20T04:41:42.424Z_

<details><summary>↩ Tool result · `toolu_01HgPVzCqg2c9J6XavdmjRxT`</summary>

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
  "parentUuid": "5db21a0b-b5f5-4926-91ba-c45099b6845f",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "cba36daf-d971-4524-b4e8-1380d1f46896",
  "sourceToolAssistantUUID": "5db21a0b-b5f5-4926-91ba-c45099b6845f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:41:42.576Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RxGDpxbT1Q1c55Taosr6xv`</summary>

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
  "parentUuid": "cba36daf-d971-4524-b4e8-1380d1f46896",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyHUaSj7rEh7tKDAFb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "595a5c21-3204-4591-828c-601f629d07bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011pCGrJo1ENhj258jepnBdC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 34818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 709,
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

_source line 14 · 2026-05-20T04:41:42.694Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CXJdh6mkrG3hzeHUXyptkV`</summary>

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
  "parentUuid": "595a5c21-3204-4591-828c-601f629d07bd",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyHUaSj7rEh7tKDAFb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de5a23a9-03ea-46c2-9307-ff84fc2dfa5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011pCGrJo1ENhj258jepnBdC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 709,
      "cache_read_input_tokens": 34818,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 709
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 193,
          "cache_read_input_tokens": 34818,
          "cache_creation_input_tokens": 709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 709,
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

_source line 15 · 2026-05-20T04:41:42.699Z_

<details><summary>↩ Tool result · `toolu_01CXJdh6mkrG3hzeHUXyptkV`</summary>

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
  "parentUuid": "de5a23a9-03ea-46c2-9307-ff84fc2dfa5b",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "28484392-f3d2-42f6-b937-2941642f0735",
  "sourceToolAssistantUUID": "de5a23a9-03ea-46c2-9307-ff84fc2dfa5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:41:42.833Z_

<details><summary>↩ Tool result · `toolu_01RxGDpxbT1Q1c55Taosr6xv`</summary>

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
535	    try:
536	        proc = await asyncio.create_subprocess_exec(
537	            *cmd,
538	            cwd=str(cwd),
539	            env=env,
540	            stdout=asyncio.subprocess.PIPE,
541	            stderr=asyncio.subprocess.PIPE,
542	        )
543	        stdout, stderr = await asyncio.wait_for(
544	            proc.communicate(),
545	            timeout=600,  # 10 min max
546	        )
547	
548	        if proc.returncode != 0:
549	            logger.warning(
550	                "Distiller session exited %d for %s: %s",
551	                proc.returncode, project,
552	                (stderr or b"").decode("utf-8", errors="replace")[:500],
553	            )
554	            return False
555	
556	        output = (stdout or b"").decode("utf-8", errors="replace")
557	        if "[DISTILL_DONE]" in output:
558	            logger.info("Distiller session completed successfully for %s", project)
559	            return True
560	
561	        logger.info("Distiller session finished for %s (no DONE marker)", project)
562	        return True
563	
564	    except asyncio.TimeoutError:
565	        logger.warning("Distiller session timed out for %s", project)
566	        return False
567	    except Exception:
568	        logger.exception("Distiller session failed for %s", project)
569	        return False
570	
571	
572	def _find_claude_binary() -> Path | None:
573	    """Locate the claude CLI binary."""
574	    import shutil
575	    for name in ("claude",):
576	        path = shutil.which(name)
577	        if path:
578	            return Path(path)
579	    return None
580	
581	
582	def _ensure_distiller_mcp_config() -> Path:
583	    """Write MCP config for Distiller role (minimal toolset)."""
584	    from core.session_server import _ensure_mcp_config_for_mode
585	    return _ensure_mcp_config_for_mode(
586	        "distiller",
587	        env_var="DISTILLER_MODE",
588	    )
589	
590	
591	# ---------------------------------------------------------------------------
592	# Skill writing / updating
593	# ---------------------------------------------------------------------------
594	
595	def _write_or_update_skills(
596	    project: str,
597	    papers: list[PaperForDistill],
598	) -> dict[str, Any]:
599	    """Read Layer 1/2 outputs and create/update skill files.
600	
601	    This is called after the Distiller session completes. The session
602	    writes skill files directly, so this function verifies they exist
603	    and returns metadata.
604	    """
605	    skills_dir = _paths.project_skills_dir(project)
606	    research_path = skills_dir / "distilled-research.skill.md"
607	    writing_path = skills_dir / "distilled-writing.skill.md"
608	
609	    result: dict[str, Any] = {
610	        "research_exists": research_path.exists(),
611	        "writing_exists": writing_path.exists(),
612	        "research_chars": 0,
613	        "writing_chars": 0,
614	        "research_version": 0,
615	        "writing_version": 0,
616	    }
617	
618	    if research_path.exists():
619	        text = research_path.read_text(encoding="utf-8")
620	        result["research_chars"] = len(text)
621	        try:
622	            skill = parse_skill_md(text, research_path)
623	            result["research_version"] = skill.version
624	        except Exception:
625	            pass
626	
627	    if writing_path.exists():
628	        text = writing_path.read_text(encoding="utf-8")
629	        result["writing_chars"] = len(text)
630	        try:
631	            skill = parse_skill_md(text, writing_path)
632	            result["writing_version"] = skill.version
633	        except Exception:
634	            pass
635	
636	    return result
637	
638	
639	def _backfill_literature_map(project: str, papers: list[PaperForDistill]) -> int:
640	    """Write newly discovered papers back to literature_map."""
641	    from core.tools.literature import add_to_literature_map
642	
643	    new_papers = []
644	    for p in papers:
645	        if not p.role:  # Papers without a role came from S2, not literature_map
646	            new_papers.append({
647	                "title": p.title,
648	                "year": p.year,
649	                "venue": p.venue,
650	                "authors": p.authors,
651	                "abstract": p.abstract,
652	                "doi": p.doi,
653	                "arxiv_id": p.arxiv_id,
654	                "url": p.url,
655	                "semantic_scholar_id": p.semantic_scholar_id,
656	                "role": "background",
657	                "verified": False,
658	            })
659	
660	    if not new_papers:
661	        return 0
662	
663	    result = add_to_literature_map(project, new_papers, added_by="distiller")
664	    if result.success:
665	        added = result.data.get("added", 0) if result.data else 0
666	        return added
667	    return 0
668	
669	
670	# ---------------------------------------------------------------------------
671	# Main entry point
672	# ---------------------------------------------------------------------------
673	
674	async def distill_project_skills(
675	    project: str,
676	    force: bool = False,
677	    auto_trigger: bool = False,
678	    callback_url: str = "",
679	    chat_id: str = "",
680	    operational_chat_id: str = "",
681	) -> DistillResult:
682	    """Main entry: collect papers → run Distiller session → verify skill output.
683	
684	    On success, also injects a ``[DISTILL]`` notification into the project's
685	    Director session (so Director can audit the distilled knowledge), mirroring
686	    the cron-hook / worker-done injection pattern.
687	
688	    Args:
689	        project: Project name.
690	        force: If True, re-distill even when no new papers are found.
691	        auto_trigger: True when fired by bootstrap auto-trigger; respects
692	            the ``auto_on_bootstrap`` config flag and silently skips if disabled.
693	        chat_id: A-group chat_id for progress card.
694	        operational_chat_id: B-group chat_id for phase notifications.
695	    """
696	    config = _load_distill_config()
697	
698	    # Bootstrap auto-trigger respects the config gate; explicit triggers ignore it.
699	    if auto_trigger and not config.get("auto_on_bootstrap", False):
700	        return DistillResult(
701	            success=False, project=project,
702	            error="auto_on_bootstrap disabled in config",
703	        )
704	
705	    # Fallback: load chat IDs from project config when not provided.
706	    if not chat_id or not operational_chat_id:
707	        try:
708	            from core.tools.project_config import load_project_config
709	            cfg_result = load_project_config(project)
710	            if cfg_result.success:
711	                feishu_cfg = (cfg_result.data or {}).get("config", {}).get("feishu", {})
712	                if not chat_id:
713	                    chat_id = feishu_cfg.get("chat_id", "")
714	                if not operational_chat_id:
715	                    operational_chat_id = feishu_cfg.get("operational_chat_id", "")
716	        except Exception:
717	            pass
718	
719	    # ── Progress helpers (same pattern as dream.py _run_dream_pipeline) ──
720	    started_at = datetime.now(timezone.utc).isoformat()
721	    _activity: list[tuple[str, str]] = []
722	    _ops_notified: set[str] = set()
723	    _card_msg_id = ""
724	
725	    _PHASE_LABEL = {
726	        "pending": "⏳ 启动",
727	        "collecting": "📚 论文收集中",
728	        "analyzing": "🔬 Distiller 精读中",
729	        "done": "✅ 完成",
730	        "failed": "❌ 失败",
731	        "skipped": "⏭️ 跳过",
732	    }
733	
734	    def _log(label: str, detail: str) -> None:
735	        _activity.append((label, detail))
736	
737	    def _notify_ops(phase: str, extra: str = "") -> None:
738	        if not operational_chat_id or phase in _ops_notified:
739	            return
740	        _ops_notified.add(phase)
741	        label = _PHASE_LABEL.get(phase, phase)
742	        text = f"[Distill] {project} — {label}"
743	        if extra:
744	            text += f"\n{extra[:300]}"
745	        try:
746	            from core.tools.feishu import send_message
747	            send_message(chat_id=operational_chat_id, text=text)
748	        except Exception:
749	            logger.debug("[distill] ops notify failed for %s", project, exc_info=True)
750	
751	    def _patch_card(phase: str, stages: list[str] | None = None,
752	                    error: str = "", result_summary: dict | None = None) -> None:
753	        nonlocal _card_msg_id
754	        if not _card_msg_id:
755	            return
756	        try:
757	            from core.tools.distill_card import patch_distill_card
758	            patch_distill_card(
759	                project=project, phase=phase, message_id=_card_msg_id,
760	                stages_completed=stages, activity=_activity, error=error,
761	                started_at=started_at, force=force, result_summary=result_summary,
762	            )
763	        except Exception:
764	            logger.debug("[distill] card patch failed for %s", project, exc_info=True)
765	
766	    # ── 0. Start ──
767	    _log("启动", f"开始蒸馏 {project}" + (" (force)" if force else ""))
768	    try:
769	        from core.tools.distill_card import send_distill_card
770	        _card_msg_id = send_distill_card(
771	            project=project, chat_id=chat_id, force=force, started_at=started_at,
772	        )
773	    except Exception:
774	        logger.debug("[distill] send card failed for %s", project, exc_info=True)
775	    _notify_ops("pending")
776	
777	    # Validate project exists
778	    project_cfg_path = _paths.projects_config_dir() / f"{project}.yaml"
779	    if not project_cfg_path.exists():
780	        _log("错误", f"项目 {project} 不存在")
781	        _patch_card("failed", error=f"项目 {project} 不存在")
782	        _notify_ops("failed", f"项目 {project} 不存在")
783	        return DistillResult(
784	            success=False, project=project,
785	            error=f"项目 {project} 不存在",
786	        )
787	
788	    # ── 1. Collect papers ──
789	    _log("收集", "从 literature_map + Semantic Scholar 收集论文...")
790	    _patch_card("collecting")
791	    _notify_ops("collecting")
792	
793	    papers = _collect_papers(project, config)
794	    if not papers:
795	        _log("收集", "未找到可供蒸馏的论文")
796	        result = DistillResult(
797	            success=False, project=project,
798	            error="未找到可供蒸馏的论文。请先在 literature_map 中添加论文。",
799	        )
800	        director_notified = False
801	        if not auto_trigger:
802	            director_notified = _inject_distill_failure_to_director(result)
803	            if director_notified:
804	                _notify_user_of_distill_followup(project, chat_id)
805	        if director_notified:
806	            _log("跟进", "已通知 Director 补充 literature_map 后重试")
807	            _patch_card("failed", error="literature_map 为空 → 已通知 Director 补充文献")
808	            _notify_ops("failed", "literature_map 为空 → 已通知 Director")
809	        else:
810	            _patch_card("failed", error="未找到论文")
811	            _notify_ops("failed", "未找到论文")
812	        return result
813	
814	    _log("收集", f"找到 {len(papers)} 篇候选论文")
815	    _patch_card("collecting", stages=["collect"])
816	
817	    # Incremental check
818	    existing_keys = _get_existing_paper_keys(project)
819	    new_paper_keys = {p.paper_key for p in papers} - existing_keys
820	    if not force and existing_keys and len(new_paper_keys) < 3:
821	        _log("增量", f"新增仅 {len(new_paper_keys)} 篇，跳过")
822	        _patch_card("skipped", stages=["collect"],
823	                    error=f"新增论文较少（{len(new_paper_keys)} 篇）")
824	        _notify_ops("skipped", f"仅 {len(new_paper_keys)} 篇新论文")
825	        return DistillResult(
826	            success=False, project=project,
827	            paper_count=len(papers),
828	            new_papers_found=len(new_paper_keys),
829	            error=f"新增论文较少（{len(new_paper_keys)} 篇），建议积累更多后再蒸馏。使用 force=True 强制蒸馏。",
830	        )
831	
832	    # Check which papers need Layer 1 analysis
833	    new_to_analyze, cached_yamls = _check_incremental(project, papers)
834	    max_deep_read = config.get("max_deep_read", 8)
835	    _log("增量", f"{len(new_to_analyze)} 篇新论文, {len(cached_yamls)} 篇已缓存")
836	
837	    # Ensure directories exist
838	    _distill_tmp_dir(project).mkdir(parents=True, exist_ok=True)
839	    _paths.project_skills_dir(project).mkdir(parents=True, exist_ok=True)
840	
841	    # Snapshot existing cached YAMLs so a failed session doesn't pollute
842	    # the cache with half-written Layer 1 outputs.
843	    pre_existing_cache = {p.name for p in _distill_tmp_dir(project).glob("*.yaml")}
844	
845	    # ── 2. Run Distiller Agent ──
846	    deep = min(len(new_to_analyze), max_deep_read)
847	    abstract = len(papers) - deep - len(cached_yamls)
848	    _log("精读", f"Distiller Agent 启动 ({deep} deep + {max(0, abstract)} abstract)")
849	    _patch_card("analyzing", stages=["collect"])
850	    _notify_ops("analyzing")
851	
852	    prompt = _build_distiller_prompt(new_to_analyze, cached_yamls, project, config)
853	    session_ok = await _run_distiller_session(project, prompt, config)
854	
855	    if not session_ok:
856	        _cleanup_partial_cache(project, pre_existing_cache)
857	        _log("失败", "Distiller session 执行失败")
858	        _patch_card("failed", stages=["collect"], error="Distiller session 失败")
859	        _notify_ops("failed", "session 执行失败")
860	        failure = DistillResult(
861	            success=False, project=project,
862	            paper_count=len(papers),
863	            error="Distiller session 执行失败",
864	        )
865	        _fire_completion_callback(failure, callback_url)
866	        return failure
867	
868	    # Verify outputs
869	    skill_info = _write_or_update_skills(project, papers)
870	
871	    if not skill_info["research_exists"] and not skill_info["writing_exists"]:
872	        _cleanup_partial_cache(project, pre_existing_cache)
873	        _log("失败", "未产出 skill 文件")
874	        _patch_card("failed", stages=["collect", "analyze"], error="未产出 skill")
875	        _notify_ops("failed", "未产出 skill 文件")
876	        failure = DistillResult(
877	            success=False, project=project,
878	            paper_count=len(papers),
879	            error="Distiller session 完成但未产出 skill 文件",
880	        )
881	        _fire_completion_callback(failure, callback_url)
882	        return failure
883	
884	    # Backfill new papers to literature_map
885	    backfilled = _backfill_literature_map(project, papers)
886	
887	    deep_count = min(len(new_to_analyze), max_deep_read) + len(cached_yamls)
888	    abstract_count = len(papers) - deep_count
889	
890	    result = DistillResult(
891	        success=True,
892	        project=project,
893	        version=max(skill_info.get("research_version", 0), skill_info.get("writing_version", 0)),
894	        paper_count=len(papers),
895	        deep_read_count=deep_count,
896	        abstract_only_count=max(0, abstract_count),
897	        new_papers_found=backfilled,
898	        research_skill_path=str(_paths.project_skills_dir(project) / "distilled-research.skill.md"),
899	        writing_skill_path=str(_paths.project_skills_dir(project) / "distilled-writing.skill.md"),
900	        research_skill_chars=skill_info.get("research_chars", 0),
901	        writing_skill_chars=skill_info.get("writing_chars", 0),
902	    )
903	
904	    # ── 3. Report ──
905	    summary = {
906	        "version": result.version,
907	        "deep_read_count": result.deep_read_count,
908	        "abstract_only_count": result.abstract_only_count,
909	        "research_skill_chars": result.research_skill_chars,
910	        "writing_skill_chars": result.writing_skill_chars,
911	        "new_papers_found": result.new_papers_found,
912	    }
913	    _log("完成", f"v{result.version}: research {result.research_skill_chars}字, writing {result.writing_skill_chars}字")
914	    _patch_card("done", stages=["collect", "analyze"], result_summary=summary)
915	    _notify_ops("done", f"v{result.version}, {result.paper_count} 篇")
916	
917	    # Inject [DISTILL] message into Director session (same pattern as
918	    # cron_hooks._route_to_director / dispatch_worker_done).
919	    _inject_distill_to_director(result, auto_trigger=auto_trigger)
920	
921	    # Fire callback so Manager can render the A群 Feishu notification.
922	    _fire_completion_callback(result, callback_url)
923	
924	    return result
925	
926	
927	def _fire_completion_callback(result: DistillResult, callback_url: str) -> None:
928	    """POST distillation result back to Manager (best-effort).
929	
930	    Includes the project's A群 chat_id so Manager can render the Feishu
931	    notification without an extra round-trip to BE for project config.
932	    Silently no-ops when ``callback_url`` is empty (manual MCP-tool path).
933	    """
934	    if not callback_url:
935	        return
936	
937	    chat_id = ""
938	    try:
939	        from core.tools.project_config import load_project_config
940	        cfg_result = load_project_config(result.project)
941	        if cfg_result.success and isinstance(cfg_result.data, dict):
942	            cfg = cfg_result.data.get("config", {})
943	            chat_id = (cfg.get("feishu") or {}).get("chat_id", "") or ""
944	    except Exception:
945	        logger.debug("[distill] failed to resolve chat_id for callback", exc_info=True)
946	
947	    try:
948	        from core.tools.distill_callbacks import DistillCallbacks
949	        emitter = DistillCallbacks.from_args(callback_url=callback_url)
950	        if emitter is None:
951	            return
952	        emitter.complete(
953	            project=result.project,
954	            status="completed" if result.success else "failed",
955	            version=result.version,
956	            paper_count=result.paper_count,
957	            deep_read_count=result.deep_read_count,
958	            abstract_only_count=result.abstract_only_count,
959	            new_papers_found=result.new_papers_found,
960	            research_skill_chars=result.research_skill_chars,
961	            writing_skill_chars=result.writing_skill_chars,
962	            chat_id=chat_id,
963	            error=result.error,
964	        )
965	    except Exception:
966	        logger.exception("[distill] completion callback failed for %s", result.project)
967	
968	
969	# ---------------------------------------------------------------------------
970	# Director session injection (mirrors cron_hooks pattern)
971	# ---------------------------------------------------------------------------
972	
973	def _inject_distill_to_director(result: DistillResult, auto_trigger: bool = False) -> None:
974	    """Inject ``[DISTILL]`` notification into the project's Director session.
975	
976	    Mirrors ``core.cron_hooks._route_to_director`` / ``dispatch_worker_done``:
977	    fact-only message (no skill loading), Director decides what to do next.
978	
979	    ``auto_trigger=True`` (bootstrap) sends a review-oriented message;
980	    ``auto_trigger=False`` (manual ``/distill``) sends an action-oriented
981	    message asking Director to review across three dimensions.
982	    """
983	    try:
984	        from core.cron_hooks import _find_director_for_project
985	        from core.session_server import get_server
986	
987	        director_info = _find_director_for_project(result.project)
988	        if not director_info:
989	            logger.info(
990	                "[distill] no Director session for %s, skipping injection",
991	                result.project,
992	            )
993	            return
994	        director_key, _ = director_info
995	
996	        srv = get_server()
997	        if not srv._started:
998	            logger.info("[distill] SessionServer not started, skipping injection")
999	            return
1000	
1001	        header = (
1002	            f"[DISTILL] 文献蒸馏已完成（v{result.version}，"
1003	            f"基于 {result.paper_count} 篇论文，精读 {result.deep_read_count} 篇）。\n"
1004	            f"研究方法论 skill：Read {result.research_skill_path}\n"
1005	            f"写作范式 skill：Read {result.writing_skill_path}"
1006	        )
1007	
1008	        if auto_trigger:
1009	            message = (
1010	                f"{header}\n"
1011	                f"请审阅蒸馏质量，确认是否准确。后续规划实验和论文写作时参考其中同行的做法和经验。"
1012	            )
1013	        else:
1014	            message = (
1015	                f"{header}\n\n"
1016	                f"请精读两个 skill，从相似和相关论文的经验中吸收可借鉴之处，对照当前项目审视：\n"
1017	                f"1. 研究方向：竞品的 claim 和我们是否重叠？蒸馏揭示的研究空白对 framing 有无启发？"
1018	                f"→ 需调整则更新 paper_framing.md + ROADMAP\n"
1019	                f"2. 实验计划：同行常用的 baseline/metric/dataset 是否已覆盖？方法论趋势对当前路线有无启发？"
1020	                f"→ 需调整则更新 experiment_plan.yaml\n"
1021	                f"3. 论文写作：同领域的叙事策略、结构惯例有无值得借鉴？"
1022	                f"→ 需调整则 director_post_to_paper_agent 通知\n"
1023	                f"判断后行动，用 director_reply_to_user 汇报审视结论和调整决定。"
1024	            )
1025	
1026	        def _silent_reply(reply: str) -> None:
1027	            logger.debug("[distill] Director reply silenced: %s", (reply or "")[:80])
1028	
1029	        srv.send_sync(
1030	            project=result.project,
1031	            message=message,
1032	            reply_fn=_silent_reply,
1033	            session_key=director_key,
1034	            source="distill:done",
1035	        )
1036	        logger.info("[distill] injected [DISTILL] into Director %s", director_key)
1037	    except Exception:
1038	        logger.exception(
1039	            "[distill] failed to inject [DISTILL] for project=%s", result.project,
1040	        )
1041	
1042	
1043	def _inject_distill_failure_to_director(result: DistillResult) -> bool:
1044	    """Inject guidance into Director when distill fails due to empty literature_map.
1045	
1046	    Returns True iff the Director session was found and the message was queued.
1047	    """
1048	    try:
1049	        from core.cron_hooks import _find_director_for_project
1050	        from core.session_server import get_server
1051	
1052	        director_info = _find_director_for_project(result.project)
1053	        if not director_info:
1054	            logger.info(
1055	                "[distill] no Director session for %s, failure guidance not delivered",
1056	                result.project,
1057	            )
1058	            return False
1059	        director_key, _ = director_info
1060	
1061	        srv = get_server()
1062	        if not srv._started:
1063	            return False
1064	
1065	        idea_brief = _paths.resolve_project_file(result.project, "IDEA_BRIEF.md")
1066	        ref_hint = (
1067	            f"参考 `{idea_brief}` 中的 key_references 和研究方向，"
1068	            if idea_brief.exists() else "通过深度文献调研，"
1069	        )
1070	
1071	        message = (
1072	            f"[DISTILL] 蒸馏失败：{result.error}\n\n"
1073	            f"`literature_map.yaml` 是蒸馏的输入源。请{ref_hint}"
1074	            f"用 `add_to_literature_map` 添加 ≥5 篇核心相关论文（含 S2 paper ID 或 arXiv ID），"
1075	            f"填充完毕后通知用户重新触发 `/distill`。"
1076	        )
1077	
1078	        def _silent_reply(reply: str) -> None:
1079	            logger.debug("[distill] Director reply silenced: %s", (reply or "")[:80])
1080	
1081	        srv.send_sync(
1082	            project=result.project,
1083	            message=message,
1084	            reply_fn=_silent_reply,
1085	            session_key=director_key,
1086	            source="distill:failed",
1087	        )
1088	        logger.info("[distill] injected [DISTILL] failure guidance into Director %s", director_key)
1089	        return True
1090	    except Exception:
1091	        logger.exception(
1092	            "[distill] failed to inject failure guidance for project=%s", result.project,
1093	        )
1094	        return False
1095	
1096	
1097	def _notify_user_of_distill_followup(project: str, chat_id: str) -> None:
1098	    """Notify A群 that Director was asked to fill literature_map after distill failure."""
1099	    if not chat_id:
1100	        return
1101	    try:
1102	        from core.tools.feishu import send_message
1103	        send_message(
1104	            chat_id=chat_id,
1105	            text=(
1106	                f"📚 {project} 的文献蒸馏暂时无法进行：literature_map 为空。\n"
1107	                f"已请 Director 参考 IDEA_BRIEF 的 key_references + 深度文献调研补充论文，"
1108	                f"完成后会再通知您触发 /distill。"
1109	            ),
1110	        )
1111	    except Exception:
1112	        logger.debug(
1113	            "[distill] failed to send A群 follow-up notice for %s", project, exc_info=True,
1114	        )
1115	
1116	
1117	# ---------------------------------------------------------------------------
1118	# Cache cleanup
1119	# ---------------------------------------------------------------------------
1120	
1121	def _cleanup_partial_cache(project: str, pre_existing: set[str]) -> None:
1122	    """Remove Layer 1 YAML files written during a failed run.
1123	
1124	    Files present before the run are preserved (those are valid cached
1125	    analyses from prior successful runs). Only new partial writes get cleaned.
1126	    """
1127	    try:
1128	        tmp_dir = _distill_tmp_dir(project)
1129	        if not tmp_dir.exists():
1130	            return
1131	        for yaml_file in tmp_dir.glob("*.yaml"):
1132	            if yaml_file.name not in pre_existing:
1133	                yaml_file.unlink(missing_ok=True)
1134	        logger.info("[distill] cleaned partial cache for %s", project)
1135	    except Exception:
1136	        logger.exception("[distill] cache cleanup failed for %s", project)
1137	
1138	
1139	# ---------------------------------------------------------------------------
1140	# MCP tool wrapper
1141	# ---------------------------------------------------------------------------
1142	
1143	def distill_papers(project: str, force: bool = False) -> ToolResult:
1144	    """从文献库蒸馏研究方法论和写作范式，生成项目专属 skill。
1145	
1146	    自动收集 literature_map + Semantic Scholar 论文，
1147	    用 Claude 分析后生成/更新 distilled-research 和 distilled-writing skill。
1148	
1149	    Args:
1150	        project: 项目名称
1151	        force: True 则忽略"无新论文"检查，强制重新蒸馏
1152	    """
1153	    try:
1154	        loop = asyncio.get_running_loop()
1155	    except RuntimeError:
1156	        loop = None
1157	
1158	    if loop and loop.is_running():
1159	        import concurrent.futures
1160	        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
1161	            result = pool.submit(
1162	                lambda: asyncio.run(distill_project_skills(project, force=force))
1163	            ).result(timeout=660)
1164	    else:
1165	        result = asyncio.run(distill_project_skills(project, force=force))
1166	
1167	    if not result.success:
1168	        return ToolResult(success=False, error=result.error)
1169	
1170	    return ToolResult(
1171	        success=True,
1172	        data={
1173	            "project": result.project,
1174	            "version": result.version,
1175	            "paper_count": result.paper_count,
1176	            "deep_read_count": result.deep_read_count,
1177	            "abstract_only_count": result.abstract_only_count,
1178	            "new_papers_found": result.new_papers_found,
1179	            "research_skill_path": result.research_skill_path,
1180	            "writing_skill_path": result.writing_skill_path,
1181	            "research_skill_chars": result.research_skill_chars,
1182	            "writing_skill_chars": result.writing_skill_chars,
1183	            "summary": (
1184	                f"📚 {project} 文献蒸馏完成 (v{result.version})\n"
1185	                f"├ 精读论文：{result.deep_read_count} 篇（全文）"
1186	                f"+ {result.abstract_only_count} 篇（仅摘要）\n"
1187	                f"├ 研究方法论 skill：{result.research_skill_chars} 字\n"
1188	                f"├ 写作范式 skill：{result.writing_skill_chars} 字\n"
1189	                f"└ 新发现论文：{result.new_papers_found} 篇已回写 literature_map"
1190	            ),
1191	        },
1192	    )
1193	
1194	
1195	# ---------------------------------------------------------------------------
1196	# Status query
1197	# ---------------------------------------------------------------------------
1198	
1199	def get_distill_status(project: str) -> ToolResult:
1200	    """查看蒸馏状态：最后蒸馏时间、论文数、version。
1201	
1202	    `literature_map_total` 和 `cached_layer1_count` 即使在 never_distilled 时也
1203	    返回真实值——caller 用这两个字段排查"为啥蒸馏跑不动/没产出"，所以不能因为没
1204	    skill 文件就早退。
1205	    """
1206	    from core.tools.literature import get_literature_map_path, _read_map
1207	
1208	    skills_dir = _paths.project_skills_dir(project)
1209	    research_path = skills_dir / "distilled-research.skill.md"
1210	    writing_path = skills_dir / "distilled-writing.skill.md"
1211	    tmp_dir = _distill_tmp_dir(project)
1212	
1213	    lit_path = get_literature_map_path(project)
1214	    lit_map = _read_map(lit_path)
1215	    literature_map_total = len(lit_map.get("papers") or {})
1216	    cached_count = len(list(tmp_dir.glob("*.yaml"))) if tmp_dir.exists() else 0
1217	
1218	    if not research_path.exists() and not writing_path.exists():
1219	        return ToolResult(
1220	            success=True,
1221	            data={
1222	                "status": "never_distilled",
1223	                "project": project,
1224	                "literature_map_total": literature_map_total,
1225	                "cached_layer1_count": cached_count,
1226	            },
1227	        )
1228	
1229	    info: dict[str, Any] = {
1230	        "project": project,
1231	        "status": "distilled",
1232	        "literature_map_total": literature_map_total,
1233	        "cached_layer1_count": cached_count,
1234	    }
1235	
1236	    for label, path in [("research", research_path), ("writing", writing_path)]:
1237	        if path.exists():
1238	            text = path.read_text(encoding="utf-8")
1239	            fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
1240	            if fm_match:
1241	                fm = yaml.safe_load(fm_match.group(1)) or {}
1242	                info[f"{label}_version"] = fm.get("version", 1)
1243	                df = fm.get("distilled_from") or {}
1244	                info[f"{label}_paper_count"] = df.get("paper_count", 0)
1245	                info[f"{label}_last_distilled"] = df.get("last_distilled", "")
1246	                info[f"{label}_chars"] = len(text)
1247	
1248	    # Delta since last distill
1249	    existing_keys = _get_existing_paper_keys(project)
1250	    all_keys = set((lit_map.get("papers") or {}).keys())
1251	    delta = len(all_keys - existing_keys) if existing_keys else 0
1252	    info["new_since_last_distill"] = delta
1253	
1254	    return ToolResult(success=True, data=info)
1255	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "595a5c21-3204-4591-828c-601f629d07bd",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "b2620231-2a56-4116-a38b-35cb8e57b19e",
  "sourceToolAssistantUUID": "595a5c21-3204-4591-828c-601f629d07bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T04:41:44.877Z_

Now let me check how the MCP server exposes these tools:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2620231-2a56-4116-a38b-35cb8e57b19e",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyQuoc3zisepT1joBH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0df830c6-9f22-4357-82dc-b32589711e92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016rXnkqsY4awkfE7Ysm8EjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6599,
      "cache_creation_input_tokens": 25074,
      "cache_read_input_tokens": 35527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25074,
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

_source line 18 · 2026-05-20T04:41:45.601Z_

<details open><summary>🔧 Tool call — Grep · `toolu_015gzrGSxSejP8nMQCaDFDsA`</summary>

```json
{
  "pattern": "add_to_literature_map|distill_papers",
  "type": "py",
  "path": "/home/ubuntu/agent-ml-research/core",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0df830c6-9f22-4357-82dc-b32589711e92",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyQuoc3zisepT1joBH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8bb3d0ab-4b09-4f26-a538-8d2a2196bcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016rXnkqsY4awkfE7Ysm8EjQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6599,
      "cache_creation_input_tokens": 25074,
      "cache_read_input_tokens": 35527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25074,
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

_source line 19 · 2026-05-20T04:41:45.620Z_

<details><summary>↩ Tool result · `toolu_015gzrGSxSejP8nMQCaDFDsA`</summary>

```text
Found 6 files
/home/ubuntu/agent-ml-research/core/tools/distill.py
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/session_claude_md.py
/home/ubuntu/agent-ml-research/core/tool_registry.py
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/core/tools/semantic_scholar.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bb3d0ab-4b09-4f26-a538-8d2a2196bcd5",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "f0e811d9-a56d-492d-bde5-eef3c12910e4",
  "sourceToolAssistantUUID": "8bb3d0ab-4b09-4f26-a538-8d2a2196bcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T04:41:45.847Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Au5w5haEUp8yD31JMLjjbt`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0e811d9-a56d-492d-bde5-eef3c12910e4",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyQuoc3zisepT1joBH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50e531be-b5ed-44a2-94fb-eb36772e7289",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016rXnkqsY4awkfE7Ysm8EjQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6599,
      "cache_creation_input_tokens": 25074,
      "cache_read_input_tokens": 35527,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6599,
          "output_tokens": 217,
          "cache_read_input_tokens": 35527,
          "cache_creation_input_tokens": 25074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25074,
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

_source line 21 · 2026-05-20T04:41:45.857Z_

<details><summary>↩ Tool result · `toolu_01Au5w5haEUp8yD31JMLjjbt`</summary>

```text
1	"""MCP Server — exposes SSH, W&B, and Registry tools via the Model Context Protocol.
2	
3	Usage:
4	    python -m core.mcp_server          # stdio transport (default, for Claude Code)
5	    python -m core.mcp_server --sse    # SSE transport (for remote clients)
6	"""
7	
8	from __future__ import annotations
9	
10	import json
11	import logging
12	import os
13	from dataclasses import asdict
14	from datetime import datetime, timezone
15	from pathlib import Path
16	from typing import Any
17	
18	logger = logging.getLogger(__name__)
19	
20	from mcp.server.fastmcp import FastMCP
21	
22	from core.tools import (
23	    artifacts as artifacts_mod,
24	    architecture as architecture_mod,
25	    clone_repo as clone_repo_mod,
26	    cron, feishu, feishu_group as feishu_group_mod,
27	    external_review as external_review_mod,
28	    visual_check as visual_check_mod,
29	    file_parser as file_parser_mod,
30	    gpu_monitor as gpu_monitor_mod,
31	    image_tools as image_tools_mod,
32	    model_registry as model_registry_mod,
33	    oss_backup, pai_eas, s3_backup,
34	    project_config, registry, ssh, wandb_client, workspace,
35	    worker as worker_mod,
36	)
37	
38	# ---------------------------------------------------------------------------
39	# Server instance
40	# ---------------------------------------------------------------------------
41	
42	mcp = FastMCP(
43	    "agent-ml-research",
44	    instructions="ML research experiment management tools",
45	)
46	
47	
48	def _tool_result_to_str(result: ssh.ToolResult) -> str:
49	    """Convert a ToolResult dataclass to a JSON string for MCP response."""
50	    return json.dumps(asdict(result), ensure_ascii=False, default=str)
51	
52	
53	# ---------------------------------------------------------------------------
54	# Chat routing helpers — resolve target chat_id from env + project config
55	# ---------------------------------------------------------------------------
56	
57	def _get_session_chat_id() -> str:
58	    """获取当前 session 绑定的群 chat_id（环境变量注入）。"""
59	    return os.environ.get("AGENT_ML_SESSION_CHAT_ID", "")
60	
61	
62	def _get_session_project() -> str:
63	    """获取当前 session 绑定的项目名。"""
64	    return os.environ.get("AGENT_ML_SESSION_PROJECT", "")
65	
66	
67	def _resolve_user_group_chat(project: str = "") -> str:
68	    """解析 A群 (user-facing group) chat_id。
69	
70	    用于目标固定发到 A群 的工具（approval_card, result_card 等）。
71	    无项目或单群模式时 fallback 到 session 所在群。
72	    """
73	    if not project:
74	        project = _get_session_project()
75	    if project:
76	        try:
77	            from core.tools.project_config import load_project_config
78	            result = load_project_config(project)
79	            if result.success:
80	                user_chat = result.data.get("config", {}).get("feishu", {}).get("chat_id", "")
81	                if user_chat:
82	                    return user_chat
83	        except Exception:
84	            pass
85	    return _get_session_chat_id()
86	
87	
88	def _resolve_ops_chat(project: str = "") -> str:
89	    """解析 B群 (operational_chat_id)，无则 fallback 到 A群。"""
90	    if not project:
91	        project = _get_session_project()
92	    if project:
93	        try:
94	            from core.tools.project_config import load_project_config
95	            result = load_project_config(project)
96	            if result.success:
97	                feishu_cfg = result.data.get("config", {}).get("feishu", {})
98	                return (
99	                    feishu_cfg.get("operational_chat_id")
100	                    or feishu_cfg.get("chat_id", "")
101	                )
102	        except Exception:
103	            pass
104	    return _get_session_chat_id()
105	
106	
107	# ---------------------------------------------------------------------------
108	# SSH Tools
109	# ---------------------------------------------------------------------------
110	
111	@mcp.tool()
112	def ssh_execute(server: str, command: str, warn: bool = False, account: str | None = None) -> str:
113	    """Execute an arbitrary command on a remote GPU server.
114	
115	    Args:
116	        server: Server name from resources.yaml (e.g. "A6000").
117	        command: Shell command to execute.
118	        warn: If True, don't raise on non-zero exit code.
119	        account: SSH account (user) on the server. None = use project's default.
120	    """
121	    result = ssh.ssh_execute(server, command, account=account, warn=warn)
122	    return _tool_result_to_str(result)
123	
124	
125	@mcp.tool()
126	def submit_training_job(
127	    server: str,
128	    gpu_ids: list[str],
129	    command: str,
130	    exp_id: str,
131	    timeout_hours: float = 24.0,
132	    account: str | None = None,
133	    project: str | None = None,
134	    plan_id: str | None = None,
135	) -> str:
136	    """Submit a training job to a remote GPU server via tmux.
137	
138	    Validates GPUs against resources.yaml (including collision detection),
139	    launches in detached tmux session. Consider using allocate_and_submit
140	    instead for a fully atomic workflow.
141	
142	    ⚠️ CRITICAL — `command` MUST be wrapped in `bash -c "..."` whenever it uses
143	    bash built-ins (`source`, `conda activate`, brace expansion, arrays, etc.).
144	    tmux runs the command under `sh`, not bash; unwrapped `source ... && python`
145	    will fail with EXIT_CODE=127 in ~1-3 minutes and the job never starts.
146	
147	    Examples:
148	        ❌ `source /root/miniconda3/bin/activate base && python train.py`
149	        ✅ `bash -c "source /root/miniconda3/bin/activate base && python train.py"`
150	        ✅ `/root/miniconda3/envs/myenv/bin/python train.py`  (abs path, no source needed)
151	
152	    Args:
153	        server: Server name from resources.yaml.
154	        gpu_ids: CUDA device ids (e.g. ["cuda:0", "cuda:1"]).
155	        command: Training command to execute. Wrap in `bash -c "..."` if using
156	            `source` / `conda activate` / other bash built-ins.
157	        exp_id: Experiment identifier (used as tmux session name).
158	        timeout_hours: Max runtime before auto-kill (default 24h).
159	        account: SSH account (user) on the server. None = use project's default.
160	        project: Project name for access control and directory isolation.
161	        plan_id: Optional experiment_plan entry id. When supplied with
162	            ``project``, the new ``exp_id`` is linked back as ``registry_id``
163	            in ``experiment_plan.yaml`` so the plan view shows live status.
164	    """
165	    # Hard guardrail: reject unwrapped bash built-ins. Docstring reminders
166	    # alone (above) aren't enough — EXIT_CODE=127 复发过多次。拦在入口让
167	    # Agent 立即拿到明确错误 + 修复提示, 避免跑 1-3 分钟才失败。
168	    import re as _re
169	    stripped = (command or "").lstrip()
170	    if not (stripped.startswith("bash -c ") or stripped.startswith("/bin/bash -c ")):
171	        _unwrapped_pat = _re.compile(
172	            r"(?:^|(?:&&|\|\||;)\s*)\s*(source\b|conda\s+activate\b|\.\s+\S)",
173	            _re.IGNORECASE,
174	        )
175	        if _unwrapped_pat.search(command or ""):
176	            escaped = (command or "").replace('"', '\\"')
177	            return _tool_result_to_str(ssh.ToolResult(
178	                success=False,
179	                error=(
180	                    "command uses bash built-ins (source / conda activate) but is "
181	                    "NOT wrapped in `bash -c \"...\"`. tmux launches under sh which "
182	                    "doesn't recognize these built-ins → EXIT_CODE=127 after ~1-3 min.\n\n"
183	                    f"Retry with: bash -c \"{escaped}\"\n\n"
184	                    "Or use absolute python path to avoid source entirely:\n"
185	                    "  /root/miniconda3/envs/&lt;env>/bin/python &lt;script>.py"
186	                ),
187	            ))
188	    result = ssh.submit_training_job(
189	        server, gpu_ids, command, exp_id, timeout_hours,
190	        account=account, project=project, plan_id=plan_id,
191	    )
192	    return _tool_result_to_str(result)
193	
194	
195	@mcp.tool()
196	def check_job_status(server: str, pid: str, account: str | None = None) -> str:
197	    """Check whether a training job is still running on a remote server.
198	
199	    Args:
200	        server: Server name from resources.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50e531be-b5ed-44a2-94fb-eb36772e7289",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "d10b35d2-e9a1-452f-b797-ee41009299ce",
  "sourceToolAssistantUUID": "50e531be-b5ed-44a2-94fb-eb36772e7289",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-20T04:41:47.214Z_

Let me search for where `add_to_literature_map` is exposed in the MCP server:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d10b35d2-e9a1-452f-b797-ee41009299ce",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCydz7SpRDWhxBff6Cv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dad3974f-1ba0-46e7-926f-050ddf14bb27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sy5XNHMec9bpW6TuRTqPJe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9657,
      "cache_read_input_tokens": 60601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9657,
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

_source line 23 · 2026-05-20T04:41:47.619Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01N9RX6hKuBVkY76BHz928Q4`</summary>

```json
{
  "command": "grep -n \"add_to_literature_map\\|distill_papers\" /home/ubuntu/agent-ml-research/core/mcp_server.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dad3974f-1ba0-46e7-926f-050ddf14bb27",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCydz7SpRDWhxBff6Cv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "057194cb-4cc4-428d-a094-7d10952f4a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Sy5XNHMec9bpW6TuRTqPJe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9657,
      "cache_read_input_tokens": 60601,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9657
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 111,
          "cache_read_input_tokens": 60601,
          "cache_creation_input_tokens": 9657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9657,
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

_source line 24 · 2026-05-20T04:41:47.666Z_

<details><summary>↩ Tool result · `toolu_01N9RX6hKuBVkY76BHz928Q4`</summary>

```text
2899:def distill_papers(project: str, force: bool = False) -> str:
2912:    from core.tools.distill import distill_papers as _dp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "057194cb-4cc4-428d-a094-7d10952f4a6f",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "4ee63a94-54ee-4876-94d0-ae284120e477",
  "sourceToolAssistantUUID": "057194cb-4cc4-428d-a094-7d10952f4a6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T04:41:49.919Z_

Let me check the full MCP server to see all literature-related tools:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ee63a94-54ee-4876-94d0-ae284120e477",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCymczddnBDK42GNzSH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9fa566c-cee7-44c5-921b-e946b9e235a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BA1GVaLni3XXwqKpo647F8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 70258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 166,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 26 · 2026-05-20T04:41:50.370Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bp2GUs32j4PkVYUaG8Q5eg`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/mcp_server.py",
  "offset": 2890,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9fa566c-cee7-44c5-921b-e946b9e235a0",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCymczddnBDK42GNzSH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62ecd3aa-05f7-48ef-bb20-297511cabd7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BA1GVaLni3XXwqKpo647F8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 70258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 166,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 27 · 2026-05-20T04:41:50.380Z_

<details><summary>↩ Tool result · `toolu_01Bp2GUs32j4PkVYUaG8Q5eg`</summary>

```text
2890	    from core.tools.dream import get_dream_trend as _gdt
2891	    return _tool_result_to_str(_gdt(project, limit=limit))
2892	
2893	
2894	# ---------------------------------------------------------------------------
2895	# Paper Distillation — domain knowledge extraction
2896	# ---------------------------------------------------------------------------
2897	
2898	@mcp.tool()
2899	def distill_papers(project: str, force: bool = False) -> str:
2900	    """从文献库蒸馏研究方法论和写作范式，生成项目专属 skill。
2901	
2902	    自动收集 literature_map + Semantic Scholar 论文，
2903	    用 Claude 分析后生成/更新 distilled-research 和 distilled-writing skill。
2904	
2905	    异步执行——Distiller Agent session 在后台运行，预计 5-10 分钟。
2906	    蒸馏完成后自动通知。
2907	
2908	    Args:
2909	        project: 项目名称
2910	        force: True 则忽略"无新论文"检查，强制重新蒸馏
2911	    """
2912	    from core.tools.distill import distill_papers as _dp
2913	    return _tool_result_to_str(_dp(project, force=force))
2914	
2915	
2916	@mcp.tool()
2917	def get_distill_status(project: str) -> str:
2918	    """查看蒸馏状态：最后蒸馏时间、论文数、version、新增论文数。
2919	
2920	    Args:
2921	        project: 项目名称
2922	    """
2923	    from core.tools.distill import get_distill_status as _gds
2924	    return _tool_result_to_str(_gds(project))
2925	
2926	
2927	@mcp.tool()
2928	def auto_build_report_facts(project: str) -> str:
2929	    """Regenerate the auto-derived facts block in report.md from registry.
2930	
2931	    Treat report.md as two sections:
2932	      - AUTO-FACTS block (between &lt;!-- AUTO-FACTS-BEGIN --> and &lt;!-- AUTO-FACTS-END -->)
2933	        → regenerated from registry by this tool
2934	      - Analysis tail (everything below END marker)
2935	        → human-authored by Director, preserved across calls
2936	
2937	    Idempotent: calling twice in a row produces identical output except for
2938	    the generated-at timestamp. The canonical facts include: experiment
2939	    counts by status/conclusion, RUNNING table (server/gpu/pid/log), recent
2940	    completions, recent failures with failure_reason, and GPU allocation
2941	    summary. This replaces hand-written "current state" paragraphs that
2942	    drifted from registry.
2943	
2944	    Call on Director session boot and after any experiment state change.
2945	
2946	    Args:
2947	        project: Project name.
2948	    """
2949	    from core.tools.report_facts import auto_build_report_facts as _abrf
2950	    result = _abrf(project)
2951	    return _tool_result_to_str(result)
2952	
2953	
2954	@mcp.tool()
2955	def bootstrap_provenance(project: str, force: bool = False) -> str:
2956	    """Auto-generate paper_provenance.yaml by scanning existing tex files.
2957	
2958	    Use this when a project has paper tex files but no provenance data yet.
2959	    Extracts claims (quantitative results, finding statements), figures,
2960	    and tables from all .tex files. Skipped if provenance already exists
2961	    unless force=True.
2962	
2963	    Args:
2964	        project: Project name.
2965	        force: Overwrite existing provenance (default False).
2966	    """
2967	    from core.tools.provenance import bootstrap_provenance_from_tex
2968	    result = bootstrap_provenance_from_tex(project, force=force)
2969	    return _tool_result_to_str(result)
2970	
2971	
2972	@mcp.tool()
2973	def impact_analysis(
2974	    project: str,
2975	    change_type: str,
2976	    change_id: str,
2977	    change_desc: str = "",
2978	) -> str:
2979	    """Analyze impact of experiment/decision change on downstream decisions and paper.
2980	
2981	    Args:
2982	        project: Project name.
2983	        change_type: "experiment" or "decision".
2984	        change_id: The exp_id or decision_id that changed.
2985	        change_desc: Description of the change.
2986	    """
2987	    from core.tools.provenance import impact_analysis as _ia
2988	    result = _ia(project, change_type, change_id, change_desc=change_desc)
2989	    return _tool_result_to_str(result)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62ecd3aa-05f7-48ef-bb20-297511cabd7b",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "cba807bd-2283-48c3-bc78-0bfe1a41855b",
  "sourceToolAssistantUUID": "62ecd3aa-05f7-48ef-bb20-297511cabd7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T04:41:50.461Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MYE7Ne18rqHbvtXMxzCgU7`</summary>

```json
{
  "command": "grep -n \"^def \" /home/ubuntu/agent-ml-research/core/mcp_server.py | grep -i \"literature\\|distill\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cba807bd-2283-48c3-bc78-0bfe1a41855b",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCymczddnBDK42GNzSH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c4899462-d733-4b82-91ae-dfad82aac555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BA1GVaLni3XXwqKpo647F8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 166,
      "cache_read_input_tokens": 70258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 166,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 29 · 2026-05-20T04:41:50.509Z_

<details><summary>↩ Tool result · `toolu_01MYE7Ne18rqHbvtXMxzCgU7`</summary>

```text
2899:def distill_papers(project: str, force: bool = False) -> str:
2917:def get_distill_status(project: str) -> str:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4899462-d733-4b82-91ae-dfad82aac555",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "d580734d-fe62-4198-adf5-4d96ea7843db",
  "sourceToolAssistantUUID": "c4899462-d733-4b82-91ae-dfad82aac555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T04:41:52.374Z_

Now let me check if `add_to_literature_map` is exposed as an MCP tool:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d580734d-fe62-4198-adf5-4d96ea7843db",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyyytY7mEN9ukYWhap",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb0f93ec-6091-436a-b2f7-a8e7f6b42ddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AT85KmFZTRERitp22AEGde",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 70424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1655,
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

_source line 31 · 2026-05-20T04:41:52.963Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R9jKibAweG8f6qsmcAwrJi`</summary>

```json
{
  "command": "grep -n \"literature_map\\|add_to\" /home/ubuntu/agent-ml-research/core/mcp_server.py | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb0f93ec-6091-436a-b2f7-a8e7f6b42ddf",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCyyytY7mEN9ukYWhap",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c9371dd5-0c1d-4c4f-9ca4-b60c7e036019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AT85KmFZTRERitp22AEGde",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 70424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1655,
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

_source line 32 · 2026-05-20T04:41:53.006Z_

<details><summary>↩ Tool result · `toolu_01R9jKibAweG8f6qsmcAwrJi`</summary>

```text
2902:    自动收集 literature_map + Semantic Scholar 论文，
3004:    literature_map.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9371dd5-0c1d-4c4f-9ca4-b60c7e036019",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "00df402f-7fb9-45e5-85b7-bc60e0be9bdd",
  "sourceToolAssistantUUID": "c9371dd5-0c1d-4c4f-9ca4-b60c7e036019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T04:41:54.168Z_

Let me check if there are any other files that might export literature tools:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00df402f-7fb9-45e5-85b7-bc60e0be9bdd",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCzArF7fbicBJuEFSob",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c9345c1-41c0-489d-ba2f-c9671783c998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QY7svHLB2WBQDYZHgxZ9mH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 72079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 154,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 34 · 2026-05-20T04:41:54.443Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01U17HXKfr8XHEuJMnx4WmQw`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -type f -name \"*.py\" -path \"*/core/tools/*\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c9345c1-41c0-489d-ba2f-c9671783c998",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCzArF7fbicBJuEFSob",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38b368ee-9188-4e1f-a120-5ddb9b90ab67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QY7svHLB2WBQDYZHgxZ9mH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 72079,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 100,
          "cache_read_input_tokens": 72079,
          "cache_creation_input_tokens": 154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 154,
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

_source line 35 · 2026-05-20T04:41:54.641Z_

<details><summary>↩ Tool result · `toolu_01U17HXKfr8XHEuJMnx4WmQw`</summary>

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
/home/ubuntu/agent-ml-research/core/tools/visual_check.py
/home/ubuntu/agent-ml-research/core/tools/provenance.py
/home/ubuntu/agent-ml-research/core/tools/result.py
/home/ubuntu/agent-ml-research/core/tools/dream_card.py
/home/ubuntu/agent-ml-research/core/tools/constraints.py
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/core/tools/ssh.py
/home/ubuntu/agent-ml-research/core/tools/risk.py
/home/ubuntu/agent-ml-research/core/tools/disk_monitor.py
/home/ubuntu/agent-ml-research/core/tools/cron.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38b368ee-9188-4e1f-a120-5ddb9b90ab67",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "de2c00c2-f5c8-4f32-ae6b-328a399396cd",
  "sourceToolAssistantUUID": "38b368ee-9188-4e1f-a120-5ddb9b90ab67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T04:41:55.819Z_

Let me check if `add_to_literature_map` is in the tool_registry:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de2c00c2-f5c8-4f32-ae6b-328a399396cd",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCzHS7xAVZ4TMgnHyG2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f15f66d0-a919-439a-bacf-54cf92287620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TBEJePRGeVNt9nCChvJWgc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 72233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 730,
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

_source line 37 · 2026-05-20T04:41:56.072Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N1Ybo2HgrU7BxHNXKNk7bh`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tool_registry.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f15f66d0-a919-439a-bacf-54cf92287620",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCzHS7xAVZ4TMgnHyG2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6877dc1-1a2a-4683-942d-25f11177d509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TBEJePRGeVNt9nCChvJWgc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 72233,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 91,
          "cache_read_input_tokens": 72233,
          "cache_creation_input_tokens": 730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 730,
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

_source line 38 · 2026-05-20T04:41:56.447Z_

<details><summary>↩ Tool result · `toolu_01N1Ybo2HgrU7BxHNXKNk7bh`</summary>

```text
1	"""Unified role-tool registry — single source of truth for which tools each agent role can access.
2	
3	Instead of scattering tool whitelists across mcp_server.py, session_server.py,
4	and session_claude_md.py, all role definitions live here.
5	
6	Usage:
7	    from core.tool_registry import get_tools_for_role, ROLES, TOOL_GROUPS, resolve_tool_groups
8	
9	    tools = get_tools_for_role("agent")             # whitelist for Agent (34 tools)
10	    tools = get_tools_for_role("director")          # whitelist for Director
11	    excluded = get_excluded_tools("worker")          # blacklist for Worker
12	    expanded = resolve_tool_groups(["ssh", "wandb"]) # expand groups for spawn_worker
13	"""
14	
15	from __future__ import annotations
16	
17	from dataclasses import dataclass, field
18	
19	
20	@dataclass(frozen=True)
21	class RoleDef:
22	    """Definition of an agent role and its tool access."""
23	    name: str
24	    label: str
25	    phase: str                              # idea | research | review | study
26	    mode: str                               # whitelist | blacklist
27	    tools: frozenset[str] = frozenset()     # whitelist (mode=whitelist) or blacklist (mode=blacklist)
28	    env_var: str = ""                       # MCP server env var (e.g. "DIRECTOR_MODE")
29	    description: str = ""
30	
31	
32	# ---------------------------------------------------------------------------
33	# Tool sets — defined once, referenced by role definitions
34	# ---------------------------------------------------------------------------
35	
36	_DIRECTOR_TOOLS = frozenset({
37	    # Inter-role messaging
38	    "director_post_to_main_agent",
39	    "director_post_to_paper_agent",
40	    "director_post_to_manager",
41	    "director_reply_to_user",
42	    "keepalive_respond",
43	    "ralph_respond",
44	    "director_get_project_overview",
45	    "get_project_status",
46	    "get_agent_queue_status",
47	    "cancel_pending_director_messages",
48	    "cancel_agent_queue_item",
49	    "replace_agent_queue",
50	    "urgent_agent_message",
51	    # Approval
52	    "approve_experiment",
53	    "reject_experiment",
54	    "post_to_reviewer",
55	    # Infrastructure
56	    "get_resource_inventory",
57	    "update_project_config",
58	    # Phase transitions
59	    "request_study_approval",
60	    "submit_paper_to_review",
61	    # Visual review gate — Director must compile/preview before submit_paper_to_review
62	    "paper_compile_and_check",
63	    "pdf_to_images",
64	    "cleanup_pdf_images",
65	    # Cross-round review issue tracker — Research Director flips
66	    # open → in_progress / in_progress → resolved after Action Matrix.
67	    "update_review_issues",
68	    # Cross-phase Director communication
69	    "research_director_post_to_study_director",
70	    # Workspace management (needed when no project is bound)
71	    "list_projects",
72	    "list_workspace_projects",
73	    "load_project_config",
74	    "update_project_config",
75	    "create_project",
76	    # Secrets vault — Director manages secrets + approves usage
77	    "store_secret",
78	    "delete_secret",
79	    "list_secrets",
80	    "approve_secret_request",
81	    "reject_secret_request",
82	    # Utility
83	    "read_local_file",
84	    "upgrade_to_dual_group",
85	    "get_resource_inventory",
86	    # Feishu — context recovery after session reset
87	    "feishu_read_chat_history",
88	    "feishu_upload_file",
89	    # TUM — API key management (Gemini/OpenAI etc.)
90	    "get_tum_config",
91	    "feishu_send_tum_key_request_card",
92	    "feishu_read_tum_pending_key",
93	    # Resource management — Director controls infrastructure & spend.
94	    # Phase 12: AutoDL/elastic-GPU rental moved fully to Manager — Director
95	    # asks for cloud GPU via director_post_to_manager and waits for the
96	    # Manager-driven approval card. Director never sees autodl_* tools.
97	    "director_allocate_gpus",
98	    "list_available_gpus",
99	    "register_server",
100	    "remove_server",
101	    "list_ssh_hosts",
102	    "check_credentials",
103	    # Roadmap — Director owns the research roadmap
104	    "update_roadmap",
105	    "read_roadmap",
106	    "log_decision",
107	    # Mistake Notebook — Director records and reviews lessons learned
108	    "log_mistake",
109	    "read_mistakes",
110	    # Constraints — Director manages active hard constraints
111	    "add_constraint",
112	    "remove_constraint",
113	    "list_constraints",
114	    # Knowledge — unified read
115	    "read_project_file",
116	    # Provenance — Director can check impact and trigger provenance
117	    "impact_analysis",
118	    "auto_build_provenance",
119	    "check_provenance_completeness",
120	    "check_paper_consistency",
121	    # Experiment Matrix — Director plans paper targets
122	    "update_matrix",
123	    "read_matrix",
124	    "get_matrix_value",
125	    "sync_matrix_status",
126	    "matrix_gap_analysis",
127	    # Experiment Plan — Director owns paper_framing.md + experiment_plan.yaml,
128	    # consults coverage matrix to decide what experiments to run next.
129	    "read_experiment_plan_with_status",
130	    "compute_coverage_matrix",
131	    # Dream Tool — async future-experiment simulator (Director-only entry).
132	    # Post-MVP forced once + on-demand for major decisions (see DREAM_AGENT_DESIGN §8).
133	    "dream_simulate",
134	    "get_dream_status",
135	    "should_skip_dream",
136	    "get_dream_trend",
137	    # Skill management — Director maintains cross-project knowledge (e.g. ml-experiment-guide)
138	    "update_skill",
139	    # Project lifecycle
140	    "archive_project",
141	    # Image management — Director queries image info for user guidance
142	    "get_image_info",
143	    # MVP — Director designs and approves MVP, then transitions to research
144	    "complete_mvp",
145	    # GPU monitoring (cached, from gpu_monitor_daemon)
146	    "get_gpu_health",
147	    "get_project_resource_usage",
148	    # S3 backup
149	    "backup_project_to_s3",
150	    "list_s3_backups",
151	
152	    # Paper distillation — domain knowledge extraction
153	    "distill_papers",
154	    "get_distill_status",
155	})
156	
157	_AGENT_TOOLS = frozenset({
158	    # ── 实验生命周期 ──
159	    "read_registry",              # 读实验状态（最高频）
160	    "update_registry",            # 更新状态/指标/结论
161	    "submit_on_allocated",        # 提交已分配 GPU 的实验
162	    "submit_training_job",        # 直接提交训练
163	    "allocate_and_submit",        # 原子化 GPU 分配+提交
164	    "register_cron",              # 注册实验监控
165	    "poll_cron",                  # 手动检查实验状态
166	    "reconcile_crons",            # session 启动时同步所有 cron
167	    "check_job_status",           # 查进程是否存活（高频纯查询）
168	    "tail_training_logs",         # 读日志尾部（高频只读，心跳检查和浅层诊断必用）
169	    "fetch_wandb_metrics",        # 查 W&B 指标（registry 无指标时 fallback）
170	    "kill_job",                   # 终止 job
171	
172	    # ── Worker 调度 ──
173	    "spawn_worker",               # 委派任务（核心）
174	    "get_worker_status",          # 读 Worker 结果
175	    "list_workers",               # 查看活跃 Worker
176	    "approve_worker",             # 审批高风险 Worker
177	    "cancel_worker",              # 取消 Worker
178	
179	    # ── 通信 ──
180	    "main_agent_post_to_director",  # 向 Director 汇报
181	    "feishu_send_message",          # 飞书文字通知
182	    "feishu_send_result_card",      # 实验结果卡片（cron 回调必用）
183	    "feishu_send_approval_card",    # 请求审批
184	    "get_tum_config",                    # TUM 服务地址
185	    "feishu_send_tum_key_request_card",  # TUM key 申请
186	    "feishu_read_tum_pending_key",      # 读取用户提交的 key
187	    "feishu_send_alert",                # 健康检查告警通知
188	    "send_progress",                # 进度条更新
189	
190	    # ── 知识管理 ──
191	    "read_project_file",          # 统一读取项目文件（替代 read_memory + read_architecture）
192	    "save_project_file",          # 统一写入项目文件（当前仅 memory.md）
193	    "read_roadmap",               # 读研究路线图（只读）
194	    "read_mistakes",              # 读错题本（只读，审批/执行前回顾）
195	    "list_constraints",           # 读活跃约束（只读）
196	    "append_idea",                # 追加实验想法
197	    "register_artifact",          # 注册产出物
198	    "list_artifacts",             # 查看已注册产出物
199	    "pdf_to_images",              # PDF 转图片（视觉检查论文）
200	    "cleanup_pdf_images",         # 清理 PDF 转图片的临时文件
201	    "verify_references",          # LaTeX 引用交叉检查 + OpenAlex 验证
202	    "update_baseline",            # 更新 baseline
203	    "get_baseline_metrics",       # 读 baseline 指标
204	
205	    # ── 项目配置 ──
206	    "load_project_config",        # 读项目配置
207	    "list_available_gpus",        # 查 GPU 可用情况
208	
209	    # ── GPU 监控 ──
210	    "get_gpu_health",             # 全局 GPU 健康度（缓存）
211	    "get_project_resource_usage", # 项目级资源使用（分配 vs 实际）
212	
213	    # ── 镜像管理 ──
214	    "get_image_info",             # 查镜像信息
215	    "detect_image",               # 检测服务器镜像
216	
217	    # ── 密钥 ──
218	    "request_secret",             # 申请密钥（需审批）
219	    "poll_secret_request",        # 轮询密钥审批结果
220	
221	    # ── 论文溯源 ──
222	    "write_paper_section",        # 写论文章节（含 provenance）
223	    "edit_paper_section",         # 编辑论文章节（含 provenance）
224	    "impact_analysis",            # 变更影响分析
225	    "auto_build_provenance",      # 自动构建溯源
226	    "check_provenance_completeness",  # 检查溯源覆盖率
227	    "check_paper_consistency",    # 跨章节一致性（数字 / cite / notation）
228	
229	    # ── 实验矩阵 ──
230	    "update_matrix",              # 创建/更新论文目标 + cells
231	    "read_matrix",                # 读矩阵（支持过滤、summary）
232	    "get_matrix_value",           # 从 registry 拉数字（按 cell 映射）
233	    "sync_matrix_status",         # 从 registry 状态同步 cell 状态
234	    "matrix_gap_analysis",        # 缺口分析
235	
236	    # ── 实验计划（experiment_plan.yaml）──
237	    # Agent 只读：理解 plan 对应的 claim 是什么，以便提交 submit_training_job 时
238	    # 关联 plan_id。Plan 本身由 Director 维护，Agent 不写。
239	    "read_experiment_plan_with_status",
240	    "compute_coverage_matrix",
241	
242	    # ── S3 备份 ──
243	    "backup_project_to_s3",
244	    "list_s3_backups",
245	
246	    # ── 论文蒸馏 ──
247	    "distill_papers",
248	    "get_distill_status",
249	})
250	
251	
252	# ---------------------------------------------------------------------------
253	# Tool Groups — Agent delegates capabilities to Workers by group name
254	# ---------------------------------------------------------------------------
255	
256	TOOL_GROUPS: dict[str, list[str]] = {
257	    "ssh":       ["ssh_execute", "ssh_read_only", "kill_job", "detect_image"],
258	    "wandb":     ["fetch_wandb_metrics", "get_best_wandb_run",
259	                  "fetch_wandb_run_history", "compare_wandb_runs", "list_wandb_runs"],
260	    # Phase 12 §6: AutoDL tools moved to Manager — no autodl_* tools live
261	    # on BE anymore. The "autodl" group is preserved as an empty list so
262	    # spawn_worker callers that pass tool_groups=["autodl"] resolve to a
263	    # no-op rather than KeyError; new code should ask Manager directly.
264	    "autodl":    [],
265	    "git":       ["clone_repo", "sync_code_to_remote", "search_repo",
266	                  "list_repo_tree", "read_repo_file"],
267	    "knowledge": ["read_project_file", "save_project_file",
268	                  "append_idea"],
269	    "registry":  ["read_registry", "update_registry", "register_artifact"],
270	    "matrix":    ["read_matrix", "update_matrix", "get_matrix_value",
271	                  "sync_matrix_status", "matrix_gap_analysis"],
272	    "feishu":    ["feishu_create_doc", "feishu_upload_file", "feishu_fetch_doc"],
273	}
274	
275	
276	def resolve_tool_groups(
277	    tool_groups: list[str] | None = None,
278	    tools: list[str] | None = None,
279	) -> list[str]:
280	    """Expand tool group names into a flat, deduplicated tool list.
281	
282	    Args:
283	        tool_groups: Group names to expand (e.g. ["ssh", "wandb"]).
284	        tools:       Individual tool names to include as-is.
285	
286	    Returns:
287	        Sorted, deduplicated list of tool names.
288	
289	    Raises:
290	        ValueError: If an unknown group name is provided.
291	    """
292	    result: set[str] = set()
293	    if tool_groups:
294	        for group in tool_groups:
295	            if group not in TOOL_GROUPS:
296	                raise ValueError(
297	                    f"Unknown tool group '{group}'. "
298	                    f"Available groups: {sorted(TOOL_GROUPS.keys())}"
299	                )
300	            result.update(TOOL_GROUPS[group])
301	    if tools:
302	        result.update(tools)
303	    return sorted(result)
304	
305	_WORKER_EXCLUDED = frozenset({
306	    # All inter-role messaging
307	    "main_agent_post_to_director",
308	    "director_post_to_main_agent",
309	    "director_post_to_paper_agent",
310	    "director_post_to_manager",
311	    "post_to_reviewer",
312	    "reviewer_post_to_director",
313	    "review_reviewer_post_to_director",
314	    "director_post_to_reviewer",
315	    "submit_review_report_to_research_director",
316	    "study_director_post_to_study_agent",
317	    "study_agent_post_to_study_director",
318	    "post_to_study_reviewer",
319	    "study_reviewer_post_to_study_director",
320	    "submit_paper_to_review",
321	    "request_study_approval",
322	    "update_study_status",
323	    "update_claim_status",
324	    # Director-only
325	    "get_project_status",
326	    "update_project_config",
327	    "approve_experiment",
328	    "reject_experiment",
329	    "director_get_project_overview",
330	    "move_idea",
331	    "refine_idea",
332	    # Worker lifecycle (no recursive spawning)
333	    "spawn_worker",
334	    "approve_worker",
335	    "cancel_worker",
336	    # Feishu approval (Agent-level only)
337	    "feishu_send_approval_card",
338	    # Resource management
339	    "director_allocate_gpus",
340	    "allocate_and_submit",
341	    "register_server",
342	    "remove_server",
343	    # Phase 12 deleted these MCP tools — entries left here would be no-ops
344	    # (you can't blacklist what doesn't exist) but listing them as a
345	    # tombstone helps future searches understand "no, Worker can't
346	    # accidentally rent cloud GPUs by sneaking in via tool_groups".
347	    # Skill management — Worker cannot modify skills
348	    "update_skill",
349	    "create_skill",
350	    "delete_skill",
351	    # Secrets — Worker cannot access secrets at all
352	    "store_secret",
353	    "delete_secret",
354	    "request_secret",
355	    "poll_secret_request",
356	    "list_secrets",
357	    "approve_secret_request",
358	    "reject_secret_request",
359	})
360	
361	_REVIEWER_TOOLS = frozenset({
362	    "read_registry",
363	    "ssh_read_only",
364	    "tail_training_logs",
365	    "fetch_wandb_metrics",
366	    "read_project_file",
367	    "read_roadmap",
368	    "list_constraints",
369	    "reviewer_post_to_director",
370	    "pdf_to_images",
371	    "cleanup_pdf_images",
372	    # 确定性 LaTeX 源码检查（reviewer 可用于审查论文排版质量）
373	    "check_figures_and_layout",
374	    # GPU monitoring (cached, read-only)
375	    "get_gpu_health",
376	    "get_project_resource_usage",
377	    # Experiment matrix (read-only — review coverage)
378	    "read_matrix",
379	    # Experiment plan (read-only — Reviewer cross-checks claims vs experiments)
380	    "read_experiment_plan_with_status",
381	    "compute_coverage_matrix",
382	})
383	
384	# Paper Agent — Research-phase writing coordinator (see prompts/roles/paper-agent.md).
385	# Strictly serial pipeline: delegates writing/plotting/literature search to Workers,
386	# does Outline / consistency / provenance / refinement orchestration itself.
387	# Deliberately NOT included: submit_*, allocate_*, update_registry, register_cron
388	# (Paper Agent does not run experiments), impact_analysis (Director-only),
389	# feishu_send_approval_card (Paper Agent does not approve experiments).
390	_PAPER_AGENT_TOOLS = frozenset({
391	    # ── 写作核心 + 溯源 ──
392	    "write_paper_section",          # 写章节 + 自动构建 provenance
393	    "edit_paper_section",           # 增量编辑 + provenance 更新
394	    "verify_references",            # 引用 LaTeX 交叉检查 + OpenAlex 验证
395	    "check_provenance_completeness",
396	    "check_paper_consistency",      # Step 4 全局一致性检查（数字 / cite / notation）
397	    "auto_build_provenance",
398	    "bootstrap_provenance",
399	
400	    # ── Worker 调度（仅 spawn + 状态查询，不审批/取消高风险 Worker）──
401	    "spawn_worker",
402	    "get_worker_status",
403	    "list_workers",
404	
405	    # ── 知识读写（实验数据只读，论文文件可读可写）──
406	    "read_registry",                # 只读实验数据
407	    "read_project_file",
408	    "save_project_file",
409	    "read_roadmap",
410	    "register_artifact",
411	    "list_artifacts",
412	    # 实验计划 — Paper Agent 写论文时按 plan 中的 claim/framing_ref 串联实验数据
413	    "read_experiment_plan_with_status",
414	    "compute_coverage_matrix",
415	
416	    # ── PDF / 视觉检查 ──
417	    "pdf_to_images",
418	    "cleanup_pdf_images",
419	    # 自动 PDF 编译 + 页数/warning 检查（PAPER_WRITING_AGENT_PLAN task 3-3）
420	    "paper_compile_and_check",
421	    # 确定性 LaTeX 源码检查（figure/caption/label/placeholder/draft artifact）
422	    "check_figures_and_layout",
423	
424	    # ── Overleaf 双向同步（PAPER_WRITING_AGENT_PLAN task 3-2）──
425	    # init: 首次绑定 Overleaf git remote
426	    # push: 推送本地编辑到 Overleaf
427	    # pull: 拉取协作者在 Overleaf 上的编辑
428	    # sync: pull→push 一站式双向同步（最常用入口）
429	    # status: 只读 — 报告 ahead/behind/dirty
430	    "overleaf_init",
431	    "overleaf_push",
432	    "overleaf_pull",
433	    "overleaf_sync",
434	    "overleaf_status",
435	
436	    # ── 通信（Paper Agent ↔ Director / Reviewer）──
437	    "paper_agent_post_to_director",
438	    "paper_agent_request_review",
439	
440	    # ── 项目配置 ──
441	    "load_project_config",
442	
443	    # ── 镜像/图片 ──
444	    "get_image_info",
445	
446	    # ── 进度上报（B 群运维群可见）──
447	    "send_progress",
448	})
449	
450	_IDEA_REVIEWER_TOOLS = frozenset({
451	    "refine_idea",
452	    "generate_ideas",
453	    "submit_idea_review",
454	    "list_pending_ideas",          # Query idea details for context in follow-up conversations
455	    "list_projects",               # Know what projects exist for context
456	})
457	
458	# Agent without project: workspace management + idea brainstorming only.
459	# No SSH, registry, cron, worker, artifact — those need a project.
460	_NO_PROJECT_AGENT_TOOLS = frozenset({
461	    # Workspace management
462	    "list_projects",
463	    "list_workspace_projects",
464	    "load_project_config",
465	    "create_project",
466	    "switch_project",
467	    # Idea tools
468	    "append_idea",
469	    "generate_ideas",
470	    # Knowledge (read-only, for cross-project reference)
471	    "read_project_file",
472	    # Communication
473	    "send_progress",
474	    # Resource visibility (read-only)
475	    "list_ssh_hosts",
476	    "check_credentials",
477	    "list_available_gpus",
478	})
479	
480	_REVIEW_DIRECTOR_TOOLS = frozenset({
481	    "director_post_to_reviewer",
482	    "submit_review_report_to_research_director",
483	    "request_study_approval",
484	    "director_get_project_overview",
485	    "read_local_file",
486	    "read_project_file",
487	    # Cross-round issue tracker — Review Director records new/recurring
488	    # findings after Step 4 report synthesis.  Reads via read_local_file.
489	    "update_review_issues",
490	    # External review (paperreview.ai)
491	    "request_external_review",
492	    "get_external_review_status",
493	    # Visual layout check (non-scoring, parallel with reviewers)
494	    "dispatch_visual_check",
495	    "get_visual_check_status",
496	})
497	
498	# Dream Review Director — same base, but write to dream_reports only.
499	# Skip the cross-round issue tracker (Dream is one-shot, no continuity),
500	# skip external review (too slow for Dream), skip Study approval (no Study
501	# phase trigger), and swap submission tool for the Dream-specific one that
502	# delivers the report straight back to Dream Tool, no 5-step protocol.
503	# See DREAM_AGENT_DESIGN.md §6.4.
504	_DREAM_REVIEW_DIRECTOR_TOOLS = frozenset({
505	    "director_post_to_reviewer",
506	    "submit_dream_review_report",
507	    "director_get_project_overview",
508	    "read_local_file",
509	    "read_project_file",
510	})
511	
512	_REVIEW_REVIEWER_TOOLS = frozenset({
513	    "review_reviewer_post_to_director",
514	    # 审稿只看投稿材料 (PDF + 补充材料), 不能看 Research 阶段内部产出。
515	    # 不给 read_local_file / ssh_read_only / read_project_file:
516	    # read_project_file 的白名单恰好就是 Reviewer 不该看的研究内部文件
517	    # (memory.md / report.md / ROADMAP.md / decisions / ideas /
518	    # paper_provenance / ARCHITECTURE.md 等), 给了等于自动泄漏。
519	    # 论文 PDF 通过 pdf_to_images(path) 直接读, 路径由 CLAUDE.md 的
520	    # ## 投稿材料 section 显式列出 (build_session_prompt 从 project
521	    # config 的 review_paper_path 加载, 锁定本轮论文)。
522	    "pdf_to_images",
523	    "cleanup_pdf_images",
524	    "verify_references",
525	})
526	
527	# Dream Review Reviewer — identical tool surface to the normal Review
528	# Reviewer (a reviewer just needs to read the PDF and respond). The
529	# difference is purely session-key isolation + a Dream-mode dispatch
530	# message from the Dream Review Director. Kept as its own constant so
531	# future tweaks (e.g. dropping verify_references) don't bleed into the
532	# real-review path.
533	_DREAM_REVIEW_REVIEWER_TOOLS = _REVIEW_REVIEWER_TOOLS
534	
535	_STUDY_DIRECTOR_TOOLS = frozenset({
536	    "study_director_post_to_study_agent",
537	    "study_director_post_to_research_director",
538	    "post_to_study_reviewer",
539	    "update_study_status",
540	    "update_verification_item_status",
541	    "get_verification_package_status",
542	    "director_get_project_overview",
543	    "read_local_file",
544	    "read_project_file",
545	    "spawn_worker",
546	    "get_worker_status",
547	    "list_workers",
548	})
549	
550	_STUDY_AGENT_TOOLS = frozenset({
551	    "study_agent_post_to_study_director",
552	    "update_study_status",
553	    "assemble_verification_part",
554	    "write_verification_part",
555	    "run_verifier",
556	    "read_local_file",
557	    "write_local_file",
558	    "read_registry",
559	    "read_project_file",
560	    "ssh_read_only",
561	    "pdf_to_images",
562	    "cleanup_pdf_images",
563	    "write_narrative_scene",
564	    "render_and_send_narrative",
565	})
566	
567	_STUDY_REVIEWER_TOOLS = frozenset({
568	    "study_reviewer_post_to_study_director",
569	    "get_verification_package_status",
570	    "read_local_file",
571	    "read_project_file",
572	    "ssh_read_only",
573	    "pdf_to_images",
574	    "cleanup_pdf_images",
575	})
576	
577	# Briefer — visitor/read-only role for non-official groups & DMs that
578	# /p into a project. No writes, no approvals, no experiment actions.
579	# Unlike Director/Reviewer, briefer's plain-text output is surfaced to
580	# the user (no silent-reply contract). See _send_to_briefer.
581	_BRIEFER_TOOLS = frozenset({
582	    # Project state (read-only)
583	    "read_registry",
584	    "read_project_file",
585	    "read_roadmap",
586	    "load_project_config",
587	    "list_projects",
588	    "list_workspace_projects",
589	    "list_artifacts",
590	    # Experiment queries
591	    "check_job_status",
592	    "tail_training_logs",
593	    "fetch_wandb_metrics",
594	    "get_best_wandb_run",
595	    "fetch_wandb_run_history",
596	    "compare_wandb_runs",
597	    "list_wandb_runs",
598	    # Provenance / baseline (read-only)
599	    "check_provenance_completeness",
600	    "check_paper_consistency",
601	    "impact_analysis",
602	    "get_baseline_metrics",
603	    # Experiment matrix (read-only)
604	    "read_matrix",
605	    # Experiment plan (read-only — Briefer reports on plan coverage)
606	    "read_experiment_plan_with_status",
607	    "compute_coverage_matrix",
608	    # Status queries
609	    "get_project_status",
610	    "get_agent_queue_status",
611	    "get_worker_status",
612	    "list_workers",
613	    "list_available_gpus",
614	    # Idea queries (no write, no gen)
615	    "list_pending_ideas",
616	    # Resource visibility (read-only).
617	    # Phase 12 §6: cloud-GPU read tools (autodl_check_balance / availability /
618	    # list_instances) moved to Manager — Briefer can no longer surface
619	    # cross-tenant cloud spend from the BE side; for that visibility users
620	    # talk to Manager Agent directly.
621	    "list_ssh_hosts",
622	    "check_credentials",
623	    # Image info
624	    "get_image_info",
625	    # Paper / references
626	    "verify_references",
627	    "pdf_to_images",
628	    "cleanup_pdf_images",
629	})
630	
631	# Distiller Agent: minimal toolset for paper analysis + skill file writing.
632	# Runs as a one-shot system session, not user-facing.
633	_DISTILLER_TOOLS = frozenset({
634	    "read_project_file",
635	    "save_project_file",
636	    "load_project_config",
637	    "read_local_file",
638	})
639	
640	# Paper audit: one-shot subprocesses dispatched by `/paper-audit` and
641	# `dispatch_visual_check` (Review phase). Each phase runs a separate Claude
642	# subprocess with a narrow whitelist — keeps the audit focused and prevents
643	# leaked parent-process MODE env vars (e.g. REVIEW_DIRECTOR_MODE inherited via
644	# `**os.environ`) from accidentally selecting the wrong role's tools.
645	_PAPER_AUDIT_VISUAL_TOOLS = frozenset({
646	    "pdf_to_images",
647	    "cleanup_pdf_images",
648	})
649	_PAPER_AUDIT_REVIEW_VISUAL_TOOLS = _PAPER_AUDIT_VISUAL_TOOLS
650	_PAPER_AUDIT_CONTENT_TOOLS = frozenset({
651	    "read_project_file",
652	    "load_project_config",
653	})
654	
655	# ---------------------------------------------------------------------------
656	# Role definitions — the single source of truth
657	# ---------------------------------------------------------------------------
658	
659	ROLES: dict[str, RoleDef] = {
660	    # ── Research phase ──
661	    "director": RoleDef(
662	        name="director", label="Research Director", phase="research",
663	        mode="whitelist", tools=_DIRECTOR_TOOLS,
664	        env_var="DIRECTOR_MODE",
665	        description="PI 角色：方向决策、资源管理、审批实验",
666	    ),
667	    "director_no_project": RoleDef(
668	        name="director_no_project", label="Director (Idea Phase)", phase="idea",
669	        mode="whitelist", tools=_DIRECTOR_TOOLS,
670	        env_var="DIRECTOR_MODE",
671	        description="立项前 Director：讨论方向、创建项目",
672	    ),
673	    "agent": RoleDef(
674	        name="agent", label="Main Agent", phase="research",
675	        mode="whitelist", tools=_AGENT_TOOLS,
676	        env_var="",  # default mode
677	        description="执行层：协调实验、调度 Worker、维护 registry",
678	    ),
679	    "reviewer": RoleDef(
680	        name="reviewer", label="Research Reviewer", phase="research",
681	        mode="whitelist", tools=_REVIEWER_TOOLS,
682	        env_var="REVIEWER_MODE",
683	        description="只读审查：科学性核查、实验评审",
684	    ),
685	    "paper_agent": RoleDef(
686	        name="paper_agent", label="Paper Agent", phase="research",
687	        mode="whitelist", tools=_PAPER_AGENT_TOOLS,
688	        env_var="PAPER_AGENT_MODE",
689	        description="论文写作协调者：Outline / 图表 / 文献 / 章节 / 迭代修改的串行编排",
690	    ),
691	    "worker": RoleDef(
692	        name="worker", label="Worker", phase="research",
693	        mode="blacklist", tools=_WORKER_EXCLUDED,
694	        env_var="",  # dynamic via WORKER_TOOLS
695	        description="短命任务：SSH/分析/写代码，由 Main Agent 派遣",
696	    ),
697	    # ── Idea phase ──
698	    "no_project": RoleDef(
699	        name="no_project", label="Agent (Idea Phase)", phase="idea",
700	        mode="whitelist", tools=_NO_PROJECT_AGENT_TOOLS,
701	        env_var="NO_PROJECT_MODE",
702	        description="无项目 Agent：workspace 管理、idea brainstorm",
703	    ),
704	    "idea_reviewer": RoleDef(
705	        name="idea_reviewer", label="Idea Reviewer", phase="idea",
706	        mode="whitelist", tools=_IDEA_REVIEWER_TOOLS,
707	        env_var="IDEA_REVIEWER_MODE",
708	        description="Idea 评审：评估研究方向可行性",
709	    ),
710	    # ── Review phase ──
711	    "review_director": RoleDef(
712	        name="review_director", label="Review Director", phase="review",
713	        mode="whitelist", tools=_REVIEW_DIRECTOR_TOOLS,
714	        env_var="REVIEW_DIRECTOR_MODE",
715	        description="审稿流程编排：安排一审二审、汇总报告、投递给 Research Director",
716	    ),
717	    "review_reviewer": RoleDef(
718	        name="review_reviewer", label="Review Reviewer", phase="review",
719	        mode="whitelist", tools=_REVIEW_REVIEWER_TOOLS,
720	        env_var="REVIEW_REVIEWER_MODE",
721	        description="圆桌 Reviewer：按 Director 分配的侧重点审稿",
722	    ),
723	    # Dream-mode counterparts — separate role definitions so MCP whitelists
724	    # and prompt builders can vary even though the underlying behaviour
725	    # (roundtable / per-reviewer focus) is shared.
726	    "dream_review_director": RoleDef(
727	        name="dream_review_director", label="Dream Review Director", phase="review",
728	        mode="whitelist", tools=_DREAM_REVIEW_DIRECTOR_TOOLS,
729	        env_var="DREAM_REVIEW_DIRECTOR_MODE",
730	        description="Dream 模拟论文审稿编排：精简工具集，报告直接回传给 Dream Tool",
731	    ),
732	    "dream_review_reviewer": RoleDef(
733	        name="dream_review_reviewer", label="Dream Review Reviewer", phase="review",
734	        mode="whitelist", tools=_DREAM_REVIEW_REVIEWER_TOOLS,
735	        env_var="DREAM_REVIEW_REVIEWER_MODE",
736	        description="Dream 圆桌 Reviewer：独立 session，按 Dream Review Director 分配的侧重点审稿",
737	    ),
738	    # ── Study phase ──
739	    "study_director": RoleDef(
740	        name="study_director", label="Study Director", phase="study",
741	        mode="whitelist", tools=_STUDY_DIRECTOR_TOOLS,
742	        env_var="STUDY_DIRECTOR_MODE",
743	        description="学习流程编排、验证协调",
744	    ),
745	    "study_agent": RoleDef(
746	        name="study_agent", label="Study Agent", phase="study",
747	        mode="whitelist", tools=_STUDY_AGENT_TOOLS,
748	        env_var="STUDY_AGENT_MODE",
749	        description="生成学习资料包、组装验证内容",
750	    ),
751	    "study_reviewer": RoleDef(
752	        name="study_reviewer", label="Study Reviewer", phase="study",
753	        mode="whitelist", tools=_STUDY_REVIEWER_TOOLS,
754	        env_var="STUDY_REVIEWER_MODE",
755	        description="审核学习资料包质量",
756	    ),
757	    # ── Visitor (any phase) ──
758	    "briefer": RoleDef(
759	        name="briefer", label="Briefer (Visitor/Read-Only)", phase="any",
760	        mode="whitelist", tools=_BRIEFER_TOOLS,
761	        env_var="BRIEFER_MODE",
762	        description="访客只读模式：非官方群/DM 查询项目状态，不可执行副作用",
763	    ),
764	    # ── System (one-shot) ──
765	    "distiller": RoleDef(
766	        name="distiller", label="Distiller Agent", phase="research",
767	        mode="whitelist", tools=_DISTILLER_TOOLS,
768	        env_var="DISTILLER_MODE",
769	        description="论文蒸馏引擎：从文献提取领域知识，生成项目专属 skill",
770	    ),
771	    "paper_audit_visual": RoleDef(
772	        name="paper_audit_visual", label="Paper Audit (Visual)", phase="any",
773	        mode="whitelist", tools=_PAPER_AUDIT_VISUAL_TOOLS,
774	        env_var="PAPER_AUDIT_VISUAL_MODE",
775	        description="/paper-audit 视觉排版审计子进程：PDF 渲染 + 排版检查",
776	    ),
777	    "paper_audit_review_visual": RoleDef(
778	        name="paper_audit_review_visual", label="Paper Audit (Review Visual)", phase="review",
779	        mode="whitelist", tools=_PAPER_AUDIT_REVIEW_VISUAL_TOOLS,
780	        env_var="PAPER_AUDIT_REVIEW_VISUAL_MODE",
781	        description="Review 阶段视觉审查子进程：与 /paper-audit visual 工具集相同",
782	    ),
783	    "paper_audit_content": RoleDef(
784	        name="paper_audit_content", label="Paper Audit (Content)", phase="any",
785	        mode="whitelist", tools=_PAPER_AUDIT_CONTENT_TOOLS,
786	        env_var="PAPER_AUDIT_CONTENT_MODE",
787	        description="/paper-audit 内容审计子进程：叙事一致性 / 结构检查",
788	    ),
789	}
790	
791	
792	# ---------------------------------------------------------------------------
793	# Public API
794	# ---------------------------------------------------------------------------
795	
796	def get_tools_for_role(role: str) -> frozenset[str]:
797	    """Return the tool set for a role (whitelist roles only).
798	
799	    Supports dynamic reviewer roles: review_reviewer_N falls back to
800	    the generic ``review_reviewer`` definition. Dream-mode reviewer roles
801	    (``dream_review_reviewer_N``) similarly fall back to
802	    ``dream_review_reviewer``.
803	    """
804	    role_def = ROLES.get(role)
805	    # Dynamic fallback: review_reviewer_3 → review_reviewer,
806	    # dream_review_reviewer_2 → dream_review_reviewer.
807	    if not role_def and role.startswith("dream_review_reviewer_") and role[len("dream_review_reviewer_"):].isdigit():
808	        role_def = ROLES.get("dream_review_reviewer")
809	    elif not role_def and role.startswith("review_reviewer_") and role[16:].isdigit():
810	        role_def = ROLES.get("review_reviewer")
811	    if not role_def or role_def.mode != "whitelist":
812	        return frozenset()
813	    return role_def.tools
814	
815	
816	def get_excluded_tools(role: str) -> frozenset[str]:
817	    """Return tools to exclude for a role (blacklist roles only)."""
818	    role_def = ROLES.get(role)
819	    if not role_def or role_def.mode != "blacklist":
820	        return frozenset()
821	    return role_def.tools
822	
823	
824	def get_env_var(role: str) -> str:
825	    """Return the MCP env var name for a role (empty for default mode)."""
826	    role_def = ROLES.get(role)
827	    return role_def.env_var if role_def else ""
828	
829	
830	# ---------------------------------------------------------------------------
831	# SAFE_MODE built-in tool allowlist
832	# ---------------------------------------------------------------------------
833	
834	# Read-only Claude built-in tools safe to auto-approve in SAFE_MODE.
835	# Bash / Write / Edit / MultiEdit / NotebookEdit are intentionally excluded —
836	# SAFE_MODE exists specifically to gate those behind human approval.
837	_SAFE_MODE_BUILTINS: frozenset[str] = frozenset({
838	    "Read", "Glob", "Grep", "WebSearch", "WebFetch", "TodoWrite",
839	})
840	
841	
842	def get_safe_mode_builtin_tools(role: str) -> list[str]:  # noqa: ARG001
843	    """Return Claude built-in tools auto-approved in SAFE_MODE for any role.
844	
845	    All roles share the same conservative set — read-only + web research only.
846	    Bash / Write / Edit are never included regardless of role.
847	    """
848	    return sorted(_SAFE_MODE_BUILTINS)
849	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6877dc1-1a2a-4683-942d-25f11177d509",
  "isSidechain": true,
  "promptId": "ae3afa2e-8668-42ff-a25e-a990d8a33cbc",
  "agentId": "a7eceb99bbc693860",
  "type": "user",
  "uuid": "e47cb2c5-2341-42c6-857c-392719f00bb5",
  "sourceToolAssistantUUID": "d6877dc1-1a2a-4683-942d-25f11177d509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T04:42:16.241Z_

Perfect! Now I have a comprehensive understanding. Let me create a summary document with the findings:

## Summary

Based on my thorough search of the codebase, here are the findings:

### 1. **Expected YAML Structure for literature_map.yaml**

The literature_map.yaml follows this structure (defined in `/home/ubuntu/agent-ml-research/core/tools/literature.py`):

```yaml
meta:
  last_updated: &lt;ISO timestamp>
  total_papers: &lt;count>

categories:
  - key: &lt;category_slug>        # e.g. "attention_mechanisms"
    name: &lt;display_name>         # e.g. "Attention Mechanisms"
    narrative: &lt;description>     # one-line narrative arc

papers:
  &lt;bibtex_key>:                  # e.g. "vaswani2017attention"
    title: &lt;string>
    authors: [&lt;list of strings>] # e.g. ["Vaswani, A.", "Shazeer, N."]
    year: &lt;int or null>
    venue: &lt;string>              # e.g. "NeurIPS", "ICML"
    url: &lt;string>
    doi: &lt;string>
    bibtex_key: &lt;string>         # auto-generated if missing
    category: &lt;string>           # must match categories[].key or empty
    role: &lt;string>               # one of: foundation, direct-competitor, method-component, evaluation, background
    relevance: &lt;string>          # free-form one-liner
    abstract: &lt;string>
    semantic_scholar_id: &lt;string>
    arxiv_id: &lt;string>
    verified: &lt;boolean>          # default False
    added_by: &lt;string>           # provenance: who added this (e.g. "paper-research", "idea_generator", "distiller", "user")
    added_at: &lt;ISO timestamp>
    source_idea_id: &lt;string>     # optional, global map only
```

**Key points:**
- The structure is **dict-based** with three top-level keys: `meta`, `categories`, `papers`
- `papers` values are dicts keyed by `bibtex_key`, not a flat list
- The system also supports a legacy list format: `{"papers": [...]}` which gets auto-converted to the dict structure
- All metadata fields are optional (system uses `dict.get()` with sensible defaults)
- Valid roles are: `foundation`, `direct-competitor`, `method-component`, `evaluation`, `background`
- The system auto-generates a `bibtex_key` if missing (format: `surname+year+firstword`, e.g. `vaswani2017attention`)

### 2. **Function: `add_to_literature_map` Exists**

Yes, `add_to_literature_map` is a fully implemented function (lines 392-494 in `/home/ubuntu/agent-ml-research/core/tools/literature.py`):

```python
def add_to_literature_map(
    project: str | None = None,
    papers: Iterable[dict] | None = None,
    added_by: str = "",
) -> ToolResult:
```

**Features:**
- Adds/merges papers into the literature_map
- Automatic dedup via DOI (exact match, normalized) → normalized title match
- Merges fields into existing entries (never overwrites, only fills empty slots)
- Auto-generates `bibtex_key` if missing
- Handles bibtex_key collisions with numeric suffixes (`key`, `key_2`, `key_3`, etc.)
- Validates `role` against `VALID_ROLES` frozenset
- Rejects papers with missing `title`
- Returns: `{"added": [keys], "merged": [keys], "rejected": [{title, reason}], "total_papers": N}`

**Recognized input fields:**
- `title`, `authors`, `year`, `venue`, `url`, `doi`, `bibtex_key`, `category`, `role`, `relevance`, `abstract`, `semantic_scholar_id`, `source_idea_id`, `verified`

### 3. **How `distill_papers` Counts Papers from literature_map**

Function: `_collect_from_literature_map()` (lines 145-179 in `/home/ubuntu/agent-ml-research/core/tools/distill.py`)

**Process:**
1. Reads `literature_map.yaml` using `_read_map()` which auto-converts list format to dict
2. Extracts `papers` field (dict): `lit_map.get("papers") or {}`
3. Handles both legacy list and dict formats:
   - **Dict format**: iterates over `papers.items()` directly
   - **List format** (legacy): converts to `{id or title or f"paper_{i}": entry}`
4. Creates `PaperForDistill` objects from each entry (lines 165-179)
5. Calls `_rank_and_trim()` (lines 295-330) which scores papers by:
   - Venue quality (top venues: NeurIPS, ICML, ICLR, etc. = +3.0)
   - Recency (within 2 years = +2.0)
   - Citation count (>50 = +2.0, >10 = +1.0)
   - Existing in literature_map (role set = +1.0, direct-competitor = +2.0)
6. Returns top N papers ranked by relevance score (default max 25 papers, configurable via `max_papers`)

**Collection layers** (if literature_map is empty):
1. **Layer 1**: literature_map (curated)
2. **Layer 2**: Semantic Scholar keyword search (project description keywords)
3. **Layer 3**: S2 recommendations (seed from Layer 1 paper IDs)
4. **Layer 4**: Citation graph (references of high-relevance papers)

### 4. **Is `add_to_literature_map` Exposed as an MCP Tool?**

**NO** — `add_to_literature_map` is NOT exposed as an MCP tool in the current codebase.

**What IS exposed:**
- `distill_papers` (MCP tool at line 2899 in `/home/ubuntu/agent-ml-research/core/mcp_server.py`)
- `get_distill_status` (MCP tool at line 2917 in `mcp_server.py`)

**Why not exposed:**
- `add_to_literature_map` is a pure Python function in `core.tools.literature` module
- It's NOT decorated with `@mcp.tool()` in `mcp_server.py`
- Not listed in any role's tool whitelist in `/home/ubuntu/agent-ml-research/core/tool_registry.py`

**How it's currently used internally:**
- Called by `_collect_from_literature_map()` in distill.py (line 641)
- Called by `_backfill_literature_map()` in distill.py (line 663)
- Called by tests in `/home/ubuntu/agent-ml-research/tests/test_literature_map.py`
- Called by `seed_literature_map()` function (line 639) which wraps it

### 5. **Alternative: `seed_literature_map` Function**

There is a public function `seed_literature_map()` (lines 606-641) that wraps `add_to_literature_map`:

```python
def seed_literature_map(
    project: str,
    seed_papers: Iterable[dict],
    source_idea_id: str = "",
) -> ToolResult:
```

Used during idea→project bootstrap to bulk-seed papers from global idea map to project map.

---

**Files involved:**
- `/home/ubuntu/agent-ml-research/core/tools/literature.py` — core CRUD + dedup logic
- `/home/ubuntu/agent-ml-research/core/tools/distill.py` — paper collection + ranking
- `/home/ubuntu/agent-ml-research/core/mcp_server.py` — MCP exposure
- `/home/ubuntu/agent-ml-research/core/tool_registry.py` — role-based tool whitelisting
- `/home/ubuntu/agent-ml-research/tests/test_literature_map.py` — comprehensive test coverage showing all usage patterns

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e47cb2c5-2341-42c6-857c-392719f00bb5",
  "isSidechain": true,
  "agentId": "a7eceb99bbc693860",
  "requestId": "req_011CbDCzRVJoiNiXZMvRRxf1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f71fe2bc-24e7-4f51-aeda-352f3f8508dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "34d21c8b-30c6-4d2d-af7e-4249ae70ee7b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "cached-percolating-seahorse",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017qeGj1zsJQ14KmUVZAoJhk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 12369,
      "cache_read_input_tokens": 72963,
      "output_tokens": 2021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12369
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 2021,
          "cache_read_input_tokens": 72963,
          "cache_creation_input_tokens": 12369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12369,
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
