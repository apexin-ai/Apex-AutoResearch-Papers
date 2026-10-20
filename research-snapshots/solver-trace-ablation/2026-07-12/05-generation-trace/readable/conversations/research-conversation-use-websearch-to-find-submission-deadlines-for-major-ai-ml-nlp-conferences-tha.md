# Research conversation: Use WebSearch to find submission deadlines for major AI/ML/NLP conferences that have NOT yet passed as of 2026-05-11. Se

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a79feaebfb7103afb.jsonl`
- **Structured JSON:** [`d7ce7824f669398a8368.json`](../../sessions/d7/d7ce7824f669398a8368.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-11T20:39:49.338Z_

Use WebSearch to find submission deadlines for major AI/ML/NLP conferences that have NOT yet passed as of 2026-05-11. Search for:

1. "NeurIPS 2026 submission deadline"
2. "AAAI 2027 submission deadline"
3. "ICLR 2027 submission deadline"
4. "EMNLP 2026 submission deadline"
5. "ACL 2027 submission deadline"
6. "ICML 2026 submission deadline" (check if already passed)
7. "COLM 2026 submission deadline"
8. "NAACL 2027 submission deadline"
9. "CoNLL 2026 submission deadline"
10. "NeurIPS 2026 workshop submission deadline"

For each venue, report the exact deadline date if found, or your best estimate. Only include venues whose submission deadline is AFTER May 11, 2026. The paper would be ready in ~16 days from now (by end of May 2026), so realistically we need venues with deadlines in late May 2026 or later.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "5fe08b03-48c1-42fa-b707-88772e0df0a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T20:39:49.339Z_

```json
{
  "parentUuid": "5fe08b03-48c1-42fa-b707-88772e0df0a4",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
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
  "uuid": "982d0edb-4581-4e20-b740-b991764dd608",
  "timestamp": "2026-05-11T20:39:49.339Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T20:39:52.338Z_



I'll search for all these conference deadlines in parallel. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "982d0edb-4581-4e20-b740-b991764dd608",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRkkVs9rMsUpTNgTgue",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3c0de2e-9fe1-44cc-b4e2-dd7991e08a1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01415pWoVK3fKjpLmuacS3uT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 807,
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

_source line 4 · 2026-05-11T20:39:52.711Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JPTYMd9Tdm7FoAC4WgGtBL`</summary>

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
  "parentUuid": "d3c0de2e-9fe1-44cc-b4e2-dd7991e08a1a",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRkkVs9rMsUpTNgTgue",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b997e98-dd10-4540-9ba9-7cc52f9dc4b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01415pWoVK3fKjpLmuacS3uT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 8223,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 807
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 807,
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

_source line 5 · 2026-05-11T20:39:52.713Z_

<details><summary>↩ Tool result · `toolu_01JPTYMd9Tdm7FoAC4WgGtBL`</summary>

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
  "parentUuid": "3b997e98-dd10-4540-9ba9-7cc52f9dc4b4",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "1c15250b-2739-41c6-a8f7-235d67b44332",
  "sourceToolAssistantUUID": "3b997e98-dd10-4540-9ba9-7cc52f9dc4b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T20:39:54.997Z_



Now let me search for all the conference deadlines in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c15250b-2739-41c6-a8f7-235d67b44332",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRm16TF2ecf4fjCBxa9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6d50d3a-c27e-4c94-85b8-b259f7cdcd89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxSJ83E3eXgowQxRczFmvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1416,
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

_source line 7 · 2026-05-11T20:39:55.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WkHPfPp96kEj779b7WEG5E`</summary>

```json
{
  "query": "NeurIPS 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d50d3a-c27e-4c94-85b8-b259f7cdcd89",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRm16TF2ecf4fjCBxa9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecf87cc9-311a-4244-8457-def72107928a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxSJ83E3eXgowQxRczFmvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1416,
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

_source line 8 · 2026-05-11T20:39:55.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jy5bth4xC4b4c7yh1ghiBs`</summary>

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
  "parentUuid": "ecf87cc9-311a-4244-8457-def72107928a",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRm16TF2ecf4fjCBxa9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdb5b0ca-c496-4d00-b1b0-655bde9e978e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxSJ83E3eXgowQxRczFmvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1416,
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

_source line 9 · 2026-05-11T20:39:56.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLJtgZUjsaR7Vt66mqWfig`</summary>

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
  "parentUuid": "bdb5b0ca-c496-4d00-b1b0-655bde9e978e",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRm16TF2ecf4fjCBxa9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a0bd1e2-5b41-4331-afc1-1893feb6487d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxSJ83E3eXgowQxRczFmvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1416,
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

_source line 10 · 2026-05-11T20:39:56.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTmfjDwmG2z9XUo7cKoVYL`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a0bd1e2-5b41-4331-afc1-1893feb6487d",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRm16TF2ecf4fjCBxa9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62b4fa9f-65f7-4670-85e0-8d3d6d32a597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxSJ83E3eXgowQxRczFmvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1416,
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

_source line 11 · 2026-05-11T20:39:56.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5tqQbbk8foorciDCDgrds`</summary>

```json
{
  "query": "ACL 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62b4fa9f-65f7-4670-85e0-8d3d6d32a597",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRm16TF2ecf4fjCBxa9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e405ffe-a4de-4d9f-8071-7eaf19f96af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxSJ83E3eXgowQxRczFmvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1416,
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

### Tool result

_source line 12 · 2026-05-11T20:39:59.260Z_

<details><summary>↩ Tool result · `toolu_01WkHPfPp96kEj779b7WEG5E`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 Conference","url":"https://neurips.cc/Conferences/2026"},{"title":"NeurIPS Conference (@NeurIPSConf) / X","url":"https://x.com/NeurIPSConf"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"}]

Based on the search results, here are the submission deadlines for NeurIPS 2026:

**Abstract submission deadline: May 4, 2026 (AOE)**

**Full paper submission deadline (including all supplementary materials): May 6, 2026 AOE**

Note that the different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines.

The conference itself will be held December 6-12, 2026, and author notification is September 24, 2026 (AoE).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecf87cc9-311a-4244-8457-def72107928a",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "884d6461-7ee8-4a27-97d0-862711dde3d1",
  "sourceToolAssistantUUID": "ecf87cc9-311a-4244-8457-def72107928a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T20:39:59.574Z_

<details><summary>↩ Tool result · `toolu_01Jy5bth4xC4b4c7yh1ghiBs`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's what I found about the AAAI 2027 submission deadline:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027. However, the AAAI 2027 paper submission deadline is TBD (UTC-12).

According to available information, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns. The official deadline has not yet been announced, but it typically follows this timeline from previous years.

For the most current information, you can check the official AAAI call for papers at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdb5b0ca-c496-4d00-b1b0-655bde9e978e",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "2f2a6186-ba03-470b-b72a-b1b1ad985d3d",
  "sourceToolAssistantUUID": "bdb5b0ca-c496-4d00-b1b0-655bde9e978e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T20:39:59.630Z_

<details><summary>↩ Tool result · `toolu_01XLJtgZUjsaR7Vt66mqWfig`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"}]

Based on the search results, I was unable to find the specific submission deadline for ICLR 2027. The search results primarily contain information about ICLR 2026 (which has a deadline for paper submissions on Sept 24) and general information about the conference.

One result mentioned that deadlines are predicted based on historical patterns and should be verified on the official conference website, but no specific ICLR 2027 deadline was provided in these results.

For the most accurate and up-to-date ICLR 2027 submission deadline, I recommend checking the official ICLR website at iclr.cc, as the 2027 call for papers and timeline may not yet be fully announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a0bd1e2-5b41-4331-afc1-1893feb6487d",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "a359cab7-895b-4ba4-99c9-33a6ae1e6198",
  "sourceToolAssistantUUID": "3a0bd1e2-5b41-4331-afc1-1893feb6487d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T20:40:00.567Z_

<details><summary>↩ Tool result · `toolu_01B5tqQbbk8foorciDCDgrds`</summary>

```text
Web search results for query: "ACL 2027 submission deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Second Call for SemEval Task Proposals 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/second-call-semeval-task-proposals-2027"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"}]

Based on the search results, here is the information about ACL 2027 submission deadlines:

The ARR submission deadline for long and short papers for EACL 2027 is August 3, 2026. (Note: The conference mentioned here is EACL 2027, which is the European Chapter of the Association for Computational Linguistics, being held in Athens, Greece from March 9-14, 2027.)

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

If you're looking for information about the main ACL 2027 conference specifically (rather than EACL 2027), the search results indicate that ACL uses the ACL Rolling Review (ARR) submission system. The specific deadline for ACL 2027 itself was not found in these search results, but you can check the official ACL website or ARR website for the exact submission deadline for the main ACL conference in 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e405ffe-a4de-4d9f-8071-7eaf19f96af6",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "d785261d-065e-4dac-84f7-4d884d50287e",
  "sourceToolAssistantUUID": "0e405ffe-a4de-4d9f-8071-7eaf19f96af6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-11T20:40:01.042Z_

<details><summary>↩ Tool result · `toolu_01LTmfjDwmG2z9XUo7cKoVYL`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here is the information about EMNLP 2026 submission deadlines:

The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

Regarding the submission deadlines, the ARR submission deadline for long and short papers is May 25, 2026, and all authors must complete the author registration form by May 27, 2026.

Additional key deadlines include:
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 2026

Note that all main *ACL conferences use ARR (ACL Rolling Review) exclusively, so submissions must go through the ARR system rather than direct conference submission.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62b4fa9f-65f7-4670-85e0-8d3d6d32a597",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "b034c140-903a-46e6-9e3d-a89aa599156e",
  "sourceToolAssistantUUID": "62b4fa9f-65f7-4670-85e0-8d3d6d32a597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-11T20:40:03.332Z_

Now let me search for the remaining conferences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b034c140-903a-46e6-9e3d-a89aa599156e",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRmcVC3rp3LZTZqpsUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "637b712a-c3a0-4424-809d-18a7be0820fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136w5RMjbYrAkfEUSUyHZoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 18 · 2026-05-11T20:40:03.825Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017gpsvXtQMZjKRtEAPSzR6S`</summary>

```json
{
  "query": "ICML 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "637b712a-c3a0-4424-809d-18a7be0820fa",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRmcVC3rp3LZTZqpsUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78b685be-5854-4c47-818f-06f43f328c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136w5RMjbYrAkfEUSUyHZoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 19 · 2026-05-11T20:40:03.830Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CbNbipTUaQMoBtYZvBNAbe`</summary>

```json
{
  "query": "COLM 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b685be-5854-4c47-818f-06f43f328c33",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRmcVC3rp3LZTZqpsUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3246602d-f72e-42a6-a68c-91c4fc096880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136w5RMjbYrAkfEUSUyHZoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 20 · 2026-05-11T20:40:04.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011EhrBcL4z3af9oi6AhBQ9K`</summary>

```json
{
  "query": "NAACL 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3246602d-f72e-42a6-a68c-91c4fc096880",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRmcVC3rp3LZTZqpsUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e427ccd5-994c-4ea7-8570-ff96629fc1b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136w5RMjbYrAkfEUSUyHZoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 21 · 2026-05-11T20:40:04.776Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pp1hpTB4CVXFjL6cJcaq7r`</summary>

```json
{
  "query": "CoNLL 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e427ccd5-994c-4ea7-8570-ff96629fc1b2",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRmcVC3rp3LZTZqpsUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d0b8598-4892-457c-abfe-ad7a8592211c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136w5RMjbYrAkfEUSUyHZoy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 10446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 22 · 2026-05-11T20:40:05.074Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ufmgz5J4xGJodmwYQRmfRt`</summary>

```json
{
  "query": "NeurIPS 2026 workshop proposal submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d0b8598-4892-457c-abfe-ad7a8592211c",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRmcVC3rp3LZTZqpsUD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd432a58-20d1-4a72-862d-2e70f8f229db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136w5RMjbYrAkfEUSUyHZoy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 10446,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 733,
          "output_tokens": 246,
          "cache_read_input_tokens": 10446,
          "cache_creation_input_tokens": 2913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2913,
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

_source line 23 · 2026-05-11T20:40:06.905Z_

<details><summary>↩ Tool result · `toolu_017gpsvXtQMZjKRtEAPSzR6S`</summary>

```text
Web search results for query: "ICML 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICML 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FConference"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"Update ICML 2025 and 2026 conference data · huggingface/ai-deadlines at 55d2124","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/55d21240bacc3ac62397280592b3dd5ded9e5683"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"}]

Based on the search results, here is the information about the ICML 2026 submission deadline:

The ICML 2026 paper submissions deadline is January 28, 2026. Abstract and paper submission deadlines are strict, and in no circumstances will extensions be given.

For position papers specifically, there are separate deadlines: the abstract deadline is January 24, 2026, and the full paper submission deadline is January 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78b685be-5854-4c47-818f-06f43f328c33",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "13940af8-f2f8-443a-b29a-1985404689e1",
  "sourceToolAssistantUUID": "78b685be-5854-4c47-818f-06f43f328c33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-11T20:40:07.605Z_

<details><summary>↩ Tool result · `toolu_01CbNbipTUaQMoBtYZvBNAbe`</summary>

```text
Web search results for query: "COLM 2026 submission deadline"

Links: [{"title":"COLM 2026: Key Dates","url":"https://colmweb.org/dates.html"},{"title":"COLM 2026: Call for Papers","url":"https://colmweb.org/cfp.html"},{"title":"Conference on Language Modeling on X: \"COLM 2026 is just around the corner! Mark your calendars for: 💡Abstract deadline: Thursday, March 26, 2026 📄Full paper submission deadline: Tuesday, March 31, 2026 Call for papers in thread (website coming soon). https://t.co/YfjLxzCqxO\" / X","url":"https://x.com/COLM_conf/status/2000952051212415394"},{"title":"COLM 2026","url":"https://colmweb.org/"},{"title":"Conference on Language Modeling (COLM), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-colm.html"},{"title":"COLM 2026: Submission Instructions","url":"https://colmweb.org/submission-instructions.html"},{"title":"COLM 2026: Author Guide","url":"https://colmweb.org/AuthorGuide.html"},{"title":"When is COLM 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/colm"},{"title":"COLM 2026 Conference | OpenReview","url":"https://openreview.net/group?id=colmweb.org%2FCOLM%2F2026%2FConference"},{"title":"COLM 2026: Call for Workshops","url":"https://colmweb.org/cfw.html"}]

Based on the search results, here are the COLM 2026 submission deadlines:

**Abstract deadline: Thursday, March 26, 2026**
**Full paper submission deadline: Tuesday, March 31, 2026**

Additionally, the review release date is May 22, 2026, with a rebuttal deadline of June 8, 2026 and a final decision date of July 8, 2026.

For workshop submissions, the suggested submission deadline for workshop contributions is June 23, 2026.

COLM 2026 will take place at the Hilton Union Square in San Francisco, USA from October 6-9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3246602d-f72e-42a6-a68c-91c4fc096880",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "8627c56d-68aa-4ceb-9f8f-0149a0734de7",
  "sourceToolAssistantUUID": "3246602d-f72e-42a6-a68c-91c4fc096880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T20:40:08.404Z_

<details><summary>↩ Tool result · `toolu_01Pp1hpTB4CVXFjL6cJcaq7r`</summary>

```text
Web search results for query: "CoNLL 2026 submission deadline"

Links: [{"title":"CoNLL 2026 | CoNLL","url":"https://conll.org/"},{"title":"CoNLL 2026 : 30th Conference on Computational Natural Language Learning","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?copyownerid=90704&eventid=191131"},{"title":"CoNLL 2026: 3rd and Final Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/BDW4FPXENUKPTACOYMT5PXZSDZHJ5LB4/"},{"title":"CoNLL 2026 (@conll_conf) / Posts / X","url":"https://x.com/conll_conf"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CFP: Conference on Computational Natural Language Learning (CoNLL) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/conference-computational-natural-language-learning"},{"title":"CoNLL 2026: 2nd Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/ZGSJK533QG74LW5JVINWOQR3LXOX5ZFJ/"},{"title":"[Corpora-List] CoNLL 2026: 3rd and Final Call for Papers","url":"http://www.mail-archive.com/corpora@list.elra.info/msg05499.html"},{"title":"CoNLL 2026: 3rd and Final Call for Papers","url":"https://groups.google.com/g/cxgsnlp-workshop/c/HGgwxfDu1yM"},{"title":"ACL 2026 Workshop CoNLL | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2026%2FWorkshop%2FCoNLL"}]

Based on the search results, the submission deadline for CoNLL 2026 (both archival and non-archival) is February 19, 2026. All deadlines are set for 11:59pm UTC-12h (Anywhere on Earth time).

The conference timeline also includes:
- Notification of acceptance: April 21, 2026
- Camera-ready papers due: May 12, 2026
- Conference: July 3-4, 2026

CoNLL will accept only direct submissions this year via OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d0b8598-4892-457c-abfe-ad7a8592211c",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "11454244-e57c-409c-af83-a5ee880aa48c",
  "sourceToolAssistantUUID": "5d0b8598-4892-457c-abfe-ad7a8592211c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T20:40:08.661Z_

<details><summary>↩ Tool result · `toolu_011EhrBcL4z3af9oi6AhBQ9K`</summary>

```text
Web search results for query: "NAACL 2027 submission deadline"

Links: [{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_country&sort=desc"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"NAACL HLT 2027 (@naaclmeeting) / Posts / X","url":"https://x.com/naaclmeeting"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Links - Human Language Intelligence Lab","url":"https://hli.skku.edu/links"},{"title":"NAACL publications","url":"http://naacl.org/naacl-pubs/"}]

Based on the search results, here's what I found about NAACL 2027:

NAACL 2027 is scheduled for April 29 - May 4, 2027. However, the submission deadline is marked as TBA (to be announced), with a note that it's predicted based on the previous year's schedule and should be verified on the official conference website.

Since NAACL uses ACL Rolling Review (ARR) for submissions, the actual submission deadline would be determined by the ARR cycle schedule rather than a single conference-specific deadline.

For the most current and official information about the NAACL 2027 submission deadline, I'd recommend checking the official NAACL website or the ACL Rolling Review dates page, as the exact deadline has not yet been formally announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e427ccd5-994c-4ea7-8570-ff96629fc1b2",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "d14de15d-a6de-43eb-89e0-53b22aae0853",
  "sourceToolAssistantUUID": "e427ccd5-994c-4ea7-8570-ff96629fc1b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-11T20:40:09.256Z_

<details><summary>↩ Tool result · `toolu_01Ufmgz5J4xGJodmwYQRmfRt`</summary>

```text
Web search results for query: "NeurIPS 2026 workshop proposal submission deadline"

Links: [{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"Guidance for NeurIPS Workshop Proposals 2026","url":"https://neurips.cc/Conferences/2026/WorkshopsGuidance"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"2026 Conference","url":"https://neurips.cc/Conferences/2026"},{"title":"NeurIPS Newsletter – April 2026 – NeurIPS Blog","url":"https://blog.neurips.cc/2026/04/22/neurips-newsletter-april-2026/"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"}]

Based on the search results, here is the information about the NeurIPS 2026 workshop proposal submission deadline:

The workshop proposal submission deadline for NeurIPS 2026 is June 06, 2026, AoE (Anywhere on Earth). 

Additional key dates for workshop submissions include:
- Workshop Application Open: April 21, 2026, AoE
- Workshop Acceptance Notification: July 11, 2026, AoE

Proposals should be submitted through the OpenReview system, and opening a new Open Review account can take two weeks or more, so organizers should plan accordingly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd432a58-20d1-4a72-862d-2e70f8f229db",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "e38758f5-3023-48cc-aec7-f2c4abecff42",
  "sourceToolAssistantUUID": "fd432a58-20d1-4a72-862d-2e70f8f229db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-11T20:40:11.535Z_

Now let me search for a few more specifics to fill in gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e38758f5-3023-48cc-aec7-f2c4abecff42",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRnDc3zg1jjde6MqFBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66d7f274-361c-4275-a3ad-7138254fecb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsMtGA4xhgNPoXpuvH2e6J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4145,
      "cache_read_input_tokens": 13359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4145,
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

_source line 29 · 2026-05-11T20:40:12.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014j9Wp9Ke7FQxeerynkXzVk`</summary>

```json
{
  "query": "ACL Rolling Review June 2026 deadline ARR submission dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d7f274-361c-4275-a3ad-7138254fecb5",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRnDc3zg1jjde6MqFBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fadea05-75a2-4aa1-bc7a-755f02ea7d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsMtGA4xhgNPoXpuvH2e6J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4145,
      "cache_read_input_tokens": 13359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4145,
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

_source line 30 · 2026-05-11T20:40:12.942Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V24VWsg6DPS9sjrTnFhrcJ`</summary>

```json
{
  "query": "AAAI 2027 call for papers deadline August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fadea05-75a2-4aa1-bc7a-755f02ea7d02",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRnDc3zg1jjde6MqFBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1742ee59-f857-49d3-adfc-7ef9217b7bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsMtGA4xhgNPoXpuvH2e6J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4145,
      "cache_read_input_tokens": 13359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4145,
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

_source line 31 · 2026-05-11T20:40:13.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JPjw7hQPS4LRjv93AvXX53`</summary>

```json
{
  "query": "NeurIPS 2026 workshop paper submission deadline December 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1742ee59-f857-49d3-adfc-7ef9217b7bf1",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRnDc3zg1jjde6MqFBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ada61d0-f362-4a61-8f16-5e718c5c94f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsMtGA4xhgNPoXpuvH2e6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4145,
      "cache_read_input_tokens": 13359,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4145
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 13359,
          "cache_creation_input_tokens": 4145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4145,
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

_source line 32 · 2026-05-11T20:40:17.003Z_

<details><summary>↩ Tool result · `toolu_01V24VWsg6DPS9sjrTnFhrcJ`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline August 2026"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"MPC Deadlines Hub","url":"https://mpc-deadlines.github.io/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's what I found regarding AAAI 2027's call for papers deadline:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027.

Regarding the submission deadline for August 2026, the paper deadline for AAAI 2027 is August 1, 2026 at 23:59, with an abstract deadline of July 25. Additionally, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

So the official deadline appears to be August 1, 2026 for paper submissions, with an earlier abstract deadline of July 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1742ee59-f857-49d3-adfc-7ef9217b7bf1",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "455f38f3-7eaf-4a68-940b-3de0eeccbf3c",
  "sourceToolAssistantUUID": "1742ee59-f857-49d3-adfc-7ef9217b7bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-11T20:40:17.770Z_

<details><summary>↩ Tool result · `toolu_01JPjw7hQPS4LRjv93AvXX53`</summary>

```text
Web search results for query: "NeurIPS 2026 workshop paper submission deadline December 2026"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"Guidance for NeurIPS Workshop Proposals 2026","url":"https://neurips.cc/Conferences/2026/WorkshopsGuidance"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"2026 Conference","url":"https://neurips.cc/Conferences/2026"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"NeurIPS 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/neurips-2026.html"}]

Based on the search results, here are the key NeurIPS 2026 workshop-related deadlines:

**Workshop Proposal Deadlines:**
- Workshop Application Deadline: June 06, 2026, AoE
- Workshop Acceptance Notification: July 11, 2026, AoE

**Workshop Paper Submission:**
- Suggested Submission Date for Workshop Contributions: August 29, 2026, AoE

**Important Notification Deadline:**
- Mandatory Accept/Reject Notification Date: September 29, 2026, AoE

**Workshop Dates:**
- Workshop Date: December 11 and December 12, 2026 (Sydney). December 12 and December 13, 2026 (Paris, Atlanta)

Note: There is no December 2026 submission deadline for workshop papers. The suggested submission deadline for workshop contributions is August 29, 2026, with organizers required to notify authors of acceptance/rejection decisions by September 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ada61d0-f362-4a61-8f16-5e718c5c94f7",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "67061f12-56a3-4a22-ab5f-826db00ad6fd",
  "sourceToolAssistantUUID": "0ada61d0-f362-4a61-8f16-5e718c5c94f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-11T20:40:20.098Z_

<details><summary>↩ Tool result · `toolu_014j9Wp9Ke7FQxeerynkXzVk`</summary>

```text
Web search results for query: "ACL Rolling Review June 2026 deadline ARR submission dates"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) submission dates and deadlines for June 2026:

## Key Information

ARR switched to 10-week review cycles starting in May 2025, which represents a change from the previous schedule. Previously, from October 2022 to February 2025, ARR ran 8-week review cycles with submission deadlines on the 15th of every second month.

The search results provide information about the review cycle structure and general submission patterns, but they don't contain a specific table with the exact June 2026 submission deadline visible in the excerpts returned. However, based on the information that the submission deadline is always the 15th of the month, the June 2026 ARR submission deadline would likely be June 15, 2026, following this consistent pattern.

For the most current and detailed information about the June 2026 cycle specifics, I recommend visiting the official ARR dates page at aclrollingreview.org/dates, which maintains a complete table of all key dates for upcoming cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3fadea05-75a2-4aa1-bc7a-755f02ea7d02",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "a3679e97-f859-41f7-bcf7-06560b53c368",
  "sourceToolAssistantUUID": "3fadea05-75a2-4aa1-bc7a-755f02ea7d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-11T20:40:23.358Z_

Let me get one more piece of information about the ARR dates for EMNLP and NAACL commitments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3679e97-f859-41f7-bcf7-06560b53c368",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRo1xr3yHWLMv6sfngD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14c2c40e-d469-42df-89a1-1509a3a257f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLdGJZG9ftW7S9TSB7n24N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1393,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 17504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 886,
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

_source line 36 · 2026-05-11T20:40:23.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FuBPwFYZ7faFpw3oV5RWCy`</summary>

```json
{
  "query": "ARR submission deadlines 2026 schedule \"June 15\" OR \"August 15\" aclrollingreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14c2c40e-d469-42df-89a1-1509a3a257f2",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRo1xr3yHWLMv6sfngD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31fd808f-5494-4332-8dd5-9d328943d01e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLdGJZG9ftW7S9TSB7n24N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1393,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 17504,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1393,
          "output_tokens": 106,
          "cache_read_input_tokens": 17504,
          "cache_creation_input_tokens": 886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 886,
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

_source line 37 · 2026-05-11T20:40:30.429Z_

<details><summary>↩ Tool result · `toolu_01FuBPwFYZ7faFpw3oV5RWCy`</summary>

```text
Web search results for query: "ARR submission deadlines 2026 schedule "June 15" OR "August 15" aclrollingreview"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"}]

Based on the search results, I found information about ARR submission deadlines for 2026:

The submission deadline is always the 15th of the month for ACL Rolling Review cycles. While the search results mention that ARR ran 8-week review cycles with submission deadlines on the 15th of every second month from October 2022 to February 2025, the system switched to 10-week cycles starting in May 2025.

For 2026 specifically, the search results indicate that submissions can be made by 5/15 (May 15, 2026), and there are references to the May 2026 ARR cycle in the context of EMNLP 2026 submissions. However, the search results do not provide a complete detailed schedule showing all 2026 submission deadlines including specific June 15 or August 15 dates.

For the most current and complete 2026 ARR submission schedule, I recommend checking the official ARR dates page at aclrollingreview.org/dates, which the search results indicate contains the full table of upcoming cycle dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31fd808f-5494-4332-8dd5-9d328943d01e",
  "isSidechain": true,
  "promptId": "f39f4e6d-18af-47a8-a966-d1747e7597c9",
  "agentId": "a79feaebfb7103afb",
  "type": "user",
  "uuid": "502e1272-b87a-4925-a2fe-3de88d00512f",
  "sourceToolAssistantUUID": "31fd808f-5494-4332-8dd5-9d328943d01e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-11T20:41:00.019Z_

Here is a comprehensive summary of AI/ML/NLP conference deadlines that are still open as of May 11, 2026, organized by deadline date.

---

## Conferences with Deadlines AFTER May 11, 2026

### 1. EMNLP 2026 -- ARR Submission Deadline: May 25, 2026
- **Venue:** Budapest, Hungary (October 24-29, 2026)
- **ARR submission deadline (long & short papers):** May 25, 2026
- **Author registration form:** May 27, 2026
- **Commitment deadline:** August 2, 2026
- **Notification:** August 20, 2026
- **Status:** FEASIBLE if your paper is ready by end of May. This is the tightest viable option.
- Sources: [EMNLP 2026](https://2026.emnlp.org/), [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)

### 2. NeurIPS 2026 Workshop Proposals -- Deadline: June 6, 2026
- **This is for workshop proposals, not papers.** If you are organizing a workshop, proposals are due June 6, 2026 AoE. 
- **Workshop paper submissions** (to accepted workshops) have a suggested deadline of August 29, 2026.
- Sources: [NeurIPS 2026 Call for Workshops](https://neurips.cc/Conferences/2026/CallForWorkshops), [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)

### 3. AAAI 2027 -- Abstract: ~July 25, 2026 | Paper: ~August 1, 2026
- **Venue:** Montreal, Quebec, Canada (February 16-23, 2027)
- **Abstract deadline:** July 25, 2026
- **Full paper submission deadline:** August 1, 2026
- **Status:** VERY FEASIBLE. Plenty of time to polish your paper.
- Sources: [AAAI Conference](https://aaai.org/conference/aaai/), [AI Conference Deadlines](https://trybibby.com/conference-deadlines)

### 4. EACL 2027 (via ARR) -- ARR Submission: August 3, 2026
- **Venue:** Athens, Greece (March 9-14, 2027)
- **ARR submission deadline:** August 3, 2026
- **Status:** VERY FEASIBLE.
- Sources: [EACL 2027](https://2027.eacl.org/), [ARR Dates](http://aclrollingreview.org/dates)

### 5. NeurIPS 2026 Workshop Papers -- Suggested Submission: August 29, 2026
- **Workshop dates:** December 11-13, 2026 (Sydney / Paris / Atlanta)
- **Suggested submission deadline for workshop contributions:** August 29, 2026
- **Mandatory notification deadline:** September 29, 2026
- **Status:** VERY FEASIBLE. Individual workshops set their own exact deadlines, but organizers are guided by the August 29 suggestion.
- Sources: [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates), [NeurIPS 2026 Workshops Guidance](https://neurips.cc/Conferences/2026/WorkshopsGuidance)

### 6. NAACL 2027 -- Deadline TBA (estimated late 2026 via ARR)
- **Venue:** TBA (April 29 - May 4, 2027)
- **Submission deadline:** Not yet announced. Based on historical patterns and the ARR cycle, the relevant ARR submission deadline will likely be in October-November 2026.
- **Status:** VERY FEASIBLE once announced.
- Sources: [NAACL](https://naacl.org/), [ARR Dates](http://aclrollingreview.org/dates)

### 7. ICLR 2027 -- Deadline TBA (estimated September-October 2026)
- **Deadline not yet announced.** Based on ICLR 2026's deadline of ~September 2025, ICLR 2027's submission deadline is expected around September-October 2026.
- **Status:** VERY FEASIBLE once announced.
- Sources: [ICLR](https://iclr.cc/), [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)

### 8. ACL 2027 -- Deadline TBA (via ARR, estimated late 2026)
- The main ACL 2027 deadline has not been announced. ACL uses ARR exclusively, and relevant ARR cycles will likely be in late 2026 or early 2027.
- **Status:** VERY FEASIBLE once announced.
- Sources: [ARR Dates](http://aclrollingreview.org/dates), [ACL 2026 for reference](https://2026.aclweb.org/)

---

## Conferences Whose Deadlines Have ALREADY PASSED (before May 11, 2026)

| Conference | Deadline | Status |
|---|---|---|
| **NeurIPS 2026** (main) | Abstract: May 4; Paper: May 6, 2026 | PASSED (just missed by ~5 days) |
| **ICML 2026** | January 28, 2026 | PASSED |
| **COLM 2026** | Abstract: March 26; Paper: March 31, 2026 | PASSED |
| **CoNLL 2026** | February 19, 2026 | PASSED |

---

## Recommended Strategy (paper ready by ~May 27, 2026)

1. **Immediate target: EMNLP 2026** (May 25 ARR deadline) -- This is tight but doable if you submit to ARR by May 25. This is a top NLP venue.

2. **Strong backup: AAAI 2027** (August 1) -- Gives you ample time. Top-tier AI conference.

3. **Also consider: EACL 2027** (August 3 ARR deadline) -- Good venue, similar timeline to AAAI.

4. **NeurIPS 2026 workshops** (~August 29) -- If the work fits a specific workshop topic, this is a good option at a premier venue.

5. **Later options: ICLR 2027, NAACL 2027, ACL 2027** -- All expected to have deadlines in September 2026 or later, giving you maximum time to refine the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "502e1272-b87a-4925-a2fe-3de88d00512f",
  "isSidechain": true,
  "agentId": "a79feaebfb7103afb",
  "requestId": "req_011CawRonbTQXkXgHERTxRii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "250302a5-6b53-483e-8b51-fa33982c4cd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "94942838-916b-492e-8ca9-992de02afd76",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPpJtg5521PZ7bYbYoY9Ub",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2202,
      "cache_read_input_tokens": 18390,
      "output_tokens": 1657,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2202
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1657,
          "cache_read_input_tokens": 18390,
          "cache_creation_input_tokens": 2202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2202,
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
