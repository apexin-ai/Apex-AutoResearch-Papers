# Research conversation: I need to find the expected YAML schema for experiment_plan.yaml used by two Python functions: `read_experiment_plan_wit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a687669e02e1c82a7.jsonl`
- **Structured JSON:** [`d13b4eee9b861ebb4aca.json`](../../sessions/d1/d13b4eee9b861ebb4aca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-13T15:38:44.682Z_

I need to find the expected YAML schema for experiment_plan.yaml used by two Python functions: `read_experiment_plan_with_status` and `compute_coverage_matrix`. These tools are defined in the agent-ml-research MCP server codebase.

Search in /home/ubuntu/agent-ml-research/ for:
1. The implementation of `read_experiment_plan_with_status` — what YAML keys does it parse? What's the expected top-level structure?
2. The implementation of `compute_coverage_matrix` — same question.
3. Any example experiment_plan.yaml files in the codebase.

The current YAML has top-level keys `claims:` (dict) and `experiments:` (list of plan entries). Each plan entry has: plan_id, name, claim, description, priority, depends_on, registry_id, notes. The tools return empty results, so one or more field names don't match.

Report: the exact expected YAML structure (key names, nesting) so I can fix the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "584b3e78-0919-456b-a9bc-11ea3f6cb999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-13T15:38:47.049Z_

I'll search the agent-ml-research codebase to find the expected YAML schema for experiment_plan.yaml.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "584b3e78-0919-456b-a9bc-11ea3f6cb999",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpQxgjD5WKHbm3GSK1u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "48247bb6-4623-408f-8ba6-ae4d7e1c2227",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DVmzgFygsbfmfb6xWD1iCd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34626,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34626,
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

_source line 3 · 2026-05-13T15:38:47.155Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MKNU2ez3xEoX9PoufQeFCm`</summary>

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
  "parentUuid": "48247bb6-4623-408f-8ba6-ae4d7e1c2227",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpQxgjD5WKHbm3GSK1u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "789dab0c-0e50-4308-8c2f-49413cb285ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DVmzgFygsbfmfb6xWD1iCd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34626,
      "cache_read_input_tokens": 0,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 34626
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 34626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 34626,
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

_source line 4 · 2026-05-13T15:38:47.319Z_

<details><summary>↩ Tool result · `toolu_01MKNU2ez3xEoX9PoufQeFCm`</summary>

```text
/home/ubuntu/agent-ml-research/scripts/smoke_test.py
/home/ubuntu/agent-ml-research/scripts/feishu_chat.py
/home/ubuntu/agent-ml-research/scripts/instance_monitor.py
/home/ubuntu/agent-ml-research/scripts/evaluation/gen_review_html.py
/home/ubuntu/agent-ml-research/scripts/migrate_experiments_to_projects.py
/home/ubuntu/agent-ml-research/scripts/migrate_v2_layout.py
/home/ubuntu/agent-ml-research/scripts/migrate_registry.py
/home/ubuntu/agent-ml-research/scripts/migrate_workspace.py
/home/ubuntu/agent-ml-research/scripts/split_active_workspaces.py
/home/ubuntu/agent-ml-research/scripts/resample_split2_neg5.py
/home/ubuntu/agent-ml-research/scripts/simulate_user.py
/home/ubuntu/agent-ml-research/scripts/compare_weight_methods.py
/home/ubuntu/agent-ml-research/.venv/bin/pdf2txt.py
/home/ubuntu/agent-ml-research/.venv/bin/dumppdf.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/aiohappyeyeballs/impl.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/aiohappyeyeballs/_staggered.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__init__.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/aiohappyeyeballs/types.py
/home/ubuntu/agent-ml-research/.venv/lib/python3.14/site-packages/annotated_doc/main.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "789dab0c-0e50-4308-8c2f-49413cb285ba",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "42276b24-4a4f-4384-8f8c-32a251df8ce7",
  "sourceToolAssistantUUID": "789dab0c-0e50-4308-8c2f-49413cb285ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-13T15:38:48.921Z_

Now let me search for the implementation of these two functions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42276b24-4a4f-4384-8f8c-32a251df8ce7",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpR9oxUcJPTrtSPUUoP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5e302ff-c9bd-4963-9433-7896f49d35d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SMy3bTaKDmRdHUydK4LB8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 34626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1464,
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

_source line 6 · 2026-05-13T15:38:49.386Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NWAsar54XfCByV7s9xN2M3`</summary>

```json
{
  "pattern": "def read_experiment_plan_with_status",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5e302ff-c9bd-4963-9433-7896f49d35d5",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpR9oxUcJPTrtSPUUoP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "70d636d0-8f40-4e2b-b5f3-6a6890698cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SMy3bTaKDmRdHUydK4LB8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 34626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1464,
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

_source line 7 · 2026-05-13T15:38:49.445Z_

<details><summary>↩ Tool result · `toolu_01NWAsar54XfCByV7s9xN2M3`</summary>

```text
Found 3 files
/home/ubuntu/agent-ml-research/docs/plans/dream/DREAM_AGENT_DESIGN.md
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/tools/experiment_plan.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70d636d0-8f40-4e2b-b5f3-6a6890698cb8",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "aff5580a-cf15-4cec-b07f-5e876de14cdf",
  "sourceToolAssistantUUID": "70d636d0-8f40-4e2b-b5f3-6a6890698cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T15:38:49.506Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BUSjCPRrirtPwsXMmufknc`</summary>

```json
{
  "pattern": "def compute_coverage_matrix",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aff5580a-cf15-4cec-b07f-5e876de14cdf",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpR9oxUcJPTrtSPUUoP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b052e75d-96de-4ed9-9fd5-505ef1602aa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SMy3bTaKDmRdHUydK4LB8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 34626,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1464
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 166,
          "cache_read_input_tokens": 34626,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1464,
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

_source line 9 · 2026-05-13T15:38:49.558Z_

<details><summary>↩ Tool result · `toolu_01BUSjCPRrirtPwsXMmufknc`</summary>

```text
Found 3 files
/home/ubuntu/agent-ml-research/docs/plans/dream/DREAM_AGENT_DESIGN.md
/home/ubuntu/agent-ml-research/core/mcp_server.py
/home/ubuntu/agent-ml-research/core/tools/experiment_plan.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b052e75d-96de-4ed9-9fd5-505ef1602aa5",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "40fc160e-dab6-453e-9aba-34714b4c2c22",
  "sourceToolAssistantUUID": "b052e75d-96de-4ed9-9fd5-505ef1602aa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-13T15:38:51.067Z_

Let me read the experiment_plan.py file which likely contains both functions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40fc160e-dab6-453e-9aba-34714b4c2c22",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRKNRmN4p2FkdNgzma",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f60cfe0f-91c7-4068-abe7-ca7de0ca1c18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BM5LwhgrLsXBHYdvSh65Ro",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 36090,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 89,
          "cache_read_input_tokens": 36090,
          "cache_creation_input_tokens": 374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 374,
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

### Tool call

_source line 11 · 2026-05-13T15:38:51.127Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tca5igGQxbw7HRHF3edd5g`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/experiment_plan.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f60cfe0f-91c7-4068-abe7-ca7de0ca1c18",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRKNRmN4p2FkdNgzma",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa4717d7-1538-458f-b111-9bc5ff9ebbdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BM5LwhgrLsXBHYdvSh65Ro",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 374,
      "cache_read_input_tokens": 36090,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 374
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 89,
          "cache_read_input_tokens": 36090,
          "cache_creation_input_tokens": 374,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 374,
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

_source line 12 · 2026-05-13T15:38:51.137Z_

<details><summary>↩ Tool result · `toolu_01Tca5igGQxbw7HRHF3edd5g`</summary>

```text
1	"""Experiment Plan — Director-authored research roadmap.
2	
3	The plan file (``projects/{project}/experiment_plan.yaml``) is the
4	authoritative list of experiments that the project will need to write the
5	target paper. Each plan entry holds **planning intent only** — the claim
6	it supports, priority, dependencies, GPU budget, description. It does
7	**not** store experiment status.
8	
9	Status comes from the registry. Plan entries link to registry entries via
10	the optional ``registry_id`` field:
11	
12	  • ``registry_id`` present + matches a registry entry → status / metrics
13	    / conclusion are read from the registry on every call.
14	  • ``registry_id`` present but registry entry missing → ``status =
15	    "orphaned"`` (registry was rebuilt / experiment was deleted by hand).
16	  • ``registry_id`` absent → implicit ``status = "planned"``.
17	
18	The "selection C" rationale (see ``docs/plans/DREAM_AGENT_DESIGN.md``) is
19	that storing status in two places creates a synchronization problem. This
20	module eliminates it by always deriving live status from the registry.
21	
22	Companion view: ``compute_coverage_matrix()`` aggregates plan entries by
23	``claim`` so Director / Dream Tool can see "for each Core Claim, what
24	experiments are planned / running / done / blocked." The matrix is
25	recomputed on demand — nothing is persisted.
26	
27	Concurrent writers (e.g. ``writeback_registry_id`` called from
28	``submit_training_job``) hold an exclusive flock on a sidecar ``.lock``
29	file and use atomic temp-and-rename, matching the patterns in
30	``literature.py`` and ``paper_checklist.py``.
31	"""
32	
33	from __future__ import annotations
34	
35	import fcntl
36	import logging
37	import os
38	import tempfile
39	from pathlib import Path
40	from typing import Any
41	
42	import yaml
43	
44	from core import paths as _paths
45	from core.tools.result import ToolResult
46	
47	logger = logging.getLogger(__name__)
48	
49	
50	PLAN_FILENAME = "experiment_plan.yaml"
51	
52	# Statuses returned by read_experiment_plan_with_status() for entries whose
53	# registry_id is absent or stale. Registry statuses (PENDING/RUNNING/DONE/...)
54	# are passed through unchanged.
55	STATUS_PLANNED = "planned"
56	STATUS_ORPHANED = "orphaned"
57	
58	# Statuses that count as "done with usable data" for coverage purposes.
59	_COVERAGE_FILLED = frozenset({"DONE"})
60	
61	# Coverage rollup buckets (returned in the matrix summary).
62	_COVERAGE_BUCKETS = ("planned", "running", "done", "failed", "orphaned")
63	
64	
65	# ---------------------------------------------------------------------------
66	# Path resolution
67	# ---------------------------------------------------------------------------
68	
69	def get_experiment_plan_path(project: str) -> Path:
70	    """Resolve the per-project experiment_plan.yaml path."""
71	    if not project:
72	        raise ValueError("project is required")
73	    p = _paths.resolve_project_file(project, PLAN_FILENAME)
74	    p.parent.mkdir(parents=True, exist_ok=True)
75	    return p
76	
77	
78	# ---------------------------------------------------------------------------
79	# Atomic I/O
80	# ---------------------------------------------------------------------------
81	
82	def _empty_plan() -> dict:
83	    return {"experiments": []}
84	
85	
86	def _read_raw(path: Path) -> dict:
87	    """Load and lightly normalise the plan file.
88	
89	    Malformed entries (missing ``id``) are dropped silently — the file may
90	    have been hand-edited. The caller (read_experiment_plan_with_status)
91	    decides how strict to be.
92	    """
93	    if not path.exists():
94	        return _empty_plan()
95	    try:
96	        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
97	    except Exception:
98	        logger.warning("Failed to parse experiment_plan at %s", path, exc_info=True)
99	        return _empty_plan()
100	    if not isinstance(data, dict):
101	        return _empty_plan()
102	    experiments = data.get("experiments")
103	    if not isinstance(experiments, list):
104	        experiments = []
105	    clean: list[dict] = []
106	    for e in experiments:
107	        if isinstance(e, dict) and e.get("id"):
108	            clean.append(e)
109	    return {"experiments": clean}
110	
111	
112	def _read_modify_write(path: Path, modifier) -> dict:
113	    path.parent.mkdir(parents=True, exist_ok=True)
114	    lock_path = path.with_suffix(".lock")
115	    with open(lock_path, "a+") as lock_f:
116	        fcntl.flock(lock_f, fcntl.LOCK_EX)
117	        try:
118	            data = _read_raw(path)
119	            modifier(data)
120	
121	            fd, tmp_path = tempfile.mkstemp(
122	                dir=str(path.parent), prefix=".plan_", suffix=".tmp",
123	            )
124	            try:
125	                with os.fdopen(fd, "w", encoding="utf-8") as tmp_f:
126	                    yaml.dump(
127	                        data, tmp_f,
128	                        default_flow_style=False, allow_unicode=True, sort_keys=False,
129	                    )
130	                    tmp_f.flush()
131	                    os.fsync(tmp_f.fileno())
132	                os.replace(tmp_path, str(path))
133	            except Exception:
134	                if os.path.exists(tmp_path):
135	                    os.unlink(tmp_path)
136	                raise
137	        finally:
138	            fcntl.flock(lock_f, fcntl.LOCK_UN)
139	    return data
140	
141	
142	# ---------------------------------------------------------------------------
143	# Registry join — runs on every read so plan/registry never drift
144	# ---------------------------------------------------------------------------
145	
146	def _load_registry_experiments(project: str) -> dict[str, dict]:
147	    """Read the registry once and return the {exp_id: entry} map.
148	
149	    Imported lazily to avoid pulling registry dependencies into modules
150	    that only need plan reads (e.g. session prompts).
151	    """
152	    try:
153	        from core.tools.registry import get_registry_path
154	        reg_path = get_registry_path(project)
155	    except Exception:
156	        return {}
157	    if not reg_path.exists():
158	        return {}
159	    try:
160	        data = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
161	    except Exception:
162	        logger.warning("Failed to parse registry at %s", reg_path, exc_info=True)
163	        return {}
164	    experiments = data.get("experiments")
165	    if not isinstance(experiments, dict):
166	        return {}
167	    return experiments
168	
169	
170	def _attach_status(entry: dict, registry: dict[str, dict]) -> dict:
171	    """Return a copy of ``entry`` with status / conclusion / metrics from registry.
172	
173	    Never mutates the input. The returned dict is what callers display —
174	    on-disk YAML stays untouched.
175	    """
176	    merged = dict(entry)
177	    reg_id = entry.get("registry_id")
178	    if reg_id:
179	        reg_exp = registry.get(reg_id)
180	        if reg_exp:
181	            merged["status"] = reg_exp.get("status", STATUS_ORPHANED)
182	            if "conclusion" in reg_exp:
183	                merged["conclusion"] = reg_exp.get("conclusion")
184	            if "metrics" in reg_exp:
185	                merged["metrics"] = reg_exp.get("metrics")
186	        else:
187	            merged["status"] = STATUS_ORPHANED
188	    else:
189	        merged["status"] = STATUS_PLANNED
190	    return merged
191	
192	
193	def read_experiment_plan_with_status(project: str) -> ToolResult:
194	    """Read the plan and overlay live status from the registry.
195	
196	    Returns:
197	        ToolResult.data = {
198	            "experiments": [
199	                {"id": "plan_001", "name": "...", "claim": "Claim 1",
200	                 "registry_id": "exp_001", "status": "RUNNING",
201	                 "metrics": {...}, "conclusion": "success", ...},
202	                ...
203	            ],
204	            "total": N,
205	        }
206	
207	    Status is one of:
208	        - "planned"  — no registry_id
209	        - "orphaned" — registry_id set but registry entry missing
210	        - any registry status (PREPARING/PENDING/QUEUED/ALLOCATED/RUNNING/
211	          ANALYZING/DONE/DEPLOYING/DEPLOYED)
212	    """
213	    if not project:
214	        return ToolResult(success=False, error="project is required")
215	
216	    plan = _read_raw(get_experiment_plan_path(project))
217	    registry = _load_registry_experiments(project)
218	
219	    merged = [_attach_status(e, registry) for e in plan.get("experiments", [])]
220	    return ToolResult(
221	        success=True,
222	        data={"experiments": merged, "total": len(merged)},
223	    )
224	
225	
226	# ---------------------------------------------------------------------------
227	# Coverage matrix — derived view, not persisted
228	# ---------------------------------------------------------------------------
229	
230	def _coverage_bucket(status: str, conclusion: str | None = None) -> str:
231	    """Map a (status, conclusion) pair to a coverage bucket."""
232	    if status == STATUS_PLANNED:
233	        return "planned"
234	    if status == STATUS_ORPHANED:
235	        return "orphaned"
236	    if status == "DONE":
237	        if conclusion == "success":
238	            return "done"
239	        if conclusion in ("failed", "killed", "negative"):
240	            return "failed"
241	        return "done"  # unknown conclusion — count as done so it isn't pending
242	    # PREPARING / PENDING / QUEUED / ALLOCATED / RUNNING / ANALYZING / DEPLOY*
243	    return "running"
244	
245	
246	def _empty_bucket_counts() -> dict[str, int]:
247	    return {b: 0 for b in _COVERAGE_BUCKETS}
248	
249	
250	def compute_coverage_matrix(project: str) -> ToolResult:
251	    """Group plan entries by ``claim`` and report coverage per claim.
252	
253	    Coverage = experiments whose ``status == DONE`` (regardless of
254	    conclusion), divided by total experiments in that claim. Claims with
255	    zero experiments report ``coverage_pct = 0.0``.
256	
257	    Returns:
258	        ToolResult.data = {
259	            "claims": ["Claim 1", "Claim 2", ...],
260	            "matrix": {
261	                "Claim 1": {
262	                    "experiments": [{...}, {...}],
263	                    "counts": {"planned": 2, "running": 1, "done": 3, ...},
264	                    "total": 6,
265	                    "coverage": "3/6",
266	                    "coverage_pct": 50.0,
267	                },
268	                ...
269	            },
270	            "unassigned": [{...}],   # entries without a `claim` field
271	            "summary": {
272	                "total_experiments": N,
273	                "total_claims": M,
274	                "counts": {"planned": ..., "running": ..., "done": ...},
275	                "coverage": "K/N",
276	                "coverage_pct": ...,
277	            },
278	        }
279	
280	    The ``unassigned`` list lets Director see which plan entries still
281	    need a claim attached — important for keeping the matrix honest.
282	    """
283	    plan_res = read_experiment_plan_with_status(project)
284	    if not plan_res.success:
285	        return plan_res
286	
287	    entries: list[dict] = plan_res.data.get("experiments", []) or []
288	
289	    by_claim: dict[str, list[dict]] = {}
290	    unassigned: list[dict] = []
291	    for e in entries:
292	        claim = e.get("claim")
293	        if claim:
294	            by_claim.setdefault(claim, []).append(e)
295	        else:
296	            unassigned.append(e)
297	
298	    matrix: dict[str, dict] = {}
299	    overall_counts = _empty_bucket_counts()
300	
301	    for claim, exps in by_claim.items():
302	        counts = _empty_bucket_counts()
303	        for e in exps:
304	            bucket = _coverage_bucket(e.get("status", STATUS_PLANNED), e.get("conclusion"))
305	            counts[bucket] += 1
306	            overall_counts[bucket] += 1
307	        total = len(exps)
308	        done = counts["done"]
309	        matrix[claim] = {
310	            "experiments": exps,
311	            "counts": counts,
312	            "total": total,
313	            "coverage": f"{done}/{total}" if total else "0/0",
314	            "coverage_pct": round(100.0 * done / total, 1) if total else 0.0,
315	        }
316	
317	    for e in unassigned:
318	        bucket = _coverage_bucket(e.get("status", STATUS_PLANNED), e.get("conclusion"))
319	        overall_counts[bucket] += 1
320	
321	    total_exps = len(entries)
322	    total_done = overall_counts["done"]
323	
324	    return ToolResult(success=True, data={
325	        "claims": sorted(by_claim.keys()),
326	        "matrix": matrix,
327	        "unassigned": unassigned,
328	        "summary": {
329	            "total_experiments": total_exps,
330	            "total_claims": len(by_claim),
331	            "counts": overall_counts,
332	            "coverage": f"{total_done}/{total_exps}" if total_exps else "0/0",
333	            "coverage_pct": round(100.0 * total_done / total_exps, 1) if total_exps else 0.0,
334	            "unassigned": len(unassigned),
335	        },
336	    })
337	
338	
339	# ---------------------------------------------------------------------------
340	# Write-back from submit_training_job — keeps plan↔registry linkage fresh
341	# ---------------------------------------------------------------------------
342	
343	def writeback_registry_id(
344	    project: str,
345	    plan_id: str,
346	    registry_id: str,
347	) -> ToolResult:
348	    """Attach a freshly-minted ``registry_id`` to a plan entry.
349	
350	    Called from ``submit_training_job(plan_id=...)`` as a side-effect so
351	    that future ``read_experiment_plan_with_status()`` calls reflect the
352	    new linkage. No-op when the plan entry is missing — ad-hoc
353	    experiments don't need a plan attachment.
354	
355	    Returns:
356	        ToolResult.data = {
357	            "linked": bool,
358	            "plan_id": "plan_003",
359	            "registry_id": "exp_001",
360	        }
361	    """
362	    if not project:
363	        return ToolResult(success=False, error="project is required")
364	    if not plan_id or not registry_id:
365	        return ToolResult(
366	            success=False,
367	            error="plan_id and registry_id are required",
368	        )
369	
370	    hit = {"linked": False}
371	
372	    def _apply(data: dict) -> None:
373	        for e in data.get("experiments", []):
374	            if e.get("id") == plan_id:
375	                e["registry_id"] = registry_id
376	                hit["linked"] = True
377	                return
378	
379	    _read_modify_write(get_experiment_plan_path(project), _apply)
380	    return ToolResult(success=True, data={
381	        "linked": hit["linked"],
382	        "plan_id": plan_id,
383	        "registry_id": registry_id,
384	    })
385	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa4717d7-1538-458f-b111-9bc5ff9ebbdb",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "f22c04a4-1860-41be-8a9b-bf1c10e8c7db",
  "sourceToolAssistantUUID": "aa4717d7-1538-458f-b111-9bc5ff9ebbdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T15:38:52.708Z_

Perfect! Now let me search for example experiment_plan.yaml files in the codebase:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f22c04a4-1860-41be-8a9b-bf1c10e8c7db",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRSGQwuRE2p3ZxeRvF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "20a16e19-f051-4dd4-9941-bd62ff857148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PH6cYT7YRf1WmiKD7v9jUc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4599,
      "cache_read_input_tokens": 36464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4599,
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

_source line 14 · 2026-05-13T15:38:53.055Z_

<details open><summary>🔧 Tool call — Glob · `toolu_017ERbTTzhixVekMKh4BSGwU`</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20a16e19-f051-4dd4-9941-bd62ff857148",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRSGQwuRE2p3ZxeRvF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f4aefddc-a6e8-49bd-9c3b-6cfa373803c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PH6cYT7YRf1WmiKD7v9jUc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4599,
      "cache_read_input_tokens": 36464,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4599
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 105,
          "cache_read_input_tokens": 36464,
          "cache_creation_input_tokens": 4599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4599,
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

_source line 15 · 2026-05-13T15:38:53.175Z_

<details><summary>↩ Tool result · `toolu_017ERbTTzhixVekMKh4BSGwU`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4aefddc-a6e8-49bd-9c3b-6cfa373803c3",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "10435385-8aa9-4ba6-801f-f202a8ef311b",
  "sourceToolAssistantUUID": "f4aefddc-a6e8-49bd-9c3b-6cfa373803c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-13T15:38:55.101Z_

Let me check the projects directory structure to see if there are any sample files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10435385-8aa9-4ba6-801f-f202a8ef311b",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRas63q8yRBBbRCkq7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ed54f3f3-420e-4520-9c98-fbb7fb4bca23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DYKq1Kw6KEtqVinBYL3P7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 41063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 120,
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

_source line 17 · 2026-05-13T15:38:55.214Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DX6pXKpHRcdRG5cVUSsm2v`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -type d -name \"projects\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed54f3f3-420e-4520-9c98-fbb7fb4bca23",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRas63q8yRBBbRCkq7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d8220573-1a33-4398-bd76-8fc376d0dbc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DYKq1Kw6KEtqVinBYL3P7e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 41063,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 120
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 91,
          "cache_read_input_tokens": 41063,
          "cache_creation_input_tokens": 120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 120,
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

_source line 18 · 2026-05-13T15:38:55.412Z_

<details><summary>↩ Tool result · `toolu_01DX6pXKpHRcdRG5cVUSsm2v`</summary>

```text
/home/ubuntu/agent-ml-research/workspace/projects
/home/ubuntu/agent-ml-research/workspace/config/projects
/home/ubuntu/agent-ml-research/manager/projects
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8220573-1a33-4398-bd76-8fc376d0dbc9",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "8905d845-5628-469f-b048-44524478d3e7",
  "sourceToolAssistantUUID": "d8220573-1a33-4398-bd76-8fc376d0dbc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T15:38:57.828Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FobYHQZUcdPb6oXyxRwBi8`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/workspace/projects -name \"experiment_plan.yaml\" -o -name \"*experiment_plan*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8905d845-5628-469f-b048-44524478d3e7",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRkiAzTBxLRPd5pHSd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50472a39-e439-4fc3-96b5-d782c8772f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01V8VwfPt3p9dDKqsuhxQNxK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 252,
      "cache_read_input_tokens": 41183,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 252
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 95,
          "cache_read_input_tokens": 41183,
          "cache_creation_input_tokens": 252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 252,
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

_source line 20 · 2026-05-13T15:38:57.882Z_

<details><summary>↩ Tool result · `toolu_01FobYHQZUcdPb6oXyxRwBi8`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50472a39-e439-4fc3-96b5-d782c8772f01",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "fc3195ab-1526-4691-93a7-e583b863eef9",
  "sourceToolAssistantUUID": "50472a39-e439-4fc3-96b5-d782c8772f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T15:38:59.992Z_

Let me check the documentation and tests for examples:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc3195ab-1526-4691-93a7-e583b863eef9",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRvy4sgenckPpzxLzJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6d760201-62a9-4479-b2f7-690b6539442b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aqkQ3MGsnCkVy53XxvdDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 114,
      "cache_read_input_tokens": 41435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 114,
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

_source line 22 · 2026-05-13T15:39:00.323Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015ZhmrWPTY1SY2H6k5hkdPW`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -type f \\( -name \"*.md\" -o -name \"*test*.py\" \\) | xargs grep -l \"experiment_plan\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d760201-62a9-4479-b2f7-690b6539442b",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpRvy4sgenckPpzxLzJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8d5a57a4-a9c5-47d5-8f0b-3cfad48e7725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011aqkQ3MGsnCkVy53XxvdDs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 114,
      "cache_read_input_tokens": 41435,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 114
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 41435,
          "cache_creation_input_tokens": 114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 114,
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

_source line 23 · 2026-05-13T15:39:00.915Z_

<details><summary>↩ Tool result · `toolu_015ZhmrWPTY1SY2H6k5hkdPW`</summary>

```text
/home/ubuntu/agent-ml-research/docs/plans/dream/DREAM_FEEDBACK_ACTION_PROTOCOL.md
/home/ubuntu/agent-ml-research/docs/plans/dream/DREAM_AGENT_DESIGN.md
/home/ubuntu/agent-ml-research/TEST.md
/home/ubuntu/agent-ml-research/CLAUDE.md
/home/ubuntu/agent-ml-research/tests/test_dream_define_tiers.py
/home/ubuntu/agent-ml-research/tests/test_experiment_matrix_skill.py
/home/ubuntu/agent-ml-research/tests/test_dream_what_if.py
/home/ubuntu/agent-ml-research/tests/test_session_claude_md.py
/home/ubuntu/agent-ml-research/tests/test_dream_elaborate.py
/home/ubuntu/agent-ml-research/tests/test_experiment_plan.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d5a57a4-a9c5-47d5-8f0b-3cfad48e7725",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "2ed1e970-9ac3-4abb-b01c-b27807df5ccd",
  "sourceToolAssistantUUID": "8d5a57a4-a9c5-47d5-8f0b-3cfad48e7725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T15:39:02.234Z_

Excellent! Let me check the test file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ed1e970-9ac3-4abb-b01c-b27807df5ccd",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpS9wg2HxCMFcpQWBcQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf90c003-9d0b-4cce-9c1a-bae492a5ea8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XEjM19SLGQEtPVmVxEPyxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 41549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 350,
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

_source line 25 · 2026-05-13T15:39:02.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SUR8q2yQjqVFAStoFL88zm`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/tests/test_experiment_plan.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf90c003-9d0b-4cce-9c1a-bae492a5ea8f",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpS9wg2HxCMFcpQWBcQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b07fbbb3-6ec2-42b6-923d-69b8853935f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XEjM19SLGQEtPVmVxEPyxj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 350,
      "cache_read_input_tokens": 41549,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 350
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 83,
          "cache_read_input_tokens": 41549,
          "cache_creation_input_tokens": 350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 350,
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

_source line 26 · 2026-05-13T15:39:02.396Z_

<details><summary>↩ Tool result · `toolu_01SUR8q2yQjqVFAStoFL88zm`</summary>

```text
1	"""Tests for ``core/tools/experiment_plan.py``.
2	
3	Covers:
4	- ``read_experiment_plan_with_status()`` overlay logic — entries with /
5	  without ``registry_id``, stale ``registry_id`` (orphaned), missing
6	  registry file, missing plan file, malformed YAML.
7	- Status / conclusion / metrics propagation from registry.
8	- ``writeback_registry_id()`` side-effect plus its no-op behaviour when
9	  the plan entry is missing.
10	- Project isolation — two projects don't see each other's plan files.
11	"""
12	
13	from __future__ import annotations
14	
15	from pathlib import Path
16	
17	import pytest
18	import yaml
19	
20	from core import paths as _paths
21	from core.tools.experiment_plan import (
22	    PLAN_FILENAME,
23	    STATUS_ORPHANED,
24	    STATUS_PLANNED,
25	    get_experiment_plan_path,
26	    read_experiment_plan_with_status,
27	    writeback_registry_id,
28	)
29	
30	
31	def _seed_plan(project: str, experiments: list[dict]) -> Path:
32	    """Write a plan YAML for ``project`` and return its path."""
33	    p = get_experiment_plan_path(project)
34	    p.write_text(yaml.safe_dump({"experiments": experiments}, allow_unicode=True))
35	    return p
36	
37	
38	def _seed_registry(project: str, experiments: dict[str, dict]) -> Path:
39	    """Write a registry YAML for ``project`` and return its path."""
40	    from core.tools.registry import get_registry_path
41	    p = get_registry_path(project)
42	    p.write_text(yaml.safe_dump({"experiments": experiments, "baseline": None}))
43	    return p
44	
45	
46	# ---------------------------------------------------------------------------
47	# read_experiment_plan_with_status
48	# ---------------------------------------------------------------------------
49	
50	class TestReadWithStatus:
51	
52	    def test_empty_when_no_files(self, workspace):
53	        result = read_experiment_plan_with_status("proj_x")
54	        assert result.success
55	        assert result.data == {"experiments": [], "total": 0}
56	
57	    def test_planned_when_no_registry_id(self, workspace):
58	        _seed_plan("proj_x", [
59	            {"id": "plan_001", "name": "main", "claim": "Claim 1"},
60	            {"id": "plan_002", "name": "ablation", "claim": "Claim 2"},
61	        ])
62	        result = read_experiment_plan_with_status("proj_x")
63	        assert result.success
64	        exps = result.data["experiments"]
65	        assert {e["id"]: e["status"] for e in exps} == {
66	            "plan_001": STATUS_PLANNED,
67	            "plan_002": STATUS_PLANNED,
68	        }
69	        # Pure planning entries do not carry conclusion/metrics keys.
70	        assert "conclusion" not in exps[0]
71	        assert "metrics" not in exps[0]
72	
73	    def test_status_pulled_from_registry(self, workspace):
74	        _seed_plan("proj_x", [
75	            {"id": "plan_001", "registry_id": "exp_001", "claim": "C1"},
76	            {"id": "plan_002", "registry_id": "exp_002", "claim": "C2"},
77	        ])
78	        _seed_registry("proj_x", {
79	            "exp_001": {"status": "DONE", "conclusion": "success",
80	                        "metrics": {"acc": 0.91}},
81	            "exp_002": {"status": "RUNNING"},
82	        })
83	        result = read_experiment_plan_with_status("proj_x")
84	        assert result.success
85	        by_id = {e["id"]: e for e in result.data["experiments"]}
86	        assert by_id["plan_001"]["status"] == "DONE"
87	        assert by_id["plan_001"]["conclusion"] == "success"
88	        assert by_id["plan_001"]["metrics"] == {"acc": 0.91}
89	        assert by_id["plan_002"]["status"] == "RUNNING"
90	        # Running entry has no conclusion/metrics keys yet.
91	        assert "conclusion" not in by_id["plan_002"]
92	
93	    def test_registry_id_without_registry_entry_is_orphaned(self, workspace):
94	        _seed_plan("proj_x", [
95	            {"id": "plan_001", "registry_id": "exp_missing"},
96	        ])
97	        _seed_registry("proj_x", {})  # registry exists, but entry is gone
98	        result = read_experiment_plan_with_status("proj_x")
99	        assert result.data["experiments"][0]["status"] == STATUS_ORPHANED
100	
101	    def test_registry_id_without_registry_file_is_orphaned(self, workspace):
102	        """If registry.yaml is missing entirely, registry_id can't be resolved."""
103	        _seed_plan("proj_x", [
104	            {"id": "plan_001", "registry_id": "exp_001"},
105	            {"id": "plan_002"},
106	        ])
107	        # Do NOT seed registry — file truly missing.
108	        result = read_experiment_plan_with_status("proj_x")
109	        by_id = {e["id"]: e for e in result.data["experiments"]}
110	        assert by_id["plan_001"]["status"] == STATUS_ORPHANED
111	        assert by_id["plan_002"]["status"] == STATUS_PLANNED
112	
113	    def test_malformed_yaml_returns_empty(self, workspace):
114	        p = get_experiment_plan_path("proj_x")
115	        p.write_text(":::not a yaml mapping:::")
116	        result = read_experiment_plan_with_status("proj_x")
117	        assert result.success
118	        assert result.data["experiments"] == []
119	
120	    def test_missing_id_entries_dropped(self, workspace):
121	        _seed_plan("proj_x", [
122	            {"id": "plan_001", "name": "good"},
123	            {"name": "missing_id"},  # dropped
124	            {"id": "plan_002"},
125	        ])
126	        result = read_experiment_plan_with_status("proj_x")
127	        ids = [e["id"] for e in result.data["experiments"]]
128	        assert ids == ["plan_001", "plan_002"]
129	
130	    def test_project_isolation(self, workspace):
131	        _seed_plan("proj_a", [{"id": "plan_001"}])
132	        _seed_plan("proj_b", [{"id": "plan_999"}])
133	        a = read_experiment_plan_with_status("proj_a").data
134	        b = read_experiment_plan_with_status("proj_b").data
135	        assert [e["id"] for e in a["experiments"]] == ["plan_001"]
136	        assert [e["id"] for e in b["experiments"]] == ["plan_999"]
137	
138	    def test_project_required(self, workspace):
139	        r = read_experiment_plan_with_status("")
140	        assert not r.success
141	        assert "project" in (r.error or "").lower()
142	
143	
144	# ---------------------------------------------------------------------------
145	# writeback_registry_id
146	# ---------------------------------------------------------------------------
147	
148	class TestWriteback:
149	
150	    def test_links_existing_entry(self, workspace):
151	        _seed_plan("proj_x", [
152	            {"id": "plan_001", "name": "main", "claim": "Claim 1"},
153	        ])
154	        r = writeback_registry_id("proj_x", "plan_001", "exp_001")
155	        assert r.success
156	        assert r.data == {
157	            "linked": True, "plan_id": "plan_001", "registry_id": "exp_001",
158	        }
159	
160	        # File reflects the linkage now.
161	        on_disk = yaml.safe_load(get_experiment_plan_path("proj_x").read_text())
162	        assert on_disk["experiments"][0]["registry_id"] == "exp_001"
163	
164	    def test_unknown_plan_id_is_noop(self, workspace):
165	        _seed_plan("proj_x", [{"id": "plan_001"}])
166	        r = writeback_registry_id("proj_x", "plan_does_not_exist", "exp_001")
167	        assert r.success           # not an error — ad-hoc experiments are fine
168	        assert r.data["linked"] is False
169	        # File untouched.
170	        on_disk = yaml.safe_load(get_experiment_plan_path("proj_x").read_text())
171	        assert on_disk["experiments"][0].get("registry_id") is None
172	
173	    def test_missing_args_rejected(self, workspace):
174	        for args in [("", "plan", "exp"), ("p", "", "exp"), ("p", "plan", "")]:
175	            r = writeback_registry_id(*args)
176	            assert not r.success
177	
178	    def test_writeback_then_status_shows_registry(self, workspace):
179	        """End-to-end: writeback updates the file, and a subsequent
180	        read_experiment_plan_with_status() sees the live registry status.
181	        """
182	        _seed_plan("proj_x", [{"id": "plan_001"}])
183	        _seed_registry("proj_x", {
184	            "exp_007": {"status": "RUNNING"},
185	        })
186	        # Before linking — status is planned.
187	        before = read_experiment_plan_with_status("proj_x").data["experiments"][0]
188	        assert before["status"] == STATUS_PLANNED
189	
190	        writeback_registry_id("proj_x", "plan_001", "exp_007")
191	
192	        after = read_experiment_plan_with_status("proj_x").data["experiments"][0]
193	        assert after["status"] == "RUNNING"
194	        assert after["registry_id"] == "exp_007"
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b07fbbb3-6ec2-42b6-923d-69b8853935f0",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "92dccaa9-20ea-41ed-8253-b4a729960284",
  "sourceToolAssistantUUID": "b07fbbb3-6ec2-42b6-923d-69b8853935f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-13T15:39:04.201Z_

Perfect! Now let me check the DREAM_AGENT_DESIGN.md for any additional documentation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92dccaa9-20ea-41ed-8253-b4a729960284",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSGS6hPnrC8TBmEkFx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4dbe6c5b-fb85-436b-a382-401eb44da6fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PjLZybMgJ86aQoXLY9LNEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2855,
      "cache_read_input_tokens": 41899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2855,
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

_source line 28 · 2026-05-13T15:39:04.590Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GQEWkAf1yAnkKaTTxmSxdY`</summary>

```json
{
  "command": "grep -A 20 \"experiment_plan\" /home/ubuntu/agent-ml-research/docs/plans/dream/DREAM_AGENT_DESIGN.md | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dbe6c5b-fb85-436b-a382-401eb44da6fc",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSGS6hPnrC8TBmEkFx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9e14119d-dfc5-4dd0-8c4b-b601f6d47a2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PjLZybMgJ86aQoXLY9LNEP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2855,
      "cache_read_input_tokens": 41899,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2855
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 116,
          "cache_read_input_tokens": 41899,
          "cache_creation_input_tokens": 2855,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2855,
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

_source line 29 · 2026-05-13T15:39:04.652Z_

<details><summary>↩ Tool result · `toolu_01GQEWkAf1yAnkKaTTxmSxdY`</summary>

````text
- [x] 0-1 实现 `core/tools/experiment_plan.py`：`read_experiment_plan_with_status()` + `compute_coverage_matrix()`
- [x] 0-2 `core/mcp_server.py`：注册 `read_experiment_plan_with_status` + `compute_coverage_matrix`
- [x] 0-3 `core/tool_registry.py`：Director/Agent/Reviewer 角色添加新工具权限
- [x] 0-4 `core/session_claude_md.py`：Director/Agent/Reviewer 的按需查阅增加 `paper_framing.md` + `experiment_plan.yaml`
- [x] 0-5 `prompts/roles/director.md`：Post-MVP 第一步改为制定 framing + plan + dream
- [x] 0-6 ROADMAP 格式简化为 dashboard（引用 framing 和 plan）
- [x] 0-7 `core/tools/experiment_matrix.py`：移除 `_sync_matrix_for_experiment()` side-effect，改为按需计算
- [x] 0-8 `config/projects/{name}.yaml`：增加 dream 配置段 schema
- [x] 0-9 `core/paths.py`：增加 `dream_report_dir(project, dream_id)` 路径函数
- [x] 0-T1 测试：`test_experiment_plan.py` — `read_with_status()` 动态合并 registry 状态（有/无 registry_id）
- [x] 0-T2 测试：`test_coverage_matrix.py` — 覆盖率矩阵从 plan + framing 按需计算

### Phase 1: Writing Utilities + Paper Agent Dream 模式
- [x] 1-1 创建 `core/writing/` 目录：`types.py`（ExperimentData / CompiledPaper）
- [x] 1-2 实现 `core/writing/latex_compiler.py`：latexmk 编译
- [x] 1-3 实现 `core/writing/template_manager.py`：加载 venue 模板
- [x] 1-4 实现 `core/writing/table_generator.py`：实验数据 → LaTeX 表格
- [x] 1-5 `prompts/roles/paper-agent.md`：增加 Dream 模式支持（简化 pipeline，一次性 session）
- [x] 1-6 `core/session_server.py`：支持 `dream_{id}:paper_agent` session key
- [x] 1-7 `core/tools/feishu_group.py`：Dream Paper Agent B 群消息带 `[Dream]` 前缀 + 不路由到其他 agent
- [x] 1-T1 测试：类型序列化 — 覆盖在 `tests/test_writing_utilities.py::TestTypesRoundTrip`
- [x] 1-T2 测试：LaTeX 编译 — 覆盖在 `tests/test_writing_utilities.py::TestLatexCompiler*`（6 个 class，含 ArgValidation/EngineMissing/LogParsing/Finalize/EndToEndMocked）
- [x] 1-T3 测试：venue 模板加载 — 覆盖在 `tests/test_writing_utilities.py::TestTemplateDiscovery/TestTemplateLookup/TestTemplateCopy`
- [x] 1-T4 测试：实验数据 → LaTeX 表格 — 覆盖在 `tests/test_writing_utilities.py::TestRenderTable*` + `TestComparisonTable`
- [x] 1-T5 测试：Paper Agent Dream 模式 session 隔离 + 消息可见性 — 见 `tests/test_paper_agent_dream_session_isolation.py`
- [x] 1-T6 测试：Dream 工具可见性 — 由 prompt 段 (`paper-agent.md` Dream 模式) + `dream_id` 短路实现，覆盖在 `tests/test_paper_agent_dream_session_isolation.py` 及 `tests/test_paper_agent_dream_e2e.py`
- [x] 1-T7 测试：Dream Paper Agent 写入 `dream_reports/{id}/{tier}/paper.tex`，不写入 `projects/{project}/paper/` — 见 `tests/test_paper_agent_dream_e2e.py` (G2 output-path isolation)

### Phase 2: Dream Tool 核心（异步架构 + 两阶段想象）
- [x] 2-1 实现 `core/dream_types.py`：DreamInput / DreamHandle / DreamOutput / TierDefinitions / TierDefinition / ImaginedScenario / ImaginedExperiment（含 WhatIfExperiment + DreamScenarioResult）
--
### 2.2 新增文件：experiment_plan.yaml

**位置**：`projects/{project}/experiment_plan.yaml`

**内容**：所有规划中的实验——包括已完成的、进行中的、和计划做但还没提交的。

```yaml
# 注意：plan 中不存 status 字段（选项 C）。
# 有 registry_id 的实验，status 通过 read_experiment_plan_with_status() 从 registry 动态读取。
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e14119d-dfc5-4dd0-8c4b-b601f6d47a2f",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "01c7ec4a-3a1b-4051-bc22-174e9bb39431",
  "sourceToolAssistantUUID": "9e14119d-dfc5-4dd0-8c4b-b601f6d47a2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-13T15:39:06.212Z_

Let me get more of this documentation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01c7ec4a-3a1b-4051-bc22-174e9bb39431",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSRvrFdtNTPG2HniYX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "17868847-cd7e-4faf-b2bf-3e458e96314b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UY8DW82tPuE1UV3gjV941A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1593,
      "cache_read_input_tokens": 44754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1593,
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

_source line 31 · 2026-05-13T15:39:07.173Z_

<details open><summary>🔧 Tool call — Read · `toolu_014GjjXLCuFYT2qUN4Y8epbx`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/docs/plans/dream/DREAM_AGENT_DESIGN.md",
  "offset": 1,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17868847-cd7e-4faf-b2bf-3e458e96314b",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSRvrFdtNTPG2HniYX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59b2e01c-e70b-4fdb-96a5-fa5830a8b740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UY8DW82tPuE1UV3gjV941A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1593,
      "cache_read_input_tokens": 44754,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1593
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 122,
          "cache_read_input_tokens": 44754,
          "cache_creation_input_tokens": 1593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1593,
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

_source line 32 · 2026-05-13T15:39:07.188Z_

<details><summary>↩ Tool result · `toolu_014GjjXLCuFYT2qUN4Y8epbx`</summary>

````text
1	# Dream Agent 设计：正向模拟与即时反馈机制
2	
3	> 日期：2026-05-10
4	> 前置阅读：
5	> - [NeurIPS 2026 复盘](../research/NEURIPS_2026_RETROSPECTIVE.md) §2（反馈稀疏与 Agent 短视）
6	> - [Paper Writing Agent 方案](PAPER_WRITING_AGENT_PLAN.md)
7	
8	---
9	
10	## TODO
11	
12	### Phase 0: Paper Framing + Experiment Plan 基础设施
13	- [x] 0-1 实现 `core/tools/experiment_plan.py`：`read_experiment_plan_with_status()` + `compute_coverage_matrix()`
14	- [x] 0-2 `core/mcp_server.py`：注册 `read_experiment_plan_with_status` + `compute_coverage_matrix`
15	- [x] 0-3 `core/tool_registry.py`：Director/Agent/Reviewer 角色添加新工具权限
16	- [x] 0-4 `core/session_claude_md.py`：Director/Agent/Reviewer 的按需查阅增加 `paper_framing.md` + `experiment_plan.yaml`
17	- [x] 0-5 `prompts/roles/director.md`：Post-MVP 第一步改为制定 framing + plan + dream
18	- [x] 0-6 ROADMAP 格式简化为 dashboard（引用 framing 和 plan）
19	- [x] 0-7 `core/tools/experiment_matrix.py`：移除 `_sync_matrix_for_experiment()` side-effect，改为按需计算
20	- [x] 0-8 `config/projects/{name}.yaml`：增加 dream 配置段 schema
21	- [x] 0-9 `core/paths.py`：增加 `dream_report_dir(project, dream_id)` 路径函数
22	- [x] 0-T1 测试：`test_experiment_plan.py` — `read_with_status()` 动态合并 registry 状态（有/无 registry_id）
23	- [x] 0-T2 测试：`test_coverage_matrix.py` — 覆盖率矩阵从 plan + framing 按需计算
24	
25	### Phase 1: Writing Utilities + Paper Agent Dream 模式
26	- [x] 1-1 创建 `core/writing/` 目录：`types.py`（ExperimentData / CompiledPaper）
27	- [x] 1-2 实现 `core/writing/latex_compiler.py`：latexmk 编译
28	- [x] 1-3 实现 `core/writing/template_manager.py`：加载 venue 模板
29	- [x] 1-4 实现 `core/writing/table_generator.py`：实验数据 → LaTeX 表格
30	- [x] 1-5 `prompts/roles/paper-agent.md`：增加 Dream 模式支持（简化 pipeline，一次性 session）
31	- [x] 1-6 `core/session_server.py`：支持 `dream_{id}:paper_agent` session key
32	- [x] 1-7 `core/tools/feishu_group.py`：Dream Paper Agent B 群消息带 `[Dream]` 前缀 + 不路由到其他 agent
33	- [x] 1-T1 测试：类型序列化 — 覆盖在 `tests/test_writing_utilities.py::TestTypesRoundTrip`
34	- [x] 1-T2 测试：LaTeX 编译 — 覆盖在 `tests/test_writing_utilities.py::TestLatexCompiler*`（6 个 class，含 ArgValidation/EngineMissing/LogParsing/Finalize/EndToEndMocked）
35	- [x] 1-T3 测试：venue 模板加载 — 覆盖在 `tests/test_writing_utilities.py::TestTemplateDiscovery/TestTemplateLookup/TestTemplateCopy`
36	- [x] 1-T4 测试：实验数据 → LaTeX 表格 — 覆盖在 `tests/test_writing_utilities.py::TestRenderTable*` + `TestComparisonTable`
37	- [x] 1-T5 测试：Paper Agent Dream 模式 session 隔离 + 消息可见性 — 见 `tests/test_paper_agent_dream_session_isolation.py`
38	- [x] 1-T6 测试：Dream 工具可见性 — 由 prompt 段 (`paper-agent.md` Dream 模式) + `dream_id` 短路实现，覆盖在 `tests/test_paper_agent_dream_session_isolation.py` 及 `tests/test_paper_agent_dream_e2e.py`
39	- [x] 1-T7 测试：Dream Paper Agent 写入 `dream_reports/{id}/{tier}/paper.tex`，不写入 `projects/{project}/paper/` — 见 `tests/test_paper_agent_dream_e2e.py` (G2 output-path isolation)
40	
41	### Phase 2: Dream Tool 核心（异步架构 + 两阶段想象）
42	- [x] 2-1 实现 `core/dream_types.py`：DreamInput / DreamHandle / DreamOutput / TierDefinitions / TierDefinition / ImaginedScenario / ImaginedExperiment（含 WhatIfExperiment + DreamScenarioResult）
43	- [x] 2-2 实现 `core/dream_registry.py`：dream_registry.yaml 持久化状态管理（per-project + 文件锁 + 备份恢复）
44	- [x] 2-3 实现 `core/tools/dream.py`：`_collect_context()` 读取 framing + plan + registry
45	- [x] 2-4 实现 `_define_tiers()`：Phase 1 单 subprocess——统一定义三档含义 + 数字范围 + 叙事方向
46	- [x] 2-5 实现 `_elaborate_scenario()`：Phase 2 每档 subprocess——基于 TierDefinition 展开详细数据
47	- [x] 2-6 实现 `_write_dream_paper()`：启动 Paper Agent Dream 模式写论文（含统计图生成）
48	- [x] 2-7 实现 `_persist_report()`：保存到 `artifacts/dream_reports/{dream_id}/`（含 logs/）
49	- [x] 2-8 实现 `dream_simulate()`：注册 dream_registry + 启动独立编排进程 + 立即返回 dream_id
50	- [x] 2-9 实现 `_run_dream_pipeline()`：独立进程（`start_new_session=True`），编排想象→写作→审稿
51	- [x] 2-10 实现 `dispatch_dream_done()`：完成回调（注入 Director session + A 群摘要）
52	- [x] 2-11 实现 `get_dream_status()`：从 dream_registry.yaml 读取进度
53	- [x] 2-12 `core/mcp_server.py`：注册 `dream_simulate` + `get_dream_status` MCP Tool
54	- [x] 2-13 `core/tool_registry.py`：Director 白名单增加 `dream_simulate` + `get_dream_status`
55	- [x] 2-T1 测试：`tests/test_dream_types.py` — 类型定义序列化/反序列化（含 TierDefinitions）+ `tests/test_dream_registry.py` 覆盖 registry CRUD/stages/recovery/project 隔离
56	- [x] 2-T2 测试：`test_dream_collect_context.py` — context 收集（有/无 framing、有/无 plan、有/无 registry）+ helpers (YAML extraction, Phase 1/2 validators, ImaginedExperiment→ExperimentData mapping, dream_simulate pre-flight, get_dream_status)
57	- [x] 2-T3 测试：`test_dream_define_tiers.py` — Phase 1 三档定义一致性（best ≥ median ≥ worst）
58	- [x] 2-T4 测试：`test_dream_elaborate.py` — Phase 2 展开结果在 Phase 1 范围内 + result_rationale 必填
59	- [x] 2-T5 测试：`test_dream_persist.py` — 持久化目录结构 + meta.yaml + logs/
60	- [x] 2-T6 测试：`test_dream_what_if.py` — what_if 追加实验的合并逻辑
61	- [x] 2-T7 测试：`test_dream_async.py` — 独立编排进程 + dream_registry 持久化 + Director 重启后 status 可查
62	- [x] 2-T8 测试：`test_dream_status.py` — get_dream_status 各阶段状态查询 + failed 状态
63	- [x] 2-T9 测试：`test_dream_pipeline_failure.py` — 各阶段失败处理：部分结果 + error 记录
64	- [x] 2-T10 测试：`test_dream_concurrent.py` — 并发调用行为
65	- [x] 2-T11 测试：`test_dream_yaml_parsing.py` — YAML 输出解析 + 校验 + 解析失败重试/降级
66	- [x] 2-T12 测试：`test_dream_registry_id_writeback.py` — submit_training_job(plan_id=...) 自动写回 registry_id
67	
68	### Phase 3: Review Phase 集成
69	- [x] 3-1 `core/session_server.py`：支持 `dream_{id}:director` / `dream_{id}:reviewer_N` session key（`_detect_role` 检测 dream 段 → `dream_review_director` / `dream_review_reviewer_N` 角色 + `_mcp_config_for_role` 路由）
70	- [x] 3-2 `core/tools/feishu_group.py`：`director_post_to_reviewer()` 支持 dream 命名空间（显式 `dream_id` 参数 + 从 session_key 自动推断）
71	- [x] 3-3 `core/tools/feishu_group.py`：`submit_dream_review_report()` 替代 `submit_review_report_to_research_director`（写 `dream_reports/{dream_id}/{tier}/review_report.md`，不走 5-step protocol）
72	- [x] 3-4 `core/tools/feishu_group.py`：`review_visible=false` 时跳过 Group C 卡片，仅走内部 session_server 路由（`director_post_to_reviewer` + `review_reviewer_post_to_director` 都支持）
73	- [x] 3-5 实现 `_submit_to_review()`：spawn Dream Review Director subprocess（`_run_dream_review_director_subprocess` + `_build_dream_review_dispatch_prompt`），等子进程退出后从文件系统读 `review_report.md`
74	- [x] 3-5b 实现 `submit_dream_review_report()`：Dream 审稿专用报告提交工具（同时注册为 MCP tool）
75	- [x] 3-5c `_ensure_dream_review_director_mcp_config()` + `_ensure_dream_review_reviewer_mcp_config()`：Dream 缩减版工具白名单（`_DREAM_REVIEW_DIRECTOR_TOOLS` / `_DREAM_REVIEW_REVIEWER_TOOLS`）+ Dream 模式指令追加（`_build_dream_review_director` / `_build_dream_review_reviewer`）
76	- [x] 3-6 Dream 审稿 artifacts 全部在 `dream_reports/` 内（`submit_dream_review_report` 仅写该目录，工具白名单已剔除 `update_review_issues` / `submit_review_report_to_research_director`）
77	- [x] 3-7 `skills/global/dream-review-simple.skill.md`：简化模式全面审稿 prompt（合并方法 + 新颖性 + 实验设计，不含格式）
78	- [x] 3-8 完整模式支持：2 Reviewers（方法+实验 / 新颖性+相关工作）+ roundtable — 新增 `skills/global/dream-review-full.skill.md`（dispatch 模板：R1 方法+实验、R2 新颖性+相关工作、Step 1/2/3/4 roundtable 流程）+ `_build_dream_review_dispatch_prompt` 在 `review_mode=full` 时指向该 skill
79	- [x] 3-T1 测试：`test_dream_review_session_isolation.py` — Dream session key / role / MCP config / 工具白名单 / 提示词 / 生命周期 / 路由 / 提交工具 全链路隔离（27 tests）
80	- [x] 3-T2 测试：`test_dream_review_artifacts_isolation.py` — Dream artifacts 不写入真实审稿路径（17 tests：output path locality / no real-review artifacts / tier 隔离 / dream_id 隔离 / 工具白名单 / 可见性不改变 artifact 位置）
81	- [x] 3-T3 测试：`test_dream_review_visible.py` — review_visible=true/false 消息路由（15 tests：director_post_to_reviewer / review_reviewer_post_to_director / submit_dream_review_report 三个入口 + 默认值 + 调度 prompt 携带）
82	- [x] 3-T4 测试：`test_dream_review_simple.py` — 简化模式 1 Reviewer 跳过交叉分享（20 tests：dispatch payload / skill 模板形状 / 不 fan-out R2 / 默认 simple）
83	- [x] 3-T5 测试：`test_dream_review_full.py` — 完整模式 2 Reviewers roundtable 协议（27 tests：dispatch payload / 新建 `dream-review-full.skill.md` / R2 routing / 白名单）
84	- [x] 3-T6 测试：`test_dream_review_no_continue.py` — Dream 审稿不支持 Continue 模式，每次 Fresh（12 tests：session key 唯一 / subprocess 无 --resume / 白名单排除 Continue 入口 / 不走审批卡片）
85	- [x] 3-T7 测试：`test_dream_review_report_delivery.py` — submit_review_report Dream 模式不走 5-step protocol，直接返回给 Dream Tool（14 tests：报告无 protocol 文本 / 不路由到 Research Director / 文件交付 / 无 issue tracker / dream_reports 路径）
86	- [x] 3-T8 测试：`test_dream_review_simple_prompt.py` — 简化模式 reviewer 使用合并 prompt（方法 + 新颖性，不含格式），而非复用单方向 prompt（13 tests：merged template 三轴 / 格式 out of scope / skill 是 Director dispatch 而非 Reviewer prompt）
87	
88	### Phase 4: Director + 飞书 + Cron 集成
89	- [x] 4-1 `core/session_claude_md.py`：`_build_director()` prompt 增加 dream 工具使用指引（仅当 `dream_simulate` 在 director 白名单时注入；含 何时调 / what_if / 三档审稿解读 / cron 当前配置摘要）
90	- [x] 4-2 `core/agents/message_router.py`：注册 `/dream` 飞书 slash 命令（含 simple/full、what_if="..."、list/status/cancel 子命令）+ Research 群 `/help` 同步
91	- [x] 4-3 `core/cron_hooks.py`：新增 `on_dream` 事件 + `DEFAULT_HOOKS["on_dream"]` → `dream-cron` skill + `on_dream(project, cron_entry)` wrapper 读取 `get_dream_config` 并按 `cron_enabled` 短路（默认 False）
92	- [x] 4-4 `skills/global/dream-cron.skill.md`：定时 Dream 行为规范（含 smart_skip / 阶段限制 / cron 只用 simple mode 等约束）
93	- [x] 4-5 实现智能跳过（`_compute_context_hash` + `should_skip_dream` MCP tool；`dream_simulate(smart_skip=True)` 短路；registry 持久化 `context_hash`）
94	- [x] 4-6 实现趋势追踪（`get_dream_trend` MCP tool：读取 `dream_reports/*/meta.yaml` + 计算相邻 dream 的 per-tier 预测 delta）
95	- [x] 4-T1 测试：`test_dream_feishu_command.py` — `/dream` / `/dream full` / `/dream what_if "..."` 解析 + list/status/cancel 子命令 + help 文本 (37 tests)
96	- [x] 4-T2 测试：`test_dream_cron.py` — cron_enabled=false 不触发；=true 按 schedule 触发 + DEFAULT_HOOKS 注册 + dream-cron skill 解析 + 端到端 send_sync (13 tests)
97	- [x] 4-T3 测试：`test_dream_smart_skip.py` — 18 tests：context hash 稳定性 + 各字段变更触发重算 + `should_skip_dream` 三种 reason + `dream_simulate(smart_skip=True)` 短路 + registry 持久化 hash
98	- [x] 4-T4 测试：`test_dream_trend.py` — 15 tests：newest-first 排序 + limit 截断 + per-tier 预测 delta（added/removed/changed）+ failed dream 透明展示 + 内部 helpers
99	
100	### 集成测试
101	- [x] E2E-1 `test_dream_e2e_simple.py`：完整流程——想象 → Paper Agent 写论文 → 简化审稿 → 报告返回 Director（4 tests：pipeline 完成、handle 同步返回、Director summary 注入、simple dispatch skill）
102	- [x] E2E-2 `test_dream_e2e_full.py`：完整流程——完整模式 2 Reviewers roundtable（3 tests：full 模式 pipeline、dream-review-full skill dispatch、review_visible 透传）
103	- [x] E2E-3 `test_dream_post_mvp.py`：Post-MVP 流程——制定 framing → plan → dream(full) → 调整 → 再 dream（4 tests：framing/plan 缺失拦截、首次 dream、调整 plan 后第二次 dream、第一次产物不变）
104	- [x] E2E-4 `test_dream_what_if_comparison.py`：两次 dream 对比（有/无 what_if）的结果差异（5 tests：baseline 无 what_if、what_if 进 meta、Phase 2 context 差异、context hash 差异、plan 文件不被修改）
105	- [x] E2E-5 `test_dream_isolation_full.py`：Dream 全链路隔离——Paper Agent session + Review session + artifacts 均不污染真实流程（10 tests：真实 paper/ 不变、真实 review_reports/ 不变、Dream artifacts 仅在 dream_reports/、session key dream 段、role 检测、白名单隔离）
106	- [x] E2E-6 `test_dream_async_director.py`：异步行为——Dream 运行期间 Director 继续审批实验、回复 Agent，Dream 完成后结果正确注入（6 tests：同步返回、status 可查、stage 状态进展、并发 status 查询不阻塞、dispatch_dream_done 注入、空 director_session_key 不崩）
107	- [x] E2E-7 `test_dream_partial_failure.py`：部分失败——某一档（如 worst）写作失败，其余两档（best/median）的审稿结果仍正常返回（6 tests：write 失败、review 失败、Phase 2 失败、2/3 失败仍 done、全失败为 failed、Director summary 反映部分失败）
108	
109	---
110	
111	## 一、定位与核心思路
112	
113	### 1.1 要解决什么问题
114	
115	Auto Research 链路中存在大量需要"评判"的环节——Idea 好不好？实验计划值不值得做？当前方向还能不能出论文？这些对象都是抽象的，无论对人还是对 Agent，直接评判都很难做准。
116	
117	目前系统中的尝试（Agent + Reviewer 聊几句得出"加 5% 中稿概率"）太糙，本质是两个 Agent 在评判一个抽象对象，没有实质性推演。
118	
119	### 1.2 核心思路
120	
121	**把难以评判的抽象对象，正向模拟为容易评判的具体对象。**
122	
123	```
124	难以直接评判的抽象对象          容易评判的具体对象
125	┌─────────────────┐          ┌─────────────────┐
126	│  Idea            │          │                 │
127	│  实验计划         │ ──Dream──→  模拟论文 PDF    │ ──Group C 审稿──→ 审稿报告
128	│  决策链           │          │  (上/中/下三档)   │
129	└─────────────────┘          └─────────────────┘
130	```
131	
132	- **Dream**：基于输入（idea + 现状 + 决策），**只想象未来的实验和结果**（不触碰已有的真实实验数据）
133	- **Paper Agent（Dream 模式）**：将 Dream 的想象内容 + 已有真实数据写成完整 LaTeX 论文并编译为 PDF
134	- **审稿**：将 PDF 交给现有的 Group C 审稿流程（Review Director + Reviewers），走完整的 roundtable 协议
135	- **综合**：Director 收到三档论文的审稿报告，自行判断 idea + 现状 + 决策的质量
136	
137	### 1.3 关键原则：Dream 只想象未来，Paper Agent 不区分来源
138	
139	Dream 的核心产出是**对未来实验和对应结果的想象**：
140	
141	- Dream 生成的是"如果做了实验 X，可能会得到结果 Y"——只想象**尚未做的**实验
142	- 已有的真实实验数据原封不动地从 registry 中读取
143	- Paper Agent（Dream 模式）收到的所有数据（真实 + 想象）都**统一当作真实数据来写作**，不做区分。因为已经分了上/中/下三档，每档本身就是一个完整的"如果未来是这样"的假设场景，全部按真实数据写，写出的论文最逼真，拿到的审稿结论也最准确
144	
145	---
146	
147	## 二、前置改动：Paper Framing + Experiment Plan
148	
149	Dream 需要两个核心输入来"做梦"——论文的完整故事（要讲什么）和实验计划（怎么讲）。目前系统中没有这两个东西。ROADMAP 太短（200 行），只覆盖核心 idea + 近期任务，缺乏长期目标和完整叙事。
150	
151	### 2.1 新增文件：paper_framing.md
152	
153	**位置**：`projects/{project}/paper_framing.md`
154	
155	**内容**：论文的完整故事——从问题到贡献到 story arc，不是大纲而是详细的叙事规划。
156	
157	```markdown
158	## Core Problem
159	[什么问题，为什么重要，现有方法为什么不够]
160	
161	## Key Insight
162	[我们的核心洞察/切入点]
163	
164	## Proposed Method
165	[方法概述，关键技术点]
166	
167	## Story Arc
168	[论文的叙事线：怎么从问题引出 insight，怎么从 insight 引出 method，
169	 怎么用实验论证 method 的有效性]
170	
171	## Core Claims
172	[每个 claim 及其所需的实验证据]
173	- Claim 1: "..." → 需要实验: main_results, baseline_comparison
174	- Claim 2: "..." → 需要实验: ablation_X, ablation_Y
175	- Claim 3: "..." → 需要实验: scale_experiment, efficiency_analysis
176	
177	## Anticipated Reviewer Concerns
178	[预判审稿人会提什么问题，每个 concern 对应什么实验来回应]
179	- Concern: "与 Z 方法的对比不充分" → 需要实验: baseline_Z_comparison
180	- Concern: "泛化性存疑" → 需要实验: cross_dataset_transfer
181	
182	## Target Venue & Constraints
183	[目标会议、页数限制、格式要求、deadline]
184	```
185	
186	**谁维护**：Research Director 通过 `save_project_file("paper_framing.md", content)` 创建和更新。Paper Agent 和 Dream Tool 通过 `read_project_file("paper_framing.md")` 读取。不需要专用工具——framing 是自由格式的 markdown，没有需要程序保障的约束。
187	
188	**与 ROADMAP 的关系**：ROADMAP 中可引用 framing（`见 paper_framing.md`），但 framing 本身独立存在，不受 200 行限制。
189	
190	### 2.2 新增文件：experiment_plan.yaml
191	
192	**位置**：`projects/{project}/experiment_plan.yaml`
193	
194	**内容**：所有规划中的实验——包括已完成的、进行中的、和计划做但还没提交的。
195	
196	```yaml
197	# 注意：plan 中不存 status 字段（选项 C）。
198	# 有 registry_id 的实验，status 通过 read_experiment_plan_with_status() 从 registry 动态读取。
199	# 无 registry_id 的实验，隐含 status = planned。
200	
201	experiments:
202	  # 已提交到 registry 的实验——plan 中只存规划信息，不存 status
203	  - id: plan_001
204	    name: "main_results_dataset_A"
205	    registry_id: exp_001            # 有此字段 = 已提交，status 从 registry 动态读取
206	    claim: "Claim 1"
207	    framing_ref: "Core Claims → Claim 1"
208	
209	  - id: plan_002
210	    name: "ablation_learning_rate"
211	    registry_id: exp_002
212	    claim: "Claim 2"
213	
214	  # 计划中的实验——无 registry_id，隐含 planned 状态
215	  - id: plan_003
216	    name: "baseline_Z_comparison"
217	    # 无 registry_id = planned
218	    claim: "Claim 1"
219	    framing_ref: "Anticipated Reviewer Concerns → 与 Z 方法的对比"
220	    priority: P0
221	    estimated_gpu_hours: 8
222	    depends_on: [plan_001]
223	    description: "在 Dataset A/B/C 上与 Z 方法做完整对比..."
224	
225	  - id: plan_004
226	    name: "cross_dataset_transfer"
227	    claim: "Claim 3"
228	    framing_ref: "Anticipated Reviewer Concerns → 泛化性"
229	    priority: P1
230	    estimated_gpu_hours: 16
231	    description: "..."
232	```
233	
234	**谁维护**：Research Director 通过 `save_project_file("experiment_plan.yaml", content)` 创建和管理。Plan 是纯规划文档，不存执行状态——所有状态查询通过 `read_experiment_plan_with_status()` 动态合并 registry。
235	
236	### 2.2.1 experiment_matrix 是否还需要存在？
237	
238	**结论：experiment_matrix 应该废弃为持久文件，改为按需计算的派生视图。**
239	
240	experiment_matrix 的核心价值是"paper target → 实验的 2D 映射 + 覆盖率可视化"。但引入 paper_framing.md 和 experiment_plan.yaml 后，这个价值已被完全覆盖：
241	
242	| matrix 提供的 | 现在由谁提供 |
243	|-------------|------------|
244	| Paper targets（9 维度） | paper_framing.md 的 Core Claims + Reviewer Concerns |
245	| 每个 target 对应什么实验 | experiment_plan.yaml 的 `claim` / `framing_ref` 字段 |
246	| 覆盖率（哪些 target 还缺实验） | 从 plan 中按 claim 分组统计即可 |
247	| Cell 状态（planned/running/filled） | `read_experiment_plan_with_status()` 动态合并 |
248	
249	**三个文件存同一件事 = 三份需要同步的状态。** 目前 `update_registry()` 已经有 `_sync_matrix_for_experiment()` 作为 side-effect；如果再加 `_sync_plan_for_experiment()`，就是一次 registry 更新要同步两个下游文件。而 plan 和 matrix 存的本质是同一件事（实验 → paper target 的映射 + 状态）。
250	
251	**改为派生视图**：当 Director 或 Dream 需要看"覆盖率矩阵"时，从 plan + framing 实时计算：
252	
253	```python
254	def compute_coverage_matrix(project: str) -> CoverageMatrix:
255	    """按需计算覆盖率矩阵，不持久化。
256	
257	    覆盖率的计算方向是 plan → framing：遍历 plan 中每个实验的 claim 字段，
258	    按 claim 分组统计。不需要解析 framing markdown 的结构——framing 是给人和
259	    LLM 读的自由文本，claim 的权威 ID 在 plan 的 claim 字段中。
260	    """
261	    framing_text = read_project_file(project, "paper_framing.md")  # 原文，供展示
262	    plan = read_experiment_plan_with_status(project)
263	
264	    # 从 plan 中提取所有唯一的 claim 名称
265	    claims = sorted(set(e["claim"] for e in plan if e.get("claim")))
266	
267	    matrix = {}
268	    for claim in claims:
269	        experiments = [e for e in plan if e.get("claim") == claim]
270	        matrix[claim] = {
271	            "experiments": experiments,
272	            "coverage": _compute_coverage(experiments),  # 0-100%
273	        }
274	    return matrix
275	```
276	
277	**设计要点**：覆盖率矩阵从 `experiment_plan.yaml` 的 `claim` 字段聚合，不解析 `paper_framing.md` 的 markdown 结构。Framing 是自由格式文档（给人和 LLM 读），不适合程序化解析。Plan 中的 `claim` 字段是结构化的权威来源——Director 在制定 plan 时确保 claim 名称与 framing 一致。
278	
279	**对现有代码的影响**：
280	- `_sync_matrix_for_experiment()` side-effect 从 `update_registry()` 中移除
281	- `experiment-matrix` skill 改为调用 `compute_coverage_matrix()` 展示结果
282	- Director prompt 中不再提 "画空矩阵"，改为 "查看覆盖率"
283	
284	### 2.2.2 experiment_plan.yaml 和 registry 是否需要两个文件？
285	
286	**问题的本质：plan 中"已提交"实验的 status 是 registry 中 status 的复制品。两个文件存同一个 status = 需要同步 = 容易不一致。**
287	
288	分析三个选项：
289	
290	**~~选项 A：合并到 registry（给 registry 加 PLANNED 状态）~~ ❌ 已否决**
291	
292	```
293	PLANNED → PREPARING → PENDING → QUEUED → ALLOCATED → RUNNING → ANALYZING → DONE
294	```
295	
296	Registry 增加字段：`claim`、`framing_ref`、`priority`、`depends_on`、`estimated_gpu_hours`。
297	
298	| 优势 | 劣势 |
299	|------|------|
300	| 单一数据源，零同步 | registry 混合了规划和执行两种职责 |
301	| 所有工具和 side-effect 自动生效 | Director 改规划（增删 PLANNED 实验）会触发 registry 的 checkpoint/report 刷新 |
302	| 状态机天然覆盖全生命周期 | PLANNED 状态的实验没有 spec（command/server/gpu），但 registry 对 RUNNING 要求 spec 齐全——两种实验的数据 schema 差异大 |
303	
304	**~~选项 B：两个文件 + 状态同步~~ ❌ 已否决**
305	
306	Plan 存规划信息 + status，registry 存执行信息 + status。通过 `update_registry()` side-effect 同步。
307	
308	| 优势 | 劣势 |
309	|------|------|
310	| 职责清晰分离 | 两个文件存同一个 status，需要同步 |
311	| Director 改规划不影响 registry | 同步逻辑增加系统复杂度 |
312	| 向后兼容（没有 plan 的项目不受影响） | 崩溃/手动编辑可能导致 drift |
313	
314	**选项 C：两个文件，plan 不存已提交实验的 status（推荐）**
315	
316	Plan 只存**规划信息**（claim、priority、depends_on、description），不存 status。Status 通过 `registry_id` 实时从 registry 查询：
317	
318	```yaml
319	experiments:
320	  # 已提交到 registry 的实验——plan 中不存 status，读取时从 registry 动态获取
321	  - id: plan_001
322	    name: "main_results_dataset_A"
323	    registry_id: exp_001            # 有这个字段 = 已提交，status 从 registry 读
324	    claim: "Claim 1"
325	    framing_ref: "Core Claims → Claim 1"
326	
327	  # 计划中的实验——没有 registry_id，status 隐含为 planned
328	  - id: plan_003
329	    name: "baseline_Z_comparison"
330	    # 无 registry_id = planned
331	    claim: "Claim 1"
332	    framing_ref: "Anticipated Reviewer Concerns → 与 Z 方法的对比"
333	    priority: P0
334	    estimated_gpu_hours: 8
335	    depends_on: [plan_001]
336	    description: "在 Dataset A/B/C 上与 Z 方法做完整对比..."
337	```
338	
339	```python
340	def read_experiment_plan_with_status(project: str) -> list[PlanEntry]:
341	    """读取 plan 时，动态合并 registry 状态。"""
342	    plan = _read_experiment_plan_raw(project)
343	    registry = _read_registry(project)
344	
345	    for entry in plan:
346	        if entry.get("registry_id"):
347	            reg_exp = registry.get(entry["registry_id"])
348	            if reg_exp:
349	                entry["status"] = reg_exp["status"]
350	                entry["conclusion"] = reg_exp.get("conclusion")
351	                entry["metrics"] = reg_exp.get("metrics")
352	            else:
353	                entry["status"] = "orphaned"  # registry 中被删了
354	        else:
355	            entry["status"] = "planned"
356	
357	    return plan
358	```
359	
360	| 优势 | 劣势 |
361	|------|------|
362	| **零同步**——plan 中没有 status 字段，不存在重复状态 | 读取 plan 需要同时读 registry（一次额外 IO） |
363	| 规划和执行完全解耦 | 调用者需要用 `read_experiment_plan_with_status()` 而非直接读 YAML |
364	| 不需要任何 `update_registry()` side-effect | |
365	| 不需要 reconciliation | |
366	| 完全向后兼容 | |
367	
368	**采用选项 C。** 原因：
369	
370	1. **从根源消除同步问题**——不存重复状态，就不需要同步
371	2. **Plan 文件成为纯规划文档**——规划内容（claim/priority/depends_on/description）只有 Director 写入
372	3. **Registry 完全不改**——不加 PLANNED 状态，不加 claim 字段，不加新 side-effect
373	4. **读取时 join 的成本可忽略**——两个小 YAML 文件的内存 join，微秒级
374	
375	**`registry_id` 写回机制：**
376	
377	Plan entry 从 planned 变为已提交时，需要写入 `registry_id`。这由**系统自动完成**（不是 Director 也不是 Agent 手动写）：
378	
379	Agent 调用 `submit_training_job()` 时传入 `plan_id` 参数：
380	```python
381	submit_training_job(
382	    ...,
383	    plan_id="plan_003",  # 对应 experiment_plan.yaml 中的 id
384	)
385	```
386	
387	`submit_training_job()` 在创建 registry entry（`exp_001`）后，自动将 `registry_id: exp_001` 写回 `experiment_plan.yaml` 中 `id == plan_003` 的 entry。这是一个**系统级 side-effect**，类似 registry 的 checkpoint/report 刷新——不改变"Director 拥有规划内容"的语义，只是维护了 plan ↔ registry 的关联。
388	
389	如果 `plan_id` 未传或未匹配到 plan entry，不报错（ad-hoc 实验不需要 plan 关联）。
390	
391	### 2.3 ROADMAP 的角色重新定义
392	
393	ROADMAP 的最大价值是**短**——200 行内覆盖核心 idea + 近期决策，适合 Agent 每次 session 启动时快速读取建立 context。但它缺乏长期目标。
394	
395	**新的分工：**
396	
397	| 文件 | 回答什么问题 | 长度 | 更新频率 |
398	|------|------------|------|---------|
399	| **paper_framing.md** | "我们在写什么论文，讲什么故事" | 无限制 | 方向变化时 |
400	| **experiment_plan.yaml** | "有哪些实验，为什么做"（status 从 registry 动态读取） | 无限制 | Director 调整规划时 |
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59b2e01c-e70b-4fdb-96a5-fa5830a8b740",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "fc45962b-92dd-41b0-8e39-f620bd97868b",
  "sourceToolAssistantUUID": "59b2e01c-e70b-4fdb-96a5-fa5830a8b740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T15:39:09.446Z_

Perfect! Now I have all the information I need. Let me also check if there's a test file for the coverage matrix to see example data:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc45962b-92dd-41b0-8e39-f620bd97868b",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSdCG9gGTEBTV1ckcC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "840d3351-ea43-4411-832c-01eb9df36b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E2Zp7t1Dp7BE1NNatJSiMy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11731,
      "cache_read_input_tokens": 46347,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11731,
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

_source line 34 · 2026-05-13T15:39:09.723Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V3CUgfpEA5wEgNgEcJA8rf`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research/tests -name \"*coverage*\" -o -name \"*matrix*\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "840d3351-ea43-4411-832c-01eb9df36b08",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSdCG9gGTEBTV1ckcC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "28f4c06e-e7f9-4163-85f7-1fa3aa63baa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E2Zp7t1Dp7BE1NNatJSiMy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11731,
      "cache_read_input_tokens": 46347,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 113,
          "cache_read_input_tokens": 46347,
          "cache_creation_input_tokens": 11731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11731,
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

_source line 35 · 2026-05-13T15:39:09.786Z_

<details><summary>↩ Tool result · `toolu_01V3CUgfpEA5wEgNgEcJA8rf`</summary>

```text
/home/ubuntu/agent-ml-research/tests/test_experiment_matrix.py
/home/ubuntu/agent-ml-research/tests/test_experiment_matrix_skill.py
/home/ubuntu/agent-ml-research/tests/test_api_matrix.py
/home/ubuntu/agent-ml-research/tests/test_coverage_matrix.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28f4c06e-e7f9-4163-85f7-1fa3aa63baa2",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "3cd5e292-d30e-4100-9877-b3dba893d1b4",
  "sourceToolAssistantUUID": "28f4c06e-e7f9-4163-85f7-1fa3aa63baa2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T15:39:11.876Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GvzsRW2jwSnLd8mEjbyhtL`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/tests/test_coverage_matrix.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cd5e292-d30e-4100-9877-b3dba893d1b4",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSpH1gJwMsdomngJp1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "675758f3-bc2b-4aa9-bc53-71b92ca0d8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01G4BFwvaMfoTGJp7TfLmJSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 58078,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 313
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 72,
          "cache_read_input_tokens": 58078,
          "cache_creation_input_tokens": 313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 313,
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

_source line 37 · 2026-05-13T15:39:11.888Z_

<details><summary>↩ Tool result · `toolu_01GvzsRW2jwSnLd8mEjbyhtL`</summary>

```text
1	"""Tests for ``compute_coverage_matrix()`` in core/tools/experiment_plan.py.
2	
3	The coverage matrix groups plan entries by ``claim`` and rolls registry
4	status up into a small bucket vocabulary (planned / running / done /
5	failed / orphaned). These tests exercise:
6	
7	- Empty / missing plan files.
8	- Grouping by claim plus the unassigned bucket.
9	- Bucket mapping for each status the registry can return.
10	- Coverage percentages with single- and multi-experiment claims.
11	- The summary section's totals.
12	"""
13	
14	from __future__ import annotations
15	
16	from pathlib import Path
17	
18	import pytest
19	import yaml
20	
21	from core.tools.experiment_plan import (
22	    compute_coverage_matrix,
23	    get_experiment_plan_path,
24	)
25	from core.tools.registry import get_registry_path
26	
27	
28	def _seed_plan(project: str, experiments: list[dict]) -> Path:
29	    p = get_experiment_plan_path(project)
30	    p.write_text(yaml.safe_dump({"experiments": experiments}, allow_unicode=True))
31	    return p
32	
33	
34	def _seed_registry(project: str, experiments: dict[str, dict]) -> Path:
35	    p = get_registry_path(project)
36	    p.write_text(yaml.safe_dump({"experiments": experiments, "baseline": None}))
37	    return p
38	
39	
40	class TestCoverageMatrix:
41	
42	    def test_empty_when_no_plan(self, workspace):
43	        r = compute_coverage_matrix("proj_x")
44	        assert r.success
45	        assert r.data["claims"] == []
46	        assert r.data["matrix"] == {}
47	        assert r.data["unassigned"] == []
48	        assert r.data["summary"]["total_experiments"] == 0
49	        assert r.data["summary"]["coverage_pct"] == 0.0
50	
51	    def test_groups_by_claim(self, workspace):
52	        _seed_plan("proj_x", [
53	            {"id": "plan_001", "claim": "Claim 1"},
54	            {"id": "plan_002", "claim": "Claim 1"},
55	            {"id": "plan_003", "claim": "Claim 2"},
56	        ])
57	        r = compute_coverage_matrix("proj_x")
58	        assert r.success
59	        assert r.data["claims"] == ["Claim 1", "Claim 2"]
60	        assert len(r.data["matrix"]["Claim 1"]["experiments"]) == 2
61	        assert len(r.data["matrix"]["Claim 2"]["experiments"]) == 1
62	
63	    def test_unassigned_entries_collected(self, workspace):
64	        _seed_plan("proj_x", [
65	            {"id": "plan_001", "claim": "Claim 1"},
66	            {"id": "plan_002"},  # no claim
67	            {"id": "plan_003"},
68	        ])
69	        r = compute_coverage_matrix("proj_x")
70	        ids = sorted(e["id"] for e in r.data["unassigned"])
71	        assert ids == ["plan_002", "plan_003"]
72	        assert r.data["summary"]["unassigned"] == 2
73	
74	    def test_coverage_pct_for_completed_claim(self, workspace):
75	        """Two of three experiments in Claim 1 are DONE/success → 66.7%."""
76	        _seed_plan("proj_x", [
77	            {"id": "plan_001", "claim": "Claim 1", "registry_id": "exp_a"},
78	            {"id": "plan_002", "claim": "Claim 1", "registry_id": "exp_b"},
79	            {"id": "plan_003", "claim": "Claim 1"},
80	        ])
81	        _seed_registry("proj_x", {
82	            "exp_a": {"status": "DONE", "conclusion": "success"},
83	            "exp_b": {"status": "DONE", "conclusion": "success"},
84	        })
85	        r = compute_coverage_matrix("proj_x")
86	        c1 = r.data["matrix"]["Claim 1"]
87	        assert c1["counts"]["done"] == 2
88	        assert c1["counts"]["planned"] == 1
89	        assert c1["coverage"] == "2/3"
90	        assert c1["coverage_pct"] == round(100 * 2 / 3, 1)
91	
92	    def test_bucket_mapping_covers_all_statuses(self, workspace):
93	        """Each registry status maps to the expected coverage bucket."""
94	        _seed_plan("proj_x", [
95	            {"id": "p_planned", "claim": "C"},
96	            {"id": "p_running", "claim": "C", "registry_id": "r_running"},
97	            {"id": "p_done", "claim": "C", "registry_id": "r_done"},
98	            {"id": "p_failed", "claim": "C", "registry_id": "r_failed"},
99	            {"id": "p_orphan", "claim": "C", "registry_id": "r_missing"},
100	        ])
101	        _seed_registry("proj_x", {
102	            "r_running": {"status": "RUNNING"},
103	            "r_done":    {"status": "DONE", "conclusion": "success"},
104	            "r_failed":  {"status": "DONE", "conclusion": "failed"},
105	            # r_missing intentionally absent → orphaned.
106	        })
107	        r = compute_coverage_matrix("proj_x")
108	        counts = r.data["matrix"]["C"]["counts"]
109	        assert counts == {
110	            "planned": 1, "running": 1, "done": 1,
111	            "failed": 1, "orphaned": 1,
112	        }
113	        # 1 done out of 5 → 20%.
114	        assert r.data["matrix"]["C"]["coverage_pct"] == 20.0
115	
116	    def test_summary_aggregates_across_claims(self, workspace):
117	        _seed_plan("proj_x", [
118	            {"id": "p1", "claim": "C1", "registry_id": "e1"},
119	            {"id": "p2", "claim": "C2", "registry_id": "e2"},
120	            {"id": "p3", "claim": "C2"},
121	        ])
122	        _seed_registry("proj_x", {
123	            "e1": {"status": "DONE", "conclusion": "success"},
124	            "e2": {"status": "RUNNING"},
125	        })
126	        r = compute_coverage_matrix("proj_x")
127	        s = r.data["summary"]
128	        assert s["total_experiments"] == 3
129	        assert s["total_claims"] == 2
130	        assert s["counts"]["done"] == 1
131	        assert s["counts"]["running"] == 1
132	        assert s["counts"]["planned"] == 1
133	        assert s["coverage"] == "1/3"
134	        assert s["coverage_pct"] == round(100 / 3, 1)
135	
136	    def test_intermediate_statuses_count_as_running(self, workspace):
137	        """PREPARING/PENDING/QUEUED/ALLOCATED/ANALYZING all roll into "running"."""
138	        statuses = ["PREPARING", "PENDING", "QUEUED", "ALLOCATED", "ANALYZING"]
139	        plan = []
140	        registry = {}
141	        for i, st in enumerate(statuses):
142	            pid = f"plan_{i:03d}"
143	            eid = f"exp_{i:03d}"
144	            plan.append({"id": pid, "claim": "C", "registry_id": eid})
145	            registry[eid] = {"status": st}
146	        _seed_plan("proj_x", plan)
147	        _seed_registry("proj_x", registry)
148	        r = compute_coverage_matrix("proj_x")
149	        assert r.data["matrix"]["C"]["counts"]["running"] == len(statuses)
150	        assert r.data["matrix"]["C"]["counts"]["done"] == 0
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "675758f3-bc2b-4aa9-bc53-71b92ca0d8c3",
  "isSidechain": true,
  "promptId": "d2598d23-c4b2-4a60-9caa-6e35fb60a8a8",
  "agentId": "a687669e02e1c82a7",
  "type": "user",
  "uuid": "6c33a799-55c9-4315-8e02-da4dace42ae7",
  "sourceToolAssistantUUID": "675758f3-bc2b-4aa9-bc53-71b92ca0d8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-13T15:39:28.251Z_

Excellent! Now I have all the information needed. Let me create a comprehensive report.

## Summary

I've successfully identified the expected YAML schema for `experiment_plan.yaml` by analyzing the implementation of both `read_experiment_plan_with_status` and `compute_coverage_matrix` in the agent-ml-research codebase.

---

## Expected YAML Schema for experiment_plan.yaml

### Top-Level Structure

The YAML file must have exactly this top-level key:

```yaml
experiments:
  - id: ...
    # other fields...
  - id: ...
    # other fields...
```

**Critical**: The top-level must be `experiments:` (NOT `claims:` and `experiments:` as a dict). Your current structure with separate `claims:` dict is not compatible.

### Required Fields Per Experiment Entry

Each entry in the `experiments` list **must** have:

1. **`id`** (required, string) — Unique identifier for the plan entry (e.g., `"plan_001"`)
   - Entries without an `id` are silently dropped during parsing (line 107 in experiment_plan.py: `if isinstance(e, dict) and e.get("id")`)

2. **`claim`** (optional, string) — The claim this experiment supports
   - Used by `compute_coverage_matrix()` to group experiments by claim (line 292)
   - If absent, the entry goes into the `unassigned` bucket (lines 290-296)
   - This field is critical for the coverage matrix functionality

3. **`registry_id`** (optional, string) — Reference to a registry experiment
   - If present and matches a registry entry: status/conclusion/metrics are pulled from registry
   - If present but registry entry is missing: status becomes `"orphaned"`
   - If absent: status defaults to `"planned"`

### Optional Fields (Recognized but Not Required)

- `name` (string) — Human-readable name
- `description` (string) — Long-form description
- `priority` (string) — Priority level (e.g., `"P0"`, `"P1"`)
- `depends_on` (list of strings) — Plan IDs this depends on
- `estimated_gpu_hours` (number) — GPU budget estimate
- `framing_ref` (string) — Reference to framing document section
- Any other custom fields — preserved but not used by tools

### Status Fields (Auto-Populated, Not in YAML)

These are **computed dynamically** during `read_experiment_plan_with_status()` and should NOT be stored in the YAML file:

- `status` — One of: `"planned"`, `"orphaned"`, or any registry status (e.g., `"RUNNING"`, `"DONE"`)
- `conclusion` — Only present if registry entry has one (e.g., `"success"`, `"failed"`)
- `metrics` — Only present if registry entry has them

---

## Correct YAML Format

```yaml
experiments:
  # Already submitted to registry
  - id: plan_001
    name: "main_results_dataset_A"
    registry_id: exp_001
    claim: "Claim 1"
    framing_ref: "Core Claims → Claim 1"

  - id: plan_002
    name: "ablation_learning_rate"
    registry_id: exp_002
    claim: "Claim 2"

  # Planned experiments (no registry_id yet)
  - id: plan_003
    name: "baseline_Z_comparison"
    claim: "Claim 1"
    framing_ref: "Anticipated Reviewer Concerns → Z comparison"
    priority: P0
    estimated_gpu_hours: 8
    depends_on: [plan_001]
    description: "Compare against Z method on Dataset A/B/C"

  - id: plan_004
    name: "cross_dataset_transfer"
    claim: "Claim 3"
    priority: P1
    estimated_gpu_hours: 16
    description: "Evaluate generalization across datasets"
```

---

## Why Your Current Structure Fails

Your current YAML has:

```yaml
claims:
  Claim 1: ...
  Claim 2: ...
experiments:
  - plan_id: ...
    name: ...
    claim: ...
```

**Issues:**

1. **Top-level `claims:` dict is ignored** — The parsers only look for `data.get("experiments")` (line 102, experiment_plan.py)
2. **Field name is `plan_id` not `id`** — The code explicitly checks `e.get("id")` (line 107); entries without `id` are dropped
3. **No `registry_id` field** — Without it, status stays `"planned"` forever and can never reflect actual registry state

---

## Source Code Evidence

**From `/home/ubuntu/agent-ml-research/core/tools/experiment_plan.py`:**

- Lines 102-109: Raw YAML parsing expects `data.get("experiments")` to be a list; drops any entry without an `id`
- Lines 176-190: `_attach_status()` joins plan with registry using the `registry_id` field
- Lines 219: `read_experiment_plan_with_status()` returns only the `experiments` list
- Lines 289-296: `compute_coverage_matrix()` groups by `claim` field; entries without `claim` go to `unassigned`

**Test evidence** (`test_experiment_plan.py` lines 58-62, test_coverage_matrix.py lines 52-61):

```python
_seed_plan("proj_x", [
    {"id": "plan_001", "name": "main", "claim": "Claim 1"},
    {"id": "plan_002", "name": "ablation", "claim": "Claim 2"},
])
```

All test examples use `id`, not `plan_id`, and `claim` as a per-entry field, not a top-level dict.

---

## Fix Required

1. **Remove the `claims:` dict entirely** — it's not parsed
2. **Rename `plan_id` to `id`** in every entry
3. **Keep `claim` as a string field in each experiment entry** (not a top-level key)
4. **Add `registry_id` field to entries already submitted**, so their status pulls from the registry
5. **Omit `status` fields from the YAML** — they're computed on every read

This structure matches the documented format in `/home/ubuntu/agent-ml-research/docs/plans/dream/DREAM_AGENT_DESIGN.md` (lines 196-232).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c33a799-55c9-4315-8e02-da4dace42ae7",
  "isSidechain": true,
  "agentId": "a687669e02e1c82a7",
  "requestId": "req_011CazpSxytY6oEaCERjAsy4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b4200317-da87-4c0c-82e6-fbe95ef52b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/.claude/sessions/agent_32270b04",
  "sessionId": "6750f4f6-3193-46ae-b369-8b58278787ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CeqHqRNkNLZd77eLHobxq5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 58391,
      "output_tokens": 1600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2299
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1600,
          "cache_read_input_tokens": 58391,
          "cache_creation_input_tokens": 2299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2299,
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
