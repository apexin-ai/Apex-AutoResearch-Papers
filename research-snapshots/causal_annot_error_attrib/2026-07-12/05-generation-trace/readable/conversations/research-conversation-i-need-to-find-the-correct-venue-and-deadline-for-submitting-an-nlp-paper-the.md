# Research conversation: I need to find the correct venue and deadline for submitting an NLP paper. The user originally wanted EMNLP 2026 but the

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a2aacfb067adbd443.jsonl`
- **Structured JSON:** [`c0cfffc03d9c8d343d00.json`](../../sessions/c0/c0cfffc03d9c8d343d00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-17T08:47:09.905Z_

I need to find the correct venue and deadline for submitting an NLP paper. The user originally wanted EMNLP 2026 but the May ARR deadline may have passed. Today is May 17, 2026.

Please search for:
1. ACL Rolling Review (ARR) 2026 deadlines — specifically June, July, August 2026 cycles
2. Which ARR cycles can target EMNLP 2026 (when is the EMNLP 2026 commitment deadline?)
3. AAAI 2027 deadline (expected around August 2026)
4. Any other suitable venues with deadlines in Summer/Fall 2026 for NLP + interpretability work

Search queries to try:
- "ACL Rolling Review 2026 deadlines"
- "ARR June 2026 deadline"
- "EMNLP 2026 deadline commitment"
- "AAAI 2027 call for papers deadline"

Report specific dates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "fad6b69f-275c-43e0-9528-eeec2ac850d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T08:47:09.907Z_

```json
{
  "parentUuid": "fad6b69f-275c-43e0-9528-eeec2ac850d7",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
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
  "uuid": "928540b7-c249-4e8b-96a9-d737879e666d",
  "timestamp": "2026-05-17T08:47:09.907Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T08:47:12.229Z_



I'll search for all of these deadlines in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "928540b7-c249-4e8b-96a9-d737879e666d",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rGG9i7nRYDtFwPvgLp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1643729f-999a-43ef-9f0f-2e34b6d0427b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZi2gccqLdV4kj5MQtCADn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 780,
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

_source line 4 · 2026-05-17T08:47:12.341Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017ufKZvUMkEeciAaDjScsN3`</summary>

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
  "parentUuid": "1643729f-999a-43ef-9f0f-2e34b6d0427b",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rGG9i7nRYDtFwPvgLp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3cfc0340-ca14-450d-bbd5-3f1e6fd41ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZi2gccqLdV4kj5MQtCADn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 8223,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 780,
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

_source line 5 · 2026-05-17T08:47:12.344Z_

<details><summary>↩ Tool result · `toolu_017ufKZvUMkEeciAaDjScsN3`</summary>

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
  "parentUuid": "3cfc0340-ca14-450d-bbd5-3f1e6fd41ffa",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "745408e5-3ae8-4322-8142-e1e93ee43f53",
  "sourceToolAssistantUUID": "3cfc0340-ca14-450d-bbd5-3f1e6fd41ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-17T08:47:15.341Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "745408e5-3ae8-4322-8142-e1e93ee43f53",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rGSmS5UguFXPfW26ce",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c91e7c50-7ffc-40df-9972-e772602ada11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wDMCMTnR4U1EGXAcSXUK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 7 · 2026-05-17T08:47:16.072Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013cirfPk6DoSTpDHViaGjxb`</summary>

```json
{
  "query": "ACL Rolling Review 2026 deadlines June July August cycles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c91e7c50-7ffc-40df-9972-e772602ada11",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rGSmS5UguFXPfW26ce",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1e1d82a-c5d2-4ecc-b5f2-0c6720041519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wDMCMTnR4U1EGXAcSXUK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 8 · 2026-05-17T08:47:16.292Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UySVZvPKfC8ERyPekmYLHM`</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1e1d82a-c5d2-4ecc-b5f2-0c6720041519",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rGSmS5UguFXPfW26ce",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85f91d54-5a57-4e2a-af8d-677fbc6401ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wDMCMTnR4U1EGXAcSXUK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 9 · 2026-05-17T08:47:17.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182LdiYPeiXVWNN1xTr4A1G`</summary>

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
  "parentUuid": "85f91d54-5a57-4e2a-af8d-677fbc6401ff",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rGSmS5UguFXPfW26ce",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a153368c-f4e6-49b5-b95c-8dc4dbaa50c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wDMCMTnR4U1EGXAcSXUK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 9003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 10 · 2026-05-17T08:47:17.542Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WpLzry3PiEnBysPucXwC4K`</summary>

```json
{
  "query": "NLP conferences 2026 2027 deadlines summer fall interpretability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a153368c-f4e6-49b5-b95c-8dc4dbaa50c4",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rGSmS5UguFXPfW26ce",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f678c33-4efa-40ac-993c-78dc9a5ae38d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wDMCMTnR4U1EGXAcSXUK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 9003,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 221,
          "cache_read_input_tokens": 9003,
          "cache_creation_input_tokens": 1406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1406,
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

_source line 11 · 2026-05-17T08:47:21.416Z_

<details><summary>↩ Tool result · `toolu_013cirfPk6DoSTpDHViaGjxb`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 deadlines June July August cycles"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's what I found about ACL Rolling Review 2026 deadlines and cycles:

## Review Cycle Structure

ACL switched to 10-week review cycles, with the new schedule starting in May 2025. This means there are generally 5 cycles a year instead of 6.

## January 2026 Cycle Deadlines

For the January 2026 submission cycle, here are the key deadlines:

- Submission deadline (all papers submitted to ARR): January 5, 2026
- Author registration form deadline: January 7, 2026
- Review submission deadline: February 7th, and meta-review deadline: March 3rd
- ARR reviews & meta-reviews available to authors: March 10, 2026

## June, July, and August 2026

Unfortunately, the search results do not contain specific submission deadlines for June, July, or August 2026 cycles for ACL Rolling Review. The official ACL Rolling Review website (aclrollingreview.org/dates) appears to have a table with upcoming cycle dates, but the complete details weren't fully captured in the search results. I recommend visiting the official ACL Rolling Review dates page directly for the most current information on future cycle deadlines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1e1d82a-c5d2-4ecc-b5f2-0c6720041519",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "2c062564-37d0-4859-825c-fa555aeb28b6",
  "sourceToolAssistantUUID": "b1e1d82a-c5d2-4ecc-b5f2-0c6720041519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T08:47:21.705Z_

<details><summary>↩ Tool result · `toolu_0182LdiYPeiXVWNN1xTr4A1G`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"}]

Based on the search results, here are the key deadlines for the AAAI 2027 call for papers:

For the Main Technical Track:
- Abstract deadline: July 21, 2026
- Full papers due: July 28, 2026
- Supplementary material and code due: July 31, 2026

All deadlines are "anywhere on earth" (UTC-12), and track-specific deadlines may differ from those listed above, with track-specific deadlines listed on their respective CFP.

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a153368c-f4e6-49b5-b95c-8dc4dbaa50c4",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "0161aedb-2676-4c0b-adaa-d84836a83da9",
  "sourceToolAssistantUUID": "a153368c-f4e6-49b5-b95c-8dc4dbaa50c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T08:47:21.733Z_

<details><summary>↩ Tool result · `toolu_01UySVZvPKfC8ERyPekmYLHM`</summary>

```text
Web search results for query: "EMNLP 2026 commitment deadline ARR cycle"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the information about the EMNLP 2026 commitment deadline in relation to the ARR cycle:

The ARR submission deadline for EMNLP 2026 (long and short papers) is May 25, 2026, and the EMNLP commitment deadline is August 2, 2026.

Papers must be submitted, at latest, by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.

Important to note: Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85f91d54-5a57-4e2a-af8d-677fbc6401ff",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "a8e18bf6-10fc-4cd0-a58c-c5448b8b670a",
  "sourceToolAssistantUUID": "85f91d54-5a57-4e2a-af8d-677fbc6401ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T08:47:23.905Z_

<details><summary>↩ Tool result · `toolu_01WpLzry3PiEnBysPucXwC4K`</summary>

```text
Web search results for query: "NLP conferences 2026 2027 deadlines summer fall interpretability"

Links: [{"title":"NLPIR 2026","url":"https://nlpir.net/"},{"title":"Natural Language Processing (NLP) Conferences 2026/2027/2028 - Conference Index","url":"https://conferenceindex.org/conferences/natural-language-processing-nlp"},{"title":"Events List | ACL Member Portal","url":"https://www.aclweb.org/portal/events?order=field_event_date&sort=desc"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"NLP Call For Papers for Conferences, Workshops and Journals at WikiCFP","url":"http://www.wikicfp.com/cfp/call?conference=NLP"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI Conference Deadlines","url":"https://hlr.github.io/deadlines/"},{"title":"NLP 2026 | International Conference on Natural Language Processing | Webinar","url":"https://www.olcias.com/nlp"},{"title":"Natural Language Processing (NLP) Conferences in USA 2026/2027/2028 - Conference Index","url":"https://conferenceindex.org/conferences/natural-language-processing-nlp/united-states"}]

I've found several NLP conferences for 2026-2027 with submission deadlines. Here are the key ones:

## Summer 2026 Conferences:

**ACL 2026** is scheduled for July 6-12, 2026 in Seoul, Korea, with an abstract deadline of January 24, 2026.

**NAACL 2026** takes place July 2-7, 2026 in San Diego, California.

**ACL Findings** will be held June 16-19, 2026 in Amsterdam, Netherlands, with an abstract deadline of February 6, 2026.

## Fall 2026 Conferences:

**EMNLP 2026** is scheduled for September 13-17, 2026 in Tampere, Finland.

**COLING 2026** will be held September 27-October 1, 2026 in Sydney, Australia.

**NeurIPS 2026** takes place November 10-14, 2026 in Rio de Janeiro, Brazil, with an abstract deadline of March 25, 2026.

## 2027 Conferences:

**ACL 2027** is scheduled for February 16-23, 2027 in Montréal, Québec, Canada.

**NAACL 2027** will be held May 16-21, 2027 in Toronto, Canada.

## Interpretability Focus:

NLPIR 2026 specifically welcomes research on "interpretable architectures" as part of its scope, with a submission deadline of June 30, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f678c33-4efa-40ac-993c-78dc9a5ae38d",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "02b0098e-7a25-49cb-becd-b0283f60a2f9",
  "sourceToolAssistantUUID": "0f678c33-4efa-40ac-993c-78dc9a5ae38d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-17T08:47:26.123Z_

Let me get more specific details on the ARR May 2026 deadline (to see if it has passed) and the COLING 2026 deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02b0098e-7a25-49cb-becd-b0283f60a2f9",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rHJ3LyESHXWnoWnfq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbc29a9f-1249-4413-a59a-c63c822dc2f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iLVKmyCqN3mpCZL2nkEkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 16 · 2026-05-17T08:47:26.620Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YDNVDhVwTSXoejVdaMa9T6`</summary>

```json
{
  "query": "ARR May 2026 submission deadline exact date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbc29a9f-1249-4413-a59a-c63c822dc2f2",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rHJ3LyESHXWnoWnfq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf6eb743-9596-47cc-912e-a855f6f0be34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iLVKmyCqN3mpCZL2nkEkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 17 · 2026-05-17T08:47:27.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dwd9ks4oih3E7735MJmxAV`</summary>

```json
{
  "query": "COLING 2026 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf6eb743-9596-47cc-912e-a855f6f0be34",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rHJ3LyESHXWnoWnfq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6fbb10f-75da-407f-9447-8e5b33946500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iLVKmyCqN3mpCZL2nkEkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 18 · 2026-05-17T08:47:27.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MYs8pyKymsgwPzVZ6ZuLao`</summary>

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
  "parentUuid": "b6fbb10f-75da-407f-9447-8e5b33946500",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rHJ3LyESHXWnoWnfq3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7b73368-44a4-4084-91ef-1ed7b9894940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iLVKmyCqN3mpCZL2nkEkg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 10409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 19 · 2026-05-17T08:47:29.065Z_

<details><summary>↩ Tool result · `toolu_01YDNVDhVwTSXoejVdaMa9T6`</summary>

```text
Web search results for query: "ARR May 2026 submission deadline exact date"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"}]

Based on the search results, the ARR May 2026 submission deadline is May 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf6eb743-9596-47cc-912e-a855f6f0be34",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "27dbdcd1-b491-4264-955a-e9baf2b00c3f",
  "sourceToolAssistantUUID": "bf6eb743-9596-47cc-912e-a855f6f0be34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T08:47:31.552Z_

<details><summary>↩ Tool result · `toolu_01MYs8pyKymsgwPzVZ6ZuLao`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS Conference on X: \"The NeurIPS 2026 submission site opening has been moved to April 15th. Note that all tracks (Main Submission, Evaluations &amp; Datasets, and Position Papers) share the same dates. The final submission deadlines remain unchanged: • Paper Abstracts: May 4th (AOE) • Full Papers:\" / X","url":"https://x.com/NeurIPSConf/status/2041303457554940336"}]

Based on the search results, here are the submission deadlines for NeurIPS 2026:

## NeurIPS 2026 Submission Deadlines

Abstract submission deadline: May 4, 2026 (AOE)

Full paper submission deadline, including all supplementary materials: May 6, 2026 AOE

The NeurIPS 2026 submission site opening has been moved to April 15th.

The different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines, though the abstract and paper deadlines remain the same across all tracks.

Additionally, all authors must have an OpenReview profile when submitting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7b73368-44a4-4084-91ef-1ed7b9894940",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "7b23bb49-ff0f-4fb7-a69c-4cc325ce72f0",
  "sourceToolAssistantUUID": "e7b73368-44a4-4084-91ef-1ed7b9894940",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T08:47:34.314Z_

<details><summary>↩ Tool result · `toolu_01Dwd9ks4oih3E7735MJmxAV`</summary>

```text
Web search results for query: "COLING 2026 submission deadline call for papers"

Links: [{"title":"COLING: International Conference on Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=533"},{"title":"COLING 2026 - International Conference on Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/coling"},{"title":"Call for Main Conference Papers - COLING 2025","url":"https://coling2025.org/calls/main_conference_papers/"},{"title":"Call for papers for computational linguistics conference in ...","url":"https://www.facebook.com/groups/CorpusLinguistics/posts/10162428528018002/"},{"title":"Computer Science conferences timeline","url":"https://lucjaulmes.github.io/cfp-timeline/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"CoNLL 2026: 3rd and Final Call for Papers - Corpora - ELRA lists","url":"https://list.elra.info/mailman3/hyperkitty/list/corpora@list.elra.info/thread/BDW4FPXENUKPTACOYMT5PXZSDZHJ5LB4/"},{"title":"AbjadNLP 2026 – The 2nd Workshop on NLP for Languages Using Arabic Script","url":"https://wp.lancs.ac.uk/abjad/"},{"title":"CoNLL 2026 | CoNLL","url":"https://conll.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, I found some relevant information about COLING 2026, though detailed submission deadline information wasn't fully captured. Here's what I found:

The International Conference on Computational Linguistics (COLING 2026) will be held in Abu Dhabi, UAE. However, the search results primarily contain information about COLING 2025, which took place in Abu Dhabi, UAE, January 19-24 2025.

The search results reference WikiCFP and ConferenceDeadlines.com as sources that track COLING submission deadlines, but the specific COLING 2026 submission deadline details were not fully provided in these results. To get the most current and detailed information about COLING 2026's call for papers and submission deadlines, I recommend checking:

1. The official COLING conference website
2. WikiCFP (wikicfp.com) - which tracks conference deadlines
3. ConferenceDeadlines.com - which specifically lists COLING deadlines

These sources would have the most up-to-date information about submission procedures, page limits, deadlines, and other requirements for COLING 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6fbb10f-75da-407f-9447-8e5b33946500",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "3747823a-03da-4f28-94c4-978eda73a3e1",
  "sourceToolAssistantUUID": "b6fbb10f-75da-407f-9447-8e5b33946500",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-17T08:47:37.027Z_

Let me also check for AACL 2026 and the exact ARR cycle dates page, plus ICML 2026 as another option.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3747823a-03da-4f28-94c4-978eda73a3e1",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rJ4iBXYGXxFNw8aqXX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea7fbae7-1683-4e1b-afe9-970589d8ec8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yRw3uoiHtMNE4NXEhpokk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1653,
      "cache_read_input_tokens": 13765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1653,
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

_source line 23 · 2026-05-17T08:47:37.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WxBgA3sf56yYFDzVZdaHdo`</summary>

```json
{
  "query": "AACL 2026 deadline commitment ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea7fbae7-1683-4e1b-afe9-970589d8ec8e",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rJ4iBXYGXxFNw8aqXX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a67a40c7-a294-4243-aa40-b1ed34b3f9cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yRw3uoiHtMNE4NXEhpokk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1653,
      "cache_read_input_tokens": 13765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1653,
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

_source line 24 · 2026-05-17T08:47:37.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TH4L8ZHRX8kfcMXXwBuY5G`</summary>

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
  "parentUuid": "a67a40c7-a294-4243-aa40-b1ed34b3f9cf",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rJ4iBXYGXxFNw8aqXX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7bc4017-785d-4f27-a9c0-d5cb12b08eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yRw3uoiHtMNE4NXEhpokk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1653,
      "cache_read_input_tokens": 13765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1653,
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

_source line 25 · 2026-05-17T08:47:38.183Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017XPcReMheA799PVVpakYG9`</summary>

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
  "parentUuid": "f7bc4017-785d-4f27-a9c0-d5cb12b08eee",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rJ4iBXYGXxFNw8aqXX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b803b846-7d23-4ed8-a9dc-06b7d38e4e8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yRw3uoiHtMNE4NXEhpokk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 694,
      "cache_creation_input_tokens": 1653,
      "cache_read_input_tokens": 13765,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1653
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 694,
          "output_tokens": 185,
          "cache_read_input_tokens": 13765,
          "cache_creation_input_tokens": 1653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1653,
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

_source line 26 · 2026-05-17T08:47:40.917Z_

<details><summary>↩ Tool result · `toolu_01WxBgA3sf56yYFDzVZdaHdo`</summary>

```text
Web search results for query: "AACL 2026 deadline commitment ARR"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Update ACL 2025 and 2026 conference deadlines · huggingface/ai-deadlines at 9dc485d","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/9dc485d7522c481c65e1e366500d2ab6398449d9"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here's the information about AACL 2026 deadline and commitment to ARR:

For AACL 2026, the final ARR submission date is May 25, 2026, and the commitment deadline is August 26, 2026.

The commitment deadline is the point at which authors who have received reviews through the ACL Rolling Review (ARR) system must decide whether to formally commit their papers to AACL 2026 for publication consideration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a67a40c7-a294-4243-aa40-b1ed34b3f9cf",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "b79c867b-c959-4ef2-ab57-822d9a7679d5",
  "sourceToolAssistantUUID": "a67a40c7-a294-4243-aa40-b1ed34b3f9cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T08:47:42.357Z_

<details><summary>↩ Tool result · `toolu_017XPcReMheA799PVVpakYG9`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"International Conference on Learning Representations ICLR on February 08-09, 2027 in Lisbon, Portugal - Conference Index","url":"https://conferenceindex.org/event/international-conference-on-learning-representations-iclr-2027-february-lisbon-pt"},{"title":"Personal Conference Deadlines","url":"https://zhaohsu.top/conference-deadlines/"}]

Based on the search results, I found some information about ICLR 2027, though the specific submission deadline appears to vary depending on the conference instance.

The search results indicate that ICLR is typically held in late April or early May each year. However, I found references to multiple ICLR 2027 events:

1. One source mentions Learning Representations scheduled for August 30-31, 2027 in Sydney

2. Another source references ICLR in Lisbon, Portugal on February 08-09, 2027 with a final submission deadline of September 30, 2027

It's important to note that there may be multiple conferences using the ICLR name, and the official ICLR conference (the main machine learning venue) may have different dates and deadlines. I'd recommend checking the official ICLR website (iclr.cc) directly for the most accurate and up-to-date submission deadline for the specific ICLR 2027 conference you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b803b846-7d23-4ed8-a9dc-06b7d38e4e8a",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "2bd953f6-9044-40f2-8299-7e6aeff7c23d",
  "sourceToolAssistantUUID": "b803b846-7d23-4ed8-a9dc-06b7d38e4e8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T08:47:42.797Z_

<details><summary>↩ Tool result · `toolu_01TH4L8ZHRX8kfcMXXwBuY5G`</summary>

```text
Web search results for query: "ICML 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here is the ICML 2026 submission deadline information:

The deadline for full paper submission for ICML 2026 is January 28, 2026. 

Additionally, there are separate deadlines for the abstract submission process: Authors should include a full title for their paper, complete author list, and complete abstract in the submission form by the abstract submission deadline, and the abstract submission deadline is January 24, 2026 AoE, while the full paper submission deadline is January 29, 2026 AoE.

Abstract and paper submission deadlines are strict, and in no circumstances will extensions be given.

If you're interested in submitting a position paper instead of a regular research paper, the position paper abstract deadline is January 24, 2026 AoE and the full submission deadline is January 29, 2026 AoE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7bc4017-785d-4f27-a9c0-d5cb12b08eee",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "69e1c493-ba51-4377-ae73-a94e193fb3c1",
  "sourceToolAssistantUUID": "f7bc4017-785d-4f27-a9c0-d5cb12b08eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T08:47:44.919Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CaM9m5xDoNGT72RfhqVGYX`</summary>

```json
{
  "query": "ICLR 2027 call for papers deadline October 2026 submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e1c493-ba51-4377-ae73-a94e193fb3c1",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rJgmMsEVDRHJJoZEjD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "388340fb-bad7-413e-aeb7-1b75920d0adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qhj8pqhctKSXXQouwftt2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 685,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 15418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2109,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 30 · 2026-05-17T08:47:45.207Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TaRTxXxaXnvN3quDVnS366`</summary>

```json
{
  "query": "EACL 2027 NAACL 2027 submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "388340fb-bad7-413e-aeb7-1b75920d0adc",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rJgmMsEVDRHJJoZEjD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38be68a8-e099-468a-826f-c7ca0494b5dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qhj8pqhctKSXXQouwftt2C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 685,
      "cache_creation_input_tokens": 2109,
      "cache_read_input_tokens": 15418,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2109
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 685,
          "output_tokens": 123,
          "cache_read_input_tokens": 15418,
          "cache_creation_input_tokens": 2109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2109,
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

_source line 31 · 2026-05-17T08:47:49.472Z_

<details><summary>↩ Tool result · `toolu_01CaM9m5xDoNGT72RfhqVGYX`</summary>

```text
Web search results for query: "ICLR 2027 call for papers deadline October 2026 submission"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Workshops Call for Proposals 2026","url":"https://iclr.cc/Conferences/2026/CallForWorkshops"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Key deadlines in AI and ML conferences | Yutori","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"}]

Based on the search results, I found information about ICLR 2026, but the official ICLR 2027 call for papers with an October 2026 deadline does not appear in the current search results. 

The search returned information about ICLR 2026, which had a submission deadline of September 24. However, specific details about an ICLR 2027 call for papers with an October 2026 submission deadline were not found in these results.

The results did show some third-party conference listings that mention various learning representations conferences in 2027 and 2028, but these appear to be from alternative or regional conferences rather than the official ICLR conference.

To find the official ICLR 2027 call for papers and its deadlines, I recommend:
- Visiting the official ICLR website directly at iclr.cc
- Checking their Conferences section for 2027 information
- Subscribing to their official announcements or mailing list

The official ICLR call for papers is typically posted several months in advance of the submission deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "388340fb-bad7-413e-aeb7-1b75920d0adc",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "d82fba1f-0745-4985-972e-46889dc6941f",
  "sourceToolAssistantUUID": "388340fb-bad7-413e-aeb7-1b75920d0adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T08:47:49.672Z_

<details><summary>↩ Tool result · `toolu_01TaRTxXxaXnvN3quDVnS366`</summary>

```text
Web search results for query: "EACL 2027 NAACL 2027 submission deadline ARR"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"Community announcement: Submission dates and process for EACL, NAACL and ACL","url":"https://www.aclweb.org/portal/sites/default/files/Submission%20Dates%20and%20Process%20for%20EACL_NAACL%20and%20ACL%202024-2.pdf"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results, here's what I found regarding submission deadlines for EACL 2027 and NAACL 2027 via ARR:

## EACL 2027
The ARR submission deadline for EACL 2027 (long & short papers) is August 3, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

EACL 2027 will be held in Athens, Greece, from March 9–14, 2027.

## NAACL 2027
The search results do not contain specific ARR submission deadline information for NAACL 2027. The official NAACL 2027 Call for Papers does not appear to have been fully finalized yet at the time of this search.

If you need information about NAACL 2027's submission deadline, I recommend checking the official NAACL website or the ARR website directly, as NAACL typically follows a similar ARR-based submission process as EACL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38be68a8-e099-468a-826f-c7ca0494b5dc",
  "isSidechain": true,
  "promptId": "88eca0fd-fb61-49a1-bbce-77e56caa3596",
  "agentId": "a2aacfb067adbd443",
  "type": "user",
  "uuid": "f034acba-aa2a-4b0d-951a-aaeaefe095b7",
  "sourceToolAssistantUUID": "38be68a8-e099-468a-826f-c7ca0494b5dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-17T08:48:20.116Z_

Here is a comprehensive summary of the deadlines I found.

---

## Summary of Venue Options for an NLP + Interpretability Paper (as of May 17, 2026)

### 1. EMNLP 2026 -- STILL VIABLE

- **Conference dates:** September 13-17, 2026, Tampere, Finland
- **ARR submission deadline:** **May 25, 2026** (8 days from now)
- **Commitment deadline:** **August 2, 2026**
- **Critical note:** Since EMNLP and AACL share the ARR May cycle, authors must **declare a target conference at submission time**, and the choice is **binding**.
- **Verdict:** This is tight but still possible if the paper can be ready by May 25.

### 2. AACL 2026 -- ALSO STILL VIABLE (same ARR cycle)

- **ARR submission deadline:** **May 25, 2026** (same May ARR cycle as EMNLP)
- **Commitment deadline:** **August 26, 2026**
- **Note:** You must choose between EMNLP and AACL at submission time (binding choice).

### 3. EACL 2027 -- Good fallback

- **Conference dates:** March 9-14, 2027, Athens, Greece
- **ARR submission deadline:** **August 3, 2026**
- **Important correction from organizers:** The deadline was corrected from August 6 to **August 3, 2026**. This is the **only viable ARR cycle** for EACL 2027 because the conference is earlier than usual.
- **Verdict:** A very solid option if you miss the May 25 deadline. Gives ~2.5 more months to prepare.

### 4. AAAI 2027 -- Strong option

- **Conference dates:** February 16-23, 2027, Montreal, Canada
- **Abstract deadline:** **July 21, 2026**
- **Full paper deadline:** **July 28, 2026**
- **Supplementary materials/code:** **July 31, 2026**
- **Note:** AAAI is not ARR-based; it has its own review process. It welcomes NLP and interpretability work.
- **Verdict:** Great option with a late-July deadline. Comfortable timeline.

### 5. ICLR 2027 -- Likely option (deadline TBD)

- **Expected submission deadline:** Likely around **September-October 2026** (ICLR 2026 had a deadline of September 24, 2025)
- **Verdict:** The CFP has not been posted yet. If the pattern holds, expect a deadline around late September/early October 2026.

### 6. NeurIPS 2026 -- ALREADY PASSED

- **Abstract deadline:** May 4, 2026 (passed)
- **Full paper deadline:** May 6, 2026 (passed)

### 7. ICML 2026 -- ALREADY PASSED

- **Deadline:** January 28-29, 2026 (long passed)

### 8. Other niche options

- **NLPIR 2026:** Submission deadline June 30, 2026. Specifically welcomes "interpretable architectures" research.
- **COLING 2026:** September 27 - October 1, 2026, Sydney, Australia. (Specific submission deadline not confirmed in search results.)

---

## Recommended Strategy

| Priority | Venue | Deadline | Notes |
|----------|-------|----------|-------|
| 1st | **EMNLP 2026** | May 25, 2026 | 8 days left -- tight but top NLP venue |
| 2nd | **AAAI 2027** | July 28, 2026 | ~10 weeks out, strong AI venue |
| 3rd | **EACL 2027** | Aug 3, 2026 | ~11 weeks, only one ARR cycle for this |
| 4th | **ICLR 2027** | ~Sep/Oct 2026 | CFP not yet posted, excellent venue |

If the paper is close to ready, the **EMNLP 2026 May 25 deadline** is still reachable. If more time is needed, **AAAI 2027 (July 28)** and **EACL 2027 (August 3)** offer comfortable timelines and are strong venues for NLP + interpretability work.

Sources:
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 announcement (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 binding conference choice update (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [AAAI 2027 Main Technical Track CFP](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [AAAI 2027 deadlines (aideadlines.org)](http://aideadlines.org/conference/?id=aaai27)
- [EACL 2027 CFP](https://2027.eacl.org/calls/papers/)
- [EACL 2027 date correction (X/Twitter)](https://x.com/eaclmeeting/status/2051971432171688436)
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)
- [AI Conference Deadlines aggregator](https://mlciv.com/ai-deadlines/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f034acba-aa2a-4b0d-951a-aaeaefe095b7",
  "isSidechain": true,
  "agentId": "a2aacfb067adbd443",
  "requestId": "req_011Cb7rKCDA75PRMnmYcPfVt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c6d9ec4-22d0-4737-aa9a-f547ab4594e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "23971999-7eaf-4430-8955-990a761bafd0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvjeKUANuSMnG4VWnSBn1x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2375,
      "cache_read_input_tokens": 17527,
      "output_tokens": 1446,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2375
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1446,
          "cache_read_input_tokens": 17527,
          "cache_creation_input_tokens": 2375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2375,
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
