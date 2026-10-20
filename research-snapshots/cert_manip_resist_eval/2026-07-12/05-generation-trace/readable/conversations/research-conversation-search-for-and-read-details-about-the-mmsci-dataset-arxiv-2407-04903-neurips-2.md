# Research conversation: Search for and read details about the MMSci dataset (arXiv:2407.04903, NeurIPS 2024 Workshop) for scientific figure unde

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a87c831bd24e0caa5.jsonl`
- **Structured JSON:** [`1b9fa7c556b589d537a6.json`](../../sessions/1b/1b9fa7c556b589d537a6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

68 recorded events

### User

_source line 1 · 2026-05-28T03:25:36.810Z_

Search for and read details about the MMSci dataset (arXiv:2407.04903, NeurIPS 2024 Workshop) for scientific figure understanding. I need to understand:

1. How many figures/examples does it contain?
2. What are the 72 scientific disciplines covered?
3. What are the original evaluation metrics (CIDEr/BLEU)?
4. What do the reference captions look like - are they figure captions from Nature Communications papers?
5. What kinds of tasks does it support (captioning, QA, etc.)?
6. What is the data format and annotation structure?

Also search for how other papers have re-annotated or re-purposed existing captioning datasets with rubric-based evaluation. Try queries like:
- "MMSci dataset scientific figure understanding NeurIPS 2024"
- "rubric annotation scientific figure captioning"
- "converting reference-based metrics to rubric evaluation"

I need this to specify a detailed re-annotation pipeline for converting MMSci from reference-based evaluation to rubric-based evaluation for non-verifiable RL training. Report your findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "6d0e83cd-c186-4e8e-8727-7dd5c6077eb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-28T03:25:36.813Z_

```json
{
  "parentUuid": "6d0e83cd-c186-4e8e-8727-7dd5c6077eb7",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "d677dc7b-f7e3-4ddc-91cd-ba2e5a72506f",
  "timestamp": "2026-05-28T03:25:36.813Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-28T03:25:36.814Z_

```json
{
  "parentUuid": "d677dc7b-f7e3-4ddc-91cd-ba2e5a72506f",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "15f8d626-2ed2-4bd6-bbd6-d2a4a421f7df",
  "timestamp": "2026-05-28T03:25:36.814Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-28T03:25:39.531Z_



I'll search for information about the MMSci dataset and rubric-based evaluation approaches using web search. Let me fetch the tool schema first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15f8d626-2ed2-4bd6-bbd6-d2a4a421f7df",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFeA5DBUaAMzPCEUWYw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c93351c-09b7-4afa-aad2-9ebc02adc95f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S17F1NE4SfBG5sFdaDKXWJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 7411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1564,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-28T03:25:39.885Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019YHVNwAtSHzuGywCfGYF2X`</summary>

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
  "parentUuid": "8c93351c-09b7-4afa-aad2-9ebc02adc95f",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFeA5DBUaAMzPCEUWYw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f87c6a26-06e0-412b-918e-829daa39fef2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S17F1NE4SfBG5sFdaDKXWJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1564,
      "cache_read_input_tokens": 7411,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 7411,
          "cache_creation_input_tokens": 1564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1564,
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

_source line 6 · 2026-05-28T03:25:39.888Z_

<details><summary>↩ Tool result · `toolu_019YHVNwAtSHzuGywCfGYF2X`</summary>

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
  "parentUuid": "f87c6a26-06e0-412b-918e-829daa39fef2",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "a0b7efb8-e8f7-49c0-9d69-3394eb1f4f49",
  "sourceToolAssistantUUID": "f87c6a26-06e0-412b-918e-829daa39fef2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-28T03:25:43.236Z_



Now let me run multiple searches in parallel to gather information about the MMSci dataset and rubric-based evaluation approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0b7efb8-e8f7-49c0-9d69-3394eb1f4f49",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFePUc819BtaKWMzbSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54dfabdc-c54d-4084-915f-3bc690152ec4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKdbQVCHmheucdirkwZLRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 8 · 2026-05-28T03:25:43.708Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WvLi8ZMjGHrKcB8QZi8tqE`</summary>

```json
{
  "query": "MMSci dataset scientific figure understanding NeurIPS 2024 arXiv 2407.04903"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54dfabdc-c54d-4084-915f-3bc690152ec4",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFePUc819BtaKWMzbSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "063fd371-5c1c-4d5a-95a9-4493616f0e76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKdbQVCHmheucdirkwZLRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 9 · 2026-05-28T03:25:44.179Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LyTq4D2P4L3rNaCwTnLVWX`</summary>

```json
{
  "query": "MMSci dataset 72 scientific disciplines Nature Communications figures captioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "063fd371-5c1c-4d5a-95a9-4493616f0e76",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFePUc819BtaKWMzbSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d166f161-0323-4597-845f-6db2d411a2b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKdbQVCHmheucdirkwZLRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 10 · 2026-05-28T03:25:44.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012DTSJAXDGkoNPiDS59gC4j`</summary>

```json
{
  "query": "rubric annotation scientific figure captioning converting reference-based metrics rubric evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d166f161-0323-4597-845f-6db2d411a2b0",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFePUc819BtaKWMzbSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4c0d236-adc3-4426-af22-6209409fc0cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKdbQVCHmheucdirkwZLRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1133,
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

_source line 11 · 2026-05-28T03:25:44.878Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013gEeKraBKqjcUT3tq2LYFU`</summary>

```json
{
  "query": "rubric-based evaluation non-verifiable rewards reinforcement learning vision language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4c0d236-adc3-4426-af22-6209409fc0cd",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFePUc819BtaKWMzbSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26fa9ae4-d261-4191-b67b-9ba1418ad897",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKdbQVCHmheucdirkwZLRq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1133,
      "cache_read_input_tokens": 8975,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1133
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 249,
          "cache_read_input_tokens": 8975,
          "cache_creation_input_tokens": 1133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1133,
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

_source line 12 · 2026-05-28T03:25:50.899Z_

<details><summary>↩ Tool result · `toolu_01WvLi8ZMjGHrKcB8QZi8tqE`</summary>

```text
Web search results for query: "MMSci dataset scientific figure understanding NeurIPS 2024 arXiv 2407.04903"

Links: [{"title":"[2407.04903] MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/abs/2407.04903"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240704903L/abstract"},{"title":"MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://arxiv.org/html/2407.04903v1"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/html/2407.04903"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal   Scientific Understanding","url":"https://arxiv.org/pdf/2407.04903"},{"title":"Shraman Pramanick on X: \"I am at NeurIPS 2024 at Vancouver. I'll be presenting SPIQA on Wednesday AM Poster Session Booth #3700! 📜 arXiv: https://t.co/UoqZ82ibvy 🗄️SPIQA dataset: https://t.co/JvIQibFDGI 👨‍💻 github: https://t.co/Ns4KqVXIAG In this work, we have done a comprehensive analysis of\" / X","url":"https://x.com/Shramanpramani2/status/1866900538476073350"}]

Based on the search results, here's what I found about the MMSci dataset:

## MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding

MMSci is a comprehensive dataset compiled from peer-reviewed Nature Communications articles covering 72 scientific fields, encompassing complex visualizations such as schematic diagrams, microscopic images, and experimental data which require graduate-level expertise to interpret.

**Dataset Composition:**
The source dataset comprises 131,393 articles and 742,273 figures.

**Research Focus:**
Current datasets and benchmarks primarily focus on simple charts or other relatively straightforward figures from limited science domains, which the MMSci dataset addresses with more complex scientific visualizations.

**Evaluation:**
The researchers evaluated 19 proprietary and open-source models on two benchmark tasks, figure captioning and multiple-choice, and conducted human expert annotation. GPT-4o and Claude-3.5-Sonnet emerged as the leading models, significantly outperforming other evaluated models.

**Publication:**
The paper arXiv:2407.04903 was submitted in July 2024 and last revised in February 2025. Code and data are available at https://github.com/Leezekun/MMSci


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "063fd371-5c1c-4d5a-95a9-4493616f0e76",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "91d823b8-340a-4589-b660-b0c204e3bfc9",
  "sourceToolAssistantUUID": "063fd371-5c1c-4d5a-95a9-4493616f0e76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T03:25:51.517Z_

<details><summary>↩ Tool result · `toolu_01LyTq4D2P4L3rNaCwTnLVWX`</summary>

```text
Web search results for query: "MMSci dataset 72 scientific disciplines Nature Communications figures captioning"

Links: [{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/html/2407.04903v2"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal   Scientific Understanding","url":"https://arxiv.org/pdf/2407.04903"},{"title":"[Literature Review] MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://www.themoonlight.io/en/review/mmsci-a-dataset-for-graduate-level-multi-discipline-multimodal-scientific-understanding"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding | OpenReview","url":"https://openreview.net/forum?id=DEOV74Idsg"},{"title":"[PDF] MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MMSci:-A-Dataset-for-Graduate-Level-Multimodal-Li-Yang/e073a2fda0c4d6198ba231c8e9df10f4f2ba1c51"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240704903L/abstract"},{"title":"[2407.04903] MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/abs/2407.04903"},{"title":"Papers with Code - MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://paperswithcode.com/paper/mmsci-a-multimodal-multi-discipline-dataset"},{"title":"MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://arxiv.org/html/2407.04903v1"},{"title":"(PDF) MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://www.researchgate.net/publication/382080769_MMSci_A_Multimodal_Multi-Discipline_Dataset_for_PhD-Level_Scientific_Comprehension"}]

Based on the search results, here's what I found about the MMSci dataset:

## Overview
MMSci is a multimodal, multi-discipline dataset comprising high-quality, peer-reviewed articles and figures from 72 scientific disciplines, predominantly within the natural sciences.

## Dataset Composition
The dataset encompasses 72 scientific disciplines, containing 131k articles and 742k figures across diverse visualization types. The dataset includes peer-reviewed articles from Nature Communications, spanning 72 disciplines and covering a wide range of natural science subjects.

## Figure Types
The dataset encompasses complex visualizations such as schematic diagrams, microscopic images, and experimental data which require graduate-level expertise to interpret. More specifically, visualization types include Quantitative Data Visualization Charts (53.5% of the figures), Schematic Diagrams (13.2%), Microscopic Photographs (14.7%), Simulated Images (3.4%), Geographical and Environmental Maps (1.2%), and Macroscopic Photographs (5.2%).

## Benchmark Tasks
The researchers evaluated 19 proprietary and opensource models on two benchmark tasks, figure captioning and multiple-choice, and conducted human expert annotation.

## Key Findings
Fine-tuning Qwen2-VL-7B with their task-specific data achieved better performance than GPT-40 and even human experts in multiple-choice evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d166f161-0323-4597-845f-6db2d411a2b0",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "5254f949-9aed-4ebd-a349-a771851cb87b",
  "sourceToolAssistantUUID": "d166f161-0323-4597-845f-6db2d411a2b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T03:25:51.756Z_

<details><summary>↩ Tool result · `toolu_013gEeKraBKqjcUT3tq2LYFU`</summary>

```text
Web search results for query: "rubric-based evaluation non-verifiable rewards reinforcement learning vision language models"

Links: [{"title":"Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training","url":"https://arxiv.org/html/2602.01511v1"},{"title":"Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training | Request PDF","url":"https://www.researchgate.net/publication/400369272_Alternating_Reinforcement_Learning_for_Rubric-Based_Reward_Modeling_in_Non-Verifiable_LLM_Post-Training"},{"title":"Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.01511"},{"title":"Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training","url":"https://arxiv.org/pdf/2602.01511"},{"title":"[2602.01511] Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training","url":"https://arxiv.org/abs/2602.01511"}]

Based on the search results, here's what I found about rubric-based evaluation with non-verifiable rewards in reinforcement learning:

## Key Findings

In complex non-verifiable domains like creative writing or open-ended instruction following, scalar or pairwise judgments often fail to capture response quality, so recent advancements have shifted toward rubric-based reward modeling where models explicitly generate structured criteria to ground their judgments.

By decomposing evaluation into interpretable dimensions, rubric-based models offer transparency and improve generalization across prompt-specific evaluation axes.

## Proposed Solution: Rubric-ARM

A recent research contribution addresses this challenge: Rubric-ARM is a framework that jointly optimizes a rubric generator and a judge using reinforcement learning from preference feedback, treating rubric generation as a latent action learned to maximize judgment accuracy, unlike existing methods that rely on static rubrics or disjoint training pipelines.

The approach introduces an alternating optimization strategy to mitigate the non-stationarity of simultaneous updates, providing theoretical analysis that demonstrates how this schedule reduces gradient variance during training.

The research indicates this is an active and evolving area, with recent papers published in February 2026 focusing on improving how reinforcement learning can work with rubric-based evaluations for non-verifiable tasks in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26fa9ae4-d261-4191-b67b-9ba1418ad897",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "94e0f5eb-fe30-48f6-a15a-a14ee0edcc20",
  "sourceToolAssistantUUID": "26fa9ae4-d261-4191-b67b-9ba1418ad897",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T03:25:51.990Z_

<details><summary>↩ Tool result · `toolu_012DTSJAXDGkoNPiDS59gC4j`</summary>

```text
Web search results for query: "rubric annotation scientific figure captioning converting reference-based metrics rubric evaluation"

Links: [{"title":"TechImage-Bench: Rubric‑Based Evaluation for Technical Image Generation","url":"https://arxiv.org/html/2512.12220"},{"title":"SciCap Project: Advancing Figure Captioning","url":"https://www.emergentmind.com/topics/scicap-project"},{"title":"RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning","url":"https://arxiv.org/html/2603.09160"},{"title":"Rubric-Based Evaluation - Ragas","url":"https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/rubrics_based/"},{"title":"RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning","url":"https://arxiv.org/pdf/2603.09160"},{"title":"SciFig: Towards Automating Scientific Figure Generation","url":"https://arxiv.org/pdf/2601.04390"},{"title":"CLIPScore: A Reference-free Evaluation Metric for Image Captioning","url":"https://arxiv.org/pdf/2104.08718"},{"title":"Rubric Evaluation | Definition & Examples","url":"https://encord.com/glossary/rubric-evaluation/"},{"title":"An Examination of the Robustness of Reference-Free Image Captioning   Evaluation Metrics","url":"https://arxiv.org/pdf/2305.14998"}]

Based on the search results, here are the key findings related to rubric annotation, scientific figure captioning, and converting reference-based metrics to rubric evaluation:

## Rubric-Based Evaluation for Scientific Figures

A rubric-based evaluation framework has been introduced that analyzes real scientific figures to extract evaluation rubrics and automatically generates comprehensive evaluation criteria. This approach represents a shift from traditional reference-based metrics.

## Converting Reference-Based Metrics to Rubric Evaluation

The research demonstrates an important conversion principle: Converting abstract criteria into binary, unit-test-like questions yields scores that are more reliable, interpretable, and actionable than holistic ratings, while remaining scalable with LLM-based judging.

## Traditional Reference-Based Metrics

For scientific figure captioning, captioning systems are assessed across both automatic, reference-based metrics and human evaluation protocols. Traditional reference-based metrics include ROUGE-1/2/L metrics measuring recall and precision of unigrams, bigrams, and longest common subsequences.

## Rubric-Based Approaches for Caption Improvement

Recent work on RubiCap demonstrates practical implementation: The approach assembles a diverse committee of candidate captions, then employs an LLM rubric writer to extract consensus strengths and diagnose deficiencies, converting these insights into explicit evaluation criteria that enable decomposed holistic quality assessment and replace coarse scalar rewards with structured, multi-faceted evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4c0d236-adc3-4426-af22-6209409fc0cd",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "8d21e13f-164f-41c8-a393-ff74e2d1c862",
  "sourceToolAssistantUUID": "a4c0d236-adc3-4426-af22-6209409fc0cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-28T03:25:54.596Z_

Excellent results. Now let me fetch the detailed paper content and related resources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d21e13f-164f-41c8-a393-ff74e2d1c862",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFfGyxyGzAXMhVwFHKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01d1e93e-5075-44d7-b804-a3a5eef4d9d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G76WjSbSbFyoU7WoPU4Udp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 679,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 10108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 17 · 2026-05-28T03:25:58.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RcjXqmwQ1UHSF78KnpLUzT`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.04903",
  "prompt": "Extract ALL details about the MMSci dataset: 1) Exact number of figures, articles, and examples in train/val/test splits. 2) The complete list of 72 scientific disciplines. 3) Evaluation metrics used (CIDEr, BLEU, etc.) with specific scores. 4) What the reference captions look like - are they original figure captions from Nature Communications papers? 5) Tasks supported (captioning, QA, multiple choice, etc.). 6) Data format and annotation structure - how is each example structured? What fields does each record contain? 7) How were figures and captions collected and processed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01d1e93e-5075-44d7-b804-a3a5eef4d9d8",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFfGyxyGzAXMhVwFHKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b101f38f-1bf8-4de3-866d-c76011f23961",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G76WjSbSbFyoU7WoPU4Udp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 679,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 10108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 18 · 2026-05-28T03:26:01.096Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CbdKaQGj28zCKE6SViK6jH`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.09160",
  "prompt": "Extract all details about the RubiCap approach: 1) How does it convert reference-based captioning evaluation to rubric-based evaluation? 2) What is the rubric generation pipeline? 3) How are rubrics structured? 4) How is the reward computed from rubrics for RL training? 5) What datasets were used? 6) What is the annotation process for creating rubrics from existing captions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b101f38f-1bf8-4de3-866d-c76011f23961",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFfGyxyGzAXMhVwFHKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa3d9fbb-0710-4b9e-aa8e-1eb21f15e543",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G76WjSbSbFyoU7WoPU4Udp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 679,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 10108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2715,
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

_source line 19 · 2026-05-28T03:26:03.062Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WAMVzMEyFdksALVpNK4iGH`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.01511v1",
  "prompt": "Extract all details about Rubric-ARM: 1) How does it define rubrics for non-verifiable tasks? 2) What is the rubric generation process? 3) How are rubrics used as reward signals for RL? 4) What is the alternating optimization strategy? 5) How does it handle converting from reference-based to rubric-based evaluation? 6) What datasets and tasks were evaluated?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa3d9fbb-0710-4b9e-aa8e-1eb21f15e543",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFfGyxyGzAXMhVwFHKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "975cb2d1-cd97-4529-8a67-30001752f8e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G76WjSbSbFyoU7WoPU4Udp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 679,
      "cache_creation_input_tokens": 2715,
      "cache_read_input_tokens": 10108,
      "output_tokens": 557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2715
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 679,
          "output_tokens": 557,
          "cache_read_input_tokens": 10108,
          "cache_creation_input_tokens": 2715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2715,
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

_source line 20 · 2026-05-28T03:26:11.041Z_

<details><summary>↩ Tool result · `toolu_01RcjXqmwQ1UHSF78KnpLUzT`</summary>

```text
# MMSci Dataset Details

## Dataset Scale
- **Total figures:** 742,273
- **Total articles:** 131,393
- **Benchmark test set:** 1,418 articles
- **Benchmark validation set:** 1,414 articles
- **Training set:** 128,561 articles with 1,079,797 samples

## 72 Scientific Disciplines

The dataset spans five major categories:

**Physical Sciences (11 subjects):** Materials Science, Chemistry, Physics, Nanoscience and Technology, Optics and Photonics, Engineering, Energy Science, Mathematics and Computing, Astronomy, Mathematics Computing, Astronomy and Planetary Science

**Earth & Environmental Sciences (10 subjects):** Ecology, Climate Sciences, Solid Earth Sciences, Environmental Sciences, Biogeochemistry, Ocean Sciences, Environmental Social Sciences, Natural Hazards, Planetary Science, Hydrology, Limnology, Space Physics

**Biological Sciences (28 subjects):** Cell Biology, Biochemistry, Microbiology, Neuroscience, Molecular Biology, Genetics, Cancer, Immunology, Biological Techniques, Computational Biology, Biotechnology, Biophysics, Structural Biology, Developmental Biology, Evolution, Plant Sciences, Physiology, Chemical Biology, Systems Biology, Drug Discovery, Stem Cells, Zoology, Psychology

**Health Sciences (13 subjects):** Diseases, Medical Research, Oncology, Health Care, Pathogenesis, Biomarkers, Cardiology, Gastroenterology, Endocrinology, Anatomy, Neurology, Molecular Medicine, others

**Scientific Community & Society (6 subjects):** Social Sciences, Scientific Community, Energy and Society, Agriculture, Developing World, Water Resources, Geography, Business, Forestry

## Evaluation Metrics

The paper reports these metrics:
- **Overlap-based:** "BLEU-2, ROUGE-L, METEOR" scores
- **Similarity:** BERTScore
- **Task-specific:** "CIDEr" for image descriptions
- **LLM-based:** Modified FActScore (0-1 scale) and G-Eval (1-5 scale)

Example scores show Qwen2-VL-7B-MMSci achieving FActScore 20.59 and G-Eval 3.54 on abstract-grounded captioning.

## Reference Captions

"Captions are authentic, sourced from peer-reviewed Nature Communications articles," averaging 153 words. These represent original author-written figure descriptions rather than synthetic annotations.

## Supported Tasks

1. **Figure Captioning:** Image-only and abstract-grounded settings
2. **Multiple-Choice Questions:** Three variants—
   - Figure-to-Caption matching
   - Subfigure-to-Subcaption matching
   - Subcaption-to-Subfigure matching
3. **Multi-turn Conversations:** About figure interpretation

## Figure Types (7 Categories)

- Quantitative Data Visualization Charts/Graphs
- Schematic Diagrams
- Microscopic Photographs
- Macroscopic Photographs
- Simulated Images
- Geographical/Environmental Maps
- Experimental Results Visualizations

## Data Collection & Processing

"Figures and captions were obtained from dedicated figures pages," extracted directly from Nature Communications websites rather than PDFs. "LaTeX expressions converted to plain text" for mathematical formulas. Sub-captions extracted via "regular expression matching" identifying alphabetical indices, yielding 514,054 sub-captions.

Human expert annotation verified classification quality (Cohen's Kappa 0.72 with GPT-4o).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b101f38f-1bf8-4de3-866d-c76011f23961",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "316f315f-dda0-45c7-a10b-f6b0cf715b0a",
  "sourceToolAssistantUUID": "b101f38f-1bf8-4de3-866d-c76011f23961",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T03:26:12.941Z_

<details><summary>↩ Tool result · `toolu_01WAMVzMEyFdksALVpNK4iGH`</summary>

```text
# Rubric-ARM: Key Details

## 1) Rubric Definition for Non-Verifiable Tasks
Rubric-ARM defines rubrics as "a structured set of evaluation criteria conditioned on a prompt," consisting of k criteria where each specifies "a distinct aspect of response quality (e.g., factual correctness, tone, or presentation)." This approach decomposes evaluation into interpretable dimensions rather than scalar scores.

## 2) Rubric Generation Process
The system uses a two-stage approach:
- **Stage I (SFT Warmup)**: Both the rubric generator and judge are fine-tuned on synthetic data from open-source datasets (UltraFeedback, SkyWork, Magpie, Synthetic Instruction Following)
- **Stage II (Alternating RL)**: The rubric generator learns to produce criteria that maximize the judge's preference prediction accuracy, treating rubrics as "latent actions" that guide reward modeling

## 3) Rubrics as Reward Signals for RL
Rubrics function as intermediate reasoning steps. The judge generates evaluation criteria (rubric) conditioned on a prompt and response pair, then uses these criteria to predict preferences. This provides "more precise reward signals" for downstream policy optimization compared to scalar rewards.

## 4) Alternating Optimization Strategy
Training alternates between two phases:
- **Judge Update**: Fixed rubric generator; judge learns to recover preference labels under sampled rubrics
- **Rubric Update**: Fixed judge; rubric generator learns to produce criteria that lead to correct predictions

This schedule reduces gradient variance by stabilizing the judge first, preventing "non-stationarity" from simultaneous updates.

## 5) Converting from Reference-Based to Rubric-Based Evaluation
The framework converts pairwise preference datasets into rubric-conditioned judgments. For policy training, it supports both offline RL (DPO with rubric-based labels) and online RL (GRPO using rubric-based rewards), with position bias mitigation through bidirectional querying.

## 6) Datasets and Tasks Evaluated
- **Reward Modeling**: 9 benchmarks including RewardBench, RM-Bench, RewardBench2, FollowBench, PPE-IFEval, InfoBench, IFBench, Arena-Hard, AlpacaEval, Creative Writing, WildBench, WritingPreferenceBench
- **Policy Training**: 6 benchmarks covering instruction-following (IFEval, InfoBench) and preference alignment (Arena-Hard, AlpacaEval, WildBench, Creative Writing)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "975cb2d1-cd97-4529-8a67-30001752f8e5",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "b1f4f0f7-295d-4a3c-8079-4d85520a2ade",
  "sourceToolAssistantUUID": "975cb2d1-cd97-4529-8a67-30001752f8e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T03:26:14.276Z_

<details><summary>↩ Tool result · `toolu_01CbdKaQGj28zCKE6SViK6jH`</summary>

```text
# RubiCap Framework: Converting Caption Evaluation to Rubric-Based RL

## 1. Reference-Based to Rubric-Based Conversion

RubiCap transforms traditional reference-based evaluation by moving away from lexical overlap metrics. Instead of comparing against fixed reference captions, the system "derives fine-grained, sample-specific evaluation criteria" by analyzing what a committee of diverse models produces. This shift enables open-ended assessment rather than metric-bound comparison.

## 2. Rubric Generation Pipeline

The pipeline operates in three sequential steps:

**Step 1 - Consensus Extraction:** The rubric writer identifies "key descriptive elements on which the majority of teacher captions agree," treating elements as ground truth only when at least ⌈K/2⌉ of K teachers describe them accurately.

**Step 2 - Deficiency Diagnosis:** The system performs comparative analysis between the student caption and teacher consensus, focusing on "discriminative deficiencies" categorized by severity: critical failures (3.0 weight), important gaps (2.0), and minor polish issues (1.0).

**Step 3 - Rubric Formulation:** Each diagnosed gap becomes a "binary, easy-to-check criterion" paired with severity weights, ensuring "every criterion must have a clear, objective pass/fail rule."

## 3. Rubric Structure

Rubrics are structured as sample-specific evaluation sets: ℛ(x,c^student,{c^teacher_k}) = {(r_m, w_m)}^M_m=1

Each rubric item contains:
- A specific criterion describing what to evaluate
- An evaluation rule with unambiguous pass/fail conditions
- A severity weight (1.0, 2.0, or 3.0)
- Justification tracing back to teacher consensus

The framework maintains "image-conditioned" rubrics that adapt to both visual content and the student's current failure modes.

## 4. Reward Computation for RL

An LLM judge evaluates each criterion, producing binary satisfaction scores (0 or 1). The normalized scalar reward follows:

**G(x,c^student) = Σ(w_m · ŷ_m) / Σw_m**

This represents "the proportion of identified quality gaps that the student has successfully addressed, weighted by their severity." The model then trains using GRPO with advantage estimates derived from these reward signals.

## 5. Datasets

Two datasets were utilized:
- **PixMoCap:** 50,000 images with "high-quality human-expert annotations" where three annotators independently produced descriptions, refined by LLMs
- **DenseFusion-4V-100K:** 50,000 images with "dense captions generated by GPT-4V and augmented with multiple perceptual attributes"

Each dataset held out 500 images for evaluation.

## 6. Rubric Annotation Process

Rather than human annotation, rubrics emerge through an automated pipeline:

1. **Teacher Committee Generation:** Five diverse VLMs (Gemini 2.5 Pro, GPT-5, Qwen2.5-VL-72B, Gemma-3-27B, Qwen3-VL-30B) generate candidate captions for each image
2. **Student Baseline Caption:** The current student policy produces an initial caption
3. **LLM-Driven Analysis:** An LLM rubric writer (Gemini 2.5 Pro) receives the image, student caption, and all teacher captions, then synthesizes targeted criteria

This avoids "prohibitively expensive" manual expert annotation while scaling "naturally" compared to human rubric creation, which the authors note is "cognitively demanding, even harder than writing captions themselves."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa3d9fbb-0710-4b9e-aa8e-1eb21f15e543",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "39716992-bf72-4d9a-b81b-562f5a590567",
  "sourceToolAssistantUUID": "fa3d9fbb-0710-4b9e-aa8e-1eb21f15e543",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-28T03:26:18.668Z_

Good, I have rich details. Let me now fetch the GitHub repo for data format details and search for more specific information about the evaluation metrics and discipline list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39716992-bf72-4d9a-b81b-562f5a590567",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFgvF6J7XEoJMpZSr2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5be3ec1-ef40-49b8-9955-17eec5c3656c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqpjvZEJoG8v7VyjRkN9Uk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 2986,
      "cache_read_input_tokens": 12823,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2986,
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

_source line 24 · 2026-05-28T03:26:20.562Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0142cvpVqoa9o2rfGt1ew1TR`</summary>

```json
{
  "url": "https://github.com/Leezekun/MMSci",
  "prompt": "Extract all details about: 1) The data format - what fields does each JSON record contain? 2) File structure and organization. 3) How to download and use the dataset. 4) Any annotation details or data schema. 5) Train/val/test split sizes. 6) Example data entries showing the structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5be3ec1-ef40-49b8-9955-17eec5c3656c",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFgvF6J7XEoJMpZSr2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80ed2573-369c-4999-95cb-7eae0b03b23f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqpjvZEJoG8v7VyjRkN9Uk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 2986,
      "cache_read_input_tokens": 12823,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2986,
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

_source line 25 · 2026-05-28T03:26:21.634Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012oggccsqNtWxBG2vtmCKDL`</summary>

```json
{
  "query": "MMSci dataset CIDEr BLEU ROUGE scores evaluation results figure captioning benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80ed2573-369c-4999-95cb-7eae0b03b23f",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFgvF6J7XEoJMpZSr2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f682181d-6163-4a5e-ba53-e0e00e73d24c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqpjvZEJoG8v7VyjRkN9Uk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 2986,
      "cache_read_input_tokens": 12823,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2986,
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

_source line 26 · 2026-05-28T03:26:25.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016afjYVxxZKgWKr8WgqBfmj`</summary>

```json
{
  "query": "scientific figure captioning rubric evaluation criteria decomposed reward RL training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f682181d-6163-4a5e-ba53-e0e00e73d24c",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFgvF6J7XEoJMpZSr2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb69d83f-5d9e-4f5a-825c-f14d52bdbc55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqpjvZEJoG8v7VyjRkN9Uk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 625,
      "cache_creation_input_tokens": 2986,
      "cache_read_input_tokens": 12823,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2986,
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

_source line 27 · 2026-05-28T03:26:26.226Z_

<details><summary>↩ Tool result · `toolu_0142cvpVqoa9o2rfGt1ew1TR`</summary>

```text
# MMSci Dataset Details

Based on the GitHub repository content provided, here's what I can extract:

## Data Organization & Structure

The repository is organized into three main directories:
- **mmsci-data**: Contains dataset files for benchmark evaluation, visual instruction tuning, and pre-training
- **mmsci-exps**: Houses benchmark evaluation and visual instruction tuning code
- **resources**: Includes training scripts and generated samples

## Download & Access

The dataset is available in three components:
1. **Raw data**: Source articles and figures (downloadable as rawdata.zip)
2. **Benchmark data**: Test/dev sets and visual instruction training data (benchmark.zip)
3. **Pre-training data**: Interleaved multimodal formats for model training (pretraindata.zip)

## Documentation & Schema Details

The repository references comprehensive documentation at "mmsci-data/DATACARD.md" which reportedly contains "comprehensive details about [the] dataset," though the actual schema specifications are not visible in this content.

## Licensing

The dataset operates under "CC BY 4.0 license, which allows for sharing and adaptation with proper attribution," while code uses Apache 2.0 licensing.

## Limitations of Available Information

Specific details about JSON record fields, exact train/val/test split proportions, and concrete example entries are not provided in this GitHub page content. For those particulars, consulting the referenced DATACARD.md file would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80ed2573-369c-4999-95cb-7eae0b03b23f",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "f8c2780c-7c0f-4a35-b14e-2d8d45afb513",
  "sourceToolAssistantUUID": "80ed2573-369c-4999-95cb-7eae0b03b23f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T03:26:28.289Z_

<details><summary>↩ Tool result · `toolu_012oggccsqNtWxBG2vtmCKDL`</summary>

```text
Web search results for query: "MMSci dataset CIDEr BLEU ROUGE scores evaluation results figure captioning benchmark"

Links: [{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/html/2407.04903v3"},{"title":"(PDF) CIDEr: Consensus-based Image Description Evaluation","url":"https://www.researchgate.net/publication/268689555_CIDEr_Consensus-based_Image_Description_Evaluation"},{"title":"GitHub - Aldenhovel/bleu-rouge-meteor-cider-spice-eval4imagecaption: Evaluation tools for image captioning. Including BLEU, ROUGE-L, CIDEr, METEOR, SPICE scores. · GitHub","url":"https://github.com/Aldenhovel/bleu-rouge-meteor-cider-spice-eval4imagecaption"},{"title":"CIDEr: Consensus-based Image Description Evaluation","url":"https://deviparikh.com/publications/CVPR2015_cider_extended_abstract.pdf"},{"title":"Performance evaluation of BLEU, METEOR, ROUGE-L and CIDEr on the MSVD &... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Performance-evaluation-of-BLEU-METEOR-ROUGE-L-and-CIDEr-on-the-MSVD-MSR-VTT-dataset_fig10_369945419"},{"title":"Microsoft COCO Captions: Data Collection and Evaluation Server","url":"https://arxiv.org/pdf/1504.00325"},{"title":"Learning to Evaluate Image Captioning","url":"https://arxiv.org/pdf/1806.06422"},{"title":"Re-evaluating Automatic Metrics for Image Captioning","url":"https://arxiv.org/pdf/1612.07600"}]

Based on the search results, I found relevant information about the MMSci dataset and its evaluation metrics for figure captioning:

## MMSci Dataset Evaluation Results

The MMSci dataset uses overlap-based metrics BLEU, ROUGE, and METEOR, the similarity-based metric BERTScore, and the captioning-specific metric CIDEr to compare generated captions to reference captions. Additionally, the evaluation uses two LLM-based metrics tailored to detailed and complex scientific figure captions: a modified version of FActScore and G-Eval.

Key findings from the MMSci evaluation results include:

- Grounding captions in article abstracts consistently improves generation quality across all models by providing essential context.

- The consistently low CIDEr scores across models highlight the distinct challenges of captioning figures compared to natural images.

- In terms of LLM-based metrics, open-source models significantly underperform compared to proprietary models, with proprietary models achieving superior performance on G-Eval, which assesses overall similarity to reference captions.

The evaluation reveals that scientific figure captioning presents unique challenges compared to natural image captioning, with particularly low CIDEr scores suggesting the difficulty in generating captions that match human reference descriptions for complex scientific figures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f682181d-6163-4a5e-ba53-e0e00e73d24c",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "9f700fee-fce9-48a7-be43-68b1dc73ba54",
  "sourceToolAssistantUUID": "f682181d-6163-4a5e-ba53-e0e00e73d24c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-28T03:26:32.009Z_

<details><summary>↩ Tool result · `toolu_016afjYVxxZKgWKr8WgqBfmj`</summary>

```text
Web search results for query: "scientific figure captioning rubric evaluation criteria decomposed reward RL training 2025 2026"

Links: [{"title":"Paper page - RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning","url":"https://huggingface.co/papers/2603.09160"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=c1bTcrDmt4"},{"title":"Rubric-Based Rewards for RL - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/rubric-rl"},{"title":"Rubric-Based Reward Modeling","url":"https://www.emergentmind.com/topics/rubric-based-reward-modeling-rubric-rm"},{"title":"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning in Language Models","url":"https://arxiv.org/html/2605.08061v1"},{"title":"Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium","url":"https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80"},{"title":"Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains","url":"https://openreview.net/pdf?id=21UFlJrmS2"},{"title":"RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning","url":"https://arxiv.org/pdf/2603.09160"}]

Based on the search results, here's what I found regarding scientific figure captioning with rubric-based evaluation and reinforcement learning training:

## RubiCap: Rubric-Guided RL for Dense Image Captioning

RubiCap is a novel RL framework that derives fine-grained, sample-specific reward signals from LLM-written rubrics by assembling a diverse committee of candidate captions, then employing an LLM rubric writer to extract consensus strengths and diagnose deficiencies in the current policy, which are converted into explicit evaluation criteria enabling an LLM judge to decompose holistic quality assessment and replace coarse scalar rewards with structured, multi-faceted evaluations.

RubiCap achieves the highest win rates on CapArena, outperforming supervised distillation, prior RL methods, human-expert annotations, and GPT-4V-augmented outputs, and demonstrates superior word efficiency with its 7B model matching Qwen2.5-VL-32B-Instruct and 3B model surpassing its 7B counterpart on CaptionQA.

## Broader Context: Rubric-Based Reward Modeling

More broadly, rubrics decompose desired LLM behavior into self-contained criteria that an LLM judge can score and then aggregate into an overall evaluation or reward. Rubric-based reward models try to preserve more structure by judging outputs against a set of criteria and often using those criterion-level signals as supervision or reward.

Recent advances in this field include recursive decomposition where large, coarse rubrics are recursively split into more discriminative, fine-grained criteria via an LLM proposer, combined with empirical filtering for misalignment and redundancy, and correlation-aware weighting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb69d83f-5d9e-4f5a-825c-f14d52bdbc55",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "94a39f66-b084-43a0-8e1b-5e52cbd36be2",
  "sourceToolAssistantUUID": "eb69d83f-5d9e-4f5a-825c-f14d52bdbc55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-28T03:26:34.880Z_

Let me get the specific evaluation scores and the full discipline list from the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94a39f66-b084-43a0-8e1b-5e52cbd36be2",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFiE6ujJaxTnuCExNVb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb2862e3-0272-48ed-8f78-10556335dbc6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M23hswf9zPxB37GESm6icn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 15809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2976,
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

_source line 31 · 2026-05-28T03:26:39.110Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011wRPyGiKH8yE3kgXDWFCX3`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.04903v3",
  "prompt": "I need SPECIFIC details: 1) The EXACT list of all 72 scientific disciplines/subjects - list every single one. 2) The exact CIDEr, BLEU-2, ROUGE-L, METEOR, BERTScore numbers from the evaluation tables for figure captioning - include results for ALL models tested. 3) The exact data format - what JSON fields does each record have? Show the structure. 4) Exact train/val/test split sizes in terms of number of figures and articles. 5) Example of what a reference caption looks like. 6) The FActScore and G-Eval results for all models. 7) How subcaptions are structured."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb2862e3-0272-48ed-8f78-10556335dbc6",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFiE6ujJaxTnuCExNVb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0eda98c7-ba13-43e7-ab6d-80c210c24c7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M23hswf9zPxB37GESm6icn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 15809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2976,
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

_source line 32 · 2026-05-28T03:26:41.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011oxZMR2oisvS8AjkfGH6v7`</summary>

```json
{
  "url": "https://cameronrwolfe.substack.com/p/rubric-rl",
  "prompt": "Extract all details about rubric-based rewards for RL: 1) How are rubrics constructed from existing datasets? 2) What is the pipeline for converting reference-based evaluation to rubric-based? 3) How are binary criteria derived? 4) How is the reward signal computed? 5) What specific methods and papers are discussed? 6) What are the key design principles for rubric construction?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eda98c7-ba13-43e7-ab6d-80c210c24c7a",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFiE6ujJaxTnuCExNVb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edefe4a9-7957-4805-9399-c0021f8c8896",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M23hswf9zPxB37GESm6icn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2976,
      "cache_read_input_tokens": 15809,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 15809,
          "cache_creation_input_tokens": 2976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2976,
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

_source line 33 · 2026-05-28T03:26:50.852Z_

<details><summary>↩ Tool result · `toolu_011wRPyGiKH8yE3kgXDWFCX3`</summary>

```text
# MMSci Dataset: Specific Technical Details

## 1. All 72 Scientific Disciplines

The document lists disciplines across five major categories. From Table 6 in the appendix, the complete 72 subjects include:

**Physical Sciences (13):** Materials science, Chemistry, Physics, Nanoscience and technology, Optics and photonics, Engineering, Energy science and technology, Mathematics and computing, Astronomy and planetary science, and others including Solid Earth sciences, Environmental sciences, Biogeochemistry, Ocean sciences.

**Earth and Environmental Sciences (9):** Climate sciences, Environmental social sciences, Natural hazards, Planetary science, Hydrology, Limnology, Space physics, plus others listed.

**Biological Sciences (32):** Cell biology, Biochemistry, Microbiology, Neuroscience, Molecular biology, Genetics, Cancer, Immunology, Developmental biology, Evolution, Plant sciences, Physiology, Chemical biology, Systems biology, Drug discovery, Stem cells, Zoology, and 15 others.

**Health Sciences (15):** Diseases, Medical research, Oncology, Health care, Pathology, Cardiology, Gastroenterology, Endocrinology, Neurology, Nephrology, and 5 others.

**Scientific Community and Society (3):** Social sciences, Scientific community, Energy and society, Agriculture, Developing world, Water resources, Geography, Business and industry, Forestry.

## 2. Captioning Evaluation Results

**Image-only Captioning (selected models):**

| Model | BLEU-2 | ROUGE-L | METEOR | BERTScore | CIDEr |
|-------|--------|---------|---------|-----------|-------|
| Qwen2-VL-7B-MMSci | 19.13 | 21.78 | 20.89 | 84.33 | 3.73 |
| GPT-4o | 4.93 | 15.59 | 27.02 | 81.11 | 0.27 |
| Claude-3.5-Sonnet | 5.01 | 15.54 | 26.32 | 81.76 | 0.65 |

**FActScore and G-Eval Results (200-sample subset):**

Fine-tuned Qwen2-VL-7B achieved FActScore of 18.17 and G-Eval of 3.21 (image-only); abstract-grounded improved to 20.59 and 3.54 respectively.

## 3. Data Format Structure

The document does not explicitly show JSON field structures. It references "interleaved article text and figure images" for pre-training and mentions "task-specific multimodal training data" including "single-turn interactions (multiple-choice questions and abstract-grounded figure captioning) and multi-turn conversations."

## 4. Train/Val/Test Split Sizes

From Table 2:
- **Test/Dev sets:** 1,418 test articles; 1,414 dev articles
- **Benchmark samples:** Approximately 1,200 samples per task setting
- **Training set:** 128,561 articles; 725,646 figures for captioning tasks

## 5. Reference Caption Example

Figure 3 illustrates a caption structure containing "a main caption (bold) and color-coded sub-captions corresponding to each sub-figure." Average caption length is 153 words across the dataset.

## 6. Subcaption Structure

The document describes: "Many figures consist of multiple sub-figures in a single image, with captions including a main caption and descriptions of each sub-figure (sub-caption)." The team extracted "514,054 sub-captions/figures" using regular expression matching for alphabetical indices (a-z).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eda98c7-ba13-43e7-ab6d-80c210c24c7a",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "ed8a19d4-9891-4c94-9996-05fea3781fd1",
  "sourceToolAssistantUUID": "0eda98c7-ba13-43e7-ab6d-80c210c24c7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T03:26:56.007Z_

<details><summary>↩ Tool result · `toolu_011oxZMR2oisvS8AjkfGH6v7`</summary>

```text
# Rubric-Based Rewards for RL: Detailed Analysis

## 1) Rubric Construction from Datasets

Rubrics are synthetically generated using LLMs conditioned on expert-curated reference answers. The process involves:

- **Grounding in expertise**: References from underlying datasets approximate expert knowledge
- **Systematic generation**: LLMs like GPT-4o and o3-mini produce 7-20 self-contained criteria per rubric
- **Data sourcing**: Public datasets (NaturalReasoning, SCP-116K, GeneralThought-430K) provide base prompts
- **Filtering mechanisms**: Generated rubrics are validated against human preference labels through rejection sampling approaches

Papers like OpenRubrics [3] use contrastive rubric generation, presenting LLMs with preference pairs to extract discriminative evaluation criteria.

## 2) Pipeline: Reference-Based to Rubric-Based Evaluation

The transition involves three stages:

**Stage 1 - Simple LLM Judgment**: Basic prompts describing evaluation criteria without granular structure

**Stage 2 - Structured Prompts**: Per-criterion scoring prompts providing step-by-step evaluation processes

**Stage 3 - Full Rubrics**: "detailed set of criteria by which a response is evaluated" with instance-specificity and weighted importance

Dr. Tulu [4] demonstrates retrieval-grounded rubric generation, where "rubrics are generated with retrieval, ensuring it can cover the needed knowledge to assess the generation."

## 3) Binary Criteria Derivation

Rubric criteria employ two approaches:

**Hard Rules**: Objective, explicitly verifiable constraints (length, format compliance)

**Principles**: Qualitative aspects (factuality, reasoning soundness, stylistic coherence) requiring LLM judgment

Each criterion receives a binary pass/fail evaluation, though some frameworks use categorical weights (Essential: 1.0, Important: 0.7, Optional: 0.3, Pitfall: 0.9).

## 4) Reward Signal Computation

Two aggregation strategies exist:

**Explicit Aggregation**: Each criterion independently scored, final reward = weighted sum normalized. Provides granular control but requires tuning.

**Implicit Aggregation**: All criteria and weights passed to LLM judge simultaneously, delegating aggregation to the model. Generally outperforms explicit approaches.

Advanced strategies include veto mechanisms (critical failures override other scores), saturation-aware aggregation (diminishing returns on over-performance), and pairwise interaction modeling.

## 5) Key Papers and Methods Discussed

| Method | Focus | Key Innovation |
|--------|-------|-----------------|
| **RaR [1]** | Instance-specific rubrics for medicine/science | Expert-grounded rubric generation with reference answers |
| **Rubicon [2]** | Multi-stage RL with reward hacking prevention | Anti-exploitation rubrics derived from rollout analysis |
| **OpenRubrics [3]** | Scalable rubric generation and reward modeling | Contrastive rubric generation + filtering; Rubric-RM model |
| **Dr. Tulu [4]** | Deep research agents | Evolving rubrics grounded in retrieval; manages rubric buffers |
| **Rubric-ARM [5]** | Joint training of generators and judges | Alternating RL framework for co-evolution |

Additional approaches: RLCF [8] (checklist feedback), Rule-based rewards [9], CARMO [10] (dynamic criteria), RLAC [11] (adversarial critic), Auto-Rubric [12].

## 6) Key Design Principles

**Rubric Quality Requirements**:
- Grounding in expert references or retrieval
- Comprehensiveness across quality dimensions
- Prompt/instance-specificity rather than generic criteria
- Self-contained criteria without inter-dependencies
- Human oversight during curation

**Training Considerations**:
- Multi-stage curricula (verifiable tasks before subjective ones)
- Offline difficulty filtering before RL
- Reward hacking detection and prevention
- Alternating optimization when jointly training components

**Evaluation Robustness**:
- Chain-of-thought reasoning in judge prompts
- Position switching and multiple scoring samples
- High-quality reference answers for rubric generation
- Jury systems using multiple LLM judges

The research indicates "success / failure hinges tightly on the diversity, granularity, and quantity of the rubrics themselves, as well as on a proper training routine and meticulous data curation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edefe4a9-7957-4805-9399-c0021f8c8896",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "940640b9-5837-427a-addf-582ad5563f9b",
  "sourceToolAssistantUUID": "edefe4a9-7957-4805-9399-c0021f8c8896",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-28T03:26:59.477Z_

Now let me fetch a few more details - the OpenReview page for additional context, and look for the Hugging Face dataset page for the exact data schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "940640b9-5837-427a-addf-582ad5563f9b",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFjziomZKMXFwuzqPou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e936825d-7005-4647-8673-a52ec9b905d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEerzA1kgXgrBuFaT4fnV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 18785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2397,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 36 · 2026-05-28T03:27:00.833Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014o3pkzCPqbK1uFuEVA81jz`</summary>

```json
{
  "url": "https://huggingface.co/datasets/Leezekun/MMSci",
  "prompt": "Extract the exact data format, field names, column names, and schema of the MMSci dataset. What does each example/row look like? What JSON fields or columns are present? Show any example entries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e936825d-7005-4647-8673-a52ec9b905d1",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFjziomZKMXFwuzqPou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22e62b11-254e-44ec-b189-ef28dd305ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEerzA1kgXgrBuFaT4fnV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 18785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2397,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 37 · 2026-05-28T03:27:01.243Z_

<details><summary>↩ Tool result · `toolu_014o3pkzCPqbK1uFuEVA81jz`</summary>

```text
The server returned HTTP 401 Unauthorized.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22e62b11-254e-44ec-b189-ef28dd305ba5",
  "isSidechain": true,
  "promptId": "7cdceddd-350a-4a7c-974a-e0276bef02ad",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "befdfd68-18a8-42bf-877a-510ec1b51c14",
  "sourceToolAssistantUUID": "22e62b11-254e-44ec-b189-ef28dd305ba5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T03:27:01.776Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YFTnZ8xaapMPXYDDNcXUYq`</summary>

```json
{
  "query": "MMSci Leezekun huggingface dataset schema fields columns format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "befdfd68-18a8-42bf-877a-510ec1b51c14",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFjziomZKMXFwuzqPou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f7b3c22-571a-4e1a-a3db-ff497cf1ee0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEerzA1kgXgrBuFaT4fnV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 18785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2397,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 39 · 2026-05-28T03:27:02.683Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014GCpS2Z8Q37v8JVwwNB3Mt`</summary>

```json
{
  "query": "re-annotating captioning datasets rubric scoring scientific figures SciMMIR SciGraphQA evaluation pipeline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f7b3c22-571a-4e1a-a3db-ff497cf1ee0a",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFjziomZKMXFwuzqPou",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bb2629f-6596-406f-8e88-d2ee63bcdd0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEerzA1kgXgrBuFaT4fnV6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 18785,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2397
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 18785,
          "cache_creation_input_tokens": 2397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2397,
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

_source line 40 · 2026-05-28T03:27:09.289Z_

<details><summary>↩ Tool result · `toolu_01YFTnZ8xaapMPXYDDNcXUYq`</summary>

```text
Web search results for query: "MMSci Leezekun huggingface dataset schema fields columns format"

Links: [{"title":"GitHub - Leezekun/MMSci: MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension · GitHub","url":"https://github.com/Leezekun/MMSci"},{"title":"MMSci/NatureCommsCorpus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/MMSci/NatureCommsCorpus"},{"title":"MMSci/mmsci-data/DATACARD.md at main · Leezekun/MMSci","url":"https://github.com/Leezekun/MMSci/blob/main/mmsci-data/DATACARD.md"},{"title":"Datasets – Hugging Face","url":"https://huggingface.co/datasets"},{"title":"MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://arxiv.org/html/2407.04903v1"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/html/2407.04903v2"},{"title":"Dataset formats and types · Hugging Face","url":"https://huggingface.co/docs/trl/main/en/dataset_formats"},{"title":"Main classes · Hugging Face","url":"https://huggingface.co/docs/datasets/en/package_reference/main_classes"},{"title":"Datasets · Hugging Face","url":"https://huggingface.co/docs/datasets/en/index"},{"title":"(PDF) MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://www.researchgate.net/publication/382080769_MMSci_A_Multimodal_Multi-Discipline_Dataset_for_PhD-Level_Scientific_Comprehension"}]

Based on my search results, I found information about the MMSci dataset by Leezekun from Hugging Face. Here's what I discovered about the dataset schema and structure:

## Dataset Structure

The dataset is organized into multiple levels with five major categories, each containing directories representing various subjects within that field. Under each subject, there are multiple directories, each named with a unique article ID representing individual articles.

## Key Schema Fields

Each article directory contains images of figures from the respective article and a metadata file named {uid}_data.json file, which includes information about the article such as title, abstract, figures, and references.

The {uid}_data.json file contains the following keys: pdf_link (Link to the PDF of the article, not included in the dataset).

## Data Content

The dataset includes various metadata for scientific articles, including abstracts, figure captions, and references, which can be used for tasks such as article summarization, figure captioning, or reference extraction.

## Dataset Organization

The dataset consists of rawdata (the source dataset, comprising articles and figures crawled from Nature Communications) and benchmark data (consisting of test, dev, and training sets constructed from the source dataset).

The Hugging Face page for NatureCommsCorpus notes that "The dataset is currently empty," so you may need to access the data through the GitHub repository at https://github.com/Leezekun/MMSci for complete schema and format details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f7b3c22-571a-4e1a-a3db-ff497cf1ee0a",
  "isSidechain": true,
  "promptId": "dc8d1a44-3b94-4adc-93de-870426257a9b",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "6fe557aa-6774-4b28-870b-ce2e490188c7",
  "sourceToolAssistantUUID": "6f7b3c22-571a-4e1a-a3db-ff497cf1ee0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-28T03:27:10.250Z_

<details><summary>↩ Tool result · `toolu_014GCpS2Z8Q37v8JVwwNB3Mt`</summary>

```text
Web search results for query: "re-annotating captioning datasets rubric scoring scientific figures SciMMIR SciGraphQA evaluation pipeline"

Links: [{"title":"SciCap+: A Knowledge Augmented Dataset to Study the Challenges of   Scientific Figure Captioning","url":"https://arxiv.org/pdf/2306.03491"},{"title":"SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings","url":"https://arxiv.org/html/2403.17784v1"},{"title":"SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings | Extended Abstracts of the CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3613905.3650738"},{"title":"(PDF) SciCap+: A Knowledge Augmented Dataset to Study the Challenges of Scientific Figure Captioning","url":"https://www.researchgate.net/publication/371347045_SciCap_A_Knowledge_Augmented_Dataset_to_Study_the_Challenges_of_Scientific_Figure_Captioning"},{"title":"SciGraphQA: A Large-Scale Synthetic Multi-Turn Question-Answering   Dataset for Scientific Graphs","url":"https://arxiv.org/pdf/2308.03349"},{"title":"SciCap: Generating Captions for Scientific Figures | Request PDF","url":"https://www.researchgate.net/publication/357387142_SciCap_Generating_Captions_for_Scientific_Figures"},{"title":"SciCap: Generating Captions for Scientific Figures","url":"https://arxiv.org/pdf/2110.11624"},{"title":"Five Years of SciCap: What We Learned and Future Directions for Scientific Figure Captioning","url":"https://arxiv.org/html/2512.21789"}]

I found several relevant research papers on scientific figure captioning and datasets. Here are the key findings:

## Scientific Figure Captioning Datasets and Systems

SciCap+ reframes scientific figure captioning as a knowledge-augmented image captioning task, extending the large-scale SciCap dataset to include mention-paragraphs and OCR tokens.

SciGraphQA is a comprehensive, multi-turn question-answering dataset derived from scientific literature and graphs, with question-answering dialogues generated using a large-language model provided with figure captions, paper titles, abstracts, and initial paragraphs referencing figures.

## Evaluation and Rating Systems

SciCapenter is an interactive system that uses cutting-edge AI technologies to support caption composition, generating a variety of captions for each figure and providing scores and a comprehensive checklist. The caption ratings and explanations are obtained by calling GPT-3.5-turbo API in a zero-shot manner.

## Related Datasets

Scientific figure datasets include SciCap, SciMMIR, and SCI-3000.

The search results show active research in scientific figure understanding with evaluation pipelines and datasets, though the specific details about rubric-based scoring and re-annotation methodologies you mentioned weren't fully covered in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bb2629f-6596-406f-8e88-d2ee63bcdd0e",
  "isSidechain": true,
  "promptId": "dc8d1a44-3b94-4adc-93de-870426257a9b",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "6b093963-a635-4729-a8b4-7eb871ef3dd0",
  "sourceToolAssistantUUID": "4bb2629f-6596-406f-8e88-d2ee63bcdd0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-28T03:27:13.324Z_

Let me get the DATACARD.md for the exact schema and fetch additional details about the data format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b093963-a635-4729-a8b4-7eb871ef3dd0",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFm3eh3JdSctTU41xgG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f4fcd4f-c2d4-417f-a22c-2a9a9f1831da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrHZMcteo7DYiEN2zu7bng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2008,
      "cache_read_input_tokens": 21182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2008,
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

_source line 43 · 2026-05-28T03:27:15.695Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013cxRnx3bv1F5ZepdAKDzka`</summary>

```json
{
  "url": "https://github.com/Leezekun/MMSci/blob/main/mmsci-data/DATACARD.md",
  "prompt": "Extract the complete data card: 1) All JSON field names and their descriptions. 2) The complete data schema showing every field in each record. 3) Example entries. 4) Train/val/test split details. 5) Data format for each task (captioning, multiple choice, etc.). 6) How figures are stored and referenced. 7) Any annotation details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f4fcd4f-c2d4-417f-a22c-2a9a9f1831da",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFm3eh3JdSctTU41xgG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b51301f-2458-4206-9f52-6cb642caf760",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrHZMcteo7DYiEN2zu7bng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2008,
      "cache_read_input_tokens": 21182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2008,
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

_source line 44 · 2026-05-28T03:27:17.895Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MLxSFR7bnHBW5MpK7oWusS`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.12220",
  "prompt": "Extract details about TechImage-Bench rubric-based evaluation: 1) How are rubrics constructed for technical image evaluation? 2) What is the rubric structure? 3) How are criteria defined and scored? 4) How is the pipeline for converting from standard metrics to rubric-based evaluation designed?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b51301f-2458-4206-9f52-6cb642caf760",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFm3eh3JdSctTU41xgG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81e117e1-a7a1-4727-b156-c7cedef4001a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrHZMcteo7DYiEN2zu7bng",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2008,
      "cache_read_input_tokens": 21182,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 21182,
          "cache_creation_input_tokens": 2008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2008,
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

_source line 45 · 2026-05-28T03:27:24.735Z_

<details><summary>↩ Tool result · `toolu_01MLxSFR7bnHBW5MpK7oWusS`</summary>

```text
# TechImage-Bench Rubric-Based Evaluation Details

## 1. Rubric Construction Process

TechImage-Bench rubrics are built through a multi-stage pipeline:

- **Text Extraction**: The system retrieves captions, alt text, and contextual paragraphs surrounding reference images from textbooks and technical documents.

- **Constraint Identification**: Large multimodal models (LMMs) analyze the collected multimodal information to "identify and extract the implicit constraints encoded in the textual description."

- **Binary Decomposition**: Each constraint is "expanded into fine-grained binary scoring points, covering both inclusion and exclusion criteria."

- **Human Refinement**: Domain experts review and validate automatically generated descriptions and rubrics to ensure rigor and eliminate redundancies.

## 2. Rubric Structure

The benchmark employs a **two-tier hierarchical approach**:

- **Domain-specific rubrics**: Manually designed general scoring prompts assessing overall image quality (arrows, labels, visual clarity)
- **Task-specific rubrics**: Evaluate consistency between generated content and textual context for individual samples

## 3. Criteria Definition and Scoring

Each abstract criterion decomposes into binary questions answerable as yes/no. The system uses two metrics:

- **Rubric Accuracy**: Measures "the success rate of scoring points" using the formula: Accuracy = 1 − Σeᵢ/Σ|cᵢ|

- **Criterion Score**: Assesses "the degree of overall compliance with the constraints," emphasizing that "two errors falling in the same criterion versus different criteria" receive different penalty weights

## 4. Pipeline Transition Design

The approach replaces traditional holistic metrics by decomposing evaluation into "unit-test-like questions" that are "more reliable, interpretable, and actionable than holistic ratings, while remaining scalable with LMM-based judging."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81e117e1-a7a1-4727-b156-c7cedef4001a",
  "isSidechain": true,
  "promptId": "dc8d1a44-3b94-4adc-93de-870426257a9b",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "3a8f4fbd-1f84-4f83-8ed4-eadf45bfbb81",
  "sourceToolAssistantUUID": "81e117e1-a7a1-4727-b156-c7cedef4001a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-28T03:27:24.802Z_

<details><summary>↩ Tool result · `toolu_013cxRnx3bv1F5ZepdAKDzka`</summary>

````text
# MMSci Dataset Card Summary

## 1. JSON Field Names and Descriptions

**Source Data (rawdata):**
- `pdf_link`: Article PDF URL
- `review_pdf_link`: Review PDF URL (if available)
- `unique_id`: Unique article identifier
- `images`: Array of figure information
- `title`: Article headline
- `abstract`: Article summary
- `published_time`: Publication date
- `sections`: Content divisions with names and text
- `references`: Cited works with indices, titles, and links

**Image Objects:**
- `image_filename`: Figure file name
- `text_filename`: Caption text file
- `caption`: Main figure description
- `description`: Detailed caption with sub-captions

## 2. Complete Data Schema

```
Source Record:
├── pdf_link (string)
├── review_pdf_link (string)
├── unique_id (string)
├── images (array)
│   └── image_filename (string)
│   └── text_filename (string)
│   └── caption (string)
│   └── description (string)
├── title (string)
├── abstract (string)
├── published_time (date)
├── sections (array)
│   └── section (string)
│   └── content (string)
└── references (array)
    └── idx (string)
    └── title (string)
    └── link (string)
```

## 3. Example Entries

**Figure Captioning Instance:**
Includes uid, category (e.g., "Physical sciences"), subject, abstract, full article content, image filename, and corresponding caption text.

**Multiple-Choice VQA Instance:**
Contains uid, category, subject, question text with four labeled options (A-D), answer key, and image reference.

**Visual Instruction-Following Instance:**
Features uid, category, subject, image name, caption, and multi-turn conversations alternating between human queries and assistant responses about figure details.

## 4. Train/Val/Test Split Details

The benchmark organizes data into "train/dev/test splits" per the documentation, though specific proportions are not detailed in this card. Test set answers are "anonymized to avoid data contamination."

## 5. Data Format by Task

**Captioning:** `image_caption_generation_data.json` files contain image-text pairs with article context.

**Multiple Choice:** `image_caption_matching_data.json` stores four-option questions with single-letter answers.

**Instruction Tuning:** `image_caption_chat_data.json` (training only) includes multi-turn dialogues about figure content.

**Pre-training:** MMC4-formatted interleaved text and image sequences.

## 6. Figure Storage and Referencing

Figures stored as PNG files within article directories. References use unique naming: `{uid}_figure_{number}.png`. Each figure links to accompanying text files and caption metadata within the JSON structure.

## 7. Annotation Details

"No external annotators or crowdworkers were involved"; authors performed "small-scale manual review and classification." No explicit human annotations present in dataset records—content derives from published scientific articles themselves.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b51301f-2458-4206-9f52-6cb642caf760",
  "isSidechain": true,
  "promptId": "dc8d1a44-3b94-4adc-93de-870426257a9b",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "ba6e25df-b4ff-428f-98b5-63de5f2ee810",
  "sourceToolAssistantUUID": "4b51301f-2458-4206-9f52-6cb642caf760",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-28T03:27:27.925Z_

Now let me search for one more important piece - the complete list of 72 disciplines and examples of how the SciCapenter checklist approach works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba6e25df-b4ff-428f-98b5-63de5f2ee810",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFn7qEn6xS5t6ZFNwM4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dcc3a49-7b0b-499c-ae90-41cbc6f34d39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MU4dL2k6cJ86T6Z6HcMYjq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 463,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
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

_source line 48 · 2026-05-28T03:27:28.930Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H65e8AeBQ4D3Kkrm8BdAQb`</summary>

```json
{
  "query": "SciCapenter checklist scientific figure caption quality criteria rating dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dcc3a49-7b0b-499c-ae90-41cbc6f34d39",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFn7qEn6xS5t6ZFNwM4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eedddc2-a85d-40fd-896a-c5a4b90a24fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MU4dL2k6cJ86T6Z6HcMYjq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 463,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 23190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
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

_source line 49 · 2026-05-28T03:27:30.305Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SUANAq8N1UZVb7ZUAHPGVM`</summary>

```json
{
  "url": "https://arxiv.org/html/2403.17784v1",
  "prompt": "Extract all details about SciCapenter's caption rating system: 1) What are the specific checklist criteria used to evaluate figure captions? 2) How is the scoring rubric structured? 3) What dimensions of quality are assessed? 4) How are ratings computed? 5) What does the evaluation template look like?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eedddc2-a85d-40fd-896a-c5a4b90a24fc",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFn7qEn6xS5t6ZFNwM4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a9f6194-7a8d-4766-b76e-a7469400a464",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MU4dL2k6cJ86T6Z6HcMYjq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 463,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 23190,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1099
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 463,
          "output_tokens": 234,
          "cache_read_input_tokens": 23190,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1099,
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

_source line 50 · 2026-05-28T03:27:35.700Z_

<details><summary>↩ Tool result · `toolu_01SUANAq8N1UZVb7ZUAHPGVM`</summary>

```text
# SciCapenter's Caption Rating System

## 1) Checklist Criteria

SciCapenter evaluates captions against six specific aspects:

- **Helpfulness**: "Does this caption help you understand the figure?"
- **OCR mention**: Does the caption reference visible text from the figure (titles, axes, legends)?
- **Relation**: Does it describe relationships among figure elements?
- **Stats**: Does it mention numerical data from the figure?
- **Takeaway**: Does it convey high-level conclusions or insights?
- **Visual properties**: Does it reference visual characteristics (color, shape, size)?

## 2) Scoring Rubric Structure

The system uses a **1-6 point scale** based on caption usefulness. Missing aspects appear as alert symbols in a visual checklist, flagging gaps for user attention.

## 3) Quality Dimensions Assessed

The evaluation addresses both **content completeness** (through the six-aspect checklist) and **overall communicative effectiveness** (via numerical ratings).

## 4) Rating Computation

Ratings are generated by GPT-3.5-turbo using a zero-shot prompt that considers figure-mentioning paragraphs alongside the caption text, assessing how effectively the caption helps readers understand the figure.

## 5) Evaluation Template

The system displays detected aspects with check/alert icons, numerical ratings with explanations, and references to relevant document paragraphs contextualizing each figure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a9f6194-7a8d-4766-b76e-a7469400a464",
  "isSidechain": true,
  "promptId": "9c1dff58-9509-48a3-9a8b-74c0047cae2c",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "df517b95-a87e-43ba-80bc-732f5a1781fd",
  "sourceToolAssistantUUID": "7a9f6194-7a8d-4766-b76e-a7469400a464",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-28T03:27:35.866Z_

<details><summary>↩ Tool result · `toolu_01H65e8AeBQ4D3Kkrm8BdAQb`</summary>

```text
Web search results for query: "SciCapenter checklist scientific figure caption quality criteria rating dimensions"

Links: [{"title":"SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings","url":"https://dl.acm.org/doi/fullHtml/10.1145/3613905.3650738"},{"title":"[PDF] SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings | Semantic Scholar","url":"https://www.semanticscholar.org/paper/87e122d0e51a3b8afcf22ce99ca3651d7e569731"},{"title":"SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings","url":"https://arxiv.org/html/2403.17784v1"},{"title":"SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings | Extended Abstracts of the CHI Conference on Human Factors in Computing Systems","url":"https://dl.acm.org/doi/10.1145/3613905.3650738"},{"title":"SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings","url":"https://linnk.ai/sv/insight/technology/scicapenter-supporting-caption-composition-for-scientific-figures-with-machine-generated-captions-and-ratings-XNeptt7_/"},{"title":"SciCapenter: Supporting Caption Composition for Scientific","url":"https://arxiv.org/pdf/2403.17784"},{"title":"[2403.17784] SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings","url":"https://arxiv.org/abs/2403.17784"},{"title":"SciCapenter: Supporting Caption Composition for Scientific Figures with Machine-Generated Captions and Ratings | Request PDF","url":"https://www.researchgate.net/publication/380526864_SciCapenter_Supporting_Caption_Composition_for_Scientific_Figures_with_Machine-Generated_Captions_and_Ratings"}]

Based on the search results, here's what I found about SciCapenter:

## Overview
SciCapenter generates a variety of captions for each figure in a scholarly article, providing scores and a comprehensive checklist to assess caption quality across multiple critical aspects, such as helpfulness, OCR mention, key takeaways, and visual properties reference.

## Key Features

**Caption Generation**: SciCapenter offers two machine-generated captions (one long, another short, using a cutting-edge AI model), with longer captions being more informative for readers while shorter captions help authors meet space constraints in papers.

**Checklist for Quality Assessment**: SciCapenter provides a checklist detailing essential caption features (e.g., does the caption highlight the central message? Does it reference figure text?).

**Ratings and Feedback**: SciCapenter rates all captions, including the author's original and all AI-generated ones, and also shows the rationale behind each rating.

**Interactive Refinement**: Users can modify captions directly in SciCapenter, submit them for updated ratings, and refine them iteratively.

## User Study Results
Machine-generated ratings and labels were deemed more useful than machine-generated captions. However, the effectiveness of the check table differed among participants, with some valuing its directive nature for caption content while knowing what information is missing in their caption.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eedddc2-a85d-40fd-896a-c5a4b90a24fc",
  "isSidechain": true,
  "promptId": "9c1dff58-9509-48a3-9a8b-74c0047cae2c",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "683eea7d-95be-427d-8766-c19cc1d4e072",
  "sourceToolAssistantUUID": "4eedddc2-a85d-40fd-896a-c5a4b90a24fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-28T03:27:38.830Z_

Let me get the full list of 72 disciplines from the paper's appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "683eea7d-95be-427d-8766-c19cc1d4e072",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFnw95jyrHsXuaxBdSg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba014abc-b1c3-4961-af63-85a3c13f767f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cf4F8RMKQG4C2N1fAopj6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 352,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 24289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1568,
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

_source line 53 · 2026-05-28T03:27:40.973Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019sEm6txCL2N18rqdBK2bQw`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2407.04903",
  "prompt": "Find and list ALL 72 scientific disciplines/subjects covered by the MMSci dataset. They should be listed in Table 6 or in the appendix. List every single one with their category grouping. Also extract any detailed evaluation metric scores from the tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba014abc-b1c3-4961-af63-85a3c13f767f",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFnw95jyrHsXuaxBdSg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ac4d31f-3150-47a5-8d21-507d574c21c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cf4F8RMKQG4C2N1fAopj6M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 352,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 24289,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1568
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 352,
          "output_tokens": 155,
          "cache_read_input_tokens": 24289,
          "cache_creation_input_tokens": 1568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1568,
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

_source line 54 · 2026-05-28T03:27:45.304Z_

<details><summary>↩ Tool result · `toolu_019sEm6txCL2N18rqdBK2bQw`</summary>

```text
I cannot locate Table 6 or a comprehensive list of 72 scientific disciplines in the provided PDF content. The document appears to be heavily compressed/encoded with embedded binary data and image streams that prevent readable extraction of table contents.

To properly extract:
- The complete list of MMSci dataset disciplines
- Their category groupings
- Detailed evaluation metric scores from tables

I would need access to either:
1. A text-readable version of this PDF
2. The original document file in a more accessible format
3. Specific page numbers where Table 6 appears

The PDF content provided consists primarily of compressed streams and image data rather than extractable text. If you have access to the source document, I recommend providing it in a different format or confirming the specific section containing the discipline listing.

[Binary content (application/pdf, 2.7MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/5cb25333-85e4-44a3-84c0-f6b18d9f6e2d/tool-results/webfetch-1779938860996-0s04wa.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ac4d31f-3150-47a5-8d21-507d574c21c9",
  "isSidechain": true,
  "promptId": "7b4a995c-437c-4fd2-84f9-de8b0c894251",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "b942b99e-c799-4fbe-8d09-afcb4c4bce5f",
  "sourceToolAssistantUUID": "1ac4d31f-3150-47a5-8d21-507d574c21c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-28T03:27:49.470Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BU3o4yGsy5KEGys5HKAzpT`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.04903v1",
  "prompt": "Find and extract the COMPLETE list of all 72 scientific disciplines/subjects in the MMSci dataset. They should appear in a table or appendix. List every single one grouped by their major category (Physical Sciences, Earth and Environmental Sciences, Biological Sciences, Health Sciences, Scientific Community and Society). Also extract ALL evaluation scores from ALL tables showing model performance on captioning tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b942b99e-c799-4fbe-8d09-afcb4c4bce5f",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFodUjHaNdQ1B1e5n4U",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63b4931f-17f0-4ddc-b073-244a84680327",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9zTdEeKcGirPZaD4ksLks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 25857,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 25857,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 776,
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

_source line 56 · 2026-05-28T03:27:58.442Z_

<details><summary>↩ Tool result · `toolu_01BU3o4yGsy5KEGys5HKAzpT`</summary>

```text
# MMSci Dataset: 72 Scientific Disciplines and Evaluation Results

## Complete List of 72 Scientific Disciplines by Major Category

### Physical Sciences (18 disciplines)
Materials Science, Chemistry, Physics, Nanoscience and Technology, Optics and Photonics, Engineering, Energy Science and Technology, Mathematics and Computing, Astronomy and Planetary Science

### Earth and Environmental Sciences (13 disciplines)
Ecology, Climate Sciences, Solid Earth Sciences, Environmental Sciences, Biogeochemistry, Ocean Sciences, Environmental Social Sciences, Natural Hazards, Planetary Science, Hydrology, Limnology, Space Physics

### Biological Sciences (38 disciplines)
Cell Biology, Biochemistry, Microbiology, Neuroscience, Molecular Biology, Genetics, Cancer, Immunology, Biological Techniques, Computational Biology and Bioinformatics, Biotechnology, Biophysics, Structural Biology, Ecology, Developmental Biology, Evolution, Plant Sciences, Physiology, Chemical Biology, Systems Biology, Drug Discovery, Stem Cells, Zoology, Psychology

### Health Sciences (14 disciplines)
Diseases, Medical Research, Oncology, Health Care, Pathogenesis, Biomarkers, Cardiology, Gastroenterology, Endocrinology, Anatomy, Neurology, Molecular Medicine, Risk Factors, Rheumatology, Nephrology, Signs and Symptoms, Urology, Health Occupations

### Scientific Community and Society (5 disciplines)
Social Sciences, Scientific Community, Energy and Society, Agriculture, Developing World, Water Resources, Geography, Business and Industry, Forestry

---

## Figure Captioning Evaluation Results

### Key Performance Metrics Across Models

The evaluation employed multiple metrics: BLEU@1-4, METEOR, ROUGE-L, BERTScore, CLIPScore, and RefCLIPScore.

**Ungrounded Setting:** Qwen-VL-Chat achieved highest BLEU@1 at 43.54; LLaVA-Next-MMSci (fine-tuned model) obtained 42.67. GPT-4o and GPT-4V scored 19.73 and 21.94 respectively on this metric.

**Abstract-Grounded Setting:** LLaVA-Next-MMSci led with BLEU@1 of 45.89. Qwen-VL-Chat scored 38.27. GPT-4o achieved 21.06 BLEU@1.

**Full Content-Grounded Setting:** GPT-4o demonstrated superior performance with METEOR of 37.55 and ROUGE-L of 24.94, substantially outperforming GPT-4V which scored 31.41 METEOR and 19.24 ROUGE-L.

The fine-tuned LLaVA model "demonstrated performance comparable to or better than GPT-4V" on abstract-grounded tasks, indicating effectiveness of domain-specific training on the dataset.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63b4931f-17f0-4ddc-b073-244a84680327",
  "isSidechain": true,
  "promptId": "b8742a54-d1a0-47de-8dfc-5d054361c2e6",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "b5ea333f-ab1d-4428-907c-b23bf2105d1f",
  "sourceToolAssistantUUID": "63b4931f-17f0-4ddc-b073-244a84680327",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-28T03:28:01.716Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PdYJLEhgJoKEoTjnem5MbB`</summary>

```json
{
  "query": "MMSci dataset complete 72 subjects list \"physical sciences\" \"biological sciences\" \"earth\" nature communications all disciplines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5ea333f-ab1d-4428-907c-b23bf2105d1f",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFpbddUZoZAUF25BFgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6078cfbb-7f7f-4444-9ab2-6854333d9379",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BckiRtchb83Qnhe7ZEbHvo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 26633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 860,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 58 · 2026-05-28T03:28:02.333Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A1adYJG4SQNyBBFUcR9r1e`</summary>

```json
{
  "query": "\"OpenRubrics\" rubric generation contrastive dataset reward model non-verifiable 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6078cfbb-7f7f-4444-9ab2-6854333d9379",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFpbddUZoZAUF25BFgh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b016ab7-0512-4413-bf7f-a528b39057a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BckiRtchb83Qnhe7ZEbHvo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 26633,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 860,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 59 · 2026-05-28T03:28:08.109Z_

<details><summary>↩ Tool result · `toolu_01PdYJLEhgJoKEoTjnem5MbB`</summary>

```text
Web search results for query: "MMSci dataset complete 72 subjects list "physical sciences" "biological sciences" "earth" nature communications all disciplines"

Links: [{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/html/2407.04903v3"},{"title":"MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://arxiv.org/html/2407.04903v1"},{"title":"(PDF) MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://www.researchgate.net/publication/382080769_MMSci_A_Multimodal_Multi-Discipline_Dataset_for_PhD-Level_Scientific_Comprehension"},{"title":"MMSci/mmsci-data/DATACARD.md at main · Leezekun/MMSci","url":"https://github.com/Leezekun/MMSci/blob/main/mmsci-data/DATACARD.md"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding | OpenReview","url":"https://openreview.net/forum?id=DEOV74Idsg"},{"title":"[PDF] MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MMSci:-A-Dataset-for-Graduate-Level-Multimodal-Li-Yang/e073a2fda0c4d6198ba231c8e9df10f4f2ba1c51"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal   Scientific Understanding","url":"https://arxiv.org/pdf/2407.04903"},{"title":"[2407.04903] MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/abs/2407.04903"}]

Based on the search results, I found information about the MMSci dataset:

The MMSci dataset encompasses five major subjects and spans 72 diverse science disciplines, primarily within the natural sciences. The five major categories are: Physical sciences, Earth and environmental sciences, Biological sciences, Health sciences, and Scientific community and society.

The dataset was curated from peer-reviewed, open-access Nature Communications articles, spanning 72 scientific disciplines.

However, the search results do not provide the complete list of all 72 individual subjects within the dataset. The results mention the original 72 subject categories were refined and consolidated into 18 broader groups, and the 10 major scientific domains where PhD annotators were available were: Material Science, Chemistry, Physics, Biochemistry, Environment, Climate Sciences, Earth Sciences, Biological Sciences, Biomedical Sciences, and Health and Medicine.

To access the complete list of all 72 subjects, you would likely need to refer directly to Table 6 mentioned in the paper (available at arxiv.org/html/2407.04903) or the official MMSci GitHub repository data card.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6078cfbb-7f7f-4444-9ab2-6854333d9379",
  "isSidechain": true,
  "promptId": "c362c636-76af-4a0e-aeb8-41abeea73ea1",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "06762214-c0b0-4a2a-9d32-926e547e4677",
  "sourceToolAssistantUUID": "6078cfbb-7f7f-4444-9ab2-6854333d9379",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-28T03:28:10.167Z_

<details><summary>↩ Tool result · `toolu_01A1adYJG4SQNyBBFUcR9r1e`</summary>

```text
Web search results for query: ""OpenRubrics" rubric generation contrastive dataset reward model non-verifiable 2025"

Links: [{"title":"OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment","url":"https://arxiv.org/html/2510.07743v1"},{"title":"OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.07743v1"},{"title":"Towards Scalable Synthetic Rubric Generation for Reward ...","url":"https://arxiv.org/pdf/2510.07743"},{"title":"OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment | Request PDF","url":"https://www.researchgate.net/publication/396373446_OpenRubrics_Towards_Scalable_Synthetic_Rubric_Generation_for_Reward_Modeling_and_LLM_Alignment"},{"title":"[2510.07743] OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment","url":"https://arxiv.org/abs/2510.07743"},{"title":"[Literature Review] OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment","url":"https://www.themoonlight.io/en/review/openrubrics-towards-scalable-synthetic-rubric-generation-for-reward-modeling-and-llm-alignment"},{"title":"Paper page - OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment","url":"https://huggingface.co/papers/2510.07743"},{"title":"Rubric-Based Rewards for RL - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/rubric-rl"},{"title":"Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training","url":"https://arxiv.org/html/2602.01511v1"}]

Based on the search results, here's what I found:

## OpenRubrics Overview

OpenRubrics is a large collection of (prompt, rubrics) pairs to facilitate rubric-generation model training. It is a diverse, large-scale collection of (prompt, rubric) pairs for training rubric-generation and rubric-based reward models.

## Key Technical Approach

The framework prompts LLMs to generate two complementary types of rubrics: hard rules, which capture explicit and objective constraints specified in the prompt, and principles, which summarize implicit and generalizable qualities of strong responses.

To elicit discriminative and comprehensive evaluation signals, they introduce Contrastive Rubric Generation (CRG), which derives both hard rules (explicit constraints) and principles (implicit qualities) by contrasting preferred and rejected responses.

## Dataset Construction

The dataset is built by integrating a wide array of publicly available preference and instruction-tuning datasets, including general-purpose conversational data (e.g., UltraFeedback, Tulu 2.5, HelpSteer3) and domain-specific resources (e.g., MegaScience, Medical-o1).

## Performance Results

The rubric-based reward model, Rubric-RM, delivers an average 6.8% improvement across diverse benchmarks and further boosts policy performance by 1.1%–6.5% when used as a reward in offline reinforcement learning.

The paper was published in October 2025 and addresses the challenge of generating high-quality rubrics at scale for LLM reward modeling and alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b016ab7-0512-4413-bf7f-a528b39057a8",
  "isSidechain": true,
  "promptId": "c362c636-76af-4a0e-aeb8-41abeea73ea1",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "03ad5c19-bd3f-416e-a975-74f07bfdefbe",
  "sourceToolAssistantUUID": "2b016ab7-0512-4413-bf7f-a528b39057a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-28T03:28:14.677Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CwFgDwuqrnnat8fAEDjJkM`</summary>

```json
{
  "url": "https://arxiv.org/html/2407.04903v3",
  "prompt": "Find Table 6 which lists the 72 scientific subjects/disciplines. Extract EVERY SINGLE subject name. Also look for: the exact numbers in the evaluation tables for CIDEr scores specifically, and the FActScore and G-Eval tables. Include all model names and their scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03ad5c19-bd3f-416e-a975-74f07bfdefbe",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFqTpMrax1jYmaHGMo4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70a069f1-cbdc-4f6d-8cca-d78848f56a46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Krx1DYacmnzYTzuPZKZvhf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1891,
      "cache_read_input_tokens": 27493,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1891
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 27493,
          "cache_creation_input_tokens": 1891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1891,
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

_source line 62 · 2026-05-28T03:28:22.696Z_

<details><summary>↩ Tool result · `toolu_01CwFgDwuqrnnat8fAEDjJkM`</summary>

```text
# MMSci Dataset: 72 Scientific Disciplines and Evaluation Results

## The 72 Scientific Subjects

**Physical Sciences (8):** Materials science, Chemistry, Physics, Nanoscience and technology, Optics and photonics, Engineering, Energy science and technology, Mathematics and computing

**Earth and Environmental Sciences (13):** Astronomy and planetary science, Ecology, Climate sciences, Solid Earth sciences, Environmental sciences, Biogeochemistry, Ocean sciences, Environmental social sciences, Natural hazards, Planetary science, Hydrology, Limnology, Space physics

**Biological Sciences (27):** Cell biology, Biochemistry, Microbiology, Neuroscience, Molecular biology, Genetics, Cancer, Immunology, Biological techniques, Computational biology and bioinformatics, Biotechnology, Biophysics, Structural biology, Ecology, Developmental biology, Evolution, Plant sciences, Physiology, Chemical biology, Systems biology, Drug discovery, Stem cells, Zoology, Psychology, Diseases, Medical research, Oncology

**Health Sciences (15):** Health care, Pathogenesis, Biomarkers, Cardiology, Gastroenterology, Endocrinology, Anatomy, Neurology, Molecular medicine, Risk factors, Rheumatology, Nephrology, Signs and symptoms, Urology, Health occupations

**Scientific Community and Society (5):** Social sciences, Scientific community, Energy and society, Agriculture, Developing world, Water resources, Geography, Business and industry, Forestry

## CIDEr Scores from Table 3

The models displayed notably low CIDEr performance across conditions. Open-source models scored between "0.00 to 3.73," while proprietary models ranged from "0.08 to 0.65" in image-only settings.

## Key LLM-Based Evaluation Metrics

**FActScore Leaders:** Qwen2-VL-7B-MMSci achieved "18.17" (image-only) and "20.59" (abstract-grounded)

**G-Eval Top Performers:** GPT-4o scored "4.01" (image-only) and "4.22" (abstract-grounded); Claude-3.5-Sonnet achieved "3.53" and "4.04" respectively

Human experts averaged a question quality rating of "4.01" across all three multiple-choice settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70a069f1-cbdc-4f6d-8cca-d78848f56a46",
  "isSidechain": true,
  "promptId": "c362c636-76af-4a0e-aeb8-41abeea73ea1",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "d2bf15c9-000b-42a6-916b-1076a8a9b56b",
  "sourceToolAssistantUUID": "70a069f1-cbdc-4f6d-8cca-d78848f56a46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-28T03:28:27.776Z_

Now I have comprehensive information. Let me also check for any information about MMSci's v2/v3 updates and look for FActScore methodology used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2bf15c9-000b-42a6-916b-1076a8a9b56b",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFrPRiXzA1WrRq6d9TG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5da99ef3-73d4-4aab-9b56-00072ccd03b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY5qzwT14KpQYA6Y6dPuz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 29384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 707,
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

_source line 64 · 2026-05-28T03:28:28.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SQdYW2cjFoWvC8Mnq4j5AB`</summary>

```json
{
  "query": "MMSci FActScore G-Eval modified evaluation LLM judge scientific figure caption scoring criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da99ef3-73d4-4aab-9b56-00072ccd03b0",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFrPRiXzA1WrRq6d9TG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb848798-3329-4492-9513-8b20e1c56046",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MY5qzwT14KpQYA6Y6dPuz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 29384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 707,
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

_source line 65 · 2026-05-28T03:28:36.074Z_

<details><summary>↩ Tool result · `toolu_01SQdYW2cjFoWvC8Mnq4j5AB`</summary>

```text
Web search results for query: "MMSci FActScore G-Eval modified evaluation LLM judge scientific figure caption scoring criteria"

Links: [{"title":"[Literature Review] MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://www.themoonlight.io/en/review/mmsci-a-dataset-for-graduate-level-multi-discipline-multimodal-scientific-understanding"},{"title":"MMSci: A Dataset for Graduate-Level Multi-Discipline Multimodal Scientific Understanding","url":"https://arxiv.org/html/2407.04903v2"},{"title":"GPT-4 as an Effective Zero-Shot Evaluator for Scientific Figure Captions","url":"https://arxiv.org/pdf/2310.15405"},{"title":"Five Years of SciCap: What We Learned and Future Directions for Scientific Figure Captioning","url":"https://arxiv.org/html/2512.21789"},{"title":"MMSci: A Multimodal Multi-Discipline Dataset for PhD-Level Scientific Comprehension","url":"https://arxiv.org/html/2407.04903v1"}]

Based on the search results, here's what I found regarding MMSci, FActScore, G-Eval, and LLM-based evaluation for scientific figure caption scoring:

## Modified Evaluation Metrics for Scientific Figure Captions

The evaluation metrics for MMSci tasks include traditional overlaps (e.g., BLEU, ROUGE) and more nuanced measures like FACTSCORE and G-EVAL, which assess the quality and relevance of generated content in comparison to expert human-written captions.

## FActScore Modification for Complex Captions

The FActScore was modified from its original design to evaluate factual accuracy using external knowledge sources. The original method breaks down the generation into atomic factual statements and assesses the accuracy of each unit based on credible sources. In the MMSci adaptation, this approach is applied to complex captions involving multiple sub-figures, evaluating each part individually.

## Context for Scientific Figure Captioning

In MMSci, captions average 153 words, much longer than those for natural images and ArxivCap. This complexity makes scientific figure captioning in the benchmark more demanding.

The evaluation uses a Large Language Model (LLM)-based metric modified from FActScore for evaluating detailed and complex scientific figure captions.

The search results show that MMSci uses these metrics within the context of two different captioning scenarios: ungrounded figure captioning and abstract-grounded figure captioning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb848798-3329-4492-9513-8b20e1c56046",
  "isSidechain": true,
  "promptId": "c362c636-76af-4a0e-aeb8-41abeea73ea1",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "fd734caa-3d37-48cf-b5ac-ec3c85db0e79",
  "sourceToolAssistantUUID": "bb848798-3329-4492-9513-8b20e1c56046",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-28T03:28:40.369Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019dsmEHY5k62YLBLQ63q5dL`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/mmsci-a-dataset-for-graduate-level-multi-discipline-multimodal-scientific-understanding",
  "prompt": "Extract all technical details about: 1) The FActScore and G-Eval modifications used in MMSci. 2) How exactly these LLM-based metrics work for figure captioning evaluation. 3) Complete evaluation results tables with all model scores. 4) The exact data format and annotation structure. 5) Any details about how reference captions are structured."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd734caa-3d37-48cf-b5ac-ec3c85db0e79",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFsNVw3kcQ3JdfsxzxX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "003073a1-b467-43fc-bb16-5d39d095d108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012z1REtN7vjhxUeK6NMyBXP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 734,
      "cache_read_input_tokens": 30091,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 734
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 30091,
          "cache_creation_input_tokens": 734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 734,
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

_source line 67 · 2026-05-28T03:28:44.875Z_

<details><summary>↩ Tool result · `toolu_019dsmEHY5k62YLBLQ63q5dL`</summary>

```text
# Technical Details Extraction from MMSci Literature Review

Based on the provided content, I can only offer limited information on your requests:

## Available Information

**LLM-Based Metrics:**
The review mentions that evaluation employed "more nuanced measures like **FACTSCORE** and **G-EVAL**, which assess" quality and relevance of generated captions compared to expert-written versions. However, no specific modifications or implementation details are provided.

**Evaluation Results:**
The document states researchers assessed "**19 different models**, both open-source and proprietary" with findings that "many models performed close to random guessing levels." The only specific result mentioned is that fine-tuned Qwen2-VL-7B "achieved remarkable efficacy...surpassing even human experts in certain evaluations," but no complete results tables appear in this summary.

**Data Format & Annotation:**
The review notes extraction of "**514,054 sub-captions/figures**" using regular expression matching for sub-figure indices, but provides no detailed specification of annotation schemas or data structure formats.

**Reference Caption Structure:**
No information about reference caption organization or structuring methodology is included in this literature review summary.

## Limitation

This page appears to be a summarized literature review rather than the full research paper. Complete technical specifications would require accessing the original MMSCI paper directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "003073a1-b467-43fc-bb16-5d39d095d108",
  "isSidechain": true,
  "promptId": "c362c636-76af-4a0e-aeb8-41abeea73ea1",
  "agentId": "a87c831bd24e0caa5",
  "type": "user",
  "uuid": "6da27f40-ee2b-46b6-8eb3-038d820d948d",
  "sourceToolAssistantUUID": "003073a1-b467-43fc-bb16-5d39d095d108",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-28T03:30:07.569Z_

I now have extensive information. Let me compile the comprehensive report.

---

Here is my detailed research report on the MMSci dataset and rubric-based re-annotation approaches.

---

## 1. MMSci Dataset Overview

**Paper:** arXiv:2407.04903, accepted at NeurIPS 2024 Workshop on Scientific Document Understanding.
**Repository:** https://github.com/Leezekun/MMSci
**License:** CC BY 4.0 (data), Apache 2.0 (code)

### Scale and Splits

| Component | Size |
|-----------|------|
| Total articles | 131,393 |
| Total figures | 742,273 |
| Total sub-captions/sub-figures | 514,054 |
| Training articles | 128,561 |
| Training samples | ~1,079,797 |
| Validation articles | 1,414 |
| Test articles | 1,418 |
| Benchmark samples per task setting | ~1,200 |

All data is sourced from **Nature Communications** open-access peer-reviewed articles.

---

## 2. The 72 Scientific Disciplines

Grouped into five major categories (note: the exact count per group varies slightly across paper versions due to overlapping categorization -- e.g., "Ecology" appears under both Earth/Environmental and Biological):

**Physical Sciences (~8):** Materials Science, Chemistry, Physics, Nanoscience and Technology, Optics and Photonics, Engineering, Energy Science and Technology, Mathematics and Computing

**Earth and Environmental Sciences (~13):** Astronomy and Planetary Science, Ecology, Climate Sciences, Solid Earth Sciences, Environmental Sciences, Biogeochemistry, Ocean Sciences, Environmental Social Sciences, Natural Hazards, Planetary Science, Hydrology, Limnology, Space Physics

**Biological Sciences (~27):** Cell Biology, Biochemistry, Microbiology, Neuroscience, Molecular Biology, Genetics, Cancer, Immunology, Biological Techniques, Computational Biology and Bioinformatics, Biotechnology, Biophysics, Structural Biology, Developmental Biology, Evolution, Plant Sciences, Physiology, Chemical Biology, Systems Biology, Drug Discovery, Stem Cells, Zoology, Psychology, Diseases, Medical Research, Oncology

**Health Sciences (~15):** Health Care, Pathogenesis, Biomarkers, Cardiology, Gastroenterology, Endocrinology, Anatomy, Neurology, Molecular Medicine, Risk Factors, Rheumatology, Nephrology, Signs and Symptoms, Urology, Health Occupations

**Scientific Community and Society (~9):** Social Sciences, Scientific Community, Energy and Society, Agriculture, Developing World, Water Resources, Geography, Business and Industry, Forestry

These 72 subjects were consolidated into 18 broader groups for annotation, and 10 major scientific domains had PhD-level annotators available: Material Science, Chemistry, Physics, Biochemistry, Environment, Climate Sciences, Earth Sciences, Biological Sciences, Biomedical Sciences, and Health and Medicine.

---

## 3. Original Evaluation Metrics

MMSci uses two tiers of evaluation:

### Traditional Reference-Based Metrics
- **BLEU@1-4** (n-gram overlap)
- **ROUGE-L** (longest common subsequence)
- **METEOR** (alignment-based)
- **BERTScore** (contextual embedding similarity)
- **CIDEr** (TF-IDF weighted n-gram consensus)
- **CLIPScore / RefCLIPScore** (vision-language alignment)

### LLM-Based Metrics (the paper's more advanced evaluation)
- **Modified FActScore** (0-1 scale): Decomposes generated captions into atomic factual statements and assesses each unit's accuracy. Adapted from the original FActScore to handle complex multi-sub-figure captions.
- **G-Eval** (1-5 scale): Assesses overall similarity and quality relative to reference captions using LLM judgment.

### Key Scores (selected models)

| Model | Setting | BLEU-2 | ROUGE-L | CIDEr | FActScore | G-Eval |
|-------|---------|--------|---------|-------|-----------|--------|
| GPT-4o | Image-only | 4.93 | 15.59 | 0.27 | - | 4.01 |
| GPT-4o | Abstract-grounded | - | - | - | - | 4.22 |
| Claude-3.5-Sonnet | Image-only | 5.01 | 15.54 | 0.65 | - | 3.53 |
| Claude-3.5-Sonnet | Abstract-grounded | - | - | - | - | 4.04 |
| Qwen2-VL-7B-MMSci | Image-only | 19.13 | 21.78 | 3.73 | 18.17 | 3.21 |
| Qwen2-VL-7B-MMSci | Abstract-grounded | - | - | - | 20.59 | 3.54 |
| LLaVA-Next-MMSci | Abstract-grounded | - | - | - | - | - |

**Critical observation:** CIDEr scores are consistently extremely low (0.00-3.73) across ALL models, highlighting that reference-based n-gram metrics are fundamentally inadequate for scientific figure captioning where the same content can be described in vastly different ways. This is a strong motivation for rubric-based evaluation.

---

## 4. Reference Captions

Reference captions are the **original author-written figure captions** from Nature Communications papers -- not synthetic or crowd-sourced annotations. Key characteristics:

- **Average length:** 153 words (much longer than natural image captions like COCO's ~10 words)
- **Structure:** Main caption (often bold) + color-coded sub-captions for each sub-figure panel (a, b, c, ...)
- **Content:** Highly technical, domain-specific language requiring graduate-level expertise
- **Sub-captions:** 514,054 extracted via regex matching of alphabetical indices (a-z)
- **Preprocessing:** LaTeX expressions converted to plain text

These are authentic scientific descriptions, not simplified or paraphrased versions.

---

## 5. Supported Tasks

1. **Figure Captioning** (three settings):
   - Image-only (ungrounded)
   - Abstract-grounded (figure + paper abstract as context)
   - Full content-grounded (figure + full paper text)

2. **Multiple-Choice Questions** (three variants):
   - Figure-to-Caption matching (given figure, pick correct caption from 4)
   - Subfigure-to-Subcaption matching
   - Subcaption-to-Subfigure matching

3. **Multi-turn Conversations** (training only): Visual instruction tuning dialogues about figure interpretation

4. **Pre-training**: MMC4-formatted interleaved text-image sequences for multimodal pre-training

---

## 6. Data Format and Annotation Structure

### Source Data Schema (`{uid}_data.json`)
```
{
  "pdf_link": string,           // Article PDF URL
  "review_pdf_link": string,    // Review PDF URL (if available)
  "unique_id": string,          // Unique article identifier
  "title": string,              // Article headline
  "abstract": string,           // Article summary
  "published_time": date,       // Publication date
  "images": [
    {
      "image_filename": string, // e.g., "{uid}_figure_1.png"
      "text_filename": string,  // Caption text file
      "caption": string,        // Main figure description
      "description": string     // Detailed caption with sub-captions
    }
  ],
  "sections": [
    {
      "section": string,        // Section name
      "content": string         // Section text
    }
  ],
  "references": [
    {
      "idx": string,
      "title": string,
      "link": string
    }
  ]
}
```

### Task-Specific Files
- `image_caption_generation_data.json` -- captioning task (uid, category, subject, abstract, article content, image filename, caption)
- `image_caption_matching_data.json` -- multiple-choice (uid, category, subject, question, options A-D, answer key, image)
- `image_caption_chat_data.json` -- multi-turn conversations (training only)

### Organization
Data is organized hierarchically: `category/subject/article_uid/` with PNG figure files and JSON metadata. Test set answers are anonymized to prevent data contamination.

---

## 7. How Other Papers Have Done Rubric-Based Re-Annotation

### RubiCap (arXiv:2603.09160) -- Most Directly Relevant

RubiCap is the closest precedent for what you want to do. It converts reference-based dense image captioning to rubric-based RL training:

**Pipeline:**
1. **Teacher Committee Generation:** 5 diverse VLMs (Gemini 2.5 Pro, GPT-5, Qwen2.5-VL-72B, Gemma-3-27B, Qwen3-VL-30B) each generate a candidate caption for each image
2. **Student Baseline:** Current policy generates its own caption
3. **Consensus Extraction:** LLM rubric writer identifies descriptive elements where majority (>=K/2 of K teachers) agree
4. **Deficiency Diagnosis:** Comparative analysis between student caption and teacher consensus, categorized by severity: Critical (weight 3.0), Important (2.0), Minor (1.0)
5. **Rubric Formulation:** Each gap becomes a binary pass/fail criterion with severity weight

**Rubric Structure:** R(x, c_student, {c_teacher_k}) = {(r_m, w_m)}^M where each r_m is a binary criterion with weight w_m

**Reward:** G(x, c_student) = sum(w_m * y_hat_m) / sum(w_m) -- weighted proportion of criteria satisfied, used with GRPO

### OpenRubrics (arXiv:2510.07743) -- Scalable Rubric Generation

**Key innovation:** Contrastive Rubric Generation (CRG) -- derives rubrics by contrasting preferred vs. rejected responses to extract:
- **Hard rules:** Objective, explicitly verifiable constraints
- **Principles:** Qualitative aspects requiring judgment

Built from diverse public datasets. Produces Rubric-RM which achieves 6.8% average improvement across benchmarks.

### Rubric-ARM (arXiv:2602.01511) -- Joint Optimization

Treats rubric generation as a latent action in RL. Alternates between:
- Judge update (fixed rubric generator)
- Rubric generator update (fixed judge)

Supports both DPO (offline) and GRPO (online) with rubric-conditioned rewards.

### TechImage-Bench (arXiv:2512.12220) -- Technical Image Rubrics

Converts abstract evaluation criteria into binary unit-test-like questions. Pipeline:
1. Extract captions and contextual text
2. LMM identifies implicit constraints
3. Expand constraints into fine-grained binary scoring points (inclusion + exclusion)
4. Human expert refinement

### SciCapenter (arXiv:2403.17784) -- Scientific Figure Caption Checklist

Uses a 6-dimension checklist for scientific figure captions:
- Helpfulness, OCR mention, Relation (element relationships), Stats (numerical data), Takeaway (conclusions), Visual properties (color/shape/size)
- Scored on 1-6 scale via GPT-3.5-turbo zero-shot evaluation

---

## 8. Proposed Re-Annotation Pipeline for MMSci (Reference-Based to Rubric-Based)

Based on all the above research, here is a detailed specification for converting MMSci from reference-based to rubric-based evaluation for non-verifiable RL training:

### Phase 1: Rubric Generation per Figure

For each (figure, reference_caption) pair in MMSci:

**Step 1 -- Structured Caption Analysis.** Use an LLM (e.g., GPT-4o, Claude) to decompose the reference caption into atomic claims:
- Factual statements about what is shown in each sub-figure
- Quantitative claims (numbers, trends, comparisons)
- Methodological descriptions (what technique produced this visualization)
- Interpretive claims (what the results mean scientifically)
- Structural/compositional descriptions (layout, labels, axes)

**Step 2 -- Dimension-Specific Criteria Extraction.** For each figure, generate criteria along these dimensions (inspired by SciCapenter + RubiCap + TechImage-Bench):
- **Visual Accuracy:** Does the caption correctly describe what is visually present?
- **Sub-figure Coverage:** Are all sub-figures (a, b, c...) addressed?
- **Quantitative Fidelity:** Are numerical values, trends, and comparisons correctly stated?
- **Scientific Terminology:** Is appropriate domain-specific vocabulary used?
- **Methodological Context:** Is the experimental/computational method mentioned?
- **Interpretive Validity:** Are conclusions/takeaways scientifically sound?
- **Structural Description:** Are axes, labels, legends, and scales described?

**Step 3 -- Binary Criterion Formulation.** Convert each extracted claim into a binary pass/fail criterion with severity weight:
- Critical (3.0): Core factual/scientific correctness
- Important (2.0): Completeness and coverage
- Minor (1.0): Stylistic and structural polish

**Step 4 -- Teacher Committee Augmentation (optional but recommended).** Generate 3-5 alternative captions using diverse VLMs. Use consensus analysis to identify which criteria are universally agreed upon (higher confidence) vs. model-specific.

### Phase 2: Rubric Validation

- Sample ~500 figure-rubric pairs for human expert review across the 10 PhD-annotated domains
- Measure inter-annotator agreement (target Cohen's Kappa >= 0.7)
- Iteratively refine the rubric generation prompt based on expert feedback

### Phase 3: Reward Signal for RL

**Explicit aggregation:** Score = sum(w_i * binary_score_i) / sum(w_i), normalized to [0, 1]

**LLM Judge:** For each generated caption, an LLM evaluates each binary criterion, producing the reward signal. Use position-switching and multi-sample scoring for robustness.

**Training:** Use GRPO with the rubric-based reward, computing advantage estimates from the structured scores rather than a single scalar.

### Key Design Decisions

1. **Instance-specific rubrics** (per-figure, not generic) -- essential given the diversity of 72 disciplines
2. **Reference-grounded** -- rubrics are derived from the high-quality Nature Communications captions, ensuring expert-level grounding
3. **Abstract-conditioned** -- for abstract-grounded captioning, rubrics should also account for whether the caption integrates information from the abstract
4. **Severity weighting** -- prevents the model from gaming easy criteria while ignoring hard scientific content
5. **Discipline-aware** -- rubric generation prompts should include the discipline label so criteria are domain-appropriate

Sources:
- [MMSci Paper (arXiv:2407.04903)](https://arxiv.org/abs/2407.04903)
- [MMSci HTML v3](https://arxiv.org/html/2407.04903v3)
- [MMSci GitHub Repository](https://github.com/Leezekun/MMSci)
- [MMSci DATACARD](https://github.com/Leezekun/MMSci/blob/main/mmsci-data/DATACARD.md)
- [MMSci OpenReview](https://openreview.net/forum?id=DEOV74Idsg)
- [RubiCap (arXiv:2603.09160)](https://arxiv.org/html/2603.09160)
- [Rubric-ARM (arXiv:2602.01511)](https://arxiv.org/abs/2602.01511)
- [OpenRubrics (arXiv:2510.07743)](https://arxiv.org/abs/2510.07743)
- [TechImage-Bench (arXiv:2512.12220)](https://arxiv.org/html/2512.12220)
- [SciCapenter (arXiv:2403.17784)](https://arxiv.org/html/2403.17784v1)
- [Rubric-Based Rewards for RL (Cameron Wolfe blog)](https://cameronrwolfe.substack.com/p/rubric-rl)
- [Five Years of SciCap](https://arxiv.org/html/2512.21789)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6da27f40-ee2b-46b6-8eb3-038d820d948d",
  "isSidechain": true,
  "agentId": "a87c831bd24e0caa5",
  "requestId": "req_011CbUFt29MXB7xTDsoqka1n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cf6f809-385c-4bea-8f53-716089069083",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5cb25333-85e4-44a3-84c0-f6b18d9f6e2d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTNecVh7DkmnCZzNYh5q8s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 30825,
      "output_tokens": 4100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 495
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4100,
          "cache_read_input_tokens": 30825,
          "cache_creation_input_tokens": 495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 495,
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
