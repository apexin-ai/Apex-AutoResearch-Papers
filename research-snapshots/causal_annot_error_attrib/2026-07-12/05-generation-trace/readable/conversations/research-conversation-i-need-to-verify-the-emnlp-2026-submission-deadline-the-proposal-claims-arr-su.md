# Research conversation: I need to verify the EMNLP 2026 submission deadline. The proposal claims "ARR submission deadline: May 25, 2026; confere

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a68adbc68b439697f.jsonl`
- **Structured JSON:** [`ffb8342cb782d8e3380b.json`](../../sessions/ff/ffb8342cb782d8e3380b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-16T09:02:59.957Z_

I need to verify the EMNLP 2026 submission deadline. The proposal claims "ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest."

1. WebSearch "EMNLP 2026 submission deadline ARR"
2. WebSearch "EMNLP 2026 Budapest dates"
3. WebSearch "ARR May 2026 deadline"
4. WebSearch "ACL Rolling Review 2026 deadlines"

Report exactly what you find about:
- Is EMNLP 2026 in Budapest?
- What is the ARR submission deadline for the cycle that feeds into EMNLP 2026?
- Is May 25, 2026 a real ARR deadline?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a68adbc68b439697f",
  "type": "user",
  "uuid": "f7d57a07-3780-4ee4-acba-16c63b474559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:02:59.959Z_

```json
{
  "parentUuid": "f7d57a07-3780-4ee4-acba-16c63b474559",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
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
  "uuid": "b851745e-6304-4525-8c98-2c26e8eb1d37",
  "timestamp": "2026-05-16T09:02:59.959Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T09:03:03.124Z_



I'll search for all four queries in parallel to verify the EMNLP 2026 submission deadline claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b851745e-6304-4525-8c98-2c26e8eb1d37",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5yfNtU2UZyCNMPNhMc1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3378a72c-f30f-4ec4-b6c6-d2341eebf153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01151fzGR6qK9ZDKSgU9jnWn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 727,
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

_source line 4 · 2026-05-16T09:03:03.137Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WuQyqEYjXz34UFchMKKZGG`</summary>

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
  "parentUuid": "3378a72c-f30f-4ec4-b6c6-d2341eebf153",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5yfNtU2UZyCNMPNhMc1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8be9c66-8fd7-4e67-a8d4-06d60b9521f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01151fzGR6qK9ZDKSgU9jnWn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 727,
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

### Tool result

_source line 5 · 2026-05-16T09:03:03.139Z_

<details><summary>↩ Tool result · `toolu_01WuQyqEYjXz34UFchMKKZGG`</summary>

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
  "parentUuid": "a8be9c66-8fd7-4e67-a8d4-06d60b9521f1",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a68adbc68b439697f",
  "type": "user",
  "uuid": "a4566db3-db5e-49ff-aae4-58bb218db012",
  "sourceToolAssistantUUID": "a8be9c66-8fd7-4e67-a8d4-06d60b9521f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T09:03:05.918Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4566db3-db5e-49ff-aae4-58bb218db012",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5yfd5FRQwkrhu3BA345",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6c149f6-1a07-4a43-828f-4739488e28f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAY4L8j12Gx9f4EHbi4T1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 7 · 2026-05-16T09:03:06.518Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TL2XQqsriooy1ZTjmUHR6s`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6c149f6-1a07-4a43-828f-4739488e28f7",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5yfd5FRQwkrhu3BA345",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f705aa4a-bddb-4eb7-88c5-e86a7ca47041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAY4L8j12Gx9f4EHbi4T1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 8 · 2026-05-16T09:03:06.876Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EQbQxz9Q8Rf5We4ANXS9eT`</summary>

```json
{
  "query": "EMNLP 2026 Budapest dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f705aa4a-bddb-4eb7-88c5-e86a7ca47041",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5yfd5FRQwkrhu3BA345",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32e994b7-cb94-4b30-bb6e-330b36827265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAY4L8j12Gx9f4EHbi4T1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 9 · 2026-05-16T09:03:06.890Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QQLacmxyAjL5Hrz1rBCAw9`</summary>

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
  "parentUuid": "32e994b7-cb94-4b30-bb6e-330b36827265",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5yfd5FRQwkrhu3BA345",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e9795a3-257a-4f8f-9163-d043f9610f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAY4L8j12Gx9f4EHbi4T1p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 10 · 2026-05-16T09:03:07.106Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DMeWqCj6ARmTrkgBz6DWB7`</summary>

```json
{
  "query": "ACL Rolling Review 2026 deadlines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e9795a3-257a-4f8f-9163-d043f9610f8a",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5yfd5FRQwkrhu3BA345",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ffdfdc3-f540-4a92-94ad-1da73df8a612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAY4L8j12Gx9f4EHbi4T1p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8950,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 207,
          "cache_read_input_tokens": 8950,
          "cache_creation_input_tokens": 1419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1419,
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

_source line 11 · 2026-05-16T09:03:09.800Z_

<details><summary>↩ Tool result · `toolu_01EQbQxz9Q8Rf5We4ANXS9eT`</summary>

```text
Web search results for query: "EMNLP 2026 Budapest dates"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing | Truescho","url":"https://truescho.com/en/opportunities/emnlp-2026-conference-on-empirical-methods-in-natural-language-processing"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

EMNLP 2026 will be held October 24-29 in Budapest, Hungary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32e994b7-cb94-4b30-bb6e-330b36827265",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a68adbc68b439697f",
  "type": "user",
  "uuid": "f68dbdcf-93a4-4115-923d-951aaaad4279",
  "sourceToolAssistantUUID": "32e994b7-cb94-4b30-bb6e-330b36827265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:03:11.680Z_

<details><summary>↩ Tool result · `toolu_01QQLacmxyAjL5Hrz1rBCAw9`</summary>

```text
Web search results for query: "ARR May 2026 deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=arr2601"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"AACL 2026 on X: \"🚨AACL-IJCNLP 2026 will be held in Hengqin, China from November 6-10, 2026. The CFP is now out! ARR submission deadline (long &amp; short papers): May 25, 2026! #NLProc #NLP Dates and full CFP here: https://t.co/4ON2H5M7zQ @aadi_joshi @kta84912 https://t.co/9ZKWmY7Jvv\" / X","url":"https://x.com/aaclmeeting/status/2041832211599733075"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's what I found about the ARR (ACL Rolling Review) May 2026 deadline:

The ARR submission deadline for May 2026 is May 25, 2026, which applies to multiple conferences. This deadline is relevant for:

- EMNLP 2026
- AACL-IJCNLP 2026

Additionally, after submission, all authors must complete the author registration form by May 27, 2026 EoD AoE (for EMNLP 2026).

For the ARR 2026 May cycle aligned with EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e9795a3-257a-4f8f-9163-d043f9610f8a",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a68adbc68b439697f",
  "type": "user",
  "uuid": "7c4e3c22-14a6-4cc9-b7e1-7cfb3cbbc435",
  "sourceToolAssistantUUID": "5e9795a3-257a-4f8f-9163-d043f9610f8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T09:03:12.035Z_

<details><summary>↩ Tool result · `toolu_01TL2XQqsriooy1ZTjmUHR6s`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"The EMNLP call for System Demonstrations has now been posted! The submission deadline is July 4th, with additional details available here: https://t.co/BQvAw3vHxT\" / X","url":"https://x.com/emnlpmeeting/status/1915050634501660921"}]

Based on the search results, here's the information about EMNLP 2026 submission deadline via ARR:

## EMNLP 2026 ARR Submission Deadline

The ARR submission deadline is May 25, 2026.

## Important Policy Information

There is a new policy for the ARR 2026 May cycle: Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Additional Important Dates

The reviewer registration deadline for all authors is May 27, 2026, author response and author-reviewer discussion occurs July 7-13, 2026, meta review is released July 30, 2026, the EMNLP commitment deadline is August 2, 2026, and notification of acceptance is August 20, 2026.

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f705aa4a-bddb-4eb7-88c5-e86a7ca47041",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a68adbc68b439697f",
  "type": "user",
  "uuid": "0cfbdc7b-713e-42ce-a0c6-9bacd184e163",
  "sourceToolAssistantUUID": "f705aa4a-bddb-4eb7-88c5-e86a7ca47041",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:03:15.539Z_

<details><summary>↩ Tool result · `toolu_01DMeWqCj6ARmTrkgBz6DWB7`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 deadlines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL ARR 2025 February | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FFebruary"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl?lang=en"}]

Based on the search results, here are the key ACL Rolling Review 2026 deadlines:

## Submission Deadline
The submission deadline for the January 2026 cycle is January 5, 2026.

## Author Requirements
All authors must complete the author registration form by January 7th 2026 EoD AoE.

## Review Completion Deadlines
Reviews must be completed by February 7th, and meta-reviews by March 3rd.

## Reviewer Registration
For authors who will be assigned as reviewers or meta-reviewers, the deadline for completing the registration form is January 7th 2026 EoD AoE.

## Reviews Available
ARR reviews and meta-reviews will be available to authors of the January cycle on March 10, 2026.

The ACL Rolling Review switched to 10-week cycles starting in May 2025, which affects the timing and frequency of review cycles compared to the previous 8-week schedule.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ffdfdc3-f540-4a92-94ad-1da73df8a612",
  "isSidechain": true,
  "promptId": "c0b2dcb7-0dd5-433d-a0d3-dd686e91d702",
  "agentId": "a68adbc68b439697f",
  "type": "user",
  "uuid": "7b4af77e-e607-4438-b7b1-c25ddf67c4af",
  "sourceToolAssistantUUID": "1ffdfdc3-f540-4a92-94ad-1da73df8a612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T09:03:32.065Z_

Here is what I found across all four searches:

---

**Is EMNLP 2026 in Budapest?**

Yes, confirmed. EMNLP 2026 will be held **October 24-29, 2026, in Budapest, Hungary**. This is stated on the official EMNLP 2026 website and corroborated by LINGUIST List, ConferenceDeadlines.com, and multiple other sources.

**What is the ARR submission deadline for the cycle that feeds into EMNLP 2026?**

The ARR May 2026 cycle is the submission cycle that feeds into EMNLP 2026. The submission deadline is **May 25, 2026**. This is confirmed by the official EMNLP 2026 Call for Papers page and the EMNLP 2026 Twitter/X account. Key downstream dates after that:

- Reviewer registration deadline for all authors: May 27, 2026
- Author response and author-reviewer discussion: July 7-13, 2026
- Meta-reviews released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026

All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

**Is May 25, 2026 a real ARR deadline?**

Yes, May 25, 2026 is a confirmed, real ARR deadline. It is the submission deadline for the ARR May 2026 cycle. Notably, this cycle is shared between **two** conferences -- EMNLP 2026 and AACL-IJCNLP 2026 (which will be held November 6-10 in Hengqin, China). Because of this shared cycle, there is an important policy: **authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026**. Submissions that do not select EMNLP 2026 during the ARR submission will not be able to commit to EMNLP 2026 later.

---

**Verdict on the proposal's claims:** The statement "ARR submission deadline: May 25, 2026; conference: October 24-29, Budapest" is **accurate on all three points** -- the date, the location, and the conference dates are all confirmed by official sources. The one nuance the proposal does not mention is the binding conference-selection requirement at submission time due to the shared EMNLP/AACL cycle.

Sources:
- [EMNLP 2026 - Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)
- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Critical Update on Shared ARR Cycle (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [AACL-IJCNLP 2026 Announcement (X/Twitter)](https://x.com/aaclmeeting/status/2041832211599733075)
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [LINGUIST List - EMNLP 2026 (Hungary)](https://linguistlist.org/issues/37/972/)
- [AI Conference Deadlines - EMNLP 2026](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b4af77e-e607-4438-b7b1-c25ddf67c4af",
  "isSidechain": true,
  "agentId": "a68adbc68b439697f",
  "requestId": "req_011Cb5ygXbNn6eUbhdUEh5mt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f3be04d-0882-4eab-b06c-646b5478f6ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3851818f-b8a5-4456-92d9-6671bfb78776",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEawEi6WTathNEuBK1DcH7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3439,
      "cache_read_input_tokens": 10369,
      "output_tokens": 920,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 920,
          "cache_read_input_tokens": 10369,
          "cache_creation_input_tokens": 3439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3439,
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
