# Research conversation: Search for the latest status of SWE-bench Verified contamination and SWE-bench Pro. I need to verify: 1. Did OpenAI actu

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a2bffc47ff86f6aca.jsonl`
- **Structured JSON:** [`0c5880beb6e4433670cc.json`](../../sessions/0c/0c5880beb6e4433670cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-12T02:30:10.784Z_

Search for the latest status of SWE-bench Verified contamination and SWE-bench Pro. I need to verify:

1. Did OpenAI actually stop reporting SWE-bench Verified scores? When?
2. What is SWE-bench Pro? When was it introduced?
3. What are the latest scores on SWE-bench Verified vs Pro for frontier models?
4. Is the claim about "verbatim gold-patch reproduction" accurate?

Use WebSearch with queries:
- "SWE-bench Verified contamination OpenAI stopped reporting 2026"
- "SWE-bench Pro benchmark 2026"
- "SWE-bench contamination gold patch reproduction frontier models"
- "SWE-bench Verified vs Pro scores comparison"

Report exactly what you find — do NOT make up information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "2050977c-0681-4a70-aaee-ea34b30ce980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T02:30:10.789Z_

```json
{
  "parentUuid": "2050977c-0681-4a70-aaee-ea34b30ce980",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
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
  "uuid": "fb9afc51-6ec5-4880-9670-ede57955f145",
  "timestamp": "2026-05-12T02:30:10.789Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T02:30:13.649Z_



I'll search for the latest information on SWE-bench Verified contamination and SWE-bench Pro. Let me first load the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9afc51-6ec5-4880-9670-ede57955f145",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtULDp7mPRCUEwT1H2f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb3da1b6-f9cc-42f2-9bc6-096bda529038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j3SvFjqrEuN2M9A2jfpJS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 735,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T02:30:13.880Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XS1U5Grn52uJTgZSjLb6ds`</summary>

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
  "parentUuid": "eb3da1b6-f9cc-42f2-9bc6-096bda529038",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtULDp7mPRCUEwT1H2f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "345177ce-75c3-48be-9802-9e771aaef620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014j3SvFjqrEuN2M9A2jfpJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 735,
      "cache_read_input_tokens": 8223,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 735,
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

_source line 5 · 2026-05-12T02:30:13.883Z_

<details><summary>↩ Tool result · `toolu_01XS1U5Grn52uJTgZSjLb6ds`</summary>

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
  "parentUuid": "345177ce-75c3-48be-9802-9e771aaef620",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "7e1ed7a0-db18-4487-b33d-ee80c507babe",
  "sourceToolAssistantUUID": "345177ce-75c3-48be-9802-9e771aaef620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T02:30:16.201Z_



Now let me run all four search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e1ed7a0-db18-4487-b33d-ee80c507babe",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtUZdxPxE7BqobkFy1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7dc3b9d-bafa-4b48-93a6-c32885ad6b99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cCfS5iUrGRWTY2hie8tSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 8958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1429,
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

_source line 7 · 2026-05-12T02:30:17.188Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FSf6Qj8yq8KoGL7qja4TUR`</summary>

```json
{
  "query": "SWE-bench Verified contamination OpenAI stopped reporting 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7dc3b9d-bafa-4b48-93a6-c32885ad6b99",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtUZdxPxE7BqobkFy1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3d214d9-1d68-455f-b397-78f92aa26d7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cCfS5iUrGRWTY2hie8tSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 8958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1429,
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

_source line 8 · 2026-05-12T02:30:17.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QTTR49veqRQupQvExjGjje`</summary>

```json
{
  "query": "SWE-bench Pro benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3d214d9-1d68-455f-b397-78f92aa26d7a",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtUZdxPxE7BqobkFy1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f987f22-452e-4f35-b35a-2e202f830190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cCfS5iUrGRWTY2hie8tSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 8958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1429,
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

_source line 9 · 2026-05-12T02:30:18.211Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JMHwU1etdfV8u4uW9BQimd`</summary>

```json
{
  "query": "SWE-bench contamination gold patch reproduction frontier models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f987f22-452e-4f35-b35a-2e202f830190",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtUZdxPxE7BqobkFy1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "87f5711b-9e55-4247-9e73-cd99bc43fabf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cCfS5iUrGRWTY2hie8tSH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 8958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1429,
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

_source line 10 · 2026-05-12T02:30:18.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BfJQz28kE12XfS3crzqLbp`</summary>

```json
{
  "query": "SWE-bench Verified vs Pro scores comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87f5711b-9e55-4247-9e73-cd99bc43fabf",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtUZdxPxE7BqobkFy1z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2930efdb-a0d9-41be-8d1e-b46ccdf39d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cCfS5iUrGRWTY2hie8tSH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1429,
      "cache_read_input_tokens": 8958,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1429
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 8958,
          "cache_creation_input_tokens": 1429,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1429,
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

_source line 11 · 2026-05-12T02:30:24.407Z_

<details><summary>↩ Tool result · `toolu_01FSf6Qj8yq8KoGL7qja4TUR`</summary>

```text
Web search results for query: "SWE-bench Verified contamination OpenAI stopped reporting 2026"

Links: [{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"},{"title":"OpenAI Developers on X: \"The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we’re no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards. SWE-bench\" / X","url":"https://x.com/OpenAIDevs/status/2026002219909427270"},{"title":"OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed","url":"https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests"},{"title":"Is SWE-bench Verified Contaminated? OpenAI Shifts to SWE-bench Pro | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/news/swe-bench-contamination-debate"},{"title":"⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data","url":"https://www.latent.space/p/swe-bench-dead"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | daily.dev","url":"https://app.daily.dev/posts/why-swe-bench-verified-no-longer-measures-frontier-coding-capabilities-yitnqurmf"},{"title":"[Leaderboard] AI Agent Framework Scorecard 2026 | Rapid Claw","url":"https://rapidclaw.dev/blog/ai-agent-benchmarks-2026"},{"title":"OpenAI o3 SWE-Bench Score: What Engineers Aren't Told","url":"https://neuralwired.com/2026/04/13/openai-o3-swe-bench-benchmark/"}]

Based on the search results, here's what happened with SWE-bench Verified contamination and OpenAI stopping reporting:

## Summary

In February 2026, OpenAI announced that "SWE-bench Verified is increasingly contaminated" and recommended SWE-bench Pro instead.

## Key Issues Identified

An audit of 138 problems that OpenAI o3 consistently failed found that 59.4% contain flawed test cases — either too narrow (enforcing specific implementation details) or too wide (testing functionality not described in the problem).

Contamination analysis showed all tested frontier models (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) can reproduce exact gold patches and verbatim problem details, indicating training data exposure.

## OpenAI's Response

In recent months OpenAI chose to report results from the public split of SWE-Bench Pro and recommended other model developers do the same. SWE-bench Pro is not perfect, but empirically seems to suffer less from contamination issues, with cases of contamination being significantly rarer and less egregious than SWE-bench Verified.

## Score Differences

Claude Mythos Preview leads SWE-bench Verified at 93.9%, but the same model scores only 45.9% on SWE-bench Pro — the harder, contamination-free version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3d214d9-1d68-455f-b397-78f92aa26d7a",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "e7ddaf85-7ed6-4e9c-a2ec-fce5f482b989",
  "sourceToolAssistantUUID": "e3d214d9-1d68-455f-b397-78f92aa26d7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T02:30:25.651Z_

<details><summary>↩ Tool result · `toolu_01BfJQz28kE12XfS3crzqLbp`</summary>

```text
Web search results for query: "SWE-bench Verified vs Pro scores comparison"

Links: [{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"You’re comparing SWE Bench Verified to SWE Bench Pro. The scores aren’t comparable.","url":"https://www.threads.com/@sobri909/post/DWfoVngkeqX/youre-comparing-swe-bench-verified-to-swe-bench-pro-the-scores-arent-comparable"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-Bench Pro Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-pro"},{"title":"SWE-Bench Pro: Raising the Bar for Agentic Coding | Scale AI","url":"https://scale.com/blog/swe-bench-pro"},{"title":"Scale Labs Leaderboard: SWE-Bench Pro (Private Dataset)","url":"https://labs.scale.com/leaderboard/swe_bench_pro_private"}]

Based on the search results, here's a comprehensive comparison of SWE-bench Verified vs Pro scores:

## Performance Gap

The benchmark is significantly more challenging than its predecessors; top models score around 23% on the SWE-Bench Pro public set, compared to 70%+ on SWE-Bench Verified. For example, Claude Mythos Preview leads SWE-bench Verified at 93.9%, but the same model scores only 45.9% on SWE-bench Pro.

## Why Verified Scores Are Higher

OpenAI has stopped reporting Verified scores after finding that every frontier model showed training data contamination on the dataset. OpenAI's audit found that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks.

## Key Differences

- **Dataset:** SWE-Bench Verified is a human-validated subset of 500 Python-only tasks from the original SWE-Bench, while SWE-Bench Pro contains 1,865 tasks across 41 actively maintained repositories spanning Python, Go, TypeScript, and JavaScript.

- **Real-world relevance:** This provides a more accurate measure of an agent's true problem-solving capabilities in environments that mirror professional software development.

- **Private subset performance:** The private subset of the SWE-Bench Pro leaderboard reveals a drop in performance. Claude Opus 4.1 decreases from 22.7% to 17.8% resolution, and OpenAI GPT-5 falls from 23.1% to 14.9%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2930efdb-a0d9-41be-8d1e-b46ccdf39d6e",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "0e5d1fbb-379b-4cf5-b371-ddaa72bd8341",
  "sourceToolAssistantUUID": "2930efdb-a0d9-41be-8d1e-b46ccdf39d6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T02:30:27.070Z_

<details><summary>↩ Tool result · `toolu_01JMHwU1etdfV8u4uW9BQimd`</summary>

```text
Web search results for query: "SWE-bench contamination gold patch reproduction frontier models"

Links: [{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"},{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | daily.dev","url":"https://app.daily.dev/posts/why-swe-bench-verified-no-longer-measures-frontier-coding-capabilities-yitnqurmf"},{"title":"Why we no longer evaluate SWE-bench Verified - OpenAI News | Aetos.AI","url":"https://aetos.ai/posts/14417b93793f21d3"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"⚡️The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data","url":"https://www.latent.space/p/swe-bench-dead"},{"title":"SWE-Bench Explained (2026): Methodology, Scoring, Contamination | CodeSOTA","url":"https://www.codesota.com/guides/swe-bench-explained"},{"title":"Approaching 90%: What Happens When AI Coding Benchmarks Saturate | AgentMarketCap","url":"https://agentmarketcap.ai/blog/2026/04/10/swe-bench-saturation-90-percent-coding-benchmarks"},{"title":"OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed","url":"https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests"},{"title":"SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard","url":"https://www.morphllm.com/swe-benchmark"},{"title":"SWE-bench Verified Issues Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified-issues"}]

Based on the web search results, here's what I found about SWE-bench contamination, gold patch reproduction, and frontier models:

## Key Findings

All tested frontier models (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) can reproduce exact gold patches and verbatim problem details, indicating training data exposure.

### Contamination Detection Method

To probe for contamination, GPT-5 received the SWE-bench Verified task's ID, description, gold patch, and PR tests. Over 15 turns, GPT-5 was allowed to vary the system/developer prompt, user prompt, and assistant prefill with different elicitation strategies. After each turn, a judge model labeled contamination severity from "none" to "strong."

### Gold Patch Reproduction Examples

GPT-5.2 outputs the exact gold patch from a short snippet of the task description, knowing the exact class and method name, and the new early return condition `if username is None or password is None` that is introduced.

Claude Opus 4.5 quoted word-for-word an inline comment from a gold patch it supposedly never encountered. Gemini 3 Flash, given only a task ID, output the complete unified diff with correct line numbers.

### Impact on Benchmark Validity

Benchmarks sourced from publicly available material carry contamination risk, where training-data exposure can silently inflate scores. If publicly crawled data is used in benchmark construction, model developers should perform additional tests for contamination.

SWE-bench Pro empirically seems to suffer less from contamination issues. The contamination pipeline found some cases of contamination, but these cases were significantly rarer and less egregious than SWE-bench Verified, and no model was able to produce a complete verbatim gold patch.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87f5711b-9e55-4247-9e73-cd99bc43fabf",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "df46ee25-4e3b-4991-abc8-e9711d83e36e",
  "sourceToolAssistantUUID": "87f5711b-9e55-4247-9e73-cd99bc43fabf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T02:30:30.310Z_

<details><summary>↩ Tool result · `toolu_01QTTR49veqRQupQvExjGjje`</summary>

```text
Web search results for query: "SWE-bench Pro benchmark 2026"

Links: [{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Pro Benchmark 2026: 30 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/swePro"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Pro Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-pro"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? | OpenReview","url":"https://openreview.net/forum?id=9R2iUHhVfr"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"}]

Based on the search results, here's comprehensive information about the SWE-bench Pro benchmark in 2026:

## Overview

SWE-Bench Pro is a benchmark designed to provide a rigorous and realistic evaluation of AI agents for software engineering. It evaluates AI coding agents on 1,865 long-horizon tasks from 41 real repositories across Python, Go, TypeScript, and JavaScript.

## Purpose & Design

SWE-Bench Pro was developed to address limitations in existing benchmarks by tackling data contamination (models likely saw evaluation code during training), limited task diversity (benchmarks focus on simple utility libraries), oversimplified problems (ambiguous issues are often removed), and unreliable testing (inconsistent setups make it difficult to verify solutions).

## Task Complexity

Every SWE-Bench Pro task requires at least 10 lines of change, with over 100 tasks requiring more than 100 lines—tasks that would take a professional engineer hours to days. SWE-Bench Pro tasks require coordinating changes across an average of 4.1 files.

## Current Leaderboard Performance (May 2026)

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Pro leaderboard with 77.8%, followed by Claude Opus 4.7 (Adaptive) (64.3%) and GPT-5.5 (58.6%).

## Comparison to SWE-bench Verified

Claude Opus 4.5 scores 80.9% on SWE-bench Verified but only 45.9% on SWE-bench Pro, using standardised scaffolding on tasks it could not have seen during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f987f22-452e-4f35-b35a-2e202f830190",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "c4dc4d10-a7d5-4373-b1e0-abb30c8d0c15",
  "sourceToolAssistantUUID": "7f987f22-452e-4f35-b35a-2e202f830190",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T02:30:33.382Z_

Let me get a few more targeted searches to fill in specific details on timing and the OpenAI announcement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4dc4d10-a7d5-4373-b1e0-abb30c8d0c15",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtVmdZ8wGhEgEWER4x7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a97fbe87-b360-4451-87d8-3cbd3341595b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2TWGQ2bqASqFsbKpU3pFj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 2078,
      "cache_read_input_tokens": 10387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2078,
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

_source line 16 · 2026-05-12T02:30:33.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MRrPyJbFTzVQJeqkEcJh7b`</summary>

```json
{
  "query": "OpenAI \"why we no longer evaluate SWE-bench Verified\" announcement date February 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a97fbe87-b360-4451-87d8-3cbd3341595b",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtVmdZ8wGhEgEWER4x7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d25aec6-0305-4e66-a737-78c6bf34bb05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2TWGQ2bqASqFsbKpU3pFj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 2078,
      "cache_read_input_tokens": 10387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2078,
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

_source line 17 · 2026-05-12T02:30:34.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XTe6pnDCgkuuiBB8tJcDxW`</summary>

```json
{
  "query": "SWE-bench Pro Scale AI launch date introduced when"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d25aec6-0305-4e66-a737-78c6bf34bb05",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtVmdZ8wGhEgEWER4x7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73aa7cd6-c3b1-4d69-b874-22a9e18b1d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S2TWGQ2bqASqFsbKpU3pFj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1930,
      "cache_creation_input_tokens": 2078,
      "cache_read_input_tokens": 10387,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2078
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1930,
          "output_tokens": 143,
          "cache_read_input_tokens": 10387,
          "cache_creation_input_tokens": 2078,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2078,
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

_source line 18 · 2026-05-12T02:30:37.133Z_

<details><summary>↩ Tool result · `toolu_01MRrPyJbFTzVQJeqkEcJh7b`</summary>

```text
Web search results for query: "OpenAI "why we no longer evaluate SWE-bench Verified" announcement date February 2026"

Links: [{"title":"Why we no longer evaluate SWE-bench Verified - DEV Community","url":"https://dev.to/jgnoncelogic/why-we-no-longer-evaluate-swe-bench-verified-59gc"},{"title":"Why we no longer evaluate SWE-bench Verified - OpenAI News | Aetos.AI","url":"https://aetos.ai/posts/14417b93793f21d3"},{"title":"Why we no longer evaluate SWE-bench Verified - Jat Ai News - Unveiling the Future of Intelligence","url":"https://news.jatlink.uk/4787"}]

Based on the search results, OpenAI announced that SWE-bench Verified is no longer used for evaluating autonomous software engineering due to flawed test cases and training data contamination. OpenAI stopped reporting SWE-bench Verified scores and recommends that other model developers do so too.

The announcement was made on **February 23, 2026**. OpenAI recommends reporting results for SWE-bench Pro instead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d25aec6-0305-4e66-a737-78c6bf34bb05",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "db40de4c-a390-4bbd-8cad-6419e5668e4a",
  "sourceToolAssistantUUID": "6d25aec6-0305-4e66-a737-78c6bf34bb05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T02:30:37.841Z_

<details><summary>↩ Tool result · `toolu_01XTe6pnDCgkuuiBB8tJcDxW`</summary>

```text
Web search results for query: "SWE-bench Pro Scale AI launch date introduced when"

Links: [{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"ScaleAI/SWE-bench_Pro · Datasets at Hugging Face","url":"https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Scale AI: SWE-Bench Pro — Raising the Bar for Agentic Coding | 0h-n0 TechBLog","url":"https://0h-n0.github.io/posts/techblog-scale-swe-bench-pro/"},{"title":"Scale AI on X: \"We launched SWE-Bench Pro last month to incredible feedback, and we’ve now updated the leaderboard with the latest models and no cost caps. SoTA models now break 40% pass rate. Congrats to @Anthropic for sweeping the top spots! 🥇Claude 4.5 Sonnet 🥈Claude 4 Sonnet 🥉Claude 4.5 https://t.co/ESaSw27W9m\" / X","url":"https://x.com/scale_AI/status/1980685992987431368"},{"title":"SWE-Bench Pro: AI on Software Engineering Tasks | Scale Labs","url":"https://labs.scale.com/papers/swe_bench_pro"},{"title":"SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard","url":"https://www.morphllm.com/swe-benchmark"},{"title":"SWE-Bench Pro: Raising the Bar for Agentic Coding | Scale AI","url":"https://scale.com/blog/swe-bench-pro"},{"title":"GitHub - scaleapi/SWE-bench_Pro-os: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? · GitHub","url":"https://github.com/scaleapi/SWE-bench_Pro-os"},{"title":"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?","url":"https://static.scale.com/uploads/654197dc94d34f66c0f5184e/SWEAP_Eval_Scale%20(9).pdf"}]

Based on the search results, SWE-Bench Pro was introduced by Scale AI to raise the bar and develop a more realistic, contamination-resistant benchmark that picks up where SWE-Bench Verified leaves off.

The launch date was September 19, 2025, as indicated in the Scale AI blog post about SWE-Bench Pro.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73aa7cd6-c3b1-4d69-b874-22a9e18b1d4d",
  "isSidechain": true,
  "promptId": "bb38eb9c-eebd-4557-8dc5-3f5aa26b5d56",
  "agentId": "a2bffc47ff86f6aca",
  "type": "user",
  "uuid": "7d209125-6411-4450-bd9d-78cf97bd8521",
  "sourceToolAssistantUUID": "73aa7cd6-c3b1-4d69-b874-22a9e18b1d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-12T02:31:17.667Z_

Here is a comprehensive report based on what the web searches returned. I am reporting exactly what the search results say.

---

## 1. Did OpenAI stop reporting SWE-bench Verified scores? When?

**Yes.** OpenAI published a post titled "Why SWE-bench Verified no longer measures frontier coding capabilities" on **February 23, 2026**. In it, OpenAI announced it would no longer report SWE-bench Verified scores and recommended that other model developers stop doing so as well.

The reasons OpenAI cited:
- **Flawed test cases:** An audit of 138 problems that OpenAI o3 consistently failed found that **59.4%** contain flawed test cases -- either too narrow (enforcing specific implementation details) or too wide (testing functionality not described in the problem).
- **Training data contamination:** All tested frontier models showed evidence of training data exposure (see item 4 below).

OpenAI now recommends reporting results on **SWE-bench Pro** instead.

---

## 2. What is SWE-bench Pro? When was it introduced?

**SWE-bench Pro** was created by **Scale AI** and launched on **September 19, 2025**. It was designed to address the contamination and task-diversity limitations of SWE-bench Verified.

Key characteristics:
- **1,865 long-horizon tasks** from **41 real repositories** across **Python, Go, TypeScript, and JavaScript** (compared to SWE-bench Verified's 500 Python-only tasks).
- Every task requires **at least 10 lines of change**, with over 100 tasks requiring more than 100 lines.
- Tasks require coordinating changes across an **average of 4.1 files**.
- Has both a **public** and **private** dataset split (the private split shows even lower scores, suggesting less overfitting/contamination).

---

## 3. Latest scores on SWE-bench Verified vs Pro for frontier models

**SWE-bench Verified (as of recent reporting):**
- Claude Mythos Preview: **93.9%** (top)
- Claude Opus 4.5: **80.9%**
- (Scores are very high across frontier models, with saturation near 90%+)

**SWE-bench Pro (public split, as of ~May 2026):**
- Claude Mythos Preview: **77.8%** (top, but note this appears to be a later measurement; earlier reports showed ~45.9%)
- Claude Opus 4.7 (Adaptive): **64.3%**
- GPT-5.5: **58.6%**

**SWE-bench Pro (private split -- even harder):**
- Claude Opus 4.1: drops from 22.7% to **17.8%**
- OpenAI GPT-5: drops from 23.1% to **14.9%**

The performance gap is dramatic. The same model (Claude Mythos Preview) that scores 93.9% on Verified scores far lower on Pro. Earlier models showed gaps like 80.9% (Verified) vs 45.9% (Pro) for Claude Opus 4.5.

---

## 4. Is the claim about "verbatim gold-patch reproduction" accurate?

**Yes, according to OpenAI's published findings.** The search results confirm:

- **GPT-5.2** was shown to output the exact gold patch from a short snippet of the task description, knowing the exact class and method name and the new early return condition introduced in the patch.
- **Claude Opus 4.5** quoted **word-for-word an inline comment** from a gold patch it supposedly never encountered.
- **Gemini 3 Flash**, given only a task ID, output the **complete unified diff with correct line numbers**.

OpenAI's contamination detection method involved giving GPT-5 a task's ID, description, gold patch, and PR tests, then allowing 15 turns to probe with different elicitation strategies. A judge model labeled contamination severity from "none" to "strong."

Importantly, on **SWE-bench Pro**, the same contamination pipeline found cases of contamination to be **significantly rarer and less egregious**, and **no model was able to produce a complete verbatim gold patch** on Pro tasks.

---

## Summary

The contamination concern is well-documented and confirmed by OpenAI's own research. SWE-bench Verified is increasingly viewed as an unreliable measure for frontier models due to training data leakage. SWE-bench Pro, while not perfect, represents the current industry-recommended alternative with substantially lower (and presumably more realistic) scores.

---

Sources:
- [Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
- [Is SWE-bench Verified Contaminated? OpenAI Shifts to SWE-bench Pro | CodeSOTA](https://www.codesota.com/news/swe-bench-contamination-debate)
- [The End of SWE-Bench Verified -- Latent Space Podcast](https://www.latent.space/p/swe-bench-dead)
- [SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean](https://www.codeant.ai/blogs/swe-bench-scores)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)
- [SWE-Bench Pro: Raising the Bar for Agentic Coding | Scale AI](https://scale.com/blog/swe-bench-pro)
- [SWE-Bench Pro Leaderboard (Public Dataset) | Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard](https://www.morphllm.com/swe-benchmark)
- [OpenAI Developers on X (announcement tweet)](https://x.com/OpenAIDevs/status/2026002219909427270)
- [Why we no longer evaluate SWE-bench Verified - DEV Community](https://dev.to/jgnoncelogic/why-we-no-longer-evaluate-swe-bench-verified-59gc)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d209125-6411-4450-bd9d-78cf97bd8521",
  "isSidechain": true,
  "agentId": "a2bffc47ff86f6aca",
  "requestId": "req_011CawtWKr3fSsvyzvauKgSm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "732efbec-5ddc-4330-938d-52a876a9ef62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f798b600-6634-458d-b3ae-c38ff9f70c19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HceL9Fjnj96f5sYeuW4ozx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3163,
      "cache_read_input_tokens": 12465,
      "output_tokens": 1610,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3163
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1610,
          "cache_read_input_tokens": 12465,
          "cache_creation_input_tokens": 3163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3163,
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
