# Research conversation: I need to check two things: 1. **SARM paper (ICLR 2026)**: Search for "SARM Stage-Aware Reward Modeling" or arXiv:2509.2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-abe2e982c5a0763f7.jsonl`
- **Structured JSON:** [`4c344e5838b281343d15.json`](../../sessions/4c/4c344e5838b281343d15.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-13T10:13:36.976Z_

I need to check two things:

1. **SARM paper (ICLR 2026)**: Search for "SARM Stage-Aware Reward Modeling" or arXiv:2509.25358. This paper introduces "Reward-Aligned Behavior Cloning (RA-BC)" that "filters and reweights demonstrations based on reward estimates." This sounds extremely relevant to a proposal about when to filter vs weight demonstrations. Please fetch the paper and check:
   - Does RA-BC provide any decision rule or analysis for when to filter vs when to reweight?
   - What exactly is the RA-BC mechanism? Is it binary filtering, continuous weighting, or both?
   - Was it accepted at ICLR 2026?

2. **CoRL 2026 deadline**: Search for "CoRL 2026 deadline" or "CoRL 2026 submission" to verify the deadline. The user mentioned abstract deadline 2026-05-26 and paper deadline 2026-05-29.

3. **ICRA 2027 deadline**: Search for "ICRA 2027 deadline" or "ICRA 2027 submission date" to check if there's any confirmed information.

4. Also search for "Why Less is More data curation theory ICLR 2025" - arXiv:2511.03492 - this is claimed to provide theoretical framework for when data pruning helps, which is directly relevant.

Report findings on all four items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "3d1c19ca-3b43-42e0-9b47-a325cd6017fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T10:13:36.979Z_

```json
{
  "parentUuid": "3d1c19ca-3b43-42e0-9b47-a325cd6017fd",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
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
  "uuid": "83d0f445-6119-4145-ad22-1a8e86ba7a60",
  "timestamp": "2026-05-13T10:13:36.979Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T10:13:42.778Z_



I'll search for all four items in parallel. Let me start by loading the web search and fetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83d0f445-6119-4145-ad22-1a8e86ba7a60",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPcxhtbvhWC5puMuVEz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6437e33f-f66f-4c4a-8224-a8432218c596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdJ8HGCg1afyMkZa7UbhG6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 882,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-13T10:13:43.230Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ejqy6bN8LA7gVToNhiYsu2`</summary>

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
  "parentUuid": "6437e33f-f66f-4c4a-8224-a8432218c596",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPcxhtbvhWC5puMuVEz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ccce734-c079-4146-b3f7-86966760ec3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdJ8HGCg1afyMkZa7UbhG6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 8223,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 882
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 882,
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

_source line 5 · 2026-05-13T10:13:43.233Z_

<details><summary>↩ Tool result · `toolu_01Ejqy6bN8LA7gVToNhiYsu2`</summary>

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
  "parentUuid": "3ccce734-c079-4146-b3f7-86966760ec3e",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "a3deb323-1768-4ba2-b2a0-aa4e3c2ebc4b",
  "sourceToolAssistantUUID": "3ccce734-c079-4146-b3f7-86966760ec3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T10:13:46.355Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3deb323-1768-4ba2-b2a0-aa4e3c2ebc4b",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPdRSURJC6KRzzeidPf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2728f281-0b0e-4af8-8e38-70f51e732839",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVh3FKU5d1k6kFHdQoyjja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-13T10:13:47.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NqEhEqSjZzuHaCQA14Qi74`</summary>

```json
{
  "query": "SARM Stage-Aware Reward Modeling arXiv:2509.25358 ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2728f281-0b0e-4af8-8e38-70f51e732839",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPdRSURJC6KRzzeidPf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d7d7a9a-86e1-4e09-afb3-fdb72f8b1daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVh3FKU5d1k6kFHdQoyjja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-13T10:13:47.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WZiW6rWvdebbLGPuWE6Ci5`</summary>

```json
{
  "query": "CoRL 2026 deadline submission date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d7d7a9a-86e1-4e09-afb3-fdb72f8b1daf",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPdRSURJC6KRzzeidPf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ec46f9d-8095-4df9-84f1-9c0ff9cc164d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVh3FKU5d1k6kFHdQoyjja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-13T10:13:48.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011NmbdiU59WmaQggC3jS7Xk`</summary>

```json
{
  "query": "ICRA 2027 deadline submission date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ec46f9d-8095-4df9-84f1-9c0ff9cc164d",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPdRSURJC6KRzzeidPf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4772af31-955b-4aed-b154-4f939339997d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVh3FKU5d1k6kFHdQoyjja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-13T10:13:49.308Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Z4bkKMdgos1MgoocMdY8p`</summary>

```json
{
  "query": "\"Why Less is More\" data curation theory arXiv:2511.03492 ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4772af31-955b-4aed-b154-4f939339997d",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPdRSURJC6KRzzeidPf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3bc18f4-e065-43b8-919a-bce025b3b782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVh3FKU5d1k6kFHdQoyjja",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 9105,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 239,
          "cache_read_input_tokens": 9105,
          "cache_creation_input_tokens": 1912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1912,
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

_source line 11 · 2026-05-13T10:13:51.440Z_

<details><summary>↩ Tool result · `toolu_01WZiW6rWvdebbLGPuWE6Ci5`</summary>

```text
Web search results for query: "CoRL 2026 deadline submission date"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"}]

Based on the search results, here are the CoRL 2026 submission deadlines:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.

Note that there are slightly different dates reported from the official X/Twitter announcement which mentions May 25 for Abstract Submission and May 28 for Full Paper Submission. I'd recommend checking the official CoRL 2026 website or the OpenReview submission portal to confirm the exact deadlines, as the deadlines are final, and accommodations cannot be made for missing them.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ec46f9d-8095-4df9-84f1-9c0ff9cc164d",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "a042b65e-b4f6-4c11-abc5-b38319e6a204",
  "sourceToolAssistantUUID": "4ec46f9d-8095-4df9-84f1-9c0ff9cc164d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T10:13:51.470Z_

<details><summary>↩ Tool result · `toolu_011NmbdiU59WmaQggC3jS7Xk`</summary>

```text
Web search results for query: "ICRA 2027 deadline submission date"

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Conference Calender 2027 in Kanazawa Institute of Technology","url":"https://wwwr.kanazawa-it.ac.jp/kawai/calendar/2027/cal27.html"},{"title":"Timetable 2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853/timetable.html"},{"title":"International Conference on Robotics and Automation","url":"https://roboticsforum.org/Conference/2027/ICRA/"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"}]

Based on the search results, I found that ICRA 2027 will be held May 24-28, 2027, and it will be held in Seoul, South Korea.

However, the search results did not contain specific information about the paper submission deadline date for ICRA 2027. The official IEEE ICRA 2027 website (2027.ieee-icra.org) would have the most up-to-date deadline information, so I recommend checking there directly for the submission deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4772af31-955b-4aed-b154-4f939339997d",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "47f5c938-29ae-4946-acfd-8d864fff9af2",
  "sourceToolAssistantUUID": "4772af31-955b-4aed-b154-4f939339997d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T10:13:52.998Z_

<details><summary>↩ Tool result · `toolu_01NqEhEqSjZzuHaCQA14Qi74`</summary>

```text
Web search results for query: "SARM Stage-Aware Reward Modeling arXiv:2509.25358 ICLR 2026"

Links: [{"title":"[2509.25358] SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://arxiv.org/abs/2509.25358"},{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://arxiv.org/html/2509.25358"},{"title":"ICLR Poster SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://iclr.cc/virtual/2026/poster/10008682"},{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://qianzhong-chen.github.io/sarm.github.io/"},{"title":"(PDF) SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://www.researchgate.net/publication/396048367_SARM_Stage-Aware_Reward_Modeling_for_Long_Horizon_Robot_Manipulation"},{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=aemqAxScl9"},{"title":"SARM: Stage-Aware Reward Modeling","url":"https://huggingface.co/docs/lerobot/en/sarm"},{"title":"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.25358v2"},{"title":"[Literature Review] SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation","url":"https://www.themoonlight.io/en/review/sarm-stage-aware-reward-modeling-for-long-horizon-robot-manipulation"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"}]

Based on the search results, here's what I found about SARM:

## SARM: Stage-Aware Reward Modeling

SARM proposes a stage-aware, video-based reward modeling framework that jointly predicts task stage and fine-grained progress, using natural language subtask annotations to derive consistent labels across variable-length demonstrations.

**Key Features:**
- This approach avoids the brittleness of frame index based labeling and provides stable supervision even in tasks like T-shirt folding.
- The reward model is robust to demonstration variability, generalizes to out-of-distribution scenarios, and improves downstream policy training.

**Authors and Affiliations:**
The paper is authored by Qianzhong Chen, Justin Yu, Mac Schwager, Pieter Abbeel, Yide Shentu, and Philipp Wu from Stanford University, UC Berkeley, and xdof.ai.

**Publication Status:**
The paper was published as a conference paper at ICLR 2026.

The paper addresses challenges in long-horizon robot manipulation, particularly with deformable objects where demonstration quality can be inconsistent. The method uses natural language annotations to create more robust reward models for training robot policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d7d7a9a-86e1-4e09-afb3-fdb72f8b1daf",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "6a6cad70-5e0b-47d8-a6a4-f56a8211bd88",
  "sourceToolAssistantUUID": "3d7d7a9a-86e1-4e09-afb3-fdb72f8b1daf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T10:13:56.138Z_

<details><summary>↩ Tool result · `toolu_018Z4bkKMdgos1MgoocMdY8p`</summary>

```text
Web search results for query: ""Why Less is More" data curation theory arXiv:2511.03492 ICLR 2025"

Links: [{"title":"[2511.03492] Why Less is More (Sometimes): A Theory of Data Curation","url":"https://arxiv.org/abs/2511.03492"},{"title":"Why Less is More (Sometimes): A Theory of Data Curation","url":"https://arxiv.org/html/2511.03492v1"},{"title":"(PDF) Why Less is More (Sometimes): A Theory of Data Curation","url":"https://www.researchgate.net/publication/397321774_Why_Less_is_More_Sometimes_A_Theory_of_Data_Curation"},{"title":"Why Less is More (Sometimes): A Theory of Data Curation | OpenReview","url":"https://openreview.net/forum?id=8KcjEygedc"},{"title":"A THEORY OF DATA CURATION","url":"https://openreview.net/pdf?id=8KcjEygedc"}]

I found the paper! Here's what I can tell you about this research:

## Overview

This paper introduces a theoretical framework to resolve a central paradox in modern machine learning: When is it better to use less data? This question has become critical as classical scaling laws suggesting "more is more" are challenged by methods like LIMO ("less is more") and s1, which achieve superior performance with small, aggressively curated datasets.

## Key Contributions

The authors study data curation strategies where an imperfect oracle selects the training examples according to their difficulty and correctness, and their results provide exact scaling law curves for test error under both label-agnostic and label-aware curation rules, revealing when and why keeping only a subset of data can improve generalization.

Under certain conditions, small curated datasets can outperform full datasets, and the authors provide analytical conditions for this by deriving precise phase transition curves tied to data size and quality.

## Validation and Applications

The theoretical claims are validated with empirical results on ImageNet, confirming predictions about when curation improves accuracy and can even mitigate model collapse. Furthermore, the framework provides a principled explanation for the contradictory curation strategies recently observed in LLM mathematical reasoning.

The paper was posted to arXiv on November 5, 2025, and is available on OpenReview for ICLR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3bc18f4-e065-43b8-919a-bce025b3b782",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "64326eb7-b2b6-4b29-b758-27d69ceb878a",
  "sourceToolAssistantUUID": "c3bc18f4-e065-43b8-919a-bce025b3b782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-13T10:14:03.591Z_

Good, I have initial results. Now let me fetch the detailed content from the SARM paper and the "Why Less is More" paper to answer the specific questions, and also fetch the CoRL 2026 and ICRA 2027 deadline pages for exact dates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64326eb7-b2b6-4b29-b758-27d69ceb878a",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPeNjXssTH4948mWK8w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "921a8ea9-11da-4138-8a87-dc1703fd662b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GReStiecpTw6qxLuvyHh7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 11017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2932,
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

_source line 16 · 2026-05-13T10:14:06.614Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015ZiLKQiHphMTuusCuB2e5q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.25358",
  "prompt": "Extract the full abstract and any mentions of \"Reward-Aligned Behavior Cloning\" or \"RA-BC\". Does the paper introduce a method called RA-BC? Does it discuss filtering vs reweighting demonstrations? What is the core mechanism of the paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "921a8ea9-11da-4138-8a87-dc1703fd662b",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPeNjXssTH4948mWK8w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21e1f910-db3f-456f-9dd3-55056fe3cf1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GReStiecpTw6qxLuvyHh7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 11017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2932,
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

_source line 17 · 2026-05-13T10:14:08.967Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wxekxf7UmHfrcrAiYpGmyt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.03492",
  "prompt": "Extract the full abstract. Does this paper provide a decision rule or theoretical framework for when to filter/prune data vs when to reweight? What are the key theoretical results about when less data is better? Was it accepted at ICLR 2025 or is it a preprint? Check the submission date carefully."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21e1f910-db3f-456f-9dd3-55056fe3cf1f",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPeNjXssTH4948mWK8w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ec0f584-9cb0-4938-82d2-13210797aa2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GReStiecpTw6qxLuvyHh7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 11017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2932,
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

_source line 18 · 2026-05-13T10:14:10.248Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VZPFuHWt36dCJYSe5CKwXv`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract all submission deadlines for CoRL 2026, including abstract deadline and paper deadline. List exact dates and times."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ec0f584-9cb0-4938-82d2-13210797aa2d",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPeNjXssTH4948mWK8w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bfcdab7-a61a-42ac-8ea1-72a9263aed1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GReStiecpTw6qxLuvyHh7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 11017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2932,
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

_source line 19 · 2026-05-13T10:14:11.535Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012AbAYFcDqNofzqLSRriJPy`</summary>

```json
{
  "url": "https://2027.ieee-icra.org/contribute/",
  "prompt": "Extract the paper submission deadline for ICRA 2027. List any dates mentioned for submissions, including abstract deadlines, paper deadlines, and notification dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bfcdab7-a61a-42ac-8ea1-72a9263aed1f",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPeNjXssTH4948mWK8w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "962cbf63-9275-4743-876a-5c4ef3c2e2a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GReStiecpTw6qxLuvyHh7K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 11017,
      "output_tokens": 519,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2932
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 519,
          "cache_read_input_tokens": 11017,
          "cache_creation_input_tokens": 2932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2932,
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

_source line 20 · 2026-05-13T10:14:12.601Z_

<details><summary>↩ Tool result · `toolu_01VZPFuHWt36dCJYSe5CKwXv`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the provided web page content, **no specific submission deadlines are listed**. 

The page states: "For paper submission format and timeline, see: [Instruction for Authors](/contributions/instruction-for-authors)" but does not include the actual dates or times on this page.

To find the abstract and paper deadlines for CoRL 2026, you would need to visit the "Instruction for Authors" section referenced in the Call for Papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bfcdab7-a61a-42ac-8ea1-72a9263aed1f",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "fa3babfd-dc35-4de2-82f7-d00b60ab22ac",
  "sourceToolAssistantUUID": "4bfcdab7-a61a-42ac-8ea1-72a9263aed1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T10:14:13.385Z_

<details><summary>↩ Tool result · `toolu_015ZiLKQiHphMTuusCuB2e5q`</summary>

```text
# SARM Paper Analysis

## Full Abstract
"Large-scale robot learning has made progress on complex manipulation tasks, yet long horizon, contact rich problems, especially those involving deformable objects, remain challenging due to inconsistent demonstration quality. We propose a stage-aware, video-based reward modeling framework that jointly predicts task stage and fine-grained progress, using natural language subtask annotations to derive consistent labels across variable-length demonstrations. This avoids the brittleness of frame index based labeling and provides stable supervision even in tasks like T-shirt folding. Our reward model is robust to demonstration variability, generalizes to out-of-distribution scenarios, and improves downstream policy training. Building on it, we introduce Reward-Aligned Behavior Cloning (RA-BC), which filters and reweights demonstrations based on reward estimates. Experiments show that our method significantly outperforms baselines in both real-world rollouts and human validation. On T-shirt folding, we achieve 83% success from the flattened state and 67% from the crumpled state, compared to 8% and 0% with vanilla BC. Overall, our results highlight reward modeling as a scalable and annotation-efficient solution for long horizon robotic manipulation."

## RA-BC Method
Yes, the paper introduces **Reward-Aligned Behavior Cloning (RA-BC)**. This technique employs both approaches: the abstract specifies it "filters and reweights demonstrations based on reward estimates," indicating the method combines filtering (removing lower-quality demonstrations) with reweighting (adjusting importance of remaining ones).

## Core Mechanism
The paper's central innovation is a video-based framework that jointly predicts task progression stages and fine-grained progress using natural language annotations, enabling consistent labeling across variable-length demonstrations without relying on brittle frame indexing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21e1f910-db3f-456f-9dd3-55056fe3cf1f",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "bbf61ac5-f660-4e2d-85cd-41790a700b73",
  "sourceToolAssistantUUID": "21e1f910-db3f-456f-9dd3-55056fe3cf1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T10:14:14.535Z_

<details><summary>↩ Tool result · `toolu_012AbAYFcDqNofzqLSRriJPy`</summary>

```text
# ICRA 2027 Paper Submission Deadlines

Based on the webpage content provided, **ICRA 2027's submission information is not yet available**. The page indicates that "ICRA 2027 Website under Construction" as of May 5, 2026.

However, the page does contain details for **ICRA 2025**, which show:

- **Paper Submission Deadline:** "15 September 2024 (11:59 PST)"
- **Accompanying Videos:** August 5 – September 9, 2024, and September 17–22, 2024

The webpage invites contributors to check back for ICRA 2027 specifics, directing visitors to the "Media Room" and "calendar" for upcoming deadlines once they are announced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "962cbf63-9275-4743-876a-5c4ef3c2e2a3",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "d8f4f715-aa34-41a3-a1df-8d1faadb32d0",
  "sourceToolAssistantUUID": "962cbf63-9275-4743-876a-5c4ef3c2e2a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T10:14:14.570Z_

<details><summary>↩ Tool result · `toolu_01Wxekxf7UmHfrcrAiYpGmyt`</summary>

```text
# Analysis of arXiv:2511.03492

## Full Abstract
"This paper introduces a theoretical framework to resolve a central paradox in modern machine learning: When is it better to use less data? This question has become critical as classical scaling laws suggesting 'more is more' are challenged by methods like LIMO and s1, which achieve superior performance with small, aggressively curated datasets. Here, we study data curation strategies where an imperfect oracle selects the training examples according to their difficulty and correctness. Our results provide exact scaling law curves for test error under both label-agnostic and label-aware curation rules, revealing when and why keeping only a subset of data can improve generalization."

## Decision Framework Provided
Yes, the paper provides a theoretical framework with **precise phase transition curves** tied to data size and quality. It analyzes both label-agnostic and label-aware curation strategies. However, the abstract does not explicitly state whether the paper addresses reweighting versus filtering as distinct approaches.

## Key Theoretical Results
The framework reveals that:
- Under certain conditions, small curated datasets outperform full datasets
- Curation can mitigate model collapse
- Exact scaling law curves define when data subsetting improves generalization

## Publication Status
This is a **preprint, not an accepted conference paper**. Submission date: **November 5, 2025**. No acceptance notification or venue publication is indicated on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ec0f584-9cb0-4938-82d2-13210797aa2d",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "a5e9833c-9667-461f-886c-ae9b4847bbab",
  "sourceToolAssistantUUID": "8ec0f584-9cb0-4938-82d2-13210797aa2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T10:14:18.702Z_

Let me get more details on the SARM paper's RA-BC mechanism and fetch the CoRL deadlines from the instructions page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5e9833c-9667-461f-886c-ae9b4847bbab",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPfjWieRpxvv7SokDiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "271cfc93-c8ca-4cbc-afa2-c25d32380b64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQg2yeheXaSHabr8x2jmrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 13949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 25 · 2026-05-13T10:14:22.536Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WTtpPc46k449FCoJPQZYCr`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.25358",
  "prompt": "Find and extract all details about the RA-BC (Reward-Aligned Behavior Cloning) method. Specifically: 1) Is it binary filtering, continuous weighting, or both? 2) Does it provide any decision rule or analysis for WHEN to filter vs WHEN to reweight? 3) How exactly does it use the reward estimates - what is the formula or mechanism? 4) Does it discuss thresholds for filtering? Look for sections about RA-BC, reward-aligned behavior cloning, demonstration filtering, demonstration reweighting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "271cfc93-c8ca-4cbc-afa2-c25d32380b64",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPfjWieRpxvv7SokDiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aca6876a-944e-427f-9d23-a119e53133db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQg2yeheXaSHabr8x2jmrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 13949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 26 · 2026-05-13T10:14:24.001Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LMiYe3NFsXH41k6Lk76Yje`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all submission deadlines for CoRL 2026, including abstract deadline, paper deadline, supplementary material deadline, notification dates. List exact dates and times."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aca6876a-944e-427f-9d23-a119e53133db",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPfjWieRpxvv7SokDiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca5d069a-0759-40f0-9c2e-49c91a3e7a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQg2yeheXaSHabr8x2jmrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 13949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 27 · 2026-05-13T10:14:25.887Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017DG8RPmvcbMGvuFiuKi5Xb`</summary>

```json
{
  "url": "https://openreview.net/forum?id=8KcjEygedc",
  "prompt": "Check the status of this paper. Was it accepted at ICLR 2025 or ICLR 2026? What venue is it submitted to? Is there a decision (accept/reject)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca5d069a-0759-40f0-9c2e-49c91a3e7a2c",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPfjWieRpxvv7SokDiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f47062e3-3726-4efe-82b3-3558251a3954",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQg2yeheXaSHabr8x2jmrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 13949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1293,
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

_source line 28 · 2026-05-13T10:14:27.406Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Dh1uEMqG8eG732PJYKLt4N`</summary>

```json
{
  "url": "https://iclr.cc/virtual/2026/poster/10008682",
  "prompt": "Confirm that SARM was accepted at ICLR 2026. Extract any details about the paper's presentation status (poster, oral, spotlight)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f47062e3-3726-4efe-82b3-3558251a3954",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPfjWieRpxvv7SokDiQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd79c497-54c6-4ce3-b431-4c73051612ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQg2yeheXaSHabr8x2jmrP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 1293,
      "cache_read_input_tokens": 13949,
      "output_tokens": 548,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 343,
          "output_tokens": 548,
          "cache_read_input_tokens": 13949,
          "cache_creation_input_tokens": 1293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1293,
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

_source line 29 · 2026-05-13T10:14:27.496Z_

<details><summary>↩ Tool result · `toolu_01LMiYe3NFsXH41k6Lk76Yje`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the provided content, the following deadline information is mentioned:

**Camera-Ready Submission:**
- "The camera-ready version of your paper is due by Oct 12, 2026 (23:59 Anywhere on Earth)"

**Rebuttal Deadline:**
- Referenced as existing but no specific date provided in the document

**Paper/Abstract Deadlines:**
- The page notes "the paper submission deadline is Thursday (5/28) EOD rather than Friday" but does not specify the year or provide complete abstract deadline details

**Notable Limitation:** The document does not contain a comprehensive "Key Dates" section with all submission deadlines explicitly listed. While the page heading references a "Key Dates" section, the actual deadline details are sparse. The instructions mention that deadlines are final and accommodations cannot be made for missed deadlines, but specific dates for abstract submission, paper submission, and review notification are not provided in this excerpt.

For complete deadline information, you would need to access the full Key Dates section of the CoRL 2026 website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca5d069a-0759-40f0-9c2e-49c91a3e7a2c",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "b80bf913-7642-473a-b617-5de77792ab97",
  "sourceToolAssistantUUID": "ca5d069a-0759-40f0-9c2e-49c91a3e7a2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T10:14:28.192Z_

<details><summary>↩ Tool result · `toolu_017DG8RPmvcbMGvuFiuKi5Xb`</summary>

```text
Based on the content provided:

**Venue:** The paper is submitted to "ICLR 2026 Conference"

**Status:** Listed as "ICLR 2026 Poster" - indicating it was accepted

**Decision:** Accept (the paper appears as an accepted poster presentation)

This paper was accepted at ICLR 2026, not ICLR 2025. The publication date shown is "26 Jan 2026" with last modification on "11 Apr 2026."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f47062e3-3726-4efe-82b3-3558251a3954",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "db0c932c-21a4-431e-99e3-e63eec155797",
  "sourceToolAssistantUUID": "f47062e3-3726-4efe-82b3-3558251a3954",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T10:14:29.275Z_

<details><summary>↩ Tool result · `toolu_01WTtpPc46k449FCoJPQZYCr`</summary>

```text
# RA-BC Method Details

## 1) Binary Filtering vs. Continuous Weighting

RA-BC uses **continuous weighting**, not binary filtering. The paper explicitly states it performs "soft filtering" rather than hard selection: "RA-BC...softly filters noisy or non-progressing data while preserving training stability via normalization."

## 2) Decision Rule for Filtering vs. Reweighting

The paper does **not provide a decision rule** for when to filter versus reweight. Instead, RA-BC uses a unified continuous weighting approach that inherently handles both cases through a single mechanism.

## 3) Mechanism and Formula

RA-BC uses this three-step process:

**Step 1 - Progress Delta:** For each demonstration, it calculates `r̂ᵢ = φ(oᵢᵗ⁺ᐃ) - φ(oᵢᵗ)`, where φ represents the reward model's progress score.

**Step 2 - Statistical Weighting:** It maintains running statistics (mean μ, std σ) of progress deltas, then applies: `w̃ᵢ = clip((r̂ᵢ - (μ - 2σ)) / (4σ + ϵ), 0, 1)`

**Step 3 - Prior Override:** It applies a threshold κ with: `wᵢ = 1{r̂ᵢ > κ} + 1{0 ≤ r̂ᵢ ≤ κ}w̃ᵢ`

The weighted loss becomes: `ℒ_RA-BC(θ) = Σ(wᵢ·ℓ(...)) / Σ(wᵢ) + ε`

## 4) Threshold Discussion

The paper mentions κ = 0.01 in experiments (roughly 1.5 minutes task duration, representing "top 5% of demonstrations") but provides **minimal discussion of threshold selection methodology**. It simply states thresholds "make weights decisive for clearly good/bad items."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aca6876a-944e-427f-9d23-a119e53133db",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "d1eab0fb-939d-43f8-90ff-d7ace0563c15",
  "sourceToolAssistantUUID": "aca6876a-944e-427f-9d23-a119e53133db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T10:14:30.344Z_

<details><summary>↩ Tool result · `toolu_01Dh1uEMqG8eG732PJYKLt4N`</summary>

```text
# SARM Acceptance at ICLR 2026

**Confirmation:** Yes, SARM was accepted at ICLR 2026.

**Presentation Status:** The paper is being presented as a **poster** at the conference.

**Details:** According to the page header, "SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation" is listed as an "ICLR Poster" scheduled for "Sat, Apr 25, 2026 • 11:15 AM – 1:45 PM PDT Pavilion 3 P3-#1107." The presentation format is explicitly identified as a poster session rather than an oral or spotlight presentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd79c497-54c6-4ce3-b431-4c73051612ac",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "eba8ce9f-18f2-4d48-9c8c-57f5ab63d0ad",
  "sourceToolAssistantUUID": "dd79c497-54c6-4ce3-b431-4c73051612ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T10:14:33.847Z_

Now let me search for the exact CoRL 2026 deadlines and check the "Why Less is More" paper's venue more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eba8ce9f-18f2-4d48-9c8c-57f5ab63d0ad",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPgtsozdKoxFVu8vAH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eac5f942-7061-4d4b-8640-41a67d5c27b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gtyjEKDM6EQSNL9YLhoym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 15242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2021,
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

_source line 34 · 2026-05-13T10:14:34.928Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K3UKYebY7mPb2upzPSkCCp`</summary>

```json
{
  "query": "CoRL 2026 abstract deadline May 26 paper deadline May 29 exact dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eac5f942-7061-4d4b-8640-41a67d5c27b6",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPgtsozdKoxFVu8vAH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39c3ec51-60b8-4f54-bfcf-52a11477b2d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gtyjEKDM6EQSNL9YLhoym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 15242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2021,
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

_source line 35 · 2026-05-13T10:14:35.069Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WewnWLdQC3hKZUv5Nt9L9N`</summary>

```json
{
  "query": "\"Why Less is More\" \"Theory of Data Curation\" ICLR 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39c3ec51-60b8-4f54-bfcf-52a11477b2d2",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPgtsozdKoxFVu8vAH2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85e2124b-e057-4ece-8eda-a14fda4f0886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gtyjEKDM6EQSNL9YLhoym",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 15242,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2021
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 15242,
          "cache_creation_input_tokens": 2021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2021,
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

_source line 36 · 2026-05-13T10:14:38.441Z_

<details><summary>↩ Tool result · `toolu_01K3UKYebY7mPb2upzPSkCCp`</summary>

```text
Web search results for query: "CoRL 2026 abstract deadline May 26 paper deadline May 29 exact dates"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"CoRL 2026 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2026"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"}]

Based on the search results, I found the exact dates for CoRL 2026 submission deadlines:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.

Note: There appears to be a slight discrepancy in one source (a Twitter post) that mentions May 25 for abstract submission and May 28 for full paper submission, but the most recent and authoritative sources confirm the May 26 and May 29 dates with times specified as 11:59 UTC.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39c3ec51-60b8-4f54-bfcf-52a11477b2d2",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "046b0f02-185f-46fb-977a-c505573e135b",
  "sourceToolAssistantUUID": "39c3ec51-60b8-4f54-bfcf-52a11477b2d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T10:14:39.511Z_

<details><summary>↩ Tool result · `toolu_01WewnWLdQC3hKZUv5Nt9L9N`</summary>

```text
Web search results for query: ""Why Less is More" "Theory of Data Curation" ICLR 2026 accepted"

Links: [{"title":"Why Less is More (Sometimes): A Theory of Data Curation | OpenReview","url":"https://openreview.net/forum?id=8KcjEygedc"},{"title":"A THEORY OF DATA CURATION","url":"https://openreview.net/pdf?id=8KcjEygedc"},{"title":"[2511.03492] Why Less is More (Sometimes): A Theory of Data Curation","url":"https://arxiv.org/abs/2511.03492"},{"title":"Why Less is More (Sometimes): A Theory of Data Curation","url":"https://arxiv.org/html/2511.03492"},{"title":"(PDF) Why Less is More (Sometimes): A Theory of Data Curation","url":"https://www.researchgate.net/publication/397321774_Why_Less_is_More_Sometimes_A_Theory_of_Data_Curation"}]

Based on the search results, I found the paper you're looking for:

"Why Less is More (Sometimes): A Theory of Data Curation" was submitted under review as a conference paper at ICLR 2026.

The paper addresses a fundamental question in machine learning: When is it better to use less data? This question has become critical as classical scaling laws suggesting "more is more" are challenged by methods like LIMO ("less is more") and s1, which achieve superior performance with small, aggressively curated datasets.

The key contributions include:

- Under certain conditions, small curated datasets can outperform full datasets, and the authors provide analytical conditions for this by deriving precise phase transition curves tied to data size and quality.

- The authors study data curation strategies where an imperfect oracle selects the training examples according to their difficulty and correctness, providing exact scaling law curves for test error under both label-agnostic and label-aware curation rules.

- The theoretical claims are validated with empirical results on ImageNet, confirming predictions about when curation improves accuracy and can even mitigate model collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85e2124b-e057-4ece-8eda-a14fda4f0886",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "9012e79d-fc60-4420-8c50-9d84c44a401f",
  "sourceToolAssistantUUID": "85e2124b-e057-4ece-8eda-a14fda4f0886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-13T10:14:47.816Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FVHtGRoDejNNxmsGzMpo53`</summary>

```json
{
  "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf",
  "prompt": "Extract the exact CoRL 2026 deadline dates. What are the abstract deadline and paper deadline?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9012e79d-fc60-4420-8c50-9d84c44a401f",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPha4W6iE8NdbfaaesJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79708c97-1c6b-49a3-bb6a-716067bba532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195tgd4ystoSECKXvzVZRMJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 17263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1347,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
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

_source line 39 · 2026-05-13T10:14:49.642Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SMwbY2J68t9oybWL9PS1wo`</summary>

```json
{
  "url": "https://openreview.net/forum?id=8KcjEygedc",
  "prompt": "What is the exact venue this paper is submitted to? Is it ICLR 2025 or ICLR 2026? Has it been accepted or is it still under review? Look for any decision tags, acceptance status, or venue information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79708c97-1c6b-49a3-bb6a-716067bba532",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPha4W6iE8NdbfaaesJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37011311-eb92-42fd-a05d-c72ceb94ccd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195tgd4ystoSECKXvzVZRMJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 17263,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1347
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 17263,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1347,
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

_source line 40 · 2026-05-13T10:14:50.145Z_

<details><summary>↩ Tool result · `toolu_01FVHtGRoDejNNxmsGzMpo53`</summary>

```text
# CoRL 2026 Deadline Dates

Based on the commit details, the exact deadline dates for CoRL 2026 are:

- **Abstract submission deadline**: May 26, 2026 at 11:59 UTC
- **Paper submission deadline**: May 29, 2026 at 11:59 UTC

## Additional Conference Details

- **Conference dates**: November 9-12, 2026
- **Venue**: JW Marriott Austin, 110 E 2nd St, Austin, TX 78701
- **Schedule breakdown**: 
  - Workshops: November 9
  - Main conference: November 10-12
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79708c97-1c6b-49a3-bb6a-716067bba532",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "6bdb7b61-87aa-4b70-b690-6a7921091347",
  "sourceToolAssistantUUID": "79708c97-1c6b-49a3-bb6a-716067bba532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-13T10:14:51.799Z_

<details><summary>↩ Tool result · `toolu_01SMwbY2J68t9oybWL9PS1wo`</summary>

```text
Based on the webpage content provided:

**Venue:** The paper is submitted to ICLR 2026, as indicated by the link "Go to **ICLR 2026 Conference** homepage" and the publication metadata stating "ICLR 2026 Poster."

**Acceptance Status:** The paper has been accepted. The document clearly identifies it as an "ICLR 2026 Poster," which denotes an accepted paper scheduled for poster presentation at the conference.

**Publication Details:** The paper was "Published: 26 Jan 2026" with a "Last Modified: 11 Apr 2026" timestamp, confirming it has moved beyond the review stage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37011311-eb92-42fd-a05d-c72ceb94ccd6",
  "isSidechain": true,
  "promptId": "c97cd0d7-6aa4-4145-a556-7af02cdfc3c0",
  "agentId": "abe2e982c5a0763f7",
  "type": "user",
  "uuid": "ae1ec5e8-14ba-4754-a698-0344f193717b",
  "sourceToolAssistantUUID": "37011311-eb92-42fd-a05d-c72ceb94ccd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-13T10:15:27.889Z_

Now I have all the information needed. Here is the comprehensive report:

---

## 1. SARM Paper (arXiv:2509.25358) -- ICLR 2026

**Acceptance status:** Confirmed accepted as a **poster** at ICLR 2026. Presented Sat, Apr 25, 2026 at Pavilion 3 P3-#1107.

**What is RA-BC?** Reward-Aligned Behavior Cloning is a method that uses **continuous ("soft") weighting**, not binary filtering. The mechanism has three steps:

1. **Progress Delta:** For each demonstration, compute `r_i = phi(o_i^{t+delta}) - phi(o_i^t)`, where phi is the reward model's progress score.
2. **Statistical Weighting:** Maintain running mean (mu) and std (sigma) of progress deltas, then compute: `w_tilde_i = clip((r_i - (mu - 2*sigma)) / (4*sigma + epsilon), 0, 1)`
3. **Prior Override:** Apply a threshold kappa: `w_i = 1{r_i > kappa} + 1{0 <= r_i <= kappa} * w_tilde_i`. Demonstrations with reward above kappa get full weight; those in [0, kappa] get the soft weight; those below 0 effectively get zero.

The weighted loss is: `L_RA-BC = sum(w_i * loss) / (sum(w_i) + epsilon)`

**Does RA-BC provide a decision rule for when to filter vs. reweight?** No. The paper does **not** provide any principled analysis or decision rule for when to filter versus when to reweight. It uses a unified continuous weighting scheme that subsumes both -- demonstrations are never hard-filtered, just soft-downweighted via the clipping mechanism. The threshold kappa = 0.01 was set empirically (described as the "top 5% of demonstrations") with minimal discussion of how to select it. So while the mechanism is relevant as a practical example of combined filtering+reweighting, it does not offer theoretical guidance on when one approach is preferable over the other.

---

## 2. CoRL 2026 Deadlines -- CONFIRMED

From the official CoRL 2026 website and the HuggingFace ai-deadlines tracker:

- **Abstract deadline:** May 26, 2026 at 11:59 UTC
- **Paper deadline:** May 29, 2026 at 11:59 UTC
- **Conference dates:** November 9-12, 2026 (workshops Nov 9, main conference Nov 10-12)
- **Venue:** JW Marriott Austin, TX
- **Camera-ready:** October 12, 2026

The user's stated deadlines (abstract May 26, paper May 29) are **correct**. Note: one source (an older Twitter/X post) mentioned May 25/May 28, but the authoritative sources confirm May 26/May 29.

---

## 3. ICRA 2027 Deadline -- NOT YET ANNOUNCED

ICRA 2027 will be held **May 24-28, 2027 in Seoul, South Korea**. However, the official website (2027.ieee-icra.org) states it is "under construction" as of May 2026. **No submission deadline has been announced yet.** For reference, ICRA 2026 had a September 15, 2025 deadline, so ICRA 2027's deadline would likely fall around September 2026, but this is speculative.

---

## 4. "Why Less is More (Sometimes): A Theory of Data Curation" (arXiv:2511.03492)

**IMPORTANT CORRECTION:** This paper was **not** accepted at ICLR 2025 as claimed. It was posted to arXiv on November 5, 2025 and was **accepted at ICLR 2026** as a poster (published Jan 26, 2026, last modified Apr 11, 2026 on OpenReview).

**Content relevance:** The paper provides a theoretical framework with **exact scaling law curves** for test error under both label-agnostic and label-aware curation rules. It derives **precise phase transition curves** tied to data size and quality that reveal when keeping only a subset of data improves generalization. Key results:

- Under certain conditions, small curated datasets provably outperform full datasets
- The framework provides analytical conditions for when data pruning helps
- Validated empirically on ImageNet
- Can explain contradictory curation strategies in LLM mathematical reasoning

However, the paper primarily addresses **filtering/pruning** (keeping vs. discarding data) rather than explicitly analyzing the **filtering vs. reweighting** trade-off. It does not directly compare these two approaches as alternatives. It is still highly relevant as theoretical grounding for why demonstration curation matters, but it would not directly answer "when should I filter vs. reweight."

---

Sources:
- [SARM on arXiv](https://arxiv.org/abs/2509.25358)
- [SARM ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10008682)
- [SARM on OpenReview](https://openreview.net/forum?id=aemqAxScl9)
- [CoRL 2026 Official Website](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 deadlines on HuggingFace ai-deadlines](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)
- [ICRA 2027 Official Website](https://2027.ieee-icra.org/contribute/)
- ["Why Less is More" on arXiv](https://arxiv.org/abs/2511.03492)
- ["Why Less is More" on OpenReview (ICLR 2026)](https://openreview.net/forum?id=8KcjEygedc)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae1ec5e8-14ba-4754-a698-0344f193717b",
  "isSidechain": true,
  "agentId": "abe2e982c5a0763f7",
  "requestId": "req_011CazPiUbcgsjxRqMBzFzkZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae44fb5b-1767-4346-9228-40badf206a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "20f4ab33-9097-4095-9841-a989ad0a1493",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L64hEyAYi4wMjoeCrf3gLT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 18610,
      "output_tokens": 1525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1525,
          "cache_read_input_tokens": 18610,
          "cache_creation_input_tokens": 624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 624,
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
