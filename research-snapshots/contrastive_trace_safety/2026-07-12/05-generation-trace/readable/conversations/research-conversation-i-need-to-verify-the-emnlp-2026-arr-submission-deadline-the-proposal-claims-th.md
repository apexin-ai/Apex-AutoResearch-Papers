# Research conversation: I need to verify the EMNLP 2026 ARR submission deadline. The proposal claims the ARR May 25, 2026 deadline is the target

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aeb9333e77b766700.jsonl`
- **Structured JSON:** [`542ff799417d73093919.json`](../../sessions/54/542ff799417d73093919.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-11T23:40:48.916Z_

I need to verify the EMNLP 2026 ARR submission deadline. The proposal claims the ARR May 25, 2026 deadline is the target.

Please search for:
1. "ARR 2026 submission deadline" 
2. "EMNLP 2026 call for papers"
3. "ACL Rolling Review May 2026 deadline"
4. "aclrollingreview.org 2026"

I need to confirm: Is there actually an ARR submission cycle with a May 25, 2026 deadline that would feed into EMNLP 2026? Report what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "ead65921-ee0a-4c34-b776-1de71cd3c697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:40:48.920Z_

```json
{
  "parentUuid": "ead65921-ee0a-4c34-b776-1de71cd3c697",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
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
  "uuid": "7e6d485a-3ec2-42f2-b47c-946acd6def6b",
  "timestamp": "2026-05-11T23:40:48.920Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:40:51.376Z_



I'll search for information about the ARR 2026 submission deadlines and EMNLP 2026 call for papers. Let me run multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e6d485a-3ec2-42f2-b47c-946acd6def6b",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfZFq2E5nAfkA4mBKqB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35e5ee5a-e244-4f00-9628-59456b32e4c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tb8NjTPTSug6DZz58nFno",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 691,
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

_source line 4 · 2026-05-11T23:40:51.617Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PCZinTDcMqvMHSviVbbLi6`</summary>

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
  "parentUuid": "35e5ee5a-e244-4f00-9628-59456b32e4c5",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfZFq2E5nAfkA4mBKqB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c0542cf-1c99-45c3-9bac-822a7c82485b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tb8NjTPTSug6DZz58nFno",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 8223,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 691
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 115,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 691,
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

_source line 5 · 2026-05-11T23:40:51.621Z_

<details><summary>↩ Tool result · `toolu_01PCZinTDcMqvMHSviVbbLi6`</summary>

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
  "parentUuid": "6c0542cf-1c99-45c3-9bac-822a7c82485b",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "b73dfaa4-a2ae-412f-ae27-8e419fc3e12c",
  "sourceToolAssistantUUID": "6c0542cf-1c99-45c3-9bac-822a7c82485b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:40:53.973Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b73dfaa4-a2ae-412f-ae27-8e419fc3e12c",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfZTahjQWXkXBn7KB4f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae4a55f5-41f3-44f4-90f7-3c9fcd5cfa43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YKYm3eBi6tE4covuKH7rK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 8914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 7 · 2026-05-11T23:40:54.457Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BNYPgU8D66BS3h8fzq7pqu`</summary>

```json
{
  "query": "ARR 2026 submission deadline ACL Rolling Review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae4a55f5-41f3-44f4-90f7-3c9fcd5cfa43",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfZTahjQWXkXBn7KB4f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11b30cfe-461a-4430-ae27-6f806925f4b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YKYm3eBi6tE4covuKH7rK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 8914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 8 · 2026-05-11T23:40:55.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F4uRfBXzidL4gBcyGimvTR`</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11b30cfe-461a-4430-ae27-6f806925f4b1",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfZTahjQWXkXBn7KB4f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c75ab70-2450-49b5-819c-e669141c607c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YKYm3eBi6tE4covuKH7rK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 8914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 9 · 2026-05-11T23:40:55.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BffqVFZKdVcYAauE5GHw3m`</summary>

```json
{
  "query": "ACL Rolling Review May 2026 deadline submission cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c75ab70-2450-49b5-819c-e669141c607c",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfZTahjQWXkXBn7KB4f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "914c611d-fffd-45ef-8abd-28c0e93974c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YKYm3eBi6tE4covuKH7rK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 8914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 10 · 2026-05-11T23:40:56.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AikYNCXsH2QoFvWAhuBM6X`</summary>

```json
{
  "query": "aclrollingreview.org 2026 deadlines schedule"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "914c611d-fffd-45ef-8abd-28c0e93974c9",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfZTahjQWXkXBn7KB4f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bd6de16-5dd5-4999-968a-964ed1e91567",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YKYm3eBi6tE4covuKH7rK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 8914,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1432
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 217,
          "cache_read_input_tokens": 8914,
          "cache_creation_input_tokens": 1432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1432,
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

_source line 11 · 2026-05-11T23:40:59.996Z_

<details><summary>↩ Tool result · `toolu_01BNYPgU8D66BS3h8fzq7pqu`</summary>

```text
Web search results for query: "ARR 2026 submission deadline ACL Rolling Review"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ARR 2026 submission deadlines:

## 2026 ARR Submission Cycles

Starting in May 2025, ARR switched to 10-week review cycles instead of the previous 8-week cycles.

For ACL 2026 specifically, papers may be submitted to the ARR 2025 October cycle and ARR 2026 January cycle.

## Key Deadlines for January 2026 Cycle

The deadline for completing the registration form is January 7th 2026 EoD AoE. ARR reviews & meta-reviews are available to authors of the January cycle by March 10, 2026.

## General Submission Deadline Pattern

The submission deadline is always the 15th of the month; other dates vary due to the length of months, timing of weekends, etc. This means the January 2026 submission deadline would fall on January 15, 2026.

All deadlines are at 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11b30cfe-461a-4430-ae27-6f806925f4b1",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "44a19839-df26-4f4f-9592-88f5f6dfeb11",
  "sourceToolAssistantUUID": "11b30cfe-461a-4430-ae27-6f806925f4b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:41:00.044Z_

<details><summary>↩ Tool result · `toolu_01F4uRfBXzidL4gBcyGimvTR`</summary>

```text
Web search results for query: "EMNLP 2026 call for papers deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"}]

Based on the search results, here are the key deadlines for EMNLP 2026 call for papers:

**Main Paper Submission Deadline:** ARR Submission Deadline is May 25, 2026

**Other Important Dates:**
- Reviewer registration deadline for ALL authors is May 27, 2026
- Author response and author-reviewer discussion period is July 7 - July 13, 2026
- Meta review is released on July 30, 2026

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth")

**Conference Details:** EMNLP 2026 will be held as a hybrid conference physically held in Budapest, Hungary from October 24-29, 2026

The papers are submitted through ACL Rolling Review (ARR), and papers must be submitted by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c75ab70-2450-49b5-819c-e669141c607c",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "7738ddcc-6c72-4728-9673-86a11d1fb631",
  "sourceToolAssistantUUID": "4c75ab70-2450-49b5-819c-e669141c607c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:41:02.440Z_

<details><summary>↩ Tool result · `toolu_01AikYNCXsH2QoFvWAhuBM6X`</summary>

```text
Web search results for query: "aclrollingreview.org 2026 deadlines schedule"

Links: [{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here are the key 2026 deadlines and schedule for ACL Rolling Review:

## 2026 Submission Cycles and Deadlines

The upcoming ARR cycles in 2026 include:

- **March 2026**: Submission March 16, Reviewer registration March 18, Reviews due April 20, Author Response April 28-May 4, Meta-reviews release May 21, Cycle End May 24
- **May 2026**: Submission May 25, Reviewer registration May 27, Reviews due June 29, Author Response July 7-July 13, Meta-reviews release July 30, Cycle End August 2
- **August 2026**: Submission August 3 (other dates TBA)
- **October 2026**: Submission October 12 (other dates TBA)

## Important Author Requirements

The deadline for completing the registration form is January 7th 2026 EoD AoE. Not all authors will receive assignments, but non-compliant papers may be desk rejected.

If authors get assignments, reviews must be completed by February 7th, and meta-reviews - by March 3rd. (This appears to be referring to the January cycle submissions.)

All deadlines are at 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bd6de16-5dd5-4999-968a-964ed1e91567",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "4bf9ef55-e084-4ab6-b988-c92ac3c7a405",
  "sourceToolAssistantUUID": "5bd6de16-5dd5-4999-968a-964ed1e91567",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:41:03.079Z_

<details><summary>↩ Tool result · `toolu_01BffqVFZKdVcYAauE5GHw3m`</summary>

```text
Web search results for query: "ACL Rolling Review May 2026 deadline submission cycle"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) May 2026 deadline and submission cycle:

## ARR Submission Schedule Changes

The ACL Peer Review Committee recommended switching to 10-week cycles, which started in May 2025. Previously, from October 2022 to February 2025, ARR ran 8-week review cycles with submission deadlines on the 15th of every second month.

## Submission Deadlines

The submission deadline is always the 15th of the month; other dates vary due to the length of months, timing of weekends, etc. This means the May 2026 ARR submission deadline would be May 15, 2026.

## Review Timeline

With 10-week cycles, instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response, as well as platform maintenance.

## Author Requirements

After submission, all authors must complete the author registration form within 48 hours of the deadline. If they get assignments, any assigned reviews and metareviews must be completed on time.

For specific details about the May 2026 cycle timeline, you can visit the official ARR dates page at aclrollingreview.org/dates for the complete schedule of review completion deadlines and other key milestones.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "914c611d-fffd-45ef-8abd-28c0e93974c9",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "41bc200a-d44b-4990-9ed4-4054213de3da",
  "sourceToolAssistantUUID": "914c611d-fffd-45ef-8abd-28c0e93974c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-11T23:41:08.001Z_

Let me also fetch the official EMNLP 2026 call for papers page and the ARR dates page directly for confirmation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41bc200a-d44b-4990-9ed4-4054213de3da",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfaJNqZ96nGgoJJRGED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1efa61b-8892-4ea5-bd95-6cfad7ef6954",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WW1gAFcu4u16RnPGQVAUL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 739,
      "cache_creation_input_tokens": 2612,
      "cache_read_input_tokens": 10346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2612,
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

_source line 16 · 2026-05-11T23:41:08.348Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FeMTJ66WNX7LDAYzX8N9TS`</summary>

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
  "parentUuid": "d1efa61b-8892-4ea5-bd95-6cfad7ef6954",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfaJNqZ96nGgoJJRGED",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "337ca317-185b-408a-8f76-c9382bc57b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WW1gAFcu4u16RnPGQVAUL9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 739,
      "cache_creation_input_tokens": 2612,
      "cache_read_input_tokens": 10346,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2612
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 739,
          "output_tokens": 106,
          "cache_read_input_tokens": 10346,
          "cache_creation_input_tokens": 2612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2612,
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

_source line 17 · 2026-05-11T23:41:08.350Z_

<details><summary>↩ Tool result · `toolu_01FeMTJ66WNX7LDAYzX8N9TS`</summary>

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
  "parentUuid": "337ca317-185b-408a-8f76-c9382bc57b5a",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "51bb22a5-3813-4593-b6fe-5c316022ad96",
  "sourceToolAssistantUUID": "337ca317-185b-408a-8f76-c9382bc57b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-11T23:41:12.677Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Cd9AZXeMepkzx6o5F4RS5F`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all important dates and deadlines mentioned on this page, especially the ARR submission deadline, commitment deadline, notification dates, and conference dates. List them all."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51bb22a5-3813-4593-b6fe-5c316022ad96",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfahPwC6txHuc14RBXK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8a26515-36a9-488a-8982-fd2d9ae8d452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcUnvLLy1ZXJPzdfKEHE62",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 12958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1363,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-11T23:41:13.915Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01StU8x5Eqt9p9y1VZiAUnxD`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract the complete schedule of ARR submission cycles for 2026, including all submission deadlines, review deadlines, meta-review release dates, and cycle end dates. List every cycle with all its dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8a26515-36a9-488a-8982-fd2d9ae8d452",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfahPwC6txHuc14RBXK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b93cea6-928d-4337-b1e4-82fa124943ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcUnvLLy1ZXJPzdfKEHE62",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 12958,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1363
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 12958,
          "cache_creation_input_tokens": 1363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1363,
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

_source line 20 · 2026-05-11T23:41:16.952Z_

<details><summary>↩ Tool result · `toolu_01Cd9AZXeMepkzx6o5F4RS5F`</summary>

```text
# EMNLP 2026 Important Dates and Deadlines

| Event | Date |
|-------|------|
| ARR submission deadline (long & short papers) | May 25, 2026 |
| Reviewer registration deadline for all authors | May 27, 2026 |
| Author response and discussion period | July 7-13, 2026 |
| Meta review released | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Acceptance notification (long & short papers) | August 20, 2026 |
| Camera-ready papers due | September 20, 2026 |
| Main Conference | October 24-29, 2026 |

**Key Note:** "All deadlines are 11:59PM UTC-12:00 ('anywhere on Earth')."

**Critical Policy Detail:** For the ARR 2026 May cycle specifically, authors must declare their intended venue at submission time. Papers selecting EMNLP 2026 during ARR submission can proceed to commitment; however, those not selecting EMNLP initially cannot subsequently commit to this conference, though papers from earlier ARR cycles remain eligible for commitment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8a26515-36a9-488a-8982-fd2d9ae8d452",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "142d6159-bb78-4875-9961-9b9b9eeba43c",
  "sourceToolAssistantUUID": "d8a26515-36a9-488a-8982-fd2d9ae8d452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-11T23:41:17.696Z_

<details><summary>↩ Tool result · `toolu_01StU8x5Eqt9p9y1VZiAUnxD`</summary>

```text
# ARR 2026 Review Cycles Schedule

Based on the webpage content, here is the complete schedule for ARR submission cycles in 2026:

## March 2026 Cycle
- **Submission:** March 16
- **Reviewer Registration:** March 18
- **Reviews Due:** April 20
- **Author Response:** April 28–May 4
- **Meta-reviews Released:** May 21
- **Cycle End:** May 24

## May 2026 Cycle
- **Submission:** May 25
- **Reviewer Registration:** May 27
- **Reviews Due:** June 29
- **Author Response:** July 7–July 13
- **Meta-reviews Released:** July 30
- **Cycle End:** August 2

## August 2026 Cycle
- **Submission:** August 3
- **Reviewer Registration:** TBA
- **Reviews Due:** TBA
- **Author Response:** TBA
- **Meta-reviews Released:** TBA
- **Cycle End:** October 11

## October 2026 Cycle
- **Submission:** October 12
- **Reviewer Registration:** TBA
- **Reviews Due:** TBA
- **Author Response:** TBA
- **Meta-reviews Released:** TBA
- **Cycle End:** December 20

The schedule reflects the transition to "10-week cycles" rather than the previous 8-week format, with several dates still to be announced for the later cycles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b93cea6-928d-4337-b1e4-82fa124943ea",
  "isSidechain": true,
  "promptId": "3b2a0dd8-0f9a-47fd-8a8e-13648a0f38b8",
  "agentId": "aeb9333e77b766700",
  "type": "user",
  "uuid": "f7a3e10a-fccc-4565-8f5b-29b6a281114a",
  "sourceToolAssistantUUID": "1b93cea6-928d-4337-b1e4-82fa124943ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-11T23:41:32.085Z_

Here is what I found, confirmed from multiple official sources:

---

**Yes, the May 25, 2026 ARR deadline is confirmed and it is the correct target for EMNLP 2026.**

The claim in the proposal is accurate. Here are the details:

**ARR May 2026 Cycle (from aclrollingreview.org/dates):**
- Submission deadline: **May 25, 2026**
- Reviewer registration: May 27, 2026
- Reviews due: June 29, 2026
- Author response period: July 7--13, 2026
- Meta-reviews released: July 30, 2026
- Cycle end: August 2, 2026

**EMNLP 2026 Timeline (from 2026.emnlp.org/calls/main_conference_papers/):**
- ARR submission deadline (long & short papers): **May 25, 2026**
- EMNLP commitment deadline: **August 2, 2026** (aligns exactly with the May cycle end)
- Acceptance notification: August 20, 2026
- Camera-ready papers due: September 20, 2026
- Main conference: **October 24--29, 2026** (Budapest, Hungary)

**Key finding:** The ARR May 2026 cycle is explicitly designed to feed into EMNLP 2026. The EMNLP commitment deadline (August 2) matches the May cycle end date exactly. This is also confirmed by EMNLP 2026's official X/Twitter account, which announced the ARR submission deadline of May 25, 2026 in their first call for papers.

**Important policy note from the EMNLP 2026 CFP:** For the May 2026 ARR cycle, authors must declare their intended venue (EMNLP 2026) at submission time. Papers that do not select EMNLP during ARR submission cannot subsequently commit to the conference, though papers from earlier ARR cycles remain eligible for commitment.

**One detail worth noting:** ARR switched from 8-week to 10-week review cycles starting May 2025, so the submission deadline is May 25 (not the 15th, which was the old pattern). All deadlines are 11:59 PM UTC-12:00 ("anywhere on Earth").

Sources:
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Rolling Review -- Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 Official Announcement on X](https://x.com/emnlpmeeting/status/2029508292637061462)
- [ACL Rolling Review -- Call for Papers](http://aclrollingreview.org/cfp)
- [EMNLP 2026 on AI Conference Deadlines](https://mlciv.com/ai-deadlines/conference/?id=emnlp26)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7a3e10a-fccc-4565-8f5b-29b6a281114a",
  "isSidechain": true,
  "agentId": "aeb9333e77b766700",
  "requestId": "req_011CawfbNsEkJeqshWL8mYUR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c6b9818-db8f-4f67-9c47-1c5384b18a62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a2713352-4566-4df3-8c81-67a4dd2758a1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXkU1NqMu2KTZfheCBpR6B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 14321,
      "output_tokens": 729,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 905
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 729,
          "cache_read_input_tokens": 14321,
          "cache_creation_input_tokens": 905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 905,
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
