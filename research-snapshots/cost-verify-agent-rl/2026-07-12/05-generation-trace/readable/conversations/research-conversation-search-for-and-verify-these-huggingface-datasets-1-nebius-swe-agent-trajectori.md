# Research conversation: Search for and verify these HuggingFace datasets: 1. "nebius/SWE-agent-trajectories" — claimed to have 80K+ trajectories

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af53a2a15d5b979eb.jsonl`
- **Structured JSON:** [`d1580154975b5a229c69.json`](../../sessions/d1/d1580154975b5a229c69.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-11T23:34:16.560Z_

Search for and verify these HuggingFace datasets:
1. "nebius/SWE-agent-trajectories" — claimed to have 80K+ trajectories
2. "nebius/SWE-rebench-openhands-trajectories" — claimed to have 67K OpenHands trajectories

Use WebSearch to search for "nebius SWE-agent-trajectories huggingface" and "nebius SWE-rebench-openhands-trajectories huggingface". Also try WebFetch on the HuggingFace dataset pages if you can find URLs. Report:
- Do these datasets exist?
- How many trajectories do they actually contain?
- What format are they in?
- Are they publicly accessible?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "af53a2a15d5b979eb",
  "type": "user",
  "uuid": "153d90aa-fb2b-463a-aeb2-c15f6d9d223d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:34:16.562Z_

```json
{
  "parentUuid": "153d90aa-fb2b-463a-aeb2-c15f6d9d223d",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
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
  "uuid": "4059b88d-564d-4122-98f0-3d6e6b1b214f",
  "timestamp": "2026-05-11T23:34:16.562Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:34:18.632Z_



I'll search for both datasets. Let me start by loading the WebSearch and WebFetch tools, then search for both datasets in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4059b88d-564d-4122-98f0-3d6e6b1b214f",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf4LLpmb6KJ1w4YRdr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9a1dafd-3c33-4a9a-ac7e-072c4fb872a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFULRNAHBqKpGXQW4RteGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 720,
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

_source line 4 · 2026-05-11T23:34:18.931Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0127ysighCVvFbavY3N6GmC1`</summary>

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
  "parentUuid": "c9a1dafd-3c33-4a9a-ac7e-072c4fb872a8",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf4LLpmb6KJ1w4YRdr8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "934aae7d-95ec-444c-959a-e42928c937be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFULRNAHBqKpGXQW4RteGQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 720,
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

### Tool result

_source line 5 · 2026-05-11T23:34:18.935Z_

<details><summary>↩ Tool result · `toolu_0127ysighCVvFbavY3N6GmC1`</summary>

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
  "parentUuid": "934aae7d-95ec-444c-959a-e42928c937be",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "af53a2a15d5b979eb",
  "type": "user",
  "uuid": "eda041d2-66ce-4b1a-b340-8d099d116a97",
  "sourceToolAssistantUUID": "934aae7d-95ec-444c-959a-e42928c937be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:34:23.084Z_



Now let me search for both datasets in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda041d2-66ce-4b1a-b340-8d099d116a97",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf4WhRFqzbkUmiYDG9Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce03f4d1-2604-4fd3-a85d-5e16be645735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7yddiEK1m44Tak8xcyWnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 7 · 2026-05-11T23:34:23.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012iHGjD2DqgGfkRcguT4pNV`</summary>

```json
{
  "query": "nebius SWE-agent-trajectories huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce03f4d1-2604-4fd3-a85d-5e16be645735",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf4WhRFqzbkUmiYDG9Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edf4bc20-f8b0-4e7e-ab6a-07f2c2be7a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7yddiEK1m44Tak8xcyWnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 8 · 2026-05-11T23:34:24.153Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EgQdizxf3RECnUVTinnVtk`</summary>

```json
{
  "query": "nebius SWE-rebench-openhands-trajectories huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edf4bc20-f8b0-4e7e-ab6a-07f2c2be7a7f",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf4WhRFqzbkUmiYDG9Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6456031-bab0-4ddf-bc53-e16fe43e748f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7yddiEK1m44Tak8xcyWnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 8943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 9 · 2026-05-11T23:34:29.907Z_

<details><summary>↩ Tool result · `toolu_012iHGjD2DqgGfkRcguT4pNV`</summary>

```text
Web search results for query: "nebius SWE-agent-trajectories huggingface"

Links: [{"title":"nebius/SWE-agent-trajectories · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nebius/SWE-agent-trajectories"},{"title":"nebius/SWE-rebench-openhands-trajectories · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories"},{"title":"nebius/SWE-agent-trajectories at main","url":"https://huggingface.co/datasets/nebius/SWE-agent-trajectories/tree/main"},{"title":"nebius/SWE-bench-extra · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nebius/SWE-bench-extra"},{"title":"SWE-rebench: A continuously updated benchmark for SWE LLMs","url":"https://nebius.com/blog/posts/introducing-swe-rebench"},{"title":"Scaling data collection for training software engineering agents","url":"https://nebius.com/blog/posts/scaling-data-collection-for-training-swe-agents"},{"title":"nebius/SWE-rebench-openhands-Qwen3-30B-A3B · Hugging Face","url":"https://huggingface.co/nebius/SWE-rebench-openhands-Qwen3-30B-A3B"},{"title":"nebius/SWE-rebench-openhands-Qwen3-235B-A22B · Hugging Face","url":"https://huggingface.co/nebius/SWE-rebench-openhands-Qwen3-235B-A22B"},{"title":"SWE-rebench dataset: More than 21,000 open tasks for SWE LLMs","url":"https://nebius.com/blog/posts/swe-rebench-dataset"},{"title":"VolkerMauel/nebius-SWE-rebench-openhands-Qwen3-30B-A3B-GGUF · Hugging Face","url":"https://huggingface.co/VolkerMauel/nebius-SWE-rebench-openhands-Qwen3-30B-A3B-GGUF"}]

Based on the search results, here's what I found about the nebius SWE-agent-trajectories dataset on Hugging Face:

## Overview
The dataset contains 80,036 trajectories generated by a software engineering agent based on the SWE-agent framework, using various models as action generators. In these trajectories, the agent attempts to solve GitHub issues from the nebius/SWE-bench-extra and the dev split of princeton-nlp/SWE-bench.

## Purpose and Achievement
This dataset was created as part of a research project focused on developing a software engineering agent using open-weight models, which achieved a score of 40.6% on the SWE-bench Verified benchmark.

## Dataset Collection
The dataset collection consisted of two stages: collecting issue-resolution instances, following a methodology similar to SWE-bench, and generating a large number of trajectories for solving the collected issues. The generated code patches in these trajectories were evaluated by the tests from the linked pull requests to determine which of them passed.

## Licensing
The dataset is licensed under the Creative Commons Attribution 4.0 license.

You can access and load the dataset using: `load_dataset('nebius/swe-agent-trajectories')`


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edf4bc20-f8b0-4e7e-ab6a-07f2c2be7a7f",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "af53a2a15d5b979eb",
  "type": "user",
  "uuid": "07ca3520-c93a-42ce-a33a-09a60bf43e66",
  "sourceToolAssistantUUID": "edf4bc20-f8b0-4e7e-ab6a-07f2c2be7a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-11T23:34:29.919Z_

<details><summary>↩ Tool result · `toolu_01EgQdizxf3RECnUVTinnVtk`</summary>

```text
Web search results for query: "nebius SWE-rebench-openhands-trajectories huggingface"

Links: [{"title":"nebius/SWE-rebench-openhands-trajectories · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories"},{"title":"nebius/SWE-rebench-openhands-Qwen3-30B-A3B · Hugging Face","url":"https://huggingface.co/nebius/SWE-rebench-openhands-Qwen3-30B-A3B"},{"title":"nebius/SWE-rebench-openhands-Qwen3-235B-A22B · Hugging Face","url":"https://huggingface.co/nebius/SWE-rebench-openhands-Qwen3-235B-A22B"},{"title":"VolkerMauel/nebius-SWE-rebench-openhands-Qwen3-30B-A3B-GGUF · Hugging Face","url":"https://huggingface.co/VolkerMauel/nebius-SWE-rebench-openhands-Qwen3-30B-A3B-GGUF"},{"title":"SWE-rebench-V2 - a nebius Collection","url":"https://huggingface.co/collections/nebius/swe-rebench-v2"},{"title":"Openhands Trajectories - a nebius Collection","url":"https://huggingface.co/collections/nebius/openhands-trajectories"},{"title":"VolkerMauel/nebius-SWE-rebench-openhands-Qwen3-30B-A3B-GGUF ...","url":"https://socket.dev/huggingface/package/volkermauel/nebius-swe-rebench-openhands-qwen3-30b-a3b-gguf?type=model"},{"title":"nebius/SWE-rebench-openhands-Qwen3-30B-A3B · Exactly what I have been looking for.","url":"https://huggingface.co/nebius/SWE-rebench-openhands-Qwen3-30B-A3B/discussions/1"},{"title":"nebius (Nebius)","url":"https://huggingface.co/nebius/collections"},{"title":"SWE-rebench dataset: More than 21,000 open tasks for SWE LLMs","url":"https://nebius.com/blog/posts/swe-rebench-dataset"}]

Here are the search results for the query "nebius SWE-rebench-openhands-trajectories huggingface":

SWE-rebench-OpenHands-Trajectories is a dataset of multi-turn agent trajectories for software engineering tasks, collected using Qwen/Qwen3-Coder-480B-A35B-Instruct with OpenHands (v0.54.0) agent scaffolding.

The dataset contains 67,074 OpenHands trajectories collected with Qwen3-Coder-480B-A35B-Instruct and includes two RFT (Rejection Sampling Fine-Tuning) checkpoints trained on the data.

One of the resulting models is SWE-rebench-openhands-Qwen3-30B-A3B, a 30B Rejection Sampling Fine-Tuning checkpoint derived from Qwen/Qwen3-30B-A3B-Instruct-2507, trained on the newly released nebius/SWE-rebench-openhands-trajectories dataset.

Similarly, SWE-rebench-openhands-Qwen3-235B-A22B is a 235B Rejection Sampling Fine-Tuning checkpoint derived from Qwen/Qwen3-235B-A22B-Instruct-2507, trained on the nebius/SWE-rebench-openhands-trajectories dataset.

The dataset and models are available on Hugging Face under the Nebius organization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6456031-bab0-4ddf-bc53-e16fe43e748f",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "af53a2a15d5b979eb",
  "type": "user",
  "uuid": "cb3987fe-6b43-4108-a83a-b7832f0f5dfd",
  "sourceToolAssistantUUID": "e6456031-bab0-4ddf-bc53-e16fe43e748f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-11T23:34:32.491Z_

Both datasets exist. Now let me fetch the actual HuggingFace dataset pages to get more detailed information about format, exact counts, and accessibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3987fe-6b43-4108-a83a-b7832f0f5dfd",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf5KSHKd8KiFa6EcpQg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b9cff89-debb-4d91-ab47-10ee58a23957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFcZtUb8PDapFZ79MNM25t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2124,
      "cache_read_input_tokens": 10862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2124,
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

_source line 12 · 2026-05-11T23:34:35.014Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WXkSkEUWYkHwVVhsWuHfx3`</summary>

```json
{
  "url": "https://huggingface.co/datasets/nebius/SWE-agent-trajectories",
  "prompt": "Extract all details about this dataset: exact number of trajectories/rows, data format (parquet, json, etc.), columns/fields, size on disk, license, whether it's publicly accessible or gated, and any description of what the trajectories contain."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b9cff89-debb-4d91-ab47-10ee58a23957",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf5KSHKd8KiFa6EcpQg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e13e346-a462-4e9e-8760-46c2b83606f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFcZtUb8PDapFZ79MNM25t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2124,
      "cache_read_input_tokens": 10862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2124,
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

_source line 13 · 2026-05-11T23:34:36.079Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VuorMEk2oWeUVXyZViXzXP`</summary>

```json
{
  "url": "https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories",
  "prompt": "Extract all details about this dataset: exact number of trajectories/rows, data format (parquet, json, etc.), columns/fields, size on disk, license, whether it's publicly accessible or gated, and any description of what the trajectories contain."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e13e346-a462-4e9e-8760-46c2b83606f0",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf5KSHKd8KiFa6EcpQg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91118e74-27b6-4146-b635-68e7f4b20c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFcZtUb8PDapFZ79MNM25t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2124,
      "cache_read_input_tokens": 10862,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2124
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 10862,
          "cache_creation_input_tokens": 2124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2124,
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

_source line 14 · 2026-05-11T23:34:40.784Z_

<details><summary>↩ Tool result · `toolu_01WXkSkEUWYkHwVVhsWuHfx3`</summary>

````text
# SWE-agent-trajectories Dataset Details

## Basic Information
- **Exact number of trajectories/rows:** 80,036
- **Data format:** Parquet
- **Total file size on disk:** 1.11 GB
- **License:** CC-BY-4.0 (Creative Commons Attribution 4.0)
- **Public accessibility:** Publicly accessible (no gating mentioned)

## Dataset Structure & Columns

The dataset contains the following fields:

| Field Name | Type | Description |
|---|---|---|
| `instance_id` | str | Repository name + issue number identifier |
| `model_name` | stringclasses (3 values) | Name of the model used to generate the trajectory |
| `target` | bool | Whether the model successfully solved the issue |
| `trajectory` | list (2-817 items) | JSON list of model reasoning/actions and environment observations |
| `exit_status` | stringclasses (9 values) | Agent completion status |
| `generated_patch` | str | Final code patch generated (1-1.86M chars) |
| `eval_logs` | str | Test execution logs verifying the patch |

## Trajectory Content

Each trajectory contains:
- **System prompt** defining the agent as an autonomous programmer with file editor interface
- **Model reasoning and actions** (role: "ai")
- **Environment observations** (role: "user")
- **Code diffs** showing file modifications
- **Test execution results** confirming patch validity

## Usage Example

```python
from datasets import load_dataset
ds = load_dataset('nebius/SWE-agent-trajectories')
```

## Key Statistics
- **Resolved issues:** 13,389 instances (16.7%)
- **Unresolved issues:** 66,647 instances (83.3%)
- **Average steps:** 31.3 (resolved) vs 58.4 (unresolved)
- **Models used:** Multiple (3 model classes, including swe-agent-llama-70b)
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e13e346-a462-4e9e-8760-46c2b83606f0",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "af53a2a15d5b979eb",
  "type": "user",
  "uuid": "1246ddad-9113-4ded-8391-1999d1cd9505",
  "sourceToolAssistantUUID": "5e13e346-a462-4e9e-8760-46c2b83606f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-11T23:34:44.329Z_

<details><summary>↩ Tool result · `toolu_01VuorMEk2oWeUVXyZViXzXP`</summary>

````text
# SWE-rebench-OpenHands-Trajectories Dataset Details

## Dataset Overview
- **Name**: nebius/SWE-rebench-openhands-trajectories
- **Source**: Hugging Face Datasets
- **License**: CC-BY-4.0
- **Accessibility**: Public (no gating mentioned)

## Trajectories & Rows
- **Total Trajectories**: 67,074
- **Total Rows**: 67,1k
- **Successful Trajectories**: 32,161
- **Average Turns per Trajectory**: 64.3
- **Max Turns**: 100

## Data Format & Size
- **Format**: Parquet (auto-converted from original format)
- **Disk Size**: 2.08 GB
- **Additional Formats**: pandas, Polars compatible

## Dataset Structure & Columns

| Field Name | Type | Description |
|---|---|---|
| `trajectory_id` | `str` | Unique identifier for each trajectory |
| `instance_id` | `str` | GitHub issue identifier (repo name + issue number) |
| `repo` | `str` | Repository identifier |
| `trajectory` | `list` | Complete conversation history with roles: `system`, `assistant`, `user`, `tool` |
| `tools` | `list` | Available tools/functions for the agent |
| `model_patch` | `str` | Final code modifications in unified diff format |
| `exit_status` | `str` | `'submit'` or error message |
| `resolved` | `int64` | Binary indicator (1 = solved, 0 = not solved) |
| `gen_tests_correct` | `float64` | Number of agent-generated tests that validate the solution |
| `pred_passes_gen_tests` | `float64` | Agent-generated tests passed by the agent's solution |

## Data Content
The trajectories contain:
- **Multi-turn agent interactions** using OpenHands (v0.54.0) scaffolding
- **Bootstrapping Model**: Qwen3-Coder-480B-A35B-Instruct
- **Real GitHub Issues**: From 1,823 repositories in nebius/SWE-rebench
- **Complete execution traces** with agent reasoning, actions, and environmental observations
- **Tool calls with arguments** (serialized as strings for storage efficiency)

## Loading the Dataset

```python
from datasets import load_dataset

ds = load_dataset("nebius/SWE-rebench-openhands-trajectories", split="train")
```

## Key Features
✅ Uses function calling capabilities  
✅ 67,074 total trajectories across 1,823 repositories  
✅ Includes evaluation metrics for agent-generated tests (unique feature)  
✅ Real-world GitHub issues  
✅ Complete conversation history with tool interactions
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91118e74-27b6-4146-b635-68e7f4b20c53",
  "isSidechain": true,
  "promptId": "86404765-12d4-410b-a2f3-5b1aec2d05d4",
  "agentId": "af53a2a15d5b979eb",
  "type": "user",
  "uuid": "2fec32b5-b1f3-423d-a307-e62a7ee9be3f",
  "sourceToolAssistantUUID": "91118e74-27b6-4146-b635-68e7f4b20c53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-11T23:35:04.108Z_

Here are the findings for both datasets:

---

## 1. nebius/SWE-agent-trajectories

- **Exists:** Yes, confirmed at `https://huggingface.co/datasets/nebius/SWE-agent-trajectories`
- **Publicly accessible:** Yes, no gating. Licensed under CC-BY-4.0.
- **Trajectory count:** **80,036** -- the "80K+" claim is accurate.
- **Format:** Parquet, 1.11 GB total.
- **Key fields:** `instance_id`, `model_name` (3 model classes including swe-agent-llama-70b), `target` (boolean for success), `trajectory` (list of 2-817 items containing agent reasoning/actions and environment observations), `exit_status`, `generated_patch`, and `eval_logs`.
- **Resolution rate:** 13,389 resolved (16.7%) vs 66,647 unresolved (83.3%). Average steps: 31.3 for resolved, 58.4 for unresolved.
- **Context:** Created as part of research on developing a SWE agent using open-weight models, which achieved 40.6% on SWE-bench Verified. Trajectories are from solving GitHub issues in nebius/SWE-bench-extra and the dev split of princeton-nlp/SWE-bench.

## 2. nebius/SWE-rebench-openhands-trajectories

- **Exists:** Yes, confirmed at `https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories`
- **Publicly accessible:** Yes, no gating. Licensed under CC-BY-4.0.
- **Trajectory count:** **67,074** -- the "67K" claim is accurate.
- **Format:** Parquet, 2.08 GB total.
- **Key fields:** `trajectory_id`, `instance_id`, `repo`, `trajectory` (multi-turn conversation with system/assistant/user/tool roles), `tools` (available functions), `model_patch` (unified diff), `exit_status`, `resolved` (binary), `gen_tests_correct`, and `pred_passes_gen_tests`.
- **Resolution rate:** 32,161 successful trajectories out of 67,074 (approximately 48%). Average turns per trajectory: 64.3, max 100 turns.
- **Context:** Collected using Qwen3-Coder-480B-A35B-Instruct with OpenHands v0.54.0 agent scaffolding, spanning 1,823 repositories from nebius/SWE-rebench. Two RFT (Rejection Sampling Fine-Tuning) model checkpoints have been trained on this data: Qwen3-30B-A3B and Qwen3-235B-A22B variants.

## Summary

Both datasets exist, are publicly accessible under CC-BY-4.0, stored in Parquet format, and the claimed trajectory counts are accurate (80,036 and 67,074 respectively). The first dataset uses a SWE-agent framework with multiple models, while the second uses the OpenHands framework with Qwen3-Coder. A notable difference is that the OpenHands trajectories include function-calling-style tool interactions and agent-generated test metrics, while the SWE-agent trajectories follow a more traditional reasoning/action/observation format.

Sources:
- [nebius/SWE-agent-trajectories on Hugging Face](https://huggingface.co/datasets/nebius/SWE-agent-trajectories)
- [nebius/SWE-rebench-openhands-trajectories on Hugging Face](https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories)
- [Nebius blog: Scaling data collection for training SWE agents](https://nebius.com/blog/posts/scaling-data-collection-for-training-swe-agents)
- [Nebius blog: SWE-rebench dataset](https://nebius.com/blog/posts/swe-rebench-dataset)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fec32b5-b1f3-423d-a307-e62a7ee9be3f",
  "isSidechain": true,
  "agentId": "af53a2a15d5b979eb",
  "requestId": "req_011Cawf6P566YAUCYNQX39k1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "375fc40f-eb69-4e4a-9a25-b9d7a8b8e5b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "77834f36-f8b9-40d3-89b9-c8bc3de789c7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178tmqdDSaDGRE5Rbxgtg2P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 12986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1511,
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
