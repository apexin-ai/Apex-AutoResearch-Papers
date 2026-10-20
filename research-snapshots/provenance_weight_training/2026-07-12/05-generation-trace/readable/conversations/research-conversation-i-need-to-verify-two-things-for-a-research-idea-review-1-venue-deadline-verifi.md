# Research conversation: I need to verify two things for a research idea review: **1. Venue deadline verification:** Search for the following ven

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a88534961460cf29b.jsonl`
- **Structured JSON:** [`7ae167ea10e859616548.json`](../../sessions/7a/7ae167ea10e859616548.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-13T05:45:33.353Z_

I need to verify two things for a research idea review:

**1. Venue deadline verification:**
Search for the following venue deadlines:
- ICLR 2027 submission deadline (search "ICLR 2027 deadline" or "ICLR 2027 call for papers")
- ICRA 2027 submission deadline (search "ICRA 2027 deadline")
- CoRL 2027 submission deadline (search "CoRL 2027 deadline")
Today's date is 2026-05-13. Are these deadlines all after today?

**2. Current SOTA on VLA benchmarks:**
Search for the current state-of-the-art on:
- SimplerEnv benchmark for VLA models (especially OOD/visual variant results)
- LIBERO benchmark suite for VLA models (what's the current top score?)
- What are the latest VLA models (2025-2026) and their performance?
Search: "SimplerEnv VLA benchmark 2026", "LIBERO VLA success rate 2026", "VLA model state of the art 2026"
- Is LIBERO really saturated at ~97% as claimed?
- What is the current best on SimplerEnv OOD visual variants?

**3. Check if the previously flagged "fabricated" references are now correctly handled:**
- Is FAN (arXiv 2604.01570) a real paper? Search specifically for arXiv ID 2604.01570
- Is GridS/"See What Matters" (ICML 2026) a real paper? Search "See What Matters differentiable grid sample pruning VLA"

Report all findings with sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "80e007b4-9677-4c29-994c-c32398b085cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T05:45:33.358Z_

```json
{
  "parentUuid": "80e007b4-9677-4c29-994c-c32398b085cf",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e2c533a4-8036-4b10-bc06-2f306136f960",
  "timestamp": "2026-05-13T05:45:33.358Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T05:45:37.554Z_



I'll search for all of these in parallel. Let me start by loading the WebSearch tool and then conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2c533a4-8036-4b10-bc06-2f306136f960",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3BNKtyA9fCwfkiR8X6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cdf9874-28f0-48be-a242-68696814eea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jrk3M2rhujtwZWRP8J4DD4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 917,
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

_source line 4 · 2026-05-13T05:45:38.150Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EWhgMQF5zX7Lrn3qUySUyz`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cdf9874-28f0-48be-a242-68696814eea7",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3BNKtyA9fCwfkiR8X6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a912eab6-cb43-456d-9f54-0c6db8d57faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jrk3M2rhujtwZWRP8J4DD4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 7304,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 917,
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

_source line 5 · 2026-05-13T05:45:38.152Z_

<details><summary>↩ Tool result · `toolu_01EWhgMQF5zX7Lrn3qUySUyz`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a912eab6-cb43-456d-9f54-0c6db8d57faa",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "e1cf332d-572d-4697-a3e9-f6d5f0e31c89",
  "sourceToolAssistantUUID": "a912eab6-cb43-456d-9f54-0c6db8d57faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T05:45:40.554Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1cf332d-572d-4697-a3e9-f6d5f0e31c89",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc8b5091-bfc8-4aca-a500-820a242457b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 7 · 2026-05-13T05:45:41.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DnhP3hWauD2c8MWviWedkx`</summary>

```json
{
  "query": "ICLR 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc8b5091-bfc8-4aca-a500-820a242457b9",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae31c0eb-c6dd-4253-aa54-7bde9af630db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 8 · 2026-05-13T05:45:41.644Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4LwmiwkCjCKGrk2qbnkZ1`</summary>

```json
{
  "query": "ICRA 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae31c0eb-c6dd-4253-aa54-7bde9af630db",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c145ee65-1ff4-4bc2-a934-542880bda996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 9 · 2026-05-13T05:45:42.045Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01114suX3BUcY2hKTm1zY9hq`</summary>

```json
{
  "query": "CoRL 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c145ee65-1ff4-4bc2-a934-542880bda996",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8866548-968d-47fc-a8ce-0f7a40609ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 10 · 2026-05-13T05:45:42.983Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011QG8CcsukaNKmTJKvr35uo`</summary>

```json
{
  "query": "SimplerEnv VLA benchmark 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8866548-968d-47fc-a8ce-0f7a40609ce2",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44e5672d-cee6-4813-8a1c-086c71d65448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 11 · 2026-05-13T05:45:43.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SKGkKGt6brjecqUVhYpzXk`</summary>

```json
{
  "query": "LIBERO VLA benchmark success rate 2026 state of the art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44e5672d-cee6-4813-8a1c-086c71d65448",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1369ef7f-47d8-4399-a463-0cc52f76c7cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 12 · 2026-05-13T05:45:43.926Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VsQmFSpzphqu5Eho3vDXeh`</summary>

```json
{
  "query": "VLA model state of the art 2025 2026 vision language action"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1369ef7f-47d8-4399-a463-0cc52f76c7cb",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83c8f297-e43e-433b-bc86-71ab2ad4a2b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 13 · 2026-05-13T05:45:44.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHTnz5P4HsrXdJYfLYAHvt`</summary>

```json
{
  "query": "arXiv 2604.01570 FAN paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83c8f297-e43e-433b-bc86-71ab2ad4a2b9",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bffe5d28-6b4a-48a1-9bea-b7d3a597a8fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1915,
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

_source line 14 · 2026-05-13T05:45:44.966Z_

<details><summary>↩ Tool result · `toolu_01A4LwmiwkCjCKGrk2qbnkZ1`</summary>

```text
Web search results for query: "ICRA 2027 submission deadline"

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"Conference Calender 2027 in Kanazawa Institute of Technology","url":"https://wwwr.kanazawa-it.ac.jp/kawai/calendar/2027/cal27.html"},{"title":"ICRA 2030: Submit Your Proposal! The IEEE #Robotics ...","url":"https://www.facebook.com/ieee.ras/posts/icra-2030-submit-your-proposalthe-ieee-robotics-and-automation-society-ras-invit/697022755988706/"},{"title":"Start Page of the Conference Management System","url":"https://ras.papercept.net/conferences/scripts/start.pl"},{"title":"Timetable 2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853/timetable.html"}]

Based on the search results, I found that IEEE ICRA 2027 is held in Seoul, South Korea, from May 24-28, 2027. However, the specific submission deadline for ICRA 2027 papers is not clearly stated in these search results. The results appear to contain information about past ICRA conferences and the conference dates, but not the exact paper submission deadline for 2027.

For the most current and accurate submission deadline information for ICRA 2027, I recommend visiting the official ICRA 2027 website at https://2027.ieee-icra.org/ or contacting the conference organizers directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c145ee65-1ff4-4bc2-a934-542880bda996",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "e1cef931-f662-4edd-8b9b-1163a4054ef8",
  "sourceToolAssistantUUID": "c145ee65-1ff4-4bc2-a934-542880bda996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T05:45:45.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RgxsXjF8RawJXBhuteR9NK`</summary>

```json
{
  "query": "\"See What Matters\" differentiable grid sample pruning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1cef931-f662-4edd-8b9b-1163a4054ef8",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Bj35wsnFcMKgZ5m1Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4fbfd7e-20a1-45a0-b57d-07ada81a38a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QrHfaEDZC9ziyN5aRZnfXp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1915,
      "cache_read_input_tokens": 8221,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 410,
          "cache_read_input_tokens": 8221,
          "cache_creation_input_tokens": 1915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1915,
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

_source line 16 · 2026-05-13T05:45:45.882Z_

<details><summary>↩ Tool result · `toolu_01DnhP3hWauD2c8MWviWedkx`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline call for papers"

Links: [{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"Call for Papers","url":"https://iclr.cc/Conferences/2025/CallForPapers"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"}]

Based on the search results, I found information about ICLR 2026, but the official call for papers for ICLR 2027 has not yet been published. The search results show current information about ICLR 2026, which is the upcoming conference.

Here's what I found:

**ICLR 2026 Information:**
The main conference is scheduled for Thursday April 23 through Saturday April 25, with workshops on Sunday April 26 through Monday April 27. The deadline for paper submissions to ICLR 2026 is Sept 24.

**About ICLR:**
The International Conference on Learning Representations (ICLR) is the premier gathering of professionals dedicated to the advancement of deep learning, and along with NeurIPS and ICML, it is one of the three primary conferences of highest impact and reputation in machine learning and artificial intelligence research.

For ICLR 2027 specific details like submission deadline and call for papers, you may want to check the official ICLR website (iclr.cc) closer to when the 2027 conference call is announced, or subscribe to their announcements for updates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae31c0eb-c6dd-4253-aa54-7bde9af630db",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "8609171c-15cb-4193-8049-6d27e58d5503",
  "sourceToolAssistantUUID": "ae31c0eb-c6dd-4253-aa54-7bde9af630db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T05:45:46.546Z_

<details><summary>↩ Tool result · `toolu_01114suX3BUcY2hKTm1zY9hq`</summary>

```text
Web search results for query: "CoRL 2027 submission deadline call for papers"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, I found information about CoRL 2026, but the search did not return specific information about CoRL 2027. Here's what I found:

**CoRL 2026 Information:**

For CoRL 2026, the abstract submission deadline is May 25, and the full paper submission deadline is May 28, with the conference taking place November 9-12 in Austin, TX.

**CoRL 2027 Information:**

Unfortunately, the search results do not contain information about CoRL 2027's call for papers or submission deadlines. Since CoRL 2026 is still upcoming (scheduled for November 2026), it's likely that the CoRL 2027 call for papers and deadlines have not yet been announced. Typically, conference organizers announce upcoming years' deadlines after the current year's conference concludes.

For the most current information about CoRL 2027, I recommend:
- Visiting the official CoRL website at corl.org
- Following CoRL on social media (@corl_conf on X/Twitter)
- Checking OpenReview.net where CoRL submissions are typically hosted


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8866548-968d-47fc-a8ce-0f7a40609ce2",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "826d4935-e770-4886-b56a-2b2c83cf67f7",
  "sourceToolAssistantUUID": "f8866548-968d-47fc-a8ce-0f7a40609ce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T05:45:49.317Z_

<details><summary>↩ Tool result · `toolu_01SKGkKGt6brjecqUVhYpzXk`</summary>

```text
Web search results for query: "LIBERO VLA benchmark success rate 2026 state of the art"

Links: [{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"}]

Based on the search results, here's what I found about LIBERO VLA benchmark success rates and state-of-the-art performance in 2026:

## LIBERO Benchmark Performance in 2026

Strong 2025-era VLA policies (OpenVLA, pi0, Octo variants) typically land in the 70-90 percent success range on Spatial, Object, and Goal, and 30-60 percent on LIBERO-100 depending on training recipe.

### State-of-the-Art Results

The OpenVLA-OFT backbone establishes a baseline with a 97.1% average success rate, while VLA-IAP achieves a state-of-the-art average success rate of 97.8%.

## Important Context on Reported Success Rates

It's worth noting that while Visual–Language–Action (VLA) models report impressive success rates exceeding 95% on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness. Recent research has revealed significant concerns: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

LIBERO is cheaper, faster, more standard in 2026 papers, and plugs into the widest range of pretrained policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1369ef7f-47d8-4399-a463-0cc52f76c7cb",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "c576cab9-56f9-4ad2-9523-e252777a35c0",
  "sourceToolAssistantUUID": "1369ef7f-47d8-4399-a463-0cc52f76c7cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T05:45:49.517Z_

<details><summary>↩ Tool result · `toolu_01XHTnz5P4HsrXdJYfLYAHvt`</summary>

```text
Web search results for query: "arXiv 2604.01570 FAN paper"

Links: [{"title":"[2604.21470] Spectral radius and edge-disjoint spanning trees of $(k+1)$-edge-connected graphs","url":"https://arxiv.org/abs/2604.21470"},{"title":"[2111.01570] Privacy-Preserving Communication-Efficient Federated Multi-Armed Bandits","url":"https://arxiv.org/abs/2111.01570"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=263&show=2000"},{"title":"[2110.01570] Hypergraph regularity and random sampling","url":"https://arxiv.org/abs/2110.01570"},{"title":"[2112.01570] Trajectory Clustering Performance Evaluation: If we know the answer, it's not clustering","url":"https://arxiv.org/abs/2112.01570"},{"title":"[2604.23671] Countable Fan Tightness and Selection Games in Group-Valued Function Spaces","url":"https://arxiv.org/abs/2604.23671"},{"title":"[2604.22019] The Specification Property on the Lelek Fan","url":"https://arxiv.org/abs/2604.22019"},{"title":"[1711.01570] Modeling of Persistent Homology","url":"https://arxiv.org/abs/1711.01570"},{"title":"The Specification Property on the Lelek Fan","url":"https://arxiv.org/html/2604.22019"},{"title":"[1507.01570] Lepton fluxes from atmospheric charm revisited","url":"https://arxiv.org/abs/1507.01570"}]

Based on the search results, I found information about arXiv paper 2604.01570. This paper is titled "Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior" by Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, and Fei Wen, and it has been accepted by CVPR 2026.

The "FAN" in the title refers to "Feasible Action Neighborhood" prior, which appears to be a technique for improving vision-language-action models through finetuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bffe5d28-6b4a-48a1-9bea-b7d3a597a8fb",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "96cab540-6914-440b-8385-b91f980ea73d",
  "sourceToolAssistantUUID": "bffe5d28-6b4a-48a1-9bea-b7d3a597a8fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T05:45:51.078Z_

<details><summary>↩ Tool result · `toolu_011QG8CcsukaNKmTJKvr35uo`</summary>

```text
Web search results for query: "SimplerEnv VLA benchmark 2026 state of the art"

Links: [{"title":"[Quick Review] BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://liner.com/review/bayesianvla-bayesian-decomposition-vision-language-action-models-via-latent-action"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.16391"},{"title":"StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing","url":"https://arxiv.org/html/2604.05014v1"},{"title":"GitHub - InternRobotics/InstructVLA: [ICLR 2026] InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation · GitHub","url":"https://github.com/InternRobotics/InstructVLA"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"GitHub - OpenGVLab/Vlaser: Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning · GitHub","url":"https://github.com/OpenGVLab/Vlaser"},{"title":"MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=54U3XHf7qq"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training","url":"https://arxiv.org/html/2604.20012"}]

Based on the search results, here's what I found about SimplerEnv VLA benchmark performance in 2026:

## State-of-the-Art Results on SimplerEnv

BayesianVLA achieves a state-of-the-art average success rate of 66.5% on SimplerEnv, representing an 11.3% absolute improvement over the QwenGR00T baseline.

DeFI sets a new state of the art on the CALVIN ABC-D benchmark (4.51 average task length), and boosts SimplerEnv-Fractal benchmark to 51.2% success rate.

MemoryVLA achieves 71.9% success rate on SimplerEnv-Bridge, 72.7% on SimplerEnv-Fractal, and 96.5% on LIBERO-5 suites, outperforming state-of-the-art baselines CogACT and pi-0 with a notable +14.6 gain on Bridge.

## Notable VLA Models and Approaches

Recent research at ICLR 2026 includes InstructVLA, which emphasizes language capability in VLAs and includes 650K tailored VLA-IT annotations, achieving leading performance across robotic manipulation tasks. DeFI uses multimodal Chain of Thought (COT) to advance the action reasoning ability of VLA.

SimpleVLA-RL improves OpenVLA-OFT performance to 97.6 points on LIBERO-Long and sets a new state-of-the-art.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44e5672d-cee6-4813-8a1c-086c71d65448",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "213251db-3506-458c-9e4e-aca6a548168a",
  "sourceToolAssistantUUID": "44e5672d-cee6-4813-8a1c-086c71d65448",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T05:45:52.068Z_

<details><summary>↩ Tool result · `toolu_01RgxsXjF8RawJXBhuteR9NK`</summary>

```text
Web search results for query: ""See What Matters" differentiable grid sample pruning VLA"

Links: [{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"Differentiable Gradient Sampling for Learning Implicit 3D Scene Reconstructions from a Single Image | OpenReview","url":"https://openreview.net/forum?id=U8pbd00cCWB"},{"title":"PDP: Parameter-free Differentiable Pruning is All You Need Minsik Cho","url":"https://arxiv.org/pdf/2305.11203v3"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"PDP: Parameter-free Differentiable Pruning is All You Need","url":"https://arxiv.org/pdf/2305.11203"},{"title":"Separate, Dynamic and Differentiable (SMART) Pruner for Block/Output Channel Pruning on Computer Vision Tasks","url":"https://arxiv.org/html/2403.19969v1"}]

Based on the search results, I found information about "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model."

Vision-Language-Action (VLA) models have shown remarkable promise in robotics manipulation, yet their high computational cost hinders real-time deployment. Existing token pruning methods suffer from a fundamental trade-off: aggressive compression using pruning inevitably discards critical geometric details like contact points, leading to severe performance degradation.

To address this challenge, the researchers propose the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression in visual tokens.

The work was presented at ICML 2026 as a poster. The key innovation of GridS is that it rethinks compression as a geometry-aware, continuous token resampling approach rather than traditional token pruning, allowing the model to maintain critical spatial details while achieving significant computational efficiency gains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4fbfd7e-20a1-45a0-b57d-07ada81a38a9",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "a58dfeaf-0951-48ed-9549-0d545a985ac5",
  "sourceToolAssistantUUID": "e4fbfd7e-20a1-45a0-b57d-07ada81a38a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T05:45:53.419Z_

<details><summary>↩ Tool result · `toolu_01VsQmFSpzphqu5Eho3vDXeh`</summary>

```text
Web search results for query: "VLA model state of the art 2025 2026 vision language action"

Links: [{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"},{"title":"[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/abs/2505.04769"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications","url":"https://vla-survey.github.io/"},{"title":"What are Vision Language Action (VLA) Models? Complete Guide","url":"https://www.articsledge.com/post/vision-language-action-vla-models"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Unified Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=PklMD8PwUy"}]

Based on the search results, here's an overview of the state-of-the-art in Vision-Language-Action (VLA) models in 2025-2026:

## Key Models and Developments

Gemini Robotics, introduced in 2025 by Google DeepMind, builds on the capabilities of Gemini 2.0 and extends multimodal data processing to the physical world, allowing robots to perform highly dexterous tasks such as folding origami and playing with cards. In June 2025, Google released Gemini Robotics On-Device, a lightweight version optimized to run locally on real robots with low-latency and high reliability.

GR00T N1, released by NVIDIA in March 2025, is a VLA for humanoid robots that adopts a dual-system architecture. This architecture combines System 1 (fast diffusion policies with 10ms latency for low-level control) and System 2 (LLM-based planners for high-level task decomposition), enabling efficient coordination between strategic planning and real-time execution.

Helix, unveiled in February 2025 by Figure AI, is a generalist VLA specifically tailored for humanoid robots. SmolVLA is an open-source compact VLA with 450 million parameters that achieved comparable performances with much larger VLAs despite its compact size.

## Recent Research Trends

A recent literature review covered over 80 VLA models published in the past three years, with key progress areas including architectural innovations, efficient training strategies, and real-time inference accelerations.

Research shows that hierarchical and late fusion architectures achieve the highest manipulation success and generalization, while diffusion-based decoders demonstrate superior cross-domain transfer and robustness compared to autoregressive heads.

A comprehensive analysis of 164 Vision-Language-Action model submissions at ICLR 2026 found trends in discrete diffusion VLAs, reasoning models, and benchmarks including LIBERO, CALVIN, and SIMPLER.

## Deployment and Applications

Expert consensus suggests commercial deployment 2025-2026, mass market adoption 2027-2030, and human-level capabilities by early 2030s.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83c8f297-e43e-433b-bc86-71ab2ad4a2b9",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "595d90c4-4b6d-468e-9bfe-ddcabbd8e5e2",
  "sourceToolAssistantUUID": "83c8f297-e43e-433b-bc86-71ab2ad4a2b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-13T05:46:00.383Z_

Good, I have initial results. Let me now fetch more specific details on the deadlines and the arXiv paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "595d90c4-4b6d-468e-9bfe-ddcabbd8e5e2",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Cr538ihWAE7kmAmGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17ba78b0-ad93-495b-9725-aeea50ff163c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhQDJ1Tg7zxYmsfR8WkaxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1538,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 10136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 24 · 2026-05-13T05:46:02.015Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KnKh8Q6DsWjBndSteCFFFi`</summary>

```json
{
  "url": "https://2027.ieee-icra.org/contribute/",
  "prompt": "What is the paper submission deadline for ICRA 2027? List all important dates and deadlines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17ba78b0-ad93-495b-9725-aeea50ff163c",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Cr538ihWAE7kmAmGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff169cee-ea4c-457c-a579-d7740b45ec4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhQDJ1Tg7zxYmsfR8WkaxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1538,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 10136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 25 · 2026-05-13T05:46:03.428Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QvEgfPYY5hrxrRCYoZgs8T`</summary>

```json
{
  "url": "https://trybibby.com/conference-deadlines",
  "prompt": "What are the submission deadlines for ICLR 2027, ICRA 2027, and CoRL 2027? List all dates mentioned for these three conferences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff169cee-ea4c-457c-a579-d7740b45ec4f",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Cr538ihWAE7kmAmGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b151d36-af4f-45d2-9789-77f7a638ec7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhQDJ1Tg7zxYmsfR8WkaxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1538,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 10136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 26 · 2026-05-13T05:46:04.281Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gz9Q65MMyzyc3eUoZQPeTg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.01570",
  "prompt": "What is the title, authors, and abstract of this paper? Is it about VLA or robotics? What is the arXiv ID?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b151d36-af4f-45d2-9789-77f7a638ec7e",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Cr538ihWAE7kmAmGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a443082-dc63-481c-8e62-ef0150af830b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhQDJ1Tg7zxYmsfR8WkaxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1538,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 10136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 27 · 2026-05-13T05:46:06.717Z_

<details><summary>↩ Tool result · `toolu_01KnKh8Q6DsWjBndSteCFFFi`</summary>

```text
# ICRA 2027 Submission Deadlines

Based on the webpage content provided, I need to clarify an important issue: **The page contains information about ICRA 2025, not ICRA 2027.**

The page header indicates "IEEE ICRA 2027" but the actual submission details reference ICRA 2025. According to the latest announcement dated May 5, 2026, "ICRA 2027 Website under Construction," suggesting the 2027 details aren't yet finalized.

## ICRA 2025 Important Deadlines

The documented deadlines for ICRA 2025 include:

**Papers:**
- Submission deadline: "15 September 2024 (11:59 PST)"
- Video submissions: August 5–September 9, 2024, and September 17–22, 2024

**Competitions:**
- Opens: July 15, 2024
- Deadline: October 15, 2024
- Notifications: October 31, 2024

**Workshops/Tutorials:**
- Deadline: "September 25th, 2024"
- Notifications: December 21, 2024

For ICRA 2027-specific deadlines, you would need to check the updated 2027 website once construction is complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff169cee-ea4c-457c-a579-d7740b45ec4f",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "0918128c-9d96-4c4a-ad71-6f90cdd0c633",
  "sourceToolAssistantUUID": "ff169cee-ea4c-457c-a579-d7740b45ec4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T05:46:07.193Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015ciFXYo5qyxEXR1snJpfLM`</summary>

```json
{
  "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html",
  "prompt": "What are the current state-of-the-art results on SimplerEnv and LIBERO benchmarks? What VLA models achieve the best scores? Report specific numbers for SimplerEnv OOD visual variants and LIBERO success rates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0918128c-9d96-4c4a-ad71-6f90cdd0c633",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Cr538ihWAE7kmAmGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d9eb30a-3755-428d-aa50-cff9742b18a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhQDJ1Tg7zxYmsfR8WkaxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1538,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 10136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 29 · 2026-05-13T05:46:08.160Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018tAGozXA4bYd2Z4hp9X72N`</summary>

```json
{
  "url": "https://icml.cc/virtual/2026/poster/65010",
  "prompt": "What is the title, authors, and abstract of this paper? Is this 'See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model' at ICML 2026? Confirm the paper name GridS."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d9eb30a-3755-428d-aa50-cff9742b18a3",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3Cr538ihWAE7kmAmGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da2000f2-1bc3-4fca-a6d5-ba8e3ae1074b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhQDJ1Tg7zxYmsfR8WkaxA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1538,
      "cache_creation_input_tokens": 5439,
      "cache_read_input_tokens": 10136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5439,
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

_source line 30 · 2026-05-13T05:46:09.161Z_

<details><summary>↩ Tool result · `toolu_01Gz9Q65MMyzyc3eUoZQPeTg`</summary>

```text
# Paper Summary

**Title:** "Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior"

**Authors:** Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, and Fei Wen

**arXiv ID:** 2604.01570

**Field:** Yes, this work addresses both topics. It focuses on Vision-Language-Action (VLA) models applied to robotic manipulation tasks.

**Abstract Summary:**
The paper addresses a gap in how VLA models are trained for robotics. The researchers observe that robotic tasks typically allow a range of near-equivalent actions rather than requiring a single precise motion. They propose a "FAN-guided regularizer" that shapes model predictions to account for this feasible action neighborhood. Using a Gaussian prior, their approach promotes smooth, focused predictions and demonstrates improvements in sample efficiency and success rates across both in-distribution and out-of-distribution scenarios during finetuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a443082-dc63-481c-8e62-ef0150af830b",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "c9a1af23-5033-4a94-8a62-af9abcc1c779",
  "sourceToolAssistantUUID": "0a443082-dc63-481c-8e62-ef0150af830b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T05:46:09.905Z_

<details><summary>↩ Tool result · `toolu_01QvEgfPYY5hrxrRCYoZgs8T`</summary>

```text
# Submission Deadlines for Three Conferences

**ICLR 2027** has two submission phases:
- Abstract deadline: "Sep 19, 2026, 11:59 AM UTC"
- Full paper deadline: "Sep 24, 2026, 11:59 AM UTC"
The conference is scheduled for April/May 2027.

**ICRA 2027** features a single deadline:
- Paper submission: "Sep 16, 2026, 11:59 AM UTC"
The event takes place May 16–21, 2027, in Toronto, Canada.

**CoRL 2026** (Conference on Robot Learning) has two separate deadlines:
- Abstract submission: "May 26, 2026, 11:59 AM UTC"
- Full paper submission: "May 29, 2026, 11:59 AM UTC"
The conference occurs November 9–12, 2026, in Austin, Texas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b151d36-af4f-45d2-9789-77f7a638ec7e",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "aee4f4ed-12e5-4411-bde6-6277c63f1347",
  "sourceToolAssistantUUID": "4b151d36-af4f-45d2-9789-77f7a638ec7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T05:46:10.323Z_

<details><summary>↩ Tool result · `toolu_018tAGozXA4bYd2Z4hp9X72N`</summary>

```text
# Paper Details

**Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu

**Conference:** ICML 2026

**Module Name:** GridS (Differentiable Grid Sampler)

**Abstract Summary:** The paper addresses computational efficiency in Vision-Language-Action models for robotics. Rather than aggressive token removal, the authors propose a geometry-aware approach that "performs task-aware, continuous resampling of visual tokens in VLA." Their GridS module achieves significant compression—"76% reduction in FLOPs with no degradation in the success rate"—while maintaining essential spatial information needed for manipulation tasks.

Yes, this is confirmed as the correct paper and module designation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da2000f2-1bc3-4fca-a6d5-ba8e3ae1074b",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "978f6cb8-951f-413f-8c1a-13e282767932",
  "sourceToolAssistantUUID": "da2000f2-1bc3-4fca-a6d5-ba8e3ae1074b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T05:46:15.167Z_

<details><summary>↩ Tool result · `toolu_015ciFXYo5qyxEXR1snJpfLM`</summary>

```text
# VLA Benchmark Performance Summary

The blog post provides limited specific numerical comparisons for state-of-the-art results across benchmarks.

## LIBERO Results

The author notes that "all mentioned concurrent discrete diffusion policies below test on LIBERO and all achieve between 95-98% average" across the four benchmark versions. For context, performance benchmarks suggest: "95% is expected for Spatial, Goal and Object, 90-95% is required for Long."

The author emphasizes that LIBERO is "basically solved," making it difficult to distinguish between top performers.

## SIMPLER Results

Performance varies significantly by setup. For the Google Robot version, "current sota models achieve around 70%-80% success rate." The blog notes that "SIMPLER is hard to interpret across setups; success spans 40–99% on Bridge."

## Key Limitation

The post explicitly avoids definitively naming which specific VLA models rank highest, stating there is "no clear statement possible to say which model is the best, as most papers only compare against each other on the usual simulation benchmarks."

The author identifies this benchmark saturation as a significant problem preventing meaningful comparison of competing approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d9eb30a-3755-428d-aa50-cff9742b18a3",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "fc5e1e79-5010-461c-be68-e96cdb3351e4",
  "sourceToolAssistantUUID": "3d9eb30a-3755-428d-aa50-cff9742b18a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-13T05:46:18.727Z_

Now let me get a few more specific details to fill gaps - specifically ICLR 2027 dates from a more authoritative source, CoRL 2027 specifically (we only found CoRL 2026), and the SimplerEnv OOD visual variant numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc5e1e79-5010-461c-be68-e96cdb3351e4",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3ET7xpBBgeHYmMoY3k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e96cac21-17e9-4975-994b-e15c92fb08b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSLYVnYvr53wHZFAGRvrLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 240,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 15575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
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

_source line 35 · 2026-05-13T05:46:19.644Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SAVvKmpxDvwUkQkJT8pYrY`</summary>

```json
{
  "query": "CoRL 2027 conference date location announcement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e96cac21-17e9-4975-994b-e15c92fb08b8",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3ET7xpBBgeHYmMoY3k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f1b5428-4599-4f2e-9d16-adb5b9803985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSLYVnYvr53wHZFAGRvrLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 240,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 15575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
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

_source line 36 · 2026-05-13T05:46:20.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HvbMj8oEgLebnyJuFY1EvH`</summary>

```json
{
  "query": "SimplerEnv OOD visual variant success rate best VLA model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f1b5428-4599-4f2e-9d16-adb5b9803985",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3ET7xpBBgeHYmMoY3k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "527876cd-4478-4814-9ed2-41fd5a48e99d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSLYVnYvr53wHZFAGRvrLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 240,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 15575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
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

_source line 37 · 2026-05-13T05:46:20.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Xs7fPJ6JGE1N72AqYgVwG`</summary>

```json
{
  "query": "LIBERO-Long best success rate VLA 2026 SimpleVLA-RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "527876cd-4478-4814-9ed2-41fd5a48e99d",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3ET7xpBBgeHYmMoY3k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d153494-281c-4df8-9372-f5cf6900a936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSLYVnYvr53wHZFAGRvrLN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 240,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 15575,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 240,
          "output_tokens": 228,
          "cache_read_input_tokens": 15575,
          "cache_creation_input_tokens": 3226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3226,
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

_source line 38 · 2026-05-13T05:46:22.920Z_

<details><summary>↩ Tool result · `toolu_01SAVvKmpxDvwUkQkJT8pYrY`</summary>

```text
Web search results for query: "CoRL 2027 conference date location announcement"

Links: [{"title":"Cork 2027 | degrowth.info","url":"https://degrowth.info/en/conference/cork-2027"},{"title":"CoRL 2025","url":"https://2025.corl.org/"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conferences | Pulkit Verma","url":"https://pulkitverma.net/conferences/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"NVIDIA at CoRL & Humanoids 2025 | Sept 27–Oct 2, Seoul","url":"https://www.nvidia.com/en-us/events/corl/"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"},{"title":"CoRL 2017 : Conference on Robot Learning","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=60391"},{"title":"Conference on Robot Learning (@corl_conf) · X","url":"https://twitter.com/corl_conf"}]

Based on the search results, I found information about CoRL (Conference on Robot Learning):

CoRL 2026 will be held in Austin, Texas, US. However, the search results do not contain any announcement regarding the date and location for CoRL 2027. The most recent specific information available is about CoRL 2026 in Austin and CoRL 2025 in Seoul, Korea.

If you're looking for CoRL 2027 details, they may not have been announced yet. You might want to check the official CoRL website or their social media channels for future announcements about the 2027 conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f1b5428-4599-4f2e-9d16-adb5b9803985",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "898503d4-5e0e-4323-badc-5fa9b1bacece",
  "sourceToolAssistantUUID": "5f1b5428-4599-4f2e-9d16-adb5b9803985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T05:46:25.587Z_

<details><summary>↩ Tool result · `toolu_014Xs7fPJ6JGE1N72AqYgVwG`</summary>

```text
Web search results for query: "LIBERO-Long best success rate VLA 2026 SimpleVLA-RL"

Links: [{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.09674v1"},{"title":"SimpleVLA-RL: Scalable RL for VLA Models","url":"https://www.emergentmind.com/papers/2509.09674"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"[Literature Review] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://www.themoonlight.io/en/review/simplevla-rl-scaling-vla-training-via-reinforcement-learning"},{"title":"SimpleVLA-RL: Scalable VLA Reinforcement Learning","url":"https://www.emergentmind.com/topics/simplevla-rl"},{"title":"GitHub - thegovind/simplevla-rl: SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://github.com/thegovind/simplevla-rl"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/simplevla-rl-scaling-vla-training-via-reinforcement"},{"title":"SimpleVLA-RL/README.md at main · PRIME-RL/SimpleVLA-RL","url":"https://github.com/PRIME-RL/SimpleVLA-RL/blob/main/README.md"}]

Based on the search results, here are the key findings regarding SimpleVLA-RL's performance on LIBERO-Long:

## Best Success Rate on LIBERO-Long

SimpleVLA-RL improves the performance of OpenVLA-OFT to 97.6 points on LIBERO-Long and sets a new state-of-the-art.

## Performance with Limited Data

Remarkably, on LIBERO-Long, success rates increase from 17.3% (One-Trajectory SFT) to 91.7% (One-Trajectory SFT + RL), representing a 430.1% relative improvement.

## Overall LIBERO Performance

On LIBERO tasks, the framework improves average success rates from 91% to 99.1%, with particularly notable gains on long-horizon tasks (98.5% vs. previous best results).

The results demonstrate that SimpleVLA-RL achieves state-of-the-art performance on LIBERO-Long, with the model reaching approximately 97.6-98.5% success rate depending on the specific evaluation configuration. This represents a significant improvement over prior methods and showcases the effectiveness of reinforcement learning for scaling Vision-Language-Action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d153494-281c-4df8-9372-f5cf6900a936",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "374646a1-0d9e-49cb-a9d6-398abfa72067",
  "sourceToolAssistantUUID": "4d153494-281c-4df8-9372-f5cf6900a936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T05:46:25.752Z_

<details><summary>↩ Tool result · `toolu_01HvbMj8oEgLebnyJuFY1EvH`</summary>

```text
Web search results for query: "SimplerEnv OOD visual variant success rate best VLA model 2026"

Links: [{"title":"VP-VLA: Visual Prompting as an Interface for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22003"},{"title":"VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model","url":"https://arxiv.org/pdf/2602.10098"},{"title":"[Quick Review] BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://liner.com/review/bayesianvla-bayesian-decomposition-vision-language-action-models-via-latent-action"},{"title":"VP-VLA: Visual Prompting as an Interface for Vision-Language-Action Models","url":"https://visualprompt-vla.github.io/"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"GitHub - InternRobotics/InstructVLA: [ICLR 2026] InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation · GitHub","url":"https://github.com/InternRobotics/InstructVLA"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries","url":"https://arxiv.org/html/2601.15197v1"}]

Based on the search results, I found several key findings about SimplerEnv OOD (out-of-distribution) visual variant success rates for VLA models in 2026:

## Best Performing VLA Models on SimplerEnv

BayesianVLA significantly outperforms all comparison baselines in the SimplerEnv environment, achieving a state-of-the-art average success rate of 66.5%. BayesianVLA achieves state-of-the-art performance on SimplerEnv and RoboCasa, demonstrating substantial gains, including an 11.3% improvement on the challenging OOD SimplerEnv benchmark.

Other notable performers include:

- VP-VLA achieves a state-of-the-art performance of 58.3% on SimplerEnv, yielding a substantial improvement of 8.3% over QwenOFT (50.0%)

- VP-VLA surpasses π0.5 (57.1%) and Isaac-GR00T-N1.6-Bridge (57.1%)

SimplerEnv evaluates models in out-of-distribution (OOD) settings, where success requires both high-precision localization and robust control. BayesianVLA's 66.5% success rate represents the best performance among VLA models on this challenging benchmark as of 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "527876cd-4478-4814-9ed2-41fd5a48e99d",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "43ee1046-a06a-4cb4-9725-19cd3c207581",
  "sourceToolAssistantUUID": "527876cd-4478-4814-9ed2-41fd5a48e99d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-13T05:46:28.858Z_

Now let me get a couple more details - specifically verify the FAN paper more thoroughly and check the ICLR 2027 dates from the aggregator site.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43ee1046-a06a-4cb4-9725-19cd3c207581",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3FEMnMZWpoW4zhJJV9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1400d135-ee92-4e56-914b-7ad86bf37325",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMdFZBxoejo16957Di2Etm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 884,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 18801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1982,
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

_source line 42 · 2026-05-13T05:46:30.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JcvcCnJh9ynhzAqfCFGJXK`</summary>

```json
{
  "query": "\"2604.01570\" \"Feasible Action Neighborhood\" CVPR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1400d135-ee92-4e56-914b-7ad86bf37325",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3FEMnMZWpoW4zhJJV9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dbbf36b-f33a-4a28-8fd8-e758f0a99e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMdFZBxoejo16957Di2Etm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 884,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 18801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1982,
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

_source line 43 · 2026-05-13T05:46:30.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PsqTfMfnDQRZu9kXLKfsuj`</summary>

```json
{
  "query": "LIBERO benchmark saturated 97% success rate VLA limitations 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dbbf36b-f33a-4a28-8fd8-e758f0a99e2f",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3FEMnMZWpoW4zhJJV9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb306c00-2cc0-480c-96f7-7d62755c61d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMdFZBxoejo16957Di2Etm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 884,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 18801,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 884,
          "output_tokens": 159,
          "cache_read_input_tokens": 18801,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1982,
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

_source line 44 · 2026-05-13T05:46:35.648Z_

<details><summary>↩ Tool result · `toolu_01JcvcCnJh9ynhzAqfCFGJXK`</summary>

```text
Web search results for query: ""2604.01570" "Feasible Action Neighborhood" CVPR 2026"

Links: [{"title":"Important Dates and Deadlines - CVPR 2026","url":"https://cvpr.thecvf.com/Conferences/2026/Dates"},{"title":"GitHub - SkalskiP/top-cvpr-2026-papers: About This repository is a curated collection of the most exciting and influential CVPR 2026 papers. 🔥 [Paper + Code + Demo]","url":"https://github.com/SkalskiP/top-cvpr-2026-papers"},{"title":"CVPR: Computer Vision and Pattern Recognition 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=628"},{"title":"CVPR 2026","url":"https://cvpr.thecvf.com/"},{"title":"CVPR 2026 Workshops - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/Conferences/2026/Workshops"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"CVPR 2025 Organizers","url":"https://cvpr.thecvf.com/Conferences/2026/Organizers"},{"title":"DataCV 2026 @ CVPR 2026","url":"https://sites.google.com/view/datacv-2026-cvpr/"},{"title":"CVPR 2026 Call for Papers - The Computer Vision Foundation","url":"https://cvpr.thecvf.com/Conferences/2026/CallForPapers"},{"title":"CVPR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=thecvf.com%2FCVPR%2F2026%2FConference"}]

The search results show CVPR 2026 conference information but don't directly contain results about the specific paper identifier "2604.01570" with the title "Feasible Action Neighborhood." The results appear to be general CVPR 2026 information rather than specific paper details.

Let me try a more targeted search for the paper:

No links found.

Based on my search attempts, I wasn't able to find specific information about the paper with identifier "2604.01570" titled "Feasible Action Neighborhood" in relation to CVPR 2026. The search returned general CVPR 2026 conference information but no results specifically matching the paper ID or exact title you're looking for.

The paper identifier appears to follow an arXiv-style format (possibly 2604.01570 from April 2026). You might try:
- Searching directly on arXiv (arxiv.org) using the paper ID
- Checking the OpenReview platform for CVPR 2026 submissions
- Searching for the paper on Google Scholar with the paper ID

Would you like me to search for something specific about this paper, such as the authors or a different variation of the title?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dbbf36b-f33a-4a28-8fd8-e758f0a99e2f",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "d955588c-7885-4ac7-bc6d-b5973880c3f0",
  "sourceToolAssistantUUID": "2dbbf36b-f33a-4a28-8fd8-e758f0a99e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-13T05:46:37.074Z_

<details><summary>↩ Tool result · `toolu_01PsqTfMfnDQRZu9kXLKfsuj`</summary>

```text
Web search results for query: "LIBERO benchmark saturated 97% success rate VLA limitations 2026"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"}]

Based on the search results, I found relevant information about LIBERO benchmarks and VLA model limitations in 2026:

## LIBERO Benchmark Saturation and VLA Limitations

Visual-Language-Action (VLA) models report impressive success rates exceeding 95% on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness. This phenomenon reflects benchmark saturation rather than true model competency.

### Key Findings on VLA Limitations:

**Performance Brittleness Under Perturbations:**
Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

**Language Grounding Weaknesses:**
Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely. More specifically, most models exploit language only superficially; robustness ablations (language deletion or paraphrasing) cause marginal or no drop in most suites.

**Paraphrase Robustness:**
Across seven VLA configurations (0.6B-7.5B), consistent performance degradation of 22-52 percentage points is observed under paraphrasing.

**Compositional Generalization:**
Current VLA models lack compositional generalization capabilities. Their learned representations are entangled and cannot handle the complex, multi-dimensional perturbations that characterize real-world environments.

In summary, while VLA models achieve high success rates on standard LIBERO benchmarks, they demonstrate critical robustness limitations when subjected to systematic perturbations, particularly in spatial reasoning and language understanding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb306c00-2cc0-480c-96f7-7d62755c61d7",
  "isSidechain": true,
  "promptId": "9e24a261-920c-4227-86ba-d5d8cf32ffd6",
  "agentId": "a88534961460cf29b",
  "type": "user",
  "uuid": "782a31c8-1e8d-4e4c-a3bd-693527e796f4",
  "sourceToolAssistantUUID": "fb306c00-2cc0-480c-96f7-7d62755c61d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-13T05:47:26.825Z_

Now I have comprehensive data for all three questions. Here is the full report:

---

## 1. Venue Deadline Verification

Based on data from the [AI & ML Conference Deadlines aggregator](https://trybibby.com/conference-deadlines):

| Conference | Deadline | After today (2026-05-13)? |
|---|---|---|
| **ICLR 2027** | Abstract: Sep 19, 2026; Full paper: Sep 24, 2026 | **Yes** -- ~4 months away |
| **ICRA 2027** | Paper submission: Sep 16, 2026 | **Yes** -- ~4 months away |
| **CoRL 2027** | **Not yet announced.** CoRL 2026 deadlines are: Abstract May 26, 2026; Full paper May 29, 2026 | CoRL **2026** is ~2 weeks away; CoRL **2027** dates are unknown |

**Key finding:** ICLR 2027 and ICRA 2027 deadlines are well after today. CoRL 2027 has not been announced yet -- if the research idea targets CoRL, only the 2026 edition (deadline May 26-29, 2026) is currently open, and that is extremely tight (13 days away). The ICRA 2027 website at [2027.ieee-icra.org](https://2027.ieee-icra.org/contribute/) is still under construction as of May 2026, so the Sep 16 date comes from the aggregator and should be confirmed closer to the date.

---

## 2. Current SOTA on VLA Benchmarks

### LIBERO Benchmark

**Is LIBERO saturated at ~97%? Yes, essentially.**

- **VLA-IAP** achieves 97.8% average success rate (current top on standard LIBERO suites).
- **SimpleVLA-RL** (ICLR 2026) reaches 97.6 on LIBERO-Long specifically, and 99.1% average across all LIBERO tasks -- the current state-of-the-art.
- **OpenVLA-OFT** baseline sits at 97.1%.
- Multiple concurrent discrete diffusion VLA papers at ICLR 2026 all land between 95-98% average.

The [ICLR 2026 VLA blog post by Moritz Reuss](https://mbreuss.github.io/blog_post_iclr_26_vla.html) explicitly states LIBERO is "basically solved," with 95% expected for Spatial/Goal/Object and 90-95% required for Long.

**However, this saturation is misleading.** [LIBERO-Plus](https://arxiv.org/abs/2510.13626) (CVPR 2026) shows that under modest perturbations (camera viewpoint changes, robot initial state variations), performance drops from 95%+ to below 30%. [LIBERO-Para](https://arxiv.org/abs/2603.28301) shows 22-52 percentage point degradation under language paraphrasing. Models largely ignore language instructions and lack compositional generalization.

### SimplerEnv Benchmark (OOD / Visual Variants)

- **BayesianVLA**: 66.5% average success rate -- current SOTA on SimplerEnv overall, representing an 11.3% improvement over QwenGR00T baseline on OOD SimplerEnv.
- **VP-VLA**: 58.3% on SimplerEnv (surpassing pi-0.5 at 57.1% and Isaac-GR00T-N1.6-Bridge at 57.1%).
- **MemoryVLA**: 71.9% on SimplerEnv-Bridge, 72.7% on SimplerEnv-Fractal.
- Google Robot setups: current SOTA models achieve around 70-80% success rate.
- Bridge setups: success spans 40-99% depending on configuration.

SimplerEnv is **not saturated** -- OOD visual variant performance remains a meaningful discriminator between models.

### Latest VLA Models (2025-2026)

Key models: Gemini Robotics (Google DeepMind, 2025), GR00T N1 (NVIDIA, March 2025), Helix (Figure AI, Feb 2025), SmolVLA (450M params, competitive with larger models), OpenVLA-OFT, pi-0/pi-0.5, SimpleVLA-RL, BayesianVLA, InstructVLA, VP-VLA, MemoryVLA, ACoT-VLA. 164 VLA-related submissions were counted at ICLR 2026 alone.

---

## 3. Previously Flagged "Fabricated" References

### FAN (arXiv 2604.01570) -- REAL

**This is a real paper.** I confirmed it directly on [arXiv](https://arxiv.org/abs/2604.01570):
- **Title:** "Boosting Vision-Language-Action Finetuning with Feasible Action Neighborhood Prior"
- **Authors:** Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, Fei Wen
- **Venue:** Accepted at CVPR 2026
- **Content:** Proposes a FAN-guided regularizer using Gaussian priors over feasible action neighborhoods to improve VLA finetuning sample efficiency and success rates in both in-distribution and OOD scenarios.

This paper is directly relevant to VLA research and is legitimately published.

### GridS / "See What Matters" (ICML 2026) -- REAL

**This is a real paper.** Confirmed via the [ICML 2026 virtual poster page](https://icml.cc/virtual/2026/poster/65010):
- **Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"
- **Authors:** Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu
- **Venue:** ICML 2026 (poster)
- **Content:** Proposes GridS (Differentiable Grid Sampler), a plug-and-play module that performs task-aware continuous resampling of visual tokens in VLA models, achieving 76% FLOPs reduction with no degradation in success rate.

Both previously flagged references are confirmed real, published papers at top venues (CVPR 2026 and ICML 2026 respectively).

---

**Sources:**
- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)
- [ICLR 2026 Official Site](https://iclr.cc/)
- [ICRA 2027 Website](https://2027.ieee-icra.org/contribute/)
- [CoRL 2026 Official Site](https://www.corl.org/)
- [State of VLA Research at ICLR 2026 -- Moritz Reuss](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
- [arXiv 2604.01570 -- FAN Paper](https://arxiv.org/abs/2604.01570)
- [ICML 2026 Poster -- See What Matters / GridS](https://icml.cc/virtual/2026/poster/65010)
- [LIBERO-Plus: Robustness Analysis (CVPR 2026)](https://arxiv.org/abs/2510.13626)
- [LIBERO-Para: Paraphrase Robustness](https://arxiv.org/abs/2603.28301)
- [SimpleVLA-RL (ICLR 2026)](https://github.com/PRIME-RL/SimpleVLA-RL)
- [BayesianVLA](https://arxiv.org/html/2601.15197v1)
- [VP-VLA](https://arxiv.org/html/2603.22003)
- [VLA Survey Paper](https://arxiv.org/abs/2505.04769)
- [VLA Wikipedia](https://en.wikipedia.org/wiki/Vision-language-action_model)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "782a31c8-1e8d-4e4c-a3bd-693527e796f4",
  "isSidechain": true,
  "agentId": "a88534961460cf29b",
  "requestId": "req_011Caz3G4w2RNy5bwCPyk1FC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e24bd9f7-8feb-4210-9c8c-fe30f67c5b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "682db55c-3db4-4c29-bfdb-bcc06d9fe02d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8diG18p9ZhDNMA36PCLGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2814,
      "cache_read_input_tokens": 20783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2814,
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
