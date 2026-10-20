# Research conversation: I need to verify: 1. EMNLP 2026 ARR submission deadline - is it actually May 25, 2026? 2. Does EMNLP 2026 accept short p

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5c1b9a4da41f2693.jsonl`
- **Structured JSON:** [`c01c30fc14a5e9e18eef.json`](../../sessions/c0/c01c30fc14a5e9e18eef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-12T00:32:04.128Z_

I need to verify:

1. EMNLP 2026 ARR submission deadline - is it actually May 25, 2026?
2. Does EMNLP 2026 accept short papers?
3. What is the ARR review cycle for a May 2026 submission?

Search for:
- "EMNLP 2026 submission deadline ARR"
- "ARR submission deadline May 2026"
- "ACL Rolling Review 2026 deadlines"

Also check:
- "EMNLP 2026 call for papers"
- site:aclrollingreview.org deadlines 2026

Report what you find about the submission timeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "376278fd-f1ae-4820-8b70-f9c180978eb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:32:04.131Z_

```json
{
  "parentUuid": "376278fd-f1ae-4820-8b70-f9c180978eb8",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
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
  "uuid": "49acddca-7c05-413a-a55c-8d243220ccca",
  "timestamp": "2026-05-12T00:32:04.131Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:32:06.994Z_



I'll search for information about EMNLP 2026 deadlines and ARR submission cycles. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49acddca-7c05-413a-a55c-8d243220ccca",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjTx9xxbdSFf2RuiALJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff4c0c36-8cf3-4ef1-984a-d77ec98eb9d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMDFvpPksvvAAtnQHNzSMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 710,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T00:32:07.382Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NCePZjsEs225tua8vwxXmV`</summary>

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
  "parentUuid": "ff4c0c36-8cf3-4ef1-984a-d77ec98eb9d9",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjTx9xxbdSFf2RuiALJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ae28946-65bf-41b0-9a39-7d2e1a685330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMDFvpPksvvAAtnQHNzSMC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 8223,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 710
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 710,
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

_source line 5 · 2026-05-12T00:32:07.386Z_

<details><summary>↩ Tool result · `toolu_01NCePZjsEs225tua8vwxXmV`</summary>

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
  "parentUuid": "0ae28946-65bf-41b0-9a39-7d2e1a685330",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "6fec075c-de55-4590-990a-3484451f8637",
  "sourceToolAssistantUUID": "0ae28946-65bf-41b0-9a39-7d2e1a685330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:32:10.030Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fec075c-de55-4590-990a-3484451f8637",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUC96X1LUy3zc4gG5B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d931d103-b9c8-4e1d-98e1-8dc06558bd8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2DnYmZHyjB9tHdDDpfz2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 7 · 2026-05-12T00:32:10.515Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S3ErpUPSyhf6cFhW3PiAmP`</summary>

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
  "parentUuid": "d931d103-b9c8-4e1d-98e1-8dc06558bd8e",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUC96X1LUy3zc4gG5B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2bf73b6-6db0-47d6-b556-debdb3b4bf88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2DnYmZHyjB9tHdDDpfz2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 8 · 2026-05-12T00:32:10.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BSKHS9pEn6NbX95WG5ZKtu`</summary>

```json
{
  "query": "ARR submission deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2bf73b6-6db0-47d6-b556-debdb3b4bf88",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUC96X1LUy3zc4gG5B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96bb3259-b079-4886-b1be-93484c325fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2DnYmZHyjB9tHdDDpfz2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 9 · 2026-05-12T00:32:11.517Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CLQWn6JSn9iQbbHHbZgH5S`</summary>

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
  "parentUuid": "96bb3259-b079-4886-b1be-93484c325fe3",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUC96X1LUy3zc4gG5B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ab2eee3-5444-4c8a-aec0-1e906163e8ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2DnYmZHyjB9tHdDDpfz2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 10 · 2026-05-12T00:32:11.532Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VoGBPdJKT4nbKXd7win2mz`</summary>

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
  "parentUuid": "4ab2eee3-5444-4c8a-aec0-1e906163e8ea",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUC96X1LUy3zc4gG5B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00896612-cb03-4451-8df0-a7795afc64de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2DnYmZHyjB9tHdDDpfz2v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1425,
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

_source line 11 · 2026-05-12T00:32:12.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0163iquwr818AvMatZnfo9AB`</summary>

```json
{
  "query": "site:aclrollingreview.org deadlines 2026",
  "allowed_domains": [
    "aclrollingreview.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00896612-cb03-4451-8df0-a7795afc64de",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUC96X1LUy3zc4gG5B",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "431f4a6c-6182-492a-937a-2763758edaa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2DnYmZHyjB9tHdDDpfz2v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1425,
      "cache_read_input_tokens": 8933,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1425
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 285,
          "cache_read_input_tokens": 8933,
          "cache_creation_input_tokens": 1425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1425,
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

_source line 12 · 2026-05-12T00:32:13.681Z_

<details><summary>↩ Tool result · `toolu_01BSKHS9pEn6NbX95WG5ZKtu`</summary>

```text
Web search results for query: "ARR submission deadline May 2026"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, the ARR (ACL Rolling Review) submission deadline for May 2026 is May 25, 2026. This deadline is relevant for researchers submitting papers to be considered by conferences such as EMNLP 2026 and other venues that use the ARR system for peer review.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96bb3259-b079-4886-b1be-93484c325fe3",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "6cd9c2f6-f854-4c03-aaa7-4e4592a15af5",
  "sourceToolAssistantUUID": "96bb3259-b079-4886-b1be-93484c325fe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:32:15.759Z_

<details><summary>↩ Tool result · `toolu_01S3ErpUPSyhf6cFhW3PiAmP`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the information about EMNLP 2026 submission deadlines through ARR:

## EMNLP 2026 ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Important Details About the ARR 2026 May Cycle

Since the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Key Dates

Additional important dates include:
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2bf73b6-6db0-47d6-b556-debdb3b4bf88",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "5a266980-8b0c-4a23-8aa7-c2ed128a92c3",
  "sourceToolAssistantUUID": "d2bf73b6-6db0-47d6-b556-debdb3b4bf88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:32:16.305Z_

<details><summary>↩ Tool result · `toolu_0163iquwr818AvMatZnfo9AB`</summary>

```text
Web search results for query: "site:aclrollingreview.org deadlines 2026"

Links: [{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Changelog","url":"http://aclrollingreview.org/changelog"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Announcement for authors and reviewers submitting to January ARR","url":"http://aclrollingreview.org/january-arr-announcement"},{"title":"ARR Dashboard","url":"https://stats.aclrollingreview.org/"}]

Based on the search results from aclrollingreview.org, here are the 2026 deadlines I found:

The deadline for completing the registration form is January 7th 2026 EoD AoE. If they get assignments, AC checklists must be completed by Jan 18th.

Additionally, papers whose authors have not registered as reviewers or ACs or have not completed their checklists as Reviewers or ACs by the designated deadline will be automatically desk rejected.

The search results indicate that ARR now uses 10-week review cycles with the submission deadline always the 15th of the month; other dates vary due to the length of months, timing of weekends, etc.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "431f4a6c-6182-492a-937a-2763758edaa5",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "702c99d2-5f61-4ec3-a939-ba23962cea70",
  "sourceToolAssistantUUID": "431f4a6c-6182-492a-937a-2763758edaa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:32:16.746Z_

<details><summary>↩ Tool result · `toolu_01CLQWn6JSn9iQbbHHbZgH5S`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 deadlines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL ARR 2025 February | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FFebruary"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl?lang=en"}]

Based on the search results, here are the key ACL Rolling Review 2026 deadlines:

## Paper Submission Deadlines

The submission deadline for all papers to ARR is January 5, 2026.

## Author Responsibilities

All authors must complete the author registration form by January 7th 2026 EoD AoE (End of Day, Anywhere on Earth).

If authors receive reviewing assignments, reviews must be completed by February 7th, and meta-reviews by March 3rd.

## Review Availability and Commitment

ARR reviews and meta-reviews are available to authors of the January cycle by March 10, 2026. The commitment deadline to ACL 2026 is March 14, 2026.

## Incentive Program Details

The deadline for completing the author registration form is January 7th 2026 EoD AoE, and reviewer checklists must be completed by Jan 21st, with the deadline for reviews on February 7th and meta-reviews on March 3rd.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ab2eee3-5444-4c8a-aec0-1e906163e8ea",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "cba0f72c-176b-4de0-a147-432e4624bfe3",
  "sourceToolAssistantUUID": "4ab2eee3-5444-4c8a-aec0-1e906163e8ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T00:32:18.287Z_

<details><summary>↩ Tool result · `toolu_01VoGBPdJKT4nbKXd7win2mz`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Here's what I found about the EMNLP 2026 Call for Papers:

## Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Key Deadlines
The ARR submission deadline for long and short papers is May 25, 2026, with reviewer registration deadline on May 27, 2026. Meta review will be released July 30, 2026, and the EMNLP commitment deadline is August 2, 2026. Notification of acceptance is August 20, 2026, and camera-ready papers are due September 20, 2026. The main conference runs October 22-26, 2026.

## Conference Location
EMNLP 2026 will be held as a hybrid conference, physically held in Budapest, Hungary from October 24th to October 29th, 2026.

## Submission Process
Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026. Dual submissions are not allowed.

## Special Theme
The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era.

## Author Requirements
All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair. After submission, all authors must complete the author registration form by May 27, 2026.

The full call for papers is available at https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00896612-cb03-4451-8df0-a7795afc64de",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "34c899ea-a682-4ed0-bde5-e9279ec6ebcf",
  "sourceToolAssistantUUID": "00896612-cb03-4451-8df0-a7795afc64de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T00:32:21.793Z_

Let me get a couple more details by fetching the official EMNLP 2026 CFP page and the ARR dates page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c899ea-a682-4ed0-bde5-e9279ec6ebcf",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUzD26jyJnyeSNBokc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e844e4e6-4286-4ced-9745-a6bd5aafce56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7W3zMhy1P3kE6jacx69KL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 515,
      "cache_creation_input_tokens": 3715,
      "cache_read_input_tokens": 10358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3715,
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

_source line 18 · 2026-05-12T00:32:22.102Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01369CpEiqU8LKCv716aPLF1`</summary>

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
  "parentUuid": "e844e4e6-4286-4ced-9745-a6bd5aafce56",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjUzD26jyJnyeSNBokc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed0b40cb-f85e-4747-a2bc-ded42dadafaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7W3zMhy1P3kE6jacx69KL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 515,
      "cache_creation_input_tokens": 3715,
      "cache_read_input_tokens": 10358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3715,
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

### Tool result

_source line 19 · 2026-05-12T00:32:22.106Z_

<details><summary>↩ Tool result · `toolu_01369CpEiqU8LKCv716aPLF1`</summary>

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
  "parentUuid": "ed0b40cb-f85e-4747-a2bc-ded42dadafaf",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "b43c3e0b-f1d7-4cbc-af76-9973f4243351",
  "sourceToolAssistantUUID": "ed0b40cb-f85e-4747-a2bc-ded42dadafaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-12T00:32:27.643Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P3x6Ys8GRqxeoSFpXTjTPD`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all key information: 1) Does EMNLP 2026 accept short papers? 2) What are ALL the important dates/deadlines? 3) What is the ARR submission deadline? 4) What is the review cycle timeline? 5) Any details about the May 2026 ARR cycle. List everything precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b43c3e0b-f1d7-4cbc-af76-9973f4243351",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjVHDDo7CLusTStGKMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca119252-0720-46ce-871d-acd32599d9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFqpqjkhZd9Pa9gJESsKvZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 14073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-12T00:32:29.582Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T5wnCoYQUUahdxCMun5QNW`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract ALL 2026 ARR submission deadlines and review cycle dates. Specifically, what is the May 2026 submission deadline? What are all the dates in the May 2026 review cycle (submission, reviewing period, meta-review, etc.)? List every cycle for 2026 with all dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca119252-0720-46ce-871d-acd32599d9f6",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjVHDDo7CLusTStGKMt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49512d1f-ac41-4da4-80d4-eeb2afa182d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFqpqjkhZd9Pa9gJESsKvZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 14073,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 14073,
          "cache_creation_input_tokens": 1141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1141,
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

_source line 22 · 2026-05-12T00:32:32.749Z_

<details><summary>↩ Tool result · `toolu_01P3x6Ys8GRqxeoSFpXTjTPD`</summary>

```text
# EMNLP 2026 Key Information

## 1) Short Papers Acceptance
Yes, EMNLP 2026 accepts short papers alongside long papers. Both are invited for submission.

## 2) ALL Important Dates/Deadlines

| Event | Date |
|-------|------|
| ARR submission deadline | May 25, 2026 |
| Reviewer registration deadline | May 27, 2026 |
| Author response & discussion | July 7-13, 2026 |
| Meta review released | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Acceptance notification | August 20, 2026 |
| Camera-ready papers due | September 20, 2026 |
| Main Conference | October 24-29, 2026 |

**Note:** "All deadlines are 11:59PM UTC-12:00 ('anywhere on Earth')."

## 3) ARR Submission Deadline
May 25, 2026

## 4) Review Cycle Timeline
The timeline spans approximately 3 months from submission to acceptance notification: submission → review assignment → author response period → meta-review → commitment opportunity → final decisions.

## 5) May 2026 ARR Cycle Details
The May 2026 ARR cycle is significant because "ARR 2026 May submission policy for EMNLP" requires authors to declare conference commitment intentions at submission. Critically, "ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026." This binding declaration does not apply to papers reviewed in earlier ARR cycles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca119252-0720-46ce-871d-acd32599d9f6",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "999246e2-e666-47c9-869e-4337fcb1bde4",
  "sourceToolAssistantUUID": "ca119252-0720-46ce-871d-acd32599d9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T00:32:33.372Z_

<details><summary>↩ Tool result · `toolu_01T5wnCoYQUUahdxCMun5QNW`</summary>

```text
# 2026 ARR Review Cycles and Deadlines

Based on the schedule provided, here are all 2026 ARR cycles:

## May 2026 Cycle
- **Submission deadline:** May 25, 2026
- **Reviewer registration deadline:** May 27, 2026
- **Reviews due:** June 29, 2026
- **Author response period:** July 7-13, 2026
- **Meta-reviews released:** July 30, 2026
- **Cycle end:** August 2, 2026

## March 2026 Cycle
- **Submission:** March 16, 2026
- **Reviewer registration:** March 18, 2026
- **Reviews due:** April 20, 2026
- **Author response:** April 28-May 4, 2026
- **Meta-reviews released:** May 21, 2026
- **Cycle end:** May 24, 2026

## August 2026 and October 2026 Cycles
The table indicates "TBA" (to be announced) for most dates in these cycles, with only the cycle end dates specified: October 11, 2026 for August cycle and December 20, 2026 for October cycle.

The document notes that "all authors must register" as reviewers following submission, with non-compliance potentially resulting in desk rejection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49512d1f-ac41-4da4-80d4-eeb2afa182d8",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "a5c1b9a4da41f2693",
  "type": "user",
  "uuid": "47b9bf9c-c544-40b1-be6e-d6eea16d7233",
  "sourceToolAssistantUUID": "49512d1f-ac41-4da4-80d4-eeb2afa182d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T00:32:50.812Z_

Here is what I found across the official sources:

---

## 1. EMNLP 2026 ARR Submission Deadline: Confirmed May 25, 2026

Yes, the ARR submission deadline for EMNLP 2026 is **May 25, 2026** (11:59 PM UTC-12:00, "Anywhere on Earth"). This is confirmed on both the official EMNLP 2026 CFP page and the ARR dates page.

**Critical caveat for the May 2026 cycle:** Because EMNLP and AACL share the ARR May cycle, authors must explicitly select their target conference (EMNLP or AACL) at submission time. This choice is **binding** -- ARR May 2026 submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026 later. This restriction does not apply to papers reviewed in earlier ARR cycles.

## 2. Short Papers: Yes, EMNLP 2026 Accepts Short Papers

The call for papers explicitly invites both **long and short papers** featuring substantial, original, and unpublished research on empirical methods for NLP.

## 3. ARR Review Cycle for a May 2026 Submission

The full May 2026 ARR cycle timeline is:

| Milestone | Date |
|---|---|
| Submission deadline | May 25, 2026 |
| Reviewer registration deadline (all authors) | May 27, 2026 |
| Reviews due | June 29, 2026 |
| Author response & author-reviewer discussion | July 7 -- July 13, 2026 |
| Meta-reviews released | July 30, 2026 |
| Cycle end / EMNLP commitment deadline | August 2, 2026 |
| Notification of acceptance | August 20, 2026 |
| Camera-ready papers due | September 20, 2026 |
| Main conference (Budapest, Hungary) | October 24--29, 2026 |

The review cycle from submission to meta-review release spans roughly 10 weeks (May 25 to July 30). The full pipeline from submission to acceptance notification is approximately 12.5 weeks.

**Important author obligations:** All authors must register as reviewers (or serve as Area Chair / Senior Area Chair) by May 27, 2026. Papers whose authors have not registered or completed their checklists may be automatically desk-rejected.

---

Sources:
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Critical Update on Binding Conference Selection (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ARR Call for Papers](http://aclrollingreview.org/cfp)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b9bf9c-c544-40b1-be6e-d6eea16d7233",
  "isSidechain": true,
  "agentId": "a5c1b9a4da41f2693",
  "requestId": "req_011CawjW6kwzZycAako8ZSnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f370cdd-95c9-4a26-8ac9-9ab2cba96512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCTviB2TWp1EVbSeEH5HR4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1077,
      "cache_read_input_tokens": 15214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1077,
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
