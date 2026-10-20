# Research conversation: You are helping me with a literature review. I need to verify whether Prioritized Experience Replay (PER) has been appli

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5721a44efe1d1515.jsonl`
- **Structured JSON:** [`2880553c5859869ea5fc.json`](../../sessions/28/2880553c5859869ea5fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-13T05:43:33.726Z_

You are helping me with a literature review. I need to verify whether Prioritized Experience Replay (PER) has been applied to imitation learning or supervised fine-tuning of large models. Search for:

1. "prioritized experience replay imitation learning" 
2. "prioritized replay supervised fine-tuning"
3. "adaptive data sampling imitation learning robot 2025 2026"
4. "experience replay demonstration learning robotics"
5. "TD error imitation learning priority"
6. "curriculum learning demonstration data robot 2025 2026"
7. "Freshness-Aware Prioritized Experience Replay" (verify this paper exists)
8. "ExpReS-VLA" (verify this paper exists)
9. "Demo-SCORE demonstration curation" (verify this paper exists)

For each search use WebSearch and report all relevant results with titles, URLs, and descriptions. I specifically need to know:
- Has anyone applied PER or TD-error-based prioritization to imitation learning (not RL)?
- Has anyone done adaptive/online data selection during SFT training of VLA or LLM models?
- Do the papers "Freshness-Aware PER", "ExpReS-VLA", and "Demo-SCORE" actually exist?

Be thorough and report everything you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "2042d64e-9f88-4621-b393-d519624c1bbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T05:43:33.729Z_

```json
{
  "parentUuid": "2042d64e-9f88-4621-b393-d519624c1bbe",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
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
  "uuid": "fce8735f-f4f0-4436-b4ff-ef87b69ed3d2",
  "timestamp": "2026-05-13T05:43:33.729Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T05:43:36.399Z_



I'll start by loading the WebSearch tool schema, then run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fce8735f-f4f0-4436-b4ff-ef87b69ed3d2",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz32YoS6KzZ3U2guxAQY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a015fa2-b961-49f2-a8a4-7c84e759b1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDqPXSXaXV73Jpf6zeiNfj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 843,
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

_source line 4 · 2026-05-13T05:43:36.620Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GCVmzdXFgZj3dquNBce2GH`</summary>

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
  "parentUuid": "7a015fa2-b961-49f2-a8a4-7c84e759b1bc",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz32YoS6KzZ3U2guxAQY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0508c63f-85ce-4b81-821b-ec87f3ad7664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDqPXSXaXV73Jpf6zeiNfj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 8223,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 843
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 843,
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

_source line 5 · 2026-05-13T05:43:36.623Z_

<details><summary>↩ Tool result · `toolu_01GCVmzdXFgZj3dquNBce2GH`</summary>

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
  "parentUuid": "0508c63f-85ce-4b81-821b-ec87f3ad7664",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "690dabb3-35be-4c60-b980-fa3ba3f3ecc6",
  "sourceToolAssistantUUID": "0508c63f-85ce-4b81-821b-ec87f3ad7664",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T05:43:39.002Z_



Now let me run all 9 searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "690dabb3-35be-4c60-b980-fa3ba3f3ecc6",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz32mTwUbirZ4U2qSwTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bd1212f-0aaf-4685-ac17-15d4c580bdbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9NUMLNCxAdGEFNt8z3Em9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 7 · 2026-05-13T05:43:39.224Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012NL3ScrKeUzV7xNZ1kKQtZ`</summary>

```json
{
  "query": "prioritized experience replay imitation learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bd1212f-0aaf-4685-ac17-15d4c580bdbf",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz32mTwUbirZ4U2qSwTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "904dc980-9136-4c87-867d-2e7de8ccce6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K9NUMLNCxAdGEFNt8z3Em9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9066,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 72,
          "cache_read_input_tokens": 9066,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
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

_source line 8 · 2026-05-13T05:43:46.162Z_

<details><summary>↩ Tool result · `toolu_012NL3ScrKeUzV7xNZ1kKQtZ`</summary>

```text
Web search results for query: "prioritized experience replay imitation learning"

Links: [{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"GitHub - CHUENGMINCHOU/AW-PER-A2C: The test code for the paper \"Attention-based advantage actor-critic algorithm with prioritized experience replay for complex 2-D robotic motion planning\".","url":"https://github.com/CHUENGMINCHOU/AW-PER-A2C"},{"title":"Attention-based advantage actor-critic algorithm with prioritized experience replay for complex 2-D robotic motion planning | Journal of Intelligent Manufacturing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10845-022-01988-z"},{"title":"Prioritized Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"},{"title":"Understanding Prioritized Experience Replay","url":"https://danieltakeshi.github.io/2019/07/14/per/"},{"title":"Distributed Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=H1Dy---0Z"},{"title":"Prioritized experience replay based on dynamics priority | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-56673-3"},{"title":"Understanding and Mitigating the Limitations of Prioritized Experience Replay","url":"https://proceedings.mlr.press/v180/pan22a/pan22a.pdf"},{"title":"Prioritized Experience Replay Explained","url":"https://paperswithcode.com/method/prioritized-experience-replay"},{"title":"Prioritized experience replay based on dynamics priority - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10933423/"}]

Based on the search results, here's information about prioritized experience replay and its connection to imitation learning:

## Prioritized Experience Replay (PER)

Experience replay lets online reinforcement learning agents remember and reuse experiences from the past. In prior work, experience transitions were uniformly sampled from a replay memory. However, a framework for prioritizing experience was developed, so as to replay important transitions more frequently, and therefore learn more efficiently.

Prioritized Experience Replay (PER) replaces uniform buffer sampling with TD-error-proportional priorities. The intuition is to more frequently replay transitions with high expected learning progress, as measured by the magnitude of their temporal-difference (TD) error. This prioritization can lead to a loss of diversity, which is alleviated with stochastic prioritization, and introduces bias, which is corrected with importance sampling.

## Connection to Imitation Learning

For imitation learning, replay of demonstrations has been used to mitigate distribution shift in DAggerstyle algorithms. Additionally, prioritization can be applied when adding extra samples to the buffer from a "demonstrator" as in Deep Q-Learning from Demonstrations, where one can adjust the raw priority values to increase those from the demonstrator.

Existing methods depend heavily on expert experiences to enhance the convergence speed of the networks by initializing them via imitation learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "904dc980-9136-4c87-867d-2e7de8ccce6c",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "51cafe3e-0415-4b21-8a07-56191595e339",
  "sourceToolAssistantUUID": "904dc980-9136-4c87-867d-2e7de8ccce6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T05:43:49.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RsAwY44vsKJozDoU8SipnP`</summary>

```json
{
  "query": "prioritized replay supervised fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51cafe3e-0415-4b21-8a07-56191595e339",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72919e17-b3d5-4893-b241-654e982464aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 10 · 2026-05-13T05:43:49.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EH87n92MAJTyN2j2Z5WbpV`</summary>

```json
{
  "query": "adaptive data sampling imitation learning robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72919e17-b3d5-4893-b241-654e982464aa",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b823ad85-d998-40c5-859e-3503e0244c48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 11 · 2026-05-13T05:43:49.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A9DoWcZF6bvKu4QwU8suw4`</summary>

```json
{
  "query": "experience replay demonstration learning robotics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b823ad85-d998-40c5-859e-3503e0244c48",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30df75be-4b56-4a4b-8321-547bf45667d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 12 · 2026-05-13T05:43:50.582Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tr3TozmpUC54q9HDfxt4Ro`</summary>

```json
{
  "query": "TD error imitation learning priority"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30df75be-4b56-4a4b-8321-547bf45667d1",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3eada84-30e8-4d69-bfc5-ebef11ecfdb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 13 · 2026-05-13T05:43:50.964Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CJSD8AzNdS6CUz8r4oufC2`</summary>

```json
{
  "query": "curriculum learning demonstration data robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3eada84-30e8-4d69-bfc5-ebef11ecfdb6",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba11780b-a330-424e-94c9-ace16fb47072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 14 · 2026-05-13T05:43:51.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wacno6foupbjQ3VQ1wo12w`</summary>

```json
{
  "query": "\"Freshness-Aware Prioritized Experience Replay\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba11780b-a330-424e-94c9-ace16fb47072",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00c99d10-5b3f-4cbe-bb5f-aafff3e44592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 15 · 2026-05-13T05:43:52.370Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U1rzqrsxX6pBQhcYFDy7GF`</summary>

```json
{
  "query": "\"ExpReS-VLA\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00c99d10-5b3f-4cbe-bb5f-aafff3e44592",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "394873e8-ab3d-4047-96bb-bd6406f41c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 873,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 16 · 2026-05-13T05:43:52.714Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BNBTVALUYWckSiWKG4esGX`</summary>

```json
{
  "query": "\"Demo-SCORE\" demonstration curation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "394873e8-ab3d-4047-96bb-bd6406f41c41",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz33TxzveA62pZMNnzPh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00833d5c-cd98-4fc1-806f-3b609789fb3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsPuJeb7Z8XfJ3Yrdc3bma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 873,
      "cache_read_input_tokens": 10479,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 10479,
          "cache_creation_input_tokens": 873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 873,
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

_source line 17 · 2026-05-13T05:43:56.882Z_

<details><summary>↩ Tool result · `toolu_01Tr3TozmpUC54q9HDfxt4Ro`</summary>

```text
Web search results for query: "TD error imitation learning priority"

Links: [{"title":"Temporal difference learning - Wikipedia","url":"https://en.wikipedia.org/wiki/Temporal_difference_learning"},{"title":"Temporal-diﬀerence methods Milica Gaˇsi´c","url":"https://www.cs.hhu.de/fileadmin/redaktion/Fakultaeten/Mathematisch-Naturwissenschaftliche_Fakultaet/Informatik/Dialog_Systems_and_Machine_Learning/Lectures_RL/L3.pdf"},{"title":"Chapter 9 Temporal-Difference Learning","url":"http://web.stanford.edu/group/pdplab/pdphandbook/handbookch10.html"},{"title":"Temporal-difference learning - ML Compiled - Read the Docs","url":"https://ml-compiled.readthedocs.io/en/latest/td.html"},{"title":"Discerning Temporal Difference Learning","url":"https://arxiv.org/html/2310.08091v2"},{"title":"What is a TD error in reinforcement learning? - Quora","url":"https://www.quora.com/What-is-a-TD-error-in-reinforcement-learning"},{"title":"RIZE: Adaptive Regularization for Imitation Learning","url":"https://arxiv.org/html/2502.20089"},{"title":"Reinforcement Learning: Temporal Difference (TD) Learning – Jordan J Hood","url":"https://www.lancaster.ac.uk/stor-i-student-sites/jordan-j-hood/2021/04/12/reinforcement-learning-temporal-difference-td-learning/"},{"title":"Understanding Prioritized Experience Replay","url":"https://danieltakeshi.github.io/2019/07/14/per/"},{"title":"Temporal-Difference (TD) learning | Towards Data Science","url":"https://towardsdatascience.com/temporal-difference-learning-47b4a7205ca8/"}]

I've found relevant information about TD error, imitation learning, and priority-based sampling. Here's a summary of the key findings:

## TD Error and Priority in Reinforcement Learning

The TD error is the difference between the current estimate for V_t, the discounted value estimate of V_{t+1} and the actual reward gained from transitioning between states.

## Prioritized Experience Replay with TD Error

Prioritized experience replay (PER) updates the value function by assigning a priority to each sample, thus giving precedence to samples with higher significance, specifically those proportional to the sampled absolute TD error. The approach more frequently replays transitions with high expected learning progress, as measured by the magnitude of their temporal-difference (TD) error.

## Application in Imitation Learning

In the context of imitation learning, TD error has been incorporated into recent methods. LSIQ minimizes the chi-squared divergence between expert and mixture distributions, resulting in a squared temporal difference (TD) error objective. Additionally, the Rainbow DQN paper showed that prioritization was perhaps the most essential extension for obtaining high scores on Atari games.

The general principle is that samples or experiences with larger TD errors represent cases where the agent's predictions were significantly wrong, making them valuable learning opportunities that merit higher priority during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3eada84-30e8-4d69-bfc5-ebef11ecfdb6",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "3660af3a-e293-4068-bc82-4aac59be6e91",
  "sourceToolAssistantUUID": "d3eada84-30e8-4d69-bfc5-ebef11ecfdb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T05:43:56.989Z_

<details><summary>↩ Tool result · `toolu_01EH87n92MAJTyN2j2Z5WbpV`</summary>

```text
Web search results for query: "adaptive data sampling imitation learning robot 2025 2026"

Links: [{"title":"Frontiers | Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682437/full"},{"title":"Imitation learning for legged robot locomotion: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1678567/pdf"},{"title":"Advancements in humanoid robot dynamics and learning-based locomotion control methods","url":"https://www.oaepublish.com/articles/ir.2025.32"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"Data Scaling Laws in Imitation Learning for Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=pISLZG7ktL"},{"title":"Foundation Models in Robotics: A Comprehensive Review of Methods, Models, Datasets, Challenges and Future Research Directions","url":"https://arxiv.org/html/2604.15395v1"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"A survey on imitation learning for contact-rich tasks in robotics - Toshiaki Tsuji, Yasuhiro Kato, Gokhan Solak, Heng Zhang, Tadej Petrič, Francesco Nori, Arash Ajoudani, 2026","url":"https://journals.sagepub.com/doi/10.1177/02783649261417694"},{"title":"Frontiers | Leveraging imitation learning in agricultural robotics: a comprehensive survey and comparative analysis","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1441312/full"},{"title":"AI Robotics: A Field Report on Imitation Learning with LeRobot","url":"https://www.ml6.eu/en/blog/ai-robotics-a-field-report-on-imitation-learning-with-lerobot"}]

Here are the search results for "adaptive data sampling imitation learning robot 2025 2026":

## Key Findings

The search reveals several relevant areas of research and development in this space:

### Imitation Learning for Robot Manipulation

Dexterous manipulation in humanoid robotics demands precise, adaptable, and sample-efficient learning methods. Traditional approaches such as reinforcement learning and imitation learning have made significant strides, but they often struggle with challenges including high-dimensional control, limited training data, and covariate shift.

### Interactive and Adaptive Approaches

Human-in-the-loop approaches ensure adaptability, enhance sample efficiency, and mitigate covariate shift by dynamically guiding the learning process. Recent papers highlight approaches like RoboCopilot: Human-in-the-loop Interactive Imitation Learning for Robot Manipulation and work on Elastic Motion Policy: An Adaptive Dynamical System for Robust and Efficient One-Shot Imitation Learning.

### Data-Driven Learning for Contact-Rich Tasks

Recent advancements in machine learning have accelerated resolution of contact dynamics problems by enabling robots to learn intricate interaction dynamics directly from data, and this shift from traditional control methods to data-driven learning has yielded significant improvements in robustness and adaptability.

### Sample Efficiency and Data Scaling

Comprehensive empirical studies on data scaling in imitation learning investigate how policy generalization performance changes with the number of training environments, objects, and demonstrations, with researchers collecting over 40,000 demonstrations and executing more than 15,000 real-world robot rollouts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b823ad85-d998-40c5-859e-3503e0244c48",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "5523d75b-c15a-464f-a87c-49bdeac34986",
  "sourceToolAssistantUUID": "b823ad85-d998-40c5-859e-3503e0244c48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T05:43:57.294Z_

<details><summary>↩ Tool result · `toolu_01RsAwY44vsKJozDoU8SipnP`</summary>

```text
Web search results for query: "prioritized replay supervised fine-tuning"

Links: [{"title":"Improved exploration–exploitation trade-off through adaptive prioritized experience replay - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231224016072"},{"title":"FIRE: Fine-Tuning with Integrated Replay & Efficiency","url":"https://www.emergentmind.com/topics/fine-tuning-with-integrated-replay-and-efficiency-fire"},{"title":"Understanding and Mitigating the Limitations of Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=HBlNGvIicg9"},{"title":"Prioritized Sequence Experience Replay","url":"https://arxiv.org/pdf/1905.12726"},{"title":"Understanding Prioritized Experience Replay","url":"https://danieltakeshi.github.io/2019/07/14/per/"},{"title":"Prioritized Replay for RL Post-training","url":"https://arxiv.org/html/2601.02648"},{"title":"DISTRIBUTED PRIORITIZED EXPERIENCE REPLAY","url":"https://openreview.net/pdf?id=H1Dy---0Z"},{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"Model-augmented Prioritized Experience Replay | OpenReview","url":"https://openreview.net/forum?id=WuEiafqdy9H"},{"title":"[1803.00933] Distributed Prioritized Experience Replay","url":"https://ar5iv.labs.arxiv.org/html/1803.00933"}]

I found several relevant results about prioritized replay and supervised fine-tuning. Here's what the search revealed:

## Key Findings

**Prioritized Replay in Supervised Fine-tuning:**

Fine-Tuning with Integrated Replay and Efficiency (FIRE) is a data-centric framework for efficient adaptation and continual improvement of machine learning models, primarily targeting LLMs, code generation systems, and machine-learned interatomic potentials. FIRE encompasses a suite of synergistic methodologies that combine replay, targeted data selection, regularization, and algorithmic innovations, enabling sample-efficient, stable, and scalable fine-tuning for both supervised and reinforcement learning scenarios.

**Possibility and Pass-rate Prioritized Experience Replay (PPER):**

In code generation, beam search is used to collect multiple candidate programs per prompt, each scored by generation likelihood and empirical pass rate. The P2Value metric, a convex combination of model and empirical signals, governs replay prioritization, which is implemented through rank-based sampling.

**Prioritized Replay in RL Fine-tuning:**

The use of prioritized replay directly amplifies the magnitude of the learning signal. Because prioritized sampling favors problems with high advantage variance, the expected per-update advantage under prioritized GRPO is larger than it would be under uniform sampling. Since the policy-gradient loss scales linearly with advantage, this amplification translates into larger effective gradients during optimization.

The search results show that prioritized replay is being applied across various machine learning contexts, including supervised fine-tuning of language models, code generation, and reinforcement learning post-training applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72919e17-b3d5-4893-b241-654e982464aa",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "be59b011-498f-407e-b400-d5564e038a27",
  "sourceToolAssistantUUID": "72919e17-b3d5-4893-b241-654e982464aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T05:43:57.346Z_

<details><summary>↩ Tool result · `toolu_01CJSD8AzNdS6CUz8r4oufC2`</summary>

```text
Web search results for query: "curriculum learning demonstration data robot 2025 2026"

Links: [{"title":"Human-Centered Robot Learning in the Era of Big Data ...","url":"https://human-cenetered-robot-learning-workshop.github.io/icra-2025/"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"[2503.02277] Active Robot Curriculum Learning from Online Human Demonstrations","url":"https://arxiv.org/abs/2503.02277"},{"title":"Learning Generalizable Robot Policy with Human Demonstration Video as a Prompt","url":"https://arxiv.org/html/2505.20795"},{"title":"Hierarchical reinforcement learning with curriculum demonstrations and goal-guided policies for sequential robotic manipulation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197625008668"},{"title":"Robotics Learning Roadmap: From Beginner to Expert (2026) | Coursera","url":"https://www.coursera.org/resources/robotics-learning-roadmap"},{"title":"Learning a Thousand Tasks in a Day | OpenReview","url":"https://openreview.net/forum?id=5e48yYecV5"},{"title":"Frontiers | CARE: towards customized assistive robot-based education","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1474741/full"},{"title":"Robotic arm successfully learns 1,000 manipulation tasks in one day","url":"https://techxplore.com/news/2025-12-robotic-arm-successfully-tasks-day.html"},{"title":"[2511.10110] Learning a Thousand Tasks in a Day","url":"https://arxiv.org/abs/2511.10110"}]

Based on the search results, here are the key findings related to curriculum learning, demonstration data, and robot learning in 2025-2026:

## Active Robot Curriculum Learning

A recent study proposes an active learning from demonstrations method that optimizes the query sequence of online human demonstrations via Curriculum Learning, where demonstrators are guided to provide demonstrations in situations of gradually increasing difficulty.

## Robot Learning from Demonstrations

Several noteworthy advances in robot learning from demonstrations have emerged:

- One approach introduces a two-stage framework that utilizes human demonstrations to learn a generalizable robot policy that can directly take human demonstration video as a prompt and perform new tasks without any new teleoperation data and model finetuning.

- The MT3 (multi-task trajectory transfer) approach is designed to retrieve and decompose demonstration data, finding demonstrations relevant to the task and adapting them to the target object while planning the robot's motions using pose estimation.

## Scaling to Large Numbers of Tasks

A significant breakthrough in 2025 demonstrated the efficiency of demonstration-based learning: Multi-Task Trajectory Transfer (MT3), an imitation learning method based on decomposition and retrieval, learns everyday manipulation tasks from as little as a single demonstration each while generalizing to novel object instances, enabling robots to learn 1,000 distinct everyday tasks in under 24 hours of human demonstrator time.

## World Models and Robot Learning

Recent research also explores world models for robot learning, where actionable world models should provide three core capabilities: foresight (anticipating future states), imagination-driven planning, and data amplification (synthesizing additional demonstrations).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba11780b-a330-424e-94c9-ace16fb47072",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "aabe4521-a154-4bf2-8b3a-8cbd8e525e19",
  "sourceToolAssistantUUID": "ba11780b-a330-424e-94c9-ace16fb47072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T05:43:57.524Z_

<details><summary>↩ Tool result · `toolu_01A9DoWcZF6bvKu4QwU8suw4`</summary>

```text
Web search results for query: "experience replay demonstration learning robotics"

Links: [{"title":"Frontiers | Solving robotics tasks with prior demonstration via exploration-efficient deep reinforcement learning","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1682200/full"},{"title":"Efficient hindsight reinforcement learning using demonstrations for robotic tasks with sparse rewards - Guoyu Zuo, Qishen Zhao, Jiahao Lu, Jiangeng Li, 2020","url":"https://journals.sagepub.com/doi/full/10.1177/1729881419898342"},{"title":"Reinforcement Learning for Robot Dexterous In-Hand ...","url":"https://www.ijres.org/papers/Volume-13/Issue-6/1306164183.pdf"},{"title":"Reinforcement learning from expert demonstrations with application to redundant robot control - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197622007436"},{"title":"Dynamic Experience Replay Jieliang Luo and Hui Li","url":"http://proceedings.mlr.press/v100/luo20a/luo20a.pdf"},{"title":"How to Train Your Robots? The Impact of Demonstration Modality on Imitation Learning","url":"https://arxiv.org/html/2503.07017v1"},{"title":"Forgetful experience replay in hierarchical reinforcement learning from expert demonstrations▪ | Knowledge-Based Systems","url":"https://dl.acm.org/doi/10.1016/j.knosys.2021.106844"},{"title":"Learning To Manipulate From Demonstration - TU Berlin","url":"https://www.tu.berlin/en/robotics/projects/ongoing-projects/learning-to-manipulate-from-demonstration"},{"title":"Multi-Objective Evolutionary Hindsight Experience Replay for Robot Manipulation Tasks | Proceedings of the Genetic and Evolutionary Computation Conference","url":"https://dl.acm.org/doi/10.1145/3638529.3654045"},{"title":"[2202.06843] Continual Learning from Demonstration of Robotics Skills","url":"https://arxiv.org/abs/2202.06843"}]

Based on the search results, here's what I found about experience replay and demonstration learning in robotics:

## Experience Replay in Demonstration Learning for Robotics

Early studies initialize training by mixing offline demonstrations and online interaction in the replay buffer and use a prioritized replay mechanism to enable the reinforcement learning (RL) policy for efficient exploration.

### Key Approaches

**Combining Demonstrations with Experience Replay:**
DDPG from demonstrations (DDPGfD) divides learning into two phases. In the pre-training phase, the agent stores the demonstration's trajectories in a replay buffer to learn in a supervised manner. And the fine-tuning phase, where the agent learns by interacting with the environment. DDPGfD also makes use of prioritized experience replay to sample transitions across the demonstrations and the agent data generated by interacting with the environment.

**Hindsight Experience Replay (HER):**
Hindsight Experience Replay (HER) helps agents learn from failed attempts by redefining goals retrospectively. Hindsight experience replay (HER) is a goal relabelling technique typically used with off-policy deep reinforcement learning algorithms to solve goal-oriented tasks; it is well suited to robotic manipulation tasks that deliver only sparse rewards.

**Dynamic Experience Replay:**
Dynamic Experience Replay (DER) allows RL algorithms to work effectively, with ablation studies showing that Dynamic Experience Replay is a crucial ingredient that either largely shortens the training time in these challenging environments or solves the tasks that the vanilla Ape-X DDPG cannot solve.

### Benefits

Effectively leveraging prior demonstrations to facilitate efficient exploration is considered a promising strategy for the broad application of off-policy DRL in real-world industrial robotics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30df75be-4b56-4a4b-8321-547bf45667d1",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "337a47ca-8581-4199-948c-b9d83bbbaca8",
  "sourceToolAssistantUUID": "30df75be-4b56-4a4b-8321-547bf45667d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T05:43:58.906Z_

<details><summary>↩ Tool result · `toolu_01Wacno6foupbjQ3VQ1wo12w`</summary>

```text
Web search results for query: ""Freshness-Aware Prioritized Experience Replay""

Links: [{"title":"[2604.16918] Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/abs/2604.16918"},{"title":"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/html/2604.16918"},{"title":"Fresher Experience Plays a More Important Role in Prioritized Experience Replay | MDPI","url":"https://www.mdpi.com/2076-3417/12/23/12489"},{"title":"Prioritized Experience Replay | Request PDF","url":"https://www.researchgate.net/publication/319770330_Prioritized_Experience_Replay"},{"title":"Prioritized Experience Replay: Turning Memory into a Curriculum | by Satyam Mishra | Medium","url":"https://satyamcser.medium.com/prioritized-experience-replay-turning-memory-into-a-curriculum-fe595ae355fd"},{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"Improved exploration–exploitation trade-off through adaptive prioritized experience replay - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231224016072"},{"title":"Understanding Prioritized Experience Replay","url":"https://danieltakeshi.github.io/2019/07/14/per/"},{"title":"Revisiting Prioritized Experience Replay: A Value Perspective | OpenReview","url":"https://openreview.net/forum?id=jAJrc-kzVd0"},{"title":"What is Prioritized Experience Replay (PER)?","url":"https://milvus.io/ai-quick-reference/what-is-prioritized-experience-replay-per"}]

Based on the search results, here's what I found about "Freshness-Aware Prioritized Experience Replay":

## Overview

Freshness-Aware Prioritized Experience Replay (FreshPER) is the first to successfully apply Prioritized Experience Replay to LLM and VLM reinforcement learning.

## The Problem It Addresses

While Experience Replay drives sample efficiency in classic RL by allowing agents to reuse past trajectories and prioritize informative ones, directly applying Prioritized Experience Replay (PER) to LLMs fails because the rapid policy evolution of billion-parameter models renders stored priorities stale, causing old high-priority trajectories to dominate sampling long after they have become uninformative.

## The Solution

Freshness-Aware PER addresses this priority staleness problem by augmenting any PER-based priority with a multiplicative exponential age decay grounded in effective sample size analysis. The key enabler is freshness-aware age decay, which addresses the priority staleness problem caused by the rapid policy evolution of billion-parameter models.

## Performance Results

Evaluations across eight environments with models ranging from 0.5B to 7B confirm that FreshPER consistently outperforms both on-policy baselines and standard PER, with particularly large gains on challenging agentic tasks.

The paper was published recently on arXiv (about 4 weeks ago as of the search date).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00c99d10-5b3f-4cbe-bb5f-aafff3e44592",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "22825d2e-338d-42f8-a209-198acb143878",
  "sourceToolAssistantUUID": "00c99d10-5b3f-4cbe-bb5f-aafff3e44592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T05:44:00.197Z_

<details><summary>↩ Tool result · `toolu_01U1rzqrsxX6pBQhcYFDy7GF`</summary>

```text
Web search results for query: ""ExpReS-VLA""

Links: [{"title":"[2511.06202] ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/abs/2511.06202"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/html/2511.06202v1"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through","url":"https://arxiv.org/pdf/2511.06202"},{"title":"Physical robot evaluation tasks. We evaluate ExpReS-VLA on five... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Physical-robot-evaluation-tasks-We-evaluate-ExpReS-VLA-on-five-manipulation-tasks-using_fig3_397480729"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.06202v1"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies | OpenReview","url":"https://openreview.net/forum?id=YWeNCMxdhM"},{"title":"(PDF) ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://www.researchgate.net/publication/397480729_ExpReS-VLA_Specializing_Vision-Language-Action_Models_Through_Experience_Replay_and_Retrieval"},{"title":"Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning | OpenReview","url":"https://openreview.net/forum?id=8xTDnj39Ti"},{"title":"Expression of VLA-4 on thymocytes. Maturation stage-associated transition and its correlation with their capacity to adhere to thymic stromal cells - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/1431122/"},{"title":"JCI - Coexpression of two fibronectin receptors, VLA-4 and VLA-5, by immature human erythroblastic precursor cells.","url":"https://www.jci.org/articles/view/115002"}]

Based on the search results, here's what I found about ExpReS-VLA:

## Overview

ExpReS-VLA (EXPierence replayed, REtrieval augmented, Specialized VLA) is a method that enables rapid on-device adaptation of pre-trained Vision-Language-Action models to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation.

## Key Features

Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization.

ExpReS-VLA maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs.

During deployment, ExpReS-VLA retrieves the k most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories.

## Performance Results

Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA.

Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning, with adaptation completing in 31 seconds using 12 demonstrations on a single RTX 5090.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "394873e8-ab3d-4047-96bb-bd6406f41c41",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "6af06a57-470b-4dfa-9ebe-93ce4b3c0746",
  "sourceToolAssistantUUID": "394873e8-ab3d-4047-96bb-bd6406f41c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T05:44:02.660Z_

<details><summary>↩ Tool result · `toolu_01BNBTVALUYWckSiWKG4esGX`</summary>

```text
Web search results for query: ""Demo-SCORE" demonstration curation"

Links: [{"title":"Demo-SCORE: Curating Demonstrations using Online Experience","url":"https://anniesch.github.io/demo-score/"},{"title":"[2503.03707] Curating Demonstrations using Online Experience","url":"https://arxiv.org/abs/2503.03707"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"[Literature Review] Curating Demonstrations using Online Experience","url":"https://www.themoonlight.io/en/review/curating-demonstrations-using-online-experience"},{"title":"Curating Demonstrations using Online Experience · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/71/"},{"title":"Illustration of Demo-SCORE. Our method self-curates demonstrations... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/llustration-of-Demo-SCORE-Our-method-self-curates-demonstrations-through-online-robot_fig2_389617044"},{"title":"Teaching Demo Score Sheet Batch 2 April 20 2024 | PDF | Classroom Management | Lesson Plan","url":"https://www.scribd.com/document/727899516/Teaching-Demo-Score-Sheet-Batch-2-April-20-2024"},{"title":"demo-score.com – L'Agence de Notation Citoyenne pour la ...","url":"https://demo-score.com/"}]

Based on the search results, here's what I found about Demo-SCORE:

## Overview

Demo-SCORE is a method for robots to self-curate based on online robot experience. It's a method aimed at improving robotic learning from heterogeneous demonstration datasets.

## The Problem

These datasets often contain demonstrations with varying levels of quality, which can hinder a robot's performance when trying to learn a task through imitation learning. Unreliable or underrepresented strategies might lead to suboptimal performance during test phases.

## How It Works

The method trains and cross-validates a classifier to discern successful policy roll-outs from unsuccessful ones and uses the classifier to filter heterogeneous demonstration datasets. More specifically, the method self-curates demonstrations through online robot experience in four steps: (i) train a policy on the full demonstration set; (ii) evaluate the policy by generating rollouts with different checkpoints; (iii) use these rollouts to train and cross-validate a classifier that distinguishes between success and failure trajectories; (iv) filter out unreliable demonstrations based on the learned classifier.

## Results

Experiments in simulation and the real world show that Demo-SCORE can effectively identify suboptimal demonstrations without manual curation, and achieves over 15-35% higher absolute success rate in the resulting policy compared to the base policy trained with all original demonstrations.

## Key Advantage

The method does not require any additional human labeling beyond the detection of success or failure during the rollout phase, making Demo-SCORE scalable to large, diverse demonstration datasets where traditional human annotation would be challenging and costly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00833d5c-cd98-4fc1-806f-3b609789fb3c",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "91baf3ed-31e1-4c74-b726-79715631ba67",
  "sourceToolAssistantUUID": "00833d5c-cd98-4fc1-806f-3b609789fb3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-13T05:44:05.194Z_

Now let me do a few follow-up searches to get more detail on the most relevant findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91baf3ed-31e1-4c74-b726-79715631ba67",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz34gZ4w56sSBLbb6Sb7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0712c28-f9d0-46e6-8334-b8b07a6ee038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mUSEmpsXnHniBoWYKmj79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7593,
      "cache_read_input_tokens": 11352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7593,
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

_source line 26 · 2026-05-13T05:44:06.615Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmXbNmvbCMgyzn17jdrVSo`</summary>

```json
{
  "query": "arxiv 2604.16918 FreshPER LLM VLM reinforcement learning details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0712c28-f9d0-46e6-8334-b8b07a6ee038",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz34gZ4w56sSBLbb6Sb7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "284e74ba-a67a-4696-9cd3-405de9ea217b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mUSEmpsXnHniBoWYKmj79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7593,
      "cache_read_input_tokens": 11352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7593,
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

_source line 27 · 2026-05-13T05:44:07.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TYyKr6b71WnDxDTBfGjsXm`</summary>

```json
{
  "query": "prioritized replay RL post-training arxiv 2601.02648"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "284e74ba-a67a-4696-9cd3-405de9ea217b",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz34gZ4w56sSBLbb6Sb7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dfb576e-ffb4-4167-b35c-f22fb5e9df9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mUSEmpsXnHniBoWYKmj79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7593,
      "cache_read_input_tokens": 11352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7593,
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

_source line 28 · 2026-05-13T05:44:08.078Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013pTmU8MEaowMqtoky4C8hm`</summary>

```json
{
  "query": "online data selection during supervised fine-tuning LLM VLA training loss priority"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dfb576e-ffb4-4167-b35c-f22fb5e9df9d",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz34gZ4w56sSBLbb6Sb7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bfa0e941-920f-43b2-8112-ce932a9876be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mUSEmpsXnHniBoWYKmj79",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7593,
      "cache_read_input_tokens": 11352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7593,
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

_source line 29 · 2026-05-13T05:44:08.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TQ7u7SNi2TJqc7NK4cRbXb`</summary>

```json
{
  "query": "DDPGfD \"deep Q-learning from demonstrations\" prioritized experience replay imitation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfa0e941-920f-43b2-8112-ce932a9876be",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz34gZ4w56sSBLbb6Sb7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "327bb475-9785-418b-a074-ffb627131510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mUSEmpsXnHniBoWYKmj79",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7593,
      "cache_read_input_tokens": 11352,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7593
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 11352,
          "cache_creation_input_tokens": 7593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7593,
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

_source line 30 · 2026-05-13T05:44:14.019Z_

<details><summary>↩ Tool result · `toolu_01TYyKr6b71WnDxDTBfGjsXm`</summary>

```text
Web search results for query: "prioritized replay RL post-training arxiv 2601.02648"

Links: [{"title":"[2601.02648] Prioritized Replay for RL Post-training","url":"https://arxiv.org/abs/2601.02648"},{"title":"Prioritized Replay for RL Post-training Mehdi Fatemi mehdi.fatemi@ieee.org","url":"https://www.arxiv.org/pdf/2601.02648"},{"title":"Prioritized Replay for RL Post-training","url":"https://arxiv.org/html/2601.02648"},{"title":"Investigating the Interplay of Prioritized Replay and Generalization","url":"https://arxiv.org/html/2407.09702v2"},{"title":"Experience Replay with Random Reshuffling","url":"https://arxiv.org/html/2503.02269v1"},{"title":"Reliability-Adjusted Prioritized Experience Replay","url":"https://arxiv.org/html/2506.18482v2"},{"title":"[1511.05952] Prioritized Experience Replay - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1511.05952"},{"title":"[2506.18482] Reliability-Adjusted Prioritized Experience Replay","url":"https://arxiv.org/abs/2506.18482"},{"title":"Reward Prediction Error Prioritisation in Experience Replay: The RPE-PER Method","url":"https://arxiv.org/html/2501.18093v1"},{"title":"Prioritized Generative Replay","url":"https://arxiv.org/html/2410.18082v2"}]

I found the paper you were looking for. Here's what arxiv 2601.02648 is about:

## Paper Summary

The paper "Prioritized Replay for RL Post-training" introduces a problem-level prioritization framework for RL post-training of large language models.

### Key Approach

Building on insights from prioritized replay in deep RL, as well as prior observations that rollouts with intermediate success rates tend to produce stronger learning signals under methods such as GRPO, the approach selects problems according to a simple, model-driven priority score derived from empirical success statistics.

### Main Difference from Traditional Curriculum Learning

In contrast to conventional curriculum strategies that emphasize easier tasks early in training, the resulting schedule naturally focuses training on problems that are neither consistently solved nor consistently failed, while deprioritizing those that contribute little gradient information.

### Technical Details

The paper studies RL post-training for large language models (LLMs), where the environment is a collection of reasoning problems or task simulators that produce complete rollouts for the agent. Because of the structural shift away from transition-level replay buffers, priority must be defined at the problem level, and the prioritization scheme is compatible with GRPO, PPO, or any other rollout-based method, since it governs the scheduling of problems rather than the form of the learning update.

The paper was submitted on January 6, 2026, and is authored by Mehdi Fatemi.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dfb576e-ffb4-4167-b35c-f22fb5e9df9d",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "2bb28fba-52f7-4049-ae2e-5ae1bfb641ee",
  "sourceToolAssistantUUID": "8dfb576e-ffb4-4167-b35c-f22fb5e9df9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T05:44:14.898Z_

<details><summary>↩ Tool result · `toolu_013pTmU8MEaowMqtoky4C8hm`</summary>

```text
Web search results for query: "online data selection during supervised fine-tuning LLM VLA training loss priority"

Links: [{"title":"Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay","url":"https://arxiv.org/html/2506.05316"},{"title":"Holdout-Loss-Based Data Selection for LLM Finetuning via In-Context Learning","url":"https://arxiv.org/html/2510.14459"},{"title":"The Ultimate Guide to Fine-Tuning LLMs from Basics to Breakthroughs: An Exhaustive Review of Technologies, Research, Best Practices, Applied Research Challenges and Opportunities (Version 1.0)","url":"https://arxiv.org/html/2408.13296v1"},{"title":"A Practical Guide to LLM Fine Tuning | Databricks Blog","url":"https://www.databricks.com/blog/llm-fine-tuning"},{"title":"Supervised Fine-tuning: customizing LLMs | by Juan Martinez | MantisNLP | Medium","url":"https://medium.com/mantisnlp/supervised-fine-tuning-customizing-llms-a2c1edbf22c3"},{"title":"The Comprehensive Guide to Fine-tuning LLM | by Sunil Rao | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/comprehensive-guide-to-fine-tuning-llm-4a8fd4d0e0af"},{"title":"Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-fine-tuning"},{"title":"Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs","url":"https://arxiv.org/html/2412.13337v1"},{"title":"Fine-Tuning Large Language Models for Specialized Use Cases - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949761224001147"},{"title":"Supervised Fine Tuning: Enhancing Your LLM Accuracy in 2025 | Label Your Data","url":"https://labelyourdata.com/articles/llm-fine-tuning/supervised-fine-tuning"}]

I found relevant research results on online data selection during supervised fine-tuning. Here are the key findings:

## Online Data Selection for LLM Training

Recent work proposes difficulty-targeted online data selection (DOTS) to improve data efficiency in LLM fine-tuning by prioritizing questions of moderate difficulty that are more likely to yield informative learning signals.

DOTS prioritizes questions of moderate difficulty relative to the current policy, accelerating convergence. This approach introduces the notion of adaptive difficulty, which measures how likely the current policy is to fail on a given question, and at each training step prioritizes questions of moderate adaptive difficulty, as these are most likely to yield meaningful learning signals.

### Loss-Based Selection Approaches

Another relevant approach focuses on loss-based metrics for data selection. An In-Context Approximation (ICA) estimates the holdout loss a model would incur after training on a candidate example and defines per-example weights that dynamically reweight gradient updates as model parameters evolve.

### Training Efficiency Results

Research shows that difficulty-targeted online data selection consistently reaches the same performance with substantially fewer training steps, achieving reductions ranging from 13.33% to 56.67%, with DOTS significantly accelerating convergence by prioritizing informative training samples.

These approaches address the challenge of efficiently selecting which data examples should be prioritized during supervised fine-tuning, with a focus on loss-based metrics and adaptive difficulty as key selection criteria.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfa0e941-920f-43b2-8112-ce932a9876be",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "8d83284c-6c15-4496-ba29-d50f93952fe2",
  "sourceToolAssistantUUID": "bfa0e941-920f-43b2-8112-ce932a9876be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T05:44:14.944Z_

<details><summary>↩ Tool result · `toolu_01TQ7u7SNi2TJqc7NK4cRbXb`</summary>

```text
Web search results for query: "DDPGfD "deep Q-learning from demonstrations" prioritized experience replay imitation"

Links: [{"title":"GitHub - felix-kerkhoff/DQfD: An implementation of Deep Q-Learning from Demonstrations (DQfD) for playing Atari 2600 video games · GitHub","url":"https://github.com/felix-kerkhoff/DQfD"},{"title":"Self-Imitation Learning from Demonstrations George Pshikhachev","url":"https://openreview.net/pdf?id=fYcViVwEH3U"},{"title":"Improved Deep Reinforcement Learning with Expert Demonstrations","url":"https://arxiv.org/pdf/2102.09243"},{"title":"[1704.03732] Deep Q-learning from Demonstrations","url":"https://ar5iv.labs.arxiv.org/html/1704.03732"},{"title":"GitHub - cychai1995/DDPGfD: DDPGfD: This is our implementation project for the Reinforcement Learning course in NCTU. · GitHub","url":"https://github.com/cychai1995/DDPGfD"},{"title":"Sheelabhadra Dey | Deep Q-learning from Demonstrations","url":"https://sheelabhadra.github.io/blog/2019/DQfD/"},{"title":"Combining Imitation Learning and Reinforcement Learning Using DQfD","url":"https://danieltakeshi.github.io/2019/04/30/il-and-rl/"},{"title":"GitHub - kairproject/kair_algorithms_draft: Reinforcement learning algorithms for robot control tasks","url":"https://github.com/kairproject/kair_algorithms_draft"},{"title":"Deep Q-Learning from Demonstrations (DQfD) Bryan Chan & Chandripal Budnarain","url":"http://www.cs.toronto.edu/~florian/courses/imitation_learning/lectures/Lecture4.pdf"},{"title":"DEEP Q LEARNING FROM DYNAMIC DEMONSTRATION ...","url":"https://openreview.net/pdf?id=hLElJeJKxzY"}]

Based on the search results, here's what I found about these reinforcement learning concepts:

## Deep Q-Learning from Demonstrations (DQfD)

DQfD is a deep reinforcement learning algorithm which leverages even very small amounts of demonstration data to massively accelerate learning. It combines reinforcement learning and imitation learning techniques.

## DDPGfD

DDPGfD is an imitation learning algorithm that infuses demonstration data into experience replay. The DDPGfD algorithm is similar to DQfD and both assist in enhancing the original algorithms through a hybrid loss function with the "expert loss". The difference between the two is that DDPGfD is based on the DDPG algorithm, which is designed to solve continuous action space problems.

## Prioritized Experience Replay in These Algorithms

Prioritized experience replay modifies the DQN agent to sample more important transitions from its replay buffer more frequently. Both DQfD and DDPGfD specifically give a priority bonus to demonstrations.

A prioritized replay mechanism is used to balance the amount of demonstration data in each mini-batch. Demonstration data is never overwritten in the replay buffer, and sampling is done using a prioritized experience replay buffer which also decides the ratio between demonstration and self-generated data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "327bb475-9785-418b-a074-ffb627131510",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "799d13df-bc2f-478a-ab80-76af8a875009",
  "sourceToolAssistantUUID": "327bb475-9785-418b-a074-ffb627131510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T05:44:16.046Z_

<details><summary>↩ Tool result · `toolu_01JmXbNmvbCMgyzn17jdrVSo`</summary>

```text
Web search results for query: "arxiv 2604.16918 FreshPER LLM VLM reinforcement learning details"

Links: [{"title":"Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/html/2604.16918"},{"title":"[2604.16918] Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning","url":"https://arxiv.org/abs/2604.16918"},{"title":"The Evolving Landscape of LLM- and VLM-Integrated Reinforcement Learning","url":"https://arxiv.org/html/2502.15214v1"},{"title":"Generalizable Dense Reward for Long-Horizon Robotic Tasks","url":"https://arxiv.org/html/2604.00055"},{"title":"[2502.15214] The Evolving Landscape of LLM- and VLM-Integrated Reinforcement Learning","url":"https://arxiv.org/abs/2502.15214"},{"title":"WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering","url":"https://arxiv.org/html/2604.05818"},{"title":"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey | OpenReview","url":"https://openreview.net/forum?id=RY19y2RI1O"},{"title":"Goal-Guided Efficient Exploration via Large Language Model in Reinforcement Learning","url":"https://arxiv.org/html/2509.22008v1"},{"title":"DriveVLM-RL: Neuroscience-Inspired Reinforcement Learning with Vision-Language Models for Safe and Deployable Autonomous Driving","url":"https://arxiv.org/html/2603.18315"},{"title":"ASPECT:Analogical Semantic Policy Execution via Language Conditioned Transfer","url":"https://arxiv.org/html/2604.08355"}]

Based on the search results, here are the key details about arxiv paper 2604.16918 on FreshPER:

## Overview

FreshPER is authored by Weiyu Ma, Yongcheng Zeng, Yan Song, Xinyu Cui, Jian Zhao, Xuhui Liu, and Mohamed Elhoseiny from institutions including KAUST, CASIA, and University College London, submitted on April 18, 2026.

## The Problem

While Reinforcement Learning has achieved impressive success in post-training LLMs and VLMs with on-policy algorithms such as PPO, GRPO, and REINFORCE++, these methods discard all collected trajectories after a single gradient update, resulting in poor sample efficiency, particularly wasteful for agentic tasks where multi-turn environment interactions are expensive.

Although Experience Replay drives sample efficiency in classic RL by allowing agents to reuse past trajectories and prioritize informative ones, directly applying Prioritized Experience Replay (PER) to LLMs fails because the rapid policy evolution of billion-parameter models renders stored priorities stale, causing old high-priority trajectories to dominate sampling long after they have become uninformative.

## The Solution

FreshPER addresses priority staleness by augmenting any PER base priority with a multiplicative exponential age decay, directly motivated by the exponential decay of effective sample size (ESS) as the policy diverges from the behavior policy, ensuring that even the highest-priority old trajectory is eventually deprioritized below a fresh trajectory of moderate priority, while preserving the informativeness-driven sampling of standard PER.

## Evaluation

FreshPER is evaluated across eight environments spanning text-only LLM and multimodal VLM settings, with all experiments using REINFORCE++ as the policy gradient algorithm and implemented on the ROLL framework. FreshPER significantly outperforms on-policy baselines, achieving +46% on NQ Search, +367% on Sokoban, and +133% on VLM FrozenLake, while standard PER without age decay consistently degrades performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "284e74ba-a67a-4696-9cd3-405de9ea217b",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "f0f9503c-fb18-4867-b9f7-8085e5a1e7e7",
  "sourceToolAssistantUUID": "284e74ba-a67a-4696-9cd3-405de9ea217b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T05:44:19.381Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HKPWrzD7dwpURUocuEeMai`</summary>

```json
{
  "query": "ExpReS-VLA arxiv 2511.06202 experience replay retrieval VLA fine-tuning details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f9503c-fb18-4867-b9f7-8085e5a1e7e7",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz35fni6Rvd9DcbV4Xpk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71179d96-9177-471a-8bae-efffb6404e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nKZDStuGuUTDpH7oSRxxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2559,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 18945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 35 · 2026-05-13T05:44:20.292Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QcBhwBPPB4BZG69bUoj1bD`</summary>

```json
{
  "query": "Demo-SCORE arxiv 2503.03707 self-curating demonstrations details RSS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71179d96-9177-471a-8bae-efffb6404e2c",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz35fni6Rvd9DcbV4Xpk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3709c2f-e01b-45da-a6d8-911f55062da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nKZDStuGuUTDpH7oSRxxd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2559,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 18945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 36 · 2026-05-13T05:44:20.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015tLbG1tYfXwaaXBwyZVb1W`</summary>

```json
{
  "query": "RIZE adaptive regularization imitation learning arxiv 2502.20089"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3709c2f-e01b-45da-a6d8-911f55062da0",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz35fni6Rvd9DcbV4Xpk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ecf45033-f975-4cf0-acd7-049db2dfcd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nKZDStuGuUTDpH7oSRxxd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2559,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 18945,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2559,
          "output_tokens": 185,
          "cache_read_input_tokens": 18945,
          "cache_creation_input_tokens": 1270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1270,
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

_source line 37 · 2026-05-13T05:44:27.338Z_

<details><summary>↩ Tool result · `toolu_015tLbG1tYfXwaaXBwyZVb1W`</summary>

```text
Web search results for query: "RIZE adaptive regularization imitation learning arxiv 2502.20089"

Links: [{"title":"[2502.20089] RIZE: Adaptive Regularization for Imitation Learning","url":"https://arxiv.org/abs/2502.20089"},{"title":"RIZE: Adaptive Regularization for Imitation Learning","url":"https://arxiv.org/html/2502.20089"},{"title":"RIZE: Regularized Imitation Learning via Distributional Reinforcement Learning","url":"https://arxiv.org/html/2502.20089v1"},{"title":"(PDF) RIZE: Regularized Imitation Learning via Distributional Reinforcement Learning","url":"https://www.researchgate.net/publication/389398702_RIZE_Regularized_Imitation_Learning_via_Distributional_Reinforcement_Learning"},{"title":"Machine Learning Feb 2025","url":"https://www.arxiv.org/list/cs.LG/2025-02?skip=2325&show=2000"},{"title":"[Literature Review] RIZE: Regularized Imitation Learning via Distributional Reinforcement Learning","url":"https://www.themoonlight.io/en/review/rize-regularized-imitation-learning-via-distributional-reinforcement-learning"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=2325&show=250"},{"title":"Distributional Inverse Reinforcement Learning","url":"https://arxiv.org/html/2510.03013v1"},{"title":"RIZE: Adaptive Regularization for Imitation Learning | OpenReview","url":"https://openreview.net/forum?id=a6DWqXJZCZ"},{"title":"RIZE: Adaptive Regularization for Imitation Learning","url":"https://openreview.net/pdf/76a9c1ed716041debf57cd550e514e02921e0d8d.pdf"}]

Based on the search results, here's what I found about RIZE (arxiv:2502.20089):

## Overview

RIZE is a novel Inverse Reinforcement Learning (IRL) method that mitigates the rigidity of fixed reward structures and the limited flexibility of implicit reward regularization. Building on the Maximum Entropy IRL framework, the approach incorporates a squared temporal-difference (TD) regularizer with adaptive targets that evolve dynamically during training, thereby imposing adaptive bounds on recovered rewards and promoting robust decision-making.

## Key Contributions

The paper introduces two main methodological innovations:

1. **Adaptive Target Rewards**: RIZE utilizes dynamic, context-sensitive reward targets that adjust throughout the training process. This contrasts with traditional methods that use fixed reward values (e.g., +1 for expert actions and -1 for agent actions).

2. **Distributional RL Integration**: To capture richer return information, the approach integrates distributional RL into the learning process.

## Empirical Results

The method achieves expert-level performance on complex MuJoCo and Adroit environments, surpassing baseline methods on the Humanoid-v2 task with limited expert demonstrations. Notably, RIZE is the only method that solves Humanoid-v2 (all baselines fail).

The paper was submitted on February 27, 2025, with subsequent revisions through November 2025, and the source code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecf45033-f975-4cf0-acd7-049db2dfcd29",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "6504c1f1-bf8e-41bc-ba43-afabd5bcea1e",
  "sourceToolAssistantUUID": "ecf45033-f975-4cf0-acd7-049db2dfcd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T05:44:31.073Z_

<details><summary>↩ Tool result · `toolu_01HKPWrzD7dwpURUocuEeMai`</summary>

```text
Web search results for query: "ExpReS-VLA arxiv 2511.06202 experience replay retrieval VLA fine-tuning details"

Links: [{"title":"[2511.06202] ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/abs/2511.06202"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://arxiv.org/html/2511.06202"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through","url":"https://arxiv.org/pdf/2511.06202"},{"title":"ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.06202v1"},{"title":"(PDF) ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval","url":"https://www.researchgate.net/publication/397480729_ExpReS-VLA_Specializing_Vision-Language-Action_Models_Through_Experience_Replay_and_Retrieval"},{"title":"𝜋^∗_0.6: a VLA That Learns From Experience","url":"https://arxiv.org/html/2511.14759"},{"title":"[2511.14759] $π^{*}_{0.6}$: a VLA That Learns From Experience","url":"https://arxiv.org/abs/2511.14759"},{"title":"Hindsight Experience Replay","url":"https://arxiv.org/pdf/1707.01495"},{"title":"[1511.05952] Prioritized Experience Replay","url":"https://arxiv.org/abs/1511.05952"},{"title":"[1712.01275] A Deeper Look at Experience Replay","url":"https://arxiv.org/abs/1712.01275"}]

I found comprehensive information about ExpReS-VLA (arxiv 2511.06202). Here are the key details about the paper:

## Overview

ExpReS-VLA is a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation.

## Technical Details

**Memory Efficiency:**
The approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs.

**Retrieval and Experience Replay:**
During deployment, ExpReS-VLA retrieves the k most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories.

**Dual-Buffer System:**
The system maintains separate circular buffers for successful and failed trajectories to enable targeted retrieval during adaptation. This separation prevents failed experiences from diluting the behavioral cloning signal while preserving them for contrastive learning.

**Novel Loss Function:**
To leverage failed attempts, the method introduces Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations collected during deployment.

## Fine-tuning Details

The hyperparameter configuration includes a learning rate of η = 2 × 10^-5 with cosine decay and batch size of 1 with gradient accumulation over 8 steps.

## Results

Experiments on the LIBERO simulation benchmark show that ExpReS-VLA improves success rates from 82.6% to 93.1% on spatial reasoning tasks and from 61% to 72.3% on long-horizon tasks compared to base OpenVLA.

Physical robot experiments across five manipulation tasks demonstrate that the approach achieves 98% success on both in-distribution and out-of-distribution tasks (with unseen backgrounds and objects), improving from 84.7% and 32% respectively for naive fine-tuning, accomplishing this adaptation in 31 seconds using only 12 demonstrations on a single RTX 5090.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71179d96-9177-471a-8bae-efffb6404e2c",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "93cddcc8-9fc7-4d55-820a-aa0f4f7eb7e9",
  "sourceToolAssistantUUID": "71179d96-9177-471a-8bae-efffb6404e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T05:44:33.863Z_

<details><summary>↩ Tool result · `toolu_01QcBhwBPPB4BZG69bUoj1bD`</summary>

```text
Web search results for query: "Demo-SCORE arxiv 2503.03707 self-curating demonstrations details RSS 2025"

Links: [{"title":"[2503.03707] Curating Demonstrations using Online Experience","url":"https://arxiv.org/abs/2503.03707"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"[PDF] Curating Demonstrations using Online Experience | Semantic Scholar","url":"https://www.semanticscholar.org/paper/776c9466ece2a34832d4ebef206fa5c2e9855b39"},{"title":"Curating Demonstrations using Online Experience | alphaXiv","url":"https://www.alphaxiv.org/en/overview/2503.03707"},{"title":"[Literature Review] Curating Demonstrations using Online Experience","url":"https://www.themoonlight.io/en/review/curating-demonstrations-using-online-experience"},{"title":"Curating Demonstrations Using Online Experience | PDF","url":"https://www.scribd.com/document/860797966/2503-03707v1"},{"title":"Curating Demonstrations using Online Experience","url":"https://www.researchgate.net/publication/395366581_Curating_Demonstrations_using_Online_Experience"},{"title":"Illustration of Demo-SCORE. Our method self-curates demonstrations... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/llustration-of-Demo-SCORE-Our-method-self-curates-demonstrations-through-online-robot_fig2_389617044"},{"title":"Curating Demonstrations using Online Experience - haebom","url":"https://slashpage.com/haebom/daily_arxiv?tl=en&post=91kwev26vd4xx2y46jpg"},{"title":"Curating Demonstrations using Online Experience","url":"https://chatpaper.com/paper/117669"}]

I found detailed information about Demo-SCORE arxiv 2503.03707. Here are the key details:

## Overview
Demo-SCORE proposes for robots to self-curate based on online robot experience. The method is aimed at improving robotic learning from heterogeneous demonstration datasets.

## Problem Addressed
Many robot demonstration datasets contain heterogeneous demonstrations of varying quality, and this heterogeneity may benefit policy pre-training, but can hinder robot performance when used with a final imitation learning objective.

## Methodology Details
The approach trains and cross-validates a classifier to discern successful policy roll-outs from unsuccessful ones and uses the classifier to filter heterogeneous demonstration datasets.

More specifically, the method self-curates demonstrations through online robot experience in four steps: (i) train a policy on the full demonstration set; (ii) evaluate the policy by generating rollouts with different checkpoints; (iii) use these rollouts to train and cross-validate a classifier that distinguishes between success and failure trajectories; (iv) filter out unreliable demonstrations based on the learned classifier, retaining only ones that do not reflect policy failures for subsequent policy training.

## Authors and Publication
The paper was authored by Annie S. Chen, Alec M. Lessing, Yuejiang Liu, and Chelsea Finn, published in Robotics on March 5, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3709c2f-e01b-45da-a6d8-911f55062da0",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "4c0600d8-8652-4275-9568-53901853c5cf",
  "sourceToolAssistantUUID": "f3709c2f-e01b-45da-a6d8-911f55062da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-13T05:44:36.843Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TBUWbfwmC94dBQhWnXw87S`</summary>

```json
{
  "query": "DOTS difficulty-targeted online data selection LLM reinforcement fine-tuning arxiv 2506.05316"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c0600d8-8652-4275-9568-53901853c5cf",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz36z2qsjWqf3EsxNx5C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bebdbb7-2511-4e9a-8cea-7576c3fec1ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169mqxHTTpvuTauQBLCMv82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 883,
      "cache_creation_input_tokens": 4598,
      "cache_read_input_tokens": 20215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4598,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 41 · 2026-05-13T05:44:37.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ybVqeNGJiBd5AhLqzyrH4`</summary>

```json
{
  "query": "\"active robot curriculum learning\" online human demonstrations arxiv 2503.02277"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bebdbb7-2511-4e9a-8cea-7576c3fec1ae",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz36z2qsjWqf3EsxNx5C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2bf4ca7-0cd8-4b2e-9425-4b1c78c435e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169mqxHTTpvuTauQBLCMv82",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 883,
      "cache_creation_input_tokens": 4598,
      "cache_read_input_tokens": 20215,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4598
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 883,
          "output_tokens": 127,
          "cache_read_input_tokens": 20215,
          "cache_creation_input_tokens": 4598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4598,
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

_source line 42 · 2026-05-13T05:44:43.326Z_

<details><summary>↩ Tool result · `toolu_01TBUWbfwmC94dBQhWnXw87S`</summary>

```text
Web search results for query: "DOTS difficulty-targeted online data selection LLM reinforcement fine-tuning arxiv 2506.05316"

Links: [{"title":"[2506.05316] Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay","url":"https://arxiv.org/abs/2506.05316"},{"title":"Improving Data Efficiency for LLM Reinforcement Fine- ...","url":"https://arxiv.org/pdf/2506.05316"},{"title":"Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay","url":"https://arxiv.org/html/2506.05316"},{"title":"Improving Data Efficiency for LLM Reinforcement Fine-tuning ...","url":"https://www.arxiv.org/pdf/2506.05316v1"},{"title":"[Literature Review] Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay","url":"https://www.themoonlight.io/en/review/improving-data-efficiency-for-llm-reinforcement-fine-tuning-through-difficulty-targeted-online-data-selection-and-rollout-replay"},{"title":"GitHub - ASTRAL-Group/data-efficient-llm-rl","url":"https://github.com/ASTRAL-Group/data-efficient-llm-rl/"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=1500&show=2000"},{"title":"Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay | OpenReview","url":"https://openreview.net/forum?id=uwUkETPIJN"},{"title":"Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs","url":"https://arxiv.org/html/2405.02774v1"},{"title":"Learning What Reinforcement Learning Can’t: Interleaved Online Fine-Tuning for hardest Questions","url":"https://arxiv.org/html/2506.07527"}]

Based on the web search results, here's what I found about the arxiv paper 2506.05316:

## Paper Overview

This is a paper titled "Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay" by Yifan Sun and colleagues.

## Main Contributions

The paper proposes two techniques to improve data efficiency in LLM RL fine-tuning: difficulty-targeted online data selection and rollout replay.

**Difficulty-Targeted Online Data Selection (DOTS):**
The method introduces the notion of adaptive difficulty to guide online data selection, prioritizing questions of moderate difficulty that are more likely to yield informative learning signals. To estimate adaptive difficulty efficiently, they develop an attention-based framework that requires rollouts for only a small reference set of questions, and the adaptive difficulty of the remaining questions is then estimated based on their similarity to this set.

**Rollout Replay (RR):**
They introduce a rollout replay mechanism inspired by experience replay in traditional RL that reuses recent rollouts, lowering per-step computation while maintaining stable updates.

## Results

Experiments across 6 LLM-dataset combinations show that the method reduces RL fine-tuning time by 23% to 62% while reaching the same level of performance as the original GRPO algorithm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bebdbb7-2511-4e9a-8cea-7576c3fec1ae",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "b1095c72-d23b-45b6-9da5-f360a08c0f18",
  "sourceToolAssistantUUID": "3bebdbb7-2511-4e9a-8cea-7576c3fec1ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-13T05:44:43.573Z_

<details><summary>↩ Tool result · `toolu_018ybVqeNGJiBd5AhLqzyrH4`</summary>

```text
Web search results for query: ""active robot curriculum learning" online human demonstrations arxiv 2503.02277"

Links: [{"title":"[2503.02277] Active Robot Curriculum Learning from Online Human Demonstrations","url":"https://arxiv.org/abs/2503.02277"},{"title":"Active Robot Curriculum Learning from Online Human Demonstrations Muhan Hou","url":"https://arxiv.org/pdf/2503.02277"},{"title":"Active Robot Curriculum Learning from Online Human Demonstrations","url":"https://arxiv.org/html/2503.02277"},{"title":"Robotics Mar 2025","url":"https://www.arxiv.org/list/cs.RO/2025-03?skip=100&show=2000"},{"title":"Computer Science Mar 2025","url":"https://arxiv.org/list/cs/2025-03?skip=1200&show=500"},{"title":"RoboCopilot: Human-in-the-loop Interactive Imitation Learning for Robot Manipulation","url":"https://arxiv.org/html/2503.07771"},{"title":"Active Robot Curriculum Learning from Online Human Demonstrations | Request PDF","url":"https://www.researchgate.net/publication/391695591_Active_Robot_Curriculum_Learning_from_Online_Human_Demonstrations"},{"title":"GitHub - ARISE-Initiative/robomimic: robomimic: A Modular Framework for Robot Learning from Demonstration · GitHub","url":"https://github.com/ARISE-Initiative/robomimic"},{"title":"Active Robot Curriculum Learning from Online Human Demonstrations | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10974044/"},{"title":"Active Robot Curriculum Learning from Online Human Demonstrations | Proceedings of the 2025 ACM/IEEE International Conference on Human-Robot Interaction","url":"https://dl.acm.org/doi/10.5555/3721488.3721587"}]

I found the paper arxiv:2503.02277. Here's what the research is about:

## Active Robot Curriculum Learning from Online Human Demonstrations

Learning from Demonstrations (LfD) allows robots to learn skills from human users, but its effectiveness can suffer due to sub-optimal teaching, especially from untrained demonstrators. Active LfD aims to improve this by letting robots actively request demonstrations to enhance learning.

However, this may lead to frequent context switches between various task situations, increasing the human cognitive load and introducing errors to demonstrations.

The researchers propose an active LfD method that optimizes the query sequence of online human demonstrations via Curriculum Learning (CL), where demonstrators are guided to provide demonstrations in situations of gradually increasing difficulty.

The paper was authored by **Muhan Hou, Koen Hindriks, A.E. Eiben, and Kim Baraka**, and was submitted on March 4, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2bf4ca7-0cd8-4b2e-9425-4b1c78c435e0",
  "isSidechain": true,
  "promptId": "b8fc6797-5cd3-4b21-a330-51e9b079fc48",
  "agentId": "a5721a44efe1d1515",
  "type": "user",
  "uuid": "a5c5d2e4-df34-43db-8a74-7fcaa94a0b73",
  "sourceToolAssistantUUID": "c2bf4ca7-0cd8-4b2e-9425-4b1c78c435e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-13T05:45:56.196Z_

Here is a comprehensive report of all findings across the nine searches.

---

## 1. Has anyone applied PER or TD-error-based prioritization to imitation learning (not RL)?

**Short answer: Not directly in the pure imitation learning (behavioral cloning) setting.** PER and TD-error prioritization remain firmly rooted in RL. However, there are important adjacent works:

**Hybrid RL+IL methods that use PER with demonstrations:**
- **DQfD (Deep Q-Learning from Demonstrations)** and **DDPGfD** both place expert demonstrations into a prioritized replay buffer alongside self-generated transitions. Demonstrations receive a priority bonus so they are replayed more frequently. However, the learning signal is still RL (TD error), not pure imitation. The demonstrations are never overwritten and the prioritized replay buffer governs the ratio of demo vs. self-generated data. [DQfD paper](https://ar5iv.labs.arxiv.org/html/1704.03732)

- **ExpReS-VLA** (see below) uses a prioritized experience replay buffer during VLA fine-tuning (which is supervised/behavioral cloning), making it the closest example of PER applied during SFT of a large model.

**TD-error in imitation learning contexts:**
- **RIZE (Adaptive Regularization for Imitation Learning)** (arxiv:2502.20089) uses a squared TD regularizer with adaptive targets in an inverse RL / imitation learning framework. It integrates distributional RL into IRL and achieves expert-level performance on complex MuJoCo and Adroit tasks. While this is not PER per se, it directly uses TD error as a learning signal within an imitation learning method. [RIZE](https://arxiv.org/abs/2502.20089)

- **LSIQ** minimizes chi-squared divergence between expert and mixture distributions, resulting in a squared TD error objective for imitation learning.

**Bottom line:** No one has taken vanilla PER (rank transitions by |TD error|, sample proportionally) and applied it to pure behavioral cloning / imitation learning. The concept does not straightforwardly transfer because pure IL lacks a value function and TD error. The closest works either (a) use PER in hybrid RL+IL methods (DQfD, DDPGfD), (b) use TD-error-based regularization within IRL frameworks (RIZE, LSIQ), or (c) use experience replay with priority during VLA fine-tuning (ExpReS-VLA).

---

## 2. Has anyone done adaptive/online data selection during SFT training of VLA or LLM models?

**Yes, several recent papers:**

- **DOTS: Difficulty-Targeted Online Data Selection** (arxiv:2506.05316) -- proposes adaptive difficulty-based online data selection for LLM RL fine-tuning. It prioritizes questions of moderate difficulty that yield the most informative learning signals. Reduces RL fine-tuning time by 23-62%. Note: this is for RL post-training (GRPO), not pure SFT. [DOTS](https://arxiv.org/abs/2506.05316)

- **Prioritized Replay for RL Post-training** (arxiv:2601.02648, Mehdi Fatemi, Jan 2026) -- introduces problem-level prioritization for RL post-training of LLMs. Focuses training on problems that are neither consistently solved nor consistently failed. Compatible with GRPO, PPO, etc. Again, this is RL post-training, not SFT. [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)

- **FreshPER** (see below) -- applies prioritized experience replay to LLM/VLM reinforcement learning, not SFT.

- **FIRE (Fine-Tuning with Integrated Replay & Efficiency)** -- a data-centric framework for efficient adaptation and continual improvement targeting LLMs and code generation. Combines replay, targeted data selection, regularization, and algorithmic innovations for both supervised and RL scenarios. [FIRE](https://www.emergentmind.com/topics/fine-tuning-with-integrated-replay-and-efficiency-fire)

- **Holdout-Loss-Based Data Selection for LLM Finetuning** (arxiv:2510.14459) -- uses in-context approximation to estimate holdout loss and dynamically reweight gradient updates during SFT as model parameters evolve. This is one of the clearest examples of adaptive data selection during SFT itself. [Holdout-Loss](https://arxiv.org/html/2510.14459)

- **ExpReS-VLA** (see below) -- uses prioritized experience replay and retrieval-augmented generation during VLA fine-tuning (supervised), making it the most direct example for VLA models.

- **Demo-SCORE** (see below) -- curates demonstration data based on online robot experience, filtering out low-quality demonstrations before policy retraining. This is offline curation between training rounds rather than online selection within a training loop.

**Bottom line:** Adaptive/online data selection during RL post-training of LLMs is an active and growing area (DOTS, Prioritized Replay, FreshPER). For pure SFT, it is less explored but emerging (Holdout-Loss, FIRE). For VLA models specifically, ExpReS-VLA is the standout example.

---

## 3. Verification of specific papers

### "Freshness-Aware Prioritized Experience Replay" -- EXISTS

- **Full title:** "Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning"
- **ArXiv:** [2604.16918](https://arxiv.org/abs/2604.16918)
- **Date:** April 18, 2026
- **Authors:** Weiyu Ma, Yongcheng Zeng, Yan Song, Xinyu Cui, Jian Zhao, Xuhui Liu, Mohamed Elhoseiny (KAUST, CASIA, UCL)
- **Key idea:** Standard PER fails for LLMs because rapid policy evolution renders stored priorities stale. FreshPER adds multiplicative exponential age decay to priorities, motivated by effective sample size analysis. Evaluated across 8 environments with 0.5B-7B models; achieves +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake vs. on-policy baselines.
- **Note:** This is for RL training (REINFORCE++), NOT supervised fine-tuning.

### "ExpReS-VLA" -- EXISTS

- **Full title:** "ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval"
- **ArXiv:** [2511.06202](https://arxiv.org/abs/2511.06202)
- **Date:** November 2025
- **Key idea:** Enables rapid on-device adaptation of pre-trained VLAs (OpenVLA) via compressed experience replay (97% storage reduction by storing vision embeddings instead of raw images) and retrieval-augmented generation. Uses a prioritized experience replay buffer that preserves recently successful trajectories. Introduces Thresholded Hybrid Contrastive Loss (THCL) to learn from both successful and failed demonstrations. Maintains separate circular buffers for successful/failed trajectories.
- **Results:** Improves LIBERO spatial reasoning from 82.6% to 93.1%, long-horizon from 61% to 72.3%. Physical robot: 98% success on in-distribution and OOD tasks (up from 84.7% and 32% with naive fine-tuning). Adapts in 31 seconds with 12 demos on a single RTX 5090.
- **Relevance:** This is the closest paper to "PER applied to SFT of a VLA model" -- it uses prioritized replay during supervised fine-tuning of OpenVLA.

### "Demo-SCORE" -- EXISTS

- **Full title:** "Curating Demonstrations using Online Experience" (Demo-SCORE is the method name)
- **ArXiv:** [2503.03707](https://arxiv.org/abs/2503.03707)
- **Date:** March 5, 2025
- **Authors:** Annie S. Chen, Alec M. Lessing, Yuejiang Liu, Chelsea Finn
- **Venue:** Accepted at RSS 2025 (Robotics: Science and Systems)
- **Project page:** [https://anniesch.github.io/demo-score/](https://anniesch.github.io/demo-score/)
- **Key idea:** Self-curates demonstration datasets via online robot experience. Four-step pipeline: (1) train policy on full demo set, (2) generate rollouts with different checkpoints, (3) train classifier to distinguish success/failure trajectories, (4) filter out unreliable demonstrations. No additional human labeling needed beyond success/failure detection.
- **Results:** 15-35% higher absolute success rate compared to training with all original demonstrations.

---

## Additional relevant papers found

- **Active Robot Curriculum Learning from Online Human Demonstrations** (arxiv:2503.02277, HRI 2025) -- Optimizes query sequence of online demonstrations via curriculum learning, guiding demonstrators to provide demos of gradually increasing difficulty. [Paper](https://arxiv.org/abs/2503.02277)

- **Data Scaling Laws in Imitation Learning for Robotic Manipulation** (OpenReview) -- Comprehensive empirical study on how policy generalization changes with number of training environments, objects, and demonstrations. [Paper](https://openreview.net/forum?id=pISLZG7ktL)

- **pi*_0.6: a VLA That Learns From Experience** (arxiv:2511.14759) -- Related VLA that incorporates online experience into learning. [Paper](https://arxiv.org/abs/2511.14759)

---

## Summary of key findings

| Question | Answer |
|----------|--------|
| PER/TD-error prioritization applied to pure imitation learning? | **No direct application.** Hybrid RL+IL methods (DQfD, DDPGfD) use PER with demo data but still use RL objectives. RIZE/LSIQ use TD error within IRL frameworks. |
| Adaptive/online data selection during SFT of VLA/LLM? | **Emerging area.** ExpReS-VLA uses prioritized replay during VLA SFT. For LLMs, most work targets RL post-training (DOTS, FreshPER, Prioritized Replay). Holdout-Loss and FIRE address SFT more directly. |
| "Freshness-Aware PER" exists? | **Yes.** arxiv:2604.16918, April 2026. For RL training of LLMs/VLMs. |
| "ExpReS-VLA" exists? | **Yes.** arxiv:2511.06202, November 2025. Uses PER during VLA fine-tuning. |
| "Demo-SCORE" exists? | **Yes.** arxiv:2503.03707, March 2025. RSS 2025. Curates demos via online experience. |

Sources:
- [Prioritized Experience Replay (Schaul et al.)](https://arxiv.org/abs/1511.05952)
- [Deep Q-Learning from Demonstrations (DQfD)](https://ar5iv.labs.arxiv.org/html/1704.03732)
- [Understanding PER - Daniel Takeshi](https://danieltakeshi.github.io/2019/07/14/per/)
- [Freshness-Aware PER (FreshPER)](https://arxiv.org/abs/2604.16918)
- [ExpReS-VLA](https://arxiv.org/abs/2511.06202)
- [Demo-SCORE](https://arxiv.org/abs/2503.03707)
- [Demo-SCORE Project Page](https://anniesch.github.io/demo-score/)
- [RIZE: Adaptive Regularization for Imitation Learning](https://arxiv.org/abs/2502.20089)
- [Prioritized Replay for RL Post-training](https://arxiv.org/abs/2601.02648)
- [DOTS: Difficulty-Targeted Online Data Selection](https://arxiv.org/abs/2506.05316)
- [Holdout-Loss-Based Data Selection for LLM Finetuning](https://arxiv.org/html/2510.14459)
- [FIRE: Fine-Tuning with Integrated Replay & Efficiency](https://www.emergentmind.com/topics/fine-tuning-with-integrated-replay-and-efficiency-fire)
- [Active Robot Curriculum Learning](https://arxiv.org/abs/2503.02277)
- [Data Scaling Laws in Imitation Learning](https://openreview.net/forum?id=pISLZG7ktL)
- [pi*_0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)
- [Dynamic Experience Replay](http://proceedings.mlr.press/v100/luo20a/luo20a.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c5d2e4-df34-43db-8a74-7fcaa94a0b73",
  "isSidechain": true,
  "agentId": "a5721a44efe1d1515",
  "requestId": "req_011Caz37hVxHVvCGdAQdWKPF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "182e2931-fe79-4762-a484-53994f93db77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d6a789c0-9c74-4575-85a9-802d261f7af3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116HhSKk5PKqapceBRQvQDo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2646,
      "cache_read_input_tokens": 24813,
      "output_tokens": 3206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2646
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3206,
          "cache_read_input_tokens": 24813,
          "cache_creation_input_tokens": 2646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2646,
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
