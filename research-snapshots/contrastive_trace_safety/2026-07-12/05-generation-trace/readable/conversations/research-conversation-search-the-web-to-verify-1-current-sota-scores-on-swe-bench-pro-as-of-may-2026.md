# Research conversation: Search the web to verify: 1. Current SOTA scores on SWE-bench Pro (as of May 2026). The idea claims top systems score 42

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-addd1852ac844ebc4.jsonl`
- **Structured JSON:** [`0e3c458019faa38fdaa6.json`](../../sessions/0e/0e3c458019faa38fdaa6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-10T18:40:43.667Z_

Search the web to verify:
1. Current SOTA scores on SWE-bench Pro (as of May 2026). The idea claims top systems score 42-59%.
2. Current SOTA scores on SWE-bench Lite (the idea needs strong baselines here).
3. Whether Qwen3.6-27B exists as a model. If not, what is the correct name for Qwen's ~27B code model?
4. How long does SWE-bench evaluation typically take per instance? The idea claims ~9min/instance.
5. What is SWE-smith and is it publicly available with 128 repositories?

Use WebSearch to verify these. Be precise about what you find vs. what you cannot confirm.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "116a30e5-ea7d-4c25-bc5e-7801244c40d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T18:40:43.669Z_

```json
{
  "parentUuid": "116a30e5-ea7d-4c25-bc5e-7801244c40d6",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
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
  "uuid": "735b7306-3e38-460e-a1c6-7b8f6544e9ff",
  "timestamp": "2026-05-10T18:40:43.669Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T18:40:47.080Z_



I'll search for all five questions in parallel to gather the information efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "735b7306-3e38-460e-a1c6-7b8f6544e9ff",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNs6Zfy28wuKyn7AApn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d980a699-cc60-47d0-9354-f8f0f3e41304",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwGWx3xmzyjC9w21Lvqh34",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 713,
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

_source line 4 · 2026-05-10T18:40:47.592Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018UAWfH6STj9ZfsFKxwTdJZ`</summary>

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
  "parentUuid": "d980a699-cc60-47d0-9354-f8f0f3e41304",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNs6Zfy28wuKyn7AApn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d6c748f9-16d2-48c8-96dc-9a6ceb4aa6a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwGWx3xmzyjC9w21Lvqh34",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 8223,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 713,
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

_source line 5 · 2026-05-10T18:40:47.595Z_

<details><summary>↩ Tool result · `toolu_018UAWfH6STj9ZfsFKxwTdJZ`</summary>

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
  "parentUuid": "d6c748f9-16d2-48c8-96dc-9a6ceb4aa6a4",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "bbcf6c77-37f2-43a9-903e-d69f642b693d",
  "sourceToolAssistantUUID": "d6c748f9-16d2-48c8-96dc-9a6ceb4aa6a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T18:40:50.328Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbcf6c77-37f2-43a9-903e-d69f642b693d",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNsPn2C2c5rQsgFYJhh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1d7556b-403c-4e78-9729-94e49e737d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqpDY5FHDj8LET2iq7UYcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8936,
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

_source line 7 · 2026-05-10T18:40:50.729Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TtaXELLiVRBDpaPWeEHHV9`</summary>

```json
{
  "query": "SWE-bench Pro leaderboard SOTA scores 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1d7556b-403c-4e78-9729-94e49e737d26",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNsPn2C2c5rQsgFYJhh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0b81b17-cef5-408e-8cb2-44ddb3011dd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BqpDY5FHDj8LET2iq7UYcA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1409,
      "cache_read_input_tokens": 8936,
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

_source line 8 · 2026-05-10T18:40:57.225Z_

<details><summary>↩ Tool result · `toolu_01TtaXELLiVRBDpaPWeEHHV9`</summary>

```text
Web search results for query: "SWE-bench Pro leaderboard SOTA scores 2026"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-bench Leaderboard: AI Coding Agent SOTA Results | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/browse/agentic/swe-bench"},{"title":"SWE-Bench Pro - Public Benchmark Details | LLM Leaderboard | DataLearnerAI","url":"https://www.datalearner.com/en/benchmarks/swe-bench-pro"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"}]

Based on the search results, here are the current SWE-bench Pro leaderboard SOTA (state-of-the-art) scores for 2026:

## SWE-bench Pro Public Set

Claude Mythos Preview from Anthropic leads the SWE-bench Pro public set with a score of 77.80% (as of April 28, 2026).

## Alternative Scoring Approaches

It's important to note that scores vary significantly depending on the evaluation methodology:

**Standard Scaffolding (SEAL Leaderboard):** Claude Opus 4.5 scores 45.9% on the SEAL leaderboard with standardized scaffolding, the highest of any model, while GPT-5.3-Codex scores 57% on SWE-bench Pro according to OpenAI's published results.

**Custom Agent Scaffolding:** When paired with WarpGrep v2 as a search subagent, Opus 4.6 reaches 57.5% on Pro (internal benchmark by Morph).

## Important Context

Top models score around 23% on the SWE-bench Pro public set, compared to 70%+ on SWE-bench Verified, highlighting the significant difference in difficulty. All models use uncapped cost with 250-turn limit unless noted, and scores can vary substantially based on the agent scaffolding used.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0b81b17-cef5-408e-8cb2-44ddb3011dd7",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "53204ac8-361b-4966-a889-35e84b4de49b",
  "sourceToolAssistantUUID": "a0b81b17-cef5-408e-8cb2-44ddb3011dd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T18:41:00.739Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WvqUte4xpFYbNRxfg6XwNy`</summary>

```json
{
  "query": "SWE-bench Lite leaderboard SOTA scores 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53204ac8-361b-4966-a889-35e84b4de49b",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNt6VyfYEwgXs5EvPud",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0a7868f-cc66-4838-b804-92e43321cfdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXGeEMRWbg1ijQJf52h6kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 10345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T18:41:02.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6JRJYKUxxWcBh8KUUiZSR`</summary>

```json
{
  "query": "Qwen3.6-27B model does it exist Qwen 27B code model name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0a7868f-cc66-4838-b804-92e43321cfdb",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNt6VyfYEwgXs5EvPud",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "394a19dc-8bf7-45cb-b36c-664671397abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXGeEMRWbg1ijQJf52h6kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 10345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T18:41:02.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016qwoHB7aPuxBa6pnuDgXGY`</summary>

```json
{
  "query": "SWE-bench evaluation time per instance minutes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "394a19dc-8bf7-45cb-b36c-664671397abe",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNt6VyfYEwgXs5EvPud",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2fe59b0-af1d-44e7-81a8-6fbf8034c937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXGeEMRWbg1ijQJf52h6kj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 10345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 887,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T18:41:02.648Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BxDLe6x6TWP4rzyhoyAtQj`</summary>

```json
{
  "query": "SWE-smith benchmark 128 repositories publicly available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2fe59b0-af1d-44e7-81a8-6fbf8034c937",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNt6VyfYEwgXs5EvPud",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "869bdb47-75f1-4848-ab1e-d83b466ea179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXGeEMRWbg1ijQJf52h6kj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 887,
      "cache_read_input_tokens": 10345,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 887
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 10345,
          "cache_creation_input_tokens": 887,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 887,
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

_source line 13 · 2026-05-10T18:41:06.678Z_

<details><summary>↩ Tool result · `toolu_01N6JRJYKUxxWcBh8KUUiZSR`</summary>

```text
Web search results for query: "Qwen3.6-27B model does it exist Qwen 27B code model name"

Links: [{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model","url":"https://qwen.ai/blog?id=qwen3.6-27b"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"qwen/qwen3.6-27b • LM Studio","url":"https://lmstudio.ai/models/qwen/qwen3.6-27b"},{"title":"Qwen3.6 - How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3.6"},{"title":"batiai/qwen3.6-27b","url":"https://ollama.com/batiai/qwen3.6-27b"},{"title":"qwen3.6:27b","url":"https://ollama.com/library/qwen3.6:27b"},{"title":"Qwen/Qwen3.6-27B | vLLM Recipes","url":"https://recipes.vllm.ai/Qwen/Qwen3.6-27B"},{"title":"Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model | Hacker News","url":"https://news.ycombinator.com/item?id=47863217"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"DavidAU/Qwen3.6-27B-Heretic-Uncensored-FINETUNE-NEO-CODE-Di-IMatrix-MAX-GGUF · Hugging Face","url":"https://huggingface.co/DavidAU/Qwen3.6-27B-Heretic-Uncensored-FINETUNE-NEO-CODE-Di-IMatrix-MAX-GGUF"}]

Yes, Qwen3.6-27B is now available on Hugging Face Hub and ModelScope, released on April 22, 2026.

Qwen3.6-27B is the flagship dense model of the Qwen3.6 family. The model is positioned as "Flagship-Level Coding in a 27B Dense Model", and it uses the same gated delta networks hybrid attention as its MoE siblings, supports vision+text input, and natively serves 262K context.

The official model name/code is **Qwen/Qwen3.6-27B** and it's available on platforms like Hugging Face, Ollama, vLLM, and other inference frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "394a19dc-8bf7-45cb-b36c-664671397abe",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "68347682-16a1-46ec-b514-c23795251069",
  "sourceToolAssistantUUID": "394a19dc-8bf7-45cb-b36c-664671397abe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:41:07.232Z_

<details><summary>↩ Tool result · `toolu_01WvqUte4xpFYbNRxfg6XwNy`</summary>

```text
Web search results for query: "SWE-bench Lite leaderboard SOTA scores 2025 2026"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Lite Leaderboard 2026 - Compare AI Model Scores","url":"https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite"},{"title":"SWE-bench Leaderboard: AI Coding Agent SOTA Results | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/browse/agentic/swe-bench"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"}]

Based on the search results, here are the current SWE-bench Lite leaderboard SOTA scores as of May 2026:

## SWE-bench Lite Top Scores (May 2026)

Claude Opus 4.6 leads the SWE-bench Lite leaderboard with a score of 62.7. The top-scoring models include Claude Opus 4.6 at 62.7%, followed by MiniMax M2.5 at 56.3%.

Currently 62 models have been evaluated on SWE-bench Lite, with an average score of 26.8 and a standard deviation of 19.9.

It's worth noting that the best model scores 46% on Pro but 81% on Verified, because Verified is contaminated, indicating that different SWE-bench variants (Lite, Verified, Pro) have different difficulty levels and potential data contamination issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0a7868f-cc66-4838-b804-92e43321cfdb",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "a4a853f1-157a-40a9-809a-d954d3ac85c6",
  "sourceToolAssistantUUID": "b0a7868f-cc66-4838-b804-92e43321cfdb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:41:08.475Z_

<details><summary>↩ Tool result · `toolu_01BxDLe6x6TWP4rzyhoyAtQj`</summary>

```text
Web search results for query: "SWE-smith benchmark 128 repositories publicly available"

Links: [{"title":"SWE-smith: Scaling Data for Software Engineering Agents | OpenReview","url":"https://openreview.net/forum?id=63iVrXc8cC"},{"title":"NeurIPS Poster SWE-smith: Scaling Data for Software Engineering Agents","url":"https://neurips.cc/virtual/2025/poster/121828"},{"title":"GitHub - SWE-bench/SWE-smith: [NeurIPS 2025 D&B Spotlight] Scaling Data for SWE-agents · GitHub","url":"https://github.com/SWE-bench/SWE-smith"},{"title":"SWE-smith: Scaling Data for Software Engineering Agents","url":"https://arxiv.org/pdf/2504.21798"},{"title":"SWE-bench","url":"https://www.swebench.com/original.html"},{"title":"[2504.21798] SWE-smith: Scaling Data for Software Engineering Agents","url":"https://arxiv.org/abs/2504.21798"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-bench · GitHub","url":"https://github.com/swe-bench"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"}]

Based on the search results, here's what I found about the SWE-smith benchmark and its 128 repositories:

## SWE-smith Overview

SWE-smith creates a dataset of 50k instances sourced from 128 GitHub repositories, an order of magnitude larger than all previous works. SWE-smith is a novel pipeline for generating software engineering training data at scale that constructs execution environments and automatically synthesizes 100s to 1,000s of task instances that break existing test(s) in codebases.

## Public Availability

SWE-smith collection procedure, task instances, trajectories, and models are open sourced to lower the barrier of entry for research in LM systems for automated software engineering. All assets are available at https://swesmith.com.

## Key Statistics

SWE-smith was applied to 128 Python repositories, generating a total of 50k instances, with an average of 381 task instances per repository.

## Model Results

Using SWE-smith data, SWE-agent-LM-32B achieved 40.2% Pass@1 resolve rate on the SWE-bench Verified benchmark, state of the art among open source models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "869bdb47-75f1-4848-ab1e-d83b466ea179",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "f8db0676-ec76-4866-8646-970af0c29a48",
  "sourceToolAssistantUUID": "869bdb47-75f1-4848-ab1e-d83b466ea179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:41:08.849Z_

<details><summary>↩ Tool result · `toolu_016qwoHB7aPuxBa6pnuDgXGY`</summary>

```text
Web search results for query: "SWE-bench evaluation time per instance minutes"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Evaluation - SWE-bench","url":"https://www.swebench.com/SWE-bench/guides/evaluation/"},{"title":"How to run SWE-bench Verified in one hour on one machine | Epoch AI","url":"https://epoch.ai/blog/swebench-docker"},{"title":"What skills does SWE-bench Verified evaluate? | Epoch AI","url":"https://epoch.ai/blog/what-skills-does-swe-bench-verified-evaluate"},{"title":"How to scale agentic evaluation: lessons from 200,000 SWE-bench runs | AI21","url":"https://www.ai21.com/blog/scaling-agentic-evaluation-swe-bench/"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"SWE-bench Verified Explained: What the Coding Agent Leaderboard Actually Measures (and What It Misses) | Groundy","url":"https://groundy.com/articles/swe-bench-verified-explained-what-the-coding-agent-leaderboard-actually-measures-and-what-it-misses/"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"Cognition | SWE-bench technical report","url":"https://cognition.ai/blog/swe-bench-technical-report"}]

Based on the search results, here are the key findings regarding SWE-bench evaluation time per instance:

## Evaluation Time Per Instance

A lightweight variant averages 3.5 minutes per example, with run times varying between variants. For a typical variant, evaluation takes about 20 minutes for a full SWE-bench evaluation.

For individual instances, typical resource constraints per instance during evaluation include 45 minutes of wall-clock time, which serves as the maximum time limit for agent evaluations.

## Historical Context

It's worth noting that SWE-bench evaluation has become significantly more efficient over time. The All Hands team originally reported that it took them "several days" to run SWE-bench lite (300 examples), or over 10 minutes per sample. More recently, optimized Docker images have allowed running SWE-bench Verified in 62 minutes on a single GitHub actions VM with 32 cores and 128GB of RAM.

Human effort estimates suggest these are complex tasks: 39% of tasks were rated as "trivial changes" requiring less than 15 minutes, while 52% were rated "small changes" taking between 15 minutes and 1 hour by experienced software engineers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2fe59b0-af1d-44e7-81a8-6fbf8034c937",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "82575076-8b2f-45e8-8b67-8e2492462f1b",
  "sourceToolAssistantUUID": "f2fe59b0-af1d-44e7-81a8-6fbf8034c937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T18:41:12.352Z_

Let me get additional details on a couple of the more nuanced points.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82575076-8b2f-45e8-8b67-8e2492462f1b",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNtxDS2e4796rTYiTf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c49949a-878d-4d56-8cc2-0e0ae5970332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrKEtcEU5oLYg8MLTPzxhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 782,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 11232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2461,
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

_source line 18 · 2026-05-10T18:41:13.425Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MF8ykUmbvJNVoDRDrGznRt`</summary>

```json
{
  "query": "SWE-bench Pro scores range top systems 2026 leaderboard results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c49949a-878d-4d56-8cc2-0e0ae5970332",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNtxDS2e4796rTYiTf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc5c9b8c-dd92-4ed9-89d9-3df1fcfab826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrKEtcEU5oLYg8MLTPzxhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 782,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 11232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2461,
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

_source line 19 · 2026-05-10T18:41:13.859Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JseScokM2YBEV2KJcMBz1v`</summary>

```json
{
  "query": "SWE-bench Lite top scores best results 2026 leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc5c9b8c-dd92-4ed9-89d9-3df1fcfab826",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNtxDS2e4796rTYiTf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "358b3ffc-48f7-4543-bec9-01fa974195c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrKEtcEU5oLYg8MLTPzxhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 782,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 11232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2461,
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

_source line 20 · 2026-05-10T18:41:14.147Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UAHf9ygerfw3i5wqWB37mS`</summary>

```json
{
  "query": "SWE-bench average time per instance agent inference cost time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "358b3ffc-48f7-4543-bec9-01fa974195c9",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNtxDS2e4796rTYiTf9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b38269e-335f-4144-9051-4370af05af23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrKEtcEU5oLYg8MLTPzxhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 782,
      "cache_creation_input_tokens": 2461,
      "cache_read_input_tokens": 11232,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 782,
          "output_tokens": 184,
          "cache_read_input_tokens": 11232,
          "cache_creation_input_tokens": 2461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2461,
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

_source line 21 · 2026-05-10T18:41:20.116Z_

<details><summary>↩ Tool result · `toolu_01UAHf9ygerfw3i5wqWB37mS`</summary>

```text
Web search results for query: "SWE-bench average time per instance agent inference cost time"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints","url":"https://arxiv.org/html/2509.09853v1"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?","url":"https://arxiv.org/html/2410.03859v1"},{"title":"Benchmarking - SWE-agent documentation","url":"https://swe-agent.com/0.7/usage/benchmarking/"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"Competitive runs - SWE-agent documentation","url":"https://swe-agent.com/latest/usage/competitive_runs/"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"Inference - SWE-bench","url":"https://www.swebench.com/SWE-bench/reference/inference/"},{"title":"SWE Benchmark: LLM evaluation in Software Engineering Setting | by Sulbha Jain | Medium","url":"https://medium.com/@sulbha.jindal/swe-benchmark-llm-evaluation-in-software-engineering-setting-52f315b2de5a"}]

Based on the search results, I found relevant information about agent inference costs and time metrics on SWE-bench:

## Agent Inference Cost and Time Metrics

Agentless consumes an average of 83.1 API calls, 209.4 seconds of inference time, and 727.9 seconds of CPU time when evaluated on SWE-bench-Verified. This appears to be among the highest resource consumption metrics for the systems tested.

For cost metrics, Grok Code Fast 1 and gpt-oss-120b deliver around 29%–30% resolved rate for only $0.03–$0.04 per problem, making them ultra-efficient budget options. In contrast, the average per-problem cost for Claude Sonnet 4 dropped from $5.29 to just $0.91 when proper caching was implemented.

The time per instance varies significantly depending on the model and configuration used. The clearest performance differences appear among tasks that take between 15 minutes and 1 hour to complete.

These metrics demonstrate that agent inference costs and time on SWE-bench vary widely based on the agent framework, underlying model, and optimization strategies employed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b38269e-335f-4144-9051-4370af05af23",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "99c7c4bc-fbfa-4aa5-b889-01a32249a67b",
  "sourceToolAssistantUUID": "2b38269e-335f-4144-9051-4370af05af23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:41:20.964Z_

<details><summary>↩ Tool result · `toolu_01MF8ykUmbvJNVoDRDrGznRt`</summary>

```text
Web search results for query: "SWE-bench Pro scores range top systems 2026 leaderboard results"

Links: [{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Pro Benchmark 2026: 30 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/swePro"},{"title":"SWE-Bench Pro Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-pro"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"}]

Based on the search results, here's what the current SWE-bench Pro leaderboard shows for top systems in 2026:

## Top SWE-bench Pro Scores (2026)

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Pro leaderboard with 77.8%, followed by Claude Opus 4.7 (Adaptive) at 64.3% and GPT-5.5 at 58.6%.

## Score Range Context

The scores on SWE-bench Pro are notably lower than on other benchmarks due to the increased difficulty. Top models score around 23% on the SWE-bench Pro public set, compared to 70%+ on SWE-Bench Verified. This significant performance drop reflects that the benchmark contains complex, long-horizon tasks requiring edits across multiple files and repositories.

## Important Notes on Score Variations

It's worth noting that three different agent systems ran the same model (Opus 4.5), and their scores ranged from 50.2% to 55.4%, with that spread coming entirely from how the agent manages context and tool calls. This indicates that reported scores can vary based on the specific scaffolding and agent framework used in evaluation.

The leaderboard continues to be updated regularly, with Scale AI adding new model evaluations to the SEAL leaderboard as they become available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc5c9b8c-dd92-4ed9-89d9-3df1fcfab826",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "0f6ae9c2-dc88-4f16-a001-1569a3ef3f44",
  "sourceToolAssistantUUID": "cc5c9b8c-dd92-4ed9-89d9-3df1fcfab826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T18:41:22.098Z_

<details><summary>↩ Tool result · `toolu_01JseScokM2YBEV2KJcMBz1v`</summary>

```text
Web search results for query: "SWE-bench Lite top scores best results 2026 leaderboard"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Lite Leaderboard 2026 - Compare AI Model Scores","url":"https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"}]

Based on the search results, here's information about the top scores on the SWE-bench Lite leaderboard as of 2026:

## SWE-bench Lite Top Scores (2026)

As of May 9, 2026, the top-scoring model on SWE-bench Lite is Claude Opus 4.6 at 62.7%, followed by Claude Opus 4.6 at 62.7% and MiniMax M2.5 at 56.3%. 62 models have been evaluated on this benchmark.

It's worth noting that while SWE-bench Lite provides a baseline evaluation, there are other benchmark variants being used:

- **SWE-bench Verified**: As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Verified leaderboard with 93.9%, followed by Claude Opus 4.7 (Adaptive) (87.6%) and GPT-5.3 Codex (85%).

- **SWE-bench Pro**: Top models score around 23% on the SWE-Bench Pro public set, compared to 70%+ on SWE-Bench Verified. This more challenging benchmark is increasingly recommended by researchers for more realistic evaluations.

The significant performance gap between SWE-bench Verified and SWE-bench Pro reflects differences in task difficulty and data contamination concerns with the Verified benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "358b3ffc-48f7-4543-bec9-01fa974195c9",
  "isSidechain": true,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "agentId": "addd1852ac844ebc4",
  "type": "user",
  "uuid": "d82194a1-c3ad-4f4d-9d0f-f5374358e5a8",
  "sourceToolAssistantUUID": "358b3ffc-48f7-4543-bec9-01fa974195c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T18:42:04.121Z_

Here are the verified findings for all five questions:

---

## 1. SWE-bench Pro SOTA Scores

The claim of "42-59%" is **partially outdated/inaccurate as of May 2026**. The current leaderboard shows scores significantly higher than that range:

- **Claude Mythos Preview**: 77.8% (top score, as of April 28, 2026)
- **Claude Opus 4.7 (Adaptive)**: 64.3%
- **GPT-5.5**: 58.6%
- Three different agent systems running the same model (Opus 4.5) scored between 50.2% and 55.4%, showing that scaffolding matters significantly.

The 42-59% range may have been accurate at an earlier point, but the frontier has moved well past 59% by May 2026. On the standardized SEAL leaderboard with constrained scaffolding, scores are lower (e.g., Claude Opus 4.5 at 45.9%), so the range depends heavily on whether custom agent scaffolding is permitted.

## 2. SWE-bench Lite SOTA Scores

The top scores on SWE-bench Lite as of May 2026:

- **Claude Opus 4.6**: 62.7% (top score)
- **MiniMax M2.5**: 56.3%
- 62 models have been evaluated; average score is 26.8% with a standard deviation of 19.9%.

For context, SWE-bench Verified (a related but different benchmark) shows much higher scores, with Claude Mythos Preview at 93.9%. This suggests SWE-bench Lite is an intermediate difficulty level -- harder than Verified but easier than Pro.

## 3. Qwen3.6-27B Existence

**Confirmed: Qwen3.6-27B does exist.** It was released on April 22, 2026 by the Qwen team (Alibaba Group). The official model name is **Qwen/Qwen3.6-27B**, and it is available on Hugging Face, Ollama, vLLM, and other platforms. It is described as a "Flagship-Level Coding in a 27B Dense Model" that uses gated delta networks hybrid attention, supports vision+text input, and has a 262K context window. The GitHub repo is at `github.com/QwenLM/Qwen3.6`.

## 4. SWE-bench Evaluation Time per Instance

The claim of "~9 min/instance" is **roughly in the right ballpark but varies widely**:

- **Agentless** averages ~209 seconds (~3.5 min) of inference time and ~728 seconds (~12 min) of CPU time per instance on SWE-bench Verified.
- The All Hands team originally reported over 10 minutes per sample for SWE-bench Lite (300 examples took "several days").
- Optimized Docker setups can run full SWE-bench Verified (500 instances) in about 62 minutes on a beefy machine (~7.4 seconds per instance for just the test execution harness, not including agent inference).
- Per-instance wall-clock timeout is typically set at 45 minutes maximum.

The ~9 min/instance figure likely refers to total agent inference + evaluation time for a mid-tier system. This is plausible but highly variable depending on the model, agent framework, and hardware. Lightweight/agentless approaches can be faster (3-4 min), while complex agent systems can take much longer.

## 5. SWE-smith: Availability and 128 Repositories

**Confirmed: SWE-smith is publicly available and uses exactly 128 repositories.**

- SWE-smith is a data generation pipeline that creates task instances from open-source repositories. It was published as a NeurIPS 2025 Datasets & Benchmarks Spotlight paper.
- It generates **50,000 task instances** from **128 Python repositories** (average of 381 instances per repo).
- All assets (collection procedure, task instances, trajectories, and trained models) are open-sourced at [swesmith.com](https://swesmith.com) and on [GitHub](https://github.com/SWE-bench/SWE-smith).
- Using SWE-smith data, they trained **SWE-agent-LM-32B**, which achieved 40.2% on SWE-bench Verified -- state of the art among open-source models at the time of publication.

---

**Summary of claim accuracy:**

| Claim | Verdict |
|---|---|
| SWE-bench Pro top systems: 42-59% | Outdated -- frontier is now up to 77.8% with custom scaffolding, though ~42-58% may hold under standardized evaluation |
| SWE-bench Lite strong baselines needed | Valid -- top score is 62.7%, many strong baselines exist |
| Qwen3.6-27B exists | Confirmed -- released April 22, 2026 |
| ~9 min/instance evaluation time | Plausible but variable (3-12 min depending on setup) |
| SWE-smith publicly available with 128 repos | Confirmed -- 128 repos, 50K instances, fully open-sourced |

Sources:
- [SWE-bench Leaderboards](https://www.swebench.com/)
- [SWE-Bench Pro Leaderboard (Scale AI)](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81% (Morph)](https://www.morphllm.com/swe-bench-pro)
- [SWE-bench Lite Leaderboard 2026](https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite)
- [Qwen3.6-27B Blog Post](https://qwen.ai/blog?id=qwen3.6-27b)
- [Qwen/Qwen3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
- [How to run SWE-bench Verified in one hour (Epoch AI)](https://epoch.ai/blog/swebench-docker)
- [SWE-smith on GitHub](https://github.com/SWE-bench/SWE-smith)
- [SWE-smith paper (arXiv)](https://arxiv.org/abs/2504.21798)
- [SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness](https://arxiv.org/html/2509.09853v1)
- [SWE-bench Pro Benchmark 2026 (BenchLM)](https://benchlm.ai/benchmarks/swePro)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d82194a1-c3ad-4f4d-9d0f-f5374358e5a8",
  "isSidechain": true,
  "agentId": "addd1852ac844ebc4",
  "requestId": "req_011CauNuvr7Ese7DmkeTG8ZR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce95f257-b1f7-48f3-8319-5e074be1e10a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcREv6eEkPSiEUZSQHcoXi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 720,
      "cache_creation_input_tokens": 2650,
      "cache_read_input_tokens": 13693,
      "output_tokens": 1673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2650
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 720,
          "output_tokens": 1673,
          "cache_read_input_tokens": 13693,
          "cache_creation_input_tokens": 2650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2650,
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
