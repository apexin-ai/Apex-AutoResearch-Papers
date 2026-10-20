# Research conversation: Search the web to verify benchmark claims and baseline results: 1. LIBERO-100 benchmark: What is the current SOTA? Is it

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a852f7874a86f5aed.jsonl`
- **Structured JSON:** [`d399d0312ff393f84074.json`](../../sessions/d3/d399d0312ff393f84074.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-10T18:35:21.282Z_

Search the web to verify benchmark claims and baseline results:

1. LIBERO-100 benchmark: What is the current SOTA? Is it saturated? Search for "LIBERO benchmark robotics 2026 SOTA results"
2. LIBERO-PRO: Does this benchmark exist? What does it test? Search for "LIBERO-PRO robustness evaluation VLA" and "LIBERO-PRO arxiv"
3. RoboCasa benchmark: What is the current SOTA? The proposal claims SOTA ~67%. Search for "RoboCasa benchmark robotics manipulation 2026 results"
4. Fast-WAM: Search for "Fast-WAM world action model test time" - what results does it achieve on LIBERO?
5. Cosmos-Policy results on LIBERO
6. Has anyone evaluated UWM on RoboCasa or LIBERO-PRO?

Also verify:
- CoRL 2026 deadlines: abstract May 26, paper May 29? Search "CoRL 2026 submission deadline"
- AVDiT (NeurIPS 2024) "mixture of noise levels audiovisual" - does it exist?
- D3P "Dynamic Denoising Diffusion Policy" - does it exist?

Report specific numbers and sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "69e04cd1-cd08-43ee-b284-5680a40ed51d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T18:35:22.892Z_

I'll search the web to verify these benchmark claims and baseline results. Let me make multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e04cd1-cd08-43ee-b284-5680a40ed51d",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1beb38d7-0538-4e46-892a-b40f63c907ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 3 · 2026-05-10T18:35:23.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XEdPQif5564yiAKM8XkEth`</summary>

```json
{
  "query": "LIBERO benchmark robotics 2026 SOTA results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1beb38d7-0538-4e46-892a-b40f63c907ae",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d1c97297-bb96-4a28-ace1-852ca7e07998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 4 · 2026-05-10T18:35:23.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HaVDjfk6mHWtC67KAoPonF`</summary>

```json
{
  "query": "LIBERO-PRO robustness evaluation VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1c97297-bb96-4a28-ace1-852ca7e07998",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57d78fd0-1786-4af9-a7a7-53d248af3976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 5 · 2026-05-10T18:35:23.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0125QG76jhazTYGkc8PmxR4i`</summary>

```json
{
  "query": "LIBERO-PRO arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57d78fd0-1786-4af9-a7a7-53d248af3976",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "21c347a0-4191-4b7f-b6a0-b155f91bca3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 6 · 2026-05-10T18:35:23.518Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VXoBcceuBhZfABWFsa8g5R`</summary>

```json
{
  "query": "RoboCasa benchmark robotics manipulation 2026 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21c347a0-4191-4b7f-b6a0-b155f91bca3f",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2ec9937-2299-47a8-b1a2-0e8ffa1f358f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 7 · 2026-05-10T18:35:23.523Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FcjcE6PnvDyzmKnHuqoinb`</summary>

```json
{
  "query": "Fast-WAM world action model test time LIBERO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2ec9937-2299-47a8-b1a2-0e8ffa1f358f",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0edaba56-194a-463b-8793-cb2584b9fc5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 8 · 2026-05-10T18:35:23.745Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DWfhvqzP2eHgKi5J52Psy7`</summary>

```json
{
  "query": "Cosmos-Policy LIBERO results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0edaba56-194a-463b-8793-cb2584b9fc5f",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58e69065-a644-4aff-bd48-0a14f688a182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 9 · 2026-05-10T18:35:23.966Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XC3BrsjE3oKkFyFvZEQHsc`</summary>

```json
{
  "query": "UWM RoboCasa LIBERO-PRO evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58e69065-a644-4aff-bd48-0a14f688a182",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3ab5dca4-ce7c-4873-acdf-9b93f24f3c73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 10 · 2026-05-10T18:35:24.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011SB1nwyF4axrQiuyZo5629`</summary>

```json
{
  "query": "CoRL 2026 submission deadline abstract paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ab5dca4-ce7c-4873-acdf-9b93f24f3c73",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "399bd3aa-8fd0-425b-ab38-3f42ac20228d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 11 · 2026-05-10T18:35:24.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KtyNqSmsyzpaRmLMfbH9qF`</summary>

```json
{
  "query": "AVDiT NeurIPS 2024 mixture noise audiovisual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "399bd3aa-8fd0-425b-ab38-3f42ac20228d",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a2e28a47-060f-4f4d-89ba-9ef8cda77ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 725
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 499,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 725,
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

_source line 12 · 2026-05-10T18:35:24.484Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qu8x91re4bPtasyCUNCKkh`</summary>

```json
{
  "query": "D3P Dynamic Denoising Diffusion Policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2e28a47-060f-4f4d-89ba-9ef8cda77ea2",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNTLG1wKLmYWyewAc1p",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fc4667d7-4ad9-4131-a0ae-42747c398234",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014KJnUJV1q7iegQwfV8WXyh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 13789,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 725
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 499,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 725,
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

_source line 13 · 2026-05-10T18:35:29.217Z_

<details><summary>↩ Tool result · `toolu_01FcjcE6PnvDyzmKnHuqoinb`</summary>

```text
Web search results for query: "Fast-WAM world action model test time LIBERO"

Links: [{"title":"[2603.16666] Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/abs/2603.16666"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"(PDF) Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://www.researchgate.net/publication/402613129_Fast-WAM_Do_World_Action_Models_Need_Test-time_Future_Imagination"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?…","url":"https://www.opentrain.ai/papers/fast-wam-do-world-action-models-need-test-time-future-imagination--arxiv-2603.16666/"},{"title":"Fast-WAM: Rethinking Test-Time Imagination","url":"https://www.emergentmind.com/papers/2603.16666"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination? | alphaXiv","url":"https://www.alphaxiv.org/resources/2603.16666v2"},{"title":"Paper page - Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://huggingface.co/papers/2603.16666"},{"title":"yuantianyuan01/FastWAM | DeepWiki","url":"https://deepwiki.com/yuantianyuan01/FastWAM"}]

Based on the search results, here's what I found about Fast-WAM and its evaluation on LIBERO:

## Fast-WAM Overview

Fast-WAM is a World Action Model (WAM) architecture that retains video co-training during training but skips future prediction at test time. The research asks whether WAMs need explicit future imagination at test time, or whether their benefit comes primarily from video modeling during training.

## Key Findings

Fast-WAM remains competitive with imagine-then-execute variants, while removing video co-training causes a much larger performance drop. This suggests the main value of video prediction in WAMs may lie in learning better world representations during training rather than generating future observations at test time.

## LIBERO Evaluation

Fast-WAM achieves competitive results with state-of-the-art methods on simulation benchmarks (LIBERO and RoboTwin). More specifically, Fast-WAM achieves competitive overall performance on LIBERO without embodied pretraining, remains close to both imagine-then-execute variants, and outperforms the no-video-co-training ablation by a clear margin.

The research paper was published in March 2026 and includes an official codebase available on GitHub, which contains training and evaluation code for LIBERO and RoboTwin benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0edaba56-194a-463b-8793-cb2584b9fc5f",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "ed9d3c49-f2b9-47d2-9e06-00e14fa632f2",
  "sourceToolAssistantUUID": "0edaba56-194a-463b-8793-cb2584b9fc5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:35:29.364Z_

<details><summary>↩ Tool result · `toolu_01VXoBcceuBhZfABWFsa8g5R`</summary>

```text
Web search results for query: "RoboCasa benchmark robotics manipulation 2026 results"

Links: [{"title":"[2603.04356] RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://arxiv.org/abs/2603.04356"},{"title":"[2407.06951] RoboCAS: A Benchmark for Robotic Manipulation in Complex Object Arrangement Scenarios","url":"https://arxiv.org/abs/2407.06951"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"},{"title":"RoboCAS: A Benchmark for Robotic Manipulation in Complex Object Arrangement Scenarios","url":"https://arxiv.org/html/2407.06951v1"},{"title":"RoboCasa: Scalable Household Robotics Simulation","url":"https://www.emergentmind.com/topics/robocasa"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | OpenReview","url":"https://openreview.net/forum?id=tQJYKwc3n4"},{"title":"RoboCasa","url":"https://robocasa.ai/"},{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/attachment?id=tQJYKwc3n4&name=pdf"},{"title":"RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots","url":"https://arxiv.org/html/2603.04356v1"}]

Based on the search results, here are the recent findings on RoboCasa benchmark robotics manipulation for 2026:

## RoboCasa365 Benchmark

RoboCasa365 is a comprehensive simulation benchmark for household mobile manipulation, introducing 365 everyday tasks across 2,500 diverse kitchen environments, with over 600 hours of human demonstration data and over 1600 hours of synthetically generated demonstration data.

### Key Features

RoboCasa365 is designed to support systematic evaluations for different problem settings, including multi-task learning, robot foundation model training, and lifelong learning.

The benchmark defines 365 tasks spanning 60 distinct kitchen activities, including manipulation, semantic reasoning, long-horizon planning, and memory-dependent tasks, with a total of 365 everyday tasks: 65 atomic tasks and 300 composite tasks.

### Benchmark Results

Extensive experiments on this benchmark with state-of-the-art methods analyze the impacts of task diversity, dataset scale, and environment variation on generalization, providing new insights into what factors most strongly affect the performance of generalist robots.

For specific model performance, a state-of-the-art model achieved 67.1% average success rate across 24 kitchen manipulation tasks on the RoboCasa simulation benchmark.

RoboCasa365 was published as a conference paper at ICLR 2026, representing a major benchmark release for the robotics community.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2ec9937-2299-47a8-b1a2-0e8ffa1f358f",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "6165ddf5-f0c1-4412-8261-0ec48f62a769",
  "sourceToolAssistantUUID": "f2ec9937-2299-47a8-b1a2-0e8ffa1f358f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:35:29.705Z_

<details><summary>↩ Tool result · `toolu_0125QG76jhazTYGkc8PmxR4i`</summary>

```text
Web search results for query: "LIBERO-PRO arxiv"

Links: [{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"[2510.03827v1] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"}]

## LIBERO-PRO on arXiv

I found the paper "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization" on arXiv.

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison. 

To address these issues, LIBERO-PRO is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

The research reveals significant findings about current VLA models: Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the generalized LIBERO-PRO setting, exposing the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

The paper was posted to arXiv on October 4, 2025 (arXiv:2510.03827), and the code is available on [GitHub](https://github.com/Zxy-MLlab/LIBERO-PRO).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21c347a0-4191-4b7f-b6a0-b155f91bca3f",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "5ba3ae75-52d8-4bd9-87a0-a90943d02808",
  "sourceToolAssistantUUID": "21c347a0-4191-4b7f-b6a0-b155f91bca3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:35:30.043Z_

<details><summary>↩ Tool result · `toolu_011SB1nwyF4axrQiuyZo5629`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline abstract paper"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on the search results, here's the key information about CoRL 2026 submission deadlines and paper requirements:

## Submission Deadlines

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC.

## Paper Format and Length

Papers should have a maximum of 8 pages for the main paper. Acknowledgments, References, and Appendix (optional) will not count towards the page limit. An additional 9th page is available for camera-ready submissions to incorporate reviewer feedback.

## Important Submission Notes

The deadlines are final, and no accommodations can be made for missing the abstract deadline or paper deadline. Authors may update the title and abstract on OpenReview after the abstract submission deadline, but authors cannot be added or removed after this deadline, as this information is required to facilitate reviewer assignments.

## Conference Details

CoRL 2026 will be held November 9-12, 2026 in Austin, Texas, US.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "399bd3aa-8fd0-425b-ab38-3f42ac20228d",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "404c242c-c0b8-49a7-8c64-b60604a343fc",
  "sourceToolAssistantUUID": "399bd3aa-8fd0-425b-ab38-3f42ac20228d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T18:35:30.059Z_

<details><summary>↩ Tool result · `toolu_01DWfhvqzP2eHgKi5J52Psy7`</summary>

```text
Web search results for query: "Cosmos-Policy LIBERO results"

Links: [{"title":"nvidia/Cosmos-Policy-LIBERO-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning - Cosmos Cookbook","url":"https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html"},{"title":"[2601.16163] Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/abs/2601.16163"},{"title":"Cosmos Policy Achieves 98.5% Robot Control With Single- ...","url":"https://quantumzeitgeist.com/percent-cosmos-policy-achieves-robot-control/"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning | OpenReview","url":"https://openreview.net/forum?id=wPEIStHxYH"},{"title":"NVIDIA adds Cosmos Policy to its world foundation models - The Robot Report","url":"https://www.therobotreport.com/nvidia-adds-cosmos-policy-world-foundation-models/"},{"title":"GitHub - NVlabs/cosmos-policy: Cosmos Policy · GitHub","url":"https://github.com/NVlabs/cosmos-policy"},{"title":"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning","url":"https://arxiv.org/html/2601.16163v1"},{"title":"cosmos-policy/LIBERO.md at main · NVlabs/cosmos-policy","url":"https://github.com/NVlabs/cosmos-policy/blob/main/LIBERO.md"}]

Based on the search results, here's a comprehensive summary of the Cosmos-Policy LIBERO results:

## Overview

Cosmos Policy achieves state-of-the-art performance on the LIBERO simulation benchmark with a 98.5% average success rate across four task suites.

## Detailed Results by Task Suite

The model demonstrated consistent high performance across four LIBERO task suites with rates of 98.1%, 100.0%, 98.2%, and 97.6% respectively. Specifically, these correspond to:
- LIBERO-Spatial: 98.1%
- LIBERO-Object: 100.0%
- LIBERO-Goal: 98.2%
- LIBERO-Long (LIBERO-10): 97.6%

## Key Capabilities

Cosmos-Policy-LIBERO-Predict2-2B is a 2B-parameter robot manipulation policy model fine-tuned from the NVIDIA Cosmos-Predict2-2B-Video2World video foundation model. The model has multimodal outputs that jointly predict actions, future states, and values through unified video diffusion.

## Comparison to Other Methods

Cosmos Policy consistently outperforms prior diffusion policies and VLA-based approaches across task suites, particularly on tasks that require precise temporal coordination and multi-step execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58e69065-a644-4aff-bd48-0a14f688a182",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "03cdfcec-1c01-4ad1-a52b-b362687c5b42",
  "sourceToolAssistantUUID": "58e69065-a644-4aff-bd48-0a14f688a182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T18:35:30.504Z_

<details><summary>↩ Tool result · `toolu_01HaVDjfk6mHWtC67KAoPonF`</summary>

```text
Web search results for query: "LIBERO-PRO robustness evaluation VLA"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"[2510.03827] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/abs/2510.03827"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"}]

Here are the search results for LIBERO-PRO robustness evaluation of VLA models:

## Overview

LIBERO-PRO is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

## Key Findings

Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the LIBERO-PRO generalized setting. This dramatic difference reveals critical weaknesses:

1. **Failure Under Simple Perturbations**: Despite achieving success rates above 90% on the standard LIBERO benchmark, models nearly collapse under changes to object positions or minor task modifications, even when constructed from training components.

2. **Illusory Robustness**: Apparent stability against object and instruction perturbations is largely due to overfitting rather than genuine task understanding.

3. **Memorization Over Understanding**: This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

4. **Language Instruction Handling**: The model relies predominantly on visual context and memorized action trajectories from training, while disregarding the linguistic content of the input.

## Conclusion

Current VLA models, despite excelling on the standard LIBERO, lack true robustness and generalization—highlighting the need for rigorous evaluation frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d78fd0-1786-4af9-a7a7-53d248af3976",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "3f5d513f-5bc5-408e-8854-d16e7b29126c",
  "sourceToolAssistantUUID": "57d78fd0-1786-4af9-a7a7-53d248af3976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T18:35:30.630Z_

<details><summary>↩ Tool result · `toolu_01XEdPQif5564yiAKM8XkEth`</summary>

```text
Web search results for query: "LIBERO benchmark robotics 2026 SOTA results"

Links: [{"title":"Robotics AI Benchmarks 2026: State of the Art | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/robotics"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO-Long — Robot Manipulation benchmark","url":"https://www.codesota.com/browse/robots/robot-manipulation/libero-long"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"}]

Based on the search results, here's what I found about LIBERO benchmark robotics performance in 2026:

## LIBERO Benchmark Overview

LIBERO is a standardized and extensible benchmarking suite that evaluates multi-modal vision-language-action models in diverse robotic manipulation tasks. It contains 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Current SOTA Results

Reported SOTA figures (>95% success) reflect performance under clean, nearly identically distributed train/test splits. However, there's an important caveat: Although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under generalized settings.

## Key Limitations

Recent research has revealed significant issues with how SOTA is reported on LIBERO. Despite achieving over 90% on the standard LIBERO benchmark, the reported scores reflect rote recall rather than genuine task understanding. Overfitting to Train/Test Homogeneity allows rote memorization, with SOTA models collapsing to near-zero success under moderate task, language, object, or environment perturbations.

## Recent Developments

To address these issues, LIBERO-PRO was introduced as an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

The search results indicate that while headline SOTA numbers on LIBERO appear very high (>90%), the actual generalization and robustness of these models remains significantly limited when evaluated under more realistic conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1c97297-bb96-4a28-ace1-852ca7e07998",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "e43ba624-6774-4fe5-8cf4-6d8fa38823ec",
  "sourceToolAssistantUUID": "d1c97297-bb96-4a28-ace1-852ca7e07998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T18:35:31.336Z_

<details><summary>↩ Tool result · `toolu_01XC3BrsjE3oKkFyFvZEQHsc`</summary>

```text
Web search results for query: "UWM RoboCasa LIBERO-PRO evaluation"

Links: [{"title":"Lightwheel: Upgraded RoboCasa and LIBERO benchmarks","url":"https://lightwheel.ai/media/lightwheel-benchmark-anouncement"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"World2Act: Latent Action Post-Training via Skill-Compositional World Models","url":"https://arxiv.org/html/2603.10422"},{"title":"BeingBeyond/Being-H05-2B_robocasa · Hugging Face","url":"https://huggingface.co/BeingBeyond/Being-H05-2B_robocasa"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"RoboCasa: Large-Scale Simulation of Household Tasks for Generalist Robots","url":"https://www.researchgate.net/publication/383894362_RoboCasa_Large-Scale_Simulation_of_Household_Tasks_for_Generalist_Robots"},{"title":"Add RoboCasa environment and imitation learning dataset integration · Issue #2380 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2380"},{"title":"nvidia/Cosmos-Policy-RoboCasa-Predict2-2B · Hugging Face","url":"https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B"},{"title":"GitHub - robocasa/robocasa: RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots · GitHub","url":"https://github.com/robocasa/robocasa"}]

Based on the search results, here's what I found about UWM, RoboCasa, and LIBERO-PRO evaluation:

## UWM (Unified World Models)

Unified World Models (UWM) is a multimodal diffusion transformer that uses separate diffusion timesteps for actions and videos to flexibly learn policies, forward dynamics, inverse dynamics, and video prediction models from both robot and video data. To further evaluate UWM's effectiveness for pretraining, it was tested on LIBERO, a robotic manipulation benchmark containing 100 robotic manipulation tasks, using 90 for pretraining and 5 for evaluation. UWM was found to outperform baseline models in both in-distribution (ID) and out-of-distribution (OOD) settings.

## LIBERO-PRO Evaluation

LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic. LIBERO-PRO is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments.

Experimental results reveal that, although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under the generalized LIBERO-PRO setting. This discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception.

## RoboCasa Context

RoboCasa is a large-scale simulation framework for training generally capable robots to perform everyday tasks, originally released in 2024 by UT Austin researchers. The latest iteration, RoboCasa365, builds upon the original release with significant new functionalities to support large-scale training and benchmarking in sim.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ab5dca4-ce7c-4873-acdf-9b93f24f3c73",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "287431a3-2a9b-4803-9dfc-823fdd543edb",
  "sourceToolAssistantUUID": "3ab5dca4-ce7c-4873-acdf-9b93f24f3c73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:35:31.534Z_

<details><summary>↩ Tool result · `toolu_01Qu8x91re4bPtasyCUNCKkh`</summary>

```text
Web search results for query: "D3P Dynamic Denoising Diffusion Policy"

Links: [{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/html/2508.06804v1"},{"title":"[2508.06804] D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://arxiv.org/abs/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via ...","url":"https://arxiv.org/pdf/2508.06804"},{"title":"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2508.06804v1"},{"title":"(PDF) D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning","url":"https://www.researchgate.net/publication/394438722_D3P_Dynamic_Denoising_Diffusion_Policy_via_Reinforcement_Learning"},{"title":"Denoising Diffusion Policy Optimization","url":"https://www.emergentmind.com/topics/denoising-diffusion-policy-optimization-ddpo"},{"title":"Diffusion Policy Framework","url":"https://www.emergentmind.com/topics/diffusion-policy-dp"},{"title":"D3PM: Discrete Denoising Diffusion Probabilistic Models","url":"https://hunterheidenreich.com/notes/machine-learning/generative-models/discrete-diffusion-models/"},{"title":"Structured Denoising Diffusion Models in Discrete State-Spaces | OpenReview","url":"https://openreview.net/forum?id=h7-XixPCAL"},{"title":"Discrete Denoising Diffusion Models (D3PM)","url":"https://www.emergentmind.com/topics/discrete-denoising-diffusion-probabilistic-models-d3pm"}]

Here are the search results for D3P Dynamic Denoising Diffusion Policy:

## Overview

D3P (Dynamic Denoising Diffusion Policy) is a diffusion policy that dynamically adjusts the number of denoising steps during task execution. It's designed for robotic visuomotor tasks, addressing the challenge that the iterative denoising process poses a major bottleneck for real-time deployment.

## Key Architecture

The D3P architecture consists of a standard noise predicting network that serves as the base diffusion policy, and a lightweight adaptor designed to predict the noise-level strides based on the current observation, which adapts the number of denoising steps for the current action.

## Motivation

Existing acceleration methods apply a fixed number of denoising steps per action, implicitly treating all actions as equally important. However, experiments reveal that robotic tasks often contain a mix of crucial and routine actions, which differ in their impact on task success.

## Training Approach

The dynamic denoising problem is mathematically formulated as a two-layer partially observable Markov decision process (POMDP), and reinforcement learning is used to jointly train both the base diffusion policy and the adaptor.

## Performance Results

On simulated tasks, D3P achieves an averaged 2.2× inference speed-up over baselines without degrading success. On a physical robot, D3P achieves a 1.9× acceleration over the baseline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc4667d7-4ad9-4131-a0ae-42747c398234",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "f469bd8d-0607-46ff-a03f-286e2fd6a351",
  "sourceToolAssistantUUID": "fc4667d7-4ad9-4131-a0ae-42747c398234",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:35:31.958Z_

<details><summary>↩ Tool result · `toolu_01KtyNqSmsyzpaRmLMfbH9qF`</summary>

```text
Web search results for query: "AVDiT NeurIPS 2024 mixture noise audiovisual"

Links: [{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://avdit2024.github.io/"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/15f4cefb0e143c7ad9d40e879b0a9d0c-Paper-Conference.pdf"},{"title":"[Quick Review] A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://liner.com/review/a-versatile-diffusion-transformer-with-mixture-of-noise-levels-for"},{"title":"NeurIPS Poster A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://neurips.cc/virtual/2024/poster/94376"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://arxiv.org/html/2405.13762v1"},{"title":"A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://papers.nips.cc/paper_files/paper/2024/hash/15f4cefb0e143c7ad9d40e879b0a9d0c-Abstract-Conference.html"},{"title":"gwang-kim.github.io/index.md at main · gwang-kim/gwang-kim.github.io","url":"https://github.com/gwang-kim/gwang-kim.github.io/blob/main/index.md"},{"title":"NeurIPS Poster A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation","url":"https://nips.cc/virtual/2024/poster/94376"},{"title":"Audio Imagination: NeurIPS 2024 Workshop AI-Driven Speech, Music, and Sound Generation","url":"https://neurips.cc/virtual/2024/workshop/84706"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=AV-DiT"}]

Based on the search results, here's information about AVDiT and the NeurIPS 2024 paper:

## Overview

AVDiT (Audiovisual Diffusion Transformer) trained with Mixture of Noise Levels (MoNL) tackles diverse audiovisual generation tasks in a single model.

## Key Innovation: Mixture of Noise Levels (MoNL)

The novel mixture of noise levels (MoNL) approach effectively learns arbitrary conditional distributions in the audiovisual space by applying variable noise levels across the temporal dimension and across modalities of the inputs. More specifically, instead of the standard fixed diffusion timestep, the approach applies variable diffusion timesteps across the temporal dimension and across modalities of the inputs.

## Model Architecture

The AVDiT integrates MoNL in a low-dimensional latent space using MAGVIT-v2 for video and SoundStream for audio, addressing high-dimensional signal complexity. AVDiT utilizes a transformer-based network for joint noise prediction, leveraging its ability to model multimodal data and capture complex spatiotemporal and cross-modal relationships.

## Capabilities and Applications

The model handles cross-modal generation (e.g., audio-to-video), multimodal interpolation, and audiovisual continuation tasks. The method enables conditional inference without additional training by selectively injecting clean inputs for conditioning and noisy inputs for generation.

## Performance

Human evaluation consistently demonstrates the superiority of AVDiT with MoNL over MM-Diffusion and other ablations, particularly in maintaining subject consistency and overall quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2e28a47-060f-4f4d-89ba-9ef8cda77ea2",
  "isSidechain": true,
  "promptId": "a59f1fa3-7bc7-47f9-9984-2006ac5278a7",
  "agentId": "a852f7874a86f5aed",
  "type": "user",
  "uuid": "d633a218-a844-46e4-a846-f54b22aacb56",
  "sourceToolAssistantUUID": "a2e28a47-060f-4f4d-89ba-9ef8cda77ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T18:35:52.537Z_

Excellent! I've completed all the searches. Here's a comprehensive report with verified benchmark claims and baseline results:

## LIBERO-100 Benchmark

**Current SOTA & Saturation Status:**
- Headline SOTA scores exceed 90%, with Cosmos-Policy achieving 98.5% average success rate across four LIBERO task suites (98.1% LIBERO-Spatial, 100.0% LIBERO-Object, 98.2% LIBERO-Goal, 97.6% LIBERO-Long)
- **CRITICAL LIMITATION**: The benchmark is saturated with inflated performance estimates. Although models achieve >90% on standard LIBERO, performance collapses to 0.0% under generalized settings with simple perturbations—exposing rote memorization rather than genuine task understanding

Source: [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163), [LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827)

## LIBERO-PRO Benchmark

**Does it exist? YES**
- LIBERO-PRO is a real, published benchmark released October 2025 (arXiv:2510.03827)
- It is an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments
- Key finding: Models achieving >90% on standard LIBERO collapse to 0.0% success on LIBERO-PRO, exposing critical weaknesses in current VLA model generalization

Sources: [LIBERO-PRO arXiv paper](https://arxiv.org/abs/2510.03827), [GitHub repository](https://github.com/Zxy-MLlab/LIBERO-PRO)

## RoboCasa Benchmark

**Current SOTA:**
- RoboCasa365 (published ICLR 2026) contains 365 everyday tasks across 2,500 diverse kitchen environments
- A state-of-the-art model achieved 67.1% average success rate across 24 kitchen manipulation tasks in simulation (confirming your ~67% claim)
- The benchmark spans 60 distinct kitchen activities including manipulation, semantic reasoning, long-horizon planning, and memory-dependent tasks

Sources: [RoboCasa365 arXiv](https://arxiv.org/abs/2603.04356), [NVIDIA Cosmos-Policy-RoboCasa results](https://huggingface.co/nvidia/Cosmos-Policy-RoboCasa-Predict2-2B)

## Fast-WAM Results on LIBERO

**SOTA on LIBERO: Exists but competitive, not leading**
- Paper published March 2026 (arXiv:2603.16666): "Do World Action Models Need Test-time Future Imagination?"
- Fast-WAM achieves competitive results on LIBERO without embodied pretraining, remaining close to imagine-then-execute variants
- Key finding: The main value of video prediction in WAMs lies in learning better world representations during training rather than generating future observations at test time

Source: [Fast-WAM arXiv](https://arxiv.org/abs/2603.16666), [GitHub repository](https://github.com/yuantianyuan01/FastWAM)

## Cosmos-Policy on LIBERO

**SOTA Results: 98.5% average success**
- LIBERO-Spatial: 98.1%
- LIBERO-Object: 100.0%
- LIBERO-Goal: 98.2%
- LIBERO-Long: 97.6%

Model is a 2B-parameter fine-tuned diffusion policy with multimodal outputs (actions, future states, and values).

Sources: [Cosmos Policy arXiv](https://arxiv.org/abs/2601.16163), [Hugging Face model card](https://huggingface.co/nvidia/Cosmos-Policy-LIBERO-Predict2-2B)

## UWM Evaluation on RoboCasa/LIBERO-PRO

**Limited evidence found:**
- Unified World Models (UWM) was evaluated on LIBERO (outperforming baselines in both ID and OOD settings), but I found no evidence of formal evaluation on LIBERO-PRO
- A mention of "Lightwheel" upgrading RoboCasa and LIBERO benchmarks exists, but no detailed UWM results on these upgraded benchmarks

Source: [UWM project page](https://weirdlabuw.github.io/uwm/), [LIBERO-PRO paper](https://arxiv.org/abs/2510.03827)

## Conference Deadlines: CoRL 2026

**Dates VERIFIED:**
- Abstract submission deadline: **May 26, 2026 at 11:59 UTC**
- Paper submission deadline: **May 29, 2026 at 11:59 UTC**
- Conference dates: November 9-12, 2026 in Austin, Texas
- Paper format: Maximum 8 pages (references, acknowledgments, and optional appendix don't count toward limit)

Sources: [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers), [CoRL 2026 Instructions for Authors](https://www.corl.org/contributions/instruction-for-authors)

## AVDiT (NeurIPS 2024)

**CONFIRMED: YES, it exists**
- Full name: "A Versatile Diffusion Transformer with Mixture of Noise Levels for Audiovisual Generation"
- Published at NeurIPS 2024
- Key innovation: Uses Mixture of Noise Levels (MoNL) that applies variable diffusion timesteps across temporal dimension and across modalities
- Handles audio-to-video generation, multimodal interpolation, and audiovisual continuation tasks
- Outperforms MM-Diffusion in human evaluation for subject consistency and quality

Sources: [AVDiT NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/15f4cefb0e143c7ad9d40e879b0a9d0c-Paper-Conference.pdf), [Project page](https://avdit2024.github.io/), [arXiv](https://arxiv.org/abs/2405.13762)

## D3P (Dynamic Denoising Diffusion Policy)

**CONFIRMED: YES, it exists**
- Full name: "D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning"
- Published August 2025 (arXiv:2508.06804)
- Dynamically adjusts the number of denoising steps during task execution to address real-time deployment bottlenecks
- Performance: 2.2× inference speed-up on simulated tasks, 1.9× acceleration on physical robots without degrading success
- Uses RL to jointly train the base diffusion policy and a lightweight adaptor

Sources: [D3P arXiv](https://arxiv.org/abs/2508.06804), [alphaXiv page](https://www.alphaxiv.org/abs/2508.06804v1)

---

## Summary of Findings

1. **LIBERO-100 is saturated with inflated metrics** - while headlines show >90%, generalization collapses to 0% under perturbations
2. **LIBERO-PRO is real and damaging** - exposes that current SOTA models rely on memorization, not understanding
3. **RoboCasa SOTA ~67%** - confirmed with ICLR 2026 publication
4. **Fast-WAM is competitive but not leading** on LIBERO
5. **Cosmos-Policy dominates at 98.5%** on standard LIBERO
6. **CoRL 2026 deadlines confirmed** - abstract May 26, paper May 29
7. **AVDiT and D3P both exist** and are recent publications with specific technical contributions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d633a218-a844-46e4-a846-f54b22aacb56",
  "isSidechain": true,
  "agentId": "a852f7874a86f5aed",
  "requestId": "req_011CauNU7pBfYSPxRn9JDFZV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e96297fa-55d6-4334-b07e-5dc6cec0942a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "fd40ea79-6fbb-4b7b-a986-d01c903c50a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01D413T8Z3BpYe9U9zxw9NrZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 9290,
      "cache_read_input_tokens": 14514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---
