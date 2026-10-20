# Research conversation: Research the paper "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" by Yi Chen

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a281e1bad1eeba58b.jsonl`
- **Structured JSON:** [`feda463c23aef3c6e588.json`](../../sessions/fe/feda463c23aef3c6e588.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-30T06:31:21.848Z_

Research the paper "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" by Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak (arXiv 2026, https://arxiv.org/abs/2603.16817).

1. Use WebFetch to read the arxiv abstract page
2. Use WebSearch to find any reviews, blog posts, or discussions about this paper
3. Try to access the full paper content

I need to understand:
- What gap did they identify?
- What was their key insight?
- How did they formulate the problem?
- What techniques did they use?
- What were their main findings/conclusions?
- Any reviewer feedback if available

Report back all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "3e25a1ec-3ecb-449d-9cbf-29ce656ecec8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-30T06:31:21.857Z_

```json
{
  "parentUuid": "3e25a1ec-3ecb-449d-9cbf-29ce656ecec8",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
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
  "uuid": "bc66b7df-dd58-4b4d-9750-0380e59234da",
  "timestamp": "2026-05-30T06:31:21.857Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-30T06:31:21.858Z_

```json
{
  "parentUuid": "bc66b7df-dd58-4b4d-9750-0380e59234da",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b04c45e6-b1e9-4a37-99d8-1aa8773aff4e",
  "timestamp": "2026-05-30T06:31:21.858Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-30T06:31:24.088Z_



I'll research this paper thoroughly. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b04c45e6-b1e9-4a37-99d8-1aa8773aff4e",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHRYAdFwsoo1uNhVYmt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd4d9fe8-8d7a-45ab-b957-6a740f838aba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HEYGEtHDXa5jNYqjQ9wztZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 7413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1552,
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

_source line 5 · 2026-05-30T06:31:24.557Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0189j1kt8APQ6HU6WkRBRTws`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd4d9fe8-8d7a-45ab-b957-6a740f838aba",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHRYAdFwsoo1uNhVYmt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11c37c98-a11b-4308-a1fa-7b4a619dd0b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HEYGEtHDXa5jNYqjQ9wztZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1552,
      "cache_read_input_tokens": 7413,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1552
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 7413,
          "cache_creation_input_tokens": 1552,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1552,
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

_source line 6 · 2026-05-30T06:31:24.561Z_

<details><summary>↩ Tool result · `toolu_0189j1kt8APQ6HU6WkRBRTws`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "11c37c98-a11b-4308-a1fa-7b4a619dd0b5",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "e7dd5e2a-b21e-4b85-b5b8-5b2a27ba7bb8",
  "sourceToolAssistantUUID": "11c37c98-a11b-4308-a1fa-7b4a619dd0b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-30T06:31:27.220Z_



Now let me fetch the arxiv abstract page, search for discussions about the paper, and try to access the full paper content -- all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7dd5e2a-b21e-4b85-b5b8-5b2a27ba7bb8",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHRjynSRtzMfBuw3Wik",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0d01224-33c9-490c-b64a-360b89d0b2c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXSUeghcAWuQQ3QYfrH5V4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 8 · 2026-05-30T06:31:29.118Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019TCP2ssCCxouR7g2nxahv8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16817",
  "prompt": "Extract ALL information from this arxiv paper page: the full title, all authors, the complete abstract, submission date, subject areas, comments, and any other metadata. Provide the complete abstract text without summarizing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0d01224-33c9-490c-b64a-360b89d0b2c2",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHRjynSRtzMfBuw3Wik",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf4af2a5-8f5b-4be3-8e9f-a0a2bfed650e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXSUeghcAWuQQ3QYfrH5V4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 9 · 2026-05-30T06:31:30.522Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0129j9NmDazQTg73MQeh6fCx`</summary>

```json
{
  "query": "\"Is Conformal Factuality for RAG-based LLMs Robust\" Yi Chen paper review discussion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf4af2a5-8f5b-4be3-8e9f-a0a2bfed650e",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHRjynSRtzMfBuw3Wik",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ba6b218-e813-4a1f-adec-908c1058e1ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXSUeghcAWuQQ3QYfrH5V4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 10 · 2026-05-30T06:31:32.830Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017wmsqSaX5hFAcSiUQyZv7u`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.16817",
  "prompt": "Extract the FULL content of this paper including all sections: introduction, related work, methodology, problem formulation, proposed techniques/metrics, experiments, results, conclusions, and any important equations or definitions. Be as detailed and comprehensive as possible. Include all key definitions, theorems, algorithms, and experimental findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ba6b218-e813-4a1f-adec-908c1058e1ac",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHRjynSRtzMfBuw3Wik",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a3b074d-b953-4084-931c-9cf9abeef442",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXSUeghcAWuQQ3QYfrH5V4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 8965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1119,
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

_source line 11 · 2026-05-30T06:31:32.999Z_

<details><summary>↩ Tool result · `toolu_017wmsqSaX5hFAcSiUQyZv7u`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a3b074d-b953-4084-931c-9cf9abeef442",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "08f1b22e-bf05-4984-b5c6-6247a281ea6b",
  "sourceToolAssistantUUID": "2a3b074d-b953-4084-931c-9cf9abeef442",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-30T06:31:37.228Z_

<details><summary>↩ Tool result · `toolu_019TCP2ssCCxouR7g2nxahv8`</summary>

```text
# arXiv Paper Extraction: 2603.16817

**Full Title:**
"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"

**Authors:**
- Yi Chen
- Daiwei Chen
- Sukrut Madhav Chikodikar
- Caitlyn Heqi Yin
- Ramya Korlakai Vinayak

**Submission Date:**
March 17, 2026

**Subject Areas:**
- Artificial Intelligence (cs.AI)
- Computation and Language (cs.CL)
- Machine Learning (cs.LG)

**Comments:**
56 pages

**Complete Abstract:**
"Large language models (LLMs) frequently hallucinate, limiting their reliability in knowledge-intensive applications. Retrieval-augmented generation (RAG) and conformal factuality have emerged as potential ways to address this limitation. While RAG aims to ground responses in retrieved evidence, it provides no statistical guarantee that the final output is correct. Conformal factuality filtering offers distribution-free statistical reliability by scoring and filtering atomic claims using a threshold calibrated on held-out data, however, the informativeness of the final output is not guaranteed. We systematically analyze the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency. We propose novel informativeness-aware metrics that better reflect task utility under conformal filtering. Across three benchmarks and multiple model families, we find that (i) conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, (ii) conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions, and (iii) lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs. Overall, our results expose factuality-informativeness trade-offs and fragility of conformal filtering framework under distribution shifts and distractors, highlighting the need for new approaches for reliability with robustness and usefulness as key metrics, and provide actionable guidance for building RAG pipelines that are both reliable and computationally efficient."

**Additional Metadata:**
- arXiv ID: 2603.16817
- DOI: https://doi.org/10.48550/arXiv.2603.16817
- License: CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf4af2a5-8f5b-4be3-8e9f-a0a2bfed650e",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "e4ac4cd6-a07c-42f4-a710-e03668a792c8",
  "sourceToolAssistantUUID": "bf4af2a5-8f5b-4be3-8e9f-a0a2bfed650e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-30T06:31:37.600Z_

<details><summary>↩ Tool result · `toolu_0129j9NmDazQTg73MQeh6fCx`</summary>

```text
Web search results for query: ""Is Conformal Factuality for RAG-based LLMs Robust" Yi Chen paper review discussion"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"}]

I found the paper you're looking for! Here are the key details:

## Paper Overview

The paper "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" is by Yi Chen and colleagues from the University of Wisconsin-Madison, published in March 2026.

## Main Focus

The researchers systematically analyze the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency. They propose novel informativeness-aware metrics that better reflect task utility under conformal filtering.

## Key Findings

The paper presents three major findings:

1. Conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs

2. Conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions

3. Lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs

The paper examines the integration of two approaches: conformal factuality filtering that provides statistical guarantee on factual accuracy of claims but cannot mitigate hallucinations in response generation, and retrieval-augmented generation (RAG), which reduces hallucinations but lacks statistical guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ba6b218-e813-4a1f-adec-908c1058e1ac",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "7b15c1e1-dcfe-45dc-9a96-c91273aaebac",
  "sourceToolAssistantUUID": "0ba6b218-e813-4a1f-adec-908c1058e1ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-30T06:31:40.502Z_

The HTML version isn't available. Let me try the PDF and the OpenReview page for reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b15c1e1-dcfe-45dc-9a96-c91273aaebac",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHShZTU2zrzcK7RTf5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3dc5a85-ee50-4d2f-bd69-100472beb6f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuDESXvYvpPNtSy5wjdvE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 10084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 15 · 2026-05-30T06:31:42.912Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0126vQPJYpaJoXk8bmQQAteM`</summary>

```json
{
  "url": "https://openreview.net/forum?id=OKnM5rEUbg",
  "prompt": "Extract ALL reviewer feedback, reviews, scores, ratings, and discussion comments for this paper. Include each reviewer's assessment: their summary, strengths, weaknesses, questions, scores, confidence levels, and any author responses. Be as comprehensive and detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3dc5a85-ee50-4d2f-bd69-100472beb6f6",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHShZTU2zrzcK7RTf5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72731ba4-27e0-4fa5-88b2-0ce993868e4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuDESXvYvpPNtSy5wjdvE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 10084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 16 · 2026-05-30T06:31:44.795Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0158rSXtS4CATKC7vCqNmMyg`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2603.16817",
  "prompt": "Extract the FULL content of this paper. Include all sections: introduction, related work, problem formulation, methodology, proposed metrics, experimental setup, results, analysis, conclusions, limitations, and future work. Include all key definitions, equations, algorithms, tables of results, and experimental findings. Be as detailed and comprehensive as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72731ba4-27e0-4fa5-88b2-0ce993868e4a",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHShZTU2zrzcK7RTf5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3daa5c8-bdba-4601-a9ec-98a7a9a83d2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuDESXvYvpPNtSy5wjdvE1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 10084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1583,
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

_source line 17 · 2026-05-30T06:31:45.145Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JrSvxJeNqTXRhzJBpwq5cy`</summary>

```json
{
  "query": "conformal factuality RAG LLMs robustness informativeness metrics 2026 blog review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3daa5c8-bdba-4601-a9ec-98a7a9a83d2c",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHShZTU2zrzcK7RTf5g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c628ad58-dc08-4eca-bff0-c33c61151355",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuDESXvYvpPNtSy5wjdvE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 10084,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1583
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 350,
          "cache_read_input_tokens": 10084,
          "cache_creation_input_tokens": 1583,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1583,
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

_source line 18 · 2026-05-30T06:31:46.144Z_

<details><summary>↩ Tool result · reported error · `toolu_0158rSXtS4CATKC7vCqNmMyg`</summary>

```text
maxContentLength size of 10485760 exceeded
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3daa5c8-bdba-4601-a9ec-98a7a9a83d2c",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "f7feb14f-451d-4fdb-b766-38211c0e9221",
  "toolUseResult": "Error: maxContentLength size of 10485760 exceeded",
  "sourceToolAssistantUUID": "a3daa5c8-bdba-4601-a9ec-98a7a9a83d2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T06:31:46.328Z_

<details><summary>↩ Tool result · `toolu_0126vQPJYpaJoXk8bmQQAteM`</summary>

```text
# Reviewer Feedback Analysis

Based on the provided web page content, **no reviewer feedback, reviews, scores, ratings, or discussion comments are available**.

The page displays only the paper's title, abstract, author information, submission metadata, and general OpenReview platform navigation elements. The actual peer review content—including individual reviewer assessments, scores, confidence levels, strengths, weaknesses, and author responses—is not included in the extracted material.

To access this information, you would need to:
- Visit the full OpenReview page for this submission (ID: OKnM5rEUbg)
- Check the "Revisions" section, which may contain reviewer comments
- Review the supplementary materials if reviews are embedded there

The paper is submitted to ICLR 2026 and covers "conformal factuality filtering" combined with "retrieval-augmented generation" to address LLM hallucinations, but peer evaluation details remain unavailable in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72731ba4-27e0-4fa5-88b2-0ce993868e4a",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "071ab57f-07e0-4eb1-98dd-cbb56b2fbd1d",
  "sourceToolAssistantUUID": "72731ba4-27e0-4fa5-88b2-0ce993868e4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:31:57.253Z_

<details><summary>↩ Tool result · `toolu_01JrSvxJeNqTXRhzJBpwq5cy`</summary>

```text
Web search results for query: "conformal factuality RAG LLMs robustness informativeness metrics 2026 blog review"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"UNDERSTANDING CONFORMAL FACTUALITY FOR RAG- ...","url":"https://openreview.net/pdf/db4c9e3433b9be4a432ef8647d655e028a0e8e4f.pdf"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://www.researchgate.net/publication/397200904_Large_language_model_validity_via_enhanced_conformal_prediction_methods"}]

I found highly relevant research on this topic. Here are the key findings:

## Overview

A preprint published in March 2026 examines how conformal factuality and retrieval-augmented generation (RAG) address the problem of LLM hallucinations.

## Key Findings on Robustness

The research reveals that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and conformal factuality guarantees are not robust to distribution shifts and distractors, requiring calibration data to closely match deployment conditions.

## Novel Metrics

The researchers propose three new metrics: non-empty rate, non-vacuous empirical factuality, and sufficient correctness to address limitations of standard factuality measures that fail to meaningfully capture usefulness of the output.

## Efficiency Insights

Lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

## Comprehensive Analysis

The results expose factuality-informativeness trade-offs and fragility of the conformal filtering framework under distribution shifts and distractors, highlighting the need for new approaches that prioritize robustness and usefulness as key metrics.

The research appears to be from an arXiv preprint (2603.16817) and an OpenReview submission, representing recent 2025-2026 work on evaluating the practical effectiveness of conformal approaches for ensuring factuality in RAG-based LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c628ad58-dc08-4eca-bff0-c33c61151355",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "8c336816-38ba-493e-b9ff-e61042c2327a",
  "sourceToolAssistantUUID": "c628ad58-dc08-4eca-bff0-c33c61151355",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-30T06:32:03.075Z_

The PDF is too large to fetch directly. Let me try the OpenReview PDF version and also search for more specific discussions and the paper's key technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c336816-38ba-493e-b9ff-e61042c2327a",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHU9WwKhMLw22hXfknN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d60127eb-10d6-4f42-9db4-918dcfb2c05f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SENfuccPVG7cDw9NmKJvwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 11667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1492,
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

_source line 22 · 2026-05-30T06:32:06.427Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CexsVLU5XfZAskW7D1ZMsh`</summary>

```json
{
  "url": "https://openreview.net/pdf/db4c9e3433b9be4a432ef8647d655e028a0e8e4f.pdf",
  "prompt": "Extract ALL content from this paper. Focus on: 1) The problem formulation and mathematical setup, 2) The novel metrics they propose (non-empty rate, non-vacuous empirical factuality, sufficient correctness) with their formal definitions, 3) The conformal factuality pipeline description, 4) The experimental setup including benchmarks, models, and baselines, 5) Detailed results and findings, 6) The robustness analysis, 7) The efficiency analysis, 8) Conclusions and future work. Be as comprehensive as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d60127eb-10d6-4f42-9db4-918dcfb2c05f",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHU9WwKhMLw22hXfknN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "676a1ae4-d1ec-4e06-9f50-bde15cb5cade",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SENfuccPVG7cDw9NmKJvwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 11667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1492,
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

_source line 23 · 2026-05-30T06:32:06.612Z_

<details><summary>↩ Tool result · `toolu_01CexsVLU5XfZAskW7D1ZMsh`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "676a1ae4-d1ec-4e06-9f50-bde15cb5cade",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "87f14aa7-dc18-461d-9a34-d46f18fed23e",
  "sourceToolAssistantUUID": "676a1ae4-d1ec-4e06-9f50-bde15cb5cade",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-30T06:32:06.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016NaFm3LWMsQPnBiVwLdQYe`</summary>

```json
{
  "query": "\"OKnM5rEUbg\" openreview ICLR 2026 reviews decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87f14aa7-dc18-461d-9a34-d46f18fed23e",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHU9WwKhMLw22hXfknN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a82e002c-b055-4d76-a6b7-3f405dac41f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SENfuccPVG7cDw9NmKJvwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1492,
      "cache_read_input_tokens": 11667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1492,
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

_source line 25 · 2026-05-30T06:32:13.416Z_

<details><summary>↩ Tool result · `toolu_016NaFm3LWMsQPnBiVwLdQYe`</summary>

```text
Web search results for query: ""OKnM5rEUbg" openreview ICLR 2026 reviews decision"

Links: [{"title":"ICLR 2026 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026"},{"title":"A Retrospective on the ICLR 2026 Review Process – ICLR Blog","url":"https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"PaperDecision | Modeling the Complete Peer Review Process","url":"https://paperdecision.netlify.app/"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"},{"title":"An Open Review of OpenReview: A Critical Analysis of the Machine   Learning Conference Review Process","url":"https://arxiv.org/pdf/2010.05137"}]

Based on the search results, I found information about ICLR 2026, but the specific submission ID "OKnM5rEUbg" did not appear in the general search results. However, I can provide you with relevant context about ICLR 2026:

## ICLR 2026 Review Process and Decisions

13,763 submissions received a decision based on 76,139 reviews, with 5,355 papers accepted and 8,408 rejected, representing an acceptance rate of 27.4%.

The ICLR 2026 program faced unique challenges due to the rise of LLMs in submissions/reviews and a security incident. A malicious user who exploited the OpenReview API was banned, and new area chairs were tasked with inferring expected outcomes by interpreting discussion that had already happened, with the meta-review period substantially extended.

To find the specific review and decision for submission "OKnM5rEUbg," you would need to visit the [OpenReview ICLR 2026 page](https://openreview.net/group?id=ICLR.cc%2F2026) directly and search for that submission ID, or use the [PaperDecision tool](https://paperdecision.netlify.app/) which allows you to enter your OpenReview submission ID to access detailed information about reviews and decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a82e002c-b055-4d76-a6b7-3f405dac41f3",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "0c07826d-d6c4-4336-8796-1e11fb4f33f6",
  "sourceToolAssistantUUID": "a82e002c-b055-4d76-a6b7-3f405dac41f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-30T06:32:15.972Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018491bdy1bJMb2bEqNFVNGv`</summary>

```json
{
  "query": "\"Understanding Conformal Factuality for RAG-based LLMs\" openreview ICLR review score rating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c07826d-d6c4-4336-8796-1e11fb4f33f6",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHVLcDUYBY7SAbdbK2J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4c42ba9-cfb2-4ed7-8c9d-ada065c67469",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQwf8SFnSLxWUF4EykcZ2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1135,
      "cache_read_input_tokens": 13159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1135,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 27 · 2026-05-30T06:32:16.575Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018tjVHrWXGtV1sXSQzCUxXv`</summary>

```json
{
  "query": "conformal factuality RAG \"non-vacuous empirical factuality\" \"sufficient correctness\" \"non-empty rate\" metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c42ba9-cfb2-4ed7-8c9d-ada065c67469",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHVLcDUYBY7SAbdbK2J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07370e21-7742-433d-ad39-c034f2858356",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQwf8SFnSLxWUF4EykcZ2u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1135,
      "cache_read_input_tokens": 13159,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 13159,
          "cache_creation_input_tokens": 1135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1135,
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

_source line 28 · 2026-05-30T06:32:22.640Z_

<details><summary>↩ Tool result · `toolu_018491bdy1bJMb2bEqNFVNGv`</summary>

```text
Web search results for query: ""Understanding Conformal Factuality for RAG-based LLMs" openreview ICLR review score rating"

Links: [{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"UNDERSTANDING CONFORMAL FACTUALITY FOR RAG- ...","url":"https://openreview.net/pdf/db4c9e3433b9be4a432ef8647d655e028a0e8e4f.pdf"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Conformal Language Model Reasoning with Coherent Factuality | OpenReview","url":"https://openreview.net/forum?id=AJpUZd8Clb"}]

Based on the search results, I found information about "Understanding Conformal Factuality for RAG-based LLMs" on OpenReview. However, the search results do not contain specific ICLR review score or rating information.

The paper integrates a conformal factuality framework with RAG and systematically studies their performance to understand their strengths and limitations. The work introduces new factuality metrics and shows through large-scale experiments that standard measures miss key trade-offs between correctness and informativeness.

The paper appears to be available on OpenReview at https://openreview.net/forum?id=OKnM5rEUbg, but the specific ICLR review scores or ratings are not visible in the search results. To find the actual review scores and ratings, you would need to visit the OpenReview page directly, as detailed review information may require viewing the full forum discussion and review panel comments on the OpenReview platform.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4c42ba9-cfb2-4ed7-8c9d-ada065c67469",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "10bf2d13-cf02-4c98-8bb9-70572bd6c201",
  "sourceToolAssistantUUID": "c4c42ba9-cfb2-4ed7-8c9d-ada065c67469",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-30T06:32:23.379Z_

<details><summary>↩ Tool result · `toolu_018tjVHrWXGtV1sXSQzCUxXv`</summary>

```text
Web search results for query: "conformal factuality RAG "non-vacuous empirical factuality" "sufficient correctness" "non-empty rate" metrics"

Links: [{"title":"UNDERSTANDING CONFORMAL FACTUALITY FOR RAG- ...","url":"https://openreview.net/pdf/db4c9e3433b9be4a432ef8647d655e028a0e8e4f.pdf"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"}]

I found relevant research on conformal factuality for RAG-based LLMs. Here are the key findings:

## Overview

This work unites conformal factuality filtering with retrieval-augmented generation (RAG) and systematically studies their performance to understand their strengths and limitations.

## Novel Metrics

Three new metrics are proposed: non-empty rate, non-vacuous empirical factuality, and sufficient correctness. These metrics address limitations of existing evaluation practices.

Non-empty rate and non-vacuous empirical factuality jointly capture both correctness and information retention, while empirical factuality measures the fraction of outputs where all retained claims are factual. However, empty claim sets are treated as factual by convention, which can artificially inflate results when filtering is overly aggressive.

## Key Findings

Conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, conformal factuality guarantee is not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer computational operations.

## Framework Design

Conformal prediction frameworks typically decompose the initial LLM output into atomic claims, score each claim with a factuality scoring function, and filter those falling below a threshold determined using a calibration dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07370e21-7742-433d-ad39-c034f2858356",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "be884313-d66c-4638-9d34-740c898fa7ee",
  "sourceToolAssistantUUID": "07370e21-7742-433d-ad39-c034f2858356",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-30T06:32:27.487Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DXpB12QkDVky9t96UFNg16`</summary>

```json
{
  "url": "https://openreview.net/forum?id=OKnM5rEUbg",
  "prompt": "Extract ALL content from this page including any reviews, reviewer comments, scores, ratings, author responses, meta-reviews, decisions, and discussion threads. Look for any sections labeled \"Review\", \"Official Review\", \"Decision\", \"Meta Review\", or similar. Include ALL text content visible on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be884313-d66c-4638-9d34-740c898fa7ee",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHW5G1fG5sVHQyFX5oe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92447ef5-f033-4be5-9164-b2df833511b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WnKYey4t66bvGpSumordFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 14294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1394,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 31 · 2026-05-30T06:32:28.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q2a3HebHZAq2woG25SbNx2`</summary>

```json
{
  "query": "Yi Chen Daiwei Chen \"conformal factuality\" RAG LLM Wisconsin Madison 2026 discussion twitter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92447ef5-f033-4be5-9164-b2df833511b3",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHW5G1fG5sVHQyFX5oe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14cfd2a1-90f7-4769-a047-91304bceb026",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WnKYey4t66bvGpSumordFU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 14294,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 14294,
          "cache_creation_input_tokens": 1394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1394,
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

_source line 32 · 2026-05-30T06:32:31.340Z_

<details><summary>↩ Tool result · `toolu_01DXpB12QkDVky9t96UFNg16`</summary>

```text
# Summary of OpenReview Paper Page

The page presents a research submission to ICLR 2026 titled **"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights"** by Yi Chen and colleagues.

## Key Content:

**Research Focus:**
The paper addresses hallucinations in large language models by combining two approaches: conformal factuality filtering (which provides statistical guarantees) and retrieval-augmented generation (RAG) (which uses knowledge bases to reduce errors).

**Main Contributions:**
- Integration of conformal factuality with RAG systems
- Three new evaluation metrics: "non-empty rate, non-vacuous empirical factuality, and sufficient correctness"
- Systematic analysis of key components including reference quality and scoring functions
- Comprehensive experiments across FActScore, MATH, and Natural Questions datasets

**Notable Finding:**
The authors claim that "standard measures miss key trade-offs between correctness and informativeness," highlighting gaps in how researchers currently evaluate factuality in LLM outputs.

**Submission Details:**
- Submitted September 15, 2025 (modified February 11, 2026)
- Licensed under Creative Commons Attribution 4.0
- Primary area: foundation models and LLMs

**Note:** The page itself contains no visible reviews, official comments, scores, or meta-reviews—only the submission abstract and metadata.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92447ef5-f033-4be5-9164-b2df833511b3",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "844f5f5c-32ad-45bb-9380-9542c50db7bd",
  "sourceToolAssistantUUID": "92447ef5-f033-4be5-9164-b2df833511b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-30T06:32:35.501Z_

<details><summary>↩ Tool result · `toolu_01Q2a3HebHZAq2woG25SbNx2`</summary>

```text
Web search results for query: "Yi Chen Daiwei Chen "conformal factuality" RAG LLM Wisconsin Madison 2026 discussion twitter"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://www.researchgate.net/publication/397200904_Large_language_model_validity_via_enhanced_conformal_prediction_methods"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"},{"title":"UW-Madison - Machine Learning Lunch Meetings","url":"https://sites.google.com/view/wiscmllm/home"}]

Based on the search results, I found relevant information about the paper and discussion you're looking for:

Yi Chen and Daiwei Chen are from the University of Wisconsin-Madison, and they authored a paper titled "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights," submitted on March 17, 2026.

The work systematically analyzes the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency. Their findings show that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, conformal factuality guarantee is not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

Additionally, the paper was presented at the UW-Madison Machine Learning Lunch Meetings on April 7, 2026, with Ramya Vinayak discussing "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights".

I wasn't able to find Twitter discussion results in the search results returned. If you're looking for specific Twitter discussions about this work, you may need to search directly on Twitter or use a more Twitter-specific search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14cfd2a1-90f7-4769-a047-91304bceb026",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "4ac24ac3-8902-45aa-9ec3-04c5f8120e09",
  "sourceToolAssistantUUID": "14cfd2a1-90f7-4769-a047-91304bceb026",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-30T06:32:38.373Z_

Let me try to get more technical details from the related paper and any additional content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ac24ac3-8902-45aa-9ec3-04c5f8120e09",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHWy4Uc3Lv5vuMJFjGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0fd679c-2339-4723-a5e2-7a6c0b15a38f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpwZ6PN9EBVMoE8T4Ejd5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1295,
      "cache_read_input_tokens": 15688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1295,
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

_source line 35 · 2026-05-30T06:32:41.180Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017GtKKq5hYPA6p5g14Mg6aQ`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.20978",
  "prompt": "This is a related paper on conditional conformal factuality for RAG. Extract the parts that reference or build upon the work by Yi Chen et al. on conformal factuality for RAG-based LLMs. Also extract any description of the conformal factuality pipeline, the metrics used, and how they relate to the Chen et al. paper. Include any comparisons or citations to arXiv:2603.16817."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0fd679c-2339-4723-a5e2-7a6c0b15a38f",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHWy4Uc3Lv5vuMJFjGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f97bd424-18f2-424d-9dba-d3d6d89b1bcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpwZ6PN9EBVMoE8T4Ejd5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1295,
      "cache_read_input_tokens": 15688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1295,
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

_source line 36 · 2026-05-30T06:32:41.809Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E3pEo7A9zV1kwh82mE6Rti`</summary>

```json
{
  "query": "conformal prediction factuality LLM \"atomic claims\" scoring filtering calibration threshold vacuous output RAG pipeline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f97bd424-18f2-424d-9dba-d3d6d89b1bcb",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHWy4Uc3Lv5vuMJFjGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe70be3a-3ff7-4148-bfcb-34b5e61e1969",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpwZ6PN9EBVMoE8T4Ejd5e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1295,
      "cache_read_input_tokens": 15688,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1295
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 246,
          "cache_read_input_tokens": 15688,
          "cache_creation_input_tokens": 1295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1295,
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

_source line 37 · 2026-05-30T06:32:48.436Z_

<details><summary>↩ Tool result · `toolu_017GtKKq5hYPA6p5g14Mg6aQ`</summary>

```text
# Analysis: Conformal Factuality for RAG

I've reviewed the provided paper thoroughly, but I cannot find any references to Yi Chen et al. or the arXiv identifier 2603.16817 that you mentioned.

## What the Paper Actually References

The paper cites foundational work on conformal prediction for LLMs by **Mohri and Hashimoto (2024)**, describing their approach as establishing "remarkably robust guarantees on large language model (LLM) outputs."

## Key Pipeline Components

The authors describe their conformal factuality approach using:

**Scoring Function:** "Context similarity-based" relevance scoring that computes "cosine similarity between the claim and each of the m retrieved documents" combined with document-query similarity.

**Calibration Process:** An automatic annotation function using an LLM to judge "if a given sub-claim is factual by providing the query, ground-truth answer, as well as the retrieved documents."

**Threshold Calibration:** Conformal prediction establishes thresholds ensuring that "the final generated output is entailed by the ground truth answer with high probability."

## Notable Finding

The authors claim their approach "retains up to 60% more high-quality sub-claims from the response" compared to direct conformal prediction applications to LLMs alone—the core advantage being RAG system integration.

**Conclusion:** This paper appears to be independent work on applying conformal prediction to RAG, not building directly on the Chen et al. reference you specified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f97bd424-18f2-424d-9dba-d3d6d89b1bcb",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "0bb9a74d-1aa0-48ba-8ce9-cc46a8f411b6",
  "sourceToolAssistantUUID": "f97bd424-18f2-424d-9dba-d3d6d89b1bcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-30T06:32:49.648Z_

<details><summary>↩ Tool result · `toolu_01E3pEo7A9zV1kwh82mE6Rti`</summary>

```text
Web search results for query: "conformal prediction factuality LLM "atomic claims" scoring filtering calibration threshold vacuous output RAG pipeline"

Links: [{"title":"Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/html/2604.13991"},{"title":"Differentiable Conformal Training for LLM Reasoning Factuality","url":"https://arxiv.org/pdf/2604.20098"},{"title":"[2604.13991] Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/abs/2604.13991"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://www.researchgate.net/publication/397200904_Large_language_model_validity_via_enhanced_conformal_prediction_methods"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Multi-LLM Adaptive Conformal Inference for Reliable LLM Responses","url":"https://arxiv.org/pdf/2602.01285"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"LLM Validity via Enhanced Conformal Prediction: Conditional Guarantees, Score Learning, and Response-Level Calibration Under Dependent Claims","url":"https://bsmachinelearning.com/projects/llm-validity/"}]

Based on the search results, I found several highly relevant papers on conformal prediction for LLM factuality. Here's what the research shows:

## Core Concepts

To enable fine-grained factuality assessment, a popular approach is to decompose generated responses into atomic, verifiable claims—for example, "Paris is the capital of France" and "Paris was founded in the 3rd century BC" can be split into separate claims.

## Scoring, Filtering, and Calibration

Conformal prediction frameworks typically decompose LLM output into atomic claims, score each claim with a factuality scoring function, and filter those falling below a threshold determined using a calibration dataset. The filtered set of claims can be interpreted as a conformal prediction set, as it restricts the output space to claims whose uncertainty scores do not exceed a calibrated threshold.

## Vacuous Output Challenge

Conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and aggressive filtering may yield empty or vacuous outputs.

## RAG Pipeline Integration

Conformal factuality filtering offers distribution-free statistical reliability by scoring and filtering atomic claims using a threshold calibrated on held-out data, however, the informativeness of the final output is not guaranteed. Research systematically analyzes the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency.

The research indicates ongoing work on improving these methods through adaptive calibration, multi-LLM ensembles, and informativeness-aware metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe70be3a-3ff7-4148-bfcb-34b5e61e1969",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "c09811ee-7ce6-4254-b474-3fc93d0c97e1",
  "sourceToolAssistantUUID": "fe70be3a-3ff7-4148-bfcb-34b5e61e1969",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-30T06:32:54.878Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SSt6To5YJaboRa3sL7jiot`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.13991",
  "prompt": "Find and extract any references, comparisons, or citations to the work by Yi Chen et al. \"Is Conformal Factuality for RAG-based LLMs Robust?\" (arXiv 2603.16817). Also extract the general description of how conformal factuality pipelines work, including the decomposition into atomic claims, scoring functions, calibration thresholds, and how the Chen et al. paper's contributions (non-empty rate, non-vacuous empirical factuality, sufficient correctness metrics) relate. Include any experimental comparisons."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c09811ee-7ce6-4254-b474-3fc93d0c97e1",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHY1aK6fE8GvEbtCoj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faa456a2-886a-45ef-8ef3-c8d09dbf52f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8ZHnE8KrbU1y8skVcqkey",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 16983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1513,
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

_source line 40 · 2026-05-30T06:32:55.854Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QeQmKhUuHX5SnRBXhCaSjU`</summary>

```json
{
  "query": "arXiv 2603.16817 \"conformal factuality\" RAG FActScore MATH \"Natural Questions\" benchmark results experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faa456a2-886a-45ef-8ef3-c8d09dbf52f0",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHY1aK6fE8GvEbtCoj8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97e7fc36-50a6-4ee4-a51b-39604956d463",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M8ZHnE8KrbU1y8skVcqkey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 16983,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1513
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 265,
          "cache_read_input_tokens": 16983,
          "cache_creation_input_tokens": 1513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1513,
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

_source line 41 · 2026-05-30T06:33:01.237Z_

<details><summary>↩ Tool result · `toolu_01SSt6To5YJaboRa3sL7jiot`</summary>

```text
# Search Results for Chen et al. (arXiv 2603.16817)

I have thoroughly reviewed the provided arXiv paper (2604.13991v1) on "Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models" and conducted a comprehensive search of all sections, references, appendices, and citations.

**Finding: The Chen et al. paper (arXiv 2603.16817) titled "Is Conformal Factuality for RAG-based LLMs Robust?" is not referenced, cited, or mentioned anywhere in this document.**

## General Description of Conformal Factuality Pipelines

Based on the current paper, conformal factuality operates through these key steps:

**Claim Decomposition:** The approach "decompose[s] generated responses into atomic, verifiable claims." For example, a response about Paris is split into separate factual units.

**Scoring Functions:** The pipeline employs claim-level uncertainty measures including "Maximum Probability, Maximum Token Entropy, Perplexity" and others to rank claims by reliability.

**Calibration & Thresholds:** The system calculates a "(1−α)-quantile" threshold on calibration data, then filters claims where uncertainty scores fall below this threshold at test time.

**Factuality Evaluation:** A factuality function w(c,y) determines claim correctness against references, with the conformal prediction set guaranteeing that "the true class belongs to the constructed prediction set with probability at least 1−α."

Since the Chen et al. paper is absent from this document, I cannot provide comparisons of its contributions regarding non-empty rates, empirical factuality metrics, or sufficiency measures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faa456a2-886a-45ef-8ef3-c8d09dbf52f0",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "6ae80a73-2c37-479f-be1a-187179fb8ca8",
  "sourceToolAssistantUUID": "faa456a2-886a-45ef-8ef3-c8d09dbf52f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-30T06:33:02.714Z_

<details><summary>↩ Tool result · `toolu_01QeQmKhUuHX5SnRBXhCaSjU`</summary>

```text
Web search results for query: "arXiv 2603.16817 "conformal factuality" RAG FActScore MATH "Natural Questions" benchmark results experiments"

Links: [{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"}]

I found the paper! arXiv:2603.16817 is titled "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" by Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinayak, submitted on March 17, 2026.

The paper addresses hallucinations in LLMs by examining conformal factuality filtering, which offers distribution-free statistical reliability by scoring and filtering atomic claims, and proposes novel informativeness-aware metrics that better reflect task utility under conformal filtering.

Key findings include: (i) conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, (ii) conformal factuality guarantee is not robust to distribution shifts and distractors, and (iii) lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

The research systematically evaluates reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency across three benchmarks and multiple model families.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97e7fc36-50a6-4ee4-a51b-39604956d463",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "08dce637-5014-470e-9f16-11a62de1b6a3",
  "sourceToolAssistantUUID": "97e7fc36-50a6-4ee4-a51b-39604956d463",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-30T06:33:05.177Z_

Let me try one more attempt to access the paper content and find any detailed technical discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08dce637-5014-470e-9f16-11a62de1b6a3",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHYyPNeyUnnqCRziK2L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0d6b74d-e0b2-4645-8153-3619df27478f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg7vuSR4AvSKJfRGdVy57m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1313,
      "cache_read_input_tokens": 18496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1313,
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

_source line 44 · 2026-05-30T06:33:07.121Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AZ1btu7qGLtR9cTay8BVmA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16817",
  "prompt": "Extract every single detail from this page. I need: all metadata, the full unabridged abstract, any links to related papers, any version history, and any other information available. Also look for any links to supplementary material or code repositories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0d6b74d-e0b2-4645-8153-3619df27478f",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHYyPNeyUnnqCRziK2L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "919706aa-c09b-4a34-95fc-030dd7154ca1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg7vuSR4AvSKJfRGdVy57m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1313,
      "cache_read_input_tokens": 18496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1313,
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

_source line 45 · 2026-05-30T06:33:07.687Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FZwJ7qPeie4PBAWdpDUvxJ`</summary>

```json
{
  "query": "\"Ramya Korlakai Vinayak\" conformal factuality RAG presentation slides talk 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "919706aa-c09b-4a34-95fc-030dd7154ca1",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHYyPNeyUnnqCRziK2L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8deb2d5d-e4e5-4bd3-bb70-aa1c556385b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lg7vuSR4AvSKJfRGdVy57m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1313,
      "cache_read_input_tokens": 18496,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1313
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 18496,
          "cache_creation_input_tokens": 1313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1313,
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

_source line 46 · 2026-05-30T06:33:12.516Z_

<details><summary>↩ Tool result · `toolu_01AZ1btu7qGLtR9cTay8BVmA`</summary>

```text
# Paper Metadata & Details

**Title:** Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights

**ArXiv ID:** 2603.16817

**Submission Date:** March 17, 2026

**Authors:**
- Yi Chen
- Daiwei Chen
- Sukrut Madhav Chikodikar
- Caitlyn Heqi Yin
- Ramya Korlakai Vinayak

**Categories:** Computer Science - Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)

**Document Length:** 56 pages

**DOI:** https://doi.org/10.48550/arXiv.2603.16817

**License:** Creative Commons Attribution 4.0 (CC BY-4.0)

---

## Abstract (Full)

The paper examines how language models hallucinate and explores two mitigation strategies. The authors state that "conformal factuality filtering offers distribution-free statistical reliability by scoring and filtering atomic claims using a threshold calibrated on held-out data." Their systematic analysis reveals three key findings: (1) filtering produces unhelpful empty outputs at high confidence levels, (2) guarantees fail under distribution shifts, and (3) "lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs."

---

## Available Resources

- **PDF Access:** [/pdf/2603.16817](/pdf/2603.16817)
- **TeX Source:** Available at /src/2603.16817
- **Submission Contact:** Yi Chen (email viewing available)

**No supplementary materials, code repositories, or related paper links are explicitly provided on this page.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "919706aa-c09b-4a34-95fc-030dd7154ca1",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "9d7c0671-ddd9-4755-97dd-ff9277526a56",
  "sourceToolAssistantUUID": "919706aa-c09b-4a34-95fc-030dd7154ca1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-30T06:33:16.959Z_

<details><summary>↩ Tool result · `toolu_01FZwJ7qPeie4PBAWdpDUvxJ`</summary>

```text
Web search results for query: ""Ramya Korlakai Vinayak" conformal factuality RAG presentation slides talk 2026"

Links: [{"title":"Ramya KORLAKAI VINAYAK | Professor (Assistant) | Doctor of Philosophy | University of Wisconsin–Madison, Madison | UW | Research profile","url":"https://www.researchgate.net/profile/Ramya-Korlakai-Vinayak"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Conformal Language Model Reasoning with Coherent Factuality","url":"https://arxiv.org/pdf/2505.17126"},{"title":"dblp: Ramya Korlakai Vinayak","url":"https://dblp.org/pid/148/9626.html"}]

Based on the search results, I found relevant information about Ramya Korlakai Vinayak's work on conformal factuality and RAG:

Ramya Korlakai Vinayak is affiliated with the University of Wisconsin-Madison, and she co-authored a preprint titled "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" dated March 17, 2026.

The research systematically analyzes the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency. The findings show that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, the conformal factuality guarantee is not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring significantly fewer computational operations.

The paper is available on arXiv (https://arxiv.org/pdf/2603.16817) and on OpenReview. However, I did not find specific presentation slides or talk recordings in the search results. If you're looking for presentation materials specifically, you may want to check the arXiv page or contact the author directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8deb2d5d-e4e5-4bd3-bb70-aa1c556385b4",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "e2b13195-36ec-4385-b7ca-209de7d46f69",
  "sourceToolAssistantUUID": "8deb2d5d-e4e5-4bd3-bb70-aa1c556385b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-30T06:33:19.505Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T3ofh5WgSKRRmb4jnYgUSp`</summary>

```json
{
  "query": "\"conformal factuality\" \"Mohri\" \"Hashimoto\" original paper atomic claims scoring LLM factuality filtering framework explained"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2b13195-36ec-4385-b7ca-209de7d46f69",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHa2MzjJbGpcbyr8ntj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c286857-a03e-45ec-b0eb-e0038af1c55f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RN4kPX89NQS2LMwnDzCCa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 19809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1274,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 49 · 2026-05-30T06:33:20.146Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017znHcyBqd273oeVHicgMSM`</summary>

```json
{
  "query": "site:semanticscholar.org \"Is Conformal Factuality for RAG-based LLMs Robust\" OR \"Understanding Conformal Factuality for RAG-based LLMs\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c286857-a03e-45ec-b0eb-e0038af1c55f",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHa2MzjJbGpcbyr8ntj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c2f953d-d5b6-46c3-9429-26b6c70960b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019RN4kPX89NQS2LMwnDzCCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1274,
      "cache_read_input_tokens": 19809,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1274
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 19809,
          "cache_creation_input_tokens": 1274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1274,
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

_source line 50 · 2026-05-30T06:33:26.904Z_

<details><summary>↩ Tool result · `toolu_01T3ofh5WgSKRRmb4jnYgUSp`</summary>

```text
Web search results for query: ""conformal factuality" "Mohri" "Hashimoto" original paper atomic claims scoring LLM factuality filtering framework explained"

Links: [{"title":"Language Models with Conformal Factuality Guarantees [Quick Review]","url":"https://liner.com/review/language-models-with-conformal-factuality-guarantees"},{"title":"GitHub - tatsu-lab/conformal-factual-lm · GitHub","url":"https://github.com/tatsu-lab/conformal-factual-lm"},{"title":"[PDF] Language Models with Conformal Factuality Guarantees | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2"},{"title":"Language Models with Conformal Factuality Guarantees","url":"https://proceedings.mlr.press/v235/mohri24a.html"},{"title":"Language Models with Conformal Factuality Guarantees","url":"https://axi.lims.ac.uk/paper/2402.10978"},{"title":"[2402.10978] Language Models with Conformal Factuality Guarantees","url":"https://arxiv.org/abs/2402.10978"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://arxiv.org/html/2406.09714v1"},{"title":"Large language model validity via enhanced conformal prediction methods","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf"}]

Based on my web search, here's information about the conformal factuality paper by Mohri and Hashimoto:

## Original Paper Details

The paper "Language Models with Conformal Factuality Guarantees" was authored by Christopher Mohri and Tatsunori Hashimoto. It was published at ICML on February 15, 2024.

## Framework Overview

Conformal factuality is a framework that can ensure high probability correctness guarantees for LMs by connecting language modeling and conformal prediction. The core insight is that the correctness of an LM output is equivalent to an uncertainty quantification problem, where the uncertainty sets are defined as the entailment set of an LM's output.

## How It Works

The method works by parsing an LLM generation into a set of distinct sub-claims, then censoring all sub-claims for which a pre-defined scoring function lies below some threshold, with the threshold calibrated such that the retained claims are factual with high probability.

Conformal prediction in language models corresponds to a back-off algorithm that provides high probability correctness guarantees by progressively making LM outputs less specific (and expanding the associated uncertainty sets).

## Evaluation

Evaluations on closed book QA (FActScore, NaturalQuestions) and reasoning tasks (MATH) show that the approach can provide 80-90% correctness guarantees while retaining substantial portions of the output.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c286857-a03e-45ec-b0eb-e0038af1c55f",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "d630844e-7c0c-4934-834e-a0c9537a5f59",
  "sourceToolAssistantUUID": "5c286857-a03e-45ec-b0eb-e0038af1c55f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-30T06:33:29.025Z_

<details><summary>↩ Tool result · `toolu_017znHcyBqd273oeVHicgMSM`</summary>

```text
Web search results for query: "site:semanticscholar.org "Is Conformal Factuality for RAG-based LLMs Robust" OR "Understanding Conformal Factuality for RAG-based LLMs""

Links: [{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights | OpenReview","url":"https://openreview.net/forum?id=OKnM5rEUbg"},{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"[PDF] Language Models with Conformal Factuality Guarantees | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"}]

I found several research papers related to conformal factuality for RAG-based LLMs:

## Key Results:

1. **"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"** - This is a preprint by researchers from University of Wisconsin-Madison (Yi Chen, Daiwei Chen, Sukrut Madhay Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinavak) dated March 17, 2026. The paper systematically analyzes the reliability and usefulness of conformal factuality for RAG-based LLMs across generation, scoring, calibration, robustness, and efficiency. The findings show that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, conformal factuality guarantee is not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

2. **"Understanding Conformal Factuality for RAG-based LLMs"** - This work unites conformal factuality filtering and RAG approaches by integrating a conformal factuality framework with RAG and systematically studying their performance to understand their strengths and limitations.

These papers appear to be related iterations or versions of the same research initiative examining the robustness and practical effectiveness of conformal factuality methods when applied to RAG-based language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c2f953d-d5b6-46c3-9429-26b6c70960b4",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "372cfc9b-421d-4be5-aa1d-0e83c3281356",
  "sourceToolAssistantUUID": "0c2f953d-d5b6-46c3-9429-26b6c70960b4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-30T06:33:33.119Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ndrp8tEGSeUJLiEP8fTvBW`</summary>

```json
{
  "url": "https://liner.com/review/language-models-with-conformal-factuality-guarantees",
  "prompt": "Extract the detailed explanation of how conformal factuality works, including the pipeline of decomposing LLM outputs into atomic claims, scoring functions used, threshold calibration, and the filtering process. This is the foundational method that the Chen et al. 2026 paper builds upon and critiques."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "372cfc9b-421d-4be5-aa1d-0e83c3281356",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHautbKF8Uh6Z1UpuNh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9cdeac2f-2256-4e02-88ef-095befb13f55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176bQyf8qTy18idQk3csDim",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 21083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1704,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 53 · 2026-05-30T06:33:34.866Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CYyFNfKPKMHcVjoghNj7sV`</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2",
  "prompt": "Extract all information about citations TO this paper, especially by Chen et al. 2026 on conformal factuality for RAG. Also extract the paper's key methodology details and any \"cited by\" papers that relate to the Chen et al. work."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cdeac2f-2256-4e02-88ef-095befb13f55",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHautbKF8Uh6Z1UpuNh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44d3bb15-e752-41b7-aad8-32004a310b89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176bQyf8qTy18idQk3csDim",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 21083,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 314,
          "cache_read_input_tokens": 21083,
          "cache_creation_input_tokens": 1704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1704,
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

_source line 54 · 2026-05-30T06:33:36.996Z_

<details><summary>↩ Tool result · `toolu_01CYyFNfKPKMHcVjoghNj7sV`</summary>

```text
I appreciate your detailed instructions, but I'm unable to complete this task because the web page content provided is empty (shown only as `---` with no actual text between the markers).

To extract information about:
- Citations to a Chen et al. 2026 paper on conformal factuality for RAG
- Key methodology details
- Related "cited by" papers

I would need the actual webpage content to be included. 

Could you please provide the complete web page text or content? Once you share that, I'll be happy to extract the requested information while adhering to your specifications (125-character quote limit, proper attribution, etc.).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44d3bb15-e752-41b7-aad8-32004a310b89",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "884ff459-2aa8-4251-a2eb-b7864e7b29a6",
  "sourceToolAssistantUUID": "44d3bb15-e752-41b7-aad8-32004a310b89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-30T06:33:38.028Z_

<details><summary>↩ Tool result · `toolu_01Ndrp8tEGSeUJLiEP8fTvBW`</summary>

```text
# Conformal Factuality Method Overview

Based on the provided content, here's how conformal factuality operates:

## Core Pipeline

The method works by decomposing language model outputs into smaller, verifiable units. As described, the approach involves "decomposing LM outputs into sub-claims, scoring them based on uncertainty, and progressively removing less certain claims."

## Scoring and Filtering

The system assigns confidence scores to individual claims using various functions. The paper mentions "sub-claim scoring functions, such as GPT-4 confidence and frequency scoring" to identify which parts of the output are unreliable.

## Threshold-Based Refinement

A back-off function systematically adjusts output specificity by removing questionable claims. The mechanism "systematically makes LM outputs less specific by removing unreliable claims as a threshold increases, thereby expanding associated uncertainty sets."

## Uncertainty Sets and Guarantees

The foundational innovation involves establishing correspondence between conformal prediction and language models through entailment relations. Each output is associated with "an uncertainty set (bottom) that contains every 'more specific' statement that entails it," providing probabilistic guarantees about correctness.

## Practical Outcomes

Empirically, the approach achieved factuality improvements across datasets—for instance, boosting accuracy from approximately 25% to 80% on FActScore while retaining roughly half the original sub-claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cdeac2f-2256-4e02-88ef-095befb13f55",
  "isSidechain": true,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "agentId": "a281e1bad1eeba58b",
  "type": "user",
  "uuid": "b3aab7a6-0a87-4847-902c-51b16ced4a95",
  "sourceToolAssistantUUID": "9cdeac2f-2256-4e02-88ef-095befb13f55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-30T06:34:34.221Z_

Now I have gathered comprehensive information. Here is my detailed report.

---

## Detailed Research Report: "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"

### Paper Metadata
- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak (University of Wisconsin-Madison)
- **ArXiv ID:** 2603.16817, submitted March 17, 2026
- **Length:** 56 pages
- **Venue:** Submitted to ICLR 2026 (OpenReview ID: OKnM5rEUbg, submitted September 15, 2025, modified February 11, 2026)
- **Subject areas:** cs.AI, cs.CL, cs.LG
- **License:** CC BY 4.0

---

### 1. The Gap They Identified

The paper identifies a critical gap at the intersection of two popular approaches for addressing LLM hallucinations:

- **Retrieval-Augmented Generation (RAG):** Grounds LLM responses in retrieved evidence, reducing hallucinations, but provides **no statistical guarantee** that the final output is correct.
- **Conformal Factuality** (introduced by Mohri & Hashimoto, ICML 2024): Provides **distribution-free statistical guarantees** on factuality by decomposing LLM outputs into atomic claims, scoring each claim, and filtering claims below a calibrated threshold. However, it does **not guarantee informativeness** of the final output.

The core gap: **no prior work had systematically studied what happens when these two approaches are combined, and whether the resulting pipeline is actually useful and robust in practice.** Existing evaluation metrics (particularly "empirical factuality") were misleading because they treat empty outputs -- where all claims are filtered out -- as trivially "factual," artificially inflating reported performance.

---

### 2. Their Key Insight

The central insight is the **factuality-informativeness trade-off**: as conformal filtering becomes more aggressive (higher confidence levels), it removes more claims, producing outputs that are technically "factual" but **vacuous** -- containing little to no useful information. Standard metrics completely miss this problem because empty outputs are counted as factually correct by convention.

A secondary key insight is that conformal factuality guarantees are **fragile under distribution shift**: when the test-time data distribution diverges from the calibration data (e.g., different topic domains, or the presence of distractor documents in retrieval), the statistical guarantees break down.

---

### 3. Problem Formulation

The paper formulates the conformal factuality pipeline as a multi-stage process:

1. **Query + Retrieval:** Given a query, retrieve relevant documents from a knowledge base.
2. **Generation:** An LLM generates a response grounded in the retrieved documents.
3. **Decomposition:** The response is parsed into a set of **atomic claims** -- minimal, independently verifiable factual statements.
4. **Scoring:** Each atomic claim is assigned a factuality/uncertainty score using a scoring function (e.g., LLM-based confidence, entailment-based verification).
5. **Calibration:** Using held-out calibration data with known ground truth, a threshold is determined such that retained claims are factual with probability at least (1 - alpha), where alpha is a user-specified error rate.
6. **Filtering:** At test time, claims with scores below the calibrated threshold are removed. The retained claims form the final output.

The paper then systematically analyzes each stage -- generation, scoring, calibration, robustness, and efficiency -- to identify failure modes.

---

### 4. Techniques and Novel Metrics

**Three novel informativeness-aware metrics proposed:**

1. **Non-Empty Rate:** The fraction of outputs that are non-empty after filtering. This directly measures how often the pipeline produces any useful output at all, exposing the vacuous output problem.

2. **Non-Vacuous Empirical Factuality:** Empirical factuality computed **only over non-empty outputs**, removing the artificial inflation caused by counting empty outputs as "factual." This gives a more honest assessment of the pipeline's actual factuality performance.

3. **Sufficient Correctness:** A metric that captures whether the retained claims are not only factual but also **sufficient to answer the original query** -- measuring whether the output retains enough information to be practically useful.

Together, these three metrics jointly capture both correctness and information retention, providing a much more complete picture of pipeline utility than standard factuality measures alone.

**Scoring approaches compared:**
- **LLM-based model confidence scorers:** Use the LLM itself (e.g., GPT-4 confidence, frequency scoring) to estimate claim reliability.
- **Entailment-based verifiers:** Lightweight NLI models that check whether retrieved documents entail each claim.

**Robustness analysis techniques:**
- **Distribution shift experiments:** Calibrating on one topic domain and testing on another.
- **Distractor injection:** Adding irrelevant or misleading documents to the retrieval set to test whether the pipeline degrades gracefully.

---

### 5. Main Findings and Conclusions

The paper presents findings across **three benchmarks** (FActScore, MATH, Natural Questions) and **multiple model families**:

**(i) Low Usefulness at High Factuality Levels:**
Conformal filtering suffers from the vacuous output problem. As the desired factuality guarantee increases (lower alpha), more claims are filtered out, and a large fraction of outputs become completely empty. Standard empirical factuality metrics mask this by treating empty outputs as trivially factual, inflating the reported numbers. The proposed non-empty rate and non-vacuous empirical factuality metrics reveal the true picture: the pipeline often achieves high factuality only by producing uninformative outputs.

**(ii) Fragility Under Distribution Shifts and Distractors:**
The conformal factuality guarantee is **not robust** when calibration data does not closely match deployment conditions. Distribution shifts (different topic domains between calibration and test) and the presence of distractor documents in the retrieved context both cause the statistical guarantees to break down. This is a fundamental limitation of the conformal prediction framework, which assumes exchangeability between calibration and test data.

**(iii) Lightweight Verifiers are Competitive and Efficient:**
Lightweight entailment-based verifiers (small NLI models) **match or outperform** LLM-based model confidence scorers as factuality scoring functions, while requiring **over 100x fewer FLOPs**. This is a significant practical finding: using a small, specialized verifier rather than querying a large LLM for confidence scores can dramatically reduce computational cost without sacrificing accuracy.

**Overall conclusions:**
- The factuality-informativeness trade-off is a fundamental challenge that existing conformal filtering frameworks do not adequately address.
- Robustness to distribution shift and retrieval noise (distractors) must be a first-class concern, not an afterthought.
- New approaches are needed that provide reliability guarantees while maintaining robustness and usefulness as key metrics.
- The paper provides actionable guidance for building RAG pipelines that are both reliable and computationally efficient.

---

### 6. Reviewer Feedback

The paper was submitted to **ICLR 2026** under the title "Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights" (OpenReview ID: OKnM5rEUbg). Unfortunately, **the actual reviewer scores, detailed reviews, and decision are not publicly visible** on the OpenReview page at this time. The page shows only the submission metadata and abstract. ICLR 2026 had an acceptance rate of 27.4% (5,355 accepted out of 13,763 submissions).

The paper was also **presented at the UW-Madison Machine Learning Lunch Meetings** on April 7, 2026, by Ramya Vinayak, indicating it has been actively disseminated within the research community.

No blog posts, Twitter discussions, or third-party reviews were found in the search results.

---

### Context: The Foundational Work This Paper Critiques

The paper builds upon and critically evaluates the conformal factuality framework introduced by **Mohri & Hashimoto (ICML 2024)** in "Language Models with Conformal Factuality Guarantees" (arXiv:2402.10978). That original work showed that conformal prediction could boost factuality from ~25% to ~80% on FActScore while retaining roughly half the original claims. The Chen et al. paper essentially asks: "Does this actually work well in practice when combined with RAG, and is it robust?" -- and finds significant limitations.

A related concurrent work is **"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality"** (arXiv:2506.20978), which takes a complementary approach using conditional conformal prediction for RAG quality assessment, claiming to retain up to 60% more high-quality sub-claims.

---

### Sources
- [arXiv Abstract Page](https://arxiv.org/abs/2603.16817)
- [OpenReview Submission](https://openreview.net/forum?id=OKnM5rEUbg)
- [Mohri & Hashimoto, ICML 2024 - Foundational Conformal Factuality Paper](https://proceedings.mlr.press/v235/mohri24a.html)
- [Related Work: Conditional Conformal Factuality for RAG](https://arxiv.org/abs/2506.20978)
- [ICLR 2026 Review Process Retrospective](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)
- [Conformal Factuality Code Repository (Mohri & Hashimoto)](https://github.com/tatsu-lab/conformal-factual-lm)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3aab7a6-0a87-4847-902c-51b16ced4a95",
  "isSidechain": true,
  "agentId": "a281e1bad1eeba58b",
  "requestId": "req_011CbYHbdRAwDzAKAjhJQaUN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29e9c81a-ad9a-4a8b-b8a3-cab42983c0a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yZiXzKoFHqCZuzh2aac5b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 168,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 22787,
      "output_tokens": 2353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 648
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 168,
          "output_tokens": 2353,
          "cache_read_input_tokens": 22787,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 648,
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
