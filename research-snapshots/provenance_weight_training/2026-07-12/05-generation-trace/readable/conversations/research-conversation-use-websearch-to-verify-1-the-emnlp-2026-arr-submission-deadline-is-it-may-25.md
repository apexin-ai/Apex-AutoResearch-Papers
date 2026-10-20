# Research conversation: Use WebSearch to verify: 1. The EMNLP 2026 ARR submission deadline — is it May 25, 2026? 2. Does EMNLP 2026 have a speci

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6d53ffdc7c9c7a88.jsonl`
- **Structured JSON:** [`4fe6c02f793e7dd2d624.json`](../../sessions/4f/4fe6c02f793e7dd2d624.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-12T00:29:50.047Z_

Use WebSearch to verify:

1. The EMNLP 2026 ARR submission deadline — is it May 25, 2026?
2. Does EMNLP 2026 have a special theme on "New Missions for NLP Research" that explicitly calls for work on data contamination, synthetic data feedback loops, and data governance?
3. What is the general timeline for EMNLP 2026?

Search for "EMNLP 2026 submission deadline", "EMNLP 2026 call for papers", "ARR 2026 May deadline", and "EMNLP 2026 special theme".

Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "8de9d7a5-3a05-47c6-950f-62a43f144215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:29:50.049Z_

```json
{
  "parentUuid": "8de9d7a5-3a05-47c6-950f-62a43f144215",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
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
  "uuid": "04188474-c66b-41b0-9c9f-01d7a50141f4",
  "timestamp": "2026-05-12T00:29:50.049Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:30:08.717Z_



I'll search for information on EMNLP 2026 using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04188474-c66b-41b0-9c9f-01d7a50141f4",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjJ4RU8G3RX9EQ7JJsc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "421ac0c8-a1f4-4570-8293-7b6ce0bd28ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hLMoBHLGzMiRKie2JTSmR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 8223,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 706,
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

### Tool call

_source line 4 · 2026-05-12T00:30:08.802Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LELhbL7c7VhQN7rwjgG4VM`</summary>

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
  "parentUuid": "421ac0c8-a1f4-4570-8293-7b6ce0bd28ae",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjJ4RU8G3RX9EQ7JJsc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fffe58d-d307-4831-94f8-917f9ad314ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hLMoBHLGzMiRKie2JTSmR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 8223,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 706,
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

_source line 5 · 2026-05-12T00:30:08.805Z_

<details><summary>↩ Tool result · `toolu_01LELhbL7c7VhQN7rwjgG4VM`</summary>

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
  "parentUuid": "9fffe58d-d307-4831-94f8-917f9ad314ee",
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "c4b8abdb-1b8b-425c-9052-a614718f3836",
  "sourceToolAssistantUUID": "9fffe58d-d307-4831-94f8-917f9ad314ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:30:13.406Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4b8abdb-1b8b-425c-9052-a614718f3836",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjKUwPHpgmghcRqtYfL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6538dec0-39da-4dbb-ab53-8c1cfc3de404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwnbQhSkM1fQ9MMJmyJ8da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 7 · 2026-05-12T00:30:13.900Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KoREVAoZgfGtVBK5cgCJ7m`</summary>

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
  "parentUuid": "6538dec0-39da-4dbb-ab53-8c1cfc3de404",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjKUwPHpgmghcRqtYfL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec6d0ec0-1ef3-4c1d-bb63-8c12c82c77d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwnbQhSkM1fQ9MMJmyJ8da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 8 · 2026-05-12T00:30:14.374Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WSHiwFyE6whcocF5Hg4nDs`</summary>

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
  "parentUuid": "ec6d0ec0-1ef3-4c1d-bb63-8c12c82c77d9",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjKUwPHpgmghcRqtYfL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ef9b928-4d29-4636-8374-83b02a6952f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwnbQhSkM1fQ9MMJmyJ8da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 9 · 2026-05-12T00:30:14.381Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Ta8jcoG49E1wtoaj3QWYD`</summary>

```json
{
  "query": "ARR 2026 May deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ef9b928-4d29-4636-8374-83b02a6952f3",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjKUwPHpgmghcRqtYfL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5e6b79c-28d0-4ff0-bdf9-ef140b3fa304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwnbQhSkM1fQ9MMJmyJ8da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 10 · 2026-05-12T00:30:14.768Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YJDaWAdXihU7uK7FgrqSHv`</summary>

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
  "parentUuid": "b5e6b79c-28d0-4ff0-bdf9-ef140b3fa304",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjKUwPHpgmghcRqtYfL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9db0eaff-aada-464e-9e05-729bba4ce79c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwnbQhSkM1fQ9MMJmyJ8da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1415,
      "cache_read_input_tokens": 8929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1415,
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

_source line 11 · 2026-05-12T00:30:17.888Z_

<details><summary>↩ Tool result · `toolu_01KoREVAoZgfGtVBK5cgCJ7m`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here's the key information about EMNLP 2026 submission deadlines:

## Main Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## Important Related Dates

The reviewer registration deadline for all authors is May 27, 2026.

The author response and author-reviewer discussion period runs from July 7-13, 2026.

The EMNLP commitment deadline is August 2, 2026, and notification of acceptance is August 20, 2026.

## General Information

EMNLP 2026 will be held in Budapest, Hungary from October 24-29, 2026. At the time of submission to ARR, authors will be asked to select a preferred venue (e.g., EMNLP 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec6d0ec0-1ef3-4c1d-bb63-8c12c82c77d9",
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "d5c6e91e-f5de-4788-b274-386c43007cbb",
  "sourceToolAssistantUUID": "ec6d0ec0-1ef3-4c1d-bb63-8c12c82c77d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:30:17.987Z_

<details><summary>↩ Tool result · `toolu_015Ta8jcoG49E1wtoaj3QWYD`</summary>

```text
Web search results for query: "ARR 2026 May deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"AACL 2026 on X: \"🚨AACL-IJCNLP 2026 will be held in Hengqin, China from November 6-10, 2026. The CFP is now out! ARR submission deadline (long &amp; short papers): May 25, 2026! #NLProc #NLP Dates and full CFP here: https://t.co/4ON2H5M7zQ @aadi_joshi @kta84912 https://t.co/9ZKWmY7Jvv\" / X","url":"https://x.com/aaclmeeting/status/2041832211599733075"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, there are several important ARR (ACL Rolling Review) deadlines in May 2026:

EMNLP 2026 has an ARR submission deadline of May 25, 2026, and AACL 2026 also has an ARR submission deadline of May 25, 2026 for long and short papers.

These are the submission deadlines for papers that will be reviewed through the ACL Rolling Review system and considered for acceptance at these two major NLP conferences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5e6b79c-28d0-4ff0-bdf9-ef140b3fa304",
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "9eca8c55-bbc2-4173-9fdd-792d4b479db5",
  "sourceToolAssistantUUID": "b5e6b79c-28d0-4ff0-bdf9-ef140b3fa304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:30:20.844Z_

<details><summary>↩ Tool result · `toolu_01WSHiwFyE6whcocF5Hg4nDs`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Here are the key details from the EMNLP 2026 Call for Papers:

## Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. The conference will be held as a hybrid conference, and physically held in Budapest, Hungary from October 24th to October 29th, 2026.

## Important Dates
The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. The meta review will be released on July 30, 2026, with the EMNLP commitment deadline on August 2, 2026, and notification of acceptance on August 20, 2026.

## Submission Process
Authors will need to explicitly declare which conference they intend to commit to at submission time when submitting to the ARR 2026 May cycle, as it is aligned with AACL 2026. This choice will be binding for EMNLP 2026. Dual submissions are not allowed.

## Special Theme
The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era.

## Reviewer Requirements
All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications.

For the complete call for papers, visit: https://2026.emnlp.org/calls/main_conference_papers/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ef9b928-4d29-4636-8374-83b02a6952f3",
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "8b929ec1-787d-4519-9dfb-c995bdfa5760",
  "sourceToolAssistantUUID": "4ef9b928-4d29-4636-8374-83b02a6952f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:30:21.622Z_

<details><summary>↩ Tool result · `toolu_01YJDaWAdXihU7uK7FgrqSHv`</summary>

```text
Web search results for query: "EMNLP 2026 special theme"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"The center of gravity in NLP is shifting. 🌍 This year's #EMNLP2026 Special Theme is \"New Missions for NLP Research.\" We welcome empirical, theoretical, or position and survey papers that reframe our collective research goals. Find out more: https://t.co/6dttoXBb3B\" / X","url":"https://x.com/emnlpmeeting/status/2029509201580446135"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP (@emnlpmeeting.bsky.social) — Bluesky","url":"https://bsky.app/profile/emnlpmeeting.bsky.social"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here's information about the EMNLP 2026 special theme:

"New Missions for NLP Research" is the special theme for EMNLP 2026.

The theme reflects how large language models have rapidly shifted from research prototypes to widely used infrastructure, changing the center of gravity of NLP research, as progress can no longer be measured only by fractional improvements in benchmark scores.

The special theme invites papers that articulate, test, and advance visions for NLP in this era, welcoming work that reflects on the mission(s) of NLP research, reframes collective research goals, proposes new evaluation and scientific methodologies, and builds bridges across multiple disciplines.

Submissions may be empirical, theoretical, or position and survey papers, but should be grounded in clear claims, strong evidence, and actionable insights.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9db0eaff-aada-464e-9e05-729bba4ce79c",
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "492dc8b6-b971-4294-af23-930abe0155fc",
  "sourceToolAssistantUUID": "9db0eaff-aada-464e-9e05-729bba4ce79c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T00:30:24.918Z_

Let me get more detail on the specific sub-topics of the special theme.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "492dc8b6-b971-4294-af23-930abe0155fc",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjLPSmHvkN6HdGdCUsp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4b6a47f-936f-42c7-acf5-fc3923962483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EMLFY6JTp2u9diMjxQgY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3759,
      "cache_read_input_tokens": 10344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3759,
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

_source line 16 · 2026-05-12T00:30:25.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0186EHhTWgxzrn6LJFZDfk3q`</summary>

```json
{
  "query": "EMNLP 2026 \"New Missions for NLP Research\" data contamination synthetic data feedback loops data governance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4b6a47f-936f-42c7-acf5-fc3923962483",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjLPSmHvkN6HdGdCUsp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4db86c08-b3b2-4e76-8a67-1f01a28ccd11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EMLFY6JTp2u9diMjxQgY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3759,
      "cache_read_input_tokens": 10344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3759,
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

_source line 17 · 2026-05-12T00:30:26.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CYLjX7MHX9oMHfM7AjhgWS`</summary>

```json
{
  "query": "site:2026.emnlp.org special theme \"New Missions for NLP Research\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db86c08-b3b2-4e76-8a67-1f01a28ccd11",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjLPSmHvkN6HdGdCUsp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "417a3b79-36e1-4df4-94ac-8cbd511fd4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EMLFY6JTp2u9diMjxQgY7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3759,
      "cache_read_input_tokens": 10344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3759,
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

_source line 18 · 2026-05-12T00:30:29.501Z_

<details><summary>↩ Tool result · `toolu_01CYLjX7MHX9oMHfM7AjhgWS`</summary>

```text
Web search results for query: "site:2026.emnlp.org special theme "New Missions for NLP Research""

Links: [{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"}]

The search found a result from the EMNLP 2026 website. The special theme for EMNLP is "New Missions for NLP Research". 

Tutorial proposals that align with this special theme are welcome, and proposers should explain why their proposal aligns with it. EMNLP 2026 will be held as a hybrid conference physically in Budapest, Hungary from October 24th to October 29th, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "417a3b79-36e1-4df4-94ac-8cbd511fd4bf",
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "fab49a65-3b74-4303-92a2-9f2e8a494fe7",
  "sourceToolAssistantUUID": "417a3b79-36e1-4df4-94ac-8cbd511fd4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:30:32.745Z_

<details><summary>↩ Tool result · `toolu_0186EHhTWgxzrn6LJFZDfk3q`</summary>

```text
Web search results for query: "EMNLP 2026 "New Missions for NLP Research" data contamination synthetic data feedback loops data governance"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"(PDF) NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark","url":"https://www.researchgate.net/publication/376393345_NLP_Evaluation_in_trouble_On_the_Need_to_Measure_LLM_Data_Contamination_for_each_Benchmark"},{"title":"EMNLP 2026 on X: \"The center of gravity in NLP is shifting. 🌍 This year's #EMNLP2026 Special Theme is \"New Missions for NLP Research.\" We welcome empirical, theoretical, or position and survey papers that reframe our collective research goals. Find out more: https://t.co/6dttoXBb3B\" / X","url":"https://x.com/emnlpmeeting/status/2029509201580446135"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"Allen School News » Allen School researchers earn EMNLP Best Paper Award for making Internet-scale texts efficiently searchable with infini-gram mini","url":"https://news.cs.washington.edu/2026/01/29/allen-school-researchers-earn-emnlp-best-paper-award/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"},{"title":"EMNLP Papers 2024 - Emory NLP","url":"https://www.linkedin.com/posts/emorynlp_emnlp-papers-2024-emory-nlp-activity-7246962103108997120-V5zk"}]

Based on the search results, here's what I found about EMNLP 2026 and the "New Missions for NLP Research" special theme:

## EMNLP 2026 Special Theme: "New Missions for NLP Research"

EMNLP 2026 features a special theme called "New Missions for NLP Research." Large language models have rapidly shifted from research prototypes to widely used infrastructure, and this new reality is changing the center of gravity of NLP research. When strong general-purpose models are increasingly available through open releases and commercial platforms, the field faces a more foundational question: What are the missions of NLP research now, and what kinds of contributions most advance that mission?

## Data Governance and Related Topics

The conference specifically welcomes research on data scarcity and limits, contamination, and the consequences of synthetic data feedback loops, and new approaches to data creation, documentation, governance, and consent.

The EMNLP 2026 special theme invites papers that articulate, test, and advance visions for NLP in this era, welcoming work that reflects on the mission(s) of NLP research, reframes collective research goals, proposes new evaluation and scientific methodologies, and builds bridges across multiple disciplines.

## Submission Information

The First Call for Papers for EMNLP 2026 is officially out, welcoming long and short papers featuring original research on empirical methods for NLP, with an ARR submission deadline of May 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4db86c08-b3b2-4e76-8a67-1f01a28ccd11",
  "isSidechain": true,
  "promptId": "6d30b030-33dc-4c7d-ad55-0f5c19192022",
  "agentId": "a6d53ffdc7c9c7a88",
  "type": "user",
  "uuid": "753404e0-fb32-47d1-8883-4f401da9646b",
  "sourceToolAssistantUUID": "4db86c08-b3b2-4e76-8a67-1f01a28ccd11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-12T00:30:49.223Z_

Here are the findings for all three questions:

---

**1. ARR Submission Deadline: May 25, 2026 -- CONFIRMED.**

The ARR submission deadline for EMNLP 2026 long and short papers is indeed **May 25, 2026**. The reviewer registration deadline for all authors follows two days later on May 27, 2026. Note that this ARR May cycle is shared with AACL-IJCNLP 2026, and authors must explicitly select their target conference at submission time (this choice is binding).

**2. Special Theme on "New Missions for NLP Research" -- CONFIRMED, including those specific topics.**

The special theme is titled **"New Missions for NLP Research."** The call for papers **explicitly** welcomes research on:
- **Data contamination**
- **Synthetic data feedback loops** (specifically: "the consequences of synthetic data feedback loops")
- **Data governance** (specifically: "new approaches to data creation, documentation, governance, and consent")
- Data scarcity and limits

The theme broadly invites empirical, theoretical, or position/survey papers that reflect on what the missions of NLP research should be now that strong general-purpose LLMs are widely available, and asks contributors to reframe collective research goals, propose new evaluation methodologies, and build bridges across disciplines.

**3. General Timeline for EMNLP 2026:**

| Milestone | Date |
|---|---|
| ARR submission deadline (long & short papers) | May 25, 2026 |
| Reviewer registration deadline (all authors) | May 27, 2026 |
| Author response & author-reviewer discussion | July 7--13, 2026 |
| Meta-review release | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Notification of acceptance | August 20, 2026 |
| Conference (Budapest, Hungary) | October 24--29, 2026 |

The conference will be held as a **hybrid** event, physically in **Budapest, Hungary**.

Sources:
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Special Theme Announcement (X/Twitter)](https://x.com/emnlpmeeting/status/2029509201580446135)
- [EMNLP 2026 ARR Target Conference Update (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [2026 *ACL Conference Dates](https://submissions.cljournal.org/index.php/cljournal/announcement/view/14)
- [LINGUIST List - EMNLP 2026](https://linguistlist.org/issues/37/972/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "753404e0-fb32-47d1-8883-4f401da9646b",
  "isSidechain": true,
  "agentId": "a6d53ffdc7c9c7a88",
  "requestId": "req_011CawjMCwGTz3RqEc7wWkiv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "284313e6-87c5-4911-a271-8b861301aa09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "29ad655f-fa0c-457e-83f8-8620db8c5bc8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NPEY3M6fVt2YiCzNiFATV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 222,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 14103,
      "output_tokens": 781,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 222,
          "output_tokens": 781,
          "cache_read_input_tokens": 14103,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1426,
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
