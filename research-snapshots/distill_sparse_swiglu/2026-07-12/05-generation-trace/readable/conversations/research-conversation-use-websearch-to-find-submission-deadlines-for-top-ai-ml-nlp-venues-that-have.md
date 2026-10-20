# Research conversation: Use WebSearch to find submission deadlines for top AI/ML/NLP venues that have NOT yet passed as of 2026-05-14. Search fo

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a389f1109bc15a10b.jsonl`
- **Structured JSON:** [`7241fec783bd58377c3d.json`](../../sessions/72/7241fec783bd58377c3d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-14T14:33:16.670Z_

Use WebSearch to find submission deadlines for top AI/ML/NLP venues that have NOT yet passed as of 2026-05-14. Search for:

1. "NeurIPS 2026 submission deadline"
2. "EMNLP 2026 submission deadline"
3. "AAAI 2027 submission deadline"
4. "NAACL 2026 submission deadline" or "NAACL 2027 submission deadline"
5. "ACL 2026 submission deadline" or "ACL 2027 submission deadline"
6. "ICLR 2027 submission deadline"
7. "COLM 2026 submission deadline"
8. "ICML 2026 submission deadline" (check if already passed)
9. "ARR June 2026 deadline" or "ACL Rolling Review 2026 deadlines"

For each venue, report: venue name, submission deadline date, notification date if available. I need to know which top-tier venues still have open deadlines after May 14, 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "156cd4d2-09d4-468e-8103-048a3058ee61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T14:33:16.674Z_

```json
{
  "parentUuid": "156cd4d2-09d4-468e-8103-048a3058ee61",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
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
  "uuid": "895eae09-65be-46bc-8aa4-f27fbcae6b2a",
  "timestamp": "2026-05-14T14:33:16.674Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T14:33:23.334Z_



I'll search for all these venue deadlines. Let me start by loading the WebSearch tool schema, then run the searches in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "895eae09-65be-46bc-8aa4-f27fbcae6b2a",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dEKhgtnu271SgAg8Yi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64d74f04-a22f-49fc-8f70-f0a776d6cf99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEGAesJeNnJ3xTPhADTq6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 792,
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

_source line 4 · 2026-05-14T14:33:25.738Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01A2uHCcY6qmcFzDvtFZAa4r`</summary>

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
  "parentUuid": "64d74f04-a22f-49fc-8f70-f0a776d6cf99",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dEKhgtnu271SgAg8Yi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01016a67-9499-4250-91bd-e3853a51269f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEGAesJeNnJ3xTPhADTq6f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 792,
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

_source line 5 · 2026-05-14T14:33:25.743Z_

<details><summary>↩ Tool result · `toolu_01A2uHCcY6qmcFzDvtFZAa4r`</summary>

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
  "parentUuid": "01016a67-9499-4250-91bd-e3853a51269f",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "7641b739-598d-41bf-9643-322132ed974a",
  "sourceToolAssistantUUID": "01016a67-9499-4250-91bd-e3853a51269f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T14:33:29.489Z_



Now let me run all the searches in parallel batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7641b739-598d-41bf-9643-322132ed974a",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dF1S7x37Y6Fvh9WGva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "20e5196b-2b13-44f8-a204-5c632ed05461",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRVJHAPRUkantLuyUPdV27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 7 · 2026-05-14T14:33:30.024Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014wUqwFLJ2CqVdDx7UpGwnp`</summary>

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
  "parentUuid": "20e5196b-2b13-44f8-a204-5c632ed05461",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dF1S7x37Y6Fvh9WGva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7aefbdf-be55-4afc-97ef-6b4a4ecaeb8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRVJHAPRUkantLuyUPdV27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 8 · 2026-05-14T14:33:30.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VhqTfdk2wkhkBZL5xD7bjt`</summary>

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
  "parentUuid": "b7aefbdf-be55-4afc-97ef-6b4a4ecaeb8c",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dF1S7x37Y6Fvh9WGva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "206c239e-8d92-4556-b657-67c2872423b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRVJHAPRUkantLuyUPdV27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 9 · 2026-05-14T14:33:30.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KvbuvEgSVuCis3ZQdcCzjP`</summary>

```json
{
  "query": "AAAI 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "206c239e-8d92-4556-b657-67c2872423b0",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dF1S7x37Y6Fvh9WGva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "084e57ea-54b5-4732-9c1f-f98902e3d840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRVJHAPRUkantLuyUPdV27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 10 · 2026-05-14T14:33:30.912Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012CGgqf9h6s2AR7RE5hcAUS`</summary>

```json
{
  "query": "NAACL 2026 or 2027 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "084e57ea-54b5-4732-9c1f-f98902e3d840",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dF1S7x37Y6Fvh9WGva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "632acf7e-d0bb-43ad-be52-fb5b5c3e3338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRVJHAPRUkantLuyUPdV27",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 11 · 2026-05-14T14:33:31.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BHbycanbE61oCXYjMwpwei`</summary>

```json
{
  "query": "ACL 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "632acf7e-d0bb-43ad-be52-fb5b5c3e3338",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dF1S7x37Y6Fvh9WGva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9201373f-1200-4a02-85ce-72397c17f450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRVJHAPRUkantLuyUPdV27",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9015,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 255,
          "cache_read_input_tokens": 9015,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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

_source line 12 · 2026-05-14T14:33:34.261Z_

<details><summary>↩ Tool result · `toolu_014wUqwFLJ2CqVdDx7UpGwnp`</summary>

```text
Web search results for query: "NeurIPS 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"NeurIPS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026%2FConference"},{"title":"2026 Conference","url":"https://neurips.cc/"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"NeurIPS Conference (@NeurIPSConf) / X","url":"https://x.com/NeurIPSConf"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"NeurIPS Conference on X: \"The NeurIPS 2026 submission site opening has been moved to April 15th. Note that all tracks (Main Submission, Evaluations &amp; Datasets, and Position Papers) share the same dates. The final submission deadlines remain unchanged: • Paper Abstracts: May 4th (AOE) • Full Papers:\" / X","url":"https://x.com/NeurIPSConf/status/2041303457554940336"}]

Based on the search results, here is the submission deadline information for NeurIPS 2026:

The abstract submission deadline is May 4, 2026 (AOE), and the full paper submission deadline, including all supplementary materials, is May 6, 2026 AOE.

The NeurIPS 2026 submission site opening has been moved to April 15th. 

The different tracks (main, evaluations and datasets, position papers) have different calls for papers, different submission portals, and possibly different timelines.

Additionally, author notification is scheduled for September 24, 2026 (AoE), and the conference will be held December 6th through 12th, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7aefbdf-be55-4afc-97ef-6b4a4ecaeb8c",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "6f266c04-bef5-49fe-9555-a93edc7d3aa7",
  "sourceToolAssistantUUID": "b7aefbdf-be55-4afc-97ef-6b4a4ecaeb8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T14:33:35.488Z_

<details><summary>↩ Tool result · `toolu_01VhqTfdk2wkhkBZL5xD7bjt`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key submission deadlines for EMNLP 2026:

The ARR submission deadline for long and short papers is May 25, 2026, and the reviewer registration deadline for all authors is May 27, 2026.

After the review process, the EMNLP commitment deadline is August 2, 2026, and the notification of acceptance for long and short papers is August 20, 2026.

Additionally, camera-ready papers are due September 20, 2026.

The conference itself will be held in Budapest, Hungary from October 24th to October 29th, 2026.

All deadlines are 11:59 PM UTC-12:00 (anywhere on Earth).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "206c239e-8d92-4556-b657-67c2872423b0",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "eefa1407-c374-46ed-b095-05a4ff467417",
  "sourceToolAssistantUUID": "206c239e-8d92-4556-b657-67c2872423b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T14:33:35.906Z_

<details><summary>↩ Tool result · `toolu_012CGgqf9h6s2AR7RE5hcAUS`</summary>

```text
Web search results for query: "NAACL 2026 or 2027 submission deadline"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"},{"title":"Links - Human Language Intelligence Lab","url":"https://hli.skku.edu/links"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"Upcoming ACL-Sponsored Events | ACL Member Portal","url":"https://www.aclweb.org/portal/acl_sponsored_events?order=field_event_country&sort=desc"},{"title":"NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"Where's Dan: Conference and Grant Deadlines","url":"https://web.stanford.edu/~jurafsky/deadlines.html"},{"title":"NAACL HLT 2027 (@naaclmeeting) / Posts / X","url":"https://x.com/naaclmeeting?lang=en"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"}]

Based on the search results, I can provide you with information about NAACL submission deadlines:

NAACL 2025 uses the ARR (ACL Rolling Review) system exclusively, which means submissions are not handled through direct conference submissions but rather through the rolling review process.

NAACL's paper submission deadline is usually in December, with the conference held in June.

However, the search results indicate that some 2026/2027 CFPs (Calls for Papers) are not yet posted. Since we're currently in May 2026, the 2026 conference information may already have passed, and the 2027 CFP details may not yet be available.

For the most current and specific submission deadlines for NAACL 2026 or 2027, I recommend checking:
- The official NAACL website at naacl.org
- The ACL Rolling Review website at aclrollingreview.org for deadline information if they're using the ARR system

Would you like me to search for more specific information about either NAACL 2026 or 2027?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "632acf7e-d0bb-43ad-be52-fb5b5c3e3338",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "e90360f9-1e7f-4e89-9f1b-6b9302c7c5e1",
  "sourceToolAssistantUUID": "632acf7e-d0bb-43ad-be52-fb5b5c3e3338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T14:33:35.938Z_

<details><summary>↩ Tool result · `toolu_01KvbuvEgSVuCis3ZQdcCzjP`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AAAI Conference on Artificial Intelligence","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"}]

Based on the search results, here's what I found about the AAAI 2027 submission deadline:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027. However, the AAAI 2027 paper submission deadline is TBD (UTC-12).

According to the search results, no deadlines have been announced yet for AAAI 2027. That said, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

For official and up-to-date information, you can check the official AAAI 2027 call for papers at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "084e57ea-54b5-4732-9c1f-f98902e3d840",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "d350a789-fe7b-4c38-98d1-d1f793c16a6d",
  "sourceToolAssistantUUID": "084e57ea-54b5-4732-9c1f-f98902e3d840",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T14:33:37.041Z_

<details><summary>↩ Tool result · `toolu_01BHbycanbE61oCXYjMwpwei`</summary>

```text
Web search results for query: "ACL 2026 submission deadline"

Links: [{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL 2026","url":"http://aideadlines.org/conference/?id=acl26"},{"title":"ACL 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=acl26"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"LINGUIST List 37.181 Confs: 64th Annual Meeting of the Association for Computational Linguistics: Industry Track (USA)","url":"https://linguistlist.org/issues/37/181/"},{"title":"ACL 2026 in California: Dates, Deadline, Fees & Registration Steps - Conference Inc.","url":"https://conferenceinc.net/post/acl/"},{"title":"LINGUIST List 36.2630 Confs: Joint Call for Tutorial Proposals: EACL/ACL 2026 (Online)","url":"https://linguistlist.org/issues/36/2630/"}]

Based on the search results, here's information about ACL 2026 submission deadlines:

The 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026) will take place in San Diego, California, from July 2 - 7, 2026.

ACL 2026 uses the ACL Rolling Review (ARR) exclusively for main conference submissions. This means there isn't a single paper submission deadline for the main conference. Instead, the ARR switched to 10-week review cycles starting in May 2025, and papers can be submitted to ARR at various times throughout the year and then committed to ACL 2026.

However, if you're interested in the **Industry Track**, the paper submission deadline is February 14, 2026. Note that the ACL 2026 Industry Track does not use ARR.

All deadlines are 11:59 pm UTC -12h (anywhere on earth).

For more specific information about ARR submission windows and commitment deadlines for ACL 2026, you may want to check the official ACL 2026 website or the ACL Rolling Review platform directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9201373f-1200-4a02-85ce-72397c17f450",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "13c5f094-0290-40e3-b664-0ca8e64f1707",
  "sourceToolAssistantUUID": "9201373f-1200-4a02-85ce-72397c17f450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-14T14:33:39.395Z_

Now let me search for the remaining venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13c5f094-0290-40e3-b664-0ca8e64f1707",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dFpqvF1yLcxXjpsaQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e43f8d59-3df6-4695-94de-09612d4d9036",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXXvzxEmBKo1qKhW7QTsWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3821,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3821,
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

_source line 18 · 2026-05-14T14:33:39.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JRZj4C2rksC5CcAtbrwcsL`</summary>

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
  "parentUuid": "e43f8d59-3df6-4695-94de-09612d4d9036",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dFpqvF1yLcxXjpsaQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca9006b5-d2c8-494b-9d3f-02eb5e7b7eb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXXvzxEmBKo1qKhW7QTsWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3821,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3821,
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

_source line 19 · 2026-05-14T14:33:40.335Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BRfAZY6XqXoFG6Ks9hNCf1`</summary>

```json
{
  "query": "COLM 2026 submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca9006b5-d2c8-494b-9d3f-02eb5e7b7eb3",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dFpqvF1yLcxXjpsaQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5aca0c3-f004-4611-bae7-5138d99781ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXXvzxEmBKo1qKhW7QTsWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3821,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3821,
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

_source line 20 · 2026-05-14T14:33:40.347Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EoDNy4cWxqj86Y6mFfhN6w`</summary>

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
  "parentUuid": "e5aca0c3-f004-4611-bae7-5138d99781ed",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dFpqvF1yLcxXjpsaQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f7a793a-bbb9-427a-9644-e7f609f94300",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXXvzxEmBKo1qKhW7QTsWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3821,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3821,
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

_source line 21 · 2026-05-14T14:33:40.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B2tZVMj5PmEjLYkvmnj2wK`</summary>

```json
{
  "query": "ACL Rolling Review June 2026 deadline ARR 2026 deadlines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f7a793a-bbb9-427a-9644-e7f609f94300",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dFpqvF1yLcxXjpsaQU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04a11e83-9f87-4125-ad19-e3435a79977e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXXvzxEmBKo1qKhW7QTsWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3821,
      "cache_read_input_tokens": 10432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3821,
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

_source line 22 · 2026-05-14T14:33:43.498Z_

<details><summary>↩ Tool result · `toolu_01BRfAZY6XqXoFG6Ks9hNCf1`</summary>

```text
Web search results for query: "COLM 2026 submission deadline"

Links: [{"title":"COLM 2026: Key Dates","url":"https://colmweb.org/dates.html"},{"title":"COLM 2026: Call for Papers","url":"https://colmweb.org/cfp.html"},{"title":"Conference on Language Modeling on X: \"COLM 2026 is just around the corner! Mark your calendars for: 💡Abstract deadline: Thursday, March 26, 2026 📄Full paper submission deadline: Tuesday, March 31, 2026 Call for papers in thread (website coming soon). https://t.co/YfjLxzCqxO\" / X","url":"https://x.com/COLM_conf/status/2000952051212415394"},{"title":"COLM 2026","url":"https://colmweb.org/"},{"title":"COLM 2026: Submission Instructions","url":"https://colmweb.org/submission-instructions.html"},{"title":"COLM 2026: Author Guide","url":"https://colmweb.org/AuthorGuide.html"},{"title":"Conference on Language Modeling (COLM), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-colm.html"},{"title":"When is COLM 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/colm"},{"title":"COLM 2026 Conference | OpenReview","url":"https://openreview.net/group?id=colmweb.org%2FCOLM%2F2026%2FConference"},{"title":"Conference on Language Modeling (@COLM_conf) / Posts ...","url":"https://x.com/COLM_conf"}]

Based on the search results, here are the COLM 2026 submission deadlines:

The abstract submission deadline is Thursday, March 26, 2026, and the full paper submission deadline is Tuesday, March 31, 2026.

Additionally, there is also a workshop submission deadline: the suggested submission deadline for workshop contributions is June 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5aca0c3-f004-4611-bae7-5138d99781ed",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "a631cc21-822b-485a-a425-384676004cbe",
  "sourceToolAssistantUUID": "e5aca0c3-f004-4611-bae7-5138d99781ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T14:33:43.845Z_

<details><summary>↩ Tool result · `toolu_01EoDNy4cWxqj86Y6mFfhN6w`</summary>

```text
Web search results for query: "ICML 2026 submission deadline"

Links: [{"title":"2026 Dates and Deadlines","url":"https://icml.cc/Conferences/2026/Dates"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"ICML 2026: Strictest New Rules Ever - LLMs Banned as Authors, Papers with AI Abuse Rejected","url":"https://eu.36kr.com/en/p/3540848514510723"},{"title":"ICML 2026 Call for Post-Conference Workshops","url":"https://icml.cc/Conferences/2026/CallForWorkshops"},{"title":"ICML 2026","url":"https://conferences-basecamp.informatik.uni-hamburg.de/conference/?id=icml26"},{"title":"ICML 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FConference"},{"title":"ICML 2026","url":"https://icml.cc/"},{"title":"ICML 2026 Author Instructions","url":"https://icml.cc/Conferences/2026/AuthorInstructions"},{"title":"ICML 2026 Call For Position Papers","url":"https://icml.cc/Conferences/2026/CallForPositionPapers"},{"title":"Update ICML 2025 and 2026 conference data · huggingface/ai-deadlines at 55d2124","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/55d21240bacc3ac62397280592b3dd5ded9e5683"}]

Based on the search results, the ICML 2026 paper submission deadline is January 28, 2026. Abstract and paper submission deadlines are strict, and in no circumstances will extensions be given.

Additionally, for position papers track, the deadline is January 29, 2026, 12 Noon UTC-0.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f7a793a-bbb9-427a-9644-e7f609f94300",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "06259b10-e962-4542-8eac-fcd04287408f",
  "sourceToolAssistantUUID": "9f7a793a-bbb9-427a-9644-e7f609f94300",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T14:33:44.777Z_

<details><summary>↩ Tool result · `toolu_01JRZj4C2rksC5CcAtbrwcsL`</summary>

```text
Web search results for query: "ICLR 2027 submission deadline"

Links: [{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"International Conference on Learning Representations - Wikipedia","url":"https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"ICLR 2026","url":"https://iclr.cc/"}]

Based on the search results, I found limited specific information about the ICLR 2027 submission deadline. ICLR 2027 is scheduled to take place May 16-21, 2027 in Toronto, Canada, but the exact submission deadline has not yet been officially published.

One source predicts the submission deadline to be July 31, 2027, based on the 2026 schedule pattern, but this is not confirmed. Since ICLR typically follows an annual cycle with submission deadlines occurring several months before the conference, the actual deadline will likely be announced on the official ICLR website once the call for papers is released.

For the most accurate and up-to-date information, I recommend checking the official ICLR website at iclr.cc or their OpenReview submission portal once the 2027 call for papers is announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca9006b5-d2c8-494b-9d3f-02eb5e7b7eb3",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "5803a90a-0cab-43b3-a851-c3358a8ad0bc",
  "sourceToolAssistantUUID": "ca9006b5-d2c8-494b-9d3f-02eb5e7b7eb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T14:33:47.377Z_

<details><summary>↩ Tool result · `toolu_01B2tZVMj5PmEjLYkvmnj2wK`</summary>

```text
Web search results for query: "ACL Rolling Review June 2026 deadline ARR 2026 deadlines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, I found information about ARR 2026 deadlines. However, I notice the search results don't contain specific information about an "ACL Rolling Review June 2026 deadline." Let me provide you with the key ARR 2026 deadlines that are available:

## ARR 2026 Deadlines

Starting in May 2025, ARR switched to 10-week review cycles, which means there are generally 5 cycles per year instead of 6.

### ARR 2026 January Cycle
The submission deadline for papers is January 5, 2026. The deadline for completing the author registration form is January 7th, 2026 EoD AoE. 

The deadline for reviews is February 7th, and for meta-reviews March 3rd.

### Key Information
Starting from 2024, all main *ACL conferences used ARR exclusively, including ACL 2026.

If you're looking for a specific June 2026 ARR cycle deadline, the current search results don't show a June 2026 cycle. Based on the 10-week cycle schedule with cycles generally occurring 5 times per year, a June 2026 submission window may not be scheduled, but I recommend checking the official [ARR dates page](http://aclrollingreview.org/dates) for the complete calendar of all 2026 cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04a11e83-9f87-4125-ad19-e3435a79977e",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "6939b9c6-bfdc-4a17-894b-d641801afaf1",
  "sourceToolAssistantUUID": "04a11e83-9f87-4125-ad19-e3435a79977e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T14:33:50.562Z_

Let me get more specific details on the ARR cycle schedule and a few venues that need clarification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6939b9c6-bfdc-4a17-894b-d641801afaf1",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dGb7ShZVBaxq2s6581",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe1a5db8-a0bb-411c-a0bf-b4983c2deb7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4D11muEQwy7Xz3TsSwL8D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2772,
      "cache_read_input_tokens": 14253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2772,
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

_source line 27 · 2026-05-14T14:33:50.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pn3SESohKwM3AdrLArBaeg`</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission cycles schedule dates aclrollingreview.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe1a5db8-a0bb-411c-a0bf-b4983c2deb7e",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dGb7ShZVBaxq2s6581",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1296129-caaa-408c-a467-b261aeaec62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4D11muEQwy7Xz3TsSwL8D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2772,
      "cache_read_input_tokens": 14253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2772,
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

_source line 28 · 2026-05-14T14:33:51.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fd2aRVJ7F7ybdoUcLK7sxA`</summary>

```json
{
  "query": "NeurIPS 2026 notification date acceptance decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1296129-caaa-408c-a467-b261aeaec62c",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dGb7ShZVBaxq2s6581",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b92eee38-7831-47f5-bd93-cb012576850c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4D11muEQwy7Xz3TsSwL8D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2772,
      "cache_read_input_tokens": 14253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2772,
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

_source line 29 · 2026-05-14T14:33:52.400Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YAWCG3sj1gNPD7WCT5fAAH`</summary>

```json
{
  "query": "NAACL 2026 conference date commitment deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b92eee38-7831-47f5-bd93-cb012576850c",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dGb7ShZVBaxq2s6581",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d79b7a9c-7e5d-4b98-a1df-3bb40c89f8c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4D11muEQwy7Xz3TsSwL8D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2772,
      "cache_read_input_tokens": 14253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2772,
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

_source line 30 · 2026-05-14T14:33:52.651Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J8UXHpC1GkLNoxb6rZCtUK`</summary>

```json
{
  "query": "AAAI 2027 call for papers deadline date expected"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d79b7a9c-7e5d-4b98-a1df-3bb40c89f8c6",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dGb7ShZVBaxq2s6581",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c49bed0-ad4b-4aa0-97d6-f56852e5ca91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4D11muEQwy7Xz3TsSwL8D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2772,
      "cache_read_input_tokens": 14253,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2772
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 14253,
          "cache_creation_input_tokens": 2772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2772,
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

_source line 31 · 2026-05-14T14:33:56.320Z_

<details><summary>↩ Tool result · `toolu_01Fd2aRVJ7F7ybdoUcLK7sxA`</summary>

```text
Web search results for query: "NeurIPS 2026 notification date acceptance decision"

Links: [{"title":"2026 Dates and Deadlines","url":"https://neurips.cc/Conferences/2026/Dates"},{"title":"2026 Conference","url":"https://neurips.cc/"},{"title":"NeurIPS 2026 Call for Workshops","url":"https://neurips.cc/Conferences/2026/CallForWorkshops"},{"title":"Call for Papers 2026","url":"https://neurips.cc/Conferences/2026/CallForPapers"},{"title":"NeurIPS 2026 Call For Competitions","url":"https://neurips.cc/Conferences/2026/CallForCompetitions"},{"title":"Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01"},{"title":"NeurIPS 2026 Evaluations & Datasets Track Call for Papers","url":"https://neurips.cc/Conferences/2026/CallForEvaluationsDatasets"},{"title":"NeurIPS: Neural Information Processing Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2212"},{"title":"Guidance for NeurIPS Workshop Proposals 2026","url":"https://neurips.cc/Conferences/2026/WorkshopsGuidance"},{"title":"2025 Dates and Deadlines","url":"https://neurips.cc/Conferences/2025/Dates"}]

Based on the search results, here are the key notification dates for NeurIPS 2026:

## Paper Submissions

The author notification date for paper submissions is September 24, 2026 (AoE).

## Workshop Submissions

The workshop acceptance notification date is July 11, 2026, AoE. Additionally, the mandatory accept/reject notification date is September 29, 2026, AoE.

## Competition Submissions

The acceptance notification for competition proposals is June 15, 2026.

The main conference itself will be held from December 6th through December 12th, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b92eee38-7831-47f5-bd93-cb012576850c",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "12cdb748-7389-4035-af41-6c0798b1a536",
  "sourceToolAssistantUUID": "b92eee38-7831-47f5-bd93-cb012576850c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T14:33:56.828Z_

<details><summary>↩ Tool result · `toolu_01J8UXHpC1GkLNoxb6rZCtUK`</summary>

```text
Web search results for query: "AAAI 2027 call for papers deadline date expected"

Links: [{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"}]

Based on the search results, here's what I found regarding AAAI 2027:

The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027.

Regarding the call for papers deadline, the paper submission deadline is currently listed as TBD. However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

The official AAAI 2027 call for papers page at https://aaai.org/conference/aaai/aaai-27/ should have the most up-to-date information once the deadlines are officially announced.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c49bed0-ad4b-4aa0-97d6-f56852e5ca91",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "d0319fea-f5cc-4570-83e6-94bfd89793d0",
  "sourceToolAssistantUUID": "3c49bed0-ad4b-4aa0-97d6-f56852e5ca91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T14:33:57.546Z_

<details><summary>↩ Tool result · `toolu_01Pn3SESohKwM3AdrLArBaeg`</summary>

```text
Web search results for query: "ACL Rolling Review 2026 submission cycles schedule dates aclrollingreview.org"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Allow Early Submissions to ACL 2026 in the October ARR Cycle | ACL Member Portal","url":"https://www.aclweb.org/portal/content/allow-early-submissions-acl-2026-october-arr-cycle"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"}]

Based on the search results from aclrollingreview.org, here's the information about the ACL Rolling Review 2026 submission cycles:

## Schedule Changes for 2026

ACL switched to 10-week review cycles starting in May 2025, replacing the previous 8-week cycles. This means there will generally be 5 cycles a year instead of 6, with more reasonable timelines for the review tasks and author response.

## January 2026 Cycle Deadlines

For the January 2026 cycle, here are the key dates:

- Submission deadline: January 5, 2026
- Author registration form deadline: January 7th 2026 End of Day (AoE)
- Reviews deadline: February 7th; Meta-reviews deadline: March 3rd
- ARR reviews & meta-reviews available to authors: March 10, 2026

## Important Author Policies

All authors must sign up as reviewers, with assignments made based on their qualifications. Papers whose authors have not registered as reviewers or completed their checklists by the designated deadline will be automatically desk-rejected.

The ARR website also notes that submissions based on the Word template will be desk-rejected starting from March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1296129-caaa-408c-a467-b261aeaec62c",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "5f653a6d-1c92-4d93-b844-e70e0b896d2e",
  "sourceToolAssistantUUID": "d1296129-caaa-408c-a467-b261aeaec62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T14:33:58.548Z_

<details><summary>↩ Tool result · `toolu_01YAWCG3sj1gNPD7WCT5fAAH`</summary>

```text
Web search results for query: "NAACL 2026 conference date commitment deadline ARR"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Second Call for Main Conference Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/calls/papers/"},{"title":"NAACL 2026 - Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/naacl"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"NAACL: North American Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2170"},{"title":"2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics - NAACL-HLT 2025","url":"https://2025.naacl.org/"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Submission Dates and Process for EACL/NAACL and ACL 2024 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/submission-dates-and-process-eaclnaacl-and-acl-2024"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"NAACL: Nations of the Americas Chapter of the ACL (Association for Computational Linguistics)","url":"https://naacl.org/"}]

Based on the search results, I found information about NAACL 2025 and general information about how NAACL 2026 will use ARR, but specific details about NAACL 2026's conference date and commitment deadline are not fully detailed in these results.

Here's what I can tell you:

**NAACL 2025 Information:**
At each cycle, after a paper has been fully reviewed, authors have the option to commit their paper to a conference, or revise and resubmit for another round of reviews. Papers that have received reviews and a meta-review from ARR may be committed to NAACL using the commitment link, which will be available only two weeks before the commitment deadline.

**NAACL 2026 General Information:**
Starting from 2024, all main *ACL conferences used ARR exclusively, including: ACL 2026 · EACL 2026 · NAACL 2025. This indicates that NAACL 2026 will also use ARR, though the specific conference date and commitment deadline for NAACL 2026 were not found in the search results.

For the specific conference dates and commitment deadlines for NAACL 2026, you may need to check the official NAACL 2026 website or call for papers when it's published.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d79b7a9c-7e5d-4b98-a1df-3bb40c89f8c6",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "df3918bd-8f26-472f-867a-0c4e11802e00",
  "sourceToolAssistantUUID": "d79b7a9c-7e5d-4b98-a1df-3bb40c89f8c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T14:34:01.257Z_

Let me get a couple more details - the full ARR cycle schedule and COLM/EMNLP notification dates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df3918bd-8f26-472f-867a-0c4e11802e00",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dHQi9qPwetLnrr25ft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a0f9aa4-2c75-435e-ac58-de95d576fb0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fH24cf3ey1oJnUmf73VmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 2491,
      "cache_read_input_tokens": 17025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2491,
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

_source line 36 · 2026-05-14T14:34:02.203Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H7dWF6xRibkHFEyCjxyMsG`</summary>

```json
{
  "query": "ARR 2026 all submission cycle dates March May July September"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a0f9aa4-2c75-435e-ac58-de95d576fb0a",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dHQi9qPwetLnrr25ft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b94e270e-dbc2-4831-bfe1-cfe068b29cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fH24cf3ey1oJnUmf73VmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 2491,
      "cache_read_input_tokens": 17025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2491,
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

_source line 37 · 2026-05-14T14:34:02.675Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C85AwrUVg9WumEfJLY11Re`</summary>

```json
{
  "query": "COLM 2026 notification date acceptance decision conference date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b94e270e-dbc2-4831-bfe1-cfe068b29cac",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dHQi9qPwetLnrr25ft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "897a1aeb-3a77-439d-9df5-f0c0729c5467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fH24cf3ey1oJnUmf73VmX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 2491,
      "cache_read_input_tokens": 17025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2491,
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

_source line 38 · 2026-05-14T14:34:02.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MRfCaPecLmNQTcg7VAtPb2`</summary>

```json
{
  "query": "ICLR 2027 expected submission deadline October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "897a1aeb-3a77-439d-9df5-f0c0729c5467",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dHQi9qPwetLnrr25ft",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32366bf4-1201-4174-9223-beee7558436c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fH24cf3ey1oJnUmf73VmX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 740,
      "cache_creation_input_tokens": 2491,
      "cache_read_input_tokens": 17025,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2491
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 740,
          "output_tokens": 189,
          "cache_read_input_tokens": 17025,
          "cache_creation_input_tokens": 2491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2491,
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

_source line 39 · 2026-05-14T14:34:07.736Z_

<details><summary>↩ Tool result · `toolu_01MRfCaPecLmNQTcg7VAtPb2`</summary>

```text
Web search results for query: "ICLR 2027 expected submission deadline October 2026"

Links: [{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"},{"title":"Key deadlines in AI and ML conferences","url":"https://scouts.yutori.com/inbox/53e01f0f-2f7a-4f63-9b38-22358e5386ac"},{"title":"International Conference on Learning Representations ICLR in August 2027 in Sydney","url":"https://waset.org/learning-representations-conference-in-august-2027-in-sydney"},{"title":"When is ICLR 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/iclr"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Year-Round Deadlines - Imranur Rahman","url":"https://imranur-rahman.github.io/deadlines/"},{"title":"ICLR 2026 Author Guide","url":"https://iclr.cc/Conferences/2026/AuthorGuide"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"International Conference on Learning Representations (ICLR)","url":"https://waset.org/learning-representations-conference"}]

I found information about ICLR 2026 submission deadlines, but the search results don't contain specific information about ICLR 2027 with an October 2026 submission deadline. 

From the search results, ICLR 2026 had a September 24 deadline for paper submissions. The results show various satellite ICLR conferences hosted on WASET with different submission deadlines, but these appear to be separate entities from the main ICLR conference.

To get accurate information about ICLR 2027's expected submission deadline, I would recommend:

1. Visiting the official ICLR website (iclr.cc) directly to check for any announced dates for ICLR 2027
2. Looking at conference deadline tracking sites like ConferenceDeadlines.com or similar resources that may have the 2027 information when it becomes available

The search results don't contain confirmed information about ICLR 2027's submission deadline being in October 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32366bf4-1201-4174-9223-beee7558436c",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "e43c117f-af6a-4365-b856-176791d276df",
  "sourceToolAssistantUUID": "32366bf4-1201-4174-9223-beee7558436c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T14:34:07.983Z_

<details><summary>↩ Tool result · `toolu_01H7dWF6xRibkHFEyCjxyMsG`</summary>

```text
Web search results for query: "ARR 2026 all submission cycle dates March May July September"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ARR 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=arr2601"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, I found information about ARR's 2026 submission schedule. ARR switched to 10-week review cycles starting in May 2025, which means the schedule changed from the previous 8-week cycles that had submission deadlines every two months.

However, the search results don't contain a complete table showing all the specific submission cycle dates for March, May, July, and September 2026. While the results reference that a table lists key dates for upcoming cycles, the actual detailed dates aren't fully visible in the search results I retrieved.

For the most current and complete ARR 2026 submission cycle dates, I recommend visiting the official ARR dates page at **aclrollingreview.org/dates**, which should have the full schedule table with all submission deadlines and important milestones for each cycle.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b94e270e-dbc2-4831-bfe1-cfe068b29cac",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "915f73ce-2460-4297-908e-923cd4ece4db",
  "sourceToolAssistantUUID": "b94e270e-dbc2-4831-bfe1-cfe068b29cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T14:34:08.577Z_

<details><summary>↩ Tool result · `toolu_01C85AwrUVg9WumEfJLY11Re`</summary>

```text
Web search results for query: "COLM 2026 notification date acceptance decision conference date"

Links: [{"title":"COLM 2026: Key Dates","url":"https://colmweb.org/dates.html"},{"title":"COLM 2026: Call for Papers","url":"https://colmweb.org/cfp.html"},{"title":"Update COLM 2026 conference data · huggingface/ai-deadlines at 24c5765","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/24c57653b9088a356b4b2d88e6a64cb4db5fbba5"},{"title":"COLM 2026","url":"https://colmweb.org/"},{"title":"colm-timeline-planning/conferences_2026.json at master · lil-lab/colm-timeline-planning","url":"https://github.com/lil-lab/colm-timeline-planning/blob/master/conferences_2026.json"},{"title":"Conference on Language Modeling (COLM), 2026 | ServiceNow AI Research","url":"https://www.servicenow.com/research/event/2026-colm.html"},{"title":"Conference on Language Modeling on X: \"COLM 2026 is just around the corner! Mark your calendars for: 💡Abstract deadline: Thursday, March 26, 2026 📄Full paper submission deadline: Tuesday, March 31, 2026 Call for papers in thread (website coming soon). https://t.co/YfjLxzCqxO\" / X","url":"https://x.com/COLM_conf/status/2000952051212415394"},{"title":"COLM 2026: FAQ","url":"https://colmweb.org/faq.html"},{"title":"COLM 2026: Call for Workshops","url":"https://colmweb.org/cfw.html"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here are the key dates for COLM 2026:

## Main Conference Deadlines and Dates

Abstract deadline: Thursday, March 26, 2026

Full paper submission deadline: Tuesday, March 31, 2026

Rebuttal period: May 22 to June 8, 2026

Decision notifications: July 8, 2026

Conference dates: October 6-9, 2026

## Workshop Dates

Workshop proposal deadline: April 14, 2026

Proposal decision notifications: May 12, 2026

Mandatory accept/reject notification for workshop contributions: July 24, 2026

## Location

COLM 2026 will take place at the Hilton Union Square in San Francisco, USA from October 6-9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "897a1aeb-3a77-439d-9df5-f0c0729c5467",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "0f860c06-ff4d-48cc-9164-1c9d159f73f2",
  "sourceToolAssistantUUID": "897a1aeb-3a77-439d-9df5-f0c0729c5467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T14:34:11.359Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ViqaLACak3Hs1VvUz4psb`</summary>

```json
{
  "query": "ARR May 2026 submission deadline cycle aclrollingreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f860c06-ff4d-48cc-9164-1c9d159f73f2",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dJ9cpvJc3XMRnoNSwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bd67332-80c4-4252-b100-2152f570c30f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8thseC8urTCt5wWkufken",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 680,
      "cache_creation_input_tokens": 2270,
      "cache_read_input_tokens": 19516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 43 · 2026-05-14T14:34:11.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KQvPHdYRnqAQjEDCRbe1ZH`</summary>

```json
{
  "query": "EMNLP 2026 ARR commitment deadline notification dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bd67332-80c4-4252-b100-2152f570c30f",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dJ9cpvJc3XMRnoNSwD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "775ed1e1-fe12-4ea5-8be2-d9093b814085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8thseC8urTCt5wWkufken",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 680,
      "cache_creation_input_tokens": 2270,
      "cache_read_input_tokens": 19516,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 680,
          "output_tokens": 116,
          "cache_read_input_tokens": 19516,
          "cache_creation_input_tokens": 2270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2270,
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

_source line 44 · 2026-05-14T14:34:15.970Z_

<details><summary>↩ Tool result · `toolu_01KQvPHdYRnqAQjEDCRbe1ZH`</summary>

```text
Web search results for query: "EMNLP 2026 ARR commitment deadline notification dates"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, here are the key ARR commitment deadline and notification dates for EMNLP 2026:

**ARR Commitment Deadline:**
EMNLP commitment deadline: August 2, 2026

**Notification of Acceptance:**
Notification of acceptance (long & short papers): August 20, 2026

**Related Key Dates:**
- ARR submission deadline (long & short papers): May 25, 2026
- Meta review released: July 30, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "775ed1e1-fe12-4ea5-8be2-d9093b814085",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "805c72bc-56d4-48ef-bae9-68732ec3f5e6",
  "sourceToolAssistantUUID": "775ed1e1-fe12-4ea5-8be2-d9093b814085",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T14:34:16.586Z_

<details><summary>↩ Tool result · `toolu_018ViqaLACak3Hs1VvUz4psb`</summary>

```text
Web search results for query: "ARR May 2026 submission deadline cycle aclrollingreview"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"How ARR works – ACL Rolling Review","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about the ARR May 2026 submission deadline cycle:

The new schedule with 10-week cycles started in May 2025, and instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response.

For the May 2026 cycle specifically:

- All authors must complete the author registration form by May 27, 2026 EoD AoE
- If you receive assignments, your reviews must be completed by July 6, or your meta-reviews - by July 29

Additionally, given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors will need to explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bd67332-80c4-4252-b100-2152f570c30f",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "0d760f65-bc75-4238-b018-cfb714171ad3",
  "sourceToolAssistantUUID": "8bd67332-80c4-4252-b100-2152f570c30f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T14:34:19.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LvnKYs2BmiMVE5xHTxvQ2N`</summary>

```json
{
  "query": "ARR July 2026 September 2026 submission cycle dates schedule"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d760f65-bc75-4238-b018-cfb714171ad3",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dJjpsbTW25mnbxxLpd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c97fdf79-b19f-452e-8cd8-c1f876d725d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsyLNhs8hzmf4EgPA8tiPS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 21786,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 851,
          "output_tokens": 67,
          "cache_read_input_tokens": 21786,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1421,
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

_source line 47 · 2026-05-14T14:34:23.895Z_

<details><summary>↩ Tool result · `toolu_01LvnKYs2BmiMVE5xHTxvQ2N`</summary>

```text
Web search results for query: "ARR July 2026 September 2026 submission cycle dates schedule"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, I found information about ARR's review cycles and schedule structure. ARR switched to 10-week cycles starting in May 2025, which replaced the previous 8-week cycle schedule.

However, the search results don't contain the specific submission cycle dates and schedule for July 2026 and September 2026. The first search result references a table with "all the key dates" for upcoming cycles on the ARR website, but the actual dates table wasn't included in the search results.

To get the specific submission deadline dates and full schedule for the July 2026 and September 2026 ARR cycles, I recommend visiting the official ARR Dates and Venues page at **http://aclrollingreview.org/dates**, which should have the complete calendar of submission deadlines, review periods, and other key milestones for those cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c97fdf79-b19f-452e-8cd8-c1f876d725d1",
  "isSidechain": true,
  "promptId": "bb079c7a-851c-4e3a-987b-fd999b2897df",
  "agentId": "a389f1109bc15a10b",
  "type": "user",
  "uuid": "7951f900-32c7-4610-ba33-0d0735efd408",
  "sourceToolAssistantUUID": "c97fdf79-b19f-452e-8cd8-c1f876d725d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-14T14:34:54.143Z_

Now I have enough information to compile a comprehensive report. Here is the summary:

---

## AI/ML/NLP Venue Deadlines -- Status as of May 14, 2026

### DEADLINES STILL OPEN (after May 14, 2026)

**1. NeurIPS 2026**
- Abstract deadline: May 4, 2026 (AOE) -- PASSED
- Full paper deadline: May 6, 2026 (AOE) -- PASSED
- **Status: CLOSED** (just barely missed)
- Notification: September 24, 2026
- Conference: December 6-12, 2026
- Source: [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)

**2. EMNLP 2026 (via ARR May cycle)**
- ARR submission deadline: **May 25, 2026** -- OPEN
- Reviewer registration deadline: May 27, 2026
- Commitment deadline: August 2, 2026
- Notification: August 20, 2026
- Camera-ready: September 20, 2026
- Conference: October 24-29, 2026, Budapest, Hungary
- Source: [EMNLP 2026](https://2026.emnlp.org/), [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)

**3. AAAI 2027**
- Submission deadline: **TBD (expected July-August 2026)**
- Conference: February 16-23, 2027, Montreal, Canada
- Source: [AAAI 2027](https://aaai.org/conference/aaai/), [AAAI 2027 on OpenReview](https://openreview.net/group?id=AAAI.org%2F2027%2FConference)

**4. ICLR 2027**
- Submission deadline: **TBD (expected ~October 2026 based on historical pattern; ICLR 2026 had a Sept 24, 2025 deadline)**
- Conference: May 16-21, 2027, Toronto, Canada
- Source: [ICLR](https://iclr.cc/), [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)

**5. ARR Future Cycles (July 2026, September 2026, etc.)**
- ARR operates on 10-week rolling cycles. The **May 2026 cycle** submission deadline is **May 25, 2026** (still open). Future cycles in July 2026 and September 2026 will also have submission deadlines. Papers reviewed via ARR can be committed to EMNLP 2026, NAACL 2027, and other future *ACL conferences.
- Source: [ARR Dates](http://aclrollingreview.org/dates)

---

### DEADLINES ALREADY PASSED (before May 14, 2026)

**6. ICML 2026**
- Paper submission deadline: January 28, 2026 -- **PASSED**
- Position papers: January 29, 2026 -- **PASSED**
- Conference: July 2026
- Source: [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)

**7. ACL 2026 (main conference via ARR)**
- ACL 2026 used ARR exclusively. The relevant ARR commitment deadline for ACL 2026 was in early 2026 (the January 2026 ARR cycle had a Jan 5 submission deadline). The conference is July 2-7, 2026, San Diego, CA.
- Industry Track deadline: February 14, 2026 -- **PASSED**
- Source: [ACL 2026](https://2026.aclweb.org/), [ACL 2026 Main Conference](https://2026.aclweb.org/calls/main_conference_papers/)

**8. COLM 2026**
- Abstract deadline: March 26, 2026 -- **PASSED**
- Full paper deadline: March 31, 2026 -- **PASSED**
- Decision notifications: July 8, 2026
- Conference: October 6-9, 2026, San Francisco
- Source: [COLM 2026 Dates](https://colmweb.org/dates.html)

**9. NAACL 2026**
- NAACL 2026 used ARR. The commitment deadline has likely already passed (NAACL typically holds its conference in the summer). NAACL 2027 details are not yet announced.
- Source: [NAACL](https://naacl.org/), [ARR Dates](http://aclrollingreview.org/dates)

**10. NeurIPS 2026** (repeated for clarity)
- Full paper deadline: May 6, 2026 -- **PASSED** (by 8 days)

---

### Summary: What Is Still Open as of May 14, 2026

| Venue | Deadline | Date | Status |
|-------|----------|------|--------|
| **EMNLP 2026** (ARR May cycle) | ARR submission | May 25, 2026 | **OPEN -- 11 days left** |
| **AAAI 2027** | Paper submission | TBD (~Jul-Aug 2026) | **Upcoming** |
| **ICLR 2027** | Paper submission | TBD (~Oct 2026) | **Upcoming** |
| **ARR future cycles** | Rolling submissions | Jul 2026, Sep 2026, etc. | **Upcoming** |
| **NAACL 2027** | Via ARR | TBD | **Not yet announced** |

The most urgent open deadline is **EMNLP 2026 via the ARR May 2026 cycle, with submissions due May 25, 2026**. After that, AAAI 2027 and ICLR 2027 will be the next major deadlines later in summer/fall 2026.

Sources:
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [EMNLP 2026](https://2026.emnlp.org/)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [AAAI Conference on AI](https://aaai.org/conference/aaai/)
- [AAAI 2027 on OpenReview](https://openreview.net/group?id=AAAI.org%2F2027%2FConference)
- [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates)
- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)
- [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates)
- [ACL 2026](https://2026.aclweb.org/)
- [ACL 2026 Main Conference Papers](https://2026.aclweb.org/calls/main_conference_papers/)
- [COLM 2026 Key Dates](https://colmweb.org/dates.html)
- [COLM 2026 Call for Papers](https://colmweb.org/cfp.html)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [NAACL](https://naacl.org/)
- [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7951f900-32c7-4610-ba33-0d0735efd408",
  "isSidechain": true,
  "agentId": "a389f1109bc15a10b",
  "requestId": "req_011Cb2dKH4L24WDwZGoXENkG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35e7222b-1a61-4f04-9258-470827282499",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "622f6a40-c195-44a2-beaf-ceeaf4491a98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNdDNQg84e3oWb8KFjYGys",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 23207,
      "output_tokens": 1952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1952,
          "cache_read_input_tokens": 23207,
          "cache_creation_input_tokens": 1565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1565,
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
