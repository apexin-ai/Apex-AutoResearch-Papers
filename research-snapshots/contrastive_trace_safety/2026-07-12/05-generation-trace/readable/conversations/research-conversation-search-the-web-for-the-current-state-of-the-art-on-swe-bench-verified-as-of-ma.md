# Research conversation: Search the web for the current state-of-the-art on SWE-bench Verified as of May 2026. I want to know: 1. What is the cur

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ae2f028d410b152c2.jsonl`
- **Structured JSON:** [`cda677cd274519277e75.json`](../../sessions/cd/cda677cd274519277e75.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-10T20:07:02.003Z_

Search the web for the current state-of-the-art on SWE-bench Verified as of May 2026. I want to know:
1. What is the current top score on SWE-bench Verified?
2. What models/systems achieve the highest scores?
3. How does an 8B model typically perform on SWE-bench Verified (if any results exist)?

Try these searches:
- "SWE-bench Verified leaderboard 2026"
- "SWE-bench Verified state of the art May 2026"
- "SWE-bench Verified best results"
- "small model SWE-bench performance 8B 7B"

Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "ae2f028d410b152c2",
  "type": "user",
  "uuid": "0611b7ca-a7a2-4d0e-8b0b-3405aae79c3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T20:07:07.256Z_

I'll search for the current state-of-the-art on SWE-bench Verified as of May 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0611b7ca-a7a2-4d0e-8b0b-3405aae79c3c",
  "isSidechain": true,
  "agentId": "ae2f028d410b152c2",
  "requestId": "req_011CauVSp96kNME3GekkU2tN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60000846-137f-4f6e-ac47-b54c64b6503d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013szkxThAByFCP25Qw3x9s4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T20:07:07.456Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LyihMMiKJU7jY56yvR54Ph`</summary>

```json
{
  "query": "SWE-bench Verified leaderboard 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60000846-137f-4f6e-ac47-b54c64b6503d",
  "isSidechain": true,
  "agentId": "ae2f028d410b152c2",
  "requestId": "req_011CauVSp96kNME3GekkU2tN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "22abac68-da72-4a11-b95a-71cb029cc8f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013szkxThAByFCP25Qw3x9s4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T20:07:07.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XGA2658S4mkoodBGnm7D1x`</summary>

```json
{
  "query": "SWE-bench Verified state of the art May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22abac68-da72-4a11-b95a-71cb029cc8f6",
  "isSidechain": true,
  "agentId": "ae2f028d410b152c2",
  "requestId": "req_011CauVSp96kNME3GekkU2tN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7a95848-96b9-4208-9f82-d8c657ba2b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013szkxThAByFCP25Qw3x9s4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T20:07:07.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QH9SF65AXUzw3HhffKzWSk`</summary>

```json
{
  "query": "SWE-bench Verified best results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a95848-96b9-4208-9f82-d8c657ba2b5a",
  "isSidechain": true,
  "agentId": "ae2f028d410b152c2",
  "requestId": "req_011CauVSp96kNME3GekkU2tN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2293d5f5-99fd-4ccd-b7c7-b140d3a42d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013szkxThAByFCP25Qw3x9s4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T20:07:07.850Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JfzzrFhjwM9NcAf6ZYQVSF`</summary>

```json
{
  "query": "small model SWE-bench performance 8B 7B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2293d5f5-99fd-4ccd-b7c7-b140d3a42d85",
  "isSidechain": true,
  "agentId": "ae2f028d410b152c2",
  "requestId": "req_011CauVSp96kNME3GekkU2tN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "236487ce-0dc1-4c5b-96ff-6b6622b91f5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013szkxThAByFCP25Qw3x9s4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13789,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 233,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 588,
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

_source line 7 · 2026-05-10T20:07:12.625Z_

<details><summary>↩ Tool result · `toolu_01XGA2658S4mkoodBGnm7D1x`</summary>

```text
Web search results for query: "SWE-bench Verified state of the art May 2026"

Links: [{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/SWE-bench/SWE-bench"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"Codesota — the open registry of state-of-the-art machine learning","url":"https://www.codesota.com/browse/agentic/swe-bench"},{"title":"SWE-bench Verified Technical Report | Verdent - Verdent Blog","url":"https://www.verdent.ai/blog/swe-bench-verified-technical-report"}]

Based on the search results, here's the state-of-the-art performance on SWE-bench Verified as of May 2026:

## Top Performers

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Verified leaderboard with 93.9%, followed by Claude Opus 4.7 (Adaptive) (87.6%) and GPT-5.3 Codex (85%).

## About SWE-bench Verified

SWE-bench Verified is a curated, human-verified subset of SWE-bench that tests models on resolving real GitHub issues from popular open-source Python repositories like Django, Flask, and scikit-learn. 44 models have been evaluated on SWE-bench Verified.

## Benchmark Composition

The benchmark consists of 500 software engineering problems from real GitHub issues, validated by human annotators for evaluating language models' ability to resolve real-world coding issues by generating patches for Python codebases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7a95848-96b9-4208-9f82-d8c657ba2b5a",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "ae2f028d410b152c2",
  "type": "user",
  "uuid": "cc8b8ac0-14d6-4841-a535-4a146974fdc1",
  "sourceToolAssistantUUID": "c7a95848-96b9-4208-9f82-d8c657ba2b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T20:07:13.808Z_

<details><summary>↩ Tool result · `toolu_01LyihMMiKJU7jY56yvR54Ph`</summary>

```text
Web search results for query: "SWE-bench Verified leaderboard 2026"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"}]

Based on the latest search results, here's what I found about the SWE-bench Verified leaderboard in 2026:

## Current Leaderboard Leaders

As of May 7, 2026, Claude Mythos Preview leads the SWE-bench Verified leaderboard with 93.9%, followed by Claude Opus 4.7 (Adaptive) (87.6%) and GPT-5.3 Codex (85%).

## Important Context About SWE-bench Verified

It's worth noting that you should treat SWE-bench Verified as a rough directional signal, not a precise measurement. A model at 80% Verified is almost certainly better than a model at 40% Verified, but the exact number carries far less precision than the leaderboard formatting suggests.

This caution exists because OpenAI has stopped reporting Verified scores after finding that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks.

## Alternative: SWE-bench Pro

OpenAI has stopped reporting Verified scores and recommends SWE-bench Pro instead. The Pro version is designed to be more contamination-resistant and better reflects real-world coding challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22abac68-da72-4a11-b95a-71cb029cc8f6",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "ae2f028d410b152c2",
  "type": "user",
  "uuid": "1955a7e0-e841-4029-834c-35ac7ca05fc1",
  "sourceToolAssistantUUID": "22abac68-da72-4a11-b95a-71cb029cc8f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T20:07:14.309Z_

<details><summary>↩ Tool result · `toolu_01QH9SF65AXUzw3HhffKzWSk`</summary>

```text
Web search results for query: "SWE-bench Verified best results"

Links: [{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"}]

Based on the search results, here are the best results on SWE-bench Verified:

## Current Top Performers

Claude Mythos Preview from Anthropic currently leads the SWE-Bench Verified leaderboard with a score of 0.939 across 89 evaluated AI models. Claude Mythos Preview leads with 93.9%, followed by Claude Opus 4.7 at 87.6% and Claude Opus 4.5 at 80.9%.

However, it's important to note that different sources report different scores based on their evaluation methodology. According to one leaderboard, GPT 5.5 leads with a performance of 82.60%, achieving the best accuracy on SWE-bench Verified, with Claude Opus 4.7 following closely at 82.00%.

## About the Benchmark

SWE-bench Verified is a verified subset of 500 software engineering problems from real GitHub issues, validated by human annotators for evaluating language models' ability to resolve real-world coding issues by generating patches for Python codebases. Human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable given the available information.

## Important Context

It's worth noting that OpenAI's audit found that every frontier model tested could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks, and OpenAI has stopped reporting Verified scores and recommends SWE-Bench Pro instead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2293d5f5-99fd-4ccd-b7c7-b140d3a42d85",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "ae2f028d410b152c2",
  "type": "user",
  "uuid": "66f0982e-95f3-4d32-86f8-93cdaad7c076",
  "sourceToolAssistantUUID": "2293d5f5-99fd-4ccd-b7c7-b140d3a42d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:07:21.580Z_

<details><summary>↩ Tool result · `toolu_01JfzzrFhjwM9NcAf6ZYQVSF`</summary>

```text
Web search results for query: "small model SWE-bench performance 8B 7B"

Links: [{"title":"SWE-bench Results Viewer","url":"https://www.swebench.com/viewer.html"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"We Benchmarked 12 Small Language Models Across 8 Tasks to Find the Best Base Model for Fine-Tuning — distil labs","url":"https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"HAL: SWE-bench Verified Mini Leaderboard","url":"https://hal.cs.princeton.edu/swebench_verified_mini"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-rebench Leaderboard","url":"https://swe-rebench.com/"}]

Based on the search results, here's what I found about small model SWE-bench performance for 7B and 8B models:

## Key Findings on Small Model Performance

The search results don't provide extensive detailed data specifically focused on 7B and 8B model performance on SWE-bench. However, there are some relevant insights:

**8B Models and Base Performance:**
The 8B models claim the top spots, with Qwen3-8B showing remarkably consistent performance across all benchmarks (lowest standard deviation). This finding comes from a broader benchmark study comparing small language models, though not specifically focused on SWE-bench.

**Open-Source Model Performance:**
There is a clear trend that closed-source models perform better on SWE-bench Verified than open-source models. While this applies broadly, it suggests that smaller open-source models (like the 7B and 8B range) would likely score lower than large proprietary models on SWE-bench.

**Comparative Context:**
The search results show that top closed-source models like Claude Opus 4.7 and GPT-5 models score in the 80%+ range on SWE-bench Verified, while the benchmark notes that most top models score over 70%, making it challenging for smaller open-source models to compete.

The search results don't provide specific performance numbers for dedicated 7B or 8B model evaluations on SWE-bench. For more detailed performance metrics on these specific model sizes, you might want to check the official SWE-bench leaderboard directly or papers specifically benchmarking small models on this task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "236487ce-0dc1-4c5b-96ff-6b6622b91f5f",
  "isSidechain": true,
  "promptId": "29c21c28-32d1-43a1-915b-aaa2e5d33c88",
  "agentId": "ae2f028d410b152c2",
  "type": "user",
  "uuid": "1eaaf588-636f-4b4f-bc1d-13d804ffff62",
  "sourceToolAssistantUUID": "236487ce-0dc1-4c5b-96ff-6b6622b91f5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T20:07:29.244Z_

## Summary: SWE-bench Verified State-of-the-Art (May 2026)

Based on my search results, here are the key findings about SWE-bench Verified performance:

### 1. Current Top Score
**Claude Mythos Preview leads with 93.9%**, followed by Claude Opus 4.7 (Adaptive) at 87.6% and GPT-5.3 Codex at 85%. (Note: Some sources report slightly different scores - GPT 5.5 has been reported at 82.60% and Claude Opus 4.7 at 82.00%, suggesting variation in evaluation methodologies across different leaderboards.)

### 2. Highest-Scoring Models/Systems
The top performers are all frontier-class models:
- **Claude Mythos Preview** (93.9%) - Anthropic
- **Claude Opus 4.7 (Adaptive)** (87.6%) - Anthropic
- **GPT-5.3 Codex** (85%) - OpenAI
- **Claude Opus 4.5** (80.9%) - Anthropic

### 3. 8B Model Performance
Unfortunately, the search results do not provide detailed specific performance numbers for 8B models on SWE-bench Verified. The results indicate that:
- **Qwen3-8B** is mentioned as showing strong performance across benchmarks, but no specific SWE-bench Verified score is provided
- There's a clear trend that **closed-source models significantly outperform open-source models** on SWE-bench Verified
- The benchmark notes most top models score over 70%, suggesting smaller open-source models (7B-8B range) would struggle to compete

### Important Caveat
**Critical finding**: OpenAI has stopped reporting Verified scores after discovering that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain tasks. OpenAI now recommends using **SWE-bench Pro** instead as a more contamination-resistant alternative.

Sources:
- [SWE-bench Leaderboards](https://www.swebench.com/)
- [SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai](https://benchlm.ai/benchmarks/sweVerified)
- [SWE-Bench Verified Benchmark Leaderboard](https://llm-stats.com/benchmarks/swe-bench-verified)
- [SWE-bench Verified | Epoch AI](https://epoch.ai/benchmarks/swe-bench-verified)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eaaf588-636f-4b4f-bc1d-13d804ffff62",
  "isSidechain": true,
  "agentId": "ae2f028d410b152c2",
  "requestId": "req_011CauVUFoUEKZRETMoPYkrn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d87aa2d4-84c1-4cc4-a04e-0d097ccfe20d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f3cebe39-ac70-4485-ab6f-907fb016d315",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ruvi16riasRAxkVHBhQV8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 14377,
      "output_tokens": 681,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4096
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 681,
          "cache_read_input_tokens": 14377,
          "cache_creation_input_tokens": 4096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4096,
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
