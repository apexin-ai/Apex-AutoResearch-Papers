# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 85
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-2/622fde7e-49a1-441f-a25d-d298deae6922.jsonl`
- **Structured JSON:** [`f77e489f2396c852e980.json`](../../sessions/f7/f77e489f2396c852e980.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T16:06:49.048Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T16:06:49.048Z",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**\n\n## Paper to analyze\n\n{\n  \"title\": \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\",\n  \"authors\": \"Zheng et al.\",\n  \"venue\": \"ACL 2025\",\n  \"url\": \"https://arxiv.org/abs/2412.06559\",\n  \"why_important\": \"ACL 2025; from Alibaba Qwen team; established the standard benchmark (3,400 expert-annotated cases) for evaluating step-level error detection in mathematical reasoning; widely used for PRM evaluation\",\n  \"one_line_summary\": \"Introduces ProcessBench, a benchmark of 3,400 competition/Olympiad-level math problems with expert-annotated error locations, revealing that existing PRMs struggle on harder problems and are outperformed by prompted critique models.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T16:06:49.051Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T16:06:49.051Z",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

## Round 1

83 recorded events

### User

_source line 3 · 2026-05-27T16:06:49.064Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**

## Paper to analyze

{
  "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
  "authors": "Zheng et al.",
  "venue": "ACL 2025",
  "url": "https://arxiv.org/abs/2412.06559",
  "why_important": "ACL 2025; from Alibaba Qwen team; established the standard benchmark (3,400 expert-annotated cases) for evaluating step-level error detection in mathematical reasoning; widely used for PRM evaluation",
  "one_line_summary": "Introduces ProcessBench, a benchmark of 3,400 competition/Olympiad-level math problems with expert-annotated error locations, revealing that existing PRMs struggle on harder problems and are outperformed by prompted critique models."
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
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "b2a81d0a-890c-46fa-8bff-1d3a3deac9c8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T16:06:49.063Z_

```json
{
  "parentUuid": "b2a81d0a-890c-46fa-8bff-1d3a3deac9c8",
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
  "uuid": "4bca6352-f402-47f9-a9eb-20ce03d0aaba",
  "timestamp": "2026-05-27T16:06:49.063Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T16:06:49.063Z_

```json
{
  "parentUuid": "4bca6352-f402-47f9-a9eb-20ce03d0aaba",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3bc7613a-a2ca-448a-ab98-101f840ed3f2",
  "timestamp": "2026-05-27T16:06:49.063Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
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
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Assistant

_source line 7 · 2026-05-27T16:06:52.144Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this paper by first fetching it from arXiv to read the full content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bc7613a-a2ca-448a-ab98-101f840ed3f2",
  "isSidechain": false,
  "requestId": "req_011CbTMswevSGGDScQ5WigLe",
  "type": "assistant",
  "uuid": "9bc37924-3ea1-490d-8fb8-d8ccbe578aec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113MsFkzSCrgQ9TLvftraZn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2200,
      "cache_read_input_tokens": 11014,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2200
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

_source line 8 · 2026-05-27T16:06:52.364Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015q3BNzgZQrV5KTM3w9gjA4`</summary>

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
  "parentUuid": "9bc37924-3ea1-490d-8fb8-d8ccbe578aec",
  "isSidechain": false,
  "requestId": "req_011CbTMswevSGGDScQ5WigLe",
  "type": "assistant",
  "uuid": "6c5c0817-b074-4a7b-b6ac-c45814dffea0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113MsFkzSCrgQ9TLvftraZn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2200,
      "cache_read_input_tokens": 11014,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2200
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

_source line 9 · 2026-05-27T16:06:52.375Z_

<details><summary>↩ Tool result · `toolu_015q3BNzgZQrV5KTM3w9gjA4`</summary>

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
  "parentUuid": "6c5c0817-b074-4a7b-b6ac-c45814dffea0",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "05b6bba6-835f-4f91-866e-4981879c268a",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6c5c0817-b074-4a7b-b6ac-c45814dffea0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T16:06:56.885Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full PDF (via HTML version) to get comprehensive content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b6bba6-835f-4f91-866e-4981879c268a",
  "isSidechain": false,
  "requestId": "req_011CbTMtBvuwjmXvvwfVAAUp",
  "type": "assistant",
  "uuid": "1350a9a4-e948-4499-ba39-90f73d5168e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XV4e9E6SfybYpUvxEyBLyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13214,
      "output_tokens": 495,
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
          "output_tokens": 495,
          "cache_read_input_tokens": 13214,
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

_source line 11 · 2026-05-27T16:06:57.462Z_

Let me fetch the paper content from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1350a9a4-e948-4499-ba39-90f73d5168e0",
  "isSidechain": false,
  "requestId": "req_011CbTMtBvuwjmXvvwfVAAUp",
  "type": "assistant",
  "uuid": "bf1fba40-d0cd-41fa-9426-cd2e7b3e0142",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XV4e9E6SfybYpUvxEyBLyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13214,
      "output_tokens": 495,
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
          "output_tokens": 495,
          "cache_read_input_tokens": 13214,
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

_source line 12 · 2026-05-27T16:06:59.241Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bm462epEvW7g7A12trgCuF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.06559",
  "prompt": "Extract the full abstract, author list, and any other metadata available on this arXiv page for the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\". Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf1fba40-d0cd-41fa-9426-cd2e7b3e0142",
  "isSidechain": false,
  "requestId": "req_011CbTMtBvuwjmXvvwfVAAUp",
  "type": "assistant",
  "uuid": "f42e3a69-e4f1-4e8c-979e-c97b165412fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XV4e9E6SfybYpUvxEyBLyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13214,
      "output_tokens": 495,
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
          "output_tokens": 495,
          "cache_read_input_tokens": 13214,
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

_source line 13 · 2026-05-27T16:07:03.230Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UT1xEUQE7Y1fwbt1UBzTtg`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.06559",
  "prompt": "Extract the FULL content of this paper, including: \n1. The complete Introduction section\n2. The complete Method/Approach section (how they built ProcessBench, annotation process, data collection)\n3. The complete Experiments/Results section (what models were evaluated, key findings, tables)\n4. The complete Related Work section\n5. The complete Conclusion/Discussion section\n6. Any limitations section\n\nBe as thorough and detailed as possible. Include specific numbers, findings, and technical details. Do NOT summarize - extract the actual content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f42e3a69-e4f1-4e8c-979e-c97b165412fb",
  "isSidechain": false,
  "requestId": "req_011CbTMtBvuwjmXvvwfVAAUp",
  "type": "assistant",
  "uuid": "c2780a62-9e5d-45ec-9bd4-659954e7e41a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XV4e9E6SfybYpUvxEyBLyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13214,
      "output_tokens": 495,
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
          "output_tokens": 495,
          "cache_read_input_tokens": 13214,
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

_source line 14 · 2026-05-27T16:07:03.263Z_

<details><summary>↩ Tool result · `toolu_01UT1xEUQE7Y1fwbt1UBzTtg`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2780a62-9e5d-45ec-9bd4-659954e7e41a",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "f9634454-be80-49fc-992e-2bde85f5d894",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 26,
    "url": "https://arxiv.org/html/2412.06559"
  },
  "sourceToolAssistantUUID": "c2780a62-9e5d-45ec-9bd4-659954e7e41a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T16:07:04.190Z_

<details><summary>↩ Tool result · `toolu_01Bm462epEvW7g7A12trgCuF`</summary>

```text
# ProcessBench Paper Metadata

**Title:** ProcessBench: Identifying Process Errors in Mathematical Reasoning

**Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin

**ArXiv ID:** 2412.06559

**Submission Date:** December 9, 2024 (v1); Last revised May 26, 2025 (v4)

**Subject Categories:** cs.AI; cs.CL; cs.LG

**Venue:** ACL 2025

**Abstract:** The authors present a benchmark called ProcessBench designed to evaluate models' capability in "identifying erroneous steps in mathematical reasoning." The dataset comprises "3,400 test cases, primarily focused on competition- and Olympiad-level math problems." Each case includes "a step-by-step solution with error location annotated by human experts." The paper evaluates both process reward models and critic models, finding that "existing PRMs typically fail to generalize to more challenging math problems" and that "QwQ-32B-Preview has demonstrated the critique capability competitive with the proprietary model GPT-4o."

**DOI:** https://doi.org/10.48550/arXiv.2412.06559
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f42e3a69-e4f1-4e8c-979e-c97b165412fb",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "789503a1-8515-497c-8403-4639853c46c3",
  "toolUseResult": {
    "bytes": 48079,
    "code": 200,
    "codeText": "OK",
    "result": "# ProcessBench Paper Metadata\n\n**Title:** ProcessBench: Identifying Process Errors in Mathematical Reasoning\n\n**Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin\n\n**ArXiv ID:** 2412.06559\n\n**Submission Date:** December 9, 2024 (v1); Last revised May 26, 2025 (v4)\n\n**Subject Categories:** cs.AI; cs.CL; cs.LG\n\n**Venue:** ACL 2025\n\n**Abstract:** The authors present a benchmark called ProcessBench designed to evaluate models' capability in \"identifying erroneous steps in mathematical reasoning.\" The dataset comprises \"3,400 test cases, primarily focused on competition- and Olympiad-level math problems.\" Each case includes \"a step-by-step solution with error location annotated by human experts.\" The paper evaluates both process reward models and critic models, finding that \"existing PRMs typically fail to generalize to more challenging math problems\" and that \"QwQ-32B-Preview has demonstrated the critique capability competitive with the proprietary model GPT-4o.\"\n\n**DOI:** https://doi.org/10.48550/arXiv.2412.06559",
    "durationMs": 4946,
    "url": "https://arxiv.org/abs/2412.06559"
  },
  "sourceToolAssistantUUID": "f42e3a69-e4f1-4e8c-979e-c97b165412fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T16:07:04.437Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01W937mQ9FkAZLbWBdcP1dKN`</summary>

```json
{
  "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors+Mathematical+Reasoning",
  "prompt": "Find the OpenReview page for the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" by Zheng et al. Return any links to the paper's review page, reviewer comments, scores, or discussion threads."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "789503a1-8515-497c-8403-4639853c46c3",
  "isSidechain": false,
  "requestId": "req_011CbTMtBvuwjmXvvwfVAAUp",
  "type": "assistant",
  "uuid": "4e040242-13f3-40e3-b082-777ff3758bca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XV4e9E6SfybYpUvxEyBLyH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 13214,
      "output_tokens": 495,
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
          "output_tokens": 495,
          "cache_read_input_tokens": 13214,
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

_source line 17 · 2026-05-27T16:07:07.398Z_

<details><summary>↩ Tool result · `toolu_01W937mQ9FkAZLbWBdcP1dKN`</summary>

```text
# Response

Based on the webpage content provided, I cannot locate the OpenReview page for "ProcessBench: Identifying Process Errors in Mathematical Reasoning" by Zheng et al. 

The content shown is only the OpenReview.net homepage footer and navigation menu. It does not contain any search results, paper listings, or specific links to the paper you're looking for.

To find this paper, you would need to:
- Use the search function on OpenReview.net
- Navigate to "All Venues" to browse conference proceedings
- Access the paper's dedicated page directly if you have its URL

The homepage states that OpenReview is "a long-term project to advance science through improved peer review," but the specific paper details are not visible in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e040242-13f3-40e3-b082-777ff3758bca",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "b3ed4ef7-4446-4f12-98cd-6a7f2e2f863c",
  "toolUseResult": {
    "bytes": 62389,
    "code": 200,
    "codeText": "OK",
    "result": "# Response\n\nBased on the webpage content provided, I cannot locate the OpenReview page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" by Zheng et al. \n\nThe content shown is only the OpenReview.net homepage footer and navigation menu. It does not contain any search results, paper listings, or specific links to the paper you're looking for.\n\nTo find this paper, you would need to:\n- Use the search function on OpenReview.net\n- Navigate to \"All Venues\" to browse conference proceedings\n- Access the paper's dedicated page directly if you have its URL\n\nThe homepage states that OpenReview is \"a long-term project to advance science through improved peer review,\" but the specific paper details are not visible in the provided content.",
    "durationMs": 2958,
    "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors+Mathematical+Reasoning"
  },
  "sourceToolAssistantUUID": "4e040242-13f3-40e3-b082-777ff3758bca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-27T16:07:10.393Z_

<details><summary>Logged reasoning block</summary>

```text
The HTML version returned a 404. Let me try the PDF version or another format. Let me also try to find the OpenReview page directly for ACL 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3ed4ef7-4446-4f12-98cd-6a7f2e2f863c",
  "isSidechain": false,
  "requestId": "req_011CbTMuHwqaCaKSnh3etLo1",
  "type": "assistant",
  "uuid": "bfa05b0f-3b72-4581-9978-7419a355779f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqEWbiMxmd82f1W4cY78No",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 13846,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 13846,
          "cache_creation_input_tokens": 1109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1109
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

_source line 19 · 2026-05-27T16:07:10.913Z_

Let me try alternative URLs to get the full paper content and find reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfa05b0f-3b72-4581-9978-7419a355779f",
  "isSidechain": false,
  "requestId": "req_011CbTMuHwqaCaKSnh3etLo1",
  "type": "assistant",
  "uuid": "dc314169-2894-46a8-af72-b38fd3dde7f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqEWbiMxmd82f1W4cY78No",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 13846,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 13846,
          "cache_creation_input_tokens": 1109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1109
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

_source line 20 · 2026-05-27T16:07:12.379Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vnw9L18BZinp1ZbefKMvFs`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.06559v4",
  "prompt": "Extract the FULL content of this paper, including:\n1. The complete Introduction section\n2. The complete Method/Approach section (how they built ProcessBench, annotation process, data collection)\n3. The complete Experiments/Results section (what models were evaluated, key findings, tables)\n4. The complete Related Work section\n5. The complete Conclusion/Discussion section\n6. Any limitations section\n\nBe as thorough and detailed as possible. Include specific numbers, findings, and technical details. Do NOT summarize - extract the actual content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc314169-2894-46a8-af72-b38fd3dde7f3",
  "isSidechain": false,
  "requestId": "req_011CbTMuHwqaCaKSnh3etLo1",
  "type": "assistant",
  "uuid": "ac979f33-f4bf-4fc1-a205-0c0bd3b9920d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqEWbiMxmd82f1W4cY78No",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 13846,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 13846,
          "cache_creation_input_tokens": 1109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1109
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

_source line 21 · 2026-05-27T16:07:12.391Z_

<details><summary>↩ Tool result · `toolu_01Vnw9L18BZinp1ZbefKMvFs`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac979f33-f4bf-4fc1-a205-0c0bd3b9920d",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "d72c6872-f921-45a9-b21b-6cee5c70ed39",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 7,
    "url": "https://arxiv.org/html/2412.06559v4"
  },
  "sourceToolAssistantUUID": "ac979f33-f4bf-4fc1-a205-0c0bd3b9920d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T16:07:13.339Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Exy9g6PCZAH3W7kZaF6jpe`</summary>

```json
{
  "url": "https://openreview.net/search?term=ProcessBench&venue=ACL",
  "prompt": "Find links to the OpenReview page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\". Return any URLs, review scores, or reviewer comments visible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d72c6872-f921-45a9-b21b-6cee5c70ed39",
  "isSidechain": false,
  "requestId": "req_011CbTMuHwqaCaKSnh3etLo1",
  "type": "assistant",
  "uuid": "800b8eb5-95e2-4a55-8564-d336d8124405",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqEWbiMxmd82f1W4cY78No",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 13846,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 13846,
          "cache_creation_input_tokens": 1109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1109
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "800b8eb5-95e2-4a55-8564-d336d8124405",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Tool result

_source line 25 · 2026-05-27T16:07:15.865Z_

<details><summary>↩ Tool result · `toolu_01Exy9g6PCZAH3W7kZaF6jpe`</summary>

```text
I cannot find the OpenReview page for "ProcessBench: Identifying Process Errors in Mathematical Reasoning" in the provided content.

The webpage shown is the OpenReview.net homepage, which displays navigation menus and general site information but does not contain specific paper details, URLs to individual papers, review scores, or reviewer comments for the requested paper.

To locate this paper, you would need to:
- Use the search function on OpenReview.net
- Visit the "All Venues" section to browse conference proceedings
- Access the paper directly if you have its URL
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "800b8eb5-95e2-4a55-8564-d336d8124405",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "85e59dae-5bc2-408a-94ee-5051bd60cb2e",
  "toolUseResult": {
    "bytes": 62285,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the OpenReview page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" in the provided content.\n\nThe webpage shown is the OpenReview.net homepage, which displays navigation menus and general site information but does not contain specific paper details, URLs to individual papers, review scores, or reviewer comments for the requested paper.\n\nTo locate this paper, you would need to:\n- Use the search function on OpenReview.net\n- Visit the \"All Venues\" section to browse conference proceedings\n- Access the paper directly if you have its URL",
    "durationMs": 2524,
    "url": "https://openreview.net/search?term=ProcessBench&venue=ACL"
  },
  "sourceToolAssistantUUID": "800b8eb5-95e2-4a55-8564-d336d8124405",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-27T16:07:20.080Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to get the paper content through the PDF or try a different version of the HTML URL. Also let me search for OpenReview directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85e59dae-5bc2-408a-94ee-5051bd60cb2e",
  "isSidechain": false,
  "requestId": "req_011CbTMuv5yMNeU57zBUBani",
  "type": "assistant",
  "uuid": "9501e94e-0a4b-4115-b969-55a8d12399ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mfaxoyHnQgzZmayF2P9T3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 14955,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 14955,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
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

_source line 27 · 2026-05-27T16:07:22.085Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GdNdhgftkBt42G6tfjpNoV`</summary>

```json
{
  "url": "https://arxiv.org/html/2412.06559v3",
  "prompt": "Extract the FULL content of this paper including all sections: Introduction, Method, Experiments/Results, Related Work, Conclusion, and Limitations. Be thorough - include specific numbers, model names, findings, dataset details, annotation methodology, and key tables/results. Do NOT summarize."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9501e94e-0a4b-4115-b969-55a8d12399ae",
  "isSidechain": false,
  "requestId": "req_011CbTMuv5yMNeU57zBUBani",
  "type": "assistant",
  "uuid": "15161dcb-df3b-4bae-b54b-7286a6714ff3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mfaxoyHnQgzZmayF2P9T3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 14955,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 14955,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
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

_source line 28 · 2026-05-27T16:07:22.093Z_

<details><summary>↩ Tool result · `toolu_01GdNdhgftkBt42G6tfjpNoV`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15161dcb-df3b-4bae-b54b-7286a6714ff3",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "7c5d110f-dc23-4dd3-b6ba-a63c1236cd79",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2412.06559v3"
  },
  "sourceToolAssistantUUID": "15161dcb-df3b-4bae-b54b-7286a6714ff3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-27T16:07:22.689Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BYUkSPJPFJt1j21n2VUoYt`</summary>

```json
{
  "url": "https://openreview.net/forum?id=ProcessBench",
  "prompt": "Find any reviewer comments, scores, or discussion for ProcessBench paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c5d110f-dc23-4dd3-b6ba-a63c1236cd79",
  "isSidechain": false,
  "requestId": "req_011CbTMuv5yMNeU57zBUBani",
  "type": "assistant",
  "uuid": "48a0adde-815d-432f-92b1-f687659be619",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011mfaxoyHnQgzZmayF2P9T3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 14955,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 14955,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
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

_source line 30 · 2026-05-27T16:07:25.381Z_

<details><summary>↩ Tool result · `toolu_01BYUkSPJPFJt1j21n2VUoYt`</summary>

```text
# ProcessBench Paper - Search Result

Based on the web page content provided, I cannot locate reviewer comments, scores, or discussion for the ProcessBench paper.

The page displays an error message stating: "The Note ProcessBench was not found." This indicates the paper is not currently available on the OpenReview platform, or the specific link/reference being searched does not exist in their database.

To find this paper, you might try:
- Searching directly on [OpenReview.net](/venues)
- Checking if it was submitted to a specific venue
- Verifying the exact title spelling and submission status
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48a0adde-815d-432f-92b1-f687659be619",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "6ce540c6-8d25-4f43-9f98-c26add0a6f25",
  "toolUseResult": {
    "bytes": 58581,
    "code": 200,
    "codeText": "OK",
    "result": "# ProcessBench Paper - Search Result\n\nBased on the web page content provided, I cannot locate reviewer comments, scores, or discussion for the ProcessBench paper.\n\nThe page displays an error message stating: \"The Note ProcessBench was not found.\" This indicates the paper is not currently available on the OpenReview platform, or the specific link/reference being searched does not exist in their database.\n\nTo find this paper, you might try:\n- Searching directly on [OpenReview.net](/venues)\n- Checking if it was submitted to a specific venue\n- Verifying the exact title spelling and submission status",
    "durationMs": 2690,
    "url": "https://openreview.net/forum?id=ProcessBench"
  },
  "sourceToolAssistantUUID": "48a0adde-815d-432f-92b1-f687659be619",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-27T16:07:25.384Z_

```json
{
  "parentUuid": "6ce540c6-8d25-4f43-9f98-c26add0a6f25",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f6f00ee8-226c-4dae-8dce-3143252afa48",
  "timestamp": "2026-05-27T16:07:25.384Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-27T16:07:28.865Z_

<details><summary>Logged reasoning block</summary>

```text
The arXiv HTML version isn't available. Let me try with the paper's PDF directly through a different approach, or try to find the paper on Semantic Scholar, or try to use the arxiv API.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f00ee8-226c-4dae-8dce-3143252afa48",
  "isSidechain": false,
  "requestId": "req_011CbTMvcoC3oj2Rd1dCRKfZ",
  "type": "assistant",
  "uuid": "97f39c0a-efbb-4043-b1e1-ec8110822ed6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gBhrxcmEnDfNPSxkRDUk9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 15569,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 615,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 15569,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 615
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

_source line 33 · 2026-05-27T16:07:32.234Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UYNTMPEFgEWfBLBkDbbE3U`</summary>

```json
{
  "url": "https://www.arxiv.org/pdf/2412.06559",
  "prompt": "Extract the complete content of this paper including all sections. Focus especially on:\n1. Introduction - what gap they identified, motivation\n2. Dataset construction methodology - how they collected problems, generated solutions, annotation process\n3. Experiments - which PRMs and critic models were evaluated, key results and numbers\n4. Analysis and findings - what patterns they discovered\n5. Related work \n6. Conclusion and limitations\nBe comprehensive and include specific numbers, percentages, model names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97f39c0a-efbb-4043-b1e1-ec8110822ed6",
  "isSidechain": false,
  "requestId": "req_011CbTMvcoC3oj2Rd1dCRKfZ",
  "type": "assistant",
  "uuid": "46ad2c57-5d31-428b-9a2a-a73e76971fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gBhrxcmEnDfNPSxkRDUk9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 15569,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 615,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 15569,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 615
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

_source line 34 · 2026-05-27T16:07:33.457Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JLaPNUPbKr3rUPydFkfJVF`</summary>

```json
{
  "url": "https://huggingface.co/papers/2412.06559",
  "prompt": "Extract all available information about the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" including any discussion, comments, or detailed description available on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46ad2c57-5d31-428b-9a2a-a73e76971fc4",
  "isSidechain": false,
  "requestId": "req_011CbTMvcoC3oj2Rd1dCRKfZ",
  "type": "assistant",
  "uuid": "524833aa-b536-43e4-a54c-efcdcc34c575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gBhrxcmEnDfNPSxkRDUk9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 15569,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 615,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 15569,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 615
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

_source line 35 · 2026-05-27T16:07:34.215Z_

<details><summary>↩ Tool result · `toolu_01JLaPNUPbKr3rUPydFkfJVF`</summary>

```text
&lt;persisted-output>
Output too large (65.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/toolu_01JLaPNUPbKr3rUPydFkfJVF.txt

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
  "parentUuid": "524833aa-b536-43e4-a54c-efcdcc34c575",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "188c6a99-a16f-4710-acd2-885f93266800",
  "toolUseResult": {
    "bytes": 67553,
    "code": 200,
    "codeText": "OK",
    "result": "# PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning\n\nChujie Zheng\\* Zhenru Zhang Beichen Zhang Runji Lin Keming Lu  \nBowen Yu\\* Dayiheng Liu\\* Jingren Zhou Junyang Lin\\*\n\nQwen Team, Alibaba Inc.\n\n&lt;https://huggingface.co/datasets/Qwen/ProcessBench>\n\n&lt;https://github.com/QwenLM/ProcessBench>\n\n## Abstract\n\nAs language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models (PRMs)* and *critic models*, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope PROCESSBENCH can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.\n\nFigure 1: Overview of evaluation results on PROCESSBENCH (see Table 3 for details).\n\n\\*Corresponding authors.# 1 Introduction\n\nIn recent years, language models have made remarkable progress in complex reasoning tasks, such as mathematics and programming (Hurst et al., 2024; OpenAI, 2024; Yang et al., 2024a,b; Dubey et al., 2024; Wake et al., 2024), yet they still make mistakes when solving challenging problems. To achieve scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024), i.e., effectively supervising AI systems that get close to or go beyond broadly human-level performance, particularly in complex tasks that are difficult for general humans, we expect language models can identify errors in their reasoning process in an automated way. However, existing benchmarks related to assessing language models' reasoning process may be hard to satisfy the growing evaluation demand for the error identification ability. Either their covered problems have become less challenging for recent language models (Zhou et al., 2024; Lightman et al., 2023), or they merely label the correctness of final answers but lack annotations for specific erroneous steps (Lin et al., 2024).\n\n```\n\"id\": \"math-22\",\n\"generator\": \"Qwen2-7B-Instruct\",\n\"problem\": \"Find the integer $n, $ 0 \\le n \\le 180, $ such that $ \\cos n^\\circ = \\cos 568^\\circ.\",\n\"steps\": [\n  \"To find the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\), we can use the periodic properties of the cosine function. First, recall that the cosine function has a period of \\(\\(360^\\circ\\)\\). This means that: \\(\\[\\ \\cos \\ \\theta = \\cos (\\theta + 360k) \\]\\) for any integer \\(\\(k\\)\\).\",\n  \"Given \\(\\(\\cos 568^\\circ\\)\\), we need to reduce this angle to an equivalent angle within the first cycle of \\(\\(0\\)\\) to \\(\\(360^\\circ\\)\\). We do this by subtracting multiples of \\(\\(360^\\circ\\)\\) until we get an angle within this range: \\(\\[\\ 568^\\circ - 360^\\circ = 208^\\circ \\]\\) So, \\(\\(\\cos 568^\\circ = \\cos 208^\\circ\\)\\).\",\n  \"However, we want to find \\(\\(n\\)\\) such that \\(\\(0 \\le n \\le 180\\)\\). Since cosine is also symmetric about \\(\\(180^\\circ\\)\\), we know that: \\(\\[\\ \\cos \\ \\theta = \\cos (180^\\circ - \\theta) \\]\\) Therefore, \\(\\(\\cos 208^\\circ = \\cos (180^\\circ - 208^\\circ)\\)\\), which simplifies to: \\(\\[\\ \\cos 208^\\circ = \\cos (-28^\\circ) \\]\\)\",\n  \"The cosine function is also even, meaning it is symmetric about the y-axis: \\(\\[\\ \\cos (-\\theta) = \\cos \\theta \\]\\) Thus, \\(\\[\\ \\cos (-28^\\circ) = \\cos 28^\\circ \\]\\)\",\n  \"So, \\(\\(n = 28^\\circ\\)\\). Hence, the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\) is \\(\\(n = 28\\)\\). The answer is \\(\\(\\boxed{28}\\)\\).\",\n],\n\"final_answer_correct\": false,\n\"label\": 2\n```\n\nFigure 2: Data example of PROCESSBENCH. The label 2 denotes that the earliest error occurs in the **2nd step** (indexed from 0). For test cases with no errors, the labels are  $-1$ .\n\nIn this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. Figure 2 presents a data example. We prioritize several principles when designing this benchmark:\n\n- • **Problem difficulty and solution diversity.** PROCESSBENCH primarily covers competition- and Olympiad-level math problems and utilizes various open-source language models to generate solutions. This ensures both the difficulty of math problems and the diversity of solution styles, enabling robust evaluation.\n- • **Scale and accuracy.** PROCESSBENCH consists of 3,400 test cases, with all solutions annotated with error locations by multiple human experts. The large scale and expert annotation ensure the data quality and the reliability of evaluation.\n- • **Simplicity.** PROCESSBENCH requires models to identify the earliest erroneous step occurring in the solution, if any exists. This straightforward evaluation protocol enables easy adaptation for various types of models, such as process reward models (PRMs) and critic models.\n\nWe conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models* (PRMs) and *critic models*. For PRMs, we include multiple open-source PRMs (Wang et al., 2024; Skywork, 2024; Xiong et al., 2024b) to assess the correctness of each reasoning step in the solution. For critic models, we prompt general language models like Qwen (Yang et al., 2024a; Qwen, 2024a; Hui et al., 2024) and GPT-4o (Hurst et al., 2024) to critique each solution step by step. We show that, despiterecent growing interest, existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset, which raises questions about the generalization abilities and scalability of the current data synthesis methodologies used to build PRMs. In contrast, general language models manifest non-trivial critique capabilities that can not only identify erroneous steps but also provide detailed explanations. The best open-source model, QwQ-32B-Preview (Qwen, 2024b), has performed competitively with the proprietary GPT-4o model, while it still lags behind the reasoning-specialized o1-mini (OpenAI, 2024). We hope PROCESSBENCH can catalyze future research in automated reasoning process assessment, establishing crucial foundations for scalable oversight of language models.\n\n## 2 Related Work\n\nThere exist several benchmarks or datasets related to assessing language models’ reasoning process. CriticBench (Lin et al., 2024) evaluates language models’ abilities to critique solutions and correct mistakes in various reasoning tasks. MathCheck (Zhou et al., 2024) synthesizes solutions containing erroneous steps using the GSM8K dataset (Cobbe et al., 2021), in which language models are tasked with judging the correctness of final answers or reasoning steps. PRM800K (Lightman et al., 2023) builds on the MATH problems (Hendrycks et al., 2021) and annotates the correctness and soundness of reasoning steps in model-generated solutions. It also has sparked a blooming of research interest in building process reward models (PRMs) (Wang et al., 2024; Xiong et al., 2024b;a).\n\nTable 1: Comparison between PROCESSBENCH and other benchmarks or datasets related to reasoning process assessment (Lin et al., 2024; Zhou et al., 2024; Lightman et al., 2023). &lt;sup>†&lt;/sup>: Solution diversity denotes the diversity of language models used for solution generation, corresponding to the “# Solution Generators” column. &lt;sup>‡&lt;/sup>: For PRM800K, we only count the 90 complete solutions in its phase 1 test set, as the complete solutions in its phase 2 test set are all terminated at the earliest erroneous steps.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>Problem Difficulty&lt;/th>\n&lt;th># Solution Generators&lt;/th>\n&lt;th>Solution Diversity&lt;sup>†&lt;/sup>&lt;/th>\n&lt;th>Step Annotation?&lt;/th>\n&lt;th>Annotator&lt;/th>\n&lt;th>Test Case Size (Identifying Process Errors)&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathCheck-GSM&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>516&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PRM800K&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>90&lt;sup>‡&lt;/sup>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PROCESSBENCH&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>3,400&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nPROCESSBENCH is distinguished from prior benchmarks or datasets in three key aspects, as highlighted in Table 1. **First**, PROCESSBENCH primarily covers more challenging math problems with competition- or Olympiad-level difficulty, which better fit the rapidly growing capabilities of modern language models. **Second**, rather than relying on synthetic data, PROCESSBENCH leverages diverse model-generated natural solutions and employs expert annotation to label erroneous steps, which ensures both real-world applicability and label accuracy. **Third**, the large scale of PROCESSBENCH (3,400 test cases in total) enables more comprehensive and robust evaluation.\n\nThere has also been extensive research on language models’ scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024) and studies on whether language models can identify the errors in their own outputs. Lightman et al. (2023); Wang et al. (2024); Luo et al. (2024) propose to train specialized reward models to supervise language models’ reasoning process (i.e., process reward models or PRMs). Huang et al. (2023); Kamoi et al. (2024) argue that general language models struggle to identify and correct their reasoning errors without external feedback. Saunders et al. (2022); McAleese et al. (2024) show that language models can be trained to write informative critiques for both assisting human evaluation and enabling self-refinement, which favorably scales with increased model capabilities (or model sizes). We believe the improved capabilities of error identification will build strong foundations for language models’ scalable oversight.\n\n## 3 Benchmark Construction\n\n### 3.1 Task Definition\n\nAs shown in Figure 2, given a math problem and a step-by-step solution, PROCESSBENCH requires models to either identify the *earliest-occurring error*, or conclude that all steps are *correct*. Formally,---\n\ngiven a math problem  $P$  and its step-by-step solution  $S = \\{s_0, \\dots, s_{n-1}\\}$ , the task is to output an index  $i \\in \\{-1, 0, \\dots, n-1\\}$ , where  $i = -1$  indicates that all steps are correct, and  $i \\geq 0$  indicates that the earliest error occurs at step  $s_i$ .\n\nTypically but non-inclusively, we consider a step as erroneous if it contains any of the following: (1) **Mathematical errors**: incorrect calculations, algebraic manipulations, or formula applications. (2) **Logical errors**: invalid deductions, unwarranted assumptions, or flawed reasoning steps. (3) **Conceptual errors**: misunderstanding or misapplication of mathematical or problem concepts. (4) **Completeness errors**: missing crucial conditions, constraints, or necessary justifications that affect the solution’s validity. Beyond these types of errors, we encourage human annotators to determine the correctness of reasoning steps based on their own expertise. We do not require human annotators to explicitly annotate error types due to the intractability of intentional categorization.\n\nNote that for steps after the first error, the meaning of their correctness may become ambiguous or debatable: derivations based on incorrect premises can make sense, but still remain on a globally incorrect reasoning path (Lightman et al., 2023). For instance, if step  $k$  contains an error in calculating  $x = 2$ , when it should be  $x = 3$ , subsequent steps may follow valid algebraic rules but operate on an incorrect value of  $x$ , making their individual correctness hard to determine. This is why PROCESSBENCH focuses on identifying the earliest-occurring error in the reasoning process.\n\n### 3.2 Data Collection\n\n**Problem Curation** We collect math problems from the test sets of four public and widely used datasets in mathematical reasoning tasks: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), Olympiad-Bench (He et al., 2024), and Omni-MATH (Gao et al., 2024). Except for GSM8K, which consists of grade school math problems, the other three datasets all contain problems with competition- or Olympiad-level difficulty.\n\n**Solution Generation** We generate solutions using the widely used Qwen (Yang et al., 2024a; Qwen, 2024a; Yang et al., 2024b) and LLaMA (Dubey et al., 2024) series open-source models, resulting in twelve distinct solution generators in total. This includes a wide range of model families, sizes, and downstream task performance, leading to the high diversity of solution styles. Table 4 in Appendix B presents the breakdown of language models used for PROCESSBENCH’s solution generation.\n\n**Solution Reformattng** In mathematical reasoning tasks, double line breaks (i.e., “\\n\\n”) are commonly used to segment solution steps (or paragraphs). However, we observed inconsistent step granularity due to varying solution styles and generation randomness. Some generated solutions frequently used double line breaks, resulting in numerous short, logically incomplete steps, while others used them sparingly, leading to lengthy paragraphs that combine multiple logical components. Such inconsistency in step granularity (and potential improper step segmentation) would impede the standardization of human annotation criteria.\n\nTo address this issue, we adopt a *solution reformattng* method to standardize the step granularity, through which the segmented paragraphs can better correspond to logically complete and progressive reasoning steps. Specifically, we first replace all the line breaks with white space, and then ask Qwen2.5-72B-Instruct to insert double line breaks (i.e., segment paragraphs) while preserving the solution content. Since we found that Qwen2.5-72B-Instruct sometimes alters the solution content ( $< 0.5\\%$ ), we remove those solutions whose final answers change after reformattng (although the content alteration may not influence benchmark construction). Consequently, the reformattng method effectively unifies the step granularity. Figure 6 in Appendix A presents an example of solution reformattng.\n\n**Expert Annotation** To ensure a balance between erroneous and correct solutions, we first use Qwen2.5-72B-Instruct to verify the correctness of final answers in the model-generated solutions against the reference answers. We then respectively sample solutions with correct or incorrect final answers for subsequent annotation in a balanced way to avoid excessive concentration on solutions from either the weakest or strongest models.\n\nWe recruit human experts with doctoral-level mathematical expertise for annotation, and all of them are required to pass the mandatory proficiency examination and annotation tutorial. The annotators are designated with the same task in § 3.1, i.e., identifying the earliest-occurring error in each solution. However, we notice that the competition- or Olympiad-level math problems can still be challenging even for doctoral students majoring in mathematics. According to the feedback from the annotators, although they were not required to solve problems from scratch but rather to identify erroneous steps in presented solutions, they would still become quite hesitant in their annotations when uncertain about the correct solution approach, which affected both the annotation speed and quality. To ease the annotation difficulty,we provide annotators with the reference solutions and answers from the original datasets, while we still explicitly instructed them to inspect and verify the presented model-generated solutions step by step.\n\nEach solution is initially assigned to three different experts. When the initial three annotators cannot reach consensus, we increase the number of annotators until three of them agree on the same result. If an agreement cannot be achieved within five annotators (e.g., annotation distribution of (2, 2, 1) or (2, 1, 1, 1)), we discard this solution. This leads to an overall  $\\sim 30\\%$  discard rate throughout the entire annotation process. We also discard the solutions where the final answers are incorrect (according to the reference answers) but the human annotation results are correct. Although such cases are fairly rare ( $< 1\\%$ ), they are mostly concentrated in the OlympiadBench and Omni-MATH problems (i.e., Olympiad-level ones). The agreement statistics in Table 2 further evidence that the more challenging problems usually need more annotators to achieve the annotation agreement, particularly for those samples with incorrect final answers. These results suggest the inherent challenge of our human annotation task.\n\n### 3.3 Statistics\n\nTable 2: Statistics of PROCESSBENCH. “% Process errors” denotes the proportion of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. “%  $\\geq n$  steps” denotes the proportion of samples whose solutions have  $\\geq n$  steps (split by double line breaks). “% 3/ $n$  agreement” denotes the proportion of samples where the three-annotator agreement is achieved within  $n$  annotators, so  $(\\% 3/3) + (\\% 3/4) + (\\% 3/5) = 100\\%$ .\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td># Samples&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% Process errors&lt;br/>(correct final answers)&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{200-193}{200} = 3.5\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-406}{500} = 18.8\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-339}{500} = 32.2\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-241}{500} = 51.8\\%&lt;/math>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td># Steps&lt;/td>\n&lt;td>5.3&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>6.8&lt;/td>\n&lt;td>6.0&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>8.6&lt;/td>\n&lt;td>7.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 5&lt;/math> steps&lt;/td>\n&lt;td>61.8%&lt;/td>\n&lt;td>57.5%&lt;/td>\n&lt;td>73.6%&lt;/td>\n&lt;td>70.4%&lt;/td>\n&lt;td>92.6%&lt;/td>\n&lt;td>92.3%&lt;/td>\n&lt;td>92.5%&lt;/td>\n&lt;td>81.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 10&lt;/math> steps&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>1.6%&lt;/td>\n&lt;td>17.8%&lt;/td>\n&lt;td>8.9%&lt;/td>\n&lt;td>33.9%&lt;/td>\n&lt;td>27.1%&lt;/td>\n&lt;td>29.2%&lt;/td>\n&lt;td>21.6%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 15&lt;/math> steps&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>0.0%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>2.0%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>8.8%&lt;/td>\n&lt;td>7.5%&lt;/td>\n&lt;td>4.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/3 agreement&lt;/td>\n&lt;td>66.7%&lt;/td>\n&lt;td>95.9%&lt;/td>\n&lt;td>59.4%&lt;/td>\n&lt;td>91.9%&lt;/td>\n&lt;td>52.8%&lt;/td>\n&lt;td>85.0%&lt;/td>\n&lt;td>47.8%&lt;/td>\n&lt;td>80.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/4 agreement&lt;/td>\n&lt;td>21.3%&lt;/td>\n&lt;td>3.6%&lt;/td>\n&lt;td>24.4%&lt;/td>\n&lt;td>4.7%&lt;/td>\n&lt;td>24.1%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>25.6%&lt;/td>\n&lt;td>13.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/5 agreement&lt;/td>\n&lt;td>12.1%&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>16.2%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>23.1%&lt;/td>\n&lt;td>5.9%&lt;/td>\n&lt;td>26.6%&lt;/td>\n&lt;td>6.2%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe resulting PROCESSBENCH has four subsets, consisting of 3,400 test cases in total. The detailed statistics are shown in Table 2 and Table 4 (in Appendix B), and we also plot in Figure 3 the distribution of error positions in erroneous samples. In general, the more challenging the problems, the more solution steps the models generate, and incorrect solutions usually contain more steps than correct ones. However, across all four subsets, a large proportion of errors occur in the earlier steps, such as steps 0-3 in GSM8K and MATH, and steps 1-5 in OlympiadBench and Omni-MATH.\n\nFigure 3: Distribution of error positions (indexed from 0; truncated to 16 for better visualization), corresponding to the *label* field as shown in Figure 2.\n\nIt is noteworthy that while we have intentionally controlled an equal number of solutions with incorrect and correct final answers (200 each for GSM8K and 500 each for other subsets), the annotationFigure 4: Process error ratios per models and subsets, computed as the proportions of samples annotated as *erroneous* among all the samples with *correct final answers* (same as in Table 2). The models used for solution generation slightly vary across different subsets, see Table 4 in Appendix B. We observe that no particular models have notably higher process error rates, while **the process error rates are consistently higher on more difficult problems for all the models.**\n\nresults reveal quite different numbers. Specifically, in the more challenging subsets like OlympiadBench and Omni-MATH, a larger proportion of solutions with correct final answers still contain erroneous steps. For instance, in OlympiadBench,  $\\frac{500-339}{500} = 32.2\\%$  of solutions with correct final answers are found to contain process errors, while in Omni-MATH this proportion is even higher ( $\\frac{500-241}{500} = 51.8\\%$ ). In contrast, these proportions in GSM8K and MATH are  $\\frac{200-193}{200} = 3.5\\%$  and  $\\frac{500-406}{500} = 18.8\\%$ , respectively. In Figure 4, for each model used for solution generation, we plot the ratio of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. We observe that the process error rates are consistently higher on more difficult problems. To our knowledge, our work is **the first to present evidence that on more challenging math problems, current language models are more prone to making process errors even when reaching correct final answers.** This also suggests the underlying limitation of rule-based RL in mathematical reasoning (i.e., rewarding merely according to the correctness of final answers) and further highlights the significance of identifying errors in the reasoning process.\n\n## 4 Evaluation\n\n### 4.1 Setup\n\nFor each subset of PROCESSBENCH, we calculate the accuracies on erroneous and correct samples, respectively, and additionally compute their harmonic mean as the **F1 score**. We primarily refer to F1 scores to compare model performance, as it balances model behaviors between being overly critical and being incapable of identifying errors.\n\nWe consider two types of models in the evaluation on PROCESSBENCH: *process reward models (PRMs)* and *critic models*.\n\n**Process Reward Models (PRMs)** As a recently focal topic, PRMs are proposed to assess and supervise the intermediate steps in language models’ reasoning process (Lightman et al., 2023), thus naturally falling in the scope of our research. In practice, PRMs are typically trained using the process labels for intermediate reasoning steps, outputting either the correctness prediction or a scalar score for each reasoning step during inference. Previous research usually evaluates PRMs based on their improvement in the Best-of-N (BoN) performance of another language model that generates solutions. However, this lacks a finer-grained inspection on their process assessment abilities, and the evaluation reliability can be heavily affected by the underlying solution generation model.\n\nOur evaluation includes several open-source PRMs: (1) Math-Shepherd (Wang et al., 2024), which obtains the process label for each step via estimating the empirical probability of this step leading to the correct final answer. (2) Two LLaMA-3.1-based PRMs from Xiong et al. (2024b), which roughly follow the training methodology of Math-Shepherd but differ in the solution generation models and optimization objectives. (3) Two Qwen2.5-Math-based PRMs recently released by Skywork (2024). (4) We also train a PRM by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K dataset, namely Qwen2.5-Math-7B-PRM800K. See Appendix C for its training details.For the (1)(2)(4) PRMs, we extract the earliest erroneous step from their correctness predictions for reasoning steps. For the (3) PRMs, which produce scalar scores for each reasoning step, we first transform these scores into binary correctness predictions (using a threshold above which steps are considered as correct), and then extract the earliest erroneous step as we do for (1)(2)(4). The transformation threshold is determined as the one giving the highest F1 score on the GSM8K subset.\n\n**Critic Models** Critic models aim to provide feedback and critique to model-generated texts, non-inclusively including verification, reflection, and correction or refinement. They have demonstrated promising utility in achieving scalable oversight (Saunders et al., 2022; McAleese et al., 2024).\n\nTraining critic models for specific domains typically requires significant and specialized effort, which is out of the scope of our work. Instead, we are more interested in the critique capabilities of *general language models*. The task definition (§ 3.1) of PROCESSBENCH enables us to apply simple prompt engineering to repurpose general language models as critic models. We show in Figure 7 in Appendix E the prompt template we implement for our evaluation. Specifically, models are prompted to return the index of the paragraph where the earliest error occurs as the *final answer*, similar to the conventional evaluation protocol for mathematical reasoning tasks (Cobbe et al., 2021; Hendrycks et al., 2021; Yang et al., 2024b).\n\nOur evaluation includes the widely-used Qwen2 (Yang et al., 2024a), Qwen2.5 (Qwen, 2024a), Qwen2.5-Math (Yang et al., 2024b), Qwen2.5-Coder (Hui et al., 2024), and LLaMA-3 (Dubey et al., 2024) series open-source models, as well as the recently released QwQ-32B-Preview reasoning model (Qwen, 2024b). We also evaluate the proprietary GPT-4o (Hurst et al., 2024) and o1-mini (OpenAI, 2024) models. We report the performance of open-source models under majority voting over eight samplings, while we also report their performance under greedy decoding in Table 9 in Appendix F. For the proprietary model GPT-4o, we report the results under greedy decoding, while for o1-mini, we report the results under single sampling as its API does not support customized decoding parameters.\n\nTable 3: Evaluation results on PROCESSBENCH. We report the F1 score of the respective accuracies on erroneous and correct samples. See Table 5 and Table 7 for breakdown of evaluation results.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad-Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>68.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>56.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>★ QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>71.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Alright, I've got this math problem to solve and a solution provided, but I need to review it paragraph by paragraph to find any errors. The problem is to find the integer  $n$ , where  $0 \\leq n \\leq 180$ , such that  $\\cos n^\\circ = \\cos 568^\\circ$ . Let's dive into the solution step by step.\n\n**Paragraph 0:\\*\\***\n\nThe solution starts by recalling that the cosine function has a period of  $360^\\circ$ , which means  $\\cos \\theta = \\cos (\\theta + 360k)$  for any integer  $k$ . That's correct. Cosine repeats every  $360^\\circ$ , so adding or subtracting multiples of  $360^\\circ$  doesn't change the value of the cosine.\n\n**Paragraph 1:\\*\\***\n\nGiven  $\\cos 568^\\circ$ , the solution reduces this angle by subtracting  $360^\\circ$  to get  $208^\\circ$ , since  $568^\\circ - 360^\\circ = 208^\\circ$ . So,  $\\cos 568^\\circ = \\cos 208^\\circ$ . That seems right.  $208^\\circ$  is within one cycle of  $0^\\circ$  to  $360^\\circ$ .\n\n**Paragraph 2:\\*\\***\n\nNow, the solution mentions that cosine is symmetric about  $180^\\circ$ , and states that  $\\cos \\theta = \\cos (180^\\circ - \\theta)$ . Wait a minute, is that correct? Let me think about this. Actually, cosine is symmetric about the y-axis, and the identity  $\\cos \\theta = \\cos (-\\theta)$  reflects that. The identity  $\\cos \\theta = \\cos (360^\\circ - \\theta)$  shows the symmetry about  $360^\\circ$ , but symmetry about  $180^\\circ$  isn't directly related to cosine's even property.\n\nHmm, maybe I need to recall some trigonometric identities here. Let's see, the cosine of an angle in standard position is equal to the cosine of its reference angle, but with a sign depending on the quadrant.  $208^\\circ$  is in the third quadrant, where cosine is negative.\n\nAlternatively, there's the identity  $\\cos (180^\\circ + \\theta) = -\\cos \\theta$ , but that's not directly applicable here.\n\nLet me double-check the symmetry properties. Cosine is an even function, meaning  $\\cos (-\\theta) = \\cos \\theta$ , which shows symmetry about the y-axis. The identity  $\\cos (360^\\circ - \\theta) = \\cos \\theta$  shows symmetry every full cycle.\n\nBut the statement  $\\cos \\theta = \\cos (180^\\circ - \\theta)$  isn't generally true. Let's test it with a specific angle. For example,  $\\theta = 30^\\circ$ :  $\\cos 30^\\circ = \\sqrt{3}/2$ , and  $\\cos (180^\\circ - 30^\\circ) = \\cos 150^\\circ = -\\sqrt{3}/2$ . These are not equal; in fact, they're negatives of each other.\n\nSo, it seems there's an error in this paragraph. The correct identity involving  $180^\\circ$  is  $\\cos (180^\\circ - \\theta) = -\\cos \\theta$ , not  $\\cos \\theta$ .\n\nTherefore, the earliest error occurs in paragraph 2.\n\n**Final Answer:**\n\n$\\boxed{2}$\n\nFigure 5: Critique generated by QwQ-32B-Preview for the test case in Figure 2.\n\n## 4.2 Results\n\nWe present the evaluation results in Table 3. Our observations are summarized as follows:\n\n**Generalization Across Difficulty** From GSM8K and MATH to OlympiadBench and Omni-MATH, with the increased difficulty of math problems, we observe a consistent performance decline for all the models, which suggests the common challenge of both PRMs and critic models in generalization abilities.\n\n**Comparison Between PRMs and Critic Models** We find that existing PRMs typically underperform the top prompt-driven critic models even on the simpler GSM8K and MATH subsets, suggesting that these PRMs struggle to indicate the correctness of the intermediate steps in mathematical reasoning. Moreover, when moving toward the more challenging OlympiadBench and Omni-MATH subsets, PRMs suffer from a more notable performance decline than critic models. This raises our concerns about the **generalization abilities and scalability of the current data synthesis methodologies used to build PRMs**. More specifically, current methodologies, as exemplified by Math-Shepherd (Wang et al., 2024), measure the correctness of an intermediate step by estimating the empirical probability of this step leading to the correct final answer. This kind of approach has two intuitive major issues: (1) The process labels heavily depend on the language model used to generate solutions (i.e., highly “on-policy”), which---\n\nwould naturally fail to indicate the correctness of reasoning steps generated by other models. (2) As demonstrated in § 3.3, current language models are prone to making process errors even when reaching correct final answers. This could substantially invalidate the estimated process labels, particularly on the more challenging math problems. In contrast, **Qwen2.5-Math-7B-PRM800K**, which is straightforwardly fine-tuned on the *fully human-annotated* PRM800K training set, exhibits significantly stronger performance and generalization ability than other PRMs.\n\n**Comparison Among Critic Models** Compared to PRMs, critic models can benefit from separate reasoning processes when critiquing solutions, as they can “think” more before indicating the correctness of each solution step, which leads to their better performance in this error identification task. Within the same model family, the error identification performance favorably scales with increased model sizes. Notably, the recently released reasoning model **QwQ-32B-Preview** **performs best among the open-source models and is highly competitive with GPT-4o**. It is noteworthy that QwQ-32B-Preview achieves more *balanced accuracies on erroneous and correct samples* (see Table 5 and 7 in Appendix F). We show in Figure 5 an example of critique generated by QwQ-32B-Preview to the test case in Figure 2, which not only identifies the erroneous step but also provides the detailed thinking process and explanation. Nevertheless, QwQ-32B-Preview still lags behind o1-mini, suggesting that although the gap in problem-solving performance is getting closer between open-source and proprietary models, there still exists another large gap in their critique capabilities.\n\n## 5 Conclusion\n\nWe introduce the PROCESSBENCH benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, characterized by its high problem difficulty and solution diversity, large scale, rigorous human annotation, and simple evaluation protocol. Through extensive evaluation with existing process reward models (PRMs) and prompt-driven critic models, we draw two main observations: (1) Existing PRMs typically underperform critic models in identifying erroneous reasoning steps, and struggle more to generalize to challenging math problems. (2) Open-source language models, as exemplified by QwQ-32B-Preview, have demonstrated critique capabilities competitive with the proprietary model GPT-4o, yet still lag behind the reasoning-specialized o1-mini model. We envision PROCESSBENCH as a cornerstone testbed for advancing automated reasoning process assessment, a critical step toward achieving scalable oversight of language models.\n\n**Limitations** Despite our best efforts throughout the entire benchmark construction process (§ 3.2), PROCESSBENCH may still contain inaccurate labels of error locations, particularly for the more challenging Olympiad-level math problems. Additionally, the solutions discarded in human annotation (§ 3.2) may involve the particularly challenging problems, which could bias the problem distribution in PROCESSBENCH, although such samples may have exceeded the capabilities of the human annotators in our annotation task.\n\n## References\n\nDario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. *arXiv preprint arXiv:1606.06565*, 2016.\n\nSamuel R Bowman, Jeeyoon Hyun, Ethan Perez, Edwin Chen, Craig Pettit, Scott Heiner, Kamilę Lukošūtė, Amanda Askell, Andy Jones, Anna Chen, et al. Measuring progress on scalable oversight for large language models. *arXiv preprint arXiv:2211.03540*, 2022.\n\nBoxi Cao, Keming Lu, Xinyu Lu, Jiawei Chen, Mengjie Ren, Hao Xiang, Peilin Liu, Yaojie Lu, Ben He, Xianpei Han, et al. Towards scalable automated alignment of llms: A survey. *arXiv preprint arXiv:2406.01252*, 2024.\n\nKarl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n\nAbhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.\n\nBofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. *arXiv preprint arXiv:2410.07985*, 2024.---\n\nChaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n\nJie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. *arXiv preprint arXiv:2310.01798*, 2023.\n\nBinyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, et al. Qwen2.5-coder technical report. *arXiv preprint arXiv:2409.12186*, 2024.\n\nAaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.\n\nRyo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. When can LLMs actually correct their own mistakes? a critical survey of self-correction of LLMs. *Transactions of the Association for Computational Linguistics*, 12:1417–1440, 2024. doi: 10.1162/tacl.a\\_00713. URL &lt;https://aclanthology.org/2024.tacl-1.78>.\n\nWoosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the 29th Symposium on Operating Systems Principles*, pages 611–626, 2023.\n\nHunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. *arXiv preprint arXiv:2305.20050*, 2023.\n\nZicheng Lin, Zhibin Gou, Tian Liang, Ruilin Luo, Haowei Liu, and Yujiu Yang. Criticbench: Benchmarking llms for critique-correct reasoning. *arXiv preprint arXiv:2402.14809*, 2024.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nNat McAleese, Rai Michael Pokorny, Juan Felipe Ceron Uribe, Evgenia Nitishinskaya, Maja Trebacz, and Jan Leike. Llm critics help catch llm bugs. *arXiv preprint arXiv:2407.00215*, 2024.\n\nOpenAI. Openai o1-mini: Advancing cost-efficient reasoning, 2024. URL &lt;https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/>.\n\nTeam Qwen. Qwen2.5: A party of foundation models, September 2024a. URL &lt;https://qwenlm.github.io/blog/qwen2.5/>.\n\nTeam Qwen. Qwq: Reflect deeply on the boundaries of the unknown, November 2024b. URL &lt;https://qwenlm.github.io/blog/qwq-32b-preview/>.\n\nWilliam Saunders, Catherine Yeh, Jeff Wu, Steven Bills, Long Ouyang, Jonathan Ward, and Jan Leike. Self-critiquing models for assisting human evaluators. *arXiv preprint arXiv:2206.05802*, 2022.\n\no1 Team Skywork. Skywork-o1 open series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nAlan Wake, Albert Wang, Bei Chen, CX Lv, Chao Li, Chengen Huang, Chenglin Cai, Chujie Zheng, Daniel Cooper, Ethan Dai, et al. Yi-lightning technical report. *arXiv preprint arXiv:2412.01253*, 2024.\n\nPeiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, August 2024. doi: 10.18653/v1/2024.acl-long.510. URL &lt;https://aclanthology.org/2024.acl-long.510>.\n\nWei Xiong, Chengshuai Shi, Jiaming Shen, Aviv Rosenberg, Zhen Qin, Daniele Calandriello, Misha Khalman, Rishabh Joshi, Bilal Piot, Mohammad Saleh, et al. Building math agents with multi-turn iterative preference learning. *arXiv preprint arXiv:2409.02392*, 2024a.---\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An implementation of generative prm. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024b.\n\nAn Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. *arXiv preprint arXiv:2407.10671*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nZihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F Wong, Xiaowei Huang, Qifeng Wang, and Kaizhu Huang. Is your model really a good math reasoner? evaluating mathematical reasoning with checklist. *arXiv preprint arXiv:2407.08733*, 2024.## A Example of Solution Reformattting\n\n&lt;table border=\"1\">\n&lt;tr>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form&lt;/p>\n&lt;math display=\"block\">\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1,&lt;/math>\n&lt;p>where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length.&lt;/p>\n&lt;p>In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>.&lt;/p>\n&lt;p>First, we calculate the distance from the center to each focus:&lt;/p>\n&lt;math display=\"block\">\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4.&lt;/math>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse.&lt;/p>\n&lt;p>Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;td style=\"vertical-align: middle; text-align: center; padding: 0 10px;\">\n&lt;/td>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form &lt;math>\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1&lt;/math>, where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length. In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>. First, we calculate the distance from the center to each focus: &lt;math>\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4&lt;/math>.&lt;/p>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse. Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>. The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;/tr>\n&lt;/table>\n\nFigure 6: Example of solution reformattting. The left is the original solution (generated by Qwen2-7B-Instruct) and the right is the reformatted one. The problem, coming from the MATH test set, is “The ellipse  $\\frac{(x-6)^2}{25} + \\frac{(y-3)^2}{9} = 1$  has two foci. Find the one with the larger  $x$ -coordinate. Enter your answer as an ordered pair, like  $(2, 1)$ .”\n\n## B Breakdown Statistics of PROCESSBENCH\n\nTable 4: Breakdown statistics of PROCESSBENCH.  $^\\dagger$ : We encountered a code bug when using Llama-3.1-70B-Instruct and Qwen2.5-72B-Instruct to generate solutions for the MATH problems, thus their counts are all zero in the MATH subset of PROCESSBENCH.  $^\\ddagger$ : For the more challenging OlympiadBench and Omni-MATH problems, we exclude models with lower accuracies from subsequent annotation.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Generator&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;math>^\\dagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>13&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>16&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>23&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>53&lt;/td>\n&lt;td>116&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>131&lt;/td>\n&lt;td>31&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>28&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>85&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>19&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-1.5B-Instruct&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>36&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>89&lt;/td>\n&lt;td>42&lt;/td>\n&lt;td>63&lt;/td>\n&lt;td>45&lt;/td>\n&lt;td>96&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>9&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>51&lt;/td>\n&lt;td>64&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>71&lt;/td>\n&lt;td>25&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-1.5B-Instruct&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>10&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>62&lt;/td>\n&lt;td>35&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>75&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>2&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>67&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>88&lt;/td>\n&lt;td>38&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>47&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>99&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>18&lt;/td>\n&lt;td>39&lt;/td>\n&lt;td>59&lt;/td>\n&lt;td>81&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Total&lt;/td>\n&lt;td colspan=\"2\">400&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>## C Training Details of Qwen2.5-Math-7B-PRM800K\n\nQwen2.5-Math-7B-PRM800K is obtained by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K training set. We replace the original language modeling head with a new reward modeling head that outputs binary classification logits. The classification loss is computed at the second line break positions in all the “\\n\\n”. We treat the original 1 and 0 labels in PRM800K as our positive labels, while -1 as negative ones. To eliminate test data contamination, we also remove the PRM800K training samples that have the same problems in PROCESSBENCH. The training was run on eight A100 80GB GPUs.\n\n## D Inference Details\n\nFor solution generation in § 3.2, all the models are set with  $p = 0.9, t = 0.7$ . For majority voting evaluation in § 4, we set  $p = 0.8, t = 0.7, k = 20$  for Qwen2.5-Math-7/72B-Instruct to ensure their normal generation, while all the other models are set with only  $p = 0.9$ . All the inference in the evaluation was run with vLLM (Kwon et al., 2023) on eight A100 80GB GPUs.\n\n## E Prompt Template for Critic Model Evaluation\n\nThe following is a math problem and a solution (split into paragraphs, enclosed with tags and indexed from 0):\n\n[Math Problem]\n\n... (math problem) ...\n\n[Solution]\n\n&lt;paragraph\\_0>\n\n... (paragraph 0 of solution) ...\n\n&lt;/paragraph\\_0>\n\n...\n\n&lt;paragraph\\_n-1>\n\n... (paragraph n-1 of solution) ...\n\n&lt;/paragraph\\_n-1>\n\nYour task is to review and critique the solution paragraph by paragraph. Once you identify an error in a paragraph, return the **index of the paragraph where the earliest error occurs**. Otherwise, return the **index of -1 (which typically denotes \"not found\")**.\n\n**Please put your final answer (i.e., the index) in \\boxed{}.**\n\nFigure 7: Prompt template for critic model evaluation. The **blue texts** indicate the input math problem and the solution (split into paragraphs). The **red texts** describe the required output content and format.## F Supplementary Evaluation Results\n\nTable 5: Breakdown of evaluation results on the GSM8K and MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>24.2&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>21.4&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>37.9&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>43.8&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>90.1&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>54.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>44.9&lt;/td>\n&lt;td>90.6&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>30.5&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>45.1&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>95.8&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 6: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the GSM8K and MATH subsets, which are marginally higher than those in Table 5 that all adopt the threshold selected on the GSM8K subset.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>38.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>49.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>44.1&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Table 7: Breakdown of evaluation results on the OlympiadBench and Omni-MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>15.0&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>8.2&lt;/td>\n&lt;td>43.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>29.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>2.1&lt;/td>\n&lt;td>99.1&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>0.9&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>20.7&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>15.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>26.5&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>28.3&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>24.1&lt;/td>\n&lt;td>92.5&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>38.7&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>90.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>68.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>45.8&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 8: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the OlympiadBench and Omni-MATH subsets, which are slightly higher than those in Table 7 that all adopt the threshold selected on the GSM8K subset.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>\n&lt;td>15.3&lt;/td>\n&lt;td>47.5&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>58.5&lt;/td>\n&lt;td>22.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>\n&lt;td>18.9&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>14.4&lt;/td>\n&lt;td>58.1&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Table 9: Breakdown of evaluation results of the open-source language models (prompted as critic models) using *greedy decoding*.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>28.5&lt;/td>\n&lt;td>9.3&lt;/td>\n&lt;td>14.1&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>5.7&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>55.7&lt;/td>\n&lt;td>21.9&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>17.1&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>7.9&lt;/td>\n&lt;td>11.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>57.5&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>66.1&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>53.9&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>66.2&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>78.6&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>14.5&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>45.9&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>62.2&lt;/td>\n&lt;td>34.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>20.2&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.2&lt;/td>\n&lt;td>25.6&lt;/td>\n&lt;td>0.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>20.3&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>15.2&lt;/td>\n&lt;td>96.1&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>39.7&lt;/td>\n&lt;td>88.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>5.2&lt;/td>\n&lt;td>8.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>67.0&lt;/td>\n&lt;td>35.5&lt;/td>\n&lt;td>66.7&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>23.7&lt;/td>\n&lt;td>63.8&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>47.8&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>63.3&lt;/td>\n&lt;td>40.4&lt;/td>\n&lt;td>86.9&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>59.8&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>49.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>61.4&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>45.3&lt;/td>\n&lt;td>91.9&lt;/td>\n&lt;td>60.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>67.4&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>58.6&lt;/td>\n&lt;td>54.2&lt;/td>\n&lt;td>56.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n  \n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>17.2&lt;/td>\n&lt;td>0.6&lt;/td>\n&lt;td>1.1&lt;/td>\n&lt;td>17.3&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>41.6&lt;/td>\n&lt;td>27.8&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>29.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>19.1&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>17.1&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>39.0&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>30.9&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>86.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>6.4&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;td>11.8&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>17.2&lt;/td>\n&lt;td>95.0&lt;/td>\n&lt;td>29.2&lt;/td>\n&lt;td>18.3&lt;/td>\n&lt;td>93.4&lt;/td>\n&lt;td>30.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>13.3&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>27.8&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>16.6&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>86.7&lt;/td>\n&lt;td>46.5&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>45.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>14.1&lt;/td>\n&lt;td>2.9&lt;/td>\n&lt;td>4.9&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>2.9&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>39.4&lt;/td>\n&lt;td>30.4&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>37.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>43.6&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>30.9&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>44.0&lt;/td>\n&lt;td>27.0&lt;/td>\n&lt;td>72.6&lt;/td>\n&lt;td>39.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>35.9&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>88.5&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>48.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n",
    "durationMs": 753,
    "url": "https://huggingface.co/papers/2412.06559"
  },
  "sourceToolAssistantUUID": "524833aa-b536-43e4-a54c-efcdcc34c575",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "188c6a99-a16f-4710-acd2-885f93266800",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Tool result

_source line 38 · 2026-05-27T16:07:40.868Z_

<details><summary>↩ Tool result · `toolu_01UYNTMPEFgEWfBLBkDbbE3U`</summary>

```text
I appreciate the request, but I need to be transparent: the content provided appears to be a PDF file rendered as binary/encoded text rather than readable document content. The material shows PDF structure markers (like `%PDF-1.5`, object definitions, and stream data) but the actual textual content is not legibly displayed.

To properly extract and summarize a research paper's:
- Introduction and motivation
- Dataset construction methodology
- Experimental results and specific numbers
- Key findings and analysis
- Related work and conclusions

I would need the document in a readable format (clean text, proper PDF conversion, or native document format).

**Could you please provide:**
1. The paper title and authors
2. A text-readable version of the document, or
3. The specific sections you'd like me to focus on in plain text format

Once I have legible content, I'll provide a comprehensive summary adhering to your guidelines (125-character quote limits, proper attribution, no copyright violations).

[Binary content (application/pdf, 723.4KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/webfetch-1779898052477-dglqz6.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46ad2c57-5d31-428b-9a2a-a73e76971fc4",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "c54dc2c6-96a0-4ee2-ba91-99e9ee021c1c",
  "toolUseResult": {
    "bytes": 740748,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate the request, but I need to be transparent: the content provided appears to be a PDF file rendered as binary/encoded text rather than readable document content. The material shows PDF structure markers (like `%PDF-1.5`, object definitions, and stream data) but the actual textual content is not legibly displayed.\n\nTo properly extract and summarize a research paper's:\n- Introduction and motivation\n- Dataset construction methodology\n- Experimental results and specific numbers\n- Key findings and analysis\n- Related work and conclusions\n\nI would need the document in a readable format (clean text, proper PDF conversion, or native document format).\n\n**Could you please provide:**\n1. The paper title and authors\n2. A text-readable version of the document, or\n3. The specific sections you'd like me to focus on in plain text format\n\nOnce I have legible content, I'll provide a comprehensive summary adhering to your guidelines (125-character quote limits, proper attribution, no copyright violations).\n\n[Binary content (application/pdf, 723.4KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/webfetch-1779898052477-dglqz6.pdf]",
    "durationMs": 8629,
    "url": "https://www.arxiv.org/pdf/2412.06559"
  },
  "sourceToolAssistantUUID": "46ad2c57-5d31-428b-9a2a-a73e76971fc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-27T16:07:43.671Z_

<details><summary>Logged reasoning block</summary>

```text
I got some content from HuggingFace. Let me read the full saved output to get the complete paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c54dc2c6-96a0-4ee2-ba91-99e9ee021c1c",
  "isSidechain": false,
  "requestId": "req_011CbTMwm1LA9CwzELzGidMa",
  "type": "assistant",
  "uuid": "412d463d-1c9b-450e-8e74-9f1c75626ae3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcBa78mHd7R2zmwpKMrBHM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 619,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 16184,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 619,
          "output_tokens": 184,
          "cache_read_input_tokens": 16184,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 672
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

_source line 40 · 2026-05-27T16:07:44.187Z_

Let me read the full saved output from HuggingFace.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "412d463d-1c9b-450e-8e74-9f1c75626ae3",
  "isSidechain": false,
  "requestId": "req_011CbTMwm1LA9CwzELzGidMa",
  "type": "assistant",
  "uuid": "387f3cb0-cf3d-4d77-b673-14424e259707",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcBa78mHd7R2zmwpKMrBHM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 619,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 16184,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 619,
          "output_tokens": 184,
          "cache_read_input_tokens": 16184,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 672
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

_source line 41 · 2026-05-27T16:07:44.844Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EyGQNqncRZiQyMkRaYQp2r`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/toolu_01JLaPNUPbKr3rUPydFkfJVF.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "387f3cb0-cf3d-4d77-b673-14424e259707",
  "isSidechain": false,
  "requestId": "req_011CbTMwm1LA9CwzELzGidMa",
  "type": "assistant",
  "uuid": "eddf8bd1-b005-4aab-b8cb-a769c62b6070",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VcBa78mHd7R2zmwpKMrBHM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 619,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 16184,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 672,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 619,
          "output_tokens": 184,
          "cache_read_input_tokens": 16184,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 672
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

_source line 42 · 2026-05-27T16:07:45.135Z_

<details><summary>↩ Tool result · reported error · `toolu_01EyGQNqncRZiQyMkRaYQp2r`</summary>

```text
File content (27035 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eddf8bd1-b005-4aab-b8cb-a769c62b6070",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "3d8ee4b6-e8e0-49b5-b2ce-c8115aa0c7c5",
  "toolUseResult": "Error: File content (27035 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "eddf8bd1-b005-4aab-b8cb-a769c62b6070",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-27T16:07:47.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MMm8FddGii6M6tKaUNVL6G`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/toolu_01JLaPNUPbKr3rUPydFkfJVF.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d8ee4b6-e8e0-49b5-b2ce-c8115aa0c7c5",
  "isSidechain": false,
  "requestId": "req_011CbTMx5FSXq3QqaA8TR1hh",
  "type": "assistant",
  "uuid": "f419f2d2-595b-497d-af35-e8c36d21a52c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bPTbnAAz73qi8r1UNxri2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 863,
      "cache_read_input_tokens": 16856,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 16856,
          "cache_creation_input_tokens": 863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 863
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

_source line 44 · 2026-05-27T16:07:48.208Z_

<details><summary>↩ Tool result · `toolu_01MMm8FddGii6M6tKaUNVL6G`</summary>

````text
1	# PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning
2	
3	Chujie Zheng\* Zhenru Zhang Beichen Zhang Runji Lin Keming Lu  
4	Bowen Yu\* Dayiheng Liu\* Jingren Zhou Junyang Lin\*
5	
6	Qwen Team, Alibaba Inc.
7	
8	&lt;https://huggingface.co/datasets/Qwen/ProcessBench>
9	
10	&lt;https://github.com/QwenLM/ProcessBench>
11	
12	## Abstract
13	
14	As language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models (PRMs)* and *critic models*, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope PROCESSBENCH can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.
15	
16	Figure 1: Overview of evaluation results on PROCESSBENCH (see Table 3 for details).
17	
18	\*Corresponding authors.# 1 Introduction
19	
20	In recent years, language models have made remarkable progress in complex reasoning tasks, such as mathematics and programming (Hurst et al., 2024; OpenAI, 2024; Yang et al., 2024a,b; Dubey et al., 2024; Wake et al., 2024), yet they still make mistakes when solving challenging problems. To achieve scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024), i.e., effectively supervising AI systems that get close to or go beyond broadly human-level performance, particularly in complex tasks that are difficult for general humans, we expect language models can identify errors in their reasoning process in an automated way. However, existing benchmarks related to assessing language models' reasoning process may be hard to satisfy the growing evaluation demand for the error identification ability. Either their covered problems have become less challenging for recent language models (Zhou et al., 2024; Lightman et al., 2023), or they merely label the correctness of final answers but lack annotations for specific erroneous steps (Lin et al., 2024).
21	
22	```
23	"id": "math-22",
24	"generator": "Qwen2-7B-Instruct",
25	"problem": "Find the integer $n, $ 0 \le n \le 180, $ such that $ \cos n^\circ = \cos 568^\circ.",
26	"steps": [
27	  "To find the integer \(\(n\)\), \(\(0 \le n \le 180\)\), such that \(\(\cos n^\circ = \cos 568^\circ\)\), we can use the periodic properties of the cosine function. First, recall that the cosine function has a period of \(\(360^\circ\)\). This means that: \(\[\ \cos \ \theta = \cos (\theta + 360k) \]\) for any integer \(\(k\)\).",
28	  "Given \(\(\cos 568^\circ\)\), we need to reduce this angle to an equivalent angle within the first cycle of \(\(0\)\) to \(\(360^\circ\)\). We do this by subtracting multiples of \(\(360^\circ\)\) until we get an angle within this range: \(\[\ 568^\circ - 360^\circ = 208^\circ \]\) So, \(\(\cos 568^\circ = \cos 208^\circ\)\).",
29	  "However, we want to find \(\(n\)\) such that \(\(0 \le n \le 180\)\). Since cosine is also symmetric about \(\(180^\circ\)\), we know that: \(\[\ \cos \ \theta = \cos (180^\circ - \theta) \]\) Therefore, \(\(\cos 208^\circ = \cos (180^\circ - 208^\circ)\)\), which simplifies to: \(\[\ \cos 208^\circ = \cos (-28^\circ) \]\)",
30	  "The cosine function is also even, meaning it is symmetric about the y-axis: \(\[\ \cos (-\theta) = \cos \theta \]\) Thus, \(\[\ \cos (-28^\circ) = \cos 28^\circ \]\)",
31	  "So, \(\(n = 28^\circ\)\). Hence, the integer \(\(n\)\), \(\(0 \le n \le 180\)\), such that \(\(\cos n^\circ = \cos 568^\circ\)\) is \(\(n = 28\)\). The answer is \(\(\boxed{28}\)\).",
32	],
33	"final_answer_correct": false,
34	"label": 2
35	```
36	
37	Figure 2: Data example of PROCESSBENCH. The label 2 denotes that the earliest error occurs in the **2nd step** (indexed from 0). For test cases with no errors, the labels are  $-1$ .
38	
39	In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. Figure 2 presents a data example. We prioritize several principles when designing this benchmark:
40	
41	- • **Problem difficulty and solution diversity.** PROCESSBENCH primarily covers competition- and Olympiad-level math problems and utilizes various open-source language models to generate solutions. This ensures both the difficulty of math problems and the diversity of solution styles, enabling robust evaluation.
42	- • **Scale and accuracy.** PROCESSBENCH consists of 3,400 test cases, with all solutions annotated with error locations by multiple human experts. The large scale and expert annotation ensure the data quality and the reliability of evaluation.
43	- • **Simplicity.** PROCESSBENCH requires models to identify the earliest erroneous step occurring in the solution, if any exists. This straightforward evaluation protocol enables easy adaptation for various types of models, such as process reward models (PRMs) and critic models.
44	
45	We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models* (PRMs) and *critic models*. For PRMs, we include multiple open-source PRMs (Wang et al., 2024; Skywork, 2024; Xiong et al., 2024b) to assess the correctness of each reasoning step in the solution. For critic models, we prompt general language models like Qwen (Yang et al., 2024a; Qwen, 2024a; Hui et al., 2024) and GPT-4o (Hurst et al., 2024) to critique each solution step by step. We show that, despiterecent growing interest, existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset, which raises questions about the generalization abilities and scalability of the current data synthesis methodologies used to build PRMs. In contrast, general language models manifest non-trivial critique capabilities that can not only identify erroneous steps but also provide detailed explanations. The best open-source model, QwQ-32B-Preview (Qwen, 2024b), has performed competitively with the proprietary GPT-4o model, while it still lags behind the reasoning-specialized o1-mini (OpenAI, 2024). We hope PROCESSBENCH can catalyze future research in automated reasoning process assessment, establishing crucial foundations for scalable oversight of language models.
46	
47	## 2 Related Work
48	
49	There exist several benchmarks or datasets related to assessing language models’ reasoning process. CriticBench (Lin et al., 2024) evaluates language models’ abilities to critique solutions and correct mistakes in various reasoning tasks. MathCheck (Zhou et al., 2024) synthesizes solutions containing erroneous steps using the GSM8K dataset (Cobbe et al., 2021), in which language models are tasked with judging the correctness of final answers or reasoning steps. PRM800K (Lightman et al., 2023) builds on the MATH problems (Hendrycks et al., 2021) and annotates the correctness and soundness of reasoning steps in model-generated solutions. It also has sparked a blooming of research interest in building process reward models (PRMs) (Wang et al., 2024; Xiong et al., 2024b;a).
50	
51	Table 1: Comparison between PROCESSBENCH and other benchmarks or datasets related to reasoning process assessment (Lin et al., 2024; Zhou et al., 2024; Lightman et al., 2023). &lt;sup>†&lt;/sup>: Solution diversity denotes the diversity of language models used for solution generation, corresponding to the “# Solution Generators” column. &lt;sup>‡&lt;/sup>: For PRM800K, we only count the 90 complete solutions in its phase 1 test set, as the complete solutions in its phase 2 test set are all terminated at the earliest erroneous steps.
52	
53	&lt;table border="1">
54	&lt;thead>
55	&lt;tr>
56	&lt;th>&lt;/th>
57	&lt;th>Problem Difficulty&lt;/th>
58	&lt;th># Solution Generators&lt;/th>
59	&lt;th>Solution Diversity&lt;sup>†&lt;/sup>&lt;/th>
60	&lt;th>Step Annotation?&lt;/th>
61	&lt;th>Annotator&lt;/th>
62	&lt;th>Test Case Size (Identifying Process Errors)&lt;/th>
63	&lt;/tr>
64	&lt;/thead>
65	&lt;tbody>
66	&lt;tr>
67	&lt;td>CriticBench&lt;/td>
68	&lt;td>★★&lt;/td>
69	&lt;td>8&lt;/td>
70	&lt;td>★★★&lt;/td>
71	&lt;td>✗&lt;/td>
72	&lt;td>-&lt;/td>
73	&lt;td>-&lt;/td>
74	&lt;/tr>
75	&lt;tr>
76	&lt;td>MathCheck-GSM&lt;/td>
77	&lt;td>★&lt;/td>
78	&lt;td>1&lt;/td>
79	&lt;td>★&lt;/td>
80	&lt;td>✓&lt;/td>
81	&lt;td>Synthetic&lt;/td>
82	&lt;td>516&lt;/td>
83	&lt;/tr>
84	&lt;tr>
85	&lt;td>PRM800K&lt;/td>
86	&lt;td>★★&lt;/td>
87	&lt;td>1&lt;/td>
88	&lt;td>★&lt;/td>
89	&lt;td>✓&lt;/td>
90	&lt;td>Human&lt;/td>
91	&lt;td>90&lt;sup>‡&lt;/sup>&lt;/td>
92	&lt;/tr>
93	&lt;tr>
94	&lt;td>PROCESSBENCH&lt;/td>
95	&lt;td>★★★&lt;/td>
96	&lt;td>12&lt;/td>
97	&lt;td>★★★&lt;/td>
98	&lt;td>✓&lt;/td>
99	&lt;td>Human&lt;/td>
100	&lt;td>3,400&lt;/td>
101	&lt;/tr>
102	&lt;/tbody>
103	&lt;/table>
104	
105	PROCESSBENCH is distinguished from prior benchmarks or datasets in three key aspects, as highlighted in Table 1. **First**, PROCESSBENCH primarily covers more challenging math problems with competition- or Olympiad-level difficulty, which better fit the rapidly growing capabilities of modern language models. **Second**, rather than relying on synthetic data, PROCESSBENCH leverages diverse model-generated natural solutions and employs expert annotation to label erroneous steps, which ensures both real-world applicability and label accuracy. **Third**, the large scale of PROCESSBENCH (3,400 test cases in total) enables more comprehensive and robust evaluation.
106	
107	There has also been extensive research on language models’ scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024) and studies on whether language models can identify the errors in their own outputs. Lightman et al. (2023); Wang et al. (2024); Luo et al. (2024) propose to train specialized reward models to supervise language models’ reasoning process (i.e., process reward models or PRMs). Huang et al. (2023); Kamoi et al. (2024) argue that general language models struggle to identify and correct their reasoning errors without external feedback. Saunders et al. (2022); McAleese et al. (2024) show that language models can be trained to write informative critiques for both assisting human evaluation and enabling self-refinement, which favorably scales with increased model capabilities (or model sizes). We believe the improved capabilities of error identification will build strong foundations for language models’ scalable oversight.
108	
109	## 3 Benchmark Construction
110	
111	### 3.1 Task Definition
112	
113	As shown in Figure 2, given a math problem and a step-by-step solution, PROCESSBENCH requires models to either identify the *earliest-occurring error*, or conclude that all steps are *correct*. Formally,---
114	
115	given a math problem  $P$  and its step-by-step solution  $S = \{s_0, \dots, s_{n-1}\}$ , the task is to output an index  $i \in \{-1, 0, \dots, n-1\}$ , where  $i = -1$  indicates that all steps are correct, and  $i \geq 0$  indicates that the earliest error occurs at step  $s_i$ .
116	
117	Typically but non-inclusively, we consider a step as erroneous if it contains any of the following: (1) **Mathematical errors**: incorrect calculations, algebraic manipulations, or formula applications. (2) **Logical errors**: invalid deductions, unwarranted assumptions, or flawed reasoning steps. (3) **Conceptual errors**: misunderstanding or misapplication of mathematical or problem concepts. (4) **Completeness errors**: missing crucial conditions, constraints, or necessary justifications that affect the solution’s validity. Beyond these types of errors, we encourage human annotators to determine the correctness of reasoning steps based on their own expertise. We do not require human annotators to explicitly annotate error types due to the intractability of intentional categorization.
118	
119	Note that for steps after the first error, the meaning of their correctness may become ambiguous or debatable: derivations based on incorrect premises can make sense, but still remain on a globally incorrect reasoning path (Lightman et al., 2023). For instance, if step  $k$  contains an error in calculating  $x = 2$ , when it should be  $x = 3$ , subsequent steps may follow valid algebraic rules but operate on an incorrect value of  $x$ , making their individual correctness hard to determine. This is why PROCESSBENCH focuses on identifying the earliest-occurring error in the reasoning process.
120	
121	### 3.2 Data Collection
122	
123	**Problem Curation** We collect math problems from the test sets of four public and widely used datasets in mathematical reasoning tasks: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), Olympiad-Bench (He et al., 2024), and Omni-MATH (Gao et al., 2024). Except for GSM8K, which consists of grade school math problems, the other three datasets all contain problems with competition- or Olympiad-level difficulty.
124	
125	**Solution Generation** We generate solutions using the widely used Qwen (Yang et al., 2024a; Qwen, 2024a; Yang et al., 2024b) and LLaMA (Dubey et al., 2024) series open-source models, resulting in twelve distinct solution generators in total. This includes a wide range of model families, sizes, and downstream task performance, leading to the high diversity of solution styles. Table 4 in Appendix B presents the breakdown of language models used for PROCESSBENCH’s solution generation.
126	
127	**Solution Reformattng** In mathematical reasoning tasks, double line breaks (i.e., “\n\n”) are commonly used to segment solution steps (or paragraphs). However, we observed inconsistent step granularity due to varying solution styles and generation randomness. Some generated solutions frequently used double line breaks, resulting in numerous short, logically incomplete steps, while others used them sparingly, leading to lengthy paragraphs that combine multiple logical components. Such inconsistency in step granularity (and potential improper step segmentation) would impede the standardization of human annotation criteria.
128	
129	To address this issue, we adopt a *solution reformattng* method to standardize the step granularity, through which the segmented paragraphs can better correspond to logically complete and progressive reasoning steps. Specifically, we first replace all the line breaks with white space, and then ask Qwen2.5-72B-Instruct to insert double line breaks (i.e., segment paragraphs) while preserving the solution content. Since we found that Qwen2.5-72B-Instruct sometimes alters the solution content ( $< 0.5\%$ ), we remove those solutions whose final answers change after reformattng (although the content alteration may not influence benchmark construction). Consequently, the reformattng method effectively unifies the step granularity. Figure 6 in Appendix A presents an example of solution reformattng.
130	
131	**Expert Annotation** To ensure a balance between erroneous and correct solutions, we first use Qwen2.5-72B-Instruct to verify the correctness of final answers in the model-generated solutions against the reference answers. We then respectively sample solutions with correct or incorrect final answers for subsequent annotation in a balanced way to avoid excessive concentration on solutions from either the weakest or strongest models.
132	
133	We recruit human experts with doctoral-level mathematical expertise for annotation, and all of them are required to pass the mandatory proficiency examination and annotation tutorial. The annotators are designated with the same task in § 3.1, i.e., identifying the earliest-occurring error in each solution. However, we notice that the competition- or Olympiad-level math problems can still be challenging even for doctoral students majoring in mathematics. According to the feedback from the annotators, although they were not required to solve problems from scratch but rather to identify erroneous steps in presented solutions, they would still become quite hesitant in their annotations when uncertain about the correct solution approach, which affected both the annotation speed and quality. To ease the annotation difficulty,we provide annotators with the reference solutions and answers from the original datasets, while we still explicitly instructed them to inspect and verify the presented model-generated solutions step by step.
134	
135	Each solution is initially assigned to three different experts. When the initial three annotators cannot reach consensus, we increase the number of annotators until three of them agree on the same result. If an agreement cannot be achieved within five annotators (e.g., annotation distribution of (2, 2, 1) or (2, 1, 1, 1)), we discard this solution. This leads to an overall  $\sim 30\%$  discard rate throughout the entire annotation process. We also discard the solutions where the final answers are incorrect (according to the reference answers) but the human annotation results are correct. Although such cases are fairly rare ( $< 1\%$ ), they are mostly concentrated in the OlympiadBench and Omni-MATH problems (i.e., Olympiad-level ones). The agreement statistics in Table 2 further evidence that the more challenging problems usually need more annotators to achieve the annotation agreement, particularly for those samples with incorrect final answers. These results suggest the inherent challenge of our human annotation task.
136	
137	### 3.3 Statistics
138	
139	Table 2: Statistics of PROCESSBENCH. “% Process errors” denotes the proportion of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. “%  $\geq n$  steps” denotes the proportion of samples whose solutions have  $\geq n$  steps (split by double line breaks). “% 3/ $n$  agreement” denotes the proportion of samples where the three-annotator agreement is achieved within  $n$  annotators, so  $(\% 3/3) + (\% 3/4) + (\% 3/5) = 100\%$ .
140	
141	&lt;table border="1">
142	&lt;thead>
143	&lt;tr>
144	&lt;th rowspan="2">&lt;/th>
145	&lt;th colspan="2">GSM8K&lt;/th>
146	&lt;th colspan="2">MATH&lt;/th>
147	&lt;th colspan="2">OlympiadBench&lt;/th>
148	&lt;th colspan="2">Omni-MATH&lt;/th>
149	&lt;/tr>
150	&lt;tr>
151	&lt;th>error&lt;/th>
152	&lt;th>correct&lt;/th>
153	&lt;th>error&lt;/th>
154	&lt;th>correct&lt;/th>
155	&lt;th>error&lt;/th>
156	&lt;th>correct&lt;/th>
157	&lt;th>error&lt;/th>
158	&lt;th>correct&lt;/th>
159	&lt;/tr>
160	&lt;/thead>
161	&lt;tbody>
162	&lt;tr>
163	&lt;td># Samples&lt;/td>
164	&lt;td>207&lt;/td>
165	&lt;td>193&lt;/td>
166	&lt;td>594&lt;/td>
167	&lt;td>406&lt;/td>
168	&lt;td>661&lt;/td>
169	&lt;td>339&lt;/td>
170	&lt;td>759&lt;/td>
171	&lt;td>241&lt;/td>
172	&lt;/tr>
173	&lt;tr>
174	&lt;td>% Process errors&lt;br/>(correct final answers)&lt;/td>
175	&lt;td colspan="2">&lt;math>\frac{200-193}{200} = 3.5\%&lt;/math>&lt;/td>
176	&lt;td colspan="2">&lt;math>\frac{500-406}{500} = 18.8\%&lt;/math>&lt;/td>
177	&lt;td colspan="2">&lt;math>\frac{500-339}{500} = 32.2\%&lt;/math>&lt;/td>
178	&lt;td colspan="2">&lt;math>\frac{500-241}{500} = 51.8\%&lt;/math>&lt;/td>
179	&lt;/tr>
180	&lt;tr>
181	&lt;td># Steps&lt;/td>
182	&lt;td>5.3&lt;/td>
183	&lt;td>5.1&lt;/td>
184	&lt;td>6.8&lt;/td>
185	&lt;td>6.0&lt;/td>
186	&lt;td>8.9&lt;/td>
187	&lt;td>8.7&lt;/td>
188	&lt;td>8.6&lt;/td>
189	&lt;td>7.4&lt;/td>
190	&lt;/tr>
191	&lt;tr>
192	&lt;td>% &lt;math>\geq 5&lt;/math> steps&lt;/td>
193	&lt;td>61.8%&lt;/td>
194	&lt;td>57.5%&lt;/td>
195	&lt;td>73.6%&lt;/td>
196	&lt;td>70.4%&lt;/td>
197	&lt;td>92.6%&lt;/td>
198	&lt;td>92.3%&lt;/td>
199	&lt;td>92.5%&lt;/td>
200	&lt;td>81.7%&lt;/td>
201	&lt;/tr>
202	&lt;tr>
203	&lt;td>% &lt;math>\geq 10&lt;/math> steps&lt;/td>
204	&lt;td>3.4%&lt;/td>
205	&lt;td>1.6%&lt;/td>
206	&lt;td>17.8%&lt;/td>
207	&lt;td>8.9%&lt;/td>
208	&lt;td>33.9%&lt;/td>
209	&lt;td>27.1%&lt;/td>
210	&lt;td>29.2%&lt;/td>
211	&lt;td>21.6%&lt;/td>
212	&lt;/tr>
213	&lt;tr>
214	&lt;td>% &lt;math>\geq 15&lt;/math> steps&lt;/td>
215	&lt;td>0.5%&lt;/td>
216	&lt;td>0.0%&lt;/td>
217	&lt;td>3.4%&lt;/td>
218	&lt;td>2.0%&lt;/td>
219	&lt;td>9.1%&lt;/td>
220	&lt;td>8.8%&lt;/td>
221	&lt;td>7.5%&lt;/td>
222	&lt;td>4.1%&lt;/td>
223	&lt;/tr>
224	&lt;tr>
225	&lt;td>% 3/3 agreement&lt;/td>
226	&lt;td>66.7%&lt;/td>
227	&lt;td>95.9%&lt;/td>
228	&lt;td>59.4%&lt;/td>
229	&lt;td>91.9%&lt;/td>
230	&lt;td>52.8%&lt;/td>
231	&lt;td>85.0%&lt;/td>
232	&lt;td>47.8%&lt;/td>
233	&lt;td>80.1%&lt;/td>
234	&lt;/tr>
235	&lt;tr>
236	&lt;td>% 3/4 agreement&lt;/td>
237	&lt;td>21.3%&lt;/td>
238	&lt;td>3.6%&lt;/td>
239	&lt;td>24.4%&lt;/td>
240	&lt;td>4.7%&lt;/td>
241	&lt;td>24.1%&lt;/td>
242	&lt;td>9.1%&lt;/td>
243	&lt;td>25.6%&lt;/td>
244	&lt;td>13.7%&lt;/td>
245	&lt;/tr>
246	&lt;tr>
247	&lt;td>% 3/5 agreement&lt;/td>
248	&lt;td>12.1%&lt;/td>
249	&lt;td>0.5%&lt;/td>
250	&lt;td>16.2%&lt;/td>
251	&lt;td>3.4%&lt;/td>
252	&lt;td>23.1%&lt;/td>
253	&lt;td>5.9%&lt;/td>
254	&lt;td>26.6%&lt;/td>
255	&lt;td>6.2%&lt;/td>
256	&lt;/tr>
257	&lt;/tbody>
258	&lt;/table>
259	
260	The resulting PROCESSBENCH has four subsets, consisting of 3,400 test cases in total. The detailed statistics are shown in Table 2 and Table 4 (in Appendix B), and we also plot in Figure 3 the distribution of error positions in erroneous samples. In general, the more challenging the problems, the more solution steps the models generate, and incorrect solutions usually contain more steps than correct ones. However, across all four subsets, a large proportion of errors occur in the earlier steps, such as steps 0-3 in GSM8K and MATH, and steps 1-5 in OlympiadBench and Omni-MATH.
261	
262	Figure 3: Distribution of error positions (indexed from 0; truncated to 16 for better visualization), corresponding to the *label* field as shown in Figure 2.
263	
264	It is noteworthy that while we have intentionally controlled an equal number of solutions with incorrect and correct final answers (200 each for GSM8K and 500 each for other subsets), the annotationFigure 4: Process error ratios per models and subsets, computed as the proportions of samples annotated as *erroneous* among all the samples with *correct final answers* (same as in Table 2). The models used for solution generation slightly vary across different subsets, see Table 4 in Appendix B. We observe that no particular models have notably higher process error rates, while **the process error rates are consistently higher on more difficult problems for all the models.**
265	
266	results reveal quite different numbers. Specifically, in the more challenging subsets like OlympiadBench and Omni-MATH, a larger proportion of solutions with correct final answers still contain erroneous steps. For instance, in OlympiadBench,  $\frac{500-339}{500} = 32.2\%$  of solutions with correct final answers are found to contain process errors, while in Omni-MATH this proportion is even higher ( $\frac{500-241}{500} = 51.8\%$ ). In contrast, these proportions in GSM8K and MATH are  $\frac{200-193}{200} = 3.5\%$  and  $\frac{500-406}{500} = 18.8\%$ , respectively. In Figure 4, for each model used for solution generation, we plot the ratio of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. We observe that the process error rates are consistently higher on more difficult problems. To our knowledge, our work is **the first to present evidence that on more challenging math problems, current language models are more prone to making process errors even when reaching correct final answers.** This also suggests the underlying limitation of rule-based RL in mathematical reasoning (i.e., rewarding merely according to the correctness of final answers) and further highlights the significance of identifying errors in the reasoning process.
267	
268	## 4 Evaluation
269	
270	### 4.1 Setup
271	
272	For each subset of PROCESSBENCH, we calculate the accuracies on erroneous and correct samples, respectively, and additionally compute their harmonic mean as the **F1 score**. We primarily refer to F1 scores to compare model performance, as it balances model behaviors between being overly critical and being incapable of identifying errors.
273	
274	We consider two types of models in the evaluation on PROCESSBENCH: *process reward models (PRMs)* and *critic models*.
275	
276	**Process Reward Models (PRMs)** As a recently focal topic, PRMs are proposed to assess and supervise the intermediate steps in language models’ reasoning process (Lightman et al., 2023), thus naturally falling in the scope of our research. In practice, PRMs are typically trained using the process labels for intermediate reasoning steps, outputting either the correctness prediction or a scalar score for each reasoning step during inference. Previous research usually evaluates PRMs based on their improvement in the Best-of-N (BoN) performance of another language model that generates solutions. However, this lacks a finer-grained inspection on their process assessment abilities, and the evaluation reliability can be heavily affected by the underlying solution generation model.
277	
278	Our evaluation includes several open-source PRMs: (1) Math-Shepherd (Wang et al., 2024), which obtains the process label for each step via estimating the empirical probability of this step leading to the correct final answer. (2) Two LLaMA-3.1-based PRMs from Xiong et al. (2024b), which roughly follow the training methodology of Math-Shepherd but differ in the solution generation models and optimization objectives. (3) Two Qwen2.5-Math-based PRMs recently released by Skywork (2024). (4) We also train a PRM by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K dataset, namely Qwen2.5-Math-7B-PRM800K. See Appendix C for its training details.For the (1)(2)(4) PRMs, we extract the earliest erroneous step from their correctness predictions for reasoning steps. For the (3) PRMs, which produce scalar scores for each reasoning step, we first transform these scores into binary correctness predictions (using a threshold above which steps are considered as correct), and then extract the earliest erroneous step as we do for (1)(2)(4). The transformation threshold is determined as the one giving the highest F1 score on the GSM8K subset.
279	
280	**Critic Models** Critic models aim to provide feedback and critique to model-generated texts, non-inclusively including verification, reflection, and correction or refinement. They have demonstrated promising utility in achieving scalable oversight (Saunders et al., 2022; McAleese et al., 2024).
281	
282	Training critic models for specific domains typically requires significant and specialized effort, which is out of the scope of our work. Instead, we are more interested in the critique capabilities of *general language models*. The task definition (§ 3.1) of PROCESSBENCH enables us to apply simple prompt engineering to repurpose general language models as critic models. We show in Figure 7 in Appendix E the prompt template we implement for our evaluation. Specifically, models are prompted to return the index of the paragraph where the earliest error occurs as the *final answer*, similar to the conventional evaluation protocol for mathematical reasoning tasks (Cobbe et al., 2021; Hendrycks et al., 2021; Yang et al., 2024b).
283	
284	Our evaluation includes the widely-used Qwen2 (Yang et al., 2024a), Qwen2.5 (Qwen, 2024a), Qwen2.5-Math (Yang et al., 2024b), Qwen2.5-Coder (Hui et al., 2024), and LLaMA-3 (Dubey et al., 2024) series open-source models, as well as the recently released QwQ-32B-Preview reasoning model (Qwen, 2024b). We also evaluate the proprietary GPT-4o (Hurst et al., 2024) and o1-mini (OpenAI, 2024) models. We report the performance of open-source models under majority voting over eight samplings, while we also report their performance under greedy decoding in Table 9 in Appendix F. For the proprietary model GPT-4o, we report the results under greedy decoding, while for o1-mini, we report the results under single sampling as its API does not support customized decoding parameters.
285	
286	Table 3: Evaluation results on PROCESSBENCH. We report the F1 score of the respective accuracies on erroneous and correct samples. See Table 5 and Table 7 for breakdown of evaluation results.
287	
288	&lt;table border="1">
289	&lt;thead>
290	&lt;tr>
291	&lt;th>Model&lt;/th>
292	&lt;th>GSM8K&lt;/th>
293	&lt;th>MATH&lt;/th>
294	&lt;th>Olympiad-Bench&lt;/th>
295	&lt;th>Omni-MATH&lt;/th>
296	&lt;th>Average&lt;/th>
297	&lt;/tr>
298	&lt;/thead>
299	&lt;tbody>
300	&lt;tr>
301	&lt;td colspan="6" style="text-align: center;">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>
302	&lt;/tr>
303	&lt;tr>
304	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
305	&lt;td>47.9&lt;/td>
306	&lt;td>29.5&lt;/td>
307	&lt;td>24.8&lt;/td>
308	&lt;td>23.8&lt;/td>
309	&lt;td>31.5&lt;/td>
310	&lt;/tr>
311	&lt;tr>
312	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
313	&lt;td>50.4&lt;/td>
314	&lt;td>33.4&lt;/td>
315	&lt;td>13.8&lt;/td>
316	&lt;td>15.8&lt;/td>
317	&lt;td>28.4&lt;/td>
318	&lt;/tr>
319	&lt;tr>
320	&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>
321	&lt;td>38.8&lt;/td>
322	&lt;td>33.8&lt;/td>
323	&lt;td>16.9&lt;/td>
324	&lt;td>16.9&lt;/td>
325	&lt;td>26.6&lt;/td>
326	&lt;/tr>
327	&lt;tr>
328	&lt;td>Skywork-PRM-1.5B&lt;/td>
329	&lt;td>59.0&lt;/td>
330	&lt;td>48.0&lt;/td>
331	&lt;td>19.3&lt;/td>
332	&lt;td>19.2&lt;/td>
333	&lt;td>36.4&lt;/td>
334	&lt;/tr>
335	&lt;tr>
336	&lt;td>Skywork-PRM-7B&lt;/td>
337	&lt;td>&lt;b>70.8&lt;/b>&lt;/td>
338	&lt;td>53.6&lt;/td>
339	&lt;td>22.9&lt;/td>
340	&lt;td>21.0&lt;/td>
341	&lt;td>42.1&lt;/td>
342	&lt;/tr>
343	&lt;tr>
344	&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>
345	&lt;td>&lt;b>68.2&lt;/b>&lt;/td>
346	&lt;td>&lt;b>62.6&lt;/b>&lt;/td>
347	&lt;td>&lt;b>50.7&lt;/b>&lt;/td>
348	&lt;td>&lt;b>44.3&lt;/b>&lt;/td>
349	&lt;td>&lt;b>56.5&lt;/b>&lt;/td>
350	&lt;/tr>
351	&lt;tr>
352	&lt;td colspan="6" style="text-align: center;">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>
353	&lt;/tr>
354	&lt;tr>
355	&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>
356	&lt;td>13.1&lt;/td>
357	&lt;td>13.8&lt;/td>
358	&lt;td>4.8&lt;/td>
359	&lt;td>12.6&lt;/td>
360	&lt;td>11.1&lt;/td>
361	&lt;/tr>
362	&lt;tr>
363	&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>
364	&lt;td>52.2&lt;/td>
365	&lt;td>22.8&lt;/td>
366	&lt;td>21.2&lt;/td>
367	&lt;td>20.0&lt;/td>
368	&lt;td>29.1&lt;/td>
369	&lt;/tr>
370	&lt;tr>
371	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
372	&lt;td>10.9&lt;/td>
373	&lt;td>5.1&lt;/td>
374	&lt;td>2.8&lt;/td>
375	&lt;td>1.6&lt;/td>
376	&lt;td>5.1&lt;/td>
377	&lt;/tr>
378	&lt;tr>
379	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
380	&lt;td>74.9&lt;/td>
381	&lt;td>48.2&lt;/td>
382	&lt;td>46.7&lt;/td>
383	&lt;td>41.0&lt;/td>
384	&lt;td>52.7&lt;/td>
385	&lt;/tr>
386	&lt;tr>
387	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
388	&lt;td>82.9&lt;/td>
389	&lt;td>59.4&lt;/td>
390	&lt;td>46.7&lt;/td>
391	&lt;td>43.0&lt;/td>
392	&lt;td>58.0&lt;/td>
393	&lt;/tr>
394	&lt;tr>
395	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
396	&lt;td>26.8&lt;/td>
397	&lt;td>25.7&lt;/td>
398	&lt;td>14.2&lt;/td>
399	&lt;td>12.7&lt;/td>
400	&lt;td>19.9&lt;/td>
401	&lt;/tr>
402	&lt;tr>
403	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
404	&lt;td>65.8&lt;/td>
405	&lt;td>52.1&lt;/td>
406	&lt;td>32.5&lt;/td>
407	&lt;td>31.7&lt;/td>
408	&lt;td>45.5&lt;/td>
409	&lt;/tr>
410	&lt;tr>
411	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
412	&lt;td>14.3&lt;/td>
413	&lt;td>6.5&lt;/td>
414	&lt;td>4.1&lt;/td>
415	&lt;td>1.8&lt;/td>
416	&lt;td>6.7&lt;/td>
417	&lt;/tr>
418	&lt;tr>
419	&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>
420	&lt;td>50.1&lt;/td>
421	&lt;td>39.9&lt;/td>
422	&lt;td>34.0&lt;/td>
423	&lt;td>27.3&lt;/td>
424	&lt;td>37.8&lt;/td>
425	&lt;/tr>
426	&lt;tr>
427	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
428	&lt;td>68.9&lt;/td>
429	&lt;td>60.1&lt;/td>
430	&lt;td>48.9&lt;/td>
431	&lt;td>46.3&lt;/td>
432	&lt;td>56.1&lt;/td>
433	&lt;/tr>
434	&lt;tr>
435	&lt;td>Qwen2-7B-Instruct&lt;/td>
436	&lt;td>8.4&lt;/td>
437	&lt;td>19.0&lt;/td>
438	&lt;td>14.7&lt;/td>
439	&lt;td>12.1&lt;/td>
440	&lt;td>13.6&lt;/td>
441	&lt;/tr>
442	&lt;tr>
443	&lt;td>Qwen2-72B-Instruct&lt;/td>
444	&lt;td>67.6&lt;/td>
445	&lt;td>49.2&lt;/td>
446	&lt;td>42.1&lt;/td>
447	&lt;td>40.2&lt;/td>
448	&lt;td>49.8&lt;/td>
449	&lt;/tr>
450	&lt;tr>
451	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
452	&lt;td>36.5&lt;/td>
453	&lt;td>36.6&lt;/td>
454	&lt;td>29.7&lt;/td>
455	&lt;td>27.4&lt;/td>
456	&lt;td>32.6&lt;/td>
457	&lt;/tr>
458	&lt;tr>
459	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
460	&lt;td>69.3&lt;/td>
461	&lt;td>53.3&lt;/td>
462	&lt;td>45.0&lt;/td>
463	&lt;td>41.3&lt;/td>
464	&lt;td>52.2&lt;/td>
465	&lt;/tr>
466	&lt;tr>
467	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
468	&lt;td>65.6&lt;/td>
469	&lt;td>53.1&lt;/td>
470	&lt;td>40.0&lt;/td>
471	&lt;td>38.3&lt;/td>
472	&lt;td>49.3&lt;/td>
473	&lt;/tr>
474	&lt;tr>
475	&lt;td>Qwen2.5-72B-Instruct&lt;/td>
476	&lt;td>76.2&lt;/td>
477	&lt;td>61.8&lt;/td>
478	&lt;td>54.6&lt;/td>
479	&lt;td>52.2&lt;/td>
480	&lt;td>61.2&lt;/td>
481	&lt;/tr>
482	&lt;tr>
483	&lt;td>&lt;b>★ QwQ-32B-Preview&lt;/b>&lt;/td>
484	&lt;td>&lt;b>88.0&lt;/b>&lt;/td>
485	&lt;td>&lt;b>78.7&lt;/b>&lt;/td>
486	&lt;td>&lt;b>57.8&lt;/b>&lt;/td>
487	&lt;td>&lt;b>61.3&lt;/b>&lt;/td>
488	&lt;td>&lt;b>71.5&lt;/b>&lt;/td>
489	&lt;/tr>
490	&lt;tr>
491	&lt;td colspan="6" style="text-align: center;">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>
492	&lt;/tr>
493	&lt;tr>
494	&lt;td>GPT-4o-0806&lt;/td>
495	&lt;td>79.2&lt;/td>
496	&lt;td>63.6&lt;/td>
497	&lt;td>51.4&lt;/td>
498	&lt;td>53.5&lt;/td>
499	&lt;td>61.9&lt;/td>
500	&lt;/tr>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "f419f2d2-595b-497d-af35-e8c36d21a52c",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "17350b97-c9f5-40cb-81c2-0ca2fc83b432",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/toolu_01JLaPNUPbKr3rUPydFkfJVF.txt",
      "content": "# PROCESSBENCH: Identifying Process Errors in Mathematical Reasoning\n\nChujie Zheng\\* Zhenru Zhang Beichen Zhang Runji Lin Keming Lu  \nBowen Yu\\* Dayiheng Liu\\* Jingren Zhou Junyang Lin\\*\n\nQwen Team, Alibaba Inc.\n\n&lt;https://huggingface.co/datasets/Qwen/ProcessBench>\n\n&lt;https://github.com/QwenLM/ProcessBench>\n\n## Abstract\n\nAs language models regularly make mistakes when solving math problems, automated identification of errors in the reasoning process becomes increasingly significant for their scalable oversight. In this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. It consists of 3,400 test cases, primarily focused on competition- and Olympiad-level math problems. Each test case contains a step-by-step solution with error location annotated by human experts. Models are required to identify the earliest step that contains an error, or conclude that all steps are correct. We conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models (PRMs)* and *critic models*, where for the latter we prompt general language models to critique each solution step by step. We draw two main observations: (1) Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models (i.e., prompted general language models) and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset. (2) The best open-source model, QwQ-32B-Preview, has demonstrated the critique capability competitive with the proprietary model GPT-4o, despite that it still lags behind the reasoning-specialized o1-mini. We hope PROCESSBENCH can foster future research in reasoning process assessment, paving the way toward scalable oversight of language models.\n\nFigure 1: Overview of evaluation results on PROCESSBENCH (see Table 3 for details).\n\n\\*Corresponding authors.# 1 Introduction\n\nIn recent years, language models have made remarkable progress in complex reasoning tasks, such as mathematics and programming (Hurst et al., 2024; OpenAI, 2024; Yang et al., 2024a,b; Dubey et al., 2024; Wake et al., 2024), yet they still make mistakes when solving challenging problems. To achieve scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024), i.e., effectively supervising AI systems that get close to or go beyond broadly human-level performance, particularly in complex tasks that are difficult for general humans, we expect language models can identify errors in their reasoning process in an automated way. However, existing benchmarks related to assessing language models' reasoning process may be hard to satisfy the growing evaluation demand for the error identification ability. Either their covered problems have become less challenging for recent language models (Zhou et al., 2024; Lightman et al., 2023), or they merely label the correctness of final answers but lack annotations for specific erroneous steps (Lin et al., 2024).\n\n```\n\"id\": \"math-22\",\n\"generator\": \"Qwen2-7B-Instruct\",\n\"problem\": \"Find the integer $n, $ 0 \\le n \\le 180, $ such that $ \\cos n^\\circ = \\cos 568^\\circ.\",\n\"steps\": [\n  \"To find the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\), we can use the periodic properties of the cosine function. First, recall that the cosine function has a period of \\(\\(360^\\circ\\)\\). This means that: \\(\\[\\ \\cos \\ \\theta = \\cos (\\theta + 360k) \\]\\) for any integer \\(\\(k\\)\\).\",\n  \"Given \\(\\(\\cos 568^\\circ\\)\\), we need to reduce this angle to an equivalent angle within the first cycle of \\(\\(0\\)\\) to \\(\\(360^\\circ\\)\\). We do this by subtracting multiples of \\(\\(360^\\circ\\)\\) until we get an angle within this range: \\(\\[\\ 568^\\circ - 360^\\circ = 208^\\circ \\]\\) So, \\(\\(\\cos 568^\\circ = \\cos 208^\\circ\\)\\).\",\n  \"However, we want to find \\(\\(n\\)\\) such that \\(\\(0 \\le n \\le 180\\)\\). Since cosine is also symmetric about \\(\\(180^\\circ\\)\\), we know that: \\(\\[\\ \\cos \\ \\theta = \\cos (180^\\circ - \\theta) \\]\\) Therefore, \\(\\(\\cos 208^\\circ = \\cos (180^\\circ - 208^\\circ)\\)\\), which simplifies to: \\(\\[\\ \\cos 208^\\circ = \\cos (-28^\\circ) \\]\\)\",\n  \"The cosine function is also even, meaning it is symmetric about the y-axis: \\(\\[\\ \\cos (-\\theta) = \\cos \\theta \\]\\) Thus, \\(\\[\\ \\cos (-28^\\circ) = \\cos 28^\\circ \\]\\)\",\n  \"So, \\(\\(n = 28^\\circ\\)\\). Hence, the integer \\(\\(n\\)\\), \\(\\(0 \\le n \\le 180\\)\\), such that \\(\\(\\cos n^\\circ = \\cos 568^\\circ\\)\\) is \\(\\(n = 28\\)\\). The answer is \\(\\(\\boxed{28}\\)\\).\",\n],\n\"final_answer_correct\": false,\n\"label\": 2\n```\n\nFigure 2: Data example of PROCESSBENCH. The label 2 denotes that the earliest error occurs in the **2nd step** (indexed from 0). For test cases with no errors, the labels are  $-1$ .\n\nIn this paper, we introduce **PROCESSBENCH** for measuring the ability to identify erroneous steps in mathematical reasoning. Figure 2 presents a data example. We prioritize several principles when designing this benchmark:\n\n- • **Problem difficulty and solution diversity.** PROCESSBENCH primarily covers competition- and Olympiad-level math problems and utilizes various open-source language models to generate solutions. This ensures both the difficulty of math problems and the diversity of solution styles, enabling robust evaluation.\n- • **Scale and accuracy.** PROCESSBENCH consists of 3,400 test cases, with all solutions annotated with error locations by multiple human experts. The large scale and expert annotation ensure the data quality and the reliability of evaluation.\n- • **Simplicity.** PROCESSBENCH requires models to identify the earliest erroneous step occurring in the solution, if any exists. This straightforward evaluation protocol enables easy adaptation for various types of models, such as process reward models (PRMs) and critic models.\n\nWe conduct extensive evaluation on PROCESSBENCH, involving two types of models: *process reward models* (PRMs) and *critic models*. For PRMs, we include multiple open-source PRMs (Wang et al., 2024; Skywork, 2024; Xiong et al., 2024b) to assess the correctness of each reasoning step in the solution. For critic models, we prompt general language models like Qwen (Yang et al., 2024a; Qwen, 2024a; Hui et al., 2024) and GPT-4o (Hurst et al., 2024) to critique each solution step by step. We show that, despiterecent growing interest, existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH. They underperform both critic models and our own trained PRM that is straightforwardly fine-tuned on the PRM800K dataset, which raises questions about the generalization abilities and scalability of the current data synthesis methodologies used to build PRMs. In contrast, general language models manifest non-trivial critique capabilities that can not only identify erroneous steps but also provide detailed explanations. The best open-source model, QwQ-32B-Preview (Qwen, 2024b), has performed competitively with the proprietary GPT-4o model, while it still lags behind the reasoning-specialized o1-mini (OpenAI, 2024). We hope PROCESSBENCH can catalyze future research in automated reasoning process assessment, establishing crucial foundations for scalable oversight of language models.\n\n## 2 Related Work\n\nThere exist several benchmarks or datasets related to assessing language models’ reasoning process. CriticBench (Lin et al., 2024) evaluates language models’ abilities to critique solutions and correct mistakes in various reasoning tasks. MathCheck (Zhou et al., 2024) synthesizes solutions containing erroneous steps using the GSM8K dataset (Cobbe et al., 2021), in which language models are tasked with judging the correctness of final answers or reasoning steps. PRM800K (Lightman et al., 2023) builds on the MATH problems (Hendrycks et al., 2021) and annotates the correctness and soundness of reasoning steps in model-generated solutions. It also has sparked a blooming of research interest in building process reward models (PRMs) (Wang et al., 2024; Xiong et al., 2024b;a).\n\nTable 1: Comparison between PROCESSBENCH and other benchmarks or datasets related to reasoning process assessment (Lin et al., 2024; Zhou et al., 2024; Lightman et al., 2023). &lt;sup>†&lt;/sup>: Solution diversity denotes the diversity of language models used for solution generation, corresponding to the “# Solution Generators” column. &lt;sup>‡&lt;/sup>: For PRM800K, we only count the 90 complete solutions in its phase 1 test set, as the complete solutions in its phase 2 test set are all terminated at the earliest erroneous steps.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>Problem Difficulty&lt;/th>\n&lt;th># Solution Generators&lt;/th>\n&lt;th>Solution Diversity&lt;sup>†&lt;/sup>&lt;/th>\n&lt;th>Step Annotation?&lt;/th>\n&lt;th>Annotator&lt;/th>\n&lt;th>Test Case Size (Identifying Process Errors)&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>MathCheck-GSM&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>516&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PRM800K&lt;/td>\n&lt;td>★★&lt;/td>\n&lt;td>1&lt;/td>\n&lt;td>★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>90&lt;sup>‡&lt;/sup>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>PROCESSBENCH&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>★★★&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>Human&lt;/td>\n&lt;td>3,400&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nPROCESSBENCH is distinguished from prior benchmarks or datasets in three key aspects, as highlighted in Table 1. **First**, PROCESSBENCH primarily covers more challenging math problems with competition- or Olympiad-level difficulty, which better fit the rapidly growing capabilities of modern language models. **Second**, rather than relying on synthetic data, PROCESSBENCH leverages diverse model-generated natural solutions and employs expert annotation to label erroneous steps, which ensures both real-world applicability and label accuracy. **Third**, the large scale of PROCESSBENCH (3,400 test cases in total) enables more comprehensive and robust evaluation.\n\nThere has also been extensive research on language models’ scalable oversight (Amodei et al., 2016; Bowman et al., 2022; Cao et al., 2024) and studies on whether language models can identify the errors in their own outputs. Lightman et al. (2023); Wang et al. (2024); Luo et al. (2024) propose to train specialized reward models to supervise language models’ reasoning process (i.e., process reward models or PRMs). Huang et al. (2023); Kamoi et al. (2024) argue that general language models struggle to identify and correct their reasoning errors without external feedback. Saunders et al. (2022); McAleese et al. (2024) show that language models can be trained to write informative critiques for both assisting human evaluation and enabling self-refinement, which favorably scales with increased model capabilities (or model sizes). We believe the improved capabilities of error identification will build strong foundations for language models’ scalable oversight.\n\n## 3 Benchmark Construction\n\n### 3.1 Task Definition\n\nAs shown in Figure 2, given a math problem and a step-by-step solution, PROCESSBENCH requires models to either identify the *earliest-occurring error*, or conclude that all steps are *correct*. Formally,---\n\ngiven a math problem  $P$  and its step-by-step solution  $S = \\{s_0, \\dots, s_{n-1}\\}$ , the task is to output an index  $i \\in \\{-1, 0, \\dots, n-1\\}$ , where  $i = -1$  indicates that all steps are correct, and  $i \\geq 0$  indicates that the earliest error occurs at step  $s_i$ .\n\nTypically but non-inclusively, we consider a step as erroneous if it contains any of the following: (1) **Mathematical errors**: incorrect calculations, algebraic manipulations, or formula applications. (2) **Logical errors**: invalid deductions, unwarranted assumptions, or flawed reasoning steps. (3) **Conceptual errors**: misunderstanding or misapplication of mathematical or problem concepts. (4) **Completeness errors**: missing crucial conditions, constraints, or necessary justifications that affect the solution’s validity. Beyond these types of errors, we encourage human annotators to determine the correctness of reasoning steps based on their own expertise. We do not require human annotators to explicitly annotate error types due to the intractability of intentional categorization.\n\nNote that for steps after the first error, the meaning of their correctness may become ambiguous or debatable: derivations based on incorrect premises can make sense, but still remain on a globally incorrect reasoning path (Lightman et al., 2023). For instance, if step  $k$  contains an error in calculating  $x = 2$ , when it should be  $x = 3$ , subsequent steps may follow valid algebraic rules but operate on an incorrect value of  $x$ , making their individual correctness hard to determine. This is why PROCESSBENCH focuses on identifying the earliest-occurring error in the reasoning process.\n\n### 3.2 Data Collection\n\n**Problem Curation** We collect math problems from the test sets of four public and widely used datasets in mathematical reasoning tasks: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), Olympiad-Bench (He et al., 2024), and Omni-MATH (Gao et al., 2024). Except for GSM8K, which consists of grade school math problems, the other three datasets all contain problems with competition- or Olympiad-level difficulty.\n\n**Solution Generation** We generate solutions using the widely used Qwen (Yang et al., 2024a; Qwen, 2024a; Yang et al., 2024b) and LLaMA (Dubey et al., 2024) series open-source models, resulting in twelve distinct solution generators in total. This includes a wide range of model families, sizes, and downstream task performance, leading to the high diversity of solution styles. Table 4 in Appendix B presents the breakdown of language models used for PROCESSBENCH’s solution generation.\n\n**Solution Reformattng** In mathematical reasoning tasks, double line breaks (i.e., “\\n\\n”) are commonly used to segment solution steps (or paragraphs). However, we observed inconsistent step granularity due to varying solution styles and generation randomness. Some generated solutions frequently used double line breaks, resulting in numerous short, logically incomplete steps, while others used them sparingly, leading to lengthy paragraphs that combine multiple logical components. Such inconsistency in step granularity (and potential improper step segmentation) would impede the standardization of human annotation criteria.\n\nTo address this issue, we adopt a *solution reformattng* method to standardize the step granularity, through which the segmented paragraphs can better correspond to logically complete and progressive reasoning steps. Specifically, we first replace all the line breaks with white space, and then ask Qwen2.5-72B-Instruct to insert double line breaks (i.e., segment paragraphs) while preserving the solution content. Since we found that Qwen2.5-72B-Instruct sometimes alters the solution content ( $< 0.5\\%$ ), we remove those solutions whose final answers change after reformattng (although the content alteration may not influence benchmark construction). Consequently, the reformattng method effectively unifies the step granularity. Figure 6 in Appendix A presents an example of solution reformattng.\n\n**Expert Annotation** To ensure a balance between erroneous and correct solutions, we first use Qwen2.5-72B-Instruct to verify the correctness of final answers in the model-generated solutions against the reference answers. We then respectively sample solutions with correct or incorrect final answers for subsequent annotation in a balanced way to avoid excessive concentration on solutions from either the weakest or strongest models.\n\nWe recruit human experts with doctoral-level mathematical expertise for annotation, and all of them are required to pass the mandatory proficiency examination and annotation tutorial. The annotators are designated with the same task in § 3.1, i.e., identifying the earliest-occurring error in each solution. However, we notice that the competition- or Olympiad-level math problems can still be challenging even for doctoral students majoring in mathematics. According to the feedback from the annotators, although they were not required to solve problems from scratch but rather to identify erroneous steps in presented solutions, they would still become quite hesitant in their annotations when uncertain about the correct solution approach, which affected both the annotation speed and quality. To ease the annotation difficulty,we provide annotators with the reference solutions and answers from the original datasets, while we still explicitly instructed them to inspect and verify the presented model-generated solutions step by step.\n\nEach solution is initially assigned to three different experts. When the initial three annotators cannot reach consensus, we increase the number of annotators until three of them agree on the same result. If an agreement cannot be achieved within five annotators (e.g., annotation distribution of (2, 2, 1) or (2, 1, 1, 1)), we discard this solution. This leads to an overall  $\\sim 30\\%$  discard rate throughout the entire annotation process. We also discard the solutions where the final answers are incorrect (according to the reference answers) but the human annotation results are correct. Although such cases are fairly rare ( $< 1\\%$ ), they are mostly concentrated in the OlympiadBench and Omni-MATH problems (i.e., Olympiad-level ones). The agreement statistics in Table 2 further evidence that the more challenging problems usually need more annotators to achieve the annotation agreement, particularly for those samples with incorrect final answers. These results suggest the inherent challenge of our human annotation task.\n\n### 3.3 Statistics\n\nTable 2: Statistics of PROCESSBENCH. “% Process errors” denotes the proportion of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. “%  $\\geq n$  steps” denotes the proportion of samples whose solutions have  $\\geq n$  steps (split by double line breaks). “% 3/ $n$  agreement” denotes the proportion of samples where the three-annotator agreement is achieved within  $n$  annotators, so  $(\\% 3/3) + (\\% 3/4) + (\\% 3/5) = 100\\%$ .\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td># Samples&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% Process errors&lt;br/>(correct final answers)&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{200-193}{200} = 3.5\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-406}{500} = 18.8\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-339}{500} = 32.2\\%&lt;/math>&lt;/td>\n&lt;td colspan=\"2\">&lt;math>\\frac{500-241}{500} = 51.8\\%&lt;/math>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td># Steps&lt;/td>\n&lt;td>5.3&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>6.8&lt;/td>\n&lt;td>6.0&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>8.6&lt;/td>\n&lt;td>7.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 5&lt;/math> steps&lt;/td>\n&lt;td>61.8%&lt;/td>\n&lt;td>57.5%&lt;/td>\n&lt;td>73.6%&lt;/td>\n&lt;td>70.4%&lt;/td>\n&lt;td>92.6%&lt;/td>\n&lt;td>92.3%&lt;/td>\n&lt;td>92.5%&lt;/td>\n&lt;td>81.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 10&lt;/math> steps&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>1.6%&lt;/td>\n&lt;td>17.8%&lt;/td>\n&lt;td>8.9%&lt;/td>\n&lt;td>33.9%&lt;/td>\n&lt;td>27.1%&lt;/td>\n&lt;td>29.2%&lt;/td>\n&lt;td>21.6%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% &lt;math>\\geq 15&lt;/math> steps&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>0.0%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>2.0%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>8.8%&lt;/td>\n&lt;td>7.5%&lt;/td>\n&lt;td>4.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/3 agreement&lt;/td>\n&lt;td>66.7%&lt;/td>\n&lt;td>95.9%&lt;/td>\n&lt;td>59.4%&lt;/td>\n&lt;td>91.9%&lt;/td>\n&lt;td>52.8%&lt;/td>\n&lt;td>85.0%&lt;/td>\n&lt;td>47.8%&lt;/td>\n&lt;td>80.1%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/4 agreement&lt;/td>\n&lt;td>21.3%&lt;/td>\n&lt;td>3.6%&lt;/td>\n&lt;td>24.4%&lt;/td>\n&lt;td>4.7%&lt;/td>\n&lt;td>24.1%&lt;/td>\n&lt;td>9.1%&lt;/td>\n&lt;td>25.6%&lt;/td>\n&lt;td>13.7%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>% 3/5 agreement&lt;/td>\n&lt;td>12.1%&lt;/td>\n&lt;td>0.5%&lt;/td>\n&lt;td>16.2%&lt;/td>\n&lt;td>3.4%&lt;/td>\n&lt;td>23.1%&lt;/td>\n&lt;td>5.9%&lt;/td>\n&lt;td>26.6%&lt;/td>\n&lt;td>6.2%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nThe resulting PROCESSBENCH has four subsets, consisting of 3,400 test cases in total. The detailed statistics are shown in Table 2 and Table 4 (in Appendix B), and we also plot in Figure 3 the distribution of error positions in erroneous samples. In general, the more challenging the problems, the more solution steps the models generate, and incorrect solutions usually contain more steps than correct ones. However, across all four subsets, a large proportion of errors occur in the earlier steps, such as steps 0-3 in GSM8K and MATH, and steps 1-5 in OlympiadBench and Omni-MATH.\n\nFigure 3: Distribution of error positions (indexed from 0; truncated to 16 for better visualization), corresponding to the *label* field as shown in Figure 2.\n\nIt is noteworthy that while we have intentionally controlled an equal number of solutions with incorrect and correct final answers (200 each for GSM8K and 500 each for other subsets), the annotationFigure 4: Process error ratios per models and subsets, computed as the proportions of samples annotated as *erroneous* among all the samples with *correct final answers* (same as in Table 2). The models used for solution generation slightly vary across different subsets, see Table 4 in Appendix B. We observe that no particular models have notably higher process error rates, while **the process error rates are consistently higher on more difficult problems for all the models.**\n\nresults reveal quite different numbers. Specifically, in the more challenging subsets like OlympiadBench and Omni-MATH, a larger proportion of solutions with correct final answers still contain erroneous steps. For instance, in OlympiadBench,  $\\frac{500-339}{500} = 32.2\\%$  of solutions with correct final answers are found to contain process errors, while in Omni-MATH this proportion is even higher ( $\\frac{500-241}{500} = 51.8\\%$ ). In contrast, these proportions in GSM8K and MATH are  $\\frac{200-193}{200} = 3.5\\%$  and  $\\frac{500-406}{500} = 18.8\\%$ , respectively. In Figure 4, for each model used for solution generation, we plot the ratio of samples with *erroneous reasoning steps* (i.e., annotated as erroneous) among all the samples with *correct final answers*. We observe that the process error rates are consistently higher on more difficult problems. To our knowledge, our work is **the first to present evidence that on more challenging math problems, current language models are more prone to making process errors even when reaching correct final answers.** This also suggests the underlying limitation of rule-based RL in mathematical reasoning (i.e., rewarding merely according to the correctness of final answers) and further highlights the significance of identifying errors in the reasoning process.\n\n## 4 Evaluation\n\n### 4.1 Setup\n\nFor each subset of PROCESSBENCH, we calculate the accuracies on erroneous and correct samples, respectively, and additionally compute their harmonic mean as the **F1 score**. We primarily refer to F1 scores to compare model performance, as it balances model behaviors between being overly critical and being incapable of identifying errors.\n\nWe consider two types of models in the evaluation on PROCESSBENCH: *process reward models (PRMs)* and *critic models*.\n\n**Process Reward Models (PRMs)** As a recently focal topic, PRMs are proposed to assess and supervise the intermediate steps in language models’ reasoning process (Lightman et al., 2023), thus naturally falling in the scope of our research. In practice, PRMs are typically trained using the process labels for intermediate reasoning steps, outputting either the correctness prediction or a scalar score for each reasoning step during inference. Previous research usually evaluates PRMs based on their improvement in the Best-of-N (BoN) performance of another language model that generates solutions. However, this lacks a finer-grained inspection on their process assessment abilities, and the evaluation reliability can be heavily affected by the underlying solution generation model.\n\nOur evaluation includes several open-source PRMs: (1) Math-Shepherd (Wang et al., 2024), which obtains the process label for each step via estimating the empirical probability of this step leading to the correct final answer. (2) Two LLaMA-3.1-based PRMs from Xiong et al. (2024b), which roughly follow the training methodology of Math-Shepherd but differ in the solution generation models and optimization objectives. (3) Two Qwen2.5-Math-based PRMs recently released by Skywork (2024). (4) We also train a PRM by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K dataset, namely Qwen2.5-Math-7B-PRM800K. See Appendix C for its training details.For the (1)(2)(4) PRMs, we extract the earliest erroneous step from their correctness predictions for reasoning steps. For the (3) PRMs, which produce scalar scores for each reasoning step, we first transform these scores into binary correctness predictions (using a threshold above which steps are considered as correct), and then extract the earliest erroneous step as we do for (1)(2)(4). The transformation threshold is determined as the one giving the highest F1 score on the GSM8K subset.\n\n**Critic Models** Critic models aim to provide feedback and critique to model-generated texts, non-inclusively including verification, reflection, and correction or refinement. They have demonstrated promising utility in achieving scalable oversight (Saunders et al., 2022; McAleese et al., 2024).\n\nTraining critic models for specific domains typically requires significant and specialized effort, which is out of the scope of our work. Instead, we are more interested in the critique capabilities of *general language models*. The task definition (§ 3.1) of PROCESSBENCH enables us to apply simple prompt engineering to repurpose general language models as critic models. We show in Figure 7 in Appendix E the prompt template we implement for our evaluation. Specifically, models are prompted to return the index of the paragraph where the earliest error occurs as the *final answer*, similar to the conventional evaluation protocol for mathematical reasoning tasks (Cobbe et al., 2021; Hendrycks et al., 2021; Yang et al., 2024b).\n\nOur evaluation includes the widely-used Qwen2 (Yang et al., 2024a), Qwen2.5 (Qwen, 2024a), Qwen2.5-Math (Yang et al., 2024b), Qwen2.5-Coder (Hui et al., 2024), and LLaMA-3 (Dubey et al., 2024) series open-source models, as well as the recently released QwQ-32B-Preview reasoning model (Qwen, 2024b). We also evaluate the proprietary GPT-4o (Hurst et al., 2024) and o1-mini (OpenAI, 2024) models. We report the performance of open-source models under majority voting over eight samplings, while we also report their performance under greedy decoding in Table 9 in Appendix F. For the proprietary model GPT-4o, we report the results under greedy decoding, while for o1-mini, we report the results under single sampling as its API does not support customized decoding parameters.\n\nTable 3: Evaluation results on PROCESSBENCH. We report the F1 score of the respective accuracies on erroneous and correct samples. See Table 5 and Table 7 for breakdown of evaluation results.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad-Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Average&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>68.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>56.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>56.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>★ QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>71.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 1799
    }
  },
  "sourceToolAssistantUUID": "f419f2d2-595b-497d-af35-e8c36d21a52c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "17350b97-c9f5-40cb-81c2-0ca2fc83b432",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Tool call

_source line 47 · 2026-05-27T16:07:54.569Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WSYLJcycMJTGbzBtRGCbUG`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/toolu_01JLaPNUPbKr3rUPydFkfJVF.txt",
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17350b97-c9f5-40cb-81c2-0ca2fc83b432",
  "isSidechain": false,
  "requestId": "req_011CbTMxJPiN2HysUtbcPLiG",
  "type": "assistant",
  "uuid": "6cb09dd1-04e2-4337-86cc-397712ff379d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJDRiA9WqwABJJq5sDqEut",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11153,
      "cache_read_input_tokens": 17719,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 17719,
          "cache_creation_input_tokens": 11153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11153
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

_source line 48 · 2026-05-27T16:07:54.867Z_

<details><summary>↩ Tool result · `toolu_01WSYLJcycMJTGbzBtRGCbUG`</summary>

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
1300	&lt;td>2.1&lt;/td>
1301	&lt;td>99.1&lt;/td>
1302	&lt;td>4.1&lt;/td>
1303	&lt;td>0.9&lt;/td>
1304	&lt;td>98.3&lt;/td>
1305	&lt;td>1.8&lt;/td>
1306	&lt;/tr>
1307	&lt;tr>
1308	&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>
1309	&lt;td>20.7&lt;/td>
1310	&lt;td>94.1&lt;/td>
1311	&lt;td>34.0&lt;/td>
1312	&lt;td>15.9&lt;/td>
1313	&lt;td>94.2&lt;/td>
1314	&lt;td>27.3&lt;/td>
1315	&lt;/tr>
1316	&lt;tr>
1317	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
1318	&lt;td>33.4&lt;/td>
1319	&lt;td>91.2&lt;/td>
1320	&lt;td>48.9&lt;/td>
1321	&lt;td>31.5&lt;/td>
1322	&lt;td>87.6&lt;/td>
1323	&lt;td>46.3&lt;/td>
1324	&lt;/tr>
1325	&lt;tr>
1326	&lt;td>Qwen2-7B-Instruct&lt;/td>
1327	&lt;td>22.4&lt;/td>
1328	&lt;td>10.9&lt;/td>
1329	&lt;td>14.7&lt;/td>
1330	&lt;td>20.0&lt;/td>
1331	&lt;td>8.7&lt;/td>
1332	&lt;td>12.1&lt;/td>
1333	&lt;/tr>
1334	&lt;tr>
1335	&lt;td>Qwen2-72B-Instruct&lt;/td>
1336	&lt;td>34.0&lt;/td>
1337	&lt;td>55.2&lt;/td>
1338	&lt;td>42.1&lt;/td>
1339	&lt;td>32.3&lt;/td>
1340	&lt;td>53.1&lt;/td>
1341	&lt;td>40.2&lt;/td>
1342	&lt;/tr>
1343	&lt;tr>
1344	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
1345	&lt;td>26.5&lt;/td>
1346	&lt;td>33.9&lt;/td>
1347	&lt;td>29.7&lt;/td>
1348	&lt;td>26.2&lt;/td>
1349	&lt;td>28.6&lt;/td>
1350	&lt;td>27.4&lt;/td>
1351	&lt;/tr>
1352	&lt;tr>
1353	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
1354	&lt;td>31.5&lt;/td>
1355	&lt;td>78.8&lt;/td>
1356	&lt;td>45.0&lt;/td>
1357	&lt;td>28.3&lt;/td>
1358	&lt;td>76.3&lt;/td>
1359	&lt;td>41.3&lt;/td>
1360	&lt;/tr>
1361	&lt;tr>
1362	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
1363	&lt;td>25.3&lt;/td>
1364	&lt;td>95.9&lt;/td>
1365	&lt;td>40.0&lt;/td>
1366	&lt;td>24.1&lt;/td>
1367	&lt;td>92.5&lt;/td>
1368	&lt;td>38.3&lt;/td>
1369	&lt;/tr>
1370	&lt;tr>
1371	&lt;td>Qwen2.5-72B-Instruct&lt;/td>
1372	&lt;td>38.7&lt;/td>
1373	&lt;td>92.6&lt;/td>
1374	&lt;td>54.6&lt;/td>
1375	&lt;td>36.6&lt;/td>
1376	&lt;td>90.9&lt;/td>
1377	&lt;td>52.2&lt;/td>
1378	&lt;/tr>
1379	&lt;tr>
1380	&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>
1381	&lt;td>&lt;b>61.4&lt;/b>&lt;/td>
1382	&lt;td>&lt;b>54.6&lt;/b>&lt;/td>
1383	&lt;td>&lt;b>57.8&lt;/b>&lt;/td>
1384	&lt;td>&lt;b>55.7&lt;/b>&lt;/td>
1385	&lt;td>&lt;b>68.0&lt;/b>&lt;/td>
1386	&lt;td>&lt;b>61.3&lt;/b>&lt;/td>
1387	&lt;/tr>
1388	&lt;tr>
1389	&lt;td colspan="7" style="text-align: center;">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>
1390	&lt;/tr>
1391	&lt;tr>
1392	&lt;td>GPT-4o-0806&lt;/td>
1393	&lt;td>45.8&lt;/td>
1394	&lt;td>58.4&lt;/td>
1395	&lt;td>51.4&lt;/td>
1396	&lt;td>45.2&lt;/td>
1397	&lt;td>65.6&lt;/td>
1398	&lt;td>53.5&lt;/td>
1399	&lt;/tr>
1400	&lt;tr>
1401	&lt;td>o1-mini&lt;/td>
1402	&lt;td>80.2&lt;/td>
1403	&lt;td>95.6&lt;/td>
1404	&lt;td>87.2&lt;/td>
1405	&lt;td>74.8&lt;/td>
1406	&lt;td>91.7&lt;/td>
1407	&lt;td>82.4&lt;/td>
1408	&lt;/tr>
1409	&lt;/tbody>
1410	&lt;/table>
1411	
1412	Table 8: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the OlympiadBench and Omni-MATH subsets, which are slightly higher than those in Table 7 that all adopt the threshold selected on the GSM8K subset.
1413	
1414	&lt;table border="1">
1415	&lt;thead>
1416	&lt;tr>
1417	&lt;th rowspan="2">Model&lt;/th>
1418	&lt;th colspan="3">OlympiadBench&lt;/th>
1419	&lt;th colspan="3">Omni-MATH&lt;/th>
1420	&lt;/tr>
1421	&lt;tr>
1422	&lt;th>error&lt;/th>
1423	&lt;th>correct&lt;/th>
1424	&lt;th>F1&lt;/th>
1425	&lt;th>error&lt;/th>
1426	&lt;th>correct&lt;/th>
1427	&lt;th>F1&lt;/th>
1428	&lt;/tr>
1429	&lt;/thead>
1430	&lt;tbody>
1431	&lt;tr>
1432	&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>
1433	&lt;td>15.3&lt;/td>
1434	&lt;td>47.5&lt;/td>
1435	&lt;td>23.1&lt;/td>
1436	&lt;td>14.0&lt;/td>
1437	&lt;td>58.5&lt;/td>
1438	&lt;td>22.6&lt;/td>
1439	&lt;/tr>
1440	&lt;tr>
1441	&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>
1442	&lt;td>18.9&lt;/td>
1443	&lt;td>48.1&lt;/td>
1444	&lt;td>27.1&lt;/td>
1445	&lt;td>14.4&lt;/td>
1446	&lt;td>58.1&lt;/td>
1447	&lt;td>23.1&lt;/td>
1448	&lt;/tr>
1449	&lt;/tbody>
1450	&lt;/table>Table 9: Breakdown of evaluation results of the open-source language models (prompted as critic models) using *greedy decoding*.
1451	
1452	&lt;table border="1">
1453	&lt;thead>
1454	&lt;tr>
1455	&lt;th rowspan="2">Model&lt;/th>
1456	&lt;th colspan="3">GSM8K&lt;/th>
1457	&lt;th colspan="3">MATH&lt;/th>
1458	&lt;/tr>
1459	&lt;tr>
1460	&lt;th>error&lt;/th>
1461	&lt;th>correct&lt;/th>
1462	&lt;th>F1&lt;/th>
1463	&lt;th>error&lt;/th>
1464	&lt;th>correct&lt;/th>
1465	&lt;th>F1&lt;/th>
1466	&lt;/tr>
1467	&lt;/thead>
1468	&lt;tbody>
1469	&lt;tr>
1470	&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>
1471	&lt;td>28.5&lt;/td>
1472	&lt;td>9.3&lt;/td>
1473	&lt;td>14.1&lt;/td>
1474	&lt;td>20.9&lt;/td>
1475	&lt;td>5.7&lt;/td>
1476	&lt;td>8.9&lt;/td>
1477	&lt;/tr>
1478	&lt;tr>
1479	&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>
1480	&lt;td>39.6&lt;/td>
1481	&lt;td>93.8&lt;/td>
1482	&lt;td>55.7&lt;/td>
1483	&lt;td>21.9&lt;/td>
1484	&lt;td>72.2&lt;/td>
1485	&lt;td>33.6&lt;/td>
1486	&lt;/tr>
1487	&lt;tr>
1488	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
1489	&lt;td>36.7&lt;/td>
1490	&lt;td>17.1&lt;/td>
1491	&lt;td>23.3&lt;/td>
1492	&lt;td>23.6&lt;/td>
1493	&lt;td>7.9&lt;/td>
1494	&lt;td>11.8&lt;/td>
1495	&lt;/tr>
1496	&lt;tr>
1497	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
1498	&lt;td>57.5&lt;/td>
1499	&lt;td>77.7&lt;/td>
1500	&lt;td>66.1&lt;/td>
1501	&lt;td>37.7&lt;/td>
1502	&lt;td>53.9&lt;/td>
1503	&lt;td>44.4&lt;/td>
1504	&lt;/tr>
1505	&lt;tr>
1506	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
1507	&lt;td>66.2&lt;/td>
1508	&lt;td>96.9&lt;/td>
1509	&lt;td>78.6&lt;/td>
1510	&lt;td>38.4&lt;/td>
1511	&lt;td>93.1&lt;/td>
1512	&lt;td>54.4&lt;/td>
1513	&lt;/tr>
1514	&lt;tr>
1515	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
1516	&lt;td>14.5&lt;/td>
1517	&lt;td>99.0&lt;/td>
1518	&lt;td>25.3&lt;/td>
1519	&lt;td>13.1&lt;/td>
1520	&lt;td>94.8&lt;/td>
1521	&lt;td>23.1&lt;/td>
1522	&lt;/tr>
1523	&lt;tr>
1524	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
1525	&lt;td>45.9&lt;/td>
1526	&lt;td>96.4&lt;/td>
1527	&lt;td>62.2&lt;/td>
1528	&lt;td>34.3&lt;/td>
1529	&lt;td>94.6&lt;/td>
1530	&lt;td>50.4&lt;/td>
1531	&lt;/tr>
1532	&lt;tr>
1533	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
1534	&lt;td>0.0&lt;/td>
1535	&lt;td>20.2&lt;/td>
1536	&lt;td>0.0&lt;/td>
1537	&lt;td>0.2&lt;/td>
1538	&lt;td>25.6&lt;/td>
1539	&lt;td>0.3&lt;/td>
1540	&lt;/tr>
1541	&lt;tr>
1542	&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>
1543	&lt;td>20.3&lt;/td>
1544	&lt;td>99.0&lt;/td>
1545	&lt;td>33.7&lt;/td>
1546	&lt;td>15.2&lt;/td>
1547	&lt;td>96.1&lt;/td>
1548	&lt;td>26.2&lt;/td>
1549	&lt;/tr>
1550	&lt;tr>
1551	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
1552	&lt;td>50.7&lt;/td>
1553	&lt;td>93.8&lt;/td>
1554	&lt;td>65.8&lt;/td>
1555	&lt;td>39.7&lt;/td>
1556	&lt;td>88.2&lt;/td>
1557	&lt;td>54.8&lt;/td>
1558	&lt;/tr>
1559	&lt;tr>
1560	&lt;td>Qwen2-7B-Instruct&lt;/td>
1561	&lt;td>28.0&lt;/td>
1562	&lt;td>0.0&lt;/td>
1563	&lt;td>0.0&lt;/td>
1564	&lt;td>19.0&lt;/td>
1565	&lt;td>5.2&lt;/td>
1566	&lt;td>8.1&lt;/td>
1567	&lt;/tr>
1568	&lt;tr>
1569	&lt;td>Qwen2-72B-Instruct&lt;/td>
1570	&lt;td>56.5&lt;/td>
1571	&lt;td>82.4&lt;/td>
1572	&lt;td>67.0&lt;/td>
1573	&lt;td>35.5&lt;/td>
1574	&lt;td>66.7&lt;/td>
1575	&lt;td>46.4&lt;/td>
1576	&lt;/tr>
1577	&lt;tr>
1578	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
1579	&lt;td>36.7&lt;/td>
1580	&lt;td>66.3&lt;/td>
1581	&lt;td>47.3&lt;/td>
1582	&lt;td>23.7&lt;/td>
1583	&lt;td>63.8&lt;/td>
1584	&lt;td>34.6&lt;/td>
1585	&lt;/tr>
1586	&lt;tr>
1587	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
1588	&lt;td>47.8&lt;/td>
1589	&lt;td>93.8&lt;/td>
1590	&lt;td>63.3&lt;/td>
1591	&lt;td>40.4&lt;/td>
1592	&lt;td>86.9&lt;/td>
1593	&lt;td>55.2&lt;/td>
1594	&lt;/tr>
1595	&lt;tr>
1596	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
1597	&lt;td>43.0&lt;/td>
1598	&lt;td>97.9&lt;/td>
1599	&lt;td>59.8&lt;/td>
1600	&lt;td>33.3&lt;/td>
1601	&lt;td>95.6&lt;/td>
1602	&lt;td>49.4&lt;/td>
1603	&lt;/tr>
1604	&lt;tr>
1605	&lt;td>Qwen2.5-72B-Instruct&lt;/td>
1606	&lt;td>61.4&lt;/td>
1607	&lt;td>98.4&lt;/td>
1608	&lt;td>75.6&lt;/td>
1609	&lt;td>45.3&lt;/td>
1610	&lt;td>91.9&lt;/td>
1611	&lt;td>60.7&lt;/td>
1612	&lt;/tr>
1613	&lt;tr>
1614	&lt;td>QwQ-32B-Preview&lt;/td>
1615	&lt;td>74.9&lt;/td>
1616	&lt;td>67.4&lt;/td>
1617	&lt;td>70.9&lt;/td>
1618	&lt;td>58.6&lt;/td>
1619	&lt;td>54.2&lt;/td>
1620	&lt;td>56.3&lt;/td>
1621	&lt;/tr>
1622	&lt;/tbody>
1623	&lt;/table>
1624	
1625	  
1626	
1627	&lt;table border="1">
1628	&lt;thead>
1629	&lt;tr>
1630	&lt;th rowspan="2">Model&lt;/th>
1631	&lt;th colspan="3">OlympiadBench&lt;/th>
1632	&lt;th colspan="3">Omni-MATH&lt;/th>
1633	&lt;/tr>
1634	&lt;tr>
1635	&lt;th>error&lt;/th>
1636	&lt;th>correct&lt;/th>
1637	&lt;th>F1&lt;/th>
1638	&lt;th>error&lt;/th>
1639	&lt;th>correct&lt;/th>
1640	&lt;th>F1&lt;/th>
1641	&lt;/tr>
1642	&lt;/thead>
1643	&lt;tbody>
1644	&lt;tr>
1645	&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>
1646	&lt;td>17.2&lt;/td>
1647	&lt;td>0.6&lt;/td>
1648	&lt;td>1.1&lt;/td>
1649	&lt;td>17.3&lt;/td>
1650	&lt;td>4.1&lt;/td>
1651	&lt;td>6.7&lt;/td>
1652	&lt;/tr>
1653	&lt;tr>
1654	&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>
1655	&lt;td>20.9&lt;/td>
1656	&lt;td>41.6&lt;/td>
1657	&lt;td>27.8&lt;/td>
1658	&lt;td>20.9&lt;/td>
1659	&lt;td>50.2&lt;/td>
1660	&lt;td>29.6&lt;/td>
1661	&lt;/tr>
1662	&lt;tr>
1663	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
1664	&lt;td>19.1&lt;/td>
1665	&lt;td>5.6&lt;/td>
1666	&lt;td>8.7&lt;/td>
1667	&lt;td>17.1&lt;/td>
1668	&lt;td>10.0&lt;/td>
1669	&lt;td>12.6&lt;/td>
1670	&lt;/tr>
1671	&lt;tr>
1672	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
1673	&lt;td>32.8&lt;/td>
1674	&lt;td>32.4&lt;/td>
1675	&lt;td>32.6&lt;/td>
1676	&lt;td>29.5&lt;/td>
1677	&lt;td>39.0&lt;/td>
1678	&lt;td>33.6&lt;/td>
1679	&lt;/tr>
1680	&lt;tr>
1681	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
1682	&lt;td>30.9&lt;/td>
1683	&lt;td>90.0&lt;/td>
1684	&lt;td>46.0&lt;/td>
1685	&lt;td>27.1&lt;/td>
1686	&lt;td>86.3&lt;/td>
1687	&lt;td>41.3&lt;/td>
1688	&lt;/tr>
1689	&lt;tr>
1690	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
1691	&lt;td>6.4&lt;/td>
1692	&lt;td>79.1&lt;/td>
1693	&lt;td>11.8&lt;/td>
1694	&lt;td>4.7&lt;/td>
1695	&lt;td>78.0&lt;/td>
1696	&lt;td>8.9&lt;/td>
1697	&lt;/tr>
1698	&lt;tr>
1699	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
1700	&lt;td>17.2&lt;/td>
1701	&lt;td>95.0&lt;/td>
1702	&lt;td>29.2&lt;/td>
1703	&lt;td>18.3&lt;/td>
1704	&lt;td>93.4&lt;/td>
1705	&lt;td>30.6&lt;/td>
1706	&lt;/tr>
1707	&lt;tr>
1708	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
1709	&lt;td>0.0&lt;/td>
1710	&lt;td>13.3&lt;/td>
1711	&lt;td>0.0&lt;/td>
1712	&lt;td>0.0&lt;/td>
1713	&lt;td>27.8&lt;/td>
1714	&lt;td>0.0&lt;/td>
1715	&lt;/tr>
1716	&lt;tr>
1717	&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>
1718	&lt;td>9.1&lt;/td>
1719	&lt;td>95.6&lt;/td>
1720	&lt;td>16.6&lt;/td>
1721	&lt;td>6.2&lt;/td>
1722	&lt;td>95.9&lt;/td>
1723	&lt;td>11.6&lt;/td>
1724	&lt;/tr>
1725	&lt;tr>
1726	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
1727	&lt;td>31.8&lt;/td>
1728	&lt;td>86.7&lt;/td>
1729	&lt;td>46.5&lt;/td>
1730	&lt;td>31.5&lt;/td>
1731	&lt;td>84.6&lt;/td>
1732	&lt;td>45.9&lt;/td>
1733	&lt;/tr>
1734	&lt;tr>
1735	&lt;td>Qwen2-7B-Instruct&lt;/td>
1736	&lt;td>14.1&lt;/td>
1737	&lt;td>2.9&lt;/td>
1738	&lt;td>4.9&lt;/td>
1739	&lt;td>13.7&lt;/td>
1740	&lt;td>2.9&lt;/td>
1741	&lt;td>4.8&lt;/td>
1742	&lt;/tr>
1743	&lt;tr>
1744	&lt;td>Qwen2-72B-Instruct&lt;/td>
1745	&lt;td>33.4&lt;/td>
1746	&lt;td>48.1&lt;/td>
1747	&lt;td>39.4&lt;/td>
1748	&lt;td>30.4&lt;/td>
1749	&lt;td>48.1&lt;/td>
1750	&lt;td>37.3&lt;/td>
1751	&lt;/tr>
1752	&lt;tr>
1753	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
1754	&lt;td>25.4&lt;/td>
1755	&lt;td>46.0&lt;/td>
1756	&lt;td>32.7&lt;/td>
1757	&lt;td>26.1&lt;/td>
1758	&lt;td>43.6&lt;/td>
1759	&lt;td>32.6&lt;/td>
1760	&lt;/tr>
1761	&lt;tr>
1762	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
1763	&lt;td>30.9&lt;/td>
1764	&lt;td>76.4&lt;/td>
1765	&lt;td>44.0&lt;/td>
1766	&lt;td>27.0&lt;/td>
1767	&lt;td>72.6&lt;/td>
1768	&lt;td>39.4&lt;/td>
1769	&lt;/tr>
1770	&lt;tr>
1771	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
1772	&lt;td>22.4&lt;/td>
1773	&lt;td>90.0&lt;/td>
1774	&lt;td>35.9&lt;/td>
1775	&lt;td>22.4&lt;/td>
1776	&lt;td>87.6&lt;/td>
1777	&lt;td>35.7&lt;/td>
1778	&lt;/tr>
1779	&lt;tr>
1780	&lt;td>Qwen2.5-72B-Instruct&lt;/td>
1781	&lt;td>33.7&lt;/td>
1782	&lt;td>88.5&lt;/td>
1783	&lt;td>48.9&lt;/td>
1784	&lt;td>33.7&lt;/td>
1785	&lt;td>88.4&lt;/td>
1786	&lt;td>48.8&lt;/td>
1787	&lt;/tr>
1788	&lt;tr>
1789	&lt;td>QwQ-32B-Preview&lt;/td>
1790	&lt;td>37.8&lt;/td>
1791	&lt;td>31.9&lt;/td>
1792	&lt;td>34.6&lt;/td>
1793	&lt;td>29.5&lt;/td>
1794	&lt;td>41.9&lt;/td>
1795	&lt;td>34.6&lt;/td>
1796	&lt;/tr>
1797	&lt;/tbody>
1798	&lt;/table>
1799	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cb09dd1-04e2-4337-86cc-397712ff379d",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "a7afb7c4-539d-4cd8-ab55-09f0dbd50bd6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-idea-review/622fde7e-49a1-441f-a25d-d298deae6922/tool-results/toolu_01JLaPNUPbKr3rUPydFkfJVF.txt",
      "content": "&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Alright, I've got this math problem to solve and a solution provided, but I need to review it paragraph by paragraph to find any errors. The problem is to find the integer  $n$ , where  $0 \\leq n \\leq 180$ , such that  $\\cos n^\\circ = \\cos 568^\\circ$ . Let's dive into the solution step by step.\n\n**Paragraph 0:\\*\\***\n\nThe solution starts by recalling that the cosine function has a period of  $360^\\circ$ , which means  $\\cos \\theta = \\cos (\\theta + 360k)$  for any integer  $k$ . That's correct. Cosine repeats every  $360^\\circ$ , so adding or subtracting multiples of  $360^\\circ$  doesn't change the value of the cosine.\n\n**Paragraph 1:\\*\\***\n\nGiven  $\\cos 568^\\circ$ , the solution reduces this angle by subtracting  $360^\\circ$  to get  $208^\\circ$ , since  $568^\\circ - 360^\\circ = 208^\\circ$ . So,  $\\cos 568^\\circ = \\cos 208^\\circ$ . That seems right.  $208^\\circ$  is within one cycle of  $0^\\circ$  to  $360^\\circ$ .\n\n**Paragraph 2:\\*\\***\n\nNow, the solution mentions that cosine is symmetric about  $180^\\circ$ , and states that  $\\cos \\theta = \\cos (180^\\circ - \\theta)$ . Wait a minute, is that correct? Let me think about this. Actually, cosine is symmetric about the y-axis, and the identity  $\\cos \\theta = \\cos (-\\theta)$  reflects that. The identity  $\\cos \\theta = \\cos (360^\\circ - \\theta)$  shows the symmetry about  $360^\\circ$ , but symmetry about  $180^\\circ$  isn't directly related to cosine's even property.\n\nHmm, maybe I need to recall some trigonometric identities here. Let's see, the cosine of an angle in standard position is equal to the cosine of its reference angle, but with a sign depending on the quadrant.  $208^\\circ$  is in the third quadrant, where cosine is negative.\n\nAlternatively, there's the identity  $\\cos (180^\\circ + \\theta) = -\\cos \\theta$ , but that's not directly applicable here.\n\nLet me double-check the symmetry properties. Cosine is an even function, meaning  $\\cos (-\\theta) = \\cos \\theta$ , which shows symmetry about the y-axis. The identity  $\\cos (360^\\circ - \\theta) = \\cos \\theta$  shows symmetry every full cycle.\n\nBut the statement  $\\cos \\theta = \\cos (180^\\circ - \\theta)$  isn't generally true. Let's test it with a specific angle. For example,  $\\theta = 30^\\circ$ :  $\\cos 30^\\circ = \\sqrt{3}/2$ , and  $\\cos (180^\\circ - 30^\\circ) = \\cos 150^\\circ = -\\sqrt{3}/2$ . These are not equal; in fact, they're negatives of each other.\n\nSo, it seems there's an error in this paragraph. The correct identity involving  $180^\\circ$  is  $\\cos (180^\\circ - \\theta) = -\\cos \\theta$ , not  $\\cos \\theta$ .\n\nTherefore, the earliest error occurs in paragraph 2.\n\n**Final Answer:**\n\n$\\boxed{2}$\n\nFigure 5: Critique generated by QwQ-32B-Preview for the test case in Figure 2.\n\n## 4.2 Results\n\nWe present the evaluation results in Table 3. Our observations are summarized as follows:\n\n**Generalization Across Difficulty** From GSM8K and MATH to OlympiadBench and Omni-MATH, with the increased difficulty of math problems, we observe a consistent performance decline for all the models, which suggests the common challenge of both PRMs and critic models in generalization abilities.\n\n**Comparison Between PRMs and Critic Models** We find that existing PRMs typically underperform the top prompt-driven critic models even on the simpler GSM8K and MATH subsets, suggesting that these PRMs struggle to indicate the correctness of the intermediate steps in mathematical reasoning. Moreover, when moving toward the more challenging OlympiadBench and Omni-MATH subsets, PRMs suffer from a more notable performance decline than critic models. This raises our concerns about the **generalization abilities and scalability of the current data synthesis methodologies used to build PRMs**. More specifically, current methodologies, as exemplified by Math-Shepherd (Wang et al., 2024), measure the correctness of an intermediate step by estimating the empirical probability of this step leading to the correct final answer. This kind of approach has two intuitive major issues: (1) The process labels heavily depend on the language model used to generate solutions (i.e., highly “on-policy”), which---\n\nwould naturally fail to indicate the correctness of reasoning steps generated by other models. (2) As demonstrated in § 3.3, current language models are prone to making process errors even when reaching correct final answers. This could substantially invalidate the estimated process labels, particularly on the more challenging math problems. In contrast, **Qwen2.5-Math-7B-PRM800K**, which is straightforwardly fine-tuned on the *fully human-annotated* PRM800K training set, exhibits significantly stronger performance and generalization ability than other PRMs.\n\n**Comparison Among Critic Models** Compared to PRMs, critic models can benefit from separate reasoning processes when critiquing solutions, as they can “think” more before indicating the correctness of each solution step, which leads to their better performance in this error identification task. Within the same model family, the error identification performance favorably scales with increased model sizes. Notably, the recently released reasoning model **QwQ-32B-Preview** **performs best among the open-source models and is highly competitive with GPT-4o**. It is noteworthy that QwQ-32B-Preview achieves more *balanced accuracies on erroneous and correct samples* (see Table 5 and 7 in Appendix F). We show in Figure 5 an example of critique generated by QwQ-32B-Preview to the test case in Figure 2, which not only identifies the erroneous step but also provides the detailed thinking process and explanation. Nevertheless, QwQ-32B-Preview still lags behind o1-mini, suggesting that although the gap in problem-solving performance is getting closer between open-source and proprietary models, there still exists another large gap in their critique capabilities.\n\n## 5 Conclusion\n\nWe introduce the PROCESSBENCH benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, characterized by its high problem difficulty and solution diversity, large scale, rigorous human annotation, and simple evaluation protocol. Through extensive evaluation with existing process reward models (PRMs) and prompt-driven critic models, we draw two main observations: (1) Existing PRMs typically underperform critic models in identifying erroneous reasoning steps, and struggle more to generalize to challenging math problems. (2) Open-source language models, as exemplified by QwQ-32B-Preview, have demonstrated critique capabilities competitive with the proprietary model GPT-4o, yet still lag behind the reasoning-specialized o1-mini model. We envision PROCESSBENCH as a cornerstone testbed for advancing automated reasoning process assessment, a critical step toward achieving scalable oversight of language models.\n\n**Limitations** Despite our best efforts throughout the entire benchmark construction process (§ 3.2), PROCESSBENCH may still contain inaccurate labels of error locations, particularly for the more challenging Olympiad-level math problems. Additionally, the solutions discarded in human annotation (§ 3.2) may involve the particularly challenging problems, which could bias the problem distribution in PROCESSBENCH, although such samples may have exceeded the capabilities of the human annotators in our annotation task.\n\n## References\n\nDario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. *arXiv preprint arXiv:1606.06565*, 2016.\n\nSamuel R Bowman, Jeeyoon Hyun, Ethan Perez, Edwin Chen, Craig Pettit, Scott Heiner, Kamilę Lukošūtė, Amanda Askell, Andy Jones, Anna Chen, et al. Measuring progress on scalable oversight for large language models. *arXiv preprint arXiv:2211.03540*, 2022.\n\nBoxi Cao, Keming Lu, Xinyu Lu, Jiawei Chen, Mengjie Ren, Hao Xiang, Peilin Liu, Yaojie Lu, Ben He, Xianpei Han, et al. Towards scalable automated alignment of llms: A survey. *arXiv preprint arXiv:2406.01252*, 2024.\n\nKarl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021.\n\nAbhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. *arXiv preprint arXiv:2407.21783*, 2024.\n\nBofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. *arXiv preprint arXiv:2410.07985*, 2024.---\n\nChaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. *arXiv preprint arXiv:2402.14008*, 2024.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring mathematical problem solving with the math dataset. *arXiv preprint arXiv:2103.03874*, 2021.\n\nJie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. *arXiv preprint arXiv:2310.01798*, 2023.\n\nBinyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, et al. Qwen2.5-coder technical report. *arXiv preprint arXiv:2409.12186*, 2024.\n\nAaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.\n\nRyo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. When can LLMs actually correct their own mistakes? a critical survey of self-correction of LLMs. *Transactions of the Association for Computational Linguistics*, 12:1417–1440, 2024. doi: 10.1162/tacl.a\\_00713. URL &lt;https://aclanthology.org/2024.tacl-1.78>.\n\nWoosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In *Proceedings of the 29th Symposium on Operating Systems Principles*, pages 611–626, 2023.\n\nHunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. *arXiv preprint arXiv:2305.20050*, 2023.\n\nZicheng Lin, Zhibin Gou, Tian Liang, Ruilin Luo, Haowei Liu, and Yujiu Yang. Criticbench: Benchmarking llms for critique-correct reasoning. *arXiv preprint arXiv:2402.14809*, 2024.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, and Abhinav Rastogi. Improve mathematical reasoning in language models by automated process supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nNat McAleese, Rai Michael Pokorny, Juan Felipe Ceron Uribe, Evgenia Nitishinskaya, Maja Trebacz, and Jan Leike. Llm critics help catch llm bugs. *arXiv preprint arXiv:2407.00215*, 2024.\n\nOpenAI. Openai o1-mini: Advancing cost-efficient reasoning, 2024. URL &lt;https://openai.com/index/openai-o1-mini-advancing-cost-efficient-reasoning/>.\n\nTeam Qwen. Qwen2.5: A party of foundation models, September 2024a. URL &lt;https://qwenlm.github.io/blog/qwen2.5/>.\n\nTeam Qwen. Qwq: Reflect deeply on the boundaries of the unknown, November 2024b. URL &lt;https://qwenlm.github.io/blog/qwq-32b-preview/>.\n\nWilliam Saunders, Catherine Yeh, Jeff Wu, Steven Bills, Long Ouyang, Jonathan Ward, and Jan Leike. Self-critiquing models for assisting human evaluators. *arXiv preprint arXiv:2206.05802*, 2022.\n\no1 Team Skywork. Skywork-o1 open series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nAlan Wake, Albert Wang, Bei Chen, CX Lv, Chao Li, Chengen Huang, Chenglin Cai, Chujie Zheng, Daniel Cooper, Ethan Dai, et al. Yi-lightning technical report. *arXiv preprint arXiv:2412.01253*, 2024.\n\nPeiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-shepherd: Verify and reinforce LLMs step-by-step without human annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, August 2024. doi: 10.18653/v1/2024.acl-long.510. URL &lt;https://aclanthology.org/2024.acl-long.510>.\n\nWei Xiong, Chengshuai Shi, Jiaming Shen, Aviv Rosenberg, Zhen Qin, Daniele Calandriello, Misha Khalman, Rishabh Joshi, Bilal Piot, Mohammad Saleh, et al. Building math agents with multi-turn iterative preference learning. *arXiv preprint arXiv:2409.02392*, 2024a.---\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An implementation of generative prm. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024b.\n\nAn Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. *arXiv preprint arXiv:2407.10671*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2.5-math technical report: Toward mathematical expert model via self-improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nZihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F Wong, Xiaowei Huang, Qifeng Wang, and Kaizhu Huang. Is your model really a good math reasoner? evaluating mathematical reasoning with checklist. *arXiv preprint arXiv:2407.08733*, 2024.## A Example of Solution Reformattting\n\n&lt;table border=\"1\">\n&lt;tr>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form&lt;/p>\n&lt;math display=\"block\">\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1,&lt;/math>\n&lt;p>where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length.&lt;/p>\n&lt;p>In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>.&lt;/p>\n&lt;p>First, we calculate the distance from the center to each focus:&lt;/p>\n&lt;math display=\"block\">\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4.&lt;/math>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse.&lt;/p>\n&lt;p>Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;td style=\"vertical-align: middle; text-align: center; padding: 0 10px;\">\n&lt;/td>\n&lt;td style=\"vertical-align: top; padding: 10px;\">\n&lt;p>The given equation is of an ellipse in the standard form &lt;math>\\frac{(x-h)^2}{a^2} + \\frac{(y-k)^2}{b^2} = 1&lt;/math>, where &lt;math>(h, k)&lt;/math> is the center of the ellipse, &lt;math>a&lt;/math> is the semi-major axis length, and &lt;math>b&lt;/math> is the semi-minor axis length. In this case, the center of the ellipse is &lt;math>(6, 3)&lt;/math>, &lt;math>a = 5&lt;/math>, and &lt;math>b = 3&lt;/math>.&lt;/p>\n&lt;p>The foci of an ellipse are located along the major axis, which is the line segment connecting the two vertices of the ellipse. The distance from the center of the ellipse to each focus is given by &lt;math>\\sqrt{a^2 - b^2}&lt;/math>. First, we calculate the distance from the center to each focus: &lt;math>\\sqrt{a^2 - b^2} = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4&lt;/math>.&lt;/p>\n&lt;p>Since the major axis of the ellipse is horizontal (because &lt;math>a &gt; b&lt;/math>), the foci are located at a distance of 4 units to the left and right of the center of the ellipse. Therefore, the two foci are at &lt;math>(6 \\pm 4, 3) = (2, 3)&lt;/math> and &lt;math>(10, 3)&lt;/math>.&lt;/p>\n&lt;p>The one with the larger &lt;math>x&lt;/math>-coordinate is &lt;math>(10, 3)&lt;/math>. The answer is: &lt;math>\\boxed{(10, 3)}&lt;/math>.&lt;/p>\n&lt;/td>\n&lt;/tr>\n&lt;/table>\n\nFigure 6: Example of solution reformattting. The left is the original solution (generated by Qwen2-7B-Instruct) and the right is the reformatted one. The problem, coming from the MATH test set, is “The ellipse  $\\frac{(x-6)^2}{25} + \\frac{(y-3)^2}{9} = 1$  has two foci. Find the one with the larger  $x$ -coordinate. Enter your answer as an ordered pair, like  $(2, 1)$ .”\n\n## B Breakdown Statistics of PROCESSBENCH\n\nTable 4: Breakdown statistics of PROCESSBENCH.  $^\\dagger$ : We encountered a code bug when using Llama-3.1-70B-Instruct and Qwen2.5-72B-Instruct to generate solutions for the MATH problems, thus their counts are all zero in the MATH subset of PROCESSBENCH.  $^\\ddagger$ : For the more challenging OlympiadBench and Omni-MATH problems, we exclude models with lower accuracies from subsequent annotation.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Generator&lt;/th>\n&lt;th colspan=\"2\">GSM8K&lt;/th>\n&lt;th colspan=\"2\">MATH&lt;math>^\\dagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">OlympiadBench&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;th colspan=\"2\">Omni-MATH&lt;math>^\\ddagger&lt;/math>&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>13&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>16&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>23&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>53&lt;/td>\n&lt;td>116&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>131&lt;/td>\n&lt;td>31&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>7&lt;/td>\n&lt;td>28&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>85&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>19&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-1.5B-Instruct&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>36&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>89&lt;/td>\n&lt;td>42&lt;/td>\n&lt;td>63&lt;/td>\n&lt;td>45&lt;/td>\n&lt;td>96&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>9&lt;/td>\n&lt;td>11&lt;/td>\n&lt;td>56&lt;/td>\n&lt;td>51&lt;/td>\n&lt;td>64&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>71&lt;/td>\n&lt;td>25&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-1.5B-Instruct&lt;/td>\n&lt;td>32&lt;/td>\n&lt;td>10&lt;/td>\n&lt;td>31&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>12&lt;/td>\n&lt;td>15&lt;/td>\n&lt;td>62&lt;/td>\n&lt;td>35&lt;/td>\n&lt;td>86&lt;/td>\n&lt;td>37&lt;/td>\n&lt;td>75&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>2&lt;/td>\n&lt;td>21&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>0&lt;/td>\n&lt;td>67&lt;/td>\n&lt;td>38&lt;/td>\n&lt;td>88&lt;/td>\n&lt;td>38&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>8&lt;/td>\n&lt;td>14&lt;/td>\n&lt;td>47&lt;/td>\n&lt;td>49&lt;/td>\n&lt;td>99&lt;/td>\n&lt;td>48&lt;/td>\n&lt;td>103&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>4&lt;/td>\n&lt;td>18&lt;/td>\n&lt;td>39&lt;/td>\n&lt;td>59&lt;/td>\n&lt;td>81&lt;/td>\n&lt;td>43&lt;/td>\n&lt;td>92&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>207&lt;/td>\n&lt;td>193&lt;/td>\n&lt;td>594&lt;/td>\n&lt;td>406&lt;/td>\n&lt;td>661&lt;/td>\n&lt;td>339&lt;/td>\n&lt;td>759&lt;/td>\n&lt;td>241&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Total&lt;/td>\n&lt;td colspan=\"2\">400&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;td colspan=\"2\">1,000&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>## C Training Details of Qwen2.5-Math-7B-PRM800K\n\nQwen2.5-Math-7B-PRM800K is obtained by fine-tuning Qwen2.5-Math-7B-Instruct on the PRM800K training set. We replace the original language modeling head with a new reward modeling head that outputs binary classification logits. The classification loss is computed at the second line break positions in all the “\\n\\n”. We treat the original 1 and 0 labels in PRM800K as our positive labels, while -1 as negative ones. To eliminate test data contamination, we also remove the PRM800K training samples that have the same problems in PROCESSBENCH. The training was run on eight A100 80GB GPUs.\n\n## D Inference Details\n\nFor solution generation in § 3.2, all the models are set with  $p = 0.9, t = 0.7$ . For majority voting evaluation in § 4, we set  $p = 0.8, t = 0.7, k = 20$  for Qwen2.5-Math-7/72B-Instruct to ensure their normal generation, while all the other models are set with only  $p = 0.9$ . All the inference in the evaluation was run with vLLM (Kwon et al., 2023) on eight A100 80GB GPUs.\n\n## E Prompt Template for Critic Model Evaluation\n\nThe following is a math problem and a solution (split into paragraphs, enclosed with tags and indexed from 0):\n\n[Math Problem]\n\n... (math problem) ...\n\n[Solution]\n\n&lt;paragraph\\_0>\n\n... (paragraph 0 of solution) ...\n\n&lt;/paragraph\\_0>\n\n...\n\n&lt;paragraph\\_n-1>\n\n... (paragraph n-1 of solution) ...\n\n&lt;/paragraph\\_n-1>\n\nYour task is to review and critique the solution paragraph by paragraph. Once you identify an error in a paragraph, return the **index of the paragraph where the earliest error occurs**. Otherwise, return the **index of -1 (which typically denotes \"not found\")**.\n\n**Please put your final answer (i.e., the index) in \\boxed{}.**\n\nFigure 7: Prompt template for critic model evaluation. The **blue texts** indicate the input math problem and the solution (split into paragraphs). The **red texts** describe the required output content and format.## F Supplementary Evaluation Results\n\nTable 5: Breakdown of evaluation results on the GSM8K and MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>24.2&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>21.4&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>37.9&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>&lt;b>70.8&lt;/b>&lt;/td>\n&lt;td>43.8&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>90.1&lt;/td>\n&lt;td>&lt;b>62.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>54.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>44.9&lt;/td>\n&lt;td>90.6&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>30.5&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>45.1&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>95.8&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>&lt;b>88.0&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 6: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the GSM8K and MATH subsets, which are marginally higher than those in Table 5 that all adopt the threshold selected on the GSM8K subset.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>38.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>49.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>44.1&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Table 7: Breakdown of evaluation results on the OlympiadBench and Omni-MATH subsets of PROCESSBENCH. The open-source language models (middle block) are evaluated via *majority voting* over eight samplings.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source Process Reward Models (PRMs)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>15.0&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>8.2&lt;/td>\n&lt;td>43.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Qwen2.5-Math-7B-PRM800K (our trained)&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>29.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>44.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Open-source language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>2.1&lt;/td>\n&lt;td>99.1&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>0.9&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>20.7&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>15.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>26.5&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>28.3&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>24.1&lt;/td>\n&lt;td>92.5&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>38.7&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>90.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>QwQ-32B-Preview&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>68.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>61.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary language models, prompted as Critic Models&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>45.8&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\nTable 8: For the two PRMs from Skywork (2024), we additionally adjust the threshold (§ 4.1) as the one leading to the highest F1 score on each subset (i.e., each subset adopts a respective optimal threshold), which can be viewed as the two PRMs’ *upper bound* performance on PROCESSBENCH. This table presents the results on the OlympiadBench and Omni-MATH subsets, which are slightly higher than those in Table 7 that all adopt the threshold selected on the GSM8K subset.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B (respective thresholds)&lt;/td>\n&lt;td>15.3&lt;/td>\n&lt;td>47.5&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>58.5&lt;/td>\n&lt;td>22.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B (respective thresholds)&lt;/td>\n&lt;td>18.9&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>14.4&lt;/td>\n&lt;td>58.1&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Table 9: Breakdown of evaluation results of the open-source language models (prompted as critic models) using *greedy decoding*.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>28.5&lt;/td>\n&lt;td>9.3&lt;/td>\n&lt;td>14.1&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>5.7&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>55.7&lt;/td>\n&lt;td>21.9&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>17.1&lt;/td>\n&lt;td>23.3&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>7.9&lt;/td>\n&lt;td>11.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>57.5&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>66.1&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>53.9&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>66.2&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>78.6&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>14.5&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>45.9&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>62.2&lt;/td>\n&lt;td>34.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>20.2&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.2&lt;/td>\n&lt;td>25.6&lt;/td>\n&lt;td>0.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>20.3&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>15.2&lt;/td>\n&lt;td>96.1&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>39.7&lt;/td>\n&lt;td>88.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>5.2&lt;/td>\n&lt;td>8.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>67.0&lt;/td>\n&lt;td>35.5&lt;/td>\n&lt;td>66.7&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>23.7&lt;/td>\n&lt;td>63.8&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>47.8&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>63.3&lt;/td>\n&lt;td>40.4&lt;/td>\n&lt;td>86.9&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>59.8&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>49.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>61.4&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>45.3&lt;/td>\n&lt;td>91.9&lt;/td>\n&lt;td>60.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>67.4&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>58.6&lt;/td>\n&lt;td>54.2&lt;/td>\n&lt;td>56.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n  \n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>error&lt;/th>\n&lt;th>correct&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Meta-Llama-3-8B-Instruct&lt;/td>\n&lt;td>17.2&lt;/td>\n&lt;td>0.6&lt;/td>\n&lt;td>1.1&lt;/td>\n&lt;td>17.3&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Meta-Llama-3-70B-Instruct&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>41.6&lt;/td>\n&lt;td>27.8&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>29.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>19.1&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>17.1&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>39.0&lt;/td>\n&lt;td>33.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>30.9&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>86.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>6.4&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;td>11.8&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>8.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>17.2&lt;/td>\n&lt;td>95.0&lt;/td>\n&lt;td>29.2&lt;/td>\n&lt;td>18.3&lt;/td>\n&lt;td>93.4&lt;/td>\n&lt;td>30.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>13.3&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;td>27.8&lt;/td>\n&lt;td>0.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>16.6&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>86.7&lt;/td>\n&lt;td>46.5&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>45.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>14.1&lt;/td>\n&lt;td>2.9&lt;/td>\n&lt;td>4.9&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>2.9&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>39.4&lt;/td>\n&lt;td>30.4&lt;/td>\n&lt;td>48.1&lt;/td>\n&lt;td>37.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>43.6&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>30.9&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>44.0&lt;/td>\n&lt;td>27.0&lt;/td>\n&lt;td>72.6&lt;/td>\n&lt;td>39.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>35.9&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>88.5&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>33.7&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>48.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>34.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n",
      "numLines": 1300,
      "startLine": 500,
      "totalLines": 1799
    }
  },
  "sourceToolAssistantUUID": "6cb09dd1-04e2-4337-86cc-397712ff379d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "a7afb7c4-539d-4cd8-ab55-09f0dbd50bd6",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Assistant

_source line 51 · 2026-05-27T16:07:58.790Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the complete paper content. Let me also try to find the OpenReview page for ACL 2025 reviews. ACL 2025 uses OpenReview for reviews, so let me try to find it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7afb7c4-539d-4cd8-ab55-09f0dbd50bd6",
  "isSidechain": false,
  "requestId": "req_011CbTMxnrjDHwKizpCf8GsW",
  "type": "assistant",
  "uuid": "9b3d0c63-29bd-4530-b3c9-385fbcbcb57c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzQ9ZJ2jDCwqRpeFtMzW9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20729,
      "cache_read_input_tokens": 28872,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 28872,
          "cache_creation_input_tokens": 20729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20729
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

_source line 52 · 2026-05-27T16:07:59.272Z_

Now let me try to find the ACL 2025 OpenReview page for this paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b3d0c63-29bd-4530-b3c9-385fbcbcb57c",
  "isSidechain": false,
  "requestId": "req_011CbTMxnrjDHwKizpCf8GsW",
  "type": "assistant",
  "uuid": "bad6a607-2a59-4714-af77-5cb2b8842f06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzQ9ZJ2jDCwqRpeFtMzW9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20729,
      "cache_read_input_tokens": 28872,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 28872,
          "cache_creation_input_tokens": 20729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20729
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

_source line 53 · 2026-05-27T16:08:01.210Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MVB9rbJCd3RDJWd32rS5SC`</summary>

```json
{
  "url": "https://openreview.net/venue?id=ACL.org/2025/Conference",
  "prompt": "Find any links to accepted papers, paper listings, or search functionality for ACL 2025 conference papers. I'm looking for the paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bad6a607-2a59-4714-af77-5cb2b8842f06",
  "isSidechain": false,
  "requestId": "req_011CbTMxnrjDHwKizpCf8GsW",
  "type": "assistant",
  "uuid": "a4253bbf-b614-4568-80e1-c62414e0d63d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WzQ9ZJ2jDCwqRpeFtMzW9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20729,
      "cache_read_input_tokens": 28872,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 28872,
          "cache_creation_input_tokens": 20729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20729
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

_source line 54 · 2026-05-27T16:08:03.782Z_

<details><summary>↩ Tool result · `toolu_01MVB9rbJCd3RDJWd32rS5SC`</summary>

```text
Based on the webpage content provided, I cannot find any links to accepted papers, paper listings, or search functionality for ACL 2025 conference papers.

The page displays an error message stating: "Venues list for ACL.org/2025/Conference is unavailable. Please try again later"

The only functional navigation options shown are links to general OpenReview resources like "About OpenReview," "All Venues," and "Hosting a Venue," but these don't provide direct access to ACL 2025 papers or a search function for the specific paper you're looking for ("ProcessBench: Identifying Process Errors in Mathematical Reasoning").

To locate this paper, you would need to wait for the venues list to become available or try accessing the ACL 2025 conference page directly through an alternative route.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4253bbf-b614-4568-80e1-c62414e0d63d",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "eeae8492-4e62-4d34-9002-c85bf3e4a74b",
  "toolUseResult": {
    "bytes": 56966,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the webpage content provided, I cannot find any links to accepted papers, paper listings, or search functionality for ACL 2025 conference papers.\n\nThe page displays an error message stating: \"Venues list for ACL.org/2025/Conference is unavailable. Please try again later\"\n\nThe only functional navigation options shown are links to general OpenReview resources like \"About OpenReview,\" \"All Venues,\" and \"Hosting a Venue,\" but these don't provide direct access to ACL 2025 papers or a search function for the specific paper you're looking for (\"ProcessBench: Identifying Process Errors in Mathematical Reasoning\").\n\nTo locate this paper, you would need to wait for the venues list to become available or try accessing the ACL 2025 conference page directly through an alternative route.",
    "durationMs": 2568,
    "url": "https://openreview.net/venue?id=ACL.org/2025/Conference"
  },
  "sourceToolAssistantUUID": "a4253bbf-b614-4568-80e1-c62414e0d63d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-27T16:08:08.957Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try searching for the paper on ACL Anthology or try a direct OpenReview search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeae8492-4e62-4d34-9002-c85bf3e4a74b",
  "isSidechain": false,
  "requestId": "req_011CbTMySyvSvs1mbRuLe6kH",
  "type": "assistant",
  "uuid": "6fbcdef1-b710-4ae7-a0eb-8104d02249ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKYp6kJzdMqCAqrG1MXMf6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 49601,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 49601,
          "cache_creation_input_tokens": 407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 407
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

_source line 56 · 2026-05-27T16:08:10.115Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QJRG8HLapQKaEX6gMFLarL`</summary>

```json
{
  "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors&venue=ACL.org/2025",
  "prompt": "Find the OpenReview page for \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\". Return any paper URLs, reviewer comments, ratings, or discussion threads."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fbcdef1-b710-4ae7-a0eb-8104d02249ce",
  "isSidechain": false,
  "requestId": "req_011CbTMySyvSvs1mbRuLe6kH",
  "type": "assistant",
  "uuid": "eb2a87cf-811f-4e82-ba37-be04c2403d1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKYp6kJzdMqCAqrG1MXMf6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 49601,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 407,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 49601,
          "cache_creation_input_tokens": 407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 407
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

_source line 57 · 2026-05-27T16:08:12.234Z_

<details><summary>↩ Tool result · `toolu_01QJRG8HLapQKaEX6gMFLarL`</summary>

```text
I cannot find information about "ProcessBench: Identifying Process Errors in Mathematical Reasoning" in the provided web page content.

The content shown is only the navigation menu and footer of OpenReview.net's homepage. It does not contain any paper details, URLs, reviewer comments, ratings, or discussion threads for the specific paper you're asking about.

To locate this paper, you would need to:
- Visit OpenReview.net directly
- Use their search function to look up "ProcessBench"
- Navigate to the relevant venue or paper page
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb2a87cf-811f-4e82-ba37-be04c2403d1c",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "bc0e15e0-6b96-417e-9946-aaaaeee91f73",
  "toolUseResult": {
    "bytes": 62408,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find information about \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" in the provided web page content.\n\nThe content shown is only the navigation menu and footer of OpenReview.net's homepage. It does not contain any paper details, URLs, reviewer comments, ratings, or discussion threads for the specific paper you're asking about.\n\nTo locate this paper, you would need to:\n- Visit OpenReview.net directly\n- Use their search function to look up \"ProcessBench\"\n- Navigate to the relevant venue or paper page",
    "durationMs": 2116,
    "url": "https://openreview.net/search?term=ProcessBench+Identifying+Process+Errors&venue=ACL.org/2025"
  },
  "sourceToolAssistantUUID": "eb2a87cf-811f-4e82-ba37-be04c2403d1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-27T16:08:16.698Z_

<details><summary>Logged reasoning block</summary>

```text
The OpenReview search seems to not work via WebFetch. Let me try a WebSearch instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc0e15e0-6b96-417e-9946-aaaaeee91f73",
  "isSidechain": false,
  "requestId": "req_011CbTMz593WyneSRhDqzYdq",
  "type": "assistant",
  "uuid": "0f386d49-50dc-4a28-8433-791b23426361",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsAvsmpB5m1oJkrPW9fkty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 50008,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 50008,
          "cache_creation_input_tokens": 302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 302
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

_source line 59 · 2026-05-27T16:08:16.764Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FG96FcEY71WXJXsd6S9RfF`</summary>

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
  "parentUuid": "0f386d49-50dc-4a28-8433-791b23426361",
  "isSidechain": false,
  "requestId": "req_011CbTMz593WyneSRhDqzYdq",
  "type": "assistant",
  "uuid": "e9b2cfc6-4195-4589-bff5-a4defa126a62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsAvsmpB5m1oJkrPW9fkty",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 50008,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 50008,
          "cache_creation_input_tokens": 302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 302
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

_source line 60 · 2026-05-27T16:08:16.767Z_

<details><summary>↩ Tool result · `toolu_01FG96FcEY71WXJXsd6S9RfF`</summary>

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
  "parentUuid": "e9b2cfc6-4195-4589-bff5-a4defa126a62",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "219542d4-a96f-4d8f-ad33-1093bc67418f",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e9b2cfc6-4195-4589-bff5-a4defa126a62",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61 · 2026-05-27T16:08:16.940Z_

```json
{
  "parentUuid": "219542d4-a96f-4d8f-ad33-1093bc67418f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ea20e15d-0de1-4751-8363-0b72975f20f7",
  "timestamp": "2026-05-27T16:08:16.940Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 62 · 2026-05-27T16:08:20.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NqokmrekKJKffBqTGFfjRB`</summary>

```json
{
  "query": "ProcessBench Identifying Process Errors Mathematical Reasoning ACL 2025 OpenReview reviews",
  "allowed_domains": [
    "openreview.net"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea20e15d-0de1-4751-8363-0b72975f20f7",
  "isSidechain": false,
  "requestId": "req_011CbTMzREXQHb8LTF2sVszE",
  "type": "assistant",
  "uuid": "c0ab238b-5e84-4bef-af4e-c7e0a7f0cff0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178WHjPi5xNEnvGcvNn9jJo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 50310,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 98,
          "cache_read_input_tokens": 50310,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 736
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

_source line 63 · 2026-05-27T16:08:29.225Z_

<details><summary>↩ Tool result · `toolu_01NqokmrekKJKffBqTGFfjRB`</summary>

```text
Web search results for query: "ProcessBench Identifying Process Errors Mathematical Reasoning ACL 2025 OpenReview reviews"

Links: [{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns | OpenReview","url":"https://openreview.net/forum?id=BatDDolhcA"},{"title":"RES-BENCH: REASONING SKILL-AWARE ...","url":"https://openreview.net/pdf/53db00076ef4ae24fdda1ae89eb6974fb4bedad1.pdf"},{"title":"Reward Under Attack: Evaluating the Sensitivity of Process Reward Models","url":"https://openreview.net/pdf?id=Hw24VOppus"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=J4UOIrxcWy"},{"title":"MPBench: A Comprehensive Multimodal Reasoning Benchmark for Process   Errors Identification","url":"https://arxiv.org/pdf/2503.12505"}]

Based on the search results, I found information about ProcessBench and related papers:

## ProcessBench Overview

ProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, consisting of 3,400 test cases primarily focused on competition- and Olympiad-level math problems, with each test case containing a step-by-step solution with error location annotated by human experts.

Models are required to identify the earliest step that contains an error, or conclude that all steps are correct.

## Evaluation and Key Findings

The evaluation involves two types of models: process reward models (PRMs) and critic models, where the latter involves prompting general language models to critique each solution step by step.

Existing PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH, and they underperform both critic models and a straightforwardly fine-tuned PRM on the PRM800K dataset. The best open-source model, QwQ-32B-Preview, has demonstrated critique capability competitive with the proprietary model GPT-4o, despite lagging behind the reasoning-specialized o1-mini.

The ProcessBench paper appears on arXiv (arxiv.org/pdf/2412.06559) and is referenced in multiple recent ACL ARR 2025 submissions related to process reward models and mathematical reasoning evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0ab238b-5e84-4bef-af4e-c7e0a7f0cff0",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "3f16c4ec-8fbf-46a5-97e6-8b0abc2d581d",
  "toolUseResult": {
    "query": "ProcessBench Identifying Process Errors Mathematical Reasoning ACL 2025 OpenReview reviews",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QZbSDhzja9UWx8Y7Px9gVR",
        "content": [
          {
            "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2412.06559"
          },
          {
            "title": "Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns | OpenReview",
            "url": "https://openreview.net/forum?id=BatDDolhcA"
          },
          {
            "title": "RES-BENCH: REASONING SKILL-AWARE ...",
            "url": "https://openreview.net/pdf/53db00076ef4ae24fdda1ae89eb6974fb4bedad1.pdf"
          },
          {
            "title": "Reward Under Attack: Evaluating the Sensitivity of Process Reward Models",
            "url": "https://openreview.net/pdf?id=Hw24VOppus"
          },
          {
            "title": "The Lessons of Developing Process Reward Models in Mathematical Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=J4UOIrxcWy"
          },
          {
            "title": "MPBench: A Comprehensive Multimodal Reasoning Benchmark for Process   Errors Identification",
            "url": "https://arxiv.org/pdf/2503.12505"
          }
        ]
      },
      "Based on the search results, I found information about ProcessBench and related papers:\n\n## ProcessBench Overview\n\nProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, consisting of 3,400 test cases primarily focused on competition- and Olympiad-level math problems, with each test case containing a step-by-step solution with error location annotated by human experts.\n\nModels are required to identify the earliest step that contains an error, or conclude that all steps are correct.\n\n## Evaluation and Key Findings\n\nThe evaluation involves two types of models: process reward models (PRMs) and critic models, where the latter involves prompting general language models to critique each solution step by step.\n\nExisting PRMs typically fail to generalize to more challenging math problems beyond GSM8K and MATH, and they underperform both critic models and a straightforwardly fine-tuned PRM on the PRM800K dataset. The best open-source model, QwQ-32B-Preview, has demonstrated critique capability competitive with the proprietary model GPT-4o, despite lagging behind the reasoning-specialized o1-mini.\n\nThe ProcessBench paper appears on arXiv (arxiv.org/pdf/2412.06559) and is referenced in multiple recent ACL ARR 2025 submissions related to process reward models and mathematical reasoning evaluation."
    ],
    "durationSeconds": 8.994029780000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c0ab238b-5e84-4bef-af4e-c7e0a7f0cff0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-27T16:08:34.485Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to find the actual OpenReview page for the ProcessBench paper at ACL 2025.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f16c4ec-8fbf-46a5-97e6-8b0abc2d581d",
  "isSidechain": false,
  "requestId": "req_011CbTN1Knt8gEqmPifpnoQr",
  "type": "assistant",
  "uuid": "c2ddb8f5-6a3c-46e2-9863-982631ed3ded",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bBM7Qnz9GyCntjKt2vgwM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 51046,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 51046,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 65 · 2026-05-27T16:08:34.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PCAXQrAZMbnTsKxLEKBPPz`</summary>

```json
{
  "query": "\"ProcessBench\" site:openreview.net ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2ddb8f5-6a3c-46e2-9863-982631ed3ded",
  "isSidechain": false,
  "requestId": "req_011CbTN1Knt8gEqmPifpnoQr",
  "type": "assistant",
  "uuid": "007f69c0-610f-4eff-8553-31fc64395f1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016bBM7Qnz9GyCntjKt2vgwM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 51046,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 51046,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 66 · 2026-05-27T16:08:39.563Z_

<details><summary>↩ Tool result · `toolu_01PCAXQrAZMbnTsKxLEKBPPz`</summary>

```text
Web search results for query: ""ProcessBench" site:openreview.net ACL 2025"

Links: [{"title":"ACL 2025 | OpenReview","url":"https://openreview.net/group?id=aclweb.org/ACL/2025"},{"title":"ACL 2025 Demo | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FDemo"},{"title":"ACL 2025 Industry Track | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FIndustry_Track"},{"title":"ACL 2025 Workshop L2M2 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop%2FL2M2"},{"title":"ACL 2025 Workshop | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop"},{"title":"ACL 2025 Workshop CoNLL | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop%2FCoNLL"},{"title":"ACL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FConference"},{"title":"ACL 2025 Workshop KnowFM | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop%2FKnowFM"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"ProcBench: Benchmark for Multi-Step Reasoning and Following Procedure","url":"https://arxiv.org/pdf/2410.03117"}]

Based on the search results, I found information about ACL 2025 on OpenReview, but the specific "ProcessBench" paper doesn't appear in these results. The search returned the ACL 2025 conference pages on OpenReview and some related benchmarks like PRMBench and ProcBench, but not specifically a paper titled "ProcessBench" for ACL 2025.

To find more specific information about ProcessBench at ACL 2025, you might want to:
- Visit the ACL 2025 Conference page directly at https://openreview.net/group?id=aclweb.org/ACL/2025/Conference
- Search for the paper by author name if you have it
- Try a more specific search with the paper's authors

Is there additional information about ProcessBench you're looking for, or would you like me to search with different terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "007f69c0-610f-4eff-8553-31fc64395f1c",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "9419521f-9ab8-41b9-b7fb-9916d3b7e961",
  "toolUseResult": {
    "query": "\"ProcessBench\" site:openreview.net ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TYWZLSnRDVzhgkkrhnDDvy",
        "content": [
          {
            "title": "ACL 2025 | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org/ACL/2025"
          },
          {
            "title": "ACL 2025 Demo | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FDemo"
          },
          {
            "title": "ACL 2025 Industry Track | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FIndustry_Track"
          },
          {
            "title": "ACL 2025 Workshop L2M2 | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop%2FL2M2"
          },
          {
            "title": "ACL 2025 Workshop | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop"
          },
          {
            "title": "ACL 2025 Workshop CoNLL | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop%2FCoNLL"
          },
          {
            "title": "ACL 2025 Conference | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FConference"
          },
          {
            "title": "ACL 2025 Workshop KnowFM | OpenReview",
            "url": "https://openreview.net/group?id=aclweb.org%2FACL%2F2025%2FWorkshop%2FKnowFM"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          },
          {
            "title": "ProcBench: Benchmark for Multi-Step Reasoning and Following Procedure",
            "url": "https://arxiv.org/pdf/2410.03117"
          }
        ]
      },
      "Based on the search results, I found information about ACL 2025 on OpenReview, but the specific \"ProcessBench\" paper doesn't appear in these results. The search returned the ACL 2025 conference pages on OpenReview and some related benchmarks like PRMBench and ProcBench, but not specifically a paper titled \"ProcessBench\" for ACL 2025.\n\nTo find more specific information about ProcessBench at ACL 2025, you might want to:\n- Visit the ACL 2025 Conference page directly at https://openreview.net/group?id=aclweb.org/ACL/2025/Conference\n- Search for the paper by author name if you have it\n- Try a more specific search with the paper's authors\n\nIs there additional information about ProcessBench you're looking for, or would you like me to search with different terms?"
    ],
    "durationSeconds": 5.028038788999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "007f69c0-610f-4eff-8553-31fc64395f1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-27T16:08:43.412Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MuiUnX4KeHCXQ1vmTJxKee`</summary>

```json
{
  "url": "https://openreview.net/group?id=aclweb.org/ACL/2025/Conference",
  "prompt": "Find the paper titled 'ProcessBench: Identifying Process Errors in Mathematical Reasoning' in the ACL 2025 accepted papers list. Return the direct URL to the paper's forum/review page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9419521f-9ab8-41b9-b7fb-9916d3b7e961",
  "isSidechain": false,
  "requestId": "req_011CbTN261SV81bi8wDUaMHR",
  "type": "assistant",
  "uuid": "37682243-d33d-4e40-964e-e763ac5ff039",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nJNiA97ADWXP5uYXhEyZj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 51790,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 51790,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
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

_source line 68 · 2026-05-27T16:08:46.067Z_

<details><summary>↩ Tool result · `toolu_01MuiUnX4KeHCXQ1vmTJxKee`</summary>

```text
I cannot find the paper titled "ProcessBench: Identifying Process Errors in Mathematical Reasoning" in the web page content provided. The content shown is only the OpenReview.net homepage with navigation elements and footer information—it does not display the ACL 2025 accepted papers list.

To locate this paper, you would need to:
1. Visit the ACL 2025 venue page on OpenReview
2. Browse or search the accepted papers list
3. Click on the paper to access its forum page

I recommend navigating directly to the ACL 2025 conference page on OpenReview.net to find this paper's URL.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37682243-d33d-4e40-964e-e763ac5ff039",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "2f7fb389-d58c-4b51-a2cf-cba20b583783",
  "toolUseResult": {
    "bytes": 73265,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find the paper titled \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\" in the web page content provided. The content shown is only the OpenReview.net homepage with navigation elements and footer information—it does not display the ACL 2025 accepted papers list.\n\nTo locate this paper, you would need to:\n1. Visit the ACL 2025 venue page on OpenReview\n2. Browse or search the accepted papers list\n3. Click on the paper to access its forum page\n\nI recommend navigating directly to the ACL 2025 conference page on OpenReview.net to find this paper's URL.",
    "durationMs": 2650,
    "url": "https://openreview.net/group?id=aclweb.org/ACL/2025/Conference"
  },
  "sourceToolAssistantUUID": "37682243-d33d-4e40-964e-e763ac5ff039",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "2f7fb389-d58c-4b51-a2cf-cba20b583783",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Assistant

_source line 71 · 2026-05-27T16:08:52.964Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try one more approach - using the Bash tool to search with `gh` or try a more specific search.

Actually, let me try directly searching for the OpenReview forum ID for this paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f7fb389-d58c-4b51-a2cf-cba20b583783",
  "isSidechain": false,
  "requestId": "req_011CbTN2ZnHd55kupQggpA23",
  "type": "assistant",
  "uuid": "db16f809-6808-4fb4-b430-f99e56e199a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3Ci4z6HRrH59LYADYTnFB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 52678,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 52678,
          "cache_creation_input_tokens": 290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 290
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

_source line 72 · 2026-05-27T16:08:53.236Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GJ1UtRh1wYbNhBbuuFvf9t`</summary>

```json
{
  "query": "openreview.net ProcessBench \"Chujie Zheng\" forum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db16f809-6808-4fb4-b430-f99e56e199a4",
  "isSidechain": false,
  "requestId": "req_011CbTN2ZnHd55kupQggpA23",
  "type": "assistant",
  "uuid": "e2d1f5f6-e781-48e2-baaa-b6b92a8c26e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3Ci4z6HRrH59LYADYTnFB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 52678,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 52678,
          "cache_creation_input_tokens": 290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 290
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

_source line 73 · 2026-05-27T16:08:59.331Z_

<details><summary>↩ Tool result · `toolu_01GJ1UtRh1wYbNhBbuuFvf9t`</summary>

```text
Web search results for query: "openreview.net ProcessBench "Chujie Zheng" forum"

Links: [{"title":"[Quick Review] ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://liner.com/review/processbench-identifying-process-errors-in-mathematical-reasoning"},{"title":"[2412.06559] ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/abs/2412.06559"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.50/"},{"title":"GitHub - QwenLM/ProcessBench: Official repository for ACL 2025 paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\"","url":"https://github.com/QwenLM/ProcessBench"},{"title":"Chujie Zheng | OpenReview","url":"https://openreview.net/profile?id=~Chujie_Zheng2"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"},{"title":"Chujie Zheng's research works","url":"https://www.researchgate.net/scientific-contributions/Chujie-Zheng-2299623231"}]

Based on the search results, I found information about ProcessBench and Chujie Zheng, though the results don't show a specific OpenReview forum discussion page. Here's what I found:

ProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, consisting of 3,400 test cases primarily focused on competition- and Olympiad-level math problems, where each test case contains a step-by-step solution with error location annotated by human experts, and models are required to identify the earliest step that contains an error or conclude that all steps are correct.

The paper was authored by Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin, and was published at ACL in December 2024.

The search results show that Chujie Zheng has an OpenReview profile, but I couldn't locate a specific forum discussion page on OpenReview for ProcessBench in these results. If you're looking for the OpenReview forum page specifically, you may want to visit openreview.net directly and search for the ProcessBench paper or Chujie Zheng's profile to access any discussion threads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2d1f5f6-e781-48e2-baaa-b6b92a8c26e9",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "617c40b1-608b-4ba2-af79-b83cafeba442",
  "toolUseResult": {
    "query": "openreview.net ProcessBench \"Chujie Zheng\" forum",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W2oxhM3F1D2qBHT2wgdDRH",
        "content": [
          {
            "title": "[Quick Review] ProcessBench: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://liner.com/review/processbench-identifying-process-errors-in-mathematical-reasoning"
          },
          {
            "title": "[2412.06559] ProcessBench: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2412.06559"
          },
          {
            "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.50/"
          },
          {
            "title": "GitHub - QwenLM/ProcessBench: Official repository for ACL 2025 paper \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\"",
            "url": "https://github.com/QwenLM/ProcessBench"
          },
          {
            "title": "Chujie Zheng | OpenReview",
            "url": "https://openreview.net/profile?id=~Chujie_Zheng2"
          },
          {
            "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://www.researchgate.net/publication/394269497_ProcessBench_Identifying_Process_Errors_in_Mathematical_Reasoning"
          },
          {
            "title": "Chujie Zheng's research works",
            "url": "https://www.researchgate.net/scientific-contributions/Chujie-Zheng-2299623231"
          }
        ]
      },
      "Based on the search results, I found information about ProcessBench and Chujie Zheng, though the results don't show a specific OpenReview forum discussion page. Here's what I found:\n\nProcessBench is a benchmark for measuring the ability to identify erroneous steps in mathematical reasoning, consisting of 3,400 test cases primarily focused on competition- and Olympiad-level math problems, where each test case contains a step-by-step solution with error location annotated by human experts, and models are required to identify the earliest step that contains an error or conclude that all steps are correct.\n\nThe paper was authored by Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin, and was published at ACL in December 2024.\n\nThe search results show that Chujie Zheng has an OpenReview profile, but I couldn't locate a specific forum discussion page on OpenReview for ProcessBench in these results. If you're looking for the OpenReview forum page specifically, you may want to visit openreview.net directly and search for the ProcessBench paper or Chujie Zheng's profile to access any discussion threads."
    ],
    "durationSeconds": 6.090419597999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e2d1f5f6-e781-48e2-baaa-b6b92a8c26e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-27T16:09:02.608Z_

<details><summary>Logged reasoning block</summary>

```text
Great - I found that the paper is in the ACL Anthology. Let me try to find the OpenReview forum or check the ACL Anthology for any reviews. Let me also check the ACL Anthology page for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "617c40b1-608b-4ba2-af79-b83cafeba442",
  "isSidechain": false,
  "requestId": "req_011CbTN3YXAPhoxjBkzHr65P",
  "type": "assistant",
  "uuid": "9c96b9d8-2bdb-403c-acdc-70e083f47583",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NY4JYenx76u73k81acHonW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 52968,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 52968,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 75 · 2026-05-27T16:09:03.165Z_

Let me check the ACL Anthology page and try to find the OpenReview forum directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c96b9d8-2bdb-403c-acdc-70e083f47583",
  "isSidechain": false,
  "requestId": "req_011CbTN3YXAPhoxjBkzHr65P",
  "type": "assistant",
  "uuid": "c0c766a4-15a0-45fa-81d1-44bd97c51b52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NY4JYenx76u73k81acHonW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 52968,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 52968,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 76 · 2026-05-27T16:09:04.994Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J6myZzCE8xUyorqwueh2r6`</summary>

```json
{
  "url": "https://aclanthology.org/2025.acl-long.50/",
  "prompt": "Extract all information about this paper from the ACL Anthology page, including any links to reviews, supplementary materials, or the OpenReview forum page. Also extract the paper's metadata like venue, publication date, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c766a4-15a0-45fa-81d1-44bd97c51b52",
  "isSidechain": false,
  "requestId": "req_011CbTN3YXAPhoxjBkzHr65P",
  "type": "assistant",
  "uuid": "f35fe9fd-1b28-4dca-bed5-109c5712c538",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NY4JYenx76u73k81acHonW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 52968,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 52968,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 77 · 2026-05-27T16:09:06.298Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KHBvUth5GQYDwzTeFHVR9X`</summary>

```json
{
  "url": "https://openreview.net/profile?id=~Chujie_Zheng2",
  "prompt": "Find any papers by Chujie Zheng related to ProcessBench that have been submitted to ACL 2025. Look for forum IDs or direct links to the ProcessBench paper's review page on OpenReview."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f35fe9fd-1b28-4dca-bed5-109c5712c538",
  "isSidechain": false,
  "requestId": "req_011CbTN3YXAPhoxjBkzHr65P",
  "type": "assistant",
  "uuid": "24993343-4b48-43de-9d21-2029fd2b7880",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NY4JYenx76u73k81acHonW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 52968,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 52968,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 78 · 2026-05-27T16:09:10.155Z_

<details><summary>↩ Tool result · `toolu_01J6myZzCE8xUyorqwueh2r6`</summary>

```text
# ProcessBench Paper Information

## Paper Metadata
- **Title:** ProcessBench: Identifying Process Errors in Mathematical Reasoning
- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Venue:** ACL (Annual Meeting of the Association for Computational Linguistics)
- **Conference:** 63rd Annual Meeting, Volume 1: Long Papers
- **Publication Date:** July 2025
- **Location:** Vienna, Austria
- **Pages:** 1009–1024
- **DOI:** 10.18653/v1/2025.acl-long.50
- **Anthology ID:** 2025.acl-long.50

## Links
- **Paper PDF:** https://aclanthology.org/2025.acl-long.50.pdf
- **Anthology Page:** https://aclanthology.org/2025.acl-long.50/
- **DOI Link:** https://doi.org/10.18653/v1/2025.acl-long.50

## Key Contribution
The paper introduces "a benchmark consisting of 3,400 test cases" for evaluating models' ability to identify errors in mathematical reasoning across competition-level problems with human-annotated error locations.

## Publisher
Association for Computational Linguistics | ISBN: 979-8-89176-251-0

**Note:** The provided content does not include links to reviews, supplementary materials, or an OpenReview forum page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f35fe9fd-1b28-4dca-bed5-109c5712c538",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "b6fdbe9d-8961-4b17-bbf3-da22e305dcb3",
  "toolUseResult": {
    "bytes": 43922,
    "code": 200,
    "codeText": "OK",
    "result": "# ProcessBench Paper Information\n\n## Paper Metadata\n- **Title:** ProcessBench: Identifying Process Errors in Mathematical Reasoning\n- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin\n- **Venue:** ACL (Annual Meeting of the Association for Computational Linguistics)\n- **Conference:** 63rd Annual Meeting, Volume 1: Long Papers\n- **Publication Date:** July 2025\n- **Location:** Vienna, Austria\n- **Pages:** 1009–1024\n- **DOI:** 10.18653/v1/2025.acl-long.50\n- **Anthology ID:** 2025.acl-long.50\n\n## Links\n- **Paper PDF:** https://aclanthology.org/2025.acl-long.50.pdf\n- **Anthology Page:** https://aclanthology.org/2025.acl-long.50/\n- **DOI Link:** https://doi.org/10.18653/v1/2025.acl-long.50\n\n## Key Contribution\nThe paper introduces \"a benchmark consisting of 3,400 test cases\" for evaluating models' ability to identify errors in mathematical reasoning across competition-level problems with human-annotated error locations.\n\n## Publisher\nAssociation for Computational Linguistics | ISBN: 979-8-89176-251-0\n\n**Note:** The provided content does not include links to reviews, supplementary materials, or an OpenReview forum page.",
    "durationMs": 5157,
    "url": "https://aclanthology.org/2025.acl-long.50/"
  },
  "sourceToolAssistantUUID": "f35fe9fd-1b28-4dca-bed5-109c5712c538",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-27T16:09:10.216Z_

<details><summary>↩ Tool result · `toolu_01KHBvUth5GQYDwzTeFHVR9X`</summary>

```text
Based on the provided OpenReview profile content for Chujie Zheng, I cannot find any papers related to ProcessBench that have been submitted to ACL 2025.

The publications listed on this profile include papers submitted to venues like NeurIPS 2025, ICLR 2026, and ResponsibleFM @ NeurIPS 2025, but none mention ProcessBench or ACL 2025 specifically. The most recent publications shown focus on topics such as jailbreak attacks, reasoning models, preference modeling, and the Qwen3 technical report.

To locate a ProcessBench paper by Chujie Zheng at ACL 2025, you would need to search directly on the ACL Anthology or conduct a broader OpenReview search filtered for ACL 2025 submissions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24993343-4b48-43de-9d21-2029fd2b7880",
  "isSidechain": false,
  "promptId": "3b855b10-1fe8-4ea0-be3c-feda8f522d0e",
  "type": "user",
  "uuid": "48fd785e-b746-4dd3-a902-a649fa2a38fa",
  "toolUseResult": {
    "bytes": 366841,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided OpenReview profile content for Chujie Zheng, I cannot find any papers related to ProcessBench that have been submitted to ACL 2025.\n\nThe publications listed on this profile include papers submitted to venues like NeurIPS 2025, ICLR 2026, and ResponsibleFM @ NeurIPS 2025, but none mention ProcessBench or ACL 2025 specifically. The most recent publications shown focus on topics such as jailbreak attacks, reasoning models, preference modeling, and the Qwen3 technical report.\n\nTo locate a ProcessBench paper by Chujie Zheng at ACL 2025, you would need to search directly on the ACL Anthology or conduct a broader OpenReview search filtered for ACL 2025 submissions.",
    "durationMs": 3915,
    "url": "https://openreview.net/profile?id=~Chujie_Zheng2"
  },
  "sourceToolAssistantUUID": "24993343-4b48-43de-9d21-2029fd2b7880",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 80 · 2026-05-27T16:09:40.405Z_

<details><summary>Logged reasoning block</summary>

```text
Alright, I wasn't able to find the OpenReview reviews for this specific paper. ACL 2025 may have used ARR (ACL Rolling Review) which does have an OpenReview platform, but the reviews may not be publicly accessible. Let me now synthesize all the information I have into the analysis JSON.

Let me now compile the comprehensive analysis based on everything I've read from the paper.

Key points from my thorough reading:

**Problem Identification:**
- Existing benchmarks for evaluating reasoning process assessment are insufficient: CriticBench lacks step-level annotations, MathCheck-GSM only uses easy GSM8K problems with synthetic errors, PRM800K only has 90 test cases in its phase 1 test set


- As LLMs get stronger, even difficult problems like those in MATH are becoming easier to solve, yet there's no standardized way to evaluate process reward models at scale on genuinely hard problems

**Key Insight:**
- The core reformulation is elegant: instead of measuring PRMs indirectly through Best-of-N improvements (which conflates model quality with the underlying solution generator), directly assess their ability to pinpoint the earliest error step as a standalone, interpretable task
- The empirical finding is striking—on harder problems, models that produce correct final answers often contain erroneous reasoning steps along the way (51.8% on Omni-MATH versus just 3.5% on GSM8K)

—which means using final answer correctness as a proxy for step-level labels, like Math-Shepherd does, fundamentally breaks down
- Surprisingly, simple prompted critics outperform specialized PRMs, and a straightforward fine-tuned PRM trained on human-annotated data from PRM800K beats all the PRMs trained with synthetic process labels

**Innovation Type:** new_benchmark (primarily), with significant analysis and empirical findings

**Method:**
I'm curating problems across four datasets ranging from grade school to Olympiad difficulty, generating solutions from twelve diverse open-source models, then standardizing step granularity using Qwen2.5-72B, and having doctoral-level mathematicians annotate with a 3-of-5 agreement threshold while balancing correct and incorrect final answers before evaluating various PRMs.

**What makes it good:**
The benchmark fills a real gap in how we evaluate PRMs, the methodology is rigorous with multiple annotators and quality controls, and the findings are provocative—synthetic labels don't generalize, simple baselines beat complex approaches, and the discovery that processes can be wrong despite correct final answers has major implications for RL training.

**Limitations:**
The hardest problems might still have inaccurate labels, the ~30% discard rate introduces survivorship bias toward easier cases, and focusing on "identify earliest error" only captures one aspect of process quality.

**Building blocks:**
Drawing from GSM8K, MATH, OlympiadBench, and Omni-MATH datasets, using PRM800K training data, and reformatting solutions via Qwen2.5-72B.

The core insight here is that current PRM training methods—which derive process labels from final-answer correctness—produce models that don't generalize beyond their training distribution. This points the field toward better approaches like human-annotated data, improved synthesis methods, or generative and critic-based alternatives instead of purely discriminative PRMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48fd785e-b746-4dd3-a902-a649fa2a38fa",
  "isSidechain": false,
  "requestId": "req_011CbTN4M2P2ZLzduUqWag3a",
  "type": "assistant",
  "uuid": "05073764-2ee0-4a90-ba16-cbdbe6b3ade2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YUDVGx2G843JEryKn1Kni",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 53778,
      "output_tokens": 2428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2428,
          "cache_read_input_tokens": 53778,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
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

_source line 81 · 2026-05-27T16:10:14.526Z_

Now I have all the information needed. Let me compile the comprehensive analysis.

```json
{
  "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
  "venue": "ACL 2025 (Long Paper, 63rd Annual Meeting, Vienna, Austria)",
  "problem_identification": "Existing benchmarks for evaluating step-level error detection in math reasoning were critically insufficient: CriticBench lacked step-level annotations, MathCheck-GSM used only easy GSM8K problems with synthetic errors, and PRM800K's test set had only 90 usable complete solutions. Meanwhile, the standard way of evaluating PRMs—measuring Best-of-N accuracy improvements—conflates PRM quality with the solution generator's quality, providing no fine-grained signal about whether a PRM can actually identify which step is wrong. The authors spotted this gap by observing that PRM research was booming (Math-Shepherd, RLHFlow, Skywork) but nobody had a clean, direct test of whether these models could do the thing they claimed to do.",
  "key_insight": "Rather than evaluating PRMs indirectly through downstream task performance (Best-of-N), the authors reformulated evaluation as a direct, interpretable task—'find the earliest erroneous step'—and in doing so revealed two devastating findings: (1) PRMs trained with synthetic process labels (estimating step correctness via final-answer probability) catastrophically fail to generalize beyond GSM8K/MATH difficulty, and (2) simply prompting general-purpose LLMs as critics outperforms specialized PRMs, suggesting that the entire current PRM training paradigm based on automated label synthesis may be fundamentally flawed.",
  "innovation_type": "new_benchmark",
  "method_summary": "The authors curated math problems from four datasets spanning grade school to Olympiad difficulty (GSM8K, MATH, OlympiadBench, Omni-MATH) and generated step-by-step solutions using 12 diverse open-source LLMs. A critical preprocessing step—solution reformatting via Qwen2.5-72B—standardized step granularity by re-segmenting solutions into logically complete reasoning steps. Doctoral-level mathematicians then annotated the earliest erroneous step in each solution, requiring 3-of-N agreement (up to 5 annotators), with ~30% of solutions discarded when consensus couldn't be reached. The benchmark evaluates two model types using F1 score (harmonic mean of error-detection and correct-solution accuracy): discriminative PRMs that score each step, and critic models where general LLMs are prompted to critique solutions step-by-step and output the error location. As a calibration baseline, the authors also trained their own PRM by straightforwardly fine-tuning Qwen2.5-Math-7B on fully human-annotated PRM800K data.",
  "what_makes_it_good": "Three elements make this paper exemplary. First, the benchmark fills an obvious-in-hindsight gap that the entire PRM community needed—it's the kind of infrastructure work that immediately becomes the standard evaluation tool. Second, the authors didn't just build a benchmark; they used it to produce genuinely surprising and field-redirecting findings (PRMs lose to prompted LLMs; 51.8% of Omni-MATH solutions with correct final answers contain process errors, undermining final-answer-based RL). Third, the methodology is unusually rigorous for benchmark papers: multiple annotators with agreement requirements, transparent discard rates, a self-trained PRM baseline to contextualize existing PRMs, and balanced sampling to prevent class imbalance artifacts.",
  "limitations_acknowledged": "The authors note that despite rigorous annotation, labels may still be inaccurate on the hardest Olympiad-level problems. They also acknowledge that the ~30% discard rate (cases where annotators couldn't reach consensus) could bias the problem distribution, potentially underrepresenting the most challenging cases that even expert annotators found ambiguous.",
  "open_questions": [
    "If synthetic process labels (à la Math-Shepherd) are fundamentally unreliable on hard problems because correct final answers can arise from flawed reasoning (51.8% on Omni-MATH), what alternative data synthesis methodologies can produce PRMs that actually generalize? Is fully human-annotated data the only viable path, or can we combine LLM-as-critic signals with verification?",
    "The paper shows reasoning models (QwQ-32B, o1-mini) dramatically outperform standard LLMs as critics—but WHY? Is it because they can independently re-solve the problem and compare, or because they have better step-level verification capabilities? Understanding this mechanism could inform how to train better PRMs.",
    "The 'earliest error' formulation avoids the ambiguity of evaluating steps after the first error, but real-world applications (e.g., targeted feedback, partial credit) may need richer error characterization—error type classification, severity assessment, or whether the error is recoverable. How should process evaluation benchmarks evolve beyond binary earliest-error detection?"
  ],
  "building_blocks": [
    "GSM8K, MATH, OlympiadBench, and Omni-MATH problem sets as difficulty-stratified sources",
    "12 diverse open-source LLMs (Qwen2, Qwen2.5, LLaMA-3 families) as solution generators for natural error diversity",
    "LLM-based solution reformatting to standardize step granularity",
    "PRM800K training set for straightforward PRM fine-tuning baseline",
    "F1 score (harmonic mean of error/correct accuracy) as balanced evaluation metric",
    "Simple prompt template converting general LLMs into step-by-step critic models",
    "Majority voting over 8 samplings for critic model evaluation",
    "Multi-annotator consensus protocol (3-of-N agreement, up to N=5)"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is the definitive evaluation infrastructure for our research area—any new PRM or step-level verification method must be benchmarked on ProcessBench. More importantly, its findings are a roadmap for what NOT to do: synthetic process labels derived from final-answer correctness estimation (the dominant paradigm) produce PRMs that fail on hard problems, while simple prompted critics and human-annotated-data-trained PRMs do far better. This directly motivates research into better credit assignment mechanisms, hybrid human-AI annotation pipelines, and generative (rather than discriminative) approaches to process reward modeling."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05073764-2ee0-4a90-ba16-cbdbe6b3ade2",
  "isSidechain": false,
  "requestId": "req_011CbTN4M2P2ZLzduUqWag3a",
  "type": "assistant",
  "uuid": "71211fd1-781d-4f74-a68b-aad575c36ca6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YUDVGx2G843JEryKn1Kni",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 953,
      "cache_read_input_tokens": 53778,
      "output_tokens": 2428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2428,
          "cache_read_input_tokens": 53778,
          "cache_creation_input_tokens": 953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 953
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

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "71211fd1-781d-4f74-a68b-aad575c36ca6",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 84_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "71211fd1-781d-4f74-a68b-aad575c36ca6",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---

### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ProcessBench paper for research innovation",
  "sessionId": "622fde7e-49a1-441f-a25d-d298deae6922"
}
```

---
