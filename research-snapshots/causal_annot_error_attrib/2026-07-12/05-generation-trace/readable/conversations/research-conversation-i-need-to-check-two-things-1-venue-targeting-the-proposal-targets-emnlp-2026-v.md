# Research conversation: I need to check two things: 1. **Venue targeting**: The proposal targets EMNLP 2026 via ARR May 2026 cycle (deadline 202

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad66df379f78ed269.jsonl`
- **Structured JSON:** [`f10ad6309128c7b0095f.json`](../../sessions/f1/f10ad6309128c7b0095f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-15T13:56:53.381Z_

I need to check two things:

1. **Venue targeting**: The proposal targets EMNLP 2026 via ARR May 2026 cycle (deadline 2026-05-25). But the revised idea now targets AAAI 2027 (expected Aug 2026), ICLR 2027 (expected Oct 2026), ACL 2027 (ARR Oct 2026). Search for:
   - "AAAI 2027 submission deadline"
   - "ICLR 2027 submission deadline" 
   - "ACL 2027 ARR deadline"
   - "EMNLP 2026 ARR submission deadline"
   Note: the user's requirement specifies EMNLP 2026 ARR deadline May 25, 2026. Check whether the revised targets make sense given the user asked specifically for EMNLP 2026.

2. **ICR Probe paper** (arXiv 2507.16488, ACL 2025) - "Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs" - This was found in competing work search. Use WebSearch and WebFetch to verify it exists and read its abstract. This paper tracks cross-layer evolution of hidden states during generation and may be highly relevant to SinkWatch.

3. Also search for: "attention sink dynamics temporal autoregressive generation hallucination 2026" to see if there's any very recent work (last 2-3 months) that directly does what SinkWatch proposes.

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "beb35661-917d-47d9-8079-ae453a74bee6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T13:56:53.384Z_

```json
{
  "parentUuid": "beb35661-917d-47d9-8079-ae453a74bee6",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
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
      "TodoWrite",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e0ad236c-689f-4e65-b10e-3a0aa25c513f",
  "timestamp": "2026-05-15T13:56:53.384Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T13:56:56.293Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0ad236c-689f-4e65-b10e-3a0aa25c513f",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGJLMZfgvq7BRWL5w2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc42ab8d-76c6-4ef7-a04e-85befb76ce22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVEEQJRnZmpGK2W4d4wnxh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 916,
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

_source line 4 · 2026-05-15T13:56:56.379Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Hu54TzBbHcJYE2YYXpHaAH`</summary>

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
  "parentUuid": "dc42ab8d-76c6-4ef7-a04e-85befb76ce22",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGJLMZfgvq7BRWL5w2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d8f3e8e-b42f-4c36-9894-82765d85c41d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KVEEQJRnZmpGK2W4d4wnxh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 916,
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

### Tool result

_source line 5 · 2026-05-15T13:56:56.383Z_

<details><summary>↩ Tool result · `toolu_01Hu54TzBbHcJYE2YYXpHaAH`</summary>

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
  "parentUuid": "5d8f3e8e-b42f-4c36-9894-82765d85c41d",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "6a9642f6-f7c3-4f62-972e-c9831b4d6da9",
  "sourceToolAssistantUUID": "5d8f3e8e-b42f-4c36-9894-82765d85c41d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T13:56:58.738Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a9642f6-f7c3-4f62-972e-c9831b4d6da9",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGXQAU8TwDqi1iFZ5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c3ccb5e-faf8-4741-915a-8ad67d6d58b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYjLZkprjrfazLCBAjsUHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-15T13:56:59.203Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TmhryFjRkcRncsf7XxzzvG`</summary>

```json
{
  "query": "AAAI 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c3ccb5e-faf8-4741-915a-8ad67d6d58b8",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGXQAU8TwDqi1iFZ5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d488c133-d563-4bd2-b9ec-259088c032e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYjLZkprjrfazLCBAjsUHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-15T13:56:59.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LxXuweMuT31PaAwQy9Fbxn`</summary>

```json
{
  "query": "ICLR 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d488c133-d563-4bd2-b9ec-259088c032e7",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGXQAU8TwDqi1iFZ5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ba344c5-40c4-4843-aac5-dda3c9f1c031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYjLZkprjrfazLCBAjsUHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-15T13:56:59.693Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YRJDCZc5ohc7zjvKxMz6Uo`</summary>

```json
{
  "query": "ACL 2027 ARR deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ba344c5-40c4-4843-aac5-dda3c9f1c031",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGXQAU8TwDqi1iFZ5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bbf4951-c4aa-46ba-aa92-bee90dbc525a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYjLZkprjrfazLCBAjsUHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-15T13:57:00.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019T28h5T7m2no87XWxmkjMP`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bbf4951-c4aa-46ba-aa92-bee90dbc525a",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGXQAU8TwDqi1iFZ5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fde2a549-b445-4972-8d46-83d55b06f1e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYjLZkprjrfazLCBAjsUHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 11 · 2026-05-15T13:57:00.646Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01At38mNa2RxXLzeZhTYZM8K`</summary>

```json
{
  "query": "arXiv 2507.16488 \"Tracking Hidden State Dynamics\" hallucination detection LLMs ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fde2a549-b445-4972-8d46-83d55b06f1e7",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGXQAU8TwDqi1iFZ5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02460834-f7a9-4d5c-888a-cf0d9bbb9189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYjLZkprjrfazLCBAjsUHD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 12 · 2026-05-15T13:57:00.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NV7gVicZez5PPFwzWqfM9U`</summary>

```json
{
  "query": "attention sink dynamics temporal autoregressive generation hallucination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02460834-f7a9-4d5c-888a-cf0d9bbb9189",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UGXQAU8TwDqi1iFZ5S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3923b8d-bc77-4989-b09e-583fc27a4308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYjLZkprjrfazLCBAjsUHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 9139,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 9139,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 13 · 2026-05-15T13:57:02.792Z_

<details><summary>↩ Tool result · `toolu_01TmhryFjRkcRncsf7XxzzvG`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"}]

Based on the search results, here's what I found regarding the AAAI 2027 submission deadline:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027. However, the AAAI 2027 paper submission deadline is TBD (to be determined).

According to the search results, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns. The official call for papers has not yet announced the specific submission deadline, so you may want to check the official AAAI 2027 website at https://aaai.org/conference/aaai/aaai-27/ for updates as they become available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d488c133-d563-4bd2-b9ec-259088c032e7",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "b3a2cd20-23ed-470c-b4dd-2bbb81b7a3d7",
  "sourceToolAssistantUUID": "d488c133-d563-4bd2-b9ec-259088c032e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:57:02.993Z_

<details><summary>↩ Tool result · `toolu_01LxXuweMuT31PaAwQy9Fbxn`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"International Conference on Learning Representations ICLR on February 08-09, 2027 in Lisbon, Portugal - Conference Index","url":"https://conferenceindex.org/event/international-conference-on-learning-representations-iclr-2027-february-lisbon-pt"},{"title":"Personal Conference Deadlines","url":"https://zhaohsu.top/conference-deadlines/"}]

Based on the search results, I found information about ICLR 2027. However, the search results show multiple ICLR 2027 conferences organized by different entities:

1. One ICLR conference is scheduled for August 30-31, 2027 in Sydney.

2. Another ICLR conference is scheduled for February 08-09, 2027 in Lisbon, Portugal, with a final submission deadline of September 30, 2027 (though this deadline appears to be after the conference date, which seems unusual).

The search results don't clearly show a specific submission deadline for the main official ICLR 2027 conference. The results mention that ICLR 2027 is expected in July 2027 with a deadline to be announced (TBA), predicted based on historical patterns.

For the most accurate and official submission deadline, I recommend checking the official ICLR website (iclr.cc) directly, as the 2027 details may not yet be fully published.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ba344c5-40c4-4843-aac5-dda3c9f1c031",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "53551b20-8a49-4280-8c8d-52d1e4add7bf",
  "sourceToolAssistantUUID": "5ba344c5-40c4-4843-aac5-dda3c9f1c031",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T13:57:03.593Z_

<details><summary>↩ Tool result · `toolu_019T28h5T7m2no87XWxmkjMP`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"The EMNLP call for System Demonstrations has now been posted! The submission deadline is July 4th, with additional details available here: https://t.co/BQvAw3vHxT\" / X","url":"https://x.com/emnlpmeeting/status/1915050634501660921"}]

The ARR submission deadline for EMNLP 2026 is May 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fde2a549-b445-4972-8d46-83d55b06f1e7",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "2046019d-c62a-411d-a6bf-724b5c153901",
  "sourceToolAssistantUUID": "fde2a549-b445-4972-8d46-83d55b06f1e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:57:03.655Z_

<details><summary>↩ Tool result · `toolu_01YRJDCZc5ohc7zjvKxMz6Uo`</summary>

```text
Web search results for query: "ACL 2027 ARR deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"},{"title":"ACL Resolutions - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Resolutions"}]

Based on the search results, the ARR submission deadline for ACL 2027 (long & short papers) is August 3, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Note that this deadline appears to be associated with EACL 2027, which is taking place in Athens, Greece in March 2027. The search results indicate this is an important deadline for that particular conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bbf4951-c4aa-46ba-aa92-bee90dbc525a",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "286feb67-be37-4310-8187-a4dc49faa81c",
  "sourceToolAssistantUUID": "7bbf4951-c4aa-46ba-aa92-bee90dbc525a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T13:57:06.730Z_

<details><summary>↩ Tool result · `toolu_01At38mNa2RxXLzeZhTYZM8K`</summary>

```text
Web search results for query: "arXiv 2507.16488 "Tracking Hidden State Dynamics" hallucination detection LLMs ACL 2025"

Links: [{"title":"[2507.16488] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/abs/2507.16488"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination","url":"https://arxiv.org/pdf/2507.16488"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/html/2507.16488"},{"title":"[2507.16488v1] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://arxiv.org/abs/2507.16488v1"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250716488Z/abstract"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs","url":"https://www.researchgate.net/publication/393923702_ICR_Probe_Tracking_Hidden_State_Dynamics_for_Reliable_Hallucination_Detection_in_LLMs"},{"title":"[PDF] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ICR-Probe:-Tracking-Hidden-State-Dynamics-for-in-Zhang-Hu/bb419a4952376815243456a7d44fa8c3eb78330f"},{"title":"ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.880/"},{"title":"[2603.16459] DynHD: Hallucination Detection for Diffusion Large Language Models via Denoising Dynamics Deviation Learning","url":"https://arxiv.org/abs/2603.16459"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"}]

Based on the search results, I found detailed information about arXiv paper 2507.16488:

## Paper Summary

The paper is titled "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs", authored by Zhenliang Zhang, Xinyu Hu, Huixuan Zhang, Junzhe Zhang, and Xiaojun Wan.

### Key Contribution

The paper introduces a novel metric called the ICR Score (Information Contribution to Residual Stream), which quantifies the contribution of modules to the hidden states' update. Existing hallucination detection methods leveraging hidden states predominantly focus on static and isolated representations, overlooking their dynamic evolution across layers, which the authors address with their approach.

### Proposed Method

The authors propose a hallucination detection method called the ICR Probe, which captures the cross-layer evolution of hidden states. Experimental results show that the ICR Probe achieves superior performance with significantly fewer parameters.

### Publication Status

The paper has been accepted to ACL 2025 (Main Conference), and it was submitted on July 22, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02460834-f7a9-4d5c-888a-cf0d9bbb9189",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "213bb521-8b36-4962-a917-1fe228a1ce42",
  "sourceToolAssistantUUID": "02460834-f7a9-4d5c-888a-cf0d9bbb9189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:57:09.253Z_

<details><summary>↩ Tool result · `toolu_01NV7gVicZez5PPFwzWqfM9U`</summary>

```text
Web search results for query: "attention sink dynamics temporal autoregressive generation hallucination 2026"

Links: [{"title":"[2604.15400] Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/abs/2604.15400"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400"},{"title":"LLM HALLUCINATION DETECTION:AFAST FOURIER ...","url":"https://openreview.net/pdf/a0eb273df4d7eb99b3e5f25f6455845460efe6a8.pdf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.10027"},{"title":"[2604.10697] Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/abs/2604.10697"},{"title":"Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2604.10697"},{"title":"VADE: Visual Attention Guided Hallucination Detection and ...","url":"https://aclanthology.org/2025.findings-acl.773.pdf"},{"title":"Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation","url":"https://arxiv.org/html/2604.10098"},{"title":"Rolling Sink","url":"https://rolling-sink.github.io/"},{"title":"[2604.10098] Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation","url":"https://arxiv.org/abs/2604.10098"}]

I found several highly relevant papers from 2026 addressing your search query. Here are the key findings:

## Recent Research on Attention Sinks and Hallucination Dynamics

### 1. **Hallucination as Trajectory Commitment**

Hallucination in autoregressive language models is governed by asymmetric attractor dynamics. This research presents causal evidence using a novel "same-prompt bifurcation" method that shows 44.3% of prompts bifurcate with factual and hallucinated trajectories diverging at the first generated token.

### 2. **Attention Sinks for Context Anchoring (SINKTRACK)**

Attention sink is the tendency to consistently allocate high attention to the very first token (⟨BOS⟩) of a sequence, and SINKTRACK treats ⟨BOS⟩ as an information anchor and injects key contextual features into its representation. SINKTRACK achieves +21.6% improvement on SQuAD2.0 with Llama3.1-8B-Instruct and +22.8% on M3CoT with Qwen2.5-VL-7B-Instruct.

### 3. **Attention Sinks as Hallucination Signals**

Hallucinations are deeply entangled with attention sinks - tokens that accumulate disproportionate attention mass during generation - indicating a transition from distributed, input-grounded attention to compressed, prior-dominated computation.

### 4. **Comprehensive Survey on Attention Sinks**

Attention sink involves a disproportionate amount of attention focused on a small subset of specific yet uninformative tokens, complicates interpretability, significantly affects training and inference dynamics, and exacerbates issues such as hallucinations.

### 5. **Temporal Dynamics in Video Generation**

Rolling Sink addresses the train-test gap in autoregressive video diffusion models, studying the gap between limited horizons during training and open-ended horizons during testing.

These studies represent a rapidly evolving field connecting attention mechanisms, temporal generation dynamics, and hallucination mitigation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3923b8d-bc77-4989-b09e-583fc27a4308",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "f681a6b5-2934-4474-8603-0792fec6ee13",
  "sourceToolAssistantUUID": "c3923b8d-bc77-4989-b09e-583fc27a4308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T13:57:12.672Z_

There are some very relevant papers found. Let me fetch more details on the most critical ones -- especially the ICR Probe paper and the two attention-sink hallucination papers from April 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f681a6b5-2934-4474-8603-0792fec6ee13",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UHU9jRBSjwLoHwLMu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bd82748-f28c-410c-85a2-8d90bbc2fe8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FApaeDSdbsi2mLBxjyWC1M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5030,
      "cache_read_input_tokens": 11052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5030,
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

_source line 20 · 2026-05-15T13:57:14.130Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XvK6N4MnV2CBZwDpEhjsKP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.16488",
  "prompt": "Extract the full abstract, authors, publication venue, and key method details of this paper. What exactly is the ICR Score and ICR Probe? How does it detect hallucinations using hidden state dynamics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bd82748-f28c-410c-85a2-8d90bbc2fe8c",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UHU9jRBSjwLoHwLMu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc5b08da-1895-4c13-b286-98bb9ef387d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FApaeDSdbsi2mLBxjyWC1M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5030,
      "cache_read_input_tokens": 11052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5030,
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

_source line 21 · 2026-05-15T13:57:15.500Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K5MENRyd911Vx5jvbG77hC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10697",
  "prompt": "Extract the full abstract, authors, publication venue/status, and key method details. How does this paper use attention sinks as signals for hallucination detection? What metrics does it track? How does it relate to temporal dynamics during autoregressive generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc5b08da-1895-4c13-b286-98bb9ef387d1",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UHU9jRBSjwLoHwLMu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8d213cd-e34c-4036-b09f-a96307f0a582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FApaeDSdbsi2mLBxjyWC1M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5030,
      "cache_read_input_tokens": 11052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5030,
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

_source line 22 · 2026-05-15T13:57:16.953Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Mt2nbtWusaFFvUZgpvHMp6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.15400",
  "prompt": "Extract the full abstract, authors, publication venue/status, and key method details. This paper is about hallucination as trajectory commitment with attractor dynamics. What exactly does it find about attention dynamics during hallucination generation? Does it involve attention sinks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8d213cd-e34c-4036-b09f-a96307f0a582",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UHU9jRBSjwLoHwLMu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "936b3572-13f8-4aa3-b000-1a14ee0ec26e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FApaeDSdbsi2mLBxjyWC1M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5030,
      "cache_read_input_tokens": 11052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5030,
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

_source line 23 · 2026-05-15T13:57:18.383Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KhshZvtiTZwpG2JatpbnZ3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10098",
  "prompt": "Extract the title, authors, abstract, and key findings of this survey on attention sinks. Does it discuss the relationship between attention sinks and hallucination? Does it discuss temporal dynamics of attention sinks during generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "936b3572-13f8-4aa3-b000-1a14ee0ec26e",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UHU9jRBSjwLoHwLMu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e66f2942-19e9-492a-8c91-0dda8b4d4dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FApaeDSdbsi2mLBxjyWC1M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5030,
      "cache_read_input_tokens": 11052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5030,
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

_source line 24 · 2026-05-15T13:57:19.980Z_

<details><summary>↩ Tool result · `toolu_01XvK6N4MnV2CBZwDpEhjsKP`</summary>

```text
# ICR Probe: Hallucination Detection in LLMs

## Full Abstract
"Large language models (LLMs) excel at various natural language processing tasks, but their tendency to generate hallucinations undermines their reliability. Existing hallucination detection methods leveraging hidden states predominantly focus on static and isolated representations, overlooking their dynamic evolution across layers, which limits efficacy. To address this limitation, we shift the focus to the hidden state update process and introduce a novel metric, the ICR Score (Information Contribution to Residual Stream), which quantifies the contribution of modules to the hidden states' update. We empirically validate that the ICR Score is effective and reliable in distinguishing hallucinations. Building on these insights, we propose a hallucination detection method, the ICR Probe, which captures the cross-layer evolution of hidden states. Experimental results show that the ICR Probe achieves superior performance with significantly fewer parameters. Furthermore, ablation studies and case analyses offer deeper insights into the underlying mechanism of this method, improving its interpretability."

## Authors
Zhenliang Zhang, Xinyu Hu, Huixuan Zhang, Junzhe Zhang, Xiaojun Wan

## Publication Venue
ACL 2025 (Main Conference)

## Key Method Details

**ICR Score**: A novel metric that measures "the contribution of modules to the hidden states' update" rather than examining static representations alone.

**ICR Probe**: The detection framework that leverages the ICR Score to track how hidden states evolve across transformer layers, identifying hallucinations through these dynamic patterns rather than isolated layer representations.

**Core Innovation**: The approach shifts from analyzing individual layer outputs to monitoring the sequential transformation of information through the model's layers, enabling more reliable hallucination identification with fewer learnable parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc5b08da-1895-4c13-b286-98bb9ef387d1",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "e165bff1-b550-4e58-9853-b2e7fb5f2aa6",
  "sourceToolAssistantUUID": "cc5b08da-1895-4c13-b286-98bb9ef387d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T13:57:20.485Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015BmxrdivsD5KRtfxY6yKqs`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "List all the ARR submission deadlines for 2026, especially the May 2026 cycle deadline and the October 2026 cycle deadline. Also list which conferences (EMNLP 2026, ACL 2027, etc.) correspond to which ARR cycles."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e165bff1-b550-4e58-9853-b2e7fb5f2aa6",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UHU9jRBSjwLoHwLMu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d8b93af-5ed5-4ec1-a9e1-d27a5ddc2d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FApaeDSdbsi2mLBxjyWC1M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5030,
      "cache_read_input_tokens": 11052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5030,
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

_source line 26 · 2026-05-15T13:57:21.111Z_

<details><summary>↩ Tool result · `toolu_01K5MENRyd911Vx5jvbG77hC`</summary>

```text
# Paper Summary: Attention Sinks for Hallucination Detection

## Citation Details
**Authors:** Jakub Binkowski, Kamil Adamczewski, Tomasz Kajdanowicz  
**Venue:** arXiv:2604.10697 (Computer Science > Computation and Language)  
**Submission:** April 12, 2026

## Full Abstract
"Large language models frequently exhibit hallucinations: fluent and confident outputs that are factually incorrect or unsupported by the input context. While recent hallucination detection methods have explored various features derived from attention maps, the underlying mechanisms they exploit remain poorly understood. In this work, we propose SinkProbe, a hallucination detection method grounded in the observation that hallucinations are deeply entangled with attention sinks - tokens that accumulate disproportionate attention mass during generation - indicating a transition from distributed, input-grounded attention to compressed, prior-dominated computation."

## Key Method Details

**Core Mechanism:** The paper identifies that attention sinks—tokens receiving excessive attention weight—serve as indicators of hallucination generation. The method suggests a shift occurs "from distributed, input-grounded attention to compressed, prior-dominated computation" when models generate false information.

**Tracked Metrics:** While not explicitly detailed in this abstract, the method computes "sink scores" from attention maps and identifies that "the classifier preferentially relies on sinks whose associated value vectors have large norms."

**Temporal Dynamics:** The approach implicitly addresses autoregressive generation by examining how attention patterns evolve during token-by-token generation, revealing when models transition away from input grounding toward internal prior-based computation.

**Performance:** The method achieves "state-of-the-art results across popular datasets and LLMs."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8d213cd-e34c-4036-b09f-a96307f0a582",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "f5ffcfa0-3881-4837-8e78-0ba6ca61ca59",
  "sourceToolAssistantUUID": "d8d213cd-e34c-4036-b09f-a96307f0a582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T13:57:21.738Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013s41Aws3beMz7vW6tkciax`</summary>

```json
{
  "url": "https://trybibby.com/conference-deadlines",
  "prompt": "List the submission deadlines for AAAI 2027 and ICLR 2027. I need the exact dates if available, or expected dates based on historical patterns."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ffcfa0-3881-4837-8e78-0ba6ca61ca59",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UHU9jRBSjwLoHwLMu6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c19afeb-cfca-4d40-9b6f-d2c0c3af603e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FApaeDSdbsi2mLBxjyWC1M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5030,
      "cache_read_input_tokens": 11052,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 738,
          "cache_read_input_tokens": 11052,
          "cache_creation_input_tokens": 5030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5030,
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

_source line 28 · 2026-05-15T13:57:23.419Z_

<details><summary>↩ Tool result · `toolu_015BmxrdivsD5KRtfxY6yKqs`</summary>

```text
# ARR 2026 Submission Deadlines and Conference Matches

## 2026 ARR Cycle Deadlines

According to the scheduling table provided:

- **May 2026 cycle**: "May 25, 2026" submission deadline
- **October 2026 cycle**: "October 12, 2026" submission deadline

## Conference-to-Cycle Alignment

The document maps the following venues to ARR cycles:

**May 2026 cycle submissions lead to:**
- EMNLP 2026 (commitment date: August 2, 2026)
- AACL 2026 (commitment date: August 26, 2026)

**October 2026 cycle submissions lead to:**
- EACL 2027 (commitment date: October 11, 2026)

Note: The website also indicates that "ACL 2026" and "EACL 2026" are listed among venues using ARR exclusively, though specific submission cycle alignments for these conferences are not detailed in the scheduling table provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d8b93af-5ed5-4ec1-a9e1-d27a5ddc2d5e",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "16efc6c5-cd75-4fe6-bbbb-0765d5e018db",
  "sourceToolAssistantUUID": "8d8b93af-5ed5-4ec1-a9e1-d27a5ddc2d5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T13:57:23.441Z_

<details><summary>↩ Tool result · `toolu_01KhshZvtiTZwpG2JatpbnZ3`</summary>

```text
# Attention Sink in Transformers Survey

**Title:** "Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation"

**Authors:** Zunhai Su, Hengyuan Zhang, Wei Wu, Yifan Zhang, Yaxiu Liu, He Xiao, Qingyao Yang, Yuxuan Sun, Rui Yang, Chao Zhang, Keyu Fan, Weihao Ye, Jing Xiong, Hui Shen, Chaofan Tao, Taiqiang Wu, Zhongwei Wan, Yulei Qian, Yuchen Xie, and Ngai Wong

**Abstract Summary:**
The survey addresses how Transformers often exhibit problematic concentration of attention on uninformative tokens. The authors describe this phenomenon as "a disproportionate amount of attention is focused on a small subset of specific yet uninformative tokens." The work organizes research across three dimensions: Fundamental Utilization, Mechanistic Interpretation, and Strategic Mitigation.

**Hallucination Connection:**
Yes, the abstract explicitly mentions that attention sinks "exacerbates issues such as hallucinations," establishing a link between this phenomenon and model-generated inaccuracies.

**Temporal Dynamics:**
The provided webpage content does not discuss temporal dynamics of attention sinks during generation. The abstract mentions effects on "training and inference dynamics" generally, but lacks specific discussion of how attention sinks evolve across generation steps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e66f2942-19e9-492a-8c91-0dda8b4d4dd9",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "c3371b3e-4399-4129-bf97-e2b054bf1005",
  "sourceToolAssistantUUID": "e66f2942-19e9-492a-8c91-0dda8b4d4dd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T13:57:25.311Z_

<details><summary>↩ Tool result · `toolu_01Mt2nbtWusaFFvUZgpvHMp6`</summary>

```text
# Paper Summary: Hallucination as Trajectory Commitment

## Full Abstract
"We present causal evidence that hallucination in autoregressive language models is an early trajectory commitment governed by asymmetric attractor dynamics. Using same-prompt bifurcation, in which we repeatedly sample identical inputs to observe spontaneous divergence, we isolate trajectory dynamics from prompt-level confounds. On Qwen2.5-1.5B across 61 prompts spanning six categories, 27 prompts (44.3%) bifurcate with factual and hallucinated trajectories diverging at the first generated token (KL = 0 at step 0, KL > 1.0 at step 1). Activation patching across 28 layers reveals a pronounced causal asymmetry: injecting a hallucinated activation into a correct trajectory corrupts output in 87.5% of trials (layer 20), while the reverse recovers only 33.3% (layer 24); both exceed the 10.4% baseline (p = 0.025) and 12.5% random-patch control. Window patching shows correction requires sustained multi-step intervention, whereas corruption needs only a single perturbation. Probing the prompt encoding itself, step-0 residual states predict per-prompt hallucination rate at Pearson r = 0.776 at layer 15 (p < 0.001 against a 1000-permutation null); unsupervised clustering identifies five regime-like groups (eta^2 = 0.55) whose saddle-adjacent cluster concentrates 12 of the 13 bifurcating false-premise prompts, indicating that the basin structure is organized around regime commitments fixed at prompt encoding."

## Author & Venue
**Author:** G. Aytug Akarlar  
**Status:** arXiv preprint (submitted April 16, 2026)  
**Subjects:** Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computation and Language (cs.CL)

## Key Methods
- Same-prompt bifurcation sampling across Qwen2.5-1.5B
- Activation patching across 28 layers with asymmetry measurements
- Window patching experiments analyzing intervention requirements
- Residual state probing and unsupervised clustering of regime groups

## Regarding Attention Sinks
The provided content does not discuss attention sinks or attention mechanisms specifically. The paper focuses on activation dynamics, layer-wise interventions, and attractor basin structure rather than attention-specific phenomena.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "936b3572-13f8-4aa3-b000-1a14ee0ec26e",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "c3c57c24-f79f-4320-bbed-3c9e386e560d",
  "sourceToolAssistantUUID": "936b3572-13f8-4aa3-b000-1a14ee0ec26e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T13:57:26.232Z_

<details><summary>↩ Tool result · `toolu_013s41Aws3beMz7vW6tkciax`</summary>

```text
# AAAI 2027 and ICLR 2027 Submission Deadlines

## AAAI 2027

The page lists two submission phases for AAAI 2027:

- **Abstract deadline:** "Jul 26, 2026, 11:59 AM UTC"
- **Full Paper deadline:** "Aug 2, 2026, 11:59 AM UTC"
- **Conference dates:** Feb 16–23, 2027 in Montréal, Canada

## ICLR 2027

Two submission phases are also specified:

- **Abstract deadline:** "Sep 19, 2026, 11:59 AM UTC"
- **Full Paper deadline:** "Sep 24, 2026, 11:59 AM UTC"
- **Conference dates:** Apr/May 2027 (specific venue TBD)

Both conferences follow a tiered submission structure with separate abstract registration and full paper deadlines, allowing researchers to refine their work between phases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c19afeb-cfca-4d40-9b6f-d2c0c3af603e",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "59dc73cb-3f7b-4edc-b44a-53690bf57bc9",
  "sourceToolAssistantUUID": "7c19afeb-cfca-4d40-9b6f-d2c0c3af603e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-15T13:57:29.683Z_

Now I have all the information needed. Let me also check if ACL 2027 maps to the ARR October 2026 cycle, since the ARR dates page didn't explicitly confirm that.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59dc73cb-3f7b-4edc-b44a-53690bf57bc9",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UJivWnvGaZhda6Gq1c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93a117c2-4781-49e3-ba2e-aea36a79544e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuasYjz1gLCddjthrcZcvE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3179,
      "cache_read_input_tokens": 16082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3179,
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

_source line 33 · 2026-05-15T13:57:30.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TpR3aFHFVYcBanPSZ8SWot`</summary>

```json
{
  "query": "ACL 2027 ARR commitment deadline submission cycle 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93a117c2-4781-49e3-ba2e-aea36a79544e",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UJivWnvGaZhda6Gq1c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b075fa0-7d22-4ee9-ab48-c90f28faa165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuasYjz1gLCddjthrcZcvE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3179,
      "cache_read_input_tokens": 16082,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 16082,
          "cache_creation_input_tokens": 3179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3179,
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

_source line 34 · 2026-05-15T13:57:34.896Z_

<details><summary>↩ Tool result · `toolu_01TpR3aFHFVYcBanPSZ8SWot`</summary>

```text
Web search results for query: "ACL 2027 ARR commitment deadline submission cycle 2026"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"}]

Based on the search results, I found relevant information about ACL 2027 and ARR submission/commitment deadlines:

For EACL 2027 (which is part of the ACL conference family), the ARR submission deadline for long and short papers is August 3, 2026.

Additionally, regarding the ARR commitment process, for EACL 2027, the final ARR submission date is August 3, 2026, and the commitment date is October 11, 2026.

The search results show that ARR switched to 10-week review cycles starting in May 2025, which affects the submission and review timeline for conferences like ACL 2027.

If you're looking for information about a specific ACL 2027 conference (such as ACL main conference, NAACL 2027, or another *CL event in 2027), please let me know and I can search for more specific deadline information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b075fa0-7d22-4ee9-ab48-c90f28faa165",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "0b95447e-a053-4a8e-a04e-91d48c64a100",
  "sourceToolAssistantUUID": "8b075fa0-7d22-4ee9-ab48-c90f28faa165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T13:57:38.728Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016TT2WLaMKx364pGDzyveAi`</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md",
  "prompt": "List all ARR cycle deadlines for 2026 and the conferences they map to. Specifically, which ARR cycle is ACL 2027 committed to? What about EMNLP 2026 and EACL 2027? Show the full table of dates and venues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b95447e-a053-4a8e-a04e-91d48c64a100",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UKMmoifYExGXpYzdT7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d520f937-3cae-4f1c-81aa-b5eda9839c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBRDZYXWs39vJnKdkMugNn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 19261,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 19261,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 796,
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

_source line 36 · 2026-05-15T13:57:43.551Z_

<details><summary>↩ Tool result · `toolu_016TT2WLaMKx364pGDzyveAi`</summary>

```text
# ARR 2026 Cycle Deadlines and Conference Commitments

Based on the document, here are the 2026 ARR cycles and their associated conferences:

## 2026 ARR Cycles and Deadlines

| Cycle | Submission | Commitment Date | Conference |
|-------|-----------|-----------------|------------|
| March 2026 | March 16 | May 24 | — |
| May 2026 | May 25 | August 2 | EMNLP 2026 |
| August 2026 | August 3 | October 11 | EACL 2027 |
| October 2026 | October 12 | December 20 | — |

## Conference Mapping

- **EMNLP 2026**: Corresponds to the May 2026 cycle with a final submission deadline of "May 25, 2026" and commitment date of August 2, 2026.

- **EACL 2027**: Corresponds to the August 2026 cycle with a final submission deadline of "August 3, 2026" and commitment date of October 11, 2026.

- **ACL 2027**: Not listed in the provided 2026 schedule. The document only mentions "ACL 2026" as a past venue participating in ARR.

Note: The August and October 2026 cycles show "TBA" for several review-related dates, indicating those details were pending publication at the time this document was created.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d520f937-3cae-4f1c-81aa-b5eda9839c37",
  "isSidechain": true,
  "promptId": "500d36b9-d925-456e-b902-c9ef1b04bbd2",
  "agentId": "ad66df379f78ed269",
  "type": "user",
  "uuid": "1d7750ae-e374-47ca-8af8-4d8c4abcacda",
  "sourceToolAssistantUUID": "d520f937-3cae-4f1c-81aa-b5eda9839c37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T13:58:24.362Z_

Now I have all the information. Here is the consolidated report.

---

## Findings

### 1. Venue Targeting / Deadline Analysis

**EMNLP 2026 (original target):**
- ARR submission deadline: **May 25, 2026** (confirmed). Commitment deadline: August 2, 2026.
- This matches exactly what the user specified. Today is May 15, 2026, so there are **10 days** remaining.

**Revised targets -- feasibility check:**

| Venue | Deadline | Source |
|-------|----------|--------|
| AAAI 2027 | Abstract: Jul 26, 2026; Paper: **Aug 2, 2026** | [Bibby](https://trybibby.com/conference-deadlines) |
| ICLR 2027 | Abstract: Sep 19, 2026; Paper: **Sep 24, 2026** | [Bibby](https://trybibby.com/conference-deadlines) |
| ACL 2027 via ARR | **Not yet listed** on ARR dates page. The October 2026 ARR cycle (deadline Oct 12, 2026) does not yet have ACL 2027 confirmed as a commitment target. Based on historical patterns, ACL 2027 would likely use the ARR December 2026 or February 2027 cycle. | [ARR Dates](https://aclrollingreview.org/dates) |
| EACL 2027 via ARR | ARR Aug 3, 2026 submission; commitment Oct 11, 2026 | [ARR Dates](https://aclrollingreview.org/dates) |

**Key observation:** The user originally asked for EMNLP 2026 (ARR May 25, 2026). The revised plan targeting AAAI 2027 / ICLR 2027 / ACL 2027 is a significant scope change -- it abandons the imminent EMNLP 2026 deadline and pushes to venues 2-5 months further out. The earliest revised target (AAAI 2027, Aug 2) gives ~2.5 months more time. ACL 2027 via ARR is not yet confirmed but would likely be late 2026 or early 2027. If the user specifically wanted EMNLP 2026, the revised targets deviate from that request and should be flagged.

---

### 2. ICR Probe Paper (arXiv 2507.16488) -- VERIFIED

- **Title:** "ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection in LLMs"
- **Authors:** Zhenliang Zhang, Xinyu Hu, Huixuan Zhang, Junzhe Zhang, Xiaojun Wan
- **Venue:** ACL 2025 Main Conference (confirmed via [ACL Anthology](https://aclanthology.org/2025.acl-long.880/))
- **Core idea:** Introduces the **ICR Score** (Information Contribution to Residual Stream), which quantifies how much each module contributes to hidden state updates across layers. The **ICR Probe** then captures cross-layer evolution of hidden states to detect hallucinations, achieving superior performance with significantly fewer parameters than static-representation baselines.
- **Relevance to SinkWatch:** High. ICR Probe tracks *dynamic evolution* of hidden states across layers, which is conceptually adjacent to tracking attention sink dynamics across generation steps. However, ICR Probe focuses on **cross-layer** (depth) dynamics within a single forward pass, while SinkWatch would focus on **cross-token** (temporal) dynamics across autoregressive generation steps. This is a meaningful distinction -- they are complementary approaches to "dynamic" hallucination detection.

---

### 3. Very Recent Competing Work (April 2026) -- CRITICAL FINDINGS

Three papers from April 2026 are highly relevant and represent potential direct competition or overlap with SinkWatch:

**(a) SinkProbe (arXiv 2604.10697, April 12, 2026)**
- **Authors:** Jakub Binkowski, Kamil Adamczewski, Tomasz Kajdanowicz
- **Title:** "Attention Sinks as Internal Signals for Hallucination Detection in Large Language Models"
- **Core finding:** Hallucinations are "deeply entangled with attention sinks" -- tokens that accumulate disproportionate attention mass during generation. Detects a transition "from distributed, input-grounded attention to compressed, prior-dominated computation." Achieves SOTA results.
- **Threat level to SinkWatch: VERY HIGH.** This paper directly uses attention sinks as hallucination detection signals, which appears to be the core premise of SinkWatch. The key question is whether SinkWatch's temporal/dynamic tracking differs sufficiently from SinkProbe's approach.

**(b) Hallucination as Trajectory Commitment (arXiv 2604.15400, April 16, 2026)**
- **Author:** G. Aytug Akarlar
- **Title:** "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation"
- **Core finding:** Hallucination is an early trajectory commitment -- 44.3% of prompts bifurcate with factual/hallucinated paths diverging at the *first generated token*. Corruption requires only a single perturbation, while correction requires sustained multi-step intervention. Uses activation patching across layers.
- **Relevance:** This provides strong mechanistic evidence for why temporal monitoring during generation matters. It does not use attention sinks specifically, but the attractor dynamics framework could be relevant to SinkWatch's theoretical framing.

**(c) Attention Sink Survey (arXiv 2604.10098, April 2026)**
- **Title:** "Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation"
- **Authors:** Zunhai Su et al. (20+ authors)
- **Relevance:** A comprehensive survey explicitly linking attention sinks to hallucination. Would need to be cited by SinkWatch and positions the field as already well-mapped.

---

### Summary of Actionable Concerns

1. **Venue mismatch:** The revised targets (AAAI/ICLR/ACL 2027) abandon the user's specified EMNLP 2026 target. This should be explicitly flagged to the user for confirmation.

2. **SinkProbe (April 2026) is a direct competitor.** A paper titled "Attention Sinks as Internal Signals for Hallucination Detection" appeared just one month ago and achieves SOTA. SinkWatch must clearly differentiate itself -- likely by emphasizing *temporal dynamics across generation steps* (how sink patterns shift token-by-token) rather than *static sink features at a given point*. The proposal needs to cite SinkProbe and explicitly argue what new ground SinkWatch covers.

3. **ICR Probe is confirmed** as published at ACL 2025 and is relevant but complementary (cross-layer vs. cross-token dynamics).

4. **The field is moving fast** -- three relevant papers in April 2026 alone, plus a comprehensive survey. Any submission needs to be positioned very carefully against this rapidly evolving landscape.

Sources:
- [ICR Probe (arXiv 2507.16488)](https://arxiv.org/abs/2507.16488)
- [ICR Probe at ACL Anthology](https://aclanthology.org/2025.acl-long.880/)
- [SinkProbe (arXiv 2604.10697)](https://arxiv.org/abs/2604.10697)
- [Hallucination as Trajectory Commitment (arXiv 2604.15400)](https://arxiv.org/abs/2604.15400)
- [Attention Sink Survey (arXiv 2604.10098)](https://arxiv.org/abs/2604.10098)
- [ARR Dates and Venues](https://aclrollingreview.org/dates)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [AI & ML Conference Deadlines](https://trybibby.com/conference-deadlines)
- [AAAI 2027 on OpenReview](https://openreview.net/group?id=AAAI.org%2F2027%2FConference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d7750ae-e374-47ca-8af8-4d8c4abcacda",
  "isSidechain": true,
  "agentId": "ad66df379f78ed269",
  "requestId": "req_011Cb4UKzo2KWqSDwCEG2NXJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "710f84f7-1ef4-4372-8b9c-833550a33dfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2f8076af-224f-4736-ae90-4e3d1d6314ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EyTLTnbbrgeXF15Ug1hcFF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 20057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 518,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
