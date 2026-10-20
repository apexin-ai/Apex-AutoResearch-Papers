# Research conversation: Use WebSearch to verify these venue deadlines: 1. AAAI 2027 - Is the abstract deadline July 21, 2026 and full papers Jul

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a27a328a6c270c784.jsonl`
- **Structured JSON:** [`9cd0d46b146daacb90d0.json`](../../sessions/9c/9cd0d46b146daacb90d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-17T09:19:59.231Z_

Use WebSearch to verify these venue deadlines:

1. AAAI 2027 - Is the abstract deadline July 21, 2026 and full papers July 28, 2026? Search "AAAI 2027 call for papers deadline" or "AAAI-27 deadline"
2. ARR August 2026 cycle - Is the submission deadline August 3, 2026? Search "ARR August 2026 deadline" or "ACL Rolling Review 2026 schedule"
3. EACL 2027 - Is the commitment deadline October 11, 2026? Search "EACL 2027 commitment deadline"
4. EMNLP 2026 ARR May cycle - Was the deadline May 25, 2026? Search "ARR May 2026 deadline"

Also search for: "Qwen3-Coder-Next" and "Qwen3.5 gated attention" to verify deployment claims.

Report exactly what you find with sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "5a5bf91b-b005-4a8e-9dae-527c12b1ac76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T09:19:59.233Z_

```json
{
  "parentUuid": "5a5bf91b-b005-4a8e-9dae-527c12b1ac76",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
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
  "uuid": "04c8694d-064e-45e1-b2e9-e5e297f49d66",
  "timestamp": "2026-05-17T09:19:59.233Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T09:20:02.234Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015ujP1DCn7n3cbLuRRBRviJ`</summary>

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
  "parentUuid": "04c8694d-064e-45e1-b2e9-e5e297f49d66",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tmS82bU2BM3xs7hGdn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33d3bb54-a43c-4efb-bdff-fbbf9fb7d1b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016EvxagH6Vt9QFniK1MYUAV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 8223,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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

_source line 4 · 2026-05-17T09:20:02.244Z_

<details><summary>↩ Tool result · `toolu_015ujP1DCn7n3cbLuRRBRviJ`</summary>

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
  "parentUuid": "33d3bb54-a43c-4efb-bdff-fbbf9fb7d1b3",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "94e0a6ee-f481-4277-b687-2a544979814e",
  "sourceToolAssistantUUID": "33d3bb54-a43c-4efb-bdff-fbbf9fb7d1b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T09:20:04.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EbdWfc6eGZvBSQTG8HNXYw`</summary>

```json
{
  "query": "AAAI 2027 call for papers deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94e0a6ee-f481-4277-b687-2a544979814e",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tmf9cF6cQacDJqSq39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a9b3288-c27e-49e7-87fd-718d1d2f0caf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLmgUdVQ97uFX6m1y4od4J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 6 · 2026-05-17T09:20:05.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhUNEFTurc8WAfB1UdRurz`</summary>

```json
{
  "query": "ARR August 2026 deadline ACL Rolling Review 2026 schedule"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a9b3288-c27e-49e7-87fd-718d1d2f0caf",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tmf9cF6cQacDJqSq39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ec7c8f6-5aae-4106-8e32-3f1e2300cc3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLmgUdVQ97uFX6m1y4od4J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 7 · 2026-05-17T09:20:05.658Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015kj3GFBaPFyqJugvtGikY2`</summary>

```json
{
  "query": "EACL 2027 commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec7c8f6-5aae-4106-8e32-3f1e2300cc3f",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tmf9cF6cQacDJqSq39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52da5402-cb43-4711-bfb5-6aea1fcd406a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLmgUdVQ97uFX6m1y4od4J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 8 · 2026-05-17T09:20:06.086Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LuGnYXZCi53R3XmvGSBt3g`</summary>

```json
{
  "query": "ARR May 2026 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52da5402-cb43-4711-bfb5-6aea1fcd406a",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tmf9cF6cQacDJqSq39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcef7093-012e-494c-972d-65d0c6a539eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLmgUdVQ97uFX6m1y4od4J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 9 · 2026-05-17T09:20:06.485Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XyDuSA3wRSSzxcanstizED`</summary>

```json
{
  "query": "Qwen3-Coder-Next"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcef7093-012e-494c-972d-65d0c6a539eb",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tmf9cF6cQacDJqSq39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e023241-ccc3-4ec6-8276-d04b04857540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLmgUdVQ97uFX6m1y4od4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9007,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 289,
          "cache_read_input_tokens": 9007,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 10 · 2026-05-17T09:20:06.489Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UT794snkYJyM3vC8ktG9o2`</summary>

```json
{
  "query": "Qwen3.5 gated attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e023241-ccc3-4ec6-8276-d04b04857540",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tmf9cF6cQacDJqSq39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77c928d1-c155-4ddd-88be-0823278d7e06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLmgUdVQ97uFX6m1y4od4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 9007,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 289,
          "cache_read_input_tokens": 9007,
          "cache_creation_input_tokens": 1392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1392,
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

_source line 11 · 2026-05-17T09:20:08.044Z_

<details><summary>↩ Tool result · `toolu_01EbdWfc6eGZvBSQTG8HNXYw`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"}]

Based on the search results, here is the information about AAAI 2027 call for papers deadlines:

The paper submission deadline for AAAI 2027 is July 28, 2026 at 11:59 PM UTC-12, with abstracts due on July 21, 2026 at 11:59 PM UTC-12. Supplementary material and code must be submitted by July 31, 2026 at 11:59 PM UTC-12.

The conference will be held in Montréal, Québec, Canada from February 16-23, 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a9b3288-c27e-49e7-87fd-718d1d2f0caf",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "776ffc99-df70-4cde-8f74-d89e3ccb8d8d",
  "sourceToolAssistantUUID": "1a9b3288-c27e-49e7-87fd-718d1d2f0caf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T09:20:09.930Z_

<details><summary>↩ Tool result · `toolu_01LuGnYXZCi53R3XmvGSBt3g`</summary>

```text
Web search results for query: "ARR May 2026 deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=arr2601"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"AACL 2026 on X: \"🚨AACL-IJCNLP 2026 will be held in Hengqin, China from November 6-10, 2026. The CFP is now out! ARR submission deadline (long &amp; short papers): May 25, 2026! #NLProc #NLP Dates and full CFP here: https://t.co/4ON2H5M7zQ @aadi_joshi @kta84912 https://t.co/9ZKWmY7Jvv\" / X","url":"https://x.com/aaclmeeting/status/2041832211599733075"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"}]

Based on the search results, the ARR (ACL Rolling Review) submission deadline for May 2026 is May 25, 2026. 

For the ARR 2026 May cycle, which is aligned with both EMNLP and AACL, authors need to explicitly declare which conference they intend to commit to at submission time, and this choice is binding.

After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcef7093-012e-494c-972d-65d0c6a539eb",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "33ffa132-fa94-4122-bfa7-559eab56c8b9",
  "sourceToolAssistantUUID": "fcef7093-012e-494c-972d-65d0c6a539eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T09:20:11.456Z_

<details><summary>↩ Tool result · `toolu_01AhUNEFTurc8WAfB1UdRurz`</summary>

```text
Web search results for query: "ARR August 2026 deadline ACL Rolling Review 2026 schedule"

Links: [{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"}]

Based on the search results, here's the information about the ARR (ACL Rolling Review) August 2026 deadline and the 2026 schedule:

## August 2026 Commitment Deadlines

EMNLP 2026 has an August 2, 2026 commitment date, and AACL 2026 has an August 26, 2026 commitment date. These dates indicate when authors must commit their reviewed papers to these respective venues.

## 2026 ACL Rolling Review Schedule

The ACL Peer Review Committee recommended switching from 8-week to 10-week review cycles, with the new schedule starting in May 2025. This means there are generally 5 cycles per year instead of 6, with more reasonable timelines for review tasks and author response.

For specific upcoming cycles, the final ARR submission date for EACL 2027 is August 3, 2026, with an October 11, 2026 commitment date.

The search results show that the submission deadline for ACL 2026 papers to ARR is January 5, 2026, with subsequent review deadlines and opportunities to commit papers to various venues throughout the year.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ec7c8f6-5aae-4106-8e32-3f1e2300cc3f",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "78d996eb-8390-4b4f-985f-05909554e6f8",
  "sourceToolAssistantUUID": "2ec7c8f6-5aae-4106-8e32-3f1e2300cc3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T09:20:13.236Z_

<details><summary>↩ Tool result · `toolu_01UT794snkYJyM3vC8ktG9o2`</summary>

```text
Web search results for query: "Qwen3.5 gated attention"

Links: [{"title":"Qwen3.5: Nobody Agrees on Attention Anymore","url":"https://huggingface.co/blog/mlabonne/qwen35"},{"title":"Qwen3.5: Nobody Agrees on Attention Anymore | by Maxime Labonne | Medium","url":"https://medium.com/@mlabonne/qwen3-5-nobody-agrees-on-attention-anymore-4709e1bd014b"},{"title":"Gated Attention | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llm-architecture-gallery/gated-attention/"},{"title":"A Visual Guide to Attention Variants in Modern LLMs","url":"https://magazine.sebastianraschka.com/p/visual-attention-variants"},{"title":"QwQZh/gated_attention · Hugging Face","url":"https://huggingface.co/QwQZh/gated_attention"},{"title":"Fine-Tune Qwen3.5-VL — NeMo-AutoModel","url":"https://docs.nvidia.com/nemo/automodel/nightly/guides/vlm/qwen3_5.html"},{"title":"Qwen 3.5 Explained: Architecture, Upgrades Over Qwen 3, Benchmarks, and Real‑World Use Cases | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/qwen-3-5-explained-architecture-upgrades-over-qwen-3-benchmarks-and-real-world-use-cases-af38b01e9888"},{"title":"[Model Request] Qwen3.5 support — Gated DeltaNet + MoE architecture · Issue #778 · mlc-ai/web-llm","url":"https://github.com/mlc-ai/web-llm/issues/778"},{"title":"Running Qwen 3.5 Medium Models on Vast.ai","url":"https://vast.ai/article/running-qwen-3-5-medium-models-on-vast-ai"},{"title":"[Deep Dive] Qwen 3.5 Brings Native Multimodality and Long Context to Small Open Models","url":"https://trilogyai.substack.com/p/deep-dive-qwen-35-brings-native-multimodality"}]

Based on the search results, here's what I found about Qwen3.5's gated attention:

## Gated Attention in Qwen3.5

Qwen3.5 combines Gated Delta Networks (a linear attention variant) with sparse Mixture-of-Experts in a hybrid architecture. Qwen3-Next uses a 3:1 hybrid attention layout in which most layers use Gated DeltaNet (linear attention) and the remaining layers use Gated Attention (full/softmax-style attention).

### Purpose and Benefits

The gated attention output gating helps eliminate attention sinks and massive activations, improving training stability at scale. More specifically, the gated attention block in Qwen-style hybrids is essentially standard scaled-dot-product attention with a few changes on top: an output gate that scales the attention result before it is added back to the residual, a zero-centered QK-Norm variant instead of standard RMSNorm for q and k.

### Role in the Hybrid Architecture

These recent hybrids do not replace attention everywhere. Instead, they replace most attention layers with a cheaper alternative and keep a smaller number of full-attention layers in the stack. Those remaining full-attention layers are where gated attention typically appears.

Qwen 3.5 addresses this with a hybrid layout that interleaves GDN layers with standard full softmax attention layers at regular intervals. Periodic full attention layers act as precision checkpoints: they can attend to any position in the full context with exact scoring, resolving ambiguities or retrieving specific facts that the compressed state might have degraded.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77c928d1-c155-4ddd-88be-0823278d7e06",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "bcd2032b-3382-410a-a265-1091060f636e",
  "sourceToolAssistantUUID": "77c928d1-c155-4ddd-88be-0823278d7e06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T09:20:13.778Z_

<details><summary>↩ Tool result · `toolu_015kj3GFBaPFyqJugvtGikY2`</summary>

```text
Web search results for query: "EACL 2027 commitment deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"EACL","url":"https://eacl.org/conferences/"},{"title":"eaclmeeting (@eaclmeeting) / X","url":"https://x.com/eaclmeeting?lang=en"},{"title":"eaclmeeting","url":"https://twitter.com/eaclmeeting?lang=en"}]

Based on the search results, here's what I found about the EACL 2027 commitment deadline:

The search results don't contain a specific commitment deadline date for EACL 2027 yet. However, I can provide some related information:

The ARR submission deadline for EACL 2027 is August 3, 2026, and EACL is earlier than usual in 2027, so this is the only viable ARR cycle.

The Program Committee is currently finalizing the comprehensive Call for Papers and detailed timetable for EACL 2027, so the complete schedule including the commitment deadline appears to be pending. For the most up-to-date information on the commitment deadline, I'd recommend checking the official EACL 2027 website at https://2027.eacl.org/ or following the EACL conference announcements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52da5402-cb43-4711-bfb5-6aea1fcd406a",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "a21cd4ae-24cb-473f-a74c-93e124d1445a",
  "sourceToolAssistantUUID": "52da5402-cb43-4711-bfb5-6aea1fcd406a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T09:20:16.697Z_

<details><summary>↩ Tool result · `toolu_01XyDuSA3wRSSzxcanstizED`</summary>

```text
Web search results for query: "Qwen3-Coder-Next"

Links: [{"title":"Qwen/Qwen3-Coder-Next · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Coder-Next"},{"title":"qwen3-coder-next","url":"https://ollama.com/library/qwen3-coder-next"},{"title":"Qwen3-Coder-Next: Pushing Small Hybrid Models","url":"https://qwen.ai/blog?id=qwen3-coder-next"},{"title":"Qwen3-Coder-Next: How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3-coder-next"},{"title":"[2603.00729] Qwen3-Coder-Next Technical Report","url":"https://arxiv.org/abs/2603.00729"},{"title":"Qwen3-Coder-Next","url":"https://lmstudio.ai/models/qwen3-coder-next"},{"title":"Qwen3 Coder Next - Amazon Bedrock","url":"https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-qwen-qwen3-coder-next.html"},{"title":"Qwen3 Coder Next - API Pricing & Providers | OpenRouter","url":"https://openrouter.ai/qwen/qwen3-coder-next"},{"title":"GitHub - QwenLM/Qwen3-Coder: Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team. · GitHub","url":"https://github.com/QwenLM/Qwen3-Coder"},{"title":"qwen/qwen3-coder-next • LM Studio","url":"https://lmstudio.ai/models/qwen/qwen3-coder-next"}]

## Qwen3-Coder-Next

Qwen3-Coder-Next is an open-weight language model designed specifically for coding agents and local development. 

### Architecture and Parameters

It features only 3B activated parameters out of 80B total parameters, achieving performance comparable to models with 10–20x more active parameters. Built on top of Qwen3-Next-80B-A3B-Base, which adopts a novel architecture with hybrid attention and MoE, Qwen3-Coder-Next has been agentically trained at scale on large-scale executable task synthesis, environment interaction, and reinforcement learning.

### Key Features

It excels at long-horizon reasoning, complex tool usage, and recovery from execution failures, ensuring robust performance in dynamic coding tasks. With a 256k context length, combined with adaptability to various scaffold templates, it enables seamless integration with different CLI/IDE platforms.

### Performance

Qwen3-Coder-Next achieves over 70% on SWE-Bench Verified using the SWE-Agent scaffold. It achieves SWE-Bench-Pro performance comparable to models with 10×–20× more active parameters.

### Availability

Qwen3-Coder-Next is licensed under Apache 2.0 and is available through multiple platforms including Hugging Face, Ollama, and various inference engines like vLLM and sglang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e023241-ccc3-4ec6-8276-d04b04857540",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "73874fc0-ed62-4f98-847f-50a651f42ff3",
  "sourceToolAssistantUUID": "6e023241-ccc3-4ec6-8276-d04b04857540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T09:20:19.493Z_

Now let me search for more specific information on the EACL 2027 commitment deadline and the ARR August 2026 submission deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73874fc0-ed62-4f98-847f-50a651f42ff3",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tniZGrdFShegmTnMuT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3edfd31-5b28-4428-b023-dd7b05a097c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THff1hZc2rH8Rjj1ywYMQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 4186,
      "cache_read_input_tokens": 10399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4186,
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

_source line 18 · 2026-05-17T09:20:20.127Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BdwFwFAoj55GY5bfbG1VjC`</summary>

```json
{
  "query": "EACL 2027 \"October 11\" commitment deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3edfd31-5b28-4428-b023-dd7b05a097c9",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tniZGrdFShegmTnMuT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4611bd1-3898-4777-8ea0-267e291bd4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THff1hZc2rH8Rjj1ywYMQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 4186,
      "cache_read_input_tokens": 10399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4186,
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

_source line 19 · 2026-05-17T09:20:21.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016AXZWc74a5KDCgQpUqeJej`</summary>

```json
{
  "query": "\"ARR August 2026\" submission deadline \"August 3\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4611bd1-3898-4777-8ea0-267e291bd4c9",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7tniZGrdFShegmTnMuT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d42440ac-d978-4389-b23b-8587b1e84e3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THff1hZc2rH8Rjj1ywYMQ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1020,
      "cache_creation_input_tokens": 4186,
      "cache_read_input_tokens": 10399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4186,
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

_source line 20 · 2026-05-17T09:20:22.623Z_

<details><summary>↩ Tool result · `toolu_01BdwFwFAoj55GY5bfbG1VjC`</summary>

```text
Web search results for query: "EACL 2027 "October 11" commitment deadline ARR"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"Submission Dates and Process for EACL/NAACL and ACL 2024 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/submission-dates-and-process-eaclnaacl-and-acl-2024"},{"title":"eaclmeeting (@eaclmeeting) / X","url":"https://x.com/eaclmeeting?lang=en"}]

Based on the search results, I found the information you were looking for:

For EACL 2027, the ARR submission deadline is August 3, 2026, and the commitment deadline is October 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4611bd1-3898-4777-8ea0-267e291bd4c9",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "bf76988a-eb37-472a-8e20-62a0c30254a3",
  "sourceToolAssistantUUID": "a4611bd1-3898-4777-8ea0-267e291bd4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T09:20:24.237Z_

<details><summary>↩ Tool result · `toolu_016AXZWc74a5KDCgQpUqeJej`</summary>

```text
Web search results for query: ""ARR August 2026" submission deadline "August 3""

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, I found information about ARR August 2026 and the August 3 deadline:

EACL 2027 has a Final ARR Submission Date of August 3, 2026. This indicates that August 3, 2026 is the submission deadline for papers to be reviewed in the ARR cycle that will be considered for the EACL 2027 conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d42440ac-d978-4389-b23b-8587b1e84e3f",
  "isSidechain": true,
  "promptId": "67bf68f5-a732-420e-aeec-d06f160e65d1",
  "agentId": "a27a328a6c270c784",
  "type": "user",
  "uuid": "7a6da04f-bacb-4d5f-a354-a87ec17765df",
  "sourceToolAssistantUUID": "d42440ac-d978-4389-b23b-8587b1e84e3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-17T09:20:54.741Z_

Here is my full report on what I found:

---

## 1. AAAI 2027 Deadlines

**CONFIRMED.** The search results confirm:
- **Abstract deadline: July 21, 2026** (11:59 PM UTC-12)
- **Full paper deadline: July 28, 2026** (11:59 PM UTC-12)
- Supplementary material/code: July 31, 2026
- Conference dates: February 16-23, 2027, Montreal, Quebec, Canada

Sources:
- [AAAI-27 Main Technical Track](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AI Deadlines - AAAI 27](http://aideadlines.org/conference/?id=aaai27)
- [PaperPilot - AAAI 2027](https://www.getpaperpilot.com/deadlines/aaai-2027.html)

---

## 2. ARR August 2026 Cycle - Submission Deadline

**CONFIRMED.** The ARR August 2026 submission deadline is **August 3, 2026**. This is specifically noted as the "Final ARR Submission Date" for EACL 2027 -- meaning it is the last ARR cycle whose reviews will be available in time for EACL 2027 commitment. The EACL Twitter account posted a correction noting the deadline is August 3 (not August 6 as previously announced).

Sources:
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [EACL Twitter correction](https://x.com/eaclmeeting/status/2051971432171688436)
- [ACL Rolling Review GitHub - dates.md](https://github.com/acl-org/aclrollingreview/blob/main/dates.md)

---

## 3. EACL 2027 Commitment Deadline

**CONFIRMED.** The EACL 2027 commitment deadline is **October 11, 2026**. The conference will be held March 9-14, 2027 in Athens, Greece (20th Conference of the European Chapter of ACL).

Sources:
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [EACL 2027 Official Website](https://2027.eacl.org/)
- [EACL 2027 Call for Main Conference Papers](https://2027.eacl.org/calls/papers/)

---

## 4. EMNLP 2026 / ARR May 2026 Cycle Deadline

**CONFIRMED.** The ARR May 2026 submission deadline is **May 25, 2026**. This is aligned with EMNLP 2026 (and also AACL 2026). The EMNLP 2026 Twitter account explicitly states: "ARR Submission Deadline: May 25, 2026." Author registration form was due by May 27, 2026.

Sources:
- [EMNLP 2026 Twitter - Call for Papers](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL ARR 2026 May on OpenReview](https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay)

---

## 5. Qwen3-Coder-Next

**EXISTS.** Qwen3-Coder-Next is a real, publicly available model. Key facts:
- **Architecture:** 80B total parameters, only 3B activated (MoE), built on Qwen3-Next-80B-A3B-Base
- **Hybrid attention + MoE architecture** (Gated DeltaNet linear attention + Gated Attention)
- **Context length:** 256K tokens
- **Performance:** Over 70% on SWE-Bench Verified (using SWE-Agent scaffold); comparable to models with 10-20x more active parameters
- **License:** Apache 2.0
- **Available on:** Hugging Face, Ollama, Amazon Bedrock, OpenRouter, LM Studio, vLLM, sglang
- **Technical report:** [arXiv:2603.00729](https://arxiv.org/abs/2603.00729)

Sources:
- [Qwen/Qwen3-Coder-Next on Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen Blog - Qwen3-Coder-Next](https://qwen.ai/blog?id=qwen3-coder-next)
- [arXiv Technical Report](https://arxiv.org/abs/2603.00729)
- [Amazon Bedrock - Qwen3-Coder-Next](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-qwen-qwen3-coder-next.html)
- [OpenRouter - Qwen3-Coder-Next](https://openrouter.ai/qwen/qwen3-coder-next)

---

## 6. Qwen3.5 Gated Attention

**EXISTS.** Qwen3.5 does use gated attention as part of a hybrid architecture. Key details:
- **Hybrid layout:** Combines Gated Delta Networks (GDN, a linear attention variant) with sparse Mixture-of-Experts
- **3:1 ratio:** Most layers use Gated DeltaNet (linear attention); remaining layers use Gated Attention (full softmax-style attention)
- **Gated Attention specifics:** Standard scaled-dot-product attention with an output gate that scales the attention result before adding to the residual, plus zero-centered QK-Norm (instead of standard RMSNorm)
- **Purpose:** The output gating eliminates attention sinks and massive activations, improving training stability at scale. Periodic full-attention layers act as "precision checkpoints" for exact positional scoring.

Sources:
- [Hugging Face Blog - "Qwen3.5: Nobody Agrees on Attention Anymore"](https://huggingface.co/blog/mlabonne/qwen35)
- [Sebastian Raschka - Gated Attention](https://sebastianraschka.com/llm-architecture-gallery/gated-attention/)
- [Medium - Qwen 3.5 Explained: Architecture, Upgrades](https://medium.com/data-science-in-your-pocket/qwen-3-5-explained-architecture-upgrades-over-qwen-3-benchmarks-and-real-world-use-cases-af38b01e9888)
- [web-llm Issue #778 - Qwen3.5 Gated DeltaNet + MoE](https://github.com/mlc-ai/web-llm/issues/778)

---

## Summary

All four venue deadlines are **confirmed as stated**:

| Venue | Deadline Type | Date | Verified |
|-------|--------------|------|----------|
| AAAI 2027 | Abstract | July 21, 2026 | Yes |
| AAAI 2027 | Full paper | July 28, 2026 | Yes |
| ARR August 2026 | Submission | August 3, 2026 | Yes |
| EACL 2027 | Commitment | October 11, 2026 | Yes |
| ARR May 2026 (EMNLP) | Submission | May 25, 2026 | Yes |

Both **Qwen3-Coder-Next** and **Qwen3.5 gated attention** are real and publicly documented -- Qwen3-Coder-Next is a deployed model available on multiple platforms with an arXiv paper, and Qwen3.5's gated attention architecture is well-documented in blog posts and community discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a6da04f-bacb-4d5f-a354-a87ec17765df",
  "isSidechain": true,
  "agentId": "a27a328a6c270c784",
  "requestId": "req_011Cb7toGok9GHCEAxqwrDyo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1fbd518a-9f5f-4865-92ab-350ead2bff01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5e5f2da5-ca26-4e16-841c-663231b08081",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7Cg34XzNptkwPxyy8ijJE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2307,
      "cache_read_input_tokens": 14585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2307,
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
