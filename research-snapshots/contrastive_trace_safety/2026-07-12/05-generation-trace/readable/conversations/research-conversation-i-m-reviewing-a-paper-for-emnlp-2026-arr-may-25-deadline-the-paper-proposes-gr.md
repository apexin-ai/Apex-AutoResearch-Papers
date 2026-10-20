# Research conversation: I'm reviewing a paper for EMNLP 2026 (ARR May 25 deadline). The paper proposes "GranRoute" — learning to route retrieval

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a30cab4ee1ca19082.jsonl`
- **Structured JSON:** [`db26829cb0f34a18e1ab.json`](../../sessions/db/db26829cb0f34a18e1ab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-11T23:38:32.993Z_

I'm reviewing a paper for EMNLP 2026 (ARR May 25 deadline). The paper proposes "GranRoute" — learning to route retrieval configurations for code repair. I need to verify:

1. **EMNLP 2026 ARR deadline**: Search for "ARR May 2026 submission deadline EMNLP" to verify the May 25, 2026 deadline is correct and that EMNLP 2026 accepts from this cycle.

2. **EMNLP short paper page limit**: Search for "EMNLP 2026 short paper page limit" or "ARR short paper format 2026" — is 4 pages correct?

3. **Novelty check — routing for retrieval in code tasks**: Search for:
   - "adaptive retrieval strategy selection code 2025 2026" 
   - "learn to select retrieval granularity 2025 2026"
   - "routing retrieval configuration 2025 2026"
   Are there any papers that already do what GranRoute proposes (learning to select retrieval configuration for code tasks)?

4. **Venue fit**: Search for "EMNLP NLP and code models track" or "EMNLP code understanding papers 2024 2025" — does this type of routing/configuration selection work fit EMNLP's scope? Look for examples of similar SE-adjacent papers accepted at EMNLP.

5. **Multi-method comparison as contribution**: Search for "systematic comparison routing methods LLM 2025 2026" — is a multi-method comparison (comparing 5 training methods) a sufficiently novel contribution, or is it considered ablation-as-paper?

6. **Bradley-Terry preference loss for routing**: Search for "Bradley-Terry preference learning routing 2025 2026" — has Bradley-Terry been used for routing configuration selection before?

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "fe0da9dd-39f2-415b-a6fe-d14b8fae3dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:38:32.996Z_

```json
{
  "parentUuid": "fe0da9dd-39f2-415b-a6fe-d14b8fae3dd1",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c5f67334-2703-43ff-b2c0-753fcb7fb575",
  "timestamp": "2026-05-11T23:38:32.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:38:35.302Z_



I'll search for all these topics in parallel to help verify the details for your EMNLP 2026 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5f67334-2703-43ff-b2c0-753fcb7fb575",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPEjFuMPsh49EqapZS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "445870d1-f6da-4629-b8b9-0e10d3818546",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtkbuMZUwy7TwHLkcKXeSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 989,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 989,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:38:35.890Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P9TDarf1gF2cZa58Y4Q58c`</summary>

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
  "parentUuid": "445870d1-f6da-4629-b8b9-0e10d3818546",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPEjFuMPsh49EqapZS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9add383-4bc2-417c-8ee3-69544fadf5d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtkbuMZUwy7TwHLkcKXeSj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 989,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
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
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 989,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-11T23:38:35.893Z_

<details><summary>↩ Tool result · `toolu_01P9TDarf1gF2cZa58Y4Q58c`</summary>

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
  "parentUuid": "b9add383-4bc2-417c-8ee3-69544fadf5d3",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "443855b1-a73f-4d66-a586-ad8fdc005139",
  "sourceToolAssistantUUID": "b9add383-4bc2-417c-8ee3-69544fadf5d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:38:38.304Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "443855b1-a73f-4d66-a586-ad8fdc005139",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPTVDfvGCW3EZeJZBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9f17e14-0c52-4e87-9e63-37fe25691554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182zhVw81bdYTYrbViCEVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-11T23:38:38.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SDoHASEJT1PvQowZ9qsy4b`</summary>

```json
{
  "query": "ARR May 2026 submission deadline EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9f17e14-0c52-4e87-9e63-37fe25691554",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPTVDfvGCW3EZeJZBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9a59fd0-919e-4d28-b887-54a9b0b1d9b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182zhVw81bdYTYrbViCEVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-11T23:38:39.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LmrC3pAsKgAdKD3qYqS4jy`</summary>

```json
{
  "query": "EMNLP 2026 short paper page limit ARR short paper format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a59fd0-919e-4d28-b887-54a9b0b1d9b4",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPTVDfvGCW3EZeJZBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "971fb6a8-2e0e-45b3-b5e0-9d78361c3fd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182zhVw81bdYTYrbViCEVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-11T23:38:40.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bg3rmehgciBkvrhPmR9KQd`</summary>

```json
{
  "query": "adaptive retrieval strategy selection code repair 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "971fb6a8-2e0e-45b3-b5e0-9d78361c3fd9",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPTVDfvGCW3EZeJZBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc6b9928-37fc-4a5b-80dd-2c6620ed5be0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182zhVw81bdYTYrbViCEVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-11T23:38:40.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GA3JC14WVbMW9wsmftb9Dt`</summary>

```json
{
  "query": "learn to select retrieval granularity code 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc6b9928-37fc-4a5b-80dd-2c6620ed5be0",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPTVDfvGCW3EZeJZBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91cec306-e991-42dc-89f8-c27a57a2c446",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182zhVw81bdYTYrbViCEVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-11T23:38:41.148Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NiacRbujvsMX17RcSe2GJ1`</summary>

```json
{
  "query": "routing retrieval configuration code LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91cec306-e991-42dc-89f8-c27a57a2c446",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPTVDfvGCW3EZeJZBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "382a6e97-1e77-4e59-bec5-5320c45f3472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182zhVw81bdYTYrbViCEVFt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1421,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-11T23:38:41.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DaDiKpHdwt5hRYiniDgbFa`</summary>

```json
{
  "query": "EMNLP code understanding papers accepted 2024 2025 software engineering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "382a6e97-1e77-4e59-bec5-5320c45f3472",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfPTVDfvGCW3EZeJZBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d1020f8-987b-49b6-9cf2-e52470d69a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182zhVw81bdYTYrbViCEVFt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 9212,
      "output_tokens": 328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 328,
          "cache_read_input_tokens": 9212,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1421,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:38:43.429Z_

<details><summary>↩ Tool result · `toolu_01LmrC3pAsKgAdKD3qYqS4jy`</summary>

```text
Web search results for query: "EMNLP 2026 short paper page limit ARR short paper format"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here is the information about EMNLP 2026 short paper page limits and ARR format:

## EMNLP 2026 Short Paper Page Limit

EMNLP 2026 uses a two-column format with an 8-page limit for long papers and a 4-page limit for short papers.

## ARR Submission Requirements

Both long and short paper submissions should follow all of the ARR submission requirements. The submissions are made through the ACL Rolling Review (ARR) system, and short papers are limited to 4 pages.

## Key Dates

The ARR submission deadline for long and short papers is May 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "971fb6a8-2e0e-45b3-b5e0-9d78361c3fd9",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "af9ee320-692e-4b4e-8b94-178a962b9e06",
  "sourceToolAssistantUUID": "971fb6a8-2e0e-45b3-b5e0-9d78361c3fd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:38:43.914Z_

<details><summary>↩ Tool result · `toolu_01SDoHASEJT1PvQowZ9qsy4b`</summary>

```text
Web search results for query: "ARR May 2026 submission deadline EMNLP 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here are the key details about the ARR May 2026 submission deadline for EMNLP 2026:

## ARR May 2026 Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Important Related Deadlines

The reviewer registration deadline for all authors is May 27, 2026.

## Key Policy Update for May 2026 Cycle

Given that the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.

## Post-Submission Timeline

- Author response and author-reviewer discussion: July 7-13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9a59fd0-919e-4d28-b887-54a9b0b1d9b4",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "d883869f-5200-4b3d-beba-8de05db22fb4",
  "sourceToolAssistantUUID": "f9a59fd0-919e-4d28-b887-54a9b0b1d9b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:38:47.095Z_

<details><summary>↩ Tool result · `toolu_01DaDiKpHdwt5hRYiniDgbFa`</summary>

```text
Web search results for query: "EMNLP code understanding papers accepted 2024 2025 software engineering"

Links: [{"title":"15 Papers Accepted to EMNLP 2024 | Department of Computer Science, Columbia University","url":"https://www.cs.columbia.edu/2024/15-papers-accepted-to-emnlp-2024/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"EMNLP 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2024-paper-list/"},{"title":"Paper Digest: EMNLP 2024 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2024/11/emnlp-2024-papers-highlights/"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"},{"title":"10 Papers Accepted at EMNLP 2024","url":"https://www.a-star.edu.sg/cfar/news/news/features/10-papers-accepted-at-emnlp-2024"},{"title":"EMNLP.2025 - Findings | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025?group=Findings"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here's what I found about code understanding papers accepted at EMNLP 2024 and 2025:

## EMNLP 2025

One notable paper accepted to EMNLP 2025 is "Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs" by Dayu Yang, Tianyang Liu, Daoan Zhang, and others. This paper surveys the intersection of code understanding and LLM reasoning capabilities in software engineering contexts.

EMNLP 2025 accepted more than 2,000 papers overall, though my search results only provide limited visibility into the specific code understanding and software engineering papers.

## EMNLP 2024

EMNLP 2024 accepted more than 1,300 papers. While the search results don't provide a comprehensive list of code understanding papers from 2024, they indicate that the conference included papers across various NLP topics.

For a more comprehensive list of code understanding and software engineering papers from both conferences, you may want to visit the official EMNLP proceedings pages directly or use academic paper databases that allow filtering by topic area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d1020f8-987b-49b6-9cf2-e52470d69a24",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "a428a69b-3fac-4208-b29d-0b8b1b5672a6",
  "sourceToolAssistantUUID": "5d1020f8-987b-49b6-9cf2-e52470d69a24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T23:38:48.267Z_

<details><summary>↩ Tool result · `toolu_01GA3JC14WVbMW9wsmftb9Dt`</summary>

```text
Web search results for query: "learn to select retrieval granularity code 2025 2026"

Links: [{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"Dense XRetrieval: What Retrieval Granularity Should We ...","url":"https://aclanthology.org/2024.emnlp-main.845.pdf"},{"title":"Dense X Retrieval: What Retrieval Granularity Should We Use?","url":"https://chentong0.github.io/factoid-wiki/"},{"title":"RAG in 2025: 7 Proven Strategies to Deploy Retrieval-Augmented Generation at Scale | Morphik Blog","url":"https://www.morphik.ai/blog/retrieval-augmented-generation-strategies"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"RESCUE: Retrieval Augmented Secure Code Generation","url":"https://www.researchgate.net/publication/396747221_RESCUE_Retrieval_Augmented_Secure_Code_Generation"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.00456v1"},{"title":"[2312.06648] Dense X Retrieval: What Retrieval Granularity Should We Use?","url":"https://arxiv.org/abs/2312.06648"},{"title":"GitHub - chentong0/factoid-wiki: Dense X Retrieval: What Retrieval Granularity Should We Use? · GitHub","url":"https://github.com/chentong0/factoid-wiki"}]

Based on the search results, I found several relevant research papers and resources about retrieval granularity in code and information retrieval systems from 2025-2026:

## Key Research on Retrieval Granularity

**Dense X Retrieval Research**: When using a learned dense retriever on a retrieval corpus at inference time, an often-overlooked design choice is the retrieval unit in which the corpus is indexed (document, passage, or sentence), and the retrieval unit choice significantly impacts the performance of both retrieval and downstream tasks.

Researchers introduced a novel retrieval unit called "proposition" for dense retrieval, defined as atomic expressions within text, each encapsulating a distinct factoid and presented in a concise, self-contained natural language format. Indexing a corpus by fine-grained units such as propositions significantly outperforms passage-level units in retrieval tasks, and constructing prompts with fine-grained retrieved units for retrieval-augmented language models improves the performance of downstream QA tasks.

**Mix-of-Granularity Approach**: The Mix-of-Granularity (MoG) method dynamically determines the optimal granularity of a knowledge database based on input queries using a router that is efficiently trained with a newly proposed loss function employing soft labels.

**Code Generation with Retrieval**: Repository-Level Code Generation (RLCG) requires models to capture long-range dependencies and ensure global semantic consistency across multiple files or modules, and Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm to address these challenges, with recent surveys providing comprehensive reviews of Retrieval-Augmented Code Generation (RACG) focusing on repository-level approaches.

You can find implementations and datasets on GitHub, such as the FactoidWiki project that provides an English Wikipedia dump indexed at the level of propositions for retrieval tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91cec306-e991-42dc-89f8-c27a57a2c446",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "be03dc38-04f0-43ad-a9a0-c0755dc0927e",
  "sourceToolAssistantUUID": "91cec306-e991-42dc-89f8-c27a57a2c446",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T23:38:48.767Z_

<details><summary>↩ Tool result · `toolu_01NiacRbujvsMX17RcSe2GJ1`</summary>

```text
Web search results for query: "routing retrieval configuration code LLM 2025 2026"

Links: [{"title":"GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub","url":"https://github.com/ulab-uiuc/LLMRouter"},{"title":"Router - Load Balancing | liteLLM","url":"https://docs.litellm.ai/docs/routing"},{"title":"Route Before Retrieve: Activating Latent Routing Abilities of LLMs for RAG vs. Long Context Selection | OpenReview","url":"https://openreview.net/forum?id=N1E7rFZJGH"},{"title":"GitHub - lm-sys/RouteLLM: A framework for serving and evaluating LLM routers - save LLM costs without compromising quality · GitHub","url":"https://github.com/lm-sys/RouteLLM"},{"title":"MeshAgent: Enabling Reliable Network Management with Large Language Models","url":"https://zaoxing.github.io/papers/2026/SIGMETRICS26_MeshAgent.pdf"},{"title":"MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents","url":"https://arxiv.org/html/2605.00356v1"},{"title":"Routing & Load Balancing | liteLLM","url":"https://docs.litellm.ai/docs/routing-load-balancing"},{"title":"GitHub - NVIDIA-AI-Blueprints/llm-router: Route LLM requests to the best model for the task at hand. · GitHub","url":"https://github.com/NVIDIA-AI-Blueprints/llm-router"},{"title":"Open-Source LLM Router for Mixture-of-Models | vLLM Semantic Router","url":"https://vllm-semantic-router.com/"},{"title":"OpenRouter","url":"https://openrouter.ai/"}]

I found several relevant results related to routing, retrieval, and LLM configuration. Here's what the search revealed:

## Key Findings:

**Recent LLM Routing Frameworks (2025-2026):**

LLMRouter was officially released in December 2025 as an open-source library enabling cost-aware LLM routing with 16+ routers, a unified CLI, and a plugin workflow for custom routers. In May 2026, RouteProfile Code and Paper were released as a general framework for designing LLM profiles for routing.

**Retrieval-Augmented Routing:**

Pre-Route is a lightweight framework submitted to ICLR 2026 that proactively chooses between retrieval-augmented generation and long-context using metadata before retrieval, delivering interpretable routing, higher performance, and lower cost.

**Configuration & Implementation Options:**

- Router provides multiple strategies for routing calls across multiple deployments, with simple-shuffle recommended for best production performance
- Router configuration is specified either in a config argument for Controller or by passing in a YAML file using the --config flag

**Advanced Router Architectures:**

Conversational memory and retrieval-grounded routing let a lightweight 8B model recover most of a 235B model's performance on persistent user-specific queries while cutting effective inference cost by 96%.

These developments represent significant advances in intelligent LLM routing and retrieval configuration for 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "382a6e97-1e77-4e59-bec5-5320c45f3472",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "45c01dd7-7a1c-431b-a395-63c6a027a2c9",
  "sourceToolAssistantUUID": "382a6e97-1e77-4e59-bec5-5320c45f3472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T23:38:48.943Z_

<details><summary>↩ Tool result · `toolu_01Bg3rmehgciBkvrhPmR9KQd`</summary>

```text
Web search results for query: "adaptive retrieval strategy selection code repair 2025 2026"

Links: [{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"A Survey of LLM-based Automated Program Repair","url":"https://arxiv.org/pdf/2506.23749"},{"title":"Adaptive RAG explained: What to know in 2026","url":"https://www.meilisearch.com/blog/adaptive-rag"},{"title":"RESCUE: Retrieval Augmented Secure Code Generation","url":"https://www.researchgate.net/publication/396747221_RESCUE_Retrieval_Augmented_Secure_Code_Generation"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium","url":"https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"[2503.06510] Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/abs/2503.06510"},{"title":"Multi-Field Adaptive Retrieval | OpenReview","url":"https://openreview.net/forum?id=3PDklqqqfN"}]

Based on the web search results, I found several relevant works on adaptive retrieval strategies and code repair from 2025-2026:

## Key Research Findings

### Adaptive Retrieval in Code Repair

ProCC adopts an adaptive retrieval selection algorithm to incorporate code similarity into the decision-making process to determine the most suitable retrieval perspective for code completion. This approach uses a prompt-based multi-retriever system with adaptive selection mechanisms.

### LLM-Based Automated Program Repair

Recent LLM-based APR systems published from January 2022 to June 2025 fall into four paradigms, with retrieval- or analysis-augmented contexts strengthening them. Fine-tuning delivers strong task alignment at high training cost; prompting enables rapid deployment but is limited by prompt design and context windows; procedural pipelines offer reproducible control with moderate overhead; agentic frameworks tackle multi-hunk or cross-file bugs at the price of increased latency and complexity.

### Adaptive RAG Strategies

Adaptive RAG improves retrieval accuracy by dynamically adjusting to user intent, query type, and context, and decides when and how to retrieve results based on question complexity. Unlike standard RAG which blindly retrieves documents for every query, adaptive RAG skips retrieval for simple prompts, performs web search for fresh information, or retrieves external knowledge from multiple sources when needed.

### Recent Papers (2025-2026)

Recent works include "Less is More: Adaptive Program Repair with Bug Localization and Preference Learning [2025-AAAI]" and "APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching [2025-USENIX Security]".

The search results indicate active research in combining adaptive retrieval strategies with code repair, particularly focusing on efficient context selection and LLM-based patch generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc6b9928-37fc-4a5b-80dd-2c6620ed5be0",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "ccf6fc5b-85dd-45e2-8560-f7d804914f45",
  "sourceToolAssistantUUID": "bc6b9928-37fc-4a5b-80dd-2c6620ed5be0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-11T23:38:56.972Z_

Now let me run the remaining searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccf6fc5b-85dd-45e2-8560-f7d804914f45",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfQQvDNnfEzwGwvQTBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c72e473f-ab95-4d8a-a9db-cffe9395d91c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJTQcBsHvewxRwgCZzh2Vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-11T23:38:58.276Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AxDKWfY68sByEREzv9KyTt`</summary>

```json
{
  "query": "systematic comparison routing methods LLM ablation-as-paper contribution 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c72e473f-ab95-4d8a-a9db-cffe9395d91c",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfQQvDNnfEzwGwvQTBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88d3499b-3d99-4cf6-bc0b-571687541b2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJTQcBsHvewxRwgCZzh2Vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-11T23:38:58.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CrA1VYZxPhJWdGupQyHuQ2`</summary>

```json
{
  "query": "Bradley-Terry preference learning routing selection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d3499b-3d99-4cf6-bc0b-571687541b2d",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfQQvDNnfEzwGwvQTBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe6c17a5-0a84-46b4-ba9b-bad0f9607e5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJTQcBsHvewxRwgCZzh2Vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-11T23:38:59.257Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013frmnqFhmf3kvwe29rhwFf`</summary>

```json
{
  "query": "EMNLP 2025 accepted papers code generation code repair retrieval augmented"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe6c17a5-0a84-46b4-ba9b-bad0f9607e5b",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfQQvDNnfEzwGwvQTBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdfa5e72-475d-4c64-beb4-699272e6cf4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJTQcBsHvewxRwgCZzh2Vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-11T23:38:59.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rx6WQESgkzwmY1UEX5Ri1M`</summary>

```json
{
  "query": "Mix-of-Granularity router retrieval granularity selection learned 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdfa5e72-475d-4c64-beb4-699272e6cf4c",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfQQvDNnfEzwGwvQTBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af70401c-5e9e-487c-bd4a-63a0b22f3592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJTQcBsHvewxRwgCZzh2Vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 10633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3012,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-11T23:39:00.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BE2ur1wAuNDmo9yv5Evjkr`</summary>

```json
{
  "query": "RouteLLM Bradley-Terry preference model routing 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af70401c-5e9e-487c-bd4a-63a0b22f3592",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfQQvDNnfEzwGwvQTBi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58803d0c-fb14-4d03-96a1-22fc82ef2c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJTQcBsHvewxRwgCZzh2Vm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2680,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 10633,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2680,
          "output_tokens": 287,
          "cache_read_input_tokens": 10633,
          "cache_creation_input_tokens": 3012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3012,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T23:39:06.295Z_

<details><summary>↩ Tool result · `toolu_01CrA1VYZxPhJWdGupQyHuQ2`</summary>

```text
Web search results for query: "Bradley-Terry preference learning routing selection 2025 2026"

Links: [{"title":"GitHub - holarissun/RewardModelingBeyondBradleyTerry: official implementation of ICLR'2025 paper: Rethinking Bradley-Terry Models in Preference-based Reward Modeling: Foundations, Theory, and Alternatives","url":"https://github.com/holarissun/RewardModelingBeyondBradleyTerry"},{"title":"Prompt-to-Leaderboard Evan Frick∗, Connor Chen∗, Joseph Tennyson∗, Tianle Li∗,","url":"https://arxiv.org/pdf/2502.14855"},{"title":"Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment | OpenReview","url":"https://openreview.net/forum?id=UgKcpPE0ZX"},{"title":"Learning From Pairwise Preferences: An Introduction to the Bradley Terry Model | by Sean Moran | Data Science Collective | Apr, 2026 | Medium","url":"https://medium.com/data-science-collective/learning-from-pairwise-preferences-an-introduction-to-the-bradley-terry-model-71020f05654c"},{"title":"[2510.15242] Bradley-Terry Policy Optimization for Generative Preference Modeling","url":"https://arxiv.org/abs/2510.15242"},{"title":"Recent advances in the Bradley–Terry Model: theory, algorithms, and applications","url":"https://arxiv.org/html/2601.14727v1"},{"title":"Estimation of partial rankings from sparse, noisy comparisons | Communications Physics","url":"https://www.nature.com/articles/s42005-025-02461-y"},{"title":"Rethinking Reward Modeling in Preference-based Large Language Model Alignment | OpenReview","url":"https://openreview.net/forum?id=rfdblE10qm"},{"title":"Bradley–Terry Policy Optimization for Generative Preference Modeling","url":"https://arxiv.org/html/2510.15242"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf/c86736447d5c66dec8140360ab743a130d9ff219.pdf"}]

Based on the search results, here are the key findings related to Bradley-Terry preference learning and routing selection in 2025-2026:

## Recent Advances in Bradley-Terry and Routing Selection

**Prompt-to-Leaderboard (P2L) Routing System:**
In January 2025, a router trained based on Bradley-Terry methodology achieved the #1 spot on the Chatbot Arena leaderboard. This system uses Bradley-Terry coefficients which are then used to predict human preference votes, resulting in prompt-dependent leaderboards that allow for optimal routing of queries to models.

**Beyond Bradley-Terry Models:**
Traditional Bradley-Terry reward models fall short in expressiveness, particularly in addressing intransitive preferences, prompting research into preference embedding approaches that capture intricate preference structures efficiently. A General Preference Model (GPM) has been shown to consistently outperform the BT reward model on the RewardBench benchmark and effectively model cyclic preferences where any BT reward model behaves like a random guess.

**Bradley-Terry Policy Optimization:**
Recent work shows that introducing chain-of-thought reasoning into preference modeling fundamentally changes the Bradley-Terry likelihood structure, resulting in a preference likelihood that cannot be optimized using standard RL objectives.

**Theoretical Foundations:**
The Bradley-Terry model is widely used in reward modeling for LLM alignment, with recent work establishing convergence rates of BT reward models based on deep neural networks.

These developments represent significant progress in understanding and extending Bradley-Terry models for modern applications in LLM evaluation and routing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe6c17a5-0a84-46b4-ba9b-bad0f9607e5b",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "9e6fd55a-dad4-422c-abb1-d2ce1c8bd4e9",
  "sourceToolAssistantUUID": "fe6c17a5-0a84-46b4-ba9b-bad0f9607e5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:39:06.340Z_

<details><summary>↩ Tool result · `toolu_013frmnqFhmf3kvwe29rhwFf`</summary>

```text
Web search results for query: "EMNLP 2025 accepted papers code generation code repair retrieval augmented"

Links: [{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"EMNLP.2025 - Findings | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025?group=Findings"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Eighteen papers by CSE researchers at EMNLP 2025","url":"https://cse.engin.umich.edu/stories/eighteen-papers-by-cse-researchers-at-emnlp-2025"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"[EMNLP 2025] Call for Main Conference Papers","url":"https://groups.google.com/g/ml-news/c/HKZ_H_iiM_A"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"EMNLP 2025 - NAVER LABS Europe","url":"https://europe.naverlabs.com/updates/emnlp/"},{"title":"EMNLP 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/emnlp-statistics/emnlp-2025-statistics/"}]

I found relevant results for your search query. Here are the key findings about EMNLP 2025 accepted papers related to code generation, code repair, and retrieval-augmented approaches:

## Code Repair with Retrieval-Augmented Approaches

One notable accepted paper in the Industry Track is "Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair" by Bojian Xiong, Yikun Lei, Xikai Liu, Shaowei Zhang, Pengyun Zhu, Yan Liu, Yong and others.

## General Conference Statistics

EMNLP-2025 accepts more than 2,000 papers, and relevant topics for the conference include Code Models and Retrieval-Augmented Language Models.

## Research on Retrieval-Augmented Code Generation

According to recent research surveying the field, EMNLP had 5 papers (4.5%) among peer-reviewed venues studying retrieval-augmented code generation approaches, though the search notes that full papers from EMNLP 2025 were not yet publicly available at the time of that survey's search.

The conference appears to have a strong focus on both code models and retrieval-augmented generation techniques, making it a significant venue for this research area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdfa5e72-475d-4c64-beb4-699272e6cf4c",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "302f2df8-6312-4540-81fd-b3694e996691",
  "sourceToolAssistantUUID": "cdfa5e72-475d-4c64-beb4-699272e6cf4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-11T23:39:06.936Z_

<details><summary>↩ Tool result · `toolu_01AxDKWfY68sByEREzv9KyTt`</summary>

```text
Web search results for query: "systematic comparison routing methods LLM ablation-as-paper contribution 2025 2026"

Links: [{"title":"Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey","url":"https://arxiv.org/html/2603.04445v1"},{"title":"Unsolvability Ceiling in Multi-LLM Routing: An Empirical Study of Evaluation Artifacts","url":"https://arxiv.org/html/2605.07395"},{"title":"LLMRouterBench: LLM Routing Benchmark","url":"https://www.emergentmind.com/topics/llmrouterbench"},{"title":"[2603.04445] Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey","url":"https://arxiv.org/abs/2603.04445"},{"title":"Rethinking Predictive LLM Routing: When Simple KNN Beats Complex Learned Routers | OpenReview","url":"https://openreview.net/forum?id=Chn50flK4X"},{"title":"A Unified Approach to Routing and Cascading for LLMs | OpenReview","url":"https://openreview.net/forum?id=AAl89VNNy1"},{"title":"Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey [Quick Review]","url":"https://liner.com/review/dynamic-model-routing-and-cascading-for-efficient-llm-inference-survey"},{"title":"A Comprehensive Benchmark for Routing LLMs to Explore ...","url":"https://aclanthology.org/2025.findings-emnlp.208.pdf"},{"title":"Towards Efficient Multi-LLM Inference: Characterization and Analysis of LLM Routing and Hierarchical Techniques","url":"https://arxiv.org/html/2506.06579v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf"}]

I found relevant research on systematic comparison of LLM routing methods from 2025-2026. Here are the key findings:

## Major Benchmarking Initiatives

RouterEval (Huang et al., 2025) is a large-scale open-source benchmark for systematic evaluation of LLM routing methods, comprising over 200 million performance records from more than 8,500 LLMs across 12 widely used benchmarks.

LLMRouterBench integrates a suite of 10 routing methods, encompassing both classical and recent architectures, and has become the standard backbone for empirical router comparison, reproducible ablation studies, and scalable integration of new LLMs and tasks.

## Systematic Comparison Approaches

Research shows that a well-tuned k-Nearest Neighbors (kNN) approach matches or outperforms state-of-the-art learned routers while being significantly more efficient, with standardized routing benchmarks spanning instruction-following, question-answering, and reasoning tasks.

The MMR-Bench benchmark includes strong single-model baselines, oracle upper bounds, and representative routing policies, enabling systematic comparison of routing strategies under fixed candidate sets and cost models.

## Ablation Studies

Methodologies for comparison include fixed-split evaluation with shared train/test splits for all routers, controlled embedding backbones, and baseline comparison against upper/lower bounds, while cross-validation and ablation studies including embedding backbone swaps are supported.

Theoretical analysis reveals that the strong locality properties of model performance in embedding space enable simple non-parametric methods to achieve superior routing decisions with lower sample complexity than parametric approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88d3499b-3d99-4cf6-bc0b-571687541b2d",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "e27863ac-8ed1-4e9b-b2d3-0a7d268aecdf",
  "sourceToolAssistantUUID": "88d3499b-3d99-4cf6-bc0b-571687541b2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-11T23:39:07.510Z_

<details><summary>↩ Tool result · `toolu_01Rx6WQESgkzwmY1UEX5Ri1M`</summary>

```text
Web search results for query: "Mix-of-Granularity router retrieval granularity selection learned 2024 2025"

Links: [{"title":"[2406.00456] Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2406.00456"},{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.00456v2"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.384/"},{"title":"GraphRAG-Router: Learning Cost-Efficient Routing over GraphRAGs and LLMs with Reinforcement Learning","url":"https://arxiv.org/html/2604.16401v1"},{"title":"Computation and Language Jun 2024","url":"https://web3.arxiv.org/list/cs.CL/2024-06?skip=1785&show=2000"},{"title":"GitHub - ZGChung/Mix-of-Granularity: [COLING 2025] Mix-of-Granularity paper","url":"https://github.com/ZGChung/Mix-of-Granularity"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"1 ExpertRAG: Efficient RAG with Mixture of Experts – Optimizing","url":"https://arxiv.org/pdf/2504.08744"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=200&show=100"}]

Based on the web search results, I found relevant information about Mix-of-Granularity (MoG):

## Mix-of-Granularity: Overview

Mix-of-Granularity (MoG) is a method that dynamically determines the optimal granularity of a knowledge source based on input queries using a router. The paper "Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation" was published in the Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025) in Abu Dhabi, UAE.

## Key Features

The router is efficiently trained with a newly proposed loss function employing soft labels. The method further extends MoG to MoG-Graph (MoGG), where reference documents are pre-processed as graphs, enabling the retrieval of distantly situated snippets.

## Problem Being Addressed

Integrating information from various reference databases is a major challenge for Retrieval-Augmented Generation (RAG) systems because each knowledge source adopts a unique data structure and follows different conventions, and retrieving from multiple knowledge sources with one fixed strategy usually leads to under-exploitation of information.

## Results

Experiments demonstrate that MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks.

The paper is authored by Zijie Zhong, Hanwen Liu, Xiaoya Cui, Xiaofan Zhang, and Zengchang Qin, with code publicly available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af70401c-5e9e-487c-bd4a-63a0b22f3592",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "832ab8b9-1c6d-41eb-93d4-152c61051ed1",
  "sourceToolAssistantUUID": "af70401c-5e9e-487c-bd4a-63a0b22f3592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-11T23:39:08.196Z_

<details><summary>↩ Tool result · `toolu_01BE2ur1wAuNDmo9yv5Evjkr`</summary>

```text
Web search results for query: "RouteLLM Bradley-Terry preference model routing 2024 2025"

Links: [{"title":"RouteLLM: Learning to Route LLMs from Preference Data | OpenReview","url":"https://openreview.net/forum?id=8sSqNntaMr"},{"title":"[2406.18665] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/pdf/2406.18665"},{"title":"RouteLLM: An Open-Source Framework for Cost-Effective LLM Routing - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2024-07-01-routellm/"},{"title":"Bradley–Terry model - Wikipedia","url":"https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model"},{"title":"Prompt-to-Leaderboard Evan Frick∗, Connor Chen∗, Joseph Tennyson∗, Tianle Li∗,","url":"https://arxiv.org/pdf/2502.14855"},{"title":"Rethinking Bradley-Terry Models in Preference-Based Reward Modeling: Foundations, Theory, and Alternatives","url":"https://arxiv.org/html/2411.04991v1"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data | Request PDF","url":"https://www.researchgate.net/publication/381770651_RouteLLM_Learning_to_Route_LLMs_with_Preference_Data"},{"title":"GitHub - general-preference/general-preference-model: [ICML 2025] Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment (https://arxiv.org/abs/2410.02197) · GitHub","url":"https://github.com/general-preference/general-preference-model"},{"title":"GitHub - holarissun/RewardModelingBeyondBradleyTerry: official implementation of ICLR'2025 paper: Rethinking Bradley-Terry Models in Preference-based Reward Modeling: Foundations, Theory, and Alternatives","url":"https://github.com/holarissun/RewardModelingBeyondBradleyTerry"}]

Based on the search results, here's what I found about RouteLLM and the Bradley-Terry preference model routing in 2024-2025:

## RouteLLM Framework

RouteLLM is a principled framework for LLM routing based on preference data. It proposes efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality.

The framework achieves significant cost reductions on popular benchmarks, including over 85% cost reduction on MT Bench, 45% on MMLU, and 35% on GSM8K compared to using only GPT-4, while still achieving 95% of GPT-4's performance.

## Training Methodology

The framework leverages human preference data and data augmentation techniques to enhance performance. Four different routers were trained using public data from Chatbot Arena.

## Recent Extensions with Bradley-Terry Models

Recent 2025 work has extended this approach with Bradley-Terry modeling. One approach uses Bradley-Terry coefficients which are used to predict human preference votes, allowing for unsupervised task-specific evaluation, optimal routing of queries to models, personalization, and automated evaluation of model strengths and weaknesses. A router trained based on this methodology achieved the #1 spot on the Chatbot Arena leaderboard in January 2025.

Additionally, research accepted to ICML 2025 titled "Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment" explores alternatives to traditional Bradley-Terry approaches for language model alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58803d0c-fb14-4d03-96a1-22fc82ef2c26",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "bbe29fe5-0eb0-4380-a5ba-dfd15d014ed9",
  "sourceToolAssistantUUID": "58803d0c-fb14-4d03-96a1-22fc82ef2c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-11T23:39:11.203Z_

Let me do a few more targeted searches to fill in gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbe29fe5-0eb0-4380-a5ba-dfd15d014ed9",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfRqLBEkFnv3kA1zEqN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a0c3fc4-da6e-4cf9-8c9e-ab6b307e09e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaUdZo2YZVPvpPzRyG65yx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7678,
      "cache_read_input_tokens": 13645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7678,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-11T23:39:11.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0143pJdCWdGuWUWp4zFU1jKN`</summary>

```json
{
  "query": "\"GranRoute\" retrieval routing code repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a0c3fc4-da6e-4cf9-8c9e-ab6b307e09e4",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfRqLBEkFnv3kA1zEqN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68f9f4a4-8d3b-4849-b307-1a3c13b65419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaUdZo2YZVPvpPzRyG65yx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7678,
      "cache_read_input_tokens": 13645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7678,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-11T23:39:12.495Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Jc3J4AXpe25W8eFDCo4rP`</summary>

```json
{
  "query": "EMNLP 2024 2025 accepted papers program repair bug fix code NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68f9f4a4-8d3b-4849-b307-1a3c13b65419",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfRqLBEkFnv3kA1zEqN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e5f4cf8-c514-4c7f-8bdf-1209bbe53fec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaUdZo2YZVPvpPzRyG65yx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7678,
      "cache_read_input_tokens": 13645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7678,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-11T23:39:13.100Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017D56ZxQng5VFYxBVySbooo`</summary>

```json
{
  "query": "ProCC adaptive retrieval selection code completion multi-retriever 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e5f4cf8-c514-4c7f-8bdf-1209bbe53fec",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfRqLBEkFnv3kA1zEqN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df318555-6bb2-48b2-9a71-1ec726d3ed77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaUdZo2YZVPvpPzRyG65yx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7678,
      "cache_read_input_tokens": 13645,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7678
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 13645,
          "cache_creation_input_tokens": 7678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7678,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T23:39:16.400Z_

<details><summary>↩ Tool result · `toolu_0143pJdCWdGuWUWp4zFU1jKN`</summary>

```text
Web search results for query: ""GranRoute" retrieval routing code repair"

Links: [{"title":"Global Routing Codes - Goldman Sachs Developer","url":"https://developer.gs.com/docs/services/transaction-banking/routing-codes/"},{"title":"GitHub - raphaelchristi/harness-evolver: Automated harness evolution for AI agents. A Claude Code plugin that iteratively optimizes system prompts, routing, retrieval, and orchestration code using full-trace counterfactual diagnosis. Based on Meta-Harness (Lee et al., 2026). · GitHub","url":"https://github.com/raphaelchristi/harness-evolver"},{"title":"ITA Software Advanced Routing Codes","url":"https://forums.dansdeals.com/index.php?topic=17085.340"},{"title":"Query Routing for Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2505.23052"},{"title":"Routing | React Router","url":"https://reactrouter.com/start/framework/routing"},{"title":"Routing Number Confusion: CA or VA? | Bank of America FAQ","url":"https://www.justanswer.com/finance/rxkjf-porque-el-numero-de-ruta-no-122000661-que-pedi-para.html"},{"title":"Build Smarter RAG with Routing and Hybrid Retrieval - Milvus Blog","url":"https://milvus.io/blog/build-smarter-rag-routing-hybrid-retrieval.md"},{"title":"RepoMasterEval: Evaluating Code Completion via Real-World Repositories","url":"https://chao-peng.github.io/publication/ase25industry/ase25industry.pdf"},{"title":"Training-Free LLM Routing for Knowledge Graph Retrieval ...","url":"https://aclanthology.org/2025.findings-emnlp.606.pdf"},{"title":"RouteThis | WiFi installation, troubleshooting and support software for Service Providers, IoT and Smart Home","url":"https://www.routethis.com/"}]

Based on the search results, I didn't find specific information about "GranRoute" as a retrieval routing code repair system. The search results returned information about:

1. Banking routing codes and payment systems
2. RAG (Retrieval-Augmented Generation) routing techniques for LLMs
3. ITA Software's routing codes for flight searches
4. React Router framework configuration
5. General retrieval routing systems for AI/ML applications

It's possible that "GranRoute" is a specialized or niche tool/system that may not have widespread web presence, could be an internal system, or might be known by a different name. 

Could you provide more context about what "GranRoute" refers to? For example:
- Is it a software tool, framework, or system?
- What domain does it operate in (finance, logistics, AI/ML, etc.)?
- Are there any organizations or projects associated with it?

This would help me conduct a more targeted search to find the information you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68f9f4a4-8d3b-4849-b307-1a3c13b65419",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "bdf19bcf-5977-4e59-bcd9-d4936b884f52",
  "sourceToolAssistantUUID": "68f9f4a4-8d3b-4849-b307-1a3c13b65419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T23:39:17.873Z_

<details><summary>↩ Tool result · `toolu_014Jc3J4AXpe25W8eFDCo4rP`</summary>

```text
Web search results for query: "EMNLP 2024 2025 accepted papers program repair bug fix code NLP"

Links: [{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"EMNLP 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2024-paper-list/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"15 Papers Accepted to EMNLP 2024 | Department of Computer Science, Columbia University","url":"https://www.cs.columbia.edu/2024/15-papers-accepted-to-emnlp-2024/"},{"title":"Customizable NLP @ EMNLP 2024","url":"https://customnlp4u-24.github.io/"}]

Based on the search results, I found relevant information about NLP papers related to program repair and code:

A paper titled "Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair" by Bojian Xiong and colleagues is listed among the accepted industry track papers for EMNLP 2025.

Additionally, EMNLP 2025 accepted more than 2,000 papers, indicating there is a substantial body of work presented at this conference. To find more papers specifically on program repair, bug fixing, and code-related NLP topics, you could:

1. Visit the official EMNLP 2025 website at https://2025.emnlp.org/ to browse the full accepted papers list
2. Use paper search platforms like Paper Copilot or Paper Digest, which have dedicated EMNLP 2024 and 2025 paper lists that allow searching by topic
3. Search by specific keywords like "program repair," "bug fix," or "code generation" on these platforms

The search results show that code-related NLP work is represented at these conferences, but a more targeted search on the conference's official program would help you identify all papers in this specific area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e5f4cf8-c514-4c7f-8bdf-1209bbe53fec",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "12aa7ca3-c766-4799-be9a-aec680252ca3",
  "sourceToolAssistantUUID": "0e5f4cf8-c514-4c7f-8bdf-1209bbe53fec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-11T23:39:21.456Z_

<details><summary>↩ Tool result · `toolu_017D56ZxQng5VFYxBVySbooo`</summary>

```text
Web search results for query: "ProCC adaptive retrieval selection code completion multi-retriever 2025"

Links: [{"title":"[2405.07530] Prompt-based Code Completion via Multi-Retrieval Augmented Generation","url":"https://arxiv.org/abs/2405.07530"},{"title":"Prompt-based Code Completion via Multi-Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2405.07530"},{"title":"Prompt-Based Code Completion via Multi-Retrieval Augmented Generation | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/full/10.1145/3725812"},{"title":"GitHub - anonepo/procc","url":"https://github.com/anonepo/procc/"},{"title":"[Literature Review] Prompt-based Code Completion via Multi-Retrieval Augmented Generation","url":"https://www.themoonlight.io/en/review/prompt-based-code-completion-via-multi-retrieval-augmented-generation"},{"title":"[PDF] Prompt-based Code Completion via Multi-Retrieval Augmented Generation | CiteDrive","url":"https://www.citedrive.com/en/discovery/prompt-based-code-completion-via-multi-retrieval-augmented-generation/"},{"title":"[2405.07530v1] Prompt-based Code Completion via Multi-Retrieval Augmented Generation","url":"https://arxiv.org/abs/2405.07530v1"},{"title":"Prompt-based Code Completion via Multi-Retrieval Augmented Generation - R Discovery","url":"https://discovery.researcher.life/article/prompt-based-code-completion-via-multi-retrieval-augmented-generation/803a45c79722384fbea23a0b76b22c16"},{"title":"Prompt-based Code Completion via Multi-Retrieval Augmented Generation | Request PDF","url":"https://www.researchgate.net/publication/390223954_Prompt-based_Code_Completion_via_Multi-Retrieval_Augmented_Generation"},{"title":"CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion","url":"https://www.researchgate.net/publication/395709304_CodeRAG_Finding_Relevant_and_Necessary_Knowledge_for_Retrieval-Augmented_Repository-Level_Code_Completion"}]

Based on the search results, here's information about ProCC and its approach to code completion:

## ProCC: Prompt-based Code Completion via Multi-Retrieval Augmented Generation

ProCC is a code completion framework leveraging prompt engineering and the contextual multi-armed bandits algorithm to flexibly incorporate and adapt to multiple perspectives of code.

### Key Components

The framework consists of two main parts:

1. **Prompt-based Multi-Retriever System**: ProCC employs a prompt-based multi-retriever system which crafts prompt templates to elicit LLM knowledge to understand code semantics with multiple retrieval perspectives.

2. **Adaptive Retrieval Selection Algorithm**: It adopts the adaptive retrieval selection algorithm to incorporate code similarity into the decision-making process to determine the most suitable retrieval perspective for the LLM to complete the code.

### How It Works

The adaptive retrieval selection algorithm is based on a contextual multi-armed bandit algorithm where the different retrieval perspectives are seen as the "arms" of the bandit and the goal is to identify which arm (i.e., perspective) yields the highest reward or performance for individual incomplete code, conditioned on the similarity between retrieved snippets and incomplete code.

### Performance Results

ProCC outperforms the widely-studied code completion technique RepoCoder by 7.92% on the public benchmark CCEval, 3.19% in HumanEval-Infilling, 2.80% on the collected open-source benchmark suite, and 4.48% on the private-domain benchmark suite collected from Kuaishou Technology in terms of Exact Match.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df318555-6bb2-48b2-9a71-1ec726d3ed77",
  "isSidechain": true,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "agentId": "a30cab4ee1ca19082",
  "type": "user",
  "uuid": "8bb36e27-2b00-486b-9b0a-26925f465fcc",
  "sourceToolAssistantUUID": "df318555-6bb2-48b2-9a71-1ec726d3ed77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-11T23:40:22.771Z_

Here are my consolidated findings across all six questions:

---

## 1. EMNLP 2026 ARR Deadline

**Confirmed: May 25, 2026 is correct.** The EMNLP 2026 CFP and official Twitter account both state the ARR submission deadline is May 25, 2026. One important wrinkle: since EMNLP 2026 and AACL share the ARR May cycle, authors must explicitly declare their target conference at submission time, and the choice is binding. Post-submission timeline: author response July 7-13, meta-review July 30, commitment deadline August 2, notification August 20.

Sources:
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Dates](http://aclrollingreview.org/dates)
- [EMNLP 2026 Twitter announcement](https://x.com/emnlpmeeting/status/2029508292637061462)

---

## 2. Short Paper Page Limit

**Confirmed: 4 pages is correct.** EMNLP 2026 follows the standard ARR format: 8 pages for long papers, 4 pages for short papers (excluding references/appendices).

Sources:
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR CFP](http://aclrollingreview.org/cfp)

---

## 3. Novelty Check -- Routing for Retrieval in Code Tasks

**There is closely related prior work, but GranRoute appears to occupy a specific niche.** Key papers to be aware of:

- **ProCC (TOSEM 2025)**: Uses a contextual multi-armed bandit algorithm to adaptively select among multiple retrieval perspectives for code completion. This is the most directly comparable work -- it frames retrieval strategy selection as a bandit problem for code tasks. GranRoute needs to clearly differentiate from ProCC.

- **Mix-of-Granularity (MoG, COLING 2025)**: Learns a router to dynamically select the optimal retrieval granularity for RAG based on input queries. Not code-specific, but the mechanism (a trained router selecting granularity) is very close to what GranRoute describes.

- **Pre-Route (submitted to ICLR 2026)**: Routes between RAG vs. long-context using metadata, but is not code-specific and not about retrieval configuration.

- **RouteLLM (2024)**: Routes between strong/weak LLMs using preference data, including a Bradley-Terry-based router. Not retrieval configuration, but the training methodology overlaps.

- **"Less is More" (AAAI 2025)**: Adaptive program repair with preference learning, but focuses on bug localization rather than retrieval routing.

**Assessment**: The specific combination of (a) learning to route retrieval *configurations* (not just granularity or model choice) for (b) code repair tasks appears novel. However, ProCC's adaptive retrieval selection for code and MoG's learned granularity router are close enough that the paper must explicitly discuss them. If GranRoute does not cite and differentiate from ProCC and MoG, that is a significant gap.

Sources:
- [ProCC (arXiv/TOSEM)](https://arxiv.org/abs/2405.07530)
- [Mix-of-Granularity (COLING 2025)](https://aclanthology.org/2025.coling-main.384/)
- [Dense X Retrieval](https://arxiv.org/abs/2312.06648)
- [Less is More (AAAI 2025)](https://arxiv.org/abs/2503.06510)

---

## 4. Venue Fit

**EMNLP is a reasonable venue, but borderline.** Evidence:

- EMNLP 2025 accepted "Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair" in its **Industry Track** (note: industry, not main conference).
- EMNLP 2025 accepted "Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs."
- A retrieval-augmented code generation survey notes EMNLP had ~4.5% of peer-reviewed RACG papers, indicating modest but real representation.
- EMNLP 2025 Findings included "Training-Free LLM Routing for Knowledge Graph Retrieval" and "A Comprehensive Benchmark for Routing LLMs," showing routing work is accepted.

**Assessment**: Code repair + retrieval routing is at the intersection of SE and NLP. EMNLP accepts such work but tends to favor it more when the NLP contribution (e.g., novel training methodology, preference modeling, language understanding) is front and center rather than pure SE evaluation. If the paper's primary contribution is the routing methodology and training signal rather than the SE evaluation, EMNLP is a good fit. If it reads more like an SE systems paper, venues like ASE/ICSE/FSE would be stronger. As a reviewer, check whether the framing emphasizes the NLP/ML contributions.

Sources:
- [EMNLP 2025 Industry Track](https://2025.emnlp.org/program/ind_papers/)
- [EMNLP 2025 Findings - Routing for KG Retrieval](https://aclanthology.org/2025.findings-emnlp.606.pdf)
- [Routing LLMs Benchmark (EMNLP 2025 Findings)](https://aclanthology.org/2025.findings-emnlp.208.pdf)

---

## 5. Multi-Method Comparison as Contribution

**A 5-method comparison alone is thin; the field has moved toward systematic benchmarking.** Relevant context:

- **LLMRouterBench** already integrates 10+ routing methods with standardized evaluation, ablation support, and reproducible comparison.
- **RouterEval (2025)** provides 200M+ performance records across 8,500+ LLMs and 12 benchmarks for systematic router evaluation.
- A notable finding from "Rethinking Predictive LLM Routing" shows that a simple kNN baseline matches or beats complex learned routers, calling into question the value of elaborate method comparisons without novel insight.

**Assessment**: If GranRoute's contribution is primarily "we tried 5 training methods and report which works best," that is indeed closer to ablation-as-paper, especially given that RouterEval and LLMRouterBench already provide more comprehensive comparison frameworks. However, if the comparison yields a *novel finding* (e.g., Bradley-Terry outperforms alternatives specifically for retrieval configuration routing, or code tasks require different routing strategies than NL tasks), that transforms it from mere comparison to empirical contribution. Check whether the paper draws generalizable insights from the comparison or just reports numbers.

Sources:
- [LLMRouterBench](https://www.emergentmind.com/topics/llmrouterbench)
- [Rethinking Predictive LLM Routing (OpenReview)](https://openreview.net/forum?id=Chn50flK4X)
- [Dynamic Model Routing Survey](https://arxiv.org/abs/2603.04445)

---

## 6. Bradley-Terry for Routing Configuration Selection

**Yes, Bradley-Terry has been used for routing, but not specifically for retrieval configuration routing.**

- **RouteLLM (2024, ICLR 2025)**: Directly uses a Bradley-Terry-based router trained on preference data from Chatbot Arena to route between strong/weak LLMs. This is the most established use of BT for routing.
- **Prompt-to-Leaderboard (P2L, 2025)**: Extends BT to compute prompt-dependent leaderboards and route queries to optimal models. Their BT-based router hit #1 on Chatbot Arena.
- **Beyond Bradley-Terry (ICLR 2025, ICML 2025)**: Multiple papers critique BT's limitations (intransitive preferences, expressiveness) and propose alternatives like General Preference Models.

**Assessment**: Using BT for routing is well-established (RouteLLM is the canonical reference). The novelty would need to be in applying BT specifically to *retrieval configuration* selection rather than model selection -- that appears to be a new application domain. However, the paper should cite RouteLLM and acknowledge this lineage. If it presents BT for routing as novel without citing RouteLLM, that is a red flag.

Sources:
- [RouteLLM (arXiv)](https://arxiv.org/abs/2406.18665)
- [RouteLLM (ICLR 2025)](https://openreview.net/forum?id=8sSqNntaMr)
- [Prompt-to-Leaderboard](https://arxiv.org/pdf/2502.14855)
- [Rethinking BT in Reward Modeling (ICLR 2025)](https://github.com/holarissun/RewardModelingBeyondBradleyTerry)
- [General Preference Model (ICML 2025)](https://github.com/general-preference/general-preference-model)

---

## Summary for Your Review

| Question | Verdict |
|---|---|
| May 25 deadline | Confirmed correct |
| 4-page short paper | Confirmed correct |
| Novelty | Niche is defensible but must cite ProCC and MoG; differentiation needed |
| Venue fit | Acceptable if NLP/ML contribution is foregrounded; borderline if SE-heavy |
| 5-method comparison | Risky as sole contribution; needs novel insight, not just numbers |
| BT for routing | Well-established for model routing (RouteLLM); new for retrieval config routing if properly framed |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bb36e27-2b00-486b-9b0a-26925f465fcc",
  "isSidechain": true,
  "agentId": "a30cab4ee1ca19082",
  "requestId": "req_011CawfSqBXeZ2EKkr2v3bpX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4de535df-525c-48ab-99f0-2317bf60b320",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9XztzJnsrrDGm6C82Ya9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2627,
      "cache_read_input_tokens": 21323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2627,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---
