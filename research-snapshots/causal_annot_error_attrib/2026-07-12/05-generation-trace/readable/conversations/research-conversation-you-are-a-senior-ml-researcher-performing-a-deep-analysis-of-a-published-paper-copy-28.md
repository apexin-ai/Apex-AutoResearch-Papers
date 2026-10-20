# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-28 (UTC).** ## Y

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/540f20bc-02e4-4934-866e-739fdd700aa7.jsonl`
- **Structured JSON:** [`59b13fc6069241d7e490.json`](../../sessions/59/59b13fc6069241d7e490.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:20:28.741Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:20:28.741Z",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**\n\n## Paper to analyze\n\n{\n  \"title\": \"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models\",\n  \"authors\": \"Zheng et al.\",\n  \"venue\": \"arXiv 2025 (survey, last revised April 2026)\",\n  \"url\": \"https://arxiv.org/abs/2510.08049\",\n  \"why_important\": \"Most comprehensive survey of the PRM field; covers data generation, PRM construction, and downstream use for test-time scaling and RL across math, code, multimodal, and agent domains\",\n  \"one_line_summary\": \"Comprehensive survey covering the full PRM pipeline — process data generation, model training, and applications in test-time scaling and RL — across mathematics, coding, multimodal reasoning, and agents.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:20:28.744Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:20:28.744Z",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-28T05:20:28.808Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-28 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**

## Paper to analyze

{
  "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
  "authors": "Zheng et al.",
  "venue": "arXiv 2025 (survey, last revised April 2026)",
  "url": "https://arxiv.org/abs/2510.08049",
  "why_important": "Most comprehensive survey of the PRM field; covers data generation, PRM construction, and downstream use for test-time scaling and RL across math, code, multimodal, and agent domains",
  "one_line_summary": "Comprehensive survey covering the full PRM pipeline — process data generation, model training, and applications in test-time scaling and RL — across mathematics, coding, multimodal reasoning, and agents."
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
  "promptId": "a99e86ca-aeb1-413c-a1fe-23ebc5ea6113",
  "type": "user",
  "uuid": "7d08210b-62c9-4fea-ba10-08e1684b5c49",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:20:28.807Z_

```json
{
  "parentUuid": "7d08210b-62c9-4fea-ba10-08e1684b5c49",
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
  "uuid": "672bd048-6bde-4ec4-aca0-c70a515b889e",
  "timestamp": "2026-05-28T05:20:28.807Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:20:28.807Z_

```json
{
  "parentUuid": "672bd048-6bde-4ec4-aca0-c70a515b889e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "79ccac6a-8a42-4eee-a85d-a23f422274ea",
  "timestamp": "2026-05-28T05:20:28.807Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
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
  "aiTitle": "Analyze PRM survey paper for research methodology",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---

### Assistant

_source line 7 · 2026-05-28T05:20:31.843Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze a paper about Process Reward Models. Let me fetch the paper from arXiv to read its content, and also check if it's on OpenReview for reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79ccac6a-8a42-4eee-a85d-a23f422274ea",
  "isSidechain": false,
  "requestId": "req_011CbUQQCWDUxM5x9CwLP2Kt",
  "type": "assistant",
  "uuid": "2a138eb8-f7d3-47c5-a4f5-3495de007a39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDeK1ZRWqENUSE2za9DyVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2203,
      "cache_read_input_tokens": 11014,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2203
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

_source line 8 · 2026-05-28T05:20:32.298Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LsNYu975vTWzsY42L7oE72`</summary>

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
  "parentUuid": "2a138eb8-f7d3-47c5-a4f5-3495de007a39",
  "isSidechain": false,
  "requestId": "req_011CbUQQCWDUxM5x9CwLP2Kt",
  "type": "assistant",
  "uuid": "9ca1db96-3783-4091-863f-2b661185c9ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YDeK1ZRWqENUSE2za9DyVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2203,
      "cache_read_input_tokens": 11014,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2203
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

_source line 9 · 2026-05-28T05:20:32.305Z_

<details><summary>↩ Tool result · `toolu_01LsNYu975vTWzsY42L7oE72`</summary>

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
  "parentUuid": "9ca1db96-3783-4091-863f-2b661185c9ab",
  "isSidechain": false,
  "promptId": "a99e86ca-aeb1-413c-a1fe-23ebc5ea6113",
  "type": "user",
  "uuid": "a7b88cf6-b895-4c68-973a-3e0a03ecc006",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "9ca1db96-3783-4091-863f-2b661185c9ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-28T05:20:34.734Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the HTML version for the full paper content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7b88cf6-b895-4c68-973a-3e0a03ecc006",
  "isSidechain": false,
  "requestId": "req_011CbUQQTapfNorxXoKYXgzF",
  "type": "assistant",
  "uuid": "e2daa442-6017-400d-8c9b-60082b9e0835",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XspGGixzFSViqi3h3qSbx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 13217,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 341,
          "cache_read_input_tokens": 13217,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
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

_source line 11 · 2026-05-28T05:20:35.344Z_

Let me fetch the paper from multiple sources to get a comprehensive view.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2daa442-6017-400d-8c9b-60082b9e0835",
  "isSidechain": false,
  "requestId": "req_011CbUQQTapfNorxXoKYXgzF",
  "type": "assistant",
  "uuid": "35b9734d-1d74-4625-9624-8da6f0c86f3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XspGGixzFSViqi3h3qSbx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 13217,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 341,
          "cache_read_input_tokens": 13217,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
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

_source line 12 · 2026-05-28T05:20:36.770Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019pdCB6riZeU2YwLQmRsUf9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.08049",
  "prompt": "Extract the full abstract, list of authors, submission/revision dates, and any other metadata available on this arXiv page. Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b9734d-1d74-4625-9624-8da6f0c86f3a",
  "isSidechain": false,
  "requestId": "req_011CbUQQTapfNorxXoKYXgzF",
  "type": "assistant",
  "uuid": "a192f78d-d6c8-4b50-8ece-d04f2840617d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XspGGixzFSViqi3h3qSbx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 13217,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 341,
          "cache_read_input_tokens": 13217,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
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

_source line 13 · 2026-05-28T05:20:39.891Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NfAFQ34BZUUNHSJWAGdj7g`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.08049",
  "prompt": "Extract the full content of this paper. I need:\n1. The complete Introduction section\n2. The complete taxonomy/framework they use to organize the survey\n3. All section headings and subheadings to understand the paper's structure\n4. The key findings, contributions, and conclusions\n5. Any discussion of open problems, challenges, or future directions\n6. Tables or figures that summarize the taxonomy\n\nBe as thorough as possible — return all substantive content, not just summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a192f78d-d6c8-4b50-8ece-d04f2840617d",
  "isSidechain": false,
  "requestId": "req_011CbUQQTapfNorxXoKYXgzF",
  "type": "assistant",
  "uuid": "69198027-84e5-4847-a187-072987a8ce86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XspGGixzFSViqi3h3qSbx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 13217,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 341,
          "cache_read_input_tokens": 13217,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
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

_source line 14 · 2026-05-28T05:20:41.742Z_

<details><summary>↩ Tool result · `toolu_019pdCB6riZeU2YwLQmRsUf9`</summary>

```text
# arXiv Paper Metadata

**Title:** "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models"

**Authors:** Congmin Zheng, Jiachen Zhu, Zhuoying Ou, Yuxiang Chen, Kangning Zhang, Rong Shan, Zeyu Zheng, Mengyue Yang, Jianghao Lin, Yong Yu, Weinan Zhang

**Abstract:** The paper examines how "Process Reward Models (PRMs) address this gap by evaluating and guiding reasoning at the step or trajectory level," covering data generation, model construction, and applications. It spans math, code, text, multimodal reasoning, robotics, and agents while reviewing benchmarks.

**Submission History:**
- v1: October 9, 2025
- v2: October 21, 2025
- v3: April 29, 2026 (current)

**Identifiers:**
- arXiv: 2510.08049
- DOI: 10.48550/arXiv.2510.08049

**Subject Classifications:**
- Computation and Language (cs.CL)
- Artificial Intelligence (cs.AI)

**Submitter:** Congmin Zheng
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a192f78d-d6c8-4b50-8ece-d04f2840617d",
  "isSidechain": false,
  "promptId": "a99e86ca-aeb1-413c-a1fe-23ebc5ea6113",
  "type": "user",
  "uuid": "d55fa3fe-a23d-4a06-bcc0-9cb207a7643a",
  "toolUseResult": {
    "bytes": 46356,
    "code": 200,
    "codeText": "OK",
    "result": "# arXiv Paper Metadata\n\n**Title:** \"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models\"\n\n**Authors:** Congmin Zheng, Jiachen Zhu, Zhuoying Ou, Yuxiang Chen, Kangning Zhang, Rong Shan, Zeyu Zheng, Mengyue Yang, Jianghao Lin, Yong Yu, Weinan Zhang\n\n**Abstract:** The paper examines how \"Process Reward Models (PRMs) address this gap by evaluating and guiding reasoning at the step or trajectory level,\" covering data generation, model construction, and applications. It spans math, code, text, multimodal reasoning, robotics, and agents while reviewing benchmarks.\n\n**Submission History:**\n- v1: October 9, 2025\n- v2: October 21, 2025\n- v3: April 29, 2026 (current)\n\n**Identifiers:**\n- arXiv: 2510.08049\n- DOI: 10.48550/arXiv.2510.08049\n\n**Subject Classifications:**\n- Computation and Language (cs.CL)\n- Artificial Intelligence (cs.AI)\n\n**Submitter:** Congmin Zheng",
    "durationMs": 4967,
    "url": "https://arxiv.org/abs/2510.08049"
  },
  "sourceToolAssistantUUID": "a192f78d-d6c8-4b50-8ece-d04f2840617d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T05:21:20.993Z_

<details><summary>↩ Tool result · `toolu_01NfAFQ34BZUUNHSJWAGdj7g`</summary>

```text
# Survey of Process Reward Models: Comprehensive Content Extraction

## 1. INTRODUCTION (Complete Section)

The introduction establishes that Large Language Models have shifted alignment paradigms from outcome-only supervision to process-aware evaluation. Traditional outcome reward models (ORMs) provide single coarse signals for long reasoning chains, but as tasks grow more complex, this approach struggles to capture stepwise progress, diagnose intermediate errors, or allocate computation adaptively.

**Key Problem Addressed:** Process Reward Models (PRMs) assess and guide reasoning at the step or trajectory level, moving beyond coarse outcome supervision.

**The PRM Loop:** The framework consists of three iterative stages:
- Generate process data
- Train PRMs  
- Use PRMs (test-time scaling or RL) → produce better data

This transforms reward modeling from a one-shot verdict into an iterative reasoning controller, enabling finer credit assignment, richer diagnostics, and improved robustness.

**Paradigm Shift:** Rather than single-turn evaluation, PRMs assess partial solutions and trajectories, leverage context for adaptive "reason-then-rate" verification, and integrate with inference-time controllers and reinforcement learning objectives.

**Positioning:** The survey uniquely targets step-level process reward modeling by organizing the full loop (data generation, PRM building, usage) for fine-grained reasoning supervision, distinct from existing surveys on test-time scaling, broad reward taxonomies, or generic deep RL reward design.

---

## 2. COMPLETE PAPER STRUCTURE & TAXONOMY

### Section Organization:

**Section 2 - How to Generate Data**
- 2.1 Human Annotation
- 2.2 Automated Supervision
- 2.3 Semi-automated Approaches

**Section 3 - How to Build PRMs**
- 3.1 Discriminative PRMs
- 3.2 Generative PRMs
- 3.3 Implicit PRMs
- 3.4 Other Architectural Innovations

**Section 4 - How to Use PRMs**
- 4.1 Test-Time Scaling
- 4.2 RL for Policy Learning

**Section 5 - Downstream Applications**
- Math
- Code
- Multimodal
- Text
- Robotics
- Agents
- Industry
- Multi-domain

**Section 6 - Benchmark**

**Section 7 - Discussion** (six evaluation aspects)
- Resource Efficiency
- Granularity
- Anti-Hacking Robustness
- Generalization
- Interpretability
- Functionality

**Section 8 - Conclusion**

**Section 9 - Limitations**

---

## 3. KEY TECHNICAL FRAMEWORKS

### Discriminative PRMs (Section 3.1)

**Mathematical Formulation:**

Scoring function outputs scalar reward: r_t = σ(f_θ(x, s_{1:t})) ∈ (0,1)

**Training Approaches:**

*Pointwise Loss:*
- Binary Cross-Entropy: L_point^BCE = E[-y_t log r_t - (1-y_t) log(1-r_t)]
- Mean Squared Error: L_point^MSE = E[(r_t - y_t)²]

*Pairwise Preference Loss:*
- P_θ(u ≻ v) = σ(f_θ(u) - f_θ(v))
- L_pair = E[-log P_θ(u ≻ v)]

**Representative Methods:** DreamPRM, PQM, ER-PRM, EDU-PRM, Q-RM, BiPRM, R-PRM, BiRM, CoLD, ProgRM

### Generative PRMs (Section 3.2)

**Two-Stage Process:**

Stage 1: Generate verification chain z_t ~ p_φ(z_t | x, s_{1:t})
Stage 2: Judge with scoring: r_t = h_ψ(x, s_{1:t}, z_t)

**Joint Training Objective:**
L_gen = -log p_φ(z_t* | x, s_{1:t}) + λ·BCE(r_t, y_t)

**Representative Methods:** ThinkPRM, GenRM, GenPRM, GRAM-R², Process-based Self-Rewarding Language Models, GM-PRM, rStar-Math

### Implicit PRMs (Section 3.3)

Infer fine-grained rewards without step-level labels through outcome feedback, model self-evaluation, or consistency constraints.

**Representative Methods:** FreePRM, Self-PRM, SP-PRM, SPARE, Universal PRM (AURORA)

### Other Architectural Innovations (Section 3.4)

Methods emphasizing structural innovations rather than loss functions:

**Representative Methods:** GraphPRM, ASPRM (AdaptiveStep), Reward-SQL, RetrievalPRM, OpenPRM, MM-PRM, Multilingual PRM, PathFinder-PRM, Hierarchical Reward Model (HRM)

---

## 4. DATA GENERATION APPROACHES

### 2.1 Human Annotation

**Example:** PRM800K dataset with human-labeled step correctness, providing high-fidelity signals that serve as benchmarks and seed material for scalable methods.

### 2.2 Automated Supervision

**Key Techniques:**

- **Symbolic Verification:** Math-Shepherd uses symbolic tools and consistency-checking heuristics
- **Formal Verification:** FOVER uses Z3 and Isabelle tools for step-level error labels
- **Tree Search:** OmegaPRM employs Monte Carlo Tree Search (MCTS) for error localization; URSA applies dual-view MCTS for multimodal mathematics
- **Execution Feedback:** CodePRM uses automated tree search and execution feedback for code reasoning
- **Pseudo-Supervision:** AlphaMath derives process supervision directly from outcome supervision
- **Self-Evolution:** rStar-Math and Qwen2.5-Math PRM use consensus-filtering and self-evolutionary strategies
- **Noise Reduction:** SCAN introduces self-denoising annotation framework

**Benefit:** Unprecedented scale and efficiency; challenge: error propagation and verifier limitations.

### 2.3 Semi-Automated Approaches

**Pattern:** Limited human-curated examples expanded through automated verification or synthesis.

**Domain Applications:**
- **Multimodal:** VRPRM, Athena, ViLBench, VisualPRM
- **Medical:** MedS³ starts with 8,000 human examples, expands via MCTS-based exploration
- **Multi-domain:** VersaPRM generates synthetic data with small-scale manual verification
- **Web Agents:** Web-Shepherd combines human oversight with automatic checks
- **GUI Tasks:** GUI-Shepherd uses dual-pipeline strategy with hybrid annotations
- **Active Learning:** ActPRM selectively queries human annotators when automated signals are uncertain

---

## 5. USAGE PARADIGMS

### 4.1 Test-Time Scaling

**Evolution:**
1. **Re-ranking Phase:** Best-of-N evaluation with PRM scores
2. **Generative Verification:** GenPRM produces verification chains before scoring
3. **Search Integration:** MCTS, beam search, and retrieval-augmented reasoning
4. **Adaptive Granularity:** AdaptiveStep dynamically partitions reasoning based on confidence

**Key Methods:** PRM-BAS (beam annealing search), CodePRM (Generate–Verify–Refine pipeline), Web-Shepherd trajectory filtering

### 4.2 RL for Policy Learning

**Mechanism:** PRMs provide dense step-level feedback replacing sparse correctness signals.

**Representative Approaches:**

- **Progress Indicators:** PAV reframes PRM outputs as advantage-like progress indicators
- **KL-Constrained RL:** ER-PRM embeds PRM rewards into KL-constrained objectives
- **Credit Assignment:** PURE proposes min-form objective (opposed to summation) to prevent reward hacking; CAPO introduces verifiable generative credit assignment
- **Token-Level Supervision:** Q-RM models Q-values over tokens for direct RL optimization
- **Consistency Filtering:** PROF ranks responses based on process–outcome consistency, removing conflicting samples
- **Actor-Critic:** AgentPRM integrates PRMs into actor–critic loops for agent tasks
- **Infrastructure:** OpenR provides systematic framework for offline and online RL integration

---

## 6. DOWNSTREAM APPLICATIONS (Summary)

**Math:** Multi-step derivation soundness, symbolic error detection, automated grading and proof validation

**Code:** Execution feedback, semantic consistency, text-to-SQL verification, software engineering patches

**Multimodal:** Visual-text coherence checks, reasoning trace re-ranking, grounded explanation selection

**Text:** Partial translation refinement, multi-hop QA, retrieval-augmented reasoning improvement

**Robotics:** Long-horizon decomposition into subgoal rewards for dense feedback in manipulation/navigation

**Agents:** Trajectory criticism, progress reward, dead-end pruning, safety during inference

**Industry:** Medical and financial reasoning with verifiable evidence-based logic for reliability

**Multi-domain:** Generalizable PRMs transferring supervision across diverse tasks

---

## 7. BENCHMARKS (Section 6)

**Mathematical Reasoning:**
- PRMBench: 6,000+ problems with 80,000 step annotations
- ProcessBench: Competition-level tasks emphasizing earliest-error detection
- Socratic-PRMBench: ~3,000 flawed trajectories grouped into six error patterns

**Multimodal:**
- ViLBench: Vision-language task comparisons
- VisualProcessBench: Human-labeled multimodal errors
- MPBench: Multiple tasks assessing step correctness and answer aggregation

**Long-Horizon:**
- WebRewardBench: 40,000 step-level preference pairs for web agents

**Robustness & Universality:**
- GSM-DC: Distractors test resilience
- UniversalBench: Cross-distribution generalization evaluation

---

## 8. DISCUSSION: COMPARATIVE ANALYSIS (Section 7)

**Figure 2 Framework:** Six-aspect evaluation comparing rule-based rewards, ORMs, and PRMs

| **Aspect** | **Rule-Based** | **ORMs** | **PRMs** |
|---|---|---|---|
| **Resource Efficiency** | Excellent (no training) | Good (single-stage) | Poor (step-level annotation) |
| **Granularity** | Variable | Single outcome | High (step-specific) |
| **Anti-Hacking Robustness** | Poor (mis-specification) | Excellent (ground-truth) | Moderate (length bias susceptible) |
| **Generalization** | Poor (task-specific) | Excellent (task-agnostic) | Moderate (domain-specific granularity) |
| **Interpretability** | Excellent (explicit) | Poor (black box) | Good (fine-grained explanation) |
| **Functionality** | Restricted | Limited (outcome only) | Versatile (search, RL, credit assignment) |

**Key Finding on Length Bias:** Analysis of PRM800K shows step-level standard deviation (71.7) exceeds trajectory-level (50.6), indicating PRMs are more susceptible to verbose but vacuous intermediate steps.

---

## 9. OPEN CHALLENGES & FUTURE DIRECTIONS

### Identified in Discussion & Conclusion:

**Resource Efficiency Challenge:** Step-wise annotation overhead (7-13 steps average per problem) creates workload several times higher than outcome labeling. Future work must reduce annotation costs via robust automation.

**Generalization Limitation:** Step definitions for mathematical derivations differ from code execution traces, necessitating frequent re-adaptation across domains. Cross-domain PRM development remains an open frontier.

**Integration with Agency:** Key challenges include integrating PRMs with agentic planning and memory systems for complex interactive tasks.

**Anti-Hacking Robustness:** PRMs require defenses against reward hacking through length bias; research on calibration and uncertainty quantification needed.

**Granularity Tension (Appendix B.3):** Defining "a step" remains contested—no consensus on appropriate granularity across reasoning domains.

**Proxy-Reward Gap (Appendix B.4):** Distinction between proxy metrics (formal verification, execution) and actual utility for human-aligned reasoning.

**Cognitive Scalability (Appendix B.1):** Human annotation capacity constraints limit scaling of high-fidelity supervision pipelines.

**Echo Chambers & Goodhart's Law (Appendix B.2):** Automated supervision risks creating feedback loops where verifiers reinforce their own errors; proxies optimized away from true objectives.

**Standardized Evaluation:** Need for consistent protocols across diverse domains and task types.

---

## 10. KEY CONTRIBUTIONS

The survey provides:

1. **Systematic Organization:** Full-loop framework (data generation → PRM building → usage)
2. **Taxonomy Clarity:** Four training paradigms (discriminative, generative, implicit, architectural)
3. **Comprehensive Coverage:** 8+ application domains with 70+ representative methods
4. **Comparative Analysis:** Six-dimension evaluation framework comparing reward mechanisms
5. **Benchmark Summary:** 10+ major benchmarks across reasoning domains
6. **Critical Discussion:** Identifies resource costs, generalization gaps, robustness risks, and theoretical tensions
7. **GitHub Repository:** Actively maintained resource linking papers and implementations

---

## 11. PAPER LIMITATIONS (Section 9)

- Taxonomy follows data–model–usage loop, potentially simplifying or abstracting hybrid methods
- Benchmark and application summaries are selective rather than comprehensive
- Some domain-specific datasets and proprietary evaluation suites not fully captured
- Focus on step-level supervision may not capture emerging trajectory-level or state-level formulations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69198027-84e5-4847-a187-072987a8ce86",
  "isSidechain": false,
  "promptId": "a99e86ca-aeb1-413c-a1fe-23ebc5ea6113",
  "type": "user",
  "uuid": "dbce5454-61ee-45f2-97f3-fef5f487fc96",
  "toolUseResult": {
    "bytes": 285000,
    "code": 200,
    "codeText": "OK",
    "result": "# Survey of Process Reward Models: Comprehensive Content Extraction\n\n## 1. INTRODUCTION (Complete Section)\n\nThe introduction establishes that Large Language Models have shifted alignment paradigms from outcome-only supervision to process-aware evaluation. Traditional outcome reward models (ORMs) provide single coarse signals for long reasoning chains, but as tasks grow more complex, this approach struggles to capture stepwise progress, diagnose intermediate errors, or allocate computation adaptively.\n\n**Key Problem Addressed:** Process Reward Models (PRMs) assess and guide reasoning at the step or trajectory level, moving beyond coarse outcome supervision.\n\n**The PRM Loop:** The framework consists of three iterative stages:\n- Generate process data\n- Train PRMs  \n- Use PRMs (test-time scaling or RL) → produce better data\n\nThis transforms reward modeling from a one-shot verdict into an iterative reasoning controller, enabling finer credit assignment, richer diagnostics, and improved robustness.\n\n**Paradigm Shift:** Rather than single-turn evaluation, PRMs assess partial solutions and trajectories, leverage context for adaptive \"reason-then-rate\" verification, and integrate with inference-time controllers and reinforcement learning objectives.\n\n**Positioning:** The survey uniquely targets step-level process reward modeling by organizing the full loop (data generation, PRM building, usage) for fine-grained reasoning supervision, distinct from existing surveys on test-time scaling, broad reward taxonomies, or generic deep RL reward design.\n\n---\n\n## 2. COMPLETE PAPER STRUCTURE & TAXONOMY\n\n### Section Organization:\n\n**Section 2 - How to Generate Data**\n- 2.1 Human Annotation\n- 2.2 Automated Supervision\n- 2.3 Semi-automated Approaches\n\n**Section 3 - How to Build PRMs**\n- 3.1 Discriminative PRMs\n- 3.2 Generative PRMs\n- 3.3 Implicit PRMs\n- 3.4 Other Architectural Innovations\n\n**Section 4 - How to Use PRMs**\n- 4.1 Test-Time Scaling\n- 4.2 RL for Policy Learning\n\n**Section 5 - Downstream Applications**\n- Math\n- Code\n- Multimodal\n- Text\n- Robotics\n- Agents\n- Industry\n- Multi-domain\n\n**Section 6 - Benchmark**\n\n**Section 7 - Discussion** (six evaluation aspects)\n- Resource Efficiency\n- Granularity\n- Anti-Hacking Robustness\n- Generalization\n- Interpretability\n- Functionality\n\n**Section 8 - Conclusion**\n\n**Section 9 - Limitations**\n\n---\n\n## 3. KEY TECHNICAL FRAMEWORKS\n\n### Discriminative PRMs (Section 3.1)\n\n**Mathematical Formulation:**\n\nScoring function outputs scalar reward: r_t = σ(f_θ(x, s_{1:t})) ∈ (0,1)\n\n**Training Approaches:**\n\n*Pointwise Loss:*\n- Binary Cross-Entropy: L_point^BCE = E[-y_t log r_t - (1-y_t) log(1-r_t)]\n- Mean Squared Error: L_point^MSE = E[(r_t - y_t)²]\n\n*Pairwise Preference Loss:*\n- P_θ(u ≻ v) = σ(f_θ(u) - f_θ(v))\n- L_pair = E[-log P_θ(u ≻ v)]\n\n**Representative Methods:** DreamPRM, PQM, ER-PRM, EDU-PRM, Q-RM, BiPRM, R-PRM, BiRM, CoLD, ProgRM\n\n### Generative PRMs (Section 3.2)\n\n**Two-Stage Process:**\n\nStage 1: Generate verification chain z_t ~ p_φ(z_t | x, s_{1:t})\nStage 2: Judge with scoring: r_t = h_ψ(x, s_{1:t}, z_t)\n\n**Joint Training Objective:**\nL_gen = -log p_φ(z_t* | x, s_{1:t}) + λ·BCE(r_t, y_t)\n\n**Representative Methods:** ThinkPRM, GenRM, GenPRM, GRAM-R², Process-based Self-Rewarding Language Models, GM-PRM, rStar-Math\n\n### Implicit PRMs (Section 3.3)\n\nInfer fine-grained rewards without step-level labels through outcome feedback, model self-evaluation, or consistency constraints.\n\n**Representative Methods:** FreePRM, Self-PRM, SP-PRM, SPARE, Universal PRM (AURORA)\n\n### Other Architectural Innovations (Section 3.4)\n\nMethods emphasizing structural innovations rather than loss functions:\n\n**Representative Methods:** GraphPRM, ASPRM (AdaptiveStep), Reward-SQL, RetrievalPRM, OpenPRM, MM-PRM, Multilingual PRM, PathFinder-PRM, Hierarchical Reward Model (HRM)\n\n---\n\n## 4. DATA GENERATION APPROACHES\n\n### 2.1 Human Annotation\n\n**Example:** PRM800K dataset with human-labeled step correctness, providing high-fidelity signals that serve as benchmarks and seed material for scalable methods.\n\n### 2.2 Automated Supervision\n\n**Key Techniques:**\n\n- **Symbolic Verification:** Math-Shepherd uses symbolic tools and consistency-checking heuristics\n- **Formal Verification:** FOVER uses Z3 and Isabelle tools for step-level error labels\n- **Tree Search:** OmegaPRM employs Monte Carlo Tree Search (MCTS) for error localization; URSA applies dual-view MCTS for multimodal mathematics\n- **Execution Feedback:** CodePRM uses automated tree search and execution feedback for code reasoning\n- **Pseudo-Supervision:** AlphaMath derives process supervision directly from outcome supervision\n- **Self-Evolution:** rStar-Math and Qwen2.5-Math PRM use consensus-filtering and self-evolutionary strategies\n- **Noise Reduction:** SCAN introduces self-denoising annotation framework\n\n**Benefit:** Unprecedented scale and efficiency; challenge: error propagation and verifier limitations.\n\n### 2.3 Semi-Automated Approaches\n\n**Pattern:** Limited human-curated examples expanded through automated verification or synthesis.\n\n**Domain Applications:**\n- **Multimodal:** VRPRM, Athena, ViLBench, VisualPRM\n- **Medical:** MedS³ starts with 8,000 human examples, expands via MCTS-based exploration\n- **Multi-domain:** VersaPRM generates synthetic data with small-scale manual verification\n- **Web Agents:** Web-Shepherd combines human oversight with automatic checks\n- **GUI Tasks:** GUI-Shepherd uses dual-pipeline strategy with hybrid annotations\n- **Active Learning:** ActPRM selectively queries human annotators when automated signals are uncertain\n\n---\n\n## 5. USAGE PARADIGMS\n\n### 4.1 Test-Time Scaling\n\n**Evolution:**\n1. **Re-ranking Phase:** Best-of-N evaluation with PRM scores\n2. **Generative Verification:** GenPRM produces verification chains before scoring\n3. **Search Integration:** MCTS, beam search, and retrieval-augmented reasoning\n4. **Adaptive Granularity:** AdaptiveStep dynamically partitions reasoning based on confidence\n\n**Key Methods:** PRM-BAS (beam annealing search), CodePRM (Generate–Verify–Refine pipeline), Web-Shepherd trajectory filtering\n\n### 4.2 RL for Policy Learning\n\n**Mechanism:** PRMs provide dense step-level feedback replacing sparse correctness signals.\n\n**Representative Approaches:**\n\n- **Progress Indicators:** PAV reframes PRM outputs as advantage-like progress indicators\n- **KL-Constrained RL:** ER-PRM embeds PRM rewards into KL-constrained objectives\n- **Credit Assignment:** PURE proposes min-form objective (opposed to summation) to prevent reward hacking; CAPO introduces verifiable generative credit assignment\n- **Token-Level Supervision:** Q-RM models Q-values over tokens for direct RL optimization\n- **Consistency Filtering:** PROF ranks responses based on process–outcome consistency, removing conflicting samples\n- **Actor-Critic:** AgentPRM integrates PRMs into actor–critic loops for agent tasks\n- **Infrastructure:** OpenR provides systematic framework for offline and online RL integration\n\n---\n\n## 6. DOWNSTREAM APPLICATIONS (Summary)\n\n**Math:** Multi-step derivation soundness, symbolic error detection, automated grading and proof validation\n\n**Code:** Execution feedback, semantic consistency, text-to-SQL verification, software engineering patches\n\n**Multimodal:** Visual-text coherence checks, reasoning trace re-ranking, grounded explanation selection\n\n**Text:** Partial translation refinement, multi-hop QA, retrieval-augmented reasoning improvement\n\n**Robotics:** Long-horizon decomposition into subgoal rewards for dense feedback in manipulation/navigation\n\n**Agents:** Trajectory criticism, progress reward, dead-end pruning, safety during inference\n\n**Industry:** Medical and financial reasoning with verifiable evidence-based logic for reliability\n\n**Multi-domain:** Generalizable PRMs transferring supervision across diverse tasks\n\n---\n\n## 7. BENCHMARKS (Section 6)\n\n**Mathematical Reasoning:**\n- PRMBench: 6,000+ problems with 80,000 step annotations\n- ProcessBench: Competition-level tasks emphasizing earliest-error detection\n- Socratic-PRMBench: ~3,000 flawed trajectories grouped into six error patterns\n\n**Multimodal:**\n- ViLBench: Vision-language task comparisons\n- VisualProcessBench: Human-labeled multimodal errors\n- MPBench: Multiple tasks assessing step correctness and answer aggregation\n\n**Long-Horizon:**\n- WebRewardBench: 40,000 step-level preference pairs for web agents\n\n**Robustness & Universality:**\n- GSM-DC: Distractors test resilience\n- UniversalBench: Cross-distribution generalization evaluation\n\n---\n\n## 8. DISCUSSION: COMPARATIVE ANALYSIS (Section 7)\n\n**Figure 2 Framework:** Six-aspect evaluation comparing rule-based rewards, ORMs, and PRMs\n\n| **Aspect** | **Rule-Based** | **ORMs** | **PRMs** |\n|---|---|---|---|\n| **Resource Efficiency** | Excellent (no training) | Good (single-stage) | Poor (step-level annotation) |\n| **Granularity** | Variable | Single outcome | High (step-specific) |\n| **Anti-Hacking Robustness** | Poor (mis-specification) | Excellent (ground-truth) | Moderate (length bias susceptible) |\n| **Generalization** | Poor (task-specific) | Excellent (task-agnostic) | Moderate (domain-specific granularity) |\n| **Interpretability** | Excellent (explicit) | Poor (black box) | Good (fine-grained explanation) |\n| **Functionality** | Restricted | Limited (outcome only) | Versatile (search, RL, credit assignment) |\n\n**Key Finding on Length Bias:** Analysis of PRM800K shows step-level standard deviation (71.7) exceeds trajectory-level (50.6), indicating PRMs are more susceptible to verbose but vacuous intermediate steps.\n\n---\n\n## 9. OPEN CHALLENGES & FUTURE DIRECTIONS\n\n### Identified in Discussion & Conclusion:\n\n**Resource Efficiency Challenge:** Step-wise annotation overhead (7-13 steps average per problem) creates workload several times higher than outcome labeling. Future work must reduce annotation costs via robust automation.\n\n**Generalization Limitation:** Step definitions for mathematical derivations differ from code execution traces, necessitating frequent re-adaptation across domains. Cross-domain PRM development remains an open frontier.\n\n**Integration with Agency:** Key challenges include integrating PRMs with agentic planning and memory systems for complex interactive tasks.\n\n**Anti-Hacking Robustness:** PRMs require defenses against reward hacking through length bias; research on calibration and uncertainty quantification needed.\n\n**Granularity Tension (Appendix B.3):** Defining \"a step\" remains contested—no consensus on appropriate granularity across reasoning domains.\n\n**Proxy-Reward Gap (Appendix B.4):** Distinction between proxy metrics (formal verification, execution) and actual utility for human-aligned reasoning.\n\n**Cognitive Scalability (Appendix B.1):** Human annotation capacity constraints limit scaling of high-fidelity supervision pipelines.\n\n**Echo Chambers & Goodhart's Law (Appendix B.2):** Automated supervision risks creating feedback loops where verifiers reinforce their own errors; proxies optimized away from true objectives.\n\n**Standardized Evaluation:** Need for consistent protocols across diverse domains and task types.\n\n---\n\n## 10. KEY CONTRIBUTIONS\n\nThe survey provides:\n\n1. **Systematic Organization:** Full-loop framework (data generation → PRM building → usage)\n2. **Taxonomy Clarity:** Four training paradigms (discriminative, generative, implicit, architectural)\n3. **Comprehensive Coverage:** 8+ application domains with 70+ representative methods\n4. **Comparative Analysis:** Six-dimension evaluation framework comparing reward mechanisms\n5. **Benchmark Summary:** 10+ major benchmarks across reasoning domains\n6. **Critical Discussion:** Identifies resource costs, generalization gaps, robustness risks, and theoretical tensions\n7. **GitHub Repository:** Actively maintained resource linking papers and implementations\n\n---\n\n## 11. PAPER LIMITATIONS (Section 9)\n\n- Taxonomy follows data–model–usage loop, potentially simplifying or abstracting hybrid methods\n- Benchmark and application summaries are selective rather than comprehensive\n- Some domain-specific datasets and proprietary evaluation suites not fully captured\n- Focus on step-level supervision may not capture emerging trajectory-level or state-level formulations",
    "durationMs": 41097,
    "url": "https://arxiv.org/html/2510.08049"
  },
  "sourceToolAssistantUUID": "69198027-84e5-4847-a187-072987a8ce86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "dbce5454-61ee-45f2-97f3-fef5f487fc96",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRM survey paper for research methodology",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---

### Assistant

_source line 18 · 2026-05-28T05:21:26.336Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me get more details on some specific aspects - the related work comparison, how they differentiate from prior surveys, and any reviewer feedback if available on OpenReview.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbce5454-61ee-45f2-97f3-fef5f487fc96",
  "isSidechain": false,
  "requestId": "req_011CbUQU3Y5763BYEkRmnAzw",
  "type": "assistant",
  "uuid": "db02bc8d-0365-46f7-a19a-aef47b36ab45",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBmGstQ44tukQLmnNHf78M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3974,
      "cache_read_input_tokens": 13871,
      "output_tokens": 439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 439,
          "cache_read_input_tokens": 13871,
          "cache_creation_input_tokens": 3974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3974
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

_source line 19 · 2026-05-28T05:21:26.522Z_

Now let me fetch more details on how they differentiate from prior surveys and check for any reviewer feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db02bc8d-0365-46f7-a19a-aef47b36ab45",
  "isSidechain": false,
  "requestId": "req_011CbUQU3Y5763BYEkRmnAzw",
  "type": "assistant",
  "uuid": "57802e46-e3af-405a-b651-431c97d80e3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBmGstQ44tukQLmnNHf78M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3974,
      "cache_read_input_tokens": 13871,
      "output_tokens": 439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 439,
          "cache_read_input_tokens": 13871,
          "cache_creation_input_tokens": 3974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3974
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

_source line 20 · 2026-05-28T05:21:30.382Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WkpGuptcRtNHMfWW7k7naX`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.08049",
  "prompt": "I need specific details on:\n1. How this survey differentiates itself from prior surveys — what existing surveys do they cite and what gap do they claim to fill? Look for any comparison table of surveys.\n2. The \"iterative loop\" framework they propose — how exactly do data generation, PRM training, and PRM usage feed back into each other?\n3. The specific insight about implicit PRMs — how do methods like FreePRM and AURORA work without step-level labels?\n4. The discussion about reward hacking, Goodhart's law, and echo chambers in detail\n5. Any specific numbers, statistics, or quantitative findings they report (e.g., how many papers surveyed, performance comparisons)\n6. The conclusion section in full detail"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57802e46-e3af-405a-b651-431c97d80e3d",
  "isSidechain": false,
  "requestId": "req_011CbUQU3Y5763BYEkRmnAzw",
  "type": "assistant",
  "uuid": "cf1dedaf-89ea-4ad1-96a7-df863b473181",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBmGstQ44tukQLmnNHf78M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3974,
      "cache_read_input_tokens": 13871,
      "output_tokens": 439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 439,
          "cache_read_input_tokens": 13871,
          "cache_creation_input_tokens": 3974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3974
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

_source line 21 · 2026-05-28T05:21:32.171Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Bv4fq6mBzwqb9y635uy421`</summary>

```json
{
  "url": "https://openreview.net/search?term=A+Survey+of+Process+Reward+Models&venue=all",
  "prompt": "Search for any OpenReview submissions related to \"A Survey of Process Reward Models\" by Zheng et al. Are there any reviews, comments, or ratings available? Extract any reviewer feedback if found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf1dedaf-89ea-4ad1-96a7-df863b473181",
  "isSidechain": false,
  "requestId": "req_011CbUQU3Y5763BYEkRmnAzw",
  "type": "assistant",
  "uuid": "d6d87bdc-c347-4c84-9e14-9bb148de0035",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBmGstQ44tukQLmnNHf78M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3974,
      "cache_read_input_tokens": 13871,
      "output_tokens": 439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 439,
          "cache_read_input_tokens": 13871,
          "cache_creation_input_tokens": 3974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3974
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

_source line 22 · 2026-05-28T05:21:35.298Z_

<details><summary>↩ Tool result · `toolu_01Bv4fq6mBzwqb9y635uy421`</summary>

```text
# Search Results for "A Survey of Process Reward Models"

Based on the provided OpenReview.net webpage content, I cannot locate any specific submissions, reviews, comments, or ratings related to "A Survey of Process Reward Models" by Zheng et al.

The page content shows only the general OpenReview.net interface elements, including navigation links, footer information, and site description stating that "OpenReview is a long-term project to advance science through improved peer review with legal nonprofit status."

To find this survey and its associated reviewer feedback, you would need to:

1. Visit OpenReview.net directly
2. Use their search functionality to query the specific paper title or author name
3. Browse the relevant conference or venue where the paper was submitted

No reviewer feedback, ratings, or comments are available in the content provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6d87bdc-c347-4c84-9e14-9bb148de0035",
  "isSidechain": false,
  "promptId": "a99e86ca-aeb1-413c-a1fe-23ebc5ea6113",
  "type": "user",
  "uuid": "715d2bb5-084f-47d7-a5c9-85653ce7755e",
  "toolUseResult": {
    "bytes": 62348,
    "code": 200,
    "codeText": "OK",
    "result": "# Search Results for \"A Survey of Process Reward Models\"\n\nBased on the provided OpenReview.net webpage content, I cannot locate any specific submissions, reviews, comments, or ratings related to \"A Survey of Process Reward Models\" by Zheng et al.\n\nThe page content shows only the general OpenReview.net interface elements, including navigation links, footer information, and site description stating that \"OpenReview is a long-term project to advance science through improved peer review with legal nonprofit status.\"\n\nTo find this survey and its associated reviewer feedback, you would need to:\n\n1. Visit OpenReview.net directly\n2. Use their search functionality to query the specific paper title or author name\n3. Browse the relevant conference or venue where the paper was submitted\n\nNo reviewer feedback, ratings, or comments are available in the content provided.",
    "durationMs": 3124,
    "url": "https://openreview.net/search?term=A+Survey+of+Process+Reward+Models&venue=all"
  },
  "sourceToolAssistantUUID": "d6d87bdc-c347-4c84-9e14-9bb148de0035",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T05:21:42.736Z_

<details><summary>↩ Tool result · `toolu_01WkpGuptcRtNHMfWW7k7naX`</summary>

```text
# Summary of Process Reward Models Survey

## 1. Differentiation from Prior Surveys

The authors explicitly position their work against three existing survey categories:

> "Current discussions mainly focus on either test-time scaling paradigms...broad reward modeling taxonomies...or generic deep RL reward design, whereas our PRM survey uniquely targets step-level process reward modeling"

They claim their innovation is organizing "the full loop of data generation, PRM building, and usage (test-time scaling and PRM-guided RL) for fine-grained reasoning supervision." No comparison table appears in the provided content, but they identify a gap in prior work's fragmentation across different aspects of PRMs.

## 2. The Iterative Loop Framework

The core contribution is visualized in Figure 1, describing a cyclical process:

**Data Generation → PRM Training → PRM Usage → Better Data Production**

The authors state: "Process Reward Models coupled with a closed loop: _generate process data_ → _train PRMs_ → _use PRMs_ (test-time scaling or RL) → _produce better data_. This loop transforms reward modeling from a one-shot verdict to an iterative controller of reasoning."

The loop enables adaptive computation allocation during inference and reinforcement learning policy improvements that generate superior training trajectories.

## 3. Implicit PRMs and Label-Free Approaches

Implicit PRMs extract fine-grained rewards without explicit step-level annotations through indirect supervision mechanisms:

- **FreePRM**: "trains a reward model without ground-truth process labels by pseudo-labeling via outcome correctness"
- **AURORA** (Universal PRM): "employs ensemble prompting and reverse verification to produce domain-agnostic self-supervised reward signals"
- **Self-PRM**: demonstrates that "LLMs under RL training can internally induce a PRM-style self-rewarding capability"

These methods leverage outcome signals, consistency constraints, or model self-evaluation as weak supervision proxies.

## 4. Reward Hacking and Goodhart's Law Discussion

The survey dedicates Appendix Section B.2 to these concerns but provides limited detail in the excerpt. In Section 7 (Anti-Hacking Robustness), they report:

> "Standard deviation of token length at step level is 71.7, significantly higher than trajectory-level SD of 50.6...greater instability indicates that step-level signals are noisier and less constrained, allowing models to more easily hack the reward by generating verbose but vacuous intermediate steps"

This quantifies how PRMs exhibit greater vulnerability to length-based exploitation than outcome reward models.

## 5. Quantitative Findings

Key statistics reported:

- **ProcessBench**: competition-level mathematical reasoning tasks
- **PRMBench**: "over 6,000 problems with 80,000 step annotations and multidimensional labels"
- **Benchmark step counts**: ProcessBench averages 7.1 steps, PRMBench 13.4 steps per solution
- **Annotation workload**: "7-13× higher than ORMs" due to per-step labeling

The paper doesn't report total papers surveyed count in accessible sections.

## 6. Conclusion Details

The conclusion (Section 8) synthesizes key themes:

> "Process Reward Models shift reasoning alignment from coarse outcome judgments to fine-grained, step-level feedback, forming a closed loop of data generation, model training, and usage that continually improves reasoning quality"

Primary challenges identified:
- Reducing annotation costs through robust automation
- Improving cross-domain generalization
- Integrating PRMs with agentic planning and memory
- Establishing standardized evaluation protocols

The authors note their vision addresses "safer, more interpretable, and broadly applicable reasoning systems" but acknowledge study limitations in completeness of benchmark/application coverage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf1dedaf-89ea-4ad1-96a7-df863b473181",
  "isSidechain": false,
  "promptId": "a99e86ca-aeb1-413c-a1fe-23ebc5ea6113",
  "type": "user",
  "uuid": "0219613c-a57d-4933-9092-0986f67df4e9",
  "toolUseResult": {
    "bytes": 285000,
    "code": 200,
    "codeText": "OK",
    "result": "# Summary of Process Reward Models Survey\n\n## 1. Differentiation from Prior Surveys\n\nThe authors explicitly position their work against three existing survey categories:\n\n> \"Current discussions mainly focus on either test-time scaling paradigms...broad reward modeling taxonomies...or generic deep RL reward design, whereas our PRM survey uniquely targets step-level process reward modeling\"\n\nThey claim their innovation is organizing \"the full loop of data generation, PRM building, and usage (test-time scaling and PRM-guided RL) for fine-grained reasoning supervision.\" No comparison table appears in the provided content, but they identify a gap in prior work's fragmentation across different aspects of PRMs.\n\n## 2. The Iterative Loop Framework\n\nThe core contribution is visualized in Figure 1, describing a cyclical process:\n\n**Data Generation → PRM Training → PRM Usage → Better Data Production**\n\nThe authors state: \"Process Reward Models coupled with a closed loop: _generate process data_ → _train PRMs_ → _use PRMs_ (test-time scaling or RL) → _produce better data_. This loop transforms reward modeling from a one-shot verdict to an iterative controller of reasoning.\"\n\nThe loop enables adaptive computation allocation during inference and reinforcement learning policy improvements that generate superior training trajectories.\n\n## 3. Implicit PRMs and Label-Free Approaches\n\nImplicit PRMs extract fine-grained rewards without explicit step-level annotations through indirect supervision mechanisms:\n\n- **FreePRM**: \"trains a reward model without ground-truth process labels by pseudo-labeling via outcome correctness\"\n- **AURORA** (Universal PRM): \"employs ensemble prompting and reverse verification to produce domain-agnostic self-supervised reward signals\"\n- **Self-PRM**: demonstrates that \"LLMs under RL training can internally induce a PRM-style self-rewarding capability\"\n\nThese methods leverage outcome signals, consistency constraints, or model self-evaluation as weak supervision proxies.\n\n## 4. Reward Hacking and Goodhart's Law Discussion\n\nThe survey dedicates Appendix Section B.2 to these concerns but provides limited detail in the excerpt. In Section 7 (Anti-Hacking Robustness), they report:\n\n> \"Standard deviation of token length at step level is 71.7, significantly higher than trajectory-level SD of 50.6...greater instability indicates that step-level signals are noisier and less constrained, allowing models to more easily hack the reward by generating verbose but vacuous intermediate steps\"\n\nThis quantifies how PRMs exhibit greater vulnerability to length-based exploitation than outcome reward models.\n\n## 5. Quantitative Findings\n\nKey statistics reported:\n\n- **ProcessBench**: competition-level mathematical reasoning tasks\n- **PRMBench**: \"over 6,000 problems with 80,000 step annotations and multidimensional labels\"\n- **Benchmark step counts**: ProcessBench averages 7.1 steps, PRMBench 13.4 steps per solution\n- **Annotation workload**: \"7-13× higher than ORMs\" due to per-step labeling\n\nThe paper doesn't report total papers surveyed count in accessible sections.\n\n## 6. Conclusion Details\n\nThe conclusion (Section 8) synthesizes key themes:\n\n> \"Process Reward Models shift reasoning alignment from coarse outcome judgments to fine-grained, step-level feedback, forming a closed loop of data generation, model training, and usage that continually improves reasoning quality\"\n\nPrimary challenges identified:\n- Reducing annotation costs through robust automation\n- Improving cross-domain generalization\n- Integrating PRMs with agentic planning and memory\n- Establishing standardized evaluation protocols\n\nThe authors note their vision addresses \"safer, more interpretable, and broadly applicable reasoning systems\" but acknowledge study limitations in completeness of benchmark/application coverage.",
    "durationMs": 12350,
    "url": "https://arxiv.org/html/2510.08049"
  },
  "sourceToolAssistantUUID": "cf1dedaf-89ea-4ad1-96a7-df863b473181",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-28T05:21:46.274Z_

<details><summary>Logged reasoning block</summary>

```text
Let me also try to get the paper's full content from the HTML version to understand more about the specific methods, particularly the data generation taxonomy and the key insights about combining different approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0219613c-a57d-4933-9092-0986f67df4e9",
  "isSidechain": false,
  "requestId": "req_011CbUQVeU4BfqBEABhcKGTX",
  "type": "assistant",
  "uuid": "8d124cb6-8d44-479d-abe7-8ae899c66e7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aj6V5ZMPyGVfoiQQUfd1L1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 209,
      "cache_creation_input_tokens": 1328,
      "cache_read_input_tokens": 17845,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 209,
          "output_tokens": 341,
          "cache_read_input_tokens": 17845,
          "cache_creation_input_tokens": 1328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1328
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

_source line 25 · 2026-05-28T05:21:46.579Z_

Let me get more specific technical details from the paper, particularly the data generation methods and the key comparative insights.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d124cb6-8d44-479d-abe7-8ae899c66e7a",
  "isSidechain": false,
  "requestId": "req_011CbUQVeU4BfqBEABhcKGTX",
  "type": "assistant",
  "uuid": "8bf4e57c-46f7-4dea-a48e-c09a97bafb7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aj6V5ZMPyGVfoiQQUfd1L1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 209,
      "cache_creation_input_tokens": 1328,
      "cache_read_input_tokens": 17845,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 209,
          "output_tokens": 341,
          "cache_read_input_tokens": 17845,
          "cache_creation_input_tokens": 1328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1328
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

_source line 26 · 2026-05-28T05:21:52.070Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018SyKir2chtwSaG7F56XdZm`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.08049",
  "prompt": "Focus on these specific aspects:\n1. The FULL abstract of the paper — every sentence verbatim\n2. How they organize the data generation section — what is the taxonomy? What are the specific automated data generation methods (Monte Carlo estimation, symbolic verification, tree search, etc.)? How do they compare?\n3. The comparison between discriminative, generative, and implicit PRMs — what are the tradeoffs they identify? Which is most promising?\n4. How do they define \"process reward\" formally vs \"outcome reward\"? What mathematical formulations do they give?\n5. The related work / prior surveys comparison — how do they position against LLM reasoning surveys, reward model surveys, and test-time compute surveys?\n6. Any tables listing methods, especially Table 1 or similar summary tables\n7. Statistics on how many papers/methods they cover"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bf4e57c-46f7-4dea-a48e-c09a97bafb7a",
  "isSidechain": false,
  "requestId": "req_011CbUQVeU4BfqBEABhcKGTX",
  "type": "assistant",
  "uuid": "02c26005-1c69-4e9a-9328-ab741040f195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aj6V5ZMPyGVfoiQQUfd1L1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 209,
      "cache_creation_input_tokens": 1328,
      "cache_read_input_tokens": 17845,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 209,
          "output_tokens": 341,
          "cache_read_input_tokens": 17845,
          "cache_creation_input_tokens": 1328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1328
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

_source line 27 · 2026-05-28T05:22:07.057Z_

<details><summary>↩ Tool result · `toolu_018SyKir2chtwSaG7F56XdZm`</summary>

```text
# Process Reward Models Survey: Key Findings

## 1. Full Abstract

"Although Large Language Models (LLMs) exhibit advanced reasoning ability, conventional alignment remains largely dominated by outcome reward models (ORMs) that judge only final answers. *Process Reward Models* (PRMs) address this gap by evaluating and guiding reasoning at the step or trajectory level. This survey provides a systematic overview of PRMs through the full loop: how to *generate process data*, *build PRMs*, and *use PRMs* for test-time scaling and reinforcement learning. We summarize applications across math, code, text, multimodal reasoning, robotics, and agents, and review emerging benchmarks. Our goal is to clarify design spaces, reveal open challenges, and guide future research toward fine-grained, robust reasoning alignment."

## 2. Data Generation Taxonomy

The authors organize process supervision into three paradigms:

**Human Annotation**: Exemplified by PRM800K, where annotators manually validate intermediate reasoning steps with high fidelity but limited scalability.

**Automated Supervision**: Includes:
- Symbolic verification (Math-Shepherd using consistency checks)
- Formal verification tools (FOVER using Z3, Isabelle)
- Monte Carlo Tree Search (OmegaPRM using MCTS for error localization)
- Self-evolutionary strategies (rStar-Math, Qwen2.5-Math)
- Execution feedback pipelines (CodePRM)
- Pseudo-process supervision from outcome signals (AlphaMath)

**Semi-automated Approaches**: Blend human-curated seeds with automated expansion (VRPRM, Athena, MedS³, VersaPRM).

The key trade-off: automation enables scale but risks error propagation and verifier limitations.

## 3. Discriminative vs. Generative vs. Implicit PRMs

**Discriminative PRMs** learn scalar scoring functions over intermediate states using pointwise (BCE/MSE) or pairwise (preference) losses. Strengths: foundational, interpretable. Weaknesses: may suffer length bias.

**Generative PRMs** first generate verification chains, then score based on those chains. Tradeoffs: maintain longer reasoning but require dual training objectives combining likelihood and supervision losses.

**Implicit PRMs** infer fine-grained rewards without step-level labels using outcome feedback, self-evaluation, or consistency constraints. Advantages: reduce annotation burden. Challenges: weaker supervision signals.

The survey suggests discriminative methods dominate current practice, with generative approaches emerging for enhanced interpretability and reasoning depth.

## 4. Formal Definitions

**Process Reward (Discriminative)**: r_t = σ(f_θ(x, s₁:ₜ)) ∈ (0,1), assigning scalar scores to partial solutions.

**Outcome Reward**: Single final-state judgment, contrasted as coarse-grained versus step-level process assessment.

The mathematical distinction highlights PRMs' granularity advantage: "essentially, the granularity of a PRM is inherently multiplied by the number of steps in a solution" versus outcome-only signals.

## 5. Positioning vs. Prior Surveys

This PRM survey uniquely targets "step-level process reward modeling" rather than broad test-time scaling paradigms, generic deep RL reward design, or outcome-centric alignment. It organizes around the closed loop: *data generation* → *training* → *usage* (test-time scaling and RL).

## 6. Summary Tables

The survey includes Figure 2 comparing rule-based rewards, ORMs, and PRMs across six dimensions:
- **Resource Efficiency**: PRMs most costly (step-wise annotation)
- **Granularity**: PRMs excel (multiplied by step count)
- **Anti-Hacking Robustness**: ORMs strongest; PRMs vulnerable to length hacking
- **Generalization**: ORMs superior; PRMs domain-specific
- **Interpretability**: PRMs bridge rule-based transparency and ORM opacity
- **Functionality**: PRMs most versatile for search and RL

## 7. Paper Coverage

The survey references approximately **100+ cited works** spanning foundational methods (PRM800K, Math-Shepherd), recent innovations (generative and implicit variants), applications across eight domains (math, code, multimodal, text, robotics, agents, industry, multi-domain), and six major benchmarks (PRMBench, ProcessBench, ViLBench, MPBench, WebRewardBench, UniversalBench).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02c26005-1c69-4e9a-9328-ab741040f195",
  "isSidechain": false,
  "promptId": "a99e86ca-aeb1-413c-a1fe-23ebc5ea6113",
  "type": "user",
  "uuid": "b36680c8-b825-4c32-a2d5-4aef4a803c37",
  "toolUseResult": {
    "bytes": 285000,
    "code": 200,
    "codeText": "OK",
    "result": "# Process Reward Models Survey: Key Findings\n\n## 1. Full Abstract\n\n\"Although Large Language Models (LLMs) exhibit advanced reasoning ability, conventional alignment remains largely dominated by outcome reward models (ORMs) that judge only final answers. *Process Reward Models* (PRMs) address this gap by evaluating and guiding reasoning at the step or trajectory level. This survey provides a systematic overview of PRMs through the full loop: how to *generate process data*, *build PRMs*, and *use PRMs* for test-time scaling and reinforcement learning. We summarize applications across math, code, text, multimodal reasoning, robotics, and agents, and review emerging benchmarks. Our goal is to clarify design spaces, reveal open challenges, and guide future research toward fine-grained, robust reasoning alignment.\"\n\n## 2. Data Generation Taxonomy\n\nThe authors organize process supervision into three paradigms:\n\n**Human Annotation**: Exemplified by PRM800K, where annotators manually validate intermediate reasoning steps with high fidelity but limited scalability.\n\n**Automated Supervision**: Includes:\n- Symbolic verification (Math-Shepherd using consistency checks)\n- Formal verification tools (FOVER using Z3, Isabelle)\n- Monte Carlo Tree Search (OmegaPRM using MCTS for error localization)\n- Self-evolutionary strategies (rStar-Math, Qwen2.5-Math)\n- Execution feedback pipelines (CodePRM)\n- Pseudo-process supervision from outcome signals (AlphaMath)\n\n**Semi-automated Approaches**: Blend human-curated seeds with automated expansion (VRPRM, Athena, MedS³, VersaPRM).\n\nThe key trade-off: automation enables scale but risks error propagation and verifier limitations.\n\n## 3. Discriminative vs. Generative vs. Implicit PRMs\n\n**Discriminative PRMs** learn scalar scoring functions over intermediate states using pointwise (BCE/MSE) or pairwise (preference) losses. Strengths: foundational, interpretable. Weaknesses: may suffer length bias.\n\n**Generative PRMs** first generate verification chains, then score based on those chains. Tradeoffs: maintain longer reasoning but require dual training objectives combining likelihood and supervision losses.\n\n**Implicit PRMs** infer fine-grained rewards without step-level labels using outcome feedback, self-evaluation, or consistency constraints. Advantages: reduce annotation burden. Challenges: weaker supervision signals.\n\nThe survey suggests discriminative methods dominate current practice, with generative approaches emerging for enhanced interpretability and reasoning depth.\n\n## 4. Formal Definitions\n\n**Process Reward (Discriminative)**: r_t = σ(f_θ(x, s₁:ₜ)) ∈ (0,1), assigning scalar scores to partial solutions.\n\n**Outcome Reward**: Single final-state judgment, contrasted as coarse-grained versus step-level process assessment.\n\nThe mathematical distinction highlights PRMs' granularity advantage: \"essentially, the granularity of a PRM is inherently multiplied by the number of steps in a solution\" versus outcome-only signals.\n\n## 5. Positioning vs. Prior Surveys\n\nThis PRM survey uniquely targets \"step-level process reward modeling\" rather than broad test-time scaling paradigms, generic deep RL reward design, or outcome-centric alignment. It organizes around the closed loop: *data generation* → *training* → *usage* (test-time scaling and RL).\n\n## 6. Summary Tables\n\nThe survey includes Figure 2 comparing rule-based rewards, ORMs, and PRMs across six dimensions:\n- **Resource Efficiency**: PRMs most costly (step-wise annotation)\n- **Granularity**: PRMs excel (multiplied by step count)\n- **Anti-Hacking Robustness**: ORMs strongest; PRMs vulnerable to length hacking\n- **Generalization**: ORMs superior; PRMs domain-specific\n- **Interpretability**: PRMs bridge rule-based transparency and ORM opacity\n- **Functionality**: PRMs most versatile for search and RL\n\n## 7. Paper Coverage\n\nThe survey references approximately **100+ cited works** spanning foundational methods (PRM800K, Math-Shepherd), recent innovations (generative and implicit variants), applications across eight domains (math, code, multimodal, text, robotics, agents, industry, multi-domain), and six major benchmarks (PRMBench, ProcessBench, ViLBench, MPBench, WebRewardBench, UniversalBench).",
    "durationMs": 14982,
    "url": "https://arxiv.org/html/2510.08049"
  },
  "sourceToolAssistantUUID": "02c26005-1c69-4e9a-9328-ab741040f195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-28T05:22:18.595Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of this paper. Let me synthesize my analysis into the requested JSON format.

Key observations for my analysis:

1. **Problem identification**: The authors identified that existing surveys covered test-time scaling, reward modeling broadly, and RL reward design, but none organized the full PRM lifecycle as a closed loop. The gap was the fragmented treatment of PRMs across different survey categories.

2. **Key insight**: The "iterative loop" framing — data generation → PRM training → PRM usage → better data — is the central intellectual contribution. This reframes reward modeling from a static judgment tool into a dynamic reasoning controller.
   
3. **Innovation type**: This is fundamentally an "analysis" paper — a survey that provides a new organizational framework (taxonomy) for an emerging field.

4. **What makes it good**: The paper excels through comprehensive coverage spanning over a hundred papers across eight domains with six benchmarks, introduces a four-way PRM taxonomy and six-dimension comparative framework, backs up open problems with quantitative evidence like length bias statistics, and most importantly, unifies fragmented work through the closed-loop framing.

5. **Limitations**: The authors acknowledge selective coverage, some taxonomy simplification, and a focus on step-level analysis that might overlook trajectory-level formulations.

6. **No reviewer feedback** since this is an arXiv preprint, so I'll move forward with composing the final JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b36680c8-b825-4c32-a2d5-4aef4a803c37",
  "isSidechain": false,
  "requestId": "req_011CbUQXSTYxNpznV2ahj6B3",
  "type": "assistant",
  "uuid": "bba06f7e-830d-4059-b399-a0aad9ce3f9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SA2XBeMX4oKSfeLrPitYGN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 19173,
      "output_tokens": 2174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2174,
          "cache_read_input_tokens": 19173,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1603
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

_source line 29 · 2026-05-28T05:23:03.809Z_

Now I have comprehensive information about the paper. Let me synthesize the analysis.

```json
{
  "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
  "venue": "arXiv 2025 (preprint survey, last revised April 2026; not peer-reviewed at a top venue)",
  "problem_identification": "The authors identified that the rapidly growing PRM literature was fragmented across three disconnected survey categories — test-time scaling paradigms, broad reward model taxonomies, and generic deep-RL reward design — but none organized the full PRM lifecycle end-to-end. They found this gap by observing that existing work treated data generation, model training, and inference-time usage as separate concerns, missing the critical feedback loop that makes PRMs iteratively self-improving. The insight that these three stages form a closed cycle (generate data → train PRM → use PRM → produce better data) was hiding in plain sight across dozens of papers but had never been explicitly articulated as an organizing principle.",
  "key_insight": "PRMs are not just step-level scoring functions — they are iterative reasoning controllers. The core reframing is the closed loop (data → training → usage → better data) that transforms reward modeling from a one-shot verdict into a continually improving system, and this loop is the right lens through which to unify the entire subfield's fragmented methods.",
  "innovation_type": "analysis",
  "method_summary": "The survey organizes ~100+ papers through a three-stage closed-loop framework: (1) Data generation, taxonomized into human annotation (PRM800K), automated supervision (Monte Carlo estimation via Math-Shepherd, formal verification via FOVER/Z3, MCTS-based search via OmegaPRM, self-evolutionary strategies via rStar-Math), and semi-automated hybrids. (2) PRM construction, classified into four paradigms — discriminative (scalar scoring with BCE/pairwise losses), generative (produce verification chains then judge), implicit (derive process rewards from outcome signals without step labels, e.g., FreePRM, AURORA), and architectural innovations (graph-based, adaptive-step, retrieval-augmented). (3) PRM usage, split into test-time scaling (best-of-N reranking → generative verification → MCTS/beam search → adaptive granularity) and RL-based policy learning (dense step-level rewards replacing sparse outcome signals, with methods like PAV, PURE, and Q-RM). A six-dimension comparative analysis (resource efficiency, granularity, anti-hacking robustness, generalization, interpretability, functionality) provides quantitative comparison against rule-based rewards and ORMs.",
  "what_makes_it_good": "The paper succeeds because it imposed intellectual order on a chaotic, fast-moving field — the four-way PRM taxonomy (discriminative/generative/implicit/architectural) and the closed-loop framing give researchers a shared vocabulary and mental model that didn't exist before. The six-dimension comparative analysis goes beyond listing methods by surfacing non-obvious tradeoffs with quantitative evidence (e.g., step-level length SD of 71.7 vs. trajectory-level 50.6, proving PRMs are more vulnerable to reward hacking than ORMs). The breadth across 8 application domains with concrete method catalogs makes it an immediately useful reference, not just an intellectual exercise.",
  "limitations_acknowledged": "The authors acknowledge their taxonomy may oversimplify hybrid methods that span categories, their benchmark and application coverage is selective rather than exhaustive, and their step-level focus may not capture emerging trajectory-level or state-level formulations that blur the boundary between process and outcome supervision.",
  "open_questions": [
    "How do we define 'a step' consistently across domains? Mathematical derivation steps, code execution traces, and agent action sequences have fundamentally different granularities, and no consensus exists — this is the granularity problem that limits cross-domain PRM transfer.",
    "How do we break the echo chamber risk in automated PRM data generation? When verifiers generate their own training data (the closed loop), Goodhart's law predicts they will optimize proxies away from true reasoning quality — what are the theoretical guarantees or practical safeguards against this collapse?",
    "Can implicit PRMs (which require no step-level labels) match or surpass discriminative PRMs in practice? If so, the entire costly annotation pipeline becomes unnecessary — but current evidence is mixed and domain-specific."
  ],
  "building_blocks": [
    "PRM800K dataset (human-annotated step-level labels as gold standard)",
    "Math-Shepherd (symbolic verification for automated step labeling)",
    "OmegaPRM / MCTS-based error localization",
    "Monte Carlo estimation for step-level credit assignment",
    "GenRM / ThinkPRM (generative verification chain paradigm)",
    "FreePRM / AURORA (label-free implicit process rewards)",
    "Best-of-N reranking with PRM scores",
    "PRMBench and ProcessBench (evaluation benchmarks with 80K+ step annotations)",
    "Six-dimension reward model evaluation framework (resource efficiency, granularity, robustness, generalization, interpretability, functionality)",
    "PAV (process advantage verifier for RL integration)",
    "PURE (min-form objective to prevent reward hacking in PRM-guided RL)",
    "rStar-Math (self-evolutionary data generation)",
    "AdaptiveStep PRM (dynamic granularity partitioning)"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This survey is the definitive map of our research area — it reveals that the most promising open frontiers for step-level verification and credit assignment are: (1) implicit/label-free PRMs that could eliminate the annotation bottleneck, (2) anti-hacking defenses against length bias and proxy gaming at the step level, and (3) the unsolved 'granularity problem' of what constitutes a step. Any new contribution in PRM-based credit assignment should position itself against this taxonomy and target one of the gaps it identifies — particularly the echo chamber risk in self-supervised PRM loops and the lack of cross-domain step definitions."
}
```

## Key Takeaways for Research Craft

**What made this survey effective as research (not just a literature review):**

1. **The unifying abstraction was the real contribution.** The closed-loop framing (data → model → usage → better data) isn't technically novel — it's an observation. But by naming it and organizing 100+ papers around it, the authors created a conceptual tool that accelerates everyone else's thinking. *Lesson: Sometimes the best research contribution is giving a field its organizing principle.*

2. **Quantitative comparison, not just taxonomic listing.** The step-level length SD (71.7) vs. trajectory-level SD (50.6) finding is a small empirical nugget buried in a survey — but it's the kind of concrete evidence that transforms "PRMs might be hackable" into "PRMs are measurably more hackable, and here's why." *Lesson: Even in survey papers, one original empirical finding can anchor the entire argument.*

3. **The four-paradigm taxonomy (discriminative/generative/implicit/architectural) was well-chosen** because it's organized by *what information the model requires*, not by application domain or chronology. This makes it predictive — you can ask "what would a new PRM look like?" and the taxonomy gives you search directions. *Lesson: Good taxonomies are organized by the dimension that generates new ideas, not the one that's easiest to enumerate.*

4. **Identifying the granularity problem as foundational.** The observation that "what is a step?" has no cross-domain answer is the kind of insight that opens research programs. *Lesson: The most valuable thing a survey can do is find the load-bearing assumption that everyone is making differently without realizing it.*

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bba06f7e-830d-4059-b399-a0aad9ce3f9d",
  "isSidechain": false,
  "requestId": "req_011CbUQXSTYxNpznV2ahj6B3",
  "type": "assistant",
  "uuid": "2da21f16-c08a-4a67-87f1-35b6948135cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SA2XBeMX4oKSfeLrPitYGN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 19173,
      "output_tokens": 2174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2174,
          "cache_read_input_tokens": 19173,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1603
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "2da21f16-c08a-4a67-87f1-35b6948135cd",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRM survey paper for research methodology",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-28 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "2da21f16-c08a-4a67-87f1-35b6948135cd",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze PRM survey paper for research methodology",
  "sessionId": "540f20bc-02e4-4934-866e-739fdd700aa7"
}
```

---
