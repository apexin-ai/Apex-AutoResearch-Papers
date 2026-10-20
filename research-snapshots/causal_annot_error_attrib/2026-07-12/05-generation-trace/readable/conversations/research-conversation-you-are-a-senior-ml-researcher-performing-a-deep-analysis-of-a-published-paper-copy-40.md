# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/fd4fd56a-809d-4417-b1f0-e25513d9de0c.jsonl`
- **Structured JSON:** [`b6ce47c80fa7dd8ea564.json`](../../sessions/b6/b6ce47c80fa7dd8ea564.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:08:10.978Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:08:10.978Z",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**\n\n## Paper to analyze\n\n{\n  \"title\": \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\",\n  \"authors\": \"Zheng et al. (Alibaba Qwen Team)\",\n  \"venue\": \"ACL 2025\",\n  \"url\": \"https://arxiv.org/abs/2412.06559\",\n  \"why_important\": \"ACL 2025; introduced the standard benchmark (3,400 test cases with human-annotated error locations) for evaluating process reward models and critic models\",\n  \"one_line_summary\": \"Introduces a benchmark of 3,400 math solutions with expert-annotated error step locations, revealing that existing PRMs fail to generalize beyond GSM8K/MATH to harder problems.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:08:10.982Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:08:10.982Z",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

## Round 1

62 recorded events

### User

_source line 3 · 2026-05-28T05:08:11.036Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-28 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**

## Paper to analyze

{
  "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
  "authors": "Zheng et al. (Alibaba Qwen Team)",
  "venue": "ACL 2025",
  "url": "https://arxiv.org/abs/2412.06559",
  "why_important": "ACL 2025; introduced the standard benchmark (3,400 test cases with human-annotated error locations) for evaluating process reward models and critic models",
  "one_line_summary": "Introduces a benchmark of 3,400 math solutions with expert-annotated error step locations, revealing that existing PRMs fail to generalize beyond GSM8K/MATH to harder problems."
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
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "fe52bfdf-ae28-4dba-ba38-cd248c4d7bf7",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:08:11.035Z_

```json
{
  "parentUuid": "fe52bfdf-ae28-4dba-ba38-cd248c4d7bf7",
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
  "uuid": "56e27efe-d450-4dc7-b673-b8a5afd512fa",
  "timestamp": "2026-05-28T05:08:11.035Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:08:11.035Z_

```json
{
  "parentUuid": "56e27efe-d450-4dc7-b673-b8a5afd512fa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "67df5ade-233a-4a06-9616-b206d1628d91",
  "timestamp": "2026-05-28T05:08:11.035Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
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
  "aiTitle": "Analyze ProcessBench paper for research methodology",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Assistant

_source line 7 · 2026-05-28T05:08:14.612Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this paper by first fetching it from arXiv to read the full content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67df5ade-233a-4a06-9616-b206d1628d91",
  "isSidechain": false,
  "requestId": "req_011CbUPTp7KM7Qtwt4CRKNwu",
  "type": "assistant",
  "uuid": "db7f2f51-c415-4f5b-b725-07adf8bc03eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZTj3akwb1DT2Tj1RkGwBw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 11014,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2187
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

_source line 8 · 2026-05-28T05:08:14.839Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DytZhip89oNtJP4ZsYgdp7`</summary>

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
  "parentUuid": "db7f2f51-c415-4f5b-b725-07adf8bc03eb",
  "isSidechain": false,
  "requestId": "req_011CbUPTp7KM7Qtwt4CRKNwu",
  "type": "assistant",
  "uuid": "6d95ffdb-09ef-4897-a755-138734f2ed20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZTj3akwb1DT2Tj1RkGwBw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 11014,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2187
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

_source line 9 · 2026-05-28T05:08:14.850Z_

<details><summary>↩ Tool result · `toolu_01DytZhip89oNtJP4ZsYgdp7`</summary>

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
  "parentUuid": "6d95ffdb-09ef-4897-a755-138734f2ed20",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "4c2dab5e-e302-4309-bea5-9f097a965200",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6d95ffdb-09ef-4897-a755-138734f2ed20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-28T05:08:18.192Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full PDF (via HTML version) to get comprehensive content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c2dab5e-e302-4309-bea5-9f097a965200",
  "isSidechain": false,
  "requestId": "req_011CbUPU6fUXBn9W11E7TCqD",
  "type": "assistant",
  "uuid": "24d0bd98-9b77-4736-948d-1c30e0d6cb2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XLmqL4FSo2GGdp42PjJJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13201,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13201,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 11 · 2026-05-28T05:08:18.877Z_

Let me fetch the paper from multiple sources to get comprehensive information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24d0bd98-9b77-4736-948d-1c30e0d6cb2c",
  "isSidechain": false,
  "requestId": "req_011CbUPU6fUXBn9W11E7TCqD",
  "type": "assistant",
  "uuid": "9eb5c0d2-2deb-4975-8a4e-9a4fd69b91ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XLmqL4FSo2GGdp42PjJJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13201,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13201,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 12 · 2026-05-28T05:08:20.338Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019g5FUaK6KhUvS2rWBK1sw6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.06559",
  "prompt": "Extract the full abstract, author list, and any other metadata available on this page for the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\". Give me everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eb5c0d2-2deb-4975-8a4e-9a4fd69b91ba",
  "isSidechain": false,
  "requestId": "req_011CbUPU6fUXBn9W11E7TCqD",
  "type": "assistant",
  "uuid": "8b264153-7227-4667-a646-f384eee719c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XLmqL4FSo2GGdp42PjJJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13201,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13201,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 13 · 2026-05-28T05:08:23.358Z_

<details><summary>↩ Tool result · `toolu_011quaFGRcdsLwGCY3JLvVBi`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "180852fe-9635-4cd3-a480-62e69895ae8b",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "224e60f1-bc7c-42d6-80b7-541e5a8a9516",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2412.06559"
  },
  "sourceToolAssistantUUID": "180852fe-9635-4cd3-a480-62e69895ae8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T05:08:23.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011quaFGRcdsLwGCY3JLvVBi`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.06559",
  "prompt": "Extract the FULL text of this paper, including all sections: Introduction, Related Work, Method/Approach, Experiments, Results, Analysis, Discussion, Limitations, and Conclusion. I need the complete technical details including:\n1. How the benchmark was constructed (data collection, annotation process)\n2. What datasets/problems were used\n3. How models were evaluated\n4. Key findings and results tables\n5. Limitations discussed by the authors\n6. Any details about the annotation methodology and quality control\nBe as comprehensive as possible - include specific numbers, model names, and findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b264153-7227-4667-a646-f384eee719c3",
  "isSidechain": false,
  "requestId": "req_011CbUPU6fUXBn9W11E7TCqD",
  "type": "assistant",
  "uuid": "180852fe-9635-4cd3-a480-62e69895ae8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XLmqL4FSo2GGdp42PjJJV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13201,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 372,
          "cache_read_input_tokens": 13201,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
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

_source line 15 · 2026-05-28T05:08:25.871Z_

<details><summary>↩ Tool result · `toolu_019g5FUaK6KhUvS2rWBK1sw6`</summary>

```text
# ProcessBench Paper Metadata

**Title:** "ProcessBench: Identifying Process Errors in Mathematical Reasoning"

**Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin

**arXiv Identifier:** 2412.06559

**Submission Date:** December 9, 2024 (v1); Last revised May 26, 2025 (v4)

**Subject Areas:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)

**Venue:** ACL 2025

**DOI:** https://doi.org/10.48550/arXiv.2412.06559

**Abstract Summary:**

The paper introduces a benchmark containing "3,400 test cases, primarily focused on competition- and Olympiad-level math problems." Each case includes "a step-by-step solution with error location annotated by human experts." The work evaluates two model types: process reward models and critic models. Key findings indicate that existing PRMs struggle generalizing to harder problems, while "QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o," though it underperforms o1-mini.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b264153-7227-4667-a646-f384eee719c3",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "82cd4de9-383f-4cd6-8dcc-c53c870df7c7",
  "toolUseResult": {
    "bytes": 48079,
    "code": 200,
    "codeText": "OK",
    "result": "# ProcessBench Paper Metadata\n\n**Title:** \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\"\n\n**Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin\n\n**arXiv Identifier:** 2412.06559\n\n**Submission Date:** December 9, 2024 (v1); Last revised May 26, 2025 (v4)\n\n**Subject Areas:** Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)\n\n**Venue:** ACL 2025\n\n**DOI:** https://doi.org/10.48550/arXiv.2412.06559\n\n**Abstract Summary:**\n\nThe paper introduces a benchmark containing \"3,400 test cases, primarily focused on competition- and Olympiad-level math problems.\" Each case includes \"a step-by-step solution with error location annotated by human experts.\" The work evaluates two model types: process reward models and critic models. Key findings indicate that existing PRMs struggle generalizing to harder problems, while \"QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o,\" though it underperforms o1-mini.",
    "durationMs": 5529,
    "url": "https://arxiv.org/abs/2412.06559"
  },
  "sourceToolAssistantUUID": "8b264153-7227-4667-a646-f384eee719c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T05:08:29.415Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FKnzsULsEwdTrscBEcP7X7`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.06559v4",
  "prompt": "Extract the FULL text of this paper, including all sections: Introduction, Related Work, Method/Approach, Experiments, Results, Analysis, Discussion, Limitations, and Conclusion. I need the complete technical details including:\n1. How the benchmark was constructed (data collection, annotation process)\n2. What datasets/problems were used\n3. How models were evaluated\n4. Key findings and results tables\n5. Limitations discussed by the authors\n6. Any details about the annotation methodology and quality control\nBe as comprehensive as possible - include specific numbers, model names, and findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82cd4de9-383f-4cd6-8dcc-c53c870df7c7",
  "isSidechain": false,
  "requestId": "req_011CbUPUuZm9rDUDUgG2i635",
  "type": "assistant",
  "uuid": "91df3876-36f6-4882-8ff3-ad4028ac2ad5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWB5vVSGXsmJiooDkYyheo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 13833,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 336,
          "cache_read_input_tokens": 13833,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 17 · 2026-05-28T05:08:29.424Z_

<details><summary>↩ Tool result · `toolu_01FKnzsULsEwdTrscBEcP7X7`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91df3876-36f6-4882-8ff3-ad4028ac2ad5",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "fbb38fdc-ab2d-4b80-bf5a-b9547b6d5ea9",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 7,
    "url": "https://arxiv.org/html/2412.06559v4"
  },
  "sourceToolAssistantUUID": "91df3876-36f6-4882-8ff3-ad4028ac2ad5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T05:08:30.689Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WmZUGdted1iN3hAvAkXJwW`</summary>

```json
{
  "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors+Mathematical+Reasoning",
  "prompt": "Find the OpenReview page for the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" by Zheng et al. Extract any reviewer comments, scores, and author responses if available. Look for the paper submission link."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbb38fdc-ab2d-4b80-bf5a-b9547b6d5ea9",
  "isSidechain": false,
  "requestId": "req_011CbUPUuZm9rDUDUgG2i635",
  "type": "assistant",
  "uuid": "829811af-b7c3-4ad5-8e30-3568d82654d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWB5vVSGXsmJiooDkYyheo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 13833,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 336,
          "cache_read_input_tokens": 13833,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 19 · 2026-05-28T05:08:36.503Z_

<details><summary>↩ Tool result · `toolu_01WmZUGdted1iN3hAvAkXJwW`</summary>

```text
I cannot locate the specific paper "ProcessBench: Identifying Process Errors in Mathematical Reasoning" by Zheng et al. on the provided webpage content.

The content shared appears to be from OpenReview.net's homepage and footer, displaying navigation menus, login options, and general site information. It does not contain any details about this particular paper, reviewer comments, scores, author responses, or submission links.

To find this paper, you would need to:
1. Visit OpenReview.net directly
2. Use their search function to query "ProcessBench" or the authors' names
3. Navigate to the specific paper's page once located

The homepage alone cannot provide the detailed peer review information you're seeking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "829811af-b7c3-4ad5-8e30-3568d82654d7",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "f2f7c86c-09be-4a25-9022-0c20571323df",
  "toolUseResult": {
    "bytes": 62389,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot locate the specific paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" by Zheng et al. on the provided webpage content.\n\nThe content shared appears to be from OpenReview.net's homepage and footer, displaying navigation menus, login options, and general site information. It does not contain any details about this particular paper, reviewer comments, scores, author responses, or submission links.\n\nTo find this paper, you would need to:\n1. Visit OpenReview.net directly\n2. Use their search function to query \"ProcessBench\" or the authors' names\n3. Navigate to the specific paper's page once located\n\nThe homepage alone cannot provide the detailed peer review information you're seeking.",
    "durationMs": 5810,
    "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors+Mathematical+Reasoning"
  },
  "sourceToolAssistantUUID": "829811af-b7c3-4ad5-8e30-3568d82654d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
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
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "f2f7c86c-09be-4a25-9022-0c20571323df",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research methodology",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Tool call

_source line 22 · 2026-05-28T05:08:42.895Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013GdLH1RWvcwYY1jbZBBVsC`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2412.06559",
  "prompt": "Extract the FULL text of this paper comprehensively. I need ALL sections including:\n\n1. INTRODUCTION - the full motivation, problem statement, and contribution claims\n2. RELATED WORK - what prior work existed\n3. BENCHMARK CONSTRUCTION / METHOD - how the 3,400 test cases were created, annotation process, datasets used, difficulty levels\n4. EVALUATION SETUP - how PRMs and critic models were evaluated, metrics used\n5. RESULTS - all key findings, numbers, comparisons between models\n6. ANALYSIS - any ablation studies, error analysis, or deeper investigation\n7. LIMITATIONS - what the authors acknowledge as limitations\n8. CONCLUSION\n\nPlease include specific numbers, model names, dataset names, accuracy figures, and any tables you can extract. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2f7c86c-09be-4a25-9022-0c20571323df",
  "isSidechain": false,
  "requestId": "req_011CbUPVgzk1dZ1i6dpjYiyb",
  "type": "assistant",
  "uuid": "7497d187-7e47-47ac-87cb-6b3edf69a320",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Chykc9o7DkUAheNYKC78wy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 14548,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 14548,
          "cache_creation_input_tokens": 690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 690
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

_source line 23 · 2026-05-28T05:08:43.886Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Fcm141w15Q1wZzpqU7R4wL`</summary>

```json
{
  "url": "https://openreview.net/search?term=ProcessBench&venue=ACL",
  "prompt": "Find and extract any OpenReview page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\". Look for reviewer comments, ratings, strengths, weaknesses, and author responses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7497d187-7e47-47ac-87cb-6b3edf69a320",
  "isSidechain": false,
  "requestId": "req_011CbUPVgzk1dZ1i6dpjYiyb",
  "type": "assistant",
  "uuid": "94c5bc67-4dba-40bd-8639-1a17ecbf0c96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Chykc9o7DkUAheNYKC78wy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 14548,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 14548,
          "cache_creation_input_tokens": 690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 690
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

_source line 24 · 2026-05-28T05:08:46.751Z_

<details><summary>↩ Tool result · `toolu_01Fcm141w15Q1wZzpqU7R4wL`</summary>

```text
I've reviewed the web page content provided, but it only contains the OpenReview.net homepage navigation and footer information. The page does not include any content related to "ProcessBench: Identifying Process Errors in Mathematical Reasoning."

To find that specific paper, you would need to:

1. Visit OpenReview.net directly
2. Use their search function to look up "ProcessBench"
3. Navigate to the paper's submission page

Once there, you should be able to access reviewer comments, ratings, strengths/weaknesses assessments, and any author responses if the review period has concluded and comments are publicly visible.

The content you've provided doesn't contain the paper details or review information you're seeking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94c5bc67-4dba-40bd-8639-1a17ecbf0c96",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "b157726b-1c2a-4e33-8127-1e9e15b56926",
  "toolUseResult": {
    "bytes": 62285,
    "code": 200,
    "codeText": "OK",
    "result": "I've reviewed the web page content provided, but it only contains the OpenReview.net homepage navigation and footer information. The page does not include any content related to \"ProcessBench: Identifying Process Errors in Mathematical Reasoning.\"\n\nTo find that specific paper, you would need to:\n\n1. Visit OpenReview.net directly\n2. Use their search function to look up \"ProcessBench\"\n3. Navigate to the paper's submission page\n\nOnce there, you should be able to access reviewer comments, ratings, strengths/weaknesses assessments, and any author responses if the review period has concluded and comments are publicly visible.\n\nThe content you've provided doesn't contain the paper details or review information you're seeking.",
    "durationMs": 2862,
    "url": "https://openreview.net/search?term=ProcessBench&venue=ACL"
  },
  "sourceToolAssistantUUID": "94c5bc67-4dba-40bd-8639-1a17ecbf0c96",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-28T05:08:50.352Z_

<details><summary>↩ Tool result · `toolu_013GdLH1RWvcwYY1jbZBBVsC`</summary>

```text
I appreciate your request, but I need to be transparent about what I'm seeing: the content you've provided appears to be a PDF file encoded in binary/compressed format (the raw PDF stream data), not readable text content.

The material starts with PDF metadata (`%PDF-1.5`, object definitions, FlateDecode compression) and contains mostly encoded image and font data rather than extractable text. This means I cannot reliably extract the paper's full sections, specific numbers, or detailed findings.

**To help you effectively, I would need:**

1. A plain text version of the paper, or
2. A properly converted PDF-to-text file, or
3. The paper's actual source (ArXiv, conference proceedings, etc.)

**What I can tell you:** Based on the filename reference in the PDF metadata (`qwen-logo.pdf`), this appears to be related to work involving the Qwen model, but I cannot extract the actual paper content from the encoded format provided.

If you can provide the paper in a text-readable format, I'll be happy to comprehensively extract all sections you've requested—including the introduction, methodology, results, analysis, limitations, and conclusion with specific numbers and model names.

[Binary content (application/pdf, 723.4KB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/webfetch-1779944922917-gxmxh0.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7497d187-7e47-47ac-87cb-6b3edf69a320",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "ca41e716-1453-4c75-b5cc-a5df2cc71121",
  "toolUseResult": {
    "bytes": 740748,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I need to be transparent about what I'm seeing: the content you've provided appears to be a PDF file encoded in binary/compressed format (the raw PDF stream data), not readable text content.\n\nThe material starts with PDF metadata (`%PDF-1.5`, object definitions, FlateDecode compression) and contains mostly encoded image and font data rather than extractable text. This means I cannot reliably extract the paper's full sections, specific numbers, or detailed findings.\n\n**To help you effectively, I would need:**\n\n1. A plain text version of the paper, or\n2. A properly converted PDF-to-text file, or\n3. The paper's actual source (ArXiv, conference proceedings, etc.)\n\n**What I can tell you:** Based on the filename reference in the PDF metadata (`qwen-logo.pdf`), this appears to be related to work involving the Qwen model, but I cannot extract the actual paper content from the encoded format provided.\n\nIf you can provide the paper in a text-readable format, I'll be happy to comprehensively extract all sections you've requested—including the introduction, methodology, results, analysis, limitations, and conclusion with specific numbers and model names.\n\n[Binary content (application/pdf, 723.4KB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/webfetch-1779944922917-gxmxh0.pdf]",
    "durationMs": 7452,
    "url": "https://arxiv.org/pdf/2412.06559"
  },
  "sourceToolAssistantUUID": "7497d187-7e47-47ac-87cb-6b3edf69a320",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-28T05:08:53.780Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try the HTML version with a different URL format, and also try to find the paper on ACL Anthology or other sources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca41e716-1453-4c75-b5cc-a5df2cc71121",
  "isSidechain": false,
  "requestId": "req_011CbUPWiATmFnDodhcY7Qn1",
  "type": "assistant",
  "uuid": "640cecb1-11a8-40af-b403-2399e87933fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcRgKoQzUJbHiBTtojdxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 185,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 15238,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 185,
          "output_tokens": 417,
          "cache_read_input_tokens": 15238,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 27 · 2026-05-28T05:08:53.781Z_

Let me try alternative sources to get the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "640cecb1-11a8-40af-b403-2399e87933fd",
  "isSidechain": false,
  "requestId": "req_011CbUPWiATmFnDodhcY7Qn1",
  "type": "assistant",
  "uuid": "245793a2-f6fa-4b02-a79a-2ea3060d72d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcRgKoQzUJbHiBTtojdxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 185,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 15238,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 185,
          "output_tokens": 417,
          "cache_read_input_tokens": 15238,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 28 · 2026-05-28T05:08:55.679Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AsPTE1ZbSAbTSbNEYyTKkf`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2412.06559",
  "prompt": "Extract the FULL text of this paper comprehensively. I need ALL sections including:\n\n1. INTRODUCTION - the full motivation, problem statement, and contribution claims\n2. RELATED WORK - what prior work existed\n3. BENCHMARK CONSTRUCTION / METHOD - how the 3,400 test cases were created, annotation process, datasets used, difficulty levels\n4. EVALUATION SETUP - how PRMs and critic models were evaluated, metrics used\n5. RESULTS - all key findings, numbers, comparisons between models\n6. ANALYSIS - any ablation studies, error analysis, or deeper investigation\n7. LIMITATIONS - what the authors acknowledge as limitations\n8. CONCLUSION\n\nPlease include specific numbers, model names, dataset names, accuracy figures, and any tables you can extract. Be extremely thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "245793a2-f6fa-4b02-a79a-2ea3060d72d2",
  "isSidechain": false,
  "requestId": "req_011CbUPWiATmFnDodhcY7Qn1",
  "type": "assistant",
  "uuid": "fca6c5d2-5a79-4210-b593-594da2af40e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcRgKoQzUJbHiBTtojdxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 185,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 15238,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 185,
          "output_tokens": 417,
          "cache_read_input_tokens": 15238,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 29 · 2026-05-28T05:08:56.837Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B8vR8gQEvzW1VoxSRAmEfj`</summary>

```json
{
  "url": "https://huggingface.co/papers/2412.06559",
  "prompt": "Extract all available information about the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" including the abstract, paper summary, and any community discussion or comments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fca6c5d2-5a79-4210-b593-594da2af40e0",
  "isSidechain": false,
  "requestId": "req_011CbUPWiATmFnDodhcY7Qn1",
  "type": "assistant",
  "uuid": "b2293244-9fb4-4cc7-90af-addb598e03b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGcRgKoQzUJbHiBTtojdxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 185,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 15238,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 185,
          "output_tokens": 417,
          "cache_read_input_tokens": 15238,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 30 · 2026-05-28T05:08:57.634Z_

<details><summary>↩ Tool result · `toolu_01B8vR8gQEvzW1VoxSRAmEfj`</summary>

```text
&lt;persisted-output>
Output too large (65.8KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt

Preview (first 2KB):
# PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning

Chujie Zheng\* Zhenru Zhang Beichen Zhang Runji Lin Keming Lu  
Bowen Yu\* Dayiheng Liu\* Jingren Zhou Junyang Lin\*

Qwen Team, Alibaba Inc.

&lt;https://huggingface.co/datasets/Qwen/ProcessBench>

&lt;https://github.com/QwenLM/ProcessBench>

## Abstract

As language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models (PRMs)* and *critic models*, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope PROCESSBENCH can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.

Figure 1: Overview of evaluation results on PROCESSBENCH (see Table 3 for details).

\*Corresponding authors.# 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "b2293244-9fb4-4cc7-90af-addb598e03b3",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "72cdd2ab-a400-47e1-b2b9-4b8fc791f305",
  "toolUseResult": {
    "bytes": 67553,
    "code": 200,
    "codeText": "OK",
    "result": "# PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning\n\nChujie Zheng\\* Zhenru Zhang Beichen Zhang Runji Lin Keming Lu  \nBowen Yu\\* Dayiheng Liu\\* Jingren Zhou Junyang Lin\\*\n\nQwen Team, Alibaba Inc.\n\n&lt;https://huggingface.co/datasets/Qwen/ProcessBench>\n\n&lt;https://github.com/QwenLM/ProcessBench>\n\n## Abstract\n\nAs language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models (PRMs)* and *critic models*, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope PROCESSBENCH can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.\n\nFigure 1: Overview of evaluation results on PROCESSBENCH (see Table 3 for details).\n\n\\*Corresponding authors.# 1 Introduction\n\nIn recent years, language models have made remarkable progress in complex reasoning tasks, such as mathematics and programming (Hurst et al., 2024; OpenAI, 2024; Yang et al., 2024a,b; Dubey et al., 2024; Wake et al., 2024), yet they still make mistakes when solving challenging problems. To achieve scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024), i.e., effectively supervising AI systems that get close to or go beyond broadly human-level performance, particularly in complex tasks that are difficult for general humans, we expect language models can identify errors in their reasoning process in an automated way. However, existing benchmarks related to assessing language models' reasoning process may be hard to satisfy the growing evaluation demand for the error identification ability. Either their covered problems have become less challenging for recent language models (Zhou et al., 2024; Lightman et al., 2023), or they merely label the correctness of final answers but lack annotations for specific erroneous steps (Lin et al., 2024).\n\n```\n\"id\": \"math-22\",\n\"generator\": \"Qwen2-7B-Instruct\",\n\"problem\": \"Find the integer $n, $ 0 \\le n \\le 180, $ such that $ \\cos n^\\circ = \\cos 568^\\circ.\",\n\"steps\": [\n  \"To find the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\), we can use the periodic properties of the cosine function. First, recall that the cosine function has a period of \\(\\(360^\\circ\\)\\). This means that: \\(\\[\\ \\cos \\ \\theta = \\cos (\\theta + 360k) \\]\\) for any integer \\(\\(k\\)\\).\",\n  \"Given \\(\\(\\cos 568^\\circ\\)\\), we need to reduce this angle to an equivalent angle within the first cycle of \\(\\(0\\)\\) to \\(\\(360^\\circ\\)\\). We do this by subtracting multiples of \\(\\(360^\\circ\\)\\) until we get an angle within this range: \\(\\[\\ 568^\\circ - 360^\\circ = 208^\\circ \\]\\) So, \\(\\(\\cos 568^\\circ = \\cos 208^\\circ\\)\\).\",\n  \"However, we want to find \\(\\(n\\)\\) such that \\(\\(0 \\le n \\le 180\\)\\). Since cosine is also symmetric about \\(\\(180^\\circ\\)\\), we know that: \\(\\[\\ \\cos \\ \\theta = \\cos (180^\\circ - \\theta) \\]\\) Therefore, \\(\\(\\cos 208^\\circ = \\cos (180^\\circ - 208^\\circ)\\)\\), which simplifies to: \\(\\[\\ \\cos 208^\\circ = \\cos (-28^\\circ) \\]\\)\",\n  \"The cosine function is also even, meaning it is symmetric about the y-axis: \\(\\[\\ \\cos (-\\theta) = \\cos \\theta \\]\\) Thus, \\(\\[\\ \\cos (-28^\\circ) = \\cos 28^\\circ \\]\\)\",\n  \"So, \\(\\(n = 28^\\circ\\)\\). Hence, the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\) is \\(\\(n = 28\\)\\). The answer is \\(\\(\\boxed{28}\\)\\).\",\n],\n\"final_answer_correct\": false,\n\"label\": 2\n```\n\nFigure 2: Data example of PROCESSBENCH. The label 2 denotes that the earliest error occurs in the **2nd step** (indexed from 0). For test cases with no errors, the labels are  $-1$ .\n\nIn this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. Figure 2 presents a data example. We prioritize several principles when designing this benchmark:\n\n- • **Problem difficulty and solution diversity.** PROCESSBENCH primarily covers competition- and Olympiad-level math problems and utilizes various open-source language models to generate solutions. This ensures both the difficulty of math problems and the diversity of solution styles, enabling robust evaluation.\n- • **Scale and accuracy.** PROCESSBENCH consists of 3,400 test cases, with all solutions annotated with error locations by multiple human experts. The large scale and expert annotation ensure the data quality and the reliability of evaluation.\n- • **Simplicity.** PROCESSBENCH requires models to identify the earliest erroneous step occurring in the solution, if any exists. This straightforward evaluation protocol enables easy adaptation for various types of models, such as process reward models (PRMs) and critic models.\n\nWe conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models* (PRMs) and *critic models*. For PRMs, we include multiple open-source PRMs (Wang et al., 2024; Skywork, 2024; Xiong et al., 2024b) to assess the correctness of each reasoning step in the solution. For critic models, we prompt general language models like Qwen (Yang et al., 2024a; Qwen, 2024a; Hui et al., 2024) and GPT-4o (Hurst et al., 2024) to critique each solution step by step. We show that, despiterecent growing interest, existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset, which raises questions about the generalization abilities and scalability of the current data synthesis methodologies used to build PRMs. In contrast, general language models manifest non-trivial critique capabilities that can not only identify erroneous steps but also provide detailed explanations. The best open-source model, QwQ-32B-Preview (Qwen, 2024b), has performed competitively with the proprietary GPT-4o model, while it still lags behind the reasoning-specialized o1-mini (OpenAI, 2024). We hope PROCESSBENCH can catalyze future research in automated reasoning process assessment, establishing crucial foundations for scalable oversight of language models.\n\n## 2 Related Work\n\nThere exist several benchmarks or datasets related to assessing language models’ reasoning process. CriticBench (Lin et al., 2024) evaluates language models’ abilities to critique solutions and correct mistakes in various reasoning tasks. MathCheck (Zhou et al., 2024) synthesizes solutions containing erroneous steps using the GSM8K dataset (Cobbe et al., 2021), in which language models are tasked with judging the correctness of final answers or reasoning steps. PRM800K (Lightman et al., 2023) builds on the MATH problems (Hendrycks et al., 2021) and annotates the correctness and soundness of reasoning steps in model-generated solutions. It also has sparked a blooming of research interest in building process reward models (PRMs) (Wang et al., 2024; Xiong et al., 2024b;a).\n\nTable 1: Comparison between PROCESSBENCH and other benchmarks or datasets related to reasoning process assessment (Lin et al., 2024; Zhou et al., 2024; Lightman et al., 2023). &lt;sup>†&lt;/sup>: Solution diversity denotes the diversity of language models used for solution generation, corresponding to the “# Solution Generators” column. &lt;sup>‡&lt;/sup>: For PRM800K, we only count the 90 complete solutions in its phase 1 test set, as the complete solutions in its phase 2 test set are all terminated at the earliest erroneous steps.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>Problem Difficulty&lt;/th>\n&lt;th># Solution Generators&lt;/th>\n&lt;th>Solution Diversity&lt;sup>†&lt;/sup>&lt;/th>\n&lt;th>Step Annotation?&lt;/th>\n&lt;th>Annotator&lt;/th>\n&lt;th>Test Case Size (Identifying Process Errors)&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathCheck-GSM&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>516&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PRM800K&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>90&lt;sup>‡&lt;/sup>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PROCESSBENCH&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>3,400&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nPROCESSBENCH is distinguished from prior benchmarks or datasets in three key aspects, as highlighted in Table 1. **First**, PROCESSBENCH primarily covers more challenging math problems with competition- or Olympiad-level difficulty, which better fit the rapidly growing capabilities of modern language models. **Second**, rather than relying on synthetic data, PROCESSBENCH leverages diverse model-generated natural solutions and employs expert annotation to label erroneous steps, which ensures both real-world applicability and label accuracy. **Third**, the large scale of PROCESSBENCH (3,400 test cases in total) enables more comprehensive and robust evaluation.\n\nThere has also been extensive research on language models’ scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024) and studies on whether language models can identify the errors in their own outputs. Lightman et al. (2023); Wang et al. (2024); Luo et al. (2024) propose to train specialized reward models to supervise language models’ reasoning process (i.e., process reward models or PRMs). Huang et al. (2023); Kamoi et al. (2024) argue that general language models struggle to identify and correct their reasoning errors without external feedback. Saunders et al. (2022); McAleese et al. (2024) show that language models can be trained to write informative critiques for both assisting human evaluation and enabling self-refinement, which favorably scales with increased model capabilities (or model sizes). We believe the improved capabilities of error identification will build strong foundations for language models’ scalable oversight.\n\n## 3 Benchmark Construction\n\n### 3.1 Task Definition\n\nAs shown in Figure 2, given a math problem and a step-by-step solution, PROCESSBENCH requires models to either identify the *earliest-occurring error*, or conclude that all steps are *correct*. Formally,---\n\ngiven a math problem  $P$  and its step-by-step solution  $S = \\{s_0, \\dots, s_{n-1}\\}$ , the task is to output an index  $i \\in \\{-1, 0, \\dots, n-1\\}$ , where  $i = -1$  indicates that all steps are correct, and  $i \\geq 0$  indicates that the earliest error occurs at step  $s_i$ .\n\nTypically but non-inclusively, we consider a step as erroneous if it contains any of the following: (1) **Mathematical errors**: incorrect calculations, algebraic manipulations, or formula applications. (2) **Logical errors**: invalid deductions, unwarranted assumptions, or flawed reasoning steps. (3) **Conceptual errors**: misunderstanding or misapplication of mathematical or problem concepts. (4) **Completeness errors**: missing crucial conditions, constraints, or necessary justifications that affect the solution’s validity. Beyond these types of errors, we encourage human annotators to determine the correctness of reasoning steps based on their own expertise. We do not require human annotators to explicitly annotate error types due to the intractability of intentional categorization.\n\nNote that for steps after the first error, the meaning of their correctness may become ambiguous or debatable: derivations based on incorrect premises can make sense, but still remain on a globally incorrect reasoning path (Lightman et al., 2023). For instance, if step  $k$  contains an error in calculating  $x = 2$ , when it should be  $x = 3$ , subsequent steps may follow valid algebraic rules but operate on an incorrect value of  $x$ , making their individual correctness hard to determine. This is why PROCESSBENCH focuses on identifying the earliest-occurring error in the reasoning process.\n\n### 3.2 Data Collection\n\n**Problem Curation** We collect math problems from the test sets of four public and widely used datasets in mathematical reasoning tasks: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), Olympiad-Bench (He et al., 2024), and Omni-MATH (Gao et al., 2024). Except for GSM8K, which consists of grade school math problems, the other three datasets all contain problems with competition- or Olympiad-level difficulty.\n\n**Solution Generation** We generate solutions using the widely used Qwen (Yang et al., 2024a; Qwen, 2024a; Yang et al., 2024b) and LLaMA (Dubey et al., 2024) series open-source models, resulting in twelve distinct solution generators in total. This includes a wide range of model families, sizes, and downstream task performance, leading to the high diversity of solution styles. Table 4 in Appendix B presents the breakdown of language models used for PROCESSBENCH’s solution generation.\n\n**Solution Reformattng** In mathematical reasoning tasks, double line breaks (i.e., “\\n\\n”) are commonly used to segment solution steps (or paragraphs). However, we observed inconsistent step granularity due to varying solution styles and generation randomness. Some generated solutions frequently used double line breaks, resulting in numerous short, logically incomplete steps, while others used them sparingly, leading to lengthy paragraphs that combine multiple logical components. Such inconsistency in step granularity (and potential improper step segmentation) would impede the standardization of human annotation criteria.\n\nTo address this issue, we adopt a *solution reformattng* method to standardize the step granularity, through which the segmented paragraphs can better correspond to logically complete and progressive reasoning steps. Specifically, we first replace all the line breaks with white space, and then ask Qwen2.5-72B-Instruct to insert double line breaks (i.e., segment paragraphs) while preserving the solution content. Since we found that Qwen2.5-72B-Instruct sometimes alters the solution content ( $< 0.5\\%$ ), we remove those solutions whose final answers change after reformattng (although the content alteration may not influence benchmark construction). Consequently, the reformattng method effectively unifies the step granularity. Figure 6 in Appendix A presents an example of solution reformattng.\n\n**Expert Annotation** To ensure a balance between erroneous and correct solutions, we first use Qwen2.5-72B-Instruct to verify the correctness of final answers in the model-generated solutions against the reference answers. We then respectively sample solutions with correct or incorrect final answers for subsequent annotation in a balanced way to avoid excessive concentration on solutions from either the weakest or strongest models.\n\nWe recruit human experts with doctoral-level mathematical expertise for annotation, and all of them are required to pass the mandatory proficiency examination and annotation tutorial. The annotators are designated with the same task in § 3.1, i.e., identifying the earliest-occurring error in each solution. However, we notice that the competition- or Olympiad-level math problems can still be challenging even for doctoral students majoring in mathematics. According to the feedback from the annotators, although they were not required to solve problems from scratch but rather to identify erroneous steps in presented solutions, they would still become quite hesitant in their annotations when uncertain about the correct solution approach, which affected both the annotation speed and quality. To ease the annotation difficulty,we provide annotators with the reference solutions and answers from the original datasets, while we still explicitly instructed them to inspect and verify the presented model-generated solutions step by step.\n\nEach solution is initially assigned to three different experts. When the initial three annotators cannot reach consensus, we increase the number of annotators until three of them agree on the same result. If an agreement cannot be achieved within five annotators (e.g., annotation distribution of (2, 2, 1) or (2, 1, 1, 1)), we discard this solution. This leads to an overall  $\\sim 30\\%$  discard rate throughout the entire annotation process. We also discard the solutions where the final answers are incorrect (according to the reference answers) but the human annotation results are correct. Although such cases are fairly rare ( $< 1\\%$ ), they are mostly concentrated in the OlympiadBench and Omni-MATH problems (i.e., Olympiad-level ones). The agreement statistics in Table 2 further evidence that the more challenging problems usually need more annotators to achieve the annotation agreement, particularly for those samples with incorrect final answers. These results suggest the inherent challenge of our human annotation task.\n\n### 3.3 Statistics\n\nTable 2: Statistics of PROCESSBENCH. “% Process errors” denotes the proportion of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. “%  $\\geq n$  steps” denotes the proportion of samples whose solutions have  $\\geq n$  steps (split by double line breaks). “% 3/ $n$  agreement” denotes the proportion of samples where the three-annotator agreement is achieved within  $n$  annotators, so  $(\\% 3/3) + (\\% 3/4) + (\\% 3/5) = 100\\%$ .\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td># Samples&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% Process errors&lt;br/>(correct final answers)&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{200-193}{200} = 3.5\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-406}{500} = 18.8\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-339}{500} = 32.2\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-241}{500} = 51.8\\%&lt;/math>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td># Steps&lt;/td>\n&lt;td>5.3&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>6.8&lt;/td>\n&lt;td>6.0&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>8.6&lt;/td>\n&lt;td>7.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 5&lt;/math> steps&lt;/td>\n&lt;td>61.8%&lt;/td>\n&lt;td>57.5%&lt;/td>\n&lt;td>73.6%&lt;/td>\n&lt;td>70.4%&lt;/td>\n&lt;td>92.6%&lt;/td>\n&lt;td>92.3%&lt;/td>\n&lt;td>92.5%&lt;/td>\n&lt;td>81.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 10&lt;/math> steps&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>1.6%&lt;/td>\n&lt;td>17.8%&lt;/td>\n&lt;td>8.9%&lt;/td>\n&lt;td>33.9%&lt;/td>\n&lt;td>27.1%&lt;/td>\n&lt;td>29.2%&lt;/td>\n&lt;td>21.6%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 15&lt;/math> steps&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>0.0%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>2.0%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>8.8%&lt;/td>\n&lt;td>7.5%&lt;/td>\n&lt;td>4.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/3 agreement&lt;/td>\n&lt;td>66.7%&lt;/td>\n&lt;td>95.9%&lt;/td>\n&lt;td>59.4%&lt;/td>\n&lt;td>91.9%&lt;/td>\n&lt;td>52.8%&lt;/td>\n&lt;td>85.0%&lt;/td>\n&lt;td>47.8%&lt;/td>\n&lt;td>80.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/4 agreement&lt;/td>\n&lt;td>21.3%&lt;/td>\n&lt;td>3.6%&lt;/td>\n&lt;td>24.4%&lt;/td>\n&lt;td>4.7%&lt;/td>\n&lt;td>24.1%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>25.6%&lt;/td>\n&lt;td>13.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/5 agreement&lt;/td>\n&lt;td>12.1%&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>16.2%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>23.1%&lt;/td>\n&lt;td>5.9%&lt;/td>\n&lt;td>26.6%&lt;/td>\n&lt;td>6.2%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe resulting PROCESSBENCH has four subsets, consisting of 3,400 test cases in total. The detailed statistics are shown in Table 2 and Table 4 (in Appendix B), and we also plot in Figure 3 the distribution of error positions in erroneous samples. In general, the more challenging the problems, the more solution steps the models generate, and incorrect solutions usually contain more steps than correct ones. However, across all four subsets, a large proportion of errors occur in the earlier steps, such as steps 0-3 in GSM8K and MATH, and steps 1-5 in OlympiadBench and Omni-MATH.\n\nFigure 3: Distribution of error positions (indexed from 0; truncated to 16 for better visualization), corresponding to the *label* field as shown in Figure 2.\n\nIt is noteworthy that while we have intentionally controlled an equal number of solutions with incorrect and correct final answers (200 each for GSM8K and 500 each for other subsets), the annotationFigure 4: Process error ratios per models and subsets, computed as the proportions of samples annotated as *erroneous* among all the samples with *correct final answers* (same as in Table 2). The models used for solution generation slightly vary across different subsets, see Table 4 in Appendix B. We observe that no particular models have notably higher process error rates, while **the process error rates are consistently higher on more difficult problems for all the models.**\n\nresults reveal quite different numbers. Specifically, in the more challenging subsets like OlympiadBench and Omni-MATH, a larger proportion of solutions with correct final answers still contain erroneous steps. For instance, in OlympiadBench,  $\\frac{500-339}{500} = 32.2\\%$  of solutions with correct final answers are found to contain process errors, while in Omni-MATH this proportion is even higher ( $\\frac{500-241}{500} = 51.8\\%$ ). In contrast, these proportions in GSM8K and MATH are  $\\frac{200-193}{200} = 3.5\\%$  and  $\\frac{500-406}{500} = 18.8\\%$ , respectively. In Figure 4, for each model used for solution generation, we plot the ratio of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. We observe that the process error rates are consistently higher on more difficult problems. To our knowledge, our work is **the first to present evidence that on more challenging math problems, current language models are more prone to making process errors even when reaching correct final answers.** This also suggests the underlying limitation of rule-based RL in mathematical reasoning (i.e., rewarding merely according to the correctness of final answers) and further highlights the significance of identifying errors in the reasoning process.\n\n## 4 Evaluation\n\n### 4.1 Setup\n\nFor each subset of PROCESSBENCH, we calculate the accuracies on erroneous and correct samples, respectively, and additionally compute their harmonic mean as the **F1 score**. We primarily refer to F1 scores to compare model performance, as it balances model behaviors between being overly critical and being incapable of identifying errors.\n\nWe consider two types of models in the evaluation on PROCESSBENCH: *process reward models (PRMs)* and *critic models*.\n\n**Process Reward Models (PRMs)** As a recently focal topic, PRMs are proposed to assess and supervise the intermediate steps in language models’ reasoning process (Lightman et al., 2023), thus naturally falling in the scope of our research. In practice, PRMs are typically trained using the process labels for intermediate reasoning steps, outputting either the correctness prediction or a scalar score for each reasoning step during inference. Previous research usually evaluates PRMs based on their improvement in the Best-of-N (BoN) performance of another language model that generates solutions. However, this lacks a finer-grained inspection on their process assessment abilities, and the evaluation reliability can be heavily affected by the underlying solution generation model.\n\nOur evaluation includes several open-source PRMs: (1) Math-Shepherd (Wang et al., 2024), which obtains the process label for each step via estimating the empirical probability of this step leading to the correct final answer. (2) Two LLaMA-3.1-based PRMs from Xiong et al. (2024b), which roughly follow the training methodology of Math-Shepherd but differ in the solution generation models and optimization objectives. (3) Two Qwen2.5-Math-based PRMs recently released by Skywork (2024). (4) We also train a PRM by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K dataset, namely Qwen2.5-Math-7B-PRM800K. See Appendix C for its training details.For the (1)(2)(4) PRMs, we extract the earliest erroneous step from their correctness predictions for reasoning steps. For the (3) PRMs, which produce scalar scores for each reasoning step, we first transform these scores into binary correctness predictions (using a threshold above which steps are considered as correct), and then extract the earliest erroneous step as we do for (1)(2)(4). The transformation threshold is determined as the one giving the highest F1 score on the GSM8K subset.\n\n**Critic Models** Critic models aim to provide feedback and critique to model-generated texts, non-inclusively including verification, reflection, and correction or refinement. They have demonstrated promising utility in achieving scalable oversight (Saunders et al., 2022; McAleese et al., 2024).\n\nTraining critic models for specific domains typically requires significant and specialized effort, which is out of the scope of our work. Instead, we are more interested in the critique capabilities of *general language models*. The task definition (§ 3.1) of PROCESSBENCH enables us to apply simple prompt engineering to repurpose general language models as critic models. We show in Figure 7 in Appendix E the prompt template we implement for our evaluation. Specifically, models are prompted to return the index of the paragraph where the earliest error occurs as the *final answer*, similar to the conventional evaluation protocol for mathematical reasoning tasks (Cobbe et al., 2021; Hendrycks et al., 2021; Yang et al., 2024b).\n\nOur evaluation includes the widely-used Qwen2 (Yang et al., 2024a), Qwen2.5 (Qwen, 2024a), Qwen2.5-Math (Yang et al., 2024b), Qwen2.5-Coder (Hui et al., 2024), and LLaMA-3 (Dubey et al., 2024) series open-source models, as well as the recently released QwQ-32B-Preview reasoning model (Qwen, 2024b). We also evaluate the proprietary GPT-4o (Hurst et al., 2024) and o1-mini (OpenAI, 2024) models. We report the performance of open-source models under majority voting over eight samplings, while we also report their performance under greedy decoding in Table 9 in Appendix F. For the proprietary model GPT-4o, we report the results under greedy decoding, while for o1-mini, we report the results under single sampling as its API does not support customized decoding parameters.\n\nTable 3: Evaluation results on PROCESSBENCH. We report the F1 score of the respective accuracies on erroneous and correct samples. See Table 5 and Table 7 for breakdown of evaluation results.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad-Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>68.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>56.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>★ QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>71.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Alright, I've got this math problem to solve and a solution provided, but I need to review it paragraph by paragraph to find any errors. The problem is to find the integer  $n$ , where  $0 \\leq n \\leq 180$ , such that  $\\cos n^\\circ = \\cos 568^\\circ$ . Let's dive into the solution step by step.\n\n**Paragraph 0:\\*\\***\n\nThe solution starts by recalling that the cosine function has a period of  $360^\\circ$ , which means  $\\cos \\theta = \\cos (\\theta + 360k)$  for any integer  $k$ . That's correct. Cosine repeats every  $360^\\circ$ , so adding or subtracting multiples of  $360^\\circ$  doesn't change the value of the cosine.\n\n**Paragraph 1:\\*\\***\n\nGiven  $\\cos 568^\\circ$ , the solution reduces this angle by subtracting  $360^\\circ$  to get  $208^\\circ$ , since  $568^\\circ - 360^\\circ = 208^\\circ$ . So,  $\\cos 568^\\circ = \\cos 208^\\circ$ . That seems right.  $208^\\circ$  is within one cycle of  $0^\\circ$  to  $360^\\circ$ .\n\n**Paragraph 2:\\*\\***\n\nNow, the solution mentions that cosine is symmetric about  $180^\\circ$ , and states that  $\\cos \\theta = \\cos (180^\\circ - \\theta)$ . Wait a minute, is that correct? Let me think about this. Actually, cosine is symmetric about the y-axis, and the identity  $\\cos \\theta = \\cos (-\\theta)$  reflects that. The identity  $\\cos \\theta = \\cos (360^\\circ - \\theta)$  shows the symmetry about  $360^\\circ$ , but symmetry about  $180^\\circ$  isn't directly related to cosine's even property.\n\nHmm, maybe I need to recall some trigonometric identities here. Let's see, the cosine of an angle in standard position is equal to the cosine of its reference angle, but with a sign depending on the quadrant.  $208^\\circ$  is in the third quadrant, where cosine is negative.\n\nAlternatively, there's the identity  $\\cos (180^\\circ + \\theta) = -\\cos \\theta$ , but that's not directly applicable here.\n\nLet me double-check the symmetry properties. Cosine is an even function, meaning  $\\cos (-\\theta) = \\cos \\theta$ , which shows symmetry about the y-axis. The identity  $\\cos (360^\\circ - \\theta) = \\cos \\theta$  shows symmetry every full cycle.\n\nBut the statement  $\\cos \\theta = \\cos (180^\\circ - \\theta)$  isn't generally true. Let's test it with a specific angle. For example,  $\\theta = 30^\\circ$ :  $\\cos 30^\\circ = \\sqrt{3}/2$ , and  $\\cos (180^\\circ - 30^\\circ) = \\cos 150^\\circ = -\\sqrt{3}/2$ . These are not equal; in fact, they're negatives of each other.\n\nSo, it seems there's an error in this paragraph. The correct identity involving  $180^\\circ$  is  $\\cos (180^\\circ - \\theta) = -\\cos \\theta$ , not  $\\cos \\theta$ .\n\nTherefore, the earliest error occurs in paragraph 2.\n\n**Final Answer:**\n\n$\\boxed{2}$\n\nFigure 5: Critique generated by QwQ-32B-Preview for the test case in Figure 2.\n\n## 4.2 Results\n\nWe present the evaluation results in Table 3. Our observations are summarized as follows:\n\n**Generalization Across Difficulty** From GSM8K and MATH to OlympiadBench and Omni-MATH, with the increased difficulty of math problems, we observe a consistent performance decline for all the models, which suggests the common challenge of both PRMs and critic models in generalization abilities.\n\n**Comparison Between PRMs and Critic Models** We find that existing PRMs typically underperform the top prompt-driven critic models even on the simpler GSM8K and MATH subsets, suggesting that these PRMs struggle to indicate the correctness of the intermediate steps in mathematical reasoning. Moreover, when moving toward the more challenging OlympiadBench and Omni-MATH subsets, PRMs suffer from a more notable performance decline than critic models. This raises our concerns about the **generalization abilities and scalability of the current data synthesis methodologies used to build PRMs**. More specifically, current methodologies, as exemplified by Math-Shepherd (Wang et al., 2024), measure the correctness of an intermediate step by estimating the empirical probability of this step leading to the correct final answer. This kind of approach has two intuitive major issues: (1) The process labels heavily depend on the language model used to generate solutions (i.e., highly “on-policy”), which---\n\nwould naturally fail to indicate the correctness of reasoning steps generated by other models. (2) As demonstrated in § 3.3, current language models are prone to making process errors even when reaching correct final answers. This could substantially invalidate the estimated process labels, particularly on the more challenging math problems. In contrast, **Qwen2.5-Math-7B-PRM800K**, which is straightforwardly fine-tuned on the *fully human-annotated* PRM800K training set, exhibits significantly stronger performance and generalization ability than other PRMs.\n\n**Comparison Among Critic Models** Compared to PRMs, critic models can benefit from separate reasoning processes when critiquing solutions, as they can “think” more before indicating the correctness of each solution step, which leads to their better performance in this error identification task. Within the same model family, the error identification performance favorably scales with increased model sizes. Notably, the recently released reasoning model **QwQ-32B-Preview** **performs best among the open-source models and is highly competitive with GPT-4o**. It is noteworthy that QwQ-32B-Preview achieves more *balanced accuracies on erroneous and correct samples* (see Table 5 and 7 in Appendix F). We show in Figure 5 an example of critique generated by QwQ-32B-Preview to the test case in Figure 2, which not only identifies the erroneous step but also provides the detailed thinking process and explanation. Nevertheless, QwQ-32B-Preview still lags behind o1-mini, suggesting that although the gap in problem-solving performance is getting closer between open-source and proprietary models, there still exists another large gap in their critique capabilities.\n\n## 5 Conclusion\n\nWe introduce the PROCESSBENCH benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, characterized by its high problem difficulty and solution diversity, large scale, rigorous human annotation, and simple evaluation protocol. Through extensive evaluation with existing process reward models (PRMs) and prompt-driven critic models, we draw two main observations: (1) Existing PRMs typically underperform critic models in identifying erroneous reasoning steps, and struggle more to generalize to challenging math problems. (2) Open-source language models, as exemplified by QwQ-32B-Preview, have demonstrated critique capabilities competitive with the proprietary model GPT-4o, yet still lag behind the reasoning-specialized o1-mini model. We envision PROCESSBENCH as a cornerstone testbed for advancing automated reasoning process assessment, a critical step toward achieving scalable oversight of language models.\n\n**Limitations** Despite our best efforts throughout the entire benchmark construction process (§ 3.2), PROCESSBENCH may still contain inaccurate labels of error locations, particularly for the more challenging Olympiad-level math problems. Additionally, the solutions discarded in human annotation (§ 3.2) may involve the particularly challenging problems, which could bias the problem distribution in PROCESSBENCH, although such samples may have exceeded the capabilities of the human annotators in our annotation task.\n\n## References\n\nDario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. *arXiv preprint arXiv:1606.06565*, 2016.\n\nSamuel R Bowman, Jeeyoon Hyun, Ethan Perez, Edwin Chen, Craig Pettit, Scott Heiner, Kamilę Lukošūtė, Amanda Askell, Andy Jones, Anna Chen, et al. Measuring progress on scalable oversight for large language models. *arXiv preprint arXiv:2211.03540*, 2022.\n\nBoxi Cao, Keming Lu, Xinyu Lu, Jiawei Chen, Mengjie Ren, Hao Xiang, Peilin Liu, Yaojie Lu, Ben He, Xianpei Han, et al. Towards scalable automated alignment of llms: A survey. *arXiv preprint arXiv:2406.01252*, 2024.\n\nKarl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n\nAbhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.\n\nBofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. *arXiv preprint arXiv:2410.07985*, 2024.---\n\nChaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n\nJie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. *arXiv preprint arXiv:2310.01798*, 2023.\n\nBinyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, et al. Qwen2.5-coder technical report. *arXiv preprint arXiv:2409.12186*, 2024.\n\nAaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.\n\nRyo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. When can LLMs actually correct their own mistakes? a critical survey of self-correction of LLMs. *Transactions of the Association for Computational Linguistics*, 12:1417–1440, 2024. doi: 10.1162/tacl.a\\_00713. URL &lt;https://aclanthology.org/2024.tacl-1.78>.\n\nWoosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the 29th Symposium on Operating Systems Principles*, pages 611–626, 2023.\n\nHunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. *arXiv preprint arXiv:2305.20050*, 2023.\n\nZicheng Lin, Zhibin Gou, Tian Liang, Ruilin Luo, Haowei Liu, and Yujiu Yang. Criticbench: Benchmarking llms for critique-correct reasoning. *arXiv preprint arXiv:2402.14809*, 2024.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nNat McAleese, Rai Michael Pokorny, Juan Felipe Ceron Uribe, Evgenia Nitishinskaya, Maja Trebacz, and Jan Leike. Llm critics help catch llm bugs. *arXiv preprint arXiv:2407.00215*, 2024.\n\nOpenAI. Openai o1-mini: Advancing cost-efficient reasoning, 2024. URL &lt;https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/>.\n\nTeam Qwen. Qwen2.5: A party of foundation models, September 2024a. URL &lt;https://qwenlm.github.io/blog/qwen2.5/>.\n\nTeam Qwen. Qwq: Reflect deeply on the boundaries of the unknown, November 2024b. URL &lt;https://qwenlm.github.io/blog/qwq-32b-preview/>.\n\nWilliam Saunders, Catherine Yeh, Jeff Wu, Steven Bills, Long Ouyang, Jonathan Ward, and Jan Leike. Self-critiquing models for assisting human evaluators. *arXiv preprint arXiv:2206.05802*, 2022.\n\no1 Team Skywork. Skywork-o1 open series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nAlan Wake, Albert Wang, Bei Chen, CX Lv, Chao Li, Chengen Huang, Chenglin Cai, Chujie Zheng, Daniel Cooper, Ethan Dai, et al. Yi-lightning technical report. *arXiv preprint arXiv:2412.01253*, 2024.\n\nPeiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, August 2024. doi: 10.18653/v1/2024.acl-long.510. URL &lt;https://aclanthology.org/2024.acl-long.510>.\n\nWei Xiong, Chengshuai Shi, Jiaming Shen, Aviv Rosenberg, Zhen Qin, Daniele Calandriello, Misha Khalman, Rishabh Joshi, Bilal Piot, Mohammad Saleh, et al. Building math agents with multi-turn iterative preference learning. *arXiv preprint arXiv:2409.02392*, 2024a.---\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An implementation of generative prm. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024b.\n\nAn Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. *arXiv preprint arXiv:2407.10671*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nZihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F Wong, Xiaowei Huang, Qifeng Wang, and Kaizhu Huang. Is your model really a good math reasoner? evaluating mathematical reasoning with checklist. *arXiv preprint arXiv:2407.08733*, 2024.## A Example of Solution Reformattting\n\n&lt;table border=\"1\">\n&lt;tr>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form&lt;/p>\n&lt;math display=\"block\">\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1,&lt;/math>\n&lt;p>where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length.&lt;/p>\n&lt;p>In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>.&lt;/p>\n&lt;p>First, we calculate the distance from the center to each focus:&lt;/p>\n&lt;math display=\"block\">\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4.&lt;/math>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse.&lt;/p>\n&lt;p>Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;td style=\"vertical-align: middle; text-align: center; padding: 0 10px;\">\n&lt;/td>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form &lt;math>\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1&lt;/math>, where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length. In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>. First, we calculate the distance from the center to each focus: &lt;math>\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4&lt;/math>.&lt;/p>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse. Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>. The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;/tr>\n&lt;/table>\n\nFigure 6: Example of solution reformattting. The left is the original solution (generated by Qwen2-7B-Instruct) and the right is the reformatted one. The problem, coming from the MATH test set, is “The ellipse  $\\frac{(x-6)^2}{25} + \\frac{(y-3)^2}{9} = 1$  has two foci. Find the one with the larger  $x$ -coordinate. Enter your answer as an ordered pair, like  $(2, 1)$ .”\n\n## B Breakdown Statistics of PROCESSBENCH\n\nTable 4: Breakdown statistics of PROCESSBENCH.  $^\\dagger$ : We encountered a code bug when using Llama-3.1-70B-Instruct and Qwen2.5-72B-Instruct to generate solutions for the MATH problems, thus their counts are all zero in the MATH subset of PROCESSBENCH.  $^\\ddagger$ : For the more challenging OlympiadBench and Omni-MATH problems, we exclude models with lower accuracies from subsequent annotation.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Generator&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;math>^\\dagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>13&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>16&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>23&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>53&lt;/td>\n&lt;td>116&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>131&lt;/td>\n&lt;td>31&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>28&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>85&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>19&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-1.5B-Instruct&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>36&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>89&lt;/td>\n&lt;td>42&lt;/td>\n&lt;td>63&lt;/td>\n&lt;td>45&lt;/td>\n&lt;td>96&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>9&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>51&lt;/td>\n&lt;td>64&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>71&lt;/td>\n&lt;td>25&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-1.5B-Instruct&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>10&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>62&lt;/td>\n&lt;td>35&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>75&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>2&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>67&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>88&lt;/td>\n&lt;td>38&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>47&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>99&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>18&lt;/td>\n&lt;td>39&lt;/td>\n&lt;td>59&lt;/td>\n&lt;td>81&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Total&lt;/td>\n&lt;td colspan=\"2\">400&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>## C Training Details of Qwen2.5-Math-7B-PRM800K\n\nQwen2.5-Math-7B-PRM800K is obtained by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K training set. We replace the original language modeling head with a new reward modeling head that outputs binary classification logits. The classification loss is computed at the second line break positions in all the “\\n\\n”. We treat the original 1 and 0 labels in PRM800K as our positive labels, while -1 as negative ones. To eliminate test data contamination, we also remove the PRM800K training samples that have the same problems in PROCESSBENCH. The training was run on eight A100 80GB GPUs.\n\n## D Inference Details\n\nFor solution generation in § 3.2, all the models are set with  $p = 0.9, t = 0.7$ . For majority voting evaluation in § 4, we set  $p = 0.8, t = 0.7, k = 20$  for Qwen2.5-Math-7/72B-Instruct to ensure their normal generation, while all the other models are set with only  $p = 0.9$ . All the inference in the evaluation was run with vLLM (Kwon et al., 2023) on eight A100 80GB GPUs.\n\n## E Prompt Template for Critic Model Evaluation\n\nThe following is a math problem and a solution (split into paragraphs, enclosed with tags and indexed from 0):\n\n[Math Problem]\n\n... (math problem) ...\n\n[Solution]\n\n&lt;paragraph\\_0>\n\n... (paragraph 0 of solution) ...\n\n&lt;/paragraph\\_0>\n\n...\n\n&lt;paragraph\\_n-1>\n\n... (paragraph n-1 of solution) ...\n\n&lt;/paragraph\\_n-1>\n\nYour task is to review and critique the solution paragraph by paragraph. Once you identify an error in a paragraph, return the **index of the paragraph where the earliest error occurs**. Otherwise, return the **index of -1 (which typically denotes \"not found\")**.\n\n**Please put your final answer (i.e., the index) in \\boxed{}.**\n\nFigure 7: Prompt template for critic model evaluation. The **blue texts** indicate the input math problem and the solution (split into paragraphs). The **red texts** describe the required output content and format.## F Supplementary Evaluation Results\n\nTable 5: Breakdown of evaluation results on the GSM8K and MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>24.2&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>21.4&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>37.9&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>43.8&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>90.1&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>54.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>44.9&lt;/td>\n&lt;td>90.6&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>30.5&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>45.1&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>95.8&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 6: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the GSM8K and MATH subsets, which are marginally higher than those in Table 5 that all adopt the threshold selected on the GSM8K subset.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>38.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>49.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>44.1&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Table 7: Breakdown of evaluation results on the OlympiadBench and Omni-MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>15.0&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>8.2&lt;/td>\n&lt;td>43.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>29.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>2.1&lt;/td>\n&lt;td>99.1&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>0.9&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>20.7&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>15.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>26.5&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>28.3&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>24.1&lt;/td>\n&lt;td>92.5&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>38.7&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>90.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>68.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>45.8&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 8: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the OlympiadBench and Omni-MATH subsets, which are slightly higher than those in Table 7 that all adopt the threshold selected on the GSM8K subset.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>\n&lt;td>15.3&lt;/td>\n&lt;td>47.5&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>58.5&lt;/td>\n&lt;td>22.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>\n&lt;td>18.9&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>14.4&lt;/td>\n&lt;td>58.1&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Table 9: Breakdown of evaluation results of the open-source language models (prompted as critic models) using *greedy decoding*.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>28.5&lt;/td>\n&lt;td>9.3&lt;/td>\n&lt;td>14.1&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>5.7&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>55.7&lt;/td>\n&lt;td>21.9&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>17.1&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>7.9&lt;/td>\n&lt;td>11.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>57.5&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>66.1&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>53.9&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>66.2&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>78.6&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>14.5&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>45.9&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>62.2&lt;/td>\n&lt;td>34.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>20.2&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.2&lt;/td>\n&lt;td>25.6&lt;/td>\n&lt;td>0.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>20.3&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>15.2&lt;/td>\n&lt;td>96.1&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>39.7&lt;/td>\n&lt;td>88.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>5.2&lt;/td>\n&lt;td>8.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>67.0&lt;/td>\n&lt;td>35.5&lt;/td>\n&lt;td>66.7&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>23.7&lt;/td>\n&lt;td>63.8&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>47.8&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>63.3&lt;/td>\n&lt;td>40.4&lt;/td>\n&lt;td>86.9&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>59.8&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>49.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>61.4&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>45.3&lt;/td>\n&lt;td>91.9&lt;/td>\n&lt;td>60.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>67.4&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>58.6&lt;/td>\n&lt;td>54.2&lt;/td>\n&lt;td>56.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n  \n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>17.2&lt;/td>\n&lt;td>0.6&lt;/td>\n&lt;td>1.1&lt;/td>\n&lt;td>17.3&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>41.6&lt;/td>\n&lt;td>27.8&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>29.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>19.1&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>17.1&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>39.0&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>30.9&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>86.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>6.4&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;td>11.8&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>17.2&lt;/td>\n&lt;td>95.0&lt;/td>\n&lt;td>29.2&lt;/td>\n&lt;td>18.3&lt;/td>\n&lt;td>93.4&lt;/td>\n&lt;td>30.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>13.3&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>27.8&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>16.6&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>86.7&lt;/td>\n&lt;td>46.5&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>45.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>14.1&lt;/td>\n&lt;td>2.9&lt;/td>\n&lt;td>4.9&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>2.9&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>39.4&lt;/td>\n&lt;td>30.4&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>37.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>43.6&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>30.9&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>44.0&lt;/td>\n&lt;td>27.0&lt;/td>\n&lt;td>72.6&lt;/td>\n&lt;td>39.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>35.9&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>88.5&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>48.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n",
    "durationMs": 792,
    "url": "https://huggingface.co/papers/2412.06559"
  },
  "sourceToolAssistantUUID": "b2293244-9fb4-4cc7-90af-addb598e03b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "72cdd2ab-a400-47e1-b2b9-4b8fc791f305",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research methodology",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Tool result

_source line 33 · 2026-05-28T05:08:59.795Z_

<details><summary>↩ Tool result · `toolu_01AsPTE1ZbSAbTSbNEYyTKkf`</summary>

```text
# Unable to Extract Paper Content

I cannot provide the comprehensive extraction you've requested. The webpage content supplied shows only a header/footer fragment from an ar5iv HTML conversion of arXiv paper 2412.06559.

**What the page shows:**
- A conversion error notification: "Conversion to HTML had a Fatal error and exited abruptly"
- Navigation elements and metadata
- No actual paper content (introduction, methods, results, etc.)

**What's missing:**
The document appears truncated or corrupted during conversion. None of the sections you need—introduction, related work, methods, results, analysis, or conclusions—are present in the provided text.

**To obtain this paper, I recommend:**
1. Visiting the direct arXiv link: https://arxiv.org/abs/2412.06559
2. Downloading the PDF version directly
3. Checking alternative viewers like Papers With Code or Hugging Face Papers

If you can provide the actual paper text or PDF content, I'd be happy to extract and analyze the information you need according to your specifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fca6c5d2-5a79-4210-b593-594da2af40e0",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "9e48db66-8505-473f-aa5b-40d1632c7462",
  "toolUseResult": {
    "bytes": 8105,
    "code": 200,
    "codeText": "OK",
    "result": "# Unable to Extract Paper Content\n\nI cannot provide the comprehensive extraction you've requested. The webpage content supplied shows only a header/footer fragment from an ar5iv HTML conversion of arXiv paper 2412.06559.\n\n**What the page shows:**\n- A conversion error notification: \"Conversion to HTML had a Fatal error and exited abruptly\"\n- Navigation elements and metadata\n- No actual paper content (introduction, methods, results, etc.)\n\n**What's missing:**\nThe document appears truncated or corrupted during conversion. None of the sections you need—introduction, related work, methods, results, analysis, or conclusions—are present in the provided text.\n\n**To obtain this paper, I recommend:**\n1. Visiting the direct arXiv link: https://arxiv.org/abs/2412.06559\n2. Downloading the PDF version directly\n3. Checking alternative viewers like Papers With Code or Hugging Face Papers\n\nIf you can provide the actual paper text or PDF content, I'd be happy to extract and analyze the information you need according to your specifications.",
    "durationMs": 4111,
    "url": "https://ar5iv.labs.arxiv.org/html/2412.06559"
  },
  "sourceToolAssistantUUID": "fca6c5d2-5a79-4210-b593-594da2af40e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-28T05:08:59.800Z_

```json
{
  "parentUuid": "9e48db66-8505-473f-aa5b-40d1632c7462",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7577fab1-c95d-495d-87f1-db728002e051",
  "timestamp": "2026-05-28T05:08:59.800Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-28T05:09:02.850Z_

Good, I got the full content from Hugging Face. Let me read the persisted output file and also try to find the paper on OpenReview for ACL 2025.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7577fab1-c95d-495d-87f1-db728002e051",
  "isSidechain": false,
  "requestId": "req_011CbUPXQaaFVvqxxXd1AV5E",
  "type": "assistant",
  "uuid": "21e180ca-bd3b-4357-9390-1a91c5a54f1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVBNdcv6jUeGvWPkAwv5Xv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 15985,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 620,
          "output_tokens": 292,
          "cache_read_input_tokens": 15985,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 966
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

_source line 36 · 2026-05-28T05:09:03.795Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EGapCkJbzKhWVXjexJDiyx`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21e180ca-bd3b-4357-9390-1a91c5a54f1d",
  "isSidechain": false,
  "requestId": "req_011CbUPXQaaFVvqxxXd1AV5E",
  "type": "assistant",
  "uuid": "ae724534-94e9-4111-a3a4-539bc7310dbd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVBNdcv6jUeGvWPkAwv5Xv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 15985,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 620,
          "output_tokens": 292,
          "cache_read_input_tokens": 15985,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 966
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

_source line 37 · 2026-05-28T05:09:04.110Z_

<details><summary>↩ Tool result · reported error · `toolu_01EGapCkJbzKhWVXjexJDiyx`</summary>

```text
File content (27035 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae724534-94e9-4111-a3a4-539bc7310dbd",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "5aaefaf8-5600-4f89-895d-b440bf5e916c",
  "toolUseResult": "Error: File content (27035 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "ae724534-94e9-4111-a3a4-539bc7310dbd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T05:09:04.912Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VgLGfb5aQ8TxyA1RUJ2S1E`</summary>

```json
{
  "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors&venue=ACL.cc/2025",
  "prompt": "Find the OpenReview submission page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\". Extract reviewer comments, scores, strengths/weaknesses, and author responses if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aaefaf8-5600-4f89-895d-b440bf5e916c",
  "isSidechain": false,
  "requestId": "req_011CbUPXQaaFVvqxxXd1AV5E",
  "type": "assistant",
  "uuid": "fec6832d-4a68-4531-a70a-9aa7f73df403",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVBNdcv6jUeGvWPkAwv5Xv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 620,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 15985,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 620,
          "output_tokens": 292,
          "cache_read_input_tokens": 15985,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 966
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

_source line 39 · 2026-05-28T05:09:07.969Z_

<details><summary>↩ Tool result · `toolu_01VgLGfb5aQ8TxyA1RUJ2S1E`</summary>

```text
I appreciate your request, but I need to be transparent: **the webpage content provided does not contain information about "ProcessBench: Identifying Process Errors in Mathematical Reasoning."**

The content you've shared only shows OpenReview.net's navigation menu, footer, and general site information (login options, venue hosting, sponsorship details, etc.). It does not include:

- The actual submission page for ProcessBench
- Reviewer comments or scores
- Strength/weakness assessments
- Author responses

**To find this information, you would need to:**

1. Visit OpenReview.net directly
2. Search for "ProcessBench" in their submission database
3. Navigate to the paper's dedicated page, which would display peer review details

If you can provide the actual submission page content or a direct link to the paper on OpenReview, I'd be happy to extract the requested information while adhering to your guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fec6832d-4a68-4531-a70a-9aa7f73df403",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "1db2b8e0-4807-4121-8cc9-7728f82c6b40",
  "toolUseResult": {
    "bytes": 62405,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I need to be transparent: **the webpage content provided does not contain information about \"ProcessBench: Identifying Process Errors in Mathematical Reasoning.\"**\n\nThe content you've shared only shows OpenReview.net's navigation menu, footer, and general site information (login options, venue hosting, sponsorship details, etc.). It does not include:\n\n- The actual submission page for ProcessBench\n- Reviewer comments or scores\n- Strength/weakness assessments\n- Author responses\n\n**To find this information, you would need to:**\n\n1. Visit OpenReview.net directly\n2. Search for \"ProcessBench\" in their submission database\n3. Navigate to the paper's dedicated page, which would display peer review details\n\nIf you can provide the actual submission page content or a direct link to the paper on OpenReview, I'd be happy to extract the requested information while adhering to your guidelines.",
    "durationMs": 3054,
    "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors&venue=ACL.cc/2025"
  },
  "sourceToolAssistantUUID": "fec6832d-4a68-4531-a70a-9aa7f73df403",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T05:09:11.148Z_

<details open><summary>🔧 Tool call — Read · `toolu_013QZr1pi325Cpgt2hwLHmCx`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt",
  "limit": 500,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1db2b8e0-4807-4121-8cc9-7728f82c6b40",
  "isSidechain": false,
  "requestId": "req_011CbUPY1XGhiDJWfE5SVya7",
  "type": "assistant",
  "uuid": "b3611dec-8fc8-4e7a-a627-bc7ef94d693f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aU8YqpHr1gbyKvTnSZUDm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 16951,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 16951,
          "cache_creation_input_tokens": 1211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1211
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

_source line 41 · 2026-05-28T05:09:11.422Z_

<details><summary>↩ Tool result · `toolu_013QZr1pi325Cpgt2hwLHmCx`</summary>

````text
0	# PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning
1	
2	Chujie Zheng\* Zhenru Zhang Beichen Zhang Runji Lin Keming Lu  
3	Bowen Yu\* Dayiheng Liu\* Jingren Zhou Junyang Lin\*
4	
5	Qwen Team, Alibaba Inc.
6	
7	&lt;https://huggingface.co/datasets/Qwen/ProcessBench>
8	
9	&lt;https://github.com/QwenLM/ProcessBench>
10	
11	## Abstract
12	
13	As language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models (PRMs)* and *critic models*, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope PROCESSBENCH can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.
14	
15	Figure 1: Overview of evaluation results on PROCESSBENCH (see Table 3 for details).
16	
17	\*Corresponding authors.# 1 Introduction
18	
19	In recent years, language models have made remarkable progress in complex reasoning tasks, such as mathematics and programming (Hurst et al., 2024; OpenAI, 2024; Yang et al., 2024a,b; Dubey et al., 2024; Wake et al., 2024), yet they still make mistakes when solving challenging problems. To achieve scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024), i.e., effectively supervising AI systems that get close to or go beyond broadly human-level performance, particularly in complex tasks that are difficult for general humans, we expect language models can identify errors in their reasoning process in an automated way. However, existing benchmarks related to assessing language models' reasoning process may be hard to satisfy the growing evaluation demand for the error identification ability. Either their covered problems have become less challenging for recent language models (Zhou et al., 2024; Lightman et al., 2023), or they merely label the correctness of final answers but lack annotations for specific erroneous steps (Lin et al., 2024).
20	
21	```
22	"id": "math-22",
23	"generator": "Qwen2-7B-Instruct",
24	"problem": "Find the integer $n, $ 0 \le n \le 180, $ such that $ \cos n^\circ = \cos 568^\circ.",
25	"steps": [
26	  "To find the integer \(\(n\)\), \(\(0 \le n \le 180\)\), such that \(\(\cos n^\circ = \cos 568^\circ\)\), we can use the periodic properties of the cosine function. First, recall that the cosine function has a period of \(\(360^\circ\)\). This means that: \(\[\ \cos \ \theta = \cos (\theta + 360k) \]\) for any integer \(\(k\)\).",
27	  "Given \(\(\cos 568^\circ\)\), we need to reduce this angle to an equivalent angle within the first cycle of \(\(0\)\) to \(\(360^\circ\)\). We do this by subtracting multiples of \(\(360^\circ\)\) until we get an angle within this range: \(\[\ 568^\circ - 360^\circ = 208^\circ \]\) So, \(\(\cos 568^\circ = \cos 208^\circ\)\).",
28	  "However, we want to find \(\(n\)\) such that \(\(0 \le n \le 180\)\). Since cosine is also symmetric about \(\(180^\circ\)\), we know that: \(\[\ \cos \ \theta = \cos (180^\circ - \theta) \]\) Therefore, \(\(\cos 208^\circ = \cos (180^\circ - 208^\circ)\)\), which simplifies to: \(\[\ \cos 208^\circ = \cos (-28^\circ) \]\)",
29	  "The cosine function is also even, meaning it is symmetric about the y-axis: \(\[\ \cos (-\theta) = \cos \theta \]\) Thus, \(\[\ \cos (-28^\circ) = \cos 28^\circ \]\)",
30	  "So, \(\(n = 28^\circ\)\). Hence, the integer \(\(n\)\), \(\(0 \le n \le 180\)\), such that \(\(\cos n^\circ = \cos 568^\circ\)\) is \(\(n = 28\)\). The answer is \(\(\boxed{28}\)\).",
31	],
32	"final_answer_correct": false,
33	"label": 2
34	```
35	
36	Figure 2: Data example of PROCESSBENCH. The label 2 denotes that the earliest error occurs in the **2nd step** (indexed from 0). For test cases with no errors, the labels are  $-1$ .
37	
38	In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. Figure 2 presents a data example. We prioritize several principles when designing this benchmark:
39	
40	- • **Problem difficulty and solution diversity.** PROCESSBENCH primarily covers competition- and Olympiad-level math problems and utilizes various open-source language models to generate solutions. This ensures both the difficulty of math problems and the diversity of solution styles, enabling robust evaluation.
41	- • **Scale and accuracy.** PROCESSBENCH consists of 3,400 test cases, with all solutions annotated with error locations by multiple human experts. The large scale and expert annotation ensure the data quality and the reliability of evaluation.
42	- • **Simplicity.** PROCESSBENCH requires models to identify the earliest erroneous step occurring in the solution, if any exists. This straightforward evaluation protocol enables easy adaptation for various types of models, such as process reward models (PRMs) and critic models.
43	
44	We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models* (PRMs) and *critic models*. For PRMs, we include multiple open-source PRMs (Wang et al., 2024; Skywork, 2024; Xiong et al., 2024b) to assess the correctness of each reasoning step in the solution. For critic models, we prompt general language models like Qwen (Yang et al., 2024a; Qwen, 2024a; Hui et al., 2024) and GPT-4o (Hurst et al., 2024) to critique each solution step by step. We show that, despiterecent growing interest, existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset, which raises questions about the generalization abilities and scalability of the current data synthesis methodologies used to build PRMs. In contrast, general language models manifest non-trivial critique capabilities that can not only identify erroneous steps but also provide detailed explanations. The best open-source model, QwQ-32B-Preview (Qwen, 2024b), has performed competitively with the proprietary GPT-4o model, while it still lags behind the reasoning-specialized o1-mini (OpenAI, 2024). We hope PROCESSBENCH can catalyze future research in automated reasoning process assessment, establishing crucial foundations for scalable oversight of language models.
45	
46	## 2 Related Work
47	
48	There exist several benchmarks or datasets related to assessing language models’ reasoning process. CriticBench (Lin et al., 2024) evaluates language models’ abilities to critique solutions and correct mistakes in various reasoning tasks. MathCheck (Zhou et al., 2024) synthesizes solutions containing erroneous steps using the GSM8K dataset (Cobbe et al., 2021), in which language models are tasked with judging the correctness of final answers or reasoning steps. PRM800K (Lightman et al., 2023) builds on the MATH problems (Hendrycks et al., 2021) and annotates the correctness and soundness of reasoning steps in model-generated solutions. It also has sparked a blooming of research interest in building process reward models (PRMs) (Wang et al., 2024; Xiong et al., 2024b;a).
49	
50	Table 1: Comparison between PROCESSBENCH and other benchmarks or datasets related to reasoning process assessment (Lin et al., 2024; Zhou et al., 2024; Lightman et al., 2023). &lt;sup>†&lt;/sup>: Solution diversity denotes the diversity of language models used for solution generation, corresponding to the “# Solution Generators” column. &lt;sup>‡&lt;/sup>: For PRM800K, we only count the 90 complete solutions in its phase 1 test set, as the complete solutions in its phase 2 test set are all terminated at the earliest erroneous steps.
51	
52	&lt;table border="1">
53	&lt;thead>
54	&lt;tr>
55	&lt;th>&lt;/th>
56	&lt;th>Problem Difficulty&lt;/th>
57	&lt;th># Solution Generators&lt;/th>
58	&lt;th>Solution Diversity&lt;sup>†&lt;/sup>&lt;/th>
59	&lt;th>Step Annotation?&lt;/th>
60	&lt;th>Annotator&lt;/th>
61	&lt;th>Test Case Size (Identifying Process Errors)&lt;/th>
62	&lt;/tr>
63	&lt;/thead>
64	&lt;tbody>
65	&lt;tr>
66	&lt;td>CriticBench&lt;/td>
67	&lt;td>★★&lt;/td>
68	&lt;td>8&lt;/td>
69	&lt;td>★★★&lt;/td>
70	&lt;td>✗&lt;/td>
71	&lt;td>-&lt;/td>
72	&lt;td>-&lt;/td>
73	&lt;/tr>
74	&lt;tr>
75	&lt;td>MathCheck-GSM&lt;/td>
76	&lt;td>★&lt;/td>
77	&lt;td>1&lt;/td>
78	&lt;td>★&lt;/td>
79	&lt;td>✓&lt;/td>
80	&lt;td>Synthetic&lt;/td>
81	&lt;td>516&lt;/td>
82	&lt;/tr>
83	&lt;tr>
84	&lt;td>PRM800K&lt;/td>
85	&lt;td>★★&lt;/td>
86	&lt;td>1&lt;/td>
87	&lt;td>★&lt;/td>
88	&lt;td>✓&lt;/td>
89	&lt;td>Human&lt;/td>
90	&lt;td>90&lt;sup>‡&lt;/sup>&lt;/td>
91	&lt;/tr>
92	&lt;tr>
93	&lt;td>PROCESSBENCH&lt;/td>
94	&lt;td>★★★&lt;/td>
95	&lt;td>12&lt;/td>
96	&lt;td>★★★&lt;/td>
97	&lt;td>✓&lt;/td>
98	&lt;td>Human&lt;/td>
99	&lt;td>3,400&lt;/td>
100	&lt;/tr>
101	&lt;/tbody>
102	&lt;/table>
103	
104	PROCESSBENCH is distinguished from prior benchmarks or datasets in three key aspects, as highlighted in Table 1. **First**, PROCESSBENCH primarily covers more challenging math problems with competition- or Olympiad-level difficulty, which better fit the rapidly growing capabilities of modern language models. **Second**, rather than relying on synthetic data, PROCESSBENCH leverages diverse model-generated natural solutions and employs expert annotation to label erroneous steps, which ensures both real-world applicability and label accuracy. **Third**, the large scale of PROCESSBENCH (3,400 test cases in total) enables more comprehensive and robust evaluation.
105	
106	There has also been extensive research on language models’ scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024) and studies on whether language models can identify the errors in their own outputs. Lightman et al. (2023); Wang et al. (2024); Luo et al. (2024) propose to train specialized reward models to supervise language models’ reasoning process (i.e., process reward models or PRMs). Huang et al. (2023); Kamoi et al. (2024) argue that general language models struggle to identify and correct their reasoning errors without external feedback. Saunders et al. (2022); McAleese et al. (2024) show that language models can be trained to write informative critiques for both assisting human evaluation and enabling self-refinement, which favorably scales with increased model capabilities (or model sizes). We believe the improved capabilities of error identification will build strong foundations for language models’ scalable oversight.
107	
108	## 3 Benchmark Construction
109	
110	### 3.1 Task Definition
111	
112	As shown in Figure 2, given a math problem and a step-by-step solution, PROCESSBENCH requires models to either identify the *earliest-occurring error*, or conclude that all steps are *correct*. Formally,---
113	
114	given a math problem  $P$  and its step-by-step solution  $S = \{s_0, \dots, s_{n-1}\}$ , the task is to output an index  $i \in \{-1, 0, \dots, n-1\}$ , where  $i = -1$  indicates that all steps are correct, and  $i \geq 0$  indicates that the earliest error occurs at step  $s_i$ .
115	
116	Typically but non-inclusively, we consider a step as erroneous if it contains any of the following: (1) **Mathematical errors**: incorrect calculations, algebraic manipulations, or formula applications. (2) **Logical errors**: invalid deductions, unwarranted assumptions, or flawed reasoning steps. (3) **Conceptual errors**: misunderstanding or misapplication of mathematical or problem concepts. (4) **Completeness errors**: missing crucial conditions, constraints, or necessary justifications that affect the solution’s validity. Beyond these types of errors, we encourage human annotators to determine the correctness of reasoning steps based on their own expertise. We do not require human annotators to explicitly annotate error types due to the intractability of intentional categorization.
117	
118	Note that for steps after the first error, the meaning of their correctness may become ambiguous or debatable: derivations based on incorrect premises can make sense, but still remain on a globally incorrect reasoning path (Lightman et al., 2023). For instance, if step  $k$  contains an error in calculating  $x = 2$ , when it should be  $x = 3$ , subsequent steps may follow valid algebraic rules but operate on an incorrect value of  $x$ , making their individual correctness hard to determine. This is why PROCESSBENCH focuses on identifying the earliest-occurring error in the reasoning process.
119	
120	### 3.2 Data Collection
121	
122	**Problem Curation** We collect math problems from the test sets of four public and widely used datasets in mathematical reasoning tasks: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), Olympiad-Bench (He et al., 2024), and Omni-MATH (Gao et al., 2024). Except for GSM8K, which consists of grade school math problems, the other three datasets all contain problems with competition- or Olympiad-level difficulty.
123	
124	**Solution Generation** We generate solutions using the widely used Qwen (Yang et al., 2024a; Qwen, 2024a; Yang et al., 2024b) and LLaMA (Dubey et al., 2024) series open-source models, resulting in twelve distinct solution generators in total. This includes a wide range of model families, sizes, and downstream task performance, leading to the high diversity of solution styles. Table 4 in Appendix B presents the breakdown of language models used for PROCESSBENCH’s solution generation.
125	
126	**Solution Reformattng** In mathematical reasoning tasks, double line breaks (i.e., “\n\n”) are commonly used to segment solution steps (or paragraphs). However, we observed inconsistent step granularity due to varying solution styles and generation randomness. Some generated solutions frequently used double line breaks, resulting in numerous short, logically incomplete steps, while others used them sparingly, leading to lengthy paragraphs that combine multiple logical components. Such inconsistency in step granularity (and potential improper step segmentation) would impede the standardization of human annotation criteria.
127	
128	To address this issue, we adopt a *solution reformattng* method to standardize the step granularity, through which the segmented paragraphs can better correspond to logically complete and progressive reasoning steps. Specifically, we first replace all the line breaks with white space, and then ask Qwen2.5-72B-Instruct to insert double line breaks (i.e., segment paragraphs) while preserving the solution content. Since we found that Qwen2.5-72B-Instruct sometimes alters the solution content ( $< 0.5\%$ ), we remove those solutions whose final answers change after reformattng (although the content alteration may not influence benchmark construction). Consequently, the reformattng method effectively unifies the step granularity. Figure 6 in Appendix A presents an example of solution reformattng.
129	
130	**Expert Annotation** To ensure a balance between erroneous and correct solutions, we first use Qwen2.5-72B-Instruct to verify the correctness of final answers in the model-generated solutions against the reference answers. We then respectively sample solutions with correct or incorrect final answers for subsequent annotation in a balanced way to avoid excessive concentration on solutions from either the weakest or strongest models.
131	
132	We recruit human experts with doctoral-level mathematical expertise for annotation, and all of them are required to pass the mandatory proficiency examination and annotation tutorial. The annotators are designated with the same task in § 3.1, i.e., identifying the earliest-occurring error in each solution. However, we notice that the competition- or Olympiad-level math problems can still be challenging even for doctoral students majoring in mathematics. According to the feedback from the annotators, although they were not required to solve problems from scratch but rather to identify erroneous steps in presented solutions, they would still become quite hesitant in their annotations when uncertain about the correct solution approach, which affected both the annotation speed and quality. To ease the annotation difficulty,we provide annotators with the reference solutions and answers from the original datasets, while we still explicitly instructed them to inspect and verify the presented model-generated solutions step by step.
133	
134	Each solution is initially assigned to three different experts. When the initial three annotators cannot reach consensus, we increase the number of annotators until three of them agree on the same result. If an agreement cannot be achieved within five annotators (e.g., annotation distribution of (2, 2, 1) or (2, 1, 1, 1)), we discard this solution. This leads to an overall  $\sim 30\%$  discard rate throughout the entire annotation process. We also discard the solutions where the final answers are incorrect (according to the reference answers) but the human annotation results are correct. Although such cases are fairly rare ( $< 1\%$ ), they are mostly concentrated in the OlympiadBench and Omni-MATH problems (i.e., Olympiad-level ones). The agreement statistics in Table 2 further evidence that the more challenging problems usually need more annotators to achieve the annotation agreement, particularly for those samples with incorrect final answers. These results suggest the inherent challenge of our human annotation task.
135	
136	### 3.3 Statistics
137	
138	Table 2: Statistics of PROCESSBENCH. “% Process errors” denotes the proportion of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. “%  $\geq n$  steps” denotes the proportion of samples whose solutions have  $\geq n$  steps (split by double line breaks). “% 3/ $n$  agreement” denotes the proportion of samples where the three-annotator agreement is achieved within  $n$  annotators, so  $(\% 3/3) + (\% 3/4) + (\% 3/5) = 100\%$ .
139	
140	&lt;table border="1">
141	&lt;thead>
142	&lt;tr>
143	&lt;th rowspan="2">&lt;/th>
144	&lt;th colspan="2">GSM8K&lt;/th>
145	&lt;th colspan="2">MATH&lt;/th>
146	&lt;th colspan="2">OlympiadBench&lt;/th>
147	&lt;th colspan="2">Omni-MATH&lt;/th>
148	&lt;/tr>
149	&lt;tr>
150	&lt;th>error&lt;/th>
151	&lt;th>correct&lt;/th>
152	&lt;th>error&lt;/th>
153	&lt;th>correct&lt;/th>
154	&lt;th>error&lt;/th>
155	&lt;th>correct&lt;/th>
156	&lt;th>error&lt;/th>
157	&lt;th>correct&lt;/th>
158	&lt;/tr>
159	&lt;/thead>
160	&lt;tbody>
161	&lt;tr>
162	&lt;td># Samples&lt;/td>
163	&lt;td>207&lt;/td>
164	&lt;td>193&lt;/td>
165	&lt;td>594&lt;/td>
166	&lt;td>406&lt;/td>
167	&lt;td>661&lt;/td>
168	&lt;td>339&lt;/td>
169	&lt;td>759&lt;/td>
170	&lt;td>241&lt;/td>
171	&lt;/tr>
172	&lt;tr>
173	&lt;td>% Process errors&lt;br/>(correct final answers)&lt;/td>
174	&lt;td colspan="2">&lt;math>\frac{200-193}{200} = 3.5\%&lt;/math>&lt;/td>
175	&lt;td colspan="2">&lt;math>\frac{500-406}{500} = 18.8\%&lt;/math>&lt;/td>
176	&lt;td colspan="2">&lt;math>\frac{500-339}{500} = 32.2\%&lt;/math>&lt;/td>
177	&lt;td colspan="2">&lt;math>\frac{500-241}{500} = 51.8\%&lt;/math>&lt;/td>
178	&lt;/tr>
179	&lt;tr>
180	&lt;td># Steps&lt;/td>
181	&lt;td>5.3&lt;/td>
182	&lt;td>5.1&lt;/td>
183	&lt;td>6.8&lt;/td>
184	&lt;td>6.0&lt;/td>
185	&lt;td>8.9&lt;/td>
186	&lt;td>8.7&lt;/td>
187	&lt;td>8.6&lt;/td>
188	&lt;td>7.4&lt;/td>
189	&lt;/tr>
190	&lt;tr>
191	&lt;td>% &lt;math>\geq 5&lt;/math> steps&lt;/td>
192	&lt;td>61.8%&lt;/td>
193	&lt;td>57.5%&lt;/td>
194	&lt;td>73.6%&lt;/td>
195	&lt;td>70.4%&lt;/td>
196	&lt;td>92.6%&lt;/td>
197	&lt;td>92.3%&lt;/td>
198	&lt;td>92.5%&lt;/td>
199	&lt;td>81.7%&lt;/td>
200	&lt;/tr>
201	&lt;tr>
202	&lt;td>% &lt;math>\geq 10&lt;/math> steps&lt;/td>
203	&lt;td>3.4%&lt;/td>
204	&lt;td>1.6%&lt;/td>
205	&lt;td>17.8%&lt;/td>
206	&lt;td>8.9%&lt;/td>
207	&lt;td>33.9%&lt;/td>
208	&lt;td>27.1%&lt;/td>
209	&lt;td>29.2%&lt;/td>
210	&lt;td>21.6%&lt;/td>
211	&lt;/tr>
212	&lt;tr>
213	&lt;td>% &lt;math>\geq 15&lt;/math> steps&lt;/td>
214	&lt;td>0.5%&lt;/td>
215	&lt;td>0.0%&lt;/td>
216	&lt;td>3.4%&lt;/td>
217	&lt;td>2.0%&lt;/td>
218	&lt;td>9.1%&lt;/td>
219	&lt;td>8.8%&lt;/td>
220	&lt;td>7.5%&lt;/td>
221	&lt;td>4.1%&lt;/td>
222	&lt;/tr>
223	&lt;tr>
224	&lt;td>% 3/3 agreement&lt;/td>
225	&lt;td>66.7%&lt;/td>
226	&lt;td>95.9%&lt;/td>
227	&lt;td>59.4%&lt;/td>
228	&lt;td>91.9%&lt;/td>
229	&lt;td>52.8%&lt;/td>
230	&lt;td>85.0%&lt;/td>
231	&lt;td>47.8%&lt;/td>
232	&lt;td>80.1%&lt;/td>
233	&lt;/tr>
234	&lt;tr>
235	&lt;td>% 3/4 agreement&lt;/td>
236	&lt;td>21.3%&lt;/td>
237	&lt;td>3.6%&lt;/td>
238	&lt;td>24.4%&lt;/td>
239	&lt;td>4.7%&lt;/td>
240	&lt;td>24.1%&lt;/td>
241	&lt;td>9.1%&lt;/td>
242	&lt;td>25.6%&lt;/td>
243	&lt;td>13.7%&lt;/td>
244	&lt;/tr>
245	&lt;tr>
246	&lt;td>% 3/5 agreement&lt;/td>
247	&lt;td>12.1%&lt;/td>
248	&lt;td>0.5%&lt;/td>
249	&lt;td>16.2%&lt;/td>
250	&lt;td>3.4%&lt;/td>
251	&lt;td>23.1%&lt;/td>
252	&lt;td>5.9%&lt;/td>
253	&lt;td>26.6%&lt;/td>
254	&lt;td>6.2%&lt;/td>
255	&lt;/tr>
256	&lt;/tbody>
257	&lt;/table>
258	
259	The resulting PROCESSBENCH has four subsets, consisting of 3,400 test cases in total. The detailed statistics are shown in Table 2 and Table 4 (in Appendix B), and we also plot in Figure 3 the distribution of error positions in erroneous samples. In general, the more challenging the problems, the more solution steps the models generate, and incorrect solutions usually contain more steps than correct ones. However, across all four subsets, a large proportion of errors occur in the earlier steps, such as steps 0-3 in GSM8K and MATH, and steps 1-5 in OlympiadBench and Omni-MATH.
260	
261	Figure 3: Distribution of error positions (indexed from 0; truncated to 16 for better visualization), corresponding to the *label* field as shown in Figure 2.
262	
263	It is noteworthy that while we have intentionally controlled an equal number of solutions with incorrect and correct final answers (200 each for GSM8K and 500 each for other subsets), the annotationFigure 4: Process error ratios per models and subsets, computed as the proportions of samples annotated as *erroneous* among all the samples with *correct final answers* (same as in Table 2). The models used for solution generation slightly vary across different subsets, see Table 4 in Appendix B. We observe that no particular models have notably higher process error rates, while **the process error rates are consistently higher on more difficult problems for all the models.**
264	
265	results reveal quite different numbers. Specifically, in the more challenging subsets like OlympiadBench and Omni-MATH, a larger proportion of solutions with correct final answers still contain erroneous steps. For instance, in OlympiadBench,  $\frac{500-339}{500} = 32.2\%$  of solutions with correct final answers are found to contain process errors, while in Omni-MATH this proportion is even higher ( $\frac{500-241}{500} = 51.8\%$ ). In contrast, these proportions in GSM8K and MATH are  $\frac{200-193}{200} = 3.5\%$  and  $\frac{500-406}{500} = 18.8\%$ , respectively. In Figure 4, for each model used for solution generation, we plot the ratio of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. We observe that the process error rates are consistently higher on more difficult problems. To our knowledge, our work is **the first to present evidence that on more challenging math problems, current language models are more prone to making process errors even when reaching correct final answers.** This also suggests the underlying limitation of rule-based RL in mathematical reasoning (i.e., rewarding merely according to the correctness of final answers) and further highlights the significance of identifying errors in the reasoning process.
266	
267	## 4 Evaluation
268	
269	### 4.1 Setup
270	
271	For each subset of PROCESSBENCH, we calculate the accuracies on erroneous and correct samples, respectively, and additionally compute their harmonic mean as the **F1 score**. We primarily refer to F1 scores to compare model performance, as it balances model behaviors between being overly critical and being incapable of identifying errors.
272	
273	We consider two types of models in the evaluation on PROCESSBENCH: *process reward models (PRMs)* and *critic models*.
274	
275	**Process Reward Models (PRMs)** As a recently focal topic, PRMs are proposed to assess and supervise the intermediate steps in language models’ reasoning process (Lightman et al., 2023), thus naturally falling in the scope of our research. In practice, PRMs are typically trained using the process labels for intermediate reasoning steps, outputting either the correctness prediction or a scalar score for each reasoning step during inference. Previous research usually evaluates PRMs based on their improvement in the Best-of-N (BoN) performance of another language model that generates solutions. However, this lacks a finer-grained inspection on their process assessment abilities, and the evaluation reliability can be heavily affected by the underlying solution generation model.
276	
277	Our evaluation includes several open-source PRMs: (1) Math-Shepherd (Wang et al., 2024), which obtains the process label for each step via estimating the empirical probability of this step leading to the correct final answer. (2) Two LLaMA-3.1-based PRMs from Xiong et al. (2024b), which roughly follow the training methodology of Math-Shepherd but differ in the solution generation models and optimization objectives. (3) Two Qwen2.5-Math-based PRMs recently released by Skywork (2024). (4) We also train a PRM by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K dataset, namely Qwen2.5-Math-7B-PRM800K. See Appendix C for its training details.For the (1)(2)(4) PRMs, we extract the earliest erroneous step from their correctness predictions for reasoning steps. For the (3) PRMs, which produce scalar scores for each reasoning step, we first transform these scores into binary correctness predictions (using a threshold above which steps are considered as correct), and then extract the earliest erroneous step as we do for (1)(2)(4). The transformation threshold is determined as the one giving the highest F1 score on the GSM8K subset.
278	
279	**Critic Models** Critic models aim to provide feedback and critique to model-generated texts, non-inclusively including verification, reflection, and correction or refinement. They have demonstrated promising utility in achieving scalable oversight (Saunders et al., 2022; McAleese et al., 2024).
280	
281	Training critic models for specific domains typically requires significant and specialized effort, which is out of the scope of our work. Instead, we are more interested in the critique capabilities of *general language models*. The task definition (§ 3.1) of PROCESSBENCH enables us to apply simple prompt engineering to repurpose general language models as critic models. We show in Figure 7 in Appendix E the prompt template we implement for our evaluation. Specifically, models are prompted to return the index of the paragraph where the earliest error occurs as the *final answer*, similar to the conventional evaluation protocol for mathematical reasoning tasks (Cobbe et al., 2021; Hendrycks et al., 2021; Yang et al., 2024b).
282	
283	Our evaluation includes the widely-used Qwen2 (Yang et al., 2024a), Qwen2.5 (Qwen, 2024a), Qwen2.5-Math (Yang et al., 2024b), Qwen2.5-Coder (Hui et al., 2024), and LLaMA-3 (Dubey et al., 2024) series open-source models, as well as the recently released QwQ-32B-Preview reasoning model (Qwen, 2024b). We also evaluate the proprietary GPT-4o (Hurst et al., 2024) and o1-mini (OpenAI, 2024) models. We report the performance of open-source models under majority voting over eight samplings, while we also report their performance under greedy decoding in Table 9 in Appendix F. For the proprietary model GPT-4o, we report the results under greedy decoding, while for o1-mini, we report the results under single sampling as its API does not support customized decoding parameters.
284	
285	Table 3: Evaluation results on PROCESSBENCH. We report the F1 score of the respective accuracies on erroneous and correct samples. See Table 5 and Table 7 for breakdown of evaluation results.
286	
287	&lt;table border="1">
288	&lt;thead>
289	&lt;tr>
290	&lt;th>Model&lt;/th>
291	&lt;th>GSM8K&lt;/th>
292	&lt;th>MATH&lt;/th>
293	&lt;th>Olympiad-Bench&lt;/th>
294	&lt;th>Omni-MATH&lt;/th>
295	&lt;th>Average&lt;/th>
296	&lt;/tr>
297	&lt;/thead>
298	&lt;tbody>
299	&lt;tr>
300	&lt;td colspan="6" style="text-align: center;">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>
301	&lt;/tr>
302	&lt;tr>
303	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
304	&lt;td>47.9&lt;/td>
305	&lt;td>29.5&lt;/td>
306	&lt;td>24.8&lt;/td>
307	&lt;td>23.8&lt;/td>
308	&lt;td>31.5&lt;/td>
309	&lt;/tr>
310	&lt;tr>
311	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
312	&lt;td>50.4&lt;/td>
313	&lt;td>33.4&lt;/td>
314	&lt;td>13.8&lt;/td>
315	&lt;td>15.8&lt;/td>
316	&lt;td>28.4&lt;/td>
317	&lt;/tr>
318	&lt;tr>
319	&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>
320	&lt;td>38.8&lt;/td>
321	&lt;td>33.8&lt;/td>
322	&lt;td>16.9&lt;/td>
323	&lt;td>16.9&lt;/td>
324	&lt;td>26.6&lt;/td>
325	&lt;/tr>
326	&lt;tr>
327	&lt;td>Skywork-PRM-1.5B&lt;/td>
328	&lt;td>59.0&lt;/td>
329	&lt;td>48.0&lt;/td>
330	&lt;td>19.3&lt;/td>
331	&lt;td>19.2&lt;/td>
332	&lt;td>36.4&lt;/td>
333	&lt;/tr>
334	&lt;tr>
335	&lt;td>Skywork-PRM-7B&lt;/td>
336	&lt;td>&lt;b>70.8&lt;/b>&lt;/td>
337	&lt;td>53.6&lt;/td>
338	&lt;td>22.9&lt;/td>
339	&lt;td>21.0&lt;/td>
340	&lt;td>42.1&lt;/td>
341	&lt;/tr>
342	&lt;tr>
343	&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>
344	&lt;td>&lt;b>68.2&lt;/b>&lt;/td>
345	&lt;td>&lt;b>62.6&lt;/b>&lt;/td>
346	&lt;td>&lt;b>50.7&lt;/b>&lt;/td>
347	&lt;td>&lt;b>44.3&lt;/b>&lt;/td>
348	&lt;td>&lt;b>56.5&lt;/b>&lt;/td>
349	&lt;/tr>
350	&lt;tr>
351	&lt;td colspan="6" style="text-align: center;">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>
352	&lt;/tr>
353	&lt;tr>
354	&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>
355	&lt;td>13.1&lt;/td>
356	&lt;td>13.8&lt;/td>
357	&lt;td>4.8&lt;/td>
358	&lt;td>12.6&lt;/td>
359	&lt;td>11.1&lt;/td>
360	&lt;/tr>
361	&lt;tr>
362	&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>
363	&lt;td>52.2&lt;/td>
364	&lt;td>22.8&lt;/td>
365	&lt;td>21.2&lt;/td>
366	&lt;td>20.0&lt;/td>
367	&lt;td>29.1&lt;/td>
368	&lt;/tr>
369	&lt;tr>
370	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
371	&lt;td>10.9&lt;/td>
372	&lt;td>5.1&lt;/td>
373	&lt;td>2.8&lt;/td>
374	&lt;td>1.6&lt;/td>
375	&lt;td>5.1&lt;/td>
376	&lt;/tr>
377	&lt;tr>
378	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
379	&lt;td>74.9&lt;/td>
380	&lt;td>48.2&lt;/td>
381	&lt;td>46.7&lt;/td>
382	&lt;td>41.0&lt;/td>
383	&lt;td>52.7&lt;/td>
384	&lt;/tr>
385	&lt;tr>
386	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
387	&lt;td>82.9&lt;/td>
388	&lt;td>59.4&lt;/td>
389	&lt;td>46.7&lt;/td>
390	&lt;td>43.0&lt;/td>
391	&lt;td>58.0&lt;/td>
392	&lt;/tr>
393	&lt;tr>
394	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
395	&lt;td>26.8&lt;/td>
396	&lt;td>25.7&lt;/td>
397	&lt;td>14.2&lt;/td>
398	&lt;td>12.7&lt;/td>
399	&lt;td>19.9&lt;/td>
400	&lt;/tr>
401	&lt;tr>
402	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
403	&lt;td>65.8&lt;/td>
404	&lt;td>52.1&lt;/td>
405	&lt;td>32.5&lt;/td>
406	&lt;td>31.7&lt;/td>
407	&lt;td>45.5&lt;/td>
408	&lt;/tr>
409	&lt;tr>
410	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
411	&lt;td>14.3&lt;/td>
412	&lt;td>6.5&lt;/td>
413	&lt;td>4.1&lt;/td>
414	&lt;td>1.8&lt;/td>
415	&lt;td>6.7&lt;/td>
416	&lt;/tr>
417	&lt;tr>
418	&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>
419	&lt;td>50.1&lt;/td>
420	&lt;td>39.9&lt;/td>
421	&lt;td>34.0&lt;/td>
422	&lt;td>27.3&lt;/td>
423	&lt;td>37.8&lt;/td>
424	&lt;/tr>
425	&lt;tr>
426	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
427	&lt;td>68.9&lt;/td>
428	&lt;td>60.1&lt;/td>
429	&lt;td>48.9&lt;/td>
430	&lt;td>46.3&lt;/td>
431	&lt;td>56.1&lt;/td>
432	&lt;/tr>
433	&lt;tr>
434	&lt;td>Qwen2-7B-Instruct&lt;/td>
435	&lt;td>8.4&lt;/td>
436	&lt;td>19.0&lt;/td>
437	&lt;td>14.7&lt;/td>
438	&lt;td>12.1&lt;/td>
439	&lt;td>13.6&lt;/td>
440	&lt;/tr>
441	&lt;tr>
442	&lt;td>Qwen2-72B-Instruct&lt;/td>
443	&lt;td>67.6&lt;/td>
444	&lt;td>49.2&lt;/td>
445	&lt;td>42.1&lt;/td>
446	&lt;td>40.2&lt;/td>
447	&lt;td>49.8&lt;/td>
448	&lt;/tr>
449	&lt;tr>
450	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
451	&lt;td>36.5&lt;/td>
452	&lt;td>36.6&lt;/td>
453	&lt;td>29.7&lt;/td>
454	&lt;td>27.4&lt;/td>
455	&lt;td>32.6&lt;/td>
456	&lt;/tr>
457	&lt;tr>
458	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
459	&lt;td>69.3&lt;/td>
460	&lt;td>53.3&lt;/td>
461	&lt;td>45.0&lt;/td>
462	&lt;td>41.3&lt;/td>
463	&lt;td>52.2&lt;/td>
464	&lt;/tr>
465	&lt;tr>
466	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
467	&lt;td>65.6&lt;/td>
468	&lt;td>53.1&lt;/td>
469	&lt;td>40.0&lt;/td>
470	&lt;td>38.3&lt;/td>
471	&lt;td>49.3&lt;/td>
472	&lt;/tr>
473	&lt;tr>
474	&lt;td>Qwen2.5-72B-Instruct&lt;/td>
475	&lt;td>76.2&lt;/td>
476	&lt;td>61.8&lt;/td>
477	&lt;td>54.6&lt;/td>
478	&lt;td>52.2&lt;/td>
479	&lt;td>61.2&lt;/td>
480	&lt;/tr>
481	&lt;tr>
482	&lt;td>&lt;b>★ QwQ-32B-Preview&lt;/b>&lt;/td>
483	&lt;td>&lt;b>88.0&lt;/b>&lt;/td>
484	&lt;td>&lt;b>78.7&lt;/b>&lt;/td>
485	&lt;td>&lt;b>57.8&lt;/b>&lt;/td>
486	&lt;td>&lt;b>61.3&lt;/b>&lt;/td>
487	&lt;td>&lt;b>71.5&lt;/b>&lt;/td>
488	&lt;/tr>
489	&lt;tr>
490	&lt;td colspan="6" style="text-align: center;">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>
491	&lt;/tr>
492	&lt;tr>
493	&lt;td>GPT-4o-0806&lt;/td>
494	&lt;td>79.2&lt;/td>
495	&lt;td>63.6&lt;/td>
496	&lt;td>51.4&lt;/td>
497	&lt;td>53.5&lt;/td>
498	&lt;td>61.9&lt;/td>
499	&lt;/tr>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "b3611dec-8fc8-4e7a-a627-bc7ef94d693f",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "ec742eed-bc4a-42bb-b532-049aa9a7715d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt",
      "content": "# PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning\n\nChujie Zheng\\* Zhenru Zhang Beichen Zhang Runji Lin Keming Lu  \nBowen Yu\\* Dayiheng Liu\\* Jingren Zhou Junyang Lin\\*\n\nQwen Team, Alibaba Inc.\n\n&lt;https://huggingface.co/datasets/Qwen/ProcessBench>\n\n&lt;https://github.com/QwenLM/ProcessBench>\n\n## Abstract\n\nAs language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models (PRMs)* and *critic models*, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope PROCESSBENCH can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.\n\nFigure 1: Overview of evaluation results on PROCESSBENCH (see Table 3 for details).\n\n\\*Corresponding authors.# 1 Introduction\n\nIn recent years, language models have made remarkable progress in complex reasoning tasks, such as mathematics and programming (Hurst et al., 2024; OpenAI, 2024; Yang et al., 2024a,b; Dubey et al., 2024; Wake et al., 2024), yet they still make mistakes when solving challenging problems. To achieve scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024), i.e., effectively supervising AI systems that get close to or go beyond broadly human-level performance, particularly in complex tasks that are difficult for general humans, we expect language models can identify errors in their reasoning process in an automated way. However, existing benchmarks related to assessing language models' reasoning process may be hard to satisfy the growing evaluation demand for the error identification ability. Either their covered problems have become less challenging for recent language models (Zhou et al., 2024; Lightman et al., 2023), or they merely label the correctness of final answers but lack annotations for specific erroneous steps (Lin et al., 2024).\n\n```\n\"id\": \"math-22\",\n\"generator\": \"Qwen2-7B-Instruct\",\n\"problem\": \"Find the integer $n, $ 0 \\le n \\le 180, $ such that $ \\cos n^\\circ = \\cos 568^\\circ.\",\n\"steps\": [\n  \"To find the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\), we can use the periodic properties of the cosine function. First, recall that the cosine function has a period of \\(\\(360^\\circ\\)\\). This means that: \\(\\[\\ \\cos \\ \\theta = \\cos (\\theta + 360k) \\]\\) for any integer \\(\\(k\\)\\).\",\n  \"Given \\(\\(\\cos 568^\\circ\\)\\), we need to reduce this angle to an equivalent angle within the first cycle of \\(\\(0\\)\\) to \\(\\(360^\\circ\\)\\). We do this by subtracting multiples of \\(\\(360^\\circ\\)\\) until we get an angle within this range: \\(\\[\\ 568^\\circ - 360^\\circ = 208^\\circ \\]\\) So, \\(\\(\\cos 568^\\circ = \\cos 208^\\circ\\)\\).\",\n  \"However, we want to find \\(\\(n\\)\\) such that \\(\\(0 \\le n \\le 180\\)\\). Since cosine is also symmetric about \\(\\(180^\\circ\\)\\), we know that: \\(\\[\\ \\cos \\ \\theta = \\cos (180^\\circ - \\theta) \\]\\) Therefore, \\(\\(\\cos 208^\\circ = \\cos (180^\\circ - 208^\\circ)\\)\\), which simplifies to: \\(\\[\\ \\cos 208^\\circ = \\cos (-28^\\circ) \\]\\)\",\n  \"The cosine function is also even, meaning it is symmetric about the y-axis: \\(\\[\\ \\cos (-\\theta) = \\cos \\theta \\]\\) Thus, \\(\\[\\ \\cos (-28^\\circ) = \\cos 28^\\circ \\]\\)\",\n  \"So, \\(\\(n = 28^\\circ\\)\\). Hence, the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\) is \\(\\(n = 28\\)\\). The answer is \\(\\(\\boxed{28}\\)\\).\",\n],\n\"final_answer_correct\": false,\n\"label\": 2\n```\n\nFigure 2: Data example of PROCESSBENCH. The label 2 denotes that the earliest error occurs in the **2nd step** (indexed from 0). For test cases with no errors, the labels are  $-1$ .\n\nIn this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. Figure 2 presents a data example. We prioritize several principles when designing this benchmark:\n\n- • **Problem difficulty and solution diversity.** PROCESSBENCH primarily covers competition- and Olympiad-level math problems and utilizes various open-source language models to generate solutions. This ensures both the difficulty of math problems and the diversity of solution styles, enabling robust evaluation.\n- • **Scale and accuracy.** PROCESSBENCH consists of 3,400 test cases, with all solutions annotated with error locations by multiple human experts. The large scale and expert annotation ensure the data quality and the reliability of evaluation.\n- • **Simplicity.** PROCESSBENCH requires models to identify the earliest erroneous step occurring in the solution, if any exists. This straightforward evaluation protocol enables easy adaptation for various types of models, such as process reward models (PRMs) and critic models.\n\nWe conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models* (PRMs) and *critic models*. For PRMs, we include multiple open-source PRMs (Wang et al., 2024; Skywork, 2024; Xiong et al., 2024b) to assess the correctness of each reasoning step in the solution. For critic models, we prompt general language models like Qwen (Yang et al., 2024a; Qwen, 2024a; Hui et al., 2024) and GPT-4o (Hurst et al., 2024) to critique each solution step by step. We show that, despiterecent growing interest, existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset, which raises questions about the generalization abilities and scalability of the current data synthesis methodologies used to build PRMs. In contrast, general language models manifest non-trivial critique capabilities that can not only identify erroneous steps but also provide detailed explanations. The best open-source model, QwQ-32B-Preview (Qwen, 2024b), has performed competitively with the proprietary GPT-4o model, while it still lags behind the reasoning-specialized o1-mini (OpenAI, 2024). We hope PROCESSBENCH can catalyze future research in automated reasoning process assessment, establishing crucial foundations for scalable oversight of language models.\n\n## 2 Related Work\n\nThere exist several benchmarks or datasets related to assessing language models’ reasoning process. CriticBench (Lin et al., 2024) evaluates language models’ abilities to critique solutions and correct mistakes in various reasoning tasks. MathCheck (Zhou et al., 2024) synthesizes solutions containing erroneous steps using the GSM8K dataset (Cobbe et al., 2021), in which language models are tasked with judging the correctness of final answers or reasoning steps. PRM800K (Lightman et al., 2023) builds on the MATH problems (Hendrycks et al., 2021) and annotates the correctness and soundness of reasoning steps in model-generated solutions. It also has sparked a blooming of research interest in building process reward models (PRMs) (Wang et al., 2024; Xiong et al., 2024b;a).\n\nTable 1: Comparison between PROCESSBENCH and other benchmarks or datasets related to reasoning process assessment (Lin et al., 2024; Zhou et al., 2024; Lightman et al., 2023). &lt;sup>†&lt;/sup>: Solution diversity denotes the diversity of language models used for solution generation, corresponding to the “# Solution Generators” column. &lt;sup>‡&lt;/sup>: For PRM800K, we only count the 90 complete solutions in its phase 1 test set, as the complete solutions in its phase 2 test set are all terminated at the earliest erroneous steps.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>Problem Difficulty&lt;/th>\n&lt;th># Solution Generators&lt;/th>\n&lt;th>Solution Diversity&lt;sup>†&lt;/sup>&lt;/th>\n&lt;th>Step Annotation?&lt;/th>\n&lt;th>Annotator&lt;/th>\n&lt;th>Test Case Size (Identifying Process Errors)&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathCheck-GSM&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>516&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PRM800K&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>90&lt;sup>‡&lt;/sup>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PROCESSBENCH&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>3,400&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nPROCESSBENCH is distinguished from prior benchmarks or datasets in three key aspects, as highlighted in Table 1. **First**, PROCESSBENCH primarily covers more challenging math problems with competition- or Olympiad-level difficulty, which better fit the rapidly growing capabilities of modern language models. **Second**, rather than relying on synthetic data, PROCESSBENCH leverages diverse model-generated natural solutions and employs expert annotation to label erroneous steps, which ensures both real-world applicability and label accuracy. **Third**, the large scale of PROCESSBENCH (3,400 test cases in total) enables more comprehensive and robust evaluation.\n\nThere has also been extensive research on language models’ scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024) and studies on whether language models can identify the errors in their own outputs. Lightman et al. (2023); Wang et al. (2024); Luo et al. (2024) propose to train specialized reward models to supervise language models’ reasoning process (i.e., process reward models or PRMs). Huang et al. (2023); Kamoi et al. (2024) argue that general language models struggle to identify and correct their reasoning errors without external feedback. Saunders et al. (2022); McAleese et al. (2024) show that language models can be trained to write informative critiques for both assisting human evaluation and enabling self-refinement, which favorably scales with increased model capabilities (or model sizes). We believe the improved capabilities of error identification will build strong foundations for language models’ scalable oversight.\n\n## 3 Benchmark Construction\n\n### 3.1 Task Definition\n\nAs shown in Figure 2, given a math problem and a step-by-step solution, PROCESSBENCH requires models to either identify the *earliest-occurring error*, or conclude that all steps are *correct*. Formally,---\n\ngiven a math problem  $P$  and its step-by-step solution  $S = \\{s_0, \\dots, s_{n-1}\\}$ , the task is to output an index  $i \\in \\{-1, 0, \\dots, n-1\\}$ , where  $i = -1$  indicates that all steps are correct, and  $i \\geq 0$  indicates that the earliest error occurs at step  $s_i$ .\n\nTypically but non-inclusively, we consider a step as erroneous if it contains any of the following: (1) **Mathematical errors**: incorrect calculations, algebraic manipulations, or formula applications. (2) **Logical errors**: invalid deductions, unwarranted assumptions, or flawed reasoning steps. (3) **Conceptual errors**: misunderstanding or misapplication of mathematical or problem concepts. (4) **Completeness errors**: missing crucial conditions, constraints, or necessary justifications that affect the solution’s validity. Beyond these types of errors, we encourage human annotators to determine the correctness of reasoning steps based on their own expertise. We do not require human annotators to explicitly annotate error types due to the intractability of intentional categorization.\n\nNote that for steps after the first error, the meaning of their correctness may become ambiguous or debatable: derivations based on incorrect premises can make sense, but still remain on a globally incorrect reasoning path (Lightman et al., 2023). For instance, if step  $k$  contains an error in calculating  $x = 2$ , when it should be  $x = 3$ , subsequent steps may follow valid algebraic rules but operate on an incorrect value of  $x$ , making their individual correctness hard to determine. This is why PROCESSBENCH focuses on identifying the earliest-occurring error in the reasoning process.\n\n### 3.2 Data Collection\n\n**Problem Curation** We collect math problems from the test sets of four public and widely used datasets in mathematical reasoning tasks: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), Olympiad-Bench (He et al., 2024), and Omni-MATH (Gao et al., 2024). Except for GSM8K, which consists of grade school math problems, the other three datasets all contain problems with competition- or Olympiad-level difficulty.\n\n**Solution Generation** We generate solutions using the widely used Qwen (Yang et al., 2024a; Qwen, 2024a; Yang et al., 2024b) and LLaMA (Dubey et al., 2024) series open-source models, resulting in twelve distinct solution generators in total. This includes a wide range of model families, sizes, and downstream task performance, leading to the high diversity of solution styles. Table 4 in Appendix B presents the breakdown of language models used for PROCESSBENCH’s solution generation.\n\n**Solution Reformattng** In mathematical reasoning tasks, double line breaks (i.e., “\\n\\n”) are commonly used to segment solution steps (or paragraphs). However, we observed inconsistent step granularity due to varying solution styles and generation randomness. Some generated solutions frequently used double line breaks, resulting in numerous short, logically incomplete steps, while others used them sparingly, leading to lengthy paragraphs that combine multiple logical components. Such inconsistency in step granularity (and potential improper step segmentation) would impede the standardization of human annotation criteria.\n\nTo address this issue, we adopt a *solution reformattng* method to standardize the step granularity, through which the segmented paragraphs can better correspond to logically complete and progressive reasoning steps. Specifically, we first replace all the line breaks with white space, and then ask Qwen2.5-72B-Instruct to insert double line breaks (i.e., segment paragraphs) while preserving the solution content. Since we found that Qwen2.5-72B-Instruct sometimes alters the solution content ( $< 0.5\\%$ ), we remove those solutions whose final answers change after reformattng (although the content alteration may not influence benchmark construction). Consequently, the reformattng method effectively unifies the step granularity. Figure 6 in Appendix A presents an example of solution reformattng.\n\n**Expert Annotation** To ensure a balance between erroneous and correct solutions, we first use Qwen2.5-72B-Instruct to verify the correctness of final answers in the model-generated solutions against the reference answers. We then respectively sample solutions with correct or incorrect final answers for subsequent annotation in a balanced way to avoid excessive concentration on solutions from either the weakest or strongest models.\n\nWe recruit human experts with doctoral-level mathematical expertise for annotation, and all of them are required to pass the mandatory proficiency examination and annotation tutorial. The annotators are designated with the same task in § 3.1, i.e., identifying the earliest-occurring error in each solution. However, we notice that the competition- or Olympiad-level math problems can still be challenging even for doctoral students majoring in mathematics. According to the feedback from the annotators, although they were not required to solve problems from scratch but rather to identify erroneous steps in presented solutions, they would still become quite hesitant in their annotations when uncertain about the correct solution approach, which affected both the annotation speed and quality. To ease the annotation difficulty,we provide annotators with the reference solutions and answers from the original datasets, while we still explicitly instructed them to inspect and verify the presented model-generated solutions step by step.\n\nEach solution is initially assigned to three different experts. When the initial three annotators cannot reach consensus, we increase the number of annotators until three of them agree on the same result. If an agreement cannot be achieved within five annotators (e.g., annotation distribution of (2, 2, 1) or (2, 1, 1, 1)), we discard this solution. This leads to an overall  $\\sim 30\\%$  discard rate throughout the entire annotation process. We also discard the solutions where the final answers are incorrect (according to the reference answers) but the human annotation results are correct. Although such cases are fairly rare ( $< 1\\%$ ), they are mostly concentrated in the OlympiadBench and Omni-MATH problems (i.e., Olympiad-level ones). The agreement statistics in Table 2 further evidence that the more challenging problems usually need more annotators to achieve the annotation agreement, particularly for those samples with incorrect final answers. These results suggest the inherent challenge of our human annotation task.\n\n### 3.3 Statistics\n\nTable 2: Statistics of PROCESSBENCH. “% Process errors” denotes the proportion of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. “%  $\\geq n$  steps” denotes the proportion of samples whose solutions have  $\\geq n$  steps (split by double line breaks). “% 3/ $n$  agreement” denotes the proportion of samples where the three-annotator agreement is achieved within  $n$  annotators, so  $(\\% 3/3) + (\\% 3/4) + (\\% 3/5) = 100\\%$ .\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td># Samples&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% Process errors&lt;br/>(correct final answers)&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{200-193}{200} = 3.5\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-406}{500} = 18.8\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-339}{500} = 32.2\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-241}{500} = 51.8\\%&lt;/math>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td># Steps&lt;/td>\n&lt;td>5.3&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>6.8&lt;/td>\n&lt;td>6.0&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>8.6&lt;/td>\n&lt;td>7.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 5&lt;/math> steps&lt;/td>\n&lt;td>61.8%&lt;/td>\n&lt;td>57.5%&lt;/td>\n&lt;td>73.6%&lt;/td>\n&lt;td>70.4%&lt;/td>\n&lt;td>92.6%&lt;/td>\n&lt;td>92.3%&lt;/td>\n&lt;td>92.5%&lt;/td>\n&lt;td>81.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 10&lt;/math> steps&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>1.6%&lt;/td>\n&lt;td>17.8%&lt;/td>\n&lt;td>8.9%&lt;/td>\n&lt;td>33.9%&lt;/td>\n&lt;td>27.1%&lt;/td>\n&lt;td>29.2%&lt;/td>\n&lt;td>21.6%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 15&lt;/math> steps&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>0.0%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>2.0%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>8.8%&lt;/td>\n&lt;td>7.5%&lt;/td>\n&lt;td>4.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/3 agreement&lt;/td>\n&lt;td>66.7%&lt;/td>\n&lt;td>95.9%&lt;/td>\n&lt;td>59.4%&lt;/td>\n&lt;td>91.9%&lt;/td>\n&lt;td>52.8%&lt;/td>\n&lt;td>85.0%&lt;/td>\n&lt;td>47.8%&lt;/td>\n&lt;td>80.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/4 agreement&lt;/td>\n&lt;td>21.3%&lt;/td>\n&lt;td>3.6%&lt;/td>\n&lt;td>24.4%&lt;/td>\n&lt;td>4.7%&lt;/td>\n&lt;td>24.1%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>25.6%&lt;/td>\n&lt;td>13.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/5 agreement&lt;/td>\n&lt;td>12.1%&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>16.2%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>23.1%&lt;/td>\n&lt;td>5.9%&lt;/td>\n&lt;td>26.6%&lt;/td>\n&lt;td>6.2%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe resulting PROCESSBENCH has four subsets, consisting of 3,400 test cases in total. The detailed statistics are shown in Table 2 and Table 4 (in Appendix B), and we also plot in Figure 3 the distribution of error positions in erroneous samples. In general, the more challenging the problems, the more solution steps the models generate, and incorrect solutions usually contain more steps than correct ones. However, across all four subsets, a large proportion of errors occur in the earlier steps, such as steps 0-3 in GSM8K and MATH, and steps 1-5 in OlympiadBench and Omni-MATH.\n\nFigure 3: Distribution of error positions (indexed from 0; truncated to 16 for better visualization), corresponding to the *label* field as shown in Figure 2.\n\nIt is noteworthy that while we have intentionally controlled an equal number of solutions with incorrect and correct final answers (200 each for GSM8K and 500 each for other subsets), the annotationFigure 4: Process error ratios per models and subsets, computed as the proportions of samples annotated as *erroneous* among all the samples with *correct final answers* (same as in Table 2). The models used for solution generation slightly vary across different subsets, see Table 4 in Appendix B. We observe that no particular models have notably higher process error rates, while **the process error rates are consistently higher on more difficult problems for all the models.**\n\nresults reveal quite different numbers. Specifically, in the more challenging subsets like OlympiadBench and Omni-MATH, a larger proportion of solutions with correct final answers still contain erroneous steps. For instance, in OlympiadBench,  $\\frac{500-339}{500} = 32.2\\%$  of solutions with correct final answers are found to contain process errors, while in Omni-MATH this proportion is even higher ( $\\frac{500-241}{500} = 51.8\\%$ ). In contrast, these proportions in GSM8K and MATH are  $\\frac{200-193}{200} = 3.5\\%$  and  $\\frac{500-406}{500} = 18.8\\%$ , respectively. In Figure 4, for each model used for solution generation, we plot the ratio of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. We observe that the process error rates are consistently higher on more difficult problems. To our knowledge, our work is **the first to present evidence that on more challenging math problems, current language models are more prone to making process errors even when reaching correct final answers.** This also suggests the underlying limitation of rule-based RL in mathematical reasoning (i.e., rewarding merely according to the correctness of final answers) and further highlights the significance of identifying errors in the reasoning process.\n\n## 4 Evaluation\n\n### 4.1 Setup\n\nFor each subset of PROCESSBENCH, we calculate the accuracies on erroneous and correct samples, respectively, and additionally compute their harmonic mean as the **F1 score**. We primarily refer to F1 scores to compare model performance, as it balances model behaviors between being overly critical and being incapable of identifying errors.\n\nWe consider two types of models in the evaluation on PROCESSBENCH: *process reward models (PRMs)* and *critic models*.\n\n**Process Reward Models (PRMs)** As a recently focal topic, PRMs are proposed to assess and supervise the intermediate steps in language models’ reasoning process (Lightman et al., 2023), thus naturally falling in the scope of our research. In practice, PRMs are typically trained using the process labels for intermediate reasoning steps, outputting either the correctness prediction or a scalar score for each reasoning step during inference. Previous research usually evaluates PRMs based on their improvement in the Best-of-N (BoN) performance of another language model that generates solutions. However, this lacks a finer-grained inspection on their process assessment abilities, and the evaluation reliability can be heavily affected by the underlying solution generation model.\n\nOur evaluation includes several open-source PRMs: (1) Math-Shepherd (Wang et al., 2024), which obtains the process label for each step via estimating the empirical probability of this step leading to the correct final answer. (2) Two LLaMA-3.1-based PRMs from Xiong et al. (2024b), which roughly follow the training methodology of Math-Shepherd but differ in the solution generation models and optimization objectives. (3) Two Qwen2.5-Math-based PRMs recently released by Skywork (2024). (4) We also train a PRM by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K dataset, namely Qwen2.5-Math-7B-PRM800K. See Appendix C for its training details.For the (1)(2)(4) PRMs, we extract the earliest erroneous step from their correctness predictions for reasoning steps. For the (3) PRMs, which produce scalar scores for each reasoning step, we first transform these scores into binary correctness predictions (using a threshold above which steps are considered as correct), and then extract the earliest erroneous step as we do for (1)(2)(4). The transformation threshold is determined as the one giving the highest F1 score on the GSM8K subset.\n\n**Critic Models** Critic models aim to provide feedback and critique to model-generated texts, non-inclusively including verification, reflection, and correction or refinement. They have demonstrated promising utility in achieving scalable oversight (Saunders et al., 2022; McAleese et al., 2024).\n\nTraining critic models for specific domains typically requires significant and specialized effort, which is out of the scope of our work. Instead, we are more interested in the critique capabilities of *general language models*. The task definition (§ 3.1) of PROCESSBENCH enables us to apply simple prompt engineering to repurpose general language models as critic models. We show in Figure 7 in Appendix E the prompt template we implement for our evaluation. Specifically, models are prompted to return the index of the paragraph where the earliest error occurs as the *final answer*, similar to the conventional evaluation protocol for mathematical reasoning tasks (Cobbe et al., 2021; Hendrycks et al., 2021; Yang et al., 2024b).\n\nOur evaluation includes the widely-used Qwen2 (Yang et al., 2024a), Qwen2.5 (Qwen, 2024a), Qwen2.5-Math (Yang et al., 2024b), Qwen2.5-Coder (Hui et al., 2024), and LLaMA-3 (Dubey et al., 2024) series open-source models, as well as the recently released QwQ-32B-Preview reasoning model (Qwen, 2024b). We also evaluate the proprietary GPT-4o (Hurst et al., 2024) and o1-mini (OpenAI, 2024) models. We report the performance of open-source models under majority voting over eight samplings, while we also report their performance under greedy decoding in Table 9 in Appendix F. For the proprietary model GPT-4o, we report the results under greedy decoding, while for o1-mini, we report the results under single sampling as its API does not support customized decoding parameters.\n\nTable 3: Evaluation results on PROCESSBENCH. We report the F1 score of the respective accuracies on erroneous and correct samples. See Table 5 and Table 7 for breakdown of evaluation results.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad-Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>68.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>56.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>★ QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>71.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>",
      "numLines": 500,
      "startLine": 0,
      "totalLines": 1799
    }
  },
  "sourceToolAssistantUUID": "b3611dec-8fc8-4e7a-a627-bc7ef94d693f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "ec742eed-bc4a-42bb-b532-049aa9a7715d",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research methodology",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Tool call

_source line 44 · 2026-05-28T05:09:17.884Z_

<details open><summary>🔧 Tool call — Read · `toolu_011ZwtQNR5432qnW92XUSsyz`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec742eed-bc4a-42bb-b532-049aa9a7715d",
  "isSidechain": false,
  "requestId": "req_011CbUPYGHXmDoUNuzWk7tMV",
  "type": "assistant",
  "uuid": "2b23aad9-12e1-49a7-b921-aaa6104c9608",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KR4BNDHUsw6GxkYz81XKCg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11171,
      "cache_read_input_tokens": 18162,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 18162,
          "cache_creation_input_tokens": 11171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11171
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

_source line 45 · 2026-05-28T05:09:17.891Z_

<details><summary>↩ Tool result · `toolu_011ZwtQNR5432qnW92XUSsyz`</summary>

```text
500	&lt;/tr>
501	&lt;tr>
502	&lt;td>o1-mini&lt;/td>
503	&lt;td>93.2&lt;/td>
504	&lt;td>88.9&lt;/td>
505	&lt;td>87.2&lt;/td>
506	&lt;td>82.4&lt;/td>
507	&lt;td>87.9&lt;/td>
508	&lt;/tr>
509	&lt;/tbody>
510	&lt;/table>Alright, I've got this math problem to solve and a solution provided, but I need to review it paragraph by paragraph to find any errors. The problem is to find the integer  $n$ , where  $0 \leq n \leq 180$ , such that  $\cos n^\circ = \cos 568^\circ$ . Let's dive into the solution step by step.
511	
512	**Paragraph 0:\*\***
513	
514	The solution starts by recalling that the cosine function has a period of  $360^\circ$ , which means  $\cos \theta = \cos (\theta + 360k)$  for any integer  $k$ . That's correct. Cosine repeats every  $360^\circ$ , so adding or subtracting multiples of  $360^\circ$  doesn't change the value of the cosine.
515	
516	**Paragraph 1:\*\***
517	
518	Given  $\cos 568^\circ$ , the solution reduces this angle by subtracting  $360^\circ$  to get  $208^\circ$ , since  $568^\circ - 360^\circ = 208^\circ$ . So,  $\cos 568^\circ = \cos 208^\circ$ . That seems right.  $208^\circ$  is within one cycle of  $0^\circ$  to  $360^\circ$ .
519	
520	**Paragraph 2:\*\***
521	
522	Now, the solution mentions that cosine is symmetric about  $180^\circ$ , and states that  $\cos \theta = \cos (180^\circ - \theta)$ . Wait a minute, is that correct? Let me think about this. Actually, cosine is symmetric about the y-axis, and the identity  $\cos \theta = \cos (-\theta)$  reflects that. The identity  $\cos \theta = \cos (360^\circ - \theta)$  shows the symmetry about  $360^\circ$ , but symmetry about  $180^\circ$  isn't directly related to cosine's even property.
523	
524	Hmm, maybe I need to recall some trigonometric identities here. Let's see, the cosine of an angle in standard position is equal to the cosine of its reference angle, but with a sign depending on the quadrant.  $208^\circ$  is in the third quadrant, where cosine is negative.
525	
526	Alternatively, there's the identity  $\cos (180^\circ + \theta) = -\cos \theta$ , but that's not directly applicable here.
527	
528	Let me double-check the symmetry properties. Cosine is an even function, meaning  $\cos (-\theta) = \cos \theta$ , which shows symmetry about the y-axis. The identity  $\cos (360^\circ - \theta) = \cos \theta$  shows symmetry every full cycle.
529	
530	But the statement  $\cos \theta = \cos (180^\circ - \theta)$  isn't generally true. Let's test it with a specific angle. For example,  $\theta = 30^\circ$ :  $\cos 30^\circ = \sqrt{3}/2$ , and  $\cos (180^\circ - 30^\circ) = \cos 150^\circ = -\sqrt{3}/2$ . These are not equal; in fact, they're negatives of each other.
531	
532	So, it seems there's an error in this paragraph. The correct identity involving  $180^\circ$  is  $\cos (180^\circ - \theta) = -\cos \theta$ , not  $\cos \theta$ .
533	
534	Therefore, the earliest error occurs in paragraph 2.
535	
536	**Final Answer:**
537	
538	$\boxed{2}$
539	
540	Figure 5: Critique generated by QwQ-32B-Preview for the test case in Figure 2.
541	
542	## 4.2 Results
543	
544	We present the evaluation results in Table 3. Our observations are summarized as follows:
545	
546	**Generalization Across Difficulty** From GSM8K and MATH to OlympiadBench and Omni-MATH, with the increased difficulty of math problems, we observe a consistent performance decline for all the models, which suggests the common challenge of both PRMs and critic models in generalization abilities.
547	
548	**Comparison Between PRMs and Critic Models** We find that existing PRMs typically underperform the top prompt-driven critic models even on the simpler GSM8K and MATH subsets, suggesting that these PRMs struggle to indicate the correctness of the intermediate steps in mathematical reasoning. Moreover, when moving toward the more challenging OlympiadBench and Omni-MATH subsets, PRMs suffer from a more notable performance decline than critic models. This raises our concerns about the **generalization abilities and scalability of the current data synthesis methodologies used to build PRMs**. More specifically, current methodologies, as exemplified by Math-Shepherd (Wang et al., 2024), measure the correctness of an intermediate step by estimating the empirical probability of this step leading to the correct final answer. This kind of approach has two intuitive major issues: (1) The process labels heavily depend on the language model used to generate solutions (i.e., highly “on-policy”), which---
549	
550	would naturally fail to indicate the correctness of reasoning steps generated by other models. (2) As demonstrated in § 3.3, current language models are prone to making process errors even when reaching correct final answers. This could substantially invalidate the estimated process labels, particularly on the more challenging math problems. In contrast, **Qwen2.5-Math-7B-PRM800K**, which is straightforwardly fine-tuned on the *fully human-annotated* PRM800K training set, exhibits significantly stronger performance and generalization ability than other PRMs.
551	
552	**Comparison Among Critic Models** Compared to PRMs, critic models can benefit from separate reasoning processes when critiquing solutions, as they can “think” more before indicating the correctness of each solution step, which leads to their better performance in this error identification task. Within the same model family, the error identification performance favorably scales with increased model sizes. Notably, the recently released reasoning model **QwQ-32B-Preview** **performs best among the open-source models and is highly competitive with GPT-4o**. It is noteworthy that QwQ-32B-Preview achieves more *balanced accuracies on erroneous and correct samples* (see Table 5 and 7 in Appendix F). We show in Figure 5 an example of critique generated by QwQ-32B-Preview to the test case in Figure 2, which not only identifies the erroneous step but also provides the detailed thinking process and explanation. Nevertheless, QwQ-32B-Preview still lags behind o1-mini, suggesting that although the gap in problem-solving performance is getting closer between open-source and proprietary models, there still exists another large gap in their critique capabilities.
553	
554	## 5 Conclusion
555	
556	We introduce the PROCESSBENCH benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, characterized by its high problem difficulty and solution diversity, large scale, rigorous human annotation, and simple evaluation protocol. Through extensive evaluation with existing process reward models (PRMs) and prompt-driven critic models, we draw two main observations: (1) Existing PRMs typically underperform critic models in identifying erroneous reasoning steps, and struggle more to generalize to challenging math problems. (2) Open-source language models, as exemplified by QwQ-32B-Preview, have demonstrated critique capabilities competitive with the proprietary model GPT-4o, yet still lag behind the reasoning-specialized o1-mini model. We envision PROCESSBENCH as a cornerstone testbed for advancing automated reasoning process assessment, a critical step toward achieving scalable oversight of language models.
557	
558	**Limitations** Despite our best efforts throughout the entire benchmark construction process (§ 3.2), PROCESSBENCH may still contain inaccurate labels of error locations, particularly for the more challenging Olympiad-level math problems. Additionally, the solutions discarded in human annotation (§ 3.2) may involve the particularly challenging problems, which could bias the problem distribution in PROCESSBENCH, although such samples may have exceeded the capabilities of the human annotators in our annotation task.
559	
560	## References
561	
562	Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. *arXiv preprint arXiv:1606.06565*, 2016.
563	
564	Samuel R Bowman, Jeeyoon Hyun, Ethan Perez, Edwin Chen, Craig Pettit, Scott Heiner, Kamilę Lukošūtė, Amanda Askell, Andy Jones, Anna Chen, et al. Measuring progress on scalable oversight for large language models. *arXiv preprint arXiv:2211.03540*, 2022.
565	
566	Boxi Cao, Keming Lu, Xinyu Lu, Jiawei Chen, Mengjie Ren, Hao Xiang, Peilin Liu, Yaojie Lu, Ben He, Xianpei Han, et al. Towards scalable automated alignment of llms: A survey. *arXiv preprint arXiv:2406.01252*, 2024.
567	
568	Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.
569	
570	Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.
571	
572	Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. *arXiv preprint arXiv:2410.07985*, 2024.---
573	
574	Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.
575	
576	Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.
577	
578	Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. *arXiv preprint arXiv:2310.01798*, 2023.
579	
580	Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, et al. Qwen2.5-coder technical report. *arXiv preprint arXiv:2409.12186*, 2024.
581	
582	Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.
583	
584	Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. When can LLMs actually correct their own mistakes? a critical survey of self-correction of LLMs. *Transactions of the Association for Computational Linguistics*, 12:1417–1440, 2024. doi: 10.1162/tacl.a\_00713. URL &lt;https://aclanthology.org/2024.tacl-1.78>.
585	
586	Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the 29th Symposium on Operating Systems Principles*, pages 611–626, 2023.
587	
588	Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. *arXiv preprint arXiv:2305.20050*, 2023.
589	
590	Zicheng Lin, Zhibin Gou, Tian Liang, Ruilin Luo, Haowei Liu, and Yujiu Yang. Criticbench: Benchmarking llms for critique-correct reasoning. *arXiv preprint arXiv:2402.14809*, 2024.
591	
592	Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.
593	
594	Nat McAleese, Rai Michael Pokorny, Juan Felipe Ceron Uribe, Evgenia Nitishinskaya, Maja Trebacz, and Jan Leike. Llm critics help catch llm bugs. *arXiv preprint arXiv:2407.00215*, 2024.
595	
596	OpenAI. Openai o1-mini: Advancing cost-efficient reasoning, 2024. URL &lt;https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/>.
597	
598	Team Qwen. Qwen2.5: A party of foundation models, September 2024a. URL &lt;https://qwenlm.github.io/blog/qwen2.5/>.
599	
600	Team Qwen. Qwq: Reflect deeply on the boundaries of the unknown, November 2024b. URL &lt;https://qwenlm.github.io/blog/qwq-32b-preview/>.
601	
602	William Saunders, Catherine Yeh, Jeff Wu, Steven Bills, Long Ouyang, Jonathan Ward, and Jan Leike. Self-critiquing models for assisting human evaluators. *arXiv preprint arXiv:2206.05802*, 2022.
603	
604	o1 Team Skywork. Skywork-o1 open series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.
605	
606	Alan Wake, Albert Wang, Bei Chen, CX Lv, Chao Li, Chengen Huang, Chenglin Cai, Chujie Zheng, Daniel Cooper, Ethan Dai, et al. Yi-lightning technical report. *arXiv preprint arXiv:2412.01253*, 2024.
607	
608	Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, August 2024. doi: 10.18653/v1/2024.acl-long.510. URL &lt;https://aclanthology.org/2024.acl-long.510>.
609	
610	Wei Xiong, Chengshuai Shi, Jiaming Shen, Aviv Rosenberg, Zhen Qin, Daniele Calandriello, Misha Khalman, Rishabh Joshi, Bilal Piot, Mohammad Saleh, et al. Building math agents with multi-turn iterative preference learning. *arXiv preprint arXiv:2409.02392*, 2024a.---
611	
612	Wei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An implementation of generative prm. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024b.
613	
614	An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. *arXiv preprint arXiv:2407.10671*, 2024a.
615	
616	An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement. *arXiv preprint arXiv:2409.12122*, 2024b.
617	
618	Zihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F Wong, Xiaowei Huang, Qifeng Wang, and Kaizhu Huang. Is your model really a good math reasoner? evaluating mathematical reasoning with checklist. *arXiv preprint arXiv:2407.08733*, 2024.## A Example of Solution Reformattting
619	
620	&lt;table border="1">
621	&lt;tr>
622	&lt;td style="vertical-align: top; padding: 10px;">
623	&lt;p>The given equation is of an ellipse in the standard form&lt;/p>
624	&lt;math display="block">\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1,&lt;/math>
625	&lt;p>where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length.&lt;/p>
626	&lt;p>In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>
627	&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\sqrt{a^2 - b^2}&lt;/math>.&lt;/p>
628	&lt;p>First, we calculate the distance from the center to each focus:&lt;/p>
629	&lt;math display="block">\sqrt{a^2 - b^2} = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4.&lt;/math>
630	&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse.&lt;/p>
631	&lt;p>Therefore, the two foci are at &lt;math>(6 \pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>
632	&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>.&lt;/p>
633	&lt;p>The answer is: &lt;math>\boxed{(10, 3)}&lt;/math>.&lt;/p>
634	&lt;/td>
635	&lt;td style="vertical-align: middle; text-align: center; padding: 0 10px;">
636	&lt;/td>
637	&lt;td style="vertical-align: top; padding: 10px;">
638	&lt;p>The given equation is of an ellipse in the standard form &lt;math>\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1&lt;/math>, where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length. In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>
639	&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\sqrt{a^2 - b^2}&lt;/math>. First, we calculate the distance from the center to each focus: &lt;math>\sqrt{a^2 - b^2} = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4&lt;/math>.&lt;/p>
640	&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse. Therefore, the two foci are at &lt;math>(6 \pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>
641	&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>. The answer is: &lt;math>\boxed{(10, 3)}&lt;/math>.&lt;/p>
642	&lt;/td>
643	&lt;/tr>
644	&lt;/table>
645	
646	Figure 6: Example of solution reformattting. The left is the original solution (generated by Qwen2-7B-Instruct) and the right is the reformatted one. The problem, coming from the MATH test set, is “The ellipse  $\frac{(x-6)^2}{25} + \frac{(y-3)^2}{9} = 1$  has two foci. Find the one with the larger  $x$ -coordinate. Enter your answer as an ordered pair, like  $(2, 1)$ .”
647	
648	## B Breakdown Statistics of PROCESSBENCH
649	
650	Table 4: Breakdown statistics of PROCESSBENCH.  $^\dagger$ : We encountered a code bug when using Llama-3.1-70B-Instruct and Qwen2.5-72B-Instruct to generate solutions for the MATH problems, thus their counts are all zero in the MATH subset of PROCESSBENCH.  $^\ddagger$ : For the more challenging OlympiadBench and Omni-MATH problems, we exclude models with lower accuracies from subsequent annotation.
651	
652	&lt;table border="1">
653	&lt;thead>
654	&lt;tr>
655	&lt;th rowspan="2">Generator&lt;/th>
656	&lt;th colspan="2">GSM8K&lt;/th>
657	&lt;th colspan="2">MATH&lt;math>^\dagger&lt;/math>&lt;/th>
658	&lt;th colspan="2">OlympiadBench&lt;math>^\ddagger&lt;/math>&lt;/th>
659	&lt;th colspan="2">Omni-MATH&lt;math>^\ddagger&lt;/math>&lt;/th>
660	&lt;/tr>
661	&lt;tr>
662	&lt;th>error&lt;/th>
663	&lt;th>correct&lt;/th>
664	&lt;th>error&lt;/th>
665	&lt;th>correct&lt;/th>
666	&lt;th>error&lt;/th>
667	&lt;th>correct&lt;/th>
668	&lt;th>error&lt;/th>
669	&lt;th>correct&lt;/th>
670	&lt;/tr>
671	&lt;/thead>
672	&lt;tbody>
673	&lt;tr>
674	&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>
675	&lt;td>11&lt;/td>
676	&lt;td>13&lt;/td>
677	&lt;td>56&lt;/td>
678	&lt;td>14&lt;/td>
679	&lt;td>0&lt;/td>
680	&lt;td>0&lt;/td>
681	&lt;td>0&lt;/td>
682	&lt;td>0&lt;/td>
683	&lt;/tr>
684	&lt;tr>
685	&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>
686	&lt;td>16&lt;/td>
687	&lt;td>15&lt;/td>
688	&lt;td>92&lt;/td>
689	&lt;td>49&lt;/td>
690	&lt;td>0&lt;/td>
691	&lt;td>0&lt;/td>
692	&lt;td>0&lt;/td>
693	&lt;td>0&lt;/td>
694	&lt;/tr>
695	&lt;tr>
696	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
697	&lt;td>38&lt;/td>
698	&lt;td>23&lt;/td>
699	&lt;td>86&lt;/td>
700	&lt;td>53&lt;/td>
701	&lt;td>116&lt;/td>
702	&lt;td>48&lt;/td>
703	&lt;td>131&lt;/td>
704	&lt;td>31&lt;/td>
705	&lt;/tr>
706	&lt;tr>
707	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
708	&lt;td>7&lt;/td>
709	&lt;td>28&lt;/td>
710	&lt;td>0&lt;/td>
711	&lt;td>0&lt;/td>
712	&lt;td>85&lt;/td>
713	&lt;td>32&lt;/td>
714	&lt;td>103&lt;/td>
715	&lt;td>19&lt;/td>
716	&lt;/tr>
717	&lt;tr>
718	&lt;td>Qwen2-1.5B-Instruct&lt;/td>
719	&lt;td>37&lt;/td>
720	&lt;td>4&lt;/td>
721	&lt;td>36&lt;/td>
722	&lt;td>11&lt;/td>
723	&lt;td>0&lt;/td>
724	&lt;td>0&lt;/td>
725	&lt;td>0&lt;/td>
726	&lt;td>0&lt;/td>
727	&lt;/tr>
728	&lt;tr>
729	&lt;td>Qwen2-7B-Instruct&lt;/td>
730	&lt;td>31&lt;/td>
731	&lt;td>21&lt;/td>
732	&lt;td>89&lt;/td>
733	&lt;td>42&lt;/td>
734	&lt;td>63&lt;/td>
735	&lt;td>45&lt;/td>
736	&lt;td>96&lt;/td>
737	&lt;td>35&lt;/td>
738	&lt;/tr>
739	&lt;tr>
740	&lt;td>Qwen2-72B-Instruct&lt;/td>
741	&lt;td>9&lt;/td>
742	&lt;td>11&lt;/td>
743	&lt;td>56&lt;/td>
744	&lt;td>51&lt;/td>
745	&lt;td>64&lt;/td>
746	&lt;td>48&lt;/td>
747	&lt;td>71&lt;/td>
748	&lt;td>25&lt;/td>
749	&lt;/tr>
750	&lt;tr>
751	&lt;td>Qwen2.5-1.5B-Instruct&lt;/td>
752	&lt;td>32&lt;/td>
753	&lt;td>10&lt;/td>
754	&lt;td>31&lt;/td>
755	&lt;td>43&lt;/td>
756	&lt;td>0&lt;/td>
757	&lt;td>0&lt;/td>
758	&lt;td>0&lt;/td>
759	&lt;td>0&lt;/td>
760	&lt;/tr>
761	&lt;tr>
762	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
763	&lt;td>12&lt;/td>
764	&lt;td>15&lt;/td>
765	&lt;td>62&lt;/td>
766	&lt;td>35&lt;/td>
767	&lt;td>86&lt;/td>
768	&lt;td>37&lt;/td>
769	&lt;td>75&lt;/td>
770	&lt;td>29&lt;/td>
771	&lt;/tr>
772	&lt;tr>
773	&lt;td>Qwen2.5-72B-Instruct&lt;/td>
774	&lt;td>2&lt;/td>
775	&lt;td>21&lt;/td>
776	&lt;td>0&lt;/td>
777	&lt;td>0&lt;/td>
778	&lt;td>67&lt;/td>
779	&lt;td>38&lt;/td>
780	&lt;td>88&lt;/td>
781	&lt;td>38&lt;/td>
782	&lt;/tr>
783	&lt;tr>
784	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
785	&lt;td>8&lt;/td>
786	&lt;td>14&lt;/td>
787	&lt;td>47&lt;/td>
788	&lt;td>49&lt;/td>
789	&lt;td>99&lt;/td>
790	&lt;td>48&lt;/td>
791	&lt;td>103&lt;/td>
792	&lt;td>29&lt;/td>
793	&lt;/tr>
794	&lt;tr>
795	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
796	&lt;td>4&lt;/td>
797	&lt;td>18&lt;/td>
798	&lt;td>39&lt;/td>
799	&lt;td>59&lt;/td>
800	&lt;td>81&lt;/td>
801	&lt;td>43&lt;/td>
802	&lt;td>92&lt;/td>
803	&lt;td>35&lt;/td>
804	&lt;/tr>
805	&lt;tr>
806	&lt;td>&lt;/td>
807	&lt;td>207&lt;/td>
808	&lt;td>193&lt;/td>
809	&lt;td>594&lt;/td>
810	&lt;td>406&lt;/td>
811	&lt;td>661&lt;/td>
812	&lt;td>339&lt;/td>
813	&lt;td>759&lt;/td>
814	&lt;td>241&lt;/td>
815	&lt;/tr>
816	&lt;tr>
817	&lt;td>Total&lt;/td>
818	&lt;td colspan="2">400&lt;/td>
819	&lt;td colspan="2">1,000&lt;/td>
820	&lt;td colspan="2">1,000&lt;/td>
821	&lt;td colspan="2">1,000&lt;/td>
822	&lt;/tr>
823	&lt;/tbody>
824	&lt;/table>## C Training Details of Qwen2.5-Math-7B-PRM800K
825	
826	Qwen2.5-Math-7B-PRM800K is obtained by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K training set. We replace the original language modeling head with a new reward modeling head that outputs binary classification logits. The classification loss is computed at the second line break positions in all the “\n\n”. We treat the original 1 and 0 labels in PRM800K as our positive labels, while -1 as negative ones. To eliminate test data contamination, we also remove the PRM800K training samples that have the same problems in PROCESSBENCH. The training was run on eight A100 80GB GPUs.
827	
828	## D Inference Details
829	
830	For solution generation in § 3.2, all the models are set with  $p = 0.9, t = 0.7$ . For majority voting evaluation in § 4, we set  $p = 0.8, t = 0.7, k = 20$  for Qwen2.5-Math-7/72B-Instruct to ensure their normal generation, while all the other models are set with only  $p = 0.9$ . All the inference in the evaluation was run with vLLM (Kwon et al., 2023) on eight A100 80GB GPUs.
831	
832	## E Prompt Template for Critic Model Evaluation
833	
834	The following is a math problem and a solution (split into paragraphs, enclosed with tags and indexed from 0):
835	
836	[Math Problem]
837	
838	... (math problem) ...
839	
840	[Solution]
841	
842	&lt;paragraph\_0>
843	
844	... (paragraph 0 of solution) ...
845	
846	&lt;/paragraph\_0>
847	
848	...
849	
850	&lt;paragraph\_n-1>
851	
852	... (paragraph n-1 of solution) ...
853	
854	&lt;/paragraph\_n-1>
855	
856	Your task is to review and critique the solution paragraph by paragraph. Once you identify an error in a paragraph, return the **index of the paragraph where the earliest error occurs**. Otherwise, return the **index of -1 (which typically denotes "not found")**.
857	
858	**Please put your final answer (i.e., the index) in \boxed{}.**
859	
860	Figure 7: Prompt template for critic model evaluation. The **blue texts** indicate the input math problem and the solution (split into paragraphs). The **red texts** describe the required output content and format.## F Supplementary Evaluation Results
861	
862	Table 5: Breakdown of evaluation results on the GSM8K and MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.
863	
864	&lt;table border="1">
865	&lt;thead>
866	&lt;tr>
867	&lt;th rowspan="2">Model&lt;/th>
868	&lt;th colspan="3">GSM8K&lt;/th>
869	&lt;th colspan="3">MATH&lt;/th>
870	&lt;/tr>
871	&lt;tr>
872	&lt;th>error&lt;/th>
873	&lt;th>correct&lt;/th>
874	&lt;th>F1&lt;/th>
875	&lt;th>error&lt;/th>
876	&lt;th>correct&lt;/th>
877	&lt;th>F1&lt;/th>
878	&lt;/tr>
879	&lt;/thead>
880	&lt;tbody>
881	&lt;tr>
882	&lt;td colspan="7" style="text-align: center;">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>
883	&lt;/tr>
884	&lt;tr>
885	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
886	&lt;td>32.4&lt;/td>
887	&lt;td>91.7&lt;/td>
888	&lt;td>47.9&lt;/td>
889	&lt;td>18.0&lt;/td>
890	&lt;td>82.0&lt;/td>
891	&lt;td>29.5&lt;/td>
892	&lt;/tr>
893	&lt;tr>
894	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
895	&lt;td>33.8&lt;/td>
896	&lt;td>99.0&lt;/td>
897	&lt;td>50.4&lt;/td>
898	&lt;td>21.7&lt;/td>
899	&lt;td>72.2&lt;/td>
900	&lt;td>33.4&lt;/td>
901	&lt;/tr>
902	&lt;tr>
903	&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>
904	&lt;td>24.2&lt;/td>
905	&lt;td>98.4&lt;/td>
906	&lt;td>38.8&lt;/td>
907	&lt;td>21.4&lt;/td>
908	&lt;td>80.0&lt;/td>
909	&lt;td>33.8&lt;/td>
910	&lt;/tr>
911	&lt;tr>
912	&lt;td>Skywork-PRM-1.5B&lt;/td>
913	&lt;td>50.2&lt;/td>
914	&lt;td>71.5&lt;/td>
915	&lt;td>59.0&lt;/td>
916	&lt;td>37.9&lt;/td>
917	&lt;td>65.3&lt;/td>
918	&lt;td>48.0&lt;/td>
919	&lt;/tr>
920	&lt;tr>
921	&lt;td>Skywork-PRM-7B&lt;/td>
922	&lt;td>61.8&lt;/td>
923	&lt;td>82.9&lt;/td>
924	&lt;td>&lt;b>70.8&lt;/b>&lt;/td>
925	&lt;td>43.8&lt;/td>
926	&lt;td>69.2&lt;/td>
927	&lt;td>53.6&lt;/td>
928	&lt;/tr>
929	&lt;tr>
930	&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>
931	&lt;td>53.1&lt;/td>
932	&lt;td>95.3&lt;/td>
933	&lt;td>68.2&lt;/td>
934	&lt;td>48.0&lt;/td>
935	&lt;td>90.1&lt;/td>
936	&lt;td>&lt;b>62.6&lt;/b>&lt;/td>
937	&lt;/tr>
938	&lt;tr>
939	&lt;td colspan="7" style="text-align: center;">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>
940	&lt;/tr>
941	&lt;tr>
942	&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>
943	&lt;td>42.5&lt;/td>
944	&lt;td>7.8&lt;/td>
945	&lt;td>13.1&lt;/td>
946	&lt;td>28.6&lt;/td>
947	&lt;td>9.1&lt;/td>
948	&lt;td>13.8&lt;/td>
949	&lt;/tr>
950	&lt;tr>
951	&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>
952	&lt;td>35.7&lt;/td>
953	&lt;td>96.9&lt;/td>
954	&lt;td>52.2&lt;/td>
955	&lt;td>13.0&lt;/td>
956	&lt;td>93.3&lt;/td>
957	&lt;td>22.8&lt;/td>
958	&lt;/tr>
959	&lt;tr>
960	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
961	&lt;td>44.4&lt;/td>
962	&lt;td>6.2&lt;/td>
963	&lt;td>10.9&lt;/td>
964	&lt;td>41.9&lt;/td>
965	&lt;td>2.7&lt;/td>
966	&lt;td>5.1&lt;/td>
967	&lt;/tr>
968	&lt;tr>
969	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
970	&lt;td>64.3&lt;/td>
971	&lt;td>89.6&lt;/td>
972	&lt;td>74.9&lt;/td>
973	&lt;td>35.4&lt;/td>
974	&lt;td>75.6&lt;/td>
975	&lt;td>48.2&lt;/td>
976	&lt;/tr>
977	&lt;tr>
978	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
979	&lt;td>72.5&lt;/td>
980	&lt;td>96.9&lt;/td>
981	&lt;td>82.9&lt;/td>
982	&lt;td>43.3&lt;/td>
983	&lt;td>94.6&lt;/td>
984	&lt;td>59.4&lt;/td>
985	&lt;/tr>
986	&lt;tr>
987	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
988	&lt;td>15.5&lt;/td>
989	&lt;td>100.0&lt;/td>
990	&lt;td>26.8&lt;/td>
991	&lt;td>14.8&lt;/td>
992	&lt;td>96.8&lt;/td>
993	&lt;td>25.7&lt;/td>
994	&lt;/tr>
995	&lt;tr>
996	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
997	&lt;td>49.8&lt;/td>
998	&lt;td>96.9&lt;/td>
999	&lt;td>65.8&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b23aad9-12e1-49a7-b921-aaa6104c9608",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "7b775eca-f4d1-4c81-a628-7cc44d6255bc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt",
      "content": "&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Alright, I've got this math problem to solve and a solution provided, but I need to review it paragraph by paragraph to find any errors. The problem is to find the integer  $n$ , where  $0 \\leq n \\leq 180$ , such that  $\\cos n^\\circ = \\cos 568^\\circ$ . Let's dive into the solution step by step.\n\n**Paragraph 0:\\*\\***\n\nThe solution starts by recalling that the cosine function has a period of  $360^\\circ$ , which means  $\\cos \\theta = \\cos (\\theta + 360k)$  for any integer  $k$ . That's correct. Cosine repeats every  $360^\\circ$ , so adding or subtracting multiples of  $360^\\circ$  doesn't change the value of the cosine.\n\n**Paragraph 1:\\*\\***\n\nGiven  $\\cos 568^\\circ$ , the solution reduces this angle by subtracting  $360^\\circ$  to get  $208^\\circ$ , since  $568^\\circ - 360^\\circ = 208^\\circ$ . So,  $\\cos 568^\\circ = \\cos 208^\\circ$ . That seems right.  $208^\\circ$  is within one cycle of  $0^\\circ$  to  $360^\\circ$ .\n\n**Paragraph 2:\\*\\***\n\nNow, the solution mentions that cosine is symmetric about  $180^\\circ$ , and states that  $\\cos \\theta = \\cos (180^\\circ - \\theta)$ . Wait a minute, is that correct? Let me think about this. Actually, cosine is symmetric about the y-axis, and the identity  $\\cos \\theta = \\cos (-\\theta)$  reflects that. The identity  $\\cos \\theta = \\cos (360^\\circ - \\theta)$  shows the symmetry about  $360^\\circ$ , but symmetry about  $180^\\circ$  isn't directly related to cosine's even property.\n\nHmm, maybe I need to recall some trigonometric identities here. Let's see, the cosine of an angle in standard position is equal to the cosine of its reference angle, but with a sign depending on the quadrant.  $208^\\circ$  is in the third quadrant, where cosine is negative.\n\nAlternatively, there's the identity  $\\cos (180^\\circ + \\theta) = -\\cos \\theta$ , but that's not directly applicable here.\n\nLet me double-check the symmetry properties. Cosine is an even function, meaning  $\\cos (-\\theta) = \\cos \\theta$ , which shows symmetry about the y-axis. The identity  $\\cos (360^\\circ - \\theta) = \\cos \\theta$  shows symmetry every full cycle.\n\nBut the statement  $\\cos \\theta = \\cos (180^\\circ - \\theta)$  isn't generally true. Let's test it with a specific angle. For example,  $\\theta = 30^\\circ$ :  $\\cos 30^\\circ = \\sqrt{3}/2$ , and  $\\cos (180^\\circ - 30^\\circ) = \\cos 150^\\circ = -\\sqrt{3}/2$ . These are not equal; in fact, they're negatives of each other.\n\nSo, it seems there's an error in this paragraph. The correct identity involving  $180^\\circ$  is  $\\cos (180^\\circ - \\theta) = -\\cos \\theta$ , not  $\\cos \\theta$ .\n\nTherefore, the earliest error occurs in paragraph 2.\n\n**Final Answer:**\n\n$\\boxed{2}$\n\nFigure 5: Critique generated by QwQ-32B-Preview for the test case in Figure 2.\n\n## 4.2 Results\n\nWe present the evaluation results in Table 3. Our observations are summarized as follows:\n\n**Generalization Across Difficulty** From GSM8K and MATH to OlympiadBench and Omni-MATH, with the increased difficulty of math problems, we observe a consistent performance decline for all the models, which suggests the common challenge of both PRMs and critic models in generalization abilities.\n\n**Comparison Between PRMs and Critic Models** We find that existing PRMs typically underperform the top prompt-driven critic models even on the simpler GSM8K and MATH subsets, suggesting that these PRMs struggle to indicate the correctness of the intermediate steps in mathematical reasoning. Moreover, when moving toward the more challenging OlympiadBench and Omni-MATH subsets, PRMs suffer from a more notable performance decline than critic models. This raises our concerns about the **generalization abilities and scalability of the current data synthesis methodologies used to build PRMs**. More specifically, current methodologies, as exemplified by Math-Shepherd (Wang et al., 2024), measure the correctness of an intermediate step by estimating the empirical probability of this step leading to the correct final answer. This kind of approach has two intuitive major issues: (1) The process labels heavily depend on the language model used to generate solutions (i.e., highly “on-policy”), which---\n\nwould naturally fail to indicate the correctness of reasoning steps generated by other models. (2) As demonstrated in § 3.3, current language models are prone to making process errors even when reaching correct final answers. This could substantially invalidate the estimated process labels, particularly on the more challenging math problems. In contrast, **Qwen2.5-Math-7B-PRM800K**, which is straightforwardly fine-tuned on the *fully human-annotated* PRM800K training set, exhibits significantly stronger performance and generalization ability than other PRMs.\n\n**Comparison Among Critic Models** Compared to PRMs, critic models can benefit from separate reasoning processes when critiquing solutions, as they can “think” more before indicating the correctness of each solution step, which leads to their better performance in this error identification task. Within the same model family, the error identification performance favorably scales with increased model sizes. Notably, the recently released reasoning model **QwQ-32B-Preview** **performs best among the open-source models and is highly competitive with GPT-4o**. It is noteworthy that QwQ-32B-Preview achieves more *balanced accuracies on erroneous and correct samples* (see Table 5 and 7 in Appendix F). We show in Figure 5 an example of critique generated by QwQ-32B-Preview to the test case in Figure 2, which not only identifies the erroneous step but also provides the detailed thinking process and explanation. Nevertheless, QwQ-32B-Preview still lags behind o1-mini, suggesting that although the gap in problem-solving performance is getting closer between open-source and proprietary models, there still exists another large gap in their critique capabilities.\n\n## 5 Conclusion\n\nWe introduce the PROCESSBENCH benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, characterized by its high problem difficulty and solution diversity, large scale, rigorous human annotation, and simple evaluation protocol. Through extensive evaluation with existing process reward models (PRMs) and prompt-driven critic models, we draw two main observations: (1) Existing PRMs typically underperform critic models in identifying erroneous reasoning steps, and struggle more to generalize to challenging math problems. (2) Open-source language models, as exemplified by QwQ-32B-Preview, have demonstrated critique capabilities competitive with the proprietary model GPT-4o, yet still lag behind the reasoning-specialized o1-mini model. We envision PROCESSBENCH as a cornerstone testbed for advancing automated reasoning process assessment, a critical step toward achieving scalable oversight of language models.\n\n**Limitations** Despite our best efforts throughout the entire benchmark construction process (§ 3.2), PROCESSBENCH may still contain inaccurate labels of error locations, particularly for the more challenging Olympiad-level math problems. Additionally, the solutions discarded in human annotation (§ 3.2) may involve the particularly challenging problems, which could bias the problem distribution in PROCESSBENCH, although such samples may have exceeded the capabilities of the human annotators in our annotation task.\n\n## References\n\nDario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. *arXiv preprint arXiv:1606.06565*, 2016.\n\nSamuel R Bowman, Jeeyoon Hyun, Ethan Perez, Edwin Chen, Craig Pettit, Scott Heiner, Kamilę Lukošūtė, Amanda Askell, Andy Jones, Anna Chen, et al. Measuring progress on scalable oversight for large language models. *arXiv preprint arXiv:2211.03540*, 2022.\n\nBoxi Cao, Keming Lu, Xinyu Lu, Jiawei Chen, Mengjie Ren, Hao Xiang, Peilin Liu, Yaojie Lu, Ben He, Xianpei Han, et al. Towards scalable automated alignment of llms: A survey. *arXiv preprint arXiv:2406.01252*, 2024.\n\nKarl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n\nAbhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.\n\nBofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. *arXiv preprint arXiv:2410.07985*, 2024.---\n\nChaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n\nJie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. *arXiv preprint arXiv:2310.01798*, 2023.\n\nBinyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, et al. Qwen2.5-coder technical report. *arXiv preprint arXiv:2409.12186*, 2024.\n\nAaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.\n\nRyo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. When can LLMs actually correct their own mistakes? a critical survey of self-correction of LLMs. *Transactions of the Association for Computational Linguistics*, 12:1417–1440, 2024. doi: 10.1162/tacl.a\\_00713. URL &lt;https://aclanthology.org/2024.tacl-1.78>.\n\nWoosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the 29th Symposium on Operating Systems Principles*, pages 611–626, 2023.\n\nHunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. *arXiv preprint arXiv:2305.20050*, 2023.\n\nZicheng Lin, Zhibin Gou, Tian Liang, Ruilin Luo, Haowei Liu, and Yujiu Yang. Criticbench: Benchmarking llms for critique-correct reasoning. *arXiv preprint arXiv:2402.14809*, 2024.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nNat McAleese, Rai Michael Pokorny, Juan Felipe Ceron Uribe, Evgenia Nitishinskaya, Maja Trebacz, and Jan Leike. Llm critics help catch llm bugs. *arXiv preprint arXiv:2407.00215*, 2024.\n\nOpenAI. Openai o1-mini: Advancing cost-efficient reasoning, 2024. URL &lt;https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/>.\n\nTeam Qwen. Qwen2.5: A party of foundation models, September 2024a. URL &lt;https://qwenlm.github.io/blog/qwen2.5/>.\n\nTeam Qwen. Qwq: Reflect deeply on the boundaries of the unknown, November 2024b. URL &lt;https://qwenlm.github.io/blog/qwq-32b-preview/>.\n\nWilliam Saunders, Catherine Yeh, Jeff Wu, Steven Bills, Long Ouyang, Jonathan Ward, and Jan Leike. Self-critiquing models for assisting human evaluators. *arXiv preprint arXiv:2206.05802*, 2022.\n\no1 Team Skywork. Skywork-o1 open series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nAlan Wake, Albert Wang, Bei Chen, CX Lv, Chao Li, Chengen Huang, Chenglin Cai, Chujie Zheng, Daniel Cooper, Ethan Dai, et al. Yi-lightning technical report. *arXiv preprint arXiv:2412.01253*, 2024.\n\nPeiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, August 2024. doi: 10.18653/v1/2024.acl-long.510. URL &lt;https://aclanthology.org/2024.acl-long.510>.\n\nWei Xiong, Chengshuai Shi, Jiaming Shen, Aviv Rosenberg, Zhen Qin, Daniele Calandriello, Misha Khalman, Rishabh Joshi, Bilal Piot, Mohammad Saleh, et al. Building math agents with multi-turn iterative preference learning. *arXiv preprint arXiv:2409.02392*, 2024a.---\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An implementation of generative prm. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024b.\n\nAn Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. *arXiv preprint arXiv:2407.10671*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nZihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F Wong, Xiaowei Huang, Qifeng Wang, and Kaizhu Huang. Is your model really a good math reasoner? evaluating mathematical reasoning with checklist. *arXiv preprint arXiv:2407.08733*, 2024.## A Example of Solution Reformattting\n\n&lt;table border=\"1\">\n&lt;tr>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form&lt;/p>\n&lt;math display=\"block\">\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1,&lt;/math>\n&lt;p>where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length.&lt;/p>\n&lt;p>In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>.&lt;/p>\n&lt;p>First, we calculate the distance from the center to each focus:&lt;/p>\n&lt;math display=\"block\">\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4.&lt;/math>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse.&lt;/p>\n&lt;p>Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;td style=\"vertical-align: middle; text-align: center; padding: 0 10px;\">\n&lt;/td>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form &lt;math>\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1&lt;/math>, where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length. In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>. First, we calculate the distance from the center to each focus: &lt;math>\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4&lt;/math>.&lt;/p>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse. Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>. The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;/tr>\n&lt;/table>\n\nFigure 6: Example of solution reformattting. The left is the original solution (generated by Qwen2-7B-Instruct) and the right is the reformatted one. The problem, coming from the MATH test set, is “The ellipse  $\\frac{(x-6)^2}{25} + \\frac{(y-3)^2}{9} = 1$  has two foci. Find the one with the larger  $x$ -coordinate. Enter your answer as an ordered pair, like  $(2, 1)$ .”\n\n## B Breakdown Statistics of PROCESSBENCH\n\nTable 4: Breakdown statistics of PROCESSBENCH.  $^\\dagger$ : We encountered a code bug when using Llama-3.1-70B-Instruct and Qwen2.5-72B-Instruct to generate solutions for the MATH problems, thus their counts are all zero in the MATH subset of PROCESSBENCH.  $^\\ddagger$ : For the more challenging OlympiadBench and Omni-MATH problems, we exclude models with lower accuracies from subsequent annotation.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Generator&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;math>^\\dagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>13&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>16&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>23&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>53&lt;/td>\n&lt;td>116&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>131&lt;/td>\n&lt;td>31&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>28&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>85&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>19&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-1.5B-Instruct&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>36&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>89&lt;/td>\n&lt;td>42&lt;/td>\n&lt;td>63&lt;/td>\n&lt;td>45&lt;/td>\n&lt;td>96&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>9&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>51&lt;/td>\n&lt;td>64&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>71&lt;/td>\n&lt;td>25&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-1.5B-Instruct&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>10&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>62&lt;/td>\n&lt;td>35&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>75&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>2&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>67&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>88&lt;/td>\n&lt;td>38&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>47&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>99&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>18&lt;/td>\n&lt;td>39&lt;/td>\n&lt;td>59&lt;/td>\n&lt;td>81&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Total&lt;/td>\n&lt;td colspan=\"2\">400&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>## C Training Details of Qwen2.5-Math-7B-PRM800K\n\nQwen2.5-Math-7B-PRM800K is obtained by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K training set. We replace the original language modeling head with a new reward modeling head that outputs binary classification logits. The classification loss is computed at the second line break positions in all the “\\n\\n”. We treat the original 1 and 0 labels in PRM800K as our positive labels, while -1 as negative ones. To eliminate test data contamination, we also remove the PRM800K training samples that have the same problems in PROCESSBENCH. The training was run on eight A100 80GB GPUs.\n\n## D Inference Details\n\nFor solution generation in § 3.2, all the models are set with  $p = 0.9, t = 0.7$ . For majority voting evaluation in § 4, we set  $p = 0.8, t = 0.7, k = 20$  for Qwen2.5-Math-7/72B-Instruct to ensure their normal generation, while all the other models are set with only  $p = 0.9$ . All the inference in the evaluation was run with vLLM (Kwon et al., 2023) on eight A100 80GB GPUs.\n\n## E Prompt Template for Critic Model Evaluation\n\nThe following is a math problem and a solution (split into paragraphs, enclosed with tags and indexed from 0):\n\n[Math Problem]\n\n... (math problem) ...\n\n[Solution]\n\n&lt;paragraph\\_0>\n\n... (paragraph 0 of solution) ...\n\n&lt;/paragraph\\_0>\n\n...\n\n&lt;paragraph\\_n-1>\n\n... (paragraph n-1 of solution) ...\n\n&lt;/paragraph\\_n-1>\n\nYour task is to review and critique the solution paragraph by paragraph. Once you identify an error in a paragraph, return the **index of the paragraph where the earliest error occurs**. Otherwise, return the **index of -1 (which typically denotes \"not found\")**.\n\n**Please put your final answer (i.e., the index) in \\boxed{}.**\n\nFigure 7: Prompt template for critic model evaluation. The **blue texts** indicate the input math problem and the solution (split into paragraphs). The **red texts** describe the required output content and format.## F Supplementary Evaluation Results\n\nTable 5: Breakdown of evaluation results on the GSM8K and MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>24.2&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>21.4&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>37.9&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>43.8&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>90.1&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>",
      "numLines": 500,
      "startLine": 500,
      "totalLines": 1799
    }
  },
  "sourceToolAssistantUUID": "2b23aad9-12e1-49a7-b921-aaa6104c9608",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "7b775eca-f4d1-4c81-a628-7cc44d6255bc",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research methodology",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Tool call

_source line 48 · 2026-05-28T05:09:23.360Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XM1tcXNdV94xKtRedHuoxX`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt",
  "offset": 1000,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b775eca-f4d1-4c81-a628-7cc44d6255bc",
  "isSidechain": false,
  "requestId": "req_011CbUPYkzS4XQw75c7YZjr4",
  "type": "assistant",
  "uuid": "1d661c2f-d8b9-484f-8d14-e5c89705bc56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157f5mUrEpMwGy16knXYtZM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10432,
      "cache_read_input_tokens": 29333,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 29333,
          "cache_creation_input_tokens": 10432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10432
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

_source line 49 · 2026-05-28T05:09:23.371Z_

<details><summary>↩ Tool result · `toolu_01XM1tcXNdV94xKtRedHuoxX`</summary>

```text
1000	&lt;td>36.0&lt;/td>
1001	&lt;td>94.3&lt;/td>
1002	&lt;td>52.1&lt;/td>
1003	&lt;/tr>
1004	&lt;tr>
1005	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
1006	&lt;td>7.7&lt;/td>
1007	&lt;td>100.0&lt;/td>
1008	&lt;td>14.3&lt;/td>
1009	&lt;td>3.4&lt;/td>
1010	&lt;td>98.3&lt;/td>
1011	&lt;td>6.5&lt;/td>
1012	&lt;/tr>
1013	&lt;tr>
1014	&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>
1015	&lt;td>33.8&lt;/td>
1016	&lt;td>96.4&lt;/td>
1017	&lt;td>50.1&lt;/td>
1018	&lt;td>25.4&lt;/td>
1019	&lt;td>92.4&lt;/td>
1020	&lt;td>39.9&lt;/td>
1021	&lt;/tr>
1022	&lt;tr>
1023	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
1024	&lt;td>54.1&lt;/td>
1025	&lt;td>94.8&lt;/td>
1026	&lt;td>68.9&lt;/td>
1027	&lt;td>44.9&lt;/td>
1028	&lt;td>90.6&lt;/td>
1029	&lt;td>60.1&lt;/td>
1030	&lt;/tr>
1031	&lt;tr>
1032	&lt;td>Qwen2-7B-Instruct&lt;/td>
1033	&lt;td>40.6&lt;/td>
1034	&lt;td>4.7&lt;/td>
1035	&lt;td>8.4&lt;/td>
1036	&lt;td>30.5&lt;/td>
1037	&lt;td>13.8&lt;/td>
1038	&lt;td>19.0&lt;/td>
1039	&lt;/tr>
1040	&lt;tr>
1041	&lt;td>Qwen2-72B-Instruct&lt;/td>
1042	&lt;td>57.0&lt;/td>
1043	&lt;td>82.9&lt;/td>
1044	&lt;td>67.6&lt;/td>
1045	&lt;td>37.7&lt;/td>
1046	&lt;td>70.9&lt;/td>
1047	&lt;td>49.2&lt;/td>
1048	&lt;/tr>
1049	&lt;tr>
1050	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
1051	&lt;td>40.6&lt;/td>
1052	&lt;td>33.2&lt;/td>
1053	&lt;td>36.5&lt;/td>
1054	&lt;td>30.8&lt;/td>
1055	&lt;td>45.1&lt;/td>
1056	&lt;td>36.6&lt;/td>
1057	&lt;/tr>
1058	&lt;tr>
1059	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
1060	&lt;td>54.6&lt;/td>
1061	&lt;td>94.8&lt;/td>
1062	&lt;td>69.3&lt;/td>
1063	&lt;td>38.4&lt;/td>
1064	&lt;td>87.4&lt;/td>
1065	&lt;td>53.3&lt;/td>
1066	&lt;/tr>
1067	&lt;tr>
1068	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
1069	&lt;td>49.3&lt;/td>
1070	&lt;td>97.9&lt;/td>
1071	&lt;td>65.6&lt;/td>
1072	&lt;td>36.7&lt;/td>
1073	&lt;td>95.8&lt;/td>
1074	&lt;td>53.1&lt;/td>
1075	&lt;/tr>
1076	&lt;tr>
1077	&lt;td>Qwen2.5-72B-Instruct&lt;/td>
1078	&lt;td>62.8&lt;/td>
1079	&lt;td>96.9&lt;/td>
1080	&lt;td>76.2&lt;/td>
1081	&lt;td>46.3&lt;/td>
1082	&lt;td>93.1&lt;/td>
1083	&lt;td>61.8&lt;/td>
1084	&lt;/tr>
1085	&lt;tr>
1086	&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>
1087	&lt;td>81.6&lt;/td>
1088	&lt;td>95.3&lt;/td>
1089	&lt;td>&lt;b>88.0&lt;/b>&lt;/td>
1090	&lt;td>78.1&lt;/td>
1091	&lt;td>79.3&lt;/td>
1092	&lt;td>&lt;b>78.7&lt;/b>&lt;/td>
1093	&lt;/tr>
1094	&lt;tr>
1095	&lt;td colspan="7" style="text-align: center;">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>
1096	&lt;/tr>
1097	&lt;tr>
1098	&lt;td>GPT-4o-0806&lt;/td>
1099	&lt;td>70.0&lt;/td>
1100	&lt;td>91.2&lt;/td>
1101	&lt;td>79.2&lt;/td>
1102	&lt;td>54.4&lt;/td>
1103	&lt;td>76.6&lt;/td>
1104	&lt;td>63.6&lt;/td>
1105	&lt;/tr>
1106	&lt;tr>
1107	&lt;td>o1-mini&lt;/td>
1108	&lt;td>88.9&lt;/td>
1109	&lt;td>97.9&lt;/td>
1110	&lt;td>93.2&lt;/td>
1111	&lt;td>83.5&lt;/td>
1112	&lt;td>95.1&lt;/td>
1113	&lt;td>88.9&lt;/td>
1114	&lt;/tr>
1115	&lt;/tbody>
1116	&lt;/table>
1117	
1118	Table 6: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the GSM8K and MATH subsets, which are marginally higher than those in Table 5 that all adopt the threshold selected on the GSM8K subset.
1119	
1120	&lt;table border="1">
1121	&lt;thead>
1122	&lt;tr>
1123	&lt;th rowspan="2">Model&lt;/th>
1124	&lt;th colspan="3">GSM8K&lt;/th>
1125	&lt;th colspan="3">MATH&lt;/th>
1126	&lt;/tr>
1127	&lt;tr>
1128	&lt;th>error&lt;/th>
1129	&lt;th>correct&lt;/th>
1130	&lt;th>F1&lt;/th>
1131	&lt;th>error&lt;/th>
1132	&lt;th>correct&lt;/th>
1133	&lt;th>F1&lt;/th>
1134	&lt;/tr>
1135	&lt;/thead>
1136	&lt;tbody>
1137	&lt;tr>
1138	&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>
1139	&lt;td>50.2&lt;/td>
1140	&lt;td>71.5&lt;/td>
1141	&lt;td>59.0&lt;/td>
1142	&lt;td>38.2&lt;/td>
1143	&lt;td>70.4&lt;/td>
1144	&lt;td>49.5&lt;/td>
1145	&lt;/tr>
1146	&lt;tr>
1147	&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>
1148	&lt;td>61.8&lt;/td>
1149	&lt;td>82.9&lt;/td>
1150	&lt;td>70.8&lt;/td>
1151	&lt;td>44.1&lt;/td>
1152	&lt;td>70.9&lt;/td>
1153	&lt;td>54.4&lt;/td>
1154	&lt;/tr>
1155	&lt;/tbody>
1156	&lt;/table>Table 7: Breakdown of evaluation results on the OlympiadBench and Omni-MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.
1157	
1158	&lt;table border="1">
1159	&lt;thead>
1160	&lt;tr>
1161	&lt;th rowspan="2">Model&lt;/th>
1162	&lt;th colspan="3">OlympiadBench&lt;/th>
1163	&lt;th colspan="3">Omni-MATH&lt;/th>
1164	&lt;/tr>
1165	&lt;tr>
1166	&lt;th>error&lt;/th>
1167	&lt;th>correct&lt;/th>
1168	&lt;th>F1&lt;/th>
1169	&lt;th>error&lt;/th>
1170	&lt;th>correct&lt;/th>
1171	&lt;th>F1&lt;/th>
1172	&lt;/tr>
1173	&lt;/thead>
1174	&lt;tbody>
1175	&lt;tr>
1176	&lt;td colspan="7" style="text-align: center;">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>
1177	&lt;/tr>
1178	&lt;tr>
1179	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
1180	&lt;td>15.0&lt;/td>
1181	&lt;td>71.1&lt;/td>
1182	&lt;td>24.8&lt;/td>
1183	&lt;td>14.2&lt;/td>
1184	&lt;td>73.0&lt;/td>
1185	&lt;td>23.8&lt;/td>
1186	&lt;/tr>
1187	&lt;tr>
1188	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
1189	&lt;td>8.2&lt;/td>
1190	&lt;td>43.1&lt;/td>
1191	&lt;td>13.8&lt;/td>
1192	&lt;td>9.6&lt;/td>
1193	&lt;td>45.2&lt;/td>
1194	&lt;td>15.8&lt;/td>
1195	&lt;/tr>
1196	&lt;tr>
1197	&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>
1198	&lt;td>10.1&lt;/td>
1199	&lt;td>51.0&lt;/td>
1200	&lt;td>16.9&lt;/td>
1201	&lt;td>10.1&lt;/td>
1202	&lt;td>51.9&lt;/td>
1203	&lt;td>16.9&lt;/td>
1204	&lt;/tr>
1205	&lt;tr>
1206	&lt;td>Skywork-PRM-1.5B&lt;/td>
1207	&lt;td>15.4&lt;/td>
1208	&lt;td>26.0&lt;/td>
1209	&lt;td>19.3&lt;/td>
1210	&lt;td>13.6&lt;/td>
1211	&lt;td>32.8&lt;/td>
1212	&lt;td>19.2&lt;/td>
1213	&lt;/tr>
1214	&lt;tr>
1215	&lt;td>Skywork-PRM-7B&lt;/td>
1216	&lt;td>17.9&lt;/td>
1217	&lt;td>31.9&lt;/td>
1218	&lt;td>22.9&lt;/td>
1219	&lt;td>14.0&lt;/td>
1220	&lt;td>41.9&lt;/td>
1221	&lt;td>21.0&lt;/td>
1222	&lt;/tr>
1223	&lt;tr>
1224	&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>
1225	&lt;td>&lt;b>35.7&lt;/b>&lt;/td>
1226	&lt;td>&lt;b>87.3&lt;/b>&lt;/td>
1227	&lt;td>&lt;b>50.7&lt;/b>&lt;/td>
1228	&lt;td>&lt;b>29.8&lt;/b>&lt;/td>
1229	&lt;td>&lt;b>86.3&lt;/b>&lt;/td>
1230	&lt;td>&lt;b>44.3&lt;/b>&lt;/td>
1231	&lt;/tr>
1232	&lt;tr>
1233	&lt;td colspan="7" style="text-align: center;">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>
1234	&lt;/tr>
1235	&lt;tr>
1236	&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>
1237	&lt;td>27.1&lt;/td>
1238	&lt;td>2.7&lt;/td>
1239	&lt;td>4.8&lt;/td>
1240	&lt;td>26.1&lt;/td>
1241	&lt;td>8.3&lt;/td>
1242	&lt;td>12.6&lt;/td>
1243	&lt;/tr>
1244	&lt;tr>
1245	&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>
1246	&lt;td>12.0&lt;/td>
1247	&lt;td>92.0&lt;/td>
1248	&lt;td>21.2&lt;/td>
1249	&lt;td>11.2&lt;/td>
1250	&lt;td>91.7&lt;/td>
1251	&lt;td>20.0&lt;/td>
1252	&lt;/tr>
1253	&lt;tr>
1254	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
1255	&lt;td>32.4&lt;/td>
1256	&lt;td>1.5&lt;/td>
1257	&lt;td>2.8&lt;/td>
1258	&lt;td>32.0&lt;/td>
1259	&lt;td>0.8&lt;/td>
1260	&lt;td>1.6&lt;/td>
1261	&lt;/tr>
1262	&lt;tr>
1263	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
1264	&lt;td>35.1&lt;/td>
1265	&lt;td>69.9&lt;/td>
1266	&lt;td>46.7&lt;/td>
1267	&lt;td>30.7&lt;/td>
1268	&lt;td>61.8&lt;/td>
1269	&lt;td>41.0&lt;/td>
1270	&lt;/tr>
1271	&lt;tr>
1272	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
1273	&lt;td>31.0&lt;/td>
1274	&lt;td>94.1&lt;/td>
1275	&lt;td>46.7&lt;/td>
1276	&lt;td>28.2&lt;/td>
1277	&lt;td>90.5&lt;/td>
1278	&lt;td>43.0&lt;/td>
1279	&lt;/tr>
1280	&lt;tr>
1281	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
1282	&lt;td>7.7&lt;/td>
1283	&lt;td>91.7&lt;/td>
1284	&lt;td>14.2&lt;/td>
1285	&lt;td>6.9&lt;/td>
1286	&lt;td>88.0&lt;/td>
1287	&lt;td>12.7&lt;/td>
1288	&lt;/tr>
1289	&lt;tr>
1290	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
1291	&lt;td>19.5&lt;/td>
1292	&lt;td>97.3&lt;/td>
1293	&lt;td>32.5&lt;/td>
1294	&lt;td>19.0&lt;/td>
1295	&lt;td>96.3&lt;/td>
1296	&lt;td>31.7&lt;/td>
1297	&lt;/tr>
1298	&lt;tr>
1299	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d661c2f-d8b9-484f-8d14-e5c89705bc56",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "accf4201-01ef-46b7-9cb9-38d517f0a171",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/fd4fd56a-809d-4417-b1f0-e25513d9de0c/tool-results/toolu_01B8vR8gQEvzW1VoxSRAmEfj.txt",
      "content": "&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>54.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>44.9&lt;/td>\n&lt;td>90.6&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>30.5&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>45.1&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>95.8&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 6: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the GSM8K and MATH subsets, which are marginally higher than those in Table 5 that all adopt the threshold selected on the GSM8K subset.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>38.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>49.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>44.1&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Table 7: Breakdown of evaluation results on the OlympiadBench and Omni-MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>15.0&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>8.2&lt;/td>\n&lt;td>43.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>29.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>",
      "numLines": 300,
      "startLine": 1000,
      "totalLines": 1799
    }
  },
  "sourceToolAssistantUUID": "1d661c2f-d8b9-484f-8d14-e5c89705bc56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-28T05:09:26.532Z_

<details><summary>Logged reasoning block</summary>

```text
I now have extensive content from the paper. Let me also try to find the OpenReview page for ACL 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "accf4201-01ef-46b7-9cb9-38d517f0a171",
  "isSidechain": false,
  "requestId": "req_011CbUPZAJPpR5xPBAtwFvbc",
  "type": "assistant",
  "uuid": "b7372967-7cec-419e-a8c7-d1be37d0d845",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzQmCCkay4zSYi4f2cJriP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 39765,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 39765,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
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

_source line 51 · 2026-05-28T05:09:27.093Z_

Now let me try to find the ACL 2025 OpenReview page specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7372967-7cec-419e-a8c7-d1be37d0d845",
  "isSidechain": false,
  "requestId": "req_011CbUPZAJPpR5xPBAtwFvbc",
  "type": "assistant",
  "uuid": "7a60126b-fab2-4f5d-a7e1-a7b53c209d0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzQmCCkay4zSYi4f2cJriP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 39765,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 39765,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
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

_source line 52 · 2026-05-28T05:09:28.512Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XbzVHPd9vMpP7k1vZ7pAEM`</summary>

```json
{
  "url": "https://openreview.net/forum?id=ProcessBench",
  "prompt": "Find reviewer comments, scores, and author responses for ProcessBench paper at ACL 2025."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a60126b-fab2-4f5d-a7e1-a7b53c209d0e",
  "isSidechain": false,
  "requestId": "req_011CbUPZAJPpR5xPBAtwFvbc",
  "type": "assistant",
  "uuid": "c239dbec-7764-4a5c-b6ce-a0223f9a73b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzQmCCkay4zSYi4f2cJriP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 39765,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 39765,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
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

_source line 53 · 2026-05-28T05:09:30.160Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NqZoaUKkpXB8CDSCg3K5B9`</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/ProcessBench%3A-Identifying-Process-Errors-in-Zheng/",
  "prompt": "Find the Semantic Scholar page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" by Zheng et al. Extract citation count, TLDR, and any other metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c239dbec-7764-4a5c-b6ce-a0223f9a73b6",
  "isSidechain": false,
  "requestId": "req_011CbUPZAJPpR5xPBAtwFvbc",
  "type": "assistant",
  "uuid": "7087c85a-c01c-4e24-9d69-582f6b48bd14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SzQmCCkay4zSYi4f2cJriP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 39765,
      "output_tokens": 291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 291,
          "cache_read_input_tokens": 39765,
          "cache_creation_input_tokens": 4126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4126
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

_source line 54 · 2026-05-28T05:09:31.354Z_

<details><summary>↩ Tool result · `toolu_01XbzVHPd9vMpP7k1vZ7pAEM`</summary>

```text
# Unable to Locate ProcessBench Paper

I cannot provide the reviewer comments, scores, and author responses you're looking for. The OpenReview page indicates that "The Note ProcessBench was not found," suggesting this paper is either not yet published on the platform, uses a different title, or may be hosted elsewhere.

To find this paper, I'd recommend:
- Checking the ACL 2025 venue page directly on OpenReview
- Searching by author name if you know it
- Visiting the official ACL 2025 conference proceedings
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c239dbec-7764-4a5c-b6ce-a0223f9a73b6",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "61d54cd4-a358-4f45-ae89-a339f2364b94",
  "toolUseResult": {
    "bytes": 58581,
    "code": 200,
    "codeText": "OK",
    "result": "# Unable to Locate ProcessBench Paper\n\nI cannot provide the reviewer comments, scores, and author responses you're looking for. The OpenReview page indicates that \"The Note ProcessBench was not found,\" suggesting this paper is either not yet published on the platform, uses a different title, or may be hosted elsewhere.\n\nTo find this paper, I'd recommend:\n- Checking the ACL 2025 venue page directly on OpenReview\n- Searching by author name if you know it\n- Visiting the official ACL 2025 conference proceedings",
    "durationMs": 2838,
    "url": "https://openreview.net/forum?id=ProcessBench"
  },
  "sourceToolAssistantUUID": "c239dbec-7764-4a5c-b6ce-a0223f9a73b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-28T05:09:32.671Z_

<details><summary>↩ Tool result · `toolu_01NqZoaUKkpXB8CDSCg3K5B9`</summary>

```text
I appreciate your request, but I'm unable to help with this task. The web page content provided appears to be empty (no actual text between the dashes), so I have no source material to extract information from.

To find the Semantic Scholar page for "ProcessBench: Identifying Process Errors in Mathematical Reasoning" by Zheng et al., you would need to:

1. Visit **semanticscholar.org** directly
2. Use their search function to locate the paper title
3. Review the citation count, abstract/TLDR, and metadata displayed on the paper's dedicated page

If you can provide the actual page content or a URL, I'd be happy to help extract the specific information you're looking for while adhering to your guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7087c85a-c01c-4e24-9d69-582f6b48bd14",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "d7d5c551-22bd-4741-8ca8-f62ab84de8bf",
  "toolUseResult": {
    "bytes": 0,
    "code": 202,
    "codeText": "Accepted",
    "result": "I appreciate your request, but I'm unable to help with this task. The web page content provided appears to be empty (no actual text between the dashes), so I have no source material to extract information from.\n\nTo find the Semantic Scholar page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" by Zheng et al., you would need to:\n\n1. Visit **semanticscholar.org** directly\n2. Use their search function to locate the paper title\n3. Review the citation count, abstract/TLDR, and metadata displayed on the paper's dedicated page\n\nIf you can provide the actual page content or a URL, I'd be happy to help extract the specific information you're looking for while adhering to your guidelines.",
    "durationMs": 2509,
    "url": "https://www.semanticscholar.org/paper/ProcessBench%3A-Identifying-Process-Errors-in-Zheng/"
  },
  "sourceToolAssistantUUID": "7087c85a-c01c-4e24-9d69-582f6b48bd14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-28T05:09:39.728Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01P1LdxVNE9kycKMK5hRiuzd`</summary>

```json
{
  "url": "https://www.semanticscholar.org/search?q=ProcessBench+Identifying+Process+Errors+Mathematical+Reasoning&sort=relevance",
  "prompt": "Find the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" and extract its citation count, any TLDR summary, and influential citations if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7d5c551-22bd-4741-8ca8-f62ab84de8bf",
  "isSidechain": false,
  "requestId": "req_011CbUPZqGBtHuE2UCPN6Xb5",
  "type": "assistant",
  "uuid": "003bcddb-2444-41ad-a680-ee0071c463a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Gxm2Z2hGcQpDzkvbaaSTG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 43891,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 43891,
          "cache_creation_input_tokens": 634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 634
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

_source line 57 · 2026-05-28T05:09:42.779Z_

<details><summary>↩ Tool result · `toolu_01P1LdxVNE9kycKMK5hRiuzd`</summary>

```text
I apologize, but I cannot extract the requested information from the provided content. The web page snippet you shared only shows the header and navigation elements of a Semantic Scholar page for "ProcessBench: Identifying Process Errors in Mathematical Reasoning" — it does not include the actual paper details such as citation count, TLDR summary, or influential citations.

To obtain this information, you would need to:

1. Visit the full Semantic Scholar page for this paper
2. Look for the citation count (typically displayed prominently)
3. Scroll to find the TLDR section if available
4. Check for "Highly Influenced Papers" or similar sections

If you can provide the complete page content with these details, I'd be happy to extract and summarize the information according to your specifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "003bcddb-2444-41ad-a680-ee0071c463a9",
  "isSidechain": false,
  "promptId": "f1bde50b-54a7-4c46-9eea-cb63fcd83c97",
  "type": "user",
  "uuid": "6c00760c-e014-48d5-804e-dd32493b1d82",
  "toolUseResult": {
    "bytes": 95099,
    "code": 200,
    "codeText": "OK",
    "result": "I apologize, but I cannot extract the requested information from the provided content. The web page snippet you shared only shows the header and navigation elements of a Semantic Scholar page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" — it does not include the actual paper details such as citation count, TLDR summary, or influential citations.\n\nTo obtain this information, you would need to:\n\n1. Visit the full Semantic Scholar page for this paper\n2. Look for the citation count (typically displayed prominently)\n3. Scroll to find the TLDR section if available\n4. Check for \"Highly Influenced Papers\" or similar sections\n\nIf you can provide the complete page content with these details, I'd be happy to extract and summarize the information according to your specifications.",
    "durationMs": 3046,
    "url": "https://www.semanticscholar.org/search?q=ProcessBench+Identifying+Process+Errors+Mathematical+Reasoning&sort=relevance"
  },
  "sourceToolAssistantUUID": "003bcddb-2444-41ad-a680-ee0071c463a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 58 · 2026-05-28T05:09:42.782Z_

```json
{
  "parentUuid": "6c00760c-e014-48d5-804e-dd32493b1d82",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "66e7664c-12e2-4bf5-88f3-806581b04128",
  "timestamp": "2026-05-28T05:09:42.782Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 59 · 2026-05-28T05:10:07.981Z_

<details><summary>Logged reasoning block</summary>

```text
I have enough information to produce a thorough analysis of the paper. Let me now synthesize everything I've read into the requested JSON format. Let me review what I've gathered:

**Paper details:**
- Title: ProcessBench: Identifying Process Errors in Mathematical Reasoning
- Authors: Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin (Qwen Team, Alibaba)
- Venue: ACL 2025
- 3,400 test cases from GSM8K, MATH, OlympiadBench, Omni-MATH


- 4 datasets with 12 solution generators from Qwen and LLaMA families

The core contribution is a benchmark where humans annotated the earliest erroneous step in mathematical solutions, revealing that existing process reward models struggle to generalize across datasets while prompted critic models—particularly reasoning-based ones like QwQ-32B-Preview—perform significantly better, and that harder problems tend to contain more process errors even when reaching correct final answers. The harder problems reveal a critical flaw in how PRMs are trained—on competition-level math, correct final answers often mask flawed reasoning, so the standard approach of using final answer correctness to label step validity breaks down. This benchmark exposes that existing PRM datasets are too easy or synthetic, and the real innovation is showing that the entire paradigm has a generalization problem rather than just needing more data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66e7664c-12e2-4bf5-88f3-806581b04128",
  "isSidechain": false,
  "requestId": "req_011CbUPaaN292Ma7nVd9RStn",
  "type": "assistant",
  "uuid": "dc21af46-fb5a-430e-ab71-0dfc791dc4f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8iesLm4q2DKi4PwG6o3Eg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 44525,
      "output_tokens": 2775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2775,
          "cache_read_input_tokens": 44525,
          "cache_creation_input_tokens": 419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 419
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

_source line 60 · 2026-05-28T05:10:52.200Z_

Now I have comprehensive content from the paper. Let me synthesize the full analysis.

```json
{
  "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
  "venue": "ACL 2025",
  "problem_identification": "The authors identified that existing benchmarks for evaluating step-level reasoning assessment (CriticBench, MathCheck-GSM, PRM800K test set) suffer from a triple deficiency: too-easy problems (GSM8K/MATH-level), too-small scale (PRM800K has only 90 usable test cases), and/or lack of human step-level error annotations. They found this gap by observing that PRMs were being evaluated only indirectly — via Best-of-N reranking accuracy — which conflates the quality of the solution generator with the quality of the verifier, and never directly tests whether a PRM can actually locate where reasoning goes wrong.",
  "key_insight": "By constructing a direct, step-level error-location benchmark at competition/Olympiad difficulty, the authors revealed two things the field had missed: (1) existing PRMs trained via Monte Carlo step-label estimation catastrophically fail to generalize beyond the difficulty level of their training data, and (2) on harder problems, language models produce correct final answers through erroneous reasoning at alarming rates (51.8% on Omni-MATH), which fundamentally undermines the data synthesis methodology used to train those PRMs in the first place — the process labels themselves are corrupted because 'leads to correct answer' ≠ 'reasoning step is correct.'",
  "innovation_type": "new_benchmark",
  "method_summary": "ProcessBench consists of 3,400 test cases drawn from four datasets of increasing difficulty (GSM8K, MATH, OlympiadBench, Omni-MATH), with solutions generated by 12 diverse open-source models (Qwen and LLaMA families). Solutions undergo a reformatting step using Qwen2.5-72B-Instruct to standardize step granularity before annotation. Doctoral-level math experts annotate the earliest erroneous step in each solution, requiring 3-out-of-up-to-5 annotator agreement (with ~30% of solutions discarded when consensus cannot be reached). The benchmark evaluates two model classes on an F1 metric (harmonic mean of accuracy on erroneous and correct samples): PRMs that output per-step correctness scores, and critic models that are general LLMs prompted to critique solutions step-by-step. A key methodological control is balanced sampling of solutions with correct vs. incorrect final answers, which enabled the discovery of high process-error rates among ostensibly correct solutions.",
  "what_makes_it_good": "Three things made this paper compelling for a top venue. First, the benchmark design is deceptively simple (find the first wrong step) yet surgically diagnostic — it separates process understanding from outcome-based evaluation, exposing a blind spot in how the entire PRM subfield was being assessed. Second, the empirical finding that 51.8% of correct-answer Olympiad solutions contain process errors is a genuinely surprising, field-redirecting result that challenges the fundamental assumption behind Monte Carlo PRM training (that correct answers imply correct reasoning). Third, the paper demonstrates that a straightforward PRM trained on fully human-annotated PRM800K data (56.5 avg F1) dramatically outperforms PRMs trained with fancier automated data synthesis (28-42 avg F1), providing a simple but provocative baseline that reframes the conversation around data quality vs. data synthesis methodology.",
  "limitations_acknowledged": "The authors acknowledge that ProcessBench may still contain inaccurate labels, particularly for Olympiad-level problems where even doctoral annotators found the task challenging. They also note that the ~30% discard rate due to annotator disagreement could bias the problem distribution, as discarded solutions likely involve the hardest problems that may exceed annotator capabilities.",
  "open_questions": [
    "How should PRM training data be constructed for harder-than-MATH problems, given that Monte Carlo estimation of step correctness breaks down when correct final answers frequently arise from flawed reasoning? The paper exposes the problem but does not propose a solution beyond 'use human annotations.'",
    "Can the gap between o1-mini (87.9 F1) and the best open-source model QwQ-32B-Preview (71.5 F1) be closed through better critic prompting or training, or does it require fundamentally different reasoning architectures? The 16-point gap on critic capability is much larger than the gap on problem-solving.",
    "What is the right granularity for step-level supervision? The paper uses LLM-based reformatting to standardize steps, but the interplay between step granularity and error detection difficulty remains unexplored — finer steps might make errors easier to localize but harder to annotate."
  ],
  "building_blocks": [
    "PRM800K dataset (Lightman et al., 2023) — used both as a training set for their baseline PRM and as a comparison benchmark",
    "GSM8K, MATH, OlympiadBench, Omni-MATH test sets — the problem sources spanning grade school to Olympiad difficulty",
    "LLM-based solution reformatting — using a strong model to standardize step granularity while preserving content",
    "Multi-annotator consensus protocol with escalation (3-of-3, then 3-of-4, then 3-of-5) — a reusable quality control methodology",
    "F1 score over binary (error/correct) classification — balances sensitivity vs. specificity for evaluating process reward models",
    "Step-by-step critique prompting template — a simple but effective way to repurpose general LLMs as critic models",
    "Majority voting over 8 samplings — used for evaluating open-source critic models",
    "12 diverse solution generators (Qwen2/2.5, LLaMA 3/3.1 across multiple sizes) — ensuring solution style diversity"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is the foundational evaluation infrastructure for the PRM research area — any new process reward model or step-level verification method must now benchmark against ProcessBench. More critically, it exposes a fundamental flaw in current PRM training methodology: Monte Carlo step-label estimation breaks down on hard problems because correct final answers don't reliably indicate correct reasoning. This directly informs future PRM research by suggesting that either human annotation, stronger automated verification, or fundamentally different credit assignment strategies are needed for the next generation of process reward models."
}
```

## Key Craft Lessons for Researchers

**1. The "diagnostic benchmark" template**: The authors didn't just build a benchmark — they built a *diagnostic tool* that reveals a specific failure mode. The task (find the first wrong step) is simple enough to be unambiguous yet powerful enough to expose that PRMs aren't actually learning process verification.

**2. Let the data surprise you**: The most impactful finding (51.8% process error rate in correct-answer Olympiad solutions) wasn't the paper's main hypothesis — it emerged from the balanced sampling design decision. This is an example of careful experimental design enabling serendipitous discovery.

**3. The "embarrassingly simple baseline" strategy**: Their Qwen2.5-Math-7B-PRM800K model is just a straightforward fine-tune on existing human-annotated data, yet it crushes PRMs built with more sophisticated automated pipelines. This kind of "simple thing that works better than complex thing" result is extremely publishable because it forces the community to reconsider its assumptions.

**4. Scaling the difficulty axis, not just the data axis**: Most benchmark papers add more data. This paper's key move was adding *harder* problems, which revealed qualitatively different failure modes (PRMs collapsing from 70.8 → 21.0 F1 from GSM8K to Omni-MATH) that would be invisible at easier difficulty levels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc21af46-fb5a-430e-ab71-0dfc791dc4f2",
  "isSidechain": false,
  "requestId": "req_011CbUPaaN292Ma7nVd9RStn",
  "type": "assistant",
  "uuid": "0cdd1a2c-d42d-43af-9fd4-9f12f94c592b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y8iesLm4q2DKi4PwG6o3Eg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 419,
      "cache_read_input_tokens": 44525,
      "output_tokens": 2775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 419,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2775,
          "cache_read_input_tokens": 44525,
          "cache_creation_input_tokens": 419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 419
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

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "0cdd1a2c-d42d-43af-9fd4-9f12f94c592b",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research methodology",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "0cdd1a2c-d42d-43af-9fd4-9f12f94c592b",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research methodology",
  "sessionId": "fd4fd56a-809d-4417-b1f0-e25513d9de0c"
}
```

---
