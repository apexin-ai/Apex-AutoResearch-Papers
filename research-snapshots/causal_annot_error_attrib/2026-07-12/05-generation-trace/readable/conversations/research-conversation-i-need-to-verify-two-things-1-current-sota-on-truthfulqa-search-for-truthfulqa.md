# Research conversation: I need to verify two things: 1. **Current SOTA on TruthfulQA**: Search for "TruthfulQA leaderboard 2026" and "TruthfulQA

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0e768b54608f18ff.jsonl`
- **Structured JSON:** [`69a27d5902a21b8bd1eb.json`](../../sessions/69/69a27d5902a21b8bd1eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-16T09:32:10.116Z_

I need to verify two things:

1. **Current SOTA on TruthfulQA**: Search for "TruthfulQA leaderboard 2026" and "TruthfulQA state of the art" on Papers With Code and other sources. What are the best methods and their scores (MC1, MC2, True+Info)?

2. **ESR (Endogenous Steering Resistance) details at different scales**: Search for "endogenous steering resistance language models arXiv 2602.06941" and use WebFetch to read https://arxiv.org/abs/2602.06941. I specifically need:
   - What is the ESR rate at 8B scale vs 70B scale?
   - Does the paper provide specific numbers for different model sizes?
   - What is the precise claim about ESR circuits?

3. Search for "PC-LDCD hallucination detection code" and check if the anonymous code at anonymous.4open.science/r/PC-LDCD-63D5 is actually accessible.

Report with specific numbers and citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "f5102b4c-069c-4b83-b370-a667959124a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T09:32:10.118Z_

```json
{
  "parentUuid": "f5102b4c-069c-4b83-b370-a667959124a2",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
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
  "uuid": "38c88596-3f8e-4db9-948e-b1a7d6d885be",
  "timestamp": "2026-05-16T09:32:10.118Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T09:32:13.806Z_



I'll tackle all three research tasks in parallel. Let me start by loading the WebSearch and WebFetch tools, then execute the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c88596-3f8e-4db9-948e-b1a7d6d885be",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tPcipNFc7jW5VJP3D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78857f1b-d353-460b-b6ea-7d2ff6f767c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYWErftr5HyaVedqbcE7bY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 793,
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

_source line 4 · 2026-05-16T09:32:13.910Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YbEsLqm1k5z85yS5SqfUgr`</summary>

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
  "parentUuid": "78857f1b-d353-460b-b6ea-7d2ff6f767c0",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tPcipNFc7jW5VJP3D",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a67c56b8-e71f-4bd9-bef1-41009801dd9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYWErftr5HyaVedqbcE7bY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 8223,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 793
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 793,
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

_source line 5 · 2026-05-16T09:32:13.913Z_

<details><summary>↩ Tool result · `toolu_01YbEsLqm1k5z85yS5SqfUgr`</summary>

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
  "parentUuid": "a67c56b8-e71f-4bd9-bef1-41009801dd9b",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "b3ba9ad1-709a-4453-b536-a89209440503",
  "sourceToolAssistantUUID": "a67c56b8-e71f-4bd9-bef1-41009801dd9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-16T09:32:17.305Z_



Now let me execute all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3ba9ad1-709a-4453-b536-a89209440503",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tg7QM1sXNpLyVL4EQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63a46c88-97f7-415a-8eeb-0833d4575ce4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADeoVUshLPgoLSaoTkF3BS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 7 · 2026-05-16T09:32:17.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SrQTmi6wa59rsyTq4Rhxg1`</summary>

```json
{
  "query": "TruthfulQA leaderboard 2026 state of the art MC1 MC2 scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63a46c88-97f7-415a-8eeb-0833d4575ce4",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tg7QM1sXNpLyVL4EQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d90ca069-ec4e-4744-ab90-ca7488ef0a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADeoVUshLPgoLSaoTkF3BS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 8 · 2026-05-16T09:32:18.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0172ZdPMwStcB4VB64Qf6Ni7`</summary>

```json
{
  "query": "TruthfulQA state of the art Papers With Code best methods 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d90ca069-ec4e-4744-ab90-ca7488ef0a1f",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tg7QM1sXNpLyVL4EQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67621945-e976-41e6-b065-ef2a4196e1be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADeoVUshLPgoLSaoTkF3BS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 9 · 2026-05-16T09:32:18.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015taQH4pdDi5ss4XHdd8dRY`</summary>

```json
{
  "query": "endogenous steering resistance language models arXiv 2602.06941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67621945-e976-41e6-b065-ef2a4196e1be",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tg7QM1sXNpLyVL4EQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1341f04c-1d76-4e8e-aae8-54ad92dc97fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADeoVUshLPgoLSaoTkF3BS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 10 · 2026-05-16T09:32:20.184Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011Ku48Y37EhxYdNQUZHFvnD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.06941",
  "prompt": "Extract all details about ESR (Endogenous Steering Resistance) including: 1) ESR rate at 8B scale vs 70B scale, 2) specific numbers for different model sizes, 3) the precise claim about ESR circuits. Include all quantitative results and model size comparisons."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1341f04c-1d76-4e8e-aae8-54ad92dc97fe",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tg7QM1sXNpLyVL4EQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71a7f9ab-1bd5-40ad-bd79-0415a870edb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADeoVUshLPgoLSaoTkF3BS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 11 · 2026-05-16T09:32:20.774Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MLMYS91rSsuy5nHkMVeYUY`</summary>

```json
{
  "query": "PC-LDCD hallucination detection code anonymous.4open.science"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71a7f9ab-1bd5-40ad-bd79-0415a870edb6",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tg7QM1sXNpLyVL4EQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcc25bf7-4e26-4050-9648-5dfdfa5267b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADeoVUshLPgoLSaoTkF3BS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 12 · 2026-05-16T09:32:21.745Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018q5PAoBFh1KPfcdUDwWLBr`</summary>

```json
{
  "url": "https://anonymous.4open.science/r/PC-LDCD-63D5",
  "prompt": "Is this repository accessible? What does it contain? List the files, README content, and any description of the PC-LDCD hallucination detection method."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcc25bf7-4e26-4050-9648-5dfdfa5267b7",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61tg7QM1sXNpLyVL4EQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ced9093-7709-483e-8f39-c2e96a55aa8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ADeoVUshLPgoLSaoTkF3BS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9016,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 9016,
          "cache_creation_input_tokens": 1919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1919,
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

_source line 13 · 2026-05-16T09:32:21.994Z_

<details><summary>↩ Tool result · reported error · `toolu_018q5PAoBFh1KPfcdUDwWLBr`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ced9093-7709-483e-8f39-c2e96a55aa8b",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "897dfe83-a902-481e-8f11-595678a8d74b",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "1ced9093-7709-483e-8f39-c2e96a55aa8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:32:23.677Z_

<details><summary>↩ Tool result · `toolu_01SrQTmi6wa59rsyTq4Rhxg1`</summary>

```text
Web search results for query: "TruthfulQA leaderboard 2026 state of the art MC1 MC2 scores"

Links: [{"title":"open-llm-leaderboard/open_llm_leaderboard · what kind of task does TruthfulQA eval? mc1? mc2? or both?","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/95"},{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"TruthfulQA Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/truthfulqa"},{"title":"TruthfulQA | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-truthful-qa"},{"title":"HuggingFaceH4/open_llm_leaderboard · what kind of task does TruthfulQA eval? mc1? mc2? or both?","url":"https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard/discussions/95"},{"title":"CollectiveCognition-v1.1-Mistral-7B","url":"https://www.promptlayer.com/models/collectivecognition-v11-mistral-7b"},{"title":"New, improved multiple-choice TruthfulQA","url":"https://www.lesswrong.com/posts/Bunfwz6JsNd44kgLT/new-improved-multiple-choice-truthfulqa"},{"title":"TruthfulQA: Benchmark for Evaluating Language | Kaggle","url":"https://www.kaggle.com/datasets/thedevastator/truthfulqa-benchmark-for-evaluating-language-mod"},{"title":"Gaming TruthfulQA: Simple Heuristics Exposed Dataset Weaknesses","url":"https://turntrout.com/original-truthfulqa-weaknesses"},{"title":"New, improved multiple-choice TruthfulQA | TruthfulAI","url":"https://truthful.ai/blog/truthfulqa-binary-choice/"}]

I found some information about TruthfulQA, but the search results don't contain a specific 2026 leaderboard with state-of-the-art MC1 and MC2 scores. However, I can provide you with some relevant context:

**About TruthfulQA Scores:**

MC1 involves selecting the only correct answer from 4-5 answer choices, with the score being simple accuracy across all questions. MC2 scores are calculated as the normalized total probability assigned to the set of true answers.

**Recent Model Performance Example:**

One example of recent performance metrics comes from a specific model: CollectiveCognition-v1.1-Mistral-7B achieved MC1 score of 0.4051 and MC2 score of 0.5738 on the TruthfulQA benchmark.

**Current Leaderboard Resources:**

There is a TruthfulQA benchmark leaderboard with 17 models evaluated, where you can compare scores, rankings, and performance metrics.

For the most current 2026 leaderboard with state-of-the-art scores, I'd recommend checking the official sources directly:
- The [TruthfulQA GitHub repository](https://github.com/sylinrl/TruthfulQA)
- The [llm-stats.com leaderboard](https://llm-stats.com/benchmarks/truthfulqa)

Would you like me to search for more specific recent model results?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d90ca069-ec4e-4744-ab90-ca7488ef0a1f",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "df6faf51-6742-43c3-b1d6-1ecfe2ddb4d9",
  "sourceToolAssistantUUID": "d90ca069-ec4e-4744-ab90-ca7488ef0a1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T09:32:24.672Z_

<details><summary>↩ Tool result · `toolu_015taQH4pdDi5ss4XHdd8dRY`</summary>

```text
Web search results for query: "endogenous steering resistance language models arXiv 2602.06941"

Links: [{"title":"[2602.06941] Endogenous Resistance to Activation Steering in Language Models","url":"https://arxiv.org/abs/2602.06941"},{"title":"Endogenous Resistance to Activation Steering in Language Models","url":"https://arxiv.org/html/2602.06941v1"},{"title":"[2602.17881] Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations","url":"https://arxiv.org/abs/2602.17881"},{"title":"[2602.02343] Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics","url":"https://arxiv.org/abs/2602.02343"},{"title":"Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics","url":"https://arxiv.org/html/2602.02343"},{"title":"[2602.01716] Mechanistic Indicators of Steering Effectiveness in Large Language Models","url":"https://arxiv.org/abs/2602.01716"},{"title":"[2602.00333] Efficient and accurate steering of Large Language Models through attention-guided feature learning","url":"https://arxiv.org/abs/2602.00333"},{"title":"Steering off Course: Reliability Challenges in Steering Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250404635Q/abstract"},{"title":"Understanding (Un)Reliability of Steering Vectors in Language Models","url":"https://arxiv.org/html/2505.22637v1"},{"title":"[2602.08440] SteerVLA: Steering Vision-Language-Action Models in Long-Tail Driving Scenarios","url":"https://arxiv.org/abs/2602.08440"}]

I found the paper for you! Here's what I found:

The paper describes how large language models can resist task-misaligned activation steering during inference, sometimes recovering mid-generation to produce improved responses even when steering remains active. This phenomenon is termed Endogenous Steering Resistance (ESR).

**Key Findings:**

Using sparse autoencoder (SAE) latents to steer model activations, the researchers found that Llama-3.3-70B shows substantial ESR, while smaller models from the Llama-3 and Gemma-2 families exhibit the phenomenon less frequently.

The researchers identified 26 SAE latents that activate differentially during off-topic content and are causally linked to ESR in Llama-3.3-70B. Zero-ablating these latents reduces the multi-attempt rate by 25%, providing causal evidence for dedicated internal consistency-checking circuits.

The researchers demonstrated that ESR can be deliberately enhanced through both prompting and training: meta-prompts instructing the model to self-monitor increase the multi-attempt rate by 4x for Llama-3.3-70B, and fine-tuning on self-correction examples successfully induces ESR.

The paper was submitted on February 6, 2026 and was authored by Alex McKenzie, Keenan Pepper, Stijn Servaes, and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1341f04c-1d76-4e8e-aae8-54ad92dc97fe",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "5e8d18fa-8293-4c9e-89d4-d6e9a3c5e09a",
  "sourceToolAssistantUUID": "1341f04c-1d76-4e8e-aae8-54ad92dc97fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:32:24.909Z_

<details><summary>↩ Tool result · `toolu_011Ku48Y37EhxYdNQUZHFvnD`</summary>

```text
# Endogenous Steering Resistance (ESR) - Key Findings

## Model Scale Comparison
The paper reveals a clear scaling pattern: **Llama-3.3-70B demonstrates substantial ESR**, while **smaller models from Llama-3 and Gemma-2 families exhibit the phenomenon less frequently**. However, the abstract does not provide specific ESR rates for 8B models versus 70B models.

## Quantitative Results
The research identified concrete numbers:
- **26 SAE latents** causally linked to ESR in Llama-3.3-70B
- **Zero-ablating these latents reduced the multi-attempt rate by 25%**, demonstrating causal evidence for resistance mechanisms
- **Meta-prompting increased the multi-attempt rate by 4x** for Llama-3.3-70B

## ESR Circuits
The precise claim states: "dedicated internal consistency-checking circuits" operate within the model. The evidence comes from the finding that specific latents "activate differentially during off-topic content" and are causally linked to ESR, supporting the hypothesis that models have built-in mechanisms to detect and resist task-misaligned steering.

## Enhancement Methods
ESR can be deliberately amplified through prompting and fine-tuning, with fine-tuning successfully inducing ESR-like behavior in smaller models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71a7f9ab-1bd5-40ad-bd79-0415a870edb6",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "a992c231-ead0-450c-ab33-2f313a915c5c",
  "sourceToolAssistantUUID": "71a7f9ab-1bd5-40ad-bd79-0415a870edb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T09:32:26.417Z_

<details><summary>↩ Tool result · `toolu_01MLMYS91rSsuy5nHkMVeYUY`</summary>

```text
Web search results for query: "PC-LDCD hallucination detection code anonymous.4open.science"

Links: [{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Decoding Memories: An Efficient Pipeline for Self-Consistency Hallucination Detection","url":"https://arxiv.org/html/2508.21228"},{"title":"4open.science | 4open-science.github.io","url":"https://4open.science/"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"[2605.07209] Hallucination Detection via Activations of Open-Weight Proxy Analyzers","url":"https://arxiv.org/abs/2605.07209"},{"title":"The Hallucinations Leaderboard, an Open Effort to Measure Hallucinations in Large Language Models","url":"https://huggingface.co/blog/leaderboard-hallucinations"},{"title":"Hallucination Detection - OpenAI Guardrails Python","url":"https://openai.github.io/openai-guardrails-python/ref/checks/hallucination_detection/"},{"title":"New tool, dataset help detect hallucinations in large language models - Amazon Science","url":"https://www.amazon.science/blog/new-tool-dataset-help-detect-hallucinations-in-large-language-models"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v1"}]

Based on the search results, I found information about PC-LDCD:

PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding) is triggered only when the latent geometry deviates from factual regions, while leaving correct generations untouched.

The method uses PCNet, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream, which detects hallucinations as geometric anomalies on the factual manifold via exact Negative Log-Likelihood computation, without needing sampling, external verifiers, or weight modifications.

Across four LLMs ranging from 1B to 8B models and four benchmarks covering conversational reasoning, knowledge-intensive QA, reading comprehension, and truthfulness, PCNet achieves near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%.

The proposed method is publicly available on GitHub at https://anonymous.4open.science/r/PC-LDCD-63D5. The anonymous.4open.science link anonymizes Github repositories prior to double blind reviewing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcc25bf7-4e26-4050-9648-5dfdfa5267b7",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "05f781ac-7b84-48ed-98b1-982213214434",
  "sourceToolAssistantUUID": "bcc25bf7-4e26-4050-9648-5dfdfa5267b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:32:34.794Z_

<details><summary>↩ Tool result · `toolu_0172ZdPMwStcB4VB64Qf6Ni7`</summary>

```text
Web search results for query: "TruthfulQA state of the art Papers With Code best methods 2025 2026"

Links: [{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"TruthfulQA Benchmark (Question Answering)","url":"https://paperswithcode.com/sota/question-answering-on-truthfulqa"},{"title":"[2109.07958] TruthfulQA: Measuring How Models Mimic Human Falsehoods","url":"https://arxiv.org/abs/2109.07958"},{"title":"TruthfulQA Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/truthfulqa"},{"title":"arXiv:2502.09387v3 [cs.CL] 16 Jun 2025","url":"https://arxiv.org/pdf/2502.09387"},{"title":"On LLMs’ Internal Representation of Code Correctness","url":"https://arxiv.org/html/2512.07404v2"},{"title":"[2502.09387] Truth Knows No Language: Evaluating Truthfulness Beyond English","url":"https://arxiv.org/abs/2502.09387"},{"title":"TruthfulQA: Measuring factual accuracy","url":"https://www.statsig.com/perspectives/truthfulqameasuringaccuracy"},{"title":"TruthfulQA: Measuring How Models Mimic Human Falsehoods Stephanie Lin","url":"https://owainevans.github.io/pdfs/truthfulQA_lin_evans.pdf"},{"title":"Papers with Code Shutdown 2025: Best API and SOTA Alternatives | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/papers-with-code"}]

Based on the search results, here's what I found about TruthfulQA state-of-the-art methods:

## Current State-of-the-Art Results

Phi-3.5-MoE-instruct from Microsoft currently leads the TruthfulQA leaderboard with a score of 0.775. Phi-3.5-MoE-instruct leads with 77.5%, followed by Granite 3.3 8B Instruct at 66.9% and Phi 4 Mini at 66.4%.

## Important Note About Papers With Code

It's worth noting that Papers with Code was shut down by Meta in July 2025. The 9,327 benchmark leaderboards, 79,817 paper-to-code linkages and 5,628 datasets that had been tracked were no longer served from the canonical URL.

## Recent Research (2025-2026)

Recent research on TruthfulQA includes:

- A professionally translated extension of TruthfulQA designed to evaluate truthfulness in Basque, Catalan, Galician, and Spanish, evaluating 12 state-of-the-art open LLMs with human evaluation, multiple-choice metrics, and LLM-as-a-Judge scoring.

- Findings show that LLM-as-a-Judge correlates more closely with human judgments than multiple-choice metrics, and informativeness plays a critical role in truthfulness assessment.

The benchmark itself continues to be widely used for evaluating language model truthfulness, though the original Papers With Code platform is no longer available as a centralized resource.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67621945-e976-41e6-b065-ef2a4196e1be",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "2a9af7be-1bae-4099-841b-6a8b4450cb64",
  "sourceToolAssistantUUID": "67621945-e976-41e6-b065-ef2a4196e1be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T09:32:38.513Z_

Let me fetch more detailed information on the TruthfulQA leaderboard and the ESR paper's full text for specific numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a9af7be-1bae-4099-841b-6a8b4450cb64",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61vD9V4i9Ai28q6iCZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "406f08b4-f539-460c-a181-ccbdf1a019e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fmfurrTYsUB3QjbhcRGPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1984,
      "cache_creation_input_tokens": 2342,
      "cache_read_input_tokens": 10935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2342,
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

_source line 20 · 2026-05-16T09:32:39.971Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RUCyMg9mnMh6G6a3YYi1mQ`</summary>

```json
{
  "url": "https://llm-stats.com/benchmarks/truthfulqa",
  "prompt": "Extract all model names and their TruthfulQA scores (MC1, MC2, True+Info). List the top performing models with their exact scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "406f08b4-f539-460c-a181-ccbdf1a019e7",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61vD9V4i9Ai28q6iCZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07e577dd-9f3f-4261-8d4f-a7c7df7780a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fmfurrTYsUB3QjbhcRGPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1984,
      "cache_creation_input_tokens": 2342,
      "cache_read_input_tokens": 10935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2342,
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

_source line 21 · 2026-05-16T09:32:42.946Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013CorcDi15up2zsjEPpZD7s`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.06941v1",
  "prompt": "Extract ALL quantitative ESR results by model size. Specifically: 1) What is the exact ESR rate or multi-attempt rate for 8B models vs 70B models? 2) What are the specific percentages or numbers for Llama-3-8B, Llama-3.1-8B, Gemma-2-9B, Gemma-2-27B, Llama-3.3-70B? 3) What is the precise definition and measurement of ESR? 4) Any tables with model-size-specific results. Include all numbers you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07e577dd-9f3f-4261-8d4f-a7c7df7780a4",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61vD9V4i9Ai28q6iCZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "951ef3f4-e297-4959-a915-fc98f54881e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fmfurrTYsUB3QjbhcRGPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1984,
      "cache_creation_input_tokens": 2342,
      "cache_read_input_tokens": 10935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2342,
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

_source line 22 · 2026-05-16T09:32:43.827Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017LNrk2LkkF5BU6Vs9A6gQX`</summary>

```json
{
  "url": "https://anonymous.4open.science/r/PC-LDCD-63D5",
  "prompt": "Check if the repository is accessible. List the files present, any README content, and the structure of the code repository."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "951ef3f4-e297-4959-a915-fc98f54881e7",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61vD9V4i9Ai28q6iCZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3e22734-3957-489a-88bb-449b551dd51a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fmfurrTYsUB3QjbhcRGPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1984,
      "cache_creation_input_tokens": 2342,
      "cache_read_input_tokens": 10935,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2342,
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

_source line 23 · 2026-05-16T09:32:43.851Z_

<details><summary>↩ Tool result · reported error · `toolu_017LNrk2LkkF5BU6Vs9A6gQX`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3e22734-3957-489a-88bb-449b551dd51a",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "44094d8b-97ef-4191-969c-766d2bee5e54",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "b3e22734-3957-489a-88bb-449b551dd51a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T09:32:44.229Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BV2WoepAkgizRNFu3KjFie`</summary>

```json
{
  "query": "TruthfulQA MC1 MC2 best scores 2025 2026 GPT-4 Claude LLaMA leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44094d8b-97ef-4191-969c-766d2bee5e54",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61vD9V4i9Ai28q6iCZH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e918e6e8-dfec-4dd8-9094-ff7036232645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fmfurrTYsUB3QjbhcRGPY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1984,
      "cache_creation_input_tokens": 2342,
      "cache_read_input_tokens": 10935,
      "output_tokens": 509,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2342
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1984,
          "output_tokens": 509,
          "cache_read_input_tokens": 10935,
          "cache_creation_input_tokens": 2342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2342,
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

_source line 25 · 2026-05-16T09:32:45.178Z_

<details><summary>↩ Tool result · `toolu_01RUCyMg9mnMh6G6a3YYi1mQ`</summary>

```text
# TruthfulQA Leaderboard Results

Based on the leaderboard data provided, here are the evaluated models and their scores:

## Top Performing Models

1. **Phi-3.5-MoE-instruct** (Microsoft) - 0.775
2. **Granite 3.3 8B Instruct** (IBM) - 0.669
3. **Phi 4 Mini** (Microsoft) - 0.664
4. **Phi-3.5-mini-instruct** (Microsoft) - 0.640
5. **Hermes 3 70B** (Nous Research) - 0.633

## All 17 Evaluated Models

The complete leaderboard includes models from Microsoft, IBM, NVIDIA, Alibaba Cloud/Qwen, AI21 Labs, Cohere, and Mistral AI, with scores ranging from 0.775 down to 0.503 (Mistral NeMo Instruct at rank 17).

**Note:** The webpage provides only overall benchmark scores, not the individual MC1, MC2, or True+Info subscores you requested. The benchmark comprises "817 questions that span 38 categories, including health, law, finance and politics," designed to evaluate whether models avoid generating false answers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07e577dd-9f3f-4261-8d4f-a7c7df7780a4",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "ddde3871-7210-4180-8b2e-67e5852a1a8e",
  "sourceToolAssistantUUID": "07e577dd-9f3f-4261-8d4f-a7c7df7780a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T09:32:50.658Z_

<details><summary>↩ Tool result · `toolu_013CorcDi15up2zsjEPpZD7s`</summary>

```text
# ESR Results by Model Size

## Exact ESR Rates and Multi-Attempt Rates

**70B Model:**
- Llama-3.3-70B: 3.8% ESR rate, 7.4% multi-attempt rate

**Smaller Models (all ≤1% ESR):**
- Llama-3.1-8B: <1% ESR rate, ≤1.2% multi-attempt rate
- Gemma-2-27B: <1% ESR rate
- Gemma-2-9B: <1% ESR rate
- Gemma-2-2B: <1% ESR rate

## ESR Definition and Measurement

The paper defines ESR as "inference-time recovery from irrelevant activation steering." More specifically, it represents "the percentage of responses containing multiple attempts that successfully improve on the first attempt."

The measurement involves two components:
- **Multi-attempt rate**: percentage of responses with explicit self-correction phrases
- **Improvement rate**: percentage of multi-attempt responses where later attempts scored higher

## Key Quantitative Findings

Under meta-prompting conditions, Llama-3.3-70B showed dramatic increases:
- Multi-attempt rate: "4.3× increase (from 7.4% to 31.7%)"
- ESR rate: "3.9× increase (from 3.8% to 14.8%)"

The ablation study revealed that zeroing off-topic detector latents reduced the multi-attempt rate by 25% in the 70B model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "951ef3f4-e297-4959-a915-fc98f54881e7",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "28f7f28e-292d-44f0-8a3d-38608067720f",
  "sourceToolAssistantUUID": "951ef3f4-e297-4959-a915-fc98f54881e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T09:32:51.152Z_

<details><summary>↩ Tool result · `toolu_01BV2WoepAkgizRNFu3KjFie`</summary>

```text
Web search results for query: "TruthfulQA MC1 MC2 best scores 2025 2026 GPT-4 Claude LLaMA leaderboard"

Links: [{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"open-llm-leaderboard/open_llm_leaderboard · what kind of task does TruthfulQA eval? mc1? mc2? or both?","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/95"},{"title":"TruthfulQA Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/truthfulqa"},{"title":"TruthfulQA | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-truthful-qa"},{"title":"HuggingFaceH4/open_llm_leaderboard · what kind of task does TruthfulQA eval? mc1? mc2? or both?","url":"https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard/discussions/95"},{"title":"TruthfulQA | AI Wiki","url":"https://aiwiki.ai/wiki/truthfulqa"},{"title":"Gaming TruthfulQA: Simple Heuristics Exposed Dataset Weaknesses","url":"https://turntrout.com/original-truthfulqa-weaknesses"},{"title":"New, improved multiple-choice TruthfulQA","url":"https://www.lesswrong.com/posts/Bunfwz6JsNd44kgLT/new-improved-multiple-choice-truthfulqa"},{"title":"TruthfulQA: Benchmark for Evaluating Language | Kaggle","url":"https://www.kaggle.com/datasets/thedevastator/truthfulqa-benchmark-for-evaluating-language-mod"},{"title":"SH2: Self-Highlighted Hesitation Helps You Decode More Truthfully","url":"https://arxiv.org/html/2401.05930v1"}]

Based on my search results, here's what I found about TruthfulQA benchmark scores:

## Key Information about TruthfulQA

MC1 (Single-true) involves selecting the only correct answer from 4-5 answer choices, while MC2 (Multi-true) is scored based on the normalized total probability assigned to the set of true answers.

## Recent Performance (2025-2026)

In January 2025, a new binary-choice format was introduced that presents only two options: the best correct answer and the best incorrect answer, with the incorrect answers manually selected to target specific imitative falsehoods while keeping format and length similar to correct answers.

On this newer binary-choice format: Claude 3.5 Sonnet was reported as the strongest model, with performance "likely close to a human baseline," while GPT-4o and LLaMA 3.2 showed room for improvement. Additionally, nearly all models performed better on the binary version than on the original multiple-choice versions.

## Historical Context

The Hugging Face Open LLM Leaderboard (v1, archived June 2024) used TruthfulQA MC2 as one of its core benchmarks, with an average MC2 score across evaluated models of approximately 0.589.

The search results don't provide specific numerical MC1 and MC2 scores for individual models like GPT-4 or LLaMA across 2025-2026, but they indicate that Claude 3.5 Sonnet is currently the top-performing model on the updated benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e918e6e8-dfec-4dd8-9094-ff7036232645",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "191df4ad-ed89-4467-939f-34ba0fff0e4b",
  "sourceToolAssistantUUID": "e918e6e8-dfec-4dd8-9094-ff7036232645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-16T09:32:55.690Z_

Let me try one more search for the PC-LDCD repository accessibility and get the PapersWithCode SOTA page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191df4ad-ed89-4467-939f-34ba0fff0e4b",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61wR9aLyBshjZE2wWjR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a0887f0-cd89-45f0-af8d-4635e53303b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CU91TsNTBpWHXwhZddLLdj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4208,
      "cache_read_input_tokens": 13277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4208,
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

_source line 29 · 2026-05-16T09:32:57.439Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XascsW9tFXCY8PqXsAnE2f`</summary>

```json
{
  "url": "https://paperswithcode.com/sota/question-answering-on-truthfulqa",
  "prompt": "Extract the top models and their exact scores on TruthfulQA. List model names, MC1, MC2, True+Info scores. Include all entries in the leaderboard table."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a0887f0-cd89-45f0-af8d-4635e53303b8",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61wR9aLyBshjZE2wWjR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "299b1bd1-a746-4d53-9b77-1159985ebbe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CU91TsNTBpWHXwhZddLLdj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4208,
      "cache_read_input_tokens": 13277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4208,
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

### Tool result

_source line 30 · 2026-05-16T09:32:57.674Z_

<details><summary>↩ Tool result · `toolu_01XascsW9tFXCY8PqXsAnE2f`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://paperswithcode.com/sota/question-answering-on-truthfulqa
Redirect URL: https://huggingface.co/papers/trending
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://huggingface.co/papers/trending"
- prompt: "Extract the top models and their exact scores on TruthfulQA. List model names, MC1, MC2, True+Info scores. Include all entries in the leaderboard table."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "299b1bd1-a746-4d53-9b77-1159985ebbe2",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "774802a1-a7fb-4eb7-996a-3a8650dc656e",
  "sourceToolAssistantUUID": "299b1bd1-a746-4d53-9b77-1159985ebbe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T09:32:58.160Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SPV5w42XPcx4inHqkpEFtw`</summary>

```json
{
  "query": "anonymous.4open.science/r/PC-LDCD-63D5 repository accessible files 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "774802a1-a7fb-4eb7-996a-3a8650dc656e",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61wR9aLyBshjZE2wWjR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6d54b41-9e32-4bda-b212-52be5bff6275",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CU91TsNTBpWHXwhZddLLdj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4208,
      "cache_read_input_tokens": 13277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4208,
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

_source line 32 · 2026-05-16T09:32:58.331Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgVscP8XHuGYfpUXv82Pap`</summary>

```json
{
  "query": "\"PC-LDCD\" \"probabilistic circuit\" hallucination detection code repository github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6d54b41-9e32-4bda-b212-52be5bff6275",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61wR9aLyBshjZE2wWjR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25b6e74e-860d-4eda-8b22-3c4d3c170e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CU91TsNTBpWHXwhZddLLdj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4208,
      "cache_read_input_tokens": 13277,
      "output_tokens": 269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 269,
          "cache_read_input_tokens": 13277,
          "cache_creation_input_tokens": 4208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4208,
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

_source line 33 · 2026-05-16T09:33:03.078Z_

<details><summary>↩ Tool result · `toolu_01SPV5w42XPcx4inHqkpEFtw`</summary>

```text
Web search results for query: "anonymous.4open.science/r/PC-LDCD-63D5 repository accessible files 2026"

Links: [{"title":"Anonymous GitHub – Share the code, not the author","url":"https://anonymous.4open.science/"},{"title":"How to create an anonymous repository for double-blind peer review? · community · Discussion #175306","url":"https://github.com/orgs/community/discussions/175306"},{"title":"GitHub - tdurieux/anonymous_github: Anonymous Github is a proxy server to support anonymous browsing of Github repositories for open-science code and data. · GitHub","url":"https://github.com/tdurieux/anonymous_github"},{"title":"4open.science | 4open-science.github.io","url":"https://4open.science/"},{"title":"FAQ – Anonymous GitHub","url":"https://anonymous.4open.science/faq"},{"title":"New anonymization - Anonymous GitHub - 4open.science","url":"https://anonymous.4open.science/anonymize"},{"title":"Anonymous GitHub | Thomas Durieux","url":"https://durieux.me/projects/anonymous-github.html"},{"title":"GitHub - fedebotu/clone-anonymous-github: Easily download anonymous Github repositories from https://anonymous.4open.science/ with a GUI interface · GitHub","url":"https://github.com/fedebotu/clone-anonymous-github"},{"title":"GitHub - ShoufaChen/clone-anonymous4open: clone/download codes from https://anonymous.4open.science/ · GitHub","url":"https://github.com/ShoufaChen/clone-anonymous4open"},{"title":"https://anonymous.4open.science/r/3c2f82ff7e26/","url":"https://anonymous.4open.science/r/3c2f82ff7e26/"}]

Based on the search results, I found information about the anonymous.4open.science service, but the search did not return specific details about the particular repository with ID "PC-LDCD-63D5" or its accessible files.

Here's what I can tell you about the service itself:

Anonymous Github is a system that helps anonymize Github repositories for double-anonymous paper submissions. The anonymization process replaces all occurrences of identifying information with "XXXX", and the README as well as all files of the repository are anonymized, even filenames are anonymized.

However, the search results don't contain specific information about what files are accessible in the repository at the URL path you mentioned (anonymous.4open.science/r/PC-LDCD-63D5). To access that specific repository and see what files are available, you would need to visit that URL directly in your web browser.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6d54b41-9e32-4bda-b212-52be5bff6275",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "2a838ddf-e565-4a29-83ce-f774effb9854",
  "sourceToolAssistantUUID": "e6d54b41-9e32-4bda-b212-52be5bff6275",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:33:04.401Z_

<details><summary>↩ Tool result · `toolu_01FgVscP8XHuGYfpUXv82Pap`</summary>

```text
Web search results for query: ""PC-LDCD" "probabilistic circuit" hallucination detection code repository github"

Links: [{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"hallucination-detection · GitHub Topics · GitHub","url":"https://github.com/topics/hallucination-detection"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"GitHub - NishilBalar/Awesome-LVLM-Hallucination: up-to-date curated list of state-of-the-art Large vision language models hallucinations research work, papers & resources · GitHub","url":"https://github.com/NishilBalar/Awesome-LVLM-Hallucination"},{"title":"hallucination · GitHub Topics · GitHub","url":"https://github.com/topics/hallucination"},{"title":"GitHub - idiap/hallucination-detection: Automatically detect hallucinations in a BART summarization model from its attentions and decoding probabilities · GitHub","url":"https://github.com/idiap/hallucination-detection"},{"title":"hallucination-mitigation · GitHub Topics · GitHub","url":"https://github.com/topics/hallucination-mitigation"},{"title":"GitHub - showlab/Awesome-MLLM-Hallucination: 📖 A curated list of resources dedicated to hallucination of multimodal large language models (MLLM).","url":"https://github.com/showlab/Awesome-MLLM-Hallucination"},{"title":"by topics | Probabilistic Circuits","url":"https://arranger1044.github.io/probabilistic-circuits/topics"}]

Based on the search results, I found relevant information about PC-LDCD and the code repository:

## PC-LDCD: Probabilistic Circuit Hallucination Detection

PC-LDCD stands for "Probabilistic Circuit Latent Density Contrastive Decoding", a method designed to address hallucinations in Large Language Models (LLMs).

### Method Overview

The approach uses PCNet, a Probabilistic Circuit (PC) trained as a tractable density estimator over a low-dimensional projection of the LLM's final hidden state. By exploiting the structural guarantees of PCs, PCNet computes the exact Negative Log-Likelihood (NLL) of any latent state in a single forward pass: no sampling, no external verifiers, and no weight modifications are needed.

### Performance

Across four LLMs, ranging from 1B to 8B models, and four benchmarks covering conversational reasoning, knowledge-intensive QA, reading comprehension, and truthfulness, PCNet achieves near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%.

### Code Repository

The proposed method is publicly available on GitHub at https://anonymous.4open.science/r/PC-LDCD-63D5.

This appears to be a recent research publication (from about 1 week ago based on the search results) that combines probabilistic circuits with hallucination detection for improved LLM reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25b6e74e-860d-4eda-8b22-3c4d3c170e1e",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "0eefff27-c6a7-4cc6-aa09-b1460a081cf4",
  "sourceToolAssistantUUID": "25b6e74e-860d-4eda-8b22-3c4d3c170e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T09:33:07.732Z_

Let me get the full paper details for PC-LDCD and check if the PapersWithCode redirect confirms the shutdown.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eefff27-c6a7-4cc6-aa09-b1460a081cf4",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61xPiXj6W1c3CZTcuhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fc1f409-836e-45f5-82bb-a49516bfbff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXvGt44nkxPprMQjbXnntd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2022,
      "cache_read_input_tokens": 17485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2022,
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

_source line 36 · 2026-05-16T09:33:09.419Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VM8deRsFrCHgbJqf6TeVaL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05953",
  "prompt": "Extract all details about PC-LDCD: authors, exact performance numbers (AUROC, F1, etc.), model sizes tested, benchmarks used, and the URL of the code repository."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fc1f409-836e-45f5-82bb-a49516bfbff7",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61xPiXj6W1c3CZTcuhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66dcb8b9-115a-4473-90c7-039c2f87eeb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXvGt44nkxPprMQjbXnntd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2022,
      "cache_read_input_tokens": 17485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2022,
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

_source line 37 · 2026-05-16T09:33:10.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011rUsGFjQVHNb9UBLVqRa1c`</summary>

```json
{
  "query": "TruthfulQA MC1 MC2 scores GPT-4o Claude 3.5 Llama 3 exact numbers benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66dcb8b9-115a-4473-90c7-039c2f87eeb8",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61xPiXj6W1c3CZTcuhH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11708093-4514-4dfd-9eff-f5ce20bd94a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXvGt44nkxPprMQjbXnntd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2022,
      "cache_read_input_tokens": 17485,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 17485,
          "cache_creation_input_tokens": 2022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2022,
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

_source line 38 · 2026-05-16T09:33:13.525Z_

<details><summary>↩ Tool result · `toolu_01VM8deRsFrCHgbJqf6TeVaL`</summary>

```text
# PC-LDCD Details

**Authors:** Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca

**Performance Metrics:**
- AUROC reaches "up to 99%" across CoQA, SQuAD v2.0, and TriviaQA
- Corruption rate reduced to 53.7%
- Preservation rate achieved 79.3%
- Highest True+Info, MC2, and MC3 scores on TruthfulQA in three of four models tested

**Model Sizes Tested:** 1B to 8B parameter models (four different LLMs)

**Benchmarks Used:**
- CoQA (conversational reasoning)
- SQuAD v2.0 (reading comprehension)
- TriviaQA (knowledge-intensive QA)
- TruthfulQA (truthfulness evaluation)

**Code Repository:** The abstract states "Our proposed method is publicly available on GitHub," but the specific URL is not provided in this page content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66dcb8b9-115a-4473-90c7-039c2f87eeb8",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "5dec0d0e-fc81-44b7-8f3c-898f31f7f955",
  "sourceToolAssistantUUID": "66dcb8b9-115a-4473-90c7-039c2f87eeb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T09:33:21.443Z_

<details><summary>↩ Tool result · `toolu_011rUsGFjQVHNb9UBLVqRa1c`</summary>

```text
Web search results for query: "TruthfulQA MC1 MC2 scores GPT-4o Claude 3.5 Llama 3 exact numbers benchmark results"

Links: [{"title":"New, improved multiple-choice TruthfulQA","url":"https://www.lesswrong.com/posts/Bunfwz6JsNd44kgLT/new-improved-multiple-choice-truthfulqa"},{"title":"New, improved multiple-choice TruthfulQA | TruthfulAI","url":"https://truthful.ai/blog/truthfulqa-binary-choice/"},{"title":"TruthfulQA | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-truthful-qa"},{"title":"TruthfulQA Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/truthfulqa"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"AI Model Benchmarks Comparison | LangDB","url":"https://langdb.ai/app/models/benchmarks/"},{"title":"Gaming TruthfulQA: Simple Heuristics Exposed Dataset Weaknesses","url":"https://turntrout.com/original-truthfulqa-weaknesses"},{"title":"30 LLM evaluation benchmarks and how they work","url":"https://www.evidentlyai.com/llm-guide/llm-benchmarks"},{"title":"open-llm-leaderboard/open_llm_leaderboard · what kind of task does TruthfulQA eval? mc1? mc2? or both?","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/95"}]

The search results provide information about TruthfulQA benchmarks and the models tested, but don't include the specific exact numerical scores for MC1 and MC2 for each model. Let me search for more specific numerical data.

Links: [{"title":"TruthfulQA Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/truthfulqa"},{"title":"TruthfulQA | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-truthful-qa"},{"title":"TruthfulQA Benchmark Overview","url":"https://www.emergentmind.com/topics/truthfulqa-benchmark"},{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"[2109.07958] TruthfulQA: Measuring How Models Mimic Human Falsehoods","url":"https://arxiv.org/abs/2109.07958"},{"title":"TruthfulQA: Measuring factual accuracy","url":"https://www.statsig.com/perspectives/truthfulqameasuringaccuracy"},{"title":"Gaming TruthfulQA: Simple Heuristics Exposed Dataset Weaknesses","url":"https://turntrout.com/original-truthfulqa-weaknesses"},{"title":"TruthfulQA: Measuring How Models Mimic Human Falsehoods Stephanie Lin","url":"https://owainevans.github.io/pdfs/truthfulQA_lin_evans.pdf"},{"title":"domenicrosati/TruthfulQA · Datasets at Hugging Face","url":"https://huggingface.co/datasets/domenicrosati/TruthfulQA"},{"title":"TruthfulQA: Measuring How Models Mimic Human Falsehoods - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.229/"}]

Let me search more specifically for the exact numerical scores for these models.

Links: [{"title":"New, improved multiple-choice TruthfulQA","url":"https://www.lesswrong.com/posts/Bunfwz6JsNd44kgLT/new-improved-multiple-choice-truthfulqa"},{"title":"New, improved multiple-choice TruthfulQA | TruthfulAI","url":"https://truthful.ai/blog/truthfulqa-binary-choice/"},{"title":"Comparison Analysis: Claude 3.5 Sonnet vs GPT-4o - Vellum","url":"https://www.vellum.ai/blog/claude-3-5-sonnet-vs-gpt4o"},{"title":"Evaluation: Llama 3.1 70B vs. Comparable Closed-Source ...","url":"https://www.vellum.ai/blog/llama-3-1-70b-vs-gpt-4o-vs-claude-3-5-sonnet"},{"title":"Claude 3.5 Sonnet June Version vs GPT-4o","url":"https://blog.promptlayer.com/claude-3-5-sonnet-june-version-vs-gpt-4o/"},{"title":"Comparing GPT-4o, LLaMA 3.1, and Claude 3.5 Sonnet","url":"https://www.walturn.com/insights/comparing-gpt-4o-llama-3-1-and-claude-3-5-sonnet"},{"title":"Llama 4 Comparison with Claude 3.7 Sonnet, GPT-4.5, and Gemini 2.5 - Bind AI","url":"https://blog.getbind.co/2025/04/06/llama-4-comparison-with-claude-3-7-sonnet-gpt-4-5-and-gemini-2-5/"},{"title":"Llama 3.1 405B vs Claude Sonnet 3.5 vs GPT 4o | by Cogni Down Under | Medium","url":"https://medium.com/@cognidownunder/llama-3-1-405b-vs-claude-sonnet-3-5-vs-gpt-4o-438ee1355b2f"},{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"GPT-4 vs Llama-3.1 vs Claude 3.5. With the release of Llama 3.1, the… | by Pavan Kumar Thatha | Medium","url":"https://medium.com/@pavankthatha/gpt-4-vs-llama-3-1-vs-claude-3-5-3bdccddf6629"}]

Based on my web searches, I found information about TruthfulQA benchmark evaluations, though the search results don't provide complete numerical data for all the specific models and metrics you requested. Here's what I discovered:

## TruthfulQA Benchmark Overview

TruthfulQA includes MC1 (Single-true) multiple-choice where one correct answer is paired with 4-5 incorrect options, and in the original paper and codebase, this metric was computed by taking the logprobs for each answer and selecting the highest. MC2 (Multi-true) scoring is the normalized total probability assigned to the set of true answers.

## Model Performance

The new binary-choice setting for TruthfulQA includes evaluations of Claude 3.5 Sonnet, GPT-4o, and Llama-3.2, with Claude 3.5 Sonnet's performance likely close to a human baseline.

Unfortunately, the web search results do not contain the specific exact numerical scores (percentages or raw numbers) for MC1 and MC2 performance for these individual models. The sources reference these benchmarks and models but don't provide the complete numerical results table you're looking for. 

To find these exact numbers, you may want to check:
- The official GitHub repository for TruthfulQA (sylinrl/TruthfulQA)
- The TruthfulAI blog post on the binary-choice version
- Individual model technical reports from OpenAI, Anthropic, and Meta


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11708093-4514-4dfd-9eff-f5ce20bd94a3",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "e6812adf-41df-4faf-8788-5f6069d339c0",
  "sourceToolAssistantUUID": "11708093-4514-4dfd-9eff-f5ce20bd94a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T09:33:25.854Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rxp2JT9TbBPzUCusHPfJ2A`</summary>

```json
{
  "url": "https://truthful.ai/blog/truthfulqa-binary-choice/",
  "prompt": "Extract all specific model scores on TruthfulQA. Include MC1, MC2, binary choice accuracy, True+Info for every model listed. Include exact percentages or decimal scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6812adf-41df-4faf-8788-5f6069d339c0",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61yebG8sYVzBoeHQpw4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd27f306-8db0-426d-8454-5ef22375f24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNQb1VzyGjr2X69Pkm5HYq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2622,
      "cache_read_input_tokens": 19507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2622,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 41 · 2026-05-16T09:33:26.275Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Rz7cvYMxr67at9S8dTDdJK`</summary>

```json
{
  "url": "https://deepeval.com/docs/benchmarks-truthful-qa",
  "prompt": "Extract all model scores, MC1, MC2, True+Info metrics for TruthfulQA. List every model and its exact scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd27f306-8db0-426d-8454-5ef22375f24f",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61yebG8sYVzBoeHQpw4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecccdc3e-c73f-4707-89cb-fb7b8b5305d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNQb1VzyGjr2X69Pkm5HYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2622,
      "cache_read_input_tokens": 19507,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2622
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 19507,
          "cache_creation_input_tokens": 2622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2622,
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

_source line 42 · 2026-05-16T09:33:29.368Z_

<details><summary>↩ Tool result · `toolu_01Rxp2JT9TbBPzUCusHPfJ2A`</summary>

```text
I cannot extract the specific model scores you requested because the webpage content does not include numerical data for those metrics.

While the article mentions "The performance of various models on the binary dataset are shown below" and references a comparison chart, the actual percentages or decimal scores are not provided in the text. The charts are referenced as images but their data values are not transcribed in the content provided.

The article discusses performance conceptually—noting that "nearly all models perform better on the binary setting" and that "Claude 3.5 Sonnet" shows performance "likely close to a human baseline"—but does not include the specific MC1, MC2, or binary-choice accuracy percentages for any individual model.

To obtain these specific scores, you would need to access the actual published benchmark results, likely through the GitHub repository or the research papers linked in the article.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd27f306-8db0-426d-8454-5ef22375f24f",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "063716a0-d6a0-46d9-ad13-5b323cb8afdc",
  "sourceToolAssistantUUID": "dd27f306-8db0-426d-8454-5ef22375f24f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T09:33:29.848Z_

<details><summary>↩ Tool result · `toolu_01Rz7cvYMxr67at9S8dTDdJK`</summary>

```text
# TruthfulQA Model Scores

The provided content does not contain any actual model scores, MC1, MC2, or True+Info metrics data. 

The page is documentation that explains how to use the TruthfulQA benchmark, including:

- Description of the benchmark (817 questions across 38 topics)
- Available configuration arguments (tasks and evaluation modes)
- Usage instructions with a code example
- Explanation of MC1 vs MC2 scoring approaches
- Complete list of 38 task categories

The documentation notes that "MC1 mode's performance is measured using an exact match scorer" while "MC2 mode employs a truth identification scorer," but no specific numerical results or comparative model performance data are presented in this content.

To find actual benchmark results comparing different models, you would need to consult the TruthfulQA GitHub repository or published research papers that have run evaluations using this benchmark.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecccdc3e-c73f-4707-89cb-fb7b8b5305d3",
  "isSidechain": true,
  "promptId": "9a348fcc-899b-494b-927d-a3b5298b08c3",
  "agentId": "a0e768b54608f18ff",
  "type": "user",
  "uuid": "cb34ab5d-7dfc-4b76-a789-d98fee583371",
  "sourceToolAssistantUUID": "ecccdc3e-c73f-4707-89cb-fb7b8b5305d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-16T09:34:11.010Z_

Now I have enough information to compile a comprehensive report. Here is the full synthesis:

---

## 1. TruthfulQA -- Current State of the Art (as of May 2026)

**Important caveat:** Papers With Code (the canonical SOTA tracker) was shut down by Meta in July 2025 and its leaderboard pages now redirect to Hugging Face. This makes it harder to find a single consolidated SOTA table. The best remaining source is [llm-stats.com](https://llm-stats.com/benchmarks/truthfulqa).

**Top models on the llm-stats.com TruthfulQA leaderboard (overall score, 817-question benchmark):**

| Rank | Model | Score |
|------|-------|-------|
| 1 | Phi-3.5-MoE-instruct (Microsoft) | 0.775 |
| 2 | Granite 3.3 8B Instruct (IBM) | 0.669 |
| 3 | Phi 4 Mini (Microsoft) | 0.664 |
| 4 | Phi-3.5-mini-instruct (Microsoft) | 0.640 |
| 5 | Hermes 3 70B (Nous Research) | 0.633 |
| ... | (17 models total, down to 0.503) | |

**Breakdowns by MC1/MC2/True+Info:** Unfortunately, the available leaderboards report a single aggregate score and do not break out MC1, MC2, or True+Info separately. The original Open LLM Leaderboard v1 (HuggingFace, archived June 2024) used MC2 exclusively and reported an average of ~0.589 across evaluated models. The newer binary-choice variant of TruthfulQA (introduced January 2025 by TruthfulAI) found that **Claude 3.5 Sonnet** performs at near-human-baseline levels, outperforming GPT-4o and Llama 3.2, but exact numerical scores are only available in the charts of the blog post (not machine-readable text).

**Key takeaway:** Phi-3.5-MoE-instruct at 77.5% is the highest publicly reported score on the standard TruthfulQA benchmark. On the newer binary-choice format, Claude 3.5 Sonnet leads.

---

## 2. ESR (Endogenous Steering Resistance) -- arXiv:2602.06941

**Paper:** "Endogenous Resistance to Activation Steering in Language Models" by Alex McKenzie, Keenan Pepper, Stijn Servaes, et al. (submitted February 6, 2026).

**Definition:** ESR is defined as "inference-time recovery from irrelevant activation steering" -- the phenomenon where a model, while being actively steered off-topic via activation vectors, spontaneously recovers mid-generation and produces an improved response.

**Specific numbers by model scale:**

| Model | ESR Rate | Multi-Attempt Rate |
|-------|----------|--------------------|
| **Llama-3.3-70B** | **3.8%** | **7.4%** |
| Llama-3.1-8B | <1% | <=1.2% |
| Gemma-2-27B | <1% | not specified |
| Gemma-2-9B | <1% | not specified |
| Gemma-2-2B | <1% | not specified |

**ESR at 8B vs 70B:** The 70B model (Llama-3.3-70B) shows an ESR rate of **3.8%** and multi-attempt rate of **7.4%**, while the 8B model (Llama-3.1-8B) is below **1% ESR** and at most **1.2% multi-attempt rate**. This is roughly a 3-4x difference in ESR rate between 8B and 70B scale.

**ESR circuits (precise claim):** The authors identified **26 SAE (Sparse Autoencoder) latents** that "activate differentially during off-topic content and are causally linked to ESR" in Llama-3.3-70B. Zero-ablating these latents **reduced the multi-attempt rate by 25%**, providing causal evidence for **"dedicated internal consistency-checking circuits"** within the model.

**Enhancement results:**
- Meta-prompts instructing the model to self-monitor increased the multi-attempt rate by **4.3x** (from 7.4% to 31.7%) and the ESR rate by **3.9x** (from 3.8% to 14.8%) for Llama-3.3-70B.
- Fine-tuning on self-correction examples successfully induced ESR-like behavior in smaller models.

---

## 3. PC-LDCD Code Repository Accessibility

**Paper:** "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits" (arXiv:2605.05953) by Erik Nielsen, Elia Cunegatti, Marcus Vukojevic, Giovanni Iacca.

**Repository URL:** `https://anonymous.4open.science/r/PC-LDCD-63D5`

**Accessibility status: NOT ACCESSIBLE (HTTP 403 Forbidden).** Two separate WebFetch attempts to reach the anonymous repository both returned **403 errors**. The anonymous.4open.science service anonymizes GitHub repositories for double-blind review; these links are often time-limited or access-restricted during the review period. Given the paper's submission date (~May 8, 2026, very recent), the repository may be:
- Temporarily restricted during active peer review
- Only accessible via browser with specific session/cookie requirements that programmatic fetching cannot satisfy
- Expired or not yet publicly activated

**What the paper claims about the code:** PC-LDCD uses PCNet (a Probabilistic Circuit trained as a tractable density estimator over LLM residual streams) to detect hallucinations as geometric anomalies. Reported results include AUROC up to 99% on CoQA, SQuAD v2.0, and TriviaQA across models from 1B to 8B parameters, with corruption rate reduced to 53.7% and preservation rate of 79.3%. It achieved the highest True+Info, MC2, and MC3 scores on TruthfulQA in three of four models tested.

---

Sources:
- [TruthfulQA Benchmark Leaderboard (llm-stats.com)](https://llm-stats.com/benchmarks/truthfulqa)
- [New, improved multiple-choice TruthfulQA (TruthfulAI blog)](https://truthful.ai/blog/truthfulqa-binary-choice/)
- [Papers With Code shutdown report (CodeSOTA)](https://www.codesota.com/papers-with-code)
- [TruthfulQA GitHub Repository](https://github.com/sylinrl/TruthfulQA)
- [Endogenous Resistance to Activation Steering (arXiv:2602.06941)](https://arxiv.org/abs/2602.06941)
- [Endogenous Resistance to Activation Steering -- full HTML](https://arxiv.org/html/2602.06941v1)
- [PC-LDCD: Hallucination as an Anomaly (arXiv:2605.05953)](https://arxiv.org/abs/2605.05953)
- [PC-LDCD full HTML paper](https://arxiv.org/html/2605.05953)
- [Anonymous GitHub (4open.science)](https://anonymous.4open.science/)
- [TruthfulQA | DeepEval Documentation](https://deepeval.com/docs/benchmarks-truthful-qa)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb34ab5d-7dfc-4b76-a789-d98fee583371",
  "isSidechain": true,
  "agentId": "a0e768b54608f18ff",
  "requestId": "req_011Cb61zGZES9pQyY42tXDyG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b640c6c1-bc01-45a9-884a-ca8f2ba3773e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6c5f2c7e-6540-471d-abde-2224054378a6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QLQm2hf4ahq3P8n11YNjJv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 22129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 665,
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
