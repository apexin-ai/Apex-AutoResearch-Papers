# Research conversation: I need to check several things: 1. Search for "OpenAI retired SWE-bench Verified" to verify the exact wording OpenAI use

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac221add50251bcb4.jsonl`
- **Structured JSON:** [`c5bf8e9e3bf20db7fb40.json`](../../sessions/c5/c5bf8e9e3bf20db7fb40.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-10T19:18:23.761Z_

I need to check several things:

1. Search for "OpenAI retired SWE-bench Verified" to verify the exact wording OpenAI used - the reviewer says they "retired" not "deprecated" the benchmark. Find the actual announcement.

2. Search for the latest SWE-bench Pro results and leaderboard status. What's the current SOTA on SWE-bench Pro? Any reward model papers evaluated on it?

3. Search for any very recent (April-May 2026) papers on code repair reward models, process reward models for agents, or diagnostic reasoning evaluation that might be relevant. Try queries like:
   - "diagnostic reasoning reward model code 2026"
   - "process reward model software engineering agent 2026"
   - "stage-level credit assignment code repair"

Report all findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "c145217b-7d46-4279-952d-7918cb1de263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:18:23.766Z_

```json
{
  "parentUuid": "c145217b-7d46-4279-952d-7918cb1de263",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
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
  "uuid": "565c1156-b46e-461c-bbab-b675b96bc369",
  "timestamp": "2026-05-10T19:18:23.766Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:18:26.335Z_



I'll search for all three topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "565c1156-b46e-461c-bbab-b675b96bc369",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjhPJfcQEUfcEMApYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d26074c-9ee0-4bce-b518-2fa8d451f33f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwzgCxd4cKwgZuw4u5w6Uz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 8223,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 731,
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

_source line 4 · 2026-05-10T19:18:26.349Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QvDFxSEnogyGvemmgAKcmk`</summary>

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
  "parentUuid": "5d26074c-9ee0-4bce-b518-2fa8d451f33f",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjhPJfcQEUfcEMApYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46c30266-04b9-401f-ab8d-d1a355c5e44b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GwzgCxd4cKwgZuw4u5w6Uz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 8223,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 731,
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

_source line 5 · 2026-05-10T19:18:26.353Z_

<details><summary>↩ Tool result · `toolu_01QvDFxSEnogyGvemmgAKcmk`</summary>

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
  "parentUuid": "46c30266-04b9-401f-ab8d-d1a355c5e44b",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "7f9d006d-45b3-4860-ad11-479bc66934d7",
  "sourceToolAssistantUUID": "46c30266-04b9-401f-ab8d-d1a355c5e44b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:18:28.724Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f9d006d-45b3-4860-ad11-479bc66934d7",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjtgTREefzzkhjUxHw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90d4505f-d611-4447-bc5c-7b7128cfd645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014F5bU83xbKqmM8E24RiEEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 7 · 2026-05-10T19:18:29.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013oMQtFXBtw9eaj3DhnGUYJ`</summary>

```json
{
  "query": "OpenAI retired SWE-bench Verified announcement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90d4505f-d611-4447-bc5c-7b7128cfd645",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjtgTREefzzkhjUxHw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7079f4d0-0cf1-4669-bde6-1d099d52194f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014F5bU83xbKqmM8E24RiEEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 8 · 2026-05-10T19:18:30.884Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017KgcdNGopUgbttttJ23cwR`</summary>

```json
{
  "query": "SWE-bench Pro leaderboard results SOTA 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7079f4d0-0cf1-4669-bde6-1d099d52194f",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjtgTREefzzkhjUxHw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc06b44d-372a-4bcc-950f-a29baea692ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014F5bU83xbKqmM8E24RiEEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 9 · 2026-05-10T19:18:31.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbkAffoiWqhxRxSJhKz62J`</summary>

```json
{
  "query": "diagnostic reasoning reward model code 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc06b44d-372a-4bcc-950f-a29baea692ea",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjtgTREefzzkhjUxHw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a639672-cf79-4e94-ba33-961ab2c74b46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014F5bU83xbKqmM8E24RiEEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 10 · 2026-05-10T19:18:31.260Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbontyDLXHD8uXcWjL1zKx`</summary>

```json
{
  "query": "process reward model software engineering agent 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a639672-cf79-4e94-ba33-961ab2c74b46",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjtgTREefzzkhjUxHw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7a6e1a1-3705-4574-aa96-c1faa48bcdcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014F5bU83xbKqmM8E24RiEEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 11 · 2026-05-10T19:18:31.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AH9kVoXT5XcfvAfWQK3KVg`</summary>

```json
{
  "query": "stage-level credit assignment code repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7a6e1a1-3705-4574-aa96-c1faa48bcdcb",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRjtgTREefzzkhjUxHw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d19f0bcc-57a8-43dc-9c06-24d2ef1b357f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014F5bU83xbKqmM8E24RiEEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 8954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
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

_source line 12 · 2026-05-10T19:18:37.432Z_

<details><summary>↩ Tool result · `toolu_013oMQtFXBtw9eaj3DhnGUYJ`</summary>

```text
Web search results for query: "OpenAI retired SWE-bench Verified announcement 2025 2026"

Links: [{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data","url":"https://www.latent.space/p/swe-bench-dead"},{"title":"OpenAI Drops SWE-bench Verified: What It Means for AI","url":"https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/"},{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"},{"title":"Aibreakingwire","url":"https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"OpenAI Developers on X: \"The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we’re no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards. SWE-bench\" / X","url":"https://x.com/OpenAIDevs/status/2026002219909427270"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"OpenAI just killed SWE-Bench Verified, the benchmark it ...","url":"https://www.linkedin.com/posts/hackerrank_openai-just-killed-swe-bench-verified-the-activity-7432807590759264256-xzhQ"}]

Based on the search results, here's what I found about OpenAI's retirement of SWE-bench Verified:

## Announcement Summary

OpenAI announced on February 23, 2026 that it would stop evaluating against SWE-bench Verified, making this a recent development. OpenAI now recommends reporting SWE-bench Pro instead and shared details on why they're no longer reporting SWE-bench Verified.

## Reasons for Retirement

OpenAI identified two major issues with the benchmark:

1. **Flawed Test Cases**: OpenAI audited 27.6% of the dataset that models often failed to solve and found that at least 59.4% of the audited problems have flawed test cases that reject functionally correct submissions.

2. **Data Contamination**: Large frontier models can learn information from their training, and it is important that they are never trained on problems and solutions they are evaluated on. This means that improvements on SWE-bench Verified no longer reflect meaningful improvements in models' real-world software development abilities.

OpenAI's researchers stated that SWE-bench Verified "has become saturated and also highly contaminated," and that incremental score gains between frontier models had shrunk to 0.1% or less.

## Recommended Alternative

OpenAI explicitly endorses SWE-bench Pro, developed by Scale AI and released in September 2025, as the successor to SWE-bench Verified.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7079f4d0-0cf1-4669-bde6-1d099d52194f",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "f2713d3d-6cd3-4d8e-a62d-b6ff01658787",
  "sourceToolAssistantUUID": "7079f4d0-0cf1-4669-bde6-1d099d52194f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:18:37.659Z_

<details><summary>↩ Tool result · `toolu_017KgcdNGopUgbttttJ23cwR`</summary>

```text
Web search results for query: "SWE-bench Pro leaderboard results SOTA 2026"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-bench Pro Benchmark 2026: 30 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/swePro"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-Bench Pro Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-pro"},{"title":"SWE-Bench Pro - Public Benchmark Details | LLM Leaderboard | DataLearnerAI","url":"https://www.datalearner.com/en/benchmarks/swe-bench-pro"},{"title":"SWE-bench Leaderboard: AI Coding Agent SOTA Results | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/browse/agentic/swe-bench"}]

Based on the search results, here are the current SWE-bench Pro leaderboard results and SOTA (State-of-the-Art) for 2026:

## Current SOTA Leader

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Pro leaderboard with 77.8%, according to BenchLM.ai's latest data.

## Top Performing Models

Claude Mythos Preview leads at 77.8%, followed by Claude Opus 4.7 (Adaptive) at 64.3% and GPT-5.5 at 58.6%.

## Important Context

It's worth noting that there are different SWE-bench variants with significantly different difficulty levels:

- **SWE-bench Pro**: A large-scale benchmark containing 1865 total tasks across 41 professional repositories, with the Public Set containing 731 instances. SWE-bench Pro scores should be preferred where available, as many existing benchmarks have data contamination issues where models have likely seen the evaluation code during training.

- **SWE-bench Verified**: Much easier and more contaminated. For comparison, Claude Opus 4.5 scores 80.9% on SWE-bench Verified, but the same model on SWE-bench Pro using standardised scaffolding scores 45.9%.

The significant gap between Pro and Verified scores demonstrates why Pro is considered a more reliable measure of actual model capability on unseen code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc06b44d-372a-4bcc-950f-a29baea692ea",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "7c06528c-9990-46a2-a585-e6c10773f34c",
  "sourceToolAssistantUUID": "cc06b44d-372a-4bcc-950f-a29baea692ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:18:38.273Z_

<details><summary>↩ Tool result · `toolu_01WbontyDLXHD8uXcWjL1zKx`</summary>

```text
Web search results for query: "process reward model software engineering agent 2026"

Links: [{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"[2601.12294] ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://arxiv.org/abs/2601.12294"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/abs/10.1145/3774904.3792551"},{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Request PDF","url":"https://www.researchgate.net/publication/403735553_AgentPRM_Process_Reward_Models_for_LLM_Agents_via_Step-Wise_Promise_and_Progress"},{"title":"Exploring Reasoning Reward Model for Agents","url":"https://arxiv.org/html/2601.22154v2"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"[2506.11425] Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards","url":"https://arxiv.org/abs/2506.11425"},{"title":"Paper page - ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents","url":"https://huggingface.co/papers/2601.12294"}]

I found several relevant research papers and resources on process reward models for software engineering agents from 2026. Here's what the search returned:

## Key Research Areas

**Process Reward Models (PRMs) for Agents:**

Process reward models are being explored to evaluate each decision and guide the agent's decision-making process. Unlike LLM reasoning where steps are scored on correctness, actions in agent tasks should be evaluated based on their proximity to the goal and the progress they have made.

**Notable Papers in 2026:**

1. **AgentPRM**: This work employs a Temporal Difference-based estimation method combined with Generalized Advantage Estimation for training, demonstrating that AgentPRM is over 8× more compute-efficient than baselines.

2. **ToolPRMBench**: ToolPRMBench is a large-scale benchmark specifically designed to evaluate PRMs for tool-using agents, built on top of several representative tool-using benchmarks and converts agent trajectories into step-level test cases.

3. **Software Engineering Applications**: SWE-PRM validates that using proprietary models as PRMs can enhance the capabilities of agents in the field of software engineering.

4. **Agent-RLVR**: Agent-RLVR is a framework that makes Reinforcement Learning from Verifiable Rewards effective in challenging agentic settings, with an initial focus on software engineering tasks, introducing agent guidance to steer agents towards successful trajectories.

These resources represent significant developments in using reward models to improve agent performance in software engineering and other complex tasks during 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7a6e1a1-3705-4574-aa96-c1faa48bcdcb",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "edb69c13-f909-4c9d-b872-33c17200334d",
  "sourceToolAssistantUUID": "b7a6e1a1-3705-4574-aa96-c1faa48bcdcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:18:38.566Z_

<details><summary>↩ Tool result · `toolu_01MbkAffoiWqhxRxSJhKz62J`</summary>

```text
Web search results for query: "diagnostic reasoning reward model code 2026"

Links: [{"title":"Verifiable Process Reward Models for Structured Reasoning","url":"https://www.arxiv.org/pdf/2601.17223"},{"title":"Exploring Reasoning Reward Model for Agents","url":"https://arxiv.org/html/2601.22154v2"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"Top 10 Open-source Reasoning Models in 2026","url":"https://www.clarifai.com/blog/top-10-open-source-reasoning-models-in-2026"},{"title":"From Mathematical Reasoning to Code: Generalization of Process Reward Models in Test-Time Scaling | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40289"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"},{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"},{"title":"Nuanced clinical reasoning remains beyond the ken of frontier LLMs","url":"https://healthexec.com/topics/artificial-intelligence/nuanced-clinical-reasoning-remains-beyond-ken-frontier-llms"},{"title":"[2604.11626] RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time","url":"https://arxiv.org/abs/2604.11626"}]

Based on the search results, here are several recent developments related to diagnostic reasoning and reward models in 2026:

## Agent Reasoning Reward Models

Agent-RRM is a multi-faceted reasoning reward model designed to provide textual critiques and holistic reasoning-aware reward, producing structured feedback for agentic trajectories including an explicit reasoning trace, a focused critique that provides refinement guidance, and an overall score that evaluates process performance. Code, models, and datasets are all released to facilitate future research.

## Process Reward Models for Structured Reasoning

Verifiable process rewards evaluate both the final risk label and additionally verify each reasoning step and its associated label. Recent work demonstrates Process Reward Models (PRMs) have shown efficacy in addressing intermediate errors through structured feedback mechanisms, with studies analyzing PRMs from multiple perspectives including training methodologies, scalability, and generalization capabilities.

## Clinical and Diagnostic Reasoning

Regarding diagnostic reasoning specifically, the PrIME-LLM framework is a multidimensional metric designed to capture performance across the full arc of diagnostic and management tasks. The risk identified is that LLMs' reasoning is brittle precisely where uncertainty and nuance matter most.

## Other Reasoning Reward Innovations

Teaching reward models to produce explicit, multi-dimensional critiques before scoring transforms them into active optimization tools; researchers introduced Preference-Anchored Rationalization (PARROT), a framework that recovers high-quality rationales from readily available preference data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a639672-cf79-4e94-ba33-961ab2c74b46",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "0136d84a-9baf-4850-a5ed-1920d0d31d1d",
  "sourceToolAssistantUUID": "4a639672-cf79-4e94-ba33-961ab2c74b46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T19:18:39.912Z_

<details><summary>↩ Tool result · `toolu_01AH9kVoXT5XcfvAfWQK3KVg`</summary>

```text
Web search results for query: "stage-level credit assignment code repair"

Links: [{"title":"RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://arxiv.org/html/2604.11037"},{"title":"Step-Level Credit Assignment","url":"https://www.emergentmind.com/topics/step-level-credit-assignment"},{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2604.09459v1"},{"title":"DIY Credit Repair: 9-Step Action Plan for Rebuilding Your Score - Studocu","url":"https://www.studocu.com/en-us/document/meridian-university/history/diy-credit-repair-the-ultimate-action-plan/80621550"},{"title":"(PDF) RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://www.researchgate.net/publication/403791864_RTMC_Step-Level_Credit_Assignment_via_Rollout_Trees"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"What is SCED? - SCED Finder | Fast access to school codes","url":"https://nces.ed.gov/scedfinder/Home/Resources?AspxAutoDetectCookieSupport=1"},{"title":"Which NAICS codes get the most funding? Find out now | Nav - Nav","url":"https://www.nav.com/blog/naics-codes-funding-3032250/"},{"title":"Solving the Credit Assignment Problem in Machine Learning","url":"https://www.exgenex.com/article/credit-assignment-problem"},{"title":"ICLR Poster SSVPO: Effective Step-Level Credit Assignment for RL Training of Language Models","url":"https://iclr.cc/virtual/2026/poster/10008182"}]

Based on the search results, here's what I found about stage-level credit assignment in code repair:

## Overview

Stage-level credit assignment involves hierarchical frameworks where credit flows from coarse to fine across stages. For example, PilotRL extends this principle to a three-stage progressive framework: (1) plan-level RL, where credit is assigned to high-level plan components; (2) step-level RL, where credit is refined within each plan component; (3) token-level RL, where credit cascades to individual tokens. This cascaded approach is designed for agents that explicitly formulate plans before executing them (e.g., "step 1: search for relevant files; step 2: understand the codebase; step 3: implement the fix").

## Key Approaches for Code Repair

In code repair tasks, progressive refinement from episode-level through step-level credit assignment demonstrates additive gains, with each stage contributing between 1.4 and 2.2 percentage points.

Rollout-Tree MC is a critic-free advantage estimator that organizes group rollouts into a shared tree to enable step-level credit assignment for agentic RL, with experiments on SWE-bench Verified showing consistent gains over trajectory-level and step-level baselines.

## Why Stage-Level Assignment Matters

Step-level credit assignment is a method to localize outcome responsibility by assigning rewards to individual steps within a sequence, enhancing interpretability in sequential decision tasks. It employs neural temporal decomposition, LLM-based token reward mapping, and information-theoretic techniques to achieve precise, low-variance policy updates.

The stage-level approach is particularly important for code repair since agentic RL extends the paradigm to multi-turn interactive tasks where LLM agents use tools and write and debug code, which represents a qualitative leap in the complexity of the RL problem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d19f0bcc-57a8-43dc-9c06-24d2ef1b357f",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "4a506f8f-6b14-44cc-b74d-032b8c982174",
  "sourceToolAssistantUUID": "d19f0bcc-57a8-43dc-9c06-24d2ef1b357f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T19:18:42.397Z_

Let me get a few more targeted searches for additional detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a506f8f-6b14-44cc-b74d-032b8c982174",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRktRrGNHTVMj9Vz6zs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7807fd4-7e84-4e18-9fe8-f100ce8fb5e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrXzLNtw3ZgTXTSpJ77BH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 10358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4784,
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

_source line 18 · 2026-05-10T19:18:43.351Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018aaiMJKUNLA1TDre1y1hV6`</summary>

```json
{
  "query": "OpenAI \"why we no longer evaluate\" SWE-bench Verified retired deprecated wording"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7807fd4-7e84-4e18-9fe8-f100ce8fb5e5",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRktRrGNHTVMj9Vz6zs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2fd31b0-0a74-40b3-80d0-ca8f8a9a6d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrXzLNtw3ZgTXTSpJ77BH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 10358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4784,
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

_source line 19 · 2026-05-10T19:18:43.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01To7qmdNEVWKVR8UgXRfSvD`</summary>

```json
{
  "query": "SWE-bench Pro reward model evaluated results paper 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fd31b0-0a74-40b3-80d0-ca8f8a9a6d2b",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRktRrGNHTVMj9Vz6zs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a2f0355-c864-4a97-9ca5-67a811e9aaa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrXzLNtw3ZgTXTSpJ77BH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 10358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4784,
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

_source line 20 · 2026-05-10T19:18:44.510Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K8ie39usQ74uju8DMNP2z1`</summary>

```json
{
  "query": "AgentPRM SWE-bench code repair process reward model results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a2f0355-c864-4a97-9ca5-67a811e9aaa7",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRktRrGNHTVMj9Vz6zs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5b5ffef-c8df-4615-b281-3b385fe898f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrXzLNtw3ZgTXTSpJ77BH1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4784,
      "cache_read_input_tokens": 10358,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4784
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 10358,
          "cache_creation_input_tokens": 4784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4784,
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

_source line 21 · 2026-05-10T19:18:51.051Z_

<details><summary>↩ Tool result · `toolu_01To7qmdNEVWKVR8UgXRfSvD`</summary>

```text
Web search results for query: "SWE-bench Pro reward model evaluated results paper 2026"

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Pro Benchmark 2026: 30 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/swePro"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"}]

Based on the search results, I found information about SWE-bench Pro benchmarks and evaluations from 2026, though I didn't find a specific paper about a "reward model" for SWE-bench Pro. Here's what I found:

## SWE-bench Pro Leaderboard Results (2026)

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Pro leaderboard with 77.8%, followed by Claude Opus 4.7 (Adaptive) (64.3%) and GPT-5.5 (58.6%).

## About SWE-bench Pro

SWE-Bench Pro is a software engineering benchmark by Scale AI that evaluates AI coding agents on 1,865 long-horizon tasks from 41 real repositories across Python, Go, TypeScript, and JavaScript. Tasks require an average of 107 lines of changes across 4.1 files.

SWE-Bench Pro filters out trivial issues by design, with tasks typically requiring substantial multi-file changes, with an average of roughly 107 lines of code across just over four files.

The search results show current benchmark evaluations but don't contain a specific research paper about a "reward model" for SWE-bench Pro evaluated in 2026. If you're looking for a particular paper on this topic, you might want to search academic repositories like arXiv or check Scale AI's official publications directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a2f0355-c864-4a97-9ca5-67a811e9aaa7",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "578be845-1d76-4a5a-9f63-5acbae7c245a",
  "sourceToolAssistantUUID": "7a2f0355-c864-4a97-9ca5-67a811e9aaa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:18:51.640Z_

<details><summary>↩ Tool result · `toolu_018aaiMJKUNLA1TDre1y1hV6`</summary>

```text
Web search results for query: "OpenAI "why we no longer evaluate" SWE-bench Verified retired deprecated wording"

Links: [{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"},{"title":"OpenAI Developers on X: \"The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we’re no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards. SWE-bench\" / X","url":"https://x.com/OpenAIDevs/status/2026002219909427270"},{"title":"OpenAI o3 SWE-Bench Score: What Engineers Aren't Told","url":"https://neuralwired.com/2026/04/13/openai-o3-swe-bench-benchmark/"},{"title":"⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data","url":"https://www.latent.space/p/swe-bench-dead"},{"title":"OpenAI Drops SWE-bench Verified: What It Means for AI","url":"https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/"},{"title":"Aibreakingwire","url":"https://aibreakingwire.com/news/openai-ditches-swe-bench-verified-cites-critical-flaws"},{"title":"OpenAI Abandons SWE-bench Verified: 59% Flawed Tests | byteiota","url":"https://byteiota.com/openai-abandons-swe-bench-verified-59-flawed-tests/"},{"title":"Why we no longer evaluate SWE-bench Verified - DEV Community","url":"https://dev.to/jgnoncelogic/why-we-no-longer-evaluate-swe-bench-verified-59gc"},{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | daily.dev","url":"https://app.daily.dev/posts/why-swe-bench-verified-no-longer-measures-frontier-coding-capabilities-yitnqurmf"},{"title":"Why we no longer evaluate SWE-bench Verified - OpenAI News | Aetos.AI","url":"https://aetos.ai/posts/14417b93793f21d3"}]

Based on the search results, I found OpenAI's official explanation for why they no longer evaluate SWE-bench Verified. Here's what they found:

## Two Major Issues with SWE-bench Verified

OpenAI audited a 27.6% subset of the dataset that models often failed to solve and found that at least 59.4% of the audited problems have flawed test cases that reject functionally correct submissions.

More specifically, the flawed test cases included problems that were too narrowly defined (enforcing specific implementation details) or too wide (testing functionality not described in the problem).

## Training Data Contamination

OpenAI found that all frontier models tested were able to reproduce the original, human-written bug fix used as the ground-truth reference, meaning that improvements on SWE-bench Verified no longer reflect meaningful improvements in models' real-world software development abilities.

## The Official Recommendation

OpenAI has stopped reporting SWE-bench Verified scores and recommends that other model developers do so too. OpenAI recommends reporting results for SWE-bench Pro instead, while they work on building new, uncontaminated evaluations.

The official post that explains this in detail is titled "Why SWE-bench Verified no longer measures frontier coding capabilities" and was published by OpenAI on February 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2fd31b0-0a74-40b3-80d0-ca8f8a9a6d2b",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "c86d12e1-ce72-4ce7-bad9-dfbd00fee6cc",
  "sourceToolAssistantUUID": "a2fd31b0-0a74-40b3-80d0-ca8f8a9a6d2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:18:52.299Z_

<details><summary>↩ Tool result · `toolu_01K8ie39usQ74uju8DMNP2z1`</summary>

```text
Web search results for query: "AgentPRM SWE-bench code repair process reward model results"

Links: [{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"arXiv:2509.16941v2 [cs.SE] 14 Nov 2025 SWE-Bench Pro: Can AI Agents Solve","url":"https://arxiv.org/pdf/2509.16941"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs Shubham Gandhi∗","url":"https://arxiv.org/pdf/2509.02360"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"[2502.10325] Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/abs/2502.10325"},{"title":"[2511.08325] AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress","url":"https://arxiv.org/abs/2511.08325"},{"title":"Mini-SWE Agent: Lightweight Code Repair Agent","url":"https://www.emergentmind.com/topics/mini-swe-agent-27d26942-1f63-4337-bee8-576ebb1468c3"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Published as a conference paper at ICLR 2025 SWE-SEARCH: ENHANCING SOFTWARE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a1e6783e4d739196cad3336f12d402bf-Paper-Conference.pdf"}]

Based on the search results, here's information about AgentPRM and its application to SWE-bench code repair:

## AgentPRM Overview

AgentPRM (Agent Process Reward Models) is a simple and scalable framework for training LLM agents to continually improve through interactions. AgentPRM follows a lightweight actor-critic paradigm, using Monte Carlo rollouts to compute reward targets and optimize policies.

## Code Repair and Process Reward Models

There are two relevant AgentPRM approaches for code repair on SWE-bench:

**1. AgentPRM for General Agent Tasks:**
InversePRM outperforms SFT on expert demonstrations (86.6% vs. 63.4%), and compared to AgentPRM trained with 70K rollouts, InversePRM achieves a significantly higher success rate in iteration 1 (82.8% vs. 73.9%). However, this research evaluated on ALFWorld rather than SWE-bench.

**2. SWE-PRM (Course-Correcting Code Agents):**
A related approach specifically for SWE-bench shows stronger results: On SWE-bench Verified, closed-source PRMs improve resolution from 40.0% to 50.6% (+10.6 percentage points), with the largest gains on medium and hard tasks. A taxonomy-guided PRM improves resolution from 40.0% to 50.6% on SWE-bench Verified, including +10.7 points on medium and +4.4 points on hard tasks, with these gains coming with shorter or comparable trajectories, translating into more efficient runs.

## Key Design Features

The PRM design leverages a taxonomy of common inefficiencies and delivers lightweight, interpretable feedback without modifying the underlying policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5b5ffef-c8df-4615-b281-3b385fe898f8",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "44ce06cf-3a17-4ad9-b4fe-663cca8a918e",
  "sourceToolAssistantUUID": "a5b5ffef-c8df-4615-b281-3b385fe898f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T19:18:55.230Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q9BcRsvhNTRYDHmyAt6A7k`</summary>

```json
{
  "query": "RTMC rollout tree step-level credit assignment SWE-bench agentic RL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44ce06cf-3a17-4ad9-b4fe-663cca8a918e",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRmoViGs7x1o367gcaG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a045b0f-0f6e-49b2-9e04-399cd6a11347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173YWnNtpVj1V3RMmzcdNN8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3089,
      "cache_read_input_tokens": 15142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3089,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T19:18:55.761Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pjqwo6X7z6d49va2UdqzSr`</summary>

```json
{
  "query": "\"SWE-PRM\" OR \"course-correcting code agents\" process reward model SWE-bench 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a045b0f-0f6e-49b2-9e04-399cd6a11347",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRmoViGs7x1o367gcaG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7af9ffc-2c5a-4d0c-ab35-8af63fefcd6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0173YWnNtpVj1V3RMmzcdNN8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3089,
      "cache_read_input_tokens": 15142,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 15142,
          "cache_creation_input_tokens": 3089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3089,
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

_source line 26 · 2026-05-10T19:19:02.133Z_

<details><summary>↩ Tool result · `toolu_01Pjqwo6X7z6d49va2UdqzSr`</summary>

```text
Web search results for query: ""SWE-PRM" OR "course-correcting code agents" process reward model SWE-bench 2026"

Links: [{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/html/2509.02360"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs | OpenReview","url":"https://openreview.net/forum?id=wyrcoDNaGO"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs Shubham Gandhi∗","url":"https://arxiv.org/pdf/2509.02360"},{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/html/2604.14820"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250902360G/abstract"},{"title":"[2509.02360] When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/abs/2509.02360"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs for NeurIPS 2025 - IBM Research","url":"https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms"}]

Based on the search results, here's what I found about SWE-PRM and course-correcting code agents with process reward models:

## SWE-PRM Overview

SWE-PRM is an inference-time Process Reward Model (PRM) that intervenes during execution to detect and course-correct trajectory-level errors. The PRM design leverages a taxonomy of common inefficiencies and delivers lightweight, interpretable feedback without modifying the underlying policy.

## Key Results on SWE-bench

A taxonomy-guided PRM improves resolution from 40.0% to 50.6% on SWE-bench Verified, including +10.7 points on medium and +4.4 points on hard tasks. These gains come with shorter or comparable trajectories, translating into more efficient runs, with the additional spend amounting to roughly $0.2 per extra resolved instance.

## Related Work: SWE-Shepherd

The search also revealed related work called SWE-Shepherd, a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents, using trajectories from SWE-Bench to construct an action-level reward dataset.

## Problem Being Addressed

Long-horizon software engineering agents frequently accumulate trajectory-level inefficiencies, patterns of reasoning and action that may not yield immediate incorrectness but gradually erode efficiency and task success, and the approach operationalizes inefficiency categories during execution, enabling a Process Reward Model to deliver corrective natural language guidance in real time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7af9ffc-2c5a-4d0c-ab35-8af63fefcd6f",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "a8a571e3-18b2-4976-be7f-ea20e81275a1",
  "sourceToolAssistantUUID": "d7af9ffc-2c5a-4d0c-ab35-8af63fefcd6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T19:19:03.092Z_

<details><summary>↩ Tool result · `toolu_01Q9BcRsvhNTRYDHmyAt6A7k`</summary>

```text
Web search results for query: "RTMC rollout tree step-level credit assignment SWE-bench agentic RL 2026"

Links: [{"title":"[2604.11037] RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://arxiv.org/abs/2604.11037"},{"title":"RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://arxiv.org/html/2604.11037v1"},{"title":"(PDF) RTMC: Step-Level Credit Assignment via Rollout Trees","url":"https://www.researchgate.net/publication/403791864_RTMC_Step-Level_Credit_Assignment_via_Rollout_Trees"},{"title":"Xiaoxiao Xu's research works | Alibaba Group and other places","url":"https://www.researchgate.net/scientific-contributions/Xiaoxiao-Xu-2321074403"},{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2604.09459v1"},{"title":"AT2PO: Agentic Turn-based Policy Optimization via Tree Search","url":"https://arxiv.org/html/2601.04767v1"},{"title":"MICA: Multi-granularity Intertemporal Credit Assignment for Long-Horizon Emotional Support Dialogue","url":"https://arxiv.org/html/2603.06194v2"},{"title":"TSR: Trajectory‑Search Rollouts for Multi‑Turn RL of LLM Agents","url":"https://arxiv.org/html/2602.11767v1"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"MULTI-TURN RL OF LLM AGENTS","url":"https://openreview.net/pdf?id=ayVIbNrYiC"}]

Based on the search results, I found comprehensive information about RTMC and related research in agentic RL:

## RTMC: Step-Level Credit Assignment via Rollout Trees

RTMC (Rollout-Tree Monte Carlo) is an advantage estimation method that aggregates return statistics across rollouts sharing a common state to produce per-step Q-values and advantages without any learned critic.

### Problem It Addresses

Multi-step agentic reinforcement learning requires fine-grained credit assignment, as existing approaches offer limited options: critic-free methods like GRPO assign a uniform advantage to every action in a trajectory, while learned value networks introduce notable overhead and can be fragile under sparse rewards.

### Key Innovation

The approach observes that group rollouts targeting the same problem often traverse overlapping intermediate states, implicitly forming a tree whose branches diverge at successive decision points. A state-action signature system compresses raw interaction histories into compact, comparable representations, making cross-rollout state matching tractable.

### Performance Results

On SWE-bench Verified, RTMC improves pass@1 by 3.2 percentage points over GRPO. In a progressive ablation study, each component yields additive gains: episode-level GRPO improves over the baseline model, adding step-level rewards provides further improvement, and Rollout-Tree MC achieves the best performance through tree-based per-step advantage estimation.

### Related Research Context

RTMC is part of a broader wave of recent work (2025-2026) addressing credit assignment in agentic RL, with other notable methods like AT2PO and TSR using complementary tree-based approaches for multi-turn agent training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a045b0f-0f6e-49b2-9e04-399cd6a11347",
  "isSidechain": true,
  "promptId": "7827e6a5-674a-403b-b943-00c1d93406f1",
  "agentId": "ac221add50251bcb4",
  "type": "user",
  "uuid": "869b6994-c042-4c30-9f57-1d529e2f3d5f",
  "sourceToolAssistantUUID": "0a045b0f-0f6e-49b2-9e04-399cd6a11347",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T19:19:45.529Z_

Here are the consolidated findings across all three topics:

---

## 1. OpenAI's Retirement of SWE-bench Verified

OpenAI did **not** use the word "retired" or "deprecated" in their official announcement. Their blog post is titled **"Why SWE-bench Verified no longer measures frontier coding capabilities"** (published February 23, 2026). The phrasing they use is "we no longer evaluate" and "we're no longer reporting" SWE-bench Verified. Third-party coverage used stronger language -- "retired" (adwaitx.com), "drops" (adwaitx.com), "ditches" (aibreakingwire), "killed" (LinkedIn/HackerRank), "abandons" (byteiota) -- but OpenAI's own wording is more measured.

**Two reasons cited by OpenAI:**
- **Flawed test cases**: They audited 27.6% of the dataset (problems models often fail) and found at least 59.4% of audited problems have flawed tests that reject functionally correct submissions.
- **Data contamination**: All frontier models tested could reproduce the original human-written bug fix used as ground truth, meaning score improvements no longer reflect real capability gains.

OpenAI now recommends **SWE-bench Pro** as the replacement benchmark.

Sources:
- [Why SWE-bench Verified no longer measures frontier coding capabilities (OpenAI)](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- [The End of SWE-Bench Verified -- Latent Space podcast](https://www.latent.space/p/swe-bench-dead)
- [OpenAI Developers tweet](https://x.com/OpenAIDevs/status/2026002219909427270)

---

## 2. SWE-bench Pro Leaderboard & SOTA

**Current SOTA (as of May 2026):** Claude Mythos Preview at **77.8%** on SWE-bench Pro.

**Top entries:**
| Model | SWE-bench Pro Score |
|-------|-------------------|
| Claude Mythos Preview | 77.8% |
| Claude Opus 4.7 (Adaptive) | 64.3% |
| GPT-5.5 | 58.6% |

**About SWE-bench Pro:** Created by Scale AI (September 2025), it contains 1,865 tasks across 41 repositories in Python, Go, TypeScript, and JavaScript. Tasks average 107 lines of changes across 4.1 files. The gap vs. Verified is dramatic -- e.g., Claude Opus 4.5 scores 80.9% on Verified but only 45.9% on Pro with standardized scaffolding.

**Reward model papers evaluated on SWE-bench Pro:** I did not find a paper specifically reporting reward model results on the SWE-bench Pro benchmark. The PRM papers below mostly evaluate on SWE-bench Verified or the original SWE-bench.

Sources:
- [SWE-bench Pro Benchmark 2026 (BenchLM.ai)](https://benchlm.ai/benchmarks/swePro)
- [SWE-Bench Pro Leaderboard (Scale AI)](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [SWE-Bench Pro Leaderboard: Why 46% Beats 81% (MorphLLM)](https://www.morphllm.com/swe-bench-pro)

---

## 3. Recent Papers on Code Repair Reward Models, Process Reward Models for Agents, and Credit Assignment (April--May 2026)

### A. SWE-Shepherd (April 2026, arxiv 2604.10493)
A framework introducing PRMs for dense, step-level supervision of repository-level code agents. Uses SWE-bench trajectories to construct an action-level reward dataset. Directly relevant to code repair reward models.

### B. SWE-TRACE (April 2026, arxiv 2604.14820)
"Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models and Heuristic Test-Time Scaling." Introduces rubric-based PRMs for SWE agents -- a structured evaluation approach for long-horizon code repair.

### C. RTMC: Step-Level Credit Assignment via Rollout Trees (April 2026, arxiv 2604.11037)
A critic-free advantage estimator that organizes group rollouts into a shared tree for step-level credit assignment. On **SWE-bench Verified**, RTMC improves pass@1 by **+3.2 percentage points** over GRPO. Progressive ablation shows additive gains at each stage (episode-level -> step-level -> tree-based). This is the closest match to "stage-level credit assignment for code repair."

### D. "From Reasoning to Agentic: Credit Assignment in RL for LLMs" (April 2026, arxiv 2604.09459)
A survey/position paper covering the full landscape of credit assignment for agentic RL, including the PilotRL three-stage framework (plan-level -> step-level -> token-level RL) where each stage contributes 1.4--2.2 percentage points of improvement.

### E. AgentPRM (published at ACM Web Conference 2026)
Process Reward Models for LLM Agents via Step-Wise Promise and Progress. Uses Temporal Difference estimation with Generalized Advantage Estimation; 8x more compute-efficient than baselines. Originally evaluated on ALFWorld, not SWE-bench directly.

### F. Course-Correcting Code Agents with PRMs (NeurIPS 2025, IBM Research)
Taxonomy-guided inference-time PRM that improves SWE-bench Verified resolution from 40.0% to 50.6% (+10.6 pp), with largest gains on medium (+10.7) and hard (+4.4) tasks. Lightweight and interpretable -- does not modify the underlying policy.

### G. Agent-RLVR (arxiv 2506.11425)
"Training Software Engineering Agents via Guidance and Environment Rewards" -- a framework making RLVR effective in agentic settings, with initial focus on SWE tasks. Introduces agent guidance to steer agents toward successful trajectories.

Sources:
- [SWE-Shepherd (arxiv 2604.10493)](https://arxiv.org/abs/2604.10493)
- [SWE-TRACE (arxiv 2604.14820)](https://arxiv.org/html/2604.14820)
- [RTMC: Step-Level Credit Assignment via Rollout Trees (arxiv 2604.11037)](https://arxiv.org/abs/2604.11037)
- [From Reasoning to Agentic: Credit Assignment in RL for LLMs (arxiv 2604.09459)](https://arxiv.org/html/2604.09459v1)
- [AgentPRM (ACM Web Conference 2026)](https://dl.acm.org/doi/abs/10.1145/3774904.3792551)
- [Course-Correcting Code Agents with PRMs (arxiv 2509.02360)](https://arxiv.org/abs/2509.02360)
- [Agent-RLVR (arxiv 2506.11425)](https://arxiv.org/abs/2506.11425)
- [Awesome Process Reward Models (GitHub)](https://github.com/RyanLiu112/Awesome-Process-Reward-Models)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "869b6994-c042-4c30-9f57-1d529e2f3d5f",
  "isSidechain": true,
  "agentId": "ac221add50251bcb4",
  "requestId": "req_011CauRnbYehpZEqjkkzzsWQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e04bbaa-381a-4836-b78c-3824978db002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "537e596f-4db9-4a52-8eec-b93704ee0982",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HJads5JEv6ezUBsPEU4CAn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 1080,
      "cache_read_input_tokens": 18231,
      "output_tokens": 1842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1080
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 944,
          "output_tokens": 1842,
          "cache_read_input_tokens": 18231,
          "cache_creation_input_tokens": 1080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1080,
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
