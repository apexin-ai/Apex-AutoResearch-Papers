# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/ae85f63b-06b5-4781-b92e-92dc801697c7.jsonl`
- **Structured JSON:** [`6f6a326ecf75b1fa46e2.json`](../../sessions/6f/6f6a326ecf75b1fa46e2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T15:48:51.860Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T15:48:51.860Z",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Synthetic Data and Self-Improvement for Mathematical Reasoning Training**\n\n## Paper to analyze\n\n{\n  \"title\": \"Process Reinforcement through Implicit Rewards (PRIME)\",\n  \"authors\": \"Cui et al.\",\n  \"venue\": \"ICLR 2025\",\n  \"url\": \"https://arxiv.org/abs/2502.01456\",\n  \"why_important\": \"ICLR 2025 paper; solved the key problem of online PRM training without expensive process labels; Eurus-2-7B-PRIME matches Qwen2.5-Math-7B-Instruct with 10% of its data\",\n  \"one_line_summary\": \"Introduces implicit process rewards derived from outcome labels to enable scalable online process reward model training, achieving 15.1% average improvement on reasoning benchmarks.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T15:48:51.863Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T15:48:51.863Z",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

## Round 1

73 recorded events

### User

_source line 3 · 2026-05-27T15:48:51.897Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Synthetic Data and Self-Improvement for Mathematical Reasoning Training**

## Paper to analyze

{
  "title": "Process Reinforcement through Implicit Rewards (PRIME)",
  "authors": "Cui et al.",
  "venue": "ICLR 2025",
  "url": "https://arxiv.org/abs/2502.01456",
  "why_important": "ICLR 2025 paper; solved the key problem of online PRM training without expensive process labels; Eurus-2-7B-PRIME matches Qwen2.5-Math-7B-Instruct with 10% of its data",
  "one_line_summary": "Introduces implicit process rewards derived from outcome labels to enable scalable online process reward model training, achieving 15.1% average improvement on reasoning benchmarks."
}

## Instructions

1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.

2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:
   - What gap did they identify and HOW did they find it?
   - What was the key insight that others missed?
   - How did they formulate the problem differently from prior work?
   - What existing technique did they adapt/combine/simplify?

3. **Learn from reviewers**: If you can find reviewer comments, extract:
   - What did reviewers praise most?
   - What concerns were raised and how were they addressed?
   - What would have made this paper even stronger?

## Output format

Output a single JSON object:
{
  "title": "Paper title",
  "venue": "Where published",
  "problem_identification": "What gap/problem did they identify? How did they find it? (2-3 sentences)",
  "key_insight": "The core intellectual contribution — the aha moment (1-2 sentences)",
  "innovation_type": "new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis",
  "method_summary": "Technical approach in 3-5 sentences — enough to understand the machinery",
  "what_makes_it_good": "Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)",
  "limitations_acknowledged": "What gaps did the authors themselves identify? (1-2 sentences)",
  "open_questions": "What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)",
  "building_blocks": ["List of methods/tools/datasets used that could be reused"],
  "reviewer_feedback_summary": "If found on OpenReview: key praise and concerns. Otherwise: null",
  "relevance_to_seed": "How does this paper relate to our research area? What can we learn from it? (1-2 sentences)"
}

Be analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "b2b15cfd-2565-42c5-a500-98e6d37cbf4e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T15:48:51.896Z_

```json
{
  "parentUuid": "b2b15cfd-2565-42c5-a500-98e6d37cbf4e",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "3d15eb05-ce41-47d4-9814-a91aa7be839f",
  "timestamp": "2026-05-27T15:48:51.896Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T15:48:51.896Z_

```json
{
  "parentUuid": "3d15eb05-ce41-47d4-9814-a91aa7be839f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cf3cceee-8c58-4028-95bc-ec01c093ba9f",
  "timestamp": "2026-05-27T15:48:51.896Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRIME paper on implicit process rewards",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Assistant

_source line 7 · 2026-05-27T15:48:54.665Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the PRIME paper (Process Reinforcement through Implicit Rewards) by fetching it from arXiv and potentially OpenReview for ICLR 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf3cceee-8c58-4028-95bc-ec01c093ba9f",
  "isSidechain": false,
  "requestId": "req_011CbTLWZAsT7FbzQzRsLTmr",
  "type": "assistant",
  "uuid": "215ae338-88d4-4023-8626-a1e093a4a58c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcjvDvovho5HZD9PXqgb4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2186,
      "cache_read_input_tokens": 11014,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 154,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2186
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

### Assistant

_source line 8 · 2026-05-27T15:48:55.404Z_

I'll fetch the paper from arXiv and also check OpenReview for reviewer comments in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "215ae338-88d4-4023-8626-a1e093a4a58c",
  "isSidechain": false,
  "requestId": "req_011CbTLWZAsT7FbzQzRsLTmr",
  "type": "assistant",
  "uuid": "48c75700-f979-4cab-89a6-b1455f785214",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcjvDvovho5HZD9PXqgb4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2186,
      "cache_read_input_tokens": 11014,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 154,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2186
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

### Tool call

_source line 9 · 2026-05-27T15:48:55.753Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012m4yR2ZzjXwLjh2ouVwe1b`</summary>

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
  "parentUuid": "48c75700-f979-4cab-89a6-b1455f785214",
  "isSidechain": false,
  "requestId": "req_011CbTLWZAsT7FbzQzRsLTmr",
  "type": "assistant",
  "uuid": "90e220a0-f89f-401c-8ea8-eb3ab0d5b426",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcjvDvovho5HZD9PXqgb4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2186,
      "cache_read_input_tokens": 11014,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2186,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 154,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2186,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2186
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

_source line 10 · 2026-05-27T15:48:55.760Z_

<details><summary>↩ Tool result · `toolu_012m4yR2ZzjXwLjh2ouVwe1b`</summary>

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
  "parentUuid": "90e220a0-f89f-401c-8ea8-eb3ab0d5b426",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "8611a96a-ca9e-4741-899a-89bf6243df43",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "90e220a0-f89f-401c-8ea8-eb3ab0d5b426",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T15:48:57.799Z_

Now let me fetch the paper from arXiv and search for it on OpenReview in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8611a96a-ca9e-4741-899a-89bf6243df43",
  "isSidechain": false,
  "requestId": "req_011CbTLWq3MNKFQwSHAtCixQ",
  "type": "assistant",
  "uuid": "73b48c8f-f46a-41f8-ace4-591e9d0b9c8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEborTgLj8Mudd6bGmwL2d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 13200,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 13200,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

### Tool call

_source line 12 · 2026-05-27T15:48:59.207Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L3nHK7zM1QgN4y9EeTfQ7o`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.01456",
  "prompt": "Extract the full abstract, introduction, and any high-level description of the method from this paper page. Include all details about the paper's contributions, motivation, and approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73b48c8f-f46a-41f8-ace4-591e9d0b9c8d",
  "isSidechain": false,
  "requestId": "req_011CbTLWq3MNKFQwSHAtCixQ",
  "type": "assistant",
  "uuid": "08e34cf2-8fe8-49d4-81a3-0ef7a1b4b69f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEborTgLj8Mudd6bGmwL2d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 13200,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 13200,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

### Tool call

_source line 13 · 2026-05-27T15:49:01.071Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AacgsE1wXr9fxaru4HypvP`</summary>

```json
{
  "url": "https://openreview.net/search?term=Process+Reinforcement+through+Implicit+Rewards+PRIME&venue=ICLR+2025",
  "prompt": "Find the OpenReview page for the paper \"Process Reinforcement through Implicit Rewards\" (PRIME) at ICLR 2025. Return the URL/link to the paper's forum page if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08e34cf2-8fe8-49d4-81a3-0ef7a1b4b69f",
  "isSidechain": false,
  "requestId": "req_011CbTLWq3MNKFQwSHAtCixQ",
  "type": "assistant",
  "uuid": "b30ae080-dc8d-455e-a2eb-58f4c3f42fc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JEborTgLj8Mudd6bGmwL2d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 13200,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 274,
          "cache_read_input_tokens": 13200,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

_source line 14 · 2026-05-27T15:49:03.570Z_

<details><summary>↩ Tool result · `toolu_01AacgsE1wXr9fxaru4HypvP`</summary>

```text
Based on the web page content provided, I cannot find a direct link to the paper "Process Reinforcement through Implicit Rewards" (PRIME) at ICLR 2025. 

The page shown is the OpenReview homepage, which displays navigation elements and general information about the platform. It states that "OpenReview is a long-term project to advance science through improved peer review," but does not contain search results or specific paper links.

To locate this paper, you would need to:
1. Use the search function on OpenReview.net
2. Navigate to the ICLR 2025 venue page via "All Venues"
3. Search directly for the paper title or authors

I cannot provide the specific paper URL based solely on this homepage content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b30ae080-dc8d-455e-a2eb-58f4c3f42fc5",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "6a53a44c-0e89-4ba0-9fb6-4716b92763b7",
  "toolUseResult": {
    "bytes": 62436,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find a direct link to the paper \"Process Reinforcement through Implicit Rewards\" (PRIME) at ICLR 2025. \n\nThe page shown is the OpenReview homepage, which displays navigation elements and general information about the platform. It states that \"OpenReview is a long-term project to advance science through improved peer review,\" but does not contain search results or specific paper links.\n\nTo locate this paper, you would need to:\n1. Use the search function on OpenReview.net\n2. Navigate to the ICLR 2025 venue page via \"All Venues\"\n3. Search directly for the paper title or authors\n\nI cannot provide the specific paper URL based solely on this homepage content.",
    "durationMs": 2496,
    "url": "https://openreview.net/search?term=Process+Reinforcement+through+Implicit+Rewards+PRIME&venue=ICLR+2025"
  },
  "sourceToolAssistantUUID": "b30ae080-dc8d-455e-a2eb-58f4c3f42fc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T15:49:05.011Z_

<details><summary>↩ Tool result · `toolu_01L3nHK7zM1QgN4y9EeTfQ7o`</summary>

```text
# Paper Summary: Process Reinforcement through Implicit Rewards

## Abstract
The paper addresses a key challenge in reinforcement learning for large language models: while dense process rewards improve inference-time scaling for complex reasoning tasks, training process reward models (PRMs) online remains difficult due to expensive process labeling and reward hacking vulnerabilities.

The authors propose **PRIME** (Process Reinforcement through IMplicit rEwards), which "enables online PRM updates using only policy rollouts and outcome labels through implicit process rewards." This approach eliminates the need for dedicated reward model training, reducing development overhead while maintaining compatibility with various advantage functions.

## Key Contributions

**Research Impact:**
- Demonstrates 15.1% average improvement across reasoning benchmarks when applied to Qwen2.5-Math-7B-Base
- Their model (Eurus-2-7B-PRIME) surpasses Qwen2.5-Math-7B-Instruct on seven benchmarks "with 10% of its training data"

**Technical Innovation:**
The method leverages implicit process rewards derived from policy rollouts and outcome labels, bypassing the traditional requirement for expensive process-level annotations. This substantially reduces the practical barriers to implementing process-based reinforcement learning.

## Availability
Code, model weights, and training data are publicly available on GitHub at the project repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08e34cf2-8fe8-49d4-81a3-0ef7a1b4b69f",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "c1800ed2-3740-4107-a232-563bc1a820cc",
  "toolUseResult": {
    "bytes": 51425,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Process Reinforcement through Implicit Rewards\n\n## Abstract\nThe paper addresses a key challenge in reinforcement learning for large language models: while dense process rewards improve inference-time scaling for complex reasoning tasks, training process reward models (PRMs) online remains difficult due to expensive process labeling and reward hacking vulnerabilities.\n\nThe authors propose **PRIME** (Process Reinforcement through IMplicit rEwards), which \"enables online PRM updates using only policy rollouts and outcome labels through implicit process rewards.\" This approach eliminates the need for dedicated reward model training, reducing development overhead while maintaining compatibility with various advantage functions.\n\n## Key Contributions\n\n**Research Impact:**\n- Demonstrates 15.1% average improvement across reasoning benchmarks when applied to Qwen2.5-Math-7B-Base\n- Their model (Eurus-2-7B-PRIME) surpasses Qwen2.5-Math-7B-Instruct on seven benchmarks \"with 10% of its training data\"\n\n**Technical Innovation:**\nThe method leverages implicit process rewards derived from policy rollouts and outcome labels, bypassing the traditional requirement for expensive process-level annotations. This substantially reduces the practical barriers to implementing process-based reinforcement learning.\n\n## Availability\nCode, model weights, and training data are publicly available on GitHub at the project repository.",
    "durationMs": 5799,
    "url": "https://arxiv.org/abs/2502.01456"
  },
  "sourceToolAssistantUUID": "08e34cf2-8fe8-49d4-81a3-0ef7a1b4b69f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T15:49:08.690Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LyDmmQWerse24z232E4K5V`</summary>

```json
{
  "url": "https://openreview.net/search?query=Process+Reinforcement+through+Implicit+Rewards&source=forum&group=ICLR.cc%2F2025%2FConference",
  "prompt": "Find the OpenReview forum URL/link for the paper \"Process Reinforcement through Implicit Rewards\" (PRIME) at ICLR 2025. Return any forum links or paper IDs you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1800ed2-3740-4107-a232-563bc1a820cc",
  "isSidechain": false,
  "requestId": "req_011CbTLXWEY8fbeaeKaXvmnz",
  "type": "assistant",
  "uuid": "4e5d6051-dfd7-4eed-b587-40fb45dd40c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrNUoSFsRL6sXc9ooHtEyB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 199,
      "cache_creation_input_tokens": 601,
      "cache_read_input_tokens": 13874,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 199,
          "output_tokens": 330,
          "cache_read_input_tokens": 13874,
          "cache_creation_input_tokens": 601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 601
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

_source line 17 · 2026-05-27T15:49:10.875Z_

<details><summary>↩ Tool result · `toolu_01LyDmmQWerse24z232E4K5V`</summary>

```text
Based on the web page content provided, I cannot find a forum URL or paper ID for "Process Reinforcement through Implicit Rewards" (PRIME) at ICLR 2025.

The page shown is OpenReview's search error page, which displays: "Error: Missing search term or query" along with navigation links and footer information. The content does not include any specific paper details or forum links.

To locate this paper, you would need to perform an actual search on OpenReview.net or navigate directly to the ICLR 2025 venue page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e5d6051-dfd7-4eed-b587-40fb45dd40c0",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "1e1c3e60-f99c-41db-906e-6ddcd428c81b",
  "toolUseResult": {
    "bytes": 62479,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find a forum URL or paper ID for \"Process Reinforcement through Implicit Rewards\" (PRIME) at ICLR 2025.\n\nThe page shown is OpenReview's search error page, which displays: \"Error: Missing search term or query\" along with navigation links and footer information. The content does not include any specific paper details or forum links.\n\nTo locate this paper, you would need to perform an actual search on OpenReview.net or navigate directly to the ICLR 2025 venue page.",
    "durationMs": 2182,
    "url": "https://openreview.net/search?query=Process+Reinforcement+through+Implicit+Rewards&source=forum&group=ICLR.cc%2F2025%2FConference"
  },
  "sourceToolAssistantUUID": "4e5d6051-dfd7-4eed-b587-40fb45dd40c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T15:49:11.298Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DRVKJyzXHi6Lz3sdVgjYR4`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.01456",
  "prompt": "Extract the full content of this paper, including:\n1. The complete Introduction section\n2. The complete Method/Approach section (how implicit process rewards work, the mathematical formulation, training procedure)\n3. The Related Work section\n4. The Experiments section (key results, baselines, ablations)\n5. The Conclusion section (limitations, future work)\n\nBe as detailed as possible. Include mathematical formulations if present. Include all technical details about how PRIME works."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e1c3e60-f99c-41db-906e-6ddcd428c81b",
  "isSidechain": false,
  "requestId": "req_011CbTLXWEY8fbeaeKaXvmnz",
  "type": "assistant",
  "uuid": "3e8497c7-b0c3-4abe-9478-aaff3f54ed26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrNUoSFsRL6sXc9ooHtEyB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 199,
      "cache_creation_input_tokens": 601,
      "cache_read_input_tokens": 13874,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 199,
          "output_tokens": 330,
          "cache_read_input_tokens": 13874,
          "cache_creation_input_tokens": 601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 601
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

_source line 19 · 2026-05-27T15:49:43.493Z_

<details><summary>↩ Tool result · `toolu_01DRVKJyzXHi6Lz3sdVgjYR4`</summary>

```text
# PRIME: Process Reinforcement through Implicit Rewards - Comprehensive Summary

## 1. Introduction

The paper addresses a critical gap in reinforcement learning for large language models: while dense process rewards have proven effective at inference time for reasoning tasks, their incorporation into RL training remains underexplored. Current industry-leading models primarily depend on sparse outcome-level rewards.

The authors identify three central challenges:

**C1 - Definition Problem:** "It is difficult to collect step-level labels since reasoning steps do not naturally occur in sequences" and defining intermediate correctness proves ambiguous.

**C2 - Scalability Issue:** Updating process reward models (PRMs) online requires extensive step-level annotation, which is "prohibitively expensive" and makes models vulnerable to reward hacking.

**C3 - Computational Overhead:** Explicit reward model training introduces costly data collection and additional training phases.

The paper proposes PRIME (Process Reinforcement through IMplicit rEwards), which leverages implicit process reward modeling to enable online PRM updates using only outcome labels and policy rollouts, eliminating the need for dense step-level supervision.

**Key Achievement:** Starting from Qwen2.5-Math-7B-Base, PRIME achieves "15.1% average improvement" across reasoning benchmarks, with the resulting model surpassing larger instruction-tuned competitors using only "10% of the data used by Qwen-Math."

---

## 2. Method: PRIME Framework

### 2.1 Core Insight: Implicit Process Rewards

PRIME operates on a crucial innovation from prior work: implicit process rewards can be derived from a model trained with only outcome-level labels.

**Training Formulation:**
The Implicit PRM is trained using outcome labels with cross-entropy loss:

ℒ_CE(φ) = -𝔼[(r_o(𝐲) · log σ(r_φ(𝐲))) + ((1-r_o(𝐲)) · log(1-σ(r_φ(𝐲))))]

**Inference Formulation:**
At inference, token-level process rewards are computed as:

r_φ(y_t) := β log[π_φ(y_t|𝐲<t) / π_ref(y_t|𝐲<t)]

where π_φ is the reward model and π_ref is a reference model, both parameterized as causal language models. The parameter β scales the reward magnitude.

**Why This Works:** The implicit formulation provides "token-level rewards at no additional cost" compared to explicit PRMs, enabling fine-grained supervision without requiring step annotations.

### 2.2 Training Procedure (Algorithm 1)

PRIME follows a straightforward five-step cycle per iteration:

1. **Generation:** Sample K responses per prompt from policy πθ
2. **Evaluation:** Compute outcome rewards using ground-truth verifiers
3. **Filtering:** Apply accuracy-based prompt filtering (retains medium-difficulty samples)
4. **PRM Update:** Forward pass through both π_φ and π_ref to obtain implicit process rewards; update PRM via CE loss on outcome-labeled data
5. **Policy Update:** Compute advantages and perform PPO-style policy updates

**Critical Design Choice - Initialization:** Rather than training PRMs separately, PRIME initializes both the policy and PRM from the same SFT model. Empirical results show this approach "greatly outperforms" dedicated PRM training, suggesting that initializing from identical models "largely alleviates the distribution shift issue."

### 2.3 Advantage Estimation with Dense Rewards

PRIME combines token-level implicit process rewards with outcome rewards by calculating returns separately before aggregating:

A_t^i = [∑_{s=t}^{|𝐲^i|} γ^{s-t} · [r_φ(y_s^i) - (1/(K-1))∑_{j≠i} r_φ(𝐲^j)]] + [r_o(𝐲^i) - (1/(K-1))∑_{j≠i} r_o(𝐲^j)]

The first term represents discounted implicit process rewards with leave-one-out baseline; the second represents outcome rewards with identical baseline treatment. The separation prevents "numerical instability" from directly mixing reward scales.

This formulation is agnostic to the underlying RL algorithm—the paper demonstrates compatibility with REINFORCE, RLOO, GRPO, and PPO.

### 2.4 Online Prompt Filtering

During training, prompts are filtered to retain samples within a "median-level difficulty range." The paper shows this "largely lowers the variance of RL training" while balancing data distribution for PRM updates.

---

## 3. Related Work

PRIME connects three research streams:

**RL for LLM Reasoning:** Recent work (OpenAI o1, DeepSeek-R1) validated large-scale RL for reasoning but primarily used outcome rewards. PRIME addresses the underexplored role of dense rewards.

**Implicit Rewards:** Methods like DPO and implicit Q-function learning showed that reward signals can be derived from model probabilities without explicit reward heads. PRIME extends this to process-level rewards.

**Process Reward Models:** Prior work used human annotations (Lightman et al., 2023) or expensive estimation methods requiring "10× more rollouts" than response-level sampling. PRIME eliminates both constraints.

---

## 4. Experiments

### 4.1 Experimental Setup

**Base Model:** Qwen2.5-Math-7B-Base  
**SFT Phase:** 230K action-centric chain-of-thought examples (math, coding, biomedicine)  
**RL Training:** 150K math/coding prompts × 4 samples per prompt  
**Evaluation:** 7 benchmarks (AIME 2024, AMC, MATH-500, Minerva Math, OlympiadBench, LeetCode, LiveCodeBench)  
**Outcome Verifier:** Exact LaTeX match for math; test case pass rate for code

### 4.2 Main Results

The resulting model, Eurus-2-7B-PRIME, achieves substantial improvements:

| Benchmark | SFT Baseline | PRIME | Improvement |
|-----------|-------------|-------|-------------|
| AIME 2024 | 3.3% | 26.7% | +23.4pp |
| AMC | 30.1% | 57.8% | +27.7pp |
| MATH-500 | 66.2% | 79.2% | +13.0pp |
| **Average** | 28.8% | 43.9% | **+15.1pp** |

Notably, Eurus-2-7B-PRIME surpasses Qwen2.5-Math-7B-Instruct (the instruction-tuned version trained on 2.5M examples) on multiple benchmarks despite using only 230K SFT + 150K RL samples—approximately 10% of the instruction-tuning data.

### 4.3 Dense vs. Sparse Rewards Comparison

When compared to RLOO with outcome rewards only (both at 240 training steps):

- **Sample Efficiency:** PRIME achieves equivalent training performance in "40% of the training steps," translating to "2.5× sample efficiency gain"
- **Final Performance:** PRIME improves outcome training rewards by "6.9%" with lower variance
- **Computational Cost:** PRM updates add "24% more time" per step, but the efficiency gain reduces wall-clock training time by approximately 2×

### 4.4 Ablation Studies

**Online PRM Updates Are Essential:**
Comparing offline vs. online PRM training shows offline PRMs suffer reward hacking—accuracy drops over training as policy distributions shift. Online-updated PRMs maintain accuracy, directly translating to improved policy performance.

**Initialization Matters More Than Explicit Training:**
A PRM trained on 500K external data (EurusPRM) underperforms initialization from the SFT model, validating the insight that matching policy-PRM initialization prevents distribution shift.

**Works Across RL Algorithms:**
PRIME boosts REINFORCE, GRPO, PPO, and RLOO, demonstrating generality. Performance gains range from 1-4% depending on algorithm and scale.

**Rewards Superior to Values:**
Direct comparison of using the Implicit PRM as either process rewards or value estimates shows process rewards outperform both dedicated value models and using the PRM as a baseline—supporting the design choice of the advantage function.

**Scaling Results:**
- Extended training (800 rollout steps) maintains "3.7% improvement" over outcome-only baselines
- Increasing samples from 4 to 16 per prompt yields "4.4% gain," suggesting further scaling potential

### 4.5 Additional Experiments

**Zero-Shot RL from Base Model:**
Training directly from base models (skipping SFT) converges faster than SFT+RL pipelines, though it saturates earlier. 32B models benefit more than 7B variants.

**Reward Model Size Sensitivity:**
Varying reward model capacity (3B to 14B) while fixing policy at 7B shows "limited influence," with 7B achieving best average performance.

**Comparison with Baselines:**
- vs. VinePPO: PRIME is "11× more efficient" and achieves higher validation accuracy
- vs. DeepScaleR: Achieves comparable performance in one-third the training steps, with "25% faster" overall computation

---

## 5. Conclusion and Implications

### Key Findings

PRIME successfully addresses all three challenges identified in the introduction:

1. **C1 (Definition):** Implicit process rewards provide token-level supervision without explicit step annotation
2. **C2 (Scalability):** Online PRM updates use only outcome labels, avoiding expensive step-level supervision
3. **C3 (Overhead):** PRM initialization from SFT/base models eliminates dedicated training phases

### Technical Contributions

- A general framework for incorporating dense token-level rewards with sparse outcome rewards in any Monte-Carlo advantage estimation
- Demonstration that PRM initialization matching policy models prevents distribution shift
- Empirical validation that process rewards outperform learned value models for reasoning tasks
- Evidence that online reward model updates are essential to prevent overoptimization

### Limitations and Future Directions

The paper acknowledges the following constraints:

- Experiments limited to models up to 32B due to "resource constraints"
- Zero-shot RL exhibits early saturation, attributed to "decrease of response diversity"—left as future work
- Online filtering heuristic could be further optimized
- The framework assumes access to ground-truth outcome verifiers (though rule-based for math/code)

### Impact

The results suggest "RL for reasoning will become increasingly important" as text data becomes depleted, and PRIME provides a practical, scalable mechanism for leveraging dense supervision in this regime. The method's simplicity—initializing from a single language model and requiring only outcome labels—substantially lowers the barriers to deployment compared to prior PRM-based approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e8497c7-b0c3-4abe-9478-aaff3f54ed26",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "5137933b-3c90-4b71-b928-5e46c2dfff67",
  "toolUseResult": {
    "bytes": 281921,
    "code": 200,
    "codeText": "OK",
    "result": "# PRIME: Process Reinforcement through Implicit Rewards - Comprehensive Summary\n\n## 1. Introduction\n\nThe paper addresses a critical gap in reinforcement learning for large language models: while dense process rewards have proven effective at inference time for reasoning tasks, their incorporation into RL training remains underexplored. Current industry-leading models primarily depend on sparse outcome-level rewards.\n\nThe authors identify three central challenges:\n\n**C1 - Definition Problem:** \"It is difficult to collect step-level labels since reasoning steps do not naturally occur in sequences\" and defining intermediate correctness proves ambiguous.\n\n**C2 - Scalability Issue:** Updating process reward models (PRMs) online requires extensive step-level annotation, which is \"prohibitively expensive\" and makes models vulnerable to reward hacking.\n\n**C3 - Computational Overhead:** Explicit reward model training introduces costly data collection and additional training phases.\n\nThe paper proposes PRIME (Process Reinforcement through IMplicit rEwards), which leverages implicit process reward modeling to enable online PRM updates using only outcome labels and policy rollouts, eliminating the need for dense step-level supervision.\n\n**Key Achievement:** Starting from Qwen2.5-Math-7B-Base, PRIME achieves \"15.1% average improvement\" across reasoning benchmarks, with the resulting model surpassing larger instruction-tuned competitors using only \"10% of the data used by Qwen-Math.\"\n\n---\n\n## 2. Method: PRIME Framework\n\n### 2.1 Core Insight: Implicit Process Rewards\n\nPRIME operates on a crucial innovation from prior work: implicit process rewards can be derived from a model trained with only outcome-level labels.\n\n**Training Formulation:**\nThe Implicit PRM is trained using outcome labels with cross-entropy loss:\n\nℒ_CE(φ) = -𝔼[(r_o(𝐲) · log σ(r_φ(𝐲))) + ((1-r_o(𝐲)) · log(1-σ(r_φ(𝐲))))]\n\n**Inference Formulation:**\nAt inference, token-level process rewards are computed as:\n\nr_φ(y_t) := β log[π_φ(y_t|𝐲<t) / π_ref(y_t|𝐲<t)]\n\nwhere π_φ is the reward model and π_ref is a reference model, both parameterized as causal language models. The parameter β scales the reward magnitude.\n\n**Why This Works:** The implicit formulation provides \"token-level rewards at no additional cost\" compared to explicit PRMs, enabling fine-grained supervision without requiring step annotations.\n\n### 2.2 Training Procedure (Algorithm 1)\n\nPRIME follows a straightforward five-step cycle per iteration:\n\n1. **Generation:** Sample K responses per prompt from policy πθ\n2. **Evaluation:** Compute outcome rewards using ground-truth verifiers\n3. **Filtering:** Apply accuracy-based prompt filtering (retains medium-difficulty samples)\n4. **PRM Update:** Forward pass through both π_φ and π_ref to obtain implicit process rewards; update PRM via CE loss on outcome-labeled data\n5. **Policy Update:** Compute advantages and perform PPO-style policy updates\n\n**Critical Design Choice - Initialization:** Rather than training PRMs separately, PRIME initializes both the policy and PRM from the same SFT model. Empirical results show this approach \"greatly outperforms\" dedicated PRM training, suggesting that initializing from identical models \"largely alleviates the distribution shift issue.\"\n\n### 2.3 Advantage Estimation with Dense Rewards\n\nPRIME combines token-level implicit process rewards with outcome rewards by calculating returns separately before aggregating:\n\nA_t^i = [∑_{s=t}^{|𝐲^i|} γ^{s-t} · [r_φ(y_s^i) - (1/(K-1))∑_{j≠i} r_φ(𝐲^j)]] + [r_o(𝐲^i) - (1/(K-1))∑_{j≠i} r_o(𝐲^j)]\n\nThe first term represents discounted implicit process rewards with leave-one-out baseline; the second represents outcome rewards with identical baseline treatment. The separation prevents \"numerical instability\" from directly mixing reward scales.\n\nThis formulation is agnostic to the underlying RL algorithm—the paper demonstrates compatibility with REINFORCE, RLOO, GRPO, and PPO.\n\n### 2.4 Online Prompt Filtering\n\nDuring training, prompts are filtered to retain samples within a \"median-level difficulty range.\" The paper shows this \"largely lowers the variance of RL training\" while balancing data distribution for PRM updates.\n\n---\n\n## 3. Related Work\n\nPRIME connects three research streams:\n\n**RL for LLM Reasoning:** Recent work (OpenAI o1, DeepSeek-R1) validated large-scale RL for reasoning but primarily used outcome rewards. PRIME addresses the underexplored role of dense rewards.\n\n**Implicit Rewards:** Methods like DPO and implicit Q-function learning showed that reward signals can be derived from model probabilities without explicit reward heads. PRIME extends this to process-level rewards.\n\n**Process Reward Models:** Prior work used human annotations (Lightman et al., 2023) or expensive estimation methods requiring \"10× more rollouts\" than response-level sampling. PRIME eliminates both constraints.\n\n---\n\n## 4. Experiments\n\n### 4.1 Experimental Setup\n\n**Base Model:** Qwen2.5-Math-7B-Base  \n**SFT Phase:** 230K action-centric chain-of-thought examples (math, coding, biomedicine)  \n**RL Training:** 150K math/coding prompts × 4 samples per prompt  \n**Evaluation:** 7 benchmarks (AIME 2024, AMC, MATH-500, Minerva Math, OlympiadBench, LeetCode, LiveCodeBench)  \n**Outcome Verifier:** Exact LaTeX match for math; test case pass rate for code\n\n### 4.2 Main Results\n\nThe resulting model, Eurus-2-7B-PRIME, achieves substantial improvements:\n\n| Benchmark | SFT Baseline | PRIME | Improvement |\n|-----------|-------------|-------|-------------|\n| AIME 2024 | 3.3% | 26.7% | +23.4pp |\n| AMC | 30.1% | 57.8% | +27.7pp |\n| MATH-500 | 66.2% | 79.2% | +13.0pp |\n| **Average** | 28.8% | 43.9% | **+15.1pp** |\n\nNotably, Eurus-2-7B-PRIME surpasses Qwen2.5-Math-7B-Instruct (the instruction-tuned version trained on 2.5M examples) on multiple benchmarks despite using only 230K SFT + 150K RL samples—approximately 10% of the instruction-tuning data.\n\n### 4.3 Dense vs. Sparse Rewards Comparison\n\nWhen compared to RLOO with outcome rewards only (both at 240 training steps):\n\n- **Sample Efficiency:** PRIME achieves equivalent training performance in \"40% of the training steps,\" translating to \"2.5× sample efficiency gain\"\n- **Final Performance:** PRIME improves outcome training rewards by \"6.9%\" with lower variance\n- **Computational Cost:** PRM updates add \"24% more time\" per step, but the efficiency gain reduces wall-clock training time by approximately 2×\n\n### 4.4 Ablation Studies\n\n**Online PRM Updates Are Essential:**\nComparing offline vs. online PRM training shows offline PRMs suffer reward hacking—accuracy drops over training as policy distributions shift. Online-updated PRMs maintain accuracy, directly translating to improved policy performance.\n\n**Initialization Matters More Than Explicit Training:**\nA PRM trained on 500K external data (EurusPRM) underperforms initialization from the SFT model, validating the insight that matching policy-PRM initialization prevents distribution shift.\n\n**Works Across RL Algorithms:**\nPRIME boosts REINFORCE, GRPO, PPO, and RLOO, demonstrating generality. Performance gains range from 1-4% depending on algorithm and scale.\n\n**Rewards Superior to Values:**\nDirect comparison of using the Implicit PRM as either process rewards or value estimates shows process rewards outperform both dedicated value models and using the PRM as a baseline—supporting the design choice of the advantage function.\n\n**Scaling Results:**\n- Extended training (800 rollout steps) maintains \"3.7% improvement\" over outcome-only baselines\n- Increasing samples from 4 to 16 per prompt yields \"4.4% gain,\" suggesting further scaling potential\n\n### 4.5 Additional Experiments\n\n**Zero-Shot RL from Base Model:**\nTraining directly from base models (skipping SFT) converges faster than SFT+RL pipelines, though it saturates earlier. 32B models benefit more than 7B variants.\n\n**Reward Model Size Sensitivity:**\nVarying reward model capacity (3B to 14B) while fixing policy at 7B shows \"limited influence,\" with 7B achieving best average performance.\n\n**Comparison with Baselines:**\n- vs. VinePPO: PRIME is \"11× more efficient\" and achieves higher validation accuracy\n- vs. DeepScaleR: Achieves comparable performance in one-third the training steps, with \"25% faster\" overall computation\n\n---\n\n## 5. Conclusion and Implications\n\n### Key Findings\n\nPRIME successfully addresses all three challenges identified in the introduction:\n\n1. **C1 (Definition):** Implicit process rewards provide token-level supervision without explicit step annotation\n2. **C2 (Scalability):** Online PRM updates use only outcome labels, avoiding expensive step-level supervision\n3. **C3 (Overhead):** PRM initialization from SFT/base models eliminates dedicated training phases\n\n### Technical Contributions\n\n- A general framework for incorporating dense token-level rewards with sparse outcome rewards in any Monte-Carlo advantage estimation\n- Demonstration that PRM initialization matching policy models prevents distribution shift\n- Empirical validation that process rewards outperform learned value models for reasoning tasks\n- Evidence that online reward model updates are essential to prevent overoptimization\n\n### Limitations and Future Directions\n\nThe paper acknowledges the following constraints:\n\n- Experiments limited to models up to 32B due to \"resource constraints\"\n- Zero-shot RL exhibits early saturation, attributed to \"decrease of response diversity\"—left as future work\n- Online filtering heuristic could be further optimized\n- The framework assumes access to ground-truth outcome verifiers (though rule-based for math/code)\n\n### Impact\n\nThe results suggest \"RL for reasoning will become increasingly important\" as text data becomes depleted, and PRIME provides a practical, scalable mechanism for leveraging dense supervision in this regime. The method's simplicity—initializing from a single language model and requiring only outcome labels—substantially lowers the barriers to deployment compared to prior PRM-based approaches.",
    "durationMs": 32190,
    "url": "https://arxiv.org/html/2502.01456"
  },
  "sourceToolAssistantUUID": "3e8497c7-b0c3-4abe-9478-aaff3f54ed26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "5137933b-3c90-4b71-b928-5e46c2dfff67",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRIME paper on implicit process rewards",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Assistant

_source line 22 · 2026-05-27T15:49:46.569Z_

<details><summary>Logged reasoning block</summary>

```text
I have very detailed information about the paper. Now let me try to find the OpenReview page for reviewer comments. Let me try a different URL format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5137933b-3c90-4b71-b928-5e46c2dfff67",
  "isSidechain": false,
  "requestId": "req_011CbTLaLr58L6Kpvos75FGc",
  "type": "assistant",
  "uuid": "0cf115a7-f04d-45c9-89a2-f9a5b277bd94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuXWVfKrpjzgvQyvuLN7z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 14475,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 14475,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
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

### Assistant

_source line 23 · 2026-05-27T15:49:47.055Z_

Excellent, I have very detailed paper content. Let me now try to find the OpenReview page with reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cf115a7-f04d-45c9-89a2-f9a5b277bd94",
  "isSidechain": false,
  "requestId": "req_011CbTLaLr58L6Kpvos75FGc",
  "type": "assistant",
  "uuid": "950084b6-463f-42a9-a41e-a8a9945725ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuXWVfKrpjzgvQyvuLN7z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 14475,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 14475,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
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

### Tool call

_source line 24 · 2026-05-27T15:49:49.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LtHG3VvSouMpFEwpvcDXec`</summary>

```json
{
  "url": "https://openreview.net/search?query=%22Process+Reinforcement+through+Implicit+Rewards%22&source=forum&offset=0&venue=ICLR.cc/2025/Conference",
  "prompt": "Find the OpenReview forum link or paper ID for \"Process Reinforcement through Implicit Rewards\" at ICLR 2025. Return any URLs, forum IDs, or links to the paper page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "950084b6-463f-42a9-a41e-a8a9945725ed",
  "isSidechain": false,
  "requestId": "req_011CbTLaLr58L6Kpvos75FGc",
  "type": "assistant",
  "uuid": "5bf41cb7-d9ab-43a3-83c8-3e69873fb3fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuXWVfKrpjzgvQyvuLN7z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 14475,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 14475,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
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

### Tool call

_source line 25 · 2026-05-27T15:49:50.525Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014FZS7pjNSFg3xhUFCSuvAA`</summary>

```json
{
  "url": "https://openreview.net/group?id=ICLR.cc/2025/Conference#tab-accept-oral",
  "prompt": "Search through the accepted papers list for \"Process Reinforcement through Implicit Rewards\" or \"PRIME\" by Cui et al. Return the forum link or paper ID if found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf41cb7-d9ab-43a3-83c8-3e69873fb3fe",
  "isSidechain": false,
  "requestId": "req_011CbTLaLr58L6Kpvos75FGc",
  "type": "assistant",
  "uuid": "af85643d-f0e2-4d27-a563-d99380b8e788",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuXWVfKrpjzgvQyvuLN7z1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3326,
      "cache_read_input_tokens": 14475,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 14475,
          "cache_creation_input_tokens": 3326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3326
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

_source line 26 · 2026-05-27T15:49:52.075Z_

<details><summary>↩ Tool result · `toolu_01LtHG3VvSouMpFEwpvcDXec`</summary>

```text
# OpenReview Search Result

I cannot find the requested information in the provided web page content. The page shown is a search error page that states "Error: Missing search term or query" and only displays OpenReview's navigation menu and footer.

To locate "Process Reinforcement through Implicit Rewards" at ICLR 2025, you would need to:

1. Visit the actual OpenReview website at openreview.net
2. Use their search function with the paper title
3. Navigate to the ICLR 2025 venue page directly
4. Browse the conference submissions

The specific paper link, forum ID, or forum page is not available in the error page content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bf41cb7-d9ab-43a3-83c8-3e69873fb3fe",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "6dbfaf57-63e0-4909-b408-4c7f5a12551d",
  "toolUseResult": {
    "bytes": 62595,
    "code": 200,
    "codeText": "OK",
    "result": "# OpenReview Search Result\n\nI cannot find the requested information in the provided web page content. The page shown is a search error page that states \"Error: Missing search term or query\" and only displays OpenReview's navigation menu and footer.\n\nTo locate \"Process Reinforcement through Implicit Rewards\" at ICLR 2025, you would need to:\n\n1. Visit the actual OpenReview website at openreview.net\n2. Use their search function with the paper title\n3. Navigate to the ICLR 2025 venue page directly\n4. Browse the conference submissions\n\nThe specific paper link, forum ID, or forum page is not available in the error page content provided.",
    "durationMs": 2653,
    "url": "https://openreview.net/search?query=%22Process+Reinforcement+through+Implicit+Rewards%22&source=forum&offset=0&venue=ICLR.cc/2025/Conference"
  },
  "sourceToolAssistantUUID": "5bf41cb7-d9ab-43a3-83c8-3e69873fb3fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T15:49:52.894Z_

<details><summary>↩ Tool result · `toolu_014FZS7pjNSFg3xhUFCSuvAA`</summary>

```text
I cannot find the paper "Process Reinforcement through Implicit Rewards" (PRIME) by Cui et al. in the provided web page content. The content shown is primarily navigation and footer information from OpenReview.net's ICLR 2025 Conference page, without displaying an actual searchable papers list or specific paper details.

To locate this paper, you would need to:
1. Visit the ICLR 2025 venue page directly on OpenReview
2. Use their search functionality to query for the paper title or authors
3. Browse the accepted papers list if available
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af85643d-f0e2-4d27-a563-d99380b8e788",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "ee2b2e55-8ce1-4656-bd3c-e13cab7d0aa9",
  "toolUseResult": {
    "bytes": 74368,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the paper \"Process Reinforcement through Implicit Rewards\" (PRIME) by Cui et al. in the provided web page content. The content shown is primarily navigation and footer information from OpenReview.net's ICLR 2025 Conference page, without displaying an actual searchable papers list or specific paper details.\n\nTo locate this paper, you would need to:\n1. Visit the ICLR 2025 venue page directly on OpenReview\n2. Use their search functionality to query for the paper title or authors\n3. Browse the accepted papers list if available",
    "durationMs": 2367,
    "url": "https://openreview.net/group?id=ICLR.cc/2025/Conference#tab-accept-oral"
  },
  "sourceToolAssistantUUID": "af85643d-f0e2-4d27-a563-d99380b8e788",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-27T15:49:52.897Z_

```json
{
  "parentUuid": "ee2b2e55-8ce1-4656-bd3c-e13cab7d0aa9",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ad33e856-9801-423d-b66b-5f38bf2f31bd",
  "timestamp": "2026-05-27T15:49:52.897Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 29 · 2026-05-27T15:49:56.334Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ECvNC36dj3rbFLEQc4mJaS`</summary>

```json
{
  "url": "https://openreview.net/forum?id=process-reinforcement-implicit-rewards",
  "prompt": "Find the paper forum page. Return all content including reviewer comments, ratings, and author responses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad33e856-9801-423d-b66b-5f38bf2f31bd",
  "isSidechain": false,
  "requestId": "req_011CbTLb2yZaBrvajMfACXA3",
  "type": "assistant",
  "uuid": "fada96b3-6d37-4551-9481-304e8300f258",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTLRygyEzfP21XUXJjQG2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 17801,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 17801,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

### Tool call

_source line 30 · 2026-05-27T15:49:57.823Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011RW23qxXMqxzD3x5sMEHyK`</summary>

```json
{
  "url": "https://www.google.com/search?q=site:openreview.net+%22Process+Reinforcement+through+Implicit+Rewards%22+ICLR+2025",
  "prompt": "Find the OpenReview URL or forum ID for the paper \"Process Reinforcement through Implicit Rewards\" at ICLR 2025. Return any URLs that point to the OpenReview forum page for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fada96b3-6d37-4551-9481-304e8300f258",
  "isSidechain": false,
  "requestId": "req_011CbTLb2yZaBrvajMfACXA3",
  "type": "assistant",
  "uuid": "7ba8fe54-1eb1-44d1-9320-872cf96e02d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MTLRygyEzfP21XUXJjQG2b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 17801,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 17801,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 31 · 2026-05-27T15:49:59.047Z_

<details><summary>↩ Tool result · `toolu_01ECvNC36dj3rbFLEQc4mJaS`</summary>

```text
I cannot locate the paper forum page or any reviewer comments, ratings, and author responses based on the content provided.

The webpage shows an **error message** stating: "The Note process-reinforcement-implicit-rewards was not found." This indicates the requested paper or forum discussion does not exist at that URL on OpenReview.net.

To find the paper you're looking for, I'd recommend:
- Visiting the main OpenReview site and using their search functionality
- Browsing their venue listings at `/venues`
- Checking if the paper title or identifier is correct
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fada96b3-6d37-4551-9481-304e8300f258",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "639db30e-5a7f-4233-93ef-d5ec0df329da",
  "toolUseResult": {
    "bytes": 58685,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot locate the paper forum page or any reviewer comments, ratings, and author responses based on the content provided.\n\nThe webpage shows an **error message** stating: \"The Note process-reinforcement-implicit-rewards was not found.\" This indicates the requested paper or forum discussion does not exist at that URL on OpenReview.net.\n\nTo find the paper you're looking for, I'd recommend:\n- Visiting the main OpenReview site and using their search functionality\n- Browsing their venue listings at `/venues`\n- Checking if the paper title or identifier is correct",
    "durationMs": 2711,
    "url": "https://openreview.net/forum?id=process-reinforcement-implicit-rewards"
  },
  "sourceToolAssistantUUID": "fada96b3-6d37-4551-9481-304e8300f258",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-27T15:50:00.181Z_

<details><summary>↩ Tool result · `toolu_011RW23qxXMqxzD3x5sMEHyK`</summary>

```text
Based on the web page content provided, I cannot find a direct OpenReview URL or forum ID for the paper "Process Reinforcement through Implicit Rewards" at ICLR 2025.

The page only contains a Google Search interface with a link that searches for the paper on OpenReview using the query "site:openreview.net" combined with the paper title and conference. However, this is a search results page rather than the actual OpenReview forum page itself.

To locate the paper's OpenReview forum page, you would need to follow the provided search link or visit OpenReview.net directly and search for the paper by title or author.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ba8fe54-1eb1-44d1-9320-872cf96e02d7",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "6e31d29a-5fe1-4f72-a2d3-b0fb72012b1f",
  "toolUseResult": {
    "bytes": 90128,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find a direct OpenReview URL or forum ID for the paper \"Process Reinforcement through Implicit Rewards\" at ICLR 2025.\n\nThe page only contains a Google Search interface with a link that searches for the paper on OpenReview using the query \"site:openreview.net\" combined with the paper title and conference. However, this is a search results page rather than the actual OpenReview forum page itself.\n\nTo locate the paper's OpenReview forum page, you would need to follow the provided search link or visit OpenReview.net directly and search for the paper by title or author.",
    "durationMs": 2356,
    "url": "https://www.google.com/search?q=site:openreview.net+%22Process+Reinforcement+through+Implicit+Rewards%22+ICLR+2025"
  },
  "sourceToolAssistantUUID": "7ba8fe54-1eb1-44d1-9320-872cf96e02d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T15:50:05.520Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BLTE12TvYvEBhbSZCaTkUN`</summary>

```json
{
  "url": "https://www.google.com/search?q=openreview.net+%22Process+Reinforcement+through+Implicit+Rewards%22",
  "prompt": "Find the OpenReview forum URL for the paper \"Process Reinforcement through Implicit Rewards\". Look for any URL containing openreview.net/forum?id= and return it exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e31d29a-5fe1-4f72-a2d3-b0fb72012b1f",
  "isSidechain": false,
  "requestId": "req_011CbTLbaDmFa29fQpzBfocW",
  "type": "assistant",
  "uuid": "e5f63584-bdfd-4461-a904-55aa53f81a49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDj1ThgTEJ5irUquYXqsZc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 18595,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 18595,
          "cache_creation_input_tokens": 576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 576
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

_source line 34 · 2026-05-27T15:50:07.991Z_

<details><summary>↩ Tool result · `toolu_01BLTE12TvYvEBhbSZCaTkUN`</summary>

```text
Based on the content provided, I cannot find the OpenReview forum URL for the paper "Process Reinforcement through Implicit Rewards". 

The webpage only contains a Google Search error message with a link to search OpenReview, but does not include the actual forum URL in the format openreview.net/forum?id=. To locate this paper, you would need to visit OpenReview.net directly or follow the search link provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5f63584-bdfd-4461-a904-55aa53f81a49",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "71ca998f-379e-47c5-b6a8-742637336407",
  "toolUseResult": {
    "bytes": 90507,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the content provided, I cannot find the OpenReview forum URL for the paper \"Process Reinforcement through Implicit Rewards\". \n\nThe webpage only contains a Google Search error message with a link to search OpenReview, but does not include the actual forum URL in the format openreview.net/forum?id=. To locate this paper, you would need to visit OpenReview.net directly or follow the search link provided on the page.",
    "durationMs": 2469,
    "url": "https://www.google.com/search?q=openreview.net+%22Process+Reinforcement+through+Implicit+Rewards%22"
  },
  "sourceToolAssistantUUID": "e5f63584-bdfd-4461-a904-55aa53f81a49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-27T15:50:11.309Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WcyZdSFJxWyoFh7zYvoQq8`</summary>

```json
{
  "url": "https://api.openreview.net/notes/search?query=Process+Reinforcement+through+Implicit+Rewards&source=forum&limit=5&content.venue=ICLR+2025",
  "prompt": "Return the full JSON response. I'm looking for the forum ID (the \"id\" field) for the paper \"Process Reinforcement through Implicit Rewards\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71ca998f-379e-47c5-b6a8-742637336407",
  "isSidechain": false,
  "requestId": "req_011CbTLc9T2MRjMKjE6Akntt",
  "type": "assistant",
  "uuid": "3dfba476-2d89-4bfe-b833-01006b109bd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZDdySymfhK4GotAyKctQa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 251,
      "cache_read_input_tokens": 19171,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 19171,
          "cache_creation_input_tokens": 251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 251
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

_source line 36 · 2026-05-27T15:50:14.790Z_

<details><summary>↩ Tool result · `toolu_01WcyZdSFJxWyoFh7zYvoQq8`</summary>

```text
Based on the provided JSON content, I cannot find a paper titled "Process Reinforcement through Implicit Rewards." The document contains five papers with the following titles:

1. "Reinforcement Learning with Perturbed Rewards"
2. "Hybrid Policies Using Inverse Rewards for Reinforcement Learning"
3. "Quantile Regression Reinforcement Learning with State Aligned Vector Rewards" (appears twice)
4. "Annotating Implicit Reasoning in Arguments with Causal Links"

The paper you're searching for does not appear in this dataset. Please verify the exact title or provide additional information to help locate the correct forum ID.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dfba476-2d89-4bfe-b833-01006b109bd0",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "277ffb8f-09a2-43a6-9a40-72c1981b441b",
  "toolUseResult": {
    "bytes": 10978,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided JSON content, I cannot find a paper titled \"Process Reinforcement through Implicit Rewards.\" The document contains five papers with the following titles:\n\n1. \"Reinforcement Learning with Perturbed Rewards\"\n2. \"Hybrid Policies Using Inverse Rewards for Reinforcement Learning\"\n3. \"Quantile Regression Reinforcement Learning with State Aligned Vector Rewards\" (appears twice)\n4. \"Annotating Implicit Reasoning in Arguments with Causal Links\"\n\nThe paper you're searching for does not appear in this dataset. Please verify the exact title or provide additional information to help locate the correct forum ID.",
    "durationMs": 3477,
    "url": "https://api.openreview.net/notes/search?query=Process+Reinforcement+through+Implicit+Rewards&source=forum&limit=5&content.venue=ICLR+2025"
  },
  "sourceToolAssistantUUID": "3dfba476-2d89-4bfe-b833-01006b109bd0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-27T15:50:18.196Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013DGTUp8K6QkpsytsFwpSjP`</summary>

```json
{
  "url": "https://api.openreview.net/notes/search?query=PRIME+implicit+process+rewards+Cui&source=forum&limit=5",
  "prompt": "Return any paper results, especially the forum ID for a paper about \"Process Reinforcement through Implicit Rewards\" or PRIME by Cui et al."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "277ffb8f-09a2-43a6-9a40-72c1981b441b",
  "isSidechain": false,
  "requestId": "req_011CbTLceYVcjrTee4qUY1Mh",
  "type": "assistant",
  "uuid": "99e52149-a889-4020-9bcc-ae76bcab076b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WWRfqTCVtxqP14dUDgPgQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 306,
      "cache_read_input_tokens": 19422,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 19422,
          "cache_creation_input_tokens": 306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 306
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

_source line 38 · 2026-05-27T15:50:22.433Z_

<details><summary>↩ Tool result · `toolu_013DGTUp8K6QkpsytsFwpSjP`</summary>

```text
Based on the provided content, I found no papers matching "Process Reinforcement through Implicit Rewards" or "PRIME by Cui et al."

The search results include papers by authors named Cui, but they focus on different topics:

1. **"Great Service! Fine-grained Parsing of Implicit Arguments"** by Ruixiang Cui and Daniel Hershcovich (Forum IDs: aUPXwSqAZFr and Qrwi5Xb1Vh) - addresses implicit arguments in NLP rather than process reinforcement.

2. A paper on "Mining process models with prime invisible tasks" by Wen et al. (Forum ID: Z2PD9ONStw4) - concerns process mining, not implicit rewards.

The requested paper does not appear in this dataset.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99e52149-a889-4020-9bcc-ae76bcab076b",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "af6f172d-607b-4a8f-b162-a5a7f7973962",
  "toolUseResult": {
    "bytes": 12207,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided content, I found no papers matching \"Process Reinforcement through Implicit Rewards\" or \"PRIME by Cui et al.\"\n\nThe search results include papers by authors named Cui, but they focus on different topics:\n\n1. **\"Great Service! Fine-grained Parsing of Implicit Arguments\"** by Ruixiang Cui and Daniel Hershcovich (Forum IDs: aUPXwSqAZFr and Qrwi5Xb1Vh) - addresses implicit arguments in NLP rather than process reinforcement.\n\n2. A paper on \"Mining process models with prime invisible tasks\" by Wen et al. (Forum ID: Z2PD9ONStw4) - concerns process mining, not implicit rewards.\n\nThe requested paper does not appear in this dataset.",
    "durationMs": 4232,
    "url": "https://api.openreview.net/notes/search?query=PRIME+implicit+process+rewards+Cui&source=forum&limit=5"
  },
  "sourceToolAssistantUUID": "99e52149-a889-4020-9bcc-ae76bcab076b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-27T15:50:24.602Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try a different approach to find the OpenReview page. The paper might be under a different ID or might have been submitted under a slightly different title.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af6f172d-607b-4a8f-b162-a5a7f7973962",
  "isSidechain": false,
  "requestId": "req_011CbTLdDHVNQeWRJrP8LPJz",
  "type": "assistant",
  "uuid": "9cd2d9a7-8fe7-4699-9c00-685a383a41f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193WCcpEpobzAGFNMMXwajY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 19728,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 330,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 19728,
          "cache_creation_input_tokens": 330,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 330
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

### Assistant

_source line 40 · 2026-05-27T15:50:25.098Z_

Let me try one more approach to find the OpenReview page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cd2d9a7-8fe7-4699-9c00-685a383a41f1",
  "isSidechain": false,
  "requestId": "req_011CbTLdDHVNQeWRJrP8LPJz",
  "type": "assistant",
  "uuid": "cb2593e9-0b58-4070-a107-818b7553156a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193WCcpEpobzAGFNMMXwajY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 19728,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 330,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 19728,
          "cache_creation_input_tokens": 330,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 330
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

### Tool call

_source line 41 · 2026-05-27T15:50:26.527Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HhHXEoMv6TcTBYc9XWMLNF`</summary>

```json
{
  "url": "https://iclr.cc/virtual/2025/papers.html?filter=areas&search=Process+Reinforcement",
  "prompt": "Find the paper \"Process Reinforcement through Implicit Rewards\" and return its OpenReview forum link or ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb2593e9-0b58-4070-a107-818b7553156a",
  "isSidechain": false,
  "requestId": "req_011CbTLdDHVNQeWRJrP8LPJz",
  "type": "assistant",
  "uuid": "c11e75ed-824c-426b-8f57-60906d60243f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193WCcpEpobzAGFNMMXwajY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 19728,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 330,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 19728,
          "cache_creation_input_tokens": 330,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 330
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

### Tool call

_source line 42 · 2026-05-27T15:50:29.285Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0183tJbrG8UJvwTqAbC63gJp`</summary>

```json
{
  "url": "https://scholar.google.com/scholar?q=%22Process+Reinforcement+through+Implicit+Rewards%22+PRIME",
  "prompt": "Find the OpenReview link for this paper. Look for any openreview.net URL in the search results and return it exactly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c11e75ed-824c-426b-8f57-60906d60243f",
  "isSidechain": false,
  "requestId": "req_011CbTLdDHVNQeWRJrP8LPJz",
  "type": "assistant",
  "uuid": "8c85123e-5508-489a-a37c-dfa8ba0c9426",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193WCcpEpobzAGFNMMXwajY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 19728,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 330,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 292,
          "cache_read_input_tokens": 19728,
          "cache_creation_input_tokens": 330,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 330
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

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "8c85123e-5508-489a-a37c-dfa8ba0c9426",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRIME paper on implicit process rewards",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Tool result

_source line 45 · 2026-05-27T15:50:31.468Z_

<details><summary>↩ Tool result · `toolu_01HhHXEoMv6TcTBYc9XWMLNF`</summary>

```text
I cannot find the paper "Process Reinforcement through Implicit Rewards" in the provided web page content. The page shows the ICLR 2025 conference navigation and interface, but does not display a list of specific papers with their titles or OpenReview links.

To locate this paper, you would need to:
1. Use the "Papers" section at "/virtual/2025/papers.html"
2. Search directly on OpenReview at "https://openreview.net/group?id=ICLR.cc"
3. Use the search functionality available on the ICLR 2025 website
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c11e75ed-824c-426b-8f57-60906d60243f",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "b3a7f7cd-d219-4485-ae7f-12b85d76583a",
  "toolUseResult": {
    "bytes": 523641,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the paper \"Process Reinforcement through Implicit Rewards\" in the provided web page content. The page shows the ICLR 2025 conference navigation and interface, but does not display a list of specific papers with their titles or OpenReview links.\n\nTo locate this paper, you would need to:\n1. Use the \"Papers\" section at \"/virtual/2025/papers.html\"\n2. Search directly on OpenReview at \"https://openreview.net/group?id=ICLR.cc\"\n3. Use the search functionality available on the ICLR 2025 website",
    "durationMs": 4938,
    "url": "https://iclr.cc/virtual/2025/papers.html?filter=areas&search=Process+Reinforcement"
  },
  "sourceToolAssistantUUID": "c11e75ed-824c-426b-8f57-60906d60243f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T15:50:32.569Z_

<details><summary>↩ Tool result · `toolu_0183tJbrG8UJvwTqAbC63gJp`</summary>

```text
I cannot find an OpenReview link in the provided content. The webpage shown is a Google Scholar search results page (in Japanese) for "Process Reinforcement through Implicit Rewards" PRIME, but it appears to be in a loading or error state. The page displays "現在システムで処理を実行できません" (the system cannot currently process this request) and contains only navigation menus and search options—no actual search results or links to OpenReview or other paper repositories are visible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c85123e-5508-489a-a37c-dfa8ba0c9426",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "a667f089-1873-4e0d-afdc-afaefbb5a885",
  "toolUseResult": {
    "bytes": 133321,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find an OpenReview link in the provided content. The webpage shown is a Google Scholar search results page (in Japanese) for \"Process Reinforcement through Implicit Rewards\" PRIME, but it appears to be in a loading or error state. The page displays \"現在システムで処理を実行できません\" (the system cannot currently process this request) and contains only navigation menus and search options—no actual search results or links to OpenReview or other paper repositories are visible.",
    "durationMs": 3280,
    "url": "https://scholar.google.com/scholar?q=%22Process+Reinforcement+through+Implicit+Rewards%22+PRIME"
  },
  "sourceToolAssistantUUID": "8c85123e-5508-489a-a37c-dfa8ba0c9426",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-27T15:50:35.629Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016s7avVy8K3tAyVEKRq3NeF`</summary>

```json
{
  "url": "https://openreview.net/forum?id=rkigcYHFDS",
  "prompt": "Check if this is the forum page for \"Process Reinforcement through Implicit Rewards\". Return the paper title and any content found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a667f089-1873-4e0d-afdc-afaefbb5a885",
  "isSidechain": false,
  "requestId": "req_011CbTLdxaj1V2jSdAi5GgZm",
  "type": "assistant",
  "uuid": "eb1361ad-95f2-4432-990d-78d4aedd7ff3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PxYhbPhCz4t7YNisNrcfS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 20058,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 20058,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

### Tool call

_source line 48 · 2026-05-27T15:50:36.833Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015h9VVLyaxdPfY7ZUe393pK`</summary>

```json
{
  "url": "https://huggingface.co/papers/2502.01456",
  "prompt": "Find any link to the OpenReview page for this paper. Also extract any additional information about the paper's venue, acceptance, or reviews."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb1361ad-95f2-4432-990d-78d4aedd7ff3",
  "isSidechain": false,
  "requestId": "req_011CbTLdxaj1V2jSdAi5GgZm",
  "type": "assistant",
  "uuid": "1fa6952e-ad8d-4afb-b51b-d2550116a941",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PxYhbPhCz4t7YNisNrcfS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 20058,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 20058,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

_source line 49 · 2026-05-27T15:50:37.647Z_

<details><summary>↩ Tool result · `toolu_015h9VVLyaxdPfY7ZUe393pK`</summary>

```text
&lt;persisted-output>
Output too large (94.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/ae85f63b-06b5-4781-b92e-92dc801697c7/tool-results/toolu_015h9VVLyaxdPfY7ZUe393pK.txt

Preview (first 2KB):
Title: Process Reinforcement through Implicit Rewards

URL Source: https://arxiv.org/html/2502.01456

Markdown Content:
Ganqu Cui 1,2†, Lifan Yuan 3∗, Zefan Wang 2∗, Hanbin Wang 4∗, Yuchen Zhang 1∗, 

Jiacheng Chen 1∗, Wendi Li 2∗, Bingxiang He 2∗, Yuchen Fan 1,5∗, Tianyu Yu 2∗, Qixin Xu 2∗, 

Weize Chen 2, Jiarui Yuan 2, Huayu Chen 2, Kaiyan Zhang 2, Xingtai Lv 2, Shuo Wang 2, 

Yuan Yao 2, Xu Han 2, Hao Peng 3, Yu Cheng 1,6, Zhiyuan Liu 2, Maosong Sun 2, 

Bowen Zhou 1,2, Ning Ding 2†

1 Shanghai AI Lab 2 Tsinghua University 3 University of Illinois Urbana-Champaign 

4 Peking University 5 Shanghai Jiaotong University 6 CUHK 

cuiganqu@pjlab.org.cn lifan4@illinois.edu

###### Abstract

Dense process rewards have proven a more effective alternative to the sparse outcome-level rewards in the inference-time scaling of large language models (LLMs), particularly in tasks requiring complex multi-step reasoning. While dense rewards also offer an appealing choice for the reinforcement learning (RL) of LLMs since their fine-grained rewards have the potential to address some inherent issues of outcome rewards, such as training efficiency and credit assignment, this potential remains largely unrealized. This can be primarily attributed to the challenges of training process reward models (PRMs) online, where collecting high-quality process labels is prohibitively expensive, making them particularly vulnerable to reward hacking. To address these challenges, we propose PRIME (P rocess R einforcement through IM plicit r E wards), which enables online PRM updates using only policy rollouts and outcome labels through implicit process rewards. PRIME combines well with various advantage functions and forgoes the dedicated reward model training phase that existing approaches require, substantially reducing the development overhead. We demonstrate PRIME’s effectiveness on competitional math and coding. Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement acro
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fa6952e-ad8d-4afb-b51b-d2550116a941",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "dec1bf6b-c399-4474-a0c9-7f6db2f12654",
  "toolUseResult": {
    "bytes": 97815,
    "code": 200,
    "codeText": "OK",
    "result": "Title: Process Reinforcement through Implicit Rewards\n\nURL Source: https://arxiv.org/html/2502.01456\n\nMarkdown Content:\nGanqu Cui 1,2†, Lifan Yuan 3∗, Zefan Wang 2∗, Hanbin Wang 4∗, Yuchen Zhang 1∗, \n\nJiacheng Chen 1∗, Wendi Li 2∗, Bingxiang He 2∗, Yuchen Fan 1,5∗, Tianyu Yu 2∗, Qixin Xu 2∗, \n\nWeize Chen 2, Jiarui Yuan 2, Huayu Chen 2, Kaiyan Zhang 2, Xingtai Lv 2, Shuo Wang 2, \n\nYuan Yao 2, Xu Han 2, Hao Peng 3, Yu Cheng 1,6, Zhiyuan Liu 2, Maosong Sun 2, \n\nBowen Zhou 1,2, Ning Ding 2†\n\n1 Shanghai AI Lab 2 Tsinghua University 3 University of Illinois Urbana-Champaign \n\n4 Peking University 5 Shanghai Jiaotong University 6 CUHK \n\ncuiganqu@pjlab.org.cn lifan4@illinois.edu\n\n###### Abstract\n\nDense process rewards have proven a more effective alternative to the sparse outcome-level rewards in the inference-time scaling of large language models (LLMs), particularly in tasks requiring complex multi-step reasoning. While dense rewards also offer an appealing choice for the reinforcement learning (RL) of LLMs since their fine-grained rewards have the potential to address some inherent issues of outcome rewards, such as training efficiency and credit assignment, this potential remains largely unrealized. This can be primarily attributed to the challenges of training process reward models (PRMs) online, where collecting high-quality process labels is prohibitively expensive, making them particularly vulnerable to reward hacking. To address these challenges, we propose PRIME (P rocess R einforcement through IM plicit r E wards), which enables online PRM updates using only policy rollouts and outcome labels through implicit process rewards. PRIME combines well with various advantage functions and forgoes the dedicated reward model training phase that existing approaches require, substantially reducing the development overhead. We demonstrate PRIME’s effectiveness on competitional math and coding. Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement across several key reasoning benchmarks over the SFT model. Notably, our resulting model, Eurus-2-7B-PRIME, surpasses Qwen2.5-Math-7B-Instruct on seven reasoning benchmarks with 10% of its training data.\n\n1 Introduction\n--------------\n\nDense process rewards, which provide feedback at each intermediate step rather than only the whole trajectory, have proven effective in inference-time scaling of large language models (LLMs) on challenging reasoning tasks(Uesato et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib48); Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26); Wang et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib49); Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)). On the training side, they also present superiority in the reinforcement learning (RL) of LLMs, particularly in improving training efficiency(Sutton & Barto, [2018](https://arxiv.org/html/2502.01456v2#bib.bib44)) and credit assignment(Leike et al., [2018](https://arxiv.org/html/2502.01456v2#bib.bib21)) compared with sparse outcome rewards. However, successful applications of dense rewards in RL for LLMs are limited(Setlur et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib38)), as current industry-leading models primarily depend on verifiable outcome rewards and have not yet demonstrated meaningful progress with dense rewards(DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7); Team et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib45)).\n\nWe identify the central challenge as how to acquire and utilize high-quality dense rewards at scale, which enables online process reward model (PRM) update efficiently. The reason is that, optimizing towards a static reward model eventually leads to overoptimization or reward hacking(Gao et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib10)) due to distribution shift. Ideally, this can be solved by improving the reward model online(Leike et al., [2018](https://arxiv.org/html/2502.01456v2#bib.bib21)). However, acquiring dense process labels for training is prohibitively more expensive. Existing methods either need to build complicated human annotation pipelines(Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)) or rely on estimation-based methods, which require about 10×\\times more rollouts for each step than sampling only the response-level trajectories(Wang et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib49); Kazemnejad et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib18)). Neither of them is scalable in online RL. Moreover, to the best of our knowledge, it remains underexplored how to incorporate dense rewards into RL for LLMs.\n\nIn this work, we propose Process Reinforcement through Implicit Rewards (PRIME), a scalable framework for enhancing reasoning capabilities via efficient reinforcement learning with dense token-level rewards. At its core, the framework employs recently proposed implicit process reward modeling(Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)) to train dense reward models with only outcome-level labels. This enables PRIME to perform online learning of reward signals using only outcome labels on policy rollouts, thereby fundamentally mitigating reward hacking while maintaining the same computational cost as traditional outcome reward models (ORMs). Besides scalability, PRIME also (1) serves as a general method to fuse token-level dense rewards and sparse outcome rewards by calculating their returns separately before summing together, which is compatible with diverse RL algorithms(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51); Kool et al., [2019](https://arxiv.org/html/2502.01456v2#bib.bib19); Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1); Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)); (2) eliminates the dedicated reward modeling stage, which is required by existing works, by simply initializing from the SFT model or even the base model (§[B.4](https://arxiv.org/html/2502.01456v2#A2.SS4 \"B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\")). In summary, starting from one single language model, the PRIME framework can efficiently accomplish the generation of dense rewards, the initialization and updating of reward models, as well as the reinforcement learning (RL) training of the policy model.\n\nIn experiments, we train Qwen2.5-Math-7B-Base(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)) with PRIME after a lightweight SFT warmup stage. Compared to RL using outcome rewards only, PRIME achieves a 2.5×2.5\\times sample efficiency gain and a 6.9%6.9\\% performance improvements on challenging math problems. As shown in Figure [12](https://arxiv.org/html/2502.01456v2#A2.F12 \"Figure 12 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), through PRIME, we successfully achieve substantial improvement on key mathematical reasoning benchmarks over the SFT model, leading to 16.7% improvement on average, and over 20% on AMC&AIME competitions. Our final model Eurus-2-7B-PRIME surpassed Qwen2.5-Math-7B-Instruct on five key mathematical benchmarks. Notably, this is achieved with only 10%10\\% of the data used by Qwen-Math, as in Table [3](https://arxiv.org/html/2502.01456v2#A2.T3 \"Table 3 ‣ B.2 Single-Forward v.s. Double-Forward ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\").\n\nOur analysis shows that updating the PRM online is key to the success of PRIME (§[5.1](https://arxiv.org/html/2502.01456v2#S5.SS1 \"5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\")). We also show that PRIME could generally boost various RL algorithms, including RLOO (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)), REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), PPO(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)), and GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)) (§[5.3](https://arxiv.org/html/2502.01456v2#S5.SS3 \"5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\")). In terms of the design choices of advantage estimate, we observe that Implicit PRMs are better to be used as reward models than value models (§[5.4](https://arxiv.org/html/2502.01456v2#S5.SS4 \"5.4 Value or Reward, How to Use the Implicit PRM? ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\")).\n\n2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards\n----------------------------------------------------------------------------------\n\nReinforcement Learning (RL) aims to learn an optimal policy π θ\\pi_{\\theta} that maximizes the expected cumulative discounted reward, namely return, when interacting with an environment. In the context of autoregressive language modeling, state at step t t is the concatenation of prompt 𝐱\\mathbf{x} and current response 𝐲<t\\mathbf{y}_{<t}, and the action is the t t-th token or step y t y_{t}.\n\n### 2.1 RL Preliminaries for LLMs\n\nPolicy Gradient. Policy gradient is a fundamental algorithm that directly optimizes this objective. Central to this approach is the advantage function A t A_{t}, which quantifies how much better an action is compared to alternatives in a given state:\n\n∇θ J​(θ)=𝔼 𝐱∼𝒟,𝐲∼π θ​[∑t=0 T∇θ log⁡π θ​(y t|𝐲<t)​A t]\\nabla_{\\theta}J(\\theta)=\\mathbb{E}_{\\mathbf{x}\\sim\\mathcal{D},\\mathbf{y}\\sim\\pi_{\\theta}}\\left[\\sum_{t=0}^{T}\\nabla_{\\theta}\\log\\pi_{\\theta}(y_{t}|\\mathbf{y}_{<t})A_{t}\\right](1)\n\nwhere (𝐱,𝐲)\\left(\\mathbf{x},\\mathbf{y}\\right) represents a pair of input and output. 𝐱\\mathbf{x} is omitted for brevity. In practice, the advantage function is implemented as cumulative discounted rewards subtracting a baseline:\n\nA t=∑s=t T γ s−t​r​(y s)−b A_{t}=\\sum_{s=t}^{T}\\gamma^{s-t}r(y_{s})-b(2)\n\nγ∈[0,1]\\gamma\\in[0,1] is a discount factor that optionally decays future rewards, and r​(y s)r(y_{s}) is the reward provided by the environment at time step s s with x x and 𝐲<s\\mathbf{y}_{<s} being omitted in conditions. Eq.[2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") is the general formula of the Monte-Carlo (MC) advantage estimate, which indicates that, the high-quality and dense reward at each step is crucial for RL. Different choices of b b include, e.g. directly using values (Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), group average of rewards(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)), and leave-one-out average of rewards (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1); Kool et al., [2019](https://arxiv.org/html/2502.01456v2#bib.bib19)).\n\nValue Models. Though the MC estimate is unbiased, it suffers from high variance because of the reliance on all future actions and rewards, which can be random and noisy. Value models, which predict expected accumulated rewards starting from a state, are adopted to help reduce the variance in advantage estimation, such as Generalized Advantage Estimation (GAE;Schulman et al., [2016](https://arxiv.org/html/2502.01456v2#bib.bib36)): A t GAE​(γ,λ)=∑s=0∞(γ​λ)s​δ t+s A_{t}^{\\text{GAE}(\\gamma,\\lambda)}=\\sum_{s=0}^{\\infty}(\\gamma\\lambda)^{s}\\delta_{t+s}, where δ t=r​(y t)+γ​V​(𝐲<t+1)−V​(𝐲<t)\\delta_{t}=r(y_{t})+\\gamma V(\\mathbf{y}_{<t+1})-V(\\mathbf{y}_{<t}) is the temporal difference (TD) error(Sutton, [1988](https://arxiv.org/html/2502.01456v2#bib.bib43)), V V is a value model, and λ\\lambda controls the bias-variance tradeoff in advantage estimation. PPO (Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)) is a representative of such actor-critic algorithms that explicitly train a value model along with the policy.\n\nReward Sparsity. Although dense rewards can be naturally integrated into the advantage function through Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\"), unfortunately, only outcome reward models (ORMs) are available in most practices of LLMs, i.e., only the final token bears a meaningful reward while intermediate tokens receive no rewards(Rafailov et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib33); Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)). In this bandit setting, r​(y t)=0 r(y_{t})=0 for t<T t<T while r​(y T)r(y_{T}) can be non-zero, and Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") becomes A=r​(y T)−b A=r(y_{T})-b. This formulation, while simpler, can suffer from reward sparsity issues as the policy receives feedback only at the end of the entire generation. This may (1) encourage spurious solutions with incorrect processes but correct answers, (2) largely reduce sample efficiency in training, and (3) encounter the credit assignment problem(Sutton & Barto, [2018](https://arxiv.org/html/2502.01456v2#bib.bib44)). These drawbacks could be further amplified on complicated tasks, which require more thinking and execution steps, urging the need of dense rewards(Uesato et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib48); Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)). Some may consider employing a value model to mitigate the problem, as it predicts values at every step t t. However, previous work showed that value models may not be able to solve the reward sparsity issue effectively due to training challenges, despite the additional computation overhead(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)). We will also empirically validate this claim in §[5.4](https://arxiv.org/html/2502.01456v2#S5.SS4 \"5.4 Value or Reward, How to Use the Implicit PRM? ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\n### 2.2 Key Challenges in Scalable Dense Rewards\n\n![Image 1: Refer to caption](https://arxiv.org/html/2502.01456v2/x1.png)\n\nFigure 1: Illustration of PRIME. PRIME follows that (1) initialize policy model and the Implicit PRM both with the reference model; (2) sample multiple responses for each prompt and filter with output accuracy; (3) obtain implicit process rewards by the Implicit PRM and update it using cross-entropy (CE) loss; (4) compute advantage and policy loss then update the policy model. \n\nThe way to mitigate the reward sparsity problem is to adopt dense reward models, namely PRMs, which score model responses over each token or step. However, it is usually infeasible in practice to incorporate dense rewards into online RL because of three critical challenges in implementation.\n\nC1. Process rewards are hard to define. It is difficult to collect step-level labels since reasoning steps do not naturally occur in sequences. Although tokens are easily distinguishable, annotating labels for each token is too costly. Moreover, defining the absolute correctness of intermediate processes as dense rewards can be ambiguous, as some incorrect steps can also positively contribute to the final answer by pruning searching branches (OpenAI, [2024](https://arxiv.org/html/2502.01456v2#bib.bib31); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)).\n\nC2. PRM online updates are not scalable. It is crucial to prevent reward overoptimization or reward hacking, which requires the reward model or value model to be updated online along with the policy model(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37); Gao et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib10)). However, training PRMs often requires extensive nuanced step-level annotation, which is infeasible in online RL training. Therefore, this brings about considerable scalability and generalization concerns in dense rewards for RL.\n\nC3. Explicit reward modeling brings extra cost. Training reward models requires extensive annotation and broad data coverage to ensure a good balance between adaptability to the policy distribution and generalization to distribution shifts. Hence, the explicit training stage introduces a very costly data collection and an additional training overhead, especially for PRMs which typically require stepwise labels.\n\nNotably, DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)) shares similar conclusions and thus is impeded from incorporating PRMs into large-scale RL training.\n\n3 PRIME\n-------\n\nTo address the above challenges, we propose PRIME, a scalable online RL method with dense rewards. The key insight of PRIME is to apply implicit process rewards, which are derivable from the Implicit PRM that is trained with only outcome labels(Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)). This property enables us to update the PRMs online to avoid reward hacking. We then design a flexible framework to incorporate implicit process rewards with outcome rewards into any kind of MC advantage estimate. PRIME is illustrated in Figure [1](https://arxiv.org/html/2502.01456v2#S2.F1 \"Figure 1 ‣ 2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") and Algorithm [1](https://arxiv.org/html/2502.01456v2#alg1 \"Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"). Next, we will detail the implicit process rewards (§[3.1](https://arxiv.org/html/2502.01456v2#S3.SS1 \"3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")) and how we leverage them to calculate advantages (§[3.2](https://arxiv.org/html/2502.01456v2#S3.SS2 \"3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")), and introduce other techniques we used (§[3.3](https://arxiv.org/html/2502.01456v2#S3.SS3 \"3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")).\n\n### 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling\n\nWe consider dense rewards from the Implicit PRM because of the scalability. In short, Implicit PRM enables training an ORM with outcome labels only while repurposing it as a PRM at inference. The training stage is the same as standard ORM pipelines, with the only difference being representing the reward as r ϕ​(𝐲):=β​log⁡π ϕ​(𝐲)π ref​(𝐲)r_{\\phi}(\\mathbf{y}):=\\beta\\log\\frac{\\pi_{\\phi}(\\mathbf{y})}{\\pi_{\\text{ref}}(\\mathbf{y})}, where π ϕ\\pi_{\\phi} is the RM and π ref\\pi_{\\text{ref}} is the reference model, both of which are causal LMs. At inference, the process rewards are obtained by:\n\nr ϕ​(y t):=β​log⁡π ϕ​(y t|𝐲<t)π ref​(y t|𝐲<t)r_{\\phi}(y_{t}):=\\beta\\log\\frac{\\pi_{\\phi}(y_{t}|\\mathbf{y}_{<t})}{\\pi_{\\text{ref}}(y_{t}|\\mathbf{y}_{<t})}(3)\n\nIn PRIME, upon rollouts being generated and graded by the (ground truth) outcome verifier, we update the Implicit PRM online with on-policy rollouts and outcome supervision and then calculate token-level dense rewards to estimate advantages, which solves C1 and C2 mentioned in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 \"2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") respectively: (1) To prevent overoptimization and reward hacking, it is crucial to update reward models online. However, updating previous PRMs (Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)) requires annotating step labels on the latest policy rollouts, which is neither efficient nor scalable during online RL. In contrast, the Implicit PRM only demands outcome labels to train due to its special reward representation, and thus it can be easily updated with policy rollouts and outcome labels or rewards, both of which have already been collected to update the policy model.\n\nAlgorithm 1 Process Reinforcement through Implicit Rewards (PRIME)\n\nInput Language model π θ init\\pi_{\\theta_{\\text{init}}}; outcome verifier r o r_{o}; dataset 𝒟\\mathcal{D}; sample number K K; total iteration N N.\n\n1:Initialize policy model\n\nπ θ,π θ old←π θ init\\pi_{\\theta},\\pi_{\\theta_{\\text{old}}}\\leftarrow\\pi_{\\theta_{\\text{init}}}\n, implicit PRM and reference model\n\nπ ϕ,π ref←π θ init\\pi_{\\phi},\\pi_{\\text{ref}}\\leftarrow\\pi_{\\theta_{\\text{init}}}\n\n2:for iteration = 1, …, N do\n\n3: Sample batch of prompts\n\nℬ∼𝒟\\mathcal{B}\\sim\\mathcal{D}\n\n4: Generate\n\nK K\nresponses:\n\n{𝐲 1,…,𝐲 K}∼π θ(⋅|𝐱)\\{\\mathbf{y}^{1},...,\\mathbf{y}^{K}\\}\\sim\\pi_{\\theta}(\\cdot|\\mathbf{x})\nfor\n\n𝐱∈ℬ\\mathbf{x}\\in\\mathcal{B}\n\n5: Compute outcome rewards:\n\nr o​(𝐲 1:K)r_{o}\\left(\\mathbf{y}^{1:K}\\right)\n\n6: Apply accuracy filter (§[3.3](https://arxiv.org/html/2502.01456v2#S3.SS3 \"3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")) on all prompts:\n\n𝒯←Filter​(𝐱,𝐲 1:K,r o​(𝐲 1:K))\\mathcal{T}\\leftarrow\\text{Filter}(\\mathbf{x},\\mathbf{y}^{1:K},r_{o}\\left(\\mathbf{y}^{1:K}\\right))\nfor\n\n𝐱∈ℬ\\mathbf{x}\\in\\mathcal{B}\n\n7: Forward pass\n\nπ ϕ,π ref\\pi_{\\phi},\\pi_{\\text{ref}}\non each\n\n(𝐱,𝐲)∈𝒯(\\mathbf{x},\\mathbf{y})\\in\\mathcal{T}\nto obatin implicit process reward\n\nr ϕ​(y t)r_{\\phi}(y_{t})\nwith Eq.[3](https://arxiv.org/html/2502.01456v2#S3.E3 \"In 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")\n\n8: Update Implicit PRM\n\nπ ϕ\\pi_{\\phi}\nby CE loss on\n\n(𝐱,𝐲,r o​(𝐲))∈𝒯(\\mathbf{x},\\mathbf{y},r_{o}\\left(\\mathbf{y}\\right))\\in\\mathcal{T}\n:\n\nℒ CE​(ϕ)=−𝔼(𝐱,𝐲,r o​(𝐲))∼𝒯​[r o​(𝐲)⋅log⁡σ​(r ϕ​(𝐲))+(1−r o​(𝐲))⋅log⁡(1−σ​(r ϕ​(𝐲)))]\\mathcal{L}_{\\text{CE}}(\\phi)=-\\mathbb{E}_{\\left(\\mathbf{x},\\mathbf{y},r_{o}\\left(\\mathbf{y}\\right)\\right)\\sim\\mathcal{T}}\\left[r_{o}\\left(\\mathbf{y}\\right)\\cdot\\log\\sigma\\left(r_{\\phi}\\left(\\mathbf{y}\\right)\\right)+(1-r_{o}\\left(\\mathbf{y}\\right))\\cdot\\log\\left(1-\\sigma\\left(r_{\\phi}\\left(\\mathbf{y}\\right)\\right)\\right)\\right]\n\n9: Compute advantages\n\nA A\nwith Eq.[5](https://arxiv.org/html/2502.01456v2#S3.E5 \"In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")\n\n10: Update policy\n\nπ θ\\pi_{\\theta}\nby PPO loss in Eq.[6](https://arxiv.org/html/2502.01456v2#S3.E6 \"In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")\n\n11: Update old parameters:\n\nθ old←θ\\theta_{\\text{old}}\\leftarrow\\theta\n\n12:end for\n\nOutput Optimized policy model π θ\\pi_{\\theta}\n\n(2) Unlike common PRMs that produce only step-level rewards, the Implicit PRM provides more fine-grained token-level rewards at no additional cost. This addresses the ambiguity in identifying steps in LLM responses while not introducing extra overhead, making it easy to combine with any RL algorithms for advantage estimation. More discussions on Implicit PRMs are in §[C](https://arxiv.org/html/2502.01456v2#A3 \"Appendix C Discussion on Implicit Process Reward ‣ Process Reinforcement through Implicit Rewards\").\n\n### 3.2 Advantage Estimation and Policy Update\n\nEstimating advantages using Monte Carlo estimator with a leave-one-out baseline. After obtaining token-level dense rewards, we calculate advantages based on either MC estimators or GAE. To determine the advantage function in PRIME, we compare GAE with several MC estimators, including REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), RLOO(Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)), and GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)). Experimental details and results can be found in §[5.3](https://arxiv.org/html/2502.01456v2#S5.SS3 \"5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\nWe find that MC estimators, despite being simpler, are strong enough to produce stable results. Therefore, we choose MC estimate as our advantage function and despite PRIME being compatible with any baseline estimation approaches, we instantiate it with a leave-one-out baseline from K K samples (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)) in this paper, as it performs better in the experiments:\n\nA i=r o​(𝐲 i)−1 K−1​∑j≠i r o​(𝐲 j)A^{i}=r_{o}(\\mathbf{y}^{i})-\\frac{1}{K-1}\\sum_{j\\neq i}r_{o}(\\mathbf{y}^{j})(4)\n\nwhere r o​(𝐲 i)r_{o}(\\mathbf{y}^{i}) denotes the reward of i i-th response, K K is the number of samples for one prompt. The leave-one-out (LOO) baseline helps reduce variances.\n\nMore specifically, we use an Implicit PRM π ϕ\\pi_{\\phi} and an outcome verifier or reward model r o r_{o}. We calculate the return of implicit process rewards and outcome rewards separately if both are available, since directly mixing their values may lead to numerical instability(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)). For implicit process rewards, we perform a three-step process to calculate return: (1) Use the averaged implicit process rewards to calculate the leave-one-out baseline; (2) Normalize the process reward at step t t by subtracting the baseline; (3) Calculate the discounted return for each response. For outcome rewards, we directly adopt LOO without any modification. Finally, the advantage is set to the combination of both returns:\n\nA t i=\\displaystyle A^{i}_{t}=∑s=t|𝐲 i|γ s−t⋅[r ϕ​(y s i)−1 K−1​∑j≠i r ϕ​(𝐲 j)]⏟RLOO with implicit process rewards+r o​(𝐲 i)−1 K−1​∑j≠i r o​(𝐲 j)⏟RLOO with outcome rewards\\displaystyle\\underbrace{\\sum_{s=t}^{|\\mathbf{y}^{i}|}\\gamma^{s-t}\\cdot\\left[r_{\\phi}(y^{i}_{s})-\\frac{1}{K-1}\\sum_{j\\neq i}r_{\\phi}\\left(\\mathbf{y}^{j}\\right)\\right]}_{\\text{RLOO with implicit process rewards}}+\\underbrace{r_{o}\\left(\\mathbf{y}^{i}\\right)-\\frac{1}{K-1}\\sum_{j\\neq i}r_{o}\\left(\\mathbf{y}^{j}\\right)}_{\\text{RLOO with outcome rewards}}(5)\n\nUpdating policy with PPO loss. We adopt PPO clip surrogate loss for more stable policy updates:\n\nL CLIP​(θ)=\\displaystyle L_{\\text{CLIP}}(\\theta)=𝔼 t​[min⁡(π θ​(y t|𝐲<t)π θ old​(y t|𝐲<t)​A t,clip​(π θ​(y t|𝐲<t)π θ old​(y t|𝐲<t),1−ϵ,1+ϵ)​A t)]\\displaystyle\\mathbb{E}_{t}\\Biggl[\\min\\biggl(\\frac{\\pi_{\\theta}(y_{t}|\\mathbf{y}_{<t})}{\\pi_{\\theta_{\\text{old}}}(y_{t}|\\mathbf{y}_{<t})}A_{t},\\text{clip}\\Bigl(\\frac{\\pi_{\\theta}(y_{t}|\\mathbf{y}_{<t})}{\\pi_{\\theta_{\\text{old}}}(y_{t}|\\mathbf{y}_{<t})},1-\\epsilon,1+\\epsilon\\Bigr)A_{t}\\biggr)\\Biggr](6)\n\nwhere ϵ\\epsilon is a clipping parameter. The loss prevents the updated policy from deviating too far from the original distribution, which is the prerequisite of importance sampling.\n\n### 3.3 Other Techniques\n\nInitializing PRM with SFT/base model. In practice, we find that the starting policy model itself serves as a decent initialization of PRM, bypassing the PRM training stage. This solves C3 in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 \"2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") and outperforms a dedicatedly trained PRM, as shown in §[5.1](https://arxiv.org/html/2502.01456v2#S5.SS1 \"5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\nOnline Prompt Filtering. As we sample multiple trajectories for each prompt, we introduce online prompt filtering which filters prompts within a certain accuracy range. This (1) preserves only the prompts within a certain median-level difficulty range(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)) and (2) balances data distribution for the Implicit PRM online training.\n\n![Image 2: Refer to caption](https://arxiv.org/html/2502.01456v2/x2.png)\n\nFigure 2: Effect of online prompt filtering.\n\nWe present the ablation study results in Figure [2](https://arxiv.org/html/2502.01456v2#S3.F2 \"Figure 2 ‣ 3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\") using RLOO with outcome rewards only, from which we can see that the online prompt filter largely lowers the variance of RL training.\n\nHow PRIME addresses challenges in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 \"2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\"). In summary, as illustrated in Figure [1](https://arxiv.org/html/2502.01456v2#S2.F1 \"Figure 1 ‣ 2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") and Algorithm [1](https://arxiv.org/html/2502.01456v2#alg1 \"Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"), PRIME adopts implicit process rewards for efficient PRM online update (C2), then integrates token-level dense rewards with outcome rewards in MC advantage estimate (C1). The PRMs are directly initialized from SFT or base models, which foregoes explicit reward modeling (C3).\n\n4 Experiments\n-------------\n\nWe first perform supervised finetuning on the base model to get a starter model for RL. Please refer to §[D](https://arxiv.org/html/2502.01456v2#A4 \"Appendix D SFT Data & Training Details ‣ Process Reinforcement through Implicit Rewards\") for more details of this stage. All experiments are conducted on 8×\\times A800 GPUs.\n\n### 4.1 RL Settings\n\nRule-based Outcome Verifier. Consistent with recent research that adopts an exact match with ground truth as unhackable rewards(Gao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib9); Lambert et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib20); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)), we define the rule-based ground truth outcome verifiers (OV) for math and coding as follows:\n\nr o math​(𝐲)\\displaystyle r_{o}^{\\text{math}}(\\mathbf{y})={1,matched 0,otherwise r o code​(𝐲)=∑#passes∑#test cases\\displaystyle=\\begin{cases}1,&\\text{matched}\\\\ 0,&\\text{otherwise}\\end{cases}\\quad r_{o}^{\\text{code}}(\\mathbf{y})=\\frac{\\sum\\text{\\#passes}}{\\sum\\text{\\#test cases}}\n\nHyperparameters. We use veRL(Sheng et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib40)) to conduct experiments. By default, we initialize the Implicit PRM with SFT model and retain the SFT model for reference logprobs. For hyperparameters, we use a constant 5×10−7 5\\times 10^{-7} learning rate together with AdamW optimizer for policy model, and use a 10−6 10^{-6} learning rate for PRMs. Both policy and PRMs use a batch size of 256 and micro batchsize of 8. The rollout stage collects 256 prompts and samples 4 responses for each prompt. We set β=0.05\\beta=0.05 for PRM training. We set KL coefficient to 0 in all experiments.\n\nEvaluation Benchmarks. We evaluate on 7 reasoning benchmarks, focusing on competition-level mathematics and programming tasks, including AIME 2024(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23)), AMC(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23)), MATH-500(Hendrycks et al., [2021b](https://arxiv.org/html/2502.01456v2#bib.bib15)), Minerva Math(Lewkowycz et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib22)), OlympiadBench(He et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib13)), LeetCode(Guo et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib11)), and LiveCodeBench (v2)(Jain et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib17)).\n\nTable 1: Detailed results of PRIME and RLOO w/ outcome verifier (OV). At the same 240 steps, the model trained by PRIME is generally better than the model trained by outcome rewards. We also reported avg@16 results in Table[12](https://arxiv.org/html/2502.01456v2#A5.T12 \"Table 12 ‣ E.5 PRM Data ‣ Appendix E RL Data Preprocessing ‣ Process Reinforcement through Implicit Rewards\").\n\n![Image 3: Refer to caption](https://arxiv.org/html/2502.01456v2/x3.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 4: Refer to caption](https://arxiv.org/html/2502.01456v2/x4.png)\n\n(b) Test accuracy across different gradient steps.\n\nFigure 3: The effect of dense reward. We compare PRIME and RLOO with outcome verifier (OV). PRIME leads to 2.5×2.5\\times sample efficiency (wall clock as X axis can be found in Figure[17](https://arxiv.org/html/2502.01456v2#A2.F17 \"Figure 17 ‣ B.6 Comparison with VinePPO ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\")) and 6.9%6.9\\% performance improvement. PRIME also substantially outperforms RLOO on downstream tasks.\n\n### 4.2 Main Results\n\nAs shown in Figure[12](https://arxiv.org/html/2502.01456v2#A2.F12 \"Figure 12 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\") and Table[1](https://arxiv.org/html/2502.01456v2#S4.T1 \"Table 1 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"), Eurus-2-7B-PRIME achieves substantial improvements on key reasoning benchmarks over the SFT version of the model, leading to 15.1% improvement on average, and over 20% on AMC and AIME competitions. Besides, Eurus-2-7B-PRIME achieves 26.7% pass@1 on AIME 2024, surpassing GPT-4o, Llama-3.1-70B-Instruct, and Qwen2.5-Math-7B-Instruct, demonstrating its excellent reasoning ability. Additional results are in §[B](https://arxiv.org/html/2502.01456v2#A2 \"Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\").\n\n### 4.3 Dense Rewards v.s. Sparse Rewards\n\nPerformance. We first validate the effect of PRIME with dense rewards compared to RLOO with outcome rewards only. We train this model for 240 steps. For PRIME, we use the same setting and train the model for 592 steps. We plot the training rewards measured by the outcome verifier and test accuracy in Figure [3](https://arxiv.org/html/2502.01456v2#S4.F3 \"Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"). Compared with sparse reward, PRIME improves the final rewards by 6.9%, with lower variances. On downstream tasks, PRIME also consistently outperforms OV only setup. Detailed results are listed in Table[1](https://arxiv.org/html/2502.01456v2#S4.T1 \"Table 1 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\").\n\nTable 2: Step-wise time cost of PRIME and RLOO.\n\nTraining Efficiency. We provide detailed training time of each training step for PRIME and RLOO in Table[2](https://arxiv.org/html/2502.01456v2#S4.T2 \"Table 2 ‣ 4.3 Dense Rewards v.s. Sparse Rewards ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"). PRIME requires 24%\\% more time cost compared with RLOO. However, as shown in Figure[3](https://arxiv.org/html/2502.01456v2#S4.F3 \"Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"), PRIME only takes 40% of the training steps to achieve the same training rewards as RLOO. This means PRIME would still be 2×\\times more efficient than RLOO when estimated by training time. Additionally, the single controller design of veRL requires no extra GPU memory since all other components (policy model, rollout engine) would be offloaded to CPU during PRM update.\n\n5 Analysis\n----------\n\n![Image 5: Refer to caption](https://arxiv.org/html/2502.01456v2/x5.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 6: Refer to caption](https://arxiv.org/html/2502.01456v2/x6.png)\n\n(b) Test accuracy across different gradient steps.\n\nFigure 4: Comparison of different PRMs. Online PRM initialized from SFT model achieved the best results. However, using PRMs trained on extra rollouts hurts the performance. \n\n### 5.1 Design Choices for the Implicit PRM\n\nThe Implicit PRM is the key component of PRIME, and its design choices greatly affect RL. In this section, we explore two major factors: (1) the initialization model and (2) the update mechanism.\n\n![Image 7: Refer to caption](https://arxiv.org/html/2502.01456v2/x7.png)\n\nFigure 5: Impact of PRM online update. Offline PRM is gradually been overoptimized while online PRMs achieve higher accuracy during training.\n\nSFT model initializes a good PRM. Conventionally, we need to collect data to train RMs and PRMs, and then we can use them in RL. However, the Implicit PRM is a language model, so we can initialize it from any language model with the same tokenizer as the policy model. To investigate whether it is still necessary to train a PRM in advance, we conduct experiments with different PRM initialization strategies: with the SFT model itself and with a specially trained PRM. For the later one, we train EurusPRM from Eurus-2-7B-SFT with additional 500K data generated by Llama3.1 and Qwen2.5 series (data details in §[E.5](https://arxiv.org/html/2502.01456v2#A5.SS5 \"E.5 PRM Data ‣ Appendix E RL Data Preprocessing ‣ Process Reinforcement through Implicit Rewards\")).\n\nWe report the experiment results in Figure[4](https://arxiv.org/html/2502.01456v2#S5.F4 \"Figure 4 ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\"). Surprisingly, directly using Eurus-2-7B-SFT to initialize the PRM greatly outperforms EurusPRM which was trained on more samples. We conjecture that initializing policy model and PRM from the same model largely alleviates the distribution shift issue, as the PRM is only trained on the online rollouts from the policy model.\n\nOnline PRM update is essential. To verify the effect of online PRM update, we pair the correct and wrong samples and calculate the PRM prediction accuracy using r ϕ​(𝐲)r_{\\phi}(\\mathbf{y}). We report the PRM classification accuracy in Figure[5](https://arxiv.org/html/2502.01456v2#S5.F5 \"Figure 5 ‣ 5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\"). The figure clearly shows that, online update mitigates overoptimization and reward hacking. The offline PRM, though starting with high accuracy, gradually drops during RL training procedure due to distribution shift. In contrast, online PRMs that are trained on policy rollouts show the reverse curve.\n\nThis is further validated with training rewards and downstream performance. To breakdown, Eurus-2-7B-SFT is both used as PRM initialization and the reference model in the main experiment, so the PRM is totally trained from scratch, which means the initial PRM outputs zero reward for all tokens. Therefore, Figure[3](https://arxiv.org/html/2502.01456v2#S4.F3 \"Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\") also demonstrates the effect of online PRM update. For EurusPRM initialization, the online run outperforms the offline run as well in Figure[4](https://arxiv.org/html/2502.01456v2#S5.F4 \"Figure 4 ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\n### 5.2 Scaling PRIME with More Compute\n\n![Image 8: Refer to caption](https://arxiv.org/html/2502.01456v2/x8.png)\n\n(a) PRIME training up to 800 steps.\n\n![Image 9: Refer to caption](https://arxiv.org/html/2502.01456v2/x9.png)\n\n(b) PRIME training with 16 rollouts per prompt.\n\nFigure 6: RL training with more training steps (Left) and larger rollout numbers (Right). \n\nTo validate the scalability of PRIME with increased computational resources, we first conduct an extended training process. Specifically, we conduct RL training for 800 rollout steps (3200 gradient steps) with PRIME and RLOO with outcome-reward only. The training results, shown in Figure[6(a)](https://arxiv.org/html/2502.01456v2#S5.F6.sf1 \"In Figure 6 ‣ 5.2 Scaling PRIME with More Compute ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") (Left), reveal that throughout the training, PRIME consistently exhibits stable growth and outperforms the baseline with an improvement of 3.7%. Moreover, we increase the number of responses sampled for each prompt from 4 to 16. The results in Figure[6(a)](https://arxiv.org/html/2502.01456v2#S5.F6.sf1 \"In Figure 6 ‣ 5.2 Scaling PRIME with More Compute ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") (Right) show that PRIME achieves non-trivial improvement of approximately 4.4% compared to RLOO.\n\n### 5.3 PRIME with Other RL Algorithms\n\nAs we stated before, PRIME is equally applicable to other RL algorithms beyond RLOO. In this section, we implement PRIME with REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)), and PPO(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)). Similarly to RLOO, we only modify the advantage estimation functions and leave the clip surrogate loss unchanged. Detailed functions can be found in §[B.3](https://arxiv.org/html/2502.01456v2#A2.SS3 \"B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). From Figure[8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") and Table[4](https://arxiv.org/html/2502.01456v2#A2.T4 \"Table 4 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), We show that PRIME boosts these algorithms on both efficiency and performance as it does with RLOO. PRIME contributes consistently regardless of the policy update method, making it a generic algorithm. It indicates that PRIME is a general plug-in for almost any RL algorithm for LLM., which largely extends the use cases of PRIME.\n\n![Image 10: Refer to caption](https://arxiv.org/html/2502.01456v2/x10.png)\n\nFigure 7: PRIME also generally benefits REINFORCE, GRPO, and PPO.\n\n![Image 11: Refer to caption](https://arxiv.org/html/2502.01456v2/x11.png)\n\nFigure 8: Comparison of value models and process reward models.\n\n### 5.4 Value or Reward, How to Use the Implicit PRM?\n\nBesides using process rewards to estimate returns, we can also employ the Implicit PRM to predict values for advantage estimation in Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\"). Therefore, we compare four variants of MC estimate to determine the best way to incorporate dense supervision. Recall that the Implicit PRM has v ϕ​(𝐲<t+1)=∑i=1 t β​log⁡π ϕ​(y i|𝐲<i)π ref​(y i|𝐲<i)v_{\\phi}(\\mathbf{y}_{<t+1})=\\sum_{i=1}^{t}\\beta\\log\\frac{\\pi_{\\phi}(y_{i}|\\mathbf{y}_{<i})}{\\pi_{\\text{ref}}(y_{i}|\\mathbf{y}_{<i})} with the process reward being r ϕ​(y t)=v ϕ​(𝐲<t+1)−v ϕ​(𝐲<t)r_{\\phi}(y_{t})=v_{\\phi}(\\mathbf{y}_{<t+1})-v_{\\phi}(\\mathbf{y}_{<t}), and we assume a ground-truth outcome verifier r o r_{o}, γ=1\\gamma=1, then we represent the variants as follows:\n\n(1) REINFORCE: A t=r o​(𝐲)A_{t}=r_{o}(\\mathbf{y}). (2) On top of (1), using a linear-head value model V V to calculate the baseline: A t=r o​(𝐲)−V​(𝐲<t)A_{t}=r_{o}(\\mathbf{y})-V(\\mathbf{y}_{<t}). This is the original PPO in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") as we set γ=1\\gamma=1 and λ=1\\lambda=1. (3) On top of (1), using values from the Implicit PRM to serve as the baseline: A t=r o​(𝐲)−v ϕ​(𝐲<t)A_{t}=r_{o}(\\mathbf{y})-v_{\\phi}(\\mathbf{y}_{<t}). This is equivalent to PPO with its value model being replaced by values from the Implicit PRM when γ=1\\gamma=1 and λ=1\\lambda=1. (4) On top of (1), using process rewards from the Implicit PRM to calculate the return: A t=r o​(𝐲)+∑s=t T r ϕ​(y s)A_{t}=r_{o}(\\mathbf{y})+\\sum_{s=t}^{T}r_{\\phi}(y_{s}). This is exactly the REINFORCE w/ PRIME in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\nFigure[8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") reports the results. Comparing PPO and REINFORCE, we find that an additional value model does not benefit policy performance. Notably, using rewards from the Implicit PRM to calculate returns, which is the default setting in PRIME, greatly outperforms all three baselines. This indicates that PRMs work better than value models in RL for LLMs. both two kinds of value models (PPO value model and Implicit PRM as value model) fall behind reward models.\n\n6 Related Work\n--------------\n\nRL for LLM Reasoning. In the area of LLMs, reinforcement learning has been widely used for aligning human preferences(Christiano et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib5); Ouyang et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib32); Cui et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib6)), but the open-source community mostly adopt imitation learning methods(Yuan et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib54); Yue et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib57); Wei et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib50); Liu et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib28)) to enhance the reasoning capabilities of LLMs. Over the past few months, the paradigm gradually shifted. OpenAI o1(Jaech et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib16)) first showed the tremendous potential of large-scale RL for reasoning LLMs, and recent works have verified the scaling effect of RL with outcome rewards(DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7); Team et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib45)). Meanwhile, the role of dense rewards in RL remains underexplored, serving the main focus of PRIME.\n\nImplicit Rewards. Implicit rewards are broadly adopted in LLM alignment(Rafailov et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib33); Chen et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib4); Azar et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib2); Ethayarajh et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib8); Rosset et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib35); Chen et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib3)). Rafailov et al. ([2024](https://arxiv.org/html/2502.01456v2#bib.bib34)) first showed that optimizing DPO objective learns a Q function implicitly. Zhou et al. ([2024](https://arxiv.org/html/2502.01456v2#bib.bib60)) utilized implicit rewards in PPO, and showed the effectiveness of dense implicit rewards. Yuan et al. ([2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)) further extended the conclusion to any loss function optimizing Eq.[3](https://arxiv.org/html/2502.01456v2#S3.E3 \"In 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\").\n\n7 Conclusion\n------------\n\nAs the fuel of LLMs, data, will be depleted in the near future, we are entering a new era of experience, which is exemplified by RL(Sutton, [2019](https://arxiv.org/html/2502.01456v2#bib.bib42)). This work develops PRIME, which produces and leverages dense rewards in online RL for LLM reasoning. Throughout the experiments, we validate that PRIME (1) greatly benefits sample efficiency and policy performance, (2) is easy to use with minimum cost, and (3) is a general method that works with broad RL algorithms together.\n\nEthics Statement\n----------------\n\nThis paper presents PRIME whose goal is to advance the field of reinforcement learning for LLMs. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.\n\nReproducibility Statement\n-------------------------\n\nWe have provided sufficient details to for reproduction, including algorithm pseudocode in Algorithm[1](https://arxiv.org/html/2502.01456v2#alg1 \"Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"), experiment configurations and hyperparameters in Section[4](https://arxiv.org/html/2502.01456v2#S4 \"4 Experiments ‣ Process Reinforcement through Implicit Rewards\") and Appendix. We have upload our code in Supplementary Material.\n\nReferences\n----------\n\n*   Ahmadian et al. (2024) Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce style optimization for learning from human feedback in llms. _arXiv preprint arXiv:2402.14740_, 2024. \n*   Azar et al. (2024) Mohammad Gheshlaghi Azar, Mark Rowland, Bilal Piot, Daniel Guo, Daniele Calandriello, Michal Valko, and Rémi Munos. A general theoretical paradigm to understand learning from human preferences. _International Conference on Artificial Intelligence and Statistics_, abs/2310.12036, 2024. \n*   Chen et al. (2024a) Changyu Chen, Zichen Liu, Chao Du, Tianyu Pang, Qian Liu, Arunesh Sinha, Pradeep Varakantham, and Min Lin. Bootstrapping language models with dpo implicit rewards. _arXiv preprint arXiv:2406.09760_, 2024a. \n*   Chen et al. (2024b) Huayu Chen, Guande He, Lifan Yuan, Ganqu Cui, Hang Su, and Jun Zhu. Noise contrastive alignment of language models with explicit rewards. _arXiv preprint arXiv:2402.05369_, 2024b. \n*   Christiano et al. (2017) Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. _Advances in neural information processing systems_, 30, 2017. \n*   Cui et al. (2024) Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao, Bingxiang He, Wei Zhu, Yuan Ni, Guotong Xie, Ruobing Xie, Yankai Lin, Zhiyuan Liu, and Maosong Sun. Ultrafeedback: Boosting language models with scaled ai feedback. In _ICML_, 2024. \n*   DeepSeek-AI et al. (2025) DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H.Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J.L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R.J. Chen, R.L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S.S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T.Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W.L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y.K. Li, Y.Q. Wang, Y.X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y.X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z.Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948). \n*   Ethayarajh et al. (2024) Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela. Kto: Model alignment as prospect theoretic optimization. _ICML_, 2024. \n*   Gao et al. (2024) Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weiling Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, and Yi Wu. On designing effective rl reward at training time for llm reasoning. _ArXiv_, abs/2410.15115, 2024. \n*   Gao et al. (2022) Leo Gao, John Schulman, and Jacob Hilton. Scaling laws for reward model overoptimization. In _International Conference on Machine Learning_, 2022. \n*   Guo et al. (2024) Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. Deepseek-coder: When the large language model meets programming–the rise of code intelligence. _arXiv preprint arXiv:2401.14196_, 2024. \n*   Haarnoja et al. (2017) Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. Reinforcement learning with deep energy-based policies. In Doina Precup and Yee Whye Teh (eds.), _Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017_, volume 70 of _Proceedings of Machine Learning Research_, pp. 1352–1361. PMLR, 2017. URL [http://proceedings.mlr.press/v70/haarnoja17a.html](http://proceedings.mlr.press/v70/haarnoja17a.html). \n*   He et al. (2024) Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. OlympiadBench: A challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), _Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pp. 3828–3850, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.211. URL [https://aclanthology.org/2024.acl-long.211/](https://aclanthology.org/2024.acl-long.211/). \n*   Hendrycks et al. (2021a) Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, et al. Measuring coding challenge competence with apps. _arXiv preprint arXiv:2105.09938_, 2021a. \n*   Hendrycks et al. (2021b) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. _arXiv preprint arXiv:2103.03874_, 2021b. \n*   Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. _arXiv preprint arXiv:2412.16720_, 2024. \n*   Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. _arXiv preprint arXiv:2403.07974_, 2024. \n*   Kazemnejad et al. (2024) Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron Courville, and Nicolas Le Roux. Vineppo: Unlocking rl potential for llm reasoning through refined credit assignment. _arXiv preprint arXiv:2410.01679_, 2024. \n*   Kool et al. (2019) Wouter Kool, Herke van Hoof, and Max Welling. Buy 4 reinforce samples, get a baseline for free! In _DeepRLStructPred@ICLR_, 2019. URL [https://api.semanticscholar.org/CorpusID:198489118](https://api.semanticscholar.org/CorpusID:198489118). \n*   Lambert et al. (2024) Nathan Lambert, Jacob Daniel Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James Validad Miranda, Alisa Liu, Nouha Dziri, Xinxi Lyu, Yuling Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and Hanna Hajishirzi. Tülu 3: Pushing frontiers in open language model post-training. _ArXiv_, abs/2411.15124, 2024. \n*   Leike et al. (2018) Jan Leike, David Krueger, Tom Everitt, Miljan Martic, Vishal Maini, and Shane Legg. Scalable agent alignment via reward modeling: a research direction. _arXiv preprint arXiv:1811.07871_, 2018. \n*   Lewkowycz et al. (2022) Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems with language models. _Advances in Neural Information Processing Systems_, 35:3843–3857, 2022. \n*   Li et al. (2024) Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Huang, Kashif Rasul, Longhui Yu, Albert Q Jiang, Ziju Shen, et al. Numinamath: The largest public dataset in ai4maths with 860k pairs of competition math problems and solutions. _Hugging Face repository_, 13:9, 2024. \n*   Li et al. (2023) Rongao Li, Jie Fu, Bo-Wen Zhang, Tao Huang, Zhihong Sun, Chen Lyu, Guang Liu, Zhi Jin, and Ge Li. Taco: Topics in algorithmic code generation dataset. _arXiv preprint arXiv:2312.14852_, 2023. \n*   Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d’Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu, and Oriol Vinyals. Competition-level code generation with alphacode. _arXiv preprint arXiv:2203.07814_, 2022. \n*   Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yura Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. _ArXiv_, abs/2305.20050, 2023. \n*   Lin et al. (2024) Zhenghao Lin, Zhibin Gou, Yeyun Gong, Xiao Liu, Yelong Shen, Ruochen Xu, Chen Lin, Yujiu Yang, Jian Jiao, Nan Duan, and Weizhu Chen. Rho-1: Not all tokens are what you need, 2024. \n*   Liu et al. (2024) Zihan Liu, Yang Chen, Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. Acemath: Advancing frontier math reasoning with post-training and reward modeling. _arXiv preprint arXiv:2412.15084_, 2024. \n*   Luo et al. (2025) Michael Luo, Sijun Tan, Justin Wong, Xiaoxiang Shi, William Y. Tang, Manan Roongta, Colin Cai, Jeffrey Luo, Li Erran Li, Raluca Ada Popa, and Ion Stoica. Deepscaler: Surpassing o1-preview with a 1.5b model by scaling rl. [https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2](https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2), 2025. Notion Blog. \n*   Ng et al. (1999) Andrew Y. Ng, Daishi Harada, and Stuart Russell. Policy invariance under reward transformations: Theory and application to reward shaping. In Ivan Bratko and Saso Dzeroski (eds.), _Proceedings of the Sixteenth International Conference on Machine Learning (ICML 1999), Bled, Slovenia, June 27 - 30, 1999_, pp. 278–287. Morgan Kaufmann, 1999. \n*   OpenAI (2024) OpenAI. Openai o1 system card. _ArXiv_, abs/2412.16720, 2024. \n*   Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. _Advances in neural information processing systems_, 35:27730–27744, 2022. \n*   Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. _Advances in Neural Information Processing Systems_, 36, 2023. \n*   Rafailov et al. (2024) Rafael Rafailov, Joey Hejna, Ryan Park, and Chelsea Finn. From r r to q∗q^{*}: Your language model is secretly a q-function. _arXiv preprint arXiv:2404.12358_, 2024. \n*   Rosset et al. (2024) Corby Rosset, Ching-An Cheng, Arindam Mitra, Michael Santacroce, Ahmed Awadallah, and Tengyang Xie. Direct nash optimization: Teaching language models to self-improve with general preferences. _ArXiv_, abs/2404.03715, 2024. \n*   Schulman et al. (2016) John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. In _4th International Conference on Learning Representations, ICLR 2016, San Juan, Puerto Rico, May 2-4, 2016, Conference Track Proceedings_, 2016. \n*   Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_, 2017. \n*   Setlur et al. (2024) Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for llm reasoning. _arXiv preprint arXiv:2410.08146_, 2024. \n*   Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y.Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024. URL [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300). \n*   Sheng et al. (2024) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. _arXiv preprint arXiv: 2409.19256_, 2024. \n*   SkunkworksAI (2024) SkunkworksAI. reasoning-0.01, 2024. \n*   Sutton (2019) Richard Sutton. The bitter lesson. _Incomplete Ideas (blog)_, 13(1):38, 2019. \n*   Sutton (1988) Richard S Sutton. Learning to predict by the methods of temporal differences. _Machine learning_, 3:9–44, 1988. \n*   Sutton & Barto (2018) Richard S Sutton and Andrew G Barto. _Reinforcement learning: An introduction_. MIT press, 2018. \n*   Team et al. (2025) Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. _arXiv preprint arXiv:2501.12599_, 2025. \n*   Team (2024) Qwen Team. Qwq: Reflect deeply on the boundaries of the unknown, November 2024. URL [https://qwenlm.github.io/blog/qwq-32b-preview/](https://qwenlm.github.io/blog/qwq-32b-preview/). \n*   Toshniwal et al. (2024) Shubham Toshniwal, Wei Du, Ivan Moshkov, Branislav Kisacanin, Alexan Ayrapetyan, and Igor Gitman. Openmathinstruct-2: Accelerating ai for math with massive open-source instruction data. _arXiv preprint arXiv:2410.01560_, 2024. \n*   Uesato et al. (2022) Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. _arXiv preprint arXiv:2211.14275_, 2022. \n*   Wang et al. (2023) Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Y.Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. _ArXiv_, abs/2312.08935, 2023. \n*   Wei et al. (2024) Yuxiang Wei, Zhe Wang, Jiawei Liu, Yifeng Ding, and Lingming Zhang. Magicoder: Empowering code generation with oss-instruct. In _Forty-first International Conference on Machine Learning_, 2024. \n*   Williams (1992) Ronald J Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. _Machine learning_, 8:229–256, 1992. \n*   Yang et al. (2024a) An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 technical report. _arXiv preprint arXiv:2412.15115_, 2024a. \n*   Yang et al. (2024b) An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement, 2024b. URL [https://arxiv.org/abs/2409.12122](https://arxiv.org/abs/2409.12122). \n*   Yuan et al. (2024a) Lifan Yuan, Ganqu Cui, Hanbin Wang, Ning Ding, Xingyao Wang, Jia Deng, Boji Shan, Huimin Chen, Ruobing Xie, Yankai Lin, Zhenghao Liu, Bowen Zhou, Hao Peng, Zhiyuan Liu, and Maosong Sun. Advancing llm reasoning generalists with preference trees. _ArXiv_, 2024a. \n*   Yuan et al. (2024b) Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free process rewards without process labels, 2024b. URL [https://arxiv.org/abs/2412.01981](https://arxiv.org/abs/2412.01981). \n*   Yue et al. (2023) Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhu Chen. Mammoth: Building math generalist models through hybrid instruction tuning. _arXiv preprint arXiv:2309.05653_, 2023. \n*   Yue et al. (2024) Xiang Yue, Tuney Zheng, Ge Zhang, and Wenhu Chen. Mammoth2: Scaling instructions from the web. _ArXiv_, abs/2405.03548, 2024. \n*   Zhang et al. (2024) Kaiyan Zhang, Sihang Zeng, Ermo Hua, Ning Ding, Zhang-Ren Chen, Zhiyuan Ma, Haoxin Li, Ganqu Cui, Biqing Qi, Xuekai Zhu, Xingtai Lv, Hu Jinfang, Zhiyuan Liu, and Bowen Zhou. Ultramedical: Building specialized generalists in biomedicine, 2024. \n*   Zheng et al. (2024) Tianyu Zheng, Ge Zhang, Tianhao Shen, Xueling Liu, Bill Yuchen Lin, Jie Fu, Wenhu Chen, and Xiang Yue. Opencodeinterpreter: Integrating code generation with execution and refinement. _arXiv preprint arXiv:2402.14658_, 2024. \n*   Zhou et al. (2024) Zhanhui Zhou, Zhixuan Liu, Jie Liu, Zhichen Dong, Chao Yang, and Yu Qiao. Weak-to-strong search: Align large language models via searching over small language models. _arXiv preprint arXiv:2405.19262_, 2024. \n*   Ziebart et al. (2008) Brian D. Ziebart, Andrew L. Maas, J.Andrew Bagnell, and Anind K. Dey. Maximum entropy inverse reinforcement learning. In Dieter Fox and Carla P. Gomes (eds.), _Proceedings of the Twenty-Third AAAI Conference on Artificial Intelligence, AAAI 2008, Chicago, Illinois, USA, July 13-17, 2008_, pp. 1433–1438. AAAI Press, 2008. URL [http://www.aaai.org/Library/AAAI/2008/aaai08-227.php](http://www.aaai.org/Library/AAAI/2008/aaai08-227.php). \n\nAppendix A Limitations\n----------------------\n\nDue to resource constraints, we only conducted experiments on models up to 32B. Besides the main experiments of PRIME, we ran fewer steps for other ablation experiments, while we conduct comparison under the same step number for fairness.\n\nAppendix B Additional Results\n-----------------------------\n\n### B.1 Reference Model Choice is Flexible\n\n![Image 12: Refer to caption](https://arxiv.org/html/2502.01456v2/figures/images/policy_ref.png)\n\n(a) Policy ref: We use the policy logprob as π ref\\pi_{\\text{ref}} for PRM.\n\n![Image 13: Refer to caption](https://arxiv.org/html/2502.01456v2/figures/images/sfr_ref.png)\n\n(b) SFT ref: We retain the initial policy to provide π ref\\pi_{\\text{ref}} for PRM and KL.\n\nFigure 9: Comparison of different reference policy implementations. One uses the running policy’s old logprobs as reference (policy ref) while the other uses the initial SFT model as the reference model (SFT ref).\n\n![Image 14: Refer to caption](https://arxiv.org/html/2502.01456v2/x12.png)\n\nFigure 10: Different reference model for PRM. We compare two reference model selection strategies for PRIME. Using the policy model as reference and using the initial SFT model as reference. Their rewards are similar.\n\nWe implement two variants of our algorithms to explore the effect of reference model of implicit PRM, one using the initial SFT model as the reference model (SFT ref) while the other using the running policy’s old logprobs as reference (policy ref), as shown in Figure[9(a)](https://arxiv.org/html/2502.01456v2#A2.F9.sf1 \"In Figure 9 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). The policy ref simply adopts the old logprob of the policy model as π ref\\pi_{\\text{ref}}, while the SFT ref remains the initial SFT model for an additional π ref\\pi_{\\text{ref}} calculation. We compare their performance in this section.\n\nFrom the training rewards in Figure [10](https://arxiv.org/html/2502.01456v2#A2.F10 \"Figure 10 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), we find the two strategies are close and have pros and cons in different aspects: The Q value calculated by implicit PRM is the expectation under the distribution of the reference model. So the updating policy could natrually serve as the reference. On the other hand, KL divergence calculation is only allowed when the initial SFT model is retained.\n\n![Image 15: Refer to caption](https://arxiv.org/html/2502.01456v2/x13.png)\n\n(a) PRM classification accuracy on training samples.\n\n![Image 16: Refer to caption](https://arxiv.org/html/2502.01456v2/x14.png)\n\n(b) Training outcome rewards.\n\nFigure 11: Single and double forward. While double forward methods obtain higher accuracy after online update, the two variants achieve similar rewards during training.\n\n### B.2 Single-Forward v.s. Double-Forward\n\nSince our implicit PRM is concurrently updated in training, for each rollout stage, we can update the PRM before the policy model and use the updated PRM to re-calculate the process rewards, which we call the double-forward setting. We investigate the impact of double-forward in both the training and test phases. Our default setting applies single-forward, which uses process rewards from old PRMs. We plot PRM accuracy on rollouts and training rewards in Figure [11](https://arxiv.org/html/2502.01456v2#A2.F11 \"Figure 11 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\").\n\nAccordingly, we find that double-forward could increase PRM accuracy, but the training rewards remain close between the two methods.\n\nTable 3: The comparison of resource requirements between Eurus-2-7B-PRIME and Qwen2.5-Math-7B-Instruct.\n\n### B.3 Results of Different RL Algorithms\n\n![Image 17: Refer to caption](https://arxiv.org/html/2502.01456v2/x15.png)\n\nFigure 12: Overall math performance. Eurus-2-7B-PRIME excels at competition-level mathematics benchmarks, outperforming advanced math models and larger models. Notably, PRIME brings substantial performance gain (+16.7%) over Eurus-2-7B-SFT.\n\nTable 4: Testset results of different RL algorithms.\n\nWe ablate PRIME and different RL algorithms with their variants and find that the PRIME algorithm achieves the best performance for several reasons.\n\nFirst of all, We compare different REINFORCE-like advantage estimators including REINFORCE, GRPO, and RLOO, toggling the existence of implicit process reward. To make different algorithms compatible with the compound of outcome verifier reward and process reward, we accordingly make adaptions similar to Eq. [5](https://arxiv.org/html/2502.01456v2#S3.E5 \"In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"). For GRPO, we have\n\nA t i=r o​(𝐲 i)−mean​(r o​(𝐲 j))std​(r o​(𝐲 j))⏟GRPO with outcome rewards+∑s=t|𝐲 i|γ s−t⋅[r ϕ​(y s i)−mean​(r ϕ​(𝐲 j)|𝐲 j|)std​(r ϕ​(𝐲 j)|𝐲 j|)]⏟GRPO with implicit process rewards.A^{i}_{t}=\\underbrace{\\frac{r_{o}\\left(\\mathbf{y}^{i}\\right)-\\text{mean}(r_{o}\\left(\\mathbf{y}^{j}\\right))}{\\text{std}(r_{o}\\left(\\mathbf{y}^{j}\\right))}}_{\\text{GRPO with outcome rewards}}+\\underbrace{\\sum_{s=t}^{|\\mathbf{y}^{i}|}\\gamma^{s-t}\\cdot\\left[\\frac{r_{\\phi}(y^{i}_{s})-\\text{mean}\\left(\\frac{r_{\\phi}\\left(\\mathbf{y}^{j}\\right)}{|\\mathbf{y}^{j}|}\\right)}{\\text{std}\\left(\\frac{r_{\\phi}\\left(\\mathbf{y}^{j}\\right)}{|\\mathbf{y}^{j}|}\\right)}\\right]}_{\\text{GRPO with implicit process rewards}}.(7)\n\nFor REINFORCE, we have\n\nA t i=r o​(𝐲 i)⏟REINFORCE with outcome rewards+∑s=t|𝐲 i|γ s−t⋅r ϕ​(y s i)⏟REINFORCE with implicit process rewards.A^{i}_{t}=\\underbrace{r_{o}\\left(\\mathbf{y}^{i}\\right)}_{\\text{REINFORCE with outcome rewards}}+\\underbrace{\\sum_{s=t}^{|\\mathbf{y}^{i}|}\\gamma^{s-t}\\cdot r_{\\phi}(y^{i}_{s})}_{\\text{REINFORCE with implicit process rewards}}.(8)\n\nAs shown in Table [4](https://arxiv.org/html/2502.01456v2#A2.T4 \"Table 4 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), PRIME contributes consistently regardless of the policy update method, making it a generic algorithm.\n\nMoreover, the PPO variant of PRIME provides no performance gain, demonstrating that the additional computation cost from the critic model is redundant. This makes it possible to compensate for the expense of the process reward model by using REINFORCE-like algorithms with simpler advantage estimators.\n\nFinally, we choose the best-performing RLOO as the advantage estimator in our algorithm.\n\n### B.4 “Zero” Experiments\n\n![Image 18: Refer to caption](https://arxiv.org/html/2502.01456v2/x16.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 19: Refer to caption](https://arxiv.org/html/2502.01456v2/x17.png)\n\n(b) Math test accuracy across different gradient steps.\n\nFigure 13: “Zero” RL from Qwen2.5-Math-7B. RL from the base model converges way faster than the SFT model, surpassing the instruct version within 32 steps.\n\n![Image 20: Refer to caption](https://arxiv.org/html/2502.01456v2/x18.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 21: Refer to caption](https://arxiv.org/html/2502.01456v2/x19.png)\n\n(b) Math test accuracy across different gradient steps.\n\nFigure 14: “Zero” RL from Qwen2.5-32B-Base. RL from a 32B base model shows more promising gain, surpassing the instruct version within 16 steps. \n\nDeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)) proposed DeepSeek-R1-Zero, which is directly trained from a base model with reinforcement learning. To further investigate the “Zero” setting, we also perform RL from Qwen2.5-Math-7B-Base and Qwen2.5-32B-Base(Yang et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib52)), skipping the SFT phase. We present the experimental results in Figure[13](https://arxiv.org/html/2502.01456v2#A2.F13 \"Figure 13 ‣ B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\") and Figure[14](https://arxiv.org/html/2502.01456v2#A2.F14 \"Figure 14 ‣ B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). The observations are as follows:\n\n(1) RL from base model is suprisingly efficient and effective. Comparing PRIME from Qwen2.5-Math-7B and Eurus-2-7B-SFT, the “Zero” setting converges much faster. This indicates that directly performing RL from a base model might be a strong alternative to the conventional SFT-RL pipeline.\n\n(2) Larger models benefit more. Comparing 7B and 32B models, we see that the 32B model gains more on both training rewards and test performance. This is aligned with the conclusion in DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)).\n\n(3) Saturation could be a potential issue. Although PRIME-Zero obtains impressive performance gain, we find it quickly saturated at a very early stage (about 50 steps), which hinders further improvement like in DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)). This is possibly attributed to the decrease of response diversity, and we leave this as future work.\n\n### B.5 Effect of Reward Model Size\n\nIn the main experiments, we set the reward model to be of the same size as the policy model by default. To further investigate the influence of reward model capacity, we conduct comparative experiments by fixing the policy model as Qwen2.5-7B-Base and varying the reward model among Qwen2.5-3B-Base, Qwen2.5-7B-Base, and Qwen2.5-14B-Base, other settings are aligned with the main experiment. The results are summarized in Table[5](https://arxiv.org/html/2502.01456v2#A2.T5 \"Table 5 ‣ B.5 Effect of Reward Model Size ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). Overall, the results suggest that reward model size has limited influence: the 7B reward model achieves the best average performance, while larger (14B) or smaller (3B) reward models do not yield clear advantages.\n\nTable 5: Performance comparison of different reward models (Qwen2.5-7B-Base as policy model).\n\n### B.6 Comparison with VinePPO\n\nVinePPO(Kazemnejad et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib18)) uses average return across trajectories to estimate the value within policy gradient update, instead of using value model in algorithm like PPO. We adopt the same setting as VinePPO, using RhoMath 1.1B(Lin et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib27)) as the base model and MATH dataset for training. We reproduced PRIME and VinePPO with 8 A800-80G for 96 steps with the same hyperparameters. It reveals that\n\n(1) PRIME is 11x more efficient than VinePPO. As shown in Figure[16](https://arxiv.org/html/2502.01456v2#A2.F16 \"Figure 16 ‣ B.6 Comparison with VinePPO ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), VinePPO takes 13.94 hours for training, while PRIME only needs 1.22 hours.\n\n(2) PRIME also consistently outperforms VinePPO on the validation set. As shown in the Table[6](https://arxiv.org/html/2502.01456v2#A2.T6 \"Table 6 ‣ B.6 Comparison with VinePPO ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), the validation accuracy of PRIME is higher than VinePPO at each validation step.\n\nTable 6: Comparison between PRIME and VinePPO.\n\n![Image 22: Refer to caption](https://arxiv.org/html/2502.01456v2/x20.png)\n\nFigure 15: Validation accuracy curves of PRIME and VinePPO.\n\n![Image 23: Refer to caption](https://arxiv.org/html/2502.01456v2/x21.png)\n\nFigure 16: Training reward curves of PRIME and DeepScaleR.\n\n![Image 24: Refer to caption](https://arxiv.org/html/2502.01456v2/x22.png)\n\nFigure 17: The effect of dense reward. We compared PRIME and RLOO with outcome verifier (OV). The figure depicts training reward curves across wall clock, revealing better sample efficiency of PRIME. \n\n### B.7 Comarison with DeepScaleR\n\nDeepScaleR(Luo et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib29)) introduces a three-stage training pipeline, with maximum allowed response length iteratively increased, from 8k (Stage 1) to 16k (Stage 2), finally to 24k (Stage 3). Through this iterative context lengthening, DeepScaleR achieve continuous performance gain. We run PRIME under the setting of DeepScaleR (base model, data, hyperparameters strictly follow the official settings). Due to resource limits, we only conduct the first (8k) stage training for 330 steps, yet PRIME achieves impressive results.\n\n(1) Model Performance. Figure[16](https://arxiv.org/html/2502.01456v2#A2.F16 \"Figure 16 ‣ B.6 Comparison with VinePPO ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\") presents the training accuracy curves of PRIME and DeepScaleR 1 1 1 Note that the provided training logs are broken according to this [issue](https://github.com/agentica-project/deepscaler/issues/1), so we estimated its training curve from the figure in the blog.. PRIME achieves comparable training accuracy within 330 steps, which is only 1/3 the steps of DeepScaleR stage 1 (1040 steps). On testsets, as shown in Table[7](https://arxiv.org/html/2502.01456v2#A2.T7 \"Table 7 ‣ B.7 Comarison with DeepScaleR ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), PRIME consistently improves the performance of DeepSeek-R1-Distill-Qwen-1.5B by 3.1 points. This validates the effectiveness of PRIME on highly capable base models.\n\n(2) Efficiency. PRIME consumed 446.7 A800 GPU hours for this experiment. In contrast, DeepScaleR consumed 3800 A100 GPU hours in total, and the first stage roughly required ∼\\sim 600 GPU hours. This means PRIME is also 25% faster than DeepScaleR. Note that the advantage could be higher considering hardware differences (A800/A100).\n\n(3) Computation Overhead. Moreover, due to the long response length of the distill model, the overhead would be attributed more to the generation phase, narrowing down the extra time PRIME brings to about 18%. This means that PRIME would be more suitable for long reasoning models.\n\nTable 7: Comparison between PRIME and DeepScaleR.\n\nAppendix C Discussion on Implicit Process Reward\n------------------------------------------------\n\n### C.1 Formulation Validity\n\nAs shown in Yuan et al. ([2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)), implicit process reward is a parameterization of reward modeling. With such parameterization, the expectation of cumulative reward starting from the y t y_{t} (i.e. q-value), q ϕ t​(𝐲<t,y t)=β​log⁡𝔼 π ref​(𝐲|𝐲≤t)​e 1 β​r ϕ​(𝐲)q_{\\phi}^{t}(\\mathbf{y}_{<t},y_{t})=\\beta\\log\\mathbb{E}_{\\pi_{\\text{ref}}(\\mathbf{y}|\\mathbf{y}_{\\leq t})}e^{\\frac{1}{\\beta}r_{\\phi}(\\mathbf{y})} would have closed-formed solution q ϕ t​(𝐲<t,y t)=∑i=1 t β​log⁡π ϕ​(y i|𝐲<i)π ref​(y i|𝐲<i)q_{\\phi}^{t}(\\mathbf{y}_{<t},y_{t})=\\sum_{i=1}^{t}\\beta\\log\\frac{\\pi_{\\phi}(y_{i}|\\mathbf{y}_{<i})}{\\pi_{\\text{ref}}(y_{i}|\\mathbf{y}_{<i})}. Therefore, despite the similarities between implicit process reward formulation to those of DPO(Rafailov et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib33); [2024](https://arxiv.org/html/2502.01456v2#bib.bib34)), it is not derived from the optimal policy of entropy-regularized RL(Ziebart et al., [2008](https://arxiv.org/html/2502.01456v2#bib.bib61); Haarnoja et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib12)).\n\n### C.2 Loss Function\n\nSince π ϕ\\pi_{\\phi} and π ref\\pi_{\\text{ref}} are language models which are inherently self-normalized, using cross-entropy loss brings about a minor issue that the minimum loss 0 cannot be reached. Therefore, the optimal solution would satisfy β​log⁡π ϕ∗​(𝐲)π ref​(𝐲)=r o+c\\beta\\log\\frac{\\pi_{\\phi}^{*}(\\mathbf{y})}{\\pi_{\\text{ref}}(\\mathbf{y})}=r_{o}+c rather than β​log⁡π ϕ∗​(𝐲)π ref​(𝐲)=r o\\beta\\log\\frac{\\pi_{\\phi}^{*}(\\mathbf{y})}{\\pi_{\\text{ref}}(\\mathbf{y})}=r_{o}. This discrepancy would not affect RL, because PRIME uses relative reward, r ϕ​(𝐲 i)−1 K−1​∑j≠i r ϕ​(𝐲 j)r_{\\phi}\\left(\\mathbf{y}^{i}\\right)-\\frac{1}{K-1}\\sum_{j\\neq i}r_{\\phi}\\left(\\mathbf{y}^{j}\\right), rather than the original reward from PRM. This means that even if the bias term is included, it would be canceled out in calculation since the bias term is only related with prompt x x.\n\nTo solve this issue, we can simply eliminate this value term by using the DPO loss. We have a pilot experiment comparing DPO and CE loss, as shown in Table[8](https://arxiv.org/html/2502.01456v2#A3.T8 \"Table 8 ‣ C.2 Loss Function ‣ Appendix C Discussion on Implicit Process Reward ‣ Process Reinforcement through Implicit Rewards\") and Figure[18](https://arxiv.org/html/2502.01456v2#A3.F18 \"Figure 18 ‣ C.2 Loss Function ‣ Appendix C Discussion on Implicit Process Reward ‣ Process Reinforcement through Implicit Rewards\"). DPO and CE achieve similar results, and we chose CE for memory efficiency.\n\nTable 8: Test accuracy of updating PRM with CE or DPO loss after training.\n\n![Image 25: Refer to caption](https://arxiv.org/html/2502.01456v2/x23.png)\n\n(a) Outcome training rewards.\n\n![Image 26: Refer to caption](https://arxiv.org/html/2502.01456v2/x24.png)\n\n(b) Math test accuracy across different gradient steps.\n\nFigure 18: Outcome rewards and test accuracy of updating PRM with DPO or CE loss during training.\n\n### C.3 Reward Shaping\n\nAnother view of PRIME is potential-based reward shaping(Ng et al., [1999](https://arxiv.org/html/2502.01456v2#bib.bib30)). If we view the q-value as the potential function, the process reward exactly satisfies the definition of shaping reward (γ=1\\gamma=1). PBRS does not affect the optimal policy, but does speed up learning, which is aligned with our results.\n\nAppendix D SFT Data & Training Details\n--------------------------------------\n\nTable 9: Actions in action-centric chain-of-thought reasoning framework.\n\nTable 10: Data statistics of SFT data.\n\nTask Dataset Size Avg. Response Length Source\nMath MathInstruct-MATH(Yue et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib56))12715 964.01[https://huggingface.co/datasets/TIGER-Lab/MathInstruct](https://huggingface.co/datasets/TIGER-Lab/MathInstruct)\nOpenMathIns-2-Aug_Math(Toshniwal et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib47))15086 1202.25[https://huggingface.co/datasets/nvidia/OpenMathInstruct-2](https://huggingface.co/datasets/nvidia/OpenMathInstruct-2)\nNumina(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23))55845 1331.61[https://huggingface.co/datasets/AI-MO/NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT)\nReasoning-001(SkunkworksAI, [2024](https://arxiv.org/html/2502.01456v2#bib.bib41))29831 1316.49[https://huggingface.co/datasets/SkunkworksAI/reasoning-0.01](https://huggingface.co/datasets/SkunkworksAI/reasoning-0.01)\nCoding Code-Feedback(Zheng et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib59))27663 1805.16[https://huggingface.co/datasets/m-a-p/Code-Feedback](https://huggingface.co/datasets/m-a-p/Code-Feedback)\nMagicoder(Wei et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib50))24480 1828.72[https://huggingface.co/datasets/ise-uiuc/Magicoder-Evol-Instruct-110K](https://huggingface.co/datasets/ise-uiuc/Magicoder-Evol-Instruct-110K)\nMagicoder-OSS(Wei et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib50))28980 1850.05[https://huggingface.co/datasets/ise-uiuc/Magicoder-OSS-Instruct-75K](https://huggingface.co/datasets/ise-uiuc/Magicoder-OSS-Instruct-75K)\nBiomedicine UltraMedical_mc(Zhang et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib58))35163 891.06[https://huggingface.co/datasets/TsinghuaC3I/UltraMedical](https://huggingface.co/datasets/TsinghuaC3I/UltraMedical)\nTotal / Avg.-229763 1390.75-\n\nWe first performed supervised finetuning for RL preparation. We focus on mathematical and coding problems in this paper. For models, we start with Qwen2.5-Math-7B-Base(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)) for its great mathematical capabilities.\n\nAction-centric chain-of-thought reasoning. We apply imitation learning (supervised finetuning) as a warmup stage to teach models to learn certain reasoning patterns. To this end, we first design an action-centric chain-of-thought reasoning framework. Table [9](https://arxiv.org/html/2502.01456v2#A4.T9 \"Table 9 ‣ Appendix D SFT Data & Training Details ‣ Process Reinforcement through Implicit Rewards\") shows the actions in the action-centric chain-of-thought reasoning framework. When the model generates answers, it conducts multi-step reasoning and chooses one of the 7 actions at each step. The response begins with the ASSESS action and ends with the OUTPUT action.\n\nConstruction of the SFT dataset. To construct the SFT dataset, we collect reasoning instructions from several open-source datasets. It is noteworthy that we did not include many datasets with ground-truth answers in SFT, even though they are of higher quality. However, we reserve them for later RL training. The reason is that we aim to use different datasets for SFT and RL to diversify the exploration in RL, and we consider ground-truth more essential in RL than in SFT. For completion, we employ LLaMA-3.1-70B-Instruct to answer the instructions, with a system prompt requesting the model to perform an action-centric chain-of-thought. Table [10](https://arxiv.org/html/2502.01456v2#A4.T10 \"Table 10 ‣ Appendix D SFT Data & Training Details ‣ Process Reinforcement through Implicit Rewards\") summarizes the key statistics of the datasets used for SFT. The datasets span mathematics, coding, and biomedicine. We finally obtain 230K SFT data and the average response length is 1390 tokens.\n\nSFT Training. During the SFT phase, we conduct full parameter fine-tuning with a learning rate of 1e-05, utilizing the AdamW optimizer alongside a cosine annealing learning rate schedule and a warmup ratio of 0.1. The batch size was set to 96, with a fixed random seed of 42. The model was trained on 230K datasets for 3 epochs.\n\nSFT Results. After finetuning, the performance of our SFT model is reported in Figure[12](https://arxiv.org/html/2502.01456v2#A2.F12 \"Figure 12 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). Compared to baselines, Eurus-2-7B-SFT lags Qwen2.5-Math-7B-Instruct on all mathematics benchmarks.\n\nAppendix E RL Data Preprocessing\n--------------------------------\n\n### E.1 RL Data Collection and Preprocessing\n\nWe curate a high-quality RL training dataset of mathematics and coding problems with outcome verifiers (LaTeX answers for math and test cases for coding). For math, we source from NuminaMath-CoT(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23)), which contains about 860K math problems. The problems span from Chinese high school mathematics to International Mathematical Olympiad competition questions. For coding, we source from APPS(Hendrycks et al., [2021a](https://arxiv.org/html/2502.01456v2#bib.bib14)), CodeContests(Li et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib25)), TACO(Li et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib24)), and Codeforces 2 2 2[https://huggingface.co/datasets/MatrixStudio/Codeforces-Python-Submissions](https://huggingface.co/datasets/MatrixStudio/Codeforces-Python-Submissions). To further increase data quality, we conduct detailed cleaning and filtering. Finally, we retain 457k math problems and 27k coding problems.\n\n### E.2 Data Filtering and Question-Type Classification\n\nThe preprocessing pipeline employs a systematic rule-based approach to filter and classify mathematical problems to create a high-quality dataset with solvable problems, appropriate difficulty levels, and correct solutions. We exclude problems containing figures or diagrams since they require visual processing capabilities. We also remove proof questions due to difficulties in answer verification. Based on specific patterns, the remaining problems are classified into question-answering, multiple-choice, or fill-in-the-blank questions. Since fill-in-the-blank questions comprise less than 400 examples compared to the much larger set of multiple-choice questions, we focus solely on multiple-choice questions for further processing.\n\n### E.3 Converting to Direct Question-Answer Format\n\nWe transform multiple-choice questions into a direct question-answer format through three sequential stages: rule-based filtering, LLM-based filtering, and LLM-based formatting.\n\nWe first identify and remove questions that inherently require multiple-choice options - specifically, those where comparing specific statements or properties is essential to the problem-solving process. These questions cannot be meaningfully converted to a direct question-answer format. The initial filtering employs simple rule-based pattern matching, searching for keywords like ”following” and ”statement” that typically indicate option-dependent problems.\n\nFollowing the rule-based filtering, we employ Llama-3.1-8B-Instruct to perform a more nuanced classification of the remaining questions. Our pilot study revealed that while the LLM occasionally misclassifies questions, it tends to err on the conservative side - marking potentially convertible questions as requiring options rather than the reverse. Given our large dataset, we accepted this conservative approach to maintain quality.\n\nFor questions classified as convertible, we implement a two-phase reformatting process: 1) Question Reformatting: Removing choice indicators and restructuring the question to elicit direct answers. 2) Solution Reformatting: Converting multiple-choice solutions into step-by-step derivations, ensuring all final answers are presented in standard LaTeX boxed format. This systematic approach maintains mathematical rigor while creating a standardized format suitable for downstream applications.\n\n### E.4 Problem and Solution Validation\n\nThe final stage involves merging all question-answer pairs and performing LLM-based comprehensive validation. We identify two key aspects in validation: solvability and correctness.\n\nWe leverage state-of-the-art mathematical reasoning models, including QwQ-32B-Preview(Team, [2024](https://arxiv.org/html/2502.01456v2#bib.bib46)) and Qwen2.5-Math-72B-Instruct(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)), employing a self-consistency approach to determine problem solvability, and if solvable, verify the correctness of solutions provided in the original dataset.\n\nTo enhance validation accuracy, we first analyzed sample problems to identify characteristics of solvable and unsolvable cases and created synthetic unsolvable problems featuring missing conditions or logical contradictions. Based on these samples, we developed specialized prompts to improve the models’ ability to distinguish solvability. Each problem undergoes five independent validation attempts, where the LLM: 1) Provides step-by-step solutions using LaTeX formatting. 2) Identifies unsolvability due to missing conditions or logical contradictions. 3) Generates complete reasoning traces for solvable problems. 4) Presents final answers in standardized LaTeX boxed format (\\boxed{...}). 5) Document any impediments to solution completion.\n\nWe evaluate two key consistency measures across multiple validation attempts: 1) Status Consistency: agreement on problem solvability. 2) Answer Consistency: consistency of solutions across different attempts and agreement between generated solutions and ground truth. The final dataset retains only problems that demonstrate consistent solvability across validation attempts, agreement in solutions across multiple attempts, and alignment with ground truth answers. This rigorous validation process ensures the resulting dataset comprises well-defined, solvable problems with verified, accurate solutions.\n\n### E.5 PRM Data\n\nTable 11: Data statistics of EurusPRM training dataset.\n\nThe dataset statistics of training EurusPRM are shown in Table[11](https://arxiv.org/html/2502.01456v2#A5.T11 \"Table 11 ‣ E.5 PRM Data ‣ Appendix E RL Data Preprocessing ‣ Process Reinforcement through Implicit Rewards\").\n\nTable 12: Avg@16 results with temperature=0.3 of PRIME and RLOO w/ outcome verifier (OV).\n",
    "durationMs": 810,
    "url": "https://huggingface.co/papers/2502.01456"
  },
  "sourceToolAssistantUUID": "1fa6952e-ad8d-4afb-b51b-d2550116a941",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "dec1bf6b-c399-4474-a0c9-7f6db2f12654",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRIME paper on implicit process rewards",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Tool result

_source line 52 · 2026-05-27T15:50:37.751Z_

<details><summary>↩ Tool result · `toolu_016s7avVy8K3tAyVEKRq3NeF`</summary>

```text
# Response

No, this is not the forum page for "Process Reinforcement through Implicit Rewards." 

The webpage displays an error message indicating "The Note rkigcYHFDS was not found," rather than content for the specified paper. The page only shows OpenReview's standard navigation menu and footer information, with no paper title or discussion content visible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb1361ad-95f2-4432-990d-78d4aedd7ff3",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "25e6103a-f568-4314-8e95-a7faf367d8a8",
  "toolUseResult": {
    "bytes": 58573,
    "code": 200,
    "codeText": "OK",
    "result": "# Response\n\nNo, this is not the forum page for \"Process Reinforcement through Implicit Rewards.\" \n\nThe webpage displays an error message indicating \"The Note rkigcYHFDS was not found,\" rather than content for the specified paper. The page only shows OpenReview's standard navigation menu and footer information, with no paper title or discussion content visible.",
    "durationMs": 2121,
    "url": "https://openreview.net/forum?id=rkigcYHFDS"
  },
  "sourceToolAssistantUUID": "eb1361ad-95f2-4432-990d-78d4aedd7ff3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53 · 2026-05-27T15:50:37.754Z_

```json
{
  "parentUuid": "25e6103a-f568-4314-8e95-a7faf367d8a8",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e6cc98f2-f962-4533-b924-c427fe11b170",
  "timestamp": "2026-05-27T15:50:37.754Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 54 · 2026-05-27T15:50:40.727Z_

<details><summary>Logged reasoning block</summary>

```text
The Hugging Face page seems to have the full paper content. Let me read more of it. But I already have extensive content from the arxiv HTML version. Let me also try to find OpenReview reviews one more time with a different approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6cc98f2-f962-4533-b924-c427fe11b170",
  "isSidechain": false,
  "requestId": "req_011CbTLeLjEzj6oEdmhuWnSH",
  "type": "assistant",
  "uuid": "f71cc8bd-c0c8-4333-a12b-daeb8940e669",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oE3xMFKiKxtE3dMc1P1sk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 20657,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 741,
          "output_tokens": 362,
          "cache_read_input_tokens": 20657,
          "cache_creation_input_tokens": 418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 418
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

### Assistant

_source line 55 · 2026-05-27T15:50:41.255Z_

Let me try to get the full paper content from the saved file and also try once more for OpenReview reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f71cc8bd-c0c8-4333-a12b-daeb8940e669",
  "isSidechain": false,
  "requestId": "req_011CbTLeLjEzj6oEdmhuWnSH",
  "type": "assistant",
  "uuid": "07a5caf4-a950-4ad7-9b8f-15d8e1b41b2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oE3xMFKiKxtE3dMc1P1sk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 20657,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 741,
          "output_tokens": 362,
          "cache_read_input_tokens": 20657,
          "cache_creation_input_tokens": 418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 418
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

### Tool call

_source line 56 · 2026-05-27T15:50:42.234Z_

<details open><summary>🔧 Tool call — Read · `toolu_0161LFPHzMdHhNYai6Mz2QVE`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/ae85f63b-06b5-4781-b92e-92dc801697c7/tool-results/toolu_015h9VVLyaxdPfY7ZUe393pK.txt",
  "limit": 300,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07a5caf4-a950-4ad7-9b8f-15d8e1b41b2d",
  "isSidechain": false,
  "requestId": "req_011CbTLeLjEzj6oEdmhuWnSH",
  "type": "assistant",
  "uuid": "b6435a4b-6e25-4684-9e82-0bbc3c183492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oE3xMFKiKxtE3dMc1P1sk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 20657,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 741,
          "output_tokens": 362,
          "cache_read_input_tokens": 20657,
          "cache_creation_input_tokens": 418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 418
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

_source line 57 · 2026-05-27T15:50:42.682Z_

<details><summary>↩ Tool result · `toolu_0161LFPHzMdHhNYai6Mz2QVE`</summary>

```text
0	Title: Process Reinforcement through Implicit Rewards
1	
2	URL Source: https://arxiv.org/html/2502.01456
3	
4	Markdown Content:
5	Ganqu Cui 1,2†, Lifan Yuan 3∗, Zefan Wang 2∗, Hanbin Wang 4∗, Yuchen Zhang 1∗, 
6	
7	Jiacheng Chen 1∗, Wendi Li 2∗, Bingxiang He 2∗, Yuchen Fan 1,5∗, Tianyu Yu 2∗, Qixin Xu 2∗, 
8	
9	Weize Chen 2, Jiarui Yuan 2, Huayu Chen 2, Kaiyan Zhang 2, Xingtai Lv 2, Shuo Wang 2, 
10	
11	Yuan Yao 2, Xu Han 2, Hao Peng 3, Yu Cheng 1,6, Zhiyuan Liu 2, Maosong Sun 2, 
12	
13	Bowen Zhou 1,2, Ning Ding 2†
14	
15	1 Shanghai AI Lab 2 Tsinghua University 3 University of Illinois Urbana-Champaign 
16	
17	4 Peking University 5 Shanghai Jiaotong University 6 CUHK 
18	
19	cuiganqu@pjlab.org.cn lifan4@illinois.edu
20	
21	###### Abstract
22	
23	Dense process rewards have proven a more effective alternative to the sparse outcome-level rewards in the inference-time scaling of large language models (LLMs), particularly in tasks requiring complex multi-step reasoning. While dense rewards also offer an appealing choice for the reinforcement learning (RL) of LLMs since their fine-grained rewards have the potential to address some inherent issues of outcome rewards, such as training efficiency and credit assignment, this potential remains largely unrealized. This can be primarily attributed to the challenges of training process reward models (PRMs) online, where collecting high-quality process labels is prohibitively expensive, making them particularly vulnerable to reward hacking. To address these challenges, we propose PRIME (P rocess R einforcement through IM plicit r E wards), which enables online PRM updates using only policy rollouts and outcome labels through implicit process rewards. PRIME combines well with various advantage functions and forgoes the dedicated reward model training phase that existing approaches require, substantially reducing the development overhead. We demonstrate PRIME’s effectiveness on competitional math and coding. Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement across several key reasoning benchmarks over the SFT model. Notably, our resulting model, Eurus-2-7B-PRIME, surpasses Qwen2.5-Math-7B-Instruct on seven reasoning benchmarks with 10% of its training data.
24	
25	1 Introduction
26	--------------
27	
28	Dense process rewards, which provide feedback at each intermediate step rather than only the whole trajectory, have proven effective in inference-time scaling of large language models (LLMs) on challenging reasoning tasks(Uesato et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib48); Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26); Wang et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib49); Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)). On the training side, they also present superiority in the reinforcement learning (RL) of LLMs, particularly in improving training efficiency(Sutton & Barto, [2018](https://arxiv.org/html/2502.01456v2#bib.bib44)) and credit assignment(Leike et al., [2018](https://arxiv.org/html/2502.01456v2#bib.bib21)) compared with sparse outcome rewards. However, successful applications of dense rewards in RL for LLMs are limited(Setlur et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib38)), as current industry-leading models primarily depend on verifiable outcome rewards and have not yet demonstrated meaningful progress with dense rewards(DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7); Team et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib45)).
29	
30	We identify the central challenge as how to acquire and utilize high-quality dense rewards at scale, which enables online process reward model (PRM) update efficiently. The reason is that, optimizing towards a static reward model eventually leads to overoptimization or reward hacking(Gao et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib10)) due to distribution shift. Ideally, this can be solved by improving the reward model online(Leike et al., [2018](https://arxiv.org/html/2502.01456v2#bib.bib21)). However, acquiring dense process labels for training is prohibitively more expensive. Existing methods either need to build complicated human annotation pipelines(Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)) or rely on estimation-based methods, which require about 10×\times more rollouts for each step than sampling only the response-level trajectories(Wang et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib49); Kazemnejad et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib18)). Neither of them is scalable in online RL. Moreover, to the best of our knowledge, it remains underexplored how to incorporate dense rewards into RL for LLMs.
31	
32	In this work, we propose Process Reinforcement through Implicit Rewards (PRIME), a scalable framework for enhancing reasoning capabilities via efficient reinforcement learning with dense token-level rewards. At its core, the framework employs recently proposed implicit process reward modeling(Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)) to train dense reward models with only outcome-level labels. This enables PRIME to perform online learning of reward signals using only outcome labels on policy rollouts, thereby fundamentally mitigating reward hacking while maintaining the same computational cost as traditional outcome reward models (ORMs). Besides scalability, PRIME also (1) serves as a general method to fuse token-level dense rewards and sparse outcome rewards by calculating their returns separately before summing together, which is compatible with diverse RL algorithms(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51); Kool et al., [2019](https://arxiv.org/html/2502.01456v2#bib.bib19); Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1); Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)); (2) eliminates the dedicated reward modeling stage, which is required by existing works, by simply initializing from the SFT model or even the base model (§[B.4](https://arxiv.org/html/2502.01456v2#A2.SS4 "B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards")). In summary, starting from one single language model, the PRIME framework can efficiently accomplish the generation of dense rewards, the initialization and updating of reward models, as well as the reinforcement learning (RL) training of the policy model.
33	
34	In experiments, we train Qwen2.5-Math-7B-Base(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)) with PRIME after a lightweight SFT warmup stage. Compared to RL using outcome rewards only, PRIME achieves a 2.5×2.5\times sample efficiency gain and a 6.9%6.9\% performance improvements on challenging math problems. As shown in Figure [12](https://arxiv.org/html/2502.01456v2#A2.F12 "Figure 12 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"), through PRIME, we successfully achieve substantial improvement on key mathematical reasoning benchmarks over the SFT model, leading to 16.7% improvement on average, and over 20% on AMC&AIME competitions. Our final model Eurus-2-7B-PRIME surpassed Qwen2.5-Math-7B-Instruct on five key mathematical benchmarks. Notably, this is achieved with only 10%10\% of the data used by Qwen-Math, as in Table [3](https://arxiv.org/html/2502.01456v2#A2.T3 "Table 3 ‣ B.2 Single-Forward v.s. Double-Forward ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards").
35	
36	Our analysis shows that updating the PRM online is key to the success of PRIME (§[5.1](https://arxiv.org/html/2502.01456v2#S5.SS1 "5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards")). We also show that PRIME could generally boost various RL algorithms, including RLOO (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)), REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), PPO(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)), and GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)) (§[5.3](https://arxiv.org/html/2502.01456v2#S5.SS3 "5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards")). In terms of the design choices of advantage estimate, we observe that Implicit PRMs are better to be used as reward models than value models (§[5.4](https://arxiv.org/html/2502.01456v2#S5.SS4 "5.4 Value or Reward, How to Use the Implicit PRM? ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards")).
37	
38	2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards
39	----------------------------------------------------------------------------------
40	
41	Reinforcement Learning (RL) aims to learn an optimal policy π θ\pi_{\theta} that maximizes the expected cumulative discounted reward, namely return, when interacting with an environment. In the context of autoregressive language modeling, state at step t t is the concatenation of prompt 𝐱\mathbf{x} and current response 𝐲<t\mathbf{y}_{<t}, and the action is the t t-th token or step y t y_{t}.
42	
43	### 2.1 RL Preliminaries for LLMs
44	
45	Policy Gradient. Policy gradient is a fundamental algorithm that directly optimizes this objective. Central to this approach is the advantage function A t A_{t}, which quantifies how much better an action is compared to alternatives in a given state:
46	
47	∇θ J​(θ)=𝔼 𝐱∼𝒟,𝐲∼π θ​[∑t=0 T∇θ log⁡π θ​(y t|𝐲<t)​A t]\nabla_{\theta}J(\theta)=\mathbb{E}_{\mathbf{x}\sim\mathcal{D},\mathbf{y}\sim\pi_{\theta}}\left[\sum_{t=0}^{T}\nabla_{\theta}\log\pi_{\theta}(y_{t}|\mathbf{y}_{<t})A_{t}\right](1)
48	
49	where (𝐱,𝐲)\left(\mathbf{x},\mathbf{y}\right) represents a pair of input and output. 𝐱\mathbf{x} is omitted for brevity. In practice, the advantage function is implemented as cumulative discounted rewards subtracting a baseline:
50	
51	A t=∑s=t T γ s−t​r​(y s)−b A_{t}=\sum_{s=t}^{T}\gamma^{s-t}r(y_{s})-b(2)
52	
53	γ∈[0,1]\gamma\in[0,1] is a discount factor that optionally decays future rewards, and r​(y s)r(y_{s}) is the reward provided by the environment at time step s s with x x and 𝐲<s\mathbf{y}_{<s} being omitted in conditions. Eq.[2](https://arxiv.org/html/2502.01456v2#S2.E2 "In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards") is the general formula of the Monte-Carlo (MC) advantage estimate, which indicates that, the high-quality and dense reward at each step is crucial for RL. Different choices of b b include, e.g. directly using values (Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), group average of rewards(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)), and leave-one-out average of rewards (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1); Kool et al., [2019](https://arxiv.org/html/2502.01456v2#bib.bib19)).
54	
55	Value Models. Though the MC estimate is unbiased, it suffers from high variance because of the reliance on all future actions and rewards, which can be random and noisy. Value models, which predict expected accumulated rewards starting from a state, are adopted to help reduce the variance in advantage estimation, such as Generalized Advantage Estimation (GAE;Schulman et al., [2016](https://arxiv.org/html/2502.01456v2#bib.bib36)): A t GAE​(γ,λ)=∑s=0∞(γ​λ)s​δ t+s A_{t}^{\text{GAE}(\gamma,\lambda)}=\sum_{s=0}^{\infty}(\gamma\lambda)^{s}\delta_{t+s}, where δ t=r​(y t)+γ​V​(𝐲<t+1)−V​(𝐲<t)\delta_{t}=r(y_{t})+\gamma V(\mathbf{y}_{<t+1})-V(\mathbf{y}_{<t}) is the temporal difference (TD) error(Sutton, [1988](https://arxiv.org/html/2502.01456v2#bib.bib43)), V V is a value model, and λ\lambda controls the bias-variance tradeoff in advantage estimation. PPO (Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)) is a representative of such actor-critic algorithms that explicitly train a value model along with the policy.
56	
57	Reward Sparsity. Although dense rewards can be naturally integrated into the advantage function through Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 "In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards"), unfortunately, only outcome reward models (ORMs) are available in most practices of LLMs, i.e., only the final token bears a meaningful reward while intermediate tokens receive no rewards(Rafailov et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib33); Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)). In this bandit setting, r​(y t)=0 r(y_{t})=0 for t<T t<T while r​(y T)r(y_{T}) can be non-zero, and Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 "In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards") becomes A=r​(y T)−b A=r(y_{T})-b. This formulation, while simpler, can suffer from reward sparsity issues as the policy receives feedback only at the end of the entire generation. This may (1) encourage spurious solutions with incorrect processes but correct answers, (2) largely reduce sample efficiency in training, and (3) encounter the credit assignment problem(Sutton & Barto, [2018](https://arxiv.org/html/2502.01456v2#bib.bib44)). These drawbacks could be further amplified on complicated tasks, which require more thinking and execution steps, urging the need of dense rewards(Uesato et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib48); Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)). Some may consider employing a value model to mitigate the problem, as it predicts values at every step t t. However, previous work showed that value models may not be able to solve the reward sparsity issue effectively due to training challenges, despite the additional computation overhead(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)). We will also empirically validate this claim in §[5.4](https://arxiv.org/html/2502.01456v2#S5.SS4 "5.4 Value or Reward, How to Use the Implicit PRM? ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards").
58	
59	### 2.2 Key Challenges in Scalable Dense Rewards
60	
61	![Image 1: Refer to caption](https://arxiv.org/html/2502.01456v2/x1.png)
62	
63	Figure 1: Illustration of PRIME. PRIME follows that (1) initialize policy model and the Implicit PRM both with the reference model; (2) sample multiple responses for each prompt and filter with output accuracy; (3) obtain implicit process rewards by the Implicit PRM and update it using cross-entropy (CE) loss; (4) compute advantage and policy loss then update the policy model. 
64	
65	The way to mitigate the reward sparsity problem is to adopt dense reward models, namely PRMs, which score model responses over each token or step. However, it is usually infeasible in practice to incorporate dense rewards into online RL because of three critical challenges in implementation.
66	
67	C1. Process rewards are hard to define. It is difficult to collect step-level labels since reasoning steps do not naturally occur in sequences. Although tokens are easily distinguishable, annotating labels for each token is too costly. Moreover, defining the absolute correctness of intermediate processes as dense rewards can be ambiguous, as some incorrect steps can also positively contribute to the final answer by pruning searching branches (OpenAI, [2024](https://arxiv.org/html/2502.01456v2#bib.bib31); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)).
68	
69	C2. PRM online updates are not scalable. It is crucial to prevent reward overoptimization or reward hacking, which requires the reward model or value model to be updated online along with the policy model(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37); Gao et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib10)). However, training PRMs often requires extensive nuanced step-level annotation, which is infeasible in online RL training. Therefore, this brings about considerable scalability and generalization concerns in dense rewards for RL.
70	
71	C3. Explicit reward modeling brings extra cost. Training reward models requires extensive annotation and broad data coverage to ensure a good balance between adaptability to the policy distribution and generalization to distribution shifts. Hence, the explicit training stage introduces a very costly data collection and an additional training overhead, especially for PRMs which typically require stepwise labels.
72	
73	Notably, DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)) shares similar conclusions and thus is impeded from incorporating PRMs into large-scale RL training.
74	
75	3 PRIME
76	-------
77	
78	To address the above challenges, we propose PRIME, a scalable online RL method with dense rewards. The key insight of PRIME is to apply implicit process rewards, which are derivable from the Implicit PRM that is trained with only outcome labels(Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)). This property enables us to update the PRMs online to avoid reward hacking. We then design a flexible framework to incorporate implicit process rewards with outcome rewards into any kind of MC advantage estimate. PRIME is illustrated in Figure [1](https://arxiv.org/html/2502.01456v2#S2.F1 "Figure 1 ‣ 2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards") and Algorithm [1](https://arxiv.org/html/2502.01456v2#alg1 "Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards"). Next, we will detail the implicit process rewards (§[3.1](https://arxiv.org/html/2502.01456v2#S3.SS1 "3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards")) and how we leverage them to calculate advantages (§[3.2](https://arxiv.org/html/2502.01456v2#S3.SS2 "3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards")), and introduce other techniques we used (§[3.3](https://arxiv.org/html/2502.01456v2#S3.SS3 "3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards")).
79	
80	### 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling
81	
82	We consider dense rewards from the Implicit PRM because of the scalability. In short, Implicit PRM enables training an ORM with outcome labels only while repurposing it as a PRM at inference. The training stage is the same as standard ORM pipelines, with the only difference being representing the reward as r ϕ​(𝐲):=β​log⁡π ϕ​(𝐲)π ref​(𝐲)r_{\phi}(\mathbf{y}):=\beta\log\frac{\pi_{\phi}(\mathbf{y})}{\pi_{\text{ref}}(\mathbf{y})}, where π ϕ\pi_{\phi} is the RM and π ref\pi_{\text{ref}} is the reference model, both of which are causal LMs. At inference, the process rewards are obtained by:
83	
84	r ϕ​(y t):=β​log⁡π ϕ​(y t|𝐲<t)π ref​(y t|𝐲<t)r_{\phi}(y_{t}):=\beta\log\frac{\pi_{\phi}(y_{t}|\mathbf{y}_{<t})}{\pi_{\text{ref}}(y_{t}|\mathbf{y}_{<t})}(3)
85	
86	In PRIME, upon rollouts being generated and graded by the (ground truth) outcome verifier, we update the Implicit PRM online with on-policy rollouts and outcome supervision and then calculate token-level dense rewards to estimate advantages, which solves C1 and C2 mentioned in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 "2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards") respectively: (1) To prevent overoptimization and reward hacking, it is crucial to update reward models online. However, updating previous PRMs (Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)) requires annotating step labels on the latest policy rollouts, which is neither efficient nor scalable during online RL. In contrast, the Implicit PRM only demands outcome labels to train due to its special reward representation, and thus it can be easily updated with policy rollouts and outcome labels or rewards, both of which have already been collected to update the policy model.
87	
88	Algorithm 1 Process Reinforcement through Implicit Rewards (PRIME)
89	
90	Input Language model π θ init\pi_{\theta_{\text{init}}}; outcome verifier r o r_{o}; dataset 𝒟\mathcal{D}; sample number K K; total iteration N N.
91	
92	1:Initialize policy model
93	
94	π θ,π θ old←π θ init\pi_{\theta},\pi_{\theta_{\text{old}}}\leftarrow\pi_{\theta_{\text{init}}}
95	, implicit PRM and reference model
96	
97	π ϕ,π ref←π θ init\pi_{\phi},\pi_{\text{ref}}\leftarrow\pi_{\theta_{\text{init}}}
98	
99	2:for iteration = 1, …, N do
100	
101	3: Sample batch of prompts
102	
103	ℬ∼𝒟\mathcal{B}\sim\mathcal{D}
104	
105	4: Generate
106	
107	K K
108	responses:
109	
110	{𝐲 1,…,𝐲 K}∼π θ(⋅|𝐱)\{\mathbf{y}^{1},...,\mathbf{y}^{K}\}\sim\pi_{\theta}(\cdot|\mathbf{x})
111	for
112	
113	𝐱∈ℬ\mathbf{x}\in\mathcal{B}
114	
115	5: Compute outcome rewards:
116	
117	r o​(𝐲 1:K)r_{o}\left(\mathbf{y}^{1:K}\right)
118	
119	6: Apply accuracy filter (§[3.3](https://arxiv.org/html/2502.01456v2#S3.SS3 "3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards")) on all prompts:
120	
121	𝒯←Filter​(𝐱,𝐲 1:K,r o​(𝐲 1:K))\mathcal{T}\leftarrow\text{Filter}(\mathbf{x},\mathbf{y}^{1:K},r_{o}\left(\mathbf{y}^{1:K}\right))
122	for
123	
124	𝐱∈ℬ\mathbf{x}\in\mathcal{B}
125	
126	7: Forward pass
127	
128	π ϕ,π ref\pi_{\phi},\pi_{\text{ref}}
129	on each
130	
131	(𝐱,𝐲)∈𝒯(\mathbf{x},\mathbf{y})\in\mathcal{T}
132	to obatin implicit process reward
133	
134	r ϕ​(y t)r_{\phi}(y_{t})
135	with Eq.[3](https://arxiv.org/html/2502.01456v2#S3.E3 "In 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards")
136	
137	8: Update Implicit PRM
138	
139	π ϕ\pi_{\phi}
140	by CE loss on
141	
142	(𝐱,𝐲,r o​(𝐲))∈𝒯(\mathbf{x},\mathbf{y},r_{o}\left(\mathbf{y}\right))\in\mathcal{T}
143	:
144	
145	ℒ CE​(ϕ)=−𝔼(𝐱,𝐲,r o​(𝐲))∼𝒯​[r o​(𝐲)⋅log⁡σ​(r ϕ​(𝐲))+(1−r o​(𝐲))⋅log⁡(1−σ​(r ϕ​(𝐲)))]\mathcal{L}_{\text{CE}}(\phi)=-\mathbb{E}_{\left(\mathbf{x},\mathbf{y},r_{o}\left(\mathbf{y}\right)\right)\sim\mathcal{T}}\left[r_{o}\left(\mathbf{y}\right)\cdot\log\sigma\left(r_{\phi}\left(\mathbf{y}\right)\right)+(1-r_{o}\left(\mathbf{y}\right))\cdot\log\left(1-\sigma\left(r_{\phi}\left(\mathbf{y}\right)\right)\right)\right]
146	
147	9: Compute advantages
148	
149	A A
150	with Eq.[5](https://arxiv.org/html/2502.01456v2#S3.E5 "In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards")
151	
152	10: Update policy
153	
154	π θ\pi_{\theta}
155	by PPO loss in Eq.[6](https://arxiv.org/html/2502.01456v2#S3.E6 "In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards")
156	
157	11: Update old parameters:
158	
159	θ old←θ\theta_{\text{old}}\leftarrow\theta
160	
161	12:end for
162	
163	Output Optimized policy model π θ\pi_{\theta}
164	
165	(2) Unlike common PRMs that produce only step-level rewards, the Implicit PRM provides more fine-grained token-level rewards at no additional cost. This addresses the ambiguity in identifying steps in LLM responses while not introducing extra overhead, making it easy to combine with any RL algorithms for advantage estimation. More discussions on Implicit PRMs are in §[C](https://arxiv.org/html/2502.01456v2#A3 "Appendix C Discussion on Implicit Process Reward ‣ Process Reinforcement through Implicit Rewards").
166	
167	### 3.2 Advantage Estimation and Policy Update
168	
169	Estimating advantages using Monte Carlo estimator with a leave-one-out baseline. After obtaining token-level dense rewards, we calculate advantages based on either MC estimators or GAE. To determine the advantage function in PRIME, we compare GAE with several MC estimators, including REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), RLOO(Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)), and GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)). Experimental details and results can be found in §[5.3](https://arxiv.org/html/2502.01456v2#S5.SS3 "5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards").
170	
171	We find that MC estimators, despite being simpler, are strong enough to produce stable results. Therefore, we choose MC estimate as our advantage function and despite PRIME being compatible with any baseline estimation approaches, we instantiate it with a leave-one-out baseline from K K samples (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)) in this paper, as it performs better in the experiments:
172	
173	A i=r o​(𝐲 i)−1 K−1​∑j≠i r o​(𝐲 j)A^{i}=r_{o}(\mathbf{y}^{i})-\frac{1}{K-1}\sum_{j\neq i}r_{o}(\mathbf{y}^{j})(4)
174	
175	where r o​(𝐲 i)r_{o}(\mathbf{y}^{i}) denotes the reward of i i-th response, K K is the number of samples for one prompt. The leave-one-out (LOO) baseline helps reduce variances.
176	
177	More specifically, we use an Implicit PRM π ϕ\pi_{\phi} and an outcome verifier or reward model r o r_{o}. We calculate the return of implicit process rewards and outcome rewards separately if both are available, since directly mixing their values may lead to numerical instability(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)). For implicit process rewards, we perform a three-step process to calculate return: (1) Use the averaged implicit process rewards to calculate the leave-one-out baseline; (2) Normalize the process reward at step t t by subtracting the baseline; (3) Calculate the discounted return for each response. For outcome rewards, we directly adopt LOO without any modification. Finally, the advantage is set to the combination of both returns:
178	
179	A t i=\displaystyle A^{i}_{t}=∑s=t|𝐲 i|γ s−t⋅[r ϕ​(y s i)−1 K−1​∑j≠i r ϕ​(𝐲 j)]⏟RLOO with implicit process rewards+r o​(𝐲 i)−1 K−1​∑j≠i r o​(𝐲 j)⏟RLOO with outcome rewards\displaystyle\underbrace{\sum_{s=t}^{|\mathbf{y}^{i}|}\gamma^{s-t}\cdot\left[r_{\phi}(y^{i}_{s})-\frac{1}{K-1}\sum_{j\neq i}r_{\phi}\left(\mathbf{y}^{j}\right)\right]}_{\text{RLOO with implicit process rewards}}+\underbrace{r_{o}\left(\mathbf{y}^{i}\right)-\frac{1}{K-1}\sum_{j\neq i}r_{o}\left(\mathbf{y}^{j}\right)}_{\text{RLOO with outcome rewards}}(5)
180	
181	Updating policy with PPO loss. We adopt PPO clip surrogate loss for more stable policy updates:
182	
183	L CLIP​(θ)=\displaystyle L_{\text{CLIP}}(\theta)=𝔼 t​[min⁡(π θ​(y t|𝐲<t)π θ old​(y t|𝐲<t)​A t,clip​(π θ​(y t|𝐲<t)π θ old​(y t|𝐲<t),1−ϵ,1+ϵ)​A t)]\displaystyle\mathbb{E}_{t}\Biggl[\min\biggl(\frac{\pi_{\theta}(y_{t}|\mathbf{y}_{<t})}{\pi_{\theta_{\text{old}}}(y_{t}|\mathbf{y}_{<t})}A_{t},\text{clip}\Bigl(\frac{\pi_{\theta}(y_{t}|\mathbf{y}_{<t})}{\pi_{\theta_{\text{old}}}(y_{t}|\mathbf{y}_{<t})},1-\epsilon,1+\epsilon\Bigr)A_{t}\biggr)\Biggr](6)
184	
185	where ϵ\epsilon is a clipping parameter. The loss prevents the updated policy from deviating too far from the original distribution, which is the prerequisite of importance sampling.
186	
187	### 3.3 Other Techniques
188	
189	Initializing PRM with SFT/base model. In practice, we find that the starting policy model itself serves as a decent initialization of PRM, bypassing the PRM training stage. This solves C3 in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 "2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards") and outperforms a dedicatedly trained PRM, as shown in §[5.1](https://arxiv.org/html/2502.01456v2#S5.SS1 "5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards").
190	
191	Online Prompt Filtering. As we sample multiple trajectories for each prompt, we introduce online prompt filtering which filters prompts within a certain accuracy range. This (1) preserves only the prompts within a certain median-level difficulty range(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)) and (2) balances data distribution for the Implicit PRM online training.
192	
193	![Image 2: Refer to caption](https://arxiv.org/html/2502.01456v2/x2.png)
194	
195	Figure 2: Effect of online prompt filtering.
196	
197	We present the ablation study results in Figure [2](https://arxiv.org/html/2502.01456v2#S3.F2 "Figure 2 ‣ 3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards") using RLOO with outcome rewards only, from which we can see that the online prompt filter largely lowers the variance of RL training.
198	
199	How PRIME addresses challenges in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 "2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards"). In summary, as illustrated in Figure [1](https://arxiv.org/html/2502.01456v2#S2.F1 "Figure 1 ‣ 2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards") and Algorithm [1](https://arxiv.org/html/2502.01456v2#alg1 "Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards"), PRIME adopts implicit process rewards for efficient PRM online update (C2), then integrates token-level dense rewards with outcome rewards in MC advantage estimate (C1). The PRMs are directly initialized from SFT or base models, which foregoes explicit reward modeling (C3).
200	
201	4 Experiments
202	-------------
203	
204	We first perform supervised finetuning on the base model to get a starter model for RL. Please refer to §[D](https://arxiv.org/html/2502.01456v2#A4 "Appendix D SFT Data & Training Details ‣ Process Reinforcement through Implicit Rewards") for more details of this stage. All experiments are conducted on 8×\times A800 GPUs.
205	
206	### 4.1 RL Settings
207	
208	Rule-based Outcome Verifier. Consistent with recent research that adopts an exact match with ground truth as unhackable rewards(Gao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib9); Lambert et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib20); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)), we define the rule-based ground truth outcome verifiers (OV) for math and coding as follows:
209	
210	r o math​(𝐲)\displaystyle r_{o}^{\text{math}}(\mathbf{y})={1,matched 0,otherwise r o code​(𝐲)=∑#passes∑#test cases\displaystyle=\begin{cases}1,&\text{matched}\\ 0,&\text{otherwise}\end{cases}\quad r_{o}^{\text{code}}(\mathbf{y})=\frac{\sum\text{\#passes}}{\sum\text{\#test cases}}
211	
212	Hyperparameters. We use veRL(Sheng et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib40)) to conduct experiments. By default, we initialize the Implicit PRM with SFT model and retain the SFT model for reference logprobs. For hyperparameters, we use a constant 5×10−7 5\times 10^{-7} learning rate together with AdamW optimizer for policy model, and use a 10−6 10^{-6} learning rate for PRMs. Both policy and PRMs use a batch size of 256 and micro batchsize of 8. The rollout stage collects 256 prompts and samples 4 responses for each prompt. We set β=0.05\beta=0.05 for PRM training. We set KL coefficient to 0 in all experiments.
213	
214	Evaluation Benchmarks. We evaluate on 7 reasoning benchmarks, focusing on competition-level mathematics and programming tasks, including AIME 2024(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23)), AMC(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23)), MATH-500(Hendrycks et al., [2021b](https://arxiv.org/html/2502.01456v2#bib.bib15)), Minerva Math(Lewkowycz et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib22)), OlympiadBench(He et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib13)), LeetCode(Guo et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib11)), and LiveCodeBench (v2)(Jain et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib17)).
215	
216	Table 1: Detailed results of PRIME and RLOO w/ outcome verifier (OV). At the same 240 steps, the model trained by PRIME is generally better than the model trained by outcome rewards. We also reported avg@16 results in Table[12](https://arxiv.org/html/2502.01456v2#A5.T12 "Table 12 ‣ E.5 PRM Data ‣ Appendix E RL Data Preprocessing ‣ Process Reinforcement through Implicit Rewards").
217	
218	![Image 3: Refer to caption](https://arxiv.org/html/2502.01456v2/x3.png)
219	
220	(a) Outcome training rewards (10-step moving).
221	
222	![Image 4: Refer to caption](https://arxiv.org/html/2502.01456v2/x4.png)
223	
224	(b) Test accuracy across different gradient steps.
225	
226	Figure 3: The effect of dense reward. We compare PRIME and RLOO with outcome verifier (OV). PRIME leads to 2.5×2.5\times sample efficiency (wall clock as X axis can be found in Figure[17](https://arxiv.org/html/2502.01456v2#A2.F17 "Figure 17 ‣ B.6 Comparison with VinePPO ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards")) and 6.9%6.9\% performance improvement. PRIME also substantially outperforms RLOO on downstream tasks.
227	
228	### 4.2 Main Results
229	
230	As shown in Figure[12](https://arxiv.org/html/2502.01456v2#A2.F12 "Figure 12 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards") and Table[1](https://arxiv.org/html/2502.01456v2#S4.T1 "Table 1 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards"), Eurus-2-7B-PRIME achieves substantial improvements on key reasoning benchmarks over the SFT version of the model, leading to 15.1% improvement on average, and over 20% on AMC and AIME competitions. Besides, Eurus-2-7B-PRIME achieves 26.7% pass@1 on AIME 2024, surpassing GPT-4o, Llama-3.1-70B-Instruct, and Qwen2.5-Math-7B-Instruct, demonstrating its excellent reasoning ability. Additional results are in §[B](https://arxiv.org/html/2502.01456v2#A2 "Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards").
231	
232	### 4.3 Dense Rewards v.s. Sparse Rewards
233	
234	Performance. We first validate the effect of PRIME with dense rewards compared to RLOO with outcome rewards only. We train this model for 240 steps. For PRIME, we use the same setting and train the model for 592 steps. We plot the training rewards measured by the outcome verifier and test accuracy in Figure [3](https://arxiv.org/html/2502.01456v2#S4.F3 "Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards"). Compared with sparse reward, PRIME improves the final rewards by 6.9%, with lower variances. On downstream tasks, PRIME also consistently outperforms OV only setup. Detailed results are listed in Table[1](https://arxiv.org/html/2502.01456v2#S4.T1 "Table 1 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards").
235	
236	Table 2: Step-wise time cost of PRIME and RLOO.
237	
238	Training Efficiency. We provide detailed training time of each training step for PRIME and RLOO in Table[2](https://arxiv.org/html/2502.01456v2#S4.T2 "Table 2 ‣ 4.3 Dense Rewards v.s. Sparse Rewards ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards"). PRIME requires 24%\% more time cost compared with RLOO. However, as shown in Figure[3](https://arxiv.org/html/2502.01456v2#S4.F3 "Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards"), PRIME only takes 40% of the training steps to achieve the same training rewards as RLOO. This means PRIME would still be 2×\times more efficient than RLOO when estimated by training time. Additionally, the single controller design of veRL requires no extra GPU memory since all other components (policy model, rollout engine) would be offloaded to CPU during PRM update.
239	
240	5 Analysis
241	----------
242	
243	![Image 5: Refer to caption](https://arxiv.org/html/2502.01456v2/x5.png)
244	
245	(a) Outcome training rewards (10-step moving).
246	
247	![Image 6: Refer to caption](https://arxiv.org/html/2502.01456v2/x6.png)
248	
249	(b) Test accuracy across different gradient steps.
250	
251	Figure 4: Comparison of different PRMs. Online PRM initialized from SFT model achieved the best results. However, using PRMs trained on extra rollouts hurts the performance. 
252	
253	### 5.1 Design Choices for the Implicit PRM
254	
255	The Implicit PRM is the key component of PRIME, and its design choices greatly affect RL. In this section, we explore two major factors: (1) the initialization model and (2) the update mechanism.
256	
257	![Image 7: Refer to caption](https://arxiv.org/html/2502.01456v2/x7.png)
258	
259	Figure 5: Impact of PRM online update. Offline PRM is gradually been overoptimized while online PRMs achieve higher accuracy during training.
260	
261	SFT model initializes a good PRM. Conventionally, we need to collect data to train RMs and PRMs, and then we can use them in RL. However, the Implicit PRM is a language model, so we can initialize it from any language model with the same tokenizer as the policy model. To investigate whether it is still necessary to train a PRM in advance, we conduct experiments with different PRM initialization strategies: with the SFT model itself and with a specially trained PRM. For the later one, we train EurusPRM from Eurus-2-7B-SFT with additional 500K data generated by Llama3.1 and Qwen2.5 series (data details in §[E.5](https://arxiv.org/html/2502.01456v2#A5.SS5 "E.5 PRM Data ‣ Appendix E RL Data Preprocessing ‣ Process Reinforcement through Implicit Rewards")).
262	
263	We report the experiment results in Figure[4](https://arxiv.org/html/2502.01456v2#S5.F4 "Figure 4 ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards"). Surprisingly, directly using Eurus-2-7B-SFT to initialize the PRM greatly outperforms EurusPRM which was trained on more samples. We conjecture that initializing policy model and PRM from the same model largely alleviates the distribution shift issue, as the PRM is only trained on the online rollouts from the policy model.
264	
265	Online PRM update is essential. To verify the effect of online PRM update, we pair the correct and wrong samples and calculate the PRM prediction accuracy using r ϕ​(𝐲)r_{\phi}(\mathbf{y}). We report the PRM classification accuracy in Figure[5](https://arxiv.org/html/2502.01456v2#S5.F5 "Figure 5 ‣ 5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards"). The figure clearly shows that, online update mitigates overoptimization and reward hacking. The offline PRM, though starting with high accuracy, gradually drops during RL training procedure due to distribution shift. In contrast, online PRMs that are trained on policy rollouts show the reverse curve.
266	
267	This is further validated with training rewards and downstream performance. To breakdown, Eurus-2-7B-SFT is both used as PRM initialization and the reference model in the main experiment, so the PRM is totally trained from scratch, which means the initial PRM outputs zero reward for all tokens. Therefore, Figure[3](https://arxiv.org/html/2502.01456v2#S4.F3 "Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards") also demonstrates the effect of online PRM update. For EurusPRM initialization, the online run outperforms the offline run as well in Figure[4](https://arxiv.org/html/2502.01456v2#S5.F4 "Figure 4 ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards").
268	
269	### 5.2 Scaling PRIME with More Compute
270	
271	![Image 8: Refer to caption](https://arxiv.org/html/2502.01456v2/x8.png)
272	
273	(a) PRIME training up to 800 steps.
274	
275	![Image 9: Refer to caption](https://arxiv.org/html/2502.01456v2/x9.png)
276	
277	(b) PRIME training with 16 rollouts per prompt.
278	
279	Figure 6: RL training with more training steps (Left) and larger rollout numbers (Right). 
280	
281	To validate the scalability of PRIME with increased computational resources, we first conduct an extended training process. Specifically, we conduct RL training for 800 rollout steps (3200 gradient steps) with PRIME and RLOO with outcome-reward only. The training results, shown in Figure[6(a)](https://arxiv.org/html/2502.01456v2#S5.F6.sf1 "In Figure 6 ‣ 5.2 Scaling PRIME with More Compute ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards") (Left), reveal that throughout the training, PRIME consistently exhibits stable growth and outperforms the baseline with an improvement of 3.7%. Moreover, we increase the number of responses sampled for each prompt from 4 to 16. The results in Figure[6(a)](https://arxiv.org/html/2502.01456v2#S5.F6.sf1 "In Figure 6 ‣ 5.2 Scaling PRIME with More Compute ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards") (Right) show that PRIME achieves non-trivial improvement of approximately 4.4% compared to RLOO.
282	
283	### 5.3 PRIME with Other RL Algorithms
284	
285	As we stated before, PRIME is equally applicable to other RL algorithms beyond RLOO. In this section, we implement PRIME with REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)), and PPO(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)). Similarly to RLOO, we only modify the advantage estimation functions and leave the clip surrogate loss unchanged. Detailed functions can be found in §[B.3](https://arxiv.org/html/2502.01456v2#A2.SS3 "B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"). From Figure[8](https://arxiv.org/html/2502.01456v2#S5.F8 "Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards") and Table[4](https://arxiv.org/html/2502.01456v2#A2.T4 "Table 4 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"), We show that PRIME boosts these algorithms on both efficiency and performance as it does with RLOO. PRIME contributes consistently regardless of the policy update method, making it a generic algorithm. It indicates that PRIME is a general plug-in for almost any RL algorithm for LLM., which largely extends the use cases of PRIME.
286	
287	![Image 10: Refer to caption](https://arxiv.org/html/2502.01456v2/x10.png)
288	
289	Figure 7: PRIME also generally benefits REINFORCE, GRPO, and PPO.
290	
291	![Image 11: Refer to caption](https://arxiv.org/html/2502.01456v2/x11.png)
292	
293	Figure 8: Comparison of value models and process reward models.
294	
295	### 5.4 Value or Reward, How to Use the Implicit PRM?
296	
297	Besides using process rewards to estimate returns, we can also employ the Implicit PRM to predict values for advantage estimation in Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 "In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards"). Therefore, we compare four variants of MC estimate to determine the best way to incorporate dense supervision. Recall that the Implicit PRM has v ϕ​(𝐲<t+1)=∑i=1 t β​log⁡π ϕ​(y i|𝐲<i)π ref​(y i|𝐲<i)v_{\phi}(\mathbf{y}_{<t+1})=\sum_{i=1}^{t}\beta\log\frac{\pi_{\phi}(y_{i}|\mathbf{y}_{<i})}{\pi_{\text{ref}}(y_{i}|\mathbf{y}_{<i})} with the process reward being r ϕ​(y t)=v ϕ​(𝐲<t+1)−v ϕ​(𝐲<t)r_{\phi}(y_{t})=v_{\phi}(\mathbf{y}_{<t+1})-v_{\phi}(\mathbf{y}_{<t}), and we assume a ground-truth outcome verifier r o r_{o}, γ=1\gamma=1, then we represent the variants as follows:
298	
299	(1) REINFORCE: A t=r o​(𝐲)A_{t}=r_{o}(\mathbf{y}). (2) On top of (1), using a linear-head value model V V to calculate the baseline: A t=r o​(𝐲)−V​(𝐲<t)A_{t}=r_{o}(\mathbf{y})-V(\mathbf{y}_{<t}). This is the original PPO in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 "Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards") as we set γ=1\gamma=1 and λ=1\lambda=1. (3) On top of (1), using values from the Implicit PRM to serve as the baseline: A t=r o​(𝐲)−v ϕ​(𝐲<t)A_{t}=r_{o}(\mathbf{y})-v_{\phi}(\mathbf{y}_{<t}). This is equivalent to PPO with its value model being replaced by values from the Implicit PRM when γ=1\gamma=1 and λ=1\lambda=1. (4) On top of (1), using process rewards from the Implicit PRM to calculate the return: A t=r o​(𝐲)+∑s=t T r ϕ​(y s)A_{t}=r_{o}(\mathbf{y})+\sum_{s=t}^{T}r_{\phi}(y_{s}). This is exactly the REINFORCE w/ PRIME in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 "Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards").
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6435a4b-6e25-4684-9e82-0bbc3c183492",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "62cde64c-29bf-4ba9-8eda-dff105668007",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/ae85f63b-06b5-4781-b92e-92dc801697c7/tool-results/toolu_015h9VVLyaxdPfY7ZUe393pK.txt",
      "content": "Title: Process Reinforcement through Implicit Rewards\n\nURL Source: https://arxiv.org/html/2502.01456\n\nMarkdown Content:\nGanqu Cui 1,2†, Lifan Yuan 3∗, Zefan Wang 2∗, Hanbin Wang 4∗, Yuchen Zhang 1∗, \n\nJiacheng Chen 1∗, Wendi Li 2∗, Bingxiang He 2∗, Yuchen Fan 1,5∗, Tianyu Yu 2∗, Qixin Xu 2∗, \n\nWeize Chen 2, Jiarui Yuan 2, Huayu Chen 2, Kaiyan Zhang 2, Xingtai Lv 2, Shuo Wang 2, \n\nYuan Yao 2, Xu Han 2, Hao Peng 3, Yu Cheng 1,6, Zhiyuan Liu 2, Maosong Sun 2, \n\nBowen Zhou 1,2, Ning Ding 2†\n\n1 Shanghai AI Lab 2 Tsinghua University 3 University of Illinois Urbana-Champaign \n\n4 Peking University 5 Shanghai Jiaotong University 6 CUHK \n\ncuiganqu@pjlab.org.cn lifan4@illinois.edu\n\n###### Abstract\n\nDense process rewards have proven a more effective alternative to the sparse outcome-level rewards in the inference-time scaling of large language models (LLMs), particularly in tasks requiring complex multi-step reasoning. While dense rewards also offer an appealing choice for the reinforcement learning (RL) of LLMs since their fine-grained rewards have the potential to address some inherent issues of outcome rewards, such as training efficiency and credit assignment, this potential remains largely unrealized. This can be primarily attributed to the challenges of training process reward models (PRMs) online, where collecting high-quality process labels is prohibitively expensive, making them particularly vulnerable to reward hacking. To address these challenges, we propose PRIME (P rocess R einforcement through IM plicit r E wards), which enables online PRM updates using only policy rollouts and outcome labels through implicit process rewards. PRIME combines well with various advantage functions and forgoes the dedicated reward model training phase that existing approaches require, substantially reducing the development overhead. We demonstrate PRIME’s effectiveness on competitional math and coding. Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement across several key reasoning benchmarks over the SFT model. Notably, our resulting model, Eurus-2-7B-PRIME, surpasses Qwen2.5-Math-7B-Instruct on seven reasoning benchmarks with 10% of its training data.\n\n1 Introduction\n--------------\n\nDense process rewards, which provide feedback at each intermediate step rather than only the whole trajectory, have proven effective in inference-time scaling of large language models (LLMs) on challenging reasoning tasks(Uesato et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib48); Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26); Wang et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib49); Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)). On the training side, they also present superiority in the reinforcement learning (RL) of LLMs, particularly in improving training efficiency(Sutton & Barto, [2018](https://arxiv.org/html/2502.01456v2#bib.bib44)) and credit assignment(Leike et al., [2018](https://arxiv.org/html/2502.01456v2#bib.bib21)) compared with sparse outcome rewards. However, successful applications of dense rewards in RL for LLMs are limited(Setlur et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib38)), as current industry-leading models primarily depend on verifiable outcome rewards and have not yet demonstrated meaningful progress with dense rewards(DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7); Team et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib45)).\n\nWe identify the central challenge as how to acquire and utilize high-quality dense rewards at scale, which enables online process reward model (PRM) update efficiently. The reason is that, optimizing towards a static reward model eventually leads to overoptimization or reward hacking(Gao et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib10)) due to distribution shift. Ideally, this can be solved by improving the reward model online(Leike et al., [2018](https://arxiv.org/html/2502.01456v2#bib.bib21)). However, acquiring dense process labels for training is prohibitively more expensive. Existing methods either need to build complicated human annotation pipelines(Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)) or rely on estimation-based methods, which require about 10×\\times more rollouts for each step than sampling only the response-level trajectories(Wang et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib49); Kazemnejad et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib18)). Neither of them is scalable in online RL. Moreover, to the best of our knowledge, it remains underexplored how to incorporate dense rewards into RL for LLMs.\n\nIn this work, we propose Process Reinforcement through Implicit Rewards (PRIME), a scalable framework for enhancing reasoning capabilities via efficient reinforcement learning with dense token-level rewards. At its core, the framework employs recently proposed implicit process reward modeling(Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)) to train dense reward models with only outcome-level labels. This enables PRIME to perform online learning of reward signals using only outcome labels on policy rollouts, thereby fundamentally mitigating reward hacking while maintaining the same computational cost as traditional outcome reward models (ORMs). Besides scalability, PRIME also (1) serves as a general method to fuse token-level dense rewards and sparse outcome rewards by calculating their returns separately before summing together, which is compatible with diverse RL algorithms(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51); Kool et al., [2019](https://arxiv.org/html/2502.01456v2#bib.bib19); Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1); Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)); (2) eliminates the dedicated reward modeling stage, which is required by existing works, by simply initializing from the SFT model or even the base model (§[B.4](https://arxiv.org/html/2502.01456v2#A2.SS4 \"B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\")). In summary, starting from one single language model, the PRIME framework can efficiently accomplish the generation of dense rewards, the initialization and updating of reward models, as well as the reinforcement learning (RL) training of the policy model.\n\nIn experiments, we train Qwen2.5-Math-7B-Base(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)) with PRIME after a lightweight SFT warmup stage. Compared to RL using outcome rewards only, PRIME achieves a 2.5×2.5\\times sample efficiency gain and a 6.9%6.9\\% performance improvements on challenging math problems. As shown in Figure [12](https://arxiv.org/html/2502.01456v2#A2.F12 \"Figure 12 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), through PRIME, we successfully achieve substantial improvement on key mathematical reasoning benchmarks over the SFT model, leading to 16.7% improvement on average, and over 20% on AMC&AIME competitions. Our final model Eurus-2-7B-PRIME surpassed Qwen2.5-Math-7B-Instruct on five key mathematical benchmarks. Notably, this is achieved with only 10%10\\% of the data used by Qwen-Math, as in Table [3](https://arxiv.org/html/2502.01456v2#A2.T3 \"Table 3 ‣ B.2 Single-Forward v.s. Double-Forward ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\").\n\nOur analysis shows that updating the PRM online is key to the success of PRIME (§[5.1](https://arxiv.org/html/2502.01456v2#S5.SS1 \"5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\")). We also show that PRIME could generally boost various RL algorithms, including RLOO (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)), REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), PPO(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)), and GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)) (§[5.3](https://arxiv.org/html/2502.01456v2#S5.SS3 \"5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\")). In terms of the design choices of advantage estimate, we observe that Implicit PRMs are better to be used as reward models than value models (§[5.4](https://arxiv.org/html/2502.01456v2#S5.SS4 \"5.4 Value or Reward, How to Use the Implicit PRM? ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\")).\n\n2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards\n----------------------------------------------------------------------------------\n\nReinforcement Learning (RL) aims to learn an optimal policy π θ\\pi_{\\theta} that maximizes the expected cumulative discounted reward, namely return, when interacting with an environment. In the context of autoregressive language modeling, state at step t t is the concatenation of prompt 𝐱\\mathbf{x} and current response 𝐲<t\\mathbf{y}_{<t}, and the action is the t t-th token or step y t y_{t}.\n\n### 2.1 RL Preliminaries for LLMs\n\nPolicy Gradient. Policy gradient is a fundamental algorithm that directly optimizes this objective. Central to this approach is the advantage function A t A_{t}, which quantifies how much better an action is compared to alternatives in a given state:\n\n∇θ J​(θ)=𝔼 𝐱∼𝒟,𝐲∼π θ​[∑t=0 T∇θ log⁡π θ​(y t|𝐲<t)​A t]\\nabla_{\\theta}J(\\theta)=\\mathbb{E}_{\\mathbf{x}\\sim\\mathcal{D},\\mathbf{y}\\sim\\pi_{\\theta}}\\left[\\sum_{t=0}^{T}\\nabla_{\\theta}\\log\\pi_{\\theta}(y_{t}|\\mathbf{y}_{<t})A_{t}\\right](1)\n\nwhere (𝐱,𝐲)\\left(\\mathbf{x},\\mathbf{y}\\right) represents a pair of input and output. 𝐱\\mathbf{x} is omitted for brevity. In practice, the advantage function is implemented as cumulative discounted rewards subtracting a baseline:\n\nA t=∑s=t T γ s−t​r​(y s)−b A_{t}=\\sum_{s=t}^{T}\\gamma^{s-t}r(y_{s})-b(2)\n\nγ∈[0,1]\\gamma\\in[0,1] is a discount factor that optionally decays future rewards, and r​(y s)r(y_{s}) is the reward provided by the environment at time step s s with x x and 𝐲<s\\mathbf{y}_{<s} being omitted in conditions. Eq.[2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") is the general formula of the Monte-Carlo (MC) advantage estimate, which indicates that, the high-quality and dense reward at each step is crucial for RL. Different choices of b b include, e.g. directly using values (Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), group average of rewards(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)), and leave-one-out average of rewards (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1); Kool et al., [2019](https://arxiv.org/html/2502.01456v2#bib.bib19)).\n\nValue Models. Though the MC estimate is unbiased, it suffers from high variance because of the reliance on all future actions and rewards, which can be random and noisy. Value models, which predict expected accumulated rewards starting from a state, are adopted to help reduce the variance in advantage estimation, such as Generalized Advantage Estimation (GAE;Schulman et al., [2016](https://arxiv.org/html/2502.01456v2#bib.bib36)): A t GAE​(γ,λ)=∑s=0∞(γ​λ)s​δ t+s A_{t}^{\\text{GAE}(\\gamma,\\lambda)}=\\sum_{s=0}^{\\infty}(\\gamma\\lambda)^{s}\\delta_{t+s}, where δ t=r​(y t)+γ​V​(𝐲<t+1)−V​(𝐲<t)\\delta_{t}=r(y_{t})+\\gamma V(\\mathbf{y}_{<t+1})-V(\\mathbf{y}_{<t}) is the temporal difference (TD) error(Sutton, [1988](https://arxiv.org/html/2502.01456v2#bib.bib43)), V V is a value model, and λ\\lambda controls the bias-variance tradeoff in advantage estimation. PPO (Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)) is a representative of such actor-critic algorithms that explicitly train a value model along with the policy.\n\nReward Sparsity. Although dense rewards can be naturally integrated into the advantage function through Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\"), unfortunately, only outcome reward models (ORMs) are available in most practices of LLMs, i.e., only the final token bears a meaningful reward while intermediate tokens receive no rewards(Rafailov et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib33); Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)). In this bandit setting, r​(y t)=0 r(y_{t})=0 for t<T t<T while r​(y T)r(y_{T}) can be non-zero, and Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") becomes A=r​(y T)−b A=r(y_{T})-b. This formulation, while simpler, can suffer from reward sparsity issues as the policy receives feedback only at the end of the entire generation. This may (1) encourage spurious solutions with incorrect processes but correct answers, (2) largely reduce sample efficiency in training, and (3) encounter the credit assignment problem(Sutton & Barto, [2018](https://arxiv.org/html/2502.01456v2#bib.bib44)). These drawbacks could be further amplified on complicated tasks, which require more thinking and execution steps, urging the need of dense rewards(Uesato et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib48); Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)). Some may consider employing a value model to mitigate the problem, as it predicts values at every step t t. However, previous work showed that value models may not be able to solve the reward sparsity issue effectively due to training challenges, despite the additional computation overhead(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39); Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)). We will also empirically validate this claim in §[5.4](https://arxiv.org/html/2502.01456v2#S5.SS4 \"5.4 Value or Reward, How to Use the Implicit PRM? ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\n### 2.2 Key Challenges in Scalable Dense Rewards\n\n![Image 1: Refer to caption](https://arxiv.org/html/2502.01456v2/x1.png)\n\nFigure 1: Illustration of PRIME. PRIME follows that (1) initialize policy model and the Implicit PRM both with the reference model; (2) sample multiple responses for each prompt and filter with output accuracy; (3) obtain implicit process rewards by the Implicit PRM and update it using cross-entropy (CE) loss; (4) compute advantage and policy loss then update the policy model. \n\nThe way to mitigate the reward sparsity problem is to adopt dense reward models, namely PRMs, which score model responses over each token or step. However, it is usually infeasible in practice to incorporate dense rewards into online RL because of three critical challenges in implementation.\n\nC1. Process rewards are hard to define. It is difficult to collect step-level labels since reasoning steps do not naturally occur in sequences. Although tokens are easily distinguishable, annotating labels for each token is too costly. Moreover, defining the absolute correctness of intermediate processes as dense rewards can be ambiguous, as some incorrect steps can also positively contribute to the final answer by pruning searching branches (OpenAI, [2024](https://arxiv.org/html/2502.01456v2#bib.bib31); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)).\n\nC2. PRM online updates are not scalable. It is crucial to prevent reward overoptimization or reward hacking, which requires the reward model or value model to be updated online along with the policy model(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37); Gao et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib10)). However, training PRMs often requires extensive nuanced step-level annotation, which is infeasible in online RL training. Therefore, this brings about considerable scalability and generalization concerns in dense rewards for RL.\n\nC3. Explicit reward modeling brings extra cost. Training reward models requires extensive annotation and broad data coverage to ensure a good balance between adaptability to the policy distribution and generalization to distribution shifts. Hence, the explicit training stage introduces a very costly data collection and an additional training overhead, especially for PRMs which typically require stepwise labels.\n\nNotably, DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)) shares similar conclusions and thus is impeded from incorporating PRMs into large-scale RL training.\n\n3 PRIME\n-------\n\nTo address the above challenges, we propose PRIME, a scalable online RL method with dense rewards. The key insight of PRIME is to apply implicit process rewards, which are derivable from the Implicit PRM that is trained with only outcome labels(Yuan et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)). This property enables us to update the PRMs online to avoid reward hacking. We then design a flexible framework to incorporate implicit process rewards with outcome rewards into any kind of MC advantage estimate. PRIME is illustrated in Figure [1](https://arxiv.org/html/2502.01456v2#S2.F1 \"Figure 1 ‣ 2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") and Algorithm [1](https://arxiv.org/html/2502.01456v2#alg1 \"Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"). Next, we will detail the implicit process rewards (§[3.1](https://arxiv.org/html/2502.01456v2#S3.SS1 \"3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")) and how we leverage them to calculate advantages (§[3.2](https://arxiv.org/html/2502.01456v2#S3.SS2 \"3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")), and introduce other techniques we used (§[3.3](https://arxiv.org/html/2502.01456v2#S3.SS3 \"3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")).\n\n### 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling\n\nWe consider dense rewards from the Implicit PRM because of the scalability. In short, Implicit PRM enables training an ORM with outcome labels only while repurposing it as a PRM at inference. The training stage is the same as standard ORM pipelines, with the only difference being representing the reward as r ϕ​(𝐲):=β​log⁡π ϕ​(𝐲)π ref​(𝐲)r_{\\phi}(\\mathbf{y}):=\\beta\\log\\frac{\\pi_{\\phi}(\\mathbf{y})}{\\pi_{\\text{ref}}(\\mathbf{y})}, where π ϕ\\pi_{\\phi} is the RM and π ref\\pi_{\\text{ref}} is the reference model, both of which are causal LMs. At inference, the process rewards are obtained by:\n\nr ϕ​(y t):=β​log⁡π ϕ​(y t|𝐲<t)π ref​(y t|𝐲<t)r_{\\phi}(y_{t}):=\\beta\\log\\frac{\\pi_{\\phi}(y_{t}|\\mathbf{y}_{<t})}{\\pi_{\\text{ref}}(y_{t}|\\mathbf{y}_{<t})}(3)\n\nIn PRIME, upon rollouts being generated and graded by the (ground truth) outcome verifier, we update the Implicit PRM online with on-policy rollouts and outcome supervision and then calculate token-level dense rewards to estimate advantages, which solves C1 and C2 mentioned in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 \"2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") respectively: (1) To prevent overoptimization and reward hacking, it is crucial to update reward models online. However, updating previous PRMs (Lightman et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib26)) requires annotating step labels on the latest policy rollouts, which is neither efficient nor scalable during online RL. In contrast, the Implicit PRM only demands outcome labels to train due to its special reward representation, and thus it can be easily updated with policy rollouts and outcome labels or rewards, both of which have already been collected to update the policy model.\n\nAlgorithm 1 Process Reinforcement through Implicit Rewards (PRIME)\n\nInput Language model π θ init\\pi_{\\theta_{\\text{init}}}; outcome verifier r o r_{o}; dataset 𝒟\\mathcal{D}; sample number K K; total iteration N N.\n\n1:Initialize policy model\n\nπ θ,π θ old←π θ init\\pi_{\\theta},\\pi_{\\theta_{\\text{old}}}\\leftarrow\\pi_{\\theta_{\\text{init}}}\n, implicit PRM and reference model\n\nπ ϕ,π ref←π θ init\\pi_{\\phi},\\pi_{\\text{ref}}\\leftarrow\\pi_{\\theta_{\\text{init}}}\n\n2:for iteration = 1, …, N do\n\n3: Sample batch of prompts\n\nℬ∼𝒟\\mathcal{B}\\sim\\mathcal{D}\n\n4: Generate\n\nK K\nresponses:\n\n{𝐲 1,…,𝐲 K}∼π θ(⋅|𝐱)\\{\\mathbf{y}^{1},...,\\mathbf{y}^{K}\\}\\sim\\pi_{\\theta}(\\cdot|\\mathbf{x})\nfor\n\n𝐱∈ℬ\\mathbf{x}\\in\\mathcal{B}\n\n5: Compute outcome rewards:\n\nr o​(𝐲 1:K)r_{o}\\left(\\mathbf{y}^{1:K}\\right)\n\n6: Apply accuracy filter (§[3.3](https://arxiv.org/html/2502.01456v2#S3.SS3 \"3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")) on all prompts:\n\n𝒯←Filter​(𝐱,𝐲 1:K,r o​(𝐲 1:K))\\mathcal{T}\\leftarrow\\text{Filter}(\\mathbf{x},\\mathbf{y}^{1:K},r_{o}\\left(\\mathbf{y}^{1:K}\\right))\nfor\n\n𝐱∈ℬ\\mathbf{x}\\in\\mathcal{B}\n\n7: Forward pass\n\nπ ϕ,π ref\\pi_{\\phi},\\pi_{\\text{ref}}\non each\n\n(𝐱,𝐲)∈𝒯(\\mathbf{x},\\mathbf{y})\\in\\mathcal{T}\nto obatin implicit process reward\n\nr ϕ​(y t)r_{\\phi}(y_{t})\nwith Eq.[3](https://arxiv.org/html/2502.01456v2#S3.E3 \"In 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")\n\n8: Update Implicit PRM\n\nπ ϕ\\pi_{\\phi}\nby CE loss on\n\n(𝐱,𝐲,r o​(𝐲))∈𝒯(\\mathbf{x},\\mathbf{y},r_{o}\\left(\\mathbf{y}\\right))\\in\\mathcal{T}\n:\n\nℒ CE​(ϕ)=−𝔼(𝐱,𝐲,r o​(𝐲))∼𝒯​[r o​(𝐲)⋅log⁡σ​(r ϕ​(𝐲))+(1−r o​(𝐲))⋅log⁡(1−σ​(r ϕ​(𝐲)))]\\mathcal{L}_{\\text{CE}}(\\phi)=-\\mathbb{E}_{\\left(\\mathbf{x},\\mathbf{y},r_{o}\\left(\\mathbf{y}\\right)\\right)\\sim\\mathcal{T}}\\left[r_{o}\\left(\\mathbf{y}\\right)\\cdot\\log\\sigma\\left(r_{\\phi}\\left(\\mathbf{y}\\right)\\right)+(1-r_{o}\\left(\\mathbf{y}\\right))\\cdot\\log\\left(1-\\sigma\\left(r_{\\phi}\\left(\\mathbf{y}\\right)\\right)\\right)\\right]\n\n9: Compute advantages\n\nA A\nwith Eq.[5](https://arxiv.org/html/2502.01456v2#S3.E5 \"In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")\n\n10: Update policy\n\nπ θ\\pi_{\\theta}\nby PPO loss in Eq.[6](https://arxiv.org/html/2502.01456v2#S3.E6 \"In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\")\n\n11: Update old parameters:\n\nθ old←θ\\theta_{\\text{old}}\\leftarrow\\theta\n\n12:end for\n\nOutput Optimized policy model π θ\\pi_{\\theta}\n\n(2) Unlike common PRMs that produce only step-level rewards, the Implicit PRM provides more fine-grained token-level rewards at no additional cost. This addresses the ambiguity in identifying steps in LLM responses while not introducing extra overhead, making it easy to combine with any RL algorithms for advantage estimation. More discussions on Implicit PRMs are in §[C](https://arxiv.org/html/2502.01456v2#A3 \"Appendix C Discussion on Implicit Process Reward ‣ Process Reinforcement through Implicit Rewards\").\n\n### 3.2 Advantage Estimation and Policy Update\n\nEstimating advantages using Monte Carlo estimator with a leave-one-out baseline. After obtaining token-level dense rewards, we calculate advantages based on either MC estimators or GAE. To determine the advantage function in PRIME, we compare GAE with several MC estimators, including REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), RLOO(Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)), and GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)). Experimental details and results can be found in §[5.3](https://arxiv.org/html/2502.01456v2#S5.SS3 \"5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\nWe find that MC estimators, despite being simpler, are strong enough to produce stable results. Therefore, we choose MC estimate as our advantage function and despite PRIME being compatible with any baseline estimation approaches, we instantiate it with a leave-one-out baseline from K K samples (Ahmadian et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib1)) in this paper, as it performs better in the experiments:\n\nA i=r o​(𝐲 i)−1 K−1​∑j≠i r o​(𝐲 j)A^{i}=r_{o}(\\mathbf{y}^{i})-\\frac{1}{K-1}\\sum_{j\\neq i}r_{o}(\\mathbf{y}^{j})(4)\n\nwhere r o​(𝐲 i)r_{o}(\\mathbf{y}^{i}) denotes the reward of i i-th response, K K is the number of samples for one prompt. The leave-one-out (LOO) baseline helps reduce variances.\n\nMore specifically, we use an Implicit PRM π ϕ\\pi_{\\phi} and an outcome verifier or reward model r o r_{o}. We calculate the return of implicit process rewards and outcome rewards separately if both are available, since directly mixing their values may lead to numerical instability(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)). For implicit process rewards, we perform a three-step process to calculate return: (1) Use the averaged implicit process rewards to calculate the leave-one-out baseline; (2) Normalize the process reward at step t t by subtracting the baseline; (3) Calculate the discounted return for each response. For outcome rewards, we directly adopt LOO without any modification. Finally, the advantage is set to the combination of both returns:\n\nA t i=\\displaystyle A^{i}_{t}=∑s=t|𝐲 i|γ s−t⋅[r ϕ​(y s i)−1 K−1​∑j≠i r ϕ​(𝐲 j)]⏟RLOO with implicit process rewards+r o​(𝐲 i)−1 K−1​∑j≠i r o​(𝐲 j)⏟RLOO with outcome rewards\\displaystyle\\underbrace{\\sum_{s=t}^{|\\mathbf{y}^{i}|}\\gamma^{s-t}\\cdot\\left[r_{\\phi}(y^{i}_{s})-\\frac{1}{K-1}\\sum_{j\\neq i}r_{\\phi}\\left(\\mathbf{y}^{j}\\right)\\right]}_{\\text{RLOO with implicit process rewards}}+\\underbrace{r_{o}\\left(\\mathbf{y}^{i}\\right)-\\frac{1}{K-1}\\sum_{j\\neq i}r_{o}\\left(\\mathbf{y}^{j}\\right)}_{\\text{RLOO with outcome rewards}}(5)\n\nUpdating policy with PPO loss. We adopt PPO clip surrogate loss for more stable policy updates:\n\nL CLIP​(θ)=\\displaystyle L_{\\text{CLIP}}(\\theta)=𝔼 t​[min⁡(π θ​(y t|𝐲<t)π θ old​(y t|𝐲<t)​A t,clip​(π θ​(y t|𝐲<t)π θ old​(y t|𝐲<t),1−ϵ,1+ϵ)​A t)]\\displaystyle\\mathbb{E}_{t}\\Biggl[\\min\\biggl(\\frac{\\pi_{\\theta}(y_{t}|\\mathbf{y}_{<t})}{\\pi_{\\theta_{\\text{old}}}(y_{t}|\\mathbf{y}_{<t})}A_{t},\\text{clip}\\Bigl(\\frac{\\pi_{\\theta}(y_{t}|\\mathbf{y}_{<t})}{\\pi_{\\theta_{\\text{old}}}(y_{t}|\\mathbf{y}_{<t})},1-\\epsilon,1+\\epsilon\\Bigr)A_{t}\\biggr)\\Biggr](6)\n\nwhere ϵ\\epsilon is a clipping parameter. The loss prevents the updated policy from deviating too far from the original distribution, which is the prerequisite of importance sampling.\n\n### 3.3 Other Techniques\n\nInitializing PRM with SFT/base model. In practice, we find that the starting policy model itself serves as a decent initialization of PRM, bypassing the PRM training stage. This solves C3 in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 \"2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") and outperforms a dedicatedly trained PRM, as shown in §[5.1](https://arxiv.org/html/2502.01456v2#S5.SS1 \"5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\nOnline Prompt Filtering. As we sample multiple trajectories for each prompt, we introduce online prompt filtering which filters prompts within a certain accuracy range. This (1) preserves only the prompts within a certain median-level difficulty range(Yang et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib53)) and (2) balances data distribution for the Implicit PRM online training.\n\n![Image 2: Refer to caption](https://arxiv.org/html/2502.01456v2/x2.png)\n\nFigure 2: Effect of online prompt filtering.\n\nWe present the ablation study results in Figure [2](https://arxiv.org/html/2502.01456v2#S3.F2 \"Figure 2 ‣ 3.3 Other Techniques ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\") using RLOO with outcome rewards only, from which we can see that the online prompt filter largely lowers the variance of RL training.\n\nHow PRIME addresses challenges in §[2.2](https://arxiv.org/html/2502.01456v2#S2.SS2 \"2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\"). In summary, as illustrated in Figure [1](https://arxiv.org/html/2502.01456v2#S2.F1 \"Figure 1 ‣ 2.2 Key Challenges in Scalable Dense Rewards ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\") and Algorithm [1](https://arxiv.org/html/2502.01456v2#alg1 \"Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"), PRIME adopts implicit process rewards for efficient PRM online update (C2), then integrates token-level dense rewards with outcome rewards in MC advantage estimate (C1). The PRMs are directly initialized from SFT or base models, which foregoes explicit reward modeling (C3).\n\n4 Experiments\n-------------\n\nWe first perform supervised finetuning on the base model to get a starter model for RL. Please refer to §[D](https://arxiv.org/html/2502.01456v2#A4 \"Appendix D SFT Data & Training Details ‣ Process Reinforcement through Implicit Rewards\") for more details of this stage. All experiments are conducted on 8×\\times A800 GPUs.\n\n### 4.1 RL Settings\n\nRule-based Outcome Verifier. Consistent with recent research that adopts an exact match with ground truth as unhackable rewards(Gao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib9); Lambert et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib20); DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7)), we define the rule-based ground truth outcome verifiers (OV) for math and coding as follows:\n\nr o math​(𝐲)\\displaystyle r_{o}^{\\text{math}}(\\mathbf{y})={1,matched 0,otherwise r o code​(𝐲)=∑#passes∑#test cases\\displaystyle=\\begin{cases}1,&\\text{matched}\\\\ 0,&\\text{otherwise}\\end{cases}\\quad r_{o}^{\\text{code}}(\\mathbf{y})=\\frac{\\sum\\text{\\#passes}}{\\sum\\text{\\#test cases}}\n\nHyperparameters. We use veRL(Sheng et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib40)) to conduct experiments. By default, we initialize the Implicit PRM with SFT model and retain the SFT model for reference logprobs. For hyperparameters, we use a constant 5×10−7 5\\times 10^{-7} learning rate together with AdamW optimizer for policy model, and use a 10−6 10^{-6} learning rate for PRMs. Both policy and PRMs use a batch size of 256 and micro batchsize of 8. The rollout stage collects 256 prompts and samples 4 responses for each prompt. We set β=0.05\\beta=0.05 for PRM training. We set KL coefficient to 0 in all experiments.\n\nEvaluation Benchmarks. We evaluate on 7 reasoning benchmarks, focusing on competition-level mathematics and programming tasks, including AIME 2024(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23)), AMC(Li et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib23)), MATH-500(Hendrycks et al., [2021b](https://arxiv.org/html/2502.01456v2#bib.bib15)), Minerva Math(Lewkowycz et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib22)), OlympiadBench(He et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib13)), LeetCode(Guo et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib11)), and LiveCodeBench (v2)(Jain et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib17)).\n\nTable 1: Detailed results of PRIME and RLOO w/ outcome verifier (OV). At the same 240 steps, the model trained by PRIME is generally better than the model trained by outcome rewards. We also reported avg@16 results in Table[12](https://arxiv.org/html/2502.01456v2#A5.T12 \"Table 12 ‣ E.5 PRM Data ‣ Appendix E RL Data Preprocessing ‣ Process Reinforcement through Implicit Rewards\").\n\n![Image 3: Refer to caption](https://arxiv.org/html/2502.01456v2/x3.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 4: Refer to caption](https://arxiv.org/html/2502.01456v2/x4.png)\n\n(b) Test accuracy across different gradient steps.\n\nFigure 3: The effect of dense reward. We compare PRIME and RLOO with outcome verifier (OV). PRIME leads to 2.5×2.5\\times sample efficiency (wall clock as X axis can be found in Figure[17](https://arxiv.org/html/2502.01456v2#A2.F17 \"Figure 17 ‣ B.6 Comparison with VinePPO ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\")) and 6.9%6.9\\% performance improvement. PRIME also substantially outperforms RLOO on downstream tasks.\n\n### 4.2 Main Results\n\nAs shown in Figure[12](https://arxiv.org/html/2502.01456v2#A2.F12 \"Figure 12 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\") and Table[1](https://arxiv.org/html/2502.01456v2#S4.T1 \"Table 1 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"), Eurus-2-7B-PRIME achieves substantial improvements on key reasoning benchmarks over the SFT version of the model, leading to 15.1% improvement on average, and over 20% on AMC and AIME competitions. Besides, Eurus-2-7B-PRIME achieves 26.7% pass@1 on AIME 2024, surpassing GPT-4o, Llama-3.1-70B-Instruct, and Qwen2.5-Math-7B-Instruct, demonstrating its excellent reasoning ability. Additional results are in §[B](https://arxiv.org/html/2502.01456v2#A2 \"Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\").\n\n### 4.3 Dense Rewards v.s. Sparse Rewards\n\nPerformance. We first validate the effect of PRIME with dense rewards compared to RLOO with outcome rewards only. We train this model for 240 steps. For PRIME, we use the same setting and train the model for 592 steps. We plot the training rewards measured by the outcome verifier and test accuracy in Figure [3](https://arxiv.org/html/2502.01456v2#S4.F3 \"Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"). Compared with sparse reward, PRIME improves the final rewards by 6.9%, with lower variances. On downstream tasks, PRIME also consistently outperforms OV only setup. Detailed results are listed in Table[1](https://arxiv.org/html/2502.01456v2#S4.T1 \"Table 1 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\").\n\nTable 2: Step-wise time cost of PRIME and RLOO.\n\nTraining Efficiency. We provide detailed training time of each training step for PRIME and RLOO in Table[2](https://arxiv.org/html/2502.01456v2#S4.T2 \"Table 2 ‣ 4.3 Dense Rewards v.s. Sparse Rewards ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"). PRIME requires 24%\\% more time cost compared with RLOO. However, as shown in Figure[3](https://arxiv.org/html/2502.01456v2#S4.F3 \"Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\"), PRIME only takes 40% of the training steps to achieve the same training rewards as RLOO. This means PRIME would still be 2×\\times more efficient than RLOO when estimated by training time. Additionally, the single controller design of veRL requires no extra GPU memory since all other components (policy model, rollout engine) would be offloaded to CPU during PRM update.\n\n5 Analysis\n----------\n\n![Image 5: Refer to caption](https://arxiv.org/html/2502.01456v2/x5.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 6: Refer to caption](https://arxiv.org/html/2502.01456v2/x6.png)\n\n(b) Test accuracy across different gradient steps.\n\nFigure 4: Comparison of different PRMs. Online PRM initialized from SFT model achieved the best results. However, using PRMs trained on extra rollouts hurts the performance. \n\n### 5.1 Design Choices for the Implicit PRM\n\nThe Implicit PRM is the key component of PRIME, and its design choices greatly affect RL. In this section, we explore two major factors: (1) the initialization model and (2) the update mechanism.\n\n![Image 7: Refer to caption](https://arxiv.org/html/2502.01456v2/x7.png)\n\nFigure 5: Impact of PRM online update. Offline PRM is gradually been overoptimized while online PRMs achieve higher accuracy during training.\n\nSFT model initializes a good PRM. Conventionally, we need to collect data to train RMs and PRMs, and then we can use them in RL. However, the Implicit PRM is a language model, so we can initialize it from any language model with the same tokenizer as the policy model. To investigate whether it is still necessary to train a PRM in advance, we conduct experiments with different PRM initialization strategies: with the SFT model itself and with a specially trained PRM. For the later one, we train EurusPRM from Eurus-2-7B-SFT with additional 500K data generated by Llama3.1 and Qwen2.5 series (data details in §[E.5](https://arxiv.org/html/2502.01456v2#A5.SS5 \"E.5 PRM Data ‣ Appendix E RL Data Preprocessing ‣ Process Reinforcement through Implicit Rewards\")).\n\nWe report the experiment results in Figure[4](https://arxiv.org/html/2502.01456v2#S5.F4 \"Figure 4 ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\"). Surprisingly, directly using Eurus-2-7B-SFT to initialize the PRM greatly outperforms EurusPRM which was trained on more samples. We conjecture that initializing policy model and PRM from the same model largely alleviates the distribution shift issue, as the PRM is only trained on the online rollouts from the policy model.\n\nOnline PRM update is essential. To verify the effect of online PRM update, we pair the correct and wrong samples and calculate the PRM prediction accuracy using r ϕ​(𝐲)r_{\\phi}(\\mathbf{y}). We report the PRM classification accuracy in Figure[5](https://arxiv.org/html/2502.01456v2#S5.F5 \"Figure 5 ‣ 5.1 Design Choices for the Implicit PRM ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\"). The figure clearly shows that, online update mitigates overoptimization and reward hacking. The offline PRM, though starting with high accuracy, gradually drops during RL training procedure due to distribution shift. In contrast, online PRMs that are trained on policy rollouts show the reverse curve.\n\nThis is further validated with training rewards and downstream performance. To breakdown, Eurus-2-7B-SFT is both used as PRM initialization and the reference model in the main experiment, so the PRM is totally trained from scratch, which means the initial PRM outputs zero reward for all tokens. Therefore, Figure[3](https://arxiv.org/html/2502.01456v2#S4.F3 \"Figure 3 ‣ 4.1 RL Settings ‣ 4 Experiments ‣ Process Reinforcement through Implicit Rewards\") also demonstrates the effect of online PRM update. For EurusPRM initialization, the online run outperforms the offline run as well in Figure[4](https://arxiv.org/html/2502.01456v2#S5.F4 \"Figure 4 ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\n### 5.2 Scaling PRIME with More Compute\n\n![Image 8: Refer to caption](https://arxiv.org/html/2502.01456v2/x8.png)\n\n(a) PRIME training up to 800 steps.\n\n![Image 9: Refer to caption](https://arxiv.org/html/2502.01456v2/x9.png)\n\n(b) PRIME training with 16 rollouts per prompt.\n\nFigure 6: RL training with more training steps (Left) and larger rollout numbers (Right). \n\nTo validate the scalability of PRIME with increased computational resources, we first conduct an extended training process. Specifically, we conduct RL training for 800 rollout steps (3200 gradient steps) with PRIME and RLOO with outcome-reward only. The training results, shown in Figure[6(a)](https://arxiv.org/html/2502.01456v2#S5.F6.sf1 \"In Figure 6 ‣ 5.2 Scaling PRIME with More Compute ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") (Left), reveal that throughout the training, PRIME consistently exhibits stable growth and outperforms the baseline with an improvement of 3.7%. Moreover, we increase the number of responses sampled for each prompt from 4 to 16. The results in Figure[6(a)](https://arxiv.org/html/2502.01456v2#S5.F6.sf1 \"In Figure 6 ‣ 5.2 Scaling PRIME with More Compute ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") (Right) show that PRIME achieves non-trivial improvement of approximately 4.4% compared to RLOO.\n\n### 5.3 PRIME with Other RL Algorithms\n\nAs we stated before, PRIME is equally applicable to other RL algorithms beyond RLOO. In this section, we implement PRIME with REINFORCE(Williams, [1992](https://arxiv.org/html/2502.01456v2#bib.bib51)), GRPO(Shao et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib39)), and PPO(Schulman et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib37)). Similarly to RLOO, we only modify the advantage estimation functions and leave the clip surrogate loss unchanged. Detailed functions can be found in §[B.3](https://arxiv.org/html/2502.01456v2#A2.SS3 \"B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). From Figure[8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") and Table[4](https://arxiv.org/html/2502.01456v2#A2.T4 \"Table 4 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), We show that PRIME boosts these algorithms on both efficiency and performance as it does with RLOO. PRIME contributes consistently regardless of the policy update method, making it a generic algorithm. It indicates that PRIME is a general plug-in for almost any RL algorithm for LLM., which largely extends the use cases of PRIME.\n\n![Image 10: Refer to caption](https://arxiv.org/html/2502.01456v2/x10.png)\n\nFigure 7: PRIME also generally benefits REINFORCE, GRPO, and PPO.\n\n![Image 11: Refer to caption](https://arxiv.org/html/2502.01456v2/x11.png)\n\nFigure 8: Comparison of value models and process reward models.\n\n### 5.4 Value or Reward, How to Use the Implicit PRM?\n\nBesides using process rewards to estimate returns, we can also employ the Implicit PRM to predict values for advantage estimation in Eq. [2](https://arxiv.org/html/2502.01456v2#S2.E2 \"In 2.1 RL Preliminaries for LLMs ‣ 2 Reinforcement Learning for LLMs and the Challenges of Incoporating Dense Rewards ‣ Process Reinforcement through Implicit Rewards\"). Therefore, we compare four variants of MC estimate to determine the best way to incorporate dense supervision. Recall that the Implicit PRM has v ϕ​(𝐲<t+1)=∑i=1 t β​log⁡π ϕ​(y i|𝐲<i)π ref​(y i|𝐲<i)v_{\\phi}(\\mathbf{y}_{<t+1})=\\sum_{i=1}^{t}\\beta\\log\\frac{\\pi_{\\phi}(y_{i}|\\mathbf{y}_{<i})}{\\pi_{\\text{ref}}(y_{i}|\\mathbf{y}_{<i})} with the process reward being r ϕ​(y t)=v ϕ​(𝐲<t+1)−v ϕ​(𝐲<t)r_{\\phi}(y_{t})=v_{\\phi}(\\mathbf{y}_{<t+1})-v_{\\phi}(\\mathbf{y}_{<t}), and we assume a ground-truth outcome verifier r o r_{o}, γ=1\\gamma=1, then we represent the variants as follows:\n\n(1) REINFORCE: A t=r o​(𝐲)A_{t}=r_{o}(\\mathbf{y}). (2) On top of (1), using a linear-head value model V V to calculate the baseline: A t=r o​(𝐲)−V​(𝐲<t)A_{t}=r_{o}(\\mathbf{y})-V(\\mathbf{y}_{<t}). This is the original PPO in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") as we set γ=1\\gamma=1 and λ=1\\lambda=1. (3) On top of (1), using values from the Implicit PRM to serve as the baseline: A t=r o​(𝐲)−v ϕ​(𝐲<t)A_{t}=r_{o}(\\mathbf{y})-v_{\\phi}(\\mathbf{y}_{<t}). This is equivalent to PPO with its value model being replaced by values from the Implicit PRM when γ=1\\gamma=1 and λ=1\\lambda=1. (4) On top of (1), using process rewards from the Implicit PRM to calculate the return: A t=r o​(𝐲)+∑s=t T r ϕ​(y s)A_{t}=r_{o}(\\mathbf{y})+\\sum_{s=t}^{T}r_{\\phi}(y_{s}). This is exactly the REINFORCE w/ PRIME in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").",
      "numLines": 300,
      "startLine": 0,
      "totalLines": 626
    }
  },
  "sourceToolAssistantUUID": "b6435a4b-6e25-4684-9e82-0bbc3c183492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-27T15:50:43.811Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V8dinDALVKUxA5ifdifE3g`</summary>

```json
{
  "url": "https://api.openreview.net/notes?content.title=Process+Reinforcement+through+Implicit+Rewards&domain=ICLR.cc/2025/Conference",
  "prompt": "Return the full JSON response including any paper IDs or forum IDs for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62cde64c-29bf-4ba9-8eda-dff105668007",
  "isSidechain": false,
  "requestId": "req_011CbTLeLjEzj6oEdmhuWnSH",
  "type": "assistant",
  "uuid": "e0b8b04c-3024-4d17-9df6-2646c37ee71d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oE3xMFKiKxtE3dMc1P1sk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 741,
      "cache_creation_input_tokens": 418,
      "cache_read_input_tokens": 20657,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 741,
          "output_tokens": 362,
          "cache_read_input_tokens": 20657,
          "cache_creation_input_tokens": 418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 418
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

_source line 59 · 2026-05-27T15:50:43.976Z_

<details><summary>↩ Tool result · `toolu_01V8dinDALVKUxA5ifdifE3g`</summary>

```text
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0b8b04c-3024-4d17-9df6-2646c37ee71d",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "54371c59-0c44-4e1a-9048-85577ca63191",
  "toolUseResult": {
    "bytes": 0,
    "code": 400,
    "codeText": "Bad Request",
    "result": "The server returned HTTP 400 Bad Request.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 162,
    "url": "https://api.openreview.net/notes?content.title=Process+Reinforcement+through+Implicit+Rewards&domain=ICLR.cc/2025/Conference"
  },
  "sourceToolAssistantUUID": "e0b8b04c-3024-4d17-9df6-2646c37ee71d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "54371c59-0c44-4e1a-9048-85577ca63191",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRIME paper on implicit process rewards",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Tool call

_source line 62 · 2026-05-27T15:50:49.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MfLvDRH8miekryo1KVaXxp`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/ae85f63b-06b5-4781-b92e-92dc801697c7/tool-results/toolu_015h9VVLyaxdPfY7ZUe393pK.txt",
  "limit": 200,
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54371c59-0c44-4e1a-9048-85577ca63191",
  "isSidechain": false,
  "requestId": "req_011CbTLeoNNNzd1DkVB7E4Zt",
  "type": "assistant",
  "uuid": "7647de9d-99a4-45f9-bd3b-9cb01c9d65eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TX5U2vYsDokDgCJz9Gk4n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17438,
      "cache_read_input_tokens": 21075,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 21075,
          "cache_creation_input_tokens": 17438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17438
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

_source line 63 · 2026-05-27T15:50:49.570Z_

<details><summary>↩ Tool result · `toolu_01MfLvDRH8miekryo1KVaXxp`</summary>

```text
300	(1) REINFORCE: A t=r o​(𝐲)A_{t}=r_{o}(\mathbf{y}). (2) On top of (1), using a linear-head value model V V to calculate the baseline: A t=r o​(𝐲)−V​(𝐲<t)A_{t}=r_{o}(\mathbf{y})-V(\mathbf{y}_{<t}). This is the original PPO in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 "Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards") as we set γ=1\gamma=1 and λ=1\lambda=1. (3) On top of (1), using values from the Implicit PRM to serve as the baseline: A t=r o​(𝐲)−v ϕ​(𝐲<t)A_{t}=r_{o}(\mathbf{y})-v_{\phi}(\mathbf{y}_{<t}). This is equivalent to PPO with its value model being replaced by values from the Implicit PRM when γ=1\gamma=1 and λ=1\lambda=1. (4) On top of (1), using process rewards from the Implicit PRM to calculate the return: A t=r o​(𝐲)+∑s=t T r ϕ​(y s)A_{t}=r_{o}(\mathbf{y})+\sum_{s=t}^{T}r_{\phi}(y_{s}). This is exactly the REINFORCE w/ PRIME in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 "Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards").
301	
302	Figure[8](https://arxiv.org/html/2502.01456v2#S5.F8 "Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards") reports the results. Comparing PPO and REINFORCE, we find that an additional value model does not benefit policy performance. Notably, using rewards from the Implicit PRM to calculate returns, which is the default setting in PRIME, greatly outperforms all three baselines. This indicates that PRMs work better than value models in RL for LLMs. both two kinds of value models (PPO value model and Implicit PRM as value model) fall behind reward models.
303	
304	6 Related Work
305	--------------
306	
307	RL for LLM Reasoning. In the area of LLMs, reinforcement learning has been widely used for aligning human preferences(Christiano et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib5); Ouyang et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib32); Cui et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib6)), but the open-source community mostly adopt imitation learning methods(Yuan et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib54); Yue et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib57); Wei et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib50); Liu et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib28)) to enhance the reasoning capabilities of LLMs. Over the past few months, the paradigm gradually shifted. OpenAI o1(Jaech et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib16)) first showed the tremendous potential of large-scale RL for reasoning LLMs, and recent works have verified the scaling effect of RL with outcome rewards(DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7); Team et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib45)). Meanwhile, the role of dense rewards in RL remains underexplored, serving the main focus of PRIME.
308	
309	Implicit Rewards. Implicit rewards are broadly adopted in LLM alignment(Rafailov et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib33); Chen et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib4); Azar et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib2); Ethayarajh et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib8); Rosset et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib35); Chen et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib3)). Rafailov et al. ([2024](https://arxiv.org/html/2502.01456v2#bib.bib34)) first showed that optimizing DPO objective learns a Q function implicitly. Zhou et al. ([2024](https://arxiv.org/html/2502.01456v2#bib.bib60)) utilized implicit rewards in PPO, and showed the effectiveness of dense implicit rewards. Yuan et al. ([2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)) further extended the conclusion to any loss function optimizing Eq.[3](https://arxiv.org/html/2502.01456v2#S3.E3 "In 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards").
310	
311	7 Conclusion
312	------------
313	
314	As the fuel of LLMs, data, will be depleted in the near future, we are entering a new era of experience, which is exemplified by RL(Sutton, [2019](https://arxiv.org/html/2502.01456v2#bib.bib42)). This work develops PRIME, which produces and leverages dense rewards in online RL for LLM reasoning. Throughout the experiments, we validate that PRIME (1) greatly benefits sample efficiency and policy performance, (2) is easy to use with minimum cost, and (3) is a general method that works with broad RL algorithms together.
315	
316	Ethics Statement
317	----------------
318	
319	This paper presents PRIME whose goal is to advance the field of reinforcement learning for LLMs. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.
320	
321	Reproducibility Statement
322	-------------------------
323	
324	We have provided sufficient details to for reproduction, including algorithm pseudocode in Algorithm[1](https://arxiv.org/html/2502.01456v2#alg1 "Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards"), experiment configurations and hyperparameters in Section[4](https://arxiv.org/html/2502.01456v2#S4 "4 Experiments ‣ Process Reinforcement through Implicit Rewards") and Appendix. We have upload our code in Supplementary Material.
325	
326	References
327	----------
328	
329	*   Ahmadian et al. (2024) Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce style optimization for learning from human feedback in llms. _arXiv preprint arXiv:2402.14740_, 2024. 
330	*   Azar et al. (2024) Mohammad Gheshlaghi Azar, Mark Rowland, Bilal Piot, Daniel Guo, Daniele Calandriello, Michal Valko, and Rémi Munos. A general theoretical paradigm to understand learning from human preferences. _International Conference on Artificial Intelligence and Statistics_, abs/2310.12036, 2024. 
331	*   Chen et al. (2024a) Changyu Chen, Zichen Liu, Chao Du, Tianyu Pang, Qian Liu, Arunesh Sinha, Pradeep Varakantham, and Min Lin. Bootstrapping language models with dpo implicit rewards. _arXiv preprint arXiv:2406.09760_, 2024a. 
332	*   Chen et al. (2024b) Huayu Chen, Guande He, Lifan Yuan, Ganqu Cui, Hang Su, and Jun Zhu. Noise contrastive alignment of language models with explicit rewards. _arXiv preprint arXiv:2402.05369_, 2024b. 
333	*   Christiano et al. (2017) Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. _Advances in neural information processing systems_, 30, 2017. 
334	*   Cui et al. (2024) Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao, Bingxiang He, Wei Zhu, Yuan Ni, Guotong Xie, Ruobing Xie, Yankai Lin, Zhiyuan Liu, and Maosong Sun. Ultrafeedback: Boosting language models with scaled ai feedback. In _ICML_, 2024. 
335	*   DeepSeek-AI et al. (2025) DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H.Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J.L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R.J. Chen, R.L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S.S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T.Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W.L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y.K. Li, Y.Q. Wang, Y.X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y.X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z.Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948). 
336	*   Ethayarajh et al. (2024) Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela. Kto: Model alignment as prospect theoretic optimization. _ICML_, 2024. 
337	*   Gao et al. (2024) Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weiling Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, and Yi Wu. On designing effective rl reward at training time for llm reasoning. _ArXiv_, abs/2410.15115, 2024. 
338	*   Gao et al. (2022) Leo Gao, John Schulman, and Jacob Hilton. Scaling laws for reward model overoptimization. In _International Conference on Machine Learning_, 2022. 
339	*   Guo et al. (2024) Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. Deepseek-coder: When the large language model meets programming–the rise of code intelligence. _arXiv preprint arXiv:2401.14196_, 2024. 
340	*   Haarnoja et al. (2017) Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. Reinforcement learning with deep energy-based policies. In Doina Precup and Yee Whye Teh (eds.), _Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017_, volume 70 of _Proceedings of Machine Learning Research_, pp. 1352–1361. PMLR, 2017. URL [http://proceedings.mlr.press/v70/haarnoja17a.html](http://proceedings.mlr.press/v70/haarnoja17a.html). 
341	*   He et al. (2024) Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. OlympiadBench: A challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), _Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pp. 3828–3850, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.211. URL [https://aclanthology.org/2024.acl-long.211/](https://aclanthology.org/2024.acl-long.211/). 
342	*   Hendrycks et al. (2021a) Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, et al. Measuring coding challenge competence with apps. _arXiv preprint arXiv:2105.09938_, 2021a. 
343	*   Hendrycks et al. (2021b) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. _arXiv preprint arXiv:2103.03874_, 2021b. 
344	*   Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. _arXiv preprint arXiv:2412.16720_, 2024. 
345	*   Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. _arXiv preprint arXiv:2403.07974_, 2024. 
346	*   Kazemnejad et al. (2024) Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron Courville, and Nicolas Le Roux. Vineppo: Unlocking rl potential for llm reasoning through refined credit assignment. _arXiv preprint arXiv:2410.01679_, 2024. 
347	*   Kool et al. (2019) Wouter Kool, Herke van Hoof, and Max Welling. Buy 4 reinforce samples, get a baseline for free! In _DeepRLStructPred@ICLR_, 2019. URL [https://api.semanticscholar.org/CorpusID:198489118](https://api.semanticscholar.org/CorpusID:198489118). 
348	*   Lambert et al. (2024) Nathan Lambert, Jacob Daniel Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James Validad Miranda, Alisa Liu, Nouha Dziri, Xinxi Lyu, Yuling Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and Hanna Hajishirzi. Tülu 3: Pushing frontiers in open language model post-training. _ArXiv_, abs/2411.15124, 2024. 
349	*   Leike et al. (2018) Jan Leike, David Krueger, Tom Everitt, Miljan Martic, Vishal Maini, and Shane Legg. Scalable agent alignment via reward modeling: a research direction. _arXiv preprint arXiv:1811.07871_, 2018. 
350	*   Lewkowycz et al. (2022) Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems with language models. _Advances in Neural Information Processing Systems_, 35:3843–3857, 2022. 
351	*   Li et al. (2024) Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Huang, Kashif Rasul, Longhui Yu, Albert Q Jiang, Ziju Shen, et al. Numinamath: The largest public dataset in ai4maths with 860k pairs of competition math problems and solutions. _Hugging Face repository_, 13:9, 2024. 
352	*   Li et al. (2023) Rongao Li, Jie Fu, Bo-Wen Zhang, Tao Huang, Zhihong Sun, Chen Lyu, Guang Liu, Zhi Jin, and Ge Li. Taco: Topics in algorithmic code generation dataset. _arXiv preprint arXiv:2312.14852_, 2023. 
353	*   Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d’Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu, and Oriol Vinyals. Competition-level code generation with alphacode. _arXiv preprint arXiv:2203.07814_, 2022. 
354	*   Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yura Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. _ArXiv_, abs/2305.20050, 2023. 
355	*   Lin et al. (2024) Zhenghao Lin, Zhibin Gou, Yeyun Gong, Xiao Liu, Yelong Shen, Ruochen Xu, Chen Lin, Yujiu Yang, Jian Jiao, Nan Duan, and Weizhu Chen. Rho-1: Not all tokens are what you need, 2024. 
356	*   Liu et al. (2024) Zihan Liu, Yang Chen, Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. Acemath: Advancing frontier math reasoning with post-training and reward modeling. _arXiv preprint arXiv:2412.15084_, 2024. 
357	*   Luo et al. (2025) Michael Luo, Sijun Tan, Justin Wong, Xiaoxiang Shi, William Y. Tang, Manan Roongta, Colin Cai, Jeffrey Luo, Li Erran Li, Raluca Ada Popa, and Ion Stoica. Deepscaler: Surpassing o1-preview with a 1.5b model by scaling rl. [https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2](https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2), 2025. Notion Blog. 
358	*   Ng et al. (1999) Andrew Y. Ng, Daishi Harada, and Stuart Russell. Policy invariance under reward transformations: Theory and application to reward shaping. In Ivan Bratko and Saso Dzeroski (eds.), _Proceedings of the Sixteenth International Conference on Machine Learning (ICML 1999), Bled, Slovenia, June 27 - 30, 1999_, pp. 278–287. Morgan Kaufmann, 1999. 
359	*   OpenAI (2024) OpenAI. Openai o1 system card. _ArXiv_, abs/2412.16720, 2024. 
360	*   Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. _Advances in neural information processing systems_, 35:27730–27744, 2022. 
361	*   Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. _Advances in Neural Information Processing Systems_, 36, 2023. 
362	*   Rafailov et al. (2024) Rafael Rafailov, Joey Hejna, Ryan Park, and Chelsea Finn. From r r to q∗q^{*}: Your language model is secretly a q-function. _arXiv preprint arXiv:2404.12358_, 2024. 
363	*   Rosset et al. (2024) Corby Rosset, Ching-An Cheng, Arindam Mitra, Michael Santacroce, Ahmed Awadallah, and Tengyang Xie. Direct nash optimization: Teaching language models to self-improve with general preferences. _ArXiv_, abs/2404.03715, 2024. 
364	*   Schulman et al. (2016) John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. In _4th International Conference on Learning Representations, ICLR 2016, San Juan, Puerto Rico, May 2-4, 2016, Conference Track Proceedings_, 2016. 
365	*   Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_, 2017. 
366	*   Setlur et al. (2024) Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for llm reasoning. _arXiv preprint arXiv:2410.08146_, 2024. 
367	*   Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y.Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024. URL [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300). 
368	*   Sheng et al. (2024) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. _arXiv preprint arXiv: 2409.19256_, 2024. 
369	*   SkunkworksAI (2024) SkunkworksAI. reasoning-0.01, 2024. 
370	*   Sutton (2019) Richard Sutton. The bitter lesson. _Incomplete Ideas (blog)_, 13(1):38, 2019. 
371	*   Sutton (1988) Richard S Sutton. Learning to predict by the methods of temporal differences. _Machine learning_, 3:9–44, 1988. 
372	*   Sutton & Barto (2018) Richard S Sutton and Andrew G Barto. _Reinforcement learning: An introduction_. MIT press, 2018. 
373	*   Team et al. (2025) Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. _arXiv preprint arXiv:2501.12599_, 2025. 
374	*   Team (2024) Qwen Team. Qwq: Reflect deeply on the boundaries of the unknown, November 2024. URL [https://qwenlm.github.io/blog/qwq-32b-preview/](https://qwenlm.github.io/blog/qwq-32b-preview/). 
375	*   Toshniwal et al. (2024) Shubham Toshniwal, Wei Du, Ivan Moshkov, Branislav Kisacanin, Alexan Ayrapetyan, and Igor Gitman. Openmathinstruct-2: Accelerating ai for math with massive open-source instruction data. _arXiv preprint arXiv:2410.01560_, 2024. 
376	*   Uesato et al. (2022) Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. _arXiv preprint arXiv:2211.14275_, 2022. 
377	*   Wang et al. (2023) Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Y.Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. _ArXiv_, abs/2312.08935, 2023. 
378	*   Wei et al. (2024) Yuxiang Wei, Zhe Wang, Jiawei Liu, Yifeng Ding, and Lingming Zhang. Magicoder: Empowering code generation with oss-instruct. In _Forty-first International Conference on Machine Learning_, 2024. 
379	*   Williams (1992) Ronald J Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. _Machine learning_, 8:229–256, 1992. 
380	*   Yang et al. (2024a) An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 technical report. _arXiv preprint arXiv:2412.15115_, 2024a. 
381	*   Yang et al. (2024b) An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement, 2024b. URL [https://arxiv.org/abs/2409.12122](https://arxiv.org/abs/2409.12122). 
382	*   Yuan et al. (2024a) Lifan Yuan, Ganqu Cui, Hanbin Wang, Ning Ding, Xingyao Wang, Jia Deng, Boji Shan, Huimin Chen, Ruobing Xie, Yankai Lin, Zhenghao Liu, Bowen Zhou, Hao Peng, Zhiyuan Liu, and Maosong Sun. Advancing llm reasoning generalists with preference trees. _ArXiv_, 2024a. 
383	*   Yuan et al. (2024b) Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free process rewards without process labels, 2024b. URL [https://arxiv.org/abs/2412.01981](https://arxiv.org/abs/2412.01981). 
384	*   Yue et al. (2023) Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhu Chen. Mammoth: Building math generalist models through hybrid instruction tuning. _arXiv preprint arXiv:2309.05653_, 2023. 
385	*   Yue et al. (2024) Xiang Yue, Tuney Zheng, Ge Zhang, and Wenhu Chen. Mammoth2: Scaling instructions from the web. _ArXiv_, abs/2405.03548, 2024. 
386	*   Zhang et al. (2024) Kaiyan Zhang, Sihang Zeng, Ermo Hua, Ning Ding, Zhang-Ren Chen, Zhiyuan Ma, Haoxin Li, Ganqu Cui, Biqing Qi, Xuekai Zhu, Xingtai Lv, Hu Jinfang, Zhiyuan Liu, and Bowen Zhou. Ultramedical: Building specialized generalists in biomedicine, 2024. 
387	*   Zheng et al. (2024) Tianyu Zheng, Ge Zhang, Tianhao Shen, Xueling Liu, Bill Yuchen Lin, Jie Fu, Wenhu Chen, and Xiang Yue. Opencodeinterpreter: Integrating code generation with execution and refinement. _arXiv preprint arXiv:2402.14658_, 2024. 
388	*   Zhou et al. (2024) Zhanhui Zhou, Zhixuan Liu, Jie Liu, Zhichen Dong, Chao Yang, and Yu Qiao. Weak-to-strong search: Align large language models via searching over small language models. _arXiv preprint arXiv:2405.19262_, 2024. 
389	*   Ziebart et al. (2008) Brian D. Ziebart, Andrew L. Maas, J.Andrew Bagnell, and Anind K. Dey. Maximum entropy inverse reinforcement learning. In Dieter Fox and Carla P. Gomes (eds.), _Proceedings of the Twenty-Third AAAI Conference on Artificial Intelligence, AAAI 2008, Chicago, Illinois, USA, July 13-17, 2008_, pp. 1433–1438. AAAI Press, 2008. URL [http://www.aaai.org/Library/AAAI/2008/aaai08-227.php](http://www.aaai.org/Library/AAAI/2008/aaai08-227.php). 
390	
391	Appendix A Limitations
392	----------------------
393	
394	Due to resource constraints, we only conducted experiments on models up to 32B. Besides the main experiments of PRIME, we ran fewer steps for other ablation experiments, while we conduct comparison under the same step number for fairness.
395	
396	Appendix B Additional Results
397	-----------------------------
398	
399	### B.1 Reference Model Choice is Flexible
400	
401	![Image 12: Refer to caption](https://arxiv.org/html/2502.01456v2/figures/images/policy_ref.png)
402	
403	(a) Policy ref: We use the policy logprob as π ref\pi_{\text{ref}} for PRM.
404	
405	![Image 13: Refer to caption](https://arxiv.org/html/2502.01456v2/figures/images/sfr_ref.png)
406	
407	(b) SFT ref: We retain the initial policy to provide π ref\pi_{\text{ref}} for PRM and KL.
408	
409	Figure 9: Comparison of different reference policy implementations. One uses the running policy’s old logprobs as reference (policy ref) while the other uses the initial SFT model as the reference model (SFT ref).
410	
411	![Image 14: Refer to caption](https://arxiv.org/html/2502.01456v2/x12.png)
412	
413	Figure 10: Different reference model for PRM. We compare two reference model selection strategies for PRIME. Using the policy model as reference and using the initial SFT model as reference. Their rewards are similar.
414	
415	We implement two variants of our algorithms to explore the effect of reference model of implicit PRM, one using the initial SFT model as the reference model (SFT ref) while the other using the running policy’s old logprobs as reference (policy ref), as shown in Figure[9(a)](https://arxiv.org/html/2502.01456v2#A2.F9.sf1 "In Figure 9 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"). The policy ref simply adopts the old logprob of the policy model as π ref\pi_{\text{ref}}, while the SFT ref remains the initial SFT model for an additional π ref\pi_{\text{ref}} calculation. We compare their performance in this section.
416	
417	From the training rewards in Figure [10](https://arxiv.org/html/2502.01456v2#A2.F10 "Figure 10 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"), we find the two strategies are close and have pros and cons in different aspects: The Q value calculated by implicit PRM is the expectation under the distribution of the reference model. So the updating policy could natrually serve as the reference. On the other hand, KL divergence calculation is only allowed when the initial SFT model is retained.
418	
419	![Image 15: Refer to caption](https://arxiv.org/html/2502.01456v2/x13.png)
420	
421	(a) PRM classification accuracy on training samples.
422	
423	![Image 16: Refer to caption](https://arxiv.org/html/2502.01456v2/x14.png)
424	
425	(b) Training outcome rewards.
426	
427	Figure 11: Single and double forward. While double forward methods obtain higher accuracy after online update, the two variants achieve similar rewards during training.
428	
429	### B.2 Single-Forward v.s. Double-Forward
430	
431	Since our implicit PRM is concurrently updated in training, for each rollout stage, we can update the PRM before the policy model and use the updated PRM to re-calculate the process rewards, which we call the double-forward setting. We investigate the impact of double-forward in both the training and test phases. Our default setting applies single-forward, which uses process rewards from old PRMs. We plot PRM accuracy on rollouts and training rewards in Figure [11](https://arxiv.org/html/2502.01456v2#A2.F11 "Figure 11 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards").
432	
433	Accordingly, we find that double-forward could increase PRM accuracy, but the training rewards remain close between the two methods.
434	
435	Table 3: The comparison of resource requirements between Eurus-2-7B-PRIME and Qwen2.5-Math-7B-Instruct.
436	
437	### B.3 Results of Different RL Algorithms
438	
439	![Image 17: Refer to caption](https://arxiv.org/html/2502.01456v2/x15.png)
440	
441	Figure 12: Overall math performance. Eurus-2-7B-PRIME excels at competition-level mathematics benchmarks, outperforming advanced math models and larger models. Notably, PRIME brings substantial performance gain (+16.7%) over Eurus-2-7B-SFT.
442	
443	Table 4: Testset results of different RL algorithms.
444	
445	We ablate PRIME and different RL algorithms with their variants and find that the PRIME algorithm achieves the best performance for several reasons.
446	
447	First of all, We compare different REINFORCE-like advantage estimators including REINFORCE, GRPO, and RLOO, toggling the existence of implicit process reward. To make different algorithms compatible with the compound of outcome verifier reward and process reward, we accordingly make adaptions similar to Eq. [5](https://arxiv.org/html/2502.01456v2#S3.E5 "In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards"). For GRPO, we have
448	
449	A t i=r o​(𝐲 i)−mean​(r o​(𝐲 j))std​(r o​(𝐲 j))⏟GRPO with outcome rewards+∑s=t|𝐲 i|γ s−t⋅[r ϕ​(y s i)−mean​(r ϕ​(𝐲 j)|𝐲 j|)std​(r ϕ​(𝐲 j)|𝐲 j|)]⏟GRPO with implicit process rewards.A^{i}_{t}=\underbrace{\frac{r_{o}\left(\mathbf{y}^{i}\right)-\text{mean}(r_{o}\left(\mathbf{y}^{j}\right))}{\text{std}(r_{o}\left(\mathbf{y}^{j}\right))}}_{\text{GRPO with outcome rewards}}+\underbrace{\sum_{s=t}^{|\mathbf{y}^{i}|}\gamma^{s-t}\cdot\left[\frac{r_{\phi}(y^{i}_{s})-\text{mean}\left(\frac{r_{\phi}\left(\mathbf{y}^{j}\right)}{|\mathbf{y}^{j}|}\right)}{\text{std}\left(\frac{r_{\phi}\left(\mathbf{y}^{j}\right)}{|\mathbf{y}^{j}|}\right)}\right]}_{\text{GRPO with implicit process rewards}}.(7)
450	
451	For REINFORCE, we have
452	
453	A t i=r o​(𝐲 i)⏟REINFORCE with outcome rewards+∑s=t|𝐲 i|γ s−t⋅r ϕ​(y s i)⏟REINFORCE with implicit process rewards.A^{i}_{t}=\underbrace{r_{o}\left(\mathbf{y}^{i}\right)}_{\text{REINFORCE with outcome rewards}}+\underbrace{\sum_{s=t}^{|\mathbf{y}^{i}|}\gamma^{s-t}\cdot r_{\phi}(y^{i}_{s})}_{\text{REINFORCE with implicit process rewards}}.(8)
454	
455	As shown in Table [4](https://arxiv.org/html/2502.01456v2#A2.T4 "Table 4 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"), PRIME contributes consistently regardless of the policy update method, making it a generic algorithm.
456	
457	Moreover, the PPO variant of PRIME provides no performance gain, demonstrating that the additional computation cost from the critic model is redundant. This makes it possible to compensate for the expense of the process reward model by using REINFORCE-like algorithms with simpler advantage estimators.
458	
459	Finally, we choose the best-performing RLOO as the advantage estimator in our algorithm.
460	
461	### B.4 “Zero” Experiments
462	
463	![Image 18: Refer to caption](https://arxiv.org/html/2502.01456v2/x16.png)
464	
465	(a) Outcome training rewards (10-step moving).
466	
467	![Image 19: Refer to caption](https://arxiv.org/html/2502.01456v2/x17.png)
468	
469	(b) Math test accuracy across different gradient steps.
470	
471	Figure 13: “Zero” RL from Qwen2.5-Math-7B. RL from the base model converges way faster than the SFT model, surpassing the instruct version within 32 steps.
472	
473	![Image 20: Refer to caption](https://arxiv.org/html/2502.01456v2/x18.png)
474	
475	(a) Outcome training rewards (10-step moving).
476	
477	![Image 21: Refer to caption](https://arxiv.org/html/2502.01456v2/x19.png)
478	
479	(b) Math test accuracy across different gradient steps.
480	
481	Figure 14: “Zero” RL from Qwen2.5-32B-Base. RL from a 32B base model shows more promising gain, surpassing the instruct version within 16 steps. 
482	
483	DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)) proposed DeepSeek-R1-Zero, which is directly trained from a base model with reinforcement learning. To further investigate the “Zero” setting, we also perform RL from Qwen2.5-Math-7B-Base and Qwen2.5-32B-Base(Yang et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib52)), skipping the SFT phase. We present the experimental results in Figure[13](https://arxiv.org/html/2502.01456v2#A2.F13 "Figure 13 ‣ B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards") and Figure[14](https://arxiv.org/html/2502.01456v2#A2.F14 "Figure 14 ‣ B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"). The observations are as follows:
484	
485	(1) RL from base model is suprisingly efficient and effective. Comparing PRIME from Qwen2.5-Math-7B and Eurus-2-7B-SFT, the “Zero” setting converges much faster. This indicates that directly performing RL from a base model might be a strong alternative to the conventional SFT-RL pipeline.
486	
487	(2) Larger models benefit more. Comparing 7B and 32B models, we see that the 32B model gains more on both training rewards and test performance. This is aligned with the conclusion in DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)).
488	
489	(3) Saturation could be a potential issue. Although PRIME-Zero obtains impressive performance gain, we find it quickly saturated at a very early stage (about 50 steps), which hinders further improvement like in DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)). This is possibly attributed to the decrease of response diversity, and we leave this as future work.
490	
491	### B.5 Effect of Reward Model Size
492	
493	In the main experiments, we set the reward model to be of the same size as the policy model by default. To further investigate the influence of reward model capacity, we conduct comparative experiments by fixing the policy model as Qwen2.5-7B-Base and varying the reward model among Qwen2.5-3B-Base, Qwen2.5-7B-Base, and Qwen2.5-14B-Base, other settings are aligned with the main experiment. The results are summarized in Table[5](https://arxiv.org/html/2502.01456v2#A2.T5 "Table 5 ‣ B.5 Effect of Reward Model Size ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards"). Overall, the results suggest that reward model size has limited influence: the 7B reward model achieves the best average performance, while larger (14B) or smaller (3B) reward models do not yield clear advantages.
494	
495	Table 5: Performance comparison of different reward models (Qwen2.5-7B-Base as policy model).
496	
497	### B.6 Comparison with VinePPO
498	
499	VinePPO(Kazemnejad et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib18)) uses average return across trajectories to estimate the value within policy gradient update, instead of using value model in algorithm like PPO. We adopt the same setting as VinePPO, using RhoMath 1.1B(Lin et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib27)) as the base model and MATH dataset for training. We reproduced PRIME and VinePPO with 8 A800-80G for 96 steps with the same hyperparameters. It reveals that
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7647de9d-99a4-45f9-bd3b-9cb01c9d65eb",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "5805f092-c77e-4769-8830-46bd9ee92b55",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/ae85f63b-06b5-4781-b92e-92dc801697c7/tool-results/toolu_015h9VVLyaxdPfY7ZUe393pK.txt",
      "content": "(1) REINFORCE: A t=r o​(𝐲)A_{t}=r_{o}(\\mathbf{y}). (2) On top of (1), using a linear-head value model V V to calculate the baseline: A t=r o​(𝐲)−V​(𝐲<t)A_{t}=r_{o}(\\mathbf{y})-V(\\mathbf{y}_{<t}). This is the original PPO in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") as we set γ=1\\gamma=1 and λ=1\\lambda=1. (3) On top of (1), using values from the Implicit PRM to serve as the baseline: A t=r o​(𝐲)−v ϕ​(𝐲<t)A_{t}=r_{o}(\\mathbf{y})-v_{\\phi}(\\mathbf{y}_{<t}). This is equivalent to PPO with its value model being replaced by values from the Implicit PRM when γ=1\\gamma=1 and λ=1\\lambda=1. (4) On top of (1), using process rewards from the Implicit PRM to calculate the return: A t=r o​(𝐲)+∑s=t T r ϕ​(y s)A_{t}=r_{o}(\\mathbf{y})+\\sum_{s=t}^{T}r_{\\phi}(y_{s}). This is exactly the REINFORCE w/ PRIME in Figure [8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\").\n\nFigure[8](https://arxiv.org/html/2502.01456v2#S5.F8 \"Figure 8 ‣ 5.3 PRIME with Other RL Algorithms ‣ 5 Analysis ‣ Process Reinforcement through Implicit Rewards\") reports the results. Comparing PPO and REINFORCE, we find that an additional value model does not benefit policy performance. Notably, using rewards from the Implicit PRM to calculate returns, which is the default setting in PRIME, greatly outperforms all three baselines. This indicates that PRMs work better than value models in RL for LLMs. both two kinds of value models (PPO value model and Implicit PRM as value model) fall behind reward models.\n\n6 Related Work\n--------------\n\nRL for LLM Reasoning. In the area of LLMs, reinforcement learning has been widely used for aligning human preferences(Christiano et al., [2017](https://arxiv.org/html/2502.01456v2#bib.bib5); Ouyang et al., [2022](https://arxiv.org/html/2502.01456v2#bib.bib32); Cui et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib6)), but the open-source community mostly adopt imitation learning methods(Yuan et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib54); Yue et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib57); Wei et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib50); Liu et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib28)) to enhance the reasoning capabilities of LLMs. Over the past few months, the paradigm gradually shifted. OpenAI o1(Jaech et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib16)) first showed the tremendous potential of large-scale RL for reasoning LLMs, and recent works have verified the scaling effect of RL with outcome rewards(DeepSeek-AI et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib7); Team et al., [2025](https://arxiv.org/html/2502.01456v2#bib.bib45)). Meanwhile, the role of dense rewards in RL remains underexplored, serving the main focus of PRIME.\n\nImplicit Rewards. Implicit rewards are broadly adopted in LLM alignment(Rafailov et al., [2023](https://arxiv.org/html/2502.01456v2#bib.bib33); Chen et al., [2024b](https://arxiv.org/html/2502.01456v2#bib.bib4); Azar et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib2); Ethayarajh et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib8); Rosset et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib35); Chen et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib3)). Rafailov et al. ([2024](https://arxiv.org/html/2502.01456v2#bib.bib34)) first showed that optimizing DPO objective learns a Q function implicitly. Zhou et al. ([2024](https://arxiv.org/html/2502.01456v2#bib.bib60)) utilized implicit rewards in PPO, and showed the effectiveness of dense implicit rewards. Yuan et al. ([2024b](https://arxiv.org/html/2502.01456v2#bib.bib55)) further extended the conclusion to any loss function optimizing Eq.[3](https://arxiv.org/html/2502.01456v2#S3.E3 \"In 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\").\n\n7 Conclusion\n------------\n\nAs the fuel of LLMs, data, will be depleted in the near future, we are entering a new era of experience, which is exemplified by RL(Sutton, [2019](https://arxiv.org/html/2502.01456v2#bib.bib42)). This work develops PRIME, which produces and leverages dense rewards in online RL for LLM reasoning. Throughout the experiments, we validate that PRIME (1) greatly benefits sample efficiency and policy performance, (2) is easy to use with minimum cost, and (3) is a general method that works with broad RL algorithms together.\n\nEthics Statement\n----------------\n\nThis paper presents PRIME whose goal is to advance the field of reinforcement learning for LLMs. There are many potential societal consequences of our work, none of which we feel must be specifically highlighted here.\n\nReproducibility Statement\n-------------------------\n\nWe have provided sufficient details to for reproduction, including algorithm pseudocode in Algorithm[1](https://arxiv.org/html/2502.01456v2#alg1 \"Algorithm 1 ‣ 3.1 Enabling Scalable Reward Update with Implicit Reward Modeling ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"), experiment configurations and hyperparameters in Section[4](https://arxiv.org/html/2502.01456v2#S4 \"4 Experiments ‣ Process Reinforcement through Implicit Rewards\") and Appendix. We have upload our code in Supplementary Material.\n\nReferences\n----------\n\n*   Ahmadian et al. (2024) Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce style optimization for learning from human feedback in llms. _arXiv preprint arXiv:2402.14740_, 2024. \n*   Azar et al. (2024) Mohammad Gheshlaghi Azar, Mark Rowland, Bilal Piot, Daniel Guo, Daniele Calandriello, Michal Valko, and Rémi Munos. A general theoretical paradigm to understand learning from human preferences. _International Conference on Artificial Intelligence and Statistics_, abs/2310.12036, 2024. \n*   Chen et al. (2024a) Changyu Chen, Zichen Liu, Chao Du, Tianyu Pang, Qian Liu, Arunesh Sinha, Pradeep Varakantham, and Min Lin. Bootstrapping language models with dpo implicit rewards. _arXiv preprint arXiv:2406.09760_, 2024a. \n*   Chen et al. (2024b) Huayu Chen, Guande He, Lifan Yuan, Ganqu Cui, Hang Su, and Jun Zhu. Noise contrastive alignment of language models with explicit rewards. _arXiv preprint arXiv:2402.05369_, 2024b. \n*   Christiano et al. (2017) Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. _Advances in neural information processing systems_, 30, 2017. \n*   Cui et al. (2024) Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao, Bingxiang He, Wei Zhu, Yuan Ni, Guotong Xie, Ruobing Xie, Yankai Lin, Zhiyuan Liu, and Maosong Sun. Ultrafeedback: Boosting language models with scaled ai feedback. In _ICML_, 2024. \n*   DeepSeek-AI et al. (2025) DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z.F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H.Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J.L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R.J. Chen, R.L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S.S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T.Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W.L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X.Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y.K. Li, Y.Q. Wang, Y.X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y.X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z.Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948). \n*   Ethayarajh et al. (2024) Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela. Kto: Model alignment as prospect theoretic optimization. _ICML_, 2024. \n*   Gao et al. (2024) Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weiling Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, and Yi Wu. On designing effective rl reward at training time for llm reasoning. _ArXiv_, abs/2410.15115, 2024. \n*   Gao et al. (2022) Leo Gao, John Schulman, and Jacob Hilton. Scaling laws for reward model overoptimization. In _International Conference on Machine Learning_, 2022. \n*   Guo et al. (2024) Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. Deepseek-coder: When the large language model meets programming–the rise of code intelligence. _arXiv preprint arXiv:2401.14196_, 2024. \n*   Haarnoja et al. (2017) Tuomas Haarnoja, Haoran Tang, Pieter Abbeel, and Sergey Levine. Reinforcement learning with deep energy-based policies. In Doina Precup and Yee Whye Teh (eds.), _Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017_, volume 70 of _Proceedings of Machine Learning Research_, pp. 1352–1361. PMLR, 2017. URL [http://proceedings.mlr.press/v70/haarnoja17a.html](http://proceedings.mlr.press/v70/haarnoja17a.html). \n*   He et al. (2024) Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. OlympiadBench: A challenging benchmark for promoting AGI with olympiad-level bilingual multimodal scientific problems. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), _Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_, pp. 3828–3850, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.211. URL [https://aclanthology.org/2024.acl-long.211/](https://aclanthology.org/2024.acl-long.211/). \n*   Hendrycks et al. (2021a) Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, et al. Measuring coding challenge competence with apps. _arXiv preprint arXiv:2105.09938_, 2021a. \n*   Hendrycks et al. (2021b) Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. _arXiv preprint arXiv:2103.03874_, 2021b. \n*   Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. _arXiv preprint arXiv:2412.16720_, 2024. \n*   Jain et al. (2024) Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models for code. _arXiv preprint arXiv:2403.07974_, 2024. \n*   Kazemnejad et al. (2024) Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron Courville, and Nicolas Le Roux. Vineppo: Unlocking rl potential for llm reasoning through refined credit assignment. _arXiv preprint arXiv:2410.01679_, 2024. \n*   Kool et al. (2019) Wouter Kool, Herke van Hoof, and Max Welling. Buy 4 reinforce samples, get a baseline for free! In _DeepRLStructPred@ICLR_, 2019. URL [https://api.semanticscholar.org/CorpusID:198489118](https://api.semanticscholar.org/CorpusID:198489118). \n*   Lambert et al. (2024) Nathan Lambert, Jacob Daniel Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James Validad Miranda, Alisa Liu, Nouha Dziri, Xinxi Lyu, Yuling Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind Tafjord, Chris Wilhelm, Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi, and Hanna Hajishirzi. Tülu 3: Pushing frontiers in open language model post-training. _ArXiv_, abs/2411.15124, 2024. \n*   Leike et al. (2018) Jan Leike, David Krueger, Tom Everitt, Miljan Martic, Vishal Maini, and Shane Legg. Scalable agent alignment via reward modeling: a research direction. _arXiv preprint arXiv:1811.07871_, 2018. \n*   Lewkowycz et al. (2022) Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, et al. Solving quantitative reasoning problems with language models. _Advances in Neural Information Processing Systems_, 35:3843–3857, 2022. \n*   Li et al. (2024) Jia Li, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Huang, Kashif Rasul, Longhui Yu, Albert Q Jiang, Ziju Shen, et al. Numinamath: The largest public dataset in ai4maths with 860k pairs of competition math problems and solutions. _Hugging Face repository_, 13:9, 2024. \n*   Li et al. (2023) Rongao Li, Jie Fu, Bo-Wen Zhang, Tao Huang, Zhihong Sun, Chen Lyu, Guang Liu, Zhi Jin, and Ge Li. Taco: Topics in algorithmic code generation dataset. _arXiv preprint arXiv:2312.14852_, 2023. \n*   Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, Thomas Hubert, Peter Choy, Cyprien de Masson d’Autume, Igor Babuschkin, Xinyun Chen, Po-Sen Huang, Johannes Welbl, Sven Gowal, Alexey Cherepanov, James Molloy, Daniel Mankowitz, Esme Sutherland Robson, Pushmeet Kohli, Nando de Freitas, Koray Kavukcuoglu, and Oriol Vinyals. Competition-level code generation with alphacode. _arXiv preprint arXiv:2203.07814_, 2022. \n*   Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yura Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. _ArXiv_, abs/2305.20050, 2023. \n*   Lin et al. (2024) Zhenghao Lin, Zhibin Gou, Yeyun Gong, Xiao Liu, Yelong Shen, Ruochen Xu, Chen Lin, Yujiu Yang, Jian Jiao, Nan Duan, and Weizhu Chen. Rho-1: Not all tokens are what you need, 2024. \n*   Liu et al. (2024) Zihan Liu, Yang Chen, Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. Acemath: Advancing frontier math reasoning with post-training and reward modeling. _arXiv preprint arXiv:2412.15084_, 2024. \n*   Luo et al. (2025) Michael Luo, Sijun Tan, Justin Wong, Xiaoxiang Shi, William Y. Tang, Manan Roongta, Colin Cai, Jeffrey Luo, Li Erran Li, Raluca Ada Popa, and Ion Stoica. Deepscaler: Surpassing o1-preview with a 1.5b model by scaling rl. [https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2](https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2), 2025. Notion Blog. \n*   Ng et al. (1999) Andrew Y. Ng, Daishi Harada, and Stuart Russell. Policy invariance under reward transformations: Theory and application to reward shaping. In Ivan Bratko and Saso Dzeroski (eds.), _Proceedings of the Sixteenth International Conference on Machine Learning (ICML 1999), Bled, Slovenia, June 27 - 30, 1999_, pp. 278–287. Morgan Kaufmann, 1999. \n*   OpenAI (2024) OpenAI. Openai o1 system card. _ArXiv_, abs/2412.16720, 2024. \n*   Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. _Advances in neural information processing systems_, 35:27730–27744, 2022. \n*   Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. _Advances in Neural Information Processing Systems_, 36, 2023. \n*   Rafailov et al. (2024) Rafael Rafailov, Joey Hejna, Ryan Park, and Chelsea Finn. From r r to q∗q^{*}: Your language model is secretly a q-function. _arXiv preprint arXiv:2404.12358_, 2024. \n*   Rosset et al. (2024) Corby Rosset, Ching-An Cheng, Arindam Mitra, Michael Santacroce, Ahmed Awadallah, and Tengyang Xie. Direct nash optimization: Teaching language models to self-improve with general preferences. _ArXiv_, abs/2404.03715, 2024. \n*   Schulman et al. (2016) John Schulman, Philipp Moritz, Sergey Levine, Michael I. Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. In _4th International Conference on Learning Representations, ICLR 2016, San Juan, Puerto Rico, May 2-4, 2016, Conference Track Proceedings_, 2016. \n*   Schulman et al. (2017) John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. _arXiv preprint arXiv:1707.06347_, 2017. \n*   Setlur et al. (2024) Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process verifiers for llm reasoning. _arXiv preprint arXiv:2410.08146_, 2024. \n*   Shao et al. (2024) Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y.Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024. URL [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300). \n*   Sheng et al. (2024) Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. _arXiv preprint arXiv: 2409.19256_, 2024. \n*   SkunkworksAI (2024) SkunkworksAI. reasoning-0.01, 2024. \n*   Sutton (2019) Richard Sutton. The bitter lesson. _Incomplete Ideas (blog)_, 13(1):38, 2019. \n*   Sutton (1988) Richard S Sutton. Learning to predict by the methods of temporal differences. _Machine learning_, 3:9–44, 1988. \n*   Sutton & Barto (2018) Richard S Sutton and Andrew G Barto. _Reinforcement learning: An introduction_. MIT press, 2018. \n*   Team et al. (2025) Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. _arXiv preprint arXiv:2501.12599_, 2025. \n*   Team (2024) Qwen Team. Qwq: Reflect deeply on the boundaries of the unknown, November 2024. URL [https://qwenlm.github.io/blog/qwq-32b-preview/](https://qwenlm.github.io/blog/qwq-32b-preview/). \n*   Toshniwal et al. (2024) Shubham Toshniwal, Wei Du, Ivan Moshkov, Branislav Kisacanin, Alexan Ayrapetyan, and Igor Gitman. Openmathinstruct-2: Accelerating ai for math with massive open-source instruction data. _arXiv preprint arXiv:2410.01560_, 2024. \n*   Uesato et al. (2022) Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. _arXiv preprint arXiv:2211.14275_, 2022. \n*   Wang et al. (2023) Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Y.Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations. _ArXiv_, abs/2312.08935, 2023. \n*   Wei et al. (2024) Yuxiang Wei, Zhe Wang, Jiawei Liu, Yifeng Ding, and Lingming Zhang. Magicoder: Empowering code generation with oss-instruct. In _Forty-first International Conference on Machine Learning_, 2024. \n*   Williams (1992) Ronald J Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. _Machine learning_, 8:229–256, 1992. \n*   Yang et al. (2024a) An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 technical report. _arXiv preprint arXiv:2412.15115_, 2024a. \n*   Yang et al. (2024b) An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement, 2024b. URL [https://arxiv.org/abs/2409.12122](https://arxiv.org/abs/2409.12122). \n*   Yuan et al. (2024a) Lifan Yuan, Ganqu Cui, Hanbin Wang, Ning Ding, Xingyao Wang, Jia Deng, Boji Shan, Huimin Chen, Ruobing Xie, Yankai Lin, Zhenghao Liu, Bowen Zhou, Hao Peng, Zhiyuan Liu, and Maosong Sun. Advancing llm reasoning generalists with preference trees. _ArXiv_, 2024a. \n*   Yuan et al. (2024b) Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free process rewards without process labels, 2024b. URL [https://arxiv.org/abs/2412.01981](https://arxiv.org/abs/2412.01981). \n*   Yue et al. (2023) Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and Wenhu Chen. Mammoth: Building math generalist models through hybrid instruction tuning. _arXiv preprint arXiv:2309.05653_, 2023. \n*   Yue et al. (2024) Xiang Yue, Tuney Zheng, Ge Zhang, and Wenhu Chen. Mammoth2: Scaling instructions from the web. _ArXiv_, abs/2405.03548, 2024. \n*   Zhang et al. (2024) Kaiyan Zhang, Sihang Zeng, Ermo Hua, Ning Ding, Zhang-Ren Chen, Zhiyuan Ma, Haoxin Li, Ganqu Cui, Biqing Qi, Xuekai Zhu, Xingtai Lv, Hu Jinfang, Zhiyuan Liu, and Bowen Zhou. Ultramedical: Building specialized generalists in biomedicine, 2024. \n*   Zheng et al. (2024) Tianyu Zheng, Ge Zhang, Tianhao Shen, Xueling Liu, Bill Yuchen Lin, Jie Fu, Wenhu Chen, and Xiang Yue. Opencodeinterpreter: Integrating code generation with execution and refinement. _arXiv preprint arXiv:2402.14658_, 2024. \n*   Zhou et al. (2024) Zhanhui Zhou, Zhixuan Liu, Jie Liu, Zhichen Dong, Chao Yang, and Yu Qiao. Weak-to-strong search: Align large language models via searching over small language models. _arXiv preprint arXiv:2405.19262_, 2024. \n*   Ziebart et al. (2008) Brian D. Ziebart, Andrew L. Maas, J.Andrew Bagnell, and Anind K. Dey. Maximum entropy inverse reinforcement learning. In Dieter Fox and Carla P. Gomes (eds.), _Proceedings of the Twenty-Third AAAI Conference on Artificial Intelligence, AAAI 2008, Chicago, Illinois, USA, July 13-17, 2008_, pp. 1433–1438. AAAI Press, 2008. URL [http://www.aaai.org/Library/AAAI/2008/aaai08-227.php](http://www.aaai.org/Library/AAAI/2008/aaai08-227.php). \n\nAppendix A Limitations\n----------------------\n\nDue to resource constraints, we only conducted experiments on models up to 32B. Besides the main experiments of PRIME, we ran fewer steps for other ablation experiments, while we conduct comparison under the same step number for fairness.\n\nAppendix B Additional Results\n-----------------------------\n\n### B.1 Reference Model Choice is Flexible\n\n![Image 12: Refer to caption](https://arxiv.org/html/2502.01456v2/figures/images/policy_ref.png)\n\n(a) Policy ref: We use the policy logprob as π ref\\pi_{\\text{ref}} for PRM.\n\n![Image 13: Refer to caption](https://arxiv.org/html/2502.01456v2/figures/images/sfr_ref.png)\n\n(b) SFT ref: We retain the initial policy to provide π ref\\pi_{\\text{ref}} for PRM and KL.\n\nFigure 9: Comparison of different reference policy implementations. One uses the running policy’s old logprobs as reference (policy ref) while the other uses the initial SFT model as the reference model (SFT ref).\n\n![Image 14: Refer to caption](https://arxiv.org/html/2502.01456v2/x12.png)\n\nFigure 10: Different reference model for PRM. We compare two reference model selection strategies for PRIME. Using the policy model as reference and using the initial SFT model as reference. Their rewards are similar.\n\nWe implement two variants of our algorithms to explore the effect of reference model of implicit PRM, one using the initial SFT model as the reference model (SFT ref) while the other using the running policy’s old logprobs as reference (policy ref), as shown in Figure[9(a)](https://arxiv.org/html/2502.01456v2#A2.F9.sf1 \"In Figure 9 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). The policy ref simply adopts the old logprob of the policy model as π ref\\pi_{\\text{ref}}, while the SFT ref remains the initial SFT model for an additional π ref\\pi_{\\text{ref}} calculation. We compare their performance in this section.\n\nFrom the training rewards in Figure [10](https://arxiv.org/html/2502.01456v2#A2.F10 \"Figure 10 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), we find the two strategies are close and have pros and cons in different aspects: The Q value calculated by implicit PRM is the expectation under the distribution of the reference model. So the updating policy could natrually serve as the reference. On the other hand, KL divergence calculation is only allowed when the initial SFT model is retained.\n\n![Image 15: Refer to caption](https://arxiv.org/html/2502.01456v2/x13.png)\n\n(a) PRM classification accuracy on training samples.\n\n![Image 16: Refer to caption](https://arxiv.org/html/2502.01456v2/x14.png)\n\n(b) Training outcome rewards.\n\nFigure 11: Single and double forward. While double forward methods obtain higher accuracy after online update, the two variants achieve similar rewards during training.\n\n### B.2 Single-Forward v.s. Double-Forward\n\nSince our implicit PRM is concurrently updated in training, for each rollout stage, we can update the PRM before the policy model and use the updated PRM to re-calculate the process rewards, which we call the double-forward setting. We investigate the impact of double-forward in both the training and test phases. Our default setting applies single-forward, which uses process rewards from old PRMs. We plot PRM accuracy on rollouts and training rewards in Figure [11](https://arxiv.org/html/2502.01456v2#A2.F11 \"Figure 11 ‣ B.1 Reference Model Choice is Flexible ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\").\n\nAccordingly, we find that double-forward could increase PRM accuracy, but the training rewards remain close between the two methods.\n\nTable 3: The comparison of resource requirements between Eurus-2-7B-PRIME and Qwen2.5-Math-7B-Instruct.\n\n### B.3 Results of Different RL Algorithms\n\n![Image 17: Refer to caption](https://arxiv.org/html/2502.01456v2/x15.png)\n\nFigure 12: Overall math performance. Eurus-2-7B-PRIME excels at competition-level mathematics benchmarks, outperforming advanced math models and larger models. Notably, PRIME brings substantial performance gain (+16.7%) over Eurus-2-7B-SFT.\n\nTable 4: Testset results of different RL algorithms.\n\nWe ablate PRIME and different RL algorithms with their variants and find that the PRIME algorithm achieves the best performance for several reasons.\n\nFirst of all, We compare different REINFORCE-like advantage estimators including REINFORCE, GRPO, and RLOO, toggling the existence of implicit process reward. To make different algorithms compatible with the compound of outcome verifier reward and process reward, we accordingly make adaptions similar to Eq. [5](https://arxiv.org/html/2502.01456v2#S3.E5 \"In 3.2 Advantage Estimation and Policy Update ‣ 3 PRIME ‣ Process Reinforcement through Implicit Rewards\"). For GRPO, we have\n\nA t i=r o​(𝐲 i)−mean​(r o​(𝐲 j))std​(r o​(𝐲 j))⏟GRPO with outcome rewards+∑s=t|𝐲 i|γ s−t⋅[r ϕ​(y s i)−mean​(r ϕ​(𝐲 j)|𝐲 j|)std​(r ϕ​(𝐲 j)|𝐲 j|)]⏟GRPO with implicit process rewards.A^{i}_{t}=\\underbrace{\\frac{r_{o}\\left(\\mathbf{y}^{i}\\right)-\\text{mean}(r_{o}\\left(\\mathbf{y}^{j}\\right))}{\\text{std}(r_{o}\\left(\\mathbf{y}^{j}\\right))}}_{\\text{GRPO with outcome rewards}}+\\underbrace{\\sum_{s=t}^{|\\mathbf{y}^{i}|}\\gamma^{s-t}\\cdot\\left[\\frac{r_{\\phi}(y^{i}_{s})-\\text{mean}\\left(\\frac{r_{\\phi}\\left(\\mathbf{y}^{j}\\right)}{|\\mathbf{y}^{j}|}\\right)}{\\text{std}\\left(\\frac{r_{\\phi}\\left(\\mathbf{y}^{j}\\right)}{|\\mathbf{y}^{j}|}\\right)}\\right]}_{\\text{GRPO with implicit process rewards}}.(7)\n\nFor REINFORCE, we have\n\nA t i=r o​(𝐲 i)⏟REINFORCE with outcome rewards+∑s=t|𝐲 i|γ s−t⋅r ϕ​(y s i)⏟REINFORCE with implicit process rewards.A^{i}_{t}=\\underbrace{r_{o}\\left(\\mathbf{y}^{i}\\right)}_{\\text{REINFORCE with outcome rewards}}+\\underbrace{\\sum_{s=t}^{|\\mathbf{y}^{i}|}\\gamma^{s-t}\\cdot r_{\\phi}(y^{i}_{s})}_{\\text{REINFORCE with implicit process rewards}}.(8)\n\nAs shown in Table [4](https://arxiv.org/html/2502.01456v2#A2.T4 \"Table 4 ‣ B.3 Results of Different RL Algorithms ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"), PRIME contributes consistently regardless of the policy update method, making it a generic algorithm.\n\nMoreover, the PPO variant of PRIME provides no performance gain, demonstrating that the additional computation cost from the critic model is redundant. This makes it possible to compensate for the expense of the process reward model by using REINFORCE-like algorithms with simpler advantage estimators.\n\nFinally, we choose the best-performing RLOO as the advantage estimator in our algorithm.\n\n### B.4 “Zero” Experiments\n\n![Image 18: Refer to caption](https://arxiv.org/html/2502.01456v2/x16.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 19: Refer to caption](https://arxiv.org/html/2502.01456v2/x17.png)\n\n(b) Math test accuracy across different gradient steps.\n\nFigure 13: “Zero” RL from Qwen2.5-Math-7B. RL from the base model converges way faster than the SFT model, surpassing the instruct version within 32 steps.\n\n![Image 20: Refer to caption](https://arxiv.org/html/2502.01456v2/x18.png)\n\n(a) Outcome training rewards (10-step moving).\n\n![Image 21: Refer to caption](https://arxiv.org/html/2502.01456v2/x19.png)\n\n(b) Math test accuracy across different gradient steps.\n\nFigure 14: “Zero” RL from Qwen2.5-32B-Base. RL from a 32B base model shows more promising gain, surpassing the instruct version within 16 steps. \n\nDeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)) proposed DeepSeek-R1-Zero, which is directly trained from a base model with reinforcement learning. To further investigate the “Zero” setting, we also perform RL from Qwen2.5-Math-7B-Base and Qwen2.5-32B-Base(Yang et al., [2024a](https://arxiv.org/html/2502.01456v2#bib.bib52)), skipping the SFT phase. We present the experimental results in Figure[13](https://arxiv.org/html/2502.01456v2#A2.F13 \"Figure 13 ‣ B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\") and Figure[14](https://arxiv.org/html/2502.01456v2#A2.F14 \"Figure 14 ‣ B.4 “Zero” Experiments ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). The observations are as follows:\n\n(1) RL from base model is suprisingly efficient and effective. Comparing PRIME from Qwen2.5-Math-7B and Eurus-2-7B-SFT, the “Zero” setting converges much faster. This indicates that directly performing RL from a base model might be a strong alternative to the conventional SFT-RL pipeline.\n\n(2) Larger models benefit more. Comparing 7B and 32B models, we see that the 32B model gains more on both training rewards and test performance. This is aligned with the conclusion in DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)).\n\n(3) Saturation could be a potential issue. Although PRIME-Zero obtains impressive performance gain, we find it quickly saturated at a very early stage (about 50 steps), which hinders further improvement like in DeepSeek-AI et al. ([2025](https://arxiv.org/html/2502.01456v2#bib.bib7)). This is possibly attributed to the decrease of response diversity, and we leave this as future work.\n\n### B.5 Effect of Reward Model Size\n\nIn the main experiments, we set the reward model to be of the same size as the policy model by default. To further investigate the influence of reward model capacity, we conduct comparative experiments by fixing the policy model as Qwen2.5-7B-Base and varying the reward model among Qwen2.5-3B-Base, Qwen2.5-7B-Base, and Qwen2.5-14B-Base, other settings are aligned with the main experiment. The results are summarized in Table[5](https://arxiv.org/html/2502.01456v2#A2.T5 \"Table 5 ‣ B.5 Effect of Reward Model Size ‣ Appendix B Additional Results ‣ Process Reinforcement through Implicit Rewards\"). Overall, the results suggest that reward model size has limited influence: the 7B reward model achieves the best average performance, while larger (14B) or smaller (3B) reward models do not yield clear advantages.\n\nTable 5: Performance comparison of different reward models (Qwen2.5-7B-Base as policy model).\n\n### B.6 Comparison with VinePPO\n\nVinePPO(Kazemnejad et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib18)) uses average return across trajectories to estimate the value within policy gradient update, instead of using value model in algorithm like PPO. We adopt the same setting as VinePPO, using RhoMath 1.1B(Lin et al., [2024](https://arxiv.org/html/2502.01456v2#bib.bib27)) as the base model and MATH dataset for training. We reproduced PRIME and VinePPO with 8 A800-80G for 96 steps with the same hyperparameters. It reveals that",
      "numLines": 200,
      "startLine": 300,
      "totalLines": 626
    }
  },
  "sourceToolAssistantUUID": "7647de9d-99a4-45f9-bd3b-9cb01c9d65eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "5805f092-c77e-4769-8830-46bd9ee92b55",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRIME paper on implicit process rewards",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Assistant

_source line 66 · 2026-05-27T15:50:53.937Z_

<details><summary>Logged reasoning block</summary>

```text
I now have a very comprehensive view of the paper. Let me also try to find the OpenReview page one more time with a different approach. But I have enough content to do a thorough analysis. Let me try one more OpenReview search approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5805f092-c77e-4769-8830-46bd9ee92b55",
  "isSidechain": false,
  "requestId": "req_011CbTLfDM1wx61kgRyAVeHi",
  "type": "assistant",
  "uuid": "9645226c-518d-4250-89be-58f745afd241",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrmGGWhjcccsP1MXkWTSh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13878,
      "cache_read_input_tokens": 38513,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 38513,
          "cache_creation_input_tokens": 13878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13878
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

### Assistant

_source line 67 · 2026-05-27T15:50:54.971Z_

I now have extensive content from the paper. Let me try one final approach to find OpenReview reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9645226c-518d-4250-89be-58f745afd241",
  "isSidechain": false,
  "requestId": "req_011CbTLfDM1wx61kgRyAVeHi",
  "type": "assistant",
  "uuid": "b4c99bbd-ef52-4d9b-b03e-79eef4f397c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrmGGWhjcccsP1MXkWTSh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13878,
      "cache_read_input_tokens": 38513,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 38513,
          "cache_creation_input_tokens": 13878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13878
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

### Tool call

_source line 68 · 2026-05-27T15:50:57.016Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013MXcjoqCumg5DrD91Qazcp`</summary>

```json
{
  "url": "https://openreview.net/search?term=%22Process+Reinforcement+through+Implicit+Rewards%22&venue=ICLR.cc/2025/Conference&type=forum",
  "prompt": "Find the forum ID or URL for the paper \"Process Reinforcement through Implicit Rewards\" at ICLR 2025. Return any results found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4c99bbd-ef52-4d9b-b03e-79eef4f397c6",
  "isSidechain": false,
  "requestId": "req_011CbTLfDM1wx61kgRyAVeHi",
  "type": "assistant",
  "uuid": "fd00eca0-bdd9-4fb2-90bc-d72dc2aeb0e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrmGGWhjcccsP1MXkWTSh7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13878,
      "cache_read_input_tokens": 38513,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 38513,
          "cache_creation_input_tokens": 13878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13878
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

_source line 69 · 2026-05-27T15:50:59.164Z_

<details><summary>↩ Tool result · `toolu_013MXcjoqCumg5DrD91Qazcp`</summary>

```text
I cannot find the forum ID or URL for the paper "Process Reinforcement through Implicit Rewards" at ICLR 2025 in the provided content.

The webpage content shown is only the header, navigation menu, and footer of OpenReview.net. It does not contain any search results, paper listings, or venue-specific information that would include details about individual papers or their forum IDs.

To locate this paper, you would need to:
1. Visit the OpenReview.net website directly
2. Navigate to the ICLR 2025 venue page
3. Use the search functionality to find the specific paper
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd00eca0-bdd9-4fb2-90bc-d72dc2aeb0e0",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "e7b7e71d-494b-4c2b-b2fd-0cd7d4fe3111",
  "toolUseResult": {
    "bytes": 62569,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the forum ID or URL for the paper \"Process Reinforcement through Implicit Rewards\" at ICLR 2025 in the provided content.\n\nThe webpage content shown is only the header, navigation menu, and footer of OpenReview.net. It does not contain any search results, paper listings, or venue-specific information that would include details about individual papers or their forum IDs.\n\nTo locate this paper, you would need to:\n1. Visit the OpenReview.net website directly\n2. Navigate to the ICLR 2025 venue page\n3. Use the search functionality to find the specific paper",
    "durationMs": 2145,
    "url": "https://openreview.net/search?term=%22Process+Reinforcement+through+Implicit+Rewards%22&venue=ICLR.cc/2025/Conference&type=forum"
  },
  "sourceToolAssistantUUID": "fd00eca0-bdd9-4fb2-90bc-d72dc2aeb0e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-27T15:51:02.761Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TZm8p3VKD738oLHcD29BDo`</summary>

```json
{
  "url": "https://openreview.net/forum?id=6v1hENMQCl",
  "prompt": "Check if this is the forum page for \"Process Reinforcement through Implicit Rewards\" (PRIME). If yes, extract ALL reviewer comments, ratings, strengths, weaknesses, questions, and author responses. Be as detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7b7e71d-494b-4c2b-b2fd-0cd7d4fe3111",
  "isSidechain": false,
  "requestId": "req_011CbTLfvHsVFHZ9LjSP1bYL",
  "type": "assistant",
  "uuid": "5ca62793-6d37-4c27-8e90-99e2ab32605e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NWoZ2R9ZvXqKmrmGYrhJs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 388,
      "cache_read_input_tokens": 52391,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 52391,
          "cache_creation_input_tokens": 388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 388
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

_source line 71 · 2026-05-27T15:51:05.281Z_

<details><summary>↩ Tool result · `toolu_01TZm8p3VKD738oLHcD29BDo`</summary>

```text
# OpenReview Forum Status

This is **not** the forum page for "Process Reinforcement through Implicit Rewards" (PRIME).

The page shown is an **error page** from OpenReview.net. The server message indicates: "The Note 6v1hENMQCl was not found." This means either the paper doesn't exist at that URL, or the link is broken.

**No review data is available** to extract from this page. The content consists only of site navigation, footer links, and an error notification.

To locate the PRIME paper's reviews, you would need the correct OpenReview URL or the paper's title/ID.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ca62793-6d37-4c27-8e90-99e2ab32605e",
  "isSidechain": false,
  "promptId": "1c7b6ba7-84ea-4cbf-ae50-f5d8c8abb2e4",
  "type": "user",
  "uuid": "2f889689-164c-457a-ba09-a8a64af802cc",
  "toolUseResult": {
    "bytes": 58573,
    "code": 200,
    "codeText": "OK",
    "result": "# OpenReview Forum Status\n\nThis is **not** the forum page for \"Process Reinforcement through Implicit Rewards\" (PRIME).\n\nThe page shown is an **error page** from OpenReview.net. The server message indicates: \"The Note 6v1hENMQCl was not found.\" This means either the paper doesn't exist at that URL, or the link is broken.\n\n**No review data is available** to extract from this page. The content consists only of site navigation, footer links, and an error notification.\n\nTo locate the PRIME paper's reviews, you would need the correct OpenReview URL or the paper's title/ID.",
    "durationMs": 2517,
    "url": "https://openreview.net/forum?id=6v1hENMQCl"
  },
  "sourceToolAssistantUUID": "5ca62793-6d37-4c27-8e90-99e2ab32605e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-27T15:51:12.386Z_

<details><summary>Logged reasoning block</summary>

```text
I've tried multiple approaches to find the OpenReview page but haven't been able to locate it. This is likely because OpenReview's search interface requires JavaScript rendering that WebFetch can't handle, or the paper might be under a different forum ID. Let me now compose the final analysis based on the very detailed paper content I've already extracted.

I have thoroughly read:
1. The full abstract
2. The complete introduction 
3. The full method section (Sections 3.1, 3.2, 3.3)
4. The experiments (Section 4)
5. The analysis (Section 5)
6. The related work (Section 6)


7. The conclusion (Section 7)
8. The limitations (Appendix A)
9. Multiple appendix sections (B.1-B.6)

This gives me comprehensive coverage of the paper to produce a thorough analysis, despite being unable to locate the OpenReview page for reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f889689-164c-457a-ba09-a8a64af802cc",
  "isSidechain": false,
  "requestId": "req_011CbTLgNRFATNBzUwF7e2fW",
  "type": "assistant",
  "uuid": "d311753a-0b27-4d6d-97a3-d09d1fc9b9be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8b7GvoLz2P8iazoZVz51B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 52779,
      "output_tokens": 1741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1741,
          "cache_read_input_tokens": 52779,
          "cache_creation_input_tokens": 294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 294
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

### Assistant

_source line 73 · 2026-05-27T15:51:52.725Z_

I've now read the paper in extensive detail — full abstract, introduction, method, experiments, analysis, conclusion, and appendices. Despite multiple attempts, I couldn't locate the OpenReview forum page for reviewer comments. Let me now produce the analysis.

```json
{
  "title": "Process Reinforcement through Implicit Rewards (PRIME)",
  "venue": "ICLR 2025",
  "problem_identification": "The authors identified that dense process rewards (PRMs) had been shown effective for inference-time scaling but remained almost entirely unused in RL training of LLMs — a striking gap between theory and practice. They diagnosed the root cause as a scalability bottleneck: updating PRMs online requires step-level process labels, which are either prohibitively expensive (human annotation) or computationally infeasible (Monte Carlo estimation requiring ~10× more rollouts per step). DeepSeek-R1 explicitly acknowledged the same limitation, validating the importance of the gap. The key framing move was decomposing this into three sub-challenges (C1: process rewards are hard to define at step level; C2: online PRM updates don't scale; C3: explicit reward modeling adds overhead), then showing a single mechanism addresses all three.",
  "key_insight": "A language model trained with only outcome-level binary labels using a specific reward parameterization (β·log(π_φ/π_ref)) can be repurposed at token granularity to yield dense process rewards — and critically, this same parameterization allows the PRM to be updated online using nothing more than the policy rollouts and outcome labels already collected for standard RL, completely sidestepping the need for process annotations. The second non-obvious insight was that initializing the PRM from the same SFT checkpoint as the policy (rather than training a dedicated PRM on external data) actually performs better, because it eliminates distribution shift between the reward model and policy from the start.",
  "innovation_type": "combination",
  "method_summary": "PRIME initializes both a policy model and an Implicit PRM from the same SFT (or base) model checkpoint. During each RL iteration, K responses are sampled per prompt, graded by a ground-truth outcome verifier (exact match for math, test cases for code), and filtered by difficulty. The Implicit PRM computes token-level process rewards as r_φ(y_t) = β·log[π_φ(y_t|y<t) / π_ref(y_t|y<t)] via a single forward pass through both models. The PRM is then updated online via cross-entropy loss using only the binary outcome labels on these same rollouts — no step-level annotation needed. For advantage estimation, the authors calculate returns from process rewards and outcome rewards separately (to avoid numerical instability from scale mismatch), each using a leave-one-out baseline, then sum them. This advantage plugs into a standard PPO clip objective. The framework is algorithm-agnostic, demonstrated to work with REINFORCE, GRPO, RLOO, and PPO.",
  "what_makes_it_good": "This paper succeeds because it delivers a rare combination: theoretical elegance (repurposing the implicit reward formulation from inference to training), practical simplicity (no new annotation pipelines, no separate PRM training phase, just initialize from SFT and go), and strong empirical results (matching a model trained on 10× more data). The ablation suite is exceptionally thorough — online vs. offline PRM, SFT vs. dedicated PRM initialization, reward vs. value usage, four different RL algorithms, scaling with compute and rollouts, reward model size sensitivity, zero-shot RL from base models, and comparison with VinePPO — leaving very few stones unturned. The problem framing is also strategically excellent: by explicitly connecting to DeepSeek-R1's stated limitation about PRMs, the authors positioned their work as solving an acknowledged industry-level bottleneck.",
  "limitations_acknowledged": "Experiments were limited to models up to 32B due to resource constraints. The 'Zero' RL setting (directly from base models without SFT) showed promising efficiency but suffered from early saturation attributed to decreasing response diversity, left as future work. The framework assumes access to ground-truth outcome verifiers (rule-based for math/code), which limits applicability to domains without such verifiers.",
  "open_questions": [
    "Can implicit process rewards work effectively in domains without ground-truth outcome verifiers (e.g., open-ended generation, scientific reasoning), perhaps using learned outcome reward models instead of exact-match verifiers?",
    "The 'Zero' RL saturation problem — why does response diversity collapse early when training from base models, and can techniques like diversity-promoting objectives or curriculum strategies overcome this?",
    "How does PRIME interact with test-time compute scaling (e.g., best-of-N, tree search)? The implicit PRM is also a valid inference-time verifier — can the same model serve dual roles during both training and inference for compounding gains?"
  ],
  "building_blocks": [
    "Implicit Process Reward Modeling (Yuan et al., 2024b — reward parameterization as β·log(π_φ/π_ref))",
    "Leave-one-out baseline for variance reduction (RLOO — Ahmadian et al., 2024)",
    "PPO clip surrogate loss (Schulman et al., 2017)",
    "veRL framework for RL training infrastructure (Sheng et al., 2024)",
    "Qwen2.5-Math-7B-Base as foundation model",
    "Rule-based outcome verifiers (exact LaTeX match for math, test case pass rate for code)",
    "Online prompt filtering by difficulty (accuracy-based)",
    "Separate return calculation for dense and sparse rewards to avoid numerical instability"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "PRIME is directly central to synthetic data and self-improvement for mathematical reasoning: it demonstrates that you can achieve dramatic improvements in math reasoning (15.1% average, 23.4% on AIME) using RL with only outcome-level supervision on self-generated rollouts — a form of self-improvement that bypasses the traditional bottleneck of expensive process-level human annotation. The key lesson for our research area is that clever reward formulations can extract dense training signal from sparse labels on synthetic data, and that keeping the reward model on-distribution with the evolving policy (via shared initialization + online updates) is more important than training it on large external datasets."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d311753a-0b27-4d6d-97a3-d09d1fc9b9be",
  "isSidechain": false,
  "requestId": "req_011CbTLgNRFATNBzUwF7e2fW",
  "type": "assistant",
  "uuid": "2493535f-407f-49b2-b24b-47fb5f96203d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R8b7GvoLz2P8iazoZVz51B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 52779,
      "output_tokens": 1741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 294,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1741,
          "cache_read_input_tokens": 52779,
          "cache_creation_input_tokens": 294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 294
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

### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "2493535f-407f-49b2-b24b-47fb5f96203d",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRIME paper on implicit process rewards",
  "sessionId": "ae85f63b-06b5-4781-b92e-92dc801697c7"
}
```

---
