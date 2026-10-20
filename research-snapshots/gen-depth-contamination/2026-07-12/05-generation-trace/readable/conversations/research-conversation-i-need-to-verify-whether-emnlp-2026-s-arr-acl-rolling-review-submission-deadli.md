# Research conversation: I need to verify whether EMNLP 2026's ARR (ACL Rolling Review) submission deadline is May 25, 2026. Search for: 1. "EMNL

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a0bac6764b0f3f00b.jsonl`
- **Structured JSON:** [`7e679f63972f13f70c15.json`](../../sessions/7e/7e679f63972f13f70c15.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-12T00:15:18.593Z_

I need to verify whether EMNLP 2026's ARR (ACL Rolling Review) submission deadline is May 25, 2026.

Search for:
1. "EMNLP 2026 submission deadline"
2. "ARR 2026 May deadline" 
3. "ACL Rolling Review 2026 deadlines"
4. "EMNLP 2026 call for papers"

I need to confirm:
- Is the ARR submission deadline for EMNLP 2026 actually May 25, 2026?
- What is the commitment deadline for EMNLP 2026?
- Are there short paper tracks at EMNLP 2026?

Report what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "7d6fe51c-3354-4683-9a06-82a38bfa7bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:15:18.595Z_

```json
{
  "parentUuid": "7d6fe51c-3354-4683-9a06-82a38bfa7bb9",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
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
  "uuid": "a112bf0a-13a8-41d5-9d8f-89a9f8fc5318",
  "timestamp": "2026-05-12T00:15:18.595Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:15:24.002Z_



I'll search for the EMNLP 2026 and ARR deadline information across multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a112bf0a-13a8-41d5-9d8f-89a9f8fc5318",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiBpZkZVM7yU7887Kwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14b9e2ac-23a1-46e4-bc61-640dbcf6d90d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PBuMKzoScbG5ybd1hpv4p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 719,
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

_source line 4 · 2026-05-12T00:15:24.304Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PpqMftQkSpuHyrt5wq8JpP`</summary>

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
  "parentUuid": "14b9e2ac-23a1-46e4-bc61-640dbcf6d90d",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiBpZkZVM7yU7887Kwf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7446aa49-a010-4a03-807b-6e22837eb385",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018PBuMKzoScbG5ybd1hpv4p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 8223,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 719
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 719,
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

_source line 5 · 2026-05-12T00:15:24.306Z_

<details><summary>↩ Tool result · `toolu_01PpqMftQkSpuHyrt5wq8JpP`</summary>

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
  "parentUuid": "7446aa49-a010-4a03-807b-6e22837eb385",
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "d87013d1-765a-4a08-b87e-ab50251fe8cc",
  "sourceToolAssistantUUID": "7446aa49-a010-4a03-807b-6e22837eb385",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:15:26.812Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d87013d1-765a-4a08-b87e-ab50251fe8cc",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiCFBqgs2n8A1v8Ta7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2aafb0f0-02e8-4447-b77d-9ad8d1e3a792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXEkKQcemYU617ofhMLQbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 7 · 2026-05-12T00:15:27.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013Q5K6t5WMd4TGPCYrgAiuE`</summary>

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
  "parentUuid": "2aafb0f0-02e8-4447-b77d-9ad8d1e3a792",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiCFBqgs2n8A1v8Ta7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdacad8a-d3ac-498b-bee3-3065df2651ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXEkKQcemYU617ofhMLQbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 8 · 2026-05-12T00:15:27.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GpskmvTAFHUKhnzrzp5ZtU`</summary>

```json
{
  "query": "ARR 2026 May deadline ACL Rolling Review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdacad8a-d3ac-498b-bee3-3065df2651ec",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiCFBqgs2n8A1v8Ta7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44575a5d-0123-4de6-8527-2fcbf55056aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXEkKQcemYU617ofhMLQbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 9 · 2026-05-12T00:15:28.229Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017233zikmG9WXfvw5H5FkuJ`</summary>

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
  "parentUuid": "44575a5d-0123-4de6-8527-2fcbf55056aa",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiCFBqgs2n8A1v8Ta7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59967276-60d6-4520-b448-41b9dbf84b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXEkKQcemYU617ofhMLQbS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1419,
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

_source line 10 · 2026-05-12T00:15:28.351Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KF1ZRHiTYg1fDJZXoEmhgP`</summary>

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
  "parentUuid": "59967276-60d6-4520-b448-41b9dbf84b36",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiCFBqgs2n8A1v8Ta7n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2528965c-d0d4-40e6-adcf-d1e1a5abc749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXEkKQcemYU617ofhMLQbS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 8942,
      "output_tokens": 210,
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
          "output_tokens": 210,
          "cache_read_input_tokens": 8942,
          "cache_creation_input_tokens": 1419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1419,
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

_source line 11 · 2026-05-12T00:15:31.581Z_

<details><summary>↩ Tool result · `toolu_013Q5K6t5WMd4TGPCYrgAiuE`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the submission deadline information for EMNLP 2026:

The ARR submission deadline for long and short papers at EMNLP 2026 is May 25, 2026.

Additionally, the reviewer registration deadline for all authors is May 27, 2026.

The EMNLP 2026 conference will be held in Budapest, Hungary from October 24th to October 29th, 2026.

It's important to note that papers can be submitted to ARR, with the EMNLP commitment deadline being August 2, 2026, and notification of acceptance on August 20, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdacad8a-d3ac-498b-bee3-3065df2651ec",
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "d6c90441-4e17-4fff-b6b8-175cb079a322",
  "sourceToolAssistantUUID": "bdacad8a-d3ac-498b-bee3-3065df2651ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:15:32.294Z_

<details><summary>↩ Tool result · `toolu_01GpskmvTAFHUKhnzrzp5ZtU`</summary>

```text
Web search results for query: "ARR 2026 May deadline ACL Rolling Review"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results, here's information about the ARR 2026 May deadline for ACL Rolling Review:

The 10-week cycle schedule started in May 2025, and this means there are generally 5 cycles a year instead of 6.

While the search results confirm that there is an ACL ARR 2026 May cycle, the specific deadline details for the May 2026 submission are not fully displayed in the search results I retrieved. However, the submission deadline is always the 15th of the month for ARR cycles, so the May 2026 deadline would likely follow this pattern.

For the most current and detailed information about the May 2026 ARR cycle submission deadline and other key dates, I recommend checking the official ACL Rolling Review dates page at aclrollingreview.org/dates or the OpenReview page for the 2026 May cycle.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44575a5d-0123-4de6-8527-2fcbf55056aa",
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "b4fe69e6-f089-441d-a1d8-0cadc77639ed",
  "sourceToolAssistantUUID": "44575a5d-0123-4de6-8527-2fcbf55056aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:15:33.585Z_

<details><summary>↩ Tool result · `toolu_017233zikmG9WXfvw5H5FkuJ`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 deadlines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL ARR 2025 February | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FFebruary"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl?lang=en"}]

Based on the search results, here are the key ACL Rolling Review 2026 deadlines:

## Submission and Review Deadlines

The submission deadline for papers to ARR is January 5, 2026. ARR reviews and meta-reviews will be available to authors by March 10, 2026.

## Author Registration and Review Responsibilities

All authors must complete the author registration form by January 7th 2026 EoD AoE. If authors receive assignments, reviews must be completed by February 7th, and meta-reviews by March 3rd.

## Conference Commitment

ARR reviews will be available March 9, 2026, with a commitment deadline for ACL 2026 of March 14, 2026.

The new 10-week review cycle schedule started in May 2025, which means there are generally 5 cycles per year instead of the previous 6, allowing for more reasonable review timelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59967276-60d6-4520-b448-41b9dbf84b36",
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "59681316-3a2c-49b6-9f22-19623ef79288",
  "sourceToolAssistantUUID": "59967276-60d6-4520-b448-41b9dbf84b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:15:35.175Z_

<details><summary>↩ Tool result · `toolu_01KF1ZRHiTYg1fDJZXoEmhgP`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's the information about the EMNLP 2026 Call for Papers:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Key Deadlines

The ARR submission deadline for long & short papers is May 25, 2026, with the EMNLP commitment deadline on August 2, 2026, and notification of acceptance on August 20, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Submission Process

Authors will need to explicitly declare which conference they intend to commit to at submission time, as the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL). This choice will be binding for EMNLP 2026.

## Conference Location and Dates

EMNLP 2026 will be held as a hybrid conference, and physically held in Budapest, Hungary from October 24th to October 29th, 2026.

## Special Theme

The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era.

For the complete call for papers, you can visit the official EMNLP 2026 website at https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2528965c-d0d4-40e6-adcf-d1e1a5abc749",
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "f60421c9-fa50-40ab-9f66-d0ebe1183d0e",
  "sourceToolAssistantUUID": "2528965c-d0d4-40e6-adcf-d1e1a5abc749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T00:15:38.518Z_

Let me get a few more details on the specific deadlines and short paper tracks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f60421c9-fa50-40ab-9f66-d0ebe1183d0e",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiD3V9y7xdgzMGroDBm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39ef358e-e67e-4d5e-ad75-6ca5e56d1aad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZAYjXHp88RZzhVbE7VvUr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3452,
      "cache_read_input_tokens": 10361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3452,
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

_source line 16 · 2026-05-12T00:15:39.137Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X6VBKH57qeRvoroVFNsTbv`</summary>

```json
{
  "query": "EMNLP 2026 short paper track commitment deadline August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39ef358e-e67e-4d5e-ad75-6ca5e56d1aad",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiD3V9y7xdgzMGroDBm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "122b1c55-f375-487c-b48a-a9a9d10169a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZAYjXHp88RZzhVbE7VvUr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3452,
      "cache_read_input_tokens": 10361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3452,
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

_source line 17 · 2026-05-12T00:15:39.333Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B3KurMkUGh94FS3afLEmH6`</summary>

```json
{
  "query": "site:2026.emnlp.org calls main conference papers deadlines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "122b1c55-f375-487c-b48a-a9a9d10169a3",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiD3V9y7xdgzMGroDBm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe803d45-5b39-4105-bd58-4c98526a8e37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZAYjXHp88RZzhVbE7VvUr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3452,
      "cache_read_input_tokens": 10361,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3452
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 10361,
          "cache_creation_input_tokens": 3452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3452,
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

_source line 18 · 2026-05-12T00:15:42.472Z_

<details><summary>↩ Tool result · `toolu_01X6VBKH57qeRvoroVFNsTbv`</summary>

```text
Web search results for query: "EMNLP 2026 short paper track commitment deadline August 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"}]

Based on the search results, the EMNLP 2026 commitment deadline for both long and short papers is August 2, 2026. This is the deadline by which authors must decide whether to commit their papers that have received reviews and a meta-review from ACL Rolling Review (ARR) to EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "122b1c55-f375-487c-b48a-a9a9d10169a3",
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "5a74ea65-a9d8-40e7-9ee4-5b0e3db6cbc0",
  "sourceToolAssistantUUID": "122b1c55-f375-487c-b48a-a9a9d10169a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:15:45.171Z_

<details><summary>↩ Tool result · `toolu_01B3KurMkUGh94FS3afLEmH6`</summary>

```text
Web search results for query: "site:2026.emnlp.org calls main conference papers deadlines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"}]

I found the information about EMNLP 2026's main conference papers call. Based on the search results, here are the key details:

## Main Conference Paper Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

**Submission Deadlines:**
All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth"). Papers must be submitted, at latest, by the ARR 2026 May cycle.

**Conference Details:**
EMNLP 2026 will be held in Budapest, Hungary from October 24th to October 29th, 2026.

**Important Policies:**
- At the time of submission to ARR, authors will be asked to select a preferred venue (e.g., EMNLP 2026).
- Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026.
- Dual submissions are not allowed!

The full Call for Main Conference Papers can be found at https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe803d45-5b39-4105-bd58-4c98526a8e37",
  "isSidechain": true,
  "promptId": "e20c24b8-cb96-4f00-adab-0bdcf25450f4",
  "agentId": "a0bac6764b0f3f00b",
  "type": "user",
  "uuid": "23cf2fd0-3ba0-4a31-9314-712d0ba8b276",
  "sourceToolAssistantUUID": "fe803d45-5b39-4105-bd58-4c98526a8e37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-12T00:16:00.668Z_

Here are the findings from my search:

---

## EMNLP 2026 Deadline Verification

### 1. ARR Submission Deadline: Confirmed -- May 25, 2026

Yes, the ARR submission deadline for EMNLP 2026 is **May 25, 2026**. This is confirmed across multiple sources, including the official EMNLP 2026 website and their official X/Twitter announcement. All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

An important note: since the ARR May 2026 cycle is shared between EMNLP and AACL-IJCNLP, authors must explicitly select their target conference at submission time, and this choice is **binding**.

Additionally, the reviewer/author registration deadline is May 27, 2026 (two days after the paper submission deadline).

### 2. Commitment Deadline: August 2, 2026

After papers go through the ARR review process during the May cycle, authors must commit their reviewed papers to EMNLP 2026 by **August 2, 2026**. Notification of acceptance follows on **August 20, 2026**.

### 3. Short Paper Track: Yes, it exists

EMNLP 2026 accepts both **long and short papers**. The official Call for Papers and the EMNLP 2026 X/Twitter account both explicitly state: "We welcome long & short papers featuring original research on empirical methods for NLP." Both paper types share the same ARR submission deadline (May 25, 2026) and the same commitment deadline (August 2, 2026).

### Key Dates Summary

| Milestone | Date |
|---|---|
| ARR Submission Deadline (long & short) | May 25, 2026 |
| Reviewer Registration Deadline | May 27, 2026 |
| Commitment Deadline | August 2, 2026 |
| Notification of Acceptance | August 20, 2026 |
| Conference (Budapest, Hungary) | October 24--29, 2026 |

---

Sources:
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Update on Binding Venue Selection (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ACL Rolling Review - Dates and Venues](http://aclrollingreview.org/dates)
- [2026 *ACL Conference Dates](https://submissions.cljournal.org/index.php/cljournal/announcement/view/14)
- [AI Conference Deadlines - EMNLP 2026](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23cf2fd0-3ba0-4a31-9314-712d0ba8b276",
  "isSidechain": true,
  "agentId": "a0bac6764b0f3f00b",
  "requestId": "req_011CawiDnEf1G7yKhqqQ75JX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22eae234-5b6f-4cc7-b7aa-1ae083d20e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d2abee89-9988-41c8-a771-960edf9f50fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5cQt1rmVXG96fMJHauigi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1713,
      "cache_read_input_tokens": 13813,
      "output_tokens": 766,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 766,
          "cache_read_input_tokens": 13813,
          "cache_creation_input_tokens": 1713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1713,
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
