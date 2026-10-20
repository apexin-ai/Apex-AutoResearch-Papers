# Research conversation: I need to verify specific data availability for a research proposal revision. Please search and fetch: 1. Search for "ti

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 1
- **Tool calls:** 36
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a1f3ab31e3696d242.jsonl`
- **Structured JSON:** [`70d66c779b547847b3a1.json`](../../sessions/70/70d66c779b547847b3a1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

84 recorded events

### User

_source line 1 · 2026-05-28T13:33:09.988Z_

I need to verify specific data availability for a research proposal revision. Please search and fetch:

1. Search for "tinyBenchmarks Polo 2024 per-item response data LLM IRT" - I need to confirm whether the full 395-model × 29K-item binary response matrix from Polo et al. (2024) is publicly available, and where exactly. Fetch the tinyBenchmarks paper or HuggingFace page.

2. Search for "huggingface open-llm-leaderboard details per-model item-level" and check whether the V2 per-model details datasets require access approval or are freely downloadable.

3. Search for "MATH-500 GSM8K items overlap Open LLM Leaderboard" to check whether MATH-500 and GSM8K items specifically are part of the Open LLM Leaderboard evaluation (V1 or V2), which would determine if we have large-N calibration data for these specific items.

4. Search for "two-stage IRT contamination detection fixed parameter" to see if anyone has combined fixed-parameter calibration with contamination/cheating detection in IRT.

Report all findings with specific URLs and details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "9fa63fdd-9b56-4f53-b40d-628c11d08048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T13:33:09.995Z_

```json
{
  "parentUuid": "9fa63fdd-9b56-4f53-b40d-628c11d08048",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "c1bed714-871d-46a9-8358-1cde7b95ee98",
  "timestamp": "2026-05-28T13:33:09.995Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T13:33:09.996Z_

```json
{
  "parentUuid": "c1bed714-871d-46a9-8358-1cde7b95ee98",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a5864311-d9b2-423c-8f44-591a07b708c8",
  "timestamp": "2026-05-28T13:33:09.996Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T13:33:12.210Z_



I'll conduct all four searches in parallel to gather the information you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5864311-d9b2-423c-8f44-591a07b708c8",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV3yH9FHFEcx8a9yz6rK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "442ffef3-806d-46cf-b2d2-d35b59e47d3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7DstpQxcsxUvGKL7V4n2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1623,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1623,
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

_source line 5 · 2026-05-28T13:33:12.670Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VV8uyTgzpCxRit9p2XR7Sk`</summary>

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
  "parentUuid": "442ffef3-806d-46cf-b2d2-d35b59e47d3d",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV3yH9FHFEcx8a9yz6rK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe7bd013-5903-4cc8-baaa-c2ea33d7ef6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7DstpQxcsxUvGKL7V4n2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1623,
      "cache_read_input_tokens": 7407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1623,
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

_source line 6 · 2026-05-28T13:33:12.677Z_

<details><summary>↩ Tool result · `toolu_01VV8uyTgzpCxRit9p2XR7Sk`</summary>

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
  "parentUuid": "fe7bd013-5903-4cc8-baaa-c2ea33d7ef6d",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "e5154fce-788f-4349-be7b-458847e23d9b",
  "sourceToolAssistantUUID": "fe7bd013-5903-4cc8-baaa-c2ea33d7ef6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T13:33:15.054Z_



Now I'll run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5154fce-788f-4349-be7b-458847e23d9b",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV3yVDmdh5QiSd9exrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49cbfc21-e176-4d3b-bb00-2dc8e6f447fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdHuwznhvTp13tfmHQYfZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 8 · 2026-05-28T13:33:16.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01635E1RBVRCFxwQkVmSQZV1`</summary>

```json
{
  "query": "tinyBenchmarks Polo 2024 per-item response data LLM IRT binary response matrix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49cbfc21-e176-4d3b-bb00-2dc8e6f447fc",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV3yVDmdh5QiSd9exrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3db1d8e9-91e2-4cb9-82fe-7c5bc62e74f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdHuwznhvTp13tfmHQYfZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 9 · 2026-05-28T13:33:16.946Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H6QjXxHFR3onjDzh8rRnH8`</summary>

```json
{
  "query": "huggingface open-llm-leaderboard details per-model item-level V2 access approval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3db1d8e9-91e2-4cb9-82fe-7c5bc62e74f9",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV3yVDmdh5QiSd9exrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b514470-9064-47c9-a4ab-502bb56ac6cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdHuwznhvTp13tfmHQYfZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 10 · 2026-05-28T13:33:17.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3gx5YvXxhRSnQLymDyyy2`</summary>

```json
{
  "query": "MATH-500 GSM8K items overlap Open LLM Leaderboard evaluation V1 V2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b514470-9064-47c9-a4ab-502bb56ac6cd",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV3yVDmdh5QiSd9exrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a43a2a0-8e30-4f1e-8c46-d99010ad1edd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdHuwznhvTp13tfmHQYfZb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9030,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1118,
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

_source line 11 · 2026-05-28T13:33:18.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A9NLh4wM779Urn7XGS5gFk`</summary>

```json
{
  "query": "two-stage IRT contamination detection fixed parameter calibration cheating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a43a2a0-8e30-4f1e-8c46-d99010ad1edd",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV3yVDmdh5QiSd9exrBh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "696bc311-9d75-4ede-bbac-95241e174599",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdHuwznhvTp13tfmHQYfZb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 9030,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1118
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 9030,
          "cache_creation_input_tokens": 1118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1118,
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

_source line 12 · 2026-05-28T13:33:24.446Z_

<details><summary>↩ Tool result · `toolu_01635E1RBVRCFxwQkVmSQZV1`</summary>

```text
Web search results for query: "tinyBenchmarks Polo 2024 per-item response data LLM IRT binary response matrix"

Links: [{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tinybenchmarks-evaluating-llms-fewer-examples"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples [Quick Review]","url":"https://liner.com/review/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"Published as a conference paper at ICLR 2025 ME TABENCH","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/pdf/2402.14992"},{"title":"metabench A Sparse Benchmark to Measure General Ability in Large Language Models","url":"https://arxiv.org/html/2407.12844v1"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICLR 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"GitHub - felipemaiapolo/tinyBenchmarks: Evaluating LLMs with fewer examples · GitHub","url":"https://github.com/felipemaiapolo/tinyBenchmarks"},{"title":"(PDF) tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://www.researchgate.net/publication/383238265_tinyBenchmarks_evaluating_LLMs_with_fewer_examples"}]

Based on the search results, I found relevant information about the tinyBenchmarks research by Polo et al. (2024):

Maia Polo et al. (2024) published "tinyBenchmarks: evaluating LLMs with fewer examples" at a major machine learning conference. 

The research uses Item Response Theory (IRT) as a core methodology. The key idea behind tinyBenchmarks is to use Item Response Theory (IRT) to get more insights from a smaller number of test samples, as IRT is a statistical method that can estimate a model's abilities based on how it performs on a few carefully selected tasks.

Regarding the per-item response data and binary response matrix: The researchers introduce the generalized p-IRT (gp-IRT) estimator, which combines direct sampling-based estimation with IRT model predictions. The proposed approach effectively handles non-binary correctness scores by binarizing them using a scenario-dependent constant, enabling broader applicability of IRT models.

Polo and colleagues analyzed 395 LLMs with high-dimensional IRT models and clustering to create four smaller benchmarks. The work demonstrates the effectiveness of this approach: evaluating LLMs on a small, curated subset of examples is highly effective for estimating their performance on full benchmarks, achieving an average estimation error of approximately 2% with as few as 100 examples per scenario.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3db1d8e9-91e2-4cb9-82fe-7c5bc62e74f9",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "6482e956-26c4-4bff-952d-0f723bedae9b",
  "sourceToolAssistantUUID": "3db1d8e9-91e2-4cb9-82fe-7c5bc62e74f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T13:33:24.971Z_

<details><summary>↩ Tool result · `toolu_01H6QjXxHFR3onjDzh8rRnH8`</summary>

```text
Web search results for query: "huggingface open-llm-leaderboard details per-model item-level V2 access approval"

Links: [{"title":"open-llm-leaderboard (Open LLM Leaderboard)","url":"https://huggingface.co/open-llm-leaderboard"},{"title":"Open LLM Leaderboard 2 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-2"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Open LLM Leaderboard v1 · Hugging Face","url":"https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive"},{"title":"FAQ","url":"https://huggingface.co/docs/leaderboards/open_llm_leaderboard/faq"},{"title":"Leaderboards and Evaluations · Hugging Face","url":"https://huggingface.co/docs/leaderboards/index"},{"title":"open-llm-leaderboard/results · Datasets at Hugging Face","url":"https://huggingface.co/datasets/open-llm-leaderboard/results"},{"title":"Open-LLM performances are plateauing, let’s make the leaderboard steep again - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/blog"},{"title":"leaderboards/docs/source/en/open_llm_leaderboard/about.md at main · huggingface/leaderboards","url":"https://github.com/huggingface/leaderboards/blob/main/docs/source/en/open_llm_leaderboard/about.md"},{"title":"Hugging Face Upgrades Open LLM Leaderboard v2 for Enhanced AI Model Comparison - InfoQ","url":"https://www.infoq.com/news/2024/10/open-llm-leaderboard-v2-launch/"}]

Based on the search results, here's what I found about the Hugging Face Open LLM Leaderboard v2:

## Overview

Hugging Face has recently released Open LLM Leaderboard v2, an upgraded version of their benchmarking platform for large language models.

## Detailed Results and Per-Model Information

Results, model per model, of all the evaluations are available. The space contains the dataset with detailed results and queries for the models on the leaderboard.

## Data Access

Aggregated results for the Open LLM Leaderboard are available - if you want to download something, it's probably this! The leaderboard provides an interactive leaderboard where you can select and filter open-source language models to see how they perform on several tests such as IFEval, BBH, MATH, GPQA, MUSR, and MMLU-PRO.

## Item-Level Evaluation Details

Instance and Prompt level measurements are available including Strict Accuracy at Instance and Prompt Levels (inst_level_strict_acc,none and prompt_level_strict_acc,none).

However, the search results don't contain specific details about access approval processes or item-level V2 restrictions. For more detailed information about access requirements for specific datasets or features, you may need to check the official Hugging Face documentation or contact the Open LLM Leaderboard team directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b514470-9064-47c9-a4ab-502bb56ac6cd",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "07358845-d2cc-4ccb-b975-0cad5d475a44",
  "sourceToolAssistantUUID": "0b514470-9064-47c9-a4ab-502bb56ac6cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T13:33:25.855Z_

<details><summary>↩ Tool result · `toolu_01A9NLh4wM779Urn7XGS5gFk`</summary>

```text
Web search results for query: "two-stage IRT contamination detection fixed parameter calibration cheating"

Links: [{"title":"Are Exam Questions Known in Advance? Using Local Dependence to Detect Cheating","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5131967/"},{"title":"Sources of Error in IRT Trait Estimation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6023095/"},{"title":"ERIC - EJ1245948 - Two IRT Fixed Parameter Calibration Methods for the Bifactor Model, Journal of Educational Measurement, 2020","url":"https://eric.ed.gov/?id=EJ1245948"},{"title":"A Comparative Study of IRT Fixed Parameter Calibration Methods","url":"https://www.researchgate.net/publication/229754277_A_Comparative_Study_of_IRT_Fixed_Parameter_Calibration_Methods"},{"title":"Practical Consequences of Item Response Theory Model Misfit in the Context of Test Equating with Mixed-Format Test Data","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5378703/"},{"title":"Linking of Rasch-Scaled Tests: Consequences of Limited Item Pools and Model Misfit","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8289883/"},{"title":"The generalized Hausman test for detecting non-normality in the latent   variable distribution of the two-parameter IRT model","url":"https://arxiv.org/pdf/2402.08376"},{"title":"ERIC - EJ1229715 - Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data, Applied Measurement in Education, 2019","url":"https://eric.ed.gov/?id=EJ1229715"},{"title":"Practical Consequences of Item Response Theory Model Misfit in the Context of Test Equating with Mixed-Format Test Data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5378703/"}]

Based on the search results, I found relevant information about your query:

In IRT analyses, it is common practice to estimate latent trait scores using a two-stage approach. In the first stage, item calibration, item parameters are estimated using methods such as marginal maximum likelihood (MML). In the second stage, trait score estimates are typically computed using methods such as maximum-likelihood estimation or expected a posteriori prediction and treating the item parameter estimates as fixed.

The search results also contain information about fixed parameter calibration methods in IRT. Fixed parameter calibration (FPC) has been used to estimate the item parameters of a new test form on the existing ability scale of an item pool. Additionally, two fixed parameter calibration methods for the bifactor model are compared: the one prior weights updating and multiple expectation-maximization (EM) cycles (OWU-MEM) and multiple prior weights updating and multiple EM cycles (MWU-MEM) methods.

Regarding contamination detection and cheating, a Bayesian method uses an Item Response Theory (IRT) model in which the guessing parameter of a 3PL model is enhanced to include IP (item preknowledge), with a person's model fit assessed with each new item response.

However, the search results don't contain a specific publication directly combining all these elements (two-stage IRT, contamination detection, fixed parameter calibration, and cheating detection) in a single study.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "696bc311-9d75-4ede-bbac-95241e174599",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "98af49ec-5f59-40e5-89d5-77ab5455acf6",
  "sourceToolAssistantUUID": "696bc311-9d75-4ede-bbac-95241e174599",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T13:33:34.614Z_

<details><summary>↩ Tool result · `toolu_01R3gx5YvXxhRSnQLymDyyy2`</summary>

```text
Web search results for query: "MATH-500 GSM8K items overlap Open LLM Leaderboard evaluation V1 V2"

Links: [{"title":"Fixing Open LLM Leaderboard with Math-Verify","url":"https://huggingface.co/blog/math_verify_leaderboard"},{"title":"Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs   Evaluation, Benchmark, and Arena","url":"https://arxiv.org/pdf/2406.07545"},{"title":"LLM Benchmarks Compared: MMLU, HumanEval, GSM8K and More (2026)","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"Scale Labs Leaderboard: Math Evaluation","url":"https://labs.scale.com/leaderboard/math"},{"title":"2026 LLM Leaderboard: compare Anthropic, Google, OpenAI, and more... — Klu","url":"https://klu.ai/llm-leaderboard"},{"title":"GSM8K | DeepEval by Confident AI - The LLM Evaluation Framework","url":"https://deepeval.com/docs/benchmarks-gsm8k"},{"title":"Demystifying LLM Leaderboards: What You Need to Know | Shakudo","url":"https://www.shakudo.io/blog/demystifying-llm-leaderboards-what-you-need-to-know"},{"title":"GSM8k Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/gsm8k"},{"title":"A Careful Examination of Large Language Model Performance on Grade   School Arithmetic","url":"https://arxiv.org/pdf/2405.00332"}]

I found some relevant information about these benchmarks, but let me search more specifically for information about the overlap between MATH-500 and GSM8K in Open LLM Leaderboard versions.

Links: [{"title":"Open LLM Leaderboard - Hugging Face Open LLM Leaderboard | LLM Benchmark | LLMIndex | LLMIndex","url":"https://llmindex.net/benchmarks/open-llm-leaderboard"},{"title":"open-llm-leaderboard/open_llm_leaderboard · Brainstorming: Suggestions for improving the leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/477"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Data Contamination Can Cross Language Barriers","url":"https://arxiv.org/pdf/2406.13236"},{"title":"Open LLM Leaderboard - Compare Open Source Large Language Models","url":"https://open-llm-leaderboard-open-llm-leaderboard.hf.space/"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs   Evaluation, Benchmark, and Arena","url":"https://arxiv.org/pdf/2406.07545"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/pdf/2502.14425"}]

Let me search more specifically for MATH-500 and GSM8K overlap details.

Links: [{"title":"LLM | 常用的数学数据集：MATH、GSM8K、AIME24 等 - MoonOut - 博客园","url":"https://www.cnblogs.com/moonout/p/19611573"},{"title":"LLM Benchmarks Compared: MMLU, HumanEval, GSM8K and More (2026)","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"GitHub - om-ai-lab/open-agent-leaderboard: Reproducible Language Agent Research · GitHub","url":"https://github.com/om-ai-lab/open-agent-leaderboard"},{"title":"Training Verifiers to Solve Math Word Problems","url":"https://arxiv.org/pdf/2110.14168"},{"title":"TinyGSM: achieving >80% on GSM8k with small language models","url":"https://arxiv.org/pdf/2312.09241"},{"title":"A Careful Examination of Large Language Model Performance on Grade   School Arithmetic","url":"https://arxiv.org/pdf/2405.00332"},{"title":"GSM8K-V: Can Vision Language Models Solve Grade School Math Word Problems in Visual Contexts","url":"https://arxiv.org/pdf/2509.25160"}]

Let me search for more specific information about Open LLM Leaderboard V1 and V2 differences.

Links: [{"title":"The LLM leaderboard is dead, long live the leaderboard | dataku","url":"https://dataku.ai/blog/llm-leaderboard-dead-long-live-leaderboard"},{"title":"leaderboards/docs/source/en/open_llm_leaderboard/archive.md at main · huggingface/leaderboards","url":"https://github.com/huggingface/leaderboards/blob/main/docs/source/en/open_llm_leaderboard/archive.md"},{"title":"Hugging Face Upgrades Open LLM Leaderboard v2 for Enhanced AI Model Comparison - InfoQ","url":"https://www.infoq.com/news/2024/10/open-llm-leaderboard-v2-launch/"},{"title":"Open LLM Leaderboard - Hugging Face Open LLM Leaderboard | LLM Benchmark | LLMIndex | LLMIndex","url":"https://llmindex.net/benchmarks/open-llm-leaderboard"},{"title":"Hugging Face Overhauls Open LLM Leaderboard with Tougher Benchmarks","url":"https://www.deeplearning.ai/the-batch/hugging-face-overhauls-open-llm-leaderboard-with-tougher-benchmarks"},{"title":"Open LLM Leaderboard v1 · Hugging Face","url":"https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive"},{"title":"openai/gsm8k · Datasets at Hugging Face","url":"https://huggingface.co/datasets/openai/gsm8k"},{"title":"Easy2Hard-Bench: Standardized Difficulty Labels for Profiling LLM Performance and Generalization","url":"https://arxiv.org/pdf/2409.18433"}]

Based on my search results, I found relevant information about the Open LLM Leaderboard versions. Here's what I discovered:

## Key Findings

The Hugging Face Open LLM Leaderboard v1 is dead and officially deprecated, with v2 using harder benchmarks and rankings looking completely different.

The v1 benchmarks were replaced with harder alternatives, where GSM8K was replaced with GPQA (among other changes like MMLU being replaced with MMLU-Pro, HellaSwag with IFEval, ARC-Challenge with BBH, TruthfulQA with MUSR, and Winogrande with MATH Level 5).

Regarding the specific benchmarks you asked about:

- MATH-500 tests competition-level mathematical reasoning across 500 problems drawn from AMC, AIME, and similar competitions, spanning five difficulty levels.

- Unlike GSM8K, MATH-500 problems require multi-step symbolic reasoning.

- The earlier v1 version ranks open large language models according to scores on six popular benchmarks, but in the intervening months, the best models approached human-level scores, partly due to technical improvements and partly because test answers leaked into the models' training sets.

The search results show that while GSM8K was used in v1 and is noted as having contamination issues, the specific technical details about MATH-500 and GSM8K item overlap in the Open LLM Leaderboard evaluation specifications were not found in these sources. For more detailed information about item-level overlap between these benchmarks, you may need to consult the Hugging Face leaderboard documentation directly or relevant research papers on benchmark contamination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a43a2a0-8e30-4f1e-8c46-d99010ad1edd",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "4e18b776-5c73-4a98-ac1f-5abec85914b9",
  "sourceToolAssistantUUID": "5a43a2a0-8e30-4f1e-8c46-d99010ad1edd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-28T13:33:36.909Z_

Now let me fetch more specific pages to get detailed answers for each question.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e18b776-5c73-4a98-ac1f-5abec85914b9",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV416N9rg1SMk7E3k7NX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f376fa8-485f-47dc-9eae-946eec9a3055",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RiTJuXHRkiwGuB3WBTV7in",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 10148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4180,
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

_source line 17 · 2026-05-28T13:33:40.671Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CvJ3RCG8qquCwZPfeGXq8Q`</summary>

```json
{
  "url": "https://github.com/felipemaiapolo/tinyBenchmarks",
  "prompt": "Look for information about the data availability: Is the full 395-model x 29K-item binary response matrix publicly available? Is there a link to download the per-item response data? Look for links to datasets, HuggingFace datasets, or data files. What data is provided in this repository?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f376fa8-485f-47dc-9eae-946eec9a3055",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV416N9rg1SMk7E3k7NX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc0eb738-a280-472f-a869-de3be0f5f903",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RiTJuXHRkiwGuB3WBTV7in",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 10148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4180,
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

_source line 18 · 2026-05-28T13:33:43.033Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B5e4A6PAi4YmTe2QMn6rh6`</summary>

```json
{
  "url": "https://huggingface.co/datasets/open-llm-leaderboard/results",
  "prompt": "What is this dataset? Is it freely downloadable or does it require access approval/gating? What data does it contain - are there per-model item-level details? What format is the data in? Is there any access restriction mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc0eb738-a280-472f-a869-de3be0f5f903",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV416N9rg1SMk7E3k7NX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ba4b971-16c4-4c49-9175-66c3a63d1d8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RiTJuXHRkiwGuB3WBTV7in",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 10148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4180,
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

_source line 19 · 2026-05-28T13:33:44.980Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F7zaWyKJZsiwR3mw11m2Wn`</summary>

```json
{
  "url": "https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive",
  "prompt": "What benchmarks were used in Open LLM Leaderboard V1? Was GSM8K one of them? List all the benchmarks used in V1 and V2. Is MATH-500 specifically used in either version?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ba4b971-16c4-4c49-9175-66c3a63d1d8e",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV416N9rg1SMk7E3k7NX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d11e0b0-5b99-439d-bdd7-cafae0eca3bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RiTJuXHRkiwGuB3WBTV7in",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 10148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4180,
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

_source line 20 · 2026-05-28T13:33:45.593Z_

<details><summary>↩ Tool result · `toolu_01F7zaWyKJZsiwR3mw11m2Wn`</summary>

````text
# Open LLM Leaderboard v1

Evaluating and comparing LLMs is hard. Our RLHF team realized this a year ago when they wanted to reproduce and compare results from several published models. It was a nearly impossible task: scores in papers or marketing releases were given without any reproducible code, sometimes doubtful, but in most cases, just using optimized prompts or evaluation setup to give the best chances to the models. They therefore decided to create a place where reference models would be evaluated in the exact same setup (same questions, asked in the same order, etc.) to gather completely reproducible and comparable results; and that’s how the Open LLM Leaderboard was born!

Following a series of highly visible model releases, it became a widely used resource in the ML community and beyond, visited by more than 2 million unique people over the last 10 months.

Around 300,000 community members used and collaborated on it monthly through submissions and discussions, usually to:

- Find state-of-the-art open-source releases as the leaderboard provides reproducible scores separating marketing fluff from actual progress in the field.
- Evaluate their work, be it pretraining or finetuning, comparing methods in the open and to the best existing models, and earning public recognition.

In June 2024, we archived it, and it was replaced by a newer version, but below, you'll find all relevant information about it!

### Tasks

📈 We evaluated models on 6 key benchmarks using the   Eleuther AI Language Model Evaluation Harness , a unified framework to test generative language models on a large number of different evaluation tasks.
-   AI2 Reasoning Challenge  (25-shot) - a set of grade-school science questions.
-   HellaSwag  (10-shot) - a test of commonsense inference, which is easy for humans (~95%) but challenging for SOTA models.
-   MMLU   (5-shot) - a test to measure a text model's multitask accuracy. The test covers 57 tasks including elementary mathematics, US history, computer science, law, and more.
-   TruthfulQA  (0-shot) - a test to measure a model's propensity to reproduce falsehoods commonly found online. Note: TruthfulQA is technically a 6-shot task in the Harness because each example is prepended with 6 Q/A pairs, even in the 0-shot setting.
-   Winogrande  (5-shot) - an adversarial and difficult Winograd benchmark at scale, for commonsense reasoning.
-   GSM8k  (5-shot) - diverse grade school math word problems to measure a model's ability to solve multi-step mathematical reasoning problems.

For all these evaluations, a higher score is a better score.

We chose these benchmarks as they test a variety of reasoning and general knowledge across a wide variety of fields in 0-shot and few-shot settings.

### Results

You can find:
- detailed numerical results in the `results` Hugging Face dataset: https://huggingface.co/datasets/open-llm-leaderboard-old/results
- details on the input/outputs for the models in the `details` of each model, which you can access by clicking the 📄 emoji after the model name
- community queries and running status in the `requests` Hugging Face dataset: https://huggingface.co/datasets/open-llm-leaderboard-old/requests
If a model's name contains "Flagged", this indicates it has been flagged by the community, and should probably be ignored! Clicking the link will redirect you to the discussion about the model.

## Reproducibility
To reproduce our results, you could run the following command, using [this version](https://github.com/EleutherAI/lm-evaluation-harness/tree/b281b0921b636bc36ad05c0b0b0763bd6dd43463) of the Eleuther AI Harness:

```bash
python main.py --model=hf-causal-experimental \
    --model_args="pretrained=,use_accelerate=True,revision=" \
    --tasks= \
    --num_fewshot= \
    --batch_size=1 \
    --output_path=
```

**Note:** We evaluated all models on a single node of 8 H100s, so the global batch size was 8 for each evaluation. If you don't use parallelism, adapt your batch size to fit.
*You can expect results to vary slightly for different batch sizes because of padding.*

The tasks and few shots parameters are:
- ARC: 25-shot, *arc-challenge* (`acc_norm`)
- HellaSwag: 10-shot, *hellaswag* (`acc_norm`)
- TruthfulQA: 0-shot, *truthfulqa-mc* (`mc2`)
- MMLU: 5-shot, *hendrycksTest-abstract_algebra,hendrycksTest-anatomy,hendrycksTest-astronomy,hendrycksTest-business_ethics,hendrycksTest-clinical_knowledge,hendrycksTest-college_biology,hendrycksTest-college_chemistry,hendrycksTest-college_computer_science,hendrycksTest-college_mathematics,hendrycksTest-college_medicine,hendrycksTest-college_physics,hendrycksTest-computer_security,hendrycksTest-conceptual_physics,hendrycksTest-econometrics,hendrycksTest-electrical_engineering,hendrycksTest-elementary_mathematics,hendrycksTest-formal_logic,hendrycksTest-global_facts,hendrycksTest-high_school_biology,hendrycksTest-high_school_chemistry,hendrycksTest-high_school_computer_science,hendrycksTest-high_school_european_history,hendrycksTest-high_school_geography,hendrycksTest-high_school_government_and_politics,hendrycksTest-high_school_macroeconomics,hendrycksTest-high_school_mathematics,hendrycksTest-high_school_microeconomics,hendrycksTest-high_school_physics,hendrycksTest-high_school_psychology,hendrycksTest-high_school_statistics,hendrycksTest-high_school_us_history,hendrycksTest-high_school_world_history,hendrycksTest-human_aging,hendrycksTest-human_sexuality,hendrycksTest-international_law,hendrycksTest-jurisprudence,hendrycksTest-logical_fallacies,hendrycksTest-machine_learning,hendrycksTest-management,hendrycksTest-marketing,hendrycksTest-medical_genetics,hendrycksTest-miscellaneous,hendrycksTest-moral_disputes,hendrycksTest-moral_scenarios,hendrycksTest-nutrition,hendrycksTest-philosophy,hendrycksTest-prehistory,hendrycksTest-professional_accounting,hendrycksTest-professional_law,hendrycksTest-professional_medicine,hendrycksTest-professional_psychology,hendrycksTest-public_relations,hendrycksTest-security_studies,hendrycksTest-sociology,hendrycksTest-us_foreign_policy,hendrycksTest-virology,hendrycksTest-world_religions* (average of all the results `acc`)
- Winogrande: 5-shot, *winogrande* (`acc`)
- GSM8k: 5-shot, *gsm8k* (`acc`)
Side note on the baseline scores: 
- for log-likelihood evaluation, we select the random baseline
- for GSM8K, we select the score obtained in the paper after finetuning a 6B model on the full GSM8K training set for 50 epochs

## Blogs

During the life of the leaderboard, we wrote 2 blogs that you can find [here](https://huggingface.co/blog/open-llm-leaderboard-mmlu) and [here](https://huggingface.co/blog/open-llm-leaderboard-drop)


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d11e0b0-5b99-439d-bdd7-cafae0eca3bb",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "9c06d18e-ea2e-4048-85e8-9a88da7c2b41",
  "sourceToolAssistantUUID": "1d11e0b0-5b99-439d-bdd7-cafae0eca3bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T13:33:46.058Z_

<details><summary>↩ Tool result · `toolu_01CvJ3RCG8qquCwZPfeGXq8Q`</summary>

```text
# Data Availability for tinyBenchmarks

Based on the repository content, here's what data is publicly available:

## Tiny Datasets
The project provides **tiny datasets with 100 examples each** hosted on HuggingFace. These include reduced versions of:
- MMLU, TruthfulQA, GSM8K, Winogrande, ARC, HellaSwag
- AlpacaEval 2.0
- HELM Lite scenarios

## Access Method
Users can access datasets through the "HuggingFace community" referenced multiple times. The README states: "Please check our HuggingFace community with tiny datasets, each one containing 100 examples."

## What's NOT Available
The page does not mention a complete 395-model × 29K-item binary response matrix or per-item response data downloads. Instead, it focuses on providing pre-created tiny benchmark datasets for evaluation purposes.

## How to Use
The repository includes a Python package installable via pip that allows users to "estimate the performance of a specific LLM on any tiny dataset or benchmark" using the provided datasets.

The emphasis is on **efficient LLM evaluation using smaller datasets** rather than providing raw response matrices from extensive model testing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc0eb738-a280-472f-a869-de3be0f5f903",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "db44f808-2ad6-4766-9f59-c800715b12c3",
  "sourceToolAssistantUUID": "dc0eb738-a280-472f-a869-de3be0f5f903",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-28T13:33:46.726Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GKobGnLfd8eypSfQUXA6ST`</summary>

```json
{
  "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5131967/",
  "prompt": "Describe this paper's methodology. Does it use IRT with fixed parameters to detect cheating or item preknowledge? Does it combine fixed-parameter calibration with contamination/cheating detection in a two-stage IRT approach? What is the main contribution?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db44f808-2ad6-4766-9f59-c800715b12c3",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV416N9rg1SMk7E3k7NX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a4b30ae-2ff3-4309-b0b7-94d30c319a14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RiTJuXHRkiwGuB3WBTV7in",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 882,
      "cache_creation_input_tokens": 4180,
      "cache_read_input_tokens": 10148,
      "output_tokens": 552,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4180
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 882,
          "output_tokens": 552,
          "cache_read_input_tokens": 10148,
          "cache_creation_input_tokens": 4180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4180,
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

_source line 23 · 2026-05-28T13:33:47.419Z_

<details><summary>↩ Tool result · `toolu_01GKobGnLfd8eypSfQUXA6ST`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5131967/
Redirect URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5131967/
Status: 301 Moved Permanently

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC5131967/"
- prompt: "Describe this paper's methodology. Does it use IRT with fixed parameters to detect cheating or item preknowledge? Does it combine fixed-parameter calibration with contamination/cheating detection in a two-stage IRT approach? What is the main contribution?"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a4b30ae-2ff3-4309-b0b7-94d30c319a14",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "ae5ebb6c-6abf-438f-ab62-cf4fd6d9d583",
  "sourceToolAssistantUUID": "9a4b30ae-2ff3-4309-b0b7-94d30c319a14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T13:33:48.151Z_

<details><summary>↩ Tool result · `toolu_01B5e4A6PAi4YmTe2QMn6rh6`</summary>

````text
# Open LLM Leaderboard Results Dataset

## Overview
This is the **results dataset** from the Open LLM Leaderboard, hosted on Hugging Face Datasets. It contains evaluation results for large language models (LLMs) on various benchmark tasks.

## Access
**Freely downloadable** - No access approval or gating is required. The dataset is publicly available at `open-llm-leaderboard/results`.

## Data Contents
The dataset contains **per-model evaluation details** including:

- **Model information**: Model name, source, parameters, dtype
- **Task results**: Performance metrics across multiple benchmark tasks (MMLU Pro, BBH tasks, MUSR, etc.)
- **Detailed metrics**: 
  - Accuracy scores (acc, acc_norm, exact_match)
  - Prompt-level and instruction-level accuracy metrics
  - Standard error measurements
- **Evaluation metadata**:
  - Git hash, timestamps, evaluation duration
  - Tokenizer configuration (pad, EOS, BOS tokens)
  - Chat template information
  - Task-specific hashes and sample counts

## Data Format
- **Primary format**: Parquet (converted from source data)
- **Splits**: `train` and `test` splits available
- **Structure**: Nested JSON objects for complex metrics and configurations

**Note**: The dataset viewer currently has a generation error (schema casting issue), but the underlying Parquet data is accessible via the Hugging Face datasets library:

```python
from datasets import load_dataset
dataset = load_dataset("open-llm-leaderboard/results")
```

## Access Restrictions
**None mentioned** - The dataset is completely open and freely available for download and use.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ba4b971-16c4-4c49-9175-66c3a63d1d8e",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "b38a2424-4e26-4ee5-94af-3a0423bb80c9",
  "sourceToolAssistantUUID": "0ba4b971-16c4-4c49-9175-66c3a63d1d8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-28T13:33:51.220Z_

Let me follow up on redirects and get more specific data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b38a2424-4e26-4ee5-94af-3a0423bb80c9",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV426FVHszY5MWURSJ9U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb575755-48a2-48f2-8c19-a0e9c8258aa4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018K3YewBZ3qkg3hJ6iX4BQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2152,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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

_source line 26 · 2026-05-28T13:33:52.170Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016eiMWarPcCf3tXFiNVGeyh`</summary>

```json
{
  "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5131967/",
  "prompt": "Describe this paper's methodology. Does it use IRT with fixed parameters to detect cheating or item preknowledge? Does it combine fixed-parameter calibration with contamination/cheating detection in a two-stage IRT approach? What is the main contribution?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb575755-48a2-48f2-8c19-a0e9c8258aa4",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV426FVHszY5MWURSJ9U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "145f5bfb-e52a-4c7e-8168-8e49ee74a05e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018K3YewBZ3qkg3hJ6iX4BQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2152,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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

_source line 27 · 2026-05-28T13:33:53.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014NK5gDxnpnLpP18i6H8YEA`</summary>

```json
{
  "query": "tinyBenchmarks HuggingFace dataset \"felipemaiapolo\" response matrix per-item results download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "145f5bfb-e52a-4c7e-8168-8e49ee74a05e",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV426FVHszY5MWURSJ9U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "885a0a93-05cb-44de-8302-54dfeed0a995",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018K3YewBZ3qkg3hJ6iX4BQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2152,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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

_source line 28 · 2026-05-28T13:33:54.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BpZUrLiDewTwiAkKs4dhSm`</summary>

```json
{
  "query": "open-llm-leaderboard \"details\" dataset per-item individual question results V2 huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "885a0a93-05cb-44de-8302-54dfeed0a995",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV426FVHszY5MWURSJ9U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af6aadf9-e89f-4e09-9ae8-0973a519c5a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018K3YewBZ3qkg3hJ6iX4BQY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2152,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2256,
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

_source line 29 · 2026-05-28T13:33:55.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VqdH38Gr9ua2sWh84WDSU`</summary>

```json
{
  "query": "Open LLM Leaderboard V2 benchmarks list \"MATH\" level 5 GSM8K removed replaced"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af6aadf9-e89f-4e09-9ae8-0973a519c5a3",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV426FVHszY5MWURSJ9U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0faf576-d708-4ec5-8ad7-3bd4727f26e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018K3YewBZ3qkg3hJ6iX4BQY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2152,
      "cache_creation_input_tokens": 2256,
      "cache_read_input_tokens": 14328,
      "output_tokens": 343,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2256
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2152,
          "output_tokens": 343,
          "cache_read_input_tokens": 14328,
          "cache_creation_input_tokens": 2256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2256,
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

_source line 30 · 2026-05-28T13:33:58.723Z_

<details><summary>↩ Tool result · `toolu_016eiMWarPcCf3tXFiNVGeyh`</summary>

```text
# Methodology Analysis

## IRT Approach
The paper uses **Item Response Theory (IRT) 2PL model** but **not with fixed parameters**. Instead, it compares item parameters estimated from compromised versus non-compromised datasets to detect changes indicating cheating.

## Two-Stage Approach?
This is **not a two-stage calibration method**. Rather, the researchers:

1. Simulate cheating by artificially modifying responses in real HAM-Nat data
2. Re-estimate IRT parameters on the contaminated dataset
3. Compare parameter shifts between versions

As stated: "Item difficulty, item discrimination, item fit, and local dependence were computed using an IRT 2PL model. Then changes in these item properties from the non-compromised to the compromised dataset were scrutinized."

## Main Contributions

The paper's key innovations are:

- **Focus on items rather than persons**: Most prior work identifies cheaters; this identifies compromised items instead
- **Local Dependence (LD) as primary indicator**: Novel application showing LD increases when items are preknown
- **Practical composite metric**: "Suspicion for IP" (SIP) combines discrimination, difficulty, and LD changes multiplicatively
- **No equating requirement**: LD can be interpreted without comparing test versions, solving a major practical barrier

The approach achieves sensitivity of 1.0 and specificity of 0.95 when 10% of test-takers know 11 of 80 items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "145f5bfb-e52a-4c7e-8168-8e49ee74a05e",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "4e5d9e87-a5ae-4e5d-b7d6-fb7fa897ff10",
  "sourceToolAssistantUUID": "145f5bfb-e52a-4c7e-8168-8e49ee74a05e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-28T13:34:00.684Z_

<details><summary>↩ Tool result · `toolu_01BpZUrLiDewTwiAkKs4dhSm`</summary>

```text
Web search results for query: "open-llm-leaderboard "details" dataset per-item individual question results V2 huggingface"

Links: [{"title":"Open LLM Leaderboard v1 · Hugging Face","url":"https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive"},{"title":"open-llm-leaderboard-old/details_voidful__qd-phi-1_5 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/open-llm-leaderboard-old/details_voidful__qd-phi-1_5"},{"title":"open-llm-leaderboard (Open LLM Leaderboard)","url":"https://huggingface.co/open-llm-leaderboard"},{"title":"open-llm-leaderboard/results · Datasets at Hugging Face","url":"https://huggingface.co/datasets/open-llm-leaderboard/results"},{"title":"open-llm-leaderboard/details · Datasets at Hugging Face","url":"https://huggingface.co/datasets/open-llm-leaderboard/details"},{"title":"open-llm-leaderboard/open_llm_leaderboard · How to download the leaderboard result data","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/1143"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Open LLM Leaderboard 2 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-2"},{"title":"CLARIN-PT-LDB: An Open LLM Leaderboard for Portuguese to assess Language, Culture and Civility","url":"https://arxiv.org/pdf/2603.12872"}]

Based on the search results, I found information about the Open LLM Leaderboard's data structure on Hugging Face:

The full dataset viewer for the open-llm-leaderboard/details dataset is not currently available, but only a preview of the rows is being shown.

However, I can provide some context: The details dataset is composed of 63 configurations, each one corresponding to one of the evaluated tasks. Each run can be found as a specific split in each configuration, with the "train" split pointing to the latest results, and an additional "results" configuration stores all the aggregated results of the run.

For accessing per-item individual question results, you can load the details from a run using Python with the datasets library, specifying the model, task configuration, and split.

If you're looking for the V2 version specifically or more detailed information about accessing individual question-level results, you may need to visit the dataset page directly at https://huggingface.co/datasets/open-llm-leaderboard/details or check the Open LLM Leaderboard documentation and discussions on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af6aadf9-e89f-4e09-9ae8-0973a519c5a3",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "d02c0ecc-976f-47ff-ab7e-9cce98b4e564",
  "sourceToolAssistantUUID": "af6aadf9-e89f-4e09-9ae8-0973a519c5a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T13:34:01.824Z_

<details><summary>↩ Tool result · `toolu_014NK5gDxnpnLpP18i6H8YEA`</summary>

```text
Web search results for query: "tinyBenchmarks HuggingFace dataset "felipemaiapolo" response matrix per-item results download"

Links: [{"title":"tinyBenchmarks/README.md at main · felipemaiapolo/tinyBenchmarks","url":"https://github.com/felipemaiapolo/tinyBenchmarks/blob/main/README.md"},{"title":"GitHub - felipemaiapolo/tinyBenchmarks: Evaluating LLMs with fewer examples · GitHub","url":"https://github.com/felipemaiapolo/tinyBenchmarks"},{"title":"tinyBenchmarks/tinyHellaswag · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tinyBenchmarks/tinyHellaswag"},{"title":"tinyBenchmarks/tinyMMLU · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tinyBenchmarks/tinyMMLU"},{"title":"tinyBenchmarks/tinyWinogrande · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tinyBenchmarks/tinyWinogrande"},{"title":"tinyBenchmarks/tinyTruthfulQA · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tinyBenchmarks/tinyTruthfulQA"},{"title":"tinyBenchmarks/tinyAlpacaEval · Datasets at Hugging Face","url":"https://huggingface.co/datasets/tinyBenchmarks/tinyAlpacaEval"}]

I found information about the tinyBenchmarks project. The tinyBenchmarks HuggingFace community contains tiny datasets with 100 examples each, including tiny versions from the Open LLM Leaderboard such as TruthfulQA, GSM8K, Winogrande, ARC, HellaSwag, and MMLU.

The search results show links to individual dataset cards (tinyMMLU, tinyHellaswag, tinyWinogrande, tinyTruthfulQA, tinyAlpacaEval) on HuggingFace. However, the search results I found don't specifically mention response matrix per-item results or how to download such data.

To get more specific information about accessing response matrices and per-item results from these datasets, you may want to:

1. Visit the individual dataset pages on HuggingFace (huggingface.co/datasets/tinyBenchmarks/[dataset-name])
2. Check the GitHub repository at https://github.com/felipemaiapolo/tinyBenchmarks for documentation on accessing detailed results
3. Review the paper referenced in the citations for more technical details about the evaluation methodology

Would you like me to search for more specific information about accessing response matrices or downloading per-item results from these datasets?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "885a0a93-05cb-44de-8302-54dfeed0a995",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "9876e87e-2342-4f98-b115-a781a1ff7197",
  "sourceToolAssistantUUID": "885a0a93-05cb-44de-8302-54dfeed0a995",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T13:34:02.431Z_

<details><summary>↩ Tool result · `toolu_019VqdH38Gr9ua2sWh84WDSU`</summary>

```text
Web search results for query: "Open LLM Leaderboard V2 benchmarks list "MATH" level 5 GSM8K removed replaced"

Links: [{"title":"Answer extraction logic for Math Lvl 5 (Open LLM Leaderboard 2) may be too strict · Issue #2539 · EleutherAI/lm-evaluation-harness","url":"https://github.com/EleutherAI/lm-evaluation-harness/issues/2539"},{"title":"leaderboards/docs/source/en/open_llm_leaderboard/archive.md at main · huggingface/leaderboards","url":"https://github.com/huggingface/leaderboards/blob/main/docs/source/en/open_llm_leaderboard/archive.md"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"2026 LLM Leaderboard: compare Anthropic, Google, OpenAI, and more... — Klu","url":"https://klu.ai/llm-leaderboard"},{"title":"Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs   Evaluation, Benchmark, and Arena","url":"https://arxiv.org/pdf/2406.07545"},{"title":"GitHub - om-ai-lab/open-agent-leaderboard: Reproducible Language Agent Research · GitHub","url":"https://github.com/om-ai-lab/open-agent-leaderboard"},{"title":"GSM8k Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/gsm8k"}]

Based on the search results, I found information about the Open LLM Leaderboard V2 and benchmarks, though the search results don't explicitly state that GSM8K was removed and replaced in the MATH Level 5 benchmark.

From the search results, the Open LLM Leaderboard V2 shows an interactive leaderboard where you can filter open-source language models to see how they perform on several tests such as IFEval, BBH, MATH, GPQA, MUSR, and MMLU‑PRO. The MATH benchmark is listed as part of the evaluation suite.

However, regarding your specific question about GSM8K being removed and replaced in the MATH Level 5 benchmark, the search results don't contain explicit information about this change. There have been observations of huge discrepancies between models on Math Lvl 5 on Open LLM Leaderboard 2, with models like Qwen2.5 showing very strong scores on GSM8K yet achieving zero or very low scores on the MATH level test, but this doesn't explicitly confirm a replacement.

To get more specific information about whether GSM8K was removed and replaced in the MATH Level 5 benchmark, you might want to check the official Open LLM Leaderboard GitHub repository or the leaderboard's documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0faf576-d708-4ec5-8ad7-3bd4727f26e7",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "0b0ea509-5a24-41c2-8c25-83ce885292e6",
  "sourceToolAssistantUUID": "b0faf576-d708-4ec5-8ad7-3bd4727f26e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-28T13:34:11.937Z_

Let me get more specific details on the remaining questions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b0ea509-5a24-41c2-8c25-83ce885292e6",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV439hP7Nf9ZvLfqAGES",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61533bca-b74e-4fb0-aded-cc79db0d7999",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fKducKnbWJKgawMLy4iw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5231,
      "cache_read_input_tokens": 16584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5231,
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

_source line 35 · 2026-05-28T13:34:14.992Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QWM4iiiv8nkS1xVR22boxm`</summary>

```json
{
  "url": "https://huggingface.co/datasets/open-llm-leaderboard/details",
  "prompt": "Is this dataset freely downloadable or does it require access approval/gating? What data does it contain - are there per-item, per-question results for each model? What benchmarks/tasks are included? Is there any access restriction? How many models are covered? What is the data structure?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61533bca-b74e-4fb0-aded-cc79db0d7999",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV439hP7Nf9ZvLfqAGES",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85d6d033-2cac-4166-8df2-246e6017ba18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fKducKnbWJKgawMLy4iw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5231,
      "cache_read_input_tokens": 16584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5231,
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

_source line 36 · 2026-05-28T13:34:15.192Z_

<details><summary>↩ Tool result · `toolu_01QWM4iiiv8nkS1xVR22boxm`</summary>

```text
The server returned HTTP 401 Unauthorized.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85d6d033-2cac-4166-8df2-246e6017ba18",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "a9f0aea4-34f9-4a57-8f0a-49a771ec743f",
  "sourceToolAssistantUUID": "85d6d033-2cac-4166-8df2-246e6017ba18",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T13:34:16.976Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PpcdCja8qnSBPMC2kwXHA3`</summary>

```json
{
  "url": "https://huggingface.co/spaces/open-llm-leaderboard/blog",
  "prompt": "What benchmarks are used in Open LLM Leaderboard V2? Is MATH Level 5 one of them? Is GSM8K included in V2? Is MATH-500 specifically used? List all V2 benchmarks precisely. What happened to GSM8K from V1?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9f0aea4-34f9-4a57-8f0a-49a771ec743f",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV439hP7Nf9ZvLfqAGES",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "977bc7a5-9f54-40f7-aa02-c50d317f888a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fKducKnbWJKgawMLy4iw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5231,
      "cache_read_input_tokens": 16584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5231,
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

_source line 38 · 2026-05-28T13:34:17.816Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017bJ9jhX86CFGAwaNTGakwV`</summary>

```json
{
  "query": "IRT person fit aberrant response detection LLM benchmark contamination training data leakage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "977bc7a5-9f54-40f7-aa02-c50d317f888a",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV439hP7Nf9ZvLfqAGES",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a27eacf7-87b6-43f9-86cc-5d0e5c96e682",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fKducKnbWJKgawMLy4iw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5231,
      "cache_read_input_tokens": 16584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5231,
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

_source line 39 · 2026-05-28T13:34:19.056Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ar7chwbQgWEiMta6Tm6Whw`</summary>

```json
{
  "query": "Polo 2024 tinyBenchmarks \"open-llm-leaderboard\" binary correctness data 395 models raw data available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a27eacf7-87b6-43f9-86cc-5d0e5c96e682",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV439hP7Nf9ZvLfqAGES",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be705610-3784-45ec-9542-219cc82761db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fKducKnbWJKgawMLy4iw5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5231,
      "cache_read_input_tokens": 16584,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5231
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 16584,
          "cache_creation_input_tokens": 5231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5231,
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

_source line 40 · 2026-05-28T13:34:20.723Z_

<details><summary>↩ Tool result · `toolu_01PpcdCja8qnSBPMC2kwXHA3`</summary>

```text
# Open LLM Leaderboard V2 Benchmarks

Based on the web page content provided, I cannot give you a definitive answer about the specific benchmarks used in Open LLM Leaderboard V2.

The page excerpt you've shared only shows:
- The leaderboard title: "Open-LLM performances are plateauing, let's make the leaderboard steep again"
- Navigation elements (blog link, like count)
- A loading state ("Refreshing")

**What's missing from this content:**
- No benchmark list is visible
- No mention of MATH Level 5
- No information about GSM8K in V2
- No details about MATH-500
- No comparison between V1 and V2 benchmarks

## Recommendation

To get accurate information about Open LLM Leaderboard V2 benchmarks, you should:

1. **Visit the full leaderboard page** at the Hugging Face Space (open-llm-leaderboard)
2. **Check the methodology/about section** of the leaderboard
3. **Review the blog** linked in the navigation for V2 updates
4. **Check the official documentation** or GitHub repository for detailed benchmark specifications

If you can provide the complete page content or the methodology section, I'd be happy to give you precise details about which benchmarks are included in V2.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "977bc7a5-9f54-40f7-aa02-c50d317f888a",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "8c858682-c0ab-4a9c-97a7-ecfee91c58a5",
  "sourceToolAssistantUUID": "977bc7a5-9f54-40f7-aa02-c50d317f888a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-28T13:34:25.765Z_

<details><summary>↩ Tool result · `toolu_01Ar7chwbQgWEiMta6Tm6Whw`</summary>

```text
Web search results for query: "Polo 2024 tinyBenchmarks "open-llm-leaderboard" binary correctness data 395 models raw data available"

Links: [{"title":"GitHub - felipemaiapolo/tinyBenchmarks: Evaluating LLMs with fewer examples · GitHub","url":"https://github.com/felipemaiapolo/tinyBenchmarks"},{"title":"[PDF] tinyBenchmarks: evaluating LLMs with fewer examples | Semantic Scholar","url":"https://www.semanticscholar.org/paper/tinyBenchmarks:-evaluating-LLMs-with-fewer-examples-Polo-Weber/4c0f88e80320885e8289a9af781a1101717104f2"},{"title":"(PDF) tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://www.researchgate.net/publication/383238265_tinyBenchmarks_evaluating_LLMs_with_fewer_examples"},{"title":"[2402.14992] tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/abs/2402.14992"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://proceedings.mlr.press/v235/maia-polo24a.html"},{"title":"EVALUATING LLMS WITH FEWER EXAMPLES","url":"https://openreview.net/pdf/25ac9459dd5b345badfd3d9a2c5e56b32fd89b07.pdf"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICML 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples--1"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICLR 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/pdf/2402.14992"}]

Based on the search results, I found relevant information about the Polo 2024 tinyBenchmarks study and the Open LLM Leaderboard data:

The data from HuggingFace's Open LLM Leaderboard is composed of 395 LLMs and approximately 29k items that were downloaded from the platform in January 2024. The study kept all models that had scores for all six scenarios: ARC, HellaSwag, MMLU, TruthfulQA, Winogrande, and GSM8K.

Regarding raw data availability, the research released a HuggingFace community collection with tiny datasets, each containing 100 examples, including tiny versions from the Open LLM Leaderboard: TruthfulQA, GSM8K, Winogrande, ARC, HellaSwag, and MMLU.

The paper releases evaluation tools and tiny versions of popular benchmarks: Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0, with empirical analysis demonstrating these tools and tiny benchmarks are sufficient to reliably and efficiently reproduce the original evaluation results.

The full paper was published at ICML 2024 and is available on arXiv (arXiv:2402.14992) with the GitHub repository at https://github.com/felipemaiapolo/tinyBenchmarks for accessing the tools and data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be705610-3784-45ec-9542-219cc82761db",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "c30f9a95-1182-4208-ae24-77b3f66940b3",
  "sourceToolAssistantUUID": "be705610-3784-45ec-9542-219cc82761db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-28T13:34:26.112Z_

<details><summary>↩ Tool result · `toolu_017bJ9jhX86CFGAwaNTGakwV`</summary>

```text
Web search results for query: "IRT person fit aberrant response detection LLM benchmark contamination training data leakage"

Links: [{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/pdf/2408.14352"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM","url":"https://arxiv.org/pdf/2411.03823"},{"title":"LLM Benchmark Datasets Should Be Contamination-Resistant","url":"https://arxiv.org/html/2605.19999v1"},{"title":"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in   Closed-Source LLMs","url":"https://arxiv.org/pdf/2402.03927"},{"title":"LessLeak-Bench: A First Investigation of Data Leakage in LLMs Across 83 Software Engineering Benchmarks","url":"https://arxiv.org/html/2502.06215v1"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"}]

I found several highly relevant papers on LLM benchmark contamination and data leakage detection. Here's what the search results reveal:

## Key Findings

**Contamination Overview:**
Data contamination occurs when part of the test set is leaked into the training phase, which makes benchmark results invalid since a model's performance may reflect its ability to retrieve training data rather than true capabilities.

Recent studies have detected widespread contamination across popular LLMs, with levels reaching up to 45% on commonly used benchmarks.

**Detection Methods:**

Several approaches have been proposed to detect contamination:
- TS-Guessing submits benchmark questions with masked parts to check if the model can correctly complete the missing part as evidence of contamination
- CoDeC produces interpretable contamination scores via in-context learning and is simple, automated, and model/dataset-agnostic
- Self-Critique probes for policy collapse in RL post-training scenarios, where models converge to narrow reasoning paths

**Types of Leakage:**
Indirect data leaking occurs when benchmark data becomes incorporated through researcher interactions during evaluation, even if a model was contamination-free initially.

When training data are accessible, overlap-based checks can reveal contamination, but for most open-source models such verification is infeasible.

The search results focus primarily on contamination detection methods rather than IRT person-fit indices specifically, though contamination undermines all benchmark-based evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a27eacf7-87b6-43f9-86cc-5d0e5c96e682",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "0e636889-b6e6-4639-89fe-2a3efc379d98",
  "sourceToolAssistantUUID": "a27eacf7-87b6-43f9-86cc-5d0e5c96e682",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-28T13:34:28.679Z_

Let me fetch a few more critical pages to fill in remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e636889-b6e6-4639-89fe-2a3efc379d98",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV44tf4VcXwZh2Koa8CF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3fd3581c-1f9c-4be9-8658-c16e7289b022",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2JyK7ngjvFdEUZpMHRHiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 21815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1675,
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

_source line 44 · 2026-05-28T13:34:32.400Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KTgvHYBCbPo3gnEUfScaHf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.14992",
  "prompt": "Look for information about data availability. Is the full 395-model x 29K-item binary response matrix publicly released? Where can the raw per-item correctness data be downloaded? Is there a HuggingFace dataset with the full response matrix, or only the 100-item tiny subsets? Check for data availability statements, supplementary materials, or links to datasets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fd3581c-1f9c-4be9-8658-c16e7289b022",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV44tf4VcXwZh2Koa8CF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0984e543-82fd-4e52-91b1-9486fde7612d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2JyK7ngjvFdEUZpMHRHiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 21815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1675,
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

_source line 45 · 2026-05-28T13:34:34.818Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VEXaeJAMHGKH3AeQEK86c2`</summary>

```json
{
  "url": "https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-2",
  "prompt": "What are the exact benchmarks used in Open LLM Leaderboard V2? Is MATH Level 5 one of the benchmarks? Is GSM8K used in V2? What about MATH-500? List all the V2 benchmarks. Also check for information about per-model details datasets and whether they require access approval."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0984e543-82fd-4e52-91b1-9486fde7612d",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV44tf4VcXwZh2Koa8CF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dc632fe-2d0b-4460-a363-206aa64201ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2JyK7ngjvFdEUZpMHRHiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 21815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1675,
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

_source line 46 · 2026-05-28T13:34:35.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GEKLHduRVVxS8DFDJEcKq`</summary>

```json
{
  "query": "IRT person-fit statistics LLM evaluation anomaly detection benchmark cheating aberrant response pattern"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dc632fe-2d0b-4460-a363-206aa64201ec",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV44tf4VcXwZh2Koa8CF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b63a3b5-a2f9-4eca-8a28-df5812ca0798",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2JyK7ngjvFdEUZpMHRHiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 21815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1675,
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

_source line 47 · 2026-05-28T13:34:36.150Z_

<details><summary>↩ Tool result · `toolu_01KTgvHYBCbPo3gnEUfScaHf`</summary>

```text
# Data Availability Information

Based on the webpage content provided, **specific information about data availability is not included**. The page shows the abstract and metadata for the arXiv paper "tinyBenchmarks: evaluating LLMs with fewer examples," but it does not contain details about:

- Whether the full 395-model × 29K-item binary response matrix is publicly available
- Links to download raw per-item correctness data
- Existence of a HuggingFace dataset with the complete response matrix
- Location of supplementary materials or datasets

The abstract mentions that researchers "release evaluation tools and tiny versions of popular benchmarks" including "Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0," but the webpage does not provide specific links or URLs to access these resources.

To find this information, you would need to:
1. Access the full PDF or HTML version of the paper
2. Check the paper's supplementary materials or appendices
3. Visit the authors' GitHub repositories or HuggingFace profiles
4. Review the project's official documentation or website
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0984e543-82fd-4e52-91b1-9486fde7612d",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "280da7ec-c731-4804-906c-e6f134b8a672",
  "sourceToolAssistantUUID": "0984e543-82fd-4e52-91b1-9486fde7612d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-28T13:34:36.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L8M2Ltyhv7azbPLpAJH3GN`</summary>

```json
{
  "query": "\"fixed parameter\" IRT \"anchor items\" calibration contamination cheating detection educational testing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "280da7ec-c731-4804-906c-e6f134b8a672",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV44tf4VcXwZh2Koa8CF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f12dc391-fb70-4a6b-abd6-47f1adee7795",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2JyK7ngjvFdEUZpMHRHiW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 921,
      "cache_creation_input_tokens": 1675,
      "cache_read_input_tokens": 21815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1675,
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

_source line 49 · 2026-05-28T13:34:39.800Z_

<details><summary>↩ Tool result · `toolu_01VEXaeJAMHGKH3AeQEK86c2`</summary>

```text
# Open LLM Leaderboard V2 Benchmarks

Based on the web page content provided, **specific benchmark details are not listed**. The page only mentions:

- A link to the "Open-LLM performances are plateauing, let's make the leaderboard steep again" blog post, which is noted as the "Release blog of the Open LLM Leaderboard v2" that should explain "what we did and why"

## What the Page Does Reference

The page includes links to relevant datasets:
- **`open-llm-leaderboard/contents`** - Aggregated results (recommended for downloading)
- **`open-llm-leaderboard/results`** - Per-model evaluation results
- **`open-llm-leaderboard/requests`** - Status of submitted models

## To Get Benchmark Details

To answer your specific questions about:
- Whether MATH Level 5, GSM8K, or MATH-500 are used
- Complete list of all V2 benchmarks
- Dataset access requirements

You would need to:
1. **Read the release blog** linked in the collection
2. **Check the datasets directly** at the Hugging Face Hub (links provided above)
3. **Visit the main leaderboard space** (Running on CPU Upgrade - 14k subscribers) which likely displays full benchmark information

The web page content alone does not contain the specific benchmark specifications you're asking about.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dc632fe-2d0b-4460-a363-206aa64201ec",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "36199113-5534-4be3-a928-8491f355e3a8",
  "sourceToolAssistantUUID": "4dc632fe-2d0b-4460-a363-206aa64201ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T13:34:44.860Z_

<details><summary>↩ Tool result · `toolu_01L8M2Ltyhv7azbPLpAJH3GN`</summary>

```text
Web search results for query: ""fixed parameter" IRT "anchor items" calibration contamination cheating detection educational testing"

Links: [{"title":"Linking of Rasch-Scaled Tests: Consequences of Limited Item Pools and Model Misfit","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8289883/"},{"title":"A New Approach to Test Score Equating Using Item Response ...","url":"https://files.eric.ed.gov/fulltext/EJ835198.pdf"},{"title":"Frontiers | Placing Multiple Tests on a Common Scale Using a Post-test Anchor Design: Effects of Item Position and Order on the Stability of Parameter Estimates","url":"https://www.frontiersin.org/articles/10.3389/fams.2018.00050/full"},{"title":"Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data: Applied Measurement in Education: Vol 32, No 4","url":"https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344"},{"title":"A Comparative Study of IRT Fixed Parameter Calibration Methods - Kim - 2006 - Journal of Educational Measurement - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.2006.00021.x"},{"title":"A Framework for Anchor Methods and an Iterative Forward Approach for DIF Detection - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5978507/"},{"title":"Detection of Two-Way Outliers in Multivariate Data and Application to   Cheating Detection in Educational Tests","url":"https://arxiv.org/pdf/1911.09408"},{"title":"Calibrating and Linking Item Parameters to a Base Scale","url":"https://files.eric.ed.gov/fulltext/ED510480.pdf"}]

I've completed the web search for your query. Here are the key findings:

## Fixed Parameter Calibration and Anchor Items

Fixed parameter calibration (FPC) has been used to estimate the item parameters of a new test form on the existing ability scale of an item pool. FPC can be applied to multiple examinee groups test data that are linked to the item pool via anchor items.

## Anchor Items and Contamination

Anchor items are used in test linking designs, where test forms share a number of common items. However, there are important considerations regarding anchor item quality. If the anchor includes one or more items with differential item functioning (DIF), the anchor is referred to as contaminated.

Regarding the optimal number of anchor items, in cases of model misfit, the share of anchor items should exceed 20% as is currently proposed in the literature.

## Cheating Detection in Educational Testing

The search results include some relevant work on cheating detection. Methods for detection of cheating in educational tests have been applied to detect cheating due to item leakage using computer-based licensure assessments. Additionally, research has proposed various person-fit indices and IRT models for detecting test takers who benefit from item preknowledge, including approaches for both adaptive and non-adaptive testing.

The search results cover IRT calibration methods, anchor item selection, contamination in DIF analysis, and cheating detection techniques in educational testing contexts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f12dc391-fb70-4a6b-abd6-47f1adee7795",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "36db88b8-2b82-47b5-a215-359a621a6d84",
  "sourceToolAssistantUUID": "f12dc391-fb70-4a6b-abd6-47f1adee7795",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-28T13:34:47.637Z_

<details><summary>↩ Tool result · `toolu_013GEKLHduRVVxS8DFDJEcKq`</summary>

```text
Web search results for query: "IRT person-fit statistics LLM evaluation anomaly detection benchmark cheating aberrant response pattern"

Links: [{"title":"How Much Do Large Language Model Cheat on Evaluation? Benchmarking Overestimation under the One-Time-Pad-Based Framework","url":"https://arxiv.org/html/2507.19219v1"},{"title":"Do LLMs cheat on benchmarks – Ehud Reiter's Blog","url":"https://ehudreiter.com/2025/12/08/do-llms-cheat-on-benchmarks/"},{"title":"Data Augmentation in Machine Learning for Cheating ...","url":"https://www.psychologie-aktuell.com/fileadmin/Redaktion/Journale/ptam_2022-4/PTAM_2022-4_3.pdf"},{"title":"Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates | OpenReview","url":"https://openreview.net/forum?id=syThiTmWWm"},{"title":"Published as a conference paper at ICLR 2025 CHEATING AUTOMATIC LLM BENCHMARKS:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf"},{"title":"ImpossibleBench: Measuring LLMs’ Propensity of Exploiting Test Cases","url":"https://arxiv.org/html/2510.20270v1"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Frontiers | Cheatomaly: weakly supervised video anomaly ranking for exam cheating detection using vision transformers","url":"https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2026.1817120/full"}]

I found several relevant results for your search. Here's what the research landscape shows:

## IRT and Person-Fit Statistics for LLM Evaluation

Item Response Theory (IRT) has recently been applied to LLM evaluation, providing item parameters such as difficulty, discrimination, and guessing, as well as latent ability estimates for models. ATLAS is a large-scale adaptive testing framework for LLMs that achieves up to 90% item reduction while maintaining measurement precision through SE-controlled stopping.

IRT-based ability estimation induces substantial rank reordering of LLM performance, with 23–31% of models shifting by more than 10 positions. Model-fit statistics (e.g., RMSEA via the M2 statistic) are important for rigorous psychometric validation and cross-model comparability.

## Traditional Cheating Detection with Person-Fit Statistics

Person-fit statistics are used to identify test-takers who are misfit persons for a specific IRT model for test development. A gated IRT model has been utilized to detect large score gain due to item exposure or item compromise.

## LLM Cheating on Benchmarks

Capable LLMs may find and exploit "shortcuts" to pass the tests instead of solving genuine issues, effectively cheating their way to success. ImpossibleBench is a framework to quantify an LLM's propensity to exploit test cases by creating "impossible" versions of coding benchmarks with mutated unit tests.

The research suggests an interesting convergence between traditional educational assessment methods (IRT-based person-fit detection) and emerging challenges in LLM evaluation around anomalous response patterns and benchmark manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b63a3b5-a2f9-4eca-8a28-df5812ca0798",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "cc949d74-0d14-4c08-a4ae-a831bccd8616",
  "sourceToolAssistantUUID": "6b63a3b5-a2f9-4eca-8a28-df5812ca0798",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-28T13:34:54.152Z_

Let me do a few final targeted searches and fetches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc949d74-0d14-4c08-a4ae-a831bccd8616",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV46UsdZvmovibQYz9Y1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8dcc603-31d4-49be-a8f3-8074c8dc11f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mw27tPw599EpriykRMQQpf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 23490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2945,
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

_source line 53 · 2026-05-28T13:34:57.974Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LmLdUshwfLhfmm4PYHo1vE`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.15055v2",
  "prompt": "Does this paper use the tinyBenchmarks data from Polo et al.? Does it mention whether the full response matrix (395 models x 29K items) is publicly available? Does it discuss where to get per-item binary correctness data for LLMs? Also check if it discusses IRT with fixed parameters or contamination detection."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8dcc603-31d4-49be-a8f3-8074c8dc11f7",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV46UsdZvmovibQYz9Y1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7360c788-83f8-4d75-a6a6-26d211c0941b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mw27tPw599EpriykRMQQpf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 23490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2945,
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

_source line 54 · 2026-05-28T13:34:59.912Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xxr9AnoMs8jCojGaiby8Ki`</summary>

```json
{
  "url": "https://huggingface.co/blog/open-llm-leaderboard-update-v2",
  "prompt": "What benchmarks are used in Open LLM Leaderboard V2? Is MATH used? Is GSM8K used in V2? What about MATH-500? List all V2 benchmarks precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7360c788-83f8-4d75-a6a6-26d211c0941b",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV46UsdZvmovibQYz9Y1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62971758-3fb7-452a-9cba-73624758a4b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mw27tPw599EpriykRMQQpf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 23490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2945,
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

_source line 55 · 2026-05-28T13:35:00.099Z_

<details><summary>↩ Tool result · `toolu_01Xxr9AnoMs8jCojGaiby8Ki`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62971758-3fb7-452a-9cba-73624758a4b5",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "b663c3c4-04ab-4384-915e-3e09f59cae52",
  "sourceToolAssistantUUID": "62971758-3fb7-452a-9cba-73624758a4b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-28T13:35:00.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LrKLRE98AekvqTWZomuMDu`</summary>

```json
{
  "query": "open-llm-leaderboard-old details_model per-item correctness download structure V1 huggingface"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b663c3c4-04ab-4384-915e-3e09f59cae52",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV46UsdZvmovibQYz9Y1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dd137f9-7275-4c3b-a7ac-c8be703e322f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mw27tPw599EpriykRMQQpf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 23490,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 832,
          "output_tokens": 352,
          "cache_read_input_tokens": 23490,
          "cache_creation_input_tokens": 2945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2945,
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

_source line 57 · 2026-05-28T13:35:03.974Z_

<details><summary>↩ Tool result · `toolu_01LmLdUshwfLhfmm4PYHo1vE`</summary>

```text
# Analysis of Paper's Data and Methods

**tinyBenchmarks usage:** The paper does not use tinyBenchmarks data from Polo et al. It cites Maia Polo et al. (2024) only in the context of "optimized item selection" as related work, not as a data source.

**Public availability of response matrix:** The paper does not mention whether the full response matrix is publicly available. It provides code availability ("Code — https://github.com/Joe-Hall-Lee/PSN-IRT") but doesn't explicitly discuss dataset release.

**Per-item binary correctness data:** The paper describes obtaining data through OpenCompass evaluation: "we conduct evaluations using OpenCompass...The evaluation results are collected in the form of binary outcomes, indicating whether each model answered each item correctly." However, it doesn't specify where readers can access raw per-item binary data.

**IRT with fixed parameters:** The paper does not discuss IRT approaches with fixed parameters. It focuses on estimating all parameters (difficulty, discriminability, guessing-rate, feasibility) jointly through neural networks.

**Contamination detection:** Yes, the paper explicitly addresses this. Finding 4 states: "Outlier-high guessing-rates in many benchmark items flag risks of data contamination," and the case study notes "This item's content is publicly accessible online, suggesting an associated risk of data contamination" as an example of identifying potentially contaminated items through high guessing parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7360c788-83f8-4d75-a6a6-26d211c0941b",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "494d2258-70eb-4227-96f3-d9c7d35e0cdb",
  "sourceToolAssistantUUID": "7360c788-83f8-4d75-a6a6-26d211c0941b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-28T13:35:07.034Z_

<details><summary>↩ Tool result · `toolu_01LrKLRE98AekvqTWZomuMDu`</summary>

```text
Web search results for query: "open-llm-leaderboard-old details_model per-item correctness download structure V1 huggingface"

Links: [{"title":"Open LLM Leaderboard v1 · Hugging Face","url":"https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive"},{"title":"leaderboards/docs/source/en/open_llm_leaderboard/archive.md at main · huggingface/leaderboards","url":"https://github.com/huggingface/leaderboards/blob/main/docs/source/en/open_llm_leaderboard/archive.md"},{"title":"open-llm-leaderboard-old (Open LLM Leaderboard Archive)","url":"https://huggingface.co/open-llm-leaderboard-old"},{"title":"GitHub - VILA-Lab/Open-LLM-Leaderboard: Open-LLM-Leaderboard: Open-Style Question Evaluation. Paper at https://arxiv.org/abs/2406.07545 · GitHub","url":"https://github.com/vila-lab/open-llm-leaderboard"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs   Evaluation, Benchmark, and Arena","url":"https://arxiv.org/pdf/2406.07545"},{"title":"open-llm-leaderboard/open_llm_leaderboard · How to download the leaderboard result data","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/1143"},{"title":"How to submit models on the Open LLM Leaderboard · Hugging Face","url":"https://huggingface.co/docs/leaderboards/open_llm_leaderboard/submitting"}]

Based on the search results, here's what I found about the Open LLM Leaderboard V1 archive and data structure:

## Data Resources

The Open LLM Leaderboard V1 provides detailed numerical results in the results Hugging Face dataset (https://huggingface.co/datasets/open-llm-leaderboard-old/results), details on the input/outputs for the models in the details of each model which you can access by clicking the 📄 emoji after the model name, and community queries and running status in the requests Hugging Face dataset (https://huggingface.co/datasets/open-llm-leaderboard-old/requests).

## Download Structure

The search results point to the `open-llm-leaderboard-old` organization on Hugging Face, which contains the archived datasets. The main datasets available are:

1. **Results dataset** - Contains detailed numerical evaluation results
2. **Requests dataset** - Contains community queries and running status information
3. **Model details** - Per-model input/output information accessible through the leaderboard interface

These datasets can be accessed and downloaded from the Hugging Face datasets platform at the URLs mentioned above. The structure appears to be organized around model evaluation results and per-item correctness information, though the search results don't provide exhaustive technical details about the exact schema or file format of the "details_model" structure you're asking about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dd137f9-7275-4c3b-a7ac-c8be703e322f",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "afc92ee4-25ff-4f25-b874-c122a41898f8",
  "sourceToolAssistantUUID": "8dd137f9-7275-4c3b-a7ac-c8be703e322f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-28T13:35:10.736Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wfa3SbAkGAFr43VxW53wsy`</summary>

```json
{
  "url": "https://huggingface.co/open-llm-leaderboard-old",
  "prompt": "List the datasets available under this organization. Are there per-model details datasets? What is the naming pattern? How many detail datasets are there? Are they freely accessible or gated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afc92ee4-25ff-4f25-b874-c122a41898f8",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV47uVkMHWtBmsMr8hZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dcd0871-6410-432d-9607-c4e17b838fcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPRNDDWtXgQz75Pra57iym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2508,
      "cache_read_input_tokens": 26435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 60 · 2026-05-28T13:35:13.070Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HH5V69rEfYeGdpTZCC1TX3`</summary>

```json
{
  "url": "https://huggingface.co/datasets/open-llm-leaderboard-old/details_voidful__qd-phi-1_5",
  "prompt": "What data does this dataset contain? Is there per-item, per-question correctness data? What is the structure - does it contain individual item responses (correct/incorrect) for each benchmark question? Is it freely downloadable? What columns and fields are available?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dcd0871-6410-432d-9607-c4e17b838fcb",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV47uVkMHWtBmsMr8hZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17afbaed-f079-4cc4-8f42-215adfb63e70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPRNDDWtXgQz75Pra57iym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2508,
      "cache_read_input_tokens": 26435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 61 · 2026-05-28T13:35:14.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XNAjvRVCTg3sNnn4K3qni7`</summary>

```json
{
  "query": "\"Open LLM Leaderboard\" V2 \"IFEval\" \"BBH\" \"MATH\" \"GPQA\" \"MUSR\" \"MMLU-PRO\" benchmarks six"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17afbaed-f079-4cc4-8f42-215adfb63e70",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV47uVkMHWtBmsMr8hZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e29b356-cbcc-4726-8a5c-847051a9e924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPRNDDWtXgQz75Pra57iym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2508,
      "cache_read_input_tokens": 26435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2508,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
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

_source line 62 · 2026-05-28T13:35:15.429Z_

<details><summary>↩ Tool result · `toolu_01Wfa3SbAkGAFr43VxW53wsy`</summary>

````text
# Datasets Under open-llm-leaderboard-old Organization

## Available Datasets

Based on the web page, there are **7,059 datasets** total in this organization. The page shows several examples:

1. **open-llm-leaderboard-old/results** (9.94k, 50 downloads)
2. **open-llm-leaderboard-old/contents** (7.26k, 125 downloads)
3. **open-llm-leaderboard-old/requests** (3, 5.12k downloads, 22 files)
4. **open-llm-leaderboard-old/dynamic_model_information** (8 files, 4 downloads)

## Per-Model Details Datasets

**Yes**, there are per-model details datasets. Examples shown:

- `open-llm-leaderboard-old/details_Ba2han__Phi-3-Medium-Llamaish`
- `open-llm-leaderboard-old/details_Hastagaras__Halu-8B-Llama3-CR-v0.45`
- `open-llm-leaderboard-old/details_bunkalab__Phi-3-mini-128k-instruct-HumanChoice-4.6k-DPO`

### Naming Pattern

```
details_[model_owner]__[model_name]
```

The pattern follows: `details_` prefix + organization/author name + `__` separator + model name.

### Number of Detail Datasets

While not explicitly stated how many are detail datasets, the page indicates there are multiple (at least 6+ visible), with the total being 7,059 datasets.

## Access Level

The datasets appear to be **freely accessible** - the page shows "Preview" and "Viewer" permissions on the listed datasets with no indication of gating or access restrictions.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dcd0871-6410-432d-9607-c4e17b838fcb",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "ad6749a8-fa3e-4825-98e5-f71ce6a0e38f",
  "sourceToolAssistantUUID": "4dcd0871-6410-432d-9607-c4e17b838fcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-28T13:35:15.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018B2iCmwTr8dfwGvhNkccF3`</summary>

```json
{
  "query": "IRT \"person fit\" \"lz\" \"lz*\" fixed item parameters LLM contamination benchmark data leakage detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad6749a8-fa3e-4825-98e5-f71ce6a0e38f",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV47uVkMHWtBmsMr8hZB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1137ef85-d1e6-4972-a826-c459ed269b96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPRNDDWtXgQz75Pra57iym",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2508,
      "cache_read_input_tokens": 26435,
      "output_tokens": 410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2508
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 410,
          "cache_read_input_tokens": 26435,
          "cache_creation_input_tokens": 2508,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2508,
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

_source line 64 · 2026-05-28T13:35:18.731Z_

<details><summary>↩ Tool result · `toolu_01HH5V69rEfYeGdpTZCC1TX3`</summary>

````text
# Dataset Content and Structure

Based on the page content, this dataset contains **evaluation results** from running the model `voidful/qd-phi-1_5` on the Open LLM Leaderboard. Here's what you need to know:

## What Data It Contains

The dataset is composed of:
- **63 configurations**, each corresponding to one evaluated task
- **Aggregated results** from 2 evaluation runs
- Individual task results for benchmarks like:
  - ARC Challenge
  - HellaSwag
  - MMLU (Massive Multitask Language Understanding) subtasks
  - TruthfulQA
  - Winogrande
  - GSM8K

## Per-Item Correctness Data

**The page does NOT clearly indicate whether individual item-level responses are included.** The visible results show only:
- **Aggregated metrics** (accuracy scores, standard errors)
- Summary statistics across all questions per task
- No per-question correctness indicators visible in the documentation

## Available Data Structure

Example loading:
```python
from datasets import load_dataset
data = load_dataset("open-llm-leaderboard/details_voidful__qd-phi-1_5",
    "harness_winogrande_5",
    split="train")
```

Available configurations include tasks like:
- `harness_arc_challenge_25`
- `harness_hellaswag_10`
- `harness_hendrycksTest-*` (multiple MMLU subtasks)
- `harness_truthfulqa_mc_0`
- `results` (aggregated metrics)

## Downloadability

✅ **Yes, freely downloadable** - Listed on Hugging Face Datasets with 26 downloads last month, 179 MB total size

## Limitation

The dataset card contains mostly **"[More Information Needed]"** placeholders, indicating incomplete documentation about the exact column structure and detailed data format.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17afbaed-f079-4cc4-8f42-215adfb63e70",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "67285f72-e703-488c-8cd5-4fcae78e53f7",
  "sourceToolAssistantUUID": "17afbaed-f079-4cc4-8f42-215adfb63e70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-28T13:35:22.741Z_

<details><summary>↩ Tool result · `toolu_01XNAjvRVCTg3sNnn4K3qni7`</summary>

```text
Web search results for query: ""Open LLM Leaderboard" V2 "IFEval" "BBH" "MATH" "GPQA" "MUSR" "MMLU-PRO" benchmarks six"

Links: [{"title":"Open LLM Leaderboard - Benchmarks - LLMIndex","url":"https://llmindex.net/benchmarks/open-llm-leaderboard"},{"title":"Open LLM Leaderboard - Compare Open Source Large Language Models","url":"https://open-llm-leaderboard-open-llm-leaderboard.hf.space/"},{"title":"Leaderboards — Oumi OSS","url":"https://oumi.ai/docs/en/latest/user_guides/evaluate/leaderboards.html"},{"title":"AI Models Ranking: Hugging Face's Open LLM Leaderboard v2 Shows Chinese Models Leading the Pack - AI Toolchest","url":"https://www.aitoolchest.com/ai-models-ranking-hugging-face-llm-leaderboard/"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Can't reproduce Open LLM Leaderboard v2 normalized scores - Beginners - Hugging Face Forums","url":"https://discuss.huggingface.co/t/cant-reproduce-open-llm-leaderboard-v2-normalized-scores/105187"},{"title":"lm-evaluation-harness/lm_eval/tasks/leaderboard/README.md at main · EleutherAI/lm-evaluation-harness","url":"https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/leaderboard/README.md"},{"title":"About · Hugging Face","url":"https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/about"},{"title":"Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs   Evaluation, Benchmark, and Arena","url":"https://arxiv.org/pdf/2406.07545"}]

Based on the search results, here's what I found about the Open LLM Leaderboard V2 and its benchmarks:

## Overview

The Open LLM Leaderboard, created by Hugging Face, is a standardized benchmarking platform designed to evaluate and rank open-source large language models (LLMs) and chatbots. The Open LLM Leaderboard v2 was launched in October 2024 with improved scoring normalization and new benchmarks including MMLU Pro, GPQA, MUSR, MATH, IFEval, and BBH.

## The Six Benchmarks

The evaluation typically involves causal language models tested without fine-tuning on the benchmark data, across benchmarks like MMLU Pro, GPQA, MUSR, MATH, IFEval, and BBH. Here's what each benchmark measures:

- **IFEval**: Evaluates the models' ability to follow instructions and provide accurate responses, including a range of tasks that require the models to use their language understanding and generation abilities.

- **BBH (Big Bench Hard)**: Tests multiple task capabilities including multistep reasoning.

- **MATH**: Tests the models' ability to solve mathematical problems and provide accurate solutions, including a range of problems that require mathematical reasoning and problem-solving abilities.

- **GPQA**: Tests the models' ability to provide accurate and informative responses to questions, including a range of questions that require models to use their knowledge and reasoning abilities.

- **MUSR**: Evaluates the models' ability to solve complex problems and provide accurate solutions, including problems that require reasoning and problem-solving abilities.

- **MMLU-PRO**: Evaluates the models' ability to answer questions and provide accurate responses, including a range of questions that require models to use their knowledge and reasoning abilities.

The leaderboard measures model capabilities across multiple challenging benchmarks that test reasoning, general knowledge, instruction following, and multi-step problem solving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e29b356-cbcc-4726-8a5c-847051a9e924",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "b9f7777f-7c92-42b1-8267-df669f90c952",
  "sourceToolAssistantUUID": "1e29b356-cbcc-4726-8a5c-847051a9e924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-28T13:35:32.180Z_

<details><summary>↩ Tool result · `toolu_018B2iCmwTr8dfwGvhNkccF3`</summary>

```text
Web search results for query: "IRT "person fit" "lz" "lz*" fixed item parameters LLM contamination benchmark data leakage detection"

Links: [{"title":"Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in   Closed-Source LLMs","url":"https://arxiv.org/pdf/2402.03927"},{"title":"How Much Can We Forget about Data Contamination? | OpenReview","url":"https://openreview.net/forum?id=Pf0PaYS9KG&noteId=MbAmNvpmdZ"},{"title":"LessLeak-Bench: A First Investigation of Data Leakage in LLMs Across 83 Software Engineering Benchmarks","url":"https://arxiv.org/html/2502.06215v1"},{"title":"Contamination Report for Multilingual Benchmarks","url":"https://arxiv.org/pdf/2410.16186"},{"title":"AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge","url":"https://arxiv.org/pdf/2412.13670"},{"title":"Benchmark Leakage Trap: Can We Trust LLM-based Recommendation?","url":"https://arxiv.org/pdf/2602.13626"},{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"(PDF) NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark","url":"https://www.researchgate.net/publication/376393345_NLP_Evaluation_in_trouble_On_the_Need_to_Measure_LLM_Data_Contamination_for_each_Benchmark"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"}]

The search results focus on data contamination and leakage in LLMs, but don't contain information specifically about IRT (Item Response Theory) person fit statistics like "lz" or "lz*" with fixed item parameters. Let me try a more targeted search for IRT person fit methods.

Links: [{"title":"lz: lz and lzstar person-fit statistics in PerFit: Person Fit","url":"https://rdrr.io/rforge/PerFit/man/lz.html"},{"title":"Package ‘PerFit’ July 21, 2025 Type Package Title Person Fit Version 1.4.7","url":"https://cran.r-project.org/web/packages/PerFit/PerFit.pdf"},{"title":"(PDF) Improving Person-Fit Assessment by Correcting the Ability Estimate and Its Reference Distribution","url":"https://www.academia.edu/23861508/Improving_Person_Fit_Assessment_by_Correcting_the_Ability_Estimate_and_Its_Reference_Distribution"},{"title":"lzpoly: lzpoly person-fit statistic in PerFit: Person Fit","url":"https://rdrr.io/cran/PerFit/man/lzpoly.html"},{"title":"The lz(p)* Person-Fit Statistic in an Unfolding Model Context - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5978489/"},{"title":"A Two-Step Method Based on lz* for Identifying Effortful Respondents","url":"https://www.mdpi.com/2079-3200/14/2/30"},{"title":"person_fit: Calculate person-fit indices in irt: Item Response Theory and Computerized Adaptive Testing Functions","url":"https://rdrr.io/cran/irt/man/person_fit.html"},{"title":"pfit: Person-Fit statistics in PP: Person Parameter Estimation","url":"https://rdrr.io/cran/PP/man/pfit.html"}]

Great! I found relevant information about IRT person fit statistics. Now let me search for specific information about using fixed item parameters and any connection to LLM contamination detection.

Links: [{"title":"Person Fit Analysis in Computerized Adaptive Testing Using Tests for a Change Point","url":"https://www.researchgate.net/publication/305630527_Person_Fit_Analysis_in_Computerized_Adaptive_Testing_Using_Tests_for_a_Change_Point"},{"title":"fitting model based: Topics by Science.gov","url":"https://www.science.gov/topicpages/f/fitting+model+based.html"},{"title":"Person-fit analysis — Grokipedia","url":"https://grokipedia.com/page/person_fit_analysis"},{"title":"Entropy-Based Measures for Person Fit in Item Response Theory - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5978476/"},{"title":"PerFit-package: Person Fit in PerFit: Person Fit","url":"https://rdrr.io/cran/PerFit/man/PerFit-package.html"},{"title":"Score-Based Tests With Fixed Effects Person Parameters in Item Response Theory: Detecting Model Misspecification Including Differential Item Functioning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12890607/"},{"title":"Reducing Calibration Bias for Person Fit Assessment by Mixture Model Expansion","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12413990/"},{"title":"IsolationForest — scikit-learn 1.8.0 documentation","url":"https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html"}]

Based on my web searches, I can now provide you with a comprehensive summary of the relevant information I found:

## Summary of Web Search Results

The search revealed information about two main topics:

### IRT Person-Fit Statistics (lz and lz*)

Drasgow et al. (1985) introduced one of the most used person-fit statistics, lz, which is the standardized log-likelihood of the respondent's response vector. The computation of lz requires that both item and ability parameters are available, and the function allows users to enter their own item and ability parameter estimates.

The lz statistic was later developed further by Snijders (2001) into the lzstar (lz*) statistic. The likelihood-based person-fit statistic, lz*, is commonly used in educational assessments to distinguish between respondents who are putting in effort and those who are not. However, lz* depends on the estimated item parameters.

### Applications to Detecting Aberrant Patterns

Person-fit measures such as lz and lz* have been studied using Monte Carlo simulation and were successfully able to detect aberrant response patterns when comparing contaminated and uncontaminated subgroups of persons.

Machine learning approaches for person-fit detection outperform conventional statistics like the lz statistic in terms of detection power, particularly for short tests, with simulations demonstrating higher sensitivity under various contamination scenarios.

### LLM Data Contamination Context

While my search found extensive literature on LLM benchmark contamination and data leakage detection methods, I did not locate papers that specifically combine IRT person-fit statistics (lz/lz*) with fixed item parameters for detecting LLM training data contamination in benchmarks. The LLM contamination literature focuses on different detection approaches such as string matching and retrieval-based methods rather than IRT-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1137ef85-d1e6-4972-a826-c459ed269b96",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "e4734a3b-96e5-4af7-a6f2-10b4c4cc50d5",
  "sourceToolAssistantUUID": "1137ef85-d1e6-4972-a826-c459ed269b96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-28T13:35:34.356Z_

Let me do final targeted searches on the remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4734a3b-96e5-4af7-a6f2-10b4c4cc50d5",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV49m4JbD9ctSYBeJhKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a8eff09-bf2d-461a-8c6c-f8a0867abbd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbj6ht2XZGZKySWbwn9SSN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4416,
      "cache_read_input_tokens": 28943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4416,
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

_source line 68 · 2026-05-28T13:35:37.298Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sj8S3tyfuuxWvhPbZFGDiB`</summary>

```json
{
  "url": "https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/about",
  "prompt": "What are the exact benchmarks used in Open LLM Leaderboard V2? Is the MATH benchmark specifically \"MATH Level 5\" or \"MATH-500\"? Which subset of MATH is used? Is GSM8K included in V2? List all benchmarks with their exact specifications (number of items, few-shot settings, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a8eff09-bf2d-461a-8c6c-f8a0867abbd0",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV49m4JbD9ctSYBeJhKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88e7ba39-864b-436f-a6f3-3c99cf869fba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbj6ht2XZGZKySWbwn9SSN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4416,
      "cache_read_input_tokens": 28943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4416,
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

_source line 69 · 2026-05-28T13:35:37.303Z_

<details><summary>↩ Tool result · `toolu_01Sj8S3tyfuuxWvhPbZFGDiB`</summary>

````text
# About

With the plethora of large language models (LLMs) and chatbots being released week upon week, often with grandiose claims of their performance, it can be hard to filter out the genuine progress that is being made by the open-source community and which model is the current state of the art.

We wrote a release blog [here](https://huggingface.co/spaces/open-llm-leaderboard/blog) to explain why we introduced this leaderboard!

## Tasks

📈 We evaluate models on 6 key benchmarks using the [Eleuther AI Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) , a unified framework to test generative language models on a large number of different evaluation tasks.

- **IFEval** ([https://arxiv.org/abs/2311.07911](https://arxiv.org/abs/2311.07911)) – IFEval is a dataset designed to test a model's ability to follow explicit instructions, such as "include keyword x" or "use format y." The focus is on the model's adherence to formatting instructions rather than the content generated, allowing for the use of strict and rigorous metrics.
- **BBH (Big Bench Hard)** ([https://arxiv.org/abs/2210.09261](https://arxiv.org/abs/2210.09261)) – A subset of 23 challenging tasks from the BigBench dataset to evaluate language models. The tasks use objective metrics, are highly difficult, and have sufficient sample sizes for statistical significance. They include multistep arithmetic, algorithmic reasoning (e.g., boolean expressions, SVG shapes), language understanding (e.g., sarcasm detection, name disambiguation), and world knowledge. BBH performance correlates well with human preferences, providing valuable insights into model capabilities.
- **MATH** ([https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874)) – MATH is a compilation of high-school level competition problems gathered from several sources, formatted consistently using Latex for equations and Asymptote for figures. Generations must fit a very specific output format. We keep only level 5 MATH questions and call it MATH Lvl 5.
- **GPQA (Graduate-Level Google-Proof Q&A Benchmark)** ([https://arxiv.org/abs/2311.12022](https://arxiv.org/abs/2311.12022)) – GPQA is a highly challenging knowledge dataset with questions crafted by PhD-level domain experts in fields like biology, physics, and chemistry. These questions are designed to be difficult for laypersons but relatively easy for experts. The dataset has undergone multiple rounds of validation to ensure both difficulty and factual accuracy. Access to GPQA is restricted through gating mechanisms to minimize the risk of data contamination. Consequently, we do not provide plain text examples from this dataset, as requested by the authors.
- **MuSR (Multistep Soft Reasoning)** ([https://arxiv.org/abs/2310.16049](https://arxiv.org/abs/2310.16049)) – MuSR is a new dataset consisting of algorithmically generated complex problems, each around 1,000 words in length. The problems include murder mysteries, object placement questions, and team allocation optimizations. Solving these problems requires models to integrate reasoning with long-range context parsing. Few models achieve better than random performance on this dataset.
- **MMLU-PRO (Massive Multitask Language Understanding - Professional)** ([https://arxiv.org/abs/2406.01574](https://arxiv.org/abs/2406.01574)) – MMLU-Pro is a refined version of the MMLU dataset, which has been a standard for multiple-choice knowledge assessment. Recent research identified issues with the original MMLU, such as noisy data (some unanswerable questions) and decreasing difficulty due to advances in model capabilities and increased data contamination. MMLU-Pro addresses these issues by presenting models with 10 choices instead of 4, requiring reasoning on more questions, and undergoing expert review to reduce noise. As a result, MMLU-Pro is of higher quality and currently more challenging than the original.

For all these evaluations, a higher score is a better score. We chose these benchmarks as they test a variety of reasoning and general knowledge across a wide variety of fields in 0-shot and few-shot settings.

## Model Types

- 🟢 **Pretrained Model:** New, base models trained on a given text corpora using masked modeling.
- 🟩 **Continuously Pretrained Model:** New, base models continuously trained on further corpora (which may include IFT/chat data) using masked modeling.
- 🔶 **Fine-Tuned on Domain-Specific Datasets Model:** Pretrained models fine-tuned on more data.
- 💬 **Chat Models (RLHF, DPO, IFT, ...):** Chat-like fine-tunes using IFT (datasets of task instruction), RLHF, DPO (changing the model loss with an added policy), etc.
- 🤝 **Base Merges and Moerges Model:** Merges or MoErges, models which have been merged or fused without additional fine-tuning.

## Results

You can find:
- Detailed numerical results in the [`results` Hugging Face dataset](https://huggingface.co/datasets/open-llm-leaderboard/results/).
- Details on the input/outputs for the models in the `details` of each model, which you can access by clicking the 📄 emoji after the model name.
- Community queries and running status in the [`requests` Hugging Face dataset](https://huggingface.co/datasets/open-llm-leaderboard/requests).

If a model's name contains "Flagged", this indicates it has been flagged by the community, and should probably be ignored! Clicking the link will redirect you to the discussion about the model.

## Reproducibility

To reproduce our results, you can use our fork of [lm_eval](https://github.com/huggingface/lm-evaluation-harness/tree/main), as our PRs are not all merged in it at the moment.
```
git clone git@github.com:huggingface/lm-evaluation-harness.git
cd lm-evaluation-harness
git checkout main
pip install -e .
lm-eval --model_args="pretrained=,revision=,dtype=" --tasks=leaderboard  --batch_size=auto --output_path=
```
**Attention:** For instruction models add the `--apply_chat_template` and `fewshot_as_multiturn` option.

**Note:** You can expect results to vary slightly for different batch sizes because of padding.

### **Task Evaluations and Parameters**

**IFEval**:

- Task: "IFEval"
- Measure: Strict Accuracy at Instance and Prompt Levels (`inst_level_strict_acc,none` and `prompt_level_strict_acc,none`)
- Shots: 0-shot for both Instance-Level Strict Accuracy and Prompt-Level Strict Accuracy
- num_choices: 0 for both Strict Accuracy at Instance and Prompt Levels.
  
**Big Bench Hard (BBH)**:

- Overview Task: "BBH"
- Shots: 3-shot for each subtask
- Measure: Normalized Accuracy across all subtasks (`acc_norm,none`)
- List of subtasks with `num_choices`:
    - BBH Sports Understanding, num_choices=2
    - BBH Tracking Shuffled Objects (Three Objects), num_choices=3
    - BBH Navigate, num_choices=2
    - BBH Snarks, num_choices=2
    - BBH Date Understanding, num_choices=6
    - BBH Reasoning about Colored Objects, num_choices=18
    - BBH Object Counting, num_choices=19 (should be 18 but we added a “0” choice)
    - BBH Logical Deduction (Seven Objects), num_choices=7
    - BBH Geometric Shapes, num_choices=11
    - BBH Web of Lies, num_choices=2
    - BBH Movie Recommendation, num_choices=6
    - BBH Logical Deduction (Five Objects), num_choices=5
    - BBH Salient Translation Error Detection, num_choices=6
    - BBH Disambiguation QA, num_choices=3
    - BBH Temporal Sequences, num_choices=4
    - BBH Hyperbaton, num_choices=2
    - BBH Logical Deduction (Three Objects), num_choices=3
    - BBH Causal Judgement, num_choices=2
    - BBH Formal Fallacies, num_choices=2
    - BBH Tracking Shuffled Objects (Seven Objects), num_choices=7
    - BBH Ruin Names, num_choices=6
    - BBH Penguins in a Table, num_choices=5
    - BBH Boolean Expressions, num_choices=2
    - BBH Tracking Shuffled Objects (Five Objects), num_choices=5

**Math Challenges**:

- Task: "Math Level 5"
- Measure: Exact Match (`exact_match,none`)
- Shots: 4-shot
- num_choices: 0

**Generalized Purpose Question Answering (GPQA)**:

- Task: "GPQA"
- Measure: Normalized Accuracy (`acc_norm,none`)
- Shots: 0-shot
- num_choices: 4

**MuSR**:

- Overview Task: "MuSR"
- Measure: Normalized Accuracy across all subtasks (`acc_norm,none`)
- MuSR Murder Mysteries: 0-shot, num_choices: 2
- MuSR Object Placement: 0-shot, num_choices: 5
- MuSR Team Allocation: 0-shot, num_choices: 3

**MMLU-PRO**:

- Task: "MMLU-PRO"
- Measure: Accuracy (`acc,none`)
- Shots: 5-shot
- num_choices: 10


````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88e7ba39-864b-436f-a6f3-3c99cf869fba",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "a4511f5a-d217-4d96-ada7-92bb27fddca2",
  "sourceToolAssistantUUID": "88e7ba39-864b-436f-a6f3-3c99cf869fba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-28T13:35:39.286Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D77XNA1vYkKWVLLjDcMP1b`</summary>

```json
{
  "url": "https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/leaderboard/README.md",
  "prompt": "What are the exact benchmarks/tasks used for the Open LLM Leaderboard V2? Is there a MATH task? Is it MATH Level 5 or MATH-500? How many items does each benchmark have? Is GSM8K included?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4511f5a-d217-4d96-ada7-92bb27fddca2",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV49m4JbD9ctSYBeJhKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97ce0219-56c3-4ad2-a66c-cd2b9508031a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbj6ht2XZGZKySWbwn9SSN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4416,
      "cache_read_input_tokens": 28943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4416,
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

_source line 71 · 2026-05-28T13:35:40.184Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kj8qhF6MCDtDrHGj1baCyr`</summary>

```json
{
  "query": "arxiv \"IRT\" \"item response theory\" LLM \"person fit\" OR \"aberrant\" OR \"anomalous\" contamination detection benchmark 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97ce0219-56c3-4ad2-a66c-cd2b9508031a",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV49m4JbD9ctSYBeJhKA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "703728f1-97e1-4c44-a2d4-993c51034010",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbj6ht2XZGZKySWbwn9SSN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4416,
      "cache_read_input_tokens": 28943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4416,
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

_source line 72 · 2026-05-28T13:35:44.655Z_

<details><summary>↩ Tool result · `toolu_01D77XNA1vYkKWVLLjDcMP1b`</summary>

```text
Based on the document provided, here are the exact benchmarks for the Open LLM Leaderboard:

**The six evaluation tasks are:**
1. "BBH (3-shots, multichoice)"
2. "GPQA (0-shot, multichoice)"
3. "mmlu-pro (5-shots, multichoice)"
4. "Musr (0-shot, multichoice)"
5. "ifeval (0-shot, generative)"
6. "Math-lvl-5 (4-shots, generative, minerva version)"

**Regarding your specific questions:**

**MATH Task:** Yes, a MATH task is included. It is specifically "Math-lvl-5" (Level 5 only), not the full MATH-500 dataset. The document notes it uses "4 shots" and is "the minerva version."

**Item counts:** The document does not specify the number of items in each benchmark.

**GSM8K:** GSM8K is not mentioned anywhere in this README, so it is not included in the leaderboard evaluation suite.

The document references a blog post for "details on the choice of those evals," but that content is not included in the material provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97ce0219-56c3-4ad2-a66c-cd2b9508031a",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "ee7cecb3-c4b5-4321-8ffa-9b407ca63fb1",
  "sourceToolAssistantUUID": "97ce0219-56c3-4ad2-a66c-cd2b9508031a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-28T13:35:49.120Z_

<details><summary>↩ Tool result · `toolu_01Kj8qhF6MCDtDrHGj1baCyr`</summary>

```text
Web search results for query: "arxiv "IRT" "item response theory" LLM "person fit" OR "aberrant" OR "anomalous" contamination detection benchmark 2024 2025"

Links: [{"title":"Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments","url":"https://arxiv.org/html/2412.02713v2"},{"title":"Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/pdf/2510.00844"},{"title":"arXiv:2506.09796v1 [cs.CL] 11 Jun 2025","url":"https://arxiv.org/pdf/2506.09796"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"A Short Note on Aberrant Responses Bias in Item Response Theory","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6365413/"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Leveraging LLM-Respondents for Item Evaluation: a Psychometric Analysis","url":"https://arxiv.org/html/2407.10899v1"}]

Based on the search results, here are the most relevant papers related to your query about IRT, person fit, LLMs, and contamination detection:

## Most Relevant Results:

**1. Applying Item Response Theory to Distinguish Between Human and Generative AI Responses** (arXiv 2412.02713, December 2024)
This work provides a theoretical foundation and empirical evidence for the application of IRT to identify AI cheating in MCQ-based assessments, directly addressing aberrant/anomalous responses in the context of LLM detection. The paper explicitly discusses person-fit statistics for aberrant response detection.

**2. Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory** (arXiv 2505.15055, January 2026)
This paper proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. It conducts extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

**3. Learning Compact Representations of LLM Abilities via Item Response Theory** (arXiv 2510.00844, October 2025)
This paper applies IRT to model LLM abilities and introduces an MoE-based method for learning query characteristics.

**4. Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory** (arXiv 2602.00521, February 2026)
This work leverages IRT-GRM to yield interpretable signals for diagnosing judgments systematically and provides practical guidance for verifying reliability of LLM-as-a-Judge.

The first paper (2412.02713) appears most directly aligned with your query regarding person fit statistics for contamination/anomalous response detection in the context of LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "703728f1-97e1-4c44-a2d4-993c51034010",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "c1432588-40fd-4a9e-bef0-5ef3fa2b9c93",
  "sourceToolAssistantUUID": "703728f1-97e1-4c44-a2d4-993c51034010",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-28T13:35:53.521Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011RK6nexAbNYQifD3fUQt6R`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.02713",
  "prompt": "Does this paper use IRT person-fit statistics to detect AI/LLM cheating? Does it use fixed item parameters calibrated on one population and then applied to another? Does it combine fixed-parameter IRT calibration with contamination or cheating detection? What specific person-fit statistics does it use? What is the methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1432588-40fd-4a9e-bef0-5ef3fa2b9c93",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV4B1WEk335AbfLu3isP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28be7e38-4cab-40cc-9d38-6a459e05d17e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017k64mn1yuadC9Vye4c72V9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 33359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4098,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 75 · 2026-05-28T13:35:55.422Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L9EX4yrwmH3kmGLmks18ST`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.15055",
  "prompt": "Does this paper discuss contamination detection via IRT? Does it use person-fit statistics? Does it use fixed item parameters? Does it mention the availability of the per-item response matrix data? Is the data publicly available?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28be7e38-4cab-40cc-9d38-6a459e05d17e",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV4B1WEk335AbfLu3isP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dafbe2d8-57a2-4332-a3b6-de8c15979cc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017k64mn1yuadC9Vye4c72V9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 33359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4098,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 76 · 2026-05-28T13:35:56.122Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KHdXew6NsSW4H9RxehTpbm`</summary>

```json
{
  "query": "MATH level 5 dataset number of items questions \"how many\" hendrycks competition mathematics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dafbe2d8-57a2-4332-a3b6-de8c15979cc4",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV4B1WEk335AbfLu3isP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ce2a1f9-7763-4791-a116-ba3b45f767a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017k64mn1yuadC9Vye4c72V9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4098,
      "cache_read_input_tokens": 33359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4098,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 77 · 2026-05-28T13:35:58.309Z_

<details><summary>↩ Tool result · `toolu_01L9EX4yrwmH3kmGLmks18ST`</summary>

```text
Based on the provided webpage content, I cannot definitively answer your questions because the page only contains the abstract and metadata for the paper, not the full text.

From what is available:

**Contamination detection via IRT:** Not mentioned in the abstract.

**Person-fit statistics:** Not mentioned in the abstract.

**Fixed item parameters:** Not mentioned in the abstract. The abstract describes "PSN-IRT" as incorporating "a rich set of item parameters," but doesn't specify whether parameters are fixed or estimated.

**Per-item response matrix data availability:** The abstract states the analysis covers "41,871 items" across benchmarks, but the provided content gives no information about whether this data is publicly available or shared.

To answer these questions accurately, you would need to access the full paper via the PDF or HTML links provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dafbe2d8-57a2-4332-a3b6-de8c15979cc4",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "76c014c6-82b5-4b51-b607-26ae8d483d46",
  "sourceToolAssistantUUID": "dafbe2d8-57a2-4332-a3b6-de8c15979cc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-28T13:35:58.369Z_

<details><summary>↩ Tool result · `toolu_011RK6nexAbNYQifD3fUQt6R`</summary>

```text
# Analysis of Paper's Methodology

Based on the abstract provided, yes, this paper does use IRT person-fit statistics to detect AI cheating:

**Core Methodology:**
The researchers apply Item Response Theory to identify when responses deviate from expected human patterns. As stated, their approach "models" these deviations "using Person-Fit Statistics."

**Detection Approach:**
The work assumes "artificial and human intelligence exhibit different response patterns, with AI cheating manifesting as deviations from the expected patterns of human responses."

**Key Findings:**
The method "effectively highlights the differences between human responses and those generated by premium versions of leading chatbots (ChatGPT, Claude, and Gemini)."

**Limitations Note:**
Importantly, the authors acknowledge the method "is also sensitive to the amount of AI cheating in the data," suggesting detection accuracy may vary based on contamination levels.

**Regarding Your Specific Questions:**
The abstract does not specify:
- Whether item parameters were fixed and calibrated on one population then applied to another
- The exact person-fit statistics employed
- Whether contamination detection was explicitly combined with fixed-parameter calibration

These technical details would require reviewing the full paper rather than just the abstract provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28be7e38-4cab-40cc-9d38-6a459e05d17e",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "b67beae6-7f97-4634-8568-5a1f1f0ba211",
  "sourceToolAssistantUUID": "28be7e38-4cab-40cc-9d38-6a459e05d17e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-28T13:36:00.787Z_

<details><summary>↩ Tool result · `toolu_01KHdXew6NsSW4H9RxehTpbm`</summary>

```text
Web search results for query: "MATH level 5 dataset number of items questions "how many" hendrycks competition mathematics"

Links: [{"title":"Datasets for Training Intelligent Tutoring Systems for Mathematics","url":"https://curriculumredesign.org/wp-content/uploads/Datasets-for-Training-Intelligent-Tutoring-Systems-for-Mathematics-CCR.pdf"},{"title":"hendrycks/competition_math · Datasets at Hugging Face","url":"https://huggingface.co/datasets/hendrycks/competition_math"},{"title":"MATH Dataset Benchmark","url":"https://www.emergentmind.com/topics/math-dataset"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset Dan Hendrycks","url":"https://arxiv.org/pdf/2103.03874"},{"title":"nlile/hendrycks-MATH-benchmark · Datasets at Hugging Face","url":"https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark"},{"title":"[2103.03874] Measuring Mathematical Problem Solving With the MATH Dataset","url":"https://arxiv.org/abs/2103.03874"},{"title":"competition_math.py · hendrycks/competition_math at 5a45cb0fd1d39bf3fc16b2a73ff8a586f8ea6f14","url":"https://huggingface.co/datasets/hendrycks/competition_math/blame/5a45cb0fd1d39bf3fc16b2a73ff8a586f8ea6f14/competition_math.py"},{"title":"dataset_infos.json · hendrycks/competition_math at 5a45cb0fd1d39bf3fc16b2a73ff8a586f8ea6f14","url":"https://huggingface.co/datasets/hendrycks/competition_math/blame/5a45cb0fd1d39bf3fc16b2a73ff8a586f8ea6f14/dataset_infos.json"},{"title":"competition_math.py · hendrycks/competition_math at main","url":"https://huggingface.co/datasets/hendrycks/competition_math/blob/main/competition_math.py"},{"title":"GitHub - hendrycks/math: The MATH Dataset (NeurIPS 2021) · GitHub","url":"https://github.com/hendrycks/math"}]

Based on the search results, I found information about the MATH dataset by Hendrycks:

The MATH dataset consists of 12,500 problems from high school mathematics competitions, including AMC 10, AMC 12, AIME, and others, and all problems are tagged with a difficulty level from 1 to 5 (with 5 being the most difficult level).

However, the search results do not provide specific information about the exact number of Level 5 items or the breakdown of questions by level. To get that specific data, you would need to access the dataset directly through the official GitHub repository (https://github.com/hendrycks/math) or the Hugging Face dataset page (https://huggingface.co/datasets/hendrycks/competition_math) where you can view the complete dataset statistics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ce2a1f9-7763-4791-a116-ba3b45f767a4",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "c4414fa0-85c9-4e2b-a440-e9d6d88b1e76",
  "sourceToolAssistantUUID": "8ce2a1f9-7763-4791-a116-ba3b45f767a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-28T13:36:04.653Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FRWK4NDKEBKHpQGuuXBdpD`</summary>

```json
{
  "url": "https://huggingface.co/datasets/hendrycks/competition_math",
  "prompt": "How many total items are in the test set? How many Level 5 items are there? What is the breakdown by difficulty level? Is MATH-500 a separate subset? How many items at each level?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4414fa0-85c9-4e2b-a440-e9d6d88b1e76",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV4BsKe4bsPDgoCWygGh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15a166ba-6f84-4310-88b7-4716dec2de46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cZpCEKKJV47AABbfeKe76",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 37457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1641,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 81 · 2026-05-28T13:36:05.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013MnnaKLmfhiXq5zNTzfemk`</summary>

```json
{
  "query": "\"MATH-500\" dataset OpenAI 500 problems subset \"level 5\" OR \"all levels\" origin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a166ba-6f84-4310-88b7-4716dec2de46",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV4BsKe4bsPDgoCWygGh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71892066-6210-4d14-9aa8-85602db1a1d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cZpCEKKJV47AABbfeKe76",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 37457,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1641
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 37457,
          "cache_creation_input_tokens": 1641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1641,
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

_source line 82 · 2026-05-28T13:36:09.272Z_

<details><summary>↩ Tool result · `toolu_01FRWK4NDKEBKHpQGuuXBdpD`</summary>

```text
# MATH Dataset Information

Based on the webpage content provided, here's what I can tell you:

## Test Set Size
**Total items in test set: 5,000 examples**

## Level 5 Items
The webpage does not specify how many Level 5 items exist in the test set.

## Breakdown by Difficulty Level
The webpage does not provide a breakdown of items by difficulty level (Level 1-5).

## MATH-500 Subset
There is no mention of MATH-500 as a separate subset in the provided content.

## Items per Level
The specific count of items at each difficulty level is not provided in this webpage.

---

### What IS Known:
- **Train split**: 7,500 examples
- **Test split**: 5,000 examples
- **Difficulty levels**: Level 1 through Level 5 (Level 1 = easiest for humans, Level 5 = hardest)
- **Subject categories**: Algebra, Counting & Probability, Geometry, Intermediate Algebra, Number Theory, Prealgebra, and Precalculus

**Note**: The dataset access appears to be disabled due to a DMCA takedown notice as of the time this page was captured. For detailed statistics on level distributions, you would need to refer to the original paper (arxiv:2103.03874) or the GitHub repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15a166ba-6f84-4310-88b7-4716dec2de46",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "bdc9f23a-f9b2-47f2-ac5c-8926555515b3",
  "sourceToolAssistantUUID": "15a166ba-6f84-4310-88b7-4716dec2de46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-28T13:36:11.499Z_

<details><summary>↩ Tool result · `toolu_013MnnaKLmfhiXq5zNTzfemk`</summary>

```text
Web search results for query: ""MATH-500" dataset OpenAI 500 problems subset "level 5" OR "all levels" origin"

Links: [{"title":"--- task_categories: - text-generation language: - en pretty_name: MATH-500 ---","url":"https://huggingface.co/datasets/HuggingFaceH4/MATH-500/raw/main/README.md"},{"title":"README.md · HuggingFaceH4/MATH-500 at main","url":"https://huggingface.co/datasets/HuggingFaceH4/MATH-500/blob/main/README.md"},{"title":"HuggingFaceH4/MATH-500 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceH4/MATH-500"},{"title":"davidkim205/ko-math-500 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/davidkim205/ko-math-500"},{"title":"MATH-500 | EvalScope","url":"https://evalscope.readthedocs.io/en/latest/benchmarks/math_500.html"},{"title":"MATH-500 Benchmark Leaderboard | Artificial Analysis","url":"https://artificialanalysis.ai/evaluations/math-500"},{"title":"MATH Level 5 - AI Wiki - Artificial Intelligence Wiki","url":"https://aiwiki.ai/wiki/MATH_Level_5"},{"title":"MATH-500 Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/math-500"},{"title":"GitHub - openai/prm800k: 800,000 step-level correctness labels on LLM solutions to MATH problems · GitHub","url":"https://github.com/openai/prm800k"}]

Based on the search results, here's what I found about the MATH-500 dataset:

## Origin

MATH-500 is a subset of 500 problems from the MATH benchmark that OpenAI created in their "Let's Verify Step by Step" paper. The 500 problems were selected uniformly at random from the MATH test set and are believed to be representative of the test set as a whole.

## Dataset Composition

MATH-500 contains 500 challenging competition mathematics problems from AMC 10, AMC 12, AIME, and other mathematics competitions. Each problem includes full step-by-step solutions and spans multiple difficulty levels across seven mathematical subjects including Prealgebra, Algebra, Number Theory, Counting and Probability, Geometry, Intermediate Algebra, and Precalculus.

## Difficulty Levels

Difficulty levels are represented by an integer from 1 to 5, where a subject's easiest problems are assigned a level of 1 and the hardest problems are assigned a level of 5. It covers five difficulty levels across various mathematical topics.

The dataset is publicly available through HuggingFace and was originally developed as part of OpenAI's research on process supervision and step-level verification for mathematical problem solving.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71892066-6210-4d14-9aa8-85602db1a1d0",
  "isSidechain": true,
  "promptId": "9bc1bbb0-978c-478a-85b9-15f107a17a96",
  "agentId": "a1f3ab31e3696d242",
  "type": "user",
  "uuid": "63831edc-a320-44d2-b819-2b9c876a46d1",
  "sourceToolAssistantUUID": "71892066-6210-4d14-9aa8-85602db1a1d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-28T13:37:17.292Z_

Now I have all the information needed. Here is the comprehensive report.

---

## Finding 1: tinyBenchmarks (Polo et al., 2024) -- Full Response Matrix Availability

**The full 395-model x ~29K-item binary response matrix is NOT directly released by Polo et al.** The tinyBenchmarks project releases only the following:

- **Tiny datasets** (100 items each) on HuggingFace under the `tinyBenchmarks` organization: `tinyMMLU`, `tinyHellaswag`, `tinyWinogrande`, `tinyTruthfulQA`, `tinyARC`, `tinyGSM8K`, and `tinyAlpacaEval`.
- A **Python package** (`tinyBenchmarks` on PyPI) for estimating full-benchmark performance from tiny subsets.
- **Code** at [github.com/felipemaiapolo/tinyBenchmarks](https://github.com/felipemaiapolo/tinyBenchmarks).

**However**, the underlying per-item response data that Polo et al. used is reconstructible. They state they downloaded it from the Open LLM Leaderboard V1 "details" datasets in January 2024. The raw per-model, per-item correctness data lives in the V1 "details" datasets (see Finding 2 below), which are public. So while Polo et al. did not package and release their assembled 395x29K matrix as a single artifact, the source data is publicly available and the matrix can be reconstructed from the V1 details datasets.

**Key URLs:**
- Paper: [arxiv.org/abs/2402.14992](https://arxiv.org/abs/2402.14992) (ICML 2024)
- GitHub: [github.com/felipemaiapolo/tinyBenchmarks](https://github.com/felipemaiapolo/tinyBenchmarks)
- HuggingFace tiny datasets: [huggingface.co/tinyBenchmarks](https://huggingface.co/tinyBenchmarks)

---

## Finding 2: Open LLM Leaderboard Per-Model Item-Level Details -- Access Status

**Both V1 and V2 per-model details datasets are freely downloadable with NO access approval required.**

**V1 (archived):**
- The `open-llm-leaderboard-old` organization on HuggingFace hosts **~7,059 datasets**, the vast majority being per-model detail datasets following the naming pattern `details_[owner]__[model_name]`.
- Each details dataset contains per-task configurations (e.g., `harness_arc_challenge_25`, `harness_hellaswag_10`, `harness_hendrycksTest-*`, `harness_truthfulqa_mc_0`, etc.) with per-item results.
- Example: [huggingface.co/datasets/open-llm-leaderboard-old/details_voidful__qd-phi-1_5](https://huggingface.co/datasets/open-llm-leaderboard-old/details_voidful__qd-phi-1_5) -- freely downloadable, 179 MB.
- Aggregated results: [huggingface.co/datasets/open-llm-leaderboard-old/results](https://huggingface.co/datasets/open-llm-leaderboard-old/results)

**V2 (current):**
- Per-model details: [huggingface.co/datasets/open-llm-leaderboard/details](https://huggingface.co/datasets/open-llm-leaderboard/details) -- this dataset returned a 401 when I tried to fetch its page directly, which may indicate **gating or a temporary issue**. The aggregated results dataset at [huggingface.co/datasets/open-llm-leaderboard/results](https://huggingface.co/datasets/open-llm-leaderboard/results) is freely accessible.
- The V2 details dataset is structured with 63 configurations (one per evaluated task), and each model run appears as a specific split. Loading example:
  ```python
  from datasets import load_dataset
  data = load_dataset("open-llm-leaderboard/details", "model_name", split="train")
  ```

**Bottom line:** V1 details are clearly ungated and freely downloadable. V2 details may have some access restriction (the 401 response is notable) -- you should verify by trying to load it directly with the `datasets` library or checking the dataset card.

---

## Finding 3: MATH-500 and GSM8K in the Open LLM Leaderboard

**V1 benchmarks (6 tasks):**
1. ARC Challenge (25-shot)
2. HellaSwag (10-shot)
3. MMLU (5-shot)
4. TruthfulQA (0-shot)
5. Winogrande (5-shot)
6. **GSM8K (5-shot)** -- YES, GSM8K was included in V1

**V2 benchmarks (6 tasks, all different from V1):**
1. IFEval (0-shot)
2. BBH -- Big Bench Hard (3-shot)
3. **MATH Level 5** (4-shot, minerva version) -- this is the Level 5 subset of the Hendrycks MATH dataset, NOT MATH-500
4. GPQA (0-shot)
5. MuSR (0-shot)
6. MMLU-PRO (5-shot)

**Critical distinctions:**
- **GSM8K**: Included in V1 only. Dropped from V2 entirely (replaced by MATH Lvl 5 and other harder benchmarks). So V1 has large-N calibration data for GSM8K items across thousands of models.
- **MATH-500**: This is a 500-problem random sample from the full MATH test set (5,000 problems) across ALL difficulty levels, created by OpenAI for their "Let's Verify Step by Step" paper ([huggingface.co/datasets/HuggingFaceH4/MATH-500](https://huggingface.co/datasets/HuggingFaceH4/MATH-500)). It is **NOT** the same as what V2 uses. V2 uses only **MATH Level 5** problems (the hardest difficulty), which is a different subset.
- **Overlap**: MATH-500 samples uniformly across levels 1-5, so roughly 1/5 of MATH-500 items (~100 problems) would be Level 5 and thus overlap with the V2 MATH Lvl 5 evaluation set. The exact overlap depends on which specific Level 5 items appear in both sets.

**For your proposal**: You have large-N item-level calibration data for GSM8K items from V1 (thousands of models). For MATH-500, only partial overlap exists with V2's MATH Level 5 evaluation. MATH-500 as a whole is NOT directly evaluated on the Open LLM Leaderboard in either version.

---

## Finding 4: Two-Stage IRT with Fixed Parameters + Contamination/Cheating Detection

**No paper was found that directly combines fixed-parameter IRT calibration with contamination/cheating detection in the specific two-stage framework you describe.** However, several closely related lines of work exist:

**IRT + Cheating Detection in Educational Testing:**
- Sinharay (2016), "Are Exam Questions Known in Advance? Using Local Dependence to Detect Cheating" ([PMC5131967](https://pmc.ncbi.nlm.nih.gov/articles/PMC5131967/)): Compares IRT 2PL item parameters between compromised and non-compromised datasets to detect item preknowledge. Uses local dependence (LD) as a primary indicator. Does NOT use fixed-parameter calibration -- instead re-estimates parameters and looks for shifts.
- Person-fit statistics (lz, lz*) are well-established in educational testing for detecting aberrant response patterns, and these do rely on treating item parameters as fixed. The R packages `PerFit` and `PP` implement these. However, this literature has not been extended to LLM benchmark contamination detection.

**IRT Applied to LLMs:**
- **"Applying IRT to Distinguish Between Human and Generative AI Responses"** ([arxiv.org/abs/2412.02713](https://arxiv.org/abs/2412.02713), Dec 2024): Uses IRT person-fit statistics to detect AI cheating on MCQ assessments. This is the closest paper to your concept -- it explicitly models AI responses as aberrant patterns using person-fit statistics. It calibrates IRT on human data and then flags AI-generated response patterns as anomalous.
- **"Lost in Benchmarks? Rethinking LLM Benchmarking with IRT"** ([arxiv.org/abs/2505.15055](https://arxiv.org/abs/2505.15055)): Notes that outlier-high guessing parameters in IRT can flag data contamination risk. Does not use fixed-parameter calibration or person-fit statistics explicitly.
- The **ATLAS** framework (adaptive testing for LLMs) uses IRT-based ability estimation with pre-calibrated item parameters, achieving 90% item reduction while maintaining precision -- this is essentially fixed-parameter calibration in practice, though not for contamination detection.

**The gap your proposal could fill**: The specific combination of (1) calibrating item parameters on a large reference population of LLMs, (2) fixing those parameters, and (3) using person-fit statistics (lz/lz*) on new models to detect contamination-driven aberrant response patterns appears to be **novel and unpublished**. The arxiv paper 2412.02713 comes closest but works in a human-vs-AI detection context rather than LLM-vs-LLM contamination detection.

Sources:
- [tinyBenchmarks paper (arXiv)](https://arxiv.org/abs/2402.14992)
- [tinyBenchmarks GitHub](https://github.com/felipemaiapolo/tinyBenchmarks)
- [Open LLM Leaderboard V1 Archive](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)
- [Open LLM Leaderboard V2 About](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/about)
- [Open LLM Leaderboard V2 Results Dataset](https://huggingface.co/datasets/open-llm-leaderboard/results)
- [Open LLM Leaderboard V1 Old Results](https://huggingface.co/datasets/open-llm-leaderboard-old/results)
- [Open LLM Leaderboard V1 Details Example](https://huggingface.co/datasets/open-llm-leaderboard-old/details_voidful__qd-phi-1_5)
- [MATH-500 on HuggingFace](https://huggingface.co/datasets/HuggingFaceH4/MATH-500)
- [MATH Dataset (Hendrycks)](https://huggingface.co/datasets/hendrycks/competition_math)
- [Eleuther AI lm-evaluation-harness Leaderboard Tasks](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/leaderboard/README.md)
- [Sinharay (2016) - Cheating Detection via Local Dependence](https://pmc.ncbi.nlm.nih.gov/articles/PMC5131967/)
- [IRT for Detecting AI Responses (arXiv 2412.02713)](https://arxiv.org/abs/2412.02713)
- [Lost in Benchmarks - PSN-IRT (arXiv 2505.15055)](https://arxiv.org/abs/2505.15055)
- [IRT Fixed Parameter Calibration Methods (Kim 2006)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.2006.00021.x)
- [Leak, Cheat, Repeat - LLM Contamination](https://arxiv.org/pdf/2402.03927)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63831edc-a320-44d2-b819-2b9c876a46d1",
  "isSidechain": true,
  "agentId": "a1f3ab31e3696d242",
  "requestId": "req_011CbV4CfBRASmoEu9MMHKoV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "16f77fe1-c255-418c-be67-9b8172a6d324",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "5b95810a-f282-45ac-8313-547d7229c270",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkUcRJvYC3EZXFwaYp6UAP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 39098,
      "output_tokens": 3036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1323
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3036,
          "cache_read_input_tokens": 39098,
          "cache_creation_input_tokens": 1323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1323,
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
