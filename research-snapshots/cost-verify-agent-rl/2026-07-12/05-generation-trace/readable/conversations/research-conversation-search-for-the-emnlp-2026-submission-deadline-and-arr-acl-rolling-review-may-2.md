# Research conversation: Search for the EMNLP 2026 submission deadline and ARR (ACL Rolling Review) May 2026 deadline. I need to know: 1. When is

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a66aace5943798990.jsonl`
- **Structured JSON:** [`943983556a2105eab1cb.json`](../../sessions/94/943983556a2105eab1cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-10T19:53:40.297Z_

Search for the EMNLP 2026 submission deadline and ARR (ACL Rolling Review) May 2026 deadline. I need to know:
1. When is the ARR May 2026 submission deadline exactly?
2. When is the EMNLP 2026 conference?
3. What is the commitment deadline for EMNLP 2026?
4. Is there an ARR June 2026 cycle that could also target EMNLP 2026?

Also search for AAAI 2027 deadline for comparison.

Use WebSearch to find this information. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "c0e6d42c-de29-4316-954e-774f19789d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:53:40.303Z_

```json
{
  "parentUuid": "c0e6d42c-de29-4316-954e-774f19789d97",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
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
  "uuid": "1fcecadd-2d62-4a37-bd38-2a710f935fba",
  "timestamp": "2026-05-10T19:53:40.303Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:53:43.235Z_



I'll search for all of these deadlines in parallel. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fcecadd-2d62-4a37-bd38-2a710f935fba",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauURiXcb1bHyxZixCUdw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a15fee1-e0f9-41b7-a1ed-92d6d0941542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3skqDubjLssdFzaoKc5NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8914,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8914,
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

_source line 4 · 2026-05-10T19:53:43.709Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LZ3nkVvqJ6483bJz315MyH`</summary>

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
  "parentUuid": "0a15fee1-e0f9-41b7-a1ed-92d6d0941542",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauURiXcb1bHyxZixCUdw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0955f702-68ab-4bff-b760-201c324096f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3skqDubjLssdFzaoKc5NC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8914,
      "cache_read_input_tokens": 0,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8914
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8914,
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

_source line 5 · 2026-05-10T19:53:43.715Z_

<details><summary>↩ Tool result · `toolu_01LZ3nkVvqJ6483bJz315MyH`</summary>

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
  "parentUuid": "0955f702-68ab-4bff-b760-201c324096f5",
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "0580545a-2b96-4aef-8ead-50291f6d5918",
  "sourceToolAssistantUUID": "0955f702-68ab-4bff-b760-201c324096f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:53:46.703Z_



Now let me search for all the deadlines in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0580545a-2b96-4aef-8ead-50291f6d5918",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauURyWmD1NbrmqFiRE5e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fde4880f-ed79-480a-90a3-3df034a6fff2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe9sVazgfP6sDCcJQNaPyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8914,
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

_source line 7 · 2026-05-10T19:53:47.542Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NSR8s7X4nj5HLS3U4C8vwB`</summary>

```json
{
  "query": "ARR ACL Rolling Review May 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fde4880f-ed79-480a-90a3-3df034a6fff2",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauURyWmD1NbrmqFiRE5e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b690daec-9aa2-4f63-9036-1554ded784c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe9sVazgfP6sDCcJQNaPyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8914,
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

_source line 8 · 2026-05-10T19:53:47.795Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014FDrfw9vdNBpZBi1mZMx5z`</summary>

```json
{
  "query": "EMNLP 2026 conference dates submission deadline commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b690daec-9aa2-4f63-9036-1554ded784c6",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauURyWmD1NbrmqFiRE5e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff60f544-971d-4dcb-9d2c-43ded003e445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe9sVazgfP6sDCcJQNaPyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8914,
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

_source line 9 · 2026-05-10T19:53:48.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018CGsE8wnNWr7rXg3XeVG7h`</summary>

```json
{
  "query": "AAAI 2027 paper submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff60f544-971d-4dcb-9d2c-43ded003e445",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauURyWmD1NbrmqFiRE5e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28a046c2-dc77-4c27-9479-d1a80337e990",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe9sVazgfP6sDCcJQNaPyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8914,
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

_source line 10 · 2026-05-10T19:53:48.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VvFwWZPaTie2ettpcDmYAa`</summary>

```json
{
  "query": "ARR June 2026 cycle deadline EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28a046c2-dc77-4c27-9479-d1a80337e990",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauURyWmD1NbrmqFiRE5e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4365f03d-7d08-4501-9ec1-49419175b0e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qe9sVazgfP6sDCcJQNaPyy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8914,
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

_source line 11 · 2026-05-10T19:53:51.449Z_

<details><summary>↩ Tool result · `toolu_01NSR8s7X4nj5HLS3U4C8vwB`</summary>

```text
Web search results for query: "ARR ACL Rolling Review May 2026 submission deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results, here's the information about the ARR ACL Rolling Review May 2026 submission deadline:

The submission deadline is always the 15th of the month, which means the May 2026 ARR submission deadline would be **May 15, 2026**.

ARR switched to 10-week review cycles starting in May 2025, so the May 2026 cycle follows this pattern. The May 15th deadline aligns with the standard ARR submission schedule under the new 10-week cycle format.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b690daec-9aa2-4f63-9036-1554ded784c6",
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "e7bec42b-b634-42ea-92ac-bf69243d2cc0",
  "sourceToolAssistantUUID": "b690daec-9aa2-4f63-9036-1554ded784c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:53:53.179Z_

<details><summary>↩ Tool result · `toolu_018CGsE8wnNWr7rXg3XeVG7h`</summary>

```text
Web search results for query: "AAAI 2027 paper submission deadline"

Links: [{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"}]

Based on the search results, here's what I found about the AAAI 2027 paper submission deadline:

The AAAI 2027 paper submission deadline is TBD (UTC-12). AAAI 2027 is being held in Montréal, Québec, Canada on February 16-23, 2027.

However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

For the official and most current information, the official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28a046c2-dc77-4c27-9479-d1a80337e990",
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "e085d7eb-8954-4d4a-953a-1bc8d75bb036",
  "sourceToolAssistantUUID": "28a046c2-dc77-4c27-9479-d1a80337e990",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:53:53.775Z_

<details><summary>↩ Tool result · `toolu_01VvFwWZPaTie2ettpcDmYAa`</summary>

```text
Web search results for query: "ARR June 2026 cycle deadline EMNLP 2026"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"The First Call for Industry Track Papers for EMNLP 2026 is officially out! Are you deploying NLP in real-world applications? Share your insights, challenges, and deployed systems with the community. 🗓️ Deadline: June 16, 2026 🔗 Link: https://t.co/ga3k6CJcm0 #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2048750521696072166"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is the information about the ARR June 2026 cycle deadline for EMNLP 2026:

The ARR Submission Deadline for EMNLP 2026 is May 25, 2026. This is actually the May 2026 cycle deadline, not a June cycle deadline.

Additional important dates include: Reviewer registration deadline for ALL authors on May 27, 2026, Author response and author-reviewer discussion from July 7 - July 13, 2026, and Meta review release on July 30, 2026.

The EMNLP commitment deadline is August 2, 2026.

It's worth noting that for the ARR 2026 May cycle aligned with EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4365f03d-7d08-4501-9ec1-49419175b0e3",
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "8988f5f5-91ca-434a-8760-3b3a894e6526",
  "sourceToolAssistantUUID": "4365f03d-7d08-4501-9ec1-49419175b0e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:53:55.211Z_

<details><summary>↩ Tool result · `toolu_014FDrfw9vdNBpZBi1mZMx5z`</summary>

```text
Web search results for query: "EMNLP 2026 conference dates submission deadline commitment deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP (@emnlpmeeting.bsky.social) — Bluesky","url":"https://bsky.app/profile/emnlpmeeting.bsky.social"}]

Here are the key dates and information for EMNLP 2026:

**Conference Dates:**
EMNLP 2026 will be held in Budapest, Hungary from October 24th to October 29th, 2026.

**Submission and Important Deadlines:**
ARR submission deadline (long & short papers) is May 25, 2026. The reviewer registration deadline for ALL authors is May 27, 2026. Author response and author-reviewer discussion runs July 7 - July 13, 2026. Meta review is released July 30, 2026. The EMNLP commitment deadline is August 2, 2026. Notification of acceptance (long & short papers) is August 20, 2026. Camera-ready papers are due September 20, 2026.

**Review Process:**
EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system. Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors. Authors then commit their reviewed articles to EMNLP 2026, where Senior Area Chairs and Program Chairs make acceptance decisions from the ARR reviews and meta-reviews.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff60f544-971d-4dcb-9d2c-43ded003e445",
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "a8a6ce8b-048d-4caa-a787-27eec98a3d41",
  "sourceToolAssistantUUID": "ff60f544-971d-4dcb-9d2c-43ded003e445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T19:53:57.631Z_

Let me get more details on the ARR dates page and check whether a June cycle exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8a6ce8b-048d-4caa-a787-27eec98a3d41",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauUSpFgGEQ4J3i6Gd1Q8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36b8ba6b-2311-4cae-a5aa-9f57931e8960",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nwq5ZV39kRkygViJuV3gyE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1599,
      "cache_creation_input_tokens": 1654,
      "cache_read_input_tokens": 10330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1654,
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

_source line 16 · 2026-05-10T19:53:58.640Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016FeKHYEuDGM8QLXEuhjW3V`</summary>

```json
{
  "query": "site:aclrollingreview.org dates 2026 submission cycles May June July"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36b8ba6b-2311-4cae-a5aa-9f57931e8960",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauUSpFgGEQ4J3i6Gd1Q8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d4f76dd-0a43-4576-87fe-4abb3c972be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nwq5ZV39kRkygViJuV3gyE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1599,
      "cache_creation_input_tokens": 1654,
      "cache_read_input_tokens": 10330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1654,
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

_source line 17 · 2026-05-10T19:53:59.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ryrf8oPtM7q9TzJyKC2xwW`</summary>

```json
{
  "query": "EMNLP 2026 call for papers \"May 25\" OR \"June 15\" ARR cycle commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d4f76dd-0a43-4576-87fe-4abb3c972be4",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauUSpFgGEQ4J3i6Gd1Q8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2434e249-c371-4129-8a86-dfc4d2ac52b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nwq5ZV39kRkygViJuV3gyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1599,
      "cache_creation_input_tokens": 1654,
      "cache_read_input_tokens": 10330,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1654
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1599,
          "output_tokens": 152,
          "cache_read_input_tokens": 10330,
          "cache_creation_input_tokens": 1654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1654,
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

_source line 18 · 2026-05-10T19:54:03.640Z_

<details><summary>↩ Tool result · `toolu_016FeKHYEuDGM8QLXEuhjW3V`</summary>

```text
Web search results for query: "site:aclrollingreview.org dates 2026 submission cycles May June July"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"}]

Based on the search results, I found information about ACL Rolling Review (ARR) submission cycles and dates. However, the search results don't contain a specific detailed table with all the May, June, and July 2026 submission cycle dates from the aclrollingreview.org/dates page itself.

What I can tell you from the results:

ARR switched to 10-week review cycles starting in May 2025, and the submission deadline is always the 15th of the month; other dates vary due to the length of months, timing of weekends, etc.

The search results reference that a table lists all the key dates, by which the authors may need to take action, for the upcoming cycles, but the specific detailed dates for May, June, and July 2026 cycles are not fully displayed in the search results I retrieved.

To get the complete submission cycle dates for May, June, and July 2026, you may want to visit the dates page directly at aclrollingreview.org/dates, which appears to contain the full schedule table.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d4f76dd-0a43-4576-87fe-4abb3c972be4",
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "327cff72-be04-42df-8d19-2a4419071cab",
  "sourceToolAssistantUUID": "1d4f76dd-0a43-4576-87fe-4abb3c972be4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T19:54:05.593Z_

<details><summary>↩ Tool result · `toolu_01Ryrf8oPtM7q9TzJyKC2xwW`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers "May 25" OR "June 15" ARR cycle commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results for EMNLP 2026 call for papers with ARR cycle commitment:

## Key Deadline: May 25, 2026

Papers must be submitted, at latest, by the ARR 2026 May cycle, with the ARR submission deadline for long and short papers being May 25, 2026.

## ARR Cycle Commitment Process

Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link. The EMNLP commitment deadline is August 2, 2026.

## Important Policy Update

There is a critical requirement for the May cycle: Authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026—ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026. This is because the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL).

The search results do not show a June 15 deadline in relation to EMNLP 2026 main conference submissions—May 25, 2026 is the primary ARR submission deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2434e249-c371-4129-8a86-dfc4d2ac52b2",
  "isSidechain": true,
  "promptId": "93faedec-a603-4f7a-8e77-8b5b5bc04770",
  "agentId": "a66aace5943798990",
  "type": "user",
  "uuid": "8d3a81ee-aee5-40a0-bfc6-0b253cd3d0e0",
  "sourceToolAssistantUUID": "2434e249-c371-4129-8a86-dfc4d2ac52b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T19:54:26.259Z_

Here are the findings:

---

**1. ARR May 2026 Submission Deadline**

The ARR May 2026 submission deadline is **May 25, 2026**. The reviewer registration deadline for all authors is May 27, 2026 (two days after submission). Note that ARR switched to 10-week review cycles starting in May 2025.

Critical policy note: Since the ARR May 2026 cycle is shared between EMNLP 2026 and AACL, authors must **explicitly declare their target conference at submission time**, and this choice is **binding**. Submissions that do not select EMNLP 2026 during the May cycle will not be able to commit to EMNLP 2026 later.

**2. EMNLP 2026 Conference Dates**

EMNLP 2026 will be held in **Budapest, Hungary, October 24--29, 2026**.

**3. EMNLP 2026 Commitment Deadline**

- Author response / author-reviewer discussion: July 7--13, 2026
- Meta-review release: July 30, 2026
- **Commitment deadline: August 2, 2026**
- Notification of acceptance: August 20, 2026
- Camera-ready deadline: September 20, 2026

Papers from the May 2026 ARR cycle or any earlier ARR cycle (with completed reviews and meta-review) may be committed to EMNLP 2026 by August 2.

**4. ARR June 2026 Cycle for EMNLP 2026?**

Based on the search results, **no**. The EMNLP 2026 call for papers states that papers must be submitted "at latest" by the ARR May 2026 cycle (May 25 deadline). There is no indication that a June 2026 ARR cycle would be eligible for EMNLP 2026 commitment. The timeline would not work: with 10-week review cycles, a June 15 submission would not receive reviews and meta-reviews before the August 2 commitment deadline. The May cycle is the last eligible cycle.

**5. AAAI 2027 (for comparison)**

- **Conference dates: February 16--23, 2027** in Montreal, Quebec, Canada
- **Submission deadline: TBD** (not yet announced). Based on historical patterns (AAAI-26 had an August 2025 deadline), the AAAI 2027 submission deadline is expected around **July--August 2026**.

---

**Summary timeline for your planning (as of May 10, 2026):**

| Event | Date |
|---|---|
| ARR May 2026 submission (last cycle for EMNLP) | May 25, 2026 (15 days from now) |
| EMNLP 2026 commitment deadline | August 2, 2026 |
| AAAI 2027 submission (estimated) | ~July/August 2026 |
| EMNLP 2026 conference | October 24--29, 2026 |
| AAAI 2027 conference | February 16--23, 2027 |

Sources:
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 Main Site](https://2026.emnlp.org/)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 binding target declaration (Twitter/X)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [AAAI 2027 Deadline Tracker](https://www.getpaperpilot.com/deadlines/aaai-2027.html)
- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)
- [ARR Call for Papers](http://aclrollingreview.org/cfp)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d3a81ee-aee5-40a0-bfc6-0b253cd3d0e0",
  "isSidechain": true,
  "agentId": "a66aace5943798990",
  "requestId": "req_011CauUTaeeWw39QQDziA5XM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57ade974-087e-4fdd-a4ba-6de9ff48c1ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b5980262-a929-4d12-a61d-d810e3f30f10",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWjU3apFtaZmjEWUk7Yt3w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3536,
      "cache_read_input_tokens": 11984,
      "output_tokens": 994,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3536
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 994,
          "cache_read_input_tokens": 11984,
          "cache_creation_input_tokens": 3536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3536,
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
