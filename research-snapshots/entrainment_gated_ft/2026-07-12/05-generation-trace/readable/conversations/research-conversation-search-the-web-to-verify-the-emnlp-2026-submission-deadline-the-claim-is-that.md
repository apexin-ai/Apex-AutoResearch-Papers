# Research conversation: Search the web to verify the EMNLP 2026 submission deadline. The claim is that the ARR submission deadline is May 25, 20

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a20ed2cc207789ad3.jsonl`
- **Structured JSON:** [`91c73560c1f5c8e08172.json`](../../sessions/91/91c73560c1f5c8e08172.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-10T18:16:37.574Z_

Search the web to verify the EMNLP 2026 submission deadline. The claim is that the ARR submission deadline is May 25, 2026. Search for:
1. "EMNLP 2026 submission deadline"
2. "ACL Rolling Review ARR 2026 May deadline"
3. "EMNLP 2026 call for papers"

Also check: is May 25, 2026 an ARR cycle deadline? How does ARR submission work for EMNLP 2026?

Report all details found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "7dd2a854-f7ea-4410-a336-44cd8f2022f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:16:37.575Z_

```json
{
  "parentUuid": "7dd2a854-f7ea-4410-a336-44cd8f2022f1",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
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
  "uuid": "6989cfd2-a0f6-48ee-91c9-b09c02edf196",
  "timestamp": "2026-05-10T18:16:37.575Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:16:39.735Z_



I'll search the web for all the requested information about EMNLP 2026 and ARR deadlines. Let me start by loading the WebSearch tool and then running the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6989cfd2-a0f6-48ee-91c9-b09c02edf196",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM2VqfjLYxeRd5QKTUe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b257c17-02fa-496f-bad8-01f4b486c740",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvonH8Uor9h1xrenEqdPV5",
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
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T18:16:40.326Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QSrugzQbev3ChSvnbZvU4t`</summary>

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
  "parentUuid": "0b257c17-02fa-496f-bad8-01f4b486c740",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM2VqfjLYxeRd5QKTUe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6d45cf2-9eab-46d6-8ef4-2e4357075e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvonH8Uor9h1xrenEqdPV5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 8223,
      "output_tokens": 122,
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
          "output_tokens": 122,
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

_source line 5 · 2026-05-10T18:16:40.332Z_

<details><summary>↩ Tool result · `toolu_01QSrugzQbev3ChSvnbZvU4t`</summary>

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
  "parentUuid": "a6d45cf2-9eab-46d6-8ef4-2e4357075e4d",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "61479124-44b0-4f43-b6ff-1277eb6e64e8",
  "sourceToolAssistantUUID": "a6d45cf2-9eab-46d6-8ef4-2e4357075e4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:16:42.871Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61479124-44b0-4f43-b6ff-1277eb6e64e8",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM2hqymjZ2xvUdQTqrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eef81222-d232-432b-8cc0-097fa3b69bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUCxMH2KwFt36zx9svsCv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1931,
      "cache_read_input_tokens": 8901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1931,
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

_source line 7 · 2026-05-10T18:16:43.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FfLPxbxU1YLM7ELeaKaWjE`</summary>

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
  "parentUuid": "eef81222-d232-432b-8cc0-097fa3b69bbc",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM2hqymjZ2xvUdQTqrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92e50f7b-11b0-44e3-822f-1d1ec4c7d052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUCxMH2KwFt36zx9svsCv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1931,
      "cache_read_input_tokens": 8901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1931,
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

_source line 8 · 2026-05-10T18:16:43.824Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XuURGLAFvDTSoXW2eBGA5D`</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 May deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92e50f7b-11b0-44e3-822f-1d1ec4c7d052",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM2hqymjZ2xvUdQTqrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "792365e6-5b3a-4ca6-a861-381bdc7aea96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUCxMH2KwFt36zx9svsCv9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1931,
      "cache_read_input_tokens": 8901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1931,
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

_source line 9 · 2026-05-10T18:16:44.168Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BfQW21s5KMuR85m9y7Kd35`</summary>

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
  "parentUuid": "792365e6-5b3a-4ca6-a861-381bdc7aea96",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM2hqymjZ2xvUdQTqrP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f99e37f-13d9-49ab-aae8-93e0f3ea8d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUCxMH2KwFt36zx9svsCv9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1931,
      "cache_read_input_tokens": 8901,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1931
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 8901,
          "cache_creation_input_tokens": 1931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1931,
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

_source line 10 · 2026-05-10T18:16:49.204Z_

<details><summary>↩ Tool result · `toolu_01XuURGLAFvDTSoXW2eBGA5D`</summary>

```text
Web search results for query: "ACL Rolling Review ARR 2026 May deadline"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"}]

Based on the search results, here's what I found about ACL Rolling Review (ARR) and May 2026 deadlines:

## ARR 2026 Schedule Changes

ACL switched from 8-week to 10-week review cycles, with the new schedule taking effect starting in May 2025. This means there will generally be 5 cycles a year instead of 6.

## Recent Deadlines (January 2026 Cycle)

While specific May 2026 deadlines aren't explicitly listed in the search results, the available information shows that the submission deadline for papers is January 5, 2026 for the January cycle. For reviewing obligations in this cycle, reviewer checklists must be completed by January 21st, with the deadline for reviews being February 7th and meta-reviews March 3rd.

The search results don't contain specific information about a May 2026 ARR submission deadline. If you're looking for details about the May 2026 cycle specifically, you may want to check the official ACL Rolling Review website at aclrollingreview.org/dates for the most up-to-date schedule.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "792365e6-5b3a-4ca6-a861-381bdc7aea96",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "6a89d2f3-8b71-4b0e-a8b9-79264c091b25",
  "sourceToolAssistantUUID": "792365e6-5b3a-4ca6-a861-381bdc7aea96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T18:16:50.744Z_

<details><summary>↩ Tool result · `toolu_01FfLPxbxU1YLM7ELeaKaWjE`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, EMNLP 2026 uses the ACL Rolling Review (ARR) process exclusively. This means there is no single fixed submission deadline for EMNLP 2026 itself. Instead, ARR runs review cycles with submission deadlines on the 15th of every second month (as of the May 2025 cycle, ARR switched to 10-week cycles).

Authors can submit their papers to any upcoming ARR cycle, and once authors have reviews they may choose to commit their paper and reviews to a publication venue like EMNLP 2026. EMNLP 2026 will be held in Budapest, Hungary from October 24th to October 29th, 2026.

For the most current and specific submission deadlines, you should check the official EMNLP 2026 website at https://2026.emnlp.org/ or the ACL Rolling Review website for the exact ARR cycle deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92e50f7b-11b0-44e3-822f-1d1ec4c7d052",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "ff5ff4f8-a479-4632-8c40-c3ec57b1559a",
  "sourceToolAssistantUUID": "92e50f7b-11b0-44e3-822f-1d1ec4c7d052",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T18:16:52.294Z_

<details><summary>↩ Tool result · `toolu_01BfQW21s5KMuR85m9y7Kd35`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the information about the EMNLP 2026 Call for Papers:

## Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. The conference will be held as a hybrid conference, and physically held in Budapest, Hungary from October 24-29, 2026.

## Key Deadlines
ARR submission deadline (long & short papers): May 25, 2026; Reviewer registration deadline for ALL authors: May 27, 2026; Author response and author-reviewer discussion: July 7 - July 13, 2026; Meta review released: July 30, 2026; EMNLP commitment deadline: August 2, 2026; Notification of acceptance (long & short papers): August 20, 2026; Camera-ready papers due (long & short): September 20, 2026.

## Submission Process
Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026: i.e., ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

## Special Theme
The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era.

## Important Policies
There is growing concern in the community regarding unethical paper submissions, including thinly sliced contributions, submissions with hallucinated citations, and entirely AI-generated papers. EMNLP will take actions against such submissions, as well as submissions that violate the ACL Policy on Publication Ethics. Such submissions may be desk rejected, and all authors involved in the submission may be ineligible to commit their paper(s) to EMNLP 2026 and EMNLP 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f99e37f-13d9-49ab-aae8-93e0f3ea8d92",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "7d104bf1-9fbf-4164-b5c0-536e32e01acf",
  "sourceToolAssistantUUID": "1f99e37f-13d9-49ab-aae8-93e0f3ea8d92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T18:16:55.368Z_

Good, I found strong results. Let me now fetch the official EMNLP 2026 call for papers page and the ARR dates page for full details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d104bf1-9fbf-4164-b5c0-536e32e01acf",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM3amcNtonwcNRkXnkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a3d91b9-3be8-42b2-add5-ea04d8660732",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gt82Yik69UrcegU5U5JV9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2788,
      "cache_read_input_tokens": 10832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2788,
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

_source line 14 · 2026-05-10T18:16:57.735Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016dzQrudCQj4fyXQcXAr3sS`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all important dates and deadlines, especially the ARR submission deadline, commitment deadline, notification dates, and camera-ready deadline. Also extract details about how ARR submission works for EMNLP 2026, including any binding declaration requirements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a3d91b9-3be8-42b2-add5-ea04d8660732",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM3amcNtonwcNRkXnkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dee4d81c-c1d9-4897-be15-40434129ca66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gt82Yik69UrcegU5U5JV9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2788,
      "cache_read_input_tokens": 10832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2788,
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

_source line 15 · 2026-05-10T18:16:59.677Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RbCtsWCU5RM3jRSuYa8BEV`</summary>

```json
{
  "url": "http://aclrollingreview.org/dates",
  "prompt": "List all ARR cycle deadlines for 2026, especially any May 2026 deadline. What is the submission deadline for the May 2026 ARR cycle? List all cycles and their dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee4d81c-c1d9-4897-be15-40434129ca66",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM3amcNtonwcNRkXnkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b29cf13-19c8-4ae5-84a0-3df58589bc4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gt82Yik69UrcegU5U5JV9U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2788,
      "cache_read_input_tokens": 10832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2788,
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

_source line 16 · 2026-05-10T18:17:00.302Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014J95Kyy7AeP4GLCdaqHRgx`</summary>

```json
{
  "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26",
  "prompt": "Extract all EMNLP 2026 deadlines and dates listed on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b29cf13-19c8-4ae5-84a0-3df58589bc4b",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM3amcNtonwcNRkXnkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53b5f551-6728-4fa8-9f62-1a6f4550e348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gt82Yik69UrcegU5U5JV9U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2788,
      "cache_read_input_tokens": 10832,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 374,
          "cache_read_input_tokens": 10832,
          "cache_creation_input_tokens": 2788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2788,
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

_source line 17 · 2026-05-10T18:17:03.523Z_

<details><summary>↩ Tool result · `toolu_014J95Kyy7AeP4GLCdaqHRgx`</summary>

```text
Based on the web page content provided, **no EMNLP 2026 deadlines or dates are listed**. 

The page shows a template structure for an AI Conference Deadlines website by Papers With Code, but it contains only placeholder elements (icons, labels like "Deadline in timezone," "Accepted Papers") without any actual conference data populated. No specific conferences or their deadlines are mentioned in the content shown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53b5f551-6728-4fa8-9f62-1a6f4550e348",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "56236888-f8b8-4474-aac2-ff3a84776742",
  "sourceToolAssistantUUID": "53b5f551-6728-4fa8-9f62-1a6f4550e348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T18:17:03.740Z_

<details><summary>↩ Tool result · `toolu_01RbCtsWCU5RM3jRSuYa8BEV`</summary>

```text
# ARR 2026 Cycle Deadlines

## May 2026 Submission Deadline
The submission deadline for the May 2026 ARR cycle is **May 25, 2026**.

## All 2026 ARR Cycles and Key Dates

| Cycle | Submission | Reviewer Registration | Reviews Due | Author Response | Meta-reviews Release | Cycle End |
|-------|-----------|----------------------|-------------|-----------------|-------------------|-----------|
| March 2026 | March 16 | March 18 | April 20 | April 28-May 4 | May 21 | May 24 |
| May 2026 | May 25 | May 27 | June 29 | July 7-July 13 | July 30 | August 2 |
| August 2026 | August 3 | TBA | TBA | TBA | TBA | October 11 |
| October 2026 | October 12 | TBA | TBA | TBA | TBA | December 20 |

## Publication Venue Commitments for 2026

The document indicates that "EMNLP 2026" has a final ARR submission date of "May 25, 2026" and a commitment deadline of August 2, 2026. AACL 2026 shares the same submission deadline but has a later commitment date of August 26, 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b29cf13-19c8-4ae5-84a0-3df58589bc4b",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "95326aaf-ec9f-4dd0-a598-732f690c79de",
  "sourceToolAssistantUUID": "8b29cf13-19c8-4ae5-84a0-3df58589bc4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T18:17:04.514Z_

<details><summary>↩ Tool result · `toolu_016dzQrudCQj4fyXQcXAr3sS`</summary>

```text
# EMNLP 2026 Key Dates and ARR Submission Details

## Important Deadlines

| Event | Date |
|-------|------|
| ARR submission deadline | May 25, 2026 |
| Reviewer registration deadline | May 27, 2026 |
| Author response/discussion period | July 7-13, 2026 |
| Meta review released | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Acceptance notification | August 20, 2026 |
| Camera-ready papers due | September 20, 2026 |
| Main Conference | October 24-29, 2026 |

**Note:** "All deadlines are 11:59PM UTC-12:00 ('anywhere on Earth')."

## ARR Submission Process for EMNLP 2026

The conference uses a two-stage review system where authors first submit to ACL Rolling Review, then commit reviewed papers to EMNLP.

### Critical Binding Declaration Requirement

A significant policy change applies to May 2026 submissions: "ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026." This venue selection at submission time is binding for EMNLP specifically, distinguishing it from earlier ARR cycles, which retain full flexibility.

### Commitment Restrictions

During the commitment phase, "modification of the author list...is not allowed," though reordering authors remains permitted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dee4d81c-c1d9-4897-be15-40434129ca66",
  "isSidechain": true,
  "promptId": "81db8023-9f36-41d7-a17a-082d964bf183",
  "agentId": "a20ed2cc207789ad3",
  "type": "user",
  "uuid": "bd0f656f-599c-4586-b16d-d8ef8e183720",
  "sourceToolAssistantUUID": "dee4d81c-c1d9-4897-be15-40434129ca66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T18:17:29.743Z_

I now have comprehensive information. Here is the full report.

---

## EMNLP 2026 Submission Deadline Verification

### Claim Verified: The ARR submission deadline of May 25, 2026 is CONFIRMED.

The official EMNLP 2026 Call for Papers and the ACL Rolling Review dates page both confirm that **May 25, 2026** is the ARR submission deadline for EMNLP 2026. The EMNLP 2026 Twitter/X account also announced this date explicitly.

---

### All Key Dates for EMNLP 2026

| Milestone | Date |
|---|---|
| ARR Submission Deadline (long & short papers) | **May 25, 2026** |
| Reviewer Registration Deadline (for ALL authors) | May 27, 2026 |
| Reviews Due | June 29, 2026 |
| Author Response & Author-Reviewer Discussion | July 7 -- July 13, 2026 |
| Meta-reviews Released | July 30, 2026 |
| EMNLP Commitment Deadline | August 2, 2026 |
| Notification of Acceptance | August 20, 2026 |
| Camera-Ready Papers Due | September 20, 2026 |
| Main Conference (Budapest, Hungary) | October 24 -- 29, 2026 |

All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

---

### Is May 25, 2026 an ARR Cycle Deadline?

Yes. May 25, 2026 is the official submission deadline for the **May 2026 ARR cycle**. The ARR switched from 8-week to 10-week review cycles starting in May 2025, so there are roughly 5 cycles per year. The 2026 ARR cycles are:

| ARR Cycle | Submission Deadline | Cycle End |
|---|---|---|
| March 2026 | March 16 | May 24 |
| **May 2026** | **May 25** | **August 2** |
| August 2026 | August 3 | October 11 |
| October 2026 | October 12 | December 20 |

---

### How ARR Submission Works for EMNLP 2026

EMNLP 2026 uses a **two-stage process** through ACL Rolling Review:

1. **Stage 1 -- ARR Submission:** Authors submit their paper to the May 2026 ARR cycle by May 25, 2026. The paper goes through the standard ARR review process (reviews, author response, meta-reviews).

2. **Stage 2 -- Commitment to EMNLP:** Once reviews are complete, authors "commit" their reviewed paper to EMNLP 2026 by the commitment deadline of August 2, 2026.

**Critical policy for EMNLP 2026 -- Binding Venue Declaration:** Because the May 2026 ARR cycle is shared with two conferences (EMNLP 2026 and AACL 2026), authors must **explicitly declare at submission time** which conference they intend to commit to. This declaration is **binding for EMNLP**: ARR May 2026 submissions that do not select EMNLP 2026 during submission will NOT be able to commit to EMNLP 2026 later. (However, AACL 2026 retains flexibility -- its commitment deadline is August 26, 2026.)

Other important policies:
- Modification of the author list between submission and commitment is not allowed (though reordering is permitted).
- EMNLP 2026 warns against unethical submissions (thinly sliced contributions, hallucinated citations, entirely AI-generated papers), which may result in desk rejection and a ban from committing to EMNLP 2026 and EMNLP 2027.

---

### Summary

The claim that the ARR submission deadline is **May 25, 2026** is **correct and verified** across multiple official sources. This is the deadline for the May 2026 ARR cycle, which feeds into EMNLP 2026 (commitment deadline August 2, 2026). Authors must remember to declare EMNLP as their target venue at submission time, as this choice is binding.

Sources:
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Rolling Review -- Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 Official Twitter/X Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [2026 *ACL Conference Dates (Computational Linguistics)](https://submissions.cljournal.org/index.php/cljournal/announcement/view/14)
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd0f656f-599c-4586-b16d-d8ef8e183720",
  "isSidechain": true,
  "agentId": "a20ed2cc207789ad3",
  "requestId": "req_011CauM4V2rTvEvRGTSsxdnE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39564af8-b689-40e7-8072-fe9355f60e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78549138-104c-475b-b6d5-c16ae158c3be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QcYrwqcBNoarVTawypNePx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 479,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 13620,
      "output_tokens": 1228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 479,
          "output_tokens": 1228,
          "cache_read_input_tokens": 13620,
          "cache_creation_input_tokens": 874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 874,
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
