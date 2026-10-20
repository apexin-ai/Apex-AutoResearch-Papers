# Research conversation: I need to verify two things about EMNLP 2026: 1. Is the ARR (ACL Rolling Review) submission deadline for EMNLP 2026 on M

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a1c323c88f4fc6a6a.jsonl`
- **Structured JSON:** [`723e18253154a1f649ed.json`](../../sessions/72/723e18253154a1f649ed.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-11T23:30:57.196Z_

I need to verify two things about EMNLP 2026:

1. Is the ARR (ACL Rolling Review) submission deadline for EMNLP 2026 on May 25, 2026? Search for "EMNLP 2026 ARR submission deadline" and "ACL Rolling Review May 2026 deadline"

2. Does EMNLP 2026 have a special theme about "New Missions for NLP Research" that explicitly calls for work on data contamination, synthetic data feedback loops, and data governance? Search for "EMNLP 2026 special theme" and "EMNLP 2026 call for papers"

Report what you find concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "925fbac5-fd9e-4f74-a107-f3f91c2f297c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:30:57.198Z_

```json
{
  "parentUuid": "925fbac5-fd9e-4f74-a107-f3f91c2f297c",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
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
  "uuid": "e4612fad-e603-42ad-aa3b-4c0bd9a6db11",
  "timestamp": "2026-05-11T23:30:57.198Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:31:17.426Z_



I'll search for both pieces of information now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4612fad-e603-42ad-aa3b-4c0bd9a6db11",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CaweodzYdfdB9H3eFcyP3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e18d7c9-427d-4d94-9f10-6a5c4130704d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZEUZ2YmynQ2s6YqgZB3DU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 718,
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

_source line 4 · 2026-05-11T23:31:17.918Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JMeATff6X3xw4cgxdELpg2`</summary>

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
  "parentUuid": "3e18d7c9-427d-4d94-9f10-6a5c4130704d",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CaweodzYdfdB9H3eFcyP3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b10a360-766d-40bd-954b-d84355fd3442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZEUZ2YmynQ2s6YqgZB3DU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 718,
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

### Tool result

_source line 5 · 2026-05-11T23:31:17.926Z_

<details><summary>↩ Tool result · `toolu_01JMeATff6X3xw4cgxdELpg2`</summary>

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
  "parentUuid": "5b10a360-766d-40bd-954b-d84355fd3442",
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "9745002c-ff12-4799-95f6-498b3a2e8ebd",
  "sourceToolAssistantUUID": "5b10a360-766d-40bd-954b-d84355fd3442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:31:25.243Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9745002c-ff12-4799-95f6-498b3a2e8ebd",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CaweqCG37Resh2EoV7zQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35333f68-a201-4de6-9a02-87ca79efdc64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEidHTVppJfm3SAG3TvCRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 7 · 2026-05-11T23:31:25.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01St7Jh7jBuTLEJZCCVXJYiy`</summary>

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
  "parentUuid": "35333f68-a201-4de6-9a02-87ca79efdc64",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CaweqCG37Resh2EoV7zQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64f6f709-c422-4073-b36c-1e08ad47f499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEidHTVppJfm3SAG3TvCRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 8 · 2026-05-11T23:31:26.254Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QHvm2LEdqceARiDgcRXzyH`</summary>

```json
{
  "query": "ACL Rolling Review May 2026 deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f6f709-c422-4073-b36c-1e08ad47f499",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CaweqCG37Resh2EoV7zQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45bcb64e-9fda-4443-b1f6-643293c92815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEidHTVppJfm3SAG3TvCRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 9 · 2026-05-11T23:31:26.728Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019aUg9123hjN7dPBMdEqNpm`</summary>

```json
{
  "query": "EMNLP 2026 special theme"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45bcb64e-9fda-4443-b1f6-643293c92815",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CaweqCG37Resh2EoV7zQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dbcf061-2a12-4c15-8a8a-daa6aa5e7dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEidHTVppJfm3SAG3TvCRp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 10 · 2026-05-11T23:31:26.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018SoPTzxQVaLb9piTue33Xd`</summary>

```json
{
  "query": "EMNLP 2026 call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dbcf061-2a12-4c15-8a8a-daa6aa5e7dce",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CaweqCG37Resh2EoV7zQX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0448d091-5550-4357-983a-413ba14b5b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEidHTVppJfm3SAG3TvCRp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8941,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 211,
          "cache_read_input_tokens": 8941,
          "cache_creation_input_tokens": 1404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1404,
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

_source line 11 · 2026-05-11T23:31:30.555Z_

<details><summary>↩ Tool result · `toolu_01St7Jh7jBuTLEJZCCVXJYiy`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, the ARR submission deadline for EMNLP 2026 is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Additional important dates for EMNLP 2026 include:
- Reviewer registration deadline for all authors: May 27, 2026
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
  "parentUuid": "64f6f709-c422-4073-b36c-1e08ad47f499",
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "d287574d-461c-4cf9-afaa-0b749cacc706",
  "sourceToolAssistantUUID": "64f6f709-c422-4073-b36c-1e08ad47f499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:31:31.008Z_

<details><summary>↩ Tool result · `toolu_01QHvm2LEdqceARiDgcRXzyH`</summary>

```text
Web search results for query: "ACL Rolling Review May 2026 deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here's information about ACL Rolling Review deadlines in May 2026:

The ACL Peer Review Committee recommended switching to 10-week review cycles, with the new schedule starting in May 2025. However, the search results don't provide specific details about a May 2026 submission deadline.

What is available from the search results:

- Papers may be submitted to the ARR 2025 October cycle and ARR 2026 January cycle
- The submission deadline is always the 15th of the month; other dates vary due to the length of months, timing of weekends, etc.

For the most current and specific information about May 2026 ARR deadlines, I recommend checking the official ACL Rolling Review website at **aclrollingreview.org**, as the detailed schedule for May 2026 may not yet be fully published in the available sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45bcb64e-9fda-4443-b1f6-643293c92815",
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "a6fdfcf9-daa9-42ad-b95e-a7828103ce0e",
  "sourceToolAssistantUUID": "45bcb64e-9fda-4443-b1f6-643293c92815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:31:31.510Z_

<details><summary>↩ Tool result · `toolu_019aUg9123hjN7dPBMdEqNpm`</summary>

```text
Web search results for query: "EMNLP 2026 special theme"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"The center of gravity in NLP is shifting. 🌍 This year's #EMNLP2026 Special Theme is \"New Missions for NLP Research.\" We welcome empirical, theoretical, or position and survey papers that reframe our collective research goals. Find out more: https://t.co/6dttoXBb3B\" / X","url":"https://x.com/emnlpmeeting/status/2029509201580446135"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP (@emnlpmeeting.bsky.social) — Bluesky","url":"https://bsky.app/profile/emnlpmeeting.bsky.social"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, "New Missions for NLP Research" is the EMNLP 2026 special theme.

The theme acknowledges that large language models have rapidly shifted from research prototypes to widely used infrastructure, changing the center of gravity of NLP research. Since progress can no longer be measured only by fractional improvements in benchmark scores, the field faces a more foundational question: What are the missions of NLP research now, and what kinds of contributions most advance that mission?

The EMNLP 2026 special theme welcomes work that reflects on the mission(s) of NLP research, reframes collective research goals, proposes new evaluation and scientific methodologies, and builds bridges across multiple disciplines that can sharpen both theories and impact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dbcf061-2a12-4c15-8a8a-daa6aa5e7dce",
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "f8c70a10-f677-44ae-be11-cf53af0793ff",
  "sourceToolAssistantUUID": "3dbcf061-2a12-4c15-8a8a-daa6aa5e7dce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:31:33.889Z_

<details><summary>↩ Tool result · `toolu_018SoPTzxQVaLb9piTue33Xd`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Here's the information about the EMNLP 2026 Call for Papers:

## Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Key Deadlines
The ARR submission deadline for long and short papers is May 25, 2026, and the EMNLP commitment deadline is August 2, 2026, with notification of acceptance on August 20, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Special Requirements for ARR Submissions
For the ARR 2026 May cycle aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026. Dual submissions are not allowed.

## Special Conference Theme
The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in the era of large language models.

## Reviewer Requirements
All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications.

## Venue
EMNLP 2026 will be held as a hybrid conference in Budapest, Hungary from October 24th to October 29th, 2026.

For the full call for papers, visit: https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0448d091-5550-4357-983a-413ba14b5b50",
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "12b74a40-9645-488e-a7a8-87e229fb8197",
  "sourceToolAssistantUUID": "0448d091-5550-4357-983a-413ba14b5b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-11T23:31:51.532Z_

Let me now fetch the official EMNLP 2026 call for papers page to check the specific details about the special theme topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12b74a40-9645-488e-a7a8-87e229fb8197",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CawerLvU3jXQLp2RQcBwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a96e4bd-5d52-4200-bd37-3338f704f9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3YQ4TmHpQrPjxBjcj9FMX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3671,
      "cache_read_input_tokens": 10345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3671,
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

_source line 16 · 2026-05-11T23:31:51.788Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LG9VBNJgpwyK1FjSx5Ux6a`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a96e4bd-5d52-4200-bd37-3338f704f9dd",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CawerLvU3jXQLp2RQcBwY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4006d378-2fcf-46cd-8bb4-15c6ec547f5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3YQ4TmHpQrPjxBjcj9FMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3671,
      "cache_read_input_tokens": 10345,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3671
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 10345,
          "cache_creation_input_tokens": 3671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3671,
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

_source line 17 · 2026-05-11T23:31:51.796Z_

<details><summary>↩ Tool result · `toolu_01LG9VBNJgpwyK1FjSx5Ux6a`</summary>

````text
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
  "parentUuid": "4006d378-2fcf-46cd-8bb4-15c6ec547f5e",
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "e67abe3d-1f91-4c8c-ad35-1f151350045c",
  "sourceToolAssistantUUID": "4006d378-2fcf-46cd-8bb4-15c6ec547f5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-11T23:31:56.593Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018wj28FAg81EM7LMNXEGVmm`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the full description of the special theme for EMNLP 2026. Does it explicitly mention \"data contamination\", \"synthetic data feedback loops\", and \"data governance\"? List all specific topics or examples mentioned under the special theme."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e67abe3d-1f91-4c8c-ad35-1f151350045c",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CawesfiLnMFLs3URtVhnp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d9ce9e6-2067-4d6f-997e-afef80d3a736",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNsD7zrCwGyMts5HBWGt2q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 14016,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 626
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 139,
          "cache_read_input_tokens": 14016,
          "cache_creation_input_tokens": 626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 626,
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

_source line 19 · 2026-05-11T23:32:02.068Z_

<details><summary>↩ Tool result · `toolu_018wj28FAg81EM7LMNXEGVmm`</summary>

```text
# EMNLP 2026 Special Theme: Full Description

The special theme is titled **"New Missions for NLP Research"** and addresses how the field must evolve now that large language models have become widely available infrastructure rather than research prototypes.

## Core Question

The theme asks: "What are the missions of NLP research now, and what kinds of contributions most advance that mission?"

## Explicit Mentions of Data-Related Concerns

Yes, the description explicitly mentions all three concepts you asked about:

- **Data contamination**: Referenced under the data bottleneck section
- **Synthetic data feedback loops**: Mentioned as a consequence researchers should examine
- **Data governance**: Listed as part of new approaches to data management

The exact wording states: "research on data scarcity and limits, contamination, and the consequences of synthetic data feedback loops, and new approaches to data creation, documentation, governance, and consent."

## Five Main Topic Areas

1. **Rethinking progress and evaluation in NLP** — moving beyond leaderboards to include real-world impact and trustworthiness

2. **From models to systems and ecosystems** — examining agentic workflows and community interactions with language technology

3. **Scientific understanding of language and cognition** — using models as experimental instruments for psycholinguistics and cognitive science

4. **Data as a bottleneck and responsibility** — addressing scarcity, contamination, and governance issues

5. **LLMs as research tools** — studying how language models support hypothesis generation and peer review without compromising scientific standards
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d9ce9e6-2067-4d6f-997e-afef80d3a736",
  "isSidechain": true,
  "promptId": "f106fb09-5670-4440-b772-04397a73b852",
  "agentId": "a1c323c88f4fc6a6a",
  "type": "user",
  "uuid": "2726b27f-2de1-4333-bae4-28d39d564357",
  "sourceToolAssistantUUID": "7d9ce9e6-2067-4d6f-997e-afef80d3a736",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-11T23:32:20.139Z_

Here are the findings for both questions:

**1. ARR Submission Deadline: Confirmed -- May 25, 2026**

Yes, the ARR submission deadline for EMNLP 2026 is indeed **May 25, 2026** (11:59 PM UTC-12:00, "anywhere on Earth"). This is confirmed across multiple sources including the official EMNLP 2026 Twitter/X account and the call for papers page. One important note: since EMNLP and AACL share the ARR May cycle, authors must explicitly select a target conference at submission time, and this choice is binding.

**2. Special Theme: Confirmed -- "New Missions for NLP Research" does explicitly call for work on all three topics**

The special theme is titled **"New Missions for NLP Research."** The official call for papers explicitly mentions all three topics you asked about. The relevant passage states:

> "research on data scarcity and limits, contamination, and the consequences of synthetic data feedback loops, and new approaches to data creation, documentation, governance, and consent."

This falls under one of five main topic areas for the theme: "Data as a bottleneck and responsibility." So yes, data contamination, synthetic data feedback loops, and data governance are all explicitly called out.

Sources:
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Special Theme announcement (X/Twitter)](https://x.com/emnlpmeeting/status/2029509201580446135)
- [EMNLP 2026 critical update on ARR May cycle (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2726b27f-2de1-4333-bae4-28d39d564357",
  "isSidechain": true,
  "agentId": "a1c323c88f4fc6a6a",
  "requestId": "req_011CawetVjbHNyPQhMNgv8Eb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c3898b3-59c1-4b03-a0dd-51a196d80c19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e3d4a678-ae0c-4d3b-b878-e2498394350b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D384iNQWBaPbLQu4t3Gaqj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 597,
      "cache_read_input_tokens": 14642,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 597
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 14642,
          "cache_creation_input_tokens": 597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 597,
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
