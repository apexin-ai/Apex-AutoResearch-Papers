# Research conversation: You are a senior ML researcher performing a deep analysis of a published paper. **Today's date: 2026-05-27 (UTC).** ## Y

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/6fd3beeb-b487-48e2-ab3c-35d10e133c80.jsonl`
- **Structured JSON:** [`78ac6a3c47b02d40f625.json`](../../sessions/78/78ac6a3c47b02d40f625.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T15:57:08.168Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T15:57:08.168Z",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "content": "You are a senior ML researcher performing a deep analysis of a published paper.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Your goal\n\nAnalyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?\n\n## Research context\n\nWe are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**\n\n## Paper to analyze\n\n{\n  \"title\": \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\",\n  \"authors\": \"Jian Zhao et al.\",\n  \"venue\": \"AAAI 2026\",\n  \"url\": \"https://arxiv.org/abs/2504.00891\",\n  \"why_important\": \"Accepted at AAAI 2026; redefines process supervision as a generative task with code verification; 1.5B model outperforms GPT-4o on ProcessBench; 7B model surpasses Qwen2.5-Math-PRM-72B; trained on only 23K examples\",\n  \"one_line_summary\": \"Redefines PRM as a generative reasoning task with explicit chain-of-thought and code verification, enabling a 1.5B parameter model to outperform GPT-4o on step-level verification using only 23K training examples.\"\n}\n\n## Instructions\n\n1. **Deep read**: Use WebFetch to read this paper's full abstract, introduction, method section, and conclusion on arXiv or OpenReview. If it's on OpenReview, also read the reviewer comments and author responses.\n\n2. **Analyze the innovation structure**: Don't just summarize — dissect HOW the authors arrived at their contribution:\n   - What gap did they identify and HOW did they find it?\n   - What was the key insight that others missed?\n   - How did they formulate the problem differently from prior work?\n   - What existing technique did they adapt/combine/simplify?\n\n3. **Learn from reviewers**: If you can find reviewer comments, extract:\n   - What did reviewers praise most?\n   - What concerns were raised and how were they addressed?\n   - What would have made this paper even stronger?\n\n## Output format\n\nOutput a single JSON object:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem did they identify? How did they find it? (2-3 sentences)\",\n  \"key_insight\": \"The core intellectual contribution — the aha moment (1-2 sentences)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach in 3-5 sentences — enough to understand the machinery\",\n  \"what_makes_it_good\": \"Why did this paper get accepted? What would reviewers have liked? (2-3 sentences)\",\n  \"limitations_acknowledged\": \"What gaps did the authors themselves identify? (1-2 sentences)\",\n  \"open_questions\": \"What follow-up questions does this paper raise? What remains unsolved? (2-3 bullet points)\",\n  \"building_blocks\": [\"List of methods/tools/datasets used that could be reused\"],\n  \"reviewer_feedback_summary\": \"If found on OpenReview: key praise and concerns. Otherwise: null\",\n  \"relevance_to_seed\": \"How does this paper relate to our research area? What can we learn from it? (1-2 sentences)\"\n}\n\nBe analytical, not descriptive. We want to learn the CRAFT of doing good research, not just know what this paper did."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T15:57:08.171Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T15:57:08.171Z",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

## Round 1

52 recorded events

### User

_source line 3 · 2026-05-27T15:57:08.185Z_

You are a senior ML researcher performing a deep analysis of a published paper.

**Today's date: 2026-05-27 (UTC).**

## Your goal

Analyze this paper NOT just for what it does, but for **HOW it innovates** — what can we learn from its approach to doing research? What made this paper good enough for a top venue?

## Research context

We are generating ideas in the area of: **Process Reward Models for Mathematical Reasoning — Step-Level Verification and Credit Assignment**

## Paper to analyze

{
  "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
  "authors": "Jian Zhao et al.",
  "venue": "AAAI 2026",
  "url": "https://arxiv.org/abs/2504.00891",
  "why_important": "Accepted at AAAI 2026; redefines process supervision as a generative task with code verification; 1.5B model outperforms GPT-4o on ProcessBench; 7B model surpasses Qwen2.5-Math-PRM-72B; trained on only 23K examples",
  "one_line_summary": "Redefines PRM as a generative reasoning task with explicit chain-of-thought and code verification, enabling a 1.5B parameter model to outperform GPT-4o on step-level verification using only 23K training examples."
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
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "20013aba-800a-47a1-bf07-b5d45febc73b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T15:57:08.184Z_

```json
{
  "parentUuid": "20013aba-800a-47a1-bf07-b5d45febc73b",
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
  "uuid": "648591fd-689c-4586-a61b-ff79e47bc035",
  "timestamp": "2026-05-27T15:57:08.184Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T15:57:08.184Z_

```json
{
  "parentUuid": "648591fd-689c-4586-a61b-ff79e47bc035",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "424cdaf1-98b3-4bde-8c58-7284de7b6e01",
  "timestamp": "2026-05-27T15:57:08.184Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
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
  "aiTitle": "Analyze GenPRM paper for research innovation",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Assistant

_source line 7 · 2026-05-27T15:57:12.171Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the paper from arXiv to get the full details. I'll also check if it's available on OpenReview for reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "424cdaf1-98b3-4bde-8c58-7284de7b6e01",
  "isSidechain": false,
  "requestId": "req_011CbTM99Pv6GCT3vSm1bu9y",
  "type": "assistant",
  "uuid": "babbd933-cdda-496a-a87b-668ffea56fce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Qu65HDHSkrKHFc9n23Wri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2242,
      "cache_read_input_tokens": 11014,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 123,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2242
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

_source line 8 · 2026-05-27T15:57:12.305Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NCFaJQi6wUMQdHms6mfefz`</summary>

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
  "parentUuid": "babbd933-cdda-496a-a87b-668ffea56fce",
  "isSidechain": false,
  "requestId": "req_011CbTM99Pv6GCT3vSm1bu9y",
  "type": "assistant",
  "uuid": "42f9db93-ed54-476c-9cdd-b3f31d63d33f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Qu65HDHSkrKHFc9n23Wri",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2242,
      "cache_read_input_tokens": 11014,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 123,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 2242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2242
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

_source line 9 · 2026-05-27T15:57:12.313Z_

<details><summary>↩ Tool result · `toolu_01NCFaJQi6wUMQdHms6mfefz`</summary>

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
  "parentUuid": "42f9db93-ed54-476c-9cdd-b3f31d63d33f",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "e992a89a-6de8-412e-a3d8-f850ade6b60f",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "42f9db93-ed54-476c-9cdd-b3f31d63d33f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-27T15:57:15.580Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the paper from arXiv. I'll fetch both the abstract page and the full PDF (via the HTML version). Let me also check OpenReview for any reviewer comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e992a89a-6de8-412e-a3d8-f850ade6b60f",
  "isSidechain": false,
  "requestId": "req_011CbTM9S1JBE3YUKQar9d3Q",
  "type": "assistant",
  "uuid": "5a93bcaf-cebc-4ba6-8c1c-697de6e89e59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPdvuWWsEA9q8Ah7UQFAwt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 13256,
      "output_tokens": 510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 510,
          "cache_read_input_tokens": 13256,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 643
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

_source line 11 · 2026-05-27T15:57:16.172Z_

Let me fetch the paper details from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a93bcaf-cebc-4ba6-8c1c-697de6e89e59",
  "isSidechain": false,
  "requestId": "req_011CbTM9S1JBE3YUKQar9d3Q",
  "type": "assistant",
  "uuid": "bbdca8de-77b5-4f82-bf90-3d9e45e135df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPdvuWWsEA9q8Ah7UQFAwt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 13256,
      "output_tokens": 510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 510,
          "cache_read_input_tokens": 13256,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 643
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

_source line 12 · 2026-05-27T15:57:16.986Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J73EBGUQAhaGWpYHHVTXVG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract the full abstract, list of authors, submission date, and any other metadata available on this arXiv page for the paper GenPRM. Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbdca8de-77b5-4f82-bf90-3d9e45e135df",
  "isSidechain": false,
  "requestId": "req_011CbTM9S1JBE3YUKQar9d3Q",
  "type": "assistant",
  "uuid": "c0b75e00-8908-4136-bdb6-972f0c20d243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPdvuWWsEA9q8Ah7UQFAwt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 13256,
      "output_tokens": 510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 510,
          "cache_read_input_tokens": 13256,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 643
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

_source line 13 · 2026-05-27T15:57:20.309Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Su8RNB37i4jbRTtk8GiujB`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.00891",
  "prompt": "Extract the FULL text of the following sections from this paper, as completely as possible:\n1. Introduction (entire section)\n2. Method / Approach (entire section, including all subsections)\n3. Conclusion (entire section)\n\nAlso extract any information about:\n- Training data (how much, what kind, how generated)\n- Key results/numbers from experiments\n- Limitations discussed by the authors\n\nReturn all text verbatim, preserving technical details, equations, and figure/table references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0b75e00-8908-4136-bdb6-972f0c20d243",
  "isSidechain": false,
  "requestId": "req_011CbTM9S1JBE3YUKQar9d3Q",
  "type": "assistant",
  "uuid": "3df0429b-64f6-4045-92f1-3e364a73588a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPdvuWWsEA9q8Ah7UQFAwt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 13256,
      "output_tokens": 510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 510,
          "cache_read_input_tokens": 13256,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 643
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

_source line 14 · 2026-05-27T15:57:20.318Z_

<details><summary>↩ Tool result · `toolu_01Su8RNB37i4jbRTtk8GiujB`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3df0429b-64f6-4045-92f1-3e364a73588a",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "5b53a26e-8127-413f-8d92-8c3c0442950a",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 5,
    "url": "https://arxiv.org/html/2504.00891"
  },
  "sourceToolAssistantUUID": "3df0429b-64f6-4045-92f1-3e364a73588a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T15:57:22.185Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0153uJWYVEMSYQAFZqGTjAnk`</summary>

```json
{
  "url": "https://openreview.net/search?term=GenPRM+Scaling+Test-Time+Compute+Process+Reward+Models+Generative+Reasoning",
  "prompt": "Find any OpenReview page for the paper \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\". Extract any links to the paper's OpenReview page, reviewer comments, scores, or author responses. If no results found, say so."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b53a26e-8127-413f-8d92-8c3c0442950a",
  "isSidechain": false,
  "requestId": "req_011CbTM9S1JBE3YUKQar9d3Q",
  "type": "assistant",
  "uuid": "a5e69de1-66f9-476a-91f8-856be20c7bd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPdvuWWsEA9q8Ah7UQFAwt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 13256,
      "output_tokens": 510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 510,
          "cache_read_input_tokens": 13256,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 643
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

_source line 16 · 2026-05-27T15:57:24.150Z_

<details><summary>↩ Tool result · `toolu_01J73EBGUQAhaGWpYHHVTXVG`</summary>

```text
# GenPRM Paper Metadata

**Full Abstract:**
"Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset. Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs."

**Authors:**
Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou

**Submission Details:**
- arXiv ID: 2504.00891
- Submitted: April 1, 2025
- Last Revised: April 5, 2025 (v2)
- Category: Computer Science - Computation and Language (cs.CL)
- DOI: https://doi.org/10.48550/arXiv.2504.00891
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0b75e00-8908-4136-bdb6-972f0c20d243",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "f63be297-fc8d-46cd-ae58-b5792d048fb3",
  "toolUseResult": {
    "bytes": 47432,
    "code": 200,
    "codeText": "OK",
    "result": "# GenPRM Paper Metadata\n\n**Full Abstract:**\n\"Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only 23K training data from MATH dataset. Through test-time scaling, a 1.5B GenPRM outperforms GPT-4o, and a 7B GenPRM surpasses Qwen2.5-Math-PRM-72B on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs.\"\n\n**Authors:**\nJian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, Bowen Zhou\n\n**Submission Details:**\n- arXiv ID: 2504.00891\n- Submitted: April 1, 2025\n- Last Revised: April 5, 2025 (v2)\n- Category: Computer Science - Computation and Language (cs.CL)\n- DOI: https://doi.org/10.48550/arXiv.2504.00891",
    "durationMs": 7158,
    "url": "https://arxiv.org/abs/2504.00891"
  },
  "sourceToolAssistantUUID": "c0b75e00-8908-4136-bdb6-972f0c20d243",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T15:57:24.485Z_

<details><summary>↩ Tool result · `toolu_0153uJWYVEMSYQAFZqGTjAnk`</summary>

```text
I cannot find any OpenReview page, links, reviewer comments, scores, or author responses for the paper "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning" in the provided content.

The webpage content shown is only the OpenReview.net homepage with navigation menus, general site information, and footer links. To locate the specific paper you're asking about, you would need to use the search functionality on OpenReview.net directly or navigate to the actual paper's detail page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5e69de1-66f9-476a-91f8-856be20c7bd3",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "165ef62b-c09b-4623-b1d8-f6061615a159",
  "toolUseResult": {
    "bytes": 62428,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot find any OpenReview page, links, reviewer comments, scores, or author responses for the paper \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\" in the provided content.\n\nThe webpage content shown is only the OpenReview.net homepage with navigation menus, general site information, and footer links. To locate the specific paper you're asking about, you would need to use the search functionality on OpenReview.net directly or navigate to the actual paper's detail page.",
    "durationMs": 2297,
    "url": "https://openreview.net/search?term=GenPRM+Scaling+Test-Time+Compute+Process+Reward+Models+Generative+Reasoning"
  },
  "sourceToolAssistantUUID": "a5e69de1-66f9-476a-91f8-856be20c7bd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-27T15:57:28.392Z_

<details><summary>Logged reasoning block</summary>

```text
The HTML version returned a 404. Let me try the PDF version or an alternative HTML rendering. Let me try fetching the paper content from the arXiv PDF or from a different URL format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "165ef62b-c09b-4623-b1d8-f6061615a159",
  "isSidechain": false,
  "requestId": "req_011CbTMAKg5Qk9goQEHF8ASm",
  "type": "assistant",
  "uuid": "f48bcc84-8042-4776-9a2d-86e1861f78b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tu2q1hZ83kMCfzjijaquzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 13899,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 13899,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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

_source line 19 · 2026-05-27T15:57:28.805Z_

The HTML version wasn't available. Let me try alternative approaches to get the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48bcc84-8042-4776-9a2d-86e1861f78b9",
  "isSidechain": false,
  "requestId": "req_011CbTMAKg5Qk9goQEHF8ASm",
  "type": "assistant",
  "uuid": "cb3d5873-a198-4155-a26e-a8070c2cc8fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tu2q1hZ83kMCfzjijaquzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 13899,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 13899,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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

_source line 20 · 2026-05-27T15:57:30.269Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SCxroahAzcTHFCd1AZBNJh`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.00891v2",
  "prompt": "Extract the FULL text of the following sections from this paper, as completely as possible:\n1. Introduction (entire section)\n2. Method / Approach (entire section, including all subsections)\n3. Conclusion (entire section)\n\nAlso extract any information about:\n- Training data (how much, what kind, how generated)\n- Key results/numbers from experiments\n- Limitations discussed by the authors\n\nReturn all text verbatim, preserving technical details, equations, and figure/table references."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb3d5873-a198-4155-a26e-a8070c2cc8fc",
  "isSidechain": false,
  "requestId": "req_011CbTMAKg5Qk9goQEHF8ASm",
  "type": "assistant",
  "uuid": "9635cc9f-0998-4d11-b523-f272c3b58616",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tu2q1hZ83kMCfzjijaquzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 13899,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 13899,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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

_source line 21 · 2026-05-27T15:57:30.279Z_

<details><summary>↩ Tool result · `toolu_01SCxroahAzcTHFCd1AZBNJh`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9635cc9f-0998-4d11-b523-f272c3b58616",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "811e51fb-d856-4078-a720-b4e04d953496",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2504.00891v2"
  },
  "sourceToolAssistantUUID": "9635cc9f-0998-4d11-b523-f272c3b58616",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T15:57:31.007Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MnQuDX4xxQXPhpKUJF5xLe`</summary>

```json
{
  "url": "https://openreview.net/search?term=GenPRM&venue=AAAI.cc",
  "prompt": "Find any OpenReview page for the paper \"GenPRM\" related to Process Reward Models. Extract any links, reviewer comments, scores, or author responses. If no results, say so clearly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "811e51fb-d856-4078-a720-b4e04d953496",
  "isSidechain": false,
  "requestId": "req_011CbTMAKg5Qk9goQEHF8ASm",
  "type": "assistant",
  "uuid": "424c059e-39d3-422d-8f42-8e656fb4d064",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tu2q1hZ83kMCfzjijaquzV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 13899,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1251,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 13899,
          "cache_creation_input_tokens": 1251,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1251
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
  "leafUuid": "424c059e-39d3-422d-8f42-8e656fb4d064",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper for research innovation",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Tool result

_source line 25 · 2026-05-27T15:57:35.887Z_

<details><summary>↩ Tool result · `toolu_01MnQuDX4xxQXPhpKUJF5xLe`</summary>

```text
Based on the web page content provided, I cannot find any information about a paper titled "GenPRM" or any discussion related to Process Reward Models.

The content shown appears to be navigation and footer elements from OpenReview.net's homepage, including menu links, policy information, and general site descriptions. It does not contain search results, paper details, reviewer comments, scores, or author responses.

To locate the GenPRM paper, you would need to use OpenReview's search function or navigate to the specific venue where it was submitted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "424c059e-39d3-422d-8f42-8e656fb4d064",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "fec8536b-e63b-4578-b945-8f79d61a09b1",
  "toolUseResult": {
    "bytes": 62279,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find any information about a paper titled \"GenPRM\" or any discussion related to Process Reward Models.\n\nThe content shown appears to be navigation and footer elements from OpenReview.net's homepage, including menu links, policy information, and general site descriptions. It does not contain search results, paper details, reviewer comments, scores, or author responses.\n\nTo locate the GenPRM paper, you would need to use OpenReview's search function or navigate to the specific venue where it was submitted.",
    "durationMs": 4878,
    "url": "https://openreview.net/search?term=GenPRM&venue=AAAI.cc"
  },
  "sourceToolAssistantUUID": "424c059e-39d3-422d-8f42-8e656fb4d064",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-27T15:57:39.432Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try fetching the PDF directly or try a different approach. Let me try the Hugging Face papers page or another mirror.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fec8536b-e63b-4578-b945-8f79d61a09b1",
  "isSidechain": false,
  "requestId": "req_011CbTMBASitVLAnukXpbZXq",
  "type": "assistant",
  "uuid": "03451a50-03aa-4e73-a14c-0479a58d7ad0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WTVLTxGsk45BBYGn43po8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 15150,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 15150,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 613
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

_source line 27 · 2026-05-27T15:57:39.939Z_

Let me try fetching the paper content through alternative sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03451a50-03aa-4e73-a14c-0479a58d7ad0",
  "isSidechain": false,
  "requestId": "req_011CbTMBASitVLAnukXpbZXq",
  "type": "assistant",
  "uuid": "220af159-785e-405d-8bd3-4bef26a65573",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WTVLTxGsk45BBYGn43po8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 15150,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 15150,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 613
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

_source line 28 · 2026-05-27T15:57:41.351Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M8wCs4hexzqjE5QNDLnYzA`</summary>

```json
{
  "url": "https://huggingface.co/papers/2504.00891",
  "prompt": "Extract all available information about the GenPRM paper, including any summary, method details, key contributions, results, and discussion. Return everything available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "220af159-785e-405d-8bd3-4bef26a65573",
  "isSidechain": false,
  "requestId": "req_011CbTMBASitVLAnukXpbZXq",
  "type": "assistant",
  "uuid": "b60ab32b-05b8-4ba8-acf3-b797b0faeaf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WTVLTxGsk45BBYGn43po8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 15150,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 15150,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 613
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

_source line 29 · 2026-05-27T15:57:42.271Z_

<details><summary>↩ Tool result · `toolu_01M8wCs4hexzqjE5QNDLnYzA`</summary>

```text
&lt;persisted-output>
Output too large (87.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt

Preview (first 2KB):
# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning

Jian Zhao&lt;sup>1,3\*&lt;/sup>, Runze Liu&lt;sup>1,2\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>

&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology

Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

`````json
{
  "recorded_role": "user",
  "parentUuid": "b60ab32b-05b8-4ba8-acf3-b797b0faeaf2",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "a43057d6-796f-42ed-b794-818d55906be8",
  "toolUseResult": {
    "bytes": 89347,
    "code": 200,
    "codeText": "OK",
    "result": "# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n\nJian Zhao&lt;sup>1,3\\*&lt;/sup>, Runze Liu&lt;sup>1,2\\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>\n\n&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology\n\nRecent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.\n\n**Figure 1: GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: (a) As a verifier:** GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling. **(b) As a critic:** GenPRM-7B demonstrates superior critique capabilities, achieving **3.4x** greater performance gains than DeepSeek-R1-Distill-Qwen-7B after 3 refinement iterations.\n\n\\* Equal contribution\n\n† Project lead & Work done during an internship at Shanghai AI Laboratory\n\n‡ Corresponding authors: Biqing Qi (qibiqing@pjlab.org.cn), Xiu Li (li.xiu@sz.tsinghua.edu.cn), and Bowen Zhou (zhoubowen@tsinghua.edu.cn)The diagram illustrates the architectural differences between classification-based PRMs and GenPRM. On the left, under the heading 'Classification-based PRM', two models are shown: 'Discriminative PRM' and 'Direct Generative PRM'. The Discriminative PRM consists of a 'value head' that outputs a score of 0.9, marked with a green checkmark. The Direct Generative PRM outputs a 'Yes' label, which is then converted to a score of 0.8, also marked with a green checkmark. On the right, under the heading 'Generative PRM (Ours)', the 'GenPRM' model is shown. It branches into three parallel paths, each consisting of a yellow circle (CoT Verification) followed by a green circle (Code Verification) and a 'Yes' or 'No' label. The top path outputs 'Yes', the middle path outputs 'No', and the bottom path outputs 'No'. These three paths converge into a final score of 0.2, which is marked with a red 'X'. A legend at the bottom identifies the yellow circle as 'CoT Verification' and the green circle as 'Code Verification'.\n\nFigure 2: Comparison between GenPRM (right) and previous classification-based PRMs (left).\n\n## 1. Introduction\n\nLarge Language Models (LLMs) have shown significant advances in recent years (OpenAI, 2023; Anthropic, 2023; OpenAI, 2024a,b; DeepSeek-AI et al., 2025). As OpenAI o1 demonstrates the great effectiveness of scaling test-time compute (OpenAI, 2024a), an increasing number of researches focus on Test-Time Scaling (TTS) methods to improve the reasoning performance of LLMs (Snell et al., 2025; Liu et al., 2025).\n\nEffective TTS requires high-quality verifiers, such as Process Reward Models (PRMs) (Liu et al., 2025). However, existing PRMs face several limitations. They exhibit limited process supervision capabilities and struggle to generalize across different models and tasks (Zheng et al., 2024; Zhang et al., 2025c; Liu et al., 2025). Furthermore, most current approaches train PRMs as classifiers that output scalar values, neglecting the natural language generation abilities of LLMs, which are pre-trained on extensive corpora. This classifier-based modeling inherently prevents PRMs from leveraging test-time scaling methods to enhance process supervision capabilities. These limitations lead us to the following research question: *How can generative modeling enhance the process supervision capabilities of PRMs while enabling test-time scaling?*\n\nIn this work, we address these challenges through a generative process reward model, named GenPRM. Specifically, GenPRM differs from classification-based PRMs in that GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) (Wei et al., 2022) reasoning and code verification processes before providing final judgment. To improve conventional hard label estimation, we propose Relative Progress Estimation (RPE), which leverages a relative criterion for label estimation. Additionally, we introduce a rationale synthesis framework with code verification to obtain high-quality process supervision reasoning data. A comparison of our method with previous classification-based methods is presented in Figure 2.\n\nOur contributions can be summarized as follows:\n\n1. 1. We propose a generative process reward model that performs explicit CoT reasoning with code verification and utilizes Relative Progress Estimation to obtain accurate PRM labels.\n2. 2. Empirical results on ProcessBench and common mathematical reasoning tasks demonstrate that GenPRM outperforms prior classification-based PRMs. Additionally, smaller GenPRM models can surpass larger PRMs via TTS.\n3. 3. We provide a new perspective on PRMs in this work, fully leveraging their TTS capabilities, reshaping their applications, and opening new directions for future research in process supervision.## 2. Preliminaries\n\n### 2.1. Markov Decision Process\n\nFollowing [Liu et al. \\(2025\\)](#), we formulate the test-time scaling process with PRMs as a Markov Decision Process (MDP) defined by  $(\\mathcal{S}, \\mathcal{A}, P, r, \\gamma)$ , where  $\\mathcal{S}$  is the state space,  $\\mathcal{A}$  is the action space,  $P$  represents transition dynamics,  $r : \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$  is the reward function, and  $\\gamma \\in [0, 1]$  is the discount factor. Starting with a prompt set  $\\mathcal{X}$  and an initial state  $s_1 = x \\sim \\mathcal{X}$ , the policy model  $\\pi_\\theta$  generates an action  $a_1 \\sim \\pi_\\theta(\\cdot | s_1)$ .&lt;sup>1&lt;/sup> Unlike traditional RL methods with stochastic transitions ([Liu et al., 2022, 2024](#)), transitions in LLMs are deterministic, i.e.,  $s_{t+1} = P(\\cdot | s_t, a_t) = [s_t, a_t]$ , where  $[\\cdot, \\cdot]$  denotes string concatenation. This process continues until the episode terminates (i.e., generating the [EOS] token), obtaining a trajectory of  $T$  steps:  $\\tau = \\{a_1, a_2, \\dots, a_T\\}$ . The goal is to optimize either the reward of each step (as in search-based methods) or the reward over the full response (as in Best-of-N sampling).\n\n### 2.2. Supervised Fine-Tuning\n\nSupervised Fine-Tuning (SFT) trains a model to predict the next token based on prior context. For a dataset  $\\mathcal{D}_{\\text{SFT}} = \\{(x^{(i)}, y^{(i)})\\}_{i=1}^N$ , the SFT loss is:\n\n$$\\mathcal{L}_{\\text{SFT}}(\\theta) = -\\mathbb{E}_{(x,y) \\sim \\mathcal{D}_{\\text{SFT}}} \\left[ \\sum_{t=1}^{|y|} \\log \\pi_\\theta(y_t | x, y_{1:t-1}) \\right], \\quad (1)$$\n\nwhere  $\\pi_\\theta$  represents a model with parameters  $\\theta$ .\n\n### 2.3. Test-Time Scaling\n\nIn this work, we consider two test-time scaling methods, including majority voting and Best-of-N.\n\n**Majority Voting.** Majority voting ([Wang et al., 2023](#)) selects the answer that appears the most frequently among all solutions.\n\n**Best-of-N.** Best-of-N (BoN) ([Brown et al., 2024](#); [Snell et al., 2025](#)) selects the best answer from  $N$  candidate solutions.\n\n## 3. Method\n\nIn this section, we first describe how to develop GenPRM and integrate the reasoning process with code verification. We then introduce how to scale test-time compute of policy models using GenPRM and apply TTS for GenPRM. Last, we present the improved label estimation method and data generation and filtering framework of GenPRM.\n\n### 3.1. GenPRM and Test-Time Scaling\n\n#### 3.1.1. From Discriminative PRM to Generative PRM\n\n**Discriminative PRM.** Assume we have a PRM dataset  $\\mathcal{D}_{\\text{Disc}} = \\{(s_t, a_t), r_t\\}$ , where  $r_t \\in \\{0, 1\\}$  for PRM labels with hard estimation. The discriminative PRM  $r_\\psi$  is trained via cross-entropy loss ([Skywork](#)\n\n&lt;sup>1&lt;/sup>Following [Snell et al. \\(2025\\)](#); [Liu et al. \\(2025\\)](#), we refer to models that generate solutions as policy models.The diagram illustrates the GenPRM framework, which consists of six key parts:\n\n- **① Solution Generation & MC Reward Estimation:** A math problem is solved by generating intermediate steps (a&lt;sub>11&lt;/sub>, a&lt;sub>21&lt;/sub>, a&lt;sub>31&lt;/sub>, a&lt;sub>12&lt;/sub>, a&lt;sub>22&lt;/sub>, a&lt;sub>32&lt;/sub>). Correct steps (q&lt;sub>1&lt;/sub>, q&lt;sub>2&lt;/sub>) are marked with blue circles, and incorrect steps (q&lt;sub>3&lt;/sub>) are marked with red circles. The MC score for a step is calculated as  $MC(s_{12}, a_{12}) = \\frac{2}{3}$ .\n- **② Relative Progress Estimation:** The process reward is estimated as  $P_t = \\frac{MC(s_t, a_t)}{MC(s_t)} \\geq \\epsilon$ . If the reward is high,  $\\hat{r}_t = 1$  (green checkmark), otherwise  $\\hat{r}_t = 0$  (red X).\n- **③ Rationale Synthesis:** A problem is analyzed using CoT (Chain of Thought) analysis to generate a rationale. This rationale is then verified using code verification (e.g., Python code) to check for potential errors. The final label is a judgement of Yes/No.\n- **④ GenPRM Training:** Data (23K) is used for SFT (Supervised Fine-Tuning) to train GenPRM. Consensus filtering is applied to the training data.\n- **⑤ Policy Model Test-Time Scaling:** The trained GenPRM functions as a verifier or critic. It can be used to verify a solution (GenPRM as a Verifier) or critique a solution (GenPRM as a Critic).\n- **⑥ GenPRM Test-Time Scaling:** The performance of GenPRM is improved through test-time scaling. Multiple steps are analyzed and verified, and their rewards are aggregated to produce a final reward  $r$ .\n\nLegend:\n\n- a Intermediate Step\n- q Correct Answer\n- q Incorrect Answer\n- r Single Reward Judgement\n- r Aggregated Reward Judgement\n\n**Figure 3: Overall framework of GenPRM.** Our framework consists of six key parts: ① The policy model generates solution steps, with MC scores estimated from rollout trajectories. ② Our proposed RPE derives accurate PRM labels. ③ High-quality process supervision data is synthesized through CoT reasoning augmented with code verification. ④ We apply consensus filtering followed by SFT to train GenPRM. ⑤ The trained GenPRM functions as a verifier or critic, enabling enhanced test-time scaling for policy models. ⑥ The performance of GenPRM further improves through test-time scaling.\n\no1 Team, 2024; Zhang et al., 2025c):\n\n$$\\mathcal{L}_{CE}(\\psi) = -\\mathbb{E}_{(s_t, a_t, r_t) \\sim \\mathcal{D}_{Disc}} [r_t \\log r_\\psi(s_t, a_t) + (1 - r_t) \\log(1 - r_\\psi(s_t, a_t))]. \\quad (2)$$\n\n**Direct Generative PRM.** With a dataset  $\\mathcal{D}_{Direct-Gen} = \\{(s_t, a_t), r_t\\}$ , where  $r_t$  is Yes for a correct step and No otherwise, the direct generative PRM (Xiong et al., 2024) is trained through SFT to predict Yes or No for each step. For step  $t$ , we use the probability of the Yes token as the predicted process reward  $\\hat{r}_t$ :\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t). \\quad (3)$$\n\n**Generative PRM.** By equipping the direct generative PRM with an explicit reasoning process like CoT (Wei et al., 2022), we obtain a generative PRM. Let  $v_{1:t-1}$  denote the rationale from step 1 to  $t-1$  and  $v_t$  denote the rationale for step  $t$ . Assume we have a dataset  $\\mathcal{D}_{Gen} = \\{(s_t, a_t, v_{1:t-1}), (v_t, r_t)\\}$ . GenPRM learns to reason and verify each step via SFT on this dataset. The generative process reward  $\\hat{r}_t$  can be obtained via the following equation:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, v_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}) \\quad (4)$$\n\n**Generative PRM with Code Verification.** If we only verify the reasoning step with CoT based on natural language, the process may lack robustness in certain complex scenarios (Zhu et al., 2024; Gou et al., 2024). The difference between the generative PRM and the generative PRM with code verification is that the latter generates code to verify the reasoning step by executing it and provides the judgment based on the execution results. At step  $t$ , after generating the rationale  $v_t$  containing CoT and code, we execute the code and obtain feedback  $f_t$ . Given the current state  $s_t$ , action  $a_t$ , previous rationales  $v_{1:t-1}$ , and previous corresponding execution feedback  $f_{1:t-1}$ , the PRM first generates therationale  $v_t$ . After execution and obtaining the feedback  $f_t$ , we compute the final generative process reward as follows:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}, v_t, f_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}) \\quad (5)$$\n\nIn the following sections, we refer to GenPRM as this generative PRM type with code verification. The effectiveness of CoT and code verification can be found in Section 4.4.\n\n### 3.1.2. Test-Time Scaling\n\n**Policy Model TTS: GenPRM as a Verifier.** To scale the test-time compute of policy models, we can sample multiple responses from policy models and then use GenPRM as a verifier to select the final answer (Snell et al., 2025) in the way of parallel TTS.\n\n**Policy Model TTS: GenPRM as a Critic.** By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and we can scale the refinement process with multiple turns in a sequential TTS manner.\n\n**GenPRM TTS.** When evaluating each solution step, we first sample  $N$  reasoning verification paths and then use majority voting to obtain the final prediction by averaging the rewards. For GenPRM without code verification, the rewards are computed as follows:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, v_t^i). \\quad (6)$$\n\nAnd we can further incorporate code verification and execution feedback into this reasoning process:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, f_{1:t-1}^i, v_t^i, f_t^i). \\quad (7)$$\n\nThen the rewards can be used for ranking the responses of policy models or be converted into binary labels through a threshold 0.5 for judging the correctness of the step. The discussion of using code verification can be found at Table 5.\n\n## 3.2. Synthesizing Data of GenPRM\n\nIn this section, we introduce our pipeline for synthesizing training data of GenPRM. The pipeline consists of three stages: (1) generating reasoning paths and obtaining PRM labels via Monte Carlo (MC) estimation; (2) evaluating the progress of each step via Relative Progress Estimation; and (3) synthesizing rationales with CoT and code verification, and inferring LLM-as-a-judge labels with consensus filtering.\n\n### 3.2.1. Solution Generation and Monte Carlo Estimation\n\n**Solution Generation with Step Forcing.** We utilize the 7.5K problems from the training set of the MATH dataset (Hendrycks et al., 2021) as the problem set. For each problem, we use Qwen2.5-7B-Instruct (Yang et al., 2024a) as the generation model to collect multiple solutions. Since using “\\n\\n” for step division does not consider the semantics of each step and may result in overly fine-grained division, we apply a step forcing approach to generate solutions. Specifically, we add “Step 1:” as the prefix for the generation model to complete the response. For a response with  $T$  reasoning steps, the format is as follows:### The response format with step forcing\n\nStep 1: {step content}\n\n...\n\nStep T: {step content}\n\nThe proportion of correct paths versus incorrect paths varies significantly depending on the difficulty of the problems. To ensure a sufficient number of correct and incorrect paths, we sample up to 2048 paths for both hard and easy problems. If no correct or incorrect paths are found after sampling 2048 responses, we discard the corresponding problems.\n\n**Balancing the Precision and Efficiency of MC Estimation.** Following Math-Shepherd (Wang et al., 2024b), we estimate the probability of correctness for each step using completion-based sampling. For each reasoning step  $s_t$ , we generate  $K$  completion trajectories using a completion model, specifically Qwen2.5-Math-7B-Instruct (Yang et al., 2024b), and use MC estimation to calculate the probability that the current step  $a_t$  is correct (Wang et al., 2024b; Zhang et al., 2025c):\n\n$$MC(s_t, a_t) = MC(s_{t+1}) = \\frac{1}{K} \\sum_{j=1}^K \\mathbb{1}(q_j = q^*), \\quad (8)$$\n\nwhere  $q_j$  is the answer of the  $j$ -th response,  $q^*$  is the ground-truth answer, and  $\\mathbb{1}$  is the indicator function. However, it is difficult for the completion model to reach the correct answer for hard problems even when the original step is correct, leading to incorrect results for MC estimation. To address this and balance the computation cost, we use a dynamic  $K$  based on the estimated Pass@1  $MC(s_1)$ :\n\n$$K = \\begin{cases} 128 & \\text{if } 0 \\leq MC(s_1) < 0.1, \\\\ 64 & \\text{if } 0.1 \\leq MC(s_1) < 0.9, \\\\ 32 & \\text{if } 0.9 \\leq MC(s_1) < 1. \\end{cases} \\quad (9)$$\n\n### 3.2.2. Relative Progress Estimation\n\nPrevious work has shown that hard label estimation is better than soft label estimation for PRMs (Zhang et al., 2025c). However, after MC estimation, we observe that although the MC score of many steps is greater than 0, the steps are incorrect, as also noted by Zhang et al. (2025c). On the other hand, we assume that a positive step should be both correct and beneficial. A reasoning step is considered as a beneficial one if it is easier to reach the correct answer by adding this step as the generation prefix. To address these issues, we propose Relative Progress Estimation (RPE), which shares a similar idea with relative advantage estimation in GRPO (Shao et al., 2024; DeepSeek-AI et al., 2025), to improve conventional hard label estimation.\n\nSpecifically, the MC score is an empirical estimation of the current state  $s_t$ . To evaluate the quality of the current action  $a_t$ , it is natural to compare the MC score of the next state  $s_{t+1}$  with that of the current state  $s_t$ , since  $s_{t+1} = [s_t, a_t]$ . For each response, if the first erroneous step is step  $t'$  (i.e.,  $MC(s_{t'}) = 0$ ), we set the MC score of the following steps to 0. Our RPE  $P_t$  for step  $t$  is defined as follows:\n\n$$P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}, \\quad (10)$$\n\nwhere  $MC(s_1)$  is the estimated Pass@1 computed in the solution generation phase. However, we empirically find that using a strict criterion where progress is always greater than 1 leads to unsatisfactory performance, as shown in Table 3. To address this, we estimate the final reward label  $\\hat{r}_t$  byintroducing a threshold  $\\epsilon$ :\n\n$$\\hat{r}_t = \\begin{cases} 1 & \\text{if } P_t \\geq \\epsilon, \\\\ 0 & \\text{otherwise.} \\end{cases} \\quad (11)$$\n\nWe also discuss another form of relative progress  $P_t = MC(s_t, a_t) - MC(s_t)$  in Table 3 in Section 4.4.\n\n### 3.2.3. Rationale Generation, Verification and Filtering\n\nTo obtain high-quality rationale data, we use QwQ-32B (Qwen Team, 2025) as the rationale generation model and introduce a three-step pipeline that automatically generates and verifies the rationale of each reasoning step. Given a problem  $x$  with a ground-truth answer  $q^*$  and candidate steps  $\\{a_1, \\dots, a_T\\}$ , the generation and verification proceed as follows:\n\n**Step 1: Code-Based Rationale Generation.** To evaluate the correctness of  $a_t$ , we synthesize step-by-step CoT analysis. It has been shown that program-based reasoning improves verification outcomes (Zhu et al., 2024). Based on CoT analysis, we continue to synthesize code-based rationales to verify  $a_t$  based on the problem and historical steps  $\\{a_1, \\dots, a_{t-1}\\}$ . We prompt the rationale generation model to surround the CoT with `&lt;analyze>` and `&lt;/analyze>`, and the code with `&lt;verify>` and `&lt;/verify>`. The prompt for rationale generation is shown in Table A.2.\n\n**Step 2: Code Execution and Verification.** With the generated code, we execute it and obtain the feedback  $f_t$  for step  $t$ . The execution feedback is formatted as [Code output: {execution result}] and is concatenated to the generated CoT and code as the prefix for the subsequent generation. If the execution result is inconsistent with the generated CoT verification, we observe that QwQ-32B performs self-reflection behaviors until reaching a consensus.\n\n**Step 3: Label Judgment and Consensus Filtering.** After generating and verifying the rationale data of all candidate steps, the rationale generation model finally outputs a number. If all steps are inferred to be correct, the number will be -1, otherwise will be the index of the first erroneous step. For each solution, if there is at least one process label with RPE is not consistent with the labels generated by LLM-as-a-judge (Zheng et al., 2023), we discard the entire solution and only retain the one with all labels consistent. After consensus filtering, we discard approximately 51% of the data and finally obtain a dataset containing 23K problems with reasoning steps and rationale data.\n\n## 4. Experiments\n\nIn this section, we aim to answer the following questions:\n\n- • **Q1:** How does GenPRM perform compared with previous PRMs? (§4.2, §4.3)\n- • **Q2:** How does the performance of GenPRM scale with more test-time compute? (§4.2, §4.3)\n- • **Q3:** How does GenPRM benefit policy model test-time scaling? (§4.3)\n- • **Q4:** How do the components and hyperparameters influence GenPRM? (§4.4)\n\n### 4.1. Setup\n\n**Benchmarks.** We evaluate GenPRM and baseline methods on ProcessBench (Zheng et al., 2024), a benchmark designed to assess process supervision capabilities in mathematical reasoning tasks.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our evaluation code is adapted from &lt;https://github.com/QwenLM/ProcessBench>.Additionally, we conduct BoN and critic refinement experiments using MATH (Hendrycks et al., 2021), AMC23 (AI-MO, 2024b), AIME24 (AI-MO, 2024a), and Minerva Math (Lewkowycz et al., 2022). For BoN response generation, we employ Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) and Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as policy models. For policy model TTS with GenPRM as the critic, we use Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) and Qwen2.5-7B-Instruct (Yang et al., 2024a) as generators.\n\n**Baselines.** For ProcessBench and BoN experiments, we compare GenPRM with the following methods:\n\n- • **Math-Shepherd-PRM-7B** (Wang et al., 2024b): This method trains a PRM using hard labels computed based on MC estimation.\n- • **RLHFlow series** (Xiong et al., 2024): Includes RLHFlow-PRM-Mistral-8B and RLHFlow-PRM-Deepseek-8B.\n- • **Skywork-PRM series** (Skywork o1 Team, 2024): Comprises Skywork-PRM-1.5B and Skywork-PRM-7B.\n- • **EurusPRM** (Cui et al., 2025): EurusPRM-Stage1 and EurusPRM-Stage2 are trained as implicit PRMs (Yuan et al., 2024).\n- • **Qwen2.5-Math series** (Zheng et al., 2024; Zhang et al., 2025c): Qwen2.5-Math-7B-Math-Shepherd and Qwen2.5-Math-7B-PRM800K are trained with Math-Shepherd (Wang et al., 2024b) and PRM800K (Lightman et al., 2024), respectively. For Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B, the training data is applied consensus filtering using LLM-as-a-judge (Zheng et al., 2023).\n- • **RetrievalPRM-7B** (Zhu et al., 2025): The method enhances PRM with retrieved questions and corresponding steps.\n- • **Universal-PRM-7B** (Tan et al., 2025): The method proposes an automated framework using ensemble prompting and reverse verification.\n- • **Dyve-14B** (Zhong et al., 2025): This method dynamically applies fast or slow verification for each reasoning step.\n- • **Direct Generative PRM-7B**: The method trains a direct generative PRM with the original language head via SFT using the same data as GenPRM, but without CoT and code verification.\n\nFor critic experiments, we use the following methods for comparison:\n\n- • **Self-Refine** (Madaan et al., 2023): This method uses the generator to self-critique and refine the solution.\n- • **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI et al., 2025): This model is fine-tuned based on Qwen2.5-Math-7B (Yang et al., 2024a) using high-quality reasoning data generated by DeepSeek-R1 (DeepSeek-AI et al., 2025).\n\n**Implementation Details.** For RPE, we set  $\\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \\times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th># Samples&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>59.0&lt;/b>&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>&lt;b>66.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>&lt;b>74.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>63.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>273K&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>253K&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage1&lt;/td>\n&lt;td>463K&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>35.6&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage2&lt;/td>\n&lt;td>30K&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>28.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>\n&lt;td>264K&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RetrievalPRM-7B&lt;/td>\n&lt;td>404K&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>60.2&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Universal-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>85.8&lt;/b>&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Direct Generative PRM-7B&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>72.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Dyve-14B&lt;/td>\n&lt;td>117K&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>58.3&lt;/td>\n&lt;td>49.0&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>78.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>&lt;b>81.7&lt;/b>&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>&lt;b>72.8&lt;/b>&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 4.2. ProcessBench Results\n\n**GenPRM outperforms classification-based PRMs on ProcessBench.** As shown in Table 1, GenPRM-7B significantly outperforms direct generative PRM and surpasses **all** previous PRMs with parameters less than 72B on ProcessBench. Also, GenPRM-1.5B outperforms Skywork-PRM-1.5B by a large margin. It is noteworthy that GenPRM is trained with merely **23K** data from **MATH** (Hendrycks et al., 2021) only. By comparing the detailed results in Table 6, we can find that the performance gain of GenPRM mainly comes from the stronger abilities of finding **erroneous** steps and we provide concrete cases in Appendix C. These results demonstrating the superiority of generative modeling of PRM.\n\n**GenPRM enables smaller PRMs surpass 10 $\\times$  larger PRMs and GPT-4o via TTS.** We also compare the TTS results of GenPRM in Table 1 and find that GenPRM-1.5B surpasses GPT-4 and GenPRM-7B exceeds Qwen2.5-Math-PRM-72B on ProcessBench via simply majority voting, showing that scaling test-time compute is highly effective for GenPRM. We also find that the performance improvement of scaling the test-time compute on **harder** problems is larger than that of easier questions.### 4.3. Policy Model Test-Time Scaling Results\n\n**GenPRM as a Verifier.** The results in Figure 4 (a)-(d) show that GenPRM outperforms the baselines on MATH, AMC23, AIME24, and Minerva Math with Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) as the generation model. The advantage of GenPRM becomes larger by scaling the test-time compute of GenPRM and the generation model. Figure 4 (e)-(h) demonstrates that GenPRM generalizes well to responses with Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as the generation model.\n\n**Figure 4:** BoN results with different generation models on multiple mathematical benchmarks.\n\n**GenPRM as a Critic.** We also conduct experiments by using GenPRM as a critic to refine the outputs of the policy model. The results in Table 2 and Figure 1 (right) show that GenPRM exhibits strong critique abilities than the baselines, significantly improving the performance of the policy model and the performance continues to increase with more refinement based on the critic feedback.\n\n### 4.4. Analysis\n\n**Label Estimation Method and Criterion.** To explore how different label estimation influences GenPRM, we conduct experiments with the following methods: (1) hard label (Wang et al., 2024b; Zhang et al., 2025c); (2) RPE in (10); and (3) a RPE variant ( $P_t = MC(s_t, a_t) - MC(s_t)$ ). For the RPE and its variant, we use different thresholds  $\\epsilon$  for evaluation and set the labels as correct by checking whether  $P_t \\geq \\epsilon$ . The results in Table 3 show that RPE and its variant outperforms hard label estimation and RPE with  $\\epsilon = 0.8$  achieves the best result. By scaling test-time compute with majority voting, the results in Table 4 demonstrate that RPE with  $\\epsilon = 0.8$  still reaches the best.**Table 2:** Results of critique refinement experiments. The results of GenPRM are shaded. For each refinement turn, the highest values are **bolded**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Critic Model&lt;/th>\n&lt;th colspan=\"5\">Gemma-3-12b-it as Generator&lt;/th>\n&lt;th colspan=\"5\">Qwen2.5-7B-Instruct as Generator&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Zero-shot&lt;/td>\n&lt;td>64.1&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>7.1&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>34.5&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>45.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 1&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>84.7&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.1&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>6.3&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>34.7&lt;/td>\n&lt;td>42.3&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>74.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>19.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>53.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>8.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>45.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>49.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 2&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>50.3&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.9&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>41.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>18.3&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.5&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>7.9&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>75.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>21.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>59.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>46.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 3&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>18.1&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>32.1&lt;/td>\n&lt;td>50.8&lt;/td>\n&lt;td>49.7&lt;/td>\n&lt;td>8.1&lt;/td>\n&lt;td>77.1&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>41.4&lt;/td>\n&lt;td>46.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>18.8&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>51.7&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>76.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>22.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>34.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>47.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>51.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Pass@1. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>72.9&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>&lt;b>73.2&lt;/b>&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>73.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>77.3&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>79.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>69.0&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>75.8&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>68.7&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>75.7&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>77.4&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>72.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>75.1&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>78.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>74.5&lt;/td>\n&lt;td>79.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>80.9&lt;/td>\n&lt;td>&lt;b>86.5&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.0&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>77.0&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.3&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>&lt;b>81.1&lt;/b>&lt;/td>\n&lt;td>84.1&lt;/td>\n&lt;td>76.0&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>79.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Reasoning Components.** To understand how each reasoning component influence GenPRM, we conduct experiments by training GenPRM with: (1) CoT data only, (2) code verification data only, and (3) full data. During inference phase, we also compare several variants. For example, GenPRM trained with full data can be used to only verify each step with CoT only by stopping generation at `&lt;/analyze>` token. The results in Table 5 show that: (1) the improvement of GenPRM mainly comesfrom CoT reasoning; (2) generating code and reasoning with code execution result improves the process verification performance as well.\n\n**Table 5:** Results on ProcessBench of GenPRM with different reasoning components, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th colspan=\"2\">Training&lt;/th>\n&lt;th colspan=\"3\">Inference&lt;/th>\n&lt;th rowspan=\"2\">GSM8K&lt;/th>\n&lt;th rowspan=\"2\">MATH&lt;/th>\n&lt;th rowspan=\"2\">Olympiad Bench&lt;/th>\n&lt;th rowspan=\"2\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>Code Exec.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>67.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>67.3&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>83.0&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;td>75.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>66.7&lt;/td>\n&lt;td>59.9&lt;/td>\n&lt;td>59.2&lt;/td>\n&lt;td>61.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>61.3&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>62.0&lt;/td>\n&lt;td>66.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.5&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 5. Related Work\n\n**Process Reward Models.** Process reward models have been proved to be effective for providing step-wise scores and are superior to outcome reward models in mathematical reasoning tasks (Uesato et al., 2022; Lightman et al., 2024). However, annotating a process supervision dataset such as PRM800K (Lightman et al., 2024) requires significant human costs. To mitigate this cost, prior works utilize Monte Carlo estimation (Wang et al., 2024b) and binary search (Luo et al., 2024) for automated label generation. Subsequent research improves PRMs through methods such as advantage modeling (Setlur et al., 2025),  $Q$ -value rankings (Li and Li, 2025), implicit entropy regularization (Zhang et al., 2024a), retrieval-augmented generation (Zhu et al., 2025), and fast-slow verification (Zhong et al., 2025). Furthermore, the community has developed high-quality open-source PRMs, including the RLHFlow series (Xiong et al., 2024), Math-psa (Wang et al., 2024a), Skywork series (Skywork o1 Team, 2024), and Qwen2.5-Math series (Zheng et al., 2024; Zhang et al., 2025c). Recently, a line of works focus on extending PRMs to other tasks, including coding (Zhang et al., 2024b), medical tasks (Jiang et al., 2025), agentic tasks (Choudhury, 2025), general domain tasks (Zhang et al., 2025a; Zeng et al., 2025), and multimodal tasks (Wang et al., 2025). Current studies also focus on benchmarking PRMs (Zheng et al., 2024; Song et al., 2025) to systematically evaluate their performance.\n\n**Large Language Model Test-Time Scaling.** Scaling test-time computation is an effective method for improving performance during the inference phase (OpenAI, 2024a,b; DeepSeek-AI et al., 2025). TTS is commonly implemented with external verifiers (e.g., ORMs and PRMs) or strategies (e.g., beam search and MCTS) (Wu et al., 2025; Snell et al., 2025; Beeching et al., 2024; Liu et al., 2025). In this work, we scale the test-time computation of a generative PRM with an explicit reasoning process and GenPRM can also serve as a verifier or a critic model in external TTS.\n\n**Enhancing the Generative Abilities of Reward Models.** Previous research has investigated methods to enhance the generative capabilities of reward models using CoT reasoning (Ankner et al., 2024; Zhang et al., 2025b; Mahan et al., 2024). For instance, CCloud reward models (Ankner et al., 2024) are trained to generate critiques for responses and predict rewards using an additional rewardhead. GenRM-CoT (Zhang et al., 2025b) and GenRM (Mahan et al., 2024) train generative reward models that perform CoT reasoning before making final predictions via SFT and preference learning, respectively. CTRL (Xie et al., 2025) demonstrates that critic models exhibit strong discriminative abilities when utilized as generative reward models. Prior to these works, GRM (Yang et al., 2024c) regularizes the hidden states of reward models with a text generation loss.\n\n## 6. Conclusion\n\nIn this work, we propose GenPRM, a generative process reward model that performs explicit reasoning and code verification for process supervision and enables scaling the test-time compute of PRMs. Experimental results on ProcessBench and several mathematical datasets show GenPRM outperforms prior PRMs. We also demonstrate that the performance of GenPRM increases via test-time scaling and GenPRM is effective as a critic model. We believe that this work provides perspectives on PRMs by demonstrating the strong TTS abilities of PRMs and extending the applications of PRMs.\n\n**Limitations.** First, GenPRM provides process supervision by generative reasoning, which introduces additional computation during inference phase. Future work will investigate how to prune the reasoning process dynamically (Zhong et al., 2025). Although GenPRM focuses mainly on mathematical reasoning tasks, it is worth to explore how to apply generative reasoning on coding and general reasoning tasks in the future (Zhang et al., 2025a). Additionally, it would be interesting to leverage RL to incentivize the generative reasoning abilities of GenPRM.\n\n## References\n\nAI-MO. AIME 2024, 2024a. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-aimo>.\n\nAI-MO. AMC 2023, 2024b. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-amc>.\n\nZachary Ankner, Mansheej Paul, Brandon Cui, Jonathan D Chang, and Prithviraj Ammanabrolu. Critique-out-Loud Reward Models. *arXiv preprint arXiv:2408.11791*, 2024.\n\nAnthropic. Introducing Claude, 2023. URL &lt;https://www.anthropic.com/index/introducing-claude/>.\n\nEdward Beeching, Lewis Tunstall, and Sasha Rush. Scaling Test-Time Compute with Open Models, 2024. URL &lt;https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute>.\n\nBradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. *arXiv preprint arXiv:2407.21787*, 2024.\n\nSanjiban Choudhury. Process Reward Models for LLM Agents: Practical Framework and Directions. *arXiv preprint arXiv:2502.10325*, 2025.\n\nGanqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process Reinforcement through Implicit Rewards. *arXiv preprint arXiv:2502.01456*, 2025.DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv preprint arXiv:2501.12948*, 2025.\n\nGemma Team and Google DeepMind. Introducing Gemma 3: The most capable model you can run on a single GPU or TPU, March 2025. URL &lt;https://blog.google/technology/developers/gemma-3>.\n\nZhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen, Yujiu Yang, Nan Duan, and Weizhu Chen. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=Sx038qxjek>.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset. In *Advances in Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021. URL &lt;https://openreview.net/forum?id=7Bywt2mQsCe>.\n\nShuyang Jiang, Yusheng Liao, Zhe Chen, Ya Zhang, Yanfeng Wang, and Yu Wang. MedS&lt;sup>3&lt;/sup>: Towards Medical Small Language Models with Self-Evolved Slow Thinking. *arXiv preprint arXiv:2501.12051*, 2025.\n\nAitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving Quantitative Reasoning Problems with Language Models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,*Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 3843–3857. Curran Associates, Inc., 2022. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf).\n\nWendi Li and Yixuan Li. Process Reward Model with Q-value Rankings. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=wQEdh2cgEk>.\n\nHunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s Verify Step by Step. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=v8L0pN6E0i>.\n\nRunze Liu, Fengshuo Bai, Yali Du, and Yaodong Yang. Meta-Reward-Net: Implicitly Differentiable Reward Learning for Preference-based Reinforcement Learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 22270–22284, 2022.\n\nRunze Liu, Yali Du, Fengshuo Bai, Jiafei Lyu, and Xiu Li. PEARL: Zero-shot Cross-task Preference Alignment and Robust Reward Learning for Robotic Manipulation. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, *International Conference on Machine Learning (ICML)*, volume 235 of *Proceedings of Machine Learning Research*, pages 30946–30964. PMLR, 21–27 Jul 2024. URL &lt;https://proceedings.mlr.press/v235/liu24o.html>.\n\nRunze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, and Bowen Zhou. Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. *arXiv preprint arXiv:2502.06703*, 2025.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, et al. Improve Mathematical Reasoning in Language Models by Automated Process Supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nAman Madaan, Niket Tandon, Prakash Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegr-effe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-Refine: Iterative Refinement with Self-Feedback. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46534–46594. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf).\n\nDakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative Reward Models. *arXiv preprint arXiv:2410.12832*, 2024.\n\nOpenAI. GPT-4 Technical Report. *arXiv preprint arXiv:2303.08774*, 2023.\n\nOpenAI. Learning to reason with LLMs, 2024a. URL &lt;https://openai.com/index/learning-to-reason-with-llms>.\n\nOpenAI. OpenAI o3-mini, 2024b. URL &lt;https://openai.com/index/openai-o3-mini>.\n\nQwen Team. QwQ-32B: Embracing the Power of Reinforcement Learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b>.Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=A6Y7AqlzLW>.\n\nZhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*, 2024.\n\nSkywork o1 Team. Skywork-o1 Open Series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nCharlie Victor Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=4FWAwZtd2n>.\n\nMingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, and Yu Cheng. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models. *arXiv preprint arXiv:2501.03124*, 2025.\n\nXiaoyu Tan, Tianchu Yao, Chao Qu, Bin Li, Minghao Yang, Dakuan Lu, Haozhe Wang, Xihe Qiu, Wei Chu, Yinghui Xu, et al. AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification. *arXiv preprint arXiv:2502.11520*, 2025.\n\nJonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n\nJun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. OpenR: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024a.\n\nPeiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, 2024b.\n\nWeiyun Wang, Zhangwei Gao, Lianjie Chen, Chen Zhe, Jinguo Zhu, Xiangyu Zhao, Yangzhou Liu, Yue Cao, Shenglong Ye, Xizhou Zhu, Lewei Lu, Haodong Duan, Yu Qiao, Jifeng Dai, and Wenhai Wang. VisualPRM: An Effective Process Reward Model for Multimodal Reasoning. *arXiv preprint arXiv:2503.10291*, 2025.\n\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. In *International Conference on Learning Representations (ICLR)*, 2023. URL &lt;https://openreview.net/forum?id=1PL1NIMMrw>.\n\nJason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in neural information processing systems (NeurIPS)*, volume 35, pages 24824–24837, 2022.Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=VNckp7JEHn>.\n\nZhihui Xie, Liyu Chen, Weichao Mao, Jingjing Xu, Lingpeng Kong, et al. Teaching Language Models to Critique via Reinforcement Learning. *arXiv preprint arXiv:2502.03492*, 2025.\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An Implementation of Generative PRM. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024.\n\nAn Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nRui Yang, Ruomeng Ding, Yong Lin, Huan Zhang, and Tong Zhang. Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024c. URL &lt;https://openreview.net/forum?id=jwh9MHEfmY>.\n\nLifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free Process Rewards without Process Labels. *arXiv preprint arXiv:2412.01981*, 2024.\n\nThomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjiae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, et al. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data. *arXiv preprint arXiv:2502.06737*, 2025.\n\nHanning Zhang, Pengcheng Wang, Shizhe Diao, Yong Lin, Rui Pan, Hanze Dong, Dylan Zhang, Pavlo Molchanov, and Tong Zhang. Entropy-Regularized Process Reward Model. *arXiv preprint arXiv:2412.11006*, 2024a.\n\nKaiyan Zhang, Jiayuan Zhang, Haoxin Li, Xuekai Zhu, Ermo Hua, Xingtai Lv, Ning Ding, Biqing Qi, and Bowen Zhou. OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees. In *International Conference on Learning Representations (ICLR)*, 2025a. URL &lt;https://openreview.net/forum?id=fGIqGfmgkW>.\n\nLunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative Verifiers: Reward Modeling as Next-Token Prediction. In *International Conference on Learning Representations (ICLR)*, 2025b. URL &lt;https://openreview.net/forum?id=Ccwp4tFETe>.\n\nYuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang. o1-Coder: an o1 Replication for Coding. *arXiv preprint arXiv:2412.00154*, 2024b.\n\nZhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The Lessons of Developing Process Reward Models in Mathematical Reasoning. *arXiv preprint arXiv:2501.07301*, 2025c.Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. ProcessBench: Identifying Process Errors in Mathematical Reasoning. *arXiv preprint arXiv:2412.06559*, 2024.\n\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46595–46623. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets\\\\_and\\\\_Benchmarks.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf).\n\nJianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, and Qiang Xu. Dyve: Thinking Fast and Slow for Dynamic Process Verification. *arXiv preprint arXiv:2502.11157*, 2025.\n\nJiachen Zhu, Congmin Zheng, Jianghao Lin, Kounianhua Du, Ying Wen, Yong Yu, Jun Wang, and Weinan Zhang. Retrieval-Augmented Process Reward Model for Generalizable Mathematical Reasoning. *arXiv preprint arXiv:2502.14361*, 2025.\n\nXuekai Zhu, Biqing Qi, Kaiyan Zhang, Xinwei Long, Zhouhan Lin, and Bowen Zhou. PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning. In Kevin Duh, Helena Gomez, and Steven Bethard, editors, *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 2571–2597, Mexico City, Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.142. URL &lt;https://aclanthology.org/2024.naacl-long.142/>.## A. Experimental Details\n\n### A.1. Scoring and Voting Methods\n\n**PRM-Last.** PRM-Last considers the process reward of the last step of the entire LLM response as the final score, i.e.,  $\\text{score} = r_T$ .\n\n**PRM-Avg.** PRM-Avg computes the mean process reward across all steps as the final score, i.e.,  $\\text{score} = \\frac{1}{T} \\sum_{t=1}^T r_t$ .\n\n**PRM-Min.** PRM-Min uses the minimum process reward across all steps as the final score, i.e.,  $\\text{score} = \\min_r \\{r_t\\}_{t=1}^T$ .\n\n### A.2. Implementation Details\n\nPrompt for CoT and code rationale generation is shown in Table A.2.\n\n#### Prompt for CoT and code rationale generation\n\n**[System]:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step with python code.\n\n**[User]:**\n\nThe following is the math problem and a solution (split into paragraphs, enclosed with tags and indexed from 1):\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n```\n&lt;paragraph_1>\n{solution_section_1}\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n{solution_section_n}\n&lt;/paragraph_n>\n```\n\nYour task is to verify the correctness of paragraph in the solution. Split your verification by ‘### Paragraph {{ID}}’.\n\nYour verification for each paragraph should be constructed by 2 parts, wrapped by ‘&lt;analyze>&lt;/analyze>’ and ‘&lt;verify>&lt;/verify>’ separately.1. 1. In ‘`&lt;analyze>&lt;/analyze>`’ part, you need to analyze the reasoning process and explain why the paragraph is correct or incorrect in detail.\n2. 2. In ‘`&lt;verify>&lt;/verify>`’ part, you must write **Python code** in the form of ‘````python\\n{CODE}\\n````’ to verify every details that can be verified by code. You can import PyPI (i.e., ‘`sympy`’, ‘`scipy`’ and so on) to implement complicated calculation. Make sure to print the critic results in the code. Every code will be executed automatically by system. You need to analyze the ‘[Code Output]’ after code executing.\n\n>Pay attention that you must follow the format of ‘````python\\n{CODE}\\n````’ when you write the code, otherwise the code will not be executed.\n\nAfter all verifications, if you identify an error in a paragraph, return the **index** of the paragraph where the earliest error occurs\\*\\*. Otherwise, return the **index** of -1 (which typically denotes \"not found\"\\*\\*. Please put your final answer (i.e., the index) within box in the form of ‘`$\\boxed{{INDEX}}$`’.\n\nFollowing [Zheng et al. \\(2024\\)](#); [Zhang et al. \\(2025c\\)](#), we use the prompt in Table A.2 to evaluate LLM-as-a-judge methods on ProcessBench ([Zheng et al., 2024](#)).\n\n#### Evaluation prompt for LLM-as-a-judge methods on ProcessBench\n\nI will provide a math problem along with a solution. They will be formatted as follows:\n\n[Math Problem]\n\n```\n&lt;math_problem>\n...(math problem)...\n&lt;/math_problem>\n```\n\n[Solution]\n\n```\n&lt;paragraph_1>\n...(paragraph 1 of solution)...\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n...(paragraph n of solution)...\n&lt;/paragraph_n>\n```\n\nYour task is to review each paragraph of the solution in sequence, analyzing, verifying, and critiquing the reasoning in detail. You need to provide the analyses and the conclusion in the following format:\n\n```\n&lt;analysis_1>\n...(analysis of paragraph 1)...\n&lt;/analysis_1>\n```...\n\n&lt;analysis\\_n>  \n ...(analysis of paragraph n)...  \n &lt;/analysis\\_n>\n\n&lt;conclusion>  \n Correct/Incorrect  \n &lt;/conclusion>\n\n\\* When you analyze each paragraph, you should use proper verification, recalculation, or reflection to indicate whether it is logically and mathematically valid. Please elaborate on the analysis process carefully.\n\n\\* If an error is detected in any paragraph, you should describe the nature and cause of the error in detail, and suggest how to correct the error or the correct approach. Once a paragraph is found to contain any error, stop further analysis of subsequent paragraphs (as they may depend on the identified error) and directly provide the conclusion of \"Incorrect.\"\n\nFor instance, given a solution of five paragraphs, if an error is found in the third paragraph, you should reply in the following format:\n\n&lt;analysis\\_1>  \n ...(analysis of paragraph 1)...  \n &lt;/analysis\\_1>\n\n&lt;analysis\\_2>  \n ...(analysis of paragraph 2)...  \n &lt;/analysis\\_2>\n\n&lt;analysis\\_3>  \n ...(analysis of paragraph 3; since an error is found here, also provide detailed critique and correction guideline)...  \n &lt;/analysis\\_3>\n\n&lt;conclusion>  \n Incorrect  \n &lt;/conclusion>\n\nNote that the analyses of paragraphs 4 and 5 should be skipped as the paragraph 3 has been found to contain an error.\n\n\\* Respond with your analyses and conclusion directly.\n\n---\n\nThe following is the math problem and the solution for you task:[Math Problem]\n\n{tagged\\_problem}\n\n[Solution]\n\n{tagged\\_response}\n\n#### Prompt for critique generation\n\n[User]:\n\nThe following is a math problem and my solution. Your task is to review and critique the paragraphs in solution step by step. Pay attention that you should not solve the problem and give the final answer. All of your task is to critique. Output your judgement of whether the paragraph is correct in the form of ‘ $\\boxed{\\{Yes|No\\}}$ ’ at the end of each paragraph verification:\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n&lt;paragraph\\_{idx}>\n\n{solution\\_section}\n\n&lt;/paragraph\\_{idx}>\n\n## B. Additional Results\n\nWe provide full results of ProcessBench in Table 6.\n\n**Model Size.** We investigate the impact of model size on GenPRM by evaluating variants with 1.5B, 7B, and 32B parameters. As shown in Table 7, scaling the model from 1.5B to 7B parameters yields substantial performance gains (57.3  $\\rightarrow$  75.2 and 63.4  $\\rightarrow$  80.5). However, further increasing the model size to 32B provides only marginal improvements, suggesting that the 7B variant offers the best balance between efficiency and effectiveness.\n\n**Data Size.** To assess the influence of training data volume, we train GenPRM on progressively larger subsets of ProcessBench (25%, 50%, and 100% of the full dataset). Table 8 demonstrates that Pass@1 F1 scores improve rapidly with initial data increases, but the growth rate slows substantially with additional data.\n\n**Inference Tokens.** We provide statistics of the reasoning tokens per step and per response in Table 9.**Table 6:** Full results of critic models and PRMs on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;br/>F1&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>45.8&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Open-Source LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>2.1&lt;/td>\n&lt;td>99.1&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>0.9&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;td>20.7&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>15.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>54.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>44.9&lt;/td>\n&lt;td>90.6&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>56.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>30.5&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>45.1&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>26.5&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>28.3&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>95.8&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>24.1&lt;/td>\n&lt;td>92.5&lt;/td>\n&lt;td>38.3&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-72B-Instruct&lt;/td>\n&lt;td>62.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>93.1&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>38.7&lt;/td>\n&lt;td>92.6&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>90.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>61.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B-Preview&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>61.4&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>57.8&lt;/td>\n&lt;td>55.7&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>61.3&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>50.2&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>59.0&lt;/td>\n&lt;td>37.9&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>15.4&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>\n&lt;td>37.0&lt;/td>\n&lt;td>92.7&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>57.1&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>47.0&lt;/td>\n&lt;td>66.5&lt;/td>\n&lt;td>55.1&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>68.7&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>97.4&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>64.7&lt;/td>\n&lt;td>87.7&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>57.2&lt;/td>\n&lt;td>76.1&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>63.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>15.0&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>99.0&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>8.2&lt;/td>\n&lt;td>43.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>24.2&lt;/td>\n&lt;td>98.4&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>21.4&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>10.1&lt;/td>\n&lt;td>51.0&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>43.8&lt;/td>\n&lt;td>62.2&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>14.0&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage1&lt;/td>\n&lt;td>46.9&lt;/td>\n&lt;td>42.0&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>38.2&lt;/td>\n&lt;td>35.6&lt;/td>\n&lt;td>23.9&lt;/td>\n&lt;td>19.8&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>21.9&lt;/td>\n&lt;td>24.5&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage2&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>44.0&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;td>35.0&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>19.1&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>18.9&lt;/td>\n&lt;td>96.6&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>7.4&lt;/td>\n&lt;td>93.8&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>4.0&lt;/td>\n&lt;td>95.0&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>28.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>95.3&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>90.1&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>87.3&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>29.8&lt;/td>\n&lt;td>86.1&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;td>55.7&lt;/td>\n&lt;td>85.5&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>83.0&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RetrievalPRM-7B&lt;/td>\n&lt;td>64.7&lt;/td>\n&lt;td>88.1&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>56.0&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>60.2&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>62.7&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Universal-PRM-7B&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>85.8&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Direct Generative PRM-7B&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;td>81.4&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>80.0&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>44.8&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;td>72.6&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Pass@1)&lt;/td>\n&lt;td>67.7&lt;/td>\n&lt;td>94.0&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>87.0&lt;/td>\n&lt;td>80.3&lt;/td>\n&lt;td>68.3&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>63.5&lt;/td>\n&lt;td>77.4&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Maj@8)&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>80.5&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>80.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Dyve-14B&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>58.3&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>49.0&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>-&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>87.3&lt;/td>\n&lt;td>74.2&lt;/td>\n&lt;td>88.2&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>67.9&lt;/td>\n&lt;td>82.0&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>64.8&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>78.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Pass@1)&lt;/td>\n&lt;td>73.1&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>79.4&lt;/td>\n&lt;td>84.1&lt;/td>\n&lt;td>81.7&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>70.3&lt;/td>\n&lt;td>75.5&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Maj@8)&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>98.5&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;td>88.7&lt;/td>\n&lt;td>86.3&lt;/td>\n&lt;td>79.0&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>84.2&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>82.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## C. Cases\n\nIn this section, we analyze two cases to have a better understanding of GenPRM. The case in Figure 5 shows that the code execution feedback can correct the mistakes in CoT and enhance the process supervision abilities of GenPRM. The case in Figure 6 demonstrates that GenPRM provides accurate process supervision with CoT reasoning only.**Table 7:** Evaluation results of GenPRM with different sizes on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model Size&lt;/th>\n&lt;th>Metric&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>OlympiadBench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"2\">1.5B&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>55.1&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Maj@8&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>65.3&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>63.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">7B&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>80.3&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Maj@8&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>80.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">32B&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>81.7&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Maj@8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>86.3&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>80.1&lt;/td>\n&lt;td>82.6&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 8:** Evaluation results of GenPRM with different proportions of training data on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Data Size&lt;/th>\n&lt;th>Metric&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>OlympiadBench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>25%&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>71.8&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>71.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>50%&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>71.5&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>74.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>100%&lt;/td>\n&lt;td>Pass@1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>80.3&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 9:** Statistics of the output tokens of GenPRM.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Step&lt;/td>\n&lt;td>344.7&lt;/td>\n&lt;td>416.2&lt;/td>\n&lt;td>432.5&lt;/td>\n&lt;td>503.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Response&lt;/td>\n&lt;td>2771.4&lt;/td>\n&lt;td>3200.2&lt;/td>\n&lt;td>4112.9&lt;/td>\n&lt;td>4877.1&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>**Problem:****Simplify  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\cos 86^\\circ$ .****Enter your answer is a trigonometric function evaluated at an integer, such as \"sin 7\". (The system will assume that the angle is in degrees.)****System:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step.\n\n**User (Turn 1):**\n\nTo simplify the expression  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\cos 86^\\circ$ , we start by using the identity  $\\cos(90^\\circ - x) = \\sin x$ . This allows us to rewrite  $\\cos 86^\\circ$  as  $\\sin 2^\\circ$ . Thus, the expression becomes:  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\sin 2^\\circ$\n\n**Assistant (Turn 1):**\n\n&lt;analyze>\n\nThe first paragraph uses the identity  $\\cos(90^\\circ - x) = \\sin(x)$  to rewrite  $\\cos(86^\\circ)$  as  $\\sin(2^\\circ)$ . This is correct because  $86^\\circ$  is  $90^\\circ - 2^\\circ$ , so substituting  $x = 2^\\circ$  gives  $\\cos(86^\\circ) = \\sin(2^\\circ)$ . The substitution is valid here. The expression is correctly transformed into  $\\cos 54^\\circ \\cos 4^\\circ - \\cos 36^\\circ \\sin 2^\\circ$ . This step is accurate.\n\n&lt;/analyze>\n\n&lt;verify>\n\n```\nimport math\nimport sympy as sp\n# Define the angles in degrees\nangle1 = 54\nangle2 = 4\nangle3 = 36\nangle4 = 86\n# Compute cos(54°) and cos(86°) using sympy's cos function\ncos54 = sp.cos(sp.rad(angle1))\ncos86 = sp.cos(sp.rad(angle4))\nsin2 = sp.sin(sp.rad(2))\ncos36 = sp.cos(sp.rad(angle3))\n# Check if cos86° equals sin2°\nis_equal = sp.simplify(cos86 - sin2) == 0\nprint(f\"cos(86°) equals sin(2°)? {is_equal}\")\n# Check the transformed expression\ntransformed = sp.cos(sp.rad(angle1)) * sp.cos(sp.rad(angle2)) - sp.cos(sp.rad(angle3)) * sin2\noriginal = sp.cos(sp.rad(angle1)) * sp.cos(sp.rad(angle2)) - sp.cos(sp.rad(angle3)) * sp.cos(sp.rad(angle4))\nprint(f\"Original expression: {original}\")\nprint(f\"Transformed expression: {transformed}\")\n```\n\n[Code Output]\n\n```\ncos(86°) equals sin(2°)? False\nOriginal expression: -(1/4 + sqrt(5)/4)*cos(43*pi/90) + sqrt(5)/8 - sqrt(5)/8*cos(pi/45)\nTransformed expression: -(1/4 + sqrt(5)/4)*sin(pi/90) + sqrt(5)/8 - sqrt(5)/8*cos(pi/45)\n```\n\nWait, the output shows that  $\\cos(86^\\circ)$  is not exactly equal to  $\\sin(2^\\circ)$  in terms of exact symbolic comparison. However, numerically they are equal. Let me check with numerical values:\n\n```\nimport math\ncos86 = math.cos(math.radians(86))\nsin2 = math.sin(math.radians(2))\nprint(\"Are they equal numerically?\", math.isclose(cos86, sin2))\n```\n\n[Code Output]\n\nAre they equal numerically? False\n\nHmm, this is unexpected. Wait, maybe due to floating-point precision? Let me compute  $\\cos(86^\\circ)$  and  $\\sin(2^\\circ)$  numerically and see if they are equal.\n\nWait, let's compute  $\\cos(86^\\circ)$  and  $\\sin(2^\\circ)$ :\n\n```\ncos(86°) ≈ cos(86) ≈ 0.06975647374412537\nsin(2°) ≈ 0.03489949670250097\n```\n\nThese are not equal. So the initial assumption that  $\\cos(86^\\circ) = \\sin(2^\\circ)$  is incorrect. Therefore, the paragraph 1 is wrong. The error is in the trigonometric identity used here.\n\nWait, but according to the identity  $\\cos(90^\\circ - x) = \\sin(x)$ , so  $\\cos(86^\\circ) = \\cos(90^\\circ - 2^\\circ) = \\sin(2^\\circ)$ . However, numerically they are not equal. So there is a mistake here. The paragraph incorrectly applied the identity, leading to an incorrect substitution. The correct substitution should be  $\\cos(86^\\circ) = \\sin(2^\\circ)$ , but numerically they are not equal. So the error is in paragraph 1.\n\nWait, but maybe the problem is that the identity is correct, but the numerical check is wrong? Let me verify:\n\nWait,  $\\cos(86^\\circ)$  is  $\\cos(90^\\circ - 4^\\circ) = \\sin(4^\\circ)$ , not  $2^\\circ$ . Wait, no, wait:  $\\cos(90^\\circ - x) = \\sin(x)$ . So if angle is  $86^\\circ$ , then  $90^\\circ - 86^\\circ = 4^\\circ$ , so  $\\cos(86^\\circ) = \\sin(4^\\circ)$ . Wait, that's the opposite of what the paragraph says. The paragraph said  $\\cos(86^\\circ) = \\sin(2^\\circ)$ , but according to the identity, it should be  $\\sin(4^\\circ)$ . So that's the mistake. The paragraph incorrectly used  $2^\\circ$  instead of  $4^\\circ$ . That's a critical error.\n\nSo paragraph 1 is wrong because it used  $2^\\circ$  instead of  $4^\\circ$  in the substitution. Therefore, the code verification shows that the substitution is incorrect, leading to an incorrect expression. The error is in paragraph 1.\n\nSo the first paragraph is incorrect.\n\n&lt;/verify>\n\n&lt;output>\n\nJudgement:  $\\boxed{\\text{No}}$ \n\n&lt;/output>\n\nFigure 5: The first case of GenPRM.**Problem:****Compute the distance between the two foci of the ellipse  $x^2 + 4y^2 = 9$ .****System:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step.\n\n-----\n\n**User (Turn 1):**\n\nSince  $x^2 + 4y^2 = 9$ , we divide both sides by 9 to obtain  $\\frac{x^2}{9} + \\frac{4y^2}{9} = 1$ .\n\n**Assistant (Turn 1):****&lt;analyze>**\n\nLet's analyze the Paragraph 1 step by step: 1. The original equation is given as  $x^2 + 4y^2 = 9$ . Dividing both sides by 9 is correct because the standard form of an ellipse requires the right-hand side to be 1. This results in  $\\frac{x^2}{9} + \\frac{4y^2}{9} = 1$ . 2. The semi-major axis  $a$  is correctly identified as 3 because the denominator under  $x^2$  is 9, so  $a^2 = 9$  leading to  $a = 3$ . 3. The semi-minor axis  $b$  is calculated as  $\\frac{3}{2}$ . Since the coefficient under  $y^2$  after division is  $\\frac{4}{9}$ , so  $b^2 = \\frac{9}{4}$  (since the denominator under  $y^2$  would be  $\\frac{9}{4}$ ), but wait, actually the equation after division is  $\\frac{x^2}{9} + \\frac{y^2}{(9/4)} = 1$ , so  $b^2 = 9/4$ , so  $b = 3/2$ . That part is correct. **So paragraph 1 is correct.**\n\n**&lt;/analyze>****&lt;output>**\n\nJudgement:  **$\\boxed{\\text{Yes}}$**\n\n**&lt;/output>****User (Turn 2)**\n\nThe distance between the two foci of an ellipse with semi-major axis  $a$  and semi-minor axis  $b$  is given by  $2c$ , where\n\n **$c = \\sqrt{a^2 - b^2} = \\sqrt{3^2 - \\left(\\frac{3}{2}\\right)^2} = \\sqrt{\\frac{27}{4} - \\frac{9}{4}} = \\sqrt{\\frac{18}{4}}$** \n **$\\frac{3\\sqrt{2}}{2}$** \n **$\\frac{3\\sqrt{2}}{2}$** \n**Assistant (Turn 2)****&lt;analyze>**\n\nLet's analyze the Paragraph 2 step by step: 1. The formula for the distance between foci is  $2c$ , where  $c = \\sqrt{a^2 - b^2}$ . This is correct for an ellipse with major axis along the x-axis (since the denominator under  $x^2$  is larger). 2. Plugging in  $a = 3$  and  $b = 3/2$ :\n\n$a^2 = 9$ ,  $b^2 = (3/2)^2 = 9/4$\n\n$c = \\sqrt{9 - 9/4} = \\sqrt{27/4}$  (Wait, 9 is 36/4, so  $36/4 - 9/4 = 27/4$ . So  $\\sqrt{27/4}$  is  $(3\\sqrt{3})/2$ , but in the solution they have  $\\sqrt{27/4 - 9/4} = \\sqrt{18/4}$ . Wait, hold on, that's an error! Wait,  $9 - 9/4 = 27/4$ , not  $18/4$ . Wait, 9 is 36/4, so  $36/4 - 9/4 = 27/4$ . Therefore  $\\sqrt{27/4}$  is  $(3\\sqrt{3})/2$ . But in the solution, they wrote  $\\sqrt{27/4 - 9/4} = \\sqrt{18/4}$ . Wait, that's wrong. The calculation inside the sqrt should be  $27/4$ , not  $18/4$ . So the error is here. Wait, but let me check again. Wait, the user's solution says  $\\sqrt{27/4 - 9/4}$  which is  $\\sqrt{18/4}$ . Wait, that's a mistake. So the error is in the arithmetic here. The correct calculation should be  $9 - (3/2)^2 = 9 - 2.25 = 6.75$ , which is  $27/4$ . So  $\\sqrt{27/4}$  is  $3\\sqrt{3}/2 \\approx 2.598$ , but the solution says  $\\sqrt{18/4}$  which is  $\\sqrt{4.5} \\approx 2.121$ . Therefore, there is an arithmetic mistake here. Therefore, paragraph 2 is incorrect. Wait, but maybe I made a mistake here? Let me recheck. The user's solution says:\n\n\" $c = \\sqrt{3^2 - (3/2)^2} = \\sqrt{27/4 - 9/4} = \\sqrt{18/4} = 3\\sqrt{2}/2$ .\"\n\nWait, 3 squared is 9, not 27. Wait, hold on, the user wrote  $3^2 - (3/2)^2 = 9 - (9/4) = (36/4 - 9/4) = 27/4$ . But in their calculation, they wrote  $\\sqrt{27/4 - 9/4}$  which would be  $\\sqrt{18/4}$ . Wait, that's a mistake. The correct expression is  $\\sqrt{9 - 9/4} = \\sqrt{27/4}$ . Therefore, the step where they wrote  $\\sqrt{27/4 - 9/4}$  is incorrect. The correct calculation is  $\\sqrt{9 - 9/4} = \\sqrt{27/4}$ . So the error is in the arithmetic here. **Therefore, paragraph 2 is incorrect.**\n\n**&lt;/analyze>****&lt;output>**\n\nJudgement:  **$\\boxed{\\text{No}}$**\n\n**&lt;/output>**\n\nFigure 6: The second case of GenPRM.\n",
    "durationMs": 913,
    "url": "https://huggingface.co/papers/2504.00891"
  },
  "sourceToolAssistantUUID": "b60ab32b-05b8-4ba8-acf3-b797b0faeaf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
`````

</details>

---

### Tool call

_source line 30 · 2026-05-27T15:57:44.315Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011qXw5kyxy1oE1nEKfQqfRy`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2504.00891",
  "prompt": "Extract the FULL text of the following sections from this paper:\n1. Introduction (entire section with all details)\n2. Method / Approach (entire section including ALL subsections - especially details about Relative Progress Estimation, rationale synthesis, code verification, training procedure)\n3. Experiments (key results, tables, comparisons)\n4. Conclusion and Limitations\n\nFocus on technical details: how is RPE defined? How is rationale data synthesized? How does code verification work? What models are used as base? What is the training data composition? What are the key experimental numbers?\n\nReturn all text as completely as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a43057d6-796f-42ed-b794-818d55906be8",
  "isSidechain": false,
  "requestId": "req_011CbTMBASitVLAnukXpbZXq",
  "type": "assistant",
  "uuid": "51442a18-2709-40a8-85de-ac9915c44d74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WTVLTxGsk45BBYGn43po8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 15150,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 15150,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 613
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "51442a18-2709-40a8-85de-ac9915c44d74",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper for research innovation",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Tool result

_source line 33 · 2026-05-27T15:57:51.072Z_

<details><summary>↩ Tool result · `toolu_011qXw5kyxy1oE1nEKfQqfRy`</summary>

```text
I appreciate your request, but I need to be transparent about what I'm encountering: the content you've provided appears to be a PDF file encoded in binary/compressed format (showing PDF stream objects with FlateDecode compression), not readable text.

The visible portions show PDF structural metadata like:
- Object references (109 0 obj, 110 0 obj, etc.)
- Compression filters and stream lengths
- Font and image definitions
- But the actual text content is compressed and not directly readable in this format

**What I cannot do:**
Extract the full Introduction, Method, Experiments, and Conclusion sections from this encoded PDF, as the text is not accessible to me in its current state.

**What would help:**
1. **Provide the paper as plain text or uncompressed PDF** - I could then extract and summarize those sections
2. **Share the paper's DOI or title** - I could reference publicly available versions
3. **Paste readable text excerpts** - I could work with actual content you've copied

**If you have access to the PDF directly**, you could:
- Copy-paste the text sections you need
- Use a PDF-to-text converter first
- Share the paper title so I can work with publicly available versions

I'm happy to help summarize the technical details about RPE, rationale synthesis, code verification, and experimental results—but I need the text content to be readable first.

[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/webfetch-1779897464340-6e8pig.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51442a18-2709-40a8-85de-ac9915c44d74",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "44dc2e10-380c-4406-90ec-9aa517edb058",
  "toolUseResult": {
    "bytes": 1397815,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I need to be transparent about what I'm encountering: the content you've provided appears to be a PDF file encoded in binary/compressed format (showing PDF stream objects with FlateDecode compression), not readable text.\n\nThe visible portions show PDF structural metadata like:\n- Object references (109 0 obj, 110 0 obj, etc.)\n- Compression filters and stream lengths\n- Font and image definitions\n- But the actual text content is compressed and not directly readable in this format\n\n**What I cannot do:**\nExtract the full Introduction, Method, Experiments, and Conclusion sections from this encoded PDF, as the text is not accessible to me in its current state.\n\n**What would help:**\n1. **Provide the paper as plain text or uncompressed PDF** - I could then extract and summarize those sections\n2. **Share the paper's DOI or title** - I could reference publicly available versions\n3. **Paste readable text excerpts** - I could work with actual content you've copied\n\n**If you have access to the PDF directly**, you could:\n- Copy-paste the text sections you need\n- Use a PDF-to-text converter first\n- Share the paper title so I can work with publicly available versions\n\nI'm happy to help summarize the technical details about RPE, rationale synthesis, code verification, and experimental results—but I need the text content to be readable first.\n\n[Binary content (application/pdf, 1.3MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/webfetch-1779897464340-6e8pig.pdf]",
    "durationMs": 6754,
    "url": "https://arxiv.org/pdf/2504.00891"
  },
  "sourceToolAssistantUUID": "51442a18-2709-40a8-85de-ac9915c44d74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-27T15:57:51.076Z_

```json
{
  "parentUuid": "44dc2e10-380c-4406-90ec-9aa517edb058",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d53c0280-2a54-4e4b-ac5c-c1404f5babc7",
  "timestamp": "2026-05-27T15:57:51.076Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-27T15:57:53.476Z_

<details><summary>Logged reasoning block</summary>

```text
I got the full paper content from Hugging Face. Let me read the saved file to get the full details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d53c0280-2a54-4e4b-ac5c-c1404f5babc7",
  "isSidechain": false,
  "requestId": "req_011CbTMCHNDwDYb6JXxbFDst",
  "type": "assistant",
  "uuid": "a76dbe51-9edf-4fa9-9a76-8f9d08b9ad0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cxKyh2hRcPegiHGWD9W8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1609,
      "cache_read_input_tokens": 15763,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 15763,
          "cache_creation_input_tokens": 1609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1609
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

_source line 36 · 2026-05-27T15:57:53.948Z_

I got the full paper content from Hugging Face. Let me read it now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a76dbe51-9edf-4fa9-9a76-8f9d08b9ad0b",
  "isSidechain": false,
  "requestId": "req_011CbTMCHNDwDYb6JXxbFDst",
  "type": "assistant",
  "uuid": "9fd1b9be-a5b6-4e84-afb7-ee4bbf377264",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cxKyh2hRcPegiHGWD9W8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1609,
      "cache_read_input_tokens": 15763,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 15763,
          "cache_creation_input_tokens": 1609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1609
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

_source line 37 · 2026-05-27T15:57:54.712Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RnV2q2WPAU4bk5PSNerGyZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fd1b9be-a5b6-4e84-afb7-ee4bbf377264",
  "isSidechain": false,
  "requestId": "req_011CbTMCHNDwDYb6JXxbFDst",
  "type": "assistant",
  "uuid": "3c46b0fb-2cef-4d7f-a654-7a74e2f83685",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015cxKyh2hRcPegiHGWD9W8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1609,
      "cache_read_input_tokens": 15763,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 15763,
          "cache_creation_input_tokens": 1609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1609
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

_source line 38 · 2026-05-27T15:57:55.052Z_

<details><summary>↩ Tool result · reported error · `toolu_01RnV2q2WPAU4bk5PSNerGyZ`</summary>

```text
File content (37144 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c46b0fb-2cef-4d7f-a654-7a74e2f83685",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "b494a835-1eea-4f5f-9346-1eda65f82b30",
  "toolUseResult": "Error: File content (37144 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "3c46b0fb-2cef-4d7f-a654-7a74e2f83685",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-27T15:57:58.362Z_

<details open><summary>🔧 Tool call — Read · `toolu_01617zXdiqZNaY78TtUNdWLE`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt",
  "limit": 500,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b494a835-1eea-4f5f-9346-1eda65f82b30",
  "isSidechain": false,
  "requestId": "req_011CbTMCaNAx6gQDypmiv8hp",
  "type": "assistant",
  "uuid": "d5547b17-e32e-47af-97a4-6a3aca5cbfd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzWaqbr3FpeJ57YC39u23x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 17372,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 450,
          "cache_read_input_tokens": 17372,
          "cache_creation_input_tokens": 246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 246
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

_source line 40 · 2026-05-27T15:57:58.654Z_

<details><summary>↩ Tool result · `toolu_01617zXdiqZNaY78TtUNdWLE`</summary>

```text
0	# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning
1	
2	Jian Zhao&lt;sup>1,3\*&lt;/sup>, Runze Liu&lt;sup>1,2\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>
3	
4	&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology
5	
6	Recent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.
7	
8	**Figure 1: GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: (a) As a verifier:** GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling. **(b) As a critic:** GenPRM-7B demonstrates superior critique capabilities, achieving **3.4x** greater performance gains than DeepSeek-R1-Distill-Qwen-7B after 3 refinement iterations.
9	
10	\* Equal contribution
11	
12	† Project lead & Work done during an internship at Shanghai AI Laboratory
13	
14	‡ Corresponding authors: Biqing Qi (qibiqing@pjlab.org.cn), Xiu Li (li.xiu@sz.tsinghua.edu.cn), and Bowen Zhou (zhoubowen@tsinghua.edu.cn)The diagram illustrates the architectural differences between classification-based PRMs and GenPRM. On the left, under the heading 'Classification-based PRM', two models are shown: 'Discriminative PRM' and 'Direct Generative PRM'. The Discriminative PRM consists of a 'value head' that outputs a score of 0.9, marked with a green checkmark. The Direct Generative PRM outputs a 'Yes' label, which is then converted to a score of 0.8, also marked with a green checkmark. On the right, under the heading 'Generative PRM (Ours)', the 'GenPRM' model is shown. It branches into three parallel paths, each consisting of a yellow circle (CoT Verification) followed by a green circle (Code Verification) and a 'Yes' or 'No' label. The top path outputs 'Yes', the middle path outputs 'No', and the bottom path outputs 'No'. These three paths converge into a final score of 0.2, which is marked with a red 'X'. A legend at the bottom identifies the yellow circle as 'CoT Verification' and the green circle as 'Code Verification'.
15	
16	Figure 2: Comparison between GenPRM (right) and previous classification-based PRMs (left).
17	
18	## 1. Introduction
19	
20	Large Language Models (LLMs) have shown significant advances in recent years (OpenAI, 2023; Anthropic, 2023; OpenAI, 2024a,b; DeepSeek-AI et al., 2025). As OpenAI o1 demonstrates the great effectiveness of scaling test-time compute (OpenAI, 2024a), an increasing number of researches focus on Test-Time Scaling (TTS) methods to improve the reasoning performance of LLMs (Snell et al., 2025; Liu et al., 2025).
21	
22	Effective TTS requires high-quality verifiers, such as Process Reward Models (PRMs) (Liu et al., 2025). However, existing PRMs face several limitations. They exhibit limited process supervision capabilities and struggle to generalize across different models and tasks (Zheng et al., 2024; Zhang et al., 2025c; Liu et al., 2025). Furthermore, most current approaches train PRMs as classifiers that output scalar values, neglecting the natural language generation abilities of LLMs, which are pre-trained on extensive corpora. This classifier-based modeling inherently prevents PRMs from leveraging test-time scaling methods to enhance process supervision capabilities. These limitations lead us to the following research question: *How can generative modeling enhance the process supervision capabilities of PRMs while enabling test-time scaling?*
23	
24	In this work, we address these challenges through a generative process reward model, named GenPRM. Specifically, GenPRM differs from classification-based PRMs in that GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) (Wei et al., 2022) reasoning and code verification processes before providing final judgment. To improve conventional hard label estimation, we propose Relative Progress Estimation (RPE), which leverages a relative criterion for label estimation. Additionally, we introduce a rationale synthesis framework with code verification to obtain high-quality process supervision reasoning data. A comparison of our method with previous classification-based methods is presented in Figure 2.
25	
26	Our contributions can be summarized as follows:
27	
28	1. 1. We propose a generative process reward model that performs explicit CoT reasoning with code verification and utilizes Relative Progress Estimation to obtain accurate PRM labels.
29	2. 2. Empirical results on ProcessBench and common mathematical reasoning tasks demonstrate that GenPRM outperforms prior classification-based PRMs. Additionally, smaller GenPRM models can surpass larger PRMs via TTS.
30	3. 3. We provide a new perspective on PRMs in this work, fully leveraging their TTS capabilities, reshaping their applications, and opening new directions for future research in process supervision.## 2. Preliminaries
31	
32	### 2.1. Markov Decision Process
33	
34	Following [Liu et al. \(2025\)](#), we formulate the test-time scaling process with PRMs as a Markov Decision Process (MDP) defined by  $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$ , where  $\mathcal{S}$  is the state space,  $\mathcal{A}$  is the action space,  $P$  represents transition dynamics,  $r : \mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$  is the reward function, and  $\gamma \in [0, 1]$  is the discount factor. Starting with a prompt set  $\mathcal{X}$  and an initial state  $s_1 = x \sim \mathcal{X}$ , the policy model  $\pi_\theta$  generates an action  $a_1 \sim \pi_\theta(\cdot | s_1)$ .&lt;sup>1&lt;/sup> Unlike traditional RL methods with stochastic transitions ([Liu et al., 2022, 2024](#)), transitions in LLMs are deterministic, i.e.,  $s_{t+1} = P(\cdot | s_t, a_t) = [s_t, a_t]$ , where  $[\cdot, \cdot]$  denotes string concatenation. This process continues until the episode terminates (i.e., generating the [EOS] token), obtaining a trajectory of  $T$  steps:  $\tau = \{a_1, a_2, \dots, a_T\}$ . The goal is to optimize either the reward of each step (as in search-based methods) or the reward over the full response (as in Best-of-N sampling).
35	
36	### 2.2. Supervised Fine-Tuning
37	
38	Supervised Fine-Tuning (SFT) trains a model to predict the next token based on prior context. For a dataset  $\mathcal{D}_{\text{SFT}} = \{(x^{(i)}, y^{(i)})\}_{i=1}^N$ , the SFT loss is:
39	
40	$$\mathcal{L}_{\text{SFT}}(\theta) = -\mathbb{E}_{(x,y) \sim \mathcal{D}_{\text{SFT}}} \left[ \sum_{t=1}^{|y|} \log \pi_\theta(y_t | x, y_{1:t-1}) \right], \quad (1)$$
41	
42	where  $\pi_\theta$  represents a model with parameters  $\theta$ .
43	
44	### 2.3. Test-Time Scaling
45	
46	In this work, we consider two test-time scaling methods, including majority voting and Best-of-N.
47	
48	**Majority Voting.** Majority voting ([Wang et al., 2023](#)) selects the answer that appears the most frequently among all solutions.
49	
50	**Best-of-N.** Best-of-N (BoN) ([Brown et al., 2024](#); [Snell et al., 2025](#)) selects the best answer from  $N$  candidate solutions.
51	
52	## 3. Method
53	
54	In this section, we first describe how to develop GenPRM and integrate the reasoning process with code verification. We then introduce how to scale test-time compute of policy models using GenPRM and apply TTS for GenPRM. Last, we present the improved label estimation method and data generation and filtering framework of GenPRM.
55	
56	### 3.1. GenPRM and Test-Time Scaling
57	
58	#### 3.1.1. From Discriminative PRM to Generative PRM
59	
60	**Discriminative PRM.** Assume we have a PRM dataset  $\mathcal{D}_{\text{Disc}} = \{(s_t, a_t), r_t\}$ , where  $r_t \in \{0, 1\}$  for PRM labels with hard estimation. The discriminative PRM  $r_\psi$  is trained via cross-entropy loss ([Skywork](#)
61	
62	&lt;sup>1&lt;/sup>Following [Snell et al. \(2025\)](#); [Liu et al. \(2025\)](#), we refer to models that generate solutions as policy models.The diagram illustrates the GenPRM framework, which consists of six key parts:
63	
64	- **① Solution Generation & MC Reward Estimation:** A math problem is solved by generating intermediate steps (a&lt;sub>11&lt;/sub>, a&lt;sub>21&lt;/sub>, a&lt;sub>31&lt;/sub>, a&lt;sub>12&lt;/sub>, a&lt;sub>22&lt;/sub>, a&lt;sub>32&lt;/sub>). Correct steps (q&lt;sub>1&lt;/sub>, q&lt;sub>2&lt;/sub>) are marked with blue circles, and incorrect steps (q&lt;sub>3&lt;/sub>) are marked with red circles. The MC score for a step is calculated as  $MC(s_{12}, a_{12}) = \frac{2}{3}$ .
65	- **② Relative Progress Estimation:** The process reward is estimated as  $P_t = \frac{MC(s_t, a_t)}{MC(s_t)} \geq \epsilon$ . If the reward is high,  $\hat{r}_t = 1$  (green checkmark), otherwise  $\hat{r}_t = 0$  (red X).
66	- **③ Rationale Synthesis:** A problem is analyzed using CoT (Chain of Thought) analysis to generate a rationale. This rationale is then verified using code verification (e.g., Python code) to check for potential errors. The final label is a judgement of Yes/No.
67	- **④ GenPRM Training:** Data (23K) is used for SFT (Supervised Fine-Tuning) to train GenPRM. Consensus filtering is applied to the training data.
68	- **⑤ Policy Model Test-Time Scaling:** The trained GenPRM functions as a verifier or critic. It can be used to verify a solution (GenPRM as a Verifier) or critique a solution (GenPRM as a Critic).
69	- **⑥ GenPRM Test-Time Scaling:** The performance of GenPRM is improved through test-time scaling. Multiple steps are analyzed and verified, and their rewards are aggregated to produce a final reward  $r$ .
70	
71	Legend:
72	
73	- a Intermediate Step
74	- q Correct Answer
75	- q Incorrect Answer
76	- r Single Reward Judgement
77	- r Aggregated Reward Judgement
78	
79	**Figure 3: Overall framework of GenPRM.** Our framework consists of six key parts: ① The policy model generates solution steps, with MC scores estimated from rollout trajectories. ② Our proposed RPE derives accurate PRM labels. ③ High-quality process supervision data is synthesized through CoT reasoning augmented with code verification. ④ We apply consensus filtering followed by SFT to train GenPRM. ⑤ The trained GenPRM functions as a verifier or critic, enabling enhanced test-time scaling for policy models. ⑥ The performance of GenPRM further improves through test-time scaling.
80	
81	o1 Team, 2024; Zhang et al., 2025c):
82	
83	$$\mathcal{L}_{CE}(\psi) = -\mathbb{E}_{(s_t, a_t, r_t) \sim \mathcal{D}_{Disc}} [r_t \log r_\psi(s_t, a_t) + (1 - r_t) \log(1 - r_\psi(s_t, a_t))]. \quad (2)$$
84	
85	**Direct Generative PRM.** With a dataset  $\mathcal{D}_{Direct-Gen} = \{(s_t, a_t), r_t\}$ , where  $r_t$  is Yes for a correct step and No otherwise, the direct generative PRM (Xiong et al., 2024) is trained through SFT to predict Yes or No for each step. For step  $t$ , we use the probability of the Yes token as the predicted process reward  $\hat{r}_t$ :
86	
87	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t). \quad (3)$$
88	
89	**Generative PRM.** By equipping the direct generative PRM with an explicit reasoning process like CoT (Wei et al., 2022), we obtain a generative PRM. Let  $v_{1:t-1}$  denote the rationale from step 1 to  $t-1$  and  $v_t$  denote the rationale for step  $t$ . Assume we have a dataset  $\mathcal{D}_{Gen} = \{(s_t, a_t, v_{1:t-1}), (v_t, r_t)\}$ . GenPRM learns to reason and verify each step via SFT on this dataset. The generative process reward  $\hat{r}_t$  can be obtained via the following equation:
90	
91	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}, v_t), \quad \text{where } v_t \sim r_\psi(\cdot \mid s_t, a_t, v_{1:t-1}) \quad (4)$$
92	
93	**Generative PRM with Code Verification.** If we only verify the reasoning step with CoT based on natural language, the process may lack robustness in certain complex scenarios (Zhu et al., 2024; Gou et al., 2024). The difference between the generative PRM and the generative PRM with code verification is that the latter generates code to verify the reasoning step by executing it and provides the judgment based on the execution results. At step  $t$ , after generating the rationale  $v_t$  containing CoT and code, we execute the code and obtain feedback  $f_t$ . Given the current state  $s_t$ , action  $a_t$ , previous rationales  $v_{1:t-1}$ , and previous corresponding execution feedback  $f_{1:t-1}$ , the PRM first generates therationale  $v_t$ . After execution and obtaining the feedback  $f_t$ , we compute the final generative process reward as follows:
94	
95	$$\hat{r}_t = r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}, f_{1:t-1}, v_t, f_t), \quad \text{where } v_t \sim r_\psi(\cdot \mid s_t, a_t, v_{1:t-1}, f_{1:t-1}) \quad (5)$$
96	
97	In the following sections, we refer to GenPRM as this generative PRM type with code verification. The effectiveness of CoT and code verification can be found in Section 4.4.
98	
99	### 3.1.2. Test-Time Scaling
100	
101	**Policy Model TTS: GenPRM as a Verifier.** To scale the test-time compute of policy models, we can sample multiple responses from policy models and then use GenPRM as a verifier to select the final answer (Snell et al., 2025) in the way of parallel TTS.
102	
103	**Policy Model TTS: GenPRM as a Critic.** By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and we can scale the refinement process with multiple turns in a sequential TTS manner.
104	
105	**GenPRM TTS.** When evaluating each solution step, we first sample  $N$  reasoning verification paths and then use majority voting to obtain the final prediction by averaging the rewards. For GenPRM without code verification, the rewards are computed as follows:
106	
107	$$\hat{r}_t = \frac{1}{N} \sum_{i=1}^N r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}^i, v_t^i). \quad (6)$$
108	
109	And we can further incorporate code verification and execution feedback into this reasoning process:
110	
111	$$\hat{r}_t = \frac{1}{N} \sum_{i=1}^N r_\psi(\text{Yes} \mid s_t, a_t, v_{1:t-1}^i, f_{1:t-1}^i, v_t^i, f_t^i). \quad (7)$$
112	
113	Then the rewards can be used for ranking the responses of policy models or be converted into binary labels through a threshold 0.5 for judging the correctness of the step. The discussion of using code verification can be found at Table 5.
114	
115	## 3.2. Synthesizing Data of GenPRM
116	
117	In this section, we introduce our pipeline for synthesizing training data of GenPRM. The pipeline consists of three stages: (1) generating reasoning paths and obtaining PRM labels via Monte Carlo (MC) estimation; (2) evaluating the progress of each step via Relative Progress Estimation; and (3) synthesizing rationales with CoT and code verification, and inferring LLM-as-a-judge labels with consensus filtering.
118	
119	### 3.2.1. Solution Generation and Monte Carlo Estimation
120	
121	**Solution Generation with Step Forcing.** We utilize the 7.5K problems from the training set of the MATH dataset (Hendrycks et al., 2021) as the problem set. For each problem, we use Qwen2.5-7B-Instruct (Yang et al., 2024a) as the generation model to collect multiple solutions. Since using “\n\n” for step division does not consider the semantics of each step and may result in overly fine-grained division, we apply a step forcing approach to generate solutions. Specifically, we add “Step 1:” as the prefix for the generation model to complete the response. For a response with  $T$  reasoning steps, the format is as follows:### The response format with step forcing
122	
123	Step 1: {step content}
124	
125	...
126	
127	Step T: {step content}
128	
129	The proportion of correct paths versus incorrect paths varies significantly depending on the difficulty of the problems. To ensure a sufficient number of correct and incorrect paths, we sample up to 2048 paths for both hard and easy problems. If no correct or incorrect paths are found after sampling 2048 responses, we discard the corresponding problems.
130	
131	**Balancing the Precision and Efficiency of MC Estimation.** Following Math-Shepherd (Wang et al., 2024b), we estimate the probability of correctness for each step using completion-based sampling. For each reasoning step  $s_t$ , we generate  $K$  completion trajectories using a completion model, specifically Qwen2.5-Math-7B-Instruct (Yang et al., 2024b), and use MC estimation to calculate the probability that the current step  $a_t$  is correct (Wang et al., 2024b; Zhang et al., 2025c):
132	
133	$$MC(s_t, a_t) = MC(s_{t+1}) = \frac{1}{K} \sum_{j=1}^K \mathbb{1}(q_j = q^*), \quad (8)$$
134	
135	where  $q_j$  is the answer of the  $j$ -th response,  $q^*$  is the ground-truth answer, and  $\mathbb{1}$  is the indicator function. However, it is difficult for the completion model to reach the correct answer for hard problems even when the original step is correct, leading to incorrect results for MC estimation. To address this and balance the computation cost, we use a dynamic  $K$  based on the estimated Pass@1  $MC(s_1)$ :
136	
137	$$K = \begin{cases} 128 & \text{if } 0 \leq MC(s_1) < 0.1, \\ 64 & \text{if } 0.1 \leq MC(s_1) < 0.9, \\ 32 & \text{if } 0.9 \leq MC(s_1) < 1. \end{cases} \quad (9)$$
138	
139	### 3.2.2. Relative Progress Estimation
140	
141	Previous work has shown that hard label estimation is better than soft label estimation for PRMs (Zhang et al., 2025c). However, after MC estimation, we observe that although the MC score of many steps is greater than 0, the steps are incorrect, as also noted by Zhang et al. (2025c). On the other hand, we assume that a positive step should be both correct and beneficial. A reasoning step is considered as a beneficial one if it is easier to reach the correct answer by adding this step as the generation prefix. To address these issues, we propose Relative Progress Estimation (RPE), which shares a similar idea with relative advantage estimation in GRPO (Shao et al., 2024; DeepSeek-AI et al., 2025), to improve conventional hard label estimation.
142	
143	Specifically, the MC score is an empirical estimation of the current state  $s_t$ . To evaluate the quality of the current action  $a_t$ , it is natural to compare the MC score of the next state  $s_{t+1}$  with that of the current state  $s_t$ , since  $s_{t+1} = [s_t, a_t]$ . For each response, if the first erroneous step is step  $t'$  (i.e.,  $MC(s_{t'}) = 0$ ), we set the MC score of the following steps to 0. Our RPE  $P_t$  for step  $t$  is defined as follows:
144	
145	$$P_t = \frac{MC(s_t, a_t)}{MC(s_t)}, \quad (10)$$
146	
147	where  $MC(s_1)$  is the estimated Pass@1 computed in the solution generation phase. However, we empirically find that using a strict criterion where progress is always greater than 1 leads to unsatisfactory performance, as shown in Table 3. To address this, we estimate the final reward label  $\hat{r}_t$  byintroducing a threshold  $\epsilon$ :
148	
149	$$\hat{r}_t = \begin{cases} 1 & \text{if } P_t \geq \epsilon, \\ 0 & \text{otherwise.} \end{cases} \quad (11)$$
150	
151	We also discuss another form of relative progress  $P_t = MC(s_t, a_t) - MC(s_t)$  in Table 3 in Section 4.4.
152	
153	### 3.2.3. Rationale Generation, Verification and Filtering
154	
155	To obtain high-quality rationale data, we use QwQ-32B (Qwen Team, 2025) as the rationale generation model and introduce a three-step pipeline that automatically generates and verifies the rationale of each reasoning step. Given a problem  $x$  with a ground-truth answer  $q^*$  and candidate steps  $\{a_1, \dots, a_T\}$ , the generation and verification proceed as follows:
156	
157	**Step 1: Code-Based Rationale Generation.** To evaluate the correctness of  $a_t$ , we synthesize step-by-step CoT analysis. It has been shown that program-based reasoning improves verification outcomes (Zhu et al., 2024). Based on CoT analysis, we continue to synthesize code-based rationales to verify  $a_t$  based on the problem and historical steps  $\{a_1, \dots, a_{t-1}\}$ . We prompt the rationale generation model to surround the CoT with `&lt;analyze>` and `&lt;/analyze>`, and the code with `&lt;verify>` and `&lt;/verify>`. The prompt for rationale generation is shown in Table A.2.
158	
159	**Step 2: Code Execution and Verification.** With the generated code, we execute it and obtain the feedback  $f_t$  for step  $t$ . The execution feedback is formatted as [Code output: {execution result}] and is concatenated to the generated CoT and code as the prefix for the subsequent generation. If the execution result is inconsistent with the generated CoT verification, we observe that QwQ-32B performs self-reflection behaviors until reaching a consensus.
160	
161	**Step 3: Label Judgment and Consensus Filtering.** After generating and verifying the rationale data of all candidate steps, the rationale generation model finally outputs a number. If all steps are inferred to be correct, the number will be -1, otherwise will be the index of the first erroneous step. For each solution, if there is at least one process label with RPE is not consistent with the labels generated by LLM-as-a-judge (Zheng et al., 2023), we discard the entire solution and only retain the one with all labels consistent. After consensus filtering, we discard approximately 51% of the data and finally obtain a dataset containing 23K problems with reasoning steps and rationale data.
162	
163	## 4. Experiments
164	
165	In this section, we aim to answer the following questions:
166	
167	- • **Q1:** How does GenPRM perform compared with previous PRMs? (§4.2, §4.3)
168	- • **Q2:** How does the performance of GenPRM scale with more test-time compute? (§4.2, §4.3)
169	- • **Q3:** How does GenPRM benefit policy model test-time scaling? (§4.3)
170	- • **Q4:** How do the components and hyperparameters influence GenPRM? (§4.4)
171	
172	### 4.1. Setup
173	
174	**Benchmarks.** We evaluate GenPRM and baseline methods on ProcessBench (Zheng et al., 2024), a benchmark designed to assess process supervision capabilities in mathematical reasoning tasks.&lt;sup>2&lt;/sup>
175	
176	&lt;sup>2&lt;/sup>Our evaluation code is adapted from &lt;https://github.com/QwenLM/ProcessBench>.Additionally, we conduct BoN and critic refinement experiments using MATH (Hendrycks et al., 2021), AMC23 (AI-MO, 2024b), AIME24 (AI-MO, 2024a), and Minerva Math (Lewkowycz et al., 2022). For BoN response generation, we employ Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) and Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as policy models. For policy model TTS with GenPRM as the critic, we use Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) and Qwen2.5-7B-Instruct (Yang et al., 2024a) as generators.
177	
178	**Baselines.** For ProcessBench and BoN experiments, we compare GenPRM with the following methods:
179	
180	- • **Math-Shepherd-PRM-7B** (Wang et al., 2024b): This method trains a PRM using hard labels computed based on MC estimation.
181	- • **RLHFlow series** (Xiong et al., 2024): Includes RLHFlow-PRM-Mistral-8B and RLHFlow-PRM-Deepseek-8B.
182	- • **Skywork-PRM series** (Skywork o1 Team, 2024): Comprises Skywork-PRM-1.5B and Skywork-PRM-7B.
183	- • **EurusPRM** (Cui et al., 2025): EurusPRM-Stage1 and EurusPRM-Stage2 are trained as implicit PRMs (Yuan et al., 2024).
184	- • **Qwen2.5-Math series** (Zheng et al., 2024; Zhang et al., 2025c): Qwen2.5-Math-7B-Math-Shepherd and Qwen2.5-Math-7B-PRM800K are trained with Math-Shepherd (Wang et al., 2024b) and PRM800K (Lightman et al., 2024), respectively. For Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B, the training data is applied consensus filtering using LLM-as-a-judge (Zheng et al., 2023).
185	- • **RetrievalPRM-7B** (Zhu et al., 2025): The method enhances PRM with retrieved questions and corresponding steps.
186	- • **Universal-PRM-7B** (Tan et al., 2025): The method proposes an automated framework using ensemble prompting and reverse verification.
187	- • **Dyve-14B** (Zhong et al., 2025): This method dynamically applies fast or slow verification for each reasoning step.
188	- • **Direct Generative PRM-7B**: The method trains a direct generative PRM with the original language head via SFT using the same data as GenPRM, but without CoT and code verification.
189	
190	For critic experiments, we use the following methods for comparison:
191	
192	- • **Self-Refine** (Madaan et al., 2023): This method uses the generator to self-critique and refine the solution.
193	- • **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI et al., 2025): This model is fine-tuned based on Qwen2.5-Math-7B (Yang et al., 2024a) using high-quality reasoning data generated by DeepSeek-R1 (DeepSeek-AI et al., 2025).
194	
195	**Implementation Details.** For RPE, we set  $\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.
196	
197	&lt;table border="1">
198	&lt;thead>
199	&lt;tr>
200	&lt;th>Model&lt;/th>
201	&lt;th># Samples&lt;/th>
202	&lt;th>GSM8K&lt;/th>
203	&lt;th>MATH&lt;/th>
204	&lt;th>Olympiad Bench&lt;/th>
205	&lt;th>Omni-MATH&lt;/th>
206	&lt;th>Avg.&lt;/th>
207	&lt;/tr>
208	&lt;/thead>
209	&lt;tbody>
210	&lt;tr>
211	&lt;td colspan="7" style="text-align: center;">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>
212	&lt;/tr>
213	&lt;tr>
214	&lt;td>GPT-4o-0806&lt;/td>
215	&lt;td>unk&lt;/td>
216	&lt;td>79.2&lt;/td>
217	&lt;td>63.6&lt;/td>
218	&lt;td>51.4&lt;/td>
219	&lt;td>53.5&lt;/td>
220	&lt;td>61.9&lt;/td>
221	&lt;/tr>
222	&lt;tr>
223	&lt;td>o1-mini&lt;/td>
224	&lt;td>unk&lt;/td>
225	&lt;td>93.2&lt;/td>
226	&lt;td>88.9&lt;/td>
227	&lt;td>87.2&lt;/td>
228	&lt;td>82.4&lt;/td>
229	&lt;td>87.9&lt;/td>
230	&lt;/tr>
231	&lt;tr>
232	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>
233	&lt;/tr>
234	&lt;tr>
235	&lt;td>Skywork-PRM-1.5B&lt;/td>
236	&lt;td>unk&lt;/td>
237	&lt;td>&lt;b>59.0&lt;/b>&lt;/td>
238	&lt;td>48.0&lt;/td>
239	&lt;td>19.3&lt;/td>
240	&lt;td>19.2&lt;/td>
241	&lt;td>36.4&lt;/td>
242	&lt;/tr>
243	&lt;tr>
244	&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>
245	&lt;td>23K&lt;/td>
246	&lt;td>52.8&lt;/td>
247	&lt;td>&lt;b>66.6&lt;/b>&lt;/td>
248	&lt;td>&lt;b>55.1&lt;/b>&lt;/td>
249	&lt;td>&lt;b>54.5&lt;/b>&lt;/td>
250	&lt;td>&lt;b>57.3&lt;/b>&lt;/td>
251	&lt;/tr>
252	&lt;tr>
253	&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>
254	&lt;td>23K&lt;/td>
255	&lt;td>51.3&lt;/td>
256	&lt;td>&lt;b>74.4&lt;/b>&lt;/td>
257	&lt;td>&lt;b>65.3&lt;/b>&lt;/td>
258	&lt;td>&lt;b>62.5&lt;/b>&lt;/td>
259	&lt;td>&lt;b>63.4&lt;/b>&lt;/td>
260	&lt;/tr>
261	&lt;tr>
262	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>
263	&lt;/tr>
264	&lt;tr>
265	&lt;td>Math-Shepherd-PRM-7B&lt;/td>
266	&lt;td>445K&lt;/td>
267	&lt;td>47.9&lt;/td>
268	&lt;td>29.5&lt;/td>
269	&lt;td>24.8&lt;/td>
270	&lt;td>23.8&lt;/td>
271	&lt;td>31.5&lt;/td>
272	&lt;/tr>
273	&lt;tr>
274	&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>
275	&lt;td>273K&lt;/td>
276	&lt;td>50.4&lt;/td>
277	&lt;td>33.4&lt;/td>
278	&lt;td>13.8&lt;/td>
279	&lt;td>15.8&lt;/td>
280	&lt;td>28.4&lt;/td>
281	&lt;/tr>
282	&lt;tr>
283	&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>
284	&lt;td>253K&lt;/td>
285	&lt;td>38.8&lt;/td>
286	&lt;td>33.8&lt;/td>
287	&lt;td>16.9&lt;/td>
288	&lt;td>16.9&lt;/td>
289	&lt;td>26.6&lt;/td>
290	&lt;/tr>
291	&lt;tr>
292	&lt;td>Skywork-PRM-7B&lt;/td>
293	&lt;td>unk&lt;/td>
294	&lt;td>70.8&lt;/td>
295	&lt;td>53.6&lt;/td>
296	&lt;td>22.9&lt;/td>
297	&lt;td>21.0&lt;/td>
298	&lt;td>42.1&lt;/td>
299	&lt;/tr>
300	&lt;tr>
301	&lt;td>EurusPRM-Stage1&lt;/td>
302	&lt;td>463K&lt;/td>
303	&lt;td>44.3&lt;/td>
304	&lt;td>35.6&lt;/td>
305	&lt;td>21.7&lt;/td>
306	&lt;td>23.1&lt;/td>
307	&lt;td>31.2&lt;/td>
308	&lt;/tr>
309	&lt;tr>
310	&lt;td>EurusPRM-Stage2&lt;/td>
311	&lt;td>30K&lt;/td>
312	&lt;td>47.3&lt;/td>
313	&lt;td>35.7&lt;/td>
314	&lt;td>21.2&lt;/td>
315	&lt;td>20.9&lt;/td>
316	&lt;td>31.3&lt;/td>
317	&lt;/tr>
318	&lt;tr>
319	&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>
320	&lt;td>445K&lt;/td>
321	&lt;td>62.5&lt;/td>
322	&lt;td>31.6&lt;/td>
323	&lt;td>13.7&lt;/td>
324	&lt;td>7.7&lt;/td>
325	&lt;td>28.9&lt;/td>
326	&lt;/tr>
327	&lt;tr>
328	&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>
329	&lt;td>264K&lt;/td>
330	&lt;td>68.2&lt;/td>
331	&lt;td>62.6&lt;/td>
332	&lt;td>50.7&lt;/td>
333	&lt;td>44.3&lt;/td>
334	&lt;td>56.5&lt;/td>
335	&lt;/tr>
336	&lt;tr>
337	&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>
338	&lt;td>~344K&lt;/td>
339	&lt;td>82.4&lt;/td>
340	&lt;td>77.6&lt;/td>
341	&lt;td>67.5&lt;/td>
342	&lt;td>66.3&lt;/td>
343	&lt;td>73.5&lt;/td>
344	&lt;/tr>
345	&lt;tr>
346	&lt;td>RetrievalPRM-7B&lt;/td>
347	&lt;td>404K&lt;/td>
348	&lt;td>74.6&lt;/td>
349	&lt;td>71.1&lt;/td>
350	&lt;td>60.2&lt;/td>
351	&lt;td>57.3&lt;/td>
352	&lt;td>65.8&lt;/td>
353	&lt;/tr>
354	&lt;tr>
355	&lt;td>Universal-PRM-7B&lt;/td>
356	&lt;td>unk&lt;/td>
357	&lt;td>&lt;b>85.8&lt;/b>&lt;/td>
358	&lt;td>77.7&lt;/td>
359	&lt;td>67.6&lt;/td>
360	&lt;td>66.4&lt;/td>
361	&lt;td>74.3&lt;/td>
362	&lt;/tr>
363	&lt;tr>
364	&lt;td>Direct Generative PRM-7B&lt;/td>
365	&lt;td>23K&lt;/td>
366	&lt;td>63.9&lt;/td>
367	&lt;td>65.8&lt;/td>
368	&lt;td>54.5&lt;/td>
369	&lt;td>55.9&lt;/td>
370	&lt;td>60.0&lt;/td>
371	&lt;/tr>
372	&lt;tr>
373	&lt;td>GenPRM-7B (Pass@1)&lt;/td>
374	&lt;td>23K&lt;/td>
375	&lt;td>78.7&lt;/td>
376	&lt;td>&lt;b>80.3&lt;/b>&lt;/td>
377	&lt;td>&lt;b>72.2&lt;/b>&lt;/td>
378	&lt;td>&lt;b>69.8&lt;/b>&lt;/td>
379	&lt;td>&lt;b>75.2&lt;/b>&lt;/td>
380	&lt;/tr>
381	&lt;tr>
382	&lt;td>GenPRM-7B (Maj@8)&lt;/td>
383	&lt;td>23K&lt;/td>
384	&lt;td>81.0&lt;/td>
385	&lt;td>&lt;b>85.7&lt;/b>&lt;/td>
386	&lt;td>&lt;b>78.4&lt;/b>&lt;/td>
387	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
388	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
389	&lt;/tr>
390	&lt;tr>
391	&lt;td colspan="7" style="text-align: center;">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>
392	&lt;/tr>
393	&lt;tr>
394	&lt;td>Dyve-14B&lt;/td>
395	&lt;td>117K&lt;/td>
396	&lt;td>68.5&lt;/td>
397	&lt;td>58.3&lt;/td>
398	&lt;td>49.0&lt;/td>
399	&lt;td>47.2&lt;/td>
400	&lt;td>55.8&lt;/td>
401	&lt;/tr>
402	&lt;tr>
403	&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>
404	&lt;td>~344K&lt;/td>
405	&lt;td>&lt;b>87.3&lt;/b>&lt;/td>
406	&lt;td>80.6&lt;/td>
407	&lt;td>74.3&lt;/td>
408	&lt;td>71.1&lt;/td>
409	&lt;td>78.3&lt;/td>
410	&lt;/tr>
411	&lt;tr>
412	&lt;td>GenPRM-32B (Pass@1)&lt;/td>
413	&lt;td>23K&lt;/td>
414	&lt;td>83.1&lt;/td>
415	&lt;td>&lt;b>81.7&lt;/b>&lt;/td>
416	&lt;td>72.8&lt;/td>
417	&lt;td>&lt;b>72.8&lt;/b>&lt;/td>
418	&lt;td>77.6&lt;/td>
419	&lt;/tr>
420	&lt;tr>
421	&lt;td>GenPRM-32B (Maj@8)&lt;/td>
422	&lt;td>23K&lt;/td>
423	&lt;td>85.1&lt;/td>
424	&lt;td>&lt;b>86.3&lt;/b>&lt;/td>
425	&lt;td>&lt;b>78.9&lt;/b>&lt;/td>
426	&lt;td>&lt;b>80.1&lt;/b>&lt;/td>
427	&lt;td>&lt;b>82.6&lt;/b>&lt;/td>
428	&lt;/tr>
429	&lt;/tbody>
430	&lt;/table>
431	
432	## 4.2. ProcessBench Results
433	
434	**GenPRM outperforms classification-based PRMs on ProcessBench.** As shown in Table 1, GenPRM-7B significantly outperforms direct generative PRM and surpasses **all** previous PRMs with parameters less than 72B on ProcessBench. Also, GenPRM-1.5B outperforms Skywork-PRM-1.5B by a large margin. It is noteworthy that GenPRM is trained with merely **23K** data from **MATH** (Hendrycks et al., 2021) only. By comparing the detailed results in Table 6, we can find that the performance gain of GenPRM mainly comes from the stronger abilities of finding **erroneous** steps and we provide concrete cases in Appendix C. These results demonstrating the superiority of generative modeling of PRM.
435	
436	**GenPRM enables smaller PRMs surpass 10 $\times$  larger PRMs and GPT-4o via TTS.** We also compare the TTS results of GenPRM in Table 1 and find that GenPRM-1.5B surpasses GPT-4 and GenPRM-7B exceeds Qwen2.5-Math-PRM-72B on ProcessBench via simply majority voting, showing that scaling test-time compute is highly effective for GenPRM. We also find that the performance improvement of scaling the test-time compute on **harder** problems is larger than that of easier questions.### 4.3. Policy Model Test-Time Scaling Results
437	
438	**GenPRM as a Verifier.** The results in Figure 4 (a)-(d) show that GenPRM outperforms the baselines on MATH, AMC23, AIME24, and Minerva Math with Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) as the generation model. The advantage of GenPRM becomes larger by scaling the test-time compute of GenPRM and the generation model. Figure 4 (e)-(h) demonstrates that GenPRM generalizes well to responses with Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as the generation model.
439	
440	**Figure 4:** BoN results with different generation models on multiple mathematical benchmarks.
441	
442	**GenPRM as a Critic.** We also conduct experiments by using GenPRM as a critic to refine the outputs of the policy model. The results in Table 2 and Figure 1 (right) show that GenPRM exhibits strong critique abilities than the baselines, significantly improving the performance of the policy model and the performance continues to increase with more refinement based on the critic feedback.
443	
444	### 4.4. Analysis
445	
446	**Label Estimation Method and Criterion.** To explore how different label estimation influences GenPRM, we conduct experiments with the following methods: (1) hard label (Wang et al., 2024b; Zhang et al., 2025c); (2) RPE in (10); and (3) a RPE variant ( $P_t = MC(s_t, a_t) - MC(s_t)$ ). For the RPE and its variant, we use different thresholds  $\epsilon$  for evaluation and set the labels as correct by checking whether  $P_t \geq \epsilon$ . The results in Table 3 show that RPE and its variant outperforms hard label estimation and RPE with  $\epsilon = 0.8$  achieves the best result. By scaling test-time compute with majority voting, the results in Table 4 demonstrate that RPE with  $\epsilon = 0.8$  still reaches the best.**Table 2:** Results of critique refinement experiments. The results of GenPRM are shaded. For each refinement turn, the highest values are **bolded**.
447	
448	&lt;table border="1">
449	&lt;thead>
450	&lt;tr>
451	&lt;th rowspan="2">Critic Model&lt;/th>
452	&lt;th colspan="5">Gemma-3-12b-it as Generator&lt;/th>
453	&lt;th colspan="5">Qwen2.5-7B-Instruct as Generator&lt;/th>
454	&lt;th rowspan="2">Avg.&lt;/th>
455	&lt;/tr>
456	&lt;tr>
457	&lt;th>AMC23&lt;/th>
458	&lt;th>AIME24&lt;/th>
459	&lt;th>MATH&lt;/th>
460	&lt;th>Minerva Math&lt;/th>
461	&lt;th>Avg.&lt;/th>
462	&lt;th>AMC23&lt;/th>
463	&lt;th>AIME24&lt;/th>
464	&lt;th>MATH&lt;/th>
465	&lt;th>Minerva Math&lt;/th>
466	&lt;th>Avg.&lt;/th>
467	&lt;/tr>
468	&lt;/thead>
469	&lt;tbody>
470	&lt;tr>
471	&lt;td>Zero-shot&lt;/td>
472	&lt;td>64.1&lt;/td>
473	&lt;td>15.8&lt;/td>
474	&lt;td>83.8&lt;/td>
475	&lt;td>31.9&lt;/td>
476	&lt;td>48.9&lt;/td>
477	&lt;td>51.6&lt;/td>
478	&lt;td>7.1&lt;/td>
479	&lt;td>76.2&lt;/td>
480	&lt;td>34.5&lt;/td>
481	&lt;td>42.4&lt;/td>
482	&lt;td>45.7&lt;/td>
483	&lt;/tr>
484	&lt;tr>
485	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 1&lt;/i>&lt;/td>
486	&lt;/tr>
487	&lt;tr>
488	&lt;td>Generator&lt;/td>
489	&lt;td>66.6&lt;/td>
490	&lt;td>15.8&lt;/td>
491	&lt;td>84.7&lt;/td>
492	&lt;td>33.3&lt;/td>
493	&lt;td>50.1&lt;/td>
494	&lt;td>50.6&lt;/td>
495	&lt;td>8.0&lt;/td>
496	&lt;td>76.8&lt;/td>
497	&lt;td>34.0&lt;/td>
498	&lt;td>42.4&lt;/td>
499	&lt;td>46.3&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5547b17-e32e-47af-97a4-6a3aca5cbfd1",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "d1fa0b6c-335b-4741-8dd7-750c5211e313",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt",
      "content": "# GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n\nJian Zhao&lt;sup>1,3\\*&lt;/sup>, Runze Liu&lt;sup>1,2\\*†&lt;/sup>, Kaiyan Zhang&lt;sup>1&lt;/sup>, Zhimu Zhou&lt;sup>3&lt;/sup>, Junqi Gao&lt;sup>4&lt;/sup>, Dong Li&lt;sup>4&lt;/sup>, Jiafei Lyu&lt;sup>1&lt;/sup>, Zhouyi Qian&lt;sup>4&lt;/sup>, Biqing Qi&lt;sup>2‡&lt;/sup>, Xiu Li&lt;sup>1‡&lt;/sup> and Bowen Zhou&lt;sup>1,2‡&lt;/sup>\n\n&lt;sup>1&lt;/sup>Tsinghua University, &lt;sup>2&lt;/sup>Shanghai AI Laboratory, &lt;sup>3&lt;/sup>BUPT, &lt;sup>4&lt;/sup>Harbin Institute of Technology\n\nRecent advancements in Large Language Models (LLMs) have shown that it is promising to utilize Process Reward Models (PRMs) as verifiers to enhance the performance of LLMs. However, current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs. In this work, we introduce GenPRM, a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. To obtain high-quality process supervision labels and rationale data, we propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification. Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only **23K** training data from **MATH** dataset. Through test-time scaling, a **1.5B** GenPRM outperforms **GPT-4o**, and a **7B** GenPRM surpasses **Qwen2.5-Math-PRM-72B** on ProcessBench. Additionally, GenPRM demonstrates strong abilities to serve as a critic model for policy model refinement. This work establishes a new paradigm for process supervision that bridges the gap between PRMs and critic models in LLMs. Our code, model, and data are available in &lt;https://ryanliu112.github.io/GenPRM>.\n\n**Figure 1: GenPRM achieves state-of-the-art performance across multiple benchmarks in two key roles: (a) As a verifier:** GenPRM-7B outperforms all classification-based PRMs of comparable size and even surpasses **Qwen2.5-Math-PRM-72B** via test-time scaling. **(b) As a critic:** GenPRM-7B demonstrates superior critique capabilities, achieving **3.4x** greater performance gains than DeepSeek-R1-Distill-Qwen-7B after 3 refinement iterations.\n\n\\* Equal contribution\n\n† Project lead & Work done during an internship at Shanghai AI Laboratory\n\n‡ Corresponding authors: Biqing Qi (qibiqing@pjlab.org.cn), Xiu Li (li.xiu@sz.tsinghua.edu.cn), and Bowen Zhou (zhoubowen@tsinghua.edu.cn)The diagram illustrates the architectural differences between classification-based PRMs and GenPRM. On the left, under the heading 'Classification-based PRM', two models are shown: 'Discriminative PRM' and 'Direct Generative PRM'. The Discriminative PRM consists of a 'value head' that outputs a score of 0.9, marked with a green checkmark. The Direct Generative PRM outputs a 'Yes' label, which is then converted to a score of 0.8, also marked with a green checkmark. On the right, under the heading 'Generative PRM (Ours)', the 'GenPRM' model is shown. It branches into three parallel paths, each consisting of a yellow circle (CoT Verification) followed by a green circle (Code Verification) and a 'Yes' or 'No' label. The top path outputs 'Yes', the middle path outputs 'No', and the bottom path outputs 'No'. These three paths converge into a final score of 0.2, which is marked with a red 'X'. A legend at the bottom identifies the yellow circle as 'CoT Verification' and the green circle as 'Code Verification'.\n\nFigure 2: Comparison between GenPRM (right) and previous classification-based PRMs (left).\n\n## 1. Introduction\n\nLarge Language Models (LLMs) have shown significant advances in recent years (OpenAI, 2023; Anthropic, 2023; OpenAI, 2024a,b; DeepSeek-AI et al., 2025). As OpenAI o1 demonstrates the great effectiveness of scaling test-time compute (OpenAI, 2024a), an increasing number of researches focus on Test-Time Scaling (TTS) methods to improve the reasoning performance of LLMs (Snell et al., 2025; Liu et al., 2025).\n\nEffective TTS requires high-quality verifiers, such as Process Reward Models (PRMs) (Liu et al., 2025). However, existing PRMs face several limitations. They exhibit limited process supervision capabilities and struggle to generalize across different models and tasks (Zheng et al., 2024; Zhang et al., 2025c; Liu et al., 2025). Furthermore, most current approaches train PRMs as classifiers that output scalar values, neglecting the natural language generation abilities of LLMs, which are pre-trained on extensive corpora. This classifier-based modeling inherently prevents PRMs from leveraging test-time scaling methods to enhance process supervision capabilities. These limitations lead us to the following research question: *How can generative modeling enhance the process supervision capabilities of PRMs while enabling test-time scaling?*\n\nIn this work, we address these challenges through a generative process reward model, named GenPRM. Specifically, GenPRM differs from classification-based PRMs in that GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought (CoT) (Wei et al., 2022) reasoning and code verification processes before providing final judgment. To improve conventional hard label estimation, we propose Relative Progress Estimation (RPE), which leverages a relative criterion for label estimation. Additionally, we introduce a rationale synthesis framework with code verification to obtain high-quality process supervision reasoning data. A comparison of our method with previous classification-based methods is presented in Figure 2.\n\nOur contributions can be summarized as follows:\n\n1. 1. We propose a generative process reward model that performs explicit CoT reasoning with code verification and utilizes Relative Progress Estimation to obtain accurate PRM labels.\n2. 2. Empirical results on ProcessBench and common mathematical reasoning tasks demonstrate that GenPRM outperforms prior classification-based PRMs. Additionally, smaller GenPRM models can surpass larger PRMs via TTS.\n3. 3. We provide a new perspective on PRMs in this work, fully leveraging their TTS capabilities, reshaping their applications, and opening new directions for future research in process supervision.## 2. Preliminaries\n\n### 2.1. Markov Decision Process\n\nFollowing [Liu et al. \\(2025\\)](#), we formulate the test-time scaling process with PRMs as a Markov Decision Process (MDP) defined by  $(\\mathcal{S}, \\mathcal{A}, P, r, \\gamma)$ , where  $\\mathcal{S}$  is the state space,  $\\mathcal{A}$  is the action space,  $P$  represents transition dynamics,  $r : \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathbb{R}$  is the reward function, and  $\\gamma \\in [0, 1]$  is the discount factor. Starting with a prompt set  $\\mathcal{X}$  and an initial state  $s_1 = x \\sim \\mathcal{X}$ , the policy model  $\\pi_\\theta$  generates an action  $a_1 \\sim \\pi_\\theta(\\cdot | s_1)$ .&lt;sup>1&lt;/sup> Unlike traditional RL methods with stochastic transitions ([Liu et al., 2022, 2024](#)), transitions in LLMs are deterministic, i.e.,  $s_{t+1} = P(\\cdot | s_t, a_t) = [s_t, a_t]$ , where  $[\\cdot, \\cdot]$  denotes string concatenation. This process continues until the episode terminates (i.e., generating the [EOS] token), obtaining a trajectory of  $T$  steps:  $\\tau = \\{a_1, a_2, \\dots, a_T\\}$ . The goal is to optimize either the reward of each step (as in search-based methods) or the reward over the full response (as in Best-of-N sampling).\n\n### 2.2. Supervised Fine-Tuning\n\nSupervised Fine-Tuning (SFT) trains a model to predict the next token based on prior context. For a dataset  $\\mathcal{D}_{\\text{SFT}} = \\{(x^{(i)}, y^{(i)})\\}_{i=1}^N$ , the SFT loss is:\n\n$$\\mathcal{L}_{\\text{SFT}}(\\theta) = -\\mathbb{E}_{(x,y) \\sim \\mathcal{D}_{\\text{SFT}}} \\left[ \\sum_{t=1}^{|y|} \\log \\pi_\\theta(y_t | x, y_{1:t-1}) \\right], \\quad (1)$$\n\nwhere  $\\pi_\\theta$  represents a model with parameters  $\\theta$ .\n\n### 2.3. Test-Time Scaling\n\nIn this work, we consider two test-time scaling methods, including majority voting and Best-of-N.\n\n**Majority Voting.** Majority voting ([Wang et al., 2023](#)) selects the answer that appears the most frequently among all solutions.\n\n**Best-of-N.** Best-of-N (BoN) ([Brown et al., 2024](#); [Snell et al., 2025](#)) selects the best answer from  $N$  candidate solutions.\n\n## 3. Method\n\nIn this section, we first describe how to develop GenPRM and integrate the reasoning process with code verification. We then introduce how to scale test-time compute of policy models using GenPRM and apply TTS for GenPRM. Last, we present the improved label estimation method and data generation and filtering framework of GenPRM.\n\n### 3.1. GenPRM and Test-Time Scaling\n\n#### 3.1.1. From Discriminative PRM to Generative PRM\n\n**Discriminative PRM.** Assume we have a PRM dataset  $\\mathcal{D}_{\\text{Disc}} = \\{(s_t, a_t), r_t\\}$ , where  $r_t \\in \\{0, 1\\}$  for PRM labels with hard estimation. The discriminative PRM  $r_\\psi$  is trained via cross-entropy loss ([Skywork](#)\n\n&lt;sup>1&lt;/sup>Following [Snell et al. \\(2025\\)](#); [Liu et al. \\(2025\\)](#), we refer to models that generate solutions as policy models.The diagram illustrates the GenPRM framework, which consists of six key parts:\n\n- **① Solution Generation & MC Reward Estimation:** A math problem is solved by generating intermediate steps (a&lt;sub>11&lt;/sub>, a&lt;sub>21&lt;/sub>, a&lt;sub>31&lt;/sub>, a&lt;sub>12&lt;/sub>, a&lt;sub>22&lt;/sub>, a&lt;sub>32&lt;/sub>). Correct steps (q&lt;sub>1&lt;/sub>, q&lt;sub>2&lt;/sub>) are marked with blue circles, and incorrect steps (q&lt;sub>3&lt;/sub>) are marked with red circles. The MC score for a step is calculated as  $MC(s_{12}, a_{12}) = \\frac{2}{3}$ .\n- **② Relative Progress Estimation:** The process reward is estimated as  $P_t = \\frac{MC(s_t, a_t)}{MC(s_t)} \\geq \\epsilon$ . If the reward is high,  $\\hat{r}_t = 1$  (green checkmark), otherwise  $\\hat{r}_t = 0$  (red X).\n- **③ Rationale Synthesis:** A problem is analyzed using CoT (Chain of Thought) analysis to generate a rationale. This rationale is then verified using code verification (e.g., Python code) to check for potential errors. The final label is a judgement of Yes/No.\n- **④ GenPRM Training:** Data (23K) is used for SFT (Supervised Fine-Tuning) to train GenPRM. Consensus filtering is applied to the training data.\n- **⑤ Policy Model Test-Time Scaling:** The trained GenPRM functions as a verifier or critic. It can be used to verify a solution (GenPRM as a Verifier) or critique a solution (GenPRM as a Critic).\n- **⑥ GenPRM Test-Time Scaling:** The performance of GenPRM is improved through test-time scaling. Multiple steps are analyzed and verified, and their rewards are aggregated to produce a final reward  $r$ .\n\nLegend:\n\n- a Intermediate Step\n- q Correct Answer\n- q Incorrect Answer\n- r Single Reward Judgement\n- r Aggregated Reward Judgement\n\n**Figure 3: Overall framework of GenPRM.** Our framework consists of six key parts: ① The policy model generates solution steps, with MC scores estimated from rollout trajectories. ② Our proposed RPE derives accurate PRM labels. ③ High-quality process supervision data is synthesized through CoT reasoning augmented with code verification. ④ We apply consensus filtering followed by SFT to train GenPRM. ⑤ The trained GenPRM functions as a verifier or critic, enabling enhanced test-time scaling for policy models. ⑥ The performance of GenPRM further improves through test-time scaling.\n\no1 Team, 2024; Zhang et al., 2025c):\n\n$$\\mathcal{L}_{CE}(\\psi) = -\\mathbb{E}_{(s_t, a_t, r_t) \\sim \\mathcal{D}_{Disc}} [r_t \\log r_\\psi(s_t, a_t) + (1 - r_t) \\log(1 - r_\\psi(s_t, a_t))]. \\quad (2)$$\n\n**Direct Generative PRM.** With a dataset  $\\mathcal{D}_{Direct-Gen} = \\{(s_t, a_t), r_t\\}$ , where  $r_t$  is Yes for a correct step and No otherwise, the direct generative PRM (Xiong et al., 2024) is trained through SFT to predict Yes or No for each step. For step  $t$ , we use the probability of the Yes token as the predicted process reward  $\\hat{r}_t$ :\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t). \\quad (3)$$\n\n**Generative PRM.** By equipping the direct generative PRM with an explicit reasoning process like CoT (Wei et al., 2022), we obtain a generative PRM. Let  $v_{1:t-1}$  denote the rationale from step 1 to  $t-1$  and  $v_t$  denote the rationale for step  $t$ . Assume we have a dataset  $\\mathcal{D}_{Gen} = \\{(s_t, a_t, v_{1:t-1}), (v_t, r_t)\\}$ . GenPRM learns to reason and verify each step via SFT on this dataset. The generative process reward  $\\hat{r}_t$  can be obtained via the following equation:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, v_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}) \\quad (4)$$\n\n**Generative PRM with Code Verification.** If we only verify the reasoning step with CoT based on natural language, the process may lack robustness in certain complex scenarios (Zhu et al., 2024; Gou et al., 2024). The difference between the generative PRM and the generative PRM with code verification is that the latter generates code to verify the reasoning step by executing it and provides the judgment based on the execution results. At step  $t$ , after generating the rationale  $v_t$  containing CoT and code, we execute the code and obtain feedback  $f_t$ . Given the current state  $s_t$ , action  $a_t$ , previous rationales  $v_{1:t-1}$ , and previous corresponding execution feedback  $f_{1:t-1}$ , the PRM first generates therationale  $v_t$ . After execution and obtaining the feedback  $f_t$ , we compute the final generative process reward as follows:\n\n$$\\hat{r}_t = r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}, v_t, f_t), \\quad \\text{where } v_t \\sim r_\\psi(\\cdot \\mid s_t, a_t, v_{1:t-1}, f_{1:t-1}) \\quad (5)$$\n\nIn the following sections, we refer to GenPRM as this generative PRM type with code verification. The effectiveness of CoT and code verification can be found in Section 4.4.\n\n### 3.1.2. Test-Time Scaling\n\n**Policy Model TTS: GenPRM as a Verifier.** To scale the test-time compute of policy models, we can sample multiple responses from policy models and then use GenPRM as a verifier to select the final answer (Snell et al., 2025) in the way of parallel TTS.\n\n**Policy Model TTS: GenPRM as a Critic.** By equipping the PRM with generative process supervision abilities, GenPRM can be naturally used as a critic model to refine the outputs of policy models and we can scale the refinement process with multiple turns in a sequential TTS manner.\n\n**GenPRM TTS.** When evaluating each solution step, we first sample  $N$  reasoning verification paths and then use majority voting to obtain the final prediction by averaging the rewards. For GenPRM without code verification, the rewards are computed as follows:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, v_t^i). \\quad (6)$$\n\nAnd we can further incorporate code verification and execution feedback into this reasoning process:\n\n$$\\hat{r}_t = \\frac{1}{N} \\sum_{i=1}^N r_\\psi(\\text{Yes} \\mid s_t, a_t, v_{1:t-1}^i, f_{1:t-1}^i, v_t^i, f_t^i). \\quad (7)$$\n\nThen the rewards can be used for ranking the responses of policy models or be converted into binary labels through a threshold 0.5 for judging the correctness of the step. The discussion of using code verification can be found at Table 5.\n\n## 3.2. Synthesizing Data of GenPRM\n\nIn this section, we introduce our pipeline for synthesizing training data of GenPRM. The pipeline consists of three stages: (1) generating reasoning paths and obtaining PRM labels via Monte Carlo (MC) estimation; (2) evaluating the progress of each step via Relative Progress Estimation; and (3) synthesizing rationales with CoT and code verification, and inferring LLM-as-a-judge labels with consensus filtering.\n\n### 3.2.1. Solution Generation and Monte Carlo Estimation\n\n**Solution Generation with Step Forcing.** We utilize the 7.5K problems from the training set of the MATH dataset (Hendrycks et al., 2021) as the problem set. For each problem, we use Qwen2.5-7B-Instruct (Yang et al., 2024a) as the generation model to collect multiple solutions. Since using “\\n\\n” for step division does not consider the semantics of each step and may result in overly fine-grained division, we apply a step forcing approach to generate solutions. Specifically, we add “Step 1:” as the prefix for the generation model to complete the response. For a response with  $T$  reasoning steps, the format is as follows:### The response format with step forcing\n\nStep 1: {step content}\n\n...\n\nStep T: {step content}\n\nThe proportion of correct paths versus incorrect paths varies significantly depending on the difficulty of the problems. To ensure a sufficient number of correct and incorrect paths, we sample up to 2048 paths for both hard and easy problems. If no correct or incorrect paths are found after sampling 2048 responses, we discard the corresponding problems.\n\n**Balancing the Precision and Efficiency of MC Estimation.** Following Math-Shepherd (Wang et al., 2024b), we estimate the probability of correctness for each step using completion-based sampling. For each reasoning step  $s_t$ , we generate  $K$  completion trajectories using a completion model, specifically Qwen2.5-Math-7B-Instruct (Yang et al., 2024b), and use MC estimation to calculate the probability that the current step  $a_t$  is correct (Wang et al., 2024b; Zhang et al., 2025c):\n\n$$MC(s_t, a_t) = MC(s_{t+1}) = \\frac{1}{K} \\sum_{j=1}^K \\mathbb{1}(q_j = q^*), \\quad (8)$$\n\nwhere  $q_j$  is the answer of the  $j$ -th response,  $q^*$  is the ground-truth answer, and  $\\mathbb{1}$  is the indicator function. However, it is difficult for the completion model to reach the correct answer for hard problems even when the original step is correct, leading to incorrect results for MC estimation. To address this and balance the computation cost, we use a dynamic  $K$  based on the estimated Pass@1  $MC(s_1)$ :\n\n$$K = \\begin{cases} 128 & \\text{if } 0 \\leq MC(s_1) < 0.1, \\\\ 64 & \\text{if } 0.1 \\leq MC(s_1) < 0.9, \\\\ 32 & \\text{if } 0.9 \\leq MC(s_1) < 1. \\end{cases} \\quad (9)$$\n\n### 3.2.2. Relative Progress Estimation\n\nPrevious work has shown that hard label estimation is better than soft label estimation for PRMs (Zhang et al., 2025c). However, after MC estimation, we observe that although the MC score of many steps is greater than 0, the steps are incorrect, as also noted by Zhang et al. (2025c). On the other hand, we assume that a positive step should be both correct and beneficial. A reasoning step is considered as a beneficial one if it is easier to reach the correct answer by adding this step as the generation prefix. To address these issues, we propose Relative Progress Estimation (RPE), which shares a similar idea with relative advantage estimation in GRPO (Shao et al., 2024; DeepSeek-AI et al., 2025), to improve conventional hard label estimation.\n\nSpecifically, the MC score is an empirical estimation of the current state  $s_t$ . To evaluate the quality of the current action  $a_t$ , it is natural to compare the MC score of the next state  $s_{t+1}$  with that of the current state  $s_t$ , since  $s_{t+1} = [s_t, a_t]$ . For each response, if the first erroneous step is step  $t'$  (i.e.,  $MC(s_{t'}) = 0$ ), we set the MC score of the following steps to 0. Our RPE  $P_t$  for step  $t$  is defined as follows:\n\n$$P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}, \\quad (10)$$\n\nwhere  $MC(s_1)$  is the estimated Pass@1 computed in the solution generation phase. However, we empirically find that using a strict criterion where progress is always greater than 1 leads to unsatisfactory performance, as shown in Table 3. To address this, we estimate the final reward label  $\\hat{r}_t$  byintroducing a threshold  $\\epsilon$ :\n\n$$\\hat{r}_t = \\begin{cases} 1 & \\text{if } P_t \\geq \\epsilon, \\\\ 0 & \\text{otherwise.} \\end{cases} \\quad (11)$$\n\nWe also discuss another form of relative progress  $P_t = MC(s_t, a_t) - MC(s_t)$  in Table 3 in Section 4.4.\n\n### 3.2.3. Rationale Generation, Verification and Filtering\n\nTo obtain high-quality rationale data, we use QwQ-32B (Qwen Team, 2025) as the rationale generation model and introduce a three-step pipeline that automatically generates and verifies the rationale of each reasoning step. Given a problem  $x$  with a ground-truth answer  $q^*$  and candidate steps  $\\{a_1, \\dots, a_T\\}$ , the generation and verification proceed as follows:\n\n**Step 1: Code-Based Rationale Generation.** To evaluate the correctness of  $a_t$ , we synthesize step-by-step CoT analysis. It has been shown that program-based reasoning improves verification outcomes (Zhu et al., 2024). Based on CoT analysis, we continue to synthesize code-based rationales to verify  $a_t$  based on the problem and historical steps  $\\{a_1, \\dots, a_{t-1}\\}$ . We prompt the rationale generation model to surround the CoT with `&lt;analyze>` and `&lt;/analyze>`, and the code with `&lt;verify>` and `&lt;/verify>`. The prompt for rationale generation is shown in Table A.2.\n\n**Step 2: Code Execution and Verification.** With the generated code, we execute it and obtain the feedback  $f_t$  for step  $t$ . The execution feedback is formatted as [Code output: {execution result}] and is concatenated to the generated CoT and code as the prefix for the subsequent generation. If the execution result is inconsistent with the generated CoT verification, we observe that QwQ-32B performs self-reflection behaviors until reaching a consensus.\n\n**Step 3: Label Judgment and Consensus Filtering.** After generating and verifying the rationale data of all candidate steps, the rationale generation model finally outputs a number. If all steps are inferred to be correct, the number will be -1, otherwise will be the index of the first erroneous step. For each solution, if there is at least one process label with RPE is not consistent with the labels generated by LLM-as-a-judge (Zheng et al., 2023), we discard the entire solution and only retain the one with all labels consistent. After consensus filtering, we discard approximately 51% of the data and finally obtain a dataset containing 23K problems with reasoning steps and rationale data.\n\n## 4. Experiments\n\nIn this section, we aim to answer the following questions:\n\n- • **Q1:** How does GenPRM perform compared with previous PRMs? (§4.2, §4.3)\n- • **Q2:** How does the performance of GenPRM scale with more test-time compute? (§4.2, §4.3)\n- • **Q3:** How does GenPRM benefit policy model test-time scaling? (§4.3)\n- • **Q4:** How do the components and hyperparameters influence GenPRM? (§4.4)\n\n### 4.1. Setup\n\n**Benchmarks.** We evaluate GenPRM and baseline methods on ProcessBench (Zheng et al., 2024), a benchmark designed to assess process supervision capabilities in mathematical reasoning tasks.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our evaluation code is adapted from &lt;https://github.com/QwenLM/ProcessBench>.Additionally, we conduct BoN and critic refinement experiments using MATH (Hendrycks et al., 2021), AMC23 (AI-MO, 2024b), AIME24 (AI-MO, 2024a), and Minerva Math (Lewkowycz et al., 2022). For BoN response generation, we employ Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) and Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as policy models. For policy model TTS with GenPRM as the critic, we use Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) and Qwen2.5-7B-Instruct (Yang et al., 2024a) as generators.\n\n**Baselines.** For ProcessBench and BoN experiments, we compare GenPRM with the following methods:\n\n- • **Math-Shepherd-PRM-7B** (Wang et al., 2024b): This method trains a PRM using hard labels computed based on MC estimation.\n- • **RLHFlow series** (Xiong et al., 2024): Includes RLHFlow-PRM-Mistral-8B and RLHFlow-PRM-Deepseek-8B.\n- • **Skywork-PRM series** (Skywork o1 Team, 2024): Comprises Skywork-PRM-1.5B and Skywork-PRM-7B.\n- • **EurusPRM** (Cui et al., 2025): EurusPRM-Stage1 and EurusPRM-Stage2 are trained as implicit PRMs (Yuan et al., 2024).\n- • **Qwen2.5-Math series** (Zheng et al., 2024; Zhang et al., 2025c): Qwen2.5-Math-7B-Math-Shepherd and Qwen2.5-Math-7B-PRM800K are trained with Math-Shepherd (Wang et al., 2024b) and PRM800K (Lightman et al., 2024), respectively. For Qwen2.5-Math-PRM-7B and Qwen2.5-Math-PRM-72B, the training data is applied consensus filtering using LLM-as-a-judge (Zheng et al., 2023).\n- • **RetrievalPRM-7B** (Zhu et al., 2025): The method enhances PRM with retrieved questions and corresponding steps.\n- • **Universal-PRM-7B** (Tan et al., 2025): The method proposes an automated framework using ensemble prompting and reverse verification.\n- • **Dyve-14B** (Zhong et al., 2025): This method dynamically applies fast or slow verification for each reasoning step.\n- • **Direct Generative PRM-7B**: The method trains a direct generative PRM with the original language head via SFT using the same data as GenPRM, but without CoT and code verification.\n\nFor critic experiments, we use the following methods for comparison:\n\n- • **Self-Refine** (Madaan et al., 2023): This method uses the generator to self-critique and refine the solution.\n- • **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI et al., 2025): This model is fine-tuned based on Qwen2.5-Math-7B (Yang et al., 2024a) using high-quality reasoning data generated by DeepSeek-R1 (DeepSeek-AI et al., 2025).\n\n**Implementation Details.** For RPE, we set  $\\epsilon = 0.8$  across all experiments, with ablation studies presented in Section 4.4. Rationale data is generated using QwQ-32B (Qwen Team, 2025) and the prompt template is shown in Table A.2. Our base models are from the DeepSeek-R1-Distill series (DeepSeek-AI et al., 2025), specifically the 1.5B, 7B, and 32B parameter variants. The training configuration for our method uses a batch size of 64 and a learning rate of  $2.0 \\times 10^{-6}$ . During evaluation, we employ a temperature of 0.6. For critique refinement experiments, we extract content within the `&lt;analyze>&lt;/analyze>` tags, focusing exclusively on steps predicted as negative by the policy model. The baseline methods utilize standardized prompt templates (detailed in Table A.2) to ensure consistent critique generation formats.**Table 1:** ProcessBench results reported with F1 scores. The results of GenPRM are shaded. For 1.5B PRMs, **bold** indicates the best Pass@1 or scores superior to GPT-4o. For 7-8B and 14-72B PRMs, **bold** denotes the best Pass@1 or scores superior to Qwen2.5-Math-PRM-72B.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th># Samples&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-0806&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (1.5B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-1.5B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>59.0&lt;/b>&lt;/td>\n&lt;td>48.0&lt;/td>\n&lt;td>19.3&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>36.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>&lt;b>66.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.3&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-1.5B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>51.3&lt;/td>\n&lt;td>&lt;b>74.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>65.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>63.4&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (7-8B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Math-Shepherd-PRM-7B&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>47.9&lt;/td>\n&lt;td>29.5&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>23.8&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Mistral-8B&lt;/td>\n&lt;td>273K&lt;/td>\n&lt;td>50.4&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>28.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RLHFlow-PRM-Deepseek-8B&lt;/td>\n&lt;td>253K&lt;/td>\n&lt;td>38.8&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>16.9&lt;/td>\n&lt;td>26.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Skywork-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>22.9&lt;/td>\n&lt;td>21.0&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage1&lt;/td>\n&lt;td>463K&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>35.6&lt;/td>\n&lt;td>21.7&lt;/td>\n&lt;td>23.1&lt;/td>\n&lt;td>31.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>EurusPRM-Stage2&lt;/td>\n&lt;td>30K&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>20.9&lt;/td>\n&lt;td>31.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Math-Shepherd&lt;/td>\n&lt;td>445K&lt;/td>\n&lt;td>62.5&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>13.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>28.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-PRM800K&lt;/td>\n&lt;td>264K&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>62.6&lt;/td>\n&lt;td>50.7&lt;/td>\n&lt;td>44.3&lt;/td>\n&lt;td>56.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-7B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;td>67.5&lt;/td>\n&lt;td>66.3&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>RetrievalPRM-7B&lt;/td>\n&lt;td>404K&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>60.2&lt;/td>\n&lt;td>57.3&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Universal-PRM-7B&lt;/td>\n&lt;td>unk&lt;/td>\n&lt;td>&lt;b>85.8&lt;/b>&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>66.4&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Direct Generative PRM-7B&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>72.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"7\" style=\"text-align: center;\">&lt;i>PRMs (14-72B)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Dyve-14B&lt;/td>\n&lt;td>117K&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>58.3&lt;/td>\n&lt;td>49.0&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>55.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-PRM-72B&lt;/td>\n&lt;td>~344K&lt;/td>\n&lt;td>&lt;b>87.3&lt;/b>&lt;/td>\n&lt;td>80.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>78.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Pass@1)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>83.1&lt;/td>\n&lt;td>&lt;b>81.7&lt;/b>&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>&lt;b>72.8&lt;/b>&lt;/td>\n&lt;td>77.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-32B (Maj@8)&lt;/td>\n&lt;td>23K&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>&lt;b>86.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>78.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.6&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 4.2. ProcessBench Results\n\n**GenPRM outperforms classification-based PRMs on ProcessBench.** As shown in Table 1, GenPRM-7B significantly outperforms direct generative PRM and surpasses **all** previous PRMs with parameters less than 72B on ProcessBench. Also, GenPRM-1.5B outperforms Skywork-PRM-1.5B by a large margin. It is noteworthy that GenPRM is trained with merely **23K** data from **MATH** (Hendrycks et al., 2021) only. By comparing the detailed results in Table 6, we can find that the performance gain of GenPRM mainly comes from the stronger abilities of finding **erroneous** steps and we provide concrete cases in Appendix C. These results demonstrating the superiority of generative modeling of PRM.\n\n**GenPRM enables smaller PRMs surpass 10 $\\times$  larger PRMs and GPT-4o via TTS.** We also compare the TTS results of GenPRM in Table 1 and find that GenPRM-1.5B surpasses GPT-4 and GenPRM-7B exceeds Qwen2.5-Math-PRM-72B on ProcessBench via simply majority voting, showing that scaling test-time compute is highly effective for GenPRM. We also find that the performance improvement of scaling the test-time compute on **harder** problems is larger than that of easier questions.### 4.3. Policy Model Test-Time Scaling Results\n\n**GenPRM as a Verifier.** The results in Figure 4 (a)-(d) show that GenPRM outperforms the baselines on MATH, AMC23, AIME24, and Minerva Math with Qwen2.5-Math-7B-Instruct (Yang et al., 2024b) as the generation model. The advantage of GenPRM becomes larger by scaling the test-time compute of GenPRM and the generation model. Figure 4 (e)-(h) demonstrates that GenPRM generalizes well to responses with Gemma-3-12b-it (Gemma Team and Google DeepMind, 2025) as the generation model.\n\n**Figure 4:** BoN results with different generation models on multiple mathematical benchmarks.\n\n**GenPRM as a Critic.** We also conduct experiments by using GenPRM as a critic to refine the outputs of the policy model. The results in Table 2 and Figure 1 (right) show that GenPRM exhibits strong critique abilities than the baselines, significantly improving the performance of the policy model and the performance continues to increase with more refinement based on the critic feedback.\n\n### 4.4. Analysis\n\n**Label Estimation Method and Criterion.** To explore how different label estimation influences GenPRM, we conduct experiments with the following methods: (1) hard label (Wang et al., 2024b; Zhang et al., 2025c); (2) RPE in (10); and (3) a RPE variant ( $P_t = MC(s_t, a_t) - MC(s_t)$ ). For the RPE and its variant, we use different thresholds  $\\epsilon$  for evaluation and set the labels as correct by checking whether  $P_t \\geq \\epsilon$ . The results in Table 3 show that RPE and its variant outperforms hard label estimation and RPE with  $\\epsilon = 0.8$  achieves the best result. By scaling test-time compute with majority voting, the results in Table 4 demonstrate that RPE with  $\\epsilon = 0.8$  still reaches the best.**Table 2:** Results of critique refinement experiments. The results of GenPRM are shaded. For each refinement turn, the highest values are **bolded**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Critic Model&lt;/th>\n&lt;th colspan=\"5\">Gemma-3-12b-it as Generator&lt;/th>\n&lt;th colspan=\"5\">Qwen2.5-7B-Instruct as Generator&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;th>AMC23&lt;/th>\n&lt;th>AIME24&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Minerva Math&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Zero-shot&lt;/td>\n&lt;td>64.1&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>31.9&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>7.1&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>34.5&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>45.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 1&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>15.8&lt;/td>\n&lt;td>84.7&lt;/td>\n&lt;td>33.3&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>46.3&lt;/td>",
      "numLines": 500,
      "startLine": 0,
      "totalLines": 2164
    }
  },
  "sourceToolAssistantUUID": "d5547b17-e32e-47af-97a4-6a3aca5cbfd1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-27T15:57:59.308Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ffv7GTTveqvAmSvpiiYGgm`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt",
  "limit": 500,
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1fa0b6c-335b-4741-8dd7-750c5211e313",
  "isSidechain": false,
  "requestId": "req_011CbTMCaNAx6gQDypmiv8hp",
  "type": "assistant",
  "uuid": "9577c7bb-6a33-484f-b5ca-8c3e9c91953e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzWaqbr3FpeJ57YC39u23x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 17372,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 450,
          "cache_read_input_tokens": 17372,
          "cache_creation_input_tokens": 246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 246
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

_source line 42 · 2026-05-27T15:58:00.367Z_

<details><summary>↩ Tool result · `toolu_015JG8FJ33Wt6o1onWjJ9hee`</summary>

`````text
1000	Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, 2024b.
1001	
1002	Weiyun Wang, Zhangwei Gao, Lianjie Chen, Chen Zhe, Jinguo Zhu, Xiangyu Zhao, Yangzhou Liu, Yue Cao, Shenglong Ye, Xizhou Zhu, Lewei Lu, Haodong Duan, Yu Qiao, Jifeng Dai, and Wenhai Wang. VisualPRM: An Effective Process Reward Model for Multimodal Reasoning. *arXiv preprint arXiv:2503.10291*, 2025.
1003	
1004	Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. In *International Conference on Learning Representations (ICLR)*, 2023. URL &lt;https://openreview.net/forum?id=1PL1NIMMrw>.
1005	
1006	Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in neural information processing systems (NeurIPS)*, volume 35, pages 24824–24837, 2022.Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=VNckp7JEHn>.
1007	
1008	Zhihui Xie, Liyu Chen, Weichao Mao, Jingjing Xu, Lingpeng Kong, et al. Teaching Language Models to Critique via Reinforcement Learning. *arXiv preprint arXiv:2502.03492*, 2025.
1009	
1010	Wei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An Implementation of Generative PRM. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024.
1011	
1012	An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*, 2024a.
1013	
1014	An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement. *arXiv preprint arXiv:2409.12122*, 2024b.
1015	
1016	Rui Yang, Ruomeng Ding, Yong Lin, Huan Zhang, and Tong Zhang. Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024c. URL &lt;https://openreview.net/forum?id=jwh9MHEfmY>.
1017	
1018	Lifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free Process Rewards without Process Labels. *arXiv preprint arXiv:2412.01981*, 2024.
1019	
1020	Thomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjiae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, et al. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data. *arXiv preprint arXiv:2502.06737*, 2025.
1021	
1022	Hanning Zhang, Pengcheng Wang, Shizhe Diao, Yong Lin, Rui Pan, Hanze Dong, Dylan Zhang, Pavlo Molchanov, and Tong Zhang. Entropy-Regularized Process Reward Model. *arXiv preprint arXiv:2412.11006*, 2024a.
1023	
1024	Kaiyan Zhang, Jiayuan Zhang, Haoxin Li, Xuekai Zhu, Ermo Hua, Xingtai Lv, Ning Ding, Biqing Qi, and Bowen Zhou. OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees. In *International Conference on Learning Representations (ICLR)*, 2025a. URL &lt;https://openreview.net/forum?id=fGIqGfmgkW>.
1025	
1026	Lunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative Verifiers: Reward Modeling as Next-Token Prediction. In *International Conference on Learning Representations (ICLR)*, 2025b. URL &lt;https://openreview.net/forum?id=Ccwp4tFETe>.
1027	
1028	Yuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang. o1-Coder: an o1 Replication for Coding. *arXiv preprint arXiv:2412.00154*, 2024b.
1029	
1030	Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The Lessons of Developing Process Reward Models in Mathematical Reasoning. *arXiv preprint arXiv:2501.07301*, 2025c.Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. ProcessBench: Identifying Process Errors in Mathematical Reasoning. *arXiv preprint arXiv:2412.06559*, 2024.
1031	
1032	Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46595–46623. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets\\_and\\_Benchmarks.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf).
1033	
1034	Jianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, and Qiang Xu. Dyve: Thinking Fast and Slow for Dynamic Process Verification. *arXiv preprint arXiv:2502.11157*, 2025.
1035	
1036	Jiachen Zhu, Congmin Zheng, Jianghao Lin, Kounianhua Du, Ying Wen, Yong Yu, Jun Wang, and Weinan Zhang. Retrieval-Augmented Process Reward Model for Generalizable Mathematical Reasoning. *arXiv preprint arXiv:2502.14361*, 2025.
1037	
1038	Xuekai Zhu, Biqing Qi, Kaiyan Zhang, Xinwei Long, Zhouhan Lin, and Bowen Zhou. PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning. In Kevin Duh, Helena Gomez, and Steven Bethard, editors, *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 2571–2597, Mexico City, Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.142. URL &lt;https://aclanthology.org/2024.naacl-long.142/>.## A. Experimental Details
1039	
1040	### A.1. Scoring and Voting Methods
1041	
1042	**PRM-Last.** PRM-Last considers the process reward of the last step of the entire LLM response as the final score, i.e.,  $\text{score} = r_T$ .
1043	
1044	**PRM-Avg.** PRM-Avg computes the mean process reward across all steps as the final score, i.e.,  $\text{score} = \frac{1}{T} \sum_{t=1}^T r_t$ .
1045	
1046	**PRM-Min.** PRM-Min uses the minimum process reward across all steps as the final score, i.e.,  $\text{score} = \min_r \{r_t\}_{t=1}^T$ .
1047	
1048	### A.2. Implementation Details
1049	
1050	Prompt for CoT and code rationale generation is shown in Table A.2.
1051	
1052	#### Prompt for CoT and code rationale generation
1053	
1054	**[System]:**
1055	
1056	You are a math teacher. Your task is to review and critique the paragraphs in solution step by step with python code.
1057	
1058	**[User]:**
1059	
1060	The following is the math problem and a solution (split into paragraphs, enclosed with tags and indexed from 1):
1061	
1062	[Math Problem]
1063	
1064	{problem}
1065	
1066	[Solution]
1067	
1068	```
1069	&lt;paragraph_1>
1070	{solution_section_1}
1071	&lt;/paragraph_1>
1072	```
1073	
1074	...
1075	
1076	```
1077	&lt;paragraph_n>
1078	{solution_section_n}
1079	&lt;/paragraph_n>
1080	```
1081	
1082	Your task is to verify the correctness of paragraph in the solution. Split your verification by ‘### Paragraph {{ID}}’.
1083	
1084	Your verification for each paragraph should be constructed by 2 parts, wrapped by ‘&lt;analyze>&lt;/analyze>’ and ‘&lt;verify>&lt;/verify>’ separately.1. 1. In ‘`&lt;analyze>&lt;/analyze>`’ part, you need to analyze the reasoning process and explain why the paragraph is correct or incorrect in detail.
1085	2. 2. In ‘`&lt;verify>&lt;/verify>`’ part, you must write **Python code** in the form of ‘````python\n{CODE}\n````’ to verify every details that can be verified by code. You can import PyPI (i.e., ‘`sympy`’, ‘`scipy`’ and so on) to implement complicated calculation. Make sure to print the critic results in the code. Every code will be executed automatically by system. You need to analyze the ‘[Code Output]’ after code executing.
1086	
1087	>Pay attention that you must follow the format of ‘````python\n{CODE}\n````’ when you write the code, otherwise the code will not be executed.
1088	
1089	After all verifications, if you identify an error in a paragraph, return the **index** of the paragraph where the earliest error occurs\*\*. Otherwise, return the **index** of -1 (which typically denotes "not found"\*\*. Please put your final answer (i.e., the index) within box in the form of ‘`$\boxed{{INDEX}}$`’.
1090	
1091	Following [Zheng et al. \(2024\)](#); [Zhang et al. \(2025c\)](#), we use the prompt in Table A.2 to evaluate LLM-as-a-judge methods on ProcessBench ([Zheng et al., 2024](#)).
1092	
1093	#### Evaluation prompt for LLM-as-a-judge methods on ProcessBench
1094	
1095	I will provide a math problem along with a solution. They will be formatted as follows:
1096	
1097	[Math Problem]
1098	
1099	```
1100	&lt;math_problem>
1101	...(math problem)...
1102	&lt;/math_problem>
1103	```
1104	
1105	[Solution]
1106	
1107	```
1108	&lt;paragraph_1>
1109	...(paragraph 1 of solution)...
1110	&lt;/paragraph_1>
1111	```
1112	
1113	...
1114	
1115	```
1116	&lt;paragraph_n>
1117	...(paragraph n of solution)...
1118	&lt;/paragraph_n>
1119	```
1120	
1121	Your task is to review each paragraph of the solution in sequence, analyzing, verifying, and critiquing the reasoning in detail. You need to provide the analyses and the conclusion in the following format:
1122	
1123	```
1124	&lt;analysis_1>
1125	...(analysis of paragraph 1)...
1126	&lt;/analysis_1>
1127	```...
1128	
1129	&lt;analysis\_n>  
1130	 ...(analysis of paragraph n)...  
1131	 &lt;/analysis\_n>
1132	
1133	&lt;conclusion>  
1134	 Correct/Incorrect  
1135	 &lt;/conclusion>
1136	
1137	\* When you analyze each paragraph, you should use proper verification, recalculation, or reflection to indicate whether it is logically and mathematically valid. Please elaborate on the analysis process carefully.
1138	
1139	\* If an error is detected in any paragraph, you should describe the nature and cause of the error in detail, and suggest how to correct the error or the correct approach. Once a paragraph is found to contain any error, stop further analysis of subsequent paragraphs (as they may depend on the identified error) and directly provide the conclusion of "Incorrect."
1140	
1141	For instance, given a solution of five paragraphs, if an error is found in the third paragraph, you should reply in the following format:
1142	
1143	&lt;analysis\_1>  
1144	 ...(analysis of paragraph 1)...  
1145	 &lt;/analysis\_1>
1146	
1147	&lt;analysis\_2>  
1148	 ...(analysis of paragraph 2)...  
1149	 &lt;/analysis\_2>
1150	
1151	&lt;analysis\_3>  
1152	 ...(analysis of paragraph 3; since an error is found here, also provide detailed critique and correction guideline)...  
1153	 &lt;/analysis\_3>
1154	
1155	&lt;conclusion>  
1156	 Incorrect  
1157	 &lt;/conclusion>
1158	
1159	Note that the analyses of paragraphs 4 and 5 should be skipped as the paragraph 3 has been found to contain an error.
1160	
1161	\* Respond with your analyses and conclusion directly.
1162	
1163	---
1164	
1165	The following is the math problem and the solution for you task:[Math Problem]
1166	
1167	{tagged\_problem}
1168	
1169	[Solution]
1170	
1171	{tagged\_response}
1172	
1173	#### Prompt for critique generation
1174	
1175	[User]:
1176	
1177	The following is a math problem and my solution. Your task is to review and critique the paragraphs in solution step by step. Pay attention that you should not solve the problem and give the final answer. All of your task is to critique. Output your judgement of whether the paragraph is correct in the form of ‘ $\boxed{\{Yes|No\}}$ ’ at the end of each paragraph verification:
1178	
1179	[Math Problem]
1180	
1181	{problem}
1182	
1183	[Solution]
1184	
1185	&lt;paragraph\_{idx}>
1186	
1187	{solution\_section}
1188	
1189	&lt;/paragraph\_{idx}>
1190	
1191	## B. Additional Results
1192	
1193	We provide full results of ProcessBench in Table 6.
1194	
1195	**Model Size.** We investigate the impact of model size on GenPRM by evaluating variants with 1.5B, 7B, and 32B parameters. As shown in Table 7, scaling the model from 1.5B to 7B parameters yields substantial performance gains (57.3  $\rightarrow$  75.2 and 63.4  $\rightarrow$  80.5). However, further increasing the model size to 32B provides only marginal improvements, suggesting that the 7B variant offers the best balance between efficiency and effectiveness.
1196	
1197	**Data Size.** To assess the influence of training data volume, we train GenPRM on progressively larger subsets of ProcessBench (25%, 50%, and 100% of the full dataset). Table 8 demonstrates that Pass@1 F1 scores improve rapidly with initial data increases, but the growth rate slows substantially with additional data.
1198	
1199	**Inference Tokens.** We provide statistics of the reasoning tokens per step and per response in Table 9.**Table 6:** Full results of critic models and PRMs on ProcessBench.
1200	
1201	&lt;table border="1">
1202	&lt;thead>
1203	&lt;tr>
1204	&lt;th rowspan="2">Model&lt;/th>
1205	&lt;th colspan="3">GSM8K&lt;/th>
1206	&lt;th colspan="3">MATH&lt;/th>
1207	&lt;th colspan="3">OlympiadBench&lt;/th>
1208	&lt;th colspan="3">Omni-MATH&lt;/th>
1209	&lt;th rowspan="2">Avg.&lt;br/>F1&lt;/th>
1210	&lt;/tr>
1211	&lt;tr>
1212	&lt;th>Err.&lt;/th>
1213	&lt;th>Corr.&lt;/th>
1214	&lt;th>F1&lt;/th>
1215	&lt;th>Err.&lt;/th>
1216	&lt;th>Corr.&lt;/th>
1217	&lt;th>F1&lt;/th>
1218	&lt;th>Err.&lt;/th>
1219	&lt;th>Corr.&lt;/th>
1220	&lt;th>F1&lt;/th>
1221	&lt;th>Err.&lt;/th>
1222	&lt;th>Corr.&lt;/th>
1223	&lt;th>F1&lt;/th>
1224	&lt;/tr>
1225	&lt;/thead>
1226	&lt;tbody>
1227	&lt;tr>
1228	&lt;td colspan="14" style="text-align: center;">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>
1229	&lt;/tr>
1230	&lt;tr>
1231	&lt;td>GPT-4-0806&lt;/td>
1232	&lt;td>70.0&lt;/td>
1233	&lt;td>91.2&lt;/td>
1234	&lt;td>79.2&lt;/td>
1235	&lt;td>54.4&lt;/td>
1236	&lt;td>76.6&lt;/td>
1237	&lt;td>63.6&lt;/td>
1238	&lt;td>45.8&lt;/td>
1239	&lt;td>58.4&lt;/td>
1240	&lt;td>51.4&lt;/td>
1241	&lt;td>45.2&lt;/td>
1242	&lt;td>65.6&lt;/td>
1243	&lt;td>53.5&lt;/td>
1244	&lt;td>61.9&lt;/td>
1245	&lt;/tr>
1246	&lt;tr>
1247	&lt;td>o1-mini&lt;/td>
1248	&lt;td>88.9&lt;/td>
1249	&lt;td>97.9&lt;/td>
1250	&lt;td>93.2&lt;/td>
1251	&lt;td>83.5&lt;/td>
1252	&lt;td>95.1&lt;/td>
1253	&lt;td>88.9&lt;/td>
1254	&lt;td>80.2&lt;/td>
1255	&lt;td>95.6&lt;/td>
1256	&lt;td>87.2&lt;/td>
1257	&lt;td>74.8&lt;/td>
1258	&lt;td>91.7&lt;/td>
1259	&lt;td>82.4&lt;/td>
1260	&lt;td>87.9&lt;/td>
1261	&lt;/tr>
1262	&lt;tr>
1263	&lt;td colspan="14" style="text-align: center;">&lt;i>Open-Source LLMs (Critic)&lt;/i>&lt;/td>
1264	&lt;/tr>
1265	&lt;tr>
1266	&lt;td>Llama-3-8B-Instruct&lt;/td>
1267	&lt;td>42.5&lt;/td>
1268	&lt;td>7.8&lt;/td>
1269	&lt;td>13.1&lt;/td>
1270	&lt;td>28.6&lt;/td>
1271	&lt;td>9.1&lt;/td>
1272	&lt;td>13.8&lt;/td>
1273	&lt;td>27.1&lt;/td>
1274	&lt;td>2.7&lt;/td>
1275	&lt;td>4.8&lt;/td>
1276	&lt;td>26.1&lt;/td>
1277	&lt;td>8.3&lt;/td>
1278	&lt;td>12.6&lt;/td>
1279	&lt;td>11.1&lt;/td>
1280	&lt;/tr>
1281	&lt;tr>
1282	&lt;td>Llama-3-70B-Instruct&lt;/td>
1283	&lt;td>35.7&lt;/td>
1284	&lt;td>96.9&lt;/td>
1285	&lt;td>52.2&lt;/td>
1286	&lt;td>13.0&lt;/td>
1287	&lt;td>93.3&lt;/td>
1288	&lt;td>22.8&lt;/td>
1289	&lt;td>12.0&lt;/td>
1290	&lt;td>92.0&lt;/td>
1291	&lt;td>21.2&lt;/td>
1292	&lt;td>11.2&lt;/td>
1293	&lt;td>91.7&lt;/td>
1294	&lt;td>20.0&lt;/td>
1295	&lt;td>29.1&lt;/td>
1296	&lt;/tr>
1297	&lt;tr>
1298	&lt;td>Llama-3.1-8B-Instruct&lt;/td>
1299	&lt;td>44.4&lt;/td>
1300	&lt;td>6.2&lt;/td>
1301	&lt;td>10.9&lt;/td>
1302	&lt;td>41.9&lt;/td>
1303	&lt;td>2.7&lt;/td>
1304	&lt;td>5.1&lt;/td>
1305	&lt;td>32.4&lt;/td>
1306	&lt;td>1.5&lt;/td>
1307	&lt;td>2.8&lt;/td>
1308	&lt;td>32.0&lt;/td>
1309	&lt;td>0.8&lt;/td>
1310	&lt;td>1.6&lt;/td>
1311	&lt;td>5.1&lt;/td>
1312	&lt;/tr>
1313	&lt;tr>
1314	&lt;td>Llama-3.1-70B-Instruct&lt;/td>
1315	&lt;td>64.3&lt;/td>
1316	&lt;td>89.6&lt;/td>
1317	&lt;td>74.9&lt;/td>
1318	&lt;td>35.4&lt;/td>
1319	&lt;td>75.6&lt;/td>
1320	&lt;td>48.2&lt;/td>
1321	&lt;td>35.1&lt;/td>
1322	&lt;td>69.9&lt;/td>
1323	&lt;td>46.7&lt;/td>
1324	&lt;td>30.7&lt;/td>
1325	&lt;td>61.8&lt;/td>
1326	&lt;td>41.0&lt;/td>
1327	&lt;td>52.7&lt;/td>
1328	&lt;/tr>
1329	&lt;tr>
1330	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
1331	&lt;td>72.5&lt;/td>
1332	&lt;td>96.9&lt;/td>
1333	&lt;td>82.9&lt;/td>
1334	&lt;td>43.3&lt;/td>
1335	&lt;td>94.6&lt;/td>
1336	&lt;td>59.4&lt;/td>
1337	&lt;td>31.0&lt;/td>
1338	&lt;td>94.1&lt;/td>
1339	&lt;td>46.7&lt;/td>
1340	&lt;td>28.2&lt;/td>
1341	&lt;td>90.5&lt;/td>
1342	&lt;td>43.0&lt;/td>
1343	&lt;td>58.0&lt;/td>
1344	&lt;/tr>
1345	&lt;tr>
1346	&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>
1347	&lt;td>15.5&lt;/td>
1348	&lt;td>100.0&lt;/td>
1349	&lt;td>26.8&lt;/td>
1350	&lt;td>14.8&lt;/td>
1351	&lt;td>96.8&lt;/td>
1352	&lt;td>25.7&lt;/td>
1353	&lt;td>7.7&lt;/td>
1354	&lt;td>91.7&lt;/td>
1355	&lt;td>14.2&lt;/td>
1356	&lt;td>6.9&lt;/td>
1357	&lt;td>88.0&lt;/td>
1358	&lt;td>12.7&lt;/td>
1359	&lt;td>19.9&lt;/td>
1360	&lt;/tr>
1361	&lt;tr>
1362	&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>
1363	&lt;td>49.8&lt;/td>
1364	&lt;td>96.9&lt;/td>
1365	&lt;td>65.8&lt;/td>
1366	&lt;td>36.0&lt;/td>
1367	&lt;td>94.3&lt;/td>
1368	&lt;td>52.1&lt;/td>
1369	&lt;td>19.5&lt;/td>
1370	&lt;td>97.3&lt;/td>
1371	&lt;td>32.5&lt;/td>
1372	&lt;td>19.0&lt;/td>
1373	&lt;td>96.3&lt;/td>
1374	&lt;td>31.7&lt;/td>
1375	&lt;td>45.5&lt;/td>
1376	&lt;/tr>
1377	&lt;tr>
1378	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
1379	&lt;td>7.7&lt;/td>
1380	&lt;td>100.0&lt;/td>
1381	&lt;td>14.3&lt;/td>
1382	&lt;td>3.4&lt;/td>
1383	&lt;td>98.3&lt;/td>
1384	&lt;td>6.5&lt;/td>
1385	&lt;td>2.1&lt;/td>
1386	&lt;td>99.1&lt;/td>
1387	&lt;td>4.1&lt;/td>
1388	&lt;td>0.9&lt;/td>
1389	&lt;td>98.3&lt;/td>
1390	&lt;td>1.8&lt;/td>
1391	&lt;td>6.7&lt;/td>
1392	&lt;/tr>
1393	&lt;tr>
1394	&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>
1395	&lt;td>33.8&lt;/td>
1396	&lt;td>96.4&lt;/td>
1397	&lt;td>50.1&lt;/td>
1398	&lt;td>25.4&lt;/td>
1399	&lt;td>92.4&lt;/td>
1400	&lt;td>39.9&lt;/td>
1401	&lt;td>20.7&lt;/td>
1402	&lt;td>94.1&lt;/td>
1403	&lt;td>34.0&lt;/td>
1404	&lt;td>15.9&lt;/td>
1405	&lt;td>94.2&lt;/td>
1406	&lt;td>27.3&lt;/td>
1407	&lt;td>37.8&lt;/td>
1408	&lt;/tr>
1409	&lt;tr>
1410	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
1411	&lt;td>54.1&lt;/td>
1412	&lt;td>94.8&lt;/td>
1413	&lt;td>68.9&lt;/td>
1414	&lt;td>44.9&lt;/td>
1415	&lt;td>90.6&lt;/td>
1416	&lt;td>60.1&lt;/td>
1417	&lt;td>33.4&lt;/td>
1418	&lt;td>91.2&lt;/td>
1419	&lt;td>48.9&lt;/td>
1420	&lt;td>31.5&lt;/td>
1421	&lt;td>87.6&lt;/td>
1422	&lt;td>46.3&lt;/td>
1423	&lt;td>56.1&lt;/td>
1424	&lt;/tr>
1425	&lt;tr>
1426	&lt;td>Qwen2-7B-Instruct&lt;/td>
1427	&lt;td>40.6&lt;/td>
1428	&lt;td>4.7&lt;/td>
1429	&lt;td>8.4&lt;/td>
1430	&lt;td>30.5&lt;/td>
1431	&lt;td>13.8&lt;/td>
1432	&lt;td>19.0&lt;/td>
1433	&lt;td>22.4&lt;/td>
1434	&lt;td>10.9&lt;/td>
1435	&lt;td>14.7&lt;/td>
1436	&lt;td>20.0&lt;/td>
1437	&lt;td>8.7&lt;/td>
1438	&lt;td>12.1&lt;/td>
1439	&lt;td>13.6&lt;/td>
1440	&lt;/tr>
1441	&lt;tr>
1442	&lt;td>Qwen2-72B-Instruct&lt;/td>
1443	&lt;td>57.0&lt;/td>
1444	&lt;td>82.9&lt;/td>
1445	&lt;td>67.6&lt;/td>
1446	&lt;td>37.7&lt;/td>
1447	&lt;td>70.9&lt;/td>
1448	&lt;td>49.2&lt;/td>
1449	&lt;td>34.0&lt;/td>
1450	&lt;td>55.2&lt;/td>
1451	&lt;td>42.1&lt;/td>
1452	&lt;td>32.3&lt;/td>
1453	&lt;td>53.1&lt;/td>
1454	&lt;td>40.2&lt;/td>
1455	&lt;td>49.8&lt;/td>
1456	&lt;/tr>
1457	&lt;tr>
1458	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
1459	&lt;td>40.6&lt;/td>
1460	&lt;td>33.2&lt;/td>
1461	&lt;td>36.5&lt;/td>
1462	&lt;td>30.8&lt;/td>
1463	&lt;td>45.1&lt;/td>
1464	&lt;td>36.6&lt;/td>
1465	&lt;td>26.5&lt;/td>
1466	&lt;td>33.9&lt;/td>
1467	&lt;td>29.7&lt;/td>
1468	&lt;td>26.2&lt;/td>
1469	&lt;td>28.6&lt;/td>
1470	&lt;td>27.4&lt;/td>
1471	&lt;td>32.6&lt;/td>
1472	&lt;/tr>
1473	&lt;tr>
1474	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
1475	&lt;td>54.6&lt;/td>
1476	&lt;td>94.8&lt;/td>
1477	&lt;td>69.3&lt;/td>
1478	&lt;td>38.4&lt;/td>
1479	&lt;td>87.4&lt;/td>
1480	&lt;td>53.3&lt;/td>
1481	&lt;td>31.5&lt;/td>
1482	&lt;td>78.8&lt;/td>
1483	&lt;td>45.0&lt;/td>
1484	&lt;td>28.3&lt;/td>
1485	&lt;td>76.3&lt;/td>
1486	&lt;td>41.3&lt;/td>
1487	&lt;td>52.2&lt;/td>
1488	&lt;/tr>
1489	&lt;tr>
1490	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
1491	&lt;td>49.3&lt;/td>
1492	&lt;td>97.9&lt;/td>
1493	&lt;td>65.6&lt;/td>
1494	&lt;td>36.7&lt;/td>
1495	&lt;td>95.8&lt;/td>
1496	&lt;td>53.1&lt;/td>
1497	&lt;td>25.3&lt;/td>
1498	&lt;td>95.9&lt;/td>
1499	&lt;td>40.0&lt;/td>
`````

</details>

<details><summary>Recorded metadata</summary>

`````json
{
  "recorded_role": "user",
  "parentUuid": "b2fe4c50-b8d0-425a-a60f-1942b9c7e82c",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "3b1307ad-fb67-456a-be28-faa3d47995d9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt",
      "content": "Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Yu Wu, and Zhifang Sui. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 9426–9439, 2024b.\n\nWeiyun Wang, Zhangwei Gao, Lianjie Chen, Chen Zhe, Jinguo Zhu, Xiangyu Zhao, Yangzhou Liu, Yue Cao, Shenglong Ye, Xizhou Zhu, Lewei Lu, Haodong Duan, Yu Qiao, Jifeng Dai, and Wenhai Wang. VisualPRM: An Effective Process Reward Model for Multimodal Reasoning. *arXiv preprint arXiv:2503.10291*, 2025.\n\nXuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-Consistency Improves Chain of Thought Reasoning in Language Models. In *International Conference on Learning Representations (ICLR)*, 2023. URL &lt;https://openreview.net/forum?id=1PL1NIMMrw>.\n\nJason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in neural information processing systems (NeurIPS)*, volume 35, pages 24824–24837, 2022.Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=VNckp7JEHn>.\n\nZhihui Xie, Liyu Chen, Weichao Mao, Jingjing Xu, Lingpeng Kong, et al. Teaching Language Models to Critique via Reinforcement Learning. *arXiv preprint arXiv:2502.03492*, 2025.\n\nWei Xiong, Hanning Zhang, Nan Jiang, and Tong Zhang. An Implementation of Generative PRM. &lt;https://github.com/RLHFlow/RLHF-Reward-Modeling>, 2024.\n\nAn Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*, 2024a.\n\nAn Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, and Zhenru Zhang. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement. *arXiv preprint arXiv:2409.12122*, 2024b.\n\nRui Yang, Ruomeng Ding, Yong Lin, Huan Zhang, and Tong Zhang. Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs. In *Advances in Neural Information Processing Systems (NeurIPS)*, 2024c. URL &lt;https://openreview.net/forum?id=jwh9MHEfmY>.\n\nLifan Yuan, Wendi Li, Huayu Chen, Ganqu Cui, Ning Ding, Kaiyan Zhang, Bowen Zhou, Zhiyuan Liu, and Hao Peng. Free Process Rewards without Process Labels. *arXiv preprint arXiv:2412.01981*, 2024.\n\nThomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjiae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, et al. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data. *arXiv preprint arXiv:2502.06737*, 2025.\n\nHanning Zhang, Pengcheng Wang, Shizhe Diao, Yong Lin, Rui Pan, Hanze Dong, Dylan Zhang, Pavlo Molchanov, and Tong Zhang. Entropy-Regularized Process Reward Model. *arXiv preprint arXiv:2412.11006*, 2024a.\n\nKaiyan Zhang, Jiayuan Zhang, Haoxin Li, Xuekai Zhu, Ermo Hua, Xingtai Lv, Ning Ding, Biqing Qi, and Bowen Zhou. OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees. In *International Conference on Learning Representations (ICLR)*, 2025a. URL &lt;https://openreview.net/forum?id=fGIqGfmgkW>.\n\nLunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal. Generative Verifiers: Reward Modeling as Next-Token Prediction. In *International Conference on Learning Representations (ICLR)*, 2025b. URL &lt;https://openreview.net/forum?id=Ccwp4tFETe>.\n\nYuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang. o1-Coder: an o1 Replication for Coding. *arXiv preprint arXiv:2412.00154*, 2024b.\n\nZhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. The Lessons of Developing Process Reward Models in Mathematical Reasoning. *arXiv preprint arXiv:2501.07301*, 2025c.Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, and Junyang Lin. ProcessBench: Identifying Process Errors in Mathematical Reasoning. *arXiv preprint arXiv:2412.06559*, 2024.\n\nLianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46595–46623. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets\\\\_and\\\\_Benchmarks.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf).\n\nJianyuan Zhong, Zeju Li, Zhijian Xu, Xiangyu Wen, and Qiang Xu. Dyve: Thinking Fast and Slow for Dynamic Process Verification. *arXiv preprint arXiv:2502.11157*, 2025.\n\nJiachen Zhu, Congmin Zheng, Jianghao Lin, Kounianhua Du, Ying Wen, Yong Yu, Jun Wang, and Weinan Zhang. Retrieval-Augmented Process Reward Model for Generalizable Mathematical Reasoning. *arXiv preprint arXiv:2502.14361*, 2025.\n\nXuekai Zhu, Biqing Qi, Kaiyan Zhang, Xinwei Long, Zhouhan Lin, and Bowen Zhou. PaD: Program-aided Distillation Can Teach Small Models Reasoning Better than Chain-of-thought Fine-tuning. In Kevin Duh, Helena Gomez, and Steven Bethard, editors, *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pages 2571–2597, Mexico City, Mexico, June 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.naacl-long.142. URL &lt;https://aclanthology.org/2024.naacl-long.142/>.## A. Experimental Details\n\n### A.1. Scoring and Voting Methods\n\n**PRM-Last.** PRM-Last considers the process reward of the last step of the entire LLM response as the final score, i.e.,  $\\text{score} = r_T$ .\n\n**PRM-Avg.** PRM-Avg computes the mean process reward across all steps as the final score, i.e.,  $\\text{score} = \\frac{1}{T} \\sum_{t=1}^T r_t$ .\n\n**PRM-Min.** PRM-Min uses the minimum process reward across all steps as the final score, i.e.,  $\\text{score} = \\min_r \\{r_t\\}_{t=1}^T$ .\n\n### A.2. Implementation Details\n\nPrompt for CoT and code rationale generation is shown in Table A.2.\n\n#### Prompt for CoT and code rationale generation\n\n**[System]:**\n\nYou are a math teacher. Your task is to review and critique the paragraphs in solution step by step with python code.\n\n**[User]:**\n\nThe following is the math problem and a solution (split into paragraphs, enclosed with tags and indexed from 1):\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n```\n&lt;paragraph_1>\n{solution_section_1}\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n{solution_section_n}\n&lt;/paragraph_n>\n```\n\nYour task is to verify the correctness of paragraph in the solution. Split your verification by ‘### Paragraph {{ID}}’.\n\nYour verification for each paragraph should be constructed by 2 parts, wrapped by ‘&lt;analyze>&lt;/analyze>’ and ‘&lt;verify>&lt;/verify>’ separately.1. 1. In ‘`&lt;analyze>&lt;/analyze>`’ part, you need to analyze the reasoning process and explain why the paragraph is correct or incorrect in detail.\n2. 2. In ‘`&lt;verify>&lt;/verify>`’ part, you must write **Python code** in the form of ‘````python\\n{CODE}\\n````’ to verify every details that can be verified by code. You can import PyPI (i.e., ‘`sympy`’, ‘`scipy`’ and so on) to implement complicated calculation. Make sure to print the critic results in the code. Every code will be executed automatically by system. You need to analyze the ‘[Code Output]’ after code executing.\n\n>Pay attention that you must follow the format of ‘````python\\n{CODE}\\n````’ when you write the code, otherwise the code will not be executed.\n\nAfter all verifications, if you identify an error in a paragraph, return the **index** of the paragraph where the earliest error occurs\\*\\*. Otherwise, return the **index** of -1 (which typically denotes \"not found\"\\*\\*. Please put your final answer (i.e., the index) within box in the form of ‘`$\\boxed{{INDEX}}$`’.\n\nFollowing [Zheng et al. \\(2024\\)](#); [Zhang et al. \\(2025c\\)](#), we use the prompt in Table A.2 to evaluate LLM-as-a-judge methods on ProcessBench ([Zheng et al., 2024](#)).\n\n#### Evaluation prompt for LLM-as-a-judge methods on ProcessBench\n\nI will provide a math problem along with a solution. They will be formatted as follows:\n\n[Math Problem]\n\n```\n&lt;math_problem>\n...(math problem)...\n&lt;/math_problem>\n```\n\n[Solution]\n\n```\n&lt;paragraph_1>\n...(paragraph 1 of solution)...\n&lt;/paragraph_1>\n```\n\n...\n\n```\n&lt;paragraph_n>\n...(paragraph n of solution)...\n&lt;/paragraph_n>\n```\n\nYour task is to review each paragraph of the solution in sequence, analyzing, verifying, and critiquing the reasoning in detail. You need to provide the analyses and the conclusion in the following format:\n\n```\n&lt;analysis_1>\n...(analysis of paragraph 1)...\n&lt;/analysis_1>\n```...\n\n&lt;analysis\\_n>  \n ...(analysis of paragraph n)...  \n &lt;/analysis\\_n>\n\n&lt;conclusion>  \n Correct/Incorrect  \n &lt;/conclusion>\n\n\\* When you analyze each paragraph, you should use proper verification, recalculation, or reflection to indicate whether it is logically and mathematically valid. Please elaborate on the analysis process carefully.\n\n\\* If an error is detected in any paragraph, you should describe the nature and cause of the error in detail, and suggest how to correct the error or the correct approach. Once a paragraph is found to contain any error, stop further analysis of subsequent paragraphs (as they may depend on the identified error) and directly provide the conclusion of \"Incorrect.\"\n\nFor instance, given a solution of five paragraphs, if an error is found in the third paragraph, you should reply in the following format:\n\n&lt;analysis\\_1>  \n ...(analysis of paragraph 1)...  \n &lt;/analysis\\_1>\n\n&lt;analysis\\_2>  \n ...(analysis of paragraph 2)...  \n &lt;/analysis\\_2>\n\n&lt;analysis\\_3>  \n ...(analysis of paragraph 3; since an error is found here, also provide detailed critique and correction guideline)...  \n &lt;/analysis\\_3>\n\n&lt;conclusion>  \n Incorrect  \n &lt;/conclusion>\n\nNote that the analyses of paragraphs 4 and 5 should be skipped as the paragraph 3 has been found to contain an error.\n\n\\* Respond with your analyses and conclusion directly.\n\n---\n\nThe following is the math problem and the solution for you task:[Math Problem]\n\n{tagged\\_problem}\n\n[Solution]\n\n{tagged\\_response}\n\n#### Prompt for critique generation\n\n[User]:\n\nThe following is a math problem and my solution. Your task is to review and critique the paragraphs in solution step by step. Pay attention that you should not solve the problem and give the final answer. All of your task is to critique. Output your judgement of whether the paragraph is correct in the form of ‘ $\\boxed{\\{Yes|No\\}}$ ’ at the end of each paragraph verification:\n\n[Math Problem]\n\n{problem}\n\n[Solution]\n\n&lt;paragraph\\_{idx}>\n\n{solution\\_section}\n\n&lt;/paragraph\\_{idx}>\n\n## B. Additional Results\n\nWe provide full results of ProcessBench in Table 6.\n\n**Model Size.** We investigate the impact of model size on GenPRM by evaluating variants with 1.5B, 7B, and 32B parameters. As shown in Table 7, scaling the model from 1.5B to 7B parameters yields substantial performance gains (57.3  $\\rightarrow$  75.2 and 63.4  $\\rightarrow$  80.5). However, further increasing the model size to 32B provides only marginal improvements, suggesting that the 7B variant offers the best balance between efficiency and effectiveness.\n\n**Data Size.** To assess the influence of training data volume, we train GenPRM on progressively larger subsets of ProcessBench (25%, 50%, and 100% of the full dataset). Table 8 demonstrates that Pass@1 F1 scores improve rapidly with initial data increases, but the growth rate slows substantially with additional data.\n\n**Inference Tokens.** We provide statistics of the reasoning tokens per step and per response in Table 9.**Table 6:** Full results of critic models and PRMs on ProcessBench.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th rowspan=\"2\">Model&lt;/th>\n&lt;th colspan=\"3\">GSM8K&lt;/th>\n&lt;th colspan=\"3\">MATH&lt;/th>\n&lt;th colspan=\"3\">OlympiadBench&lt;/th>\n&lt;th colspan=\"3\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;br/>F1&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;th>Err.&lt;/th>\n&lt;th>Corr.&lt;/th>\n&lt;th>F1&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Proprietary LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4-0806&lt;/td>\n&lt;td>70.0&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>63.6&lt;/td>\n&lt;td>45.8&lt;/td>\n&lt;td>58.4&lt;/td>\n&lt;td>51.4&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>53.5&lt;/td>\n&lt;td>61.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>o1-mini&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>93.2&lt;/td>\n&lt;td>83.5&lt;/td>\n&lt;td>95.1&lt;/td>\n&lt;td>88.9&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>87.2&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>82.4&lt;/td>\n&lt;td>87.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"14\" style=\"text-align: center;\">&lt;i>Open-Source LLMs (Critic)&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-8B-Instruct&lt;/td>\n&lt;td>42.5&lt;/td>\n&lt;td>7.8&lt;/td>\n&lt;td>13.1&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>9.1&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>27.1&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>26.1&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>12.6&lt;/td>\n&lt;td>11.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3-70B-Instruct&lt;/td>\n&lt;td>35.7&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;td>13.0&lt;/td>\n&lt;td>93.3&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>92.0&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>11.2&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>29.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-8B-Instruct&lt;/td>\n&lt;td>44.4&lt;/td>\n&lt;td>6.2&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>41.9&lt;/td>\n&lt;td>2.7&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>1.5&lt;/td>\n&lt;td>2.8&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>0.8&lt;/td>\n&lt;td>1.6&lt;/td>\n&lt;td>5.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.1-70B-Instruct&lt;/td>\n&lt;td>64.3&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>35.4&lt;/td>\n&lt;td>75.6&lt;/td>\n&lt;td>48.2&lt;/td>\n&lt;td>35.1&lt;/td>\n&lt;td>69.9&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>30.7&lt;/td>\n&lt;td>61.8&lt;/td>\n&lt;td>41.0&lt;/td>\n&lt;td>52.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>72.5&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>43.3&lt;/td>\n&lt;td>94.6&lt;/td>\n&lt;td>59.4&lt;/td>\n&lt;td>31.0&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>46.7&lt;/td>\n&lt;td>28.2&lt;/td>\n&lt;td>90.5&lt;/td>\n&lt;td>43.0&lt;/td>\n&lt;td>58.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-7B-Instruct&lt;/td>\n&lt;td>15.5&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>26.8&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>96.8&lt;/td>\n&lt;td>25.7&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>91.7&lt;/td>\n&lt;td>14.2&lt;/td>\n&lt;td>6.9&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.7&lt;/td>\n&lt;td>19.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Math-72B-Instruct&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>96.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>36.0&lt;/td>\n&lt;td>94.3&lt;/td>\n&lt;td>52.1&lt;/td>\n&lt;td>19.5&lt;/td>\n&lt;td>97.3&lt;/td>\n&lt;td>32.5&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>96.3&lt;/td>\n&lt;td>31.7&lt;/td>\n&lt;td>45.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>7.7&lt;/td>\n&lt;td>100.0&lt;/td>\n&lt;td>14.3&lt;/td>\n&lt;td>3.4&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>6.5&lt;/td>\n&lt;td>2.1&lt;/td>\n&lt;td>99.1&lt;/td>\n&lt;td>4.1&lt;/td>\n&lt;td>0.9&lt;/td>\n&lt;td>98.3&lt;/td>\n&lt;td>1.8&lt;/td>\n&lt;td>6.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-14B-Instruct&lt;/td>\n&lt;td>33.8&lt;/td>\n&lt;td>96.4&lt;/td>\n&lt;td>50.1&lt;/td>\n&lt;td>25.4&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>39.9&lt;/td>\n&lt;td>20.7&lt;/td>\n&lt;td>94.1&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>15.9&lt;/td>\n&lt;td>94.2&lt;/td>\n&lt;td>27.3&lt;/td>\n&lt;td>37.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>54.1&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>68.9&lt;/td>\n&lt;td>44.9&lt;/td>\n&lt;td>90.6&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>91.2&lt;/td>\n&lt;td>48.9&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>87.6&lt;/td>\n&lt;td>46.3&lt;/td>\n&lt;td>56.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>4.7&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>30.5&lt;/td>\n&lt;td>13.8&lt;/td>\n&lt;td>19.0&lt;/td>\n&lt;td>22.4&lt;/td>\n&lt;td>10.9&lt;/td>\n&lt;td>14.7&lt;/td>\n&lt;td>20.0&lt;/td>\n&lt;td>8.7&lt;/td>\n&lt;td>12.1&lt;/td>\n&lt;td>13.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2-72B-Instruct&lt;/td>\n&lt;td>57.0&lt;/td>\n&lt;td>82.9&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>37.7&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>49.2&lt;/td>\n&lt;td>34.0&lt;/td>\n&lt;td>55.2&lt;/td>\n&lt;td>42.1&lt;/td>\n&lt;td>32.3&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>40.2&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>40.6&lt;/td>\n&lt;td>33.2&lt;/td>\n&lt;td>36.5&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>45.1&lt;/td>\n&lt;td>36.6&lt;/td>\n&lt;td>26.5&lt;/td>\n&lt;td>33.9&lt;/td>\n&lt;td>29.7&lt;/td>\n&lt;td>26.2&lt;/td>\n&lt;td>28.6&lt;/td>\n&lt;td>27.4&lt;/td>\n&lt;td>32.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>54.6&lt;/td>\n&lt;td>94.8&lt;/td>\n&lt;td>69.3&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>87.4&lt;/td>\n&lt;td>53.3&lt;/td>\n&lt;td>31.5&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>45.0&lt;/td>\n&lt;td>28.3&lt;/td>\n&lt;td>76.3&lt;/td>\n&lt;td>41.3&lt;/td>\n&lt;td>52.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>49.3&lt;/td>\n&lt;td>97.9&lt;/td>\n&lt;td>65.6&lt;/td>\n&lt;td>36.7&lt;/td>\n&lt;td>95.8&lt;/td>\n&lt;td>53.1&lt;/td>\n&lt;td>25.3&lt;/td>\n&lt;td>95.9&lt;/td>\n&lt;td>40.0&lt;/td>",
      "numLines": 500,
      "startLine": 1000,
      "totalLines": 2164
    }
  },
  "sourceToolAssistantUUID": "b2fe4c50-b8d0-425a-a60f-1942b9c7e82c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
`````

</details>

---

### Tool result

_source line 43 · 2026-05-27T15:57:59.316Z_

<details><summary>↩ Tool result · `toolu_01Ffv7GTTveqvAmSvpiiYGgm`</summary>

```text
500	&lt;td>46.3&lt;/td>
501	&lt;/tr>
502	&lt;tr>
503	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
504	&lt;td>69.1&lt;/td>
505	&lt;td>17.9&lt;/td>
506	&lt;td>84.6&lt;/td>
507	&lt;td>33.0&lt;/td>
508	&lt;td>51.2&lt;/td>
509	&lt;td>50.6&lt;/td>
510	&lt;td>6.3&lt;/td>
511	&lt;td>77.7&lt;/td>
512	&lt;td>34.7&lt;/td>
513	&lt;td>42.3&lt;/td>
514	&lt;td>46.8&lt;/td>
515	&lt;/tr>
516	&lt;tr>
517	&lt;td>GenPRM-7B&lt;/td>
518	&lt;td>&lt;b>74.1&lt;/b>&lt;/td>
519	&lt;td>&lt;b>19.6&lt;/b>&lt;/td>
520	&lt;td>&lt;b>86.0&lt;/b>&lt;/td>
521	&lt;td>&lt;b>35.3&lt;/b>&lt;/td>
522	&lt;td>&lt;b>53.8&lt;/b>&lt;/td>
523	&lt;td>&lt;b>57.5&lt;/b>&lt;/td>
524	&lt;td>&lt;b>8.3&lt;/b>&lt;/td>
525	&lt;td>&lt;b>80.6&lt;/b>&lt;/td>
526	&lt;td>&lt;b>36.5&lt;/b>&lt;/td>
527	&lt;td>&lt;b>45.7&lt;/b>&lt;/td>
528	&lt;td>&lt;b>49.8&lt;/b>&lt;/td>
529	&lt;/tr>
530	&lt;tr>
531	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 2&lt;/i>&lt;/td>
532	&lt;/tr>
533	&lt;tr>
534	&lt;td>Generator&lt;/td>
535	&lt;td>66.6&lt;/td>
536	&lt;td>18.0&lt;/td>
537	&lt;td>84.8&lt;/td>
538	&lt;td>31.6&lt;/td>
539	&lt;td>50.3&lt;/td>
540	&lt;td>49.8&lt;/td>
541	&lt;td>8.0&lt;/td>
542	&lt;td>76.9&lt;/td>
543	&lt;td>31.8&lt;/td>
544	&lt;td>41.6&lt;/td>
545	&lt;td>46.0&lt;/td>
546	&lt;/tr>
547	&lt;tr>
548	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
549	&lt;td>70.9&lt;/td>
550	&lt;td>18.3&lt;/td>
551	&lt;td>85.0&lt;/td>
552	&lt;td>33.5&lt;/td>
553	&lt;td>51.9&lt;/td>
554	&lt;td>51.9&lt;/td>
555	&lt;td>7.9&lt;/td>
556	&lt;td>78.1&lt;/td>
557	&lt;td>32.8&lt;/td>
558	&lt;td>42.7&lt;/td>
559	&lt;td>47.3&lt;/td>
560	&lt;/tr>
561	&lt;tr>
562	&lt;td>GenPRM-7B&lt;/td>
563	&lt;td>&lt;b>75.0&lt;/b>&lt;/td>
564	&lt;td>&lt;b>21.3&lt;/b>&lt;/td>
565	&lt;td>&lt;b>86.9&lt;/b>&lt;/td>
566	&lt;td>&lt;b>35.6&lt;/b>&lt;/td>
567	&lt;td>&lt;b>54.7&lt;/b>&lt;/td>
568	&lt;td>&lt;b>59.4&lt;/b>&lt;/td>
569	&lt;td>&lt;b>9.6&lt;/b>&lt;/td>
570	&lt;td>&lt;b>82.2&lt;/b>&lt;/td>
571	&lt;td>&lt;b>35.0&lt;/b>&lt;/td>
572	&lt;td>&lt;b>46.6&lt;/b>&lt;/td>
573	&lt;td>&lt;b>50.7&lt;/b>&lt;/td>
574	&lt;/tr>
575	&lt;tr>
576	&lt;td colspan="12" style="text-align: center;">&lt;i>Turn 3&lt;/i>&lt;/td>
577	&lt;/tr>
578	&lt;tr>
579	&lt;td>Generator&lt;/td>
580	&lt;td>67.8&lt;/td>
581	&lt;td>18.1&lt;/td>
582	&lt;td>85.0&lt;/td>
583	&lt;td>32.1&lt;/td>
584	&lt;td>50.8&lt;/td>
585	&lt;td>49.7&lt;/td>
586	&lt;td>8.1&lt;/td>
587	&lt;td>77.1&lt;/td>
588	&lt;td>30.8&lt;/td>
589	&lt;td>41.4&lt;/td>
590	&lt;td>46.1&lt;/td>
591	&lt;/tr>
592	&lt;tr>
593	&lt;td>DeepSeek-R1-Distill-7B&lt;/td>
594	&lt;td>69.6&lt;/td>
595	&lt;td>18.8&lt;/td>
596	&lt;td>85.0&lt;/td>
597	&lt;td>33.4&lt;/td>
598	&lt;td>51.7&lt;/td>
599	&lt;td>51.9&lt;/td>
600	&lt;td>8.3&lt;/td>
601	&lt;td>78.2&lt;/td>
602	&lt;td>32.7&lt;/td>
603	&lt;td>42.7&lt;/td>
604	&lt;td>47.2&lt;/td>
605	&lt;/tr>
606	&lt;tr>
607	&lt;td>GenPRM-7B&lt;/td>
608	&lt;td>&lt;b>76.2&lt;/b>&lt;/td>
609	&lt;td>&lt;b>22.8&lt;/b>&lt;/td>
610	&lt;td>&lt;b>86.7&lt;/b>&lt;/td>
611	&lt;td>&lt;b>36.0&lt;/b>&lt;/td>
612	&lt;td>&lt;b>55.4&lt;/b>&lt;/td>
613	&lt;td>&lt;b>62.7&lt;/b>&lt;/td>
614	&lt;td>&lt;b>9.3&lt;/b>&lt;/td>
615	&lt;td>&lt;b>82.9&lt;/b>&lt;/td>
616	&lt;td>&lt;b>34.9&lt;/b>&lt;/td>
617	&lt;td>&lt;b>47.5&lt;/b>&lt;/td>
618	&lt;td>&lt;b>51.5&lt;/b>&lt;/td>
619	&lt;/tr>
620	&lt;/tbody>
621	&lt;/table>
622	
623	**Table 3:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Pass@1. The best results are shown in **bold**.
624	
625	&lt;table border="1">
626	&lt;thead>
627	&lt;tr>
628	&lt;th>Estimation Method&lt;/th>
629	&lt;th>Positive Label Criterion&lt;/th>
630	&lt;th>GSM8K&lt;/th>
631	&lt;th>MATH&lt;/th>
632	&lt;th>Olympiad Bench&lt;/th>
633	&lt;th>Omni-MATH&lt;/th>
634	&lt;th>Avg.&lt;/th>
635	&lt;/tr>
636	&lt;/thead>
637	&lt;tbody>
638	&lt;tr>
639	&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>
640	&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>
641	&lt;td>72.9&lt;/td>
642	&lt;td>78.9&lt;/td>
643	&lt;td>&lt;b>73.2&lt;/b>&lt;/td>
644	&lt;td>68.0&lt;/td>
645	&lt;td>73.2&lt;/td>
646	&lt;/tr>
647	&lt;tr>
648	&lt;td rowspan="3">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>
649	&lt;td>&lt;math>P_t \geq -0.1&lt;/math>&lt;/td>
650	&lt;td>77.3&lt;/td>
651	&lt;td>79.9&lt;/td>
652	&lt;td>70.8&lt;/td>
653	&lt;td>68.5&lt;/td>
654	&lt;td>74.1&lt;/td>
655	&lt;/tr>
656	&lt;tr>
657	&lt;td>&lt;math>P_t \geq -0.3&lt;/math>&lt;/td>
658	&lt;td>76.8&lt;/td>
659	&lt;td>79.6&lt;/td>
660	&lt;td>71.1&lt;/td>
661	&lt;td>69.0&lt;/td>
662	&lt;td>74.1&lt;/td>
663	&lt;/tr>
664	&lt;tr>
665	&lt;td>&lt;math>P_t \geq -0.5&lt;/math>&lt;/td>
666	&lt;td>75.8&lt;/td>
667	&lt;td>80.2&lt;/td>
668	&lt;td>72.8&lt;/td>
669	&lt;td>68.6&lt;/td>
670	&lt;td>74.3&lt;/td>
671	&lt;/tr>
672	&lt;tr>
673	&lt;td rowspan="4">&lt;math>P_t = \frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>
674	&lt;td>&lt;math>P_t \geq 0.1&lt;/math>&lt;/td>
675	&lt;td>74.8&lt;/td>
676	&lt;td>78.7&lt;/td>
677	&lt;td>71.6&lt;/td>
678	&lt;td>68.7&lt;/td>
679	&lt;td>73.5&lt;/td>
680	&lt;/tr>
681	&lt;tr>
682	&lt;td>&lt;math>P_t \geq 0.5&lt;/math>&lt;/td>
683	&lt;td>75.7&lt;/td>
684	&lt;td>79.2&lt;/td>
685	&lt;td>70.4&lt;/td>
686	&lt;td>68.5&lt;/td>
687	&lt;td>73.5&lt;/td>
688	&lt;/tr>
689	&lt;tr>
690	&lt;td>&lt;math>P_t \geq 0.8&lt;/math>&lt;/td>
691	&lt;td>&lt;b>78.7&lt;/b>&lt;/td>
692	&lt;td>&lt;b>80.3&lt;/b>&lt;/td>
693	&lt;td>72.2&lt;/td>
694	&lt;td>&lt;b>69.8&lt;/b>&lt;/td>
695	&lt;td>&lt;b>75.2&lt;/b>&lt;/td>
696	&lt;/tr>
697	&lt;tr>
698	&lt;td>&lt;math>P_t \geq 1.0&lt;/math>&lt;/td>
699	&lt;td>76.4&lt;/td>
700	&lt;td>77.4&lt;/td>
701	&lt;td>68.1&lt;/td>
702	&lt;td>67.2&lt;/td>
703	&lt;td>72.3&lt;/td>
704	&lt;/tr>
705	&lt;/tbody>
706	&lt;/table>
707	
708	**Table 4:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Maj@8. The best results are shown in **bold**.
709	
710	&lt;table border="1">
711	&lt;thead>
712	&lt;tr>
713	&lt;th>Estimation Method&lt;/th>
714	&lt;th>Positive Label Criterion&lt;/th>
715	&lt;th>GSM8K&lt;/th>
716	&lt;th>MATH&lt;/th>
717	&lt;th>Olympiad Bench&lt;/th>
718	&lt;th>Omni-MATH&lt;/th>
719	&lt;th>Avg.&lt;/th>
720	&lt;/tr>
721	&lt;/thead>
722	&lt;tbody>
723	&lt;tr>
724	&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>
725	&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>
726	&lt;td>75.1&lt;/td>
727	&lt;td>83.8&lt;/td>
728	&lt;td>&lt;b>80.6&lt;/b>&lt;/td>
729	&lt;td>74.4&lt;/td>
730	&lt;td>78.5&lt;/td>
731	&lt;/tr>
732	&lt;tr>
733	&lt;td rowspan="3">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>
734	&lt;td>&lt;math>P_t \geq -0.1&lt;/math>&lt;/td>
735	&lt;td>79.8&lt;/td>
736	&lt;td>85.1&lt;/td>
737	&lt;td>78.0&lt;/td>
738	&lt;td>74.5&lt;/td>
739	&lt;td>79.4&lt;/td>
740	&lt;/tr>
741	&lt;tr>
742	&lt;td>&lt;math>P_t \geq -0.3&lt;/math>&lt;/td>
743	&lt;td>80.9&lt;/td>
744	&lt;td>&lt;b>86.5&lt;/b>&lt;/td>
745	&lt;td>78.1&lt;/td>
746	&lt;td>75.0&lt;/td>
747	&lt;td>80.2&lt;/td>
748	&lt;/tr>
749	&lt;tr>
750	&lt;td>&lt;math>P_t \geq -0.5&lt;/math>&lt;/td>
751	&lt;td>78.1&lt;/td>
752	&lt;td>85.6&lt;/td>
753	&lt;td>79.1&lt;/td>
754	&lt;td>73.4&lt;/td>
755	&lt;td>79.1&lt;/td>
756	&lt;/tr>
757	&lt;tr>
758	&lt;td rowspan="4">&lt;math>P_t = \frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>
759	&lt;td>&lt;math>P_t \geq 0.1&lt;/math>&lt;/td>
760	&lt;td>77.0&lt;/td>
761	&lt;td>84.6&lt;/td>
762	&lt;td>78.1&lt;/td>
763	&lt;td>75.3&lt;/td>
764	&lt;td>78.7&lt;/td>
765	&lt;/tr>
766	&lt;tr>
767	&lt;td>&lt;math>P_t \geq 0.5&lt;/math>&lt;/td>
768	&lt;td>78.0&lt;/td>
769	&lt;td>85.2&lt;/td>
770	&lt;td>78.2&lt;/td>
771	&lt;td>74.3&lt;/td>
772	&lt;td>78.9&lt;/td>
773	&lt;/tr>
774	&lt;tr>
775	&lt;td>&lt;math>P_t \geq 0.8&lt;/math>&lt;/td>
776	&lt;td>81.0&lt;/td>
777	&lt;td>85.7&lt;/td>
778	&lt;td>78.4&lt;/td>
779	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
780	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
781	&lt;/tr>
782	&lt;tr>
783	&lt;td>&lt;math>P_t \geq 1.0&lt;/math>&lt;/td>
784	&lt;td>&lt;b>81.1&lt;/b>&lt;/td>
785	&lt;td>84.1&lt;/td>
786	&lt;td>76.0&lt;/td>
787	&lt;td>74.7&lt;/td>
788	&lt;td>79.0&lt;/td>
789	&lt;/tr>
790	&lt;/tbody>
791	&lt;/table>
792	
793	**Reasoning Components.** To understand how each reasoning component influence GenPRM, we conduct experiments by training GenPRM with: (1) CoT data only, (2) code verification data only, and (3) full data. During inference phase, we also compare several variants. For example, GenPRM trained with full data can be used to only verify each step with CoT only by stopping generation at `&lt;/analyze>` token. The results in Table 5 show that: (1) the improvement of GenPRM mainly comesfrom CoT reasoning; (2) generating code and reasoning with code execution result improves the process verification performance as well.
794	
795	**Table 5:** Results on ProcessBench of GenPRM with different reasoning components, reported with Maj@8. The best results are shown in **bold**.
796	
797	&lt;table border="1">
798	&lt;thead>
799	&lt;tr>
800	&lt;th colspan="2">Training&lt;/th>
801	&lt;th colspan="3">Inference&lt;/th>
802	&lt;th rowspan="2">GSM8K&lt;/th>
803	&lt;th rowspan="2">MATH&lt;/th>
804	&lt;th rowspan="2">Olympiad Bench&lt;/th>
805	&lt;th rowspan="2">Omni-MATH&lt;/th>
806	&lt;th rowspan="2">Avg.&lt;/th>
807	&lt;/tr>
808	&lt;tr>
809	&lt;th>CoT&lt;/th>
810	&lt;th>Code&lt;/th>
811	&lt;th>CoT&lt;/th>
812	&lt;th>Code&lt;/th>
813	&lt;th>Code Exec.&lt;/th>
814	&lt;/tr>
815	&lt;/thead>
816	&lt;tbody>
817	&lt;tr>
818	&lt;td>x&lt;/td>
819	&lt;td>x&lt;/td>
820	&lt;td>x&lt;/td>
821	&lt;td>x&lt;/td>
822	&lt;td>x&lt;/td>
823	&lt;td>63.9&lt;/td>
824	&lt;td>65.8&lt;/td>
825	&lt;td>54.5&lt;/td>
826	&lt;td>55.9&lt;/td>
827	&lt;td>60.0&lt;/td>
828	&lt;/tr>
829	&lt;tr>
830	&lt;td>x&lt;/td>
831	&lt;td>✓&lt;/td>
832	&lt;td>x&lt;/td>
833	&lt;td>✓&lt;/td>
834	&lt;td>x&lt;/td>
835	&lt;td>67.0&lt;/td>
836	&lt;td>70.8&lt;/td>
837	&lt;td>61.6&lt;/td>
838	&lt;td>57.4&lt;/td>
839	&lt;td>64.2&lt;/td>
840	&lt;/tr>
841	&lt;tr>
842	&lt;td>x&lt;/td>
843	&lt;td>✓&lt;/td>
844	&lt;td>x&lt;/td>
845	&lt;td>✓&lt;/td>
846	&lt;td>✓&lt;/td>
847	&lt;td>70.6&lt;/td>
848	&lt;td>76.6&lt;/td>
849	&lt;td>67.3&lt;/td>
850	&lt;td>63.9&lt;/td>
851	&lt;td>69.6&lt;/td>
852	&lt;/tr>
853	&lt;tr>
854	&lt;td>✓&lt;/td>
855	&lt;td>x&lt;/td>
856	&lt;td>✓&lt;/td>
857	&lt;td>x&lt;/td>
858	&lt;td>x&lt;/td>
859	&lt;td>76.4&lt;/td>
860	&lt;td>83.0&lt;/td>
861	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
862	&lt;td>75.4&lt;/td>
863	&lt;td>78.8&lt;/td>
864	&lt;/tr>
865	&lt;tr>
866	&lt;td rowspan="5">✓&lt;/td>
867	&lt;td rowspan="5">✓&lt;/td>
868	&lt;td>x&lt;/td>
869	&lt;td>✓&lt;/td>
870	&lt;td>x&lt;/td>
871	&lt;td>60.1&lt;/td>
872	&lt;td>66.7&lt;/td>
873	&lt;td>59.9&lt;/td>
874	&lt;td>59.2&lt;/td>
875	&lt;td>61.5&lt;/td>
876	&lt;/tr>
877	&lt;tr>
878	&lt;td>x&lt;/td>
879	&lt;td>✓&lt;/td>
880	&lt;td>✓&lt;/td>
881	&lt;td>61.3&lt;/td>
882	&lt;td>74.7&lt;/td>
883	&lt;td>68.1&lt;/td>
884	&lt;td>62.0&lt;/td>
885	&lt;td>66.5&lt;/td>
886	&lt;/tr>
887	&lt;tr>
888	&lt;td>✓&lt;/td>
889	&lt;td>x&lt;/td>
890	&lt;td>x&lt;/td>
891	&lt;td>78.8&lt;/td>
892	&lt;td>85.1&lt;/td>
893	&lt;td>78.7&lt;/td>
894	&lt;td>74.9&lt;/td>
895	&lt;td>79.3&lt;/td>
896	&lt;/tr>
897	&lt;tr>
898	&lt;td>✓&lt;/td>
899	&lt;td>✓&lt;/td>
900	&lt;td>x&lt;/td>
901	&lt;td>&lt;b>81.0&lt;/b>&lt;/td>
902	&lt;td>85.1&lt;/td>
903	&lt;td>78.1&lt;/td>
904	&lt;td>75.5&lt;/td>
905	&lt;td>79.9&lt;/td>
906	&lt;/tr>
907	&lt;tr>
908	&lt;td>✓&lt;/td>
909	&lt;td>✓&lt;/td>
910	&lt;td>✓&lt;/td>
911	&lt;td>&lt;b>81.0&lt;/b>&lt;/td>
912	&lt;td>&lt;b>85.7&lt;/b>&lt;/td>
913	&lt;td>78.4&lt;/td>
914	&lt;td>&lt;b>76.8&lt;/b>&lt;/td>
915	&lt;td>&lt;b>80.5&lt;/b>&lt;/td>
916	&lt;/tr>
917	&lt;/tbody>
918	&lt;/table>
919	
920	## 5. Related Work
921	
922	**Process Reward Models.** Process reward models have been proved to be effective for providing step-wise scores and are superior to outcome reward models in mathematical reasoning tasks (Uesato et al., 2022; Lightman et al., 2024). However, annotating a process supervision dataset such as PRM800K (Lightman et al., 2024) requires significant human costs. To mitigate this cost, prior works utilize Monte Carlo estimation (Wang et al., 2024b) and binary search (Luo et al., 2024) for automated label generation. Subsequent research improves PRMs through methods such as advantage modeling (Setlur et al., 2025),  $Q$ -value rankings (Li and Li, 2025), implicit entropy regularization (Zhang et al., 2024a), retrieval-augmented generation (Zhu et al., 2025), and fast-slow verification (Zhong et al., 2025). Furthermore, the community has developed high-quality open-source PRMs, including the RLHFlow series (Xiong et al., 2024), Math-psa (Wang et al., 2024a), Skywork series (Skywork o1 Team, 2024), and Qwen2.5-Math series (Zheng et al., 2024; Zhang et al., 2025c). Recently, a line of works focus on extending PRMs to other tasks, including coding (Zhang et al., 2024b), medical tasks (Jiang et al., 2025), agentic tasks (Choudhury, 2025), general domain tasks (Zhang et al., 2025a; Zeng et al., 2025), and multimodal tasks (Wang et al., 2025). Current studies also focus on benchmarking PRMs (Zheng et al., 2024; Song et al., 2025) to systematically evaluate their performance.
923	
924	**Large Language Model Test-Time Scaling.** Scaling test-time computation is an effective method for improving performance during the inference phase (OpenAI, 2024a,b; DeepSeek-AI et al., 2025). TTS is commonly implemented with external verifiers (e.g., ORMs and PRMs) or strategies (e.g., beam search and MCTS) (Wu et al., 2025; Snell et al., 2025; Beeching et al., 2024; Liu et al., 2025). In this work, we scale the test-time computation of a generative PRM with an explicit reasoning process and GenPRM can also serve as a verifier or a critic model in external TTS.
925	
926	**Enhancing the Generative Abilities of Reward Models.** Previous research has investigated methods to enhance the generative capabilities of reward models using CoT reasoning (Ankner et al., 2024; Zhang et al., 2025b; Mahan et al., 2024). For instance, CCloud reward models (Ankner et al., 2024) are trained to generate critiques for responses and predict rewards using an additional rewardhead. GenRM-CoT (Zhang et al., 2025b) and GenRM (Mahan et al., 2024) train generative reward models that perform CoT reasoning before making final predictions via SFT and preference learning, respectively. CTRL (Xie et al., 2025) demonstrates that critic models exhibit strong discriminative abilities when utilized as generative reward models. Prior to these works, GRM (Yang et al., 2024c) regularizes the hidden states of reward models with a text generation loss.
927	
928	## 6. Conclusion
929	
930	In this work, we propose GenPRM, a generative process reward model that performs explicit reasoning and code verification for process supervision and enables scaling the test-time compute of PRMs. Experimental results on ProcessBench and several mathematical datasets show GenPRM outperforms prior PRMs. We also demonstrate that the performance of GenPRM increases via test-time scaling and GenPRM is effective as a critic model. We believe that this work provides perspectives on PRMs by demonstrating the strong TTS abilities of PRMs and extending the applications of PRMs.
931	
932	**Limitations.** First, GenPRM provides process supervision by generative reasoning, which introduces additional computation during inference phase. Future work will investigate how to prune the reasoning process dynamically (Zhong et al., 2025). Although GenPRM focuses mainly on mathematical reasoning tasks, it is worth to explore how to apply generative reasoning on coding and general reasoning tasks in the future (Zhang et al., 2025a). Additionally, it would be interesting to leverage RL to incentivize the generative reasoning abilities of GenPRM.
933	
934	## References
935	
936	AI-MO. AIME 2024, 2024a. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-aimo>.
937	
938	AI-MO. AMC 2023, 2024b. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-amc>.
939	
940	Zachary Ankner, Mansheej Paul, Brandon Cui, Jonathan D Chang, and Prithviraj Ammanabrolu. Critique-out-Loud Reward Models. *arXiv preprint arXiv:2408.11791*, 2024.
941	
942	Anthropic. Introducing Claude, 2023. URL &lt;https://www.anthropic.com/index/introducing-claude/>.
943	
944	Edward Beeching, Lewis Tunstall, and Sasha Rush. Scaling Test-Time Compute with Open Models, 2024. URL &lt;https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute>.
945	
946	Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. *arXiv preprint arXiv:2407.21787*, 2024.
947	
948	Sanjiban Choudhury. Process Reward Models for LLM Agents: Practical Framework and Directions. *arXiv preprint arXiv:2502.10325*, 2025.
949	
950	Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process Reinforcement through Implicit Rewards. *arXiv preprint arXiv:2502.01456*, 2025.DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv preprint arXiv:2501.12948*, 2025.
951	
952	Gemma Team and Google DeepMind. Introducing Gemma 3: The most capable model you can run on a single GPU or TPU, March 2025. URL &lt;https://blog.google/technology/developers/gemma-3>.
953	
954	Zhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen, Yujiu Yang, Nan Duan, and Weizhu Chen. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=Sx038qxjek>.
955	
956	Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset. In *Advances in Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021. URL &lt;https://openreview.net/forum?id=7Bywt2mQsCe>.
957	
958	Shuyang Jiang, Yusheng Liao, Zhe Chen, Ya Zhang, Yanfeng Wang, and Yu Wang. MedS&lt;sup>3&lt;/sup>: Towards Medical Small Language Models with Self-Evolved Slow Thinking. *arXiv preprint arXiv:2501.12051*, 2025.
959	
960	Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving Quantitative Reasoning Problems with Language Models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,*Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 3843–3857. Curran Associates, Inc., 2022. URL [https://proceedings.neurips.cc/paper\\_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf).
961	
962	Wendi Li and Yixuan Li. Process Reward Model with Q-value Rankings. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=wQEdh2cgEk>.
963	
964	Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s Verify Step by Step. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=v8L0pN6E0i>.
965	
966	Runze Liu, Fengshuo Bai, Yali Du, and Yaodong Yang. Meta-Reward-Net: Implicitly Differentiable Reward Learning for Preference-based Reinforcement Learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 22270–22284, 2022.
967	
968	Runze Liu, Yali Du, Fengshuo Bai, Jiafei Lyu, and Xiu Li. PEARL: Zero-shot Cross-task Preference Alignment and Robust Reward Learning for Robotic Manipulation. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, *International Conference on Machine Learning (ICML)*, volume 235 of *Proceedings of Machine Learning Research*, pages 30946–30964. PMLR, 21–27 Jul 2024. URL &lt;https://proceedings.mlr.press/v235/liu24o.html>.
969	
970	Runze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, and Bowen Zhou. Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. *arXiv preprint arXiv:2502.06703*, 2025.
971	
972	Liangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, et al. Improve Mathematical Reasoning in Language Models by Automated Process Supervision. *arXiv preprint arXiv:2406.06592*, 2024.
973	
974	Aman Madaan, Niket Tandon, Prakash Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegr-effe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-Refine: Iterative Refinement with Self-Feedback. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46534–46594. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf).
975	
976	Dakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative Reward Models. *arXiv preprint arXiv:2410.12832*, 2024.
977	
978	OpenAI. GPT-4 Technical Report. *arXiv preprint arXiv:2303.08774*, 2023.
979	
980	OpenAI. Learning to reason with LLMs, 2024a. URL &lt;https://openai.com/index/learning-to-reason-with-llms>.
981	
982	OpenAI. OpenAI o3-mini, 2024b. URL &lt;https://openai.com/index/openai-o3-mini>.
983	
984	Qwen Team. QwQ-32B: Embracing the Power of Reinforcement Learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b>.Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=A6Y7AqlzLW>.
985	
986	Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*, 2024.
987	
988	Skywork o1 Team. Skywork-o1 Open Series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.
989	
990	Charlie Victor Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=4FWAwZtd2n>.
991	
992	Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, and Yu Cheng. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models. *arXiv preprint arXiv:2501.03124*, 2025.
993	
994	Xiaoyu Tan, Tianchu Yao, Chao Qu, Bin Li, Minghao Yang, Dakuan Lu, Haozhe Wang, Xihe Qiu, Wei Chu, Yinghui Xu, et al. AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification. *arXiv preprint arXiv:2502.11520*, 2025.
995	
996	Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.
997	
998	Jun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. OpenR: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024a.
999	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9577c7bb-6a33-484f-b5ca-8c3e9c91953e",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "f74ec7da-9017-44d4-8702-ae160a20a097",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt",
      "content": "&lt;td>46.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.1&lt;/td>\n&lt;td>17.9&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>33.0&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>50.6&lt;/td>\n&lt;td>6.3&lt;/td>\n&lt;td>77.7&lt;/td>\n&lt;td>34.7&lt;/td>\n&lt;td>42.3&lt;/td>\n&lt;td>46.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>74.1&lt;/b>&lt;/td>\n&lt;td>&lt;b>19.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>53.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>57.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>8.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>45.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>49.8&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 2&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>18.0&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>31.6&lt;/td>\n&lt;td>50.3&lt;/td>\n&lt;td>49.8&lt;/td>\n&lt;td>8.0&lt;/td>\n&lt;td>76.9&lt;/td>\n&lt;td>31.8&lt;/td>\n&lt;td>41.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>70.9&lt;/td>\n&lt;td>18.3&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.5&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>7.9&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>75.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>21.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>54.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>59.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>35.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>46.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>50.7&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"12\" style=\"text-align: center;\">&lt;i>Turn 3&lt;/i>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Generator&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>18.1&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>32.1&lt;/td>\n&lt;td>50.8&lt;/td>\n&lt;td>49.7&lt;/td>\n&lt;td>8.1&lt;/td>\n&lt;td>77.1&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>41.4&lt;/td>\n&lt;td>46.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1-Distill-7B&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;td>18.8&lt;/td>\n&lt;td>85.0&lt;/td>\n&lt;td>33.4&lt;/td>\n&lt;td>51.7&lt;/td>\n&lt;td>51.9&lt;/td>\n&lt;td>8.3&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>32.7&lt;/td>\n&lt;td>42.7&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GenPRM-7B&lt;/td>\n&lt;td>&lt;b>76.2&lt;/b>&lt;/td>\n&lt;td>&lt;b>22.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>86.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>36.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>55.4&lt;/b>&lt;/td>\n&lt;td>&lt;b>62.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>9.3&lt;/b>&lt;/td>\n&lt;td>&lt;b>82.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>34.9&lt;/b>&lt;/td>\n&lt;td>&lt;b>47.5&lt;/b>&lt;/td>\n&lt;td>&lt;b>51.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Pass@1. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>72.9&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;td>&lt;b>73.2&lt;/b>&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>73.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>77.3&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>76.8&lt;/td>\n&lt;td>79.6&lt;/td>\n&lt;td>71.1&lt;/td>\n&lt;td>69.0&lt;/td>\n&lt;td>74.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>75.8&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;td>72.8&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>68.7&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>75.7&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>70.4&lt;/td>\n&lt;td>68.5&lt;/td>\n&lt;td>73.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>&lt;b>78.7&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.3&lt;/b>&lt;/td>\n&lt;td>72.2&lt;/td>\n&lt;td>&lt;b>69.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>75.2&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>77.4&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>72.3&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4:** Results of GenPRM with different label estimation method and threshold on ProcessBench, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Estimation Method&lt;/th>\n&lt;th>Positive Label Criterion&lt;/th>\n&lt;th>GSM8K&lt;/th>\n&lt;th>MATH&lt;/th>\n&lt;th>Olympiad Bench&lt;/th>\n&lt;th>Omni-MATH&lt;/th>\n&lt;th>Avg.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;math>P_t = MC(s_t, a_t)&lt;/math> (hard label)&lt;/td>\n&lt;td>&lt;math>P_t &gt; 0&lt;/math>&lt;/td>\n&lt;td>75.1&lt;/td>\n&lt;td>83.8&lt;/td>\n&lt;td>&lt;b>80.6&lt;/b>&lt;/td>\n&lt;td>74.4&lt;/td>\n&lt;td>78.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">&lt;math>P_t = MC(s_t, a_t) - MC(s_t)&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq -0.1&lt;/math>&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>74.5&lt;/td>\n&lt;td>79.4&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.3&lt;/math>&lt;/td>\n&lt;td>80.9&lt;/td>\n&lt;td>&lt;b>86.5&lt;/b>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.0&lt;/td>\n&lt;td>80.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq -0.5&lt;/math>&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;td>73.4&lt;/td>\n&lt;td>79.1&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">&lt;math>P_t = \\frac{MC(s_t, a_t)}{MC(s_t)}&lt;/math>&lt;/td>\n&lt;td>&lt;math>P_t \\geq 0.1&lt;/math>&lt;/td>\n&lt;td>77.0&lt;/td>\n&lt;td>84.6&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.3&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.5&lt;/math>&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>78.2&lt;/td>\n&lt;td>74.3&lt;/td>\n&lt;td>78.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 0.8&lt;/math>&lt;/td>\n&lt;td>81.0&lt;/td>\n&lt;td>85.7&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;math>P_t \\geq 1.0&lt;/math>&lt;/td>\n&lt;td>&lt;b>81.1&lt;/b>&lt;/td>\n&lt;td>84.1&lt;/td>\n&lt;td>76.0&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>79.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Reasoning Components.** To understand how each reasoning component influence GenPRM, we conduct experiments by training GenPRM with: (1) CoT data only, (2) code verification data only, and (3) full data. During inference phase, we also compare several variants. For example, GenPRM trained with full data can be used to only verify each step with CoT only by stopping generation at `&lt;/analyze>` token. The results in Table 5 show that: (1) the improvement of GenPRM mainly comesfrom CoT reasoning; (2) generating code and reasoning with code execution result improves the process verification performance as well.\n\n**Table 5:** Results on ProcessBench of GenPRM with different reasoning components, reported with Maj@8. The best results are shown in **bold**.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th colspan=\"2\">Training&lt;/th>\n&lt;th colspan=\"3\">Inference&lt;/th>\n&lt;th rowspan=\"2\">GSM8K&lt;/th>\n&lt;th rowspan=\"2\">MATH&lt;/th>\n&lt;th rowspan=\"2\">Olympiad Bench&lt;/th>\n&lt;th rowspan=\"2\">Omni-MATH&lt;/th>\n&lt;th rowspan=\"2\">Avg.&lt;/th>\n&lt;/tr>\n&lt;tr>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>CoT&lt;/th>\n&lt;th>Code&lt;/th>\n&lt;th>Code Exec.&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>65.8&lt;/td>\n&lt;td>54.5&lt;/td>\n&lt;td>55.9&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>67.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>57.4&lt;/td>\n&lt;td>64.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>76.6&lt;/td>\n&lt;td>67.3&lt;/td>\n&lt;td>63.9&lt;/td>\n&lt;td>69.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>83.0&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;td>75.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td rowspan=\"5\">✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>60.1&lt;/td>\n&lt;td>66.7&lt;/td>\n&lt;td>59.9&lt;/td>\n&lt;td>59.2&lt;/td>\n&lt;td>61.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>x&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>61.3&lt;/td>\n&lt;td>74.7&lt;/td>\n&lt;td>68.1&lt;/td>\n&lt;td>62.0&lt;/td>\n&lt;td>66.5&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.7&lt;/td>\n&lt;td>74.9&lt;/td>\n&lt;td>79.3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>x&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>85.1&lt;/td>\n&lt;td>78.1&lt;/td>\n&lt;td>75.5&lt;/td>\n&lt;td>79.9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>&lt;b>81.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>85.7&lt;/b>&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>&lt;b>76.8&lt;/b>&lt;/td>\n&lt;td>&lt;b>80.5&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## 5. Related Work\n\n**Process Reward Models.** Process reward models have been proved to be effective for providing step-wise scores and are superior to outcome reward models in mathematical reasoning tasks (Uesato et al., 2022; Lightman et al., 2024). However, annotating a process supervision dataset such as PRM800K (Lightman et al., 2024) requires significant human costs. To mitigate this cost, prior works utilize Monte Carlo estimation (Wang et al., 2024b) and binary search (Luo et al., 2024) for automated label generation. Subsequent research improves PRMs through methods such as advantage modeling (Setlur et al., 2025),  $Q$ -value rankings (Li and Li, 2025), implicit entropy regularization (Zhang et al., 2024a), retrieval-augmented generation (Zhu et al., 2025), and fast-slow verification (Zhong et al., 2025). Furthermore, the community has developed high-quality open-source PRMs, including the RLHFlow series (Xiong et al., 2024), Math-psa (Wang et al., 2024a), Skywork series (Skywork o1 Team, 2024), and Qwen2.5-Math series (Zheng et al., 2024; Zhang et al., 2025c). Recently, a line of works focus on extending PRMs to other tasks, including coding (Zhang et al., 2024b), medical tasks (Jiang et al., 2025), agentic tasks (Choudhury, 2025), general domain tasks (Zhang et al., 2025a; Zeng et al., 2025), and multimodal tasks (Wang et al., 2025). Current studies also focus on benchmarking PRMs (Zheng et al., 2024; Song et al., 2025) to systematically evaluate their performance.\n\n**Large Language Model Test-Time Scaling.** Scaling test-time computation is an effective method for improving performance during the inference phase (OpenAI, 2024a,b; DeepSeek-AI et al., 2025). TTS is commonly implemented with external verifiers (e.g., ORMs and PRMs) or strategies (e.g., beam search and MCTS) (Wu et al., 2025; Snell et al., 2025; Beeching et al., 2024; Liu et al., 2025). In this work, we scale the test-time computation of a generative PRM with an explicit reasoning process and GenPRM can also serve as a verifier or a critic model in external TTS.\n\n**Enhancing the Generative Abilities of Reward Models.** Previous research has investigated methods to enhance the generative capabilities of reward models using CoT reasoning (Ankner et al., 2024; Zhang et al., 2025b; Mahan et al., 2024). For instance, CCloud reward models (Ankner et al., 2024) are trained to generate critiques for responses and predict rewards using an additional rewardhead. GenRM-CoT (Zhang et al., 2025b) and GenRM (Mahan et al., 2024) train generative reward models that perform CoT reasoning before making final predictions via SFT and preference learning, respectively. CTRL (Xie et al., 2025) demonstrates that critic models exhibit strong discriminative abilities when utilized as generative reward models. Prior to these works, GRM (Yang et al., 2024c) regularizes the hidden states of reward models with a text generation loss.\n\n## 6. Conclusion\n\nIn this work, we propose GenPRM, a generative process reward model that performs explicit reasoning and code verification for process supervision and enables scaling the test-time compute of PRMs. Experimental results on ProcessBench and several mathematical datasets show GenPRM outperforms prior PRMs. We also demonstrate that the performance of GenPRM increases via test-time scaling and GenPRM is effective as a critic model. We believe that this work provides perspectives on PRMs by demonstrating the strong TTS abilities of PRMs and extending the applications of PRMs.\n\n**Limitations.** First, GenPRM provides process supervision by generative reasoning, which introduces additional computation during inference phase. Future work will investigate how to prune the reasoning process dynamically (Zhong et al., 2025). Although GenPRM focuses mainly on mathematical reasoning tasks, it is worth to explore how to apply generative reasoning on coding and general reasoning tasks in the future (Zhang et al., 2025a). Additionally, it would be interesting to leverage RL to incentivize the generative reasoning abilities of GenPRM.\n\n## References\n\nAI-MO. AIME 2024, 2024a. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-aimo>.\n\nAI-MO. AMC 2023, 2024b. URL &lt;https://huggingface.co/datasets/AI-MO/aimo-validation-amc>.\n\nZachary Ankner, Mansheej Paul, Brandon Cui, Jonathan D Chang, and Prithviraj Ammanabrolu. Critique-out-Loud Reward Models. *arXiv preprint arXiv:2408.11791*, 2024.\n\nAnthropic. Introducing Claude, 2023. URL &lt;https://www.anthropic.com/index/introducing-claude/>.\n\nEdward Beeching, Lewis Tunstall, and Sasha Rush. Scaling Test-Time Compute with Open Models, 2024. URL &lt;https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute>.\n\nBradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. *arXiv preprint arXiv:2407.21787*, 2024.\n\nSanjiban Choudhury. Process Reward Models for LLM Agents: Practical Framework and Directions. *arXiv preprint arXiv:2502.10325*, 2025.\n\nGanqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Wendi Li, Bingxiang He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, et al. Process Reinforcement through Implicit Rewards. *arXiv preprint arXiv:2502.01456*, 2025.DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. *arXiv preprint arXiv:2501.12948*, 2025.\n\nGemma Team and Google DeepMind. Introducing Gemma 3: The most capable model you can run on a single GPU or TPU, March 2025. URL &lt;https://blog.google/technology/developers/gemma-3>.\n\nZhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen, Yujiu Yang, Nan Duan, and Weizhu Chen. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=Sx038qxjek>.\n\nDan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob Steinhardt. Measuring Mathematical Problem Solving With the MATH Dataset. In *Advances in Neural Information Processing Systems Datasets and Benchmarks Track (Round 2)*, 2021. URL &lt;https://openreview.net/forum?id=7Bywt2mQsCe>.\n\nShuyang Jiang, Yusheng Liao, Zhe Chen, Ya Zhang, Yanfeng Wang, and Yu Wang. MedS&lt;sup>3&lt;/sup>: Towards Medical Small Language Models with Self-Evolved Slow Thinking. *arXiv preprint arXiv:2501.12051*, 2025.\n\nAitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving Quantitative Reasoning Problems with Language Models. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors,*Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 3843–3857. Curran Associates, Inc., 2022. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2022/file/18abbeef8cfe9203fdf9053c9c4fe191-Paper-Conference.pdf).\n\nWendi Li and Yixuan Li. Process Reward Model with Q-value Rankings. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=wQEdh2cgEk>.\n\nHunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s Verify Step by Step. In *International Conference on Learning Representations (ICLR)*, 2024. URL &lt;https://openreview.net/forum?id=v8L0pN6E0i>.\n\nRunze Liu, Fengshuo Bai, Yali Du, and Yaodong Yang. Meta-Reward-Net: Implicitly Differentiable Reward Learning for Preference-based Reinforcement Learning. In *Advances in Neural Information Processing Systems (NeurIPS)*, volume 35, pages 22270–22284, 2022.\n\nRunze Liu, Yali Du, Fengshuo Bai, Jiafei Lyu, and Xiu Li. PEARL: Zero-shot Cross-task Preference Alignment and Robust Reward Learning for Robotic Manipulation. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp, editors, *International Conference on Machine Learning (ICML)*, volume 235 of *Proceedings of Machine Learning Research*, pages 30946–30964. PMLR, 21–27 Jul 2024. URL &lt;https://proceedings.mlr.press/v235/liu24o.html>.\n\nRunze Liu, Junqi Gao, Jian Zhao, Kaiyan Zhang, Xiu Li, Biqing Qi, Wanli Ouyang, and Bowen Zhou. Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. *arXiv preprint arXiv:2502.06703*, 2025.\n\nLiangchen Luo, Yinxiao Liu, Rosanne Liu, Samrat Phatale, Harsh Lara, Yunxuan Li, Lei Shu, Yun Zhu, Lei Meng, Jiao Sun, et al. Improve Mathematical Reasoning in Language Models by Automated Process Supervision. *arXiv preprint arXiv:2406.06592*, 2024.\n\nAman Madaan, Niket Tandon, Prakash Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegr-effe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-Refine: Iterative Refinement with Self-Feedback. In A. Oh, T. Nau-mann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, *Advances in Neural Information Processing Systems (NeurIPS)*, volume 36, pages 46534–46594. Curran Associates, Inc., 2023. URL [https://proceedings.neurips.cc/paper\\\\_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf](https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf).\n\nDakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative Reward Models. *arXiv preprint arXiv:2410.12832*, 2024.\n\nOpenAI. GPT-4 Technical Report. *arXiv preprint arXiv:2303.08774*, 2023.\n\nOpenAI. Learning to reason with LLMs, 2024a. URL &lt;https://openai.com/index/learning-to-reason-with-llms>.\n\nOpenAI. OpenAI o3-mini, 2024b. URL &lt;https://openai.com/index/openai-o3-mini>.\n\nQwen Team. QwQ-32B: Embracing the Power of Reinforcement Learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b>.Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=A6Y7AqlzLW>.\n\nZhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*, 2024.\n\nSkywork o1 Team. Skywork-o1 Open Series. &lt;https://huggingface.co/Skywork>, November 2024. URL &lt;https://huggingface.co/Skywork>.\n\nCharlie Victor Snell, Jaehoon Lee, Kelvin Xu, and Aviral Kumar. Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning. In *International Conference on Learning Representations (ICLR)*, 2025. URL &lt;https://openreview.net/forum?id=4FWAwZtd2n>.\n\nMingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, and Yu Cheng. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models. *arXiv preprint arXiv:2501.03124*, 2025.\n\nXiaoyu Tan, Tianchu Yao, Chao Qu, Bin Li, Minghao Yang, Dakuan Lu, Haozhe Wang, Xihe Qiu, Wei Chu, Yinghui Xu, et al. AURORA: Automated Training Framework of Universal Process Reward Models via Ensemble Prompting and Reverse Verification. *arXiv preprint arXiv:2502.11520*, 2025.\n\nJonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. *arXiv preprint arXiv:2211.14275*, 2022.\n\nJun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. OpenR: An open source framework for advanced reasoning with large language models. *arXiv preprint arXiv:2410.09671*, 2024a.\n",
      "numLines": 500,
      "startLine": 500,
      "totalLines": 2164
    }
  },
  "sourceToolAssistantUUID": "9577c7bb-6a33-484f-b5ca-8c3e9c91953e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-27T15:58:00.361Z_

<details open><summary>🔧 Tool call — Read · `toolu_015JG8FJ33Wt6o1onWjJ9hee`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu-idea-review/6fd3beeb-b487-48e2-ab3c-35d10e133c80/tool-results/toolu_01M8wCs4hexzqjE5QNDLnYzA.txt",
  "limit": 500,
  "offset": 1000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f74ec7da-9017-44d4-8702-ae160a20a097",
  "isSidechain": false,
  "requestId": "req_011CbTMCaNAx6gQDypmiv8hp",
  "type": "assistant",
  "uuid": "b2fe4c50-b8d0-425a-a60f-1942b9c7e82c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzWaqbr3FpeJ57YC39u23x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 17372,
      "output_tokens": 450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 450,
          "cache_read_input_tokens": 17372,
          "cache_creation_input_tokens": 246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 246
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "3b1307ad-fb67-456a-be28-faa3d47995d9",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper for research innovation",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Assistant

_source line 47 · 2026-05-27T15:58:26.132Z_

<details><summary>Logged reasoning block</summary>

```text
I now have extensive information about the paper. Let me also check for any remaining content I might have missed - specifically the conclusion section and any AAAI-specific review information. But I think I have enough now to construct the analysis.

Let me now synthesize everything I've learned:

**Paper Overview:**
GenPRM redefines process reward modeling from a discriminative task to a generative reasoning task. Instead of outputting a scalar value, it performs chain-of-thought reasoning with code verification before judging each step.

**Key Technical Contributions:**
1. **Generative PRM formulation**: Instead of training a classifier (discriminative PRM) or direct generative PRM (just predict Yes/No), they add explicit CoT reasoning + code verification before the judgment


2. **Relative Progress Estimation (RPE)**: A new labeling scheme that measures whether a step makes relative progress toward the answer, computed as the ratio of successful continuations from that step versus all continuations from the initial state
3. **Rationale synthesis with code verification**: Using QwQ-32B to generate reasoning traces with code verification, then filtering through consensus and RPE labels
4. **Test-time scaling of PRMs themselves**: Since GenPRM is generative, sampling multiple verification paths and aggregating results via majority voting

**Key Results:**
- Trained on just 23K examples from the MATH dataset
- GenPRM-1.5B outperforms GPT-4o on ProcessB (63.4 vs 61.9 avg F1 with Maj@8)
- GenPRM-7B surpasses Qwen2.5-Math-PRM-72B (80.5 vs 78.3 avg F1 with Maj@8)
- Demonstrates 3.4x greater performance gains than DeepSeek-R1-Distill-Qwen-7B in critic capabilities

**Innovation Analysis:**

1. **Problem Identification**: They pinpointed three core limitations: classifier-based PRMs struggle with generalization, scalar predictions underutilize LLM generation capabilities, and discriminative approaches can't leverage test-time scaling. The breakthrough was recognizing that treating PRMs as classifiers leaves generative potential untapped.

2. **Key Insight**: The core realization was...

The real innovation here is reframing process verification as a reasoning task rather than classification—by having the PRM generate reasoning chains and code before making a judgment, they unlock both pretrained reasoning abilities and enable test-time scaling through multiple verification paths.

3. **Innovation Type**: Fundamentally a reformulation that shifts PRMs from classification to generation, layering in CoT reasoning, code verification, and relative progress estimation.

4. **What makes it compelling**: Achieves strong data efficiency with just 23K examples, delivers dramatic scaling where a 1.5B model outperforms GPT-4o, presents a clean and well-motivated framework, and opens new possibilities like test-time scaling for PRMs and dual-use as both verifier and critic.

5. **Building blocks**: Monte Carlo estimation, step forcing, chain-of-thought reasoning, code verification, consensus filtering, supervised fine-tuning, all built on DeepSeek-R1-Distill base.

The main tradeoffs are higher inference costs, the focus being limited to math problems, and RL training remaining unexplored. Now I'm putting together the JSON analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b1307ad-fb67-456a-be28-faa3d47995d9",
  "isSidechain": false,
  "requestId": "req_011CbTMCyQ1aH42vaXAamgzZ",
  "type": "assistant",
  "uuid": "fca8bf4c-672f-4cbb-8537-63167750d725",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LccKVMrMJ15LJSrqy6wF1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33138,
      "cache_read_input_tokens": 17618,
      "output_tokens": 977,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 977,
          "cache_read_input_tokens": 17618,
          "cache_creation_input_tokens": 33138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33138
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

_source line 48 · 2026-05-27T15:58:26.134Z_

Now I have comprehensive content from the paper. Let me also try to find AAAI reviewer comments:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fca8bf4c-672f-4cbb-8537-63167750d725",
  "isSidechain": false,
  "requestId": "req_011CbTMCyQ1aH42vaXAamgzZ",
  "type": "assistant",
  "uuid": "ab76db54-0424-425f-b12d-8064d9310f04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LccKVMrMJ15LJSrqy6wF1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33138,
      "cache_read_input_tokens": 17618,
      "output_tokens": 977,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 977,
          "cache_read_input_tokens": 17618,
          "cache_creation_input_tokens": 33138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33138
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

_source line 49 · 2026-05-27T15:58:26.348Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011jKHsqCrBPhUsNQvbCjWpp`</summary>

```json
{
  "url": "https://openreview.net/search?term=GenPRM+Process+Reward&venue=AAAI.cc/2026",
  "prompt": "Search for the paper GenPRM about Process Reward Models. Extract any reviewer comments, scores, or author responses. If no results found, say so."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab76db54-0424-425f-b12d-8064d9310f04",
  "isSidechain": false,
  "requestId": "req_011CbTMCyQ1aH42vaXAamgzZ",
  "type": "assistant",
  "uuid": "b9e5dd55-b88e-48da-ab92-95e6f1352e5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LccKVMrMJ15LJSrqy6wF1q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33138,
      "cache_read_input_tokens": 17618,
      "output_tokens": 977,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 977,
          "cache_read_input_tokens": 17618,
          "cache_creation_input_tokens": 33138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33138
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

_source line 50 · 2026-05-27T15:58:28.347Z_

<details><summary>↩ Tool result · `toolu_011jKHsqCrBPhUsNQvbCjWpp`</summary>

```text
Based on the web page content provided, I cannot find any information about a paper called "GenPRM" or any reviewer comments, scores, or author responses related to Process Reward Models.

The content shown is primarily the OpenReview.net homepage with navigation links, footer information, and general site descriptions. It does not contain search results or details about specific papers.

To locate this paper and its reviews, you would need to use the search functionality on the OpenReview website directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9e5dd55-b88e-48da-ab92-95e6f1352e5f",
  "isSidechain": false,
  "promptId": "3f1e98cf-fe84-4c53-a39a-388c5e8388c9",
  "type": "user",
  "uuid": "651d6108-042d-4701-9eec-f70b8a2035ef",
  "toolUseResult": {
    "bytes": 62341,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the web page content provided, I cannot find any information about a paper called \"GenPRM\" or any reviewer comments, scores, or author responses related to Process Reward Models.\n\nThe content shown is primarily the OpenReview.net homepage with navigation links, footer information, and general site descriptions. It does not contain search results or details about specific papers.\n\nTo locate this paper and its reviews, you would need to use the search functionality on the OpenReview website directly.",
    "durationMs": 1989,
    "url": "https://openreview.net/search?term=GenPRM+Process+Reward&venue=AAAI.cc/2026"
  },
  "sourceToolAssistantUUID": "b9e5dd55-b88e-48da-ab92-95e6f1352e5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-27T15:58:31.037Z_

<details><summary>Logged reasoning block</summary>

```text
AAAI reviews are not on OpenReview, so I won't be able to get reviewer comments. AAAI typically uses its own review system. Let me now compose the final analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "651d6108-042d-4701-9eec-f70b8a2035ef",
  "isSidechain": false,
  "requestId": "req_011CbTMF2nDUSNVVmQRouDVt",
  "type": "assistant",
  "uuid": "d0ea1019-bd7d-486e-9ae0-838aa6f9d06d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014PS6E5En7cVD9fmTH4bQ7f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 50756,
      "output_tokens": 1781,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1089,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1781,
          "cache_read_input_tokens": 50756,
          "cache_creation_input_tokens": 1089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1089
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

_source line 52 · 2026-05-27T15:59:15.623Z_

I now have all the information I need. AAAI doesn't use OpenReview, so reviewer comments aren't publicly available. Let me now produce the deep analysis.

```json
{
  "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
  "venue": "AAAI 2026",
  "problem_identification": "The authors identified that existing PRMs are fundamentally limited by being trained as classifiers (outputting scalar scores), which (1) wastes the generative capabilities of the underlying LLM backbone, (2) prevents PRMs from benefiting from test-time scaling (you can't sample multiple reasoning paths from a scalar head), and (3) limits generalization across models and tasks. They found this gap by observing the asymmetry between how policy models (which benefit enormously from test-time scaling) and verifiers (which are frozen classifiers) are treated — a structural bottleneck hiding in plain sight within the TTS pipeline.",
  "key_insight": "Process verification is fundamentally a reasoning task, not a classification task. By making the PRM 'think before judging' — generating explicit chain-of-thought analysis and executable code verification before emitting a Yes/No token — you unlock the same test-time scaling benefits for verifiers that policy models already enjoy, and you can distill this capability into tiny models because the reasoning is explicit rather than compressed into a scalar.",
  "innovation_type": "new_formulation",
  "method_summary": "GenPRM reformulates step-level process verification from discriminative scoring to generative reasoning. For each reasoning step, the model generates a CoT analysis (wrapped in &lt;analyze> tags), then synthesizes Python code to numerically verify claims (wrapped in &lt;verify> tags), executes the code, and only then predicts Yes/No. Training data is constructed via a three-stage pipeline: (1) Monte Carlo rollout estimation of step correctness using dynamic sampling budgets (32-128 completions based on problem difficulty), (2) Relative Progress Estimation (RPE) — labeling a step as correct only if MC(s_{t+1})/MC(s_t) ≥ 0.8, measuring whether the step makes relative progress rather than just absolute correctness, and (3) rationale synthesis using QwQ-32B with code verification, filtered by consensus between RPE labels and LLM-as-judge labels (~51% of data discarded). The final 23K training examples are used for SFT on DeepSeek-R1-Distill base models. At inference, test-time scaling is achieved by sampling N verification paths per step and aggregating via majority voting.",
  "what_makes_it_good": "Three things likely clinched acceptance: (1) extraordinary data efficiency — 23K examples beating models trained on 344K+ examples, with a 1.5B model outperforming GPT-4o, which is the kind of eye-catching result that demands explanation; (2) conceptual elegance — the paper doesn't just add a technique, it reframes the entire PRM paradigm and shows this reframing has cascading benefits (TTS for verifiers, dual verifier/critic use, better generalization); (3) thorough ablations dissecting every component (RPE thresholds, CoT vs. code contributions, model/data scaling) that demonstrate genuine understanding rather than lucky hyperparameter choices.",
  "limitations_acknowledged": "The authors note three limitations: (1) GenPRM's generative reasoning introduces significant additional inference computation compared to scalar PRMs, (2) the work focuses exclusively on mathematical reasoning and hasn't been validated on coding or general reasoning tasks, and (3) they haven't explored using RL to further improve the generative reasoning abilities (only SFT was used).",
  "open_questions": [
    "Can the generative PRM paradigm transfer to domains without easily executable verification code (e.g., commonsense reasoning, ethical judgment, open-ended writing), where the code-verification component that provides ~5-6% of the gains would be unavailable?",
    "The consensus filtering discards 51% of training data — is this aggressive filtering the secret sauce (high data quality) or a limitation (wasted compute)? Could iterative self-improvement or RL on the filtered-out data recover additional signal?",
    "RPE uses a fixed threshold ε=0.8 across all problems — could adaptive thresholds (per difficulty level or per step position) further improve label quality, and what is the theoretical justification for the ratio form vs. difference form of relative progress?"
  ],
  "building_blocks": [
    "Monte Carlo rollout estimation for step-level labels (from Math-Shepherd)",
    "DeepSeek-R1-Distill series as reasoning-capable base models (1.5B, 7B, 32B)",
    "QwQ-32B as a rationale synthesis teacher model",
    "Step forcing for structured solution generation",
    "Consensus filtering between MC-derived labels and LLM-as-judge labels",
    "Code execution sandbox for runtime verification during both training data generation and inference",
    "MATH dataset (7.5K problems as the seed problem set)",
    "ProcessBench for step-level verification evaluation",
    "Majority voting over generative verification paths for TTS",
    "Relative advantage estimation concept adapted from GRPO/DeepSeek-R1"
  ],
  "reviewer_feedback_summary": null,
  "relevance_to_seed": "This paper is directly at the frontier of our research area — it proposes the most significant paradigm shift in PRM design since Math-Shepherd's automated labeling. The key lesson for our research is that reformulating verification as generation (rather than classification) is a multiplier: it simultaneously solves data efficiency, generalization, and scalability problems. The RPE labeling method and consensus filtering pipeline are immediately reusable building blocks, and the paper's success with only 23K examples suggests that the bottleneck in PRM research has been formulation quality, not data quantity."
}
```

## Key Takeaways for Research Craft

**What we can learn from HOW this paper innovates:**

1. **Identify structural asymmetries**: The authors noticed that policy models get test-time scaling benefits but verifiers don't — this asymmetry was a signal that the verifier formulation was suboptimal. Looking for such asymmetries in pipelines is a powerful research heuristic.

2. **Reformulation > accumulation**: Rather than building a better classifier PRM (the incremental path), they asked "should PRMs be classifiers at all?" This yielded 10x more impact than any architectural tweak could have.

3. **Borrow ideas across abstraction levels**: RPE borrows the relative advantage idea from GRPO (a policy optimization method) and applies it to label estimation — a cross-level transfer that others missed because PRM labeling and policy training are usually studied by different subcommunities.

4. **Quality filtering as a force multiplier**: The consensus filtering (discarding 51% of data) is brutal but effective. The paper shows that 23K clean examples > 344K noisy examples — a reminder that data curation deserves as much engineering attention as model architecture.

5. **Stack cheap verification signals**: CoT reasoning alone accounts for most gains (~78.8 avg), but adding code verification pushes to 80.5 — a modest but meaningful increment that makes the system more robust on hard problems. The lesson: layering complementary verification modalities compounds reliability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0ea1019-bd7d-486e-9ae0-838aa6f9d06d",
  "isSidechain": false,
  "requestId": "req_011CbTMF2nDUSNVVmQRouDVt",
  "type": "assistant",
  "uuid": "bc339fbe-7e1b-4715-9347-3ede11ec3074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014PS6E5En7cVD9fmTH4bQ7f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1089,
      "cache_read_input_tokens": 50756,
      "output_tokens": 1781,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1089,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1781,
          "cache_read_input_tokens": 50756,
          "cache_creation_input_tokens": 1089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1089
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing a deep analysis of a published paper.  **Today's date: 2026-05-27 (UTC).**  ## Your goal  Analyze this paper NOT just for what it does, but for **HOW it innov…",
  "leafUuid": "bc339fbe-7e1b-4715-9347-3ede11ec3074",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze GenPRM paper for research innovation",
  "sessionId": "6fd3beeb-b487-48e2-ab3c-35d10e133c80"
}
```

---
