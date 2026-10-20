# Research conversation: In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse, find the definition/

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4362469ba847a909.jsonl`
- **Structured JSON:** [`f23b27fb385592fc44e2.json`](../../sessions/f2/f23b27fb385592fc44e2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-18T21:17:25.763Z_

In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse, find the definition/template for "Table 7" in the paper. Check docs/paper/*.tex files and any artifact files. I need to know the exact columns and format of Table 7. Search for "Table 7", "table7", "cross-architecture", "generalize" in tex files. Report what columns Table 7 has and what format each row should be in.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "4baee91b-3f12-4045-a561-7a03c5b6cbaa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-18T21:17:27.002Z_

I'll search for Table 7 in the project's paper files. Let me start by exploring the structure and then searching for the table definition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4baee91b-3f12-4045-a561-7a03c5b6cbaa",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHVS9NPM9XmpvjEcrs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6f1bd8a9-a22f-4033-ad38-a50155463dcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016NoUzoLDtCGYtVTSUyBP6D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17079,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17079,
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

_source line 3 · 2026-05-18T21:17:27.377Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FvnZ59PykyS7dAwUmkAMJm`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.tex\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f1bd8a9-a22f-4033-ad38-a50155463dcd",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHVS9NPM9XmpvjEcrs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33dbce0e-9f09-4592-8b27-93b81fe2034a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016NoUzoLDtCGYtVTSUyBP6D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17079,
      "cache_read_input_tokens": 0,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17079
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 131,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17079,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17079,
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

_source line 4 · 2026-05-18T21:17:27.434Z_

<details><summary>↩ Tool result · `toolu_01FvnZ59PykyS7dAwUmkAMJm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/single_method_errors.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/single_method_errors_ae8937.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33dbce0e-9f09-4592-8b27-93b81fe2034a",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "ff65f731-55e9-4da2-85c0-40cc7bd1152a",
  "sourceToolAssistantUUID": "33dbce0e-9f09-4592-8b27-93b81fe2034a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-18T21:17:28.793Z_

Now let me search for Table 7 in the tex files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff65f731-55e9-4da2-85c0-40cc7bd1152a",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHcYXPhNQ7Gx9QP3SR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c62054f7-9f14-4063-bc3e-077068ec0f42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Wkq79vrbRJmXwxnM2fiSg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 17079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1767,
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

_source line 6 · 2026-05-18T21:17:29.696Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AndXVNosavbCtWYRNbA6B9`</summary>

```json
{
  "pattern": "Table\\s+7|table7|cross-architecture|generalize",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "type": "tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c62054f7-9f14-4063-bc3e-077068ec0f42",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHcYXPhNQ7Gx9QP3SR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "63a06449-934e-4177-9f34-20cb8083be0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Wkq79vrbRJmXwxnM2fiSg8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 17079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1767,
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

_source line 7 · 2026-05-18T21:17:29.738Z_

<details><summary>↩ Tool result · `toolu_01AndXVNosavbCtWYRNbA6B9`</summary>

```text
Found 5 files
docs/paper/limitations.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63a06449-934e-4177-9f34-20cb8083be0b",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "fa7cb6a7-5c41-418e-a850-b3adc5c69e8e",
  "sourceToolAssistantUUID": "63a06449-934e-4177-9f34-20cb8083be0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T21:17:30.129Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01KMqZR2zBmVe9XGzUTmwY5W`</summary>

```json
{
  "pattern": "Table\\s+7|table7|cross-architecture|generalize",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
  "type": "tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa7cb6a7-5c41-418e-a850-b3adc5c69e8e",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHcYXPhNQ7Gx9QP3SR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c8673f82-3ccd-4560-b039-cca2010bc10c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Wkq79vrbRJmXwxnM2fiSg8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 17079,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1767
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 306,
          "cache_read_input_tokens": 17079,
          "cache_creation_input_tokens": 1767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1767,
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

_source line 9 · 2026-05-18T21:17:30.147Z_

<details><summary>↩ Tool result · `toolu_01KMqZR2zBmVe9XGzUTmwY5W`</summary>

```text
Found 1 file
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8673f82-3ccd-4560-b039-cca2010bc10c",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "e8cd0b6c-2456-4651-bea3-908b0f288518",
  "sourceToolAssistantUUID": "c8673f82-3ccd-4560-b039-cca2010bc10c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-18T21:17:37.027Z_

Let me search more specifically for "Table 7" with context in the experiments.tex file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8cd0b6c-2456-4651-bea3-908b0f288518",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHq6aRi8z7h5hXZNVW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0cf898ca-0148-4b55-90b3-1d38eff2f23c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HqjHDbEM7Juuh48JxmpQti",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 18846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 426,
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

_source line 11 · 2026-05-18T21:17:37.822Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FPXnY1Qf8w5uWAKqkhXG5j`</summary>

```json
{
  "pattern": "Table 7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cf898ca-0148-4b55-90b3-1d38eff2f23c",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHq6aRi8z7h5hXZNVW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5d46a70-487a-41c8-943a-47c0650a605c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HqjHDbEM7Juuh48JxmpQti",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 18846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 426,
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

_source line 12 · 2026-05-18T21:17:37.845Z_

<details><summary>↩ Tool result · `toolu_01FPXnY1Qf8w5uWAKqkhXG5j`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5d46a70-487a-41c8-943a-47c0650a605c",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "86813dbe-462c-4a42-af25-19cd1836fcb6",
  "sourceToolAssistantUUID": "f5d46a70-487a-41c8-943a-47c0650a605c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T21:17:38.990Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FmTic8AXSrrYo3KGDwXKsS`</summary>

```json
{
  "pattern": "\\\\begin\\{table\\}|\\\\begin\\{tabular\\}|\\\\label\\{table:7\\}|\\\\label\\{table:seven\\}|cross-architecture",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86813dbe-462c-4a42-af25-19cd1836fcb6",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjHq6aRi8z7h5hXZNVW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2b017b7f-f771-43ae-87c4-6dcc94476655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HqjHDbEM7Juuh48JxmpQti",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 426,
      "cache_read_input_tokens": 18846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 426,
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

_source line 14 · 2026-05-18T21:17:39.005Z_

<details><summary>↩ Tool result · `toolu_01FmTic8AXSrrYo3KGDwXKsS`</summary>

```text
27-Cross-correlation analysis uses a maximum lag of 5 generations.
28-Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all six contamination levels.
29-
30:\begin{table}[t]
31-\centering
32-\small
33-[Omitted long context line]
34-\label{tab:drift_summary}
35:\begin{tabular}{lccccc}
36-\toprule
37-$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
38-\midrule
--
101-\label{fig:consensus_heatmap}
102-\end{figure}
103-
104:\begin{table}[t]
105-\centering
106-\small
107-[Omitted long context line]
108-\label{tab:method_comparison}
109:\begin{tabular}{lcccccc}
110-\toprule
111-Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
112-\midrule
--
156-Table~\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.
157-At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.
158-
159:\begin{table}[t]
160-\centering
161-\small
162-\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\alpha{=}0.25$ and $\alpha{=}1.0$. Tier~3: $K{\geq}4/5$ methods; Tier~2: $K{\geq}3/5$. Drift is generation~0$\to$10. GPT-2-medium $\alpha{=}0.25$: single seed (seed=42); Pythia $\alpha{=}0.25$: 3-seed mean${\pm}$std. The onset boundary ($\alpha{\approx}0.25$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}
163-\label{tab:cross_arch_regime}
164:\begin{tabular}{llcccccc}
165-\toprule
166-$\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\ Granger & Tier~3 \\
167-\midrule
--
190-We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
191-
192-\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
193:Token entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \S\ref{sec:discussion}).
194-Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.
195-Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
196-Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
--
245-Table~\ref{tab:fpr_fnr} reports the calibration results.
246-Table~\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\alpha$ including the null control, Toda--Yamamoto misses true signals at $\alpha{=}0.75$, while the consensus at $K{\geq}3$ yields the correct verdict across all five contamination levels.
247-
248:\begin{table}[t]
249-\centering
250-\caption{Single-method inference errors across contamination levels.
251-Each cell shows the verdict (significant or not) based on multi-seed majority ($\geq$2/3 seeds with $\geq$4/8 pairs significant).
--
254-Only the multi-method consensus ($K{\geq}3$) yields the correct verdict at all five contamination levels.}
255-\label{tab:single-method-errors}
256-\resizebox{\columnwidth}{!}{%
257:\begin{tabular}{lccccc}
258-\toprule
259- & \multicolumn{2}{c}{\textit{No signal}} & \textit{Ambiguous} & \multicolumn{2}{c}{\textit{Causal signal}} \\
260-\cmidrule(lr){2-3} \cmidrule(lr){4-4} \cmidrule(lr){5-6}
--
310-Toda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\max}$), confirming its poor sensitivity at $T{=}10$.
311-We note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\beta{=}0.3$).
312-
313:\begin{table}[t]
314-\centering
315-\small
316-[Omitted long context line]
317-\label{tab:fpr_fnr}
318:\begin{tabular}{lcc}
319-\toprule
320-Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
321-\midrule
--
339-To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
340-All conditions use $\alpha{=}1.0$; architecture conditions use a single seed, while scale and domain conditions use two seeds (s42, s43) to assess replicability.
341-
342:\begin{table}[t]
343-\centering
344-\small
345-\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\alpha{=}1.0$, $n_{\text{perm}}{=}5{,}000$). Each cell reports the fraction of 8~canary$\to$downstream pairs per condition reaching BH-corrected FDR significance ($q{=}0.05$), with two seeds (s42, s43) to assess replicability for scale and domain conditions. MMCT: weighted forward consensus (\S\ref{sec:mmct}).}
346-\label{tab:generalization}
347-\resizebox{\columnwidth}{!}{%
348:\begin{tabular}{llcccccccc}
349-\toprule
350-Variation & Model / Dataset & \rotatebox{70}{Naive} & \rotatebox{70}{Diff.\ XCorr} & \rotatebox{70}{Threshold} & \rotatebox{70}{PermG (fwd)} & \rotatebox{70}{PermG (rev)} & \rotatebox{70}{TY} & \rotatebox{70}{$K{\geq}4/5$} & \rotatebox{70}{MMCT} \\
351-\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b017b7f-f771-43ae-87c4-6dcc94476655",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "0275962c-ad59-4ded-bcc5-3431bb2abe0d",
  "sourceToolAssistantUUID": "2b017b7f-f771-43ae-87c4-6dcc94476655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T21:17:41.068Z_

Great! I found Table 7 (the generalization table). Let me read the full experiments.tex file to get the complete table definition:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0275962c-ad59-4ded-bcc5-3431bb2abe0d",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjJW5s1cBTCFRrK8R2f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9018b8c7-6543-49c4-9510-ce839d68a8c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XgBdAJkjQL6tjYFmU2ZSok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2541,
      "cache_read_input_tokens": 19272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2541,
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

_source line 16 · 2026-05-18T21:17:41.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KkAN6YnK9W96w6GV45SfUr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9018b8c7-6543-49c4-9510-ce839d68a8c3",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjJW5s1cBTCFRrK8R2f",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ebe08803-8675-4a5e-91be-79f885dda374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XgBdAJkjQL6tjYFmU2ZSok",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2541,
      "cache_read_input_tokens": 19272,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2541
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 120,
          "cache_read_input_tokens": 19272,
          "cache_creation_input_tokens": 2541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2541,
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

_source line 17 · 2026-05-18T21:17:42.215Z_

<details><summary>↩ Tool result · `toolu_01KkAN6YnK9W96w6GV45SfUr`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across six contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:method_sensitivity}, \S\ref{sec:regime}, and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; $\alpha{=}0.10$ uses a single seed (42, preliminary).
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
18	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
19	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
20	Token entropy is the mean next-token prediction entropy $H(p_\theta | \text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.
21	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
22	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
23	Code and data will be released upon publication.
24	
25	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
26	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
27	Cross-correlation analysis uses a maximum lag of 5 generations.
28	Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all six contamination levels.
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
34	\label{tab:drift_summary}
35	\begin{tabular}{lccccc}
36	\toprule
37	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
38	\midrule
39	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
40	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
41	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
42	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
43	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
44	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	
50	\subsection{Method Sensitivity Analysis}
51	\label{sec:method_sensitivity}
52	
53	We open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.
54	If different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.
55	
56	\paragraph{Five-method ablation.}
57	We apply five lead-lag detection methods to the $\alpha{=}1.0$ condition (4~seeds, 16 canary$\to$downstream pairs).
58	The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
59	Method choice alone swings significance from \textbf{100\% to 25\%}: 50--57\% of pairs classified as significant under one method flip to non-significant under another.
60	The spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
61	Table~\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.
62	
63	\paragraph{First-differencing diagnostic.}
64	A single preprocessing decision can eliminate an entire analysis channel.
65	For canary$\to$diversity pairs at $\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.
66	For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
67	The apparent canary$\to$perplexity relationship is entirely an artifact of co-trending.
68	Notably, at $\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.
69	
70	\paragraph{Augmentation order sensitivity.}
71	Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
72	At $d_{\max}{=}0$ (most permissive), approximately 6\% of pairs are rejected; at adaptive $d_{\max}$ determined by ADF unit-root tests, 75\%; at $d_{\max}{=}1$ (most conservative), \textbf{94\%}.
73	This single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.
74	
75	\begin{figure}[t]
76	\centering
77	\includegraphics[width=\linewidth]{figures/differencing_dmax.pdf}
78	\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\alpha{=}1.0$, 4~seeds). \textbf{(a)}~First-differencing eliminates the canary$\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\to$diversity pairs retain significance after differencing (24/24$\to$24/24). \textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\max}$: from $\sim$6\% rejection at $d_{\max}{=}0$ to 94\% at $d_{\max}{=}1$, demonstrating that this single hyperparameter can reverse conclusions about temporal precedence.}
79	\label{fig:differencing_dmax}
80	\end{figure}
81	
82	\paragraph{Inter-method agreement.}
83	Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\alpha{=}0.0$ through $\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.
84	Cross-architecture validation on GPT-2-medium (12 canary$\to$downstream pairs) yields Fleiss' $\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.
85	Restricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.
86	Table~\ref{tab:method_comparison} extends the analysis across contamination levels.
87	At $\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \textbf{100\%} of pairs significant, a textbook spurious-regression outcome in trending time series.
88	Permutation Granger correctly finds 0\% across all three null-control seeds; Toda--Yamamoto finds 0--12.5\% (1/24 total, attributable to a degenerate $\text{df}_{\text{resid}}{=}1$ case; \S\ref{sec:consensus_validation}).
89	At $\alpha{=}0.50$, naive and differenced cross-correlation both find 100\% significance while threshold onset and all causal methods find 0\% (Figure~\ref{fig:consensus_heatmap}), illustrating that even among non-causal methods, sensitivity diverges sharply at this boundary.
90	
91	\paragraph{Method$\times$regime interaction.}
92	Table~\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.
93	At $\alpha{=}0.25$, differenced cross-correlation drops to 25\% and threshold onset to 0\%, while naive cross-correlation remains at 100\%, demonstrating that even partial detrending removes marginal associations at low contamination.
94	In the lowest-contamination regime ($\alpha{\leq}0.25$, three seeds), the false confirmation rate for the most liberal method approaches 100\%, while all Granger-type tests correctly find 0\%, a regime where single-method analysis is maximally dangerous.
95	The graded response across methods, combined with the block structure visible in Figure~\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \S\ref{sec:regime}.
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=\linewidth]{figures/consensus_heatmap.pdf}
100	\caption{Method$\times$regime consensus heatmap (Pythia-410M). Each cell shows the consensus tier ($K$-of-$M$ agreement) for a given lead-lag method (rows) and contamination level $\alpha$ (columns). A clear block structure emerges: correlation-based methods (naive, differenced, threshold) find significance across all $\alpha$ levels, while Granger-type methods find significance only at $\alpha{\geq}0.75$. The $\alpha{=}0.50$ column is maximally dangerous (high correlation coexists with zero causal precedence), illustrating Pitfall~3 (regime dependence). Color scale: dark = significant (Tier~3), light = non-significant (Tier~1).}
101	\label{fig:consensus_heatmap}
102	\end{figure}
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{FDR significance rates (\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\% (naive cross-correlation) to 0\% (permutation Granger) at $\alpha{\leq}0.25$, with seed-dependent onset at $\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\to$downstream pairs (token entropy and ECE $\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$), excluding failed candidates (\S\ref{sec:case_study}). Seed coverage: $\alpha{=}1.0$: 4 seeds (32 pairs); $\alpha{=}0.00$, $\alpha{=}0.75$: 3 seeds (24 pairs); $\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}
108	\label{tab:method_comparison}
109	\begin{tabular}{lcccccc}
110	\toprule
111	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
112	\midrule
113	Naive XCorr     & 100   & 100  & 100  & 100   & 100   & 100  \\
114	Diff.\ XCorr   & 37.5  & 25   & 100  & 100   & 100   & 37.5 \\
115	Threshold       & 20.8  & 0    & 0    & 33.3  & 100   & 20.8 \\
116	Perm.\ Granger  & 0     & 0    & 0--75$^\dagger$  & 79.2  & 75    & 0    \\
117	Toda--Yamamoto  & 0     & 12.5 & 0    & 12.5  & 59.4  & 0    \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	
123	\subsection{Regime-Dependent Detectability}
124	\label{sec:regime}
125	
126	Beyond method choice, the contamination level~$\alpha$ determines whether a temporal lead exists to detect.
127	We present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.
128	
129	\paragraph{Raw drift.}
130	Table~\ref{tab:drift_summary} shows that diversity collapse occurs at \emph{all} contamination levels, not only under full synthetic replacement.
131	Distinct-1 declines by 13.8\% even at $\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets).
132	A single-seed observation at $\alpha{=}0.10$ reveals a steep diversity cliff: distinct-1 drops by 39.6\%, nearly matching the 3-seed mean at $\alpha{=}0.25$ ($-40.3{\pm}0.3\%$); distinct-2 shows a comparable jump ($-56.4\%$ vs.\ $-56.4{\pm}0.7\%$ at $\alpha{=}0.25$).
133	Token entropy at $\alpha{=}0.10$, however, differs from the null by less than 1 percentage point ($-5.3\%$ vs.\ $-4.6{\pm}0.4\%$), constituting a canary blind spot in which diversity has already collapsed but no canary metric responds.
134	At higher contamination, distinct-1 decline continues: $-37.1{\pm}0.4\%$ ($\alpha{=}0.50$), $-32.3{\pm}0.5\%$ ($\alpha{=}0.75$), and $-27.8{\pm}1.6\%$ ($\alpha{=}1.0$).
135	The non-monotonic pattern (diversity declining \emph{more} at moderate~$\alpha$ than at extreme~$\alpha$) is confirmed by 3-seed replication at $\alpha{=}0.25$ (std${=}0.3\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.
136	
137	\begin{figure}[t]
138	\centering
139	\includegraphics[width=\linewidth]{figures/regime_map.pdf}
140	\caption{Detectability regime map across contamination levels (Pythia-410M). Permutation Granger FDR significance rate (solid line) and consensus tier (shaded regions) as a function of $\alpha$. The onset boundary lies at $\alpha{\approx}0.25$--$0.50$: at $\alpha{\leq}0.25$, all seeds agree on null (0/24); at $\alpha{=}0.50$, detectability is seed-dependent (0/8--6/8, 3~seeds, median 3/8); at $\alpha{=}0.75$, directional asymmetry emerges robustly (19/24 forward, 0/24 reverse, 3~seeds) but method consensus remains transitional (Tier~2--3); at $\alpha{=}1.0$, full Confirmatory consensus is achieved (24/24 forward, Tier~3, 4~seeds). Multi-seed replication: $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3~seeds; $\alpha{=}1.0$: 4~seeds.}
141	\label{fig:regime_map}
142	\end{figure}
143	
144	\paragraph{Granger-precedence detectability.}
145	Despite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\ref{fig:regime_map}).
146	Permutation Granger tests (first-differenced, BH-corrected) find 0/24 pairs FDR-significant at $\alpha{=}0.00$ (3~seeds), 0/8 at $\alpha{=}0.10$ (1~seed, preliminary), 0/24 at $\alpha{=}0.25$ (3~seeds), 0/8--6/8 at $\alpha{=}0.50$ (seed-dependent; 3~seeds, median 3/8), and \textbf{6/8} at $\alpha{=}1.0$.
147	At $\alpha{=}0.75$ (3~seeds), permutation Granger finds 19/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.
148	Under Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.
149	Within-$\alpha$ multi-seed analysis at $\alpha{=}1.0$ yields \textbf{24/24} canary$\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.
150	The resulting dose-response pattern is monotonic: causal detectability is absent at $\alpha{\leq}0.25$ (including $\alpha{=}0.10$, where diversity collapse is already severe but the canary signal is undetectable), seed-dependent at $\alpha{=}0.50$, and robust above $\alpha{=}0.75$ (Figure~\ref{fig:regime_map}).
151	The onset boundary lies at $\alpha{\approx}0.25$--$0.50$, consistent with theoretical expectations about signal-to-noise limits in short time series~\cite{boettiger2012limits}.
152	At the extremes, the transition is unambiguous: 0/24 FDR-significant pairs at $\alpha{\leq}0.25$ (3~seeds) versus 24/24 at $\alpha{=}1.0$ (4~seeds, Tier~3 consensus).
153	Between these extremes, individual-seed stochasticity determines whether the consensus threshold is crossed; the data map a boundary region rather than a sharp phase transition.
154	Sensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\ref{app:robustness}).
155	Cross-architecture validation on GPT-2-medium confirms this boundary: at $\alpha{=}0.25$, at most 1/8 pairs reach Confirmatory consensus ($K{\geq}4/5$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\%$ vs.\ Pythia $-4.7{\pm}0.5\%$), while at $\alpha{=}1.0$ all 6 canary$\to$diversity pairs reach $K{\geq}4/5$ (\S\ref{sec:discussion}).
156	Table~\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.
157	At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.
158	
159	\begin{table}[t]
160	\centering
161	\small
162	\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\alpha{=}0.25$ and $\alpha{=}1.0$. Tier~3: $K{\geq}4/5$ methods; Tier~2: $K{\geq}3/5$. Drift is generation~0$\to$10. GPT-2-medium $\alpha{=}0.25$: single seed (seed=42); Pythia $\alpha{=}0.25$: 3-seed mean${\pm}$std. The onset boundary ($\alpha{\approx}0.25$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}
163	\label{tab:cross_arch_regime}
164	\begin{tabular}{llcccccc}
165	\toprule
166	$\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\ Granger & Tier~3 \\
167	\midrule
168	0.25 & Pythia-410M  & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & 0/8 & 0/8 \\
169	0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\
170	\midrule
171	1.00 & Pythia-410M  & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & 6/8 & 6/8 \\
172	1.00 & GPT-2-medium & \multicolumn{6}{c}{(reported in \S\ref{sec:discussion}; 6/8 canary$\to$downstream pairs at Tier~3)} \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	\paragraph{Onset boundary at $\alpha{=}0.50$.}
178	The $\alpha{=}0.50$ regime provides particularly informative evidence.
179	Naive and differenced cross-correlation find 100\% significance while threshold onset finds 0\% (Table~\ref{tab:method_comparison}), and causal methods confirm emerging detectability in a majority of seeds: two of three seeds show directional asymmetry under permutation Granger (6/8 and 3/8 forward, 0/8 reverse), while one seed shows synchronous collapse (0/8).
180	The majority-signal outcome places $\alpha{=}0.50$ in a transitional regime where causal detectability is emerging but not yet robust, bridging the null regime ($\alpha{\leq}0.25$) and the consistently detectable regime ($\alpha{\geq}0.75$).
181	This seed dependence exemplifies our central argument: even within a single regime and method, stochastic variation in training determines whether the consensus threshold is crossed.
182	At this boundary, canary sensitivity is metric-dependent: token entropy fails to reach FDR significance in any seed ($p_{\text{fdr}}{\geq}0.086$), while ECE achieves significance in the two signal-positive seeds (s43, s44), identifying ECE as the more sensitive canary at the onset boundary.
183	Figure~\ref{fig:consensus_heatmap} visualizes this interaction across all method$\times\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.
184	
185	
186	\subsection{Case Study: Canary Prediction of Diversity Collapse}
187	\label{sec:case_study}
188	
189	Having established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).
190	We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
191	
192	\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
193	Token entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \S\ref{sec:discussion}).
194	Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.
195	Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
196	Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
197	Reverse-direction tests (downstream$\to$canary) find \textbf{0/24} FDR-significant (all $p{>}0.49$), establishing complete directional asymmetry.
198	
199	\begin{figure}[t]
200	\centering
201	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
202	\caption{Metric trajectories across 10 generations at $\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}
203	\label{fig:metric_trajectory}
204	\end{figure}
205	
206	\paragraph{High contamination ($\alpha{=}0.75$, 3 seeds).}
207	Directional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 19/24 forward pairs FDR-significant, 0/24 reverse).
208	However, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\alpha{=}0.75$ squarely in the transitional detection regime.
209	Differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\S\ref{sec:pitfalls}).
210	
211	\paragraph{ECE as a conditional secondary canary.}
212	ECE's forward consensus matches token entropy (both achieve PermG\_fwd 6/8 across all conditions), but the reverse profile diverges sharply.
213	Across 7 validated conditions (3 architectures $\times$ 2 scales $\times$ 2 domains), token entropy reverse direction yields \textbf{0/28} FDR-significant pairs (consistent unidirectional causality), while ECE reverse direction yields \textbf{13/28} significant pairs, with 5/7 conditions containing at least one reverse-significant pair, all in the distinct$\to$ECE direction.
214	This bidirectional coupling is the core reason ECE is classified as a secondary canary: ECE and diversity exhibit mutual feedback, and the interpretability of ECE's causal direction is correspondingly limited.
215	This result also instantiates Claim~3 (method sensitivity): when only forward significance is considered, the two canary types appear equivalent; incorporating reverse-direction tests separates them. The choice of analysis dimension alters the canary classification itself.
216	
217	\paragraph{Failed canary candidates.}
218	Not all metrics serve as canaries.
219	Effective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.
220	Effective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\alpha{=}0.25$ it \emph{increases} from 2.37 to 8.48 (+258\%).
221	The GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.
222	This opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\S\ref{sec:discussion}).
223	
224	\paragraph{Consensus filtering.}
225	Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
226	The 10 eliminated pairs comprise all canary$\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).
227	The consensus framework reduces the naive 100\% significance rate to the 37.5\% rate supported by the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
228	
229	
230	\subsection{Consensus Framework Validation}
231	\label{sec:consensus_validation}
232	
233	We validate the consensus framework's calibration using built-in experimental controls.
234	
235	\paragraph{False positive rate.}
236	At $\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.
237	Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation) through 37.5\% (differenced) and 20.8\% (threshold) down to \textbf{0\%} (permutation Granger: 0/24 across all three seeds).
238	The consensus framework at $K{\geq}4/5$ achieves \textbf{FPR${=}$0\%} (0/24 pairs, three independent seeds), matching the best individual methods while providing robustness against miscalibration of any single method (Table~\ref{tab:fpr_fnr}).
239	
240	\paragraph{False negative rate.}
241	At $\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\geq}3\times$ the $\alpha{=}0.0$ baseline (entropy $11.93\times$, ECE $73.12\times$) and canary onset strictly preceding downstream onset by ${\geq}1$ generation (\S\ref{sec:calibration}).
242	FNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\geq}3/4$, $S{\geq}3/4$, all~6 are recovered (\textbf{FNR${=}$0\%}).
243	Toda--Yamamoto alone yields FNR${=}$33.3\% (2/6), missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
244	Both FPR and FNR are validated on the joint method${\times}$seed dimension (FPR: 3~seeds at $\alpha{=}0.0$; FNR: 4~seeds at $\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\geq}4/5$).
245	Table~\ref{tab:fpr_fnr} reports the calibration results.
246	Table~\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\alpha$ including the null control, Toda--Yamamoto misses true signals at $\alpha{=}0.75$, while the consensus at $K{\geq}3$ yields the correct verdict across all five contamination levels.
247	
248	\begin{table}[t]
249	\centering
250	\caption{Single-method inference errors across contamination levels.
251	Each cell shows the verdict (significant or not) based on multi-seed majority ($\geq$2/3 seeds with $\geq$4/8 pairs significant).
252	\checkmark\ = correct, \textcolor{red}{FP} = false positive, \textcolor{blue}{FN} = false negative, $\circ$ = ambiguous ground truth (either verdict plausible).
253	Naive XCorr produces false positives at \emph{every} $\alpha$ including the null control, while TY Granger misses true signals at $\alpha{=}0.75$.
254	Only the multi-method consensus ($K{\geq}3$) yields the correct verdict at all five contamination levels.}
255	\label{tab:single-method-errors}
256	\resizebox{\columnwidth}{!}{%
257	\begin{tabular}{lccccc}
258	\toprule
259	 & \multicolumn{2}{c}{\textit{No signal}} & \textit{Ambiguous} & \multicolumn{2}{c}{\textit{Causal signal}} \\
260	\cmidrule(lr){2-3} \cmidrule(lr){4-4} \cmidrule(lr){5-6}
261	Method & $\alpha{=}0.00$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.00$ \\
262	\midrule
263	Naive XCorr
264	  & \textcolor{red}{FP}{\scriptsize\ 8,7,8}
265	  & \textcolor{red}{FP}{\scriptsize\ 8,8}
266	  & $\circ${\scriptsize\ 8,8,8}
267	  & \checkmark{\scriptsize\ 8,8,8}
268	  & \checkmark{\scriptsize\ 8,8,8} \\
269	Diff XCorr (FDR)
270	  & \checkmark{\scriptsize\ 4,3,3}
271	  & \checkmark{\scriptsize\ 3,1}
272	  & $\circ${\scriptsize\ 8,6,6}
273	  & \checkmark{\scriptsize\ 8,8,8}
274	  & \checkmark{\scriptsize\ 8,8,8} \\
275	Threshold Onset
276	  & \checkmark{\scriptsize\ 3,1,1}
277	  & \checkmark{\scriptsize\ 0,0}
278	  & $\circ${\scriptsize\ 0,0,0}
279	  & \checkmark{\scriptsize\ 4,0,4}
280	  & \checkmark{\scriptsize\ 8,8,8} \\
281	Perm Granger (FDR)
282	  & \checkmark{\scriptsize\ 0,0,0}
283	  & \checkmark{\scriptsize\ 0,0}
284	  & $\circ${\scriptsize\ 0,6,3}
285	  & \checkmark{\scriptsize\ 8,5,6}
286	  & \checkmark{\scriptsize\ 6,6,6} \\
287	TY Granger
288	  & \checkmark{\scriptsize\ 1,1,0}
289	  & \checkmark{\scriptsize\ 0,2}
290	  & $\circ${\scriptsize\ 0,0,0}
291	  & \textcolor{blue}{FN}{\scriptsize\ 1,1,1}
292	  & \checkmark{\scriptsize\ 6,6,4} \\
293	\midrule
294	\textbf{Consensus ($K{\geq}3$)}
295	  & \checkmark
296	  & \checkmark
297	  & $\circ$
298	  & \checkmark
299	  & \checkmark \\
300	\bottomrule
301	\multicolumn{6}{l}{\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\
302	\multicolumn{6}{l}{\footnotesize Seeds: $\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\alpha{=}0.25$: 43, 44; $\alpha{=}1.00$: 42, 43, 45.} \\
303	\end{tabular}%
304	}
305	\end{table}
306	
307	\paragraph{Bootstrap power analysis.}
308	To quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\alpha{=}1.0$).
309	Permutation Granger achieves power${=}1.0$ on genuine pairs (canary$\to$diversity) and power${=}0.0$ on spurious pairs (canary$\to$perplexity), providing clean separation.
310	Toda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\max}$), confirming its poor sensitivity at $T{=}10$.
311	We note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\beta{=}0.3$).
312	
313	\begin{table}[t]
314	\centering
315	\small
316	\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\geq}4/5$ achieves FPR${=}$0\% and FNR${=}$0\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}
317	\label{tab:fpr_fnr}
318	\begin{tabular}{lcc}
319	\toprule
320	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
321	\midrule
322	Naive XCorr              & 100\%              & 0\%  \\
323	Differenced XCorr        & 37.5\%             & 0\%  \\
324	Threshold Onset          & 20.8\% (12.5--37.5) & 0\%  \\
325	Permutation Granger      & 0\%                & 0\%  \\
326	Toda--Yamamoto           & 4.2\% (0--12.5)    & 33.3\% \\
327	\midrule
328	Consensus ($K{\geq}4/5$)              & 0\%    & 0\%  \\
329	Consensus ($K{\geq}4/5$, $S{\geq}3/4$) & 0\%    & 0\%  \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	
335	\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}
336	\label{sec:generalization}
337	
338	The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).
339	To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
340	All conditions use $\alpha{=}1.0$; architecture conditions use a single seed, while scale and domain conditions use two seeds (s42, s43) to assess replicability.
341	
342	\begin{table}[t]
343	\centering
344	\small
345	\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\alpha{=}1.0$, $n_{\text{perm}}{=}5{,}000$). Each cell reports the fraction of 8~canary$\to$downstream pairs per condition reaching BH-corrected FDR significance ($q{=}0.05$), with two seeds (s42, s43) to assess replicability for scale and domain conditions. MMCT: weighted forward consensus (\S\ref{sec:mmct}).}
346	\label{tab:generalization}
347	\resizebox{\columnwidth}{!}{%
348	\begin{tabular}{llcccccccc}
349	\toprule
350	Variation & Model / Dataset & \rotatebox{70}{Naive} & \rotatebox{70}{Diff.\ XCorr} & \rotatebox{70}{Threshold} & \rotatebox{70}{PermG (fwd)} & \rotatebox{70}{PermG (rev)} & \rotatebox{70}{TY} & \rotatebox{70}{$K{\geq}4/5$} & \rotatebox{70}{MMCT} \\
351	\midrule
352	Baseline & Pythia-410M / Wiki & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 & 5/8 \\
353	Architecture & GPT-2-medium / Wiki & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 5/8 & 6/8 & \textbf{8/8} \\
354	Architecture & OPT-1.3B / Wiki & 8/8 & 6/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 & 5/8 \\
355	Scale ($3.4\times$) & Pythia-1.4B / Wiki (s42) & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 & 4/8 \\
356	Scale ($3.4\times$) & Pythia-1.4B / Wiki (s43) & 8/8 & 6/8 & 8/8 & 6/8 & 2/8 & 4/8 & 6/8 & 4/8 \\
357	\addlinespace
358	Domain & Pythia-1B / C4 (s42) & 8/8 & 6/8 & 8/8 & 6/8 & 3/8 & 3/8 & 6/8 & 5/8 \\
359	Domain & Pythia-1B / C4 (s43) & 8/8 & 6/8 & 8/8 & 6/8 & 0/8 & 3/8 & 6/8 & 4/8 \\
360	\bottomrule
361	\multicolumn{10}{l}{\footnotesize PG reverse significance arises from distinct$\to$ECE bidirectional coupling (\S\ref{sec:case_study}).} \\
362	\multicolumn{10}{l}{\footnotesize MMCT exceeds $K{\geq}4/5$ on GPT-2-medium (8/8 vs.\ 6/8); see \S\ref{sec:mmct} for weighting details.} \\
363	\end{tabular}%
364	}
365	\end{table}
366	
367	\paragraph{Architecture generalization.}
368	Table~\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.
369	All models reach Tier~3 consensus ($K{\geq}4/5$) with 6/8 canary$\to$downstream pairs confirmed.
370	Permutation Granger forward significance is consistent across architectures (6/8 in all three), while reverse significance ranges from 2/8 to 3/8, concentrated in distinct$\to$ECE pairs consistent with the bidirectional coupling identified in \S\ref{sec:case_study}.
371	
372	Method-level variation across architectures is informative.
373	Threshold onset detection reaches 8/8 on both GPT-2-medium and OPT-1.3B, where token entropy exhibits a pronounced generation-0$\to$1 discontinuity that cleanly exceeds the onset threshold.
374	Toda--Yamamoto ranges from 4/8 (Pythia-410M) to 6/8 (OPT-1.3B), with GPT-2-medium at 5/8, consistent with its known sensitivity to residual degrees of freedom at short series lengths (\S\ref{sec:consensus_validation}).
375	All three architectures converge at $K{\geq}4/5$ consensus (6/8 each).
376	MMCT weighted consensus (\S\ref{sec:mmct}) exceeds the uniform threshold on GPT-2-medium (8/8 vs.\ 6/8), demonstrating that FPR-inverse weighting recovers additional signal that the ad-hoc $K{\geq}4/5$ threshold misses.
377	
378	\paragraph{Cross-condition patterns.}
379	Two structural patterns emerge across all generalization conditions.
380	First, canary$\to$perplexity pairs yield 0/14 at $K{\geq}4/5$ consensus across all conditions in Table~\ref{tab:generalization}, confirming that the spurious-channel finding from \S\ref{sec:method_sensitivity} is not architecture-specific but a structural property of the canary$\to$perplexity relationship: perplexity co-moves synchronously with canary metrics rather than lagging them, regardless of model family or training domain.
381	This elevates the perplexity channel result from a single-condition diagnostic (\S\ref{sec:case_study}) to a cross-validated finding: diversity collapse is the predictable downstream dimension, perplexity is not.
382	Second, restricting to canary$\to$diversity pairs (excluding the structurally non-predictable perplexity channel), 41 of 42 pairs across all conditions achieve $K{\geq}4/5$ consensus (97.6\%), with the sole exception in the Pythia-1.4B seed=42 condition.
383	This near-perfect diversity-specific consensus validates that the framework reliably identifies the predictable dimension of iterative training collapse across architectures, scales, and domains.
384	
385	\paragraph{Scale generalization.}
386	Scaling from 410M to 1.4B parameters within the Pythia family yields seed-dependent consensus.
387	Seed 42 produces $K{\geq}4/5{=}5/8$ with permutation Granger at 5/8 forward and 0/8 reverse, while seed 43 produces $K{\geq}4/5{=}6/8$ with 6/8 forward and 2/8 reverse (Table~\ref{tab:generalization}).
388	The weaker seed-42 result (the only condition below 6/8 consensus) reflects Toda--Yamamoto yielding 0/8, consistent with its known power limitations at short series lengths.
389	Permutation Granger reverse pairs that reach significance (2/8 in s43) all involve ECE in the distinct$\to$ECE direction, consistent with the bidirectional coupling pattern observed in the baseline (\S\ref{sec:case_study}).
390	Token entropy maintains 0/8 reverse across both seeds.
391	
392	\paragraph{Domain generalization.}
393	Replacing WikiText-103 with C4 confirms that the lead-lag pattern is not an artifact of narrow topical distribution.
394	Pythia-1B on C4 achieves $K{\geq}4/5{=}6/8$ in both seeds (s42, s43), with permutation Granger at 6/8 forward in both seeds.
395	Reverse significance is seed-dependent: s42 yields 3/8 reverse (all ECE pairs) while s43 yields 0/8 reverse, consistent with ECE's bidirectional coupling being more pronounced in certain stochastic realizations.
396	Token entropy maintains perfect unidirectionality (0/4 reverse) in both seeds, confirming its superiority as a directional canary across domains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebe08803-8675-4a5e-91be-79f885dda374",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "9a1044fe-727b-46ca-8cd7-166f65c7f09c",
  "sourceToolAssistantUUID": "ebe08803-8675-4a5e-91be-79f885dda374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-18T21:17:44.502Z_

Perfect! I found the complete definition of Table 7. Let me also check if there are any artifact versions to make sure I have the most complete information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a1044fe-727b-46ca-8cd7-166f65c7f09c",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjJhoZTndEHfR6TYcjK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dcea0cad-55fe-49b3-8044-c18f6218bc1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FDmmmUNL83PD787qPDPtzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 14442,
      "cache_read_input_tokens": 21813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14442,
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

_source line 19 · 2026-05-18T21:17:45.273Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RMpAS2z8b9nMi4dCkFSuR7`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts -name \"*generalization*\" -o -name \"*table7*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcea0cad-55fe-49b3-8044-c18f6218bc1c",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjJhoZTndEHfR6TYcjK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39b4e48f-9513-42aa-9893-659f8bd470b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FDmmmUNL83PD787qPDPtzX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 14442,
      "cache_read_input_tokens": 21813,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 138,
          "cache_read_input_tokens": 21813,
          "cache_creation_input_tokens": 14442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14442,
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

_source line 20 · 2026-05-18T21:17:45.325Z_

<details><summary>↩ Tool result · `toolu_01RMpAS2z8b9nMi4dCkFSuR7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/generalization_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/intermediate/generalization_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/generalization_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/gen_wiki_gpt2m_a100_s42_v4/report/gpt2m_wiki_8pair_table7_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/generalization_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39b4e48f-9513-42aa-9893-659f8bd470b5",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "2993d19a-ed2e-41a7-bb78-49f08645e401",
  "sourceToolAssistantUUID": "39b4e48f-9513-42aa-9893-659f8bd470b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-18T21:17:46.589Z_

Great! Let me check the artifact versions and the generalization draft to see if there are any additional details:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2993d19a-ed2e-41a7-bb78-49f08645e401",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjJwNtLUgqAvA8Zd3XP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e9465741-f42a-46c4-9970-1f4703788ece",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FvbTvPAVSx9HFAETU7kqJr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 36255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 381,
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

_source line 22 · 2026-05-18T21:17:47.021Z_

<details open><summary>🔧 Tool call — Read · `toolu_018BEeEP19nbCRKzpgGN4GBX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/generalization_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9465741-f42a-46c4-9970-1f4703788ece",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjJwNtLUgqAvA8Zd3XP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d25cb68f-eb06-4dca-aa53-fc621c564891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FvbTvPAVSx9HFAETU7kqJr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 36255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 381,
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

_source line 23 · 2026-05-18T21:17:47.028Z_

<details><summary>↩ Tool result · `toolu_018BEeEP19nbCRKzpgGN4GBX`</summary>

```text
1	% ============================================================
2	% generalization_draft.tex
3	% Pre-drafted paragraphs and table structure for §5.5
4	% (Cross-Architecture and Cross-Domain Generalization)
5	%
6	% STATUS: Draft with placeholders. Awaiting Phase 2 results.
7	%
8	% PLACEHOLDERS:
9	%   \textbf{XX}  — numeric value to fill from experiment
10	%   \textbf{[TBD]}  — entire row/cell pending experiment completion
11	%   VERSION A / VERSION B — pick one after results are in
12	%
13	% USAGE: Copy relevant pieces into docs/paper/experiments.tex §5.5
14	%        after results arrive. Do NOT edit this file as ground truth.
15	% ============================================================
16	
17	
18	% ============================================================
19	% TABLE: Generalization summary (replaces skeleton in experiments.tex)
20	% ============================================================
21	
22	\begin{table}[t]
23	\centering
24	\small
25	\caption{Generalization of lead-lag detectability across model scale,
26	architecture family, and training domain ($\alpha{=}1.0$, single seed
27	per condition). Each cell reports the fraction of 8 canary$\to$downstream
28	pairs (token entropy and ECE $\times$ 4 downstream metrics) reaching
29	BH-corrected FDR significance ($q{=}0.05$). Direction asymmetry shows
30	forward vs.\ reverse permutation Granger significance. The baseline row
31	reproduces the single-seed Pythia-410M result for comparison; 4-seed
32	pooled rates are reported in Table~\ref{tab:method_comparison}.
33	``Key canary'' identifies the metric with the strongest consensus
34	signal in each condition.}
35	\label{tab:generalization}
36	\begin{tabular}{llcccccc}
37	\toprule
38	Variation & Model / Dataset
39	  & \rotatebox{70}{Naive XCorr}
40	  & \rotatebox{70}{Diff.\ XCorr}
41	  & \rotatebox{70}{Threshold}
42	  & \rotatebox{70}{PermG (fwd/rev)}
43	  & \rotatebox{70}{TY}
44	  & \rotatebox{70}{$K{\geq}4/5$} \\
45	\midrule
46	Baseline
47	  & Pythia-410M / WikiText
48	  & 8/8 & 8/8 & 8/8 & 6/8\,/\,0/8 & 4/8 & 6/8 \\
49	\addlinespace
50	Scale
51	  & Pythia-410M / WikiText  % <-- reference row for scale comparison
52	  & 8/8 & 8/8 & 8/8 & 6/8\,/\,0/8 & 4/8 & 6/8 \\
53	  % FILL: Pythia-410M row is duplicated as reference; remove if redundant
54	Scale
55	  & Pythia-1.4B / WikiText  % <-- NEW: scale variation (same family, 3.4x params)
56	  & \textbf{XX} & \textbf{XX} & \textbf{XX}
57	  & \textbf{XX}\,/\,\textbf{XX} & \textbf{XX} & \textbf{XX} \\
58	\addlinespace
59	Architecture
60	  & OPT-1.3B / WikiText  % <-- NEW: different model family
61	  & \textbf{XX} & \textbf{XX} & \textbf{XX}
62	  & \textbf{XX}\,/\,\textbf{XX} & \textbf{XX} & \textbf{XX} \\
63	\addlinespace
64	Domain
65	  & Pythia-1B / C4  % <-- NEW: different training domain
66	  & \textbf{XX} & \textbf{XX} & \textbf{XX}
67	  & \textbf{XX}\,/\,\textbf{XX} & \textbf{XX} & \textbf{XX} \\
68	\addlinespace
69	Cross-arch
70	  & GPT-2-medium / WikiText  % <-- existing result from discussion.tex
71	  & 8/8 & 6/6 & 6/6 & 6/6\,/\,0/6 & 1/6 & 6/6 \\
72	\bottomrule
73	\end{tabular}
74	\end{table}
75	
76	
77	% ============================================================
78	% TABLE: Generalization drift profile (supplementary detail)
79	% ============================================================
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{Metric drift (\%, generation~0$\to$10) for generalization
85	conditions at $\alpha{=}1.0$ (single seed). The baseline Pythia-410M
86	drift is the 4-seed mean from Table~\ref{tab:drift_summary}. Entropy
87	and ECE drift magnitudes that exceed baseline indicate stronger canary
88	signals; distinct-$n$ drift magnitudes indicate comparable diversity
89	collapse across conditions.}
90	\label{tab:generalization_drift}
91	\begin{tabular}{llccccc}
92	\toprule
93	Variation & Model / Dataset & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
94	\midrule
95	Baseline  & Pythia-410M / Wiki
96	  & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
97	Scale     & Pythia-1.4B / Wiki
98	  & \textbf{XX} & \textbf{XX} & \textbf{XX} & \textbf{XX} & \textbf{XX} \\
99	Arch      & OPT-1.3B / Wiki
100	  & \textbf{XX} & \textbf{XX} & \textbf{XX} & \textbf{XX} & \textbf{XX} \\
101	Domain    & Pythia-1B / C4
102	  & \textbf{XX} & \textbf{XX} & \textbf{XX} & \textbf{XX} & \textbf{XX} \\
103	Cross-arch & GPT-2-medium / Wiki
104	  & $-$\textbf{XX} & $+$\textbf{XX} & $-$\textbf{XX} & $-$\textbf{XX} & $+$\textbf{XX} \\
105	  % NOTE: GPT-2m α=1.0 drift numbers are in discussion.tex but not tabulated.
106	  % Extract from gen_wiki_gpt2m_a100_s42_v3 results when filling.
107	\bottomrule
108	\end{tabular}
109	\end{table}
110	
111	
112	% ============================================================
113	% VERSION A: All generalization conditions confirm the pattern
114	% ============================================================
115	
116	% Use this version if: Pythia-1.4B, OPT-1.3B, and Pythia-1B/C4 all show
117	% PermG forward significance >= 4/8 with reverse ~0/8, and consensus
118	% K>=4/5 yields >= 4/8 pairs.
119	
120	\paragraph{Generalization design.}
121	% WHY generalization matters (reviewer pre-emption)
122	The method sensitivity, regime dependence, and consensus results above
123	are calibrated on a single model family and dataset (Pythia-410M,
124	WikiText-103). A reviewer could reasonably question whether these
125	findings reflect architecture-specific artifacts or dataset-specific
126	distributional properties rather than general characteristics of
127	iterative training collapse. We test three orthogonal generalization
128	axes: model scale (Pythia-410M $\to$ Pythia-1.4B, same family, 3.4$\times$
129	parameters), architecture family (Pythia $\to$ OPT-1.3B, different
130	model family with different tokenizer and pre-training corpus), and
131	training domain (WikiText-103 $\to$ C4, web-scale versus curated text).
132	Each condition uses the full five-method panel and consensus pipeline at
133	$\alpha{=}1.0$, the regime where the baseline yields unambiguous Tier~3
134	consensus.
135	
136	\paragraph{Scale invariance.}
137	Scaling from 410M to 1.4B parameters within the Pythia family preserves
138	the core pattern. Permutation Granger identifies \textbf{XX}/8
139	forward-direction pairs as FDR-significant with \textbf{XX}/8 reverse,
140	confirming directional asymmetry at a scale 3.4$\times$ larger than the
141	baseline. Consensus at $K{\geq}4/5$ yields \textbf{XX}/8 pairs, compared
142	to 6/8 in the baseline (Table~\ref{tab:generalization}). Metric drift
143	magnitudes are \textbf{comparable to / larger than / smaller than}
144	% FILL: pick one based on results
145	the 410M baseline (Table~\ref{tab:generalization_drift}), indicating
146	that the canary signal \textbf{scales proportionally with / is
147	independent of / attenuates with} model capacity.
148	% FILL: pick one
149	
150	\paragraph{Architecture invariance.}
151	OPT-1.3B uses a different tokenizer (GPT-2 BPE vs.\ NeoX), different
152	pre-training corpus (a subset of The Pile vs.\ The Pile), and different
153	architectural choices (learned positional embeddings vs.\ rotary).
154	Despite these differences, the consensus pipeline produces \textbf{XX}/8
155	Tier~3 pairs with permutation Granger forward significance at
156	\textbf{XX}/8 and reverse at \textbf{XX}/8
157	(Table~\ref{tab:generalization}). Combined with the GPT-2-medium result
158	(6/6 Tier~3; \S\ref{sec:discussion}), this places three distinct
159	decoder-only transformer families in the Confirmatory regime at
160	$\alpha{=}1.0$, consistent with the hypothesis that the entropy-precedes-diversity
161	pattern reflects a general property of autoregressive collapse rather
162	than an architecture-specific coincidence.
163	
164	\paragraph{Domain invariance.}
165	Replacing WikiText-103 with C4 (a web-crawled corpus with different
166	distributional characteristics, vocabulary coverage, and domain
167	composition) tests whether the lead-lag pattern depends on the training
168	data distribution. Pythia-1B trained on C4 yields \textbf{XX}/8
169	forward-direction permutation Granger pairs with \textbf{XX}/8 reverse,
170	and consensus $K{\geq}4/5$ at \textbf{XX}/8
171	(Table~\ref{tab:generalization}). The result confirms that the canary
172	signal is not an artifact of WikiText's narrow topical distribution.
173	% NOTE: If C4 results differ from WikiText, add a sentence about
174	% domain-specific onset boundaries.
175	
176	\paragraph{Cross-condition consistency.}
177	Across all four generalization conditions (including GPT-2-medium from
178	\S\ref{sec:discussion}), the consensus framework produces a consistent
179	pattern: correlation-based methods find near-universal significance,
180	permutation Granger confirms directional asymmetry with forward
181	$\gg$ reverse, and Toda--Yamamoto shows reduced sensitivity consistent
182	with the short-series power limitation identified in
183	\S\ref{sec:consensus_validation}. The three methodological pitfalls
184	(method sensitivity, regime dependence, and preprocessing sensitivity)
185	are replicated in every condition tested, confirming that these pitfalls
186	are structural properties of lead-lag analysis in iterative training
187	rather than artifacts of a specific experimental configuration.
188	
189	
190	% ============================================================
191	% VERSION B: Partial generalization (some conditions fail or differ)
192	% ============================================================
193	
194	% Use this version if: one or more conditions show PermG forward < 4/8,
195	% or consensus K>=4/5 yields < 4/8, or reverse direction is non-zero,
196	% or drift patterns diverge qualitatively.
197	
198	\paragraph{Generalization design.}
199	% (Same as VERSION A — copy the paragraph above)
200	The method sensitivity, regime dependence, and consensus results above
201	are calibrated on a single model family and dataset (Pythia-410M,
202	WikiText-103). A reviewer could reasonably question whether these
203	findings reflect architecture-specific artifacts or dataset-specific
204	distributional properties rather than general characteristics of
205	iterative training collapse. We test three orthogonal generalization
206	axes: model scale (Pythia-410M $\to$ Pythia-1.4B, same family, 3.4$\times$
207	parameters), architecture family (Pythia $\to$ OPT-1.3B, different
208	model family with different tokenizer and pre-training corpus), and
209	training domain (WikiText-103 $\to$ C4, web-scale versus curated text).
210	Each condition uses the full five-method panel and consensus pipeline at
211	$\alpha{=}1.0$.
212	
213	\paragraph{Scale and architecture variation.}
214	Scaling to Pythia-1.4B preserves directional asymmetry (permutation Granger:
215	\textbf{XX}/8 forward, \textbf{XX}/8 reverse) with consensus $K{\geq}4/5$
216	at \textbf{XX}/8 pairs, consistent with the 410M baseline. OPT-1.3B
217	\textbf{also confirms / partially confirms / does not replicate} the
218	pattern:
219	% FILL: pick one and continue based on results
220	permutation Granger yields \textbf{XX}/8 forward and \textbf{XX}/8
221	reverse. The reduced consensus rate in OPT-1.3B
222	% (if applicable)
223	may reflect its different tokenizer granularity, which alters how token
224	entropy aggregates distributional information, or its different
225	pre-training distribution, which shifts the baseline metric trajectories
226	in ways that affect Granger-test power at $T{=}10$.
227	% NOTE: Expand this explanation based on which specific methods fail.
228	
229	\paragraph{Domain sensitivity.}
230	The C4 condition reveals that training domain affects lead-lag
231	detectability. Pythia-1B on C4 yields \textbf{XX}/8 permutation Granger
232	forward pairs (compared to \textbf{XX}/8 on WikiText), with consensus
233	$K{\geq}4/5$ at \textbf{XX}/8. The weaker signal
234	% (if applicable — adjust if C4 is actually stronger)
235	is consistent with C4's higher lexical diversity reducing the
236	signal-to-noise ratio for diversity metrics: when the baseline vocabulary
237	usage is more uniform, collapse-induced diversity reduction produces
238	smaller absolute changes in distinct-$n$, pushing temporal leads below
239	the statistical detection floor.
240	% NOTE: If C4 is the condition that fails, this paragraph becomes the
241	% key result. If C4 works fine, merge with VERSION A paragraphs.
242	
243	\paragraph{Boundary conditions for generalization.}
244	The partial generalization results define boundary conditions for the
245	consensus framework. The three pitfalls (method sensitivity, regime
246	dependence, preprocessing sensitivity) replicate across all conditions
247	tested, confirming their structural nature. The canary prediction
248	pattern (entropy precedes diversity) holds in \textbf{XX} of
249	\textbf{XX} conditions at $\alpha{=}1.0$, with the
250	\textbf{[condition name]} condition representing a boundary case where
251	\textbf{[specific finding]}. This result refines rather than undermines
252	the framework: the consensus pipeline correctly identifies weaker signals
253	as sub-threshold rather than producing false confirmations, demonstrating
254	that the $K{\geq}4/5$ threshold is appropriately conservative across
255	diverse experimental conditions.
256	% NOTE: This "boundary conditions" framing turns partial failure into
257	% a positive narrative — the framework correctly identifies limits.
258	
259	
260	% ============================================================
261	% NOTES FOR FILLING IN RESULTS
262	% ============================================================
263	
264	% 1. For each new condition, run the full analysis pipeline:
265	%    - Metric drift (gen 0→10) for all 5 metrics
266	%    - Five-method panel: naive XCorr, diff XCorr, threshold, PermG, TY
267	%    - PermG forward and reverse counts (out of 8 pairs)
268	%    - Consensus K>=4/5 count
269	%    - Direction asymmetry (forward - reverse)
270	%
271	% 2. Decision rule for VERSION A vs B:
272	%    - VERSION A if ALL conditions show PermG fwd >= 4/8, rev <= 1/8,
273	%      and K>=4/5 >= 4/8
274	%    - VERSION B if ANY condition shows PermG fwd < 4/8 OR rev >= 2/8
275	%      OR K>=4/5 < 4/8
276	%    - For mixed results, use VERSION B structure but incorporate
277	%      VERSION A paragraphs for conditions that do work
278	%
279	% 3. After filling numbers:
280	%    - Run: grep "—" generalization_draft.tex  (must be zero)
281	%    - Run: grep "ing," generalization_draft.tex  (review each match)
282	%    - Check all XX placeholders are replaced
283	%    - Verify narrative consistency with Abstract and Introduction
284	%
285	% 4. Integration with existing paper:
286	%    - This replaces the skeleton in experiments.tex §5.5 (lines 330-352)
287	%    - The GPT-2m cross-arch data stays in discussion.tex but is
288	%      referenced here via the table
289	%    - Update Abstract if generalization results are strong enough
290	%      to mention (VERSION A only)
291	%    - Update Contribution list in Introduction if adding a new
292	%      generalization contribution bullet
293	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d25cb68f-eb06-4dca-aa53-fc621c564891",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "8cc4b907-6839-4a22-ba84-f5467f21e00d",
  "sourceToolAssistantUUID": "d25cb68f-eb06-4dca-aa53-fc621c564891",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T21:17:47.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EyXDpezojPMJzZHfNt6uam`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/gen_wiki_gpt2m_a100_s42_v4/report/gpt2m_wiki_8pair_table7_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cc4b907-6839-4a22-ba84-f5467f21e00d",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjJwNtLUgqAvA8Zd3XP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "302548a1-21c2-4f79-9f14-46ed054816bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FvbTvPAVSx9HFAETU7kqJr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 381,
      "cache_read_input_tokens": 36255,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 381
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 216,
          "cache_read_input_tokens": 36255,
          "cache_creation_input_tokens": 381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 381,
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

_source line 25 · 2026-05-18T21:17:47.343Z_

<details><summary>↩ Tool result · `toolu_01EyXDpezojPMJzZHfNt6uam`</summary>

```text
1	# GPT-2-medium WikiText-103 8-Pair Table 7 Analysis
2	
3	**Experiment**: gen_wiki_gpt2m_a100_s42_v4
4	**Model**: gpt2-medium (355M)
5	**Dataset**: wikitext103_5k, alpha=1.0, seed=42
6	**Generations**: 11 (gen0-gen10), 5000 steps/gen
7	**Parameters**: n_perm=5000, xcorr_lag=5, granger_lag=1
8	
9	## Table 7 Row
10	
11	| Naive | Diff | Thresh | PG_fwd | PG_rev | TY | K>=4 |
12	|-------|------|--------|--------|--------|-----|------|
13	| 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 |
14	
15	## Per-Pair Detail
16	
17	| Pair | Naive | Diff(FDR) | Thresh | TY | PG_fwd | PG_rev | K |
18	|------|-------|-----------|--------|-----|--------|--------|---|
19	| ent->ppl | Y (p=0.0199) | Y (q=0.0016) | Y (L=7) | N (p=0.9998) | N (p=0.4989) | N (p=0.1820) | 3/5 |
20	| ent->d1 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | N (p=0.1160) | Y (p=0.0006) | N (p=0.0964) | 4/5 |
21	| ent->d2 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | Y (p=0.0017) | Y (p=0.0020) | N (p=0.1052) | 5/5 |
22	| ent->d3 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | Y (p=0.0000) | Y (p=0.0024) | N (p=0.1062) | 5/5 |
23	| ece->ppl | Y (p=0.0076) | Y (q=0.0029) | Y (L=6) | N (p=0.2254) | N (p=0.8796) | N (p=0.6107) | 3/5 |
24	| ece->d1 | Y (p=0.0000) | Y (q=0.0007) | Y (L=1) | Y (p=0.0000) | Y (p=0.0006) | Y (p=0.0032) | 5/5 |
25	| ece->d2 | Y (p=0.0000) | Y (q=0.0000) | Y (L=1) | Y (p=0.0000) | Y (p=0.0010) | Y (p=0.0160) | 5/5 |
26	| ece->d3 | Y (p=0.0000) | Y (q=0.0000) | Y (L=1) | Y (p=0.0000) | Y (p=0.0010) | Y (p=0.0084) | 5/5 |
27	
28	## Drift Analysis (gen0 -> gen10)
29	
30	| Metric | Gen0 | Gen10 | Change% |
31	|--------|------|-------|---------|
32	| token_entropy | 3.5714 | 0.4794 | -86.6% |
33	| ece | 0.0112 | 0.5216 | +4571.9% |
34	| perplexity | 32.63 | 16520.55 | +50527.6% |
35	| distinct_1 | 0.1044 | 0.0918 | -12.1% |
36	| distinct_2 | 0.5483 | 0.4717 | -14.0% |
37	| distinct_3 | 0.8441 | 0.7394 | -12.4% |
38	| self_bleu | 0.0094 | 0.0119 | +25.9% |
39	| effective_rank | 2.3722 | 25.0018 | +953.9% |
40	| mauve | 0.0315 | 0.0339 | +7.9% |
41	
42	## Comparison with Other Conditions
43	
44	| Row | Naive | Diff | Thresh | PG fwd | PG rev | TY | K>=4 |
45	|-----|-------|------|--------|--------|--------|-----|------|
46	| Baseline (Pythia-410M) | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 4/8 | 6/8 |
47	| **GPT-2m (355M)** | **8/8** | **8/8** | **8/8** | **6/8** | **3/8** | **5/8** | **6/8** |
48	| OPT-1.3B | 8/8 | 6/8 | 8/8 | 6/8 | 2/8 | 6/8 | 6/8 |
49	| Pythia-1.4B s42 | 7/8 | 6/8 | 8/8 | 5/8 | 0/8 | 0/8 | 5/8 |
50	| C4 s42 | 8/8 | 6/8 | 8/8 | 6/8 | 3/8 | 3/8 | 6/8 |
51	
52	## Key Findings
53	
54	1. **K>=4 = 6/8**: Strong consensus, matching Baseline and OPT-1.3B level. GPT-2m confirms canary-downstream causal signal generalizes across architectures.
55	2. **Naive/Diff/Thresh all 8/8**: Perfect detection on correlation-based and threshold methods, consistent with strong monotonic degradation trends.
56	3. **PG_fwd = 6/8, PG_rev = 3/8**: Correct asymmetry (forward > reverse), confirming directional causality from canary to downstream.
57	4. **TY = 5/8**: Higher than Baseline (4/8), driven by ece->d1/d2/d3 and ent->d2/d3 pairs. The two ppl pairs fail TY (p=0.9998 and 0.2254), consistent with perplexity's delayed onset (L=6-7) reducing TY power.
58	5. **Perplexity explosion**: +50527.6% drift (32.6 -> 16520.5), the most extreme among all conditions, indicating severe model collapse in GPT-2m.
59	6. **Token entropy collapse**: -86.6% (3.57 -> 0.48), more severe than typical Pythia experiments, suggesting GPT-2m is more susceptible to distributional narrowing.
60	
61	## JSON Output
62	Full per-pair results saved to: `/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/analysis/gpt2m_8pair_table7.json`
63	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "302548a1-21c2-4f79-9f14-46ed054816bb",
  "isSidechain": true,
  "promptId": "0e22f213-588a-426c-aeb0-ca2bc344319a",
  "agentId": "a4362469ba847a909",
  "type": "user",
  "uuid": "83956b38-11dd-414a-8bbb-74709bd9af7e",
  "sourceToolAssistantUUID": "302548a1-21c2-4f79-9f14-46ed054816bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-18T21:17:58.099Z_

Perfect! Now I have a complete picture of Table 7. Let me provide a comprehensive report.

## Summary: Table 7 Definition and Format

**Table 7 Title**: "Generalization of lead-lag detectability across architecture, scale, and domain"

**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex` (lines 342-365)

### Table 7 Exact Columns:

The table has **9 columns**:

1. **Variation** - Row category (Baseline, Architecture, Scale, Domain)
2. **Model / Dataset** - Specific model name and training dataset (e.g., "Pythia-410M / Wiki", "GPT-2-medium / Wiki", "OPT-1.3B / Wiki", "Pythia-1.4B / Wiki", "Pythia-1B / C4")
3. **Naive** - Naive cross-correlation significance (fraction out of 8 pairs)
4. **Diff. XCorr** - Differenced cross-correlation FDR significance (fraction out of 8)
5. **Threshold** - Threshold onset detection significance (fraction out of 8)
6. **PermG (fwd)** - Permutation Granger forward direction significance (fraction out of 8)
7. **PermG (rev)** - Permutation Granger reverse direction significance (fraction out of 8)
8. **TY** - Toda-Yamamoto Granger significance (fraction out of 8)
9. **$K{\geq}4/5$** - Consensus threshold (K≥4/5 methods) significance (fraction out of 8)

### Row Format:

Each row contains:
- **Variation type** (Architecture | Scale | Domain)
- **Model/Dataset combination**
- **8 numeric cells** in format: **X/8** representing "number of 8 canary→downstream pairs" reaching BH-corrected FDR significance at q=0.05

### Key Details:

**Row Structure** (from the actual data in experiments.tex lines 352-360):
- Baseline: Pythia-410M / Wiki
- Architecture: GPT-2-medium / Wiki, OPT-1.3B / Wiki  
- Scale: Pythia-1.4B / Wiki (two seeds: s42, s43)
- Domain: Pythia-1B / C4 (two seeds: s42, s43)

**Data Format Per Cell**: Each cell reports the count of canary→downstream pairs (out of 8 total pairs: 2 canaries × 4 downstream metrics) that reach BH-corrected FDR significance (q=0.05).

**Specific Values** from the finalized table (lines 352-360):
```
Baseline | Pythia-410M / Wiki | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 4/8 | 6/8
Architecture | GPT-2-medium / Wiki | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8
Architecture | OPT-1.3B / Wiki | 8/8 | 6/8 | 8/8 | 6/8 | 2/8 | 6/8 | 6/8
Scale (3.4×) | Pythia-1.4B / Wiki (s42) | 7/8 | 6/8 | 8/8 | 5/8 | 0/8 | 0/8 | 5/8
Scale (3.4×) | Pythia-1.4B / Wiki (s43) | 8/8 | 6/8 | 8/8 | 6/8 | 2/8 | 4/8 | 6/8
Domain | Pythia-1B / C4 (s42) | 8/8 | 6/8 | 8/8 | 6/8 | 3/8 | 3/8 | 6/8
Domain | Pythia-1B / C4 (s43) | 8/8 | 6/8 | 8/8 | 6/8 | 0/8 | 3/8 | 6/8
```

### Experimental Settings for Table 7:
- **Contamination level**: α = 1.0 (full synthetic replacement)
- **Number of pairs tested**: 8 canary→downstream pairs (2 canaries: token entropy, ECE × 4 downstream metrics: Distinct-1, Distinct-2, Perplexity, and implicitly Distinct-3)
- **Seed coverage**: Architecture conditions use single seed (s42); Scale and Domain conditions use two seeds (s42, s43)
- **Permutation count**: n_perm = 5,000
- **Significance threshold**: BH-corrected FDR at q = 0.05

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83956b38-11dd-414a-8bbb-74709bd9af7e",
  "isSidechain": true,
  "agentId": "a4362469ba847a909",
  "requestId": "req_011CbAjK5qsYRVrm4z959uBn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "797250fd-d2da-4214-940a-af8dcd8aad50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "6c5856df-7e7e-4732-a15b-77014fe6cce0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KAK5MtRY4xaqGe3ULaYiLL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7154,
      "cache_read_input_tokens": 36636,
      "output_tokens": 1243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1243,
          "cache_read_input_tokens": 36636,
          "cache_creation_input_tokens": 7154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7154,
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
