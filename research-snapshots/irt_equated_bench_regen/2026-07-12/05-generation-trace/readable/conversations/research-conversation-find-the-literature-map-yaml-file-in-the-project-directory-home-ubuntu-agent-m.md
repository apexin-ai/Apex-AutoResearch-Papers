# Research conversation: Find the literature_map.yaml file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5a664161719b85a9.jsonl`
- **Structured JSON:** [`33ef992d9b01525a55fe.json`](../../sessions/33/33ef992d9b01525a55fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-21T03:47:40.950Z_

Find the literature_map.yaml file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/. Search broadly — it might be in artifacts/, paper/, or root level. Also check if there's a core/tools/literature.py or similar module under /home/ubuntu/agent-ml-research/.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b7659c62-7248-4d0c-bac6-a05298eadbc6",
  "agentId": "a5a664161719b85a9",
  "type": "user",
  "uuid": "d25666a4-36ec-440b-92fe-142ab4326ed6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T03:47:42.587Z_

I'll search for the literature_map.yaml file and any related literature modules in the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d25666a4-36ec-440b-92fe-142ab4326ed6",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fMgg6GsDAgvtsE2Cq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85e8f8a8-57b9-4e95-8ab1-dac777f09422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
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

_source line 3 · 2026-05-21T03:47:43.033Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01BEJrYhGm5cwnvSYJK32ztw`</summary>

```json
{
  "pattern": "**/literature_map.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85e8f8a8-57b9-4e95-8ab1-dac777f09422",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fMgg6GsDAgvtsE2Cq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "09da1c56-87fe-432f-a3d8-ab88f8a24656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
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

_source line 4 · 2026-05-21T03:47:43.063Z_

<details><summary>↩ Tool result · `toolu_01BEJrYhGm5cwnvSYJK32ztw`</summary>

```text
literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09da1c56-87fe-432f-a3d8-ab88f8a24656",
  "isSidechain": true,
  "promptId": "b7659c62-7248-4d0c-bac6-a05298eadbc6",
  "agentId": "a5a664161719b85a9",
  "type": "user",
  "uuid": "868ea32f-627a-42db-915d-2a8e2988014f",
  "sourceToolAssistantUUID": "09da1c56-87fe-432f-a3d8-ab88f8a24656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T03:47:43.244Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Tvsba9Ho4T2rmHRXXqRHh1`</summary>

```json
{
  "pattern": "**/literature*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "868ea32f-627a-42db-915d-2a8e2988014f",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fMgg6GsDAgvtsE2Cq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57c8495f-a3fb-4d96-8640-72b764b41a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
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

_source line 6 · 2026-05-21T03:47:43.257Z_

<details><summary>↩ Tool result · `toolu_01Tvsba9Ho4T2rmHRXXqRHh1`</summary>

```text
artifacts/_project/report/literature_survey_d011.md
artifacts/_project/report/literature_survey_d011_167b57.md
artifacts/literature_survey_d011.md
literature_map.lock
literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57c8495f-a3fb-4d96-8640-72b764b41a12",
  "isSidechain": true,
  "promptId": "b7659c62-7248-4d0c-bac6-a05298eadbc6",
  "agentId": "a5a664161719b85a9",
  "type": "user",
  "uuid": "fc699435-6b26-449b-b6df-068205a8b302",
  "sourceToolAssistantUUID": "57c8495f-a3fb-4d96-8640-72b764b41a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T03:47:43.463Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MMRMSoY5VMVPVj6CNcnNwg`</summary>

```json
{
  "pattern": "**/literature.py",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc699435-6b26-449b-b6df-068205a8b302",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fMgg6GsDAgvtsE2Cq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7e1facc-d477-46c6-8544-7a28f9612fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
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

_source line 8 · 2026-05-21T03:47:43.531Z_

<details><summary>↩ Tool result · `toolu_01MMRMSoY5VMVPVj6CNcnNwg`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/literature.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7e1facc-d477-46c6-8544-7a28f9612fff",
  "isSidechain": true,
  "promptId": "b7659c62-7248-4d0c-bac6-a05298eadbc6",
  "agentId": "a5a664161719b85a9",
  "type": "user",
  "uuid": "37d9b26e-b983-412b-9799-ea667d448e9f",
  "sourceToolAssistantUUID": "c7e1facc-d477-46c6-8544-7a28f9612fff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T03:47:43.613Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UYxaktFa6a2WN9KwMQapsY`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"literature*\" -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37d9b26e-b983-412b-9799-ea667d448e9f",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fMgg6GsDAgvtsE2Cq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3755188e-28e3-4eb0-b855-17c37200f61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27702
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 342,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27702,
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

_source line 10 · 2026-05-21T03:47:43.851Z_

<details><summary>↩ Tool result · `toolu_01UYxaktFa6a2WN9KwMQapsY`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/__pycache__/literature.cpython-314.pyc
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/skills/global/literature-scan.skill.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3755188e-28e3-4eb0-b855-17c37200f61d",
  "isSidechain": true,
  "promptId": "b7659c62-7248-4d0c-bac6-a05298eadbc6",
  "agentId": "a5a664161719b85a9",
  "type": "user",
  "uuid": "4fe2a9d5-65c0-48b9-a446-72cf4871b034",
  "sourceToolAssistantUUID": "3755188e-28e3-4eb0-b855-17c37200f61d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T03:47:45.567Z_

Perfect! Now let me read the key files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fe2a9d5-65c0-48b9-a446-72cf4871b034",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fa44pE2TtSTLSkWfy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b751cee8-388b-49ef-8629-a5e4a1636e20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3RxNbnYv9wXBtkybk7yPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 27702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 12 · 2026-05-21T03:47:46.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HEneRTG7YQi7qxybzZuni1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b751cee8-388b-49ef-8629-a5e4a1636e20",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fa44pE2TtSTLSkWfy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "caa34e77-a7c3-4ed1-83c3-b19d3f7944c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3RxNbnYv9wXBtkybk7yPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 27702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 13 · 2026-05-21T03:47:46.473Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JLApBeVKFHKwvyL8wcb66F`</summary>

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
  "parentUuid": "caa34e77-a7c3-4ed1-83c3-b19d3f7944c2",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fa44pE2TtSTLSkWfy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af04debd-12d3-457c-9268-9337b49ee7b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3RxNbnYv9wXBtkybk7yPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 27702,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 154,
          "cache_read_input_tokens": 27702,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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

_source line 14 · 2026-05-21T03:47:46.517Z_

<details><summary>↩ Tool result · `toolu_01JLApBeVKFHKwvyL8wcb66F`</summary>

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
  "parentUuid": "af04debd-12d3-457c-9268-9337b49ee7b2",
  "isSidechain": true,
  "promptId": "b7659c62-7248-4d0c-bac6-a05298eadbc6",
  "agentId": "a5a664161719b85a9",
  "type": "user",
  "uuid": "c595bed7-5ecf-41e7-be15-3b0cd830a9e0",
  "sourceToolAssistantUUID": "af04debd-12d3-457c-9268-9337b49ee7b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T03:47:46.602Z_

<details><summary>↩ Tool result · `toolu_01HEneRTG7YQi7qxybzZuni1`</summary>

```text
1	categories:
2	- key: contamination_detection
3	  name: Benchmark Contamination Detection
4	  narrative: Methods for detecting training data contamination in LLM benchmarks,
5	    including RL-robust approaches
6	- key: irt_equating
7	  name: IRT Methodology & Equating
8	  narrative: Item Response Theory models, calibration, equating, and their application
9	    to LLM evaluation
10	- key: benchmark_design
11	  name: Dynamic Benchmark Design
12	  narrative: Approaches for creating contamination-resistant or self-updating benchmarks
13	- key: dif_methodology
14	  name: DIF Statistical Methods
15	  narrative: Differential Item Functioning detection methods, power analysis, and
16	    small-sample strategies
17	- key: item_generation
18	  name: Automated Item Generation
19	  narrative: LLM-based test item generation with difficulty control and psychometric
20	    validation
21	meta:
22	  last_updated: '2026-05-21T03:43:39.944Z'
23	  total_papers: 40
24	papers:
25	  balloccu2024leak:
26	    abstract: ''
27	    added_at: '2026-05-21T01:40:37.987Z'
28	    added_by: literature-gap-fill
29	    authors:
30	    - Balloccu, S.
31	    - Schmidtova, P.
32	    - Lango, M.
33	    - Dusek, O.
34	    bibtex_key: balloccu2024leak
35	    category: contamination_detection
36	    doi: 10.18653/v1/2024.eacl-long.5
37	    relevance: Systematic survey of data leakage in closed-source LLMs covering 255
38	      papers and 263 benchmarks; establishes scope of contamination problem motivating
39	      our detection approach
40	    role: foundation
41	    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056
42	    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in
43	      Closed-Source LLMs'
44	    url: https://arxiv.org/abs/2402.03927
45	    venue: EACL 2024
46	    verified: true
47	    year: 2024
48	  belzak2020smallsample:
49	    abstract: ''
50	    added_at: '2026-05-20T17:30:00.000Z'
51	    added_by: director
52	    authors:
53	    - Belzak, W.
54	    bibtex_key: belzak2020smallsample
55	    category: dif_methodology
56	    doi: 10.1080/00273171.2019.1671162
57	    relevance: Parsimonious logistic regression with sum scores outperforms complex
58	      IRT models for DIF detection in small samples; directly applicable to our N=50-80
59	      model cohorts
60	    role: method-component
61	    semantic_scholar_id: 8f13882b6f37be1ade68c40539156277e5723395
62	    title: Testing Differential Item Functioning in Small Samples
63	    url: https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162
64	    venue: Multivariate Behavioral Research
65	    verified: true
66	    year: 2020
67	  dekoninck2024constat:
68	    abstract: ''
69	    added_at: '2026-05-21T01:40:37.987Z'
70	    added_by: literature-gap-fill
71	    authors:
72	    - Dekoninck, J.
73	    - Mueller, M. N.
74	    - Vechev, M.
75	    bibtex_key: dekoninck2024constat
76	    category: contamination_detection
77	    doi: ''
78	    relevance: Performance-based contamination detection via perturbation analysis;
79	      closest methodological parallel to our DIF approach in using behavioral patterns
80	      rather than memorization signals
81	    role: direct-competitor
82	    semantic_scholar_id: ''
83	    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'
84	    url: https://arxiv.org/abs/2405.16281
85	    venue: NeurIPS 2024
86	    verified: true
87	    year: 2024
88	  golchin2024timetravel:
89	    abstract: ''
90	    added_at: '2026-05-21T01:40:37.987Z'
91	    added_by: literature-gap-fill
92	    authors:
93	    - Golchin, S.
94	    - Surdeanu, M.
95	    bibtex_key: golchin2024timetravel
96	    category: contamination_detection
97	    doi: ''
98	    relevance: Instance-level contamination detection via guided completion prompts;
99	      baseline approach for individual-item detection that our group-level DIF method
100	      extends
101	    role: method-component
102	    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404
103	    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'
104	    url: https://arxiv.org/abs/2308.08493
105	    venue: ICLR 2024
106	    verified: true
107	    year: 2024
108	  hardy2026scalability:
109	    abstract: ''
110	    added_at: '2026-05-20T17:30:00.000Z'
111	    added_by: director
112	    authors:
113	    - Hardy, M.
114	    - Gilbert, J.
115	    - Domingue, B.
116	    bibtex_key: hardy2026scalability
117	    category: irt_equating
118	    doi: 10.48550/arXiv.2603.24999
119	    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform
120	      IRT item diagnostics; lightweight pre-filter for item quality before our parametric
121	      calibration
122	    role: method-component
123	    semantic_scholar_id: ''
124	    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients
125	    url: https://arxiv.org/abs/2603.24999
126	    venue: arXiv
127	    verified: true
128	    year: 2026
129	  kim2019fpc:
130	    abstract: ''
131	    added_at: '2026-05-20T17:30:00.000Z'
132	    added_by: director
133	    authors:
134	    - Kim, S.
135	    - Kolen, M.
136	    bibtex_key: kim2019fpc
137	    category: irt_equating
138	    doi: 10.1080/08957347.2019.1660344
139	    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full
140	      calibration; core methodology for our bifactor IRT equating with anchor items
141	    role: method-component
142	    semantic_scholar_id: ''
143	    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data
144	    url: https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344
145	    venue: Applied Measurement in Education
146	    verified: true
147	    year: 2019
148	  li2024contamination:
149	    abstract: ''
150	    added_at: '2026-05-21T01:40:37.987Z'
151	    added_by: literature-gap-fill
152	    authors:
153	    - Li, Y.
154	    - Guo, Y.
155	    - Guerin, F.
156	    - Lin, C.
157	    bibtex_key: li2024contamination
158	    category: contamination_detection
159	    doi: 10.18653/v1/2024.findings-emnlp.30
160	    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks
161	      via Common Crawl matching; primary ground-truth comparison for our DIF-based
162	      contamination detection
163	    role: foundation
164	    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0
165	    title: An Open-Source Data Contamination Report for Large Language Models
166	    url: https://aclanthology.org/2024.findings-emnlp.30/
167	    venue: Findings of EMNLP 2024
168	    verified: true
169	    year: 2024
170	  liang2026dvd:
171	    abstract: ''
172	    added_at: '2026-05-20T17:30:00.000Z'
173	    added_by: director
174	    authors:
175	    - Liang, R.
176	    bibtex_key: liang2026dvd
177	    category: contamination_detection
178	    doi: ''
179	    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74
180	      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under
181	      RL training
182	    role: direct-competitor
183	    semantic_scholar_id: ''
184	    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'
185	    url: https://arxiv.org/abs/2601.04895
186	    venue: arXiv
187	    verified: true
188	    year: 2026
189	  shi2024mink:
190	    abstract: ''
191	    added_at: '2026-05-21T01:40:37.987Z'
192	    added_by: literature-gap-fill
193	    authors:
194	    - Shi, W.
195	    - Ajith, A.
196	    - Xia, M.
197	    - Huang, Y.
198	    - Liu, D.
199	    - Blevins, T.
200	    - Chen, D.
201	    - Zettlemoyer, L.
202	    bibtex_key: shi2024mink
203	    category: contamination_detection
204	    doi: ''
205	    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining
206	      data detection; key baseline whose limitations under RL training motivate our
207	      DIF-based alternative
208	    role: foundation
209	    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a
210	    title: Detecting Pretraining Data from Large Language Models
211	    url: https://arxiv.org/abs/2310.16789
212	    venue: ICLR 2024
213	    verified: true
214	    year: 2024
215	  tao2026selfcritique:
216	    abstract: ''
217	    added_at: '2026-05-20T17:30:00.000Z'
218	    added_by: director
219	    authors:
220	    - Tao, Y.
221	    bibtex_key: tao2026selfcritique
222	    category: contamination_detection
223	    doi: ''
224	    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse
225	      detection, but remains individual-model-level; our DIF is group-level and complementary
226	    role: direct-competitor
227	    semantic_scholar_id: ''
228	    title: Detecting Data Contamination from Reinforcement Learning Post-training
229	      for Large Language Models
230	    url: https://arxiv.org/abs/2510.09259
231	    venue: ICLR 2026
232	    verified: true
233	    year: 2026
234	  wang2026fragility:
235	    abstract: ''
236	    added_at: '2026-05-20T17:30:00.000Z'
237	    added_by: director
238	    authors:
239	    - Wang, H.
240	    - Li, H.
241	    - Ko, B.
242	    - Zhang, H.
243	    bibtex_key: wang2026fragility
244	    category: contamination_detection
245	    doi: ''
246	    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp
247	      AUROC degradation), motivating our DIF-based approach which operates on behavioral
248	      patterns immune to NLL smoothing
249	    role: foundation
250	    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3
251	    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models
252	    url: https://arxiv.org/abs/2510.02386
253	    venue: ICLR 2026
254	    verified: true
255	    year: 2026
256	  white2025livebench:
257	    abstract: ''
258	    added_at: '2026-05-20T17:30:00.000Z'
259	    added_by: director
260	    authors:
261	    - White, C.
262	    bibtex_key: white2025livebench
263	    category: benchmark_design
264	    doi: 10.48550/arXiv.2406.19314
265	    relevance: Monthly-updated contamination-free benchmark with objective scoring;
266	      no difficulty calibration or psychometric equivalence across updates
267	    role: direct-competitor
268	    semantic_scholar_id: 4e5d86ea8eacd341d13123852d50d1ef62738744
269	    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'
270	    url: https://arxiv.org/abs/2406.19314
271	    venue: ICLR 2025
272	    verified: true
273	    year: 2025
274	  zhang2024gsm1k:
275	    abstract: ''
276	    added_at: '2026-05-20T17:30:00.000Z'
277	    added_by: director
278	    authors:
279	    - Zhang, H.
280	    bibtex_key: zhang2024gsm1k
281	    category: contamination_detection
282	    doi: ''
283	    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides
284	      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4
285	      logits) critical for our DIF power analysis
286	    role: foundation
287	    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f
288	    title: A Careful Examination of Large Language Model Performance on Grade School
289	      Arithmetic
290	    url: https://arxiv.org/abs/2405.00332
291	    venue: arXiv
292	    verified: true
293	    year: 2024
294	  zhang2024minkpp:
295	    abstract: ''
296	    added_at: '2026-05-21T01:40:37.987Z'
297	    added_by: literature-gap-fill
298	    authors:
299	    - Zhang, J.
300	    - Sun, J.
301	    - Yeats, E.
302	    - Ouyang, Y.
303	    - Kuo, M.
304	    - Zhang, J.
305	    - Yang, H.
306	    - Li, H.
307	    bibtex_key: zhang2024minkpp
308	    category: contamination_detection
309	    doi: ''
310	    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key
311	      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our
312	      DIF-based alternative
313	    role: direct-competitor
314	    semantic_scholar_id: ''
315	    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large
316	      Language Models'
317	    url: https://arxiv.org/abs/2404.02936
318	    venue: arXiv
319	    verified: true
320	    year: 2024
321	  lalor2019irt:
322	    title: 'Learning Latent Parameters without Human Response Patterns: Item Response
323	      Theory with Artificial Crowds'
324	    authors:
325	    - Lalor, J.
326	    - Wu, H.
327	    - Yu, H.
328	    year: 2019
329	    venue: EMNLP-IJCNLP 2019
330	    url: https://aclanthology.org/D19-1434/
331	    doi: 10.18653/v1/D19-1434
332	    bibtex_key: lalor2019irt
333	    category: irt_equating
334	    role: foundation
335	    relevance: Pioneering application of IRT to NLP evaluation using artificial crowds
336	      of DNN models; establishes that IRT parameters from machine response patterns
337	      correlate with human-calibrated parameters
338	    abstract: ''
339	    semantic_scholar_id: df6cd8a8d836e75690141deb732f6d19f0176a2e
340	    verified: true
341	    added_by: literature-gap-fill
342	    added_at: '2026-05-21T02:29:19.632Z'
343	  vania2021irt:
344	    title: Comparing Test Sets with Item Response Theory
345	    authors:
346	    - Vania, C.
347	    - Htut, P.M.
348	    - Huang, W.
349	    - Mungra, D.
350	    - Pang, R.Y.
351	    - Phang, J.
352	    - Liu, H.
353	    - Cho, K.
354	    - Bowman, S.R.
355	    year: 2021
356	    venue: ACL 2021
357	    url: https://aclanthology.org/2021.acl-long.92/
358	    doi: 10.18653/v1/2021.acl-long.92
359	    bibtex_key: vania2021irt
360	    category: irt_equating
361	    role: foundation
362	    relevance: IRT-based analysis of NLU benchmark discriminability; shows which test
363	      sets remain effective at differentiating strong models and which are saturated
364	    abstract: ''
365	    semantic_scholar_id: 4ca39cf99747b8962fe37e7e025e284872df3425
366	    verified: true
367	    added_by: literature-gap-fill
368	    added_at: '2026-05-21T02:29:19.632Z'
369	  li2025atlas:
370	    title: 'Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static
371	      Benchmarks'
372	    authors:
373	    - Li, P.
374	    - Tang, X.
375	    - Chen, S.
376	    - Cheng, Y.
377	    - Metoyer, R.
378	    - Hua, T.
379	    - Chawla, N.V.
380	    year: 2025
381	    venue: arXiv
382	    url: https://arxiv.org/abs/2511.04689
383	    doi: 10.48550/arXiv.2511.04689
384	    bibtex_key: li2025atlas
385	    category: irt_equating
386	    role: method-component
387	    relevance: IRT-based adaptive testing framework (ATLAS) reduces benchmark items
388	      by 90% while preserving ability estimates; demonstrates IRT enables efficient
389	      LLM evaluation
390	    abstract: ''
391	    semantic_scholar_id: 087ce2837a0d5562bc95a40e77a327a6d033366c
392	    verified: true
393	    added_by: literature-gap-fill
394	    added_at: '2026-05-21T02:29:19.632Z'
395	  chen2025irtnet:
396	    title: Learning Compact Representations of LLM Abilities via Item Response Theory
397	    authors:
398	    - Chen, J.
399	    - Wang, C.
400	    - Zhang, G.
401	    - Ye, P.
402	    - Bai, L.
403	    - Hu, W.
404	    - Qu, Y.
405	    - Hu, S.
406	    year: 2025
407	    venue: arXiv
408	    url: https://arxiv.org/abs/2510.00844
409	    doi: 10.48550/arXiv.2510.00844
410	    bibtex_key: chen2025irtnet
411	    category: irt_equating
412	    role: method-component
413	    relevance: Multidimensional IRT with MoE network for learning LLM ability vectors
414	      and query discrimination/difficulty; demonstrates IRT-based model routing and
415	      benchmark prediction
416	    abstract: ''
417	    semantic_scholar_id: ''
418	    verified: true
419	    added_by: literature-gap-fill
420	    added_at: '2026-05-21T02:29:19.632Z'
421	  choi2026llmjudgeirt:
422	    title: Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
423	    authors:
424	    - Choi, J.
425	    - Park, S.
426	    - Cho, C.
427	    - Park, H.
428	    - Kim, B.
429	    year: 2026
430	    venue: arXiv
431	    url: https://arxiv.org/abs/2602.00521
432	    doi: 10.48550/arXiv.2602.00521
433	    bibtex_key: choi2026llmjudgeirt
434	    category: irt_equating
435	    role: method-component
436	    relevance: Applies IRT Graded Response Model to diagnose LLM judge reliability;
437	      extends IRT application beyond benchmark scoring to evaluation pipeline quality
438	      assessment
439	    abstract: ''
440	    semantic_scholar_id: 4fc931a456c8162716deadbc9db6fd770189e632
441	    verified: true
442	    added_by: literature-gap-fill
443	    added_at: '2026-05-21T02:29:19.632Z'
444	  holland1988mh:
445	    title: Differential Item Functioning and the Mantel-Haenszel Procedure
446	    authors:
447	    - Holland, P.W.
448	    - Thayer, D.T.
449	    year: 1988
450	    venue: In H. Wainer & H.I. Braun (Eds.), Test Validity, Lawrence Erlbaum
451	    url: https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x
452	    doi: 10.1002/j.2330-8516.1986.tb00186.x
453	    bibtex_key: holland1988mh
454	    category: dif_methodology
455	    role: foundation
456	    relevance: Seminal paper introducing the Mantel-Haenszel procedure for DIF detection;
457	      establishes the ETS classification system (A/B/C) used as standard DIF effect-size
458	      metric
459	    abstract: ''
460	    semantic_scholar_id: 5fbc064e7104036b77a2bf6f0ad509031965c275
461	    verified: true
462	    added_by: literature-gap-fill
463	    added_at: '2026-05-21T03:21:36.315Z'
464	  shealy1993sibtest:
465	    title: A Model-Based Standardization Approach that Separates True Bias/DIF from
466	      Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF
467	    authors:
468	    - Shealy, R.
469	    - Stout, W.
470	    year: 1993
471	    venue: Psychometrika
472	    url: https://link.springer.com/article/10.1007/BF02294572
473	    doi: 10.1007/BF02294572
474	    bibtex_key: shealy1993sibtest
475	    category: dif_methodology
476	    role: foundation
477	    relevance: Introduces SIBTEST, a nonparametric DIF detection method that separates
478	      true item bias from group ability differences; alternative to MH that handles
479	      non-uniform DIF
480	    abstract: ''
481	    semantic_scholar_id: 82f3db496626afd828fedb01a41f719a50dbfc2c
482	    verified: true
483	    added_by: literature-gap-fill
484	    added_at: '2026-05-21T03:21:36.315Z'
485	  clauser1998dif:
486	    title: Using Statistical Procedures to Identify Differentially Functioning Test
487	      Items
488	    authors:
489	    - Clauser, B.E.
490	    - Mazor, K.M.
491	    year: 1998
492	    venue: 'Educational Measurement: Issues and Practice'
493	    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x
494	    doi: 10.1111/j.1745-3992.1998.tb00619.x
495	    bibtex_key: clauser1998dif
496	    category: dif_methodology
497	    role: foundation
498	    relevance: Comprehensive review of DIF detection methods (MH, SIBTEST, logistic
499	      regression, IRT-based); standard reference for comparing statistical approaches
500	      to DIF
501	    abstract: ''
502	    semantic_scholar_id: c2377c505c95b924e972e61dadec81e9c87dea18
503	    verified: true
504	    added_by: literature-gap-fill
505	    added_at: '2026-05-21T03:21:36.315Z'
506	  zumbo1999handbook:
507	    title: 'A Handbook on the Theory and Methods of Differential Item Functioning
508	      (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type
509	      (Ordinal) Item Scores'
510	    authors:
511	    - Zumbo, B.D.
512	    year: 1999
513	    venue: 'Ottawa: Directorate of Human Resources Research and Evaluation, Department
514	      of National Defense'
515	    url: https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf
516	    doi: ''
517	    bibtex_key: zumbo1999handbook
518	    category: dif_methodology
519	    role: foundation
520	    relevance: Foundational DIF handbook presenting logistic regression as a unitary
521	      framework for DIF analysis; establishes the Zumbo-Thomas logistic regression
522	      approach widely used in applied DIF research
523	    abstract: ''
524	    semantic_scholar_id: 7f88fb0ad98645582665532600d7c46406fa2db6
525	    verified: true
526	    added_by: literature-gap-fill
527	    added_at: '2026-05-21T03:21:36.315Z'
528	  meredith1993invariance:
529	    title: Measurement Invariance, Factor Analysis and Factorial Invariance
530	    authors:
531	    - Meredith, W.
532	    year: 1993
533	    venue: Psychometrika
534	    url: https://link.springer.com/article/10.1007/BF02294825
535	    doi: 10.1007/BF02294825
536	    bibtex_key: meredith1993invariance
537	    category: dif_methodology
538	    role: foundation
539	    relevance: Defines the measurement invariance hierarchy (configural, metric, scalar,
540	      strict factorial invariance); theoretical foundation linking DIF to latent variable
541	      fairness
542	    abstract: ''
543	    semantic_scholar_id: 7eb541983de0a39586a699e255563b26e9291340
544	    verified: true
545	    added_by: literature-gap-fill
546	    added_at: '2026-05-21T03:21:36.315Z'
547	  vandenberg2000invariance:
548	    title: 'A Review and Synthesis of the Measurement Invariance Literature: Suggestions,
549	      Practices, and Recommendations for Organizational Research'
550	    authors:
551	    - Vandenberg, R.J.
552	    - Lance, C.E.
553	    year: 2000
554	    venue: Organizational Research Methods
555	    url: https://journals.sagepub.com/doi/10.1177/109442810031002
556	    doi: 10.1177/109442810031002
557	    bibtex_key: vandenberg2000invariance
558	    category: dif_methodology
559	    role: foundation
560	    relevance: Comprehensive review of measurement invariance testing practices; establishes
561	      CFA-based invariance testing as prerequisite for valid cross-group comparisons,
562	      analogous to our cross-model DIF analysis
563	    abstract: ''
564	    semantic_scholar_id: 1c9389250c1fac06eda5dcf39a8ea16cf8c92c89
565	    verified: true
566	    added_by: literature-gap-fill
567	    added_at: '2026-05-21T03:21:36.315Z'
568	  swaminathan1990logistic:
569	    title: Detecting Differential Item Functioning Using Logistic Regression Procedures
570	    authors:
571	    - Swaminathan, H.
572	    - Rogers, H.J.
573	    year: 1990
574	    venue: Journal of Educational Measurement
575	    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x
576	    doi: 10.1111/j.1745-3984.1990.tb00754.x
577	    bibtex_key: swaminathan1990logistic
578	    category: dif_methodology
579	    role: foundation
580	    relevance: Introduces logistic regression for DIF detection, distinguishing uniform
581	      and non-uniform DIF; more powerful than MH for non-uniform DIF and directly
582	      applicable to our contamination-as-DIF framework
583	    abstract: ''
584	    semantic_scholar_id: d14b3b6e927ff8e51406fad1010244ecabc07da0
585	    verified: true
586	    added_by: literature-gap-fill
587	    added_at: '2026-05-21T03:21:36.315Z'
588	  teresi2007dif:
589	    title: Differential Item Functioning and Health Assessment
590	    authors:
591	    - Teresi, J.A.
592	    - Fleishman, J.A.
593	    year: 2007
594	    venue: Quality of Life Research
595	    url: https://link.springer.com/article/10.1007/s11136-007-9184-6
596	    doi: 10.1007/s11136-007-9184-6
597	    bibtex_key: teresi2007dif
598	    category: dif_methodology
599	    role: method-component
600	    relevance: Reviews DIF detection strategies including propensity score matching
601	      approaches for controlling confounders; methodological basis for our propensity-matched
602	      contamination group comparison
603	    abstract: ''
604	    semantic_scholar_id: 5ddbe080c2c0cdff671d9b9c2a795e366b6eb098
605	    verified: true
606	    added_by: literature-gap-fill
607	    added_at: '2026-05-21T03:21:36.315Z'
608	  lord1980irt:
609	    title: Applications of Item Response Theory to Practical Testing Problems
610	    authors:
611	    - Lord, F.M.
612	    year: 1980
613	    venue: 'Hillsdale, NJ: Lawrence Erlbaum Associates'
614	    url: https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067
615	    doi: ''
616	    bibtex_key: lord1980irt
617	    category: dif_methodology
618	    role: foundation
619	    relevance: Introduces Lord's chi-square test for IRT-based DIF detection by comparing
620	      item parameters across groups; foundational IRT reference for our parametric
621	      DIF approach
622	    abstract: ''
623	    semantic_scholar_id: ''
624	    verified: true
625	    added_by: literature-gap-fill
626	    added_at: '2026-05-21T03:21:36.315Z'
627	  raju1988area:
628	    title: The Area between Two Item Characteristic Curves
629	    authors:
630	    - Raju, N.S.
631	    year: 1988
632	    venue: Psychometrika
633	    url: https://link.springer.com/article/10.1007/BF02294403
634	    doi: 10.1007/BF02294403
635	    bibtex_key: raju1988area
636	    category: dif_methodology
637	    role: method-component
638	    relevance: Develops signed and unsigned area measures between item characteristic
639	      curves for IRT-based DIF quantification; provides effect-size metrics complementing
640	      statistical significance tests
641	    abstract: ''
642	    semantic_scholar_id: 545c20c1f2575833f81418f4757cb78446465cd7
643	    verified: true
644	    added_by: literature-gap-fill
645	    added_at: '2026-05-21T03:21:36.315Z'
646	  muthen1985mimic:
647	    title: A Method for Studying the Homogeneity of Test Items with Respect to Other
648	      Relevant Variables
649	    authors:
650	    - Muthén, B.
651	    year: 1985
652	    venue: Journal of Educational Statistics
653	    url: ''
654	    doi: 10.2307/1164966
655	    bibtex_key: muthen1985mimic
656	    category: dif_methodology
657	    role: method-component
658	    relevance: Seminal MIMIC model for DIF with continuous covariates; future-work
659	      alternative to failed θ-conditioning (plan_012)
660	    abstract: ''
661	    semantic_scholar_id: ''
662	    verified: true
663	    added_by: paper_agent
664	    added_at: '2026-05-21T03:34:08.189Z'
665	  woods2009mimic:
666	    title: Empirical Selection of Anchors for Tests of Differential Item Functioning
667	    authors:
668	    - Woods, C.M.
669	    year: 2009
670	    venue: Applied Psychological Measurement
671	    url: ''
672	    doi: 10.1177/0146621609331279
673	    bibtex_key: woods2009mimic
674	    category: dif_methodology
675	    role: method-component
676	    relevance: Modern MIMIC-based DIF detection with anchor selection; addresses impact-vs-DIF
677	      confound in our future work
678	    abstract: ''
679	    semantic_scholar_id: ''
680	    verified: true
681	    added_by: paper_agent
682	    added_at: '2026-05-21T03:34:08.189Z'
683	  habba2026growingpains:
684	    abstract: ''
685	    added_at: '2026-05-20T17:30:00.000Z'
686	    added_by: director
687	    authors:
688	    - Habba, E.
689	    - Itzhak, I.
690	    - Yehudai, A.
691	    - Perlitz, Y.
692	    - Bandel, E.
693	    - Shmueli-Scheuer, M.
694	    - Choshen, L.
695	    - Stanovsky, G.
696	    bibtex_key: habba2026growingpains
697	    category: irt_equating
698	    doi: 10.48550/arXiv.2604.12843
699	    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100
700	      anchor items for extensible evaluation (rho>=0.9); addresses score comparability
701	      but NOT contamination detection or item regeneration
702	    role: direct-competitor
703	    semantic_scholar_id: ''
704	    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter
705	      Calibration'
706	    url: https://arxiv.org/abs/2604.12843
707	    venue: arXiv
708	    verified: true
709	    year: 2026
710	  zhou2026psnirt:
711	    abstract: ''
712	    added_at: '2026-05-20T17:30:00.000Z'
713	    added_by: director
714	    authors:
715	    - Zhou, H.
716	    - Huang, H.
717	    - Zhao, Z.
718	    - Han, L.
719	    - Wang, H.
720	    - Chen, K.
721	    - Yang, M.
722	    - Bao, W.
723	    - Dong, J.
724	    - Xu, B.
725	    - Zhu, C.
726	    - Cao, H.
727	    - Zhao, T.
728	    bibtex_key: zhou2026psnirt
729	    category: irt_equating
730	    doi: ''
731	    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published
732	      IRT parameters for MMLU we can use in semi-synthetic validation
733	    role: method-component
734	    semantic_scholar_id: ''
735	    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item
736	      Response Theory
737	    url: https://arxiv.org/abs/2505.15055
738	    venue: AAAI 2026
739	    verified: true
740	    year: 2026
741	  kipnis2024metabench:
742	    title: metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language
743	      Models
744	    authors:
745	    - Kipnis, A.
746	    - Voudouris, K.
747	    - Schulze Buschoff, L.M.
748	    - Schulz, E.
749	    year: 2024
750	    venue: arXiv
751	    url: https://arxiv.org/abs/2407.12844
752	    doi: 10.48550/arXiv.2407.12844
753	    bibtex_key: kipnis2024metabench
754	    category: benchmark_design
755	    role: foundation
756	    relevance: Primary data source providing item-level response matrix across 5000+
757	      LLMs on 6 benchmarks; IRT-based item selection methodology enables our DIF analysis
758	      on compressed benchmark items
759	    abstract: ''
760	    semantic_scholar_id: dfd5186def202285a0f23cd3f08415a5780895c1
761	    verified: true
762	    added_by: literature-gap-fill
763	    added_at: '2026-05-21T03:43:39.896Z'
764	  hendrycks2021mmlu:
765	    title: Measuring Massive Multitask Language Understanding
766	    authors:
767	    - Hendrycks, D.
768	    - Burns, C.
769	    - Basart, S.
770	    - Zou, A.
771	    - Mazeika, M.
772	    - Song, D.
773	    - Steinhardt, J.
774	    year: 2021
775	    venue: ICLR 2021
776	    url: https://arxiv.org/abs/2009.03300
777	    doi: ''
778	    bibtex_key: hendrycks2021mmlu
779	    category: benchmark_design
780	    role: foundation
781	    relevance: Seminal 57-subject benchmark for LLM evaluation; primary benchmark
782	      in our DIF analysis due to documented contamination and available IRT parameters
783	    abstract: ''
784	    semantic_scholar_id: 814a4f680b9ba6baba23b93499f4b48af1a27678
785	    verified: true
786	    added_by: literature-gap-fill
787	    added_at: '2026-05-21T03:43:39.896Z'
788	  liang2023helm:
789	    title: Holistic Evaluation of Language Models
790	    authors:
791	    - Liang, P.
792	    - Bommasani, R.
793	    - Lee, T.
794	    - Tsipras, D.
795	    - Soylu, D.
796	    - Yasunaga, M.
797	    - Zhang, Y.
798	    - Narayanan, D.
799	    - Wu, Y.
800	    - Kumar, A.
801	    year: 2023
802	    venue: TMLR 2023
803	    url: https://arxiv.org/abs/2211.09110
804	    doi: 10.1111/nyas.15007
805	    bibtex_key: liang2023helm
806	    category: benchmark_design
807	    role: foundation
808	    relevance: Holistic multi-metric evaluation framework covering accuracy, calibration,
809	      robustness, fairness, and bias; establishes multi-dimensional evaluation philosophy
810	      complementary to our psychometric approach
811	    abstract: ''
812	    semantic_scholar_id: ce913026f693101e54d3ab9152e107034d81fce1
813	    verified: true
814	    added_by: literature-gap-fill
815	    added_at: '2026-05-21T03:43:39.896Z'
816	  chiang2024chatbot:
817	    title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'
818	    authors:
819	    - Chiang, W.-L.
820	    - Zheng, L.
821	    - Sheng, Y.
822	    - Angelopoulos, A.N.
823	    - Li, T.
824	    - Li, D.
825	    - Zhang, H.
826	    - Zhu, B.
827	    - Jordan, M.I.
828	    - Gonzalez, J.E.
829	    - Stoica, I.
830	    year: 2024
831	    venue: ICML 2024
832	    url: https://arxiv.org/abs/2403.04132
833	    doi: 10.48550/arXiv.2403.04132
834	    bibtex_key: chiang2024chatbot
835	    category: benchmark_design
836	    role: method-component
837	    relevance: Crowdsourced pairwise comparison with ELO ranking as contamination-resistant
838	      alternative to static benchmarks; contrasts with our item-level psychometric
839	      approach
840	    abstract: ''
841	    semantic_scholar_id: 53f4fb0e9972989194368faf288ff8e3cba5bd60
842	    verified: true
843	    added_by: literature-gap-fill
844	    added_at: '2026-05-21T03:43:39.896Z'
845	  mialon2023gaia:
846	    title: 'GAIA: a benchmark for General AI Assistants'
847	    authors:
848	    - Mialon, G.
849	    - Fourrier, C.
850	    - Swift, C.
851	    - Wolf, T.
852	    - LeCun, Y.
853	    - Scialom, T.
854	    year: 2023
855	    venue: arXiv
856	    url: https://arxiv.org/abs/2311.12983
857	    doi: 10.48550/arXiv.2311.12983
858	    bibtex_key: mialon2023gaia
859	    category: benchmark_design
860	    role: method-component
861	    relevance: Benchmark with verifiable ground-truth answers designed to resist memorization;
862	      exemplifies objective-scoring benchmark design philosophy shared by our regenerated
863	      items
864	    abstract: ''
865	    semantic_scholar_id: ab8169d6e4dfabfe7c30ebec1bb871bf3e1551cd
866	    verified: true
867	    added_by: literature-gap-fill
868	    added_at: '2026-05-21T03:43:39.896Z'
869	  li2024latesteval:
870	    title: 'LatestEval: Addressing Data Contamination in Language Model Evaluation
871	      through Dynamic and Time-Sensitive Test Construction'
872	    authors:
873	    - Li, Y.
874	    - Guerin, F.
875	    - Lin, C.
876	    year: 2024
877	    venue: AAAI 2024
878	    url: https://arxiv.org/abs/2312.12343
879	    doi: 10.48550/arXiv.2312.12343
880	    bibtex_key: li2024latesteval
881	    category: benchmark_design
882	    role: direct-competitor
883	    relevance: Automated dynamic test construction from recent texts to avoid contamination;
884	      addresses temporal contamination but lacks psychometric difficulty calibration
885	      across test versions
886	    abstract: ''
887	    semantic_scholar_id: 8106d03fb984afd8c3d066cd4f993eb2616a0da5
888	    verified: true
889	    added_by: literature-gap-fill
890	    added_at: '2026-05-21T03:43:39.896Z'
891	  kiela2021dynabench:
892	    title: 'Dynabench: Rethinking Benchmarking in NLP'
893	    authors:
894	    - Kiela, D.
895	    - Bartolo, M.
896	    - Nie, Y.
897	    - Kaushik, D.
898	    - Geiger, A.
899	    - Wu, Z.
900	    - Vidgen, B.
901	    - Prasad, G.
902	    - Singh, A.
903	    - Ringshia, P.
904	    - Ma, Z.
905	    - Thrush, T.
906	    - Riedel, S.
907	    - Talat, Z.
908	    - Stenetorp, P.
909	    - Jia, R.
910	    year: 2021
911	    venue: NAACL 2021
912	    url: https://arxiv.org/abs/2104.14337
913	    doi: 10.18653/v1/2021.naacl-main.324
914	    bibtex_key: kiela2021dynabench
915	    category: benchmark_design
916	    role: foundation
917	    relevance: Seminal dynamic adversarial benchmarking platform with human-and-model-in-the-loop
918	      dataset creation; establishes the paradigm of continuously evolving benchmarks
919	      that our IRT-equated regeneration extends with psychometric equivalence guarantees
920	    abstract: ''
921	    semantic_scholar_id: 77a096d80eb4dd4ccd103d1660c5a5498f7d026b
922	    verified: true
923	    added_by: literature-gap-fill
924	    added_at: '2026-05-21T03:43:39.896Z'
925	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa34e77-a7c3-4ed1-83c3-b19d3f7944c2",
  "isSidechain": true,
  "promptId": "b7659c62-7248-4d0c-bac6-a05298eadbc6",
  "agentId": "a5a664161719b85a9",
  "type": "user",
  "uuid": "f025be82-87ac-46b6-9c53-12931e6ce645",
  "sourceToolAssistantUUID": "caa34e77-a7c3-4ed1-83c3-b19d3f7944c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-21T03:47:56.694Z_

Perfect! I've found and analyzed both files. Here's my report:

## Summary

**Files Found:**

1. **Project literature_map.yaml**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml`
   - Contains 40 verified papers across 5 categories
   - Last updated: 2026-05-21T03:43:39.944Z
   - Categories: contamination_detection, irt_equating, benchmark_design, dif_methodology, item_generation

2. **Literature module**: `/home/ubuntu/agent-ml-research/core/tools/literature.py`
   - Core implementation (~640 lines)
   - Provides persistent, atomic literature map management

## Key Implementation Details

**Data Structure** (literature_map.yaml):
- `meta`: last_updated timestamp, total_papers count
- `categories`: list of {key, name, narrative} for Related Work subsections
- `papers`: dict with entries keyed by bibtex_key (e.g., `balloccu2024leak`)

**Paper Record Schema** (per entry):
- Core metadata: title, authors[], year, venue, url, doi, bibtex_key
- Classification: category, role (foundation|direct-competitor|method-component|evaluation|background), verified
- Research context: relevance, abstract, semantic_scholar_id
- Provenance: added_by, added_at timestamp, optional source_idea_id

**API Functions** (literature.py):
- `read_literature_map(project, mode)` — supports modes: summary, category:X, competitors, unverified, bib, full
- `add_to_literature_map(project, papers, added_by)` — dedup via DOI (exact) or normalized title
- `update_literature_category(paper_key, category, role, relevance, verified)` — partial updates
- `upsert_category(key, name, narrative)` — manage Related Work sections
- `seed_literature_map(project, seed_papers, source_idea_id)` — bulk-seed from ideas

**File I/O** (robust):
- Atomic reads via snapshot mechanism (no tearing under concurrent writes)
- Exclusive flock on .lock file + atomic temp→rename for writers
- Automatic merging (fill-empty-slots, never overwrite) when duplicate detected

**Dedup Strategy**:
- Match order: DOI exact (normalized) → normalized title → bibtex_key collision suffix
- Normalization: lowercase, diacritics removed, punctuation→spaces, whitespace collapsed

The project's 40 papers span contamination detection (Min-K%, DIF methods), IRT equating (fixed-parameter calibration), benchmark design (MMLU, LiveBench), and DIF statistical foundations (Mantel-Haenszel, logistic regression).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f025be82-87ac-46b6-9c53-12931e6ce645",
  "isSidechain": true,
  "agentId": "a5a664161719b85a9",
  "requestId": "req_011CbF2fmuhJXJk8sKHo4fxV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2646387-7762-4712-9c26-26f9889370bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011Dd6K516fSnYKPqogJFv55",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7786,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 29134,
      "output_tokens": 685,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13095
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7786,
          "output_tokens": 685,
          "cache_read_input_tokens": 29134,
          "cache_creation_input_tokens": 13095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13095,
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
