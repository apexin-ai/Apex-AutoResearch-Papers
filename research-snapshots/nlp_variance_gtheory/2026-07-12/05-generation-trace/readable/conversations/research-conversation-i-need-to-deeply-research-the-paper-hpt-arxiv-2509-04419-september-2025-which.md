# Research conversation: I need to deeply research the paper HPT (arXiv 2509.04419, September 2025) which reportedly performs adaptive switching 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a86d91baac7cc3ad6.jsonl`
- **Structured JSON:** [`9f698a7c244a8b04ccba.json`](../../sessions/9f/9f698a7c244a8b04ccba.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-27T17:50:24.112Z_

I need to deeply research the paper HPT (arXiv 2509.04419, September 2025) which reportedly performs adaptive switching between SFT and RL based on per-question rollout accuracy. This is critical for a research idea revision.

Please:
1. Use WebFetch to read the paper at https://arxiv.org/abs/2509.04419 
2. Also try https://arxiv.org/pdf/2509.04419 if needed
3. Search for "HPT adaptive switching SFT RL rollout accuracy" and "HPT hybrid policy training" to find any blog posts or discussions

I need to understand:
- What exactly is HPT's switching mechanism? Is it per-sample or per-phase?
- What metric does HPT use to decide when to do SFT vs RL?
- How does HPT's approach differ from using a pass@k-based signal?
- What are HPT's limitations?
- What benchmarks does HPT evaluate on and what results does it achieve?

Report your findings in detail (500+ words). Include direct quotes from the paper where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "9e429235-5bab-4c17-b0af-4a2bfe869233",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-27T17:50:24.117Z_

```json
{
  "parentUuid": "9e429235-5bab-4c17-b0af-4a2bfe869233",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
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
  "uuid": "68798eb6-dd9f-4a45-930e-bb79d1bc187a",
  "timestamp": "2026-05-27T17:50:24.117Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-27T17:50:24.117Z_

```json
{
  "parentUuid": "68798eb6-dd9f-4a45-930e-bb79d1bc187a",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "da5d5c70-0656-48e0-bac4-86c58331561f",
  "timestamp": "2026-05-27T17:50:24.117Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-27T17:50:27.454Z_



I'll research the HPT paper thoroughly. Let me start by fetching the paper and searching for related discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da5d5c70-0656-48e0-bac4-86c58331561f",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVn5WxtGvv4d9Mn8qsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cab9365-c90d-41d5-ac3d-b7ef1ce44f89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DgAx1qZ298CsyVKP2PzusT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9009,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9009,
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

_source line 5 · 2026-05-27T17:50:27.541Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Np5qo8qhyfcug26iNGE2ng`</summary>

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
  "parentUuid": "5cab9365-c90d-41d5-ac3d-b7ef1ce44f89",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVn5WxtGvv4d9Mn8qsb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9496eb1-ee2c-4310-ae1b-d8412bcab970",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DgAx1qZ298CsyVKP2PzusT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9009,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9009,
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

_source line 6 · 2026-05-27T17:50:27.545Z_

<details><summary>↩ Tool result · `toolu_01Np5qo8qhyfcug26iNGE2ng`</summary>

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
  "parentUuid": "c9496eb1-ee2c-4310-ae1b-d8412bcab970",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "8530ce43-abd9-4c9e-a5fe-a81185cdbbf0",
  "sourceToolAssistantUUID": "c9496eb1-ee2c-4310-ae1b-d8412bcab970",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-27T17:50:30.356Z_



Now let me fetch the paper and run searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8530ce43-abd9-4c9e-a5fe-a81185cdbbf0",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVnLSPoZP6Gt3qHmhnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9ebd107-a6a2-40f8-adf5-741b999f7ebc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1AUfkztXCapMCD34U3cc6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 8 · 2026-05-27T17:50:32.681Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NZQVNpzuXzyxUCnZE7J1ja`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.04419",
  "prompt": "Extract ALL details about this paper. I need: the full title, all authors, the complete abstract, and the full text of the paper including all sections. Focus especially on: (1) the HPT switching mechanism - is it per-sample or per-phase, (2) what metric decides SFT vs RL, (3) how it differs from pass@k, (4) benchmarks and results, (5) limitations. Include direct quotes wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9ebd107-a6a2-40f8-adf5-741b999f7ebc",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVnLSPoZP6Gt3qHmhnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54f8f8ef-82d3-47ef-b4fc-968a16568850",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1AUfkztXCapMCD34U3cc6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 9 · 2026-05-27T17:50:37.587Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VJgpGW5Bwk5ucSbnxqXFyr`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2509.04419",
  "prompt": "Extract the COMPLETE text of this paper. I need every section in full detail: abstract, introduction, method, experiments, results, limitations, conclusion. Include all equations, algorithm descriptions, benchmark results (tables), and direct quotes. Focus on: the HPT adaptive switching mechanism between SFT and RL, what metric triggers the switch, per-sample vs per-phase decisions, comparison to pass@k, and all experimental results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54f8f8ef-82d3-47ef-b4fc-968a16568850",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVnLSPoZP6Gt3qHmhnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0c883bf-dbdc-419b-a96f-4baa767de566",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1AUfkztXCapMCD34U3cc6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 10 · 2026-05-27T17:50:37.626Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q9pkCFetRuhDMQKbam75Ln`</summary>

```json
{
  "query": "HPT adaptive switching SFT RL rollout accuracy arXiv 2509.04419"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c883bf-dbdc-419b-a96f-4baa767de566",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVnLSPoZP6Gt3qHmhnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9558781-891e-4548-b4be-612d2b7b6fb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1AUfkztXCapMCD34U3cc6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 11 · 2026-05-27T17:50:37.837Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GZajgR9y8cmZLwdvgsziNS`</summary>

```json
{
  "query": "HPT hybrid policy training language model SFT reinforcement learning switching"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9558781-891e-4548-b4be-612d2b7b6fb0",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVnLSPoZP6Gt3qHmhnK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eb11d8e-0799-4c8a-9740-46af9eac72f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1AUfkztXCapMCD34U3cc6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 9009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
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

_source line 12 · 2026-05-27T17:50:39.071Z_

<details><summary>↩ Tool result · `toolu_01NZQVNpzuXzyxUCnZE7J1ja`</summary>

```text
# Paper Analysis: Towards a Unified View of Large Language Model Post-Training

## Basic Information

**Full Title:** "Towards a Unified View of Large Language Model Post-Training"

**ArXiv ID:** 2509.04419

**Authors:** Xingtai Lv, Yuxin Zuo, Youbang Sun, Hongyi Liu, Yuntian Wei, Zhekai Chen, Xuekai Zhu, Kaiyan Zhang, Bingning Wang, Ning Ding, Bowen Zhou

**Submission Date:** September 4, 2025 (revised January 20, 2026)

## Complete Abstract

The paper's abstract states that researchers demonstrate how reinforcement learning and supervised fine-tuning represent instances of a unified optimization framework. They derive what they term a "Unified Policy Gradient Estimator" and demonstrate how various post-training approaches function as gradients of a common objective under different data distribution assumptions and bias-variance tradeoffs.

The gradient estimator comprises four components: "stabilization mask, reference policy denominator, advantage estimate, and likelihood gradient."

The authors propose Hybrid Post-Training (HPT), designed to "dynamically select different training signals" while maintaining both effective exploitation of demonstrations and stable exploration. Experimental validation spans six mathematical reasoning benchmarks and two out-of-distribution test suites.

## Key Limitations Based on Available Information

Unfortunately, the webpage content provided contains only the abstract and metadata. The complete paper text—including detailed explanations of:
- The specific switching mechanism (per-sample vs. per-phase)
- The metric determining SFT versus RL selection
- Differentiation from pass@k methodology
- Full benchmark results and ablation studies
- Acknowledged limitations

—is not included in the accessible content above. To obtain these specifics, you would need to access the full PDF or HTML version of the paper via the arXiv links provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54f8f8ef-82d3-47ef-b4fc-968a16568850",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "89b8e37f-2faa-42a5-a336-85a7b412578a",
  "sourceToolAssistantUUID": "54f8f8ef-82d3-47ef-b4fc-968a16568850",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T17:50:44.638Z_

<details><summary>↩ Tool result · `toolu_01Q9pkCFetRuhDMQKbam75Ln`</summary>

```text
Web search results for query: "HPT adaptive switching SFT RL rollout accuracy arXiv 2509.04419"

Links: [{"title":"Towards a Unified View of Large Language Model Post-Training","url":"https://arxiv.org/html/2509.04419"},{"title":"[2509.04419] Towards a Unified View of Large Language Model Post-Training","url":"https://arxiv.org/abs/2509.04419"},{"title":"Towards a Unified View of Large Language Model Post- ...","url":"https://arxiv.org/pdf/2509.04419"},{"title":"Unify Post-Training 2025-09-05","url":"https://arxiv.org/pdf/2509.04419v1"},{"title":"One-Token Rollout: Guiding Supervised Fine-Tuning of LLMs with Policy Gradient","url":"https://arxiv.org/html/2509.26313"},{"title":"PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost","url":"https://arxiv.org/pdf/2603.21383"},{"title":"Debunk the Myth of SFT Generalization","url":"https://arxiv.org/pdf/2510.00237"},{"title":"Beat the long tail: Distribution-Aware Speculative Decoding for RL Training","url":"https://arxiv.org/pdf/2511.13841"},{"title":"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead","url":"https://arxiv.org/pdf/2510.01624"}]

Based on the search results for arXiv 2509.04419, I found the paper you're looking for:

**"Towards a Unified View of Large Language Model Post-Training"**

The paper implements a simple instance of HPT (Hybrid Post-Training) which adaptively switches between SFT and RL based on rollout accuracy.

Key findings from the paper:

- The paper demonstrates that SFT and RL approaches are not contradictory but are instances of a single optimization process, deriving a Unified Policy Gradient Estimator that presents various post-training approaches as gradients of a common objective under different data distribution assumptions and bias-variance tradeoffs.

- HPT surpasses strong baselines such as SFT and demonstrates consistent performance across six mathematical reasoning benchmarks and two out-of-distribution suites, across models of varying scales and families.

- With Qwen2.5-Math-7B, HPT achieves a 7-point gain over strong baselines on AIME 2024, and also yields substantial improvements on smaller and weaker models like Qwen2.5-Math-1.5B and Llama3.1-8B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9558781-891e-4548-b4be-612d2b7b6fb0",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "ad01180d-5eda-49e8-8498-8c31fcec63ca",
  "sourceToolAssistantUUID": "a9558781-891e-4548-b4be-612d2b7b6fb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T17:50:44.702Z_

<details><summary>↩ Tool result · `toolu_01GZajgR9y8cmZLwdvgsziNS`</summary>

```text
Web search results for query: "HPT hybrid policy training language model SFT reinforcement learning switching"

Links: [{"title":"Towards a Unified View of Large Language Model Post-Training","url":"https://arxiv.org/html/2509.04419v1"},{"title":"[Literature Review] Towards a Unified View of Large Language Model Post-Training","url":"https://www.themoonlight.io/en/review/towards-a-unified-view-of-large-language-model-post-training"},{"title":"Paper page - Towards a Unified View of Large Language Model Post-Training","url":"https://huggingface.co/papers/2509.04419"},{"title":"Towards a Unified View of Large Language Model Post-Training | by Dixon | Medium","url":"https://medium.com/@huguosuo/towards-a-unified-view-of-large-language-model-post-training-0ec2557fa3a4"},{"title":"Towards a Unified View of Large Language Model Post- ...","url":"https://arxiv.org/pdf/2509.04419"},{"title":"[2509.04419] Towards a Unified View of Large Language Model Post-Training","url":"https://arxiv.org/abs/2509.04419"},{"title":"Towards a Unified View of Large Language Model Post-Training | OpenReview","url":"https://openreview.net/forum?id=3UxhlRCVgr"},{"title":"Towards a Unified View of Large Language Model Post-Training - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250904419L/abstract"},{"title":"Entropy-Gated Selective Policy Optimization:Token-Level Gradient Allocation for Hybrid Training of Large Language Models","url":"https://arxiv.org/pdf/2602.03309"}]

Based on the search results, I found comprehensive information about HPT (Hybrid Policy Training/Hybrid Post-Training):

## Overview

Hybrid Post-Training (HPT) is an algorithm that dynamically adapts between SFT for exploitation and RL for exploration based on real-time performance feedback.

## Theoretical Foundation

The paper shows that SFT and RL approaches are not in contradiction, but are instances of a single optimization process, with researchers deriving a Unified Policy Gradient Estimator that presents various post-training approaches as the gradient of a common objective under different data distribution assumptions and bias-variance tradeoffs.

## Key Mechanism

HPT uses a mixed loss combining SFT and RL terms and dynamically adjusts the weights of SFT vs. RL based on real-time performance feedback. More specifically, HPT dynamically adjusts the balance between SFT and RL, with SFT dominating early training for weaker models and RL increasing as competence grows, stabilizing at a low SFT contribution.

## Performance Results

HPT consistently surpasses strong baselines, including SFT, GRPO, sequential SFT→GRPO, and other mixed-policy methods like LUFFY and SRFT, across various model scales (Qwen2.5-Math-1.5B, Qwen2.5-Math-7B, Llama3.1-8B).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eb11d8e-0799-4c8a-9740-46af9eac72f0",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "b86e2227-0892-4ef7-be12-67fb5a4def15",
  "sourceToolAssistantUUID": "1eb11d8e-0799-4c8a-9740-46af9eac72f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T17:50:51.144Z_

<details><summary>↩ Tool result · `toolu_01VJgpGW5Bwk5ucSbnxqXFyr`</summary>

```text
# Summary of "Towards a Unified View of Large Language Model Post-Training"

## Overview
This paper proposes a unified framework for LLM post-training that combines Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), presenting an **adaptive switching mechanism called HPT (Hybrid Post-Training)**.

## Key Contribution: HPT Adaptive Switching

### The Core Mechanism
The paper introduces a method to dynamically switch between SFT and RL phases during post-training. Rather than treating these as separate sequential stages, HPT determines per-sample whether to apply SFT or RL based on model performance signals.

### Switching Metric
The adaptive switch is triggered by **pass@k performance**: samples where the model can generate correct solutions (i.e., "pass" at least one valid response within k attempts) transition from SFT to RL. As the authors note, once a model demonstrates capability on a task, "reinforcement learning can more effectively optimize behavior through reward signals."

### Per-Sample vs Per-Phase Decision
Critically, HPT operates at the **per-sample granularity** rather than global phase transitions. Each training example is individually assessed:
- **SFT applied when**: Model cannot reliably solve the task (fail@k scenario)
- **RL applied when**: Model demonstrates competency (pass@k scenario)

This contrasts with traditional pipelines applying SFT globally, then RL globally.

## Experimental Setup

The paper evaluates HPT on mathematical reasoning and coding benchmarks including:
- **MATH benchmark** (competition-level mathematics)
- **OlympiadBench** (olympiad-level problems)
- **NuminaMath** (diverse math problems)
- Code generation tasks

## Results Summary

### Key Findings
1. **Efficiency gains**: HPT achieves comparable performance to sequential SFT→RL pipelines using **fewer total training steps**

2. **Performance improvements**: On reasoning tasks, the adaptive mechanism yields measurable gains over fixed-phase training strategies

3. **Sample utilization**: By dynamically routing samples, HPT optimizes which training signal (learning-from-demonstration vs reward optimization) suits each example

### Comparison to Pass@K
The paper positions HPT as more nuanced than simple pass@k metrics for evaluation—it uses pass@k as a **training-time signal** for routing, not merely as a test-time metric. This allows continuous adaptation rather than static curriculum decisions.

## Technical Approach

**Algorithm structure**: 
- Compute model's pass rate on each training sample
- Route to SFT if fail@k (lacks basic capability)
- Route to RL if pass@k (can solve but needs optimization)
- Maintain separate loss functions and optimize jointly

## Limitations & Scope

The paper acknowledges:
- Evaluation primarily on math/code domains
- Computational overhead of per-sample routing decisions
- Dependency on reward signal quality for RL phases
- Limited analysis of hyperparameter sensitivity to switching thresholds

## Conclusion

HPT presents a principled alternative to treating post-training as sequential phases. By leveraging sample-level performance indicators to adaptively allocate SFT vs RL, the framework achieves "more efficient utilization of training compute while maintaining or improving solution quality."

The unifying perspective treats both SFT and RL as complementary optimization objectives rather than sequential pipeline stages, enabling fine-grained curriculum learning based on demonstrated model capability.

[Binary content (application/pdf, 995.5KB) also saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/048e6312-5e6d-4b84-a83d-11995bf4caaf/tool-results/webfetch-1779904237606-3hqr3a.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0c883bf-dbdc-419b-a96f-4baa767de566",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "ab6e0712-7268-4d17-8da7-6539d9994b56",
  "sourceToolAssistantUUID": "c0c883bf-dbdc-419b-a96f-4baa767de566",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-27T17:50:53.668Z_

Good, I have initial information. Let me now get the full HTML version of the paper for more detailed content, and also check the blog posts and reviews found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6e0712-7268-4d17-8da7-6539d9994b56",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVp55EDL9Kcpy5e4X9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c9e7ab6-5a5e-45a3-a82f-6d87a834ad36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7bQp5A8wBH3AsMTppqx3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1513,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 10135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1804,
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

_source line 17 · 2026-05-27T17:50:57.077Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PMqpb8ghCqFGhWVEARxcSN`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.04419",
  "prompt": "Extract the COMPLETE text of this paper, every section. I need: (1) the full method/algorithm description of HPT including equations, (2) exactly how the switching between SFT and RL works - per-sample or per-phase, what metric triggers it, (3) the exact algorithm pseudocode if any, (4) ALL experimental results including tables with numbers, (5) ALL ablation studies, (6) the limitations section, (7) how HPT relates to or differs from pass@k signals, (8) comparison to baselines like GRPO, LUFFY, SRFT. Include direct quotes from the paper wherever possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c9e7ab6-5a5e-45a3-a82f-6d87a834ad36",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVp55EDL9Kcpy5e4X9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f02efb50-c14a-43a5-9cd1-df474a1f9749",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7bQp5A8wBH3AsMTppqx3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1513,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 10135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1804,
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

_source line 18 · 2026-05-27T17:50:58.572Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011RH7qzCQHNrHMSBTPidH6K`</summary>

```json
{
  "url": "https://www.themoonlight.io/en/review/towards-a-unified-view-of-large-language-model-post-training",
  "prompt": "Extract all details about the HPT paper review. I need: the switching mechanism details, per-sample vs per-phase, the metric used, results, limitations, and any criticism or analysis of the approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f02efb50-c14a-43a5-9cd1-df474a1f9749",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVp55EDL9Kcpy5e4X9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "534f3c66-ac5f-4535-9f7b-3d69c8bb9e90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7bQp5A8wBH3AsMTppqx3c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1513,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 10135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1804,
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

_source line 19 · 2026-05-27T17:50:59.583Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017h6mReXtKixcPVtaYAQbkd`</summary>

```json
{
  "url": "https://medium.com/@huguosuo/towards-a-unified-view-of-large-language-model-post-training-0ec2557fa3a4",
  "prompt": "Extract all details about HPT (Hybrid Post-Training). I need: the switching mechanism, how it decides SFT vs RL per sample, the metric used, experimental results, and any analysis or criticism."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "534f3c66-ac5f-4535-9f7b-3d69c8bb9e90",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVp55EDL9Kcpy5e4X9z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa9e1648-df87-40aa-a90c-0115dfcf102f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q7bQp5A8wBH3AsMTppqx3c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1513,
      "cache_creation_input_tokens": 1804,
      "cache_read_input_tokens": 10135,
      "output_tokens": 517,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1804
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1513,
          "output_tokens": 517,
          "cache_read_input_tokens": 10135,
          "cache_creation_input_tokens": 1804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1804,
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

_source line 20 · 2026-05-27T17:51:04.442Z_

<details><summary>↩ Tool result · `toolu_011RH7qzCQHNrHMSBTPidH6K`</summary>

```text
# HPT (Hybrid Post-Training) Paper Analysis

## Switching Mechanism Details

HPT employs a **dynamic gating mechanism** that determines training signal selection. The approach uses a binary switch based on real-time model performance:

> "(α, β) = (0, 1), if P ≤ γ; (1, 0), if P > γ"

This creates two distinct operational modes: supervised fine-tuning when underperforming and reinforcement learning when competent.

## Granularity Level

The switching operates **per-question** rather than per-sample or per-phase. Performance metric *P* is computed as "the mean verification score of n on-policy trajectories generated by the current model" for each specific question encountered during training.

## Performance Metric

The system measures success through verification scores of generated trajectories. The authors demonstrate results across multiple mathematical reasoning benchmarks:

- AIME 2024, AIME 2025, AMC
- MATH-500, Minerva, OlympiadBench
- Out-of-distribution tests: ARC-c, GPQA

A notable achievement: "HPT achieved a 7-point gain over the strongest baseline on AIME 2024 with Qwen2.5-Math-7B."

## Key Results

HPT demonstrates:
- Superior large-k Pass@k scores, indicating expanded capability boundaries
- Strong exploitation on difficult problems while mitigating catastrophic forgetting
- Dynamic adjustment favoring SFT early in training, increasing RL as competence develops
- Maintained output entropy and preservation of long-form reasoning patterns

## Limitations & Critical Analysis

The paper identifies several constraints:

- **Threshold sensitivity**: "The optimal gate threshold γ is task- and model-dependent," requiring empirical tuning
- **Off-policy assumptions questioned**: "Off-policy RL for offline data may not be as crucial as direct SFT within the HPT framework"
- The approach inherently adds complexity through dynamic coefficient management, though specific computational overhead isn't detailed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "534f3c66-ac5f-4535-9f7b-3d69c8bb9e90",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "674a2b6e-6525-47f5-ac06-43dc7e37ab8b",
  "sourceToolAssistantUUID": "534f3c66-ac5f-4535-9f7b-3d69c8bb9e90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T17:51:04.702Z_

<details><summary>↩ Tool result · `toolu_017h6mReXtKixcPVtaYAQbkd`</summary>

```text
# Hybrid Post-Training (HPT) Details

## Switching Mechanism
The article describes HPT as using "a mixed loss combining SFT and RL terms" that "dynamically adjusts the weights of SFT vs. RL based on real-time performance feedback." However, specific technical details about the switching algorithm are not provided in this summary.

## Per-Sample Decision Logic
The document does not explain how HPT decides between SFT and RL on individual samples. It only mentions the overall strategy: the system "exploits SFT when the model is weak, then shifts to RL as the model grows stronger."

## Performance Metric
The content does not explicitly name which metric triggers the adaptive switching. It references "real-time performance feedback" without specifying whether this involves loss thresholds, benchmark scores, or other measurements.

## Experimental Results
HPT showed "consistent gains across multiple reasoning benchmarks, surpassing strong baselines like SFT→GRPO and LUFFY." Performance was "especially effective on mathematical reasoning tasks" and worked well even on smaller models like Qwen2.5–1.5B.

## Analysis or Criticism
The article identifies limitations: "The dynamic switching mechanism may require careful tuning for different domains" and notes the framework "currently focuses on text-based reasoning; multimodal post-training is a natural next step."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa9e1648-df87-40aa-a90c-0115dfcf102f",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "d09d40c5-3963-46e6-90eb-2f3c19f5ec38",
  "sourceToolAssistantUUID": "fa9e1648-df87-40aa-a90c-0115dfcf102f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T17:51:34.224Z_

<details><summary>↩ Tool result · `toolu_01PMqpb8ghCqFGhWVEARxcSN`</summary>

````text
# Summary: "Towards a Unified View of Large Language Model Post-Training"

## (1) Complete HPT Method Description

**Core Concept:**
The paper proposes Hybrid Post-Training (HPT), which "dynamically selects different training signals" by mixing SFT and RL losses based on real-time performance feedback.

**The Unified Policy Gradient Estimator (UPGE):**
The authors derive a unified framework:
```
grad_Uni = 𝟙_stable × (1/π_ref) × Â × ∇π_θ
```

This decomposes into four components:
- **Stabilization Mask** (𝟙_stable): Prevents gradient updates when policy diverges too much
- **Reference Policy Denominator** (π_ref): Token-level reweighting coefficient
- **Advantage Estimate** (Â): Sequence-level quality measure
- **Likelihood Gradient** (∇π_θ): Backpropagation of gradient information

**Common Objective (Equation 1):**
```
J_μ(θ) = E[r(τ|q)] - μKL(π_β(·|q) ∥ π_θ(·|q)), μ ≥ 0
```

Where the gradient decomposes into: "a reward + trust-region term sampled from π_θ and a data-adherence (SFT) term sampled from π_β."

## (2) Exact Switching Mechanism

**Per-Question Level Switching:**

The mechanism operates **per question**, not per phase. For each training question:

```
Performance P = (1/n) × Σ v(τ_i)  [from n=8 rollouts]
```

Where v(τ_i) ∈ {0,1} indicates correct answer.

**Binary Switch Functions (Equation 10):**
```
α = f(P) = {1 if P > γ,  0 if P ≤ γ}
β = g(P) = {1 if P ≤ γ,  0 if P > γ}
```

**Interpretation:** "When the model demonstrates strong capability, it is advantageous to emphasize on-policy RL to foster exploration; conversely, when the model's competence is limited, SFT should take precedence."

The gate threshold γ determines the switching point. Experiments use γ=0 for Qwen models (switch to SFT only when all 8 rollouts fail) and γ=2/8 for LLaMA.

## (3) Complete Algorithm Pseudocode

**Algorithm 1: Hybrid Post-Training (HPT)**

```
Input: Pretrained LLM π_θ, SFT dataset with trajectories τ*, 
       verifier v, n on-policy samples, T total steps

for t = 1 to T:
  for i = 1 to n:
    Sample trajectory τ_i ~ π_θ(·|q)
    Evaluate: v(τ_i) ← R(τ_i) ∈ {0,1}
  
  P ← (1/n)Σ v(τ_i)
  α ← f(P), β ← g(P)
  
  Compute L_RL using rollouts {τ_i}
  Compute L_SFT on trajectory τ*
  L ← α·L_RL + β·L_SFT
  
  θ ← θ - η∇_θL
```

**RL Loss (Dr. GRPO, Equation 11):**
```
L_RL = -(1/n)Σ_i Σ_t min(r_{i,t}·A_{i,t}, clip(r_{i,t}, 1-ε, 1+ε)·A_{i,t})
```

Where r_{i,t} is the per-token importance sampling ratio.

**SFT Loss (Equation 12):**
```
L_SFT = -(1/|τ*|) Σ_t log π_θ(τ*_t | q, τ*_{&lt;t})
```

## (4) Complete Experimental Results

**Main Results Table 2: Qwen2.5-Math-7B**

| Method | AIME24 | AIME25 | AMC | MATH-500 | Minerva | Olympiad | Avg |
|--------|--------|--------|-----|----------|---------|----------|-----|
| SFT | 25.1 | 22.8 | 56.1 | 84.2 | 33.8 | 44.7 | 44.5 |
| GRPO | 19.4 | 13.8 | 59.1 | 81.8 | 38.2 | 46.2 | 43.1 |
| SFT→GRPO | 25.7 | 21.6 | 62.2 | 84.6 | 38.2 | 46.8 | 46.5 |
| LUFFY | 26.1 | 21.8 | 66.2 | 88.4 | 41.9 | 54.1 | 49.8 |
| SRFT | 18.4 | 15.5 | 55.9 | 83.8 | 42.6 | 48.9 | 44.2 |
| **HPT** | **33.0** | **21.9** | **69.4** | **89.2** | **46.0** | **56.9** | **52.7** |

**Key Result:** "HPT achieves marked improvements over existing mixed-policy approaches such as LUFFY and SRFT, with particularly notable gains of 6.9 and 14.6 points on AIME 2024, respectively."

Out-of-Distribution Performance (same model):
- ARC-c: HPT 81.6 vs LUFFY 80.8
- GPQA: HPT 42.9 vs LUFFY 39.4
- OOD Average: HPT 62.3 vs LUFFY 60.1

**Table 3: Smaller Models**

LLaMA3.1-8B (Average across 6 benchmarks):
- LUFFY: 13.2
- **HPT: 18.2** (+37% improvement)

Qwen2.5-Math-1.5B:
- LUFFY: 34.7
- **HPT: 41.9** (+21% improvement)

## (5) Ablation Studies

**Table 5: Impact of Off-Policy RL**

Comparing different paradigms on Qwen2.5-Math-1.5B:

| Method | AIME24 | AIME25 | AMC | MATH-500 | Minerva | Olympiad | Avg |
|--------|--------|--------|-----|----------|---------|----------|-----|
| OFF/ON | 16.6 | 11.8 | 47.3 | 76.2 | 35.3 | 41.6 | 38.1 |
| Mix/ON | 16.7 | 17.2 | 46.9 | 79.4 | 37.5 | 43.9 | 40.3 |
| SFT/ON (HPT) | 16.6 | 17.8 | 51.0 | 81.0 | 37.5 | 47.3 | 41.9 |

Conclusion: "The SFT/ON method achieves the best average performance (41.9), outperforming both Mix/ON (40.3) and OFF/ON (38.1). This suggests that off-policy RL may not be essential, as SFT already serves effectively."

**Table 6: Gate Threshold Ablation (γ parameter)**

| γ | AIME24 | AIME25 | AMC | MATH-500 | Minerva | Olympiad | Avg |
|---|--------|--------|-----|----------|---------|----------|-----|
| 2/8 | 15.8 | 13.0 | 49.0 | 77.6 | 34.6 | 44.1 | 39.0 |
| 1/8 | 18.1 | 14.2 | 46.0 | 75.4 | 35.7 | 42.5 | 38.7 |
| **0** | **16.6** | **17.8** | **51.0** | **81.0** | **37.5** | **47.3** | **41.9** |

Finding: "γ=0 achieves the best overall performance with an average score of 41.9...maintaining a dynamic balance between the exploration of RL and the exploitation of SFT" is crucial.

**Section 4.5 Analysis:**
Figure 8 shows that higher γ increases SFT usage but doesn't necessarily improve performance, indicating the optimal switching rate depends on base model capability.

## (6) Limitations Section

The paper lacks an explicit "Limitations" section. However, several constraints emerge:

1. **Simplistic gating mechanism:** The authors note their "highly streamlined experimental setup" uses binary switches rather than continuous weighting.

2. **Model-specific tuning required:** "The optimal degree of this gating mechanism should be adjusted according to the characteristics of the base model and the specific training data employed."

3. **Limited theoretical justification for offline data:** "Neither of the two approaches is entirely theoretically justified, from an RL perspective; both require a lower bound on the state-action visitation...which can not be satisfied due to the severely limited datasets in practice."

4. **Computational cost not detailed:** While claiming efficiency improvements over SFT→GRPO, explicit computational measurements are absent.

## (7) Relationship to Pass@k Signals

**Section 4.1 - Exploration Analysis:**

The authors evaluate Pass@k up to 1024 samples per problem. Key finding: "HPT achieves the highest large-k Pass@k performance overall. This indicates that Hybrid Post-Training not only delivers substantial improvements in Pass@1, but also maximally preserves and enhances the model's exploratory ability."

**Critical Observation:**
The paper contrasts with "Limit-of-RLVR" work: "While RLVR training yields a significant improvement in Pass@1, it does not lead to gains in large-k Pass@k." HPT breaks this pattern by maintaining high Pass@k despite specializing on Pass@1 via the RL component.

**Figure 2 Results:**
On AIME25, AIME24, and AMC:
- GRPO shows lower Pass@k expansion
- SFT shows better Pass@k but lower Pass@1
- HPT achieves superior performance across both metrics

This suggests: "methods incorporating SFT achieve higher large-k Pass@k compared to the GRPO (purely RL). This may be attributed to the introduction of data outside the model's own distribution during SFT, which increases output uncertainty while also providing new knowledge from offline data."

## (8) Comparison to Baseline Methods

### vs. GRPO (Pure On-Policy RL)

**Strengths of HPT:**
- Qwen2.5-Math-7B AIME24: HPT 33.0 vs GRPO 19.4 (+70%)
- Provides stable initialization via SFT when RL exploration fails
- Maintains higher entropy throughout training (Figure 7)

**GRPO Weakness:** "GRPO frequently produces dense white regions...dense error regions, reflecting widespread rollout errors across outputs. This illustrates a core limitation of RL methods: they struggle to learn effectively when frequent rollout errors occur."

### vs. LUFFY (Mixed-Policy Baseline)

**Key Difference:** LUFFY uses "fixed coefficient, a predefined schedule, a dynamic adjustment based on entropy, or a learnable parameter" whereas HPT uses "performance feedback on question[s]."

**Performance Gap:**
- AIME24: HPT 33.0 vs LUFFY 26.1 (+27%)
- Average across 6 benchmarks: HPT 52.7 vs LUFFY 49.8 (+5.8%)
- Out-of-distribution: HPT 62.3 vs LUFFY 60.1

**Mechanism Difference:** LUFFY mixes losses at task level with fixed weighting. HPT "dynamically selects different training signals" per question based on immediate performance.

### vs. SRFT (Offline-First)

**Results:**
- AIME24: HPT 33.0 vs SRFT 18.4 (+79%)
- Average: HPT 52.7 vs SRFT 44.2 (+19%)

**Conceptual Difference:** "SRFT... integrates SFT or SFT-style imitation learning losses directly with RL objectives" using offline data primarily. HPT dynamically balances based on online performance rather than pre-computed offline advantages.

### vs. SFT→GRPO (Sequential Two-Stage)

**Practical Advantage:** "HPT also yields substantial improvements even on relatively smaller and weaker models...achieves marked improvements over existing mixed-policy approaches...surpasses SFT→GRPO, which requires substantially higher computational cost."

**Training Visualization (Section 4.2):**
Figure 4 demonstrates that despite SFT→GRPO having an unfair advantage (pre-SFT training), HPT "consistently outperforms SFT→GRPO by substantially enhancing learning performance on the training set."

### Zero-RL Comparisons (Table 2)

| Method | AIME24 |
|--------|--------|
| SimpleRL-Zero | 27.0 |
| OpenReasoner-Zero | 16.5 |
| Oat-Zero | 33.4 |
| **HPT** | **33.0** |

HPT achieves competitive performance with Zero-RL approaches while providing more principled integration of supervised data.

---

## Key Innovation Summary

HPT's core contribution is the **per-question adaptive switching** mechanism:
- When rollout performance P ≤ γ: emphasize SFT (exploitation)
- When rollout performance P > γ: emphasize RL (exploration)

This "intrinsically adaptive" approach outperforms fixed-coefficient methods because it responds to individual question difficulty rather than applying uniform mixing across all training examples.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f02efb50-c14a-43a5-9cd1-df474a1f9749",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "651da581-e690-4515-a82e-5958d70df665",
  "sourceToolAssistantUUID": "f02efb50-c14a-43a5-9cd1-df474a1f9749",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-27T17:51:37.458Z_

Now let me get one more critical piece -- the OpenReview discussion and the HuggingFace paper page to see if there are any reviewer comments or community discussions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "651da581-e690-4515-a82e-5958d70df665",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVsFEWFmoAU2amA5FaC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8fb4345-aef8-42dc-b128-418257870ff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ivnc4Vq1bzWNPauAfwu9v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 818,
      "cache_creation_input_tokens": 5693,
      "cache_read_input_tokens": 11939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5693,
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

_source line 24 · 2026-05-27T17:51:39.288Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Li9qkYYddM15c36LGSq4JK`</summary>

```json
{
  "url": "https://openreview.net/forum?id=3UxhlRCVgr",
  "prompt": "Extract all reviewer comments, scores, and discussion about this HPT paper. I need: reviewer critiques, strengths/weaknesses identified, any questions about the switching mechanism, and the overall decision. Include direct quotes from reviewers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8fb4345-aef8-42dc-b128-418257870ff1",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVsFEWFmoAU2amA5FaC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cdbe2471-2867-4c48-aaec-451677c94a7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ivnc4Vq1bzWNPauAfwu9v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 818,
      "cache_creation_input_tokens": 5693,
      "cache_read_input_tokens": 11939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5693,
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

_source line 25 · 2026-05-27T17:51:40.341Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NcH2DwoJJESmSReF3KKt29`</summary>

```json
{
  "url": "https://huggingface.co/papers/2509.04419",
  "prompt": "Extract all comments, discussions, and community reactions about this HPT paper. Include any criticism or praise."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdbe2471-2867-4c48-aaec-451677c94a7f",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVsFEWFmoAU2amA5FaC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aee8247b-c17e-48d7-a320-86b8a8205e87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ivnc4Vq1bzWNPauAfwu9v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 818,
      "cache_creation_input_tokens": 5693,
      "cache_read_input_tokens": 11939,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5693
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 818,
          "output_tokens": 260,
          "cache_read_input_tokens": 11939,
          "cache_creation_input_tokens": 5693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5693,
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

_source line 26 · 2026-05-27T17:51:43.650Z_

<details><summary>↩ Tool result · `toolu_01Li9qkYYddM15c36LGSq4JK`</summary>

```text
# Review Information Not Available

Based on the webpage content provided, I cannot extract reviewer comments, scores, or discussion details about this paper. 

The page shows only the paper's metadata:
- **Title:** "Towards a Unified View of Large Language Model Post-Training"
- **Status:** "Desk Rejected Submission" (ICLR 2026)
- **Key contribution:** The Unified Policy Gradient Estimator (UPGE) framework and Hybrid Post-Training (HPT) algorithm

However, the actual reviewer feedback, critiques, scoring, and discussion are **not displayed** on this landing page. To access this information, you would need to:

1. Log into OpenReview.net
2. Navigate to the full submission page
3. Check the "Revisions" tab (linked on the page)
4. Review the decision letters and reviewer reports

The desk rejection status indicates the paper was rejected at the initial editorial stage, likely before full peer review, which may explain why detailed reviewer comments aren't present on this public-facing version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdbe2471-2867-4c48-aaec-451677c94a7f",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "ed9dfc6f-9ed8-4b6b-bb0d-8e4d8e3a8a94",
  "sourceToolAssistantUUID": "cdbe2471-2867-4c48-aaec-451677c94a7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T17:51:47.175Z_

<details><summary>↩ Tool result · `toolu_01NcH2DwoJJESmSReF3KKt29`</summary>

```text
# Comments, Discussions, and Community Reactions to the HPT Paper

Based on the provided web page content, I cannot find explicit comments, discussions, or community reactions embedded within the paper itself. The document is a formal academic paper published on arXiv (https://arxiv.org/html/2509.04419), and it does not contain a comments section, discussion forum, or community feedback.

## What the Paper Does Contain:

**Peer Review and Validation Elements:**
- Extensive experimental validation across multiple benchmarks (AIME 2024/2025, AMC, MATH-500, Minerva, OlympiadBench, GPQA, ARC-c)
- Ablation studies and empirical analysis sections (Section 5)
- Comparisons against multiple strong baselines (SFT, GRPO, LUFFY, SRFT, SRFT, and Zero-RL variants)

**Key Findings That Would Generate Discussion:**
1. **Performance Gains**: HPT achieves a 7-point improvement over SFT→GRPO on AIME 2024 with Qwen2.5-Math-7B (33.0% vs 25.7%)
2. **Theoretical Contribution**: The Unified Policy Gradient Estimator framework showing SFT and RL optimize a common objective
3. **Novel Finding**: HPT maintains higher Pass@k performance than pure RL methods, suggesting enhanced exploration capacity
4. **Simplicity**: Despite a "highly streamlined experimental setup" with binary gating, it outperforms more complex methods

## To Find Community Reactions:

You would need to check:
- **ArXiv discussions** or comment sections
- **GitHub repository**: https://github.com/TsinghuaC3I/Unify-Post-Training
- **Twitter/X** discussions from the authors
- **Research forums** (e.g., Papers with Code, Hugging Face discussions)
- **Academic social media** platforms
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aee8247b-c17e-48d7-a320-86b8a8205e87",
  "isSidechain": true,
  "promptId": "81938832-294a-4147-b0ab-ad0ff816bfdb",
  "agentId": "a86d91baac7cc3ad6",
  "type": "user",
  "uuid": "a3154851-26d6-4b8d-b127-55247929f41f",
  "sourceToolAssistantUUID": "aee8247b-c17e-48d7-a320-86b8a8205e87",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-27T17:52:40.432Z_

I now have comprehensive information. Let me compile the detailed research report.

---

## Detailed Research Report: HPT (Hybrid Post-Training)

**Paper:** "Towards a Unified View of Large Language Model Post-Training"
**ArXiv:** 2509.04419 (September 2025, revised January 2026)
**Authors:** Xingtai Lv, Yuxin Zuo, Youbang Sun, Hongyi Liu, Yuntian Wei, Zhekai Chen, Xuekai Zhu, Kaiyan Zhang, Bingning Wang, Ning Ding, Bowen Zhou (Tsinghua University C3I group)
**Status:** Desk-rejected at ICLR 2026 (per OpenReview)
**Code:** https://github.com/TsinghuaC3I/Unify-Post-Training

---

### 1. Theoretical Foundation: The Unified Policy Gradient Estimator

HPT rests on a theoretical contribution showing that SFT and RL are not contradictory approaches but instances of a single optimization process. The authors derive a **Unified Policy Gradient Estimator (UPGE)** that decomposes into four components: a stabilization mask, a reference policy denominator, an advantage estimate, and a likelihood gradient. The common objective is:

```
J_mu(theta) = E[r(tau|q)] - mu * KL(pi_beta(.|q) || pi_theta(.|q)),  mu >= 0
```

The gradient of this objective decomposes into "a reward + trust-region term sampled from pi_theta and a data-adherence (SFT) term sampled from pi_beta." This theoretical unification is what motivates the practical HPT algorithm.

---

### 2. HPT's Switching Mechanism: Per-Question, Not Per-Phase

This is the most critical finding for your research idea revision. **HPT operates at per-question granularity, not per-phase.** For each training question `q`, the algorithm:

1. Generates `n=8` on-policy rollouts from the current model
2. Computes a performance score: `P = (1/n) * sum(v(tau_i))` where `v(tau_i) in {0, 1}` indicates whether each rollout produced a correct answer
3. Applies a **binary gate** based on threshold gamma:

```
alpha = f(P) = { 1 if P > gamma,  0 if P <= gamma }   (RL weight)
beta  = g(P) = { 1 if P <= gamma,  0 if P > gamma }   (SFT weight)
```

The combined loss is: `L = alpha * L_RL + beta * L_SFT`

The authors state: "When the model demonstrates strong capability, it is advantageous to emphasize on-policy RL to foster exploration; conversely, when the model's competence is limited, SFT should take precedence."

**Key design choice:** The gate is binary (hard switching), not a soft mixture. For any given question at any given training step, the model receives EITHER SFT signal OR RL signal, never both simultaneously. The threshold gamma is model-dependent: gamma=0 for Qwen models (SFT only when ALL 8 rollouts fail) and gamma=2/8 for LLaMA.

---

### 3. How HPT Differs from Pass@k-Based Signals

HPT uses rollout accuracy (essentially a pass@8 computation) as a **training-time routing signal**, not merely as an evaluation metric. The key distinctions:

- **Pass@k as evaluation** measures capability breadth post-training. HPT uses the same computation **during training** to decide which gradient signal to apply.
- **HPT preserves Pass@k better than pure RL.** The authors find: "HPT achieves the highest large-k Pass@k performance overall. This indicates that Hybrid Post-Training not only delivers substantial improvements in Pass@1, but also maximally preserves and enhances the model's exploratory ability." They contrast this with RLVR findings: "While RLVR training yields a significant improvement in Pass@1, it does not lead to gains in large-k Pass@k."
- **The signal is binary, not granular.** Unlike approaches that might weight by pass@k rate, HPT collapses the signal to a binary SFT-or-RL decision. This is simpler but coarser than, say, weighting the SFT loss proportionally to (1 - pass_rate).

---

### 4. Comparison to Baselines

**On Qwen2.5-Math-7B (6-benchmark average):**

| Method | Average | AIME24 |
|---|---|---|
| SFT | 44.5 | 25.1 |
| GRPO (pure RL) | 43.1 | 19.4 |
| SFT then GRPO | 46.5 | 25.7 |
| LUFFY | 49.8 | 26.1 |
| SRFT | 44.2 | 18.4 |
| **HPT** | **52.7** | **33.0** |

HPT achieves "marked improvements over existing mixed-policy approaches such as LUFFY and SRFT, with particularly notable gains of 6.9 and 14.6 points on AIME 2024, respectively."

**On weaker/smaller models**, HPT's advantage is even more pronounced:
- LLaMA3.1-8B: HPT 18.2 vs LUFFY 13.2 (average, +37%)
- Qwen2.5-Math-1.5B: HPT 41.9 vs LUFFY 34.7 (+21%)

**Out-of-distribution** (ARC-c, GPQA): HPT 62.3 vs LUFFY 60.1, showing generalization holds.

**Key mechanism difference vs. LUFFY:** LUFFY uses "fixed coefficient, a predefined schedule, a dynamic adjustment based on entropy, or a learnable parameter" whereas HPT uses "performance feedback on questions" -- i.e., LUFFY's mixing is not conditioned on per-question difficulty.

---

### 5. Ablation Findings

**Gate threshold (gamma):** On Qwen2.5-Math-1.5B, gamma=0 (SFT only when all rollouts fail) achieves the best average of 41.9, compared to gamma=1/8 (38.7) and gamma=2/8 (39.0). This means very aggressive RL usage is preferred when the model has any capability on a question.

**Off-policy RL vs SFT for low-accuracy questions:** The paper tested replacing SFT with off-policy RL for questions where rollouts fail. Result: "The SFT/ON method achieves the best average performance (41.9), outperforming both Mix/ON (40.3) and OFF/ON (38.1). This suggests that off-policy RL may not be essential, as SFT already serves effectively."

**Training dynamics (Figure 4):** HPT's SFT proportion starts high and decreases over training as the model becomes more capable. The authors note this creates "a dynamic balance between the exploration of RL and the exploitation of SFT."

---

### 6. Limitations

The paper lacks a formal limitations section, but several emerge:

1. **Binary gating is simplistic.** The authors themselves call it a "highly streamlined experimental setup." A continuous weighting by rollout accuracy might capture more nuance.

2. **Threshold requires per-model tuning.** "The optimal degree of this gating mechanism should be adjusted according to the characteristics of the base model and the specific training data employed." Gamma=0 works for Qwen but gamma=2/8 for LLaMA.

3. **Theoretical gap for offline data.** "Neither of the two approaches is entirely theoretically justified, from an RL perspective; both require a lower bound on the state-action visitation...which can not be satisfied due to the severely limited datasets in practice."

4. **Domain-limited evaluation.** All experiments are on mathematical reasoning. The authors note "multimodal post-training is a natural next step."

5. **Computational overhead not quantified.** Each training step requires n=8 rollouts for routing, but the paper does not detail wall-clock comparisons.

6. **Desk-rejected at ICLR 2026**, suggesting reviewers/editors found significant issues (though specific reviewer comments are not publicly available).

---

### 7. Key Takeaways for Your Research Idea Revision

- HPT's switching is **per-question, binary, based on rollout accuracy (pass@8 > gamma)**. It is not a phase-level switch.
- The mechanism is extremely simple: if any rollout succeeds (gamma=0), do RL; if all fail, do SFT. This simplicity is both a strength (easy to implement) and a limitation (no nuanced weighting).
- HPT does NOT use a continuous pass@k rate as a mixing weight -- it collapses to a binary decision. There is room for more sophisticated approaches.
- The idea that SFT is better for "too-hard" questions and RL for "learnable" ones is well-supported by HPT's results but not novel to HPT alone (similar intuitions appear in curriculum RL literature).
- HPT's strongest results are on small/weak models where pure RL struggles most -- this is where the SFT fallback provides the biggest lift.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2509.04419)
- [arXiv HTML full paper](https://arxiv.org/html/2509.04419)
- [arXiv PDF](https://arxiv.org/pdf/2509.04419)
- [OpenReview submission](https://openreview.net/forum?id=3UxhlRCVgr)
- [Moonlight review](https://www.themoonlight.io/en/review/towards-a-unified-view-of-large-language-model-post-training)
- [Medium summary](https://medium.com/@huguosuo/towards-a-unified-view-of-large-language-model-post-training-0ec2557fa3a4)
- [HuggingFace paper page](https://huggingface.co/papers/2509.04419)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3154851-26d6-4b8d-b127-55247929f41f",
  "isSidechain": true,
  "agentId": "a86d91baac7cc3ad6",
  "requestId": "req_011CbTVtCcXDTW8nqDFVUUsw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9976eed9-1b97-473d-8f33-45a299224813",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "048e6312-5e6d-4b84-a83d-11995bf4caaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjL4NS65bYANM6wt2rmemC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1821,
      "cache_read_input_tokens": 17632,
      "output_tokens": 2495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2495,
          "cache_read_input_tokens": 17632,
          "cache_creation_input_tokens": 1821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1821,
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
