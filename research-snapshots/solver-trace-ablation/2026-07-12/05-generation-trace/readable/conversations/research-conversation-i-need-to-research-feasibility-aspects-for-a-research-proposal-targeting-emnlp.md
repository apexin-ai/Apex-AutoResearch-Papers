# Research conversation: I need to research feasibility aspects for a research proposal targeting EMNLP 2026 ARR May 25 deadline: 1. Search for "

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4600e201e124ae0b.jsonl`
- **Structured JSON:** [`50572097f3ddcbcdd048.json`](../../sessions/50/50572097f3ddcbcdd048.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-12T00:33:38.335Z_

I need to research feasibility aspects for a research proposal targeting EMNLP 2026 ARR May 25 deadline:

1. Search for "EMNLP 2026 ARR deadline May 2026" to confirm the exact submission deadline and format requirements (especially for Findings track vs. main conference).

2. Search for "autoformalization 7B model" or "small language model autoformalization" to understand how well 7B models can autoformalize logic/math — are there any papers showing 7B model autoformalization quality?

3. Search for "FoVer PRM" model availability — is the FoVer-PRM model publicly available on HuggingFace? Search "FoVer PRM huggingface" or "Qwen-2.5-7B-FoVer-PRM".

4. Search for "VersaPRM huggingface" to check model availability.

5. Search for "SAFE step-level verification github" to check if the SAFE codebase is actually available and usable.

Report in under 400 words with specific findings on each point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "6ca268ff-1cf6-4f5a-a9a9-e5f92397b51f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:33:38.342Z_

```json
{
  "parentUuid": "6ca268ff-1cf6-4f5a-a9a9-e5f92397b51f",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e7bddb65-5b9b-4798-af35-041e0af7501e",
  "timestamp": "2026-05-12T00:33:38.342Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:33:40.576Z_



I'll research all five points in parallel using web searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7bddb65-5b9b-4798-af35-041e0af7501e",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011CawjatTumFPTJ2UfqrVGK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "668d3d56-d837-4ed1-8035-b105d9ff9bfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXqaUFZ3k1F794zXkkbFPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 781,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T00:33:40.882Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KDkpsHfzZFYHpDwEv28yhE`</summary>

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
  "parentUuid": "668d3d56-d837-4ed1-8035-b105d9ff9bfb",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011CawjatTumFPTJ2UfqrVGK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90a1bc28-5a04-4f7d-8575-588287642f31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JXqaUFZ3k1F794zXkkbFPp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 7304,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 7304,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 781,
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

_source line 5 · 2026-05-12T00:33:40.885Z_

<details><summary>↩ Tool result · `toolu_01KDkpsHfzZFYHpDwEv28yhE`</summary>

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
  "parentUuid": "90a1bc28-5a04-4f7d-8575-588287642f31",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "ca0372ed-053e-4a58-8f43-1f0c9e1900a3",
  "sourceToolAssistantUUID": "90a1bc28-5a04-4f7d-8575-588287642f31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:33:44.155Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca0372ed-053e-4a58-8f43-1f0c9e1900a3",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjb5XRVodfzmUgkyqwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14f224d2-af90-4cd3-a601-5396462508aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa2QMDpQD3CoHQhuEX7Qwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 7 · 2026-05-12T00:33:44.729Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Zw6GiRGR5Vu5pL8CHQErm`</summary>

```json
{
  "query": "EMNLP 2026 ARR deadline May 2026 submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f224d2-af90-4cd3-a601-5396462508aa",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjb5XRVodfzmUgkyqwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a01a389-3eb7-450b-b238-702b133f0c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa2QMDpQD3CoHQhuEX7Qwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 8 · 2026-05-12T00:33:45.758Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UGCXQbciMdG8BxiHGEQUVa`</summary>

```json
{
  "query": "autoformalization 7B model small language model autoformalization quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a01a389-3eb7-450b-b238-702b133f0c27",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjb5XRVodfzmUgkyqwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a051da7d-9379-458f-a241-10318dd45f9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa2QMDpQD3CoHQhuEX7Qwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 9 · 2026-05-12T00:33:46.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pr144oJ9vCTfFjH5tbqQpN`</summary>

```json
{
  "query": "FoVer PRM huggingface Qwen-2.5-7B-FoVer-PRM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a051da7d-9379-458f-a241-10318dd45f9b",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjb5XRVodfzmUgkyqwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "788ff724-4f04-45cf-8381-f41bc04a61f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa2QMDpQD3CoHQhuEX7Qwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 10 · 2026-05-12T00:33:47.578Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CrjNFrCG9ueqT5kq5Bmjrv`</summary>

```json
{
  "query": "VersaPRM huggingface model availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "788ff724-4f04-45cf-8381-f41bc04a61f8",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjb5XRVodfzmUgkyqwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9c4d6fc-54d3-40de-9328-49c6e902aad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa2QMDpQD3CoHQhuEX7Qwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1406,
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

_source line 11 · 2026-05-12T00:33:47.844Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MTYNpfVQujE2R4BkUBJmrs`</summary>

```json
{
  "query": "SAFE step-level verification github code available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9c4d6fc-54d3-40de-9328-49c6e902aad5",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjb5XRVodfzmUgkyqwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d80a505-a674-4fda-bd05-272a0e1fdd41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa2QMDpQD3CoHQhuEX7Qwz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1406,
      "cache_read_input_tokens": 8085,
      "output_tokens": 278,
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
          "output_tokens": 278,
          "cache_read_input_tokens": 8085,
          "cache_creation_input_tokens": 1406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1406,
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

_source line 12 · 2026-05-12T00:33:51.721Z_

<details><summary>↩ Tool result · `toolu_014Zw6GiRGR5Vu5pL8CHQErm`</summary>

```text
Web search results for query: "EMNLP 2026 ARR deadline May 2026 submission"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about EMNLP 2026 ARR deadline and submission requirements:

## ARR Submission Deadline

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

## Important Related Dates

The reviewer registration deadline for all authors is May 27, 2026, with author response and author-reviewer discussion running July 7-13, 2026, meta review released July 30, 2026, and the EMNLP commitment deadline on August 2, 2026.

## Key Submission Policy

Given that the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026—ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.

After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE (End of Day, Anywhere on Earth).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a01a389-3eb7-450b-b238-702b133f0c27",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "1567e173-6853-4b7d-9c39-9e38c0b73b9a",
  "sourceToolAssistantUUID": "7a01a389-3eb7-450b-b238-702b133f0c27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:33:52.248Z_

<details><summary>↩ Tool result · `toolu_01UGCXQbciMdG8BxiHGEQUVa`</summary>

```text
Web search results for query: "autoformalization 7B model small language model autoformalization quality"

Links: [{"title":"Towards Autoformalization of LLM-generated Outputs for Requirement Verification","url":"https://arxiv.org/html/2511.11829"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"},{"title":"Lean-ing on Quality: How High-Quality Data Beats Diverse Multilingual Data in AutoFormalization","url":"https://arxiv.org/html/2502.15795"},{"title":"GitHub - THUNLP-MT/FormaRL: [COLM25] Enhancing Autoformalization with no Labeled Data · GitHub","url":"https://github.com/THUNLP-MT/FormaRL"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/html/2410.04194"},{"title":"Autoformalization with Large Language Models Yuhuai Wu1,2† Albert Q. Jiang3","url":"https://openreview.net/pdf?id=IUikebJ1Bf0"},{"title":"Autoformalization with Large Language Models","url":"https://research.google/pubs/autoformalization-with-large-language-models/"},{"title":"[2205.12615] Autoformalization with Large Language Models","url":"https://arxiv.org/abs/2205.12615"},{"title":"[2505.23486] Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/abs/2505.23486"},{"title":"Autoformalization with Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2205.12615"}]

Based on the search results, here's what I found about autoformalization with 7B models and small language models:

## Autoformalization 7B Models

DeepSeek-Prover-v2 comes in two versions: a 7B and a 671B model, with researchers using the 7B model due to resource constraints. The model is trained on data from formal languages like Lean, which is crucial for converting natural language into Lean syntax.

## Quality of Smaller Models

Research shows that smaller models can achieve competitive performance:

- DeepSeekMath with 7B parameter sizes achieved comparable performance to Minerva540B, showing that the number of parameters is not the only key factor in mathematical reasoning ability, and strong performance can also be obtained in smaller models.

- MS-RAG can lift the performance of smaller models, with Mistral (7B) and MS-RAG outperforming larger models.

## Data Quality Challenges

A key insight for autoformalization quality is data quality: Approaches surpass the performance of finetuning with extensive multilingual datasets such as MMA on ProofNet with only 1/150th of the tokens. Autoformalization requires high-quality parallel corpora consisting of aligned informal and formal mathematical statements.

The research indicates that 7B models can be effective for autoformalization tasks when properly trained and with high-quality training data, making them practical alternatives to much larger models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a051da7d-9379-458f-a241-10318dd45f9b",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "849cbe2d-cc0d-4af5-8f10-ad755a982ab7",
  "sourceToolAssistantUUID": "a051da7d-9379-458f-a241-10318dd45f9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:33:52.511Z_

<details><summary>↩ Tool result · `toolu_01Pr144oJ9vCTfFjH5tbqQpN`</summary>

```text
Web search results for query: "FoVer PRM huggingface Qwen-2.5-7B-FoVer-PRM"

Links: [{"title":"Qwen/Qwen2.5-Math-PRM-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B"},{"title":"Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B · Hugging Face","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B"},{"title":"README.md · Qwen/Qwen2.5-Math-PRM-7B at main","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/README.md"},{"title":"Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B · Hugging Face","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B"},{"title":"ob11/Qwen-VL-PRM-7B · Hugging Face","url":"https://huggingface.co/ob11/Qwen-VL-PRM-7B"},{"title":"modeling_qwen2_rm.py · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B at 37fd8caf36a962f8b79748a860f291db28752d9b","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B/blob/37fd8caf36a962f8b79748a860f291db28752d9b/modeling_qwen2_rm.py"},{"title":"modeling_qwen2_rm.py · Qwen/Qwen2.5-Math-PRM-7B at main","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/blob/main/modeling_qwen2_rm.py"},{"title":"Support for Qwen 2.5 Math PRMs · Issue #43 · huggingface/search-and-learn","url":"https://github.com/huggingface/search-and-learn/issues/43"},{"title":"Qwen2.5 - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen25"},{"title":"Qwen/Qwen2.5-Math-PRM-7B · Error loading model","url":"https://huggingface.co/Qwen/Qwen2.5-Math-PRM-7B/discussions/10"}]

Based on the search results, I didn't find a specific model called "Qwen-2.5-7B-FoVer-PRM" on Hugging Face. However, I found related Process Reward Models (PRMs) for Qwen 2.5:

**Related Models Found:**

1. **Qwen2.5-Math-PRM-7B** - Qwen released Process Reward Models (PRMs), including Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B.

2. **Qwen2.5-Math-PRM-7B is a process reward model typically used for offering feedback on the quality of reasoning and intermediate steps rather than generation. PRMs emerge as a promising approach for process supervision in mathematical reasoning of Large Language Models (LLMs), aiming to identify and mitigate intermediate errors in the reasoning processes.

3. **Skywork o1 Open-PRM-Qwen-2.5-7B extends the capabilities of the 1.5B model by scaling up to handle more demanding reasoning tasks, pushing the boundaries of AI reasoning.

The specific "FoVer-PRM" variant you mentioned doesn't appear in the search results. It's possible that this is a very recent model, a private repository, or it may be referenced under a different name. If you have more details about where this model is hosted or additional context, I can search for more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "788ff724-4f04-45cf-8381-f41bc04a61f8",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "2f3b2ed8-11c3-4379-a485-42d59b26ff5a",
  "sourceToolAssistantUUID": "788ff724-4f04-45cf-8381-f41bc04a61f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:33:53.076Z_

<details><summary>↩ Tool result · `toolu_01MTYNpfVQujE2R4BkUBJmrs`</summary>

```text
Web search results for query: "SAFE step-level verification github code available"

Links: [{"title":"Secure use reference - GitHub Docs","url":"https://docs.github.com/en/actions/reference/security/secure-use"},{"title":"StepSecurity - Detect, Prevent, and Respond to Software Supply Chain Attacks","url":"https://www.stepsecurity.io/"},{"title":"Safe Outputs MCP Gateway Specification | GitHub Agentic Workflows","url":"https://github.github.com/gh-aw/reference/safe-outputs-specification/"},{"title":"StepSecurity · GitHub","url":"https://github.com/step-security"},{"title":"GitHub Actions Security - StepSecurity","url":"https://www.stepsecurity.io/github-actions-and-stepsecurity"},{"title":"GitHub - Authenticator-Extension/Authenticator: Authenticator generates 2-Step Verification codes in your browser. · GitHub","url":"https://github.com/Authenticator-Extension/authenticator"},{"title":"2-step-verification · GitHub Topics · GitHub","url":"https://github.com/topics/2-step-verification"},{"title":"Two step verification · GitHub","url":"https://gist.github.com/stamp/3918214"},{"title":"GitHub - step-security/harden-runner: Harden-Runner is a CI/CD security agent that works like an EDR for GitHub Actions runners. It monitors network egress, file integrity, and process activity on those runners, detecting threats in real-time. · GitHub","url":"https://github.com/step-security/harden-runner"},{"title":"GitHub - Hameem1/Step-Detection-using-Machine-Learning: Implements an entire machine learning pipeline to train and evaluate a Random Forest Classifier on labeled gait data for walking. Data generated during the experiment has led to helpful insights in to the problem domain.","url":"https://github.com/Hameem1/Step-Detection-using-Machine-Learning"}]

Based on the search results, here's what I found regarding SAFE step-level verification:

The search results include information about SAFE outputs processing operations with validation involving pre-execution verification of operation structure, limits, and authorization. This appears to be part of schema validation, limit enforcement, and allowlist checking.

Additionally, there's a GitHub specification related to this: SAFE includes post-compilation checking of configuration integrity through hash validation and staged mode for preview execution without creating permanent GitHub resources.

The most relevant resource appears to be the GitHub Agentic Workflows documentation at **https://github.github.com/gh-aw/reference/safe-outputs-specification/**, which contains detailed information about the SAFE outputs specification including step-level verification requirements.

However, the search results don't show a specific standalone GitHub repository dedicated exclusively to SAFE step-level verification code. If you're looking for implementation code, you may want to check the official GitHub Agentic Workflows repository or the GitHub documentation site directly for links to related code repositories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d80a505-a674-4fda-bd05-272a0e1fdd41",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "d86a2ebf-c33f-4748-a89a-aca518d77990",
  "sourceToolAssistantUUID": "6d80a505-a674-4fda-bd05-272a0e1fdd41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T00:33:53.568Z_

<details><summary>↩ Tool result · `toolu_01CrjNFrCG9ueqT5kq5Bmjrv`</summary>

```text
Web search results for query: "VersaPRM huggingface model availability"

Links: [{"title":"UW-Madison-Lee-Lab/VersaPRM · Hugging Face","url":"https://huggingface.co/UW-Madison-Lee-Lab/VersaPRM"},{"title":"VersaPRM - a UW-Madison-Lee-Lab Collection","url":"https://huggingface.co/collections/UW-Madison-Lee-Lab/versaprm"},{"title":"Models – Hugging Face","url":"https://huggingface.co/models"},{"title":"Loading models · Hugging Face","url":"https://huggingface.co/docs/transformers/models"},{"title":"Models · Hugging Face","url":"https://huggingface.co/docs/transformers/main_classes/model"},{"title":"Hugging Face – The AI community building the future.","url":"https://huggingface.co/"},{"title":"The Model Hub · Hugging Face","url":"https://huggingface.co/docs/hub/models-the-hub"},{"title":"Models compatible with the Transformers library – Hugging Face","url":"https://huggingface.co/models?library=transformers"},{"title":"Models available on all – Hugging Face","url":"https://huggingface.co/models?inference_provider=all&sort=trending"},{"title":"Hugging Face · GitHub","url":"https://github.com/huggingface"}]

Based on the search results, I can provide you with information about the VersaPRM model availability on Hugging Face:

VersaPRM is a fine-tuned version of UW-Madison-Lee-Lab/Llama-PRM800K on UW-Madison-Lee-Lab/MMLU-Pro-CoT-Train-Labeled. The model is available on Hugging Face under the repository `UW-Madison-Lee-Lab/VersaPRM`.

However, this model isn't deployed by any Inference Provider. This means you cannot use it directly through Hugging Face's inference API, but you can still download and use it locally in your own applications.

Additionally, there is a collection of VersaPRMs using various training configurations, which provides multiple variants of the model for different use cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9c4d6fc-54d3-40de-9328-49c6e902aad5",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "78d0768d-6052-4ca4-b2d0-ac54c72d39c1",
  "sourceToolAssistantUUID": "c9c4d6fc-54d3-40de-9328-49c6e902aad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-12T00:33:56.112Z_

The last two searches need refinement. Let me do more targeted follow-up searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78d0768d-6052-4ca4-b2d0-ac54c72d39c1",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjc1bJu5rYrBZTvZT8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9d64075-59a2-46cc-b92f-2fc643f3390d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcdN5XopLkxm3by5prGtdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 736,
      "cache_creation_input_tokens": 3735,
      "cache_read_input_tokens": 9491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3735,
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

_source line 18 · 2026-05-12T00:33:57.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017tgwfTNDKoQ5aGXdJLRXdH`</summary>

```json
{
  "query": "FoVer formal verification process reward model paper github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9d64075-59a2-46cc-b92f-2fc643f3390d",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjc1bJu5rYrBZTvZT8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed3f906d-2836-4ed4-9ff9-ed57acee3f59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcdN5XopLkxm3by5prGtdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 736,
      "cache_creation_input_tokens": 3735,
      "cache_read_input_tokens": 9491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3735,
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

_source line 19 · 2026-05-12T00:33:57.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CywxKPhpQUDNZ7iDCrqMfw`</summary>

```json
{
  "query": "SAFE search for accurate fact-checking verification LLM github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed3f906d-2836-4ed4-9ff9-ed57acee3f59",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjc1bJu5rYrBZTvZT8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9ccf383-c1cf-46e4-bbe5-ce53fa2ac8de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcdN5XopLkxm3by5prGtdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 736,
      "cache_creation_input_tokens": 3735,
      "cache_read_input_tokens": 9491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3735,
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

_source line 20 · 2026-05-12T00:33:58.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C92UR9JkRpQ43nubznYmkE`</summary>

```json
{
  "query": "EMNLP 2026 Findings track vs main conference format requirements page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9ccf383-c1cf-46e4-bbe5-ce53fa2ac8de",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawjc1bJu5rYrBZTvZT8k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ed5582b-e679-457c-b15b-43f03c3f7ce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PcdN5XopLkxm3by5prGtdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 736,
      "cache_creation_input_tokens": 3735,
      "cache_read_input_tokens": 9491,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 736,
          "output_tokens": 181,
          "cache_read_input_tokens": 9491,
          "cache_creation_input_tokens": 3735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3735,
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

_source line 21 · 2026-05-12T00:34:03.387Z_

<details><summary>↩ Tool result · `toolu_017tgwfTNDKoQ5aGXdJLRXdH`</summary>

```text
Web search results for query: "FoVer formal verification process reward model paper github"

Links: [{"title":"FoVer: Efficient PRM Training Data Synthesis via Formal Verification","url":"https://fover-prm.github.io/"},{"title":"GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub","url":"https://github.com/psunlpgroup/FoVer"},{"title":"FOVER: Training Verifiers with Formal Tools","url":"https://www.emergentmind.com/papers/2505.15960"},{"title":"Paper page - Training Step-Level Reasoning Verifiers with Formal Verification Tools","url":"https://huggingface.co/papers/2505.15960"},{"title":"Actions · psunlpgroup/FoVer","url":"https://github.com/psunlpgroup/FoVer/actions"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/abs/2505.15960"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=formal+verification"},{"title":"(PDF) Training Step-Level Reasoning Verifiers with Formal Verification Tools","url":"https://www.researchgate.net/publication/391990893_Training_Step-Level_Reasoning_Verifiers_with_Formal_Verification_Tools"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data | OpenReview","url":"https://openreview.net/forum?id=LAejsDitr3"}]

Based on the search results, here's what I found about FoVer:

## FoVer: Formal Verification for Process Reward Models

FoVer is a framework that synthesizes PRM training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle.

### Key Innovation

FoVer efficiently creates accurate training data for process reward models (PRMs) using formal verification tools. In contrast, existing methods are costly and produce noisy labels, as they rely on human annotation or repeated LLM calls.

### Paper and Publication

The paper "Efficient PRM Training Data Synthesis via Formal Verification" was published in ACL 2026 Findings. The authors include Ryo Kamoi, Yusen Zhang, Nan Zhang, and others.

### GitHub Repository

The GitHub repository is available at https://github.com/psunlpgroup/FoVer, and includes code and materials for the paper along with trained models.

### Results

Experiments on 12 reasoning benchmarks show that fine-tuning on the training data improves PRMs not only on math and logic reasoning tasks, which are informal variants of the training tasks, but also on NLI and BBH benchmarks, which differ substantially from the tasks used to construct the training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed3f906d-2836-4ed4-9ff9-ed57acee3f59",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "1299857c-63c6-4eb3-b229-1393b6910ef7",
  "sourceToolAssistantUUID": "ed3f906d-2836-4ed4-9ff9-ed57acee3f59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T00:34:03.944Z_

<details><summary>↩ Tool result · `toolu_01CywxKPhpQUDNZ7iDCrqMfw`</summary>

```text
Web search results for query: "SAFE search for accurate fact-checking verification LLM github"

Links: [{"title":"GitHub - jagilley/fact-checker: Fact-checking LLM outputs with self-ask · GitHub","url":"https://github.com/jagilley/fact-checker"},{"title":"fact check and claim verification using large language models · GitHub","url":"https://gist.github.com/chunhualiao/3925c8deb8b25636a880bef0ea1cbc1c"},{"title":"Long-form factuality in large language models Jerry Wei∗1 Chengrun Yang∗1","url":"https://openreview.net/pdf?id=4M9f8VMt2C"},{"title":"DeepMind develops SAFE, an AI-based app that can fact-check LLMs","url":"https://techxplore.com/news/2024-03-deepmind-safe-ai-based-app.html"},{"title":"GitHub - BharathxD/ClaimeAI: This AI fact-checking system, built with LangGraph, dissects text into verifiable claims, cross-referencing them with real-world evidence via web searches. It then generates detailed accuracy reports, ideal for combating misinformation in LLM outputs, news, or any text. · GitHub","url":"https://github.com/BharathxD/fact-checker"},{"title":"GitHub - yuxiaw/OpenFactCheck · GitHub","url":"https://github.com/yuxiaw/OpenFactCheck"},{"title":"OpenFactCheck: A Unified Framework for Factuality Evaluation of LLMs","url":"https://openfactcheck.com/"},{"title":"GitHub - wangcunxiang/LLM-Factuality-Survey: The repository for the survey paper <&lt;Survey on Large Language Models Factuality: Knowledge, Retrieval and Domain-Specificity>> · GitHub","url":"https://github.com/wangcunxiang/LLM-Factuality-Survey"},{"title":"Awesome-LLM-Safety/subtopic/Truthfulness&Misinformation.md at main · ydyjya/Awesome-LLM-Safety","url":"https://github.com/ydyjya/Awesome-LLM-Safety/blob/main/subtopic/Truthfulness&Misinformation.md"},{"title":"GitHub - mbzuai-nlp/fire: A lightweight, agent-style framework for fact-checking atomic claims using iterative retrieval and verification. Reduces LLM and search cost while maintaining strong factuality performance. · GitHub","url":"https://github.com/mbzuai-nlp/fire"}]

Based on the search results, here's what I found about SAFE for fact-checking verification of LLMs:

## SAFE: Search-Augmented Factuality Evaluator

SAFE is an AI-based system developed by Google's DeepMind that can be used to fact-check the results of LLMs such as ChatGPT.

### Key Features and Performance

SAFE outperforms crowdsourced human annotators, agreeing with 72% of human annotations and winning 76% of disagreement cases from a random sample of 100 disagreement cases. SAFE is also 20× cheaper than human annotators.

### How It Works

SAFE uses two key insights: first, long-form responses should be evaluated at the granularity of individual facts, following text decomposition.

### GitHub Repository

The code is publicly available at https://github.com/google-deepmind/long-form-factuality/tree/main/eval/safe.

### Related Projects

The search also revealed other fact-checking frameworks inspired by or related to SAFE:
- ClaimeAI uses the Search-Augmented Factuality Evaluator (SAFE) methodology, implementing the basic idea of using search results to verify individual claims
- FIRE is an agent-based framework that, compared to SAFE, integrates reasoning and retrieval, dynamically controls retrieval depth, and reduces LLM cost by 7.6× and search cost by 16.5×


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9ccf383-c1cf-46e4-bbe5-ce53fa2ac8de",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "fa1f0696-e819-4b3f-b3f5-b015d5aa7b96",
  "sourceToolAssistantUUID": "d9ccf383-c1cf-46e4-bbe5-ce53fa2ac8de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T00:34:13.791Z_

<details><summary>↩ Tool result · `toolu_01C92UR9JkRpQ43nubznYmkE`</summary>

```text
Web search results for query: "EMNLP 2026 Findings track vs main conference format requirements page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Update EMNLP System Demonstrations Track with 2026 conference data · huggingface/ai-deadlines at 6a94f2c","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/6a94f2c940ba976564775b34f6b224b0f9ad638d"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"}]

The search found general information about EMNLP 2026, but I need to search more specifically for the Findings track requirements and page limit specifications to compare with the main conference.

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"}]

I found that the format is two-column with an 8-page limit for long papers and a 4-page limit for short papers for EMNLP 2026. However, I still need to find specific information about the Findings track. Let me search more specifically for that.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"}]

Let me search directly on the EMNLP 2026 website for the Findings track page.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Sponsors - EMNLP 2026","url":"https://2026.emnlp.org/sponsors/"}]

Let me search for the main conference paper requirements with page limits more specifically.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"LINGUIST List 37.1616 Confs: Workshop at EMNLP 2026: Multimodal Interaction in Face-to-Face Dialogue (Hungary)","url":"https://linguistlist.org/issues/37/1616/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026: Conference on Empirical Methods in Natural Language Processing","url":"https://www.myhuiban.com/conference/424?lang=en_us"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on my search results, I have found information about the EMNLP 2026 main conference paper requirements. However, I was unable to locate a dedicated "Findings track" call for papers on the EMNLP 2026 website. Let me provide you with what I found:

## Summary of EMNLP 2026 Main Conference Paper Requirements

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Findings Track Information

Unfortunately, I was unable to locate a dedicated call for papers or specific submission requirements page for an EMNLP 2026 Findings track in the search results. The official EMNLP 2026 website mentions that some papers not selected for the main conference may be considered for the Findings (based on references in the registration information), but a dedicated Findings track CFP with page limit specifications was not found in my search.

This differs from other ACL conferences (like EACL 2026, which explicitly mentions that Findings papers may consist of a similar structure to main conference papers), but EMNLP 2026's specific Findings track requirements may not yet be published, or may be published on a separate page that wasn't captured in my searches. I recommend checking the EMNLP 2026 official website directly or contacting the program chairs for the most current information on the Findings track specifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ed5582b-e679-457c-b15b-43f03c3f7ce9",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "a7aa8bda-ac40-4439-98c0-cbfea779aee8",
  "sourceToolAssistantUUID": "1ed5582b-e679-457c-b15b-43f03c3f7ce9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T00:34:16.359Z_

Now let me do one more targeted search for the FoVer model on HuggingFace specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7aa8bda-ac40-4439-98c0-cbfea779aee8",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011CawjdW2sA8TrYzXVwtpnN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1aaf6315-5f6a-4866-b9d5-366ed07361c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137SdbeZu5rXAqd2n4PgQuu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5552,
      "cache_read_input_tokens": 13226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5552,
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

_source line 25 · 2026-05-12T00:34:16.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DXWm8PhA92xfWdVS9u2FZw`</summary>

```json
{
  "query": "site:huggingface.co psunlpgroup FoVer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aaf6315-5f6a-4866-b9d5-366ed07361c3",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011CawjdW2sA8TrYzXVwtpnN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1716f929-43c7-4231-b6aa-1361b95a7f7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137SdbeZu5rXAqd2n4PgQuu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5552,
      "cache_read_input_tokens": 13226,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 13226,
          "cache_creation_input_tokens": 5552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5552,
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

_source line 26 · 2026-05-12T00:34:21.887Z_

<details><summary>↩ Tool result · `toolu_01DXWm8PhA92xfWdVS9u2FZw`</summary>

```text
Web search results for query: "site:huggingface.co psunlpgroup FoVer"

Links: [{"title":"https://huggingface.co/datasets/ryokamoi/FoVer-mis...","url":"https://huggingface.co/datasets/ryokamoi/FoVer-misc/resolve/main/README.md?download=true"},{"title":"FoVer - a ryokamoi Collection","url":"https://huggingface.co/collections/ryokamoi/fover"},{"title":"RaphaelLiu/PusaV1 · Hugging Face","url":"https://huggingface.co/RaphaelLiu/PusaV1"},{"title":"RaphaelLiu/PusaV1 at main","url":"https://huggingface.co/RaphaelLiu/PusaV1/tree/main"},{"title":"RaphaelLiu/Pusa-V0.5 · Hugging Face","url":"https://huggingface.co/RaphaelLiu/Pusa-V0.5"},{"title":"PSHuman - a Hugging Face Space by fffiloni","url":"https://huggingface.co/spaces/fffiloni/PSHuman"},{"title":"AI4Protein/DeepSol · Datasets at Hugging Face","url":"https://huggingface.co/datasets/AI4Protein/DeepSol"},{"title":"unsloth/Qwen3.5-9B-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3.5-9B-GGUF"},{"title":"Paper page - ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents","url":"https://huggingface.co/papers/2603.18815"},{"title":"P-tuning · Hugging Face","url":"https://huggingface.co/docs/peft/en/package_reference/p_tuning"}]

Based on the search results, I found information about FoVer on Hugging Face:

FoVer is an approach for training Process Reward Models (PRMs) on step-level error labels that are automatically annotated using formal verification tools (e.g., Z3, Isabelle). The project includes a dataset with automatically annotated step-level error labels on LLM responses for formal logic and proof tasks.

The FoVer project appears to be associated with the psunlpgroup GitHub organization. The FoVer models on Hugging Face are Process Reward Models trained on step-level error labels automatically annotated by formal verification tools. The project provides both raw datasets and balanced datasets for training, with models available for Llama 3.1 8B and Qwen 2.5 7B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1716f929-43c7-4231-b6aa-1361b95a7f7f",
  "isSidechain": true,
  "promptId": "09e5626c-0c83-4d7f-8c3b-ff62fb446df0",
  "agentId": "a4600e201e124ae0b",
  "type": "user",
  "uuid": "61e03a34-193a-4462-bd4b-1991fcaaf8ff",
  "sourceToolAssistantUUID": "1716f929-43c7-4231-b6aa-1361b95a7f7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-12T00:34:47.201Z_

Here are the findings for each of your five research questions:

**1. EMNLP 2026 ARR Deadline & Format**
The ARR submission deadline is **May 25, 2026**. Commitment deadline is August 2, 2026. Format: long papers 8 pages, short papers 4 pages (plus 1 extra page in camera-ready). Critical caveat: since EMNLP and AACL share the ARR May cycle, authors **must select a target conference at submission time, and this choice is binding**. Findings track exists but uses the same ARR submission process; no separate page limits are published -- Findings papers follow the same format as main conference papers.

**2. 7B Model Autoformalization**
Evidence is encouraging. DeepSeek-Prover-v2 (7B) is used for formal reasoning. DeepSeekMath-7B achieved performance comparable to Minerva-540B on math reasoning. The paper "Lean-ing on Quality" (Feb 2025) shows that data quality matters more than scale -- high-quality Lean data with 1/150th the tokens outperforms multilingual datasets. FormaRL (COLM 2025) enhances autoformalization with no labeled data. Bottom line: **7B models are viable for autoformalization when trained on high-quality data**, but they lag behind frontier models on the hardest benchmarks.

**3. FoVer-PRM Availability**
Yes, publicly available. The GitHub repo is at [psunlpgroup/FoVer](https://github.com/psunlpgroup/FoVer) (ACL 2026 Findings). Models are hosted on HuggingFace under a [ryokamoi FoVer collection](https://huggingface.co/collections/ryokamoi/fover), including variants for **Llama 3.1 8B and Qwen 2.5 7B**. Training data with step-level error labels (annotated via Z3/Isabelle) is also available.

**4. VersaPRM Availability**
Yes, available at [UW-Madison-Lee-Lab/VersaPRM](https://huggingface.co/UW-Madison-Lee-Lab/VersaPRM) on HuggingFace (fine-tuned on Llama-PRM800K with MMLU-Pro-CoT-Train-Labeled). A full collection of VersaPRM variants exists. No hosted inference endpoint, but weights are downloadable for local use.

**5. SAFE Codebase**
Yes, available. Google DeepMind's SAFE (Search-Augmented Factuality Evaluator) code is at [google-deepmind/long-form-factuality](https://github.com/google-deepmind/long-form-factuality/tree/main/eval/safe). It decomposes long-form text into atomic claims and verifies each via search. It outperformed crowdsourced annotators (72% agreement, winning 76% of disputes) at 20x lower cost.

Sources:
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 binding conference selection notice](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [Autoformalization Survey (2025)](https://arxiv.org/abs/2505.23486)
- [Lean-ing on Quality](https://arxiv.org/html/2502.15795)
- [FormaRL (COLM 2025)](https://github.com/THUNLP-MT/FormaRL)
- [FoVer GitHub](https://github.com/psunlpgroup/FoVer)
- [FoVer HuggingFace Collection](https://huggingface.co/collections/ryokamoi/fover)
- [VersaPRM on HuggingFace](https://huggingface.co/UW-Madison-Lee-Lab/VersaPRM)
- [SAFE Codebase](https://github.com/google-deepmind/long-form-factuality/tree/main/eval/safe)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61e03a34-193a-4462-bd4b-1991fcaaf8ff",
  "isSidechain": true,
  "agentId": "a4600e201e124ae0b",
  "requestId": "req_011Cawje6cyxJiYyewTnrxja",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a703e828-65d7-44d6-b8ed-23f92e23ecc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "71515179-49ba-4f84-8f4c-7a23c618c0fd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UxuMTHBD6oLLCEjE125DH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 815,
      "cache_read_input_tokens": 18778,
      "output_tokens": 1048,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 815
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1048,
          "cache_read_input_tokens": 18778,
          "cache_creation_input_tokens": 815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 815,
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
