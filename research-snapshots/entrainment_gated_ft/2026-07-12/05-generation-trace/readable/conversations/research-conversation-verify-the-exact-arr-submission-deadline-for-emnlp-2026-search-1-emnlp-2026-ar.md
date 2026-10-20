# Research conversation: Verify the exact ARR submission deadline for EMNLP 2026. Search: 1. "EMNLP 2026 ARR deadline May 2026" 2. "ACL Rolling R

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa41b20557312a0be.jsonl`
- **Structured JSON:** [`0e6e2db6848293662f75.json`](../../sessions/0e/0e6e2db6848293662f75.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-12T01:46:41.237Z_

Verify the exact ARR submission deadline for EMNLP 2026. Search:
1. "EMNLP 2026 ARR deadline May 2026"
2. "ACL Rolling Review May 2026 submission deadline"
3. site:2026.emnlp.org calls
4. site:aclrollingreview.org dates

I need the exact date. The proposal claims May 25, 2026. Today is May 12, 2026 — how many days remain?

Report the exact deadline date and source URL.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "2e68db18-1bc0-498b-a06f-7a7ea18c339e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:46:41.244Z_

```json
{
  "parentUuid": "2e68db18-1bc0-498b-a06f-7a7ea18c339e",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
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
  "uuid": "d587112a-f62e-42d7-bb66-80c3f9005de3",
  "timestamp": "2026-05-12T01:46:41.244Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:46:43.902Z_



I'll search for the EMNLP 2026 ARR submission deadline using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d587112a-f62e-42d7-bb66-80c3f9005de3",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011Cawq9yKcWnPRw2VnxJXNB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea479884-a4b9-494d-bf50-46662a016bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ee49bhm8eH4CxuLRri2LfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 678,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T01:46:44.034Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017WmrEcR4KACRZEstWMefWv`</summary>

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
  "parentUuid": "ea479884-a4b9-494d-bf50-46662a016bb8",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011Cawq9yKcWnPRw2VnxJXNB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f95d36e5-cacc-4768-9cb6-288e77253672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ee49bhm8eH4CxuLRri2LfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 8223,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 678
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 678,
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

_source line 5 · 2026-05-12T01:46:44.039Z_

<details><summary>↩ Tool result · `toolu_017WmrEcR4KACRZEstWMefWv`</summary>

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
  "parentUuid": "f95d36e5-cacc-4768-9cb6-288e77253672",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "b5949577-93ed-43d8-b26e-74e31f7ead06",
  "sourceToolAssistantUUID": "f95d36e5-cacc-4768-9cb6-288e77253672",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:46:46.615Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5949577-93ed-43d8-b26e-74e31f7ead06",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqABVqmaWwkAM74AYcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a381fbcf-419f-4fe1-9cfd-0f9dac7acb80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113FHGD4oJFVZFYUN5RnNTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8901,
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

_source line 7 · 2026-05-12T01:46:47.097Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JzhetU1HXuhoYk2LPVUbLE`</summary>

```json
{
  "query": "EMNLP 2026 ARR deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a381fbcf-419f-4fe1-9cfd-0f9dac7acb80",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqABVqmaWwkAM74AYcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dda1b2a-74a0-47eb-b971-c9494e4bc54f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113FHGD4oJFVZFYUN5RnNTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8901,
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

_source line 8 · 2026-05-12T01:46:47.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LY27cmH6M13ZSVhPXTZz2n`</summary>

```json
{
  "query": "ACL Rolling Review May 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dda1b2a-74a0-47eb-b971-c9494e4bc54f",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqABVqmaWwkAM74AYcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1d6479c-49f9-4b00-9214-074535d64a96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113FHGD4oJFVZFYUN5RnNTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8901,
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

_source line 9 · 2026-05-12T01:46:48.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TrT8MozYo4p1qmsmo2XjGA`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline dates",
  "allowed_domains": [
    "2026.emnlp.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1d6479c-49f9-4b00-9214-074535d64a96",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqABVqmaWwkAM74AYcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c576fbad-35a1-43a9-aa63-ff313c6ee06b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113FHGD4oJFVZFYUN5RnNTz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8901,
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

_source line 10 · 2026-05-12T01:46:49.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YUs3sA2f1oTzKFY2GLptfL`</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission deadlines dates",
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
  "parentUuid": "c576fbad-35a1-43a9-aa63-ff313c6ee06b",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqABVqmaWwkAM74AYcr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfe9ac22-4851-48b4-9dce-74a533d7cf05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113FHGD4oJFVZFYUN5RnNTz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 8901,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1416
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 273,
          "cache_read_input_tokens": 8901,
          "cache_creation_input_tokens": 1416,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1416,
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

_source line 11 · 2026-05-12T01:46:52.208Z_

<details><summary>↩ Tool result · `toolu_01JzhetU1HXuhoYk2LPVUbLE`</summary>

```text
Web search results for query: "EMNLP 2026 ARR deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, I found detailed information about the EMNLP 2026 ARR deadline in May 2026:

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

Additionally, here are some other important May 2026 deadlines related to EMNLP 2026:

- Reviewer registration deadline for all authors is May 27, 2026

An important note: Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dda1b2a-74a0-47eb-b971-c9494e4bc54f",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "83ce2477-1caf-46b9-96c5-421069d161f3",
  "sourceToolAssistantUUID": "4dda1b2a-74a0-47eb-b971-c9494e4bc54f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T01:46:52.907Z_

<details><summary>↩ Tool result · `toolu_01LY27cmH6M13ZSVhPXTZz2n`</summary>

```text
Web search results for query: "ACL Rolling Review May 2026 submission deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results, I can provide you with information about the ACL Rolling Review submission deadlines for 2026:

ACL Rolling Review switched from 8-week to 10-week review cycles starting in May 2025, which means the schedule has changed from the previous pattern of submission deadlines on the 15th of every second month.

For submissions in 2026, the submission deadline for ARR papers is January 5, 2026. There isn't a specific May 2026 submission deadline listed in the current schedule, as with 10-week cycles there are generally 5 cycles per year instead of 6.

If you're looking for details about a May 2026 ARR cycle specifically, the search results don't show a May 2026 submission deadline. The current documented deadlines focus on the January 2026 cycle and earlier cycles. You may want to check the official ACL Rolling Review dates page at aclrollingreview.org/dates for the most up-to-date schedule, as the May 2026 cycle details may not yet be finalized.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1d6479c-49f9-4b00-9214-074535d64a96",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "3063c19d-e174-4ec4-98d8-f42589fea153",
  "sourceToolAssistantUUID": "a1d6479c-49f9-4b00-9214-074535d64a96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T01:46:54.311Z_

<details><summary>↩ Tool result · `toolu_01YUs3sA2f1oTzKFY2GLptfL`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 submission deadlines dates"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/some-important-dates/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Six Week Cycles – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/six-week-cycles/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission deadlines:

The ACL Peer Review Committee recommended switching to 10-week cycles, which will be in action starting in May 2025. This change affects the schedule going forward.

ACL 2026 is listed as a main *ACL conference using ARR exclusively for paper submissions.

However, the search results don't provide a comprehensive table of all 2026 submission deadlines. The results reference a dates page that should contain this information, but the specific 2026 deadline dates aren't fully displayed in the search results. For the most detailed and up-to-date list of all 2026 submission deadlines, you would need to visit the official ACL Rolling Review dates page at http://aclrollingreview.org/dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfe9ac22-4851-48b4-9dce-74a533d7cf05",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "febedd8d-c775-47a8-8702-bfecb869f8b1",
  "sourceToolAssistantUUID": "cfe9ac22-4851-48b4-9dce-74a533d7cf05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T01:46:54.569Z_

<details><summary>↩ Tool result · `toolu_01TrT8MozYo4p1qmsmo2XjGA`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline dates"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

Based on the search results, here are the EMNLP 2026 submission deadline dates:

**Main Conference Papers:**
Papers must be submitted, at latest, by the ARR 2026 May cycle. Additionally, after submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

**Industry Track:**
Paper submission deadline: June 16, 2026 (11:59 PM UTC-12:00, AoE)

**General Note:**
All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

The main conference will be held October 24–29 in Budapest, Hungary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c576fbad-35a1-43a9-aa63-ff313c6ee06b",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "0102b5fc-e210-485c-90e7-44e66b18e2b0",
  "sourceToolAssistantUUID": "c576fbad-35a1-43a9-aa63-ff313c6ee06b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T01:46:58.884Z_

Let me now fetch the official pages to confirm the exact date and get the precise source URL.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0102b5fc-e210-485c-90e7-44e66b18e2b0",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqAxEQFQd6j5FiWXZ6g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2df1bd77-c088-479a-ace6-6ef2f547b2b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECygHjwdeXkTRABt5ycEcK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 690,
      "cache_creation_input_tokens": 2419,
      "cache_read_input_tokens": 10317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2419,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T01:46:59.150Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0119puFdDvZCH7Ag2iNYhFBG`</summary>

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
  "parentUuid": "2df1bd77-c088-479a-ace6-6ef2f547b2b0",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqAxEQFQd6j5FiWXZ6g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "843a5321-97ec-4c72-8982-32e7cc153ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ECygHjwdeXkTRABt5ycEcK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 690,
      "cache_creation_input_tokens": 2419,
      "cache_read_input_tokens": 10317,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 690,
          "output_tokens": 96,
          "cache_read_input_tokens": 10317,
          "cache_creation_input_tokens": 2419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2419,
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

_source line 17 · 2026-05-12T01:46:59.152Z_

<details><summary>↩ Tool result · `toolu_0119puFdDvZCH7Ag2iNYhFBG`</summary>

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
  "parentUuid": "843a5321-97ec-4c72-8982-32e7cc153ca9",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "b0f2861f-ecd5-48ba-8bfa-1c099edff556",
  "sourceToolAssistantUUID": "843a5321-97ec-4c72-8982-32e7cc153ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T01:47:05.250Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KWwNeHj2Gc5TQ1awVCPuww`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the exact ARR submission deadline date for EMNLP 2026 main conference papers. Include any details about the May 2026 ARR cycle deadline, including the exact date and timezone. List all important dates mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0f2861f-ecd5-48ba-8bfa-1c099edff556",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqBJSq2KGhohtUYWo7M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f4eb021-37fb-4909-99ea-14a5b31328f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Rn6z2KepTqE86dDCsUcZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1304,
      "cache_read_input_tokens": 12736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1304,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T01:47:06.018Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01922BQVrAEPQnRZHj3LnVPY`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract the exact submission deadline date for the ARR May 2026 cycle. List all 2026 submission cycle dates with their exact deadlines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f4eb021-37fb-4909-99ea-14a5b31328f1",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqBJSq2KGhohtUYWo7M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6bba8090-4adf-4368-9aec-9bee2de63032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Rn6z2KepTqE86dDCsUcZg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1304,
      "cache_read_input_tokens": 12736,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1304
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 232,
          "cache_read_input_tokens": 12736,
          "cache_creation_input_tokens": 1304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1304,
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

_source line 20 · 2026-05-12T01:47:09.043Z_

<details><summary>↩ Tool result · `toolu_01922BQVrAEPQnRZHj3LnVPY`</summary>

```text
# ARR 2026 Submission Deadlines

## May 2026 Cycle Submission Deadline

The exact submission deadline for the ARR May 2026 cycle is **May 25, 2026**.

## All 2026 Submission Cycle Dates

Based on the scheduling table provided, here are all submission deadlines for 2026:

| Cycle | Submission Deadline |
|-------|-------------------|
| March 2026 | March 16, 2026 |
| May 2026 | May 25, 2026 |
| August 2026 | August 3, 2026 |
| October 2026 | October 12, 2026 |

The document notes that "in addition to submission and author response dates, the following action points are now listed, as non-compliance may result in desk rejection or sanctions," including reviewer registration requirements for all authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bba8090-4adf-4368-9aec-9bee2de63032",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "a5e4e862-b256-4756-9eef-2a29047e4534",
  "sourceToolAssistantUUID": "6bba8090-4adf-4368-9aec-9bee2de63032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T01:47:09.096Z_

<details><summary>↩ Tool result · `toolu_01KWwNeHj2Gc5TQ1awVCPuww`</summary>

```text
# EMNLP 2026 ARR Submission Deadline

**Exact ARR Submission Deadline:**
"May 25, 2026" with the note that "All deadlines are 11:59PM UTC-12:00 ('anywhere on Earth')."

This represents the submission window for both long and short papers to the ARR 2026 May cycle, which feeds into EMNLP 2026.

## All Important Dates for EMNLP 2026:

| Event | Date |
|-------|------|
| ARR submission deadline | May 25, 2026 |
| Reviewer registration deadline | May 27, 2026 |
| Author response/discussion period | July 7–13, 2026 |
| Meta review released | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Acceptance notification | August 20, 2026 |
| Camera-ready papers due | September 20, 2026 |
| Main Conference | October 24–29, 2026 |

**Note:** "All deadlines are 11:59PM UTC-12:00" representing the earliest possible timezone globally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f4eb021-37fb-4909-99ea-14a5b31328f1",
  "isSidechain": true,
  "promptId": "390bb392-ae11-4ba9-9889-d3f1d608da4a",
  "agentId": "aa41b20557312a0be",
  "type": "user",
  "uuid": "713bef98-f08b-4013-b000-ba4397f3df5e",
  "sourceToolAssistantUUID": "7f4eb021-37fb-4909-99ea-14a5b31328f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T01:47:19.138Z_

Here are the findings:

---

**The proposal's claim of May 25, 2026 is correct.**

**Exact deadline:** May 25, 2026, at 11:59 PM UTC-12:00 (Anywhere on Earth / AoE)

**Days remaining:** From today (May 12, 2026) to May 25, 2026 = **13 days remain.**

**Additional critical date:** All authors must also complete the reviewer registration form by May 27, 2026 (EoD AoE), or the submission may be desk-rejected.

**Important note:** Since EMNLP 2026 and AACL share the ARR May 2026 cycle, authors must explicitly select a target conference at submission time, and this choice is binding.

**Source URLs:**
- [Call for Main Conference Papers -- EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/) (official conference page)
- [Dates and Venues -- ACL Rolling Review](https://aclrollingreview.org/dates) (official ARR schedule confirming May 25, 2026)
- [EMNLP 2026 on X -- First Call for Papers announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 on X -- Critical update about EMNLP/AACL shared cycle](https://x.com/emnlpmeeting/status/2047754845919031450)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "713bef98-f08b-4013-b000-ba4397f3df5e",
  "isSidechain": true,
  "agentId": "aa41b20557312a0be",
  "requestId": "req_011CawqC2Niv1ymNWZaFzG5x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0209027c-2dc1-4902-9b1c-197acf1bfd8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dded2294-72af-403c-8e91-afcdfee4dea9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2omj6LzDHssV8M8H6Xkhd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 239,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 14040,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 654
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 239,
          "output_tokens": 374,
          "cache_read_input_tokens": 14040,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 654,
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
