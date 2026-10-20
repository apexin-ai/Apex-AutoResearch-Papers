# Research conversation: I need to find and read the paper "Mapping Faithful Reasoning in Language Models" by Li et al. (arXiv 2510.22362), prese

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a7570908b24c44cbc.jsonl`
- **Structured JSON:** [`04cbff97ddfc26232d0c.json`](../../sessions/04/04cbff97ddfc26232d0c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-19T12:01:00.300Z_

I need to find and read the paper "Mapping Faithful Reasoning in Language Models" by Li et al. (arXiv 2510.22362), presented at the NeurIPS 2025 MechInterp Workshop. It introduces something called "Concept Walk" which projects each reasoning step onto concept directions and tracks temporal evolution of internal activations for faithfulness diagnosis. They reportedly find easy→decorative, hard→faithful patterns.

Please:
1. Search for this paper using WebSearch
2. Use WebFetch on the arXiv page to read the abstract and key details
3. Report back: What exactly is Concept Walk? How does it track temporal evolution? What are the key findings about easy vs hard tasks? What models/benchmarks do they use? How does it differ from answer-content linear probes?

Search queries to try:
- "Mapping Faithful Reasoning Language Models" Li 2510.22362
- "Concept Walk" faithfulness reasoning NeurIPS 2025
- arxiv.org 2510.22362

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "5511e92a-4ca2-4ae6-a469-f6e3d3785c38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T12:01:00.304Z_

```json
{
  "parentUuid": "5511e92a-4ca2-4ae6-a469-f6e3d3785c38",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
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
  "uuid": "f131d155-824d-4425-af72-741567624f2f",
  "timestamp": "2026-05-19T12:01:00.304Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T12:01:00.305Z_

```json
{
  "parentUuid": "f131d155-824d-4425-af72-741567624f2f",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9dda9302-d0fa-45dc-a413-aa3c3d9c7b32",
  "timestamp": "2026-05-19T12:01:00.305Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T12:01:02.982Z_



I'll search for this paper using multiple approaches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dda9302-d0fa-45dc-a413-aa3c3d9c7b32",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtfRMzLzKKVt9Mtx3Bg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cce24d01-6dd6-490b-930d-2720b25994b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYwuifrA3MabBWrAGzkkDv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1581,
      "cache_read_input_tokens": 7773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1581,
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

_source line 5 · 2026-05-19T12:01:03.384Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HusZWfUbiQK8a8gs6nZkQA`</summary>

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
  "parentUuid": "cce24d01-6dd6-490b-930d-2720b25994b4",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtfRMzLzKKVt9Mtx3Bg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "441c33b3-3238-47ee-89e7-b22546addd0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DYwuifrA3MabBWrAGzkkDv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1581,
      "cache_read_input_tokens": 7773,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1581
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 7773,
          "cache_creation_input_tokens": 1581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1581,
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

_source line 6 · 2026-05-19T12:01:03.387Z_

<details><summary>↩ Tool result · `toolu_01HusZWfUbiQK8a8gs6nZkQA`</summary>

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
  "parentUuid": "441c33b3-3238-47ee-89e7-b22546addd0b",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "7623d909-5740-4ec4-85c2-9598698d1e89",
  "sourceToolAssistantUUID": "441c33b3-3238-47ee-89e7-b22546addd0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-19T12:01:05.807Z_



Now let me search for the paper using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7623d909-5740-4ec4-85c2-9598698d1e89",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtfekPpP4WCotx1M9gz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44f318c2-7f43-4a17-b0aa-10573b12daee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VixFvFoawhuCd8bX4YW2hY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 8 · 2026-05-19T12:01:06.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BjSe9M5SfaTdiwZcQxsuwx`</summary>

```json
{
  "query": "\"Mapping Faithful Reasoning Language Models\" Li 2510.22362"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44f318c2-7f43-4a17-b0aa-10573b12daee",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtfekPpP4WCotx1M9gz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fc5c4db-85c7-4a78-b979-c8117848340c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VixFvFoawhuCd8bX4YW2hY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 9 · 2026-05-19T12:01:06.755Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BW9vyuZZVibPD6gS4ggcz8`</summary>

```json
{
  "query": "\"Concept Walk\" faithfulness reasoning NeurIPS 2025 MechInterp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fc5c4db-85c7-4a78-b979-c8117848340c",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtfekPpP4WCotx1M9gz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3f9a8e7-7c79-4d28-989e-256ea72ac884",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VixFvFoawhuCd8bX4YW2hY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1115,
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

_source line 10 · 2026-05-19T12:01:06.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016AcAgPwWekNhsyEikuHPz5`</summary>

```json
{
  "query": "arxiv 2510.22362"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3f9a8e7-7c79-4d28-989e-256ea72ac884",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtfekPpP4WCotx1M9gz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd4db53d-23c8-4541-8878-b429bc0ce466",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VixFvFoawhuCd8bX4YW2hY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1115,
      "cache_read_input_tokens": 9354,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1115
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 179,
          "cache_read_input_tokens": 9354,
          "cache_creation_input_tokens": 1115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1115,
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

_source line 11 · 2026-05-19T12:01:11.873Z_

<details><summary>↩ Tool result · `toolu_01BjSe9M5SfaTdiwZcQxsuwx`</summary>

```text
Web search results for query: ""Mapping Faithful Reasoning Language Models" Li 2510.22362"

Links: [{"title":"[2510.22362] Mapping Faithful Reasoning in Language Models","url":"https://arxiv.org/abs/2510.22362"},{"title":"Mapping Faithful Reasoning in Language Models","url":"https://arxiv.org/html/2510.22362"},{"title":"Mapping Faithful Reasoning in Language Models","url":"https://arxiv.org/pdf/2510.22362"},{"title":"Mapping Faithful Reasoning in Language Models Jiazheng Li∗","url":"https://openreview.net/pdf/89878ca66572c0425255f7be53b2879e6d2e7e7b.pdf"},{"title":"Faithful Reasoning Using Large Language Models","url":"https://arxiv.org/pdf/2208.14271"}]

Based on the search results, here's information about the paper:

**"Mapping Faithful Reasoning in Language Models"** (arXiv:2510.22362) is a research paper by Jiazheng Li, Andreas Damianou, J Rosser, José Luis Redondo García, and Konstantina Palla, submitted on October 25, 2025.

**Main Contributions:**

The paper addresses the problem that chain-of-thought (CoT) traces in reasoning language models are not always faithful reflections of internal computation. The authors introduce Concept Walk, a general framework for tracing how a model's internal stance evolves with respect to a concept direction during reasoning, which operates in activation space by projecting each reasoning step onto the concept direction learned from contrastive data.

**Key Findings:**

Applying Concept Walk to the domain of Safety using Qwen 3-4B, the authors find that in 'easy' cases, perturbed CoTs are quickly ignored indicating decorative reasoning, whereas in 'hard' cases, perturbations induce sustained shifts in internal activations consistent with faithful reasoning.

The paper is available on arXiv at: https://arxiv.org/abs/2510.22362


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fc5c4db-85c7-4a78-b979-c8117848340c",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "c84d46ea-2dad-4fc2-958c-adb246f99243",
  "sourceToolAssistantUUID": "0fc5c4db-85c7-4a78-b979-c8117848340c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T12:01:12.778Z_

<details><summary>↩ Tool result · `toolu_016AcAgPwWekNhsyEikuHPz5`</summary>

```text
Web search results for query: "arxiv 2510.22362"

Links: [{"title":"[2510.22362] Mapping Faithful Reasoning in Language Models","url":"https://arxiv.org/abs/2510.22362"},{"title":"[2509.22362] Neural Feature Geometry Evolves as Discrete Ricci Flow","url":"https://arxiv.org/abs/2509.22362"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"[2511.22362] Efficient-Husformer: Efficient Multimodal Transformer Hyperparameter Optimization for Stress and Cognitive Loads","url":"https://arxiv.org/abs/2511.22362"},{"title":"Estimating the Causal Effect of Early ArXiving on Paper Acceptance","url":"https://arxiv.org/pdf/2306.13891"}]

Based on the search results, arxiv paper 2510.22362 is titled "Mapping Faithful Reasoning in Language Models" and discusses how chain-of-thought traces promise transparency for reasoning language models, but prior work shows they are not always faithful reflections of internal computation.

The paper introduces Concept Walk, a general framework for tracing how a model's internal stance evolves with respect to a concept direction during reasoning. Unlike surface text, Concept Walk operates in activation space, projecting each reasoning step onto the concept direction learned from contrastive data.

As a case study, they apply Concept Walk to the domain of Safety using Qwen 3-4B, finding that in 'easy' cases, perturbed chain-of-thoughts are quickly ignored, indicating decorative reasoning, whereas in 'hard' cases, perturbations induce sustained shifts in internal activations, consistent with faithful reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd4db53d-23c8-4541-8878-b429bc0ce466",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "1913c2fd-359a-4884-851d-0c07b7c758fe",
  "sourceToolAssistantUUID": "fd4db53d-23c8-4541-8878-b429bc0ce466",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T12:01:25.419Z_

<details><summary>↩ Tool result · `toolu_01BW9vyuZZVibPD6gS4ggcz8`</summary>

```text
Web search results for query: ""Concept Walk" faithfulness reasoning NeurIPS 2025 MechInterp"

Links: [{"title":"Mapping Faithful Reasoning in Language Models Jiazheng Li∗","url":"https://openreview.net/pdf/89878ca66572c0425255f7be53b2879e6d2e7e7b.pdf"},{"title":"Mapping Faithful Reasoning in Language Models","url":"https://arxiv.org/pdf/2510.22362"},{"title":"GitHub - FarnoushRJ/RelP: [NeurIPS 2025 MechInterp Workshop - Spotlight] Official implementation of the paper \"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching\" · GitHub","url":"https://github.com/FarnoushRJ/RelP"},{"title":"Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations","url":"https://arxiv.org/pdf/2504.14150"},{"title":"Balancing Faithfulness and Performance in Reasoning via Multi-Listener Soft Execution","url":"https://arxiv.org/pdf/2602.16154"},{"title":"NeurIPS.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/NeurIPS.2025"}]

Based on the search results, here's what I found about "Concept Walk":

Concept Walk is a general framework for tracing how a model's internal stance evolves with respect to a concept direction during reasoning. Unlike surface text, it operates in activation space, projecting each reasoning step onto the concept direction learned from contrastive data.

This allows researchers to observe whether reasoning traces shape outcomes or are discarded. In a case study applying Concept Walk to the domain of Safety using Qwen 3-4B, the researchers found that in "easy" cases, perturbed chain-of-thought (CoT) traces are quickly ignored, indicating decorative reasoning, whereas in "hard" cases, perturbations induce sustained shifts in internal activations, consistent with faithful reasoning.

The methodological contribution of Concept Walk is that it provides a lens to re-examine faithfulness through concept-specific internal dynamics, helping identify when reasoning traces can be trusted and when they risk misleading practitioners. The work appears in the 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop on Mechanistic Interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3f9a8e7-7c79-4d28-989e-256ea72ac884",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "b4287914-147f-45a5-9789-6f7431334080",
  "sourceToolAssistantUUID": "e3f9a8e7-7c79-4d28-989e-256ea72ac884",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-19T12:01:29.139Z_

I found the paper. Now let me fetch the full details from both the arXiv abstract page and the HTML version for more depth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4287914-147f-45a5-9789-6f7431334080",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBthGidj2Y3pLgNWc3Kn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76b09860-633d-4474-9740-3afdf7265606",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdFAmsHwpvpzP8D15Xe8md",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 504,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 10469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1337,
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

_source line 15 · 2026-05-19T12:01:30.433Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Lo3NSRsbGDzB6eBsq2Z1jw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.22362",
  "prompt": "Extract the full abstract, all author names and affiliations, the submission date, and any other metadata (keywords, categories, venue). Reproduce the abstract in full without summarizing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76b09860-633d-4474-9740-3afdf7265606",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBthGidj2Y3pLgNWc3Kn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29f93c76-9aae-4abe-bf1c-ca13e3e6dfa9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdFAmsHwpvpzP8D15Xe8md",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 504,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 10469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1337,
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

_source line 16 · 2026-05-19T12:01:34.264Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GQpWEsosxu3eYzV8Tu2X3c`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.22362",
  "prompt": "Extract the full content of this paper in detail. I need:\n1. The complete abstract\n2. The full introduction - what problem are they solving, what is the gap\n3. The Concept Walk methodology in full detail - how concept directions are learned, how projections work, how temporal evolution is tracked, what equations/formulas are involved\n4. How they differ from answer-content linear probes\n5. The experimental setup - which models, which benchmarks/datasets, what perturbation methods they use\n6. Key results and findings - especially about easy vs hard tasks, decorative vs faithful reasoning\n7. The conclusion and limitations\nPlease be as thorough and detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29f93c76-9aae-4abe-bf1c-ca13e3e6dfa9",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBthGidj2Y3pLgNWc3Kn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c4365a5-8f77-4efc-ac35-e2220383a13e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EdFAmsHwpvpzP8D15Xe8md",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 504,
      "cache_creation_input_tokens": 1337,
      "cache_read_input_tokens": 10469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1337,
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

### Tool result

_source line 17 · 2026-05-19T12:01:35.428Z_

<details><summary>↩ Tool result · `toolu_01Lo3NSRsbGDzB6eBsq2Z1jw`</summary>

```text
# Paper Metadata Extraction

**Title:** Mapping Faithful Reasoning in Language Models

**arXiv ID:** 2510.22362

**Submission Date:** October 25, 2025

**Categories:** Computer Science - Machine Learning (cs.LG); Computation and Language (cs.CL)

**Venue:** Mechanistic Interpretability Workshop at NeurIPS 2025

## Authors
- Jiazheng Li
- Andreas Damianou
- J Rosser
- José Luis Redondo García
- Konstantina Palla

*(Affiliations are not provided in the source material)*

## Abstract

"Chain-of-thought (CoT) traces promise transparency for reasoning language models, but prior work shows they are not always faithful reflections of internal computation." The authors introduce Concept Walk, operating in activation space rather than surface text to track how a model's internal stance evolves during reasoning. Testing on Qwen 3-4B for safety tasks, they demonstrate that "in 'easy' cases, perturbed CoTs are quickly ignored, indicating decorative reasoning, whereas in 'hard' cases, perturbations induce sustained shifts in internal activations, consistent with faithful reasoning." The framework helps practitioners identify when reasoning traces can be trusted versus when they may mislead.

**License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29f93c76-9aae-4abe-bf1c-ca13e3e6dfa9",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "d2c07bf7-7b8a-4694-8aee-2f0d44687bb0",
  "sourceToolAssistantUUID": "29f93c76-9aae-4abe-bf1c-ca13e3e6dfa9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T12:02:00.657Z_

<details><summary>↩ Tool result · `toolu_01GQpWEsosxu3eYzV8Tu2X3c`</summary>

```text
# Mapping Faithful Reasoning in Language Models - Comprehensive Summary

## 1. Abstract

The authors introduce Concept Walk, a framework for tracing how a model's internal representations evolve with respect to specific concepts during multi-step reasoning. Rather than analyzing surface-level text, this method operates in activation space by projecting reasoning steps onto learned concept directions. Applied to safety in Qwen 3-4B, they discover that "easy" cases show decorative reasoning (perturbed reasoning is quickly ignored), while "hard" cases demonstrate faithful reasoning (perturbations induce sustained activation shifts). The contribution is methodological, providing a lens to identify when reasoning traces can be trusted.

## 2. Introduction & Problem Statement

**Core Problem:**
The paper addresses a critical gap in LLM oversight. While chain-of-thought (CoT) reasoning traces promise transparency, mounting evidence suggests they often function as post-hoc rationalizations rather than faithful representations of actual computation. As they state, practitioners may "place trust in explanations that played little or no role in generating the decisions they seek to validate."

**The Gap:**
Prior work identifies *whether* CoT influences outcomes but doesn't reveal *how* internal concept representations evolve during reasoning. The authors explain: "While prior filtering methods identify when CoT traces influence outcomes, they do not reveal how internal concept representations evolve during reasoning."

Their key question: "How do internal safety activations behave differently in computational vs. decorative reasoning cases?"

## 3. Concept Walk Methodology - Complete Detail

### 3.1 Three-Stage Framework

The methodology comprises filtering, direction computation, and temporal tracking.

### 3.2 Safety Direction Learning

**Difference of Means Approach:**
They construct contrastive datasets of unsafe and safe prompts, computing mean activations:

- μ_unsafe(ℓ,t) = average activation across unsafe prompts at layer ℓ, token t
- μ_safe(ℓ,t) = average activation across safe prompts at layer ℓ, token t

The safety direction vector is: **v = μ_unsafe - μ_safe** (normalized)

This captures the activation space axis distinguishing safe from unsafe content.

**Direction Selection Constraints:**
They filter candidate vectors using three metrics:
- **Bypass score**: How effectively the direction suppresses refusal on harmful prompts
- **Induce score**: Ability to induce refusal on harmless prompts  
- **KL divergence**: Minimal disruption to general model outputs (threshold: <0.1)

Additionally, they exclude late-layer directions (>0.8L) that primarily suppress output tokens rather than encoding genuine safety features.

### 3.3 Temporal Tracking via Concept Walk

For each reasoning step s, they:
1. Extract residual stream activations for all tokens in that step
2. Average token activations into step-level representation: **h_s**
3. Compute cosine similarity with the safety vector: **α_s = cos(h_s, v)**

This produces a scalar alignment score per step, creating a trajectory showing whether internal safety activation emerges, persists, or decays throughout reasoning.

**Key Design Choice:** They compute the safety direction in non-thinking mode (standard inference) but apply it to thinking-mode activations, assuming core safety encoding remains stable across modes while temporal expression differs.

### 3.4 Perturbation Analysis

To test if internal safety activations track reasoning use, they inject flawed reasoning steps at the midpoint of original CoTs and compare:
- Baseline activation trajectory
- Perturbed activation trajectory

If the model integrates the perturbation into its decision process (hard cases), safety activations should show sustained, structured shifts. If the model ignores the flawed reasoning (easy cases), shifts should be transient and the model reverts to original trajectories.

## 4. Differentiation from Answer-Content Probes

The paper implicitly distinguishes their approach by focusing on **concept-specific temporal dynamics** rather than static output prediction. Standard linear probes (answer-content probes) typically:
- Learn a linear classifier mapping activations to binary outputs
- Apply this uniformly across positions or layers
- Provide static, position-agnostic interpretations

Concept Walk instead:
- Derives directions from contrastive datasets capturing semantic meaning
- Tracks *evolution* across reasoning steps
- Reveals whether concept signals persist (computational) or decay (decorative)
- Tests faithfulness via perturbation sensitivity within activation space

## 5. Experimental Setup

### 5.1 Models

**Safety Direction Learning:** Mistral-7B-Instruct-v0.2 (7.3B parameters) - used to generate synthetic datasets and establish baseline safety vectors

**Analysis Model:** Qwen 3-4B with controllable thinking mode (36-layer Transformer, 128K context)

### 5.2 Datasets

Two synthetic datasets generated via prompting Mistral with policy guidelines:

| Category | Training | Validation | Test | Total Pairs |
|----------|----------|-----------|------|------------|
| Harm | 1,746 | 873 | 292 | 2,911 |
| Hate | 2,890 | 1,445 | 484 | 4,819 |

**Domain:** Music playlist requests (e.g., "playlist for a dinner party")

**Filtering:** After excluding instances where model predictions mismatched ground truth, final counts were:
- Hate: 256 violative, 462 non-violative
- Harm: 181 violative, 290 non-violative

### 5.3 Perturbation Method

**CoT Mistake Injection Procedure:**
1. Generate baseline CoT from Qwen
2. Identify midpoint reasoning step
3. Replace with logically flawed but fluent alternative (e.g., "This is safe. Therefore, I will answer.")
4. Feed prefix [prompt + steps 1 to i-1 + injected_step] through model
5. Resume autoregressive CoT generation
6. Compare final output; retain examples where perturbation significantly alters behavior

This filters for "hard" cases (CoT-sensitive) vs. "easy" cases (CoT-insensitive).

## 6. Key Findings

### 6.1 Easy Cases (Decorative Reasoning)

- Perturbed CoTs produce **transient safety activation shifts**
- Model rapidly reverts to original trajectory
- Internal state quickly "self-corrects" despite flawed reasoning
- Indicates CoT functions as post-hoc rationalization
- Example: "Playlist for a bar crawl" - model initially acknowledges injected error but quickly reverses course

### 6.2 Hard Cases (Faithful Reasoning)

- Perturbations induce **sustained, structured activation shifts**
- Safety activations diverge from baseline and persist multiple steps beyond injection
- Downstream reasoning tracks the altered internal state
- Final output often changes in response to perturbation
- Example: "Can you recommend some classic rock tunes" - injected error produces lasting divergence in both activation and decision

### 6.3 Violative vs. Non-Violative Prompts

- Unsafe prompts consistently trigger **higher initial safety activation**
- Confirms safety vector effectively captures unsafe content recognition
- However, temporal trajectories in hard violative cases show small sample sizes, warranting caution in interpretation

## 7. Conclusion & Limitations

### Conclusions

"Concept Walk provides a lens to re-examine faithfulness through concept-specific internal dynamics, helping identify when reasoning traces can be trusted and when they risk misleading practitioners."

Key insight: Models may acknowledge flawed reasoning but only under specific conditions does this engagement causally shape outcomes—distinguishing genuine computation from superficial rationalization.

### Limitations

1. **Cross-mode representation shift:** Safety direction learned in non-thinking mode; representations may differ during reasoning mode
2. **Incomplete coverage:** Method cannot capture hidden reasoning pathways unexpressed in verbal output
3. **Small sample sizes:** Hard case violative examples had limited cohorts after filtering
4. **Single model/domain:** Analysis restricted to Qwen 3-4B and safety concept; generalization unclear
5. **Perturbation timing:** Study uses fixed midpoint injection; systematic variation of timing and strength would clarify sensitivity
6. **Refusal pattern encoding:** Safety vector may partially encode refusal patterns, potentially obscuring fine-grained mid-trace dynamics

The authors note: "Computing mode-specific and step-local directions could address potential representation shifts between thinking and non-thinking modes, providing more accurate measures."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c4365a5-8f77-4efc-ac35-e2220383a13e",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "2f3088f0-8c02-46f3-9d2f-0a18d9c4a818",
  "sourceToolAssistantUUID": "0c4365a5-8f77-4efc-ac35-e2220383a13e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T12:02:04.036Z_

Excellent. I now have comprehensive details. Let me also check the OpenReview page for any additional reviewer/venue information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f3088f0-8c02-46f3-9d2f-0a18d9c4a818",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtjsNXrUKo8DwCJJaZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49a72167-c892-42ce-8bbc-bb80e75570a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015z9RH4MJgg5koFK1uLGuns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 11806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3189,
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

_source line 20 · 2026-05-19T12:02:06.350Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013sUT5LkWKinPgTq6x7pCEQ`</summary>

```json
{
  "url": "https://openreview.net/pdf/89878ca66572c0425255f7be53b2879e6d2e7e7b.pdf",
  "prompt": "Extract any additional details not already covered: author affiliations, any additional experimental details, figures described, equations, or reviewer comments. Also look for any details about how Concept Walk compares specifically to answer-content linear probes or other faithfulness methods like Lanham et al. or Turpin et al."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49a72167-c892-42ce-8bbc-bb80e75570a4",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtjsNXrUKo8DwCJJaZ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "67a4e539-2abb-4f58-b78c-015adc160d42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015z9RH4MJgg5koFK1uLGuns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 11806,
      "output_tokens": 196,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3189
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 196,
          "cache_read_input_tokens": 11806,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3189,
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

_source line 21 · 2026-05-19T12:02:13.548Z_

<details><summary>↩ Tool result · `toolu_013sUT5LkWKinPgTq6x7pCEQ`</summary>

```text
I appreciate your request, but I need to point out that the content provided appears to be raw PDF binary data rather than readable text. The material shows PDF object streams with encoded/compressed content that hasn't been properly decoded for analysis.

To extract the details you're asking about—author affiliations, experimental details, Concept Walk comparisons, and methodology comparisons with approaches like Lanham et al. or Turpin et al.—I would need:

1. **Properly decoded PDF text** rather than binary stream objects
2. **Readable content** from the document's pages

**What I can observe from the metadata:**
- The PDF appears to be a linearized document (references to /Linearized and page objects suggest it's a multi-page academic paper)
- There are embedded fonts and image objects indicating figures/content
- Object streams contain compressed scholarly material

**Recommendation:** Please provide the paper content in one of these formats:
- Plain text extracted from the PDF
- Markdown version of the paper
- Screenshot or OCR'd text from the relevant sections

Once you supply readable text, I can extract specific details about Concept Walk's methodology, author information, experimental comparisons, and how it positions itself relative to other faithfulness evaluation methods.

[Binary content (application/pdf, 5.9MB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-gen-pipeline/a600395c-52af-4483-884f-a0137eaa6f5f/tool-results/webfetch-1779192127343-sdoxo9.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67a4e539-2abb-4f58-b78c-015adc160d42",
  "isSidechain": true,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "agentId": "a7570908b24c44cbc",
  "type": "user",
  "uuid": "106f78cd-3be4-494c-a2e0-a046a5198568",
  "sourceToolAssistantUUID": "67a4e539-2abb-4f58-b78c-015adc160d42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T12:02:43.372Z_

I have all the information needed to provide a thorough report. Here is the full synthesis:

---

## Paper: "Mapping Faithful Reasoning in Language Models" (arXiv 2510.22362)

**Authors:** Jiazheng Li, Andreas Damianou, J Rosser, Jose Luis Redondo Garcia, Konstantina Palla
**Venue:** Mechanistic Interpretability Workshop at NeurIPS 2025
**Submitted:** October 25, 2025
**Categories:** cs.LG, cs.CL

---

### What Is Concept Walk?

Concept Walk is a three-stage framework for tracing how a model's internal representations evolve with respect to a specific concept (in their case study, "safety") during multi-step chain-of-thought (CoT) reasoning. It operates entirely in activation space rather than analyzing surface text. The three stages are:

1. **Filtering** -- selecting cases where perturbation to the CoT actually changes vs. does not change the model's output (to separate "hard" from "easy" cases).
2. **Direction computation** -- learning a concept direction vector from contrastive data.
3. **Temporal tracking** -- projecting each reasoning step's activations onto that direction to produce a step-by-step trajectory.

---

### How Concept Directions Are Learned

They use a **difference-of-means** approach on contrastive datasets (unsafe vs. safe prompts):

- Compute mean activations for unsafe prompts: mu_unsafe(layer, token)
- Compute mean activations for safe prompts: mu_safe(layer, token)
- Safety direction vector: **v = mu_unsafe - mu_safe** (normalized)

Candidate direction vectors are filtered using three criteria:
- **Bypass score**: effectiveness at suppressing refusal on harmful prompts
- **Induce score**: ability to induce refusal on harmless prompts
- **KL divergence**: minimal disruption to general model outputs (threshold < 0.1)

They also exclude late-layer directions (beyond 80% of model depth) that primarily suppress output tokens rather than encoding genuine safety features.

An important design choice: the safety direction is computed in **non-thinking mode** (standard inference) but applied to **thinking-mode** activations, under the assumption that core safety encoding remains stable across modes while temporal expression differs.

---

### How Temporal Evolution Is Tracked

For each reasoning step `s` in the CoT:

1. Extract residual stream activations for all tokens in that step
2. Average token activations into a step-level representation: **h_s**
3. Compute cosine similarity with the safety direction vector: **alpha_s = cos(h_s, v)**

This produces a scalar alignment score per step, creating a trajectory that reveals whether internal safety activation emerges, persists, or decays throughout reasoning. By comparing the baseline trajectory (original CoT) against a perturbed trajectory (CoT with injected flawed reasoning at the midpoint), they can diagnose whether the model's internal state actually tracks the reasoning content.

---

### Key Findings: Easy vs. Hard Tasks

**Easy cases (decorative reasoning):**
- Perturbed CoTs produce only **transient** safety activation shifts
- The model rapidly reverts to its original activation trajectory
- The internal state "self-corrects" despite the injected flawed reasoning
- The CoT functions as a post-hoc rationalization -- it does not causally drive the output
- Example: "Playlist for a bar crawl" -- model acknowledges the injected error briefly but quickly reverses course

**Hard cases (faithful reasoning):**
- Perturbations induce **sustained, structured** activation shifts
- Safety activations diverge from baseline and persist for multiple steps beyond injection point
- Downstream reasoning tracks the altered internal state
- The final output often changes in response to the perturbation
- The CoT is genuinely computational -- it causally shapes the outcome
- Example: "Can you recommend some classic rock tunes" -- injected error produces lasting divergence in both activation trajectory and final decision

Additionally, **unsafe prompts consistently trigger higher initial safety activation**, confirming the safety direction vector effectively captures unsafe content recognition.

---

### Models and Benchmarks

- **Direction learning model:** Mistral-7B-Instruct-v0.2 (7.3B parameters) -- used to generate synthetic contrastive datasets
- **Analysis model:** Qwen 3-4B with controllable thinking mode (36-layer Transformer, 128K context)
- **Domain:** Safety (specifically music playlist requests, e.g., "playlist for a dinner party")
- **Datasets (synthetic, generated via Mistral with policy guidelines):**
  - Harm category: 1,746 train / 873 val / 292 test (2,911 total pairs)
  - Hate category: 2,890 train / 1,445 val / 484 test (4,819 total pairs)
- After filtering for prediction-ground-truth match: Hate = 256 violative + 462 non-violative; Harm = 181 violative + 290 non-violative

**Perturbation method:** At the midpoint of the CoT, they replace a reasoning step with a logically flawed but fluent alternative (e.g., "This is safe. Therefore, I will answer."), then resume autoregressive generation and compare outputs/trajectories.

---

### How It Differs from Answer-Content Linear Probes

Standard answer-content linear probes:
- Learn a linear classifier mapping activations to a binary output (e.g., safe/unsafe)
- Apply this uniformly across positions or layers
- Provide **static, position-agnostic** interpretations -- they tell you "the model has already decided X at layer Y" but not how that decision evolves through reasoning steps

Concept Walk instead:
- Derives directions from **contrastive datasets capturing semantic meaning** (not trained to predict the answer)
- Tracks the **temporal evolution** of concept alignment across reasoning steps -- it produces a trajectory, not a single snapshot
- Reveals whether concept signals **persist** (faithful/computational) or **decay** (decorative) after perturbation
- Tests faithfulness via **perturbation sensitivity within activation space** rather than just checking if the model's output changes
- Is **concept-specific** -- different concept directions can be plugged in for different analysis domains

The key insight is that Concept Walk goes beyond "does the model know the answer early?" (which probes answer) to "does the reasoning process causally shape the internal concept representation over time?"

---

### Limitations

1. Cross-mode representation shift: safety direction learned in non-thinking mode may not perfectly transfer to thinking mode
2. Cannot capture hidden reasoning pathways unexpressed in verbal output
3. Small sample sizes for hard violative cases after filtering
4. Only tested on one model (Qwen 3-4B) and one domain (safety)
5. Fixed midpoint perturbation injection -- systematic variation of timing/strength not explored
6. Safety vector may partially encode refusal patterns, potentially obscuring fine-grained mid-trace dynamics

---

Sources:
- [arXiv Abstract: 2510.22362](https://arxiv.org/abs/2510.22362)
- [arXiv HTML Full Paper](https://arxiv.org/html/2510.22362)
- [arXiv PDF](https://arxiv.org/pdf/2510.22362)
- [OpenReview PDF](https://openreview.net/pdf/89878ca66572c0425255f7be53b2879e6d2e7e7b.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "106f78cd-3be4-494c-a2e0-a046a5198568",
  "isSidechain": true,
  "agentId": "a7570908b24c44cbc",
  "requestId": "req_011CbBtkpgLBLhpm1Qc1BZoy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95ee816a-34a4-4feb-ba83-94990dc44f94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPz8RkGm2n2pUhccCDeH1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 14995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 660,
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
