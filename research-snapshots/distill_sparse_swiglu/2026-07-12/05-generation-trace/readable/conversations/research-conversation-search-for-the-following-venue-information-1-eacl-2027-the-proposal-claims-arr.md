# Research conversation: Search for the following venue information: 1. **EACL 2027**: The proposal claims "ARR August 3, 2026 — 81 days; commitm

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa9fe07b4a9f81ef6.jsonl`
- **Structured JSON:** [`970143e668ef33adc224.json`](../../sessions/97/970143e668ef33adc224.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-14T16:05:23.790Z_

Search for the following venue information:

1. **EACL 2027**: The proposal claims "ARR August 3, 2026 — 81 days; commitment deadline October 11, 2026" as primary target. Search for:
   - Has EACL 2027 been announced? What are the actual dates?
   - What is the ARR August 2026 submission deadline?
   - Is the commitment deadline correct?

2. **EMNLP 2026**: The proposal acknowledges it's infeasible. The user's requirement says "ARR submission deadline 2026-05-25 (11 days from today 2026-05-14)". Verify this is correct.

3. **ARR cycle dates**: Search for "ARR 2026 submission deadlines" to verify the August cycle date.

4. Also search for: "AAAI 2027 submission deadline" to verify the "expected ~August 2026" claim.

Report exactly what you find. If dates cannot be confirmed, say so explicitly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "c8485a32-2e89-4d64-a191-8ccdd773366e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T16:05:23.793Z_

```json
{
  "parentUuid": "c8485a32-2e89-4d64-a191-8ccdd773366e",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
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
  "uuid": "14cf5b9d-7f94-4550-b09e-16ca301af272",
  "timestamp": "2026-05-14T16:05:23.793Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T16:05:26.967Z_



I'll search for all of these venue and deadline details in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14cf5b9d-7f94-4550-b09e-16ca301af272",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFkneae4mjZS91oHoK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88e77e15-3b88-416a-90ce-cc2f6eaed806",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRj59EuecSjFGKyVCYZaGo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 784,
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

_source line 4 · 2026-05-14T16:05:27.136Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XFbSQWxnNHnfoNuMt7vp5h`</summary>

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
  "parentUuid": "88e77e15-3b88-416a-90ce-cc2f6eaed806",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFkneae4mjZS91oHoK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30ee10be-db24-4d54-babf-97e1e57c9ff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRj59EuecSjFGKyVCYZaGo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 8223,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 784,
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

_source line 5 · 2026-05-14T16:05:27.139Z_

<details><summary>↩ Tool result · `toolu_01XFbSQWxnNHnfoNuMt7vp5h`</summary>

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
  "parentUuid": "30ee10be-db24-4d54-babf-97e1e57c9ff5",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "0b7f7e31-8a0a-4680-a464-cbf523f63a41",
  "sourceToolAssistantUUID": "30ee10be-db24-4d54-babf-97e1e57c9ff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T16:05:29.487Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b7f7e31-8a0a-4680-a464-cbf523f63a41",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFzzvNYYKEx97iNMYn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41235804-fd40-45fe-b65e-9a86b3d380ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwPNAM2qXmkCPo75vQ233A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1408,
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

_source line 7 · 2026-05-14T16:05:29.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QLxnFQoUToimufNysFh1EL`</summary>

```json
{
  "query": "EACL 2027 conference dates location announcement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41235804-fd40-45fe-b65e-9a86b3d380ab",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFzzvNYYKEx97iNMYn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a7354c6-c92e-45c1-aac3-69b946bf3ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwPNAM2qXmkCPo75vQ233A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1408,
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

_source line 8 · 2026-05-14T16:05:30.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Eja22HdaGetb9HZMtCzbLQ`</summary>

```json
{
  "query": "ARR August 2026 submission deadline ACL Rolling Review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a7354c6-c92e-45c1-aac3-69b946bf3ed4",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFzzvNYYKEx97iNMYn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33a64aee-e41a-4d01-a97e-b9dedc76540d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwPNAM2qXmkCPo75vQ233A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1408,
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

_source line 9 · 2026-05-14T16:05:31.412Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ES4GgZUixgPWQRo7i37MiN`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a64aee-e41a-4d01-a97e-b9dedc76540d",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFzzvNYYKEx97iNMYn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b89e6c18-110c-4123-b633-bb614e43a74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwPNAM2qXmkCPo75vQ233A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1408,
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

_source line 10 · 2026-05-14T16:05:31.416Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VBuunk2jvTQLq6hrkyCjQ9`</summary>

```json
{
  "query": "ARR 2026 submission deadlines cycle dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b89e6c18-110c-4123-b633-bb614e43a74a",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFzzvNYYKEx97iNMYn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec016569-20f0-4af1-ab14-843906a2695b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwPNAM2qXmkCPo75vQ233A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1408,
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

_source line 11 · 2026-05-14T16:05:31.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BfvBh7f3FF2mMR8d1u3Lck`</summary>

```json
{
  "query": "AAAI 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec016569-20f0-4af1-ab14-843906a2695b",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kFzzvNYYKEx97iNMYn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5810da06-65c4-4939-a555-7a56c68b6461",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwPNAM2qXmkCPo75vQ233A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 9007,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 263,
          "cache_read_input_tokens": 9007,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1408,
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

_source line 12 · 2026-05-14T16:05:33.613Z_

<details><summary>↩ Tool result · `toolu_01QLxnFQoUToimufNysFh1EL`</summary>

```text
Web search results for query: "EACL 2027 conference dates location announcement"

Links: [{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"CALL FOR BIDS TO HOST EACL 2027 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-bids-host-eacl-2027"},{"title":"EACL","url":"https://eacl.org/conferences/"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"LINGUIST List 36.2662 FYI: Call for Bids to Host the European Chapter of the Association for Computational Linguistics (EACL) Conference 2027 (Online)","url":"https://linguistlist.org/issues/36/2662/"},{"title":"The 63rd Annual Meeting of the Association for Computational Linguistics - ACL 2025","url":"https://2025.aclweb.org/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR BIDS TO HOST EACL 2027","url":"https://groups.google.com/g/ml-news/c/kpHUYDfojbE"},{"title":"Venue -","url":"https://2027.eacl.org/participants/venue/"},{"title":"EACL 2027 (@eaclmeeting.bsky.social)","url":"https://bsky.app/profile/did:plc:l76acjcnqvkmpd673433pkiw"}]

Based on the search results, here are the details about EACL 2027:

**Location and Dates:** EACL 2027 will be held in Athens, Greece from March 9-14, 2027.

**Venue:** The conference will take place at the Megaron Athens International Conference Centre (MAICC), located in the vibrant centre of Athens, Greece. MAICC spans 143,000 m² and offers 18 meeting spaces capable of accommodating up to 6,000 delegates.

**Conference Status:** The EACL 2027 website is now officially live, with regular updates expected concerning the conference, important dates, calls for papers, venue specifics, and more.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a7354c6-c92e-45c1-aac3-69b946bf3ed4",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "44b58557-b8c2-4402-b7eb-51b4ce6d2fb3",
  "sourceToolAssistantUUID": "5a7354c6-c92e-45c1-aac3-69b946bf3ed4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T16:05:34.842Z_

<details><summary>↩ Tool result · `toolu_01Eja22HdaGetb9HZMtCzbLQ`</summary>

```text
Web search results for query: "ARR August 2026 submission deadline ACL Rolling Review"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, I found information about ARR submission deadlines for August 2026. The August 2026 ARR cycle has a submission deadline of August 3, 2026. This cycle aligns with commitments to EACL 2027, which has a commitment date of October 11, 2026.

The search results also show that ACL Peer Review Committee recommended switching to 10-week review cycles, with the new schedule starting in May 2025, which means there are generally 5 cycles per year instead of 6.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33a64aee-e41a-4d01-a97e-b9dedc76540d",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "9ddbcdb7-1f62-4609-a7a1-c897a52ac915",
  "sourceToolAssistantUUID": "33a64aee-e41a-4d01-a97e-b9dedc76540d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T16:05:36.299Z_

<details><summary>↩ Tool result · `toolu_01ES4GgZUixgPWQRo7i37MiN`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key deadlines for EMNLP 2026 regarding ARR submissions and commitment:

**ARR Submission Deadline:** May 25, 2026

**EMNLP Commitment Deadline:** August 2, 2026

Additional relevant dates include:
- Reviewer registration deadline for all authors: May 27, 2026
- Meta review released: July 30, 2026
- Notification of acceptance: August 20, 2026

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

It's important to note that authors will need to explicitly declare which conference they intend to commit to at submission time for the ARR 2026 May cycle, and this choice will be binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b89e6c18-110c-4123-b633-bb614e43a74a",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "c6520186-8d84-4a81-b5c5-910c930d2997",
  "sourceToolAssistantUUID": "b89e6c18-110c-4123-b633-bb614e43a74a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T16:05:36.467Z_

<details><summary>↩ Tool result · `toolu_01BfvBh7f3FF2mMR8d1u3Lck`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline call for papers"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI 2027 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2027%2FConference"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"}]

Based on the search results, here's what I found about AAAI 2027:

**Conference Details:**
The Forty-first Conference on Artificial Intelligence will be held in Montréal, Québec, Canada from February 16-23, 2027.

**Submission Deadline:**
The AAAI 2027 paper submission deadline is TBD (UTC-12). However, submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

**Official Information:**
The official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/. The official deadline information has not yet been announced, so you may want to check that official page or the OpenReview platform for the most current details as they become available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5810da06-65c4-4939-a555-7a56c68b6461",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "20ab812c-0997-4022-be54-54e91d218474",
  "sourceToolAssistantUUID": "5810da06-65c4-4939-a555-7a56c68b6461",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T16:05:38.073Z_

<details><summary>↩ Tool result · `toolu_01VBuunk2jvTQLq6hrkyCjQ9`</summary>

```text
Web search results for query: "ARR 2026 submission deadlines cycle dates"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here are the ARR 2026 submission deadlines and cycle dates:

## 2026 ARR Schedule

Starting in May 2025, ARR switched to 10-week review cycles instead of the previous 8-week cycles. This means that instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response.

### Key 2026 Deadlines:

**January 2026 Cycle:**
- Submission deadline: January 5, 2026
- If assigned reviews, they must be completed by February 7th, and meta-reviews by March 3rd
- ARR reviews & meta-reviews available to authors: March 10, 2026

**October 2026 Cycle:**
- Submission deadline: October 12, 2026, with final commitment deadline: December 20, 2026

All deadlines are at 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec016569-20f0-4af1-ab14-843906a2695b",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "709dcbae-875c-409a-af05-a01fea816d6c",
  "sourceToolAssistantUUID": "ec016569-20f0-4af1-ab14-843906a2695b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-14T16:05:40.963Z_

Let me get more precise details on the ARR dates page and the EACL 2027 call for papers to confirm the exact deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "709dcbae-875c-409a-af05-a01fea816d6c",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kGoY8LtW7H47v5pNRR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c80a61f-753a-4d1e-b33d-efe2151feeac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3STkCKSvyU7qgS7cmAqMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 10415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
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

_source line 18 · 2026-05-14T16:05:41.919Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LsPSLMczzdNXfs1djuTqhh`</summary>

```json
{
  "query": "site:aclrollingreview.org dates 2026 August October submission commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c80a61f-753a-4d1e-b33d-efe2151feeac",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kGoY8LtW7H47v5pNRR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38ef118b-9734-43da-bf36-f584aee3ae00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3STkCKSvyU7qgS7cmAqMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 10415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
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

_source line 19 · 2026-05-14T16:05:42.387Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013vU4VDvv32pFtoVXHShdpu`</summary>

```json
{
  "query": "site:2027.eacl.org important dates commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38ef118b-9734-43da-bf36-f584aee3ae00",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kGoY8LtW7H47v5pNRR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2a0a7e7-4444-43f0-ba1b-bc48b03a89d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3STkCKSvyU7qgS7cmAqMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 10415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
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

_source line 20 · 2026-05-14T16:05:42.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0126RoYQLVQHZY8fXRtR28Tf`</summary>

```json
{
  "query": "EACL 2027 commitment deadline ARR October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2a0a7e7-4444-43f0-ba1b-bc48b03a89d6",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kGoY8LtW7H47v5pNRR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "418d6fe6-cd94-4064-8dc2-400d43c9b432",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3STkCKSvyU7qgS7cmAqMx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 10415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
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

_source line 21 · 2026-05-14T16:05:43.347Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U8VHRs8ihmxEyTroKkjvsu`</summary>

```json
{
  "query": "AAAI 2027 abstract deadline paper deadline August 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418d6fe6-cd94-4064-8dc2-400d43c9b432",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kGoY8LtW7H47v5pNRR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "075313f6-80a4-4204-bf86-5d43b677dd58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3STkCKSvyU7qgS7cmAqMx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 796,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 10415,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2979
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 796,
          "output_tokens": 251,
          "cache_read_input_tokens": 10415,
          "cache_creation_input_tokens": 2979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2979,
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

_source line 22 · 2026-05-14T16:05:45.600Z_

<details><summary>↩ Tool result · `toolu_013vU4VDvv32pFtoVXHShdpu`</summary>

```text
Web search results for query: "site:2027.eacl.org important dates commitment deadline"

Links: [{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"Organizing Committee -","url":"https://2027.eacl.org/committees/organization/"},{"title":"Venue -","url":"https://2027.eacl.org/participants/venue/"}]

Based on the search results from the EACL 2027 website, I found some information about deadlines:

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth"). However, the search results indicate that the Program Committee is currently finalizing the comprehensive Call for Papers and detailed timetable, and they are preparing to share the primary submission deadline.

The search results don't contain the specific important dates or commitment deadline information you're looking for. For complete details about the important dates and commitment deadlines for EACL 2027, I recommend visiting the main conference website at 2027.eacl.org directly, as the detailed information appears to still be in preparation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2a0a7e7-4444-43f0-ba1b-bc48b03a89d6",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "489f4f0f-9f6b-4347-8a0d-e39abf49abc2",
  "sourceToolAssistantUUID": "c2a0a7e7-4444-43f0-ba1b-bc48b03a89d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T16:05:46.710Z_

<details><summary>↩ Tool result · `toolu_01U8VHRs8ihmxEyTroKkjvsu`</summary>

```text
Web search results for query: "AAAI 2027 abstract deadline paper deadline August 2026"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"MPC Deadlines Hub","url":"https://mpc-deadlines.github.io/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information about AAAI 2027 deadlines:

For AAAI 2027, the paper deadline is August 1, 2026, and the abstract deadline is July 25. The conference will be held February 16-23, 2027 in Montréal, Québec, Canada.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "075313f6-80a4-4204-bf86-5d43b677dd58",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "5806d54e-b8d2-434a-b6b2-61e5cfa535bf",
  "sourceToolAssistantUUID": "075313f6-80a4-4204-bf86-5d43b677dd58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T16:05:46.713Z_

<details><summary>↩ Tool result · `toolu_0126RoYQLVQHZY8fXRtR28Tf`</summary>

```text
Web search results for query: "EACL 2027 commitment deadline ARR October 2026"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"The 19th Conference of the European Chapter of the Association for Computational LinguisticsRabat, MoroccoMarch 24-29, 2026 -","url":"https://2026.eacl.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"EACL: Conference of the European Chapter of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=785"},{"title":"EACL 2026 SRW ARR Commitment | OpenReview","url":"https://openreview.net/group?id=eacl.org%2FEACL%2F2026%2FSRW_ARR_Commitment"},{"title":"eaclmeeting (@eaclmeeting) / X","url":"https://x.com/eaclmeeting?lang=en"}]

Based on the search results, I found information about the EACL 2027 commitment deadline:

For EACL 2027, the ARR submission deadline is August 3, 2026, and the commitment deadline is October 11, 2026.

This means that authors who have submitted papers to ARR and received reviews must commit their papers to EACL 2027 by October 11, 2026, if they want them to be considered for publication at the conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "418d6fe6-cd94-4064-8dc2-400d43c9b432",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "46e5fa4b-7362-49cb-95dc-fbf598202478",
  "sourceToolAssistantUUID": "418d6fe6-cd94-4064-8dc2-400d43c9b432",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T16:05:47.591Z_

<details><summary>↩ Tool result · `toolu_01LsPSLMczzdNXfs1djuTqhh`</summary>

```text
Web search results for query: "site:aclrollingreview.org dates 2026 August October submission commitment"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission dates and process for 2024 Conferences","url":"http://aclrollingreview.org/submission-dates-for-2024/"},{"title":"Response to ACL 2023 Questions","url":"http://aclrollingreview.org/ACL-2023-session/"},{"title":"ARR Changelog","url":"http://aclrollingreview.org/changelog"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Dashboard","url":"https://stats.aclrollingreview.org/"}]

Based on the search results, I found information about ACL Rolling Review dates, though the specific table with August and October 2026 dates wasn't fully visible in the search results. However, I can provide you with what I found:

From October 2022 to February 2025, ARR ran 8-week review cycles with submission deadlines on the 15th of every second month. After extensive deliberation and community feedback, the ACL Peer Review Committee recommended switching to 10-week cycles, with the new schedule starting in May 2025.

The search results indicate that there is a table listing all key dates by which authors may need to take action for the upcoming cycles, but the complete table with the specific August and October 2026 submission and commitment deadlines was not fully displayed in the search results.

For the most current and complete schedule including the specific dates for August and October 2026 submissions and commitment deadlines, I recommend visiting the official ACL Rolling Review dates page directly at http://aclrollingreview.org/dates, where the full table should be available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38ef118b-9734-43da-bf36-f584aee3ae00",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "f9ca5ed3-599b-4f57-b905-4831874a419d",
  "sourceToolAssistantUUID": "38ef118b-9734-43da-bf36-f584aee3ae00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T16:05:50.448Z_

Let me do one more search to fetch the exact ARR dates table from the GitHub source to get precise cycle dates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ca5ed3-599b-4f57-b905-4831874a419d",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kHWEbb3JB7qM3c9scD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36fb56d0-40c2-41f5-a90f-f62767fd4851",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqDYPkZNHxNFVP7VTzRxrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1603,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 13394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1655,
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

_source line 27 · 2026-05-14T16:05:50.768Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UngmXqunanue4XkqHneZ2h`</summary>

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
  "parentUuid": "36fb56d0-40c2-41f5-a90f-f62767fd4851",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kHWEbb3JB7qM3c9scD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac391e1a-a42e-4ac0-9887-fb5e88b6a026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqDYPkZNHxNFVP7VTzRxrZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1603,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 13394,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1603,
          "output_tokens": 101,
          "cache_read_input_tokens": 13394,
          "cache_creation_input_tokens": 1655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1655,
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

_source line 28 · 2026-05-14T16:05:50.770Z_

<details><summary>↩ Tool result · `toolu_01UngmXqunanue4XkqHneZ2h`</summary>

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
  "parentUuid": "ac391e1a-a42e-4ac0-9887-fb5e88b6a026",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "69f76196-b667-49a6-8536-26cbd96f9786",
  "sourceToolAssistantUUID": "ac391e1a-a42e-4ac0-9887-fb5e88b6a026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T16:05:54.945Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RjST8zB9FDZkmE6YNo9KeY`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract the complete table of ARR submission deadlines and commitment deadlines for 2026, especially the May 2026, August 2026, and October 2026 cycles. Include all dates shown for each cycle (submission deadline, review deadline, meta-review deadline, commitment deadlines for each conference)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69f76196-b667-49a6-8536-26cbd96f9786",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kHk3ok2PnmetGjGoZE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "744d50db-fe23-479e-bb6d-103a91afa1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei71ReotgtWXVwdrGyxNGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2222,
      "cache_read_input_tokens": 15049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2222,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 30 · 2026-05-14T16:05:55.856Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C4rVmQ2abb1V1fnYR158Xp`</summary>

```json
{
  "url": "https://2027.eacl.org/calls/papers/",
  "prompt": "Extract all important dates, deadlines, submission information, ARR submission deadline, and commitment deadline for EACL 2027. Include any information about the ARR cycle that feeds into EACL 2027."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "744d50db-fe23-479e-bb6d-103a91afa1cc",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kHk3ok2PnmetGjGoZE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0f41cfc-cc73-4159-922f-772b0acff3b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei71ReotgtWXVwdrGyxNGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2222,
      "cache_read_input_tokens": 15049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2222,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 31 · 2026-05-14T16:05:57.030Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G8FzBZckLLKuYgvQzP8hWG`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all important dates and deadlines for EMNLP 2026 main conference papers, including ARR submission deadline, commitment deadline, notification dates, and any other key dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0f41cfc-cc73-4159-922f-772b0acff3b7",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kHk3ok2PnmetGjGoZE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebfa0ca7-a67a-48d7-aad3-3149e0bfa624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ei71ReotgtWXVwdrGyxNGK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2222,
      "cache_read_input_tokens": 15049,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 15049,
          "cache_creation_input_tokens": 2222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2222,
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

_source line 32 · 2026-05-14T16:05:58.860Z_

<details><summary>↩ Tool result · `toolu_01C4rVmQ2abb1V1fnYR158Xp`</summary>

```text
# EACL 2027 Important Dates and Submission Information

**Primary Deadline:**
- **ARR Submission Deadline:** August 3, 2026 (Anywhere on Earth)
  - Applies to both long and short papers

**Current Status:**
The conference organizers note that "Our Program Committee is currently finalizing the comprehensive Call for Papers and detailed timetable for EACL 2027." The complete call for papers details have not yet been released.

**Submission Guidance:**
Prospective authors are advised to "familiarize themselves with the ARR author guidelines" as they prepare manuscripts, with a reference to resources available at aclrollingreview.org/authors.

**Note:** This announcement indicates that EACL 2027 will use the ACL Rolling Review (ARR) system for submissions, but a full commitment deadline and additional timeline details are not yet available on this page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0f41cfc-cc73-4159-922f-772b0acff3b7",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "6a81043e-4df5-4548-998b-a53b503a2715",
  "sourceToolAssistantUUID": "a0f41cfc-cc73-4159-922f-772b0acff3b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T16:05:58.907Z_

<details><summary>↩ Tool result · `toolu_01RjST8zB9FDZkmE6YNo9KeY`</summary>

```text
# ARR 2026 Submission and Commitment Deadlines

## Review Cycles Schedule

The ARR adopted a new 10-week cycle structure starting May 2025. Here are the key dates for 2026:

**May 2026 Cycle:**
- Submission: May 25, 2026
- Reviewer registration: May 27, 2026
- Reviews due: June 29, 2026
- Author response: July 7-13, 2026
- Meta-reviews released: July 30, 2026
- Cycle end: August 2, 2026

**August 2026 Cycle:**
- Submission: August 3, 2026
- Remaining dates marked as "TBA"
- Cycle end: October 11, 2026

**October 2026 Cycle:**
- Submission: October 12, 2026
- Remaining dates marked as "TBA"
- Cycle end: December 20, 2026

## Conference Commitment Deadlines

Papers can be committed to these venues:

| Conference | Final ARR Submission | Commitment Deadline |
|---|---|---|
| EMNLP 2026 | May 25, 2026 | August 2, 2026 |
| AACL 2026 | May 25, 2026 | August 26, 2026 |
| EACL 2027 | August 3, 2026 | October 11, 2026 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "744d50db-fe23-479e-bb6d-103a91afa1cc",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "824b90a6-d5fc-40a9-a32c-392c755de160",
  "sourceToolAssistantUUID": "744d50db-fe23-479e-bb6d-103a91afa1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T16:06:01.443Z_

<details><summary>↩ Tool result · `toolu_01G8FzBZckLLKuYgvQzP8hWG`</summary>

```text
# EMNLP 2026 Main Conference Papers: Key Dates

**Submission & Review Phase:**
- "ARR submission deadline (long & short papers): May 25, 2026"
- "Reviewer registration deadline for ALL authors: May 27, 2026"
- "Author response and author-reviewer discussion: July 7 - July 13, 2026"
- "Meta review released: July 30, 2026"

**Commitment & Decision Phase:**
- "EMNLP commitment deadline: August 2, 2026"
- "Notification of acceptance (long & short papers): August 20, 2026"

**Final Submission & Conference:**
- "Camera-ready papers due (long & short): September 20, 2026"
- "Main Conference (dates for Workshops/Tutorials TBD): October 24 - 29, 2026"

**Important Note:** All deadlines are set for "11:59PM UTC-12:00 ('anywhere on Earth')". The two-stage review system requires authors to first submit through ACL Rolling Review by May 25, then commit their reviewed papers to EMNLP by August 2 before final acceptance decisions are made.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebfa0ca7-a67a-48d7-aad3-3149e0bfa624",
  "isSidechain": true,
  "promptId": "e3489f72-9f90-4393-86a8-561ce1d6a08f",
  "agentId": "aa9fe07b4a9f81ef6",
  "type": "user",
  "uuid": "37ffe663-32fd-472e-b136-f041d400e95f",
  "sourceToolAssistantUUID": "ebfa0ca7-a67a-48d7-aad3-3149e0bfa624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T16:06:27.356Z_

Here are my findings for each item:

---

## 1. EACL 2027

**Confirmed: EACL 2027 has been announced.**

- **Conference dates:** March 9-14, 2027, in Athens, Greece (Megaron Athens International Conference Centre)
- **Official website:** [2027.eacl.org](https://2027.eacl.org/)
- **ARR submission deadline:** August 3, 2026 -- confirmed on both the [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/) and the [ARR dates page](http://aclrollingreview.org/dates)
- **Commitment deadline:** October 11, 2026 -- confirmed on the [ARR dates page](http://aclrollingreview.org/dates)
- **Days between today (May 14, 2026) and August 3, 2026:** 81 days -- this is correct

**Verdict:** The proposal's claim of "ARR August 3, 2026 -- 81 days; commitment deadline October 11, 2026" is **fully correct and verified**.

Note: The EACL 2027 Call for Papers page itself states the ARR submission deadline but mentions the full detailed timetable is still being finalized by the Program Committee. However, the commitment deadline of October 11 is confirmed via the official ARR dates page.

---

## 2. EMNLP 2026

**Confirmed from the [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/):**

- **ARR submission deadline:** May 25, 2026
- **Days from today (May 14, 2026) to May 25, 2026:** 11 days -- this is correct
- **Commitment deadline:** August 2, 2026
- **Notification of acceptance:** August 20, 2026
- **Conference dates:** October 24-29, 2026

**Verdict:** The proposal's statement that the EMNLP 2026 ARR submission deadline is May 25, 2026 (11 days from today) is **correct**. The acknowledgment that this is infeasible as a primary target is reasonable given the tight timeline.

---

## 3. ARR Cycle Dates for 2026

**Confirmed from the [ARR Dates and Venues page](http://aclrollingreview.org/dates):**

ARR switched to 10-week review cycles starting May 2025. The 2026 cycles are:

| Cycle | Submission Deadline | Cycle End |
|---|---|---|
| January 2026 | January 5, 2026 | March 10, 2026 |
| May 2026 | May 25, 2026 | August 2, 2026 |
| August 2026 | August 3, 2026 | October 11, 2026 |
| October 2026 | October 12, 2026 | December 20, 2026 |

The conference commitment deadlines mapped to these cycles:
- **EMNLP 2026:** Final ARR submission May 25 / Commitment August 2, 2026
- **AACL 2026:** Final ARR submission May 25 / Commitment August 26, 2026
- **EACL 2027:** Final ARR submission August 3 / Commitment October 11, 2026

**Verdict:** The August 2026 ARR cycle date of August 3 is **confirmed**.

---

## 4. AAAI 2027

**Partially confirmed:**

- **Conference dates:** February 16-23, 2027, in Montreal, Quebec, Canada
- **Paper submission deadline:** August 1, 2026 (per [conference deadline aggregator sites](https://trybibby.com/conference-deadlines))
- **Abstract deadline:** July 25, 2026 (per the same aggregator sites)
- **Official call for papers:** Not yet published on [aaai.org](https://aaai.org/conference/aaai/) as of these search results

**Verdict:** The proposal's claim of "expected ~August 2026" for AAAI 2027 is **plausible and consistent** with what aggregator sites report (abstract July 25, paper August 1). However, **these dates have not been officially confirmed by AAAI yet** -- they appear to be estimated based on historical patterns. The official AAAI 2027 call for papers has not been released. If accurate, there would be a near-direct conflict with the ARR August 3 deadline (AAAI paper deadline August 1, ARR deadline August 3), which is worth noting for planning purposes.

---

## Summary

| Claim | Status |
|---|---|
| EACL 2027 ARR deadline August 3, 2026 (81 days) | **Confirmed** |
| EACL 2027 commitment deadline October 11, 2026 | **Confirmed** |
| EMNLP 2026 ARR deadline May 25, 2026 (11 days) | **Confirmed** |
| ARR August 2026 cycle date | **Confirmed: August 3, 2026** |
| AAAI 2027 deadline ~August 2026 | **Plausible but not officially announced** (aggregators say abstract Jul 25, paper Aug 1) |

Sources:
- [EACL 2027 Official Website](https://2027.eacl.org/)
- [EACL 2027 Call for Papers](https://2027.eacl.org/calls/papers/)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Twitter/X Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [AI & ML Conference Deadlines 2026-2027 (Bibby)](https://trybibby.com/conference-deadlines)
- [AAAI Conference Page](https://aaai.org/conference/aaai/)
- [ARR GitHub dates.md](https://github.com/acl-org/aclrollingreview/blob/main/dates.md)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37ffe663-32fd-472e-b136-f041d400e95f",
  "isSidechain": true,
  "agentId": "aa9fe07b4a9f81ef6",
  "requestId": "req_011Cb2kJXS4aiWEVgjmzyVke",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d973418-1406-4783-b646-9444cf1227fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "488bd993-e061-42c8-a01f-134c037243bc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbupbtHKUXJSC5NDaim6cu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1295,
      "cache_read_input_tokens": 17271,
      "output_tokens": 1589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1295
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1589,
          "cache_read_input_tokens": 17271,
          "cache_creation_input_tokens": 1295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1295,
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
