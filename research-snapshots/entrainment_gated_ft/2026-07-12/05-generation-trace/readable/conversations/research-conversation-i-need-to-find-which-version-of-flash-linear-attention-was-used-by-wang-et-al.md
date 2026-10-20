# Research conversation: I need to find which version of flash-linear-attention was used by Wang et al. in their paper "A Systematic Analysis of 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 1
- **Tool calls:** 35
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4e73858aead4b989.jsonl`
- **Structured JSON:** [`a9cdd429a64c11e559ae.json`](../../sessions/a9/a9cdd429a64c11e559ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

84 recorded events

### User

_source line 1 · 2026-05-18T12:25:46.079Z_

I need to find which version of flash-linear-attention was used by Wang et al. in their paper "A Systematic Analysis of Hybrid Linear Attention" (arXiv 2507.06457). Please:

1. Use WebFetch to get https://arxiv.org/abs/2507.06457 — look for any GitHub repo link, code availability section, or version information
2. Use WebFetch to get https://huggingface.co/m-a-p/transformer_340M_baseline — look for model card info, requirements, or fla version
3. Use WebFetch to get https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research — look for all model links and any version info mentioned
4. Try WebSearch for "m-a-p gated_deltanet_1.3B_hybrid" or similar model names on huggingface to find a model card that might mention fla version

Report any version numbers, commit hashes, or requirements files you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "cb10215a-a6bf-4728-bdc6-53d6c3f715e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T12:25:46.081Z_

```json
{
  "parentUuid": "cb10215a-a6bf-4728-bdc6-53d6c3f715e3",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2089efda-5782-412f-a014-0c016028bf23",
  "timestamp": "2026-05-18T12:25:46.081Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T12:25:49.236Z_



I'll start by loading the WebFetch and WebSearch tools, then make all the requests.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2089efda-5782-412f-a014-0c016028bf23",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2k2Y7DkbVxMWVvKBpM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d430fa61-5eb9-4a2c-b0dd-9ff593fdb53a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCPA4x6cQAzYqwL4kdDB7M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7299,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7299,
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

_source line 4 · 2026-05-18T12:25:49.555Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018cd4mwmyrCGHzymFZkS9zz`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d430fa61-5eb9-4a2c-b0dd-9ff593fdb53a",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2k2Y7DkbVxMWVvKBpM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fee0adfa-5ab9-4cee-8b38-4fe75c141a69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCPA4x6cQAzYqwL4kdDB7M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7299,
      "cache_read_input_tokens": 8252,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7299
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7299,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7299,
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

_source line 5 · 2026-05-18T12:25:49.557Z_

<details><summary>↩ Tool result · `toolu_018cd4mwmyrCGHzymFZkS9zz`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "fee0adfa-5ab9-4cee-8b38-4fe75c141a69",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "fcc54be7-b101-4b35-a407-3d8214f1217b",
  "sourceToolAssistantUUID": "fee0adfa-5ab9-4cee-8b38-4fe75c141a69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T12:25:52.651Z_



Now let me make all four requests in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc54be7-b101-4b35-a407-3d8214f1217b",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2kHiRXX3QpmX8NCJPa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33825a08-38df-4331-8c6e-c7e9269eca9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbSbUV8Zhk2jckBYCBh5ED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 15551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1957,
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

_source line 7 · 2026-05-18T12:25:54.527Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YUmHW1zPqP7724dJXv4eVc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.06457",
  "prompt": "Find any information about: 1) GitHub repository links or code availability, 2) flash-linear-attention (fla) version or commit hash, 3) software dependencies or requirements, 4) any mention of specific library versions used. Extract all URLs, version numbers, and commit hashes mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33825a08-38df-4331-8c6e-c7e9269eca9f",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2kHiRXX3QpmX8NCJPa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c501a9b4-2f81-4fc0-8f5e-fd1f0b932445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbSbUV8Zhk2jckBYCBh5ED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 15551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1957,
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

_source line 8 · 2026-05-18T12:25:56.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RGVP8DoqMegtEpmyorkmob`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/transformer_340M_baseline",
  "prompt": "Find any information about: 1) flash-linear-attention (fla) version or commit hash, 2) software dependencies or requirements, 3) training configuration or library versions, 4) any links to GitHub repos or requirements files. Extract all version numbers and dependency information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c501a9b4-2f81-4fc0-8f5e-fd1f0b932445",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2kHiRXX3QpmX8NCJPa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "653eab12-1381-4d5a-86a8-5ebdc5a288e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbSbUV8Zhk2jckBYCBh5ED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 15551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1957,
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

_source line 9 · 2026-05-18T12:25:57.824Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013LDnTErVSkKDcbtaoXqFJU`</summary>

```json
{
  "url": "https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research",
  "prompt": "List ALL model names/links in this collection. For each, note any version information, fla version, flash-linear-attention version, commit hash, or dependency information mentioned. Extract everything related to software versions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "653eab12-1381-4d5a-86a8-5ebdc5a288e3",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2kHiRXX3QpmX8NCJPa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "794396e9-03e2-441f-ba48-d295e72b110d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbSbUV8Zhk2jckBYCBh5ED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 15551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1957,
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

_source line 10 · 2026-05-18T12:25:58.306Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GWYAoKHPG1s5nGB9ofPmXs`</summary>

```json
{
  "query": "m-a-p gated_deltanet hybrid flash-linear-attention fla version huggingface model card"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "794396e9-03e2-441f-ba48-d295e72b110d",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2kHiRXX3QpmX8NCJPa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ce2a85b-6df0-4b5b-ae5b-c314ab2a5062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbSbUV8Zhk2jckBYCBh5ED",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 15551,
      "output_tokens": 464,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 464,
          "cache_read_input_tokens": 15551,
          "cache_creation_input_tokens": 1957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1957,
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

_source line 11 · 2026-05-18T12:25:58.918Z_

<details><summary>↩ Tool result · `toolu_01YUmHW1zPqP7724dJXv4eVc`</summary>

```text
# Search Results Summary

Based on the provided content, here's what I found:

## Code/Repository Availability
The paper mentions open-sourced models with this reference: **"Our models are open-sourced at [this https URL]"** - however, the actual URL is not fully displayed in the extracted text, only a placeholder link to a Hugging Face collection about "hybrid-linear-attention-research."

## Flash-Linear-Attention (FLA)
No mention of flash-linear-attention, version numbers, or commit hashes appears in this document.

## Software Dependencies
No specific library versions, dependency lists, or software requirements are detailed in the provided content.

## URLs Found
- Hugging Face collection reference: `https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e`
- DOI: `https://doi.org/10.48550/arXiv.2507.06457`

## Conclusion
The abstract references open-sourced models but does not provide detailed technical setup information, version specifics, or GitHub repository links within this landing page content. For complete implementation details, accessing the full PDF or HTML paper version would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c501a9b4-2f81-4fc0-8f5e-fd1f0b932445",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "9b5a02b8-96e4-4ad4-8ecc-0bc7e2ed40e1",
  "sourceToolAssistantUUID": "c501a9b4-2f81-4fc0-8f5e-fd1f0b932445",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T12:26:00.512Z_

<details><summary>↩ Tool result · `toolu_01RGVP8DoqMegtEpmyorkmob`</summary>

```text
# Analysis of Model Page Content

Based on the provided web page content for `m-a-p/transformer_340M_baseline`, here's what I found:

## Information Available:

1. **Model Specifications:**
   - Model size: 0.3B params
   - Tensor type: F32
   - Format: Safetensors

2. **Collection Reference:**
   - Part of "Hybrid Linear Attention Research" collection
   - Updated Sep 11, 2025
   - Contains 62 items focused on "1.3B & 340M hybrid linear-attention experiments"

## Information NOT Available:

❌ **Flash-Linear-Attention (FLA) version or commit hash** - Not provided on this page

❌ **Software dependencies or requirements** - Not listed (page notes "No model card")

❌ **Training configuration or library versions** - Not specified

❌ **GitHub repo links or requirements files** - Not included in the content provided

## Recommendation:

To find the missing technical details, you would need to:
- Check the actual **model card** (if one exists beyond what's shown)
- Visit the **Files section** (indicated by "xet" link)
- Check the associated **GitHub repository** for the m-a-p organization
- Review the **Hybrid Linear Attention Research collection** page for documentation
- Contact the model creators (Multimodal Art Projection organization)

The provided web page is primarily a landing/overview page without detailed technical specifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "653eab12-1381-4d5a-86a8-5ebdc5a288e3",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "fab4a885-0058-4ae2-8d24-747131e38315",
  "sourceToolAssistantUUID": "653eab12-1381-4d5a-86a8-5ebdc5a288e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T12:26:04.731Z_

<details><summary>↩ Tool result · `toolu_01GWYAoKHPG1s5nGB9ofPmXs`</summary>

```text
Web search results for query: "m-a-p gated_deltanet hybrid flash-linear-attention fla version huggingface model card"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Idiap/gated-deltanet-attn-1.4B-30B · Hugging Face","url":"https://huggingface.co/Idiap/gated-deltanet-attn-1.4B-30B"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"GitHub - NVlabs/GatedDeltaNet: [ICLR 2025] Official PyTorch Implementation of Gated Delta Networks: Improving Mamba2 with Delta Rule · GitHub","url":"https://github.com/NVlabs/GatedDeltaNet"},{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"Gated DeltaNet | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llms-from-scratch/ch04/08_deltanet/"},{"title":"DeltaNet Explained (Part I) | Songlin Yang","url":"https://sustcsonglin.github.io/blog/2024/deltanet-1/"},{"title":"hustvl/InfiniteVL · Hugging Face","url":"https://huggingface.co/hustvl/InfiniteVL"},{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e"},{"title":"Linear Attention Models (GLA, Delta Net) | fla-org/flame | DeepWiki","url":"https://deepwiki.com/fla-org/flame/7.3-linear-attention-models-(gla-delta-net)"}]

Based on the web search results, I found relevant information about the m-a-p gated_deltanet hybrid flash-linear-attention model:

The m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 model is a gated_deltanet architecture with 0.4B parameters that is part of a collection for "All 1.3B & 340M hybrid linear-attention experiments".

Gated DeltaNet was added to the flash-linear-attention (FLA) library in December 2024. The FLA library now provides a flexible way for training hybrid models.

The model appears to be housed on Hugging Face. The model card indicates there is currently "No model card" available at the specific Hugging Face URL (m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1).

These models are part of m-a-p's hybrid linear-attention research collection featuring 1.3B and 340M parameter experiments.

If you need more detailed information about the model card or specific configuration details, you may want to visit the Hugging Face model page directly or check the related FLA documentation and repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ce2a85b-6df0-4b5b-ae5b-c314ab2a5062",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "03eea91a-7c2d-4233-81f3-e579ce6bc2fa",
  "sourceToolAssistantUUID": "5ce2a85b-6df0-4b5b-ae5b-c314ab2a5062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T12:26:10.508Z_

<details><summary>↩ Tool result · `toolu_013LDnTErVSkKDcbtaoXqFJU`</summary>

```text
# Hybrid Linear Attention Research Collection - Model List

## All Models in Collection

### 340M Parameter Models (20B Tokens)

1. **m-a-p/340M-20B-GatedDeltaNet-hybrid-3-1** - 0.4B | Updated Mar 3, 2025
2. **m-a-p/340M-20B-GatedDeltaNet-hybrid-6-1** - 0.4B | Updated Mar 3, 2025
3. **m-a-p/340M-20B-GLA-hybrid-6-1** - 0.3B | Updated Mar 3, 2025
4. **m-a-p/340M-20B-GLA-hybrid-3-1** - 0.3B | Updated Mar 3, 2025
5. **m-a-p/340M-20B-GLA-hybrid-12-1** - 0.3B | Updated Mar 3, 2025
6. **m-a-p/340M-20B-GLA-hybrid-24-1** - 0.3B | Updated Mar 3, 2025
7. **m-a-p/340M-20B-HGRN2-pure-baseline** - 0.3B | Updated Mar 3, 2025
8. **m-a-p/340M-20B-HGRN2-hybrid-6-1** - 0.3B | Updated Mar 3, 2025
9. **m-a-p/340M-20B-HGRN2-hybrid-3-1** - 0.3B | Updated Mar 3, 2025
10. **m-a-p/340M-20B-HGRN2-hybrid-12-1** - 0.3B | Updated Mar 4, 2025
11. **m-a-p/340M-20B-HGRN2-hybrid-24-1** - 0.3B | Updated Mar 4, 2025
12. **m-a-p/340M-20B-DeltaNet-hybrid-3-1** - 0.3B | Updated Mar 4, 2025
13. **m-a-p/340M-20B-DeltaNet-pure** - 0.3B | Updated Mar 4, 2025
14. **m-a-p/340M-20B-DeltaNet-hybrid-6-1** - 0.3B | Updated Mar 4, 2025
15. **m-a-p/340M-20B-DeltaNet-hybrid-12-1** - 0.3B | Updated Mar 4, 2025
16. **m-a-p/340M-20B-DeltaNet-hybrid-24-1** - 0.3B | Updated Mar 4, 2025
17. **m-a-p/340M-20B-RetNet-hybrid-24-1** - 0.3B | Updated Mar 4, 2025
18. **m-a-p/340M-20B-RetNet-hybrid-12-1** - 0.3B | Updated Mar 4, 2025
19. **m-a-p/340M-20B-RetNet-hybrid-6-1** - 0.3B | Updated Mar 4, 2025
20. **m-a-p/340M-20B-RetNet-hybrid-3-1** - 0.3B | Updated Mar 4, 2025
21. **m-a-p/340M-20B-RetNet-pure** - 0.3B | Updated Mar 4, 2025
22. **m-a-p/340M-20B-HGRN-hybrid-3-1** - 0.3B | Updated Apr 20, 2025
23. **m-a-p/340M-20B-HGRN-hybrid-6-1** - 0.3B | Updated Apr 20, 2025
24. **m-a-p/340M-20B-HGRN-hybrid-12-1** - 0.3B | Updated Apr 20, 2025
25. **m-a-p/340M-20B-HGRN-hybrid-24-1** - 0.3B | Updated Apr 20, 2025
26. **m-a-p/340M-20B-HGRN-pure-baseline** - 0.3B | Updated Apr 20, 2025
27. **m-a-p/340M-20B-GLA-pure-baseline** - 0.3B | Updated May 10, 2025
28. **m-a-p/340M-20B-GatedDeltaNet-hybrid-12-1** - 0.4B | Updated May 10, 2025
29. **m-a-p/340M-20B-GatedDeltaNet-pure-baseline** - 0.4B | Updated Jun 7, 2025
30. **m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1** - 0.4B | Updated Jun 10, 2025
31. **m-a-p/transformer_340M_baseline** - 0.3B | Updated Sep 11, 2025

### 1.3B Parameter Models (100B Tokens)

1. **m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1** - 1B | Updated Apr 20, 2025
2. **m-a-p/1.3B-100B-GatedDeltaNet-hybrid-6-1** - 1B | Updated Apr 20, 2025
3. **m-a-p/1.3B-100B-GatedDeltaNet-hybrid-12-1** - 1B | Updated Apr 20, 2025
4. **m-a-p/1.3B-100B-GatedDeltaNet-hybrid-24-1** - 1B | Updated Apr 20, 2025
5. **m-a-p/1.3B-100B-GLA-hybrid-3-1** - 1B | Updated Apr 20, 2025
6. **m-a-p/1.3B-100B-GLA-hybrid-6-1** - 1B | Updated Apr 20, 2025
7. **m-a-p/1.3B-100B-GLA-hybrid-12-1** - 1B | Updated Apr 20, 2025
8. **m-a-p/1.3B-100B-GLA-hybrid-24-1** - 1B | Updated Apr 20, 2025
9. **m-a-p/1.3B-100B-HGRN2-hybrid-3-1** - 1B | Updated Apr 20, 2025
10. **m-a-p/1.3B-100B-HGRN2-hybrid-6-1** - 1B | Updated Apr 20, 2025
11. **m-a-p/1.3B-100B-HGRN2-hybrid-12-1** - 1B | Updated Apr 20, 2025
12. **m-a-p/1.3B-100B-HGRN2-hybrid-24-1** - 1B | Updated Apr 20, 2025
13. **m-a-p/1.3B-100B-HGRN-hybrid-3-1** - 1B | Updated Apr 20, 2025
14. **m-a-p/1.3B-100B-HGRN-hybrid-6-1** - 1B | Updated Apr 20, 2025
15. **m-a-p/1.3B-100B-HGRN-hybrid-12-1** - 1B | Updated Apr 20, 2025
16. **m-a-p/1.3B-100B-HGRN-hybrid-24-1** - 1B | Updated Apr 20, 2025
17. **m-a-p/1.3B-100B-HGRN-pure** - 1B | Updated Apr 20, 2025
18. **m-a-p/1.3B-100B-RetNet-hybrid-3-1** - 1B | Updated Apr 20, 2025
19. **m-a-p/1.3B-100B-RetNet-hybrid-6-1** - 1B | Updated Apr 20, 2025
20. **m-a-p/1.3B-100B-RetNet-hybrid-12-1** - 1B | Updated Apr 20, 2025
21. **m-a-p/1.3B-100B-RetNet-hybrid-24-1** - 1B | Updated Apr 20, 2025
22. **m-a-p/1.3B-100B-RetNet-pure** - 1B | Updated Apr 20, 2025
23. **m-a-p/1.3B-100B-GLA-pure** - 1B | Updated Apr 20, 2025
24. **m-a-p/1.3B-100B-HGRN2-pure** - 1B | Updated May 10, 2025
25. **m-a-p/1.3B-100B-GatedDeltaNet-pure** - 1B | Updated May 10, 2025
26. **m-a-p/1.3B-100B-DeltaNet-hybrid-3-1** - 1B | Updated Jun 7, 2025
27. **m-a-p/1.3B-100B-DeltaNet-hybrid-6-1** - 1B | Updated Jun 7, 2025
28. **m-a-p/1.3B-100B-DeltaNet-hybrid-12-1** - 1B | Updated Jun 7, 2025
29. **m-a-p/1.3B-100B-DeltaNet-hybrid-24-1** - 1B | Updated Jun 7, 2025
30. **m-a-p/1.3B-100B-DeltaNet-pure** - 1B | Updated Jun 7, 2025
31. **m-a-p/transformer_1.3B_baseline** - 1B | Updated Sep 11, 2025

## Version Information Found

**No explicit version information, commit hashes, or dependency details** (such as Flash Linear Attention versions) are mentioned in the page content. Only update dates and model sizes are provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "794396e9-03e2-441f-ba48-d295e72b110d",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "44eed099-d269-44fc-af68-2278a0862240",
  "sourceToolAssistantUUID": "794396e9-03e2-441f-ba48-d295e72b110d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T12:26:14.492Z_

The model pages have "No model card." Let me try fetching the full paper PDF and also check specific model repos for config files that might mention the fla version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44eed099-d269-44fc-af68-2278a0862240",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2mpy9ZJU5S4gpVw3HF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b20a554-e907-4132-b741-2e43af98973a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3N19Zgtc2FqUK3AYdmCVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 17508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 16 · 2026-05-18T12:26:17.334Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LZdF4AmpzDu1k29zabMaBB`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.06457",
  "prompt": "Find ANY mention of: 1) flash-linear-attention or fla library version, commit hash, or installation instructions, 2) GitHub repository URL for code, 3) software dependencies, requirements, or environment setup, 4) any pip install commands or package versions. Look in the entire paper including appendix, footnotes, and supplementary sections. Extract all version numbers and URLs found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b20a554-e907-4132-b741-2e43af98973a",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2mpy9ZJU5S4gpVw3HF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "903b83a4-8378-4eb4-bb20-228d7c434318",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3N19Zgtc2FqUK3AYdmCVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 17508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 17 · 2026-05-18T12:26:19.220Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011L9tTfi4i7PzZCkWRWcy26`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1",
  "prompt": "Find any information about: 1) flash-linear-attention (fla) version, commit hash, or package version, 2) training configuration, software dependencies, requirements, 3) any config.json contents showing library versions, 4) any README or model card content. Extract all technical details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "903b83a4-8378-4eb4-bb20-228d7c434318",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2mpy9ZJU5S4gpVw3HF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b461ee1-c30e-4090-be91-0918e69135b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3N19Zgtc2FqUK3AYdmCVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 17508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 18 · 2026-05-18T12:26:21.095Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TXFy8V8qtAGPekWKiLZWuh`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/tree/main",
  "prompt": "List ALL files in this model repository. I'm looking for config.json, requirements.txt, README.md, or any file that might contain version information about flash-linear-attention or other dependencies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b461ee1-c30e-4090-be91-0918e69135b7",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2mpy9ZJU5S4gpVw3HF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34db6bc3-e83e-4859-a49b-abdc8b7964b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3N19Zgtc2FqUK3AYdmCVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 17508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3793,
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

_source line 19 · 2026-05-18T12:26:21.984Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012sUhk8izJLhdnXtpu5LZbS`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1",
  "prompt": "Find any information about: 1) flash-linear-attention (fla) version, commit hash, or package version, 2) training configuration, software dependencies, 3) any model card or README content, 4) any config.json or requirements. Extract all technical details and version numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34db6bc3-e83e-4859-a49b-abdc8b7964b2",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2mpy9ZJU5S4gpVw3HF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4cd15cb-e3ac-45e5-8abb-dc404e3fbedb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3N19Zgtc2FqUK3AYdmCVE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 3793,
      "cache_read_input_tokens": 17508,
      "output_tokens": 628,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3793
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 628,
          "cache_read_input_tokens": 17508,
          "cache_creation_input_tokens": 3793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3793,
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

_source line 20 · 2026-05-18T12:26:22.070Z_

<details><summary>↩ Tool result · `toolu_01LZdF4AmpzDu1k29zabMaBB`</summary>

```text
# Software Dependencies and Installation Information

After thoroughly reviewing the entire paper, I found **minimal technical setup information**:

## Found References

1. **Library Mention**: The paper states models are "implemented using the [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) library" but provides **no version number, commit hash, or installation instructions**.

2. **GitHub URL**: Only one repository link appears: `https://github.com/fla-org/flash-linear-attention`

3. **No Dependency Details**: The paper contains **no pip install commands, requirements files, or environment specifications**.

4. **Training Framework**: The work uses "AdamW optimizer with a cosine learning rate schedule" but doesn't specify which framework (PyTorch, etc.) or versions.

5. **Dataset Reference**: Mentions "fineweb-edu" dataset but without specific version or access instructions.

## Key Limitation

The authors note: "Our model training and inference are both implemented using the flash-linear-attention library" but unfortunately do not include reproducibility details such as specific versions, dependency lists, or setup procedures in this document.

For implementation details, readers would need to consult the linked GitHub repository or contact the authors directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "903b83a4-8378-4eb4-bb20-228d7c434318",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "44378d9a-2ad7-4bac-a78c-c3848f00548e",
  "sourceToolAssistantUUID": "903b83a4-8378-4eb4-bb20-228d7c434318",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T12:26:23.169Z_

<details><summary>↩ Tool result · `toolu_011L9tTfi4i7PzZCkWRWcy26`</summary>

```text
# Analysis of Available Technical Information

Based on the provided web page content, **very limited technical details are available**. Here's what can be extracted:

## Available Information

### Model Metadata
- **Model Name**: `m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1`
- **Organization**: Multimodal Art Projection (m-a-p)
- **Model Size**: 1B params
- **Tensor Type**: F32
- **Format**: Safetensors
- **Downloads (last month)**: 14

### Associated Collection
- **Collection**: "Hybrid Linear Attention Research"
- **Description**: "All 1.3B & 340M hybrid linear-attention experiments"
- **Items**: 62
- **Updated**: Sep 11, 2025

## Missing Information

❌ **No config.json contents** - Not displayed on page  
❌ **No README or model card** - Page explicitly states "No model card"  
❌ **No flash-linear-attention (fla) version/commit hash** - Not provided  
❌ **No training configuration details** - Not available  
❌ **No software dependencies/requirements** - Not specified  
❌ **No package versions** - Not listed  

## Recommendation

To access the complete technical specifications, you would need to:
1. Visit the model's [Files section](https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/tree/main)
2. Download and review the `config.json` file directly
3. Check for any README.md files in the repository
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b461ee1-c30e-4090-be91-0918e69135b7",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "01bc3e7a-65d8-410a-a01d-c46fe2fea5ac",
  "sourceToolAssistantUUID": "4b461ee1-c30e-4090-be91-0918e69135b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T12:26:24.832Z_

<details><summary>↩ Tool result · `toolu_01TXFy8V8qtAGPekWKiLZWuh`</summary>

```text
# Files in the Model Repository

Based on the web page content, here are **ALL files** listed in this model repository:

1. **.gitattributes** (1.52 kB)
2. **config.json** (1.16 kB) ✓
3. **generation_config.json** (111 Bytes)
4. **model-00001-of-00002.safetensors** (4.99 GB)
5. **model-00002-of-00002.safetensors** (606 MB)
6. **model.safetensors.index.json** (29.1 kB)
7. **special_tokens_map.json** (414 Bytes)
8. **tokenizer.json** (3.51 MB)
9. **tokenizer_config.json** (1.03 kB)

## Key Findings:

- **config.json** is present (1.16 kB) - likely contains model architecture and dependency information
- **No requirements.txt** file is listed
- **No README.md** file is visible in the provided content
- **No flash-linear-attention version info** is shown in the file listing

To find version information about dependencies like flash-linear-attention, you would need to examine the **config.json** file directly, as it's the most likely location for such metadata in this model repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34db6bc3-e83e-4859-a49b-abdc8b7964b2",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "cec1942c-10ad-4ed6-92b9-355ac14fbd16",
  "sourceToolAssistantUUID": "34db6bc3-e83e-4859-a49b-abdc8b7964b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T12:26:25.546Z_

<details><summary>↩ Tool result · `toolu_012sUhk8izJLhdnXtpu5LZbS`</summary>

```text
# Technical Details Analysis

Based on the provided web page content, here's what I found:

## Available Information:

1. **Model Specifications:**
   - Model size: 0.4B params
   - Tensor type: F32
   - Format: Safetensors
   - Architecture: gated_deltanet (hybrid linear-attention based)

2. **Model Identity:**
   - Model name: `340M-20B-GatedDeltaNet-New-hybrid-24-1`
   - Organization: m-a-p (Multimodal Art Projection)
   - HuggingFace URL: `/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1`

## Missing Information:

❌ **No model card or README content** - The page explicitly states "No model card"

❌ **Flash-Linear-Attention (FLA) version** - Not mentioned in the provided content

❌ **Commit hash** - Not visible in this page excerpt

❌ **Training configuration** - Not documented

❌ **Software dependencies/requirements** - Not specified

❌ **config.json details** - Not shown

❌ **Package versions** - Not provided

## Recommendation:

To obtain complete technical details, you would need to:
1. Visit the full model repository page directly
2. Check the "Files and versions" section (linked as `/tree/main`)
3. Look for `config.json`, `requirements.txt`, or `README.md` files in the repository
4. Review the model card section which appears to be empty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4cd15cb-e3ac-45e5-8abb-dc404e3fbedb",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "9cf7701a-02be-4c8d-94a7-b9529e07ef9c",
  "sourceToolAssistantUUID": "a4cd15cb-e3ac-45e5-8abb-dc404e3fbedb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-18T12:26:28.967Z_

Let me now fetch the config.json files directly and also check the GitHub repo for version tags.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cf7701a-02be-4c8d-94a7-b9529e07ef9c",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2nwKfS8sb1uCpee2bn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6d0dca2-a456-4768-98e3-5d9274124583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5crpUb7WaCLpWtyTjG5Tz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3138,
      "cache_read_input_tokens": 21301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3138,
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

_source line 25 · 2026-05-18T12:26:30.688Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U7b9LYGFyDRQXZUQzJZZUL`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1/raw/main/config.json",
  "prompt": "Show the COMPLETE contents of this config.json file. I need to see every field, especially any field related to: auto_map, transformers_version, fla version, or any version/library references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6d0dca2-a456-4768-98e3-5d9274124583",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2nwKfS8sb1uCpee2bn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c90292c2-ef73-497b-b075-5cdd848f0cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5crpUb7WaCLpWtyTjG5Tz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3138,
      "cache_read_input_tokens": 21301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3138,
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

_source line 26 · 2026-05-18T12:26:31.649Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sa9CwTLHzaGhTdRNGGWYyM`</summary>

```json
{
  "url": "https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1/raw/main/config.json",
  "prompt": "Show the COMPLETE contents of this config.json file. I need every field, especially auto_map, transformers_version, fla version, or any version/library references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c90292c2-ef73-497b-b075-5cdd848f0cbe",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2nwKfS8sb1uCpee2bn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "807718d9-d490-48de-90e0-e340b360f048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5crpUb7WaCLpWtyTjG5Tz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3138,
      "cache_read_input_tokens": 21301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3138,
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

_source line 27 · 2026-05-18T12:26:33.914Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XooVqU8UNj81Gq1UzK9mPy`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention",
  "prompt": "Find: 1) The latest release version or tag, 2) Any releases listed on the page, 3) The version number in setup.py or pyproject.toml if shown, 4) Recent commits or tags. List all version numbers visible on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807718d9-d490-48de-90e0-e340b360f048",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2nwKfS8sb1uCpee2bn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e5d875b-9234-4340-9535-8175f9166489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5crpUb7WaCLpWtyTjG5Tz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3138,
      "cache_read_input_tokens": 21301,
      "output_tokens": 491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 491,
          "cache_read_input_tokens": 21301,
          "cache_creation_input_tokens": 3138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3138,
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

_source line 28 · 2026-05-18T12:26:33.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019e13KRFqdoDo4CZFGXKPZi`</summary>

```json
{
  "query": "\"flash-linear-attention\" \"fla\" version pypi pip install site:github.com/fla-org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e5d875b-9234-4340-9535-8175f9166489",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2nwKfS8sb1uCpee2bn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f04c5ba-b098-4fec-b1df-5b21688d314b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5crpUb7WaCLpWtyTjG5Tz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3138,
      "cache_read_input_tokens": 21301,
      "output_tokens": 491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 491,
          "cache_read_input_tokens": 21301,
          "cache_creation_input_tokens": 3138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3138,
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

_source line 29 · 2026-05-18T12:26:34.995Z_

<details><summary>↩ Tool result · `toolu_01U7b9LYGFyDRQXZUQzJZZUL`</summary>

````text
# Complete Config.json Contents

Here is the **complete and entire** contents of the config.json file:

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_1.3B_3.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      2,
      5,
      8,
      11,
      14,
      17,
      20,
      23
    ],
    "num_heads": 16,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 8,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

## Key Findings:

**Version/Library References Found:**
- **`transformers_version`**: `"4.49.0"` ✓

**NOT Present in this config:**
- `auto_map` - **Not included**
- `fla_version` - **Not included**
- Any other library/framework version references

This is a **GatedDeltaNet** 1.3B parameter model configuration with 24 hidden layers, using hybrid attention-convolution architecture with gating mechanisms.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c90292c2-ef73-497b-b075-5cdd848f0cbe",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "6c06d90f-4136-4a3d-806b-53f6378f43a0",
  "sourceToolAssistantUUID": "c90292c2-ef73-497b-b075-5cdd848f0cbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T12:26:35.274Z_

<details><summary>↩ Tool result · `toolu_01Sa9CwTLHzaGhTdRNGGWYyM`</summary>

````text
# Complete Config.json Contents

Here is the **complete and exhaustive** contents of the configuration file:

```json
{
  "_name_or_path": "/mnt/bn/ridger1/flame/configs/GatedDeltaNet/gated_deltanet_340M_24.json",
  "architectures": [
    "GatedDeltaNetForCausalLM"
  ],
  "attn": {
    "layers": [
      23
    ],
    "num_heads": 32,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  },
  "attn_mode": "chunk",
  "bos_token_id": 1,
  "conv_size": 4,
  "eos_token_id": 2,
  "expand_k": 1,
  "expand_v": 1,
  "fuse_cross_entropy": true,
  "fuse_norm": true,
  "fuse_swiglu": true,
  "head_dim": 256,
  "hidden_act": "swish",
  "hidden_ratio": 4,
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": null,
  "max_position_embeddings": 2048,
  "model_type": "gated_deltanet",
  "norm_eps": 1e-06,
  "norm_first": false,
  "num_heads": 4,
  "num_hidden_layers": 24,
  "qk_activation": "silu",
  "qk_norm": "l2",
  "tie_word_embeddings": false,
  "torch_dtype": "float32",
  "transformers_version": "4.49.0",
  "use_beta": true,
  "use_cache": true,
  "use_gate": true,
  "use_output_norm": true,
  "use_short_conv": true,
  "vocab_size": 32000
}
```

## Key Version/Library References Found:
- **transformers_version**: `4.49.0`
- **torch_dtype**: `float32`
- **No auto_map field** present in this configuration
- **No fla_version field** present in this configuration

The config contains **31 fields total**. There are no additional version or library references beyond what is listed above.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "807718d9-d490-48de-90e0-e340b360f048",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "bb8ff09e-b052-44a6-b199-f74ea4531111",
  "sourceToolAssistantUUID": "807718d9-d490-48de-90e0-e340b360f048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T12:26:38.425Z_

<details><summary>↩ Tool result · `toolu_01XooVqU8UNj81Gq1UzK9mPy`</summary>

```text
# Version Information from Flash Linear Attention Repository

## Latest Release
The latest release version is **v0.5.0**, dated April 21, 2026.

## All Listed Releases
The page indicates there are **13 total releases** available, with v0.5.0 being the most recent.

## Version Numbers Found

1. **v0.5.0** (Latest - April 21, 2026)
2. **v0.3.2** (mentioned in installation notes as a milestone for package split)
3. **v0.1** (mentioned in news section from May 2024)

## Additional Technical Requirements
The documentation specifies minimum dependencies including "PyTorch >= 2.7.0" and "Triton >= 3.3," though these are not release versions for the FLA project itself.

The page notes that 12 additional releases exist beyond v0.5.0, though specific version numbers for those earlier releases are not displayed in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e5d875b-9234-4340-9535-8175f9166489",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "ce3b694c-738a-45d0-870d-4a9f96bac167",
  "sourceToolAssistantUUID": "9e5d875b-9234-4340-9535-8175f9166489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T12:26:39.897Z_

<details><summary>↩ Tool result · `toolu_019e13KRFqdoDo4CZFGXKPZi`</summary>

```text
Web search results for query: ""flash-linear-attention" "fla" version pypi pip install site:github.com/fla-org"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/README.md"},{"title":"GitHub - fla-org/flash-bidirectional-linear-attention: Triton implement of bi-directional (non-causal) linear attention · GitHub","url":"https://github.com/fla-org/flash-bidirectional-linear-attention"},{"title":"GitHub - fla-org/flame: 🔥 A minimal training framework for scaling FLA models","url":"https://github.com/fla-org/flame"},{"title":"flash-linear-attention/setup.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/setup.py"},{"title":"flash-linear-attention/examples/training.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/examples/training.md"},{"title":"GitHub - fla-org/fla-zoo: Flash-Linear-Attention models beyond language · GitHub","url":"https://github.com/fla-org/fla-zoo"},{"title":"flash-linear-attention/fla/layers/linear_attn.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/linear_attn.py"},{"title":"flash-linear-attention/pyproject.toml at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/pyproject.toml"}]

Based on the search results, here's the information about flash-linear-attention (FLA):

## Installation

You can install fla with pip: `pip install flash-linear-attention`. Alternatively, for the latest features and updates, you can install the package from source.

## Package Structure

Starting from v0.3.2, the packages published on PyPI are fla-core and flash-linear-attention. The former contains all customized kernels and only depends on PyTorch, Triton, and einops. The latter is an extension package of the former, containing fla/layers and fla/models, and depends on transformers.

## Requirements

The package requires Python >=3.10 and has dependencies on torch>=2.5, transformers>=4.45.0, datasets>=3.3.0, einops, and ninja.

## Installation from Source

If you want the latest development version, you can uninstall both packages first to ensure a successful upgrade and then use: `pip install -U --no-use-pep517 git+https://github.com/fla-org/flash-linear-attention --no-deps`.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f04c5ba-b098-4fec-b1df-5b21688d314b",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "11e92aec-cd21-418f-992e-82f41f375a34",
  "sourceToolAssistantUUID": "3f04c5ba-b098-4fec-b1df-5b21688d314b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-18T12:26:44.545Z_

Now let me check the GitHub releases page and also the flame training framework (referenced in the config path) to see if there's version pinning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11e92aec-cd21-418f-992e-82f41f375a34",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2ozfMrHRL1v91P95V5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24414183-d8da-4097-90bd-5a4891869992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVvkh3vCeGHSix5NRBEJtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2987,
      "cache_read_input_tokens": 24439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2987,
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

_source line 34 · 2026-05-18T12:26:46.423Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016TDGXGPnP43eL9kjwGXqrp`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases",
  "prompt": "List ALL release versions with their dates. I need to find which version would have been current around March-June 2025 when the m-a-p models were trained. List every release tag and date visible on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24414183-d8da-4097-90bd-5a4891869992",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2ozfMrHRL1v91P95V5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b42ed93-9d61-4883-aa0c-d01ff0825f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVvkh3vCeGHSix5NRBEJtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2987,
      "cache_read_input_tokens": 24439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2987,
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

_source line 35 · 2026-05-18T12:26:47.831Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018FCvmBvJLEJAgLxqBPLXtk`</summary>

```json
{
  "url": "https://github.com/fla-org/flame",
  "prompt": "Find: 1) Any requirements.txt, setup.py, or pyproject.toml that pins the flash-linear-attention version, 2) Any mention of fla version requirements, 3) Installation instructions that specify a version. Look for dependency specifications."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b42ed93-9d61-4883-aa0c-d01ff0825f48",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2ozfMrHRL1v91P95V5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3edc8d6f-fd86-415a-863c-c4e53b55aa5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVvkh3vCeGHSix5NRBEJtv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2987,
      "cache_read_input_tokens": 24439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2987,
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

_source line 36 · 2026-05-18T12:26:48.950Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D49MtvmcSQRgvLnZXTTnM8`</summary>

```json
{
  "query": "arxiv 2507.06457 \"systematic analysis hybrid linear attention\" Wang flash-linear-attention version code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3edc8d6f-fd86-415a-863c-c4e53b55aa5a",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2ozfMrHRL1v91P95V5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3b3628f-243a-400d-acc2-a49b0bfa4269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVvkh3vCeGHSix5NRBEJtv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2987,
      "cache_read_input_tokens": 24439,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 341,
          "cache_read_input_tokens": 24439,
          "cache_creation_input_tokens": 2987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2987,
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

_source line 37 · 2026-05-18T12:26:50.124Z_

<details><summary>↩ Tool result · `toolu_016TDGXGPnP43eL9kjwGXqrp`</summary>

```text
# Flash-Linear-Attention Release Versions and Dates

Based on the GitHub releases page, here are all visible release versions with their dates:

1. **v0.5.0** - April 21, 2025
2. **v0.4.2** - March 12, 2025
3. **v0.4.1** - December 24, 2024
4. **v0.4.0** - October 27, 2024
5. **v0.3.2** - September 10, 2024
6. **v0.3.1** - August 26, 2024
7. **v0.3.0** - July 14, 2024
8. **v0.2.2** - June 5, 2024
9. **v0.2.1** - April 23, 2024
10. **v0.2.0** - April 11, 2024

## For March-June 2025 Training Timeline

If the m-a-p models were trained during March-June 2025, the current versions would have been:
- **v0.4.2** (March 12, 2025) through **v0.5.0** (April 21, 2025)

The v0.5.0 release represents "the main new model this release is MoBA / FlashMoBA" and introduces multi-backend support moving beyond Triton-only infrastructure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b42ed93-9d61-4883-aa0c-d01ff0825f48",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "63d4f3ba-0fb0-44f1-9c17-fe699a14d118",
  "sourceToolAssistantUUID": "7b42ed93-9d61-4883-aa0c-d01ff0825f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T12:26:53.077Z_

<details><summary>↩ Tool result · `toolu_018FCvmBvJLEJAgLxqBPLXtk`</summary>

```text
# Flash-Linear-Attention Version Requirements

Based on the GitHub repository content, here are the relevant dependency specifications:

## Installation Instructions

The setup guide includes this specific instruction:

> "pip uninstall flash-linear-attention && pip install -U --no-use-pep517 git+https://github.com/fla-org/flash-linear-attention"

This command installs the latest development version from the GitHub repository without pinning to a specific release version.

## Related Dependencies

The framework also requires a specific torchtitan version:

> "pip install git+https://github.com/pytorch/torchtitan.git@0b44d4c"

## Additional Notes

- No explicit version pin (like `flash-linear-attention==X.Y.Z`) appears in the provided content
- The installation uses the `-U` flag to upgrade to the newest available version
- The `--no-use-pep517` flag suggests building directly from source
- While `pyproject.toml` and `setup.py` files are mentioned in the repository structure, their specific contents are not shown in the provided material

The developers recommend using recent versions: **torch>=2.6** and **triton>=3.0** for optimal compatibility with torch.compile features.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3edc8d6f-fd86-415a-863c-c4e53b55aa5a",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "fa6f72f0-10c3-4e5b-93b6-a3009051b0f0",
  "sourceToolAssistantUUID": "3edc8d6f-fd86-415a-863c-c4e53b55aa5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T12:27:01.652Z_

<details><summary>↩ Tool result · `toolu_01D49MtvmcSQRgvLnZXTTnM8`</summary>

```text
Web search results for query: "arxiv 2507.06457 "systematic analysis hybrid linear attention" Wang flash-linear-attention version code github"

Links: [{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"[PDF] A Systematic Analysis of Hybrid Linear Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Systematic-Analysis-of-Hybrid-Linear-Attention-Wang-Zhu/f7ad9ebc481e23ae7fa90d98d3814518e94adcd1"},{"title":"(PDF) A Systematic Analysis of Hybrid Linear Attention","url":"https://www.researchgate.net/publication/393538945_A_Systematic_Analysis_of_Hybrid_Linear_Attention"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"A Systematic Analysis of Hybrid Linear Attention | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/systematic-analysis-hybrid-linear-attention"},{"title":"Alphaxiv","url":"https://www.alphaxiv.org/overview/2507.06457v1"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation ...","url":"https://arxiv.org/pdf/2601.22156"},{"title":"Hybrid Architectures for Language Models: Systematic Analysis and Design Insights","url":"https://arxiv.org/html/2510.04800v1"}]

Now let me search for the GitHub code repository related to this paper:

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact attention · GitHub","url":"https://github.com/Dao-AILab/flash-attention"},{"title":"flash-linear-attention/examples/training.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/examples/training.md"},{"title":"flash-linear-attention/fla/layers/based.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/based.py"},{"title":"GitHub - fla-org/flash-bidirectional-linear-attention: Triton implement of bi-directional (non-causal) linear attention · GitHub","url":"https://github.com/fla-org/flash-bidirectional-linear-attention"},{"title":"flash-linear-attention/fla/layers/rebased.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/rebased.py"},{"title":"flash-linear-attention/fla/layers/gla.py at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/fla/layers/gla.py"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"}]

Let me search more specifically for the Wang et al. paper code and models:

Links: [{"title":"Undergraduate alumni Dustin Wang and PhD Students Rui-Jie Zhu and Taylor Kergan submit a preprint titled, “A Systematic Analysis of Hybrid Linear Attention” | Neuromorphic Computing Group","url":"https://ncg.ucsc.edu/2025/07/08/undergraduate-alumni-dustin-wang-and-phd-students-rui-jie-zhu-and-taylor-kergan-submit-a-preprint-titled-a-systematic-analysis-of-hybrid-linear-attention/"},{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"[2507.06457v1] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457v1"},{"title":"Rui-Jie Zhu","url":"https://www.catalyzex.com/author/Rui-Jie%20Zhu"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"[PDF] A Systematic Analysis of Hybrid Linear Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Systematic-Analysis-of-Hybrid-Linear-Attention-Wang-Zhu/f7ad9ebc481e23ae7fa90d98d3814518e94adcd1"},{"title":"Paper page - A Systematic Analysis of Hybrid Linear Attention","url":"https://huggingface.co/papers/2507.06457"},{"title":"Rui-Jie Zhu's research works | University of California, Santa Cruz and other places","url":"https://www.researchgate.net/scientific-contributions/Rui-Jie-Zhu-2218187817"}]

Based on my search results, here's what I found about the arXiv paper 2507.06457:

## Paper Overview

The paper "A Systematic Analysis of Hybrid Linear Attention" was authored by Dustin Wang and 10 other authors, submitted on July 8, 2025.

## Research Content

The paper addresses how Transformers face quadratic complexity and memory issues with long sequences, prompting the adoption of linear attention mechanisms using fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers. Despite extensive hybrid architecture research, the choice of linear attention component has not been deeply explored.

The researchers trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

## Key Findings

While language modeling remains stable across linear-to-full attention ratios, recall significantly improves with increased full attention layers, particularly below a 3:1 ratio. The study highlights selective gating, hierarchical recurrence, and controlled forgetting as critical for effective hybrid models. The authors recommend architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently.

## Code and Models

The paper notes that their model training and inference are both implemented using the flash-linear-attention library. The trained models are open-sourced at https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e. The main code repository for flash-linear-attention can be found at https://github.com/fla-org/flash-linear-attention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3b3628f-243a-400d-acc2-a49b0bfa4269",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "58ac3d34-b67e-4e3e-8070-d32afe50a80a",
  "sourceToolAssistantUUID": "e3b3628f-243a-400d-acc2-a49b0bfa4269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-18T12:27:04.863Z_

Let me try a few more targeted approaches - checking the flame training framework's requirements and the HuggingFace papers page for discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58ac3d34-b67e-4e3e-8070-d32afe50a80a",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2qc1tcSRwcJaKi2Rid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6536618c-7a7d-4f4a-9b47-283c0ddfde18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPVLi4EV926VxiuCtY7n8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 27426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3018,
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

_source line 41 · 2026-05-18T12:27:05.833Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U9ciQ7Qr4f3AKfZwiAfv3E`</summary>

```json
{
  "url": "https://github.com/fla-org/flame/blob/main/pyproject.toml",
  "prompt": "Show the COMPLETE contents of this pyproject.toml. I need to see all dependency specifications, especially any flash-linear-attention or fla version pins."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6536618c-7a7d-4f4a-9b47-283c0ddfde18",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2qc1tcSRwcJaKi2Rid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbb6ab4b-2e94-4c75-9e10-7bca66459718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPVLi4EV926VxiuCtY7n8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 27426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3018,
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

_source line 42 · 2026-05-18T12:27:07.266Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nx4h9kyXz4ELf6tJzTqbja`</summary>

```json
{
  "url": "https://huggingface.co/papers/2507.06457",
  "prompt": "Find any discussion comments, author responses, or additional information about the paper. Look for any mention of flash-linear-attention version, code repository, or implementation details shared in comments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbb6ab4b-2e94-4c75-9e10-7bca66459718",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2qc1tcSRwcJaKi2Rid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "872b19e3-ecb2-4e5a-86d6-3a1b7ef0a36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPVLi4EV926VxiuCtY7n8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 27426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3018,
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

_source line 43 · 2026-05-18T12:27:07.750Z_

<details><summary>↩ Tool result · `toolu_01Nx4h9kyXz4ELf6tJzTqbja`</summary>

```text
&lt;persisted-output>
Output too large (63.9KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt

Preview (first 2KB):
Title: A Systematic Analysis of Hybrid Linear Attention

URL Source: https://arxiv.org/html/2507.06457

Markdown Content:
1]UC Santa Cruz 2]ByteDance Seed 3]University of Groningen 4]CASIA 5]PolyU 6]M-A-P \contribution[*]Equal Contribution \contribution[†]Corresponding authors

Rui-Jie Zhu 

Steven Abreu Yong Shan Taylor Kergan Yuqi Pan Yuhong Chou Zheng Li Ge Zhang Wenhao Huang Jason Eshraghian [ [ [ [ [ [ [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)[jsn@ucsc.edu](mailto:jsn@ucsc.edu)

(July 8, 2025)

###### Abstract

Transformers face quadratic complexity and memory issues with long sequences, prompting the adoption of linear attention mechanisms using fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers. Despite extensive hybrid architecture research, the choice of linear attention component has not been deeply explored. We systematically evaluate various linear attention models across generations—vector recurrences to advanced gating mechanisms—both standalone and hybridized. To enable this comprehensive analysis, we trained and open-sourced 72 models***Our model training and inference are both implemented using the [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) library.: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios. Benchmarking on standard language modeling and recall tasks reveals that superior standalone linear models do not necessarily excel in hybrids. While language modeling remains stable across linear-to-full attention ratios, recall significantly improves with increased full attention layers, particularly below a 3:1 ratio. Our study highlights selective gating, hierarchical recurrence, and controlled forgetting as critical for effective hybrid models. We recommend architectures such as H
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "872b19e3-ecb2-4e5a-86d6-3a1b7ef0a36b",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "57bf8ff5-0236-44bd-91b3-42e269261022",
  "sourceToolAssistantUUID": "872b19e3-ecb2-4e5a-86d6-3a1b7ef0a36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T12:27:08.173Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01156gBdX5KgxVLKtnr9aKs1`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/setup.py",
  "prompt": "Show the COMPLETE contents of setup.py. I need the version number defined in this file."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57bf8ff5-0236-44bd-91b3-42e269261022",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2qc1tcSRwcJaKi2Rid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f5a7683-3c54-4052-9bbb-b45c7559cdad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPVLi4EV926VxiuCtY7n8h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 27426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3018,
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

_source line 45 · 2026-05-18T12:27:09.156Z_

<details><summary>↩ Tool result · `toolu_01U9ciQ7Qr4f3AKfZwiAfv3E`</summary>

````text
# FLAME pyproject.toml Contents

Based on the GitHub page content provided, here is the complete pyproject.toml file:

```toml
[project]
name = "flame"
dynamic = ["version"]
description = "A minimal training framework for scaling FLA models"
readme = "README.md"
authors = [
{ name = "Songlin Yang", email = "yangsl66@mit.edu" },
{ name = "Yu Zhang", email = "yzhang.cs@outlook.com" },
]
license = { file = "LICENSE" }
classifiers = [
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
"Topic :: Scientific/Engineering :: Artificial Intelligence",
]
requires-python = ">=3.10"
dependencies = [
'flash-linear-attention',
'torch>=2.5',
'torchdata',
'transformers>=4.45.0',
'triton>=3.0',
'datasets>=3.3.0',
'einops',
'ninja',
'wandb',
'tiktoken',
'tensorboard',
]

[project.optional-dependencies]
dev = ["pytest"]

[project.urls]
Homepage = "https://github.com/fla-org/flame"

[build-system]
requires = ["setuptools>=45", "wheel", "ninja", "torch"]

[tool.isort]
line_length = 127
multi_line_output = 3
```

**Key Finding:** The `flash-linear-attention` dependency has **no version pin specified**—it will install the latest available version.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbb6ab4b-2e94-4c75-9e10-7bca66459718",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "891fc094-dbab-46c1-b0da-60574499da18",
  "sourceToolAssistantUUID": "fbb6ab4b-2e94-4c75-9e10-7bca66459718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T12:27:09.269Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RzfSzGSU26S5FuC1aJdLup`</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/",
  "prompt": "List ALL release versions with dates available on PyPI. I need the complete version history to determine which version was current in early 2025."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "891fc094-dbab-46c1-b0da-60574499da18",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2qc1tcSRwcJaKi2Rid",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "889b87f8-dac3-4a7e-8586-260f8befde9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TPVLi4EV926VxiuCtY7n8h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3018,
      "cache_read_input_tokens": 27426,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 27426,
          "cache_creation_input_tokens": 3018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3018,
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

_source line 47 · 2026-05-18T12:27:11.053Z_

<details><summary>↩ Tool result · `toolu_01156gBdX5KgxVLKtnr9aKs1`</summary>

````text
# Setup.py Contents

The setup.py file shown is complete. However, **the actual version number is not hardcoded in this file**. Instead, it's dynamically retrieved from the package's `__init__.py`:

```python
def get_package_version():
    init_file = Path(os.path.dirname(os.path.abspath(__file__))) / 'fla' / '__init__.py'
    with open(init_file) as f:
        version_match = re.search(r"^__version__\s*=\s*(.*)", f.read(), re.MULTILINE)
```

The version is "extracted from the `fla/__init__.py` file at package initialization time." To find the actual version number, you would need to check that `__init__.py` file, which is not displayed in the provided content.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f5a7683-3c54-4052-9bbb-b45c7559cdad",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "b1c05917-cb41-4657-9f84-0d864f9858cc",
  "sourceToolAssistantUUID": "5f5a7683-3c54-4052-9bbb-b45c7559cdad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T12:27:13.128Z_

<details><summary>↩ Tool result · `toolu_01RzfSzGSU26S5FuC1aJdLup`</summary>

```text
# Flash Linear Attention Release History

Based on the PyPI page, here is the complete version history with release dates:

| Version | Release Date |
|---------|--------------|
| 0.5.0 | Apr 21, 2026 |
| 0.4.2 | Mar 12, 2026 |
| 0.4.1 | Dec 24, 2025 |
| 0.4.0 | Oct 27, 2025 |
| 0.3.2 | Sep 10, 2025 |
| 0.3.1 | Aug 26, 2025 |
| 0.3.0 | Jul 14, 2025 |
| 0.2.2 | Jun 5, 2025 |
| 0.2.1 | Apr 23, 2025 |
| 0.2.0 | Apr 11, 2025 |
| 0.1.2 | Mar 31, 2025 |
| 0.1.1 | Mar 24, 2025 |
| 0.1 | Mar 20, 2025 |

## Early 2025 Status

In early 2025 (January-February), version 0.1 would have been the current release, having launched on March 20, 2025. The package was in its initial stages, offering "a collection of implementations for state-of-the-art linear attention models."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "889b87f8-dac3-4a7e-8586-260f8befde9d",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "3847fc13-ce4e-4238-89ff-5d1a831ee148",
  "sourceToolAssistantUUID": "889b87f8-dac3-4a7e-8586-260f8befde9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-18T12:27:17.012Z_

Let me now read the full paper HTML for any specific version mentions, and also check the actual `__init__.py` for what version was tagged at the relevant commit dates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3847fc13-ce4e-4238-89ff-5d1a831ee148",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2rShaznjskS23fUq7A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7306d003-6058-476f-90e9-a90e6c65c44d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKZjwKFBxZxZ1U1ohHV7oS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2231,
      "cache_read_input_tokens": 30444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2231,
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

_source line 50 · 2026-05-18T12:27:18.148Z_

<details open><summary>🔧 Tool call — Read · `toolu_018G1wmdbTUGuSYYLn8krZFN`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7306d003-6058-476f-90e9-a90e6c65c44d",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2rShaznjskS23fUq7A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81b8c811-9e7b-4642-a39a-142edff457b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKZjwKFBxZxZ1U1ohHV7oS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2231,
      "cache_read_input_tokens": 30444,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2231
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 30444,
          "cache_creation_input_tokens": 2231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2231,
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

_source line 51 · 2026-05-18T12:27:18.400Z_

<details><summary>↩ Tool result · `toolu_018G1wmdbTUGuSYYLn8krZFN`</summary>

```text
0	Title: A Systematic Analysis of Hybrid Linear Attention
1	
2	URL Source: https://arxiv.org/html/2507.06457
3	
4	Markdown Content:
5	1]UC Santa Cruz 2]ByteDance Seed 3]University of Groningen 4]CASIA 5]PolyU 6]M-A-P \contribution[*]Equal Contribution \contribution[†]Corresponding authors
6	
7	Rui-Jie Zhu 
8	
9	Steven Abreu Yong Shan Taylor Kergan Yuqi Pan Yuhong Chou Zheng Li Ge Zhang Wenhao Huang Jason Eshraghian [ [ [ [ [ [ [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)[jsn@ucsc.edu](mailto:jsn@ucsc.edu)
10	
11	(July 8, 2025)
12	
13	###### Abstract
14	
15	Transformers face quadratic complexity and memory issues with long sequences, prompting the adoption of linear attention mechanisms using fixed-size hidden states. However, linear models often suffer from limited recall performance, leading to hybrid architectures that combine linear and full attention layers. Despite extensive hybrid architecture research, the choice of linear attention component has not been deeply explored. We systematically evaluate various linear attention models across generations—vector recurrences to advanced gating mechanisms—both standalone and hybridized. To enable this comprehensive analysis, we trained and open-sourced 72 models***Our model training and inference are both implemented using the [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) library.: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios. Benchmarking on standard language modeling and recall tasks reveals that superior standalone linear models do not necessarily excel in hybrids. While language modeling remains stable across linear-to-full attention ratios, recall significantly improves with increased full attention layers, particularly below a 3:1 ratio. Our study highlights selective gating, hierarchical recurrence, and controlled forgetting as critical for effective hybrid models. We recommend architectures such as HGRN-2 or GatedDeltaNet with a linear-to-full ratio between 3:1 and 6:1 to achieve Transformer-level recall efficiently.
16	
17	\correspondence
18	
19	Ge Zhang at , Jason Eshraghian at \checkdata[Opensourced Models][Page](https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e)
20	
21	1 Introduction
22	--------------
23	
24	The Transformer architecture [[1](https://arxiv.org/html/2507.06457v1#bib.bib1)] has become the dominant network design for Large Language Models (LLMs). However, its quadratic complexity in sequence length for a single forward pass, O⁢(L 2)𝑂 superscript 𝐿 2 O(L^{2})italic_O ( italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ), and the linearly growing Key-Value (KV) cache in full attention mechanisms [[1](https://arxiv.org/html/2507.06457v1#bib.bib1)], become problematic as sequences lengthen. To address this, numerous alternative approaches have emerged, with linear complexity models representing one of the most promising directions [[2](https://arxiv.org/html/2507.06457v1#bib.bib2)]. These models compress the linearly growing KV cache into a static vector or matrix—a hidden state—thereby achieving O⁢(L)𝑂 𝐿 O(L)italic_O ( italic_L ) overall complexity [[2](https://arxiv.org/html/2507.06457v1#bib.bib2)]. This innovation tackles both the quadratic complexity problem and the issue of an expanding KV cache.
25	
26	To better utilize these fixed hidden states, linear complexity models have evolved through roughly three generations. The first generation was characterized by vector-level hidden states derived from traditional Recurrent Neural Networks (RNNs)[[3](https://arxiv.org/html/2507.06457v1#bib.bib3)]. The second generation advanced this by employing outer products for state expansion, creating 2D hidden states [[4](https://arxiv.org/html/2507.06457v1#bib.bib4)]. The third generation further refined these models by introducing delta rule state transitions [[5](https://arxiv.org/html/2507.06457v1#bib.bib5)], replacing the hidden state decay mechanisms used in the first two generations. Each successive generation has generally yielded improved performance in both common reasoning and retrieval benchmarks.
27	
28	Despite these advancements, the same fixed hidden state that enables linear complexity also introduces limitations in recall capabilities; linear attention models typically demonstrate poorer recall performance[[6](https://arxiv.org/html/2507.06457v1#bib.bib6), [7](https://arxiv.org/html/2507.06457v1#bib.bib7), [8](https://arxiv.org/html/2507.06457v1#bib.bib8)]. To mitigate this deficiency, Hybrid Linear Attention models have emerged[[9](https://arxiv.org/html/2507.06457v1#bib.bib9)]. This approach interleaves full attention layers with linear attention layers. Although the overall complexity remains quadratic due to the inclusion of full attention, these hybrid models deliver significantly better recall performance[[10](https://arxiv.org/html/2507.06457v1#bib.bib10), [11](https://arxiv.org/html/2507.06457v1#bib.bib11)] and have successfully scaled to 400 billion parameters while maintaining competitive common reasoning performance[[11](https://arxiv.org/html/2507.06457v1#bib.bib11)].
29	
30	However, a critical observation in the development of hybrid models is that while the choice of the full attention mechanism is generally consistent, the selection of the linear attention component appears relatively arbitrary. Existing research predominantly focuses on ablation studies concerning the ratio of full to linear attention layers, rather than on the specific architectural choices within the linear models themselves [[12](https://arxiv.org/html/2507.06457v1#bib.bib12), [10](https://arxiv.org/html/2507.06457v1#bib.bib10), [11](https://arxiv.org/html/2507.06457v1#bib.bib11), [13](https://arxiv.org/html/2507.06457v1#bib.bib13)]. These studies often implicitly assume that a superior standalone linear model will inherently lead to a better-performing hybrid model. We ask: is this assumption valid? Furthermore, the determination of the optimal ratio in hybrid models is frequently guided by minimizing loss values, which primarily reflects performance on short-text modeling tasks, potentially overlooking the more critical aspect of recall performance. Finally, Ref.[[14](https://arxiv.org/html/2507.06457v1#bib.bib14)] has demonstrated that simply increasing the state size of linear attention models yields diminishing returns. Given this limitation, we hypothesize that performance improvements may instead depend on a model’s ability to effectively manage and retrieve information from its stored memory–a capability we examine through our language modeling and recall evaluations.
31	
32	In this work, we conduct a comprehensive investigation into a wide array of linear attention architectures spanning all three generations, analyzing their language modeling and recall performance when hybridized. We also benchmark pure linear attention models as a baseline and examine the impact of varying the ratio between full and linear attention layers. Our research aims to answer three primary questions: 1) Does a linear attention model with better standalone performance necessarily translate to a superior hybrid model architecture? 2) What aspects are more significantly influenced by the ratio of full to linear attention layers: overall language modeling (LM) performance or recall capabilities? 3) Which architectural components or design principles within linear attention models are most crucial for optimizing both LM performance and recall?
33	
34	This paper makes three primary contributions.
35	
36	1.   1.
37	We provide a comparative analysis of various linear attention architectures from all three recognized generations, evaluating both their standalone language modeling and their recall performance and also when integrated into hybrid models;
38	
39	2.   2.
40	We examine the assumption that improvements in standalone linear attention models directly correlate with enhanced performance in hybrid architectures, offering evidence-based insights into this relationship;
41	
42	3.   3.
43	our work analyzes how the ratio of full attention to linear attention layers in hybrid models distinctly affects overall language modeling capabilities versus specific recall performance, while also identifying key architectural components within linear attention models that are crucial for these metrics.
44	
45	2 Related work
46	--------------
47	
48	#### Linear complexity language models.
49	
50	Early efforts to tame the quadratic cost of softmax attention rewrote it as an associative recurrent update, giving linear attention with O⁢(L)𝑂 𝐿 O(L)italic_O ( italic_L ) compute and memory [[2](https://arxiv.org/html/2507.06457v1#bib.bib2)]. Subsequent fast-weight and kernel views improved stability and throughput [[15](https://arxiv.org/html/2507.06457v1#bib.bib15)]. A parallel line scales recurrent networks themselves: RWKV introduces a receptance-weighted key–value recurrence that matches Transformer perplexity while keeping a constant-size cache [[16](https://arxiv.org/html/2507.06457v1#bib.bib16)]; RetNet adds exponential decay for longer retention [[17](https://arxiv.org/html/2507.06457v1#bib.bib17)]; Mamba and its successor Mamba-2 treat input-conditioned state-space models as RNNs, closing most perplexity gaps on open benchmarks with linear-time generation [[18](https://arxiv.org/html/2507.06457v1#bib.bib18)]. Gated extensions (HGRN2, Gated DeltaNet) further refine selective forgetting with per-token gates [[4](https://arxiv.org/html/2507.06457v1#bib.bib4), [19](https://arxiv.org/html/2507.06457v1#bib.bib19)]. Despite these gains, purely linear/recurrent models still underperform Transformers on long-context retrieval and in-context learning [[20](https://arxiv.org/html/2507.06457v1#bib.bib20), [21](https://arxiv.org/html/2507.06457v1#bib.bib21), [22](https://arxiv.org/html/2507.06457v1#bib.bib22)], motivating hybrid designs. See Table [1](https://arxiv.org/html/2507.06457v1#S3.T1 "Table 1 ‣ 3.1 Linear Attention and its variants ‣ 3 Method ‣ A Systematic Analysis of Hybrid Linear Attention") for a more detailed overview of these models.
51	
52	#### Hybrid architectures.
53	
54	The dominant remedy is to interleave a small number of full-attention layers with many linear-time layers, yielding Transformer-like recall at a fraction of the KV-cache cost. Small-scale hybrid models include Hybrid-H3 [[23](https://arxiv.org/html/2507.06457v1#bib.bib23)] using only two attention layers with up to 2.7B parameters, StripedHyena [[13](https://arxiv.org/html/2507.06457v1#bib.bib13)] using a 1:1 ratio with 7B parameters, RecurrentGemma [[24](https://arxiv.org/html/2507.06457v1#bib.bib24)] using a 2:1 ratio and sliding window attention with 2B and 9B parameters, and Mamba-2-Hybrid [[20](https://arxiv.org/html/2507.06457v1#bib.bib20)] using a 4:1 ratio with 8B parameters. Large-scale demonstrations include Jamba (7:1 Mamba:Transformer) [[12](https://arxiv.org/html/2507.06457v1#bib.bib12), [9](https://arxiv.org/html/2507.06457v1#bib.bib9)] and production models at Character.ai and MiniMax that converge on a 6–7:1 ratio [[25](https://arxiv.org/html/2507.06457v1#bib.bib25), [11](https://arxiv.org/html/2507.06457v1#bib.bib11)]. Variants trade capacity for memory: Zamba shares a single global-attention block across many recurrent blocks [[26](https://arxiv.org/html/2507.06457v1#bib.bib26), [27](https://arxiv.org/html/2507.06457v1#bib.bib27)]; Samba keeps complexity strictly linear by pairing Mamba with sliding-window attention (SWA) [[28](https://arxiv.org/html/2507.06457v1#bib.bib28)]. Beyond block-wise mixing, _prefill–decode_ hybrids such as YOCO compress all keys during an O⁢(L)𝑂 𝐿 O(L)italic_O ( italic_L ) prefill pass and reuse them during decoding, slashing cache by ×\times×layer-count [[29](https://arxiv.org/html/2507.06457v1#bib.bib29), [30](https://arxiv.org/html/2507.06457v1#bib.bib30)]. A finer granularity is _head-wise_ mixing: Hymba allocates some attention heads to softmax and the rest to state-space updates within the same layer, halving cache while preserving accuracy [[10](https://arxiv.org/html/2507.06457v1#bib.bib10)]. Empirically, long-context quality rises steeply once a few full-attention blocks or heads are present, after which perplexity plateaus; thus the linear:full ratio primarily controls recall, whereas language modeling loss is comparatively insensitive.
55	
56	#### Principled hybrid architecture design
57	
58	While these empirical studies demonstrate the viability of hybrid approaches, recent work has sought more principled design methodologies. The STAR framework [[31](https://arxiv.org/html/2507.06457v1#bib.bib31)] uses a unified mathematical foundation for linear attention mechanisms to enable automated architecture synthesis through an evolutionary optimization method. Complementarily, Poli et al. [[32](https://arxiv.org/html/2507.06457v1#bib.bib32)] propose using synthetic tasks to isolate specific capabilities and understand component interactions, finding that optimal architectures leverage specialized layers through hybrid topology. These frameworks suggest that hybrid design can move beyond empirical ratio exploration toward more grounded optimization of component synergies.
59	
60	3 Method
61	--------
62	
63	### 3.1 Linear Attention and its variants
64	
65	Table 1: Unified comparison of linear-time attention mechanisms across three “generations”. 1st Gen keeps a vector 𝒉 t∈ℝ d subscript 𝒉 𝑡 superscript ℝ 𝑑{\bm{h}}_{t}\!\in\!\mathbb{R}^{d}bold_italic_h start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT with element-wise gating e.g.HGRN and Hawk, so the read-out is a Hadamard product (𝒉 t⊙𝒒 t direct-product subscript 𝒉 𝑡 subscript 𝒒 𝑡{\bm{h}}_{t}\odot{\bm{q}}_{t}bold_italic_h start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ⊙ bold_italic_q start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT). 2nd Gen stores a matrix 𝐒 t∈ℝ d×n subscript 𝐒 𝑡 superscript ℝ 𝑑 𝑛{\mathbf{S}}_{t}\!\in\!\mathbb{R}^{d\times n}bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_d × italic_n end_POSTSUPERSCRIPT via outer-product additions plus multiplicative decay, including GLA, RetNet, RWKV-6, HGRN-2 and Mamba. 3rd Gen introduces delta-rule controlled forgetting that explicitly erases stale content (DeltaNet family). 𝒗 t,𝒌 t,𝒒 t subscript 𝒗 𝑡 subscript 𝒌 𝑡 subscript 𝒒 𝑡{\bm{v}}_{t},{\bm{k}}_{t},{\bm{q}}_{t}bold_italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT , bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT , bold_italic_q start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT are value, key and query projections; 𝜶 t,β t,𝒓 t,𝒊 t subscript 𝜶 𝑡 subscript 𝛽 𝑡 subscript 𝒓 𝑡 subscript 𝒊 𝑡{\bm{\alpha}}_{t},\beta_{t},{\bm{r}}_{t},{\bm{i}}_{t}bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT , italic_β start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT , bold_italic_r start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT , bold_italic_i start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT are gates; ⊙direct-product\odot⊙ is the Hadamard product.
66	
67	This section formalizes the three generations of linear–time attention mechanisms that motivate our study and explains why we benchmark the specific representatives HGRN (first generation) and HGRN-2, GLA, RetNet (second generation). For each generation we summarize the core update rule, highlight the architectural property that distinguishes it from its predecessors, and discuss its implications for hybrid design. Table[1](https://arxiv.org/html/2507.06457v1#S3.T1 "Table 1 ‣ 3.1 Linear Attention and its variants ‣ 3 Method ‣ A Systematic Analysis of Hybrid Linear Attention") gives a unified algebraic view of the mechanisms introduced below.
68	
69	![Image 1: Refer to caption](https://arxiv.org/html/2507.06457v1/x1.png)
70	
71	Figure 1: Three ‘generations’ of linear-attention state updates. Generation 1 (left): Gated Vector Recurrence keeps a single vector h t∈ℝ d subscript ℎ 𝑡 superscript ℝ 𝑑 h_{t}\in\mathbb{R}^{d}italic_h start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT. Each step first decays the previous state by an element-wise gate α t subscript 𝛼 𝑡\alpha_{t}italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT (grey), then adds the gated input v t subscript 𝑣 𝑡 v_{t}italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT (pink). Update and memory are both O⁢(d)𝑂 𝑑 O(d)italic_O ( italic_d ). Generation 2 (centre): Outer-Product State with Decay stores a full matrix S t∈ℝ d×n subscript 𝑆 𝑡 superscript ℝ 𝑑 𝑛 S_{t}\in\mathbb{R}^{d\times n}italic_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_d × italic_n end_POSTSUPERSCRIPT. A diagonal decay mask (𝟏⁢α t⊤)1 superscript subscript 𝛼 𝑡 top(\mathbf{1}\,\alpha_{t}^{\!\top})( bold_1 italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT ) scales every column, after which a rank-1 outer product v t⁢k t⊤subscript 𝑣 𝑡 superscript subscript 𝑘 𝑡 top v_{t}k_{t}^{\!\top}italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT is written (pink/blue). Cost rises to O⁢(d 2)𝑂 superscript 𝑑 2 O(d^{2})italic_O ( italic_d start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ). Generation 3 (right): Δ Δ\Delta roman_Δ-Rule Controlled Forgetting first erases the slice of S t−1 subscript 𝑆 𝑡 1 S_{t-1}italic_S start_POSTSUBSCRIPT italic_t - 1 end_POSTSUBSCRIPT aligned with key k t subscript 𝑘 𝑡 k_{t}italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT using the projector I−β t⁢k t⁢k t⊤𝐼 subscript 𝛽 𝑡 subscript 𝑘 𝑡 superscript subscript 𝑘 𝑡 top I-\beta_{t}k_{t}k_{t}^{\!\top}italic_I - italic_β start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT (cells with 1 1 1 1), then writes the new outer product β t⁢v t⁢k t⊤subscript 𝛽 𝑡 subscript 𝑣 𝑡 superscript subscript 𝑘 𝑡 top\beta_{t}v_{t}k_{t}^{\!\top}italic_β start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT. This selective forget-then-write preserves capacity while matching the O⁢(d 2)𝑂 superscript 𝑑 2 O(d^{2})italic_O ( italic_d start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ) compute and memory of Generation 2. The arrow at the bottom emphasizes the historical progression from minimal to maximal recall capability.
72	
73	### 3.2 From vector recurrence to controlled forgetting
74	
75	#### Generation 1 – gated vector recurrence.
76	
77	Early linear models collapsed the per-token key–value cache into a single d 𝑑 d italic_d-dimensional vector that is updated additively and modulated by a learned gate. Formally, 𝒉 t=𝜶 t⊙𝒉 t−1+(1−𝜶 t)⊙𝒗 t,𝒐 t=𝒉 t⊙𝒒 t formulae-sequence subscript 𝒉 𝑡 direct-product subscript 𝜶 𝑡 subscript 𝒉 𝑡 1 direct-product 1 subscript 𝜶 𝑡 subscript 𝒗 𝑡 subscript 𝒐 𝑡 direct-product subscript 𝒉 𝑡 subscript 𝒒 𝑡{\bm{h}}_{t}={\bm{\alpha}}_{t}\odot{\bm{h}}_{t-1}+(1-{\bm{\alpha}}_{t})\odot{% \bm{v}}_{t},\;{\bm{o}}_{t}={\bm{h}}_{t}\odot{\bm{q}}_{t}bold_italic_h start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ⊙ bold_italic_h start_POSTSUBSCRIPT italic_t - 1 end_POSTSUBSCRIPT + ( 1 - bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ) ⊙ bold_italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT , bold_italic_o start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = bold_italic_h start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ⊙ bold_italic_q start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT (HGRN; ​ The element-wise gate 𝜶 t=f θ⁢(x 1:t)∈(0,1)d subscript 𝜶 𝑡 subscript 𝑓 𝜃 subscript 𝑥:1 𝑡 superscript 0 1 𝑑{\bm{\alpha}}_{t}=f_{\theta}(x_{1:t})\in(0,1)^{d}bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = italic_f start_POSTSUBSCRIPT italic_θ end_POSTSUBSCRIPT ( italic_x start_POSTSUBSCRIPT 1 : italic_t end_POSTSUBSCRIPT ) ∈ ( 0 , 1 ) start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT enables selective retention without the vanishing gradients that plagued classical RNNs, yet the scalar state vector still struggles to store multiple competing memories.
78	
79	#### Generation 2 – outer-product state with decay.
80	
81	To increase capacity, second-generation architectures promote the hidden state to a matrix 𝐒 t∈ℝ d×n subscript 𝐒 𝑡 superscript ℝ 𝑑 𝑛{\mathbf{S}}_{t}\in\mathbb{R}^{d\times n}bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_d × italic_n end_POSTSUPERSCRIPT, typically n=d 𝑛 𝑑 n=d italic_n = italic_d, accumulating rank-one outer products while applying a decay gate: 𝐒 t=𝐒 t−1⊙(𝟏⁢𝜶 t⊤)+𝒗 t⁢𝒌 t⊤,𝒐 t=𝐒 t⁢𝒒 t.formulae-sequence subscript 𝐒 𝑡 direct-product subscript 𝐒 𝑡 1 1 superscript subscript 𝜶 𝑡 top subscript 𝒗 𝑡 superscript subscript 𝒌 𝑡 top subscript 𝒐 𝑡 subscript 𝐒 𝑡 subscript 𝒒 𝑡{\mathbf{S}}_{t}={\mathbf{S}}_{t-1}\odot(\mathbf{1}{\bm{\alpha}}_{t}^{\!\top})% +{\bm{v}}_{t}{\bm{k}}_{t}^{\!\top},\;{\bm{o}}_{t}={\mathbf{S}}_{t}{\bm{q}}_{t}.bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = bold_S start_POSTSUBSCRIPT italic_t - 1 end_POSTSUBSCRIPT ⊙ ( bold_1 bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT ) + bold_italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT , bold_italic_o start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_q start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT . The form of the decay distinguishes three representative models. (i)HGRN-2 ties the gate across keys and values, i.e.𝜶 t=α t⁢𝟏 subscript 𝜶 𝑡 subscript 𝛼 𝑡 1{\bm{\alpha}}_{t}=\alpha_{t}\mathbf{1}bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_1, yielding a hierarchical separation between slowly changing coarse memory and rapidly updated token detail [[4](https://arxiv.org/html/2507.06457v1#bib.bib4)]. (ii)GLA lets 𝜶 t subscript 𝜶 𝑡{\bm{\alpha}}_{t}bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT be fully data-dependent, learned per time-step and per channel, providing maximal flexibility but higher parameter cost [[34](https://arxiv.org/html/2507.06457v1#bib.bib34)]. (iii)RetNet fixes 𝜶 t=γ subscript 𝜶 𝑡 𝛾{\bm{\alpha}}_{t}=\gamma bold_italic_α start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = italic_γ with γ∈(0,1)𝛾 0 1\gamma\in(0,1)italic_γ ∈ ( 0 , 1 ) learned once and shared across positions, giving the simplest decay and the fastest inference but no content adaptivity [[17](https://arxiv.org/html/2507.06457v1#bib.bib17)].
82	
83	#### Generation 3 – delta-rule controlled forgetting.
84	
85	The third generation abandons per-channel (diagonal) decay and instead applies a rank-1 dense transition that first erases any content aligned with the current key and then writes the new association:
86	
87	𝐒 t=𝐒 t−1⁢(𝐈−β t⁢𝒌 t⁢𝒌 t⊤)+β t⁢𝒗 t⁢𝒌 t⊤,β t∈(0,1).formulae-sequence subscript 𝐒 𝑡 subscript 𝐒 𝑡 1 𝐈 subscript 𝛽 𝑡 subscript 𝒌 𝑡 superscript subscript 𝒌 𝑡 top subscript 𝛽 𝑡 subscript 𝒗 𝑡 superscript subscript 𝒌 𝑡 top subscript 𝛽 𝑡 0 1{\mathbf{S}}_{t}={\mathbf{S}}_{t-1}\bigl{(}\mathbf{I}-\beta_{t}{\bm{k}}_{t}{% \bm{k}}_{t}^{\!\top}\bigr{)}+\beta_{t}{\bm{v}}_{t}{\bm{k}}_{t}^{\!\top},\qquad% \beta_{t}\!\in\!(0,1).bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = bold_S start_POSTSUBSCRIPT italic_t - 1 end_POSTSUBSCRIPT ( bold_I - italic_β start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT ) + italic_β start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT , italic_β start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ ( 0 , 1 ) .
88	
89	Because the projector 𝐈−β t⁢𝒌 t⁢𝒌 t⊤𝐈 subscript 𝛽 𝑡 subscript 𝒌 𝑡 superscript subscript 𝒌 𝑡 top\mathbf{I}-\beta_{t}{\bm{k}}_{t}{\bm{k}}_{t}^{\!\top}bold_I - italic_β start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT couples all channels, information can flow across dimensions, alleviating state crowding and markedly boosting long-range recall. The update is mathematically identical to a single stochastic-gradient step on an online least-squares objective—hence the name “delta rule”—the hidden state behaves similar to a fast, continually trained associative memory. This interpretation also clarifies why models such as DeltaNet and Gated DeltaNet [[5](https://arxiv.org/html/2507.06457v1#bib.bib5), [19](https://arxiv.org/html/2507.06457v1#bib.bib19)] can match Transformer perplexity and exceed it on recall-heavy tasks: each rank-1 correction injects quadratic feature interactions, giving the network a nonlinear expressiveness that standard soft-max attention (a TC 0 circuit) lacks, yet without sacrificing the O⁢(L)𝑂 𝐿 O(L)italic_O ( italic_L ) time and memory footprint.
90	
91	### 3.3 Why these representatives?
92	
93	Our main objective is to understand the roles of state size and state management in hybrid stacks. For analysis, we pick one representative for each linear attention family and treat it as the “spokesperson" for a cluster of closely related variants:
94	
95	*   •
96	HGRN (Gen-1) – the strongest vector-state model on language tasks, providing a clean, low-capacity baseline against which all matrix variants can be compared.
97	
98	*   •
99	RetNet (Gen-2, fixed decay) – its single scalar decay factor γ 𝛾\gamma italic_γ is shared across positions and channels. Lightning uses the identical mechanism, so RetNet serves as the representative for all fixed-gate outer-product models.
100	
101	*   •
102	GLA (Gen-2, data-dependent gates) – applies a fully learned per-token diagonal gate. Mamba-2 reduces this to a data-dependent scalar gate, and RWKV-6 modifies only the read-out while keeping the same gated update; all three therefore live on the same design axis, with GLA chosen as the most expressive exemplar.
103	
104	*   •
105	HGRN-2 (Gen-2, tied gate / hierarchical) – couples keys and values through a single gate, realizing a two-scale hierarchy at minimal cost. MetaLA adopts the identical tied-gate update, so HGRN-2 stands in for this class.
106	
107	These four models span the spectrum from fixed through data-dependent to hierarchically shared gating, giving us a controlled way to study how each strategy interacts with the sparse set of full-attention layers in a hybrid model. Generation-3 delta-rule networks (DeltaNet, Gated DeltaNet) are surveyed only briefly, as they are currently the sole public implementations of their family; this choice keeps our core comparison focused on the gating–versus–state-size trade-offs within Generations 1–2.
108	
109	### 3.4 Hybridization Strategy
110	
111	Figure[2](https://arxiv.org/html/2507.06457v1#S3.F2 "Figure 2 ‣ 3.4 Hybridization Strategy ‣ 3 Method ‣ A Systematic Analysis of Hybrid Linear Attention") sketches the hybrid stack used throughout our experiments. Each input sequence is first mapped to embeddings, after which the network applies a repeating block of two conceptually different layers:
112	
113	*   •
114	Linear–attention layer. The layer carries a constant-size state 𝐒 t subscript 𝐒 𝑡\mathbf{S}_{t}bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT that is updated by an outer-product write 𝐒 t=𝐒 t−1+𝒗 t⁢𝒌 t⊤subscript 𝐒 𝑡 subscript 𝐒 𝑡 1 subscript 𝒗 𝑡 superscript subscript 𝒌 𝑡 top\mathbf{S}_{t}=\mathbf{S}_{t-1}+{\bm{v}}_{t}{\bm{k}}_{t}^{\top}bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT = bold_S start_POSTSUBSCRIPT italic_t - 1 end_POSTSUBSCRIPT + bold_italic_v start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT bold_italic_k start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT (or the model-specific variant from Table[1](https://arxiv.org/html/2507.06457v1#S3.T1 "Table 1 ‣ 3.1 Linear Attention and its variants ‣ 3 Method ‣ A Systematic Analysis of Hybrid Linear Attention")). Because 𝐒 t subscript 𝐒 𝑡\mathbf{S}_{t}bold_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT does not grow with the sequence, these layers add 𝒪⁢(L⁢d)𝒪 𝐿 𝑑\mathcal{O}(Ld)caligraphic_O ( italic_L italic_d ) or 𝒪⁢(L⁢d 2)𝒪 𝐿 superscript 𝑑 2\mathcal{O}(Ld^{2})caligraphic_O ( italic_L italic_d start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT )compute and a negligible amount of cache at inference time.
115	
116	*   •
117	Full-attention layer. A standard soft-max attention Atten⁢(Q,K,V)=softmax⁢(Q⁢K⊤/d k)⁢V Atten 𝑄 𝐾 𝑉 softmax 𝑄 superscript 𝐾 top subscript 𝑑 𝑘 𝑉\text{Atten}(Q,K,V)=\mathrm{softmax}\!\bigl{(}QK^{\top}/\sqrt{d_{k}}\bigr{)}V Atten ( italic_Q , italic_K , italic_V ) = roman_softmax ( italic_Q italic_K start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT / square-root start_ARG italic_d start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT end_ARG ) italic_V refreshes global token-to-token interaction and writes its keys and values to the KV cache.
118	
119	We interleave the two kinds of layers in a fixed ratio r:1:𝑟 1 r{:}1\;italic_r : 1(linear : full), repeating the composite block N 𝑁 N italic_N times. During training the stack is processed exactly like a Transformer; during autoregressive decoding only the full-attention layers enlarge the cache, so the memory footprint is reduced by roughly a factor of r 𝑟 r italic_r. In Section [4](https://arxiv.org/html/2507.06457v1#S4 "4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") we sweep r∈{24,12,6,3}𝑟 24 12 6 3 r\in\{24,12,6,3\}italic_r ∈ { 24 , 12 , 6 , 3 } (plus the pure cases) to quantify how this trade-off affects language-model loss and recall capability.
120	
121	![Image 2: Refer to caption](https://arxiv.org/html/2507.06457v1/x2.png)
122	
123	Figure 2: Hybrid architecture: an embedding layer, N 𝑁 N italic_N repetitions of linear-attention followed by full-attention, and a projection head. Only the full-attention blocks grow the KV cache.
124	
125	### 3.5 Benchmarking framework
126	
127	For our comparative analysis, we benchmark a selection of hybridized linear attention mechanisms encompassing all three generations on language understanding and recall tasks. Specifically, we evaluate model performance on the following benchmarks: ARC-Challenge (ARC-c) [[38](https://arxiv.org/html/2507.06457v1#bib.bib38)], ARC-Easy (ARC-e) [[38](https://arxiv.org/html/2507.06457v1#bib.bib38)], HellaSwag [[39](https://arxiv.org/html/2507.06457v1#bib.bib39)], LAMBADA (LMB) [[40](https://arxiv.org/html/2507.06457v1#bib.bib40)], OpenBookQA (OBQA) [[41](https://arxiv.org/html/2507.06457v1#bib.bib41)], and PIQA [[42](https://arxiv.org/html/2507.06457v1#bib.bib42)]. For recall-specific evaluation, we additionally use RULER [[43](https://arxiv.org/html/2507.06457v1#bib.bib43)], a suite of benchmarks that assess a model’s performance on retrieval, multi-hop tracing, aggregation, and question answering.
128	
129	To systematically evaluate hybridization trade-offs, we test five configurations for each linear attention mechanism: linear-to-full attention ratios of 24:1, 12:1, 6:1, 3:1, and a fully linear (pure) variant. As a baseline, we also include a standard full-transformer model.
130	
131	All models are pretrained on the fineweb-edu[[44](https://arxiv.org/html/2507.06457v1#bib.bib44)] dataset and using flash-linear-attention library[[45](https://arxiv.org/html/2507.06457v1#bib.bib45)]. The 340M-parameter models are trained on 20 billion tokens, and the 1.3B-parameter models are trained on 100 billion tokens. All models are optimized using the AdamW optimizer with a cosine learning rate schedule. For the 340M-parameter models, we use a batch size of 50k tokens, accumulating a total of 20 billion training tokens. For the 1.3B-parameter models, the batch size is set to 1 million tokens, reaching a total of 100 billion training tokens. All evaluation benchmarks are conducted in a zero-shot manner without any task-specific fine-tuning or prompt engineering.
132	
133	4 Empirical Study
134	-----------------
135	
136	The empirical analysis then unfolds in three steps: First, we compare each linear-attention backbone in isolation and in a hybridised form that interleaves full-attention layers, revealing whether strong standalone results translate into strong hybrids. Next, keeping all other factors fixed, we vary the linear-to-full ratio (24:1, 12:1, 6:1, 3:1, and the pure linear case) and observe its effect on language-model accuracy and long-range recall as measured by RULER. Finally, by contrasting model families that differ in gating, recurrence hierarchy, and forgetting mechanisms, we identify the architectural ingredients that let hybrids match Transformer-level recall with a much smaller KV cache.
137	
138	### 4.1 Standalone Performance versus Hybrid Performance
139	
140	We investigate whether linear-attention architectures that excel in standalone evaluation maintain their relative performance when combined with full attention in hybrid configurations. Tables [2](https://arxiv.org/html/2507.06457v1#S4.T2 "Table 2 ‣ 4.1 Standalone Performance versus Hybrid Performance ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") and [3](https://arxiv.org/html/2507.06457v1#S4.T3 "Table 3 ‣ 4.1 Standalone Performance versus Hybrid Performance ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") show that this is not the case
141	
142	At the 340M parameter scale, GatedDeltaNet achieves the highest standalone accuracy. However, when hybridized, HGRN2 at a 6:1 linear-to-full attention ratio outperforms it, exceeding both the Transformer baseline and the standalone leader by 1.2 percentage points.
143	
144	Table 2: 340M model comparison of the best performing hybrid ratios from each linear attention variant as well as the transformer for language modeling performance. Up arrows indicate that a higher number is better while down arrows indicate a lower number is better. 340M models show insignificant recall capability due to their relatively small parameter count. We omit recall benchmarks for this reason.
145	
146	The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization. GatedDeltaNet at 24:1 and HGRN2 at 6:1 achieve equivalent performance, with several other hybrid configurations within one percentage point.
147	
148	Table 3: 1.3B parameter equivalent of Table [2](https://arxiv.org/html/2507.06457v1#S4.T2 "Table 2 ‣ 4.1 Standalone Performance versus Hybrid Performance ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention")
149	
150	The relative performance of different architectures changes substantially when linear and full attention mechanisms are combined, making standalone scores unreliable predictors of hybrid performance.
151	
152	### 4.2 Impact of the Linear-to-Full Attention Ratio
153	
154	![Image 3: Refer to caption](https://arxiv.org/html/2507.06457v1/extracted/6607318/Figures/trendgraph.png)
155	
156	Figure 3: Language performance and recall performance tasks are averaged and compared over varying ratios
157	
158	We examine how the linear-to-full attention ratio affects language modeling and recall performance. Figure [3](https://arxiv.org/html/2507.06457v1#S4.F3 "Figure 3 ‣ 4.2 Impact of the Linear-to-Full Attention Ratio ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") illustrates the contrasting behavior of these two capabilities across different architectures and ratios. The left panel shows that language modeling performance remains largely flat across all ratio configurations. Most architectures cluster around 0.55-0.57 average LM score, with minimal variation.
159	
160	The right panel reveals a markedly different pattern for recall performance. All architectures show a clear upward trend as the proportion of full-attention layers increases. Performance rises from pure linear configurations (around 0.1-0.35 RULER score) toward the full-attention baseline (dashed line at approximately 0.42). Notably, most architectures approach or exceed this baseline at the 3:1 ratio, with some like DeltaNet and Gated-DeltaNet achieving their peak recall performance at this configuration. This trend demonstrates that recall capability benefits substantially from increased full-attention allocation, unlike language modeling performance. The reason behind this recall trend is likely because of the near infinite hidden state inherent in the KV cache. With more full attention layers present, hybrid models perform better in recall tasks.
161	
162	The behavior of these two capabilities has practical implications. Systems prioritizing language modeling can operate efficiently with high linear-to-full ratios, while applications requiring long-range recall need more balanced attention distributions.
163	
164	We investigate the impact of the hybrid ratio further in Figure [4](https://arxiv.org/html/2507.06457v1#S4.F4 "Figure 4 ‣ 4.3 Architectural Determinants of Hybrid Effectiveness ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention"). Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio, with higher concentrations of full attention performing better than lower concentrations. Common Word Extraction (CWE) and Frequent Word Extraction (FWE) does not seem to correlate with the hybrid ratio.
165	
166	These trends indicate that, apart from pure recall tasks, where the goal is to remember some information presented in the past of a long sequence, the hybrid ratio does not make much difference. Practitioners can freely optimize the linear to full attention ratio with minimal effect on language modeling performance.
167	
168	### 4.3 Architectural Determinants of Hybrid Effectiveness
169	
170	Our experiments indicate that hybrid performance hinges on three complementary architectural properties rather than any single mechanism. Figure[3](https://arxiv.org/html/2507.06457v1#S4.F3 "Figure 3 ‣ 4.2 Impact of the Linear-to-Full Attention Ratio ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") and Tables [6](https://arxiv.org/html/2507.06457v1#S4.T6 "Table 6 ‣ 4.5 Summary of Findings and Practical Guidelines ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") and [5](https://arxiv.org/html/2507.06457v1#S4.T5 "Table 5 ‣ Practical guideline. ‣ 4.3 Architectural Determinants of Hybrid Effectiveness ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") supply the quantitative backdrop; the analysis below is necessarily observational. Ablations are left to future work.
171	
172	![Image 4: Refer to caption](https://arxiv.org/html/2507.06457v1/extracted/6607318/Figures/trend_graphs_2x2.png)
173	
174	Figure 4: RULER sub task results based on ratio. RetNet and HGRN model families are omitted as their recall benchmark results were insignificant.
175	
176	Table 4: Language modeling performance results from each linear attention variant and ratio are averaged across 1.3B and 340M parameter scales. Total average represents the aggregate score for each ratio. Pure refers to a pure Linear Attention model.
177	
178	#### Selective gating prevents catastrophic overwriting.
179	
180	Architectures that expose their hidden state to a learned, token-wise gate—GatedDeltaNet and HGRN-2—consistently perform best in recall once hybridised, surpassing the Transformer baseline by 2–5 percentage points at the optimal ratio. By contrast, RetNet’s fixed exponential decay fails to protect long-range cues, yielding near-zero recall even when full-attention layers are added.
181	
182	#### Hierarchical recurrence supplies multi-timescale context.
183	
184	The two-level pathway in HGRN-2 stores coarse summaries at a slower update rate while the fast path handles token-level details. Relative to its single-path ablation (HGRN), this hierarchy doubles recall and improves the LM–recall trade-off in Figure[3](https://arxiv.org/html/2507.06457v1#S4.F3 "Figure 3 ‣ 4.2 Impact of the Linear-to-Full Attention Ratio ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention"), suggesting that widely spaced full-attention layers benefit from a recurrent hierarchy that can “latch” information between them.
185	
186	#### Controlled forgetting curbs state crowding.
187	
188	GatedDeltaNet realises controlled forgetting with an outer-product delta rule, whereas HGRN-2 achieves the same goal through gated diagonal decay. Although only the former subtracts stale content explicitly, both mechanisms prevent the unbounded accumulation that plagues purely additive updates (e.g.GLA) and therefore attain strong recall scores.
189	
190	#### Interaction with the linear to full ratio.
191	
192	Language-model accuracy varies by less than one percent across ratios, but recall rises steadily as full-attention layers are added and saturates around 3:1. Architectures lacking either gated or delta-style forgetting never reach Transformer-level recall, regardless of ratio, implying that a suitable model architecture is necessary to attain results on par with the Transformer.
193	
194	#### Practical guideline.
195	
196	A memory-constrained practitioner can select a gated, hierarchically recurrent model with controlled forgetting—concretely, HGRN-2 or GatedDeltaNet—and devote roughly one quarter of the layers to full attention. In our 1.3B-parameter setting this configuration achieved near-Transformer recall while cutting KV-cache memory by a factor of four. Verifying the trend at larger scales remains future work.
197	
198	Table 5: Recall performance results from each linear attention variant and ratio are averaged. Total average represents the aggregate score for each ratio.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81b8c811-9e7b-4642-a39a-142edff457b2",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "04b51471-6d80-439d-9ab4-1785898166a8",
  "sourceToolAssistantUUID": "81b8c811-9e7b-4642-a39a-142edff457b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-18T12:27:24.729Z_

<details open><summary>🔧 Tool call — Read · `toolu_014vGcqvG8a98234jJwA8ThS`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/862a51fb-ad20-4c48-8de6-4985ffc65890/tool-results/toolu_01Nx4h9kyXz4ELf6tJzTqbja.txt",
  "limit": 200,
  "offset": 199
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04b51471-6d80-439d-9ab4-1785898166a8",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2rqFQA2KBn4UobxVvZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e5f7d57-ad0e-45a0-85dc-e2440b89d17b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015g5TV6ZhcQHVagCbXSKFR5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 32675,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 32675,
          "cache_creation_input_tokens": 14639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14639,
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

_source line 53 · 2026-05-18T12:27:24.734Z_

<details><summary>↩ Tool result · `toolu_014vGcqvG8a98234jJwA8ThS`</summary>

```text
199	Table 5: Recall performance results from each linear attention variant and ratio are averaged. Total average represents the aggregate score for each ratio.
200	
201	### 4.4 Performance-Efficiency Pareto Front
202	
203	We further explore the Pareto Front of performance and efficiency for all hybrid models considered herein. We relate the FLOPs of the token mixers to the language modeling performance for each model and hybridization setting (averaged over all benchmarks and both model sizes). Details for the FLOP calculation are presented in Appendix [A](https://arxiv.org/html/2507.06457v1#A1 "Appendix A Forward-Pass FLOP Analysis of Token Mixers ‣ A Systematic Analysis of Hybrid Linear Attention"). Figure [5(a)](https://arxiv.org/html/2507.06457v1#S4.F5.sf1 "Figure 5(a) ‣ Figure 5 ‣ 4.4 Performance-Efficiency Pareto Front ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") shows this Pareto Front with the FLOPs calculated for the 1.3B parameter models and a sequence length of 4,096. The Pareto Front of optimality is shown with a dashed line. It is immediately evident that the pure HGRN model, due to its vector-sized state, uses orders of magnitude fewer FLOPs than all other models. The full transformer model is on the opposite end of the Pareto Front, representing the highest performance and lowest efficiency. The middle of the Pareto Front is occupied by the HGRN 24:1 model and the HGRN2 6:1 model.
204	
205	![Image 5: Refer to caption](https://arxiv.org/html/2507.06457v1/x3.png)
206	
207	(a)Sequence length L=4096 𝐿 4096 L=4096 italic_L = 4096.
208	
209	![Image 6: Refer to caption](https://arxiv.org/html/2507.06457v1/x4.png)
210	
211	(b)Sequence length L=32768 𝐿 32768 L=32768 italic_L = 32768.
212	
213	Figure 5: Performance-Efficiency Pareto Front where FLOPs are calculated for the 1.3B parameter models with two different sequence lengths. Note that the y-axis is inverted so that the Pareto Front can be clearly seen towards the top-right.
214	
215	Figure [5(b)](https://arxiv.org/html/2507.06457v1#S4.F5.sf2 "Figure 5(b) ‣ Figure 5 ‣ 4.4 Performance-Efficiency Pareto Front ‣ 4 Empirical Study ‣ A Systematic Analysis of Hybrid Linear Attention") shows the same models with the FLOPs calculated for a sequence length of 32,768. This pushes the efficiency of models with attention layers further down. The two ends of the spectrum–the pure HGRN and the pure transformer–remain, but the lower-performance half of the spectrum is now also occupied by the pure RetNet, pure HGRN2, and pure GatedDeltaNet (in increasing order of performance).
216	
217	However, it is important to note that our efficiency metric–FLOPs in the forward pass–do not directly translate into throughput or latency on conventional hardware. Specifically, the pure HGRN model is the most efficient model in our analysis but this efficiency may not be reflected in throughput on modern GPUs. Although the HGRN requires fewer operations in total, it still requires a comparable number of memory accesses and its element-wise vector operations may underutilize the GPU in comparison to matrix operations in other token mixers. However, the HGRN’s reduced computational footprint may be accelerated on smaller GPUs or neuromorphic hardware [[46](https://arxiv.org/html/2507.06457v1#bib.bib46), [47](https://arxiv.org/html/2507.06457v1#bib.bib47)].
218	
219	### 4.5 Summary of Findings and Practical Guidelines
220	
221	This section condenses our empirical study into clear, actionable insights for building memory-efficient long-context language models.
222	
223	*   •
224	Hybrid quality cannot be inferred from standalone performance. GatedDeltaNet is strongest in purely linear form, yet HGRN-2 delivers the best results once full-attention layers are added, showing that standalone benchmarks are insufficient when selecting a hybrid backbone.
225	
226	*   •
227	Recall—not perplexity—determines the optimal linear:full mix. Moving from a 24:1 to a 3:1 ratio nearly doubles RULER recall while shifting language-model loss by less than 1,
228	
229	*   •
230	Three architectural ingredients underpin effective hybrids. Selective gating, hierarchical recurrence, and controlled forgetting jointly enable Transformer-level recall with a small KV cache; omitting any one of these components degrades retrieval markedly.
231	
232	*   •
233	Recommended deployment recipe. Employ a gated, hierarchical backbone (e.g., HGRN-2 or GatedDeltaNet) with one soft-max attention layer for every 3–6 linear layers. In our 1.3,B-parameter setting this achieves near-Transformer recall while shrinking the KV cache by a factor of 4–7.
234	
235	Table 6: Model ratios from each family with the best average RULER results are shown here.
236	
237	5 Conclusion
238	------------
239	
240	We delivered the first systematic comparison of three generations of linear-time attention mechanisms, evaluated both in isolation and within hybrid architectures that interleave a minority of full-attention layers. The study shows that, when equipped with gating, hierarchical recurrence, and controlled forgetting, linear backbones can match Transformer-level recall at a fraction of the KV-cache cost; a 3:1–6:1 (linear:full) ratio provides a practical balance between memory and quality.
241	
242	#### Limitations and future work.
243	
244	Our analysis is confined to models up to 1.3B parameters, a 2,048-token context window, and block-wise mixing ratios. Whether the observed trade-offs persist at the 10B+ scale, with 128k token contexts, or under instruction-tuning and multilingual data remains open. Exploring finer-grained hybrids (e.g., head-wise or dynamic routing) and automated architecture search (e.g., the STAR framework) constitute promising directions for extending this work.
245	
246	References
247	----------
248	
249	*   [1] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need, 2023. 
250	*   [2] Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and François Fleuret. Transformers are rnns: Fast autoregressive transformers with linear attention, 2020. 
251	*   [3] Aaron Voelker, Ivana Kajić, and Chris Eliasmith. Legendre memory units: Continuous-time representation in recurrent neural networks. Advances in neural information processing systems, 32, 2019. 
252	*   [4] Zhen Qin, Songlin Yang, Weixuan Sun, Xuyang Shen, Dong Li, Weigao Sun, and Yiran Zhong. Hgrn2: Gated linear rnns with state expansion, 2024. 
253	*   [5] Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, and Yoon Kim. Parallelizing linear transformers with the delta rule over sequence length, 2025. 
254	*   [6] Xuyang Shen, Dong Li, Ruitao Leng, Zhen Qin, Weigao Sun, and Yiran Zhong. Scaling laws for linear complexity language models. arXiv preprint arXiv:2406.16690, 2024. 
255	*   [7] Samy Jelassi, David Brandfonbrener, Sham M. Kakade, and Eran Malach. Repeat after me: transformers are better than state space models at copying. In Proceedings of the 41st International Conference on Machine Learning, ICML’24. JMLR.org, 2024. 
256	*   [8] Jerome Sieber, Carmen Amo Alonso, Alexandre Didier, Melanie Zeilinger, and Antonio Orvieto. Understanding the differences in foundation models: Attention, state space models, and recurrent neural networks. In The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024. 
257	*   [9] Jamba Team. Jamba-1.5: Hybrid transformer–mamba models at scale, 2024. 
258	*   [10] Xin Dong, Yonggan Fu, Shizhe Diao, Wonmin Byeon, Zijia Chen, et al. Hymba: A hybrid-head architecture for small language models, 2024. 
259	*   [11] MiniMax AI Team. Minimax-01: Scaling foundation models with lightning attention, 2025. 
260	*   [12] Opher Lieber, Barak Lenz, Hofit Bata, Gal Cohen, Shaked Meirom, Yoav Shoham, et al. Jamba: A hybrid transformer–mamba language model, 2024. 
261	*   [13] Michael Poli, Jue Wang, Stefano Massaroli, Jeffrey Quesnelle, Ryan Carlow, Eric Nguyen, and Armin Thomas. StripedHyena: Moving Beyond Transformers with Hybrid Signal Processing Models, 12 2023. 
262	*   [14] Kai Liu, Jianfei Gao, and Kai Chen. Scaling laws for rnn llm in long-context scenarios with state size. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics. Association for Computational Linguistics, 2025. 
263	*   [15] Imanol Schlag, Kazuki Irie, and Jürgen Schmidhuber. Linear transformers are secretly fast weight programmers, 2021. 
264	*   [16] Bo Peng, Eric Alcaide, Quentin Anthony, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin Cheng, Michael Chung, Matteo Grella, Kranthi Kiran GV, Xuzheng He, Haowen Hou, Jiaju Lin, Przemyslaw Kazienko, Jan Kocon, Jiaming Kong, Bartlomiej Koptyra, Hayden Lau, Krishna Sri Ipsit Mantri, Ferdinand Mom, Atsushi Saito, Guangyu Song, Xiangru Tang, Bolun Wang, Johan S. Wind, Stanislaw Wozniak, Ruichong Zhang, Zhenyuan Zhang, Qihang Zhao, Peng Zhou, Qinghua Zhou, Jian Zhu, and Rui-Jie Zhu. Rwkv: Reinventing rnns for the transformer era, 2023. 
265	*   [17] Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, and Furu Wei. Retentive network: A successor to transformer for large language models, 2023. 
266	*   [18] Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with selective state spaces, 2024. 
267	*   [19] Songlin Yang, Jan Kautz, and Ali Hatamizadeh. Gated delta networks: Improving mamba2 with delta rule, 2025. 
268	*   [20] Roger Waleffe, Wonmin Byeon, Duncan Riach, Brandon Norick, Vijay Korthikanti, Tri Dao, Albert Gu, Ali Hatamizadeh, Sudhakar Singh, Deepak Narayanan, et al. An empirical study of mamba-based language models. arXiv preprint arXiv:2406.07887, 2024. 
269	*   [21] Jongho Park, Jaeseung Park, Zheyang Xiong, Nayoung Lee, Jaewoong Cho, Samet Oymak, Kangwook Lee, and Dimitris Papailiopoulos. Can mamba learn how to learn? a comparative study on in-context learning tasks. arXiv preprint arXiv:2402.04248, 2024. 
270	*   [22] Yingfa Chen, Xinrong Zhang, Shengding Hu, Xu Han, Zhiyuan Liu, and Maosong Sun. Stuffed mamba: State collapse and state capacity of RNN-based long-context modeling, 2024. 
271	*   [23] Daniel Y Fu, Tri Dao, Khaled Kamal Saab, Armin W Thomas, Atri Rudra, and Christopher Re. Hungry hungry hippos: Towards language modeling with state space models. In The Eleventh International Conference on Learning Representations, 2023. 
272	*   [24] Aleksandar Botev, Soham De, Samuel L. Smith, Anushan Fernando, et al. Recurrentgemma: Moving past transformers for efficient open language models, 2024. 
273	*   [25] Character.AI Research Blog. Optimizing ai inference at character.ai. [https://research.character.ai/optimizing-inference/](https://research.character.ai/optimizing-inference/), 2024. 
274	*   [26] Paolo Glorioso, Quentin Anthony, Yury Tokpanov, James Whittington, Jonathan Pilault, and Beren Millidge. Zamba: A compact 7b ssm hybrid model, 2024. 
275	*   [27] Paolo Glorioso, Quentin Anthony, Yury Tokpanov, Anna Golubeva, Vasudev Shyam, et al. The zamba2 suite: Technical report, 2024. 
276	*   [28] Liliang Ren, Yang Liu, Yadong Lu, Yelong Shen, Chen Liang, and Weizhu Chen. Samba: Simple hybrid state space models for efficient unlimited context language modeling, 2024. 
277	*   [29] Yutao Sun, Li Dong, Yi Zhu, Shaohan Huang, Wenhui Wang, Shuming Ma, Quanlu Zhang, Jianyong Wang, and Furu Wei. You only cache once: Decoder-decoder architectures for language models, 2024. 
278	*   [30] Elliott Goldstein, Michael Goldblum, Minshuo Chen, and Tom Goldstein. Goldfinch: Tokencat compression for memory-efficient hybrid rnn–transformer models, 2024. 
279	*   [31] Armin W Thomas, Rom Parnichkun, Alexander Amini, Stefano Massaroli, and Michael Poli. STAR: Synthesis of tailored architectures. In The Thirteenth International Conference on Learning Representations, 2025. 
280	*   [32] Michael Poli, Armin W Thomas, Eric Nguyen, Pragaash Ponnusamy, Björn Deiseroth, Kristian Kersting, Taiji Suzuki, Brian Hie, Stefano Ermon, Christopher Ré, Ce Zhang, and Stefano Massaroli. Mechanistic design and scaling of hybrid architectures. In Proceedings of the 41st International Conference on Machine Learning, ICML’24, 2024. 
281	*   [33] Soham De, Samuel L Smith, Anushan Fernando, Aleksandar Botev, George Cristian-Muraru, Albert Gu, Ruba Haroun, Leonard Berrada, Yutian Chen, Srivatsan Srinivasan, et al. Griffin: Mixing gated linear recurrences with local attention for efficient language models. arXiv preprint arXiv:2402.19427, 2024. 
282	*   [34] Songlin Yang, Bailin Wang, Yikang Shen, Rameswar Panda, and Yoon Kim. Gated linear attention transformers with hardware-efficient training. In Proceedings of the 41st International Conference on Machine Learning (ICML), 2024. 
283	*   [35] Tri Dao and Albert Gu. Transformers are ssms: Generalized models and efficient algorithms through structured state space duality. arXiv preprint arXiv:2405.21060, 2024. 
284	*   [36] Bo Peng, Daniel Goldstein, Quentin Anthony, Alon Albalak, Eric Alcaide, Stella Biderman, Eugene Cheah, Xingjian Du, Teddy Ferdinan, Haowen Hou, Przemysław Kazienko, Kranthi Kiran GV, Jan Kocoń, Bartłomiej Koptyra, Satyapriya Krishna, Ronald McClelland Jr., Jiaju Lin, Niklas Muennighoff, Fares Obeid, Atsushi Saito, Guangyu Song, Haoqin Tu, Cahya Wirawan, Stanisław Woźniak, Ruichong Zhang, Bingchen Zhao, Qihang Zhao, Peng Zhou, Jian Zhu, and Rui-Jie Zhu. Eagle and finch: Rwkv with matrix-valued states and dynamic recurrence, 2024. 
285	*   [37] Yuhong Chou, Man Yao, Kexin Wang, Yuqi Pan, Rui-Jie Zhu, Jibin Wu, Yiran Zhong, Yu Qiao, Bo Xu, and Guoqi Li. Metala: Unified optimal linear approximation to softmax attention map. Advances in Neural Information Processing Systems, 37:71034–71067, 2024. 
286	*   [38] Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge, 2018. 
287	*   [39] Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a machine really finish your sentence?, 2019. 
288	*   [40] Denis Paperno, Germán Kruszewski, Angeliki Lazaridou, Quan Ngoc Pham, Raffaella Bernardi, Sandro Pezzelle, Marco Baroni, Gemma Boleda, and Raquel Fernández. The lambada dataset: Word prediction requiring a broad discourse context, 2016. 
289	*   [41] Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. Can a suit of armor conduct electricity? a new dataset for open book question answering, 2018. 
290	*   [42] Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. Piqa: Reasoning about physical commonsense in natural language, 2019. 
291	*   [43] Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and Boris Ginsburg. Ruler: What’s the real context size of your long-context language models?, 2024. 
292	*   [44] Guilherme Penedo, Hynek Kydlíček, Anton Lozhkov, Margaret Mitchell, Colin A Raffel, Leandro Von Werra, Thomas Wolf, et al. The fineweb datasets: Decanting the web for the finest text data at scale. Advances in Neural Information Processing Systems, 37:30811–30849, 2024. 
293	*   [45] Songlin Yang and Yu Zhang. Fla: A triton-based library for hardware-efficient implementations of linear attention mechanism, 2024. 
294	*   [46] Rui-Jie Zhu, Yu Zhang, Ethan Sifferman, Tyler Sheaves, Yiqiao Wang, Dustin Richmond, Peng Zhou, and Jason K. Eshraghian. Scalable matmul-free language modeling, 2024. 
295	*   [47] Steven Abreu, Sumit Bam Shrestha, Rui-Jie Zhu, and Jason Eshraghian. Neuromorphic principles for efficient large language models on intel loihi 2. In First Workshop on Scalable Optimization for Efficient and Adaptive Foundation Models, 2025. 
296	
297	Appendix A Forward-Pass FLOP Analysis of Token Mixers
298	-----------------------------------------------------
299	
300	This section derives closed-form expressions for the floating-point operations (FLOPs) required by the different recurrent and linear-attention token mixers that are presented in this paper, and contrasts them with classical softmax self-attention. All counts are per layer, forward pass only, aggregated over all heads. Projection layers, (un-)embedding, residual additions, normalisation, and other feed-forward blocks are _not_ included so that every token mixer is compared on equal footing.
301	
302	#### Notation and assumptions
303	
304	*   •
305	L 𝐿 L italic_L – causal sequence length (tokens seen by the layer).
306	
307	*   •
308	H 𝐻 H italic_H - number of heads in the model (this applies to all trained models except the HGRN-1 model where H=1 𝐻 1 H=1 italic_H = 1 by design).
309	
310	*   •
311	d 𝑑 d italic_d – width of a single head. Vectors within a single head live in ℝ d superscript ℝ 𝑑\mathbb{R}^{d}blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT. For a model dimension d model subscript 𝑑 model d_{\text{model}}italic_d start_POSTSUBSCRIPT model end_POSTSUBSCRIPT with H 𝐻 H italic_H heads we have d=d model/H 𝑑 subscript 𝑑 model 𝐻 d=d_{\text{model}}/H italic_d = italic_d start_POSTSUBSCRIPT model end_POSTSUBSCRIPT / italic_H.
312	
313	*   •
314	One FLOP is a single floating-point multiply _or_ add.
315	
316	*   •
317	Only the token-mixer is costed. Projections, MLPs, norms, residuals are identical across models and therefore omitted.
318	
319	*   •
320	All counts below are _per token, per layer, summed over all heads_. Multiply by L 𝐿 L italic_L for a sequence, and by the number of layers to estimate a full network.
321	
322	Table 7: Per-token forward FLOP counts _summed over all heads_. Multiply by L 𝐿 L italic_L to obtain the per-layer sequence cost. For HGRN-1 the mixer is single-head by design (H=1 𝐻 1 H=1 italic_H = 1); all other models allow arbitrary H 𝐻 H italic_H. Softmax attention is quadratic in L 𝐿 L italic_L, whereas the linear/recurrent mixers are linear.
323	
324	#### Baseline: softmax self-attention
325	
326	The dot-product matrix Q⁢K⊤𝑄 superscript 𝐾 top QK^{\top}italic_Q italic_K start_POSTSUPERSCRIPT ⊤ end_POSTSUPERSCRIPT is strictly lower-triangular under causal masking. Forming and applying it costs (H⁢L⁢(L+1)⁢d head)𝐻 𝐿 𝐿 1 subscript 𝑑 head(H\,L(L+1)d_{\mathrm{head}})( italic_H italic_L ( italic_L + 1 ) italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT ) multiplies plus the same number of adds. Using d model=H⁢d head subscript 𝑑 model 𝐻 subscript 𝑑 head d_{\mathrm{model}}=Hd_{\mathrm{head}}italic_d start_POSTSUBSCRIPT roman_model end_POSTSUBSCRIPT = italic_H italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT gives
327	
328	FLOPs softmax≈ 2⁢L 2⁢d model.subscript FLOPs softmax 2 superscript 𝐿 2 subscript 𝑑 model\mathrm{FLOPs}_{\text{softmax}}\;\approx\;2L^{2}d_{\mathrm{model}}.roman_FLOPs start_POSTSUBSCRIPT softmax end_POSTSUBSCRIPT ≈ 2 italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT roman_model end_POSTSUBSCRIPT .(1)
329	
330	Importantly the head count cancels, so the quadratic term depends only on the model width.
331	
332	#### Vector-state mixers (classical / gated RNNs)
333	
334	A single hidden vector h t∈ℝ d head subscript ℎ 𝑡 superscript ℝ subscript 𝑑 head h_{t}\!\in\!\mathbb{R}^{d_{\mathrm{head}}}italic_h start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT end_POSTSUPERSCRIPT is maintained _per head_. Each head therefore needs 5⁢d head 5 subscript 𝑑 head 5d_{\mathrm{head}}5 italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT FLOPs per token. Aggregating over H 𝐻 H italic_H heads:
335	
336	FLOPs vector=5⁢H⁢d head=5⁢d model.subscript FLOPs vector 5 𝐻 subscript 𝑑 head 5 subscript 𝑑 model\mathrm{FLOPs}_{\text{vector}}=5Hd_{\mathrm{head}}=5d_{\mathrm{model}}.roman_FLOPs start_POSTSUBSCRIPT vector end_POSTSUBSCRIPT = 5 italic_H italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT = 5 italic_d start_POSTSUBSCRIPT roman_model end_POSTSUBSCRIPT .(2)
337	
338	For HGRN-1 and Hawk, the reference implementation is single-head; we therefore take H=1 𝐻 1 H=1 italic_H = 1 and d head=d model subscript 𝑑 head subscript 𝑑 model d_{\mathrm{head}}=d_{\mathrm{model}}italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT = italic_d start_POSTSUBSCRIPT roman_model end_POSTSUBSCRIPT.
339	
340	#### Matrix-state mixers (outer-product family)
341	
342	Each head carries a dense state S t∈ℝ d head×d head subscript 𝑆 𝑡 superscript ℝ subscript 𝑑 head subscript 𝑑 head S_{t}\in\mathbb{R}^{d_{\mathrm{head}}\times d_{\mathrm{head}}}italic_S start_POSTSUBSCRIPT italic_t end_POSTSUBSCRIPT ∈ blackboard_R start_POSTSUPERSCRIPT italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT × italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT end_POSTSUPERSCRIPT. If an update costs k⁢d head 2 𝑘 superscript subscript 𝑑 head 2 k\,d_{\mathrm{head}}^{2}italic_k italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT FLOPs per head (where k 𝑘 k italic_k is a constant that varies between different models), the layer total is:
343	
344	FLOPs matrix=k⁢H⁢d head 2=k⁢d model 2 H.subscript FLOPs matrix 𝑘 𝐻 superscript subscript 𝑑 head 2 𝑘 superscript subscript 𝑑 model 2 𝐻\mathrm{FLOPs}_{\text{matrix}}=kHd_{\mathrm{head}}^{2}\;=\;k\,\frac{d_{\mathrm% {model}}^{2}}{H}.roman_FLOPs start_POSTSUBSCRIPT matrix end_POSTSUBSCRIPT = italic_k italic_H italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = italic_k divide start_ARG italic_d start_POSTSUBSCRIPT roman_model end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG italic_H end_ARG .(3)
345	
346	Hence adding more heads _reduces_ the cost of these mixers at fixed d model subscript 𝑑 model d_{\mathrm{model}}italic_d start_POSTSUBSCRIPT roman_model end_POSTSUBSCRIPT. Each “pass” over the d head×d head subscript 𝑑 head subscript 𝑑 head d_{\mathrm{head}}\times d_{\mathrm{head}}italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT × italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT matrix either multiplies all entries or adds a rank–1 outer product, each costing d head 2 superscript subscript 𝑑 head 2 d_{\mathrm{head}}^{2}italic_d start_POSTSUBSCRIPT roman_head end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT FLOPs. Summing the passes per token per head gives:
347	
348	*   •
349	RetNet / Mamba–2: five passes ⇒⇒\Rightarrow⇒ k=5.
350	
351	*   •
352	GLA, RWKV–6, HGRN–2: two extra gating passes (seven total) ⇒⇒\Rightarrow⇒ k=7.
353	
354	*   •
355	DeltaNet (& Gated): one further forget/restore pass (eight total) ⇒⇒\Rightarrow⇒ k=8.
356	
357	#### Summary
358	
359	Table [7](https://arxiv.org/html/2507.06457v1#A1.T7 "Table 7 ‣ Notation and assumptions ‣ Appendix A Forward-Pass FLOP Analysis of Token Mixers ‣ A Systematic Analysis of Hybrid Linear Attention") shows a comparison between all models presented in Table 1. Once head aggregation is included the classical vector mixers (HGRN-1, Hawk) remain linear in L 𝐿 L italic_L and independent of H 𝐻 H italic_H. Outer-product and Delta-rule mixers grow as d model 2/H superscript subscript 𝑑 model 2 𝐻 d_{\mathrm{model}}^{2}/H italic_d start_POSTSUBSCRIPT roman_model end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT / italic_H—wider models prefer more heads from a FLOP viewpoint—yet are still asymptotically cheaper than softmax self-attention for long sequences. Figure [6](https://arxiv.org/html/2507.06457v1#A1.F6 "Figure 6 ‣ Summary ‣ Appendix A Forward-Pass FLOP Analysis of Token Mixers ‣ A Systematic Analysis of Hybrid Linear Attention") shows how the FLOPs scale with sequence lengths for different pure (non-hybrid) token mixers.
360	
361	![Image 7: Refer to caption](https://arxiv.org/html/2507.06457v1/x5.png)
362	
363	Figure 6: Relationship between the sequence length and the number of FLOPs required by different token mixers. Note that the HGRN-2 and GLA overlap, see analysis in the text.
364	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e5f7d57-ad0e-45a0-85dc-e2440b89d17b",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "e15bee43-497c-4696-81e3-73cab4d12360",
  "sourceToolAssistantUUID": "6e5f7d57-ad0e-45a0-85dc-e2440b89d17b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-18T12:27:30.000Z_

Now I have the full paper. The paper cites flash-linear-attention as reference [45] but does not specify a version or commit hash. Let me check the PyPI release history more carefully to map dates to the models' training timeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e15bee43-497c-4696-81e3-73cab4d12360",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2sJWF6KktJqgrFWEXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "655b81d0-6f3e-4b4d-8bcc-cc6e4d5e6c3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrsNhdmdeiRC3wtkwoxq7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8886,
      "cache_read_input_tokens": 47314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8886,
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

_source line 55 · 2026-05-18T12:27:30.944Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WGgwn4nBtPPZaa23ENe4mt`</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/#history",
  "prompt": "List ALL versions with their exact release dates. I need the complete version history table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "655b81d0-6f3e-4b4d-8bcc-cc6e4d5e6c3a",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2sJWF6KktJqgrFWEXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "868b3d26-7294-4bd4-b169-9c718db21028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrsNhdmdeiRC3wtkwoxq7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8886,
      "cache_read_input_tokens": 47314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8886,
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

_source line 56 · 2026-05-18T12:27:32.838Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DYa6vMWCdpH4Mwah43qymY`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.2",
  "prompt": "Show the release notes for v0.4.2. What changes were included? What was the date? Any breaking changes or new model support mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "868b3d26-7294-4bd4-b169-9c718db21028",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2sJWF6KktJqgrFWEXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "315c08e1-6ddc-44f2-896c-924eca296a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrsNhdmdeiRC3wtkwoxq7t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8886,
      "cache_read_input_tokens": 47314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8886,
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

_source line 57 · 2026-05-18T12:27:33.300Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ASkRHAVMWJgYWySkoMGvsK`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.4.1",
  "prompt": "Show the release notes for v0.4.1. What changes were included? What was the date? List all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "315c08e1-6ddc-44f2-896c-924eca296a92",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2sJWF6KktJqgrFWEXq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d67fb820-b0d3-4a48-a7db-b017c055892f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrsNhdmdeiRC3wtkwoxq7t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8886,
      "cache_read_input_tokens": 47314,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 47314,
          "cache_creation_input_tokens": 8886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8886,
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

_source line 58 · 2026-05-18T12:27:34.399Z_

<details><summary>↩ Tool result · `toolu_01WGgwn4nBtPPZaa23ENe4mt`</summary>

```text
# Flash Linear Attention - Complete Version History

Based on the PyPI page, here is the complete release history with dates:

| Version | Release Date |
|---------|---|
| 0.5.0 | Apr 21, 2026 |
| 0.4.2 | Mar 12, 2026 |
| 0.4.1 | Dec 24, 2025 |
| 0.4.0 | Oct 27, 2025 |
| 0.3.2 | Sep 10, 2025 |
| 0.3.1 | Aug 26, 2025 |
| 0.3.0 | Jul 14, 2025 |
| 0.2.2 | Jun 5, 2025 |
| 0.2.1 | Apr 23, 2025 |
| 0.2.0 | Apr 11, 2025 |
| 0.1.2 | Mar 31, 2025 |
| 0.1.1 | Mar 24, 2025 |
| 0.1 | Mar 20, 2025 |

The current stable release is **0.5.0** (April 2026), which provides "efficient implementations for emerging model architectures, with a focus on efficient sequence modeling."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "868b3d26-7294-4bd4-b169-9c718db21028",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "daa73d30-91ff-4e4d-b63f-618c498330b1",
  "sourceToolAssistantUUID": "868b3d26-7294-4bd4-b169-9c718db21028",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-18T12:27:38.868Z_

<details><summary>↩ Tool result · `toolu_01ASkRHAVMWJgYWySkoMGvsK`</summary>

```text
# Release Notes for v0.4.1

**Release Date:** December 24

**Notable Changes:**

The v0.4.1 release included 30+ commits addressing performance optimizations and bug fixes across multiple components:

**Key Improvements:**
- "Fix oom on A6000" memory issue resolution
- KDA (kernel) optimizations including fused gate operations and intra-chunk attention improvements
- Precision fixes for RMSNorm dtype handling
- L2Norm recompilation avoidance for variable-length inputs
- NSA layer enhancements with head_dim parameter support
- GDN out-of-bounds bug corrections

**Bug Fixes:**
- Fixed weight decay term in KDA
- Corrected K/V dimension mismatches in attention backward kernels
- Resolved contiguous memory layout enforcement in KDA gate
- Fixed docstring parameter documentation

**Performance Features:**
- Added chunk_indices parameter to reduce redundant computation
- Implemented token-parallel intra-chunk attention
- Enabled precision autotune capabilities
- Added PTX softplus support for AMD/Intel devices

The release attracted 7 new contributors and included 160 subsequent commits to the main branch, indicating active ongoing development.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d67fb820-b0d3-4a48-a7db-b017c055892f",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "62cd0f61-7b25-414e-99ef-eed73ab6275e",
  "sourceToolAssistantUUID": "d67fb820-b0d3-4a48-a7db-b017c055892f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T12:27:39.033Z_

<details><summary>↩ Tool result · `toolu_01DYa6vMWCdpH4Mwah43qymY`</summary>

```text
# Flash-Linear-Attention v0.4.2 Release Notes

**Release Date:** March 12, 2024

## Key Changes

This release included 41 merged pull requests with improvements across multiple components:

**Performance & Optimization:**
- Introduced a backend dispatch system for better flexibility
- Reduced device-to-host/host-to-device synchronization overhead
- Added lowerbound gate function to speed up KDA and DPLR operations
- Optimized convolution operations with mixed Triton forward and CUDA backward support

**Bug Fixes & Compatibility:**
- Fixed memory access issues in convolution kernels
- Corrected varlen-related logic in NSA dkv kernel
- Enhanced compatibility with Triton 3.2 and AMD RDNA GPUs
- Fixed initialization issues for Mamba2 with FSDP-2 DTensors
- Prevented int32 index overflow for long sequences

**Architectural Improvements:**
- Refactored convolution code into organized packages
- Centralized reference implementations
- Added cache support for intra-card context parallelism
- Removed deprecated torch.jit.script decorators

## Breaking Changes or New Models

The release notes do not explicitly mention breaking changes or new model support, focusing instead on internal improvements and optimizations to existing implementations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "315c08e1-6ddc-44f2-896c-924eca296a92",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "7331a832-6e1a-4b17-a0ab-a2248b679179",
  "sourceToolAssistantUUID": "315c08e1-6ddc-44f2-896c-924eca296a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-18T12:27:43.289Z_

Now let me check for any connection between the paper authors and the fla repository, and look at what version of fla existed when the earliest models (March 2025) were uploaded.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7331a832-6e1a-4b17-a0ab-a2248b679179",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2tMdngagg6FFqyUosQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00d3bdf1-f7ea-4294-9188-2b986148f9fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HgGai1m2T76o8dKnm7muJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 305,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 56200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1039,
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

_source line 62 · 2026-05-18T12:27:44.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XEYEFkkdbkdD8DxgJFTX6m`</summary>

```json
{
  "query": "\"Songlin Yang\" \"Yu Zhang\" flash-linear-attention \"Wang\" \"hybrid linear attention\" fla version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00d3bdf1-f7ea-4294-9188-2b986148f9fc",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2tMdngagg6FFqyUosQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f975c08e-f82b-4b81-916a-6cf7dfcf5068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HgGai1m2T76o8dKnm7muJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 305,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 56200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1039,
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

_source line 63 · 2026-05-18T12:27:45.039Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SCBLu2KgnVaFpwQNRQCDMZ`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/blob/main/fla/__init__.py",
  "prompt": "Show the complete contents of this __init__.py file. I need to see the __version__ variable."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f975c08e-f82b-4b81-916a-6cf7dfcf5068",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2tMdngagg6FFqyUosQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6004ea8-0b90-40b4-b461-9738b89ceebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016HgGai1m2T76o8dKnm7muJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 305,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 56200,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 305,
          "output_tokens": 216,
          "cache_read_input_tokens": 56200,
          "cache_creation_input_tokens": 1039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1039,
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

_source line 64 · 2026-05-18T12:27:48.161Z_

<details><summary>↩ Tool result · `toolu_01SCBLu2KgnVaFpwQNRQCDMZ`</summary>

````text
Based on the webpage content provided, here is the complete `__init__.py` file:

```python
# Copyright (c) 2023-2026, Songlin Yang, Yu Zhang, Zhiyuan Li
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
# For a list of all contributors, visit:
# https://github.com/fla-org/flash-linear-attention/graphs/contributors

import importlib
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

__version__ = "0.5.1"

__all__: list[str] = []

def _export_optional_public_api(module_name: str) -> None:
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        if exc.name == module_name:
            return
        raise

    globals()[module_name.rsplit(".", maxsplit=1)[-1]] = module

    for name in module.__all__:
        if name.endswith("Config"):
            continue
        globals()[name] = getattr(module, name)
        __all__.append(name)

_export_optional_public_api("fla.layers")
_export_optional_public_api("fla.models")

del _export_optional_public_api
```

The `__version__` variable is set to **"0.5.1"**.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6004ea8-0b90-40b4-b461-9738b89ceebe",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "719654eb-bed6-42fb-80b9-560790548a33",
  "sourceToolAssistantUUID": "b6004ea8-0b90-40b4-b461-9738b89ceebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T12:28:02.263Z_

<details><summary>↩ Tool result · `toolu_01XEYEFkkdbkdD8DxgJFTX6m`</summary>

```text
Web search results for query: ""Songlin Yang" "Yu Zhang" flash-linear-attention "Wang" "hybrid linear attention" fla version"

Links: [{"title":"Songlin Yang","url":"https://sustcsonglin.github.io/"},{"title":"publications | Songlin Yang - GitHub Pages","url":"https://sustcsonglin.github.io/publications/"},{"title":"[PDF] Gated Linear Attention Transformers with Hardware-Efficient Training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Gated-Linear-Attention-Transformers-with-Training-Yang-Wang/62b18cc55dcc7ffe52c28e1086aee893b7bc4334"},{"title":"Linear Transformers for Eﬃcient Sequence Modeling Songlin Yang MIT CSAIL","url":"https://sustcsonglin.github.io/assets/pdf/talk_linear_transformer.pdf"},{"title":"Published as a conference paper at ICLR 2026 LOG-LINEAR ATTENTION Han Guo1∗","url":"https://arxiv.org/pdf/2506.04761"},{"title":"Gated Slot Attention for Efficient Linear-Time Sequence Modeling Yu Zhang1∗","url":"https://arxiv.org/pdf/2409.07146"},{"title":"Songlin Yang","url":"https://www.catalyzex.com/author/Songlin%20Yang"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"Parallelizing Linear Transformers with the Delta Rule over Sequence Length","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d13a3eae72366e61dfdc7eea82eeb685-Paper-Conference.pdf"},{"title":"DeltaNet Explained (Part II) | Songlin Yang - GitHub Pages","url":"https://sustcsonglin.github.io/blog/2024/deltanet-2/"}]

I found relevant information about the research you're asking about. Here are the key findings:

## Flash Linear Attention (FLA) Library

Songlin Yang and Yu Zhang developed FLA: A Triton-based library for hardware-efficient implementations of linear attention mechanism (2024).

## Key Papers and Research

Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, and Yoon Kim published work on Gated Linear Attention Transformers with Hardware-Efficient Training at NeurIPS 2024, with an implementation called FLASHLINEARATTENTION that is faster than FLASHATTENTION-2 even on short sequence lengths.

Yang, Wang, Zhang, Shen, and Kim also published "Parallelizing Linear Transformers with the Delta Rule over Sequence Length" as a NeurIPS '24 paper.

## Hybrid Linear Attention

A hybrid linear attention architecture called Kimi Linear was introduced by the Kimi Team including Yu Zhang and Songlin Yang, which outperforms full attention across various scenarios including short-context, long-context, and reinforcement learning scaling regimes.

The research involves developing efficient implementations of linear attention mechanisms in Triton, with focus on hardware optimization through techniques like block-parallel computations over sequence chunks and specialized matrix representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f975c08e-f82b-4b81-916a-6cf7dfcf5068",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "c21bc3c4-79ca-4d0b-8846-1cb7ef0ae691",
  "sourceToolAssistantUUID": "f975c08e-f82b-4b81-916a-6cf7dfcf5068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-18T12:28:05.938Z_

Now let me check the git tags/commits around March 2025 to determine what version was available when training began. Let me also check if there's a specific commit referenced in the flame repo.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c21bc3c4-79ca-4d0b-8846-1cb7ef0ae691",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2v4qoBF56j1goNxtZF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93bd132e-c9a1-4064-9cf0-605dc0e9d83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018pEMCdcAFVXXgUpAfDFhAX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 390,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 57239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 67 · 2026-05-18T12:28:06.892Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UvBurSF6LqsLP6KAQFVXN9`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/v0.1",
  "prompt": "Show the release notes for v0.1. What was the exact date? What features and models were supported? List all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93bd132e-c9a1-4064-9cf0-605dc0e9d83b",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2v4qoBF56j1goNxtZF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5720a1c6-9b9e-45cf-9591-ddbdccd44497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018pEMCdcAFVXXgUpAfDFhAX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 390,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 57239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1462,
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

_source line 68 · 2026-05-18T12:28:07.263Z_

<details><summary>↩ Tool result · reported error · `toolu_01UvBurSF6LqsLP6KAQFVXN9`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5720a1c6-9b9e-45cf-9591-ddbdccd44497",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "c4461a7c-eade-4988-b84c-d1fc060d5f12",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "5720a1c6-9b9e-45cf-9591-ddbdccd44497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-18T12:28:07.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WF9XbE8bDHrq1273GtHYvp`</summary>

```json
{
  "query": "site:huggingface.co m-a-p \"1.3B-100B\" OR \"340M-20B\" \"fla\" OR \"flash-linear-attention\" version requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4461a7c-eade-4988-b84c-d1fc060d5f12",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2v4qoBF56j1goNxtZF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62a6da50-8727-4553-afb7-420bbcbca848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018pEMCdcAFVXXgUpAfDFhAX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 390,
      "cache_creation_input_tokens": 1462,
      "cache_read_input_tokens": 57239,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1462
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 390,
          "output_tokens": 239,
          "cache_read_input_tokens": 57239,
          "cache_creation_input_tokens": 1462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1462,
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

_source line 70 · 2026-05-18T12:28:13.180Z_

<details><summary>↩ Tool result · `toolu_01WF9XbE8bDHrq1273GtHYvp`</summary>

```text
Web search results for query: "site:huggingface.co m-a-p "1.3B-100B" OR "340M-20B" "fla" OR "flash-linear-attention" version requirements"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"},{"title":"flash-linear-attention/examples/training.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/examples/training.md"},{"title":"flash-linear-attention/README.md at main · fla-org/flash-linear-attention","url":"https://github.com/sustcsonglin/flash-linear-attention/blob/main/README.md"},{"title":"m-a-p/transformer_340M_baseline · Hugging Face","url":"https://huggingface.co/m-a-p/transformer_340M_baseline"},{"title":"m-a-p/1.3B-100B-DeltaNet-hybrid-6-1 · Hugging Face","url":"https://huggingface.co/m-a-p/1.3B-100B-DeltaNet-hybrid-6-1"},{"title":"Hybrid Linear Attention Research - a m-a-p Collection","url":"https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research"},{"title":"m-a-p/340M-20B-DeltaNet-hybrid-24-1 · Hugging Face","url":"https://huggingface.co/m-a-p/340M-20B-DeltaNet-hybrid-24-1"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/html/2507.06457v1"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=linear+attention"}]

Based on the search results, I found information about the m-a-p models with the model sizes you specified (340M-20B and 1.3B-100B) related to flash-linear-attention (fla).

The m-a-p team trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios. All models are pretrained on the fineweb-edu dataset and using flash-linear-attention library.

However, the search results do not contain specific information about version requirements for these models. The results show model collections and repositories on Hugging Face (m-a-p organization) that contain these model configurations, but detailed version requirements for dependencies are not included in the search results provided.

To find specific version requirements, you may need to:
1. Visit the individual model cards on the Hugging Face Hub for each m-a-p model variant
2. Check the flash-linear-attention GitHub repository's requirements.txt or setup.py files
3. Review the model's README files which typically list compatibility information


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62a6da50-8727-4553-afb7-420bbcbca848",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "fcc375df-1516-4a49-b07e-5babd49f8e7f",
  "sourceToolAssistantUUID": "62a6da50-8727-4553-afb7-420bbcbca848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-18T12:28:16.701Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SzfHUseRiWvcFPvGLD6fZQ`</summary>

```json
{
  "url": "https://github.com/fla-org/flash-linear-attention/releases/tag/0.1",
  "prompt": "Show the release notes for v0.1 (tag 0.1). What was the exact date? What features were supported?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc375df-1516-4a49-b07e-5babd49f8e7f",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2vsWSxw576rucAFJ7E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1facd57e-f288-4dc8-b4b6-a49b071960f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vfwY42vokt1rfmNpjPPhu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 58701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1561,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
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

_source line 72 · 2026-05-18T12:28:17.118Z_

<details><summary>↩ Tool result · reported error · `toolu_01SzfHUseRiWvcFPvGLD6fZQ`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1facd57e-f288-4dc8-b4b6-a49b071960f4",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "3822510e-e79d-4e6e-8d77-e10a2fc9ef7f",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "1facd57e-f288-4dc8-b4b6-a49b071960f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T12:28:17.132Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DbQbBn9hzvuc2B4zDHXC4b`</summary>

```json
{
  "command": "pip show flash-linear-attention 2>/dev/null || echo \"flash-linear-attention not installed locally\"",
  "description": "Check if flash-linear-attention is installed locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3822510e-e79d-4e6e-8d77-e10a2fc9ef7f",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2vsWSxw576rucAFJ7E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a87cb94f-4ec6-4524-919b-11b7d514c176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vfwY42vokt1rfmNpjPPhu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 58701,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1561
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 58701,
          "cache_creation_input_tokens": 1561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1561,
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

_source line 74 · 2026-05-18T12:28:17.600Z_

<details><summary>↩ Tool result · `toolu_01DbQbBn9hzvuc2B4zDHXC4b`</summary>

```text
flash-linear-attention not installed locally
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a87cb94f-4ec6-4524-919b-11b7d514c176",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "17b4b6d8-8728-4ebb-9d12-f1ef9699a7ba",
  "sourceToolAssistantUUID": "a87cb94f-4ec6-4524-919b-11b7d514c176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-18T12:28:22.586Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HLzXUuiSvsqTsU5txsFhqB`</summary>

```json
{
  "query": "pypi flash-linear-attention 0.1 \"Mar 2025\" release history versions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17b4b6d8-8728-4ebb-9d12-f1ef9699a7ba",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2wCooeNET7ag53fych",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d6256dd-bea3-4153-9e95-3d5a5cb7fe46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YQRKgnorS5LeGurPhn8jj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 60262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 282,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 76 · 2026-05-18T12:28:23.378Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015ZRJsYZaqcRCSr4FhGtX8M`</summary>

```json
{
  "url": "https://pypi.org/project/flash-linear-attention/0.1/",
  "prompt": "Show the exact release date and metadata for flash-linear-attention version 0.1. What Python version is required? What are the dependencies?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d6256dd-bea3-4153-9e95-3d5a5cb7fe46",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2wCooeNET7ag53fych",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df41bdb2-cf95-449c-8bc9-e98fb1ca1241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016YQRKgnorS5LeGurPhn8jj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 60262,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 60262,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 282,
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

_source line 77 · 2026-05-18T12:28:26.025Z_

<details><summary>↩ Tool result · `toolu_015ZRJsYZaqcRCSr4FhGtX8M`</summary>

```text
I cannot provide the requested information about flash-linear-attention version 0.1 based on the content provided. The web page shows only an error message stating that "A required part of this site couldn't load," which prevents access to the package metadata, release date, Python version requirements, and dependency information you're asking about.

To find this information, you would need to:
- Resolve the loading issue (check connection, disable ad blockers, try another browser)
- Visit a package repository like PyPI directly
- Check the project's GitHub releases page
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df41bdb2-cf95-449c-8bc9-e98fb1ca1241",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "b1195a41-1282-4905-82ac-bd444769898b",
  "sourceToolAssistantUUID": "df41bdb2-cf95-449c-8bc9-e98fb1ca1241",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-18T12:28:28.274Z_

<details><summary>↩ Tool result · `toolu_01HLzXUuiSvsqTsU5txsFhqB`</summary>

```text
Web search results for query: "pypi flash-linear-attention 0.1 "Mar 2025" release history versions"

Links: [{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"},{"title":"piwheels - flash-linear-attention","url":"https://www.piwheels.org/project/flash-linear-attention/"},{"title":"flash-attn · PyPI","url":"https://pypi.org/project/flash-attn/"},{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"flash-linear-attention/FAQs.md at main · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md"},{"title":"jax-flash-attn2 · PyPI","url":"https://pypi.org/project/jax-flash-attn2/"},{"title":"Releases · Dao-AILab/flash-attention","url":"https://github.com/Dao-AILab/flash-attention/releases"},{"title":"flash-sparse-attn · PyPI","url":"https://pypi.org/project/flash-sparse-attn/"},{"title":"flash-attn 0.2.1","url":"https://pypi.org/project/flash-attn/0.2.1/"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"}]

Based on the search results, I found the release history information for the `flash-linear-attention` package on PyPI.

The flash-linear-attention package has version 0.1 released on Mar 20, 2025, with version 0.1.1 released on Mar 24, 2025, and version 0.1.2 released on Mar 31, 2025.

The complete release timeline from the PyPI page shows these March 2025 releases in the context of the broader version history, which includes earlier and later versions spanning from March 2025 through March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d6256dd-bea3-4153-9e95-3d5a5cb7fe46",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "be014bda-2473-434d-9328-1a6377e36935",
  "sourceToolAssistantUUID": "5d6256dd-bea3-4153-9e95-3d5a5cb7fe46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-18T12:28:32.216Z_

Let me try one more approach to get the specific version info - checking the config path in the model config, which shows `/mnt/bn/ridger1/flame/`, suggesting they used the flame training framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be014bda-2473-434d-9328-1a6377e36935",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2wyzuCZxyy23T6rxBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2fd6d2e-3b9e-4562-801a-436df3913cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqvrRZbyh3c1VPikLcDgNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 150,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 60544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 80 · 2026-05-18T12:28:33.256Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TTPsJsfufFo7TeiiadjdrY`</summary>

```json
{
  "url": "https://github.com/fla-org/flame/blob/main/requirements.txt",
  "prompt": "Show all contents of requirements.txt if it exists."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fd6d2e-3b9e-4562-801a-436df3913cc3",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2wyzuCZxyy23T6rxBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "185741fe-e1a7-412f-8e95-81c4e9e991fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqvrRZbyh3c1VPikLcDgNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 150,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 60544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 776,
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

_source line 81 · 2026-05-18T12:28:33.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WjZgWdKRE4Q1gGuAv22Rb5`</summary>

```json
{
  "query": "\"2507.06457\" \"flash-linear-attention\" version commit OR \"v0.\" reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "185741fe-e1a7-412f-8e95-81c4e9e991fc",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2wyzuCZxyy23T6rxBd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd821a75-38ca-44cd-9db1-5953b9027bbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqvrRZbyh3c1VPikLcDgNW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 150,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 60544,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 150,
          "output_tokens": 201,
          "cache_read_input_tokens": 60544,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 776,
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

_source line 82 · 2026-05-18T12:28:34.044Z_

<details><summary>↩ Tool result · reported error · `toolu_01TTPsJsfufFo7TeiiadjdrY`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "185741fe-e1a7-412f-8e95-81c4e9e991fc",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "e2a5f14f-dea8-4ffb-96e4-8d0d5bf697d8",
  "toolUseResult": "Error: Request failed with status code 404",
  "sourceToolAssistantUUID": "185741fe-e1a7-412f-8e95-81c4e9e991fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-18T12:28:38.426Z_

<details><summary>↩ Tool result · `toolu_01WjZgWdKRE4Q1gGuAv22Rb5`</summary>

```text
Web search results for query: ""2507.06457" "flash-linear-attention" version commit OR "v0." reproducibility"

Links: [{"title":"GitHub - fla-org/flash-linear-attention: 🚀 Efficient implementations for emerging model architectures","url":"https://github.com/fla-org/flash-linear-attention"},{"title":"Releases · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/releases"},{"title":"Releases · Dao-AILab/flash-attention","url":"https://github.com/Dao-AILab/flash-attention/releases"},{"title":"[2507.06457] A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/abs/2507.06457"},{"title":"Commits · fla-org/flash-linear-attention","url":"https://github.com/fla-org/flash-linear-attention/commits/main"},{"title":"GitHub - Fzkuji/flash-linear: 🚀 Efficient implementations of state-of-the-art linear attention models in Pytorch and Triton","url":"https://github.com/Fzkuji/flash-linear-attention"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"Home · fla-org/flash-linear-attention Wiki · GitHub","url":"https://github.com/fla-org/flash-linear-attention/wiki"},{"title":"FLA · GitHub","url":"https://github.com/fla-org"},{"title":"flash-linear-attention · PyPI","url":"https://pypi.org/project/flash-linear-attention/"}]

I found results related to the arXiv paper 2507.06457 "A Systematic Analysis of Hybrid Linear Attention" and the flash-linear-attention repository. The paper trained and open-sourced 72 models: 36 at 340M parameters (20B tokens) and 36 at 1.3B parameters (100B tokens), covering six linear attention variants across five hybridization ratios.

The search returned information about the flash-linear-attention GitHub repository and its releases, but the specific version, commit hash, or "v0." version information related to this paper's reproducibility wasn't clearly displayed in the search results. You may need to check the paper itself or the GitHub repository's releases page directly to find the exact version or commit hash used for the experiments in paper 2507.06457.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd821a75-38ca-44cd-9db1-5953b9027bbd",
  "isSidechain": true,
  "promptId": "2fac6bd4-42e9-4d78-bed4-83bb1e17e82d",
  "agentId": "a4e73858aead4b989",
  "type": "user",
  "uuid": "5cbb97be-0fa8-4d3d-86f9-e4020e5f64d9",
  "sourceToolAssistantUUID": "fd821a75-38ca-44cd-9db1-5953b9027bbd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-18T12:28:59.400Z_

Here is a comprehensive summary of findings.

## Results

**The paper does not specify an exact flash-linear-attention version or commit hash.** Wang et al. (arXiv 2507.06457) only state: "Our model training and inference are both implemented using the flash-linear-attention library" with a link to `https://github.com/fla-org/flash-linear-attention` (reference [45]). No version number, commit hash, requirements file, or reproducibility details are provided in the paper text, appendices, or model cards.

### What I checked:

1. **Full paper HTML** (`https://arxiv.org/html/2507.06457v1`) -- searched every section including appendix. Only mentions "flash-linear-attention library" with the GitHub link. No version specified.

2. **HuggingFace model cards** -- All 62 models in the collection (`https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e`) have "No model card." No README, no requirements.txt.

3. **Model config.json files** (checked `m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1` and `m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1`) -- contain `"transformers_version": "4.49.0"` but no fla version field. The `_name_or_path` field shows `/mnt/bn/ridger1/flame/configs/...`, confirming they used the `fla-org/flame` training framework.

4. **flame training framework** (`https://github.com/fla-org/flame`) -- `pyproject.toml` lists `flash-linear-attention` as a dependency **with no version pin** (just bare `'flash-linear-attention'`). Installs from source via `pip install -U --no-use-pep517 git+https://github.com/fla-org/flash-linear-attention`.

5. **PyPI release history** for `flash-linear-attention`:
   - v0.1: Mar 20, 2025
   - v0.1.1: Mar 24, 2025
   - v0.1.2: Mar 31, 2025
   - v0.2.0: Apr 11, 2025
   - v0.2.1: Apr 23, 2025
   - v0.2.2: Jun 5, 2025
   - v0.3.0: Jul 14, 2025
   - v0.3.1: Aug 26, 2025
   - v0.3.2: Sep 10, 2025
   - v0.4.0: Oct 27, 2025
   - v0.4.1: Dec 24, 2025
   - v0.4.2: Mar 12, 2026
   - v0.5.0: Apr 21, 2026

### Best estimate based on timeline:

The earliest model uploads were **March 3, 2025** (340M models) and **April 20, 2025** (1.3B models). Since the first PyPI release (v0.1) was March 20, 2025, and the earliest models were uploaded March 3, the authors almost certainly used a **pre-release / source install** from the main branch of the GitHub repo, predating the v0.1 PyPI release. The flame framework's install instructions confirm this pattern (install from git, not PyPI).

For the 1.3B models (uploaded April 20, 2025), training would have started well before that date, likely also using a pre-v0.1 or early v0.1.x source install.

**Bottom line: No exact version is documented anywhere. The most likely scenario is a source install from the `main` branch of `https://github.com/fla-org/flash-linear-attention` circa February-March 2025, predating or contemporaneous with the v0.1 release (Mar 20, 2025).**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cbb97be-0fa8-4d3d-86f9-e4020e5f64d9",
  "isSidechain": true,
  "agentId": "a4e73858aead4b989",
  "requestId": "req_011CbA2xjVJJYf2kTjB3moSs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c155626-3f79-4d59-98cc-c37347a69e8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "sessionId": "862a51fb-ad20-4c48-8de6-4985ffc65890",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XbiJoEE4uwaLayHyGsXJD6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1146,
      "cache_read_input_tokens": 61320,
      "output_tokens": 990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 990,
          "cache_read_input_tokens": 61320,
          "cache_creation_input_tokens": 1146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1146,
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
