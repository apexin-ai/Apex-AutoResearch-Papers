# Research conversation: I need to verify the current SOTA (as of May 2026) on three benchmarks used in agent RL research: 1. **ALFWorld**: Curre

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 87
- **Recorded user turns:** 1
- **Tool calls:** 38
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a82ed4aeafe0578d0.jsonl`
- **Structured JSON:** [`fc1dbb58e0c34b12b773.json`](../../sessions/fc/fc1dbb58e0c34b12b773.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

87 recorded events

### User

_source line 1 · 2026-05-10T19:25:01.688Z_

I need to verify the current SOTA (as of May 2026) on three benchmarks used in agent RL research:

1. **ALFWorld**: Current claimed SOTA is Embodied Planner-R1 at 97.78% and HiPER at 97.4%. Is this still current? Any newer methods?
2. **WebShop**: Current claimed SOTA is HiPER at 83.3% (Qwen2.5-7B). Any newer methods surpassing this?
3. **Mind2Web**: What are the current best results? Specifically for RL-trained LLM agents at the 7B scale.

Use WebSearch with queries like:
- "ALFWorld SOTA 2026 reinforcement learning agent"
- "WebShop SOTA 2026 LLM agent"
- "Mind2Web SOTA 2026 LLM agent reinforcement learning"
- "Papers with Code ALFWorld"
- "Papers with Code WebShop"
- "Mind2Web benchmark results 2026"

Also search for:
- "verl-agent Mind2Web" to see if the GiGPO codebase supports Mind2Web
- "GRPO Mind2Web" to see if anyone has applied GRPO to Mind2Web

I need concrete numbers to assess headroom on each benchmark. Report findings concisely with method names, scores, and model sizes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "0452f4a2-170a-4d34-a52c-2aaac7a58ee3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:25:01.691Z_

```json
{
  "parentUuid": "0452f4a2-170a-4d34-a52c-2aaac7a58ee3",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
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
  "uuid": "df16666c-4605-4635-9f99-8a9e4e406c11",
  "timestamp": "2026-05-10T19:25:01.691Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:25:04.352Z_



I'll search across all these queries in parallel to gather the information efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df16666c-4605-4635-9f99-8a9e4e406c11",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSF2ihqNwrg6h4eMnce",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67211d0a-8c99-446d-9178-3ef490880dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UczfxB2owgKVoUEMQNDXFY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 875,
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

### Tool call

_source line 4 · 2026-05-10T19:25:04.711Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DEHuSfKCm7dxKahLJm5VhN`</summary>

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
  "parentUuid": "67211d0a-8c99-446d-9178-3ef490880dd1",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSF2ihqNwrg6h4eMnce",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0aeb2ea-7b3d-4c32-8111-23b4eb9ba34e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UczfxB2owgKVoUEMQNDXFY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 8223,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 875,
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

_source line 5 · 2026-05-10T19:25:04.714Z_

<details><summary>↩ Tool result · `toolu_01DEHuSfKCm7dxKahLJm5VhN`</summary>

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
  "parentUuid": "b0aeb2ea-7b3d-4c32-8111-23b4eb9ba34e",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "88de03bb-bcb9-4db8-81ed-cc3c3133bf91",
  "sourceToolAssistantUUID": "b0aeb2ea-7b3d-4c32-8111-23b4eb9ba34e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:25:07.782Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88de03bb-bcb9-4db8-81ed-cc3c3133bf91",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSFFqVKmkZpVoHJ2hmM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "933d2400-cdb1-4552-a71c-2b3da11d4339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBMvui7e8HRQxLNLWdzgvi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 7 · 2026-05-10T19:25:08.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hsibs6EAspvtp7NwDUpDG6`</summary>

```json
{
  "query": "ALFWorld SOTA 2026 reinforcement learning agent benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "933d2400-cdb1-4552-a71c-2b3da11d4339",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSFFqVKmkZpVoHJ2hmM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d78665a-64fd-4586-98ea-52f4687310d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBMvui7e8HRQxLNLWdzgvi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 9098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1409,
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

_source line 8 · 2026-05-10T19:25:15.125Z_

<details><summary>↩ Tool result · `toolu_01Hsibs6EAspvtp7NwDUpDG6`</summary>

```text
Web search results for query: "ALFWorld SOTA 2026 reinforcement learning agent benchmark results"

Links: [{"title":"Recent Advances in Reinforcement Learning for Continuous Control | SOTA Early 2026","url":"https://araffin.github.io/slides/advances-rl-sota-2026/"},{"title":"Learning to Simulate from Experience for Better AI Agents","url":"https://arxiv.org/pdf/2510.09577"},{"title":"A Review for Deep Reinforcement Learning in Atari:","url":"https://arxiv.org/pdf/2112.04145"},{"title":"A Survey on Evaluation of LLM-based Agents","url":"https://arxiv.org/html/2503.16416v2"},{"title":"ALFWorld: Textual and Embodied Agent Benchmark","url":"https://www.emergentmind.com/topics/alfworld"},{"title":"Agentic Critical Training","url":"https://arxiv.org/html/2603.08706v1"},{"title":"AI Benchmarking 2026 - Measure Models, Agents, and Your Own Evals | benchmarkingagents.com","url":"https://benchmarkingagents.com/"},{"title":"[2311.16714] Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld","url":"https://arxiv.org/abs/2311.16714"},{"title":"Code Generation Benchmarks 2026: SOTA LLMs for Programming | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"GitHub - stevenyangyj/Emma-Alfworld: Official code for the paper: Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld · GitHub","url":"https://github.com/stevenyangyj/Emma-Alfworld"}]

Based on the web search results, I found several relevant papers and benchmarking resources related to ALFWorld and recent reinforcement learning agent results in 2026:

## Key Findings:

**Recent ALFWorld Benchmark Papers (2026):**

Recent experiments on ALFWorld and other synthetic benchmarks show the effectiveness of frameworks combining reasoning traces with reinforcement learning methods. Research shows that DeepSeek-R1 struggled in ALFWorld as it struggles to model the environment layout, while methods like DISTILL(RESIM) and DYNA-GRPO improved the simulation ability alongside task performance compared to baselines.

**Agentic Critical Training Results:**

On the out-of-distribution split of ALFWorld, adding Agentic Critical Training (ACT) improves both imitation learning and reinforcement learning, with RL + ACT achieving the best out-of-distribution performance overall. The ACT training method shows larger gains on out-of-distribution tasks (3.73 percentage points) than on in-distribution tasks (2.15 percentage points), indicating that the reasoning acquired generalizes to unseen task configurations.

**General Agent Benchmarking Trends:**

Research indicates that even state-of-the-art models struggle with long-horizon planning, which remains a challenge on ALFWorld and similar benchmarks in 2026.

The search results indicate that ALFWorld continues to be an active area of research in 2026, with new methods focusing on improving agent simulation abilities and reasoning for better task performance on both in-distribution and out-of-distribution tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d78665a-64fd-4586-98ea-52f4687310d5",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "d29bb708-f68d-4ee4-9af9-a9a519f40438",
  "sourceToolAssistantUUID": "3d78665a-64fd-4586-98ea-52f4687310d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T19:25:18.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PkTSZ7hjjXQ3dV5rCLiLpL`</summary>

```json
{
  "query": "WebShop SOTA 2026 LLM agent benchmark score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d29bb708-f68d-4ee4-9af9-a9a519f40438",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSG28Wr8ZsjwjAJRH3i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a91bfb46-85c5-48a6-b2bf-0fa7f2427519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H13NbcdrYAHYzGZVxumj22",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 10507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 909,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T19:25:18.636Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E2xeQ3zya1R5C6J64ayoRu`</summary>

```json
{
  "query": "Mind2Web SOTA 2026 LLM agent reinforcement learning results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a91bfb46-85c5-48a6-b2bf-0fa7f2427519",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSG28Wr8ZsjwjAJRH3i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84ebf803-cc40-4c2d-b44a-cd1651cc8a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H13NbcdrYAHYzGZVxumj22",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 10507,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 10507,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 909,
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

_source line 11 · 2026-05-10T19:25:18.669Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UU8cSgkZiu7qDnDSU7qUSC`</summary>

```json
{
  "query": "Papers with Code ALFWorld leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84ebf803-cc40-4c2d-b44a-cd1651cc8a90",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSG28Wr8ZsjwjAJRH3i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4816f135-d49f-4018-9f52-cd070689aef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H13NbcdrYAHYzGZVxumj22",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 10507,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 10507,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 909,
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

_source line 12 · 2026-05-10T19:25:23.551Z_

<details><summary>↩ Tool result · `toolu_01PkTSZ7hjjXQ3dV5rCLiLpL`</summary>

```text
Web search results for query: "WebShop SOTA 2026 LLM agent benchmark score"

Links: [{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Code Generation Benchmarks 2026: SOTA LLMs for Programming | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models","url":"https://www.google.com/goto?url=CAESYQE7q4yl6wyfXRR2JuB7E_15YCXuvBmO78fxKdWA6TH7LyPq_s72lC08-k3_7KT-LsC4CdknODWtDgRm9wBLQF0AbLlzR9lkGzIcqvWuv1h3FyiIoQ9y4kdTtd7KvvR9TBw%3D"},{"title":"10 AI agent benchmarks","url":"https://www.evidentlyai.com/blog/ai-agent-benchmarks"},{"title":"LLM Agent & Tool-Use Benchmarks — Function Calling, MCP, Structured Output Rankings (2026) | BenchLM.ai","url":"https://benchlm.ai/llm-agent-benchmarks"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"A Survey on Evaluation of LLM-based Agents","url":"https://arxiv.org/html/2503.16416v2"}]

Based on the search results, I found a reference to WebShop as an LLM agent benchmark, but the results don't contain specific SOTA (State-of-the-Art) 2026 scores for WebShop. 

WebShop is mentioned as one of eight environments evaluated in AgentBench, which assesses the ability of LLM-as-Agent to reason and make decisions in multi-turn open-ended settings, including Web Shopping among other tasks like Operating System, Database, and Knowledge Graph challenges.

However, the search results don't provide the current SOTA benchmark scores for WebShop specifically in 2026. To find the actual performance scores for WebShop, you may want to:
- Check the CodeSOTA registry directly at codesota.com
- Look at agent benchmark leaderboards on BenchLM.ai or llm-stats.com
- Search for more recent WebShop benchmark papers or benchmark tracking sites

Would you like me to search for more specific information about WebShop benchmark scores?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a91bfb46-85c5-48a6-b2bf-0fa7f2427519",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "12a64172-e7df-4869-936e-48f42ca303d9",
  "sourceToolAssistantUUID": "a91bfb46-85c5-48a6-b2bf-0fa7f2427519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:25:25.152Z_

<details><summary>↩ Tool result · `toolu_01E2xeQ3zya1R5C6J64ayoRu`</summary>

```text
Web search results for query: "Mind2Web SOTA 2026 LLM agent reinforcement learning results"

Links: [{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"A REAL-WORLD WEBAGENT WITH PLANNING, LONG ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf"},{"title":"World Models for LLM Web Navigation","url":"https://www.emergentmind.com/papers/2410.13232"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation","url":"https://arxiv.org/html/2410.13232"},{"title":"web agents with world models: learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf"},{"title":"Adapting Multimodal Web Agents with Few-Shot Learning ...","url":"https://aclanthology.org/2025.acl-long.1008.pdf"},{"title":"A Brief Overview: Agentic Reinforcement Learning In Large Language Models","url":"https://arxiv.org/html/2604.27859v2"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | OpenReview","url":"https://openreview.net/forum?id=kiYqbO3wqw"}]

Based on the search results, here's what I found about Mind2Web SOTA 2026 for LLM agents:

## Recent State-of-the-Art Results

A World-model-augmented (WMA) web agent recently achieved new SOTA performance on Mind2Web, significantly outperforming previous SOTA methods including AWM. The paper validates the approach on benchmarks like WebArena and Mind2Web, achieving new state-of-the-art results in long-horizon web navigation.

## Key Approach: World Models

Research confirms the absence of world models in current LLMs like GPT-4o and Claude-3.5-Sonnet, and presents a World-model-augmented web agent which simulates the outcomes of its actions for better decision-making, using transition-focused observation abstraction with free-form natural language descriptions highlighting important state differences.

## Reinforcement Learning in Web Agents

Recent work emphasizes reinforcement learning approaches for web agents. By shifting the optimization objective from instantaneous rewards to the cumulative return of entire trajectories, this approach enables multi-step interactions where the consequences of early actions propagate through time, equipping agents with long-horizon planning, strategic tool utilization, and persistent memory.

## Benchmark Overview

Mind2Web contains 2,350 tasks spanning 137 websites across 31 domains, providing a comprehensive benchmark for evaluating generalist web agents across diverse real-world scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84ebf803-cc40-4c2d-b44a-cd1651cc8a90",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "36c966d9-675a-4483-b4f7-7d6171812669",
  "sourceToolAssistantUUID": "84ebf803-cc40-4c2d-b44a-cd1651cc8a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:25:25.969Z_

<details><summary>↩ Tool result · `toolu_01UU8cSgkZiu7qDnDSU7qUSC`</summary>

```text
Web search results for query: "Papers with Code ALFWorld leaderboard"

Links: [{"title":"ALFRED Leaderboard","url":"https://askforalfred.com/leaderboard/leaderboard.html"},{"title":"Trending Papers - Hugging Face","url":"https://paperswithcode.com/dataset/alfworld"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | OpenReview","url":"https://openreview.net/forum?id=0IOX0YcCdTn"},{"title":"GitHub - stevenyangyj/Emma-Alfworld: Official code for the paper: Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld · GitHub","url":"https://github.com/stevenyangyj/Emma-Alfworld"},{"title":"Papers with Code is Dead — Best Alternatives 2026 by Use Case | Codesota | CodeSOTA","url":"https://www.codesota.com/papers-with-code"},{"title":"Papers with Code - ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://paperswithcode.com/paper/alfworld-aligning-text-and-embodied"},{"title":"tutorials/add_results.md at main · paperswithcode/tutorials","url":"https://github.com/paperswithcode/tutorials/blob/main/add_results.md"},{"title":"GitHub - askforalfred/alfred: ALFRED - A Benchmark for Interpreting Grounded Instructions for Everyday Tasks · GitHub","url":"https://github.com/askforalfred/alfred"},{"title":"Papers with Code - ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks","url":"https://paperswithcode.com/paper/alfred-a-benchmark-for-interpreting-grounded"},{"title":"LEGOBench: Leaderboard Generation Benchmark for Scientific Models","url":"https://arxiv.org/html/2401.06233v1"}]

Based on the search results, I can provide you with information about ALFWorld and Papers with Code:

## ALFWorld Overview

ALFWorld is a simulator that enables agents to learn abstract, text-based policies in TextWorld and then execute goals from the ALFRED benchmark in a rich visual environment. This approach fosters better agent generalization than training only in the visually grounded environment.

## Important Update About Papers with Code

It's important to note that Meta sunsetted Papers with Code on July 24-25, 2025 without prior notice, and the 9,327 benchmark leaderboards that had been tracked are no longer served from the canonical URL. The domain now redirects to Hugging Face Trending Papers; the leaderboards are gone.

## Available Alternative Resources

While the original Papers with Code leaderboards are no longer available, historical data was rescued by the community — as JSON dumps on GitHub, as the pwc-archive on Hugging Face, and as 2021-era imports into the Open Research Knowledge Graph.

For ALFWorld specifically, you can find research papers and implementations related to the benchmark, such as EMMA (Embodied Multi-Modal Agent), which demonstrates 20%-70% improvement in success rate compared to SOTA VLM-based agents on ALFWorld benchmark's diverse tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4816f135-d49f-4018-9f52-cd070689aef3",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "a9ce282f-df2b-47ff-80d3-bc2ca56a8702",
  "sourceToolAssistantUUID": "4816f135-d49f-4018-9f52-cd070689aef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T19:25:29.039Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E2qmh79sYfcpAu5wnZWyuE`</summary>

```json
{
  "query": "HiPER ALFWorld WebShop score reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9ce282f-df2b-47ff-80d3-bc2ca56a8702",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSGpWYdwXCmjDrFvtzh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "833df6fb-6c53-4f0a-aef5-697aac32701f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZVMyBcYtjg1wPyw3T2NP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 11416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T19:25:29.543Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0161L9braPbcPSSFpUB5cZoj`</summary>

```json
{
  "query": "Embodied Planner-R1 ALFWorld 97.78"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "833df6fb-6c53-4f0a-aef5-697aac32701f",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSGpWYdwXCmjDrFvtzh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8c94a85-d4e6-466c-b749-422f6a368ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZVMyBcYtjg1wPyw3T2NP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 11416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T19:25:30.535Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BDdm8HjN6ZhmjoaME6ZMue`</summary>

```json
{
  "query": "verl-agent Mind2Web GiGPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8c94a85-d4e6-466c-b749-422f6a368ffa",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSGpWYdwXCmjDrFvtzh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c34f3d41-33ec-445a-98c6-59766523292a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZVMyBcYtjg1wPyw3T2NP5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 11416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2707,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T19:25:30.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQcysGyp5bWw2FpNt1eDfy`</summary>

```json
{
  "query": "GRPO Mind2Web web agent reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c34f3d41-33ec-445a-98c6-59766523292a",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSGpWYdwXCmjDrFvtzh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f913bbd-7ce7-4ea6-9a93-8ccf744f433b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZVMyBcYtjg1wPyw3T2NP5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2707,
      "cache_read_input_tokens": 11416,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 11416,
          "cache_creation_input_tokens": 2707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2707,
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

_source line 19 · 2026-05-10T19:25:35.469Z_

<details><summary>↩ Tool result · `toolu_01E2qmh79sYfcpAu5wnZWyuE`</summary>

```text
Web search results for query: "HiPER ALFWorld WebShop score reinforcement learning 2025"

Links: [{"title":"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/html/2602.16165"},{"title":"[2602.16165] HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/abs/2602.16165"},{"title":"[2602.16165v1] HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/abs/2602.16165v1"},{"title":"SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/html/2602.08234"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v1"},{"title":"Entropy-Modulated Policy Gradients for Long-Horizon LLM ...","url":"https://arxiv.org/pdf/2509.09265"},{"title":"Agentic Critical Training","url":"https://attention-is-all-i-need.github.io/ACT/"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Meta AI Introduces DreamGym: A Textual Experience Synthesizer For Reinforcement learning RL Agents - MarkTechPost","url":"https://www.marktechpost.com/2025/11/17/meta-ai-introduces-dreamgym-a-textual-experience-synthesizer-for-reinforcement-learning-rl-agents/"},{"title":"Language Agent Meets Offline Reinforcement Learning Critic","url":"https://aclanthology.org/2024.emnlp-main.268.pdf"}]

Based on the search results, here's what I found about HiPER, ALFWorld, and WebShop scores in reinforcement learning:

## HiPER Performance Results

HiPER achieves state-of-the-art performance on challenging interactive benchmarks, reaching 97.4% success on ALFWorld and 83.3% on WebShop with Qwen2.5-7B-Instruct (+6.6% and +8.3% over the best prior method).

## What is HiPER?

HiPER is a novel Hierarchical Plan-Execute RL framework that explicitly separates high-level planning from low-level execution, factorizing the policy into a high-level planner that proposes subgoals and a low-level executor that carries them out over multiple action steps.

## Key Results

These results highlight the importance of explicit hierarchical decomposition for scalable RL training of multi-turn LLM agents. The method consistently outperforms all evaluated baseline methods, including the best known prior method GiGPO, across both benchmarks and model sizes.

The research was published on arXiv in February 2026, demonstrating significant advances in reinforcement learning training for large language model agents on long-horizon interactive tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "833df6fb-6c53-4f0a-aef5-697aac32701f",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "7185effa-0f32-47b1-9bd0-e601cb77c417",
  "sourceToolAssistantUUID": "833df6fb-6c53-4f0a-aef5-697aac32701f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T19:25:35.849Z_

<details><summary>↩ Tool result · `toolu_0161L9braPbcPSSFpUB5cZoj`</summary>

```text
Web search results for query: "Embodied Planner-R1 ALFWorld 97.78"

Links: [{"title":"Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2506.23127"},{"title":"Unleashing Embodied Task Planning Ability in LLMs via ...","url":"https://arxiv.org/pdf/2506.23127"},{"title":"GitHub - OpenMOSS/Embodied-Planner-R1: Embodied-Planner-R1: Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning · GitHub","url":"https://github.com/OpenMOSS/Embodied-Planner-R1"},{"title":"[2506.23127] Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2506.23127"},{"title":"ALFWORLD: ALIGNING TEXT AND EMBODIED ...","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"[Literature Review] Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://www.themoonlight.io/en/review/unleashing-embodied-task-planning-ability-in-llms-via-reinforcement-learning"},{"title":"ALFWorld Suite: Dual-View AI Simulator","url":"https://www.emergentmind.com/topics/alfworld-suite"},{"title":"ALFWorld: Textual and Embodied Agent Benchmark","url":"https://www.emergentmind.com/topics/alfworld"},{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"Constrained Natural Language Action Planning for Resilient Embodied Systems","url":"https://arxiv.org/html/2510.06357v1"}]

Based on the search results, here's what I found about Embodied Planner-R1 and its ALFWorld performance:

Embodied Planner-R1 achieves impressive completion rates of 97.78% on ALFWorld and 79.92% on ScienceWorld, surpassing prior methods by a large margin.

Embodied Planner-R1 is a novel outcome-driven reinforcement learning framework that enables LLMs to develop interactive capabilities through autonomous exploration with minimal supervision. The framework incorporates three key innovations: (1) pure reinforcement learning with group rollout, incorporating in-environment interaction through parallel exploration; (2) completion-driven sparse reward; and (3) Interactive Policy Optimization (IPO) for efficient learning from grouped trajectories.

On the ALFWorld benchmark, Embodied Planner-R1 achieved accuracy rates of 99.29% and 96.27% in seen and unseen scenarios, respectively, surpassing the previous best method ETO by 15.00% and 16.42%. Additionally, the model exhibits robust generalization, with only a -3.33% generation gap in unseen environments—substantially lower than comparable methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8c94a85-d4e6-466c-b749-422f6a368ffa",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "73801986-07b7-486f-86a4-6bdb721407a6",
  "sourceToolAssistantUUID": "c8c94a85-d4e6-466c-b749-422f6a368ffa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T19:25:37.570Z_

<details><summary>↩ Tool result · `toolu_01RQcysGyp5bWw2FpNt1eDfy`</summary>

```text
Web search results for query: "GRPO Mind2Web web agent reinforcement learning"

Links: [{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://arxiv.org/html/2306.06070v3"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336"},{"title":"[PDF] Mind2Web: Towards a Generalist Agent for the Web | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mind2Web:-Towards-a-Generalist-Agent-for-the-Web-Deng-Gu/58f8925a8b87054ad0635a6398a7fe24935b1604"},{"title":"[2306.06070] Mind2Web: Towards a Generalist Agent for the Web","url":"https://arxiv.org/abs/2306.06070"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | Request PDF","url":"https://www.researchgate.net/publication/371490628_Mind2Web_Towards_a_Generalist_Agent_for_the_Web"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | OpenReview","url":"https://openreview.net/forum?id=kiYqbO3wqw"},{"title":"MIND2WEB: Towards a Generalist Agent for the Web Xiang Deng∗ Yu Gu Boyuan Zheng","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/5950bf290a1570ea401bf98882128160-Paper-Datasets_and_Benchmarks.pdf"}]

Based on the search results, here's what I found about GRPO, Mind2Web, and web agents with reinforcement learning:

## Mind2Web Dataset

Mind2Web is the first dataset for developing and evaluating generalist agents for the web. Mind2Web contains 2,350 tasks from 137 websites spanning 31 domains and can follow language instructions to complete complex tasks on any website.

## GRPO in Web Agent Training

GRPO (Group Relative Policy Optimization) appears in recent research on training web agents. Inspired by group relative policy optimization (GRPO), researchers have extended it to multi-turn settings (M-GRPO) for training web agents, employing an asynchronous trajectory rollout strategy to further improve training efficiency.

Additionally, GRPO has been employed for offline reinforcement learning training with a group size of 8 in web agent development.

## Reinforcement Learning with Mind2Web

Future directions for Mind2Web include integrating multi-modal information, reinforcement learning with feedback from real websites, and specialized LMs for web understanding and action taking.

Recent work has successfully combined these approaches, with methods substantially improving task success rates of web agents—boosting Qwen-2.5-3B from 6.1% to 33.9% and Llama-3.1-8B from 8.5% to 44.8%—surpassing previous state-of-the-art results on the WebArena-Lite benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f913bbd-7ce7-4ea6-9a93-8ccf744f433b",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "decdfb11-771c-4488-9f4b-6a14ccd8d1b8",
  "sourceToolAssistantUUID": "4f913bbd-7ce7-4ea6-9a93-8ccf744f433b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:25:37.746Z_

<details><summary>↩ Tool result · `toolu_01BDdm8HjN6ZhmjoaME6ZMue`</summary>

```text
Web search results for query: "verl-agent Mind2Web GiGPO"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"verl-agent - a langfeng01 Collection","url":"https://huggingface.co/collections/langfeng01/verl-agent-684970e8f51babe2a6d98554"},{"title":"GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub","url":"https://github.com/verl-project/verl"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"verl-agent/gigpo at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/gigpo"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"},{"title":"[2506.21506] Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://arxiv.org/abs/2506.21506"}]

Based on the search results, here's what I found about these three related projects:

## verl-agent

verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for the paper "Group-in-Group Policy Optimization for LLM Agent Training". It supports multiple RL algorithms including GiGPO, GRPO, PPO, DAPO, GSPO, RLOO, and REINFORCE++.

## GiGPO (Group-in-Group Policy Optimization)

GiGPO is a novel algorithm designed to support fine-grained credit assignment in long-horizon LLM agent training. It introduces a two-level grouping mechanism: Episode-level groups capture overall task success via total returns (like GRPO), while step-level groups gather repeated states across trajectories to compute relative advantages for individual actions. GiGPO is fully critic-free, maintains the same GPU memory footprint and LLM rollout cost as GRPO, yet achieves significantly better training efficiency and performance.

## Mind2Web

Mind2Web is a dataset for developing and evaluating generalist agents for the web that can follow language instructions to complete complex tasks on any website, containing 2,350 tasks from 137 websites spanning 31 domains.

These three elements work together in agent training research - verl-agent provides the training framework, GiGPO is a cutting-edge algorithm implemented within that framework, and Mind2Web is one of the benchmark datasets used to evaluate these agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c34f3d41-33ec-445a-98c6-59766523292a",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "7a7aa068-595c-404c-90e7-1b4a05e75f35",
  "sourceToolAssistantUUID": "c34f3d41-33ec-445a-98c6-59766523292a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T19:25:40.621Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012RkEaAaK7AzTtsugumJ621`</summary>

```json
{
  "query": "GiGPO ALFWorld WebShop results Qwen 7B score table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a7aa068-595c-404c-90e7-1b4a05e75f35",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSHgrhAjkz17WmH1qAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbd21b21-39fc-475c-9922-f1debf6851c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158FHNKHH8cFaWFMfDzoFnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 14123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T19:25:41.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EgSDAzXtAxK82jpvVUwaVj`</summary>

```json
{
  "query": "Mind2Web benchmark best results element accuracy step success 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbd21b21-39fc-475c-9922-f1debf6851c5",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSHgrhAjkz17WmH1qAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e5207b4-7fd4-485f-b4ba-4f7dca44e050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158FHNKHH8cFaWFMfDzoFnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 14123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T19:25:42.096Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QdSpbUAA7Kk6hdRcju1SPv`</summary>

```json
{
  "query": "Agentic Critical Training ACT ALFWorld WebShop score 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e5207b4-7fd4-485f-b4ba-4f7dca44e050",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSHgrhAjkz17WmH1qAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bb6a9b6-51b3-473a-9b78-f33694276bc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158FHNKHH8cFaWFMfDzoFnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 14123,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2959,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T19:25:42.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CabVvF7JRr512amS63uGjm`</summary>

```json
{
  "query": "verl-agent supported benchmarks Mind2Web environment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bb6a9b6-51b3-473a-9b78-f33694276bc5",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSHgrhAjkz17WmH1qAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fda9d022-82f8-4373-b025-e9c64d4a7f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158FHNKHH8cFaWFMfDzoFnR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 14123,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 968,
          "output_tokens": 218,
          "cache_read_input_tokens": 14123,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2959,
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

_source line 27 · 2026-05-10T19:25:46.874Z_

<details><summary>↩ Tool result · `toolu_012RkEaAaK7AzTtsugumJ621`</summary>

```text
Web search results for query: "GiGPO ALFWorld WebShop results Qwen 7B score table"

Links: [{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Phase-Aware Mixture of Experts for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2602.17038"},{"title":"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/html/2602.16165"},{"title":"AgentRL: Scaling Agentic Reinforcement Learning with a ...","url":"https://arxiv.org/pdf/2510.04206"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training - Consensus","url":"https://consensus.app/papers/groupingroup-policy-optimization-for-llm-agent-training-an-feng/ae6de571c22e532d95865b46257f2719/"},{"title":"Retrieval-Augmented LLM Agents: Learning to Learn from Experience","url":"https://arxiv.org/html/2603.18272"},{"title":"Qwen (Qwen)","url":"https://huggingface.co/Qwen"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld"},{"title":"Qwen Studio","url":"https://qwen.ai/blog?id=qwen3.6-27b"}]

Based on the search results, I found relevant information about GiGPO's performance on ALFWorld and WebShop benchmarks with Qwen models.

## GiGPO Results with Qwen on ALFWorld and WebShop

GiGPO (without standard deviation) surpasses GRPO by 13.3% on ALFWorld and 10.6% on WebShop at 1.5B, and by 12.6% and 9.1%, respectively, at 7B.

The experiments with Qwen2.5-1.5B/3B/7B-Instruct show that GiGPO consistently outperforms prompt-based agents, actor-critic baselines, and prior group-based RL methods, achieving performance gains of greater than 12% on ALFWorld and greater than 9% on WebShop over GRPO.

The search results reference the GiGPO paper which includes detailed score tables comparing GiGPO's performance across different model sizes (1.5B, 3B, and 7B) against baselines like PPO, GRPO, and RLOO. However, the specific table data itself is not fully reproduced in these search results. For the complete score tables with exact numbers, you may want to directly access the full GiGPO paper at the provided sources (particularly the arxiv.org/html/2505.10978v1 link or the PDF at ntu.edu.sg).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbd21b21-39fc-475c-9922-f1debf6851c5",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "fdfd84a5-6bb0-4421-b568-f55445b895df",
  "sourceToolAssistantUUID": "dbd21b21-39fc-475c-9922-f1debf6851c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T19:25:48.473Z_

<details><summary>↩ Tool result · `toolu_01QdSpbUAA7Kk6hdRcju1SPv`</summary>

```text
Web search results for query: "Agentic Critical Training ACT ALFWorld WebShop score 2026"

Links: [{"title":"Agentic Critical Training","url":"https://arxiv.org/html/2603.08706v1"},{"title":"Agentic Critical Training","url":"https://attention-is-all-i-need.github.io/ACT/"},{"title":"Paper published at the Lifelong Agent Workshop @ ICLR 2026 MAGE:","url":"https://openreview.net/pdf/d80ccf0395e94992b8cb63a1961d4b4612df0a4e.pdf"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v3"},{"title":"SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/html/2602.08234"},{"title":"AGENTRL: SCALING AGENTIC REINFORCEMENT ...","url":"https://openreview.net/pdf?id=zq3vAmuUk9"},{"title":"AgentRL: Scaling Agentic Reinforcement Learning with a ...","url":"https://arxiv.org/pdf/2510.04206"},{"title":"Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks","url":"https://arxiv.org/html/2602.22817"},{"title":"15 Agentic AI Design Patterns You Should Know: Research-Backed and Emerging Frameworks (2026)","url":"https://aitoolsclub.com/15-agentic-ai-design-patterns-you-should-know-research-backed-and-emerging-frameworks-2026/"},{"title":"Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents","url":"https://arxiv.org/html/2601.18217"}]

Based on the search results, I found information about Agentic Critical Training (ACT) and its performance on ALFWorld and WebShop benchmarks:

## Agentic Critical Training (ACT) Overview

ACT is a reinforcement learning paradigm that trains LLM agents to identify better actions among alternatives, producing genuine self-reflection rather than imitating it.

## Performance on ALFWorld and WebShop (2026)

ACT consistently improves agent performance when combined with different post-training methods across three challenging agent benchmarks (ALFWorld, WebShop, ScienceWorld).

The specific performance improvements include:

- ACT provides an average improvement of 5.07 percentage points over imitation learning (IL) and 4.62 percentage points over reinforcement learning (RL).

- ACT's gain on out-of-distribution (OOD) tasks (3.73pp) is larger than on in-distribution (ID) tasks (2.15pp), indicating the reasoning generalizes to unseen configurations.

- RL w/ ACT achieves the best overall performance.

The research demonstrates that because ACT is trained through RL rather than imitation learning, the model must autonomously discover chain-of-thought reasoning that causally leads to correct action selection, with the model rewarded only for selecting correctly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bb6a9b6-51b3-473a-9b78-f33694276bc5",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "bc703837-fbbd-4394-921c-93e0f19c29a4",
  "sourceToolAssistantUUID": "5bb6a9b6-51b3-473a-9b78-f33694276bc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T19:25:48.863Z_

<details><summary>↩ Tool result · `toolu_01EgSDAzXtAxK82jpvVUwaVj`</summary>

```text
Web search results for query: "Mind2Web benchmark best results element accuracy step success 2025 2026"

Links: [{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"GitHub - OSU-NLP-Group/Online-Mind2Web: An Illusion of Progress? Assessing the Current State of Web Agents · GitHub","url":"https://github.com/OSU-NLP-Group/Online-Mind2Web"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents | OpenReview","url":"https://openreview.net/forum?id=6jZi4HSs6o"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents","url":"https://arxiv.org/html/2504.01382v4"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://osu-nlp-group.github.io/Mind2Web-2/"},{"title":"Online-Mind2Web Benchmark","url":"https://www.emergentmind.com/topics/online-mind2web-benchmark"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge | OpenReview","url":"https://openreview.net/forum?id=AUaW6DS9si"},{"title":"HAL: Online Mind2Web Leaderboard","url":"https://hal.cs.princeton.edu/online_mind2web"}]

Based on the search results, here's what I found about Mind2Web benchmark best results for element accuracy, step success, and other metrics in 2025-2026:

## Online-Mind2Web Benchmark Results (2025)

The Operator agent achieves 61.3% human-evaluated success rate (71.8% WebJudge), which represents the best performance on the more recent Online-Mind2Web benchmark. However, most other agents cluster at 28–30% (WebJudge 34–40%), a stark drop from previously reported >90% success on WebVoyager.

## Key Metrics and Evaluation Framework

The Step-Level Evaluation measures completion rate, where for each task an agent receives a point for each correctly achieved key node using one of three target types (URL, element path, or element value). Task-Level Evaluation considers a task successfully completed if all key nodes are achieved, with the Task Success Rate (SR) being the average across tasks.

## Mind2Web 2 Results (2025)

The best-performing system, OpenAI Deep Research, can achieve 50-70% of human performance while spending half the time on the Mind2Web 2 benchmark for agentic search tasks.

The search results show that web agent performance metrics have become more rigorous and realistic, with the newer Online-Mind2Web benchmark revealing significantly lower success rates than previously reported metrics on older benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e5207b4-7fd4-485f-b4ba-4f7dca44e050",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "5e4175fa-26f6-43c0-be17-732e8d6bc930",
  "sourceToolAssistantUUID": "5e5207b4-7fd4-485f-b4ba-4f7dca44e050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:25:50.323Z_

<details><summary>↩ Tool result · `toolu_01CabVvF7JRr512amS63uGjm`</summary>

```text
Web search results for query: "verl-agent supported benchmarks Mind2Web environment"

Links: [{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | OpenReview","url":"https://openreview.net/forum?id=kiYqbO3wqw"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://osu-nlp-group.github.io/Mind2Web-2/"},{"title":"GitHub - OSU-NLP-Group/Mind2Web-2: [NeurIPS'25 D&B] Mind2Web-2 Benchmark: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://github.com/OSU-NLP-Group/Mind2Web-2"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge | OpenReview","url":"https://openreview.net/forum?id=AUaW6DS9si"},{"title":"GitHub - OSU-NLP-Group/Online-Mind2Web: An Illusion of Progress? Assessing the Current State of Web Agents · GitHub","url":"https://github.com/OSU-NLP-Group/Online-Mind2Web"},{"title":"WebCanvas: Benchmarking Web Agents in Online Environments | OpenReview","url":"https://openreview.net/forum?id=wkp57p0uhm"},{"title":"How we built the best browser agent with Auto-Research","url":"https://browser-use.com/posts/online-mind2web-benchmark"}]

The search results provide information about Mind2Web and related benchmarks, but don't specifically mention "verl-agent" or its supported benchmarks. Let me search more specifically for that.

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use","url":"https://arxiv.org/html/2509.01055v1"},{"title":"Performance Tuning Guide — verl documentation","url":"https://verl.readthedocs.io/en/latest/perf/perf_tuning.html"},{"title":"Dongfu Jiang on X: \"Introducing VerlTool - a unified and easy-to-extend tool agent training framework based on verl. Recently, there's been a growing trend toward training tool agents with reinforcement learning algorithms like GRPO and PPO. Representative works include SearchR1, ToRL, ReTool, and https://t.co/dF6lcpg7C9\" / X","url":"https://x.com/DongfuJiang/status/1929198238017720379"},{"title":"Verlog: A Multi-turn RL framework for LLM agents – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2025/09/15/verlog-a-multi-turn-rl-framework-for-llm-agents/"},{"title":"How to train and scale AI math/coding agents using VeRL on any AI infra | SkyPilot Blog","url":"https://blog.skypilot.co/verl-rl-training/"},{"title":"Agentic RL frameworks and environments: Torchforge, ACE, Verl, openenv | by evoailabs | Medium","url":"https://evoailabs.medium.com/agentic-rl-frameworks-torchforge-ace-verl-3dd116b987dc"},{"title":"VERL - Agent-lightning","url":"https://microsoft.github.io/agent-lightning/latest/algorithm-zoo/verl/"},{"title":"AgentFly: Extensible and Scalable Reinforcement Learning for LM Agents","url":"https://arxiv.org/html/2507.14897v1"},{"title":"Training a Coding Agent with veRL - a Lightning environment by lantiga","url":"https://lightning.ai/lightning-ai/environments/training-a-coding-agent-with-verl"}]

Based on the search results, I found information about verl-agent and its supported environments. Here's what I found:

## VERL-Agent Supported Environments

The supported environments are adapted from ALFWorld, Sokoban, SkyRL-Gym, Search-R1, Gym Cards, WebShop, and AppWorld.

Verl-agent offers a diverse set of interactive environments including Search-R1 experiment, embodied AI environments like ALFWorld, visual games such as Sokoban and Gym Cards, and digital interface control tasks like WebShop and AppWorld (experimental).

However, regarding **Mind2Web** specifically, the search results do not show Mind2Web as one of the officially supported benchmarks/environments listed for verl-agent. The supported environments appear to be focused on different types of tasks (text-based reasoning, embodied AI, visual games, and web/app interfaces), but Mind2Web is not explicitly mentioned in the verl-agent documentation.

If you're looking to use Mind2Web with verl-agent, you may need to create a custom environment adapter, as verl-agent is designed to be extensible for different environment types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fda9d022-82f8-4373-b025-e9c64d4a7f81",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "89f7b378-d673-4a77-b0ba-23d3410e5b04",
  "sourceToolAssistantUUID": "fda9d022-82f8-4373-b025-e9c64d4a7f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T19:25:54.439Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018QGFQt191aYHQAho2nkge6`</summary>

```json
{
  "query": "GiGPO paper exact scores ALFWorld WebShop Qwen2.5-7B table results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f7b378-d673-4a77-b0ba-23d3410e5b04",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSJcdUbsynQgE1hVFRT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72ffddc9-2ece-4e25-9f99-96d0e664f53d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwZxZdrv7UJMdPqmDvmzkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5290,
      "cache_read_input_tokens": 17082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T19:25:55.369Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kfs93khiufYDwbUW7iCaRz`</summary>

```json
{
  "query": "ACT Agentic Critical Training ALFWorld exact score percentage table arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72ffddc9-2ece-4e25-9f99-96d0e664f53d",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSJcdUbsynQgE1hVFRT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f31b91d9-a060-419e-889e-066b40fb2c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwZxZdrv7UJMdPqmDvmzkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5290,
      "cache_read_input_tokens": 17082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5290,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T19:25:56.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Csqdgyt442Nhav4ZhQDSrQ`</summary>

```json
{
  "query": "Mind2Web element accuracy cross-task cross-website cross-domain best results 7B model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f31b91d9-a060-419e-889e-066b40fb2c97",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSJcdUbsynQgE1hVFRT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ff358b3-4730-4ba1-9058-b79562239451",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwZxZdrv7UJMdPqmDvmzkv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5290,
      "cache_read_input_tokens": 17082,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5290
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 17082,
          "cache_creation_input_tokens": 5290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5290,
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

_source line 34 · 2026-05-10T19:26:00.387Z_

<details><summary>↩ Tool result · `toolu_018QGFQt191aYHQAho2nkge6`</summary>

```text
Web search results for query: "GiGPO paper exact scores ALFWorld WebShop Qwen2.5-7B table results"

Links: [{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Phase-Aware Mixture of Experts for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2602.17038"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v3"},{"title":"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/html/2602.16165"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training - Consensus","url":"https://consensus.app/papers/groupingroup-policy-optimization-for-llm-agent-training-an-feng/ae6de571c22e532d95865b46257f2719/"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop"},{"title":"Can GRPO Boost Complex Multimodal Table ...","url":"https://aclanthology.org/2025.emnlp-main.637.pdf"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen2.5 7B Instruct Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen-2.5-7b-instruct"}]

Based on the search results, here is information about the GiGPO paper's exact scores for ALFWorld and WebShop with Qwen2.5-7B:

## GiGPO Performance with Qwen2.5-7B

GiGPO achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO, along with remarkable performance on search-based QA tasks (42.1% on 3B and 47.2% on 7B).

However, the search results I found don't contain the exact/precise table values for the Qwen2.5-7B results on ALFWorld and WebShop. The paper appears to report relative improvements over baselines rather than absolute scores in the accessible sections.

For reference, related work shows that with Qwen2.5-7B, HiPER achieves 97.4% on ALFWorld and 83.3% on WebShop, both exceeding GiGPO by around +7%, which suggests the GiGPO baseline scores were approximately 90.2% on ALFWorld and around 76% on WebShop, though these are derived figures rather than directly stated results.

To find the exact table with the specific GiGPO scores, you may need to consult the full paper PDF directly or look for the results table in the paper's main sections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72ffddc9-2ece-4e25-9f99-96d0e664f53d",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "6493124a-3e22-49e2-a179-64f421fd9b2a",
  "sourceToolAssistantUUID": "72ffddc9-2ece-4e25-9f99-96d0e664f53d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T19:26:02.167Z_

<details><summary>↩ Tool result · `toolu_01Kfs93khiufYDwbUW7iCaRz`</summary>

```text
Web search results for query: "ACT Agentic Critical Training ALFWorld exact score percentage table arxiv"

Links: [{"title":"Agentic Critical Training","url":"https://arxiv.org/html/2603.08706v1"},{"title":"Agentic Critical Training","url":"https://attention-is-all-i-need.github.io/ACT/"},{"title":"[2603.08706] Agentic Critical Training","url":"https://arxiv.org/abs/2603.08706"},{"title":"AgentRL: Scaling Agentic Reinforcement Learning with a ...","url":"https://arxiv.org/pdf/2510.04206"},{"title":"Work in Progress ReAct Meets ActRe: When Language Agents Enjoy Training","url":"https://arxiv.org/pdf/2403.14589"},{"title":"[2603.08706v1] Agentic Critical Training","url":"https://arxiv.org/abs/2603.08706v1"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v1"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"},{"title":"AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents Chang Ma∗♠","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"Preprint. Under Review. A PRACTITIONER’S GUIDE TO MULTI-TURN AGENTIC","url":"https://arxiv.org/pdf/2510.01132"}]

I found the paper on Agentic Critical Training (ACT). Based on the search results, I can provide you with information about the ACT results on ALFWorld:

ALFWorld reports success rates, and ACT provides positive transfer: Adding ACT yields an average improvement of 5.07pp over IL and 4.62pp over RL. RL w/ ACT achieves the best overall performance.

The paper is available on arXiv (2603.08706) and was published on March 9, 2026. The researchers evaluate ACT on three diverse benchmarks: ALFWorld (embodied household tasks), WebShop (web-based shopping), and ScienceWorld (scientific reasoning). All methods are trained on exactly the same expert trajectories.

For more detailed specific score percentage tables for ALFWorld, you would need to access the full paper directly at the arxiv links (https://arxiv.org/html/2603.08706v1 or https://arxiv.org/abs/2603.08706), as the exact numerical percentage table data from the paper is not fully reproduced in the search results I retrieved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f31b91d9-a060-419e-889e-066b40fb2c97",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "dbac62f3-01b2-402c-8328-5c9b2ed51e51",
  "sourceToolAssistantUUID": "f31b91d9-a060-419e-889e-066b40fb2c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T19:26:03.898Z_

<details><summary>↩ Tool result · `toolu_01Csqdgyt442Nhav4ZhQDSrQ`</summary>

```text
Web search results for query: "Mind2Web element accuracy cross-task cross-website cross-domain best results 7B model 2025 2026"

Links: [{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Success rate on Mind2Web cross-task, cross-website, and cross-domain... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-on-Mind2Web-cross-task-cross-website-and-cross-domain-generalization-test_tbl4_383951232"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://ukgovernmentbeis.github.io/inspect_evals/evals/assistants/mind2web/"},{"title":"osunlp/Mind2Web · Datasets at Hugging Face","url":"https://huggingface.co/datasets/osunlp/Mind2Web"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | OpenReview","url":"https://openreview.net/forum?id=kiYqbO3wqw"},{"title":"GitHub - OSU-NLP-Group/Online-Mind2Web: An Illusion of Progress? Assessing the Current State of Web Agents · GitHub","url":"https://github.com/OSU-NLP-Group/Online-Mind2Web"},{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v3"},{"title":"arXiv:2502.11357v2 [cs.AI] 19 Feb 2025","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/03/explorer_arxiv.pdf"}]

Based on the search results, here's what I found regarding Mind2Web element accuracy on cross-task, cross-website, and cross-domain benchmarks with 7B models in 2025-2026:

## Key Findings

**Mind2Web Dataset Overview:**
Mind2Web contains 2,350 tasks spanning 137 websites, with three levels of generalization testing: Cross Task Generalization (across tasks in the same environment), Cross Website Generalization (across websites under the same domain), and Cross Domain Generalization (across tasks and environments).

**7B Model Performance:**
Recent research has highlighted strong 7B model performance on Mind2Web. Fine-tuned WebJudge-7B weights have been released as a robust and reliable reward model for Reinforcement learning. Additionally, DeepMiner-Mano-7B was developed through a three-stage training methodology built upon UI-TARS-1.5-7B, encompassing SFT, offline RL, and online RL.

**State-of-the-Art Results:**
Empirical evaluations on Mind2Web demonstrate Mano's superiority in multiple key performance metrics, setting new state-of-the-art standards in success rate, element precision, and stepwise completion.

**Recent Benchmark Extensions:**
The original static Mind2Web benchmark has been extended with Mind2Web-live, an online benchmark for web agents, which employs multi-phase filtering, re-annotation, and replay mechanisms to ensure that 542 diverse web tasks yield accurate, reproducible evaluation data.

The search results show active research in 2025 with improved 7B model architectures and evaluation methodologies, though specific element accuracy percentages for all three generalization settings are not detailed in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ff358b3-4730-4ba1-9058-b79562239451",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "6bf392c6-0dae-432b-8b74-be146b856788",
  "sourceToolAssistantUUID": "9ff358b3-4730-4ba1-9058-b79562239451",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-10T19:26:08.362Z_

Let me fetch the actual paper pages for exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bf392c6-0dae-432b-8b74-be146b856788",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSKcgySJ5wc92hNPnzR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91388cce-e55c-407d-b7df-2b79e76cfe42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxYdAJqiepappHbYitRJs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2887,
      "cache_read_input_tokens": 22372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2887,
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

_source line 38 · 2026-05-10T19:26:10.260Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VnUNvkwQg9AeTUWfUs35vi`</summary>

```json
{
  "query": "arxiv 2505.10978 GiGPO ALFWorld 90.8 WebShop 75.0 Qwen2.5-7B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91388cce-e55c-407d-b7df-2b79e76cfe42",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSKcgySJ5wc92hNPnzR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80906eef-645a-4265-8d28-1f638125a223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxYdAJqiepappHbYitRJs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2887,
      "cache_read_input_tokens": 22372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2887,
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

_source line 39 · 2026-05-10T19:26:11.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FsznvcNCJoo83KGRMjgHho`</summary>

```json
{
  "query": "HiPER arxiv 2602.16165 ALFWorld 97.4 WebShop 83.3 GiGPO baseline comparison table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80906eef-645a-4265-8d28-1f638125a223",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSKcgySJ5wc92hNPnzR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ababaf80-45ac-4637-9654-bca3401e7788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxYdAJqiepappHbYitRJs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2887,
      "cache_read_input_tokens": 22372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2887,
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

_source line 40 · 2026-05-10T19:26:12.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GQZTz2uxQgfyiUMNxxk2dN`</summary>

```json
{
  "query": "Embodied-Planner-R1 ALFWorld unseen 96.27 seen 99.29 Qwen model size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ababaf80-45ac-4637-9654-bca3401e7788",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSKcgySJ5wc92hNPnzR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2a83090-2425-48f1-acd5-8b291af48786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxYdAJqiepappHbYitRJs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2887,
      "cache_read_input_tokens": 22372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2887,
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

_source line 41 · 2026-05-10T19:26:13.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Atd9x3SypaQxo6pvUmtZ1i`</summary>

```json
{
  "query": "SkillRL ALFWorld WebShop score 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2a83090-2425-48f1-acd5-8b291af48786",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSKcgySJ5wc92hNPnzR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce546b34-a439-418e-882e-e5bcc11d121b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxYdAJqiepappHbYitRJs7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2887,
      "cache_read_input_tokens": 22372,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 22372,
          "cache_creation_input_tokens": 2887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2887,
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

_source line 42 · 2026-05-10T19:26:16.385Z_

<details><summary>↩ Tool result · `toolu_01VnUNvkwQg9AeTUWfUs35vi`</summary>

```text
Web search results for query: "arxiv 2505.10978 GiGPO ALFWorld 90.8 WebShop 75.0 Qwen2.5-7B"

Links: [{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://arxiv.org/pdf/2505.10978"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978"},{"title":"[2505.10978] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop"},{"title":"Phase-Aware Mixture of Experts for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2602.17038"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"Hindsight Credit Assignment for Long-Horizon LLM Agents","url":"https://arxiv.org/html/2603.08754"},{"title":"Graph-Enhanced Policy Optimization in LLM Agent Training","url":"https://arxiv.org/html/2510.26270"}]

Based on the search results, I found information about arxiv paper 2505.10978. Here's what the paper is about:

The paper introduces Group-in-Group Policy Optimization (GiGPO), a novel RL algorithm that achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.

Regarding the performance metrics you mentioned:

GiGPO achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO, along with remarkable performance on search-based QA tasks (42.1% on 3B and 47.2% on 7B).

The experiments use Qwen2.5-1.5B/3B/7B-Instruct models.

The specific performance numbers you mentioned (90.8% on ALFWorld and 75.0% on WebShop for Qwen2.5-7B) appear to be the actual benchmark results, though I note from another paper that on ALFWorld (7B), GiGPO achieves an overall success rate of 90.8%, which matches your ALFWorld figure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80906eef-645a-4265-8d28-1f638125a223",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "6704a20f-5146-473b-9bb9-4b44fdf86499",
  "sourceToolAssistantUUID": "80906eef-645a-4265-8d28-1f638125a223",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T19:26:17.568Z_

<details><summary>↩ Tool result · `toolu_01GQZTz2uxQgfyiUMNxxk2dN`</summary>

```text
Web search results for query: "Embodied-Planner-R1 ALFWorld unseen 96.27 seen 99.29 Qwen model size"

Links: [{"title":"GitHub - OpenMOSS/Embodied-Planner-R1: Embodied-Planner-R1: Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning · GitHub","url":"https://github.com/OpenMOSS/Embodied-Planner-R1"},{"title":"Unleashing Embodied Task Planning Ability in LLMs via ...","url":"https://arxiv.org/pdf/2506.23127"},{"title":"Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2506.23127"},{"title":"[2506.23127] Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2506.23127"},{"title":"IffYuan/Embodied-R1-3B-v1 · Hugging Face","url":"https://huggingface.co/IffYuan/Embodied-R1-3B-v1"},{"title":"alfworld: aligning text and embodied environments for ...","url":"https://arxiv.org/pdf/2010.03768"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"ALFWORLD: ALIGNING TEXT AND EMBODIED ...","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"Embodied-R1: RL for Embodied AI","url":"https://www.emergentmind.com/topics/embodied-r1"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://vagen-ai.github.io/vagen_paper.pdf"}]

Based on the search results, I found information about Embodied-Planner-R1 and its performance metrics:

On the ALFWorld benchmark, Embodied Planner-R1 achieved accuracy rates of 99.29% and 96.27% in seen and unseen scenarios, respectively. 

The model builds upon the foundation of Qwen2.5-7B-Instruct, making the model size **7 billion parameters**. The training was performed at a context length of 4096.

The performance metrics you mentioned (96.27% for unseen and 99.29% for seen) correspond to Embodied-Planner-R1's ALFWorld evaluation results, and it surpassed the previous best method ETO by 15.00% and 16.42%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2a83090-2425-48f1-acd5-8b291af48786",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "64d3b49a-0701-4067-bb22-bc1377d541c1",
  "sourceToolAssistantUUID": "a2a83090-2425-48f1-acd5-8b291af48786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T19:26:17.598Z_

<details><summary>↩ Tool result · `toolu_01FsznvcNCJoo83KGRMjgHho`</summary>

```text
Web search results for query: "HiPER arxiv 2602.16165 ALFWorld 97.4 WebShop 83.3 GiGPO baseline comparison table"

Links: [{"title":"HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/html/2602.16165"},{"title":"[2602.16165] HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/abs/2602.16165"},{"title":"[2602.16165v1] HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents","url":"https://arxiv.org/abs/2602.16165v1"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"},{"title":"SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/html/2602.08234"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | OpenReview","url":"https://openreview.net/forum?id=0IOX0YcCdTn"},{"title":"Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks","url":"https://arxiv.org/html/2602.22817"},{"title":"Proximity-Based Multi-Turn Optimization: Practical Credit Assignment for LLM Agent Training","url":"https://arxiv.org/html/2602.19225"},{"title":"[PDF] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ALFWorld:-Aligning-Text-and-Embodied-Environments-Shridhar-Yuan/398a0625e8707a0b41ac58eaec51e8feb87dd7cb"}]

I found the paper! Here's what the search results show about HiPER and the performance metrics you mentioned:

HiPER achieves state-of-the-art performance on challenging interactive benchmarks, reaching 97.4% success on ALFWorld and 83.3% on WebShop with Qwen2.5-7B-Instruct (+6.6% and +8.3% over the best prior method). The method consistently outperforms all evaluated baseline methods, including the best known prior method GiGPO.

The paper (arxiv 2602.16165) is titled "HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents." It identifies a consistent implicit hierarchical structure in successful multi-turn LLM agent behavior and makes it explicit through a Plan–Execute interface that separates high-level subgoal planning from low-level action execution.

The comparison table you're asking about should be available in the full paper at https://arxiv.org/html/2602.16165, where Table 1 reports the success rate (%) of all six task categories and overall success rate for ALFWorld, and for WebShop reports the task score and success rate (%).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ababaf80-45ac-4637-9654-bca3401e7788",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "48ed6329-beb8-4fd2-ab67-57d7d635ef72",
  "sourceToolAssistantUUID": "ababaf80-45ac-4637-9654-bca3401e7788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T19:26:17.928Z_

<details><summary>↩ Tool result · `toolu_01Atd9x3SypaQxo6pvUmtZ1i`</summary>

```text
Web search results for query: "SkillRL ALFWorld WebShop score 2026"

Links: [{"title":"SKILLRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/pdf/2602.08234"},{"title":"SkillRL: Recursive Skill-Augmented RL","url":"https://www.emergentmind.com/papers/2602.08234"},{"title":"GitHub - aiming-lab/SkillRL: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning · GitHub","url":"https://github.com/aiming-lab/SkillRL"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"},{"title":"Paper page - SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://huggingface.co/papers/2602.08234"},{"title":"SKILLRL: EVOLVING AGENTS VIA RECURSIVE SKILL","url":"https://openreview.net/pdf/28faf9da2a024d3f3a3fbb4ccf04b3d89a15cba0.pdf"},{"title":"[2602.08234] SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/abs/2602.08234"},{"title":"🥇Top AI Papers of the Week","url":"https://nlp.elvissaravia.com/p/top-ai-papers-of-the-week-544"},{"title":"Agent Era Triggering the Great AI Market Reset?","url":"https://www.superintelligencenewsletter.com/p/agent-era-triggering-the-great-ai"},{"title":"SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/400604241_SkillRL_Evolving_Agents_via_Recursive_Skill-Augmented_Reinforcement_Learning"}]

Based on the search results, here are the key scores for SkillRL on ALFWorld and WebShop in 2026:

## ALFWorld Performance
SkillRL achieves 89.9% average success on ALFWorld, outperforming the strongest non-skill RL baseline (GRPO) by 15.3% absolute.

## WebShop Performance
SkillRL attains a 72.7% average success rate on WebShop, consistently beating memory-based and RL-based baselines.

These results come from a research paper published in February 2026, where SkillRL achieves state-of-the-art performance across ALFWorld, WebShop and seven search-augmented tasks, outperforming strong baselines by over 15.3%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce546b34-a439-418e-882e-e5bcc11d121b",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "a3659a7e-07b0-4342-80ba-aead21629c5d",
  "sourceToolAssistantUUID": "ce546b34-a439-418e-882e-e5bcc11d121b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T19:26:20.981Z_

Now let me get the remaining details on Embodied-Planner-R1 overall score and Mind2Web specific numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3659a7e-07b0-4342-80ba-aead21629c5d",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSLef5KZSVBiqJPhEmv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a896c8c-d6f9-47ac-8c06-f0d80fd7f72c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXWzuacSYBU8F3YNb7fohY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3577,
      "cache_read_input_tokens": 25259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3577,
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

_source line 47 · 2026-05-10T19:26:21.992Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017RQMMDkMbgRQAojZJWwh8v`</summary>

```json
{
  "query": "Embodied-Planner-R1 overall ALFWorld 97.78 average seen unseen combined"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a896c8c-d6f9-47ac-8c06-f0d80fd7f72c",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSLef5KZSVBiqJPhEmv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6819fa9-c6f4-4b2d-9f55-d291de076352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXWzuacSYBU8F3YNb7fohY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3577,
      "cache_read_input_tokens": 25259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3577,
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

_source line 48 · 2026-05-10T19:26:23.958Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CRusGKueCCkzDE2D282Gcy`</summary>

```json
{
  "query": "Mind2Web offline benchmark element accuracy step success rate 2025 2026 fine-tuned 7B agent results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6819fa9-c6f4-4b2d-9f55-d291de076352",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSLef5KZSVBiqJPhEmv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2ab686c-573d-47e9-ad70-e567c596e6f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXWzuacSYBU8F3YNb7fohY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3577,
      "cache_read_input_tokens": 25259,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 25259,
          "cache_creation_input_tokens": 3577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3577,
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

_source line 49 · 2026-05-10T19:26:23.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UPsbZVKS9VxAE3VFaQxNC6`</summary>

```json
{
  "query": "AgentTrek DigiRL WebAgent-R1 Mind2Web reinforcement learning results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2ab686c-573d-47e9-ad70-e567c596e6f2",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSLef5KZSVBiqJPhEmv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1410616f-9eaa-40eb-9520-c86328d7b3df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BXWzuacSYBU8F3YNb7fohY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3577,
      "cache_read_input_tokens": 25259,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3577
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 25259,
          "cache_creation_input_tokens": 3577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3577,
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

_source line 50 · 2026-05-10T19:26:28.231Z_

<details><summary>↩ Tool result · `toolu_017RQMMDkMbgRQAojZJWwh8v`</summary>

```text
Web search results for query: "Embodied-Planner-R1 overall ALFWorld 97.78 average seen unseen combined"

Links: [{"title":"Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2506.23127"},{"title":"Unleashing Embodied Task Planning Ability in LLMs via ...","url":"https://arxiv.org/pdf/2506.23127"},{"title":"GitHub - OpenMOSS/Embodied-Planner-R1: Embodied-Planner-R1: Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning · GitHub","url":"https://github.com/OpenMOSS/Embodied-Planner-R1"},{"title":"[2506.23127] Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2506.23127"},{"title":"ALFWORLD: ALIGNING TEXT AND EMBODIED ...","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"ALFWorld Suite: Dual-View AI Simulator","url":"https://www.emergentmind.com/topics/alfworld-suite"},{"title":"[Literature Review] Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://www.themoonlight.io/en/review/unleashing-embodied-task-planning-ability-in-llms-via-reinforcement-learning"},{"title":"ALFWorld: Textual and Embodied Agent Benchmark","url":"https://www.emergentmind.com/topics/alfworld"},{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"Constrained Natural Language Action Planning for Resilient Embodied Systems","url":"https://arxiv.org/html/2510.06357v1"}]

Based on the search results, I found detailed information about Embodied-Planner-R1's performance on ALFWorld:

On the ALFWorld benchmark, Embodied Planner-R1 achieved accuracy rates of 99.29% and 96.27% in seen and unseen scenarios, respectively. The overall combined average result you mentioned (97.78%) represents the average performance across both seen and unseen environments.

The model exhibits robust generalization, with only a -3.33% generation gap in unseen environments—substantially lower than comparable methods. This indicates strong performance consistency between the seen and unseen test conditions.

The paper is titled "Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning" and introduces Embodied Planner-R1, a framework that integrates outcome-driven reinforcement learning with LLMs for interactive planning. The framework achieved this high performance through pure reinforcement learning with group rollout, incorporating in-environment interaction through parallel exploration, completion-driven sparse reward, and Interactive Policy Optimization (IPO) for efficient learning from grouped trajectories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6819fa9-c6f4-4b2d-9f55-d291de076352",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "ab2d01e2-fe44-4b40-8ed4-24962c1d2511",
  "sourceToolAssistantUUID": "b6819fa9-c6f4-4b2d-9f55-d291de076352",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T19:26:30.745Z_

<details><summary>↩ Tool result · `toolu_01UPsbZVKS9VxAE3VFaQxNC6`</summary>

```text
Web search results for query: "AgentTrek DigiRL WebAgent-R1 Mind2Web reinforcement learning results"

Links: [{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"[2505.16421] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2505.16421"},{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi-Turn","url":"https://arxiv.org/pdf/2505.16421"},{"title":"[Literature Review] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://www.themoonlight.io/en/review/webagent-r1-training-web-agents-via-end-to-end-multi-turn-reinforcement-learning"},{"title":"Paper page - WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2505.16421"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=KqrYTALRjH"},{"title":"[Quick Review] AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://liner.com/review/agenttrek-agent-trajectory-synthesis-via-guiding-replay-with-web-tutorials"},{"title":"WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis","url":"https://arxiv.org/html/2507.04370"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2505.16421"},{"title":"AgentTrek: Agent Trajectory synthesis","url":"https://openreview.net/pdf/e95d923ccea15b1bab268aeeb8b3845547e3dafe.pdf"}]

Based on the search results, here's a summary of the key reinforcement learning results related to these methods:

## WebAgent-R1 Results

WebAgent-R1 boosted the task success rate of Qwen-2.5-3B from 6.1% to 33.9% and Llama-3.1-8B from 8.5% to 44.8% on the WebArena-Lite benchmark. Applying RL on top of the SFT-trained policy led to additional substantial gains (e.g., further boosting Qwen2.5-3B from 20% to 33.9%). While prior RL solutions for web agents, such as DigiRL and WebRL, have also shown performance gains, WebAgent-R1's method achieves even stronger results, highlighting the effectiveness of its end-to-end multi-turn RL framework.

## AgentTrek Results

The Qwen2-VL model trained with both AgentTrek and Mind2Web data achieved the highest cross-domain step success rate of 52.6%. On the Multimodal-Mind2Web benchmark specifically, the Qwen2-VL model fine-tuned with AgentTrek data achieved a cross-domain step success rate of 42.1%.

## Relationship to Mind2Web

The search results indicate that researchers adopted WebArena as the web environment over other simulated or static environments such as WebShop or Mind2Web for greater practicality, though Mind2Web is referenced as a complementary benchmark for evaluating web agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1410616f-9eaa-40eb-9520-c86328d7b3df",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "bf6c68bf-0a80-4fc2-8089-d08705bb5bd4",
  "sourceToolAssistantUUID": "1410616f-9eaa-40eb-9520-c86328d7b3df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T19:26:33.699Z_

<details><summary>↩ Tool result · `toolu_01CRusGKueCCkzDE2D282Gcy`</summary>

```text
Web search results for query: "Mind2Web offline benchmark element accuracy step success rate 2025 2026 fine-tuned 7B agent results table"

Links: [{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"GitHub - OSU-NLP-Group/Online-Mind2Web: An Illusion of Progress? Assessing the Current State of Web Agents · GitHub","url":"https://github.com/OSU-NLP-Group/Online-Mind2Web"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://ukgovernmentbeis.github.io/inspect_evals/evals/assistants/mind2web/"},{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v3"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Mind2Web: Towards a Generalist Agent for the Web [Quick Review]","url":"https://liner.com/review/mind2web-towards-a-generalist-agent-for-the-web"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://osu-nlp-group.github.io/Mind2Web-2/"},{"title":"Introducing ScribeAgent, setting a new bar for performance on web-navigation benchmarks | Scribe","url":"https://scribehow.com/library/scribe-agent"},{"title":"How we built the best browser agent with Auto-Research","url":"https://browser-use.com/posts/online-mind2web-benchmark"}]

The search results provide relevant information about Mind2Web benchmarks and various agent evaluations. However, I haven't found a specific results table with the exact metrics you're looking for (element accuracy, step success rate for fine-tuned 7B agents). Let me search more specifically for recent results tables.

Links: [{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"GitHub - OSU-NLP-Group/Online-Mind2Web: An Illusion of Progress? Assessing the Current State of Web Agents · GitHub","url":"https://github.com/OSU-NLP-Group/Online-Mind2Web"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://osu-nlp-group.github.io/Mind2Web-2/"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents","url":"https://arxiv.org/html/2504.01382v4"},{"title":"HAL: Online Mind2Web Leaderboard","url":"https://hal.cs.princeton.edu/online_mind2web"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"arXiv:2502.11357v2 [cs.AI] 19 Feb 2025","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/03/explorer_arxiv.pdf"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents | OpenReview","url":"https://openreview.net/forum?id=6jZi4HSs6o"},{"title":"osunlp/Online-Mind2Web · Datasets at Hugging Face","url":"https://huggingface.co/datasets/osunlp/Online-Mind2Web"}]

Based on my search results, I found relevant information about Mind2Web benchmark evaluations and fine-tuned models. Here's what I found:

## Key Findings:

**Fine-tuned 7B Model Results:**
A fine-tuned WebJudge-7B model has been released for use as a robust and reliable reward model for reinforcement learning.

**Element Accuracy and Step Success Rate:**
From the original Mind2Web paper, Flan-T5XL achieves element accuracy of 55.1% and step success rate of 52.0% in the cross-task setting, and 42.0% element accuracy and 38.9% step success rate in the cross-website setting.

**Recent 7B Model Performance:**
For more recent fine-tuned models around size 7B, Qwen2-VL-7B improves from 14.5% to 19.3% on the Mind2Web-Live benchmark after fine-tuning.

**Online Benchmark Developments:**
Online-Mind2Web was accepted to COLM 2025, and fine-tuned WebJudge-7B weights are available on Hugging Face.

Unfortunately, I could not locate a comprehensive results table specifically containing all the exact metrics you requested (element accuracy, step success rate for fine-tuned 7B agents) with 2025-2026 data in a single table format. The most detailed historical results appear to be from the original Mind2Web paper using Flan-T5 models, while more recent results focus on different evaluation frameworks like Online-Mind2Web. You may want to check the respective GitHub repositories or papers directly for the most current results tables.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2ab686c-573d-47e9-ad70-e567c596e6f2",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "580306aa-21ce-4bdc-bfbe-07a1e9824077",
  "sourceToolAssistantUUID": "a2ab686c-573d-47e9-ad70-e567c596e6f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-10T19:26:37.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXuh6L6XAxWqi8s52qMPbc`</summary>

```json
{
  "query": "\"Mind2Web\" \"element accuracy\" \"step success\" cross-task cross-website cross-domain SOTA table 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "580306aa-21ce-4bdc-bfbe-07a1e9824077",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSMp6sia27JnpEmBd2Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f08e9744-babd-4662-a840-4b914aa55d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLdUGADA1vzZyvfyHzVC4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 972,
      "cache_creation_input_tokens": 2518,
      "cache_read_input_tokens": 28836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2518,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-10T19:26:37.988Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AWzEjpK2HHRk1ZVPAEXe1A`</summary>

```json
{
  "query": "Mano Mind2Web results element accuracy step success 7B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f08e9744-babd-4662-a840-4b914aa55d17",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSMp6sia27JnpEmBd2Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a306dda8-ca3a-418e-b9cf-9f228000aee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLdUGADA1vzZyvfyHzVC4Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 972,
      "cache_creation_input_tokens": 2518,
      "cache_read_input_tokens": 28836,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 972,
          "output_tokens": 130,
          "cache_read_input_tokens": 28836,
          "cache_creation_input_tokens": 2518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2518,
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

_source line 55 · 2026-05-10T19:26:43.339Z_

<details><summary>↩ Tool result · `toolu_01AWzEjpK2HHRk1ZVPAEXe1A`</summary>

```text
Web search results for query: "Mano Mind2Web results element accuracy step success 7B"

Links: [{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v1"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"GitHub - OSU-NLP-Group/Online-Mind2Web: An Illusion of Progress? Assessing the Current State of Web Agents · GitHub","url":"https://github.com/OSU-NLP-Group/Online-Mind2Web"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"Success rate on Mind2Web cross-task, cross-website, and cross-domain... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-on-Mind2Web-cross-task-cross-website-and-cross-domain-generalization-test_tbl4_383951232"},{"title":"Online-Mind2Web Leaderboard - a Hugging Face Space by osunlp","url":"https://huggingface.co/spaces/osunlp/Online_Mind2Web_Leaderboard"},{"title":"ScribeAgent: Towards Specialized Web Agents Using Production-Scale Workflow Data","url":"https://arxiv.org/html/2411.15004"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"HAL: Online Mind2Web Leaderboard","url":"https://hal.cs.princeton.edu/online_mind2web"},{"title":"[PDF] Mind2Web: Towards a Generalist Agent for the Web | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mind2Web:-Towards-a-Generalist-Agent-for-the-Web-Deng-Gu/58f8925a8b87054ad0635a6398a7fe24935b1604"}]

Based on the search results, I found relevant information about Mano and its Mind2Web performance:

Mano-7B is a model developed through a three-stage training methodology built upon UI-TARS-1.5-7B, encompassing SFT, offline RL, and online RL.

Rigorous empirical evaluations conducted on the Mind2Web benchmark demonstrate Mano's superiority in multiple key performance metrics, with Mano setting new state-of-the-art standards in success rate, element precision, and stepwise completion.

The Mind2Web benchmark primarily evaluates the accuracy of web-based operations, covering over 100 websites, 1,000+ operation trajectories, and 7,000+ actions, with 3 testing protocols for comprehensive assessment.

The search results confirm that Mano-7B achieved strong performance on Mind2Web with improvements in element accuracy (element precision), step success rate (stepwise completion), and overall task success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a306dda8-ca3a-418e-b9cf-9f228000aee4",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "0d0feccd-aa31-4551-8a5a-9f3e3a466fb4",
  "sourceToolAssistantUUID": "a306dda8-ca3a-418e-b9cf-9f228000aee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T19:26:45.951Z_

<details><summary>↩ Tool result · `toolu_01CXuh6L6XAxWqi8s52qMPbc`</summary>

```text
Web search results for query: ""Mind2Web" "element accuracy" "step success" cross-task cross-website cross-domain SOTA table 2024 2025"

Links: [{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Success rate on Mind2Web cross-task, cross-website, and cross-domain... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-on-Mind2Web-cross-task-cross-website-and-cross-domain-generalization-test_tbl4_383951232"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"SOTA Offline Action Prediction on Mind2Web Cross-Domain v1.0 (test) and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/offline-action-prediction-on-mind2web-cross-domain-v1-0-test"},{"title":"From Grounding to Planning: Benchmarking Bottlenecks in Web Agents","url":"https://arxiv.org/html/2409.01927v1"},{"title":"osunlp/Mind2Web · Datasets at Hugging Face","url":"https://huggingface.co/datasets/osunlp/Mind2Web"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://ukgovernmentbeis.github.io/inspect_evals/evals/assistants/mind2web/"},{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v3"},{"title":"TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision","url":"https://arxiv.org/html/2403.06221v1"}]

I found relevant information about Mind2Web and the metrics you're asking about. Here's what I found:

## Overview of Mind2Web

Mind2Web is a dataset for developing and evaluating generalist agents for the web that can follow language instructions to complete complex tasks on any website. Mind2Web contains 2,350 tasks spanning 137 websites.

## Evaluation Metrics

EA (element accuracy) is short for element accuracy and AF1 is short for action F1. Evaluation of Offline Action Prediction performance is measured by Element Accuracy (Ele. Acc), Operation F1 (Op. F1), and Step Success Rate (Step SR).

## Generalization Testing

The dataset tests different levels of generalization abilities: Cross Task Generalization (generalization across tasks in the same environment), Cross Website Generalization (generalization across websites under the same domain), and Cross Domain Generalization (generalization across tasks and environments).

## Recent SOTA Results

Recent papers have reported state-of-the-art improvements on Mind2Web:

- Mano sets new state-of-the-art standards in success rate, element precision, and stepwise completion.

- TRAD improves element accuracy, step SR, and SR remarkably over the powerful Synapse agent by 2.1%, 1.4%, and 0.5%.

The search results include references to 2024-2025 benchmarking results, with the most recent being from October 2025 showing Mano's performance on Mind2Web.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f08e9744-babd-4662-a840-4b914aa55d17",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "fa3e760a-5024-474d-83ad-eb57fd78eb56",
  "sourceToolAssistantUUID": "f08e9744-babd-4662-a840-4b914aa55d17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-10T19:26:48.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JTkMR4rVindeeHkFowuwM6`</summary>

```json
{
  "query": "Mano arxiv 2509.17336 Mind2Web cross-task element accuracy 73 step success numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa3e760a-5024-474d-83ad-eb57fd78eb56",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSNiU5NpLgc63MUhjvs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e92aca5d-6d33-43c6-a167-aee628220af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1oDUZN8feVaWsVvDTX5T2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 2054,
      "cache_read_input_tokens": 31354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2054,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 51,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-10T19:26:49.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018MKyFPJ6Ef47ZcQzm3Pugi`</summary>

```json
{
  "query": "ScribeAgent Mind2Web element accuracy cross-domain step success rate results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e92aca5d-6d33-43c6-a167-aee628220af4",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSNiU5NpLgc63MUhjvs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "847622bb-3250-4d8f-9889-41fe80b17fec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1oDUZN8feVaWsVvDTX5T2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 838,
      "cache_creation_input_tokens": 2054,
      "cache_read_input_tokens": 31354,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 838,
          "output_tokens": 126,
          "cache_read_input_tokens": 31354,
          "cache_creation_input_tokens": 2054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2054,
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

_source line 59 · 2026-05-10T19:26:55.172Z_

<details><summary>↩ Tool result · `toolu_01JTkMR4rVindeeHkFowuwM6`</summary>

```text
Web search results for query: "Mano arxiv 2509.17336 Mind2Web cross-task element accuracy 73 step success numbers"

Links: [{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v1"},{"title":"[2509.17336] Mano Technical Report","url":"https://arxiv.org/abs/2509.17336"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://arxiv.org/html/2306.06070v3"},{"title":"Dual-View Visual Contextualization for Web Navigation","url":"https://arxiv.org/html/2402.04476v1"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"MIND2WEB: Towards a Generalist Agent for the Web Xiang Deng∗ Yu Gu Boyuan Zheng","url":"https://arxiv.org/pdf/2306.06070"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | OpenReview","url":"https://openreview.net/forum?id=kiYqbO3wqw"},{"title":"Success rate on Mind2Web cross-task, cross-website, and cross-domain... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-on-Mind2Web-cross-task-cross-website-and-cross-domain-generalization-test_tbl4_383951232"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"osunlp/Mind2Web · Datasets at Hugging Face","url":"https://huggingface.co/datasets/osunlp/Mind2Web"}]

Based on the search results, I found information about the Mano paper (arxiv 2509.17336) and its evaluation on the Mind2Web benchmark:

The official evaluation metrics for Mind2Web include element accuracy (Ele.Acc), operation F1 score (Op.F1), and step success rate (Step SR). The evaluation of multi-modal Mind2Web consists of 3 protocols: cross-task, which measures generalization across tasks within the same environment; cross-website, which evaluates generalization across websites within the same domain; and cross-domain, which assesses generalization across different tasks and environments.

The DeepMiner-Mano-7B model was compared against state-of-the-art methods on the Mind2Web test set, with results demonstrating significant improvements in operation accuracy compared to existing approaches. Rigorous empirical evaluations on Mind2Web demonstrate Mano's superiority in multiple key performance metrics, in particular setting new state-of-the-art standards in success rate, element precision, and stepwise completion.

However, the search results do not contain the specific numerical values you mentioned (73% for cross-task element accuracy or the exact step success rate numbers). To find those specific performance metrics, you may need to consult the full technical report directly at arxiv.org/html/2509.17336v1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e92aca5d-6d33-43c6-a167-aee628220af4",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "839bf821-2397-494e-bf6a-505b29189fe7",
  "sourceToolAssistantUUID": "e92aca5d-6d33-43c6-a167-aee628220af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-10T19:26:56.107Z_

<details><summary>↩ Tool result · `toolu_018MKyFPJ6Ef47ZcQzm3Pugi`</summary>

```text
Web search results for query: "ScribeAgent Mind2Web element accuracy cross-domain step success rate results"

Links: [{"title":"Introducing ScribeAgent, setting a new bar for performance on web-navigation benchmarks | Scribe","url":"https://scribehow.com/library/scribe-agent"},{"title":"SCRIBEAGENT: TOWARDS SPECIALIZED WEB AGENTS","url":"https://arxiv.org/pdf/2411.15004"},{"title":"ScribeAgent: Fine-Tuning Open-Source LLMs for Enhanced Web Navigation – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2024/12/06/scribeagent-fine-tuning-open-source-llms-for-enhanced-web-navigation/"},{"title":"ScribeAgent: Towards Specialized Web Agents Using Production-Scale Workflow Data","url":"https://arxiv.org/html/2411.15004"},{"title":"ScribeAgent: State-of-the-Art Web Navigation Performance","url":"https://scribe.com/library/scribe-agent"},{"title":"Success rate on Mind2Web cross-task, cross-website, and cross-domain... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-on-Mind2Web-cross-task-cross-website-and-cross-domain-generalization-test_tbl4_383951232"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v3"},{"title":"GitHub - colonylabs/ScribeAgent: Code for ScribeAgent paper","url":"https://github.com/colonylabs/ScribeAgent"}]

Based on the search results, here are the key findings on ScribeAgent's performance on Mind2Web with focus on element accuracy, cross-domain generalization, and step success rate:

## Element Accuracy and Step Success Rate

Performance is measured by element accuracy, which checks if the correct target is selected; action F1 score, which measures operation correctness like text input; step success rate, which evaluates whether both the target element and the operation are correct.

## State-of-the-Art Results on Mind2Web

ScribeAgent-Small and ScribeAgent-Large achieve state-of-the-art performance on Mind2Web and substantially improve the baseline from the WebArena benchmark with a 53% task success rate, surpassing previous best results by 7.3 percentage points (considering text-only baselines).

## Cross-Domain Performance

ScribeAgent-Large's element accuracy and step success rate metrics are also competitive with the best-fine-tuned baseline, HTML-T5-XL, on cross-website and cross-domain tasks.

The 32B-parameter ScribeAgent-Large achieves state-of-the-art direct generation performance on Mind2Web, with step success rate surpassing the baselines by 5-10% across all test sets.

## Zero-Shot Generalization

ScribeAgent did not fine-tune on the Mind2Web training data for evaluation as zero-shot, and for multi-stage evaluation, ScribeAgent-Large achieves the best overall zero-shot performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "847622bb-3250-4d8f-9889-41fe80b17fec",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "723336dd-6f84-4115-82dc-55430d1ce720",
  "sourceToolAssistantUUID": "847622bb-3250-4d8f-9889-41fe80b17fec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-10T19:26:59.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017m7tcuPeVDpUw21ZSN5miM`</summary>

```json
{
  "query": "Mind2Web offline action prediction cross-domain element accuracy 75 80 best result wizwand SOTA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "723336dd-6f84-4115-82dc-55430d1ce720",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSPTtkYmNHvrG7PULzC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2ac411a-9da0-4313-b94a-70852cf08a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeTGpMkHLNZ8SDupyoJhTK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2738,
      "cache_read_input_tokens": 33408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2738,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-10T19:27:00.804Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BcMPBFX5b9EMs4UiwMMJNj`</summary>

```json
{
  "query": "ALFWorld benchmark newer than HiPER Embodied-Planner-R1 2026 success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2ac411a-9da0-4313-b94a-70852cf08a9a",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSPTtkYmNHvrG7PULzC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9d2f1e1b-ab09-43c8-8ad0-0f6c7b741381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeTGpMkHLNZ8SDupyoJhTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2738,
      "cache_read_input_tokens": 33408,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2738
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 33408,
          "cache_creation_input_tokens": 2738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2738,
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

_source line 63 · 2026-05-10T19:27:05.597Z_

<details><summary>↩ Tool result · `toolu_01BcMPBFX5b9EMs4UiwMMJNj`</summary>

```text
Web search results for query: "ALFWorld benchmark newer than HiPER Embodied-Planner-R1 2026 success rate"

Links: [{"title":"Unleashing Embodied Task Planning Ability in LLMs via ...","url":"https://arxiv.org/pdf/2506.23127"},{"title":"ALFWorld: Textual and Embodied Agent Benchmark","url":"https://www.emergentmind.com/topics/alfworld"},{"title":"agentquest/agentquest/benchmarks/alfworld/README.md at main · nec-research/agentquest","url":"https://github.com/nec-research/agentquest/blob/main/agentquest/benchmarks/alfworld/README.md"},{"title":"ALFWorld Benchmark","url":"https://www.emergentmind.com/topics/alfworld-benchmark"},{"title":"Under review as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.09577"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"A collection of benchmarks for emboided robotic agent based on LLMs | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/a-collection-of-benchmarks-for-emboided-robotic-agent-based-on-llms-40482ecef189"},{"title":"ALFWORLD: ALIGNING TEXT AND EMBODIED ...","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | OpenReview","url":"https://openreview.net/forum?id=0IOX0YcCdTn"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"}]

Based on the search results, I found relevant information about ALFWorld benchmark performance:

Embodied Planner-R1 achieves a completion rate of 97.78% on ALFWorld, which appears to be a 2026 model based on the paper publication information.

For comparison, RESIM achieves a strong performance on ALFWorld with 87.7% success, which is mentioned in a paper under review for ICLR 2026.

So to answer your query: the HiPER Embodied-Planner-R1 model achieves a 97.78% success rate on the ALFWorld benchmark, making it one of the highest-performing models evaluated on this benchmark. There are other recent models like RESIM (87.7%) showing strong but lower performance, indicating that Embodied Planner-R1 represents a significant advance in this area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d2f1e1b-ab09-43c8-8ad0-0f6c7b741381",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "94ecb4e8-9b48-40d1-a34c-a86f497785d8",
  "sourceToolAssistantUUID": "9d2f1e1b-ab09-43c8-8ad0-0f6c7b741381",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-10T19:27:06.783Z_

<details><summary>↩ Tool result · `toolu_017m7tcuPeVDpUw21ZSN5miM`</summary>

```text
Web search results for query: "Mind2Web offline action prediction cross-domain element accuracy 75 80 best result wizwand SOTA"

Links: [{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"SOTA Offline Action Prediction on Mind2Web Cross-Domain v1.0 (test) and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/offline-action-prediction-on-mind2web-cross-domain-v1-0-test"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://arxiv.org/html/2306.06070v3"},{"title":"Mind2Web: Towards a Generalist Agent for the Web [Quick Review]","url":"https://liner.com/review/mind2web-towards-a-generalist-agent-for-the-web"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://ukgovernmentbeis.github.io/inspect_evals/evals/assistants/mind2web/"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | OpenReview","url":"https://openreview.net/forum?id=kiYqbO3wqw"},{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336"},{"title":"Success rate on Mind2Web cross-task, cross-website, and cross-domain... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rate-on-Mind2Web-cross-task-cross-website-and-cross-domain-generalization-test_tbl4_383951232"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"}]

Based on the web search results, I found information about offline action prediction on Mind2Web's cross-domain evaluation:

Evaluation of Offline Action Prediction performance on the test split of the Mind2Web Cross-Domain v1.0 dataset is measured by Element Accuracy (Element Acc), Operation F1 (Op. F1), and Step Success Rate (Step SR).

The Wizwand platform hosts a leaderboard for this specific task. HTML-T5-XL is listed among the methods evaluated, with the results updated about 1 month ago.

Regarding the specific accuracy ranges you mentioned (75-80%), I found that Flan-T5XL achieves 55.1% Element Accuracy in the Cross-Task setting and 42.0% Element Accuracy in the Cross-Website setting, which falls below the 75-80% range you asked about. More recent models may have achieved higher accuracy, though the search results didn't reveal specific results in that higher range.

The Wizwand leaderboard at the link found (https://www.wizwand.com/sota/offline-action-prediction-on-mind2web-cross-domain-v1-0-test) appears to be the primary source for state-of-the-art (SOTA) results on this specific benchmark, where you can find the latest comparative results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2ac411a-9da0-4313-b94a-70852cf08a9a",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "6555ba77-3458-4da2-8feb-55ed7f42d592",
  "sourceToolAssistantUUID": "c2ac411a-9da0-4313-b94a-70852cf08a9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-10T19:27:09.309Z_

Let me try to fetch the Wizwand page and the actual paper pages for concrete Mind2Web numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6555ba77-3458-4da2-8feb-55ed7f42d592",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSQFYPMWQZnBi3EA6AQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24d0b7f9-0340-403b-a881-0acac1e901ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3fNCzUFfyjgwuMUqqbq9j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 36146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-10T19:27:10.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KMfhuPRcwQZk8UzVxyUknZ`</summary>

```json
{
  "query": "site:wizwand.com Mind2Web cross-domain SOTA element accuracy step success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24d0b7f9-0340-403b-a881-0acac1e901ad",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSQFYPMWQZnBi3EA6AQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b05eaa8-b3b0-486a-bc06-c3849ee77c48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3fNCzUFfyjgwuMUqqbq9j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 36146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1143,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-10T19:27:11.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H4YL68pwEVfLyGNkWjjAFj`</summary>

```json
{
  "query": "Mind2Web cross-task element accuracy 73.6 72 step success 68 ScribeAgent Mano AgentTrek"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b05eaa8-b3b0-486a-bc06-c3849ee77c48",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSQFYPMWQZnBi3EA6AQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fd0f5ce-5b8a-4a6e-844e-3cec6cac109e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3fNCzUFfyjgwuMUqqbq9j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 734,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 36146,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1143
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 734,
          "output_tokens": 158,
          "cache_read_input_tokens": 36146,
          "cache_creation_input_tokens": 1143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1143,
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

_source line 68 · 2026-05-10T19:27:14.208Z_

<details><summary>↩ Tool result · `toolu_01KMfhuPRcwQZk8UzVxyUknZ`</summary>

```text
Web search results for query: "site:wizwand.com Mind2Web cross-domain SOTA element accuracy step success"

Links: [{"title":"SOTA Offline Action Prediction on Mind2Web Cross-Domain v1.0 (test) and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/offline-action-prediction-on-mind2web-cross-domain-v1-0-test"},{"title":"Discover AI/ML SOTA papers with code and benchmarks - Wizwand","url":"https://www.wizwand.com/"},{"title":"SOTA Binary Classification (Human vs Machine speech) on Inner In-Domain (test) and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/binary-classification-human-vs-machine-speech-on-inner-in-domain-test"},{"title":"SOTA benchmarks on Ogbn-arxiv and PapersWithCode | Wizwand","url":"https://www.wizwand.com/dataset/ogbn-arxiv"},{"title":"SOTA Information Retrieval on LoTTE Forum and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/information-retrieval-on-lotte-forum"},{"title":"SOTA Image Classification on ImageNet (Top-1 Accuracy) and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/image-classification-on-imagenet-top-1-accuracy"},{"title":"SOTA Visual Question Answering on RealworldQA and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/visual-question-answering-on-realworldqa"},{"title":"SOTA Action Recognition on NTU RGB+D (Cross-subject) and PapersWithCode | Wizwand","url":"https://www.wizwand.com/sota/action-recognition-on-ntu-rgb-plus-d-cross-subject"},{"title":"SOTA benchmarks on benchmark and PapersWithCode | Wizwand","url":"https://www.wizwand.com/dataset/benchmark"},{"title":"Discover AI/ML SOTA papers with code and benchmarks","url":"https://www.wizwand.com/paper/view/68fa78dc1e209131cea7add9"}]

I found the search results for your query. The first result points to a Wizwand page that evaluates Offline Action Prediction performance on the Mind2Web Cross-Domain v1.0 test dataset, measured by Element Accuracy, Operation F1, and Step Success Rate. 

The specific page is located at: https://www.wizwand.com/sota/offline-action-prediction-on-mind2web-cross-domain-v1-0-test

This appears to be a SOTA (State of the Art) benchmark page on Wizwand that tracks performance metrics for models performing offline action prediction on the Mind2Web cross-domain dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b05eaa8-b3b0-486a-bc06-c3849ee77c48",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "340ac622-0834-4ba5-9a9a-957403a41e22",
  "sourceToolAssistantUUID": "8b05eaa8-b3b0-486a-bc06-c3849ee77c48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-10T19:27:26.137Z_

<details><summary>↩ Tool result · `toolu_01H4YL68pwEVfLyGNkWjjAFj`</summary>

```text
Web search results for query: "Mind2Web cross-task element accuracy 73.6 72 step success 68 ScribeAgent Mano AgentTrek"

Links: [{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Introducing ScribeAgent, setting a new bar for performance on web-navigation benchmarks | Scribe","url":"https://scribehow.com/library/scribe-agent"},{"title":"osunlp/Mind2Web · Datasets at Hugging Face","url":"https://huggingface.co/datasets/osunlp/Mind2Web"},{"title":"Mind2Web: Towards a Generalist Agent for the Web | OpenReview","url":"https://openreview.net/forum?id=kiYqbO3wqw"},{"title":"MIND2WEB: Towards a Generalist Agent for the Web Xiang Deng∗ Yu Gu Boyuan Zheng","url":"https://arxiv.org/pdf/2306.06070"},{"title":"SCRIBEAGENT: TOWARDS SPECIALIZED WEB AGENTS","url":"https://arxiv.org/pdf/2411.15004"},{"title":"ScribeAgent: Fine-Tuning Open-Source LLMs for Enhanced Web Navigation – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2024/12/06/scribeagent-fine-tuning-open-source-llms-for-enhanced-web-navigation/"},{"title":"ScribeAgent: Towards Specialized Web Agents Using Production-Scale Workflow Data","url":"https://arxiv.org/html/2411.15004v2"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"}]

I found relevant search results about Mind2Web and ScribeAgent. Let me search for more specific information about the other agents mentioned (Mano and AgentTrek) to provide you with comprehensive results.

Links: [{"title":"AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://agenttrek.github.io/"},{"title":"[2412.09605] AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://arxiv.org/abs/2412.09605"},{"title":"[Quick Review] AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://liner.com/review/agenttrek-agent-trajectory-synthesis-via-guiding-replay-with-web-tutorials"},{"title":"GitHub - xlang-ai/AgentTrek: [ICLR2025 Spotlight] Agent Trajectory Synthesis via Guiding Replay with Web Tutorials · GitHub","url":"https://github.com/xlang-ai/AgentTrek"},{"title":"AgentTrek: Agent Trajectory synthesis","url":"https://openreview.net/pdf/e95d923ccea15b1bab268aeeb8b3845547e3dafe.pdf"},{"title":"AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials | OpenReview","url":"https://openreview.net/forum?id=EEgYUccwsV"},{"title":"Paper page - AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://huggingface.co/papers/2412.09605"},{"title":"(PDF) AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://www.researchgate.net/publication/387053624_AgentTrek_Agent_Trajectory_Synthesis_via_Guiding_Replay_with_Web_Tutorials"},{"title":"[Literature Review] AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials","url":"https://www.themoonlight.io/en/review/agenttrek-agent-trajectory-synthesis-via-guiding-replay-with-web-tutorials"},{"title":"AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241209605X/abstract"}]

Now let me search for specific performance metrics including "Mano" which appears to be another agent mentioned in your query.

Links: [{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://osu-nlp-group.github.io/Mind2Web-2/"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents | OpenReview","url":"https://openreview.net/forum?id=6jZi4HSs6o"},{"title":"How we built the best browser agent with Auto-Research","url":"https://browser-use.com/posts/online-mind2web-benchmark"},{"title":"Online-Mind2Web Benchmark","url":"https://www.emergentmind.com/topics/online-mind2web"},{"title":"MM-Mind2Web Leaderboard","url":"https://llm-stats.com/benchmarks/mm-mind2web"},{"title":"Promoting Sustainable Web Agents: Benchmarking and Estimating Energy Consumption Through Empirical and Theoretical Analysis","url":"https://arxiv.org/html/2511.04481v1"},{"title":"Evaluating AI Web Agents: Insights from the WebCanvas Benchmark | by iMean AI | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/evaluating-ai-web-agents-insights-from-the-mind2web-live-benchmark-e83f9e62c416"}]

Based on my web search results, I found information about the agents and benchmarks you mentioned. Here's what I discovered:

## Mind2Web Benchmark

Mind2Web is the first dataset for developing and evaluating generalist agents for the web that can follow language instructions to complete complex tasks on any website. With over 2,000 open-ended tasks collected from 137 websites spanning 31 domains and crowdsourced action sequences for the tasks, Mind2Web provides three necessary ingredients for building generalist web agents: 1. diverse domains, websites, and tasks, 2. use of real-world websites instead of simulated and simplified ones, and 3. a broad spectrum of user interaction patterns.

## ScribeAgent Performance

ScribeAgent models achieve state-of-the-art performance on Mind2Web and substantially improve the baseline from the WebArena benchmark with a 53% task success rate, surpassing previous best results by 7.3 percentage points (considering text-only baselines). On the Mind2Web benchmark, ScribeAgent-Large achieves best overall state-of-the-art zero shot performance in the multi-stage setting and is competitive with the best fine-tuned baseline.

## AgentTrek

AgentTrek is a scalable data synthesis pipeline that generates web agent trajectories by leveraging publicly available tutorials. On the Multimodal-Mind2Web benchmark, the Qwen2-VL model fine-tuned with AgentTrek data achieved strong performance across cross-task, cross-website, and cross-domain settings, with a cross-domain step success rate of 42.1%.

## Mano

DeepMiner-Mano-7B is compared against state-of-the-art methods based on both agent frameworks and agent models on the Mind2Web test set, with results demonstrating significant improvements in operation accuracy compared to state-of-the-art approaches.

The specific numeric metrics you mentioned (73.6, 72, 68, etc.) weren't visible in the search results I found. For detailed performance tables with those exact numbers, you may need to check the full research papers directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fd0f5ce-5b8a-4a6e-844e-3cec6cac109e",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "fe466022-0b3a-405b-bf75-e0e6d7fc9551",
  "sourceToolAssistantUUID": "6fd0f5ce-5b8a-4a6e-844e-3cec6cac109e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-10T19:27:28.892Z_

Let me try to fetch the actual paper pages for exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe466022-0b3a-405b-bf75-e0e6d7fc9551",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSRgNeWpAr1ASuBBsrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3007052-f4cf-4f7d-8a3c-a166c5b48b5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZdcRbf8pxtvqrn9zDvq3H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 37289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3867,
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

_source line 71 · 2026-05-10T19:27:29.535Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B8PuQeUc3qtCFVwS3XL6ex`</summary>

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
  "parentUuid": "c3007052-f4cf-4f7d-8a3c-a166c5b48b5f",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSRgNeWpAr1ASuBBsrd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89af8351-d49b-4e04-ba8f-5a6c215e8461",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZdcRbf8pxtvqrn9zDvq3H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3867,
      "cache_read_input_tokens": 37289,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 37289,
          "cache_creation_input_tokens": 3867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3867,
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

_source line 72 · 2026-05-10T19:27:29.539Z_

<details><summary>↩ Tool result · `toolu_01B8PuQeUc3qtCFVwS3XL6ex`</summary>

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
  "parentUuid": "89af8351-d49b-4e04-ba8f-5a6c215e8461",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "f5b667c5-d216-4ecb-b4ff-293539608f5c",
  "sourceToolAssistantUUID": "89af8351-d49b-4e04-ba8f-5a6c215e8461",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-10T19:27:32.236Z_



Let me fetch the actual paper pages to get concrete numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5b667c5-d216-4ecb-b4ff-293539608f5c",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSRw8AESKfBcsqJTa2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e750231-d4fc-48e8-9b2b-0af555d5234f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxoP8GEV3Woehndviv7mwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 41156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
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

_source line 74 · 2026-05-10T19:27:36.487Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018nnXgvK9cmyhVFQpuWKFiM`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.16165",
  "prompt": "Extract the exact performance numbers from the results tables. I need: 1) HiPER scores on ALFWorld (overall success rate) and WebShop (task score and success rate) for all model sizes (1.5B, 3B, 7B). 2) GiGPO baseline scores on ALFWorld and WebShop for comparison. 3) Any other baselines reported (GRPO, PPO, etc). Return all numbers in a table format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e750231-d4fc-48e8-9b2b-0af555d5234f",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSRw8AESKfBcsqJTa2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8b1ceab-0c8b-4ef0-867c-9895ffdb7b64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxoP8GEV3Woehndviv7mwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 41156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
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

_source line 75 · 2026-05-10T19:27:38.437Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XCjzAXWuYVMojMJ5Zytm5u`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.10978v3",
  "prompt": "Extract the exact performance numbers from the results tables for GiGPO on ALFWorld and WebShop. I need: 1) GiGPO scores with Qwen2.5-7B on ALFWorld (overall success rate %) and WebShop (task score %). 2) Comparison with GRPO, PPO, and other baselines. 3) All model sizes reported (1.5B, 3B, 7B). Return all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b1ceab-0c8b-4ef0-867c-9895ffdb7b64",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSRw8AESKfBcsqJTa2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b38c8f3f-cec8-467d-9945-1a05eac9e9a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxoP8GEV3Woehndviv7mwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 41156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
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

_source line 76 · 2026-05-10T19:27:40.847Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SuT9hwWmUtCMwWXtaBan7U`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.17336v3",
  "prompt": "Extract the exact performance numbers for Mano on the Mind2Web benchmark. I need element accuracy, operation F1, and step success rate for cross-task, cross-website, and cross-domain settings. Also extract the model size and any comparison baselines. Return all numbers in table format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b38c8f3f-cec8-467d-9945-1a05eac9e9a4",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSRw8AESKfBcsqJTa2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "003d7ea4-ba29-40bb-86a2-b15b2deaf442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxoP8GEV3Woehndviv7mwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 41156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
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

_source line 77 · 2026-05-10T19:27:42.360Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q2ef3zofMHseeW5Ee7GhuQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.08706v1",
  "prompt": "Extract the exact performance numbers from the results tables for ACT (Agentic Critical Training) on ALFWorld and WebShop. I need specific success rate percentages for all methods tested (IL, RL, IL+ACT, RL+ACT). Return all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "003d7ea4-ba29-40bb-86a2-b15b2deaf442",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSRw8AESKfBcsqJTa2a",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab5eb256-77bb-4bbb-8422-960de522d1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxoP8GEV3Woehndviv7mwP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 41156,
      "output_tokens": 630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 630,
          "cache_read_input_tokens": 41156,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 609,
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

_source line 78 · 2026-05-10T19:27:42.539Z_

<details><summary>↩ Tool result · `toolu_018nnXgvK9cmyhVFQpuWKFiM`</summary>

```text
# Performance Results from HiPER Paper

## ALFWorld Results (Overall Success Rate %)

| Model | HiPER | GiGPO | GRPO | PPO |
|-------|-------|-------|------|-----|
| Qwen2.5-1.5B | 95.3 ± 1.4 | 86.7 ± 1.7 | 71.1 ± 8.2 | 68.2 ± 1.8 |
| Qwen2.5-7B | 97.4 ± 1.6 | 90.8 ± 1.3 | 85.4 ± 2.0 | 82.8 ± 1.1 |

## WebShop Results

| Model | Metric | HiPER | GiGPO | GRPO | PPO |
|-------|--------|-------|-------|------|-----|
| Qwen2.5-1.5B | Task Score | 85.7 ± 3.2 | 83.5 ± 1.8 | 75.8 ± 3.5 | 73.8 ± 3.0 |
| Qwen2.5-1.5B | Success Rate (%) | 71.4 ± 9.0 | 67.4 ± 4.5 | 56.8 ± 3.8 | 51.5 ± 2.9 |
| Qwen2.5-7B | Task Score | 92.2 ± 0.3 | 86.2 ± 2.6 | 79.3 ± 2.8 | 81.4 ± 3.1 |
| Qwen2.5-7B | Success Rate (%) | 83.3 ± 0.9 | 75.2 ± 3.8 | 66.1 ± 3.7 | 68.7 ± 5.1 |

## Key Performance Gains

The document reports that "HiPER reaches 97.4% success on ALFWorld and 83.3% on WebShop with Qwen2.5-7B-Instruct (+6.6% and +8.3% over the best prior method)." Note: A 3B model size was not evaluated in the provided results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8b1ceab-0c8b-4ef0-867c-9895ffdb7b64",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "ba783f68-2bdc-472a-9304-26759355b536",
  "sourceToolAssistantUUID": "e8b1ceab-0c8b-4ef0-867c-9895ffdb7b64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-10T19:27:43.441Z_

<details><summary>↩ Tool result · `toolu_01XCjzAXWuYVMojMJ5Zytm5u`</summary>

```text
# GiGPO Performance Results

## ALFWorld (Overall Success Rate %)

**Qwen2.5-7B-Instruct:**
- GiGPO w/ std: 90.8±1.3%
- GiGPO w/o std: 90.2±2.3%
- GRPO: 77.6±5.2%
- PPO: 80.4±2.7%

**Qwen2.5-1.5B-Instruct:**
- GiGPO w/ std: 86.7±1.7%
- GiGPO w/o std: 86.1±4.7%
- GRPO: 72.8±3.6%
- PPO: 54.4±3.1%

## WebShop (Task Score)

**Qwen2.5-7B-Instruct:**
- GiGPO w/ std: 84.4±2.9
- GiGPO w/o std: 86.2±2.6
- GRPO: 79.3±2.8
- PPO: 81.4±3.1

**Qwen2.5-1.5B-Instruct:**
- GiGPO w/ std: 83.1±1.6
- GiGPO w/o std: 83.5±1.8
- GRPO: 75.8±3.5
- PPO: 73.8±3.0

## Key Performance Gains

"GiGPO injects fine-grained, step-level credit signals" achieving "performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO," all "without compromising the core strengths of group-based RL."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b38c8f3f-cec8-467d-9945-1a05eac9e9a4",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "56dc687d-985c-434b-a124-28fde3b79405",
  "sourceToolAssistantUUID": "b38c8f3f-cec8-467d-9945-1a05eac9e9a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-10T19:27:45.616Z_

<details><summary>↩ Tool result · `toolu_01SuT9hwWmUtCMwWXtaBan7U`</summary>

```text
# Mano Performance on Mind2Web Benchmark

| Metric | Cross-Task | Cross-Website | Cross-Domain |
|--------|-----------|---------------|--------------|
| **Element Accuracy** | 80.8 | 75.7 | 74.3 |
| **Operation F1** | 91.5 | 91.4 | 91.5 |
| **Step Success Rate** | 73.9 | 68.3 | 67.6 |

## Model Details
- **Model**: Mano-7B (7 billion parameters)
- **Base Model**: UITARS-1.5-7B, derived from Qwen2.5-VL-7B

## Key Comparison Baselines

| Model | Element Accuracy (Cross-Task) | Step Success Rate (Cross-Task) |
|-------|------------------------------|-------------------------------|
| UI-TARS-7B | 73.1 | 67.1 |
| UI-TARS-72B | 74.7 | 68.6 |
| **Mano-7B** | **80.8** | **73.9** |
| AutoWebGLM | — | 66.4 |
| Claude (computer-use) | 62.7 | 53.5 |

Mano-7B demonstrates "significant improvements in operation accuracy compared to SOTA approaches" through extensive online data augmentation for coordinate localization training and reinforcement learning enhancements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "003d7ea4-ba29-40bb-86a2-b15b2deaf442",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "62b8b952-0d6b-4fcd-96f5-0518d8833c85",
  "sourceToolAssistantUUID": "003d7ea4-ba29-40bb-86a2-b15b2deaf442",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-10T19:27:45.846Z_

<details><summary>↩ Tool result · `toolu_01Q2ef3zofMHseeW5Ee7GhuQ`</summary>

```text
# ACT Performance Results

Based on Table 1 from the paper, here are the exact success rate percentages:

## ALFWorld (In-Distribution)
- Imitation Learning: 85.71%
- Early Experience: 87.86%
- IL w/ ACT: 91.43%
- RL: 90.71%
- RL w/ ACT: 92.86%

## ALFWorld (Out-of-Distribution)
- Imitation Learning: 82.84%
- Early Experience: 85.82%
- IL w/ ACT: 87.31%
- RL: 84.33%
- RL w/ ACT: 88.06%

## WebShop
- Imitation Learning: 28.00%
- Early Experience: 31.00%
- IL w/ ACT: 31.60%
- RL: 29.40%
- RL w/ ACT: 33.80%

The results demonstrate that "adding ACT yields an average improvement of 5.07 percentage points over IL" and "4.62 percentage points over RL across all benchmarks."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab5eb256-77bb-4bbb-8422-960de522d1ee",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "962cd577-72ef-4471-a5a9-ad7c38500745",
  "sourceToolAssistantUUID": "ab5eb256-77bb-4bbb-8422-960de522d1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 82 · 2026-05-10T19:27:49.649Z_

Now let me get the Embodied-Planner-R1 details and check verl-agent's README for supported environments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "962cd577-72ef-4471-a5a9-ad7c38500745",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauST8Y35pWqmdZMEc5gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4917eaea-e642-455b-b5c4-387fa100db11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLu74znWNbGeN3etdyyJhe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2493,
      "cache_read_input_tokens": 41765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2493,
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

_source line 83 · 2026-05-10T19:27:52.005Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011BsxZ9gmdgqzCMxYueSEez`</summary>

```json
{
  "url": "https://github.com/langfengQ/verl-agent/blob/master/README.md",
  "prompt": "List all supported environments/benchmarks in verl-agent. Does it support Mind2Web? What environments are listed? Return the exact list of supported environments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4917eaea-e642-455b-b5c4-387fa100db11",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauST8Y35pWqmdZMEc5gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a05e97e-0111-4c54-9797-ba825b95bf74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLu74znWNbGeN3etdyyJhe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2493,
      "cache_read_input_tokens": 41765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2493,
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

_source line 84 · 2026-05-10T19:27:54.180Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015oRi6NBjYiacLLuHkyHSpC`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.23127",
  "prompt": "Extract the exact performance numbers for Embodied-Planner-R1 on ALFWorld. I need: overall success rate (97.78%), seen and unseen scores, model size, and comparison with baselines like ETO, ReAct, etc. What base model is used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a05e97e-0111-4c54-9797-ba825b95bf74",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauST8Y35pWqmdZMEc5gv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a21e9ce5-347d-405d-8929-fdec038f1387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLu74znWNbGeN3etdyyJhe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2493,
      "cache_read_input_tokens": 41765,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2493
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 41765,
          "cache_creation_input_tokens": 2493,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2493,
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

_source line 85 · 2026-05-10T19:27:55.921Z_

<details><summary>↩ Tool result · `toolu_011BsxZ9gmdgqzCMxYueSEez`</summary>

```text
# Supported Environments in verl-agent

Based on the README, here are the **supported environments**:

1. **ALFWorld** - Embodied AI tasks
2. **WebShop** - E-commerce interface control
3. **Search (Tool Calling)** - Search-R1 experiments
4. **Sokoban** - Visual puzzle game
5. **Gym Cards** - Card game environment
6. **AppWorld** - Digital interface control (experimental)

## Mind2Web Support

**No, Mind2Web is not supported.** The documentation lists only the six environments above under "Rich Suite of Environments" in the Key Features section.

The framework is designed for "multi-turn RL training" and explicitly mentions support for "reasoning agents in both visual and text-based tasks," but Mind2Web is not included in the supported benchmark list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a05e97e-0111-4c54-9797-ba825b95bf74",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "80d3e631-997e-4f05-a52c-627dc81d2fb8",
  "sourceToolAssistantUUID": "7a05e97e-0111-4c54-9797-ba825b95bf74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-10T19:27:58.504Z_

<details><summary>↩ Tool result · `toolu_015oRi6NBjYiacLLuHkyHSpC`</summary>

```text
# Embodied Planner-R1 Performance on ALFWorld

## Exact Performance Numbers

**Overall Performance:**
- "99.29% and 96.27% in seen and unseen scenarios, respectively, surpassing the previous best method ETO by 15.00% and 16.42%"

**Breakdown:**
- Seen tasks: 99.29%
- Unseen tasks: 96.27%
- Combined average: 97.78%

## Base Model

The system uses "Qwen2.5-7B-Instruct" as its foundation, a 7-billion parameter model fine-tuned with the reinforcement learning framework.

## Key Baseline Comparisons

The method substantially outperforms established approaches:

| Method | ALFWorld Average |
|--------|-----------------|
| ReAct (prompt-based) | ~31-40% |
| ETO (training baseline) | 82.07% |
| **Embodied Planner-R1** | **97.78%** |

The research emphasizes that trajectory-based baselines relying on human annotations "cluster around 80%" on ALFWorld, while Embodied Planner-R1 "easily surpasses this ceiling, achieving over 95%" through autonomous exploration with minimal supervision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a21e9ce5-347d-405d-8929-fdec038f1387",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a82ed4aeafe0578d0",
  "type": "user",
  "uuid": "43e76a08-751c-4386-a612-c45359771ba6",
  "sourceToolAssistantUUID": "a21e9ce5-347d-405d-8929-fdec038f1387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 87 · 2026-05-10T19:28:41.692Z_

Now I have all the data I need. Here is the comprehensive report:

---

## Benchmark SOTA Report (as of May 2026)

### 1. ALFWorld

**Your claimed SOTA numbers are still current.** The top two methods are:

| Method | Base Model | Overall Success Rate | Notes |
|---|---|---|---|
| **Embodied Planner-R1** | Qwen2.5-7B | **97.78%** (seen: 99.29%, unseen: 96.27%) | Pure RL with Interactive Policy Optimization; arxiv 2506.23127 |
| **HiPER** | Qwen2.5-7B | **97.4% +/- 1.6** | Hierarchical Plan-Execute RL; arxiv 2602.16165 |
| GiGPO | Qwen2.5-7B | 90.8% +/- 1.3 | Group-in-Group Policy Optimization; arxiv 2505.10978 |
| ACT (RL+ACT) | (not specified) | 92.86% (ID) / 88.06% (OOD) | Agentic Critical Training; arxiv 2603.08706 |
| SkillRL | - | 89.9% | Recursive Skill-Augmented RL; arxiv 2602.08234 |
| GRPO | Qwen2.5-7B | 85.4% +/- 2.0 | Baseline |
| PPO | Qwen2.5-7B | 82.8% +/- 1.1 | Baseline |

**Headroom assessment:** ALFWorld is nearly saturated. Embodied Planner-R1 at 97.78% and HiPER at 97.4% leave very little room (~2-3%) for improvement. The benchmark is approaching its ceiling for 7B models.

No newer methods surpassing these two were found in my search.

---

### 2. WebShop

**Your claimed SOTA is still current.** HiPER holds the top spot:

| Method | Base Model | Task Score | Success Rate |
|---|---|---|---|
| **HiPER** | Qwen2.5-7B | **92.2 +/- 0.3** | **83.3% +/- 0.9** |
| GiGPO | Qwen2.5-7B | 86.2 +/- 2.6 | 75.2% +/- 3.8 |
| PPO | Qwen2.5-7B | 81.4 +/- 3.1 | 68.7% +/- 5.1 |
| GRPO | Qwen2.5-7B | 79.3 +/- 2.8 | 66.1% +/- 3.7 |
| SkillRL | - | - | 72.7% |
| ACT (RL+ACT) | - | - | 33.8% (different eval setup) |

**Headroom assessment:** More headroom than ALFWorld. HiPER's 83.3% success rate leaves ~17% room for improvement. The task score of 92.2 is high but the gap between task score and success rate suggests agents often get close but fail to complete. No newer methods surpassing HiPER were found.

---

### 3. Mind2Web

Mind2Web uses a different evaluation paradigm (offline action prediction) with metrics: Element Accuracy, Operation F1, and Step Success Rate across three generalization splits. The best results for RL-trained 7B agents:

| Method | Size | Cross-Task Ele.Acc | Cross-Task Step SR | Cross-Website Ele.Acc | Cross-Website Step SR | Cross-Domain Ele.Acc | Cross-Domain Step SR |
|---|---|---|---|---|---|---|---|
| **Mano-7B** | 7B | **80.8** | **73.9** | **75.7** | **68.3** | **74.3** | **67.6** |
| UI-TARS-72B | 72B | 74.7 | 68.6 | - | - | - | - |
| UI-TARS-7B | 7B | 73.1 | 67.1 | - | - | - | - |
| Claude (computer-use) | - | 62.7 | 53.5 | - | - | - | - |
| AgentTrek + Qwen2-VL | 7B | - | - | - | - | - | 42.1 (MM-Mind2Web) |

**Mano-7B** (built on UI-TARS-1.5-7B / Qwen2.5-VL-7B) is the current SOTA at the 7B scale. It uses a 3-stage pipeline: SFT, offline RL, and online RL. Notably, the 7B Mano outperforms the 72B UI-TARS by ~5-6 points on cross-task metrics.

**Headroom assessment:** Significant headroom remains. Cross-domain Step SR at 67.6% means roughly 1 in 3 steps fail on unseen domains. This is substantially less saturated than ALFWorld/WebShop.

---

### 4. verl-agent / GiGPO and Mind2Web

**verl-agent does NOT support Mind2Web.** Its supported environments are:
- ALFWorld, WebShop, Search-R1, Sokoban, Gym Cards, AppWorld (experimental)

Mind2Web would require building a custom environment adapter. The challenge is that Mind2Web's original formulation is an offline benchmark (predicting actions from cached HTML), not a live interactive environment -- making it non-trivial to wrap as an RL environment. The newer Online-Mind2Web and Mind2Web-Live variants are interactive but use real websites, adding complexity.

**GRPO on Mind2Web:** WebAgent-R1 (arxiv 2505.16421) applied M-GRPO (Multi-turn GRPO) to web agent training, but evaluated on WebArena-Lite rather than Mind2Web directly. No paper was found applying GRPO specifically to Mind2Web's offline action prediction task.

---

### Summary of Headroom

| Benchmark | Current SOTA | Score | Headroom |
|---|---|---|---|
| ALFWorld | Embodied Planner-R1 | 97.78% | ~2% (near-saturated) |
| WebShop (success rate) | HiPER | 83.3% | ~17% (moderate) |
| Mind2Web (cross-domain Step SR) | Mano-7B | 67.6% | ~32% (substantial) |

Mind2Web has by far the most headroom and is the least explored with RL methods at the 7B scale.

Sources:
- [HiPER paper (arxiv 2602.16165)](https://arxiv.org/html/2602.16165)
- [GiGPO paper (arxiv 2505.10978)](https://arxiv.org/html/2505.10978v3)
- [Embodied Planner-R1 (arxiv 2506.23127)](https://arxiv.org/html/2506.23127)
- [ACT paper (arxiv 2603.08706)](https://arxiv.org/html/2603.08706v1)
- [SkillRL (arxiv 2602.08234)](https://arxiv.org/html/2602.08234)
- [Mano Technical Report (arxiv 2509.17336)](https://arxiv.org/html/2509.17336v3)
- [verl-agent GitHub](https://github.com/langfengQ/verl-agent)
- [WebAgent-R1 (arxiv 2505.16421)](https://arxiv.org/html/2505.16421v1)
- [AgentTrek (arxiv 2412.09605)](https://arxiv.org/abs/2412.09605)
- [ScribeAgent (arxiv 2411.15004)](https://arxiv.org/html/2411.15004v2)
- [Wizwand Mind2Web Leaderboard](https://www.wizwand.com/sota/offline-action-prediction-on-mind2web-cross-domain-v1-0-test)
- [Online Mind2Web Leaderboard (HAL)](https://hal.cs.princeton.edu/online_mind2web)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43e76a08-751c-4386-a612-c45359771ba6",
  "isSidechain": true,
  "agentId": "a82ed4aeafe0578d0",
  "requestId": "req_011CauSU4p5DzALp3Y938zkM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d8d4d5b-c0d8-4065-abc2-c079eeda30f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ESa4eyMJgwgotZingrg2Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 44258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 831,
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
