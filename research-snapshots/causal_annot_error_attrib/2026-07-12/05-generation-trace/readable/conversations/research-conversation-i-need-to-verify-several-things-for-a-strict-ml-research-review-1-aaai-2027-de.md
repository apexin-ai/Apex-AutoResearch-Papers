# Research conversation: I need to verify several things for a strict ML research review: 1. **AAAI 2027 deadline**: The proposal claims "abstrac

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad9ac1a5e5625edd4.jsonl`
- **Structured JSON:** [`f1cbbdf7f2b5f6812257.json`](../../sessions/f1/f1cbbdf7f2b5f6812257.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

42 recorded events

### User

_source line 1 · 2026-05-17T08:56:25.023Z_

I need to verify several things for a strict ML research review:

1. **AAAI 2027 deadline**: The proposal claims "abstract deadline July 21, paper deadline July 28, 2026". Search for the actual AAAI 2027 Call for Papers and verify these dates. Today is May 17, 2026.

2. **EACL 2027 deadline**: The proposal claims "ARR deadline August 3, 2026". Verify this.

3. **EMNLP 2026 ARR deadline**: Was the May 2025 ARR deadline actually May 25? When is the next ARR cycle after that? Is there a June or July 2026 ARR deadline that could target EMNLP 2026?

4. **NeurIPS 2025 Best Paper on gated attention (arXiv:2505.06708)**: "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
   - Verify this paper exists and was NeurIPS 2025 Best Paper
   - Verify the G1 gate design: query-conditional, post-SDPA sigmoid gates
   - Verify that per-head gating was identified as the most important design choice
   - This paper proposes gating for training new models from scratch — confirm it was NOT proposed as a fine-tuning intervention

5. **MoH (ICML 2025, arXiv:2410.11842)**: Verify it exists, was at ICML 2025, and achieves +2.4% over LLaMA3-8B with 75% of heads.

Use WebSearch and WebFetch to verify each claim. Report findings with specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "a3488290-db46-4d1e-a1bb-66eb5e61f388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T08:56:25.027Z_

```json
{
  "parentUuid": "a3488290-db46-4d1e-a1bb-66eb5e61f388",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "40e8aa0f-8239-4a70-9a06-701d1e01a20e",
  "timestamp": "2026-05-17T08:56:25.027Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T08:56:28.203Z_



I'll systematically verify each claim. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40e8aa0f-8239-4a70-9a06-701d1e01a20e",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryBbG5Pkiv6qdPDJVV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6dc7a979-56cd-4187-a40b-0281d347a37c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01628rv8FfewjJV8sejZURvE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 936,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-17T08:56:28.252Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NycnZ8o8ULxNQgeFGKwRfG`</summary>

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
  "parentUuid": "6dc7a979-56cd-4187-a40b-0281d347a37c",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryBbG5Pkiv6qdPDJVV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9c1a9f8-c9c9-4db1-b46e-b460ee49312c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01628rv8FfewjJV8sejZURvE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 7304,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 936,
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

_source line 5 · 2026-05-17T08:56:28.254Z_

<details><summary>↩ Tool result · `toolu_01NycnZ8o8ULxNQgeFGKwRfG`</summary>

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
  "parentUuid": "a9c1a9f8-c9c9-4db1-b46e-b460ee49312c",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "1fc6ecc4-1453-4fee-a1d5-5795095f4d07",
  "sourceToolAssistantUUID": "a9c1a9f8-c9c9-4db1-b46e-b460ee49312c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-17T08:56:31.903Z_



Now let me launch all the searches in parallel to verify each claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fc6ecc4-1453-4fee-a1d5-5795095f4d07",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryRZ9beLGeVQT4GFQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f039288c-484a-401c-96a9-c88c5b080a41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGmghPEHxnDzyRFpjwLFpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-17T08:56:33.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R45SETFdVoFWCtfEzAmWAq`</summary>

```json
{
  "query": "AAAI 2027 Call for Papers deadline dates 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f039288c-484a-401c-96a9-c88c5b080a41",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryRZ9beLGeVQT4GFQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4340a63d-b57f-4755-be91-64b575302648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGmghPEHxnDzyRFpjwLFpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-17T08:56:33.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WeGREPZtqtDPchEZBtiidd`</summary>

```json
{
  "query": "EACL 2027 deadline ARR submission date 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4340a63d-b57f-4755-be91-64b575302648",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryRZ9beLGeVQT4GFQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0526958b-66d2-4596-9ee2-2dff4fc5b4b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGmghPEHxnDzyRFpjwLFpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 9 · 2026-05-17T08:56:34.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012VhMho4XbWL1K5P17MPJvv`</summary>

```json
{
  "query": "ACL Rolling Review ARR 2025 2026 deadlines schedule cycle dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0526958b-66d2-4596-9ee2-2dff4fc5b4b8",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryRZ9beLGeVQT4GFQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d390215e-1442-404c-aacd-5d3408a917c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGmghPEHxnDzyRFpjwLFpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-17T08:56:35.271Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DMLptM6UQPCUXETgBuWF29`</summary>

```json
{
  "query": "arXiv 2505.06708 \"Gated Attention\" NeurIPS 2025 best paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d390215e-1442-404c-aacd-5d3408a917c9",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryRZ9beLGeVQT4GFQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35dd9357-a315-4f77-bc4a-cfa21680b248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGmghPEHxnDzyRFpjwLFpw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 11 · 2026-05-17T08:56:35.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TLGzQgSu9Dyxv3WUfAQhAG`</summary>

```json
{
  "query": "arXiv 2410.11842 \"Mixture of Head\" MoH ICML 2025 LLaMA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35dd9357-a315-4f77-bc4a-cfa21680b248",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7ryRZ9beLGeVQT4GFQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3345daa-b5b5-49f6-88f0-f65063206545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGmghPEHxnDzyRFpjwLFpw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 8240,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 310,
          "cache_read_input_tokens": 8240,
          "cache_creation_input_tokens": 1912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1912,
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

_source line 12 · 2026-05-17T08:56:37.579Z_

<details><summary>↩ Tool result · `toolu_01WeGREPZtqtDPchEZBtiidd`</summary>

```text
Web search results for query: "EACL 2027 deadline ARR submission date 2026"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"The 20th Conference of the European Chapter of the Association for Computational LinguisticsAthens, GreeceMarch 9-14, 2027 -","url":"https://2027.eacl.org/"},{"title":"eaclmeeting on X: \"📢⚠️ IMPORTANT DATE CORRECTION: the ARR deadline for EACL 2027 is Aug 3, 2026 (not Aug 6 as previously announced). EACL is earlier than usual in '27, so this is the only viable ARR cycle! 📚 All areas of CL/NLP + related fields welcome. Full CfP coming soon. #NLProc #EACL2027\" / X","url":"https://x.com/eaclmeeting/status/2051971432171688436"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EACL 2027 Call for Main Conference Papers","url":"https://2027.eacl.org/calls/papers/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Frequently Asked Questions for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/faq/"}]

Based on the search results, here's the information about EACL 2027 ARR submission deadlines:

The ARR submission deadline for EACL 2027 (long & short papers) is August 3, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Additionally, the ARR deadline for EACL 2027 is August 3, 2026 (not August 6 as previously announced), and EACL is earlier than usual in 2027, so this is the only viable ARR cycle.

The paper commitment date for EACL 2027 is October 11, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0526958b-66d2-4596-9ee2-2dff4fc5b4b8",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "f6ef92f3-7023-4f32-918e-b74eb0485138",
  "sourceToolAssistantUUID": "0526958b-66d2-4596-9ee2-2dff4fc5b4b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T08:56:37.691Z_

<details><summary>↩ Tool result · `toolu_01R45SETFdVoFWCtfEzAmWAq`</summary>

```text
Web search results for query: "AAAI 2027 Call for Papers deadline dates 2026"

Links: [{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/conference/?id=aaai27"},{"title":"AAAI Conference on Artificial Intelligence - AAAI","url":"https://aaai.org/conference/aaai/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"AAAI 2027 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AAAI 2027 LaTeX Template | Author Kit & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/aaai"},{"title":"40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"}]

Based on the web search results, here's what I found about AAAI 2027 Call for Papers deadline dates:

The AAAI 2027 full paper deadline is August 2, 2026, 11:59 AM UTC. The conference will be held in Montréal, Québec, Canada from February 16-23, 2027.

However, it's worth noting that some sources indicate the paper submission deadline as TBD (UTC-12), and submission deadlines for AAAI 2027 are expected around July–August 2026 based on historical patterns.

For the most up-to-date and official information, the official AAAI 2027 call for papers is at https://aaai.org/conference/aaai/aaai-27/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4340a63d-b57f-4755-be91-64b575302648",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "07a3e682-e39c-43c4-9ecd-d8c27cff33cf",
  "sourceToolAssistantUUID": "4340a63d-b57f-4755-be91-64b575302648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T08:56:42.449Z_

<details><summary>↩ Tool result · `toolu_012VhMho4XbWL1K5P17MPJvv`</summary>

```text
Web search results for query: "ACL Rolling Review ARR 2025 2026 deadlines schedule cycle dates"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"}]

Based on the search results, here's information about ACL Rolling Review (ARR) deadlines and schedule for 2025-2026:

## Schedule Changes

From October 2022 to February 2025, ARR ran 8-week review cycles, with submission deadlines on the 15th of every second month. The ACL Peer Review Committee recommended to switch to 10-week cycles, with the new schedule beginning in May 2025. This means that instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks and author response, as well as platform maintenance.

## 2025 Cycles

In 2025, due to the switch to 10-week cycles enacted relatively late in the year, there were 4 review cycles in total.

## 2026 ACL Submission Deadlines

For ACL 2026 specifically:
- Papers may be submitted to the ARR 2025 October cycle and ARR 2026 January cycle
- Submission deadline (all papers are submitted to ARR): January 5, 2026
- ARR reviews & meta-reviews available to authors of the January cycle: March 10, 2026
- All authors must complete the author registration form by January 7th 2026 EoD AoE. If they get assignments, reviews must be completed by February 7th, and meta-reviews - by March 3rd.

For the complete, detailed schedule with all upcoming cycle dates, the official ARR Dates and Venues page at aclrollingreview.org/dates provides a comprehensive table of key submission, review, and meta-review deadlines for all upcoming cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d390215e-1442-404c-aacd-5d3408a917c9",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "e0c18c3d-584c-4f3b-be6a-6a22a4e86295",
  "sourceToolAssistantUUID": "d390215e-1442-404c-aacd-5d3408a917c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T08:56:42.987Z_

<details><summary>↩ Tool result · `toolu_01TLGzQgSu9Dyxv3WUfAQhAG`</summary>

```text
Web search results for query: "arXiv 2410.11842 "Mixture of Head" MoH ICML 2025 LLaMA"

Links: [{"title":"[2410.11842] MoH: Multi-Head Attention as Mixture-of-Head Attention","url":"https://arxiv.org/abs/2410.11842"},{"title":"MoH: Multi-Head Attention as Mixture-of-Head Attention","url":"https://arxiv.org/html/2410.11842v3"},{"title":"Paper page - MoH: Multi-Head Attention as Mixture-of-Head Attention","url":"https://huggingface.co/papers/2410.11842"},{"title":"ICML Poster MoH: Multi-Head Attention as Mixture-of-Head Attention","url":"https://icml.cc/virtual/2025/poster/44579"},{"title":"GitHub - SkyworkAI/MoH: MoH: Multi-Head Attention as Mixture-of-Head Attention · GitHub","url":"https://github.com/SkyworkAI/MoH"},{"title":"GitHub - withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs: [TKDE'25] The official GitHub page for the survey paper \"A Survey on Mixture of Experts in Large Language Models\". · GitHub","url":"https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs"},{"title":"MoH: Multi-Head Attention as Mixture-of-Head Attention | OpenReview","url":"https://openreview.net/forum?id=eYtgs9k75o"},{"title":"A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications","url":"https://arxiv.org/html/2503.07137v1"},{"title":"Track: Poster Session 1 West","url":"https://icml.cc/virtual/2025/session/50257"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"}]

I found the research paper you're looking for! Here's what I discovered:

**MoH: Multi-Head Attention as Mixture-of-Head Attention** (arXiv:2410.11842) is a paper that upgrades the multi-head attention mechanism, the core of the Transformer model, to improve efficiency while maintaining or surpassing previous accuracy levels.

**Key Concept:**
The paper proposes Mixture-of-Head attention (MoH), a new architecture that treats attention heads as experts in the Mixture-of-Experts (MoE) mechanism.

**Main Advantages:**
MoH enables each token to select the appropriate attention heads, enhancing inference efficiency without compromising accuracy or increasing the number of parameters, and replaces the standard summation in multi-head attention with a weighted summation, introducing flexibility to the attention mechanism.

**Performance with LLaMA:**
MoH-LLaMA3-8B achieves an average accuracy of 64.0% across 14 benchmarks, outperforming LLaMA3-8B by 2.4% by utilizing only 75% of the attention heads.

**ICML 2025:**
The paper was presented at ICML 2025, where MoH lets the model choose only the most helpful attention heads for each piece of input, making the model faster and more efficient without hurting its performance—and often making it even better.

The paper is available on arXiv and has code available on GitHub at the Skywork AI repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3345daa-b5b5-49f6-88f0-f65063206545",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "100904ad-6543-4c5a-95b2-2017af271180",
  "sourceToolAssistantUUID": "e3345daa-b5b5-49f6-88f0-f65063206545",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T08:56:43.151Z_

<details><summary>↩ Tool result · `toolu_01DMLptM6UQPCUXETgBuWF29`</summary>

```text
Web search results for query: "arXiv 2505.06708 "Gated Attention" NeurIPS 2025 best paper"

Links: [{"title":"[2505.06708] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiv.org/abs/2505.06708"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | OpenReview","url":"https://openreview.net/forum?id=1b7whO4SfY"},{"title":"[NeurIPS 2025] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiviq.substack.com/p/neurips-2025-gated-attention-for"},{"title":"gated_attention/README.md at main · qiuzh20/gated_attention","url":"https://github.com/qiuzh20/gated_attention/blob/main/README.md"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2505.06708"},{"title":"[2505.06708] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://ar5iv.labs.arxiv.org/html/2505.06708"},{"title":"NeurIPS Poster Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://neurips.cc/virtual/2025/poster/120216"},{"title":"[2505.06708v1] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiv.org/abs/2505.06708v1"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://www.researchgate.net/publication/391675977_Gated_Attention_for_Large_Language_Models_Non-linearity_Sparsity_and_Attention-Sink-Free"}]

Based on the search results, I can provide you with comprehensive information about arXiv paper 2505.06708:

## Paper Overview

The paper is titled "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free" and was submitted on May 10, 2025.

## Key Finding

The paper's central finding is that a simple modification—applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)—consistently improves performance. This modification also enhances training stability, tolerates larger learning rates, and improves scaling properties.

## Research Methodology

The authors performed a comprehensive comparison over 30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models trained on a 3.5 trillion token dataset.

## NeurIPS 2025 Recognition

Yes, the paper received major recognition at NeurIPS 2025:

- The paper has been awarded the NeurIPS 2025 Best Paper Award!
- This prestigious honor recognizes only 4 papers out of 5,290 accepted submissions, highlighting the foundational impact of the work on attention mechanism design.
- The paper was selected as an Oral Presentation at NeurIPS 2025, placing among the top 1.5% of submissions (77 out of 5,290 accepted papers).

## Authors

The authors are Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, and Junyang Lin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35dd9357-a315-4f77-bc4a-cfa21680b248",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "74d2b897-f487-436e-a293-5615c34d5fd2",
  "sourceToolAssistantUUID": "35dd9357-a315-4f77-bc4a-cfa21680b248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T08:56:45.371Z_

Good, I have initial results. Now let me fetch more details on several of these to verify specific claims more precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74d2b897-f487-436e-a293-5615c34d5fd2",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7rzX2q8seBWwQ5tTjfT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cf32741-e1f3-4948-8476-5ab59ac4da1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyTTQ5Zx4VtvVkQoDfW4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3766,
      "cache_read_input_tokens": 10152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3766,
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

_source line 18 · 2026-05-17T08:56:47.378Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01A28sNinDBFi8pJboeBjxR9`</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-27/",
  "prompt": "Find the exact submission deadlines for AAAI 2027 - specifically the abstract deadline and the full paper deadline. List all important dates mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4cf32741-e1f3-4948-8476-5ab59ac4da1d",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7rzX2q8seBWwQ5tTjfT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13575a32-eaa6-41e0-a19a-f56857790eca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyTTQ5Zx4VtvVkQoDfW4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3766,
      "cache_read_input_tokens": 10152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3766,
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

_source line 19 · 2026-05-17T08:56:49.959Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016MaJUbZ2fTKaaf6NiZamtj`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "List ALL ARR cycle submission deadlines for 2025 and 2026. I need to know: 1) Was there a May 2025 deadline and what exact date? 2) What are all the 2025 and 2026 cycle deadlines? 3) Which ARR cycles can target EMNLP 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13575a32-eaa6-41e0-a19a-f56857790eca",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7rzX2q8seBWwQ5tTjfT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9efd88d4-4805-421b-adea-820fc16e08a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyTTQ5Zx4VtvVkQoDfW4U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3766,
      "cache_read_input_tokens": 10152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3766,
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

_source line 20 · 2026-05-17T08:56:51.306Z_

<details><summary>↩ Tool result · `toolu_01A28sNinDBFi8pJboeBjxR9`</summary>

```text
# AAAI-27 Submission Deadlines

## Key Dates

**Abstract Deadline:** "July 21, 2026 at 11:59 PM UTC-12"

**Full Paper Deadline:** "July 28, 2026 at 11:59 PM UTC-12"

## All Important Dates

- June 17, 2026 – Open Review registration opens
- June 24, 2026 – Paper submission portal opens
- July 21, 2026 – Abstracts due
- July 28, 2026 – Complete papers due
- July 31, 2026 – Supplementary materials and code due
- September 24, 2026 – Phase 1 rejection notifications
- October 19-25, 2026 – Author feedback period
- November 30, 2026 – Final acceptance/rejection decisions
- December 14, 2026 – Camera-ready files due
- February 16-23, 2027 – Conference dates in Montréal, Canada

All deadlines follow "anywhere on earth" time (UTC-12) standards.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13575a32-eaa6-41e0-a19a-f56857790eca",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "8434d3ed-e744-42f4-8daf-015981d8efb8",
  "sourceToolAssistantUUID": "13575a32-eaa6-41e0-a19a-f56857790eca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T08:56:55.129Z_

<details><summary>↩ Tool result · `toolu_016MaJUbZ2fTKaaf6NiZamtj`</summary>

```text
# ARR Cycle Deadlines: 2025-2026

## 1) May 2025 Deadline
Yes, there was a May 2025 deadline. The document states: "The new schedule will be in action, starting in May 2025 cycle." However, the specific submission date for May 2025 is not provided in the table, as the table only lists cycles "following the new schedule" beginning with March 2026.

## 2) All 2025 and 2026 Cycle Deadlines

**2025:** The page notes that "In 2025, due to the switch to 10-week cycles enacted relatively late in the year, there was 4 review cycles in total," but specific dates for 2025 cycles are not included in the schedule table provided.

**2026 Submission Deadlines:**
- March 2026: March 16
- May 2026: May 25
- August 2026: August 3
- October 2026: October 12

## 3) ARR Cycles Targeting EMNLP 2026

Two cycles can target EMNLP 2026:
- **March 2026** (final ARR submission: May 25, 2026)
- **May 2026** (final ARR submission: May 25, 2026; commitment: August 2, 2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9efd88d4-4805-421b-adea-820fc16e08a2",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "8e2779de-d926-4bea-a6ce-2f636f3890d5",
  "sourceToolAssistantUUID": "9efd88d4-4805-421b-adea-820fc16e08a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T08:56:55.512Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XfVMLw7phW1NUnyZwsSC6Q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.06708",
  "prompt": "Extract details about this paper: 1) What is the G1 gate design - is it query-conditional? Are the gates post-SDPA sigmoid gates? 2) Was per-head gating identified as the most important design choice? 3) Is this paper about training new models from scratch, or about fine-tuning existing models? 4) What are the key findings about gate design?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e2779de-d926-4bea-a6ce-2f636f3890d5",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7rzX2q8seBWwQ5tTjfT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b0cc5f9-281a-40f3-958a-980d8dba7942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyTTQ5Zx4VtvVkQoDfW4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3766,
      "cache_read_input_tokens": 10152,
      "output_tokens": 619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3766
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 619,
          "cache_read_input_tokens": 10152,
          "cache_creation_input_tokens": 3766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3766,
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

### Tool call

_source line 23 · 2026-05-17T08:56:55.520Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CgiV6ycxHnjGAk57itwHts`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.11842",
  "prompt": "Verify: 1) What is MoH exactly? 2) Does MoH-LLaMA3-8B achieve +2.4% over LLaMA3-8B with 75% of heads? 3) Is this confirmed at ICML 2025? Extract the exact performance claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b0cc5f9-281a-40f3-958a-980d8dba7942",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7rzX2q8seBWwQ5tTjfT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2988aca-fa5e-49dd-bf7b-fa16c8ee89a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyTTQ5Zx4VtvVkQoDfW4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3766,
      "cache_read_input_tokens": 10152,
      "output_tokens": 619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3766
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 619,
          "cache_read_input_tokens": 10152,
          "cache_creation_input_tokens": 3766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3766,
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

### Tool call

_source line 24 · 2026-05-17T08:56:55.524Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HaoYMD3RPStucNM6bVnMx7`</summary>

```json
{
  "query": "NeurIPS 2025 best paper award winners list official"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2988aca-fa5e-49dd-bf7b-fa16c8ee89a6",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7rzX2q8seBWwQ5tTjfT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c2ddfbd-157b-49f3-ab72-65df612e0292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAyTTQ5Zx4VtvVkQoDfW4U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 3766,
      "cache_read_input_tokens": 10152,
      "output_tokens": 619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3766
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 619,
          "cache_read_input_tokens": 10152,
          "cache_creation_input_tokens": 3766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3766,
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

_source line 25 · 2026-05-17T08:56:59.994Z_

<details><summary>↩ Tool result · `toolu_01CgiV6ycxHnjGAk57itwHts`</summary>

```text
# Verification of MoH Paper Claims

**1) What is MoH exactly?**

MoH (Mixture-of-Head Attention) treats attention heads as experts in a Mixture-of-Experts mechanism. As stated: "MoH...treats attention heads as experts in the Mixture-of-Experts (MoE) mechanism." It enables tokens to select appropriate attention heads dynamically, replacing standard summation with weighted summation.

**2) Does MoH-LLaMA3-8B achieve +2.4% over LLaMA3-8B with 75% of heads?**

Yes, this claim is made in the abstract: "MoH-LLaMA3-8B achieves an average accuracy of 64.0% across 14 benchmarks, outperforming LLaMA3-8B by 2.4% by utilizing only 75% of the attention heads."

**3) Is this confirmed at ICML 2025?**

The paper states: "Accepted by ICML 2025, code: [this https URL](https://github.com/SkyworkAI/MoH)" indicating acceptance, though the submission history shows the latest version (v3) is dated December 1, 2025, which is after ICML 2025 would have occurred.

**Performance claims summary:** MoH outperforms standard multi-head attention "by using only 50%-90% of the attention heads" across ViT, DiT, and LLM experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2988aca-fa5e-49dd-bf7b-fa16c8ee89a6",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "0bff2762-eaf5-44d3-8e06-c00223480344",
  "sourceToolAssistantUUID": "f2988aca-fa5e-49dd-bf7b-fa16c8ee89a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T08:57:00.317Z_

<details><summary>↩ Tool result · `toolu_01XfVMLw7phW1NUnyZwsSC6Q`</summary>

```text
# Paper Details: Gated Attention for LLMs

Based on the available content, I can provide limited information:

**1) G1 Gate Design:**
The abstract indicates gates are "applied a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)," suggesting post-SDPA sigmoid application. However, the provided excerpt doesn't specify whether gates are query-conditional.

**2) Per-Head Gating Importance:**
The abstract confirms that "a simple modification-applying a head-specific sigmoid gate" consistently improves performance, indicating per-head gating was a key focus. However, this web page doesn't explicitly rank it as the single most important design choice among all tested variants.

**3) Training vs. Fine-tuning:**
The paper involved "training on a 3.5 trillion token dataset" across "30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models," indicating training from scratch rather than fine-tuning.

**4) Key Gate Design Findings:**
According to the abstract, effectiveness stems from: "(1) introducing non-linearity upon the low-rank mapping in the softmax attention, and (2) applying query-dependent sparse gating scores to modulate the SDPA output." Additionally, the mechanism "mitigates 'attention sink' and enhances long-context extrapolation performance."

**Note:** The full PDF would contain additional implementation details not visible in this abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b0cc5f9-281a-40f3-958a-980d8dba7942",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "67b29de2-7995-4390-8365-4e825cff597c",
  "sourceToolAssistantUUID": "8b0cc5f9-281a-40f3-958a-980d8dba7942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T08:57:06.062Z_

<details><summary>↩ Tool result · `toolu_01HaoYMD3RPStucNM6bVnMx7`</summary>

```text
Web search results for query: "NeurIPS 2025 best paper award winners list official"

Links: [{"title":"Announcing the NeurIPS 2025 Best Paper Awards – NeurIPS Blog","url":"https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/"},{"title":"NeurIPS 2025 Awards","url":"https://neurips.cc/virtual/2025/awards_detail"},{"title":"NeurIPS 2025 Best Papers Winners Announced: Decade-Old Classic Work by He Kaiming, Sun Jian, Etc. Wins Award","url":"https://eu.36kr.com/en/p/3570970959395720"},{"title":"NeurIPS 2025 Best Paper Awards - by David Mataciunas","url":"https://aiconnections.substack.com/p/neurips-2025-best-paper-awards"},{"title":"Alibaba Qwen Wins “NeurIPS 2025 Best Paper Award” for Breakthrough in Attention Mechanisms | Alizila","url":"https://www.alizila.com/alibaba-qwen-wins-neurips-2025-best-paper-award-for-breakthrough-in-attention-mechanisms/"},{"title":"NeurIPS 2025 Best Papers in Comics - by Grigory Sapunov","url":"https://gonzoml.substack.com/p/neurips-2025-best-papers-in-comics"},{"title":"@Kseniase on Hugging Face: \"15 Outstanding Research Papers from NeurIPS 2025 NeurIPS 2025, as a premier…\"","url":"https://huggingface.co/posts/Kseniase/673116238988658"},{"title":"The Best Papers at NeurIPS 2025, Explained - The Neuron","url":"https://www.theneuron.ai/explainer-articles/the-best-papers-at-neurips-2025-explained/"},{"title":"The Best of NeurIPS 2025: A Deep Dive into This Year’s Award-Winning AI Research | by evoailabs | Medium","url":"https://evoailabs.medium.com/the-best-of-neurips-2025-a-deep-dive-into-this-years-award-winning-ai-research-4bc99b19da8d"},{"title":"Announcing the Test of Time Paper Award for NeurIPS 2025 – NeurIPS Blog","url":"https://blog.neurips.cc/2025/11/26/announcing-the-test-of-time-paper-award-for-neurips-2025/"}]

Based on the official announcement, here's the complete list of NeurIPS 2025 Best Paper Award winners:

## Best Papers (4 winners)

The best paper awards this year go to four best papers (one of which is from the datasets and benchmarks track):

1. **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)** - Introduces Infinity-Chat, a benchmark of 26K real-world open-ended queries paired with 31K dense human annotations, revealing pronounced intra- and inter-model homogenization

2. **Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free** - The first in the industry to systematically examine how attention gating affects the performance and training of large models

3. **1000 Layer Networks for Self-Supervised RL** - Shows that making RL networks extremely deep, up to 1024 layers, unlocks major gains in self-supervised reinforcement learning, improving contrastive RL performance by 2 to 50 times on locomotion and manipulation benchmarks

4. **Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training** - Shows that diffusion models have two key moments during training: one when they start generating good samples and another when they begin memorizing the data, creating a widening window where the model can generalize well without overfitting

## Runner-Up Papers (3 winners)

Three runner-up papers also received awards:

1. **Optimal Mistake Bounds for Transductive Online Learning** - Solves a 30-year-old problem by showing exactly how much unlabeled data can help in online learning, proving that the best possible mistake bound in the transductive setting scales with the square root of the Littlestone dimension

2. **Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** - Tests whether RL with verifiable rewards actually gives language models new reasoning abilities, finding that base models outperform the RL-trained ones when many samples are allowed

3. **Representation Superposition and Neural Scaling Laws** - Argues that neural scaling laws in language models arise from representation superposition, where adjusting the strength of superposition shows that under strong superposition the loss naturally decreases in proportion to model size


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c2ddfbd-157b-49f3-ab72-65df612e0292",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "d1b838fa-769e-4059-a238-b71582b2d910",
  "sourceToolAssistantUUID": "2c2ddfbd-157b-49f3-ab72-65df612e0292",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-17T08:57:09.143Z_

Now let me get more details on the Gated Attention paper's specific design choices and verify the ARR May 2025 date more precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1b838fa-769e-4059-a238-b71582b2d910",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s2CyCNwtiNugki9Ac5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7dcc83e-a9cb-42f9-a8c3-c9361c4d8398",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nee4JJCwpR8AKojJUegGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4250,
      "cache_read_input_tokens": 13918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4250,
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

_source line 29 · 2026-05-17T08:57:13.455Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BsZCLU1hFxRRsXQMd3br8Q`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2505.06708",
  "prompt": "I need to verify specific claims about this paper: 1) What exactly is the G1 gate design? Is it query-conditional? Are the gates applied post-SDPA as sigmoid gates? 2) Was per-head gating explicitly identified as THE most important design choice in their ablation study? 3) Is this paper exclusively about training new models from scratch (pre-training), or does it also propose fine-tuning existing models? Look for any mention of fine-tuning or adapting existing models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7dcc83e-a9cb-42f9-a8c3-c9361c4d8398",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s2CyCNwtiNugki9Ac5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dd9d7e8-b977-4296-8768-9d740f269035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nee4JJCwpR8AKojJUegGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4250,
      "cache_read_input_tokens": 13918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4250,
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

_source line 30 · 2026-05-17T08:57:15.858Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EyvDRj4zRu5v3vgMkDTGvu`</summary>

```json
{
  "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md",
  "prompt": "List all ARR submission deadlines for 2025 cycles. Was there a May 2025 cycle? What was the exact submission date? Also list any June or July 2025 or 2026 deadlines. What are the EMNLP 2026 commitment deadlines?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd9d7e8-b977-4296-8768-9d740f269035",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s2CyCNwtiNugki9Ac5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1169bb9-9ca7-4674-9b4d-d3ba3fe0d244",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nee4JJCwpR8AKojJUegGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4250,
      "cache_read_input_tokens": 13918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4250,
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

_source line 31 · 2026-05-17T08:57:16.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GKedYEfNZQRcLmHWhLLgAq`</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR commitment date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1169bb9-9ca7-4674-9b4d-d3ba3fe0d244",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s2CyCNwtiNugki9Ac5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12da070a-e818-4a0e-8efe-e960ae4c5911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nee4JJCwpR8AKojJUegGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4250,
      "cache_read_input_tokens": 13918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4250,
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

_source line 32 · 2026-05-17T08:57:19.458Z_

<details><summary>↩ Tool result · `toolu_01BsZCLU1hFxRRsXQMd3br8Q`</summary>

```text
# Analysis of Gated Attention Paper Claims

## 1. G1 Gate Design

**Query-conditional:** Yes. The paper states that G1 gating scores are "derived from the hidden states corresponding to the current query" and depend on Xi. The gate formula shows: "σ(XWθ)" where X represents query-dependent hidden states.

**Post-SDPA sigmoid gates:** Confirmed. The design applies "a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)." The gating mechanism is multiplicative: "Y′=Y⊙σ(XWθ)" where the output is element-wise multiplied by sigmoid-activated scores.

## 2. Per-Head Gating as Critical Design Choice

**Explicitly identified as most important:** Yes, the ablation study emphasizes this. Table 1 shows headwise gating (row 10) substantially outperforms head-shared variants (row 12). The paper notes: "Head-Specific Gating Matters. Applying headwise gating at G1 and G2 introduces very few additional parameters (less than 2M) but still delivers substantial improvements."

Section 4.2 reinforces this: "Head-Specific Sparsity Matters" and emphasizes that "individual attention heads capture distinct aspects."

## 3. Pre-training vs. Fine-tuning Scope

**Exclusively pre-training from scratch.** The paper trains models on "3.5 trillion token dataset" and "400B tokens" with standard pre-training procedures. There is **no mention of fine-tuning existing models** or adapting pre-trained checkpoints. All experiments involve training from initialization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dd9d7e8-b977-4296-8768-9d740f269035",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "57205262-91f7-4c38-a81b-c8ba064f5674",
  "sourceToolAssistantUUID": "3dd9d7e8-b977-4296-8768-9d740f269035",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T08:57:19.736Z_

<details><summary>↩ Tool result · `toolu_01EyvDRj4zRu5v3vgMkDTGvu`</summary>

```text
# ARR Submission Deadlines and Commitment Dates

## 2025 Cycles
According to the document, "In 2025, due to the switch to 10-week cycles enacted relatively late in the year, there was 4 review cycles in total." The specific 2025 submission deadlines are not listed in the provided table, which only shows cycles from March 2026 onwards.

## May 2025 Cycle
Yes, there was a May 2025 cycle, though its exact submission date is not detailed in this document excerpt.

## June-July 2025 Deadlines
No submission deadlines for June or July 2025 appear in the content provided.

## June-July 2026 Deadlines
The table lists:
- **May 2026**: Submission deadline May 25, 2026
- **August 2026**: Submission deadline August 3, 2026

No June or July 2026 submission deadlines are specified.

## EMNLP 2026 Commitment Deadline
"The commitment date for EMNLP 2026 is August 2, 2026," with a final ARR submission deadline of May 25, 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1169bb9-9ca7-4674-9b4d-d3ba3fe0d244",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "3c7b345e-2276-4d1c-8b2d-dcb86e9c4a04",
  "sourceToolAssistantUUID": "a1169bb9-9ca7-4674-9b4d-d3ba3fe0d244",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T08:57:25.252Z_

<details><summary>↩ Tool result · `toolu_01GKedYEfNZQRcLmHWhLLgAq`</summary>

```text
Web search results for query: "EMNLP 2026 submission deadline ARR commitment date"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, here are the key dates for EMNLP 2026:

**ARR Submission Deadline:** May 25, 2026

**EMNLP Commitment Deadline:** August 2, 2026

Additional important dates include:
- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12da070a-e818-4a0e-8efe-e960ae4c5911",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "80b2b7f5-40a6-4996-ba67-647ff5f4da25",
  "sourceToolAssistantUUID": "12da070a-e818-4a0e-8efe-e960ae4c5911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-17T08:57:28.161Z_

Let me get one more piece of information -- the exact May 2025 ARR deadline date to verify the "May 25" claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80b2b7f5-40a6-4996-ba67-647ff5f4da25",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s3d5oXMyXBkKMDyTaA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db73d217-5b48-4958-820d-94ec59c5f1b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Lt9rmQRvYKp3VEZ8BRwro",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 18168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1890,
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

_source line 36 · 2026-05-17T08:57:28.365Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GQsDuFf4pu44QvmeNPnZ1Y`</summary>

```json
{
  "query": "ARR \"May 2025\" submission deadline exact date ACL Rolling Review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db73d217-5b48-4958-820d-94ec59c5f1b3",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s3d5oXMyXBkKMDyTaA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "314e0aa7-0031-47c3-bbd4-8dce418694f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Lt9rmQRvYKp3VEZ8BRwro",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 18168,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1890
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 18168,
          "cache_creation_input_tokens": 1890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1890,
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

_source line 37 · 2026-05-17T08:57:31.769Z_

<details><summary>↩ Tool result · `toolu_01GQsDuFf4pu44QvmeNPnZ1Y`</summary>

```text
Web search results for query: "ARR "May 2025" submission deadline exact date ACL Rolling Review"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025) – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2025"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL ARR | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR"},{"title":"ACLRollingReview (@ReviewAcl) / X","url":"https://x.com/reviewacl"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2025","url":"https://2025.aclweb.org/calls/main_conference_papers/"}]

Based on the search results, the submission deadline for the May 2025 cycle is May 19. This is confirmed in another source that specifies all authors are expected to complete a registration form within 48 hours after submission deadline (before May 21 EoD AoE for May 2025 cycle, where the submission deadline is May 19).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "314e0aa7-0031-47c3-bbd4-8dce418694f8",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "fb590ac7-1a57-45a8-bc01-e9e7b4c70292",
  "sourceToolAssistantUUID": "314e0aa7-0031-47c3-bbd4-8dce418694f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T08:57:34.437Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PmuvQxAKP83oJbCSwSik6A`</summary>

```json
{
  "url": "https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay",
  "prompt": "What was the exact submission deadline for the ARR May 2025 cycle? Was it May 19 or May 25?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb590ac7-1a57-45a8-bc01-e9e7b4c70292",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s46uNSyMJuZstQvuoM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f712fc0e-2c5f-439c-ba7d-b502331bc002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013C6d5nCAq9KUhNBUHsAv4j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 20058,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 686
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 20058,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 686,
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

_source line 39 · 2026-05-17T08:57:36.361Z_

<details><summary>↩ Tool result · `toolu_01PmuvQxAKP83oJbCSwSik6A`</summary>

```text
I cannot find the specific submission deadline for the ARR May 2025 cycle in the provided content. The web page excerpt shows only the OpenReview navigation menu and footer information, without details about submission deadlines for any particular venue or cycle.

To find this information, you would need to visit the actual ARR May 2025 venue page on OpenReview.net or check the official ACL Rollout (ARR) submission guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f712fc0e-2c5f-439c-ba7d-b502331bc002",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "7e0a9fa4-ac52-4042-a8bb-2688fb345099",
  "sourceToolAssistantUUID": "f712fc0e-2c5f-439c-ba7d-b502331bc002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T08:57:39.127Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2f3GTSppnuriJscuAYo1F`</summary>

```json
{
  "query": "\"ARR May 2025\" \"May 19\" submission deadline EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e0a9fa4-ac52-4042-a8bb-2688fb345099",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s4SYpGFyQjcdoHnGms",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f73053dc-56fc-4a79-944a-8600a0725cce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DUrQGkn3dsTpApytpoVcBZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 240,
      "cache_read_input_tokens": 20744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 240,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 41 · 2026-05-17T08:57:45.209Z_

<details><summary>↩ Tool result · `toolu_01R2f3GTSppnuriJscuAYo1F`</summary>

```text
Web search results for query: ""ARR May 2025" "May 19" submission deadline EMNLP 2025"

Links: [{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"},{"title":"LINGUIST List 36.640 Confs: The 2025 Conference on Empirical Methods in Natural Language Processing / China","url":"https://linguistlist.org/issues/36/640/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - EMNLP 2025","url":"https://2025.emnlp.org/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2025 : Empirical Methods in Natural Language Processing","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=187880"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"EMNLP 2025 (@emnlpmeeting) / X","url":"https://x.com/emnlpmeeting?lang=en"}]

Based on the search results, here's the information about the ARR May 2025 cycle and EMNLP 2025 submission deadline:

The ARR submission deadline (for long & short papers) for EMNLP 2025 is May 19, 2025. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Authors are expected to complete a registration form within 48 hours after the submission deadline (before May 21 EoD AoE for the May 2025 cycle).

Key dates for EMNLP 2025 following the ARR submission include:
- Commitment deadline: July 31, 2025
- Notification of acceptance: August 20, 2025
- Camera-ready papers due: September 19, 2025
- Main Conference: November 5-9, 2025

This May 2025 cycle marks part of a significant change in ARR's schedule: The new 10-week cycle schedule is in action, starting in May 2025, replacing the previous 8-week cycles.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f73053dc-56fc-4a79-944a-8600a0725cce",
  "isSidechain": true,
  "promptId": "de625f70-45d8-4ac8-b5c5-eb7f71d2f1ee",
  "agentId": "ad9ac1a5e5625edd4",
  "type": "user",
  "uuid": "702a38b3-a595-4c8c-92b5-f143dbd0b7e7",
  "sourceToolAssistantUUID": "f73053dc-56fc-4a79-944a-8600a0725cce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-17T08:58:31.111Z_

Now I have all the information needed. Here is my comprehensive verification report:

---

## Verification Report for ML Research Review

### 1. AAAI 2027 Deadline

**Claim:** "Abstract deadline July 21, paper deadline July 28, 2026"

**Verdict: CORRECT.** The official AAAI-27 page confirms:
- Abstract deadline: **July 21, 2026** (11:59 PM UTC-12)
- Full paper deadline: **July 28, 2026** (11:59 PM UTC-12)
- Conference: February 16-23, 2027, Montreal, Canada

Sources:
- [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/)
- [AI Deadlines - AAAI 27](http://aideadlines.org/conference/?id=aaai27)

---

### 2. EACL 2027 Deadline

**Claim:** "ARR deadline August 3, 2026"

**Verdict: CORRECT.** The EACL 2027 organizers confirmed the ARR submission deadline is **August 3, 2026**. They issued a correction (it was originally announced as August 6, then corrected to August 3). Importantly, EACL is earlier than usual in 2027, so this is the **only viable ARR cycle** for EACL 2027. The commitment deadline is October 11, 2026.

Sources:
- [EACL 2027 Official Site](https://2027.eacl.org/)
- [EACL Date Correction on X](https://x.com/eaclmeeting/status/2051971432171688436)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)

---

### 3. EMNLP 2026 / ARR Deadlines

**Claim:** "May 2025 ARR deadline was May 25"

**Verdict: INCORRECT.** The May 2025 ARR submission deadline was **May 19, 2025** (not May 25). This is confirmed by the EMNLP 2025 organizers on X and the ARR incentives page. The May 2025 cycle was the first under the new 10-week schedule (replacing 8-week cycles).

**Regarding the next ARR cycle and EMNLP 2026 targeting:**
- ARR switched to 10-week cycles starting May 2025, yielding ~5 cycles/year instead of 6.
- The 2026 ARR cycle dates are: **March 16**, **May 25**, **August 3**, **October 12**.
- There is **no June or July 2026 ARR deadline**. The cycles jump from May 25 directly to August 3.
- For **EMNLP 2026**, the final ARR submission deadline is **May 25, 2026**, with a commitment deadline of **August 2, 2026**. Papers from the March 2026 cycle can also be committed to EMNLP 2026.

Sources:
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2025 on X confirming May 19 deadline](https://x.com/emnlpmeeting/status/1892259536137785419)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [ARR GitHub dates.md](https://github.com/acl-org/aclrollingreview/blob/main/dates.md)

---

### 4. NeurIPS 2025 Best Paper -- Gated Attention (arXiv:2505.06708)

**Paper existence:** CONFIRMED. "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free" by Zihan Qiu et al. (Alibaba Qwen team), arXiv:2505.06708.

**NeurIPS 2025 Best Paper:** CONFIRMED. It was one of **4 Best Paper winners** out of 5,290 accepted papers (not just an Oral -- it won the actual Best Paper Award). This is confirmed by the official NeurIPS blog post.

**G1 gate design -- query-conditional, post-SDPA sigmoid gates:** CONFIRMED. The paper defines gating as Y' = Y . sigma(X * W_theta), where:
- Gates are applied **after SDPA** (post-SDPA), confirmed explicitly
- Gates use **sigmoid** activation, confirmed
- Gates are **query-conditional** ("derived from the hidden states corresponding to the current query" / "query-dependent sparse gating scores")

**Per-head gating as most important design choice:** CONFIRMED. The ablation study (Table 1) shows headwise gating (row 10) substantially outperforms head-shared variants (row 12). The paper explicitly states "Head-Specific Gating Matters" and emphasizes that "individual attention heads capture distinct aspects." The improvement comes with very few additional parameters (<2M).

**Training from scratch, NOT fine-tuning:** CONFIRMED. All experiments involve pre-training from scratch on 3.5 trillion tokens (15B MoE models) and 400B tokens (1.7B dense models). There is **no mention of fine-tuning or adapting existing models** anywhere in the paper.

Sources:
- [arXiv:2505.06708](https://arxiv.org/abs/2505.06708)
- [NeurIPS 2025 Best Paper Awards (Official Blog)](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- [GitHub: gated_attention](https://github.com/qiuzh20/gated_attention)
- [ar5iv HTML version](https://ar5iv.labs.arxiv.org/html/2505.06708)
- [Alibaba Alizila coverage](https://www.alizila.com/alibaba-qwen-wins-neurips-2025-best-paper-award-for-breakthrough-in-attention-mechanisms/)

---

### 5. MoH (arXiv:2410.11842)

**Paper existence:** CONFIRMED. "MoH: Multi-Head Attention as Mixture-of-Head Attention" by the Skywork AI team.

**ICML 2025:** CONFIRMED. The paper states "Accepted by ICML 2025" and appears in the [ICML 2025 virtual poster session](https://icml.cc/virtual/2025/poster/44579).

**+2.4% over LLaMA3-8B with 75% of heads:** CONFIRMED. The abstract explicitly states: "MoH-LLaMA3-8B achieves an average accuracy of 64.0% across 14 benchmarks, outperforming LLaMA3-8B by 2.4% by utilizing only 75% of the attention heads."

Sources:
- [arXiv:2410.11842](https://arxiv.org/abs/2410.11842)
- [ICML 2025 Poster](https://icml.cc/virtual/2025/poster/44579)
- [GitHub: SkyworkAI/MoH](https://github.com/SkyworkAI/MoH)
- [OpenReview](https://openreview.net/forum?id=eYtgs9k75o)

---

### Summary Table

| Claim | Verdict |
|---|---|
| AAAI 2027: abstract Jul 21, paper Jul 28 | **CORRECT** |
| EACL 2027: ARR deadline Aug 3, 2026 | **CORRECT** |
| May 2025 ARR deadline was May 25 | **INCORRECT -- it was May 19** |
| No June/July 2026 ARR cycle exists | Confirmed (May 25 -> Aug 3 gap) |
| EMNLP 2026 ARR deadline is May 25, 2026 | **CORRECT** |
| Gated Attention paper exists at arXiv:2505.06708 | **CORRECT** |
| Gated Attention won NeurIPS 2025 Best Paper | **CORRECT** |
| G1 = query-conditional post-SDPA sigmoid gates | **CORRECT** |
| Per-head gating = most important design choice | **CORRECT** |
| Gated Attention is for training from scratch, not fine-tuning | **CORRECT** |
| MoH exists at arXiv:2410.11842, at ICML 2025 | **CORRECT** |
| MoH: +2.4% over LLaMA3-8B with 75% heads | **CORRECT** |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "702a38b3-a595-4c8c-92b5-f143dbd0b7e7",
  "isSidechain": true,
  "agentId": "ad9ac1a5e5625edd4",
  "requestId": "req_011Cb7s56P9VedusDrfd73xd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f5eba00-42b5-4258-aace-59332d83f0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "33c25f21-583e-4fb5-a548-770cd8f14e78",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113ztbjcbGvJBvayTNcCKps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 863,
      "cache_read_input_tokens": 20984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 863,
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
